"""Build source-token counting from the installed Ollama Llama 3 GGUF vocabulary."""
import hashlib
import inspect
import json
import re
from pathlib import Path

MODEL_DIGEST = '46e0c10c039e019119339687c3c1757cc81b9da49709a3b3924863ba87ca666e'


def sha256_file(path):
    digest = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(4 * 1024 * 1024), b''):
            digest.update(block)
    return digest.hexdigest()


def model_files(models_root):
    root = models_root.resolve()
    manifest = root/'manifests/registry.ollama.ai/library/llama3.1/8b'
    raw = manifest.read_bytes()
    if hashlib.sha256(raw).hexdigest() != MODEL_DIGEST:
        raise ValueError('Installed Llama manifest differs from the recorded development model.')
    layers = [item for item in json.loads(raw)['layers']
              if item['mediaType'] == 'application/vnd.ollama.image.model']
    if len(layers) != 1 or not re.fullmatch(r'sha256:[0-9a-f]{64}', layers[0]['digest']):
        raise ValueError('Expected one model layer with a valid SHA-256 digest.')
    blob = root/'blobs'/layers[0]['digest'].replace(':', '-')
    if not blob.resolve().is_relative_to(root):
        raise ValueError('Model layer path escapes the model directory.')
    if blob.stat().st_size != layers[0]['size']:
        raise ValueError('Installed model layer size differs from its manifest.')
    return blob, layers[0]['digest'].split(':')[1]


def read_metadata(blob):
    # GGUFReader memory maps the file; no model tensors are decoded or loaded.
    from gguf import GGUFReader
    from transformers.integrations.ggml import _gguf_parse_value
    reader = GGUFReader(str(blob))
    result = {}
    for key, field in reader.fields.items():
        if key == 'general.architecture' or key.startswith('tokenizer.ggml.'):
            values = [_gguf_parse_value(field.parts[index], field.types) for index in field.data]
            result[key] = values if int(field.types[0]) == 9 else values[0]
    return result


def tokenizer_from_metadata(metadata):
    from tokenizers import Regex, pre_tokenizers
    from transformers.integrations.ggml import GGUF_TOKENIZER_MAPPING, convert_gguf_tokenizer
    from transformers.convert_slow_tokenizer import TikTokenConverter
    if (metadata.get('general.architecture') != 'llama'
            or metadata.get('tokenizer.ggml.model') != 'gpt2'
            or metadata.get('tokenizer.ggml.pre') != 'llama-bpe'):
        raise ValueError('This check supports only the installed Llama 3 llama-bpe tokenizer.')
    mapping = GGUF_TOKENIZER_MAPPING['tokenizer']
    parameters = {renamed: metadata['tokenizer.'+key] for key, renamed in mapping.items()
                  if renamed and 'tokenizer.'+key in metadata}
    if not parameters.get('tokens') or not parameters.get('merges'):
        raise ValueError('Model tokenizer vocabulary or merges are missing.')
    tokenizer, _ = convert_gguf_tokenizer('llama', parameters)
    # The 4.49 GGUF converter uses GPT-2's ByteLevel splitting by default.
    # Use the Llama 3 pattern from the same pinned Transformers implementation.
    pattern = inspect.signature(TikTokenConverter.__init__).parameters['pattern'].default
    if not isinstance(pattern, str) or r'\p{N}{1,3}' not in pattern:
        raise ValueError('Pinned Transformers Llama 3 splitting pattern is unavailable.')
    tokenizer.pre_tokenizer = pre_tokenizers.Sequence([
        pre_tokenizers.Split(Regex(pattern), behavior='isolated'),
        pre_tokenizers.ByteLevel(add_prefix_space=False, use_regex=False),
    ])
    restore_llama3_decoder(tokenizer)
    return tokenizer, pattern


def restore_llama3_decoder(tokenizer):
    from tokenizers import decoders
    # The GGUF converter retains SentencePiece's leading-space removal.
    # Llama 3 uses byte-level BPE, so decoding must preserve literal spaces.
    tokenizer.decoder = decoders.ByteLevel()
    return tokenizer


def validate_roundtrip(tokenizer, text):
    ids = tokenizer.encode(text, add_special_tokens=False).ids
    if tokenizer.decode(ids, skip_special_tokens=False) != text:
        raise ValueError('Tokenizer did not preserve the probe source text exactly.')
    return ids


def validate_count(local_count, reported_count, add_bos):
    if type(reported_count) is not int or reported_count != local_count + int(add_bos):
        raise ValueError('Local source-token count disagrees with raw Ollama prompt counting.')

import hashlib
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from extraction.llama_tokenizer import model_files, restore_llama3_decoder, sha256_file, validate_count, validate_roundtrip


class LlamaTokenizerGuards(unittest.TestCase):
    def setUp(self):
        self.fixture_root = Path(__file__).resolve().parents[1]/'work/tokenizer_guard_tests'
        self.fixture_root.mkdir(parents=True, exist_ok=True)

    def test_count_rejects_nonmatching_raw_runtime_counts(self):
        validate_count(500, 501, True)
        validate_count(500, 500, False)
        for reported in [499, 502, None, '501', True]:
            with self.assertRaises(ValueError):
                validate_count(500, reported, True)

    def test_lossy_unicode_roundtrip_is_rejected(self):
        class LossyTokenizer:
            def encode(self, text, **kwargs):
                return type('Encoding', (), {'ids': [1, 2]})()
            def decode(self, ids, **kwargs):
                return 'victims devices'
        with self.assertRaises(ValueError):
            validate_roundtrip(LossyTokenizer(), 'victim’s devices')

    def test_bytelevel_decoder_preserves_leading_spaces_without_changing_ids(self):
        from tokenizers import Tokenizer, decoders, models, pre_tokenizers
        vocabulary = {symbol: i for i, symbol in enumerate(sorted(pre_tokenizers.ByteLevel.alphabet()))}
        tokenizer = Tokenizer(models.BPE(vocabulary, []))
        tokenizer.pre_tokenizer = pre_tokenizers.ByteLevel(add_prefix_space=False, use_regex=False)
        tokenizer.decoder = decoders.Sequence([decoders.ByteLevel(), decoders.Strip(' ', left=1)])
        source = '  victim’s café🙂 devices\n  '
        before = tokenizer.encode(source, add_special_tokens=False).ids
        with self.assertRaises(ValueError):
            validate_roundtrip(tokenizer, source)
        restore_llama3_decoder(tokenizer)
        self.assertEqual(validate_roundtrip(tokenizer, source), before)

    def test_manifest_binding_and_model_layer_size(self):
        with tempfile.TemporaryDirectory(dir=self.fixture_root) as tmp:
            root = Path(tmp)
            manifest = root/'manifests/registry.ollama.ai/library/llama3.1/8b'
            manifest.parent.mkdir(parents=True)
            blob_digest = 'a' * 64
            raw = json.dumps({'layers': [{'mediaType': 'application/vnd.ollama.image.model',
                                         'digest': 'sha256:'+blob_digest, 'size': 3}]}).encode()
            manifest.write_bytes(raw)
            blob = root/'blobs'/('sha256-'+blob_digest)
            blob.parent.mkdir()
            blob.write_bytes(b'abc')
            with patch('extraction.llama_tokenizer.MODEL_DIGEST', hashlib.sha256(raw).hexdigest()):
                self.assertEqual(model_files(root), (blob, blob_digest))
                blob.write_bytes(b'ab')
                with self.assertRaises(ValueError):
                    model_files(root)
            with self.assertRaises(ValueError):
                model_files(root)

    def test_streamed_blob_hash_changes_with_contents(self):
        with tempfile.TemporaryDirectory(dir=self.fixture_root) as tmp:
            blob = Path(tmp)/'model'
            blob.write_bytes(b'abc')
            self.assertEqual(sha256_file(blob), hashlib.sha256(b'abc').hexdigest())
            blob.write_bytes(b'abd')
            self.assertNotEqual(sha256_file(blob), hashlib.sha256(b'abc').hexdigest())


if __name__ == '__main__':
    unittest.main()

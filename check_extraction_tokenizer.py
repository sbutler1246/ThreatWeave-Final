"""Verify GGUF-derived source counting against raw local Ollama prompts."""
import argparse
import hashlib
import json
import os
import sys
from datetime import datetime, timezone
from importlib.metadata import version
from pathlib import Path
from uuid import uuid4

from extraction.llama_tokenizer import (
    MODEL_DIGEST, model_files, read_metadata, sha256_file,
    tokenizer_from_metadata, validate_count, validate_roundtrip,
)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', type=Path, default=Path(__file__).resolve().parent)
    parser.add_argument('--models', type=Path,
                        default=Path(os.environ.get('OLLAMA_MODELS', str(Path.home()/'.ollama/models'))))
    args = parser.parse_args()
    repo = args.repo.resolve()
    output = repo/'work/extraction_tokenizer'/(datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')+'-'+uuid4().hex[:8])
    output.mkdir(parents=True)
    summary = {'purpose': 'source_tokenizer_runtime_check', 'status': 'started',
               'model': 'llama3.1:8b', 'model_digest': MODEL_DIGEST,
               'models_root': str(args.models.resolve()), 'probes': []}
    http = None
    try:
        if (sys.version_info[:2] != (3, 12) or version('transformers') != '4.49.0'
                or version('gguf') != '0.10.0' or version('sentencepiece') != '0.2.0'):
            raise ValueError('Use Python 3.12, Transformers 4.49.0, GGUF 0.10.0 and SentencePiece 0.2.0.')
        summary['packages'] = {name: version(name) for name in ['transformers', 'tokenizers', 'gguf', 'sentencepiece', 'numpy']}
        blob, blob_digest = model_files(args.models)
        print('Checking the existing model file checksum and reading tokenizer metadata...', flush=True)
        if sha256_file(blob) != blob_digest:
            raise ValueError('Installed model file checksum differs from the manifest.')
        metadata = read_metadata(blob)
        tokenizer, pattern = tokenizer_from_metadata(metadata)
        add_bos = metadata.get('tokenizer.ggml.add_bos_token', True)
        if type(add_bos) is not bool:
            raise ValueError('Invalid model BOS-token policy.')
        summary.update(model_blob_sha256=blob_digest, add_bos_token=add_bos,
                       splitting_pattern=pattern, vocabulary_size=tokenizer.get_vocab_size())
        # Source-only probes; no benchmark answers or graph facts are used.
        manifest = json.loads((repo/'benchmarks/corpus_manifest.json').read_text(encoding='utf-8'))
        record = next(r for r in manifest['documents'] if r['doc_id'] == 'AA23-136A')
        source_path = (repo/record['text_file']).resolve()
        if not source_path.is_relative_to(repo):
            raise ValueError('Probe source path escapes the workspace.')
        source = source_path.read_text(encoding='utf-8')
        if hashlib.sha256(source.encode('utf-8')).hexdigest() != record['normalized_sha256']:
            raise ValueError('Frozen probe source checksum changed.')
        start = source.index('BianLian group actors used Rclone')
        probes = ["  Port 123456789: TCP/UDP. Can't connect.\nScan output.  ",
                  'Unicode: café, naïve, victim’s devices — MFA\r\n次の行🙂',
                  source[start:start+2500]]
        import requests
        http = requests.Session()
        http.trust_env = False
        tags = http.get('http://localhost:11434/api/tags', timeout=10)
        tags.raise_for_status()
        installed = next((m for m in tags.json()['models'] if m['name'] == 'llama3.1:8b'), None)
        if not installed or installed.get('digest') != MODEL_DIGEST:
            raise ValueError('Ollama serving model differs from the verified local manifest.')
        for number, text in enumerate(probes, 1):
            ids = validate_roundtrip(tokenizer, text)
            case = {'probe': number, 'text_sha256': hashlib.sha256(text.encode('utf-8')).hexdigest(),
                    'source_tokens': len(ids), 'expected_raw_prompt_tokens': len(ids)+int(add_bos)}
            summary['probes'].append(case)
            print(f'[{number}/{len(probes)}] Comparing source token count with Ollama...', flush=True)
            response = http.post('http://localhost:11434/api/generate', json={
                'model': 'llama3.1:8b', 'prompt': text, 'raw': True, 'stream': False,
                'options': {'temperature': 0, 'num_ctx': 8192, 'num_predict': 1},
            }, timeout=90)
            response.raise_for_status()
            value = response.json()
            (output/f'probe_{number}_ollama.json').write_text(json.dumps(value, indent=2)+'\n', encoding='utf-8')
            if not value.get('done') or value.get('error'):
                raise ValueError('Raw Ollama token-count probe did not complete.')
            case['reported_raw_prompt_tokens'] = value.get('prompt_eval_count')
            validate_count(len(ids), case['reported_raw_prompt_tokens'], add_bos)
            case['status'] = 'passed'
        tokenizer_path = output/'tokenizer.json'
        tokenizer.save(str(tokenizer_path))
        summary.update(status='ready', tokenizer_sha256=sha256_file(tokenizer_path),
                       tokenizer_file='tokenizer.json',
                       scope='Source tokens only; BOS and chat/prompt overhead are counted separately.')
    except Exception as exc:
        summary.update(status='failed', error=f'{type(exc).__name__}: {exc}')
        print('FAIL: '+summary['error'], flush=True)
    finally:
        if http is not None:
            http.close()
        summary['finished_at'] = datetime.now(timezone.utc).isoformat()
        (output/'summary.json').write_text(json.dumps(summary, indent=2, ensure_ascii=False)+'\n', encoding='utf-8')
    if summary['status'] == 'ready':
        pointer = repo/'work/extraction_tokenizer/current.json'
        temporary = pointer.with_suffix('.tmp')
        temporary.write_text(json.dumps({'run': output.name, 'model_digest': MODEL_DIGEST,
                                        'tokenizer_sha256': summary['tokenizer_sha256']}, indent=2)+'\n', encoding='utf-8')
        temporary.replace(pointer)
    lines = ['# Llama source-tokenizer check', '', 'Status: '+summary['status'], '',
             'Reads the existing Ollama model vocabulary; model weights are not loaded by the checker.',
             'Raw Ollama probes test token-count agreement and source round trips. This does not validate extraction quality.', '',
             'Records: '+str(output), '', 'Model digest: '+MODEL_DIGEST, '']
    for probe in summary['probes']:
        lines.append(f'- Probe {probe["probe"]}: local source tokens {probe["source_tokens"]}; expected raw count {probe["expected_raw_prompt_tokens"]}; reported {probe.get("reported_raw_prompt_tokens", "unavailable")}; {probe.get("status", "incomplete")}.')
    if summary.get('error'):
        lines.extend(['', 'Error: '+summary['error']])
    lines.extend(['', 'Full-corpus chunking and the five-report extraction timing/overlap pilot remain pending.', ''])
    review = repo/'docs'/('ThreatWeave_extraction_tokenizer_'+output.name+'.md')
    review.write_text('\n'.join(lines), encoding='utf-8')
    print(f'Saved setup records: {output}\nSaved review document: {review}', flush=True)
    if summary['status'] == 'ready':
        print('READY: Llama source-tokenizer round trips and raw Ollama token-count checks passed.', flush=True)
        return 0
    return 1


if __name__ == '__main__':
    raise SystemExit(main())

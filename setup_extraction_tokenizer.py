"""Install the small GGUF metadata reader and check source-token counting."""
import argparse
import subprocess
import sys
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', type=Path, default=Path(__file__).resolve().parent)
    parser.add_argument('--uv', type=Path, default=Path.home()/'.local/bin/uv.exe')
    parser.add_argument('--models', type=Path, help='Explicit Ollama model directory, overriding OLLAMA_MODELS.')
    args = parser.parse_args()
    if sys.version_info[:2] != (3, 12) or not args.uv.is_file():
        parser.error('Use the existing Python 3.12 environment and installed uv.')
    repo = args.repo.resolve()
    print('Installing GGUF 0.10.0 and its SentencePiece import dependency 0.2.0; internet access is needed.', flush=True)
    result = subprocess.run([str(args.uv), 'pip', 'install', '--python', sys.executable,
                             '--cache-dir', str(repo/'work/uv-cache'), '--link-mode', 'copy',
                             '--no-deps', 'gguf==0.10.0', 'sentencepiece==0.2.0'], cwd=repo)
    if result.returncode:
        return result.returncode
    command = [sys.executable, str(repo/'check_extraction_tokenizer.py'), '--repo', str(repo)]
    if args.models is not None:
        command.extend(['--models', str(args.models)])
    return subprocess.run(command, cwd=repo).returncode


if __name__ == '__main__':
    raise SystemExit(main())

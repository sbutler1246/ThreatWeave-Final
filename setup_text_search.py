"""Install the development text-search packages, then verify MiniLM and Chroma."""
import argparse
import subprocess
import sys
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', type=Path, default=Path(__file__).resolve().parent)
    parser.add_argument('--uv', type=Path, default=Path.home()/'.local'/'bin'/'uv.exe')
    args = parser.parse_args()
    repo = args.repo.resolve()
    if sys.version_info[:2] != (3, 12):
        parser.error('Use the existing Python 3.12 environment for this step.')
    if not args.uv.is_file():
        parser.error(f'uv was not found at {args.uv}; supply --uv with its installed path.')
    print('ThreatWeave text-search setup', flush=True)
    print(f'Python environment: {sys.executable}', flush=True)
    print('Installing pinned packages with CPU PyTorch. Internet access is needed.', flush=True)
    command = [str(args.uv), 'pip', 'install', '--python', sys.executable,
               '--cache-dir', str(repo/'work'/'uv-cache'), '--torch-backend', 'cpu',
               '-r', str(repo/'requirements-text.txt')]
    result = subprocess.run(command, cwd=repo)
    if result.returncode:
        print('Installation failed; the model check was not started.', flush=True)
        return result.returncode
    folder = repo/'work'/'text_setup'
    folder.mkdir(parents=True, exist_ok=True)
    freeze = subprocess.run([str(args.uv), 'pip', 'freeze', '--python', sys.executable],
                            cwd=repo, capture_output=True, text=True)
    if freeze.returncode:
        print(freeze.stderr, file=sys.stderr)
        return freeze.returncode
    (folder/'installed_environment.txt').write_text(freeze.stdout, encoding='utf-8')
    print('Checking the configured MiniLM revision and a local Chroma collection.', flush=True)
    return subprocess.run([sys.executable, str(repo/'check_text_setup.py'),
                           '--repo', str(repo)], cwd=repo).returncode


if __name__ == '__main__':
    raise SystemExit(main())

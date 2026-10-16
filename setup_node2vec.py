"""Install pinned graph-embedding packages and run a synthetic Node2Vec check."""
import argparse
import json
import subprocess
import sys
from pathlib import Path

from graph.node2vec_training import training_environment, training_parameters


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', type=Path, default=Path(__file__).resolve().parent)
    parser.add_argument('--uv', type=Path, default=Path.home()/'.local/bin/uv.exe')
    args = parser.parse_args()
    repo = args.repo.resolve()
    if sys.version_info[:2] != (3, 12):
        parser.error('Use the existing Python 3.12 environment.')
    if not args.uv.is_file():
        parser.error('Installed uv was not found; supply its path with --uv.')
    config = json.loads((repo/'config.json').read_text(encoding='utf-8'))
    params = training_parameters(config)
    print('ThreatWeave Node2Vec setup: installing pinned packages; internet access is needed.', flush=True)
    result = subprocess.run([str(args.uv), 'pip', 'install', '--python', sys.executable,
        '--cache-dir', str(repo/'work/uv-cache'), '--torch-backend', 'cpu',
        '-r', str(repo/'requirements-node2vec.txt')], cwd=repo)
    if result.returncode:
        print('Installation failed; Node2Vec checks were not started.', flush=True)
        return result.returncode
    folder = repo/'work/node2vec_setup'
    folder.mkdir(parents=True, exist_ok=True)
    freeze = subprocess.run([str(args.uv), 'pip', 'freeze', '--python', sys.executable],
                            cwd=repo, capture_output=True, text=True)
    if freeze.returncode:
        print(freeze.stderr, file=sys.stderr)
        return freeze.returncode
    (folder/'installed_environment.txt').write_text(freeze.stdout, encoding='utf-8')
    return subprocess.run([sys.executable, str(repo/'check_node2vec_setup.py'),
        '--repo', str(repo)], cwd=repo, env=training_environment(params)).returncode


if __name__ == '__main__':
    raise SystemExit(main())

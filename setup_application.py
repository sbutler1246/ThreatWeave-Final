"""Operator-run UI installer that refuses to change existing index dependencies."""
import argparse
import importlib.metadata
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from uuid import uuid4


def installed():
    return {d.metadata['Name']: d.version for d in importlib.metadata.distributions() if d.metadata['Name']}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', type=Path, default=Path(__file__).resolve().parent)
    parser.add_argument('--uv', type=Path, default=Path.home()/'.local/bin/uv.exe')
    args = parser.parse_args()
    repo = args.repo.resolve()
    if sys.version_info[:2] != (3, 12):
        parser.error('Use the existing ThreatWeave Python 3.12 environment.')
    if not args.uv.is_file():
        parser.error('Installed uv was not found; supply its location with --uv.')
    folder = repo/'work/application_setup'/(datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')+'-'+uuid4().hex[:8])
    folder.mkdir(parents=True)
    before = installed()
    constraints = folder/'existing_packages.txt'
    constraints.write_text(''.join(f'{k}=={v}\n' for k, v in sorted(before.items())), encoding='utf-8')
    receipt = {'purpose': 'development_application_setup', 'status': 'checking_dependencies',
               'python': sys.version, 'before': before, 'streamlit_pin': '1.66.0'}
    def save():
        (folder/'setup_receipt.json').write_text(json.dumps(receipt, indent=2)+'\n', encoding='utf-8')
    save()
    command = [str(args.uv), 'pip', 'install', '--python', sys.executable,
        '--cache-dir', str(repo/'work/uv-cache'), '--only-binary', ':all:',
        '--constraint', str(constraints), '-r', str(repo/'requirements-application.txt')]
    print('Checking UI dependencies while preserving all existing package versions...', flush=True)
    check = subprocess.run(command+['--dry-run'], cwd=repo)
    if check.returncode:
        receipt['status'] = 'dependency_check_failed'
        save()
        print('Setup stopped before installation. Existing package constraints were not relaxed.')
        return check.returncode
    print('Installing the interface packages. Internet access is required.', flush=True)
    result = subprocess.run(command, cwd=repo)
    after = installed()
    changed = {name: [version, after.get(name)] for name, version in before.items() if after.get(name) != version}
    receipt.update(after=after, changed_existing_packages=changed,
                   status='install_failed' if result.returncode else 'installed')
    save()
    if result.returncode or changed:
        print('Setup did not pass package preservation checks. See the saved receipt:', folder)
        return result.returncode or 1
    print('Running offline interface checks; Neo4j and Ollama will not be called.', flush=True)
    checked = subprocess.run([sys.executable, str(repo/'check_application_setup.py')], cwd=repo)
    receipt['status'] = 'ready' if checked.returncode == 0 else 'interface_checks_failed'
    save()
    print('Saved setup records:', folder)
    if checked.returncode == 0:
        print('READY: Interface installed, existing packages preserved, offline UI checks passed.')
    return checked.returncode


if __name__ == '__main__':
    raise SystemExit(main())

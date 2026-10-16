"""Offline UI smoke checks; never instantiates real service adapters."""
import importlib.metadata
import subprocess
import sys
from pathlib import Path


def main():
    if importlib.metadata.version('streamlit') != '1.66.0':
        print('Streamlit differs from requirements-application.txt.')
        return 1
    repo = Path(__file__).resolve().parent
    return subprocess.run([sys.executable, '-m', 'unittest', 'discover', '-s', 'tests',
                           '-p', 'test_application_ui.py', '-v'], cwd=repo).returncode


if __name__ == '__main__':
    raise SystemExit(main())

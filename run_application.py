"""Launch the development UI on localhost; no live query runs at startup."""
import importlib.metadata
import subprocess
import sys
from pathlib import Path


def main():
    try:
        version = importlib.metadata.version('streamlit')
    except importlib.metadata.PackageNotFoundError:
        print('Run setup_application.py with this Python environment first.')
        return 1
    if version != '1.66.0':
        print('Streamlit version differs from the application pin; run setup_application.py.')
        return 1
    repo = Path(__file__).resolve().parent
    try:
        return subprocess.run([sys.executable, '-m', 'streamlit', 'run', str(repo/'streamlit_app.py'),
            '--server.address=127.0.0.1', '--server.port=8501', '--server.headless=true',
            '--browser.gatherUsageStats=false', '--server.fileWatcherType=none'], cwd=repo).returncode
    except KeyboardInterrupt:
        print('\nThreatWeave stopped. Saved results remain on disk.')
        return 130


if __name__ == '__main__':
    raise SystemExit(main())

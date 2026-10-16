"""Operator-run direct ATT&CK mitigation import for the three-report extension."""
import sys

from graph.corpus_extension_mitigations import prepare
from import_corpus_pilot_mitigations import main


if __name__ == '__main__':
    try:
        sys.exit(main(preparer=prepare,output_kind='corpus_extension_mitigations',label='Three-report extension'))
    except (KeyboardInterrupt,EOFError):
        print('\nExtension mitigation import cancelled; saved previews remain available.')
        sys.exit(2)
    except Exception as error:
        print(f'FAIL: {type(error).__name__}: {error}')
        sys.exit(1)

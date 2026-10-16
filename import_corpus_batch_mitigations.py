"""Operator-run direct mitigation import for the reviewed additional development batch."""
import sys

from graph.corpus_batch_mitigations import prepare
from import_corpus_pilot_mitigations import main


if __name__ == '__main__':
    try:
        sys.exit(main(preparer=prepare, output_kind='corpus_batch_mitigations',
                      label='Additional development batch'))
    except (KeyboardInterrupt, EOFError):
        print('\nImport cancelled; saved previews remain available.')
        sys.exit(2)
    except Exception as error:
        print(f'FAIL: {type(error).__name__}: {error}')
        sys.exit(1)

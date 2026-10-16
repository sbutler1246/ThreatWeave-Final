"""Operator-run import of Supported three-report development assertions."""
import sys

from graph.corpus_extension_ingestion import prepare
from ingest_corpus_pilot import main


if __name__ == '__main__':
    try:
        sys.exit(main(preparer=prepare,output_kind='corpus_extension_ingestion',label='three-report extension'))
    except (KeyboardInterrupt,EOFError):
        print('\nExtension import cancelled; saved previews remain available.')
        sys.exit(2)
    except Exception as error:
        print(f'FAIL: {type(error).__name__}: {error}')
        sys.exit(1)

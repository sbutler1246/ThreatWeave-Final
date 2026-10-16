"""Import the supported additional-development review; never accept held candidates."""
import sys

from graph.corpus_batch_ingestion import prepare
from ingest_corpus_pilot import main


if __name__ == '__main__':
    try:
        sys.exit(main(preparer=prepare, output_kind='corpus_batch_ingestion', label='corpus batch'))
    except (KeyboardInterrupt, EOFError):
        print('\nBatch import cancelled; saved previews remain available.')
        sys.exit(2)
    except Exception as error:
        print(f'FAIL: {type(error).__name__}: {error}')
        sys.exit(1)

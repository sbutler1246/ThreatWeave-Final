"""Operator-run direct ATT&CK mitigation import for reviewed held-out sources."""
import sys
from evaluation.corpus_mitigations import prepare
from import_corpus_pilot_mitigations import main

if __name__ == '__main__':
    try:
        sys.exit(main(preparer=prepare,output_kind='evaluation_corpus_mitigations',label='Held-out evaluation corpus'))
    except (KeyboardInterrupt,EOFError):
        print('Evaluation mitigation import cancelled; saved records remain.')
        sys.exit(2)
    except Exception as error:
        print(f'FAIL: {type(error).__name__}: {error}')
        sys.exit(1)

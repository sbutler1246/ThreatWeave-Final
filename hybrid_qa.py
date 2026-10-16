"""Run full hybrid QA, requiring the separate validated Node2Vec graph index."""
import sys
from combined_qa import main


if __name__ == '__main__':
    try:
        sys.exit(main(full_hybrid=True))
    except (KeyboardInterrupt, EOFError):
        print('\nHybrid QA cancelled; existing records remain saved.')
        sys.exit(2)
    except Exception as exc:
        print(f'FAIL: {type(exc).__name__}: {exc}')
        sys.exit(1)

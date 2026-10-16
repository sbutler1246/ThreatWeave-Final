"""Build standalone browser forms from the fixed blinded human-review packet."""
from pathlib import Path
from evaluation.review_forms import build

if __name__=='__main__':build(Path(__file__).resolve().parent)

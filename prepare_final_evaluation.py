"""Prepare isolated final question inputs and audit saved evaluation graph/text assets."""
from pathlib import Path
from evaluation.experiment_plan import save_prepared

if __name__=='__main__':save_prepared(Path(__file__).resolve().parent)

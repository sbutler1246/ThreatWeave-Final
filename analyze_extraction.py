"""Score preserved source-only extraction without new model or graph calls."""
import json
from pathlib import Path
from evaluation.extraction_analysis import analyze

if __name__ == '__main__':
    folder, result = analyze(Path(__file__).resolve().parent)
    print('EXTRACTION ANALYSIS:', folder)
    print(json.dumps({key: value for key, value in result.items() if key not in
                     ['strict_pipeline', 'duplicate_normalized_sensitivity']}, indent=2))
    for label in ['strict_pipeline', 'duplicate_normalized_sensitivity']:
        print(label, json.dumps({key: result[label][key] for key in
                                ['tp', 'fp', 'fn', 'precision', 'recall', 'f1']}, indent=2))

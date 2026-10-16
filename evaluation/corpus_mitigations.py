"""Frozen direct ATT&CK references anchored to the completed evaluation import."""
from pathlib import Path

from evaluation.corpus_ingestion import prepare as prepare_predictions
from extraction.llama_tokenizer import sha256_file
from graph.corpus_pilot_mitigations import prepare as prepare_references, write_transaction

IMPORT_RUN = '20261016T042742Z-72fb42f8'


def prepare(repo):
    repo = Path(repo).resolve()
    predictions = prepare_predictions(repo)
    if (predictions.get('scope_assignment') != 'evaluation'
            or not predictions.get('evaluation_plan_fingerprint')
            or any(a.get('scope_assignment') != 'evaluation'
                   or a.get('evaluation_plan_fingerprint') != predictions['evaluation_plan_fingerprint']
                   for item in predictions['items'] for a in item['assertions'])):
        raise ValueError('Direct evaluation references require explicitly scoped source predictions.')
    payload = prepare_references(repo,prediction_preparer=lambda _:predictions,
                                 import_kind='evaluation_corpus_ingestion',import_run=IMPORT_RUN)
    source = repo/'work/evaluation_corpus_ingestion'/IMPORT_RUN
    payload.update(source_scope_assignment='evaluation',
                   evaluation_plan_fingerprint=predictions['evaluation_plan_fingerprint'],
                   source_import_receipt_sha256=sha256_file(source/'import_receipt.json'),
                   source_prepared_records_sha256=sha256_file(source/'prepared_records.json'))
    return payload

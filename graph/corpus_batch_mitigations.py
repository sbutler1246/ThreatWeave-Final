"""Direct ATT&CK 17.1 references bound to the completed additional source import."""
from graph.corpus_batch_ingestion import prepare as prepare_predictions
from graph.corpus_pilot_mitigations import prepare as prepare_references, write_transaction

IMPORT_RUN = '20261015T173114Z-643927a9'


def prepare(repo):
    return prepare_references(repo, prediction_preparer=prepare_predictions,
                              import_kind='corpus_batch_ingestion', import_run=IMPORT_RUN)

"""Direct frozen references anchored to the completed three-report source import."""
from graph.corpus_extension_ingestion import prepare as prepare_predictions
from graph.corpus_pilot_mitigations import prepare as prepare_references, write_transaction

IMPORT_RUN = '20261016T001729Z-60fdb691'


def prepare(repo):
    return prepare_references(repo, prediction_preparer=prepare_predictions,
                              import_kind='corpus_extension_ingestion', import_run=IMPORT_RUN)

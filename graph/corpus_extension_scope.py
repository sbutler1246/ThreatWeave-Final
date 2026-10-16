"""Expand accepted retrieval only from the verified three-report import receipts."""
from graph.corpus_extension_mitigations import prepare
from graph.corpus_pilot_scope import expand as expand_verified

MITIGATION_RUN = '20261016T002000Z-fd9e2fc1'


def expand(repo, profiles, references, entities):
    expand_verified(repo,profiles,references,entities,preparer=prepare,
                    mitigation_kind='corpus_extension_mitigations',mitigation_run=MITIGATION_RUN)

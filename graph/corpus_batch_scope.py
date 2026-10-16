"""Add only source and direct references bound to the completed batch receipts."""
from graph.corpus_batch_mitigations import prepare
from graph.corpus_pilot_scope import expand as expand_verified

MITIGATION_RUN = '20261015T173540Z-9792c14d'


def expand(repo, profiles, references, entities):
    expand_verified(repo, profiles, references, entities, preparer=prepare,
                    mitigation_kind='corpus_batch_mitigations', mitigation_run=MITIGATION_RUN)

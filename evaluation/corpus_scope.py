"""Receipt-bound shared evaluation evidence; development assets remain separate."""
import hashlib
import json
from pathlib import Path

from evaluation.corpus_mitigations import prepare as prepare_evaluation_references
from extraction.llama_tokenizer import sha256_file
from graph.corpus_pilot_scope import expand
from graph.development_retrieval import DevelopmentGraphRetriever, PATH_QUERY, source_profiles as development_profiles

MITIGATION_RUN = '20261016T043104Z-85c82c88'


def source_profiles(repo):
    repo = Path(repo).resolve()
    profiles,references,entities,config = development_profiles(repo)
    payload = prepare_evaluation_references(repo)
    folder = repo/'work/evaluation_corpus_mitigations'/MITIGATION_RUN
    saved = json.loads((folder/'prepared_records.json').read_text(encoding='utf-8'))
    for key in ['source_scope_assignment','evaluation_plan_fingerprint',
                'source_import_receipt_sha256','source_prepared_records_sha256']:
        if saved.get(key) != payload[key]:
            raise ValueError('Evaluation reference import identity changed.')
    expand(repo,profiles,references,entities,preparer=lambda _:payload,
           mitigation_kind='evaluation_corpus_mitigations',mitigation_run=MITIGATION_RUN)
    identity = {'profiles':{key:{'source_hash':p['document'].content_hash,
                'triples':sorted(p['allowed_triples']),'assertions':p.get('accepted_assertions',{})}
                for key,p in sorted(profiles.items())}, 'reference_ids':sorted(references),
                'entities':entities, 'evaluation_plan_fingerprint':payload['evaluation_plan_fingerprint'],
                'mitigation_import_receipt_sha256':sha256_file(folder/'import_receipt.json'),
                'source_import_receipt_sha256':payload['source_import_receipt_sha256']}
    scope_hash = hashlib.sha256(json.dumps(identity,sort_keys=True,ensure_ascii=False).encode()).hexdigest()
    scope = {'name':'frozen_shared_evaluation_sources_v1','sha256':scope_hash,
             'cisa_scope_count':len(profiles),'attack_reference_count':len(references),
             'evaluation_plan_fingerprint':payload['evaluation_plan_fingerprint'],
             'mitigation_import_receipt_sha256':identity['mitigation_import_receipt_sha256'],
             'source_import_receipt_sha256':identity['source_import_receipt_sha256'],
             'policy':'Same reviewed development plus evaluation source windows and direct references for all four modes; no labels or reference answers.'}
    return profiles,references,entities,dict(config,evaluation_scope=scope)


class EvaluationGraphRetriever(DevelopmentGraphRetriever):
    """Inherit frozen retrieval methods with a separate explicitly supplied scope."""
    def __init__(self,repo,driver=None,database='neo4j'):
        self.repo,self.driver,self.database = Path(repo).resolve(),driver,database
        self.profiles,self.references,self.expected_entities,self.config = source_profiles(self.repo)
        self.scope_name = self.config['evaluation_scope']['name']
        settings = self.config['retrieval']
        self.max_seeds = settings['max_seeds']
        self.max_candidates = settings['max_candidate_paths']
        self.max_paths = settings['final_paths']
        self.byte_cap = settings['evidence_token_budget']
        self.max_hops = settings['max_hops']
        if not 1<=self.max_hops<=3:
            raise ValueError('Frozen graph retrieval supports one to three hops.')
        self.configuration_hash = hashlib.sha256((json.dumps(self.config,sort_keys=True)+PATH_QUERY+
            'development-graph-retrieval-v2-reviewed-scopes;context-cap=utf8-bytes;domain-filter;longest-name-spans').encode()).hexdigest()
        self.last_context,self.last_stats = '',{}

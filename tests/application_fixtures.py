"""Synthetic evidence for application tests; no services or benchmark records."""
from application_engine import QueryResult
from schemas import AnswerResponse, EvidenceBundle, GraphPath, Passage, QueryRequest

TEXT = 'Example affiliates use Example Tool for remote access.'


def bundle(mode='graph_only', empty=False):
    passages = [] if empty else [Passage(citation_id='E1', doc_id='synthetic', chunk_id='chunk',
        source_url='https://example.org/source', text=TEXT, start=0, end=len(TEXT), source_kind='cisa')]
    paths = [] if empty or mode == 'text_only' else [GraphPath(path_id='P1', edges=[{
        'head_id': 'local:actor', 'predicate': 'USES', 'tail_id': 'local:tool',
        'assertion_ids': ['synthetic-assertion'], 'citation_ids': ['E1']}])]
    return EvidenceBundle(passages=passages, paths=paths, citation_ids=[] if empty else ['E1'],
        retrieval_ms=0, configuration_hash='test-'+mode, corpus_version='synthetic')


def result(question='What was observed?', mode='graph_only'):
    answer = AnswerResponse(answer=TEXT+' [E1]', claims=[{'text': TEXT, 'citations': ['E1']}],
        evidence=bundle(mode), abstained=False, execution_time_ms=1)
    return QueryResult(QueryRequest(question=question, mode=mode, corpus_version='synthetic'), answer,
        {'selected_path_count': len(answer.evidence.paths)},
        {'local:actor': {'name': 'Example affiliates', 'type': 'ThreatGroup'},
         'local:tool': {'name': 'Example Tool', 'type': 'Software'}},
        {'synthetic': {'title': 'Synthetic source', 'publication_date': None}}, 'test-digest', 'synthetic-run')


class FakeUIEngine:
    def __init__(self):
        self.calls = []
        self.closed = False

    def execute(self, request):
        self.calls.append(request)
        value = result(request.question, request.mode.value)
        value.request = request
        value.answer.evidence.corpus_version = request.corpus_version
        value.folder = 'synthetic-run-'+str(len(self.calls))
        return value

    def close(self):
        self.closed = True

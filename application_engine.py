"""Session-scoped application adapter over the unchanged development pipelines."""
import copy
import hashlib
import json
import math
import threading
import time
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlsplit
from uuid import uuid4

from graph.development_retrieval import source_profiles
from graph_qa import GENERATOR_VERSION, generate, save
from schemas import AnswerResponse, EvidenceBundle, QueryRequest


@dataclass
class ConnectionSettings:
    uri: str = 'bolt://localhost:7687'
    username: str = 'neo4j'
    database: str = 'neo4j'
    password: str = field(default='', repr=False)
    timeout: float = 60

    def __post_init__(self):
        uri = urlsplit(self.uri)
        if (uri.scheme not in {'bolt', 'bolt+s', 'bolt+ssc', 'neo4j', 'neo4j+s', 'neo4j+ssc'}
                or not uri.hostname or uri.username or uri.password or uri.query or uri.fragment):
            raise ValueError('Use a Neo4j URI without embedded credentials.')
        if not self.username.strip() or not self.database.strip():
            raise ValueError('Enter a username and database name.')
        if not math.isfinite(self.timeout) or not 0 < self.timeout <= 300:
            raise ValueError('Timeout must be between zero and 300 seconds.')


class QueryStageError(RuntimeError):
    """Public errors deliberately omit driver/HTTP exception text and credentials."""
    def __init__(self, stage, message, folder=None):
        self.stage, self.folder = stage, folder
        super().__init__(message)


@dataclass
class QueryResult:
    request: QueryRequest
    answer: AnswerResponse
    retrieval: dict
    entities: dict
    sources: dict
    model_digest: str
    folder: str

    def as_dict(self):
        return {'request': self.request.model_dump(mode='json'),
                'answer': self.answer.model_dump(mode='json'),
                'retrieval': self.retrieval, 'entities': self.entities, 'sources': self.sources,
                'model_digest': self.model_digest, 'folder': self.folder}


def make_retriever(mode, repo, driver, database):
    # Imports and index loading are lazy; importing the UI never connects services.
    if mode == 'text_only':
        from retrieval.text_retrieval import DevelopmentTextRetriever
        return DevelopmentTextRetriever(repo)
    if mode == 'graph_only':
        from graph.development_retrieval import DevelopmentGraphRetriever
        return DevelopmentGraphRetriever(repo, driver, database)
    if mode == 'hybrid_no_node2vec':
        from retrieval.combined_retrieval import DevelopmentCombinedRetriever
        return DevelopmentCombinedRetriever(repo, driver, database)
    if mode == 'hybrid':
        from retrieval.hybrid_retrieval import DevelopmentHybridRetriever
        return DevelopmentHybridRetriever(repo, driver, database)
    raise ValueError('Unknown retrieval mode.')


def make_driver(settings):
    from neo4j import GraphDatabase
    return GraphDatabase.driver(settings.uri, auth=(settings.username, settings.password),
        connection_timeout=10, connection_acquisition_timeout=15, max_transaction_retry_time=15)


class ApplicationEngine:
    """Implements interfaces.QueryEngine; history is never appended to model context."""
    def __init__(self, repo, settings=None, *, retriever_factory=make_retriever,
                 driver_factory=make_driver, http=None, generator=generate, profiles_loader=source_profiles):
        self.repo = Path(repo).resolve()
        self.settings = copy.copy(settings or ConnectionSettings())
        self._config_bytes = (self.repo/'config.json').read_bytes()
        self.config = json.loads(self._config_bytes)
        profiles, references, self.entities, scoped_config = profiles_loader(self.repo)
        self.scope = scoped_config.get('development_scope', {})
        self.sources = {p['document'].doc_id: {
            'title': p['document'].title, 'publication_date': p['document'].publication_date,
            'source_kind': p['document'].source} for p in profiles.values()}
        self.sources.update({r['document']['doc_id']: {
            'title': r['document']['title'], 'publication_date': r['document'].get('publication_date'),
            'source_kind': 'attack'} for r in references.values()})
        if http is None:
            import requests
            http = requests.Session()
            http.trust_env = False
        self.http, self.generator = http, generator
        self._factory, self._driver_factory = retriever_factory, driver_factory
        self._profiles_loader = profiles_loader
        self._driver, self._retrievers, self._digest, self._assets = None, {}, None, {}
        self._lock, self._closed = threading.Lock(), False

    def query(self, request):
        return self.execute(request).answer

    def execute(self, request):
        with self._lock:
            return self._execute(request)

    def _execute(self, request):
        request = QueryRequest.model_validate(request)
        if self._closed:
            raise QueryStageError('connection', 'Reconnect before asking another question.')
        if request.corpus_version != self.config['corpus_version']:
            raise QueryStageError('configuration', 'The question uses a different corpus version.')
        if (self.repo/'config.json').read_bytes() != self._config_bytes:
            raise QueryStageError('configuration', 'Configuration changed. Reconnect to reload it.')
        mode = request.mode.value
        folder = self.repo/'work/application_qa'/(datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')+'-'+uuid4().hex[:8])
        folder.mkdir(parents=True)
        save(folder/'question.json', request.model_dump(mode='json'))
        summary = {'purpose': 'development_application_qa', 'mode': mode, 'status': 'started',
            'generator_version': GENERATOR_VERSION, 'semantic_review_status': 'pending',
            'development_scope': self.scope,
            'latency_scope': 'Service/index initialization, retrieval, packing and generation for this request.'}
        save(folder/'summary.json', summary)
        stage, started = 'connection', time.perf_counter()
        try:
            if mode != 'text_only':
                if self._driver is None:
                    self._driver = self._driver_factory(self.settings)
                    self.settings.password = ''
                self._driver.verify_connectivity()
            stage = 'index'
            # Long-lived UI sessions must recheck the frozen sources, not only
            # the copies used when the session/retriever was first constructed.
            _, _, _, current_config = self._profiles_loader(self.repo)
            if current_config.get('development_scope', {}) != self.scope:
                raise ValueError('Source scope changed; reconnect.')
            if mode not in self._retrievers:
                self._retrievers[mode] = self._factory(mode, self.repo, self._driver, self.settings.database)
                r = self._retrievers[mode]
                paths = []
                text = getattr(r, 'text', r)
                if hasattr(text, 'manifest') and 'records_path' in text.manifest:
                    records = Path(text.manifest['records_path'])
                    paths.extend([records, records.parent/'manifest.json'])
                index = getattr(r, 'index', None)
                if index is not None and 'vectors_path' in index.manifest:
                    vectors = Path(index.manifest['vectors_path'])
                    paths.extend([vectors, vectors.parent/'manifest.json', Path(index.manifest['projection_path'])])
                self._assets[mode] = {p: hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
            retriever = self._retrievers[mode]
            for path, expected_hash in self._assets[mode].items():
                if hashlib.sha256(path.read_bytes()).hexdigest() != expected_hash:
                    raise ValueError('Saved index assets changed; reconnect.')
            if retriever.config.get('development_scope', {}) != self.scope:
                raise ValueError('Source scope changed.')
            for key in ('corpus_version', 'attack_release', 'llm', 'retrieval', 'text_embedding', 'node2vec'):
                if retriever.config.get(key) != self.config.get(key):
                    raise ValueError('Retriever configuration differs from the application.')
            # Do not reuse a fitted graph index after its published pointer changes.
            if mode == 'hybrid':
                pointer = json.loads((self.repo/'work/graph_index/current.json').read_text(encoding='utf-8'))
                if pointer['index_fingerprint'] != retriever.index.manifest['index_fingerprint']:
                    raise ValueError('Graph index changed.')
            stage = 'model'
            response = self.http.get('http://localhost:11434/api/tags', timeout=(10, self.settings.timeout))
            response.raise_for_status()
            model = next((m for m in response.json()['models'] if m['name'] == self.config['llm']['model']), None)
            digest = model.get('digest') if model else None
            expected = self.config['llm'].get('digest') or self._digest
            if not digest or (expected and digest != expected):
                raise ValueError('Model missing or changed.')
            self._digest = digest
            summary.update(model=model['name'], model_digest=digest,
                options={k: self.config['llm'][k] for k in ('temperature', 'num_ctx', 'num_predict')},
                configuration_hash=retriever.configuration_hash)
            stage = 'retrieval'
            bundle = EvidenceBundle.model_validate(retriever.retrieve(request))
            if bundle.corpus_version != request.corpus_version or bundle.configuration_hash != retriever.configuration_hash:
                raise ValueError('Retriever returned a mismatched bundle.')
            stats = copy.deepcopy(retriever.last_stats)
            save(folder/'evidence.json', bundle.model_dump(mode='json'))
            save(folder/'retrieval.json', stats)
            stage = 'generation'
            if not bundle.passages or (mode == 'graph_only' and not bundle.paths):
                answer = AnswerResponse(answer='The retrieved evidence is insufficient to answer this question.',
                    claims=[], evidence=bundle, abstained=True, execution_time_ms=0)
                generation = {'attempts': 0}
            else:
                answer, generation = self.generator(self.http, request, bundle, retriever.last_context,
                    retriever.config, folder, self.settings.timeout)
                answer = AnswerResponse.model_validate(answer)
                if answer.evidence != bundle:
                    raise ValueError('Generator changed the evidence.')
            answer.execution_time_ms = (time.perf_counter()-started)*1000
            answer.warnings = list(dict.fromkeys(answer.warnings+[
                'Development sources only; citation validity does not establish claim correctness.',
                'Human semantic review and final evaluation remain pending.']))
            summary.update(status='abstained' if answer.abstained else 'answer_ready_for_review',
                **generation, execution_time_ms=answer.execution_time_ms,
                finished_at=datetime.now(timezone.utc).isoformat())
            result = QueryResult(request, answer, stats, copy.deepcopy(self.entities),
                                 copy.deepcopy(self.sources), digest, str(folder))
            save(folder/'answer.json', answer.model_dump(mode='json'))
            save(folder/'display.json', result.as_dict())
            save(folder/'summary.json', summary)
            return result
        except Exception:
            messages = {
                'connection': 'Neo4j could not be reached. Check the connection settings and password.',
                'index': 'The selected evidence index could not be verified. Check its saved build and reconnect.',
                'model': 'The configured Ollama model is unavailable or changed. Check Ollama and reconnect.',
                'retrieval': 'Evidence retrieval failed. Check source/index freshness and question length.',
                'generation': 'A valid cited answer could not be produced. Check Ollama and try again.'}
            message = messages[stage]
            summary.update(status='failed', failed_stage=stage, error=message)
            save(folder/'summary.json', summary)
            raise QueryStageError(stage, message, str(folder)) from None

    def close(self):
        with self._lock:
            try:
                if self._driver is not None:
                    self._driver.close()
            finally:
                self.http.close()
                self.settings.password = ''
                self._retrievers.clear()
                self._closed = True

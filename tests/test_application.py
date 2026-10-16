import json
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import MagicMock

from application_engine import ApplicationEngine, ConnectionSettings, QueryStageError
from application_view import add_history, graph_html, query_graph
from application_fixtures import TEXT, bundle, result
from schemas import AnswerResponse, QueryRequest


class ApplicationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.repo = Path(self.temp.name)
        self.config = {'corpus_version': 'synthetic', 'llm': {'model': 'test-model', 'digest': None,
                       'temperature': 0, 'num_ctx': 8192, 'num_predict': 700}}
        (self.repo/'config.json').write_text(json.dumps(self.config), encoding='utf-8')
        self.http = MagicMock()
        self.http.get.return_value.json.return_value = {'models': [{'name': 'test-model', 'digest': 'digest-a'}]}
        self.driver, self.factory, self.generator = MagicMock(), MagicMock(), MagicMock()
        self.empty = False

        def retriever(mode, repo, driver, database):
            value = SimpleNamespace(config=self.config, configuration_hash='test-'+mode,
                last_stats={}, last_context='Exact synthetic context')
            def retrieve(request):
                return bundle(mode, self.empty)
            value.retrieve = MagicMock(side_effect=retrieve)
            value.index = SimpleNamespace(manifest={'index_fingerprint': 'graph-test'})
            return value
        self.factory.side_effect = retriever

        def generate(http, request, evidence, context, config, folder, timeout):
            return AnswerResponse(answer=TEXT+' [E1]', claims=[{'text': TEXT, 'citations': ['E1']}],
                evidence=evidence, abstained=False, execution_time_ms=0), {'attempts': 1}
        self.generator.side_effect = generate
        pointer = self.repo/'work/graph_index/current.json'
        pointer.parent.mkdir(parents=True)
        pointer.write_text(json.dumps({'index_fingerprint': 'graph-test'}), encoding='utf-8')
        self.engine = ApplicationEngine(self.repo, ConnectionSettings(password='SECRET-MARKER'),
            retriever_factory=self.factory, driver_factory=lambda settings: self.driver,
            http=self.http, generator=self.generator,
            profiles_loader=lambda repo: ({}, {}, {}, self.config))
        self.addCleanup(self.engine.close)

    def request(self, mode='text_only'):
        return QueryRequest(question='What was observed?', mode=mode, corpus_version='synthetic')

    def test_modes_dispatch_without_fallback_and_records_preserve_requested_mode(self):
        for mode in ('text_only', 'graph_only', 'hybrid_no_node2vec', 'hybrid'):
            value = self.engine.execute(self.request(mode))
            receipt = json.loads((Path(value.folder)/'summary.json').read_text(encoding='utf-8'))
            self.assertEqual((receipt['mode'], value.request.mode.value), (mode, mode))
            self.assertEqual(receipt['model_digest'], 'digest-a')
            self.assertEqual(receipt['generator_version'], 'development-shared-cited-generator-v2')
        self.assertEqual([call.args[0] for call in self.factory.call_args_list],
                         ['text_only', 'graph_only', 'hybrid_no_node2vec', 'hybrid'])

    def test_text_only_does_not_create_or_probe_neo4j(self):
        self.engine.execute(self.request())
        self.assertIsNone(self.engine._driver)
        self.driver.verify_connectivity.assert_not_called()
        self.assertEqual(self.generator.call_args.args[3], 'Exact synthetic context')

    def test_corpus_and_changed_configuration_rejected_before_service_calls(self):
        request = self.request()
        request.corpus_version = 'other'
        with self.assertRaises(QueryStageError):
            self.engine.execute(request)
        (self.repo/'config.json').write_text('{}', encoding='utf-8')
        with self.assertRaises(QueryStageError):
            self.engine.execute(self.request())
        self.http.get.assert_not_called()
        self.factory.assert_not_called()

    def test_empty_evidence_abstains_without_generation(self):
        self.empty = True
        answer = self.engine.query(self.request('graph_only'))
        self.assertTrue(answer.abstained)
        self.assertEqual(answer.claims, [])
        self.generator.assert_not_called()

    def test_mismatched_retriever_and_changed_generator_evidence_are_rejected(self):
        self.engine.execute(self.request())
        retriever = self.engine._retrievers['text_only']
        retriever.config = {**self.config, 'llm': {**self.config['llm'], 'num_predict': 900}}
        with self.assertRaises(QueryStageError) as caught:
            self.engine.execute(self.request())
        self.assertEqual(caught.exception.stage, 'index')
        retriever.config = self.config
        def altered(*args):
            response = result(mode='text_only').answer
            response.evidence.configuration_hash = 'changed'
            return response, {'attempts': 1}
        self.generator.side_effect = altered
        with self.assertRaises(QueryStageError) as caught:
            self.engine.execute(self.request())
        self.assertEqual(caught.exception.stage, 'generation')

    def test_missing_full_hybrid_index_is_error_not_ablation(self):
        self.factory.side_effect = ValueError('missing graph vectors SECRET-MARKER')
        with self.assertRaises(QueryStageError) as caught:
            self.engine.execute(self.request('hybrid'))
        self.assertEqual(caught.exception.stage, 'index')
        self.assertNotIn('SECRET-MARKER', str(caught.exception))
        self.assertEqual(self.factory.call_count, 1)
        self.generator.assert_not_called()

    def test_model_change_and_graph_pointer_change_rejected(self):
        self.engine.execute(self.request())
        self.http.get.return_value.json.return_value['models'][0]['digest'] = 'digest-b'
        with self.assertRaises(QueryStageError) as caught:
            self.engine.execute(self.request())
        self.assertEqual(caught.exception.stage, 'model')
        self.http.get.return_value.json.return_value['models'][0]['digest'] = 'digest-a'
        self.engine.execute(self.request('hybrid'))
        (self.repo/'work/graph_index/current.json').write_text('{"index_fingerprint":"changed"}', encoding='utf-8')
        with self.assertRaises(QueryStageError) as caught:
            self.engine.execute(self.request('hybrid'))
        self.assertEqual(caught.exception.stage, 'index')

    def test_long_lived_session_rejects_changed_sources_and_index_files(self):
        make = self.factory.side_effect
        records = self.repo/'records.json'
        records.write_text('original', encoding='utf-8')
        (self.repo/'manifest.json').write_text('{}', encoding='utf-8')
        def with_assets(*args):
            r = make(*args)
            r.manifest = {'records_path': str(records)}
            return r
        self.factory.side_effect = with_assets
        self.engine.execute(self.request())
        records.write_text('altered', encoding='utf-8')
        with self.assertRaises(QueryStageError) as caught:
            self.engine.execute(self.request())
        self.assertEqual(caught.exception.stage, 'index')
        records.write_text('original', encoding='utf-8')
        self.engine._profiles_loader = lambda repo: ({}, {}, {}, {'development_scope': {'sha256': 'changed'}})
        with self.assertRaises(QueryStageError) as caught:
            self.engine.execute(self.request())
        self.assertEqual(caught.exception.stage, 'index')

    def test_generation_failure_receipt_never_logs_exception_credentials(self):
        self.generator.side_effect = RuntimeError('SECRET-MARKER raw response')
        with self.assertRaises(QueryStageError) as caught:
            self.engine.execute(self.request())
        self.assertEqual(caught.exception.stage, 'generation')
        receipt = (Path(caught.exception.folder)/'summary.json').read_text(encoding='utf-8')
        self.assertNotIn('SECRET-MARKER', receipt)
        self.assertNotIn('raw response', receipt)

    def test_history_is_snapshot_not_live_mutable_state(self):
        value = result()
        history = add_history([], value)
        value.answer.claims[0].text = 'Changed later'
        self.assertEqual(history[0]['answer']['claims'][0]['text'], TEXT)
        self.assertEqual(len(add_history(history, value, limit=1)), 1)

    def test_graph_uses_only_returned_edges_and_treats_source_labels_as_data(self):
        value = result()
        graph = query_graph(value.answer, value.entities)
        self.assertEqual(len(graph['edges']), 1)
        self.assertEqual(graph['edges'][0]['origin'], 'CISA observation')
        value.entities['local:tool']['name'] = '</script><script>BAD_SOURCE()</script>'
        html = graph_html(value.answer, value.entities)
        self.assertNotIn('</script><script>BAD_SOURCE()', html)
        self.assertIn('\\u003c/script', html)
        self.assertNotIn('https://', html)  # No CDN or external graph dependency.

    def test_close_releases_resources_and_disallows_further_queries(self):
        self.engine.execute(self.request('graph_only'))
        self.engine.close()
        self.driver.close.assert_called()
        self.http.close.assert_called()
        self.assertEqual(self.engine.settings.password, '')
        with self.assertRaises(QueryStageError):
            self.engine.execute(self.request())

    def test_connection_settings_reject_embedded_credentials_and_nonfinite_timeout(self):
        for kwargs in ({'uri': 'bolt://user:password@localhost:7687'}, {'timeout': float('nan')}):
            with self.assertRaises(ValueError):
                ConnectionSettings(**kwargs)


if __name__ == '__main__':
    unittest.main()

import os
import unittest
from unittest.mock import MagicMock, patch

from fastapi.testclient import TestClient

import live_api
import test_application as fixtures
from application_engine import QueryStageError


class LiveAPITests(unittest.TestCase):
    def setUp(self):
        self.fixture = fixtures.ApplicationTests(methodName='runTest')
        self.fixture.setUp()
        self.addCleanup(self.fixture.doCleanups)

    def test_http_queries_dispatch_all_modes_through_application_engine(self):
        engine = self.fixture.engine
        with TestClient(live_api.create_live_app(lambda: engine)) as client:
            self.assertEqual(client.get('/health').json()['status'], 'ready')
            for mode in ('text_only', 'graph_only', 'hybrid_no_node2vec', 'hybrid'):
                response = client.post('/query', json=self.fixture.request(mode).model_dump(mode='json'))
                self.assertEqual(response.status_code, 200, response.text)
                self.assertFalse(response.json()['abstained'])
                self.assertEqual(response.json()['claims'][0]['citations'], ['E1'])
        self.assertEqual([call.args[0] for call in self.fixture.factory.call_args_list],
                         ['text_only', 'graph_only', 'hybrid_no_node2vec', 'hybrid'])
        self.assertEqual(len(list((self.fixture.repo/'work/application_qa').glob('*/answer.json'))), 4)
        self.fixture.driver.close.assert_called_once()
        self.fixture.http.close.assert_called_once()

    def test_invalid_request_and_corpus_mismatch_do_not_call_services(self):
        with TestClient(live_api.create_live_app(lambda: self.fixture.engine)) as client:
            self.assertEqual(client.post('/query', json={'question': 'x'}).status_code, 422)
            request = self.fixture.request().model_dump(mode='json')
            request['corpus_version'] = 'other'
            self.assertEqual(client.post('/query', json=request).status_code, 409)
        self.fixture.http.get.assert_not_called()

    def test_empty_graph_evidence_returns_cited_contract_abstention(self):
        self.fixture.empty = True
        with TestClient(live_api.create_live_app(lambda: self.fixture.engine)) as client:
            response = client.post('/query', json=self.fixture.request('graph_only').model_dump(mode='json'))
            self.assertEqual(response.status_code, 200)
            self.assertTrue(response.json()['abstained'])
        self.fixture.generator.assert_not_called()

    def test_errors_are_mapped_without_leaking_credentials(self):
        engine = MagicMock()
        with TestClient(live_api.create_live_app(lambda: engine)) as client:
            errors = [(QueryStageError(stage, 'SECRET-MARKER'), code) for stage, code in
                [('configuration', 409), ('connection', 503), ('index', 503),
                 ('model', 503), ('retrieval', 502), ('generation', 502)]]
            errors += [(TimeoutError('SECRET-MARKER'), 504), (ConnectionError('SECRET-MARKER'), 503),
                       (RuntimeError('SECRET-MARKER'), 500)]
            for error, code in errors:
                engine.query.side_effect = error
                response = client.post('/query', json=self.fixture.request().model_dump(mode='json'))
                self.assertEqual(response.status_code, code)
                self.assertNotIn('SECRET-MARKER', response.text)
        engine.close.assert_called_once()

    def test_startup_failure_is_redacted_and_never_serves_unconfigured_engine(self):
        with self.assertRaisesRegex(RuntimeError, '^Could not initialize ThreatWeave') as caught:
            with TestClient(live_api.create_live_app(MagicMock(side_effect=ValueError('SECRET-MARKER')))):
                self.fail('Startup must fail.')
        self.assertNotIn('SECRET-MARKER', str(caught.exception))

    def test_default_app_constructs_live_engine_at_startup_and_closes_it(self):
        engine = MagicMock()
        with patch.object(live_api, 'build_engine', return_value=engine) as build:
            app = live_api.create_live_app()
            build.assert_not_called()
            with TestClient(app) as client:
                build.assert_called_once_with()
                self.assertIs(app.state.engine, engine)
                self.assertEqual(client.get('/health').json()['service_checks'], 'performed_per_query')
            self.assertIsNone(app.state.engine)
            engine.close.assert_called_once()

    def test_engine_builder_uses_portable_provider_and_environment_credentials(self):
        with patch.dict(os.environ, {'THREATWEAVE_NEO4J_URI': 'bolt://localhost:9999',
                'THREATWEAVE_NEO4J_USER': 'reader', 'THREATWEAVE_NEO4J_DATABASE': 'example',
                'THREATWEAVE_NEO4J_PASSWORD': 'SECRET-MARKER'}), \
                patch.object(live_api, 'ApplicationEngine') as engine:
            live_api.build_engine(self.fixture.repo)
        settings = engine.call_args.args[1]
        self.assertEqual((settings.uri, settings.username, settings.database),
                         ('bolt://localhost:9999', 'reader', 'example'))
        self.assertEqual(settings.password, 'SECRET-MARKER')
        self.assertNotIn('SECRET-MARKER', repr(settings))
        self.assertEqual(engine.call_args.kwargs['profiles_loader'].__module__, 'portable_sources')

    def test_supported_launcher_uses_live_app_and_private_password_prompt(self):
        import portable
        with patch('sys.argv', ['portable.py', 'api', '--uri', 'bolt://localhost:9999', '--prompt-password']), \
                patch.dict(os.environ, {'THREATWEAVE_NEO4J_DATABASE': 'from_environment'}), \
                patch.object(portable.getpass, 'getpass', return_value='SECRET-MARKER'), \
                patch.object(portable.subprocess, 'run') as run:
            run.return_value.returncode = 0
            self.assertEqual(portable.main(), 0)
        command = run.call_args.args[0]
        self.assertIn('live_api:app', command)
        self.assertIn('127.0.0.1', command)
        self.assertNotIn('SECRET-MARKER', ' '.join(command))
        env = run.call_args.kwargs['env']
        self.assertEqual(env['THREATWEAVE_NEO4J_URI'], 'bolt://localhost:9999')
        self.assertEqual(env['THREATWEAVE_NEO4J_DATABASE'], 'from_environment')
        self.assertEqual(env['THREATWEAVE_NEO4J_PASSWORD'], 'SECRET-MARKER')


if __name__ == '__main__':
    unittest.main()

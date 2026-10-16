"""Real Streamlit AppTest checks after the operator installs the pinned UI."""
import importlib.util
import unittest
from pathlib import Path
from unittest.mock import patch

if importlib.util.find_spec('streamlit') is None:
    raise unittest.SkipTest('Streamlit setup pending; run setup_application.py to enable UI checks.')

from streamlit.testing.v1 import AppTest
from application_fixtures import FakeUIEngine
from application_engine import QueryStageError

REPO = Path(__file__).resolve().parents[1]


class ApplicationUITests(unittest.TestCase):
    def app(self):
        # Any accidental real adapter creation fails; tests never contact services.
        guard = patch('application_engine.ApplicationEngine', side_effect=AssertionError('Real services forbidden in UI tests'))
        guard.start()
        self.addCleanup(guard.stop)
        return AppTest.from_file(str(REPO/'streamlit_app.py'), default_timeout=20).run()

    def test_initial_page_load_needs_no_services(self):
        app = self.app()
        self.assertEqual(len(app.exception), 0)
        self.assertEqual(app.title[0].value, 'ThreatWeave')
        self.assertEqual(app.session_state['history'], [])

    def test_question_modes_history_sources_and_graph_render(self):
        app = self.app()
        engine = FakeUIEngine()
        app.session_state['engine'] = engine
        app.selectbox[0].select('graph_only').run()
        app.text_area[0].input('What was observed?')
        next(b for b in app.button if b.label == 'Ask ThreatWeave').click().run()
        self.assertEqual(len(app.exception), 0)
        self.assertEqual(len(engine.calls), 1)
        self.assertEqual(engine.calls[0].mode.value, 'graph_only')
        self.assertEqual(len(app.session_state['history']), 1)
        self.assertTrue(any('Example affiliates' in text.value for text in app.text))
        self.assertEqual([tab.label for tab in app.tabs], ['Sources', 'Query graph', 'Run details'])
        next(b for b in app.button if b.label == 'Disconnect / reconnect').click().run()
        self.assertEqual(len(app.exception), 0)
        self.assertTrue(engine.closed)
        self.assertEqual(len(app.session_state['history']), 1)

    def test_failed_query_keeps_history_without_recording_fake_answer(self):
        app = self.app()
        engine = FakeUIEngine()
        def fail(request):
            raise QueryStageError('index', 'The evidence index could not be verified.')
        engine.execute = fail
        app.session_state['engine'] = engine
        app.text_area[0].input('What was observed?')
        next(b for b in app.button if b.label == 'Ask ThreatWeave').click().run()
        self.assertEqual(len(app.exception), 0)
        self.assertEqual(app.session_state['history'], [])
        self.assertTrue(any('could not be verified' in e.value for e in app.error))

    def test_multiple_modes_history_navigation_and_clearing_are_session_only(self):
        app = self.app()
        engine = FakeUIEngine()
        app.session_state['engine'] = engine
        modes = ['text_only', 'graph_only', 'hybrid_no_node2vec', 'hybrid']
        for index, mode in enumerate(modes):
            next(w for w in app.selectbox if w.label == 'Retrieval mode').select(mode).run()
            app.text_area[0].input(f'Question number {index+1}?')
            next(b for b in app.button if b.label == 'Ask ThreatWeave').click().run()
            self.assertEqual(len(app.exception), 0)
        self.assertEqual([q.mode.value for q in engine.calls], modes)
        self.assertEqual(len(app.session_state['history']), 4)
        self.assertEqual(len(app.get('download_button')), 1)
        next(w for w in app.selectbox if w.label == 'Answer history').select(0).run()
        self.assertTrue(any(h.value == 'Question number 1?' for h in app.subheader))
        self.assertEqual(len(engine.calls), 4)
        next(b for b in app.button if b.label == 'Clear visible history').click().run()
        self.assertEqual(app.session_state['history'], [])
        self.assertFalse(engine.closed)
        self.assertEqual(len(engine.calls), 4)


if __name__ == '__main__':
    unittest.main()

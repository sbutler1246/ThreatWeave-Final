"""Live HTTP entry point; the original api.py remains the frozen design contract."""
from contextlib import asynccontextmanager
import os
from pathlib import Path

from fastapi import FastAPI, HTTPException

from application_engine import ApplicationEngine, ConnectionSettings, QueryStageError
from schemas import AnswerResponse, QueryRequest

ROOT = Path(__file__).resolve().parent


def build_engine(repo=ROOT):
    """Use this checkout's portable sources and locally built indexes."""
    from portable_sources import install, source_profiles
    install()
    settings = ConnectionSettings(
        uri=os.environ.get('THREATWEAVE_NEO4J_URI', 'bolt://localhost:7687'),
        username=os.environ.get('THREATWEAVE_NEO4J_USER', 'neo4j'),
        database=os.environ.get('THREATWEAVE_NEO4J_DATABASE', 'neo4j'),
        password=os.environ.get('THREATWEAVE_NEO4J_PASSWORD', ''))
    return ApplicationEngine(repo, settings, profiles_loader=source_profiles)


def create_live_app(engine_factory=None):
    factory = build_engine if engine_factory is None else engine_factory

    @asynccontextmanager
    async def lifespan(app):
        try:
            engine = factory()
        except Exception:
            raise RuntimeError('Could not initialize ThreatWeave. Check local sources and connection settings.') from None
        app.state.engine = engine
        try:
            yield
        finally:
            app.state.engine = None
            engine.close()

    app = FastAPI(title='ThreatWeave Live API', version='1.0.0', lifespan=lifespan)
    app.state.engine = None

    @app.get('/health')
    def health():
        # Services/indexes are checked by the engine for the selected query mode.
        return {'status': 'ready' if app.state.engine is not None else 'not_started',
                'service_checks': 'performed_per_query'}

    @app.post('/query', response_model=AnswerResponse)
    def query(request: QueryRequest):
        engine = app.state.engine
        if engine is None:
            raise HTTPException(503, 'ThreatWeave has not started.')
        try:
            return engine.query(request)
        except QueryStageError as error:
            status, detail = {
                'configuration': (409, 'Corpus or configuration changed. Restart the API with matching settings.'),
                'connection': (503, 'Neo4j is unavailable. Check its service and connection settings.'),
                'index': (503, 'The selected index is missing or could not be verified. Rebuild it and restart the API.'),
                'model': (503, 'The configured Ollama model is unavailable or changed.'),
                'retrieval': (502, 'Evidence retrieval failed. Check source and index freshness.'),
                'generation': (502, 'The model did not produce a valid cited answer.')
            }.get(error.stage, (500, 'The query could not be completed.'))
            raise HTTPException(status, detail) from None
        except TimeoutError:
            raise HTTPException(504, 'The query timed out.') from None
        except ConnectionError:
            raise HTTPException(503, 'A required service is unavailable.') from None
        except Exception:
            raise HTTPException(500, 'The query could not be completed.') from None

    return app


# Uvicorn starts the lifecycle and injects the real ApplicationEngine before serving.
app = create_live_app()

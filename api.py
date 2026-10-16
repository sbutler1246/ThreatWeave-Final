"""API contract factory; inject a real engine to serve answers."""
from fastapi import FastAPI, HTTPException
from schemas import QueryRequest, AnswerResponse
from interfaces import QueryEngine

class ManifestMismatchError(ValueError): pass

def create_app(engine: QueryEngine | None=None):
    app=FastAPI(title='ThreatWeave',version='0.1.0')
    @app.get('/health')
    def health():
        return {'status':'ready' if engine is not None else 'not_configured'}
    @app.post('/query',response_model=AnswerResponse)
    def query(request: QueryRequest):
        if engine is None: raise HTTPException(503,'Query engine adapters not configured')
        try: return engine.query(request)
        except ManifestMismatchError as exc: raise HTTPException(409,'Corpus/index manifest mismatch') from exc
        except TimeoutError as exc: raise HTTPException(504,'Query timed out') from exc
        except ConnectionError as exc: raise HTTPException(503,'Required service unavailable') from exc
    return app

app=create_app()

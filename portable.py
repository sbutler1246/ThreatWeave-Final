"""Portable live-application preparation. Run --help from your own checkout."""
import argparse
from datetime import datetime, timezone
import getpass
import importlib.metadata
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parent


def schema_statements(text):
    schema = '\n'.join(line for line in text.splitlines() if not line.strip().startswith('//'))
    return [statement.strip() for statement in schema.split(';') if statement.strip()]


def sources():
    from portable_sources import check
    bundle, projection, fingerprint = check(ROOT)
    print(f'PASS: {len(bundle["profiles"])} CISA source windows; {len(bundle["references"])} ATT&CK references; '
        f'{len(projection["nodes"])} domain nodes; {len(projection["edges"])} directed facts.')
    print('Original scope fingerprint: ' + bundle['config']['development_scope']['sha256'])
    return bundle, projection, fingerprint


def download():
    from huggingface_hub import snapshot_download
    config = json.loads((ROOT / 'config.json').read_text(encoding='utf-8'))
    cache = ROOT / 'work/model_cache/sentence_transformers'
    os.environ.pop('HF_HUB_OFFLINE', None)
    path = snapshot_download(repo_id=config['text_embedding']['model'], revision=config['text_embedding']['revision'],
        cache_dir=str(cache), token=False, allow_patterns=['*.json', '*.txt', '*.safetensors', '1_Pooling/*'])
    print('Downloaded pinned MiniLM revision into this checkout: ' + str(path))


def import_graph(uri, user, database):
    from neo4j import GraphDatabase
    from resolve import norm
    bundle, projection, fingerprint = sources()
    password = getpass.getpass('Password for YOUR empty Neo4j database: ')
    def write(tx):
        if tx.run('MATCH (n) RETURN count(n) AS count').single()['count']:
            raise ValueError('Choose a new empty database. This importer never deletes existing data.')
        entities = bundle['entities']
        labels = {'ThreatGroup', 'Software', 'Technique', 'Mitigation'}
        for entity in entities.values():
            if entity['type'] not in labels:
                raise ValueError('Unexpected entity type')
            props = dict(entity, normalized_name=entity.get('normalized_name', norm(entity['name'])))
            tx.run(f'CREATE (e:Entity:{entity["type"]}) SET e = $props', props=props).consume()
        records = []
        for item in bundle['items']:
            records.extend(dict(document=item['document'], chunk=item['chunk'], assertion=a) for a in item['assertions'])
        records.extend(bundle['references'].values())
        for record in records:
            for label, key, props in [('Document', 'doc_id', record['document']), ('Chunk', 'chunk_id', record['chunk'])]:
                tx.run(f'MERGE (n:{label} {{{key}:$id}}) SET n += $props', id=props[key], props=props).consume()
            a = record['assertion']
            if a['predicate'] not in {'USES', 'USES_TECHNIQUE', 'MITIGATED_BY'}:
                raise ValueError('Unexpected predicate')
            tx.run('MERGE (a:Assertion {assertion_id:$id}) SET a += $props', id=a['assertion_id'], props=a).consume()
            props = {k: v for k, v in a.items() if k not in {'assertion_id', 'head_id', 'tail_id', 'predicate'}}
            tx.run('MATCH (h:Entity {canonical_id:$head}), (t:Entity {canonical_id:$tail}) '
                f'MERGE (h)-[r:{a["predicate"]}]->(t) SET r += $props, r.assertion_ids = CASE '
                'WHEN $aid IN coalesce(r.assertion_ids,[]) THEN r.assertion_ids ELSE coalesce(r.assertion_ids,[]) + [$aid] END',
                head=a['head_id'], tail=a['tail_id'], aid=a['assertion_id'], props=props).consume()
        for item in bundle['items']:
            for mention in item['mentions']:
                tx.run('MATCH (e:Entity {canonical_id:$id}), (d:Document {doc_id:$doc}) '
                    'MERGE (e)-[m:MENTIONED_IN {chunk_id:$chunk}]->(d) SET m += $props',
                    id=mention['canonical_id'], doc=mention['source_doc_id'], chunk=mention['chunk_id'], props=mention).consume()
        # The original importer keeps the last occurrence for each entity/chunk/document.
        mentions = list({(m['canonical_id'], m['source_doc_id'], m['chunk_id']): m
            for item in bundle['items'] for m in item['mentions']}.values())
        verified = tx.run('UNWIND $rows AS row MATCH (e:Entity)-[m:MENTIONED_IN]->(d:Document) '
            'WHERE e.canonical_id=row.canonical_id AND d.doc_id=row.source_doc_id AND m.chunk_id=row.chunk_id '
            'AND m.evidence_text=row.evidence_text AND m.evidence_start=row.evidence_start AND m.evidence_end=row.evidence_end '
            'RETURN count(*) AS count', rows=mentions).single()['count']
        if verified != len(mentions):
            raise ValueError('Imported source mentions differ from their original evidence.')
        return len(records)
    try:
        with GraphDatabase.driver(uri, auth=(user, password), connection_timeout=10) as driver:
            driver.verify_connectivity()
            with driver.session(database=database) as session:
                # Schema statements do not delete data; data insertion is one transaction.
                for statement in schema_statements((ROOT / 'graph/schema.cypher').read_text(encoding='utf-8')):
                    session.run(statement).consume()
                count = session.execute_write(write)
            from graph.development_projection import read_projection
            from graph.development_retrieval import DevelopmentGraphRetriever
            from portable_sources import install
            install()
            actual, actual_hash = read_projection(driver, DevelopmentGraphRetriever(ROOT), database)
            if actual_hash != fingerprint:
                raise ValueError('Imported graph differs from the accepted source projection.')
    finally:
        password = None
    print(f'PASS: {count} original assertions imported and live directed projection verified.')


def index(kind, preview):
    from portable_sources import install
    install()
    if kind == 'graph':
        # Set BEFORE the interpreter starts; original indexer will not respawn without the adapter.
        from graph.node2vec_training import training_environment, training_parameters
        config = json.loads((ROOT / 'config.json').read_text(encoding='utf-8'))
        env = training_environment(training_parameters(config))
        keys = ('PYTHONHASHSEED', 'OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS', 'NUMEXPR_NUM_THREADS')
        if any(os.environ.get(k) != env[k] for k in keys):
            return subprocess.run([sys.executable, str(ROOT / 'portable.py'), 'index-graph'] + (['--preview'] if preview else []),
                cwd=ROOT, env=env).returncode
    module = __import__('index_development_' + kind)
    sys.argv = [module.__file__, '--repo', str(ROOT)] + (['--preview'] if preview else [])
    return module.main()


def doctor():
    sources()
    versions = {}
    for package in ('streamlit', 'pydantic', 'neo4j', 'requests', 'sentence-transformers', 'transformers',
                    'torch', 'numpy', 'chromadb', 'node2vec', 'gensim', 'networkx', 'scipy'):
        versions[package] = importlib.metadata.version(package)
    folder = ROOT / 'outputs/reproduction' / datetime.now(timezone.utc).strftime('environment-%Y%m%dT%H%M%S%fZ')
    folder.mkdir(parents=True)
    (folder / 'environment.json').write_text(json.dumps(dict(python=sys.version, packages=versions), indent=2) + '\n', encoding='utf-8')
    print('PASS: Application dependencies installed. Environment receipt: ' + str(folder))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=['check-sources', 'doctor', 'download-model', 'import-graph', 'index-text', 'index-graph', 'app', 'api'])
    parser.add_argument('--preview', action='store_true', help='Validate index inputs without indexing.')
    parser.add_argument('--uri', default='bolt://localhost:7687')
    parser.add_argument('--user', default='neo4j')
    parser.add_argument('--database', default='neo4j')
    parser.add_argument('--port', type=int, default=8000, help='Local API port (default: 8000).')
    parser.add_argument('--prompt-password', action='store_true', help='Prompt for the API Neo4j password without echoing it.')
    args = parser.parse_args()
    if not 1 <= args.port <= 65535:
        parser.error('Choose a port between 1 and 65535.')
    if sys.version_info[:2] != (3, 12):
        parser.error('Use Python 3.12 for the application environment.')
    try:
        if args.command == 'check-sources': sources()
        elif args.command == 'doctor': doctor()
        elif args.command == 'download-model': download()
        elif args.command == 'import-graph': import_graph(args.uri, args.user, args.database)
        elif args.command.startswith('index-'): return index(args.command[6:], args.preview)
        elif args.command == 'api':
            if any(importlib.util.find_spec(name) is None for name in ('fastapi', 'uvicorn')):
                print('Install requirements-api.txt in this application environment first.', file=sys.stderr)
                return 1
            env = os.environ.copy()
            # Environment settings remain usable with the default command.
            for option, name, value in (
                    ('--uri', 'THREATWEAVE_NEO4J_URI', args.uri),
                    ('--user', 'THREATWEAVE_NEO4J_USER', args.user),
                    ('--database', 'THREATWEAVE_NEO4J_DATABASE', args.database)):
                if any(arg == option or arg.startswith(option + '=') for arg in sys.argv[1:]):
                    env[name] = value
            if args.prompt_password:
                env['THREATWEAVE_NEO4J_PASSWORD'] = getpass.getpass('Password for YOUR Neo4j database: ')
            return subprocess.run([sys.executable, '-m', 'uvicorn', 'live_api:app',
                '--host', '127.0.0.1', '--port', str(args.port)], cwd=ROOT, env=env).returncode
        elif args.command == 'app':
            return subprocess.run([sys.executable, '-m', 'streamlit', 'run', str(ROOT / 'portable_app.py'),
                '--server.address=127.0.0.1', '--server.port=8501', '--server.headless=true',
                '--browser.gatherUsageStats=false', '--server.fileWatcherType=none'], cwd=ROOT).returncode
    except KeyboardInterrupt:
        print('\nStopped. Saved records remain in this checkout.')
        return 130
    except Exception as error:
        # Driver errors can contain connection details; avoid printing exception bodies.
        print('FAIL: ' + type(error).__name__ + '. Check installed dependencies, source checks and your local service settings.', file=sys.stderr)
        if args.command not in {'import-graph'} or isinstance(error, ValueError):
            print(str(error), file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

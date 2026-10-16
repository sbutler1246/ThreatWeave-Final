"""Record source-only evaluation scope and fixture projection without live services."""
import json
from datetime import datetime, timezone
from pathlib import Path
from uuid import uuid4

from evaluation.corpus_scope import EvaluationGraphRetriever, MITIGATION_RUN
from evaluation.text_sources import parents, prepare_records
from extraction.llama_tokenizer import sha256_file
from graph.development_projection import preview_projection, undirected_graph
from retrieval.development_text import load_tokenizer


def snapshot(repo,graph,selected,records,fingerprint):
    repo = Path(repo).resolve()
    projection,projection_hash,_,_ = preview_projection(graph)
    domain = undirected_graph(projection)
    import networkx as nx
    out = repo/'work/evaluation_scope_runs'/(datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')+'-'+uuid4().hex[:8])
    out.mkdir(parents=True)
    def save(name,value):
        (out/name).write_text(json.dumps(value,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    save('records.json',records)
    save('source_fixture_projection.json',projection)
    receipt = {'status':'offline_scope_prepared','service_calls':False,'live_graph_verified':False,
               'embedding_or_node2vec_fitted':False,'evaluation_scope':graph.config['evaluation_scope'],
               'development_scope':graph.config['development_scope'],'text_fingerprint':fingerprint,
               'source_fixture_projection_sha256':projection_hash,'cisa_scope_count':len(graph.profiles),
               'attack_reference_count':len(graph.references),'node_count':len(projection['nodes']),
               'directed_fact_count':len(projection['edges']),'undirected_edge_count':domain.number_of_edges(),
               'component_sizes':sorted((len(c) for c in nx.connected_components(domain)),reverse=True),
               'retrieval_chunk_count':len(records),'human_review_status':'pending',
               'files_sha256':{name:sha256_file(out/name) for name in ['records.json','source_fixture_projection.json']},
               'mitigation_import_run':MITIGATION_RUN,
               'note':'Source fixture is for offline checks only; operator builds live evaluation indexes separately.'}
    save('scope_receipt.json',receipt)
    print('OFFLINE SHARED EVALUATION SCOPE:',len(graph.profiles),'CISA windows;',len(graph.references),'reference parents;',
          len(records),'text chunks;',len(projection['nodes']),'nodes;',len(projection['edges']),'directed facts.')
    print('Saved scope:',out)
    return out


if __name__ == '__main__':
    repo = Path(__file__).resolve().parent
    graph = EvaluationGraphRetriever(repo)
    # Reuse the validated scope rather than reconstruct it a second time.
    selected,config = parents(repo,scope=(graph.profiles,graph.references,graph.expected_entities,graph.config))
    tokenizer = load_tokenizer(repo,config)
    records,_,fingerprint = prepare_records(repo,tokenizer,selected=selected,config=config)
    snapshot(repo,graph,selected,records,fingerprint)

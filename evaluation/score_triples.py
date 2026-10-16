"""Exact canonical triple scoring inside a declared complete annotation scope."""
import json
import sys
from pathlib import Path

def key(x): return (x['head_id'],x['predicate'],x['tail_id'])

def score(predictions,gold,scope):
    scopes=set(scope)
    if not scopes: raise ValueError('Complete annotated chunk scope is required')
    if not all(x.get('verified') is True for x in gold):
        raise ValueError('Gold triples require verification')
    expected={key(x) for x in gold if x['chunk_id'] in scopes}
    selected=[x for x in predictions if x['chunk_id'] in scopes and x.get('origin','extracted')=='extracted']
    actual={key(x) for x in selected}
    supported={key(x) for x in selected if x.get('evidence_valid') is True}
    tp=len(supported & expected); fp=len(actual)-tp; fn=len(expected)-tp
    precision=tp/(tp+fp) if tp+fp else None
    recall=tp/(tp+fn) if tp+fn else None
    undefined=[]
    if precision is None:undefined.append('precision')
    if recall is None:undefined.append('recall')
    f1=None if undefined else (2*precision*recall/(precision+recall) if precision+recall else 0.0)
    if f1 is None:undefined.append('f1')
    return {'tp':tp,'fp':fp,'fn':fn,'precision':precision,'recall':recall,
            'f1':f1,'undefined_metrics':undefined,'scope_chunks':len(scopes),
            'fused_predictions_excluded':sum(x.get('origin')=='fused' for x in predictions)}

if __name__=='__main__':
    pred=json.loads(Path(sys.argv[1]).read_text(encoding='utf-8'))
    gold=json.loads(Path(sys.argv[2]).read_text(encoding='utf-8'))
    if gold.get('annotation_scope_complete') is not True:
        raise ValueError('Complete human annotation of evaluation scope is required')
    print(json.dumps(score(pred,gold['triples'],gold['annotation_scope']),indent=2))

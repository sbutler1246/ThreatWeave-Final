"""Receipt-gated extension scope parity and complete saved source provenance."""
import copy
import json
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

from graph.corpus_extension_scope import MITIGATION_RUN
from graph.development_projection import freeze_projection, preview_projection
from graph.development_retrieval import DevelopmentGraphRetriever
from retrieval.development_text import parents
from retrieval.hybrid_retrieval import saved_projection_rows

REPO = Path(__file__).resolve().parents[1]
REVIEW_HASH = '46424ab5d763dbd5f97b8beebce27d24a98ff9108f70fe200e1d99d45437dd21'


class CorpusExtensionScopeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.graph = DevelopmentGraphRetriever(REPO)
        cls.projection,cls.fingerprint,cls.edges,cls.rows = preview_projection(cls.graph)

    def test_exact_receipt_gated_scope_and_domain_counts(self):
        g = self.graph
        self.assertEqual((len(g.profiles),len(g.references),len(g.expected_entities)),(53,139,142))
        self.assertEqual((len(self.projection['nodes']),len(self.projection['edges'])),(142,245))
        selected = [a for p in g.profiles.values() for a in p.get('accepted_assertions',{}).values()]
        self.assertEqual(len(selected),114)
        added = [a for a in selected if a['source_review_sha256']==REVIEW_HASH]
        self.assertEqual(len(added),27)
        self.assertEqual(len({a['chunk_id'] for a in added}),12)
        self.assertEqual({a['source_doc_id'] for a in added},{'AA24-038A','AA23-144A','AA22-321A'})
        self.assertTrue(all(a['source_review_disposition']=='supported' and a['human_review_status']=='pending' for a in selected))
        self.assertTrue(all(a['predicate'] in {'USES','USES_TECHNIQUE'} for a in added))
        self.assertTrue(all(n['type'] not in {'Document','Chunk','Assertion'} for n in self.projection['nodes']))

    def test_text_and_graph_share_every_exact_parent(self):
        selected,config = parents(REPO)
        expected = set(self.graph.profiles) | {r['chunk']['chunk_id'] for r in self.graph.references.values()}
        self.assertEqual(len(selected),192)
        self.assertEqual({c.chunk_id for _,c,_ in selected},expected)
        self.assertEqual(config['development_scope'],self.graph.config['development_scope'])
        for doc,chunk,_ in selected:
            self.assertEqual(doc.text[chunk.start:chunk.end],chunk.text)
            for context in chunk.inherited_context:
                self.assertEqual(doc.text[context.start:context.end],context.text)

    def test_saved_projection_roundtrip_keeps_all_reviewed_source_supports(self):
        rows = saved_projection_rows(SimpleNamespace(projection=self.projection),self.graph)
        projection,fingerprint = freeze_projection(self.graph,self.edges,rows)
        self.assertEqual(projection,self.projection)
        self.assertEqual(fingerprint,self.fingerprint)
        supports = [s['source_record'] for e in projection['edges'] for s in e['support'] if 'source_record' in s]
        self.assertEqual(len(supports),114)
        added = [a for a in supports if a['source_review_sha256']==REVIEW_HASH]
        self.assertEqual(len(added),27)
        recovered = [a for a in added if a['source_generation_status']=='validation_failed']
        self.assertEqual(len(recovered),2)
        self.assertTrue(all(json.loads(a['offline_selector_normalization_json'])[0]['original_relation_index']==2 for a in recovered))

    def test_extension_raw_recovery_and_review_tampering_is_rejected(self):
        row = next(r for r in self.rows if r['assertion'].get('source_review_sha256')==REVIEW_HASH)
        a = row['assertion']
        triple = a['head_id'],a['predicate'],a['tail_id']
        for key in ['source_review_sha256','source_generation_raw_file_sha256',
                    'offline_validation_receipt_sha256','offline_selector_normalization_json']:
            changed = copy.deepcopy(row)
            changed['assertion'][key] = 'changed'
            with self.subTest(key=key),self.assertRaisesRegex(ValueError,'pinned supported source review'):
                self.graph._verify_record(changed,*triple)

    def test_mitigation_receipt_and_saved_reference_tampering_block_scope(self):
        root = REPO/'work/corpus_extension_mitigations'/MITIGATION_RUN
        original = Path.read_text
        for filename in ['import_receipt.json','prepared_records.json']:
            def changed(path,*args,**kwargs):
                value = original(path,*args,**kwargs)
                if path==root/filename:
                    data = json.loads(value)
                    if filename=='import_receipt.json':
                        data['same_window_three_hop_chain_count'] = 2
                    else:
                        data['parts'][0]['records'][0]['assertion']['evidence_text'] = 'changed'
                    return json.dumps(data)
                return value
            with self.subTest(filename=filename),patch.object(Path,'read_text',changed):
                with self.assertRaises(ValueError):
                    DevelopmentGraphRetriever(REPO)

    def test_only_new_supported_windows_expand_scope_with_identical_retrieval_settings(self):
        old = DevelopmentGraphRetriever(REPO,include_corpus_extension=False)
        self.assertEqual((len(old.profiles),len(old.references)),(41,96))
        self.assertNotEqual(old.configuration_hash,self.graph.configuration_hash)
        self.assertNotEqual(old.config['development_scope']['sha256'],self.graph.config['development_scope']['sha256'])
        for key in ['retrieval','llm','chunking','text_embedding','node2vec']:
            self.assertEqual(old.config[key],self.graph.config[key])
        added = set(self.graph.profiles)-set(old.profiles)
        self.assertEqual(len(added),12)
        self.assertEqual({c.split(':')[0] for c in added},{'AA24-038A','AA23-144A','AA22-321A'})
        for c in added:
            profile = self.graph.profiles[c]
            self.assertTrue(all(a['source_review_sha256']==REVIEW_HASH for a in profile['accepted_assertions'].values()))


if __name__ == '__main__':
    unittest.main()

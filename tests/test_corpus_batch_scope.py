"""Receipt-gated batch expansion, source parity and multi-support graph provenance."""
import copy
import json
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

from graph.corpus_batch_scope import MITIGATION_RUN
from graph.development_projection import freeze_projection, preview_projection
from graph.development_retrieval import DevelopmentGraphRetriever
from retrieval.development_text import parents
from retrieval.hybrid_retrieval import saved_projection_rows

REPO = Path(__file__).resolve().parents[1]


class CorpusBatchScopeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.graph = DevelopmentGraphRetriever(REPO,include_corpus_extension=False)
        cls.projection, cls.fingerprint, cls.edges, cls.rows = preview_projection(cls.graph)

    def test_exact_accepted_scope_and_domain_counts(self):
        g = self.graph
        self.assertEqual((len(g.profiles),len(g.references),len(g.expected_entities)),(41,96,117))
        self.assertEqual((len(self.projection['nodes']),len(self.projection['edges'])),(117,179))
        approved = [a for p in g.profiles.values() for a in p.get('accepted_assertions',{}).values()]
        self.assertEqual(len(approved),87)
        batch = [a for a in approved if 'offline_validation_receipt_sha256' in a]
        self.assertEqual(len(batch),53)
        self.assertTrue(all(a['source_review_disposition']=='supported' for a in approved))
        self.assertTrue(all(a['human_review_status']=='pending' for a in approved))
        self.assertTrue(all(n['type'] not in {'Document','Chunk','Assertion'} for n in self.projection['nodes']))

    def test_all_repeated_facts_preserve_distinct_source_supports(self):
        supports = [s for e in self.projection['edges'] for s in e['support'] if 'source_record' in s]
        self.assertEqual(len(supports),87)
        self.assertEqual(len({s['assertion']['assertion_id'] for s in supports}),87)
        self.assertTrue(any(len(e['support'])>1 for e in self.projection['edges']))
        signatures = [(e['head_id'],e['predicate'],e['tail_id']) for e in self.projection['edges']]
        self.assertEqual(len(signatures),len(set(signatures)))
        for s in supports:
            a = s['source_record']
            profile = self.graph.profiles[a['chunk_id']]
            self.assertEqual(profile['document'].text[a['evidence_start']:a['evidence_end']],a['evidence_text'])

    def test_text_and_graph_share_all_exact_source_parents(self):
        selected, config = parents(REPO,include_corpus_extension=False)
        expected = set(self.graph.profiles) | {r['chunk']['chunk_id'] for r in self.graph.references.values()}
        self.assertEqual(len(selected),137)
        self.assertEqual({chunk.chunk_id for _,chunk,_ in selected},expected)
        self.assertEqual(config['development_scope'],self.graph.config['development_scope'])
        for doc,chunk,_ in selected:
            self.assertEqual(doc.text[chunk.start:chunk.end],chunk.text)

    def test_full_hybrid_projection_roundtrip_preserves_offline_recovery_metadata(self):
        rows = saved_projection_rows(SimpleNamespace(projection=self.projection),self.graph)
        restored, fingerprint = freeze_projection(self.graph,self.edges,rows)
        self.assertEqual(restored,self.projection)
        self.assertEqual(fingerprint,self.fingerprint)
        raw = [s['source_record'] for e in restored['edges'] for s in e['support']
               if 'offline_validation_receipt_sha256' in s.get('source_record',{})]
        self.assertEqual(len(raw),53)
        self.assertTrue(any(a['source_generation_status']=='validation_failed' for a in raw))

    def test_batch_recovery_metadata_tampering_is_rejected(self):
        row = next(r for r in self.rows if 'offline_validation_receipt_sha256' in r['assertion'])
        a = row['assertion']
        triple = a['head_id'],a['predicate'],a['tail_id']
        for key in ['source_generation_raw_file_sha256','offline_validation_receipt_sha256',
                    'offline_selector_normalization_json']:
            changed = copy.deepcopy(row)
            changed['assertion'][key] = 'changed'
            with self.subTest(key=key), self.assertRaisesRegex(ValueError,'pinned supported source review'):
                self.graph._verify_record(changed,*triple)

    def test_import_receipt_and_saved_reference_tampering_block_scope(self):
        folder = REPO/'work/corpus_batch_mitigations'/MITIGATION_RUN
        original = Path.read_text
        for filename in ['import_receipt.json','prepared_records.json']:
            def changed(target,*args,**kwargs):
                text = original(target,*args,**kwargs)
                if target == folder/filename:
                    data = json.loads(text)
                    if filename == 'import_receipt.json':
                        data['reference_assertion_count'] = 50
                    else:
                        data['parts'][0]['records'][0]['assertion']['evidence_text'] = 'changed'
                    return json.dumps(data)
                return text
            with self.subTest(filename=filename),patch.object(Path,'read_text',changed):
                with self.assertRaises(ValueError):
                    DevelopmentGraphRetriever(REPO)

    def test_source_identity_normalization_retains_only_matching_names(self):
        from graph.corpus_batch_scope import expand
        original = self.graph.expected_entities['local:AA23-319A:rhysida-actors']
        alternate = dict(original,name=original['name'].swapcase())
        profiles,references,entities = {},{},{alternate['canonical_id']:alternate}
        expand(REPO,profiles,references,entities)
        self.assertEqual(len(profiles),25)
        entities = {alternate['canonical_id']:dict(alternate,name='Unrelated group')}
        with self.assertRaisesRegex(ValueError,'identity conflicts'):
            expand(REPO,{},{},entities)

    def test_batch_scope_has_new_identity_with_frozen_retrieval_settings(self):
        old = DevelopmentGraphRetriever(REPO,include_corpus_batch=False)
        self.assertEqual(len(old.profiles),16)
        self.assertNotEqual(old.configuration_hash,self.graph.configuration_hash)
        self.assertNotEqual(old.config['development_scope']['sha256'],self.graph.config['development_scope']['sha256'])
        for key in ['retrieval','llm','chunking','text_embedding','node2vec']:
            self.assertEqual(old.config.get(key),self.graph.config.get(key))


if __name__ == '__main__':
    unittest.main()

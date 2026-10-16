"""Remaining-report source boundaries, frozen preparation and mocked extraction/resume."""
import copy
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from extraction import corpus_extension as extension
from extraction.corpus_batch import pending
from extraction.corpus_chunking import digest, load_verified_tokenizer
from extraction.corpus_pilot import configuration, run, save
from test_corpus_pilot import HttpFixture, Response, TokenizerFixture, fixture

REPO = Path(__file__).resolve().parents[1]


class CorpusExtensionPreparationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.prepared = extension.prepare(REPO)
        cls.items,cls.config,cls.catalog,cls.attack_hash,cls.identity,cls.plan = cls.prepared
        cls.checks = extension.preflight(cls.items,cls.config,cls.catalog,load_verified_tokenizer(REPO)[0])

    def test_exact_three_reports_and_disjoint_split_safe_selection(self):
        self.assertEqual([(d['doc_id'],d['chunk_count']) for d in self.identity['documents']],
                         [('AA24-038A',19),('AA23-144A',9),('AA22-321A',5)])
        scopes = self.plan['scope_ids']
        self.assertEqual(len(scopes),33)
        self.assertEqual(len(set(scopes)),33)
        self.assertEqual(len(self.plan['excluded_prior_scope_ids']),54)
        self.assertTrue(set(scopes).isdisjoint(self.plan['excluded_prior_scope_ids']))
        self.assertTrue(set(extension.DOCUMENTS).isdisjoint(self.plan['excluded_held_out_reports']))
        self.assertEqual(len(self.plan['excluded_held_out_reports']),7)
        self.assertEqual(self.plan['fingerprint'],digest({k:v for k,v in self.plan.items() if k!='fingerprint'}))
        self.assertEqual(self.identity['fingerprint'],digest({k:v for k,v in self.identity.items() if k!='fingerprint'}))

    def test_complete_technical_section_coverage_and_exact_contexts(self):
        for source in self.identity['documents']:
            covered = set()
            for item in self.items:
                if item['document'].doc_id != source['doc_id']:
                    continue
                doc,chunk = item['document'],item['chunk']
                self.assertEqual(doc.text[chunk.start:chunk.end],chunk.text)
                self.assertTrue(source['technical_start']<=chunk.start<chunk.end<=source['technical_end'])
                self.assertTrue(400<=item['preparation']['source_tokens']<=600)
                for c in chunk.inherited_context:
                    self.assertEqual(doc.text[c.start:c.end],c.text)
                covered.update(range(chunk.start,chunk.end))
            self.assertEqual(covered,set(range(source['technical_start'],source['technical_end'])))

    def test_frozen_generation_and_all_prompt_budgets(self):
        settings = configuration(self.config,self.identity,self.attack_hash)
        self.assertEqual(settings['options'],{'temperature':0,'num_ctx':8192,'num_predict':700})
        self.assertEqual(settings['bounds']['relations'],4)
        self.assertEqual(self.plan['configuration_hash'],digest(settings))
        self.assertEqual(len(self.checks),33)
        self.assertTrue(all(r['within_budget'] and r['estimated_total_tokens']<=8192 for r in self.checks))
        self.assertEqual(sum(not r['mention_count'] for r in self.checks),2)
        self.assertEqual([r['scope_id'] for r in self.checks],self.plan['scope_ids'])

    def test_changed_split_manifest_selection_or_duplicate_sources_are_rejected(self):
        manifest = json.loads((REPO/'benchmarks/corpus_manifest.json').read_text(encoding='utf-8'))
        split = json.loads((REPO/'benchmarks/split_manifest.json').read_text(encoding='utf-8'))
        for change in ['blocked','missing','duplicate','added']:
            m,s = copy.deepcopy(manifest),copy.deepcopy(split)
            if change=='blocked':
                s['held_out_evidence_scopes'].append('AA24-038A:heldout:test')
            elif change=='missing':
                m['documents'] = [d for d in m['documents'] if d['doc_id']!='AA22-321A']
            elif change=='duplicate':
                m['documents'].append(copy.deepcopy(m['documents'][0]))
            else:
                m['documents'].append({'doc_id':'unknown-source'})
            with self.subTest(change=change),self.assertRaises(ValueError):
                extension.selection(m,s)

    def test_changed_frozen_source_is_rejected(self):
        original = Path.read_text
        target = REPO/'data/AA22-321A.txt'
        def changed(path,*args,**kwargs):
            value = original(path,*args,**kwargs)
            return value+'changed source' if path==target else value
        with patch.object(Path,'read_text',changed),self.assertRaisesRegex(ValueError,'source checksum changed'):
            extension.prepare(REPO)

    def test_saved_preparation_reconstructs_and_tampering_blocks_extraction(self):
        # Use the exact already-reconstructed source inputs to focus this check on saved artifacts.
        with patch.object(extension,'prepare',return_value=self.prepared),patch.object(
                extension,'preflight',return_value=self.checks):
            values = extension.read_prepared(REPO)
            self.assertEqual(values[-1],self.plan)
            root = values[-2]
            original = Path.read_text
            for filename in ['chunks.json','preflight.json','summary.json']:
                def changed(path,*args,**kwargs):
                    value = original(path,*args,**kwargs)
                    if path==root/filename:
                        data = json.loads(value)
                        if filename=='chunks.json':
                            data[0]['chunk']['text'] = 'changed source'
                        elif filename=='preflight.json':
                            data[0]['prompt_hash'] = 'changed prompt'
                        else:
                            data['model_calls'] = True
                        return json.dumps(data)
                    return value
                with self.subTest(filename=filename),patch.object(Path,'read_text',changed):
                    with self.assertRaisesRegex(ValueError,'preflight changed'):
                        extension.read_prepared(REPO)


class CorpusExtensionRunnerTests(unittest.TestCase):
    def setUp(self):
        root = REPO/'work/corpus_extension_tests'
        root.mkdir(parents=True,exist_ok=True)
        temporary = tempfile.TemporaryDirectory(dir=root)
        self.addCleanup(temporary.cleanup)
        self.repo = Path(temporary.name)
        (self.repo/'docs').mkdir()
        self.config = {'llm':{'model':'llama3.1:8b','temperature':0,'num_ctx':8192,'num_predict':700}}
        self.identity = {'fingerprint':'f'*64}
        self.items = [fixture('Group Alpha actors used Tool Beta.') for _ in range(2)]
        for i,item in enumerate(self.items):
            item['chunk'].chunk_id += str(i)
        self.plan = {'purpose':'remaining_three_development_report_extraction',
                     'configuration_hash':digest(configuration(self.config,self.identity,'a'*64)),
                     'scope_ids':[i['chunk'].chunk_id for i in self.items]}

    def generate(self,items,responses,resume=None):
        http = HttpFixture()
        root = self.repo/'work'/extension.OUTPUT_KIND
        before = set(root.iterdir()) if root.exists() else set()
        with patch('requests.Session',return_value=http),patch.object(http,'post',side_effect=responses),patch(
                'extraction.corpus_pilot.load_verified_tokenizer',return_value=(TokenizerFixture(),{})):
            code = run(self.repo,items,self.config,[],'a'*64,self.identity,self.repo/'prepared',
                       retry_of=resume,batch_plan=self.plan,output_kind=extension.OUTPUT_KIND)
        return code,next(p for p in root.iterdir() if p not in before)

    def test_mocked_extraction_isolated_and_repeated_completed_empty_results_skipped(self):
        empty = Response({'done':True,'done_reason':'stop','response':'{"relations":[]}'})
        code,folder = self.generate(self.items,[empty,empty])
        self.assertEqual(code,0)
        summary = json.loads((folder/'summary.json').read_text(encoding='utf-8'))
        self.assertEqual(summary['purpose'],self.plan['purpose'])
        self.assertFalse(summary['graph_writes'])
        self.assertEqual(summary['empty_scopes'],2)
        self.assertFalse((self.repo/'work/corpus_extraction_batch').exists())
        self.assertEqual(pending(self.repo,self.items,[],self.plan,folder,output_kind=extension.OUTPUT_KIND),([],2))
        with self.assertRaises(ValueError):
            pending(self.repo,self.items,[],self.plan,folder)

    def test_mocked_failed_window_resumes_without_repeating_successes(self):
        empty = Response({'done':True,'done_reason':'stop','response':'{"relations":[]}'})
        code,folder = self.generate(self.items,[empty,Response({'error':'offline'},503)])
        self.assertEqual(code,1)
        rest,count = pending(self.repo,self.items,[],self.plan,folder,output_kind=extension.OUTPUT_KIND)
        self.assertEqual((rest,count),([self.items[1]],1))
        code,second = self.generate(rest,[empty],folder)
        self.assertEqual(code,0)
        self.assertEqual(pending(self.repo,self.items,[],self.plan,second,output_kind=extension.OUTPUT_KIND),([],2))
        summary = json.loads((second/'summary.json').read_text(encoding='utf-8'))
        summary['retry_of'] = str(second)
        save(second/'summary.json',summary)
        with self.assertRaises(ValueError):
            pending(self.repo,self.items,[],self.plan,second,output_kind=extension.OUTPUT_KIND)

    def test_unknown_output_kind_is_rejected_before_creating_files(self):
        with self.assertRaisesRegex(ValueError,'output kind'):
            run(self.repo,[],self.config,[],'a'*64,self.identity,self.repo/'prepared',output_kind='../outside')
        with self.assertRaisesRegex(ValueError,'output kind'):
            pending(self.repo,[],[],self.plan,self.repo,output_kind='../outside')


if __name__ == '__main__':
    unittest.main()

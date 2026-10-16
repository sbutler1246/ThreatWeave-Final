import json
import unittest

from extraction.corpus_batch_review import unique_selection
from extraction.source_choices import make_prompt, validate_output
from test_source_choices import item, selector


class BatchReviewTests(unittest.TestCase):
    def test_duplicate_relationship_drops_only_later_support_and_keeps_raw_unchanged(self):
        source = item('Group Alpha actors used Tool Beta.\nGroup Alpha actors deployed Tool Beta.')
        _, _, _, index = make_prompt(source, [])
        relation = {'head':selector(index,'Group Alpha actors','ThreatGroup'), 'predicate':'USES',
                    'tail':selector(index,'Tool Beta','Software'), 'unit_ids':['u001'], 'context_ids':[]}
        other = dict(relation, unit_ids=['u002'])
        raw = json.dumps({'relations':[relation,other]})
        with self.assertRaisesRegex(ValueError,'Repeated'):
            validate_output(raw, source, [], index)
        derived, changes = unique_selection(raw,index)
        batch, _, _ = validate_output(derived, source, [], index)
        self.assertEqual(len(batch.relations),1)
        self.assertEqual(json.loads(raw)['relations'],[relation,other])
        self.assertEqual(changes[0]['removed_selection'],other)
        self.assertEqual(changes[0]['retained_original_relation_index'],0)

    def test_distinct_relationships_are_not_dropped(self):
        source = item('Group Alpha actors used Tool Beta.\nGroup Alpha actors used Tool Gamma.')
        _, _, _, index = make_prompt(source, [])
        relations = [{'head':selector(index,'Group Alpha actors','ThreatGroup'),'predicate':'USES',
                      'tail':selector(index,name,'Software'),'unit_ids':[unit],'context_ids':[]}
                     for name,unit in [('Tool Beta','u001'),('Tool Gamma','u002')]]
        raw = json.dumps({'relations':relations})
        derived, changes = unique_selection(raw,index)
        self.assertEqual(json.loads(derived),json.loads(raw))
        self.assertEqual(changes,[])

    def test_normalization_does_not_accept_unknown_selectors(self):
        with self.assertRaises(ValueError):
            unique_selection('{"relations":[{"head":"unknown","tail":"unknown","predicate":"USES","unit_ids":["u001"]}]}',
                             {'identities':{}})

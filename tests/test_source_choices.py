import json
import unittest

from extraction.source_choices import has_mention, index_source, make_prompt, validate_output
from schemas import Chunk, Document, Entity, SourceContext


def item(text, prefix=''):
    full = prefix+text
    return {'chunk': Chunk(chunk_id='sample:development:test', doc_id='sample', start=len(prefix), end=len(full), text=text),
            'document': Document(doc_id='sample', title=prefix.strip() or 'Source', source_url='https://example.org/source',
                                 text=full, content_hash='a'*64), 'spec': {'kind': 'prose'}}


def selector(index, name, kind):
    return next(key for key, value in index['choices'].items() if value['name'] == name and value['type'] == kind)


class SourceChoiceTests(unittest.TestCase):
    def selection(self, index, units=None, contexts=None):
        return {'relations': [{'head': selector(index, 'Group Alpha actors', 'ThreatGroup'), 'predicate': 'USES',
                'tail': selector(index, 'Tool Beta', 'Software'), 'unit_ids': units or ['u001'], 'context_ids': contexts or []}]}

    def test_short_catalog_words_need_local_command_or_software_context(self):
        catalog = [Entity(canonical_id='attack:S0110', type='Software', name='at',
                          attack_id='S0110', resolution_status='canonical'),
                   Entity(canonical_id='attack:S0039', type='Software', name='net',
                          attack_id='S0039', resolution_status='canonical')]
        source = item('Group Alpha actors used Tool Beta malware at times. At times it failed.\n'
                      'Group Alpha actors ran at 13:37 task.exe.\n'
                      'net user /domain [T1087.002]\n')
        index = index_source(source, catalog)
        at = index['choices'][selector(index, 'at', 'Software')]
        self.assertFalse(has_mention(at, 'Group Alpha actors used Tool Beta malware at times.'))
        self.assertFalse(has_mention(at, 'At times it failed.'))
        self.assertTrue(has_mention(at, 'Group Alpha actors ran at 13:37 task.exe.'))
        self.assertTrue(has_mention(index['choices'][selector(index, 'net', 'Software')], 'net user /domain [T1087.002]'))
        only_prose = index_source(item('Group Alpha actors used Tool Beta malware at times.'), catalog)
        self.assertFalse(any(value['name'] == 'at' for value in only_prose['choices'].values()))

    def test_actor_software_scope_is_preserved_instead_of_generic_actor_names(self):
        source = item('Threat actors leveraging Solar ransomware used Tool Beta.\n'
                      'Threat actors leveraging Lunar have deployed Tool Gamma.\n')
        _, _, schema, index = make_prompt(source, [])
        actors = {choice['name'] for choice in index['choices'].values() if choice['type'] == 'ThreatGroup'}
        self.assertIn('Threat actors leveraging Solar ransomware', actors)
        self.assertIn('Threat actors leveraging Lunar', actors)
        self.assertNotIn('Threat actors', actors)
        value = {'relations': [{'unit_ids':['u001'], 'context_ids':[],
                 'head':selector(index, 'Threat actors leveraging Solar ransomware', 'ThreatGroup'),
                 'predicate':'USES', 'tail':selector(index, 'Tool Beta', 'Software')}]}
        batch, _, aligned = validate_output(json.dumps(value), source, [], index)
        self.assertEqual(batch.entities[0].name, 'Threat actors leveraging Solar ransomware')
        self.assertEqual(aligned[0]['document_start'], 0)

    def test_explicit_table_aliases_share_reported_id_without_global_alias_changes(self):
        from jsonschema import Draft202012Validator
        source = item('Table 1: Malware Used by Group Alpha actors\nMalware\nUse\n'
                      'SolarTool (also known as OrbitTool [S0001])\nEnables remote access.\n')
        catalog = [Entity(canonical_id='attack:S0001', type='Software', name='OrbitTool',
                          attack_id='S0001', resolution_status='canonical')]
        _, _, schema, index = make_prompt(source, catalog)
        primary = selector(index, 'SolarTool', 'Software')
        alias = selector(index, 'OrbitTool', 'Software')
        self.assertEqual(index['choices'][primary]['attack_id'], 'S0001')
        self.assertEqual(index['identities'][primary], index['identities'][alias])
        offered = {tail for p in index['evidence_patterns'] for tail in p['tails']}
        self.assertEqual(len(offered & {primary, alias}), 1)
        relation = {'unit_ids':['u001','u004'], 'context_ids':[],
                    'head':selector(index, 'Group Alpha actors', 'ThreatGroup'),
                    'predicate':'USES', 'tail':next(iter(offered & {primary, alias}))}
        self.assertTrue(Draft202012Validator(schema).is_valid({'relations':[relation]}))
        batch, resolution, _ = validate_output(json.dumps({'relations':[relation]}), source, catalog, index)
        self.assertEqual(batch.entities[1].attack_id, 'S0001')
        self.assertEqual(resolution[1]['canonical_id'], 'attack:S0001')
        self.assertEqual(catalog[0].aliases, [])
        # An alias-looking prose sentence is outside the row-scoped identity rule.
        prose = index_source(item('SolarTool (also known as OrbitTool [S0001]) is discussed.'), catalog)
        self.assertFalse(any(value['name'] == 'SolarTool' and value['attack_id'] for value in prose['choices'].values()))

    def test_conflicting_source_alias_ids_are_not_silently_selected(self):
        source = item('Table 1: Malware Used by Group Alpha actors\nMalware\nUse\n'
                      'SolarTool (also known as OrbitTool [S0001])\nEnables remote access.\n'
                      'SolarTool (also known as OtherTool [S0002])\nEnables remote access.\n')
        index = index_source(source, [])
        self.assertFalse(any(value['name'] == 'SolarTool' for value in index['choices'].values()))

    def test_unknown_source_ids_are_recorded_but_not_offered_as_executable_choices(self):
        from jsonschema import Draft202012Validator
        source = item('Group Alpha actors used S9999.')
        _, _, schema, index = make_prompt(source, [])
        key = selector(index, 'S9999', 'Software')
        self.assertIn(key, index['unavailable_choices'])
        self.assertEqual(index['evidence_patterns'], [])
        self.assertTrue(Draft202012Validator(schema).is_valid({'relations':[]}))
        self.assertFalse(Draft202012Validator(schema).is_valid({'relations':[{}]}))

    def test_conditionals_are_flagged_without_hiding_definite_behavior(self):
        source = item('If Group Alpha actors gain access, they use Tool Beta.\n'
                      'Group Alpha actors use Tool Beta.\n')
        _, _, _, index = make_prompt(source, [])
        value = self.selection(index)
        _, _, aligned = validate_output(json.dumps(value), source, [], index)
        self.assertIn('source_conditional_wording', aligned[0]['review_flags'])
        value['relations'][0]['unit_ids'] = ['u002']
        _, _, aligned = validate_output(json.dumps(value), source, [], index)
        self.assertEqual(aligned[0]['review_flags'], [])

    def test_model_visible_options_match_schema_and_still_allow_abstention(self):
        from itertools import product
        from jsonschema import Draft202012Validator
        for text in ['Group Alpha actors used Tool Beta.\nGroup Alpha actors did not use Tool Gamma.',
                     'no named entities here.']:
            with self.subTest(text=text):
                source = item(text)
                system, prompt, schema, index = make_prompt(source, [])
                options = json.loads(prompt.split('\nEVIDENCE_OPTIONS (literal/type possibilities, not asserted facts):\n')[1])
                self.assertEqual(options, index['evidence_patterns'])
                validator = Draft202012Validator(schema)
                self.assertTrue(validator.is_valid({'relations': []}))
                self.assertIn('including unsupported or negated ones', system)
                self.assertEqual(len(schema['properties']['relations']['items'].get('anyOf', [])), len(options))
                for option in options:
                    for head, tail in product(option['heads'], option['tails']):
                        relation = {key: option[key] for key in ['unit_ids', 'context_ids', 'predicate']}
                        relation.update(head=head, tail=tail)
                        self.assertTrue(validator.is_valid({'relations': [relation]}))
                if options:
                    # An explicit negative example remains a possibility requiring
                    # model judgment; the menu must not silently turn it into a fact.
                    gamma = selector(index, 'Tool Gamma', 'Software')
                    self.assertTrue(any(gamma in option['tails'] for option in options))

    def test_sentence_and_annotated_list_boundaries_prevent_cross_tool_ids(self):
        from jsonschema import Draft202012Validator
        source = item('ProbeAlpha [T1016], ProbeBeta [T1482], and NetTool collected data. Another sentence.', prefix='Heading café\n')
        catalog = [Entity(canonical_id='attack:'+identifier, type=kind, name=name,
                          attack_id=identifier, resolution_status='canonical') for identifier,kind,name in [
                          ('S0001','Software','ProbeAlpha'),('S0002','Software','ProbeBeta'),
                          ('S0003','Software','NetTool'),('T1016','Technique','Network Configuration'),
                          ('T1482','Technique','Domain Trust Discovery')]]
        _, _, schema, index = make_prompt(source, catalog)
        self.assertEqual(len(index['units']), 4)
        for unit in index['units'].values():
            self.assertEqual(source['chunk'].text[unit['start']:unit['end']], unit['text'])
        value = {'relations': [{'unit_ids': ['u001'], 'context_ids': [],
                 'head': selector(index, 'ProbeAlpha', 'Software'), 'predicate': 'USES_TECHNIQUE',
                 'tail': selector(index, 'T1016', 'Technique')}]}
        self.assertTrue(Draft202012Validator(schema).is_valid(value))
        _, _, aligned = validate_output(json.dumps(value), source, catalog, index)
        self.assertEqual(aligned[0]['document_start'], len('Heading café\n'))
        value['relations'][0]['head'] = selector(index, 'NetTool', 'Software')
        self.assertFalse(Draft202012Validator(schema).is_valid(value))
        with self.assertRaises(ValueError):
            validate_output(json.dumps(value), source, catalog, index)

    def test_same_line_pronoun_pair_keeps_actor_attribution_but_other_named_actor_does_not(self):
        from jsonschema import Draft202012Validator
        catalog = [Entity(canonical_id='attack:T1598', type='Technique', name='Phishing for Information',
                          attack_id='T1598', resolution_status='canonical')]
        for subject, expected in [('Actors',True),('Group Beta actors',False)]:
            source = item('Group Alpha actors gained access. '+subject+' used T1598.')
            _, _, schema, index = make_prompt(source, catalog)
            value = {'relations': [{'unit_ids': ['u001','u002'], 'context_ids': [],
                     'head': selector(index, 'Group Alpha actors', 'ThreatGroup'), 'predicate': 'USES_TECHNIQUE',
                     'tail': selector(index, 'T1598', 'Technique')}]}
            self.assertEqual(Draft202012Validator(schema).is_valid(value), expected)

    def test_independent_full_actor_phrases_retain_each_qualifier(self):
        from jsonschema import Draft202012Validator
        source = item('Some Group Alpha affiliates exfiltrate files. Group Alpha affiliates used Tool Beta.')
        _, _, schema, index = make_prompt(source, [])
        self.assertTrue(any(v['name'] == 'Some Group Alpha affiliates' and v['type'] == 'ThreatGroup'
                            for v in index['choices'].values()))
        value = {'relations': [{'unit_ids': ['u002'], 'context_ids': [],
                 'head': selector(index, 'Group Alpha affiliates', 'ThreatGroup'), 'predicate': 'USES',
                 'tail': selector(index, 'Tool Beta', 'Software')}]}
        self.assertTrue(Draft202012Validator(schema).is_valid(value))
        value['relations'][0]['head'] = selector(index, 'Some Group Alpha affiliates', 'ThreatGroup')
        self.assertFalse(Draft202012Validator(schema).is_valid(value))

    def test_unrelated_affiliate_sentence_does_not_rename_selected_actor(self):
        source = item('Group Alpha actors used Tool Beta.\nGroup Alpha affiliates used Tool Gamma.')
        _, _, _, index = make_prompt(source, [])
        value = {'relations': [{'unit_ids': ['u001'], 'context_ids': [],
                 'head': selector(index, 'Group Alpha actors', 'ThreatGroup'), 'predicate': 'USES',
                 'tail': selector(index, 'Tool Beta', 'Software')}]}
        batch, _, _ = validate_output(json.dumps(value), source, [], index)
        self.assertEqual(len(batch.relations), 1)

    def test_complete_unknown_list_names_do_not_emit_prefixes_or_actor_alias_software(self):
        source = item('Group Alpha actors deploy software such as Orbit sync and StarDesk in preparation for access.\n'
                      'Group Alpha actors use native BrickOS tools.\n'
                      'This lists tools Delta Group repurposed. Delta Group actors used remote services.\n')
        catalog = [Entity(canonical_id='attack:G9999', type='ThreatGroup', name='Delta Group',
                          attack_id='G9999', resolution_status='canonical')]
        index = index_source(source, catalog)
        names = {choice['name'] for choice in index['choices'].values() if choice['type'] == 'Software'}
        self.assertIn('Orbit sync', names)
        self.assertIn('StarDesk', names)
        self.assertNotIn('Orbit', names)
        self.assertNotIn('BrickOS', names)
        self.assertNotIn('Delta Group', names)

    def test_canonical_name_id_duplicates_are_not_separate_selectable_relationships(self):
        from jsonschema import Draft202012Validator
        source = item('Group Alpha actors used SolarTool [S0001].')
        catalog = [Entity(canonical_id='attack:S0001', type='Software', name='SolarTool',
                          attack_id='S0001', resolution_status='canonical')]
        _, _, schema, index = make_prompt(source, catalog)
        value = {'relations': [{'unit_ids': ['u001'], 'context_ids': [],
                 'head': selector(index, 'Group Alpha actors', 'ThreatGroup'), 'predicate': 'USES',
                 'tail': selector(index, 'SolarTool', 'Software')}]}
        self.assertTrue(Draft202012Validator(schema).is_valid(value))
        duplicate = dict(value['relations'][0], tail=selector(index, 'S0001', 'Software'))
        self.assertFalse(Draft202012Validator(schema).is_valid({'relations': [duplicate]}))
        value['relations'].append(duplicate)
        with self.assertRaisesRegex(ValueError, 'Repeated selected relationship'):
            validate_output(json.dumps(value), source, catalog, index)

    def test_table_scope_survives_a_description_split_into_sentences(self):
        from jsonschema import Draft202012Validator
        source = item('Table 1: Tools Used by Group Alpha actors\nName\nDescription\n'
                      'ProbeAlpha\nEnables remote control. Calls native APIs [T1055.002].\n'
                      'ProbeBeta\nEnables remote control.\n')
        catalog = [Entity(canonical_id='attack:T1055.002', type='Technique', name='Portable Executable Injection',
                          attack_id='T1055.002', resolution_status='canonical')]
        _, _, schema, index = make_prompt(source, catalog)
        value = {'relations': [{'unit_ids': ['u001','u007'], 'context_ids': [],
                 'head': selector(index, 'Group Alpha actors', 'ThreatGroup'), 'predicate': 'USES',
                 'tail': selector(index, 'ProbeBeta', 'Software')}]}
        self.assertTrue(Draft202012Validator(schema).is_valid(value))
        value['relations'][0] = {'unit_ids': ['u004','u006'], 'context_ids': [],
                 'head': selector(index, 'ProbeAlpha', 'Software'), 'predicate': 'USES_TECHNIQUE',
                 'tail': selector(index, 'T1055.002', 'Technique')}
        self.assertTrue(Draft202012Validator(schema).is_valid(value))
        self.assertEqual(len(validate_output(json.dumps(value), source, catalog, index)[0].relations), 1)

    def test_unknown_software_requires_naming_context_not_a_capitalized_verb_or_reference(self):
        source = item('Posed as company IT staff using phone calls [T1598].\n'
                      'Uses malware as part of its TTPs. See Table 2.\n'
                      'See Appendix: Windows PowerShell and Command Shell Activity.\n'
                      'Group Alpha actors deploy remote access software such as NewTool and OtherTool.\n'
                      'PortProbe, a network scanner, discovers open ports.\n'
                      'NovaLoader invokes native memory API functions.\n'
                      'Run sample.exe to start the test.\n')
        index = index_source(source, [])
        names = {value['name'] for value in index['choices'].values() if value['type'] == 'Software'}
        for name in ['Posed', 'IT', 'TTPs. See Table', 'See Table', 'Windows PowerShell', 'Command Shell Activity']:
            self.assertNotIn(name, names)
        for name in ['NewTool', 'OtherTool', 'PortProbe', 'NovaLoader', 'sample.exe']:
            self.assertIn(name, names)

    def test_unknown_table_row_names_remain_available(self):
        source = item('Table 1: Tools Used by Group Alpha actors\nTool\nIntended Use\n'
                      'NewRemote.io\nEnables remote control.\n')
        index = index_source(source, [])
        self.assertTrue(any(value['name'] == 'NewRemote.io' and value['type'] == 'Software'
                            for value in index['choices'].values()))

    def test_catalog_behavior_names_require_their_exact_id_in_selected_units(self):
        catalog = [Entity(canonical_id='attack:T1589.001', type='Technique', name='Credentials',
                          attack_id='T1589.001', resolution_status='canonical')]
        source = item('Group Alpha actors used compromised credentials for access.\n'
                      'Credentials [T1589.001] are listed separately.\n')
        _, _, schema, index = make_prompt(source, catalog)
        # Case-preserving lowercase use has no local identifier and is not typed
        # as an ATT&CK behavior just because the catalog contains that noun.
        self.assertFalse(any(value['name'] == 'credentials' and value['type'] == 'Technique'
                             for value in index['choices'].values()))
        choice = index['choices'][selector(index, 'Credentials', 'Technique')]
        self.assertEqual(choice['attack_id'], 'T1589.001')
        self.assertFalse(has_mention(choice, 'Credentials were used for access.'))
        self.assertTrue(has_mention(choice, 'Credentials [T1589.001]'))

    def test_actor_name_substrings_cannot_supply_an_independent_software_endpoint(self):
        software = {'name': 'Crimson', 'type': 'Software', 'attack_id': None}
        self.assertFalse(has_mention(software, 'Crimson actors used remote services.'))
        self.assertTrue(has_mention(software, 'Crimson actors deployed Crimson ransomware.'))
        catalog = [Entity(canonical_id='attack:S9999', type='Software', name='Crimson',
                          attack_id='S9999', resolution_status='canonical')]
        from jsonschema import Draft202012Validator
        source = item('Crimson actors used remote services.')
        _, _, schema, _ = make_prompt(source, catalog)
        self.assertEqual(schema['properties']['relations']['maxItems'], 0)
        source = item('Crimson actors deployed Crimson ransomware.')
        _, _, schema, index = make_prompt(source, catalog)
        value = {'relations': [{'unit_ids': ['u001'], 'context_ids': [],
                 'head': selector(index, 'Crimson actors', 'ThreatGroup'), 'predicate': 'USES',
                 'tail': selector(index, 'Crimson', 'Software')}]}
        self.assertTrue(Draft202012Validator(schema).is_valid(value))

    def test_missing_caption_requires_empty_context_array_without_empty_enum(self):
        from jsonschema import Draft202012Validator
        source = item('Group Alpha actors used Tool Beta.')
        _, _, schema, index = make_prompt(source, [])
        branches = schema['properties']['relations']['items']['anyOf']
        self.assertTrue(all(branch['properties']['context_ids'] == {'const': []} for branch in branches))
        self.assertNotIn('"enum": []', json.dumps(schema))
        validator = Draft202012Validator(schema)
        value = self.selection(index)
        self.assertTrue(validator.is_valid(value))
        value['relations'][0]['context_ids'] = ['ctx1']
        self.assertFalse(validator.is_valid(value))
        with self.assertRaises(ValueError):
            validate_output(json.dumps(value), source, [], index)

    def test_caption_schema_keeps_only_available_caption_ids(self):
        from jsonschema import Draft202012Validator
        prefix = 'Table 1: Tools Used by Group Alpha actors\n'
        source = item('Tool Beta enables remote control.', prefix=prefix)
        source['chunk'].inherited_context = [SourceContext(start=0, end=len(prefix)-1, text=prefix.rstrip())]
        _, _, schema, index = make_prompt(source, [])
        validator = Draft202012Validator(schema)
        self.assertTrue(validator.is_valid(self.selection(index, contexts=['ctx1'])))
        self.assertFalse(validator.is_valid(self.selection(index, contexts=['ctx2'])))

    def test_no_selectable_endpoints_allows_only_empty_relations(self):
        from jsonschema import Draft202012Validator
        for text in ['no named entities here.', 'TA0001']:
            with self.subTest(text=text):
                source = item(text)
                _, _, schema, index = make_prompt(source, [])
                self.assertNotIn('"enum": []', json.dumps(schema))
                validator = Draft202012Validator(schema)
                self.assertTrue(validator.is_valid({'relations': []}))
                self.assertFalse(validator.is_valid({'relations': [{}]}))
                batch, _, _ = validate_output('{"relations":[]}', source, [], index)
                self.assertEqual(batch.relations, [])

    def test_schema_rejects_globally_valid_endpoint_from_wrong_unit(self):
        from jsonschema import Draft202012Validator
        source = item('Group Alpha actors used Tool Beta.\nGroup Alpha actors used Tool Gamma.')
        _, _, schema, index = make_prompt(source, [])
        value = self.selection(index)
        value['relations'][0]['tail'] = selector(index, 'Tool Gamma', 'Software')
        self.assertFalse(Draft202012Validator(schema).is_valid(value))
        with self.assertRaises(ValueError):
            validate_output(json.dumps(value), source, [], index)
        value['relations'][0]['unit_ids'] = ['u002']
        self.assertTrue(Draft202012Validator(schema).is_valid(value))
        self.assertEqual(len(validate_output(json.dumps(value), source, [], index)[0].relations), 1)

    def test_schema_enforces_predicate_type_with_literal_id_and_keeps_uncertainty_flag(self):
        from jsonschema import Draft202012Validator
        source = item('Group Alpha actors may use T1078.')
        catalog = [Entity(canonical_id='attack:T1078', type='Technique', name='Valid Accounts',
                          aliases=[], attack_id='T1078', resolution_status='canonical')]
        _, _, schema, index = make_prompt(source, catalog)
        value = {'relations': [{'unit_ids': ['u001'], 'context_ids': [],
                 'head': selector(index, 'Group Alpha actors', 'ThreatGroup'), 'predicate': 'USES_TECHNIQUE',
                 'tail': selector(index, 'T1078', 'Technique')}]}
        validator = Draft202012Validator(schema)
        self.assertTrue(validator.is_valid(value))
        _, _, alignments = validate_output(json.dumps(value), source, catalog, index)
        self.assertIn('source_uncertainty_wording', alignments[0]['review_flags'])
        value['relations'][0]['predicate'] = 'USES'
        self.assertFalse(validator.is_valid(value))

    def test_inline_caption_can_scope_a_tool_row_but_not_following_hash_table(self):
        from jsonschema import Draft202012Validator
        source = item('Table 1: Tools Leveraged by Group Alpha Actors\nName\nDescription\nTool Beta\n'
                      'Enables remote control.\nTable 2: MD5 Hashes\nTool Gamma\nA file hash.\n')
        _, _, schema, index = make_prompt(source, [])
        value = {'relations': [{'unit_ids': ['u001','u004'], 'context_ids': [],
                 'head': selector(index, 'Group Alpha Actors', 'ThreatGroup'), 'predicate': 'USES',
                 'tail': selector(index, 'Tool Beta', 'Software')}]}
        self.assertTrue(Draft202012Validator(schema).is_valid(value))
        batch, _, aligned = validate_output(json.dumps(value), source, [], index)
        self.assertEqual(aligned[0]['selected_unit_ids'], ['u001','u004'])
        self.assertEqual(source['chunk'].text[batch.relations[0].evidence.start:batch.relations[0].evidence.end],
                         batch.relations[0].evidence.quote)
        value['relations'][0].update(unit_ids=['u001','u007'], tail=selector(index, 'Tool Gamma', 'Software'))
        self.assertFalse(Draft202012Validator(schema).is_valid(value))
        with self.assertRaises(ValueError):
            validate_output(json.dumps(value), source, [], index)

    def test_colon_subject_list_is_selectable_and_negation_still_needs_semantic_review(self):
        from jsonschema import Draft202012Validator
        source = item('Group Alpha actors used these tools:\nTool Beta\n')
        _, _, schema, index = make_prompt(source, [])
        self.assertTrue(Draft202012Validator(schema).is_valid(self.selection(index, ['u001','u002'])))
        source = item('Group Alpha actors did not use Tool Beta.')
        _, _, schema, index = make_prompt(source, [])
        # The menu enforces source locality/type only. It must never be treated
        # as semantic acceptance or as a generated extraction by itself.
        self.assertTrue(Draft202012Validator(schema).is_valid(self.selection(index)))

    def test_mention_proof_requires_word_boundaries_and_exact_id_namespace(self):
        self.assertFalse(has_mention({'name': 'tool', 'attack_id': None}, 'toolbox'))
        self.assertFalse(has_mention({'name': 'T1090', 'attack_id': 'T1090'}, 'T1090.002'))
        self.assertTrue(has_mention({'name': 'T1090', 'attack_id': 'T1090'}, '[T1090] [T1090.002]'))

    def test_arbitrary_neighbor_units_and_repeated_relations_are_rejected(self):
        source = item('Group Alpha actors used tools.\nTool Beta\n')
        _, _, _, index = make_prompt(source, [])
        with self.assertRaises(ValueError):
            validate_output(json.dumps(self.selection(index, ['u001','u002'])), source, [], index)
        source = item('Group Alpha actors used Tool Beta.')
        _, _, _, index = make_prompt(source, [])
        value = self.selection(index)
        value['relations'].append(dict(value['relations'][0]))
        with self.assertRaises(ValueError):
            validate_output(json.dumps(value), source, [], index)

    def test_nested_colon_list_keeps_three_selected_units_and_exact_technique_id(self):
        from jsonschema import Draft202012Validator
        source = item('Group Alpha actors queried these domains:\nAccount information:\nT1069.002\n')
        catalog = [Entity(canonical_id='attack:T1069.002', type='Technique', name='Domain Groups',
                          aliases=[], attack_id='T1069.002', resolution_status='canonical')]
        _, _, schema, index = make_prompt(source, catalog)
        value = {'relations': [{'unit_ids': ['u001','u002','u003'], 'context_ids': [],
                 'head': selector(index, 'Group Alpha actors', 'ThreatGroup'), 'predicate': 'USES_TECHNIQUE',
                 'tail': selector(index, 'T1069.002', 'Technique')}]}
        self.assertTrue(Draft202012Validator(schema).is_valid(value))
        _, _, aligned = validate_output(json.dumps(value), source, catalog, index)
        self.assertEqual(aligned[0]['selected_unit_ids'], ['u001','u002','u003'])

    def test_numbered_units_preserve_repeated_source_text_and_absolute_offsets(self):
        source = item('Group Alpha actors used Tool Beta.\nGroup Alpha actors used Tool Beta.', prefix='Title\n')
        index = index_source(source, [])
        batch, _, aligned = validate_output(json.dumps(self.selection(index, ['u002'])), source, [], index)
        expected = source['document'].text.rfind('Group Alpha actors')
        self.assertEqual(aligned[0]['document_start'], expected)
        span = batch.relations[0].evidence
        self.assertEqual(source['chunk'].text[span.start:span.end], span.quote)
        self.assertIsNone(batch.relations[0].confidence)

    def test_subject_and_list_units_are_kept_as_literal_contiguous_evidence(self):
        source = item('Group Alpha actors used these tools:\nTool Beta\n')
        index = index_source(source, [])
        batch, _, aligned = validate_output(json.dumps(self.selection(index, ['u001','u002'])), source, [], index)
        self.assertEqual(batch.relations[0].evidence.quote, source['chunk'].text.rstrip())
        self.assertEqual(aligned[0]['selected_unit_ids'], ['u001','u002'])

    def test_names_from_titles_invented_selectors_and_freeform_fields_are_rejected(self):
        source = item('Group Alpha actors used Tool Beta.', prefix='Different Group\n')
        index = index_source(source, [])
        self.assertFalse(any(value['name'] == 'Different Group' for value in index['choices'].values()))
        for change in ['head', 'attack_id', 'quote']:
            value = self.selection(index)
            if change == 'head':
                value['relations'][0]['head'] = 'm999_G'
            else:
                value['relations'][0][change] = 'invented'
            with self.subTest(change=change), self.assertRaises(ValueError):
                validate_output(json.dumps(value), source, [], index)

    def test_unselected_passage_cannot_supply_an_endpoint(self):
        source = item('Group Alpha actors used tools.\nTool Beta\nUnrelated Line\n')
        index = index_source(source, [])
        with self.assertRaises(ValueError):
            validate_output(json.dumps(self.selection(index, ['u001','u003'])), source, [], index)

    def test_caption_scope_is_allowed_but_title_scope_is_not(self):
        prefix = 'Table 1: Tools Used by Group Alpha actors\n'
        source = item('Tool Beta enables remote control.', prefix=prefix)
        source['chunk'].inherited_context = [SourceContext(start=0, end=len(prefix)-1, text=prefix.rstrip())]
        index = index_source(source, [])
        batch, _, aligned = validate_output(json.dumps(self.selection(index, contexts=['ctx1'])), source, [], index)
        self.assertEqual(len(batch.relations), 1)
        self.assertEqual(aligned[0]['context_spans'][0]['text'], prefix.rstrip())
        with self.assertRaises(ValueError):
            validate_output(json.dumps(self.selection(index)), source, [], index)

    def test_id_namespaces_and_qualified_actor_names_are_preserved(self):
        source = item('ALPHV Blackcat affiliates used Ngrok [S0508] under T1219 and TA0001.')
        catalog = [Entity(canonical_id='attack:S0508', type='Software', name='Ngrok', aliases=[],
                          attack_id='S0508', resolution_status='canonical')]
        index = index_source(source, catalog)
        for name, kind in [('S0508','Software'), ('T1219','Technique'), ('TA0001','Tactic')]:
            choices = [value for value in index['choices'].values() if value['name'] == name]
            self.assertEqual({value['type'] for value in choices}, {kind})
            self.assertEqual(choices[0]['attack_id'], name)
        self.assertTrue(any(value['name'] == 'ALPHV Blackcat affiliates' and value['type'] == 'ThreatGroup'
                            for value in index['choices'].values()))
        self.assertFalse(any(value['name'] == 'ALPHV Blackcat' and value['type'] == 'ThreatGroup'
                             for value in index['choices'].values()))

    def test_software_cannot_be_selected_as_technique(self):
        source = item('Group Alpha actors used Tool Beta.')
        index = index_source(source, [])
        value = self.selection(index)
        value['relations'][0]['predicate'] = 'USES_TECHNIQUE'
        with self.assertRaises(ValueError):
            validate_output(json.dumps(value), source, [], index)


if __name__ == '__main__':
    unittest.main()

"""Exact source coverage, tokenizer bounds, overlap and context integrity."""
import re
import unittest

from retrieval.development_text import sha, split_parent
from schemas import Chunk, Document, SourceContext


class WordTokenizer:
    is_fast = True

    def __call__(self, text, **kwargs):
        matches = list(re.finditer(r'\S+', text))
        value = {'input_ids': list(range(len(matches)))}
        if kwargs.get('return_offsets_mapping'):
            value['offset_mapping'] = [m.span() for m in matches]
        return value


class TextChunkTests(unittest.TestCase):
    def fixture(self):
        header = 'Actor heading'
        body = ' '.join('item'+str(i) for i in range(65))+'\n'
        full = header+'\n\n'+body
        doc = Document(doc_id='test', title='Test source', source_url='https://example.org/source',
                       text=full, content_hash=sha(full))
        chunk = Chunk(chunk_id='test:parent', doc_id='test', start=len(header)+2,
                      end=len(full), text=body,
                      inherited_context=[SourceContext(start=0, end=len(header), text=header)])
        return doc, chunk

    def test_long_parent_preserves_coverage_and_context_under_both_limits(self):
        doc, parent = self.fixture()
        settings = {'retrieval_minilm_wordpiece_ceiling': 14,
                    'retrieval_character_ceiling': 95, 'retrieval_overlap_wordpieces': 3}
        records = split_parent(doc, parent, WordTokenizer(), settings)
        self.assertGreater(len(records), 1)
        covered = set()
        for record in records:
            child = record['chunk']
            self.assertEqual(child['text'], doc.text[child['start']:child['end']])
            self.assertEqual(child['parent_extraction_chunk_id'], parent.chunk_id)
            self.assertEqual(child['inherited_context'], [c.model_dump() for c in parent.inherited_context])
            self.assertLessEqual(record['wordpiece_count'], 14)
            self.assertLessEqual(len(record['embedding_text']), 95)
            covered.update(range(child['start'], child['end']))
        self.assertEqual(covered, set(range(parent.start, parent.end)))
        self.assertTrue(all(a['chunk']['start'] < b['chunk']['start'] < a['chunk']['end']
                            for a, b in zip(records, records[1:])))

    def test_parent_or_context_tampering_is_rejected(self):
        for field in ['text', 'inherited_context']:
            doc, parent = self.fixture()
            if field == 'text':
                parent.text = 'x'+parent.text[1:]
            else:
                parent.inherited_context[0].text = 'Wrong heading'
            with self.subTest(field=field), self.assertRaises(ValueError):
                split_parent(doc, parent, WordTokenizer(), {'retrieval_minilm_wordpiece_ceiling': 20,
                    'retrieval_character_ceiling': 100, 'retrieval_overlap_wordpieces': 3})

    def test_context_cannot_consume_entire_chunk_budget(self):
        doc, parent = self.fixture()
        with self.assertRaisesRegex(ValueError, 'no room'):
            split_parent(doc, parent, WordTokenizer(), {'retrieval_minilm_wordpiece_ceiling': 2,
                'retrieval_character_ceiling': 100, 'retrieval_overlap_wordpieces': 1})

    def test_zero_overlap_still_covers_whitespace_between_words(self):
        doc, parent = self.fixture()
        records = split_parent(doc, parent, WordTokenizer(), {'retrieval_minilm_wordpiece_ceiling': 12,
            'retrieval_character_ceiling': 100, 'retrieval_overlap_wordpieces': 0})
        self.assertEqual(''.join(r['chunk']['text'] for r in records), parent.text)

    def test_invalid_overlap_and_non_fast_tokenizer_are_rejected(self):
        doc, parent = self.fixture()
        settings = {'retrieval_minilm_wordpiece_ceiling': 12,
                    'retrieval_character_ceiling': 100, 'retrieval_overlap_wordpieces': 12}
        with self.assertRaises(ValueError):
            split_parent(doc, parent, WordTokenizer(), settings)
        settings['retrieval_overlap_wordpieces'] = 3
        tokenizer = WordTokenizer()
        tokenizer.is_fast = False
        with self.assertRaisesRegex(ValueError, 'fast tokenizer'):
            split_parent(doc, parent, tokenizer, settings)


if __name__ == '__main__':
    unittest.main()

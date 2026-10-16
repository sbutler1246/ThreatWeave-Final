import hashlib
import unittest

from extraction.corpus_chunking import split_section, technical_bounds
from schemas import Document


class CharacterTokenizer:
    def encode(self, text, **kwargs):
        return type('Encoding', (), {'ids': list(map(ord, text)),
                                     'offsets': [(i, i+1) for i in range(len(text))]})()
    def decode(self, ids, **kwargs):
        return ''.join(map(chr, ids))


class CorpusChunkingTests(unittest.TestCase):
    def fixture(self, body):
        text = 'Source title\nTechnical Details\n'+body+'\nMitigations\nSource advice'
        doc = Document(doc_id='sample', title='Source title', source_url='https://example.org/source',
                       text=text, content_hash=hashlib.sha256(text.encode()).hexdigest())
        start, end, heading = technical_bounds(text)
        return doc, start, end, heading

    def chunks(self, body, overlap=6):
        doc, start, end, heading = self.fixture(body)
        records = split_section(doc, CharacterTokenizer(), start, end, heading,
                                target=50, minimum=40, maximum=60, overlap=overlap)
        return doc, start, end, records

    def test_exact_unicode_coverage_and_measured_limits(self):
        doc, start, end, records = self.chunks(('victim’s devices café🙂\n')*15)
        covered = set()
        for item in records:
            chunk = item['chunk']
            self.assertEqual(chunk['text'], doc.text[chunk['start']:chunk['end']])
            self.assertTrue(40 <= item['source_tokens'] <= 60)
            for context in chunk['inherited_context']:
                self.assertEqual(context['text'], doc.text[context['start']:context['end']])
            covered.update(range(chunk['start'], chunk['end']))
        self.assertEqual(covered, set(range(start, end)))
        for first, second in zip(records, records[1:]):
            a, b = first['chunk'], second['chunk']
            self.assertTrue(a['start'] < b['start'] < a['end'])
            self.assertEqual(second['overlap_with_previous_tokens'], a['end']-b['start'])

    def test_zero_overlap_preserves_source_and_final_reanchor_is_explicit(self):
        doc, start, end, records = self.chunks('x'*115, overlap=0)
        covered = set().union(*(set(range(r['chunk']['start'], r['chunk']['end'])) for r in records))
        self.assertEqual(covered, set(range(start, end)))
        self.assertTrue(records[-1]['terminal_reanchored'])
        self.assertTrue(40 <= records[-1]['source_tokens'] <= 60)

    def test_small_whole_section_is_retained_and_labeled(self):
        doc, start, end, records = self.chunks('tiny source')
        self.assertEqual(len(records), 1)
        self.assertTrue(records[0]['short_section'])
        self.assertEqual(records[0]['chunk']['text'], doc.text[start:end])

    def test_missing_duplicate_or_empty_technical_sections_are_rejected(self):
        for source in ['Summary only', 'Technical Details\nMitigations',
                       'Technical Details\nx\nTechnical Details\ny\nMitigations']:
            with self.assertRaises(ValueError):
                technical_bounds(source)

    def test_invalid_overlap_is_rejected(self):
        doc, start, end, heading = self.fixture('x'*150)
        with self.assertRaises(ValueError):
            split_section(doc, CharacterTokenizer(), start, end, heading,
                          target=50, minimum=40, maximum=60, overlap=40)


if __name__ == '__main__':
    unittest.main()

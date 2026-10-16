"""Review-gated import preparation for the three-report development extension."""
from extraction.corpus_extension import OUTPUT_KIND, read_prepared
from graph.corpus_batch_ingestion import prepare as prepare_reviewed

REVIEW_FILE = 'docs/ThreatWeave_corpus_extension_source_review.json'
IMPLEMENTATION_FILES = {'check_corpus_extension.py','extraction/corpus_extension.py','extraction/corpus_pilot.py',
                        'extraction/corpus_batch_review.py','extraction/development_batch.py','extraction/source_choices.py'}


def prepare(repo):
    return prepare_reviewed(repo, review_file=REVIEW_FILE, batch_preparer=read_prepared,
                            review_kind='corpus_extension_review_checks', run_kind=OUTPUT_KIND,
                            implementation_files=IMPLEMENTATION_FILES)

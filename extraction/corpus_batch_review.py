"""Offline revalidation and explicit derived candidates; never edit model output."""
import json

from extraction.source_choices import SourceSelection


def unique_selection(raw, index):
    """Keep the first occurrence of each typed identity link, recording removals."""
    selected = SourceSelection.model_validate_json(raw)
    kept, seen, changes = [], {}, []
    for number, relation in enumerate(selected.relations):
        if relation.head not in index['identities'] or relation.tail not in index['identities']:
            raise ValueError('Unknown source selector in saved output.')
        key = (index['identities'][relation.head], relation.predicate.value, index['identities'][relation.tail])
        if key in seen:
            changes.append({'action': 'remove_duplicate_relationship', 'original_relation_index': number,
                            'retained_original_relation_index': seen[key],
                            'removed_selection': relation.model_dump(mode='json'),
                            'reason': 'Same typed endpoint identities and predicate; first support retained. '
                                      'Original alternative evidence remains in the unmodified model response.'})
        else:
            seen[key] = number
            kept.append(relation.model_dump(mode='json'))
    return json.dumps({'relations': kept}, ensure_ascii=False), changes

"""Exact ID/name/verified-alias lookup; no automatic fuzzy merges."""
import unicodedata
from schemas import Entity, EntityCandidate, ResolutionResult

def norm(s): return ' '.join(unicodedata.normalize('NFKC',s).casefold().split())

def resolve(candidate: EntityCandidate, reference: list[Entity]) -> ResolutionResult:
    pool=[x for x in reference if x.type==candidate.type]
    names=[x for x in pool if norm(candidate.name) in {norm(x.name),*(norm(a) for a in x.aliases)}]
    if candidate.attack_id:
        matches=[x for x in pool if x.attack_id==candidate.attack_id]
        if len(matches)!=1: return ResolutionResult(entity=None,status='unresolved',reason='unknown or ambiguous ID')
        obj=matches[0]
        if names and any(x.canonical_id!=obj.canonical_id for x in names):
            return ResolutionResult(entity=None,status='conflict',reason='ID and name disagree')
        return ResolutionResult(entity=obj,status='resolved',reason='type-compatible ID; reported spelling is not added as a verified alias')
    aliases=[x for x in pool if norm(candidate.name) in {norm(a) for a in x.aliases}]
    canonical=[x for x in pool if norm(x.name)==norm(candidate.name)]
    matches=aliases or canonical
    if len(matches)==1: return ResolutionResult(entity=matches[0],status='resolved',reason='unique exact name or verified alias')
    return ResolutionResult(entity=None,status='unresolved',reason='unknown or ambiguous name')

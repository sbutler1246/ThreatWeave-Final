"""ThreatWeave Pydantic v2 contracts. All spans are half-open character offsets."""
from datetime import datetime, timezone
from enum import Enum
from typing import Literal
from pydantic import BaseModel, ConfigDict, Field, HttpUrl, model_validator

class StrictModel(BaseModel):
    model_config = ConfigDict(extra='forbid', str_strip_whitespace=False)

class EntityType(str, Enum):
    GROUP='ThreatGroup'
    SOFTWARE='Software'
    TECHNIQUE='Technique'
    TACTIC='Tactic'
    MITIGATION='Mitigation'
    CAMPAIGN='Campaign'

class Predicate(str, Enum):
    USES='USES'
    TECHNIQUE='USES_TECHNIQUE'
    TACTIC='PART_OF_TACTIC'
    MITIGATED_BY='MITIGATED_BY'
    CAMPAIGN='ASSOCIATED_WITH'

ALLOWED = {
    ('ThreatGroup','USES','Software'),
    ('ThreatGroup','USES_TECHNIQUE','Technique'),
    ('Software','USES_TECHNIQUE','Technique'),
    ('Technique','PART_OF_TACTIC','Tactic'),
    ('Technique','MITIGATED_BY','Mitigation'),
    ('ThreatGroup','ASSOCIATED_WITH','Campaign'),
}

class Document(StrictModel):
    doc_id: str = Field(min_length=1)
    title: str = Field(min_length=1)
    source_url: HttpUrl
    publication_date: str | None = None
    source: Literal['cisa','attack']='cisa'
    text: str = Field(min_length=1)
    content_hash: str = Field(pattern=r'^[a-f0-9]{64}$')

class SourceContext(StrictModel):
    """Inherited heading/caption with offsets into the same normalized document."""
    start: int=Field(ge=0)
    end: int=Field(gt=0)
    text: str=Field(min_length=1)
    @model_validator(mode='after')
    def span(self):
        if self.end-self.start!=len(self.text):raise ValueError('context span mismatch')
        return self

class Chunk(StrictModel):
    chunk_id: str = Field(min_length=1)
    doc_id: str = Field(min_length=1)
    start: int = Field(ge=0)
    end: int = Field(gt=0)
    text: str = Field(min_length=1)
    inherited_context: list[SourceContext]=Field(default_factory=list)
    role: Literal['extraction','retrieval']='extraction'
    parent_extraction_chunk_id: str | None=None
    embedding: list[float] | None = Field(default=None, min_length=384, max_length=384)
    @model_validator(mode='after')
    def span(self):
        if self.end-self.start != len(self.text):
            raise ValueError('chunk length must equal end-start')
        return self

class EntityCandidate(StrictModel):
    local_id: str = Field(min_length=1)
    type: EntityType
    name: str = Field(min_length=1)
    attack_id: str | None = None

class EvidenceSpan(StrictModel):
    start: int = Field(ge=0)
    end: int = Field(gt=0)
    quote: str = Field(min_length=1)
    @model_validator(mode='after')
    def span(self):
        if self.end-self.start != len(self.quote):
            raise ValueError('evidence span length mismatch')
        return self

class RelationCandidate(StrictModel):
    head: str
    predicate: Predicate
    tail: str
    evidence: EvidenceSpan
    confidence: float | None = Field(default=None,ge=0,le=1)

class ExtractionBatch(StrictModel):
    entities: list[EntityCandidate]
    relations: list[RelationCandidate]
    @model_validator(mode='after')
    def endpoints(self):
        by_id={x.local_id:x for x in self.entities}
        if len(by_id)!=len(self.entities): raise ValueError('duplicate local ID')
        for r in self.relations:
            if r.head not in by_id or r.tail not in by_id:
                raise ValueError('dangling relation endpoint')
            signature=(by_id[r.head].type.value,r.predicate.value,by_id[r.tail].type.value)
            if signature not in ALLOWED: raise ValueError('forbidden endpoint/predicate combination')
        return self

class Entity(StrictModel):
    canonical_id: str
    type: EntityType
    name: str
    aliases: list[str]=Field(default_factory=list)
    attack_id: str | None=None
    description: str | None=None
    stix_id: str | None=None
    attack_release: str | None=None
    resolution_status: Literal['canonical','local','review']
    graph_embedding: list[float] | None=Field(default=None,min_length=128,max_length=128)

class ResolutionResult(StrictModel):
    entity: Entity | None
    status: Literal['resolved','unresolved','conflict']
    reason: str

class RetrievalMode(str,Enum):
    TEXT='text_only'
    GRAPH='graph_only'
    HYBRID='hybrid'
    ABLATION='hybrid_no_node2vec'

class QueryRequest(StrictModel):
    question: str=Field(min_length=3,max_length=2000)
    mode: RetrievalMode
    corpus_version: str=Field(min_length=1)

class Passage(StrictModel):
    citation_id: str
    doc_id: str
    chunk_id: str
    source_url: HttpUrl
    text: str
    start: int=Field(ge=0)
    end: int=Field(gt=0)
    source_kind: Literal['cisa','attack']

class RelationshipEdge(StrictModel):
    head_id: str
    predicate: Predicate
    tail_id: str
    assertion_ids: list[str]=Field(min_length=1)
    citation_ids: list[str]=Field(min_length=1)

class Assertion(StrictModel):
    """Evidence-bearing properties attached to a factual graph edge."""
    assertion_id: str
    head_id: str
    predicate: Predicate
    tail_id: str
    source_doc_id: str
    chunk_id: str
    evidence_text: str=Field(min_length=1)
    origin: Literal['extracted','fused']
    validation_status: Literal['pending_review','validated','human_verified','rejected']
    confidence: float | None=Field(default=None,ge=0,le=1)

class SourceClaimLink(StrictModel):
    entity_canonical_id: str
    document_id: str
    predicate: Literal['MENTIONED_IN','SUPPORTED_BY']
    claim_key: str | None=None
    evidence_text: str
    @model_validator(mode='after')
    def attribute_claim(self):
        if self.predicate=='SUPPORTED_BY' and not self.claim_key:
            raise ValueError('SUPPORTED_BY must identify a specific attribute claim')
        return self

class GraphPath(StrictModel):
    path_id: str
    edges: list[RelationshipEdge]=Field(min_length=1,max_length=3)
    @model_validator(mode='after')
    def continuity(self):
        if any(a.tail_id!=b.head_id for a,b in zip(self.edges,self.edges[1:])):
            raise ValueError('graph path edges must form a continuous directed chain')
        return self

class EvidenceBundle(StrictModel):
    passages: list[Passage]=Field(default_factory=list)
    paths: list[GraphPath]=Field(default_factory=list)
    citation_ids: list[str]=Field(default_factory=list)
    retrieval_ms: float=Field(ge=0)
    configuration_hash: str
    corpus_version: str
    @model_validator(mode='after')
    def citations(self):
        ids=[p.citation_id for p in self.passages]
        if len(set(ids))!=len(ids) or set(ids)!=set(self.citation_ids):
            raise ValueError('citation map mismatch')
        for path in self.paths:
            for edge in path.edges:
                if not set(edge.citation_ids)<=set(ids): raise ValueError('unknown path citation')
        return self

class Claim(StrictModel):
    text: str=Field(min_length=1)
    citations: list[str]=Field(min_length=1)

class AnswerResponse(StrictModel):
    answer: str
    claims: list[Claim]
    evidence: EvidenceBundle
    abstained: bool
    execution_time_ms: float=Field(ge=0)
    generation_timestamp: datetime=Field(default_factory=lambda:datetime.now(timezone.utc))
    warnings: list[str]=Field(default_factory=list)
    @model_validator(mode='after')
    def grounded_ids(self):
        for claim in self.claims:
            if not set(claim.citations)<=set(self.evidence.citation_ids):
                raise ValueError('unknown answer citation')
        if not self.abstained and not self.claims:
            raise ValueError('non-abstaining answer requires claims')
        return self

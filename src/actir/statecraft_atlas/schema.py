"""Version 0.1.0 types for the Statecraft Atlas.

The module represents the A.0 contract without deciding whether a populated
record is admissible. Cross-record and semantic validation belongs to Stage
A.2. All records are immutable so later transformations must create auditable
revisions instead of silently changing evidence.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import StrEnum
SCHEMA_VERSION = "0.1.0"


class SourceType(StrEnum):
    OFFICIAL_STATEMENT = "official_statement"
    STRATEGY_DOCUMENT = "strategy_document"
    TREATY = "treaty"
    LEGISLATION = "legislation"
    ACADEMIC_ANALYSIS = "academic_analysis"
    NEWS_REPORT = "news_report"
    DATASET = "dataset"
    ARCHIVAL_RECORD = "archival_record"
    OTHER = "other"


class EpistemicStatus(StrEnum):
    OBSERVED = "observed"
    ALLEGED = "alleged"
    INFERRED = "inferred"
    RECOMMENDED = "recommended"
    PREDICTED = "predicted"
    HYPOTHETICAL = "hypothetical"
    COUNTERFACTUAL = "counterfactual"


class DiscourseFunction(StrEnum):
    STATEMENT = "statement"
    PROMISE = "promise"
    THREAT = "threat"
    DEMAND = "demand"
    JUSTIFICATION = "justification"
    REASSURANCE = "reassurance"
    COMMITMENT = "commitment"
    DENIAL = "denial"
    AMBIGUITY = "ambiguity"
    OTHER = "other"


class ActionKind(StrEnum):
    ACTION = "action"
    RESTRAINT = "restraint"
    NONUSE = "nonuse"
    DELAY = "delay"
    WAITING = "waiting"
    AMBIGUITY = "ambiguity"
    CONCEALMENT = "concealment"
    DELEGATION = "delegation"
    REASSURANCE = "reassurance"
    ACCOMMODATION = "accommodation"
    DIVERSIFICATION = "diversification"
    INSTITUTION_BUILDING = "institution_building"
    DOMESTIC_MOBILIZATION = "domestic_mobilization"
    CAPABILITY_CONSTRUCTION = "capability_construction"
    RECOGNITION = "recognition"
    LEGITIMATION = "legitimation"
    INACTION = "inaction"


class VerificationDisposition(StrEnum):
    SUPPORTS = "supports"
    CONTRADICTS = "contradicts"
    MIXED = "mixed"
    UNRESOLVED = "unresolved"
    ABSTAIN = "abstain"


class SequenceRelation(StrEnum):
    PRECEDES = "precedes"
    RESPONDS_TO = "responds_to"
    ADAPTS_TO = "adapts_to"
    CONTRIBUTES_TO = "contributes_to"
    CONTRADICTS = "contradicts"
    REVISES = "revises"


class HumanDisposition(StrEnum):
    UNREVIEWED = "unreviewed"
    ADOPT = "adopt"
    REJECT = "reject"
    REVISE = "revise"
    DEFER = "defer"
    REQUEST_ALTERNATIVES = "request_alternatives"


@dataclass(frozen=True, slots=True)
class VersionedRecord:
    """Base for independently stored Atlas entities."""

    schema_version: str = field(init=False, default=SCHEMA_VERSION)


@dataclass(frozen=True, slots=True)
class Source(VersionedRecord):
    source_id: str
    title: str
    source_type: SourceType
    publication_date: str | None
    author_or_speaker: tuple[str, ...]
    publisher: str | None
    stable_identifier: str
    language: str
    corpus_layer: str | None = None


@dataclass(frozen=True, slots=True)
class EvidenceSpan(VersionedRecord):
    span_id: str
    source_id: str
    exact_text: str
    locator: str
    start_offset: int | None = None
    end_offset: int | None = None


@dataclass(frozen=True, slots=True)
class DiscourseAct(VersionedRecord):
    discourse_id: str
    actor: str
    function: DiscourseFunction
    content: str
    epistemic_status: EpistemicStatus
    evidence_span_ids: tuple[str, ...]
    date: str | None = None
    addressees: tuple[str, ...] = ()
    ambiguity_note: str | None = None


@dataclass(frozen=True, slots=True)
class ReportedAction:
    """A source's behavior report, not an independently verified event."""

    actor: str
    kind: ActionKind
    description: str
    epistemic_status: EpistemicStatus
    targets: tuple[str, ...] = ()
    instrument: str | None = None
    domain: str | None = None
    intensity: str | None = None
    duration: str | None = None
    cost: str | None = None
    reversibility: str | None = None


@dataclass(frozen=True, slots=True)
class SourceExplanation:
    """A mechanism asserted by a source, not an ACTIR causal conclusion."""

    expected_mechanism: str
    assumptions: tuple[str, ...]
    scope_conditions: tuple[str, ...]
    stated_confidence: str | None = None


@dataclass(frozen=True, slots=True)
class OutcomeClaim:
    """A reported consequence awaiting a separate verification decision."""

    description: str
    epistemic_status: EpistemicStatus
    intended: bool | None = None
    date: str | None = None


@dataclass(frozen=True, slots=True)
class ActionMechanismClaim(VersionedRecord):
    claim_id: str
    observation: str
    reported_action: ReportedAction
    context: str
    source_explanation: SourceExplanation
    evidence_span_ids: tuple[str, ...]
    counterpart_responses: tuple[str, ...] = ()
    adaptations: tuple[str, ...] = ()
    outcome_claims: tuple[OutcomeClaim, ...] = ()
    discourse_act_ids: tuple[str, ...] = ()
    capability_and_role_claims: tuple[str, ...] = ()


@dataclass(frozen=True, slots=True)
class VerificationDecision(VersionedRecord):
    verification_id: str
    subject_record_id: str
    disposition: VerificationDisposition
    rationale: str
    verifier: str
    decided_at: str
    evidence_span_ids: tuple[str, ...]
    abstention_reason: str | None = None
    human_adjudication: str | None = None


@dataclass(frozen=True, slots=True)
class SequenceLink(VersionedRecord):
    link_id: str
    from_record_id: str
    to_record_id: str
    relation: SequenceRelation
    evidence_span_ids: tuple[str, ...] = ()
    note: str | None = None


@dataclass(frozen=True, slots=True)
class PolicyCondition:
    condition_id: str
    description: str
    evidence_record_ids: tuple[str, ...] = ()


@dataclass(frozen=True, slots=True)
class PolicyStep:
    step_id: str
    condition_ids: tuple[str, ...]
    action: str
    expected_mechanism: str
    fallback_step_ids: tuple[str, ...] = ()
    stopping_conditions: tuple[str, ...] = ()
    resource_commitments: tuple[str, ...] = ()
    reversibility: str | None = None
    provenance_record_ids: tuple[str, ...] = ()


@dataclass(frozen=True, slots=True)
class PolicyProgram(VersionedRecord):
    program_id: str
    name: str
    decision_context_id: str
    conditions: tuple[PolicyCondition, ...]
    steps: tuple[PolicyStep, ...]
    uncertainties: tuple[str, ...]
    provenance_record_ids: tuple[str, ...]


@dataclass(frozen=True, slots=True)
class OutcomeVector:
    security: float | None
    prosperity: float | None
    strategic_autonomy: float | None
    regional_order: float | None
    cost: float | None
    reversibility: float | None


@dataclass(frozen=True, slots=True)
class ProgramAssessment:
    program_id: str
    outcomes: OutcomeVector
    hard_constraint_violations: tuple[str, ...] = ()
    failure_reasons: tuple[str, ...] = ()
    behavioral_descriptors: tuple[str, ...] = ()


@dataclass(frozen=True, slots=True)
class AuditEvent:
    event_id: str
    transformation: str
    method: str
    input_record_ids: tuple[str, ...]
    output_record_ids: tuple[str, ...]
    occurred_at: str


@dataclass(frozen=True, slots=True)
class DecisionDossier(VersionedRecord):
    dossier_id: str
    question: str
    as_of_date: str
    focal_actor: str
    current_evidence_ids: tuple[str, ...]
    constraints: tuple[str, ...]
    objectives: tuple[str, ...]
    preferences: tuple[str, ...]
    uncertainties: tuple[str, ...]
    horizons: tuple[str, ...]
    resource_envelope: tuple[str, ...]
    authorization_policy: str
    retrieved_record_ids: tuple[str, ...]
    policy_program_ids: tuple[str, ...]
    assessments: tuple[ProgramAssessment, ...]
    competing_interpretations: tuple[str, ...]
    evidence_requests: tuple[str, ...]
    abstention_reason: str | None
    audit_events: tuple[AuditEvent, ...]
    human_disposition: HumanDisposition = HumanDisposition.UNREVIEWED


ATLAS_ENTITY_TYPES: tuple[type[VersionedRecord], ...] = (
    Source,
    EvidenceSpan,
    DiscourseAct,
    ActionMechanismClaim,
    VerificationDecision,
    SequenceLink,
    PolicyProgram,
    DecisionDossier,
)

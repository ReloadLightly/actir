"""Deterministic semantic validation for Statecraft Atlas records.

Validation reports defects without rewriting records. It is deliberately
limited to the A.0 invariants: provenance, epistemic state, temporal sequence,
and transformation authorization. Corpus ingestion and extraction are later
stages.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from enum import StrEnum
from typing import Iterable

from actir.statecraft_atlas.schema import (
    ActionMechanismClaim,
    AuditEvent,
    DiscourseAct,
    EpistemicStatus,
    EvidenceSpan,
    SequenceLink,
    SequenceRelation,
    Source,
    VerificationDecision,
    VerificationDisposition,
)


class ValidationCode(StrEnum):
    MISSING_PROVENANCE = "missing_provenance"
    UNKNOWN_REFERENCE = "unknown_reference"
    INVALID_EPISTEMIC_STATE = "invalid_epistemic_state"
    TEMPORAL_ORDER = "temporal_order"
    UNAUTHORIZED_TRANSFORMATION = "unauthorized_transformation"
    INVALID_ABSTENTION = "invalid_abstention"


@dataclass(frozen=True, slots=True)
class ValidationIssue:
    code: ValidationCode
    record_id: str
    message: str


@dataclass(frozen=True, slots=True)
class ValidationReport:
    issues: tuple[ValidationIssue, ...]

    @property
    def is_valid(self) -> bool:
        return not self.issues


def _issue(code: ValidationCode, record_id: str, message: str) -> ValidationIssue:
    return ValidationIssue(code=code, record_id=record_id, message=message)


def _parse_iso_date(value: str | None) -> date | None:
    if value is None:
        return None
    try:
        return date.fromisoformat(value)
    except ValueError:
        return None


def validate_atlas(
    *,
    sources: Iterable[Source] = (),
    evidence_spans: Iterable[EvidenceSpan] = (),
    discourse_acts: Iterable[DiscourseAct] = (),
    claims: Iterable[ActionMechanismClaim] = (),
    verifications: Iterable[VerificationDecision] = (),
    sequence_links: Iterable[SequenceLink] = (),
    audit_events: Iterable[AuditEvent] = (),
    record_dates: dict[str, str | None] | None = None,
    authorized_methods: frozenset[str] = frozenset({"human_entry"}),
) -> ValidationReport:
    """Return all A.2 invariant violations without mutating any record.

    ``record_dates`` is an explicit external index because the initial schema
    allows several records to be undated. Temporal validation abstains when
    either endpoint has no valid ISO date.
    """

    source_items = tuple(sources)
    span_items = tuple(evidence_spans)
    discourse_items = tuple(discourse_acts)
    claim_items = tuple(claims)
    verification_items = tuple(verifications)
    link_items = tuple(sequence_links)
    audit_items = tuple(audit_events)
    issues: list[ValidationIssue] = []

    source_ids = {source.source_id for source in source_items}
    span_ids = {span.span_id for span in span_items}
    record_ids = {
        *(act.discourse_id for act in discourse_items),
        *(claim.claim_id for claim in claim_items),
    }

    for source in source_items:
        if not all((source.title.strip(), source.stable_identifier.strip(), source.language.strip())):
            issues.append(_issue(
                ValidationCode.MISSING_PROVENANCE,
                source.source_id,
                "A source requires title, stable identifier, and language.",
            ))

    for span in span_items:
        if span.source_id not in source_ids:
            issues.append(_issue(
                ValidationCode.UNKNOWN_REFERENCE,
                span.span_id,
                "Evidence span refers to an unknown source.",
            ))
        if not span.exact_text.strip() or not span.locator.strip():
            issues.append(_issue(
                ValidationCode.MISSING_PROVENANCE,
                span.span_id,
                "Evidence span requires exact text and a locator.",
            ))
        if ((span.start_offset is None) != (span.end_offset is None)
                or (span.start_offset is not None and span.start_offset > span.end_offset)):
            issues.append(_issue(
                ValidationCode.MISSING_PROVENANCE,
                span.span_id,
                "Evidence offsets must be absent together or have nondecreasing order.",
            ))

    for discourse in discourse_items:
        if not isinstance(discourse.epistemic_status, EpistemicStatus):
            issues.append(_issue(
                ValidationCode.INVALID_EPISTEMIC_STATE,
                discourse.discourse_id,
                "Discourse requires an EpistemicStatus enum value.",
            ))
        issues.extend(_validate_span_references(discourse.discourse_id, discourse.evidence_span_ids, span_ids))

    for claim in claim_items:
        if not isinstance(claim.reported_action.epistemic_status, EpistemicStatus):
            issues.append(_issue(
                ValidationCode.INVALID_EPISTEMIC_STATE,
                claim.claim_id,
                "Reported action requires an EpistemicStatus enum value.",
            ))
        for outcome in claim.outcome_claims:
            if not isinstance(outcome.epistemic_status, EpistemicStatus):
                issues.append(_issue(
                    ValidationCode.INVALID_EPISTEMIC_STATE,
                    claim.claim_id,
                    "Outcome claim requires an EpistemicStatus enum value.",
                ))
        issues.extend(_validate_span_references(claim.claim_id, claim.evidence_span_ids, span_ids))

    for verification in verification_items:
        if verification.subject_record_id not in record_ids:
            issues.append(_issue(
                ValidationCode.UNKNOWN_REFERENCE,
                verification.verification_id,
                "Verification refers to an unknown discourse act or claim.",
            ))
        if not isinstance(verification.disposition, VerificationDisposition):
            issues.append(_issue(
                ValidationCode.INVALID_EPISTEMIC_STATE,
                verification.verification_id,
                "Verification requires a VerificationDisposition enum value.",
            ))
        issues.extend(_validate_span_references(
            verification.verification_id, verification.evidence_span_ids, span_ids
        ))
        if verification.disposition == VerificationDisposition.ABSTAIN and not (
            verification.abstention_reason and verification.abstention_reason.strip()
        ):
            issues.append(_issue(
                ValidationCode.INVALID_ABSTENTION,
                verification.verification_id,
                "An abstaining verifier must state why evidence is insufficient.",
            ))

    date_index = record_dates or {}
    for link in link_items:
        if link.from_record_id not in record_ids or link.to_record_id not in record_ids:
            issues.append(_issue(
                ValidationCode.UNKNOWN_REFERENCE,
                link.link_id,
                "Sequence link refers to an unknown discourse act or claim.",
            ))
            continue
        from_date = _parse_iso_date(date_index.get(link.from_record_id))
        to_date = _parse_iso_date(date_index.get(link.to_record_id))
        if from_date is None or to_date is None:
            continue

        # A link always reads: from_record_id RELATION to_record_id.
        # A predecessor must be earlier; a response or adaptation must be later.
        invalid_order = (
            link.relation == SequenceRelation.PRECEDES and from_date > to_date
        ) or (
            link.relation in {
                SequenceRelation.RESPONDS_TO,
                SequenceRelation.ADAPTS_TO,
            }
            and from_date < to_date
        )
        if invalid_order:
            issues.append(_issue(
                ValidationCode.TEMPORAL_ORDER,
                link.link_id,
                (
                    "Temporal order contradicts the convention "
                    "'from_record_id RELATION to_record_id'."
                ),
            ))

    for event in audit_items:
        if event.method not in authorized_methods:
            issues.append(_issue(
                ValidationCode.UNAUTHORIZED_TRANSFORMATION,
                event.event_id,
                "Audit event uses a method outside the frozen authorization policy.",
            ))
        if not event.input_record_ids or not event.output_record_ids:
            issues.append(_issue(
                ValidationCode.UNAUTHORIZED_TRANSFORMATION,
                event.event_id,
                "Every transformation must name both inputs and outputs.",
            ))

    return ValidationReport(issues=tuple(issues))


def _validate_span_references(
    record_id: str, referenced_span_ids: tuple[str, ...], known_span_ids: set[str]
) -> list[ValidationIssue]:
    if not referenced_span_ids:
        return [_issue(
            ValidationCode.MISSING_PROVENANCE,
            record_id,
            "Record requires at least one evidence span.",
        )]
    return [
        _issue(
            ValidationCode.UNKNOWN_REFERENCE,
            record_id,
            f"Record refers to unknown evidence span '{span_id}'.",
        )
        for span_id in referenced_span_ids
        if span_id not in known_span_ids
    ]

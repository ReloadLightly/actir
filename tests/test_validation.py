import unittest

from actir.statecraft_atlas.schema import (
    ActionKind,
    ActionMechanismClaim,
    AuditEvent,
    DiscourseFunction,
    DiscourseAct,
    EpistemicStatus,
    EvidenceSpan,
    ReportedAction,
    SequenceLink,
    SequenceRelation,
    Source,
    SourceExplanation,
    SourceType,
    VerificationDecision,
    VerificationDisposition,
)
from actir.statecraft_atlas.validation import ValidationCode, validate_atlas


SOURCE = Source(
    source_id="source-1",
    title="Permission-safe fixture",
    source_type=SourceType.OTHER,
    publication_date="2022-01-01",
    author_or_speaker=("Fixture author",),
    publisher="ACTIR",
    stable_identifier="fixture:source-1",
    language="en",
)
SPAN = EvidenceSpan(
    span_id="span-1",
    source_id="source-1",
    exact_text="The actor announced a limited measure.",
    locator="paragraph 1",
)
DISCOURSE = DiscourseAct(
    discourse_id="discourse-1",
    actor="Japan",
    function=DiscourseFunction.STATEMENT,
    content="announced a limited measure",
    epistemic_status=EpistemicStatus.OBSERVED,
    evidence_span_ids=("span-1",),
)
CLAIM = ActionMechanismClaim(
    claim_id="claim-1",
    observation="regional uncertainty",
    reported_action=ReportedAction(
        actor="Japan",
        kind=ActionKind.RESTRAINT,
        description="delayed a response",
        epistemic_status=EpistemicStatus.ALLEGED,
    ),
    context="synthetic fixture",
    source_explanation=SourceExplanation(
        expected_mechanism="delay leaves room for information",
        assumptions=("signals remain observable",),
        scope_conditions=("short horizon",),
    ),
    evidence_span_ids=("span-1",),
)


class ValidationTests(unittest.TestCase):
    def test_complete_small_atlas_is_valid(self) -> None:
        report = validate_atlas(
            sources=(SOURCE,),
            evidence_spans=(SPAN,),
            discourse_acts=(DISCOURSE,),
            claims=(CLAIM,),
            audit_events=(AuditEvent(
                event_id="audit-1",
                transformation="human transcription",
                method="human_entry",
                input_record_ids=("span-1",),
                output_record_ids=("claim-1",),
                occurred_at="2026-08-13",
            ),),
        )
        self.assertTrue(report.is_valid)

    def test_rejects_missing_exact_provenance(self) -> None:
        report = validate_atlas(
            sources=(SOURCE,),
            evidence_spans=(EvidenceSpan("span-1", "source-1", "", ""),),
        )
        self.assertIn(ValidationCode.MISSING_PROVENANCE, {x.code for x in report.issues})

    def test_rejects_invalid_epistemic_state(self) -> None:
        malformed = DiscourseAct(
            discourse_id="discourse-bad",
            actor="Japan",
            function=DiscourseFunction.STATEMENT,
            content="a statement",
            epistemic_status="fact",  # type: ignore[arg-type]
            evidence_span_ids=("span-1",),
        )
        report = validate_atlas(
            sources=(SOURCE,), evidence_spans=(SPAN,), discourse_acts=(malformed,)
        )
        self.assertIn(ValidationCode.INVALID_EPISTEMIC_STATE, {x.code for x in report.issues})

    def _report_for_link(
        self,
        relation: SequenceRelation,
        from_date: str,
        to_date: str,
    ):
        """Validate one dated link using the from RELATION to convention."""

        report = validate_atlas(
            sources=(SOURCE,),
            evidence_spans=(SPAN,),
            discourse_acts=(DISCOURSE,),
            claims=(CLAIM,),
            sequence_links=(SequenceLink(
                link_id="link-1",
                from_record_id="claim-1",
                to_record_id="discourse-1",
                relation=relation,
            ),),
            record_dates={"claim-1": from_date, "discourse-1": to_date},
        )
        return report

    def test_precedes_requires_from_record_not_to_be_later(self) -> None:
        report = self._report_for_link(
            SequenceRelation.PRECEDES,
            from_date="2023-01-01",
            to_date="2022-01-01",
        )
        self.assertIn(ValidationCode.TEMPORAL_ORDER, {x.code for x in report.issues})

    def test_responds_to_requires_from_record_not_to_be_earlier(self) -> None:
        report = self._report_for_link(
            SequenceRelation.RESPONDS_TO,
            from_date="2021-01-01",
            to_date="2022-01-01",
        )
        self.assertIn(ValidationCode.TEMPORAL_ORDER, {x.code for x in report.issues})

    def test_adapts_to_requires_from_record_not_to_be_earlier(self) -> None:
        report = self._report_for_link(
            SequenceRelation.ADAPTS_TO,
            from_date="2021-01-01",
            to_date="2022-01-01",
        )
        self.assertIn(ValidationCode.TEMPORAL_ORDER, {x.code for x in report.issues})

    def test_directional_relations_accept_coherent_order(self) -> None:
        cases = (
            (SequenceRelation.PRECEDES, "2022-01-01", "2023-01-01"),
            (SequenceRelation.RESPONDS_TO, "2023-01-01", "2022-01-01"),
            (SequenceRelation.ADAPTS_TO, "2023-01-01", "2022-01-01"),
        )
        for relation, from_date, to_date in cases:
            with self.subTest(relation=relation):
                report = self._report_for_link(relation, from_date, to_date)
                self.assertNotIn(
                    ValidationCode.TEMPORAL_ORDER,
                    {x.code for x in report.issues},
                )

    def test_rejects_unauthorized_or_untraceable_transformation(self) -> None:
        report = validate_atlas(audit_events=(AuditEvent(
            event_id="audit-bad",
            transformation="opaque rewrite",
            method="unknown_model",
            input_record_ids=(),
            output_record_ids=(),
            occurred_at="2026-08-13",
        ),))
        codes = {x.code for x in report.issues}
        self.assertIn(ValidationCode.UNAUTHORIZED_TRANSFORMATION, codes)

    def test_abstention_requires_a_reason(self) -> None:
        report = validate_atlas(
            sources=(SOURCE,),
            evidence_spans=(SPAN,),
            claims=(CLAIM,),
            verifications=(VerificationDecision(
                verification_id="verification-1",
                subject_record_id="claim-1",
                disposition=VerificationDisposition.ABSTAIN,
                rationale="insufficient outcome evidence",
                verifier="human reviewer",
                decided_at="2026-08-13",
                evidence_span_ids=("span-1",),
            ),),
        )
        self.assertIn(ValidationCode.INVALID_ABSTENTION, {x.code for x in report.issues})

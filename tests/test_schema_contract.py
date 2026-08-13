from dataclasses import FrozenInstanceError, fields
import unittest

from actir.statecraft_atlas.schema import (
    ATLAS_ENTITY_TYPES,
    SCHEMA_VERSION,
    ActionMechanismClaim,
    DecisionDossier,
    DiscourseAct,
    EvidenceSpan,
    OutcomeClaim,
    ReportedAction,
    Source,
    SourceType,
    SourceExplanation,
    VerificationDecision,
)


class SchemaContractTests(unittest.TestCase):
    def test_stage_a1_defines_the_eight_versioned_entities(self) -> None:
        self.assertEqual(
            {entity.__name__ for entity in ATLAS_ENTITY_TYPES},
            {
                "Source",
                "EvidenceSpan",
                "DiscourseAct",
                "ActionMechanismClaim",
                "VerificationDecision",
                "SequenceLink",
                "PolicyProgram",
                "DecisionDossier",
            },
        )
        for entity in ATLAS_ENTITY_TYPES:
            self.assertIn("schema_version", {item.name for item in fields(entity)})
            self.assertTrue(entity.__dataclass_params__.frozen)

    def test_schema_version_is_explicit_and_records_are_immutable(self) -> None:
        source = Source(
            source_id="source-1",
            title="Synthetic source",
            source_type=SourceType.OTHER,
            publication_date=None,
            author_or_speaker=(),
            publisher=None,
            stable_identifier="fixture:source-1",
            language="en",
        )
        self.assertEqual(source.schema_version, SCHEMA_VERSION)
        with self.assertRaises(FrozenInstanceError):
            source.title = "silently revised"  # type: ignore[misc]

    def test_epistemic_layers_have_separate_types(self) -> None:
        claim_fields = {item.name: item.type for item in fields(ActionMechanismClaim)}
        self.assertIn("reported_action", claim_fields)
        self.assertIn("source_explanation", claim_fields)
        self.assertIn("outcome_claims", claim_fields)
        self.assertIsNot(ReportedAction, SourceExplanation)
        self.assertIsNot(SourceExplanation, OutcomeClaim)
        self.assertNotIn(DiscourseAct, (ReportedAction, SourceExplanation, OutcomeClaim))
        self.assertNotIn(VerificationDecision, (ReportedAction, OutcomeClaim))

    def test_exact_provenance_slots_exist_before_validation(self) -> None:
        self.assertTrue(
            {"source_id", "exact_text", "locator"}.issubset(
                {item.name for item in fields(EvidenceSpan)}
            )
        )
        self.assertIn(
            "evidence_span_ids",
            {item.name for item in fields(ActionMechanismClaim)},
        )

    def test_dossier_keeps_decision_dimensions_separate(self) -> None:
        names = {item.name for item in fields(DecisionDossier)}
        self.assertTrue(
            {
                "constraints",
                "objectives",
                "preferences",
                "uncertainties",
                "assessments",
                "abstention_reason",
                "human_disposition",
            }.issubset(names)
        )


if __name__ == "__main__":
    unittest.main()

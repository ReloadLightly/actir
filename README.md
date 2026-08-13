# ACTIR Statecraft Atlas

ACTIR—the Adaptive Computational Theory of International Relations—is the
framework. The Statecraft Atlas is its versioned dataset and evidence layer. It
reconstructs what states say, what they are reported to do, why sources expect
those actions to work, how other actors respond, and what outcomes can be
independently checked. ACTIR uses those records to construct provenance-rich
policy programs that can be retrieved, challenged, recombined, simulated, and
improved.

Japan's search for a novel foreign policy after 2022 is the first decision
context. ACTIR does not predict an optimal Japanese policy or automate a
sovereign decision. It produces an auditable portfolio of conditional options
for human deliberation under uncertainty.

## The sole IR baseline

ACTIR begins from the five assumptions that define John J. Mearsheimer's
offensive realism in *The Tragedy of Great Power Politics* (2001):

1. the international system is anarchic;
2. great powers possess some offensive military capability;
3. states cannot be certain about other states' intentions;
4. survival is the primary goal of great powers;
5. great powers are rational strategic actors.

These assumptions define the strategic environment. They do not give ACTIR an
oracle, erase uncertainty, or predetermine one Japanese strategy. Other
scholarship may enter the Atlas as source material, but it does not supply
additional governing axioms.

## The Atlas record

The fundamental unit is an action–mechanism claim:

```text
actor → observation → action → target → expected mechanism
      → response → adaptation → outcome → evidence
```

ACTIR preserves four epistemically different layers:

1. what a state says;
2. what a state is reported to have done;
3. how a source explains or evaluates the action;
4. what independently verifiable outcomes followed.

Each record retains its document, passage, date, source type, epistemic status,
extraction history, verification decision, and human adjudication. An LLM may
assist extraction; it is never the epistemic authority.

## From Atlas to decision support

```text
Japanese decision question and evidence
                  ↓
 retrieve analogous actions, mechanisms, failures, and responses
                  ↓
 compose conditional policy programs and neglected alternatives
                  ↓
 challenge them across uncertain intentions and plausible responses
                  ↓
 evaluate security, prosperity, autonomy, regional order, and reversibility
                  ↓
 preserve a diverse portfolio with provenance and unresolved disagreement
                  ↓
 human adoption, rejection, revision, or abstention
```

Japan's four immediate policy domains—self-help and resilience, the
United States–Japan alliance, FOIP-oriented regional networks, and relations
with China—are initial retrieval views. They do not limit the Atlas's action
grammar, which must also represent restraint, delay, ambiguity, reassurance,
diversification, delegation, institution-building, domestic mobilization, and
deliberate inaction.

## ShinkaEvolve compatibility

The Atlas supplies ACTIR's evidence; ACTIR owns the decision loop.
ShinkaEvolve is a replaceable search backend that may later propose or mutate
inspectable policy programs against a frozen ACTIR task. It may not silently
alter evidence, the five assumptions, constraints, outcome definitions,
held-out cases, or human authority.

ACTIR will first work deterministically without an API. Once the schema,
retrieval, evaluation, and decision dossier are independently viable, the same
candidate interface can support enumeration, human proposals,
quality-diversity search, or ShinkaEvolve.

## Status: Stage A.1

This branch replaces the January 2026 notebook experiment with the Statecraft
Atlas north star. The earlier files remain recoverable in Git history but are
not part of the new repository tree.

Stage A.1 adds only the typed, versioned Statecraft Atlas schema. It asks one
question: can the contract's epistemic distinctions and decision-support
artifacts be represented without collapsing them?

- [`docs/STATECRAFT_ATLAS_CONTRACT.md`](docs/STATECRAFT_ATLAS_CONTRACT.md)
- [`docs/DEVELOPMENT_PROTOCOL.md`](docs/DEVELOPMENT_PROTOCOL.md)
- [`src/actir/statecraft_atlas/schema.py`](src/actir/statecraft_atlas/schema.py)

This stage contains no corpus record, extraction, semantic validator,
retrieval, simulation, search, result, API call, or ShinkaEvolve dependency.
Stage A.2 will add semantic validation against these frozen types.

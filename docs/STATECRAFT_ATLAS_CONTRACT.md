# ACTIR Statecraft Atlas Contract

## 1. Purpose

ACTIR—the Adaptive Computational Theory of International Relations—is the
framework. The Statecraft Atlas is its versioned dataset and evidence layer. It
converts provenance-bearing evidence about statecraft into structured
action–mechanism records, connects those records into policy sequences, and
makes them usable by ACTIR for retrieval, counterfactual challenge, portfolio
construction, and adaptive decision support.

The Atlas is not a topic model, an unverified LLM knowledge base, a catalog of
academic schools, or a machine for declaring one universally best strategy.

## 2. Axiomatic boundary

The only governing IR assumptions are the five bedrock assumptions of
Mearsheimer's offensive realism:

1. the international system lacks a central authority above states;
2. great powers retain some capacity to harm or destroy one another;
3. intentions cannot be known with certainty;
4. survival is the primary goal;
5. great powers reason strategically about how to survive.

ACTIR operationalizes these assumptions without adding perfect information,
automatic aggression, inevitable war, or a predetermined policy ranking.
Uncertainty about intentions makes inference necessary. Offensive capability
makes error consequential. Anarchy makes external guarantees provisional.
Survival constrains other goals. Rationality makes conditional policy programs
and anticipated responses appropriate objects of analysis.

Japan is the focal decision-maker inside a regional system containing great
powers. The contract does not require every actor to be classified as a great
power or reduced to an identical unit.

## 3. Epistemic layers

The Atlas never collapses the following into one field:

- **discourse:** what an authorized state representative says, promises,
  threatens, demands, justifies, or leaves ambiguous;
- **reported action:** what a source claims an actor did or deliberately did
  not do;
- **source explanation:** the mechanism a source claims connected situation,
  action, response, and outcome;
- **outcome verification:** what additional evidence supports, contradicts, or
  leaves unresolved about the reported consequences.

A statement of intent is not an action. A reported action is not necessarily a
verified event. A source's explanation is not an ACTIR causal conclusion.

## 4. Unit of analysis

The canonical record is:

```text
<actor, observation, action, target, context, expected mechanism,
 counterpart response, adaptation, outcome, evidence>
```

Every record also stores:

- original wording and exact evidence span;
- document, author or speaker, date, page or paragraph, and stable identifier;
- source and document type;
- whether the content is observed, alleged, inferred, recommended, predicted,
  hypothetical, or counterfactual;
- global and regional strategic context at the recorded time;
- capability and role descriptions as asserted by the source;
- action instrument, domain, intensity, duration, cost, and reversibility;
- mechanism assumptions, scope conditions, and stated confidence;
- intended and reported consequences;
- extraction model or method, verifier decision, revisions, abstentions, and
  human adjudication;
- links to preceding and subsequent records in a policy sequence.

The Atlas records source claims about mechanisms without adopting additional
IR theories as governing assumptions.

## 5. Initial corpus boundary

The long-term Atlas has three connected layers:

1. **ACTIR-IS50:** action–mechanism claims extracted from substantive
   contributions to *International Security*, 1976–2026;
2. **ACTIR-UNGDC:** an ACTIR speech-act layer over the existing UN General
   Debate Corpus, beginning in 1946;
3. **Outcome verification:** a thinner independently sourced layer for checking
   consequential actions, responses, and outcomes.

Neither corpus is identical to world behavior or representative of all global
knowledge. Coverage, editorial selection, language, geography, actor visibility,
and security-domain bias must be measured and reported.

The initial implementation contains schemas and synthetic or permission-safe
fixtures only. It does not redistribute copyrighted articles or automate bulk
text mining without the relevant authorization.

## 6. Action grammar and policy programs

The ontology must include positive action, restraint, non-use, delay, waiting,
ambiguity, concealment, delegation, reassurance, accommodation,
diversification, institution-building, domestic mobilization, capability
construction, recognition, legitimation, and deliberate inaction.

Atomic actions become decision-support material only when connected into
conditional programs:

```text
observation_t → interpretation_t → action_t → response_t+1
              → adaptation_t+2 → outcome
```

A `PolicyProgram` therefore contains conditions, actions, expected mechanisms,
fallbacks, stopping conditions, resource commitments, reversibility, and
provenance links. It remains inspectable by a human reviewer.

For Japan after 2022, self-help, alliance management, FOIP-oriented networking,
and China policy are retrieval and composition views over this wider grammar.

## 7. Decision-support contract

An ACTIR decision query supplies a dated question, current evidence, constraints,
objectives, horizons, resource envelope, and an authorization policy. The Atlas
must return a dossier containing:

- analogous historical and proposed actions with provenance;
- mechanisms and scope conditions claimed for each action;
- counterpart responses, adaptations, failures, and unresolved outcomes;
- conditional policy programs, including neglected and inactive alternatives;
- explicit uncertainties and competing interpretations of intentions;
- security, prosperity, strategic-autonomy, regional-order, cost, and
  reversibility consequences kept as a visible vector;
- hard-constraint violations and failure reasons;
- behavioral differences among viable options;
- citations and an audit trail for every machine-produced transformation;
- an abstention or evidence-request pathway when the record is insufficient.

Human authorities define national interests, constraints, acceptable evidence,
objective weights, and adoption. ACTIR cannot execute policy or permanently
self-authorize.

## 8. Search-backend contract

ACTIR owns evidence, schema, retrieval, inference, scenario interfaces,
constraints, evaluation, provenance, portfolio construction, and human
authorization. A search backend receives a frozen task and returns inspectable
candidate programs.

```python
class PolicyProgram(Protocol):
    def decide(self, observation, memory): ...

class CandidateGenerator(Protocol):
    def generate(self, task, population, budget): ...
```

The initial generator is deterministic and API-free. ShinkaEvolve later
implements `CandidateGenerator` without becoming an architectural dependency.
It may mutate policy-program code but not the Atlas records, axioms, evaluator,
constraints, hidden cases, or authorization policy. Behavioral novelty and
source-code novelty remain separate measurements.

## 9. Non-negotiable invariants

- every extracted claim has exact provenance or is rejected;
- discourse, reported behavior, explanation, and verified outcome remain
  separate;
- source claims never become ACTIR conclusions without verification status;
- candidate programs never receive hidden world labels;
- deterministic replay is available for every transformation and dossier;
- constraints, objectives, preferences, and uncertainties are separate;
- outcome vectors and hard failures cannot be erased by scalarization;
- disagreement, abstention, and negative evidence survive the pipeline;
- held-out evidence cannot guide extraction or candidate generation;
- search conditions use matched budgets and disclosed seeds;
- human authorities can reject, revise, defer, or halt the process.

## 10. Initial non-goals

The first prototype does not claim exhaustive statecraft coverage, causal truth,
forecasting of intentions, autonomous Japanese policy recommendation,
coevolving worlds, goal switching, evaluator evolution, open-ended evolution,
or recursive self-improvement. It does not treat an LLM as an epistemic
authority or novelty as beneficial before a matched test demonstrates it.

## 11. Prototype acceptance condition

Before ShinkaEvolve integration, ACTIR must complete one API-free,
exactly replayable decision query over a small validated fixture corpus. It must
retrieve relevant action–mechanism records, preserve their epistemic status,
compose at least two meaningfully different conditional policy programs, expose
their provenance and trade-offs, identify insufficient evidence, and permit a
human reviewer to adopt, reject, revise, defer, or request alternatives.

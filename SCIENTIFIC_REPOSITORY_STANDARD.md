# Scientific Repository Standard

## Constitution for executable scientific papers on GitHub

**Version:** 1.0.0  
**Status:** Adopted  
**Effective date:** 2026-09-04  
**Scope:** All new research repositories and all progressively migrated existing repositories in the ReloadLightly portfolio

---

## Preamble

A research repository is not merely a container for code. It is a scientific argument whose method happens to be executable.

Every repository governed by this standard must make the following chain visible, testable, and inspectable:

> **question → hypothesis or objective → method → experiment or evidence → result → interpretation → bounded claim**

The README is the compact paper. The source code is the executable method. Experiment configurations are the protocol. Tests protect methodological validity. Raw outputs are the evidence. Analysis scripts transform evidence into reported findings. Figures and tables communicate those findings. Releases freeze citable versions of the study.

The purpose of this standard is not to impose more engineering. Its purpose is to prevent engineering from replacing research.

---

# Article I — Authority, scope, and interpretation

## 1.1 Governing rule

This standard governs the structure, scientific narrative, evidence handling, visual language, and migration of all research repositories in the portfolio.

It applies to:

- computational experiments;
- datasets and evidence databases;
- benchmarks and evaluation suites;
- artificial-life and evolutionary-computation studies;
- post-training and multi-agent systems research;
- computational social science and international-relations projects;
- research-oriented tools, websites, and books when they are maintained in repositories.

## 1.2 Scientific structure, not performative uniformity

All repositories must share the same epistemic structure, but they must not pretend to be the same kind of study.

An experimental repository should state hypotheses, baselines, variables, and results. A dataset repository should state its collection question, inclusion rules, coverage, provenance, validation, and known gaps. A theoretical or design repository should state its problem, propositions, artifacts, evaluation criteria, and limitations. A replication repository should distinguish faithful reconstruction from modern extension.

No repository may invent experiments, hypotheses, or findings merely to resemble a paper.

## 1.3 Normative terms

The words **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, and **MAY** indicate decreasing levels of obligation.

## 1.4 Precedence

The order of authority is:

1. this standard;
2. a repository-specific scientific contract or frozen protocol;
3. the README;
4. experiment configurations and analysis plans;
5. implementation details.

A repository-specific protocol may be stricter than this standard. It may deviate only when the deviation is scientifically necessary and explicitly recorded in the README under **Deviations from the standard**.

---

# Article II — The repository as an executable paper

## 2.1 Required organizing logic

Repository work must be organized around:

> **question → evidence → claim**

It must not be organized primarily around:

> features → modules → infrastructure → documentation

## 2.2 Scientific role of repository components

| Repository component | Scientific role |
|:---|:---|
| `README.md` | Compact paper and primary research narrative |
| Source code | Executable method or artifact |
| Experiment configuration | Frozen or versioned protocol |
| Tests | Checks on implementation correctness and scientific invariants |
| Raw results | Primary evidence |
| Analysis scripts | Reproducible transformation from evidence to findings |
| Tables and figures | Scientific communication |
| `CITATION.cff` | Scholarly identity and preferred citation |
| Release or tag | Frozen, citable study version |
| Commit hash | Exact provenance of an execution |

## 2.3 The anti-bloat rule

A new abstraction, service, layer, module, schema, workflow, or dependency may be added only when it does at least one of the following:

1. enables a specified experiment;
2. prevents a concrete validity failure;
3. makes a reported result reproducible;
4. materially reduces the complexity of the scientific workflow;
5. supports a clearly named reuse case already present in the research program.

“Good engineering practice,” architectural symmetry, hypothetical scale, or future flexibility are not sufficient on their own.

## 2.4 The learning test

Before substantial work begins, the repository must be able to answer:

> What will we know after this work that we do not know now?

If the answer is only “the codebase will be more complete,” the proposed work is not yet a research step.

---

# Article III — Scientific stages and honest status

Every repository must declare one current scientific stage near the top of its README.

| Stage | Meaning | Permitted claim language |
|:---|:---|:---|
| **Protocol** | The question, method, and decision rules are being specified | No empirical findings |
| **Exploratory** | Pilots or calibration are being used to understand the system | Preliminary observations only |
| **Frozen** | Confirmatory design, metrics, exclusions, and budget are fixed | No conclusion until planned evidence is collected |
| **Completed** | Planned analysis is finished and the evidence bundle is available | Bounded findings supported by the frozen evidence |
| **Archived** | Work has stopped or been superseded | Historical claims only; limitations and reason for archival stated |

A repository must not describe itself as completed because its software runs. Completion is scientific: the stated question has been answered to the degree promised, the evidence is available, and the claim boundary is explicit.

Recommended status block:

```markdown
> **Study status:** Frozen  
> **Standard:** Scientific Repository Standard v1.0.0  
> **Primary question:** [one sentence]  
> **Primary claim:** Not yet evaluated  
> **Reproduction:** `[command or “available after confirmatory execution”]`
```

---

# Article IV — The scientific contract

Before expensive implementation or execution, every repository must define a minimal scientific contract.

## 4.1 Mandatory questions

The contract must identify:

1. the research question;
2. the unit of analysis or experimental unit;
3. the scientific contribution sought;
4. hypotheses, propositions, or research objectives;
5. the proposed method or artifact;
6. meaningful baselines or counterfactuals;
7. the primary outcome or validation target;
8. secondary outcomes, if any;
9. success, failure, and abstention criteria;
10. threats to validity;
11. the compute, API, time, or annotation budget;
12. the evidence required for the strongest intended claim.

## 4.2 Hypotheses are not mandatory when inappropriate

Descriptive, archival, dataset, translation, or design projects may replace hypotheses with explicit research objectives or validation questions. The project must still define what evidence would count as success and what its outputs cannot establish.

## 4.3 Baseline discipline

A baseline must represent a meaningful alternative explanation, method, or decision rule. A deliberately weak comparator is not a scientific baseline.

Where relevant, the repository should include:

- a simple heuristic;
- random or uninformed behavior;
- a fixed-capacity or non-adaptive method;
- the previous state of the art;
- an ablation that removes the proposed mechanism;
- an outside option or no-intervention condition.

## 4.4 Pre-execution decision rules

For confirmatory work, the following must be fixed before results are inspected:

- primary metric;
- direction of improvement;
- seed or sampling plan;
- number of runs or stopping rule;
- exclusion criteria;
- aggregation method;
- uncertainty estimate;
- threshold or rule for accepting, rejecting, or leaving a hypothesis unresolved.

---

# Article V — The README as a compact scientific paper

## 5.1 Purpose

The README must allow a technically literate reader to understand the study without opening the source tree.

Within the first screen, the reader should be able to identify:

- the problem;
- the study status;
- the central method;
- the strongest supported finding, or the fact that no finding is yet available;
- the shortest reproduction path.

## 5.2 Canonical section order

A full README should use the following order. Sections that genuinely do not apply may be omitted, but their absence must not hide missing scientific work.

```markdown
# [Scientific title]

> [One sentence stating the problem, method, and strongest supported finding—or current study status.]

> **Study status:** [Protocol | Exploratory | Frozen | Completed | Archived]  
> **Standard:** Scientific Repository Standard v1.0.0  
> **Primary claim:** [bounded claim or “not yet evaluated”]  
> **Reproduction:** `[shortest command]`

[up to four restrained badges]

## Abstract

## 1. Research question

## 2. Why this matters

## 3. Contributions

## 4. Related work

## 5. Hypotheses or research objectives

## 6. Method

## 7. Experimental design or evidence protocol

## 8. Results

### 8.1 Primary result
### 8.2 Robustness, ablations, or validation
### 8.3 Failure cases and null results

## 9. Interpretation

## 10. Limitations and threats to validity

## 11. Reproduction

## 12. Repository map

## 13. Citation

## 14. License and responsible use
```

## 5.3 Abstract

The abstract should normally be 150–250 words and must state:

1. the problem;
2. the research question;
3. the method;
4. the evidence or experimental design;
5. the principal result, if available;
6. the boundary of the claim.

An unfinished study must not use future results as if they already existed.

## 5.4 Contributions

Contributions should be separated where useful into:

- **conceptual** — a new framing, construct, or theoretical connection;
- **methodological** — a new experimental or computational method;
- **empirical** — a new result or observation;
- **artifact** — a reusable dataset, benchmark, implementation, or evidence bundle.

A repository must not claim all four by default.

## 5.5 Results-first communication

When results exist, the primary result must appear before implementation details. The README should not force readers through installation instructions before revealing what the study found.

## 5.6 Claim language

The README must distinguish:

- **finding** — directly supported by reported evidence;
- **interpretation** — a reasoned account of what the finding may mean;
- **speculation** — a plausible but untested extension;
- **future work** — work not yet performed.

These categories must not be blended into a single triumphant conclusion.

## 5.7 Failure visibility

Negative results, failed hypotheses, ceiling effects, sensitivity, non-convergence, and uninformative experiments are part of the scientific record. They must not be hidden merely because they weaken the narrative.

---

# Article VI — Canonical repository structure

## 6.1 Minimal principle

The directory tree must be as small as the study permits. The following is the canonical full structure, not a requirement to create empty folders.

```text
repository/
├── README.md
├── SCIENTIFIC_REPOSITORY_STANDARD.md
├── CITATION.cff
├── LICENSE
├── pyproject.toml                 # or the ecosystem equivalent
│
├── src/
│   └── project_name/              # executable method
│
├── experiments/
│   ├── configs/                   # versioned experimental conditions
│   ├── run.py                     # primary experiment entry point
│   └── README.md                  # protocol detail beyond the main README
│
├── analysis/
│   ├── analyze.py                 # evidence → reported statistics
│   └── make_figures.py            # statistics → figures and tables
│
├── results/
│   ├── README.md                  # provenance and result inventory
│   ├── raw/                       # immutable primary outputs when practical
│   ├── derived/                   # reproducibly generated summaries
│   └── manifest.json              # execution and provenance metadata
│
├── figures/
│   ├── main-result.svg
│   └── method-overview.svg
│
├── tests/
│   └── ...                        # correctness and scientific invariants
│
└── scripts/
    └── reproduce.sh               # shortest route to the central result
```

## 6.2 Meaningful directories only

A directory may be omitted when the project does not need it. A project must not create folders to look complete.

Examples:

- a small deterministic replication may not need `scripts/`;
- a dataset repository may use `data/`, `schema/`, and `validation/` instead of `src/`;
- a theory repository may use `models/`, `examples/`, and `checks/`;
- a website repository may keep its framework structure while presenting the research logic in the README.

## 6.3 Root-level constitution

Every newly created repository must include `SCIENTIFIC_REPOSITORY_STANDARD.md` at the root or a root-level pointer that pins the exact adopted version and records any deviations.

The canonical version should ultimately live in a dedicated public standards or template repository. Local copies make the governing version inspectable from an offline clone.

---

# Article VII — Experimental and evidence discipline

## 7.1 Separate exploration from confirmation

Exploratory work may tune environments, discover bugs, select metrics, or reveal ceiling and floor effects. Confirmatory work must use a frozen design.

Exploratory evidence must not be silently promoted into confirmatory evidence.

## 7.2 Smallest informative experiment

Before scaling, run the smallest experiment that can falsify the central mechanism or expose a broken design.

The preferred progression is:

1. deterministic unit or toy check;
2. minimal pilot;
3. calibration;
4. frozen matched comparison;
5. robustness or extension only if the primary result warrants it.

## 7.3 Budget before execution

Every costly run must declare a budget before execution, including relevant limits on:

- wall-clock time;
- CPU, GPU, or memory;
- API spend;
- number of model calls;
- human annotation;
- seeds or replications.

A run that exceeds its budget must stop or be explicitly reauthorized. More compute is not automatically more science.

## 7.4 Raw and derived evidence

Raw outputs must be preserved unchanged whenever practical. Reported tables and figures must be generated from raw or immutable intermediate outputs by versioned analysis code.

Manually copying numbers into a README is acceptable only for tiny results and only when the source file and derivation are clearly identified. Automated generation is preferred.

## 7.5 Result provenance

Each confirmatory result bundle should record:

- repository commit SHA;
- standard version;
- configuration file and hash;
- command executed;
- environment and dependency lock;
- seed or sampling identifier;
- hardware or execution host where material;
- start and completion times;
- raw output locations;
- analysis script version;
- exclusions and reasons;
- model, provider, prompt, cache, and cost metadata for LLM-dependent work.

## 7.6 Evidence-to-claim traceability

Every principal claim in the README must point to the table, figure, result file, or analysis artifact that supports it.

A reader should be able to move in both directions:

> claim → reported result → analysis → raw evidence → configuration → code commit

and

> raw evidence → analysis → reported result → bounded claim

---

# Article VIII — Code, tests, and reproducibility

## 8.1 Code serves the study

Code quality matters because scientific claims depend on it. Code architecture is not itself the scientific contribution unless the repository explicitly studies architecture.

## 8.2 Tests must protect something real

Every test should map to at least one of:

- a known or plausible implementation failure;
- a scientific invariant;
- a frozen contract;
- a reproduction path;
- a previously observed regression;
- a boundary condition that would invalidate a claim.

Tests must not be added merely to increase test counts or create governance theater.

## 8.3 Scientific invariants

Where relevant, tests should demonstrate properties such as:

- conservation or accounting identities;
- seed determinism;
- separation of training and held-out data;
- unchanged frozen baselines;
- equal budgets across treatment conditions;
- absence of information leakage;
- correct outside-option or welfare accounting;
- faithful replay of cached model responses;
- reproducible aggregation and figure generation.

## 8.4 Reproduction target

Every completed repository should provide one shortest documented route to its central result.

Preferred form:

```bash
git clone <repository>
cd <repository>
<environment setup>
<one reproduction command>
```

Where full reproduction is costly, the repository must provide:

1. a low-cost verification path;
2. the frozen full protocol;
3. the original result bundle;
4. the exact command used for the full run.

## 8.5 Determinism and stochasticity

Deterministic components must be deterministic under documented conditions. Stochastic components must expose and record seeds or sampling identifiers. Claims must reflect variation across runs rather than a single favorable trajectory.

---

# Article IX — Shared minimalist visual system

## 9.1 Design objective

Visual design must reduce cognitive load while increasing scientific legibility. Beauty should emerge from alignment, restraint, hierarchy, spacing, and consistency—not decoration.

The portfolio should look like a coherent research laboratory without making different studies visually indistinguishable.

## 9.2 Core palette

Generated figures, diagrams, and repository graphics should use the following default palette:

| Role | Value | Use |
|:---|:---|:---|
| Paper | `#FFFFFF` | Background |
| Ink | `#111827` | Primary text and axes |
| Slate | `#475569` | Secondary text and baselines |
| Muted | `#94A3B8` | Secondary marks and annotations |
| Rule | `#E2E8F0` | Borders, dividers, and light grids |
| Accent | `#0072B2` | One focal method, result, or path |

Rules:

- Use white or transparent backgrounds.
- Use grayscale for most information.
- Use the accent color only to direct attention.
- Do not use color as the sole carrier of meaning.
- Use additional colors only when the scientific content genuinely requires categorical distinction; pair them with labels, markers, line styles, or patterns.
- Avoid gradients, glow, shadows, glass effects, and decorative textures.

## 9.3 Typography

- GitHub-native text should use GitHub’s default typography.
- Generated scientific visuals should use a reproducible system sans-serif, preferably `DejaVu Sans` where available.
- Use at most two font weights in a single visual.
- Titles use sentence case, not title case.
- Avoid all-caps labels except short identifiers such as `H1` or `CPU`.
- Mathematical notation and variable names must be consistent across prose, code, tables, and figures.

## 9.4 Figure dimensions and formats

- Prefer SVG for repository figures and diagrams.
- Prefer PDF or SVG for manuscript export.
- Use PNG only when raster output is necessary.
- Design full-width README figures for approximately 960 px display width.
- Avoid extremely wide or tall figures that interrupt reading flow.
- Preserve consistent margins and visual density across repositories.
- Every figure must have meaningful alternative text and a caption.

## 9.5 Figure grammar

A scientific figure must include, where applicable:

- a claim-oriented title;
- labeled axes with units;
- sample size or number of runs;
- uncertainty representation;
- direct labels or a compact legend;
- a caption stating what is shown, under what conditions, and how it should be read.

Prefer titles that communicate the finding:

> **Adaptive search improves early, while later generations mostly increase complexity**

rather than generic titles such as:

> **Fitness by generation**

## 9.6 Chart rules

Charts must:

- use a zero baseline when the quantity and comparison require it;
- avoid truncated axes that exaggerate differences unless clearly justified;
- avoid dual y-axes except under exceptional, explained circumstances;
- show individual runs or distributions when means alone would conceal instability;
- include uncertainty for stochastic comparisons;
- use direct labeling when it reduces legend lookup;
- place the baseline before the proposed method in reading order;
- avoid 3D effects, chart junk, unnecessary icons, and ornamental annotations.

For two-method comparisons, the preferred grammar is:

- baseline in slate or gray;
- proposed method in the single accent color;
- uncertainty in a lighter shade or transparent band;
- distinct markers or line styles so the plot remains legible without color.

## 9.7 Diagram rules

Method and system diagrams should:

- read left to right or top to bottom;
- express one principal process;
- use short noun labels for entities and verb labels for transformations;
- minimize crossing arrows;
- use consistent shape semantics;
- avoid more than roughly seven primary nodes in one view;
- move implementation detail into a secondary diagram when necessary;
- use the accent color for the focal loop or novel mechanism only.

## 9.8 Badge rules

A README may use no more than four badges near the top. Preferred badges are:

1. tests or reproducibility;
2. study status or release;
3. license;
4. citation or archival identifier.

Avoid oversized badge styles, vanity metrics, and walls of platform logos.

## 9.9 Table constitution

GitHub tables must remain native Markdown whenever possible. Their visual quality comes from disciplined structure rather than custom HTML.

Every scientific table must have:

1. a numbered, descriptive title above it;
2. no more than roughly six columns in the main README;
3. units and metric direction in headers;
4. text columns left aligned and numeric columns right aligned;
5. consistent precision within each column;
6. run count, sample size, or coverage where relevant;
7. uncertainty where the process is stochastic;
8. restrained emphasis;
9. a one-sentence reading immediately below it.

### 9.9.1 Primary result table template

```markdown
**Table 1 — Primary comparison under the frozen test condition**

| Method | Performance ↑ | Complexity ↓ | Runs | Uncertainty | Role |
|:---|---:|---:|---:|---:|:---|
| Fixed baseline | 0.812 | 65.0 units | 30 | ±0.014 | Baseline |
| Random search | 0.821 | 18.4 units | 30 | ±0.012 | Comparator |
| Proposed method | **0.846** | **5.3 units** | 30 | ±0.009 | Primary |

*Reading:* The proposed method improves the primary outcome while using fewer active units; the robustness analysis below determines how broadly that result can be interpreted.
```

Illustrative values must never be mistaken for project results.

### 9.9.2 Hypothesis table template

```markdown
**Table 1 — Confirmatory hypotheses and decision rules**

| ID | Hypothesis | Operational test | Primary metric | Decision rule |
|:---|:---|:---|:---|:---|
| H1 | [claim] | [matched comparison] | [metric ↑] | [predeclared rule] |
| H2 | [claim] | [ablation] | [metric ↓] | [predeclared rule] |
```

### 9.9.3 Experimental design table template

```markdown
**Table 2 — Frozen experimental design**

| Element | Specification |
|:---|:---|
| Experimental unit | [unit] |
| Conditions | [conditions] |
| Seeds or samples | [plan] |
| Primary metric | [metric and direction] |
| Stopping rule | [rule] |
| Compute budget | [budget] |
```

### 9.9.4 Table prohibitions

Do not use:

- screenshots of tables;
- empty cells when `—` would communicate absence;
- mixed precision without justification;
- colored emoji as status indicators;
- bolding of every favorable number;
- a “best” label when differences are not meaningfully comparable;
- giant configuration dumps in the README;
- horizontally scrolling tables when a supplementary CSV or Markdown file would be clearer.

---

# Article X — Scientific writing and claim discipline

## 10.1 Tone

Writing should be confident about what the evidence supports and explicit about what remains uncertain.

Avoid marketing language such as “revolutionary,” “breakthrough,” “state of the art,” or “solves” unless the repository provides a comparison and evidence adequate to defend the term.

## 10.2 Strongest defensible sentence

Every repository should identify:

> the strongest scientifically defensible sentence the current evidence supports.

The README, figures, directory structure, and reproduction path should be organized around that sentence.

## 10.3 No result laundering

A result observed during calibration, debugging, prompt selection, environment tuning, or baseline construction must not be reported as untouched confirmatory evidence.

## 10.4 Null and unresolved conclusions

“Unresolved under the current design” is a legitimate conclusion. A study must not force a binary success story when the evidence is weak, noisy, ceiling-saturated, underpowered, or internally inconsistent.

---

# Article XI — Citation, provenance, licensing, and responsible use

## 11.1 Citation

Every mature repository should contain `CITATION.cff` and a preferred citation block in the README.

The citation should identify:

- author or authors;
- title;
- year;
- version or release;
- repository or archival identifier;
- DOI when available.

## 11.2 Sources and related work

External datasets, papers, models, repositories, and frameworks must be cited at the point where they inform the method or claim. A generic references dump does not replace source-to-claim attribution.

## 11.3 Data provenance

Dataset and evidence repositories must document:

- source origin;
- collection dates;
- inclusion and exclusion rules;
- transformations;
- licensing constraints;
- known coverage gaps;
- human and model-assisted annotation roles;
- verification and adjudication procedures.

## 11.4 Responsible use

Repositories involving human data, political decision support, model behavior, or potentially consequential deployment must state relevant ethical, privacy, misuse, and authority boundaries.

---

# Article XII — Migration manual for existing repositories

Existing repositories must be migrated one at a time. Migration is a scientific reconstruction, not a mass formatting exercise.

## 12.1 Migration principle

Do not begin by rearranging directories.

Begin by asking:

> What question does this repository address, what evidence currently exists, and what is the strongest claim it can honestly support?

## 12.2 Migration passes

| Pass | Objective | Required output |
|:---|:---|:---|
| **0. Preserve** | Protect the current state | Baseline tag, branch, archive, or recorded commit SHA |
| **1. Extract** | Recover the actual scientific question and contribution | One-page scientific inventory |
| **2. Audit evidence** | Identify authentic results, missing provenance, and unsupported claims | Evidence-to-claim map |
| **3. Rebuild README** | Convert the narrative into a compact paper | Standard-conforming README |
| **4. Normalize evidence** | Separate raw, derived, and reported results | Result inventory and manifest |
| **5. Normalize visuals** | Restyle decisive tables and figures | Reproducible standard-conforming visuals |
| **6. Reproduce** | Establish the shortest valid path to the central result | Documented reproduction command |
| **7. Prune** | Remove or archive layers that do not support the study | Smaller, clearer scientific surface |
| **8. Freeze** | Create a citable scientific version | Release, tag, citation, and final limitations |

## 12.3 One reviewable step at a time

A migration should normally use small, reviewable pull requests. A recommended sequence is:

1. scientific inventory and status correction;
2. README reconstruction;
3. result and provenance normalization;
4. visual normalization;
5. reproduction path;
6. structural cleanup only after the scientific shape is clear.

A migration must not rewrite code merely to match the canonical directory tree.

## 12.4 Evidence-to-claim map

Each migration should create a temporary or permanent table like this:

```markdown
| Intended claim | Current evidence | Confidence | Gap | Action |
|:---|:---|:---|:---|:---|
| [claim] | [files/runs] | [high/medium/low] | [gap] | [retain/retest/withdraw] |
```

This table determines what survives into the rebuilt README.

## 12.5 Migration stop condition

A migration pass is complete when it improves scientific legibility or reproducibility without opening unrelated engineering work.

Do not use migration as permission to redesign the entire codebase.

---

# Article XIII — Bootstrap procedure for new repositories

## 13.1 First commit

A new research repository should begin with:

- `README.md` containing the title, status, question, contribution, method sketch, and next experiment;
- `SCIENTIFIC_REPOSITORY_STANDARD.md` pinned to the adopted version;
- a license;
- a minimal environment definition if code exists;
- no speculative infrastructure.

## 13.2 Before implementation

Before the first substantial implementation milestone, the repository must state:

- what the first informative experiment is;
- what baseline it uses;
- what result would falsify or weaken the central idea;
- what the run will cost;
- where the evidence will be stored.

## 13.3 Template repository

The canonical standard should be paired with a GitHub template repository containing:

- this constitution;
- the README skeleton;
- minimal result and figure conventions;
- a restrained pull-request checklist;
- no domain-specific source code.

New repositories should be created from that template whenever practical. GitHub template repositories copy the template’s files and directory structure into a new repository, making them the appropriate mechanism for initializing this standard consistently.

## 13.4 Account-level defaults

A public account-level `.github` repository should hold supported default community-health files, especially:

- `CONTRIBUTING.md`;
- `.github/PULL_REQUEST_TEMPLATE.md`;
- issue templates for experiments, replications, and migrations when genuinely useful.

The account-level defaults should reference this constitution without duplicating unnecessary process.

---

# Article XIV — Incremental conformance levels

These levels are migration milestones, not permanent alternative standards.

| Level | Name | Minimum state |
|:---|:---|:---|
| **SRS-1** | Paper-shaped | Honest status, question, contribution, method, limitations, standard README order |
| **SRS-2** | Evidence-linked | Hypotheses or objectives, baselines, result provenance, claim-to-evidence links, reproduction path |
| **SRS-3** | Paper-ready | Frozen evidence bundle, reproducible figures and tables, citation, release, full limitations |

New protocol-stage repositories may begin at SRS-1. Completed studies should reach SRS-3.

A repository must never claim a higher level merely because the required file names exist.

---

# Article XV — Adoption checklist

A repository conforms to this standard only when the substantive answers are present.

## 15.1 Scientific core

- [ ] The research question is stated in one sentence.
- [ ] The repository’s current scientific stage is explicit.
- [ ] Contributions are bounded and not inflated.
- [ ] Hypotheses, objectives, or validation questions are testable.
- [ ] Baselines or counterfactuals are meaningful.
- [ ] Success, failure, and unresolved outcomes are defined.
- [ ] Limitations and threats to validity are visible.

## 15.2 Evidence and reproducibility

- [ ] The primary claim points to specific evidence.
- [ ] Raw and derived results are distinguishable.
- [ ] Confirmatory design is frozen before confirmatory inspection.
- [ ] Seeds, samples, exclusions, and budgets are recorded.
- [ ] The central result has a documented reproduction path.
- [ ] Figures and tables are generated reproducibly where practical.
- [ ] Tests protect concrete failure modes or scientific invariants.

## 15.3 Communication and design

- [ ] The README functions as a compact paper.
- [ ] The main result or honest no-result status appears early.
- [ ] Tables follow the shared table constitution.
- [ ] Figures follow the shared minimalist visual system.
- [ ] Color is not the sole information channel.
- [ ] Badges and decorative elements are restrained.
- [ ] Terminology, units, notation, and precision are consistent.

## 15.4 Scholarly identity

- [ ] The repository has a license.
- [ ] Mature work has `CITATION.cff`.
- [ ] External sources and artifacts are attributed.
- [ ] A release or tag freezes completed work.
- [ ] Responsible-use boundaries are stated where relevant.

---

# Article XVI — Governance of this standard

## 16.1 Versioning

This standard uses semantic versioning:

- **patch** releases clarify wording without changing obligations;
- **minor** releases add backward-compatible guidance or templates;
- **major** releases change required structure or scientific obligations.

## 16.2 Evidence-based revision

The standard should change only to solve an observed problem encountered while creating, executing, reviewing, or migrating a real repository.

No rule should be added merely because it sounds comprehensive.

## 16.3 Bureaucracy budget

Every proposed new requirement must answer:

1. What concrete failure does it prevent?
2. What scientific value does it add?
3. Can an existing requirement be simplified or removed in exchange?

The standard must not become the kind of engineering layer it was created to prevent.

## 16.4 Deviations

A repository may deviate when scientific necessity requires it. The README must then include:

```markdown
## Deviations from the Scientific Repository Standard

| Rule | Deviation | Scientific reason | Consequence |
|:---|:---|:---|:---|
| [section] | [change] | [reason] | [effect on comparison or reproducibility] |
```

## 16.5 Review cycle

The standard should be reviewed after several real migrations, not on a fixed bureaucratic schedule. Revisions should be informed by friction, ambiguity, or failure observed in practice.

---

# Appendix A — Compact README starter

````markdown
# [Scientific title]

> [Problem + method + strongest supported finding or honest current status.]

> **Study status:** Protocol  
> **Standard:** Scientific Repository Standard v1.0.0  
> **Primary claim:** Not yet evaluated  
> **Reproduction:** Not yet available

## Abstract

[150–250 words: problem, question, method, design, result/status, claim boundary.]

## 1. Research question

**Question.** [One precise sentence.]

## 2. Why this matters

[Scientific importance and unresolved gap.]

## 3. Contributions

1. **Conceptual:** [only if applicable]
2. **Methodological:** [only if applicable]
3. **Empirical:** [only if applicable]
4. **Artifact:** [only if applicable]

## 4. Related work

[Smallest relevant lineage and exact unresolved issue.]

## 5. Hypotheses or research objectives

**Table 1 — Hypotheses and decision rules**

| ID | Hypothesis or objective | Operational test | Decision rule |
|:---|:---|:---|:---|
| H1 | [statement] | [test] | [rule] |

## 6. Method

[Representation, algorithm, environment, assumptions, and one central diagram if useful.]

## 7. Experimental design or evidence protocol

**Table 2 — Study design**

| Element | Specification |
|:---|:---|
| Unit | [unit] |
| Conditions | [conditions] |
| Baselines | [baselines] |
| Primary metric | [metric ↑/↓] |
| Seeds or samples | [plan] |
| Budget | [budget] |
| Exclusions | [rules] |

## 8. Results

[Primary result table or: “No confirmatory results are reported at the current stage.”]

## 9. Interpretation

[What the result supports, what it does not, and plausible mechanisms.]

## 10. Limitations and threats to validity

[Internal, external, construct, statistical, and implementation limitations as applicable.]

## 11. Reproduction

```bash
[shortest exact path]
```

## 12. Repository map

| Path | Scientific role |
|:---|:---|
| `src/` | Executable method |
| `experiments/` | Protocols and configurations |
| `results/` | Evidence and provenance |
| `analysis/` | Evidence-to-finding transformations |
| `figures/` | Reproducibly generated visuals |
| `tests/` | Correctness and scientific invariants |

## 13. Citation

[Preferred citation.]

## 14. License and responsible use

[License and relevant boundaries.]
````

---

# Appendix B — Pull-request scientific check

Every substantial pull request should answer four questions in plain language:

```markdown
## Scientific purpose

What question, experiment, evidence, or validity risk does this change address?

## Change

What changed, and what deliberately did not change?

## Evidence

What tests, runs, or inspections support the change?

## Claim impact

Does this strengthen, weaken, narrow, or leave unchanged any README claim?
```

A pull request that cannot answer the first question should usually not be opened.

---

# Appendix C — One-page migration worksheet

```markdown
# Scientific reconstruction: [repository]

## Current question

[What question the repository actually addresses.]

## Intended contribution

[Conceptual / methodological / empirical / artifact.]

## Current evidence

[Files, runs, tables, figures, or none.]

## Strongest defensible claim

[One sentence.]

## Unsupported or overstated claims

[Claims to withdraw, narrow, or retest.]

## Scientific stage

[Protocol / Exploratory / Frozen / Completed / Archived.]

## Smallest next informative step

[One experiment, analysis, or reconstruction step.]

## Migration pass

[0–8 from Article XII.]

## Explicit non-goals

[Engineering work that will not be opened during this pass.]
```

---

# Closing principle

A strong repository should make it easy to answer five questions:

1. What did we ask?
2. What did we do?
3. What did we observe?
4. What may we conclude?
5. How can someone verify it?

Everything else is subordinate.

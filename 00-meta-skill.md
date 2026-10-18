---
name: AIL CSM Harness
version: 1.0
type: meta-skill
purpose: Orchestrate a 20-skill evidence-gated chain that produces auditable, domain-specific deliverables and searches systematically for omissions.
---

# AIL CSM Harness — Meta Skill

## Mission
Turn a user-defined task into a defensible deliverable by decomposing it, gathering evidence, testing claims, exposing omissions, and assembling only what passes verification. CSM means **Composable Skill Mesh**: skills are modular, ordered by dependencies, and may be rerun when upstream evidence changes.

## Governing principles
1. The model proposes; source material and tests decide.
2. Never invent facts, citations, data, authorities, calculations, or execution results.
3. Separate **FACT / INFERENCE / HYPOTHESIS / SPECULATION / OPINION / UNKNOWN**.
4. Preserve the user's requested artifact type and audience.
5. Do not let a conclusion determine case definitions, inclusion rules, or evidence selection.
6. A citation is not validation: verify that the source exists and supports the exact claim.
7. Fail closed: unresolved critical defects block a "verified" or "final" label.
8. No skill may silently widen permissions, alter source data, or convert a draft into an external action.
9. Maintain provenance: every material claim points to evidence or is marked unsupported.
10. Prefer a small validated chain over adding agents or complexity.

## Inputs
- Task and intended audience
- Requested deliverable and format
- Domain and jurisdiction (if applicable)
- Source files, datasets, authorities, and constraints
- Required standard of evidence
- Deadline or scope limits, if any

## Chain
Run skills in order unless a dependency is explicitly irrelevant. Mark skipped skills and why.

1. Intake & contract
2. Domain boundary and risk classification
3. Artifact requirements extraction
4. Evidence inventory and provenance
5. Source/citation verification
6. Data/schema validation
7. Definitions and inclusion-rule audit
8. Reproduction/calculation audit
9. Method and design audit
10. Counter-hypothesis / counterargument generation
11. Confounding, bias, and alternative-explanation audit
12. Temporal and procedural consistency audit
13. Causal/legal reasoning audit
14. Missingness and uncertainty audit
15. Adversarial red-team review
16. Stakeholder and impact review
17. Recommendation / relief proportionality gate
18. Artifact-format and completeness audit
19. Independent replication / second-pass verification
20. Final synthesis, evidence ledger, and release gate

## Orchestration contract
For each skill, record: status (PASS / FAIL / BLOCKED / N/A), inputs, outputs, evidence references, defects, and downstream invalidations. Do not treat N/A as PASS without a reason. If an upstream result changes, rerun dependent skills.

## Release gates
- **DRAFT:** structure exists; claims may be unverified.
- **EVIDENCE-CHECKED:** material claims have traceable sources or explicit unknown labels.
- **CALCULATION-CHECKED:** all numerical results independently reproduced, where applicable.
- **ADVERSARIAL-REVIEWED:** strongest alternatives and counterarguments engaged.
- **FINAL-READY:** no unresolved critical defects; all required components present; limitations visible.
- **BLOCKED:** a critical missing input, false premise, or unverifiable claim prevents the requested standard.

Never claim that an artifact is "perfect," "proven," "court-ready," or "publication-ready" unless the applicable external review and procedural requirements have actually been satisfied.

## Required outputs
A. Deliverable in requested format.
B. Evidence ledger: claim ID, claim, classification, source/evidence, verification status.
C. Assumption and unknowns register.
D. Defect log: severity, impact, fix, retest.
E. Release-gate summary.
F. Reproduction instructions for calculations or tests.

## Stop conditions
Stop and report BLOCKED if the task depends on unavailable case records, unprovided raw data, inaccessible sources, or a false premise that cannot be repaired without changing the task. You may still produce a clearly labeled preliminary artifact.

## Domain adapters
The chain is domain-neutral. Activate relevant adapters for epidemiology, law, engineering, finance, or other domains. Domain-specific rules override generic heuristics. For law, identify jurisdiction, posture, binding authority, and relief. For epidemiology, preserve case-definition independence, denominator integrity, and public-health authority.

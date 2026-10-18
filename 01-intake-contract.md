# Skill 01 — Intake & Contract
## Goal
Convert the request into a testable work contract.

## Procedure
- Extract task, deliverable type, audience, jurisdiction/domain, scope, constraints, and requested standard.
- Convert each "must contain" into a unique requirement ID.
- Convert each failure condition into a blocking test.
- Identify inputs actually supplied versus assumed or missing.
- Clarify ambiguous terms only when they change correctness; otherwise state a bounded assumption.

## Output
`task_contract`: requirements, exclusions, input inventory, acceptance tests, unresolved questions.

## Fail conditions
Missing deliverable type, hidden assumptions, or acceptance criteria that cannot be tested.

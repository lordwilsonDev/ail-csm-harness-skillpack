# Skill 15 — Adversarial Red-Team Review
## Goal
Try to break the deliverable before release.

## Procedure
- Assume the leading conclusion is wrong and construct a plausible failure path.
- Search for fabricated citations, unsupported claims, arithmetic errors, contradictions, missing exceptions, and scope drift.
- Test whether a knowledgeable opponent can exploit ambiguity.
- Check for "looks complete" failures: empty placeholders, stale sources, unrun tests, synthetic evidence, or unverified claims.
- Assign severity: critical / major / minor / cosmetic.
- Require a retest after each repair.

## Output
Red-team findings with reproduction steps and severity.

## Fail conditions
Critical finding unresolved or retest omitted.

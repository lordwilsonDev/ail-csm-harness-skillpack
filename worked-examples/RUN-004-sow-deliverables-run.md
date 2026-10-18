# Worked example 4: take a consultant's promised deliverables and run them

Run 2026-10-18. The idea: take the deliverables a consultant promises in a scope of work (SOW), turn each into a pass/fail requirement (harness steps 01-03), and see which ones the harness plus leanrea can produce.

Source SOW: the State of North Carolina's public template [Statement of Work under STC 918A, security assessment services](https://it.nc.gov/documents/files/918a-security-assessment-services-sow-template/open) (linked, not copied here). It is written for a government agency's whole IT environment. The target here is one open-source program, the installed GitHub CLI (`gh` 2.87.3), so only the software-shaped deliverables apply.

## What the SOW promises (its report outline)
Executive summary; methodology; governance gaps; a matrix of vulnerabilities with remediation; per-item detail ranked high/medium/low with description, external exposure, verification, and mitigation; penetration test results; patching gaps; network security gaps; misconfigurations from traffic; a summary by NIST 800-53 control; overall posture; a prioritized short/long-term remediation plan with estimated costs; appendices (tools used, logs). Services it lists: penetration test, network mapping, vulnerability scan, phishing, wireless, web application, operating system, database.

## Can the harness and leanrea produce it?
| Promised deliverable | Result | Evidence |
|---|---|---|
| Executive summary | PRODUCED | below |
| Methodology and approach | PRODUCED | below |
| Matrix of vulnerabilities and remediation | PRODUCED | `RUN-004-files/RUN-004-vuln-matrix.csv`, 126 rows |
| Risk ranking high/medium/low | PARTLY | Only 29 of 90 merged advisories carry a severity; 61 are unrated by the database |
| Detailed description | PARTLY | One-line advisory summary and fixed-in version per row |
| Verification of vulnerability | NOT DONE | Matches are by version range. Whether the program can reach the flawed code is unknown. Next step: `govulncheck` in binary mode (needs a download, not done without permission) |
| External exposure | NOT ASSESSED | A command-line tool, not a hosted service |
| Patching gaps | PRODUCED | installed 2.87.3 vs latest 2.102.0 (below) |
| Prioritized remediation plan | PRODUCED | below |
| Cost estimates in the plan | NOT PRODUCED | No honest basis for dollar estimates |
| Summary by NIST 800-53 control | INFERRED ONLY | The matching controls are vulnerability monitoring (RA-5) and flaw remediation (SI-2); not mapped control by control |
| Appendix: tools and logs | PRODUCED | this file, the CSV, the scripts and queries listed below |
| Penetration test, network mapping, phishing, wireless, OS and database assessment, governance review, interviews | NOT POSSIBLE | Each needs authorization, access to the customer's systems, a site visit, or people. None of it can be done from a laptop against a public program |
| Vendor's signed certification and presenting the report | NOT POSSIBLE | A signature and accountability belong to a person or firm |

## Evidence gathering (harness step 04 with leanrea)
1. `go version -m` on a copy of the binary gave 161 modules plus the Go toolchain (RUN-002).
2. One batched query to the public OSV database ([osv.dev](https://osv.dev)) sent the 161 module names and versions plus `stdlib 1.26.0` (package names and versions only). Took 0.7 seconds.
3. A second method re-queried each affected package individually: agreed on all 17 of 17.
4. Fetched all 118 advisory records, merged duplicates (a GitHub advisory and a Go advisory often describe the same flaw): 90 unique vulnerabilities.
5. Compared against the latest release: `gh` v2.102.0 (published 2026-09-30), its `go.mod` versions re-queried the same way.

## Executive summary
- 17 of the 162 components (161 modules and the Go standard library) match one or more published advisories for the versions inside the installed binary: 90 unique advisories (8 critical, 8 high, 12 moderate, 1 low, 61 unrated).
- These are version-range matches. They do not prove the program can be attacked through any of them; that was not tested.
- The installed `gh` is 2.87.3 (February 2026). The latest release, 2.102.0 (September 30, 2026), is also what Homebrew's index lists. Using its dependency versions, advisory records on non-standard-library components fall from 80 to 6. Its Go toolchain line is 1.27.1: the standard library has 13 advisory records at 1.27.1 versus 46 at the installed build's 1.26.0 (toolchain version from `go.mod`, not from a built binary).
- Recommended action (not performed): `brew upgrade gh`. Your decision.

## What went wrong or was weak
- Raw advisory counts are alarming and easy to over-read; the harness's "version match is not reachability" rule is the guard. It is stated in the summary instead of the headline.
- 61 of 90 have no severity. I did not invent one.
- No cost or time-saved measurement for the AI part itself; tool runtime was seconds, AI usage unmeasured.

## Limits
Public advisory data only; one program; one pass by one reviewer (self-review); no active testing; not a certification of any kind.

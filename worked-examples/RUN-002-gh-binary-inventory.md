# Worked example 2: harness first, then leanrea (domain: software supply chain)

Run 2026-10-18. Domain chosen: "What is in this installed program?" Target: the GitHub CLI (`gh` 2.87.3) installed on this Mac through Homebrew. Open-source tool, own machine, read-only work on a copy. The 20-step chain (`00-meta-skill.md`) frames the work; the leanrea skill (`extras/leanrea/SKILL.md`) is the tool that gathers the evidence.

## Result in one line
FINAL-READY for the stated scope (static inventory of one binary): all 161 embedded dependencies match the project's own `go.mod` at the same release tag. This is not a security audit and says nothing about how the program behaves when run.

## Contract (steps 01-03)
- Deliverable: an inventory of toolchain, module, dependencies, build settings, and signing.
- Risk: low (read-only, copy of the binary, public project).
- Requirements: R1 Go version. R2 module and version. R3 dependency count and notable ones. R4 build settings. R5 signing. R6 every claim labeled seen / inferred / unknown.

## Evidence gathering with leanrea (step 04)
One batched call, as the skill says (Go row plus the Mach-O row): `go version -m`, `lipo -info`, `otool -L`, `codesign`.

## Ledger
| ID | Claim | Label | Evidence |
|---|---|---|---|
| E1 | Built with Go 1.26.0 | SEEN | `go version -m` line 1; `strings` finds `go1.26.0` (second method) |
| E2 | Module `github.com/cli/cli/v2`, entry `cmd/gh`, module version `(devel)` | SEEN | `go version -m` |
| E3 | 161 embedded dependencies | SEEN | counted two ways, both 161; 0 `replace` entries |
| E4 | Build settings: `-trimpath=true`, `CGO_ENABLED=1`, tag `updateable`, darwin/arm64 | SEEN | `go version -m` build lines |
| E5 | Notable deps: cobra v1.10.2, go-gh v2.13.0, bubbletea v1.3.10, grpc v1.78.0, sigstore-go v1.1.4, go-tuf v2.4.1, go-keyring v0.2.6 | SEEN | `go version -m` |
| E6 | Signed ad hoc by the linker (no developer identity, no team ID), no entitlements | SEEN | `codesign -dv` |
| E7 | Links only system libraries (libSystem, libresolv, CoreFoundation, Security) | SEEN | `otool -L` |
| E8 | All 161 dependency versions equal the versions in the project's `go.mod` at tag `v2.87.3` | SEEN | compared every entry: 161 same, 0 different, 0 missing |
| E9 | This is the official release build | UNKNOWN | Versions match source, but no build attestation was checked. Matching versions don't prove who built it |
| E10 | The 16 `go.mod` entries not found in the binary are test or tool dependencies | INFERRED | Not tested |
| E11 | The `updateable` tag relates to self-update support | INFERRED | Name only; code not read |

## Harness steps 05-20 in brief
| Step | Status | Note |
|---|---|---|
| 05 Sources | PASS | Release tag `v2.87.3` exists upstream; `go.mod` fetched from that tag |
| 06 Data | PASS | Tool output parsed two ways, counts equal |
| 07 Definitions | N/A | None needed |
| 08 Calculations | PASS | 161 = 161; compare 161/161 |
| 09 Method | PASS with limit | Static reading shows build metadata, not behavior |
| 10 Counter-hypothesis | PASS | Strongest alternative: "this is not the upstream source." Versions match for all 161 entries, so it's consistent with upstream, but see E9 |
| 11 Bias | FIXED | First pass compared only 7 deps I picked as "notable." That is selection bias, so I compared all 161. All match |
| 12 Timeline | PASS | Release date 2026-02-23 shown by `gh --version`; Go 1.26.0 consistent with that date |
| 13 Reasoning | PASS | "Matches upstream" is claimed, "is the official build" is not |
| 14 Unknowns | listed | E9, E10, E11 |
| 15 Red team | 1 minor | My first upstream fetch failed because the shell treated `?ref=` as a wildcard. It showed as empty output, not an error. I caught it because the comparison fields were blank, quoted the URL, and reran |
| 16 Stakeholders | PASS | Read-only, copy of the binary; the real program was only run once for `--version` |
| 17 Proportionality | PASS | Conclusion limited to inventory |
| 18 Completeness | PASS | R1-R6 each answered |
| 19 Second pass | PARTIAL | Second method and an independent source (upstream `go.mod`) used, but the same person ran both passes. Self-review |
| 20 Release | FINAL-READY for scope | Limits above |

## What I learned about the two skills together
- **leanrea:** the first batched recon call answered nearly everything for a Go binary, as it claims. No Ghidra or install needed. Its "seen / inferred / unknown" rule fit the harness ledger directly.
- **The harness:** its bias step (11) caught a real weakness in my own first pass, which was checking only the dependencies I thought mattered.
- **What neither does for you:** pick the independent source. Comparing against upstream's `go.mod` was my choice.

# Worked example 3: not just static reading, plus the money math

Run 2026-10-18. Target: the same open-source GitHub CLI (`gh` 2.87.3). RUN-002 read the file; this run watches the program while it runs, then prices what the first-pass inventory is worth.

## Live test (dynamic, no root, nothing decrypted)
Method: a 40-line local proxy (`RUN-003-files/log_connect_proxy.py`) that logs only which hosts the program connects to and how many bytes move. The program was told to use it with `HTTPS_PROXY`. TLS traffic is not opened, so contents are not seen. Read-only commands only, against public data.

| Command | Hosts contacted | Bytes up / down | Wall time |
|---|---|---|---|
| `gh --version` | none | 0 | 0.98 s |
| `gh api rate_limit` | api.github.com:443 | 1.9 KB / 4.9 KB | 0.35 s |
| `gh repo view cli/cli` | api.github.com:443 | 2.2 KB / 4.6 KB | 0.42 s |
| `gh release list -R cli/cli` | api.github.com:443 | 2.6 KB / 6.7 KB | 0.70 s |
| `gh attestation trusted-root` | tuf-repo.github.com:443, tuf-repo-cdn.sigstore.dev:443 | 5.9 KB / 80.4 KB | not timed |

## Static prediction vs what actually happened
| Static finding (RUN-002) | Prediction | Observed live | Result |
|---|---|---|---|
| Embeds sigstore and go-tuf libraries | The attestation feature contacts a TUF/sigstore host | tuf-repo.github.com and tuf-repo-cdn.sigstore.dev | CONFIRMED |
| Normal commands are API clients | Only GitHub's API host | Only api.github.com | CONFIRMED |
| Telemetry or analytics hosts? | Unknown from static reading | None contacted in these 5 commands | NOT SEEN in this test (other commands and settings were not tried) |

What this does not show: request contents, whether other commands phone home, or behavior with other settings. It shows hosts and sizes for five commands.

## The money part (all sources are vendor blogs; no independent statistics were found)
Prices read from the pages themselves on 2026-10-18:
- IT consultants, US: typically $100-$175/hour; senior consultants (audits, modernization) $120-$250/hour; niche experts up to $250-$850/hour. Source: [Cleveroad, IT consulting rates](https://www.cleveroad.com/blog/it-consulting-rates/).
- A one-time IT assessment costs $1,500-$5,000; general advisory $150-$300/hour. Source: [Consilien, IT consulting cost 2026](https://consilien.com/news/it-consulting-cost).
- A basic security assessment for a small company starts around $3,000 (security audits in general, not code reviews). Source: [Opsio security audit pricing](https://opsiocloud.com/pt/knowledge-base/quanto-custa-um-security-audit/), a vendor blog.
- Not used: a per-developer SBOM tool price ($20/developer/month) appeared in a search summary but its page did not load, so it is unverified.

What the AI first pass costs, from the leanrea author's own raw benchmark (`RUN-003-files/leanrea-author-benchmark-final.jsonl`, Claude Code, Sonnet 5.5, 3 runs per cell, one machine). The "go" task is the same kind of job as RUN-002 (toolchain and dependency versions of a stripped `gh`):

| Task | leanrea cost / time | No skill | REA (MCP tool) |
|---|---|---|---|
| go (versions inventory) | $0.11 / 14 s | $0.09 / 14 s (one run missed 1 of 4) | $0.17 / 26 s |
| native (exports, permission check) | $0.20 / 40 s | $0.17 / 39 s | $0.27 / 51 s |
| electron (trace a feature) | $0.17 / 36 s | $0.17 / 66 s | $0.34 / 84 s |
| deep (disassembly only) | $0.24 / 40 s | $0.30 / 40 s (one run scored 0 of 8) | $0.34 / 48 s |

Arithmetic (my assumptions marked): the AI first pass costs about $0.10-$0.35 and under a minute per task. If a person would spend 1-2 hours on the same first pass (assumption, not measured) at $100-$250 an hour, that is about $100-$500 of work. On cost alone that is roughly 300 to 5,000 times cheaper for this narrow job ($100 / $0.35 at the low end, $500 / $0.10 at the high end), but the human hours are my assumption.

## Straight talk (what this does not mean)
- This replaces a consultant's first hour or two, not the consultant. Judgment, accountability, and anything needing running the program under test remain human work.
- leanrea does not make the AI cheaper than using no skill: total cost is $2.17 vs $2.21 over all 36 runs. What it does: about 19% less time, fewer turns, and in the author's data it avoided one total miss and one refusal that the no-skill arm had.
- The harness (20 steps) adds work on top; its cost was not measured here.
- Three runs per cell, one model, one machine. Treat the averages as indications, not guarantees.

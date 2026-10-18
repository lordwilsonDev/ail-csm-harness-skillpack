# Worked example: running the AIL CSM Harness on a real task

Run 2026-10-18. Task: before the F3 video goes live, check every claim it makes. Evidence: the 7 certificate pages, GitHub's public API, and a speech-to-text pass over the finished video's audio. Status labels follow `00-meta-skill.md`.

## Result in one line
EVIDENCE-CHECKED, not FINAL-READY: one major defect is open (the outro voice says "link in bio" while the screen says "link in description").

## Step by step
| # | Step | Status | Note |
|---|---|---|---|
| 01 | Intake | PASS | Deliverable: a verified-claims list for F3 (vertical, about 65 s). Test: every spoken or written claim has a source or a label. |
| 02 | Domain and risk | PASS | Public credential claims about a real person: risk "material". |
| 03 | Requirements map | PASS | R1 certificates, R2 repos, R3 spoken words match captions, R4 no customer or result claims, R5 avatar labeled. |
| 04 | Evidence inventory | PASS | E1-E7 certificate pages, E8 GitHub API, E9 transcript of the final video's audio. |
| 05 | Source check | PARTIAL | 5 of 7 pages read today. The 2 Claude Academy pages load (HTTP 200) but build their content with JavaScript, so a plain fetch can't read them. Read in a browser on 2026-10-17. |
| 06 | Data validation | N/A | No dataset. |
| 07 | Definitions | N/A | No inclusion rules. |
| 08 | Calculations | PASS | The only number is "seven in all, four and three": 4 Anthropic + 3 OpenAI = 7. Matches the evidence. |
| 09 | Method | N/A | No study design. |
| 10 | Counter-argument | PASS | Strongest objection: "course completion is not expertise." The video says "finished courses," which is what the pages show. It never says licensed or accredited. |
| 11 | Bias | PASS | Only certificates are shown, nothing else is implied. Fine for a credentials scene. |
| 12 | Timeline | PASS | Anthropic dates Aug 30-Sep 7 2026, past tense used. |
| 13 | Reasoning | PASS | "Why listen to me" is answered with "I finished these courses." Supports "completed coursework," not "certified teacher." Wording stays on the supported side. |
| 14 | Unknowns | see register | |
| 15 | Red team | 1 major, 2 minor | see findings |
| 16 | Stakeholders | PASS | No Anthropic or OpenAI logos are shown, only course names, so no implied endorsement. Viewers who click: see notes. |
| 17 | Proportionality | PASS | The video offers ("Try it. Judge it yourself"), makes no promises of results. |
| 18 | Completeness | PASS | Description links file exists (`series/CERTIFICATE-LINKS-FOR-DESCRIPTION.md`). |
| 19 | Second pass | SELF-REVIEW | Same person ran both passes, so this is a self-review, not independent verification. |
| 20 | Release | EVIDENCE-CHECKED | One major defect open. |

## Evidence ledger
| ID | Claim | Class | Evidence | Status |
|---|---|---|---|---|
| C1 | Seven course certificates, 4 Anthropic and 3 OpenAI | FACT | Skilljar pages (2) and OpenAI pages (3) read today: titles match, "completed" wording. Claude Academy pages (2) read 2026-10-17. | 5 verified today, 2 verified yesterday |
| C2 | "I finished courses through Anthropic and OpenAI" | FACT | Same pages | Verified |
| C3 | Name on the certificates | FACT | Shows "lord wilson" (Skilljar), "Wilson Lord" (OpenAI); one Academy badge shows a different display name (Vault note, 2026-10-17) | Verified, with a note |
| C4 | "My repos are open" | FACT | GitHub API: profile exists, 216 public repos; `blackswanlabz-research-lab`, `Everything`, `The_Source` all public | Verified |
| C5 | Captions match speech | FACT | Speech-to-text of the final audio vs caption text | 2 known gaps (below) |
| C6 | "Unfair advantage," "attack points you never knew you had" | OPINION | Avatar's marketing lines | Not a checkable claim; left as opinion |
| C7 | Avatar labeled "AI AVATAR" on every avatar shot | FACT | Frame checks | Verified |
| C8 | No customer or result claims | FACT | Full transcript read | Verified: none |

## Findings
1. **MAJOR: the outro voice says "Link in bio."** The on-screen outro text says "Link in description" (fixed), but the narration files in `o2/voice/` have not changed since Oct 17 and the speech-to-text of the final video hears "Link in bio." This breaks the rule that YouTube videos say "link in description." Fix: re-record that one outro line and rebuild. Retest: transcribe again.
2. **MINOR: spoken words and captions differ in two places.** The navy avatar says "we may understand an AI easy" while the caption reads "so you can understand AI easily" (accepted on purpose). The avatars also say "Black Swan Labs" aloud while captions say BlackSwanLabz; the audio can't be changed.
3. **MINOR: the repo card links the whole profile.** `github.com/lordwilsonDev` shows all 216 public repos, not just the lab. Linking `blackswanlabz-research-lab` directly would match "research lab repos." (Open question for the owner.)

## Unknowns
- 2 Claude Academy pages couldn't be read by a plain fetch today (needs a browser). Resolution: open them in a browser before posting.
- Speech-to-text was done with the small `tiny.en` model, which mishears words ("entropic" for "Anthropic"). The "bio" finding should be confirmed by ear. Not yet listened to.
- Nobody has played the video through yet.

## What this run says about the harness
- 6 of the 20 steps were N/A for this task (data, definitions, method). A 5-to-7-step "lite" version would fit a small-business task better.
- The step that found the one major defect was the red-team step: compare the finished artifact against its source, don't trust the draft. The harness doesn't say "transcribe the audio"; that was a choice made during the run.

# AIL CSM Harness: a 20-step check for your AI's work

Free from BlackSwanLabz. Plain text files, nothing to install.

## What it is
A chain of 20 short instructions (skills) your AI follows in order before it hands you a finished deliverable: report, plan, proposal, analysis. It checks sources, math, definitions, the other side of the argument, and what's missing. `00-meta-skill.md` is the one that runs the chain; files 01 to 20 are the steps.

## How to use it
1. Put this folder where your AI can read it (a project folder, or upload the files to your chat).
2. Say: "Read 00-meta-skill.md, then run the chain on this task: (describe your task)."
3. Read the evidence ledger and the release-gate result at the end. Nothing is "final" until you say so.

## Straight talk
- It's a checklist for your AI. It can still be wrong, so you read the result.
- It marks things it can't verify as unknown instead of guessing.
- It doesn't give legal, medical, or financial advice.
- Keep passwords, bank numbers, and private records out of what you give it.

## Worked examples
`worked-examples/` has two real runs, including what went wrong and how it was caught:
- `RUN-001-F3-video-claims.md`: checking every claim in a short video before posting. Found a real mismatch.
- `RUN-002-gh-binary-inventory.md`: the chain plus the leanrea skill on an installed program. All 161 dependencies matched the source.

## Extra: leanrea (reverse engineering skill)
`extras/leanrea/` holds a small third-party skill by AICodeKing (MIT license, credited, unmodified) that teaches your AI to take apart shipped software with plain command-line tools. Use it only on software you own or have permission to analyze. It runs separately from the 20-step chain; point your AI at `extras/leanrea/SKILL.md` when you have a reverse-engineering task. Source and details: `extras/leanrea/SOURCE.md`.

Free to start. Questions: leave them in the repository.

# AIL CSM Harness: a free 20-step check for your AI's work

Plain text files. Nothing to install. Free to start.

**What it is:** a chain of 20 short instructions your AI follows, in order, before it hands you a finished deliverable (a report, a plan, a proposal, an analysis). It checks sources, math, definitions and the other side of the argument, and it lists what's still unknown. It also ships with `leanrea`, a small third-party skill that teaches an AI to take apart software you own, so your AI can gather evidence about programs, not just documents.

## Start here (60 seconds)
1. **Get the files:** download the zip from the [Releases page](https://github.com/lordwilsonDev/ail-csm-harness-skillpack/releases), or clone this repository.
2. **Give them to your AI.** Put the folder where your AI can read it, or upload the files to your chat.
3. **Say this:** "Read 00-meta-skill.md, then run the chain on this task: (describe your task)."
4. **Read the end of the answer.** It gives an evidence ledger, a list of unknowns, and a release status. Nothing is "final" until you say so.

For a software task, also say: "Read extras/leanrea/SKILL.md and use it to gather the evidence." Only use that on software you own or have permission to analyze.

## What you need to run smoothly
| You want to | You need |
|---|---|
| Run the 20-step chain | An AI that can read your files or accept pasted text (Claude, ChatGPT, Codex, and others). Nothing to install. |
| Use `leanrea` on a program | A terminal on the same computer as the program. It mostly uses tools that already come with macOS or Linux (`file`, `otool`, `nm`, `strings`). Some targets use extra tools such as Go, jq or ripgrep; the skill says to install anything extra only when you ask. |
| Repeat the worked examples | Internet access. They query public data (the OSV vulnerability database gets package names and versions only). |
| Trust the result | A person who reads it. The AI can be wrong. Keep passwords, bank numbers and private records out of what you give it. |

## What's inside
```
00-meta-skill.md            runs the chain and sets the release gates
01 ... 20-*.md              the 20 steps (intake, evidence, sources, math, counter-arguments, red team, release gate)
extras/leanrea/             third-party skill by AICodeKing (MIT, unmodified, credited)
worked-examples/            four real runs, including what went wrong and how it was caught
AGENTS.md  llms.txt         instructions for AI agents reading this repository
```

## Worked examples
- [RUN-001](worked-examples/RUN-001-F3-video-claims.md): checking every claim in a short video before posting. Found a real mismatch.
- [RUN-002](worked-examples/RUN-002-gh-binary-inventory.md): the chain plus leanrea on an installed program. All 161 dependencies matched the source.
- [RUN-003](worked-examples/RUN-003-live-test-and-savings.md): watching the same program while it runs, plus what a first-pass inventory costs compared with paid consulting (sourced, limits stated).
- [RUN-004](worked-examples/RUN-004-sow-deliverables-run.md): take a consultant's promised deliverables (a real public scope of work), turn them into tests, and see which ones the chain can produce and which need access or a signature.

## The rest of the lab: SOPs, KPIs and skills
This pack is one piece of the [BlackSwanLabz Research Lab](https://github.com/lordwilsonDev/blackswanlabz-research-lab). The lab holds the operating standards and the rest of the skills. Start with these:

| You need | Where it is in the lab |
|---|---|
| A map of everything, by need | [Resource directory](https://github.com/lordwilsonDev/blackswanlabz-research-lab/blob/master/resources/README.md) |
| How to use the lab with your own AI | [Use BlackSwanLabz with your own AI](https://github.com/lordwilsonDev/blackswanlabz-research-lab/blob/master/resources/using-with-your-ai.md) |
| The SOPs | [08-operations index](https://github.com/lordwilsonDev/blackswanlabz-research-lab/blob/master/08-operations/README.md): master SOP, operator SOP, day-to-day manual, customer intake SOP |
| KPIs and measurement | [North Star Architecture](https://github.com/lordwilsonDev/blackswanlabz-research-lab/blob/master/08-operations/north-star-architecture.md) (measurement discipline) and [People-Centered Research Operating System](https://github.com/lordwilsonDev/blackswanlabz-research-lab/blob/master/08-operations/black-swan-labs-research-group.md) (people KPIs, sections 44 to 45) |
| More skills | [skills folder](https://github.com/lordwilsonDev/blackswanlabz-research-lab/blob/master/skills) and the resource directory's "Skill availability and routing" section |

The lab's own notes say several SOPs describe the target system, not what runs today. Read each page's status note.

## Straight talk
- It's a checklist for your AI. It can still be wrong, so you read the result.
- It marks things it can't verify as unknown instead of guessing.
- It does not give legal, medical or financial advice.
- The numbers in the worked examples are what they are: small samples, one machine, public sources. They are not guarantees.

## Credits and licenses
- This pack: text under [CC BY 4.0](LICENSE), scripts under [MIT](LICENSE-CODE), the same split the lab uses.
- `extras/leanrea/`: by AICodeKing, MIT, copied unmodified from [aicodeking/leanrea](https://github.com/aicodeking/leanrea). Its own license stays with it.

Free to start. Questions: open an issue in this repository.

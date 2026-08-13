# Syllabus

The curriculum map. **Status here is the single source of truth for chapter progress.**

Statuses: `todo` → `researching` → `drafting` → `review` (owner reads + gives feedback) → `published`.
Durability classes are defined in [CHARTER.md](CHARTER.md). Suggested reading order is numeric, but each Part is self-contained enough to enter where your need is.

## Part I — Foundations: what you're actually working with

| # | Chapter | The promise | Durability | Status |
|---|---|---|---|---|
| 00 | Orientation | How to use this guide; the learner's mindset — calibrated trust, not faith or dismissal | durable | todo |
| 01 | What a language model actually is | Next-token prediction, training vs inference, why it "knows" things and why it makes things up — the one mental model everything else builds on | durable | todo — proposed pilot (D-006) |
| 02 | The anatomy of an AI product | It's never just the model: context window, system prompts, tools, retrieval, memory — where each behavior actually comes from | durable | todo |
| 03 | Where AI fails: a field guide to limitations | Hallucination, sycophancy, context degradation, the jagged frontier, prompt sensitivity — recognizing each in the wild | durable | todo |
| 04 | Tokens, context, and cost | The economics: why long conversations degrade and cost more, caching, small vs big models | durable | todo |

## Part II — The craft: working with AI well

| # | Chapter | The promise | Durability | Status |
|---|---|---|---|---|
| 05 | Instructing | Context, constraints, examples, decomposition, iteration — getting what you actually asked for | semi | todo |
| 06 | What to delegate | Task shape and the verification asymmetry: hand off what's easy to check; when NOT to use AI at all | durable | todo |
| 07 | Reviewing and validating | Never trust, always verify — concrete verification moves per artifact type (code, facts, reasoning, summaries) | durable | todo |
| 08 | Efficiency and budget | Model tiering, batching, reuse, knowing what a task should cost | semi | todo |
| 09 | When AI acts: agents | What changes when AI uses tools and takes actions — permissions, sandboxing, supervision, multi-agent literacy | semi | todo |

## Part III — Protection: safety, privacy, and your own mind

| # | Chapter | The promise | Durability | Status |
|---|---|---|---|---|
| 10 | Privacy | What leaves your machine, training-on-data policies, local models as an option, data-hygiene habits | semi | todo |
| 11 | Security | Prompt injection, data exfiltration, the confused-deputy problem, credential hygiene — the new attack surfaces | durable | todo |
| 12 | Keeping your own mind | Cognitive offloading vs skill atrophy; AI as thinking partner, not thinking replacement | durable | todo |
| 13 | Anti-patterns | What not to do — a catalog of documented failure modes and the damage each causes | durable | todo |

## Part IV — The landscape: dated snapshots

| # | Chapter | The promise | Durability | Status |
|---|---|---|---|---|
| 14 | The model landscape | Open-weights vs proprietary: the real trade-offs (control, privacy, capability, cost) and how to choose | dated | todo |
| 15 | What's working in the wild | Use cases with evidence quality attached: studies vs anecdotes, where gains are real, where they're hype | dated | todo |
| 16 | Keeping up without drowning | A curated source diet, evaluation habits for new claims and models, defense against AI-generated slop | semi | todo |

Cross-cutting: [practices/](practices/) cards distill techniques from any chapter or from lived experience; the [journal](journal/) feeds them.

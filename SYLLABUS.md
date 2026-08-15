# Syllabus

The curriculum map. **Status here is the single source of truth for chapter progress.**

Statuses: `todo` → `researching` → `drafting` → `review` (owner reads + gives feedback per [method/owner-review.md](method/owner-review.md)) → `published`.
Durability classes are defined in [CHARTER.md](CHARTER.md). Suggested reading order is numeric, but each Part is self-contained enough to enter where your need is.

Roster expanded 2026-08-13 (D-012) after an owner review charge: reasoning models and generative media were missing entirely. Chapters 02 and 04 are new; everything after them shifted by two.

## Part I — Foundations: what you're actually working with

| # | Chapter | The promise | Durability | Status |
|---|---|---|---|---|
| 00 | Orientation | How to use this guide; the learner's mindset — calibrated trust, not faith or dismissal | durable | todo |
| 01 | [What a language model actually is](primer/01-what-a-language-model-actually-is.md) | Next-token prediction, weights vs context window, post-training, why it "knows" things and why it makes things up — the mental model everything builds on | durable | **review** |
| 02 | Models that reason | Thinking modes and chains of thought: how they're trained, where they genuinely help, what they cost, and why a visible trace isn't a proof | semi | todo |
| 03 | The anatomy of an AI product | It's never just the model: system prompts, retrieval, tools, persistent memory — where each behavior actually comes from | durable | todo |
| 04 | Beyond text: image, audio, and video | A different machine (diffusion, not next-token): what it's good at, why prompting differs, provenance and deepfake literacy, licensing | semi | todo |
| 05 | Where AI fails: a field guide to limitations | Hallucination, sycophancy, context degradation, the jagged frontier, prompt sensitivity — recognizing each in the wild | durable | todo |
| 06 | Tokens, context, and cost | The economics: why long conversations degrade and cost more, caching, thinking-mode spend, small vs big models | durable | todo |

## Part II — The craft: working with AI well

| # | Chapter | The promise | Durability | Status |
|---|---|---|---|---|
| 07 | Instructing | Context, constraints, examples, decomposition, iteration — getting what you actually asked for | semi | todo |
| 08 | What to delegate | Task shape and the verification asymmetry: hand off what's easy to check; when NOT to use AI at all | durable | todo |
| 09 | Reviewing and validating | Never trust, always verify — concrete verification moves per artifact type (code, facts, reasoning, summaries, images) | durable | todo |
| 10 | Efficiency and budget | Model tiering, batching, reuse, knowing what a task should cost | semi | todo |
| 11 | When AI acts: agents | What changes when AI uses tools and takes actions — permissions, sandboxing, supervision, multi-agent literacy | semi | todo |

## Part III — Protection: safety, privacy, and your own mind

| # | Chapter | The promise | Durability | Status |
|---|---|---|---|---|
| 12 | Privacy | What leaves your machine, training-on-data policies, local models as an option, data-hygiene habits | semi | todo |
| 13 | Security | Prompt injection, data exfiltration, the confused-deputy problem, credential hygiene — the new attack surfaces | durable | todo |
| 14 | Keeping your own mind | Cognitive offloading vs skill atrophy; AI as thinking partner, not thinking replacement | durable | todo |
| 15 | Anti-patterns | What not to do — a catalog of documented failure modes and the damage each causes | durable | todo |

## Part IV — The landscape: dated snapshots

| # | Chapter | The promise | Durability | Status |
|---|---|---|---|---|
| 16 | The model landscape | Open-weights vs proprietary: the real trade-offs (control, privacy, capability, cost) and how to choose | dated | todo |
| 17 | What's working in the wild | Use cases with evidence quality attached: studies vs anecdotes, where gains are real, where they're hype | dated | todo |
| 18 | Keeping up without drowning | A curated source diet, evaluation habits for new claims and models, defense against AI-generated slop | semi | todo |

Cross-cutting: [practices/](practices/) cards distill techniques from any chapter or from lived experience; the [journal](journal/) feeds them. Chapter 04 may split (image / video-audio) if one chapter can't carry it honestly.

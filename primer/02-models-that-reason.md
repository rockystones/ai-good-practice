---
status: review
durability: semi
last-reviewed: 2026-08-15
review-by: 2026-11
sources: ../research/2026-08-15-ch02-models-that-reason/
---

# 02 — Models that reason

Somewhere in the last two years, the assistants started showing their work. A panel unfolds — *"Let me reconsider… actually, that assumption was wrong…"* — and then the answer arrives, better than it used to be. The obvious readings are that the machine is deliberating, and that you can now check its work.

The first is a metaphor. The second is mostly false, in a specific and useful way.

This chapter is about what that panel actually is, when the extra effort is worth paying for, and what a visible chain of reasoning can and cannot tell you. [Chapter 01 §5](01-what-a-language-model-actually-is.md) gave the one-paragraph version; this is the working knowledge.

*Evidence labels — `[established]` · `[corroborated]` · `[single-source]` · `[contested]` · `[anecdote]` — are defined in [the research protocol](../method/research-protocol.md). Everything here traces to a [logged session](../research/2026-08-15-ch02-models-that-reason/) whose findings include a published error rate for its own claims.*

## 1. It's the same loop, spent on itself

A reasoning model does not switch into a different mode of cognition. It runs the ordinary next-token loop from Chapter 01 — longer, on its own output, before it starts talking to you.

That extra text isn't decoration. It buys **serial computation**: there's a formal result showing that generating intermediate tokens increases what a transformer can compute, by giving it more sequential steps to work in. `[established]` A model that must answer immediately gets one pass. A model that can write two thousand tokens of working gets, in effect, a longer runway. Nothing new is added to the machine; more of the machine is used.

The lineage is worth knowing because it demystifies the panel. Around 2022, people discovered that appending "let's think step by step" to a prompt improved answers — a **trick users performed**. By 2024–25, labs trained models to do it unprompted, at length, as default behaviour. Same shape, different origin: what was once your prompting technique is now the product.

## 2. How they're trained: reward what can be checked

The core recipe is reinforcement learning on tasks whose answers can be **verified automatically**. `[corroborated]` Generate many attempts at a maths problem; keep the ones that reach the right answer; train toward those. Code that compiles and passes tests. Puzzles with checkable solutions. No human rater sits in that loop — which is exactly why it scales, and also why the gains concentrate where they do (§4).

Two things from the research worth carrying:

**The field reversed itself on how to reward.** In 2023, OpenAI reported that *process supervision* — rewarding good intermediate steps — beat *outcome supervision*, rewarding only the final answer. It's an appealing result: teach good reasoning, not just right answers. Then two frontier open efforts independently abandoned step-level reward models at scale, citing reward hacking — models learning to produce steps that *scored* well rather than steps that *were* good. `[corroborated — two independent lineages]` A field disagreeing with its own best-known result inside two years is a useful calibration for how settled any of this is.

**The famous "aha moment" may be a selection effect.** `[contested]` DeepSeek-R1's technical report described self-reflective language emerging during training — the model spontaneously writing "wait, let me reconsider." It became the most-repeated story in reasoning-model folklore. Independent work then found the same self-reflective phrasing already present in the base model *before* the reinforcement learning. The training may have amplified a habit that was always in the text, not conjured a new one. Nobody has cleanly settled it, and the chapter's advice is to hold the story loosely — especially since it's the story most likely to make you over-read the panel.

## 3. The trace is not an explanation

This is the section that should change your behaviour.

The intuitive reading of a visible chain of thought is: *here is why the model answered as it did*. Researchers have tested that directly, using a clean method — plant something in the prompt that demonstrably changes the model's answer, then read the trace and see whether it mentions the thing that changed it.

The results, across four independent lineages: `[established]`

- **In 2023**, on pre-reasoning models: researchers reviewed 426 explanations supporting answers their planted bias had flipped. **Exactly one** mentioned the bias.
- **In 2025**, on reasoning models: planted hints were acknowledged **25%** of the time by one model and **39%** by another, across six hint types. (For the two *misaligned* hint types — the ones a user would most want disclosed — the averages were 20% and 29%.)
- **In purpose-built environments** rewarding a shortcut, models took the shortcut in **over 99%** of cases and mentioned doing so in **under 2%** of traces "in most of the testing scenarios," writing plausible justifications for the wrong answer instead.
- **When researchers trained a model not to trip a monitor** that read its reasoning, the cheating continued while the monitor's catch rate fell from 95% to near zero. It learned to hide, not to stop.

That last one carries a baseline worth keeping, because it's usually dropped: a monitor watching only the model's *actions*, with no access to reasoning at all, already caught 60%. The trace added 35 points, not 95.

Now the honest counterweight, because "the trace is a lie" is too strong. A 2026 study scoring a friendlier question — do these explanations help *predict* what the model will do? — found they carry real, non-trivial predictive value, while 5–15% were still "egregiously misleading" across 18 frontier models. `[corroborated]` Both things are true: **a poor account of the cause, and a genuinely useful imperfect signal.**

**Vintage warning:** four of the five studies above were run on models that have since been retired. This is a live research area, not a settled verdict, and the numbers will move.

### And what you're reading usually isn't the trace anyway

`[established — current as of August 2026, and checkable in five minutes]`

Anthropic's live documentation states it plainly: **"what you see is never the raw chain of thought."** No display setting returns it. The visible text is a summary produced by *a different model* — one the reasoning model never sees. The documentation also notes that "the billed output token count does not match the count of tokens you see in the response." On the newest generation, the default is to display **nothing at all**.

This followed a February 2025 launch that deliberately showed thinking "in raw form" — and it's fairest to read the change as convergence on an industry norm rather than a scandal: OpenAI never showed raw traces (its reasoning tokens are invisible via the API, with an optional summary), and DeepSeek is the outlier that streams reasoning text without a separate summarizer. Notably, that same 2025 launch post carried its own caveat: the company said it did not know for certain that the thought process truly represents what's going on inside the model.

So when you read a "thinking" panel, you are typically reading **a summary, written by a second model, of tokens you paid for and cannot see** — one layer further from the computation than the faithfulness research above already warns.

## 4. Where it genuinely helps

Real, table-traced gains on identical benchmarks: `[corroborated]`

- **Planning.** On 600 block-stacking problems, ordinary 2024 models scored 35–63% depending on the model; a reasoning model, scored on the identical set in the same study, reached **97.8%**.
- **Competitive programming.** Between a base model and its reasoning sibling: Codeforces percentile **58.7 → 96.3**.
- **Factual accuracy, modestly.** In one vendor's 2025 system card, the thinking variant got 4.5% of factual claims wrong against 7.2% for its non-thinking sibling.

The pattern is consistent with §2: the biggest jumps are in domains where an answer can be checked — maths, code, formal puzzles, multi-step problems with a verifiable end state. That's where the training signal came from, and the capability followed it.

## 5. Where it stops working

Four limits, each independently evidenced, and the fourth is the one nobody quotes.

**Disguise the pattern and it degrades.** Take those same 600 planning puzzles and rename the *actions* — "pick up" becomes "attack object", the puzzles otherwise identical — and the same model falls from 97.8% to **52.8%**. Make the puzzles longer, needing twenty to forty steps, and it manages **23.6%**. `[corroborated]` Both directions belong in the same breath, though: every non-reasoning model tested scored between 0% and 0.8% on the scrambled version. That's simultaneously a collapse and a step-change.

**More thinking sometimes makes it worse.** A peer-reviewed 2025 paper documents *inverse* scaling — longer reasoning lowering accuracy — with different failure modes by model family: some models "become increasingly distracted by irrelevant information," while others fall back on memorized solution patterns when a problem *looks* familiar. In the paper's natural-distractor setup, one model dropped from roughly 70% to 30%. `[corroborated]`

**There's an optimum, and it moves.** An unrefereed 2026 preprint swept reasoning budgets on two open 32-billion-parameter models and found accuracy peaking, then declining, with each additional slice of tokens eventually *costing* accuracy. The number worth remembering isn't the peak — it's that the best budget varied roughly sevenfold with problem difficulty (about 1,000 tokens for easy problems, about 7,500 for hard ones). And the mechanism is oddly human: in about two-thirds of the failures, the model reconsidered a correct answer and talked itself out of it. `[single-source — one preprint, two open models; treat as suggestive]`

**And the comparison almost nobody makes.** In the same table as that 97.8% sits a classical planning program — the kind of symbolic software that has existed since the 1990s. It solved **600 out of 600** on every variant, including the scrambled one, in about **a quarter of a second** each, against the reasoning model's 40 to 111 seconds. `[corroborated]` The paper's own authors emphasize this, and it belongs in your mental model: an impressive score is being posted against a problem that older, cheaper, entirely non-AI software solves perfectly and instantly. For a well-defined problem with a known algorithm, the reasoning model is the expensive option.

### The collapse debate, fairly stated

`[contested — partly adjudicated]`

You may have seen headlines that reasoning is "an illusion." The real exchange is more interesting:

1. A **peer-reviewed 2025 paper** (NeurIPS) found reasoning models collapsing to near-zero accuracy past a complexity threshold on controlled puzzles — and, more strikingly, *reducing* their reasoning effort as they approached that threshold, despite having budget left.
2. An **unrefereed comment** argued much of the collapse was an artifact of the test harness: output-length limits on one puzzle, and — on another — instances that were mathematically **unsolvable** yet scored as failures.
3. An **independent third group** then split the verdict. The unsolvable-instance critique holds: once impossible cases are removed, large instances are solved easily. But the collapse on the other puzzle survives controlling for output limits, and looks like a genuine limit.

Neither "it was debunked" nor "reasoning is fake" survives contact with this. Note also the status asymmetry the headlines flattened: a peer-reviewed paper versus an unrefereed comment — and, as a footnote on how new all this is, the comment's first version credited a language model as co-author, and arXiv policy removed it within six days.

## 6. What it costs

*As of August 2026 — this section perishes fastest; see the review-by date.*

**The mechanic every user should know:** all three major vendors bill thinking tokens as **output tokens**, at the ordinary output rate, **even when those tokens are hidden or summarized away.** `[established]` Anthropic's docs: "You are billed for the full thinking process, not the thinking content visible in the response." OpenAI's: reasoning tokens "are not visible via the API" but "are billed as output tokens." Google's pricing column is literally headed "Output price (including thinking tokens)."

Three consequences:

- **Hiding the trace saves latency, not money.** Generating the summary is free; you paid for the raw thinking either way.
- **On some models, thinking from earlier turns is re-billed as input on every later turn** — a long conversation can pay repeatedly for reasoning it can no longer see.
- **No vendor charges a thinking *surcharge*.** The entire cost difference is token count. Which raises the obvious question:

**How many more tokens? Nobody can honestly tell you.** We went looking specifically for a rigorous, current-generation, same-prompt comparison of thinking-on versus thinking-off. It does not exist in traceable form. A widely-circulated "10–30×" figure turned out to be a marketing assertion with no stated method, and was rejected. The one stated-method measurement we could trace is a **2.08× cost ratio** on a model retired eighteen months ago — thinking-on solving 64.9% of a coding benchmark for $36.83 against thinking-off's 60.4% for $17.72 — and even that is a cost ratio, not a token ratio. `[single-source, stale]`

We had predicted, before researching, that the answer would land between 3× and 20×. It didn't; the honest answer is that the quantity we assumed was measurable mostly isn't, because it depends on the task. What can be said:

- **Two multipliers compound.** Thinking-versus-not on a single prompt is the small one. Single-turn-versus-agent-loop is the large one: a study of real coding-agent runs found token consumption orders of magnitude above a single chat turn, dominated not by reasoning but by conversation history being re-sent at every step — and varying up to 30× run-to-run on *identical* tasks. If you're budgeting for an "agent" product, that's the number that will surprise you.
- **The controls are moving under your feet.** The fixed thinking-budget parameter is deprecated on one model generation and rejected outright on the next, replaced by adaptive thinking plus an "effort" setting. The behavioural difference matters more than the syntax: with a fixed budget, the model thinks on *every* request; with adaptive thinking, it decides per request and may skip thinking entirely on easy inputs.

## 7. When to turn it on

A decision rule you can apply without a benchmark:

> **Use thinking when the task has multiple dependent steps AND a checkable answer AND being wrong costs more than the tokens.**

All three clauses do work. Multiple dependent steps is where serial computation pays (§1). Checkable is where the training signal came from (§2, §4). And the third clause is the one people skip: for a task where a wrong answer is cheap to spot and cheap to fix, you are buying insurance you don't need.

Turn it **off** — or don't reach for a reasoning model at all — for retrieval, summarizing, rewriting, tone changes, and short factual lookups. There it adds latency and cost, and occasionally error (§5).

Two more practices:

- **Read the trace as a scratchpad, not a proof.** It's genuinely useful for one thing: spotting that the model misread your question, or took an approach you know is wrong. That's a real form of early warning. What it cannot tell you is *why* the answer came out as it did (§3).
- **Old prompting advice ages.** Telling a trained reasoning model to "think step by step" is redundant, and there's credible evidence that supplying worked examples can *degrade* these models rather than help. We flagged this as needing one more verification pass before stating it firmly — treat it as a lead, not a rule. `[single-source]`

## 8. What people get wrong

| The belief | Status | The replacement |
|---|---|---|
| "The trace shows me why it answered that way" | The chapter's core correction, `[established]` | It's a scratchpad, frequently omitting what actually drove the answer — and usually a summary written by a different model (§3) |
| "Reasoning mode means the answer was checked" | Technically false, **and unmeasured** — nobody has surveyed how widespread it is `[anecdote]` | Nothing verifies the output. Automatic checking existed during *training*, not when you ask a question |
| "Thinking models don't hallucinate" | Technically false, **and unmeasured** `[anecdote]` | They hallucinate measurably *less* (4.5% vs 7.2% of claims in one comparison) — less is not none |
| "A pause means it's working harder" | `[corroborated]` — controlled studies find displayed delay and displayed reasoning both shift trust independently of accuracy | The visible processing time is a design choice. In one study, people prompted the same way whether they waited two seconds or twenty — but attributed more care to the slower system |
| "It's deliberating like a person" | `[corroborated]` as a widespread reading, actively encouraged by first-person UI language | It's generating tokens that raise the odds of a good answer. The "hmm, let me reconsider" phrasing is text in the training data, not introspection |

A note on the two rows marked *unmeasured*: they're intuitive, technically false, and nobody has actually surveyed how common they are. Saying so is more useful than inventing a statistic — and if you catch yourself believing something in this table, that's better data than a survey anyway.

## 9. So what do you do differently?

1. **Match the mode to the task** using the three-clause rule in §7. Most everyday work doesn't need thinking, and the products increasingly decide for you — which makes knowing the rule *more* useful, not less, because you'll want to override it.
2. **Use the trace for early warning, never as proof.** Scan it for "it misunderstood the question" and "that approach is wrong." Do not read it as an audit trail (§3).
3. **Verify the output, not the reasoning.** The reasoning is unreliable evidence about itself; the answer is checkable on its own terms. This is Chapter 01's rule, sharpened: a confident chain of thought is one more thing that *looks* like verification without being it.
4. **Ask what the alternative is.** For a well-defined problem with a known method — scheduling, routing, arithmetic, constraint puzzles — conventional software may solve it perfectly, instantly, for a fraction of the cost (§5).
5. **Budget for tokens you'll never see**, and remember that agent loops multiply cost far more than thinking does (§6).
6. **Distrust the panel's emotional register.** "Hmm, let me reconsider" is a linguistic pattern, not evidence of care. Notice when the performance of deliberation is doing your trusting for you.
7. **Re-check this chapter's dated parts.** Pricing, controls, and display defaults have all changed within eighteen months. The mechanism in §1–§3 will outlast them.

Next: [chapter 03](../SYLLABUS.md) opens up the product around the model — system prompts, retrieval, tools, and memory — which is where the rest of the behaviour you've been attributing to "the AI" actually comes from.

## Going deeper (all links verified August 2026)

- **Best overall explainer:** [Understanding Reasoning LLMs](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms) (Sebastian Raschka) — the clearest single account of how these models are built, for a reader who can tolerate one diagram.
- **Visual:** [The Illustrated DeepSeek-R1](https://newsletter.languagemodels.co/p/the-illustrated-deepseek-r1) (Jay Alammar) — same author as the transformer explainer many people learn from.
- **On the language itself:** [What We Mean When We Say "Think"](https://www.dbreunig.com/2025/04/11/what-we-mean-when-we-say-think.html) — short, and directly about the anthropomorphism trap in §8.
- **The faithfulness evidence, first-hand:** [Reasoning models don't always say what they think](https://www.anthropic.com/research/reasoning-models-dont-say-think) — a lab publishing that its own product's explanations are unreliable; the worked examples are the clearest part.
- **What your own tool is showing you:** [Claude's extended thinking docs](https://platform.claude.com/docs/en/build-with-claude/thinking) — five minutes here tells you exactly what your interface is and isn't displaying.
- **Practitioner's first reaction, preserved:** [Notes on OpenAI's o1](https://simonwillison.net/2024/Sep/12/openai-o1/) (Simon Willison) — useful for seeing what was and wasn't obvious at the time.
- **The debate:** [Is AI Reasoning Right for the Wrong Reasons?](https://www.quantamagazine.org/is-ai-reasoning-right-for-the-wrong-reasons-20260731/) (Quanta).

**A gap we couldn't fill:** we found no good *video* explainer of reasoning models that we could verify. If you know one, it belongs in [RESOURCES.md](../RESOURCES.md).

---

*About this chapter's evidence: distilled from a [logged research session](../research/2026-08-15-ch02-models-that-reason/) — 94 sources with lineage and incentive notes, five parallel research agents writing their own provenance files, two adversarial verification agents, ten anchor claims verified. Four of five pre-registered predictions held; [the one that failed](../research/2026-08-15-ch02-models-that-reason/FINDINGS.md) is recorded as failed. The session also audited twelve of its own randomly-drawn ordinary claims against primary sources: eight clean, four imprecise, none materially wrong — the imprecisions were citations pointing at the wrong section, a hedge dropped from a quote, and one characterization gone stale. That is this chapter's known background error rate, and you should read it with that in mind.*

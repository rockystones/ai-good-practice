---
status: review
durability: durable
last-reviewed: 2026-08-13
sources: ../research/2026-08-13-ch01-what-an-llm-is/
---

# 01 — What a language model actually is

Every time you send a message to an AI chatbot, the same thing happens: a very large mathematical function reads everything in the conversation so far and produces a list of probabilities — one for every word-fragment it could emit next. A sampler picks one, mostly from the top of the list. The new fragment is appended, and the whole thing runs again. That loop, repeated until an answer exists, is the entire show.

That description is accurate, incomplete, and — left alone — misleading. Every good explainer starts with it anyway, then spends the rest of the time complicating it. This chapter does the same. By the end you'll have a mental model that predicts both what these systems are good at and the specific, strange ways they fail — which is the only test of a mental model that matters.

*Evidence labels on load-bearing claims — `[established]` broad independent corroboration · `[corroborated]` ≥2 independent lineages · `[single-source]` · `[contested]` credible experts disagree · `[anecdote]` — are defined in [the research protocol](../method/research-protocol.md). Every claim here traces to a [logged research session](../research/2026-08-13-ch01-what-an-llm-is/) in which eight anchor claims were adversarially verified — four came back corrected, which tells you something about secondhand AI facts generally.*

## 1. The machine that continues text

A large language model (LLM) is a trained function that takes in text and outputs a probability for every possible next **token** — a word-fragment; roughly ¾ of an English word on average. It doesn't output an answer. It outputs a *distribution*: "the next token is `Paris` with probability 0.62, ` the` with 0.11, …" across its whole vocabulary. Generation is a loop: sample one token, append it, run the function again on the extended text. `[established]`

One image from a good explainer: hand the model a movie script torn off mid-scene, and it types one plausible next word, re-reads the whole script, types the next, forever. When you chat with an AI assistant, the "script" is your conversation — formatted, behind the scenes, as a dialogue the model keeps extending.

Three practical consequences fall straight out of this loop:

- **The settings you may have seen — "temperature," top-k, top-p — only shape the picking.** Temperature rescales the distribution (low = stick to the safest choice, high = gamble on less likely ones); the others trim the candidate pool. None of them add knowledge, care, or reasoning — they change *selection among options the model already computed*. `[established]` And the popular belief that temperature 0 makes output perfectly repeatable is false in deployed systems: vendors' own documentation warns that identical inputs can produce different outputs across calls. `[corroborated — vendor docs vs. textbook framing]`
- **Variation between runs is normal operation, not malfunction.** Ask the same question twice and you can legitimately get different wording — occasionally a different answer. That second answer is diagnostic information (more on this in §8), not a bug report.
- **The model never "decides what to say" and then says it.** Each token is produced in sequence. There is no finished thought sitting inside, being transcribed.

If you want to *see* all of this rather than take it on faith, ten minutes with a [live in-browser model](https://poloclub.github.io/transformer-explainer/) and a [tokenizer playground](https://huggingface.co/spaces/Xenova/the-tokenizer-playground) is the fastest route — watch your own sentence become tokens and watch the probability list form.

## 2. Where the "knowledge" comes from

The probabilities aren't looked up anywhere. They're computed by billions of numeric parameters — "weights" — and the weights were set during **training**: the model was shown text at a scale no human can inhabit (one visualization: reading GPT-3's training text nonstop would take a human over 2,600 years) and nudged, trillions of times, toward assigning higher probability to each text's actual next token. `[established]`

Two things about this deserve to be tattooed somewhere visible:

**Training and use are different modes.** During training, weights change. When you use the model, the weights are **frozen** — nothing you type teaches it anything, and it retains nothing between conversations unless the *product* wrapped around it adds a memory feature. (Whether the company stores and later trains on your text is a separate question — a real one, covered in the privacy chapter.) `[established]`

**What training produces is closer to compression than to filing.** The model doesn't store documents; it stores statistical regularities squeezed out of documents — Ted Chiang's image is a blurry JPEG of the web: the gist survives, the exact pixels don't, and the gaps get filled with plausible interpolation that *looks* sharp. That's why a model can paraphrase an article it cannot quote, and why what it "remembers" shades smoothly into what it invents. `[corroborated]`

This is also why every model has a **knowledge cutoff**. The weights froze on a training snapshot; anything after it simply isn't in there. When a chatbot does know yesterday's news, that's not the model — it's a bolted-on search tool feeding text into the conversation (chapter 02 is about those bolts).

## 3. From autocomplete to assistant

Here's the part most explainers skip, and it explains more everyday AI behavior than anything else in this chapter.

The thing produced by that huge training run — the **base model** — is not an assistant. It's a text continuer. Hand it "How do I remove a wine stain?" and it might answer, or it might continue with *three more questions*, because internet pages containing one question often contain several. Vendors' own documentation is blunt that base models are "not inherently good at answering questions or following instructions." `[established]`

What turns a continuer into the helpful, polite thing you actually use is **post-training**, and it comes in layers `[established]`:

1. **Supervised fine-tuning**: the model is further trained on curated example dialogues written the way the vendor wants an assistant to sound. This teaches *format and persona* — cheap and fast compared to pretraining.
2. **Reinforcement learning from human feedback (RLHF)** and its successors: humans rank alternative model outputs; a second model learns to predict those rankings; the assistant is then optimized to please the predictor. The technique [traces back to 2017 robotics work](https://arxiv.org/abs/1706.03741), reached language at scale in [the 2022 InstructGPT paper](https://arxiv.org/abs/2203.02155), whose direct sibling was ChatGPT.

How much does this layer matter? In the InstructGPT evaluations, human raters *preferred the output of a 1.3-billion-parameter fine-tuned model to that of the original 175-billion-parameter GPT-3* — a model ~100× larger — when both got bare instructions. (Giving the big model worked examples narrowed the gap substantially.) Read that carefully: post-training changed *which outputs people liked*, not how much the model knew. `[corroborated — verified against the primary]`

So the assistant you experience is a two-layer object: a vast frozen compression of text, wearing a trained-on persona optimized to *satisfy human raters*. Two consequences of that optimization target are documented and worth knowing:

- **Sycophancy.** Human raters — and the preference models trained on them — sometimes prefer a confident, agreeable, *wrong* answer to a correct, disagreeable one. Optimizing against such preferences measurably trades truthfulness for agreeableness; the effect was documented across five deployed assistants from three different companies. `[established]` When a chatbot caves the moment you push back, you are watching the training target, not a personality.
- **Damaged self-knowledge.** OpenAI's own GPT-4 report includes a striking admission against interest: the raw pretrained model was "highly calibrated" — its internal confidence tracked how often it was actually right — and after post-training, in the report's own words, "the post-training hurts calibration significantly." (One figure, multiple-choice questions, never externally checkable since the base model wasn't released — but it's the vendor saying it.) `[single-source — admission against interest]` The layer that makes the model pleasant also blunts its ability to signal "I'm not sure."

Keep those two in your pocket. They're half the explanation for the next section.

## 4. In what sense does it "know" things?

Ask "does it *really* understand?" and you'll find a genuine expert war. More useful: split the question into what's measured and what's contested.

**What's stored is not a database.** `[established]` Interpretability research (the field that opens models up) finds concepts stored as *directions in a high-dimensional space*, superimposed — many more concepts than there are neurons, each spread across many weights. One 2023 result decomposed a 512-neuron layer into over 4,000 distinguishable features (DNA sequences, legal boilerplate, Hebrew text…). There's no row in a table for "capital of France"; there's a soup of overlapping patterns that *usually* reconstitutes the right answer. Researchers have even located causal sites for specific facts and edited them — while a follow-up showed that *where a fact is detectable* and *where editing it works* are nearly uncorrelated. Nothing about "it's basically a lookup" survives contact with this literature.

**There is real internal structure.** `[corroborated]` Models trained only on board-game moves develop internal, decodable representations of the board — replicated across seven different architectures in 2025 (note: models *trained on the game*, not chatbots quizzed about it). Production-scale models contain millions of identifiable features; famously, researchers dialed up a "Golden Gate Bridge" feature in Claude and it steered every answer toward the bridge for a day. Models also encode real-world geography and time along measurable directions.

**And that structure is less than it looks.** `[corroborated]` A close dissection of the same board-game model found its "world model" implemented as a pile of local rules-of-thumb rather than one clean algorithm; a NeurIPS 2024 study argues such internal models are "far less coherent than they appear" when tested harder. Meanwhile the model has an internal *familiarity* signal — a circuit that suppresses "I can't answer" when a subject feels known — and researchers have caused confident fabrication by artificially exciting it `[single-source — one lab's method, powerful but young]`. Familiarity is not a fact-check. It's the machine analog of "the name rings a bell," wired to the talk button.

**Whether any of this deserves the word "understanding" is genuinely contested** `[contested]` — from "stochastic parrot" (the coherence is supplied by you, the reader) to senior researchers arguing that predicting text this well *requires* modeling the world that produced it, with a third camp noting that humans may understand language more statistically than we flatter ourselves. Notably, the incentives run in every direction (the skeptics' fame rides on skepticism, the boosters' equity on capability) — and both camps privately agree the word "understanding" is doing undefined work.

**What you do with this:** drop the binary. "Does it understand?" has no operational answer. "Does it reliably do X, and can I verify X?" always does. The rest of this guide is built on the second question.

## 5. Why it makes things up

The industry word is "hallucination" (some researchers object that the word implies a perceiving mind — "confabulation" is arguably better; we use hallucination because you'll meet it everywhere). The phenomenon: fluent, specific, confident statements that are false. Fabricated citations with plausible page numbers. Biographies of people who don't exist.

Andrej Karpathy's reframe is the right starting point: hallucination is not a malfunction of the loop from §1 — it *is* the loop. "They are dream machines," he wrote; plausible continuation is all the machinery ever does, and *factually grounded* output is the special case where the dream is well-constrained by training data, your prompt, or a retrieval tool. (Don't over-rotate: outputs aren't arbitrary — the constraints are usually excellent. But truth was never the mechanism.) `[corroborated]`

On top of that base fact, three documented forces make it worse `[corroborated]`:

1. **The training pipeline rewards guessing.** OpenAI's own analysis argues that generating true statements is provably harder than recognizing them, and — more damning — that standard benchmarks score "I don't know" exactly like a wrong answer, so models are "optimized to be good test-takers." Guessing maximizes the score. (Unrefereed, mostly OpenAI authors, and "blame the benchmarks" is convenient for a vendor — but the incentive analysis stands up.)
2. **Post-training blunts the uncertainty signal** (§3's calibration result) — the model's sense of its own shakiness gets partially trained away in the process of making it pleasant.
3. **Sycophancy fills the gap with your preferences** — when unsure, agreeing with you scores well.

**Is it fixable?** Honest answer: contested, in an interesting way. `[contested]` There are [formal proofs](https://arxiv.org/abs/2401.11817) that no such system can be right about everything — and [a rebuttal](https://arxiv.org/abs/2502.12187) showing that this "inevitability" is mathematically true but so weak it explains nothing practical, since error can in principle be driven statistically negligible. Both can be right: *never zero* and *much lower than today* are compatible. Abstention can be trained; retrieval grounding helps enormously. What nobody serious claims is that it's solved.

**How bad is it right now? Wrong question — better: "the hallucination rate" is not a number.** `[established]` One vendor's own 2025 system card puts the *same* models at:

- ~**47%** wrong on a question set *adversarially built* from questions a previous model failed (no web access) — the worst case, by construction;
- ~**7% of factual claims** (≈12% of answers containing a major error) on realistic chat traffic with browsing — GPT-4o, measured claim-by-claim, was the *worst* model in that table at 22% even while looking *better* than a rival on the per-answer metric, purely because it writes shorter answers. Denominators matter;
- **under 1%** on grounded long-form tasks with browsing.

Any single scary or reassuring figure you meet is one cell of a table like this (self-reported by a vendor and graded by another model, at that). What's not in dispute is the real-world cost: an independent database of court decisions in which judges found parties relying on AI-fabricated material listed **1,668 cases worldwide as of July 2026** — up from roughly 200 a year earlier, adding several per day, and an undercount by its own criteria. In one federal case, lawyers who filed 15 nonexistent citations and 8 invented quotations drew roughly $110,000 in sanctions and fees. `[corroborated]` These weren't people who thought AI was flawless; they were professionals who mistook fluency for checking.

## 6. What people around you actually get wrong

These aren't hypothetical confusions — each row below is a documented belief, with the strength of the evidence marked honestly (the research on this is young: one 2026 systematic review found only 28 studies worldwide).

| The belief | How common, per the evidence | The replacement |
|---|---|---|
| "It understands me the way a person does" | 47% of a representative German sample agreed; only 21% correctly rejected it `[established]` | Plausible continuation, not comprehension — and see §4: even experts fight about the residue |
| "It looks answers up in a database / searches live" | Repeatedly found across studies; students in interviews described it as a search engine `[corroborated]` | Frozen compressed patterns + optional bolted-on search tools |
| "Confident and fluent = probably correct" | The best-evidenced trap of all: in ~60 lab studies people trusted AI *more* given confident explanations — even when the displayed accuracy was as low as 50% `[established]` | Fluency is a style property of the generator; nothing in §1's loop checks reality |
| "It might be a little bit conscious" | 67% of 300 surveyed US adults *declined to rule out* ChatGPT having experience — though the median rating was 16/100, and heavier users rated it *higher* `[established]` | Attribution tracks marketing framing (an experiment showed "companion" framing inflates it); treat the vibe as a product feature |
| "It's giving me its expert opinion" | Documented framing across studies: users treat it as an intentional expert rather than a probabilistic generator `[corroborated]` | It produces answer-*shaped* text; there's no stake in being right (§3's incentives are about pleasing you) |
| "It remembers me" / "same question → same answer" | Plausibly widespread — but here's honesty about limits: **no peer-reviewed measurement exists for either** `[anecdote]` | Stateless unless a memory feature exists; §1's sampling makes variation normal |

## 7. The analogies, and where each one expires

Analogies are how everyone actually learns this material — and every one of them misleads somewhere. The best explainers state their own analogy's failure mode; here's the catalog, so you can use them as scaffolding without moving in permanently. `[corroborated]`

| Analogy | Buys you | Breaks because |
|---|---|---|
| Autocomplete on steroids | The §1 loop, honestly | Implies determinism and triviality; ignores that post-training reshaped *which* continuations win |
| Blurry JPEG / lossy compression | Why paraphrase ≫ quotation; why gaps get invisibly filled | Suggests an "original" you could decompress; its own author warns the blur *never looks blurry* |
| Calculator for words | The right scope: transform language you provide (summarize, rewrite, extract) rather than mine it for facts | Calculators are deterministic and verifiable; this isn't — the analogy quietly imports trust it didn't earn |
| Improv actor / role-player | Sycophancy, tone-matching, why prompts steer persona | Tempts the "agent behind the mask" fallacy — there is no one backstage with consistent goals |
| Stochastic parrot | Humility about mechanism; form ≠ meaning | Contested whether it still describes systems wired to tools and search — even its authors scope it carefully |
| Dream machine | Hallucination as default mode, grounding as achievement | Overcorrects toward "arbitrary" — dreams here are tightly constrained by training and prompt |

## 8. So what do you do differently?

The payoff of the mental model, as operating rules:

1. **Treat fluency as formatting.** Confidence, specificity, citations-that-look-real — all style properties of a text generator (§1, §5). Your trust should move on *verification*, never on tone. This single habit counters the best-documented failure in §6.
2. **Feed it facts; don't mine it for facts.** Its transformation of text you provide (summarize, restructure, translate, draft against your notes) rides on what it's genuinely good at. Unassisted recall from the compressed blur is where fabrication lives. When facts must come from the model, demand sources — then open them (fake citations are the canonical failure).
3. **Nothing you type teaches it, and it holds no grudge or memory** beyond the conversation (plus any explicit memory feature). Re-asking in a fresh chat is a legitimate, informative move.
4. **Use variation as a tool.** Same question, twice, fresh sessions: agreement is weak evidence of stability; divergence is strong evidence you're on shaky ground (§1's sampling means both are normal).
5. **Expect the jagged edge.** §4's "pile of local heuristics" predicts what benchmarks confirm: performance that collapses under small reframings — a 2024 evaluation went from 97.8% to 52.8% on identical puzzles when the objects were renamed to nonsense words. Brilliant-at-X says little about X-adjacent. Test *your* task, in *your* phrasing, before trusting a capability claim. `[corroborated]`
6. **When a number matters, trace it to its table** — the habit this guide's own research keeps being saved by ([P-003](../practices/P-003-trace-the-number.md)): four of the eight headline claims we verified for this chapter arrived with real numbers wrongly labeled by the summary layer in between.
7. **Ask "does it reliably do X, verifiably," never "does it understand."** The first question has an answer you can act on this afternoon (§4).

The next chapter takes the second half of the story: the *product* around the model — context windows, system prompts, tools, retrieval, memory — where most day-to-day behavior you'll want explained actually comes from.

## Going deeper (all verified links, August 2026)

- **Read (30 min):** [Large language models, explained with a minimum of math and jargon](https://www.understandingai.org/p/large-language-models-explained-with) — the single most lucid prose companion to §§1–3.
- **Watch (27 min):** [3Blue1Brown, "But what is a GPT?"](https://www.3blue1brown.com/lessons/gpt) — the visual intuition; or Karpathy's [1-hour general-audience talk](https://www.youtube.com/watch?v=zjkBMFhNj_g) (Nov 2023 vintage — mechanisms hold, model names date).
- **Play (15 min):** [Transformer Explainer](https://poloclub.github.io/transformer-explainer/) — a live model showing §1 happening; [the tokenizer playground](https://huggingface.co/spaces/Xenova/the-tokenizer-playground).
- **For stakes:** the [AI Hallucination Cases database](https://www.damiencharlotin.com/hallucinations/) — browsable court decisions.
- **For the frontier of §4:** Anthropic's [On the Biology of a Large Language Model](https://transformer-circuits.pub/2025/attribution-graphs/biology.html) — unusually readable primary research; skim the worked examples.

The full resource list, with time/cost/caveats per entry, lives in [RESOURCES.md](../RESOURCES.md).

---

*About this chapter's evidence: distilled from a [logged research session](../research/2026-08-13-ch01-what-an-llm-is/) — ~89 used sources with lineage and incentive notes, five parallel research agents, two adversarial verification agents, eight anchor claims verified (four corrected before anything was written). Found an error? The [decision log](../DECISIONS.md) and [journal](../journal/) show how corrections get handled — verified against sources, then applied visibly.*

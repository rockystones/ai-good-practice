# Findings — ch01-what-an-llm-is (session R1)

Written 2026-08-13 against [BRIEF.md](BRIEF.md). Method: 5 Sonnet-class gatherers (one per planned angle; raw reports in [gather/](gather/)) + 2 Opus-class adversarial verifiers on eight anchor claims ([verify/](verify/)) + orchestrator synthesis. Grades: `established` / `corroborated` / `single-source` / `contested` / `anecdote` per [../../method/research-protocol.md](../../method/research-protocol.md). Claim IDs resolve via [SOURCES.md](SOURCES.md).

**Verification changed the answers.** Of eight anchor claims sent to adversarial verification, four needed material correction (wrong metric labels, a percentage that wasn't a percentage of people, a stale figure, a weak source about to anchor a section). Everything below incorporates those verdicts.

## Answers by sub-question

### SQ1 — What does "predicting the next token" actually mean? `[established]`

A language model is a trained mathematical function that, given text so far, outputs a **probability distribution over every possible next token** (~50k–100k token vocabulary). Generation is a loop: sample one token from that distribution, append it, run again (A2.c1, A3.c1, A10.c1 — three independent lineages, formula-level consistent). Sampling controls reshape *selection only*: temperature rescales the distribution, top-k/top-p shrink the candidate pool; none of them add knowledge or reasoning (A10.c4). Temperature values are empirical folklore, not theory — Wolfram: "just a matter of what's been found to work in practice" (A4.c3).

**Training vs inference is the load-bearing distinction for readers**: training changes weights via backpropagation over enormous corpora; at use time the weights are **frozen** — nothing you say teaches the model anything (A4.c4, A7.c1, A14.c4). All randomness at use time lives in the sampling step.

Nuance worth printing: **temperature 0 still isn't fully deterministic in deployed systems** — Anthropic's own docs warn identical inputs may produce different outputs across API calls (A7.c5). Textbook framing vs deployment reality; learners will otherwise assume temp-0 = same answer every time.

*Confidence: high. Mechanism corroborated across formula-level, official-docs, and explainer lineages that don't cite each other.*

### SQ2 — What do pretraining and post-training each contribute? `[established]`

- **Pretraining** (self-supervised next-token prediction over hundreds of billions of words) bakes general language patterns and knowledge-shaped compression into the weights. The result — a **base model** — is "not inherently good at answering questions or following instructions" (A7.c2); Karpathy-attributed framing: "an internet document simulator" (A14.c2). Two independent tiers converge.
- **Supervised fine-tuning** teaches assistant format from curated demonstrations — cheap and iterable (hours, not months) vs pretraining (A8.c1, A14.c5, A5.c1).
- **RLHF** (rank outputs → reward model → RL with a KL leash) shapes *which* outputs people get. Lineage traced cleanly: Christiano et al. 2017 (Atari/robotics preferences, A9) → InstructGPT 2022 (A8) → "ChatGPT is a sibling model to InstructGPT … same methods" (A5.c3).
- **Effect size, verified (V2)**: human raters preferred the 1.3B InstructGPT over the **unprompted** 175B GPT-3 (85±3% vs plain, 71±4% vs few-shot at equal size; few-shot prompting narrows the gap materially). Safe gloss: post-training changed *which outputs people liked*, not how much the model knew — and it costs an "alignment tax" on some benchmarks.
- **What comes after RLHF has no single story** `[corroborated]`: Anthropic frames Constitutional AI/RLAIF (A6); a 2025 survey frames five post-training paradigms (A12.c2); Karpathy-attributed material emphasizes verifiable-reward RL with "no human involved" for checkable domains (A14.c6). Picking one framing would imply false consensus.

*Confidence: high on the pipeline; the divergent successor framings are themselves the finding.*

### SQ3 — In what sense does an LLM "know" things? Layered answer

**What's stored** `[established]`: not a database. Concepts live as **directions in activation space, superposed** — more features than neurons, each a non-orthogonal combination across many parameters (B2.c1–c3; ROME's causal-tracing lineage B5 agrees knowledge has causal sites while Hase et al. B6 shows located ≠ editable, ρ≈−0.13). "Where is it stored" and "where can you change it" are empirically different questions — no database metaphor survives that.

**What the structure looks like** `[corroborated]`: three compatible measurements, not a debate with a winner (V2 framing):
1. *Structured, decodable state exists*: Othello board state decodable and causally load-bearing (C4, C5); a 2025 ICLR study retrained seven architectures on Othello moves and found all "induce the board layout" with strikingly similar features (C6 — **verified with caveats: models retrained on Othello, not probed as shipped; the abstract's "99%" is not traceable to a results table and measures cross-model representation alignment — do not print it**). Space/time coordinates linearly encoded in Llama-2 (C11); millions of interpretable, steerable features in a production Claude (C9, B3).
2. *The implementation looks like heuristics*: the same Othello-GPT computes board state via "many independent decision rules," not one algorithm (C7); Melanie Mitchell endorses this reading (C8.c2).
3. *Coherence is weaker than the diagnostics suggest*: Vafa et al. (NeurIPS 2024, found by verification) show generative models pass world-model probes while their implicit world models are "far less coherent than they appear."

**The model has an internal signal about its own knowledge** `[single-source at mechanistic level]`: Anthropic's circuit tracing found a default "can't answer" circuit gated by familiarity features; artificially activating "known answer" features for a fake name produces confident fabrication (B1.c1–c2). Powerful, but one lab's method that works on ~25% of attempted prompts by its own accounting (B1.c5) — flag, don't over-build on it.

**Whether any of this is "understanding"** `[contested]`: Bender — comprehension is supplied by the human reader; "synthetic text-extruding machines" (B9, C1, C2). Sutskever — prediction requires modeling "the underlying reality" (C13). Hinton — humans understand "in much the same way" (C14). The incentive gradient runs almost perfectly opposite the technical claim on both sides (C12 vs C13 incentive notes) — and, notably, both camps complain "understanding/world model" is doing undefined work (C2.c2, C8.c1): the rare cross-camp agreement. Interpretability's own value is contested by credentialed voices (B7 vs B8).

*Confidence: high on distributed storage; medium on how well internals are understood; the interpretation question should be presented as genuinely open.*

### SQ4 — Why confident falsehoods, and is it fixable?

**The evidence-supported arc (V1):** three independent strands converge —
1. **Training and evaluation reward confident guessing** `[corroborated]`: OpenAI's own analysis: hallucinations "originate simply as errors in binary classification" under natural statistical pressure (generating truths is provably harder than recognizing them — bounded below by roughly twice the corresponding true/false classification error), and persist because benchmarks score "I don't know" like a wrong answer — "models are optimized to be good test-takers" (B10, verified verbatim; unrefereed preprint, 3 of 4 authors OpenAI, "blame the benchmarks" is vendor-convenient — print the provenance; serious framing criticism exists).
2. **Post-training damages the model's own uncertainty signal** `[single-source, admission against interest]`: pretrained GPT-4 "highly calibrated"; "the post-training hurts calibration significantly" (B13, verified verbatim — **say "post-training," not "RLHF"**; one figure, MMLU multiple-choice, externally unreproducible since the base model was never released).
3. **Sycophancy enters through human preference data** `[established]`: five assistants across three vendors; humans and preference models sometimes prefer agreeable-wrong over correct-disagreeable; optimizing against that "sometimes sacrifices truthfulness" (B12, ICLR 2024; converges with Bender's independent attribution B9.c3).

**Is it intrinsic?** `[contested — corrected pairing after verification]`: The gatherer's rebuttal source (Ackermann & Emanuilov) was **dropped on verification** (1 citation, unidentifiable co-author, self-referential trilogy, product-shaped fix). The honest pairing is: **Xu, Jain & Kankanhalli** (arXiv 2401.11817) — hallucination formally inevitable for any computable LLM as a general problem solver (diagonalization) — **with Suzuki et al.** (arXiv 2502.12187) — that result is "practically inert" (needs infinite input space) and hallucination can be made "statistically negligible" with enough data quality/quantity. "Mathematically inevitable" is true in a precise but weak sense that does NOT imply "can't be substantially reduced." Fatalism is not supported; neither is "solved."

**Current state** `[established]`: Not solved, and **"the hallucination rate" is not a number** (V1's central finding): the same GPT-5 system card puts the same models at ~47% (gpt-5-main, adversarially-collected SimpleQA, no web; abstentions make accuracy+hallucination ≠ 100%), ~7.2% of claims / 11.6% of responses (production-style traffic with browsing; gpt-5-thinking 4.5%/9.6%), and 0.6–0.9% (grounded long-form with browsing). Metric traps verified in the table itself: GPT-4o *beats* o3 on response-level while being *worst in the table* on claim-level (22.0%) — shorter answers, fewer claims per response. All numbers vendor self-reported and LLM-graded. Meanwhile real-world stakes are measurable and rising `[corroborated]`: ≥1,668 court decisions worldwide involving hallucinated material as of 2026-07-02 (~200 → 1,668 in about a year, ~8/day, an explicit undercount by the maintainer's criteria; Oregon's *Couvrette v. Wisnovsky*: 15 fabricated citations + 8 fabricated quotations, roughly $110,000 combined — details corrected in verification). Abstention can be trained (R-Tuning, B17) and retrieval helps hugely (the 0.7% row) — reducible, not eliminated.

*Confidence: high on "large, real, unsolved-but-reducible"; the intrinsic question stays contested with the corrected source pairing.*

### SQ5 — Which misconceptions do non-engineers demonstrably hold? `[graded per item]`

| Misconception | Evidence | Replacement |
|---|---|---|
| "It understands language the way a human does" | `established` — 47% of a nationally representative German sample agreed; **only 21% correctly rejected**; 32% unsure (verified primary, n≈1,000×2 surveys; SD2.c1→V2 upgrade); octopus-test argument (SD7); consciousness-attribution data (below) | It produces statistically plausible continuations; whether that constitutes "understanding" is genuinely contested even among experts — certainty in either direction is overclaiming |
| "It searches the web / has a database it looks up" | `corroborated` — review-level synthesis (SD2.c2, SD2.c3) + direct study of data-flow mental models (SD1); **the "93% of students" figure is REFUTED — it was 26 of 28 coded interview units from a 20-person study; use qualitative phrasing only** (V2) | Answers are generated from patterns fixed at training time; live search, when present, is a bolted-on tool |
| "Confident, fluent tone signals accuracy" | `established` — strongest-evidenced item: ~60-study Microsoft Aether review; even 50%-labeled accuracy plus a confident explanation raised trust (SD3.c1–c5) | Fluency is a generation-quality byproduct; nothing in generation cross-checks reality |
| "It might be somewhat conscious / have feelings" | `established`, precision-critical — 67% of N=300 US adults *declined to rule out* ChatGPT having experience, but **median rating 16/100**; heavier users rated it *higher* (verified; SD4→V2); attribution is manipulable by marketing framing (CHI 2026 RCT, SD5) | Not "most people think it's conscious" — most people won't rule it out, and framing moves the needle; that malleability is itself the lesson |
| "It's an agent/expert giving its opinion" | `corroborated` (SD2.c3) | A generator of helpful-answer-shaped text; no persistent goals or stake in being right |
| "It remembers me by default" / "it's deterministic" | `anecdote` — **zero peer-reviewed N-studies found for either** (G4's honest negative result); practitioner/blog tier only (SD18, SD19) | Stateless per conversation (memory = added feature); sampled generation varies legitimately |

The field itself is young: the one systematic review covers 28 studies, 2023–2024 only, mostly non-representative samples — and it garbled one of its own sources (V2). *Cite primaries for numbers.*

### SQ6 — How do the best explainers teach this? `[corroborated]`

**Two ordering traditions, no comparative study**: technical explainers (Wolfram, Karpathy, 3B1B, Alammar) open with a deliberately reductive mechanism hook ("just predicting the next word") and save limits for the end; AI-literacy curricula (Long & Magerko lineage) put recognition and misconception-correction first. **No study experimentally compares analogy framings or orderings for adult learning outcomes** — a real gap (and an honest framing opportunity: present what credible educators do and where each admits its analogy misleads).

Analogy catalog with failure modes (each named by its own popularizer or a peer-reviewed critic — the strongest pattern found): autocomplete-on-steroids (implies determinism; ignores RLHF reshaping — SD18.c1); blurry-JPEG compression (implies a retrievable original; Chiang names it himself — SD17.c2); simulator/role-play (the "agent behind the mask" fallacy — SD11.c2); calculator-for-words (imports determinism and verifiability LLMs don't have — SD10.c2 + the one peer-reviewed analogy-failure analysis, Voinea SD8); stochastic parrot (contested whether it still describes tool-using systems — SD18.c2 vs SD16); dream machine (repairs "confident=correct" but risks implying arbitrariness — G4's own unsourced inference, flagged). Meta-observation: the three most credentialed explainers all choose the same "too simple" hook and immediately complicate it — a deliberate strategy worth copying.

### SQ7 — What should we recommend? → [../../RESOURCES.md](../../RESOURCES.md)

16 link-verified recommendations + follow-list, categorized with time/cost/caveats. Notable: no verified curated list for conceptual non-coder learners exists (all awesome-lists skew practitioner); three high-reputation resources (Wolfram essay, Guardian and FT visual explainers) fell out on fetch technicalities, not quality — recheck in a normal browser before the chapter cites them.

## Surprises

1. **The verification stage changed four of eight anchor claims** — all four the same species: a real number detached from what it measured by a summary layer (two metric-label merges, a units-of-analysis error *inside a peer-reviewed systematic review*, a stale figure). See retro.
2. **GPT-4o is simultaneously better and worse than o3 on the same eval** depending on denominator — the cleanest teaching example of metric traps we could have asked for, sitting in a vendor's own table.
3. **A replication that strengthened a splashy result** (Othello across 7 architectures) — against the usual deflation heuristic — while a mechanistic dissection of the same artifact deflated its interpretation anyway.
4. **Heavier chatbot users attribute more consciousness, not less** (verified) — familiarity does not breed calibration.
5. **Temp-0 nondeterminism** is documented in official vendor docs but absent from every popular explainer checked.
6. **A viral statistic debunked in passing**: "a quarter of teens feel AI understands them better than most people" is NOT in the Common Sense Media report it's usually attributed to (G4 read it cover-to-cover).
7. **The two-Mitchells hazard** (Margaret vs Melanie) — misattribution trap flagged before it bit.

## Contested points — kept visible

| Point | Position A | Position B | What would settle it |
|---|---|---|---|
| Is hallucination intrinsic? | Formally inevitable (Xu et al. 2401.11817) | Inevitability result practically inert; statistically negligible with enough data (Suzuki et al. 2502.12187); incentive-fixable (Kalai et al.) | Whether abstention-aware scoring + data scaling drives production rates toward zero over model generations |
| Do LLMs "understand"? | Bender: form without meaning; reader supplies comprehension | Sutskever/Hinton: prediction requires modeling underlying reality | A falsifiable, pre-committed definition both camps accept (neither currently offers one) |
| World models | Decodable causal internal state, replicated ×7 | Implementation = local heuristics; coherence weaker than probes imply (Vafa et al.) | Frontier-scale causal studies on out-of-distribution generalization |
| Emergent abilities | Real discontinuous jumps (Wei; U-curves) | Largely metric artifacts (Schaeffer) | Pre-registered prospective predictions of jumps before larger models are tested |
| "Hallucination" as a term | Standard usage (field, OpenAI) | Category error implying a perceiving mind (Bender); "confabulation" alternative | Terminological — chapter should note the dispute, pick one, and say why |

## Open questions (logged, not silently dropped)

- Karpathy video transcripts unverifiable with current tooling (YouTube 401) — exact analogy wording needs transcript access before quoting verbatim in the chapter.
- Stochastic Parrots 2021 never read cover-to-cover (paywall) — pull via institutional access before featuring prominently.
- Anthropic-heavy interpretability set — balance-check against Google DeepMind (Nanda's team) work in a follow-up.
- Whole source set is Anglophone/US-centric — non-Western perspectives unsampled.
- Current Charlotin count and GPT-5 table values should be re-pulled at drafting time (both move).
- Empirical pedagogy of analogies: genuine research gap — nothing to cite; chapter must frame accordingly.

## Retrospective (Phase 5 — the five questions)

1. **Did results answer the framed question?** Yes, without drift: all seven sub-questions answered at `corroborated`-or-better except where the honest answer is "the literature is thin" (SQ5's two unmeasured misconceptions; SQ6's missing pedagogy studies) — which the brief's priors P4 predicted. Priors: P1 confirmed; P2 *refined* (inevitable-in-a-weak-formal-sense vs practically-reducible is sharper than the prior's framing); P3 confirmed contested; P4 confirmed.
2. **Were the sources right?** Primaries and admission-against-interest vendor documents carried the most weight. The single highest-yield decision was **spending Opus on adversarial verification rather than more gathering** — it changed four of eight anchor claims. Lowest yield: community-discourse bundles (used only as discourse evidence, correctly).
3. **Comprehensive enough / loud-source traps?** Diversity quota held (~10% max single voice). Two traps caught: an unverifiable rebuttal paper nearly anchored the intrinsic-hallucination position (loud-because-convenient); a peer-reviewed review's paraphrase nearly substituted for its own primary. Saturation was not formally run — the session stopped at budget/coverage criteria with gaps logged above (per protocol's stopping rules).
4. **How do results map to the question?** Every SQ answer cites claim IDs traceable through SOURCES.md → gather/ files → verify/ verdicts. The chapter can be drafted from this file alone, following citations down only where needed.
5. **What to improve next time?**
   - **Adopted as a protocol amendment (D-009): the Numbers Rule** — no statistic ships without being traced to the primary table/figure it came from; secondary summaries (including peer-reviewed reviews and paper abstracts) garble labels at an observed rate of ~4 in 8 anchor claims.
   - **Access playbook** captured in [../../method/access-notes.md](../../method/access-notes.md) — proxy routes, blocked domains, PDF workarounds — so future sessions stop rediscovering them.
   - Gap to close next session: video-transcript tooling for quoting talks.
   - Tier design validated: Sonnet gathers wide, Opus verifies narrow. Keep.

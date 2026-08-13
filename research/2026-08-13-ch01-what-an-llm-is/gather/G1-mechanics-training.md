# G1 — Mechanics & training pipeline (raw gatherer report)

*Intermediate artifact: Sonnet-class gatherer, session R1, 2026-08-13, assigned SQ1+SQ2. Authoritative synthesis: `../FINDINGS.md`. Source IDs SA-n; claim IDs An.cm.*

## SOURCES

### SA-1 — "Large language models, explained with a minimum of math and jargon" (Understanding AI)
- URL: https://www.understandingai.org/p/large-language-models-explained-with · Accessed: 2026-08-13 · Author/date: Timothy B. Lee & Sean Trott, 2023-07-27 · Type/Tier: B (journalist w/ CS background + cognitive scientist; secondary synthesis, checkable track record) · Lineage: synthesizes GPT-3-era transformer literature into original jargon-free prose · Incentive: subscription-newsletter reputation; no product — low distortion · Status: used
- Claims:
  - A1.c1 — Words represented as vectors; attention heads use query/key vectors so words "look around" for relevant context; GPT-3's largest version performs 9,216 attention operations per prediction
  - A1.c2 — Feed-forward layers act as "a database of information the model has learned" (~1.2B params/layer in GPT-3), vs attention heads which retrieve info already in the prompt
  - A1.c3 — Training = forward pass + backward pass (backprop adjusts 175B weights); GPT-3 trained on ~500B words; "more than 300 billion trillion" floating-point ops
  - A1.c4 — Size progression: GPT-1 117M (2018) → GPT-2 1.5B → GPT-3 175B; GPT-4 undisclosed, "widely believed" larger
  - A1.c5 — Analogy: training as adjusting a shower faucet toward the right temperature, smaller adjustments as you converge

### SA-2 — "But what is a GPT? Visual intro to transformers" (3Blue1Brown, Deep Learning ch.5)
- URL: https://www.3blue1brown.com/lessons/gpt/ · Accessed: 2026-08-13 · Author/date: Grant Sanderson (text: Justin Sun), 2024-04-01 · Type/Tier: B (independent educator, large checkable track record, Patreon-funded) · Lineage: original geometric/visual derivation of attention; echoes Vaswani et al. for underlying math · Incentive: education-channel reputation; no LLM product · Status: used
- Claims:
  - A2.c1 — Transformer output is "a prediction of what comes next, in the form of a probability distribution" over all possible next chunks; only the final vector is used for the prediction
  - A2.c2 — Repeated sampling-and-refeeding "is essentially what's happening" when ChatGPT produces one word at a time
  - A2.c3 — Weights are "the actual brains of the model"; nearly all computation is weighted sums packaged as matrices
  - A2.c4 — GPT-3 specs: 175B params across ~28,000 matrices; embedding dim 12,288; vocab 50,257; context 2,048 tokens; embedding matrix = 617,558,016 weights

### SA-3 — "Large Language Models explained briefly" (3Blue1Brown)
- URL: https://www.3blue1brown.com/lessons/mini-llm/ · Accessed: 2026-08-13 · Author/date: Grant Sanderson, 2024-11-20 · Type/Tier: B · Lineage: condensed overview echoing SA-2 + published RLHF literature · Incentive: same as SA-2 · Status: used
- Claims:
  - A3.c1 — An LLM is "a sophisticated mathematical function that predicts what word comes next," assigning probabilities to all possible next words
  - A3.c2 — Analogy: a movie script torn off mid-page, finished by repeated predict-and-refeed
  - A3.c3 — Analogy: parameters as "dials on a really big machine"; changing them changes next-word probabilities
  - A3.c4 — Pretraining via backprop on "many, many trillions of examples"; then RLHF where workers flag unhelpful/problematic predictions
  - A3.c5 — Scale renderings: GPT-3's training text = "over 2,600 years" of human reading; largest-model training = "well over 100,000,000 years" at 1B ops/sec single-machine

### SA-4 — "What Is ChatGPT Doing … and Why Does It Work?"
- URL: https://writings.stephenwolfram.com/2023/02/what-is-chatgpt-doing-and-why-does-it-work/ · Accessed: 2026-08-13 (direct fetch blocked by TLS cert error; retrieved via r.jina.ai reader proxy, cross-checked against a mirror) · Author/date: Stephen Wolfram, 2023-02 · Type/Tier: B (named domain expert; writes to reinforce his own computational worldview) · Lineage: primary essay, original pedagogical build-up (letter frequencies → n-grams → neural nets) · Incentive: sells Mathematica/Wolfram|Alpha + personal brand; mild framing incentive · Status: used
- Claims:
  - A4.c1 — "What ChatGPT is always fundamentally trying to do is to produce a 'reasonable continuation'" based on learned probabilities
  - A4.c2 — Temperature: always picking the top word gives "flat" essays; some randomness gives "more interesting" text; T≈0.8 "seems best" for essays
  - A4.c3 — Explicitly: no theory for the temperature choice — "just a matter of what's been found to work in practice"; term borrowed from statistical physics, "no 'physical' connection"
  - A4.c4 — Training = examples + loss function + "path of steepest descent" (backprop/gradient descent)
  - A4.c5 — Counterintuitive: "easier to solve more complicated problems with neural nets than simpler ones" (higher-dim weight spaces offer more descent paths)
  - A4.c6 — Scale: ~175B weights; GPT-2 12 blocks/768-dim; GPT-3 96 blocks/12,288-dim; ~50,000 tokens; "a few hundred billion words" training text

### SA-5 — "Introducing ChatGPT" (OpenAI)
- URL: https://openai.com/index/chatgpt/ · Accessed: 2026-08-13 (direct 403; via r.jina.ai proxy) · Author/date: OpenAI, undated on page (late-2022 announcement) · Type/Tier: A (official first-party) · Lineage: company's own account; ties to SA-8 methodology · Incentive: direct marketing incentive — highest distortion risk in this set · Status: used
- Claims:
  - A5.c1 — Supervised fine-tuning first: trainers played both user and assistant, mixed with InstructGPT dataset reformatted as dialogue
  - A5.c2 — Reward-model stage: trainers ranked completions; comparisons trained a reward model; fine-tuned with PPO, iterated several times
  - A5.c3 — "ChatGPT is a sibling model to InstructGPT … trained using the same methods"; fine-tuned from a GPT-3.5-series model finished "in early 2022"
  - A5.c4 — Trained on Azure AI supercomputing infrastructure

### SA-6 — "Constitutional AI: Harmlessness from AI Feedback" (Anthropic)
- URL: https://www.anthropic.com/research/constitutional-ai-harmlessness-from-ai-feedback · Accessed: 2026-08-13 · Author/date: Anthropic, 2022-12-15 (arXiv 2212.08073) · Type/Tier: A (official research artifact) · Lineage: originates Constitutional AI/RLAIF · Incentive: commercial + safety-brand (promotes own methodology) · Status: used
- Claims:
  - A6.c1 — Goal: "train a harmless AI assistant … without any human labels identifying harmful outputs" (RLAIF)
  - A6.c2 — Two phases: supervised (self-critique + revision → finetune) then RL (AI judges pairs → preference model)
  - A6.c3 — Oversight from "a list of rules or principles"; chain-of-thought reasoning for transparency of self-evaluation

### SA-7 — Claude Docs Glossary (Anthropic)
- URL: https://platform.claude.com/docs/en/about-claude/glossary · Accessed: 2026-08-13 · Author/date: Anthropic, undated (treated warily per method rules) · Type/Tier: A (official docs) · Lineage: primary as Anthropic's own definitions; underlying concepts not original to it · Incentive: developer-trust accuracy incentive + product framing · Status: used
- Claims:
  - A7.c1 — "Pretraining is the initial process of training language models on a large unlabeled corpus"; autoregressive models pretrained to predict next word given context
  - A7.c2 — "These pretrained models are not inherently good at answering questions or following instructions" — fine-tuning and RLHF refine them
  - A7.c3 — RLHF: humans rank ≥2 example outputs; RL "encourages the model to prefer outputs that are similar to the higher-ranked ones" (cites arXiv 2204.05862)
  - A7.c4 — Temperature controls randomness of predictions; higher = more creative/diverse, lower = more conservative
  - A7.c5 — "Even with temperature set to 0, the results will not be fully deterministic" — identical inputs may differ across API calls (Anthropic's own and third-party inference)
  - A7.c6 — A token ≈ 3.5 English characters for Claude
  - A7.c7 — Context window described as "working memory," distinct from training corpus

### SA-8 — "Training language models to follow instructions with human feedback" (InstructGPT)
- URL: https://arxiv.org/abs/2203.02155 · Accessed: 2026-08-13 (abstract-page depth only) · Author/date: Ouyang et al. (OpenAI), 2022-03-04; NeurIPS 2022 · Type/Tier: A (peer-reviewed primary) · Lineage: originates the SFT-then-RLHF-at-GPT-3-scale recipe; builds on SA-9 · Incentive: OpenAI validation incentive, mitigated by peer review · Status: used
- Claims:
  - A8.c1 — Two stages: SFT on labeler demonstrations, then RLHF on labeler rankings
  - A8.c2 — Human raters preferred a 1.3B-param InstructGPT's outputs over untuned 175B GPT-3 — ~100× smaller, preferred
  - A8.c3 — RLHF improved truthfulness, reduced toxicity, minimal benchmark regressions ("alignment tax")

### SA-9 — "Deep Reinforcement Learning from Human Preferences"
- URL: https://arxiv.org/abs/1706.03741 · Accessed: 2026-08-13 (abstract-page depth) · Author/date: Christiano, Leike, Brown, Martic, Legg, Amodei, 2017-06-12; NeurIPS 2017 · Type/Tier: A (peer-reviewed primary) · Lineage: establishes the technique later branded RLHF; predates SA-8 · Incentive: academic priority · Status: used
- Claims:
  - A9.c1 — RL from "human preferences between pairs of trajectory segments" instead of a hand-crafted reward function
  - A9.c2 — Solved Atari/robotics tasks with feedback on "less than one percent" of interactions
  - A9.c3 — Complex novel behaviors from ~1 hour of human time

### SA-10 — "How do temperature, top-k, and top-p sampling differ?"
- URL: https://sebastianraschka.com/faq/docs/temperature-topk-topp-sampling.html · Accessed: 2026-08-13 · Author/date: Sebastian Raschka, undated (treated warily) · Type/Tier: B (ML researcher/author, strong track record) · Lineage: secondary technical synthesis; attributes top-p to Holtzman et al. · Incentive: books/courses/brand; low distortion (formula-level verifiable) · Status: used
- Claims:
  - A10.c1 — Temperature formula p_i(T)=exp(z_i/T)/Σexp(z_j/T); T=1 unchanged, T<1 sharpens, T>1 flattens; ratios change, ranking preserved
  - A10.c2 — Top-k keeps fixed count + renormalizes; top-p keeps smallest prefix reaching cumulative p (adaptive; Holtzman et al.)
  - A10.c3 — Worked numeric example: [0.50,0.25,0.15,0.07,0.03] → top-k=3 → [0.556,0.278,0.167] → T=0.5 → [0.734,0.183,0.066,…]
  - A10.c4 — Sampling controls "cannot add factual knowledge or reasoning ability" — they change token selection, not weights

### SA-11 — "Illustrating Reinforcement Learning from Human Feedback" (Hugging Face)
- URL: https://huggingface.co/blog/rlhf · Accessed: 2026-08-13 · Author/date: Nathan Lambert, Castricato, von Werra, Havrilla, 2022-12-09 · Type/Tier: B (practitioner team, checkable track record) · Lineage: synthesizes SA-8/SA-9 into a 3-step pedagogical framing · Incentive: open-source mindshare; low pressure on RLHF facts · Status: used
- Claims:
  - A11.c1 — RLHF = (1) pretrain LM, (2) train reward model mapping text → scalar human-preference reward, (3) fine-tune LM against it via RL (typically PPO)
  - A11.c2 — Analogy: reward model as "part of the environment" in the RL loop
  - A11.c3 — Example ratio: 175B policy LM + 6B reward model; preference datasets ~50k labeled comparisons
  - A11.c4 — PPO objective includes KL-divergence penalty (r = r_θ − λr_KL) to stop the policy drifting too far from the pretrained model

### SA-12 — "A Survey on Post-training of Large Language Models"
- URL: https://arxiv.org/abs/2503.06072 · Accessed: 2026-08-13 (abstract-page depth) · Author/date: Guiyao Tie, Zeli Zhao, et al. (26 authors), 2025-03-08 rev. 2025-08-01 · Type/Tier: A-preprint (not verified peer-reviewed) · Lineage: tertiary survey; originates a 5-paradigm taxonomy · Incentive: academic citation · Status: used
- Claims:
  - A12.c1 — Post-training addresses pretrained models' "restricted reasoning capacities, ethical uncertainties, and suboptimal domain-specific performance"
  - A12.c2 — Five paradigms: Fine-tuning, Alignment, Reasoning, Efficiency, Integration/Adaptation — "from ChatGPT to DeepSeek-R1"
  - A12.c3 — Pretraining builds capability; post-training mitigates biases, deepens reasoning, enhances domain adaptability

### SA-13 — "[1hr Talk] Intro to Large Language Models" (Karpathy)
- URL: https://www.youtube.com/watch?v=zjkBMFhNj_g · Accessed: 2026-08-13 (**metadata fetched directly; transcript blocked (401) both direct and via proxy — claims are metadata + convergent third-party paraphrase, NOT verified transcript**) · Author/date: Andrej Karpathy, 2023-11-22 · Type/Tier: B with lowered confidence (secondary-paraphrase basis flagged) · Lineage: primary talk explaining published literature in own words; write-ups echo it, not each other · Incentive: educator reputation · Status: used with caveat
- Claims:
  - A13.c1 — [secondary-corroborated] Base-model generation as "dreaming" internet documents — mimicking, not retrieving
  - A13.c2 — [secondary-corroborated] LLM-as-emerging-OS analogy (kernel coordinating memory/compute/tools)
  - A13.c3 — [secondary-corroborated] Kahneman analogy: current LLMs = System 1; System 2 is a goal
  - A13.c4 — Chapter structure (confirmed via direct metadata): 3-stage pipeline — pretraining → "internet document simulator"; SFT → assistant + "LLM Psychology"; RLHF/RL
  - A13.c5 — Quote (snippet-sourced, single-source): "do not trust what LLMs say or do" without independent verification

### SA-14 — "Deep Dive into LLMs like ChatGPT" (Karpathy)
- URL: https://www.youtube.com/watch?v=7xTGNNLPyMI · Accessed: 2026-08-13 (**metadata direct; transcript blocked (401); claims rest on Karpathy's own X announcement + two independent, non-cross-citing write-ups (anfalmushtaq.com, anup.io)**) · Author/date: Andrej Karpathy, 2025-02-05, 3h31m · Type/Tier: B with same caveat · Lineage: primary talk; triangulated write-ups · Incentive: educator reputation; (unverified 2026 headline re: joining Anthropic pretraining postdates the video — not treated as incentive factor) · Status: used with caveat
- Claims:
  - A14.c1 — Karpathy's own X description: "a general audience deep dive … the full training stack … mental models of how to think about their 'psychology'"; stage 1 = "pretraining: data, tokenization, Transformer neural network I/O" (x.com/karpathy/status/1887211193099825254)
  - A14.c2 — [secondary-corroborated ×2] Base model = "an internet document simulator" / "just an expensive autocomplete"
  - A14.c3 — [secondary-corroborated] Parameters as a "lossy zip file" of internet knowledge; weights = "vague recollection" vs context tokens = "working memory"
  - A14.c4 — [secondary-corroborated] Weights frozen during generation; only training backprop updates them; generation stochastic, not deterministic replay
  - A14.c5 — [secondary-corroborated] SFT swaps internet data for curated conversations with chat-template tokens; hours not months; iterable often
  - A14.c6 — [secondary-corroborated] RL with verifiable rewards (math): "no human is involved" — generate many candidates, train on the ones reaching correct answers; AlphaGo "Move 37" analogy
  - A14.c7 — [secondary-corroborated] RLHF for unverifiable domains via reward model; "the reward model is just a simulation of human preferences"; over-optimizing risks reward-hacked "complete nonsense"
  - A14.c8 — [secondary-corroborated ×1] "Swiss cheese" capability model — gaps scattered unpredictably

## REJECTED / NOT PURSUED
- R-1 — web.archive.org mirrors of SA-4/SA-5 — tool-level block on the domain; superseded by proxy fetches
- R-2 — help.openai.com "How ChatGPT … developed" — 403; redundant with SA-5
- R-3 — openai.com/chatgpt/overview/ — 403; not retried (SA-5 covers)
- R-4 — lawwu.github.io Karpathy-summary URL — resolved to blog index, content mismatch
- R-5 — fullpicture.app mirror of SA-4 — Tier D mirror; superseded by proxy fetch of the real essay
- R-6 — articsledge.com "What Are Model Weights … in 2026?" — SEO listicle pattern; skipped without fetch
- R-7 — arXiv 2407.16216 RL-for-post-training survey — unread lead; SA-12 covers taxonomy need
- R-8 — Iowa State PDF reprint of Wolfram essay — 9MB, unreadable in environment; superseded

## GATHERER ANSWERS (working synthesis — superseded by ../FINDINGS.md)

### SQ1 — next-token prediction
- Forward pass ends in a probability distribution over the whole vocabulary (~50k tokens), via softmax over logits (A2.c1, A10.c1, A3.c1).
- Autoregressive loop: sample, append, re-run ("torn-off movie script", A3.c2; "one word at a time", A2.c2).
- Temperature rescales logits pre-softmax (A10.c1); Wolfram's T≈0.8 for essays with explicitly no theory behind it (A4.c2-c3); top-k/top-p shrink the candidate pool (A10.c2).
- Sampling knobs change selection only — no knowledge or reasoning added (A10.c4).
- Training (backprop, weight changes) vs inference (frozen weights, randomness only in sampling) (A4.c4, A14.c4, A7.c1).
- GPT-3 concrete scale: 175B params, 96 layers, 12,288-dim, 2,048-token context (A2.c4, A4.c6).
- Confidence: high on mechanism (formulas + official docs + Wolfram mutually consistent); medium-high on Karpathy-attributed specifics (paraphrase basis).

### SQ2 — pretraining vs post-training
- Pretraining: self-supervised next-token prediction over huge unlabeled corpus; general patterns + knowledge-shaped compression into weights (A7.c1, A1.c3, A3.c4).
- Base model ≠ assistant: "not inherently good at answering questions" (A7.c2); "internet document simulator"/"expensive autocomplete" (A14.c2) — independent convergence.
- SFT teaches format/behavior from curated demonstrations; cheap and iterable vs pretraining (A8.c1, A14.c5, A5.c1).
- RLHF: rankings → reward model → PPO with KL constraint (A8.c1, A5.c2, A11.c1, A11.c4).
- Lineage: Christiano 2017 (A9) → InstructGPT (A8) → ChatGPT "sibling model … same methods" (A5.c3).
- Effect size: 1.3B RLHF'd preferred over 175B untuned (A8.c2) — post-training reshapes perceived quality more than raw capability.
- Failure modes + successors: reward-model over-optimization (A14.c7); Constitutional AI/RLAIF (A6); five-paradigm post-training landscape incl. verifiable-reward RL (A12.c2, A14.c6).
- Confidence: high on pipeline; medium on "what comes after RLHF" (three framings diverge — a finding).

## ANALOGIES OBSERVED
- Lee & Trott → shower-faucet training adjustment
- 3B1B → weights as "the brains"; torn-off movie script; parameters as dials
- Wolfram → "reasonable continuation"; temperature borrowed loosely from physics
- Anthropic CAI → written "constitution" the model critiques itself against
- Anthropic glossary → context window as "working memory"
- HF → reward model as part of the RL environment
- Karpathy (secondary-corroborated) → dreaming internet documents; LLM-as-OS kernel; System 1/System 2; lossy zip file; internet document simulator; student-practicing-problems RLHF; Swiss cheese capability; Move 37
- Jay Alammar (resource-only) → smartphone predictive-text, much larger; query/key as sticky-note vs filing-cabinet labels

## CONTRADICTIONS & SURPRISES
- **Temperature-0 is not actually deterministic in deployed systems** — textbook framing (A10) vs Anthropic's explicit docs warning (A7.c5). Theory-vs-deployment gap; learners will assume temp0 = same answer every time.
- **"What replaces RLHF" has no single answer**: Anthropic → RLAIF/CAI (A6); survey → five-way branch (A12.c2); Karpathy-attributed → verifiable-reward RL (A14.c6). Picking one implies false consensus.
- **Explainers conflate GPT-3's disclosed 175B with ChatGPT's undisclosed size** (A4.c6, A1.c3 vs A1.c4).
- **Same fact, three rhetorical packagings** of corpus scale: "~500B words" / "a few hundred billion" / "2,600 years of reading" (A1.c3, A4.c6, A3.c5) — pedagogy-relevant.
- **Verification gap**: neither Karpathy transcript retrievable (YouTube 401 direct + proxy); claims rest on tweet + convergent independent write-ups — substance likely accurate, wording not verbatim-confirmed.
- **Unverified tangential lead**: 2026-05-19 TechCrunch headline "Karpathy joins Anthropic's pre-training team" — not fetched/confirmed; postdates both videos; confirm before citing his affiliation anywhere.

## COVERAGE NOTE
- Karpathy transcripts: need purpose-built transcript tooling or browser automation; matters for exact analogy wording (pedagogy agent needs precise phrasing).
- SA-8/SA-9 read at abstract depth; pull full PDFs for exact figures if chapter cites percentages.
- Unread lead: arXiv 2407.16216 (second post-training survey) for cross-checking SA-12.
- 3B1B attention chapter located but not fetched (venue-diversity quota).
- SA-7 undated official docs — could be revised without trail.
- Set skews US/Anglophone big-lab + celebrity-educator; no non-Western explainer perspectives sampled.
- Tooling notes: writings.stephenwolfram.com = persistent TLS error (use r.jina.ai proxy); openai.com/help.openai.com = 403 to direct fetch (proxy works for openai.com). Future sessions: go straight to proxy.

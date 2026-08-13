# V2 — Adversarial verification: capability-evidence anchor claims

*Opus-class verifier, session R1, 2026-08-13. Mandate: try to break five load-bearing claims from the gather phase. Verdicts feed `../FINDINGS.md`.*

## Claim 1 — InstructGPT 1.3B preferred over 175B GPT-3 — **CONFIRMED as quotation; WEAKENED as gloss** (add one condition)

- Abstract verbatim: outputs from 1.3B InstructGPT "are preferred to outputs from the 175B GPT-3, despite having 100x fewer parameters." Baseline nuance: that sentence names **unprompted** GPT-3; the few-shot-prompted baseline is separate. At 175B: InstructGPT preferred **85 ±3%** vs plain GPT-3, **71 ±4%** vs few-shot GPT-3 (§4.1) — few-shot prompting materially narrows the gap; the paper never asserts 1.3B beats *prompted* 175B.
- Authors flag evaluation-set bias (training prompts designed for InstructGPT) and mitigate by evaluating on the GPT-3 API prompt distribution ("do not change significantly").
- "Preferred" = human preference by ~40 contracted labelers on instruction-style prompts, NOT "knows more"; the paper concedes an alignment tax on public NLP benchmarks.
- Chapter's gloss "post-training reshaped behavior so much that a 100×-smaller model was preferred" is safe — don't upgrade to "outperformed."

Printable: "Human raters preferred the output of a 1.3B model fine-tuned on human feedback to that of the original 175B GPT-3 — about 100× larger — when both got instruction-style prompts with no examples. A few worked examples narrow the gap substantially. What changed was which outputs people liked, not how much the model knew."

Sources: arXiv 2203.02155 abs + ar5iv full text (2026-08-13).

## Claim 2 — Othello world-model replication — **WEAKENED: do not print "99% board-grounding accuracy"**

- Abstract wording verbatim-correct (7 models; "up to 99% accuracy in unsupervised grounding"; "considerably stronger evidence"). ICLR 2025.
- But: **"99" appears only in the abstract** — no results table reports it. The measured quantity is **cross-model representation ALIGNMENT** (adversarial training + Procrustes, cosine similarity between model pairs; max unsupervised ≈97.2), NOT a board-state probe accuracy. Two independent full-text readings disagreed on what the 99% anchors to — the number is not traceable to a labeled table, so it must not be a headline statistic.
- **Models were retrained/fine-tuned on Othello game data** (LoRA for LLaMA-2/Mistral) — a reader must not infer a shipped chatbot contains a game board.
- "Bag of heuristics" (MATS 6.0, 2024-07-02) **coexists** rather than superseding: probes decode the board (agreed by both camps); the mechanism looks like many independent local rules; authors hedge ("cannot rule out … a single succinct algorithm"; "interim report"). Two levels: WHAT is represented (decodable state) vs HOW computed (heuristics).
- **Stronger peer-reviewed skeptic found**: Vafa, Chen, Rambachan, Kleinberg & Mullainathan, "Evaluating the World Model Implicit in a Generative Model" (NeurIPS 2024, arXiv 2406.03689) — Myhill–Nerode-inspired metrics incl. Othello: models pass existing diagnostics but their implicit world models are "far less coherent than they appear."

Printable: "A 2025 ICLR paper retrained seven architectures on nothing but Othello moves and reported all of them 'induce the Othello board layout,' converging on similar internal features across different designs — 'considerably stronger evidence' for the world-model hypothesis. Two caveats belong with it: the models were trained on Othello, not simply asked about it; and researchers examining HOW the board is computed find a pile of independent local rules, with a NeurIPS 2024 group arguing these implicit world models are markedly less coherent than the standard tests suggest."

Sources: arXiv 2503.04421 abs + HTML (×3 targeted fetches; PDF undecodable); LessWrong MATS post; WebSearch (ICLR status; Vafa et al.); openreview.net blocked by bot challenge (2026-08-13).

## Claim 3 — Kambhampati "3%" — **CONFIRMED as 2023 history; REFUTED in present tense**

- Primary (arXiv 2302.06706, 2023-02-13): "averaging only about 3% success rate" — GPT-3 davinci 1% (6/600), Instruct-GPT3 6.8% (41/600), BLOOM 1.6%; Mystery Blocksworld ~1.1%; human baseline 78%. **Pre-GPT-4 models only.**
- Same group, 2024 (arXiv 2409.13373): **o1-preview 97.8%** (587/600) Blocksworld; **52.8%** Mystery (obfuscated); **37.3%** randomized Mystery; **23.6%** on 110 larger 20+-step instances; o1-mini 56.6%/19.1%; best non-reasoning LLM (LLaMA 3.1 405B) 62.6%, "no LLM achieves even 5%" on Mystery. o1 = "a quantum improvement … still far from saturating." Cost $42.12/100 instances; classical planners: 100%, faster, cheaper, with guarantees.
- DeepSeek-R1 ~96.6%/39.8% — **search synthesis only, do not print without primary**.
- Constructive branch: LLM-Modulo (ICML 2024 spotlight, arXiv 2402.01817) — LLM + sound external verifiers; the group's own answer to its own critique.
- **The durable point is the obfuscation gap** (97.8% → 52.8% → 37.3% on renamed/randomized versions; collapse with plan length), not the perishable 3%.

Printable: "Tested rigorously in early 2023, the best models produced correct executable plans on a classic block-stacking benchmark only ~3% of the time — vs 78% for humans. By late 2024 OpenAI's o1-preview solved 97.8% of the same problems. But rename the objects into nonsense words and it drops to 52.8%; require twenty or more steps and it manages 23.6%. A conventional planning algorithm solves all of them, faster and far more cheaply."

Sources: arXiv 2302.06706 abs + ar5iv; arXiv 2409.13373 abs + HTML; arXiv 2206.10498 (PlanBench — no numbers in abstract, don't cite for figures); WebSearch (2026-08-13).

## Claim 4 — Misconception review — **SPLIT: (a) CONFIRMED & improved; (b) REFUTED as stated**

- Review bibliographics confirmed (UAIS vol 25 art 54, 2026; PRISMA; 670→28 studies, 2023–2024; "Knowledge and Awareness" underexplored).
- **(a) upgraded to the primary**: Lermann Henestrosa & Kimmerle = **two nationally representative German surveys** (n=1,028 Mar 2022; n=1,013 Jul 2023). Item-level: "AI language models can give good answers because they have learned to understand language like a human" — **47.29% incorrectly agreed, 20.53% correctly rejected, 32.18% don't know**. (Separate item: quality-depends-only-on-training-data — 49.06% incorrect.) Cite the primary with the German-sample scope; it's stronger than the review's compressed paraphrase.
- **(b) REFUTED as printed**: "93% of participants expected a search engine" traces to Kim, Yu, Detrick & Li (Educ. Inf. Technol. 30(1), 2024) = **20 Chinese students** at one Sino-British university, semi-structured interviews with a bespoke ChatGPT-4 tool. Table 2: "Search engine 26 (93%)" — **26 > 20 participants**; the percentages are shares of **28 coded qualitative units**, not people (26/28=92.9%). The systematic review misread its own source ("almost all participants (93%)"). Use qualitative phrasing only, no percentage. (Table-cell values via search synthesis + Springer full-text "28 totals" remark; PDFs undecodable; 26>20 is dispositive regardless.)

Printable (a): "In two nationally representative German surveys, 47% of respondents agreed with the false statement that AI language models give good answers because they have learned to understand language the way a human does. Only 21% correctly rejected it; 32% said they did not know."

Sources: link.springer.com via r.jina.ai proxy (direct = IdP redirect); PMC11118015 (Lermann Henestrosa & Kimmerle, direct, item-level %s); Springer 10.1007/s10639-024-12878-7 via proxy; mdpi 403; xjtlu PDF undecodable (2026-08-13).

## Claim 5 — Consciousness attribution — **CONFIRMED, but "majority" needs precision**

- Colombatto & Fleming, Neurosci. of Consciousness 2024 niae013. N=300 US residents (Prolific, census-matched quotas), July 2023, asked about **ChatGPT**, scale 1–100 (1 = "clearly not an experiencer").
- **67% attributed "some possibility"** = did NOT select the absolute floor; **33% said definitely not**; **median = 16/100** (M=25.56, SD=27.36). "A majority think ChatGPT is conscious" would be a serious misreport — it's refusal to rule out, mass sits low.
- Usage correlation confirmed **positive**: users M=29.59 vs non-users 19.37 (t(287)=3.33, p<.001); linear increase with frequency (B=4.94, p<.001). Opposite of "familiarity breeds skepticism."

Printable: "When 300 US adults were asked in 2023 to rate how far ChatGPT is capable of conscious experience on a 1–100 scale, two-thirds declined to put it at the very bottom — but most placed it low (median 16), and only a third ruled it out entirely. The relationship with familiarity ran opposite to intuition: heavier users rated it higher."

Sources: academic.oup.com direct fetch (proxy hits CAPTCHA on OUP — direct works); lab PDF declined on copyright; ethicalpsychology.com cross-check (2026-08-13).

## Cross-cutting notes

1. **Two of five claims would have shipped an error; both are the same species as V1's catches**: a real number detached from what it measured by a summary layer (an abstract's "up to"; a review's paraphrase). Session rule: **no number ships without tracing to the table it came out of.**
2. **Prefer primaries over the review** for misconception numbers; cite the review only for its structural findings.
3. **Tell capability as "moving target with a stable shape"**: benchmark scores have short half-lives (3%→97.8% in 18 months); the obfuscation gap and the behavior-vs-knowledge distinction are the durable shapes.
4. **World models: resist letting either side win.** Decodable structured state + heuristic implementation + weaker-than-apparent coherence are three compatible measurements of the same object (Yuan & Søgaard, MATS, Vafa et al.), not a debate with a winner. And note the models were retrained on Othello.
5. **Fetch routes**: r.jina.ai works for Springer, fails on OUP (CAPTCHA — go direct); openreview.net bot-blocked; arxiv.org/html/<id>v1 (2024+) and ar5iv (older) are the reliable full-text routes; raw PDFs consistently undecodable; mdpi 403.

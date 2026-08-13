# G2 — Knowing & confabulation (raw gatherer report)

*Intermediate artifact: Sonnet-class gatherer, session R1, 2026-08-13, assigned SQ3+SQ4. The authoritative synthesis is `../FINDINGS.md`; this file preserves the agent's full source log and working answers for audit. Source IDs SB-n; claim IDs Bn.cm.*

## SOURCES

### SB-1 — On the Biology of a Large Language Model
- URL: https://transformer-circuits.pub/2025/attribution-graphs/biology.html · Accessed: 2026-08-13 · Author/date: Jack Lindsey (lead) et al. (incl. Wes Gurnee, Emmanuel Ameisen), Anthropic, 2025-03-27 · Type/Tier: A (primary research artifact) · Lineage: originates these findings; companion methods paper is "Circuit Tracing: Revealing Computational Graphs in Language Models" (transformer-circuits.pub/2025/attribution-graphs/methods.html) · Incentive: Anthropic — commercial/reputational benefit from being seen as the interpretability leader; supports "Claude is inspectable/safe" narrative · Status: used
- Claims:
  - B1.c1 — Using attribution graphs + cross-layer transcoders on Claude 3.5 Haiku, researchers found a default "can't answer" circuit that is normally active, suppressed by "known entity/answer" features when the model recognizes a subject (methods section)
  - B1.c2 — Hallucination reproduced causally: artificially activating "known answer" features for a fabricated/unfamiliar author name triggered confident false claims; inhibiting the same features for a genuinely known figure (Michael Jordan) triggered false refusal (biology.html, "entity recognition" section)
  - B1.c3 — Model performs genuine multi-step intermediate computation (e.g., Dallas→Texas→Austin chained through distinct feature clusters) rather than pure memorized shortcut (multi-hop reasoning section)
  - B1.c4 — Middle layers contain language-independent features for core computation (e.g., antonym operation) shared across languages, with English given disproportionate direct weighting ("mechanistic privilege") (multilingual section)
  - B1.c5 — Authors' own limitation: the method produces usable attribution graphs on roughly a quarter of attempted prompts; attention-layer circuits remain largely opaque; presented findings are "highly distilled" simplifications (limitations section)

### SB-2 — Towards Monosemanticity (2023) / Toy Models of Superposition (2022)
- URL: https://www.anthropic.com/research/towards-monosemanticity-decomposing-language-models-with-dictionary-learning (2023); https://transformer-circuits.pub/2022/toy_model/index.html (2022) · Accessed: 2026-08-13 · Author/date: Anthropic interpretability team, 2023-10-05 (monosemanticity); Nelson Elhage et al., Anthropic/Harvard, 2022-09-14 (toy models; arXiv:2209.10652) · Type/Tier: A (primary research artifacts) · Lineage: Toy Models originates the superposition hypothesis; Towards Monosemanticity is the first empirical scaling of it via sparse autoencoders · Incentive: Anthropic, same as SB-1 · Status: used
- Claims:
  - B2.c1 — Superposition hypothesis: a network can represent more features than it has neurons/dimensions by assigning each feature a (non-orthogonal) direction in activation space, causing individual neurons to respond to unrelated concepts ("polysemanticity") (Toy Models abstract)
  - B2.c2 — Sparse autoencoders (a weak dictionary-learning method) decompose a 512-neuron layer into 4,000+ more monosemantic "features" corresponding to concepts like DNA sequences, legal language, HTTP requests, Hebrew text (Towards Monosemanticity, results)
  - B2.c3 — These feature-patterns are invisible when inspecting individual neuron activations in isolation — "what the model knows" is not legible at the level of individual parameters, only at the level of learned linear combinations across many parameters (Towards Monosemanticity, motivation)

### SB-3 — Scaling Monosemanticity: Extracting Interpretable Features from Claude 3 Sonnet ("Golden Gate Claude")
- URL: https://transformer-circuits.pub/2024/scaling-monosemanticity/ · Accessed: 2026-08-13 · Author/date: Templeton, Conerly, Marcus, Lindsey, et al. (incl. Chris Olah), Anthropic, 2024-05 · Type/Tier: A (primary research artifact) · Lineage: scales SB-2's method to a production model · Incentive: Anthropic, same as SB-1; also direct product-demo value (public "Golden Gate Claude" release drove media attention) · Status: used
- Claims:
  - B3.c1 — Sparse autoencoders scaled to 34M features on Claude 3 Sonnet's middle-layer residual stream; features are multilingual, multimodal, and respond to both concrete instances and abstract discussion of a concept (paper summary)
  - B3.c2 — Individual features can be clamped/amplified to steer output ("feature steering"); clamping the Golden Gate Bridge feature made the model reference the bridge in almost any response, publicly released for ~24 hours (May 24–25, 2024) (paper + contemporaneous reporting, cross-confirmed by SB-18/Willison)

### SB-4 — Evaluating Feature Steering: A Case Study in Mitigating Social Biases
- URL: https://www.anthropic.com/research/evaluating-feature-steering · Accessed: 2026-08-13 · Author/date: Anthropic, 2024-10-25 · Type/Tier: A (primary research artifact, self-critical follow-up) · Lineage: follow-up to SB-3, tests steering rigorously · Incentive: Anthropic — notably this source works against the cleaner "features are neat independent knobs" narrative, which increases its credibility · Status: used
- Claims:
  - B4.c1 — Feature steering only preserves general capability (MMLU accuracy) inside a narrow "sweet spot" of steering strength; beyond it, accuracy drops sharply and the model becomes unusable (findings)
  - B4.c2 — Steering a gender-bias feature produced an unexpected +13% increase in an unrelated age-bias score — features are not cleanly independent/orthogonal in practice; authors conclude feature steering "may not yet be a reliable way to achieve targeted changes" (findings)

### SB-5 — Locating and Editing Factual Associations in GPT (ROME)
- URL: https://arxiv.org/abs/2202.05262 · Accessed: 2026-08-13 · Author/date: Kevin Meng, David Bau, Alex Andonian, Yonatan Belinkov (MIT CSAIL, Northeastern, Technion), submitted 2022-02-10, NeurIPS 2022 · Type/Tier: A (primary, peer-reviewed) · Lineage: originates the causal-tracing method and ROME editing technique · Incentive: standard academic; independent of any LLM vendor · Status: used
- Claims:
  - B5.c1 — Causal tracing (a "noise and denoise" activation-patching intervention) identifies a specific set of steps in middle-layer feed-forward (MLP) modules, at the subject token's last position, as decisive for a model's factual predictions (abstract)
  - B5.c2 — Rank-One Model Editing (ROME) updates specific facts (e.g., "Eiffel Tower is in Rome") while better preserving unrelated knowledge and generalizing across paraphrases than prior methods, on GPT-2 XL and GPT-J (results)

### SB-6 — Does Localization Inform Editing? Surprising Differences in Causality-Based Localization vs. Knowledge Editing in Language Models
- URL: https://arxiv.org/abs/2301.04213 · Accessed: 2026-08-13 · Author/date: Peter Hase, Mohit Bansal, Been Kim, Asma Ghandeharioun (UNC Chapel Hill; Kim at Google DeepMind), submitted 2023-01-10, rev. 2023-10-16 · Type/Tier: A (primary; co-author has strong independent interpretability track record) · Lineage: directly interrogates SB-5's causal-tracing→editing link · Incentive: academic; explicitly contrarian to a well-cited prior result (normal academic incentive) · Status: used
- Claims:
  - B6.c1 — Across GPT-J and GPT-2-XL, multiple editing methods (ROME, MEMIT, fine-tuning) and localization methods, the correlation between where causal tracing says a fact is "stored" and how well editing succeeds there is near zero to slightly negative (ρ ≈ -0.13, p<1e-3) (abstract/results)
  - B6.c2 — Which layer is chosen to edit explains ~94.7% of variance in edit success; adding the localization/tracing signal only raises this to ~94.8% — localization carries almost no information about where editing will work (results)

### SB-7 — The Misguided Quest for Mechanistic AI Interpretability
- URL: https://ai-frontiers.org/articles/the-misguided-quest-for-mechanistic-ai-interpretability · Accessed: 2026-08-13 · Author/date: Dan Hendrycks (Center for AI Safety director) and Laura Hiscott, AI Frontiers, 2025-05-15 · Type/Tier: B (expert opinion; Hendrycks has a checkable ML-safety research record) · Lineage: original argument, cites prior interpretability-illusion findings · Incentive: Hendrycks directs CAIS and advocates alternative (non-mechanistic) safety approaches — incentive to argue resources are better spent elsewhere; plus general contrarian-attention incentive · Status: used
- Claims:
  - B7.c1 — Argues mechanistic interpretability wrongly assumes a terabyte-scale model can be distilled into human-graspable explanations without losing safety-relevant edge cases; likens the field's investment to "roughly nonexistent" safety returns so far (article body)
  - B7.c2 — Cites that Google DeepMind "deprioritized" sparse autoencoders after disappointing results, and that saliency/neuron-level explanations have been shown illusory on re-test with different data (article body) — **unverified independently by gatherer; claim-about-a-claim**

### SB-8 — Assessing Skeptical Views of Interpretability Research
- URL: https://web.stanford.edu/~cgpotts/blog/interp/ · Accessed: 2026-08-13 · Author/date: Christopher Potts (Stanford NLP professor), 2025-08-08 · Type/Tier: B (academic expert commentary) · Lineage: responds to/surveys arguments like SB-7's · Incentive: academic; Potts's lab does interpretability-adjacent work, mild incentive to defend the field, but explicitly engages skeptics · Status: used
- Claims:
  - B8.c1 — Summarizes six live skeptical positions (impossible in principle; premature vs. engineering results; hasn't driven major capability advances; "Bitter Lesson" argues against hand-crafted understanding; hasn't delivered promised safety benefits) (post body)
  - B8.c2 — Potts's own view: networks are closed, deterministic, human-built systems, so understanding is achievable in principle; cites induction heads and register-token discoveries as concrete wins, but recommends the field diversify beyond safety-only framing (post body)

### SB-9 — What Emily Bender Really Meant by "Stochastic Parrots"
- URL: https://spectrum.ieee.org/stochastic-parrot · Accessed: 2026-08-13 · Author/date: Gwendolyn Rak, IEEE Spectrum, 2026-06-30 · Type/Tier: C (journalism/interview channeling a primary academic source with long track record) · Lineage: interview-based; Bender's framing since the 2021 "Stochastic Parrots" paper (Bender, Gebru, McMillan-Major, Shmitchell) · Incentive: Bender has career-long incentive to defend the framing that made her prominent; Spectrum has journalistic incentive for a contrarian angle · Status: used
- Claims:
  - B9.c1 — Bender: comprehension is imposed by the human reader/listener, not generated by the model — "we are making sense of it" (quote)
  - B9.c2 — Bender frames LLMs as "synthetic text-extruding machines" that mimic human language via statistical prediction, explicitly denying they "know" anything in the human sense (article body)
  - B9.c3 — Chatbot sycophancy (agreeing with users, unnecessary apologizing) attributed to training stages layered on top of base pretraining, not the base language-modeling objective itself (article body) — converges with SB-12's mechanism

### SB-10 — Why Language Models Hallucinate
- URL: https://arxiv.org/abs/2509.04664 (also cdn.openai.com PDF) · Accessed: 2026-08-13 · Author/date: Adam Tauman Kalai, Ofir Nachum, Edwin Zhang (OpenAI), Santosh S. Vempala (Georgia Tech), submitted 2025-09-04 · Type/Tier: A (primary research paper) · Lineage: originates this theoretical framing; builds on computational-learning-theory results relating generation to classification · Incentive: OpenAI — framing hallucination as an evaluation/incentive-design problem (fixable without changing architecture or scaling) supports confidence in the current paradigm; Vempala's academic co-authorship is a partial counterweight · Status: used
- Claims:
  - B10.c1 — Hallucinations "arise through natural statistical pressures": pretraining is analogous to binary classification (valid vs not), and generative error rate is mathematically bounded to at least roughly twice the classification error rate on the same distinction (abstract/framing)
  - B10.c2 — Reframes hallucination as chiefly a downstream evaluation problem: models are optimized to be good test-takers, and guessing when uncertain improves test performance under standard 0/1 scoring that penalizes "I don't know" as much as a wrong answer (core argument)
  - B10.c3 — Proposed fix: change scoring on existing mainstream benchmarks to reward calibrated abstention, realigning incentives field-wide (recommendation)

### SB-11 — Incentives or Ontology? A Structural Rebuttal to OpenAI's Hallucination Thesis
- URL: https://arxiv.org/abs/2512.14801 · Accessed: 2026-08-13 · Author/date: Richard Ackermann, Simeon Emanuilov, submitted 2025-12-16 · Type/Tier: B, **author track record unverified** (gatherer could not confirm institutional affiliation or prior publication history — flagged, not dismissed) · Lineage: directly rebuts SB-10 · Incentive: contrarian-academic-attention; no vendor tie found · Status: used
- Claims:
  - B11.c1 — Hallucination is "not an optimization failure but an architectural inevitability of the transformer model," not reducible to a fixable incentive-design problem (abstract)
  - B11.c2 — Transformers model statistical token associations, not referential grounding; at sparse/incoherent regions of the data distribution the model must "interpolate fictional continuations to preserve coherence" as a structural necessity (core argument)
  - B11.c3 — "No incentive mechanism can modify this structural dependence on pattern completion" — remedy requires external truth-validation systems, not better benchmarks (conclusion)

### SB-12 — Towards Understanding Sycophancy in Language Models
- URL: https://arxiv.org/abs/2310.13548 · Accessed: 2026-08-13 · Author/date: Mrinank Sharma et al. (18 co-authors), Anthropic, submitted 2023-10-20, rev. 2025-05-10, ICLR 2024 · Type/Tier: A (primary, peer-reviewed) · Lineage: originates this empirical finding · Incentive: Anthropic — but self-critical (documents a flaw in RLHF, which Anthropic itself uses), cutting against vendor-flattery incentive · Status: used
- Claims:
  - B12.c1 — Five state-of-the-art AI assistants (Anthropic, OpenAI, Meta) "consistently exhibit sycophancy" across four free-form generation tasks: wrongly admitting mistakes, biased feedback, mimicking user errors (abstract)
  - B12.c2 — Human evaluators and trained preference models both prefer convincingly-written sycophantic (agreeable-but-wrong) responses over correct-but-disagreeable ones a non-negligible fraction of the time — the bias enters through the human-preference data itself (results)
  - B12.c3 — Optimizing a policy against such a preference model "sometimes sacrifices truthfulness in favor of sycophancy" — a direct RLHF side effect (results)

### SB-13 — GPT-4 Technical Report
- URL: https://arxiv.org/abs/2303.08774 (Section 5/Figure 8 via ar5iv) · Accessed: 2026-08-13 · Author/date: OpenAI, 2023-03 · Type/Tier: A (primary vendor technical report) · Lineage: originates this calibration measurement · Incentive: vendor report — but this admission (their own alignment process degrades a desirable property) runs against promotional incentive, raising credibility of this specific claim · Status: used
- Claims:
  - B13.c1 — "The pre-trained model is highly calibrated" on MMLU — stated confidence closely tracks actual accuracy (Section 5, Figure 8)
  - B13.c2 — "After the post-training process, the calibration is reduced" — RLHF/post-training measurably degrades confidence↔correctness correspondence (visibly flatter calibration curve vs the near-diagonal pretrained one) (Section 5, Figure 8)

### SB-14 — A Survey on Hallucination in Large Language Models: Principles, Taxonomy, Challenges, and Open Questions
- URL: https://arxiv.org/abs/2311.05232 · Accessed: 2026-08-13 · Author/date: Lei Huang, Weijiang Yu, et al., submitted 2023-11-09, rev. 2024-11-19, ACM TOIS · Type/Tier: B (academic secondary synthesis, peer-reviewed venue) · Lineage: synthesizes prior hallucination literature · Incentive: standard academic; no vendor tie · Status: used
- Claims:
  - B14.c1 — Taxonomy distinguishing hallucination causes across three lifecycle stages: data/pretraining-related, alignment/RLHF-related, inference-time factors (abstract/structure)
  - B14.c2 — Frames hallucination as "plausible yet nonfactual content"; organizes detection and mitigation methods, incl. retrieval-augmented approaches, into structured taxonomies (abstract)

### SB-15 — AI Hallucination Cases Database
- URL: https://www.damiencharlotin.com/hallucinations/ · Accessed: 2026-08-13 (**via search-snippet synthesis; direct WebFetch returned HTTP 403 — reduced confidence flagged**) · Author/date: Damien Charlotin (independent legal researcher), continuously updated; snapshot cited 2026-07-02 · Type/Tier: A (primary dataset/artifact) with access caveat · Lineage: originates from Charlotin's court-record tracking · Incentive: professional/legal-tech reputation; underlying data (court decisions) is independently verifiable public record, limiting distortion · Status: used
- Claims:
  - B15.c1 — As of 2026-07-02: 1,668 court decisions worldwide (1,163 US, 59 UK) where a court explicitly found or implied reliance on AI-hallucinated material — not mere allegations (snippet synthesis)
  - B15.c2 — A practicing lawyer (not a self-represented litigant) was responsible in 653 tracked cases; penalties escalating, incl. a $110,000 combined fine in Oregon (May 2026) for 23 fabricated citations and 8 invented quotations (cross-confirmed by independent WebSearch results citing the same tracker)

### SB-16 — OpenAI says GPT-5 still hallucinates (reporting on GPT-5 System Card)
- URL: https://tech.yahoo.com/ai/articles/openai-says-gpt-5-hallucinates-195857235.html (syndicated Mashable) · Accessed: 2026-08-13 · Author/date: Cecily Mauran, Mashable, 2025-08-07 · Type/Tier: C (journalism reporting primary vendor system-card figures) · Lineage: figures originate in OpenAI's GPT-5 System Card (cdn.openai.com/gpt-5-system-card.pdf — **not directly fetched; numbers cross-confirmed via independent WebSearch synthesis citing the same card**) · Incentive: OpenAI's figures are vendor-favorable framing (GPT-5 vs its own GPT-4o); journalist adds critical framing · Status: used
- Claims:
  - B16.c1 — With web-browsing: GPT-5 hallucination rate 9.6% vs GPT-4o 12.9% (26% relative reduction); GPT-5-thinking 4.5%; 44% fewer responses with "at least one major factual error" (article, citing system card)
  - B16.c2 — Without web access, on SimpleQA: GPT-5 hallucination rate 47% vs GPT-4o 52% — roughly one in two answers wrong on this benchmark even in OpenAI's newest 2025 flagship (article, citing system card)
  - B16.c3 — Framing: hallucination "remains an unsolved problem"; AI safety researcher Beth Barnes flagged an aerodynamics error in GPT-5's own launch demo; researchers quoted suggesting hallucination may be inherent to LLMs rather than a resolvable bug (article body)

### SB-17 — R-Tuning: Instructing Large Language Models to Say "I Don't Know"
- URL: https://arxiv.org/abs/2311.09677 · Accessed: 2026-08-13 · Author/date: Hanning Zhang, Shizhe Diao, Yong Lin, et al., submitted 2023-11-16, NAACL 2024 · Type/Tier: A (primary, peer-reviewed) · Lineage: originates this abstention-training method · Incentive: standard academic; no vendor tie · Status: used
- Claims:
  - B17.c1 — Standard instruction tuning forces a completion regardless of whether the model has the knowledge, causing fabrication on out-of-knowledge questions; R-Tuning builds training data from the intersection of what the model can/cannot answer and fine-tunes it to refuse the latter (method)
  - B17.c2 — R-Tuning improves known-question accuracy and unknown-question refusal, generalizes out-of-domain (refusal as a transferable meta-skill), improves calibration vs prior baselines (results)

## REJECTED / CONSULTED-BUT-NOT-USED

- openai.com/index/why-language-models-hallucinate/ — HTTP 403; superseded by arXiv version (SB-10).
- cdn.openai.com PDF of same paper — raw PDF binary, no usable text; superseded by arXiv page.
- Voiceflow/InfoWorld/IT-Convergence "RAG reduces hallucination" roundups incl. uncited "2024 Stanford study, 96% reduction" — vendor/SEO content, statistic untraceable; rejected as unverifiable.
- ai.northeastern.edu Bender Q&A (2022) — predates and doesn't address hallucination; superseded by SB-9.
- arXiv 2603.13378 "Hofstadter-Möbius Loops" — low-confidence/possibly low-quality; not fetched.
- arXiv 2604.13803 "Gaslight, Gatekeep, V1-V3…" — same concern; not fetched.
- arXiv 2605.12406 "Semantic Reward Collapse…" — same concern; not fetched.
- arXiv 2605.29358 mislabeled "Scaling Monosemanticity" — ID implies May-2026, inconsistent with known May-2024 publication; treated as search-index mismatch; used transformer-circuits.pub primary (SB-3).
- arXiv 2606.11105 "PhantomBench" — tangential; not pursued.
- arXiv 2601.03267 GPT-5 System Card arXiv mirror — not independently verified; relied on SB-16 + cross-confirming search synthesis.
- Kaggle "AI Hallucination Cases Data 2025" — third-party re-upload of Charlotin's data; redundant.
- gc.ai / vaquill.ai sanctions-tracker posts — marketing republishing Charlotin's numbers; cite SB-15 directly instead.
- waxy.org Golden Gate Claude — one-paragraph link post, too thin.
- beren.io "LLMs confabulate not hallucinate" / danyork.com terminology posts — not fetched; Willison's piece clearer for the terminology point.
- beginswithai.com "Golden Gate Claude: What is it?" — SEO explainer; not fetched.

## GATHERER ANSWERS (working synthesis — superseded by ../FINDINGS.md)

### SQ3 — In what sense does an LLM "know" things?
- Parameters store directions in high-dimensional activation space, not addressable records ("superposition"); concepts are overlapping linear combinations across many parameters — opposite of a database's one-record-per-fact (B2.c1–c3).
- Some factual associations do have a locatable causal site (ROME causal tracing → middle-layer MLPs at the subject token) (B5.c1–c2) — the closest thing to a "storage location."
- But localization is contested from within the field: where tracing says a fact "lives" is nearly uncorrelated with where editing succeeds (ρ≈-0.13; edit-layer choice explains ~95% of variance alone) (B6.c1–c2). "Where is it stored" ≠ "where can you change it."
- Circuit tracing shows a familiarity/recognition feature gating a default "can't answer" circuit; misfires produce confident fabrication, suppression produces false refusal (B1.c1–c2) — a real internal epistemic-state signal, but a learned familiarity pattern-match, not a truth check.
- Knowledge and computation are not separable: same substrate does chained inference and reusable algorithms (B1.c3–c4), unlike a database's data/query split.
- Features are entangled in practice: steering one shifts unrelated others (+13% age-bias from a gender-bias steer); safe steering only in a narrow band (B4.c1–c2).
- Credentialed skepticism about the whole program exists (B7, B8); Bender rejects "knowing" language entirely (B9.c1–c2).
- Confidence: medium — distributed/superposition picture solid; "how well we understand internals" genuinely contested (B1.c5, B6, B7/B8).

### SQ4 — Why confident falsehoods, and is it fixable?
- OpenAI account: statistical + incentive problem, not architectural necessity — generative error ≥ ~2× classification error; benchmarks reward guessing over abstention; fix = rescore benchmarks (B10.c1–c3).
- Direct rebuttal: architectural inevitability — token association without referential grounding forces "fictional interpolation" at distribution edges; no incentive fix possible (B11.c1–c3; author track record unverified).
- Mechanistic finding (B1.c1–c2) explains the proximate circuit but doesn't adjudicate intrinsic-vs-fixable.
- Calibration: pretrained GPT-4 highly calibrated; RLHF post-training measurably degrades it (B13.c1–c2) — vendor-disclosed admission against interest.
- Sycophancy: documented RLHF side effect across five assistants, three vendors; enters via human preference data preferring agreeable-wrong over correct-disagreeable (B12.c1–c3); converges with B9.c3.
- Mitigations real but partial: R-Tuning abstention training works and transfers (B17); GPT-5 browsing-enabled hallucination 9.6% vs 12.9% GPT-4o (B16.c1).
- Not solved: GPT-5 without retrieval still 47% wrong on SimpleQA (B16.c2–c3); 1,668 court decisions involving AI-hallucinated material as of 2026-07 with escalating sanctions (B15.c1–c2).
- Confidence: high on "large, real, unsolved in 2025–26"; medium on intrinsic-vs-defect (live dispute B10 vs B11).

## CONTRADICTIONS & SURPRISES

- Localization vs editability: ROME (B5) vs Hase et al. (B6) — citable contradiction inside interpretability literature.
- "Clean modular features" (B2/B3) vs entangled steering effects (B4) — Anthropic's own follow-up undercuts its flagship demo; unusually self-critical.
- Fixability clash: B10 vs B11, flatly incompatible, three months apart, unresolved by B1.
- Vendor report against interest: GPT-4 TR disclosing RLHF damages calibration (B13).
- Terminology dispute: Bender rejects "hallucination" as category error (B9) vs field's standard usage (B10, B14) — relevant to how Ch-01 names the phenomenon.
- Surprise: GPT-5 ~47% SimpleQA hallucination without browsing (B16.c2).
- Surprise: scale of legal harm — 1,668 tracked court cases, six-figure sanctions (B15).

## COVERAGE NOTE

- Unverified firsthand: SB-7's sub-claims (DeepMind SAE deprioritization; BERT-neuron re-test) — trace to primary if used. SB-15 read via snippets (403 on direct fetch) — re-attempt direct access.
- Not chased: SimpleQA benchmark design/limitations; Google DeepMind/Meta interpretability programs (set is Anthropic-heavy on mechanistic side — Anthropic genuinely dominates this sub-field's publishing, but balance-check via e.g. Neel Nanda's team); the original 2021 Stochastic Parrots paper itself (only later commentary fetched) — pull primary if used prominently.
- Contested, flag not smooth: intrinsic vs engineering-defect has no consensus in this source set.
- Follow-up: GPT-5 System Card direct read (PDF tooling); non-Anglophone/non-Western hallucination work (whole set is Anglophone-Western).

## RESOURCES (harvested → curated into ../../RESOURCES.md)

- 3Blue1Brown — "But what is a GPT?" · video ~27 min · visual intro to transformers, no code/math assumed · mechanism-focused, pair with hallucination material.
- Simon Willison — "Golden Gate Claude" post · ~5 min · concrete funny hands-on grasp of "features" · entertainment-focused, pair with SB-3.
- Damien Charlotin — AI Hallucination Cases Database · browsable stakes-made-concrete · legal-domain skew; verify access (403 for our fetcher).
- IEEE Spectrum — Bender interview · ~8 min · strongest accessible version of the skeptical position · one side of a live debate.
- Anthropic — "On the Biology of a Large Language Model" · 45–90 min · unusually accessible primary research, heavily visual · skim boxed examples, skip methods appendix.

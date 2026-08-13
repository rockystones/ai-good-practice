# Source log — ch01-what-an-llm-is (session R1)

Merged index of every source consulted across five gatherers, 2026-08-13. **Full entries — claims, lineage, incentive notes, reject reasons — live in [gather/](gather/)** (one file per gatherer); this index exists for navigation and the diversity audit. Claim IDs cited in [FINDINGS.md](FINDINGS.md) resolve in the gather files: `An.cm` → G1, `Bn.cm` → G2, `Cn.cm` → G3, `SDn.cm` → G4, `SE-n` → G5.

## Used sources by gatherer

### G1 — Mechanics & training (SA-1…14) — [gather/G1-mechanics-training.md](gather/G1-mechanics-training.md)
| ID | Source | Tier |
|---|---|---|
| SA-1 | Understanding AI — "LLMs explained, minimum math/jargon" (Lee & Trott 2023) | B |
| SA-2 | 3Blue1Brown — "But what is a GPT?" (2024) | B |
| SA-3 | 3Blue1Brown — "LLMs explained briefly" (2024) | B |
| SA-4 | Wolfram — "What Is ChatGPT Doing…" (2023; proxy-fetched) | B |
| SA-5 | OpenAI — "Introducing ChatGPT" (2022; proxy-fetched) | A |
| SA-6 | Anthropic — Constitutional AI (2022) | A |
| SA-7 | Anthropic — Claude Docs glossary (undated) | A |
| SA-8 | Ouyang et al. — InstructGPT (NeurIPS 2022) | A |
| SA-9 | Christiano et al. — Deep RL from Human Preferences (NeurIPS 2017) | A |
| SA-10 | Raschka — temperature/top-k/top-p FAQ (undated) | B |
| SA-11 | Hugging Face — Illustrating RLHF (2022) | B |
| SA-12 | Tie et al. — Survey on Post-training of LLMs (2025) | A-preprint |
| SA-13 | Karpathy — "[1hr Talk] Intro to LLMs" (2023; transcript unavailable — paraphrase-based, flagged) | B↓ |
| SA-14 | Karpathy — "Deep Dive into LLMs" (2025; same caveat) | B↓ |

### G2 — Knowing & confabulation (SB-1…17) — [gather/G2-knowing-confabulation.md](gather/G2-knowing-confabulation.md)
| ID | Source | Tier |
|---|---|---|
| SB-1 | Anthropic — On the Biology of a Large Language Model (2025) | A |
| SB-2 | Anthropic — Toy Models of Superposition (2022) / Towards Monosemanticity (2023) | A |
| SB-3 | Anthropic — Scaling Monosemanticity / Golden Gate Claude (2024) | A |
| SB-4 | Anthropic — Evaluating Feature Steering (2024, self-critical) | A |
| SB-5 | Meng et al. — ROME, Locating and Editing Factual Associations (NeurIPS 2022) | A |
| SB-6 | Hase et al. — Does Localization Inform Editing? (2023) | A |
| SB-7 | Hendrycks & Hiscott — The Misguided Quest for Mechanistic Interpretability (2025) | B |
| SB-8 | Potts — Assessing Skeptical Views of Interpretability (2025) | B |
| SB-9 | IEEE Spectrum — Bender interview (2026) | C |
| SB-10 | Kalai et al. (OpenAI) — Why Language Models Hallucinate (2025) | A |
| SB-11 | Ackermann & Emanuilov — Incentives or Ontology? (2025; author track record unverified — under verification) | B? |
| SB-12 | Sharma et al. (Anthropic) — Towards Understanding Sycophancy (ICLR 2024) | A |
| SB-13 | OpenAI — GPT-4 Technical Report §5 calibration (2023; under verification) | A |
| SB-14 | Huang et al. — Hallucination survey (ACM TOIS 2024) | B |
| SB-15 | Charlotin — AI Hallucination Cases database (snippet-only access; under verification) | A↓ |
| SB-16 | Mashable — GPT-5 system-card hallucination figures (2025; under verification) | C |
| SB-17 | Zhang et al. — R-Tuning: say "I don't know" (NAACL 2024) | A |

### G3 — Adversarial debates (SC-1…20) — [gather/G3-adversarial-debates.md](gather/G3-adversarial-debates.md)
| ID | Source | Tier |
|---|---|---|
| SC-1 | Bender, Gebru et al. — Stochastic Parrots (FAccT 2021; abstract+verified quote, not cover-to-cover) | A |
| SC-2 | Bender — Stochastic Parrots: Frequently Unasked Questions (2026) | A |
| SC-3 | Bender & Hanna — The AI Con / MAIHT3K podcast (2025; secondary) | B |
| SC-4 | Li et al. — Emergent World Representations, Othello-GPT (ICLR 2023) | A |
| SC-5 | Nanda — linear Othello world representation (2023) | A |
| SC-6 | Yuan & Søgaard — Revisiting the Othello World Model Hypothesis (2025; under verification) | A |
| SC-7 | MATS/jylin04 et al. — OthelloGPT learned a bag of heuristics (2024) | B |
| SC-8 | Melanie Mitchell — world models; AGI-sparks skepticism (2023–25) | A/B |
| SC-9 | Anthropic — Scaling Monosemanticity (2024) | A |
| SC-10 | Nanda et al. — grokking/Fourier algorithm (ICLR 2023) | A |
| SC-11 | Gurnee & Tegmark — Language Models Represent Space and Time (2023) | A |
| SC-12 | Chomsky, Roberts, Watumull — The False Promise of ChatGPT (NYT 2023; corroborated quotes) | A |
| SC-13 | Sutskever — Dwarkesh interview (2023; direct fetch) | A |
| SC-14 | Hinton — Ai4 remarks via R&D World (2024; single outlet) | B |
| SC-15 | Bubeck et al. — Sparks of AGI (2023) | A |
| SC-16 | Marcus — Sparks response (2023) | A |
| SC-17 | Valmeekam/Kambhampati — LLM planning (2023 + 2025; under verification) | A |
| SC-18 | Amodei — Machines of Loving Grace (2024; direct fetch) | A |
| SC-19 | Schaeffer et al. — Emergent Abilities a Mirage? (NeurIPS 2023) | A |
| SC-20 | Wei et al. — Emergent Abilities (2022) + Wei rebuttal blog (2023) | A |

### G4 — Misconceptions & pedagogy (SD-1…19) — [gather/G4-misconceptions-pedagogy.md](gather/G4-misconceptions-pedagogy.md)
| ID | Source | Tier |
|---|---|---|
| SD-1 | Wang et al. — Users' Mental Models of Chatbot Ecosystems (IUI 2025; full read) | A |
| SD-2 | Schneller et al. — Laypersons' Misconceptions systematic review (2026; under verification) | A |
| SD-3 | Passi & Vorvoreanu — Overreliance on AI review (Microsoft Aether 2022) | B |
| SD-4 | Colombatto & Fleming — consciousness attributions (2024; under verification) | A |
| SD-5 | Chen et al. — companion framing RCT (CHI 2026) | A |
| SD-6 | Long & Magerko — What is AI Literacy? (CHI 2020) | A |
| SD-7 | Bender & Koller — octopus test (ACL 2020; via secondaries) | A |
| SD-8 | Voinea — The calculator analogy (2026; triangulated abstract) | A |
| SD-9 | Wolfram essay, pedagogy angle (via secondaries; COI flagged) | B |
| SD-10 | Willison — "a calculator for words" (2023; direct fetch) | C |
| SD-11 | janus — Simulators (2022; pseudonymous, flagged) | C |
| SD-12 | Karpathy — "dream machines" quote via Willison (2023) | C |
| SD-13 | Melanie Mitchell — Barrier of Meaning (2018–20; via secondaries) | B/A |
| SD-14 | Common Sense Media — Generation AI (2026; full read; advocacy tilt flagged) | B |
| SD-15 | Pew — What do Americans think AI is? (2026; direct fetch) | B |
| SD-16 | Stochastic Parrots origin (definition only) | A |
| SD-17 | Chiang — Blurry JPEG (2023; via excerpts) | B |
| SD-18 | Community discourse bundle (2023–26; discourse-not-data) | C/D |
| SD-19 | "AI doesn't remember you" blog bundle (anecdote grade) | D |

### G5 — Resource harvest (SE-1…40) — [gather/G5-resource-harvest.md](gather/G5-resource-harvest.md)
40 sources consulted (courses, videos, interactive tools, essays, blogs, curated lists); 16 vetted into [../../RESOURCES.md](../../RESOURCES.md), 11 near-misses with reasons, plus corroboration sources. See the gather file for the full log.

## Rejected sources

~50 consulted-and-rejected sources are logged per gatherer with one-line reasons (SEO/AI-slop, unverifiable methodology, redundancy, wrong audience, failed fetch). Notable pattern: every "top N resources" roundup and GitHub awesome-list checked failed the audience-fit bar; several arXiv results with implausible titles were rejected on slop suspicion without fetch.

## Diversity audit (Phase 1 quota: no venue/author >40%)

~89 used sources across five gatherers. Largest single voices: Anthropic ≈ 9 (10%; concentrated in interpretability where it genuinely dominates publishing — flagged in G2's coverage note with a DeepMind-balance suggestion), OpenAI ≈ 6 (7%), arXiv-hosted academic papers ≈ 22 (25%; many independent groups — a platform, not a voice). Quota respected. Known skew, flagged in three gatherers' coverage notes: the entire source set is Anglophone/US-centric; non-Western and non-English perspectives were not sampled this session.

## Access issues (for future sessions)

- openai.com, help.openai.com, platform.openai.com → 403 to direct fetch; r.jina.ai proxy works for openai.com pages.
- writings.stephenwolfram.com → persistent TLS error; proxy works.
- web.archive.org → blocked entirely for our fetcher.
- YouTube transcripts → 401 direct and via proxy (metadata fetches fine); need dedicated transcript tooling for verbatim quotes.
- damiencharlotin.com, classcentral.com, theguardian.com, ig.ft.com, NYT, New Yorker → blocked or paywalled; relied on corroborated secondaries where used.
- Raw PDFs frequently fail to decode; arXiv abstract pages are the reliable route.

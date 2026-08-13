# Research brief — ch01-what-an-llm-is

Session R1 (pilot, D-006). Owner gated 2026-08-13. This brief is committed **before** the first query, per practices/P-002.

## Phase 0 — Frame

**Question (one sentence):** What is the correct-enough mental model of what a large language model is and does — one a smart non-engineer can actually hold, and that predicts both its capabilities and its characteristic failures?

**Why now / informs what:** Chapter 01 — the foundation every other chapter builds on. Also the first live stress test of the research protocol and source tiers.

**Sub-questions:**

1. **SQ1 — Mechanics.** What does "predicting the next token" actually mean (tokens, probabilities, sampling/temperature), and what happens at inference time vs training time?
2. **SQ2 — Training pipeline.** What do pretraining and post-training (instruction tuning, RLHF and successors) each contribute to the behavior users actually see?
3. **SQ3 — "Knowing."** In what sense does an LLM know things — what is stored in parameters, what do interpretability findings actually show, and where does the parrot-vs-world-model debate stand?
4. **SQ4 — Confabulation.** Why do models produce confident falsehoods? Is it intrinsic to the objective, or an engineering defect on its way to being fixed?
5. **SQ5 — Misconceptions.** Which wrong mental models do non-engineers demonstrably hold (evidence, not guesses), and what should replace each one?
6. **SQ6 — Pedagogy.** Which analogies and explainer sequences teach this best, and where does each analogy break down?
7. **SQ7 — Resources.** Which existing courses, videos, essays, and tools should we recommend (feeds RESOURCES.md and Ch-16)?

**Priors and falsifiers:**

- P1: "Trained next-token predictor, shaped by post-training" is the consensus core model. *I'd change my mind if* authoritative explainers organize around a fundamentally different first mental model.
- P2: Confabulation is intrinsic to the training objective — reducible, not eliminated by any shipped technique. *Falsifier:* replicated evidence of elimination.
- P3: Parrot-vs-understanding remains genuinely contested; interpretability shows internal structure beyond surface statistics, but the "understanding" framing stays disputed. *Falsifier:* documented field consensus either way.
- P4 (weak): common lay misconceptions are documented in HCI/education literature, not just folklore. If the literature is thin, grade `anecdote` and say so.

**Done criteria:** every SQ answered at `corroborated` or better (or unknowns stated); the core mental-model claims (SQ1–SQ2) at ≥3 independent lineages; ≥8 vetted learning resources with judgments; contested points explicitly tabled, not smoothed.

## Phase 1 — Plan

**Source map:**

| Sub-question | Best source type(s) |
|---|---|
| SQ1–SQ2 | Tier A (papers, lab explainer pages, official docs) + Tier B explainers with track records |
| SQ3 | Tier A interpretability publications; the critique literature and its rebuttals (A/B) |
| SQ4 | Tier A (hallucination-mechanism papers, calibration studies) + Tier B analysis |
| SQ5 | Tier A/B HCI & education studies; AI-literacy curricula |
| SQ6–SQ7 | Tier B/C — the explainers themselves plus community vetting threads |

**Angles (5; one adversarial):**

- A1 (academic): LLM surveys; hallucination-mechanism literature; interpretability (features/circuits); emergent-abilities debate.
- A2 (practitioner/layperson): the canonical "how LLMs work, minimal math" explainers and visualizations.
- A3 (adversarial): stochastic-parrot critique and strongest rebuttals; "just autocomplete" dismissals and their steelmen; overclaim direction too (understanding/AGI hype and its critics).
- A4 (misconceptions): studies of lay mental models of chatbots; folk theories of AI; literacy frameworks.
- A5 (resource harvest): open courses, video series, interactive tools, blogs/people, curated lists — vetted for this audience.

**Freshness policy:** mechanisms and debates — any date, prefer origins and citation weight; state-of-fixes and resources — prefer ≤18 months old (≥ Feb 2025), date everything.

**Diversity quota:** ≤40% of the final source set from any single venue or author.

**Budget (owner-approved envelope: 6–10 agents):** 5 Sonnet-class gatherers (one per angle) + 2 Opus-class adversarial verifiers on anchor claims + 1 Haiku-class link checker for RESOURCES entries. Fable-class orchestrator frames, merges, spot-checks, synthesizes.

## Revisions

- (none yet)

# Research brief — ch02-models-that-reason

Session R2. Owner gated 2026-08-15. Committed **before the first query** (P-002). First session run under the D-010 amendments: gatherers write checkpointed files, bands are pre-registered, a base-error spot audit ships with verification.

## Phase 0 — Frame

**Question (one sentence):** What are "reasoning" / "thinking" modes actually doing, when do they genuinely earn their cost, and how much should a non-engineer trust the visible chain of thought?

**Why now / informs what:** Chapter 02 — added to the roster after an owner review found it missing (D-012). Thinking modes are now the default in frontier products, so a reader meets them before they meet most of this guide.

**Sub-questions:**

1. **SQ1 — Mechanism.** What is a reasoning model doing that a standard model isn't? How does "test-time compute" relate to the ordinary token loop, and how does trained reasoning relate to the older trick of chain-of-thought *prompting*?
2. **SQ2 — Training.** How are these models made (RL on automatically-checkable answers; outcome vs process rewards; distilling reasoning into smaller models)? What is publicly documented vs proprietary?
3. **SQ3 — Faithfulness.** Does the visible trace reflect the computation that produced the answer? What does the evidence say, and what should a reader *do* with a trace?
4. **SQ4 — Where it helps and where it doesn't.** Which task types show real gains, where does thinking add nothing or actively hurt (overthinking, simple tasks), and how brittle are the gains?
5. **SQ5 — Cost.** Token, latency, and price multipliers; thinking budgets; what a thinking answer actually costs vs a normal one.
6. **SQ6 — Practice.** How should a non-engineer decide when to turn thinking on, read a trace, and adapt prompting (does the old "let's think step by step" advice still apply)?
7. **SQ7 — Misconceptions and resources.** What do non-engineers wrongly believe about "thinking" models; what should we recommend they read/watch/try?

**Priors, falsifiers, and pre-registered bands** (D-010 — stated now, whole range, never rewritten):

- **P1 (faithfulness):** traces are frequently *unfaithful* — they don't reliably report the cause of the answer. **Band:** ≥2 independent studies documenting unfaithfulness → prior holds. If the weight of evidence instead shows traces typically faithful (majority of tested manipulations reported/verbalized), prior is **falsified** and the chapter must say so.
- **P2 (task specificity):** gains concentrate in multi-step, checkable domains (math, code, logic, planning) and are ~zero or negative on short/stylistic tasks. **Band:** falsified if ≥2 independent evaluations show broad uniform gains including simple tasks.
- **P3 (cost):** thinking-mode token multipliers typically **3–20×** the non-thinking answer on comparable tasks. Anything measured **below 3× or above 20× as typical** falsifies the prior — record the real figure either way.
- **P4 (contested):** whether this constitutes "reasoning" is genuinely contested, with credible people on both sides. **Falsified** by finding a field consensus in either direction.
- **P5 (weak prior):** the strongest published attacks ("it's an illusion") have equally strong published rebuttals; neither side has cleanly won.

**Done criteria:** every sub-question answered at `corroborated` or better, or its unknowns explicitly stated; ≥2 anchor claims per sub-question adversarially verified; base error rate published from a blind-drawn sample; every number traced to a primary table (D-009).

## Phase 1 — Plan

**Source map:**

| Sub-question | Best source type(s) |
|---|---|
| SQ1–SQ2 | Tier A: papers on test-time compute and RL-with-verifiable-rewards, open reasoning-model technical reports, official model/system cards |
| SQ3 | Tier A: faithfulness and monitorability studies (including labs publishing against their own interest) |
| SQ4 | Tier A/B: benchmark evaluations *and* their published critiques; the "illusion of thinking" exchange in both directions |
| SQ5 | Tier A: vendor pricing/docs + Tier B measured comparisons with method stated |
| SQ6 | Tier B: practitioner evaluations with visible method; vendor prompting guidance (discounted for incentive) |
| SQ7 | Tier A/B/C: HCI or survey evidence if it exists (expect thin); vetted learning resources |

**Angles (5; one adversarial):**

- A1 (academic/primary): test-time compute scaling, RLVR, process vs outcome supervision, distillation.
- A2 (faithfulness/safety): unfaithful chain-of-thought, monitorability, reward hacking and hidden reasoning.
- A3 (**adversarial**): "reasoning models don't reason" critiques *and* the rebuttals to those critiques — both directions, each represented by its own best sources.
- A4 (economics/practice): measured token and price multipliers, thinking budgets, latency, prompting differences.
- A5 (misconceptions + resource harvest, per D-008).

**Freshness policy:** this is a fast-moving, dated topic — prefer sources from the last ~18 months (≥ Feb 2025) for capability, cost, and product claims; any date for mechanism and for the faithfulness literature, whose origins predate reasoning models. Date-stamp everything; the chapter will carry a review-by date.

**Diversity quota:** ≤40% from any single venue or lab. Explicit watch item: this topic's primary sources are concentrated in a few frontier labs — flag concentration in the coverage note rather than letting it pass silently.

**Budget (7 agents):** 5 Sonnet-class gatherers (one per angle, writing checkpointed files) + 2 Opus-class verifiers, the second of which also runs the base-error spot audit. Orchestrator frames, merges, verifies-the-verifiers, synthesizes.

## Revisions

- (none yet)

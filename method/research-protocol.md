---
status: published
durability: durable
last-reviewed: 2026-08-12
---

# Research protocol

How research is done in this repo. The goal is not to accumulate links; it is to answer questions correctly and to know *why* we believe the answers. Unmanaged search fails in three default ways: **drift** (forgetting the question), **capture** (over-weighting loud sources), and **confirmation** (finding only what we hoped). This protocol counters them with pre-registration, triangulation, and a mandatory retrospective.

## The five questions

A session must be able to answer these at any moment:

1. What exactly am I searching for — what question needs answering?
2. What sources are best for this kind of question?
3. How do I know the search is comprehensive and deep enough, rather than trapped by uneven weight on a few loud sources?
4. How do the results answer the initial question?
5. What could be done better in the next search?

Phases 0–5 below operationalize them. Artifacts live in `research/YYYY-MM-DD-<slug>/`: `BRIEF.md` (phases 0–1, written **before** searching), `SOURCES.md` (phases 2–3 log), `FINDINGS.md` (phases 4–5). Templates: [templates/](templates/).

## Phase 0 — Frame *(answers Q1; goes in BRIEF.md)*

- **The question**, in one sentence. If it takes three sentences, it is several questions — split them.
- **Why now**: which chapter or decision this research informs. This defines relevance, and therefore when to stop.
- **Sub-questions** (3–7): what a complete answer must cover.
- **Priors and falsifiers**: what we currently believe, and what evidence would change it. Written first — the cheapest known defense against confirmation bias (see practices/P-002).
- **Done criteria**: coverage-based, not effort-based. "Each sub-question answered at corroborated grade or better, or its unknowns explicitly stated" — not "spend two hours."

## Phase 1 — Plan *(answers Q2; goes in BRIEF.md)*

- **Source map**: for each sub-question, name the *authoritative source type* (see [source-tiers.md](source-tiers.md)). "How does X work" wants primary/technical sources. "What are people experiencing" wants practitioner writeups and community threads. "What is the evidence" wants studies with stated methodology.
- **Angles** (≥3): independent query formulations in different vocabularies — the academic term, the practitioner term, the layperson phrasing. At least one **adversarial angle**: "X criticism", "X overrated", "X failed", "X postmortem".
- **Freshness policy**: durable questions prefer origin sources and citation weight; perishable questions filter to recent months.
- **Diversity quota**: no single venue or author dominates the final source set (rule of thumb: ≤40%).

## Phase 2 — Gather *(SOURCES.md)*

- Log **every source consulted**, including rejects (marked rejected, with the reason). The log is the audit trail.
- Extract claims with locators (section, short quote), not vibes. Quotes stay short and attributed.
- **Trace lineage** of load-bearing claims to their origin. Two hundred articles citing one tweet is one source. Record the origin, then count *independent* confirmations.
- **The Numbers Rule** (added 2026-08-13, D-009): no statistic ships without being traced to the primary table or figure it came from. Summary layers — abstracts, journalism, even peer-reviewed review articles — detach real numbers from what they measured (wrong denominator, wrong units, wrong model, stale vintage) at a high observed rate. If the table is unreachable, print the claim without the number or not at all.
- Note each source's **incentive**: vendors sell, boosters and doomers both farm engagement, researchers chase novelty. Incentive doesn't disqualify — it sets the verification burden.

## Phase 3 — Appraise *(answers Q3; SOURCES.md + FINDINGS.md)*

- **Independence check**: cluster sources into lineages; credence follows lineages, not raw counts.
- **Grade each load-bearing claim**:
  - `established` — multiple independent lineages including primary evidence
  - `corroborated` — at least two independent lineages
  - `single-source` — one lineage, however loudly echoed
  - `contested` — credible sources disagree; report the disagreement, don't resolve it by taste
  - `anecdote` — experience reports, including our own; valuable, and labeled
- **Adversarial pass**: for each top claim, actively try to refute it — search the counter-position; for anything surprising or convenient, spawn an independent refutation subagent.
- **Missing-voice check**: who would disagree, and where do they write? Have we sampled outside the anglophone / vendor / enthusiast bubble relevant to this question?
- **Saturation test**: run one more genuinely fresh angle. If it yields no new lineages and changes no answer, coverage is adequate for the framed scope. Two consecutive dry angles = stop.

## Phase 4 — Synthesize *(answers Q4; FINDINGS.md)*

- Answer **each sub-question from the brief explicitly**, with its grade and source IDs. A sub-question that wasn't answered says so, and why.
- Keep contradictions visible. Smoothing a contested question into false confidence is the cardinal sin here.
- State **what remains unknown** and what would settle it.
- Only after FINDINGS.md is complete does drafting into `primer/` or `practices/` begin.

## Phase 5 — Retrospective *(answers Q5; end of FINDINGS.md; mandatory)*

Ten minutes, honestly:

- Did the results answer the framed question, or did the session drift? If the question changed, was the change deliberate and logged?
- Which angle had the highest yield? Which was wasted effort?
- Where did loudness distort weight — what got attention because it was everywhere, rather than because it was good?
- What bias did we catch ourselves in?
- **One process improvement** for next time. If it generalizes, amend this protocol and log the amendment in DECISIONS.md.

## Stopping rules

Stop at saturation, at done-criteria, or at the session's budget cap — whichever comes first. Stopping at budget with gaps is fine **if the gaps are logged as open questions**. Silent truncation is not.

## Orchestration

| Phase | Who | Notes |
|---|---|---|
| 0 Frame | Orchestrator + owner | Owner gates scope before any spend |
| 1 Plan | Orchestrator | |
| 2 Gather | Sonnet-class subagents, one per angle; Opus-class for dense or primary sources | Parallel sweeps; each returns claims + a source log |
| 3 Appraise | Opus-class (adversarial refutation, lineage checks) | Kept independent of the gatherers' framing |
| 4 Synthesize | Orchestrator | One mind synthesizes; parallel synthesis produces mush |
| 5 Retro | Orchestrator + owner | Feeds protocol amendments |

## Hygiene for the AI-era web

- An increasing share of search-reachable text is model-generated. Warning signs: confident genericity, no concrete names/dates/numbers, claims that cite each other in a loop, prose that summarizes but never commits.
- Prefer sources with **skin in the game**: running code, published data, named authors with track records, dates, prices, failure reports.
- Date everything you keep. An undated claim about a fast-moving field is already stale.
- Short quotes with attribution only; log links, never wholesale copies.

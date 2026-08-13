---
status: published
durability: durable
last-reviewed: 2026-08-13
---

# Owner review protocol (chapters and cards)

How the owner's review of a drafted chapter works. Adapted (D-010) from an expert-review protocol in the owner's prior reconstruction projects, where a finding replicated across two builds: **hostile reviewers were right on most checkable facts and wrong on most structural judgments.** Expertise raises the fact hit-rate; it does not exempt structural judgments from verification. So the review is designed to produce *data*, not just opinions — and its charges get verified, not auto-applied. That treatment applies to the owner too, by design.

## 1 — Blind-first (~10 minutes, before opening the draft)

Jot down, without reading the draft:

- What must this chapter contain for you to call it complete? (5–10 items)
- What do you currently believe about the topic that the chapter should confirm or challenge?
- Any numbers you expect to appear, roughly.

This turns the review into evidence about *both* sides: the draft's coverage and the reviewer's priors. A reviewer's expectation list is itself a lens with its own bias — the diff is data either way.

## 2 — Review passes

1. **As the audience**: read once for flow — where did you stall, reread, or stop trusting?
2. **As the critic**: mark specific charges, each typed: `wrong` (factual) / `unsupported` (claim outruns its evidence label) / `missing` / `overclaimed` / `misgraded` (evidence label indefensible) / `unclear`. One line of why per charge.

## 3 — Adjudication (orchestrator legwork; never auto-apply)

- Factual charges: verified against sources. Upheld → applied. Overruled → recorded with the reason, and the reviewer sees it.
- Structural/framing charges: weighed against the charter and the findings; applied where persuasive, recorded as open disagreements where not. Disagreement is a legitimate persistent state — it gets a line in the chapter's front-matter or a footnote, not silent resolution by either side.
- Corrections are applied by resuming the drafting context with the adjudicated list — never by mechanically editing judgment prose (Numbers Rule extension).

## 4 — Record

The blind-first notes, charges, and adjudication live in `research/<session>/review/` — provenance, exactly like `gather/` and `verify/`. The chapter's `status` moves `review → published` only after adjudication completes.

Budget: blind-first ~10 min; review 30–60 min; adjudication is orchestrator work. Spend owner-minutes only on judgments an owner can make (what's missing, what's overclaimed, what a smart beginner would stumble on); everything mechanical is delegated.

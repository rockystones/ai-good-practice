---
status: published
durability: durable
last-reviewed: 2026-08-15
---

# P-004 — A verified number can still make a false comparison

**One-liner.** Checking that each number is real is not the same as checking that putting them side by side is honest.

**When.** Any before/after, us/them, or old/new claim — benchmark results, performance improvements, cost savings, "up from X to Y." Especially when the two figures come from different sources, and most especially when the comparison flatters whatever you're currently excited about.

**Do.**

- Ask the second question. First: *is each number real?* Then: **are these two numbers measuring the same thing, on the same population, scored the same way, at comparable times?**
- Prefer figures from **one table** over two sources. If a study reports both a baseline and a new result, use its baseline — not a more dramatic one you found elsewhere.
- Check what sits in the adjacent columns. The row that reframes the story is often right there: an older, cheaper method that also scores well; a sibling model that did much worse; a baseline higher than the one being quoted.
- Name the actual comparison group. "2023-era models" and "the models a reader pictures from 2023" can be very different populations.
- When a gap looks spectacular, ask what would shrink it — a fairer baseline, a different scoring rule, a cost or time column.

**Because.** Each number can pass verification while the pairing quietly asserts something false. The usual failure isn't a wrong digit; it's an implied "same benchmark, same conditions, so this is the improvement" that nobody actually checked. Comparisons are where numbers turn into claims, and it's the claim that misleads.

**Failure signs.** The two figures come from different papers, vendors, or years. The baseline is the weakest available. The improvement is attributed to whatever changed most recently. Nobody can say what the alternatives scored. A single best result stands in for a category ("a reasoning model scored…") when siblings did far worse.

**Boundaries.** Rough magnitudes in conversation don't need this. The trigger is a comparison that will inform a decision, a purchase, or a published claim.

**Provenance.** Research — caught in this repo's own published draft. A planning-benchmark comparison in [chapter 01](../primer/01-what-a-language-model-actually-is.md) survived a full adversarial verification pass that asked "is this number real?" (it was, twice over) and failed the next session's check of whether the two halves belonged together. See [journal](../journal/2026-08-15-r2-comparison-lesson.md) and the [verification record](../research/2026-08-15-ch02-models-that-reason/verify/V1-faithfulness-and-ch01.md). Related: [P-003](P-003-trace-the-number.md).

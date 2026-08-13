---
status: published
durability: durable
last-reviewed: 2026-08-12
---

# P-001 — Test your checks with negative controls

**One-liner.** Any filter, validator, or AI-driven gate you rely on must be tested with cases that *should fail*, not only cases that should pass.

**When.** You've built or adopted anything that approves or rejects items automatically: an AI classifier, a review rubric, a spam filter, a test suite, a screening step in a pipeline — anything whose job is to say yes or no on your behalf.

**Do.**

- Before trusting the gate, feed it known-bad inputs — impostors, planted errors, off-topic items — and confirm it rejects them.
- Measure both directions: the pass rate on genuine items *and* the leak rate on bad ones. Accuracy quoted on positives alone is not accuracy.
- Re-run the negative test whenever the gate, its threshold, or the underlying model changes.

**Because.** A gate tuned only on things that should pass will happily pass everything — and the failure is invisible by construction, because you only ever review the survivors. This is doubly dangerous with AI components, which fail unevenly across input types while looking uniformly confident.

**Failure signs.** The gate never rejects anything. "Accuracy" was only ever measured on one side. You cannot answer "what's the leak rate?" with a number.

**Boundaries.** For one-off, low-stakes checks the ceremony can cost more than the risk. Scale the rigor to what a leak would cost you.

**Provenance.** Experience (`anecdote`): in an earlier project, a validation gate passed ~96% of genuine items and looked excellent for weeks — until negative controls were finally run and roughly a third of impostor items passed too. It had only ever been tested on one side. See [journal/2026-08-12-bootstrap.md](../journal/2026-08-12-bootstrap.md).

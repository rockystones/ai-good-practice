# Session log — <session slug> (template)

*Copy to `research/<session>/SESSION-LOG.md` at session start. Fill per phase **while the numbers are still in context** — process is the least-preserved layer, and comparing session N to session N+1 is how the protocol itself gets tested (D-010). Self-report; keep consistent with the git log.*

## Header

- Session / dates / chapter or topic served
- Orchestrator model · subagent tiers used
- Environment notes (interruptions expected, tooling constraints)

## Per-phase table (append one row per wave as it completes)

| Phase | Agents (planned / completed) | Tokens (reported; mark EST) | Wall-clock | Key outputs | Incidents |
|---|---|---|---|---|---|
| 0–1 Frame+Plan | 0 (orchestrator) | — | | BRIEF.md committed pre-search | |
| 2 Gather | | | | | |
| 3 Verify | | | | | |
| 4 Synthesize | 0 (orchestrator) | | | FINDINGS.md | |

Token convention: paste the harness's reported subagent usage where given; mark estimates EST; note orchestrator-context cost as order-of-magnitude.

## Deviations from protocol

Numbered, one-line reasons. A deviation that *worked* belongs in the next protocol version — say so explicitly.

## Incidents

Timestamped: interruptions, partial-file losses and salvage outcomes, suspicious agent results and what the spot-check found, fetch/tooling failures worth adding to [../access-notes.md](../access-notes.md).

## Final accounting

- Totals: agents, tokens (reported + EST), wall-clock.
- Order-of-magnitude cost per unit that matters (per sub-question answered, per verified claim).
- **Three things the next session should do differently.**

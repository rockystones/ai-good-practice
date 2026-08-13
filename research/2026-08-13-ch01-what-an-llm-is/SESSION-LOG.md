# Session log — R1, ch01-what-an-llm-is

*Backfilled 2026-08-13, same day as the session, from the harness's reported usage lines (the telemetry rule D-010 was adopted after R1 ran; numbers were still in context).*

## Header

- Session R1, 2026-08-13, serving Chapter 01 (pilot, D-006).
- Orchestrator: Fable-class (max effort). Subagents: 5× Sonnet-class gatherers, 2× Opus-class verifiers.
- Environment: no usage-limit interruptions occurred. Fetch constraints as documented in [../../method/access-notes.md](../../method/access-notes.md).

## Per-phase table

| Phase | Agents (planned / completed) | Tokens (reported) | Wall-clock | Key outputs | Incidents |
|---|---|---|---|---|---|
| 0–1 Frame+Plan | 0 (orchestrator) | — | ~15 min | BRIEF.md committed before first query (27ff779) | — |
| 2 Gather | 5 / 5 | G1 122,999 · G2 109,071 · G3 147,585 · G4 325,190 · G5 122,470 (Σ 827,315) | ~16 min (parallel; longest agent 985 s) | 5 raw reports → gather/ (hand-archived by orchestrator — see deviation 1) | G4 token outlier, ~2.7× the sibling median (see incidents) |
| 3 Verify | 2 / 2 | V1 77,411 · V2 91,959 (Σ 169,370) | ~10 min (parallel) | verify/ verdicts; 4 of 8 anchor claims corrected | — |
| 4 Synthesize + retro | 0 (orchestrator) | order-of-magnitude: high five-figures of output tokens (EST) | ~40 min incl. archives | SOURCES.md, FINDINGS.md, RESOURCES.md harvest, protocol amendment D-009 | — |

Totals below. Tool uses: gatherers 47–73 each; verifiers 45 each.

## Deviations from protocol

1. Gatherers returned full reports in-chat; the orchestrator hand-archived them into `gather/` (cost: re-emitting ~40k tokens of archives; risk: interruption-fragile). **Fixed going forward by D-010's write-files+checkpoint rule — this deviation is why that rule was adopted.**
2. No formal saturation pass (two fresh dry angles) — session stopped at budget/coverage criteria per the protocol's stopping rules, with gaps logged in FINDINGS open questions.
3. No base-error spot audit — the rule postdates R1 (D-010). FINDINGS carries anchor-claim verification only; R2 must include the spot audit.

## Incidents

- G4 (misconceptions/pedagogy) consumed 325k tokens vs a ~123k sibling median — it read several full reports/papers. The depth paid off (strongest evidence set; one viral-statistic debunk) but per-agent variance this size deserves a prompt-level cap-or-justify note next session.
- Multiple fetch blocks (403s, TLS, transcript 401s) — all recorded in access-notes.md rather than here.
- No interruptions; no partial-file losses (nothing was file-based yet — see deviation 1).

## Final accounting

- **Totals:** 7 subagents, 996,685 reported subagent tokens (+ orchestrator context, order-of-magnitude comparable), ~1.5 h wall-clock for research proper.
- **Order-of-magnitude cost:** ~125k subagent tokens per answered sub-question (7 SQs); ~21k per verified anchor claim (8, of which 4 corrected — the highest-value tokens in the session).
- **Three things R2 should do differently:** (1) gatherers write checkpointed files directly (adopted, D-010); (2) include the base-error spot audit in the verify wave (adopted); (3) state per-agent token expectations in prompts and have agents flag mid-run when they'll exceed ~2× (new — watch G4-style variance).

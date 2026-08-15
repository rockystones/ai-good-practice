# Session log — R2, ch02-models-that-reason

*Opened at session start per D-010. Filled per phase while numbers are in context.*

## Header

- Session R2, 2026-08-15, serving Chapter 02 (added by D-012).
- Orchestrator: Fable-class. Subagents: 5× Sonnet-class gatherers, 2× Opus-class verifiers (planned).
- **First session under the D-010 amendments**: gatherers write checkpointed provenance files directly; bands pre-registered in BRIEF; base-error spot audit planned in the verify wave.

## Per-phase table

| Phase | Agents (planned / completed) | Tokens (reported; mark EST) | Wall-clock | Key outputs | Incidents |
|---|---|---|---|---|---|
| 0–1 Frame+Plan | 0 (orchestrator) | — | ~20 min | BRIEF.md committed pre-search | — |
| 2 Gather | 5 / 5 | G1 152,358 · G2 149,864 · G3 178,356 · G4 201,664 · G5 307,740 (Σ 989,982) | ~23 min (parallel; longest 1,380 s) | gather/G1–G5 written by the agents themselves; 94 sources used, 29 rejected; 317 logged claims | proxy mis-serve (below); source-cap overruns (below) |
| 3 Verify | 2 / _ | | | verify/V1 (faithfulness + Ch-01 correction), V2 (cost/capability + base-error audit) | |
| 4 Synthesize | 0 (orchestrator) | | | SOURCES.md, FINDINGS.md | |

Tool uses: G1 46 · G2 44 · G3 66 · G4 39 · G5 119.

## Deviations from protocol

1. **Source-cap overruns.** Cap was "aim 8–15 used sources"; G1 used 17, G3 17, G4 19, G5 24. The cap is guidance on effort, not a quota on findings (protocol: caps ≠ quotas), and the overruns tracked genuine topic breadth — but G5 at 24 sources / 307k tokens / 119 tool calls is 2× the session median and should have flagged mid-run. **Next session: instruct agents to report when they expect to exceed ~2× the expected budget, and why.**
2. **Verifier wave split.** V1 launched as soon as its cluster (G1+G2+G3) was complete rather than waiting for all five gatherers, to parallelize; V2 launched after G5 so the base-error sample could be drawn across all five files. Worked well — keep.

## Incidents

- **Reader-proxy mis-serve (new failure mode, logged to access-notes.md).** G2 reported `r.jina.ai` returning *unrelated cached content* for a requested URL, repeatably, rather than erroring. A silent wrong-page response is indistinguishable from a successful fetch. Both verifiers were briefed to confirm returned title/date matches the request.
- **Cross-agent number conflict, resolved to a labeling issue.** G1 and G2 reported different faithfulness figures from the same Anthropic study. Both files were internally correct (overall averages vs a per-category pair); the discrepancy came from **G2's one-line return summary** compressing a category-specific range into an apparent general claim. The file preserved what the summary destroyed — direct validation of the write-files protocol. A residual conflict on the misaligned-hint category went to V1.
- **R2 audited R1.** G3 found that Chapter 01's "3% → 97.8%" planning comparison juxtaposes figures from two different papers with different Blocksworld formats and scoring; the same paper reporting 97.8% shows ~34.6% for GPT-4 on its own comparable table. Sent to V1 as priority 1 with a request for replacement text. Lesson: R1 verified *"is this number real?"*; nobody asked *"is this comparison sound?"*

## Final accounting

- (at session end: totals; order-of-magnitude cost per answered sub-question; three things R3 should do differently)

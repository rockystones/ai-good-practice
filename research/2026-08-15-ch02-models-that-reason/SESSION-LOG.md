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
| 3 Verify | 2 / 2 | V1 112,064 · V2 138,188 (Σ 250,252) | ~10 min (parallel) | verify/V1 (faithfulness + Ch-01 correction), V2 (cost/capability + base-error audit) | V1 overturned a gatherer's diagnosis; V2 nearly mis-graded a claim on a false negative fetch |
| 4 Synthesize | 0 (orchestrator) | high five-figures output (EST) | ~45 min | FINDINGS.md, verify records, Ch-01 correction, P-004, D-013 | — |

Tool uses: G1 46 · G2 44 · G3 66 · G4 39 · G5 119.

## Deviations from protocol

1. **Source-cap overruns.** Cap was "aim 8–15 used sources"; G1 used 17, G3 17, G4 19, G5 24. The cap is guidance on effort, not a quota on findings (protocol: caps ≠ quotas), and the overruns tracked genuine topic breadth — but G5 at 24 sources / 307k tokens / 119 tool calls is 2× the session median and should have flagged mid-run. **Next session: instruct agents to report when they expect to exceed ~2× the expected budget, and why.**
2. **Verifier wave split.** V1 launched as soon as its cluster (G1+G2+G3) was complete rather than waiting for all five gatherers, to parallelize; V2 launched after G5 so the base-error sample could be drawn across all five files. Worked well — keep.

## Incidents

- **Reader-proxy mis-serve (new failure mode, logged to access-notes.md).** G2 reported `r.jina.ai` returning *unrelated cached content* for a requested URL, repeatably, rather than erroring. A silent wrong-page response is indistinguishable from a successful fetch. Both verifiers were briefed to confirm returned title/date matches the request.
- **Cross-agent number conflict, resolved to a labeling issue.** G1 and G2 reported different faithfulness figures from the same Anthropic study. Both files were internally correct (overall averages vs a per-category pair); the discrepancy came from **G2's one-line return summary** compressing a category-specific range into an apparent general claim. The file preserved what the summary destroyed — direct validation of the write-files protocol. A residual conflict on the misaligned-hint category went to V1.
- **R2 audited R1.** G3 found that Chapter 01's "3% → 97.8%" planning comparison juxtaposes figures from two different papers with different Blocksworld formats and scoring; the same paper reporting 97.8% shows ~34.6% for GPT-4 on its own comparable table. Sent to V1 as priority 1 with a request for replacement text. Lesson: R1 verified *"is this number real?"*; nobody asked *"is this comparison sound?"*

## Final accounting

- **Totals:** 7 subagents, **1,240,234 reported subagent tokens** (gather 989,982 + verify 250,252), ~35 min wall-clock for the agent waves, 366 tool uses. Orchestrator context cost comparable in order of magnitude.
- **Vs R1:** 1.24M vs 0.997M tokens for a comparable 7-agent envelope (+24%), but R1's orchestrator additionally re-emitted ~40k tokens hand-archiving reports that agents now write themselves. Sources: 94 used / 29 rejected (R1: ~89 / ~50).
- **Order-of-magnitude cost:** ~177k subagent tokens per answered sub-question (7 SQs); ~25k per verified anchor claim (10); ~21k for the entire 12-claim base-error audit — the cheapest and highest-information single component of the session.
- **Value concentration:** the verify wave was 20% of tokens and produced the session's two most consequential outputs (the Chapter 01 correction and the measured error rate). Same lesson as R1: **gather wide and cheap, verify narrow and hard.**
- **Three things R3 should do differently:**
  1. Have agents flag mid-run when they expect to exceed ~2× their expected budget (G5: 307k tokens, 119 tool calls, 24 sources vs a 15-source cap).
  2. Run the venue-line check (arXiv Comments) as a standing step during gathering, not as a verifier catch — three misgradings would have been avoided for one line of effort each.
  3. Spot-check gather files' ANSWERS prose against their own claims; over-generalization lives in the synthesis, and the synthesis is what reaches the chapter.

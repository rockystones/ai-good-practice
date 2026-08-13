# Decision log

Format: `D-###` (date) — decision, rationale. Status: **adopted** / **open** / **superseded**.

- **D-001** (2026-08-12, adopted) — **Public from day one.** The GitHub repo was created public by the owner at initialization. Implication: every commit is immediately published, so the hygiene gates (D-004) are mandatory, not optional.

- **D-002** (2026-08-12, adopted) — **License: Apache-2.0**, chosen by the owner at repo creation. Covers tools and text alike. Revisit only if content-specific licensing (e.g., CC BY-SA for prose) ever matters.

- **D-003** (2026-08-12, adopted) — **Durability separation.** Content is classed durable / semi / dated (see CHARTER.md), because mixing evergreen mental models with perishable landscape facts is how AI guides rot. Dated pages carry "As of" headers and review-by dates.

- **D-004** (2026-08-12, adopted) — **Hygiene gates.** Commits use the GitHub noreply address; `tools/scan.py` must pass before every commit (`--staged`) and push (`--all`); both enforced by hooks (`tools/hooks` via `core.hooksPath`). Never bypassed with `--no-verify`. Scanner false positives go in `tools/scan-allow.txt`, exact string, with a comment.

- **D-005** (2026-08-12, adopted) — **Model-tier orchestration.** Top-tier model orchestrates (framing, synthesis, editorial judgment); Opus-class subagents for deep research, appraisal, and drafting; Sonnet-class for source sweeps and extraction; Haiku-class for mechanical chores. Research sessions are owner-gated with scope proposed upfront. Rationale: quality where judgment concentrates, economy where it doesn't.

- **D-006** (2026-08-12, **open**) — **Pilot chapter.** Proposal: Chapter 01, *What a language model actually is* — it anchors every other chapter, and it tests the research protocol on a well-documented topic where source quality varies wildly (good stress test for the tiering rules). Awaiting owner confirmation.

- **D-007** (2026-08-12, **open**) — **Syllabus roster.** 16-chapter map proposed in SYLLABUS.md; owner to confirm, reorder, or add topics before heavy research investment.

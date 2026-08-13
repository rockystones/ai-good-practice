# Decision log

Format: `D-###` (date) — decision, rationale. Status: **adopted** / **open** / **superseded**.

- **D-001** (2026-08-12, adopted) — **Public from day one.** The GitHub repo was created public by the owner at initialization. Implication: every commit is immediately published, so the hygiene gates (D-004) are mandatory, not optional.

- **D-002** (2026-08-12, adopted) — **License: Apache-2.0**, chosen by the owner at repo creation. Covers tools and text alike. Revisit only if content-specific licensing (e.g., CC BY-SA for prose) ever matters.

- **D-003** (2026-08-12, adopted) — **Durability separation.** Content is classed durable / semi / dated (see CHARTER.md), because mixing evergreen mental models with perishable landscape facts is how AI guides rot. Dated pages carry "As of" headers and review-by dates.

- **D-004** (2026-08-12, adopted) — **Hygiene gates.** Commits use the GitHub noreply address; `tools/scan.py` must pass before every commit (`--staged`) and push (`--all`); both enforced by hooks (`tools/hooks` via `core.hooksPath`). Never bypassed with `--no-verify`. Scanner false positives go in `tools/scan-allow.txt`, exact string, with a comment. *Addendum 2026-08-13:* owner enabled GitHub's server-side rejection of pushes that expose a personal email — defense in depth behind the local hooks.

- **D-005** (2026-08-12, adopted) — **Model-tier orchestration.** Top-tier model orchestrates (framing, synthesis, editorial judgment); Opus-class subagents for deep research, appraisal, and drafting; Sonnet-class for source sweeps and extraction; Haiku-class for mechanical chores. Research sessions are owner-gated with scope proposed upfront. Rationale: quality where judgment concentrates, economy where it doesn't.

- **D-006** (2026-08-12, adopted 2026-08-13) — **Pilot chapter.** Chapter 01, *What a language model actually is* — it anchors every other chapter, and it tests the research protocol on a well-documented topic where source quality varies wildly (good stress test for the tiering rules). Confirmed by owner 2026-08-13; research session R1 run the same day → `research/2026-08-13-ch01-what-an-llm-is/`.

- **D-007** (2026-08-12, adopted 2026-08-13) — **Syllabus roster.** 16-chapter map in SYLLABUS.md confirmed "for now" by owner 2026-08-13. Roster changes go through this log.

- **D-008** (2026-08-13, adopted) — **Resource capture.** Standing owner instruction: during any research session, recommendable learning resources encountered along the way (open courses, videos, interactive tools, blogs, people to follow, curated lists) are logged to RESOURCES.md with a why-good note and the session pointer — even when they're outside the session's question. Capture is cheap and happens inline; curation and ranking happen via Chapter 16 and refresh passes.

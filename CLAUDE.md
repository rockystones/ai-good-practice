# CLAUDE.md — working rules for this repo

Purpose: a primer + practice guide for using AI well, aimed at smart non-engineers. Before substantive work, read [CHARTER.md](CHARTER.md) (goals, editorial principles), [SYLLABUS.md](SYLLABUS.md) (chapter map and status), and [method/](method/) (research rules).

## Hygiene — non-negotiable

- **This repo is PUBLIC.** Anything committed is published immediately.
- Commits use the GitHub noreply email. Verify before the first commit of a session: `git config user.email` must end in `users.noreply.github.com`. The pre-commit hook enforces this.
- Before **every commit and push**, the sensitive-info scanner must pass: `python tools/scan.py --staged` (commit) / `--all` (push). The hooks in `tools/hooks` run these automatically — never bypass with `--no-verify`.
- New clone setup: `git config core.hooksPath tools/hooks` and set the noreply email (both are local config, not committed).
- Never commit: personal email addresses, real names beyond the GitHub handle, absolute local paths, machine or network details, tokens/keys, or anything under `private/` (the gitignored never-commit zone for drafts with personal context).
- Scanner false positives: add the exact matched text to `tools/scan-allow.txt` with a comment line above it.

## Orchestration and budget

- The orchestrator (top-tier model) does framing, decomposition, synthesis, editorial judgment, and final review.
- Subagents by tier — **Opus-class**: deep research, source appraisal, adversarial refutation, chapter drafting. **Sonnet-class**: source sweeps, claim extraction, per-source summaries, cross-referencing. **Haiku-class**: mechanical chores (link checks, index/status regeneration, format lint).
- Don't fan out when the orchestrator can do the work in fewer tokens. Parallelism is for breadth, not ceremony.
- **Research sessions are owner-gated**: propose scope first (topic, sub-questions, rough agent count), wait for go. One topic per session.
- Session types: **research** (runs the protocol, gated) → **distill** (research → chapter/cards) → **owner review** (feedback pass) → **refresh** (re-verify dated pages on their review-by dates).

## Content rules

- Every content page carries front-matter: `status` (draft/reviewed/published), `durability` (durable/semi/dated), `last-reviewed`, and for dated pages `review-by`.
- Dated pages open with "As of <Month YYYY>".
- Load-bearing claims carry evidence labels (established / corroborated / single-source / contested / anecdote) per [method/research-protocol.md](method/research-protocol.md).
- Research outputs land in `research/YYYY-MM-DD-<slug>/` **before** anything is distilled into `primer/` or `practices/`.
- During any research, log recommendable learning resources (courses, sites, tools, people, lists) to [RESOURCES.md](RESOURCES.md) with a why-good note and the session pointer (D-008). Capture inline; curate later.
- Plain language; jargon defined on first use. English.

## Logs

- Project decisions → [DECISIONS.md](DECISIONS.md) (`D-###`, dated, with rationale).
- Lessons and experience → [journal/](journal/), public-safe phrasing only.
- Chapter status lives **only** in SYLLABUS.md — don't duplicate it elsewhere.

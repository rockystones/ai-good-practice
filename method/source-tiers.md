---
status: published
durability: semi
last-reviewed: 2026-08-12
---

# Source tiers

Default credence by source type, for AI topics specifically. A tier sets the *starting* credence and the verification burden — never the verdict. Tier A sources can be wrong; Tier D leads can be right. Grades attach to claims (see [research-protocol.md](research-protocol.md)); tiers attach to venues.

## Tier A — Primary and artifact

Peer-reviewed papers; arXiv preprints from known labs and authors (unreviewed — check who wrote it and whether code/data ship with it); official model cards and system cards; official documentation and changelogs; the actual code or product you can run yourself.

- *Strengths:* closest to ground truth for "how it works" and "what it does."
- *Failure modes:* papers overclaim in abstracts (read the tables, not the abstract); official docs carry marketing gravity on quality claims ("best-in-class"); benchmarks measure the benchmark.

## Tier B — Expert secondary

Lab research blogs; independent practitioners with public track records who show their work, publish failures, and admit error. The test for "expert" is a checkable track record, not follower count.

- *Strengths:* interpretation, synthesis, honest field experience.
- *Failure modes:* even the best have beats and blind spots; a lab blog never undercuts its employer.

Named starting points (curated, not exhaustive; to be re-vetted when Chapter 16 is researched): Simon Willison (practical LLM engineering, rigorous show-your-work), Andrej Karpathy (foundations and explainers), Lilian Weng (survey depth), Chip Huyen (production ML), Nathan Lambert / Interconnects (post-training, open models), Ethan Mollick (non-engineer use; hype-warm, discount accordingly), Zvi Mowshowitz (dense roundups; strongly opinionated, work shown).

## Tier C — Community and journalism

Hacker News (comment sections are decent BS detectors; negativity bias), r/LocalLLaMA (ground truth for open-weights practice; enthusiast bias), LessWrong / Alignment Forum (safety depth; insular vocabulary), quality tech journalism and newsletters (good for events and timelines; weak for technical claims — they echo press releases).

- *Use for:* what practitioners actually experience, early signals, dissent that polished venues filter out.
- *Failure modes:* survivorship ("my AI workflow" posts select for success stories), pile-ons, motivated reasoning in both hype and doom directions.

## Tier D — Leads only

SEO content farms, "top 10 prompts" listicles, engagement-bait threads, AI-generated aggregator sites, anything undated or unsigned. Never cite as evidence; occasionally useful as a lead to a real source.

## Cross-cutting rules

- **Match tier to question type.** "What are people experiencing" makes Tier C primary evidence (graded anecdote or corroborated); "how does attention work" makes Tier C nearly worthless.
- **Incentive audit on every source:** who benefits if I believe this?
- **Independence beats volume.** One paper plus one independent replication outweighs fifty reposts of a press release.

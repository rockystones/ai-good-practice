# AI Good Practice

A primer and practice guide for using AI well — written for smart people who are not AI engineers and don't have a CS degree, but want real understanding instead of folklore.

**Status:** bootstrap. Structure, method, and hygiene tooling are in place; chapters are researched and written one at a time.

## Why this exists

Most AI writing is either vendor documentation (accurate, but narrow and product-bound), news (fast, but shallow and hype-prone), or tip listicles (confident, but unsourced and quickly stale). This repo aims at the missing layer: durable mental models, evidence-graded claims, and practices that survive model generations — plus a documented learning path showing how the conclusions were reached, so others can learn the lessons faster.

## How to read this repo

- Start with [SYLLABUS.md](SYLLABUS.md) — the full curriculum map and each chapter's status.
- **Durable pages** (mental models, practices) are written to stay true across model generations.
- **Dated pages** (model landscape, use-case evidence) begin with "As of &lt;month year&gt;" and carry a review-by date. Trust them like milk, not wine.
- [practices/](practices/) holds standalone practice cards — the shortest useful unit of advice.

## Map

| Path | What lives there |
|---|---|
| [SYLLABUS.md](SYLLABUS.md) | Curriculum map + chapter status (single source of truth) |
| [primer/](primer/) | The chapters — the actual guide |
| [practices/](practices/) | Practice cards: one durable technique each |
| [method/](method/) | How research here is done: protocol, source tiers, templates |
| [research/](research/) | Dated research-session outputs (briefs, source logs, findings) |
| [journal/](journal/) | Learning log — lessons captured as they happen |
| [DECISIONS.md](DECISIONS.md) | Decision log for the project itself |
| [tools/](tools/) | Hygiene tooling (sensitive-info scanner, git hooks) |

## Method

Every substantive claim in the guide traces back to a research session under `research/`, run against the protocol in [method/research-protocol.md](method/research-protocol.md): question written before searching, every source logged, claims graded by evidence, retrospective at the end. The repo practices what it preaches — it is built with AI assistance under the same verification, budget, and hygiene rules it teaches.

## License

Apache-2.0 (see [LICENSE](LICENSE)).

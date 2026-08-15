# Source log — ch02-models-that-reason (session R2)

Navigation index. **Full entries — every source with lineage, incentive, status, and per-claim IDs — live in [gather/](gather/)**, written by the gatherers themselves under the checkpoint rule (first session to work this way). 94 sources used, 29 rejected, 317 logged claims. Claim IDs `G<n>.<source>.<claim>` resolve in the corresponding gather file.

| File | Angle | Used / rejected | Claims |
|---|---|---|---|
| [G1-mechanism-training.md](gather/G1-mechanism-training.md) | Academic/primary: test-time compute, RLVR, process vs outcome supervision, distillation | 17 / 1 | 66 |
| [G2-faithfulness.md](gather/G2-faithfulness.md) | Faithfulness & monitorability; what products actually display | 12 / 1 | 51 |
| [G3-capability-evidence.md](gather/G3-capability-evidence.md) | Adversarial, both directions: gains, limits, the collapse debate | 17 / 5 | 61 |
| [G4-cost-and-practice.md](gather/G4-cost-and-practice.md) | Economics: billing mechanics, budgets/controls, prompting differences | 19 / 10 | 82 |
| [G5-misconceptions-resources.md](gather/G5-misconceptions-resources.md) | Misconceptions + vetted learning resources | 24 / 12 | 57 |

## Verification

| File | Scope | Outcome |
|---|---|---|
| [V1-faithfulness-and-ch01.md](verify/V1-faithfulness-and-ch01.md) | 6 faithfulness anchors + a correction to already-published Chapter 01 | Ch-01 comparison confirmed misleading (gatherer's *diagnosis* overturned); 1 gatherer label corrected; 2 popular framings corrected (inverse-scaling is an inverted U; the 95% monitor figure has a 60% baseline) |
| [V2-cost-capability-and-base-error.md](verify/V2-cost-capability-and-base-error.md) | 5 cost/capability anchors + the blind-drawn base-error audit | All 5 anchors confirmed with scope corrections; **12-claim audit: 8 OK, 4 imprecise, 0 wrong**; peer-review status corrected on 3 sources |

## Diversity audit (Phase 1 quota: ≤40% any venue/author)

Quota held. Two concentrations flagged rather than hidden, both in [FINDINGS](FINDINGS.md): faithfulness evidence is Anthropic/OpenAI-heavy (they are the labs publishing it, including against their own interest), and four of five faithfulness anchors were measured on models now retired. Vendor documentation is used for billing and product mechanics — first-party and appropriate there — and is separated from vendor *capability* claims, which are treated as marketing until independently checked.

## Access notes contributed to the [playbook](../../method/access-notes.md)

- **New failure mode:** the reader proxy can return *unrelated cached content* rather than erroring — a silent wrong page is indistinguishable from a successful fetch. Always confirm the returned title/date matches the request.
- arXiv `/abs/` pages were the highest-yield route for authorship, dates, and **peer-review status** (the Comments field); `/html/<id>vN` for body text; `/pdf/` remains undecodable.
- Directly fetchable this session without incident: arxiv.org, anthropic.com, platform.claude.com, ai.google.dev, simonwillison.net, engineering.nyu.edu, machinelearning.apple.com.

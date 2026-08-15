# V2 — Adversarial verification: cost/capability anchors + base-error spot audit

*Opus-class verifier, session R2, 2026-08-15. Sample for the audit was drawn by the orchestrator (stratified, blind, excluding anchor claims) per D-010 — the agent under audit never chooses its own sample.*

## Anchor verdicts

### A1 — "When More Thinking Hurts" (arXiv 2604.10739) — **CONFIRMED existence / WEAKENED as a threshold**
Real, not slop: Shu Zhou, Rui Ling, Junan Chen, Xin Wang, Tao Fan, Hao Wang; submitted 2026-04-12; 11 pages; cs.AI; **v1 only, unrefereed, no journal ref**.
The 12K figure is correctly reported but **is one curve, not a threshold**: R1-32B on AIME peaks at 12K tokens (55.8%) and falls to 54.9% at 16K. Only **two models swept** (DeepSeek-R1-Distill-32B, s1-32B — both 32B open-weight; no frontier model). The paper's own difficulty analysis gives a different scale entirely: optimal budget "varies dramatically, from 1.0K tokens for Level 1 to 7.5K for Level 5" (MATH-500); easy problems cross the overthinking threshold at 2K vs 8K for Level 5. Marginal utility per 500 tokens (R1-32B/AIME): 0.5–2K +3.2 → 8–12K +0.1 → 12–16K **−0.3** (sign flip genuine). Mechanism: "67.5% involve genuine overthinking where the model explicitly reconsiders and rejects a correct answer."
**Do not write "reasoning accuracy peaks near 12K tokens" unqualified.**

### A2 — All three vendors bill thinking tokens as output tokens — **CONFIRMED, with nuances**
- **Anthropic**: "Tokens Claude uses while thinking (billed as output tokens)"; billing identical for `display: "summarized"` and `"omitted"`; "You are billed for the full thinking process, not the thinking content visible in the response."
- **OpenAI**: "While reasoning tokens are not visible via the API, they still occupy space in the model's context window and are billed as output tokens."
- **Google**: "response pricing is the sum of output tokens and thinking tokens"; pricing column header reads "Output price (including thinking tokens)."
Nuances: Anthropic charges **nothing** for generating the summary (hiding thinking saves latency, not money); on keep-all models, **prior turns' retained thinking is re-billed as *input* tokens** on every later turn; Google's free tier includes thinking; **none of the three has a thinking surcharge** — it's the ordinary output rate.

### A3 — `budget_tokens` deprecation — **CONFIRMED**
Verbatim: deprecated on Claude 4.6 models (requests still succeed); "Claude 4.7 and later models do not support it and reject requests that use it, returning a 400 error." Migration: `budget_tokens` → `thinking: {type:"adaptive"}` + `output_config: {effort: …}` (`max`/`xhigh`/`high`(default)/`medium`/`low`, availability varies).
The quotable behavioural difference: with a fixed budget the model thinks on *every* request; with adaptive thinking it decides per request and at lower effort "may skip thinking entirely on easy inputs."

### A4 — The Apple exchange — **CONFIRMED with two corrections to our corpus**
- **Apple's paper is peer-reviewed**: arXiv Comments field reads "NeurIPS 2025. camera-ready version…". *Neither G3 nor G5 recorded this*, and it changes how the exchange should be weighed. Authors: Shojaee, Mirzadeh, Alizadeh, Horton, Bengio, Farajtabar. Claims verbatim: "complete accuracy collapse beyond certain complexities"; reasoning effort "increases… up to a point, then declines despite having remaining token budget."
- **The rebuttal is cited from a superseded version in two of our files.** Current v2 (2025-06-16) is titled "Comment on The Illusion of Thinking…", author **A. Lawsen alone**; arXiv note: "Latest version removes Claude as a co-author, in line with arXiv policies." G3 recorded the v1 byline and called model-co-credit "an unresolved norms question" — **arXiv settled it for this paper within six days.** Past tense only.
- **Replication confirmed exactly as G3 reported**: Dellibarda Varela, Romero-Sorozabal, Rocon, Cebrian (arXiv 2507.01231), using Gemini 2.5 Pro. Hanoi failures "not purely result of output constraints, but also partly a result of cognition limitations… around 8 disks"; River Crossing results "hinge upon testing unsolvable configurations… Once we limit tests strictly to solvable problems—LRMs effortlessly solve large instances involving over 100 agent pairs."

### A5 — Inverse Scaling in Test-Time Compute — **CONFIRMED, stronger than recorded**
First author is **Aryo Pradipta Gema** (G3 truncated the name). **Venue now primary-confirmed — G3 can drop its hedge**: "Published in TMLR (12/2025; Featured Certification; J2C Certification)" — peer-reviewed with TMLR's top two distinctions.
Claude failure mode verbatim in abstract: "Claude models become increasingly distracted by irrelevant information." The o-series phrase is **body, not abstract** (abstract says they "resist distractors but overfit to problem framings") — cite the body.
Magnitude: ~10–15 points for Opus 4 on Misleading Math in the *controlled* setup; but the paper's **natural-overthinking setup is far larger — Opus 4 falls from ~70% to ~30% with five distractors**, which G3 did not report. Five failure modes total, including "Claude Sonnet 4 showing increased expressions of self-preservation."

## Base-error spot audit

Twelve blind-drawn, stratified, non-anchor claims:

| Claim | Verdict | Note |
|---|---|---|
| G1.8.3 (o1 system card) | **OK** | Near-identical to source footnote |
| G1.15.5 (Kimi k1.5) | **OK** | All five benchmark figures exact |
| G2.4.5 (CoT monitorability) | **MINOR** | Content real; **locator wrong** — fourth item is in the open-questions section, not the recommendations list |
| G2.11.2 (covert sandbagging) | **OK** | Verbatim; drops a parenthetical without ellipsis (meaning unchanged) |
| G3.11.4 (GSM-Symbolic) | **OK** | Abstract characterization exact; the gatherer's hedge on the Phi-3-mini attribution can be **lifted** — the body supports it |
| G3.14.3 (inverse scaling) | **OK** | Figure 3 range correctly labelled approximate |
| G4.9.6 (Gemini latency) | **MINOR** | **Quote hygiene**: source says "may take significantly longer"; rendered as "take[s]" — hedge hardened into assertion; elided "(non thinking)" is load-bearing |
| G4.12.3 (Aider cost ratio) | **OK** | All four figures verbatim; arithmetic checks (2.078 ≈ 2.08×; 4.5 pp) |
| G4.17.2 (faithfulness) | **OK** | Hedge unnecessary — claim stated flat out on the cited page |
| G5.8.3 (Willison on Apple paper) | **OK** | Verbatim (see the negative-fetch note below) |
| G5.11.2 (NYU study) | **MINOR** | Content verbatim but **on a different page** than the URL cited |
| G5.14.3 (Apple debate) | **MINOR** | "Contested" right; **"unresolved" is stale** since the Jul 2025 replication — and internally inconsistent with G3.10 in the same corpus |

**Observed: N = 12 · 8 OK · 4 MINOR · 0 WRONG · 0 UNVERIFIABLE.**
**Imprecision rate 33% (4/12); materially-wrong rate 0%.**
95% Clopper–Pearson on 4/12 ≈ **10%–65%**; on 0/12 WRONG, 95% upper bound ≈ **22%**. With n=12 the honest statement is "somewhere between one-in-ten and two-in-three claims carry an imprecision," not "one in three."

### What kind of errors dominate — **not numbers**
Every numeric value checked survived: Kimi's five benchmark figures, Willison's four leaderboard figures plus two derived quantities, four sandbagging percentages, the Opus 4 range. **The Numbers Rule is working.** All four defects sit in softer layers:
1. **Locator drift (2 of 4)** — right source, wrong page/section. The dominant failure mode, and the one most likely to embarrass a chapter: a reader who follows the citation finds nothing there.
2. **Quote hygiene (1 + a near-miss)** — dropping a modal turns "may take significantly longer" into "takes significantly longer". This is the mechanism by which hedged vendor language hardens into confident chapter prose.
3. **Stale characterization (1)** — true in June 2025, not now.

### The opposite error, invisible to this metric
Two claims (G3.11.4, G4.17.2) were flagged low-confidence when the primary supports them outright, and two sources' peer-review status was missed or hedged (NeurIPS 2025; TMLR Featured + J2C). **Under-claiming doesn't show up in an error rate but costs real evidential weight.** If the session publishes 33%, it must say alongside it that roughly as many claims were *under*-stated.

## Cross-cutting notes

- **Peer-review status is systematically under-recorded.** A single pass over the arXiv Comments field for every A-tier source would fix this cheaply — and it materially changes how the Apple exchange should be weighed (peer-reviewed paper vs unrefereed comment).
- **"One negative fetch is not evidence of absence."** A first pass reported a quote absent from Willison's post; a second, differently-phrased pass found it verbatim in the opening sentence. **The published error rate would have been wrong by one full claim (8%) had that not been re-checked.** Any verifier working through a summarizing fetch tool must confirm negatives with a second differently-scoped query before recording a refutation.
- **Accurate claims, over-generalized synthesis.** G4's ANSWERS prose presents the 12K peak and the 1K–7.5K difficulty range as one coherent picture without noting they come from different benchmarks and rest on two 32B open models. The claim-level entries are accurate; the *summary* over-reaches — and the summary is what reaches the chapter.
- **Access playbook held.** No proxy substitution observed; the single proxy fetch returned the correct title for the requested URL. arXiv `/abs/` pages were the highest-yield route for authorship, dates, and venue.

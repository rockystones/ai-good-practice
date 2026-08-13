# V1 — Adversarial verification: hallucination-evidence anchor claims

*Opus-class verifier, session R1, 2026-08-13. Mandate: try to break five load-bearing claims from the gather phase. Verdicts feed `../FINDINGS.md`.*

## Claim 1 — GPT-4 calibration degraded by post-training — **CONFIRMED** (one word must change)

Primary (GPT-4 Technical Report, §5 "Limitations"): "the pre-trained model is highly calibrated … after the post-training process, the calibration is reduced (Figure 8)." Figure 8 caption: "The post-training hurts calibration significantly."

Corrections for the chapter:
1. **Say "post-training," not "RLHF."** The report never attributes the loss specifically to RLHF — that was the gatherer's inference.
2. No numeric calibration-error value exists in the report — don't invent one.
3. Scope: one figure, subset of MMLU, multiple-choice logprobs — not free-text assertions. Externally unreproducible (base model never released).
4. March-2023 GPT-4 result; don't generalize to "alignment always destroys calibration" or to current models.

Safe formulation: "OpenAI's own GPT-4 Technical Report notes the raw pretrained model was 'highly calibrated' — its stated confidence tracked how often it was right — but after post-training 'the calibration is reduced'; the figure caption puts it bluntly: 'The post-training hurts calibration significantly.' (Subset of MMLU multiple-choice; no numeric error published; base model never released, so no outside party has checked.)"

Sources: arxiv.org/abs/2303.08774 + ar5iv + arxiv HTML v6 (full text, 2026-08-13).

## Claim 2 — GPT-5 hallucination rates — **(a) WEAKENED, materially misstated; (b) CONFIRMED w/ caveats**

Primary: GPT-5 System Card (2025-08-13), full PDF read via r.jina.ai proxy. **Two metrics, two denominators — the gatherer merged them:**

| Model | % of factual **claims** with errors | % of **responses** with ≥1 major incorrect claim |
|---|---|---|
| gpt-5-thinking | **4.5%** | **9.6%** |
| gpt-5-main | 7.2% | 11.6% |
| o3 | 12.7% | 20.6% |
| GPT-4o | 22.0% | 12.9% |

(Production-traffic-style prompts, browsing enabled, graded by an LLM with web access.)

Corrections:
1. "GPT-5 9.6% vs GPT-4o 12.9%, thinking 4.5%" is wrong — **9.6% and 4.5% are the same model** (gpt-5-thinking) on two metrics. gpt-5-main = 11.6%/7.2%. Never compare across columns.
2. **Teachable trap:** GPT-4o beats o3 on the response metric (12.9% vs 20.6%) but is the worst in the table on the claim metric (22.0%) — same eval, opposite ranking, because GPT-4o writes shorter answers (fewer claims per response). Denominators matter.
3. The hallucination statistics are themselves **graded by a language model** and are vendor self-report without external replication — say so.
4. SimpleQA-no-web (Table 8): gpt-5-main 0.46 accuracy / 0.47 hallucination (GPT-4o 0.44/0.52; gpt-5-thinking 0.55/0.40). Note accuracy+hallucination ≠ 100% (abstentions ≈ 7%); attribute 47% to **gpt-5-main**, not "GPT-5."
5. **SimpleQA is adversarially collected against GPT-4 responses** (its own abstract) — a constructed worst case, not a usage rate.
6. Same system card, same models: ~47% (adversarial no-web) vs ~7% of claims (production-style) vs **0.6–0.9%** (LongFact/FActScore with browsing). **"The hallucination rate" is not a property of the model; it's a property of the question set.** Print the spread, not one number.

Sources: r.jina.ai/https://cdn.openai.com/gpt-5-system-card.pdf (×2 independent prompts); arxiv.org/abs/2411.04368 (SimpleQA); independent search corroboration (2026-08-13).

## Claim 3 — Charlotin legal-hallucination database — **WEAKENED** (count holds; Oregon details corrected)

- Count trajectory independently corroborated: ~200 (mid-2025) → 1,227 (2026-04, of which 811 US) → 1,598 (2026-06-09) → **1,668 (2026-07-02)**. The 1,163-US sub-figure could NOT be verified (plausible from the April ratio, unconfirmed). Live rows read through **2026-08-11** — the true current count is materially higher (~8 new cases/day); don't state a specific current number.
- Inclusion criteria CONFIRMED strict: only decisions where a court found or clearly implied reliance on hallucinated material; "mere accusations do not count"; maintainer's own words: "necessarily an undercount." Known US skew partly reflects court-record transparency (PACER) vs European anonymization.
- **Oregon case = Couvrette v. Wisnovsky (D. Or.): 15 fabricated citations + 8 fabricated quotations** (not 23+8 — that double-counted), orders **Dec 12 2025 + Mar 23 2026** (not May 2026), ≈ **"roughly $110,000"** combined sanctions/fees (secondary sources disagree at the cent level — don't print an exact figure).

Safe formulation: "…1,668 court decisions worldwide as of 2 July 2026 — up from roughly 200 a year earlier, still adding about eight a day; it counts only decisions where a court found or clearly implied reliance on fabricated material… In one Oregon federal case, lawyers who filed 15 nonexistent citations and 8 fabricated quotations drew roughly $110,000 in combined sanctions and fees."

Sources: damiencharlotin.com (403 direct; partial via proxy); Charlotin's FAQ at artificialauthority.ai; WSBA nwsidebar (2026-03-02); grllp.com case note; haqq.ai audit (all 2026-08-13).

## Claim 4 — Kalai et al. "Why Language Models Hallucinate" — **CONFIRMED** (precision fix + provenance)

All three sub-claims verbatim in arXiv 2509.04664 (v1 2025-09-04): statistical origin ("errors in binary classification… natural statistical pressures"), evaluation incentives ("optimized to be good test-takers"), fix = **rescore existing dominant benchmarks**, explicitly rather than adding new hallucination evals.

Corrections:
1. The bound is **≳ 2× the "Is-It-Valid" (IIV) misclassification rate** with correction terms — not a clean "2× classification error." Safe: "generation is provably harder than recognition — generating-true-statements error is bounded below by roughly twice the error of the corresponding true/false classification."
2. Provenance: unrefereed preprint; 3 of 4 authors at OpenAI; "the benchmarks are at fault" is a convenient conclusion for a vendor. Print it.
3. Serious criticism exists (LessWrong close reading: possible conflation of reward-model vs policy classification errors; the 2× may be "the trivial one"; rescoring-beats-new-evals asserted without empirical support; Wegner: models LLMs as test-takers rather than generative processes). No refutation of the formal result found — criticism is about framing/practical relevance.

Sources: arXiv abs + full HTML; LessWrong close reading; Wegner critique (2026-08-13).

## Claim 5 — Ackermann & Emanuilov rebuttal — **WEAKENED → do not cite; superior replacement found**

- Paper exists and says what was reported. But: **citation count 1**; arXiv-only; **Ackermann has no discoverable affiliation or prior record**; Emanuilov is real (Sofia University PhD; runs UnfoldAI consultancy) but 23 total citations, h-index 3, in unrelated areas; the paper is the third in a **self-referential trilogy** whose "empirical" support is the authors' own prior unreviewed preprint, and whose proposed fix ("Licensing Oracle") is their own product concept. (Also: a search summarizer's claim of Simons Foundation support is false — that's arXiv's site-wide funding footer. Do not repeat.)
- **Replacement pairing for the intrinsic-vs-fixable debate:**
  - **Xu, Jain & Kankanhalli (NUS), "Hallucination is Inevitable: An Innate Limitation of LLMs," arXiv 2401.11817** — real, widely cited, formal result: a computable LLM cannot agree with a computable ground truth on all inputs (learning-theory/diagonalization); hallucination inevitable *for general problem solvers*. Still a preprint — say so.
  - **Suzuki, He, Tian & Wang, "Hallucinations are inevitable but can be made statistically negligible," arXiv 2502.12187** — the rebuttal: computability-style inevitability "cannot explain practical issues" (requires infinite input space; near-trivial from the halting problem); with sufficient data quality/quantity hallucination is **statistically negligible**.
  - Honest framing: "mathematically inevitable" is true in a precise but very weak sense, and does NOT imply "cannot be substantially reduced." Citing inevitability alone breeds fatalism the math doesn't support.
- Further leads found, NOT vetted: arXiv 2506.06382, 2510.05116, 2508.07334.

Sources: arXiv 2512.14801 + 2509.16297 + 2511.06073; Semantic Scholar API (citation count); Google Scholar profile; arXiv 2401.11817 + alphaxiv affiliation page; arXiv 2502.12187; dblp (2026-08-13).

## Cross-cutting notes

1. **"The hallucination rate" is not a number.** Same models span ~47% (adversarial) → ~7% (production-style claims) → ~0.7% (grounded long-form with browsing). Make the spread the teaching point; any single figure misleads in one direction or the other.
2. **Two metric traps** the gatherers fell into: claim-level vs response-level denominators (opposite model rankings in one table); accuracy + hallucination ≠ 100% (abstention is a third outcome).
3. **Vendor self-report runs through the whole story** (GPT-4 calibration, GPT-5 tables, the leading why-paper — all OpenAI; numbers LLM-graded; base model unreleasable-for-checking). One honest paragraph strengthens the chapter.
4. **Lineage lesson:** both secondary-aggregator-based claims came back "real numbers, wrong labels." Rule adopted: no number ships without a primary or a dated verbatim quote.
5. **Straw-source averted:** the weak rebuttal would have been the counter-position; replaced with the Xu/Suzuki pairing.
6. **Arc the evidence supports:** training/eval rewards confident guessing (Kalai) + post-training degrades the model's own uncertainty signal (GPT-4 §5) + real-world costs measurable and rising (Charlotin) — coherent without the 47% shock number.

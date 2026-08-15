# 2026-08-15 — The check we didn't know we were missing

**What happened.** Research for chapter 02 audited a claim in chapter 01 that had already passed adversarial verification, and found it misleading anyway.

The claim: a planning benchmark where "2023-era models produced correct plans about 3% of the time" and "a 2024 reasoning model scored 97.8%." Session R1 verified both numbers against primaries — both real, both correctly transcribed, both still true today. Session R2 asked a different question and the sentence fell apart:

- The 3% described GPT-3 and BLOOM-era models from a February 2023 paper. Readers hearing "2023-era models" picture GPT-4 or ChatGPT — which scored about 35% on those same 600 problems.
- The very study reporting 97.8% shows, in the adjacent table, *2024 non-reasoning* models already scoring 35–63%. Most of the climb predated reasoning models entirely; the sentence handed them credit for it.
- The best-performing reasoning model was quoted; its sibling scored 56.6% on the identical set.
- And one table over: a classical planning program of a kind that has existed since the 1990s solves all 600 problems, perfectly, in about a quarter of a second — a fact the paper's own authors emphasize.

A second, simpler error rode along: the harder variant renames the puzzle *actions* ("pick up" → "attack object"), not the objects. The chapter said objects.

**The lesson, and it's a new one.** R1 asked *is this number real?* and answered it rigorously. Nobody asked *is this comparison sound?* Those are different checks, and the second one is where verified numbers turn into false claims. → [P-004](../practices/P-004-check-the-comparison.md).

**Two smaller corrections from the same pass**, both worth remembering because both were repeated confidently before being checked:

- "Bigger models produce less faithful reasoning" — the actual finding is an inverted U. A mid-sized model was the most faithful; smaller models were *also* less faithful. The popular framing keeps only the half that sounds ominous.
- "A chain-of-thought monitor caught 95%" — true, but the baseline monitor that saw only actions and no reasoning already caught 60%. The contribution was 60→95, not 0→95. A number with no baseline is a number doing propaganda.

**What worked.** The verifier declined to accept the gatherer's diagnosis of the problem, checked the primary itself, and found the gatherer had identified a real defect for the wrong reason — then supplied replacement text. Adversarial verification catching a *research agent's* reasoning, not just its facts, is the layer working as designed.

**Process note.** Corrections here are visible: the chapter carries a dated correction notice rather than a silent edit. A guide about calibrated trust that quietly fixes its own record would be teaching the opposite of its content.

# G5 — Learning-resource harvest (raw gatherer report)

*Intermediate artifact: Sonnet-class gatherer, session R1, 2026-08-13, assigned SQ7. Authoritative curated list: `../../../RESOURCES.md`. Source IDs SE-n.*

## SOURCES CONSULTED

- SE-1 — Elements of AI — https://www.elementsofai.com/ · MinnaLearn + University of Helsinki, est. 2018 · Course, Tier A · used
- SE-2 — Class Central listing (Elements of AI) — classcentral.com · rejected (403 on every page incl. root; could not verify despite organic appearances across 6+ unrelated searches)
- SE-3 — DeepLearning.AI "AI For Everyone" — https://www.deeplearning.ai/courses/ai-for-everyone/ · Andrew Ng · Course, Tier A · used
- SE-4 — DeepLearning.AI "Generative AI for Everyone" — https://www.deeplearning.ai/courses/generative-ai-for-everyone/ · Andrew Ng · Course, Tier A · used
- SE-5 — DeepLearning.AI "ChatGPT Prompt Engineering for Developers" · rejected (requires Python against an API; wrong audience despite beginner framing)
- SE-6 — Google AI Essentials — https://grow.google/ai-essentials/ · Course, Tier A · used
- SE-7 — Cohere LLM University · rejected (developer/enterprise-API focused)
- SE-8 — 3Blue1Brown Neural Networks hub — https://www.3blue1brown.com/topics/neural-networks · Video series, Tier A · used (JS-heavy render; chapter verified via SE-9)
- SE-9 — 3Blue1Brown "Transformers, the tech behind LLMs" — https://www.3blue1brown.com/lessons/gpt · April 2024 · Video, Tier A · used
- SE-10 — Karpathy "[1hr Talk] Intro to LLMs" — youtube.com/watch?v=zjkBMFhNj_g · Nov 2023 · Video, Tier A · used
- SE-11 — archive.org corroboration of SE-10 · Tier B · used (title/uploader/date confirmed)
- SE-12 — Karpathy "Deep Dive into LLMs like ChatGPT" — youtube.com/watch?v=7xTGNNLPyMI · Feb 2025 · Video, Tier A · used
- SE-13 — Karpathy's X post announcing SE-12 (x.com/karpathy/status/1887211193099825254) · Tier A creator statement · used — "general audience" framing is Karpathy's own
- SE-14 — HN thread on SE-12 (news.ycombinator.com/item?id=42952960) · Tier C corroboration · used
- SE-15 — Brendan Bycroft LLM Visualization — https://bbycroft.net/llm · Interactive, Tier A · used (thin JS render; description from SE-16)
- SE-16 — GitHub README bbycroft/llm-viz · Tier A (creator's repo) · used
- SE-17 — Willison post on Bycroft's tool · Tier C corroboration · used
- SE-18 — Transformer Explainer — https://poloclub.github.io/transformer-explainer/ · Georgia Tech/IBM · Interactive, Tier A · used (rich interactive content confirmed directly)
- SE-19 — Georgia Tech news release on SE-18 · Tier B corroboration · used
- SE-20 — OpenAI Tokenizer (platform.openai.com/tokenizer) · rejected (403 ×2; could not confirm it loads without login)
- SE-21 — gpt-tokenizer.dev · used with caveat (resolves but too thin to confirm functionality; secondary alternative only)
- SE-22 — HF "The Tokenizer Playground" (huggingface.co/spaces/Xenova/the-tokenizer-playground) · Interactive, Tier A · used ("Running" status, 692 likes confirmed)
- SE-23 — BertViz (github.com/jessevig/bertviz) · Interactive, Tier A · used
- SE-24 — Wolfram "What Is ChatGPT Doing…" · rejected-for-vetted-list (TLS cert error ×4 across domain — see NEAR-MISSES)
- SE-25 — ResearchGate PDF of Wolfram essay · Tier C corroboration · logged, not fetched
- SE-26 — Understanding AI "LLMs explained with a minimum of math and jargon" — understandingai.org · Lee & Trott, July 2023 · Essay, Tier A · used (no paywall confirmed)
- SE-27 — Eric Holscher "The Best Introduction to LLMs I've Found" (ericholscher.com, Jan 2025) · Tier C corroboration · used (independent endorsement of SE-26)
- SE-28 — Jay Alammar "The Illustrated Transformer" — jalammar.github.io/illustrated-transformer/ · June 2018, updated 2025 · Essay, Tier A · used
- SE-29 — Guardian visual explainer (Nov 2023) · rejected-for-vetted-list (domain refused by fetch tool; read only via search extraction)
- SE-30 — FT "Generative AI exists because of the transformer" (ig.ft.com, Sept 2023) · rejected-for-vetted-list (same domain-refusal)
- SE-31 — Stephen Downes repost corroborating SE-30 (downes.ca/post/75594) · Tier C · used — notes FT made it free/open-access
- SE-32 — One Useful Thing (oneusefulthing.org) · Ethan Mollick · Newsletter, Tier A · used
- SE-33 — Simon Willison's Weblog (simonwillison.net) · Blog, Tier A · used (active through Aug 2026 confirmed)
- SE-34 — AI Snake Oil → **redirects to normaltech.ai** ("AI as Normal Technology") · Kapoor (formerly w/ Narayanan) · Newsletter, Tier A · used — rebrand/domain move confirmed live
- SE-35 — Princeton news release on Narayanan & Kapoor · Tier B corroboration · used
- SE-36 — Hannibal046/Awesome-LLM (25.8k stars) · rejected (papers/frameworks oriented — wrong altitude for non-coders; logged as most prominent list in the space)
- SE-37 — owainlewis/awesome-artificial-intelligence · rejected (skews technical, thin beginner section)
- SE-38 — KDnuggets "10 Free Resources to Learn LLMs" (Aug 2024) · rejected (most resources assume coding/ML background despite framing)
- SE-39 — R2D3 "A Visual Introduction to Machine Learning" (r2d3.us, 2015) · Interactive essay, Tier A · used
- SE-40 — General awareness searches (HN jargon-free thread id=36941705, TuringPost/DataCamp roundups) · Tier C · logged for context only

## VETTED RESOURCES (16)

### Elements of AI — https://www.elementsofai.com/ (verified loads 2026-08-13)
course · Free MinnaLearn/Univ. Helsinki intro-AI course; Part 1 "Introduction to AI" requires "no complicated math or programming"; 2M+ learners, 170+ countries, unusually strong non-CS uptake · ~5-6 hrs Part 1 (~30 hrs full) · free · long-running since 2018, still active 2026 · Caveats: Part 2 needs basic Python — stop after Part 1 if no-code; broad AI survey, not LLM-specific · Serves: Ch-01 + general "start here"

### AI For Everyone (DeepLearning.AI / Andrew Ng) — https://www.deeplearning.ai/courses/ai-for-everyone/ (verified loads)
course · Non-technical: what AI can/can't do, applying it in an organization; no coding, no equations · ~7 hrs · $49 certificate track (aid available; free-audit not confirmed) · flagship non-technical offering · Caveats: business/strategy framing, thin on LLM mechanics vs the GenAI course · Serves: "using AI at work" chapters more than Ch-01

### Generative AI for Everyone (DeepLearning.AI / Andrew Ng) — https://www.deeplearning.ai/courses/generative-ai-for-everyone/ (verified loads)
course · Non-technical, specifically how generative AI/LLMs work + lifecycle + prompting basics; "doesn't require any coding skills or prior knowledge of AI" · ~5 hrs · freemium (certificate needs Coursera PRO; verify pricing at signup) · current flagship · Caveats: pricing page vague · Serves: Ch-01 core + prompting chapter

### Google AI Essentials — https://grow.google/ai-essentials/ (verified loads)
course · Google's beginner course on practical genAI use (Gemini-based); five modules incl. "how AI works", prompting, responsible use; "no experience required" · <5 hrs · **$49/month subscription after 7-day trial** · active · Caveats: subscription pricing is a real barrier vs free options — flag clearly · Serves: Ch-01 basics + prompting

### 3Blue1Brown — "Transformers, the tech behind LLMs" (Deep Learning Ch.5) — https://www.3blue1brown.com/lessons/gpt (verified loads); hub: /topics/neural-networks
video · Visual walkthrough of transformer internals (tokenization, embeddings, attention, softmax); widely regarded best visual/intuitive explanation · ~27 min (Ch.5); 2-3 hrs with lead-up chapters · free · Ch.5 April 2024, channel active · Caveats: assumes patience for some math visuals; best after/alongside Ch.1-2 of the series · Serves: Ch-01 core

### Karpathy — "[1hr Talk] Intro to Large Language Models" — youtube.com/watch?v=zjkBMFhNj_g (verified loads)
video · One-hour general-audience talk: what LLMs are, pretraining vs fine-tuning, LLM-as-OS mental model · ~1 hr · free · Nov 2023; still the standard reference cited in 2026 · Caveats: field-as-of-Nov-2023 — pair with something current · Serves: Ch-01 core

### Karpathy — "Deep Dive into LLMs like ChatGPT" — youtube.com/watch?v=7xTGNNLPyMI (title verified directly; date/desc via his X post)
video · 3.5-hour full training stack: pretraining data/tokenization, SFT, RLHF, reasoning models (incl. DeepSeek-R1); Karpathy's own framing: for people who use ChatGPT, not engineers · 3.5 hrs (flag the commitment) · free · Feb 2025, his most-cited general explainer · Caveats: long — a "go deeper" rec, not first touch · Serves: Ch-01 deep + training chapter

### Transformer Explainer — https://poloclub.github.io/transformer-explainer/ (verified loads, rich interactive confirmed)
interactive · Live GPT-2 running in-browser: type text, watch next-token prediction, Sankey diagrams, hoverable attention maps · 10-30 min · free, no account · Georgia Tech/IBM; 560k+ users reported; AAAI demo paper · Caveats: GPT-2 (small, dated) as the example — one-line caveat needed · Serves: Ch-01 core — likely best single interactive

### Brendan Bycroft's LLM Visualization — https://bbycroft.net/llm (verified loads; description via creator's GitHub README)
interactive · 3D step-by-step animated inference walkthrough down to individual matrix operations; GPT-2/3-scale topology · 20-40 min · free · creator active; still cited/shared 2026 · Caveats: visually dense — second stop after basic vocabulary · Serves: Ch-01 core

### Hugging Face Tokenizer Playground — https://huggingface.co/spaces/Xenova/the-tokenizer-playground (verified "Running", 692 likes)
interactive · Type text → see tokens + IDs across multiple tokenizers; makes "the model sees tokens, not words" tangible in ten seconds · 5-10 min · free, no login · active Space · Caveats: OpenAI's official tokenizer couldn't be verified (403 ×2) — use this instead; gpt-tokenizer.dev = thinly-verified backup · Serves: Ch-01 core

### BertViz — https://github.com/jessevig/bertviz (verified loads)
interactive · Attention visualization (head/model/neuron views) via pre-loaded Colab notebook — no coding needed, just open and click · 15-20 min · free · Apache-2.0, actively-starred · Caveats: Colab intimidates some non-coders even pre-loaded; offer as optional deeper dive · Serves: Ch-01 (attention concept)

### R2D3 — A Visual Introduction to Machine Learning — https://r2d3.us/visual-intro-to-machine-learning-part-1/ (verified loads)
interactive · Scrollytelling animated explanation of how a basic ML classifier learns (SF-vs-NYC houses decision tree) · 15-20 min · free · 2015 classic, still functioning and recommended in 2026 · Caveats: predates transformers/LLMs entirely — a "what is ML generally" primer before Ch-01, not a substitute · Serves: Ch-01 prerequisite

### Understanding AI — "LLMs explained with a minimum of math and jargon" — https://www.understandingai.org/p/large-language-models-explained-with (verified loads, no paywall)
essay · Lee & Trott: word vectors, attention, feed-forward layers via plain analogies; independently praised ("most lucid plain-English breakdown", SE-27) · 20-30 min · free · July 2023, still actively cited · Caveats: none significant — near best-in-class for Ch-01 core reading · Serves: Ch-01 — likely the single essay to lead with

### Jay Alammar — "The Illustrated Transformer" — https://jalammar.github.io/illustrated-transformer/ (verified loads)
essay · Canonical diagram-heavy transformer walkthrough; used at Stanford/Harvard/MIT/Princeton/CMU as standard first read · 30-45 min · free · June 2018, updated 2025 — still the reference · Caveats: assumes "neural network"/"embedding" as known terms — read after the Understanding AI piece · Serves: Ch-01 deeper pointer

### One Useful Thing (Ethan Mollick) — https://www.oneusefulthing.org/ (verified loads)
blog/person · Wharton professor on practical AI implications for work/education; research-grounded, 450k+ subscribers · 5-10 min/post · free · very active · Caveats: business/education beat, not mechanics · Serves: prompting / workplace-use / education chapters

### Simon Willison's Weblog — https://simonwillison.net/ (verified active through Aug 2026)
blog/person · Independent developer tracking releases, agents, prompt injection, hands-on testing; skeptical-but-fair, accessible informal benchmarks · short posts, several/week · free · Caveats: writes primarily for developers — filter to conceptual/security posts for this audience · Serves: prompting, agents, security chapters

### AI Snake Oil → AI as Normal Technology — https://www.aisnakeoil.com/ → **https://www.normaltech.ai/** (redirect verified live)
blog/person · Princeton researchers' critical analysis: what AI can/can't do, debunking overclaims; credentialed anti-hype counterweight (book: "AI Snake Oil", Princeton UP) · 10-15 min/post · free · 82k+ subscribers, active · Caveats: **rebranded + moved domains** — use the new URL; book vs newsletter now distinctly branded · Serves: "evaluating AI claims" / keeping-up chapters

## NEAR-MISSES

- **Wolfram, "What Is ChatGPT Doing…"** — likely the second-most-cited plain-language explainer after Karpathy; excluded ONLY because WebFetch hit a persistent TLS certificate error (×4) on the domain; well-corroborated secondhand. Re-check with browser-based access before chapter finalization.
- **Guardian visual explainer** ("How AI chatbots work", Nov 2023) — fetch tool refuses the domain; content via search extraction looked well-suited. Follow up with a different fetch path.
- **FT "Generative AI exists because of the transformer"** (Sept 2023) — same domain-refusal; corroborated as unusually free/open-access (SE-31).
- **Class Central** — the one genuine maintained meta-directory for this audience; 403 on every page. Retry with browser rendering.
- **OpenAI Tokenizer** — 403 ×2; unverified. HF playground substitutes.
- **Hannibal046/Awesome-LLM** — loads fine, actively maintained, but research-paper/framework altitude.
- **owainlewis/awesome-artificial-intelligence** — mixed audience, thin beginner section.
- **KDnuggets "10 Free Resources"** — most entries assume coding despite framing.
- **Cohere LLM University** — developer/API-integration focus.
- **DeepLearning.AI Prompt Eng. for Developers** — requires Python; wrong fit.
- **gpt-tokenizer.dev** — resolves but JS-thin; unconfirmed beyond title.

## COVERAGE NOTE

- **Curated-lists category is a genuine gap**: every awesome-list checked skews engineer/researcher; no verified list aimed at conceptual non-coder learners was found. Follow-up: retry Class Central with browser rendering; hunt specifically for non-practitioner lists.
- **Three high-reputation resources fell out on fetch technicalities, not quality** (Wolfram essay, Guardian, FT) — targeted re-check with different tooling before the chapter is finalized.
- **Blogs/people category thin (3 entries)**: didn't chase Melanie Mitchell, Gary Marcus, Zvi Mowshowitz etc. — worth a dedicated pass mapping hype-positive vs skeptical vs neutral-technical beats.
- **Not explored**: non-English resources (Elements of AI is multilingual, noted in passing); accessibility of interactive tools (Bycroft's 3D likely poor for screen readers — flag to chapter writer).

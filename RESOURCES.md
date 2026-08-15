# Learning resources

Captured during research sessions (D-008): things worth recommending to a smart non-engineer learning AI. Capture happens inline during research; curation and ranking happen when Chapter 16 is researched and on refresh passes. Dead or degraded links get pruned on refresh.

Entries from session R1 were link-verified on 2026-08-13 unless marked otherwise. Format: **Name** — link · what/why · time · caveats · (session found).

## Start here (courses, no code)

- **Elements of AI** — https://www.elementsofai.com/ · Free Univ.-of-Helsinki intro-AI course; Part 1 needs no math or programming; 2M+ learners, translated into 20+ languages · ~5–6 h · Part 2 requires Python — stop after Part 1 if no-code; broad AI survey, not LLM-specific · (R1)
- **Generative AI for Everyone** (DeepLearning.AI, Andrew Ng) — https://www.deeplearning.ai/courses/generative-ai-for-everyone/ · Non-technical course specifically on how generative AI/LLMs work + prompting basics · ~5 h · freemium; verify Coursera pricing at signup · (R1)
- **AI For Everyone** (DeepLearning.AI, Andrew Ng) — https://www.deeplearning.ai/courses/ai-for-everyone/ · Non-technical what-AI-can/can't-do with organizational framing · ~7 h · $49 certificate track; thinner on LLM mechanics than the GenAI course · (R1)
- **Google AI Essentials** — https://grow.google/ai-essentials/ · Beginner practical genAI use, five modules · <5 h · $49/month subscription after trial — a real barrier vs the free options · (R1)
- **Anthropic Academy: AI Fluency** — https://anthropic.skilljar.com/ai-fluency-framework-foundations · Free structured course teaching a when-to-trust/delegate/verify decision framework rather than button-clicking · self-paced · vendor-produced; scan for self-serving framing · (R1)

## Videos

- **3Blue1Brown — "But what is a GPT?"** (Deep Learning ch. 5) — https://www.3blue1brown.com/lessons/gpt · Best-in-class visual intuition for transformers; free, no product agenda · ~27 min (2–3 h with lead-up chapters) · assumes patience for visualized math; pair with a prose companion · (R1)
- **Karpathy — "[1hr Talk] Intro to Large Language Models"** — https://www.youtube.com/watch?v=zjkBMFhNj_g · Probably the single best "one hour and you get it" general-audience talk · ~1 h · field-as-of-Nov-2023; pair with something current · (R1)
- **Karpathy — "Deep Dive into LLMs like ChatGPT"** — https://www.youtube.com/watch?v=7xTGNNLPyMI · Full training stack (pretraining → SFT → RLHF → reasoning models) for people who use ChatGPT, per Karpathy's own framing · 3.5 h — a real commitment; the "go deeper" pick, not first touch · (R1)
- **Karpathy's channel generally** — https://www.youtube.com/@AndrejKarpathy · Includes build-it-yourself videos for readers who outgrow conceptual explanations · hours · from-scratch videos assume Python · (R1)

## Interactive tools

- **Transformer Explainer** (Georgia Tech/IBM) — https://poloclub.github.io/transformer-explainer/ · Live GPT-2 in the browser: type text, watch next-token prediction with zoomable plain-language↔math views; likely the best single interactive · 10–30 min · GPT-2-scale example, not a frontier model · (R1)
- **LLM Visualization** (Brendan Bycroft) — https://bbycroft.net/llm · 3D step-by-step walkthrough of inference down to individual matrix operations · 20–40 min · dense; second stop after basic vocabulary · (R1)
- **Tokenizer Playground** (Hugging Face) — https://huggingface.co/spaces/Xenova/the-tokenizer-playground · Makes "the model sees tokens, not words" tangible in ten seconds · 5–10 min · OpenAI's official tokenizer page couldn't be verified by our tooling; this one was · (R1)
- **BertViz** — https://github.com/jessevig/bertviz · Attention visualization via pre-loaded Colab, no coding needed · 15–20 min · Colab intimidates some non-coders; optional deeper dive · (R1)
- **R2D3 — A Visual Introduction to Machine Learning** — https://r2d3.us/visual-intro-to-machine-learning-part-1/ · Gentle scrollytelling on how a basic classifier learns; good "what is ML at all" pre-primer · 15–20 min · predates LLMs entirely — prerequisite framing, not a substitute · (R1)
- **Anthropic — Scaling Monosemanticity feature demos** — https://transformer-circuits.pub/2024/scaling-monosemanticity/ · The Golden-Gate-Bridge-feature demo is a genuinely concrete "aha" for what's inside a model · ~10 min for the demo · vendor framing; the raw finding is solid, the interpretation is theirs · (R1)

## Essays & books

- **Understanding AI — "Large language models, explained with a minimum of math and jargon"** (Lee & Trott) — https://www.understandingai.org/p/large-language-models-explained-with · Independently praised as the most lucid plain-English LLM explainer; the single essay to lead with · 20–30 min · none significant · (R1)
- **Jay Alammar — "The Illustrated Transformer"** — https://jalammar.github.io/illustrated-transformer/ · The canonical diagram walkthrough, used as the standard first read at several universities · 30–45 min · assumes "neural network"/"embedding" as known terms; read second · (R1)
- **Wolfram — "What Is ChatGPT Doing … and Why Does It Work?"** — https://writings.stephenwolfram.com/2023/02/what-is-chatgpt-doing-and-why-does-it-work/ · Unusually complete single-author account from letter-frequencies to RLHF · 1–2 h · conflict of interest: pitches his own symbolic-computation ecosystem as the fix — read "solution" sections accordingly; site is fetch-flaky (TLS), verified only via proxy/secondaries · (R1)
- **Anthropic — "On the Biology of a Large Language Model"** — https://transformer-circuits.pub/2025/attribution-graphs/biology.html · Unusually accessible primary research: heavily visual worked examples (poetry planning, arithmetic, the hallucination circuit) · 45–90 min skimming the boxed examples · long; skip the methods appendix · (R1)
- **Ted Chiang — "ChatGPT Is a Blurry JPEG of the Web"** (New Yorker, 2023) · The compression analogy at its best, including the author naming its own failure mode · ~20 min · paywalled · (R1)
- **Narayanan & Kapoor — "AI Snake Oil"** (Princeton UP, 2024) — https://press.princeton.edu/books/hardcover/9780691249131/ai-snake-oil · Possibly the best-calibrated general-audience book: neither doom nor hype, by named computer scientists · book-length · broader than LLMs (predictive AI too) · (R1)
- **Julian Michael — "To Dissect an Octopus"** — https://julianmichael.org/blog/2020/07/23/to-dissect-an-octopus.html · Best accessible route into the Bender–Koller "fluent ≠ understanding" thought experiment · ~15 min · philosophical argument, not empirical proof · (R1)
- **IEEE Spectrum — Bender interview on "stochastic parrots"** — https://spectrum.ieee.org/stochastic-parrot · The strongest accessible statement of the skeptical position on machine "knowing" · ~8 min · one side of a live debate; pair with the interpretability side · (R1)

## Reasoning / thinking models (session R2)

- **Understanding Reasoning LLMs** (Sebastian Raschka) — https://magazine.sebastianraschka.com/p/understanding-reasoning-llms · The clearest single account of how reasoning models are built · ~25 min · one diagram's worth of technical tolerance required · (R2)
- **The Illustrated DeepSeek-R1** (Jay Alammar) — https://newsletter.languagemodels.co/p/the-illustrated-deepseek-r1 · Visual walkthrough of a reasoning model's training recipe, by the author of the transformer explainer many people learn from · ~20 min · (R2)
- **What We Mean When We Say "Think"** (David Breunig) — https://www.dbreunig.com/2025/04/11/what-we-mean-when-we-say-think.html · Short essay directly on the anthropomorphism trap in vendor UI language · ~8 min · (R2)
- **Reasoning models don't always say what they think** (Anthropic) — https://www.anthropic.com/research/reasoning-models-dont-say-think · A lab publishing that its own product's explanations are unreliable; worked examples are the clearest part · ~15 min · admission-against-interest, which is why it's worth reading · (R2)
- **Claude's extended thinking docs** — https://platform.claude.com/docs/en/build-with-claude/thinking · Five minutes here tells you exactly what your own interface is and isn't showing you, and what you're billed for · ~5 min · vendor docs, but this is the authoritative place for product mechanics · (R2)
- **Chain of Thought Monitorability** (multi-lab position paper) — https://arxiv.org/abs/2507.11473 · Why the field treats a readable trace as a safety property worth protecting, and what would break it · ~30 min for the framing sections · technical, but the opening is accessible · (R2)
- **Notes on OpenAI's o1** (Simon Willison) — https://simonwillison.net/2024/Sep/12/openai-o1/ · A careful practitioner's first reaction, preserved — useful for seeing what was and wasn't obvious at the time · ~10 min · (R2)
- **DeepSeek R1's recipe** (Nathan Lambert, Interconnects) — https://www.interconnects.ai/p/deepseek-r1-recipe-for-o1 · Post-training specialist on what the open replication actually showed · ~15 min · assumes some ML vocabulary · (R2)
- **Is AI Reasoning Right for the Wrong Reasons?** (Quanta) — https://www.quantamagazine.org/is-ai-reasoning-right-for-the-wrong-reasons-20260731/ · General-audience entry to the collapse debate · ~15 min · (R2)

**Gap:** no verifiable good *video* explainer of reasoning models was found (R2). One candidate couldn't be verified because YouTube transcripts are unreachable with our tooling. Contributions welcome.

**Rejected, and why** (R2): a "5 Best AI Reasoning Models" listicle with unsourced benchmark percentages and no method; a hands-on reasoning course requiring Python (wrong audience, same pattern as R1's rejection); a hallucination-detection vendor's blog on a rival model's hallucination rate (direct commercial incentive, unvetted); an interactive trace visualizer that requires you to already have a trace to paste.

## People & blogs to follow

- **Simon Willison** — https://simonwillison.net/ · Clearest skeptical-but-fair practitioner tracking of what new models actually do; start with "a calculator for words" (2023) · several short posts/week · writes for developers; filter to conceptual/security posts · (R1)
- **Melanie Mitchell — "AI: A Guide for Thinking Humans"** — https://aiguide.substack.com · The most careful non-hyperbolic capability analysis found this session; a good default second opinion on any big claim · ~10 min/post · has a named skeptical prior · (R1)
- **Ethan Mollick — One Useful Thing** — https://www.oneusefulthing.org/ · Research-grounded practical-use beat for non-technical readers · ~10 min/post · practical-use focus, not mechanics; hype-warm — discount accordingly · (R1)
- **Sayash Kapoor (& formerly Arvind Narayanan) — AI as Normal Technology** — https://www.normaltech.ai/ · Credentialed anti-hype counterweight · ~10–15 min/post · note: rebranded from "AI Snake Oil" and moved domains — old links redirect · (R1)
- **Sebastian Raschka** — https://sebastianraschka.com/ · Exact formulas with worked numeric examples; the "graduate to this next" technical stop · ~10 min/entry · denser than the rest of this list · (R1)
- **Nathan Lambert — Interconnects** & **Hugging Face blog** — https://huggingface.co/blog · Post-training and open-model developments explained by practitioners · ~15 min/post · assumes some ML vocabulary · (R1)
- **Neel Nanda — mechanistic interpretability write-ups** — https://www.neelnanda.io/mechanistic-interpretability/othello · Clearest plain-language account of how researchers test what's inside a model, by someone who does it · 20–30 min · assumes comfort with the probe/vector idea · (R1)
- **Jason Wei — "Common arguments regarding emergent abilities"** — https://www.jasonwei.net/blog/common-arguments-regarding-emergent-abilities · A scientist steelmanning the critique of his own famous result — worth reading for the epistemic style alone · ~15 min · still a defense; read alongside Schaeffer et al. · (R1)

## Podcasts

- **Mystery AI Hype Theater 3000** (Bender & Hanna, DAIR) — https://dair-institute.org/maiht3k/ · Entertaining hype-debunking; builds critical-listening habits · 45–60 min/ep · strongly one-sided (deflationary); pair with the other side · (R1)

## Reference datasets & explainers

- **Damien Charlotin — AI Hallucination Cases database** — https://www.damiencharlotin.com/hallucinations/ · Searchable court-case database that makes hallucination's real-world stakes concrete · 5–15 min · legal-domain skew; our tooling hit a 403 — verify access in a normal browser · (R1)
- **Quanta — "'World Models,' an Old Idea in AI, Mount a Comeback"** — https://www.quantamagazine.org/world-models-an-old-idea-in-ai-mount-a-comeback-20250902/ · Clearest general-audience on-ramp to the world-model debate · ~15 min · partly about robotics/video models · (R1)

## Known gaps (for the Ch-16 session)

- No verified curated list aimed at conceptual non-coder learners exists among those checked — every awesome-list skews practitioner (R1 finding).
- Guardian and FT visual explainers (both well-corroborated) and Class Central could not be verified by session tooling — recheck in a normal browser.
- People-to-follow list is Anglophone/US-skewed; hype-positive vs skeptical vs neutral beats deserve a dedicated mapping pass.

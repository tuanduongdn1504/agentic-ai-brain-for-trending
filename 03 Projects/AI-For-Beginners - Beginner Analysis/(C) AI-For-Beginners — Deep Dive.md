# (C) AI-For-Beginners — Deep Dive (v191)

> **Wiki v191** · built 2026-07-03 · subject `microsoft/AI-For-Beginners` · source snapshot pinned at commit **`3662ce1`** (2026-07-02T15:04:45Z) · 169 non-translation text files fetched per-file from raw.githubusercontent (WebFetch-first fallback — the v6 precedent; a full clone was infeasible: the 50+ translation trees push the pack past ~1.1 GB and the local git 2.19.0 lacks `sparse-checkout`).
> Companion docs: `(C) AI-For-Beginners — Verdict.md` · `(C) AI-For-Beginners — Pilot Methods Menu.md` · `wiki.html`.

## TL;DR

**AI for Beginners** is Microsoft's free, MIT-licensed, 12-week / 24-lesson curriculum on classical AI and deep-learning fundamentals — symbolic AI → neural networks → computer vision → NLP (through transformers/BERT and a short LLM/prompt-engineering lesson) → genetic algorithms / deep RL / multi-agent systems → AI ethics. It is the **foundations layer of the Microsoft "-for-Beginners" franchise** whose upper floors are Generative-AI-for-Beginners, **AI-Agents-for-Beginners (= this corpus's v6 subject)** and MCP-for-Beginners. Scale: 51.3k★ / 10.3k forks (page/API-stated, §37.4), 42 Jupyter notebooks (most in **both TensorFlow and PyTorch**), 12 labs, a Vue quiz app, sketchnotes, and **50-language automated translation** via Azure/co-op-translator. It teaches **what Claude is made of** (embeddings → attention → transformers → LLMs) but contains **zero Claude/Anthropic content** (grep-verified) and its NLP arc is BERT-era — including a flat-out wrong "GPT-4 = 100T parameters" table cell (hand-verified in source). The most curious 2026 fact: this pre-LLM curriculum is now **maintained by agents** — a root `AGENTS.md` onboarding doc, Copilot Autofix/Dependabot commits, and the pinned HEAD itself is a merged `copilot/fix-review-comments` PR.

## Identity card

| Field | Value |
|---|---|
| Repo | `microsoft/AI-For-Beginners` (aka.ms/ai-beginners; docs site microsoft.github.io/AI-For-Beginners, Docsify) |
| License | MIT |
| Language | Jupyter Notebook ~100% (page-stated) |
| Scale | 51.3k★ / 10.3k forks / ~100+ contributors / 0 releases (page/API-stated, §37.4 — no velocity claims) |
| Created | 2021-03-03 (API-stated); content substantially developed 2022; announced via Soshnikov's blog |
| Pinned | commit `3662ce1` = merged PR #680 `copilot/fix-review-comments` (2026-07-02) |
| Primary author | **Dmitry Soshnikov, PhD** (README-verified; web-reported: ex-Microsoft Cloud Advocate ~16 yrs, associate professor HSE/MAI Moscow, now leads an AI Lab at HSE Art & Design — no longer at Microsoft) |
| Editor | **Jen Looper, PhD** (web-reported: architect of the -for-Beginners franchise, announced Web-Dev-for-Beginners Nov 2020; in 2026 Director of DevRel at Cloudinary) |
| Other credits | Tomomi Imura (@girlie_mac, sketchnotes) · Lateefah Bello (quizzes, MLSA) · Evgenii Pishchik (core contributor) |
| Top committers | leestott (295) · skytin1004 (238) · jlooper (168) · shwars/Soshnikov (102) (API-stated) |

## What it is — curriculum architecture (hand-verified against the snapshot tree)

README line 21 (verbatim): *"Explore the world of **Artificial Intelligence** (AI) with our 12-week, 24-lesson curriculum! It includes practical lessons, quizzes, and labs. The curriculum is beginner-friendly and covers tools like TensorFlow and PyTorch, as well as ethics in AI."*

Real directory sections (`lessons/`): `0-course-setup` · `1-Intro` · `2-Symbolic` · `3-NeuralNetworks` · `4-ComputerVision` · `5-NLP` · `6-Other` · `7-Ethics` · `X-Extras` · `sketchnotes`.

| # | Section | Lessons | On-goal notes |
|---|---|---|---|
| 1 | Intro | 01 History of AI | GPT-3/BERT already named as the "huge successes" (line 142) |
| 2 | Symbolic AI | 02 Knowledge representation, expert systems, ontologies | the pre-ML half of AI most modern curricula skip |
| 3 | Neural Networks | 03 Perceptron · 04 Multi-layer + **build-your-own framework** · 05 Frameworks (TF/PyTorch) + overfitting | the from-scratch layer (v74 LLMs-from-scratch's spiritual sibling) |
| 4 | Computer Vision | 06 CV intro/OpenCV · 07 CNNs · 08 Transfer learning · 09 Autoencoders/VAE · 10 GANs · 11 Object detection · 12 Segmentation | CNN-era; ViT only in Extras |
| 5 | NLP | 13 TextRep (BoW/TF-IDF) · 14 Embeddings (Word2Vec/GloVe) · 15 Language modeling · 16 RNN · 17 Generative RNN · 18 **Transformers/BERT** · 19 NER · 20 **LLMs + prompt engineering** | **the "what Claude is made of" spine** |
| 6 | Other AI | 21 Genetic algorithms · 22 Deep RL (Gym/CartPole, policy gradient + actor-critic) · 23 **Multi-Agent Systems** | classic-MAS vocabulary |
| 7 | Ethics | 24 **AI Ethics / Responsible AI** | the flagship fairness example is **hiring bias** |
| X | Extras | X1 Multimodal (CLIP, VQGAN, DALL-E) | the only post-2021 generative-vision content |

## The learning machinery (the transferable gold for a Scrum coach)

Hand-verified lesson template (from `3-NeuralNetworks/03-Perceptron/README.md`): title → **[Pre-lecture quiz]** (ff-quizzes.netlify.app/en/ai/quiz/N) → content sections → Conclusion → **🚀 Challenge** → **[Post-lecture quiz]** → **Review & Self Study** → **[Assignment]** (`lab/README.md` + a lab notebook, e.g. `PerceptronMultiClass.ipynb`).

- **42 notebooks**, most lessons offering **parallel TensorFlow AND PyTorch implementations** (framework-agnostic pedagogy — you learn the concept, not the API).
- **12 `lab/` directories** (12/24 lessons) — independent exercises with their own notebooks, vs the guided lesson notebooks.
- **Quiz app**: Vue 2.6 + vue-i18n + vue-router (`etc/quiz-app/`); quizzes stored as per-lesson JSON under `assets/translations/<lang>/`; served online (ff-quizzes.netlify.app) or locally; deployable to Azure Static Web Apps. ⚠️ The README's own quiz counts are inconsistent (a "40 quizzes / 50 questions" line vs 24 lesson files × pre+post) — flagged, not resolved.
- **Sketchnotes** by Tomomi Imura (`lessons/sketchnotes/`, PNG; excluded from our text snapshot).
- **Microsoft Learn links** in ~7 lesson files (lower density than the README implies) + a Learn collection.
- **5 documented run paths** (`0-course-setup/how-to-run.md`): local conda (`environment.yml`, env `ai4beg`) · VS Code + devcontainer · local Jupyter · **GitHub Codespaces** · **Binder** (free but "access blocked resources", slow — disclosed).
- **requirements.txt hand-read**: `tensorflow==2.17.0`, `keras==3.13.2`, `gym==0.26.2`, `gensim==4.3.3`, `nltk==3.9.4`, `tokenizers==0.20.0`, pandas 2.2.2 — pins refreshed relatively recently (this is NOT an abandoned 2022 freeze).

## The NLP → LLM spine (lessons 13–20), hand-read

This is the corpus-relevant core: the shortest credible path from "what is a token, really" to "what is Claude, architecturally".

- **L13–15**: BoW/TF-IDF → Word2Vec/GloVe embeddings → training embeddings + language modeling. Durable: the geometric intuition for semantic similarity that underlies modern retrieval/matching.
- **L16–17**: RNNs and generative RNNs — taught as the stepping stone (historically honest, but the lessons do not carry a "transformers replaced this in production" banner).
- **L18 Transformers/BERT** (hand-fetched): attention as weighting the "contextual impact of each input vector on each output prediction"; positional encoding (sinusoidal formulae); multi-head attention "to capture several different types of dependencies"; BERT + DistilBERT; notebooks in both frameworks via HuggingFace. **Encoder/BERT-centric; GPT mentioned, decoder-only era not developed.**
- **L20 LLMs / Prompt Programming** (hand-fetched + hand-grepped): GPT family framing ("GPT is not a single model, but rather a collection of models"), few-shot/zero-shot framing, perplexity, a **Prompt Engineering section**, and one notebook — `GPT-PyTorch.ipynb` (HuggingFace GPT-2 text generation; **no OpenAI/Azure API notebook in this lesson**, despite what its filenames suggest to a skimmer).
- **The verified error** (`lessons/5-NLP/20-LangModels/README.md:32`, verbatim table cell): GPT-2 *"upto 1.5 billion parameters"* | GPT-3 *"up to 175 billion parameters"* | GPT-4 **"100T parameters and accepts both image and text inputs and outputs text."** The 100T figure is folklore — never confirmed, contradicted by every credible estimate — and is stated **without hedging**. A beginner leaves this lesson misinformed about the single most-cited LLM scale fact.
- **What's absent for 2026**: tokenizers as a first-class concept, context windows, RLHF/instruction-tuning (why Claude ≠ base GPT-2), scaling laws, RAG, function/tool calling, agent loops. The README itself routes generative-AI learners to the sibling course (line 74: the *"Generative AI with Azure OpenAI Service"* path; Other-Curricula section → Generative-AI-for-Beginners).

## Lessons 21–24 — the two vault-relevant surprises

**L23 Multi-Agent Systems** (hand-grep-verified quotes): the *"**emergent** (or **synergetic**) approach"* — intelligence from *"[the] combined behavior of [many relatively simple agents]"*; **Agent** = *"an entity that lives in some **environment**, which it can perceive, and act upon"*; reactive/deliberative + passive/active/cognitive taxonomies; **BDI architecture**; KIF/KQML agent-communication languages; NetLogo flocking (alignment/cohesion/separation). This is the **1990s-2000s vocabulary of exactly what the vault does daily in 2026** — except modern practice inverted it: learned reasoning instead of hardcoded rules, top-down orchestration instead of bottom-up emergence, natural language instead of KQML. A one-page "then vs now" mapping is a genuinely useful vault artifact (pilot B6).

**L24 Ethics / Responsible AI** (hand-grep-verified): six principles — Fairness, Reliability & Safety, Privacy & Security, Inclusiveness, Transparency, Accountability — plus the **Microsoft RAI Toolbox**: InterpretML (interpretability), **Fairlearn** (bias detection), Error Analysis, EconML (causal), DiCE (counterfactual). The flagship fairness example, verbatim (`lessons/7-Ethics/README.md:15`): *"when we try to predict the probability of getting a **software developer job** for a person, the model is likely to give higher [preference to males]"* — **the lesson's own example domain is hiring**, i.e. hireui's product domain. This is the most directly applicable page in the whole curriculum (pilots B8/D13/D14).

## Infrastructure & maintenance — the 2026 state

- **Maintenance mode: automation-heavy steady state.** 321 commits since 2025-01-01 (API-stated) but the last ~30 are dominated by translation syncs, Dependabot, **Copilot Autofix**, and housekeeping PRs; lesson content itself is not visibly evolving. Dependency pins ARE refreshed; the *architecture* of the content is 2022's.
- **`AGENTS.md` at repo root** (hand-read): a full agent-onboarding doc — project overview, setup commands, key technologies, architecture map — i.e. the curriculum is set up so **coding agents can maintain it**, and they visibly do (HEAD = merged `copilot/fix-review-comments`). An education repo that predates the LLM era, now agent-operated. No CLAUDE.md / copilot-instructions.md / .cursorrules (checked).
- **Translations**: 50 languages **machine-translated and kept in sync** by the **Azure/co-op-translator** GitHub Action (66 releases, ~625★, v0.19.2 Jun-2026 — web-reported). Includes Vietnamese. This is franchise-wide infrastructure — a different mechanism from human-translated i18n (cf. easy-vibe v77's 13 human locales).
- **CI**: CodeQL + OpenSSF Scorecard. **Install risk: VERY LOW** (audited — no postinstall/curl|bash/telemetry; standard conda/pip ML deps; datasets from official sources; Kaggle sets manual-download).
- **Community**: Discord + Azure AI Foundry Developer Forum; issue templates for lesson corrections + translation feedback; repeated community requests for certificates (none offered).

## The franchise (where this sits — web-reported, URLs verified by redirect where noted)

Microsoft's stated internal sequence: **ML-for-Beginners** (87.6k★, classic ML, no deep learning) → **AI-for-Beginners** (this; symbolic AI + neural nets + DL) → **Generative-AI-for-Beginners** (113k★, 21 lessons + setup; L17 = AI agents) → **AI-Agents-for-Beginners** (68.4k★, 15 lessons — **corpus subject v6**, taken as the operator's fork in Apr 2026 when it was 10+4 lessons) → **MCP-for-Beginners** (16.7k★, 12 modules). Side branches: Edge-AI (SLMs + agents), LangChain×3 (agent-first), GenAI-.NET/Java/JS (agent-heavy), Web-Dev/Data-Science/IoT/Cybersecurity/XR (non-AI or archived), Copilot series. **No unified landing page exists** — the franchise is stitched by aka.ms short-links and each README's "Other Curricula" section. Several siblings also carry AGENTS.md files.

Positioning vs the landscape (web-reported, common knowledge — held loosely): fast.ai = top-down code-first DL for coders; Karpathy Zero-to-Hero = bottom-up from autograd to GPT (the closest LLM-era complement to this course's L13–20); HuggingFace courses = library-centric NLP/agents; Ng/deeplearning.ai = MOOC-style theory. **AI-for-Beginners' unique cells**: symbolic AI + AI history, dual-framework parallel notebooks, ethics as a first-class lesson, 50-language accessibility, institutional MIT-licensed openness. **Its weakest cell in 2026**: everything after 2021 (LLM-era depth).

## Honest caveats (the errata sheet)

| # | Caveat | Evidence |
|---|---|---|
| 1 | **"GPT-4 = 100T parameters" stated as fact** | `lessons/5-NLP/20-LangModels/README.md:32`, hand-verified verbatim |
| 2 | NLP arc is BERT/RNN-era; no RLHF, tokenizer-as-concept, context windows, RAG, tool calling, agent loops | hand-reads L16–20 |
| 3 | Content in maintenance mode — bots + translations dominate 2025–26 commits; lesson architecture unchanged since ~2022 | commit profile (API-stated) |
| 4 | CNN-era CV; ViT/CLIP only in Extras | tree + L6–12 notes |
| 5 | README's own quiz-count arithmetic is inconsistent | README lines 21/38/159–161 |
| 6 | MS Learn links are external dependencies (and sparser than implied — ~7 lesson files) | hand-grep |
| 7 | Some lessons GPU-preferred; Binder path resource-starved (disclosed in-source) | how-to-run.md |
| 8 | Metrics are page/API-stated (§37.4) — no velocity claims | discipline |

## Verification methodology (for the audit)

15-agent read-only workflow (`wf_3d05777c-6d2`, ~2.08M tokens: 8 source readers + 4 web researchers + 2 auditors + 1 critic) over the pinned snapshot. **Six readers returned zero-tool-call, parametric-memory notes** (caught via per-agent `toolCalls` metadata + snapshot greps): fabricated paths (`lessons/18-Transformers/Transformers.md`, a `for-teachers/` directory, React quiz app, OpenAI/Azure notebooks in L20), a reworded "100T" quote, an invented weekly-cadence schedule. **All discarded.** Everything load-bearing in this document is either (a) my own hand-fetch/hand-grep of the pinned snapshot (README, L18, L20, L23, L24, requirements.txt, AGENTS.md, quiz-app package.json, lesson-3 template, tree listings, Claude-mention grep = zero hits), or (b) one of the 8 verified tool-using agents, marked page-stated/web-reported where applicable. Corpus claims (v6 sibling, prior Microsoft subjects, T3 tier, i18n records) were grep-verified by hand in `_state/` + `_patterns/` per `feedback_wiki_verify_independently_check_collisions`.

# Overview — Cole Medin on Google's Open Knowledge Format (OKF)

**Source:** [T33iI6izAKw](https://www.youtube.com/watch?v=T33iI6izAKw) (Cole Medin, 2026-07-02, 19:37). Full transcript: `raw/2026-07-15-okf-open-knowledge-format.md`.

A 20-minute explainer-plus-plug: Cole introduces **OKF**, argues it's "the future of personal agents," walks through the SPEC and a traditional Karpathy wiki, and gives away an OKF "bundle" of his own AI-coding videos as a working example.

## The argument, in order

1. **The Karpathy LLM Wiki took off [00:02].** A "couple months ago" (actually ~3 months — gist created 2026-04-04) Karpathy published the LLM-wiki *pattern*: instead of dumping docs into RAG, have the LLM incrementally build and maintain a persistent, cross-linked markdown wiki — reading each new source, extracting key info, updating entity pages, so the agent can traverse a knowledge graph. Cole says the gist "got to **40,000 stars**" — **this is wrong; it's ~5,000** (see [[caveats-and-corrections]]).

2. **The problem: no standard [01:25].** When everyone one-shots their own wiki from the gist, each is structured differently — different metadata (`tags` vs `categories`), different folders, different link conventions. So you **can't hand your wiki to someone else's agent** and have it search optimally. Use cases that need this: team wikis, sharing a curated knowledge base with colleagues, a creator packaging their content for followers.

3. **The fix: Google's OKF [01:53].** A "beautifully simple" standard *on top of* Karpathy's pattern that guarantees your wiki is built in a way other agents can consume, and vice-versa. Cole frames it as *"like what MCP did for agent-to-tool communication, OKF does for agent-to-knowledge-base communication"* — his analogy, not Google's ([[claims-scorecard]] grades it OPINION).

4. **What OKF standardizes — two things [03:14]:** (a) **how you organize** — entity/concept documents, indexes within folders + a top-level index; (b) **the exact metadata fields** — YAML frontmatter at the top of every doc. **`type` is the single required field** (it gives categorization so agents can filter/traverse); `title`, `tags`, `related`, etc. are optional/recommended. Full detail: [[what-okf-standardizes]].

5. **Building with it [06:47].** Point your coding agent at the SPEC.md, tell it to build a new OKF wiki or **refactor an existing one** — "like a skill," it teaches the agent the terminology, bundle structure, and frontmatter. For big wikis, use **sub-agents** to refactor sections in parallel. (Cole's "GPT 5.5 or Opus 4.8 can handle it" — both are real models; ✅.)

6. **Why it matters even if you never share [09:35].** A common standard lets people exchange *structural ideas* ("here are the entity pages working well for me"). Cole hedges: *"I don't think OKF is going to in the end be the standard, but we're going to see something like it"* — a hedge the [[thesis-critique]] argues undercuts his own case.

7. **The gift: his OKF bundle [11:00].** [`coleam00/cole-medin-ai-coding`](https://github.com/coleam00/cole-medin-ai-coding) packages his best AI-coding videos as an OKF "bundle." You clone it, give your agent the SPEC + a prompt, and query it. Cole says it has "**four videos**" — **it actually has five** (see [[caveats-and-corrections]]). He also says it brings the bundle "into your local Obsidian or Notion" — **the README describes clone + read-markdown / a small `okf-cli.py`, no Obsidian/Notion import** (MISLEADING).

8. **The demo [16:25].** He asks his second brain "what bundles do I have?" (CLI lists them), then "What's Cole's single biggest idea for reliable AI code?" — the agent does progressive disclosure (index → concepts → reads `context-engineering`) and answers. (Note: the agent surfaced *context engineering*, not the "PIV loop" Cole elsewhere calls his "primary mental model" — a small inconsistency.)

9. **"Is OKF too simple?" [17:33].** Cole concedes a "valid" critique — OKF adds little on top of Karpathy (basically folder/index organization + a couple metadata conventions). His rebuttal: **that's the point.** Minimally-opinionated = the bare-minimum interoperability layer, and that's a feature. ([[thesis-critique]] disputes this for the *personal* use case; the [[what-okf-standardizes]] article notes Cole *understates* what OKF actually adds.)

## The one-line verdict

OKF is **real, official Google, genuinely useful, and genuinely minimal.** The video is **accurate on the substance** and **sloppy on the numbers**, and its **framing inverts Google's actual (enterprise) emphasis** — see [[personal-vs-enterprise-framing]]. For *this vault*, the interesting part isn't the video's hype; it's that the vault **is** a Karpathy wiki and could adopt OKF: [[vault-adoption-pilot]].

## Key Takeaways

- OKF = a thin standard formalizing the Karpathy LLM-wiki pattern; markdown + YAML frontmatter; **only `type` is required**.
- It's a real Google Cloud release (Apache-2.0, launch blog 2026-06-13), **built for enterprise data sharing** but honestly usable for personal wikis too.
- Cole's technical explanation is trustworthy; **don't quote his numbers** (40K stars → ~5K; four videos → five).
- The video's biggest distortion is **emphasis**, not fact: personal-second-brain framing over Google's enterprise-first intent.
- The corpus-relevant question is **not** "is the video right" but "**should this vault adopt OKF?**" → [[vault-adoption-pilot]] (verdict: WATCH, run one 40-minute experiment).

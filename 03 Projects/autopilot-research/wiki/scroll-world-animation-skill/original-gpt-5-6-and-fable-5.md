# Originals: GPT-5.6 Sol (OpenAI) and Claude Fable 5 (Anthropic)

## Source

Main-loop `WebSearch`/`WebFetch` (2026-07-14), independent of and cross-checking the workflow (`wf_885d81d7-1a2` dive/verify `gpt-5-6-codex-soul`). This article exists because the workflow's own dive for Fable 5 **failed outright** ("Prompt is too long") and its GPT-5.6 verify pass included at least one detail the main loop could not corroborate — both models needed direct, independent confirmation before being asserted in this wiki.

## GPT-5.6 Sol, Terra, Luna (OpenAI) — real, confirmed independently

The video's auto-captions render the model the presenter runs inside OpenAI Codex as "GPT 5.6 Soul." **This is a real model, not a mis-transcription of something else — the caption is a phonetic mishearing of "Sol," which the video's own written description spells correctly ("the new GPT 5.6 Sol").**

Confirmed via a main-loop `WebSearch` against OpenAI's own site and independent press (not just the workflow's Haiku-run research):
- OpenAI's GPT-5.6 is a **three-model family named after the Sun, Earth, and Moon**: **Sol** (flagship — OpenAI's best coding model yet, sets a new state of the art on Terminal-Bench 2.1, strong at long-horizon agentic/cybersecurity tasks), **Terra** (balanced, everyday work), **Luna** (fast, affordable).
- Sources: `openai.com/index/gpt-5-6/`, `openai.com/index/previewing-gpt-5-6-sol/`, `github.blog/changelog/2026-07-09-openais-gpt-5-6-sol-terra-and-luna-are-now-available-in-github-copilot`, TechCrunch ("OpenAI launches its new family of models with GPT-5.6," 2026-07-09), 9to5Mac (limited-release coverage 2026-06-26 and GA coverage 2026-07-09), MarkTechPost (2026-07-09).
- **Timeline:** a limited preview began **2026-06-26**; general availability across ChatGPT, Codex, and the API began **2026-07-09** — exactly **2 days before this video was uploaded** (2026-07-11). The video's "brand new" framing is accurate, not hype.
- **Pricing** (per million tokens): Sol $5 input / $30 output; Terra $2.50 input / $15 output; Luna $1 input / $6 output.
- Sol landed the same day (2026-07-09) inside GitHub Copilot per GitHub's own changelog — independent third-party confirmation this is a real, shipped model family, not vaporware.

**Correction (Rule 12 fail-loud):** one workflow verify agent claimed the June 26 limited preview was restricted to "~20 government-approved organizations" and characterized it as gated "per US gov." **No source found in independent main-loop search corroborates this for GPT-5.6 specifically.** The most likely explanation is that the agent conflated this with the genuinely-real, but *separate*, Anthropic Fable-5 export-control episode below — both stories involve "government" and "limited access" in the same rough time window, which is exactly the kind of surface-similarity a research agent can wrongly merge. **This claim is excluded from the wiki.**

## Claude Fable 5 (Anthropic) — real, and had a genuine recent outage

The workflow's own dive on Fable 5 died with "Prompt is too long" before returning anything, so every fact below comes from the main loop's own search and fetch.

- **Claude Fable 5 is a real, current Anthropic model** — Anthropic's first public "Mythos-class" model, launched **2026-06-09** alongside Claude Mythos 5. Fable 5 is the safety-tuned, generally-available sibling of the pair; built-in safeguards route a small share of queries (under 5% of sessions, per Anthropic) to Claude Opus 4.8 instead of answering directly.
- **Pricing:** $10 per million input tokens / $50 per million output tokens — per Anthropic's own announcement, less than half the price of "Claude Mythos Preview."
- **Availability:** Claude API, Claude Platform on AWS/Bedrock, Google Cloud, and Microsoft Foundry.
- Sources: `anthropic.com/news/claude-fable-5-mythos-5`, `platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5`, `anthropic.com/news/redeploying-fable-5`.

**A detail the video never mentions, worth surfacing on its own:** Fable 5 (and Mythos 5) were **unavailable for 19 days**, from **2026-06-12 to 2026-06-30**. Per Anthropic's own "Redeploying Claude Fable 5" post, fetched directly: the US government applied export controls on June 12 after Amazon researchers found a way to bypass Fable 5's safeguards; the controls required restricting access by nationality, and since Anthropic "had no reliable way to verify nationality in real-time," it suspended access for **all** users, everywhere, rather than partially comply. Access was restored globally starting **2026-07-01**, after Anthropic trained an improved safety classifier and the export controls were lifted.

By the time this video was uploaded (2026-07-11), Fable 5 had been continuously available again for only about 10 days.

## Why this matters for the video

Both AI models the presenter one-shots this website with — GPT-5.6 Sol and Claude Fable 5 — are extremely recent: Sol reached general availability 2 days before upload, and Fable 5 had only just come back from a 19-day, government-triggered outage 10 days before upload. Neither of these facts is disclosed in the video. This doesn't undermine the demo's technical claims, but it's useful context for anyone trying to reproduce this exact workflow: both halves of the "one skill, two AI stacks" comparison were running on models that had been stable in their current form for less than two weeks.

## Model-identity cross-check: Seedance and GPT Image 2

- **Seedance** (ByteDance's video-generation model, used via Higgsfield for the camera-flight clips) — already confirmed real in this corpus at [[ai-web-design-workflow/original-seedance-2-0]] (Seedance 2.0, real ByteDance model). This video's usage is consistent with that prior finding; no contradiction.
- **"GPT Image 2"** — OpenAI's current flagship image-generation model, API model id `gpt-image-2`. This is the **same underlying product family** already documented in this corpus's [[ai-web-design-workflow/original-chatgpt-images-2-0]] under its consumer-facing name, "ChatGPT Images 2.0" (rolled out ~2026-04-21). "GPT Image 2" is the API/creator-facing name for the same model line, not a separate, newer model — worth cross-linking rather than treating as a new discovery.

## Cross-links

[[scroll-world-animation-skill/_index]] · [[scroll-world-animation-skill/original-higgsfield-platform]] · [[ai-web-design-workflow/original-seedance-2-0]] · [[ai-web-design-workflow/original-chatgpt-images-2-0]] · [[jasonlee-claude-mobile-app/_index]] (a separate, earlier Fable-5-pricing garble-guard case in this corpus)

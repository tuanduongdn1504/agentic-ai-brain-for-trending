# Original: GPT-5.5 + OpenAI Codex

> The coding agent doing the build in the video. Verified live (post-Jan-2026 cutoff — fetched, not recalled). Note: the official `openai.com/index/introducing-gpt-5-5/` page **403'd**; first-party detail came from OpenAI developer API docs + corroborated web sources. See [[ai-web-design-workflow/source-provenance]].

## What it is

- **GPT-5.5** — OpenAI's frontier model, **released 2026-04-23** (ChatGPT), API **2026-04-24**. **Powers / is available in Codex** (more precise than the video's "ships with Codex" — Codex is a separate product that now runs GPT-5.5).
- **Codex** — OpenAI's agentic coding harness (CLI/IDE), architecturally a near-peer of Claude Code (memory file, plan mode, git-worktree parallelism, sandbox). See the sibling topic [[codex/_index]].

## Verified facts

- **Context window: 400K** (T2-confirmed across tiers Plus/Pro/Business/Enterprise/Edu/Go). ⚠️ A "1M-token" figure appeared in one source and is **NOT verified** — do not cite 1M.
- **Reasoning-effort modes:** `low`, `medium` (default), `high`, `xhigh`, and `none` (latency-critical). ⚠️ **There is no "extra high intelligence" mode** — the video's phrasing ("extra high effort / extra high intelligence") is informal; the real top tier is `xhigh`.
- **Pricing (API):** ~$5 / 1M input, ~$30 / 1M output (≈2× GPT-5.4's $2.50/$15). **GPT-5.5 Pro:** $30 / $180.
- **Token efficiency:** OpenAI claims **~40% fewer output tokens than GPT-5.4** for equivalent tasks — ⚠️ **self-reported, no published benchmark scaffold**; treat as directional and test on your own workload.
- **Images 2.0 in Codex:** GPT-5.5 + Images 2.0 (rolled out ~2026-04-21–22) enables one-shot generation of visual assets inside the coding flow → [[ai-web-design-workflow/original-chatgpt-images-2-0]].

## The Claude-vs-Codex front-end claim — evidence-checked

The video runs **Claude Opus 4.7** ("extra high effort") and **Codex/GPT-5.5** ("extra high intelligence") on the same landing-page prompt and the creator subjectively prefers Codex. **This is a single-prompt opinion, and the broader evidence runs the other way:**

- A **multi-prompt UI comparison** (blog.kilo.ai) rated **Opus 4.7 more polished and more custom** on front-end output.
- **Sam Altman publicly acknowledged GPT-5.5 trailed on front-end at launch.**
- **SWE-bench Verified:** the two are within **~5 points** (Opus slightly ahead) — and both vendors acknowledge possible benchmark contamination, so neither's score is decisive for *comparative* design claims.
- **Agentic benchmarks** (Terminal-Bench, OSWorld, Tau2-bench): **GPT-5.5 leads** — but that's tool-use/agency, **not** design quality.
- **There is no published design-quality benchmark** for either model.

**Bottom line:** the video's "Codex builds better landing pages" is **not** supported. If anything, current evidence favors **Claude for front-end polish** — and the Taste Skill closes the remaining gap on either model. For a Claude-centric operator this means **no model switch is warranted**; the win is the *skill*, not the vendor. See [[ai-web-design-workflow/overview]].

## What's flagged / unverified

- Official GPT-5.5 announcement page unreachable (403) — first-party numbers are from API docs + aggregation.
- "1M context" — unverified (400K is the verified figure).
- The video's exact comparison prompt and settings — not located; not reproducible from the video alone.
- "~40% fewer tokens" — OpenAI self-report, unreplicated.

## Key takeaways

- GPT-5.5 is real and strong on agentic coding, but **the video's design-superiority claim over Claude is unsupported and likely backwards**.
- Use **exact mode names** (`low/medium/high/xhigh/none`), not "extra high intelligence."
- The whole workflow is model-agnostic; pick the model on evidence (front-end → Claude) and let the **Taste Skill** do the taste work.

## Cross-links

[[codex/_index]] (Codex-as-harness; Codex-as-adversarial-reviewer) · [[ai-web-design-workflow/overview]] · [[ai-web-design-workflow/taste-skill-deep-dive]] · [[harness-engineering/_index]] · [[ai-news-2026-w19/_index]] (GPT-5.5 / Opus 4.7 rumor-era snapshot)

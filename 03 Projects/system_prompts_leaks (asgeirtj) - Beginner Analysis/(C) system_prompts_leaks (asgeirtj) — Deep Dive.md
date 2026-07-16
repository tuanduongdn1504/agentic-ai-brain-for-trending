# (C) system_prompts_leaks (asgeirtj) — Deep Dive (LLM Wiki v205)

> **AI-generated (Claude).** Built 2026-07-16 for `github.com/asgeirtj/system_prompts_leaks`. Facts hand-verified via WebFetch (repo + raw README + Anthropic folder) + WebSearch (author identity). Star/fork/commit counts are **page-stated (§37.4 — this environment mocks the GitHub API)** and sources disagree (see below) → **not a Pattern #52 velocity claim**.

---

## 0. One line

The **canonical, continuously-updated, real-name, public-domain (CC0) archive of the actual production system prompts** of every major AI product — **Claude Opus 4.8 / Sonnet 5 / Fable 5 / Claude Code / Claude Design / Cowork / Mobile, ChatGPT GPT-5.6, Gemini 3.x, Grok, Copilot, Cursor, Perplexity, and ~40 more** — maintained in the open by a disclosed individual (Ásgeir Thor Johnson, Iceland) and covered by *The Washington Post*.

**It is a different repo and a different author from the corpus's existing v21 `system-prompts-leaks` subject** (`x1xhlol/system-prompts-and-models-of-ai-tools`). This is the genre's **"legitimate/accountable" pole** to x1xhlol's "pseudonymous/gray" pole.

---

## 1. Identity (hand-verified, WebSearch + repo)

| Field | Value |
|---|---|
| **Repo** | `asgeirtj/system_prompts_leaks` (underscores — NOT the hyphenated v21 repo) |
| **Author** | **Ásgeir Thor Johnson** — `asgeirtj`, **Iceland**, `asgeirtj@gmail.com`, X **@asgeirtj**, ~1.8k GitHub followers. **A fully disclosed individual** (real name + location + contact). |
| **Purpose (README)** | *"The purpose of this repo is to document the System Prompt instructions for all the AI chatbots out there - Claude, ChatGPT, Gemini etc."* |
| **Description** | *"Extracted system prompts from Anthropic - Claude Fable 5, Opus 4.8, Claude Code, Claude Design. OpenAI - ChatGPT GPT-5.6, Codex GPT-5.6, GPT-5.5. Google - Gemini 3.5 Flash, 3.1 Pro, Antigravity. xAI - Grok, Cursor, Copilot, VS Code, Perplexity, and more. Updated regularly."* |
| **License** | **CC0-1.0** (public domain dedication — deliberately non-restrictive) |
| **Stars / forks** | **~51.5K–58.1K★ / ~8.4K–9.6K forks** — page-stated §37.4, **sources conflict** (WebFetch of the repo page: 58.1k★/9.6k; WebSearch summary: 51.5K★/8.4K). → **NOT a #52 claim.** |
| **Commits / activity** | **640 commits**; **updated regularly** (last seen 2026-07-14); "Updated regularly" in the description. |
| **Languages** | **JavaScript 71.5% / Python 28.5%** — repo *tooling* (the GitHub Pages site generator at `asgeirtj.github.io/system_prompts_leaks`), not the archived content (the prompts are Markdown). |
| **Monetization** | **None.** Email + X only. No Patreon / Ko-fi / crypto. |
| **Press** | ***The Washington Post*, May 11 2026** — *"See the hidden rules behind AI. Then use them to rewrite this article."* (README-stated) |
| **Contribution** | **"PRs Welcome"** — open, crowd-sourced archive. |
| **Disclaimer** | **None explicit.** No ethics/legal statement in the README. |
| **Extraction method** | **Undisclosed.** The only validation signal is an image captioned *"Claude confirming an extracted system prompt is authentic"* (self-confirmation — weak evidence; see §6). |

---

## 2. ⚠️ THE COLLISION — this is NOT the corpus's v21 subject

The vault **already has** a `system-prompts-leaks` wiki at **v21**, but it is a **different repo, author, and posture**:

| Axis | **v21 `x1xhlol/system-prompts-and-models-of-ai-tools`** | **v205 `asgeirtj/system_prompts_leaks`** |
|---|---|---|
| Author identity | **Pseudonymous** — x1xhlol / lucknitelol / NotLucknite (3 handles) | **Disclosed real person** — Ásgeir Thor Johnson, Iceland |
| License | **GPL-3.0** (controversial copyleft asserted over non-owned content — Pattern #39) | **CC0-1.0** (public-domain dedication; disclaims all rights — the honest choice for extracted-not-owned content) |
| Monetization | **6-channel** (Patreon + Ko-fi + BTC + LTC + ETH + Solana token) **+ ZeroLeaks** commercial derivative (Pattern #37 + #40 perverse-incentive) | **None** |
| Positioning | **"LeaksLab"** Discord, leak-framing | **"document the system prompts"** + WaPo coverage + "PRs Welcome" |
| Update cadence | one-time leak (Pattern #21 21a) | **continuously updated** (closer to 21b) |
| Content | 31 AI tools | ~15 vendors + ~40 tools, **Claude-heavy** incl. current frontier + every Claude surface |
| Corpus scope call (then) | **OUTSIDE-SCOPE + pilot-AVOID** (brand-association risk > pilot value) | **GOAL-ALIGNED INCLUDE** — see §7 (corpus stance evolved via v65) |

→ **This ship uses a distinct folder** (`system_prompts_leaks (asgeirtj) - Beginner Analysis`) and **does not touch** the existing `system-prompts-leaks - Beginner Analysis` (x1xhlol v21). asgeirtj is a **genuine cross-author 2nd instance** of the multi-tool-prompt-archive genre (Pattern #38 38a) — see §8.

---

## 3. What's actually in it

Top-level folders (hand-verified): **`/Anthropic`, `/OpenAI`, `/Google`, `/xAI`, `/Microsoft`, `/Cursor`, `/Perplexity`, `/Meta`, `/Mistral`, `/DeepSeek`, `/Kimi` (Moonshot), `/Qwen`, `/Notion`, `/Misc`, `/Official`, `/.github`.**

### The `/Anthropic` folder — the reason this is on-goal (Goal #1: master Claude)

This is a **comprehensive, current archive of essentially every Claude surface's production instructions** (hand-verified listing):

- **Frontier models:** `claude-opus-4.6.md`, `claude-opus-4.6-no-tools.md`, `claude-opus-4.7.md`, `claude-opus-4.8.md`, `claude-sonnet-4.6.md`, `claude-sonnet-4.6-no-tools.md`, `claude-sonnet-5.md`, `claude-fable-5.md`
- **Product / feature surfaces:** `claude-code/` (subfolder), `claude-design.md`, `claude-cowork.md`, `claude-cowork-dispatch.md`, `claude-desktop-code.md`, `claude-for-excel.md`, `claude-for-word.md`, `claude-in-chrome.md`, `claude-in-powerpoint.md`, `claude-mobile-ios.md`
- **Injected-context / tool / feature instructions:** `anthropic_reminders.md`, `sonnet-4.6-reminders.md` (the long-conversation reminders — the *same class of injected text you can see in this very session*), `default-styles.md`, `visualize.md`, `research_instructions.md`, `anthropic-interviewer.md`
- **Subfolders:** `Claude Code/`, `Official/` (published/official prompts), `old/` (superseded snapshots), `raw/` (unprocessed captures)

The other vendor folders are structurally similar (per-model + per-surface `.md` files): OpenAI (GPT-5.6/5.5/5.4, Codex, o3/o4-mini, tools, policies), Google (Gemini 3.5 Flash / 3.1 Pro, Antigravity CLI, Jules), xAI (Grok 4.3 Beta / 4.2), Microsoft (GitHub Copilot, VS Code Copilot, Copilot CLI, macOS app), plus Cursor, Perplexity, Meta AI, Mistral, DeepSeek, Kimi, Qwen, Notion, and a `Misc` bucket (Docker Gordon, Zed AI, ElevenLabs Voice Agent, and more).

**This is a reference archive — content to *read*, not software to *run*.** The JS/Py in the repo is the GitHub-Pages site that renders the archive.

---

## 4. Why it matters — the "understanding-agent-internals" value

Reading a product's **actual production system prompt** is one of the highest-signal ways to learn:

1. **How Claude is instructed** (Goal #1 — master Claude). The Opus 4.8 / Sonnet 5 / Claude Code / Claude Design prompts show real, current structure: role framing, tool-definition style, artifact rules, safety/refusal instructions, output-format discipline, the `anthropic_reminders` injection pattern. This is the exact material the vault studied at **v65 claude-code-system-prompts** — but broader (v65 was Claude-Code-only; asgeirtj covers Code + Design + Cowork + Mobile + Excel/Word + Chrome + the frontier models).
2. **Cross-vendor prompt-engineering craft.** Diffing Claude vs GPT vs Gemini vs Grok system prompts is a masterclass in how the best teams structure instructions, tool schemas, and guardrails.
3. **Prompt-injection defense study.** The safety/anti-manipulation sections of these prompts are a real reference for hardening *your own* LLM features against user-supplied-content injection (directly relevant to hireui — Goal #2 — where candidate-supplied text will flow into any LLM feature).
4. **A prompt-engineering changelog.** Version-over-version files (`claude-opus-4.6` → `4.7` → `4.8`) let you watch how Anthropic's instructions evolved.

---

## 5. Provenance & the WaPo signal

- **Mainstream-press legitimacy (corpus-first for this genre):** *The Washington Post* covered it (May 11 2026). No prior corpus prompt-archive subject (x1xhlol v21, claude-code-system-prompts v65) had mainstream-press coverage. Combined with CC0 + real identity + no monetization + "PRs Welcome," asgeirtj is the **accountable/legitimate pole** of the prompt-leak-archive genre.
- **Apparent vendor tolerance:** as with v65, no visible DMCA / takedown despite scale and Claude-heavy coverage — a soft signal that the vendors treat these as observational, not adversarial.

---

## 6. Honest caveats (blunt)

1. **Authenticity is NOT vendor-guaranteed.** These are *extracted* prompts. The only stated validation is a screenshot of "Claude confirming a prompt is authentic" — **a model confirming its own leaked prompt is weak evidence** (models confabulate; a confirmation prompt is easy to lead). Treat any single file as *plausible, unverified* — cross-check load-bearing claims against behavior.
2. **Staleness.** Prompts drift the moment a vendor ships. A file labeled `claude-opus-4.8.md` is a snapshot; the live prompt may already differ. The `old/` folder acknowledges this.
3. **Extraction method undisclosed.** Unknown whether via prompt-injection extraction from the live product, community submission, or something else — so provenance quality varies file-to-file (it's crowd-sourced: "PRs Welcome").
4. **Gray-zone genre.** Extracting closed-source instructions sits in a legal/ethical gray area. CC0 + real identity + no monetization make it *far cleaner* than v21's setup — but it is still not vendor-published. Fine to **read/learn**; do **not** build a product on it or copy vendor prompt *text* verbatim.
5. **Not a tool.** It's a passive content archive. There's nothing to install, no capability added — the value is entirely in reading it.

---

## 7. Scope evolution — why INCLUDE now when v21 was OUTSIDE-SCOPE

The v21 twin was rated **OUTSIDE-SCOPE + pilot-AVOID** (2026-04-19, routine v2). The corpus's stance on prompt-archives **moved** afterward:

- **v65 claude-code-system-prompts** (2026-05) — a Claude-internals reference archive — was **GOAL-ALIGNED INCLUDE (b) STRONG**, establishing the *"reverse-engineering-reference-archive"* T1 sub-archetype, because *understanding agent internals* is directly on-goal for "master Claude."
- **v173 claude-tap** explicitly names *"system-prompts-leaks"* as part of the **understanding-agent-internals thread** (the static-collection counterpart to its live-capture proxy).

So treating asgeirtj as GOAL-ALIGNED INCLUDE is **consistent with the corpus's current stance**; treating it OUTSIDE-SCOPE would be inconsistent with v65. See the Verdict doc for the full 4-criteria call. (The (b) MODERATE reading — "a passive multi-vendor reference, not a Claude-specific actionable resource," the awesome-artificial-intelligence v170 calibration — is recorded as the operator-reviewable alternative.)

---

## 8. Pattern outcome (summary — full call in the Verdict)

- **NO MINT.** No new top-level pattern (max stays #85). No new §C standalone. **Counts UNCHANGED 46/11.**
- **Pattern #38 "Prompt-Leak-Archive Genre" — 38a instance-strengthening N=1 → N=2** (x1xhlol v21 + asgeirtj v205): the corpus's **first genuine cross-author 2nd multi-tool-prompt-archive.** N-tally = audit bookkeeping (recorded, **not** self-incremented — #38 is already CONFIRMED).
- **Pattern #21 "System Prompts Leaks" N=1 → N=2** (multi-tool leak archive; asgeirtj's continuous-update cadence straddles 21a one-time / 21b continuous-extraction).
- **Within-genre polarity observation (DEFERRED watch axis, NOT minted):** disclosed-real-identity + CC0 + no-monetization + press-covered ("legitimate/accountable pole") vs x1xhlol's pseudonymous + GPL + crypto-monetized ("gray pole"). A real within-#38 axis; recorded for the audit.
- **Anti-instances (bound existing candidates):** asgeirtj **bounds #36** (Pseudonymous-Researcher — pseudonymity is NOT required by the genre), **bounds #37** (Crypto-Donation-Funded — monetization is NOT required), and **contrasts #39** (Controversial-License — CC0 public-domain vs GPL copyleft-on-non-owned-content).
- **Does NOT un-stale Pattern #79** (Continuous-Reverse-Engineering Reference Archive, N=1 @v65): asgeirtj is continuously updated but its extraction is **live-model / crowd-sourced with no compiled-source parsing and no per-release latency disclosure** — it fails 2 of #79's 3 criteria (v65 parses the compiled npm package + ships a 176-version CHANGELOG). So NOT a clean #79 2nd instance.
- **Corpus-first sub-facet (recorded, NOT minted):** mainstream-press (Washington Post) coverage of a corpus subject.

---

## 9. Cross-references

- **v21 `x1xhlol/system-prompts-and-models-of-ai-tools`** — the genre twin; the contrast pole (see §2). Patterns #21/#27/#29/#36/#37/#38/#39/#40.
- **v65 `Piebald-AI/claude-code-system-prompts`** — the single-vendor continuous Claude-Code-internals archive; the (b)-STRONG precedent that makes asgeirtj INCLUDE. Pattern #21 21b, #79.
- **v173 `liaohch3/claude-tap`** — the *live-capture* proxy whose docs name system-prompts-leaks as the static-collection counterpart (understanding-agent-internals thread).
- **Pattern #38** (Prompt-Leak-Archive Genre, CONFIRMED v53) · **#21** (System Prompts Leaks, CONFIRMED v63) · **#79** (Continuous-Reverse-Engineering Reference Archive, N=1 stale @v65).
- **Goal #2 (hireui):** the meetily v196 / mosh-ai vendor-seam thread (writing hireui's first LLM system prompt) + the career-ops v200 anti-fabrication + the api-security BOLA / prompt-injection-defense threads.

---

## 10. Bottom line

A **genuinely useful, low-risk, read-only reference** for both goals — the current production system prompts of Claude (and everyone else), maintained cleanly in the open. Unlike its v21 twin (pilot-AVOID), asgeirtj is **safe to read and learn from today.** Its value is entirely in the reading: study how Claude is actually instructed, mine the structure for your own prompts, and use the safety sections as an injection-defense reference — but never trust a single file as authoritative, never copy vendor text verbatim, and never build a product on top of a gray-zone extracted archive.

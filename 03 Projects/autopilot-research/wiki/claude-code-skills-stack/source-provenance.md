# Source Provenance — Verification Ledger

> **Method:** path-5 yt-dlp full transcript (en auto-subs) → deep-dive + adversarial verify Workflow `wf_04da379d-ca9` (21 agents: 9 deep-dive [Haiku] + 9 verify + 3 cross-cutting refuters) → **independent `gh api` ground-check of every cited repo** (2026-06-29) by the main loop. Compiled 2026-06-29.

## Why the extra `gh api` pass

The deep-dive agents ran on Haiku and returned **very high star counts** (Superpowers 241K "global rank 15", G-Stack 117K, ui-ux-pro-max 97K) — exactly the kind of fact subagents confabulate. Per vault verification discipline (independently check identity/metric claims), the main loop queried the **live GitHub API** for all 15 repos. Result: **the agents' numbers were accurate** — the live API confirmed every star count within margin. The grounding turned skepticism into confirmation; it also confirmed the structural corrections (kepano = personal repo; `obsidianmd/obsidian-skills` = 404; Eric's skills public; marketing = Eric Osiu).

## `gh api` ground-truth table (2026-06-29)

| Repo | Stars | License | Lang | Created | State |
|---|---|---|---|---|---|
| obra/superpowers | 240,869 | MIT | Shell | 2025-10-09 | active |
| garrytan/gstack | 117,834 | MIT | TypeScript | 2026-03-11 | active |
| gsd-build/get-shit-done | 64,570 | MIT | JavaScript | 2025-12-14 | **archived** |
| open-gsd/gsd-core | 5,346 | MIT | JavaScript | 2026-05-22 | active |
| nextlevelbuilder/ui-ux-pro-max-skill | 97,573 | MIT | Python | 2025-11-30 | active |
| voltagent/awesome-design-md | 94,132 | MIT | (md) | 2026-03-31 | active |
| kepano/obsidian-skills | 38,756 | MIT | (md) | 2026-01-02 | active |
| **obsidianmd/obsidian-skills** | — | — | — | — | **404 NOT FOUND** |
| microsoft/playwright-mcp | 34,479 | Apache-2.0 | TS | 2025-03-21 | active |
| microsoft/playwright-cli | 11,670 | Apache-2.0 | JS | 2020-06-19 | active |
| anthropics/skills | 156,362 | (mixed) | Python | 2025-09-22 | active |
| anthropics/claude-plugins-official | 31,274 | Apache-2.0 | Python | 2025-11-20 | active |
| EricTechPro/startup-claude-skills | 51 | MIT | (md) | 2026-03-10 | active |
| ericosiu/ai-marketing-skills | 2,738 | MIT | Python | 2026-03-28 | active |
| google-labs-code/design.md | 22,960 | Apache-2.0 | TS | 2026-04-10 | active |

## ✅ CONFIRMED

- **All 10 originals are real** with accurate stars/licenses (table above).
- **Skill Creator is genuinely first-party Anthropic** (`anthropics/skills/skill-creator`); "2.0" = 2026-03-03 evals update.
- **Superpowers** = Jesse Vincent (`obra`); v6.0 ~50% token reduction; `dispatching-parallel-agents` skill real.
- **GSD** context-isolation differentiator (fresh 200K per executor, 5-phase loop) real; **G-Stack** persona commands + `/qa` (real Playwright Chromium) + `/cso` (OWASP+STRIDE) real.
- **design.md** was created by Google inside **Stitch** (May 2025) and open-sourced by Google Labs ~April 2026 — NOT a pre-existing community convention.
- **Steph Ango (kepano) is CEO of Obsidian** and authored the obsidian skill.
- **Eric's /fix-ticket + Playwright skill are PUBLIC** (`EricTechPro/startup-claude-skills`, MIT).
- **Telegram plugin is official Anthropic**; Sentry/Jira/Vercel integrations are official MCPs.
- **BookZero.ai is real** (~1.2K users); creator is ex-Amazon (L6); product name is **BookZero** (auto-captions garbled to "bookworm/bookero").
- **UI UX Pro Max install is safe** (no postinstall; 4 clean deps; local CSV data; GitHub-release fetch w/ fallback).

## 🔧 CORRECTED

- **Superpowers pipeline order** — video: "brainstorm → plan → write-tests-first → execute". Actual: TDD runs **during** execution (step 5), review **between** tasks. (PARTIAL)
- **Superpowers language** — NOT Markdown; **Shell 51.6% / JS 41.3%** + TS. (REFUTED a draft claim)
- **UI UX Pro Max "trained on hundreds of datasets"** — REFUTED; it's a **deterministic reasoning engine over bundled CSV lookup tables** (67 styles / 161 palettes / 57 fonts / 99 guidelines / 25 charts) + 161 reasoning rules. No ML training.
- **Obsidian skill is "official Obsidian" + "a RAG"** — REFUTED; it's Steph Ango's **personal** repo (`obsidianmd/obsidian-skills` is a 404) and is a set of **format-handling skills**, not a RAG. The RAG-like behavior is the **Karpathy LLM-Wiki pattern** it *composes with*.
- **Playwright skill is gated** — REFUTED; **public** MIT.
- **"43 marketing skills" are Eric Tech's** — CORRECTED; they're **Eric Osiu's** (`ericosiu/ai-marketing-skills`), cited not authored. "43" is a loose sub-skill count (~15 categories).
- **Skill Creator "four agents incl. Executor"** — PARTIAL; three documented agents (grader/comparator/analyzer); no "Executor".
- **GSD original is the one to install** — CORRECTED; the original is **archived** → use **`open-gsd/gsd-core`**.
- **Playwright MCP schema overhead "~3,600 tokens"** — underestimate (~10×); real benchmarks show tens-of-thousands at session start; CLI ~68 tokens.

## ⚠️ FLAGGED (unverifiable / soft)

- **"/fix-ticket replaces ~90% of junior SWE jobs"** — hyperbole; real signal = junior-hiring freeze (~62% of surveyed managers) + postings −30% since 2022.
- **"43 skills took BookZero 0→1000 users"** — UNVERIFIABLE single-channel attribution.
- **"Garry Tan (YC) personally authored G-Stack"** — owner login `garrytan`; plausible but not hard-verified; treat repo facts as solid, the celebrity-author claim as soft.
- **GSD "meme-coin / trust incident → governance move"** — single-source rationale for the archive→fork; the *archive* is verified, the *story* is not.
- **G-Stack "devil's advocate" persona + exact 23-vs-43 command count** — paraphrase; counts vary by release.
- **Eric "ex-Microsoft"** — Amazon L6 confirmed; Microsoft inferred, not directly confirmed.
- **Exact Skill Creator helper-script filenames** — approximate (repo references differ from draft).
- Eric's specific "16-phase QA" demo — UNVERIFIABLE beyond the transcript (no public artifact).

## Confidence

High on existence/ownership/stars/licenses (live `gh api` + multi-source). Medium on framework internal command counts + token benchmarks (third-party). Low/flagged on creator success anecdotes + the GSD-incident narrative.

## Related

[[claude-code-skills-stack/_index]] · [[claude-code-skills-stack/video-to-original-crosswalk]]

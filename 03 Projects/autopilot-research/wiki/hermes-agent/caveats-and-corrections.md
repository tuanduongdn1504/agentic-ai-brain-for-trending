# Hermes Agent — Caveats & Corrections

## Source
Refute-first workflow `wf_06a79485-687` (evidence + corrections) + 2 completeness critics + main-loop primary checks. Companion to [[claims-scorecard]].

## 🔄 Corrections added by the 2026-09-03 revisit

New corrections from the second drain. Full evidence + the 78-claim scorecard: [[revisit-2026-09-03]].

7. **"Windows support requires WSL 2" → FALSE.** Windows is **native** — the README ships `iex (irm https://hermes-agent.nousresearch.com/install.ps1)`, installing to `%LOCALAPPDATA%\hermes`. WSL2 is an alternative.
8. **"16 platforms including iMessage and WeChat" → FALSE.** The README enumerates **8** entry points (Telegram, Discord, Slack, WhatsApp, Signal, Email, Home Assistant, CLI). **WeChat is a third-party community bridge** (`AaronWong1999/hermesclaw`); iMessage is not listed.
9. **"Ollama is the easiest way to run local models" → FALSE, and it matters most.** The documented integration is **"Ollama Cloud"** — a cloud service requiring an API key, default endpoint `https://ollama.com/v1`. Ollama is not named in Hermes' own docs; official local-model guidance is "your own endpoint". **The bundle's most-recommended "private" path is a third-party cloud by default.** Directly compounds the data-residency blocker below.
10. **"Requires a 64,000-token context window to provide agent tools" → FALSE (unanimous, 3/3 lenses).** No minimum exists; tools activate when present and defer their schemas. ~60K is a *tool-listing budget ceiling*, not a requirement.
11. **"Claude Code is available as a provider / is positioned as a companion tool" → FALSE.** Claude Code appears **nowhere in the README**. ⚠️ But the repo's **GitHub topics do include `claude-code`, `claude`, `codex`, `anthropic`, `openai`** — a plausible seed for this recurring confusion ([[the-vendor-seeded-false-claim]]).
12. **"6 execution backends" → 7.** `+ Vercel Sandbox`, verified verbatim in the README.
13. **"20+ platforms" and "60+ built-in tools" → DOWNGRADED to UNVERIFIABLE.** Neither string is in the README; the docs site is JS-rendered and unreadable by `curl`. 8 entry points is the confirmed floor. *(A grounder agent fabricated a 20-name enumeration during this drain — see the process failures in [[revisit-2026-09-03]].)*
14. **Nous Portal tiers → STALE.** Free/Plus/Super/Ultra has **no 2026-09-03 corroboration**; the Portal is behind a Vercel Security Checkpoint. Do not cite ([[pricing-license-and-skill-hub]]).
15. **Desktop "macOS 12+/Windows 10-11" version floors → UNVERIFIED.** `apps/desktop/README.md` names the three platforms with no floors. These figures were previously in this wiki and a critic agent "confirmed" them *by reading this wiki* — circular ([[hermes-desktop]]).
16. **"~90 skills pre-installed" → do not pin a number, and do not conflate skills with tools.** Skills are *generated* from experience and grow per user; tools ship fixed. No primary source states a built-in skill count.

**Still standing from 2026-07-18, now independently corroborated:** the "runs under Claude Code" correction (C17) drew **2 contradictions and 0 repeats** across six fresh sources — the field now agrees with the corpus.

**Still standing and now traced to its source:** "the only agent with a built-in learning loop" (H4) is **the vendor's own README text, live on 2026-09-03**, which is why it recurs. [[the-vendor-seeded-false-claim]].

## Corrections (2026-07-18 — Rule 12, fail loud)
1. **"22K stars" → 216,731 stars.** Widely-repeated SEO blogs undercount by ~10× (H2). The real figure makes Hermes the **largest single repo by stars in the corpus** (> AutoGPT 184,043).
2. **"Launched February 2026" → first release March 12, 2026 (v0.2.0).** Repo created 2025-07-22; no Feb release. (H5.)
3. **"Only agent with a built-in learning loop" → FALSE.** Refuted by Hermes' own OpenClaw-import tool (H4).
4. **"Runs under Claude Code" → FALSE.** It's MCP interop, both directions (C17 → [[claude-code-interop]]).
5. **"Built before OpenClaw" (t8) → unsupported/false.** Hermes repo is 2025-07-22 and ships an OpenClaw→Hermes migrator; the "we came first" framing is not evidenced. *(No independently-verified OpenClaw creation date is asserted here.)*
6. **"No-code / easier than OpenClaw" → MISLEADING.** Developer CLI/TUI needing Python 3.11/Node/ripgrep/ffmpeg + config (H6).

## ⚠️ Material contradiction — skill self-improvement maturity (Rule 7: surfaced, not averaged)
- **Marketing / promotional videos:** "autonomous skill creation + self-improving skills" is *the* core differentiator.
- **Credible technical reviewer (Sean's AI Stories, t4):** on camera, *"I don't think it self-triggered self-learning skills yet. It only triggered learning the memory"* — and Hermes **lacks LLM-ops/eval systems** to measure whether a skill actually improved. He wanted proactive skill-saving; it wasn't there.
- **Verdict:** memory learning is real; **autonomous skill-quality evolution is unproven**. Read "self-improving skills" as "saved-and-reused skills, quality-evolution unverified."

## Unverified-but-important (do NOT assert; verify before relying)
- **OpenRouter "224B vs 186B daily tokens, overtook OpenClaw June 2026"** — UNVERIFIABLE + likely a category error (OpenRouter ranks models, not agents). (H3.)
- **"Every-10-turn background fact-checking prevents hallucination"** (NetworkChuck) — not in docs or other sources.
- **Anthropic "June 15 subscription" pricing claim** (t8) — that Claude Code *subscriptions* can no longer run third-party agents free after June 15; monthly agent-SDK credit; non-interactive mode affected. **Unverified secondary claim wrapped in ad-hominem ("greedy little Dario")** — check Anthropic's own pricing docs. (Cf. [[claude-api-cost-optimization|claude-api-cost-optimization]].)
- **OpenClaw "50,000+ community skills"** and OpenClaw security-history specifics (t1/t8) — source-claims, not primary-verified.
- **Skill/tool counts vary by version:** "90 skills default" (t8) vs "68 skills / 28 tools" (t1) vs "60+ tools" (docs) — do not pin one number.
- **Honcho version details** ("0.11.0 major overhaul", "Gemini Flash summarization layer" — t5) — external Plastic Labs product; not confirmed in Hermes docs.

## Documentation / architecture gaps (critic-identified — real risks for deployment)
- **Subagent isolation threat-model** — how isolated are parallel subagents? sandbox attack surface? exfiltration/escalation paths? Undocumented.
- **Honcho / cloud-backend data residency** — where are user-model data and tokens processed for Portal + Honcho? No residency/privacy guarantees found. *(Direct blocker for any candidate-facing use — see the hireui candidate-LLM legibility ADR.)*
- **Performance limits** — max subagents, per-op token limits, latency SLAs — undocumented.
- **`hermes claw migrate` caveat (t8):** imported OpenClaw files "don't carry over cleanly" (instructions were OpenClaw-specific) and imported logins still point to OpenClaw's channels — the AI LABS team chose **not** to import. Migration is lossy.
- A **live cron bug** was observed (t4): scheduled job fired 2/10 times, didn't update results unless asked.

## Key Takeaways
- The corrections cluster into one shape: **accurate capabilities, inflated framing.** The confirmed core is trustworthy; the superlatives are not.
- **Biggest substantive caveat:** the flagship "self-improving skills" is, per the most credible reviewer, **memory-learning today** — not a proven autonomous skill-quality loop.
- **Biggest deployment blocker for the operator:** **data-residency + subagent-isolation are undocumented** — same hard blocker flagged for [[vercel-eve|vercel-eve]]. Do not put candidate PII near it without those answers.

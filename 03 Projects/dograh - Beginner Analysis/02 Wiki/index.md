# dograh — Wiki (v122)

> `dograh-hq/dograh` · **"Open source voice AI platform. Self-hosted alternative to Vapi and Retell."** · A Pipecat-based, self-hostable platform for building production **voice agents** — telephony (Twilio/Vonage/Vobiz/Cloudonix), STT/TTS/speech-to-speech, a drag-and-drop workflow builder, MCP-native tool-calling, BYOK across providers. "From zero to a working bot in under 2 minutes."

**(C) Claude-generated wiki page.** Fetched 2026-05-30 (GitHub API + README + org page + AGENTS.md/CLAUDE.md + 2 SKILL.md). Routine v2.4, wiki #122. **⚠️ Built under the 3rd operator-elected Phase 0.9 OVERRIDE in corpus history — STRICT verdict was 0/4 SKIP (out of corpus scope: a voice/telephony product, not a software-dev-agent subject). See the OVERRIDE verdict doc in `01 Analysis/`.**

> **Version note:** this is **v122**, not v121 — `v121 CodexKit` shipped concurrently (commit `62d98a8`) during this build.

---

## Identity

| Field | Value |
|---|---|
| Repo | [`dograh-hq/dograh`](https://github.com/dograh-hq/dograh) |
| What | **Self-hosted voice-AI / telephony agent platform** (Vapi/Retell alternative) |
| Tier / archetype | **Corpus-outlier** — does NOT fit the agent-*for-coding* T1–T5 taxonomy. Closest = **T5 Application / T2 Service**. **CORPUS-FIRST voice-AI / telephony-agent platform** (first agent platform in the corpus for a non-software-dev domain). |
| Stars / forks | **3,729★ / 773 forks** (fork_ratio **0.21** — strong active-deployment intent) |
| Watchers / open issues | 36 subscribers / 22 open |
| Created / pushed | 2025-09-09 / 2026-05-29 (**~263 days** old at fetch); latest release **v1.32.0** (2026-05-28) |
| Velocity | **~14.2 stars/day → sustained-low, NOT a Pattern #52 instance** (below all sub-class floors; profile like v100 Easydict / v116 Sana — steady accrual, not a viral pulse). High *release* cadence (v1.32 in ~8 mo). |
| License | **BSD-2-Clause** (GitHub API agrees; clean single license) |
| Language | **Python 57.8%** / TypeScript 38.5% / Shell 2.2% / PowerShell / JS (~30 MB) |
| Distribution | **Docker-Compose one-liner** (`curl … docker-compose.yaml && … docker compose up`); managed cloud at **app.dograh.com**; `dograh-sdk` on PyPI |
| Default branch / homepage | `main` / app.dograh.com |
| Author | **dograh-hq** (`owner.type: Organization`) = **Zansat Technologies Private Limited**; "founded by exited founders, ex-CTOs, and YC alumni" (2024). Likely India-linked (Pvt Ltd + India/UAE go-to-market), HQ unstated, founders not publicly named. |
| Topics | voice-agents, voice-ai-platform, conversational-ai, telephony, speech-to-speech, speech-to-text, text-to-speech, ai-calling, asterisk-ari, local-llm, no-code, on-prem, pipecat, vapi-alternative, self-hosted |

## What it is

dograh is a developer-first, **fully self-hostable voice-AI platform** — an open-source alternative to the hosted Vapi / Retell voice-agent services. You design a voice agent in a drag-and-drop **workflow builder**, wire it to telephony (Twilio, Vonage, Vobiz, Cloudonix) for inbound/outbound calls (with human-transfer), and run the whole stack on your own infrastructure with **no vendor lock-in**. It is built on **Pipecat** (the open multimodal-conversational-AI framework; the org maintains its own pipecat fork) and is **BYOK** across the swappable layers — speech-to-speech *or* separate LLM / STT / TTS providers — plus **MCP-native** tool-calling so agents can invoke external tools.

Architecture (per the repo + its `AGENTS.md`): a **FastAPI** Python backend + a **Next.js/TypeScript** frontend + Postgres / Redis / MinIO, shipped Docker-first. Supporting org repos: forks of `vllm` (LLM inference), `langfuse` (LLM observability), `speaches` (STT), `asyncari` (Asterisk), plus a small `skills` repo.

It is **not** a coding agent, a Claude-Code tool, an agentskills.io product, or anything in the autonomous-*software-development* space the corpus tracks. It builds **agents that answer and make phone calls.** It lands in this corpus only by an explicit operator override (below).

## The one genuinely corpus-relevant thread (and why it doesn't flip the verdict)

dograh is a clean real-world specimen of a **commercial product team operationalizing Claude Code agent-skills as *internal* engineering discipline** — not as a product, but as how they build the product:

- **`CLAUDE.md` is an 11-byte `@AGENTS.md` import** — a single-source-of-truth: one canonical instruction file, pulled into Claude Code via the `@`-include.
- **A hierarchical `AGENTS.md` tree** (root → `api/` → `ui/` → deeper) with explicit parent/child ownership boundaries.
- **`.agents/skills/review-agents-md/SKILL.md`** — a **drift-guard skill** that audits that AGENTS.md tree against the live code: hierarchy tests (parent-fit / child-fit / no-duplication / downward-pointing / no-gaps / **no-drift**), finding-classes (`stale` / `missing-child-agents` / `wrong-level` / `extra-detail`), "treat the repo as source of truth," spawns a subagent to refresh references first.
- **`.agents/skills/review-pr/SKILL.md`** — a **domain-specific PR security/correctness audit** over 8 Dograh-specific failure modes (org-scoping on cross-tenant access, unauth routes/websockets, unsigned-webhook trust, SQL-outside-DB-client layering, stale multi-worker cache, unsafe prod migrations, UI-bypassing-generated-SDK, secrets-in-logs), reported as `file:line → problem → correct pattern`, bucketed Blocker / Should-fix / Nit.

This *is* in the corpus's methodology wheelhouse, and it's a genuinely good example of agent-skill-driven engineering governance. **But it's the repo's engineering exhaust, not its product** — and a large, growing fraction of all serious repos now ship a `CLAUDE.md` + `AGENTS.md`. Counting that as corpus-relevance would erode the scope discipline. So it's recorded as an *observation*, not as grounds for inclusion.

## Why it's in the corpus (and the honest caveat)

It's here because the operator chose to override the include/skip gate. The disciplined verdict was **SKIP**:

- **(a)** Zansat Technologies Pvt Ltd is a VC-adjacent, exit-founder/YC-alumni commercial team — not an indie cultural peer, not a foundational vendor the vault depends on. **FAIL.**
- **(b)** Zero relevance to the documented #1 goal ("master Claude and autonomous agents *for software development*"); dograh builds *phone-call agents*; no vault/Scrum/dev-workflow utility. **FAIL.**
- **(c)** Genuinely well-built — *as a voice-AI platform*, a different domain. The only transferable thread is the incidental internal Claude-Code tooling above. **WEAK.**
- **(d)** Connectivity is incidental (product-MCP, internal SKILL.md tooling, CLAUDE.md/AGENTS.md hierarchy, BYOK). No agentskills.io *product* chain, no Karpathy lineage, no Claude-Code-tool adjacency. **WEAK.**

→ **0/4 clear PASS → STRICT SKIP → operator OVERRIDE INCLUDE** (**3rd** in corpus history after v84 image-blaster + v116 Sana). Treat this page as corpus-knowledge-of-an-outlier, not a vault pilot or a goal-aligned subject.

**⚠️ This override TRIPS the 2-in-20 frequency trigger** (v116 + v122 within the last 20 ships) — the first time that trigger fires in corpus history. The next audit (~v124–v125) is **mandated** to review Phase 0.9 STRICT for a systematic miss-pattern (routine v2.3 §7). See the verdict doc.

## Honest non-claims

- **NOT** an agent-for-software-development tool; **NOT** a Claude-Code skill/plugin product; **NOT** an agentskills.io product-implementer (its SKILL.md files are *internal* dev tooling).
- **NOT** a Pattern #52 velocity instance (~14/d sustained-low).
- **NO** new top-level Pattern; **NO** Pattern Library state change. Out of scope → contributes nothing to the agent/skill pattern corpus.
- Only real Pattern observations are domain-agnostic / incidental: **#82 quantitative-marketing** (MODERATE); **Library-vocab #12** LLM-routing-artifacts and **#81 Manifest-Drift PROPER pole** (both incidental N+1, no state change); thin **#18** MCP-native + **#84** BYOK + **#45** BSD-2.

---

*See `01 Analysis/(C) Phase-0-and-0.9-OVERRIDE-verdict.md` for the full gate decision + the 2-in-20 trip, and `01 Analysis/(C) Pattern-Library-Phase-4b-3rd-override-observation.md` for the (deliberately thin) Pattern Library contribution.*

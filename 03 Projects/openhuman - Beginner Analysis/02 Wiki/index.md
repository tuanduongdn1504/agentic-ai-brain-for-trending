# OpenHuman — Wiki (v118)

> `tinyhumansai/openhuman` · **"Your Personal AI super intelligence. Private, Simple and extremely powerful."** · An open-source agentic desktop assistant (Rust + Tauri + TS) that builds a persistent **Memory Tree + Obsidian-compatible Markdown vault** from 118+ connected services — **explicitly inspired by Andrej Karpathy's obsidian-wiki workflow** — and can expose that memory to Claude Code / Cursor / Codex / OpenCode via an **agentmemory backend**.

**(C) Claude-generated wiki page.** Fetched 2026-05-29 (GitHub API + README + author profile). Routine v2.4, wiki #118. Phase 0.9 **STRONG INCLUDE 3/4** — (d) STRONGEST, (b)(c) STRONG, (a) FAIL. The single most *methodology-recursive* subject since v94: it productizes the exact Karpathy LLM-wiki pattern this vault is built on.

---

## Identity

| Field | Value |
|---|---|
| Repo | [`tinyhumansai/openhuman`](https://github.com/tinyhumansai/openhuman) |
| What | **Open-source agentic desktop assistant with a persistent Memory Tree + Markdown vault** |
| Tier / archetype | **T1/T2 Agent harness** (desktop agent assistant; sibling to v107 claude-code-harness + v99 cmux; Tauri-desktop like v73 cc-switch + v117 CodexPlusPlus) |
| Stars / forks | **29,402★ / 2,775 forks** (fork_ratio **0.094**) |
| Subscribers / open issues | 139 / 108 |
| Created / pushed | 2026-02-18 / 2026-05-29 (**~100 days** old at fetch) |
| Velocity | **~294 stars/day → Pattern #52 HIGH-NOT-EXTREME upper edge** (150–300/d, just below the >300/d EXTREME floor), sustained **>90 days** = notably strong/long |
| License | **GPL-3.0** (GitHub API + README agree) |
| Language | **Rust ~61% + TypeScript ~36%** |
| Stack | **Rust (cargo) + Tauri desktop + TypeScript**; build needs Node 24+, pnpm 10.10, Rust 1.93, CMake/Ninja/ripgrep |
| Platforms | macOS (Homebrew), Linux (apt / AUR), Windows (MSI); native pkgs + .dmg/.deb/.AppImage/.msi |
| Default branch / homepage | `main` / tinyhumans.ai/openhuman |
| Author | **Steven Enamakel** (@senamakel) — **Dubai-located**, bio "Builder & Hustler", company @tinyhumansai, linktr.ee/enamakel; account 2017, 50 repos, 213 followers. Repo owned by org **tinyhumansai**. |

## What it is

OpenHuman is a desktop "personal AI" that continuously ingests your work life (Gmail, Notion, GitHub, Slack, Calendar, Drive, Linear, Jira, Stripe — 118+ via one-click OAuth) into a **persistent memory** the agent can reason over. Its two defining ideas are directly corpus-relevant:

1. **Memory Tree + Obsidian-compatible Markdown vault — an automated Karpathy LLM-wiki.** Data from connected services is canonicalized into **≤3k-token Markdown chunks**, scored, and organized into **hierarchical summary trees**, stored in local SQLite and *also* exported as `.md` files in an Obsidian-style vault you can browse/edit. The README cites **Andrej Karpathy's obsidian-wiki workflow** as the inspiration. This is, in effect, a productized + auto-ingesting version of the exact pattern Storm Bear's vault runs by hand.
2. **agentmemory backend → shared memory for other coding agents.** Optionally wires the same persistent memory into [`rohitg00/agentmemory`](https://github.com/rohitg00/agentmemory) so **Claude Code, Cursor, Codex, and OpenCode** can read it. *(agentmemory is also the v66 corpus subject — exact-identity match flagged for audit verification.)*

## Architecture & features

- **Local-first + hybrid-managed.** Memory Tree, Markdown vault, workspace config, runtime state live locally (SQLite + `.md`). **But the default experience is *managed*:** account sign-in, model routing, web-search proxying, and OAuth (via **Composio**) run through OpenHuman-hosted services. Fully-local/BYO mode (own models, search, Composio key) is possible but some real-time triggers still need the managed backend.
- **Model routing** — picks an LLM per workload (reasoning / fast / vision); default proxies through the OpenHuman backend; one subscription covers all models; optional **Ollama** local.
- **TokenJuice compression** — all tool outputs / scrapes / emails / search payloads are HTML→Markdown converted, deduped, summarized (CJK/emoji-safe) before hitting the LLM; claimed **"up to 80%"** cost/latency reduction (cf. v97 distill).
- **Auto-fetch** every 20 min pulls fresh data into the memory tree.
- **Batteries:** web search/fetch, full coder toolset (fs/git/lint/test/grep), native voice (STT + ElevenLabs TTS + mascot lip-sync), desktop mascot, a **meeting agent that joins Google Meets as a participant**, background thinking.
- **`.claude/` + `AGENTS.md` + `CLAUDE.md` + `.agents/` + MCP Registry** integration (Library-vocab #12 routing artifacts; agentskills.io/Claude-Code adjacency).

## ⚠️ Honest "Private" caveat

The headline is "**Private**, Simple and extremely powerful," and data does stay on-device as a local Markdown vault. But the **default path routes your model calls, web searches, and 118 OAuth handshakes through OpenHuman-hosted servers (Composio proxy) on a single paid subscription.** To be genuinely private you must opt into BYO-models + BYO-Composio + local search — at which point you lose some real-time/hosted features. This is documented, not hidden, but the "Private" framing is doing a lot of work for what is, by default, a managed commercial service. Early-beta status + a 118-service OAuth trust surface compound the consideration.

## Why it's in the corpus

**STRONG INCLUDE 3/4** (load-bearing on (b)(c)(d); (d) STRONGEST):
- **(a) FAIL** — Steven Enamakel, Dubai-located, Indian-heritage-diaspora solo founder of an org. Not a VN/Asian-LOCATED cultural-peer; mirrors the v98/v112/v113 diaspora-founder FAILs. Dubai/Gulf is a corpus-novel locale but N=1 — **no new (a) sub-axis coined** (per the (a)-8 South-American N=1-retirement precedent).
- **(b) STRONG** — sits exactly at the goal-#1 (Claude Code) ∩ vault-methodology (Karpathy LLM-wiki) intersection; the agentmemory backend can give Claude Code persistent memory, and the Memory-Tree technique is directly study-relevant to the vault. Tempered from STRONGEST by the managed-by-default backend + early-beta + trust surface.
- **(c) STRONG** — instructive reference design for productizing the LLM-wiki/persistent-memory pattern (Memory Tree + summary trees + TokenJuice + Composio connectors + model routing).
- **(d) STRONGEST** — exceptional connectivity: Karpathy LLM-wiki lineage (corpus Pattern 1) + agentmemory v66 + Claude/Cursor/Codex/OpenCode multi-harness + .claude/AGENTS.md/MCP + TokenJuice↔v97 distill + Tauri-desktop↔v73/v117.

## Pattern Library contribution (summary)

- **PRIMARY: Pattern #57 corpus-recursive sub-variant "Productized/Automated Karpathy-LLM-Wiki-Pattern at the Methodology-Influence Layer" → N=2** (v94 Understand-Anything + **v118 OpenHuman**). The vault's own foundational pattern, observed being productized into a commercial tool a second time. Promotion-eligibility at N=3; audit decision.
- SECONDARY: **Pattern #85 Platform-Primitive Foundation / agentmemory v66** (memory-as-shared-backend for 4 coding agents — verify v66↔rohitg00/agentmemory identity); **Pattern #84 cross-vendor** (Claude/Cursor/Codex/OpenCode); **Pattern #18 B1 MCP** + 118-Composio aggregation; **Pattern #52 HIGH-NOT-EXTREME** upper-edge (~294/d × 100d); **Pattern #82 quantitative-marketing** ("super intelligence" / "first agent harness" / "up to 80%"); **Pattern #66 supply-chain** (managed-default proxy vs "Private" framing); **LV-C7 Tauri-desktop-harness cluster → N=3** (v73 + v117 + v118); TokenJuice ↔ v97 distill / Token-Economy-Quantification; Library-vocab #12 routing artifacts.
- **Honest non-claims:** (a) FAILs honestly; the "Private" claim is caveated; NOT a Pattern #52 promotion (HIGH-NOT-EXTREME N+1); the #57 corpus-recursive promotion is an audit decision; OpenHuman's product purpose (personal-assistant memory auto-ingesting 118 services) **differs** from the vault's (curated research corpus) even though the *technique* (Karpathy Markdown-wiki + summary trees) is shared — it does NOT "replace the vault"; **zero new standalone Library-vocab minted** (§28); no Pattern Library state change at ship.

---

*See `01 Analysis/(C) Phase-0-and-0.9-INCLUDE-verdict.md` and `01 Analysis/(C) Pattern-Library-Phase-4b-Karpathy-LLM-Wiki-productized-corpus-recursive-N2.md`.*

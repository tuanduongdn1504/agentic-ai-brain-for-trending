# (C) Phase-0.9 verdict — devspace (v171) — GOAL-ALIGNED INCLUDE 3/4

**Subject:** `Waishnav/devspace` — *"Turn ChatGPT into Codex."* A self-hosted MCP server that gives a hosted chat host (ChatGPT / Claude / any MCP-capable host) read/write/edit/search/execute access to local code, via local endpoint or HTTPS tunnel, behind owner-password approval — no file upload.

**Verdict:** **GOAL-ALIGNED INCLUDE 3/4** — (a) FAIL · (b) STRONG · (c) STRONG · (d) STRONG.
**Tier:** T2 Service (self-hosted MCP server / developer tool).
**2-tier INCLUDE (routine v2.5 §31):** the tier is keyed on **(b)**. (b) = STRONG (MODERATE+) → **GOAL-ALIGNED**. (a)'s FAIL is *immaterial* to the tier.

---

## Criterion-by-criterion

### (a) Author cultural-peer / Anthropic axis — **FAIL** (genuine, no rescue)

- Author = **Waishnav** (@wshxnv): an individual indie developer, creator of GitCMS, openly building "a single-person company doing multiple millions in revenue."
- Not Anthropic, not an org. The only major-vendor (a) carve-out **(a)-7 "Foundational-Vendor-Direct-Source" is Anthropic-only**, and devspace's author is neither.
- He discloses **more** identity than v168 ponytail's bare pseudonymous handle (real product history, public revenue thesis, X presence). But the question (a) asks is **cultural-peer-of-Storm-Bear on a *registered* axis**, and:
  - "fellow indie / solo developer building in public" is **not a registered (a) axis** (the registered axes are VN/Asian solo-dev, Tiếng Việt, vi-VN i18n, VN/Asian community-org, VN/Asian founder-anchor, recognized-cultural-cluster, + (a)-7 Anthropic-only).
  - "Waishnav"/"Vaishnav" → Indian-heritage **inference**; per v151 / v160→v169 discipline a name/heritage inference is **NOT** an (a)-rescue.
- **→ (a) FAILs cleanly. No rescue, no axis minted.** Consistent with v168 / v169 / v170 (all three FAILed (a) and shipped GOAL-ALIGNED via (b)).
- ⚠️ **Recorded operator-reviewable calibration:** "solo indie SaaS founder building in public" is the closest (a) cultural-peer angle this subject offers, and Storm Bear *is* a software developer. Whether "indie builder" should ever become a registered (a) axis is logged as an open question (it touches the standing recommendation (ii) on (a)-rescue tightening). NOT minted at ship time. Does not change the verdict.

### (b) Goal-relevance — **STRONG** (the criterion that keys the tier)

Goal #1: *"Master Claude and autonomous agents for software development."*

devspace is **MCP infrastructure for coding agents** — exactly the goal domain:
- It is an **MCP server** (the core Claude/agent interop protocol).
- It **turns a chat model into an autonomous coding agent** over local code (read/write/execute/git) — this is *literally* "autonomous agents for software development."
- It **supports Claude** as a host, honors **`CLAUDE.md`**, and **discovers agent skills** (`SKILL.md` folders).
- It ships **git-worktree-isolated parallel coding sessions** — the same isolation mechanism Claude Code uses for parallel sub-agents, and the substrate of the operator's active multi-agent-orchestration pilot thread.
- It is **directly pilotable into the vault** (MCP access to this vault's own code).

**Held at STRONG, not STRONGEST**, because:
- The thesis is **ChatGPT-primary** ("turn *ChatGPT* into Codex"; "ChatGPT becomes the operating system for everything") — Claude is a secondary, "and Claude"-tier host.
- It is **third-party** (not the vault's own work, not an Anthropic substrate).

STRONG-near-STRONGEST is defensible (MCP + Claude-host + CLAUDE.md + agent-skills + worktree-parallel-sessions is a dense on-goal cluster). Either way → **GOAL-ALIGNED** (§31 keys on (b) MODERATE+).

### (c) Engineered surface — **STRONG**

- Published npm package `@waishnav/devspace`; CLI (`init` / `serve`).
- MCP server in **TypeScript (87.3%)**, Vite build, Node ≥20.12.
- Tunneling layer (local `127.0.0.1:7676/mcp` or public HTTPS).
- **Owner-password auth** (`~/.devspace/auth.json`), **folder-root sandboxing**, **git-worktree isolation**, tool-card UI.
- Shipped as **v1.0.0** — a real, runnable product, not a prototype or a links list.

### (d) Pattern contribution — **STRONG**

- **1 corpus-first §C standalone** (the bridge capability — see the PRIMARY doc) on a genuinely novel axis (bridge-direction + remote→local security).
- A **clean Pattern #18 B1-MCP instance** (one-server-many-MCP-clients).
- Scoped secondary observations (#84 host-agnosticism / #22 consumer-side / #19 19a portfolio / #66 security-conscious).
- The pattern home is unambiguous; nothing is forced.

---

## Tier reasoning (explicit — the v169 cascade-error guard)

Routine v2.5 §31 keys the GOAL-ALIGNED vs OFF-GOAL tier on **(b) only**:
- **GOAL-ALIGNED INCLUDE** = (b) MODERATE+.
- **OFF-GOAL CAPTURE** = (b) FAIL, captured via (a)-rescue or operator override.

Here (b) = **STRONG** → **GOAL-ALIGNED INCLUDE**. (a)'s FAIL is irrelevant to the tier. This is the exact point the v169 build workflow got wrong (its synthesis + all 5 verifiers + critic shared "(a) FAIL → OFF-GOAL"); it is stated explicitly here so the error is not repeated. v168 ponytail (`(a) FAIL · (b) STRONG`) and v170 awesome-artificial-intelligence (`(a) FAIL · (b) MODERATE`) both shipped GOAL-ALIGNED on the same logic.

## §35 soft off-goal-rate ceiling

Rolling-3-ship window {v169 GA, v170 GA, **v171 GA**} = **0 OFF-GOAL → CLEAR.** No ceiling-override needed or taken. 18 consecutive goal-aligned ships v153→v171.

## Streak

`GA:32 · OG:11 [7 ov]` → **`GA:33 · OG:11 [7 ov]`** (33rd GOAL-ALIGNED PASS; NOT an override; "49+3\*" frozen @v125).

## Domain note

v168 (code-minimalism) / v169 (defensive-security) / v170 (AI-engineering field-map) varied the domain off the v153→v166 operating/monitoring niche. **v171 devspace returns to the goal-#1 substrate core** (MCP infrastructure for coding agents) but is a *fresh shape* — a hosted-chat-host → local-machine coding bridge, distinct from every prior corpus MCP server and from the operating-niche tools.

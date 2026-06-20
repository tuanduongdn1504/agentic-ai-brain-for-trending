# (C) devspace — LLM Wiki (v171)

> **Ship:** v171 · 2026-06-20 · branch `wiki/v171-devspace` off `main` (based at `9561603` = v170, which is not yet merged — branching off `main`/`b55e0d4` would orphan the v168 + v169 + v170 cumulative state)
> **Verdict:** GOAL-ALIGNED INCLUDE 3/4 — (a) FAIL · (b) STRONG · (c) STRONG · (d) STRONG
> **Pattern outcome:** **1 NEW Library-vocab §C standalone (CORPUS-FIRST, N=1)** — *"Self-Hosted MCP Bridge that Turns a Hosted Chat Host into a Local Coding Agent (remote→local file+shell+git access via tunnel + owner-approval, no file upload)."* Plus a **clean Pattern #18 sub-mechanism B / B1-MCP instance-strengthening** (devspace is another one-server-many-MCP-clients instance, the agentmemory v66 / codegraph v70 lineage). Secondary scoped observations only (#84 / #22 / #19 / #66). NO new top-level pattern (max stays **#85**). Counts UNCHANGED (**46 / 10**); tracked PROVISIONAL §C surface ≈28 → ≈29 (+1 standalone).
> **Tier:** **T2 Service** (a self-hosted MCP server / developer tool you install + run; kin to codegraph v70 and agentmemory v66).
> ✅ **Returns to the goal-#1 core** after three domain-varying ships (v168 code-minimalism / v169 defensive-security / v170 AI-engineering field-map). devspace is dead-center on *"master Claude and autonomous agents for software development"* — it is MCP infrastructure that *makes a chat host into a coding agent over local code.* It is a fresh shape, not a return to the v153→v166 operating/monitoring niche.
>
> ⚠️ **(a) FAIL is genuine, not a downgrade.** The author discloses an identity (indie solo-founder, GitCMS creator, public revenue goal) — more than v168's bare handle — but "fellow indie developer" is **not a registered (a) cultural-peer axis**, and per the v159→v170 discipline a name/heritage inference is not an (a)-rescue. The tier keys on **(b)**, which is STRONG → GOAL-ALIGNED regardless. See §5.

---

## 1. What it is

`Waishnav/devspace` — tagline, verbatim:

> *"Turn ChatGPT into Codex"* — *"Bring a Codex-style coding workflow to ChatGPT."*

devspace is a **self-hosted MCP (Model Context Protocol) server** that gives a *hosted chat host* — ChatGPT first, "and Claude" / any MCP-capable host — the ability to **read, write, edit, search, and execute code in your local projects**, *without uploading your files to a third-party service.* You install it on your own machine; the chat host connects to it over a local endpoint (`http://127.0.0.1:7676/mcp`) or a public HTTPS tunnel, and from then on the chat behaves like a full local coding agent.

The thesis is stated bluntly by the author:

> *"My bet is that ChatGPT becomes the operating system for everything."*

devspace is the bet's first product: instead of a coding agent (Claude Code, Codex CLI) that *already* lives on your machine, it takes a host that *doesn't* — a hosted chat UI — and **brings the machine to it**, behind an explicit, inspectable, owner-approved tool surface.

This is the corpus's **first** subject of this exact shape: a self-hosted bridge whose function is to *turn a non-coding-agent chat host into a local coding agent.* (See §6 for why this is distinct from the corpus's prior MCP servers.)

## 2. What it exposes (the MCP tool surface)

Per the README, devspace exposes these capabilities to the connected host:

- **Read, write, and edit files** in the workspace.
- **Search code and inspect directories.**
- **Run shell commands** — for tests, builds, git, and package scripts.
- **Follow instructions from `AGENTS.md` and `CLAUDE.md` files** (it honors the agent-instruction convention as a first-class feature).
- **Discover local agent skills from skill folders** (it is a *consumer* of the agent-skills convention — the production end of which is the agentskills.io / `SKILL.md` ecosystem the corpus tracks at Pattern #57).
- **Display tool cards and change summaries** in compatible hosts (ChatGPT Apps-compatible UI).
- **Git worktree isolation for parallel coding sessions** — multiple isolated working trees so the host can run parallel coding sessions without clobbering one another.

That last item is notable for goal #1: **git-worktree-per-parallel-session is exactly the isolation mechanism Claude Code uses for parallel sub-agents**, and it is the substrate of the operator's active multi-agent-orchestration pilot thread. devspace ships it as a built-in.

## 3. The distinctive contribution (why it's corpus-first)

The corpus already has MCP servers — but they all run in the *opposite direction* of devspace:

| Subject | MCP role | Direction |
|---|---|---|
| **agentmemory** (v66) | memory backend (51 tools) | *adds memory to* a local agent |
| **codegraph** (v70) | pre-indexed code knowledge graph (8 tools) | *adds read-only context to* a local agent |
| **google_workspace_mcp** (v140) | Workspace tools, tiered | *adds SaaS reach to* a local agent |
| **supermemory** (v132), **nature-MCP** (v119) | memory / domain data | *augment* a local agent |
| **devspace** (v171) | file + shell + git over your machine | **turns a *hosted chat host* INTO a local coding agent** |

Every prior MCP server in the corpus **augments a coding agent that already exists locally** (Claude Code, Cursor, Codex CLI) with extra context or memory. devspace **manufactures the coding agent**: it takes a host that has *no* local presence (a hosted chat UI) and grants it full read/write/execute/git over your machine. The axis is the **direction of the bridge** (remote-host → local-machine) plus the **remote→local security model** (tunnel + owner-password approval + folder-root allowlist) that the direction forces. That combination is new to the corpus.

This is the same shape as v140 google_workspace_mcp (a clean Pattern #18 MCP instance *and* a corpus-first capability standalone) and v165 lazyagent (a clean tier-instance *and* a corpus-first capability standalone). The capability is the mint; the MCP-server structure is instance-strengthening of Pattern #18 (§6).

## 4. How it works (architecture + security model)

- **Install / run:** `npm install -g @waishnav/devspace` → `devspace init` → `devspace serve`. Connect at `http://127.0.0.1:7676/mcp` (local) or via a public HTTPS tunnel.
- **Stack:** TypeScript 87.3% / JavaScript 8.2% / CSS 4.3% / HTML 0.2%; Node.js ≥ 20.12 < 27 (22 LTS recommended); Vite build; npm. (Page-stated; §7.)
- **Security / approval model** (the load-bearing part of a remote→local bridge):
  - **Owner-password approval at connect time.** When a client connects, devspace opens an *Owner password approval page*; you enter the password printed by `devspace init`. The password is stored in `~/.devspace/auth.json` — "Keep that password private."
  - **Folder-root allowlist.** "You decide which roots are allowed" during init — the host can only reach the directories you grant.
  - **Explicit trust framing.** The README is candid: treat a connected client "like a **trusted coding partner with access to your machine**." This is honest-disclosure of the real risk surface (cf. Pattern #66 / #83 honest-deficiency-disclosure) — a remote chat host with shell-execution over your files is exactly as dangerous as it sounds, and the docs say so.
- **No file upload.** The privacy pitch: your code stays on your machine; the host reaches it through "explicit, inspectable tools," not by ingesting your repo into a third-party service.

## 5. Phase 0.9 verdict — GOAL-ALIGNED INCLUDE 3/4

- **(a) FAIL.** The author is **Waishnav** (@wshxnv) — an **individual indie developer**, GitCMS creator, openly *"on a journey to build a single-person company doing multiple millions in revenue."* He is not Anthropic, not an org, and not any of the vault's registered cultural-peer (a)-axes; the only major-vendor (a) carve-out, **(a)-7 "Foundational-Vendor-Direct-Source," is Anthropic-only.** He discloses *more* identity than v168 ponytail's bare handle — but **"fellow indie/solo developer building in public" is not a registered (a) axis**, and "Waishnav"/"Vaishnav" (Indian-heritage name) is a *heritage inference*, which per the v151 / v160→v169 discipline is **NOT** an (a)-rescue. **(a) FAILs cleanly; no rescue, no axis minted** — consistent with v168 (bare-handle FAIL) / v169 (corporate-not-Anthropic FAIL) / v170 (individual-author / name-inference FAIL). ⚠️ *Operator-reviewable:* "solo indie SaaS founder building in public" is the closest thing this subject offers to an (a) cultural-peer angle (Storm Bear *is* a software developer); it is recorded as an open calibration question, not minted. It does not affect the tier.
- **(b) STRONG.** Goal #1 = *"master Claude and autonomous agents for software development."* devspace is **MCP infrastructure for coding agents** — core Claude/agent substrate. It supports **Claude as a host**, honors **`CLAUDE.md`**, **discovers agent skills**, and ships **git-worktree-isolated parallel coding sessions** (the exact multi-agent mechanism the operator is piloting). It is directly *about* turning a chat model into an autonomous coding agent over local code — squarely on-goal, and directly pilotable into the vault. Held at **STRONG (not STRONGEST)** because the thesis is **ChatGPT-primary** ("turn *ChatGPT* into Codex"; "ChatGPT becomes the OS") with Claude as a secondary host, and it is third-party (not the vault's own work or an Anthropic substrate). STRONG-near-STRONGEST is defensible; either way → GOAL-ALIGNED (§31 keys on (b) MODERATE+).
- **(c) STRONG.** Real, substantial engineered surface: a published npm package (`@waishnav/devspace`), an MCP server in TypeScript (87.3%), a tunneling layer, an owner-approval auth system (`~/.devspace/auth.json`), folder-root sandboxing, git-worktree isolation, a CLI (`init` / `serve`), and tool-card UI. Shipped as **v1.0.0**. Not a prototype.
- **(d) STRONG.** A **corpus-first capability** (the §C standalone) on top of a **clean Pattern #18 B1-MCP instance** — the pattern connection is unambiguous and the novel axis (bridge-direction + remote→local security) is real, not forced.

**Tier (2-tier INCLUDE, routine v2.5 §31):** (b) is **STRONG** (MODERATE+) → **GOAL-ALIGNED INCLUDE**, full stop. (a)'s FAIL does **not** make a (b)-STRONG subject off-goal — that was the v169 cascade error, explicitly guarded against here.

## 6. Pattern Library outcome

**PRIMARY — 1 NEW Library-vocab §C standalone (CORPUS-FIRST, N=1):**

> **"Self-Hosted MCP Bridge that Turns a Hosted Chat Host into a Local Coding Agent (remote→local file+shell+git access via tunnel + owner-approval, no file upload)."**

CORPUS-FIRST — see §3 for the full distinction table. The novel axis is the **direction of the bridge** (a *hosted chat host* → *your local machine*, manufacturing a coding agent where none existed) plus the **remote→local security model** (HTTPS tunnel + owner-password approval + folder-root allowlist) that the direction necessitates. Distinct from every prior corpus MCP server (agentmemory v66 / codegraph v70 / nature-MCP v119 / supermemory v132 / google_workspace_mcp v140 — all *augment a local agent*), and distinct from the GUI-wraps-a-local-CLI direction of CodePilot v161 (the opposite vector). **§28: 1 new standalone (≤2 cap honored). PROMOTION-ELIGIBLE at a genuine 2nd "hosted-chat-host → local-machine coding bridge." Time-aware stale-watch: ≥15 wikis AND ≥30 days (§39).**

**SECONDARY — clean Pattern #18 sub-mechanism B / B1-MCP instance-strengthening (tracked at the #18 layer, NOT this standalone):** devspace IS a one-binary-many-MCP-clients server (ChatGPT, Claude, any MCP-capable host) — the agentmemory v66 / codegraph v70 B1-MCP lineage, instance N+1. This is the *distribution structure*; the §C standalone is the *capability/direction*. Different axes (the v140 / v165 precedent) → both recorded, no double-count, no over-mint.

**SECONDARY observations (NOT minted):**

- **Pattern #84 84c "Provider-Agnostic-By-Design" — scoped observation.** devspace is **host-agnostic by protocol**: it serves any MCP-capable host (ChatGPT / Claude) over one server, and consumes **both** `AGENTS.md` **and** `CLAUDE.md`. Recorded as a scoped 84c observation on the *host/instruction-convention* axis — NOT the ponytail 84c.1/84c.2 "14-platform native-rule-file distribution" mechanism (that contamination was caught + rejected at v169; do not repeat it).
- **Pattern #22 (AGENTS.md / CLAUDE.md) — consumer-side cross-reference.** Most #22 observations are about a repo *having* these files. devspace is unusual: it *consumes* them as a runtime feature (it follows their instructions, and discovers `SKILL.md` skill folders). A consumer-side data-point, noted, not re-minted.
- **Pattern #19 (ecosystem / portfolio-builder), sub-archetype 19a (founder-personal-portfolio) — data-point.** Waishnav = solo founder building a product portfolio (GitCMS + devspace) toward an explicit single-person-company revenue goal. Clean data-point of a CONFIRMED pattern; no new sub-mechanism.
- **Pattern #66 (supply-chain / security-conscious design) — cross-reference.** Local-only (no upload), owner-password approval, folder-root allowlist, explicit "trusted coding partner with access to your machine" disclosure. Security-conscious by design; cross-referenced, not instanced.

**Explicit NON-claims:**

- **NOT a new top-level pattern.** Max confirmed stays **#85**; the bridge capability lives at the §C-standalone tier per §28 (the same anti-inflation that rejected #86/#88 at v168).
- **NOT Pattern #52 (viral velocity).** ≈1,400★ / 131 forks / 1 release (v1.0.0, 2026-06-16) are **page-stated, NOT API-verified** (§37.4). If creation ≈ release, the page-implied rate (~350★/day over ~4 days) would *look* EXTREME-tier — but with **no API-verified creation date**, velocity is **unestablishable** → explicitly **not a #52 claim** (the v168/v169/v170 discipline).
- **NOT Pattern #57 (corpus-recursion).** devspace *mentions* ChatGPT / Codex / Claude as hosts and consumes the agent-skills convention, but it cites **no Storm Bear corpus subjects** as source material. Mentions/convention-consumption ≠ recursion.
- **NOT a re-classification.** It is a clean #18 B1-MCP instance + a corpus-first capability standalone — not a new tier, not a new sub-archetype mint.

**Counts UNCHANGED: 46 confirmed top-level patterns / 10 CONFIRMED Library-vocab.** Tracked PROVISIONAL §C surface ≈28 → **≈29** (+1 standalone).

## 7. §37 provenance

- **Page-stated, NOT API-verified (§37.4):** ≈**1,400★ / 131 forks / 1 published release (v1.0.0, 2026-06-16) / 1 contributor** *(as of 2026-06-20 page render, github.com/Waishnav/devspace — confidence: stated, NOT API-verified)*. **MIT** license. Languages: TypeScript 87.3% / JavaScript 8.2% / CSS 4.3% / HTML 0.2% (page-stated).
- **No API-verified creation date** → age & velocity **unestablishable** → **explicitly NOT a Pattern #52 claim.** The single release dated 2026-06-16 is page-stated, not API-verified.
- **Author identity:** "Waishnav" (GitHub `Waishnav`, X `@wshxnv`), GitCMS creator, "single-person company / multiple millions in revenue" goal — confidence: **stated** (self-declared on the repo / profile), not independently verified. The (a) FAIL does not depend on the exact identity (an individual non-Anthropic author FAILs (a) regardless).
- **README contents** (§2 capabilities, §4 security model) are page-verified from the rendered README + repo page at ship time. The git-worktree-isolation feature is README-stated; no implementation detail is published in the README (recorded honestly).

## 8. Streak / state

- **Streak:** `GA:32 · OG:11 [7 ov]` → **`GA:33 · OG:11 [7 ov]`** (33rd GOAL-ALIGNED PASS; NOT an override; historical "49+3\*" frozen @v125).
- **§35 ceiling:** rolling-3-ship window {v169 GA, v170 GA, **v171 GA**} = **0 OG → STAYS CLEAR.** No ceiling-override needed or taken.
- **18 consecutive goal-aligned ships v153→v171.** v168 (code-minimalism) / v169 (defensive-security) / v170 (AI-engineering field-map) varied the domain off the v153→v166 operating/monitoring niche; **v171 returns to the goal-#1 substrate core** (MCP infrastructure for coding agents) with a fresh shape.
- **Counts:** 46 confirmed patterns / 10 CONFIRMED Library-vocab **UNCHANGED.** Max pattern #85. PROVISIONAL §C surface ≈28 → ≈29.
- **Override-frequency triggers (2-in-20 / 3-in-30):** v153→v171 = **zero** operator overrides (clean).

## 9. Pilot note

devspace is the **highest-VALUE on-goal pilot candidate to date** *and* the **highest-RISK** — the two are inseparable here.

- **Why high-value:** it is directly pilotable into the vault. It could give Claude (or ChatGPT) MCP access to *this vault's own code*, it honors `CLAUDE.md`, it discovers `05 Skills/`, and its **git-worktree-isolated parallel sessions** are the exact substrate of the operator's active **multi-agent-orchestration pilot thread**. It is also relevant to the **hireui** pilot target (an MCP coding bridge for a real codebase).
- **Why high-risk:** it grants a **remote chat host read/write/EXECUTE/git access to your local machine over a tunnel.** That is a far larger blast radius than v169 SkillSpector (read-only) or v168 ponytail (config hooks).
- **Pilot fence (if attempted):**
  1. `install-snapshot` first (global npm install — capture what `@waishnav/devspace` writes).
  2. `npm-security-check` on `@waishnav/devspace` *before* installing (new package, 1 contributor, global install, possible postinstall).
  3. **LOCAL-ONLY mode first** — `http://127.0.0.1:7676/mcp`, **no public tunnel** — until you trust it.
  4. Restrict the folder-root allowlist to a **scratch directory**, never the whole machine; keep the owner password private.
  5. Pin **v1.0.0**; treat shell-execution access as security-sensitive.
- **Ranking:** **SkillSpector (v169) remains the lowest-risk *first* pilot** (read-only, free, `--no-llm` over `05 Skills/`). devspace is the **highest-value** pilot but should come *after* a low-risk pilot proves the loop, and only behind the fence above. The PILOT lever still formally stands (zero piloted).

## Suggested next action

Commit the v171 ship on `wiki/v171-devspace` (don't merge — operator reviews + merges; the branch is based on v170/`9561603`, which is itself unmerged, to preserve the v168+v169+v170 cumulative state). Then the highest-value open move is still the **standing PILOT lever** — and devspace sharpens it: run **SkillSpector `--no-llm` over `05 Skills/`** first (lowest-risk loop-proof), then, if you want the high-value on-goal pilot, stand up **devspace in LOCAL-ONLY mode over a scratch dir behind the §9 fence** to test the multi-agent-orchestration / worktree-parallel-session workflow against the vault.

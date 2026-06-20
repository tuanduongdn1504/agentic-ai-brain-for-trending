# (C) PRIMARY — devspace (v171) — 1 NEW §C standalone + Pattern #18 B1-MCP strengthening + secondary observations

**Subject:** `Waishnav/devspace` — self-hosted MCP server that turns a hosted chat host (ChatGPT / Claude) into a local coding agent over your own machine.
**Pattern outcome shape:** the v140 / v158 / v165 shape — **1 corpus-first §C standalone (N=1) + a clean instance-strengthening of an existing pattern + scoped secondary observations, NO top-level mint, NO confirmed-count change.**

---

## PRIMARY — 1 NEW Library-vocab §C standalone (N=1, CORPUS-FIRST)

### "Self-Hosted MCP Bridge that Turns a Hosted Chat Host into a Local Coding Agent (remote→local file+shell+git access via tunnel + owner-approval, no file upload)"

A self-hosted MCP server whose **function** is to take a *hosted chat host that has no local presence* (ChatGPT first; "and Claude" / any MCP-capable host) and grant it a **full local coding-agent surface** over your own machine:

- **read / write / edit files**, **search code**, **inspect directories**,
- **run shell commands** (tests / builds / git / package scripts),
- **git-worktree isolation** for parallel coding sessions,
- honoring **`AGENTS.md` + `CLAUDE.md`** and **discovering local `SKILL.md` agent-skill folders**,
- reachable over a **local endpoint** (`127.0.0.1:7676/mcp`) **or a public HTTPS tunnel**,
- gated by an **owner-password approval page** (`~/.devspace/auth.json`) + a **folder-root allowlist**,
- with **no file upload** (code stays on the machine; reached via explicit, inspectable tools).

**Why CORPUS-FIRST — the bridge runs in a new direction.** Every prior corpus MCP server *augments a coding agent that already exists locally*:

| Subject | What its MCP server does | Vector |
|---|---|---|
| **agentmemory** (v66) | memory backend (51 tools, 15+ platforms) | augments a local agent |
| **codegraph** (v70) | pre-indexed code knowledge graph (8 tools, 4 platforms) | augments a local agent (read-only context) |
| **nature-MCP** (v119) | scientific-publishing domain data | augments a local agent |
| **supermemory** (v132) | memory provider | augments a local agent |
| **google_workspace_mcp** (v140) | Workspace tools, tiered exposure | augments a local agent (SaaS reach) |
| **devspace** (v171) | file + shell + git over your machine | **manufactures** the coding agent — turns a *hosted chat host* into one |

devspace inverts the vector: instead of adding context/memory/reach to Claude Code / Cursor / Codex CLI (agents that already live on the machine), it **brings the machine to a host that has no local presence**, and therefore must carry a **remote→local security model** (HTTPS tunnel + owner-password approval + folder-root allowlist + "trusted coding partner with access to your machine" disclosure) that none of the augment-a-local-agent servers need.

It is also the **opposite vector** of CodePilot (v161, "Desktop GUI Client / Visual Front-End for a CLI Coding Agent") — CodePilot *wraps a local CLI agent in a GUI*; devspace *gives a remote GUI/chat host a local agent.* And it is distinct from the orchestration platforms (Paseo v150 / ai-maestro v163 — they orchestrate *multiple* heterogeneous agents; devspace bridges *one* host to local code).

**The novel axis = (direction of the bridge: hosted-host → local-machine) × (the remote→local security model the direction forces).** That combination is new to the corpus.

**§28 compliance:** 1 new standalone (≤2 cap honored). **PROMOTION-ELIGIBLE at a genuine 2nd "hosted-chat-host → local-machine coding bridge."** Time-aware stale-watch: ≥15 wikis AND ≥30 days (§39).

**Forming meta-theme (WATCH, do NOT pre-merge):** *"MCP servers as the agent-capability substrate."* devspace (manufacture a coding agent), the augment-a-local-agent servers (v66/v70/v119/v132/v140), and the orchestration platforms all sit on the MCP-substrate axis — but on **different functions** (manufacture vs augment vs orchestrate). Recording them as one class would be the "generalize-the-definition-to-fit" error the corpus guards against.

---

## SECONDARY — clean Pattern #18 sub-mechanism B / B1-MCP instance-strengthening (tracked at the #18 layer)

devspace **is** a one-binary-many-MCP-clients server: a single self-hosted server serving any MCP-capable host (ChatGPT, Claude, …). This is a clean instance of **Pattern #18 → shared-backend-service sub-archetype → sub-mechanism B "one-binary-many-CLIENTS" → B1 MCP variant** — the **agentmemory v66 + codegraph v70** lineage (later joined by v119/v132/v140), instance **N+1**.

- This is the **distribution structure**; the §C standalone above is the **capability/direction**. Different axes → both recorded, **no double-count, no over-mint** (the v140 google_workspace_mcp precedent: a clean #18 MCP instance *and* a corpus-first capability standalone).
- Tracked at the Pattern #18 layer (in `_patterns/02b` / audit queue), **NOT** in the §C standalone tally.

---

## SECONDARY observations (NOT minted)

### Pattern #84 84c "Provider-Agnostic-By-Design" — scoped observation

devspace is **host-agnostic by protocol** — one server serves ChatGPT *or* Claude *or* any MCP-capable host, and it consumes **both** `AGENTS.md` **and** `CLAUDE.md`. Recorded as a scoped 84c observation on the **host / instruction-convention** axis.

⚠️ **NOT** ponytail's 84c.1/84c.2 "14-platform native-rule-file distribution" mechanism. devspace doesn't distribute rule files to N harnesses; it *serves* N hosts over one protocol and *reads* the two dominant instruction conventions. Keeping these distinct avoids repeating the v169 ponytail-contamination of the 84c framing.

### Pattern #22 (AGENTS.md / CLAUDE.md) — consumer-side cross-reference

Most #22 observations concern a repo *having* `AGENTS.md` / `CLAUDE.md`. devspace is the unusual case of a tool that *consumes* them as a runtime feature ("follow instructions from AGENTS.md and CLAUDE.md files") and discovers `SKILL.md` skill folders. A consumer-side data-point of the agent-instruction + agent-skills conventions. Noted, not re-minted.

### Pattern #19 (ecosystem / portfolio-builder), sub-archetype 19a — data-point

Waishnav is a solo founder building a product portfolio (GitCMS → devspace) toward an explicit "single-person company / multiple millions in revenue" goal. Clean data-point of the CONFIRMED Pattern #19 founder-personal-portfolio sub-archetype (19a). No new sub-mechanism.

### Pattern #66 (supply-chain / security-conscious design) — cross-reference

Local-only (no file upload), owner-password approval, folder-root allowlist, and the explicit "trusted coding partner with access to your machine" disclosure are a security-conscious posture (and an honest statement of the real blast radius — cf. #83 honest-deficiency-disclosure). Cross-referenced, not instanced.

---

## NON-claims

- **NOT a new top-level pattern.** Confirmed max stays **#85**; the bridge capability lives at the §C-standalone tier per §28 (the same anti-inflation that rejected #86/#88 at v168).
- **NOT Pattern #52 (viral velocity).** ≈1,400★ / 131 forks / 1 release (v1.0.0, 2026-06-16) are page-stated, NOT API-verified (§37.4); **no API-verified creation date** → velocity unestablishable. The page-implied ~350★/day (if creation ≈ release) is *suggestive only* and explicitly **not** a #52 claim.
- **NOT Pattern #57 (corpus-recursion).** It mentions ChatGPT / Codex / Claude as hosts and consumes the agent-skills convention, but cites no Storm Bear corpus subjects as source material. Mentions / convention-consumption ≠ recursion.
- **NOT a re-classification or a new tier.** Clean T2 Service / #18 B1-MCP instance + a corpus-first capability standalone.

**Counts UNCHANGED: 46 patterns / 10 CONFIRMED Library-vocab.** Tracked PROVISIONAL §C surface ≈28 → **≈29** (+1 standalone).

---

## Build note (transparency)

This wiki was built **inline** (not via the multi-agent build workflow). The v169 ship logged that the workflow's synthesis + all 5 verifiers + critic shared a single false premise ("(a) FAIL → OFF-GOAL") that defeated independent verification; an inline human-gated read of §31 is at least as reliable for a verdict that turns on the (b)-keys-the-tier rule. The tier call here was checked directly against routine v2.5 §31 + the v168/v170 precedent. The one judgment most worth a second opinion is **(b) STRONG vs STRONGEST** (ChatGPT-primary vs Claude-secondary) and the **(a) operator-reviewable "indie-builder axis"** question — both flagged above for the operator / next audit, neither minted at ship time.

# (C) Phase-0.9 verdict — v174 Agent-Reach — GOAL-ALIGNED INCLUDE 3/4

**Subject:** `Panniantong/Agent-Reach` — *"Give your AI agent eyes to see the entire internet… one CLI, zero API fees"*; self-described *"a capability layer, not just another tool."*
**Verdict:** **GOAL-ALIGNED INCLUDE 3/4 — (a) FAIL · (b) STRONG · (c) STRONG · (d) STRONG. Tier: T2 Service.**
**Tier key (routine v2.5 §31):** the tier keys on **(b)** goal-relevance. (b) STRONG (MODERATE+) → **GOAL-ALIGNED INCLUDE**, regardless of the (a) FAIL.

---

## (a) FAIL — author cultural-peer axis (but NOT a bare handle)

The author `Panniantong` (display **"Pnant Panniantong"**) discloses an indie-builder identity — verified by direct WebFetch of the GitHub profile:
- bio name **"Neo Reid"**, since 2020
- *"Solo founder. All employees are AI."*
- motto *"Ship it. Open-source it. Move on."*
- focus *"AI agents that actually do things"*
- public X **@Neo_Reidlab**; sibling repo **xfetch** (a Twitter CLI scraper)

This is **not Anthropic** (the only major-vendor carve-out, (a)-7 "Foundational-Vendor-Direct-Source," is Anthropic-only), and "solo indie builder building in public" is **not a registered (a) cultural-peer axis**. So (a) **FAILS**.

But it is **not a bare-handle case** like v173 claude-tap (`liaohch3`) or v172 (`DeusData`) — it is the **v171 devspace** situation (Waishnav, disclosed solo indie founder). Per the v171 precedent + standing recommendation (ii): the "indie-builder axis" is logged **operator-reviewable, NOT minted** as an (a) rescue → **clean FAIL under the current rule, no axis.** A name/heritage inference (Chinese-language origin from the WeChat/Chinese-platform focus) is likewise **NOT** an (a)-rescue (the v159→v173 discipline).

⚠️ **2nd instance flag (operator-reviewable, NOT minted):** this is the **second** subject (after v171 devspace) where a *disclosed* solo-indie-builder identity raises whether "solo indie founder building in public" should ever be a registered (a) cultural-peer axis for a software-developer operator. Recorded as **reinforcing** the v171 open recommendation, not resolving it.

## (b) STRONG — goal-relevance (the deciding axis)

Goal #1 = *"master Claude and autonomous agents for software development."*

Agent-Reach gives a coding agent a **genuinely new capability** — federated read+search reach across the open web, social, video, code-hosts, RSS, finance, and semantic search. An agent that can't read the web is half-blind; this is core agent-autonomy substrate. It is:

- **Claude-Code-first** among the supported agents (Claude Code ✓ / OpenClaw ✓ / Cursor ✓ / Windsurf ✓ / any shell agent).
- a **capability layer** (the README's own framing) — one install gives the agent reach across 13 heterogeneous platforms.
- **directly pilotable into the vault** (free multi-platform web research for the vault's own Claude Code, no API-key wiring).

Held at **STRONG (not STRONGEST):** third-party **bundler architecture** (it routes to existing OSS tools; it does not invent retrieval) and a **capability-augmentation** layer — it extends what the agent can reach, it is not the agent itself / not Anthropic core substrate. STRONGEST is reserved for Anthropic core substrate or the agent itself.

## (c) STRONG — engineered substance

Python capability layer; 13-platform federated readers/searchers; **ordered primary+fallback backend routing with real-time functional detection + auto-switch on failure**; `agent-reach doctor` diagnostics; MCP integration (Exa via `mcporter`, no key); credential security (`600`-perm local storage, no-upload, `--safe` / `--dry-run`, clean uninstall); **agent-driven self-install**; bundles ~9 backend tools (`twitter-cli`/`bili-cli`/`rdt-cli`/`yt-dlp`/`feedparser`/`gh`/`mcporter`/Jina/Exa); 7 releases to v1.5.0. Not a prototype.

## (d) STRONG — pattern home

A clean **§C capability standalone** (CORPUS-FIRST, N=1 — "Multi-Platform Web/Social Read+Search Capability Layer for Coding Agents") with an unambiguous home and a clear adjacency map (crawl4ai v29 / browser-use / Scrapling v149 / google_workspace_mcp v140 / Jina+Exa). Nothing is forced. See `(C) PRIMARY — multi-platform-web-reach standalone N1.md`.

---

## Tier-tag (routine v2.5 §31)

**GOAL-ALIGNED INCLUDE. Tier: T2 Service** (self-hosted local CLI capability-layer for agents; consistent with v171/v172/v173). (b) STRONG → the corpus's core. Counts toward the goal-aligned PASS streak: **GA:35 → GA:36.** §35 rolling-3-ship window {v172 GA, v173 GA, **v174 GA**} = 0 OG → CLEAR. **21 consecutive goal-aligned ships v153→v174.**

⚠️ **v169 cascade guard:** the v169 SkillSpector ship logged a shared-premise error ("(a) FAIL ⟹ OFF-GOAL") across its synthesis + verifiers + critic. That conflation is wrong — §31 keys the tier on **(b) only**, and v168 ponytail shipped GOAL-ALIGNED with exactly (a) FAIL · (b) STRONG. The v174 verification gave each of 3 lenses a distinct question precisely so they could not share that premise; the critic's `cascade_check` = "CASCADE RISK = ZERO."

## Verification

Verdict produced **inline**, then **adversarially verified by a 3-lens + critic workflow**:
- **Lens 1 (goal-relevance/tier/identity): AMEND** — (b) STRONG keys the verdict, (a) FAIL, T2 Service, streak math all CONFIRMED; two amendments raised: (1) note the disclosed indie-builder identity (v171 frame); (2) verify CORPUS-FIRST vs "v142 claude-web-research."
- **Lens 2 (capability-novelty/corpus-collision): CONFIRM** (high) — real grep; no collision; CORPUS-FIRST N=1 justified.
- **Lens 3 (secondary/non-claims): CONFIRM** (high) — secondaries + non-claims correctly scoped; #12 = confirmed-incidental scoped note.
- **Critic (anti-inflation): `overall: AMEND`** — `cascade_check` = ZERO; `inflation_check` = discipline HELD (1 mint ≤2 cap, N=1, max #85, no improper N-bumps, counts 46/10 unchanged); 3 amendments listed.

**Disposition:**
- **Amendment 1 ((a) identity framing): INCORPORATED** — independently re-verified by WebFetch of the profile (Neo Reid / solo founder / @Neo_Reidlab / xfetch); reframed (a) accordingly.
- **Amendment 3 (#12 incidental scoping): INCORPORATED.**
- **Amendment 2 ("v142 claude-web-research" collision): DISMISSED — confabulation.** Independent grep over all `_state/` chapters found **no** "web-research/claude-web/claude-web-research" subject anywhere; **v142 = OrcaSlicer-bambulab** (a 3D-printing slicer, STRICT 0/4 SKIP, T5 out-of-scope), and chapter `_state/04` (Lens 1's cited source) holds only v30–v39. The critic's "resolution" ("v142 provides single-platform web-search via Exa") was itself invented — neither Lens 1 nor the critic read the file. **The fabrication was NOT propagated.** CORPUS-FIRST N=1 stands on Lens 2's real grep + the independent grep.

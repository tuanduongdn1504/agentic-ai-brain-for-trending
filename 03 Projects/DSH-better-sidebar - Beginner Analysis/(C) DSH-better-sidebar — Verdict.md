# (C) DSH-better-sidebar — Verdict (v237)

**Subject:** `omdsh-dev/DSH-better-sidebar` · npm `dsh-better-sidebar` v0.13.0 · MIT
**Date:** 2026-08-18 · **Routine:** LLM Wiki Routine v2.7
**Verdict:** **GOAL-ALIGNED INCLUDE 3/4** · **NO MINT** · counts **46/11 UNCHANGED** · §C live standalones **49 unchanged**

---

## Phase 0.9 — four-criteria read

| # | Criterion | Call | Reasoning |
|---|---|---|---|
| **(a)** | Anthropic-authored / registered (a)-7 vendor-direct | **FAIL** | `omdsh-dev` = "Oh My DSH," an explicitly **unofficial community plugin org** for DeepSeek Harness (106 repos, 5 members, own hub). Not Anthropic; not DeepSeek either. §41 — no name/heritage/locale/notability rescue. #19 19a: first `omdsh-dev` author. |
| **(b)** | Goal relevance | **MODERATE** ⚠️STRONG-reviewable | *Keys the tier.* See below. |
| **(c)** | Substance | **STRONG** ⚠️MODERATE-reviewable | 216 commits / 10 releases in a week; a documented, capability-gated public extension API; a real test pyramid incl. a **real-host Playwright mount smoke test**; OIDC provenance publishing; lazy-load discipline; i18n; disclosed limitations. Caveats: v0.x against a release-candidate host, 97 open issues, the 7-vs-6 doc drift, ⚠️ **NOT source-cloned**. |
| **(d)** | Corpus connectivity | **STRONG** | Third consecutive ship in the v235 dependency graph; sibling to v236; the harness-UI family (CodePilot v161 §C#27 / hermes-webui v227 / lobehub v222 / Codex-Dream-Skin v216); the v158 observability sub-archetype (subagent topology); Pattern #68 (two "awesome" lists forming); #83 honest-deficiency disclosure; #66 both poles; an AionUi/v206 ecosystem-collision cross-ref. |

**Tier keyed on (b) MODERATE+ → GOAL-ALIGNED per §31. §40 available but not needed** — MODERATE is reached on the merits.

### Why (b) is MODERATE and not STRONG

**For MODERATE (what earns it):** the interaction surface of a **coding-agent runtime** is the Goal-#1 harness-UI substrate the vault studies (CodePilot v161 / hermes-webui v227 family). It ships a **sub-agent topology + task monitoring** panel (the v158 observability sub-archetype, as one tab). And its **extension-API design is a genuinely studiable artifact** for hireui's own agent-nativity spec — the best worked example the corpus holds of exposing a stable public API *from* a plugin.

**Against STRONG (what caps it):** it adds **zero agent capability**. That is not an inference — it is source-verified: `dsh.plugin.json` declares `contributes: { tools: [], skills: [] }`, **both empty**. The agent gains nothing; the *human* gains panels. It runs on a rival lab's release-candidate runtime, and **Claude appears nowhere in it** (v236 at least had Claude as an aesthetic target and an optional backend through the host's `llm-pi-ai` seam; here Claude is only whatever the host is configured with).

⚠️ **The v216 discriminator, applied again.** Codex-Dream-Skin v216 was (b) FAIL / OFF-GOAL because it was CSS wallpaper with **zero** functional surface. This implements terminal, git, filesystem, editor, browser and sub-agent-monitoring surfaces with a public API and a CI mount gate → **MODERATE, not FAIL** — the same shape as v236 and v217.

⚠️ **Reviewable alternatives, both recorded:** **(b) STRONG** is defensible on the extension-API-design + observability grounds → GA:95 either way. **(b) FAIL → OFF-GOAL** is *not* defensible here (the functional surface is far above the v216 floor), so no OG alternative is recorded.

---

## Pattern outcome: **NO MINT**

### Primary — instance-strengthening, not a new class

v236 recorded a **DEFERRED watch axis**: *"sanctioned in-process UI-seam replacement via a host agent's own plugin kernel."* v237 is a genuine second instance, but it requires **generalizing the axis**:

- v236 **replaced** the front door (a TUI in place of the default interface).
- v237 **adds** a right panel — and explicitly negotiates for the slot rather than seizing it (mutual exclusion with `aionui-panel`).

→ Generalize to **"sanctioned in-process UI-layer plugin on a host agent's own extension kernel"** → **N=2 (v236 + v237)**. **Recorded, NOT self-promoted** — a promotion is an audit act (the v232 / v235 rule). Flagged to the overdue audit.

### The §C-mint alternative — recorded and DECLINED

**Candidate:** *"Second-Order Extension Host — a third-party plugin that re-exposes its own public, capability-gated extension API so that further third-party plugins extend the PLUGIN rather than the host."*

**Genuinely distinct on mechanism**, hand-checked against every near neighbour:
- **CodePilot v161 §C#27** wraps a CLI agent **from outside** (spawns/drives it) — this mounts **in-process** → **NOT a clean §C#27 N=2** (the v227/v236 "distinct on two axes → adjacency" handling).
- **hermes-webui v227** = a separate web server fronting an install, not a kernel plugin.
- **Codex-Dream-Skin v216** = *unsanctioned* CDP injection vs a *sanctioned* kernel plugin.
- **Kilo Code v177** has an MCP marketplace but **is** the coding-agent product, not a plugin within one.
- **dsh-TUI v236** replaces a seam; it does not publish an extension point of its own.
- Corpus-first is real: `extension point` / `plugin API` / `second-order` / `registerTab` / `extensible` / `extension-host` all return **0** in `_patterns/06`.

**DECLINED on five grounds:**
1. **§C vocab is agent-capability-shaped.** Second-order extensibility is a *software-architecture* property, not an agent capability — and `contributes` is literally empty. The v236 "presentation-not-capability" objection applies with full force.
2. **Emphatically NOT world-first.** VS Code extensions have exported their own APIs to other extensions for roughly a decade (`extensions.getExtension(id).exports`); Eclipse extension points predate that; Backstage, Obsidian and Figma all do it. Minting this would be minting a standard software-engineering pattern the corpus merely hadn't written down.
3. **§28 anti-inflation / draw-the-circle** (camofox v179 / lobehub v222 / Firecrawl v214). "Plugin that hosts plugins" is first only because the circle is drawn there.
4. **The precedent chain now runs five deep** — lobehub v222, hermes-webui v227, Codex-Dream-Skin v216, dsh-TUI v236 all declined on front-end/UI-layer grounds. A fifth instance strengthens the rule rather than breaking it.
5. **Weak anchor.** One plugin — strong as it is — in a ~2-week-old ecosystem, among competing right-panels (`aionui-panel`, `dsh-web-ui`'s panel), from an org shipping 106 repos.

→ Recorded as a corpus-knowledge data-point + **a second DEFERRED watch axis: "plugin-as-platform — a third-party extension that publishes its own capability-gated extension API."** Flagged to the audit, **NOT executed.**

**Counts UNCHANGED: 46 confirmed patterns / 11 CONFIRMED Library-vocab. §C live standalones 49 unchanged. Surface ≈56 unchanged.**

---

## SECONDARY (recorded, NOT minted)

- **#57 genuine**, same relation shape as v236 (*runs inside* v235) — **17 `peerDependencies`**, the `@deepseek-ai/*` set at **`^0.1.0-rc.6`**, the same RC pin v236 carried. ⚠️ Now the **third consecutive ship in one dependency graph**, and the first **lateral** relation the corpus holds (v236 and v237 are unrelated sibling plugins in the same host, with no dependency on each other). Whether #57 needs a "sibling-plugins-in-a-prior-subject's-kernel" sub-variant is an **audit** call; N recorded-not-incremented.
- **#66 — a genuinely two-sided case.** *Positive:* **npm Trusted Publishing (OIDC) + `--provenance` + no `NPM_TOKEN` secret**, a zero-source-write rule, a build-purity gate, and a real-host mount smoke test. This is the **publish-side complement to pi v228's consume-side hardening playbook** — the corpus's two strongest supply-chain positives now cover both directions. *Negative:* `prepare` lifecycle script, `node-pty` native compile, user-togglable sandbox escapes (`browserNoSandbox` / `htmlViewerNoSandbox` / `htmlViewerDefaultUnsafe`) inside a panel holding a real shell and an embedded browser, 17 peers pinned to a **release candidate**, a ~2-week-old ecosystem with ≥6 unvetted directories, and **NOT source-cloned**.
- **#83 honest-deficiency disclosure** — the README volunteers its own gaps (no file watcher, no git push/pull/fetch, terminal remounts on pane drag, unusable <768 px) and the sandbox model is *shown in the UI* with deliberate temporary unlock. A clean instance.
- **v158 observability sub-archetype — ADJACENCY, NO N-bump.** The `subagent` tab is child-agent topology + task monitoring, but it is **one tab inside a UI plugin**, not an observability *tool*. Classing it as an instance would be the generalize-to-fit error (the claude-tap v173 discipline).
- **#84 84c INHERITED** from the host's provider seam, not implemented here → **NO N-bump** (identical to v236).
- **#12** — ships `AGENTS.md` as an enforced house-rules document consumed by agents working on the repo; **NO N-bump**.
- **Pattern #68 cross-ref** — ≥2 curated "awesome" lists have formed around DSH in ~2 weeks (`awesome-dsh-plugin`, `Dominic789654/awesome-deepseek-harness`). Ecosystem-formation data-point, not a subject.
- **LV-C4 cadence** — 10 releases across 7 days, page-stated **with explicit dates** (a firmer signal than star counts).
- **AionUi ecosystem-collision cross-ref** — `aionui-panel` ports the UI of **AionUi**, built by **iOfficeAI = the author org of v206 OfficeCLI**; v237 declares runtime mutual exclusion with it. ⚠️ Different author, no citation, no dependency → **NOT #57**.
- **Fourth consecutive ship handing the vault machinery for its own invariants** — v234 staleness-tracking → v235 doc-verification gates → v236 CI boundary gates → **v237 a pack-and-mount-into-a-real-host smoke test**. Pointed at the **C22–C27 backlog + the deferred retire pass**.

## NON-claims

NOT **#52** (stars/forks page-stated §37.4; the release cadence is cited as LV-C4, not velocity) · NOT **world-first** (VS Code extension exports / Eclipse extension points precede by ~a decade) · NOT **#18 B1-MCP** (ships no MCP server; `contributes.tools`/`skills` are **empty arrays**, source-verified) · NOT an **N=2 of §C#27** (wraps-from-outside vs mounts-in-process) · NOT an **N=2 of DeepSeek-TUI v72** (a standalone client for DeepSeek *models*) · NOT a **new top-level pattern** (max #85) · NOT **first-party DeepSeek** (explicitly unofficial) · NOT **the agent** (a UI layer) · NOT **source-cloned**.

## Tier

**T4 Plugin/Extension** (in-process UI-layer plugin — the `opencode-antigravity-auth` v67 bridge-plugin tier) with a **T2-client facet** (CodePilot v161 / hermes-webui v227 family). ⚠️ Tier reviewable — there is still no clean "UI-layer plugin" tier (the v192/v193/v213/v236 handling).

---

## Streak & §35

**v236 GA:94 → `GA:95 · OG:13 [7 ov]`** — **18 consecutive goal-aligned ships.**
**§35 CLEAR:** rolling-3 window {v235 GA, v236 GA, **v237 GA**} = **0 OG**.

---

## Verification record

✅ **INLINE + fully hand-verified** per `feedback_wiki_verify_independently_check_collisions`. **No workflow, no subagent** — the shim is **970,546 bytes (~242K tokens)**, which overflows every subagent's 200K context; the deep-dive workflows have failed prompt-too-long on every ship from v200 to v236.

- **Source hand-fetched:** rendered repo page, `README.md`, `README_EN.md`, `package.json`, `dsh.plugin.json`, `cordis.patch.yml`, `AGENTS.md`, `docs/external-plugin-guide.md`, the releases page, the org page.
- **Collision by sanity-anchored hand-grep — CLEAN.** `better-sidebar` **0**, `omdsh` **0**, `Oh My DSH` **0**, `betterSidebar` **0** across all of `_state/` + `_patterns/`. **Anchors confirm the grep works:** `deepseek-harness` 12/2, `dsh-TUI` 10/1, `Cordis` 11/2, `hermes-webui` 5/2, `CodePilot` 21/14, `lobehub` 12/8.
- **Live corpus links found by grep:** `AionUi` 5/2 (→ v206 OfficeCLI's author org) and `dsh-desktop` 1/1 (→ already flagged at v236).
- **Registry read verbatim:** the CodePilot §C#27 row (`_patterns/06:76`) and the full v236 §F entry (`_patterns/06:291`), which supplied the hand-verified near-neighbour boundaries.
- `inflation_check` **HELD** — 0 mints; the §C alternative declined on five grounds; counts 46/11 unchanged; max #85; no N-bumps (#84 84c none, #12 none, v158 adjacency-only, #57 recorded-not-incremented); no double-count.

### Errors caught by hand

1. **7-vs-6 built-in tabs.** Both READMEs say "7 built-in tabs"; `AGENTS.md`'s table lists **6** and its reference section says "6 tabs." Reconciled: `explorer` was folded into the `editor` "file window" at **v0.13.0** — the READMEs are one release stale.
2. **Corpus correction — v236's "four-day-old ecosystem" is imprecise.** DSH's page shows **12,404 commits / ~154.1k★**; this plugin's releases run 11 → 17 Aug. Accurate: *the public plugin ecosystem is ~2 weeks old; the DSH codebase is not.* Flagged for the audit.
3. **API-mocked figures rejected (§37.4).** `api.github.com` returned `created_at 2026-08-07` and 2,038 stars; per §37.4 the API is mocked here, so the **page-stated release dates** were used for the cadence claim instead — and **no #52 claim was made**.
4. **`contributes: { tools: [], skills: [] }` is empty** — this converted the "adds no agent capability" reasoning from an inference into a source-verified fact, and is what holds (b) at MODERATE.
5. **`aionui-panel` is not by iOfficeAI.** It lives in `zhu1090093659/dsh-web-ui` and *ports* AionUi's UI — so it is an ecosystem-collision cross-ref, **not** a corpus-recursive dependency on v206's author.

### Sandbox note (carried forward)

`python3` is silently broken in this environment (v236 finding, still true) → line-based `awk` / `sed` / `grep -c -F` only. The vault shell also intermittently drops stdout and returns `N matches in 0 files` — defeat it by re-running line-anchored (`awk '/pat/{print NR": "...}'`) or routing to a file. `git` here is old (no `branch --show-current`; use `rev-parse --abbrev-ref HEAD`).

---

## Bottom line

**A community org nobody had heard of two weeks ago built a VS Code-grade panel inside a rival lab's brand-new agent runtime, and then did the thing that actually matters: it published its own extension API and used it for its own built-ins.** That is the strongest available evidence that v235's *"Everything is a Plugin"* claim is re-entrant, not just marketing — the kernel supports plugins that are themselves platforms.

It is still a UI layer that adds no agent capability, on a rival lab's release candidate, with a `prepare` script and a native build. **Read it, steal two ideas, do not install it.**

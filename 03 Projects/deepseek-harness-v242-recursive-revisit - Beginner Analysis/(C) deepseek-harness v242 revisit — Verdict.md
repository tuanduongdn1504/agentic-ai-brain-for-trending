# (C) deepseek-harness — Verdict (v242 corpus-recursive revisit of v235)

**Subject:** `deepseek-ai/deepseek-harness` (`dsh`) · MIT · **`0.1.0-rc.7`** · clone HEAD `99f6f02fecdb…` (2026-08-17)
**Ship:** v242 · 2026-08-18 · **corpus-recursive REVISIT — the 4th in wiki history** (ECC v78 · agency-agents v185 · pi v228 · **dsh v242**)
**Verdict:** **GOAL-ALIGNED INCLUDE 3/4** · **NO MINT** · counts **46 / 11 UNCHANGED** · §C live standalones **49 unchanged** · surface **≈56 unchanged**
**Streak:** v241 GA:99 → **`GA:100 · OG:13 [7 ov]`** (**23 consecutive GA**, v220→v242) · **§35 CLEAR** (window {v240 GA, v241 GA, **v242 GA**} = 0 OG)
**Tier:** **T5 Agent-as-application** — agent-runtime / harness-kernel flavor (unchanged from v235; the grok-build v215 / Kilo Code v177 / OpenHands v30 tier) + a T2 self-hosted-service facet.
**Method:** ✅ **SOURCE-CLONED with full history** — the gap v235 disclosed. 14-agent workflow (11 succeeded, 3 schema-failed; ~1.60M subagent tokens, 485 tool uses, 426s) **plus** hand-verification of every load-bearing number. Collision grep run **before** analysis, and it is what caught that this subject was already v235.

---

## Why this revisit exists

v235 (2026-08-17) rated this repo and disclosed its own limitation in bold: **"⚠️ NOT source-cloned."** That gap turned out to be load-bearing — **four of the five caveats carrying v235's (c) risk assessment were third-party claims it could not check.** The operator elected the revisit over a duplicate or a chain-stop. It closes the gap and corrects the record.

---

## Four-criteria assessment (routine v2.7)

### (a) FAIL
DeepSeek AI — a Chinese frontier-model lab, **not Anthropic**. §41 applies: no name/heritage/locale/notability inference; a declared Anthropic affiliation or a registered (a)-7 vendor-direct source is required, and neither exists.

**#19 19a — RETURNING institution, third first-party `deepseek-ai` subject** (DeepSpec v186 · deepseek-harness v235 · this revisit). Unchanged from v235.

**⭐ New for this ship: the first-party status is now *source-verified*** — 2,246 of 12,404 commits (18.1%) from 10 distinct `@deepseek.com` addresses, distributed across the project's own development window (2026-06-19 → 08-17, 71.9% clustered 07-22 → 08-11), **not inherited** — the explicit contrast with v241. ⚠️ But the boundary is stated: the top author (42.4%, a GitHub noreply address) **cannot** be confirmed as staff from source, and the GitHub API is mocked here (§37.4), so that stays unknown.

### (b) STRONG — keys the tier, cleanly GA (no §40 rescue needed)
An **autonomous agent runtime for software development** = Goal #1 core. All four Claude/Anthropic contact points v235 identified are **CONFIRMED at rc.7**, and one is **extended**: rc.7 adds `feat(agent-presets): enable background Codex and Claude Code subagent tasks`.

Still **STRONG, not STRONGEST**, for exactly v235's reasons, which the clone confirms rather than softens: a competitor lab's runtime; DeepSeek models are the shipped default; **`packages/llm/` contains no `llm-anthropic`** — Claude is reachable only through the wrapped third-party pi seam; and it remains a developer preview with no evaluation story.

Dead-centre on live vault threads: harness-engineering, multi-agent orchestration, agent-primitive convergence, MCP-client posture, context compaction, and the claude-api-cost-optimization thread.

### (c) STRONG — and now *actually evidenced*, which is the point of the revisit
The clone materially **improves** the picture in the mechanisable places and **sharpens** the gap in the one that matters.

**Verified strengths:** exemplary vendor attribution (9 Shigma packages, author + MIT + per-package LICENSE preserved, `THIRD_PARTY_NOTICES.md`, an 18-section modification manifest); **deny-by-default install scripts** (pnpm `strictDepBuilds` + `allowBuilds`: 5 allowed, **3 explicitly denied, with a written rationale**); a **`minimumReleaseAge` cooldown** whose documented exclusion is pi itself; a lockfile with **1,203 resolutions and ZERO `npmmirror`/`taobao`/`cnpm`**; only **2** packages repo-wide declaring lifecycle scripts; a **benign 845-line stdlib-only `postinstall`** (local git hooks, ownership marker, lock, no network fetch); real cross-platform sandboxing incl. an in-repo native `landlock-run`; **816 spec files / ~299K test lines / 723 fixtures — more test code than source**; **4 numbered postmortems**; **11 recorded *rejected* decisions**; and a **custom git merge driver** enforcing its own bilingual doc invariant.

**Caveats that survive contact with source:**
- **Developer preview `0.1.0-rc.7`**, breaking changes promised in bold (none materialised rc.5→rc.7, but the warning is forward-looking).
- **No evaluation harness at all** — `BENCHMARK.md` is still 3 lines; **adversarially CONFIRMED**. The single most important gap, and the only v235 caveat that holds.
- **Telemetry opt-out, default ON** (`DSH_TELEMETRY_DISABLED`), with an honest disclosure that it does not suppress the DeepSeek provider header (**#83**).
- **ZERO of 12,404 commits GPG-signed.**
- **Closed to external pull requests** by stated policy → no upstream recourse for a downstream fix.
- PRC-default DeepSeek egress; `dsh-plugin` ecosystem entirely unvetted for code behaviour.

**Caveats RETIRED as unsupported** — see the Deep Dive for evidence: "squashed-merge / contributor-hostile / provenance opacity" (**REFUTED**), "~19% ecosystem compatibility (41/219)" (**no in-repo basis**; v240 catalogued 1,390 plugins), "~10× token usage vs Pi" (**no in-repo basis**; the project's own meter is a documented ~4-char-per-token heuristic), "a confirmed context-duplication bug" (**documented as architecturally fixed 2026-08-11 — before the rc.5 v235 rated**).

### (d) STRONG
v235 (same repo) · the six-ship periphery v236/v237/v239/v240/v241 · **pi v228 / v36** (#57, now version-pinned and release-age-excluded by name) · grok-build v215 (§C row 102, still recorded-not-executed) · v181 cortex-hub (attribution contrast) · v239 (AI-authorship-provenance contrast) · the stale **v140 §C row** (Finding 10) · Pattern #12 · Pattern #18 (MCP client) · Pattern #66 · Pattern #83.

---

## Pattern outcome: **NO MINT** — the NINTH consecutive DSH decline

Counts **46 top-level / 11 CONFIRMED Library-vocab UNCHANGED**; §C live standalones **49 unchanged**; tracked surface **≈56 unchanged**.

**The mint was tested adversarially and REFUTED**, on three independent grounds:

1. **Decisive external prior art.** Eclipse RCP / OSGi (Eclipse 1.0 2001; 3.0 2004 = the platform as OSGi bundles) is the canonical self-extending plugin architecture whose workbench is itself a plug-in; VS Code's extension host, JupyterLab/lumino and Theia populate the space. Identical to the ground on which v241's desktop mint was declined.
2. **⭐ The subject does not claim novelty, and the architecture is credited to a third party.** `README.md:7`, verbatim: *"It uses an architecture where **everything is a plugin**, and is powered by [Cordis](https://github.com/cordiverse/cordis), whose design is described in [_A Programming Paradigm for Spatiotemporal Composability_](https://github.com/cordiverse/paper)."* dsh is the **consumer** of the plugin framework, not its author — `vendor/cordis/LICENSE` is "Copyright (c) 2021-present Shigma", upstream `cordiverse/cordis`. Minting would over-claim **on the subject's behalf** — the **v211 discipline**.
3. **§28 anti-inflation + chain depth.** The DSH chain is now **nine deep** (v216→v222→v227→v236→v237→v239→v240→v241→**v242**), eight consecutive DSH ships. A revisit of the chain's own host is the last place to mint.

**No new §C standalone. No new top-level pattern** (max #85 unchanged).

### Instance-strengthening — RECORDED, NOT self-incremented

- **⭐ The stale v140 §C row "Graduated / Least-Privilege Tool-Exposure" gains a strong, *implemented* N=2 candidate** (Deep Dive Finding 10): `docs/tool-catalog.md` documents opt-in-only high-privilege toolsets, and the dynamic-package toolset is *"Not in any shipped tree (a deliberate opt-in — dynamic package code reaches the real runtime)"* with activation gated on `ctx.dynamicCordisRunner` injection — *"a composition missing it never activates the tools."* This row has sat at N=1 for ~100 wikis; v238 raised it; v241 declined Fabric's version because enforcement was disclosed **unimplemented**. **This one is implemented and enforced by composition.** → **flagged to the audit; a promotion is an audit act (the v232 rule).**
- **pi v228's supply-chain exemplar → an independent instance** (deny-by-default `allowBuilds` + `minimumReleaseAge`), forming a set with **v241's desktop** (5-allow/3-deny, different package manager, same posture).
- **#57** — the pi dependency is now **exactly pinned** (`@earendil-works/pi-ai@0.82.1`) and named in a release-age exclusion list, the most precisely-evidenced form the corpus holds. Plus a **six-way governance fan-in** newly *explained* rather than merely observed.
- **#83** — telemetry off-switch scope disclosed honestly; `token-meter` self-labelled approximate.
- **#66** — two-sided: exemplary vendoring and lockfile hygiene vs. unvetted plugin ecosystem + default-ON telemetry.
- **grok-build v215 §C row 102 N=2** — unchanged from v235: **recorded, NOT executed.**

---

## The five findings, one line each

1. **⭐⭐⭐ "Closed core, open periphery" is the governance cause of the whole chain.** `CONTRIBUTING.md`: *"We are sorry that we cannot accept external pull requests at the moment"* → *"Create a plugin… Associate your GitHub project with the `dsh-plugin` topic"* → *"not a mandate from us."* The 1,390-plugin catalogue, the three plugin suites and the containing desktop client all descend from one sentence. 1,008 PR merges, all internal; the `deepseek-harness` org has **zero public repositories**.
2. **⭐⭐⭐ Four of v235's five load-bearing caveats were inherited third-party claims; three fail on contact with source. The one that holds is the one v235 verified itself** → **D25: an un-cloned subject's caveats are hearsay.**
3. **⭐⭐⭐ Two headline scale figures are bilingual double-counts** — "1,386 decision records" = 693 EN + 692 ZH; real = **693**. "~170K doc lines" → **90,857** English. The project enforces the pairing with a **git merge driver**; the vault counted the translations → **D23: declare the language basis of every count.**
4. **⭐⭐ The rc ladder tracked across six ships is version churn** — rc.5 → rc.6 = **69 minutes, +224/−224, version strings only**; rc.6 → rc.7 = 4 days, zero breaking changes, zero package delta → **D24: a version-number delta is not a code delta.**
5. **⭐⭐ Harness exhaustively tested, model never evaluated** — and with v240/v241's identity-only install gates, **nothing in the stack measures whether a plugin makes the agent worse.** Identity verified end to end; effect unmeasured end to end.

---

## Errors caught this ship — SEVEN, and THREE are mine or the vault's

| # | Error | Correction |
|---|---|---|
| 1 | **Mine** — inferred "DSH does not globally disable install scripts" | **Corrected upward**: `pnpm-workspace.yaml` deny-by-default + `allowBuilds`; the truth is stronger |
| 2 | **Agent** — "No CONTRIBUTING.md" | **FALSE.** It exists at root and is this wiki's headline source |
| 3 | **Agent** — "1,389 decision records (not 1,386 claimed)" | A **bilingual sum**, not a record count; hand count = **693** (the same trap v235 fell into) |
| 4 | **Agent** — merge counts 70 / 950 | Hand-measured **69 / 939**; used mine |
| 5 | **v235** — four inherited caveats | Three refuted / unsupported / stale |
| 6 | **v235** — two scale figures | Bilingual double-counts |
| 7 | **The corpus** — rc-ladder-as-maturity, inferred across six ships | 69 minutes across zero code |

⭐ **The v241 lesson held again:** every load-bearing number here was hand-verified, and three of the seven errors were caught by doing so rather than by asking an agent.

---

## Pilot posture

**⚠️ READ-AND-BORROW. INSTALL NOTHING. NOT a hireui component.** Reasons, all source-verified: developer preview with breaking changes promised; **no evaluation harness**; telemetry **default ON**; a `postinstall` (benign, but present); PRC-default DeepSeek egress; **closed to external PRs**, so a downstream fix has no upstream path; and a wholly unvetted plugin ecosystem.

**🔴 Never** point it at candidate data, and **never** treat a `dsh-plugin` topic listing or a catalogue entry as a safety signal — nothing in this ecosystem reviews plugin code.

**Do not cite:** "~19% compatibility", "~10× tokens", "a context-duplication bug", "1,386 decision records", or any star figure.

⭐ **A1 → C12 → B7** — the vault now holds **four** of the pieces for `verify-vault-docs` and this ship adds the fourth: v240 prose-vs-code · v240 the inventory rule *as working code* · v241 provenance-at-divergence · **v242 language-basis declaration (D23)**. DSH hands over a fifth mechanism outright: **a git merge driver that keeps a bilingual doc triple in sync.** **Eight consecutive ships have now handed over the parts.**

---

## Bottom line

**GOAL-ALIGNED INCLUDE 3/4 · NO MINT · counts unchanged · GA:100.**

The subject is better engineered than v235 could show and worse documented in exactly one dimension than v235 reported — and the difference between those two statements is one `git clone`. The revisit's real product is not a re-rating of DeepSeek's runtime; it is **four corrections to the vault's own record and a rule (D25) that says why they happened.**

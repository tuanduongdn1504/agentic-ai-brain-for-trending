# (C) dsh-anchored-standard — Verdict (wiki v238)

**Subject:** `xiaobright/dsh-anchored-standard`
**Date:** 2026-08-18 · **Routine:** LLM Wiki Routine v2.7 · **Operator-requested**
**Verdict produced INLINE + hand-verified** per `feedback_wiki_verify_independently_check_collisions`.

---

## 1. Phase 0.9 — four criteria

| Criterion | Call | Reasoning |
|---|---|---|
| **(a) Anthropic-affiliation / registered vendor-direct source** | **FAIL** | `xiaobright` is a **bare handle** — 6 repos, 32 followers, 0 following, no bio, no company, no location, no website. No declared Anthropic affiliation; not a registered (a)-7 vendor-direct source. §41 forbids name/heritage/locale inference. Cleaner FAIL than v237's org. #19 19a first `xiaobright` author. |
| **(b) Goal-relevance** | **MODERATE — keys the tier** ⚠️ **STRONG-reviewable** | See §2 below. |
| **(c) Substance** | **STRONG** | See §3. |
| **(d) Corpus fit** | **STRONG** | See §4. |

**Tier: GOAL-ALIGNED INCLUDE 3/4**, cleanly via §31 on (b) MODERATE+. **§40 not needed** (MODERATE reached on the merits). **No OFF-GOAL alternative recorded** — it sits far above the v216 (b)-FAIL floor (v216 was cosmetic CSS with zero functional surface; this is a source-verified behavioural mechanism with published ablations).

---

## 2. (b) MODERATE — why, and why STRONG is genuinely arguable

**For MODERATE (the recorded call):**
- It is a preset for a **rival lab's harness**, targeting a **rival model** (DeepSeek V4 Pro), pinned to a **release candidate**.
- **Claude appears only as something it deletes** — the `CLAUDE.md` digest is one of the auto-injections `context-gate` strips. There is no Claude support, no Claude path, nothing to install for a Claude user.
- The benefit it exists to deliver is **not established** (see §5) — so the on-goal payoff is a hypothesis, not a capability.
- Consistent with the v235→v237 DSH run, all held at (b) MODERATE.

**For STRONG (recorded as reviewable):**
- The subject matter *is* harness engineering — the exact substrate Goal #1 names — and it is the first corpus subject to treat **the tool surface as a cognitive variable** rather than a budget line.
- Its central finding maps onto a **documented first-party Claude platform feature** (Tool Search Tool + `defer_loading: true`), so the operator can test it natively.
- It lands directly on the vault's **live infrastructure problem**: the ~54K-token tool catalog, which this session again proved binding when 18 workflow subagents overflowed at ~207K. Issue #6 measured a ~9 KB injection destroying a reproducible effect (81% → 0/9); the operator's is ~6× larger.
- It is on the `claude-api-cost-optimization` thread from a new angle (surface size as a quality variable, not only a cost variable).

**Recorded MODERATE**, consistent with the run; the STRONG case is flagged for the audit.

---

## 3. (c) STRONG

**Substance verified:** the mechanism is real and well built. `context-gate.mjs` hooks two genuine unified injection paths (`system-prompt/assemble` blanking `contexts` wholesale; `agent/pre-step` filtering to the claimed batch + `allowKinds`), promotion is derived from durable `tool/call` / `assistant/message` events so resume is safe, `compaction/end` re-demotes, and both filters **fail open** by explicit design. `tool-bootstrap.mjs` filters rather than replaces, composes the resident set from `bootstrapTools + ['dev_tool_search','skill_search','skill_load'] + unlockedFor(session)`, strips `bootstrapMaxTokens` at promotion for a documented reason, and degrades to the full catalog on a missing bootstrap tool while failing **at mount** on an invalid `promoteOn` — fail-soft at runtime, fail-fast at config. `toolchoice-adapter.mjs` vendors a protocol-faithful subset of DeepSeek's own SSE/serialize/translate pipeline to reach `tool_choice: "none"`, which the harness vocabulary does not expose, and discloses the vendoring in `NOTICE`. 7 self-contained modes, 19 test files, `sync-modes.mjs` enforcing self-containment in CI, zero dependencies.

**Caveats, stated honestly:** v0.1.0 and **maintenance-only as of 2026-08-17** · single-lab, single-model scope · pinned to `0.1.0-rc.5` while the ecosystem moved to rc.6 · **NOT source-cloned** (fetched files, not a clone) · `eternal-minimal.mjs`, `wire-think.mjs`, `cot-drip.mjs`, `deliberation-gate.mjs` are **doc-stated, not source-verified** (my fetch returned summaries for those; flagged rather than papered over) · two of the seven modes were designed by a contributor, not the author (per `ACKNOWLEDGEMENTS.md`) · the headline benefit is unreproduced.

---

## 4. (d) STRONG — corpus fit

The **fourth consecutive ship in one dependency graph** (v235 host → v236 UI-seam plugin → v237 UI-layer plugin-as-platform → **v238 agent preset**), and a third structural kind of DSH extension: a composition of the host's own rows rather than an added capability. Uniquely in the chain it pins **rc.5 — v235's exact release candidate** (v236/v237 both carried rc.6).

Threads it lands on: harness-engineering (openinterpreter v223, grok-build v215) · `claude-api-cost-optimization` · agent-behaviour rulesets (ponytail v168) · agent-skill optimisation (SkillOpt v178) · tool-exposure gating (google_workspace_mcp v140) · pre-LLM interception (headroom v144) · LV-C2 cost economics · Pattern #83 honest disclosure · the DSH ecosystem-formation data-point.

**⭐ Sharpest cross-reference — openinterpreter v223, independent thesis convergence.** v223's §C standalone rests on "a model's agentic performance depends on the harness it was RL-tuned against → ship one binary that *becomes* any harness." v238 reaches the identical premise from inside a single harness: find the specific lever that reproduces the trained-for condition, and measure it. Both converge on **Kimi K3** — v223 reimplemented the Kimi-Code harness Rust-native; v238's `FAREWELL.md` cites Kimi K3's technical report as evidence that training across diverse harnesses is the real fix. **Neither cites the other → NOT Pattern #57**, a genuine independent convergence, recorded.

---

## 5. What the evidence establishes (load-bearing)

| Claim | Status |
|---|---|
| The preset changes the **style** of the model's first reasoning chain | **ESTABLISHED.** #65 (@TipsyDrifter, 3×3 randomised block): 9/9 separated perfectly by preset; *"real and very robust."* |
| The tool schema is the decisive lever at default maxTokens | **SUPPORTED** by #11 (@Rtyyy233, 45-session controlled trial); README states 5/5 minimal anchored vs 11/11 standard-family standard-like. |
| Auto-injected context can destroy the effect | **ESTABLISHED.** #6: ~9 KB skill catalog → **0/9** anchored vs ~81% without. |
| The preset makes the model **better** | **NOT ESTABLISHED.** #65: +3.3 ability, **95% CI [−2.6, +9.3]**, ANOVA F(2,6)=1.05, not significant. |
| The headline "Project2 98/99" reflects the shipped composition | **NO — retracted by the repo itself.** #60 (@MolecularFullerene) showed those runs used `pwsh`+`read` → full 25-tool catalog; the exact Minimal pair came later. The README carries the caveat; **the tagline still advertises 98/99.** |
| The trajectory effect is stable on current weights | **DISPUTED.** #51 (@JimMilk, 11 rounds × 3 OSes): Ability 85–90, 98/99 not reproduced, trajectory showed **no correlation with scores**, *"not reproducible on current weights"*; losses traced to a **model-layer defect** (F3-05 session_id authorization) *"unrelated to OS/preset/trajectory."* |

**The two independent replications disagree with each other.** Any use of this subject must carry that.

---

## 6. PATTERN OUTCOME — **NO MINT**

**Counts UNCHANGED: 46 confirmed top-level patterns / 11 CONFIRMED Library-vocab. §C live standalones 49 unchanged. Tracked surface ≈56 unchanged.**

### Why no mint — five grounds

1. **Emphatically NOT world-first, and the closest prior art is Anthropic's own product.** The **Tool Search Tool** with `defer_loading: true` **strips deferred tools from the initial system prompt** and restores them on demand via a search tool — documented 77K → 8.7K tokens on the first request. That is the same bootstrap → discovery → promote shape, shipped first-party. Academic prior art is also thick: **arXiv:2604.21816** (dynamic tool gating + lazy schema loading, Apr 2026 — explicitly ties tool-visibility minimisation to preserved reasoning quality), **arXiv:2605.24660** (how many tools should an agent see), **arXiv:2512.15274** *"Well Begun, Half Done"* and **arXiv:2506.22058** *"Lost at the Beginning of Reasoning"* (the first step disproportionately determines the outcome), plus a least-privilege tool-restriction literature.
2. **The distinctive contribution is a RATIONALE + a MEASUREMENT, not a capability.** Everyone else stages tools for token economy or least privilege; this project does it for reasoning-trajectory selection and measures the dose-response. §C vocabulary is **agent-capability-shaped** → the **PixelRAG v211 discipline** applies exactly: *corpus-first for a technique ≠ a mintable §C class*, especially when not world-first.
3. **§28** — don't draw the circle around the instance.
4. **The benefit is unestablished and the replications conflict** (§5). Minting a class whose value one replication fails to confirm and another disputes outright would encode a contested claim as vocabulary.
5. **A weak, now-dead anchor in a crowded class.** v0.1.0, maintenance-only from 2026-08-17, one preset in a ~2-week-old ecosystem — and the class is **not anchored here**: `dsh-routing-suite` (~5.7k★, different author) does *"first-turn tool injection"*, `J-Space-Cognition-Suite` does model-agnostic inference-time cognitive control, and the subject's own issue **#53** is *"Convergent two-phase design from an independent lineage."*

**Fifth consecutive NO-MINT in the DSH chain — but on different grounds than v236/v237** (those were presentation-not-capability; this one is not-world-first + rationale-not-mechanism). Worth noting so the audit does not read a pattern of reflexive declines.

### ⚠️ §C-mint alternative RECORDED + DECLINED

*"Harness-Level Inference-Time Trajectory Conditioning — a host-agent preset that constrains the first request's API-visible tool schema and blanks every auto-injected context to select the model's reasoning trajectory, then auto-promotes to a resident catalog on a durable session event, with the intervention's dose-response measured."*

Genuinely distinct on mechanism and **corpus-first by grep** (`defer_loading`, `Tool Search`, `progressive tool`, `tool gating`, `lazy schema`, `attractor`, `resident catalog`, `dose-response`, `first-request` all **0** in `_state/03c`, `_patterns/06`, `_patterns/02b`). Hand-checked distinct from every near neighbour:

- **v140 `google_workspace_mcp` §C** — the closest row, and **NOT its N=2**: scoped by its own text to *"a 2nd **MCP server** with graduated/tiered tool exposure"* (v238 is a harness preset, not an MCP server), and its rationale is explicitly **API-quota + permission-scope**, applied as a **deployment-time static tier flag**. v238 is a **per-session runtime phase machine keyed on durable events**, for reasoning quality. Same silhouette, different animal.
- **v144 `headroom` §C** — pre-LLM interceptor that **compresses** for token economy; that row already distinguishes itself from v140's tool-registration gating.
- **v223 `openinterpreter` §C** — harness **emulation** (swap whole harness personalities); v238 is one measured lever inside one harness. Same thesis, opposite direction.
- **v178 `SkillOpt` §C** — optimises a skill **document** in text space via a validation gate. Different object.
- **v168 `ponytail` §C** — a hand-authored behaviour ruleset **injected** as prose; v238 **removes**, and its lever is the API tool schema.
- **v186 `DeepSpec`** — speculative decoding: weights/decoding layer, not the request surface.

**LOSES on the five grounds above.** → Recorded as a corpus-knowledge data-point plus a **DEFERRED watch axis**: *"harness-level inference-time trajectory conditioning — manipulating the first-request tool surface (and blanking auto-injections) to select a model's reasoning trajectory, dose-response measured."* Flagged to the audit, **not executed.**

### ⚠️ Also flagged to the audit — a stale row this ship touched

**v140's §C row carries *"5-wiki stale-watch ~v155"* and is still at N=1 at v238 (~98 wikis).** Past both §28.3/§39 floors. The audit should decide: **retire, or generalise it** to cover staged tool exposure regardless of rationale (which would make v238 its N=2 and resolve this ship's boundary question in one move). Recorded, **not self-executed** — a promotion or retirement is an audit act (the v232/v235/v237 rule).

---

## 7. SECONDARY findings (recorded, NOT minted)

- **⭐⭐ Pattern #83 honest-deficiency-disclosure — the corpus's sharpest instance to date, and a *stronger form* than self-disclosure.** The tagline advertises "Project2 98/99"; the README body then dismantles it. Critically, the correction was **forced by a third party**: @MolecularFullerene's issue #60 showed the docs had *retroactively* re-attributed historical runs to a composition they never used. The author accepted it, documented the provenance caveat, added that the generic prefab *"must not"* carry those scores, and links both replications that fail to confirm the benefit. **Author-accepted third-party provenance correction** is a distinct and stronger 83-flavour than volunteering one's own gaps — recorded for the audit as a possible sub-mechanism.
- **⭐ LV-C2 cost economics — a research project killed by inference pricing.** Evaluation rounds went ~¥2 → ~¥12 (~$0.28 → ~$1.70); FAREWELL: *"continuing to pile on features without verification capability is irresponsible to users."* The citable lesson: **for inference-time research the binding constraint is the cost of EVALUATION, not development.** A tiny absolute number × many required rounds = project death.
- **#20 Token-Economy-Quantification — QUALIFIED-ADJACENT, NO N-bump.** It quantifies the intervention's *behavioural* effect (we/let-me rates, hit rates, ablation tables), not artifact token footprint → **N stays 4** (the ponytail v168 handling).
- **#57 — recorded, N NOT incremented.** Fourth consecutive ship in one dependency graph; a third structural kind of DSH extension; and the only member pinning v235's exact rc.5. Extends v237's lateral-recursion question — an audit call.
- **#19 19a** — first `xiaobright` author. Portfolio is measurement-first (`modeltest` frozen private eval harness; `modeltest-v5` *"failed experiments archive (stalled)"*; `remote-mcp`; `vision-mcp-pool`).
- **#66 — genuinely two-sided.** *Positive:* zero npm dependencies, **no lifecycle scripts**, no network calls, no telemetry, CI `permissions: contents: read`, atomic writes confined to `$DSH_HOME`, a tightly-bounded installing-agent contract. *Negative:* the prefab replays **80 KB / 212 KB of another person's recorded reasoning** into your session with stale tool results verbatim (only `skill_search` re-rendered live) = a self-inflicted context-injection surface; `custom-bash.mjs` **runs without OS sandbox confinement on Windows** (its own description says so); the README's own *"same trust level as shell access."*
- **DSH ecosystem formation.** Directories now claim **1,253** (dshplugin.dev) / **1,345** (deepseekdocs) plugins — v236 recorded ~1,120 one day earlier. The `dsh-plugin` GitHub topic reports **7,164**, which I treat as an unreliable upper bound (self-applied topic). The divergence is the finding.
- **Community collective, not a solo build.** `ACKNOWLEDGEMENTS.md` credits ~15 handles; two of seven shipped modes (Eternal Minimal, Wire Think-Execute) were designed by Greenhand-monster, and the FAREWELL states the contributors' work *"clearly exceed[s] my own capability range."*

### NON-claims

NOT #52 (page-stated §37.4) · **NOT world-first** (decisively — Anthropic ships the mechanism) · NOT #18 B1-MCP (ships no MCP server) · NOT an N=2 of v140 / v144 / v168 / v178 / v223 · NOT Pattern #57 for the v223 convergence (no citation either way) · NOT a new top-level pattern (max #85) · NOT first-party DeepSeek (*"not affiliated with or endorsed by DeepSeek"*) · NOT source-cloned · NOT a UI plugin (a preset — the third structural kind in the DSH chain).

---

## 8. Tier

**T4 Plugin/Extension (agent-preset / row-composition flavour)** with a **T1 Skill/Methodology facet** — the durable payload is the measured findings and `HANDOFF-2.md`'s pitfall lists, not the installable artifact (which is dead). **Tier reviewable at the audit**, since "agent preset" is a new structural kind for the taxonomy.

---

## 9. Streak / §35

- **Streak: v237 GA:95 → `GA:96 · OG:13 [7 ov]`** — **19 consecutive goal-aligned ships.**
- **§35 CLEAR** — rolling-3 window {v236 GA, v237 GA, **v238 GA**} = **0 OG**.
- No operator override consumed (operator-requested, GA on the merits).

---

## 10. Verification record

**Verdict INLINE + hand-verified.** ⚠️ **The Workflow tool FAILED** — all 18 agents died *prompt-too-long* at **~207.2K** (limit 200K). Routed around it with **7 direct `Agent` (Explore) fan-outs**, which succeeded. All corpus claims verified by me:

- **Collision grep, sanity-anchored** (`_state/03c` + `_patterns/06` + `_patterns/02b`): anchors hit (`deepseek-harness` 14, `dsh-TUI` 13, `better-sidebar` 7, `Cordis` 15, `SkillOpt` 21, `ponytail` 56) → grep confirmed working. Subject terms **all 0** (`xiaobright`, `anchored-standard`, `eternal-minimal`, `whoami`, `0liveiraaa`, `Cotexplorations`, `dose-response`, `resident catalog`, `str_replace_editor`, `dev_tool_search`, `Project2`, `prefab`, `defer_loading`, `Tool Search`, `progressive tool`, `tool gating`, `lazy schema`, `attractor`). Near-misses read in context and all incidental: "trajectory" = star-velocity + open-core trajectory; `tool_choice` = pi v228's `disableNamedToolChoice` config field; "agent preset" = v236 shipping presets as an aside; "V4 Pro" = DeepSpec v186.
- **§C rows read verbatim** for v140 (line 67), v144 (70), v168 (78), v178 (86), v223 (104) before ruling on distinctness.
- **Identity** by direct profile WebFetch → bare handle confirmed.
- **`HANDOFF.md` 404 confirmed twice** — absent from the git tree API listing *and* 404 on raw fetch.

**Errors caught during the build:**

1. **My own** — I told the operator the v237 shim compaction had "restored fan-out capability" after a trivial `Explore` agent succeeded at 15.8K. Wrong as stated: **the Agent tool works; the Workflow tool still fails at ~207.2K.** Corrected in-session. Precise remaining gap: the shim is ~**7K tokens (~30KB)** over the ceiling.
2. **An agent's confused issue-#11 table** — its rendering showed "8/8 We-need success · 100%" for `pwsh+read` while simultaneously showing that condition's let-me rate at 2.0–2.6, which contradicts itself. Not propagated; the README's own 5/5-vs-11/11 framing is cited with #11 attributed as the source, and the reconciliation is left flagged rather than invented.
3. **An agent honestly flagged its own gap** — WebFetch returned summaries rather than raw code for 4 of 5 exotic-mode files. Those are labelled **doc-stated** throughout, not presented as source-verified.
4. **A `dsh-plugin` topic count of 7,164** taken at face value would have wildly overstated ecosystem size against v236's ~1,120 → treated as an unreliable self-applied-topic upper bound.
5. **A near-miss mint** — the v140 row's surface similarity is close enough that "N=2 of v140" was tempting; reading the row verbatim showed it is scoped to MCP servers and to a quota/permission rationale, which kills it.

**`inflation_check`: HELD.** 0 mints. §C mint DECLINED on five grounds with the alternative recorded. No N-bumps (#20 qualified-adjacent, #57 recorded-not-incremented, #83 recorded). Counts 46/11 unchanged. Max top-level pattern #85 respected. No promotions self-executed (v140 generalise-or-retire flagged to the audit).

---

## 11. Pilot

**⚠️ Read and borrow — do NOT install.** Nothing here is installable for a Claude user: a dead v0.1.0 preset for a rival harness on an old release candidate, whose benefit two replications failed to confirm.

⭐ **A1 → B5 → C11** — read the three-lever finding and issue #6 (zero install) → write a tool-surface hygiene rule into `CLAUDE.md` (treat the MCP catalog as a *reasoning* variable, not only a token cost) → trial Anthropic's **Tool Search Tool + `defer_loading: true`** on the vault's own Claude Code and **measure** it against the ccusage/OTel layer.

Full menu in `(C) dsh-anchored-standard — Pilot Methods Menu.md`. **NOT a hireui component.**

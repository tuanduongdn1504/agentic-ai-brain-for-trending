# (C) DeepSeek-Balance-Whale-Widget — Verdict

**Wiki v277 · 2026-08-25 · `MeteorNOX/DeepSeek-Balance-Whale-Widget` · npm `dsh-whale-widget` v0.2.10 · MIT**

---

## Phase 0.9 STRICT — GOAL-ALIGNED INCLUDE 3/4

| Criterion | Verdict | Evidence |
|---|---|---|
| **(a)** author archetype is structural peer to the operator | **FAIL** | `MeteorNOX` is a **pseudonymous** handle — an explicit FAIL under (a)'s own wording — and **NOT Anthropic**, so §41 also answers no. No name/heritage/locale inference (§41). |
| **(b)** goal-relevance | **STRONG** ⚠️ *MODERATE reviewable* | Two independent grounds — see below. |
| **(c)** methodology-influence node | **STRONG** | `whale-widget-prompt.md` is a **spec written as an LLM prompt** and designated by the README as the authority for all future edits, carrying 12 numbered hard-won conclusions. A working instance of this vault's own founding thesis, reached independently — and the **third consecutive ship** to productise it from outside (v268 `lat.md`, v269 `llm-wiki`, v277). |
| **(d)** in-corpus reference | **STRONG** | **Pattern #57 at a verified N=3 in one subject:** **v235** DeepSeek Harness (host runtime, Cordis kernel, `session/event` stream, `dsh plugin` installer) · **v239** dsh-web-ui (its `dsh-market` probe script is what the HEAD commit exists to satisfy) · **v73** cc-switch (credited **by name, twice, in desktop-branch source**). |

**Sum of PASS = 3 → STRONG INCLUDE.** **(b) MODERATE+ → GOAL-ALIGNED INCLUDE** (§31). No §40 override invoked; no §35 pressure.

### The (b) call, and the decision I am handing you

**(b) STRONG** rests on two grounds, either of which alone would clear MODERATE:

1. **The repository ships a released, tagged application whose core service module exists to configure Claude Code.** `src-tauri/src/service/claude_config.rs` on `origin/For–WinDesktop` (tag `v1.0.0+win`, PR #26) writes `ANTHROPIC_BASE_URL`, `ANTHROPIC_AUTH_TOKEN` and **all four Claude model aliases** into the user's global `~/.claude/settings.json`, and the module openly credits **corpus subject v73 (`cc-switch`)** twice. That is direct goal-#1 substrate.
2. **The main product is an agent-spend metering surface** — the corpus's **7th** observability (a) metering instance — sitting on a live vault thread (`claude-api-cost-optimization`, the `ccusage → OTel → Grafana` observability thread).

⚠️ **The reviewable alternative is (b) MODERATE**, keyed on the **npm-published product alone**: on `main`, across all 15 tracked files, `Claude` / `Anthropic` / `MCP` return **zero** hits (positive controls `DeepSeek` = 4 files, `dsh` = 7), and neither product is deployable by this vault (no DSH instance; the desktop app is Windows-only). That is exactly the **v236 dsh-TUI** precedent — *"(b) MODERATE keys the tier ⚠️STRONG-reviewable"*.

⭐ **The tier is GOAL-ALIGNED under both readings, so nothing downstream turns on it** — streak, §35 and the override review are unaffected. **Say the word and I flip it.** I chose STRONG because the most goal-relevant code in the repository is real, released and tagged, and rating it MODERATE would mean rating the repository by the file its README happens to describe — which is the exact mistake §D45 exists to prevent.

---

## Mint decision — NO NEW MINT

**Counts: 46 top-level patterns / 12 CONFIRMED Library-vocab — UNCHANGED. §C-1 13 UNCHANGED. §C-2 38 UNCHANGED.**

**Corpus-first check, full vault extent** (24,116 `.md`/`.html`/`.sh` files; positive controls fire — `dsh-web-ui` 16 files, `deepseek-harness` 29, `Cordis` 18, `DSH` 27): `MeteorNOX` **0** · `dsh-whale` **0** · `余额` **0** · `balance widget` **0**. Subject is new to the corpus.

⚠️ **The near-collision was checked by hand, not trusted to the index.** v239's entry describes *"an animated whale pet"* assigned as the 6th instance of observability sub-flavour **(b)**. I cloned `zhu1090093659/dsh-web-ui`: `packages/` holds **`dsh-pet`** and **`dsh-miku-pet`**, and `grep -ri "MeteorNOX|dsh-whale-widget|DeepSeek-Balance-Whale"` over that clone returns **zero hits**. ⇒ Different projects, different authors, different npm scopes. (Convergence is over-determined regardless: DeepSeek's brand mark is a whale.)

### Recorded instance-strengthenings — recorded, NOT self-promoted

*(A promotion is an audit act — the v232/v235/v237/v239 rule.)*

| # | Class | Movement |
|---|---|---|
| 1 | v237's generalised axis *"sanctioned in-process **UI-LAYER PLUGIN** on a host agent's own extension kernel"* | **N=3 → N=4** (v236 + v237 + v239 + v277). Independent author, non-port, different function, Cordis-mounted via first-party `dsh plugin`. **PROMOTION-ELIGIBLE since N=3 — now over-satisfied.** |
| 2 | Observability sub-archetype, sub-flavour **(a) metering** | **N=6 → N=7** (v89, v109, v157, v158, v159, v165 + v277); sub-archetype overall **N=12 → N=13**. |
| 3 | Pattern **#57** corpus-recursive | **N=3 in one subject** (v235 · v239 · v73). |
| 4 | The **v73 `cc-switch`** class (agent-config rewriter that repoints Claude Code at another backend) | **N=2, credited-port flavour** — the v208 OmniRoute handling. |

⭐ **On #2 — it is (a), not (b), and reading the definition changed the answer.** Sub-flavour (b) requires *"a reactive desktop-pet/avatar whose state tracks aggregate agent **run-state** as the primary display."* This whale's primary display is **money**; its animations react to *user touch*, not to agent state. It is a **meter wearing a pet** — and the sub-archetype's **first (a) metering instance mounted in-process inside the host agent's own web UI**, rather than as a separate desktop app, menu-bar item or TUI. *(The v262 discipline: read the row's own definition before counting. It prevented a false (b) N=7 here.)*

### Mints DECLINED, with the ground named

| Candidate | Declined on |
|---|---|
| *"Affective/character-vehicle cost meter"* — the pet-that-is-a-meter hybrid | **presentation-not-capability** — the ground that decided v236 dsh-TUI, v216 Codex-Dream-Skin, v227 hermes-webui, v222 lobehub. A pet-shaped meter is a presentation of metering. Recorded as the sub-flavour observation above. |
| *"Balance-delta-derived spend ledger"* — metering spend by differencing an account balance, no usage API / no token counting / no log parsing | **technique-not-capability** (the v211 PixelRAG discipline) **+ not world-first** (balance-polling is not novel; with no network, priority is establishable neither way). **→ DEFERRED watch axis, N=1.** |
| *"Agent-config rewriter repointing Claude Code at a rival backend"* — the desktop branch | **`cc-switch` (v73) already occupies the class**, and this is an **openly-credited derivation**, not an independent instance. → recorded as v73-class N=2, credited-port flavour. |

⚠️ **§28 anti-inflation was NOT used as a ground for any decline** (§44.5 — it may not be the sole ground, and here it was not a ground at all).

### DEFERRED watch axes minted (N=1, recorded — not filed as §C rows)

1. **Balance-delta-derived spend ledger** — deriving agent spend from observed account-balance decreases, with a disclosed error model.
2. **The generating prompt as the maintained authoritative spec** — a repository whose design doc, onboarding doc and maintenance interface are one file explicitly written to be handed to an LLM. **Third consecutive ship touching this vault's founding pattern from outside.**

---

## Bookkeeping

| Field | Value |
|---|---|
| Streak | v276 `GA:133` → **`GA:134 · OG:13 [7 ov]`** |
| Consecutive goal-aligned | **57** (v220 → v277) |
| §35 off-goal ceiling | **CLEAR** — window {v275 GA, v276 GA, v277 GA} = 0 OG |
| Override review | **17th consecutive discharge** (v153 → v277 = 0 overrides; lifetime 10, 3 `[ceiling-override]` v146/v148/v152) |
| Top-level patterns | **46 UNCHANGED** (max #85 — none minted in 47 ships) |
| CONFIRMED Library-vocab | **12 UNCHANGED** |
| §C-1 / §C-2 | **13 / 38 UNCHANGED** |
| Tier | **T4 Plugin/Extension**, with a T2-desktop-application facet on the `For–WinDesktop` branch |

⚠️ **The ~v268 audit named at v259 is now SEVENTEEN SHIPS OVERDUE.** This ship hands it: the **v237 axis at N=4** (promotion-eligible since N=3, now over-satisfied), the **(a) metering N=7** increment, the **v73-class N=2**, the **(b) STRONG-vs-MODERATE** call above, and — inherited — v274's **v107 Enforced-Gate N=2 watch, now 169 ships past its scheduled "~v115"**, plus v275's **#23 N=6** and v276's **C26 mechanism-clause generalisation**.

---

## The verdict in one paragraph

**A five-day-old, fifteen-file hobby widget that is better engineered than most things the corpus reviews, and wrong at every point where it touches something it does not own.** Inside its own walls: a never-throw route contract, retry-with-stale-fallback, in-flight de-duplication, per-session cost bucketing that anticipates *subagent parallelism*, an explicit memory-leak disposer, an 8 KB body cap, no XSS path in 2,000 hand-written lines of framework-free DOM code, and — the best thing in it — **price rules versioned by date**, so historical hourly buckets are costed under the rule that was in force when they happened. The vault's own v270 rule was *"the only defence is a date"*; this author put the date in the code. Outside its walls: a missing `package.json` field silently broke marketplace installation until an emergency fix a day before this wiki; the highest-numbered release is an orphaned zip from before the project's history began; `"license": "MIT"` was a metadata claim forty hours before it was a document; three routes serve the user's account balance with `Access-Control-Allow-Origin: *`; and its own spec document states that the exported plugin name must match `package.json` — while the code still exports the dead pre-package name. **The spec is a prompt, and it is excellent, and its only false sentence is the one claiming how current it is.** ⇒ *The gate you cannot write is the one whose requirement lives in someone else's code.* 🔴 **And the sting is on the branch the README never mentions:** a Tauri desktop app in this repository rewrites your **global `~/.claude/settings.json`** to point every Claude Code invocation at `api.deepseek.com/anthropic` with a plaintext key, merging carefully for Claude and **clobbering `~/.codex/config.toml` wholesale** — because `serde_json` was already in the dependency tree and no TOML parser was. **v265's rule, in a stranger's codebase: a discipline travels freely wherever it is free, and stops wherever the safe choice would cost something.**

---

*Prefix `(C)` — Claude-authored under operator direction. Shipped on `wiki/v277-whale-widget` off the v276 tip (`56f35cb`); **NOT auto-merged.***

---

*Artifact: https://claude.ai/code/artifact/fc363e2a-3f77-462f-8344-296a673b63a3*

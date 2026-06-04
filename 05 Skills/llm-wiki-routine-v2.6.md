# LLM Wiki Routine — v2.6 delta (§35: Soft Off-Goal-Rate Ceiling)

**Codified:** 2026-06-01, post-v130 audit. **Status:** CURRENT (supersedes v2.5). **Base:** this is a delta on top of v2.5 (`llm-wiki-routine-v2.5.md`) — all of v2.5 §31–§34 (the 2-tier INCLUDE + GOAL-ALIGNED/OFF-GOAL-CAPTURE tagging + forward-only streak-split + per-ship tier-tag procedure) remains in force unchanged. v2.6 adds ONE thing: a forward governor on the off-goal-capture rate.

**Why:** v120 and v125 both correctly diagnosed off-goal intake as an *intake-channel* issue (not a Phase-0.9 criteria defect), and v2.5 gave off-goal capture an honest label (OFF-GOAL CAPTURE, via (a)-rescue or override). But honest tagging only *measures* off-goal intake — it does not *slow* it. The result: v127/v128/v129 were three consecutive off-goal captures ((a)-rescue N=4), off-goal rate 3-of-4 under v2.5, with no goal-#1 ship between them. §35 is the missing forward governor, adopted by operator sign-off at the v130 audit.

---

## §35 — Soft Off-Goal-Rate Ceiling

### §35.1 The rule

- **Window:** any **3 consecutive wiki-ships.** Audit-only sessions (e.g., v125, v130) are NOT ships — they do not count toward the window and do not advance it.
- **Ceiling:** **≤ 1 OFF-GOAL CAPTURE per rolling 3-ship window.** (OFF-GOAL CAPTURE = a (b)-FAIL subject captured via either the (a)-rescue channel or the override channel, per v2.5 §31.)
- **Breach:** the last 3 wiki-ships contain **≥ 2 OFF-GOAL CAPTUREs.**

### §35.2 Enforcement (soft)

While the ceiling is **breached**:
- The **next wiki-ship MUST be a GOAL-ALIGNED INCLUDE** ((b) MODERATE+, per v2.5 §31) before any further OFF-GOAL CAPTURE is built.
- If an **off-goal subject is requested while breached**, the routine MUST:
  1. **State the breach up front** (current rolling-window tally), and
  2. require **either** (i) a goal-aligned subject for this ship, **or** (ii) an explicit, logged **CEILING-OVERRIDE** from the operator.
- **CEILING-OVERRIDE** is distinct from the Phase-0.9 (a)/(b) operator override. "Soft" means the operator can *always* elect it with eyes open; it is logged (in the ship's verdict doc + the shim streak line) as `[ceiling-override]` so the bypass is visible, not silent.

### §35.3 Clear / reset

The ceiling **clears automatically** once the rolling 3-ship window again holds **≤ 1 OFF-GOAL CAPTURE** (i.e., after enough goal-aligned ships scroll the off-goal captures out of the last-3 window).

### §35.4 Relationship to the override-frequency triggers (2-in-20 / 3-in-30)

- The override-frequency triggers (routine v2.3 §7) are **RETAINED** — they specifically watch the *override door* for a systematic Phase-0.9 miss-pattern, and remain a narrower diagnostic.
- §35 is **broader and the operative forward governor**: it bounds the *total* off-goal-capture rate across BOTH doors (override + (a)-rescue), which the override triggers do not see.
- Where they overlap, §35 governs forward intake; the override triggers continue to fire as a diagnostic that mandates an override-review at the next audit.

### §35.5 Reporting

- The shim streak line reports the forward v2.5 figure (`GA:n · OG:m [k ov]`) AND, when relevant, the **current rolling-3-ship off-goal tally** and whether the ceiling is **BREACHED** or **clear**.
- A CEILING-OVERRIDE ship carries `[ceiling-override]` in its streak entry and a one-line justification in its verdict doc.

---

## §36 — State at codification (2026-06-01, post-v130)

- **Ceiling status: BREACHED.** Last 3 wiki-ships = v127 (OG) + v128 (OG) + v129 (OG) = 3 off-goal in 3.
- **Consequence: the next wiki-ship (v131) MUST be a GOAL-ALIGNED INCLUDE**, or carry an explicit logged `[ceiling-override]`.
- Forward streak (v2.5 §32): historical "49+3\*" FROZEN @v125; **GA:1 · OG:3 [1 ov]**.
- Override lifetime: 4 (v84 + v116 + v122 + v127); 3-in-30 tripped at v127 (v116+v122+v127).
- Pattern Library state UNCHANGED: 46 confirmed / ~25 active / 8 Library-vocab CONFIRMED.
- Cadence: next natural audit ~v134-v135.

**Routine now v2.6 CURRENT** (supersedes v2.5). v2.5 §31–§34 unchanged; v2.6 adds §35 (ceiling) + §36 (state) + §37/§38 (fact-provenance + audit-checklist addendum, added 2026-06-02 from the v134 READ pilot). NO Phase-0.9 STRICT criteria change (v125 cleared the criteria; v2.6 is an intake-governor + documentation-discipline layer, not a rubric change).

---

## §37 — Fact-Provenance Discipline (wiki-ship checklist) — added 2026-06-02

**Source:** borrowed by hand from the v134 obsidian-second-brain READ pilot (`03 Projects/obsidian-second-brain - Beginner Analysis/01 Analysis/(C) PILOT-borrow-by-hand-bitemporal-reconcile-synthesize.md`, Borrow 1). It keeps the vault's hand-curation gate — this is a **writing convention**, not automation. NO Phase-0.9 criteria change.

### §37.1 The rule
Every **volatile external fact** in a project entry / wiki index / shim carries an inline **recency marker + source + confidence tag**.

### §37.2 Format
`<claim> (as of YYYY-MM, <source> — confidence: <level>)`
e.g. `4.4k★ (as of 2026-06, github.com/1weiho/open-slide repo page — confidence: stated, NOT API-verified)`.

### §37.3 Confidence vocabulary (maps onto the vault's existing inferred-vs-declared discipline)
- `stated` — quoted verbatim from the source / repo page, or operator-declared
- `high` — multiple independent sources agree
- `medium` — single plausible source / reasonable inference
- `speculation` — Claude's inference (e.g. "Taiwan-inferred", "inferred China-Mainland")

The Phase-0.9 (a)-axis inferred-vs-declared call already uses this distinction informally (v89/v90 "inferred" ≈ speculation/medium; v119/v135 "declared" ≈ stated); §37 formalizes the vocabulary.

### §37.4 API-unverifiable metrics (the sandbox constraint)
This environment **mocks the GitHub API**, so stars / forks / `created_at` fetched via `curl` are NOT authoritative. Any such metric MUST carry `NOT API-verified` + its actual provenance (repo page / README / releases list). This replaces the ad-hoc caveat written by hand at v134/v135.

### §37.5 Scope — "volatile" =
star/fork counts, funding, version numbers, release dates, author role/affiliation/location, "X in Y weeks" velocity claims. Stable structural facts (license SPDX, file tree, language %) need provenance only when contested.

## §38 — Audit-Checklist Additions (reconcile + synthesize disciplines, human-gated) — added 2026-06-02

**Source:** Borrows 3 + 4 of the same pilot. The vault's mini-audits already ARE the reconcile/synthesize pass; §38 borrows the *structure* and keeps the operator as the write-gate (the source auto-resolves + auto-writes; the vault flags-for-operator + routes mints through §28).

### §38.1 Contradiction pass (reconcile)
At each audit, for flagged contradictions:
- **Classify** each: **clear-winner** (one fact supersedes — log the supersession + date) / **ambiguous** (both plausible — open it) / **evolution** (a position/verdict legitimately changed over time — log as history, NOT a contradiction).
- **contradiction ≠ evolution:** a verdict that changed across versions (e.g. open-slide "not yet corpus-relevant" v91 → subject v135) is evolution, not conflict.
- **Source-authority rank** when facts conflict: declared/primary > repo page > inferred.
- **Default outcome = flagged-for-operator.** The vault does NOT auto-resolve (the "ask before editing my notes" rule). Auto-resolution is explicitly NOT borrowed.
- **Track ambiguous ones** in `04 Reviews/(C) OPEN-CONFLICTS.md` with `status: open` so they don't evaporate in prose.
- **Report** the contradiction tally as `X found / Y resolved-with-operator / Z flagged-for-operator`.

### §38.2 Synthesis pass (synthesize) — routed through §28
Run these scan dimensions as audit prompts. The source auto-writes synthesis pages; the vault does NOT — every candidate routes through the §28 ≤2-new-standalones cap + clustering-first + auto-retire (the over-generation guard the source lacks):
- **cross-source** — a concept/pattern in 2+ unrelated subjects
- **entity-convergence** — authors/orgs recurring across subjects with no connection page (current gap: rohitg00 ×2 v66+v113, nexu-io ×2 v83+v91, cited-to-subject v91→v135 — candidates for a lightweight `entities/` index)
- **concept-evolution** — an idea with 3+ updates across wikis
- **orphan-rescue** — project entries with no inbound cross-reference

### §38.3 Discipline
§38 adds NO automation and NO scheduled agents. It is an audit *checklist*; the operator remains the write-gate. Rejected-as-incompatible (documented in the pilot): auto-rewrite-5–15-pages, scheduled headless agents, the Two-Output Rule, auto-resolution.

### §38.4 Not-yet-applied (deferred from the pilot's 5-item proposal)
Two proposed items are NOT in this addendum — the operator scoped the apply to Borrow 1 + the audit-checklist + the registry correction: **per-fact `History:` line on revision** (Borrow 2) and **`## For future Claude` preamble standardization** (Borrow 5). Both remain available to adopt later.

---

## §39. Time-aware auto-retire window (mini-codification, v151 audit 2026-06-04, operator sign-off)

Amends §28.3. The standalone-N=1 auto-retire window is now **time-aware**: a standalone N=1 is auto-retired at the next audit only once it has gone **both ≥15 wikis AND ≥30 days** without strengthening (retire on whichever threshold is satisfied *later* — "15 wikis OR 30 days, whichever is longer"). Re-registerable on a genuine 2nd instance.

**Why:** the wiki-count-only rule mis-fires under burst cadence. The v126–v151 window shipped 25 wikis in ~3 calendar days; the old rule would have mechanically retired days-old CORPUS-FIRST standalones (e.g. v132 "Open Comparative Benchmark Framework," ~19 wikis but ~3 days old) as "stale." The 30-day floor protects recent items during bursts; the 15-wiki ceiling continues to retire genuinely-stale items under slow cadence. Authoritative rule text updated in `llm-wiki-routine-v2.4.md §28.3`. This is the ONLY change adopted from the v151 audit's three recommendations — the off-goal-intake lever and the (a)-rescue tightening remain PENDING operator sign-off.

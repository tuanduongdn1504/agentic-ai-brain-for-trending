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

**Routine now v2.6 CURRENT** (supersedes v2.5). v2.5 §31–§34 unchanged; v2.6 adds §35 (ceiling) + §36 (state). NO Phase-0.9 STRICT criteria change (v125 cleared the criteria; v2.6 is an intake-governor, not a rubric change).

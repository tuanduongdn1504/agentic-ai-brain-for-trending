# (C) Pattern Library mini-audit — v130 (2026-06-01)

**Off-goal-capture closeout + adoption of the soft off-goal-rate ceiling (routine v2.6 §35).**

**Class:** operator-requested audit, run immediately after the v129 ship to "close out the now-doubled off-goal findings." **Routine at entry:** v2.5. **Routine at exit:** v2.6 (this audit codifies §35). **Streak:** unchanged (audit ≠ ship) — historical "49+3\*" FROZEN @v125; forward `GA:1 · OG:3 [1 ov]`. **State:** UNCHANGED (46 confirmed / ~25 active / 8 Library-vocab CONFIRMED). **Fact-verification:** 13th clean audit (v127/v128/v129 freshly fetched this session-arc; metadata clean).

---

## A. The off-goal-capture findings — CLOSED OUT

The finding is no longer a hypothesis; it is a measured trend. Under routine v2.5 (forward window from v126):

| Ship | Subject | Tier (v2.5) | Channel |
|---|---|---|---|
| v126 | compound-engineering-plugin | **GOAL-ALIGNED** | (b) STRONGEST |
| v127 | developer-portfolios | OFF-GOAL CAPTURE | override (a-FAIL, 0/4) |
| v128 | Echo Loop | OFF-GOAL CAPTURE | (a)-rescue (1/4) |
| v129 | English-level-up-tips | OFF-GOAL CAPTURE | (a)-rescue (1/4) |

**Confirmed findings:**
1. **Off-goal-capture rate = 3-of-4** under v2.5; the **last 3 ships are all off-goal** (v127/v128/v129). This is the dominant recent signal.
2. **(a)-rescue off-goal capture = N=4** (v80 + v123 + v128 + v129) — the channel the v125 audit flagged at N=2 is now robustly established (a-PASS + b-FAIL → WEAK INCLUDE on (a) alone).
3. **Override channel: 4 lifetime overrides** (v84 + v116 + v122 + v127); v127 re-tripped **2-in-20** and tripped **3-in-30 for the first time** (v116+v122+v127). Acknowledged; the forward remedy is §35 (below).
4. **English-learning micro-cluster N=2** (v128 + v129) — two consecutive off-goal captures in the same content domain by Chinese cultural-peers. **Noted, NOT minted** (off-goal captures do not drive the Pattern Library — §28 + v125 anti-inflation).

**Diagnosis (re-confirms v125):** this is an **intake-channel** issue, NOT a Phase-0.9 criteria defect. The STRICT criteria are working — they correctly tag every one of these (b) FAIL. v2.5 then correctly *labels* them OFF-GOAL CAPTURE. The gap is that **honest tagging measures off-goal intake but does not slow it** — neither the (a)-rescue door nor the override door has a default that discourages building an off-goal subject. **No criteria change. No re-tagging of history.** The fix is a forward intake governor.

---

## B. Decision adopted — SOFT OFF-GOAL-RATE CEILING (operator sign-off, this session)

Operator selected, among four candidate levers (outlier-track-by-default / per-request goal-aligned gate / soft rate ceiling / accept-as-deliberate), the **soft off-goal-rate ceiling.** Codified as **routine v2.6 §35** (`05 Skills/llm-wiki-routine-v2.6.md`):

- **Window:** any 3 consecutive **wiki-ships** (audit-only sessions do NOT count as ships and do NOT advance the window).
- **Ceiling:** **≤ 1 OFF-GOAL CAPTURE per rolling 3-ship window.**
- **Breach:** the last 3 ships contain **≥ 2** OFF-GOAL CAPTUREs.
- **Enforcement (soft):** while breached, the **next ship MUST be a GOAL-ALIGNED INCLUDE** ((b) MODERATE+) before any further OFF-GOAL CAPTURE is built. If an off-goal subject is requested while breached, the routine **flags the breach and requires either** (i) a goal-aligned subject first, or (ii) an explicit, logged **ceiling-override** (distinct from the Phase-0.9 (a)/(b) override; "soft" = operator can always elect it with eyes open).
- **Clear:** the ceiling resets automatically once the rolling 3-ship window again holds ≤ 1 off-goal capture.
- **Relationship to the override-frequency triggers:** the 2-in-20 / 3-in-30 override triggers are RETAINED (they specifically watch the override door for systematic Phase-0.9 misses). §35 is broader and more direct — it governs the *total* off-goal rate across BOTH doors (override + (a)-rescue). Where they overlap, §35 is the operative forward governor; the override triggers remain as a narrower diagnostic.

---

## C. Applying the ceiling to current state — BREACHED → v131 must be GOAL-ALIGNED

Last 3 ships = v127 (OG) + v128 (OG) + v129 (OG) = **3 off-goal in 3 → ceiling BREACHED (3 > 1).**

**Consequence: the next wiki-ship (v131) MUST be a GOAL-ALIGNED INCLUDE.** An off-goal subject requested for v131 will be flagged against the breach and will require either a goal-aligned subject first or an explicit logged ceiling-override. (v130 is this audit and does not count as a ship; the window is unchanged by it.)

This is the concrete teeth the prior two audits lacked: v120 and v125 correctly *diagnosed* off-goal intake but had no forward governor, so the rate kept climbing (v127→v128→v129). §35 converts the diagnosis into an enforceable forward constraint.

---

## D. Hygiene

- **Fact-verification:** v127 (developer-portfolios), v128 (Echo Loop), v129 (English-level-up-tips) were all freshly fetched (GitHub API + README) during this session-arc; metadata (stars/forks/dates/license/language) recorded as fetched. No corrections. **13th consecutive clean fact-verification audit.**
- **Pattern Library state:** UNCHANGED — 46 confirmed / ~25 active / 8 Library-vocab CONFIRMED. The three off-goal ships contributed ZERO new patterns / sub-archetypes / Library-vocab (§28 honored; registry `06` not moved). Correct, non-inflated outcome.
- **Streak:** UNCHANGED (audit ≠ ship). Historical "49+3\*" FROZEN @v125; forward **GA:1 · OG:3 [1 ov]**.
- **Cadence:** v130 audit complete. Next natural audit ~v134-v135 (or trigger-forced). **v131+ = wikis OK, BUT §35 requires v131 to be goal-aligned (ceiling currently breached).**

---

## E. Storm Bear's blunt take

The audit's headline was settled before it started — 3 off-goal ships in a row, (a)-rescue at N=4, override re-trip at v127 — so the value here is the *decision*, and it's the right one with teeth. v2.5 made off-goal capture honest; v2.6 §35 makes it *bounded*. The two prior audits (v120, v125) both correctly named the intake-channel problem and both lacked a forward governor, which is exactly why the rate climbed from "flagged" to 3-of-4. The ceiling fixes that: it doesn't ban off-goal capture (you can still elect it via a logged ceiling-override), it just stops the corpus drifting three-deep into cultural-peer cataloguing without a single goal-#1 ship in between.

And the part no accounting rule can fix: the ceiling now *forces* the thing I've recommended for six straight messages — **the next ship must be goal-aligned.** The cleanest way to satisfy it isn't to find another in-scope repo to catalogue; it's to finally **pilot v126 compound-engineering**, which is goal-aligned, already shipped, and still un-piloted. The ceiling and the standing recommendation now point at the same move.

---

*Codification: `05 Skills/llm-wiki-routine-v2.6.md` (§35). Closes the off-goal findings from v120 + v125 + the v127/v128/v129 ships. Override-frequency triggers retained as a narrower diagnostic under §35.*

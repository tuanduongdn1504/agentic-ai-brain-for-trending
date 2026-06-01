# Skill: LLM Wiki Routine v2.5 (delta)

**Status:** CURRENT (supersedes v2.4 as of 2026-05-30). v2.3 base + v2.4 §27–§30 remain authoritative; v2.5 documents the delta only.
**Trigger:** operator sign-off (2026-05-30) on the **v125 audit §C recommendation** — the corpus-knowledge-outlier track. The v125 audit (`04 Reviews/(C) 2026-05-30 … v125 …md`) DISCHARGED the first-ever 2-in-20 override-frequency trigger by finding it was **not** a Phase-0.9 STRICT criteria defect but an **intake-channel pattern**: off-goal subjects enter the corpus through two doors — **override** (when (a) FAILs) and **(a)-rescue** (when (a) PASSes) — and only the override door is honestly labeled. v2.5 codifies the fix.
**Scope:** a 2-tier INCLUDE distinction + a forward-only streak-split. **No Phase-0.9 STRICT criteria change** (the criteria are correctly calibrated — they accurately flag off-goal subjects). This changes verdict *labeling* and streak *accounting*, not the rubric.

---

## §31. The corpus-knowledge-outlier track (2-tier INCLUDE)

### The finding being resolved (v125 §B)

Phase-0.9 treats *any single criterion PASS* as INCLUDE-worthy, conflating two orthogonal questions: **"is the author a cultural-peer?" (a)** and **"does the subject serve goal #1?" (b)**. A cultural-peer's off-goal side-project PASSes (a) and thus "INCLUDEs" as a "WEAK INCLUDE 1/4" — which looks like a normal clean PASS, counts toward the streak/INCLUDE-rate, and carries no off-goal flag. Meanwhile an operator override of an off-goal subject ((a) FAILs) IS honestly flagged (0/4 + asterisk). Both admit subjects that don't serve goal #1; only one is labeled. **5 off-goal captures to date:** (a)-rescue — v80 SmartMacroAI (RPA), v123 MoneyPrinterTurbo (faceless-video); override — v84 image-blaster (creative-tech), v116 Sana (vision research), v122 dograh (voice-AI).

### The 2-tier distinction (keyed on (b) goal-relevance)

After Phase-0.9 produces its STRICT verdict, route the INCLUDE into one of two tiers by **(b)**:

- **GOAL-ALIGNED INCLUDE** — **(b) PASSes (MODERATE or better).** The subject genuinely serves goal #1 (Claude-Code tooling / agent-skills / autonomous-coding / LLM-tooling / vault-methodology). The corpus's core. Counts toward the **goal-aligned PASS streak**.
- **OFF-GOAL CAPTURE (corpus-knowledge-outlier)** — **(b) FAILs, but the subject is captured anyway**, via *either* channel:
  - **(a)-rescue** — (a) PASSes (cultural-peer), b/c/d fail → previously a "WEAK INCLUDE 1/4."
  - **operator override** — (a) FAILs / sub-threshold, operator force-builds → previously an "OVERRIDE."
  Tagged distinctly + honestly labeled **"off-goal corpus-knowledge."** Does **NOT** count toward the goal-aligned PASS streak and does **NOT** inflate the goal-aligned INCLUDE-rate.

**Decision rule (one line):** *INCLUDE with (b) MODERATE+ → GOAL-ALIGNED; INCLUDE with (b) FAIL (whether carried by (a)-rescue or by override) → OFF-GOAL CAPTURE.* SKIP (true out-of-scope, not force-built) is unchanged — not an INCLUDE, not a capture.

### What this fixes

Unifies the override + (a)-rescue channels under one honest label regardless of (a); stops the (a)-rescue channel from silently padding the streak; gives the operator a legitimate, non-punitive way to capture notable off-goal repos (which they clearly want — 5 instances) without it reading as either a discipline failure (override) or a goal-aligned win ((a)-rescue). The corpus's headline "INCLUDE rate" / "PASS streak" now measures **goal-#1 progress**, not "anything captured."

---

## §32. Streak-split — FORWARD-ONLY (operator-specified)

**Forward-only. Committed history is NOT rewritten.**

- **Frozen historical figure (through v125): "49+3\*"** = 49 PASS + 3 OVERRIDE. This figure is **NOT recomputed** and **NOT re-tagged.** v80/v123 stay recorded as "WEAK INCLUDE 1/4"; v84/v116/v122 stay "OVERRIDE." The 2-tier lens applies to their *lineage note* (they are the 5 retroactive examples of off-goal capture) but their per-wiki entries are unchanged.
- **Forward (v126+):** two running streams, reset/started at v126:
  - **GA — Goal-Aligned PASS streak:** consecutive count of GOAL-ALIGNED INCLUDEs ((b) MODERATE+). Broken by an off-goal capture **or** a SKIP.
  - **OG — Off-Goal Capture tally:** cumulative count of off-goal captures since v126, annotated by channel — `(a)r` = (a)-rescue, `ov` = operator override.
- **Forward notation:** carry the frozen historical alongside the forward streams, e.g.
  `49+3* (frozen @v125) · forward from v126 → GA:n · OG:m [k ov]`.
  A goal-aligned v126 reads `GA:1 · OG:0`; an (a)-rescue off-goal v127 reads `GA:0 (broken) · OG:1 [0 ov]`.
- **INCLUDE-rate reporting:** report the **goal-aligned INCLUDE rate** (GA ÷ goal-relevant attempts) as the headline; report off-goal captures as a separate line. Do not blend them into one "~97% INCLUDE" figure going forward.

### Override-frequency trigger — reconciled, NOT replaced

The 2-in-20 / 3-in-30 override-frequency trigger (v2.3 §7) **continues unchanged**, watching the **override mechanism specifically** (the `ov` subset) — overrides remain a distinct operator action worth rate-limiting. **NEW soft signal (v2.5):** also monitor **total off-goal-capture rate** (both channels). If off-goal captures exceed ~1-in-5 ships over any 10-ship window, flag it at the next audit as a goal-drift signal (the corpus cataloguing faster than it advances goal #1) — soft/advisory, not a mandated-audit trigger. (Rationale: the v125 finding is that the *combined* off-goal intake is the real pattern; the override-only trigger sees just half.)

---

## §33. Operating-procedure deltas (what changes per-ship)

1. **Phase-0.9 verdict step:** after assigning (a)(b)(c)(d) and the INCLUDE/SKIP call, add a one-line **tier tag**: `GOAL-ALIGNED INCLUDE` or `OFF-GOAL CAPTURE [(a)r | ov]` or `SKIP`. Put it in the verdict doc + the project CLAUDE.md + the chapter entry + the shim.
2. **Off-goal captures still get a full wiki** (they're corpus-knowledge — that's the point); they are NOT a lesser build. They simply don't advance the goal-aligned streak and are labeled honestly.
3. **Pilot line:** an OFF-GOAL CAPTURE is by definition NOT a Tier-1 pilot for goal #1 (it failed (b)); say so plainly (it may still be a reference/curiosity).
4. **Audit carry:** the off-goal-capture tally + channel mix is reviewed at each natural audit (goal-drift check).

---

## §34. State after v2.5 codification

| Field | Value |
|---|---|
| Confirmed Patterns | **46** (UNCHANGED) |
| Library-vocab CONFIRMED | **8** (UNCHANGED) |
| Routine version | **v2.5 CURRENT** (supersedes v2.4) |
| Phase-0.9 STRICT criteria | **UNCHANGED** (no redesign — v125 cleared them) |
| Streak (historical, frozen) | **"49+3\*"** through v125 (NOT recomputed) |
| Streak (forward, from v126) | **GA / OG [ov]** 2-tier split (§32) |
| Off-goal-capture lineage (retroactive examples, not re-tagged) | v80 + v123 ((a)-rescue) · v84 + v116 + v122 (override) = 5 |
| v125 §C outlier-track | **ADOPTED 2026-05-30** (operator sign-off; was "pending") |

**Version log:** v2.5 = v2.4 + §31 (corpus-knowledge-outlier 2-tier INCLUDE) + §32 (forward-only streak-split + override-frequency reconciliation) + §33 (per-ship procedure deltas) + §34 (state). v2.3 base + v2.3.1 §25–§26 + v2.4 §27–§30 remain authoritative.

---

## Storm Bear's blunt-and-direct note

This isn't a criteria change — the rubric was right, it correctly flagged every off-goal subject. The change is **honesty in accounting.** For five subjects the corpus quietly counted off-goal captures as wins (the (a)-rescue door) or as flagged-exceptions (the override door) without a single shared label saying "this didn't serve goal #1." v2.5 gives that label, *forward-only*, so the historical "49+3\*" stays as the honest record of how it was counted then, and from v126 the goal-aligned streak measures what it claims to measure. The deliberately-light part: no retroactive rewrite, no punitive override-tightening, and the off-goal capture still gets a full wiki — because capturing notable off-goal repos is a legitimate thing the operator wants; it just shouldn't masquerade as goal progress. The one thing this *doesn't* fix and shouldn't pretend to: the corpus still catalogues faster than it pilots. The accounting now makes that visible instead of hiding it — which is the point.

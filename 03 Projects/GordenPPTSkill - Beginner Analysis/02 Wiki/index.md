# GordenPPTSkill — Wiki (v133)

> `GordenSun/GordenPPTSkill` · **"AI-friendly PPT builder skill: 17 hand-polished Chinese PPTX templates + non-destructive text-only editing tools (python-pptx based). Pick a template, write edits.json, build a real .pptx with the layout intact. Personal/research use only."** · An agentskills.io `SKILL.md` skill that builds/edits PowerPoint decks from built-in Chinese templates.

**(C) Claude-generated wiki page.** Fetched 2026-06-01 (GitHub API + README + recursive tree + SKILL.md + template INDEX). Routine **v2.6, wiki #133**. Phase 0.9: **WEAK INCLUDE → OFF-GOAL CAPTURE via the (a)-rescue channel** (v2.5 §31) — (a) PASS, (b) **FAIL**, (c) MODERATE, (d) MODERATE–STRONG. **The 5th (a)-rescue off-goal capture** (v80 + v123 + v128 + v129 + v133). Built at operator election (eyes-open: flagged off-goal, operator chose "build it anyway"). The §35 ceiling **stays clear** (window → {v131 GA, v132 GA, v133 OG} = 1 OG ≤ 1).

---

## Identity

| Field | Value |
|---|---|
| Repo | [`GordenSun/GordenPPTSkill`](https://github.com/GordenSun/GordenPPTSkill) |
| What | **agentskills.io `SKILL.md` skill** that generates/edits **PowerPoint (.pptx)** decks — pick a built-in Chinese template, write `edits.json`, text-only non-destructive build (layout/color/font preserved) via `python-pptx` |
| Tier / archetype | **T1 Assistant Skill** (content/design-productivity vertical) — agentskills.io implementer; design-skill-cluster adjacency (PPT/deck sub-cluster, cf. v82 huashu-design PPTX, v105 guizang) |
| Stars / forks | **1,311★ / 120 forks** |
| Created / pushed | 2026-05-27 / 2026-06-01 (**~5 days old**) |
| Velocity | **~262★/day over 5 days = sharp nascent pulse** (HIGH-velocity band, but far too young to confirm Pattern #52) |
| License | **Non-commercial / "Other"** — "禁止任何商业用途" (prohibits any commercial use); personal/research only |
| Language | **Python** (the `scripts/`); content = `SKILL.md` + 19 PPTX template binaries |
| Skill name | `gorden-ppt-skill` (bilingual zh+en `description`) |
| Templates | **19 built-in** per SKILL.md + `templates/INDEX.md` (⚠️ GitHub repo description says **17** — minor count-drift); incl. minimal-business-summary, mckinsey-style, data-viz-deck, geometric-summary, architecture-deck, competition-speech, red-patriot-youth (党政红), cute-orange-class — **strongly China-scenario-specific** (work reports, 述职竞聘, 思政课件, 开题答辩) |
| Default branch / homepage | `main` / — |
| Author | **Gorden Sun** (`GordenSun`, `owner.type: User`; Twitter @Gorden_Sun; location undeclared; account 2013, 56 repos, 23 followers) — **inferred China-Mainland** (Chinese templates + Chinese-primary README + name) |

## What it is

A Claude/AI agent **skill** for making PowerPoint decks. Workflow: the agent picks one of **19 hand-polished Chinese PPTX templates** (or the user's own `.pptx`), writes an `edits.json`, and `scripts/build_pptx.py` does a **non-destructive, text-only** rebuild — replacing text without breaking the original layout/colors/font-sizes — with built-in **overflow detection** (text-box capacity) and **same-level-title font-size consistency** checks. Also supports fully original minimal layouts. Repo: `SKILL.md` + `references/{workflow, pptx-edit-schema, chart-editing, custom-template-workflow, original-design-guide}` + `scripts/{build_pptx, apply_update, check_update, build_manifest, compute_capacity, render_slides}` + `templates/` (19 × {template.pptx, detail.json, intro.md, preview.png}) + `manifest.json` + `NOTICE.md` + `VERSION` + `CHANGELOG`. Notable mechanic: on first use the skill instructs the agent to run `python3 scripts/apply_update.py` (a **self-update-on-first-use** step).

## Why it's in the corpus (and why it's OFF-GOAL)

**OFF-GOAL CAPTURE via (a)-rescue** (v2.5 §31 — (b) FAILs, so this is NOT goal-aligned; it enters on (a) alone). Built at explicit operator election after being flagged off-goal.

- **(a) PASS** — inferred China-Mainland cultural-peer (Chinese-first README, Chinese-scenario templates incl. 党政/思政, Chinese author name). China-cluster N+1 (v82/v94/v100/v117/v123/v128/v129/v133).
- **(b) FAIL** — it generates **presentations**, not software / autonomous agents. Zero goal-#1 (software-dev/agent) utility. The skill-authoring-exemplar angle is a (c)/(d) consolation, not goal-relevance. Same shape as the design-skill cluster's weak-(b) members, made explicit under v2.5.
- **(c) MODERATE** — a competently-built agentskills.io skill (clean SKILL.md + references + scripts + manifest + capacity/overflow checks + self-update); a mild skill-structure exemplar, but the domain (PPT-gen) is off corpus-core.
- **(d) MODERATE–STRONG** — agentskills.io 57k chain implementer + design/content-skill-cluster adjacency (esp. v82 huashu-design's PPTX export, v105 guizang social-card) + `NOTICE.md` attribution (cf. v75 impeccable) + Pattern #45 non-commercial-license sub-typology.

**The include rests on (a)+(c)+(d); (b) FAILs — so it's an off-goal capture, not a goal-aligned include.** This is the 5th (a)-rescue off-goal capture (v80 + v123 + v128 + v129 + v133) — the exact intake pattern the v125 and v130 audits flagged as the corpus's dominant drift signal.

## Pattern Library contribution (summary)

**NO Pattern Library state change. ZERO new Library-vocab minted (§28). NO new sub-archetype.** Off-goal captures are corpus-knowledge, not pattern-fuel (the v125/v128/v129 discipline). Observations only, noted not minted:
- **agentskills.io 57k chain — another implementer** (administrative; CONFIRMED N=3 unchanged; exact count still flagged for audit per v115).
- **design/content-skill cluster adjacency** — a PPT/deck-generation skill (cf. v82 huashu-design PPTX export, v105 guizang). Noted, not a mint.
- **Pattern #45 non-commercial license** ("禁止任何商业用途" / "Other") — sub-typology specimen (cf. v69 acceptable-use, v77 CC-NC).
- **`NOTICE.md` attribution** present (cf. v75 impeccable's 2-source NOTICE chain) — noted.
- **Manifest-drift observation** — GitHub description "17 templates" vs SKILL.md + `templates/INDEX.md` "19" (Pattern #81-adjacent; noted, not a clean #81 instance).
- **Self-update-on-first-use** (`apply_update.py`/`check_update.py`) — a mild novel mechanic; noted, NOT minted (off-goal capture).
- **NOT a confirmed Pattern #52** (~262★/day but only 5 days old — sharp nascent pulse, too young; recorded as negative/nascent evidence).
- **China-Mainland cluster N+1.**

**Honest non-claims:** (b) FAILs (this is honestly off-goal, not laundered into goal-aligned); NO new top-level Pattern / sub-archetype / Library-vocab (anti-inflation, per v125 — off-goal subjects don't earn mints); NOT a pilot.

## Pilot

**NOT a pilot.** Corpus-knowledge of a cultural-peer's off-goal skill. (If Storm Bear ever needs Chinese-scenario decks — sprint reports, etc. — it's a low-cost `SKILL.md` to try, but that's incidental, not goal-#1 work; and the license is non-commercial.) The standing goal-#1 move remains piloting one of the three un-piloted goal-aligned subjects (v126 compound-engineering / v131 harness / v132 supermemory).

---

*See `01 Analysis/(C) Phase-0-and-0.9-INCLUDE-verdict.md` and `01 Analysis/(C) Pattern-Library-Phase-4b-off-goal-capture-observation.md`.*

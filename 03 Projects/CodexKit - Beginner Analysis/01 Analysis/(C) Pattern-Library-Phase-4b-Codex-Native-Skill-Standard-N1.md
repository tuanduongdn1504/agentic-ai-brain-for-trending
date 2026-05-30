# (C) Pattern Library — Phase 4b — CodexKit (v121)

**Routine:** v2.4. **Ship:** 2026-05-30. **Net Pattern Library state change: NONE** (46 confirmed / ~25 active / 8 Library-vocab CONFIRMED unchanged). The contribution is **2 NEW Library-vocab standalones (PROVISIONAL N=1)** at the §28 cap, plus cluster filings + administrative strengthening. **No new top-level Pattern; no promotions.**

> **§28 compliance note (the v120-audit lesson):** every observation below that is "filed" is *actually written into* `_patterns/06-library-vocab-registry.md` in this same session — not merely claimed here. Rule 5: "filing is an ACT, not a claim." See registry sections C (two new standalones) and B (LV-C1 / LV-C4 member notes).

---

## PRIMARY — NEW Library-vocab standalone (PROVISIONAL N=1, CORPUS-FIRST)

### "Codex-Native Skill Collection implementing OpenAI's Codex skill spec — a *parallel* skill-authoring standard to agentskills.io"

**The observation.** CodexKit is a library of 90 skills authored in **OpenAI Codex's own skill format**: a `SKILL.md` body + an `agents/openai.yaml` metadata file, discoverable via the **`.agents/skills`** install convention, installed to `~/.agents/skills`. This is the Codex/ChatGPT analogue of what agentskills.io (`SKILL.md` + `.claude/` + `AGENTS.md`, the Pattern #57 57k chain) is for Claude/multi-harness.

**Why it's corpus-first.** The corpus has three prior Codex subjects, but each is a *tool around* Codex, not a skill collection authored *in* its skill format:
- **v62 codex-plugin-cc** — a cross-vendor *bridge* (Codex ↔ Claude Code).
- **v117 CodexPlusPlus** — a Codex *management harness* (config-switching, session mgmt, CDP injection).
- **v112 freellmapi** — a provider *proxy* (OpenAI-compatible aggregation).

None ships a body of skills in the Codex skill spec. CodexKit is the **first observed implementation of the Codex skill-authoring standard as a third-party skill library** — the structural counterpart of the v76→v119 agentskills.io implementer chain, on the *other* standard.

**Why it matters.** It is evidence that the agent-skill ecosystem is **bifurcating into two standards**: agentskills.io (Claude / multi-harness; the 57k chain) and Codex-native (`agents/openai.yaml`; Codex / ChatGPT). The corpus has tracked the agentskills.io side intensively; this is the first data point on the *parallel* side authored as a skill collection. Tracking the split is genuinely useful for the corpus's "skill standard" understanding.

**Honest scoping.** Deliberately **NOT** registered as a Pattern #57 57k implementer — 57k is specifically the *agentskills.io* conformance chain; counting a competing standard in it would corrupt that chain's meaning. This is a *sibling* standard, registered as its own Library-vocab item. PROVISIONAL N=1; promotion-eligible at N=2 (a 2nd Codex-native skill collection) — at which point a "Codex-native skill standard" sub-claim could form, parallel to 57k.

**Filed:** `_patterns/06-library-vocab-registry.md` section C (live standalone).

---

## SECONDARY — NEW Library-vocab standalone (PROVISIONAL N=1)

### "Multi-Domain (Cross-Functional) Skill Collection" — vs the single-vertical Domain-Vertical archetype

**The observation.** The corpus's **T1 Domain-Vertical-Skill-Collection** (CONFIRMED N=4: v64 SEO / v90 academic / v98 cybersecurity / v119 nature) is defined by **one** vertical per bundle. CodexKit inverts that: **one bundle spanning 15 work domains × 90 skills** (engineering + project management + finance + legal + HR + ops + strategy + analytics + marketing + sales + CX + founder workflows + …). It is a *cross-functional / horizontal* skill OS rather than a vertical specialist.

**Why register it.** This is a genuine structural contrast at the tier-sub-archetype layer, not a restatement of the confirmed single-vertical archetype. If a 2nd multi-domain (horizontal) skill collection appears, this becomes an N=2 sibling sub-archetype to the single-vertical one — a real fork in the T1 skill-collection taxonomy worth naming early.

**Honest scoping.** PROVISIONAL N=1; tracked at the Library-vocab layer (registry section C) for visibility, structurally a tier-sub-archetype observation. It does **not** change the CONFIRMED Domain-Vertical N=4 count (that count is about single-vertical bundles; CodexKit is the contrast case, not a 5th single-vertical instance).

**Filed:** `_patterns/06-library-vocab-registry.md` section C (live standalone).

*(These two standalones = exactly the §28 rule-2 cap of ≤2 genuinely-new standalones per wiki. Everything below joins a cluster or is administrative — no further minting.)*

---

## Cluster filings (no new mint — §28 rule 5 "clustering-first")

- **LV-C4 (Cadence / Velocity micro-signals)** ← **high fork_ratio 0.526 at micro-scale with *sustained* development.** 19★ / 10 forks is an exceptionally high fork-ratio (cf. VN cluster v76 0.296 / v79 0.484 / v80 0.765), BUT — unlike the #17 "Try-Once-and-Move-On" CONFIRMED profile — CodexKit shows **sustained dev** (8 releases, v0.10.0, 7 open issues, recent push). So this is a *distinct* micro-signal: high-deployment-intent + active maintenance at micro-star-scale. Filed as an LV-C4 member note (explicitly NOT a clean #17 Try-Once instance).
- **LV-C1 (Vendor-Direct Skill-Authoring & Distribution)** ← the **5-Layer Framework + 4C verification gates + 3-tier structure** authoring methodology, filed as an *adjacent* member (third-party author, not vendor-direct — noted as such, so it doesn't inflate the (a)-7-sister framing).

## Administrative strengthening (no mint)

- **Pattern #19 "VN-Community Multi-Profile-Type" (CONFIRMED N=5)** — CodexKit adds a **VN-solo prolific-builder** data point (236 public repos). Administrative only; no count change at the Library-vocab layer.
- **Codex-tool cluster** (v62 + v117 + CodexKit) — the cluster now has a bridge + a management harness + a skill collection.
- **MIT clean** (LICENSE + GitHub API agree).

## Negative evidence

- **NOT a Pattern #52 instance** — ~0.27 stars/day is far below every velocity sub-class floor. Recording the negative case (a micro-scale, non-viral subject) keeps Pattern #52's sub-class boundaries honest.

---

## Honest non-claims (load-bearing)

1. **NOT in the agentskills.io 57k chain** — Codex's competing standard, deliberately excluded so the 57k chain stays meaningful.
2. **(b) is WEAK, not MODERATE** — Codex-only (no Claude) + business-ops (not software-dev). No laundering on skill-authoring-reference grounds.
3. **(a) is inferred, not declared** — strong evidence (VN name + shipped VN quick-guide) but the profile declares no location.
4. **NO new top-level Pattern, NO promotion** — the PRIMARY is a Library-vocab N=1; the corpus stays at 46 confirmed.
5. **Exactly 2 new standalones** (the §28 cap) — everything else cluster-filed or administrative.
6. **Filing is done, not claimed** — the registry was actually edited this session (the v120-audit §28 rule-5 lesson).

**Storm Bear's blunt take.** A clean, honest STRONG INCLUDE 3/4 that earns its place on (a)(c)(d) while (b) genuinely WEAK keeps it off any pilot list — this is a *Codex* business-ops kit, and you run Claude on software/Scrum work, so it's a read-the-architecture subject, not an install. The one genuinely new corpus contribution is the **Codex-native skill standard as a parallel to agentskills.io**: the corpus has tracked the Claude/agentskills.io skill standard hard, and this is the first time the *other* standard shows up as an actual skill library — a fork in the ecosystem worth naming at N=1. The multi-domain-vs-single-vertical contrast is a smaller but real second item. No promotions, no top-level pattern, and the registry was actually edited this time — which, per the v120 audit, is the part that's been slipping.

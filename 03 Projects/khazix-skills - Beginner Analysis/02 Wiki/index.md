# khazix-skills — wiki (v138)

> **(C) AI-generated wiki page.** Subject: [`KKKKhazix/khazix-skills`](https://github.com/KKKKhazix/khazix-skills). Built 2026-06-02 under LLM Wiki Routine v2.6.
> ⚠️ Metadata caveat (§37): this sandbox mocks the GitHub API, so stars / forks / created_at are **not API-verified** — figures below are from the repo page + README + the gh-api mock, flagged where approximate.

## Identity

| Field | Value |
|---|---|
| Repo | `KKKKhazix/khazix-skills` |
| Tagline | **"A few AI skills I actually use every day, open-sourced as-is."** |
| Author | **数字生命卡兹克 / "Digital Life Kha'Zix"** (`KKKKhazix`) — a notable Chinese AI content creator; each skill links a companion WeChat article |
| Tier | **T1 Assistant Skill** — a personal, multi-harness, agentskills.io-standard **collection of 5 skills** |
| License | MIT |
| Language | Python 52.8% / HTML 47.2% |
| Stars | ≈ **12.8k** / 1.7k forks / 65 watchers / 27 open issues — *stated, NOT API-verified* (§37.4) |
| Created | ~**2026-04-06** (~2 months) — *NOT API-verified*; ~225★/day if accurate, **no #52 claim** |
| Verdict | **GOAL-ALIGNED INCLUDE 4/4** — (a) PASS + (b) **MODERATE** + (c) STRONG + (d) STRONG |

## What it is

A bilingual (zh + en), **agentskills.io-standard** collection of **5 AI agent skills the creator personally uses daily**, packaged for 8 harnesses (Claude Code / Codex / OpenCode / OpenClaw / Cursor / Gemini CLI / Cline / Windsurf). Install via natural language — *"Install this skill: https://github.com/KKKKhazix/khazix-skills/tree/main/&lt;skill-name&gt;"* → the agent clones it into the right directory. Each skill = `SKILL.md` + `references/` (+ `scripts/`/`assets/` where needed).

| Skill | What it does |
|---|---|
| 🧹 **neat-freak** | `/neat` reconciles project docs + **CLAUDE.md** + **agent memory** with the code after a session (3-layer sync) |
| 🔭 **hv-analysis** | product/company/concept → 10k–30k-word PDF research report (horizontal/vertical methodology; `md_to_pdf.py` + schema.json) |
| ✍️ **khazix-writer** | agent writes long-form Chinese in the creator's personal voice/style (content_methodology.md + style_examples.md) |
| 🔥 **aihot** | pull AI HOT's daily AI-news report from aihot.virxact.com, one sentence, no API key |
| 💽 **storage-analyzer** | scan Mac/Windows disk → three-tier cleanup plan + browser one-click trash (read-only scan + confirmation UI; scan.py/server.py/build_report.py + HTML report) |

## Why it's in the corpus

- **(a)** PASS — inferred **China-Mainland** cultural-peer (Simplified-Chinese profile, 数字生命卡兹克, WeChat-article funnel, `wechat-article-exporter` sibling repo). Confidence medium-high; established China-Mainland cluster.
- **(b)** **MODERATE (load-bearing)** — an agentskills.io-standard multi-harness skill *collection* (skill-authoring-exemplar value) + **neat-freak** is a genuine goal-#1/vault-relevant dev-workflow skill. **MODERATE not STRONG**: an influencer's personal grab-bag (4 of 5 skills off the software-dev core). **MODERATE not FAIL (vs v133 GordenPPTSkill):** neat-freak is a real agent-workflow skill + the repo is a studyable SKILL.md-collection — recorded so the next audit can challenge it.
- **(c)** STRONG — clean per-skill structure (SKILL.md + references/ + scripts/ + assets/), bilingual, multi-harness; storage-analyzer is a genuinely well-built skill.
- **(d)** STRONG — multi-skill-collection siblings (v81/v121/v124/v119/v98/v90/v64) + agentskills.io standard + Pattern #84 8-harness + neat-freak echoes the vault's own CLAUDE.md/memory-sync discipline + khazix-writer strengthens v108 voice-calibration + Chinese-AI-KOL author thread (v82 花叔 / v105 歸藏).

## Pattern Library contribution (Phase 4b)

- **PRIMARY:** NEW Library-vocab standalone FILED to registry 06 §C — **"Personal Daily-Driver Skill Collection (creator-curated, eclectic)"** N=1 CORPUS-FIRST ("skills I personally use every day, open-sourced as-is"; distinct from the single-domain T1 Domain-Vertical collection and from v121 CodexKit's cross-functional business-ops matrix; promotion-eligible at N=2).
- **SECONDARY (instance notes / strengthening):** **"voice-calibration personalization" RE-REGISTERED → N=2** (v108 humanizer de-AI-voice + v138 khazix-writer reproduce-specific-voice; a strengthening, not a new mint) · Pattern #84 84c multi-harness N+1 (8 harnesses) · Pattern #57 agentskills.io-standard conformance N+1 (modest; **NOT** an `npx skills add` 57k-CLI implementer — clone + ClawHub/Tessl) · neat-freak = vault-state-sync corpus-recursive (OBSERVATION, not minted) · Pattern #19 Chinese-AI-KOL + WeChat-funnel sub-mechanism (v82/v105/v138; observation) · Pattern #82 quantitative-marketing (mild) · China-Mainland cluster N+1.
- **State change: NONE** (46 confirmed / 8 Library-vocab CONFIRMED). §28 new-standalone count = 1 (≤2). NO top-level pattern, NO tier sub-archetype. **NOT a Pattern #52 promotion** (velocity unverified + <90d). **NOT an agentskills.io 57k implementer**.

## §35 / streak

- §35 ceiling **STAYS CLEAR** — window {v136 GA, v137 GA, v138 GA} = 0 OG. No override. Consecutive-GA run v134→v138 = 5.
- Streak: **`GA:7 · OG:4 [1 ov]` → `GA:8 · OG:4 [1 ov]`** ("49+3\*" frozen @v125). v138 = 8th GOAL-ALIGNED PASS.

## Pilot note

**Tier-1 PILOTABLE — and `neat-freak` is the directly-vault-useful one** (continuing the v137 "actually pilot something" thread). `/neat`'s 3-layer reconcile (docs + CLAUDE.md + agent memory ↔ code) is precisely the manual sync this routine performs on every wiki ship — so it's worth a real trial *on this vault's workflow*.

- **Reversible trial:** install neat-freak alone (*"Install this skill: …/tree/main/neat-freak"*), run `/neat` on a scratch repo (or a copy of this vault), inspect what it reconciles, delete if unwanted.
- **`install-snapshot` recommended** — the skills carry Python scripts; storage-analyzer spins up a local browser server.
- **Study angle even if you don't keep it:** the per-skill structure (SKILL.md + references/ + scripts/ + assets/) is a clean model for a personal multi-skill collection — and neat-freak's `sync-matrix.md` is worth reading against this vault's own CLAUDE.md-sync discipline.
- Not a daily-driver beyond neat-freak: hv-analysis/khazix-writer/aihot/storage-analyzer are content/utility skills off the software-dev core.

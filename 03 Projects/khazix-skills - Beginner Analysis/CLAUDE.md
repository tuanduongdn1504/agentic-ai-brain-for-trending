# khazix-skills — project context (v138)

**(C) AI-generated project folder.** Subject: [`KKKKhazix/khazix-skills`](https://github.com/KKKKhazix/khazix-skills). Wiki #138, built 2026-06-02 under LLM Wiki Routine v2.6. Shipped on branch `wiki/v138-khazix-skills` (stacked on the still-unmerged `wiki/v137-book-to-skill`).

## One-liner
"A few AI skills I actually use every day, open-sourced as-is." A bilingual (zh + en), **agentskills.io-standard, multi-harness** (Claude Code / Codex / OpenCode / OpenClaw / Cursor / Gemini CLI / Cline / Windsurf) collection of **5 personal daily-driver skills** by **数字生命卡兹克 / "Digital Life Kha'Zix"** (`KKKKhazix`, a notable Chinese AI content creator; each skill links a companion WeChat article). MIT. Python 52.8% / HTML 47.2%. ≈12.8k★ (NOT API-verified).

## The 5 skills
1. **neat-freak** — `/neat` reconciles project docs + **CLAUDE.md** + **agent memory** with the code after a session (3-layer sync). *← the genuinely goal-#1 + directly-vault-applicable one; it's this vault's own state-maintenance discipline, productized.*
2. **hv-analysis** — drop in a product/company/concept → 10k–30k-word PDF research report (horizontal/vertical methodology; `md_to_pdf.py` + schema.json).
3. **khazix-writer** — makes the agent write long-form Chinese in the creator's personal voice/style (references: content_methodology.md + style_examples.md).
4. **aihot** — pull daily AI news from aihot.virxact.com with one sentence, no API key.
5. **storage-analyzer** — scan Mac/Windows disk → three-tier cleanup plan + browser one-click trash (scan.py + server.py + build_report.py + HTML report).

## Why it's here (and the honest calibration)
- **(b) MODERATE, load-bearing call:** it's an agentskills.io-standard multi-harness skill *collection* (skill-authoring-exemplar value) AND **neat-freak** is a real goal-#1/vault-relevant dev-workflow skill. Held at **MODERATE not STRONG** because the collection as a whole is an **influencer's personal grab-bag** (research-report / writing-voice / AI-news / disk-cleanup dominate; only 1 of 5 is genuinely software-dev). **The load-bearing reason it's MODERATE not FAIL (vs v133 GordenPPTSkill (b)-FAIL): neat-freak is a genuine agent-workflow dev skill + the whole repo is a studyable SKILL.md-collection exemplar** — recorded so the next audit can challenge it, not laundered.
- **(a) PASS:** inferred China-Mainland cultural-peer (Simplified-Chinese profile, 数字生命卡兹克, WeChat-article funnel, China-specific tooling) — confidence medium-high (§37 `speculation/medium`). The established China-Mainland cluster.

## Verdict + Pattern Library impact
- **GOAL-ALIGNED INCLUDE 4/4** — (a) PASS + (b) MODERATE + (c) STRONG + (d) STRONG. (Same shape as v135 open-slide.)
- **PRIMARY:** NEW Library-vocab standalone FILED to registry 06 §C — **"Personal Daily-Driver Skill Collection (creator-curated, eclectic)"** N=1 CORPUS-FIRST ("skills I personally use every day, open-sourced as-is"; distinct from the T1 Domain-Vertical single-domain collection [v64/v90/v98/v119/v124] and from v121 CodexKit's Multi-Domain *Cross-Functional* business-ops matrix; promotion-eligible at N=2).
- **SECONDARY (instance notes / strengthening):** **"voice-calibration personalization" RE-REGISTERED → N=2** (v108 humanizer + v138 khazix-writer; the v108 standalone auto-retired ~v123, §28-re-registered on this genuine 2nd — a strengthening, not a new mint) · Pattern #84 84c multi-harness N+1 (8 harnesses) · Pattern #57 agentskills.io-standard conformance N+1 (modest — **NOT** an `npx skills add` 57k-CLI implementer; installs via natural-language clone + ClawHub/Tessl) · neat-freak = vault-state-sync corpus-recursive observation (3-layer doc/CLAUDE.md/memory sync = the vault's own discipline; OBSERVATION, NOT minted) · Pattern #19 Chinese-AI-KOL-with-personal-brand + WeChat-content-funnel sub-mechanism (v82 花叔 / v105 歸藏 / v138; OBSERVATION) · Pattern #82 quantitative-marketing (badges, WeChat funnel) · China-Mainland cluster N+1.
- **NO Pattern Library state change** (46 confirmed / 8 Library-vocab CONFIRMED). NO new top-level pattern. NO new tier sub-archetype. §28 new-standalone count = 1 (≤2; the voice-calibration N=2 is a re-registration/strengthening, not a new standalone). **NOT a Pattern #52 promotion** (velocity ~225★/day strong but <90d pulse AND NOT API-verified). **NOT an agentskills.io 57k `npx skills add` implementer**.

## §35 / streak
- §35 **STAYS CLEAR** — window {v136 GA, v137 GA, v138 GA} = 0 OG. No override. Consecutive-GA run v134→v138 = 5.
- Streak (v2.6 §32): **`GA:7 · OG:4 [1 ov]` → `GA:8 · OG:4 [1 ov]`** ("49+3\*" frozen @v125). v138 = 8th GOAL-ALIGNED PASS.

## Pilot
**Tier-1 PILOTABLE — and `neat-freak` is the directly-vault-useful one** (continues the v137 "finally pilot something" thread). `/neat` reconciles docs + CLAUDE.md + agent memory with code after a session — which is *exactly* the manual CLAUDE.md-sync this routine does on every wiki ship. Reversible: install neat-freak alone (`Install this skill: …/tree/main/neat-freak`), run `/neat` on a scratch repo, inspect, delete. `install-snapshot` recommended (skills carry Python scripts; storage-analyzer runs a local server). Study angle: how a 5-skill personal collection is structured (SKILL.md + references/ + scripts/ + assets/ per skill) is a clean model to borrow.

## Files
- `01 Analysis/(C) Phase-0-and-0.9-INCLUDE-verdict.md` — the gate.
- `01 Analysis/(C) Pattern-Library-Phase-4b.md` — PRIMARY + secondaries + honest non-claims.
- `02 Wiki/index.md` — the wiki page.

## Data caveat (§37)
Sandbox mocks the GitHub API → stars/forks/created_at NOT API-verified. Figures (≈12.8k★ / 1.7k forks / 65 watchers; created ~2026-04-06; MIT; Python+HTML) are from the repo page + README + the gh-api mock, flagged `stated, NOT API-verified` (§37.4). ~225★/day if accurate; no Pattern #52 claim (velocity unverified + <90d).

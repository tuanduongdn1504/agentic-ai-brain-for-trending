# scientific-agent-skills — Wiki (v124)

> `K-Dense-AI/scientific-agent-skills` · **"Turn any AI agent into an AI Scientist."** · An open **agentskills.io-standard scientific skill library** — 141/142 `SKILL.md` skills across 17 research domains + 78–100+ scientific databases — installable into Claude Code, Cursor, Codex, Google Antigravity, Gemini CLI, and Claude Cowork. Renamed from **"Claude Scientific Skills"** when it broadened from Claude-only to the open Agent Skills standard.

**(C) Claude-generated wiki page.** Fetched 2026-05-30 (GitHub API + README + org page + root-contents listing). Routine v2.4, wiki #124. **STRONG INCLUDE 3/4** ((c)(d) STRONG, (b) MODERATE, (a) FAIL US-commercial-org) — the first clearly-in-scope subject of the post-v120 window. ⚠️ **v125 is now a HARD audit** (mandated Phase-0.9 override-review + "(a)-rescue N=2" + natural cadence). See `01 Analysis/`.

---

## Identity

| Field | Value |
|---|---|
| Repo | [`K-Dense-AI/scientific-agent-skills`](https://github.com/K-Dense-AI/scientific-agent-skills) |
| What | **agentskills.io-standard scientific skill library** (141 SKILL.md skills + 100+ databases) |
| Tier / archetype | **T1 Assistant Skill / Domain-Vertical-Skill-Collection** (scientific-research vertical) — CONFIRMED archetype, this = **N=5** + largest-scale instance |
| Stars / forks | **26,567★ / 2,750 forks** (fork_ratio 0.10) — mega-scale |
| Watchers / open issues | 132 subscribers / 23 open |
| Created / pushed | 2025-10-19 / 2026-05-28 (**~223 days** old); **83 releases**, v2.45.0 |
| Velocity | **~119 stars/day → Pattern #52 SUSTAINED-MODERATE-HIGH** (25–150/d, upper end), sustained ~223 days |
| License | **MIT** (per-skill licenses may vary in each `SKILL.md`) |
| Language | **Python 75.4%** + **TeX 16.7%** (scientific/LaTeX) + HTML + Shell; `uv`, Python 3.13+ tooling |
| Install | `npx skills add K-Dense-AI/scientific-agent-skills` · `gh skill install …` |
| Harnesses | Claude Code · Cursor · Codex · Google Antigravity · Gemini CLI · **Claude Cowork** |
| Author | **K-Dense Inc.** ("K-Dense AI"; `owner.type: Organization`) — **US** commercial AI-science startup; bio "A world leader in empowering scientists with AI agentic tools"; hosted platform "K-Dense Web" + free OSS desktop "K-Dense BYOK" + repos `karpathy` / `agentic-data-scientist` |
| Topics | agent-skills, ai-scientist, bioinformatics, chemoinformatics, **claude**, **claude-skills**, **claudecode**, drug-discovery, genomics, proteomics, materials-science, scientific-computing |

## What it is

A large, standards-based **skill library that turns an AI coding agent into a research assistant** ("AI Scientist"). You install it with one command and your agent gains 141 ready-to-use `SKILL.md` skills spanning 17 domains — **🧬 Bioinformatics & Genomics (23)**, **🧪 Cheminformatics & Drug Discovery (10)**, **🏥 Clinical Research (8)**, **📊 Data Analysis & Visualization (19)**, **🤖 ML & AI (14)**, **📚 Scientific Communication (27)**, plus proteomics, neuroscience, materials, lab automation, multi-omics, protein engineering, research methodology, and regulatory — and a unified **database-lookup skill** reaching 78–100+ scientific databases.

It is **fully agentskills.io-compliant** (every skill is a spec-valid `SKILL.md` with versioned frontmatter), **vendor-neutral** (6 harnesses), and **security-conscious**: skills are scanned weekly by an **LLM-based Cisco AI Defense Skill Scanner**, with results published in a 518 KB `SECURITY.md`. The same library is the foundation for **K-Dense BYOK**, a free open-source desktop "AI co-scientist" (bring your own keys, 40+ models, optional Modal cloud scaling).

This is the corpus's bread-and-butter archetype — a **Domain-Vertical-Skill-Collection** — and unlike the prior two builds (v122 dograh voice-AI override; v123 MoneyPrinterTurbo faceless-video (a)-rescue), it's squarely on the agent-skills axis the corpus tracks.

## Why it's in the corpus — STRONG INCLUDE 3/4

- **(a) FAIL** — K-Dense Inc. is a US commercial AI-science startup, not a cultural-peer and not a foundational vendor the vault depends on (a third-party skill author, like v114 GreenSock).
- **(b) MODERATE** — the scientific domain is off Storm Bear's software-dev/Scrum vertical (near-zero as *daily tools*), but it's a Claude-Code agentskills.io library and a genuine **skill-authoring exemplar** for goal #1 (how to structure, spec-enforce, version, security-scan, and distribute a 141-skill library). Mirrors v119 nature-skills exactly.
- **(c) STRONG** — one of the largest, most mature domain libraries in the corpus: 141 skills × 17 domains + 100+ DBs + published weekly security-scanning + spec-compliance enforcement (`scan_skills.py`, CONTRIBUTING).
- **(d) STRONG** — agentskills.io 57k chain **12th implementer**; **T1 Domain-Vertical-Skill-Collection → N=5**; direct **v119 nature-skills sibling**; 6-harness (incl. Claude Cowork); Pattern #66 skill-security-scanning; and a corpus-recursive **Karpathy-echo** (K-Dense's `karpathy` repo).

## Pattern Library contribution (no state change)

- **PRIMARY:** **T1 Domain-Vertical-Skill-Collection → N=5** (scientific vertical; v64/v90/v98/v119/v124) — administrative strengthening of a CONFIRMED archetype; largest-scale instance.
- **SECONDARY:** agentskills.io 57k **12th implementer** + Claude→open-standard broadening; **Pattern #66 published skill-security-scanning N=2** (with v76); Pattern #84 6-harness; Pattern #82 dense quantitative-marketing; Pattern #81/LV-C3 *weak* skill-count-drift member (141/142); Karpathy-echo; v119 sibling.
- **§28:** ZERO new Library-vocab standalones; 2 cluster-filings actually written to the registry (LV-C1 commercial-OSS-library-as-funnel; LV-C3 weak drift member). State UNCHANGED. Streak "48+3\*" → "49+3\*".

## Honest non-claims

- **NO** new top-level Pattern; T1 N=5 is administrative (CONFIRMED since v101).
- Skill-security-scanning is a Pattern #66 **N=2 strengthening, NOT corpus-first** (v76 had injection-scanning first).
- The 141/142 drift is a **weak** LV-C3 member, **not** a clean Pattern #81 N=3.
- (a) **FAILs** honestly; the INCLUDE is 3/4 on (b)(c)(d), not inflated; **conditional/reference pilot**, not a daily-use tool.

---

*See `01 Analysis/(C) Phase-0-and-0.9-INCLUDE-verdict.md` for the full gate decision + the v125-hard-audit flag, and `01 Analysis/(C) Pattern-Library-Phase-4b-T1-Domain-Vertical-Skill-Collection-N5.md` for the PRIMARY + the §28 registry filings.*

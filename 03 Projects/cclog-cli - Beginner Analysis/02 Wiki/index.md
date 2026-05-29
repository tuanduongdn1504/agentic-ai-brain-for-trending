# cclog-cli — Wiki (v109)

> *"cclog-cli tracks Claude Code usage, including tokens, requests, and responses. It provides history and analytics to help debug workflows, monitor costs, and optimize performance by making AI interactions transparent."*

## 1. Identity & metadata

| Field | Value |
|---|---|
| Repo | `thanhquangqb95/cclog-cli` |
| Author | **Lê Thanh Quảng (@thanhquangqb95)** — location **"Việt Nam"** (explicit); bio "dev"; gmail thanhquangqb95@gmail.com; Facebook lethanhquangqb1995; GitHub since 2016; 2 followers / 11 public repos. ("qb" ≈ Quảng Bình; "95"/1995 birth year.) |
| Tier / archetype | **T2 Service** / "AI-Agent Observability/Metering Tool" sub-archetype (N=2 with v89 VibeCodingTracker) |
| License | **MIT declared in `package.json`** but **no LICENSE file** (GitHub API `license: null`; `/contents/LICENSE` → 404) = Pattern #83 83f.4 declared-but-no-file |
| Primary language | TypeScript ~98% (+ React dashboard via Vite, Express server, Node ESM) |
| Stars / forks | **3 ★ / 0 forks / 0 subscribers / 0 open issues** — micro-scale, essentially undiscovered |
| Created / pushed | 2026-04-11 / 2026-04-19 (~48 days; ~8-day active window) |
| Velocity | **~0.06 stars/day** — NOT a Pattern #52 instance (far below all sub-class floors) |
| Versioning | `package.json` v1.2.1; CHANGELOG.md; ~6 git tags / 22 commits (GitHub releases endpoint = 0; tags ≠ releases) |
| Default branch | `main` · topics: claude, claude-code, cli-tool, dashboard, tracking |

## 2. What it does

A **local-first, read-only** tool that parses Claude Code session logs from `~/.claude/projects/` and surfaces usage analytics:

- **Session analysis** — input / output / total / cache tokens per session.
- **Project summaries** + per-project breakdowns + daily token trends + subagent details + session ranking.
- **Cost estimation** — bundled pricing snapshots (`data/`), optional live refresh via `pricepertoken.com`.
- **Two surfaces** — terminal summary/ranked-list (CLI) + Express + React web dashboard (`cclog-cli run`).
- **Export** — JSON / CSV.
- **Read-only** — never modifies source log files.

**Install:** `npm i -g cclog-cli` (Node 18+). Cross-platform (Node).

## 3. Architecture

```
cclog-cli/
├── src/         ← TypeScript CLI source (log parser + analytics + cost estimator)
├── web/         ← React dashboard (Vite)
├── data/        ← bundled pricing snapshots
├── scripts/     ← build/release
├── assets/      ← dashboard screenshots
├── package.json (license MIT, bin: cclog-cli, v1.2.1) · tsconfig.json · CHANGELOG.md
├── README.md · logo.png · .gitignore · .repomixignore
└── (no LICENSE file)
```

## 4. Corpus position (cross-references)

- **T2 "AI-Agent Observability/Metering Tool" sub-archetype N=2 STRENGTHENING (PRIMARY)** — direct sibling to [[v89 VibeCodingTracker]] (the PROVISIONAL N=1 anchor). Same archetype (parse agent logs → token/cost/session analytics, read-only), **distinct implementations**: v89 = Rust CLI + multi-registry + LiteLLM cost-attribution; v109 = TypeScript + React dashboard + `pricepertoken.com` cost-refresh. → cross-instance spread; PROMOTION-ELIGIBLE-toward-CONFIRMED at N=3.
- **VN-LOCATED cluster extension** — Lê Thanh Quảng (Việt Nam) joins [[v76 agent-skills-standard]] (Hanoi) + [[v80 SmartMacroAI]] (VN) + [[v85 ui-ux-pro-max]] (VN-org) + [[v87 claude-comstyle]] (VN-solo) + [[v88 teleport]] (Hanoi). Pattern #19 "VN-Community Multi-Profile-Type" (CONFIRMED N=5 at v90) N+1 — adds a "VN-solo-dev observability-tool" profile.
- **Pattern #83 83f.4 "declared-but-no-LICENSE-file" N+1** — `package.json` MIT, no LICENSE file (v79 autoresearch anchor; v109 = package.json-MIT variant).
- **Cost-attribution via external pricing service** (`pricepertoken.com`) — distinct from v89's LiteLLM fuzzy-model-matching; Library-vocab candidate.
- **Claude Code v65** = the log source consumed.
- **Micro-scale-tolerant filter validation** — at 3 stars, this is among the lowest-profile subjects in the v60+ window; INCLUDE rests on cultural-peer + functional-fit + archetype, not popularity (density-not-scale-dependent, validated v90 audit).

## 5. Functional fit / pilot relevance

**HIGH — Tier-1 actionable.** Storm Bear runs Claude Code *intensively* (100+ wikis in ~6 months; this session alone shipped v105–v109). cclog-cli surfaces exactly the token/cost/session analytics for that load — the same value-prop that made v89 a pilot candidate, but with a friendlier install (`npm i -g`) + web dashboard. Cost-of-trial LOW, reversible (`npm uninstall -g cclog-cli`). Sits with claude-mem v103 (memory) / claude-code-harness v107 (process) / humanizer v108 (de-slop) as a usage/cost-observability pilot.

## 6. Honest caveats

- **3 stars = essentially undiscovered.** No corpus-influence claim; this is an archetype-confirmation + cultural-peer + personal-utility INCLUDE, not a methodology-influence node.
- **No CORPUS-FIRST node** — a smaller, less-novel implementation of the v89 archetype.
- **License gap** — MIT declared in `package.json` only; no LICENSE file (a real, if minor, OSS hygiene gap).
- **Not a Claude Code skill/plugin itself** — a standalone CLI that *consumes* Claude Code artifacts; no SKILL.md / AGENTS.md / agentskills.io.

## Sources
- [thanhquangqb95/cclog-cli · GitHub](https://github.com/thanhquangqb95/cclog-cli)
- [Lê Thanh Quảng (@thanhquangqb95) · GitHub profile](https://github.com/thanhquangqb95)

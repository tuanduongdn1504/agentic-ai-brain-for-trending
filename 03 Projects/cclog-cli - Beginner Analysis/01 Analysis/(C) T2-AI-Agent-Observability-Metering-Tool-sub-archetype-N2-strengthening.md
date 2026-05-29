# (C) Phase 4b PRIMARY — T2 sub-archetype "AI-Agent Observability/Metering Tool" N=2 STRENGTHENING

**Vehicle:** routine v2.3 §3 Phase 4b — sub-archetype strengthening (PROVISIONAL N=1 → N=2).
**Confidence:** HIGH.
**Subject:** v109 `thanhquangqb95/cclog-cli`.

## The observation

The T2 Service sub-archetype **"AI-Agent Observability/Metering Tool"** was registered PROVISIONAL N=1 at v89 (`Mai0313/VibeCodingTracker`). v109 cclog-cli is a clean **N=2** instance — same archetype, distinct implementation.

| Axis | v89 VibeCodingTracker (N=1 anchor) | v109 cclog-cli (N=2) |
|---|---|---|
| Function | Parse AI-coding-assistant logs → token/cost/usage analytics | Parse Claude Code logs (`~/.claude/projects/`) → token/cost/session analytics |
| Mode | Read-only observability | Read-only (never modifies source files) |
| Language | **Rust** (97.1%) | **TypeScript** (~98%) + React dashboard |
| Surface | CLI | CLI + Express/React web dashboard |
| Distribution | Multi-registry (npm ×2 + PyPI + Cargo + Docker) | Single npm (`npm i -g cclog-cli`) |
| Cost-attribution | LiteLLM fuzzy-model-matching | Bundled pricing snapshots + `pricepertoken.com` live-refresh |
| Scale | Micro (8★) | Micro (3★) |

The **distinct implementations at the same archetype** (Rust-CLI-multi-registry vs TypeScript-React-dashboard; LiteLLM vs external-pricing-service) give genuine cross-instance spread — the archetype is defined by *what it does* (read-only agent-log → usage/cost analytics), not by stack.

## Proposed action
- **N=2 STRENGTHENING** registered at v109. Sub-archetype stays PROVISIONAL.
- **PROMOTION-ELIGIBLE-toward-CONFIRMED at N=3** — watch for a third agent-observability/metering tool.
- Cross-instance spread already strong (2 languages, 2 cost-attribution mechanisms, 2 surfaces) — a clean N=3 would support CONFIRMED.

## SECONDARY observations (held at OC layer per cascade-discipline)

1. **VN-LOCATED cluster extension** — Lê Thanh Quảng (Việt Nam) extends the VN sub-cluster (v76 Hanoi + v80 VN + v85 VN-org + v87 VN-solo + v88 Hanoi). Pattern #19 "VN-Community Multi-Profile-Type" (CONFIRMED N=5 at v90) N+1 — adds a "VN-solo-dev observability-tool" profile-type.
2. **Pattern #83 83f.4 "declared-but-no-LICENSE-file" N+1** — `package.json` declares `"license": "MIT"` but there is no LICENSE file (`/contents/LICENSE` → 404; GitHub API `license: null`). v79 autoresearch was the 83f.4 anchor (README-declared); v109 = package.json-declared variant.
3. **Cost-attribution via external pricing service** (`pricepertoken.com` live-refresh + bundled snapshots) — distinct mechanism from v89's LiteLLM fuzzy-model-matching; Library-vocab candidate "Cost-Attribution via External Pricing Service."
4. **Micro-scale-tolerant filter validation** — at 3 stars (among the lowest in the v60+ window), the INCLUDE rests on archetype + cultural-peer + functional-fit, not popularity (density-not-scale-dependent, validated v90 audit).
5. **NOT a Pattern #52 instance** — ~0.06 stars/day.
6. **`.repomixignore`** — repomix (repo-to-LLM-context) artifact note.

## Honest non-claims
- **No new top-level pattern** — N=2 strengthening of an existing PROVISIONAL sub-archetype.
- **No CORPUS-FIRST node** — v109 is a smaller, less-novel implementation than v89.
- **agentskills.io / SKILL.md / AGENTS.md** — none; cclog-cli *consumes* Claude Code artifacts, is not a skill itself. NOT in the Pattern #57 57k chain.

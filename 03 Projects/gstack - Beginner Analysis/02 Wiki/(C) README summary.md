# (C) README Summary

> **Source:** `00 Sources/gstack/README.md` (411 lines, ~16KB)
> **Ingested:** 2026-04-18
> **Coverage:** Full file
> **Routine context:** Source #1 of 3 cho gstack project (Phase 2)

---

## TL;DR

**VI:** gstack là **slash-command framework** cho Claude Code (+ 9 harness khác) do **Garry Tan (President & CEO của Y Combinator)** build và open-source. Concept cốt lõi: biến Claude Code thành **"virtual engineering team"** — 23 specialists (CEO, eng manager, designer, reviewer, QA lead, security officer, release engineer, ...) + 8 power tools, tất cả là slash commands trong Markdown. Claim đáng chú ý: Garry ship **600,000+ LOC trong 60 ngày** part-time bằng tool này.

**EN:** gstack is a slash-command framework for Claude Code (+ 9 other AI agents). By Garry Tan (President & CEO of Y Combinator). Turns Claude Code into a **"virtual engineering team"** — 23 specialists + 8 power tools, all slash commands. Notable: Garry claims 600K+ LOC in 60 days part-time.

**Key differentiator vs ECC + Superpowers:** Workflow là **role-based pipeline** (CEO → Eng → Designer → Reviewer → QA → Security → Release), không phải skill catalog (ECC) hoặc methodology framework (Superpowers).

---

## Tác giả + credibility

**Garry Tan** — President & CEO của Y Combinator (https://x.com/garrytan)

Background:
- Worked với hàng ngàn startups (Coinbase, Instacart, Rippling) khi họ 1-2 người trong garage
- Trước YC: 1 trong những eng/PM/designers đầu tiên của Palantir
- Cofounded Posterous (sold to Twitter)
- Built Bookface (YC's internal social network)

→ **Authority signal cao** cho founder/tech lead audience. Khác audience ECC (broad dev) và Superpowers (methodology-focused dev).

**Claim đáng verify:**
- 600,000+ LOC trong 60 ngày, 35% tests
- 10,000-20,000 LOC/day, part-time
- 1,237 GitHub contributions trong 2026 (vs 772 năm 2013)
- "Last `/retro` tuần qua: 140,751 LOC added, 362 commits, ~115k net LOC một tuần"

→ TODO Phase 3: verify trong CHANGELOG hoặc git log nếu repo public commit history.

---

## Cốt lõi: 23 specialists + 8 power tools (Sprint pipeline)

### "The sprint" pattern

Workflow = `Think → Plan → Build → Review → Test → Ship → Reflect`. Mỗi skill feed into next:

```
/office-hours         → write design doc
↓
/plan-ceo-review      → reads design doc, challenges scope
↓
/plan-eng-review      → ASCII diagrams, edge cases, test matrix
↓
/plan-design-review   → AI Slop detection, design rubric 0-10
↓
[implementation]
↓
/review               → catches production bugs, auto-fixes
↓
/qa <staging-url>     → opens real browser, finds bugs
↓
/ship                 → tests, coverage audit, push, PR
```

→ **Mental model:** sprint của startup được encode thành command pipeline.

### 23 specialists (workflow skills)

| Skill | Specialist role | Key insight |
|-------|----------------|-------------|
| `/office-hours` | YC Office Hours | 6 forcing questions reframe product trước code |
| `/plan-ceo-review` | CEO/Founder | 4 modes: Expansion/Selective/Hold/Reduction |
| `/plan-eng-review` | Eng Manager | ASCII diagrams data flow, edge cases, test matrix |
| `/plan-design-review` | Senior Designer | Rates dimension 0-10, AI Slop detection, AskUserQuestion per choice |
| `/plan-devex-review` | DX Lead | TTHW benchmark, magical moment design, 20-45 forcing questions |
| `/design-consultation` | Design Partner | Build design system from scratch |
| `/review` | Staff Engineer | Bugs that pass CI but blow production |
| `/investigate` | Debugger | Iron Law: no fixes without investigation, stops after 3 failed fixes |
| `/design-review` | Designer Who Codes | Audit + fix, atomic commits, before/after screenshots |
| `/devex-review` | DX Tester | Live audit, navigate docs, time TTHW |
| `/design-shotgun` | Design Explorer | 4-6 AI mockup variants, comparison board, taste memory |
| `/design-html` | Design Engineer | Mockup → production HTML với Pretext, 30KB zero-deps |
| `/qa` | QA Lead | Real browser, atomic commits, regression tests |
| `/qa-only` | QA Reporter | Same methodology as /qa, report only |
| `/pair-agent` | Multi-Agent Coordinator | Share browser với OpenClaw/Hermes/Codex/Cursor |
| `/cso` | Chief Security Officer | OWASP Top 10 + STRIDE, 8/10+ confidence gate, 17 false positive exclusions |
| `/ship` | Release Engineer | Sync main, tests, coverage, push, PR |
| `/land-and-deploy` | Release Engineer | Merge PR, wait CI/deploy, verify production |
| `/canary` | SRE | Post-deploy monitoring loop |
| `/benchmark` | Performance Engineer | Core Web Vitals before/after PR |
| `/document-release` | Technical Writer | Update all docs to match shipped code |
| `/retro` | Eng Manager | Per-person breakdowns, shipping streaks, growth opportunities |
| `/learn` | Memory | Manage gstack learnings cross-session, prune, export |

### 8 power tools

| Skill | Purpose |
|-------|---------|
| `/codex` | Second opinion từ OpenAI Codex CLI (3 modes: review/adversarial/consultation) |
| `/careful` | Warns trước rm -rf, DROP TABLE, force-push |
| `/freeze` | Restrict file edits to one directory |
| `/guard` | `/careful` + `/freeze` combined |
| `/unfreeze` | Remove freeze |
| `/open-gstack-browser` | Launch GStack Browser với sidebar, anti-bot stealth |
| `/setup-deploy` | One-time deploy config |
| `/gstack-upgrade` | Self-updater, syncs global + vendored installs |

→ **Verified:** README claim "23 specialists + 8 power tools" match folder count.

---

## Distribution model: 10-host cross-harness

**README list 10 harnesses supported** (vs ECC's 5, Superpowers's 7):

| Agent | Install path |
|-------|--------------|
| Claude Code | `~/.claude/skills/gstack` (primary) |
| OpenAI Codex CLI | `~/.codex/skills/gstack-*/` |
| OpenCode | `~/.config/opencode/skills/gstack-*/` |
| Cursor | `~/.cursor/skills/gstack-*/` |
| Factory Droid | `~/.factory/skills/gstack-*/` |
| Slate | `~/.slate/skills/gstack-*/` |
| Kiro | `~/.kiro/skills/gstack-*/` |
| Hermes | `~/.hermes/skills/gstack-*/` |
| GBrain (mod) | `~/.gbrain/skills/gstack-*/` |
| OpenClaw | Native via `clawhub` |

**Adding new host:** Per docs, "It's one TypeScript config file, zero code changes" — `hosts/<name>.ts` declarative pattern.

→ **Most cross-harness của 3 frameworks.** ECC: 5, Superpowers: 7, gstack: **10**.

### Native OpenClaw skills (4 conversational)

`clawhub install gstack-openclaw-office-hours gstack-openclaw-ceo-review gstack-openclaw-investigate gstack-openclaw-retro`

→ Ship qua ClawHub (OpenClaw marketplace) — methodology skills không cần Claude Code session.

---

## "Parallel sprints" — Conductor integration (10-15 sprints)

**Quote nguyên văn:**
> "I regularly run 10-15 parallel sprints — that's the practical max right now."

[Conductor](https://conductor.build) runs multiple Claude Code sessions parallel, mỗi cái own isolated workspace. gstack designed cho parallel execution:
- Sprint structure ngăn 10 agents thành 10 sources of chaos
- "Manage them way a CEO manages a team — check in on decisions that matter, let rest run"

→ **Distinctive philosophy:** gstack scales với Conductor cho parallel sprints, không phải sequential workflow như Superpowers's 7-stage.

---

## Karpathy connection (meta-relevance cho Storm Bear vault)

README cite Karpathy 2 lần:

1. **Opening quote** từ Andrej Karpathy:
> "I don't think I've typed like a line of code probably since December, basically, which is an extremely large change." — March 2026, No Priors podcast

2. **"Karpathy's four failure modes? Already covered."** — section claim gstack workflow enforce Karpathy's 4 AI coding rules:
   - Wrong assumptions → `/office-hours` forces vào open trước code
   - Overcomplexity → `/review` catches
   - Orthogonal edits → `/review` catches drive-by
   - Imperative over declarative → `/ship` transforms tasks thành verifiable goals

→ **Cross-vault relevance:** Storm Bear vault chính nó được build trên Karpathy's LLM Wiki pattern. gstack cite Karpathy explicit + claim implement his 4 rules. **Convergent thinking.**

---

## Monetization + license

**MIT license. Free forever. No premium tier, no waitlist.**

> "I open sourced how I build software. You can fork it and make it your own."

**Hiring CTA in README:**
> "We're hiring. Want to ship 10K+ LOC/day and help harden gstack? Come work at YC — ycombinator.com/software. Extremely competitive salary and equity. San Francisco, Dogpatch District."

→ gstack functions as **YC recruiting funnel** + open-source dev tool. Distinct commercial model so với:
- ECC: separate paid products (AgentShield commercial)
- Superpowers: zero commercial, pure OSS
- gstack: free OSS + recruiting signal

---

## Telemetry stance

**Opt-in default OFF** — first-run asks. Sent (if opt-in): skill name, duration, success/fail, gstack version, OS. **Never sent:** code, file paths, repo names, prompts.

Storage: Supabase với schema public trong `supabase/migrations/`. Public key + RLS deny direct access. Edge functions enforce schema.

→ **Privacy-conscious design.** Match (or exceed) ECC's stance.

---

## Connection to sibling projects (cross-vault)

| Aspect | ECC | Superpowers | gstack |
|--------|-----|-------------|--------|
| Distribution philosophy | Plugin | Marketplace + git URL | Slash command symlinks |
| Workflow | Skill compose ad-hoc | 7-stage hard-gated | Role-based sprint pipeline |
| Cross-harness count | 5 | 7 | **10** |
| Author archetype | Solo dev (Anthropic Hackathon Winner) | Solo dev (OG dev tool author) | **CEO of YC** |
| Audience focus | Broad dev | Methodology-focused dev | **Founder/CEO** + Claude Code first-timer + tech lead |
| Open-source model | Plugin + paid products | Pure OSS | OSS + recruiting funnel |
| TDD pattern | `tdd-workflow` skill (best practice) | Iron Law (mandatory) | Built into `/ship` (test bootstrapping) |
| Subagent | 48 specialized | 1 + dynamic spawn | 23 specialists + parallel via Conductor |

→ **Convergent insights:**
- All 3 priortize cross-harness portability
- All 3 build TDD into workflow (different intensity)
- All 3 emphasize discipline over capability

→ **Divergent:**
- gstack uniquely tuned cho **founder/CEO audience** (vs ECC: broad, Superpowers: methodology-focused dev)
- gstack uniquely **role-based** vs skill-catalog vs methodology-stage

---

## Open questions resolved

- ✅ Q3: 23 specialists + 8 power tools — folder count match
- ✅ Q7: Multi-host support level — 10 hosts, declarative TypeScript config
- ✅ Q8: Garry's CEO position — explicitly tunes audience to founders, recruiting funnel embedded

## Open questions raised

- ⏸ Verify 600K LOC/60 days claim trong git log
- ⏸ `/office-hours` 6 forcing questions cụ thể là gì? — đọc skill template
- ⏸ "Taste memory" trong `/design-shotgun` — implementation pattern reusable cho Storm Bear?
- ⏸ Pretext (cho `/design-html`) — 30KB zero-dep CSS layout system, đáng deep dive nếu Storm Bear cần design tooling

---

## Cross-references

- [[(C) CLAUDE.md summary]] — development conventions + slop-scan + voice protections
- [[(C) ETHOS + ARCHITECTURE summary]] — builder philosophy + browser daemon design
- [[(C) index]]
- [[(C) log]]
- Cross-project: `../../Everything Claude Code - Beginner Analysis/02 Wiki/(C) README summary.md`
- Cross-project: `../../Superpowers - Beginner Analysis/02 Wiki/(C) README summary.md`

## Citations

- `00 Sources/gstack/README.md` (full file, lines 1-411)
- Quote from Karpathy: README line 3
- Quote about LOC volume: README line 9
- Hiring CTA: README lines 352-353

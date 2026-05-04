# (C) Specialist Roles

> **Source:** synthesized từ README.md (lines 186-237), verified qua folder listing `00 Sources/gstack/`
> **Ingested:** 2026-04-18
> **Type:** Entity page (building block) — entity #2 cho gstack

---

## One-liner

**VI:** Specialist Roles là **23 slash commands + 8 power tools** trong gstack, mỗi cái persona khác nhau (CEO, Eng Manager, Designer, QA Lead, CSO, ...). Mental model: Claude Code trở thành "virtual engineering team" — không phải generic AI mà **team of specialists**, mỗi role có rubric + output schema riêng.

**EN:** 23 slash commands + 8 power tools, each a distinct persona. Mental model: Claude Code becomes a "virtual engineering team" — not generic AI but a team of specialists with their own rubrics and output schemas.

---

## Khi nào dùng concept này

**Hữu ích khi:**
- Setup project lần đầu — hiểu role cần gọi cho task nào
- Debug workflow — skill nào miss? sprint pipeline đang ở đâu?
- Compare với ECC's 48 agents / Superpowers's 1 agent — understand distribution of specialization
- Team adoption — train new members về role taxonomy

**Không cần deep dive nếu:** chỉ dùng `/autoplan` (auto-routes to right specialists).

---

## Comparison sibling

| Axis | Specialist Roles (gstack) | Subagents (ECC) | Sub-prompts (Superpowers SDD) |
|------|--------------------------|------------------|-------------------------------|
| Count | 23 specialists + 8 power tools | 48 specialized agents | 1 code-reviewer + dynamic spawn |
| Invocation | Slash command `/qa`, `/review` | Task tool với agent name | `Task` tool spawn within SDD skill |
| Granularity | Role-based (CEO, QA, CSO) | Domain-based (security, DB, frontend) | Function-based (implementer/reviewer) |
| Output schema | Markdown with sections | Free-form text | **Structured status (DONE/CONCERNS/BLOCKED/NEEDS_CONTEXT)** |
| Reusable across projects | ✅ Yes (universal) | ✅ Yes | ✅ Yes |
| Voice-friendly | ✅ "run QA" → /qa | ❌ Agent name required | ❌ SDD internal |

→ **Distinctive:** gstack's specialist model maps to startup org chart. ECC maps to technology domain. Superpowers maps to function.

---

## Sub-types: 4 categories

### Category 1: Think + Plan (5 roles)

| Role | Persona | Core technique |
|------|---------|----------------|
| `/office-hours` | YC Office Hours | 6 forcing questions reframe product |
| `/plan-ceo-review` | CEO/Founder | 4 modes: Expansion/Selective/Hold/Reduction |
| `/plan-eng-review` | Eng Manager | ASCII diagrams, state machines, test matrix |
| `/plan-design-review` | Senior Designer | 0-10 rubric per dimension, AI Slop detection |
| `/plan-devex-review` | DX Lead | TTHW benchmark, 20-45 forcing questions, 3 modes (EXPANSION/POLISH/TRIAGE) |
| `/autoplan` | Review Pipeline (orchestrator) | CEO → design → eng → DX auto-chain |

### Category 2: Design system (3 roles)

| Role | Persona | Core technique |
|------|---------|----------------|
| `/design-consultation` | Design Partner | Build design system from scratch |
| `/design-shotgun` | Design Explorer | 4-6 AI mockup variants + comparison board + taste memory |
| `/design-html` | Design Engineer | Mockup → production HTML with Pretext (30KB zero-deps) |

### Category 3: Review + Test + Ship (11 roles)

| Role | Persona | Core technique |
|------|---------|----------------|
| `/review` | Staff Engineer | Bugs that pass CI, auto-fix obvious |
| `/investigate` | Debugger | **Iron Law: no fixes without investigation**, stops after 3 failed fixes |
| `/design-review` | Designer Who Codes | Audit + fix, atomic commits |
| `/devex-review` | DX Tester | Live audit, navigate docs, time TTHW |
| `/qa` | QA Lead | Real browser, atomic commits, regression tests per bug |
| `/qa-only` | QA Reporter | Same methodology as /qa, report-only |
| `/cso` | Chief Security Officer | OWASP Top 10 + STRIDE, 8/10+ confidence gate |
| `/codex` | Second Opinion | Independent review from OpenAI Codex CLI (3 modes) |
| `/ship` | Release Engineer | Sync main, tests, coverage, push, PR |
| `/land-and-deploy` | Release Engineer | Merge, CI/deploy wait, verify production |
| `/canary` | SRE | Post-deploy monitoring loop |
| `/benchmark` | Performance Engineer | Core Web Vitals before/after PR |

### Category 4: Meta + Reflect (4 roles)

| Role | Persona | Core technique |
|------|---------|----------------|
| `/retro` | Eng Manager | Per-person breakdowns, `/retro global` cross-project |
| `/document-release` | Technical Writer | Update all docs to match shipped code |
| `/learn` | Memory | Manage gstack learnings, prune, export |
| `/pair-agent` | Multi-Agent Coordinator | Share browser với other AI agents |

### Power tools (8)

| Tool | Purpose |
|------|---------|
| `/careful` | Safety guardrails — warns rm -rf, DROP TABLE, force-push |
| `/freeze` | Edit lock — restrict edits to one directory |
| `/guard` | `/careful` + `/freeze` combined |
| `/unfreeze` | Remove freeze |
| `/browse` | Browser access cho agent |
| `/open-gstack-browser` | Launch GStack Browser visible |
| `/setup-deploy` | One-time deploy config |
| `/gstack-upgrade` | Self-update |

→ **Folder count verified:** `find 00 Sources/gstack -maxdepth 1 -type d` = 30+ folders. Matches README claim "23 specialists + 8 power tools."

---

## Anatomy của 1 Specialist Role

Mỗi role là 1 folder trong repo root chứa:

```
<role-name>/
├── SKILL.md           ← Generated từ template (prompt Claude reads)
├── SKILL.md.tmpl      ← Template source of truth
└── <support files>    ← Optional rubrics, fixtures, scripts
```

**Example: `/cso` (Chief Security Officer):**
- `cso/SKILL.md` — prompt Claude reads khi user invokes
- `cso/SKILL.md.tmpl` — template source (edit here, regen via `bun run gen:skill-docs`)
- Persona framing + OWASP Top 10 checklist + STRIDE methodology + false positive rules

**Example: `/review` (Staff Engineer):**
- `review/SKILL.md` — review rubric
- Auto-fix rules embedded
- References shared `error-handling.ts` utilities

---

## Cơ chế: Specialist persona injection

Mỗi SKILL.md opens với persona framing:
- "You are a Chief Security Officer..."
- "You are a Staff Engineer reviewing this PR..."
- "You are a YC Partner running office hours..."

**Why personas work:**
- LLM steers output toward persona's typical behavior
- User mental model matches (hire CSO = expect OWASP audit)
- Different personas catch different bugs (eng finds race conditions, designer finds AI slop)

### Preamble injection (ETHOS principles)

Per ETHOS.md: "These principles are injected into every workflow skill's preamble automatically."

**Boil the Lake + Search Before Building + User Sovereignty** applied to every role. Ensures consistency without duplicating prose per skill.

→ **Pattern:** DRY for principles. Preamble system injects shared ethos into every specialist prompt.

---

## Out-of-box behavior per role

**Consistent across roles:**
- Reads CLAUDE.md for project-specific config
- Uses AskUserQuestion for ambiguities
- Persists decisions to CLAUDE.md so không hỏi lại
- Writes design doc / findings artifact for next stage

**Role-specific:**
- `/qa` opens real browser (requires browser daemon running)
- `/cso` runs OWASP + STRIDE scans
- `/ship` bootstraps test framework if missing
- `/retro` reads git log + test health trends

---

## Configuration knobs per role

Most roles read from CLAUDE.md:
- Test command (ask if missing, persist)
- Deploy command (from `/setup-deploy`)
- Staging URL (for `/qa`)
- Base branch (detect dynamically: main/master)
- Project-specific patterns

**No hardcoded configs across roles** — per CLAUDE.md platform-agnostic rule.

---

## Recipes

### Recipe 1: Feature development (user-facing)

```
/office-hours → /autoplan → [implement] → /design-review → /qa → /ship
```

### Recipe 2: Infrastructure change

```
/office-hours → /plan-eng-review → [implement] → /review → /ship
```

→ Smart routing skips design + DX review (infra, not user-facing).

### Recipe 3: Bug investigation

```
/investigate <bug description>
```

**Iron Law:** no fixes without investigation. Traces data flow, tests hypotheses. **Stops after 3 failed fixes** → escalate.

→ Analog to Superpowers's structured status protocol (BLOCKED status).

### Recipe 4: Security audit before launch

```
/cso
```

Produces:
- OWASP Top 10 findings (only 8/10+ confidence)
- STRIDE threat model
- Concrete exploit scenario per finding
- 17 false positive exclusions applied (zero-noise)

### Recipe 5: Cross-model second opinion

```
/review      (Claude reviews branch)
/codex       (OpenAI Codex reviews same branch)
```

When both have run, cross-model analysis shows which findings overlap vs unique to each.

→ **Distinctive:** gstack is only framework with native cross-model review.

### Recipe 6: Weekly retro

```
/retro              (current project)
/retro global       (across ALL your projects + AI tools: Claude Code, Codex, Gemini)
```

Per-person breakdowns, shipping streaks, test health trends, growth opportunities.

---

## Advanced patterns

### Pattern: Interactive role với AskUserQuestion

Many roles stop for user decisions:
- `/plan-design-review` — one AskUserQuestion per design choice
- `/plan-devex-review` — 20-45 forcing questions
- `/office-hours` — 6 forcing questions

→ **User Sovereignty ETHOS applied** — AI recommends, user decides.

### Pattern: Role self-limitation

`/investigate` stops after 3 failed fixes. `/qa` does atomic commits (can rollback). `/careful` warns before destructive ops.

→ **Safety via self-limitation** — roles know when to escalate.

### Pattern: Artifact output schema

Each role produces known artifact:
- `/office-hours` → design doc (feeds `/plan-*-review`)
- `/plan-eng-review` → test plan (feeds `/qa`)
- `/review` → findings list (feeds `/ship` verify-fixed)

### Pattern: Cross-role memory via /learn

`/learn` manages learnings across sessions. Role outputs can annotate learnings (project-specific patterns, pitfalls, preferences). Next invocation of same role benefits.

→ **Continuous learning compound.** Match ECC's continuous-learning pattern.

---

## Combination với building blocks khác

### + Sprint Pipeline
Specialist Roles populate stages của Sprint Pipeline. Pipeline = flow, Roles = content.

### + Browser Daemon
Roles yêu cầu browser (`/qa`, `/design-review`, `/devex-review`, `/browse`) depend vào daemon architecture.

### + Multi-Host Platform
Same 23 roles deploy on 10 hosts với tool name mapping. Specialist personas travel cross-harness.

### Cross-project: + ECC's 48 agents
ECC agents are **domain-specialized** (security, DB, frontend). gstack roles are **function-specialized** (CEO, QA, release). Orthogonal taxonomies. Could combine if needed (unlikely mix-recommended).

### Cross-project: + Superpowers 1 agent + SDD
Superpowers has 1 pre-built agent (code-reviewer) + spawn implementer/reviewer dynamically. Different philosophy — Superpowers generic + flexible, gstack pre-built + role-defined.

---

## Anti-patterns

❌ **Use `/ship` without `/review`** — skip safety net. Roles compose by design.

❌ **Skip `/office-hours`** — start at `/plan-*` means building wrong thing (reframing step skipped).

❌ **Force `/plan-design-review` cho infra change** — smart routing exists for a reason.

❌ **Treat role outputs as optional** — each stage's output feeds next. Skip = break pipeline.

❌ **Bypass `/investigate`** — "I know the bug" → Iron Law says investigate. Skipping = speculative fix.

❌ **Run `/cso` để bỏ qua security discipline** — 8/10+ confidence gate shouldn't be lowered. Findings below threshold = noise, not safety.

❌ **Ignore AskUserQuestion pauses** — User Sovereignty ETHOS. Pauses are features, not friction.

---

## Cross-references

- [[(C) Sprint Pipeline]] — workflow orchestration
- [[(C) Browser Daemon Architecture]] — tech for /qa, /design-review
- [[(C) Multi-Host Declarative Platform]] — distribution
- [[(C) README summary]] — role list original
- [[(C) CLAUDE.md summary]] — skill template system
- Cross-project: `../../Everything Claude Code - Beginner Analysis/02 Wiki/(C) Subagents.md`
- Cross-project: `../../Superpowers - Beginner Analysis/02 Wiki/(C) Subagent-Driven Development.md`

## Citations

- README.md lines 188-215 (24 specialist rows)
- README.md lines 227-237 (8 power tools table)
- README.md lines 218-224 (routing matrix)
- CLAUDE.md lines 82-160 (project structure showing role folders)
- Verified folder existence via directory listing

## TODO

- ⏸ Deep dive `/cso` SKILL.md — 17 false positive exclusions specific list worth extracting
- ⏸ Verify `/autoplan` internal sequence — is it truly sequential CEO→design→eng→DX or parallel?
- ⏸ Compare `/investigate` Iron Law với Superpowers TDD Iron Law — convergent discipline?
- ⏸ Map `/retro global` cross-project pattern — adaptable cho Storm Bear vault reflection?

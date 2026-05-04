# (C) Sprint Pipeline

> **Source:** synthesized từ README.md (lines 180-240), CLAUDE.md, ETHOS.md
> **Ingested:** 2026-04-18
> **Type:** Entity page (workflow concept) — building block #1 cho gstack

---

## One-liner

**VI:** Sprint Pipeline là **workflow xương sống của gstack** — mỗi feature đi qua pipeline `Think → Plan → Build → Review → Test → Ship → Reflect` với specialists cụ thể cho từng stage. Mỗi skill **feed output vào next skill** (design doc từ `/office-hours` → input cho `/plan-ceo-review` → v.v.), không cần human relay.

**EN:** Sprint Pipeline is gstack's workflow backbone — each feature flows through `Think → Plan → Build → Review → Test → Ship → Reflect` with specific specialists per stage. Each skill feeds output to the next without human relay.

---

## Khi nào dùng concept này

**Hữu ích khi:**
- Hiểu vì sao gstack "là process, không phải collection of tools"
- Designing workflow framework riêng — xem pipeline-vs-catalog trade-off
- So sánh với Superpowers's 7-stage workflow (analog, different granularity)
- Team setup Claude Code lần đầu — cần mental model "how skills compose"

**Không cần để dùng gstack cơ bản** — skills auto-suggest, agent biết pipeline. Hiểu pipeline giúp deliberate decisions (khi nào skip, khi nào parallelize).

---

## Comparison sibling

| Khía cạnh | Sprint Pipeline (gstack) | 7-Stage Workflow (Superpowers) | Sequential Phases (ECC) |
|-----------|--------------------------|-------------------------------|-------------------------|
| Stages | 7 cao-level (Think/Plan/Build/Review/Test/Ship/Reflect) | 7 explicit (Brainstorming → Finishing) | 5 soft (Research/Plan/Implement/Review/Verify) |
| Enforcement | Skill auto-suggest theo context | HARD-GATE XML blocks | Best-practice guidance |
| Subagents | 23 specialists pre-built | 1 reviewer + dynamic spawn | 48 specialized |
| Flexibility | Smart routing (skip infra from CEO) | Hard gates (không skip stage 1, 5) | Full flexibility |
| Parallelism | **Conductor-based** 10-15 parallel sprints | Limited (subagent dispatch) | Skill-compose parallel |
| Reflection phase | `/retro` built-in weekly | Iteration log manual | Not explicit |

→ **Distinctive:** gstack có **reflection phase** built-in (`/retro` + cross-project `/retro global`). Superpowers + ECC không mandate reflection.

---

## Sub-types: 4 routing modes

Per README "Which review should I use?":

### 1. User-facing products (UI, web, mobile)
- **Plan stage:** `/plan-design-review` — AI Slop detection, design rubric 0-10
- **Live audit:** `/design-review` — atomic commits, before/after screenshots

### 2. Developer products (API, CLI, SDK, docs)
- **Plan stage:** `/plan-devex-review` — TTHW benchmark, 20-45 forcing questions
- **Live audit:** `/devex-review` — actually tests onboarding, times TTHW

### 3. Architecture (data flow, perf, tests)
- **Plan stage:** `/plan-eng-review` — ASCII diagrams, edge cases, test matrix
- **Live audit:** `/review` — staff engineer bugs

### 4. All-of-above
- `/autoplan` — runs CEO → design → eng → DX automatically, surfaces only taste decisions

→ **Smart routing principle:** "Just like at a well-run startup — CEO doesn't look at infra bugs, design review isn't needed for backend." Pipeline adapts to work type.

---

## Anatomy của 1 sprint

**Example từ README:**

```
1. User: "I want to build a daily briefing app for my calendar"
2. /office-hours
   Agent: asks about pain (specific examples, not hypotheticals)
   User: explains — multiple Google calendars, stale info, wrong locations
   Agent: "pushes back on framing" — reframes as "personal chief of staff AI"
   Agent: extracts 5 capabilities, challenges 4 premises
   Agent: 3 implementation approaches với effort estimates
   Agent: RECOMMENDATION — narrowest wedge tomorrow, full vision 3-month
   Agent: writes design doc → feeds downstream skills

3. /plan-ceo-review
   Agent: reads design doc, challenges scope, runs 10-section review
   Agent: picks mode (Expansion/Selective/Hold/Reduction)

4. /plan-eng-review
   Agent: ASCII diagrams for data flow, state machines, error paths
   Agent: test matrix, failure modes, security concerns

5. User: "Approve plan. Exit plan mode."
   Agent: writes 2,400 lines across 11 files. ~8 minutes.

6. /review
   Agent: [AUTO-FIXED] 2 issues. [ASK] Race condition → user approves fix.

7. /qa https://staging.myapp.com
   Agent: opens real browser, clicks through flows, finds and fixes a bug.

8. /ship
   Tests: 42 → 51 (+9 new). PR: github.com/you/app/pull/42
```

**Key insight từ example:**
- User said "daily briefing app" → Agent said "you're building chief of staff AI" because it **listened to pain, not feature request**
- 8 commands end-to-end
- "That is not a copilot. That is a team."

---

## Cơ chế: Skills compose via artifact hand-off

**Không phải loose collection of skills. Each skill:**

1. **Reads artifacts produced by previous skill** — design doc từ `/office-hours` picked up by `/plan-ceo-review`
2. **Writes artifacts consumed by next skill** — test plan từ `/plan-eng-review` picked up by `/qa`
3. **Cross-references catch drift** — `/review` catches bugs that `/ship` verifies fixed

**"Nothing falls through the cracks because every step knows what came before it."**

→ **Pattern:** Artifact-driven skill composition. Each skill has known input/output schema.

### Proactive skill suggestions

> "gstack notices what stage you're in — brainstorming, reviewing, debugging, testing — and suggests the right skill. Don't like it? Say 'stop suggesting' and it remembers across sessions."

→ **Self-routing** — agent detects stage + suggests. User can override.

---

## Out-of-box behavior

**Khi cài gstack, ngay lập tức có:**
- 23 specialists (slash commands) auto-discoverable
- 8 power tools
- Proactive skill suggestions (default ON)
- Cross-session memory via `/learn`
- Voice-friendly trigger phrases (cho AquaVoice/Whisper)

**KHÔNG có:**
- Pre-configured project — first invocation của `/office-hours` writes CLAUDE.md
- Pre-set design system — `/design-consultation` builds from scratch
- External telemetry (opt-in OFF by default)

---

## Configuration knobs

| Knob | Type | Default | Khi cần đổi |
|------|------|---------|-------------|
| `skill_prefix` trong `~/.gstack/config.yaml` | boolean | `false` (short names like `/qa`) | Namespace xung đột với other skill packs → `/gstack-qa` |
| Proactive suggestions | toggle via voice | ON | "Stop suggesting" → persists |
| Telemetry | opt-in | OFF | First run asks; `gstack-config set telemetry off` to disable |
| Parallel workers (Conductor) | external tool | n/a | Scale 1 → 6 → 12 → 15 sprints as team grows |
| Auto-upgrade | `auto_upgrade` in config | throttled hourly | Aggressive: set `auto_upgrade: true` |

---

## Recipes

### Recipe 1: First-time user — pilot run (30 min)

```
1. Install gstack (30s)
2. /office-hours — describe what you're building
3. /plan-ceo-review — see CEO reframing on your feature idea
4. /review — run trên any branch with changes
5. /qa — test against staging
6. STOP. You'll know if this is for you.
```

→ README explicitly says: "Stop there. You'll know if this is for you."

### Recipe 2: Solo founder full sprint

```
Monday:
  /office-hours → 30 min spec
  /autoplan → 1 hour reviewed plan (CEO → design → eng auto)

Tuesday-Wednesday:
  [implementation, agent writes 2-5K LOC]
  /review → auto-fix issues
  /qa → real browser test

Thursday:
  /ship → PR opened
  /land-and-deploy → merge, deploy, verify production

Friday:
  /retro → weekly engineering retro, per-person breakdowns
  /document-release → update docs to match shipped code
```

### Recipe 3: Tech lead team mode (shared repo)

```bash
cd ~/.claude/skills/gstack && ./setup --team
cd <your-repo>
~/.claude/skills/gstack/bin/gstack-team-init required
git add .claude/ CLAUDE.md && git commit -m "require gstack for AI-assisted work"
```

→ Every developer installs globally, updates auto. Silent hourly sync. No vendored files in repo.

### Recipe 4: 10-15 parallel sprints (Conductor)

[Conductor](https://conductor.build) runs multiple Claude Code sessions parallel, each isolated workspace:
- Session 1: `/office-hours` on new idea
- Session 2: `/review` on PR
- Session 3: implementing feature
- Session 4: `/qa` on staging
- Sessions 5-15: other branches

> "You manage them the way a CEO manages a team: check in on decisions that matter, let rest run."

### Recipe 5: Security audit

```
/cso
```

OWASP Top 10 + STRIDE threat model. 17 false positive exclusions, 8/10+ confidence gate, independent finding verification, concrete exploit scenario per finding.

→ **Zero-noise discipline** — only high-confidence findings shown.

---

## Advanced patterns

### Pattern: Artifact-driven skill composition

Each skill produces known output schema (design doc, test plan, PR body), consumed by next skill. Reusable cho Storm Bear nếu build skill library.

### Pattern: Smart review routing

Pipeline knows when CEO review doesn't apply (infra bugs) vs when needed (user-facing change). Reduces noise.

### Pattern: Voice-friendly trigger phrases

Instead of `/qa`, say "run QA" or "test the website". Skill matches via description. Accessibility win.

### Pattern: "Boomerang" plan vs live audit comparison

`/plan-devex-review` scores plan. `/devex-review` tests live. **Compare scores → see if plan matched reality.**

→ **Feedback loop** cho plan quality over time. Storm Bear vault could adapt cho wiki build routine (expected vs actual velocity).

### Pattern: Taste memory (`/design-shotgun`)

After few rounds, tool biases toward what user actually likes. Learning compound across sessions.

→ **Generalizable:** any skill với preference could learn user taste. Cross-session memory = `/learn`.

---

## Combination với building blocks khác

### + Specialist Roles
Sprint Pipeline = **orchestration**; Specialist Roles = **content** (xem [[(C) Specialist Roles]]).

### + Browser Daemon
Browser daemon makes `/qa` + `/design-review` + `/devex-review` possible (real clicks, real screenshots). Không có daemon = pipeline mất half its power.

### + Multi-Host Platform
Pipeline runs on 10 hosts, với tool name mapping runtime. Voice trigger phrases work universally.

### Cross-project: + Superpowers 7-Stage Workflow
**Convergent:** both enforce sequence Think → Plan → Build → Review → Test → Ship.
**Divergent:** Superpowers HARD-GATE (XML), gstack smart-routing (skill auto-suggest). Different mechanisms, same intent.

### Cross-project: + ECC Sequential Phases
ECC's phases softer (guidance), gstack's harder (pipeline). Same conceptual skeleton.

---

## Anti-patterns

❌ **Use 1 skill without pipeline context** — `/ship` without `/review` = skip safety net. gstack expects sequence.

❌ **Override smart routing blindly** — if `/autoplan` skips design review, likely your change is infra-only. Don't force design review.

❌ **Treat `/retro` as optional** — reflection is phase 7. Skip = lose learning compound.

❌ **Run 15 parallel sprints without Conductor** — gstack designed for isolated workspaces. Without Conductor, agents step on each other.

❌ **Skip `/office-hours` for "simple" tasks** — README example shows "daily briefing" reframed as "chief of staff AI." Missing reframing = building wrong thing.

❌ **Treat AskUserQuestion as friction** — it's User Sovereignty enforcement (xem ETHOS).

---

## Cross-references

- [[(C) Specialist Roles]] — 23 roles detail
- [[(C) Browser Daemon Architecture]] — tech backbone cho /qa and /design-review
- [[(C) Multi-Host Declarative Platform]] — distribution model
- [[(C) README summary]]
- [[(C) ETHOS + ARCHITECTURE summary]]
- Cross-project: `../../Superpowers - Beginner Analysis/02 Wiki/(C) The 7-Stage Workflow.md`
- Cross-project: `../../Everything Claude Code - Beginner Analysis/02 Wiki/(C) Skills.md`

## Citations

- README.md lines 180-240 (sprint pipeline description)
- README.md lines 138-178 (concrete example walkthrough)
- README.md lines 218-224 (routing table)

## TODO

- ⏸ Verify exact sequence cho `/autoplan` — reads CEO + design + eng + DX? All parallel?
- ⏸ `/retro global` cross-project — worth deep dive for Storm Bear vault reflection pattern
- ⏸ "Taste memory" implementation — cross-session learning could adapt vault's continuous-learning v2

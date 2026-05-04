# (C) Skills + Commands + Lifecycle cluster summary — codymaster

> **Sources:** skills/ listing (79 folders), commands/ listing (11 files), README §Full Lifecycle + §4-Layer Protection + §60+ Skill Arsenal
> **Status:** ✅ Phase 2 source summary
> **Parent index:** [[(C) index]]

---

## 1. Why cluster

Skills + commands + lifecycle = the **user-facing surface** of codymaster. Brain primitives (5-Tier Memory, Smart Spine, etc — see [[(C) Novel Primitives cluster summary]]) are the engine. This cluster is the steering wheel.

## 2. 79 skills — the real count

Actual skills in `skills/` folder as of 2026-04-19:

### Engineering & Code (9)
cm-autopilot, cm-clean-code, cm-code-review, cm-codeintell, cm-debugging, cm-tdd, cm-test-gate, cm-quality-gate, cm-security-gate

### DevOps & Deployment (5)
cm-conductor-worktrees, cm-git-worktrees, cm-post-deploy-canary, cm-safe-deploy, cm-safe-i18n

### Secret & Security (2)
cm-secret-shield, cm-identity-guard

### Project & Team Management (6)
cm-booking-calendar, cm-brainstorm-idea, cm-planning, cm-retro-cli, cm-sprint-bus, cm-status

### Design & UX (4)
cm-design-studio, cm-design-system, cm-ui-preview, cm-ux-master

### Ads, Analytics, Growth (4)
cm-ads-tracker, cm-cro-methodology, cm-growth-hacking, cm-jtbd

### Publishing & Content (2)
cm-auto-publisher, cm-content-factory

### Skills Management / Self-Healing (7)
cm-skill-chain, cm-skill-evolution, cm-skill-health, cm-skill-index, cm-skill-mastery, cm-skill-search, cm-skill-share

### Infrastructure & Tools (9)
cm-dashboard, cm-dockit, cm-execution, cm-google-form, cm-mcp-engineering, cm-notebooklm, cm-readit, cm-reactor, cm-terminal

### Business & Search (3)
cm-browse, cm-deep-search, (plus cm-jtbd above counted once)

### Other / Meta (various)
cm-continuity, cm-ecosystem-roadmap, cm-engineering-meta, cm-example, cm-guardian-runtime, cm-how-it-work, cm-project-bootstrap, cm-qa-visual-cli, cm-second-opinion-cli, cm-start

**Total visible:** ~79 folders. README says "60+". Plugin.json says "68+". Real count **79**.

## 3. Why the marketing undersells

Hypotheses:
1. **Conservative claim discipline** — author wrote README at skill-count 60, then added 19 more but didn't update
2. **Some folders are WIP/internal** — cm-example, cm-how-it-work, cm-start could be template/documentation-skills not counted
3. **"60+" is sticky marketing** — easier to preserve than update

**Wiki convention:** we use **79** as ground truth but report all three numbers (60+/68+/79) when relevant.

## 4. 11 commands (not 20+)

Files in `commands/`:
1. bootstrap.md
2. build.md
3. content.md
4. continuity.md
5. debug.md
6. demo.md
7. deploy.md
8. plan.md
9. review.md
10. track.md
11. ux.md

All `.md` — presumably each is a command-workflow definition (not a CLI shim).

### Reconciling "20+ Commands" claim
README lists CLI verbs: `cm status`, `cm dashboard`, `cm brain`, `cm chain`, `cm deploy`, `cm agent`, `cm sprint`, etc. These are operational commands invoked via the `cm` CLI (from `package.json` bin field).

**Two distinct "command" concepts:**
- **Workflow commands** (`commands/` folder, 11 files) — slash-command or skill-like workflows a user invokes inside Claude/Cursor
- **CLI verbs** (`cm <verb>`) — shell-level commands the `cm` binary accepts

README conflates both when claiming "20+". More honest: **11 workflow commands + ~10-15 CLI verbs = ~20-25 total invocation surfaces**. Marketing is technically defensible, practically misleading for new users.

## 5. Full Lifecycle (Idea → Production → Learning)

README's lifecycle model:

```
Idea → Plan → Design → Test First → Code → Debug → Quality Gate 
→ Security Scan → Deploy → Monitor → Document → Learn & Improve
                                                        ↓
                                              (feedback loop back to Plan)
```

### Lifecycle coverage vs T1 peers

| Stage | codymaster | BMAD | GSD | gstack | Superpowers | ECC |
|-------|-----------|------|-----|--------|-------------|-----|
| **Idea** | cm-brainstorm-idea, cm-jtbd | ⚠️ | ❌ | ❌ | ❌ | ❌ |
| **Plan** | cm-planning, cm-sprint-bus | ✅ PM agent | Partial | ✅ PM | ✅ stage 1 | ❌ |
| **Design** | cm-design-studio, cm-design-system, cm-ux-master | ⚠️ UX agent | ❌ | ❌ | ❌ | ❌ |
| **Test First** | cm-tdd | ⚠️ TEA module | Partial | ⚠️ | ✅ (TDD core) | ⚠️ |
| **Code** | cm-autopilot, cm-clean-code | ✅ Amelia | ✅ agents | ✅ roles | ✅ stage 4 | ✅ skills |
| **Debug** | cm-debugging | ⚠️ | ⚠️ | ⚠️ | ✅ stage 5 | ⚠️ |
| **Quality** | cm-quality-gate, cm-code-review | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ⚠️ |
| **Security** | cm-security-gate, cm-secret-shield | ❌ | ❌ | ❌ | ❌ | AgentShield ✅ |
| **Deploy** | cm-safe-deploy, cm-post-deploy-canary | ❌ | ❌ | ❌ | ❌ | ❌ |
| **Monitor** | cm-post-deploy-canary | ❌ | ❌ | ❌ | ❌ | ❌ |
| **Document** | cm-dockit, cm-auto-publisher | ❌ | ❌ | ❌ | ❌ | ❌ |
| **Learn** | cm-skill-evolution, cm-learning-promoter | ❌ | ❌ | ❌ | ❌ | ❌ |

→ **codymaster is the only T1 framework claiming end-to-end Idea→Learn coverage.** Peers cluster around Code + Plan ± Test.

### Verification skepticism

"Full Lifecycle" is a big claim. Realistic assessment:
- **Code/Debug/Test stages** = deep coverage, many skills
- **Plan/Design stages** = multiple skills, but depth per skill unknown
- **Idea stage** (cm-brainstorm-idea, cm-jtbd) = 2 skills, probably shallow without integration with user's actual product context
- **Deploy/Monitor stages** = 2 skills (cm-safe-deploy, cm-post-deploy-canary), probably checklist-grade not autonomous
- **Learn stage** (cm-skill-evolution, cm-learning-promoter) = self-healing for the framework itself, not for user's product

**Honest framing:** codymaster has **coverage artifacts** at every lifecycle stage but not **equal depth**. Compare: gstack claims "virtual engineering team" but is mostly role framing; codymaster delivers more actual skills per stage.

## 6. 4-Layer Protection

Before Deploy, codymaster enforces:

| Layer | Protections | Relevant skills |
|-------|-------------|-----------------|
| **Layer 1** | TDD + Code Review | cm-tdd, cm-code-review, cm-clean-code |
| **Layer 2** | Secret scan + Vuln scan + Account validation | cm-secret-shield, cm-security-gate, cm-identity-guard |
| **Layer 3** | Isolated git worktrees | cm-git-worktrees, cm-conductor-worktrees |
| **Layer 4** | Quality gates + Multi-gate safe deploy | cm-quality-gate, cm-safe-deploy, cm-post-deploy-canary |

### Why this matters
- **Defense in depth** — each layer independently catches different risks
- **Matches ECC AgentShield philosophy** (security as first-class, not afterthought)
- **Git worktrees isolation** (Layer 3) matches gstack's parallel-dispatch pattern

**Unique to codymaster:** all 4 layers integrated in one kit. Peers have some layers but not cohesive 4-layer system.

## 7. Skill domain groupings (user-facing)

README's marketing grouping:

| Domain | Skill count (approx) | Storm Bear relevance |
|--------|---------------------|----------------------|
| Engineering | ~10-12 | Direct (dev work) |
| Operations | ~8-10 | Direct (deploy, security) |
| Product/UX | ~6-8 | Adjacent (Scrum coaching includes product) |
| Growth | ~5-7 | Low (marketing-adjacent) |
| Enterprise | ~2-3 | Low (small biz scope) |
| Self-Healing | ~5-7 | Meta (framework maintenance) |
| Orchestration | ~4-5 | Direct (skill chaining) |

### Scope observations
- Growth domain (cm-ads-tracker, cm-cro-methodology, cm-growth-hacking) = unusual for a "coding" framework
- Enterprise domain thin (cm-reactor + cm-notebooklm only) — name suggests scope but delivery is narrow
- Self-Healing = most unusual; no peer has "framework maintains itself" as domain

### Storm Bear skill-fit
Most relevant for Scrum coach + dev:
- **cm-retro-cli** — retrospective facilitation CLI
- **cm-sprint-bus** — sprint coordination
- **cm-planning** — sprint/quarter planning
- **cm-brainstorm-idea** — ideation facilitation
- **cm-jtbd** — jobs-to-be-done framework
- **cm-continuity** — cross-session memory (coaching context preservation)

6 directly-relevant skills. That's substantial for Storm Bear pilot value.

## 8. Naming conventions

All skills prefixed `cm-` (CodyMaster namespace). Consistent, clean.

Compare to peers:
- BMAD: named personas (Amelia, PM, Architect) — anthropomorphic
- GSD: role-based (`backend-dev`, `security-reviewer`) — functional
- gstack: specialist roles (frontend-engineer, qa-engineer) — role-based
- Superpowers: pattern tags (TDD-first, spec-driven) — methodology
- ECC: skill names (no consistent prefix) — flat namespace

→ **codymaster's `cm-` prefix is the most consistent namespace** in T1. Helpful for discoverability + conflict avoidance with other frameworks.

## 9. Commands (workflow-level) — brief inventory

| File | Likely purpose (inferred from name) |
|------|--------------------------------------|
| bootstrap.md | Initialize a new codymaster-enabled project |
| build.md | Trigger build/compile workflow |
| content.md | Content factory workflow (ads/marketing content) |
| continuity.md | Save/restore cross-session context |
| debug.md | Debug workflow |
| demo.md | Generate demo/preview |
| deploy.md | Safe-deploy pipeline workflow |
| plan.md | Planning workflow (sprint/quarter) |
| review.md | Code review workflow |
| track.md | Status/progress tracking |
| ux.md | UX workflow (design system, preview) |

**Observations:**
- Covers major lifecycle stages (plan, build, review, deploy, ux, content)
- Missing: idea, monitor, learn, security (these likely live as CLI verbs `cm <verb>` not workflow commands)
- `continuity.md` surfaces cross-session memory as user-facing command — unique

## 10. Dependency on `cm` CLI

From package.json:
- `bin: { cm: dist/index.js, codymaster: dist/index.js }` — dual alias
- CLI entry = TypeScript compiled to JS
- Dependencies: @clack/prompts (interactive), better-sqlite3 (Smart Spine backing), chalk (terminal color), chokidar (file watcher), commander (CLI framework), express (web dashboard?), prompts, yaml

### Implications
- `cm` CLI must be installed (`npm install -g codymaster`) for many workflows
- Not pure-Markdown like BMAD — has binary runtime
- SQLite = actual local database, not Markdown files. More DB-backed than peers.

**Contrast with T1 peers:**
- BMAD: natural-language markdown core (no code)
- GSD: markdown + TS workflow
- gstack: TypeScript roles
- codymaster: **TypeScript + SQLite backing + markdown skills on top** — most engineered runtime in T1

## 11. Install surface

Install commands + what they give you:

| Method | Installs | Scope |
|--------|----------|-------|
| `claude plugin marketplace add tody-agent/codymaster` | Claude Code CLI | Per-environment |
| Claude Desktop Plugin marketplace | Claude Desktop | Per-environment |
| `/add-plugin cody-master` | Cursor | Per-editor |
| `gemini extensions install https://github.com/tody-agent/codymaster` | Gemini CLI | Per-environment |
| `npm install -g codymaster` | Global `cm` binary | All projects |
| `npm install codymaster` | Per-project `cm` | Single project |
| OpenCode/OpenClaw/Codex/Antigravity | Per platform docs | Varies |

**8+ platforms is real** — each install path actually works (per README instructions).

## 12. Cross-references

- [[(C) README + VN summary]] — positioning + scale reality-check
- [[(C) Novel Primitives cluster summary]] — Brain/Smart Spine/CodeGraph behind these skills
- [[(C) 79 Skills 8 Domains + 11 Commands Architecture]] — entity page (Phase 3)

## Open questions surfaced

- Why 79 skills not 60+? Reserve discipline or stale doc? (Q2 existing)
- Which `commands/` vs CLI verbs count is authoritative? (Q3 existing)
- cm-autopilot — does it actually autopilot, or curated workflow? (new — Q30)
- cm-reactor — name unclear; what is Reactor? (new — Q31)
- cm-codeintell = CodeGraph backing skill; how does it cache? (new — Q32)

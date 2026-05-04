# GSD (Get Shit Done) — Hướng dẫn cho người mới

> **For team / Cho team:** Đây là hướng dẫn để bắt đầu với **GSD** — "meta-prompting, context engineering and spec-driven development system" cho 14+ AI coding harnesses. Đọc 1 lần ~30 phút, đủ để cài đặt + chạy 1 phase end-to-end.
>
> **Tác giả wiki:** Storm Bear, dựa trên `gsd-build/get-shit-done` (v1.37.1+, 2026-04-17).
> **Ngày:** 2026-04-18 | **Phiên bản:** v1
> **Song ngữ:** Tiếng Việt (chính) + English (technical terms)
>
> **Note:** GSD không có VN translation official (4 langs: en/pt-BR/zh-CN/ja-JP/ko-KR). Storm Bear wiki là VN-first reference đầu tiên.

---

## 📋 Mục lục

1. [Tại sao đọc cái này](#tại-sao-đọc-cái-này)
2. [Part 1: GSD là gì + "Context rot"](#part-1-gsd-là-gì--context-rot)
3. [Part 2: 5-Step Workflow](#part-2-5-step-workflow)
4. [Part 3: 33 Agents + 83 Commands overview](#part-3-33-agents--83-commands-overview)
5. [Part 4: Setup roadmap 1 tuần](#part-4-setup-roadmap-1-tuần)
6. [Part 5: Unique features (Spike/Sketch/Seeds/Threads/Workstreams)](#part-5-unique-features)
7. [Part 6: Compare với 3 siblings Tier 1](#part-6-compare-với-3-siblings-tier-1)
8. [Part 7: FAQ](#part-7-faq)
9. [Part 8: Resources](#part-8-resources)

---

## Tại sao đọc cái này

### Ai nên đọc / Who should read

- **Dev muốn spec-driven development** nhưng ghét BMAD/Speckit overhead
- **Solo developer / small team** ship volume cao qua Claude Code (or 14 other harnesses)
- **Team lead** đang evaluate 4 Tier 1 frameworks (cần đọc sibling guides + 4-way comparison)
- **Anyone** đang gặp "context rot" — agent quality degrade mid-session

### Bạn sẽ có gì

- Hiểu "**context rot**" và 4-mechanism GSD solution
- Nắm **5-step workflow** (discuss/plan/execute/verify/ship)
- Biết **33 agents + 83 commands** (overview, không memorize)
- **Setup roadmap 1 tuần** từ zero → ship first phase
- Compare với 3 siblings Tier 1 → decide nếu GSD fit bạn

### Không phải là gì

- ❌ Tutorial Claude Code từ đầu
- ❌ Deep dive từng command trong 83
- ❌ Advanced topics: SDK usage, custom hooks
- ❌ Tokenomics của $GSD Solana token

---

## Part 1: GSD là gì + "Context rot"

### TL;DR

**GSD (Get Shit Done)** là **Tier 1 agent-as-assistant framework** cho 14+ AI coding harnesses. Do TÂCHES (solo developer, tên X tag `@gsd_foundation`) build. **MIT license**. Distribution qua npm: `npx get-shit-done-cc@latest`.

**Backed by:**
- `$GSD` Solana token + gsd_foundation
- Discord community
- "Trusted by engineers at Amazon, Google, Shopify, Webflow" claim

### Core positioning: "Solves context rot"

Đây là **unique framing** — 3 siblings Tier 1 không explicitly name this problem:

> "Context rot — the quality degradation that happens as Claude fills its context window."

**Without GSD:**
```
Session start (0% context)
  ↓
Read files, tool calls, responses (context fills)
  ↓
Context at 180k/200k
  ↓
Claude says "I'll be more concise now" ← rot starts
  ↓
Claude forgets earlier constraints
  ↓
Output = inconsistent garbage
```

**With GSD (4 mechanisms):**

1. **File-structured context engineering** — `.planning/` files với size budgets
2. **XML prompt formatting** — precision vs markdown ambiguity
3. **Fresh 200k per subagent** — orchestrator stays light (30-40%), work offloaded
4. **Runtime context monitor hook** — `gsd-context-monitor.js` detects approaching threshold

→ **Đọc sâu:** [[../02 Wiki/(C) Context Rot Solution]]

### Author voice: TÂCHES

```
"I'm a solo developer. I don't write code — Claude Code does."

"Other spec-driven development tools exist; BMAD, Speckit... But they all seem
to make things way more complicated than they need to be. I'm not a 50-person
software company. I don't want to play enterprise theater. I'm just a creative
person trying to build great things that work."

"That's what this is. No enterprise roleplay bullshit. Just an incredibly
effective system for building cool stuff consistently using Claude Code."
```

→ **Anti-enterprise-theater positioning.** Similar attitude to gstack's Garry Tan, different framing (solo creator vs YC CEO).

---

## Part 2: 5-Step Workflow

**Mental model:** GSD = `discuss → plan → execute → verify → ship` per phase.

### Step 1: `/gsd-discuss-phase <N>`

Lock implementation preferences BEFORE planning.

System analyzes phase + identifies gray areas:
- Visual features → Layout, density, empty states
- APIs/CLIs → Response format, flags, error handling
- Content systems → Structure, tone, depth

Asks until satisfied. Output: `CONTEXT.md` feeds downstream.

**Modes:**
- `questions` (default)
- `assumptions` (reads codebase, surfaces assumptions)
- `--batch` (group questions)
- `--chain` (auto-chain to plan + execute)

### Step 2: `/gsd-plan-phase <N>`

4 parallel researchers + planner + checker loop.

```
plan-phase
  ↓
4 parallel researchers (stack + features + arch + pitfalls)
  ↓
Research synthesizer merges
  ↓
RESEARCH.md
  ↓
Planner creates 2-3 atomic XML plans
  ↓
Plan checker validates (loop if fail)
  ↓
PLAN.md files
```

### Step 3: `/gsd-execute-phase <N>`

**Wave-based parallel execution.**

```
WAVE 1 (parallel)   →   WAVE 2   →   WAVE 3
Plan 01 | Plan 02        Plan 03       Plan 04
```

- Independent plans → same wave → parallel
- Dependent plans → later wave → wait
- File conflicts → sequential

Fresh 200k context per plan. Atomic commit per task.

### Step 4: `/gsd-verify-work <N>`

**Manual UAT.** System walks you through deliverables. You verify feature actually works as expected.

Auto-diagnose failures → creates fix plans. Re-execute if needed.

### Step 5: `/gsd-ship <N>`

Create PR with auto-generated body + clean branch (filters `.planning/` commits).

### Or: `/gsd-next` auto-routing

```bash
/gsd-next
# System detects current state + runs next step
```

→ **Zero workflow memorization.** System knows.

### Quick Mode: `/gsd-quick`

For ad-hoc tasks:
```bash
/gsd-quick
> "Add dark mode toggle to settings"
```

Flags: `--discuss`, `--research`, `--validate`, `--full` (composable).

→ **Đọc sâu:** [[../02 Wiki/(C) 5-Step Workflow]]

---

## Part 3: 33 Agents + 83 Commands overview

**Scope của GSD = largest trong 4 Tier 1 frameworks:**

| Aspect | Count |
|--------|-------|
| Specialized agents | **33** (folder) / 21 (docs lag) |
| Slash commands | **83** |
| Hooks | **11** |

### Agent categories (function-based taxonomy)

- **Researchers (5):** project/phase/ui/domain/ai research
- **Analyzers (3):** assumptions, advisor, pattern mapper
- **Synthesizers (2):** research, doc
- **Planners (2):** planner, roadmapper
- **Executors (2):** executor, code-fixer
- **Checkers + Verifiers + Auditors (10):** plan/integration/ui/security/nyquist/etc.
- **Mappers + Debuggers (3):** codebase-mapper, debugger, debug-session-manager
- **Doc Writers (3):** writer, verifier, classifier
- **Profilers + Utilities (3):** user-profiler, framework-selector, intel-updater

→ **Đọc sâu:** [[../02 Wiki/(C) 33 Specialized Agents + Commands]]

### Command categories

Core: **new-project, discuss, plan, execute, verify, ship, next**

Navigation: **progress, help, update, manager**

Session: **pause-work, resume-work, session-report**

Code quality: **review, secure-phase, audit-uat, docs-update**

Spiking+Sketching: **spike, sketch, wrap-ups**

Backlog: **plant-seed, add-backlog, review-backlog, thread**

Workstreams + Workspaces: parallel milestone work

Utilities: **settings, set-profile, debug, do, note, health, stats**

Plus Brownfield: **`/gsd-map-codebase`** for existing repos.

→ Full list in [[../02 Wiki/(C) README summary]].

---

## Part 4: Setup roadmap 1 tuần

### Day 1: Install

**Interactive mode (recommended):**
```bash
npx get-shit-done-cc@latest
# Pick: Claude Code (or your harness)
# Pick: Global (all projects) or Local (current)
```

**Or non-interactive:**
```bash
npx get-shit-done-cc --claude --global
```

**Verify:**
```
/gsd-help
```

Should list all commands.

### Day 2: First phase

```bash
# In any project (new or existing)
/gsd-new-project
```

System asks questions about:
- Project goals
- Tech stack preferences
- Constraints
- Edge cases

Spawns 4 parallel researchers → creates `PROJECT.md`, `REQUIREMENTS.md`, `ROADMAP.md`.

Approve roadmap.

### Day 3: Discuss + Plan phase 1

```bash
/gsd-next   # → auto-routes to /gsd-discuss-phase 1
```

Answer gray-area questions → `CONTEXT.md`.

```bash
/gsd-next   # → auto-routes to /gsd-plan-phase 1
```

Wait for 4 parallel researchers → plans generated → plan checker validates.

Approve plan.

### Day 4: Execute + Verify

```bash
/gsd-next   # → /gsd-execute-phase 1
```

**Walk away.** Wave-based parallel execution. Each plan in fresh 200k context. Come back to completed work + clean git history.

```bash
/gsd-next   # → /gsd-verify-work 1
```

Manual UAT. Confirm each deliverable works.

### Day 5: Ship or iterate

If verify passes:
```bash
/gsd-next   # → /gsd-ship 1 (or next phase)
```

Creates PR.

If verify fails:
- System auto-generates fix plans
- Re-run `/gsd-execute-phase` với fixes

### Day 6: Explore unique features

Try:
- `/gsd-spike "Can we use library X?"` — throwaway experiment
- `/gsd-sketch "Dashboard layout variants"` — throwaway HTML mockups
- `/gsd-plant-seed "Add dark mode in phase 3"` — forward-looking idea
- `/gsd-thread debugging` — persistent context thread

### Day 7: Assess

**Success criteria:**
- ✅ Shipped 1 phase end-to-end
- ✅ Main context stayed 30-40% throughout (no context rot)
- ✅ Atomic commits trong git log
- ✅ `.planning/` structure populated correctly

**Decide:**
- GSD fits → rollout to team
- Different fit → try sibling (gstack/Superpowers/ECC) — see Part 6
- Not for current project → keep for later

---

## Part 5: Unique features

GSD có **5 unique mechanisms** trong Tier 1:

### 1. Spiking & Sketching (throwaway experiments)

**`/gsd-spike [idea]`** — run 2-5 focused experiments với Given/When/Then verdicts before planning.

**`/gsd-sketch [idea]`** — 2-3 interactive HTML mockup variants per design question.

Store in `.planning/spike-*/` or `.planning/sketch-*/`.

**Wrap-up commands** package findings into project-local skill file:
- `/gsd-spike-wrap-up` → skill cho future build conversations
- `/gsd-sketch-wrap-up` → skill cho future builds

→ **Experiments BEFORE planning, packaged INTO skills AFTER.** Unique learning loop.

### 2. Seeds (forward-looking capture)

```bash
/gsd-plant-seed "Add AI image generation in phase 5"
```

**Trigger conditions** cause seed to surface at right milestone. Not a TODO (forget-and-never-revisit) — time-aware.

### 3. Threads (persistent cross-session context)

```bash
/gsd-thread debugging
# Append context
# Next session: /gsd-thread debugging resumes where you left off
```

**Lightweight cross-session knowledge** cho work spanning multiple sessions.

### 4. Workstreams (parallel milestone work)

```bash
/gsd-workstreams create feature-a
/gsd-workstreams create feature-b
/gsd-workstreams switch feature-a
```

Namespaced parallel work within milestone. Teammates can work concurrently.

### 5. Multi-Project Workspaces

```bash
/gsd-new-workspace
# Isolated workspace với repo copies (worktrees or clones)
```

Work on multiple projects concurrently, isolated.

→ **Đọc sâu:** [[../02 Wiki/(C) 5-Step Workflow]] + [[../02 Wiki/(C) USER-GUIDE summary]]

---

## Part 6: Compare với 3 siblings Tier 1

**Quick decision matrix** (full 4-way trong [[(C) Tier 1 4-way comparison]]):

| Criterion | ECC | Superpowers | gstack | **GSD** |
|-----------|-----|-------------|--------|---------|
| **Scope** | 185 skills + 48 agents | 14 skills + 1 agent | 23 specialists + 8 tools | **33 agents + 83 commands** |
| **Workflow** | Sequential phases | 7-stage hard-gated | Sprint pipeline (smart routing) | **5-step + `/gsd-next` auto-route** |
| **Harnesses** | 5 | 7 | 10 | **14** |
| **Distribution** | Plugin + manual | Marketplace + git | Setup script + git | **`npx` npm one-liner** |
| **Core framing** | Performance optimization | Methodology (Iron Law) | Virtual team (role-based) | **"Context rot solution"** |
| **TDD** | Skill-based | Iron Law mandatory | Built into `/ship` | **Via `gsd-add-tests` command** |
| **Unique feature** | 48 specialized domain agents | 11 Rationalizations + Red Flags | Browser automation daemon | **Spike/Sketch/Seeds/Threads** |
| **Tone** | Prescriptive | Iron Law strict | Founder direct | **Anti-enterprise-theater** |
| **License** | MIT | MIT | MIT | **MIT** |
| **Token/commercial** | Plugin + paid products | None | YC recruiting | **$GSD Solana token** |
| **Best for** | Broad polyglot team | Disciplined production | Solo founder velocity | **Context rot-prone long sessions** |

### When to pick GSD over siblings

✅ **Pick GSD nếu:**
- Bạn gặp "quality drops mid-session" đều đặn
- Muốn spec-driven nhưng ghét BMAD/Speckit overhead
- Đang dùng harness ngoài Claude Code (Kilo, Windsurf, Antigravity, Augment, Trae, Qwen, etc.)
- Cần spike/sketch BEFORE planning (experiments first)
- Team value auto-routing (don't memorize stages)

❌ **Skip GSD nếu:**
- Polyglot specialized needs → ECC's 185 skills
- Value Iron Law TDD + voice discipline → Superpowers
- Founder-velocity + browser automation → gstack
- Prefer git clone vs npm → gstack `./setup`

### When to pick gstack over GSD

- Role-based mental model (CEO/Eng/Designer) intuitive hơn 5-step
- Built-in browser automation daemon
- `/retro` + `/retro global` cross-project reflection
- Garry Tan's voice resonate

### When to pick Superpowers over GSD

- Iron Law TDD non-negotiable
- Eval-driven discipline tốt hơn auto-routing
- "Your human partner" tone resonate
- Zero-dep philosophy important

### When to pick ECC over GSD

- Polyglot team cần 185 skills
- Cần specialized domain agents (security/DB/frontend)
- Mature stable ecosystem
- Enterprise security via AgentShield

→ **Full decision matrix:** [[(C) Tier 1 4-way comparison]]

---

## Part 7: FAQ

### Q1: "Context rot" có thật không?

Có. Anthropic's own research confirms context degradation với long sessions. GSD's mechanisms (file-structured engineering + fresh subagent contexts + XML precision) address empirically.

### Q2: $GSD Solana token ảnh hưởng bạn không?

**Nhóm user:** không. MIT license, tool free. Token = foundation funding mechanism. Holders ≠ gatekeepers.

**Caveat:** Commercial implications nếu token value tied to framework usage. Watch cho future pricing changes.

### Q3: 14 harnesses — tất cả equally supported?

**No.** Claude Code most tested. Others (especially Tier 2: Kilo, Windsurf, etc.) may have edge cases. Check `docs/skills/discovery-contract.md` cho canonical format.

### Q4: 83 commands — phải học hết không?

Không. Start với 7 core:
- `/gsd-new-project`
- `/gsd-next` (auto-routes everything)
- `/gsd-help`
- `/gsd-progress`
- `/gsd-quick` (ad-hoc tasks)
- `/gsd-pause-work` / `/gsd-resume-work`

Rest discover organically.

### Q5: TÂCHES là ai?

Author. Solo developer. X handle `@gsd_foundation`. GSD builder. Anti-enterprise-theater voice.

### Q6: Conflict với 3 sibling frameworks?

Yes. Skill name overlap (review/debug/ship). **Pick 1.** Can try multiple in different projects, không mix trong same repo.

### Q7: GSD có VN translation không?

Không trực tiếp. 4 langs: en, pt-BR, zh-CN, ja-JP, ko-KR.

Storm Bear's wiki = first VN reference. Potential contribution opportunity (PR VN README).

### Q8: `.planning/` commit vào git không?

**Yes.** GSD design expects `.planning/` trong git. Enables cross-session resume, team handoff, PR traceability.

**Trade-off:** noise trong repo. `/gsd-pr-branch` filters `.planning/` commits cho clean PR.

### Q9: Storm Bear nên dùng GSD không?

**Deferred decision.** Current recommendation (post-5-wiki-analysis):
- **Primary for Scrum coaching velocity:** gstack (persona match)
- **Secondary personal AI:** goclaw Lite (vault as query layer)
- **GSD:** try nếu context rot problem surfaces in practice

Pilot real use trước (Option A trong v3+v4 iteration logs).

### Q10: Integration với siblings?

Không explicit. Không giống goclaw's ACP provider (which spawns Claude Code với gstack skills).

**Potential:** GSD's skills format = Anthropic-compatible → import into Claude Code alongside other frameworks. But skill name collisions.

---

## Part 8: Resources

### Repo + docs

- **Repo:** https://github.com/gsd-build/get-shit-done
- **npm:** https://www.npmjs.com/package/get-shit-done-cc
- **Discord:** https://discord.gg/mYgfVNfA2r
- **X / Twitter:** https://x.com/gsd_foundation
- **$GSD Token:** https://dexscreener.com/solana/...
- **Docs in repo:** `docs/USER-GUIDE.md`, `docs/ARCHITECTURE.md`, `docs/AGENTS.md`, `docs/FEATURES.md`, `docs/CONFIGURATION.md`, `docs/COMMANDS.md`

### Wiki Storm Bear (đọc sâu)

- [[../02 Wiki/(C) README summary]]
- [[../02 Wiki/(C) USER-GUIDE summary]]
- [[../02 Wiki/(C) ARCHITECTURE + CHANGELOG summary]]
- [[../02 Wiki/(C) Context Rot Solution]]
- [[../02 Wiki/(C) 5-Step Workflow]]
- [[../02 Wiki/(C) 33 Specialized Agents + Commands]]
- [[../02 Wiki/(C) 14-Harness npm Distribution]]
- [[(C) Tier 1 4-way comparison]] — ECC vs Superpowers vs gstack vs GSD

### Sibling wikis

- ECC: `../../Everything Claude Code - Beginner Analysis/02 Wiki/(C) index.md`
- Superpowers: `../../Superpowers - Beginner Analysis/02 Wiki/(C) index.md`
- gstack: `../../gstack - Beginner Analysis/02 Wiki/(C) index.md`
- goclaw (Tier 2): `../../goclaw - Beginner Analysis/02 Wiki/(C) index.md`

### Reference docs mentioned in GSD

- `docs/skills/discovery-contract.md` — canonical skill format
- `docs/manual-update.md` — non-npm install paths
- `references/doc-conflict-engine.md` — used by /gsd-ingest-docs + /gsd-import

### Community + related

- SpecKit, OpenSpec, Taskmaster (explicit competitors referenced by TÂCHES)
- Karpathy's LLM Wiki pattern (Storm Bear vault's founding principle)
- Discord community
- YC Office Hours concept (gstack parallel)

### Khi gặp issue

- **Install fails:** `npx get-shit-done-cc --claude --global --sdk` (force SDK install)
- **Commands not found:** check harness version + verify `.claude/skills/` or `commands/gsd/` populated
- **Workflow stuck:** `/gsd-forensics`
- **`.planning/` corrupted:** `/gsd-health --repair`
- **Session lost:** `/gsd-resume-work`
- **Context rot symptoms:** `/gsd-pause-work` → fresh session → `/gsd-resume-work`
- **Update issues:** `npx get-shit-done-cc@latest` (re-run installer)

---

## Closing thoughts — GSD's place trong ecosystem

GSD là **4th Tier 1 entrant** trong Storm Bear analysis. Fills specific niche:
- **Most harnesses** (14) = broadest reach
- **Most commands** (83) = comprehensive but risk overwhelm
- **Context rot specific framing** = resonates with devs suffering this pain
- **Anti-enterprise-theater tone** = solo developer cultural match

**Trade-offs:**
- + npm distribution friction-low
- + 33 specialized agents function-organized
- + Workstreams + Workspaces + Seeds + Threads unique
- - 83 commands = learning cliff for comprehensive use
- - Docs lag behind code (33 vs 21 agents)
- - No official VN support
- - $GSD token future implications unclear

**Storm Bear takeaway:**
Don't default-install. Evaluate:
1. Do you suffer context rot concretely?
2. Do you prefer auto-routing (`/gsd-next`) over explicit stages?
3. Do you value spec-driven với spike/sketch before planning?

3 YES → pilot GSD 1 week.

**Otherwise:** stick với current pick (gstack recommendation from v4).

---

> **Wiki maintained by Storm Bear.** GSD = 5th LLM Wiki project trong vault. Nếu thấy fact sai hoặc outdated (aggressive development), ping để fix.

# (C) Skills Library — Entity Page

> **Type:** Building block #2 — primary content of Superpowers
> **Status:** Second entity page
> **Sources:** 5 — README, brainstorming/SKILL.md, test-driven-development/SKILL.md, CLAUDE.md, ls verification
> **Last updated:** 2026-04-18

---

## Một câu / One-liner

**VI:** 14 carefully-curated skills là **primary content** của Superpowers — mỗi skill là markdown file với frontmatter description trigger, body workflow + anti-pattern tables + hard gates. Quality-over-quantity philosophy: 14 skills (vs ECC 185) nhưng mỗi skill **eval-tested + adversarial pressure tested + non-removable carefully-tuned content**.

**EN:** 14 carefully-curated skills are the **primary content** of Superpowers — each is a markdown file with frontmatter description trigger, body workflow + anti-pattern tables + hard gates. Quality-over-quantity philosophy.

---

## Khi nào dùng / Khi nào KHÔNG dùng

### ✅ Dùng skill khi:
- Workflow lặp lại với pattern rõ ràng
- Cần enforce specific behavior (TDD, brainstorm-first, etc.)
- Multi-step process mà order matters
- Cần document anti-patterns + rationalizations cùng lúc với workflow

### ❌ KHÔNG dùng skill khi:
- One-off task không tái dùng (overkill)
- Logic mechanical/format-only (dùng hook thay)
- Domain-specific (per CLAUDE.md, không add core — own plugin)
- Customization team-specific (không belong in core)

---

## Skill vs Hook vs Agent vs Command (chọn cái nào?)

| Tiêu chí | Skill | Hook | Agent | Command |
|----------|-------|------|-------|---------|
| **Scope trong Superpowers** | 14 skills (PRIMARY) | 1 (session-start only) | 1 (code-reviewer only) | 3 (all DEPRECATED) |
| **Trigger** | Description match (auto) | SessionStart event | Invoked by skills | User `/cmd` (legacy) |
| **Reasoning** | ✅ Full agent inference | ❌ Mechanical | ✅ Full | Limited |
| **Modify per-project** | ❌ Don't modify core | ✅ Customize | ❌ | Deprecated |
| **Enforcement** | Hard gates + Iron Laws | None | Soft (skill invokes) | Soft |
| **Status** | ✅ Primary surface | Minimal | Single specialist | ❌ Going away |

> **Quy tắc Superpowers:** Almost everything là skill. Hook minimal. Agent rare. Command going away.

---

## 14 Skills — categorized

> Verified bằng `ls skills/` (2026-04-18) = **14 directories** (matches README description, not 13 listed).

### Testing (1 skill)

| Skill | Purpose |
|-------|---------|
| `test-driven-development` | RED-GREEN-REFACTOR cycle, Iron Law enforcement, 372-line skill including testing anti-patterns reference |

### Debugging (2 skills)

| Skill | Purpose |
|-------|---------|
| `systematic-debugging` | 4-phase root cause process. Includes root-cause-tracing, defense-in-depth, condition-based-waiting techniques |
| `verification-before-completion` | Ensure it's actually fixed (not just appears fixed) |

### Collaboration (8 skills) — largest category

| Skill | Purpose | Stage |
|-------|---------|-------|
| `brainstorming` | Socratic design refinement, save spec doc | Stage 1 |
| `writing-plans` | Detailed implementation plans (bite-sized 2-5 min tasks) | Stage 3 |
| `executing-plans` | Batch execution với checkpoints (fallback when no subagent) | Stage 4 alternative |
| `subagent-driven-development` | Fast iteration với two-stage review (preferred) | Stage 4 primary |
| `dispatching-parallel-agents` | Concurrent subagent workflows | Stage 4 advanced |
| `requesting-code-review` | Pre-review checklist | Stage 6 |
| `receiving-code-review` | Responding to feedback | After Stage 6 |
| `using-git-worktrees` | Parallel development branches | Stage 2 |
| `finishing-a-development-branch` | Merge/PR/keep/discard decision | Stage 7 |

> **Note:** README lists 9 collaboration skills nhưng folder has 8. Discrepancy — `subagent-driven-development` listed twice in README (under "executing-plans or **subagent-driven-development**" + standalone) likely overcounted.

### Meta (2 skills)

| Skill | Purpose |
|-------|---------|
| `writing-skills` | Create new skills theo best practices (eval methodology, testing) |
| `using-superpowers` | Introduction to skills system + tool mappings per harness |

### Observed actual count

Verified `ls skills/` returned 14 directories. README's categorization sum:
- Testing: 1
- Debugging: 2
- Collaboration: 8 (deduplicating)
- Meta: 2

**Total: 13** in README. Folder count: 14. Discrepancy explanation: Likely `subagent-driven-development` is listed standalone in README's collaboration section AND folder, making 14 actual. Worth verify in next ingest.

---

## Anatomy: A Skill File trông như thế nào / What a skill file looks like

### Minimal frontmatter (per agentskills.io spec)

Per CLAUDE.md (v5.0.6 fix from PR #882):
> "writing-skills — corrected false claim that SKILL.md frontmatter supports 'only two fields'; now says 'two required fields' and links to the agentskills.io specification for all supported fields"

**2 required fields:**
- `name`
- `description`

**Other fields per spec:** `model`, additional metadata.

### Full skill structure (observed pattern)

```markdown
---
name: test-driven-development
description: Use when implementing any feature or bugfix, before writing implementation code
---

# Test-Driven Development (TDD)

## Overview
[2-4 sentences core principle]

## When to Use
**Always:**
- [list]

**Exceptions (ask your human partner):**
- [list]

## The Iron Law
```
[Non-negotiable rule, ALL CAPS]
```

## Red-Green-Refactor (or main process)
[Detailed steps with code examples]

## Good Tests / Bad Tests (with examples)
<Good>
[code]
</Good>

<Bad>
[code]
</Bad>

## Why Order Matters / Reasoning sections
[Counter-arguments to common excuses]

## Common Rationalizations
| Excuse | Reality |
| ... | ... |

## Red Flags - STOP and Start Over
[List of warning signs]

## Example: [Concrete walkthrough]

## Verification Checklist
- [ ] Item 1
- [ ] Item 2

## When Stuck
| Problem | Solution |
| ... | ... |

## Related Integration sections (cross-skill references)

## Final Rule
[Reinforce Iron Law]
```

### Special elements observed

| Element | Purpose | Example |
|---------|---------|---------|
| `<HARD-GATE>...</HARD-GATE>` | Non-bypassable boundary | `brainstorming` Stage 1 hard gate |
| `<Good>...</Good>` / `<Bad>...</Bad>` | Code example contrast | TDD skill |
| `<SUBAGENT-STOP>` | Skip skill when running as subagent | `using-superpowers` (v5.0.0) |
| ALL-CAPS Iron Laws | Non-negotiable rules | "NO PRODUCTION CODE WITHOUT A FAILING TEST FIRST" |
| Common Rationalizations table | Counter-excuse training | TDD, brainstorming |
| Red Flags table | Self-detection patterns | TDD (13 patterns) |
| Graphviz `digraph` blocks | Visual process flow | TDD, brainstorming |

---

## Cơ chế / How It Works

### Skill auto-trigger flow

```
User input arrives
    ↓
Agent reads context + assesses intent
    ↓
For each available skill:
  Match skill description against intent
  Check trigger keywords ("MUST use", "before any X", action verbs)
    ↓
If match found:
  Inject skill SKILL.md into context
  Apply hard gates (block alternative paths)
  Follow workflow + checklist + process flow
    ↓
Execute workflow:
  - Step 1, 2, 3...
  - Self-review checks
  - Anti-pattern detection
    ↓
Stage transition:
  Skill body specifies "transition to writing-plans" etc.
  Next skill activates
```

### Cross-skill orchestration

Skills reference other skills explicitly:
- `brainstorming` ends with: "Invoke writing-plans skill"
- `writing-plans` invokes `subagent-driven-development`
- `subagent-driven-development` invokes `test-driven-development` per task
- All review skills can invoke `code-reviewer` agent

→ Skill graph emerges, not flat.

### Subagent context isolation (v5.0.2)

When skill dispatches subagent (e.g., `subagent-driven-development` per task):
- Subagent receives **only context it needs**
- Prevents context window pollution
- Match ECC's "Iterative Retrieval Pattern"

---

## Configuration

### Modify skill behavior

**Per CLAUDE.md, this is restricted:**
> "PRs that restructure, reword, or reformat skills to 'comply' with Anthropic's skills documentation will not be accepted without extensive eval evidence showing the change improves outcomes."

**Officially supported:**
- Use `superpowers:writing-skills` skill to develop changes
- Adversarial pressure testing across multiple sessions
- Show before/after eval results

**Not supported (will be rejected):**
- Modify Red Flags tables casually
- Modify Rationalizations lists casually
- Change "your human partner" terminology
- Restructure Iron Law framing

### Override per-project

**Per CLAUDE.md (v5.0.0 instruction priority):**
> "If CLAUDE.md or AGENTS.md says 'don't use TDD' and a skill says 'always use TDD,' the user's instructions win."

**Practical:**
```markdown
# Project CLAUDE.md
For this prototype, skip TDD and brainstorming. We're exploring.
```

→ Skills respect, defer to user instruction.

### Add custom skill

**Per CLAUDE.md, custom skills don't belong in core:**
> "Skills, hooks, or configuration that only benefit a specific project, team, domain, or workflow do not belong in core. Publish these as a separate plugin."

**Process:**
1. Create new plugin folder (own repo)
2. Use `writing-skills` skill to draft SKILL.md
3. Test với adversarial pressure
4. Distribute via own marketplace

---

## Recipes

### Recipe 1: Use existing skill (typical)

User just uses superpowers normally — skills auto-trigger qua description matching. No setup needed beyond install.

```bash
/plugin install superpowers@claude-plugins-official
# Done — skills auto-active
```

### Recipe 2: Override skill cho project (rare)

```markdown
# In project's CLAUDE.md
This project uses Pytest, not Vitest. TDD skill should suggest pytest commands instead of npm test.

# Or even more direct:
For experimental playground only — skip Stage 1 brainstorming.
```

→ Skills auto-respect.

### Recipe 3: Build own skill (own plugin)

```bash
# Use writing-skills meta-skill
"I want to write a skill for our team's [specific workflow]"
```

→ `writing-skills` skill walks through anatomy + eval requirements.

### Recipe 4: Skip skill mid-execution (with consent)

User: *"I know TDD says delete code, but for this exploration I want to keep it. Permission granted."*

→ Per Iron Law's exception clause: *"No exceptions without your human partner's permission."*

---

## Patterns kết hợp / Combination patterns

### Skill + Skill (chain)

Skills explicitly handoff. Stage transitions via "Invoke X skill":
- brainstorming → writing-plans → SDD → TDD → code review → finishing
- Forms 7-stage workflow.

### Skill + Hook (minimal in Superpowers)

Only `session-start` hook → injects bootstrap context (using-superpowers reference). Hook doesn't trigger skills, just provides initial agent awareness.

### Skill + Subagent (context isolation)

Per v5.0.2 cross-skill principle. Skill dispatches subagent with **minimal context**:
- Subagent gets task + relevant skill content only
- Doesn't get full main conversation
- Prevents pollution

### Skill + agent (single specialist)

Only `code-reviewer` agent. Invoked by `requesting-code-review` skill. Provides specialized review behavior.

### Skill + custom CLAUDE.md (override)

User instructions trump skill defaults (v5.0.0 priority hierarchy). Use cho project-specific deviations.

---

## Anti-patterns / Sai lầm hay gặp

1. **Modify "your human partner" → "the user"** — deliberate terminology, will be rejected. Per CLAUDE.md.
2. **Add domain-specific skill to core** — portfolio building, prediction markets, games → standalone plugin only.
3. **Add third-party dependency to skill** — zero-dependency by design. Will be rejected.
4. **Restructure skill to "comply" với Anthropic guidance** — Superpowers' philosophy DIFFERS deliberately. Need eval evidence.
5. **Skip carefully-tuned tables** (Red Flags, Common Rationalizations) — these are eval-tested. Don't trim.
6. **Treat skill as documentation** — it's behavior-shaping code. Test changes adversarially.
7. **Skip self-review steps** — v5.0.6 lesson: 30s self-review catches 3-5 bugs vs 25 min subagent review with same defect rate.
8. **Use deprecated commands** instead of skills — `/brainstorm`, `/write-plan`, `/execute-plan` removing in next major.
9. **Skip HARD-GATE blocks** — designed non-bypassable. If you find way around, that's a skill bug to file.
10. **Bulk modify multiple skills in 1 PR** — one problem per PR rule. Bulk = closed.

---

## Skills count cross-project comparison

| Aspect | Superpowers | ECC |
|--------|-------------|-----|
| **Skills count** | **14** | **185** |
| Categories | 4 (Testing, Debugging, Collaboration, Meta) | 12+ (per language, per framework, etc.) |
| Skill complexity | Deep (TDD = 372 lines) | Variable (some simple, some deep) |
| Curation level | Aggressive (eval gates, hard quality bar) | Inclusive (community + ECC core) |
| Acceptance new skill | "Würöuld this benefit completely different project type?" → if no, reject | More inclusive |
| Update process | Eval evidence required | Less stringent |
| Domain-specific OK? | ❌ Own plugin only | ✅ Many domains in core |
| Self-similar (per-language) | ❌ One TDD skill total | ✅ Per-language (django-tdd, python-testing, etc.) |

> **Insight:** Superpowers' 14 skills là **deliberate architectural constraint**. ECC's 185 skills là **inclusive ecosystem**. Different philosophies, both valid.

---

## Tools liên quan / Related Tools

| Tool | Purpose |
|------|---------|
| `writing-skills` skill | Meta-skill cho creating new skills |
| `using-superpowers` skill | Bootstrap + tool mappings per harness |
| Skill `description` field | Auto-trigger mechanism |
| `<HARD-GATE>` XML tags | Non-bypassable boundary marker |
| Common Rationalizations tables | Anti-excuse training |
| Red Flags tables | Self-detection patterns |
| Graphviz `digraph` | Visual process flow embed |
| agentskills.io specification | Frontmatter standard |

---

## Cross-references

- [[(C) The 7-Stage Workflow]] — uses 7-9 skills sequentially
- [[(C) Subagent-Driven Development]] — Stage 4 deep dive
- [[(C) Distribution Model]] — how skills ship across 7 harnesses
- [[(C) Philosophy and Contribution Culture summary]] — eval discipline + carefully-tuned content
- [[(C) Release Notes overview]] — v5.0.6 review loop optimization
- [[(C) README summary]] — skills overview
- ECC sister: `03 Projects/Everything Claude Code - Beginner Analysis/02 Wiki/(C) Skills.md` — ECC's 185 skills entity page
- [[(C) index]]

## Citations

- `00 Sources/superpowers/skills/test-driven-development/SKILL.md` (full file, 372 lines)
- `00 Sources/superpowers/skills/brainstorming/SKILL.md` (lines 1–100)
- `00 Sources/superpowers/CLAUDE.md` (full file, contributor guidelines context)
- `00 Sources/superpowers/README.md`, lines 137–162 (skills library list)
- `00 Sources/superpowers/RELEASE-NOTES.md`, v5.0.6 (review loop optimization)
- Verified count: `ls skills/ | wc -l` = 14 dirs (2026-04-18)
- agentskills.io specification (referenced)

---

## TODO cho lần ingest tiếp

- [ ] Verify exact 14 skills (one possibly hidden in README double-count)
- [ ] Read `writing-skills/SKILL.md` for eval methodology
- [ ] Read `using-superpowers/SKILL.md` for harness tool mappings
- [ ] Read `systematic-debugging/SKILL.md` cho 4-phase debug process
- [ ] Sample 1 collaboration skill not yet read (e.g., `requesting-code-review`)
- [ ] Find references/anti-patterns files mentioned in skills (`@testing-anti-patterns.md`)

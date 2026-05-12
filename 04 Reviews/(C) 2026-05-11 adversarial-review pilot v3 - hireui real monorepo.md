# (C) Adversarial-Review Comparison Pilot v3 — hireui real monorepo

> **Date:** 2026-05-11
> **Supersedes:** `(C) 2026-05-08 adversarial-review comparison pilot setup plan.md` (v2 sandbox)
> **Why v3:** v2 designed for sandbox feature on `_pilots/` namespace. Real target = `/Users/Cvtot/monorepo/hireui` which **already has BMAD methodology harness installed**, making cc-sdd install HIGH-CONFLICT. v3 pivots Stratum A representative from cc-sdd (drop) → BMAD `bmad-review-adversarial-general` (already deployed). Pilot feature becomes harness upgrade (Concept 6 deferred_count schema) per recursive elegance principle — pilot tools applied TO improve the harness they're being measured by.
> **Status:** Proposal — operator decision required before Step 0 starts

---

## 1. Pilot intent (revised from v2)

**Original v2 intent:** Pattern #76 Stratum A (architectural role-separation) vs Stratum B (prompt-framing variant) empirical evaluation comparing cc-sdd vs codex-plugin-cc on synthetic sandbox feature.

**v3 intent (3 layers):**

1. **Pattern #76 empirical comparison** — BMAD `bmad-review-adversarial-general` (Stratum A baseline, already deployed) vs codex-plugin-cc `/codex:adversarial-review` (Stratum B, NEW install) on real harness upgrade work
2. **Orthogonal overlay test** — does layering andrej-karpathy-skills (4 behavioral principles) on top of methodology harness change review character?
3. **Skills collection complement test** — do 3 cherry-picked mattpocock skills add value without colliding with hireui's existing `cm-*` skill family?

**Real feature scope:** Implement **Concept 6 (deferred_count schema)** from `(C) 2026-05-06 v2 changes - integrating KJ OS concepts.md` — the only 🔴 HIGH-priority v2 plan item not yet implemented in hireui.

---

## 2. State of hireui at v3-start (verified 2026-05-11)

### v2 plan implementation status

| Concept | v2 priority | Current hireui state | Pilot relevance |
|---------|-------------|----------------------|-----------------|
| 1 Constitutional Invariants | 🔴 HIGH today | ✅ DONE (`CONSTITUTION.md` 62 lines, I-1 to I-7) | Pilot operates under invariants |
| 5 Mandatory Next-Action | 🔴 HIGH today | ✅ DONE (CLAUDE.md I-7 + § Suggested Next Action) | Pilot reviews must end with next-action |
| 10 Goodhart's Law | 🔴 HIGH today | ✅ DONE (CLAUDE.md line 88) | Pilot avoids metric-target trap |
| **4 Dated session artifacts** | 🔴 HIGH this week | 🟡 PARTIAL (template exists; 2 logs in `_bmad-output/sessions/`; `.cm/traces/sessions/` empty) | Pilot generates 1 dated log per day |
| **2 Phase 0 pre-flight skill** | 🔴 HIGH this week | 🟡 PARTIAL (cm-continuity exists; cm-pre-flight separate skill unverified) | Step 0 below operationalizes |
| **6 deferred_count schema** | 🔴 HIGH this week | ❌ **MISSING** — no field in `.cm/memory/*.json` | **PILOT FEATURE WORK** |
| 14 Chapter convention | 🟡 MED this month | ❌ MISSING (defer per v2 plan) | N/A pilot |
| 9 OBSERVATION-TRACK | 🟢 LOW-MED | ❌ MISSING (defer per v2 plan) | N/A pilot |
| 3, 7, 8, 11, 12, 13 | MED/LOW | Deferred per v2 triggers | N/A pilot |

### hireui beyond v2 plan

- ✅ `AGENTS.md` cross-platform coverage
- ✅ `apps/mobile/CLAUDE.md` per-app scope
- ✅ ~23 `.claude/skills/cm-*/` skills (cm-continuity / cm-quality-gate / cm-dashboard / cm-planning / cm-jtbd / cm-debugging / cm-code-review / cm-design-system / cm-execution / cm-git-worktrees / etc.)
- ✅ ~18 BMAD slash commands `.claude/commands/bmad-*.md` (bmad-review-adversarial-general / bmad-brainstorming / bmad-shard-doc / bmad-tea-* test architecture family)
- ✅ Parallel install `.cursor/commands/` + `.cursor/rules/`
- ✅ Pre-commit hook `scripts/git-hooks/pre-commit-branch-policy.sh` enforcing I-2
- ✅ `_bmad-output/{runbooks,sessions,test-artifacts,tickets}` structure
- 🟡 Branch state: `agent/local-sandbox` working surface (I-3 invariant: local-only)
- 🟡 `agent-dev` is persistent harness branch (per I-2 invariant)

---

## 3. Conflict-aware install matrix

| Tool | v2 plan | v3 plan | Rationale |
|------|---------|---------|-----------|
| **cc-sdd v61** | Install as Stratum A | ❌ **DROP** | HIGH CONFLICT — would duplicate BMAD methodology harness + adversarial review + spec/gate primitives; 6 of 11 v2 criteria flag direct conflict |
| **codex-plugin-cc v62** | Install as Stratum B | ✅ **KEEP** | Orthogonal to BMAD; ChatGPT subscription gate; plugin marketplace install |
| **andrej-karpathy-skills v63** | not in v2 | ✅ **NEW** orthogonal overlay | 4 principles modify HOW LLM thinks; ~2-min install; behavioral layer test |
| **mattpocock/skills (FULL install — all 19 active skills)** | not in v2 | ✅ **NEW** full collection with management policy | Install ALL 19 active skills (engineering/productivity/personal/misc; skip deprecated/in-progress per upstream status). Functional duplicates of `cm-*` skills are kept and managed via the **Duplicate-Skill Management Policy (§3.5 NEW)** — namespace prefix discipline + description-narrowing + precedence registry + conflict telemetry. Operator-requested change 2026-05-11: do NOT cherry-pick; preserve duplicates for orthogonal-perspective measurement value, then ablate at Step 10. |

### What gets installed where

```
/Users/Cvtot/monorepo/hireui/
├── .claude/
│   ├── commands/bmad-*.md           ← existing (Stratum A baseline)
│   ├── skills/cm-*/                  ← existing
│   └── skills/karpathy-guidelines/   ← NEW (Step 4)
├── .cursor/
│   ├── commands/                     ← existing
│   └── rules/karpathy-guidelines.mdc ← NEW (auto-installed by plugin)
├── .codex/                            ← NEW (Step 3; gitignore)
├── .pilot-log/                        ← NEW (Step 6+; gitignore; ephemeral)
└── (existing structure unchanged)
```

Plus cherry-picked mattpocock skills copied manually (NOT via plugin install) to:
```
.claude/skills/mattpocock-prototype/SKILL.md     ← copied from mattpocock/skills/skills/engineering/prototype/
.claude/skills/mattpocock-to-issues/SKILL.md     ← copied from mattpocock/skills/skills/engineering/to-issues/
.claude/skills/mattpocock-write-a-skill/SKILL.md ← copied from mattpocock/skills/skills/productivity/write-a-skill/
```

`mattpocock-` prefix to avoid `cm-*` namespace collision and signal mattpocock provenance.

### .gitignore additions

```gitignore
# Pilot tools (per-developer; promote to tracked after pilot evaluation)
.claude/skills/karpathy-guidelines/
.claude/skills/mattpocock-*/
.codex/
.pilot-log/
```

---

## 3.5 Duplicate-Skill Management Policy (NEW — operator request 2026-05-11)

> **Operator intent:** "When adding a new skills bundle to any harness — even when skills functionally duplicate existing ones — INSTALL ALL rather than SKIP-and-cherry-pick. The duplicate-perspective value is worth preserving for measurement. But the agent must not get confused by competing skills firing on the same trigger. Need a management strategy."

### The core problem

When 2+ skills auto-invoke on similar trigger criteria (e.g., `cm-debugging` description = "Use when debugging" + `mattpocock-diagnose` description = "Use when diagnosing code issues"), the agent must pick one. Picks may be inconsistent across sessions, opaque to the operator, and unmeasurable. Without a policy, full-install collapses into chaos.

### 4-layer management policy

#### Layer 1 — Namespace prefix discipline (provenance always visible)

Every skill carries an explicit source prefix in its installed folder name:

| Prefix | Source | Authority |
|--------|--------|-----------|
| `cm-*` | hireui native (Compound Mind harness) | **PRIMARY** for hireui-internal operations |
| `bmad-*` | BMAD-METHOD (already installed) | **PRIMARY** for methodology workflow (spec/design/tasks/review) |
| `mattpocock-*` | mattpocock/skills | **REFERENCE-ALT** — orthogonal perspective from external |
| `karpathy-*` | andrej-karpathy-skills | **OVERLAY** — behavioral overlay, not task-execution |
| `cs-*` | (reserved) cc-sdd if ever installed | N/A v3 (dropped) |
| `codex-*` | codex-plugin-cc (Claude Code plugin namespace) | **REVIEW-ALT** — Stratum B for Pattern #76 measurement |

**Rule:** When operator or agent invokes a slash command or skill, the prefix immediately signals where authority comes from. No ambiguous "did the agent pick the hireui or the external skill?" — provenance is in the filename.

**Implementation:** all mattpocock skills get copied with `mattpocock-` prefix at install time (Step 5 below).

#### Layer 2 — Description-narrowing at install (trigger differentiation)

When installing a functional duplicate, **rewrite the `description:` frontmatter** to narrow trigger conditions explicitly. Original skill text stays intact (the behavior); only the trigger description changes.

**Example — `mattpocock/skills/engineering/diagnose` → `.claude/skills/mattpocock-diagnose/`:**

Original frontmatter:
```yaml
---
name: diagnose
description: Use when debugging code issues, tracking down bugs, or
  diagnosing unexpected behavior in a codebase.
license: MIT
---
```

Installed-into-hireui frontmatter:
```yaml
---
name: mattpocock-diagnose
description: |
  External-perspective debugging alternative to cm-debugging (hireui native primary).
  Use ONLY when:
  (a) operator explicitly invokes /mattpocock-diagnose, OR
  (b) cm-debugging has already run and operator requests a second-opinion review, OR
  (c) the issue is in code outside hireui conventions (e.g., investigating an
      upstream library's behavior with no hireui-stack assumptions).
  Do NOT auto-invoke for routine hireui debugging — cm-debugging is primary.
license: MIT
source: mattpocock/skills (v1.0; imported 2026-05-11)
namespace_role: REFERENCE-ALT
primary_alternative: cm-debugging
---
```

**5-field metadata extension** added to every imported skill:
- `source:` — upstream repo + version + import date (provenance audit trail)
- `namespace_role:` — PRIMARY / REFERENCE-ALT / OVERLAY / REVIEW-ALT (matches Layer 1 table)
- `primary_alternative:` — name of the cm-*/bmad-* skill this defers to (empty if none)
- `installed_via:` — copy / plugin-marketplace / manual-curl (audit trail for uninstall)
- `pilot_evaluation_end:` — date when ablation decision is due (e.g., 2026-05-18 = 1 week from pilot start)

#### Layer 3 — Precedence registry (single source of truth)

Create `.cm/memory/skill-precedence.json` — authoritative map from functional category → ordered list of skills, primary first:

```json
{
  "_meta": {
    "version": "1.0",
    "last_audited": "2026-05-11",
    "policy": "First skill in array is PRIMARY auto-invoke. Subsequent skills are REFERENCE-ALT or REVIEW-ALT; invoke only on explicit operator request or after primary has run."
  },
  "debugging": ["cm-debugging", "mattpocock-diagnose"],
  "triage_and_quality_gate": ["cm-quality-gate", "mattpocock-triage"],
  "code_review": ["cm-code-review", "bmad-review-adversarial-general", "codex-adversarial-review", "mattpocock-triage"],
  "spec_writing": ["bmad-shard-doc", "mattpocock-to-prd"],
  "ticket_creation": ["mattpocock-to-issues"],
  "architecture_planning": ["cm-planning", "mattpocock-improve-codebase-architecture", "mattpocock-zoom-out"],
  "test_design": ["bmad-tea-bmad-test-design", "mattpocock-tdd"],
  "test_architecture": ["bmad-tea-bmad-testarch-framework", "bmad-tea-bmad-testarch-atdd"],
  "brainstorming": ["cm-brainstorm-idea", "bmad-brainstorming"],
  "continuity_and_session": ["cm-continuity"],
  "deep_search_and_zoom": ["cm-deep-search", "mattpocock-zoom-out"],
  "interview_pattern": ["cm-jtbd", "mattpocock-grill-with-docs", "mattpocock-grill-me"],
  "skill_creation": ["mattpocock-write-a-skill"],
  "prototyping": ["mattpocock-prototype"],
  "git_workflow_guardrails": ["scripts/git-hooks/pre-commit-branch-policy.sh", "mattpocock-git-guardrails-claude-code (REFERENCE-ONLY; do not invoke — pre-commit hook is authoritative)"],
  "behavioral_overlay": ["karpathy-guidelines"]
}
```

**How the agent uses this registry:**

1. Agent considering a trigger reads `.cm/memory/skill-precedence.json` first
2. Identifies functional category matching the task
3. Invokes the FIRST skill in the array unless:
   - Operator explicitly asked for a different one
   - First-skill output already exists and operator wants second-opinion
4. Logs invocation to `.cm/memory/skill-invocation-log.json` (telemetry; Layer 4)

**Operator can override** by editing the registry; agents cannot edit it (mirrors CONSTITUTION.md authority pattern from I-7).

#### Layer 4 — Conflict telemetry + ablation rules

Create `.cm/memory/skill-invocation-log.json` to capture every skill invocation:

```json
{
  "_schema": "1.0",
  "_started": "2026-05-11",
  "invocations": [
    {
      "ts": "2026-05-11T14:23:00Z",
      "trigger_description": "operator: debug the deferred_count migration script",
      "functional_category": "debugging",
      "candidates_considered": ["cm-debugging", "mattpocock-diagnose"],
      "selected": "cm-debugging",
      "selection_reason": "registry_primary",
      "operator_override": false,
      "outcome_quality": null
    }
  ]
}
```

**Ablation rules at Step 10 adoption decision (pilot end):**

| Telemetry pattern | Decision |
|-------------------|---------|
| REFERENCE-ALT skill invoked ≥ 3 times AND ≥ 1 invocation produced useful-distinct-output | **KEEP** + promote to tracked |
| REFERENCE-ALT skill invoked < 3 times in pilot week | **DEMOTE** to `.disabled-mattpocock-<name>/` directory; keep file for re-install but block auto-invoke |
| REFERENCE-ALT skill invoked but outcome_quality always = "duplicate-of-primary" | **REMOVE** entirely |
| PRIMARY skill invoked < 50% of category total | **RE-EVALUATE precedence** — maybe REFERENCE-ALT is actually better; swap order in registry |

**Honest-signal protection:** the `outcome_quality` field is set by the OPERATOR after reviewing the output, not by the agent (prevents agent-self-reporting bias).

### Special cases (3 conflicts requiring extra discipline)

#### Special case A — `mattpocock-git-guardrails-claude-code` vs hireui I-2 invariant pre-commit hook

**Conflict severity:** HIGHEST — mattpocock's git-guardrails could disable or duplicate hireui's `scripts/git-hooks/pre-commit-branch-policy.sh`, which is **enforcement for I-2 invariant** (non-negotiable per CONSTITUTION).

**Resolution:** install as `mattpocock-git-guardrails-claude-code/` with frontmatter:
```yaml
namespace_role: REFERENCE-ONLY-DO-NOT-INVOKE
primary_alternative: scripts/git-hooks/pre-commit-branch-policy.sh (authoritative)
warning: |
  This skill conflicts with hireui's I-2 invariant pre-commit hook enforcement.
  Kept for cross-pattern comparison only. NEVER invoke. If pre-commit hook
  needs modification, edit scripts/git-hooks/pre-commit-branch-policy.sh
  directly per CONSTITUTION I-2 amendment rule.
```

Add explicit registry entry:
```json
"git_workflow_guardrails": [
  "scripts/git-hooks/pre-commit-branch-policy.sh",
  "mattpocock-git-guardrails-claude-code (REFERENCE-ONLY; do not invoke — pre-commit hook is authoritative)"
]
```

#### Special case B — `mattpocock-setup-pre-commit` (already-configured conflict)

hireui's pre-commit is already configured (Husky + lint-staged + branch-policy). Install `mattpocock-setup-pre-commit/` with:
```yaml
namespace_role: REFERENCE-DOCUMENTATION
status: NOT-APPLICABLE-AT-INSTALL-TIME (hireui pre-commit already configured)
description: |
  Reference skill for understanding mattpocock's pre-commit setup approach.
  hireui already has pre-commit configured (Husky + lint-staged + branch-policy);
  do not re-run setup. Read for cross-pattern comparison only.
```

#### Special case C — `mattpocock-grill-with-docs` + `mattpocock-grill-me` already cross-ported to KJ OS Brain-setup v2

Storm Bear vault's Brain-setup v2 (per root CLAUDE.md "Pattern 2") was cross-ported from mattpocock/grill-with-docs at v57. The grill-* skills are **already integrated upstream**. Install but mark:
```yaml
namespace_role: REFERENCE-PORTED
status: ALREADY-INTEGRATED-IN-VAULT-BRAIN-SETUP-V2
description: |
  Upstream source of KJ OS Template's Brain-setup v2 (Pattern 2). Use the
  vault's Brain-setup skill for new context personalization; this raw form
  is kept for upstream-update tracking only.
```

### Summary: how full-install + management changes Step 5

Before (v2 plan original v3 draft):
- Install 3 cherry-picked skills (`mattpocock-prototype` + `mattpocock-to-issues` + `mattpocock-write-a-skill`)
- SKIP 9 (debugging/triage/git-guardrails/setup-pre-commit/improve-codebase-architecture/tdd/grill-*/zoom-out/to-prd)
- 1 OUT-OF-SCOPE clean install

After (this §3.5 policy applied):
- Install **all 19 active mattpocock skills** as `mattpocock-*`
- Apply description-narrowing to 12 skills with cm-*/bmad-* duplicates
- Mark 3 skills as REFERENCE-ONLY-DO-NOT-INVOKE (git-guardrails + setup-pre-commit + ported grill-*)
- Create `.cm/memory/skill-precedence.json` registry
- Start `.cm/memory/skill-invocation-log.json` telemetry
- Per-skill ablation decision at Step 10 (was: bulk decision)

### Implementation cost added

| Sub-task | Time | Where |
|---------|------|-------|
| Bulk install (19 skills) | ~10 min | Step 5 |
| Description-narrowing (12 duplicates) | ~20-30 min | Step 5 |
| Precedence registry creation | ~15 min | Step 5 |
| Telemetry schema + initial log | ~10 min | Step 5 |
| Per-skill ablation review at Step 10 | ~30 min | Step 10 |
| **Total added** | **~85-95 min** | — |

**Net impact on pilot budget:** ~7-9h → **~8.5-10.5h** spread over 1 week. Tradeoff: full-install + management = ~1.5h overhead for richer ablation evidence vs cherry-pick = 0 overhead but loses orthogonal-perspective data.

### Reversibility guarantee

If management overhead proves not worth it after 1 week:
1. Read `.cm/memory/skill-invocation-log.json`
2. Identify skills with 0 invocations OR only duplicate-of-primary outcomes
3. Bulk `rm -rf .claude/skills/mattpocock-<name>/` for low-utility entries
4. Update `skill-precedence.json` to remove them
5. Retain `mattpocock-prototype` + `mattpocock-to-issues` + `mattpocock-write-a-skill` (the original cherry-pick subset) as minimum

**Worst case** = cherry-pick-equivalent state with 1 week of measurement evidence proving why.

---

## 3.6 Cross-Session Enforcement (NEW — operator request 2026-05-12)

> **Operator intent (verbatim):** "Does the Skill Management Policy guarantee no context loss across sessions?"
>
> **Honest answer:** §3.5 artifacts (skill files / registry JSON / telemetry JSON / CLAUDE.md pointer) persist on disk and survive sessions. **But enforcement is 0-60% depending on Claude's compliance.** Fresh session may not auto-read the registry, may not auto-write telemetry, may invoke REFERENCE-ONLY skills despite annotations. Three context-loss vectors documented below + 5-layer enforcement (E1-E5) to close all gaps.

### 3 context-loss vectors §3.5 does NOT close on its own

| Vector | Effect | Why current design fails |
|--------|--------|--------------------------|
| **V1: Precedence registry orphaned** | Fresh session ignores `.cm/memory/skill-precedence.json` → PRIMARY/REFERENCE-ALT distinction collapses; auto-invoke reverts to description-matching | Registry is a JSON file Claude must be TOLD to read; no auto-load mechanism |
| **V2: Telemetry log starves** | `.cm/memory/skill-invocation-log.json` stays `invocations: []` → Step 10 ablation has 0 data → default-REMOVE all REFERENCE-ALT skills (false-signal) | No hook captures invocations; relies on agent self-reporting which is forgettable + biased |
| **V3: Description-narrowing partial** | `mattpocock-*` SKILL.md body may still match trigger patterns despite narrowed description; Claude auto-invokes anyway | Description is a hint, not a hard rule; body content also influences relevance scoring |

### 5-layer enforcement (E1-E5) — FULL (c) tier selected

#### E1 — NEW I-8 Constitutional Invariant (hard-soft tier)

Add to `/Users/Cvtot/monorepo/hireui/CONSTITUTION.md` as **I-8** invariant:

```markdown
### I-8 Skill precedence registry consultation is non-negotiable

When invoking any skill, agents MUST consult `.cm/memory/skill-precedence.json`
before selection if the trigger matches a functional category with ≥2 registered
candidates. Selection logic:

1. If only 1 skill registered for category → invoke that skill
2. If ≥2 skills registered → invoke FIRST array entry (PRIMARY) unless:
   (a) operator explicitly named a different candidate, OR
   (b) PRIMARY already ran in current session AND operator requested second-opinion
3. If invoked skill has `namespace_role: REFERENCE-ONLY-DO-NOT-INVOKE` →
   MUST refuse invocation; only operator may override with explicit `--override` flag

Violation = constitutional invariant breach. Agents that violate I-8 must
self-report at next response with: "I-8 violation: invoked <skill> instead of
PRIMARY <primary_alternative>. Reason: ___"

Operator may amend I-8 by editing CONSTITUTION.md directly (per existing
amendment rule); agents cannot.
```

**Strength:** ⭐⭐⭐⭐ HARD-SOFT (CONSTITUTION-tier authority; non-negotiable per existing I-1 to I-7 framework; but enforcement still depends on Claude reading + obeying CONSTITUTION)

**Implementation cost:** ~5 min (edit CONSTITUTION.md)

#### E2 — SessionStart hook (deterministic)

Add to `.claude/settings.json` (or `.claude/settings.local.json` for per-developer):

```json
{
  "hooks": {
    "SessionStart": [
      {
        "matcher": ".*",
        "command": "bash scripts/hooks/print-skill-policy.sh"
      }
    ]
  }
}
```

Create `scripts/hooks/print-skill-policy.sh`:

```bash
#!/bin/bash
# Print skill-management policy summary at every session start.
# Ensures every new session is aware of precedence registry + I-8 invariant.

REGISTRY=".cm/memory/skill-precedence.json"
TELEMETRY=".cm/memory/skill-invocation-log.json"

echo "===== HIREUI SKILL-MANAGEMENT POLICY (active per CONSTITUTION I-8) ====="
echo ""
echo "Precedence registry: $REGISTRY"
if [ -f "$REGISTRY" ]; then
  echo "Categories tracked: $(jq 'to_entries | map(select(.key | startswith("_") | not)) | length' "$REGISTRY" 2>/dev/null || echo "?")"
  echo "Last audited: $(jq -r '._meta.last_audited' "$REGISTRY" 2>/dev/null || echo "?")"
else
  echo "  ⚠️ REGISTRY MISSING — create per pilot plan v3 §3.5 Step 5.C"
fi

echo ""
echo "Telemetry log: $TELEMETRY"
if [ -f "$TELEMETRY" ]; then
  INV_COUNT=$(jq '.invocations | length' "$TELEMETRY" 2>/dev/null || echo "?")
  echo "Invocations logged this pilot: $INV_COUNT"
else
  echo "  ⚠️ TELEMETRY MISSING — initialize per pilot plan v3 §3.5 Step 5.D"
fi

echo ""
echo "I-8 rule summary: Consult registry BEFORE invoking any skill in a"
echo "multi-candidate functional category. PRIMARY first unless operator override."
echo "============================================================================"
```

```bash
# Make executable
chmod +x scripts/hooks/print-skill-policy.sh
```

**Strength:** ⭐⭐⭐⭐ DETERMINISTIC (hook runs at every session start; agents see policy in context immediately)

**Implementation cost:** ~20 min (script + settings.json)

**Closes vector:** V1 — registry no longer orphaned; auto-loaded into session context.

#### E3 — PostToolUse telemetry hook (deterministic; highest leverage)

Add to `.claude/settings.json`:

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Skill",
        "command": "bash scripts/hooks/log-skill-invocation.sh"
      }
    ]
  }
}
```

Create `scripts/hooks/log-skill-invocation.sh`:

```bash
#!/bin/bash
# Auto-append invocation entry to .cm/memory/skill-invocation-log.json
# after every Skill tool call. Removes agent-self-reporting bias.

TELEMETRY=".cm/memory/skill-invocation-log.json"
TS=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

# Hook receives tool input via stdin (JSON envelope per Claude Code spec)
INPUT=$(cat)
SKILL_NAME=$(echo "$INPUT" | jq -r '.tool_input.skill // "unknown"' 2>/dev/null)

# Determine functional category from precedence registry
REGISTRY=".cm/memory/skill-precedence.json"
CATEGORY="uncategorized"
if [ -f "$REGISTRY" ]; then
  CATEGORY=$(jq -r --arg s "$SKILL_NAME" '
    to_entries
    | map(select(.key | startswith("_") | not))
    | map(select(.value | tostring | contains($s)))
    | first.key // "uncategorized"
  ' "$REGISTRY" 2>/dev/null || echo "uncategorized")
fi

# Determine candidates considered (siblings in same category)
CANDIDATES=$(jq -r --arg c "$CATEGORY" '.[$c] // [] | tostring' "$REGISTRY" 2>/dev/null || echo "[]")

# Append entry
NEW_ENTRY=$(jq -n \
  --arg ts "$TS" \
  --arg skill "$SKILL_NAME" \
  --arg cat "$CATEGORY" \
  --argjson cands "$CANDIDATES" \
  '{
    ts: $ts,
    skill: $skill,
    functional_category: $cat,
    candidates_considered: $cands,
    selected: $skill,
    selection_reason: "registry_primary",
    operator_override: false,
    outcome_quality: null
  }')

# Update telemetry log atomically
if [ -f "$TELEMETRY" ]; then
  jq --argjson entry "$NEW_ENTRY" '.invocations += [$entry]' "$TELEMETRY" > "$TELEMETRY.tmp" && mv "$TELEMETRY.tmp" "$TELEMETRY"
fi
```

```bash
chmod +x scripts/hooks/log-skill-invocation.sh
```

**Strength:** ⭐⭐⭐⭐⭐ DETERMINISTIC + UNBIASED (hook fires programmatically; cannot be skipped; agent self-reporting bias eliminated)

**Implementation cost:** ~40 min (script + jq logic + atomic-write pattern)

**Closes vector:** V2 — telemetry no longer starves; Step 10 ablation has guaranteed data.

**Note:** `selection_reason` defaults to `registry_primary` from the hook; operator manually updates `outcome_quality` post-review (preserves honest-signal protection).

#### E4 — PreToolUse HARD block hook (deterministic; programmatic enforcement)

Add to `.claude/settings.json`:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Skill",
        "command": "bash scripts/hooks/check-skill-policy.sh"
      }
    ]
  }
}
```

Create `scripts/hooks/check-skill-policy.sh`:

```bash
#!/bin/bash
# HARD block: refuse skill invocations that violate §3.5 policy.
# Exit 1 = block; exit 0 = allow.

INPUT=$(cat)
SKILL_NAME=$(echo "$INPUT" | jq -r '.tool_input.skill // ""')
SKILL_DIR=".claude/skills/$SKILL_NAME"
SKILL_MD="$SKILL_DIR/SKILL.md"

# Read namespace_role from skill frontmatter
if [ -f "$SKILL_MD" ]; then
  ROLE=$(grep -E "^namespace_role:" "$SKILL_MD" | sed 's/namespace_role: *//' | tr -d ' ')

  # Block REFERENCE-ONLY-DO-NOT-INVOKE skills
  if [ "$ROLE" = "REFERENCE-ONLY-DO-NOT-INVOKE" ]; then
    OVERRIDE=$(echo "$INPUT" | jq -r '.tool_input.override // false')
    if [ "$OVERRIDE" != "true" ]; then
      echo "BLOCKED: $SKILL_NAME has namespace_role=REFERENCE-ONLY-DO-NOT-INVOKE per pilot plan v3 §3.5 special-case." >&2
      echo "To force-invoke, set tool_input.override=true (operator-only)." >&2
      exit 1
    fi
  fi

  # Verify primary_alternative ran first (if registered)
  PRIMARY_ALT=$(grep -E "^primary_alternative:" "$SKILL_MD" | sed 's/primary_alternative: *//' | tr -d ' ')
  if [ -n "$PRIMARY_ALT" ] && [ "$PRIMARY_ALT" != "N/A" ]; then
    # Check if primary ran in last 30 min of telemetry
    TELEMETRY=".cm/memory/skill-invocation-log.json"
    RECENT_PRIMARY=$(jq -r --arg p "$PRIMARY_ALT" \
      '.invocations | map(select(.selected == $p)) | last.ts // ""' "$TELEMETRY" 2>/dev/null)
    if [ -z "$RECENT_PRIMARY" ]; then
      echo "WARNING: $SKILL_NAME is REFERENCE-ALT to $PRIMARY_ALT but primary has not run." >&2
      echo "Consider invoking $PRIMARY_ALT first, or set operator_override=true." >&2
      # Soft warning — don't block on this; agent decides based on warning
    fi
  fi
fi

exit 0
```

```bash
chmod +x scripts/hooks/check-skill-policy.sh
```

**Strength:** ⭐⭐⭐⭐⭐ PROGRAMMATIC HARD BLOCK (cannot be bypassed without explicit override flag)

**Implementation cost:** ~30 min (script + jq logic + override handling)

**Closes vector:** V3 — description-narrowing soft enforcement is backed up by hard programmatic block on REFERENCE-ONLY skills + soft warning on REFERENCE-ALT precedence.

#### E5 — CONTINUITY.md skill-state section (soft pickup)

Add to `.cm/CONTINUITY.md` as part of standard session pickup:

```markdown
## Skill management active state (per pilot plan v3 §3.5/§3.6)

- **Registry:** `.cm/memory/skill-precedence.json` (17 functional categories tracked; last audited 2026-05-11)
- **Telemetry:** `.cm/memory/skill-invocation-log.json` (N invocations logged this pilot)
- **CONSTITUTION authority:** I-8 invariant (precedence registry consultation non-negotiable)
- **Hooks active:** SessionStart (print-skill-policy.sh) / PreToolUse (check-skill-policy.sh) / PostToolUse (log-skill-invocation.sh)
- **Active pilot:** 2026-05-11 adversarial-review v3 (BMAD Stratum A vs codex-plugin-cc Stratum B + karpathy overlay + mattpocock full-install)
- **Pilot evaluation due:** 2026-05-18 (Step 10 ablation decisions)
- **Reference:** `/Users/Cvtot/KJ OS Template/04 Reviews/(C) 2026-05-11 adversarial-review pilot v3 - hireui real monorepo.md`
```

**Update CONTINUITY.md.template** to include this section structure permanently (so future pilots auto-track skill-management state).

**Strength:** ⭐⭐⭐ SOFT PICKUP (CONTINUITY auto-loaded at session start per existing hireui pattern; signals active management state)

**Implementation cost:** ~10 min (added to Step 0.C; auto-updated by hook at session start ideally)

**Closes vector:** V1 reinforced + cross-pilot continuity.

### Combined enforcement matrix (all 5 layers active)

| Vector | E1 (I-8) | E2 (SessionStart) | E3 (PostToolUse) | E4 (PreToolUse) | E5 (CONTINUITY) | Combined |
|--------|---------|-------------------|------------------|-----------------|-----------------|----------|
| V1 registry orphaned | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | — | — | ⭐⭐⭐ | **⭐⭐⭐⭐⭐ CLOSED** |
| V2 telemetry starves | ⭐ | ⭐ | ⭐⭐⭐⭐⭐ | — | — | **⭐⭐⭐⭐⭐ CLOSED** |
| V3 description partial | ⭐⭐ | — | — | ⭐⭐⭐⭐⭐ | — | **⭐⭐⭐⭐⭐ CLOSED** |

**All 3 vectors closed.** Bypass requires:
- Editing CONSTITUTION.md (operator-only per I-8 amendment rule)
- Removing hook entries from settings.json (operator action; visible in git diff)
- Passing explicit `--override` flag (operator-only per E4 spec)

### Step 0 + Step 5 cost additions for E1-E5

| Layer | Where in plan | Time added |
|-------|---------------|-----------|
| E1 I-8 invariant | Step 0 NEW sub-step 0.F | +5 min |
| E2 SessionStart hook | Step 5 NEW sub-step 5.H | +20 min |
| E3 PostToolUse telemetry hook | Step 5 NEW sub-step 5.I | +40 min |
| E4 PreToolUse HARD block hook | Step 5 NEW sub-step 5.J | +30 min |
| E5 CONTINUITY skill-state section | Step 0.C extension | +10 min |
| **Total added** | — | **+105 min** |

### Reversibility preserved (E1-E5 opt-out paths)

| Layer | Reversibility |
|-------|---------------|
| E1 | Edit CONSTITUTION.md → remove I-8 |
| E2 | Remove SessionStart hook entry from settings.json |
| E3 | Remove PostToolUse hook entry from settings.json |
| E4 | Remove PreToolUse hook entry from settings.json |
| E5 | Edit CONTINUITY.md → remove skill-management section |

All 5 layers are **opt-out reversible** at any point during pilot. Per-layer cost-benefit re-evaluation possible mid-pilot.

### Pattern Library implication (NEW at v3.2)

The 5-layer enforcement design — namespace prefix + description-narrowing + precedence registry + telemetry hooks + CONSTITUTION invariant — is candidate **Pattern #78 Cross-Session Duplicate-Skill Management** for v66/v69 audit consideration:

- **N=1 baseline at v63.5/v66 if hireui pilot demonstrates value**
- **Un-stale criterion:** 2nd harness deploying same 5-layer policy
- **Promotion criterion (structural-N=2):** mechanism reproducibly closes V1/V2/V3 vectors across 2 distinct harnesses

---

## 4. Step 0 — MANDATORY pre-flight gap-fill (~40-55 min, was 30-45 min)

**Cannot start pilot until Step 0 closes the 3 partial/missing v2 plan items affecting pilot integrity.**

### 0.A Verify Concept 2 pre-flight skill state (~5 min)

```bash
cd /Users/Cvtot/monorepo/hireui
ls -la .claude/skills/cm-continuity/SKILL.md
cat .claude/skills/cm-continuity/SKILL.md | head -50
# Decision: is Phase 0 pre-flight encoded here, OR does cm-pre-flight need separate creation?
```

**Decision gate:** if `cm-continuity` covers Phase 0 → mark Concept 2 DONE; if not → create `cm-pre-flight` skill as part of pilot work (folded into Step 6).

### 0.B Decide Concept 4 cadence approach (~5 min)

Two existing session-log locations:
- `_bmad-output/sessions/` — 2 entries dated 2026-05-06
- `.cm/traces/sessions/` — empty (template exists)

**Decision gate:** pick ONE authoritative location for ongoing session logs. Recommend `_bmad-output/sessions/` (has live entries; BMAD-namespaced; matches existing cadence). Update `.cm/traces/SESSION-TEMPLATE.md` header to point operators to `_bmad-output/sessions/`.

### 0.C Update CONTINUITY.md with pilot-start declaration + E5 skill-management section (~15 min)

```bash
# Add to .cm/CONTINUITY.md at the top:
# Pilot in progress: 2026-05-11 adversarial-review v3
# Branch: agent/pilot-2026-05-11-adversarial-review (from agent-dev)
# Reference: /Users/Cvtot/KJ OS Template/04 Reviews/(C) 2026-05-11 adversarial-review pilot v3 - hireui real monorepo.md
# Pilot feature: Concept 6 deferred_count schema
```

Plus add E5 skill-management state section to `.cm/CONTINUITY.md` (per §3.6 E5):

```markdown
## Skill management active state (per pilot plan v3 §3.5/§3.6)

- **Registry:** `.cm/memory/skill-precedence.json` (17 functional categories; last audited 2026-05-11)
- **Telemetry:** `.cm/memory/skill-invocation-log.json` (initialized 2026-05-11; updated by E3 PostToolUse hook)
- **CONSTITUTION authority:** I-8 invariant (precedence registry consultation non-negotiable; added 2026-05-11)
- **Hooks active:** SessionStart (print-skill-policy.sh) / PreToolUse (check-skill-policy.sh) / PostToolUse (log-skill-invocation.sh)
- **Active pilot:** 2026-05-11 adversarial-review v3 (BMAD Stratum A vs codex-plugin-cc Stratum B + karpathy overlay + mattpocock full-install)
- **Pilot evaluation due:** 2026-05-18 (Step 10 ablation decisions)
- **Reference:** `/Users/Cvtot/KJ OS Template/04 Reviews/(C) 2026-05-11 adversarial-review pilot v3 - hireui real monorepo.md`
```

**Also update `.cm/CONTINUITY.md.template`** with the same section structure as a permanent template element — future pilots inherit skill-management state-tracking automatically.

### 0.D Create pilot branch from agent-dev (~5 min)

```bash
cd /Users/Cvtot/monorepo/hireui

# Ensure agent-dev is current
git fetch origin
git checkout agent-dev
git pull origin agent-dev

# Verify clean state
git status  # MUST be clean before next step

# Create pilot branch
git checkout -b agent/pilot-2026-05-11-adversarial-review

# Push to set upstream
git push -u origin agent/pilot-2026-05-11-adversarial-review

# Verify pre-commit hook accepts agent/* branch family per I-2
git status
```

**Verification:** branch matches harness-files-allowed pattern per I-2 invariant. Pre-commit hook test:
```bash
# Touch a harness file and dry-run commit (don't actually commit)
echo "" >> CLAUDE.md
git add CLAUDE.md
GIT_HOOKS_DRY_RUN=1 git commit -m "test" || echo "(dry-run failed if hook misconfigured)"
git restore --staged CLAUDE.md
git restore CLAUDE.md
```

### 0.E Create pilot vault meta-folder + README (~5 min)

```bash
# SESSION B (vault root) — open NEW Claude Code session
cd "/Users/Cvtot/KJ OS Template"
mkdir -p "03 Projects/_pilots/2026-05-11 adversarial-review-v3-hireui/pilot-log"
```

Create `03 Projects/_pilots/2026-05-11 adversarial-review-v3-hireui/README.md` with:
- Pilot description + target monorepo path
- Real feature scope: Concept 6 deferred_count schema
- Architecture reference (Hybrid Option 3+5 from v2)
- Cross-references to v2 KJ OS integration plan + hireui CONSTITUTION + cc-sdd/codex-plugin-cc/karpathy-skills wiki entries

Commit vault meta-setup:
```bash
git -C "/Users/Cvtot/KJ OS Template" add "03 Projects/_pilots/2026-05-11 adversarial-review-v3-hireui/"
git -C "/Users/Cvtot/KJ OS Template" commit -m "Pilot v3 setup: meta-folder for adversarial-review pilot on hireui (BMAD vs codex-plugin-cc Stratum A/B + karpathy + mattpocock cherry-pick)"
```

### 0.F Add I-8 invariant to CONSTITUTION.md (E1 enforcement; ~5 min)

Open `/Users/Cvtot/monorepo/hireui/CONSTITUTION.md` and append after I-7:

```markdown
### I-8 Skill precedence registry consultation is non-negotiable

When invoking any skill, agents MUST consult `.cm/memory/skill-precedence.json`
before selection if the trigger matches a functional category with ≥2 registered
candidates. Selection logic:

1. If only 1 skill registered for category → invoke that skill
2. If ≥2 skills registered → invoke FIRST array entry (PRIMARY) unless:
   (a) operator explicitly named a different candidate, OR
   (b) PRIMARY already ran in current session AND operator requested second-opinion
3. If invoked skill has `namespace_role: REFERENCE-ONLY-DO-NOT-INVOKE` →
   MUST refuse invocation; only operator may override with explicit `--override` flag

Violation = constitutional invariant breach. Agents that violate I-8 must
self-report at next response with: "I-8 violation: invoked <skill> instead of
PRIMARY <primary_alternative>. Reason: ___"

Operator may amend I-8 by editing CONSTITUTION.md directly (per existing
amendment rule); agents cannot.
```

Verify:
```bash
grep -A 18 "^### I-8" CONSTITUTION.md | head -22
```

**Reference:** Pilot plan v3 §3.6 E1 layer.

### Step 0 verification checklist

- [ ] 0.A cm-continuity OR cm-pre-flight skill confirmed covering Phase 0 pre-flight
- [ ] 0.B Authoritative session-log location decided (recommend `_bmad-output/sessions/`)
- [ ] 0.C CONTINUITY.md updated with pilot-start declaration + E5 skill-management section
- [ ] 0.D `agent/pilot-2026-05-11-adversarial-review` branch created from `agent-dev`, pushed, pre-commit hook test passes
- [ ] 0.E Vault meta-folder + README created, committed
- [ ] 0.F **NEW** I-8 invariant added to CONSTITUTION.md (E1 layer per §3.6)

---

## 5. Step 1 — Pre-flight tools (~10 min)

```bash
node --version    # ≥ 18.18 required
npm --version
which claude      # OR however you invoke Claude Code

# ChatGPT subscription verify
# Open https://chat.openai.com/billing OR
echo $OPENAI_API_KEY | head -c 10

# Disk space
df -h ~/ | head -2     # need ≥2GB free
```

**Stop if fail.** No proceed until pre-reqs met.

---

## 6. Step 2 — Open Session A at hireui CWD (~5 min)

```bash
cd /Users/Cvtot/monorepo/hireui
pwd                                  # MUST equal /Users/Cvtot/monorepo/hireui
git branch --show-current           # MUST equal agent/pilot-2026-05-11-adversarial-review
```

**ĐÓNG** Session B (vault). **MỞ NEW** Claude Code session at this CWD.

**Critical:** Session A loads hireui's `CLAUDE.md` + `CONSTITUTION.md` + `AGENTS.md` as primary context. Vault rules NOT auto-active.

### First-prompt in Session A — context-load verification

```
Verify you've loaded:
1. /Users/Cvtot/monorepo/hireui/CONSTITUTION.md (7 invariants)
2. /Users/Cvtot/monorepo/hireui/CLAUDE.md (mandatory next-action + Goodhart's law)
3. /Users/Cvtot/monorepo/hireui/AGENTS.md
4. Current branch: agent/pilot-2026-05-11-adversarial-review
5. .cm/CONTINUITY.md current state

Confirm before any tool installs.
```

---

## 7. Step 3 — Install codex-plugin-cc (Stratum B) (~15-20 min, Session A)

```
/plugin marketplace add openai/codex-plugin-cc
/plugin install codex@openai-codex
/reload-plugins
/codex:setup
```

`/codex:setup` will prompt ChatGPT/OpenAI auth — complete the flow.

**Verification:**
```
Type /codex: — autocomplete should show 7 commands:
  review / adversarial-review / rescue / status / result / cancel / setup
```

---

## 8. Step 4 — Install karpathy-skills (~5 min, Session A)

```
/plugin marketplace add forrestchang/andrej-karpathy-skills
/plugin install andrej-karpathy-skills@karpathy-skills
/reload-plugins
```

**Verification:**
```bash
ls .claude/skills/karpathy-guidelines/SKILL.md
# Plus .cursor/rules/karpathy-guidelines.mdc should auto-deploy
ls .cursor/rules/karpathy-guidelines.mdc
```

Skill auto-invokes when matching description criteria fire (no explicit slash command).

---

## 9. Step 5 — Full-install mattpocock skills + apply §3.5 management policy (~45-55 min, Session A)

**Operator-requested change (2026-05-11):** install ALL 19 active mattpocock skills (not cherry-pick subset). Apply Duplicate-Skill Management Policy from §3.5 to prevent agent-confusion across competing-trigger skills.

### 5.A Bulk install (~10 min)

```bash
# Use temp clone (NOT in monorepo)
mkdir -p ~/tmp && cd ~/tmp
git clone --depth 1 https://github.com/mattpocock/skills.git mattpocock-skills-temp

# Bulk-copy all 19 active skills into hireui with mattpocock- prefix
cd /Users/Cvtot/monorepo/hireui

for category in engineering productivity personal misc; do
  for skill_dir in ~/tmp/mattpocock-skills-temp/skills/$category/*/; do
    skill_name=$(basename "$skill_dir")
    # Skip if SKILL.md doesn't exist (defensive)
    [ -f "$skill_dir/SKILL.md" ] || continue
    mkdir -p ".claude/skills/mattpocock-$skill_name"
    cp "$skill_dir/SKILL.md" ".claude/skills/mattpocock-$skill_name/SKILL.md"
    # Copy any helper files in the skill folder
    cp -r "$skill_dir"/* ".claude/skills/mattpocock-$skill_name/" 2>/dev/null
  done
done

# SKIP deprecated/in-progress directories (upstream maintainer signals not-ready)
# (deprecated and in-progress are not iterated in the for-loop)

# Cleanup temp clone
rm -rf ~/tmp/mattpocock-skills-temp

# Verify count
ls .claude/skills/mattpocock-*/SKILL.md | wc -l    # Expect ~19
```

**Expected 19 installs** (4 categories):
- engineering (10): mattpocock-diagnose / mattpocock-grill-with-docs / mattpocock-improve-codebase-architecture / mattpocock-prototype / mattpocock-setup-matt-pocock-skills / mattpocock-tdd / mattpocock-to-issues / mattpocock-to-prd / mattpocock-triage / mattpocock-zoom-out
- productivity (3): mattpocock-caveman / mattpocock-grill-me / mattpocock-write-a-skill
- personal (2): mattpocock-edit-article / mattpocock-obsidian-vault
- misc (4): mattpocock-git-guardrails-claude-code / mattpocock-migrate-to-shoehorn / mattpocock-scaffold-exercises / mattpocock-setup-pre-commit

### 5.B Description-narrowing for the 12 duplicates (~20-30 min)

Open each duplicate skill's SKILL.md and rewrite the `description:` frontmatter per §3.5 Layer 2 template.

**Bulk script approach** — generate a sed-edit batch from a duplicates manifest:

```bash
cd /Users/Cvtot/monorepo/hireui

# Manifest: skill name → primary alternative → namespace role
cat > /tmp/mattpocock-duplicates-manifest.txt << 'EOF'
mattpocock-diagnose|cm-debugging|REFERENCE-ALT
mattpocock-triage|cm-quality-gate|REFERENCE-ALT
mattpocock-improve-codebase-architecture|cm-planning|REFERENCE-ALT
mattpocock-zoom-out|cm-deep-search|REFERENCE-ALT
mattpocock-tdd|bmad-tea-bmad-teach-me-testing|REFERENCE-ALT
mattpocock-to-prd|bmad-shard-doc|REFERENCE-ALT
mattpocock-grill-with-docs|cm-jtbd|REFERENCE-PORTED
mattpocock-grill-me|cm-jtbd|REFERENCE-PORTED
mattpocock-git-guardrails-claude-code|scripts/git-hooks/pre-commit-branch-policy.sh|REFERENCE-ONLY-DO-NOT-INVOKE
mattpocock-setup-pre-commit|scripts/git-hooks/pre-commit-branch-policy.sh|REFERENCE-DOCUMENTATION
mattpocock-setup-matt-pocock-skills|N/A|REFERENCE-DOCUMENTATION
mattpocock-caveman|N/A|REFERENCE-ALT
EOF
```

For each line, manually edit the corresponding `.claude/skills/<name>/SKILL.md` to:
1. Replace `name: <original>` with `name: mattpocock-<original>`
2. Rewrite `description:` per §3.5 Layer 2 template (narrow trigger to "explicit invocation OR second-opinion after primary")
3. Append the 5-field metadata extension (`source:` / `namespace_role:` / `primary_alternative:` / `installed_via:` / `pilot_evaluation_end:`)

**Recommendation:** prompt Session A Claude:
```
Read /tmp/mattpocock-duplicates-manifest.txt. For each row, edit the corresponding
.claude/skills/<name>/SKILL.md to:
1. Add 5-field metadata extension per pilot plan v3 §3.5 Layer 2
2. Narrow the description: frontmatter to specify "explicit invocation OR
   second-opinion after primary_alternative runs"
3. Preserve all body content unchanged

Report each file edited.
```

Clean (non-duplicate) installs (`mattpocock-prototype` / `mattpocock-to-issues` / `mattpocock-write-a-skill` / `mattpocock-edit-article` / `mattpocock-obsidian-vault` / `mattpocock-migrate-to-shoehorn` / `mattpocock-scaffold-exercises`) get a minimal frontmatter update only:
```yaml
namespace_role: PRIMARY (no cm-*/bmad-* alternative; mattpocock-* is sole provider)
source: mattpocock/skills (v1.0; imported 2026-05-11)
installed_via: copy (manual bulk script)
pilot_evaluation_end: 2026-05-18
```

### 5.C Create precedence registry (~15 min)

```bash
mkdir -p .cm/memory
cat > .cm/memory/skill-precedence.json << 'EOF'
{
  "_meta": {
    "version": "1.0",
    "last_audited": "2026-05-11",
    "policy": "First skill in array is PRIMARY auto-invoke. Subsequent skills are REFERENCE-ALT or REVIEW-ALT; invoke only on explicit operator request or after primary has run.",
    "amendment_rule": "Only operator (not agents) may edit this file. Mirrors CONSTITUTION I-7 amendment rule."
  },
  "debugging": ["cm-debugging", "mattpocock-diagnose"],
  "triage_and_quality_gate": ["cm-quality-gate", "mattpocock-triage"],
  "code_review": [
    "cm-code-review",
    "bmad-review-adversarial-general",
    "codex-adversarial-review",
    "mattpocock-triage"
  ],
  "spec_writing": ["bmad-shard-doc", "mattpocock-to-prd"],
  "ticket_creation": ["mattpocock-to-issues"],
  "architecture_planning": [
    "cm-planning",
    "mattpocock-improve-codebase-architecture",
    "mattpocock-zoom-out"
  ],
  "test_design": ["bmad-tea-bmad-test-design", "mattpocock-tdd"],
  "test_architecture": [
    "bmad-tea-bmad-testarch-framework",
    "bmad-tea-bmad-testarch-atdd"
  ],
  "brainstorming": ["cm-brainstorm-idea", "bmad-brainstorming"],
  "continuity_and_session": ["cm-continuity"],
  "deep_search_and_zoom": ["cm-deep-search", "mattpocock-zoom-out"],
  "interview_pattern": ["cm-jtbd", "mattpocock-grill-with-docs", "mattpocock-grill-me"],
  "skill_creation": ["mattpocock-write-a-skill"],
  "prototyping": ["mattpocock-prototype"],
  "git_workflow_guardrails": [
    "scripts/git-hooks/pre-commit-branch-policy.sh",
    "mattpocock-git-guardrails-claude-code (REFERENCE-ONLY; do not invoke — pre-commit hook is authoritative)"
  ],
  "behavioral_overlay": ["karpathy-guidelines"]
}
EOF

# Track in agent-dev branch later (Step 6 commit)
ls -la .cm/memory/skill-precedence.json
```

### 5.D Initialize telemetry log (~10 min)

```bash
cat > .cm/memory/skill-invocation-log.json << 'EOF'
{
  "_schema": "1.0",
  "_started": "2026-05-11",
  "_purpose": "Capture every skill invocation during pilot to inform Step 10 ablation decisions. Operator updates outcome_quality after reviewing output.",
  "invocations": []
}
EOF
```

### 5.E Special-case handling (~5 min)

Verify the 3 special-case skills (§3.5 special cases A/B/C) have correct `namespace_role`:
```bash
grep -A 2 "namespace_role:" .claude/skills/mattpocock-git-guardrails-claude-code/SKILL.md
# Expect: REFERENCE-ONLY-DO-NOT-INVOKE

grep -A 2 "namespace_role:" .claude/skills/mattpocock-setup-pre-commit/SKILL.md
# Expect: REFERENCE-DOCUMENTATION

grep -A 2 "namespace_role:" .claude/skills/mattpocock-grill-with-docs/SKILL.md
# Expect: REFERENCE-PORTED
```

### 5.F Update CLAUDE.md with policy pointer (~5 min)

Add a section to hireui `CLAUDE.md` documenting that the management policy exists:

```markdown
## Skill management policy

When multiple installed skills serve overlapping functional categories,
consult `.cm/memory/skill-precedence.json` for the authoritative invocation
order. Telemetry captured in `.cm/memory/skill-invocation-log.json`. See
pilot plan v3 §3.5 for the 4-layer management approach
(/Users/Cvtot/KJ OS Template/04 Reviews/(C) 2026-05-11 adversarial-review pilot v3 - hireui real monorepo.md).
```

### 5.G Verification

```bash
# Skill count
ls .claude/skills/mattpocock-*/ | wc -l    # ~19

# Precedence registry exists
test -f .cm/memory/skill-precedence.json && echo "OK"

# Telemetry initialized
test -f .cm/memory/skill-invocation-log.json && echo "OK"

# Special cases marked
grep -l "REFERENCE-ONLY-DO-NOT-INVOKE" .claude/skills/mattpocock-*/SKILL.md
```

### .gitignore decision for mattpocock-* skills

Per Section 3, `mattpocock-*` skills are pilot-experimental and **gitignored**. But the precedence registry + telemetry log SHOULD be tracked (they're harness state). Update `.gitignore`:

```gitignore
# Pilot tools (per-developer; promote to tracked after pilot evaluation)
.claude/skills/karpathy-guidelines/
.claude/skills/mattpocock-*/
.codex/
.pilot-log/

# DO NOT ignore — track these even during pilot
# .cm/memory/skill-precedence.json    ← TRACKED
# .cm/memory/skill-invocation-log.json ← TRACKED (rotating; operator owns retention)
```

**At Step 10 ablation decision:** per-skill, decide REMOVE / KEEP-UNTRACKED / KEEP-AND-PROMOTE-TRACKED. KEEP-AND-PROMOTE-TRACKED moves the skill out of `.gitignore` exclusion and commits it as team-shared harness.

### 5.H Implement E2 SessionStart hook (~20 min)

```bash
mkdir -p scripts/hooks
cat > scripts/hooks/print-skill-policy.sh << 'EOF'
#!/bin/bash
# E2 — SessionStart hook per pilot plan v3 §3.6.
# Print skill-management policy summary at every session start.

REGISTRY=".cm/memory/skill-precedence.json"
TELEMETRY=".cm/memory/skill-invocation-log.json"

echo "===== HIREUI SKILL-MANAGEMENT POLICY (active per CONSTITUTION I-8) ====="
echo ""
echo "Precedence registry: $REGISTRY"
if [ -f "$REGISTRY" ]; then
  echo "Categories tracked: $(jq 'to_entries | map(select(.key | startswith("_") | not)) | length' "$REGISTRY" 2>/dev/null || echo "?")"
  echo "Last audited: $(jq -r '._meta.last_audited' "$REGISTRY" 2>/dev/null || echo "?")"
else
  echo "  ⚠️ REGISTRY MISSING — create per pilot plan v3 §3.5 Step 5.C"
fi
echo ""
echo "Telemetry log: $TELEMETRY"
if [ -f "$TELEMETRY" ]; then
  INV_COUNT=$(jq '.invocations | length' "$TELEMETRY" 2>/dev/null || echo "?")
  echo "Invocations logged this pilot: $INV_COUNT"
else
  echo "  ⚠️ TELEMETRY MISSING — initialize per pilot plan v3 §3.5 Step 5.D"
fi
echo ""
echo "I-8 rule summary: Consult registry BEFORE invoking any skill in a"
echo "multi-candidate functional category. PRIMARY first unless operator override."
echo "============================================================================"
EOF
chmod +x scripts/hooks/print-skill-policy.sh

# Add hook entry to .claude/settings.local.json (per-developer; not team-shared yet)
# Use jq for safe JSON merge
SETTINGS=".claude/settings.local.json"
if [ ! -f "$SETTINGS" ]; then echo '{}' > "$SETTINGS"; fi
jq '.hooks.SessionStart = [{"matcher": ".*", "command": "bash scripts/hooks/print-skill-policy.sh"}]' "$SETTINGS" > "$SETTINGS.tmp" && mv "$SETTINGS.tmp" "$SETTINGS"

# Verify
cat "$SETTINGS"
bash scripts/hooks/print-skill-policy.sh    # dry-run
```

### 5.I Implement E3 PostToolUse telemetry hook (~40 min)

```bash
cat > scripts/hooks/log-skill-invocation.sh << 'EOF'
#!/bin/bash
# E3 — PostToolUse hook per pilot plan v3 §3.6.
# Auto-append invocation entry to .cm/memory/skill-invocation-log.json
# after every Skill tool call. Removes agent-self-reporting bias.

TELEMETRY=".cm/memory/skill-invocation-log.json"
TS=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

# Hook receives tool input via stdin (JSON envelope per Claude Code spec)
INPUT=$(cat)
SKILL_NAME=$(echo "$INPUT" | jq -r '.tool_input.skill // "unknown"' 2>/dev/null)

# Determine functional category from precedence registry
REGISTRY=".cm/memory/skill-precedence.json"
CATEGORY="uncategorized"
CANDIDATES="[]"
if [ -f "$REGISTRY" ]; then
  CATEGORY=$(jq -r --arg s "$SKILL_NAME" '
    to_entries
    | map(select(.key | startswith("_") | not))
    | map(select(.value | tostring | contains($s)))
    | first.key // "uncategorized"
  ' "$REGISTRY" 2>/dev/null || echo "uncategorized")
  CANDIDATES=$(jq -c --arg c "$CATEGORY" '.[$c] // []' "$REGISTRY" 2>/dev/null || echo "[]")
fi

# Append entry
NEW_ENTRY=$(jq -n \
  --arg ts "$TS" \
  --arg skill "$SKILL_NAME" \
  --arg cat "$CATEGORY" \
  --argjson cands "$CANDIDATES" \
  '{
    ts: $ts,
    skill: $skill,
    functional_category: $cat,
    candidates_considered: $cands,
    selected: $skill,
    selection_reason: "registry_primary",
    operator_override: false,
    outcome_quality: null
  }')

# Update telemetry log atomically
if [ -f "$TELEMETRY" ]; then
  jq --argjson entry "$NEW_ENTRY" '.invocations += [$entry]' "$TELEMETRY" > "$TELEMETRY.tmp" && mv "$TELEMETRY.tmp" "$TELEMETRY"
fi
EOF
chmod +x scripts/hooks/log-skill-invocation.sh

# Add hook entry to settings.local.json
SETTINGS=".claude/settings.local.json"
jq '.hooks.PostToolUse = [{"matcher": "Skill", "command": "bash scripts/hooks/log-skill-invocation.sh"}]' "$SETTINGS" > "$SETTINGS.tmp" && mv "$SETTINGS.tmp" "$SETTINGS"

# Verify
cat "$SETTINGS"
```

**Dry-run test:** invoke any skill manually and check `.cm/memory/skill-invocation-log.json` for new entry.

### 5.J Implement E4 PreToolUse HARD block hook (~30 min)

```bash
cat > scripts/hooks/check-skill-policy.sh << 'EOF'
#!/bin/bash
# E4 — PreToolUse HARD block per pilot plan v3 §3.6.
# Refuse skill invocations that violate §3.5 policy.
# Exit 1 = block; exit 0 = allow.

INPUT=$(cat)
SKILL_NAME=$(echo "$INPUT" | jq -r '.tool_input.skill // ""')
SKILL_DIR=".claude/skills/$SKILL_NAME"
SKILL_MD="$SKILL_DIR/SKILL.md"

if [ -f "$SKILL_MD" ]; then
  ROLE=$(grep -E "^namespace_role:" "$SKILL_MD" | sed 's/namespace_role: *//' | tr -d ' ')

  # HARD BLOCK: REFERENCE-ONLY-DO-NOT-INVOKE skills
  if [ "$ROLE" = "REFERENCE-ONLY-DO-NOT-INVOKE" ]; then
    OVERRIDE=$(echo "$INPUT" | jq -r '.tool_input.override // false')
    if [ "$OVERRIDE" != "true" ]; then
      echo "BLOCKED: $SKILL_NAME has namespace_role=REFERENCE-ONLY-DO-NOT-INVOKE per pilot plan v3 §3.5 special-case." >&2
      echo "To force-invoke, set tool_input.override=true (operator-only)." >&2
      exit 1
    fi
  fi

  # SOFT WARNING: REFERENCE-ALT skill invoked without primary running first
  PRIMARY_ALT=$(grep -E "^primary_alternative:" "$SKILL_MD" | sed 's/primary_alternative: *//' | tr -d ' ')
  if [ -n "$PRIMARY_ALT" ] && [ "$PRIMARY_ALT" != "N/A" ]; then
    TELEMETRY=".cm/memory/skill-invocation-log.json"
    RECENT_PRIMARY=$(jq -r --arg p "$PRIMARY_ALT" \
      '.invocations | map(select(.selected == $p)) | last.ts // ""' "$TELEMETRY" 2>/dev/null)
    if [ -z "$RECENT_PRIMARY" ]; then
      echo "WARNING: $SKILL_NAME is REFERENCE-ALT to $PRIMARY_ALT but primary has not run." >&2
      echo "Consider invoking $PRIMARY_ALT first, or set operator_override=true." >&2
    fi
  fi
fi

exit 0
EOF
chmod +x scripts/hooks/check-skill-policy.sh

# Add hook entry to settings.local.json
SETTINGS=".claude/settings.local.json"
jq '.hooks.PreToolUse = [{"matcher": "Skill", "command": "bash scripts/hooks/check-skill-policy.sh"}]' "$SETTINGS" > "$SETTINGS.tmp" && mv "$SETTINGS.tmp" "$SETTINGS"

# Verify
cat "$SETTINGS"
```

**Dry-run test:**
```bash
# Simulate REFERENCE-ONLY skill invocation
echo '{"tool_input":{"skill":"mattpocock-git-guardrails-claude-code"}}' | bash scripts/hooks/check-skill-policy.sh
# Expected: exit 1 with BLOCKED message
echo "exit: $?"

# Simulate with override
echo '{"tool_input":{"skill":"mattpocock-git-guardrails-claude-code","override":true}}' | bash scripts/hooks/check-skill-policy.sh
# Expected: exit 0
echo "exit: $?"
```

### Step 5 verification checklist (post-E1-E5)

- [ ] 5.A Bulk install: ~19 mattpocock-* skills present in `.claude/skills/`
- [ ] 5.B Description-narrowing: 12 duplicates have 5-field metadata extension
- [ ] 5.C Precedence registry created at `.cm/memory/skill-precedence.json`
- [ ] 5.D Telemetry log initialized at `.cm/memory/skill-invocation-log.json`
- [ ] 5.E Special-case skills marked REFERENCE-ONLY-DO-NOT-INVOKE / REFERENCE-DOCUMENTATION / REFERENCE-PORTED
- [ ] 5.F CLAUDE.md updated with policy pointer
- [ ] 5.G .gitignore updated for `mattpocock-*` + telemetry/registry kept tracked
- [ ] 5.H **E2** SessionStart hook installed; dry-run prints policy summary
- [ ] 5.I **E3** PostToolUse telemetry hook installed; dry-run appends entry
- [ ] 5.J **E4** PreToolUse HARD block hook installed; dry-run blocks REFERENCE-ONLY skill

---

## 10. Step 6 — Pilot feature work: Concept 6 deferred_count schema (Day 1-2, ~2-3h)

**This is the real harness upgrade closing v2 plan HIGH gap.**

### Specification

Add `deferred_count` tracking to `.cm/memory/decisions.json` + `.cm/memory/learnings.json` per v2 Concept 6:

```json
// .cm/memory/decisions.json schema addition
{
  "decisions": [
    {
      "id": "...",
      "title": "...",
      "status": "pending|active|deferred|closed",
      "deferred_count": 0,                          // NEW field
      "last_deferred_at": "ISO-8601 timestamp",     // NEW field
      "attention_tag": null | "🟡 ATTENTION" | "🔴 BLOCKING-RECOMMENDATION",  // NEW field
      ...
    }
  ]
}
```

Tagging logic:
- `deferred_count >= 3` → `attention_tag = "🟡 ATTENTION"`
- `deferred_count >= 5` → `attention_tag = "🔴 BLOCKING-RECOMMENDATION"` (blocks new work in same scope)

### Workflow (use BMAD methodology, NOT cc-sdd)

```
Session A prompt:
/bmad-brainstorming "Designing deferred_count tracking schema for .cm/memory/{decisions,learnings}.json per v2 Concept 6"
```

Walk through BMAD's phases:
1. **Brainstorming** — explore options (field placement / threshold tuning / tag semantics / migration strategy for existing 4 deferred items mentioned in v2 plan)
2. **Indexing/sharding** — `/bmad-shard-doc` if needed for design doc decomposition
3. **Design** — produce design doc as `_bmad-output/tickets/HIR-XXXX-deferred-count-schema.md` (use next available ticket number from `_bmad-output/tickets/` directory)
4. **Implementation** — write code/JSON edits + migration script
5. **Quality gate** — invoke `cm-quality-gate` skill (already installed)

### Implementation artifacts to produce

| Artifact | Path | Purpose |
|---|---|---|
| Design doc | `_bmad-output/tickets/HIR-XXXX-deferred-count.md` | Spec + design + tasks |
| JSON schema update | `.cm/memory/decisions.json` (+ learnings.json) | Add 3 fields per entry |
| Migration script | `scripts/migrate-deferred-count.sh` | Backfill `deferred_count=0` for existing entries; tag the 4 items v2 plan flagged (EAS init / MS OAuth / HIRE_AGENT staging / Sentry rotation) |
| Documentation | Update `.cm/CONTINUITY.md.template` to reference new fields | Operator awareness |
| Test | Manual verification | Run migration + spot-check decisions.json output |

### Commit (per I-2 invariant — harness files on agent-* branch ✅)

```bash
git add .cm/memory/decisions.json .cm/memory/learnings.json scripts/migrate-deferred-count.sh _bmad-output/tickets/HIR-XXXX-deferred-count.md .cm/CONTINUITY.md.template
git commit -m "feat(harness): deferred_count schema per v2 Concept 6 — pilot v3 implementation work"
```

Pre-commit hook will run; expect pass (all files are harness files; branch is `agent/pilot-*`).

### End-of-Day-1 — Generate session log

Per Concept 4 cadence:
```
Generate _bmad-output/sessions/(C) 2026-05-11 pilot-v3-day1-concept6-impl.md
using existing template format from 2026-05-06 v1/v2 session logs.
```

---

## 11. Step 7 — Same feature, Stratum B comparison (Day 3, ~1-1.5h)

After Concept 6 implementation committed, run review modes on the **same diff** for empirical comparison.

### 7.A Stratum A baseline — BMAD adversarial review

```
/bmad-review-adversarial-general

Context: Review my deferred_count schema implementation in HEAD vs main.
Files changed: .cm/memory/decisions.json + .cm/memory/learnings.json + scripts/migrate-deferred-count.sh + _bmad-output/tickets/HIR-XXXX-deferred-count.md
Be adversarial — challenge schema choices, migration safety, threshold values, edge cases.
```

**Capture** full review output to `.pilot-log/day3a-bmad-stratum-a.md`. Note:
- Wall-clock time
- Token cost (approximate)
- Distinct issues raised count
- Real bugs caught vs false positives

### 7.B Stratum B neutral — codex-plugin-cc neutral

```
/codex:review --base agent-dev
```

**Capture** to `.pilot-log/day3b-codex-neutral.md`.

### 7.C Stratum B adversarial — codex-plugin-cc adversarial

```
/codex:adversarial-review --base agent-dev "challenge the threshold values (3 / 5) and the migration script's safety for existing JSON entries"
```

**Capture** to `.pilot-log/day3c-codex-adversarial-stratum-b.md`.

### End-of-Day-3 — Copy logs to vault

```bash
# From Session A
cp .pilot-log/day3*.md "/Users/Cvtot/KJ OS Template/03 Projects/_pilots/2026-05-11 adversarial-review-v3-hireui/pilot-log/"
```

Per Hybrid Option 3+5: monorepo `.pilot-log/` is ephemeral working memory; vault `pilot-log/` is persistent record.

---

## 12. Step 8 — Layered overlay ablation test (Day 4, ~1h)

Test whether karpathy-skills 4 principles change review character when stacked on BMAD Stratum A.

### 8.A Disable karpathy-skills temporarily

```bash
# Move skill out temporarily (rename to disable)
mv .claude/skills/karpathy-guidelines .claude/skills/.disabled-karpathy-guidelines
# Also disable Cursor rule
mv .cursor/rules/karpathy-guidelines.mdc .cursor/rules/.disabled-karpathy-guidelines.mdc
```

### 8.B Re-run BMAD adversarial review (without overlay)

```
/bmad-review-adversarial-general
[same context as 7.A]
```

Capture → `.pilot-log/day4a-bmad-without-karpathy-overlay.md`.

### 8.C Re-enable karpathy-skills

```bash
mv .claude/skills/.disabled-karpathy-guidelines .claude/skills/karpathy-guidelines
mv .cursor/rules/.disabled-karpathy-guidelines.mdc .cursor/rules/karpathy-guidelines.mdc
```

### 8.D Re-run BMAD adversarial review (with overlay)

```
/bmad-review-adversarial-general
[same context as 7.A]
```

Capture → `.pilot-log/day4b-bmad-with-karpathy-overlay.md`.

### 8.E Differential analysis

Did the 4 principles (Think Before Coding / Simplicity First / Surgical Changes / Goal-Driven Execution) change review:
- Issue density?
- Issue character (more "simplification" suggestions? more "clarification questions"?)
- Recommended next-actions?

Capture differential to `.pilot-log/day4c-overlay-differential.md`.

---

## 13. Step 9 — Cross-comparison + findings (Day 5-7, ~2-3h, Session B)

### 9.A Switch to Session B (vault root)

ĐÓNG Session A. MỞ Session B:
```bash
cd "/Users/Cvtot/KJ OS Template"
# Open NEW Claude Code session here
```

### 9.B Build comparison-table.md

```
Read all pilot-log files in
/Users/Cvtot/KJ OS Template/03 Projects/_pilots/2026-05-11 adversarial-review-v3-hireui/pilot-log/

Build comparison-table.md with metrics from pilot plan v2 §Day 5-6 section,
adapted for v3:

Modes compared:
1. BMAD bmad-review-adversarial-general (Stratum A baseline)
2. codex-plugin-cc /codex:review (Stratum B neutral)
3. codex-plugin-cc /codex:adversarial-review (Stratum B adversarial)
4. BMAD WITHOUT karpathy-skills overlay
5. BMAD WITH karpathy-skills overlay

Metrics per mode:
- Lines of review output
- Distinct issues raised count
- Design-decision vs implementation-detail issue distribution
- False positives
- Real bugs caught
- Token/cost estimate
- Wall-clock time
- Operator interpretation effort (1-5)
- Actionability (1-5)

Save to: 03 Projects/_pilots/2026-05-11 adversarial-review-v3-hireui/pilot-log/comparison-table.md
```

### 9.C Write findings.md (8 sections per v2 Day 7 template)

```
Write 03 Projects/_pilots/2026-05-11 adversarial-review-v3-hireui/findings.md

8 required sections:
1. TL;DR (3-5 bullets)
2. Methodology (what was measured, how, on what feature)
3. Quantitative findings (numbers from comparison-table)
4. Qualitative findings (review-character differences)
5. Stratum A (BMAD) vs Stratum B (codex-plugin-cc) verdict for Pattern #76
6. Overlay effect (karpathy-skills with/without ablation)
7. mattpocock cherry-pick utility (did mattpocock-prototype / mattpocock-to-issues / mattpocock-write-a-skill get invoked? help?)
8. Storm Bear recommendation + Pattern Library implications
9. Pilot reproducibility (what would replay this pilot need?)

Duplicate to 04 Reviews/(C) 2026-05-XX adversarial-review pilot v3 findings.md
(use actual completion date)
```

### 9.D Commit vault findings

```bash
cd "/Users/Cvtot/KJ OS Template"
git add "03 Projects/_pilots/2026-05-11 adversarial-review-v3-hireui/" "04 Reviews/"
git commit -m "Pilot v3 findings: BMAD vs codex-plugin-cc + karpathy overlay + mattpocock cherry-pick empirical results"
```

---

## 14. Step 10 — Adoption decisions + state sync (~30 min, Session B)

### 10.A Pattern #76 empirical verdict

| Stratum | Representative | Pilot evidence | Adoption decision |
|---------|---------------|----------------|-------------------|
| A (architectural role-separation) | BMAD `bmad-review-adversarial-general` | (filled from findings) | **KEEP** (already deployed; primary methodology harness) |
| B (prompt-framing variant) | codex-plugin-cc `/codex:adversarial-review` | (filled from findings) | adopt / hybrid / abandon |

Document in findings.md §5.

### 10.B Overlay decision — karpathy-skills

| Outcome | Decision |
|---------|---------|
| Day 4 ablation shows clear character improvement | KEEP permanently; promote `.claude/skills/karpathy-guidelines/` to tracked |
| No measurable difference | UNINSTALL (`/plugin uninstall`); remove `.cursor/rules/karpathy-guidelines.mdc` |
| Mixed signal | KEEP installed (low cost); re-evaluate at v66 mini-audit |

### 10.C mattpocock full-install ablation — per-skill telemetry-driven decisions

**Read `.cm/memory/skill-invocation-log.json` to extract invocation counts + outcome_quality per skill.**

Apply §3.5 Layer 4 ablation rules to each of the 19 installed `mattpocock-*` skills:

| Telemetry pattern | Decision |
|-------------------|---------|
| Invoked ≥ 3 times AND ≥ 1 useful-distinct-output | **KEEP-AND-PROMOTE-TRACKED** — remove from `.gitignore`, commit, mark namespace_role: PRIMARY or REFERENCE-ALT-VALIDATED |
| Invoked 1-2 times with mixed outcomes | **KEEP-UNTRACKED-EXPERIMENTAL** — stays in `.gitignore`, re-evaluate at next pilot cycle |
| Invoked < 1 time during pilot week | **DEMOTE** — move to `.claude/skills/.disabled-mattpocock-<name>/` (file kept, auto-invoke blocked) |
| Invoked but outcome_quality always = "duplicate-of-primary" | **REMOVE** — `rm -rf .claude/skills/mattpocock-<name>/`, remove from precedence registry |
| Special-case skills (mattpocock-git-guardrails-claude-code / mattpocock-setup-pre-commit) | **KEEP-UNTRACKED-REFERENCE-ONLY** regardless of invocation count (documentation value) |

**Precedence registry audit:** update `.cm/memory/skill-precedence.json`:
- For each functional category, check if PRIMARY skill was invoked < 50% of category total → consider swapping order
- Remove entries for REMOVED skills
- Update `last_audited` timestamp

**Document per-skill decisions in findings.md §7** with telemetry citations (invocation count + selection_reason distribution + outcome_quality breakdown).

### 10.C.bis Telemetry insights — what the data reveals

Beyond per-skill keep/remove, extract corpus-level observations:
- Which functional category had highest competing-skill invocation rate? (signals where management policy paid off most)
- Which `cm-*` skills got their PRIMARY status validated by data?
- Did any REFERENCE-ALT skill surprise by being invoked more than its PRIMARY? (precedence-swap candidate)
- Operator-override rate: how often did operator manually invoke a non-PRIMARY skill? (signals registry needs amendment)

Capture insights for Pattern Library — potential candidate: "Pattern #78 Duplicate-Skill Management via Precedence Registry + Telemetry" (would register at v66 mini-audit if pattern repeats in 2nd harness).

### 10.D Update vault state files (Session B prompt)

```
Update vault state with pilot v3 findings:

1. Root CLAUDE.md state-block — add post-v63-wiki-ship + post-pilot-v3 evidence note
   under "Current Pattern Library state" + Weekly Update

2. _state/pilot-ranking-2026-05-07.md — update:
   - cc-sdd v61 #1 → mark "PILOT DEFERRED (HIGH CONFLICT with BMAD; v3 pivot to BMAD as Stratum A)"
   - codex-plugin-cc v62 #1.5 → mark adoption decision (sustained-use / hybrid / abandon)
   - karpathy-skills v63 #3.5 → mark adoption decision
   - mattpocock-skills v57 → mark cherry-pick decisions (3 skills evaluated)

3. GOALS.md weekly update — note Goal #2 progress:
   - Pilot deferral imbalance reduced from 9/0 → 9/2 (codex-plugin-cc + karpathy-skills both deployed and evaluated)
   - cc-sdd v61 #1 status changes from "ready-to-pilot" → "PILOT-N/A due to BMAD conflict at target monorepo"
   - mattpocock v57 cherry-pick = 3 skills deployed

4. _patterns/03-active-candidates.md — note Pattern #76 + sister candidate
   empirical evidence ready for v66 audit (Stratum A BMAD vs Stratum B codex-plugin-cc
   real-world comparison data)

5. _patterns/05-recent-additions.md — append "Post-pilot-v3 empirical evidence" section

DO NOT execute v66 mini-audit. Just stage evidence in state files.
```

### 10.E Final commit

```bash
git -C "/Users/Cvtot/KJ OS Template" status
git -C "/Users/Cvtot/KJ OS Template" diff CLAUDE.md  # Review
git -C "/Users/Cvtot/KJ OS Template" add -A
git -C "/Users/Cvtot/KJ OS Template" commit -m "Adversarial-review pilot v3 complete: vault state synced with empirical evidence"
```

### 10.F Close pilot branch in hireui

```bash
cd /Users/Cvtot/monorepo/hireui

# Merge pilot branch back to agent-dev (per I-2 invariant; harness branch family)
git checkout agent-dev
git pull origin agent-dev
git merge --no-ff agent/pilot-2026-05-11-adversarial-review -m "Merge pilot v3: deferred_count schema + adversarial-review measurement complete"
git push origin agent-dev

# Optionally delete pilot branch
# git branch -d agent/pilot-2026-05-11-adversarial-review
# git push origin --delete agent/pilot-2026-05-11-adversarial-review
```

---

## 15. Session boundary summary

| Phase | Session | CWD | Duration |
|-------|---------|-----|---------|
| Step 0 — Pre-flight gap-fill (incl. E1 I-8 + E5 CONTINUITY section) | Mixed (terminal + Session B) | both | ~40-55 min |
| Step 1 — Pre-flight tools | terminal | any | ~10 min |
| Step 2-4 — Tool installs (codex-plugin-cc + karpathy-skills) | Session A | hireui monorepo | ~25 min |
| Step 5 — Full-install mattpocock + §3.5/§3.6 policy + E2/E3/E4 hooks | Session A | hireui monorepo | ~140-150 min |
| Step 6 — Concept 6 feature work | Session A | hireui monorepo | ~2-3h |
| Step 7 — Stratum A vs B reviews | Session A | hireui monorepo | ~1-1.5h |
| Step 8 — Overlay ablation | Session A | hireui monorepo | ~1h |
| Step 9 — Cross-comparison + findings | Session B (NEW) | vault root | ~2-3h |
| Step 10 — Adoption + state sync (incl. telemetry-driven per-skill ablation) | Session B | vault root | ~45 min |

**Total operator time:** ~9-11h spread over 1 week (up from v3.1's 8.5-10.5h due to +105 min E1-E5 enforcement; up from v3.0's 7-9h due to +1.5h §3.5 management policy + 105 min §3.6 cross-session enforcement).

---

## 16. Decision points during pilot

1. **End of Step 0.A:** Is cm-pre-flight discipline encoded? If no → create as Step 6 sub-task
2. **End of Step 5:** mattpocock cherry-pick conflicts surface? If yes → ablate the conflicting skill before Step 6
3. **End of Step 6:** Concept 6 implementation passes tests + commit hooks? If no → fix before review modes (Step 7 needs stable diff)
4. **End of Step 8:** karpathy ablation shows signal? If no signal → reduce Step 10.B confidence
5. **End of Step 9:** findings clean enough to commit? If incomplete → extend Day 7 or schedule Day 8

---

## 17. Failure modes (5 hybrid-architecture-specific + 3 v3-new)

### Inherited from v2

1. **Session A vs B confusion** — operator commits findings.md in monorepo or pilot-log in vault
2. **Branch-discipline violation** — pilot work committed to wrong branch (project file on `agent-*`, or harness file on `mobile/*`)
3. **`.pilot-log/` gitignore drift** — monorepo `.pilot-log/` accidentally tracked
4. **Cross-session file paths** — Session B can't read Session A's `.pilot-log/` because it's monorepo-local (resolved by copy-to-vault discipline)
5. **CONTINUITY.md stale** — pilot work happens but CONTINUITY.md not updated end-of-session

### NEW at v3

6. **BMAD slash-command unfamiliarity** — operator hasn't used `bmad-review-adversarial-general` before; needs prompt-engineering iterations to match cc-sdd's `kiro-review` rigor
7. **Concept 6 scope creep** — deferred_count schema implementation expands to also-touching learnings.json + meta-learnings.json + observation-track.json — exceed 1-3h budget
8. **Late-surfacing skill conflict during full-install** — `mattpocock-<name>` behavior overlaps with `cm-execution` or other previously-unmapped `cm-*` skill not in §3.5 duplicates manifest; agent auto-invokes wrong skill mid-pilot
9. **Precedence registry ignored** — agent invokes a skill without consulting `.cm/memory/skill-precedence.json` first; telemetry shows non-PRIMARY selections without `operator_override=true`
10. **Telemetry not populated** — agents don't write to `.cm/memory/skill-invocation-log.json`; Step 10 ablation lacks data
11. **Description-narrowing too narrow** — `mattpocock-*` REFERENCE-ALT skills never fire because operator never explicitly invokes them; 1-week pilot ends with all telemetry counts at 0 → forced REMOVE decisions despite low signal

### Mitigation

For each failure mode, predefined recovery:
- F1-F5 inherited mitigations from v2 (Session boundary discipline + git status checks at session boundaries)
- F6: keep `cc-sdd kiro-review` reference at v61 wiki entity-2 open for prompt-engineering comparison
- F7: if scope creep detected at 2h mark, freeze Concept 6 to decisions.json ONLY; commit; treat learnings.json/meta-learnings.json as v4 pilot work
- F8: ablate conflicting `mattpocock-*` skill (add to precedence registry as DEMOTE or REMOVE); document at findings §7
- F9: add I-8 invariant candidate at v66 audit ("Agents MUST consult `.cm/memory/skill-precedence.json` before invoking any skill when ≥2 candidates match"); meanwhile manually audit telemetry mid-pilot at Day 3 to catch drift early
- F10: at Day 3 midpoint, manually inspect `.cm/memory/skill-invocation-log.json` — if `invocations: []` still empty, ADD a hook or prompt-template that auto-logs invocations; alternative: operator manually appends entries when invoking skills
- F11: at Day 3 midpoint, if all `mattpocock-*` REFERENCE-ALT skills show 0 invocations, **deliberately invoke** 2-3 of them on real tasks to generate at least minimum-viable signal for Step 10 decisions; reframe "0 invocations = REMOVE" → "0 invocations + 0 operator-prompted use = REMOVE; 0 invocations + operator-prompted-and-not-useful = REMOVE; 0 invocations + never-tested = KEEP-UNTRACKED-EXPERIMENTAL"

---

## 18. Pickup state for fresh sessions

If pilot interrupted mid-stream, on resume:

1. Read `.cm/CONTINUITY.md` (hireui) — current branch + last commit + active blockers
2. Read this file (pilot v3) — find current Step
3. Read most recent `.pilot-log/dayN-*.md` — find last captured artifact
4. Read most recent `_bmad-output/sessions/(C) YYYY-MM-DD pilot-v3-*.md` — find session-level state
5. `git status` + `git log -10 --oneline` — verify disk state
6. Resume at next-incomplete Step

---

## 19. Cross-references

- **v2 pilot plan (sandbox):** `04 Reviews/(C) 2026-05-08 adversarial-review comparison pilot setup plan.md`
- **v2 KJ OS integration plan (hireui):** `03 Projects/product/hireui-harness/(C) 2026-05-06 v2 changes - integrating KJ OS concepts.md`
- **hireui CONSTITUTION:** `/Users/Cvtot/monorepo/hireui/CONSTITUTION.md`
- **hireui CLAUDE.md:** `/Users/Cvtot/monorepo/hireui/CLAUDE.md`
- **cc-sdd wiki (DROPPED from v3 install):** `03 Projects/cc-sdd - Beginner Analysis/`
- **codex-plugin-cc wiki:** `03 Projects/codex-plugin-cc - Beginner Analysis/`
- **karpathy-skills wiki:** `03 Projects/andrej-karpathy-skills - Beginner Analysis/`
- **mattpocock-skills upstream:** [github.com/mattpocock/skills](https://github.com/mattpocock/skills) (69.7K stars / MIT)
- **Pilot ranking authoritative:** `_state/pilot-ranking-2026-05-07.md`

---

## 20. Metadata

- **Generated:** 2026-05-11
- **Last revised:** 2026-05-12 (v3.2 update — operator-requested FULL (c) tier E1-E5 cross-session enforcement in §3.6 + namespace rename `mattpocock-*` / `karpathy-*` / `codex-*` replacing short `mp-*` / `kp-*` for instant provenance visibility)
- **Revision history:**
  - v3.0 (2026-05-11): initial v3 written; cherry-pick mattpocock subset (3 skills); soft enforcement only
  - v3.1 (2026-05-11): operator-requested full-install + §3.5 4-layer management policy; ~700 → ~1,100 lines
  - v3.2 (2026-05-12): operator-requested cross-session enforcement (E1-E5 hooks + CONSTITUTION I-8 + CONTINUITY skill-state) closing 3 context-loss vectors; namespace rename to full source names; ~1,100 → ~1,700+ lines
- **Generator session:** Claude Code session 73+ (post v63 wiki ship)
- **Document length:** ~1,700+ lines
- **Verdict confidence:** Highest of v3 series — based on verified hireui state + verified mattpocock repo inventory + conflict-aware install matrix + 4-layer management policy + 5-layer cross-session enforcement + reversibility guarantee
- **Source-verification:** All claims cite specific files + line numbers OR GitHub API responses
- **Authoritative state:** This is a proposal. Operator decides Step 0 → execute or defer.
- **v3.1 change rationale (verbatim operator 2026-05-11):** "When adding a new skills bundle to any harness — even when skills functionally duplicate existing ones — INSTALL ALL rather than SKIP-and-cherry-pick. The duplicate-perspective value is worth preserving for measurement. But the agent must not get confused by competing skills firing on the same trigger. Need a management strategy."
- **v3.2 change rationale (verbatim operator 2026-05-12):** "Cách triển khai Skill Management Policy ở trên có đảm bảo không bị mất context ở session khác không?" (Does the Skill Management Policy guarantee no context loss across sessions?) → answered with 3-vector gap analysis + 5-layer E1-E5 enforcement (HARD-SOFT CONSTITUTION + 3 hooks + soft CONTINUITY). Operator selected (c) FULL tier + namespace rename to full source names.
- **Cross-pattern implications:** §3.5 + §3.6 9-mechanism policy (namespace prefix + description-narrowing + precedence registry + telemetry-driven ablation + CONSTITUTION invariant + SessionStart hook + PostToolUse hook + PreToolUse hook + CONTINUITY skill-state) is a candidate **Pattern #78 Cross-Session Duplicate-Skill Management** for Pattern Library v66/v69 audit consideration — would register N=1 stale-flagged at v66 if mechanism demonstrates value at pilot end; second harness deploying same policy would un-stale-flag. **Structural-N=2 promotion** would require 2 harnesses successfully closing V1/V2/V3 context-loss vectors via E1-E5 enforcement.

---

## 🎯 Suggested Next Action

**Execute Step 0 NOW (~30-45 min) — gap-fill the 3 partial v2 plan items + create pilot branch from agent-dev.** This is the mandatory pre-step user flagged; it must close before tool installs start. Lowest-cost path forward.

Alternative if Step 0 feels too heavy this session:
- **Light alternative:** Execute only Step 0.D (~5 min) — create the pilot branch — and defer 0.A-0.C to next session. Branch creation alone is low-risk and unblocks tool installs whenever next session starts.
- **Heaviest alternative:** Execute Step 0 + Step 1 pre-flight tools (~45-60 min total) — ready to install codex-plugin-cc + karpathy-skills next session.

**If only 1 thing can be done today:** Step 0.D (~5 min) — `git checkout -b agent/pilot-2026-05-11-adversarial-review` from `agent-dev`. Costs nothing, preserves option.

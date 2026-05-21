# Pilot 1 — router-multimodel setup plan

> **Status:** PLAN — for operator review before execution. **No commands have been run.**
> **Drafted:** 2026-05-21
> **Drafted by:** Claude (autopilot-research session)
> **Pilot pattern source:** [[wiki/harness-engineering/personal-repo-router-multimodel|personal-repo-router-multimodel]] (howznguyen blog 2026-05-19, commit `844275d`)
> **Pilot type:** Tier-A operationally pilotable, individual-scale
> **Estimated total time:** ~1h setup + 30 days measurement window
> **Reversibility:** Full (delete settings.json overrides + kill router process)

This plan walks the operator through deploying howznguyen's cross-vendor multi-model pattern on the operator's primary working machine. The pattern routes Claude Code's 3 model slots (opus/sonnet/haiku) via a local router process to different upstream providers — opus→Kiro (Claude Opus 4.6 supervisor), sonnet+haiku→Codex (GPT-5.5 sub-agent executor).

The plan is structured for review-before-execution: each step has an EXECUTE annotation, prerequisites are explicit, and decision gates appear at risky transitions.

---

## Part 1 — Prerequisites checklist

Complete this checklist BEFORE running any setup commands. If any prerequisite is missing, document the gap and decide whether to acquire-then-proceed or defer the pilot.

### Account / API access

- [ ] **Kiro account with Claude Opus 4.6 API access**
  - Kiro is the provider exposing Claude Opus 4.6 used by howznguyen
  - **Verify:** can you generate an API key for Kiro right now? If unknown, this is a blocker — research Kiro signup/pricing first
  - **Cost model:** unknown to this plan; investigate before committing

- [ ] **Codex (OpenAI) account with GPT-5.5 API access**
  - Codex / OpenAI account for sub-agent executor
  - **Verify:** existing API key OR ability to provision one
  - **Cost model:** OpenAI per-token billing applies; sub-agent invocations rack up GPT-5.5 inference cost

- [ ] **9Router or equivalent router/proxy installed**
  - 9Router is howznguyen's choice (https://9router.com)
  - **Alternatives** documented in the source article: OmniRoute (https://omniroute.online), CLI API Proxy, any router exposing Anthropic/OpenAI-compatible endpoint
  - **⚠️ AUDIT-ABILITY GAP:** 9Router is a black box per the wiki article. Operator should investigate licensing, open-source status, and security posture BEFORE routing production credentials through it
  - **Decision gate:** if 9Router is closed-source and the operator cares about credential auditability, switch to a self-hosted alternative (e.g., LiteLLM proxy) at this step

### Tooling

- [ ] **Claude Code installed** on operator's primary machine
  - Verify with `claude --version` (or your install path equivalent)
  - **Required:** a version of Claude Code that respects the `ANTHROPIC_DEFAULT_OPUS_MODEL` / `_SONNET_MODEL` / `_HAIKU_MODEL` env-equivalent settings.json keys
  - **Pre-flight check:** read `claude --help` or docs to confirm these config keys exist in your installed version. **The pattern depends on this config schema not changing.**

- [ ] **`curl` available** for smoke tests
- [ ] **Existing `~/.claude/settings.json` backed up** before overrides applied (next step writes to this file)

### Sandbox project

- [ ] **A non-production sandbox repo identified** for the pilot
  - Avoid running the pilot on a repo with sensitive secrets or production deployment paths
  - Ideal: a personal side-project or a duplicate of a real codebase used for experimentation
  - **Reason:** if the router or any model misbehaves, blast radius stays bounded

### Knowledge prereqs

- [ ] Operator has read [[wiki/harness-engineering/personal-repo-router-multimodel|personal-repo-router-multimodel]] in full
- [ ] Operator understands the task-allocation rubric (Opus should-do / GPT should-do / sub-agent NEVER-do without plan)
- [ ] Operator has identified 3-5 concrete task types to test the pattern on (e.g., "add a new test file", "research codebase pattern X", "implement function Y")

---

## Part 2 — Setup (estimated ~1 hour)

### Step 2.1 — Backup existing Claude Code config

```bash
# EXECUTE — backup before overriding
mkdir -p ~/.claude/backup
cp ~/.claude/settings.json ~/.claude/backup/settings.json.pre-router-pilot.$(date +%Y%m%d-%H%M%S) 2>/dev/null || echo "no existing settings.json — fresh install"
```

**Verify:** if settings.json existed, you should see a timestamped backup in `~/.claude/backup/`. If not, a fresh install is fine; you'll create settings.json in step 2.4.

### Step 2.2 — Install router

This step is router-specific. **Operator chooses one** based on Part 1 audit-ability decision.

**Option A — 9Router** (howznguyen's choice; closed-source, audit-ability gap):

```bash
# EXECUTE — follow 9Router's documented install procedure at https://9router.com
# (The blog post does not include exact install commands; operator must follow vendor docs.)
# After install, 9Router runs as a local process on port 20128 by default.
```

**Option B — LiteLLM proxy** (open-source alternative; recommended if audit-ability matters):

```bash
# EXECUTE — install LiteLLM proxy
pip install 'litellm[proxy]'

# Create a config file mapping route names to providers
cat > ~/.litellm-router-config.yaml <<'YAML'
model_list:
  - model_name: kr/claude-opus-4.6
    litellm_params:
      model: claude-opus-4.6  # or whatever Kiro's actual model ID is
      api_base: <KIRO_API_BASE_URL>
      api_key: os.environ/KIRO_API_KEY
  - model_name: cx/gpt-5.5
    litellm_params:
      model: gpt-5.5  # or whatever OpenAI/Codex's actual model ID is
      api_base: <CODEX_API_BASE_URL>
      api_key: os.environ/OPENAI_API_KEY
YAML

# Start the proxy
litellm --config ~/.litellm-router-config.yaml --port 20128
```

**⚠️ FLAGS for review:**
- The exact Kiro API endpoint + model identifier is not in this plan. Operator must verify against Kiro's docs before running.
- LiteLLM config format is current as of 2026-05; verify against latest LiteLLM docs at execution time.

### Step 2.3 — Smoke-test the router

Verify the router process is alive and answers HTTP requests.

```bash
# EXECUTE — confirm router is up
curl -s http://127.0.0.1:20128/v1/models -H "Authorization: Bearer $ROUTER_API_KEY" | jq . | head -30
```

**Expected:** JSON response listing the routes you configured (`kr/claude-opus-4.6`, `cx/gpt-5.5`). **If you get connection-refused:** router didn't start; check logs, retry step 2.2.

**⚠️ Decision gate:** if the router doesn't smoke-test green in 10 minutes of troubleshooting, STOP the pilot, document the failure in `output/`, and revisit. Don't continue with a broken router.

### Step 2.4 — Configure Claude Code to use the router

Write `~/.claude/settings.json` per howznguyen's pattern:

```bash
# EXECUTE — write Claude Code settings (overrides any pre-existing settings.json)
cat > ~/.claude/settings.json <<'JSON'
{
  "ANTHROPIC_BASE_URL": "http://127.0.0.1:20128/v1",
  "ANTHROPIC_AUTH_TOKEN": "YOUR_ROUTER_API_KEY_HERE",
  "ANTHROPIC_DEFAULT_OPUS_MODEL": "kr/claude-opus-4.6",
  "ANTHROPIC_DEFAULT_SONNET_MODEL": "cx/gpt-5.5",
  "ANTHROPIC_DEFAULT_HAIKU_MODEL": "cx/gpt-5.5"
}
JSON
```

**⚠️ EDIT BEFORE EXECUTE:**
- Replace `YOUR_ROUTER_API_KEY_HERE` with the actual router API key (from Step 2.2)
- If the operator's existing `settings.json` had non-router keys (theme, hooks, etc.), those will be lost. **Re-add them manually** by referencing the backup from Step 2.1.

**Verify:**

```bash
# EXECUTE — check settings.json is valid JSON
jq . ~/.claude/settings.json
```

### Step 2.5 — Restart Claude Code

```bash
# EXECUTE — kill any existing Claude Code session (graceful)
# Then start fresh — exact command depends on your install method
claude --help | head -5   # verify Claude Code still runs after settings change
```

**If Claude Code refuses to start** after the settings change, restore from backup:

```bash
cp ~/.claude/backup/settings.json.pre-router-pilot.<timestamp> ~/.claude/settings.json
```

### Step 2.6 — Verify model routing end-to-end

In a new Claude Code session in the sandbox repo:

```
> What model are you?
```

**Expected:** the response should indicate the agent identifies as Opus (because opus slot now routes to Kiro Opus 4.6).

Then test sub-agent routing:

```
> spawn agent sonnet
> Task: respond with the single word "test" and nothing else
```

**Expected:** the sub-agent task completes with response "test". Behind the scenes, Claude Code dispatched to the sonnet slot, which the router forwarded to Codex GPT-5.5.

**⚠️ FAILURE MODES (from the wiki article):**
- **Sai model name / prefix** — route needs exact `kr/claude-opus-4.6` (not `claude-opus-4.6`); same for `cx/gpt-5.5`. Fix the settings.json values to match the router's exact route names.
- **Sai biến env** — Claude Code uses `ANTHROPIC_AUTH_TOKEN`, not `ANTHROPIC_API_KEY`. Double-check.
- **Stale session** — settings.json changes don't reload mid-session; restart Claude Code if smoke fails.
- **Format compatibility** — if router doesn't translate Anthropic API ↔ OpenAI API for the GPT route, smoke will fail with schema errors. LiteLLM handles this; verify 9Router does too.

---

## Part 3 — Measurement plan (30-day pilot window)

Track 3 axes. Establish baseline FIRST (pre-pilot), then measure pilot performance.

### Baseline week (week 0 — BEFORE flipping the router)

Operate Claude Code normally (no router) for 7 days. Track per-task:

| Metric | Source | Notes |
|---|---|---|
| **Credit cost per task** | Manual log OR Anthropic dashboard | If Anthropic dashboard doesn't break out per-session cost, estimate via token counts × current pricing |
| **Time to task completion** | Stopwatch on operator side | Wall-clock from "task started" to "task accepted" |
| **Task correctness** | Manual review of output | Binary OR 1-5 scale per task |
| **Task type** | Operator tag | One of: implement / refactor / test / docs / research / debug |

Record baseline in `04 Reviews/(C) 2026-05-XX-pilot-1-baseline.md` (operator-owned file). Aim for 20-30 baseline tasks across task types.

### Pilot weeks (weeks 1-4 — router active)

Same tracking, same task types. Aim for parity in task volume and type mix.

### Decision metric (30-day endpoint)

| Outcome | What it means | Recommended action |
|---|---|---|
| **Credit cost down ≥30%, correctness within ±10%** | Pilot succeeds — pattern is operationally viable | Continue with router setup; document in [[wiki/harness-engineering/personal-repo-router-multimodel\|wiki article]] as N=2 corroboration |
| **Credit cost down 10-30%, correctness within ±10%** | Marginal win — depends on operator's pain priority | Decide based on whether the operator's primary pain was cost or correctness |
| **Credit cost down <10%** OR **correctness down >10%** | Pilot fails | Revert to pre-pilot config; document what didn't work |
| **Sub-agent dispatch fails frequently** OR **router is unreliable** | Infrastructure failure | Pilot is inconclusive — try LiteLLM if 9Router was the choice (or vice versa); retry with cleaner router |

### Daily-log template

Recommended: keep a simple log file at `~/router-pilot-log.md` with entries like:

```
## 2026-05-XX
- Task: add error handling to billing/invoice.py
- Type: implement
- Pre-pilot baseline expected: $0.15, 4 min, correctness 4/5
- Actual (router): $0.08, 3 min, correctness 4/5
- Notes: sub-agent took the implement step; supervisor reviewed; correct on first attempt
```

---

## Part 4 — Reversal procedure

If pilot fails OR operator decides to abandon mid-pilot:

```bash
# EXECUTE — restore pre-pilot settings.json
cp ~/.claude/backup/settings.json.pre-router-pilot.<timestamp> ~/.claude/settings.json

# Kill the router process
# 9Router: depends on install method — check vendor docs
# LiteLLM: kill the proxy process by PID or pkill litellm

# Restart Claude Code
# Verify pre-pilot behavior restored
```

**Verify:** in a Claude Code session, the agent should once again identify as default Claude (not Opus 4.6 via router). Sub-agent spawning should dispatch to standard sonnet (not GPT-5.5).

---

## Part 5 — Pilot decision gates (review checkpoints)

Stop and reassess if any of these happen during the pilot:

| Trigger | Action |
|---|---|
| **Router process crashes >2x in first 48h** | Switch router (9Router ↔ LiteLLM) or abort |
| **Sub-agent failures >20% of dispatches in first week** | Investigate format compatibility OR abort |
| **Credit cost is HIGHER than baseline in first 3 days** | Investigate sub-agent over-invocation OR abort |
| **Sub-agent leaks credentials or accesses unintended files** | ABORT immediately; pattern's auth model (sub-agent inherits Claude Code permissions) is too loose for this operator |
| **Any production-impacting incident traced to the router** | ABORT immediately + investigate |

---

## Part 6 — Open questions to resolve before execution

Operator should answer these BEFORE starting Step 2.1:

1. **Which router?** 9Router (per howznguyen) or LiteLLM (open-source)? Decision drives Step 2.2 path.
2. **What's the realistic per-token cost of Kiro Opus 4.6?** This determines whether the cost-savings claim is plausible at the operator's task volume.
3. **What's the realistic per-token cost of Codex GPT-5.5?** Same — sub-agent invocations have to be cheap enough that delegation pays back.
4. **Does the operator's settings.json currently contain hooks, themes, or other configs** that will be wiped by Step 2.4? If yes, plan to re-add them.
5. **What sandbox repo will be used?** Identify and bound the pilot to that repo.
6. **What's the operator's baseline credit spend per week** in current Claude Code usage? Without this number, measuring "30% savings" is impossible.

---

## Part 7 — Post-pilot deliverable

At the end of the 30-day window, operator should produce:

- **`04 Reviews/(C) 2026-06-XX-pilot-1-router-multimodel-results.md`** — final write-up with:
  - Baseline week numbers (from week 0)
  - Pilot weeks numbers (weeks 1-4)
  - Comparison table
  - Decision: continue / abandon
  - Lessons learned
  - Cross-link to update [[wiki/harness-engineering/personal-repo-router-multimodel|personal-repo-router-multimodel]] with N=2 corroboration data (or N=1+falsification)

If the pilot succeeds, this becomes the second corpus source corroborating howznguyen's pattern — strong promotion-candidate signal for Storm Bear Pattern Library.

If the pilot fails, this becomes counter-evidence — equally valuable.

---

## Summary table for review

| Phase | Time | Reversible? | Risk level |
|---|---|---|---|
| Part 1 — Prerequisites | 30-60 min | N/A (no changes yet) | None (read-only audit) |
| Part 2.1 — Backup | 1 min | N/A | None |
| Part 2.2 — Install router | 15-30 min | Yes (uninstall) | Medium — depends on router choice + audit-ability |
| Part 2.3 — Smoke router | 5 min | N/A (read-only) | None |
| Part 2.4 — Update settings.json | 5 min | Yes (restore from backup) | Medium — affects Claude Code session behavior |
| Part 2.5 — Restart Claude Code | 5 min | Yes | Low |
| Part 2.6 — Smoke routing | 10 min | N/A (read-only) | None |
| Part 3 — Measurement | 30 days | N/A | None (observation phase) |
| Part 4 — Reversal | 5 min | N/A (this IS the reversal) | None |
| Part 5 — Decision gates | continuous | N/A | None (review-only) |

**Total operator-active time:** ~1.5h (setup) + ~5 min/day logging × 30 days = ~3.5h
**Total wall-clock time:** ~5 weeks (1 baseline week + 4 pilot weeks)

---

## Operator decision required BEFORE execution

- [ ] All Part 1 prerequisites checked
- [ ] All Part 6 open questions answered
- [ ] Router choice made (9Router vs LiteLLM)
- [ ] Baseline week 0 dates committed to calendar
- [ ] Sandbox repo identified
- [ ] Post-pilot write-up file path pre-created in `04 Reviews/` as a placeholder

When all checkboxes are checked, execute Part 2 in sequence. Otherwise, defer.

---

## Cross-links

- [[wiki/harness-engineering/personal-repo-router-multimodel|Pilot pattern source article]]
- [[wiki/harness-engineering/_index|harness-engineering topic index]]
- Future write-up location: `04 Reviews/(C) 2026-06-XX-pilot-1-router-multimodel-results.md` (operator creates after pilot completes)

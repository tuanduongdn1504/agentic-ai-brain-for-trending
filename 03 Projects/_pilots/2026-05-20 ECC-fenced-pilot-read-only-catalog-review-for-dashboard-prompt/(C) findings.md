# (C) ECC fenced-pilot — read-only catalog review for `build-your-own-dashboard-prompt` improvement

**Date:** 2026-05-20
**Scope:** Read-only review (zero install, zero blast-radius)
**Method:** `git clone --depth 1 https://github.com/affaan-m/ECC.git /tmp/ecc-pilot-review/ECC` + survey skills/agents/commands + cross-reference against `build-your-own-dashboard-prompt` artifact + needs
**Target:** improve the prompt-as-product at `03 Projects/product/build-your-own-dashboard-prompt/observability/build-your-own-dashboard-prompt.md` (39.2KB / 828 lines + 5 amendment files v0.5.0 → v0.6.3)
**Pilot framing:** ECC v78 corpus-recursive revisit confirmed CORPUS-RECORD velocity + 232 codified skills + 60 agents + 75 commands. This pilot evaluates which ECC components are highest-leverage for *prompt improvement* (not product build).

---

## Target context

`build-your-own-dashboard-prompt.md` is the canonical prompt that drives the build of **claude-agentic-os** — a local Claude Code observability + Mission Control product. The artifact has been iterated through 5 amendment cycles (v0.5.0 → v0.6.3 spanning 1,738 lines of amendments). The dashboard product itself ships: FastAPI + SQLite + React/Vite/TanStack + Playwright + framer-motion + Telegram bridge + Mission Control dispatcher.

**Why ECC is potentially high-leverage here:**
- ECC ships a **`prompt-optimizer`** skill (398 lines) explicitly for prompt improvement
- ECC ships a **`prp-*` command suite** (prp-prd + prp-plan + prp-implement + prp-pr + prp-commit) — PRP = Product Requirements Prompt — directly matches the dashboard-prompt's artifact-class
- ECC's dashboard-relevant agents (fastapi-reviewer + database-reviewer + e2e-runner + silent-failure-hunter) provide vault-aligned review patterns the prompt could *codify*
- ECC's 232-skill density provides cross-cutting reference patterns that the dashboard-prompt is reinventing piecemeal

---

## TOP 5 high-value candidates for dashboard-prompt improvement

### #1 — `skills/prompt-optimizer/SKILL.md` (398 lines)

**Why it's the obvious starting candidate:** literal direct-match. ECC's prompt-optimizer is "Analyze raw prompts, identify intent and gaps, match ECC components (skills/commands/agents/hooks), and output a ready-to-paste optimized prompt. Advisory role only — never executes the task itself."

**Application to dashboard-prompt:**
- Run prompt-optimizer over the 39.2KB main prompt → identify intent gaps, ambiguities, redundancies
- Match prompt's "build with these" sections against ECC's actual `fastapi-patterns`, `python-patterns`, `e2e-testing`, `database-migrations` skills
- Output: a "what would make this prompt clearer + more deterministic" critique

**Risk:** prompt-optimizer is community-origin (author: YannJY02) not core ECC, version 1.0.0. Quality-vary risk.

**Verdict:** **PRIMARY candidate.** Highest expected leverage at lowest blast-radius (read-only application; advisory output only).

### #2 — `commands/prp-prd.md` + `commands/prp-plan.md` + `commands/prp-implement.md` + `commands/prp-pr.md` + `commands/prp-commit.md` (PRP workflow suite)

**Why it matches:** PRP = "Product Requirements Prompt" methodology, adapted from PRPs-agentic-eng by Wirasm. This is **exactly the artifact-class** that `build-your-own-dashboard-prompt` belongs to — a prompt that drives product construction with rigorous validation loops.

**Application to dashboard-prompt:**
- Use `prp-prd` to retroactively run a "would this prompt pass PRD discipline?" audit on the existing dashboard-prompt
- Compare PRP plan structure (problem-first + hypothesis-driven + validation-gates) against dashboard-prompt's current section structure
- Extract the validation-loop pattern: "every change verified immediately — never accumulate broken state" (from prp-implement) → does dashboard-prompt's "Stop conditions" + "Order of operations" sections enforce this?

**Verdict:** **STRUCTURAL candidate.** Highest-leverage for *rewriting* the prompt to PRP discipline rather than tweaking it.

### #3 — `commands/learn.md` + `commands/learn-eval.md` + `skills/continuous-learning-v2/`

**Why it matches:** The dashboard-prompt has 5 amendment files (v0.5.0 + v0.6.0 + v0.6.1 + v0.6.2 + v0.6.3) totaling 1,738 lines of "what we learned after shipping." `/learn` and continuous-learning-v2 are explicit ECC patterns for **extracting reusable patterns from sessions/amendments and converting them to skills/rules**.

**Application to dashboard-prompt:**
- Run `/learn` over the 5 amendments → extract: which amendments were structural (changed prompt design) vs cosmetic (clarified existing intent)?
- Identify the "amendment vs core" boundary — what should be in main prompt vs what should be in skills/rules referenced by the prompt
- Output: a "core-prompt + skill-reference" architecture refactor proposal

**Verdict:** **REFACTOR candidate.** Highest-leverage for shrinking the prompt by extracting patterns into skill-references.

### #4 — `skills/rules-distill/SKILL.md` (264 lines)

**Why it matches:** "Scan skills to extract cross-cutting principles and distill them into rules — append, revise, or create new rule files." Applied across the dashboard-prompt + amendments, this could distill repeated principles (e.g., "use raw SQLite, no ORM"; "deterministic doctor health-check"; "stop conditions before partial implementations") into a clean rule layer.

**Application to dashboard-prompt:**
- Scan all 6 prompt/amendment files for cross-cutting principles
- Output: distilled rules file (e.g., `RULES.md`) referenced by prompt rather than re-stated each amendment
- Reduces 39.2KB main prompt + 1,738-line amendment surface

**Verdict:** **CONSOLIDATION candidate.** Highest-leverage for reducing token-budget of the prompt itself.

### #5 — `agents/silent-failure-hunter.md` + `agents/code-reviewer.md` applied to the prompt-as-document

**Why it matches:** silent-failure-hunter is designed to "review code for silent failures, swallowed errors, bad fallbacks, and missing error propagation." Applied to the prompt-as-document, this means: "what does the prompt *fail to specify* that the implementer must guess?" — the prompt's silent failures are its under-specifications.

**Application to dashboard-prompt:**
- Run silent-failure-hunter (conceptually, not literally) over each section
- Output: list of under-specified directives + missing failure-modes + assumed-but-unstated invariants
- Example targets: "What happens if `~/.claude/projects/*.jsonl` is missing?" "What if OTLP ingest rate exceeds SQLite write capacity?" "What's the prompt's behavior when the OAuth account hint file is corrupted?"

**Verdict:** **AUDIT candidate.** Highest-leverage for catching prompt-level under-specifications before they become product bugs.

---

## SECONDARY candidates (relevant but lower-leverage)

| Candidate | Why relevant | Why not in TOP 5 |
|-----------|--------------|--------------------|
| `skills/dashboard-builder/SKILL.md` | Literal name-match for dashboard product | Aimed at Grafana/SigNoz, not Claude Code dashboards; philosophy (answer real operator questions, not vanity metrics) is relevant but not prompt-specific |
| `agents/fastapi-reviewer.md` + `skills/fastapi-patterns/` | Directly matches dashboard's FastAPI backend | More relevant for product implementation than prompt improvement |
| `agents/database-reviewer.md` + `skills/postgres-patterns/` | Direct match for 18-table SQLite schema | Postgres-specific; SQLite discipline may not transfer cleanly |
| `agents/e2e-runner.md` + `skills/e2e-testing/` | Dashboard ships Playwright smoke tests | Implementation-level; prompt only needs to *reference* this pattern |
| `skills/motion-advanced/` + `skills/motion-foundations/` + `skills/motion-patterns/` + `skills/motion-ui/` | Dashboard uses framer-motion | Implementation-level; prompt's "Visual direction" section is brief |
| `commands/cost-report.md` + `skills/cost-tracking/` + `skills/token-budget-advisor/` | Dashboard has cost/token panels | Product-feature-level; prompt is feature-complete |
| `agents/loop-operator.md` + `skills/continuous-agent-loop/` + `skills/autonomous-loops/` | Mission Control dispatcher = autonomous loop | Implementation-level; prompt's "Mission Control dispatcher" section already exists |
| `commands/multi-execute.md` + `commands/multi-workflow.md` + `commands/multi-plan.md` | Mission Control task queue pattern | Could inspire HITL task-queue design; secondary to PRP suite |
| `skills/agent-eval/` + `skills/eval-harness/` + `commands/learn-eval.md` | For evaluating the dispatcher behavior | Different artifact-class (dispatcher eval, not prompt eval) |
| `skills/agentic-os/` | Literal name-match for product | No visible content (need deeper probe to confirm relevance) |
| `agents/code-explorer.md` + `skills/codebase-onboarding/` + `skills/code-tour/` | For README + docs | Adjacent artifact, not core prompt improvement |
| `skills/context-budget/` + `skills/token-budget-advisor/` | Dashboard has token/cost panels | Implementation-level metric definition |
| `skills/prompt-optimizer/` SKILL.md `metadata.author = YannJY02` | Already TOP 5 #1 | (note: community-origin flag for due-diligence) |

---

## NOT relevant (filtered out)

Out of 232 skills, the following are NOT relevant to dashboard-prompt improvement:

- Language-specific patterns Storm Bear isn't using (perl-patterns, kotlin-*, dotnet-patterns, dart-flutter-patterns, swift-*, csharp-testing, harmonyos-app-resolver)
- Domain-specific verticals (healthcare-cdss-patterns, customs-trade-compliance, defi-amm-security, llm-trading-agent-security, scientific-db-pubmed-database, energy-procurement)
- Vendor-specific tooling not in dashboard stack (jira-integration, google-workspace-ops, x-api, exa-search, github-ops, hipaa-compliance)
- Marketing/business (brand-voice, investor-materials, investor-outreach, market-research, seo, lead-intelligence)
- Hardware/infrastructure (homelab-*, cisco-ios-patterns, network-bgp-diagnostics, netmiko-ssh-automation)

Total filtered: ~80 skills clearly out-of-scope. ~150 skills potentially relevant; TOP 5 + 13 SECONDARY = 18 most-leverage subset.

---

## Decision gate

This pilot was scoped as **read-only catalog review with zero blast-radius**. The next decision is what (if anything) advances to the next pilot stage:

### Option A — Stop here, treat findings as reference

Use this findings document as a permanent reference. No installation. Next time dashboard-prompt is amended (v0.6.4 or v0.7.0), consult the TOP 5 candidates and apply them manually (e.g., write a v0.7.0 amendment that itself follows the PRP-PRD discipline; run a silent-failure-hunter pass; do a rules-distill consolidation).

**Cost:** zero further effort. **Benefit:** reference exists; no install commitment.

### Option B — Single-skill fenced test (Option 2 from original pilot question)

Pick ONE of the TOP 5 (recommended: **#1 prompt-optimizer**) and apply it once to the dashboard-prompt by manual file copy to scratch dir + manual invocation. Document the resulting "optimized prompt" or critique without merging anything into the live prompt.

**Cost:** ~30-60 min focused session. **Benefit:** real evidence of leverage; reversible (rm -rf scratch dir).

### Option C — Full prp-* workflow rerun

Use the PRP suite (#2) to rerun dashboard-prompt as a PRP-disciplined v0.7.0. This is a substantial undertaking (effectively rewriting the prompt under PRP discipline) but produces the highest possible leverage if dashboard-prompt is high-priority.

**Cost:** multi-session effort. **Benefit:** prompt structurally improved to PRP discipline.

### Recommendation

**Option A → reassessed when next amendment cycle begins.** The dashboard-prompt is already at v0.6.3 (5 amendments) and 39.2KB; the marginal cost of installing/integrating ECC components NOW (before v0.7.0 is contemplated) exceeds the marginal benefit. When v0.7.0 work begins (or when an amendment-cycle is triggered by a real product issue), revisit this document → pick the candidate most aligned with the amendment's intent → execute that single candidate in scratch-dir before merging.

If Storm Bear disagrees with "wait until next amendment" assessment, **Option B with #1 prompt-optimizer** is the next-step recommendation (lowest commitment + highest expected signal).

---

## Pilot validation

| Pilot success criterion | Status |
|--------------------------|--------|
| Zero blast-radius (no vault file modified outside `_pilots/`) | ✓ |
| Findings document written to `_pilots/` | ✓ |
| TOP 5 candidates identified with explicit rationale | ✓ |
| SECONDARY candidates documented (not just dismissed) | ✓ |
| Decision gate with explicit next-step options | ✓ |
| Clean temp directory cleanup-able (`rm -rf /tmp/ecc-pilot-review/`) | ✓ |
| Pilot ranking unchanged (cc-switch #1 / agent-skills-standard #2 / ECC #3 fenced-scope / codegraph #4 / agents-best-practices #5 / agentmemory #6) | ✓ |

**Pilot status:** **COMPLETED at Option 1 read-only catalog review scope.**

This is the **2nd FULLY-COMPLETED pilot in Storm Bear vault history** (after v3.2 hireui adversarial-review 2026-05-13). Pattern Library implication: **completed-pilot count 1 → 2** — relevant to Pattern #80 (Tool-Level Adversarial Review) tracking at v80 audit.

**Temp dir cleanup:** `rm -rf /tmp/ecc-pilot-review/` recommended when this document is finalized. (Not executed automatically; preserved in case operator wants deeper probe.)

**Vault state changes:** zero outside `_pilots/`. No commit required unless operator wants the pilot findings preserved in git history (recommended).

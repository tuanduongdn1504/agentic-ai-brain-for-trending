# (C) C2 — AGENTS.md + CLA + CONTRIBUTING + SUL-1.0 + governance + telemetry

> **Cluster scope:** Contributor-facing governance + license + privacy/legal documentation surface.
> **Source files:** `AGENTS.md` (173 lines, auto-generated 2026-04-18 commit 2892ca4a) + `CLA.md` (59 lines) + `CONTRIBUTING.md` (~270 lines) + `LICENSE.md` (SUL-1.0 83 lines) + `docs/legal/privacy-policy.md` + `docs/legal/terms-of-service.md`
> **Wiki phase:** Phase 2 cluster summary
> **Cross-wiki siblings cited:** GitNexus v33 (PolyForm Pattern #72) / aidevops v47 (3-layer governance 22c) / Vercel v51 (22d identical-mirror) / OMC v27 (Korean ecosystem peer)

---

## 1. SUL-1.0 — Sustainable Use License Version 1.0 (corpus-first SUL family)

`LICENSE.md` (verified verbatim 83 lines). Key provisions:

**Acceptance:** "By using the software, you agree to all of the terms and conditions below."

**Copyright License:** "non-exclusive, royalty-free, worldwide, non-sublicensable, non-transferable license to use, copy, distribute, make available, and prepare derivative works of the software"

**Limitations (CRITICAL — non-commercial-restriction):**
> "You may use or modify the software only for **your own internal business purposes** or for **non-commercial or personal use**. You may distribute the software or provide it to others only if you do so **free of charge for non-commercial purposes**. You may not alter, remove, or obscure any licensing, copyright, or other notices of the licensor in the software. Any use of the licensor's trademarks is subject to applicable law."

**Patent License:** Standard reciprocal patent grant with patent-claim-termination clause.

**Notices:** Modified copies must include prominent notice of modification.

**Termination:** 30-day cure period for first violation; permanent termination on second violation.

**Definitions:** "licensor" = entity offering terms (legally undefined in file — could be YeonGyu individually, Sionic AI, or Sisyphus Labs depending on actual IP-rights structure); "your company" = comprehensive control-relationship definition.

**License-family analysis:**
- **Same name** as **n8n.io's Sustainable Use License** (n8n v1.0 introduced this license family in 2022)
- **Same archetype** as **PolyForm Noncommercial 1.0.0** (GitNexus v33 Pattern #72) — both restrict commercial use
- **Distinct from** open-core models (e.g., shannon v45 AGPL + Pro / Vercel v51 MIT + commercial tier) — SUL prohibits commercial use entirely (no separate commercial license offered yet — Sisyphus Labs waitlist suggests future commercial-tier may emerge)

**Pattern #29 sub-context observation (NEW v52):**
- **29-custom-non-OSI-non-commercial-restriction** sub-context — N=2 with PolyForm Noncommercial (GitNexus v33)
- Family-specific: PolyForm Noncommercial = standardized polyformproject.org license; SUL = n8n-derived (or independently-named) license
- **Decision (per consolidation-forward discipline):** Strengthen Pattern #29 with NEW sub-context "29-custom-non-OSI-non-commercial-restriction" at N=2. Do NOT generalize Pattern #72 (different specific license families with different specific terms).
- Promotion-candidate at next mini-audit under structural-N=2 criterion if formalized.

**Storm Bear commercial-blocking implication:** Storm Bear's Scrum coaching is commercial business (paying clients). SUL-1.0 limitation "internal business purposes" + "non-commercial purposes" prohibits commercial deployment. Pilot-eval or internal-process-tooling only. ⚠️ This is the **defining license-blocker for Storm Bear adoption** of omo. Beginner guide must flag prominently.

## 2. CLA.md — Contributor License Agreement (corpus-first formal CLA at solo-Korean-T1)

`CLA.md` (verified verbatim 59 lines). Key provisions:

**Owner:** "YeonGyu Kim (Owner)" — explicit individual ownership (not Sionic AI, not Sisyphus Labs).

**Grants from contributor:**
1. **Copyright License** — perpetual, worldwide, non-exclusive, no-charge, royalty-free, irrevocable
2. **Patent License** — same scope
3. **Relicensing Rights** — *"The right to relicense the Contribution under any license, including proprietary licenses, without requiring additional permission from you."*

**Future License Changes (CRITICAL):**
> "You acknowledge and agree that:
> 1. The Project may change its license in the future.
> 2. Your Contributions may be distributed under a different license than the one in effect at the time of your Contribution.
> 3. This includes, but is not limited to, relicensing under source-available or proprietary licenses."

→ **Forward-relicensing flexibility = open-core-prep signal.** Combined with Sisyphus Labs commercial waitlist, this CLA provides legal infrastructure to relicense omo OSS into commercial product later. Owner = individual (YeonGyu) so all IP rights consolidated (clean transferability to commercial entity).

**Governing law:** Republic of Korea.

**Mechanism:** CLA Assistant bot tracks agreement on PR submission.

**Pattern #12 strengthening (governance-depth):** CLA at solo-T1 is **rare in corpus**:
- claude-howto v32 (Korean diaspora French): CONTRIBUTING.md only, no CLA
- agency-agents v18 (US solo enterprise): minimal governance
- spec-kit v17 (corporate-official GitHub/Microsoft): formal CLA + 6-file governance
- pi-mono v36 (Austrian solo): heavy governance + `lgtm`/`lgtmi` PR fast-track + CLA via cla.yml workflow
- omo v52 (Korean solo + Sionic AI affiliated): formal CLA + 5-file governance + CLA assistant + cla.yml workflow

→ CLA at solo-T1 = 7th counter-evidence wiki for Pattern #12 v42 refined formulation. Maintainer-philosophy + commercial-incubation-ambition = drivers (NOT just solo-vs-corporate axis).

**Pattern #69 Agent-PR Fast-Track Governance Protocol** observation: omo doesn't have explicit `lgtm`/`lgtmi` keyword like pi-mono v36; CLA discipline is different governance mechanism (legal vs operational). NOT a #69 strengthening.

## 3. CONTRIBUTING.md — Contributor guidance + English-language-policy

`CONTRIBUTING.md` (~270 lines). Key sections:

**Code of Conduct:** "Be respectful, inclusive, and constructive."

**Language Policy (corpus-first explicit at T1):**
> "**English is the primary language for all communications in this repository.**
>
> This includes:
> - Issues and bug reports
> - Pull requests and code reviews
> - Documentation and comments
> - Discussions and community interactions
>
> ### Why English?
> - **Global Accessibility**: English allows contributors from all regions to collaborate effectively
> - **Consistency**: A single language keeps discussions organized and searchable
> - **Open Source Best Practice**: Most successful open-source projects use English as the lingua franca"

→ **Korean author + 5-language README + EN-only contributor language policy** = corpus-first triple combination. README user-facing localization decoupled from contributor-facing English-monoglot governance.

→ Joins claude-code-best-practice v34 (Pakistani author + EN-only README + EN governance) and OMC v27 (Korean author + 7-language README + EN-leaning governance) as Korean/Asian-ecosystem-author convention: source localization, contribution centralization.

**Need help with English?** *"If English isn't your first language, don't worry! We value your contributions regardless of perfect grammar. You can: Use translation tools to help compose messages..."* — explicit non-native-friendly framing.

**Project structure section:** Documents `src/` organization; refers to AGENTS.md for architectural map.

**Adding-new-X workflow sections:** Agent / Hook / Tool / MCP server. Each documents factory pattern + registration location.

## 4. AGENTS.md — Auto-generated 173-line architecture overview

**Verbatim header:** *"# oh-my-opencode — OpenCode Plugin / **Generated:** 2026-04-18 | **Commit:** 2892ca4a | **Branch:** dev"*

→ **Auto-generated AGENTS.md** = corpus-first observation at T1. Generated via `/init-deep` slash command per README. Hierarchical generation: project root + per-subdirectory.

**Key architectural facts extracted (verbatim):**
- Plugin entry: `src/index.ts` → 5-step init (loadConfig → createManagers → createTools → createHooks → createPluginInterface)
- 1,766 TypeScript source files
- 377K LOC
- 104 barrel index.ts files
- 26 tools across 16 directories
- 11 named agents (Sisyphus / Hephaestus / Oracle / Librarian / Explore / Atlas / Prometheus / Metis / Momus / Multimodal-Looker / Sisyphus-Junior)
- 52 lifecycle hooks across 5 tiers (Session 24 + Tool-Guard 14 + Transform 5 + Continuation 7 + Skill 2)
- 19 feature modules
- 32 Zod v4 schema files
- 3-tier MCP system (built-in + Claude Code .mcp.json + skill-embedded)
- 10 OpenCode hook handlers
- 6-phase config loading pipeline
- 11 platform-specific compiled binaries

**Initialization flow (verbatim):**
```
pluginModule.server(input, options)
  ├─→ loadPluginConfig()         # JSONC parse → project/user merge → Zod validate → migrate
  ├─→ createManagers()           # TmuxSessionManager, BackgroundManager, SkillMcpManager, ConfigHandler
  ├─→ createTools()              # SkillContext + AvailableCategories + ToolRegistry (26 tools)
  ├─→ createHooks()              # 3-tier: Core(43) + Continuation(7) + Skill(2) = 52 hooks
  └─→ createPluginInterface()    # 10 OpenCode hook handlers → PluginInterface
```

**Multi-level config (verbatim):**
```
Project (.opencode/oh-my-opencode.jsonc)  →  User (~/.config/opencode/oh-my-opencode.jsonc)  →  Defaults
```

→ **3-level config + JSONC + Zod v4 + idempotent migrations + atomic writes** = corpus-first config-rigor at solo-T1. Heavier than aidevops v47 (3-layer governance file hierarchy) — different mechanism (config vs documentation).

**Conventions section (verbatim selections):**
- Runtime: Bun only (1.3.11 in CI) — never use npm/yarn
- TypeScript: strict mode, ESNext, `bun-types` (never `@types/node`)
- Test pattern: Bun test (`bun:test`), co-located `*.test.ts`, given/when/then style
- Factory pattern: `createXXX()` for all tools, hooks, agents
- Hook tiers: Session (24) → Tool-Guard (14) → Transform (5) → Continuation (7) → Skill (2)
- Agent modes: `primary` (respects UI model) vs `subagent` (own fallback chain) vs `all`
- Model resolution: 4-step: override → category-default → provider-fallback → system-default
- File naming: kebab-case for all files/directories
- No path aliases: no `@/` — relative imports only
- 200 LOC soft limit per file
- Catch-all files banned (`utils.ts`, `helpers.ts`, `service.ts`)

**Anti-patterns (verbatim):**
- Never use `as any`, `@ts-ignore`, `@ts-expect-error`
- Never suppress lint/type errors
- Never add emojis to code/comments unless user explicitly asks
- Never commit unless explicitly requested
- Never run `bun publish` directly — use GitHub Actions
- Test: given/when/then — never use Arrange-Act-Assert comments
- Never use em dashes, en dashes, or AI filler phrases in generated content (← enforced by comment-checker hook)

**Comparison to Pattern #22 AGENTS.md sub-variants:**
- 22a monolithic (gh-aw v48 / spec-kit v17 / claude-code-best-practice v34) — single comprehensive AGENTS.md
- 22b minimum-viable-shim (bizos v37 327B + 11B CLAUDE.md alias) — minimum-effort
- 22c authoritative-with-shim (aidevops v47 — 3-layer hierarchy)
- 22d identical-mirror (Vercel v51 — byte-identical AGENTS.md = CLAUDE.md)
- **omo v52 = NEW 22e? OR 22a-variant** — auto-generated hierarchical (per AGENTS.md text mentions per-subdirectory generation via /init-deep)

**Decision:** omo's AGENTS.md = **22a monolithic single-file 173-line auto-generated** at root level. Per-subdirectory AGENTS.md exists in src/agents/AGENTS.md / src/tools/AGENTS.md / src/features/AGENTS.md (verified via /bin/ls) but those are separate files, not 22c hierarchical-with-redirect-shim. Closer to 22a than other sub-variants. **Within Pattern #22 22a; NOT new sub-variant. Strengthening only.**

NOT registering 22e — consolidation-forward discipline. Pattern #22 already has 4 sub-variants formalized at v51.

## 5. Telemetry — PostHog with hashed installation ID

README + AGENTS.md notes:
- PostHog backend
- Hashed installation identifier (never raw hostname)
- Opt-out: `OMO_SEND_ANONYMOUS_TELEMETRY=0` OR `OMO_DISABLE_POSTHOG=1`
- Privacy Policy at `docs/legal/privacy-policy.md`
- ToS at `docs/legal/terms-of-service.md`
- Default: ON (opt-out, not opt-in)

**Pattern #12 strengthening:** Telemetry-on-by-default with explicit opt-out + Privacy Policy + ToS + dependency `posthog-node ^5.29.2` in package.json = corpus-first explicit telemetry transparency at solo-T1. Joins:
- aidevops v47: explicit telemetry policy
- bizos v37: in-app /guide tutorial
- spec-kit v17: AI-disclosure policy

→ **omo v52 = 7th counter-evidence wiki for Pattern #12 v42 refined formulation**. Solo-Korean-T1 + maintainer-philosophy (operational thoroughness from manifesto + Sionic AI / Sisyphus Labs commercial-incubation ambition) drives heavy governance. Refined formulation HOLDS strongly.

## 6. CI/CD workflow inventory (7 workflows)

Per AGENTS.md + verified via /bin/ls .github/workflows/ (probed):
- `ci.yml` — push/PR to master/dev. Tests (split: mock-heavy isolated + batch), typecheck, build, schema auto-commit
- `publish.yml` — manual dispatch. Version bump, **dual npm publish (oh-my-opencode + oh-my-openagent)**, platform binaries, GitHub release
- `publish-platform.yml` — called by publish. **11 platform binaries via bun compile** (darwin/linux/windows)
- `sisyphus-agent.yml` — @mention / dispatch. **AI agent handles issues/PRs** (Jobdori-built per README building-in-public)
- `refresh-model-capabilities.yml` — weekly schedule / dispatch. Auto-refresh model capabilities from models.dev API
- `cla.yml` — issue_comment/PR. CLA Assistant for contributors
- `lint-workflows.yml` — push to .github/. actionlint + shellcheck on workflow files

**Sisyphus-agent.yml = corpus-first AI-agent-handles-issues-PRs at T1**. Jobdori (YeonGyu's customized OpenClaw fork — Korean: 잡도리 / "doing thoroughly") triages issues + handles PRs autonomously. Ties Pattern #69 Agent-PR Fast-Track Governance Protocol — but mechanism is different (Jobdori = AI executes; #69 protocols are human-mediated approval keywords).

**dual npm publish** in publish.yml = Pattern #58 58c sub-variant validated at workflow level: `oh-my-opencode` + `oh-my-openagent` both published from same build artifacts.

## 7. Privacy Policy + Terms of Service (corpus-first explicit at solo-T1)

`docs/legal/privacy-policy.md` + `docs/legal/terms-of-service.md` (verified via /bin/ls; not deeply read in this cluster summary — flagged for follow-up).

→ **Legal documents at solo-T1** = exceptional. Joins:
- ollama v46 (commercial-runtime corpus-position)
- bizos v37 (cold-start commercial intent)
- DeepTutor v38 (academic-lab medium-governance)
- aidevops v47 (commercial-positioning aidevops.sh)

omo v52's privacy/ToS = consistent with Sionic AI / Sisyphus Labs commercial-incubation ambition. Not solo-hobbyist defaults.

## 8. AGENTS.md WHERE TO LOOK table — 14-row maintainer guide

| Task | Location | Notes |
|---|---|---|
| Add new agent | `src/agents/` + `src/agents/builtin-agents/` | Follow createXXXAgent factory pattern |
| Add new hook | `src/hooks/{name}/` + register in `src/plugin/hooks/create-*-hooks.ts` | Match event type to tier |
| Add new tool | `src/tools/{name}/` + register in `src/plugin/tool-registry.ts` | Follow createXXXTool factory |
| Add new feature module | `src/features/{name}/` | Standalone module, wire in plugin/ |
| Add new MCP | `src/mcp/` + register in `createBuiltinMcps()` | Remote HTTP only (tier 1 of 3) |
| Add new skill | `src/features/builtin-skills/skills/` | Implement BuiltinSkill interface |
| Add new command | `src/features/builtin-commands/` | Template in templates/ |
| Add new CLI command | `src/cli/cli-program.ts` | Commander.js subcommand |
| Add new doctor check | `src/cli/doctor/checks/` | Register in checks/index.ts |
| Modify config schema | `src/config/schema/` + update root schema | Zod v4, add to OhMyOpenCodeConfigSchema |
| Add new category | `src/tools/delegate-task/constants.ts` | DEFAULT_CATEGORIES + CATEGORY_MODEL_REQUIREMENTS |
| Debug provider errors | `src/hooks/runtime-fallback/` | Reactive error recovery (distinct from model-fallback) |
| External notifications | `src/openclaw/` | Bidirectional Discord/Telegram/webhook integration |
| Skill-embedded MCP | `src/features/skill-mcp-manager/` | Tier 3 MCPs (stdio + HTTP, per-session) |

→ **WHERE TO LOOK table at solo-T1** = corpus-first explicit maintainer-onboarding guide with task→location mapping. Reduces contributor friction.

## 9. Notes section (operational details)

Verbatim selections from AGENTS.md:
- Logger writes to `/tmp/oh-my-opencode.log`
- Background tasks: 5 concurrent per model/provider (configurable, circuit breaker support)
- Plugin load timeout: 10s for Claude Code plugins
- Model fallback: per-agent chains in `shared/model-requirements.ts`, not a single global priority
- Two fallback systems: `model-fallback` (proactive, chat.params) vs `runtime-fallback` (reactive, session.error)
- Config migration: idempotent via `_migrations` tracking, creates timestamped backups before atomic writes
- Build: bun build (ESM) + tsc --emitDeclarationOnly, externals: @ast-grep/napi
- Test setup: `test-setup.ts` preloaded via bunfig.toml, resets session/cache state between tests
- Test split: `script/run-ci-tests.ts` auto-isolates files using `mock.module()`
- 104 barrel export files (index.ts) establish module boundaries
- Architecture rules enforced via `.sisyphus/rules/modular-code-enforcement.md`
- Windows builds run on `windows-latest` runner (not cross-compiled) to avoid Bun segfaults
- Platform binaries detect AVX2 + libc family at runtime, fallback to baseline if needed
- Hashline edit: every Read output tagged with `LINE#ID` content hashes; edits reject on hash mismatch
- IntentGate: classifies user intent (research/implementation/investigation/evaluation/fix) before routing

→ **Operational rigor at solo-T1**: 14+ explicit operational notes. Counter-evidence reinforcement to Pattern #12 v42 refined formulation.

## 10. Cluster takeaways

- **SUL-1.0 license** = corpus-first SUL family at T1. Pattern #29 NEW sub-context "29-custom-non-OSI-non-commercial-restriction" at N=2 with PolyForm Noncommercial (GitNexus v33). **Storm Bear commercial-blocker** for Scrum coaching deployment.
- **CLA.md with relicensing rights + future-license-changes clause** = corpus-first formal CLA at solo-Korean-T1 with explicit open-core-prep legal infrastructure. Owner = YeonGyu individual (clean IP-rights consolidation for future Sisyphus Labs commercial transfer).
- **CONTRIBUTING.md English-language-policy + 5-language user-facing README** = corpus-first decoupled localization-vs-governance language strategy.
- **AGENTS.md auto-generated** via `/init-deep` slash command + per-subdirectory hierarchical generation = corpus-first auto-generated AGENTS.md at T1. Within Pattern #22 22a monolithic (NOT new sub-variant; consolidation-forward). 173-line single root + per-subdir separate files.
- **Telemetry-on-by-default + PostHog hashed-ID + opt-out via 2 env vars + Privacy Policy + ToS** = corpus-first telemetry transparency surface at solo-T1.
- **7 GitHub Actions workflows** including `sisyphus-agent.yml` (Jobdori AI agent handles issues/PRs) + `cla.yml` (CLA Assistant) + `publish.yml` (dual-npm-publish + 11 platform binaries) + `lint-workflows.yml` (actionlint + shellcheck on workflows themselves).
- **Pattern #18 OpenCode-primary observation N=2** strengthens at v52 (omo IS OpenCode plugin extending runtime; aidevops v47 was N=1 stale-risk-flagged with v52 stale-check; omo un-stales + reaches structural N=2 = promotion-candidate).
- **Pattern #58 58c sub-variant** validated at workflow level (publish.yml dual-npm-publish + dual-bin alias in package.json + compatibility layer in opencode.json + dual-basename config recognition).
- **Pattern #50 50d sub-variant NEW** (Sisyphus Labs incubation-waitlist commercial-funnel-terminus distinct from 50a/b/c).
- **Pattern #12 v42 refined 7th counter-evidence wiki** — solo-Korean-T1 with heavy governance (5 governance files + telemetry + Privacy/ToS + 7 workflows + auto-generated AGENTS.md + WHERE TO LOOK table + factory patterns + 200 LOC soft limit + catch-all banned + AI filler enforcement). HOLDS strongly.

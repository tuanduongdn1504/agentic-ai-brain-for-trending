# (C) C3 — src architecture + 26 tools + OpenClaw fork + 11-platform binaries + Sionic AI + Sisyphus Labs

> **Cluster scope:** Technical architecture + distribution surface + commercial ecosystem.
> **Source files:** `src/` (1,766 TS files / 17 tool subdirs / 11 named agents / 19 features / 32 Zod schemas) + `packages/` (11 platform binaries) + `package.json` (dual-bin + 11 optionalDeps + dependencies) + `bunfig.toml` + `bun.lock` + `docs/guide/` + `docs/reference/` + `docs/superpowers/` + Sionic AI org metadata + Sisyphus Labs landing
> **Wiki phase:** Phase 2 cluster summary
> **Cross-wiki siblings cited:** OMC v27 / aidevops v47 / pi-mono v36 / multica v15 / paperclip v14 / GitNexus v33

---

## 1. Repository structure (top-level)

Verified via /bin/ls:
```
/
├── README.md (24.5 KB) + 4 translations (ko/ja/zh-cn/ru)
├── AGENTS.md (173-line auto-generated, root)
├── CLA.md (59 lines)
├── CONTRIBUTING.md (~270 lines)
├── LICENSE.md (SUL-1.0 83 lines)
├── package.json (104 lines; dual-bin + 11-platform optionalDeps)
├── bun.lock (Bun lockfile)
├── bunfig.toml (Bun config)
├── tsconfig.json
├── postinstall.mjs
├── test-setup.ts + bun-test.d.ts
├── assets/ (images/banners)
├── bin/ (entry points; oh-my-opencode.js + alias)
├── docs/ (5 subdirs: guide / reference / examples / legal / troubleshooting + manifesto.md + model-capabilities-maintenance.md + superpowers/)
├── drafts/
├── packages/ (11 platform-specific compiled binary subdirs)
├── script/ (build/publish automation)
├── signatures/ (cryptographic verification?)
├── src/ (1,766 TS files; 22 subdirs)
└── tests/
```

→ **EXTREME repository scale at solo-T1**: 1,766 TS files / 377K LOC / 104 barrel index.ts files / 32 Zod schemas / 11 platform-binary packages / 5-language docs.

## 2. src/ subdirectory architecture (22 subdirs verified)

```
src/
├── index.ts (plugin entry; default export pluginModule shape {id, server})
├── plugin-config.ts (JSONC multi-level config; Zod v4)
├── plugin-interface.ts
├── plugin-state.ts
├── create-managers.ts / create-tools.ts / create-hooks.ts / create-runtime-tmux-config.ts
├── AGENTS.md (per-src-subdir AGENTS.md)
├── __tests__/
├── agents/ (11 named agents + factory + builders)
├── cli/ (Commander.js subcommands: install / run / doctor / mcp-oauth)
├── config/ (32 Zod v4 schema files)
├── features/ (19 feature modules)
├── generated/ (auto-generated code)
├── hooks/ (52 hooks across 5 tiers)
├── mcp/ (3 built-in remote MCPs: websearch + context7 + grep_app)
├── openclaw/ (bidirectional Discord/Telegram/webhook/command integration)
├── plugin/ (10 OpenCode hook handlers + 52 hook composition)
├── plugin-handlers/ (6-phase config loading pipeline)
├── shared/ (170+ utility files; barrel-exported)
├── testing/ (test infrastructure)
└── tools/ (26 tools across 17 subdirs)
```

→ **104 barrel index.ts files** establish module boundaries. **No path aliases (`@/`)** — relative imports only. **200 LOC soft limit per file**. Catch-all files banned.

## 3. 26 tools across 17 subdirs (verified via /bin/ls src/tools/)

```
src/tools/
├── ast-grep         # AST-aware code search and rewrites (25 languages)
├── background-task  # Parallel background agent execution
├── call-omo-agent   # Call other agents
├── delegate-task    # Category-based delegation (visual-eng / deep / quick / ultrabrain)
├── glob             # File glob matching
├── grep             # Text search
├── hashline-edit    # LINE#ID content-hash-validated edits (corpus-first)
├── interactive-bash # Tmux-backed interactive bash sessions
├── look-at          # Multimodal look at file/screenshot
├── lsp              # LSP integration (rename / goto_definition / find_references / diagnostics)
├── session-manager  # Tmux session lifecycle
├── shared/          # Common tool utilities
├── skill            # Skill invocation
├── skill-mcp        # Skill-embedded MCP management
├── slashcommand     # Slash command dispatch
├── task             # Task tracking
└── AGENTS.md        # Per-tools-subdir AGENTS.md
```

**Key tool spotlight:**
- **hashline-edit** — corpus-first **LINE#ID content-hash-validated edit tool** at T1. Inspired by oh-my-pi (Can Bölük). Every Read output tagged with `LINE#ID` content hashes; edits reject on hash mismatch. README claims: "Grok Code Fast 1: 6.7% → 68.3% success rate. Just from changing the edit tool."
- **lsp** — `lsp_rename`, `lsp_goto_definition`, `lsp_find_references`, `lsp_diagnostics`. Workspace-aware refactoring at agent-tool level (corpus-first explicit LSP-tool-suite at T1; precedent in graphify v16 / GitNexus v33 had similar but bridge-tier).
- **ast-grep** — Pattern-aware code search and rewriting across 25 languages. Wrapper around `@ast-grep/cli` + `@ast-grep/napi`.
- **interactive-bash + session-manager + tmux features** — Tmux-backed interactive terminal sessions; agent stays in REPL/debugger/TUI throughout work.
- **delegate-task** — Category-based routing (visual-engineering / deep / quick / ultrabrain). Sisyphus delegates to subagent by category, not model. Category maps to model via `src/tools/delegate-task/constants.ts` `CATEGORY_MODEL_REQUIREMENTS`.
- **skill-mcp** — Manages 3rd-tier MCP (skill-embedded; loaded per-session stdio + HTTP).

## 4. 11 named agents (verified via /bin/ls src/agents/)

| Agent | Mythology source | Role (per README + AGENTS.md) | Default model chain |
|---|---|---|---|
| **Sisyphus** | Greek (endless toil) | Main orchestrator; "Does not stop halfway" | claude-opus-4-7 / kimi-k2.5 / glm-5 |
| **Sisyphus-Junior** | Greek | Variant for smaller scope | (probable lighter model chain) |
| **Hephaestus** | Greek (forge god) | Autonomous deep worker; "Legitimate Craftsman" | gpt-5.4 |
| **Prometheus** | Greek (foresight) | Strategic planner; interview mode | claude-opus-4-7 / kimi-k2.5 / glm-5 |
| **Oracle** | Greek (divination) | Architecture/debugging | (configurable) |
| **Librarian** | Functional | Docs/code search | (configurable) |
| **Explore** | Functional | Fast codebase grep | (configurable) |
| **Atlas** | Greek (titan / heavenly burden) | (per AGENTS.md inventory; docs unclear) | (configurable) |
| **Metis** | Greek (wisdom/cunning) | (per AGENTS.md inventory) | (configurable) |
| **Momus** | Greek (mockery/criticism) | Critic/reviewer (probable; Momus = Greek god of satire) | (configurable) |
| **Multimodal-Looker** | Functional | Vision-augmented inspection | (vision-capable model) |

→ **Greek-mythology cluster** = corpus-first heavy mythology theme at T1. Pattern #25 Personality-Driven Agent Design retired v27 — do NOT re-register. Aesthetic/cultural choice, not architectural.

→ **Per-agent factory pattern** (`createXXXAgent`) + agent-builder + dynamic-agent-prompt-builder + 14 overridable agent fields × 21 fields each.

→ Agent modes: `primary` (respects UI model) vs `subagent` (own fallback chain) vs `all`.

→ Model resolution: 4-step (override → category-default → provider-fallback → system-default).

## 5. 19 feature modules (verified via /bin/ls src/features/)

```
src/features/
├── background-agent
├── boulder-state                # Sisyphus reference (boulder = the rock he pushes)
├── builtin-commands             # ultrawork / ulw / start-work / init-deep / etc.
├── builtin-skills               # playwright / git-master / frontend-ui-ux / + custom
├── claude-code-agent-loader     # Claude Code agent compat
├── claude-code-command-loader   # Claude Code command compat
├── claude-code-mcp-loader       # Claude Code MCP compat (.mcp.json)
├── claude-code-plugin-loader    # Claude Code plugin compat
├── claude-code-session-state    # Claude Code session continuity
├── claude-tasks                 # Task tracking
├── context-injector             # Auto-inject AGENTS.md / README.md / conditional rules
├── hook-message-injector
├── mcp-oauth                    # MCP OAuth flow
├── opencode-skill-loader        # OpenCode skill compat
├── run-continuation-state
├── skill-mcp-manager            # Tier 3 MCPs (stdio + HTTP, per-session)
├── task-toast-manager
├── team-mode
├── tmux-subagent
└── tool-metadata-store
```

**Key features:**
- **Claude-code-* loaders (5 separate modules)** — full Claude Code compatibility: agents / commands / MCPs / plugins / session-state. Validates README claim: *"Your hooks, commands, skills, MCPs, and plugins? All work here. Full compatibility, including plugins."*
- **opencode-skill-loader** — primary OpenCode skill mechanism
- **context-injector** — auto-inject AGENTS.md / README.md / conditional rules into agent context
- **skill-mcp-manager** — 3rd-tier MCP (skill-embedded), stdio + HTTP, per-session lifecycle
- **mcp-oauth** — OAuth flow for remote MCPs (corpus-first explicit MCP-OAuth feature at T1)
- **boulder-state + builtin-skills + builtin-commands** — Sisyphus mythology + executable surface
- **team-mode + tmux-subagent + background-agent** — parallel execution architecture

## 6. 52 hooks across 5 tiers

Per AGENTS.md HOOK TIERS (verbatim):
- **Session (24)** — created / deleted / idle / error / + 20 more session lifecycle
- **Tool-Guard (14)** — file guard / label truncator / rules injector / prometheus md-only / + 10 more
- **Transform (5)** — context injection / thinking block validation / tool pair validation / + 2 more
- **Continuation (7)** — context + todo preservation during compaction / + 6 more
- **Skill (2)** — skill-specific hooks

**3-tier registration breakdown (per AGENTS.md initialization flow):**
- Core (43) + Continuation (7) + Skill (2) = 52 total

**10 OpenCode hook handlers** wrap the 52 hooks (per AGENTS.md table):
| Handler | Purpose |
|---|---|
| config | 6-phase: provider → plugin-components → agents → tools → MCPs → commands |
| tool | 26 registered tools |
| chat.message | First-message variant, session setup, keyword detection (ultrawork/search/analyze) |
| chat.params | Anthropic effort level, think mode, runtime fallback override |
| chat.headers | Copilot x-initiator header injection |
| event | Session lifecycle, openclaw dispatch, runtime fallback |
| tool.execute.before | Pre-tool hooks (file guard, label truncator, rules injector, prometheus md-only) |
| tool.execute.after | Post-tool hooks (output truncation, comment checker, hashline read enhancer) |
| experimental.chat.messages.transform | Context injection, thinking block validation, tool pair validation |
| experimental.session.compacting | Context + todo preservation during compaction |

**comment-checker hook** = corpus-first explicit AI-slop-prevention hook at T1. Enforces "no em dashes / en dashes / AI filler phrases" anti-pattern.

**hashline read enhancer** = post-tool hook tagging Read output with LINE#ID content hashes. Architectural foundation for hashline-edit tool.

## 7. 3-tier MCP system (corpus-first explicit 3-tier MCP at T1)

| Tier | Source | Mechanism | Examples |
|---|---|---|---|
| **Built-in** | `src/mcp/` | 3 remote HTTP MCPs | websearch (Exa/Tavily) + context7 (official docs) + grep_app (GitHub code search) |
| **Claude Code** | `.mcp.json` | `${VAR}` env expansion via `claude-code-mcp-loader` | User-configured per Claude Code convention |
| **Skill-embedded** | SKILL.md YAML | Per-session stdio + HTTP via `skill-mcp-manager` | Skills bring own MCP servers |

→ **Skill-embedded MCP tier (Tier 3) = corpus-first explicit at T1**. Mechanism: skills load + unload MCP servers per-session, scoped to task, gone when done. Avoids context-budget pollution from always-on MCPs. README verbatim: *"MCP servers eat your context budget. We fixed that. Skills bring their own MCP servers. Spin up on-demand, scoped to task, gone when done. Context window stays clean."*

→ Pattern #18 strengthening: omo treats MCP as 3-tier scoping mechanism (architectural) rather than flat-protocol. Layer-2 strengthening within Pattern #18 (recall #18 v36 added Layer 0 OpenClaw+Hermes community-platform-scoped + Layer 1 per-runtime). omo v52 introduces explicit 3-tier within Layer 1 (built-in + .mcp.json + skill-embedded).

## 8. Pattern #18 OpenCode-primary observation N=2 (UN-STALE)

omo IS OpenCode plugin extending OpenCode runtime (verified via package.json dependency `@opencode-ai/plugin ^1.4.0` + `@opencode-ai/sdk ^1.4.0` + repo description "OpenCode Plugin" + index.ts plugin entry pattern).

**Pattern #18 OpenCode-primary observation history:**
- v47 aidevops: registered N=1 stale-risk-flagged at registration (v47 → v52 stale-check / v57 retire-check)
- **v52 omo: 2nd OpenCode-primary T1 framework — UN-STALES + reaches structural N=2**
- Promotion-candidate at next mini-audit under structural-N=2 criterion (criterion #2)

This validates v47 v2.1 mechanism — pre-registered stale-check thresholds correctly identify un-stale opportunities.

→ Pattern #18 sub-axis observation strengthening: 3-runtime-primacy diversity now formally validated at N=2 (Claude-Code-primary majority + OpenCode-primary aidevops v47 + omo v52 + Codex-primary observed via oh-my-codex sibling). 4-layer formal-statement-update for Pattern #18 (already promotion-candidate from v47 mini-audit) reinforced.

## 9. OpenClaw fork — Jobdori (Korean: 잡도리)

`src/openclaw/` subdir handles bidirectional integration: Discord / Telegram / webhook / command. Per AGENTS.md WHERE TO LOOK table.

README verbatim mention: *"The maintainer builds and maintains oh-my-opencode in real-time with **Jobdori**, an AI assistant built on a heavily customized fork of OpenClaw."*

→ Jobdori = corpus-first explicit named OpenClaw-fork at T1 (Korean "잡도리" / "doing thoroughly" / "discipline"). Aligns with Sisyphus mythology (endless toil, never giving up) + manifesto (Human In The Loop = Bottleneck).

**Pattern #18 OpenClaw observation strengthening (Layer 0):** omo extends prior corpus presences:
- v14 paperclip — OpenClaw integration
- v15 multica — OpenClaw integration
- v16 graphify — OpenClaw integration (execution-level install paths)
- v18 agency-agents — OpenClaw integration
- v27 OMC — OpenClaw fork-extension (Korean Seoul author)
- **v52 omo — Jobdori = customized OpenClaw fork (Korean Seoul author, 2nd Korean OpenClaw-fork)**

→ Pattern #73 73a Korean-Regional-Archetype T1 sub-observation: Korean-OpenClaw-fork-extension (OMC + omo = N=2 Korean Seoul authors building customized OpenClaw forks). Within Pattern #73 strengthening, NOT new candidate.

## 10. 11 platform-specific compiled binaries

`packages/` subdir verified via package.json `optionalDependencies`:

| Platform | Variant | Optional dep |
|---|---|---|
| **darwin-arm64** | (default) | oh-my-opencode-darwin-arm64 |
| **darwin-x64** | (default) | oh-my-opencode-darwin-x64 |
| **darwin-x64-baseline** | (no AVX2) | oh-my-opencode-darwin-x64-baseline |
| **linux-arm64** | (glibc) | oh-my-opencode-linux-arm64 |
| **linux-arm64-musl** | (Alpine) | oh-my-opencode-linux-arm64-musl |
| **linux-x64** | (glibc + AVX2) | oh-my-opencode-linux-x64 |
| **linux-x64-baseline** | (glibc, no AVX2) | oh-my-opencode-linux-x64-baseline |
| **linux-x64-musl** | (Alpine + AVX2) | oh-my-opencode-linux-x64-musl |
| **linux-x64-musl-baseline** | (Alpine, no AVX2) | oh-my-opencode-linux-x64-musl-baseline |
| **windows-x64** | (default) | oh-my-opencode-windows-x64 |
| **windows-x64-baseline** | (no AVX2) | oh-my-opencode-windows-x64-baseline |

→ **11 platform-specific compiled binaries** = corpus-most-platform-binary-distribution-at-T1. Built via Bun compile (`build:binaries` script). Runtime detects AVX2 + libc family + falls back to baseline if needed (per AGENTS.md NOTES).

→ Pattern #2 Distribution Evolution strengthening: 11-platform-binary at T1 + npm dual-bin + bunx + curl install = 4+ distribution surfaces at T1. Strengthening only (no new pattern).

→ Windows builds run on `windows-latest` runner (not cross-compiled) to avoid Bun segfaults — operational rigor observation.

## 11. 32 Zod v4 schema files (config validation)

`src/config/` contains 32 schema files (per AGENTS.md). JSONC config validated by Zod v4 with:
- `safeParse()` fills defaults for omitted fields
- Partial parsing as fallback
- `migrateConfigFile()` transforms legacy keys automatically (idempotent via `_migrations` tracking)
- Atomic writes with timestamped backups

→ **Config-rigor at solo-T1**: most-elaborate config validation observed in corpus. Schema-driven defaults + migrations + atomic writes + backups = production-grade config infrastructure.

## 12. Multi-runtime category-based model routing (Pattern #28 strengthening)

**4 default categories** (per README):
- `visual-engineering` — Frontend, UI/UX, design
- `deep` — Autonomous research + execution
- `quick` — Single-file changes, typos
- `ultrabrain` — Hard logic, architecture decisions (routes to GPT-5.4 xhigh by default)

→ Plus 4 more categories likely defined in `src/tools/delegate-task/constants.ts` (per AGENTS.md WHERE TO LOOK table — 8 built-in categories).

**Mechanism:** Sisyphus delegates to subagent by **category**, not model. Category maps to model via `CATEGORY_MODEL_REQUIREMENTS`. Agent says what kind of work; harness picks the right model.

**Multi-provider stack (per README + AGENTS.md):**
- Claude Opus 4.7 (orchestration; Sisyphus / Prometheus default)
- Kimi K2.5 (orchestration alternative)
- GLM 5 (orchestration alternative)
- GPT-5.4 (deep work; Hephaestus default; ultrabrain xhigh routing)
- Minimax (speed)
- Gemini (creativity)

→ **Pattern #28 strengthening: 14th+ data point + category-based routing as 4th sub-axis** (joins routing-abstraction + native-multi-provider + verification-not-routing 3-axis taxonomy from v47 aidevops). Within Pattern #28 strengthening; NOT new candidate (consolidation-forward).

→ **Pattern #28 sub-observation: subscription-rotation strategy** (ChatGPT $20 + Kimi $0.99 + GLM $10 stack per README) = parallel to aidevops v47's 4-provider OAuth pool. Strengthening via subscription-pool-multi-provider sub-axis.

## 13. Built-in slash commands (per AGENTS.md + README)

Identified commands (subset; full inventory requires probing `src/features/builtin-commands/`):
- **`ultrawork`** / **`ulw`** — primary entrypoint; "every agent activates, doesn't stop until done"
- **`/ulw-loop`** / **Ralph Loop** — self-referential loop; "doesn't stop until 100% done"
- **`/start-work`** — calls Prometheus interview-mode planner
- **`/init-deep`** — auto-generates hierarchical AGENTS.md files

→ **`ultrawork` + ralph loop** = corpus-first explicit "doesn't stop until done" command primitives at T1. Operationalizes manifesto autonomy-max framing.

→ **`/init-deep`** = corpus-first auto-generation of hierarchical AGENTS.md at T1. Justifies Pattern #22 22a auto-generated sub-observation.

## 14. Sionic AI org affiliation (Korean AI startup)

**Sionic AI (`@sionic-ai`)** — verified via probe metadata:
- Tagline: *"Make your AI Agent Great Again"*
- Homepage: sionic.ai
- Created: 2023-05-22
- 57 public repos
- 141 followers
- Korean AI startup (probable Seoul HQ given YeonGyu Seoul + Korean naming convention 잡도리/Jobdori)

YeonGyu-Kim listed in Sionic AI org member list per probe (confirms employment). Per Sionic AI bio: focus on AI agents.

**Relationship to omo:** YeonGyu's day-job employer; Sionic AI's tagline parallels omo's autonomy-max manifesto framing. omo OSS may serve as Sionic AI's open-source publishing channel + recruiting funnel + technology validation surface.

## 15. Sisyphus Labs commercial incubation (sisyphuslabs.ai)

**sisyphuslabs.ai** landing page (per probe):
- Tagline: *"Sisyphus is the agent that codes like your team"*
- Pitch: *"We're building a fully productized version of Sisyphus to define the future of frontier agents. Join the waitlist"*
- CTA: Waitlist signup

**Relationship to omo + Sionic AI:** Sisyphus Labs = separate venture (per separate domain + separate brand + separate landing page). Likely structured as YeonGyu's own commercial spin-off from omo OSS, distinct from Sionic AI day-job. Parallel to:
- Composio Inc. (awesome-claude-skills v50) — commercial parent of OSS aggregator
- Keygraph (shannon v45) — commercial parent of OSS Lite + Pro
- All Hands AI (OpenHands v30) — commercial parent of OSS

**Pattern #50 50d sub-variant NEW:** **incubation-waitlist-as-funnel-terminus** — separate commercial entity (Sisyphus Labs) with waitlist landing page entrypoint embedded in OSS README banner. Mechanism distinct from:
- 50a standard commercial-tier funnel (most prior #50 data points; commercial tier exists alongside OSS)
- 50b recruiting-as-funnel-terminus (MiroFish v49 + omo v52 testimonials echo)
- 50c aggregator-with-bundled-commercial-product (awesome-claude-skills v50)

→ N=1 stale-flagged at registration v52 → v57 stale-check / v62 retire-check.

→ Pattern #31 Open-Core Commercial Entity strengthening reinforced (omo SUL-1.0 OSS + sisyphuslabs.ai future commercial product). 11+ data point at #31 (post-v51 was 10+).

## 16. Documentation surface

`docs/` subdirs (verified via /bin/ls):
- **`guide/`** (4 files) — installation / overview / orchestration / + 1
- **`reference/`** — cli / configuration / features
- **`examples/`** (3 jsonc configs) — coding-focused / planning-focused / default
- **`legal/`** — privacy-policy + terms-of-service
- **`troubleshooting/`** — ollama.md + others
- **`superpowers/`** — plans/ + specs/ subdirs (corpus-first integration of obra/superpowers v2)
- **`manifesto.md`** — corpus-first explicit manifesto at solo-T1
- **`model-capabilities-maintenance.md`** — refresh-model-capabilities workflow doc

→ **3 example .jsonc configs** = corpus-first plug-and-play config templates at T1.

→ **`docs/superpowers/`** = direct integration of obra/superpowers (Storm Bear v2 wiki subject) as skill-system component within omo. Pattern #57 57a 5th data point.

→ **`docs/legal/`** = corpus-first dedicated legal subdirectory at solo-T1. Privacy policy + terms of service.

## 17. Pattern #57 corpus-internal recursion (5th data point + 57c structural N=2)

**Pattern #57 57a Direct citation 5th data point:**
- omo's `docs/superpowers/` integrates obra/superpowers v2 wiki subject directly
- 57a was N=4 pre-v52 (CONFIRMED v50 mini-audit; default-criterion ≥3-cross-tier)
- v52: 5th data point strengthening

**Pattern #57 57c Forward-citation-then-wiki sub-variant N=2 STRUCTURAL:**
- 57c registered v51 N=1 (multica v15 cited "Vercel agent-skills import (first)" 36 wikis BEFORE v51 wiki built; first 57c data point)
- **v52 omo: OMC v27 wiki entry cited "oh-my-opencode" as 1 of 5 inspirational sources** (per CLAUDE.md state block: "5 explicit intellectual sources cited: oh-my-opencode / claude-hud / Superpowers v2 / everything-claude-code v1 / Ouroboros") — 25 wikis BEFORE v52 wiki built
- **57c reaches N=2 structural at v52** — promotion-candidate at next mini-audit under structural-N=2 criterion
- 57c sub-variant promotion would parallel:
  - Pattern #58 promotion at v42 mini-audit
  - Pattern #69 promotion at v36 mini-audit
  - Pattern #59 promotion at v36 mini-audit

→ **Significant validation of forward-citation-then-wiki mechanism** as corpus-selection-discipline external validity signal across multiple wiki gaps (36-wiki gap v15→v51; 25-wiki gap v27→v52).

## 18. Cluster takeaways

- **EXTREME primitive surface at solo-T1**: 1,766 TS files / 26 tools / 11 named agents / 52 hooks / 19 features / 3-tier MCP / 11 platform binaries / 32 Zod schemas / 8 categories / 14 overridable agent fields × 21 fields each. **EXTREME primitive-count tier** — comparable to ruflo v42 / aidevops v47 / awesome-claude-skills v50.
- **Hashline LINE#ID edit tool** = corpus-first hash-anchored edit at T1 (inspired by oh-my-pi / Can Bölük; Pattern #19 archetype 2 NEW influence node observation).
- **3-tier MCP system** (built-in + .mcp.json + skill-embedded) = corpus-first explicit 3-tier MCP scoping at T1. Skill-embedded MCP per-session loading prevents context-budget pollution.
- **Multi-runtime category-based routing** (visual-engineering / deep / quick / ultrabrain) = Pattern #28 4th sub-axis observation; subscription-rotation strategy as parallel sub-axis.
- **Pattern #18 OpenCode-primary observation N=2 UN-STALE** at v52 (joins aidevops v47 N=1; promotion-candidate at next mini-audit under structural-N=2).
- **Jobdori (Korean: 잡도리) = customized OpenClaw fork by YeonGyu** — explicit named fork at T1; 2nd Korean Seoul OpenClaw-fork (joins OMC v27); within Pattern #73 73a Korean ecosystem strengthening.
- **11 platform-specific compiled binaries** via Bun compile = corpus-most-platform-binary distribution at T1.
- **5 Claude-code-* loaders** + opencode-skill-loader = full Claude Code compatibility validated at architecture level (matches README claim).
- **Greek-mythology persona cluster** (Sisyphus / Hephaestus / Prometheus / Oracle / Atlas / Metis / Momus + 4 functional) = aesthetic/cultural choice (Pattern #25 retired; documentation only).
- **Sionic AI org + Sisyphus Labs commercial incubation** = parallel commercial structures; Pattern #50 50d sub-variant NEW (incubation-waitlist-as-funnel-terminus N=1 stale-flagged).
- **Pattern #57 57a 5th data point** (`docs/superpowers/` cites Storm Bear v2 wiki subject obra/superpowers).
- **Pattern #57 57c structural N=2** at v52 (OMC v27 cited oh-my-opencode 25 wikis pre-v52; joins v51 vercel-labs 36-wiki gap); promotion-candidate at next mini-audit.
- **comment-checker hook** + **anti-AI-slop conventions** (no em dashes / en dashes / AI filler phrases enforced via post-tool hook) = corpus-first explicit AI-slop-prevention infrastructure at T1.
- **`/init-deep` auto-generated AGENTS.md hierarchical** = within Pattern #22 22a (consolidation-forward; NOT new sub-variant).

# (C) E1 — Core product — omo coding harness + ultrawork + multi-runtime orchestration

> **Entity:** oh-my-openagent (omo) — the OpenCode plugin extending Claude Code with 11 Greek-mythology specialist agents + 26 tools + 52 hooks + 3-tier MCP + Hashline LINE#ID edit tool + IntentGate classifier + multi-runtime category-based model routing.
> **Wiki version:** v52 — 13-section canonical entity format
> **Cross-wiki siblings cited:** OMC v27 (Korean Seoul T1 ecosystem peer) / obra/superpowers v2 (cited in docs/superpowers/) / aidevops v47 (OpenCode-primary N=1 → omo N=2) / paperclip v14 (autonomy-max framing comparison) / pi-mono v36 (multi-package monorepo solo-Korean parallel)

---

## 1. What is it?

omo (oh-my-openagent; previously oh-my-opencode) is an OpenCode plugin that converts the OpenCode CLI runtime into a "batteries-included" multi-agent coding harness. User installs the plugin against existing OpenCode runtime and gains: 11 named Greek-mythology specialist agents (Sisyphus orchestrator + Hephaestus deep worker + Prometheus planner + 8 others), 26 specialized tools (LSP-suite + ast-grep + Hashline LINE#ID-validated edit + tmux-backed interactive bash + multimodal vision), 52 lifecycle hooks across 5 tiers (session / tool-guard / transform / continuation / skill), 3-tier MCP system (3 built-in remote HTTP + Claude Code .mcp.json compat + skill-embedded per-session), 8 model-category routing (visual-engineering / deep / quick / ultrabrain / + 4 more), 11 platform-compiled Bun binaries (darwin/linux/windows × x64/arm64 × baseline/musl), Claude Code full compatibility (hooks/commands/skills/MCPs/plugins reused unchanged), and one-word entrypoint `ultrawork` (or `ulw`) that activates every agent until task is done.

**Tier:** T1 Agent-as-assistant (16th T1 entrant in Storm Bear corpus; extends T1 from N=15 post-v51 Vercel).

**Sub-archetype:** Solo-Korean-Seoul-OpenClaw-fork-harness with EXTREME primitive surface (1,766 TS files / 377K LOC). Sister archetype to OMC v27 Yeachan Heo (also Korean Seoul, also OpenClaw-based, also `oh-my-*` naming, also Sisyphus mythology).

**Scale:** 54,135 stars / ~4.7 months ≈ ~11.5K stars/month sustained-community-viral; 4,394 forks (8.1%); 651 open issues (HIGH community contribution churn); v3.17.5 (200+ releases mature); pushed today (2026-04-25); ~30 MB repo; default branch `dev` (corpus-first `dev` default at T1).

## 2. Why it exists (philosophy + manifesto)

**Manifesto principle (corpus-first explicit):** *"HUMAN IN THE LOOP = BOTTLENECK. Think about autonomous driving. When a human has to take over the wheel, that's not a feature. It's a failure of the system. Why is coding any different? Oh My OpenAgent is built on this premise: Human intervention during agentic work is fundamentally a wrong signal. If the system is designed correctly, the agent should complete the work without requiring you to babysit it."*

**Adversarial-Anthropic positioning (corpus-first explicit subject README claim):** *"Anthropic blocked OpenCode because of us. Yes this is true. They want you locked in. Claude Code's a nice prison, but it's still a prison. We don't do lock-in here. We ride every model. Claude / Kimi / GLM for orchestration. GPT for reasoning. Minimax for speed. Gemini for creativity."*

⚠️ Subject-claim caveat: "Anthropic blocked OpenCode because of us" is asserted in README and references X.com @thdxr post. Storm Bear vault has not independently verified the underlying incident. Document with caveat.

**Indistinguishable-code goal:** *"Code written by the agent should be indistinguishable from code written by a senior engineer. Not 'AI-generated code that needs cleanup.' The actual, final, production-ready code."*

**Token-cost vs productivity:** Higher token usage acceptable for productivity gains; cheaper models for simple tasks; cache learnings across sessions.

**Comparison to corpus autonomy poles:**
- paperclip v14: "zero-human companies" (organizational endpoint framing; Pattern #13 retired)
- omo v52: "Human In The Loop = BOTTLENECK" (operational signal framing; autonomous-driving analogy)
- Both reach Pattern #51 Vibe-Coding Spectrum anti-vibe / pro-full-autonomy via different framings

## 3. Architecture (5-step initialization)

```
pluginModule.server(input, options)
  ├─→ loadPluginConfig()         # JSONC parse → project/user merge → Zod validate → migrate
  ├─→ createManagers()           # TmuxSessionManager, BackgroundManager, SkillMcpManager, ConfigHandler
  ├─→ createTools()              # SkillContext + AvailableCategories + ToolRegistry (26 tools)
  ├─→ createHooks()              # 3-tier: Core(43) + Continuation(7) + Skill(2) = 52 hooks
  └─→ createPluginInterface()    # 10 OpenCode hook handlers → PluginInterface
```

Plugin entry: `src/index.ts` → default export `pluginModule` shape `{ id, server }`.

**Multi-level config:**
```
Project (.opencode/oh-my-opencode.jsonc)  →  User (~/.config/opencode/oh-my-opencode.jsonc)  →  Defaults
```

**Config format:** JSONC with comments, Zod v4 validation, snake_case keys. 32 schema files in `src/config/`. Idempotent migrations via `_migrations` tracking. Atomic writes with timestamped backups.

**Module structure:** 104 barrel index.ts files. No path aliases (`@/`); relative imports only. 200 LOC soft limit per file. Catch-all files (`utils.ts`, `helpers.ts`) banned. Factory pattern (`createXXX()`) for all tools/hooks/agents.

**Runtime:** Bun only (1.3.11 in CI). Never npm/yarn. TypeScript strict mode + ESNext + bundler moduleResolution + `bun-types`.

## 4. Greek-mythology specialist agents (11 named)

| Agent | Role | Default model |
|---|---|---|
| **Sisyphus** | Main orchestrator; "Does not stop halfway" | claude-opus-4-7 / kimi-k2.5 / glm-5 |
| **Sisyphus-Junior** | Lighter-scope variant | (configurable) |
| **Hephaestus** | Autonomous deep worker; "Legitimate Craftsman" | gpt-5.4 |
| **Prometheus** | Strategic planner; interview mode | claude-opus-4-7 / kimi-k2.5 / glm-5 |
| **Oracle** | Architecture/debugging | (configurable) |
| **Librarian** | Docs/code search | (configurable) |
| **Explore** | Fast codebase grep | (configurable) |
| **Atlas** | (per AGENTS.md inventory) | (configurable) |
| **Metis** | (per AGENTS.md inventory) | (configurable) |
| **Momus** | Critic/reviewer (Greek god of satire) | (configurable) |
| **Multimodal-Looker** | Vision-augmented inspection | (vision-capable model) |

**Pattern #25 Personality-Driven Agent Design retired v27** — Greek-mythology cluster documented as aesthetic/cultural choice; NOT re-registered.

Per-agent factory pattern (`createXXXAgent`) + agent-builder + dynamic-agent-prompt-builder + 14 overridable agent fields × 21 fields each. Agent modes: `primary` (respects UI model) vs `subagent` (own fallback chain) vs `all`. Model resolution: 4-step (override → category-default → provider-fallback → system-default).

## 5. 26 tools across 17 subdirs

| Subdir | Tool family | Notes |
|---|---|---|
| ast-grep | AST-aware code search/rewrite | 25 languages; wraps `@ast-grep/cli` + `@ast-grep/napi` |
| background-task | Parallel background agents | 5 concurrent per model/provider; circuit breaker |
| call-omo-agent | Call other agents | Inter-agent dispatch |
| delegate-task | Category-based delegation | 8 categories: visual-eng / deep / quick / ultrabrain / + 4 more |
| glob | File glob matching | Standard glob support |
| grep | Text search | Wraps grep |
| **hashline-edit** | LINE#ID content-hash-validated edits | **Corpus-first hash-anchored edit at T1** |
| interactive-bash | Tmux-backed bash sessions | REPLs / debuggers / TUIs persist |
| look-at | Multimodal file/screenshot viewing | Vision-capable model required |
| lsp | LSP integration | rename / goto_definition / find_references / diagnostics |
| session-manager | Tmux session lifecycle | Per-agent + cross-agent |
| skill | Skill invocation | Bridges to skill-mcp |
| skill-mcp | Skill-embedded MCP management | Tier 3 MCPs; per-session stdio + HTTP |
| slashcommand | Slash command dispatch | ultrawork / ulw / start-work / init-deep / + others |
| task | Task tracking | Todo enforcement (per `todo-enforcer` hook) |

**hashline-edit spotlight (corpus-first at T1):**
- Inspired by oh-my-pi (github.com/can1357/oh-my-pi) + cited blog "The Harness Problem" by Can Bölük
- Every Read output tagged with `LINE#ID` content hashes (e.g., `11#VK| function hello() {`)
- Edits reference those hash tags; reject on hash mismatch before applying
- README claim: "Grok Code Fast 1: 6.7% → 68.3% success rate. Just from changing the edit tool."
- Pattern #19 archetype 2 methodology-lineage NEW influence node observation: Can Bölük joins corpus-first

## 6. 52 lifecycle hooks across 5 tiers

| Tier | Count | Examples |
|---|---|---|
| Session | 24 | created / deleted / idle / error / + 20 more lifecycle |
| Tool-Guard | 14 | file-guard / label-truncator / rules-injector / prometheus-md-only / + 10 more |
| Transform | 5 | context-injection / thinking-block-validation / tool-pair-validation / + 2 |
| Continuation | 7 | context+todo preservation during compaction / + 6 more |
| Skill | 2 | skill-specific hooks |

**10 OpenCode hook handlers** wrap the 52 hooks (config / tool / chat.message / chat.params / chat.headers / event / tool.execute.before / tool.execute.after / experimental.chat.messages.transform / experimental.session.compacting).

**comment-checker hook** = corpus-first explicit AI-slop-prevention hook at T1. Enforces "no em dashes / en dashes / AI filler phrases" anti-pattern.

**hashline read enhancer** = post-tool hook tagging Read output with LINE#ID content hashes. Architectural foundation for hashline-edit tool.

## 7. 3-tier MCP system (corpus-first explicit at T1)

| Tier | Source | Mechanism | Examples |
|---|---|---|---|
| **Built-in** | `src/mcp/` | 3 remote HTTP MCPs | websearch (Exa/Tavily) + context7 (official docs) + grep_app (GitHub code search) |
| **Claude Code** | `.mcp.json` | `${VAR}` env expansion via `claude-code-mcp-loader` | User-configured per Claude Code convention |
| **Skill-embedded** | SKILL.md YAML | Per-session stdio + HTTP via `skill-mcp-manager` | Skills bring own MCP servers |

**Skill-embedded MCP rationale (verbatim):** *"MCP servers eat your context budget. We fixed that. Skills bring their own MCP servers. Spin up on-demand, scoped to task, gone when done. Context window stays clean."*

→ Pattern #18 strengthening: omo treats MCP as 3-tier scoping mechanism (architectural Layer-1 sub-tiering).

→ Pattern #18 OpenCode-primary observation N=2 UN-STALE at v52 (joins aidevops v47 N=1 stale-risk-flagged with v52 stale-check; structural-N=2 promotion-candidate at next mini-audit).

## 8. Multi-runtime category-based model routing

**4 README-named categories** (likely 8 in `src/tools/delegate-task/constants.ts`):
- `visual-engineering` — Frontend, UI/UX, design
- `deep` — Autonomous research + execution
- `quick` — Single-file changes, typos
- `ultrabrain` — Hard logic, architecture decisions (routes to GPT-5.4 xhigh)

**6+ providers in stack:**
- Claude Opus 4.7 (orchestration)
- Kimi K2.5 (orchestration alt)
- GLM 5 (orchestration alt)
- GPT-5.4 (deep work + ultrabrain)
- Minimax (speed)
- Gemini (creativity)

**Subscription-rotation strategy:** README recommends ChatGPT $20 + Kimi $0.99 + GLM $10 stack. Parallel to aidevops v47's 4-provider OAuth pool.

→ Pattern #28 14th+ data point + category-based routing as 4th sub-axis (joins routing-abstraction + native-multi-provider + verification-not-routing 3-axis taxonomy).

## 9. Built-in slash commands

- **`ultrawork`** / **`ulw`** — primary entrypoint; "every agent activates, doesn't stop until done"
- **`/ulw-loop`** / **Ralph Loop** — self-referential loop; "doesn't stop until 100% done"
- **`/start-work`** — calls Prometheus interview-mode planner
- **`/init-deep`** — auto-generates hierarchical AGENTS.md files throughout project
- (Additional commands likely in `src/features/builtin-commands/` not enumerated)

**`ultrawork` + ralph loop** = corpus-first explicit "doesn't stop until done" command primitives at T1. Operationalizes manifesto autonomy-max framing.

**`/init-deep`** = corpus-first auto-generation of hierarchical AGENTS.md at T1. Justifies Pattern #22 22a auto-generated sub-observation (within 22a; NOT new sub-variant per consolidation-forward).

## 10. Claude Code compatibility

**5 dedicated Claude-code-* loader feature modules:**
- `claude-code-agent-loader` — Claude Code agents
- `claude-code-command-loader` — Claude Code commands
- `claude-code-mcp-loader` — `.mcp.json` with `${VAR}` env expansion
- `claude-code-plugin-loader` — Claude Code plugins
- `claude-code-session-state` — session continuity

**README claim (verbatim):** *"You dialed in your Claude Code setup. Good. Every hook, command, skill, MCP, plugin works here unchanged. Full compatibility, including plugins."*

→ Validates README claim at architecture level. omo IS strict superset of Claude Code feature surface.

## 11. Distribution + installation

**11 platform-specific compiled binaries** via Bun compile:
- darwin × {arm64, x64, x64-baseline}
- linux × {arm64, arm64-musl, x64, x64-baseline, x64-musl, x64-musl-baseline}
- windows × {x64, x64-baseline}

→ Corpus-most-platform-binary distribution at T1.

**npm dual-bin alias:** `oh-my-opencode` AND `oh-my-openagent` shell to same `bin/oh-my-opencode.js` (Pattern #58 58c sub-variant NEW v52).

**Installation paths:**
1. **For Humans:** Paste install prompt to LLM agent (Claude Code / AmpCode / Cursor / etc.)
2. **For LLM Agents:** `curl -s https://raw.githubusercontent.com/code-yeongyu/oh-my-openagent/refs/heads/dev/docs/guide/installation.md`
3. Manual: read `docs/guide/installation.md` directly

**Telemetry:** PostHog with hashed installation ID. Opt-out: `OMO_SEND_ANONYMOUS_TELEMETRY=0` OR `OMO_DISABLE_POSTHOG=1`. Privacy Policy + ToS in `docs/legal/`.

## 12. Reception (subject-claim caveat applied)

**Pattern #50 50b recruiting-as-funnel-terminus testimonials (verbatim):**
- *"You guys should pull this into core and recruit him. Seriously. It's really, really, really good."* — Henning Kilset
- *"Hire @yeon_gyu_kim if you can convince him, this dude has revolutionized opencode."* — mysticaltech

**Productivity claims (verbatim, subject-claim caveat):**
- *"It made me cancel my Cursor subscription."* — Arthur Guiot
- *"Knocked out 8000 eslint warnings with Oh My Opencode, just in a day"* — Jacob Ferrari
- *"I converted a 45k line tauri app into a SaaS web app overnight using Ohmyopencode and ralph loop."* — James Hargis
- *"If Claude Code does in 7 days what a human does in 3 months, Sisyphus does it in 1 hour."* — B, Quant Researcher

⚠️ Caveat: Testimonials are subject-claim per README selection; representative selection bias possible. Independent verification not performed by Storm Bear vault.

**Adoption signals:**
- 54K stars / 4.7 months
- 4,394 forks (8.1%)
- 651 open issues (HIGH community contribution churn — typical of viral plugin)
- Discord community 1.4K members
- 200+ npm releases (3.x active development)
- YouTube reviews (Darren Builds AI: "Oh My OpenCode Is Actually Insane")

## 13. Cross-references + Pattern Library impact

**Cross-wiki siblings:**
- **OMC v27 Yeachan Heo** — Korean Seoul T1 ecosystem peer; cited "oh-my-opencode" as 1 of 5 inspirational sources (Pattern #57 57c structural N=2 promotion-candidate)
- **obra/superpowers v2 (Jesse Vincent)** — omo's `docs/superpowers/` subdir directly cites/integrates (Pattern #57 57a 5th data point)
- **aidevops v47** — Pattern #18 OpenCode-primary observation N=1 → omo v52 = N=2 UN-STALE + promotion-candidate
- **paperclip v14** — autonomy-max framing precedent ("zero-human" vs omo "Human In The Loop = BOTTLENECK")
- **GitNexus v33** — Pattern #72 PolyForm Noncommercial sibling; SUL-1.0 = N=2 sub-context within Pattern #29
- **pi-mono v36** — solo-multi-package monorepo parallel; both have LSP-tool-suite at agent-tool level
- **vercel-labs v51** — Pattern #57 57c sibling (v51 was 57c N=1; omo v52 is 57c N=2)
- **multica v15 / graphify v16 / agency-agents v18** — prior OpenClaw-corpus presences

**Pattern Library impact at v52:**
- Pattern #57 57a 5th data point strengthening
- **Pattern #57 57c structural N=2** at v52 — promotion-candidate at next mini-audit under structural-N=2 criterion
- **Pattern #18 OpenCode-primary observation N=2** UN-STALE — promotion-candidate at next mini-audit under structural-N=2 criterion
- Pattern #58 sub-variant 58c rebrand-repo-keep-npm-package + dual-bin-alias NEW v52 (N=1 stale-flagged)
- Pattern #50 sub-variant 50d incubation-waitlist-as-funnel-terminus NEW v52 (N=1 stale-flagged)
- Pattern #29 NEW sub-context custom-non-OSI-non-commercial-restriction (N=2 with PolyForm GitNexus v33)
- Pattern #73 73a Korean strengthening (N=2 Korean-Seoul-T1; sub-observations: oh-my-* naming + Sisyphus mythology + OpenClaw-fork-extension)
- Pattern #28 14th+ data point + category-based routing sub-axis
- Pattern #19 archetype 2 methodology-lineage NEW influence node Can Bölük (oh-my-pi / The Harness Problem blog)
- Pattern #2 distribution evolution corpus-most-platform-binary at T1 strengthening
- Pattern #12 v42 refined 7th counter-evidence wiki (HOLDS)
- Pattern #17 variant 1 19th+ data point strengthening
- Pattern #27 sustained-community-viral ~11.5K stars/month

→ **0 new active candidates registered. 16-CONSECUTIVE-WIKI ZERO-REGISTRATION STREAK NEW LONGEST in corpus history (v37-v52).**

# Entity: codex-plugin-cc (core product) — T4 Bridge competitor-platform-plugin

> **Wiki:** codex-plugin-cc v62 / 2026-05-08
> **Format:** 13-section canonical entity page

---

## 1. Identity

**codex-plugin-cc** is a **T4 Bridge plugin** that integrates OpenAI Codex into Anthropic Claude Code workflows via 7 slash commands, enabling code reviews and task delegation without context switching between IDEs. **CORPUS-FIRST competitor-published plugin for rival platform.**

## 2. Source

- Repo: [`openai/codex-plugin-cc`](https://github.com/openai/codex-plugin-cc)
- License: Apache-2.0
- Stars: 17,800 / Forks: 1,000 / Watchers: 59 / Open issues: 104 / Commits: 26
- Primary lang: JavaScript 100%
- Latest: v1.0.4 (2026-04-18)
- Author: OpenAI organization (corporate-official)

## 3. Tier placement

**T4 (Bridge — competitor-platform-bridge-as-plugin).**

3rd Pattern #18 Layer 2 sub-archetype (after content-transformation N=8 + protocol-translation N=1 free-claude-code v60 + install-time-skill-format-translator cc-sdd v61). Mechanism distinct from prior sub-archetypes: cross-vendor IDE plugin (Claude Code host → Codex backend; runtime delegation; cross-vendor authentication required).

Alternative considered: T1 Augmentation. Rejected — surface in Claude Code but function = cross-platform integration; bridge framing more honest.

## 4. Core mechanism

**7 slash commands organized 3 ways:**

| Category | Commands | Purpose |
|---|---|---|
| Review | `/codex:review` + `/codex:adversarial-review` | Pre-shipping code review with optional adversarial framing |
| Task delegation | `/codex:rescue` | Long-running investigation/fix delegation to Codex |
| Background-task lifecycle | `/codex:status` + `/codex:result` + `/codex:cancel` | 4-command lifecycle with rescue (NEW corpus-first explicit surface) |
| Setup | `/codex:setup` | Authentication + installation verification |

**Plugin architecture (6 primitive types):**
- `agents/` — agent skill implementations
- `commands/` — slash command implementations
- `hooks/` — lifecycle hooks
- `prompts/` — prompt templates (incl. adversarial-review reframing prompt)
- `schemas/` — JSON schemas
- `skills/` — skill definitions

**Cross-vendor authentication:** Local auth via Codex app server; ChatGPT subscription OR OpenAI API key required; user authenticates to Codex separately from Claude Code session.

## 5. Adversarial review mechanism (counter-evidence to Pattern #76)

`/codex:adversarial-review` *"reframes existing review function"* — same Codex review function, adversarial system/user prompt variation. Targets design decisions over implementation details; accepts custom focus text + `--base <ref>`.

**Key distinction from cc-sdd v61 Pattern #76 N=1 baseline:**

| Dimension | cc-sdd v61 (Pattern #76) | codex-plugin-cc v62 |
|---|---|---|
| Reviewer role | Separate `kiro-review` subagent | Same review function |
| Mechanism stratum | Architectural (role separation) | Prompt-engineering (template variation) |
| Auto-debug-on-rejection | Yes | No |
| Fresh-evidence completion gate | Yes | No |

Counter-evidence narrows Pattern #76 scope to "adversarial-by-design role separation as architectural primitive specifically — not adversarial-framed prompts within same review function."

## 6. Differentiators (vs corpus T4 sub-archetypes)

| Sub-archetype | Wiki | Mechanism | Translation timing |
|---|---|---|---|
| api-protocol-translation-proxy | free-claude-code v60 | Anthropic Messages ↔ provider protocols | Runtime |
| install-time-per-platform-skill-format-translator | cc-sdd v61 | Skill format adapter | Install-time |
| **competitor-platform-bridge-as-plugin** | **codex-plugin-cc v62** | **Cross-vendor IDE delegation** | **Runtime** |

Distinct mechanism: codex-plugin-cc bridges between vendor platforms (Anthropic ↔ OpenAI) at IDE-plugin level, not at API-protocol or skill-format level.

## 7. Origin / lineage

- OpenAI corporate-strategic origin (corpus 2nd corporate-org after Microsoft spec-kit/markitdown)
- v1.0.4 with 26 commits = highly-condensed development; small team velocity
- Apache-2.0 license = OpenAI corporate-AI-tool default (matches spec-kit + magika observations)
- No external methodology lineage (no SDD / BMM / TDD / Karpathy / EARS); functional-tool-shaped
- Strategic motive: marketshare retention via cross-publication (acknowledges Claude Code UX preference)

## 8. Adoption signals

- 17.8K stars / 26 commits = ~684 stars-per-commit (extreme density signaling viral attention on small commit base)
- 1K forks (5.6% fork ratio — typical OSS engagement)
- 104 open issues at 26 commits = active community engagement
- Launched April 2026; ~3 weeks at v62 ship — very recent
- ChatGPT subscription gate filters non-OpenAI users

## 9. Limitations / failure modes

- ❌ ChatGPT subscription OR OpenAI API key REQUIRED (gates non-OpenAI users)
- ❌ Single-host (Claude Code only) — not multi-platform plugin
- ❌ One-direction integration (Claude Code → Codex only; Codex CLI cannot invoke Claude Code)
- ❌ Cross-vendor authentication overhead (separate auth flow)
- ❌ EN-only documentation (no i18n)
- ❌ No MCP integration (Codex backend not MCP-exposed)
- ❌ Apache-2.0 NOTICE file overhead vs MIT
- ⚠️ Cross-vendor supply-chain implications (trust boundary spans Anthropic + OpenAI)

## 10. Storm Bear vault applicability

**Pilot relevance: MEDIUM-HIGH (top-5 candidate but conditional on cc-sdd pilot).**

Why:
- Storm Bear has ChatGPT subscription (gate satisfied)
- Direct deployable for vault Claude Code workflow as code-review augmentation
- Apache-2.0 license compatible with vault commercial use
- Adversarial-review feature complements cc-sdd v61 pilot (#1) for comparison study

Caveats:
- Single-host plugin (Claude Code only) — narrower leverage than cc-sdd multi-platform
- Cross-vendor cost overhead (ChatGPT subscription tokens consumed)
- Best as **comparison-pilot** to cc-sdd, not standalone

**Recommended pilot scope:**
1. Install via `/plugin marketplace add openai/codex-plugin-cc` + `/plugin install codex@openai-codex` (~30 min including Codex auth setup)
2. Run `/codex:review` + `/codex:adversarial-review` on same diff cc-sdd `kiro-review` reviews (apple-to-apple comparison)
3. Measure: review-quality / latency / cost / ergonomics
4. Document `04 Reviews/(C) 2026-05-XX codex-plugin-cc comparison-pilot.md`

## 11. Open questions

See `01 Analysis/(C) open questions.md` — 20 questions covering project / org / Pattern Library / vault / methodology.

## 12. Cross-references

**Pattern #76 N=1 baseline + counter-evidence:**
- [cc-sdd v61](../../cc-sdd%20-%20Beginner%20Analysis/) — separate-role architectural primitive

**T4 Bridge sub-archetype peers:**
- [free-claude-code v60](../../free-claude-code%20-%20Beginner%20Analysis/) — api-protocol-translation-proxy (Layer 2 sibling)
- [cc-sdd v61](../../cc-sdd%20-%20Beginner%20Analysis/) — install-time-skill-format-translator (Layer 2 sibling)
- [graphify v16](../../graphify%20-%20Beginner%20Analysis/) — content-transformation T4
- [markitdown v28](../../markitdown%20-%20Beginner%20Analysis/) — content-transformation T4 (Microsoft corporate sibling)

**Corporate-strategic archetype peers:**
- [spec-kit v17](../../spec-kit%20-%20Beginner%20Analysis/) — Microsoft GitHub corporate T1
- [markitdown v28](../../markitdown%20-%20Beginner%20Analysis/) — Microsoft corporate T4

**Claude Code plugin marketplace peers (Pattern #59):**
- [oh-my-claudecode v27](../../oh-my-claudecode%20-%20Beginner%20Analysis/)
- [claude-hud v35](../../claude-hud%20-%20Beginner%20Analysis/)

**Pattern Library entries referenced:**
- Pattern #76 Adversarial Subagent Review Architecture (N=1 baseline; counter-evidence at v62)
- Pattern #18 Layer 2 sub-archetype (3rd at codex-plugin-cc)
- Pattern #19 corporate-strategic archetype (N=2 cross-org)
- Pattern #59 Claude Code Plugin Marketplace Native (corporate-scale strengthening)
- Pattern #57 implicit-host-platform citation (observation)
- NEW Pattern #77 candidate: Cross-Vendor Cooperative Plugin Publication
- NEW Pattern candidate: Background-Task-Lifecycle-Primitive-Set
- NEW sister to Pattern #76: Adversarial-Review-as-Prompt-Framing-Variant

## 13. Next action

For Pattern Library: register counter-evidence-driven refinement of Pattern #76 + 4 new candidate observations at next mini-audit (v66 natural cadence per v63 audit triggers).

For Storm Bear vault: consider as comparison-pilot to cc-sdd v61 pilot (parallel deployment of both adversarial-review mechanisms on same diffs).

For corpus monitoring: watch for 2nd cross-vendor-cooperation observation (Anthropic publishing for Codex CLI? GitHub Copilot for Claude Code?) to un-stale-flag NEW Pattern #77 candidate.

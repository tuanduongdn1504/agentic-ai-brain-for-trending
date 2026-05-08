# Cluster 1 — User-facing docs

> **Sources:** README.md (English) + landing tagline + 13-language i18n note + installation flags + workflow walkthrough.
> **Wiki:** cc-sdd v61.

---

## 1. Verbatim positioning / tagline

> *"Turn approved specs into long-running autonomous implementation. A minimal, adaptable SDD harness with Agent Skills for Claude Code, Codex, Cursor, Copilot, Windsurf, OpenCode, Gemini CLI, and Antigravity."*

> *"explicit contracts at the right granularity let AI-driven development at team scale move faster, not slower"* (philosophy)

> *"specifications as contracts between system components rather than top-down commands. Code remains the source of truth, while specs make boundaries explicit"*

## 2. Installation surface

```bash
cd your-project
npx cc-sdd@latest
```

Optional platform flags (one per supported agent):
- `--claude-skills` (default — Claude Code)
- `--codex-skills` (Codex)
- `--cursor-skills` (Cursor IDE)
- `--copilot-skills` (GitHub Copilot)
- `--windsurf-skills` (Windsurf IDE)
- `--opencode-skills` (OpenCode)
- `--gemini-skills` (Gemini CLI)
- `--antigravity` (Antigravity — experimental)

Language selection: `--lang ja` / `--lang zh-TW` / 11 additional codes (13 total).

## 3. Supported platform table (verbatim from README)

| Platform | Status | Skills Mode flag |
|---|---|---|
| Claude Code | Stable | `--claude-skills` (default) |
| Codex | Stable | `--codex-skills` |
| Cursor IDE | Beta | `--cursor-skills` |
| GitHub Copilot | Beta | `--copilot-skills` |
| Windsurf IDE | Beta | `--windsurf-skills` |
| OpenCode | Beta | `--opencode-skills` |
| Gemini CLI | Beta | `--gemini-skills` |
| Antigravity | Experimental | `--antigravity` |

**Observation:** 2 stable + 5 beta + 1 experimental = unequal-maturity-distribution-across-8-platforms. Claude Code is reference-stable; treats other platforms as derivatives needing per-platform Skills format adaptation. Distinct from OpenSpec v58 30+ tools (no maturity tier disclosed) and free-claude-code v60 6-providers (homogeneous-stable).

## 4. Typical workflow walkthrough (README)

For a new feature like Photo Albums:

1. `/kiro-discovery` → generates `brief.md` + suggests next command
2. `/kiro-spec-init` → initialize specification
3. `/kiro-spec-requirements` → EARS-format requirements
4. `/kiro-spec-design` → architecture with Mermaid diagrams
5. `/kiro-spec-tasks` → implementation tasks with boundaries
6. `/kiro-impl` → autonomous execution (TDD + independent review + auto-debug)

**Observation:** 6-step linear workflow with explicit human-approval gates at requirements/design/tasks boundaries. Compare to spec-kit v17 9-article constitution + plan/specify/tasks (3-step) — cc-sdd has finer-grained intermediate steps with discovery routing.

## 5. Output artifacts

| File | Format | Purpose |
|---|---|---|
| `brief.md` | natural language | Initial discovery output |
| `roadmap.md` | natural language | Multi-feature project map |
| `requirements.md` | EARS-formatted | Acceptance criteria |
| `research.md` | investigation notes | Generated when discovery needs investigation |
| `design.md` | architecture + Mermaid + File Structure Plan | Technical design |
| `tasks.md` | checkboxes + P-wave annotations + boundaries | Implementation breakdown |
| `spec.json` | metadata | Phase status tracking |

**Observation:** Output artifact set similar to spec-kit v17 (specify.md / plan.md / tasks.md) but extends with: (a) discovery-phase artifacts (brief.md / roadmap.md), (b) research.md for investigation, (c) tasks.md richer (P-waves + boundary markers + dependency annotations).

## 6. Customization

> *"Teams can edit templates and rules in `{{KIRO_DIR}}/settings/` to match workflow preferences, including PRD-style requirements, API schemas, approval gates, and domain-specific standards."*

`{{KIRO_DIR}}` = `.kiro/` by default (configurable). Templates editable per-team.

## 7. i18n coverage (Greek added v2.0.5)

**13 languages supported** via `--lang <code>` flag. Documentation explicitly available in:
- English (default)
- Japanese (ja/ subdirectory in docs/guides/)
- Traditional Chinese (zh-TW)
- + 10 more (Greek added v2.0.5; full list inferred from CHANGELOG)

**Observation:** 13-language coverage exceeds OpenSpec v58 (30+ tools but unclear i18n) and matches/exceeds spec-kit v17 (English-primary). Reflects gotalab's Japan-based authorship + active i18n maintenance.

## 8. Corpus-first observations

- **CORPUS-FIRST Kiro IDE methodology lineage** (v3.0.2 CHANGELOG removed Amazon book reference; `.kiro/` directory convention implies Kiro IDE methodology heritage — first time corpus encounters this lineage chain)
- **Solo-Japanese T1 author** at the README level (gotalab — Japan / "Agentic AI Engineer / Data Analyst" / Zenn-platform-active)
- **Skills-mode-as-primary-install-target** (8 platforms; v3.0.0 architectural shift; deprecated command-based installs as secondary)
- **`brief.md` as discovery routing artifact** — corpus-first dedicated discovery output (not requirements not design — pre-spec routing decision file)
- **EARS-format requirements explicit reference** — first time corpus encounters EARS by name (spec-kit v17 mentions structured requirements but not EARS naming)
- **File Structure Plan (FSP)** as design.md sub-section — corpus-first explicit FSP primitive
- **P-wave task priority annotation** (P0, P1, etc.) — corpus-first explicit wave-based priority model
- **Boundary marker per-task** in tasks.md — corpus-first per-task boundary annotation primitive

## 9. Absences (vs prior corpus subjects)

- ❌ NO direct mention of OpenClaw runtime
- ❌ NO direct mention of Hermes runtime
- ❌ NO MCP-server primitive (skillport sibling product DOES — not cc-sdd itself)
- ❌ NO direct citation of spec-kit v17 / OpenSpec v58 / GSD v5 (cc-sdd does not foil these in 57c-anti-pattern style)
- ❌ NO Karpathy / Bostrom / John Lam citation
- ❌ NO 9-article constitution (vs spec-kit v17)
- ❌ NO marketplace ecosystem (vs spec-kit v17 80+ marketplace)
- ❌ NO research-paper-chain (vs ai-agents-for-beginners / autoresearch / LlamaFactory)

## 10. Counter-evidence flags (vs Pattern Library)

- **Pattern #51 Vibe-Coding spectrum NUANCE** — cc-sdd anti-vibe BUT explicitly acknowledges vibe-coding's legitimate use cases ("/kiro-discovery can legitimately conclude that no specification is needed"; "If the discipline feels like overhead, your specs are probably too big"). Refines spec-kit v17's pure anti-vibe stance toward an anti-vibe-with-pragmatic-acknowledgment sub-pole. Counter-evidence-driven refinement candidate.

## 11. Pattern advancement check

- **Pattern #21 SDD Methodology Emergence** — un-stale strong evidence (3rd-4th independent SDD framework with novel solo-Japanese archetype; un-stale criterion satisfied per v25-flag promotion criterion)
- **Pattern #18 Layer 2 sub-archetype** — agent-platform-format-translation-installer N=1 candidate registration
- **Pattern #19 first-mover-authority-without-lineage** — gotalab ecosystem-portfolio strengthens N=2 (already at N=2 post-v60 free-claude-code)
- **Pattern #55 solo-regional T1 archetype** — Japan added (4th regional after VN/CN/Korean)

## 12. Section-level observations

- README structure: Overview → Core Concept → Key Features in v3.0 → Installation → Supported Platforms → Typical Workflow → Output Artifacts → Customization → Documentation Resources → License
- README tagline opens with "Turn approved specs into long-running autonomous implementation" — verb-first action framing (vs spec-kit v17 noun-first "spec-driven development for AI agents")
- README mentions "8 different AI coding agents" — count is foreground, not platform names
- Workflow described in concrete-feature example (Photo Albums) not abstract — pedagogically warmer than spec-kit v17

## 13. Cross-wiki corpus-context

- Direct sibling: spec-kit v17 (T1 SDD Microsoft) + OpenSpec v58 (T1 SDD Fission-AI) + GSD v5 / gsd-2 v54 (T1 SDD gsd-build)
- Adjacent ecosystem: free-claude-code v60 (T4 6-provider proxy) + n8n v56 (16-LLM platform) + mattpocock-skills v57 (Agent Skills builder)
- Solo-regional peers: codymaster v12 (VN) + TrendRadar v19 (CN) + OMC v27 (Korean)

## 14. Supply-chain awareness

- ❌ No untrusted-code ingestion (cc-sdd does NOT distribute third-party plugins — installs gotalab's own templates)
- ⚠️ However `npx cc-sdd@latest` runs latest npm package; standard npm supply-chain risk applies
- ⚠️ Templates editable + customizable — locally-edited templates not signed/verified, but that's appropriate for team-customization
- ✅ Generally low supply-chain risk surface compared to aggregator-genre subjects (awesome-mcp-servers / awesome-claude-skills / awesome-design-md)

## 15. Length / granularity note

README is concise (~120 lines estimated). Detailed workflow examples + per-skill behaviors live in `docs/guides/*.md` (covered in Cluster 3). Reflects gotalab's preference for layered documentation: high-level overview → detailed guides on demand.

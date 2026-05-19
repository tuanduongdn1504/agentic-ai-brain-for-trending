# Phase 4b PRIMARY proposal — Pattern #84 84c N=5 STRENGTHENING with NEW sub-mechanism "CLI-generates-native-formats-from-canonical-source"

**Wiki:** v76 HoangNguyen0403/agent-skills-standard
**Date:** 2026-05-19
**Type:** Phase 4b PRIMARY (sub-mechanism strengthening + NEW sub-sub-mechanism candidate within already-CONFIRMED Pattern #84 84c sub-mechanism)
**Phase 4b vehicle class:** Sub-mechanism N-strengthening with mechanism-layer-distinction registration (extends v66 Pattern #19 19a/b/c/d strengthening vehicle + v70 codegraph sub-mechanism formalization vehicle = 6th-vehicle hybrid)
**Confidence:** HIGH

## Executive summary

Pattern #84 Cross-Vendor Ecosystem-Tolerance was promoted to CONFIRMED at v72 PROMOTION-DRIVEN + 5TH-CONSECUTIVE-TRIGGER mini-audit with sub-taxonomy 84a Tool-tolerance + 84b Usage-enforcement + 84c Provider-Agnostic-By-Design. Sub-mechanism 84c has been strengthening monotonically across 5 consecutive wikis v71→v72→v73→v75→v76, and v76 introduces a **NEW sub-sub-mechanism layer-distinction within 84c distribution layer**: CLI-generates-native-formats-from-canonical-source (v76) vs repo-stored-N-harness-replicas (v75).

5-instance Pattern #84 sub-mechanism-strengthening arc within post-promotion window = **NEW CORPUS-RECORD** extending v75's 4-instance record.

## Sub-mechanism 84c definition (confirmed at v72 audit)

**84c "Provider-Agnostic-By-Design":** Single subject demonstrates cross-vendor distribution discipline as **author-design-choice** (internally-adopted by author as architectural principle), distinct from 84a Tool-tolerance (externally-applied by tool ecosystem) and 84b Usage-enforcement (provider-enforced by API).

## v76 agent-skills-standard evidence in detail

### Multi-harness coverage (10+ harnesses via CLI sync)

agent-skills-standard generates native formats for 10+ AI coding agents via `npx agent-skills-standard sync` CLI command:

| Harness | Native format | Output location |
|---------|---------------|-----------------|
| Claude Code | Command Markdown | `.claude/` |
| Roo | Command Markdown | (Roo-specific) |
| OpenCode | Command Markdown | `.opencode/` |
| Cursor | Skill folder with SKILL.md | `.cursor/rules/` |
| Trae | Skill folder with SKILL.md | `.trae/skills/` |
| Codex | Skill folder with SKILL.md | `.codex/skills/<workflow>/SKILL.md` |
| Gemini | TOML command files | (Gemini-specific) |
| GitHub Copilot | Prompt instruction files | `.github/instructions/*.instructions.md` |
| Windsurf | MCP + Rule Persistence | `.codeium/windsurf/mcp_config.json` |
| Kiro | Native Markdown workflows | (Kiro-specific) |
| Antigravity | Native Markdown workflows | `.antigravity/` |
| MCP | Tool definitions (JSON) | MCP-compatible runtimes |

### Mechanism distinction from v75 impeccable

This is the architecturally-defining distinction at v76:

| Aspect | v75 impeccable (repo-stored) | v76 agent-skills-standard (CLI-generated) |
|--------|------------------------------|-------------------------------------------|
| Storage location | 14 harness-specific directories pre-built into repo | Single canonical `skills/` directory |
| Per-harness output | Pre-replicated at build-time (CI generates 14× content) | Generated at user install-time via `sync` command |
| Repo size | Bloated (14× content footprint) | Minimal (1× content footprint) |
| Update propagation | Re-replicate all 14 directories at every build | User re-runs `npx agent-skills-standard sync` |
| User experience | Browse to chosen harness directory + copy | `npx ... init` + `sync` (zero browse) |
| New-harness onboarding | Add new directory to repo + update CI | Add new format generator template to CLI |
| Storage cost | Bloated repo size | Minimal |
| Maintenance cost | Build-time-replication CI | Run-time-generation CLI |
| Network round-trip cost | None (pre-built artifacts in repo) | Single download + local generation |

Both mechanisms serve Pattern #84 84c "Provider-Agnostic-By-Design" — author-design-choice for multi-target portability. Different mechanisms = distinct sub-sub-mechanisms within 84c.

### 5-instance Pattern #84 sub-mechanism-strengthening arc

| # | Wiki | Subject | Layer | Mechanism | Count metric | Status |
|---|------|---------|-------|-----------|--------------|--------|
| 1 | v71 | agents-best-practices | methodology | dual-vendor pattern-synthesis | 2 vendors (Anthropic + OpenAI) | 84c registration (pre-promotion) |
| 2 | v72 | DeepSeek-TUI | runtime | provider-API matrix | 9 providers | 84c N=2 post-promotion |
| 3 | v73 | cc-switch | runtime | provider-API matrix | 12 providers | 84c N=3 + CORPUS-RECORD migration |
| 4 | v75 | impeccable | distribution | **repo-stored-N-harness-replicas** | 14 harnesses | 84c N=4 + CORPUS-RECORD + new layer (distribution) |
| **5** | **v76** | **agent-skills-standard** | **CLI-generation** | **CLI-generates-native-formats-from-canonical-source** | **10+ harnesses (NEW MECHANISM)** | **84c N=5 + NEW CORPUS-RECORD + NEW sub-mechanism at distribution layer** |

## Three corpus-firsts at v76

### Corpus-first 1: FIRST 5-instance Pattern #84 sub-mechanism-strengthening arc within post-promotion window

Pattern #84 was promoted at v72. Sub-mechanism 84c has strengthened in EVERY post-promotion wiki:

| Post-promotion wiki | 84c strengthening contribution |
|---------------------|--------------------------------|
| v72 DeepSeek-TUI | 9-provider matrix (CORPUS-RECORD at v72) |
| v73 cc-switch | 12-provider matrix (CORPUS-RECORD at v73) |
| v75 impeccable | 14-harness distribution layer (CORPUS-RECORD at v75) |
| **v76 agent-skills-standard** | **NEW sub-mechanism mechanism-layer-distinction at distribution layer** |

5-wiki monotonic strengthening arc = **NEW CORPUS-RECORD** extending v75's 4-instance record.

No prior post-promoted pattern has achieved 5-instance arc. Most prior post-promoted patterns strengthen 1-2 instances within first 5 wikis post-promotion. Pattern #84 is now corpus-record exemplar of post-promotion sustainability.

### Corpus-first 2: FIRST CLI-generation distribution mechanism distinct from repo-stored replicas

v75 impeccable proved repo-stored model. v76 agent-skills-standard proves CLI-generated model. Two distinct sub-sub-mechanisms within 84c distribution layer:

- **84c.1 "repo-stored-N-harness-replicas"** (v75 impeccable)
- **84c.2 "CLI-generates-native-formats-from-canonical-source"** (v76 agent-skills-standard)

Both serve Pattern #84 84c "Provider-Agnostic-By-Design" goal. Different mechanisms.

### Corpus-first 3: FIRST sub-mechanism mechanism-layer-distinction within 84c

84c sub-mechanism now has explicit layer-distinction:

- **Methodology layer** (v71): synthesizing methodologies of multiple vendors
- **Runtime layer** (v72-v73): single client supports multiple upstream APIs
- **Distribution layer** (v75-v76): multi-harness skill distribution, with 2 sub-sub-mechanisms (repo-stored vs CLI-generated)

This is **FIRST explicit layer + mechanism-axis distinction within a single sub-mechanism** in the corpus.

## Promotion criteria evaluation (84c sub-mechanism layer)

Pattern #84 is already CONFIRMED. This proposal documents 84c sub-mechanism evolution and proposes:

1. **84c sub-mechanism formalization** (N=5 ≥ formal-sub-mechanism threshold; sustained across 5 wikis = corpus-record sustainability)
2. **84c sub-sub-mechanism registration**:
   - 84c.1 "repo-stored-N-harness-replicas" (v75 impeccable)
   - 84c.2 "CLI-generates-native-formats-from-canonical-source" (v76 agent-skills-standard)
3. **84c layer-distinction registration** (methodology + runtime + distribution layers all covered)

| Criterion | Status at v76 |
|-----------|---------------|
| N-count within sub-mechanism | N=5 (v71 + v72 + v73 + v75 + v76) ≥ formal-sub-mechanism threshold |
| Cross-tier evidence | T1 (v71) + T1 (v72) + T2 (v73) + T1 (v75) + T1 (v76) = 2-tier coverage (T1 dominant) |
| Cross-archetype evidence | Solo-Eastern-European (v71) + Solo-community (v72) + Solo-community-Chinese (v73) + Founder-personal-Google (v75) + Solo-VN-Hanoi (v76) = 5-archetype coverage |
| Measurement axis layer | Methodology (v71) + Runtime (v72-v73) + Distribution-repo-stored (v75) + Distribution-CLI-generated (v76) = 3-layer + 2-sub-sub-mechanism coverage |
| Sustainability | 5-instance monotonic-strengthening arc = NEW CORPUS-RECORD |
| Geographic coverage | Eastern-Europe + multiple Asian + USA + Vietnam = 4-continent coverage |

**Verdict:** 84c is now FULLY MATURE sub-mechanism with multi-layer + multi-archetype + multi-geographic + multi-sub-sub-mechanism coverage. No further evidence-strengthening required.

## Proposed audit actions at v77 mini-audit (if elected)

### Primary action

**Pattern #84 84c sub-mechanism formalization with layer-distinction:**

1. Promote 84c from sub-mechanism candidate (currently registered as sub-typology under Pattern #84 confirmed entry) to formal sub-mechanism with explicit Pattern Library entry
2. Register 3-layer coverage (methodology + runtime + distribution) as 84c structural property
3. Register 2 sub-sub-mechanisms within distribution layer (84c.1 repo-stored + 84c.2 CLI-generated)
4. Update Pattern Library entry with full 5-instance evidence chain

### Secondary actions from v76 contributions

- **Pattern #83 sub-mechanism 83f "license-declaration-vs-actual-mismatch" PROMOTION evaluation** at N=2 (v74 LLMs-from-scratch + v76 agent-skills-standard); promote to formal sub-mechanism within Pattern #83
- **Pattern #19 NEW sub-mechanism 19g "Vietnamese-Solo-Standards-Codifier" PROVISIONAL registration** (Hoang multi-product portfolio anchored by standards-codification)
- **Pattern #18 sub-mechanism B B1 MCP variant strengthening** (Transparent Interception + audit logs at v76; B1 N=3 with within-B1 sub-variant candidate "MCP-Transparent-Interception-with-audit-logs")
- **Pattern #78 N=4 CORPUS-RECORD codification density verification** (259 skills × 20+ frameworks at v76)
- **Pattern #82 N+1 quantitative-marketing verification** ("85% fewer tokens" + 540 tokens/skill + 90% scouting reduction + benchmark-report.md)
- **Pattern #66 6-axis supply-chain integrity discipline registration** (text-only + zero-telemetry + local-first + prompt-injection-scanning + Zod-validation + per-skill evals.json)
- **Pattern #57 sub-variant 57c-product 3+-corpus-subject ecosystem citation strengthening** (v62 Codex + v65 Claude Code system prompts + v71 agents-best-practices cited)
- **OC-X "Audit-Log-As-Enforcement-Layer" first-cycle stale-check** (MCP audit logs at v76)
- **OC-Y "Engagement-Deficit-Extreme-With-Active-Forks" first-cycle stale-check** (0 issues / 147 forks at v76)
- **OC-Z "VN-Solo-Developer-Standards-Codifier" first-cycle stale-check** (Hoang VN-Hanoi archetype at v76)
- **Library-vocabulary item #9 NEW CORPUS-RECORD 8-pattern couple-count verification** at v76
- **Library-vocabulary item #11 Engagement-Deficit-Extreme corpus-record-low strengthening verification** at v76

### Audit batch projection

Combined with v74 + v75 + v76 wiki audit-agenda contributions, v77 audit batch projected at ~15-18 items if elected at v77-natural-cadence trigger. Below v69's CORPUS-LARGEST 24-item batch and v72's 24-item batch. Manageable scale.

## Cross-corpus impacts

- **Pattern #84 84c 5-wiki monotonic corpus-record migration** = NEW CORPUS-RECORD post-promotion sustainability discipline; sets new floor for sub-mechanism strengthening expectations
- **Cross-layer + mechanism-axis sub-mechanism validation** (methodology + runtime + distribution layers; repo-stored + CLI-generated mechanisms at distribution layer) = 84c is fully mature sub-mechanism with multi-axis coverage
- **CORPUS-FIRST VN-located solo developer in v60+ window** = restores VN representation to corpus + provides direct structural-blueprint for Storm Bear vault-publication scenario
- **Hoang + agent-skills-standard + multi-harness ecosystem citation** = Pattern #57 sub-variant 57c-product strengthening (v62 Codex + v65 Claude Code system prompts + v71 agents-best-practices ecosystem all cited)
- **8-pattern coupled-design at single wiki** (Pattern #84 + #78 + #19 + #82 + #83 83f + #18 + #66 + #57) = NEW potential CORPUS-RECORD couple-count; Library-vocabulary item #9 strengthening
- **Storm Bear streak CORPUS-RECORD extension to 12 consecutive PASS** = post-v64-RESET corpus-record extension; first 4/4 STRONGEST since v66 agentmemory (10-wiki gap)

## Conclusion

Pattern #84 84c "Provider-Agnostic-By-Design" sub-mechanism has reached corpus-record sustainability through 5-instance monotonic strengthening with multi-layer + multi-mechanism + multi-archetype + multi-geographic coverage. Phase 4b PRIMARY proposal: ratify 84c as fully mature sub-mechanism with multi-axis coverage + register 2 sub-sub-mechanisms at distribution layer (repo-stored + CLI-generated) + register monotonic-corpus-record-migration as routine v2.3 codification candidate.

**No top-level Pattern #84 state change required** — pattern is already CONFIRMED. This proposal documents sub-mechanism maturation + proposes 84c formal sub-mechanism elevation + sub-sub-mechanism registration for v77 audit deliberation.

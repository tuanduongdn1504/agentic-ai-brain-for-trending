# claude-code-harness — Wiki (v107)

> *"Claude Code Dedicated Development Harness — Achieving High-Quality Development Through an Autonomous Plan→Work→Review Cycle."*

## 1. Identity & metadata

| Field | Value |
|---|---|
| Repo | `Chachamaru127/claude-code-harness` |
| Author | **Chachamaru** — Japan ("company: Japan"), Twitter **@vibecoder_japan**, 42 followers, 14 public repos, GitHub since 2021-12. **FIRST Japan-LOCATED subject in the v60+ window.** |
| Tier / archetype | **T1 Assistant Skill** / NEW sub-archetype "Autonomous Plan→Work→Review Operating-Loop Harness (Enforced-Gate)" (PRIMARY) |
| License | **MIT** + `LICENSE.ja.md` (Japanese-language license — corpus-notable bilingual-license artifact) |
| Languages | Shell 44.3% · **Go 31.9%** · JavaScript 13.9% · TypeScript 8.3% · Python 1.6% |
| Stars / forks | 2,125 ★ / 218 forks (fork ratio 0.103 — active deployment) |
| Subscribers / open issues | 7 / 8 |
| Created / pushed | 2025-12-12 / 2026-05-27 (~168 days) |
| Velocity | **~12.6 stars/day = sustained-low** (NOT a Pattern #52 instance; below all sub-class floors) |
| Maturity | **VERSION 4.12.11**; README cites **173 releases + 1,241 commits** = **~1 release/day cadence** (GitHub API releases endpoint returned 30 on page 1 — pagination) |
| Default branch | `main` · no topics · no homepage · ~150 MB |
| Locales | README.md (EN) + README_ja.md (Japanese) |

## 2. What it does — the Plan→Work→Review→Release loop

The harness converts ad-hoc Claude Code agent work into a **disciplined, gated operating loop**. Stated problem: *"Claude Code is powerful, but raw agent work drifts: plans live in chat, tests become optional, review happens too late, and release evidence gets rebuilt by memory."*

| Phase | Command | What it enforces |
|---|---|---|
| **Plan** | `/harness-plan` | Generates `spec.md` + `Plans.md` (scope, acceptance criteria, dependencies, unknowns, stop conditions). **User approval gates execution.** |
| **Work** | `/harness-work` | Implements *only approved* tasks; TDD + embedded verification. |
| **Review** | `/harness-review` | Independent assessment, separate from implementation. **Major findings block release.** |
| **Release** | `/harness-release` | Packages verified evidence ("Work All Evidence Pack") for PR/deploy. |
| **Sync** | `/harness-sync` | State reconciliation. |

**Source-of-truth discipline (the load-bearing idea):** specification files are the source of truth; *"Data the agent has not seen stays `unknown` instead of being silently invented."* This is a structural anti-hallucination guardrail — and it maps directly onto Storm Bear's own CLAUDE.md rules ("NEVER fabricate", "NEVER make silent assumptions").

## 3. Architecture

```
claude-code-harness/
├── .claude-plugin / .claude        ← Claude Code plugin + config
├── .codex-plugin / codex / skills-codex   ← Codex CLI surface
├── .cursor-plugin / .cursor        ← Cursor surface
├── opencode                        ← OpenCode surface
├── skills/        ← ~25 verb-skills (harness-plan/work/review/release/sync + setup/loop/accept/progress + ci/crud/deploy/auth/memory/principles/agent-browser/...)
├── agents/        ← advisor.md · reviewer.md · scaffolder.md · worker.md (4 role agents)
├── go/ + go.work  ← Go-native guardrail engine (no Node.js required)
├── bin/           ← `bin/harness doctor --migration-report` etc.
├── hooks/ + .githooks/   ← git-hook guardrail enforcement
├── monitors/      ← runtime monitors
├── benchmarks/ + scorecard.yml   ← quality gates / OpenSSF-style scorecard
├── harness.toml + config schema + example   ← config-driven
├── output-styles / docs / assets / scripts
├── CLAUDE.md · IMPLEMENTATION_GUIDE.md · Plans.md · CHANGELOG.md · SECURITY.md · VERSION
└── LICENSE.md + LICENSE.ja.md · README.md + README_ja.md
```

- **Go-native guardrail engine** (no Node.js) — substrate choice; the gates/hooks/monitors are enforced by compiled code, not prose.
- **Companion project `harness-mem`** provides optional cross-session memory (memory-system adjacency — see §5).
- **Acknowledged design-pattern sources:** "Hierarchical skill design" (AI Masao) + "Test tampering prevention patterns" (Beagle).

## 4. Distribution & multi-harness support

- **Claude Code (v2.1+)** — primary; plugin marketplace → `/plugin install` → `/harness-setup` (~30-second install).
- **Codex CLI** — internal-compatible (`scripts/setup-codex.sh --user`).
- **OpenCode** — internal-compatible (`scripts/setup-opencode.sh`).
- **Cursor / GitHub Copilot CLI / Codex app** — *candidate tiers* (adapter/handoff research only).
- = **Pattern #84 84c Provider-Agnostic-By-Design** (repo-stored 84c.1: `.claude-plugin` + `.codex-plugin` + `.cursor-plugin` + `skills` + `skills-codex`; CLI-generated 84c.2: setup scripts). Multi-harness with explicit **tier gradation** (supported vs candidate) — a corpus-notable honesty about which harnesses are first-class.

## 5. Corpus position (cross-references)

- **Methodology lineage:** [[v71 agents-best-practices]] (agentic execution-separation "model proposes, harness disposes" / L0–L4 autonomy) — v107 is the **executable, gated** realization of what v71 *described*. [[v61 cc-sdd]] (spec/plan discipline, Pattern #21). [[v78 ECC]] (multi-harness operator system).
- **NEW T1 sub-archetype (PRIMARY):** "Autonomous Plan→Work→Review Operating-Loop Harness (Enforced-Gate)" — distinct from descriptive frameworks (v71) and skill-bundles, by enforced gates + Go guardrail engine + spec-as-source-of-truth.
- **Pattern #83 NEW sub-variant candidate "Unknown-Stays-Unknown anti-invention guardrail at spec-layer"** — unknown data stays `unknown` rather than silently invented; honest-deficiency discipline made structural.
- **Pattern #84 84c Provider-Agnostic multi-harness N+1** (4-harness + candidate tiers).
- **Memory-system adjacency:** `harness-mem` companion → [[v66 agentmemory]] + [[v103 claude-mem]] (Pattern #85 Platform-Primitive Foundation, just N=2-strengthened at v106). Adjacent, not the subject itself.
- **High-development-cadence-relative-to-star-velocity** — ~1 release/day + 1,241 commits at modest 2.1K★ = Library-vocab N=2 with [[v89 VibeCodingTracker]] (high-release-cadence at micro-scale); v107 = mid-scale instance.
- **Japan-LOCATED first-instance** — extends the Asian-LOCATED cluster with a NEW sub-locale (prior Asian = Vietnam + China-Mainland + Taiwan). Pattern #19 NEW sub-mechanism candidate "Japanese-Located Solo-Dev with Vibe-Coder Identity (@vibecoder_japan)".
- **Pattern #57 57c-product citation density:** Claude Code v65 + Codex v62 + OpenCode v67 + Cursor v75/v76 = 4 corpus-subject harness citations.
- **Pattern #28 Editorial-Build-Validator adjacency** — scorecard.yml + gates + evidence-packs = deterministic quality-gate discipline (validator-family).

## 6. Honest caveats

- **NOT a Pattern #52 instance** — ~12.6 stars/day is sustained-low. The story is *high development cadence at modest stars* (a builder's tool), not virality.
- **Release count:** README says 173; GitHub API releases endpoint returned 30 (page-1 pagination). VERSION = 4.12.11. Cited the README figure; flagged the API discrepancy honestly.
- **agentskills.io conformance NOT claimed** — the verb-skill model *aligns with* the agentskills.io paradigm but the repo does not declare spec conformance, so v107 is **NOT** counted in the Pattern #57 57k standards-conformance chain (v76→…→v104). Honest non-claim.
- **(a) is cluster-extension-driven** — Japan is a new Asian sub-locale (genuinely corpus-novel) but Japanese is not Storm Bear's language; the cultural-peer signal is archetype (solo Asian dev building Claude Code agentic tooling), not direct nationality/role peer.

## Sources
- [Chachamaru127/claude-code-harness · GitHub](https://github.com/Chachamaru127/claude-code-harness)
- [@vibecoder_japan · X](https://x.com/vibecoder_japan)

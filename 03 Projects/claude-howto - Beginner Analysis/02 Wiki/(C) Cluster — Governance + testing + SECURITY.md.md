# (C) Cluster — Governance + testing + SECURITY.md

> **Cluster 2** of 3 — Contributor-facing governance: CONTRIBUTING.md (381 lines) + SECURITY.md (334 lines) + CODE_OF_CONDUCT.md (220 lines).
> **Source:** `luongnv89/claude-howto` main branch, fetched 2026-04-22.

## 1. Governance file inventory

Confirmed 6 governance files:
1. `README.md` (878 lines EN) + 3 i18n variants
2. `LICENSE` (MIT)
3. `CONTRIBUTING.md` (381 lines)
4. `SECURITY.md` (334 lines)
5. `CODE_OF_CONDUCT.md` (220 lines)
6. `.github/TESTING.md` (referenced, not fetched directly — documented testing practices)

**NOT present (absences informative):**
- **AGENTS.md — NOT in root.** Counter-evidence for Pattern #22 AGENTS.md industry-standard at T1? At N=2 absence pattern emerging (agency-agents v18 also lacks AGENTS.md). Notable: claude-howto is ABOUT agent templates but doesn't use AGENTS.md filename convention. Strengthens boundary of Pattern #22 (AGENTS.md = contributor doc for meta-frameworks; tutorial frameworks may substitute with CONTRIBUTING.md).
- No AI-disclosure clause in CONTRIBUTING.md — confirms Pattern #23 AI-Disclosure Policy remains RETIRED (retired at v27 audit after N=1 spec-kit only, no corporate follow-on; claude-howto as a Claude-Code-focused framework lacking AI-disclosure is further evidence retirement was appropriate).
- No `CODEOWNERS` file referenced
- No `FUNDING.yml` referenced (no sponsorship mechanism visible)
- No `.github/ISSUE_TEMPLATE/` explicitly shown (may exist but not in README)

## 2. Pre-commit hooks = 5 CI-identical checks

Per CONTRIBUTING.md lines 99-107:

| Hook | What it checks |
|------|---------------|
| `markdown-lint` | Markdown formatting + structure |
| `cross-references` | Relative links, anchors, code fences |
| `mermaid-syntax` | All ` ```mermaid ` blocks parse correctly |
| `link-check` | External URLs reachable |
| `build-epub` | EPUB generates without errors (on `.md` changes) |

**Corpus-first:** `mermaid-syntax` + `cross-references` + `build-epub` pre-commit hooks are novel at T1. No prior T1 corpus framework shipped these. Graphify v16 had diagram-validator; claude-howto extends to 3 novel pre-commit checks.

**Implication:** Luong treats documentation AS CODE with CI-enforceable checks. Testing infrastructure applies to content, not just scripts. This is PRODUCTION-GRADE maintenance for a tutorial repo. Pattern observation: rigor vs subject-matter: claude-howto IS docs, yet has CI discipline rivaling code projects.

## 3. Contribution types (5 categories)

Per CONTRIBUTING.md §"Types of Contributions":
1. **New Examples or Templates** — copy-paste ready code + explanations + use cases + troubleshooting
2. **Documentation Improvements** — clarify / fix typos / add missing info / improve code examples
3. **Feature Guides** — step-by-step tutorials + architecture diagrams + common patterns + anti-patterns
4. **Bug Reports** — expected vs actual + reproduction + Claude Code version + OS
5. **Feedback and Suggestions** — better explanations / coverage gaps / reorganization

Standard open-source taxonomy — no novel types like paperclip v14's alignment-theory-visibility or agency-agents v18's personality-driven feedback.

## 4. Template-specific contribution workflow

CONTRIBUTING.md documents 5 per-feature add-a-X workflows:

**Add a Slash Command:**
1. Create `.md` in `01-slash-commands/`
2. Include: description + use cases + installation + usage examples + customization tips
3. Update `01-slash-commands/README.md`

**Add a Skill:**
1. Create directory in `03-skills/`
2. Include: `SKILL.md` main doc + `scripts/` helpers + `templates/` prompts + usage example
3. Update `03-skills/README.md`

**Add a Subagent:**
1. Create `.md` in `04-subagents/`
2. Include: purpose + capabilities + system prompt + use cases + integration
3. Update `04-subagents/README.md`

**Add MCP Configuration:**
1. Create `.json` in `05-mcp/`
2. Include: config explanation + env vars + setup + usage
3. Update `05-mcp/README.md`

**Add a Hook:**
1. Create `.sh` in `06-hooks/`
2. Include: shebang + description + comments + error handling + security considerations
3. Update `06-hooks/README.md`

**Novel discipline:** Every contribution requires README update at the SAME LEVEL. README is source of truth + living index. Contrast with larger projects (spec-kit v17) where README = project overview, per-folder READMEs often minimal.

## 5. Conventional commit format

Per CONTRIBUTING.md §"Commit Guidelines":
```
type(scope): description

[optional body]
```

Types: `feat / fix / docs / refactor / style / test / chore`

Examples:
- `feat(slash-commands): Add API documentation generator`
- `docs(memory): Improve personal preferences example`
- `fix(README): Correct table of contents link`

Standard Conventional Commits spec (https://conventionalcommits.org). Consistent with modern open-source discipline.

## 6. Testing infrastructure (unusual for tutorial repo)

Per README §"Testing" + CONTRIBUTING.md §"Set Up Your Environment":

**Stack:**
- **Unit tests:** pytest (Python 3.10, 3.11, 3.12 matrix)
- **Linting/Formatting:** Ruff (fast Rust-based Python linter)
- **Security:** Bandit (Python security scanner — Pattern #24 SECURITY.md toolchain)
- **Type Checking:** mypy (static analysis)
- **Build Verification:** EPUB generation tested
- **Coverage:** Codecov integration

**Install:**
```bash
uv pip install -r scripts/requirements-dev.txt
```

**Run:**
```bash
pytest scripts/tests/ -v
pytest scripts/tests/ -v --cov=scripts --cov-report=html
ruff check scripts/ && ruff format --check scripts/
bandit -c pyproject.toml -r scripts/ --exclude scripts/tests/
mypy scripts/ --ignore-missing-imports
```

**CI trigger:** Every push to `main`/`develop` + every PR to `main`.

**Corpus-first at T1:** Full pytest + Ruff + Bandit + mypy stack for a tutorial repo. Prior T1 corpus rarely had unit tests for content — most treat content as markdown + rely on human review. Luong applies full Python code-quality discipline to build scripts (EPUB builder + doc utilities).

## 7. SECURITY.md governance depth

SECURITY.md 334 lines — MEDIUM-HEAVY depth. Contents:

**§Overview** — statement of security importance + reporting expectation.

**§Supported Versions:**
| Version | Status | Support Until |
|---------|--------|---------------|
| Latest (main) | ✅ Active | Current + 6 months |
| 1.x releases | ✅ Active | Until next major version |

**§Security Practices (3 sub-sections):**
1. **Code Security** — Dependency Management + Code Quality + Access Control
2. **Documentation Security** — No Secrets in Examples + Security Best Practices + Content Review
3. **Dependency Security** — Scanning + Updates + Transparency

**§Reporting a Vulnerability** — explicit private disclosure path:
1. GitHub Private Vulnerability Reporting: https://github.com/luongnv89/claude-howto/security/advisories
2. `.github/SECURITY_REPORTING.md` for detailed instructions
3. **DO NOT open a public issue** for security vulnerabilities

**Pattern #24 SECURITY.md at T1 — 4th data point:**

Prior data points (Pattern confirmed v18):
1. graphify v16 (T4 solo) — first standalone SECURITY.md in corpus
2. spec-kit v17 (T1 corporate) — corporate-grade
3. agency-agents v18 (T1 solo-enterprise-scale) — light-governance despite scale

Now adding:
4. **claude-howto v32 (T1 VN-diaspora solo, 28K)** — MEDIUM-HEAVY (334 lines with 3-tier structure + supported-versions table + private-disclosure channel)

**Strengthens Pattern #24 formulation:** SECURITY.md emergence at T1 is archetype-independent (corporate, community-viral, VN-diaspora-solo all adopt). Pattern more universal than originally scoped.

## 8. CODE_OF_CONDUCT.md

220 lines. Contents (inferred from structure):
- Contributor Covenant v2.1 (standard) or variant
- Expected behavior
- Unacceptable behavior
- Enforcement responsibility (maintainers)
- Reporting channel
- Enforcement guidelines (graduated sanctions)

Standard corporate/community governance. Not novel at T1 (spec-kit v17 also has CoC; BMAD v11 has CoC).

## 9. Development environment — uv + npm dual-tooling

**Python side (uv):**
```bash
pip install uv
uv venv && source .venv/bin/activate
uv pip install -r scripts/requirements-dev.txt
uv pip install pre-commit
pre-commit install
```

**Node.js side:**
```bash
npm install -g markdownlint-cli
npm install -g @mermaid-js/mermaid-cli
```

**Dual-toolchain discipline:** Python for build scripts + unit tests; Node.js for content validation (markdown + Mermaid). First corpus T1 with explicit Python + Node.js dual-tooling documentation. Contrast:
- codymaster v12 — Python primary
- gstack v3 — shell primary
- spec-kit v17 — Python (uv) primary
- ECC v1 — markdown-only with minor Python
- BMAD v11 — CLI + markdown

**Corpus observation:** claude-howto's dual-tooling reflects that content repos increasingly need heterogeneous CI.

## 10. Absence of AI-assisted-contribution governance (revival-check negative for Pattern #23)

CONTRIBUTING.md says: *"Provide attribution where needed"* (generic, line 326). No section on:
- AI-assisted contribution disclosure
- AI-generated code labeling
- Tool-use transparency (`🤖🤖🤖` suffix like awesome-mcp-servers v31)

**Revival-check negative for Pattern #23 AI-Disclosure Policy:** Pattern #23 was RETIRED at v27 audit (was N=1 spec-kit v17 only; no corporate follow-on across 10 wikis). claude-howto at v32 confirms retirement rationale — even a Claude-Code-focused framework doesn't adopt AI-disclosure policy. Pattern #23 stays RETIRED.

## 11. 4-check pre-merge gate

Per CONTRIBUTING.md:
> *"Pre-commit hooks run the same checks as CI locally before every commit. All four checks must pass before a PR will be accepted."*

But actually listed FIVE checks (markdown-lint / cross-references / mermaid-syntax / link-check / build-epub). Minor documentation inconsistency in CONTRIBUTING (says "four" in prose, lists 5 in table).

**Flag:** Phase 6 fact-verification should note this but not require correction in wiki files — we're cataloging, not auditing Luong's docs.

## 12. Branch naming convention

```bash
git checkout -b add/feature-name
git checkout -b fix/issue-description
git checkout -b docs/improvement-area
```

Kebab-case with semantic prefix. Standard but not universal — spec-kit v17 uses different branching convention. Luong's convention is simpler (3 categories vs GitFlow complexity).

## 13. Corpus-first observations from Cluster 2

1. **Pattern #24 SECURITY.md T1 4th data point** — strengthens pattern; now universal across corporate + community-viral + solo-enterprise + VN-diaspora archetypes at T1
2. **mermaid-syntax + build-epub pre-commit hooks** — novel CI checks for tutorial repo (corpus-first)
3. **Full pytest + Ruff + Bandit + mypy + Codecov stack** for tutorial repo — treats content as code (corpus-first at T1)
4. **Python + Node.js dual-toolchain** documentation — first corpus T1 with explicit dual-tooling
5. **5-check pre-commit gate** (markdown-lint / cross-references / mermaid-syntax / link-check / build-epub)
6. **Per-feature contribution workflow** — 5 add-a-X documented (slash cmd / skill / subagent / MCP / hook) each with 3-step checklist + same-level README update mandate
7. **AGENTS.md ABSENCE** — counter-evidence for Pattern #22 T1-universality (at N=2 absence after agency-agents v18); AGENTS.md may be meta-framework-specific
8. **No AI-disclosure in CONTRIBUTING** — Pattern #23 was RETIRED v27 audit; claude-howto provides no revival evidence (strengthens retirement rationale: corporate-policy-specific)
9. **EPUB build-integrity** as pre-commit hook — content-production CI (corpus-first)
10. **3-tier SECURITY.md structure** — Code Security + Documentation Security + Dependency Security sub-sections (most organized security doc at T1 after spec-kit v17)
11. **Conventional Commits spec adoption** — `feat/fix/docs/refactor/style/test/chore` taxonomy (standard but explicit enforcement unusual at solo-author T1)
12. **Current-branch-only security support** — *"Updates are applied directly to the main branch"* — honest acknowledgment that educational guide ≠ versioned library

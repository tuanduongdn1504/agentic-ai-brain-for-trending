# (C) Architecture + Release cluster summary

> Nguồn: `CLAUDE.md` (7.5 KB) + `CHANGELOG.md` (21 KB) + `AGENTS.md` (2.2 KB), fetched 2026-04-18
> Coverage: 4-layer architecture + release trajectory + agent operating rules

## TL;DR

3 smaller files combine to cover **how notebooklm-py is built, evolves, and expects agents to behave**. Architecture = clean 4-layer (CLI/Client/Core/RPC). Releases = 1-2 week cadence, v0.3.x maturity, breaking changes via deprecation warnings. Agent rules = profile isolation, `--json` outputs, explicit notebook IDs, no reliance on context files for parallel work.

---

## Part 1 — CLAUDE.md (Project Architecture)

### 4-Layer Architecture

```
CLI Layer (Click commands, per-domain modules)
   ↓
Client Layer (Main async NotebookLMClient, namespaced APIs)
   ↓
Core Layer (HTTP/RPC infrastructure, _core.py)
   ↓
RPC Layer (Method IDs, request encoding, response parsing — rpc/types.py)
```

**Separation rationale:**
- RPC layer = fragile (undocumented Google APIs), isolated
- Core layer = stable HTTP plumbing
- Client layer = pythonic async API (`client.notebooks.*`)
- CLI layer = Click commands (thin wrapper around Client)

→ **Changes to RPC don't cascade to Client/CLI.** Only `rpc/types.py` needs updating when Google changes method IDs.

### Key Modules

| Module | Purpose |
|--------|---------|
| `client.py` | Main NotebookLMClient |
| `_core.py` | HTTP/RPC infrastructure |
| `_notebooks.py` | Notebook domain API |
| `_sources.py` | Sources domain API |
| `_artifacts.py` | Artifacts (generation) domain API |
| `_chat.py` | Chat domain API |
| `rpc/types.py` | **Source of truth for RPC method IDs** (fragile) |
| `cli/` | Click command modules per domain |

### Development Workflow

**Pre-commit checks (REQUIRED):**
```
ruff format + ruff check + mypy + pytest
```

One-liner provided để run all before commit.

### Testing Strategy (3 tiers)

- **Unit tests** — Encoding/decoding, no network
- **Integration tests** — Mocked HTTP responses
- **E2E tests** — Real API, requires auth, marked `@pytest.mark.e2e`

→ **Mature testing pyramid.** Not just E2E — explicit unit + integration layers.

### Common Pitfalls

1. RPC method IDs change — monitor network traffic, update
2. Nested list structures in params — position-sensitive
3. Source ID nesting varies — `[id]` through `[[[[id]]]]`
4. CSRF tokens expire — refresh/re-auth
5. Rate limiting — delays between bulk ops required

→ **Documented gotchas.** Reduces bus-factor risk slightly by writing down tribal knowledge.

### PR Requirements

- Monitor CI status
- Address review comments
- Reply to feedback threads
- Verify all checks pass + merge status CLEAN
- "Not done until fully addressed"

### Conventions

- Namespace domain APIs under client (`client.notebooks.list()`)
- Follow CONTRIBUTING.md for naming
- Lowercase-kebab for doc filenames
- Suggest CLI for quick tasks/scripts
- Suggest Python API for application integration

---

## Part 2 — CHANGELOG.md (Release Trajectory)

### Release Cadence

**1-2 weeks per release.** Active development since January 2026 (3 months).

### Version Trajectory

| Version | Date | Highlights |
|---------|------|-----------|
| **v0.3.4** | Mar 12, 2026 | Notebook metadata export, cinematic video, infographic styles, source delete-by-title |
| **v0.3.3** | Mar 3, 2026 | Note-saving from chat, slide deck revision, PPTX downloads, conversation persistence |
| **v0.3.2** | Jan 26, 2026 | Fixed conversation reset, UTF-8 encoding, Windows Playwright compat |
| **v0.3.1** | Jan 23, 2026 | Windows CLI hangs, unicode errors, streaming download corruption, partial ID matching |
| **v0.3.0** | Jan 21, 2026 | **Major:** 80+ languages, sharing API, `SourceType`/`ArtifactType` enums, centralized exceptions |

### Breaking Changes (v0.3.0)

Deprecated properties (removed in v0.4.0):
- `Source.source_type`
- `Artifact.artifact_type`
- `Artifact.variant`
- `StudioContentType`

→ **Deprecation warnings before removal.** Semver-respectful.

### Stability Trajectory

- **v0.1.x** — beta
- **v0.2.x** — initial stabilization (Windows fixes, auth fixes)
- **v0.3.x** — production-grade (API enrichment, DX)

→ **Confidence in core.** Focus has shifted from fixing to expanding.

### RPC Fragility (explicit)

CHANGELOG openly addresses "RPC fragility as inherent limitation of undocumented Google APIs." Not hidden.

**Takeaway:** Don't pin library to critical production without fallback plan.

---

## Part 3 — AGENTS.md (Agent Operating Rules)

### Key Directives

**Isolation:**
> "Isolate runs with `NOTEBOOKLM_HOME=/tmp/<agent-id>` when multiple agents share one machine."

Prevents state/credential conflicts between concurrent agents.

**Authentication:**
> "Run `uv run pytest tests/e2e -m readonly` only after `notebooklm login` and setting test notebook env vars."

E2E tests require real auth.

**HTTP Recording (for testing):**
```bash
NOTEBOOKLM_VCR_RECORD=1 uv run pytest tests/integration/test_vcr_*.py -v
```

Generates cassettes (recorded request/response).

### Technical Conventions

- Use `--json` for programmatic consumption
- **Pass explicit notebook IDs** instead of `notebooklm use` (especially parallel agents)
- Target Python 3.10+
- 100-char line limits
- Double quotes
- 90%+ code coverage enforced

### Commit Standards

Semantic commit prefixes:
- `feat(scope):` — new feature
- `fix(scope):` — bug fix
- `refactor(scope):` — refactor
- `style:` — style-only changes

**Scopes aligned with command groups:** `cli`, `test`, `rpc`.

---

## Cross-file synthesis

### What these 3 files together tell us

1. **Library is disciplined** — pre-commit hooks, 90% coverage, semver, deprecation warnings
2. **Architecture is thoughtful** — 4 layers isolate fragile RPC from stable user-facing API
3. **Agent operation is explicitly designed** — AGENTS.md is NOT just agent-friendly, it's agent-first
4. **Maintainability is good, bus factor still 1** — documented pitfalls + tests + clean arch, but teng-lin = sole maintainer

### Signals for Storm Bear operator

**Safe to adopt for:**
- Research workflow automation
- Scrum retrospective → podcast pipeline
- Source aggregation for team briefings
- Personal research assistant via Claude Code skill

**Risky to pin in production without fallback:**
- Real-time business-critical workflows (RPC can break)
- Apps sold to end-users (quality dependent on Google RPC stability)
- Long-running unattended automation (rate limits unpredictable)

### Agent usage best practices (extracted)

1. Always `--json` for programmatic parsing
2. Always explicit `-n <notebook_id>` in parallel/background agents
3. Set `NOTEBOOKLM_PROFILE` or `NOTEBOOKLM_HOME` for isolation
4. Respect autonomy rules (confirm destructive/long-running/download/save)
5. Use SKILL.md processing time table for timeouts
6. Fallback plan for rate-limited ops (audio/video/quiz/flashcard/infographic/slide-deck)

---

## Cross-references

- Main summary: [[(C) README summary]]
- SKILL summary: [[(C) SKILL summary]]
- Related entities:
  - [[(C) Python API Architecture]] (draws from CLAUDE.md 4-layer design)
- Sibling cross-refs:
  - ECC release cadence patterns
  - goclaw's 4-tier architecture (similar separation-of-concerns principle)
  - gstack's specialist role testing strategy

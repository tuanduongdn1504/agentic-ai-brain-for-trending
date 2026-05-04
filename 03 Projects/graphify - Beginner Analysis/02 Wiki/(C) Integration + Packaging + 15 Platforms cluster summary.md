# (C) Integration + Packaging + 15 Platforms cluster summary — graphify

> **Sources:** README platform install section + pyproject.toml + release v0.4.23 notes + cross-wiki ecosystem references
> **Status:** ✅ Phase 2 source summary
> **Parent index:** [[(C) index]]

---

## 1. Why cluster

Graphify's distribution model is unusual: **a single skill installable into 15 agent platforms**. This cluster traces distribution mechanics (pyproject.toml, PyPI, install commands) + per-platform integration detail + ecosystem-level significance (OpenClaw + Hermes validation).

## 2. 15-platform install matrix

### All install targets

| # | Platform | Provider | Cross-wiki? |
|---|----------|----------|-------------|
| 1 | **Claude Code** | Anthropic | ✅ (16 wikis) |
| 2 | **Codex** | OpenAI | ✅ (multica v15, paperclip v14) |
| 3 | **OpenCode** | Community | ✅ (multica v15) |
| 4 | **Cursor** | Cursor | ✅ (many wikis) |
| 5 | **GitHub Copilot CLI** | Microsoft | — (first explicit) |
| 6 | **VS Code Copilot Chat** | Microsoft | — (first explicit) |
| 7 | **Gemini CLI** | Google | ✅ (gws v13 partial) |
| 8 | **Aider** | Community | — (first explicit) |
| 9 | **OpenClaw** | Community | ✅✅✅ (codymaster v12 + paperclip v14 + multica v15) — **4th wiki** |
| 10 | **Factory Droid** | Factory | — (first explicit) |
| 11 | **Trae (standard)** | Community | — (first explicit) |
| 12 | **Trae (CN)** | Community | — (first explicit) |
| 13 | **Hermes** | Nous Research? | ✅✅ (paperclip v14 + multica v15) — **3rd wiki** |
| 14 | **Kiro IDE/CLI** | Community | — (first explicit) |
| 15 | **Google Antigravity** | Google | — (first explicit) |

### Install command pattern

```bash
pip install graphifyy
graphify install                    # Auto-detect platforms installed
graphify claude install             # Explicit Claude Code
graphify codex install              # Explicit Codex
graphify openclaw install           # Explicit OpenClaw
# ... etc for each of 15 platforms
```

### Per-platform install behavior

Each platform has a skill-install convention:
- **Claude Code:** writes to `~/.claude/skills/graphify/`
- **Codex / others:** platform-specific skill paths

## 3. Agent-runtime standards CONFIRMED via install-surface

### Pattern #18 evolution

Pattern #18 candidate (from multica v15): "Agent Runtime Standardization — OpenClaw + Hermes emerging as de facto standards."

**Graphify v16 evidence:**
- Graphify ships **dedicated install paths** for OpenClaw + Hermes
- Not just documentation mentions — executable skill integration
- Confirms OpenClaw + Hermes as real target runtimes with real install surface

### Cross-wiki OpenClaw timeline

| Wiki | Context | Evidence level |
|------|---------|----------------|
| codymaster v12 | Listed as install platform | Documentation |
| paperclip v14 | First-class adapter — "If OpenClaw is employee, Paperclip is the company" | Architecture |
| multica v15 | Listed in 8 supported agent models | Documentation |
| **graphify v16** | Dedicated `graphify openclaw install` | **Execution** |

**Pattern #18 strengthened:** 4 wikis now → OpenClaw is **de facto standard**, not hypothesis.

### Cross-wiki Hermes timeline

| Wiki | Context | Evidence level |
|------|---------|----------------|
| paperclip v14 | Hermes adapter externalization | Architecture |
| multica v15 | Listed in 8 supported agent models | Documentation |
| **graphify v16** | Dedicated `graphify hermes install` | **Execution** |

**Pattern #18 strengthened:** 3 wikis now → Hermes is **de facto standard** (slightly behind OpenClaw).

## 4. pyproject.toml + PyPI distribution

### Package naming

- **GitHub repo:** `safishamsi/graphify`
- **PyPI package:** `graphifyy` (double-y)
- **CLI entry point:** `graphify` (single-y)

**Why the double-y?** Hypotheses:
- Typo-squat resistance on PyPI
- Namespace conflict with existing `graphify` PyPI package (possible)
- Brand distinguishing

### Python requirements

- Python 3.10+
- Key dependencies: networkx, graspologic, tree-sitter, faster-whisper, anthropic SDK, vis.js (web assets)

### Release cadence

- **169 commits on v4 branch** (April 2026)
- **v0.4.23** latest release, April 18, 2026
- Pre-1.0 status = active development + breaking changes allowed

**Corpus context:** Most frameworks are pre-1.0:
- multica v15: v0.2.6
- gws v13: v0.22.5
- BMAD v11: v6.3.0
- graphify v16: v0.4.23

## 5. Versioning strategy

### v4 branch hypothesis

Commits counted on "v4 branch" — suggests:
- Major versions have dedicated branches (v1, v2, v3, v4)
- Or: v4 = current development branch; main lags
- Or: v4 = internal iteration codename

**Without git history access, speculation only.**

**Comparison:** codymaster v12 had v5.1.0 npm / v6.0.0 website skew. Graphify's v4-branch-with-0.4.23-tag suggests similar pattern.

## 6. Homepage: penpax.ai (author product brand)

### What is penpax.ai?

- Hosted at `safishamsi.github.io/penpax.ai` (GitHub Pages)
- Author brand for safishamsi's work
- Unclear if commercial or portfolio

### Ecosystem-layer hypothesis

Like **nextlevelbuilder org** publishes goclaw + ui-ux-pro-max-skill (v15 observation) — safishamsi may publish graphify + other agent-space tools under penpax.ai brand.

**Pattern #17 (Ecosystem-Layer Organizations) candidate evidence:**
- nextlevelbuilder — publishes across projects (goclaw + ui-ux-pro-max-skill)
- safishamsi / penpax.ai — potentially publishes more (beyond graphify)
- anthropics/skills + vercel-labs/agent-skills — official skill registries

**Individual ecosystem-layer vs org ecosystem-layer** — pattern refinement candidate.

## 7. Release notes (v0.4.23, April 18, 2026)

### Inferred content (not directly fetched)

v0.4.23 released 1 day before this wiki build. Active development.

Pre-1.0 status implies:
- API may break
- Features added frequently
- Lock file / pin version for production

**Storm Bear consideration:** If piloting graphify, pin to specific version for reproducibility.

## 8. Contribution model

### 7 contributors

Graphify has 7 contributors on GitHub. Distribution:
- safishamsi (primary; likely 90%+ of commits)
- 6 others (drive-by / feature additions)

### Corpus context

Solo-primary-with-contributors pattern:
- autoresearch v10: Karpathy primary, few others
- notebooklm-py v7: teng-lin primary, solo
- **graphify v16: safishamsi primary, 7 total**

→ Solo-primary-but-open-to-contribution model. Intermediate between pure-solo and team.

## 9. 30K stars at solo = scale outlier

### Corpus comparison

Solo-maintainer star counts:
- autoresearch v10: 74K (Karpathy name brand)
- **graphify v16: 30K**
- notebooklm-py v7: ~300

**graphify 30K = 100× larger than notebooklm-py solo peer.**

### Explanatory hypotheses

1. **Product-market fit** — knowledge graphs for code is hot
2. **Karpathy halo effect** — cited Karpathy = cross-promotion
3. **Broad-install strategy** — 15 platforms = 15× addressable users
4. **Timing** — agent skills ecosystem maturing; graphify hits sweet spot
5. **Marketing polish** — penpax.ai brand + multi-language README

**Most likely:** combination of product-market fit + broad distribution + Karpathy inspiration.

## 10. Distribution strategy comparison

| Framework | Distribution | Primary install |
|-----------|--------------|-----------------|
| multica v15 | Multi-channel | Homebrew + script + desktop + self-host |
| paperclip v14 | Self-hosted | Docker + npm |
| gws v13 | 5+ channels | cargo + homebrew + asdf + docker + script |
| notebooklm-py v7 | PyPI | `pip install` |
| **graphify v16** | **PyPI + 15 platform-skills** | **pip + platform-install** |

**graphify most broad in agent-platform integration** (15 skill installs); moderate in install-channel breadth (primarily PyPI).

## 11. Platform roadmap signals

### Absent from 15 targets (notable)

- **Claude Desktop** (not CLI) — unclear if supported
- **OpenAI ChatGPT (web)** — not supported
- **Anthropic Claude (web)** — not supported
- **Perplexity** — not mentioned
- **Bard / Gemini (web)** — CLI only, not web

**Pattern:** CLI + IDE-plugin bias. Web-UI agents not targeted (architectural limitation: graphify runs locally).

### Missing integrations that could come

- **Continue.dev** (VSCode AI plugin)
- **Jupyter AI**
- **Zed editor**
- **Neovim AI plugins**

## 12. Corpus-first observations

- **Broadest agent-platform install surface** (15 targets) — graphify unique
- **First PyPI package with platform-install subcommands** (graphify install vs library-only)
- **OpenClaw + Hermes execution-level validation** (4th and 3rd wiki respectively)
- **`graphifyy` double-y naming** (unique on PyPI)
- **Single solo-maintainer + 30K stars + 7 contributors** (scale outlier for solo)

## 13. Cross-references

- [[(C) README + multi-language cluster summary]]
- [[(C) ARCHITECTURE + AGENTS + SECURITY cluster summary]]
- [[(C) 15-Platform Install + Agent-Runtime Standards Confirmed]] (entity)

# (C) Integration + Extensions + Packaging cluster summary — spec-kit

> **Sources:** README agent integrations section + extension mechanism + pyproject.toml + Community Extensions catalog
> **Status:** ✅ Phase 2 source summary
> **Parent index:** [[(C) index]]

---

## 1. Why cluster

spec-kit's distribution is **3-layered**: (1) PyPI via uv, (2) 30+ agent-platform integrations, (3) 80+ community extensions. Together they form the largest agent-skill ecosystem in Storm Bear corpus.

## 2. 30+ AI agent integrations

### Named in README (14 of 30+)

1. **Claude Code** (Anthropic)
2. **Gemini CLI** (Google)
3. **Cursor CLI** (Cursor)
4. **Qwen CLI** (Alibaba)
5. **opencode** (community — note: same project as OpenCode?)
6. **Codex CLI** (OpenAI)
7. **Qoder CLI** (community)
8. **Tabnine CLI** (Tabnine)
9. **Kiro CLI** (community)
10. **Pi** (Inflection AI)
11. **Forge** (community)
12. **Goose** (Block/Square — Block Inc. AI tool)
13. **Mistral Vibe** (Mistral AI)
14. **GitHub Copilot** (GitHub/Microsoft)

Full list: https://github.github.io/spec-kit/reference/integrations.html

### Notable NOT in list (compared to multica v15 / paperclip v14 / graphify v16)

- ❌ **OpenClaw** — community-platform standard, not in spec-kit
- ❌ **Hermes** — community-platform standard, not in spec-kit
- ❌ **Aider** — listed in graphify v16 but not confirmed in spec-kit 14-of-30+
- ❌ **Cursor (IDE)** — only Cursor CLI (different product)

### Pattern #18 (Agent Runtime Standardization) TEST at v17

**Prior evidence (v15-v16):**
- OpenClaw in 4 wikis (codymaster + paperclip + multica + graphify)
- Hermes in 3 wikis (paperclip + multica + graphify)

**v17 result:**
- spec-kit (corporate-official, T1, largest integration list) does **NOT** adopt OpenClaw/Hermes
- Corporate-official framework uses different agent ecosystem subset

**Pattern #18 refinement:** 

> "Agent runtime standardization is **community-platform-specific** phenomenon. Corporate-official frameworks select agents from commercial + community-popular list, avoiding emerging community standards that haven't achieved commercial adoption."

**Prediction:** Future corporate T1 frameworks will follow spec-kit pattern (mainstream commercial + popular community, skip emerging standards). Future community T5/T2 frameworks will adopt OpenClaw + Hermes.

### Integration architecture (from AGENTS.md)

```
src/specify_cli/integrations/<agent-key>/
  ├── __init__.py
  ├── integration.py      (extends base class)
  ├── templates/          (agent-specific templates)
  └── metadata.toml       (agent config)
```

Registered in `INTEGRATION_REGISTRY` via decorator pattern.

### Base class hierarchy

```
IntegrationBase (fully custom)
├── MarkdownIntegration   (most CLI agents)
├── TomlIntegration       (TOML config)
├── YamlIntegration       (YAML config)
└── SkillsIntegration     (Claude Code-style skills)
```

## 3. 80+ community extensions marketplace

### Browse + install

```bash
specify extension search
specify extension add <extension-name>
```

### Community catalog

**URL:** https://speckit-community.github.io/extensions/

**Scale:** 80+ extensions at v17 time (per README).

### Extension categories (5)

1. **docs** — documentation generation / updates
2. **code** — code generation / transformation
3. **process** — workflow orchestration
4. **integration** — connect to external services (Jira, GitHub, etc.)
5. **visibility** — dashboards, reporting, observability

### Extension effect classification (2)

- **Read-only** — queries, analysis, reports (no mutations)
- **Read+Write** — modifies code, files, external systems

### Example extensions (from README context)

- **Jira sync** (integration category, Read+Write)
- **Security review** (code + visibility, Read-only)
- **QA testing** (process + code, Read+Write)

### Governance disclaimer (verbatim)

> "Community extensions are independently created and maintained by their respective authors. GitHub and the Spec Kit maintainers may review pull requests that add entries to the community catalog for formatting, catalog structure, or policy compliance, but they do **not review, audit, endorse, or support the extension code itself**."

### Corpus significance

**80+ extensions = largest agent-skill marketplace in corpus.**

Prior marketplace patterns:
- BMAD v6.3: community module browser — **emerging** (few modules)
- graphify v16: N/A (single tool, no extensions)
- spec-kit v17: **operational at scale** (80+)

**Pattern #7 (Marketplace Emergence) reinforced:** marketplace matures at corporate-official scale.

**Prediction:** BMAD v6.3's emerging marketplace will mature to spec-kit-scale if BMAD sustains. Other T1 frameworks will add marketplaces as they scale.

## 4. Packaging — uv tool install (corpus-first)

### uv ecosystem

- **uv** = modern Python packaging tool by Astral (replaces pip + pipx + virtualenv)
- Written in Rust, 10-100× faster than pip
- Monthly release cadence, bleeding-edge

### spec-kit install commands

```bash
# Persistent
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git@vX.Y.Z

# One-time
uvx --from git+https://github.com/github/spec-kit.git@vX.Y.Z specify init <NAME>

# Upgrade
uv tool install specify-cli --force --from git+https://github.com/github/spec-kit.git@vX.Y.Z
```

### Corpus corpus novelty

**First framework using `uv tool install` in corpus.**

Prior Python frameworks:
- graphify v16: `pip install graphifyy`
- notebooklm-py v7: `pip install`
- deer-flow v9: pip + Docker

**Implication:** GitHub-official endorsement of uv = likely drives broader Python ecosystem adoption.

### `specify-cli` package name

- **Package:** `specify-cli`
- **CLI entry:** `specify`
- **Unified command:** `specify` + subcommands (version, init, extension search/add, etc.)

## 5. Git-integrated workflow

### `specify init` creates project structure

```
<project>/
├── .specify/
│   ├── constitution.md
│   ├── specs/
│   │   └── 001-feature/
│   │       ├── spec.md
│   │       ├── plan.md
│   │       └── tasks.md
│   └── templates/
├── memory/
│   └── constitution.md
└── (project code)
```

### `/speckit.specify` creates git branch

Each spec gets a git branch automatically:
- Branch naming: `001-feature-name`
- Feature numbering: sequential
- Branch tracking: per-spec work in isolation

**Git-native workflow** — spec-kit embeds git conventions.

## 6. Distribution summary

### 3-layer distribution

| Layer | Mechanism | Scale |
|-------|-----------|-------|
| 1. Core | `uv tool install specify-cli` | 1 binary |
| 2. Agent integrations | `src/.../integrations/` + registry | 30+ agents |
| 3. Extensions | `specify extension add ...` | 80+ community |

### Total surface

30+ × 80+ = up to ~2400 combinations (if every extension worked with every agent).

**Implication:** spec-kit is **largest agent-skill combinatorial surface** in corpus.

## 7. Corporate resources enabling scale

### Signals

- **GitHub organization repo** — visibility + SEO
- **Pinned on github.com/github** — likely promoted
- **Official GitHub Pages homepage**
- **Full corporate governance** (6 files)
- **AI-disclosure policy** — corporate-managed
- **Community extension catalog hosted at speckit-community.github.io**

### Corpus comparison

| Framework | Stars | Scale enabled by |
|-----------|-------|-------------------|
| spec-kit v17 | **89.2K** | **GitHub corporate + SDD thesis + organic promotion** |
| BMAD v11 | 45K | LLC formalization + scale-domain-adaptive framing |
| graphify v16 | 30K | Solo-broad + multi-platform + Karpathy halo |
| multica v15 | 16.2K | Linear-analog + broad surface + hybrid arch |

## 8. Extension catalog analysis (inferred)

### Category distribution (hypothesis, not confirmed)

If ~80 extensions:
- **docs:** ~15 extensions (auto-README, doc-sync, etc.)
- **code:** ~25 extensions (generators, refactors, etc.)
- **process:** ~15 extensions (workflow, CI, etc.)
- **integration:** ~20 extensions (Jira, Slack, Notion, etc.)
- **visibility:** ~5 extensions (dashboards, reports)

### Read-only vs Read+Write

- **Read-only:** safer, low-barrier (analysis, search, reports)
- **Read+Write:** higher-value, more caution (code gen, external mutations)

Likely 60/40 split read-only to read+write (guess).

## 9. Edges + failure modes

### Integration edges

- **Platform drift** — 30+ agents = 30+ maintenance burdens
- **Base class mis-selection** — re-architecture cost
- **Registry conflicts** — `key` collision if two agents have same CLI name

### Extension edges

- **Unaudited code** — "GitHub does not audit" → security risk
- **Stale extensions** — authors abandon but catalog retains
- **Version fragility** — extensions may break on spec-kit updates
- **Licensing inconsistency** — community authors license however they want

### Packaging edges

- **uv version requirement** — users without uv installed need extra step
- **`uv tool install` path** — may not be on PATH by default
- **Git+SSH vs HTTPS** — private forks may not install

## 10. Cross-references

- [[(C) README + spec-driven cluster summary]] — methodology
- [[(C) AGENTS + CONTRIBUTING + SECURITY + SUPPORT + DEVELOPMENT + COC cluster summary]] — governance
- [[(C) 30+ Platform Integration + 80+ Community Extensions Marketplace]] (entity)
- [[(C) GitHub-Official Corporate Backing + T1 Corporate-vs-Community Bifurcation]] (entity)

## 11. Open questions

- Q1: Full 30+ agent list beyond 14 named?
- Q2: Full 80+ extension list?
- Q3: Extension install security model (sandboxing?)
- Q4: Extension deprecation process?
- Q6: Why uv vs pip? (performance? official Microsoft endorsement?)
- Q26: GitHub features integration (Issues, PRs, Projects)?
- Q27: VS Code extension existence?

## 12. Corpus-first observations

- **Broadest integration surface (30+)** — corpus new max
- **Largest extension marketplace (80+)** — corpus new max
- **First uv tool install**
- **First extension-governance disclaimer at scale**
- **First 3-layer distribution** (core + integrations + extensions)
- **Corporate resources enable 89.2K stars** (4× nearest community T1)

## 13. Decision log

- **v0.1-0.5:** likely initial SDD methodology + Claude Code
- **v0.6:** expanding to 10+ integrations
- **v0.7.x current:** 30+ integrations + 80+ extensions + uv packaging
- **Future:** likely more integrations, marketplace curation, possibly Copilot-deep integration

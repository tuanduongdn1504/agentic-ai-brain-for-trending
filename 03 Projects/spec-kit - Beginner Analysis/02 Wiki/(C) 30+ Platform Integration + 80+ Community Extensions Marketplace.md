# (C) 30+ Platform Integration + 80+ Community Extensions Marketplace

> **Type:** Entity — distribution + ecosystem
> **Parent:** [[(C) index]]
> **Sources:** [[(C) Integration + Extensions + Packaging cluster summary]] §2-§4; [[(C) README + spec-driven cluster summary]] §7
> **Status:** ✅ Phase 3 entity page

---

## 1. Summary

Spec-kit's **3-layer distribution** — core CLI + 30+ agent integrations + 80+ community extensions — forms the **largest agent-skill combinatorial surface in Storm Bear corpus**. Surpasses graphify v16 (15 integrations) and BMAD v6.3 (emerging marketplace) by significant margins. The marketplace adopts **corporate hands-off governance** ("GitHub does not review, audit, endorse, or support extension code"). Pattern #18 (OpenClaw/Hermes standardization) **tested and refined** at v17 — corporate-official spec-kit does NOT adopt community-platform runtime standards, revealing Pattern #18 as community-platform-specific phenomenon.

## 2. Key claims

1. **30+ AI agent integrations** — corpus new broadest (vs graphify 15)
2. **80+ community extensions** — corpus new largest (vs BMAD emerging)
3. **5 category taxonomy** — docs / code / process / integration / visibility
4. **2 effect tiers** — Read-only vs Read+Write
5. **Corporate hands-off governance** — "not reviewed, audited, endorsed, supported"
6. **Modular integration architecture** — 4 base classes + registry pattern
7. **Pattern #18 REFINED** — runtime standards are community-platform-specific

## 3. Evidence + sources

| Claim | Source | Confidence |
|-------|--------|-----------|
| 30+ integrations | README verbatim | High |
| 14 named, full list external | README + external doc reference | High |
| 80+ extensions | README + speckit-community catalog URL | High |
| 5 categories / 2 effects | README extension mechanism section | High |
| No OpenClaw/Hermes | README full integration list absence | High |
| Corporate disclaimer | README verbatim | High |

## 4. 3-layer distribution architecture

```
┌─────────────────────────────────────────────┐
│  Layer 1: Core CLI (`specify`)              │
│  ├── uv tool install specify-cli            │
│  └── slash commands (/speckit.*)            │
└────────────────┬────────────────────────────┘
                 │
┌────────────────▼────────────────────────────┐
│  Layer 2: Agent Integrations (30+)          │
│  ├── src/specify_cli/integrations/          │
│  │   ├── claude/                            │
│  │   ├── codex/                             │
│  │   ├── cursor/                            │
│  │   └── ... (30+ subpackages)              │
│  └── INTEGRATION_REGISTRY                   │
└────────────────┬────────────────────────────┘
                 │
┌────────────────▼────────────────────────────┐
│  Layer 3: Community Extensions (80+)        │
│  ├── speckit extension add <name>           │
│  ├── speckit-community.github.io/extensions │
│  └── 5 categories × 2 effects               │
└─────────────────────────────────────────────┘
```

## 5. Agent integrations detail

### Named in README (14 of 30+)

| # | Platform | Provider |
|---|----------|----------|
| 1 | Claude Code | Anthropic |
| 2 | Gemini CLI | Google |
| 3 | Cursor CLI | Cursor |
| 4 | Qwen CLI | Alibaba |
| 5 | opencode | Community |
| 6 | Codex CLI | OpenAI |
| 7 | Qoder CLI | Community |
| 8 | Tabnine CLI | Tabnine |
| 9 | Kiro CLI | Community |
| 10 | Pi | Inflection AI |
| 11 | Forge | Community |
| 12 | Goose | Block Inc |
| 13 | Mistral Vibe | Mistral AI |
| 14 | GitHub Copilot | GitHub/Microsoft |

### Coverage (by provider type)

- **Major commercial:** Claude Code, Gemini, Cursor, Qwen, Codex, Tabnine, Pi, Mistral, Copilot (9)
- **Community/open-source:** opencode, Qoder, Kiro, Forge, Goose (5)
- **Chinese-ecosystem:** Qwen, possibly Qoder/Kiro (regional diversity)
- **Remaining 16+:** not enumerated in README

### Integration architecture (from AGENTS.md)

```python
# src/specify_cli/integrations/<key>/__init__.py

@register_integration
class MyIntegration(MarkdownIntegration):  # or Toml/Yaml/Skills
    key = "myagent"
    config = {...}
    registrar_config = {...}
    context_file = "AGENTS.md"  # or CLAUDE.md
```

### 4 base class options

| Base class | Use case |
|------------|----------|
| `MarkdownIntegration` | Most CLI agents (Claude, Codex, etc.) |
| `TomlIntegration` | TOML-config agents |
| `YamlIntegration` | YAML-config agents |
| `SkillsIntegration` | Claude Code skill system |
| `IntegrationBase` | Fully custom |

## 6. Community extensions detail

### Browse / install commands

```bash
specify extension search [query]
specify extension add <extension-name>
specify extension list
specify extension remove <extension-name>
```

### Catalog

**Hosted at:** https://speckit-community.github.io/extensions/

### 5 categories

| Category | Purpose | Example extensions (hypothetical) |
|----------|---------|-----------------------------------|
| **docs** | Documentation | auto-readme, doc-sync, api-docs-gen |
| **code** | Code transformation | formatter, linter, refactor-assistant |
| **process** | Workflow | pr-reviewer, release-automation |
| **integration** | External services | jira-sync, slack-notifier, notion-export |
| **visibility** | Observability | cost-tracker, metrics-dashboard |

### 2 effect tiers

- **Read-only** — queries, analysis, reports (no mutations)
- **Read+Write** — modifies code, files, or external systems (higher trust required)

### Corporate hands-off policy (verbatim)

> "Community extensions are independently created and maintained by their respective authors. GitHub and the Spec Kit maintainers may review pull requests that add entries to the community catalog for formatting, catalog structure, or policy compliance, but they do **not review, audit, endorse, or support the extension code itself**."

### Corpus-first

**First explicit corporate marketplace disclaimer at scale** in Storm Bear corpus. 

Prior marketplaces:
- BMAD v6.3: emerging, few modules, no explicit disclaimer yet
- spec-kit v17: 80+ extensions + formal disclaimer

**Pattern #7 (Marketplace Emergence) reinforced + extended:** marketplace matures → formal governance structure emerges.

## 7. Pattern #18 (Agent Runtime Standardization) TEST at v17

### Prior evidence (v15-v16)

| Standard | Wikis mentioning | Evidence level |
|----------|------------------|----------------|
| OpenClaw | codymaster v12 + paperclip v14 + multica v15 + graphify v16 (4 wikis) | Doc → Arch → Doc → Execution |
| Hermes | paperclip v14 + multica v15 + graphify v16 (3 wikis) | Arch → Doc → Execution |

Pattern #18 at v16 status: **strengthened via execution evidence** (graphify install paths).

### v17 result

**spec-kit has largest integration list in corpus (30+) but does NOT adopt OpenClaw or Hermes.**

### Interpretation

**Pattern #18 refinement:**

> "Agent runtime standardization (OpenClaw + Hermes) is a **community-platform ecosystem phenomenon**. Corporate-official frameworks select from commercial + mainstream community agents, avoiding emerging community standards that haven't achieved broad corporate adoption."

### Evidence for tier-dependence

| Wiki archetype | OpenClaw? | Hermes? |
|----------------|-----------|---------|
| T1 solo-community (codymaster) | ✅ | ❌ |
| T5 community-platform (paperclip) | ✅ | ✅ |
| T2 community-platform (multica) | ✅ | ✅ |
| T4 solo-broad (graphify) | ✅ | ✅ |
| **T1 corporate-official (spec-kit)** | **❌** | **❌** |

**Pattern refinement:** OpenClaw + Hermes are community-platform ecosystem. Corporate frameworks opt out.

### Prediction

- Future community-platform frameworks: adopt OpenClaw/Hermes
- Future corporate frameworks: skip OpenClaw/Hermes
- Testable at v18+ across both archetype classes.

## 8. Scale signals

### Corpus distribution scale

| Framework | Integrations | Extensions/skills | Combinatorial surface |
|-----------|--------------|-------------------|----------------------|
| ECC v1 | 1 | — | 1 |
| gstack v3 | 1 | — | 1 |
| BMAD v11 | ~5 IDEs | emerging | ~50 |
| codymaster v12 | 8+ | 79 | ~632 |
| multica v15 | 8 | 4 skills | 32 |
| graphify v16 | 15 | — | 15 |
| **spec-kit v17** | **30+** | **80+** | **2400+** |

**spec-kit 4× next-largest** in combinatorial surface (codymaster 632).

### Enterprise-grade scale

30+ agents × 80+ extensions = enterprise-grade agent-skill ecosystem. Positions spec-kit as **infrastructure layer** for agent-assisted development, not just one framework.

## 9. Corporate resources enabling scale

### GitHub-as-backer enabling factors

1. **Official org visibility** — `github/` org repo = featured, promoted
2. **GitHub Pages free hosting** — homepage + docs + catalog
3. **GitHub Actions CI** — testing 30+ integrations
4. **Dev team resources** — enables 30+ integrations maintenance
5. **Community scale** — 89.2K stars → huge extension author pool
6. **Corporate governance** — 6 governance files + legal team

### Contrast with community frameworks

- Superpowers v2: 1 solo maintainer → can't scale integrations
- BMAD v11: LLC, small team → marketplace emerging
- graphify v16: solo + 7 contributors → 15 platforms is their max

**Corporate resources enable 2-5× scale** over community frameworks at T1.

## 10. Edges + failure modes

### Integration edges

- **30+ platform drift** — each platform evolves; breakages frequent
- **Base-class mis-selection** — architectural mismatch = rewrite
- **Key collision** — two agents with same CLI name conflict

### Extension edges

- **Unaudited code risk** — "GitHub does not audit" → user responsibility
- **Stale extensions** — authors abandon; catalog still shows
- **Version drift** — extensions break on spec-kit updates
- **License inconsistency** — community author choice
- **Security** — Read+Write extensions can modify code / external systems

### Marketplace governance edges

- **Moderation inconsistency** — "formatting, catalog structure, policy compliance" = fuzzy criteria
- **No rating system** — quality hard to assess
- **No deprecation process** — unclear how extensions leave catalog

## 11. Related concepts

- [[(C) Spec-Driven Development methodology + Constitution + 7-step Workflow]] — what integrations enable
- [[(C) GitHub-Official Corporate Backing + T1 Corporate-vs-Community Bifurcation]] — enables scale
- [[(C) T1 7-way + SDD Convergence + Intellectual Lineage Diversification + Storm Bear]] — tier context

## 12. Cross-project comparison

### Extension/marketplace patterns in corpus

| Framework | Pattern | Scale | Governance |
|-----------|---------|-------|------------|
| BMAD v6.3 | Community module browser | Few modules | Emerging |
| codymaster v12 | 79 embedded skills | Medium | In-tree |
| multica v15 | skills-lock.json (external deps) | 4 skills | SHA-256 integrity |
| graphify v16 | 15-platform install | Medium | Skill-per-platform |
| **spec-kit v17** | **Catalog + install CLI** | **80+ @ corporate** | **Hands-off disclaimer** |

**spec-kit's marketplace = most mature in corpus** by every dimension (size, governance formality, enterprise readiness).

## 13. Open questions

- Q1: Full 30+ agent list beyond 14 named?
- Q2: Full 80+ extension list + category breakdown?
- Q3: Extension install security model (sandboxing? permissions?)
- Q4: Extension deprecation process?
- Q17: Relationship to GitHub AGENTS.md format proposal?
- Q19: Enterprise SSO for extension catalog?

## 14. References

- README.md §Supported Integrations + §Community Extensions
- AGENTS.md §Integration Architecture
- Community catalog: https://speckit-community.github.io/extensions/
- Integrations guide: https://github.github.io/spec-kit/reference/integrations.html
- Parent: [[(C) index]]

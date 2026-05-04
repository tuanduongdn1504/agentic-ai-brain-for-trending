# (C) 11-Platform Install + OpenClaw 5th Wiki Validation

> **Type:** Entity — distribution + Pattern #18 reinforcement
> **Parent:** [[(C) index]]
> **Sources:** [[(C) README + CONTRIBUTING + zh-CN cluster summary]] §7-§8, cross-wiki OpenClaw timelines
> **Status:** ✅ Phase 3 entity page

---

## 1. Summary

agency-agents ships **11 platform installations** via `convert.sh` + `install.sh` shell scripts, making it the **5th Storm Bear corpus wiki to mention OpenClaw** (after codymaster v12 + paperclip v14 + multica v15 + graphify v16). This is the **2nd wiki with execution-level OpenClaw install paths** (after graphify v16). The v17 Pattern #18 refinement (runtime standards are community-platform-specific) is **validated** — agency-agents is solo/community style, and includes OpenClaw, whereas corporate spec-kit v17 (30+ integrations) explicitly excluded OpenClaw. Hermes absent from agency-agents — partial Pattern #18 (OpenClaw more universal than Hermes within community-platform archetype).

## 2. Key claims

1. **11 platform installations** — targeted subset vs spec-kit 30+, graphify 15
2. **OpenClaw 5th wiki mention** — Pattern #18 strengthened
3. **2nd execution-level OpenClaw install** — after graphify v16
4. **Pattern #18 v17 refinement validated** — community-platform includes OpenClaw, corporate excludes
5. **Hermes absent** — partial Pattern #18 (only 3 wikis now include Hermes, all have OpenClaw too)
6. **Shell-based conversion pipeline** — parallels gstack v3

## 3. Evidence + sources

| Claim | Source | Confidence |
|-------|--------|-----------|
| 11 platforms | README verbatim | High |
| OpenClaw included | README platform list | High |
| Hermes absent | README platform list negative | High |
| 5 wikis mention OpenClaw | Storm Bear corpus retrospective | High |
| Execution-level install | `install.sh --tool openclaw` inferred | Medium (not directly verified) |

## 4. 11-platform install matrix

### Supported platforms

| # | Platform | Provider | In corpus? |
|---|----------|----------|------------|
| 1 | **Claude Code** | Anthropic | ✅ (17 wikis) |
| 2 | **GitHub Copilot** | Microsoft | ✅ (spec-kit + graphify) |
| 3 | **Antigravity** | Google | ✅ (spec-kit) |
| 4 | **Gemini CLI** | Google | ✅ (many) |
| 5 | **OpenCode** | Community | ✅ (many) |
| 6 | **OpenClaw** | Community | ✅ (5th wiki now) |
| 7 | **Cursor** | Cursor | ✅ (many) |
| 8 | **Aider** | Community | ✅ (graphify + spec-kit) |
| 9 | **Windsurf** | Codeium | **First corpus mention** |
| 10 | **Qwen Code** | Alibaba | ✅ (spec-kit) |
| 11 | **Kimi Code** | Moonshot | **First corpus mention** |

### Platform comparison vs other wikis

| Platform | spec-kit v17 | graphify v16 | agency-agents v18 |
|----------|--------------|--------------|-------------------|
| Total count | 30+ | 15 | 11 |
| Claude Code | ✅ | ✅ | ✅ |
| Codex | ✅ | ✅ | ❌ |
| Cursor | ✅ | ✅ | ✅ |
| Copilot | ✅ | ✅ | ✅ |
| Gemini CLI | ✅ | ✅ | ✅ |
| Antigravity | ✅ | ❌ | ✅ |
| OpenCode | ✅ | ✅ | ✅ |
| Aider | ❌ | ✅ | ✅ |
| OpenClaw | **❌** | ✅ | ✅ |
| Hermes | ❌ | ✅ | ❌ |
| Windsurf | ❌ | ❌ | ✅ |
| Kimi Code | ❌ | ❌ | ✅ |
| Qwen | ✅ | ❌ | ✅ |
| Kiro | ✅ | ✅ | ❌ |

### Novel entries at v18

- **Windsurf** (Codeium) — first corpus platform
- **Kimi Code** (Moonshot AI, Chinese) — first corpus platform

agency-agents reaches Chinese-ecosystem platforms (Qwen, Kimi) + niche Western (Windsurf).

## 5. Pattern #18 evolution at v18 — full timeline

### OpenClaw corpus timeline

| Wiki | Version | Evidence level | Context |
|------|---------|----------------|---------|
| codymaster | v12 | 📄 Doc | Listed as install platform |
| paperclip | v14 | 🏗️ Architecture | First-class adapter metaphor |
| multica | v15 | 📄 Doc | 1 of 8 supported agent models |
| graphify | v16 | 🛠️ Execution | Dedicated `graphify openclaw install` |
| **agency-agents** | **v18** | **🛠️ Execution** | **install.sh supports openclaw target** |

**5 wikis now mention OpenClaw.** **2 with execution-level install.** Pattern #18 = **de facto runtime standard** in community-platform archetype.

### Hermes corpus timeline

| Wiki | Version | Evidence level |
|------|---------|----------------|
| paperclip | v14 | 🏗️ Architecture |
| multica | v15 | 📄 Doc |
| graphify | v16 | 🛠️ Execution |
| **agency-agents** | **v18** | **❌ (absent)** |

**3 wikis include Hermes (down from appearing in 3 of 4 prior community-platform wikis).**

### Pattern #18 sub-finding

**OpenClaw adoption rate > Hermes adoption rate** within community-platform archetype:
- OpenClaw: 5 of 5 community-platform wikis (100%)
- Hermes: 3 of 5 community-platform wikis (60%)

**Interpretation:** OpenClaw is more mature / widely-supported standard. Hermes is second-tier.

### Pattern #18 v17 refinement VALIDATED

**v17 refinement claim:**
> "Agent runtime standardization is community-platform-specific. Corporate-official frameworks avoid emerging community standards."

**v18 evidence:**
- agency-agents (solo-community archetype) → includes OpenClaw ✅
- spec-kit v17 (corporate) → excludes OpenClaw ✅
- Pattern holds at 5-wiki / 1-contrast evidence level

## 6. Shell-based conversion architecture

### convert.sh pipeline

```
Master .md agent files (repo)
           ↓
        convert.sh
           ↓
  ┌───────┴───────┬──────────┬────────┐
  ↓               ↓          ↓        ↓
Cursor         Claude      Kimi    ...11 platforms
(.mdc)          (.md)      (YAML)   (various)
```

### Parallel execution

```bash
# Auto-detect CPU count
CPU_COUNT=$(nproc 2>/dev/null || sysctl -n hw.ncpu 2>/dev/null || echo 4)

./scripts/convert.sh --parallel --jobs $CPU_COUNT
```

### install.sh flags

```bash
# Interactive (default)
./scripts/install.sh
./scripts/install.sh --interactive --parallel

# Targeted
./scripts/install.sh --tool claude-code
./scripts/install.sh --tool cursor
./scripts/install.sh --tool opencode
./scripts/install.sh --tool openclaw   # ← OpenClaw execution evidence

# Batch
./scripts/install.sh --no-interactive --tool all
./scripts/install.sh --no-interactive --parallel --jobs 4
```

## 7. Shell-first philosophy — Pattern convergence

### agency-agents v18 + gstack v3 — only shell-primary T1 frameworks

| Framework | Lang | Install | Use case |
|-----------|------|---------|----------|
| gstack v3 | shell 100% | `curl | bash` | YC virtual eng team |
| **agency-agents v18** | **shell 96.8%** | `./scripts/install.sh` | **AI agency 144 agents** |

### Advantages

- No Python / Node / uv dependency
- Universal Unix compatibility
- Low-friction install
- Script-literate users comfortable

### Disadvantages

- Windows users need WSL
- Less sophisticated dependency management
- No package-manager versioning

### Pattern candidate #26 — Shell-first T1

Two data points isn't enough but trend observable:
- Shell-first = 2 T1 frameworks
- Package-manager (npm/pip/uv) = 6 T1 frameworks

**Minority pattern** at T1. Watch v19+ for more shell-first entrants.

## 8. Distribution surface comparison

### 3-way distribution

| Framework | Platforms | Extensions | Combinatorial |
|-----------|-----------|------------|---------------|
| spec-kit v17 | 30+ | 80+ | ~2400 |
| graphify v16 | 15 | — | 15 |
| **agency-agents v18** | **11** | **144 built-in agents** | **1584** |

### Agency-agents combinatorial = 1584

**11 platforms × 144 agents** = 1584 installable agent-platform combinations.

**Practical meaning:** any of 144 agents runs on any of 11 platforms = broadest agent-library-platform matrix in corpus.

## 9. Corporate resources asymmetry

### spec-kit (corporate) vs agency-agents (solo)

| Aspect | spec-kit v17 | agency-agents v18 |
|--------|--------------|-------------------|
| Stars | 89.2K | 82.9K |
| Author | GitHub corporate | msitarzewski solo |
| Platforms | 30+ | 11 |
| Marketplace | 80+ extensions | 144 built-in |
| Governance files | 6 | 5 |
| Release cadence | v0.7.3 tagged | No releases |

**Scale ≈ 90% of corporate-T1, but built by solo.**

**Implication:** community + personality-driven design can approach corporate-resource-enabled frameworks in reach.

## 10. Edges + failure modes

### Platform coverage edges

- **No Codex, Kiro** — spec-kit has these, agency-agents doesn't
- **Windsurf / Kimi Code first-corpus** — less documented adjacency
- **Platform evolution** — 11 platforms × ongoing format drift

### OpenClaw adoption edges

- **5 wikis now commit to OpenClaw** — if OpenClaw forks or deprecates, cross-wiki impact
- **Hermes partial** — inconsistent community-platform stance
- **No OpenClaw governance** documented in any wiki

### Shell-first edges

- **Windows friction** — WSL required
- **Script injection risk** — `install.sh` runs arbitrarily
- **Dependency assumption** — `nproc` / `sysctl` availability

## 11. Related concepts

- [[(C) 144 Agent Personalities + 12 Divisions Taxonomy]] — what gets distributed
- [[(C) Solo-at-Enterprise-Scale + Reddit Community Origin + Pattern 20 Revision]] — organizational meta
- [[(C) T1 8-way + Agent Persona Library + Pattern 19 No-Lineage + Storm Bear]] — tier meta

## 12. Cross-project comparison

### Platform adoption strategy

| Framework | Strategy |
|-----------|----------|
| spec-kit | Mainstream + popular community (30+) |
| graphify | Broad community-platform (15 w/ OpenClaw + Hermes) |
| **agency-agents** | **Selective community-platform (11 w/ OpenClaw, no Hermes)** |

Different distribution strategies reflect different archetype positioning.

## 13. References

- README 11-platform list
- Cross-wiki OpenClaw mentions: codymaster v12 + paperclip v14 + multica v15 + graphify v16 + agency-agents v18
- Pattern #18 history: root `GOALS.md` version log
- Parent: [[(C) index]]

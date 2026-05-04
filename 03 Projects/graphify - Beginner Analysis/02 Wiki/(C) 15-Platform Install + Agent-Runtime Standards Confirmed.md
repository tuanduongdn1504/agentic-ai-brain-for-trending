# (C) 15-Platform Install + Agent-Runtime Standards Confirmed

> **Type:** Entity — distribution + cross-wiki ecosystem signal
> **Parent:** [[(C) index]]
> **Sources:** [[(C) Integration + Packaging + 15 Platforms cluster summary]] §2-§3, cross-wiki OpenClaw/Hermes timelines
> **Status:** ✅ Phase 3 entity page

---

## 1. Summary

Graphify ships **15 dedicated skill-install paths** — the **broadest agent-platform integration surface** in Storm Bear corpus. This includes explicit install paths for **OpenClaw** (now confirmed in 4 wikis) and **Hermes** (now confirmed in 3 wikis) — upgrading these from "mentioned in docs" to "execution-level target runtimes." Pattern #18 (Agent Runtime Standardization) is **strengthened from candidate to supported hypothesis** at v16.

## 2. Key claims

1. **15 platforms supported** — broadest in corpus
2. **OpenClaw install path** — 4th wiki mentioning OpenClaw; first with dedicated CLI install
3. **Hermes install path** — 3rd wiki; first with dedicated CLI install
4. **Pattern #18 strengthened** — execution evidence > documentation evidence
5. **Universal skill distribution model** — skill-per-platform, single codebase
6. **CLI + IDE-plugin bias** — no web-UI targets (architectural constraint)

## 3. Evidence + sources

| Claim | Source | Confidence |
|-------|--------|-----------|
| 15 platforms | README platform install section | High |
| OpenClaw dedicated install | README + command reference | High |
| Hermes dedicated install | README + command reference | High |
| OpenClaw 4th wiki | codymaster v12 + paperclip v14 + multica v15 + graphify v16 | High |
| Hermes 3rd wiki | paperclip v14 + multica v15 + graphify v16 | High |

## 4. 15 platforms — detailed

### Tier A: Major commercial platforms (4)

| Platform | Provider | Role in corpus |
|----------|----------|----------------|
| **Claude Code** | Anthropic | Primary integration (most wikis) |
| **Codex** | OpenAI | Multi-wiki presence |
| **Cursor** | Cursor | IDE-based AI coding |
| **GitHub Copilot CLI** | Microsoft | Terminal-first Copilot |

### Tier B: Community-driven platforms (4)

| Platform | Role |
|----------|------|
| **OpenCode** | Community code agent |
| **Aider** | Terminal-first AI pair programmer |
| **OpenClaw** | Emerging runtime standard (4 wikis now) |
| **Hermes** | Emerging runtime standard (3 wikis now) |

### Tier C: Provider-specific / emerging (4)

| Platform | Provider |
|----------|----------|
| **VS Code Copilot Chat** | Microsoft |
| **Gemini CLI** | Google |
| **Factory Droid** | Factory |
| **Kiro IDE/CLI** | Community |

### Tier D: Specialty / regional (3)

| Platform | Provider/Region |
|----------|-----------------|
| **Trae (standard)** | Community |
| **Trae (CN)** | Chinese community (regional variant) |
| **Google Antigravity** | Google research |

### Install pattern

```bash
pip install graphifyy
graphify [platform] install
```

Writes skill to platform-specific location (e.g., `~/.claude/skills/graphify/` for Claude Code).

## 5. Pattern #18 — Agent Runtime Standardization

### Formal statement (v16 update)

> "As the agent ecosystem matures, certain runtime identifiers emerge as **de facto standards** that multiple independent frameworks support as target runtimes. **Execution-level evidence (dedicated install paths) is stronger than documentation mentions.**"

### OpenClaw timeline

| v# | Wiki | Evidence level | Context |
|----|------|----------------|---------|
| v12 | codymaster | 📄 Doc mention | Listed as install platform |
| v14 | paperclip | 🏗️ Architecture | First-class adapter + metaphor |
| v15 | multica | 📄 Doc mention | 1 of 8 supported agent models |
| **v16** | **graphify** | **🛠️ Execution** | **Dedicated `graphify openclaw install`** |

**Progression:** doc → architecture → doc → execution. Graphify is **first to ship production install binding** for OpenClaw.

### Hermes timeline

| v# | Wiki | Evidence level | Context |
|----|------|----------------|---------|
| v14 | paperclip | 🏗️ Architecture | Hermes adapter externalization note |
| v15 | multica | 📄 Doc mention | 1 of 8 supported agent models |
| **v16** | **graphify** | **🛠️ Execution** | **Dedicated `graphify hermes install`** |

**Progression:** architecture → doc → execution. Similar pattern.

### What this means

**OpenClaw and Hermes are real target runtimes, not aspirational.** Multiple independent projects ship binding code. The agent-runtime ecosystem is **consolidating around shared identifiers**.

**Predicted next wikis:** Should show more OpenClaw + Hermes integrations. Confidence: high.

## 6. Why graphify can integrate with 15 platforms

### Architectural answer

Graphify's skill surface is simple:
- **Input:** folder path or query string
- **Output:** markdown / JSON / stdout text
- **Invocation:** CLI command or MCP server

No deep-integration needed. Per-platform install writes a thin skill definition pointing to the same `graphify` CLI binary.

### Contrast with heavy integrations

- multica v15 desktop: requires Electron + WebSocket + daemon → per-platform deep work
- paperclip v14: requires persistent server + React UI → not a skill
- graphify: single Python CLI → trivially re-wrappable as skill

**Skill-as-distribution-unit favors simple tools.**

## 7. Implications for corpus ecosystem

### Validation of "skill-first" distribution

Graphify proves **skill-first distribution works at 30K-star scale**:
- No SaaS
- No server
- No monetization (yet)
- Just: pip install + skill install

**Replicable pattern** for future agent-tooling projects.

### OpenClaw + Hermes are standards

Storm Bear should now treat OpenClaw + Hermes as **de facto agent-runtime standards** in corpus analysis:
- Future wikis mentioning them = confirms pattern
- Future wikis without them = potential gap or intentional omission
- **Pattern #18 promotion from candidate to confirmed at v16** is justified

### Web-UI absence = architectural constraint

Graphify's missing integrations (ChatGPT web, Claude.ai web, Bard web) signal:
- **Browser-based agents can't run local Python**
- **Skill distribution requires CLI/daemon presence**
- **Future web-skill protocol?** (MCP web bridges might enable this — open question)

## 8. Edges + failure modes

### Platform drift

- Each of 15 platforms evolves its skill format
- Graphify must update per-platform install code
- **Maintenance burden scales with platform count**

### OpenClaw + Hermes identity questions

- **Which OpenClaw?** — if multiple implementations emerge, graphify install may target wrong one
- **Which Hermes?** — name collision risk (multiple "Hermes" projects in AI space)
- **Versioning** — if OpenClaw v1 vs v2 exist, graphify install may not specify

### Install path drift

- Claude Code `~/.claude/skills/` format may change
- Cursor skills API evolving
- Platform-specific breakage = per-platform release

## 9. Related concepts

- [[(C) Knowledge Graph for AI Coding Assistants]] — what the install provides
- [[../../multica - Beginner Analysis/02 Wiki/(C) skills-lock + Ecosystem Cross-Pollination]] — ecosystem context
- [[../../paperclip - Beginner Analysis/02 Wiki/(C) BYO Agent Adapter System + OpenClaw Standard]] — OpenClaw architectural entity

## 10. Cross-project comparison

### Platform counts by framework

| Framework | Platforms supported | Notes |
|-----------|---------------------|-------|
| ECC v1 | ~1 (Claude Code) | Native single |
| Superpowers v2 | ~3 | Claude Code + few |
| gstack v3 | 1 (Claude Code) | Tight coupling |
| GSD v5 | 14+ | Meta-prompting across harnesses |
| BMAD v11 | Multiple | IDE + Claude Code + others |
| codymaster v12 | 8+ | Multi-platform |
| multica v15 | 8 agent models supported | BYO agent |
| **graphify v16** | **15 skill-install targets** | **Broadest** |

**graphify wins broadest install surface** by nearly 2× over next closest.

### Contrast with single-platform

Projects locking to 1 platform:
- gstack v3 (Claude Code)
- ECC v1 (Claude Code primarily)
- autoresearch v10 (Claude Code via OAuth)

**Tradeoff:** depth vs breadth. gstack invests depth in Claude Code specifically; graphify spreads wide.

## 11. Open questions

- Q31: Per-platform install tested? (CI matrix across 15 platforms?)
- Q32: How quickly does graphify update when a platform's skill format changes?
- Q33: Are all 15 platforms actively maintained? (vs stale entries)
- Q34: Is there metrics on which platforms are most-used by graphify users?
- Q35: OpenClaw version support? (v1 / v2?)
- Q36: Hermes = which specific project? (name disambiguation)

## 12. Decision log

- **v0.1:** Claude Code install only
- **v0.2:** +Codex, +Cursor
- **v0.3:** +Gemini CLI, +Copilot CLI, +Aider
- **v0.4:** +OpenClaw, +Hermes, +OpenCode
- **v0.4.23 current:** 15 platforms
- **Future (inferred):** more community skills + possibly web-UI via MCP bridges

## 13. References

- README platform install section
- Cross-wiki OpenClaw mentions: codymaster v12 + paperclip v14 + multica v15 + graphify v16
- Cross-wiki Hermes mentions: paperclip v14 + multica v15 + graphify v16
- Parent: [[(C) index]]
- Storm Bear vault Pattern Library #18

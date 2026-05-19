# Entity 2: Distribution & Multi-Platform Ecosystem

**Type:** T1 Deployment package | **Format:** Skills CLI + git-clone + prompt-based | **Platforms:** Claude Code, Codex, OpenAI Agents

---

## 1. What is it?

agents-best-practices distribution ecosystem enables deployment across 3 major AI agent platforms via skills CLI, git clone, or prompt-based integration. Package = SKILL.md + 15 reference files (48KB markdown).

---

## 2. Who uses it?

- **Platform operators:** Installing skill in Claude Code / Codex environments
- **DevOps engineers:** Packaging skills for multi-platform deployment
- **SDK users:** Integrating via npm + GitHub
- **Offline users:** Deploying without npm dependency

---

## 3. Core function

Provides three deployment pathways (skills CLI → git clone → prompt-based) enabling agents-best-practices adoption across provider landscape. Removes installation friction through choice.

---

## 4. Architecture

```
agents-best-practices Repository
  ├─ SKILL.md (skill definition)
  ├─ README.md (usage guide)
  └─ references/ (15 markdown files)
  
Distribution Channel 1: npm + skills CLI
  → npm registry
  → `skills attach DenisSergeevitch/agents-best-practices`
  → Auto-discovered in Claude Code / Codex
  
Distribution Channel 2: Git Clone
  → GitHub repository
  → Local file:// references
  → Manual installation for offline use
  
Distribution Channel 3: Prompt-Based
  → Copy SKILL.md content into system prompt
  → Reference 15 files as separate context blocks
  → Works with any agent platform
```

---

## 5. Key concepts

### 15-Reference Architecture
Each reference file serves governance purpose:
- agentic_loop.md (7 invariants)
- 8_principles.md (foundational philosophy)
- autonomy_levels.md (L0-L4 progression)
- context_architecture.md (12-tier model)
- tool_design.md (risk taxonomy)
- planning_mode.md (complex task design)
- security_threats.md (15-category threat model)
- implementation_pathway.md (15-step build sequence)
- draft_commit_pattern.md (two-phase separation)
- error_handling.md (errors as observations)
- observability.md (trace discipline)
- prompt_caching.md (token optimization)
- mcp_integration.md (connector architecture)
- skills_connectors.md (skill packaging)
- guardrails.md (7-layer security defense)

### MCP Staged Exposure
Load tools in 4 stages (list → search → load full schemas → execute) to prevent context explosion while maintaining full capability access.

### Multi-Platform Support Matrix

| Feature | Claude Code | Codex | OpenAI Agents |
|---------|---|---|---|
| Skills CLI | ✓ | ✓ | ✗ |
| File tools | ✓ | ✓ | ✓ custom |
| MCP native | ✓ | ✗ | ✗ |
| Prompt caching | ✓ | ✓ | ✓ |
| Token efficiency | Minimal discovery | Minimal discovery | Full in-prompt |
| Setup time | <1 min | <1 min | ~10 min (manual) |

---

## 6. Design philosophy

**Multi-platform first:** Support all major AI agent platforms equally (no vendor preference).

**Progressive disclosure:** Expose skill incrementally (name → description → principles → references) to minimize token cost.

**Offline-capable:** Git clone fallback ensures deployment without npm infrastructure.

**Cache-friendly:** Stable prefix (tool defs, static instructions) designed for prompt caching; dynamic suffix (task-specific context) kept minimal.

---

## 7. Configuration & deployment

**Installation Path 1: Skills CLI**
```bash
npm install -g skills
skills attach DenisSergeevitch/agents-best-practices
```
Outcome: Skill auto-discovered in Claude Code / Codex. Works immediately.
Requirement: Node.js 18+, npm 9+

**Installation Path 2: Git Clone**
```bash
git clone https://github.com/DenisSergeevitch/agents-best-practices.git
cp -r agents-best-practices/SKILL.md ~/.codex-skills/
cp -r agents-best-practices/references/ ~/.codex-skills/references/
```
Outcome: Skill + references locally available. Manual version control.
Requirement: Git, file system access

**Installation Path 3: Prompt-Based**
Copy SKILL.md + 15 reference files content into system prompt directly.
Outcome: Works with any agent platform. No installation friction.
Cost: Token overhead (~35K tokens per session); no caching benefit

---

## 8. Integration with other entities

- **Entity 1 (Core Skill):** Defines skill content + philosophy; Entity 2 handles distribution
- **Entity 3 (Pattern Library):** Analyzes ecosystem standards integration (Pattern #78 N=3)
- **Entity 4 (Storm Bear):** Recommends deployment path for vault context

**Related subjects:**
- v66 agentmemory: Sister T2 service (also distributed via skills CLI)
- v65 claude-code-system-prompts: Alternative multi-platform reference (prompt-based install)
- v62 codex-plugin-cc: Cross-vendor deployment precedent

---

## 9. Typical workflow

**Claude Code deployment (5 min):**
1. Open Claude Code terminal
2. Run: `npm install -g skills && skills attach DenisSergeevitch/agents-best-practices`
3. Verify: `skills list | grep agents-best-practices`
4. Use: Reference skill in prompts (skill activates automatically)

**Codex deployment (5 min):**
1. Run: `skills attach DenisSergeevitch/agents-best-practices`
2. Skill auto-discovered in function-calling prompt
3. Use: Agent can invoke skill references

**OpenAI Agents deployment (10 min):**
1. Clone repo: `git clone https://github.com/DenisSergeevitch/agents-best-practices.git`
2. Copy SKILL.md into agent system prompt
3. Copy 15 reference files as separate context blocks
4. Use: Agent references skill via included content

**Offline deployment (5 min):**
1. Clone repo (no npm needed)
2. Use local file:// paths for SKILL.md + references
3. Works without internet connectivity

---

## 10. Tradeoffs

**Strengths:**
✓ Multi-platform support (Claude Code + Codex + OpenAI Agents)
✓ Installation choice (npm vs git clone vs prompt-based)
✓ Offline-capable (git clone doesn't require npm infrastructure)
✓ Progressive disclosure (agent loads references on-demand)
✓ Token-efficient (prompt caching compatible; <50KB footprint)
✓ Version-pinned (stable distribution via GitHub + npm)

**Limitations:**
✗ npm dependency (for skills CLI path; git clone avoids this)
✗ Context overhead (15 references = 48KB markdown; compaction required for long tasks)
✗ MCP limitations (native MCP in Claude Code only; Codex uses HTTP bridge; OpenAI Agents requires custom tools)
✗ Setup variation (installation path differs by platform; operator must choose correctly)
✗ Cache management (prompt caching beneficial for multi-task; adds implementation complexity)

---

## 11. Pattern library impact

**Pattern #78 (Living-Domain-Standards) N=3:**
Integrates MCP spec 2025-11-25 (referenced in mcp_integration.md) + OWASP + NIST. Multi-platform distribution enforces standard compatibility across Claude Code / Codex / OpenAI Agents.

**Pattern #84 (Cross-Vendor Ecosystem-Tolerance) N=3:**
agents-best-practices is provider-agnostic (no vendor preference). Distribution across Claude Code + Codex + OpenAI Agents equally demonstrates ecosystem tolerance in practice.

**Corpus-first:**
- First 15-reference-file structured reference library (most comprehensive reference architecture in corpus)
- First provider-agnostic skill with equal support for all 3 major agent platforms
- First multi-platform skill installer supporting both CLI + git-clone + prompt-based pathways

---

## 12. Related corpus subjects

| Subject | Relation | Deployment Method |
|---------|----------|------------------|
| v66 agentmemory | Sister T2 Service | Skills CLI |
| v65 claude-code-system-prompts | Pattern #78 co-evidence | Prompt-based (GitHub readme) |
| v62 codex-plugin-cc | Cross-vendor deployment | OpenAI plugin format |
| v63 andrej-karpathy-skills | High-velocity skill | Single-artifact (git clone) |
| v61 cc-sdd | Framework reference | Git clone |

---

## 13. Next steps

**For operators:** Choose installation path (skills CLI for maximum convenience; git clone for offline; prompt-based for any platform). Follow typical workflow for your platform.

**For platform engineers:** Validate MCP connector integration; test all 3 platforms (Claude Code, Codex, OpenAI Agents).

**For ecosystem researchers:** Monitor adoption across platforms; track which deployment path users prefer (signal for future skill design).

**For Storm Bear:** See Entity-4 (Storm Bear meta-entity) for recommended deployment path in vault context.

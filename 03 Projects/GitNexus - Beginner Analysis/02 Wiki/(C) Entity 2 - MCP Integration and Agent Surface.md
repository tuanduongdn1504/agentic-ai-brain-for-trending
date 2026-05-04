# (C) Entity — MCP Integration + Agent Surface

> **Category:** Agent integration architecture
> **Tier:** T4 bridge (MCP-runtime-standard consumer)
> **Wiki:** v33
> **Date:** 2026-04-23

---

## 1. One-line summary

GitNexus exposes its knowledge graph through a 16-tool MCP server configurable across 5 AI editors, with Claude Code receiving the deepest integration (MCP + Skills + bidirectional PreToolUse/PostToolUse hooks) — establishing GitNexus as the corpus's most extensive single-project MCP implementation.

## 2. MCP tool catalog (complete)

### Per-repo tools (7+)

| Tool | Signature (paraphrased) | Purpose |
|------|------------------------|---------|
| `list_repos` | `() → [repo, …]` | Enumerate indexed repositories |
| `query` | `(question, filters?)` | Natural-language or structured query |
| `context` | `(target: file/function/class)` | Fetch context for a symbol |
| `impact` | `(proposed_change)` | Blast-radius analysis |
| `detect_changes` | `(git_diff)` | Changed-lines → affected processes |
| `rename` | `(old_symbol, new_symbol)` | Multi-file coordinated rename |
| `cypher` | `(cypher_query)` | Raw Cypher graph query (power-user) |

### Group tools (5 — multi-repo)

| Tool | Purpose |
|------|---------|
| `group_list` | List repository groups |
| `group_sync` | Sync all repos in group with git HEAD |
| `group_contracts` | Identify contract-boundaries (API surfaces) between repos |
| `group_query` | Cross-repo query |
| `group_status` | Group-level health/indexing state |

### Additional tools (4 — counted to 16 total)
- context-specific helpers (prompt resources, skill registrations)
- Exact names not fully detailed in README; documented as "tools + resources + prompts + skills" collectively

## 3. Editor integration matrix

| Editor | MCP | Skills | Hooks | Setup command |
|--------|-----|--------|-------|---------------|
| **Claude Code** | ✓ | ✓ (4 built-in + auto-generated) | ✓ PreToolUse + PostToolUse | `gitnexus setup` |
| **Cursor** | ✓ | ✓ | — | `gitnexus setup` (writes `.cursor/mcp.json`) |
| **Codex** (OpenAI) | ✓ | ✓ | — | `gitnexus setup` |
| **Windsurf** | ✓ | — | — | `gitnexus setup` |
| **OpenCode** | ✓ | ✓ | — | `gitnexus setup` |

**Claude Code = deepest integration in corpus** — first in corpus with bidirectional PreToolUse + PostToolUse hooks.

## 4. Built-in skills (`.claude/skills/`)

| Skill | Purpose |
|-------|---------|
| **Exploring** | Agent explores unfamiliar codebase via GitNexus queries |
| **Debugging** | Agent traces bug through knowledge graph (execution-flow perspective) |
| **Impact Analysis** | Before change, agent calls `impact` for blast-radius |
| **Refactoring** | Multi-file rename with `rename` tool preserving correctness |

### Auto-generated skills via `--skills` flag

`gitnexus analyze --skills` generates repo-specific skills based on detected codebase patterns (e.g., if React detected, skill for "React component refactoring" emerges).

## 5. Hook architecture (Claude Code bidirectional)

### PreToolUse
- Fires BEFORE Claude Code executes a tool (e.g., Edit, Bash, Read)
- GitNexus hook fetches context from knowledge graph
- Appends context to agent's tool-use input
- **Effect:** agent has architectural context before making changes

### PostToolUse
- Fires AFTER Claude Code completes a tool execution
- GitNexus hook detects modified files
- Triggers incremental re-index
- **Effect:** graph stays current with user's edits

### Significance
- **Corpus-first bidirectional hook integration** (prior wikis used PreToolUse or PostToolUse singly)
- **Real-time graph accuracy** — graph never goes stale mid-session
- **Claude Code exclusive** — Cursor/Codex/Windsurf/OpenCode lack equivalent hook systems (platform differentiator signal)

## 6. Multi-repo architecture

### Global MCP registry

One `gitnexus-mcp-server` instance can serve multiple indexed repositories:

```
gitnexus-mcp-server ─┬─ repo1/
                     ├─ repo2/
                     └─ repo3/
```

Agent chooses `repo_id` parameter for per-repo tools. Groups allow batch operations.

### Group semantics

- Groups = collections of repos (e.g., micro-services in an org)
- `group_contracts` — identifies API-surface boundaries (cross-repo contract tests potential)
- `group_query` — spans all group repos
- `group_sync` — batch git HEAD sync across group

**Use case example:**
- Org has 12 micro-services in a "payments" group
- Developer modifies `payments-auth/src/token.ts` return type
- `group_contracts` identifies 3 other services consuming that type
- `group_query` locates all consumption sites
- `impact` analyzes blast radius across all 4 affected repos

### Novel primitive in corpus
- graphify v16: single-repo
- crawl4ai v29: multi-URL (web content)
- markitdown v28: single-document
- **GitNexus v33: multi-repo graph operations** (corpus-first)

## 7. MCP as corpus-wide runtime standard

### Pattern #18 layer 1 (CONFIRMED v15, MCP-extended v31 mini-audit)

- **Transport/protocol layer:** MCP (85K-scale via awesome-mcp-servers v31)
- **Consumers in corpus:** goclaw v4 / multica v15 / graphify v16 / spec-kit v17 / TrendRadar v19 / OpenHands v30 / **GitNexus v33** (7+ wikis with explicit MCP consumption)
- GitNexus = **most tools exposed per project (16)** reinforces MCP as universal layer

### GitNexus position in MCP ecosystem

- **Directory listing:** GitNexus likely listed in awesome-mcp-servers v31 (85K directory of 1,200+ MCP servers)
- **Quality differentiator:** 16 tools is upper-end of MCP server tool count
- **Adoption depth:** 5 editors = cross-ecosystem reach

## 8. Comparison with prior MCP observations

| Wiki | MCP role | Tool count |
|------|----------|------------|
| goclaw v4 | MCP consumer | Not disclosed |
| multica v15 | MCP consumer + skill registry | ~4-6 tools |
| graphify v16 | MCP server output | Not disclosed |
| spec-kit v17 | MCP consumer | Not disclosed |
| TrendRadar v19 | MCP server (21+ tools across 5 categories) | 21+ |
| OpenHands v30 | MCP consumer | Not disclosed |
| awesome-mcp-servers v31 | MCP directory (1,200+ servers) | meta-reference |
| markitdown v28 | MCP consumer | ~3 tools |
| **GitNexus v33** | **MCP server** | **16 tools** |

**TrendRadar v19 has 21+ tools; GitNexus v33 has 16.** Both in upper tier of MCP exposure. TrendRadar = news/trends domain; GitNexus = code domain. Different domains, similar MCP investment depth.

## 9. Hook integration distinctiveness

| Wiki | Hook integration |
|------|------------------|
| graphify v16 | Skill only (no hooks) |
| spec-kit v17 | No hooks (documentation only) |
| OMC v27 | Tmux-worker orchestration (not Claude Code hooks) |
| claude-howto v32 | TEACHES hooks (25 hook events documented) but doesn't USE hooks |
| **GitNexus v33** | **USES PreToolUse + PostToolUse hooks for real-time graph updates** |

GitNexus = **first corpus framework actually USING Claude Code bidirectional hooks for its own functioning** (not just documenting or teaching).

## 10. LangChain ReAct browser-agent

### Purpose
- Browser-resident AI agent (within gitnexus.vercel.app web UI)
- User chats with agent; agent queries local LadybugDB via LangChain ReAct reasoning

### Distinction from MCP agent
- **MCP agent:** developer's external agent (Claude Code, Cursor) consumes GitNexus via MCP
- **ReAct agent:** built-in browser agent consumes graph directly
- **Use case:** user wants quick exploration without external agent setup

### Significance
- Dual-agent surface — external (MCP) + built-in (ReAct)
- Corpus-first dual-surface documented

## 11. MCP resources + prompts + skills (the "4 additional tools" buffer)

MCP servers can expose:
- **Tools** — functions agents call
- **Resources** — data agents read (e.g., wiki pages from knowledge graph)
- **Prompts** — templates agents instantiate (e.g., "explain this codebase")
- **Skills** — reusable agent routines

GitNexus exposes all 4 kinds; "16 MCP tools" likely a mix or rounded claim. Exact breakdown not fully in README; comprehensive MCP server by any measure.

## 12. Agent context delivery primitives

### Context packages
- **Process-grouped:** results organized by execution-flow rather than flat file list
- **Confidence-scored:** each relationship has confidence level (EXTRACTED / INFERRED / AMBIGUOUS inherited from graphify v16 pattern)
- **Embedding-ranked:** hybrid BM25 + semantic + RRF re-ranking

### Token efficiency claim
- README claims "reliable, token-efficient" — no quantitative benchmark provided
- **Intuition:** graph query returns ~50 relevant symbols vs grep-with-context returning 2000+ tokens
- **Benchmark gap:** Pattern #8 absence at T4

## 13. Operator adoption friction

### Zero-friction path
1. `npm install -g gitnexus`
2. `gitnexus analyze /path/to/repo`
3. `gitnexus setup`
4. Open Claude Code → MCP server appears → 16 tools available

**~3 minutes end-to-end** for solo developer.

### Team / production friction
1. Docker Compose OR Kubernetes (Sigstore-signed)
2. Group-registry configuration for multi-repo
3. Shared MCP server address across team
4. **PolyForm Noncommercial commercial-gate** — requires akonlabs.com agreement for commercial team use

**~1-2 days + legal review** for production deployment.

## 14. Cross-wiki references

- [[graphify - Beginner Analysis]] v16 — MCP server output peer
- [[awesome-mcp-servers - Beginner Analysis]] v31 — MCP directory meta-reference
- [[spec-kit - Beginner Analysis]] v17 — MCP consumer peer
- [[TrendRadar - Beginner Analysis]] v19 — MCP server with 21+ tools peer
- [[OpenHands - Beginner Analysis]] v30 — MCP consumer at T5 peer
- [[claude-howto - Beginner Analysis]] v32 — documents Claude Code hooks (25 events)

## 15. Pattern Library observations

- **Pattern #18 Agent Runtime Standardization** — Strong data point (16 MCP tools + 5 editors + bidirectional hooks)
- **Pattern #22 AGENTS.md** — Absent (not in README); narrow-scope T4 refinement signal
- **Pattern #28 Multi-Provider AI Support (CONFIRMED v25)** — not direct provider-routing, but 5 editor integrations = editor-level multi-provider analog
- **Pattern #56 Multi-Runtime Orchestration (candidate v27)** — GitNexus integrates 5 editor runtimes but doesn't ORCHESTRATE them (distinct from OMC v27 multi-runtime orchestration)

## 16. Future-looking (roadmap implications for MCP)

Roadmap "AST decorator detection" could expose framework-specific MCP tools:
- `react_component_analysis`
- `spring_controller_hierarchy`
- `django_url_graph`

Would expand 16 → 30+ MCP tools, further solidifying GitNexus as MCP-exposure leader in corpus.

"LLM cluster enrichment" could expose:
- `cluster_semantic_name`
- `cluster_cohesion_score`

Enhancing context delivery quality.

"Incremental indexing" improves hook performance — PostToolUse hook becomes near-instant vs current full re-index.

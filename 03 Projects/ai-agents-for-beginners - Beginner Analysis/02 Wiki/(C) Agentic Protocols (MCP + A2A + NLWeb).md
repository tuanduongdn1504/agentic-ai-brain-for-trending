# (C) Agentic Protocols (MCP + A2A + NLWeb)

> Entity page — Infrastructure concept
> Sources: Lesson 11 (agentic protocols)
> Format: 13-section canonical

## 1. What are they / Là gì

**3 protocols** forming tiered agent ecosystem infrastructure:

| Protocol | Full name | Connects |
|----------|-----------|----------|
| **MCP** | Model Context Protocol | LLM ↔ tools |
| **A2A** | Agent-to-Agent | Agent ↔ agent |
| **NLWeb** | Natural Language Web | Agent ↔ website |

Không phải tools, là **specifications/standards** để tools interoperate.

## 2. Why they matter / Sao quan trọng

**Pre-protocol era:**
- Each tool = custom API integration code
- Can't swap LLM models easily (coupled to tool calling format)
- Agents can't talk to each other across vendors
- Websites unreachable to agents except via scraping

**Post-protocol era (emerging):**
- Write tool once, use from any MCP-compliant LLM
- Agents from different vendors interoperate via A2A
- Websites become agent-accessible via NLWeb
- **Composability unlocked.**

## 3. MCP detail

### Architecture
Client-server. Hosts (LLM apps like Claude Code) connect to servers exposing capabilities.

### 3 capability types
- **Tools** — discrete functions agents can invoke (e.g., "create GitHub issue")
- **Resources** — read-only data items (e.g., "file contents at path X")
- **Prompts** — predefined templates (e.g., "code review template")

### Origin
Anthropic (released 2024), now wide adoption.

### Status
**Most adopted of 3 protocols.** Claude Code native support, many sibling frameworks integrate.

## 4. A2A detail

### Purpose
Cross-vendor agent collaboration.

### Key properties
- Different AI agents communicate across organizations + tech stacks
- Each agent runs own LLM + internal tools
- Built-in authentication
- Enables multi-vendor systems

### Vs MCP
| Axis | MCP | A2A |
|------|-----|-----|
| **Scope** | LLM-to-tool (intra-stack) | Agent-to-agent (inter-vendor) |
| **Auth** | Host-managed | Built-in |
| **Use case** | Tool integration | Cross-org agent collaboration |

### Origin
Google (2025).

### Status
Emerging. Smaller adoption than MCP currently.

## 5. NLWeb detail

### Purpose
Transform websites into AI-accessible systems.

### Mechanism
- Processes natural language questions through embedding models + vector DBs
- Simultaneously functions as MCP server (dual role)
- AI agents can query website content directly

### Dual interface
- **For humans** — natural language Q&A UI
- **For agents** — MCP server interface

### Origin
Microsoft (2025).

### Status
Newest of 3. Bet on web-wide agent accessibility.

## 6. Tiered ecosystem

| Tier | Protocol | What it connects | Example |
|------|----------|------------------|---------|
| **Tools** | MCP | Agent → tools/data | Claude Desktop + filesystem MCP |
| **Peers** | A2A | Agent → agent | Agent (vendor X) → Agent (vendor Y) |
| **Web** | NLWeb | Agent → website | AI agent → Microsoft Learn via NLWeb |

→ **Complementary, not competing.** All 3 needed for full agent ecosystem.

## 7. Why protocols solve agent industry challenges

### Solved by MCP
- Static API integration (now dynamic tool discovery)
- Model-tool coupling (now swap models without rewrites)
- Per-tool auth complexity (now standardized)

### Solved by A2A
- Vendor lock-in for multi-agent systems
- Authentication fragmentation across orgs
- Cross-LLM coordination impossibility

### Solved by NLWeb
- Scraping-based web access (brittle)
- No grounded citation for AI answers
- Web content not agent-structured

## 8. Adoption patterns (2026 snapshot)

| Protocol | Adoption | Evidence |
|----------|----------|----------|
| **MCP** | High | Claude Code, many IDEs, Tier 1 siblings integrate |
| **A2A** | Medium | Google Cloud, some enterprise |
| **NLWeb** | Low-emerging | Microsoft demos, few production deployments |

→ **MCP = must-know now. A2A = track. NLWeb = watch.**

## 9. Trade-offs / Limitations

- **Protocol sprawl** — 3 protocols to track, each evolving
- **Vendor-driven** — each protocol has single "owner" organization
- **Security surface expanded** — protocols = new attack vectors
- **Overhead** — protocol negotiation adds latency
- **Immature A2A/NLWeb** — breaking changes likely

## 10. Comparison to sibling implementations

| Sibling | MCP usage | A2A usage | NLWeb usage |
|---------|-----------|-----------|-------------|
| **ECC** | Core (MCP servers in config) | None | None |
| **Superpowers** | Used (MCP integration) | None | None |
| **gstack** | Used (multi-MCP support) | None | None |
| **GSD** | 14 harnesses = MCP-aware | None | None |
| **goclaw** | Platform-level MCP routing | Not documented | Not documented |

→ **All 5 siblings = MCP users. None visible A2A or NLWeb adopters yet.**

**Signal:** MCP is the only "here now" protocol. A2A and NLWeb = future.

## 11. Common pitfalls

1. **Treating all 3 as equivalent** — they solve different problems, don't force one-size-fits-all
2. **Premature A2A adoption** — spec still evolving, expect breaking changes
3. **MCP server sprawl** — installing 20 MCP servers = security + complexity nightmare
4. **Ignoring auth implications** — MCP server = tool execution, misconfigured = exfil risk
5. **NLWeb for internal content** — NLWeb designed for public web, overkill for private KB

## 12. When NOT to use each protocol

- **MCP not needed:** agent needs only LLM reasoning, no external tools
- **A2A not needed:** all agents from same vendor/stack
- **NLWeb not needed:** agent accesses structured APIs, not website crawling

## 13. Storm Bear vault relevance + References

**Vault currently:**
- **MCP:** Not configured yet. Could add filesystem MCP, GitHub MCP for future.
- **A2A:** N/A (single-agent vault).
- **NLWeb:** N/A (vault is private Obsidian).

**Upgrade path for Storm Bear:**
1. **Near-term:** Add MCP servers for GitHub (PR creation) + filesystem (cross-vault operations)
2. **Mid-term:** Monitor A2A for multi-vendor Storm Bear team tools
3. **Long-term:** Consider NLWeb if vault publishes public wiki

**Cross-referential knowledge:**
- All Tier 1 siblings USE MCP → vault should understand MCP config deeply
- goclaw PLATFORM-deploys via MCP routing → if vault adopts goclaw, MCP mastery required

## References

- Source: [[(C) Frameworks + Protocols cluster summary]] (lesson 11)
- Related entities: [[(C) Agent Design Patterns]], [[(C) Agentic RAG]], [[(C) Multi-Agent Systems]]
- External specs:
  - MCP: modelcontextprotocol.io (Anthropic)
  - A2A: Google Cloud A2A docs
  - NLWeb: Microsoft Learn NLWeb docs
- Sibling MCP implementations:
  - `../../Everything Claude Code - Beginner Analysis/02 Wiki/(C) MCP servers.md` (if exists)
  - `../../get-shit-done - Beginner Analysis/02 Wiki/(C) 14-Harness npm Distribution.md`

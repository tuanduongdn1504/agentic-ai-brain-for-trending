# (C) Agentic RAG

> Entity page — Workflow concept
> Sources: Lesson 05
> Format: 13-section canonical

## 1. What is it / Nó là gì

**Agentic RAG** = Retrieval-Augmented Generation với **iterative loop + autonomous decision-making**. Thay vì linear pipeline (retrieve → read → respond), agent:
- Plans next step
- Selects tool/retrieval method
- Assesses result
- Refines or tries alternative
- Maintains memory to avoid repetition

**Key distinction:** State + self-direction, not scripted chain-of-thought.

## 2. Why it matters / Sao quan trọng

**Classic RAG failure modes:**
- Ambiguous queries → wrong retrieval
- Multi-step research → manual orchestration needed
- Conflicting sources → no resolution mechanism
- Stale indexes → no retry logic

**Agentic RAG addresses:**
- Ambiguous → refines query in loop
- Multi-step → orchestrates itself
- Conflicting → evaluates + selects
- Stale → switches tool/source

**Cost:** more tokens, longer latency. **Worth it** khi queries complex enough.

## 3. The 5-Step Iterative Loop

1. **Initial LLM Call** — present user objective to model
2. **Tool Selection** — model identifies needed info, invokes retrieval method
3. **Assessment** — evaluate returned data sufficiency
4. **Refinement / Repeat** — adjust approach if needed, try alternative tools
5. **Memory Maintenance** — track previous attempts to avoid repetition

**Loop terminates when:**
- Assessment says "sufficient"
- Max iterations reached
- Timeout hit
- User cancels

## 4. Classic RAG vs Agentic RAG

| Axis | Classic RAG | Agentic RAG |
|------|-------------|-------------|
| **Flow** | Linear | Loop |
| **Decision** | Scripted | Autonomous |
| **State** | Stateless | State + memory |
| **Tool use** | Single | Multiple, switchable |
| **Query refinement** | No | Yes |
| **Latency** | Low (1 call) | Medium-high (N calls) |
| **Cost** | Low | Medium-high |
| **Fit** | Simple Q&A | Complex research |

## 5. Capabilities

### Self-Correction
- Iterate failed queries
- Rewrite database calls
- Invoke diagnostic tools when first tool returns insufficient

### Domain Autonomy
- Operate dynamically within defined boundaries
- Respect available infrastructure
- Don't invent new sources

### Extended Workflows
- Evolve strategies as new info surfaces
- Handle multi-hop reasoning (A retrieved → reveals need for B → retrieves B)

## 6. Applications

- **Compliance verification** — multi-step doc check với self-check
- **Complex DB queries** — SQL agent tries approaches, refines
- **Lengthy research** — agent spans multiple sources, synthesizes
- **Multi-source reconciliation** — evaluate conflicting info sources

## 7. Design considerations

### Memory design
- Per-loop iteration scratchpad
- Cross-loop session memory
- Cross-session long-term memory (optional)

### Tool registry
- Which retrieval tools available? (vector DB, SQL, web, file search)
- Cost per tool (token + latency)
- When to switch vs refine current

### Assessment heuristic
- How does agent know "enough"?
- LLM-judged confidence? Cosine similarity threshold? Human eval?

### Iteration cap
- Max loops before escalation to human
- Budget per query (tokens + time)

## 8. Trade-offs / Limitations

- **Cost unpredictable** — N iterations variable, budget harder
- **Hallucination amplification** — self-correction might cement wrong answer
- **Latency** — users may timeout mentally before agent finishes
- **Debugging harder** — loop state complex to trace
- **Prompt engineering burden** — assessment prompt = critical engineering

## 9. Comparison to sibling implementations

| Sibling | Agentic RAG implementation |
|---------|---------------------------|
| **ECC** | Not explicit. Skills lookup = static. |
| **Superpowers** | Partial. Search + doc ingest, but not full loop. |
| **gstack** | Spec-driven search + iterative refinement in phases |
| **GSD** | `/gsd-ingest-docs` command = structured doc-to-knowledge, not full RAG loop |
| **goclaw** | **Full Agentic RAG implementation** — Knowledge Vault với 3-tier memory + iterative retrieval |

→ **goclaw = most complete Agentic RAG of 5 siblings.** Others implement subset.

## 10. Common pitfalls

1. **No iteration cap** — infinite loop drains budget
2. **Assessment prompt too lenient** — agent says "sufficient" too early
3. **Tool registry too small** — agent can't switch when stuck
4. **Memory leaks** — each iteration adds context, eventually overflow
5. **Missing terminator** — no "give up + escalate human" path

## 11. When NOT to use Agentic RAG

- **Simple factual Q&A** — classic RAG sufficient, lower cost
- **Latency-critical** — real-time chat, sub-second response needed
- **Deterministic required** — regulatory contexts with audit trail
- **Budget-constrained** — N-call cost unacceptable
- **Training data sufficient** — if LLM knows answer, no retrieval needed

## 12. Storm Bear vault relevance

**Vault's `llm-wiki-ingest` skill** ≈ **Agentic RAG applied to wiki construction**:

| Agentic RAG step | Wiki build analog |
|------------------|-------------------|
| Initial LLM Call | "Build wiki for X topic" |
| Tool Selection | Read source file / cross-reference sibling wiki |
| Assessment | "Is this entity page complete per 13-section format?" |
| Refinement | Re-read source, add missing section |
| Memory Maintenance | Cross-reference prior entity pages, log |

→ **Vault operationalizes Agentic RAG for knowledge-building domain.** Course teaches general pattern, vault applies to specific use.

**goclaw Knowledge Vault** = full production-ready Agentic RAG. Future Storm Bear vault upgrade path.

## 13. References

- Source: [[(C) Core lessons cluster summary]] (lesson 05)
- Related entities: [[(C) Agent Design Patterns]], [[(C) Agentic Protocols (MCP + A2A + NLWeb)]]
- Sibling implementations:
  - `../../goclaw - Beginner Analysis/02 Wiki/(C) 3-Tier Memory + Knowledge Vault.md` (full implementation)
  - `../../get-shit-done - Beginner Analysis/02 Wiki/(C) Context Rot Solution.md` (related: context management)
- Vault skill: `../../../05 Skills/llm-wiki-ingest.md`

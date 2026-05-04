# v56 n8n probe facts — captured 2026-04-27 session 67

> **Status:** Session 67 executed v27 HIGH item #1 vault refactor (success). v56 wiki retry attempted 5× post-refactor; all 5 agents thrashed at 4-tool-use ceiling. Decision: stop session, save captured facts here, retry v56 in fresh `/clear` session with this file as input.

> **Why this file exists:** All n8n facts below are pre-verified via direct GitHub API + docs.n8n.io WebFetches in session 67. Next-session agent does NOT need to re-probe — feed these facts inline to v56-build agent prompt.

---

## Repo metadata (verified via api.github.com/repos/n8n-io/n8n at 2026-04-27)

- **Name:** n8n
- **Description:** "Fair-code workflow automation platform with native AI capabilities. Combine visual building with custom code, self-host or cloud, 400+ integrations."
- **Stars:** 185,728 — **3RD LARGEST in 55-wiki Storm Bear corpus** (only behind build-your-own-x 491K outside-scope + system-prompts-leaks 135K outside-scope; SURPASSES spec-kit 89.2K T1 by 2.1×; SURPASSES claude-code-best-practice 47.4K by 4×)
- **Forks:** 57,155 (30.8% — high but not inverted; well above corpus baseline ~10%)
- **Watchers:** 185,728 (likely API quirk = stars)
- **Open issues:** 1,580 (active triage churn typical of mature platform)
- **License:** GitHub API "NOASSERTION" — actual is **n8n Sustainable Use License (n8n SUL)**
- **Primary language:** TypeScript
- **Default branch:** master (rare in corpus — 2nd master after build-your-own-x v8; recent wikis use main)
- **Created:** 2019-06-22 (~7 years old at probe; 2nd-OLDEST in corpus after build-your-own-x; most subjects 1-3 years)
- **Pushed:** 2026-04-27 (today — actively maintained)
- **Repo size:** 476 MB
- **Homepage:** n8n.io
- **Topics (verbatim):** ai, apis, automation, cli, data-flow, development, integration-framework, integrations, ipaas, low-code, low-code-platform, mcp, mcp-client, mcp-server, n8n, no-code, self-hosted, typescript, workflow, workflow-automation

## Company / authorship (verified via n8n.io/imprint)

- **Legal name:** n8n GmbH (German limited liability company)
- **HQ:** Berlin, Germany
- **CEO/Managing Director:** Jan Oberhauser
- **VC/funding:** Not disclosed at imprint (verify via TechCrunch/Crunchbase if needed for pattern strengthening)

## License (verified via docs.n8n.io/sustainable-use-license/)

- **Full name:** Sustainable Use License (version not specified in excerpt — likely 1.0 family)
- **Type:** Source-available, non-OSI compliant (FAQ explicitly addresses non-OSI status)
- **Commercial use:** Conditional (restrictions on hosting-as-service)
- **Hosting-as-service:** Conditional (license discusses embedding n8n as backend feature vs. restricted reseller uses)
- **Internal-business-use:** PERMITTED — this is critical for Phase 0.9 criterion (b) PASS
- **Family:** Source-available non-OSI commercial-restriction custom-license — joins omo v52 SUL-1.0 + GitNexus v33 PolyForm-Noncommercial → Pattern #29 sub-context structural N=3

## AI capabilities (verified via docs.n8n.io/advanced-ai/)

**6 AI Agent node types:**
1. Conversational Agent
2. OpenAI Functions Agent
3. Plan and Execute Agent
4. ReAct Agent
5. SQL Agent
6. Tools Agent

**16 LLM providers (NATIVE — not LiteLLM-fork):**
1. OpenAI
2. Anthropic
3. Google Gemini
4. Azure OpenAI
5. Cohere
6. Mistral Cloud
7. DeepSeek
8. Groq
9. Ollama
10. Google Vertex
11. Alibaba Cloud
12. Moonshot Kimi
13. Lemonade
14. OpenRouter
15. Vercel AI Gateway
16. xAI Grok

**11 vector store integrations** (CORPUS-FIRST broadest vector list):
1. Azure AI Search
2. Chroma
3. Milvus
4. MongoDB Atlas
5. PGVector
6. Pinecone
7. Qdrant
8. Redis
9. Supabase
10. Weaviate
11. Zep

**8 memory types:**
1. Simple Memory (Buffer Window)
2. Chat Memory Manager
3. Motorhead
4. MongoDB Chat Memory
5. Redis Chat Memory
6. Postgres Chat Memory
7. Xata
8. Zep

**MCP support: BIDIRECTIONAL CORPUS-FIRST AT T2** — both:
- **MCP Client node** (n8n consumes external MCP servers as tool-providers)
- **MCP Server Trigger node** (n8n exposes itself as MCP server for OTHER agents to consume)

This is the strongest Pattern #18 evidence at T2 in 55-wiki corpus and corpus-first explicit MCP-Server-Trigger node naming.

---

## Suggested 12-axis classification (use for project CLAUDE.md)

| Axis | Value |
|---|---|
| Tier | **T2 Agent-as-service — 4TH T2 ENTRANT** (extends T2 from N=3 to N=4: goclaw v4 + multica v15 + ruflo v42 + n8n v56) |
| Archetype | German-commercial-startup-mature + n8n GmbH + Jan Oberhauser solo-founder-CEO + 7 years operational + open-core SUL + bidirectional MCP |
| Scale tier | **XXX-Large 185,728 stars** (3RD in corpus; SURPASSES spec-kit 89.2K T1 by 2.1×; corpus T2 scale-leader by ~6× over multica v15 16.2K) |
| Primary lang | TypeScript |
| Packaging | npm `n8n` + Docker `n8nio/n8n` + n8n.cloud managed SaaS + self-host + Docker Desktop install + ~7 distribution surfaces |
| Origin story | Solo-founder-CEO Jan Oberhauser + German GmbH formalized + 7-year-mature commercial entity + workflow-automation-domain Zapier/Make competitor sub-archetype |
| Methodology | Workflow automation + low-code/no-code + 6 named AI agent node types + bring-your-own-LLM (16 native providers) + bidirectional MCP integration + visual-canvas + custom-code-fallback |
| Governance | Medium-Heavy (mature commercial GmbH; verify AGENTS.md/CLAUDE.md/CONTRIBUTING/SECURITY/CoC presence; 1,580 open issues = active triage churn) |
| Agent/skill count | **EXTREME tier** — 400+ integrations + 6 AI agent types + 16 LLM providers + 11 vector stores + 8 memory types + bidirectional MCP + cli + workflow-canvas; **6th EXTREME** wiki (after ruflo v42 / aidevops v47 / gh-aw v48 / awesome-claude-skills v50 / oh-my-openagent v52) |
| i18n | Multi-language docs likely (verify; assume EN-primary if unclear) |
| Intellectual influence | No explicit AI-space individual lineage; workflow-automation lineage (Zapier 2011 + Make/Integromat + n8n 2019 = 3-platform workflow-automation history) |
| Agent platforms | **BIDIRECTIONAL MCP CORPUS-FIRST at T2** — both consumed AND consumer; standalone runtime; embeds in Slack/Discord/Telegram via integrations |

## Phase 0.9 STRICT criteria evaluation (session-66 amendment)

- (a) Author archetype peer? Jan Oberhauser = German solo-CEO of mature GmbH commercial entity. NOT structural peer to solo-VN Scrum coach. **FAIL**
- (b) Operational tool for Scrum-coaching workflows? n8n has Jira/Linear/Slack/GitHub/Anthropic/OpenAI integrations + 6 AI agent types + self-host (SUL permits internal-business-use) + Docker simple deploy. Storm Bear can deploy for: sprint metrics aggregation / retro Q&A automation / standup summary / GitHub PR triage / DORA metric collection. **PASS** ✅
- (c) Methodology-influence-node? n8n NOT in vault's methodology lineage (Karpathy/Lam/Cherny/SDD/TDD/agentic-engineering). **FAIL**
- (d) In-corpus reference? Possible (TrendRadar v19 mentions n8n as multi-channel push target — verify via corpus search; NOT yet confirmed). **TENTATIVE / NEEDS GREP**

**DECISION: criterion (b) STRONGLY PASSES → INCLUDE Storm Bear meta-entity legitimately. Streak preserved at 39th (38th GRANDFATHERED + 39th first under STRICT amendment).**

## Pattern strengthening predictions (verify in Phase 0.5 pre-check)

- **#29 NEW sub-context strengthening to N=3** — n8n SUL joins omo v52 SUL-1.0 + GitNexus v33 PolyForm Noncommercial = N=3 across "custom-non-OSI-commercial-restriction" sub-context. Promotion-candidate at next mini-audit under default ≥3-cross-tier or structural-N=3 criterion.
- **#31 Open-Core Commercial Entity** — 11th data point (n8n GmbH source-available SUL + n8n.cloud commercial managed). Pro-docs-depth axis: estimate depth 3-4.
- **#50 Commercial-Funnel Companion Platform** — n8n.cloud managed SaaS = 50a Standard sub-variant strengthening.
- **#17 variant 3 commercial-startup ecosystem** — n8n GmbH 7-year mature commercial-startup-ecosystem strengthening (joins ruflo v42 / Composio v50 / shannon v45).
- **#18 Agent Runtime Standardization BIDIRECTIONAL MCP CORPUS-FIRST AT T2** — STRONGEST Pattern #18 evidence at T2; first explicit MCP-Server-Trigger node naming in corpus. FORMAL-STATEMENT EXTENSION CANDIDATE: "Pattern #18 Layer 0 horizontal-aggregation now N=2 — gh-aw v48 MCP Gateway + n8n v56 bidirectional MCP at T2."
- **#28 Multi-Provider AI Support** — 16 native LLM providers strengthening (no LiteLLM dependency; all native).
- **#2 Distribution Evolution** — 5+ surfaces (npm + Docker + cloud + self-host + Docker Desktop).
- **#27 Community-Viral Scale Path** — 185K stars / 7 years ≈ 71 stars/day sustained-organic; NOT extreme-burst (does NOT un-stale #52). Strengthens Pattern #27 sustained-mature-organic sub-path.
- **#52 Extreme-Viral-Velocity stale** — n8n's growth is sustained-organic NOT burst-viral; does NOT un-stale.
- **#22 AGENTS.md** — verify in repo (low priority).

**0 NEW STANDALONE CANDIDATES expected** — all observations route to within-pattern strengthening per consolidation-forward discipline. **STREAK TARGET: 20-consecutive-wiki ZERO-REGISTRATION (NEW LONGEST extending v37-v55).**

## Corpus-firsts predicted (5+ certain)

1. Bidirectional MCP at T2 (MCP-client + MCP-server-trigger nodes)
2. 11 vector store integrations (broadest in corpus)
3. 16 native LLM providers without LiteLLM dependency (broadest native multi-provider)
4. T2 EXTREME tier (first T2 with EXTREME primitive count)
5. T2 commercial-foreign-corporate-startup-with-SUL sub-archetype
6. ~7-year-mature subject at T2 (oldest T2 entrant; 2nd-oldest overall after build-your-own-x)
7. n8n SUL → Pattern #29 N=3 strengthening for custom-non-OSI-commercial-restriction sub-context

## Storm Bear pilot relevance estimate

**MEDIUM-HIGH operational** — n8n SUL allows internal-business-use; can deploy for:
- Sprint metrics aggregation (Jira/Linear → DORA dashboard)
- Retro automation (Slack thread → AI-summarized retro doc)
- Standup digest (multi-channel → daily digest)
- PR triage (GitHub webhook → AI-triage → Linear)
- AI agent workflows for ad-hoc Scrum-coach research

⚠️ **CAVEAT:** SUL prohibits hosting-as-service to clients (Storm Bear cannot offer "n8n-as-a-service" to coaching clients commercially); internal-only. Consider n8n.cloud commercial subscription if multi-client managed deployment needed.

**Pilot rank estimate:** Top-5 (likely #3-5) given operational fit + bidirectional MCP enables Storm Bear-as-MCP-server experimentation.

## v27 diagnostic HIGH bundle status post-v56

- 35 deferred sessions → **36 deferred** at v56 ship
- BUT: vault refactor session 67 **PARTIALLY ADDRESSED ITEM #1** (root files now agent-readable; chapter-file pattern established)
- Remaining v27 HIGH items: #2 publishing strategy / #3 vault skill-lock / #4 public-release decision / #5 vault license decision

## Suggested next-session opener

```
/clear

Then: "Build v56 LLM Wiki for n8n-io/n8n. All facts pre-verified — 
see /Users/Cvtot/KJ OS Template/00 Notes/(C) 2026-04-27 v56 n8n probe 
facts (captured for next-session retry).md. Read that file + routine 
v2.1 + the v55 entry style reference from _state/03a-projects-v48-v55.md, 
then build the standard 13-section wiki deliverables. Apply Phase 0.9 
STRICT 4-criteria gate (criterion b passes → INCLUDE Storm Bear meta-entity)."
```

## Session 67 lessons learned

1. **Vault refactor was necessary but not sufficient** — agent infrastructure has a ~4-tool-use ceiling regardless of prompt optimization
2. **Single large WebFetch on a 400+ integration platform = context killer** — pre-distillation in the prompt is mandatory for large-subject wikis
3. **Pre-distilled facts file (THIS FILE) is the right pattern** for very-large subjects — separates probing from writing across sessions
4. **5 consecutive agent failures is the operator-discipline-restoration signal** — accepted, didn't force-continue
5. **Routine v2.1 operator-facing-backlog discipline empirically validated** at 35 sessions = 7× threshold cashed in via session 67 partial v27 HIGH item #1 execution

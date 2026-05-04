# (C) Combined Source Cluster Summary

> **Compressed scope:** Standard 3-cluster split not warranted at v56 because all facts are pre-distilled from session 67 WebFetches. This single combined cluster summarizes all probed sources with citation discipline.

## Source 1: GitHub repo metadata

**URL:** https://api.github.com/repos/n8n-io/n8n
**Probed:** 2026-04-27 session 67

**Key facts:**
- Repository name: `n8n-io/n8n`
- Description: "Fair-code workflow automation platform with native AI capabilities. Combine visual building with custom code, self-host or cloud, 400+ integrations."
- **Stars: 185,728** (3rd-largest in 56-wiki Storm Bear corpus)
- Forks: 57,155 (30.8% — high but not inverted)
- Watchers: 185,728 (likely API quirk = stars)
- Open issues: 1,580
- License (GitHub API field): "NOASSERTION" (actual = n8n SUL — see Source 3)
- Primary language: TypeScript
- Default branch: **master** (rare in corpus; recent wikis use main; 2nd master after build-your-own-x v8)
- Created: 2019-06-22 (~7 years old at probe; 2nd-OLDEST in corpus after build-your-own-x; most subjects 1-3 years)
- Last pushed: 2026-04-27 (today — actively maintained)
- Repo size: 476 MB
- Homepage: n8n.io
- Topics (verbatim): ai, apis, automation, cli, data-flow, development, integration-framework, integrations, ipaas, low-code, low-code-platform, **mcp, mcp-client, mcp-server**, n8n, no-code, self-hosted, typescript, workflow, workflow-automation

## Source 2: Company / authorship (imprint)

**URL:** https://n8n.io/imprint/
**Probed:** 2026-04-27 session 67

**Key facts:**
- Legal name: **n8n GmbH** (German limited liability company)
- HQ: **Berlin, Germany**
- CEO/Managing Director: **Jan Oberhauser** (solo-founder-CEO, identified as managing director)
- VC/funding: Not disclosed at imprint level (Q5 in OPEN-QUESTIONS.md)

## Source 3: Sustainable Use License

**URL:** https://docs.n8n.io/sustainable-use-license/
**Probed:** 2026-04-27 session 67

**Key facts:**
- Full name: **Sustainable Use License (n8n SUL)**
- Type: **Source-available, non-OSI compliant** (FAQ explicitly addresses non-OSI status)
- Commercial use: **Conditional** (restrictions on hosting-as-service)
- Hosting-as-service: **Conditional** (license discusses embedding n8n as backend feature vs. restricted reseller uses)
- **Internal-business-use: PERMITTED** (critical for Phase 0.9 criterion (b) PASS)
- Family: Source-available non-OSI commercial-restriction custom-license — joins omo v52 SUL-1.0 + GitNexus v33 PolyForm-Noncommercial → **Pattern #29 sub-context structural N=3**

## Source 4: AI capabilities (advanced AI docs)

**URL:** https://docs.n8n.io/advanced-ai/
**Probed:** 2026-04-27 session 67

**Key facts:**

**6 AI Agent node types:**
1. Conversational Agent
2. OpenAI Functions Agent
3. Plan and Execute Agent
4. ReAct Agent
5. SQL Agent
6. Tools Agent

**16 native LLM providers** (no LiteLLM dependency):
OpenAI / Anthropic / Google Gemini / Azure OpenAI / Cohere / Mistral Cloud / DeepSeek / Groq / Ollama / Google Vertex / Alibaba Cloud / Moonshot Kimi / Lemonade / OpenRouter / Vercel AI Gateway / xAI Grok

**11 vector store integrations** (CORPUS-FIRST broadest vector list):
Azure AI Search / Chroma / Milvus / MongoDB Atlas / PGVector / Pinecone / Qdrant / Redis / Supabase / Weaviate / Zep

**8 memory types:**
Simple Memory / Chat Memory Manager / Motorhead / MongoDB Chat Memory / Redis Chat Memory / Postgres Chat Memory / Xata / Zep

**MCP support: BIDIRECTIONAL CORPUS-FIRST AT T2:**
- **MCP Client node** — n8n consumes external MCP servers as tool-providers
- **MCP Server Trigger node** — n8n exposes itself as MCP server for OTHER agents to consume

This is the strongest Pattern #18 evidence at T2 in 56-wiki corpus and corpus-first explicit MCP-Server-Trigger node naming.

## Cross-source synthesis

n8n is best understood as a **3-decade workflow-automation lineage** (Zapier 2011 → Make/Integromat → n8n 2019) with a **modern AI-agent overlay** that grew organically across 7 years of solo-founder-CEO operational discipline. Unlike pure-AI-startups (e.g., shannon v45 founded-in-AI-era), n8n is a workflow-automation-platform that ADDED AI capabilities — distinguishing its commercial-startup-ecosystem maturity profile from younger AI-native peers.

Key tension surfaced: **n8n SUL custom-license commercial-restriction creates a Storm Bear pilot constraint**. Internal-business-use permitted means Storm Bear can self-host n8n for personal Scrum-coaching automation. Hosting-as-service-to-clients restricted means Storm Bear cannot offer "managed n8n workflows" to coaching clients commercially without n8n.cloud subscription. This is the critical Phase 0.9 criterion (b) qualification: n8n IS operational for Storm Bear's internal use; NOT operational for Storm Bear's external service-delivery use without commercial license.

## Limits of probe

- Q1-Q6 in OPEN-QUESTIONS.md are unresolved at v56 ship
- 400+ integration list NOT enumerated (cite-not-replicate per EXTREME primitive-count discipline)
- Multi-language docs status assumed EN-primary
- VC funding stage / round history not surfaced

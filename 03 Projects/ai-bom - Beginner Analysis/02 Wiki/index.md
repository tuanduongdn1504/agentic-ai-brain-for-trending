# (C) Trusera/ai-bom — "AI Bill of Materials" (v156 wiki)

> **Status: GOAL-ALIGNED INCLUDE 3/4** ((a) FAIL · (b) MODERATE [borderline, flagged for audit] · (c) STRONG · (d) STRONG). An open-source scanner that inventories + risk-scores every AI/agent component in a codebase or infra and emits SBOM-standard output. The **governance/supply-chain-inventory layer** of the "operate-your-agent-stack" tool family. CORPUS-FIRST AI-BOM generator. See `01 Analysis/`. Related-topic (the macOS-app-to-manage-AI-BOM ask) → `02 Wiki/(C) related-topic-macOS-app-to-manage-AI-BOM.md`.

**Repo:** https://github.com/Trusera/ai-bom · **Owner:** `Trusera` (security vendor — "Securing the Agentic Service Mesh"; trusera.dev) · **License:** Apache-2.0
**Tagline:** *"Discover every AI agent, model, and API in your infrastructure"*

## What it is
An **AI Bill of Materials** tool — the AI/agent analogue of a software SBOM. You point `ai-bom` at a codebase / container image / cloud account / n8n workflow / Jupyter notebook / GitHub Actions, and it **statically scans** for AI components, **risk-scores** them (0–100 + severity), checks them against compliance frameworks (EU AI Act, OWASP, licenses), and emits a standards-compliant inventory (CycloneDX 1.6 / SPDX 3.0 / SARIF 2.1.0 + HTML/Markdown/CSV/JUnit/JSON). The pitch is the "AI-shaped gap" left by traditional SBOM tools (Trivy/Syft/Grype don't know what an agent or a model is) and the **EU AI Act Article 53** (Aug 2025) requirement for a complete AI-component inventory.

It is **the open-source foundation of the commercial Trusera platform** for AI-agent security (open-core).

## What it inventories (13 auto-registered scanners)
- **LLM providers** — OpenAI, **Anthropic**, Google AI, Mistral, Cohere, Ollama, DeepSeek
- **Agent frameworks** — LangChain, CrewAI, AutoGen, LlamaIndex, LangGraph
- **Model references** — `gpt-4o`, `claude-3-5-sonnet`, `gemini-1.5-pro`, `llama-3`; model files (`.gguf`/`.safetensors`/`.onnx`/`.pt`)
- **API keys / secrets** — `sk-*` (OpenAI), `sk-ant-*` (Anthropic), `hf_*` (HuggingFace)
- **AI containers** — Ollama, vLLM, HuggingFace TGI, NVIDIA Triton, ChromaDB
- **Cloud AI** — AWS Bedrock/SageMaker, Azure OpenAI/ML, Google Vertex AI
- **MCP servers** — Model Context Protocol server configs (⚠️ it *detects* them — see "the direction" below)
- **+ endpoints, n8n nodes, CrewAI flows, Jupyter notebooks, GitHub Actions, model files, 25+ AI SDKs** across Python/JS/TS/Java/Go/Rust/Ruby

## Architecture (the instructive part)
> Scanner Engine [13 auto-registered scanners] → Pydantic models [`AIComponent` + `ScanResult`] → Risk Scorer [0–100 + severity] → Compliance modules [EU AI Act / OWASP / licenses] → Output [CycloneDX 1.6, SARIF 2.1.0, SPDX 3.0, HTML, Markdown, CSV, JUnit, JSON]

- **Regex-based detection by default** (not AST) — chosen for speed; parallel scanner execution via thread pool; risk scoring is stateless; CycloneDX 1.6 JSON generated directly from dicts.
- **651+ tests, 80%+ coverage** (per the contributing section).

## How you run it (7 surfaces)
```bash
pipx install ai-bom && ai-bom scan .                      # CLI (recommended)
docker run --rm -v $(pwd):/scan ghcr.io/trusera/ai-bom scan /scan
pip install ai-bom                                         # Python library: from ai_bom import scan
# + GitHub Action (uses: trusera/ai-bom@main) · n8n community node (n8n-nodes-trusera)
# + VS Code extension (trusera.ai-bom-scanner) · SDKs (trusera-sdk: Python / TypeScript / Go)
ai-bom scan-cloud ; ai-bom dashboard                       # cloud scan ; Flask HTML dashboard
```

## The direction (why this is a governance tool, not an agent tool)
ai-bom *audits* the agent ecosystem — it **detects** MCP servers, agent frameworks, and LLM providers as **inventory items**. It does **not** expose an MCP server, ship a Claude skill, or act as an agent. That's the opposite direction from the corpus's agent-capability tools:
- **v149 Scrapling** ships an MCP server + agent-skill so an agent can **use** it → capability-FOR-agents.
- **v156 ai-bom** scans your stack and lists the MCP servers/agents it **finds** → governance-OVER-the-stack.

This is the same "observes vs controls/serves" distinction the corpus drew at **v154 agentpet** (observes agents) vs the **v153/v117/v73 Tauri management-GUIs** (control them).

## Where it sits in the corpus
ai-bom adds a **new layer to the "operate-your-agent-stack" tool family** the corpus has been building since v149:

| Layer | Corpus members |
|---|---|
| provider-aggregation | Pattern #18 #8 (v73 + v112 + v117) |
| capability-provision (tool FOR agents) | v149 Scrapling |
| orchestration (agent-of-agents) | v150 Paseo |
| account / quota management | v153 ai-switcher |
| observability / metering | v89 + v109 + v154 agentpet |
| ambient / affective status | v154 + v155 (desktop pets) |
| **governance / supply-chain inventory** | **v156 ai-bom (NEW)** |

It is the **CORPUS-FIRST AI-BOM / AI-supply-chain-inventory generator** — see `01 Analysis/(C) Pattern-Library-Phase-4b.md` (PRIMARY, filed to registry 06 §C).

## Provenance (§37)
≈**246★** / 68 forks / 5 watchers / 7 open issues / 8 open PRs / **279 commits** / latest release **v3.1.0 (Feb 12, 2026)** / Apache-2.0 / Python 65.9% (+ TypeScript 28.3% + Go 5.3%).
*Page-stated as of 2026-06 via WebFetch of the rendered repo — **NOT independently API-verified (§37.4)**; this environment mocks the GitHub API.* Creation date not stated on the page → age/velocity unestablished → **NOT a Pattern #52 claim** (246★ is modest regardless). Owner `Trusera` (security vendor; ai-bom = the OSS foundation of the Trusera platform).

## Why it's goal-aligned (MODERATE, and where the line is)
- **On goal #1 (adjacent-but-real):** its entire subject matter IS the AI/agent ecosystem — it inventories agent frameworks, MCP servers, and LLM providers. "Know what AI/agents are actually in your stack" (EU AI Act, OWASP, supply-chain risk) is a legitimate professional dimension of *operating* autonomous-agent software at scale, and a coherent same-family member alongside agent-observability (v154) and account-management (v153).
- **Held MODERATE, not STRONG:** the center of gravity is **security / compliance / governance**, not building-or-operating coding agents; it's an audit/scanner you don't *build with*; for THIS vault's Claude-Code-mastery goal it's **adjacent-domain → architecture-study / awareness value, not a daily operational tool.** Flagged explicitly for the next audit to challenge (could go WEAK/off-goal).
- **No §35 incentive to inflate:** the ceiling was already clear (3 consecutive goal-aligned ships) before this ship, so the verdict is on merits.

## §35 / streak
**§35 STAYS CLEAR** — window {v154 GA, v155 GA, v156 GA} = 0 OG (4 consecutive goal-aligned ships). NOT an override → override-frequency UNCHANGED (7-in-20 trailing; lifetime 10). Streak GA:18·OG:11 → **GA:19·OG:11 [7 ov]** (19th goal-aligned PASS). Note: this **breaks the 3-in-a-row "desktop-app-to-manage-AI-coding-tools" niche run** (v153/v154/v155) — ai-bom is a different shape (a CLI/library governance scanner), though still in the broad operate-your-agent-stack family.

## Pilot
**READ-leaning pilot candidate.** It's genuinely worth *running once* — `pipx install ai-bom && ai-bom scan .` on a repo (or `docker run … scan /scan`) is reversible and shows you what AI components a scanner finds in your own code, and the **CycloneDX/SPDX/SARIF output design** is worth reading regardless. But its daily value to a Scrum-coach-mastering-Claude is awareness/architecture-study, not a tool you'd operate continuously. `install-snapshot` first if you `pipx install`. ⚠️ Standing note: the corpus has 4 goal-aligned ships running and ~zero piloted — running *one* scan here would be a cheap way to break that.

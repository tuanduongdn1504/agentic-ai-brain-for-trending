# (C) Workflow Builder + LLM-Abstraction + Cloud Cluster Summary

> **Cluster:** Workflow builder blocks + multi-LLM support + Skyvern Cloud vs self-hosted
> **Parent:** [[(C) index]]
> **Sources:** README workflow + integrations + deployment sections
> **Status:** ✅ Phase 2 cluster summary

---

## 1. Cluster scope

3 related signals:
1. **Workflow builder block catalog** — browser task + data + control-flow blocks
2. **Multi-LLM provider abstraction** — 10+ providers (OpenAI/Anthropic/Bedrock/Gemini/Ollama/OpenRouter/etc.)
3. **Cloud vs self-hosted** — Skyvern Cloud managed vs local pip/Docker

## 2. Workflow builder blocks

### Block catalog

| Block type | Purpose |
|------------|---------|
| **Browser Task** | High-level task ("book a flight") |
| **Action** | Low-level action (click/type) |
| **Data Extraction** | Scrape structured data |
| **Validation** | Check page state / conditions |
| **For Loops** | Iterate over lists |
| **File Parsing** | Parse PDFs / CSVs / docs |
| **Email Sending** | Send email via SMTP/API |
| **HTTP Request** | Call external APIs |
| **Custom Code** | Arbitrary Python/JS |
| **File Upload** | Upload to block storage |
| **Conditionals** | (Forthcoming — not yet shipped) |

### Novel observation

**10+ block types = comprehensive workflow surface.** Comparable scope to:
- Zapier (SaaS automation platform)
- Make.com (visual workflow builder)
- N8N (open-source workflow automation)

**Skyvern integrates with all 3** (listed as workflow-platform integrations).

### Integration positioning

Skyvern = **LLM-native browser agent** that plugs into existing workflow platforms. Not a full Zapier replacement — focused layer.

## 3. Multi-LLM provider abstraction

### Supported providers

| Provider | Models | Notes |
|----------|--------|-------|
| OpenAI | GPT-5, GPT-4.1, o3, o4-mini | Primary |
| Anthropic | Claude 4, Claude 4.5 | Primary |
| Azure OpenAI | Same as OpenAI | Enterprise |
| AWS Bedrock | Multiple | Enterprise |
| Gemini | Google Gemini | |
| Ollama | Local self-hosted | Privacy-first |
| OpenRouter | Aggregated | Cost optimization |
| OpenAI-compatible endpoints | Any | Fallback |

### Pattern #28 Multi-Provider AI Abstraction (candidate v19)

Skyvern strengthens Pattern #28:
- v19 TrendRadar — LiteLLM 100+ providers
- **v24 Skyvern — 8 explicit providers + OpenAI-compatible-endpoints-catch-all**

### Cross-framework multi-provider comparison

| Framework | Provider abstraction |
|-----------|---------------------|
| TrendRadar v19 | LiteLLM (100+) |
| multica v15 | 8 models BYO |
| **Skyvern v24** | **8+ providers native** |
| Other T5 | Single or few providers |

Pattern #28 candidate strengthens; still N=2 explicit framework-level abstraction.

## 4. Installation methods

### Option 1 — pip (recommended)

```bash
pip install skyvern
skyvern quickstart
```

### Option 2 — Docker Compose

```bash
pip install skyvern && skyvern quickstart
# Select "Docker Compose" when prompted
# Access at http://localhost:8080
```

### Option 3 — Managed Cloud (app.skyvern.com)

- No infrastructure setup
- Parallel execution
- Anti-bot detection
- Proxy networks
- CAPTCHA solvers

### Requirements

- Python 3.11.x (3.12 compatible, 3.13 unsupported)
- Node.js + npm
- Windows: Rust + VS Code C++ dev tools

## 5. Integrations + authentication

### Password managers

| Manager | Support |
|---------|---------|
| Bitwarden | ✅ Supported |
| Custom HTTP credential service | ✅ Supported |
| 1Password | ❌ Unsupported |
| LastPass | ❌ Unsupported |

### 2FA methods

- **QR-based** (Google Authenticator, Authy)
- **Email-based**
- **SMS-based**

### Workflow platforms

- **Zapier** — SaaS automation integration
- **Make.com** — visual workflow integration
- **N8N** — OSS workflow integration

### Observation

**First corpus framework with explicit password-manager integration (Bitwarden).** 2FA support breadth is novel.

## 6. Browser support

- **Chrome/Chromium only** — via CDP (Chrome DevTools Protocol)
- Chrome 136+ requires workaround for user data
- No Firefox/Safari mentioned

### Observation

**Narrower browser support than raw Playwright** (which supports Firefox + WebKit). Skyvern is vision-specialized on Chromium ecosystem.

## 7. Telemetry + governance

### Telemetry

- **Enabled by default**
- **Opt-out:** `SKYVERN_TELEMETRY=false`

### Governance

- `CONTRIBUTING.md` exists
- "Help Wanted" issues labeled
- PR/issues welcome
- Discord community

### Pattern #23 AI-Disclosure Policy (candidate)

Skyvern has telemetry-disclosure (data collection opt-out), not AI-disclosure policy. Pattern #23 doesn't test.

## 8. Skyvern Cloud — proprietary anti-bot moat

### What's in Cloud, not OSS

- **Anti-bot detection** — bypasses commercial bot-detection systems
- **Parallel execution** — distributed browser pool
- **Proxy networks** — IP rotation
- **CAPTCHA solvers** — automated CAPTCHA handling

### Commercial positioning

> *"anti-bot measures available in our managed cloud offering"*

### Pattern implications

- **#31 Open-Core Commercial Entity** — OSS core + proprietary Cloud tier (N=2 with fish-speech v20)
- **#48 candidate (NEW v24): Proprietary-Anti-Bot Commercial Moat** — specific differentiator

### Why anti-bot matters

Browser automation on commercial websites (e.g., booking sites, e-commerce) increasingly faces bot-detection (Cloudflare Turnstile, Akamai, reCAPTCHA). OSS users hit these; Cloud users don't (Skyvern-AI's moat).

## 9. Cross-T5 deployment comparison

| Framework | OSS deployment | Managed/cloud tier |
|-----------|----------------|---------------------|
| deer-flow v9 | Docker Compose + K8s | ByteDance internal (not public) |
| autoresearch v10 | Local Python (single GPU) | None (solo project) |
| paperclip v14 | pip + Docker | None disclosed |
| **Skyvern v24** | **pip + Docker Compose** | **Skyvern Cloud (app.skyvern.com)** |

**Skyvern = first T5 with explicit paid managed cloud tier.** Different commercial model than deer-flow (internal) or autoresearch (research) or paperclip (no commercial).

## 10. Key observations

### Cluster-level

- **10+ workflow blocks** = comprehensive automation surface
- **8+ LLM providers native** = strong multi-provider (Pattern #28 data point)
- **3 install paths** (pip / Docker / Cloud) — lean vs LlamaFactory's 5+ paths
- **Bitwarden + 2FA integration** = novel corpus-first
- **Skyvern Cloud anti-bot moat** = open-core commercial differentiator

### Cross-corpus

- **Pattern #31 Open-Core Commercial Entity** → N=2 with Skyvern, candidate for promotion
- **Pattern #28 Multi-Provider AI Abstraction** → strengthens as candidate (8+ native)
- **Password-manager integration** = first corpus observation
- **Skyvern Cloud = first T5 paid managed tier**

## 11. References

- Parent: [[(C) index]]
- Source: README installation + integrations + cloud sections
- Sibling clusters: [[(C) README + positioning + benchmarks cluster summary]] + [[(C) Commercial-entity + AGPL + anti-bot moat cluster summary]]
- T5 peers: deer-flow v9 + autoresearch v10 + paperclip v14

---

**Cluster summary: 10+ workflow builder blocks + 8+ LLM providers (OpenAI/Anthropic/Bedrock/Gemini/Ollama/OpenRouter/Azure/OpenAI-compatible) + 3 install paths (pip/Docker/Cloud) + Bitwarden + 2FA + Zapier/Make/N8N integrations. Skyvern Cloud anti-bot proprietary moat (Pattern #31 open-core). First T5 with paid managed tier.**

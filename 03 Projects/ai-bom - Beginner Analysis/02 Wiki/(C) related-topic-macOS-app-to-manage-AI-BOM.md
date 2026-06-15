# (C) Related topic — "a macOS app to manage an AI Bill of Materials" (v156)

> **Operator-requested related topic** (alongside the `Trusera/ai-bom` subject). **Headline finding: no dedicated native macOS app to manage AI-BOMs exists** (as of 2026-06). The space is **CLI tools + commercial web platforms**, all runnable *on* macOS but none *native* to it. So this page is a **landscape + gap analysis**, not a wiki of an existing product. Honest framing throughout.

> **↪ See also — broader landscape + ranking:** [`00 Notes/(C) AIBOM-tool-landscape.md`](../../../../00%20Notes/(C)%20AIBOM-tool-landscape.md) — a verified ranking of ~10 AIBOM tools (cdxgen, snyk/agent-scan, Cisco aibom, OWASP generator, Trusera/ai-bom, msaad00/agent-bom, …) + the definitive macOS-app verdict (still none) + a best-Mac-front-end-substrate ranking. Built 2026-06-05 from a 20-repo verification sweep (74 candidates).

## 1. What an AI-BOM is (the concept)
An **AI Bill of Materials (AI-BOM / AIBOM)** is a complete, structured inventory of every component in an AI system: **models, training datasets, prompts, software dependencies, agent frameworks, MCP servers, model configs, version history, pipelines, and third-party services**. It is the AI-specific extension of the software SBOM.

**Why it exists now (the regulatory driver):**
- **EU AI Act, Article 53** (obligations from Aug 2025) — requires a complete AI-component inventory/technical documentation for general-purpose AI.
- **NIST AI Risk Management Framework (AI RMF)** — detailed records of AI components, usage, and risk profiles.
- **CISA/NTIA SBOM lineage + OWASP** — AI-BOM extends the established SBOM minimum-elements work into the AI domain.

**The standards it serializes into:**
- **CycloneDX 1.6** — added ML-BOM / model-card support; the de-facto AI-BOM serialization (OWASP Dependency-Track compatible).
- **SPDX 3.0** — SPDX with AI/dataset profiles.
- **SARIF 2.1.0** — for CI/code-scanning surfacing.

## 2. The tool landscape (2026-06)
| Tool | Type | Form factor | Notes |
|---|---|---|---|
| **Trusera/ai-bom** (this wiki's subject) | OSS | **CLI + Flask web dashboard + Docker + VS Code ext + n8n node** | scans code/containers/cloud → CycloneDX/SPDX/SARIF; Apache-2.0 |
| **Cisco AI Defense — AI BOM** | Commercial + an OSS tool | Web platform (+ open-source component) | "know your AI stack," incl. how assets are orchestrated in agentic workflows |
| **Mend.io** | Commercial | Web platform | auto-detects models/agents/RAGs/MCPs; **live, continuously-updated AI-BOM**; policy enforcement at scale |
| **Snyk / JFrog / Wiz / Cycode / Sysdig / Palo Alto** | Commercial | Web platforms / SaaS | AI-BOM/AI-security modules; cloud-native, dashboard-driven |

**None of these is a native macOS application.** They are CLIs and web platforms.

## 3. The macOS angle — how you'd "manage an AI-BOM" on a Mac today
There is **no native macOS app** (no `.app`, no menu-bar/tray manager, no Mac App Store entry) dedicated to managing AI-BOMs. On a Mac you manage AI-BOMs by:
1. **`pipx install ai-bom` → `ai-bom scan .`** — the CLI runs natively on macOS (Python 3.10+).
2. **`ai-bom dashboard`** — ai-bom's own **Flask HTML dashboard** in the browser (the closest thing to a "manage" GUI; it's web, not native).
3. **`docker run … ghcr.io/trusera/ai-bom scan /scan`** — Docker Desktop on macOS.
4. **VS Code extension** (`trusera.ai-bom-scanner`) — inline in the editor on macOS.
5. **Commercial web consoles** (Mend/Snyk/etc.) — in the browser.

So "manage AI-BOM on macOS" = **CLI + browser dashboard**, not a native Mac experience. That is the gap.

## 4. The gap — what a native macOS AI-BOM manager *would* be (and the corpus connection)
This is an **opportunity/gap**, not an existing product — flagged as such. A genuinely native macOS app to manage AI-BOMs would plausibly be:
- a **menu-bar / tray app** that re-scans on a schedule and surfaces a glanceable count + risk badge for "AI components in my projects,"
- with **diff-over-time** (what AI got added/removed since the last scan), **per-project CycloneDX/SPDX export**, and **drift/alert** on new high-risk components or leaked keys,
- driving the `ai-bom` CLI / `trusera-sdk` underneath (an open-core wrapper).

**Corpus connection — this is a recognizable shape:** the vault's last three ships are *native-desktop management/monitoring surfaces for AI coding tools* —
- **v153 ai-switcher** — a **native-macOS Tauri** control-plane (accounts/quota for Claude Code/Codex/Antigravity),
- **v154 agentpet** — a **native-macOS Swift** menu-bar monitor of multiple coding agents,
- **v155 openpets** — a cross-platform **Electron** desktop pet showing live agent status.

A "macOS app to manage AI-BOM" would be **the governance-layer analog** of those: a native-desktop surface, but for the *supply-chain-inventory/governance* layer instead of orchestration/observability. The building blocks the corpus already catalogs are all present — a Tauri/Swift/Electron shell (v153/v154/v155) wrapping a scanner CLI (v156 ai-bom) with scheduled re-scan + ambient status. That nobody has shipped it yet is the genuinely interesting finding.

## 5. Honest caveats
- **No such macOS app exists** — this is gap/landscape analysis, not a product wiki (clearly flagged).
- The landscape facts above are from web sources (Wiz/Cycode/Snyk/JFrog/Sysdig/Mend/Palo Alto/Cisco guides) **as of 2026-06**, NOT API-verified; vendor capabilities change.
- ai-bom's "dashboard" is a **Flask web** dashboard, not a native macOS GUI — do not overstate it as a Mac app.

## Sources
- [Trusera/ai-bom](https://github.com/Trusera/ai-bom)
- [AI-BOMs: A Practical Guide | Wiz](https://www.wiz.io/academy/ai-security/ai-bom-ai-bill-of-materials)
- [AIBOM: The Complete Guide | Cycode](https://cycode.com/blog/ai-bill-of-materials/)
- [Your Guide to AIBOMs | Snyk](https://snyk.io/articles/ai-security/ai-bill-of-materials-aibom/)
- [What is an AIBOM? | JFrog](https://jfrog.com/learn/ai-security/aibom/)
- [What is an AIBOM? | Sysdig](https://www.sysdig.com/learn-cloud-native/what-is-ai-bill-of-materials-aibom)
- [Creating an AI-BOM for Secure GenAI | Mend.io](https://www.mend.io/blog/what-is-an-ai-bill-of-materials-ai-bom/)
- [What Is an AI-BOM? | Palo Alto Networks](https://www.paloaltonetworks.com/cyberpedia/what-is-an-ai-bom)
- [Introducing AI BOM in Cisco AI Defense | Cisco Blogs](https://blogs.cisco.com/ai/know-your-ai-stack-introducing-ai-bom-in-cisco-ai-defense)
- [What Is an AI Bill of Materials? | BizTech Magazine](https://biztechmagazine.com/article/2026/05/what-ai-bill-materials)

# (C) AIBOM tool landscape — repos to manage an AI Bill of Materials

> **What this is:** a durable landscape + ranking of open-source **AI Bill of Materials (AIBOM / AI-BOM)** tools — the genre of `Trusera/ai-bom` and `msaad00/agent-bom` — plus the adjacent agent/MCP-security and general-SBOM tooling, viewed through the **"a macOS app to manage AIBOM"** lens.
> **Built:** 2026-06-05, from a verification workflow (29 agents · 74 candidates discovered · **20 repos independently verified** · 6 discovery angles → per-repo provenance → hand-synthesised ranking).
> **⚠️ Provenance note on `Trusera/ai-bom` + `msaad00/agent-bom`:** these two were analysed in depth on an **unmerged side branch** (`wiki/v157-agent-bom`) and are **NOT corpus-numbered** here — on `main` the v156/v157 slots are different subjects (clawd-on-desk / ClaudeBar). This note is filed **standalone** (no version, no Pattern-Library state change); treat the ai-bom/agent-bom analysis as held-pending, not shipped.
> **⚠️ METRICS (§37.4):** this environment **mocks the GitHub API** — every ★/fork/commit/release figure below is **page-stated (read off the rendered repo page), NOT API-verified.** Stars are an especially weak signal here (e.g. msaad00/agent-bom: ~2,351 commits / 111 releases but ~22★). Treat all numbers as directional and possibly stale.

---

## Bottom line first
- **There is NO native macOS app to manage an AIBOM.** Verified across 20 repos + 74 candidates: not one is a `.app` / menu-bar / tray manager. "Manage AIBOM on a Mac" today = **a CLI + a web dashboard in your browser.** Closest Mac-flavoured things are tangential: `cdxgen` can do macOS *hardware* HBOM (not AIBOM), and `snyk/agent-scan` runs on macOS as a CLI. A native-Mac AIBOM manager is a genuine, unfilled **build opportunity**.
- **Strongest tools overall** are `cdxgen` (standards workhorse, OWASP) and `snyk/agent-scan` (most-adopted, Snyk) — both bigger/more-proven than the two anchor repos. `Trusera/ai-bom` is a solid mid-tier dedicated scanner; `msaad00/agent-bom` is the most *interesting design* but the least *proven*.
- **If the real goal is "build a Mac app to manage AIBOM,"** the tool to *wrap* is one with a clean REST/MCP API — **msaad00/agent-bom** (63-tool MCP server + REST) or **cisco-ai-defense/aibom** (FastAPI) — not the highest-starred one.

---

## Overall ranking (AIBOM-relevant tools)
Criteria = **AIBOM fit × maturity/backing × adoption × "manage" surface.** Re-rank by your priority using the dimension tables below. (★ = page-stated, NOT API-verified.)

| # | Repo | ★ | Backing | Why here |
|---|---|---|---|---|
| 1 | [cdxgen/cdxgen](https://github.com/cdxgen/cdxgen) | ~989 | OWASP/CycloneDX | The standards workhorse — 7-yr mature (v12.6.0), first-class `aibom` command (+8 BOM types), CycloneDX+SPDX, REST server (:9090), Homebrew/Winget. **Caveat: general-purpose — AI is 1 of 8 BOM types.** |
| 2 | [snyk/agent-scan](https://github.com/snyk/agent-scan) | ~2,575 | Snyk | **Most-adopted.** Inventories agent components (harnesses/MCP/skills) across Claude Code/Cursor/Windsurf/Gemini/Codex/VS Code/Amazon Q + 15+ threat scans; runs on macOS/Linux/Win. **Caveat: NOT a true AIBOM — JSON only (no CycloneDX/SPDX/SARIF), Snyk-token-gated, no own API/MCP/dashboard.** |
| 3 | [cisco-ai-defense/aibom](https://github.com/cisco-ai-defense/aibom) | ~89 | Cisco AI Defense | **Best DEDICATED, full-infra AIBOM.** 23 scanners, 30 AI component types, 3-tier detection (deterministic + xref + mandatory-LLM agentic), CycloneDX-ML/SPDX-3.0/SARIF + HTML dashboard + FastAPI + policy engine + EU-AI-Act/OWASP-Agentic/NIST-AI-RMF mappings. **Caveat: LLM-enrichment mandatory; newer (v0.x).** |
| 4 | [Trusera/ai-bom](https://github.com/Trusera/ai-bom) | ~246–258 | Trusera (open-core) | Dedicated AIBOM; 13 scanners, 9 formats; **widest delivery surface** (CLI/Docker/GH-Action/n8n-node/VS-Code-ext/SDKs + dashboard). Detects MCP, **does not serve one** (confirmed — see discrepancy log). |
| 5 | [GenAI-Security-Project/aibom-generator](https://github.com/GenAI-Security-Project/aibom-generator) (OWASP) | ~75 | OWASP GenAI | The **official OWASP AIBOM generator**; CycloneDX 1.6 + completeness scoring + **hosted web app** (owasp-genai-aibom.org). **Caveat: Hugging Face *models* only — no agents/MCP/infra.** *(`aetheris-ai/aibom-generator` is the same project under another org handle.)* |
| 6 | [msaad00/agent-bom](https://github.com/msaad00/agent-bom) | ~22 | solo | **Richest architecture** — scanner + 63-tool MCP server + runtime gateway + blast-radius graph; full standards output; **the best Mac-front-end substrate.** **Caveat: solo, pre-1.0 (v0.88), ~22★/0 watchers (engagement-deficit-extreme).** |
| 7 | [idlab-discover/aibomgen-cli](https://github.com/idlab-discover/aibomgen-cli) | ~6 | OWASP-ecosystem | Go CLI: scans repos for Hugging Face model/dataset usage → CycloneDX AIBOM; has a companion dashboard + GH Action. **Caveat: HF-specific, AGPL-3.0, pre-1.0.** |
| 8 | [SecAI-Hub/ai-model-bom](https://github.com/SecAI-Hub/ai-model-bom) | unknown | solo | Go; model-FILE-scoped AIBOM (.gguf/.safetensors/.pt) + Ed25519 signing + attestation + REST daemon. **Caveat: model-only (no agent/MCP traversal); nascent (~3 commits).** |
| 9 | [vinzabe/ai-bom-generator](https://github.com/vinzabe/ai-bom-generator) | ~0 | solo | Python; CycloneDX 1.5 ML extension + **pickle-malware scanner** + Ed25519/sigstore signing. **Caveat: nascent, 0★.** |
| 10 | [jasebell/ai-bill-of-materials](https://github.com/jasebell/ai-bill-of-materials) | ~13 | solo | A **schema/template proposal only** (TeX/Bibtex), not a working generator; stale since Oct 2023. Historical/conceptual. |

---

## Grouped view (apples-to-apples)

### A. Dedicated AIBOM generators
`cisco-ai-defense/aibom` (89★, best-in-class) · `Trusera/ai-bom` (~246★, widest distribution) · `GenAI-Security-Project/aibom-generator` (OWASP, 75★, HF-models-only, has web GUI) · `msaad00/agent-bom` (22★, richest design) · `idlab-discover/aibomgen-cli` (6★, HF Go CLI) · `SecAI-Hub/ai-model-bom` (model-file + signing) · `vinzabe/ai-bom-generator` (0★, ML + pickle-malware).

### B. Adjacent heavyweights (stronger tools, different shape)
`cdxgen/cdxgen` (989★, general BOM gen w/ first-class `aibom`) · `snyk/agent-scan` (2,575★, agent inventory + security — *not* a standards AIBOM).

### C. Agent / MCP security & registry (supply-chain adjacent, NOT AIBOM generators)
[`cisco-ai-defense/mcp-scanner`](https://github.com/cisco-ai-defense/mcp-scanner) (962★, MCP threat scanner — YARA + LLM-as-judge + VirusTotal) · [`Agent-Threat-Rule/agent-threat-rules`](https://github.com/Agent-Threat-Rule/agent-threat-rules) (254★, "Sigma-for-agents" detection-rule format, 651 rules, ships an MCP server, in production at Microsoft/Cisco/MISP) · [`NimbleBrainInc/mpak`](https://github.com/NimbleBrainInc/mpak) (6★, MCP package registry + L1–L4 trust scoring + 25 controls).

### D. General SBOM / CycloneDX tooling (AI-BOM as a variant, not AI-first)
[`anchore/syft`](https://github.com/anchore/syft) (9,108★, the big general SBOM scanner) · [`CycloneDX/cyclonedx-cli`](https://github.com/CycloneDX/cyclonedx-cli) (506★, analyse/merge/diff/convert) · [`CycloneDX/sbom-utility`](https://github.com/CycloneDX/sbom-utility) (141★, validate/query/manage incl. ML-BOM) · [`CycloneDX/cyclonedx-python`](https://github.com/CycloneDX/cyclonedx-python) (378★) · [`protobom/protobom`](https://github.com/protobom/protobom) (326★, SBOM interchange lib) · [`CycloneDX/specification`](https://github.com/CycloneDX/specification) (517★, the ECMA-424 standard itself — defines AI/ML-BOM; not a tool). *(Not AIBOM at all: `ossf/scorecard` — OSS security-health scorecard — surfaced in discovery but excluded.)*

---

## Re-ranking by the dimension that matters to you
- **Most adopted / safest bet:** snyk/agent-scan (~2,575★) → cdxgen (~989★) → cisco mcp-scanner (~962★, MCP-security). *(syft is bigger at ~9.1k★ but general-SBOM, not AIBOM.)*
- **Truest standards "BOM" artifact** (CycloneDX/SPDX you can load into Dependency-Track): cdxgen → cisco/aibom → Trusera → OWASP generator → cyclonedx-cli/sbom-utility. *(snyk/agent-scan drops — JSON only.)*
- **Best DEDICATED, full-infra AIBOM** (agents+MCP+models+cloud, not just models): **cisco/aibom → Trusera → msaad00/agent-bom.** *(OWASP + idlab + SecAI drop — model/HF-only.)*
- **Best substrate to build your macOS front-end on** (exposes REST/MCP to wrap): **msaad00/agent-bom (MCP-63-tools + REST) → cisco/aibom (FastAPI) → cdxgen (REST :9090) → OWASP generator (hosted web + REST).** *(snyk is the worst wrap-target — cloud + token-gated, no own API. Trusera has an n8n node + dashboard but no documented REST/MCP server.)*
- **Best signing / attestation** (provenance integrity): SecAI-Hub/ai-model-bom (Ed25519 + attestations) · vinzabe/ai-bom-generator (Ed25519/sigstore + pickle-malware) · cdxgen (JSF signing).

---

## ⚠️ Discrepancy log (resolved)
1. **Trusera/ai-bom "MCP server" claim — RESOLVED.** A workflow verify-agent skim-claimed Trusera ships an MCP server + REST API. A focused re-fetch confirms the opposite: Trusera **detects** MCP servers (scan target) but **does NOT serve one**, and has **no documented REST API** (it has an n8n community node + a dashboard). The verify-agent over-read (conflated "MCP scanner" + "n8n node" into "MCP Server + REST API"). The ai-bom side-branch analysis (which called it "detects MCP, does not serve") stands.
2. **snyk/agent-scan "2,575 watchers"** — a verify-agent over-read (copied the star count into the watcher field). Watchers are ~14 (direct fetch). Stars ~2,575 page-stated.
3. **Star drift:** Trusera shows ~246 vs ~258 across fetches days apart — normal page-stated drift; both NOT API-verified.

---

## Context (where AIBOM sits)
AIBOM is the **governance / supply-chain-inventory layer** of the "operate-your-agent-stack" tool family (provider-aggregation / capability / orchestration / account-mgmt / observability / ambient-status / **governance**). `Trusera/ai-bom` + `msaad00/agent-bom` form a genuine AIBOM-generator pair (independent, no fork), and this landscape shows the category is *populated* (≥7 dedicated generators) — i.e. "AI-BOM generator" is a real, recurring tool archetype, not a one-off. *(Any corpus Pattern-Library promotion of that archetype is a separate audit decision, not asserted here — this note is standalone.)*

## Unverified candidates worth a future look (dropped at the 22-repo verify cap)
From the 74 discovered, these AIBOM/agent-relevant ones were NOT verified (capped out): `snyk-labs/ai-bom-scan`, `HTS-ASPM/aibom`, `anthonyharrison/mlbomdoc`, `apisec-inc/mcp-audit`, `NuGuardAI/xelo`, `konjoai/squash`, `iron-kite/rudor`, `sktelecom/sbom-tools`, `kusari-oss/mikebom`, `Nanako0129/TokenBar` (possibly a Mac menu-bar *token* tracker — adjacent, not AIBOM). Verify before relying on any.

## Method footnote
Workflow `aibom-landscape-verify` (run `wf_eec05bf2-ba2`): 6 parallel discovery angles → 22 repos verified in parallel (20 succeeded; `CycloneDX/cyclonedx-go` failed "prompt too long") → auto-synth agent failed "prompt too long" → ranking hand-synthesised from verified records + one focused Trusera re-fetch. All metrics page-stated (GitHub API mocked, §37.4).

# (C) Firecrawl — Pilot Methods Menu (24 methods)

*LLM Wiki v214 · 2026-07-17 · `firecrawl/firecrawl`*
*Blunt framing: Firecrawl is a genuinely useful, directly-pilotable web-data layer for Goal #1, and a real-but-fenced Goal-#2 (hireui) play. The value ladder runs read-and-learn → borrow-zero-install → hands-on-on-public-data → hireui-behind-a-legal-fence → personal → vault-meta. **The one thing that governs every hireui method: web scraping of anything candidate-adjacent is a PII + ToS + GDPR gray zone — a data-residency/legal review gates it, and self-host to keep data local.***

**⭐ One-thing path: A1 → C11 → D16.**

---

## A — Read & learn (zero risk, zero install)

- **A1 ⭐** Read the endpoint design (scrape/crawl/map/search/extract/interact/agent/batch) as a case study in *how a web-data capability is factored for agents* — note that `search` returns full page content (not just links) and `extract` is schema-driven JSON. Internalize the "arbitrary web → clean markdown that preserves heading hierarchy → chunk/embed" pipeline that makes it a RAG default.
- **A2** Read the **agent-nativity stack** (REST API + 9 SDKs + first-party MCP server + Firecrawl Skill) as the exemplar for "expose one capability to every harness" — the fullest such stack in the corpus. Compare to geti v213 (Skill-only) and palmier-pro v192 (MCP-only).
- **A3** Read the **open-core split** (AGPL-3.0 engine + paid cloud + MIT SDKs) as a business-model reference; map what's OSS vs cloud-only from the README's "Open Source vs Cloud" comparison.
- **A4** Map Firecrawl against **crawl4ai v29** (self-run library, data sovereignty) and **Jina Reader** (zero-friction, prepend `r.jina.ai/`) — a decision matrix of *hosted-service vs library vs micro-API* for the vault's own web-research needs.

## B — Borrow patterns (zero install, into the vault / hireui specs)

- **B5 ⭐** Steal the **"clean-markdown-that-preserves-hierarchy for chunking"** discipline into the vault's own web-research + RAG notes: when Claude ingests web content, prefer structured markdown over raw HTML (the "structured-surface-not-raw-dump" thread — browser-use v41 / page-agent v199 text / PixelRAG v211 pixels / Firecrawl markdown).
- **B6** Borrow the **`extract`-against-a-schema** pattern for hireui's future data-ingestion: never free-text-parse a page; define a JSON schema and extract to it (deterministic, testable).
- **B7** Borrow the **`interact`-before-`extract`** discipline (click/scroll/wait to reach content) as the design note for any hireui flow that must reach data behind interaction.
- **B8** Borrow the **AGPL-vs-MIT split awareness** into hireui's dependency policy: depend on the MIT SDKs freely; never fork+self-serve the AGPL engine into a product without a license review.
- **B9** Borrow the **first-party-MCP + Skill + SDK** distribution shape as the template for how hireui would eventually expose its *own* capabilities to agents (composes with the palmier-pro v192 `ToolExecutor` MCP template + geti v213 skill-suite template).

## C — Hands-on trial (low risk, on PUBLIC non-sensitive data)

- **C11 ⭐** `install-snapshot` → `npm-security-check firecrawl-py` (or the Node SDK) → get a `firecrawl.dev` API key → **scrape one public docs page → markdown** and one **`extract`-to-schema** call, in a scratch dir. Prove the loop on non-sensitive public data.
- **C12** Install the **`firecrawl-mcp-server`** against a scratch Claude Code session (env-var API key) and have Claude research one public topic through it — measure the token cost of the returned markdown vs raw HTML.
- **C13** Install the **Firecrawl Skill** (Claude Code / OpenCode) and compare the Skill path vs the MCP path vs a direct SDK call for the same scrape.
- **C14** Try the **self-hosted OSS** engine in Docker on a scratch machine (no cloud key) → confirm it works air-gapped, note the AGPL obligations, and benchmark it vs the cloud for one crawl.
- **C15** Bake-off Firecrawl vs **crawl4ai v29** (self-run) vs **Jina Reader** on the same 3 pages — cost, markdown quality, JS-heavy-page success. Feeds the A4 decision matrix.
- **C16** Test the **`agent` endpoint** (`spark-1-mini` vs `spark-1-pro`) on one open-ended research task — is the "describe-it-in-English → it searches+retrieves" worth the credits vs orchestrating scrape+search yourself?

## D — hireui / Goal #2 (behind the legal + residency fence)

- **D16 ⭐** Spec a **hireui public-web enrichment slice** on an `agent-*` branch: given a company's public site, `extract` a structured company profile (industry / size / tech-stack) to a JSON schema — **gated by a data-residency + ToS review**; **self-host** so scraped data stays local; **no candidate PII** scraped without legal sign-off. Design/spec only (hireui has no LLM spend yet → build-it-right).
- **D17** Write the **data-residency + ToS ADR** for any hireui web-scraping: cloud (egresses queries + content to Firecrawl) vs self-host (local, AGPL). Candidate-adjacent data → self-host or don't.
- **D18** Compose with **career-ops v200 / miai-cv-matching**: if hireui ever ingests public job-market or company data to *explain* a match, Firecrawl is the ingestion layer feeding the Match-Explain rubric — behind the same fence.
- **D19** A **robots.txt / copyright / GDPR compliance checklist** as a hard gate in hireui's scraping pipeline (the README's own "respect websites' policies" made enforceable, not advisory).
- **D20** Feed Firecrawl-scraped **public company docs** into a hireui RAG index for recruiter-facing context (never candidate PII) — schema-validated, source-cited, local index.

## E — Off-goal / personal

- **E21** Use Firecrawl (or Jina Reader for zero-friction) as your personal **web→markdown reader** for feeding the vault's own research (public sources only).
- **E22** Build a small **watch-a-page-for-changes** script (map + scrape on a schedule) for tracking public docs of tools the vault studies — read-only, public.

## F — Vault-meta / audit

- **F23 ⭐** File the **§C standalone at N=2** ("Web-Crawl / Web-Data-to-LLM-Ready-Markdown Capability Layer for Agents"; crawl4ai v29 + Firecrawl v214) + the **NO-MINT reviewable alternative** + the **Scrapling-v149-as-possible-N=3** audit question for the ~v221 audit.
- **F24** Record the **corpus-recursive-dependency** data-point (Firecrawl was a dependency of rowboat v43 / awesome-llm-apps v201 / claude-seo v64 before becoming a subject) — the GitNexus-v33-in-cortex-hub-v181 shape; a watch-axis for "now-subjects that earlier subjects depended on."
- **F25** Write the **web-reach-for-agents taxonomy** synthesis: federated-platform-read+search (Agent-Reach v174) vs arbitrary-open-web-crawl-to-markdown (crawl4ai v29 / Firecrawl v214) vs browser-automation-action (browser-use v41 / Skyvern v24) vs stealth-browser-server (camofox v179) vs local-doc-conversion (markitdown v28) vs screenshot-RAG (PixelRAG v211) — the sharpest cross-cut in the corpus's web-capability neighborhood.

---

### Fence (mandatory for any hands-on / hireui method)
`install-snapshot` before install · `npm-security-check` the SDK · **public non-sensitive data first** · **candidate-adjacent data → self-host + a data-residency/legal review, or don't** · AGPL-3.0 core = productization-blocker (depend on MIT SDKs, don't fork+serve the engine) · respect robots.txt/ToS/copyright/GDPR (enforce, don't advise) · pin `firecrawl-py` / v2.11.0 · hireui per its CONSTITUTION (I-2 `agent-*` branch / I-8 operator-installs / GitNexus-first; design/spec only).

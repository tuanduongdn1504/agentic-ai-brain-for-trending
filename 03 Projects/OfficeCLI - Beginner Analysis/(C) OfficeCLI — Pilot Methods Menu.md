# (C) OfficeCLI — Pilot Methods Menu

> LLM Wiki **v206** · `iOfficeAI/OfficeCLI` · 24 ways to apply it, low→high commitment.
> ⭐ **One-thing path: A1 → C12 → D17** (read the SKILL.md disciplines → scratch offer-letter `{{key}}` merge → a hireui offer-letter-generation slice on an `agent-*` branch).
> **Standing fence (applies to every C/D method):** `install-snapshot` first → inspect `install.sh` (prefer a manual binary or a pinned package-manager install over `curl|bash`) → `npm-security-check` `@officecli/sdk` / `officecli-sdk` before any SDK install → scratch dir before any real data → **review what OfficeCLI writes into your agent configs** (it auto-installs a skill file + MCP config) → **candidate PII never leaves the machine without a residency decision** → hireui work per its CONSTITUTION (I-2 `agent-*` branch / I-8 operator-installs / GitNexus-first) → pin **v1.0.136**.

---

## A — Read & learn (zero risk, zero install)

- **A1 ⭐** Read the `SKILL.md` (`curl -fsSL https://officecli.ai/SKILL.md`) as an **agent-capability-design case study** — the three-layer "prefer higher layers" discipline, help-first anti-hallucination, verify-after-changes, the render-and-verify loop, the specialized-sub-skills loader. ~3,500 words, ~20 min.
- **A2** Read it as a **template for how to package a capability three ways at once** (MCP server + auto-installed cross-harness SKILL.md + SDKs) — the reference model for making *any* hireui capability agent-native.
- **A3** Compare OfficeCLI's approach to **Anthropic's own `docx`/`xlsx`/`pptx` skills** (available in this very vault session) — same job (Office-doc manipulation for Claude), different delivery (Anthropic-internal Python skills vs a standalone deterministic renderable cross-harness CLI). Note what each does better.
- **A4** Read the render-and-verify loop (`watch` + `validate` + `view issues`) as the **maker/checker discipline applied to document output** — the same shape as the vault's loop-verifier and video-use v198's self-eval.

## B — Borrow patterns (zero-install, into the vault / hireui specs)

- **B5** Put the **render-and-verify rule** in `CLAUDE.md` / any hireui LLM-feature spec: *"an agent that produces a document (or any renderable artifact) must render + validate it before claiming done."* Highest-ROI steal.
- **B6** Steal the **help-first anti-hallucination rule** (*"ALWAYS run help instead of guessing property names/formats"*) into the vault's agent-discipline notes — it's the deterministic-tool analogue of career-ops v200's anti-fabrication rule (B5 there).
- **B7** Adopt the **three-layer "prefer higher layers" progressive-disclosure** pattern as a design principle for any hireui tool surface (semantic API first, raw fallback last).
- **B8** Adopt **deterministic JSON-with-consistent-schemas + `--json`** as the contract for any hireui agent tool (no regex extraction) — pair with the mosh-ai vendor-seam thread.
- **B9** Note the **resident-mode / batch / round-trip-dump** trio as the token/latency-economy pattern for multi-step document workflows (→ the claude-api-cost-optimization thread).

## C — Hands-on scratch trials (low-risk, throwaway dir)

- **C10** `install-snapshot` → install the binary (manual download preferred over `curl|bash`) → `officecli --help` → render a sample `.docx` to HTML/PNG and confirm the agent can "see" it.
- **C11** Register the MCP server against a **scratch** Claude Code project (`officecli mcp claude`), inspect the tool surface, and drive one `view`/`get`/`query` on a sample document.
- **C12 ⭐** **Offer-letter merge on a scratch dir:** take a `.docx` with `{{name}}`/`{{role}}`/`{{salary}}` placeholders + a JSON of values → template-merge → render + `validate`. This is the exact low-risk first hireui slice, rehearsed on fake data.
- **C13** **CV parsing on a sanitized `.docx`:** `view`/`get`/`query` a fake résumé into structured JSON (name/experience/skills sections). Measure how deterministic the extraction is vs an LLM-only parse.
- **C14** **Spreadsheet analytics smoke test:** build an `.xlsx` with 350+-formula auto-eval + a pivot table from a fake candidate-pipeline range; confirm the formula engine computes on write.
- **C15** Measure the **token/tool-call economy** of a multi-step edit with resident mode ON vs OFF (pairs with the ccusage/OTel observability pilot).

## D — hireui / Goal-#2 (behind the CONSTITUTION fence — the real payoff)

- **D16** **CV-ingestion slice:** on an `agent-*` branch, prototype reading an uploaded candidate `.docx` résumé → deterministic structured JSON → feed the candidate-summary / Match-Explain LLM feature (composes with the miai-cv-matching + career-ops v200 D16 threads). Sanitized/consented data only.
- **D17 ⭐** **Offer-letter generation slice:** a `{{key}}`-template `.docx` → merge candidate/role data → render + `validate` before send → human-in-loop approval. The lowest-risk, highest-value first hireui document feature; template-driven, deterministic, no free-text LLM in the legal path.
- **D18** **Pipeline/scorecard `.xlsx` export:** generate recruiter analytics (time-to-fill, stage funnels, interview scorecards) with the formula/pivot engine — a deterministic reporting feature, no LLM spend.
- **D19** **Client one-pager / shortlist `.pptx`:** generate a candidate-shortlist deck from structured data (the specialized "pitch decks" sub-skill) — an outbound artifact for TalentAxis GTM.
- **D20** **Wire the render-and-verify gate into hireui's doc pipeline:** any generated document must render + `validate` + pass a schema check before a human sees it (the B5 rule, productized).
- **D21** **Candidate-PII residency ADR:** decide where document bytes + extracted PII live (OfficeCLI runs local → PII need never egress) — mirror the local-AI-coding-agents / google-ai-studio residency ADRs. Gate D16–D19 behind it.

## E — Personal / off-goal

- **E22** Use OfficeCLI + Claude Code as your own **"generate this report/deck/spreadsheet from a spec"** assistant for vault admin / TalentAxis ops (audit docs, review summaries → `.docx`/`.xlsx`).
- **E23** Evaluate **AionUi** (the org's Cowork sibling, ~30k★) separately as a multi-CLI Cowork surface — a cross-ref to the operating-niche, not a dependency of this pilot.

## F — Vault-meta

- **F24** File the **"agent capability-layer surface taxonomy"** synthesis for the ~v212 audit: web (Agent-Reach v174) / mobile-simulator (serve-sim v183) / stealth-browser (camofox v179) / in-page-GUI (page-agent v199) / file-search (fff v194) / browser-automation (browser-use v41) / **Office-documents (OfficeCLI v206)** — and re-confirm the OfficeCLI NO-MINT alternative (Office-vertical-of-the-family) vs the minted surface-boundary reading. Also queue the markitdown-v28 (conversion) ↔ OfficeCLI-v206 (authoring) direction pair as the document-handling contrast.

---

### The pragmatic recommendation

OfficeCLI is the **sharpest product-capability pilot for hireui since serve-sim v183** — recruiting *is* document I/O (résumés in; offer letters, reports, decks out). But it's a **capability you wire into a product**, so start read-only and template-driven: **A1 → C12 (scratch offer-letter merge) → D17 (a hireui offer-letter slice on an `agent-*` branch)**, gated behind **D21 (the PII-residency ADR)**. Keep free-text LLM out of the legal/offer path (deterministic template-merge only); let the render-and-verify gate (D20) be the safety net. hireui has no LLM spend yet → build-it-right, don't retrofit.

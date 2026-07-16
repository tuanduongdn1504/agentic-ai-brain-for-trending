# (C) OfficeCLI — Deep Dive

> LLM Wiki **v206** · subject `iOfficeAI/OfficeCLI` · built 2026-07-16 · GOAL-ALIGNED INCLUDE 3/4 · **1 NEW §C standalone at N=1 (CORPUS-FIRST for the Office-document surface, NOT world-first)** · counts 46/11 UNCHANGED.
> Verdict + pattern accounting → `(C) OfficeCLI — Verdict.md`. Pilots → `(C) OfficeCLI — Pilot Methods Menu.md`.
> ⚠️ **Source-provenance:** this wiki is **WebFetch/DeepWiki/SKILL.md-verified, NOT source-cloned.** The C# internals (rendering-engine fidelity, the 350+-formula evaluator, resident-mode metrics, the MCP protocol code) are page/doc/DeepWiki-stated, not read from the source tree. The load-bearing corpus claims (collision-cleanness, goal-alignment, the mint, identity, landscape) ARE hand-verified. See "What I verified vs didn't."

---

## 1. What it is, in one line

`iOfficeAI/OfficeCLI` — tagline **"OfficeCLI is the world's first and the best Office suite designed for AI agents"** / **"Give any AI agent full control over Word, Excel, and PowerPoint — in one line of code."**

A **single, self-contained binary** that lets an AI agent **create, read, and modify Microsoft Office documents** (`.docx` / `.xlsx` / `.pptx`) **with no Microsoft Office installed** — via a built-in HTML/PNG rendering engine (so the agent can *see* and verify what it produced), a 350+-function Excel formula evaluator + native pivot tables, a three-layer Read→DOM→Raw-XML command surface, resident mode, and deterministic JSON I/O. It ships **as an agent capability three ways at once**: a built-in **MCP server** (Claude Code / Cursor / VS Code / LM Studio), an **auto-installed `SKILL.md`** (Claude Code / Cursor / Windsurf / GitHub Copilot), and **Python + Node SDKs**.

- **License:** Apache-2.0
- **Language:** C# 94.6% / Shell 4.0% / other 1.4%
- **Version:** v1.0.136 (2026-07-14) · **130 releases**
- **Stars:** ~18.1k (repo page) — ⚠️ SkillsLLM lists ~8.4k; the two conflict → **page-stated, §37.4, NOT a Pattern #52 claim** · ~1.2k forks
- **Author/org:** **iOfficeAI** (GitHub org "AionUi", bio *"AI on UI"*, `officecli.ai` / `aionui.com`) — **anonymous** (no public members), **NOT Anthropic**
- **i18n:** ships a `README_zh.md` (Chinese)

This is the **corpus's first Office-document creation+manipulation capability layer for AI agents.** It sits squarely on the vault's Goal #1 (agent capability substrate) and is **directly, sharply pilotable into hireui** (a recruitment SaaS: resumes in, offer letters / candidate reports / pipeline spreadsheets / client decks out).

---

## 2. Identity & provenance

- **iOfficeAI = an anonymous, independent org** — the GitHub org "AionUi" (bio *"AI on UI"*, 581 followers, `aionui.com`, X `@AionUi`). **No public members; no location; no disclosed individual founders; no Anthropic connection stated.** This is a **bare-org author** — the DeusData v172 / Jo-Inc v179 situation.
- **A serial AI-agent-infra builder.** Beyond OfficeCLI (C#, ~18k★) the org ships:
  - **AionUi** (TypeScript, ~30k★) — *"Free, local, open-source 24/7 Cowork app for OpenClaw, Hermes Agent, Claude Code, Codex, OpenCode, Gemini CLI and 20+ more CLI."* (A multi-CLI Cowork GUI — a cross-ref to the vault's operating-niche + Anthropic Cowork; **not a corpus subject**.)
  - **AionCore** / **aionrs** (Rust — *"a multi-provider AI agent CLI with tool orchestration"*), **AionHub** (agent/skill/assistant extension hub), forked `gemini-cli-pro`, forked `echarts`.
- **Chinese-language i18n present** (`README_zh.md`) — a neutral fact; per routine §41 this is **not an (a)-rescue** (no name/heritage/locale inference), and it is not load-bearing on any claim here.

**Bottom line on identity:** a capable, prolific, anonymous non-Anthropic org. Clean **(a) FAIL** — the tier keys on **(b)**.

---

## 3. Architecture — the three-layer document model

OfficeCLI structures every document operation across three abstraction levels, and the embedded `SKILL.md` teaches agents to **"always prefer higher layers"** (progressive disclosure — drop to raw XML only for edge cases):

| Layer | Purpose | Commands |
|---|---|---|
| **L1 — Read / Inspect** | Semantic content views | `view`, `get`, `query`, `validate` |
| **L2 — DOM operations** | Structured, path-addressed element edits (`/slide[1]/shape[2]`) | `get`, `query`, `set`, `add`, `remove`, `move`, `swap`, `batch`, find/replace, clone |
| **L3 — Raw XML** | Direct XPath / OpenXML-part access as a universal fallback | `raw`, `raw-set` |

**Per-format coverage (DeepWiki-stated):**
- **Word (`.docx`)** — paragraphs, runs, tables, headers/footers, **Content Controls (SDT)**, watermarks, **Table of Contents**, RTL-language support.
- **Excel (`.xlsx`)** — a built-in evaluator with **350+ formulas auto-evaluated on write**, sheet management, conditional formatting, data validation, and **native pivot-table generation from source ranges** (README-asserted; DeepWiki's extract did not surface pivot internals → flagged page-stated).
- **PowerPoint (`.pptx`)** — slides, shapes, animations, transitions, plus a specialized rendering engine for interactive HTML previews.

---

## 4. The four engineering distinctives (why it isn't "just another python-docx wrapper")

1. **Built-in HTML/PNG rendering engine — the agent can SEE its output.** OfficeCLI converts `.docx`/`.xlsx`/`.pptx` to **high-fidelity HTML and PNG** so an agent can *verify* layout rather than emit blind OpenXML. This is the **render-and-verify / maker-checker discipline** (the vault's own loop-verifier, video-use v198's self-eval, the ai-web-design redesign-gate) applied to **document output**. The `watch` command gives a **live browser preview with auto-refresh + click-to-select** (click an element, then `get <file> selected`).

2. **Formula & pivot engine.** A real Excel evaluator (350+ functions, auto-computed on write) + native pivot tables — most competitor Office-MCP servers are thin `openpyxl` wrappers that don't evaluate formulas.

3. **Single self-contained binary, no Office, no Python.** C# native binary for Windows/macOS/Linux. Competitors are typically Python processes needing `python-docx`/`openpyxl`/`python-pptx` and sometimes a real Office install (COM automation on Windows/macOS).

4. **Deterministic JSON I/O.** Every command supports `--json` with **consistent schemas** → agents parse reliably **without regex extraction**. Plus **resident mode** (a `ResidentServer` background process, ~60s idle timeout) so multi-step edits don't pay disk-I/O per call, **batch operations**, and **round-trip dump** (serialize a whole document to replayable JSON).

---

## 5. The agent-facing surface — three delivery channels

OfficeCLI is delivered **as an agent capability**, not just a CLI a human types:

- **Built-in MCP server** — `officecli mcp claude`, `officecli mcp cursor`, `officecli mcp vscode`, … registers a JSON-RPC MCP server for **Claude Code, Cursor, VS Code, LM Studio**. (A clean **Pattern #18 sub-archetype B / B1-MCP** instance — one server, many clients.)
- **Auto-installed Agent Skill (`SKILL.md`)** — the tool **auto-detects AI environments** (Claude Code, Cursor, Windsurf, GitHub Copilot) and installs its skill file; agents can also pull it live via `curl -fsSL https://officecli.ai/SKILL.md` (→ `raw.githubusercontent.com/.../main/SKILL.md`). (**Cross-harness distribution — Pattern #84 84c** — but NOT the ponytail-v168 14-platform generator mechanism: OfficeCLI distributes ONE skill + ONE MCP server that many harnesses consume.)
- **SDKs** — Python `pip install officecli-sdk`, Node `npm install @officecli/sdk` — thin resident-pipe SDKs that **auto-provision the native CLI when missing**.

### The `SKILL.md` (~3,500 words) — the on-goal gold

Opening: *"AI-friendly CLI for .docx, .xlsx, .pptx. Single binary, no dependencies, no Office installation needed."* Its disciplines are directly borrowable into any agent workflow:

- **Help-first / anti-hallucination:** *"When unsure about property names, value formats, or command syntax, ALWAYS run help instead of guessing."*
- **Three-layer discipline:** *"Always prefer higher layers"* (progressive disclosure).
- **Verify-after-changes:** run `validate` and `view issues` after every edit.
- **Render-and-verify loop:** `watch` for live preview + click-to-select.
- **Resident-mode + flush-boundary hygiene** (save only before a non-OfficeCLI program touches the file).
- **Specialized sub-skills loader** — format-specific rule packs the agent activates on demand (academic papers, pitch decks, financial models, Morph animations).

---

## 6. Installation

```bash
# Unix/Linux/macOS
curl -fsSL https://raw.githubusercontent.com/iOfficeAI/OfficeCLI/main/install.sh | bash
# Windows PowerShell
irm https://raw.githubusercontent.com/iOfficeAI/OfficeCLI/main/install.ps1 | iex
# Package managers
brew install officecli   # scoop install officecli   # npm i -g @officecli/sdk (auto-provisions the binary)
# or download a platform binary from GitHub Releases
```

⚠️ **Supply-chain / attack-surface note (#66):** the primary install is a `curl|bash` / `irm|iex` pipe; the SDKs **auto-provision the native binary** (pip/npm fetch and run it); and the tool **auto-detects AI environments and writes a skill file + MCP config into them.** For a tool that reads and writes your documents and edits your agent configs, that is a real install-time surface — offset by Apache-2.0 (auditable) and no stated telemetry, but it earns a fence (see the Pilot Menu).

---

## 7. Landscape — corpus-first, NOT world-first

The **"world's first and best Office suite for AI agents"** tagline is **marketing**: the Office-document-for-agents space is **already populated** (all landscape-stated):

- `office-mcp` (create_docx/edit_docx/create_xlsx/create_pptx over python-docx/openpyxl)
- `jenstangen1/pptx-xlsx-mcp`, `vAirpower/macos-office365-mcp-server` (COM automation, Claude/Cline)
- `lingfan36/ai-office-mcp` (**"358 measured tools"** across PPT/Excel/Word on Windows)
- `ForLegalAI/mcp-ms-office-documents`, the **openpyxl MCP server**, `trsdn/markitdown-mcp`

Most of these are **single-format Python MCP wrappers**. OfficeCLI's genuine differentiators against the field: **one self-contained C# binary** (no Python/Office), a **rendering engine** (see-your-output), a **real formula/pivot evaluator**, a **three-layer unified surface across all three formats**, and **cross-harness distribution** (MCP + auto-installed SKILL.md + SDKs). It is plausibly the **most comprehensive / most-starred** instance of the class — but **not the first, and "best" is unverifiable.**

**Corpus-wise, it IS first:** a by-hand grep of `_state/` + `_patterns/` + `03 Projects/` returns **no prior OfficeCLI / iOfficeAI / AionUi subject and no Office-document-manipulation subject.** The only adjacent corpus subject is **markitdown v28** (`microsoft/markitdown`) — which converts Office/PDF documents **→ markdown for LLM ingestion** (read-only, one-way). OfficeCLI is the **opposite direction and larger scope**: full create/read/modify authoring + rendering. And **Anthropic's own `docx`/`xlsx`/`pptx` skills** (the closest *conceptual* peer — Office-doc manipulation for Claude, Python-based, internal) are exactly what OfficeCLI is a standalone, deterministic, renderable, cross-harness open-source alternative to.

---

## 8. Facts & metrics (with provenance)

| Fact | Value | Provenance |
|---|---|---|
| License | Apache-2.0 | repo page |
| Language | C# 94.6% / Shell 4.0% | repo page |
| Version / releases | v1.0.136 (2026-07-14) / 130 releases | repo page §37.4 |
| Stars / forks | ~18.1k / ~1.2k (⚠️ SkillsLLM: ~8.4k — conflict) | page-stated §37.4 → NOT #52 |
| Excel functions | "350+" | README / doc-stated (not source-verified) |
| SKILL.md length | ~3,500 words | fetched |
| MCP clients | Claude Code, Cursor, VS Code, LM Studio | README |
| Skill auto-install harnesses | Claude Code, Cursor, Windsurf, GitHub Copilot | README |

**⚠️ The environment mocks the GitHub API (§37.4)** — stars/forks/dates are **page-stated, not API-verified** → **no viral-velocity (#52) claim.** The star figure additionally **conflicts across pages** (18.1k vs 8.4k).

---

## 9. What I verified vs didn't (honesty note)

**Hand-verified (load-bearing):**
- **Collision-cleanness** — file-routed grep of `_state/` + `_patterns/` + `03 Projects/` for OfficeCLI / iOfficeAI / AionUi = **0 hits**; a `markitdown` sanity grep = **6 hits** (proving the grep works, defeating the flaky-shell stdout-drop that produced a false-empty on the first two attempts).
- **The office-document surface is corpus-first** — no prior `.docx`/`.xlsx`/`.pptx` manipulation subject; markitdown v28 is the conversion-direction contrast.
- **The §C capability-layer cluster** (Agent-Reach v174 / serve-sim v183 / camofox v179 / page-agent v199 / browser-use v41 / fff v194) read from the registry — **no Office surface** among them.
- **Identity** — WebSearch + org WebFetch (iOfficeAI/AionUi anonymous, non-Anthropic).
- **Landscape** — WebSearch (populated MCP-server space → NOT world-first).
- **What the tool does + how it's delivered** — repo page + raw README + SKILL.md + DeepWiki.

**NOT verified (flagged, non-load-bearing):**
- The **C# source was not cloned/read.** Rendering-engine fidelity, the 350+-formula evaluator internals, resident-mode latency metrics, pivot-table generation, and the MCP protocol code are **page/doc/DeepWiki-stated.** The verdict does **not** hinge on these internals — it hinges on *what the tool does, how it's delivered, and that it's collision-clean*, all of which are verified. (c) STRONG is recorded **with this caveat foregrounded.**

---

## 10. Why it matters for the two goals

- **Goal #1 (master Claude + autonomous agents for software dev):** OfficeCLI is a clean study in **agent capability-layer design** — three-channel delivery (MCP + auto-installed cross-harness SKILL.md + SDKs), the render-and-verify discipline, deterministic JSON, progressive-disclosure layering, help-first anti-hallucination. Claude Code is a **first-class target.**
- **Goal #2 (hireui):** This is the **sharpest product-capability pilot since serve-sim v183.** hireui is a recruitment SaaS, and Office documents are core to recruiting: **CVs/résumés come in as `.docx`; offer letters, candidate one-pagers, and client reports go out as `.docx`/`.pdf`; pipeline analytics and interview scorecards live in `.xlsx`; candidate shortlists and client pitches ship as `.pptx`.** OfficeCLI gives hireui's future agent a deterministic, renderable, no-Office-install way to do all of that — with a template-merge (`{{key}}`) path for offer letters that is exactly the low-risk first slice.

**One-thing path:** A1 (read the SKILL.md's disciplines) → C-tier (scratch: parse a sample CV `.docx`, generate an offer letter from a `{{key}}` template) → D-tier (a hireui offer-letter-generation slice on an `agent-*` branch, per hireui's CONSTITUTION). See the Pilot Methods Menu.

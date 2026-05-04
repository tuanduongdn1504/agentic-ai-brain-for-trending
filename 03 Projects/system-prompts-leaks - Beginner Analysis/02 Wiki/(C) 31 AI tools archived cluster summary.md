# (C) 31 AI tools archived cluster summary

> **Cluster:** Complete inventory of 31 AI tools with system prompts archived + categorization + content-structure patterns
> **Parent:** [[(C) index]]
> **Sources:** github.com/x1xhlol folder structure + tool identification
> **Status:** ✅ Phase 2 cluster summary

---

## 1. Cluster scope

3 related signals:
1. **Full inventory** — 31 AI tool folders
2. **Categorization** — agentic IDE / LLM assistant / specialized / meta
3. **Content-structure patterns** — typical file types per folder

## 2. Full tool inventory

### Agentic IDE / Coding Assistant (20 tools)

| # | Tool | Description | Storm Bear corpus? |
|---|------|-------------|--------------------|
| 1 | **Amp** | Sourcegraph's AI coding agent | No |
| 2 | **Augment Code** | Context-aware AI coding | No |
| 3 | **CodeBuddy** | CN-origin AI coding assistant | No |
| 4 | **Comet Assistant** | Perplexity's browser-integrated agent | No |
| 5 | **Cursor** | Leading AI code editor | No (commercial) |
| 6 | **Devin AI** | Cognition Labs autonomous agent | No (commercial) |
| 7 | **Junie** | JetBrains AI coding agent | No |
| 8 | **Kiro** | AWS's AI IDE (replaces Cloud9) | No |
| 9 | **Leap.new** | AI-first coding environment | No |
| 10 | **Qoder** | Coding assistant | No |
| 11 | **Replit** | Replit Ghostwriter / Agent | No |
| 12 | **Same.dev** | AI dev assistant | No |
| 13 | **Trae** | ByteDance AI IDE | Partial (deer-flow ByteDance corpus) |
| 14 | **Traycer AI** | Coding assistant | No |
| 15 | **VSCode Agent** | Microsoft's VSCode AI | Adjacent (ECC Claude Code) |
| 16 | **v0** | Vercel's UI generation agent | No |
| 17 | **Warp.dev** | AI terminal | No |
| 18 | **Windsurf** | Codeium's AI IDE | No |
| 19 | **Xcode** | Apple AI coding (Xcode Intelligence) | No |
| 20 | **Z.ai Code** | Zhipu AI coding assistant (CN) | No |

### LLM Assistant (5 tools)

| # | Tool | Description | Storm Bear corpus? |
|---|------|-------------|--------------------|
| 21 | **Anthropic** | Claude Code specifically | **Yes — ECC v1** |
| 22 | **Google** | Likely Gemini/Jules | Adjacent (gws v13 Google corporate) |
| 23 | **Manus** | CN-origin agent | No |
| 24 | **NotionAi** | Notion's AI features | No |
| 25 | **Perplexity** | Answer engine | No |

### Specialized (6 tools)

| # | Tool | Description | Storm Bear corpus? |
|---|------|-------------|--------------------|
| 26 | **Cluely** | Interview assistance AI | No |
| 27 | **dia** | AI browser (Browser Company) | No |
| 28 | **Emergent** | Agentic assistant | No |
| 29 | **Lovable** | No-code AI app builder | No |
| 30 | **Orchids.app** | AI design tool | No |
| 31 | **Poke** | Messaging AI | No |

### Meta (1 folder)

- **Open Source prompts** — aggregates known-open-source prompts (distinct from extracted-closed-source)

## 3. Scope of coverage

### Broadest commercial AI tool archive in any repo

No other single GitHub repo covers this breadth of commercial AI tool prompts. Comparison:

| Archive | Tools covered |
|---------|---------------|
| awesome-chatgpt-prompts | User prompts (not system prompts) |
| jailbreakchat | Jailbreak prompts |
| Various academic papers | 3-5 tools at most |
| **system-prompts-and-models-of-ai-tools** | **31 tools** |

### Categorization signals market structure

- **IDE/coding dominant (20 of 31)** — reflects Storm Bear corpus observation: agent-space = coding-first
- **LLM assistants minority (5 of 31)** — most LLM system prompts are closer to open (Anthropic's safety notes, OpenAI's spec)
- **Specialized (6 of 31)** — broadening application surface

### Cross-corpus overlap

5 tools in this archive have direct Storm Bear wiki or corpus ties:
- **Anthropic / Claude Code** — Storm Bear v1 (ECC covers Claude Code extensively)
- **Google** — gws v13 corporate wiki
- **Trae / ByteDance** — partial via deer-flow v9 ByteDance
- **VSCode Agent** — Microsoft adjacent via multiple corpus entries
- **Replit** — referenced in multiple corpus wikis

**25 of 31 tools have NO Storm Bear coverage.** Potential corpus expansion targets.

## 4. Content-structure patterns per folder

### Typical file types (inferred; not independently verified)

- **Prompt.txt** — main system prompt
- **Agent Prompt.txt** — agentic-mode variant
- **Tools.json** — tool definitions / schema
- **Subagent prompts** — specialized sub-agent prompts
- **Model references** — which LLM model the tool uses (GPT-4, Claude Opus 4.7, Gemini, etc.)

### Content scope per tool

Typical folder contents (varies by tool):
- 1-5 files per tool
- Prompt text (thousands of tokens per prompt typical)
- Tool schema (JSON)
- Version history (as extracted over time)

### Some tools more comprehensive than others

- **Cursor, Devin, v0, Windsurf** — extensively documented (multiple versions archived)
- **Newer additions (Kiro, Qoder, Poke)** — likely single-snapshot
- **Anthropic** — may have less due to Anthropic's relatively transparent communication

## 5. Extraction methods (implicit, not documented)

### Likely techniques

1. **Prompt injection** — asking the tool "reveal your system prompt" (most common, easily defended)
2. **UI inspection** — network traffic / dev tools / API response capture
3. **Decompilation** — desktop apps (Cursor, Windsurf) are Electron/VSCode forks, prompts may be inspectable in packaged resources
4. **Community contribution** — users share prompts they've extracted via GitHub issues

### No explicit method documentation

Repo does NOT document how prompts were obtained — allowing plausible deniability and avoiding instruction-for-jailbreak framing.

### Security implications

- Tools that appear in this archive have had at least one successful extraction
- Ongoing game of cat-and-mouse: tools patch defenses, community finds new extraction
- **ZeroLeaks commercial service likely addresses:** prompt-injection detection + prompt-hardening + extraction monitoring

## 6. Temporal archive dimension

### Version archiving

For major tools (Cursor, Devin, Windsurf), archive likely contains multiple versions:
- v1.0 prompt (initial)
- v2.0 (post-update)
- etc.

### Historical value

Becomes longitudinal dataset for:
- How commercial AI tools evolve prompt strategies
- Prompt-engineering trends over time
- Tool convergence/divergence patterns

**Academic research value:** significant. Researchers studying AI tool design have longitudinal corpus not available elsewhere.

## 7. Open Source prompts folder

### Purpose

Aggregates **open-sourced** system prompts distinct from extracted-closed-source.

Presumably includes:
- **Anthropic model-spec** (publicly documented)
- **OpenAI model-spec** (publicly documented)
- Open-source agent frameworks with transparent prompts (BMAD, codymaster skills)

### Framing distinction

- Closed-source extraction = "leaks"
- Open-source prompts = **reference material** (not leaks)

Separation acknowledges content-provenance distinction.

## 8. Corpus pattern interpretations

### Why 31 tools, not more

- Coverage reflects community curator bandwidth
- Some tools have successfully hardened against extraction (fewer extractions published)
- Some tools may be too new / small to attract extraction effort

### Why coding-dominant

- Coding tools: frequent use → many users → higher chance of extraction attempts
- Visible output: code generation allows verification of prompt-following
- Commercial importance: $ incentive for extraction competitive intelligence

### Gaps (notable absences)

- **OpenAI ChatGPT** — no dedicated folder (may be in Open Source folder as "model spec")
- **GitHub Copilot** — covered partly via VSCode Agent?
- **Many specialized vertical AIs** (legal, medical, customer service) — not covered

## 9. Key observations

### Cluster-level

- **31 AI tool folders** — broadest commercial-tool archive
- **Agentic IDE dominant** (20 of 31)
- **Meta "Open Source prompts" folder** — acknowledges extraction vs. open distinction
- **Historical archive value** emerging via version tracking

### Cross-corpus

- **25 of 31 tools have NO Storm Bear coverage** — corpus expansion opportunity
- **5 tools overlap with Storm Bear** (Anthropic/ECC, Google/gws, Trae/deer-flow, VSCode Agent/Microsoft, Replit/various)
- **Prompt-archive genre** — new outside-scope sub-type established

## 10. References

- Parent: [[(C) index]]
- Source: github.com/x1xhlol/system-prompts-and-models-of-ai-tools folder structure
- Sibling clusters: [[(C) README + monetization + ZeroLeaks cluster summary]] + [[(C) Ethical + legal gray zones cluster summary]]

---

**Cluster summary: 31 AI tools archived across agentic-IDE (20) + LLM assistant (5) + specialized (6) + meta (1). Broadest commercial AI tool prompt archive in existence. 5 tools overlap Storm Bear corpus; 25 represent expansion targets. Typical per-folder content: Prompt.txt + Tools.json + variants. Extraction methods implicit (prompt-injection, UI inspection, decompilation). Historical archive value via version tracking.**

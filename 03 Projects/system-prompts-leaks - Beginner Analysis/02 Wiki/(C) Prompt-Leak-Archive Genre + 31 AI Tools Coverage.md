# (C) Prompt-Leak-Archive Genre + 31 AI Tools Coverage

> **Type:** Entity — genre definition + content scope
> **Parent:** [[(C) index]]
> **Sources:** Repo folder structure + 31-tool inventory
> **Status:** ✅ Phase 3 entity page

---

## 1. Summary

system-prompts-and-models-of-ai-tools establishes a **new genre in Storm Bear corpus**: prompt-leak-archive. 3rd outside-scope sub-type (after education-aggregator v8 and foundation-model v20). Archives system prompts extracted from **31 commercial AI tools** (20 agentic IDE + 5 LLM assistant + 6 specialized + 1 meta-OSS folder). **Broadest commercial AI tool coverage in any single GitHub repository.** 5 of 31 tools overlap with Storm Bear corpus (primarily Anthropic/ECC); 25 represent potential corpus expansion targets.

## 2. Key claims

1. Prompt-leak-archive = 3rd outside-scope genre in Storm Bear corpus
2. 31 AI tools archived = broadest commercial-tool coverage in any repo
3. Agentic IDE dominant (20 of 31) — reflects coding-first agent-space
4. 5 of 31 tools overlap Storm Bear corpus (Anthropic, Google, Trae, VSCode Agent, Replit)
5. Pattern #38 candidate formalized (prompt-leak-archive genre)
6. Version-archival dimension creates longitudinal research value

## 3. Evidence + sources

| Claim | Source | Confidence |
|-------|--------|-----------|
| 31-tool count | Folder structure enumeration | High |
| Agentic IDE 20/31 | Tool-identification categorization | High |
| Corpus overlap 5 tools | Cross-reference Storm Bear 20 wikis | High |
| Broadest commercial coverage | Market survey | Medium (no systematic comparison with other archives) |
| Longitudinal value | Version-archiving inference | Medium (not independently verified) |

## 4. Genre definition: Prompt-Leak-Archive

### Defining features

1. **Content = extracted system prompts** (not authored prompts)
2. **Sources = closed-source commercial AI tools** (not open-source)
3. **Archive format = folder-per-tool** (not mixed aggregation)
4. **Legal position = gray zone** (extraction + redistribution contested)
5. **Author typology = pseudonymous or security-research community** (common)
6. **Monetization = patronage + commercial derivative** (when present)

### Distinction from related genres

| Genre | Content | Legal position |
|-------|---------|----------------|
| **Open source prompt libraries** | Authored + shared | Clear (MIT/Apache licenses) |
| **Prompt engineering tutorials** | Examples + patterns | Clear (educational) |
| **Prompt marketplace** | Commercial user prompts | Clear (marketplace TOS) |
| **Jailbreak repositories** | Adversarial prompts | Gray (TOS violation) |
| **Prompt-leak-archive** | Extracted proprietary prompts | **Gray (copyright + TOS + trade secret)** |

### Pattern #38 candidate formalized

**Formal statement:**
> "Prompt-leak-archive genre: repositories aggregating system prompts extracted from closed-source commercial AI tools. Distinct from authored-prompt libraries, tutorials, marketplaces, and jailbreak archives. Characterized by (a) content = extracts not originals, (b) sources = closed-source commercial, (c) legal position = gray, (d) author = often pseudonymous, (e) monetization = patronage + commercial derivative when present."

**Evidence at v21:** 1 (system-prompts-leaks v21)

**Required for promotion:** 2+ similar archives.

**Prediction:** May remain rare due to legal-complexity barriers, but related genres (leaked training data, leaked benchmark data) may emerge.

## 5. 31-tool inventory by category

### Category 1: Agentic IDE / Coding (20 tools)

Includes mainstream commercial tools:
- **Mainstream:** Cursor, Windsurf, Copilot (VSCode Agent), v0
- **Autonomous agents:** Devin AI, Replit (Ghostwriter/Agent)
- **Professional IDE AI:** Junie (JetBrains), Xcode (Apple)
- **Enterprise:** Kiro (AWS), Amp (Sourcegraph)
- **Terminal:** Warp.dev
- **CN-origin:** Trae (ByteDance), CodeBuddy, Z.ai Code (Zhipu)
- **Various:** Augment Code, Comet Assistant, Leap.new, Qoder, Same.dev, Traycer AI

### Category 2: LLM Assistant (5 tools)

- **Anthropic** (Claude Code specifically)
- **Google** (likely Gemini / Jules / Vertex AI code assistants)
- **Manus** (CN-origin agent)
- **NotionAi** (Notion's AI features)
- **Perplexity** (answer engine)

### Category 3: Specialized (6 tools)

- **Cluely** (interview assistance — controversial)
- **Dia** (The Browser Company's AI browser)
- **Emergent** (agentic assistant)
- **Lovable** (no-code app builder)
- **Orchids.app** (AI design)
- **Poke** (messaging AI)

### Category 4: Meta (1 folder)

- **"Open Source prompts"** — aggregates publicly-disclosed prompts (Anthropic model-spec, OpenAI model-spec, open agent frameworks)

## 6. Cross-Storm Bear overlap

### 5 of 31 tools overlap corpus

| Tool | Storm Bear wiki | Overlap type |
|------|-----------------|--------------|
| **Anthropic / Claude Code** | ECC v1 | Deep (Claude Code is center of ECC wiki) |
| **Google** | gws v13 | Adjacent (Workspace CLI covers Google ecosystem) |
| **Trae** | deer-flow v9 (partial — both ByteDance) | Adjacent (ByteDance-family, not same tool) |
| **VSCode Agent** | ECC v1 (adjacent) + spec-kit v17 (Microsoft-family) | Adjacent (Microsoft ecosystem) |
| **Replit** | None direct | Indirect (mentioned in multiple T1 install lists) |

### 25 tools without Storm Bear coverage

Potential corpus expansion targets:
- **Cursor, Windsurf, Devin, v0** — major agent-space commercial
- **Kiro (AWS), Junie (JetBrains), Xcode (Apple)** — enterprise IDE AI
- **Cluely, Lovable, Orchids** — specialized verticals
- **Comet, NotionAi, Perplexity, Manus** — assistant variants
- **CN-origin:** Trae, CodeBuddy, Z.ai Code, Manus — validate Pattern #18 regional hypothesis (4 CN tools in archive)

## 7. Content-structure per folder (typical)

### Expected file types

- `Prompt.txt` — primary system prompt
- `Agent Prompt.txt` — agentic-mode variant  
- `Tools.json` — tool schema definitions
- `Subagent [N] Prompt.txt` — specialized sub-agent prompts
- Model designation (often in folder README or inline)

### Content depth varies by tool

- **Cursor:** extensively documented (multiple versions)
- **Devin:** comprehensive (autonomous agent requires rich prompt)
- **v0:** extensively documented (Vercel's flagship AI)
- **Windsurf:** detailed (Codeium's flagship)
- **Anthropic:** possibly lighter (Anthropic publicly documents via model spec)
- **Newer tools (Kiro, Qoder, Poke):** single-snapshot likely

## 8. Temporal archive dimension

### Version tracking

For mature tools, archive likely contains version progression:
- v1.0 (initial extract)
- v1.5 (updated after tool iteration)
- v2.0 (major revision)
- etc.

### Historical research value

Creates **longitudinal corpus** for studying:
- How commercial AI tools evolve prompt engineering strategies
- Convergence/divergence patterns across tools
- Response to prompt-injection attempts (hardening history)
- Feature additions visible through prompt changes

**Academic value:** significant; not available elsewhere at this scale.

### Corpus science methodology implication

Storm Bear corpus could, in theory, analyze prompts extracted here for:
- How agents describe their tools
- Emotion/personality tag emergence
- Context-management strategies
- Safety rail patterns

But: would require explicit scoping + ethical review (content-provenance concerns).

## 9. What's NOT in the archive

### Notable absences

- **OpenAI ChatGPT** direct system prompt (may be in meta folder)
- **GitHub Copilot** (may be under VSCode Agent or Google folder)
- **Slack AI, Microsoft 365 Copilot** enterprise products
- **Vertical specialist tools** (Harvey, legal; Glass Health, medical; etc.)
- **Voice agents** (Retell, Vapi)
- **Search agents** (Exa, Kagi Assistant)

### Gap interpretation

Either:
- Prompts not successfully extracted yet
- Tools effectively hardened against extraction
- Community bandwidth limits
- Author curator selection bias

## 10. Edges + failure modes

### Known limitations

- **Version currency** — prompts archived become outdated as tools update
- **Extraction accuracy** — prompt-injection may yield partial or fabricated content
- **Tool authors' updates** — post-archive updates not captured
- **No verification** — no independent confirmation that archived prompts are real
- **Community contribution quality variance** — some contributions may be fabricated

### Pattern risks

- Pattern #38 (prompt-leak-archive genre) at N=1 — hypothesis until 2nd similar archive
- Coverage claim ("broadest in any repo") not systematically verified

## 11. Related concepts

- [[(C) Ethical + legal gray zones cluster summary]] — legal context for this content
- [[(C) Pseudonymous Solo + Crypto-Token Monetization]] — how archive is maintained financially
- [[(C) Outside-Scope Sub-Types + Pattern 20 Revision 3 + Storm Bear]] — outside-scope framework
- Pattern #38 (prompt-leak-archive genre) — formalized here
- Parent: [[(C) index]]

## References

- Repo folder structure
- 31-tool inventory and categorization
- Cross-Storm Bear 20-wiki reference

---

**31 AI tools archived across 4 categories (agentic IDE 20 / LLM 5 / specialized 6 / meta 1). Broadest commercial AI tool coverage in any single GitHub repo. 5 of 31 tools overlap Storm Bear corpus; 25 represent expansion targets. 4 CN-origin tools present (Trae, CodeBuddy, Z.ai Code, Manus) — Pattern #18 regional validation opportunity. Pattern #38 candidate (prompt-leak-archive genre) formalized. Temporal/version archival creates longitudinal research value. 3rd outside-scope sub-type in Storm Bear corpus.**

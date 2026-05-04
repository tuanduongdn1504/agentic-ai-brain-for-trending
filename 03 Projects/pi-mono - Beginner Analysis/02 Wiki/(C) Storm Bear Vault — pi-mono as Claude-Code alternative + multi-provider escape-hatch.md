# Storm Bear Vault — pi-mono as Claude-Code alternative + multi-provider escape-hatch

**Entity type:** Storm Bear meta-entity (25th consecutive — v10-v36)
**Role:** Per v2.1 Phase 0.9 per-wiki applicability evaluation — YES include
**Wiki version:** v1 (2026-04-23 — pi-mono wiki v1, 36th LLM Wiki)

---

## Why pi-mono is relevant to Storm Bear operator

pi-mono is the **first plausible direct alternative to Claude Code** to enter Storm Bear's corpus via the v36 wiki. Storm Bear currently runs 100% on Claude Code (Anthropic-subscription-locked) for vault maintenance, wiki generation, and agent-assisted Scrum coaching work. pi-coding-agent offers a comparable feature surface with structural differences Storm Bear should understand even if no switch is planned.

Concrete points of operator-relevance:

### 1. Multi-provider escape-hatch (pi-ai)

**The problem:** Storm Bear is locked to Anthropic. If Anthropic raises prices, deprecates features Storm Bear relies on, or experiences extended outages, there's no immediate fallback inside the Claude Code workflow.

**pi-ai as escape:** 20+ providers (Anthropic, OpenAI, Google, local vLLM/Ollama/LM Studio, etc.) with cross-provider context handoffs mid-session. Worst-case insurance: if Claude API is down, switch to GPT-5-Codex or Gemini 3 within the same session without losing conversation state.

**Action-item signal:** Install pi-coding-agent as a backup runtime. ~15 minutes of setup. Zero ongoing cost unless actively used (API-key-mode; pay-per-use on whichever provider is running).

### 2. Session export + HF publication workflow

**The problem:** Storm Bear's wikis are private Obsidian-vault markdown files. Generation sessions themselves are ephemeral (Claude Code in-session context window). There's no published artifact beyond the final wiki file.

**pi's model:** `/export` produces HTML of the whole session. `/share` uploads as private GitHub gist. `pi-share-hf` publishes redacted sessions to Hugging Face dataset. Mario personally publishes his own sessions; the flywheel is **working-out-loud + data-donation**.

**Alignment with Storm Bear "Karpathy LLM Wiki" philosophy:** Karpathy's pattern is "LLM builds wiki incrementally; compound knowledge over time." Publication of session data is adjacent — not the wiki artifact itself, but the **generative process**. Storm Bear already publishes guide-style outputs (`03 Published/`); publishing generation sessions themselves would be a new tier of transparency.

**Action-item signal:** Low priority. Experiment if Storm Bear ever ships a public tooling brand; not useful for current private-vault mode.

### 3. Agent-Skills interop via pi-skills (1.3K-star sibling)

**The problem:** Storm Bear relies on Claude Code's `skills/` directory. If Claude Code's skill system changes incompatibly (unlikely but possible), Storm Bear's skill investments are locked to that one runtime.

**pi-skills as interop:** pi-skills claims "compatible with Claude Code and Codex CLI." Skills authored via the broader Agent Skills standard work across runtimes.

**Action-item signal:** If Storm Bear builds new custom skills going forward, author them to the Agent Skills standard (not Claude-Code-specific conventions) to preserve runtime portability. Observational; confirm actual compatibility before committing.

### 4. `lgtm` / `lgtmi` governance-gate model — NOT applicable to Storm Bear today

**The observation:** Mario uses a maintainer-approval keyword gate to manage 38.9K-star contributor inbound.

**Why NOT applicable to Storm Bear:** Storm Bear's vault is private. No external contributor flow. Governance gate is solving a problem Storm Bear doesn't have.

**Future-relevance:** If Storm Bear ever publishes any asset with inbound-contributor potential (e.g., open-source skill library, Scrum-coach-prompt-template repo), the `lgtm`/`lgtmi` model is a proven-at-scale low-overhead gate worth borrowing.

### 5. Mario's libGDX → pi-mono cross-domain founder-equity transition

**The observation:** Mario leveraged 15-year game-framework reputation to bootstrap pi-mono to 38.9K in 8.5 months.

**Storm Bear analog:** Storm Bear's Scrum-coach brand equity (existing client base, VN Scrum community visibility) is **latent capital** for any future AI-tooling brand. If Storm Bear ever open-sources or publishes an AI-Scrum-coach tool, cross-domain founder-equity is a real lever — not a new insight but a pattern to recognize when the time comes.

**Action-item signal:** None today. File as strategic-reminder.

### 6. Severe caveat: MCP incompatibility

**The problem:** Storm Bear workflow may rely on MCP servers (e.g., filesystem MCP, search MCP, calendar MCP). pi explicitly excludes MCP in favor of CLI-tools-with-READMEs + Agent-Skills + custom-extensions.

**Implication:** **pi is NOT a drop-in Claude Code replacement** if Storm Bear has MCP investments. Switching would require re-implementing MCP server functionality as pi extensions (non-trivial: extensions are TypeScript modules with full ExtensionAPI; feasible but requires dev work).

**Action-item signal:** Before any serious pi pilot, audit Storm Bear's MCP dependencies. If >1 MCP server is actively used, pi is high-friction alternative. If zero MCP usage, pi is low-friction alternative.

---

## Pilot viability summary

**Verdict: MEDIUM pilot priority — NEW #3 (after spec-kit v17 + OMC v27).**

**Pros:**
- Install is one command (`npm install -g @mariozechner/pi-coding-agent`)
- MIT license + solo author + active maintenance (pushed today)
- 20+-provider unlock = real multi-cloud resilience
- Direct architectural comparison with Claude Code = educational value even if not adopted
- Mario's ecosystem (pi-skills, pi-share-hf) = multi-asset pilot surface

**Cons:**
- Solo bus factor (higher than corporate-backed; lower than solo-without-libGDX-lineage)
- EN-only docs (no VN for VN-client demos)
- Heavy learning curve (~110 user-facing primitives)
- MCP incompatibility = friction if Storm Bear has MCP investments
- 8.5-month-old project (less production track record than Claude Code)
- Heavy governance-gate for contribution-back (would need `lgtm` approval before any PR to pi-mono)

**Recommended pilot mode (2-4 hours):**
1. Install `pi-coding-agent` (~10 min)
2. Run one Scrum-doc-session with multi-provider swap (Claude → GPT → back) to test handoff (~30 min)
3. Export session to HTML + inspect artifact (~10 min)
4. Install pi-skills compatibility layer + try one cross-runtime skill (~30 min)
5. Write 1-page comparison note (pi vs Claude Code) for Storm Bear decision-log (~60 min)
6. File pilot outcome in Reviews folder

**When to pilot:** Low urgency. Run during a "routine v2.2 refactor" downtime, not during active wiki-generation work.

---

## Cross-corpus position (Storm Bear pilot ranking refresh at v36)

1. **spec-kit v17** (enterprise-corporate stability + SDD methodology) — unchanged
2. **OMC v27** (multi-runtime Scrum-ceremony alignment) — unchanged
3. **pi-mono v36 🆕** (Claude-Code alternative + multi-provider escape-hatch — NEW #3)
4. **BMAD v11** (VN translation + methodology + 45K) — drops 1 rank
5. **markitdown v28** (doc ingestion utility) — drops 1 rank
6. **crawl4ai v29** (web research utility) — drops 1 rank
7. **OpenHands v30** (SWE-agent platform) — drops 1 rank
8. **claude-howto v32** (self-onboarding meta-ROI) — drops 1 rank
9. gws v13 / 10. codymaster v12 / 11. multica v15 / 12. graphify v16 / 13. agency-agents v18 / 14. claude-hud v35 / 15. claude-code-best-practice v34 / 16. GitNexus v33

**Infrastructure-usable-today list (separate from framework-pilot):**
1. markitdown v28 (doc ingestion)
2. crawl4ai v29 (web research)
3. awesome-mcp-servers v31 (MCP server discovery)
4. gws v13 (Google Workspace CLI)
5. **pi-mono v36 🆕 (multi-provider backup coding-agent runtime)**

---

## Implications for Storm Bear routine

No direct routine changes at v36. pi-mono observations feed into:
- **Pattern Library awareness** (Pattern #18 MCP-exclusion watch; Pattern #28 refinement candidate; Pattern #69 N=2 promotion-candidate)
- **Future pilot decision** (medium priority; 2-4 hour evaluation)
- **Strategic reminder** (cross-domain founder-equity as future Storm Bear brand-equity lever)

No vault-wide workflow changes recommended from v36 observations.

---

## 25th consecutive Storm Bear meta-entity

Per v2.1 Phase 0.9, this is the 25th consecutive wiki (v10-v36) with a Storm Bear meta-entity. Justification this time:

1. pi-coding-agent is a plausible Claude-Code-alternative (operator-relevant)
2. pi-ai unlocks multi-provider escape-hatch (operator-relevant)
3. pi-skills interop signal for future skill-authorship choices (operator-relevant)
4. Mario's libGDX founder-equity transition = cross-domain-brand-equity lever (strategic-reminder relevance)
5. `lgtm`/`lgtmi` governance-gate = observable but not-currently-applicable (reserve-bank relevance)
6. HF-session-donation flywheel = philosophical-adjacent to Storm Bear's "compound knowledge" mission (reflective relevance)

**v2.1 Phase 0.9 "per-wiki applicability" is affirmed; inclusion passes threshold.**

---

## Cross-references

- Cluster: `(C) Cluster — Root README + 7-package monorepo + contribution gate.md`
- Related entities: `(C) pi-coding-agent — Flagship terminal coding harness.md`; `(C) pi-ai + pi-agent-core — Foundation libraries.md`; `(C) Mario Zechner — Austrian solo-flagship + ecosystem portfolio.md`
- Cross-wiki peers: claude-hud v35 (HIGH pilot Storm Bear relevance — plugin directly usable today); claude-howto v32 (HIGH pilot — self-onboarding meta-ROI); OMC v27 (architectural cousin); spec-kit v17 (methodology preference)

---

*(C) Claude-generated 2026-04-23 per routine v2.1.*

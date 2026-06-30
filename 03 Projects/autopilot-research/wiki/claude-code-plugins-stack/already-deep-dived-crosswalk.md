# The 7 already-deep-dived originals — crosswalk + refreshed metadata

> Seven of the 17 already have full deep-dives elsewhere in the wiki. This article is the bridge: where each lives, what *this* video adds, and refreshed `gh api` metadata (2026-06-29) where it drifted from the prior build. Don't re-deep-dive these — follow the link.

| Tool | Lives in | Prior metric | Now (2026-06-29) | What this video adds |
|---|---|---|---|---|
| Taste Skill | [[ai-web-design-workflow/_index]] | ~47.2K★ | **52,861★** | nothing new; names 3 sub-skills (image-to-code/redesign/output) |
| Awesome Design MD | [[claude-code-skills-stack/_index]] | ~94.1K★ | **94,193★** | the Airtable walkthrough; "clone the language not the site" framing |
| Playwright CLI | [[claude-code-skills-stack/_index]] | ~11.7K★ | **11,671★** | repeats the CLI-over-MCP token thesis |
| Codex Plugin | [[codex/_index]] + Storm Bear v62 | 17.8K★ (v62) | **21,835★** (+23%) | `/codex:rescue`, parallel work framing |
| Skill Creator | [[claude-code-skills-stack/_index]] + [[claude-skills/_index]] | ~156.4K★ | **156,454★** | "most important skill" (editorial) |
| Obsidian | [[claude-code-skills-stack/_index]] + [[claude-code-memory-systems/_index]] | ~38.8K★ | **38,802★** | the "fake KG vs LightRAG" framing |
| LightRAG | [[claude-code-memory-systems/_index]] (L5 mention) | — | **37,129★** | first dedicated treatment; RAG-Anything |

---

## Taste Skill — `leonxlnx/taste-skill` → [[ai-web-design-workflow/_index]]
Refreshed: **52,861★** (was ~47.2K). The adversarial pass made two corrections to *prior* coverage worth noting: (1) the **pre-flight gate count is not enumerable from the public README** — the 2026-06-20 ai-web-design build cited "62," this build's stage-1 said "54"; **neither is verifiable** from the public repo, so cite "a pre-flight anti-slop gate" without a number; (2) the stack is **framework-agnostic** (React/Vue/Svelte) using **GSAP** animations — not "React/Next + Tailwind v4 + Motion" (that was a stage-1 over-specification, refuted). This video adds nothing the Taste Skill deep-dive lacks; it just names the image-to-code / redesign / output sub-skills. **Its real rival here is [[claude-code-plugins-stack/new-design-tools-impeccable|Impeccable]]** (which adds a live visual editor).

## Awesome Design MD — `voltagent/awesome-design-md` → [[claude-code-skills-stack/_index]]
Refreshed: **94,193★**, 73–74 brand `DESIGN.md` files. This video gives the clearest *demo* (the Airtable breakdown: structure/colors/surfaces/typography/spacing/buttons) and the cleanest one-liner ("clone the design *language*, not the site"). The "Google Stitch invented `design.md`" provenance remains **unverifiable** (no official `google/stitch` repo; docs inaccessible) — consistent with the prior build. Composes with [[claude-code-plugins-stack/new-design-tools-impeccable|Impeccable]] (which *exports* `DESIGN.md` in the same format).

## Playwright CLI — `microsoft/playwright-cli` → [[claude-code-skills-stack/_index]]
Refreshed: **11,671★**. The video repeats the (correct) thesis that the CLI is more token-efficient than the Playwright **MCP**. New cautions from this build's adversarial pass: the repo's **2020 creation date is the parent project** (the *agent CLI product* launched **early 2026**); "**70+ commands**" is overstated (~40–50); and the famous "**27K vs 114K tokens (~4×)**" figure is a **third-party benchmark**, not first-party Microsoft data (the official docs say "token-efficient" qualitatively, without numbers). The prior [[claude-code-skills-stack/_index]] CLI-vs-MCP decision (default CLI for cost, MCP for high-fidelity detail) stands.

## Codex Plugin — `openai/codex-plugin-cc` → [[codex/_index]] + Storm Bear v62
Refreshed: **21,835★** (was 17.8K at Storm Bear v62 ~7 weeks ago, **+23%**). Two corrections to prior coverage: it ships **8 slash commands**, not 7 — v62 missed **`/codex:setup`** (the others: `review`, `adversarial-review`, `rescue`, `transfer`, `status`, `result`, `cancel`); and **ChatGPT *Free*** is supported (not just paid). The video's "Claude over-trusts its own code" rationale is **video speculation** — not in OpenAI's docs (the feature is documented as "pressure-test assumptions"). `/codex:transfer` (hand a Claude Code session into Codex without re-context) is a notable capability prior coverage missed.

## Skill Creator — `anthropics/skills` → [[claude-code-skills-stack/_index]] + [[claude-skills/_index]]
Refreshed: **156,454★** (repo-level; `license: null` = mixed/source-available). The video correctly frames it as Create → Eval → Improve → **Benchmark** (with-skill vs baseline + a blind comparator). Two corrections: the loop is **semi-manual**, not "auto" (you define prompts/assertions, spawn runs, review, then iterate); and "**arguably the most important skill**" is editorial with no supporting metric. Its grader/comparator = LLM-as-judge ([[prompt-evaluation/_index]]).

## Obsidian — `kepano/obsidian-skills` → [[claude-code-skills-stack/_index]] + [[claude-code-memory-systems/_index]]
Refreshed: **38,802★**. The big correction (consistent across builds): **kepano = Steph Ango is Obsidian's CEO, NOT its founder** (co-founders: Shida Li @licat / CTO, Erica Xu @silver / COO). And the skill is a **file-format tool** (markdown/bases/json-canvas/cli/defuddle), **NOT a memory or RAG system** — the "improve Claude Code memory" framing is misdirected; the memory/retrieval is the Karpathy LLM-Wiki pattern *this vault already runs*. Personal repo, not the `obsidianmd` org.

## LightRAG — `HKUDS/LightRAG` → [[claude-code-memory-systems/_index]] (L5)
First dedicated treatment (previously a passing L5 mention). **37,129★**, EMNLP 2025 (arXiv:2410.05779), dual-level graph+vector retrieval, 5 query modes, pluggable stores. **RAG-Anything** (multimodal) is now **merged into v1.5+**, not a separate extension (the video is slightly outdated). Three flags: the "**Obsidian's fake knowledge graph**" jab is a **false dichotomy** (a note-taking backlink graph ≠ a retrieval index — different jobs); "**lightweight**" applies to *architecture*, not compute (needs a capable LLM); and the perf-vs-GraphRAG edge is **contradicted by a 2025 meta-eval** (arXiv:2506.06331 — under unbiased evaluation, NaiveRAG outperforms LightRAG; E²GraphRAG reports ~100× speedup over it). **No official Claude Code skill** — integration is REST API or library embedding.

## Cross-links
- [[claude-code-plugins-stack/video-to-original-crosswalk]] — the full per-tool crosswalk
- [[claude-code-plugins-stack/source-provenance]] — every correction with evidence

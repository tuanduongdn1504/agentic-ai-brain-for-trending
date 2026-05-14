# Cluster 2 — Extraction methodology + CLAUDE.md

> **Sources:** CLAUDE.md (1.6 KB) + tools/updatePrompts.js (19.5 KB) + README "Extraction" section + tweakcc sister-tool integration

## The extraction methodology (README + tools/updatePrompts.js)

The README "Extraction" section states:

> *"This repository contains the system prompts extracted using a script from the latest npm version of Claude Code. As they're extracted directly from Claude Code's compiled source code, they're guaranteed to be exactly what Claude Code uses."*

**Mechanism:** Claude Code ships as compiled JavaScript in `@anthropic-ai/claude-code` npm package. Source code is NOT publicly available (per `anthropics/claude-code` GitHub repo description). The `tools/updatePrompts.js` script (19.5 KB JavaScript) parses the compiled JS to extract the 110+ system-prompt strings.

**Discipline:** The README notes precisely what the limitation is:

> *"Note that some prompts contain interpolated bits such as builtin tool name references, lists of available sub agents, and various other context-specific variables, so the actual counts in a particular Claude Code session will differ slightly — **likely not beyond ±20 tokens, however**."*

**±20 token tolerance** is a quantified accuracy claim — corpus-rare quantified-accuracy-disclosure for reverse-engineering tools.

## Template variables — what the prompts look like

Per the project's own CLAUDE.md:

> *"Template variables like `${BASH_TOOL_NAME}` are interpolated at runtime by Claude Code — they appear as literal strings in these files."*

**Reading the archive correctly:** A file like `tool-description-bash-overview.md` will contain literal `${BASH_TOOL_NAME}` strings rather than resolved values. The archive captures the prompt-template, not the rendered prompt. This is **methodologically rigorous** — preserves what's actually in the source code rather than guessing runtime values.

## YAML frontmatter discipline (per CLAUDE.md)

> *"The `system-prompts/` directory contains markdown files with YAML frontmatter noting the Claude Code version and template variables."*

Each of the 293 system-prompt files has YAML frontmatter recording:
- Claude Code version at which it was last observed
- Template variables present in that prompt

This is **per-file versioning** — each prompt-fragment is independently version-tracked. Corpus-rare granularity.

## CLAUDE.md verbatim (1.6 KB project instructions)

The repo's own CLAUDE.md is minimal but precise:

```
# Claude Code System Prompts

## What this repository is

System prompts extracted via script from the Claude Code npm package's compiled
JavaScript source. Maintained by Piebald AI, not by Anthropic.

## What Claude Code is

Claude Code is Anthropic's CLI tool for agentic coding. It is distributed as a
compiled npm package (@anthropic-ai/claude-code). Source code is not publicly
available. The anthropics/claude-code GitHub repository contains issues and
releases only.

## How to use these files

- Reference: Understand what prompts Claude Code uses and how they change
- Local patching: Use tweakcc to customize individual prompt pieces
- Feature requests: File issues at anthropics/claude-code/issues

## For AI agents working with this repository

- These files are extracted reference material, not modifiable source code
- Editing files here does not change Claude Code's behavior
- The system-prompts/ directory contains markdown files with YAML frontmatter
- Template variables like ${BASH_TOOL_NAME} are interpolated at runtime
- The CHANGELOG.md tracks prompt changes across Claude Code versions
```

**6 essential disciplines** encoded in 1.6 KB:

1. **Author-attribution disclosure** ("Maintained by Piebald AI, not by Anthropic") — explicit third-party stance
2. **Source-availability disclosure** ("Source code is not publicly available")
3. **Usage tiers** (Reference / Local patching / Feature requests)
4. **AI-agent-meta-instruction** ("For AI agents working with this repository") — corpus-first formal section addressed to AI agents about the meta-nature of the archive
5. **Modification-impact disclosure** ("Editing files here does not change Claude Code's behavior")
6. **File-format disclosure** (YAML frontmatter + template variables + CHANGELOG)

**Corpus-comparison with claude-seo v64's CLAUDE.md (210 lines):** claude-seo v64's is product-deep (Security Rules / Report Generation Rules / 25-skill architecture / etc.); v65's is concept-shallow but **meta-aware** (addresses the archive's reflexive nature). Both serve different purposes correctly.

## The "For AI agents working with this repository" section — corpus-significance

This is a **corpus-first formal AI-agent-meta-instruction section** in any 64-wiki corpus subject. Most subjects' CLAUDE.md addresses the agent as developer/operator; v65 addresses the agent as both consumer-of-reference AND as agent-that-might-be-confused-by-its-own-system-prompt-being-the-subject.

**Reflexivity observation:** When Claude Code itself reads this CLAUDE.md (during user invocation of skills like `/init` or general workflow), the agent reads literal documentation of its own system prompts. This is **corpus-recursive at meta-level** — sister to Pattern #57 (Recursive Corpus Reference) but at agent-self-awareness scale.

Pattern Library implication candidate: **"Agent-Self-Awareness Reference Disclosure"** — when an archive of agent-X's internals exists, agent-X reading that archive must be guided to not mistake it for its own configuration. v65 is the first observed instance.

## tools/updatePrompts.js — the extraction script (19.5 KB)

The single source-tool is a JavaScript file that:
1. Downloads latest `@anthropic-ai/claude-code` npm package
2. Parses the compiled minified JS
3. Identifies the 110+ prompt strings via pattern-matching
4. Extracts each string + YAML frontmatter metadata
5. Generates markdown files in `system-prompts/`
6. Updates CHANGELOG.md with per-version delta description
7. (Likely) computes token counts for each prompt

**Operational discipline:** "Updated within minutes of each Claude Code release" (per README) implies **automated CI/CD pipeline** — likely a GitHub Action watching npm registry for new Claude Code releases and triggering `updatePrompts.js` automatically.

**Corpus-significance:** 19.5 KB single-script extraction is **lean tooling for a massive subject** (293 files / 211 KB CHANGELOG / 110+ prompts). Sister to claude-seo v64's 30 Python scripts (different domain) — both demonstrate small-tooling-with-large-output discipline.

## tweakcc — the sister-tool patching mechanism

The README repeatedly references **tweakcc** (separately maintained by Piebald-AI at https://github.com/Piebald-AI/tweakcc):

> *"Want to **modify a particular piece of the system prompt** in your own Claude Code installation? Use **tweakcc**. It —*
> - *lets you customize the the individual pieces of the system prompt as markdown files, and then*
> - *patches your npm-based or native (binary) Claude Code installation with them, and also*
> - *provides diffing and conflict management for when both you and Anthropic have conflicting modifications to the same prompt file."*

**Functional pairing:** claude-code-system-prompts = the **observation half** (reference archive of what Claude Code uses). tweakcc = the **modification half** (patches your local installation).

The two products together form a **complete observe-and-modify stack** for Claude Code's prompts:
- Step 1: Read claude-code-system-prompts to understand what's in Claude Code
- Step 2: Use tweakcc to patch your local installation with custom variants
- Step 3: tweakcc handles diffing + conflict management when Anthropic ships changes upstream

**Corpus-rare two-product pairing**: most subjects ship as single-product or as ecosystem-portfolio (Pattern #19 ecosystem-portfolio-builder); claude-code-system-prompts + tweakcc are a **focused 2-product observe-and-modify pairing** — sub-archetype within Pattern #19 distinct from claude-seo v64's 5-product domain-vertical-ecosystem.

## Piebald — commercial product context (piebald.ai)

The README banner advertises:

> *"Check out Piebald: We've released Piebald, the ultimate agentic AI developer experience. Download it and try it out for free!"*

**Piebald.ai** = Piebald-AI's commercial product (agentic AI developer experience). The screenshot in README implies a desktop/cloud product comparable to Claude Code in scope.

**Strategic interpretation**: Piebald-AI's open-source claude-code-system-prompts + tweakcc serve dual purposes:
1. **Direct community value**: third-party reference + customization tools for Claude Code users
2. **Indirect commercial value**: position Piebald-AI as the "team that knows Claude Code at the deepest level" — credibility-building for their commercial Piebald product

This is **Pattern #19 ecosystem-portfolio-builder at corporate-org archetype** with **observation-as-marketing** strategy. Distinct from:
- gotalab v61 solo-Japanese SDD-vertical ecosystem (4 products)
- forrestchang v63 solo-engineer-commercial (2 products: karpathy-skills + Multica)
- AgriciDaniel v64 solo-individual-SEO-vertical (5 products)
- **Piebald-AI v65 corporate-org-observation-as-marketing (3 products: Piebald commercial + claude-code-system-prompts + tweakcc)**

## Repository contents map (root files)

| File | Size | Function |
|---|---|---|
| `.gitignore` | 46 B | minimal gitignore |
| `CHANGELOG.md` | 211 KB | **176-version absorption ledger** (Cluster 3 dives deep) |
| `CLAUDE.md` | 1.6 KB | minimal project instructions (verbatim above) |
| `LICENSE` | 1.0 KB | MIT (standard) |
| `README.md` | 69 KB | comprehensive guide (Cluster 1 details) |
| `system-prompts/` | dir | **293 prompt files** (Cluster 1 inventory) |
| `tools/updatePrompts.js` | 19.5 KB | extraction script (this cluster) |

**No CI config visible in root** at probe time — but per the README's "Updated within minutes" claim, CI must exist (likely `.github/workflows/` not in root or visible at probe). Corpus-typical for reference archives.

**No tests directory** — sister to claude-seo v64's 13+ governance files; v65 deliberately MINIMAL governance for reference archive (no tests needed for documentation; the source-of-truth is upstream Claude Code).

**No CONTRIBUTORS / CODE_OF_CONDUCT / CONTRIBUTING / etc.** — only LICENSE + README + CLAUDE.md as governance. Sub-archetype: **lean-governance reference archive**.

## License + intellectual stance

MIT license. Standard. But notice the **intellectual stance discipline**:

- Repository is open-source MIT
- Content is **extracted from Anthropic's closed-source product**
- Piebald-AI explicitly states "Maintained by Piebald AI, not by Anthropic"

**No copyright dispute observed** — Anthropic appears to tolerate this extraction (Piebald-AI is mentioned in Awesome Claude Code; no DMCA notices observable; Anthropic could have asked for takedown if disputed).

**Corpus-significance:** This is a **CORPUS-FIRST observation of corporate-tolerated-reverse-engineering** for an agentic-AI product. Pattern Library candidate: "Vendor-Tolerated-Third-Party-Reverse-Engineering Reference" — observational at v65; not formally registered.

Sister to claude-seo v64's external-authority-tracking (Google tolerates third-party SEO tools tracking their guidelines) — both show vendor-tolerance for third-party transparency layers.

## Extraction-as-methodology distinct from documentation-as-methodology

The defining methodological choice: **extraction-from-compiled-source** vs **documentation-by-authoring**.

| Choice | Method | Tolerance | Maintenance burden |
|---|---|---|---|
| **Documentation-by-authoring** | Read product docs + write your own version | High accuracy gap (paraphrasing drift) | Manual update per release |
| **Extraction-from-compiled-source** (v65) | Parse compiled binary; preserve verbatim | ±20 token tolerance disclosed | Single-script automation |

**Methodological rigor**: extraction-from-compiled-source has **higher accuracy guarantee** (verbatim from source code) BUT requires reverse-engineering capability (Piebald-AI built `updatePrompts.js` as proprietary expertise).

This is the **strongest observed reverse-engineering-as-discipline in corpus** — sister to v21 system-prompts-leaks (one-time leak) but with continuous-versioning + quantified-tolerance + automated-tooling making it **fundamentally different category**.

Pattern Library implication: **NEW Pattern candidate "Continuous-Reverse-Engineering Reference Archive"** N=1 stale-flagged at v65 — see Entity 2 for the formal proposal.

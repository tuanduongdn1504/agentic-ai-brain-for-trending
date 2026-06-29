# Video → Original Crosswalk

*Map of Ben AI's 8 meta-skills to their canonical sources, original URLs, customizations, and omissions.*

## Skill-to-Source Table

| Skill | Canonical Original | URL | What Ben Adds/Customizes | What It Omits/Simplifies |
|---|---|---|---|---|
| **1. Process Interviewer** | Matt Pocock's /grill-me skill + Anthropic skill-building best practices | https://github.com/mattpocock/skills / https://support.claude.com/en/articles/12512198-creating-custom-skills | Adapted grill-me's core interview loop; outputs PRD embedding Anthropic best practices; auto-checks second-brain/workspace first to avoid re-asking answered questions | Omits grill-with-docs (sister skill for CONTEXT.md + ADRs); simplifies grilling model-invoked mechanism to single-skill wrapper |
| **2. Prompt Master** | Anthropic's Prompt Improver tool (Claude Console) | https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-tools | ⚠️ Ben rebrands 'Prompt Improver' as 'Prompt Master'; may add custom UI/templates; claims to 'turn brain-dumps into structured prompts' | Unclear if Ben's version adds beyond Anthropic's 4-step enhancement (example-ID → structured-template → chain-of-thought → example-enhancement) or is purely cosmetic rebranding |
| **3. Humanizer** | Wikipedia's "Signs of AI writing" guide (8+ categories, 20+ concrete tells) | https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing | ⚠️ Encodes Wikipedia's tells (content patterns, language patterns, style, citation issues, markup) as automated linter; removes AI vocabulary per era (2023-mid-2024 vs mid-2024-2025 variants); claims customizable-to-your-style | ⚠️ Wikipedia guide not directly verified as Ben's actual source; customization mechanisms unconfirmed; implementation details not publicly accessible |
| **4. Fact Checker** | Evidence-based verification + web-cross-reference methodology (general best practice, no single canonical source) | Freeform methodology; web-search integration not formalized | Systematic verification pipeline: claim → search → evaluate sources → output true/mostly-true/unverifiable/false counts | Simplified from academic fact-checking harnesses (no inter-annotator agreement, no confidence scoring beyond categorical labels) |
| **5. Find Skills** | skills.sh Open Agent Skills Ecosystem (788,224+ total installs; ~1,000+ listed unique skills as of 2026) | https://skills.sh | Wraps skills.sh discovery in Claude skill format; surfaces leaderboard + topic navigation + trending filters within agent | ⚠️ Ben claims '91,000+ skills' (8.6× outdated); actual ecosystem 788K+ installs; skill deduplication unclear |
| **6. Front-end Slides** | Design methodology synthesis: visual hierarchy (IXD Foundation), data-ink ratio (Edward Tufte), type-scale typography, reveal.js HTML convention, animation restraint (Nielsen Norman), one-idea-per-slide (Duarte Slide:ology®) | https://ixdf.org, https://edwardtufte.com, https://reveal.js, https://duarte.com | Consolidates multi-source design frameworks into automated HTML slide generator; accepts brand guide (colors/fonts/design rules); outputs reveal.js-format with style presets (default 'neon cyber' for AI topics); CSS-variable tokenization | Omits interactivity design (beyond keyboard/presenter-notes); simplifies branding to 2-3 font + color-palette inputs; no custom reveal.js plugin architecture |
| **7. Decision Toolkit** | First-principles thinking (Farnam Street), probabilistic thinking, second-order thinking, pre-mortem (Klein & Kahneman), confirmation-bias checks (Kahneman), sunk-cost elimination, opportunity-cost analysis (Farnam Street), decision matrix MCDA, expected value (Decision Theory / Annie Duke), regret minimization (Stoic philosophy), inversion/reverse analysis (Charlie Munger) | https://fs.blog/mental-models, https://en.wikipedia.org/wiki/Decision_matrix, https://duke.annie.edu | Outputs two artifacts: markdown framework doc + interactive HTML decision wizard; guides user through 10-step flow (frame → clean-slate test → timing → stakeholders → bias checks → opportunity cost → scenarios+probabilities → verdict options → first-principles test); principle "guide, don't decide" = no recommendation, structure only | Omits advanced decision science (Monte Carlo simulation, sensitivity analysis, Bayesian networks); simplifies weighting to optional importance multipliers; no explicit stakeholder voting/consensus mechanism |
| **8. MCP Builder** | Anthropic's official `mcp-builder` skill + MCP (Model Context Protocol) spec | https://github.com/anthropics/skills / https://modelcontextprotocol.io | Invokes the official `mcp-builder` skill on a target API's docs; asks capability questions; outputs server code + a JSON snippet for the Claude config file | Ben's Circle.so / Reddit example servers aren't public; output quality unverified |

## Methodology-Derived vs. Original-Resource-Backed vs. First-Party-Built-In

### Original-Resource-Backed (Canonical Source Verifiable)
- **Skill #1 (Process Interviewer)**: Matt Pocock's /grill-me skill is verified; Anthropic best practices documented in official docs. ✓
- **Skill #3 (Humanizer)**: Wikipedia's "Signs of AI writing" exists and is comprehensive (20+ tells). ✓
- **Skill #4 (Fact Checker)**: Evidence-based verification is freeform methodology (no single canonical source, but grounded in general best practice).
- **Skill #5 (Find Skills)**: skills.sh ecosystem is real (788K+ ecosystem, not Ben's claimed 91K). ⚠️ **Outdated metric.**
- **Skill #6 (Front-end Slides)**: Distills multi-source design pedagogy (Tufte, Duarte, IXD Foundation, reveal.js). ✓
- **Skill #7 (Decision Toolkit)**: Consolidates peer-reviewed frameworks (Farnam Street, Kahneman, Munger, Annie Duke). ✓

### Methodology-Derived (Frameworks Repackaged, No Single Source)
- **Skill #2 (Prompt Master)**: ⚠️ **Anthropic's official tool is "Prompt Improver", not "Prompt Master".** Ben may have renamed or built independent wrapper. **Terminology mismatch flagged.**
- **Skill #7 (Decision Toolkit)** also here: synthesizes 10+ independent frameworks into single wizard (pre-mortem + opportunity-cost + expected-value, etc.). First-principles consolidation, not novel methodology.

### First-Party-Built-In (Anthropic Official, Not Third-Party Adaptation)
- **Skill #8 (MCP Builder)**: ✅ **VERIFIED REAL.** `mcp-builder` is a genuine Anthropic-published skill in [anthropics/skills](https://github.com/anthropics/skills) (verified 2026-06-20, alongside `skill-creator`/`pdf`/`pptx`/`xlsx`/`docx`/`frontend-design`/`claude-api`). Ben's "built-in Anthropic skill" claim is correct — the **only** first-party item in the set.

---

## Key Takeaways

- **Skills #1, #3, #5, #6, #7 are grounded in verifiable canonical sources** (Pocock, Wikipedia, skills.sh, design theory, decision science). Ben's adaptation adds convenient packaging + second-brain auto-pull orchestration.

- **Skill #2 (Prompt Master) has terminology drift**: Anthropic's official tool is "Prompt Improver" (Claude Console). Ben may have rebranded or built independent tool; no "Prompt Master" in official Anthropic Skills registry. ⚠️

- **Skill #8 (MCP Builder) IS a verified built-in Anthropic skill** (`mcp-builder` in anthropics/skills, confirmed 2026-06-20). Ben's attribution is correct.

- **Ben's "91,000 skills" claim is stale by ~8.6×**: skills.sh now hosts 788K+ total installs across ~1,000+ listed unique skills (as of 2026-06-20). Video metric appears outdated.

- **Six of eight skills encode established external lineages** ([[claude-skills/source-provenance]]): design theory, behavioral economics, decision science, interview methodology. One (Skill #8) is **flagged unverified**; one (Skill #2) **conflicts with official Anthropic naming**.

- **Skills leverage "second brain" context auto-pull** to avoid re-asking answered questions (Skill #1 pattern). Validates [[ai-operating-system/_index]] + [[claude-code-memory-systems/_index]] as load-bearing architecture for meta-skill power multiplier.

- **Ben's meta-skills favor concrete procedures over hype** — "remove Wikipedia's signs of AI" beats "unlock your potential."

---

## Source

**Video**: YouTube "8 Claude Skills I Can't Live Without" by Ben AI (@BenAI92), 2026-04-18, ~147K views, https://www.youtube.com/watch?v=bXnRA3pJavE

**Original Resources** (cited in skills + digest):
- https://github.com/mattpocock/skills (Process Interviewer baseline)
- https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing (Humanizer)
- https://skills.sh (Find Skills ecosystem)
- https://ixdf.org, https://edwardtufte.com, https://reveal.js, https://duarte.com (Front-end Slides)
- https://fs.blog/mental-models (Decision Toolkit)
- https://support.claude.com/en/articles/12512198-creating-custom-skills (Anthropic Skills best practices)
- https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-tools (Prompt Improver, not "Prompt Master")

---

## Cross-References

[[claude-skills/the-eight-meta-skills]] | [[claude-skills/original-anthropic-agent-skills]] | [[claude-skills/original-matt-pocock-grill-me]] | [[claude-skills/original-wikipedia-signs-of-ai-writing]] | [[claude-skills/original-skills-sh-marketplace]] | [[claude-skills/source-provenance]] | [[ai-operating-system/_index]] | [[claude-code-memory-systems/_index]]

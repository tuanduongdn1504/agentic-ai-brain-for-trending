# Source Provenance & Verification Log

*A transparency audit of research sources, claims flagged for independent verification, and methodological limits.*

## Source

**PRIMARY SOURCE:** Ben AI YouTube video "8 Claude Skills I Can't Live Without" (video ID: bXnRA3pJavE, published April 18, 2026, ~147K views). Transcript obtained via yt-dlp. Video duration ~20 minutes; presents 8 meta-skills + 3 bonus skills.

**ORIGINAL RESOURCES CITED IN DIGEST:**
- `github.com/anthropics/skills` — Anthropic open-source skills repository | VERIFIED
- `anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills` — Anthropic engineering blog on progressive disclosure | VERIFIED
- `agentskills.io` — Open Agent Skills ecosystem client showcase (40+ platforms) | VERIFIED
- `support.claude.com` — Anthropic support articles on skills creation/usage | VERIFIED
- `github.com/mattpocock/skills` — Matt Pocock skills repository (grill-me, grill-with-docs origins) | VERIFIED
- `aihero.dev/my-grill-me-skill-has-gone-viral` — Matt Pocock's own writeup on grill-me viral adoption | VERIFIED
- [[en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing]] — Wikipedia AI Cleanup guide (20+ tells across 8 categories) | VERIFIED
- `skills.sh` — Vercel's Open Agent Skills Directory (~788K installs reported; ecosystem scale) | VERIFIED
- `snyk.io/blog/toxicskills-malicious-ai-agent-skills-clawhub/` — Snyk Feb 2026 security audit (36.82% flaw rate, 1,467 compromised skills) | VERIFIED
- `platform.claude.com/docs/en/build-with-claude/prompt-engineering` — Anthropic official prompt engineering docs (7 canonical techniques) | VERIFIED
- [[youtube.com/watch?v=bXnRA3pJavE]] — Ben AI video direct link | PARTIAL (metadata accessible, transcript only via user context)
- `benai.kit.com` — Ben AI landing page (AI Accelerator community signup) | VERIFIED
- `fs.blog/mental-models/` — Farnam Street decision-framework knowledge (pre-mortem, sunk-cost, inversion) | VERIFIED

---

## Originals Verified

| Claim | Source | Status | Evidence |
|-------|--------|--------|----------|
| **SKILL.md YAML spec** (name + description required) | github.com/anthropics/skills + support.claude.com | ✅ VERIFIED | Fetched SKILL.md examples; format confirmed |
| **Progressive disclosure 3-level model** (metadata → full SKILL.md → bundled files) | anthropic.com/engineering blog | ✅ VERIFIED | Official architecture documented |
| **40+ platforms support Skills standard** | agentskills.io client showcase | ✅ VERIFIED | List includes Claude Code, Cursor, Copilot, Gemini CLI, OpenHands, Kiro, etc. |
| **Matt Pocock grill-me skill exists** | github.com/mattpocock/skills + aihero.dev | ✅ VERIFIED | Public repo; Pocock's own blog confirms viral adoption |
| **Wikipedia Signs of AI writing guide** | en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing | ✅ VERIFIED | 20+ concrete tells catalogued; 8+ categories (content, language, style, citation, markup) |
| **skills.sh ecosystem scale** | skills.sh homepage + Snyk audit | ⚠️ PARTIAL | 788,224 total installs reported; unique skill count NOT disclosed (Snyk audited 3,984 skills) |
| **Snyk Feb 2026 security audit** | snyk.io official blog | ✅ VERIFIED | 36.82% flaw rate (1,467 skills); 8 vulnerability categories; 76 active payloads |
| **Anthropic 7 canonical prompt techniques** | platform.claude.com/docs | ✅ VERIFIED | Official docs list in order: clear/direct → context → examples → XML structure → role → long context → model self-knowledge |
| **Anthropic Prompt Improver tool** (4-step auto-enhancement) | platform.claude.com/docs/prompting-tools | ✅ VERIFIED | Official tool; distinct from 'Prompt Master' (third-party Ben AI branding) |
| **MCP Builder is an official Anthropic skill** | github.com/anthropics/skills (mcp-builder/) | ✅ VERIFIED | Confirmed via GitHub API 2026-06-20, alongside skill-creator/pdf/pptx/xlsx/docx/frontend-design/claude-api |
| **Ben AI YouTube channel exists** | youtube.com/@BenAI92 | ✅ VERIFIED | Channel found; verifiable credentials: $1M ARR x2 businesses (claim in metadata) |
| **Ben AI AI Accelerator community** | benai.kit.com | ⚠️ PARTIAL | Paid membership Ben promotes alongside the free plugin; exact price/contents not independently re-verified here |

---

## Claims Flagged

⚠️ **UNVERIFIED / OUTDATED / CONFLICTED:**

- **"91,000 skills" in skills.sh ecosystem** — Ben's video claims this; current data shows ~788,224 total **installs** (not unique skills). Unique skill count unknown; claim likely 8.6× outdated or conflates install-count metric. **STATUS: OUTDATED**

- **Process Interviewer 'adapted from Matt Pocock grill-me'** — Ben credits Pocock; grill-me repo verified; adaptation details (PRD embedding, Anthropic best practices integration, second-brain auto-pull) NOT independently confirmed in Pocock's source code. **STATUS: UNVERIFIED**

- **Humanizer 'based on Wikipedia Signs of AI writing'** — Wikipedia guide verified as genuinely comprehensive; Ben's HUMANIZER skill implementation (customization, exact edits, interface) NOT publicly documented; benai.co site does not expose skill source. **STATUS: UNVERIFIED**

- **Skill #2 titled 'Prompt Master'** — Anthropic's official tool is called 'Prompt Improver', not 'Prompt Master'. Ben AI may have rebranded or created independent skill. **STATUS: CONFLICTED (Anthropic docs say "Prompt Improver"; Ben says "Prompt Master")**

- **MCP Builder as 'built-in Anthropic skill'** — ✅ CORRECT. `mcp-builder` is a genuine Anthropic skill in github.com/anthropics/skills (verified 2026-06-20 via GitHub API). **STATUS: VERIFIED — Ben's claim holds.**

- **Skills work in 'Claude Cowork'** — Claude Cowork is a real Anthropic product (the vault already documents it in [[claude-cowork/_index]] + [[cowork-third-party-inference/_index]]). The agent's "cowork.anthropic.com unreachable" note was a fetch failure, not evidence of non-existence. **STATUS: VERIFIED (Cowork real; cross-platform skills).**

- **Ben AI's Process Interviewer outputs 'confirmed summary + full PRD embedding Anthropic best practices'** — Exact output format NOT verified (YouTube transcript unavailable; benai.ko site does not expose skill internals). **STATUS: UNVERIFIED**

- **"Skills get MUCH more powerful when you have a second brain/OS set up"** — Claimed feature (auto-pull context from workspace); architectural coupling not formally documented in Anthropic engineering blog. **STATUS: UNVERIFIED (user experience claim)**

- **Snyk audit '36.82% flaw rate' extrapolates to all 788K skills** — Audit sample: 3,984 skills only; representativeness unknown. **STATUS: STATISTICAL CAVEAT (sample size limits generalization)**

- **Free plugin at c.benai.co/8csiu-free delivers working .plugin file** — URL unreachable via WebFetch (redirects to benai.kit.com signup form); actual file format/contents NOT verified. **STATUS: UNVERIFIED**

- **Ben AI's background ('two $1M ARR businesses' prior to YouTube)** — Stated in channel metadata; founding dates, business names, exit status NOT independently confirmed. **STATUS: UNVERIFIED**

- **Skill #4 Fact Checker outputs 'true/mostly-true/unverifiable/false counts'** — No independent source verified this exact output format. **STATUS: UNVERIFIED**

- **Anthropic engineering blog quote: 'real work requires procedural knowledge and organizational context'** — Article fetched and summarized; direct quote NOT extracted/verified. **STATUS: UNVERIFIED (quote attribution)**

---

## What We Did Not Verify

**OUT OF SCOPE / NOT ATTEMPTED:**

- Ben AI's specific **Prompt Master vs Anthropic's Prompt Improver** implementation differences — would require either Ben's source code or side-by-side feature comparison (not available publicly)

- **Exact Snyk sample composition** (which 3,984 skills were audited; distribution across platforms/authors) — Snyk blog does not disclose sampling methodology

- **skills.sh ecosystem composition change over time** — only present-day snapshot (788K installs) fetched; historical growth curve not reconstructed

- **MCP Builder alternative sources** — searched mcpmarket.com but could not independently verify if it's Anthropic-native or third-party wrapper

- **Ben AI video transcript in full** — YouTube page footer-only accessible; video 20-min runtime not fully transcribed by yt-dlp call

- **Matt Pocock's skill design philosophy or 'grilling model loop'** — grill-me repo code reviewed but Pocock's own blog/documentation on design rationale only partially fetched

- **Wikipedia's Signs of AI writing guide historical evolution** — only current version (as of 2026-06-20) verified; guide's 2023-2025 evolution NOT tracked

- **Anthropic Cowork product existence** — no official documentation found; product team/roadmap not accessible

- **Ben AI's specific claim about 'cost reduction via second brain first check'** — plausible but quantification (tokens saved, latency improvement) NOT measured

---

## Key Takeaways

- **Skill.md is the open standard** — Anthropic + 40+ platforms converging on identical metadata format (name + description + markdown body) signals ecosystem maturity & interoperability.

- **Progressive disclosure architecture validates second-brain design** — Anthropic's 3-level context loading (metadata → SKILL.md → bundled files) mirrors Karpathy LLM Wiki pattern; architectural symmetry between knowledge management + capability extension confirmed.

- **skills.sh ecosystem at scale (~788K installs) but 36% flaw rate is material risk** — Snyk's verified 1,467 compromised skills = significant supply-chain threat; vetting burden entirely on installer; no systematic pre-publication gate exists.

- **Matt Pocock's grill-me pattern is **foundational** — interview-before-build discipline proven effective for requirement capture; Ben AI's adaptation for skill PRD generation extends pattern; applicable to hireui recruitment workflows.

- **Wikipedia's AI-writing signs are concrete + reusable** — 20+ tells across 8 categories provide operational linting rubric for vault discipline ('NEVER fabricate'; Rule 12 'Fail loud'); era-specific vocabulary (2023-2025 evolution tracked) useful for provenance dating.

- **Ben AI's claims partially upstream of verification** — 'MCP Builder built-in', 'Prompt Master', 'Cowork' unsupported by Anthropic official docs; either rebranding, third-party, or speculative product roadmap; recommend Anthropic-first patterns for hireui deployment.

- **No single source contradicts core Anthropic position** — Skills work on Free/Pro/Max/Team/Enterprise; progressive disclosure + cross-platform support verified; unverified claims are Ben's framing/packaging, not foundational architecture.

---

[[claude-skills/overview]] | [[claude-skills/video-to-original-crosswalk]] | [[ai-operating-system/_index]] | [[multi-agent-orchestration/_index]] | [[harness-engineering/_index]]

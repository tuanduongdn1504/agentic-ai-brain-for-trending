# Original: Wikipedia "Signs of AI Writing"

*Deep-dive the Wikipedia Signs of AI writing guide that operationalizes into the Humanizer skill. List the concrete catalogued tells/categories so detection logic is reconstructable.*

## Summary

Wikipedia's "[Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)" guide is a genuine, comprehensive WikiProject AI Cleanup resource that catalogues 20+ concrete tells of machine-generated text across 8+ major categories. The guide is substantial enough to serve as a detection framework—though the tells evolve as AI writing techniques advance (tracked with era-specific vocabulary lists: 2023–mid-2024 vs mid-2024–2025 variants).

Ben AI's **Humanizer skill** explicitly operationalizes this guide by scanning for and removing these patterns from AI-generated content. However, ⚠️ the Humanizer skill's exact implementation, customization options, and whether it covers the full 2025+ vocabulary list are unverified—Ben's personal site does not publicly expose skill documentation.

## Key Takeaways

**8+ Major Categories of AI-Writing Tells (from Wikipedia):**

- **Content Patterns** — undue emphasis on significance, promotional language ("boasts", "delve"), vague attribution ("industry reports", "some critics", "recent studies"), outline-like conclusions, false neutrality through excessive hedging
- **Language Patterns** — "not just X but also Y" construction, rule of three (three-item lists as filler), excessive em-dashes, avoidance of "is/are" in favor of "stands as"/"serves as", transitional glue ("Additionally", "Furthermore")
- **Style & Formatting** — excessive title-case, over-boldface, markdown artifacts, smart quotes
- **Citation Issues** — broken links, invalid DOIs, unsourced claims, hallucinated references
- **Markup Bugs** — oaicite tags, contentReference markers, span artifacts
- **Article Structure** — abrupt style shifts mid-article, uneven paragraph density, list-heavy vs narrative sections
- **Era-Specific Vocabulary** — Wikipedia tracks generation-era signals:
  - **2023–mid-2024:** "additionally", "bolstered", "boasts", "crucial", "delve", "intricate", "landscape", "meticulous", "pivotal", "testament", "vibrant"
  - **mid-2024–2025:** "align with", "enhance", "fostering", "highlighting"
  - **2025+:** emerging patterns tracked but incomplete
- **Vagueness & Hedging** — excessive "may", "might", "could", "arguably" where specificity expected

**Humanizer operationalizes by:**
- Scanning text against Wikipedia's 20+ tells
- Removing filler phrases ("hope you're well", "I look forward to")
- Replacing vague hype ("unlock", "innovative") with specifics
- Flagging excessive formatting (bold, title-case, em-dashes)
- Rejecting unsourced attribution
- Designed as final-step polish in copywriting pipelines

**How to Reconstruct Without Humanizer:**
1. Read https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing
2. Build a linting checklist (8 categories above)
3. Scan systematically for tells in your text
4. Cross-reference era-specific vocabulary to date suspected AI content
5. Edit surgically: remove tells, add specificity, normalize tone

## Source

- **Primary:** https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing (fetched 2026-06-20)
- **Ben AI attribution:** YouTube "8 Claude Skills I Can't Live Without" (bXnRA3pJavE, 2026-04-18); free plugin c.benai.co/8csiu-free ⚠️ (URL unverified / not directly accessible)
- **Related:** [[claude-skills/original-anthropic-agent-skills]], [[prompt-evaluation/_index]], [[ai-operating-system/_index]]

## Operational Relevance

**For Storm Bear vault:** Wikipedia's tells are essential for the vault CLAUDE.md Rule 3 (Surgical Changes) and Rule 1 (Think Before Coding). When reviewing Claude-generated wiki files (marked `(C)`), vet against Wikipedia's rubric:
- Reject promotional tone and vague attribution
- Use era-specific vocabulary to date generated content (provenance tracking)
- Archive only editorially-polished versions post-humanization

**For hireui recruitment SaaS:** Humanizer applies to AI-augmented customer-facing communication (rejection emails, interview feedback, offer letters). Vague attribution or promotional hype in recruitment messaging damages trust. Chain after [[claude-skills/original-prompt-engineering-best-practices|prompt-optimization]] for human-quality correspondence.

---

**Related:** [[claude-skills/overview]], [[prompt-evaluation/_index]], [[claude-skills/video-to-original-crosswalk]]

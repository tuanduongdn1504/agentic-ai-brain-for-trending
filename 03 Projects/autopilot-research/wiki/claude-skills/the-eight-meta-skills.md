# The 8 Meta-Skills — Catalog

*A detailed reference guide to Ben AI's foundational meta-skills for Claude workflows, with installation, customization, and cross-references to originating frameworks.*

## 1. Process Interviewer

**Problem it solves:** Fuzzy requirements and misalignment — you think you know what you want, then see the output and realize the brief was incomplete.

**What it does:** Conducts a structured 10–15+ question interview to extract and validate a process or specification BEFORE execution. Outputs a confirmed summary + full PRD embedding Anthropic's [[claude-skills/original-anthropic-agent-skills|agent skill-building best practices]].

**How it's used (demo):** Say "interview me about a recruitment screening workflow." The skill asks questions one at a time, surfaces edge cases, and constructs a decision tree. With a second brain configured, it checks your workspace first to avoid re-asking answered questions. Reduces token waste on back-and-forth clarification.

**Install or invoke:** Available via c.benai.co/8csiu-free (free plugin) or as standalone skill in Claude Code marketplace. Trigger: explicitly invoke '/process-interviewer' or let it auto-run if configured in folder instructions.

**Customize & chain tips:** 
- Pair with Skill #2 (Prompt Master) to optimize the PRD output into a reusable prompt.
- Chain into Skill #8 (MCP Builder) if the process involves custom API connectors.
- With second brain: ensures no duplicate interviews across multiple projects.

**Original it derives from:** [[claude-skills/original-matt-pocock-grill-me|Matt Pocock's grill-me skill]]. ⚠️ Ben AI credits Pocock's grill-me as the source but independent verification of Pocock's grill-me authorship not completed. Both skills follow the "interview before execution" pattern. Ben's adaptation adds Anthropic skill-building best practices formatting.

---

## 2. Prompt Master

**Problem it solves:** Unstructured brain-dumps (voice notes, chat transcripts, rambling ideas) don't trigger Claude's best-practice capabilities.

**What it does:** Transforms messy input into an optimized, structured prompt following [[claude-skills/original-prompt-engineering-best-practices|Anthropic's canonical techniques]]: clear intent, examples, XML tags, role definition, context stacking, and grounding.

**How it's used (demo):** End a voice note with "optimize this using the prompt master skill"; Claude rewrites it into a professional, structured prompt. Can auto-pull second-brain context if configured.

**Install or invoke:** Via c.benai.co/8csiu-free or Claude Code marketplace. Trigger: '/prompt-master' or auto-run via workspace folder instructions.

**Customize & chain tips:**
- Chain BEFORE Skill #1 (Process Interviewer) to clean up the initial brief.
- Chain AFTER Skill #7 (Decision Toolkit) to structure decision outputs into reusable prompt templates.
- Can save outputs as [[claude-skills/overview|skill templates]] for reuse across projects.

**Original it derives from:** ⚠️ Likely based on [[claude-skills/original-prompt-engineering-best-practices|Anthropic's official prompt-engineering best practices]]. Anthropic documents an official tool called "Prompt Improver" (not "Prompt Master"), which performs 4-step automated enhancement. No independent verification that Ben AI built or rebranded an official Anthropic "Prompt Master" skill exists.

---

## 3. Humanizer

**Problem it solves:** AI-generated text for public audiences carries recognizable tells that undermine credibility.

**What it does:** Removes signs of AI writing by comparing text against [[claude-skills/original-wikipedia-signs-of-ai-writing|Wikipedia's comprehensive "Signs of AI writing" guide]]. Targets patterns like promotional hype ("unlock potential"), vague attribution, excessive em-dashes, and rule-of-three constructions.

**How it's used (demo):** Paste AI-generated copy. Run '/humanizer'. Claude rewrites to remove documented AI-writing patterns. Examples: "unlock your potential" → "increase your ability to X"; "some say" → cite a specific source or remove.

**Install or invoke:** Via c.benai.co/8csiu-free or marketplace. Trigger: '/humanizer' on any text leaving your workspace.

**Customize & chain tips:**
- Chain as LAST step in copywriting pipelines (Process Interviewer → Prompt Master → content generation → **Humanizer**).
- Pair with Skill #4 (Fact Checker) for published articles (verify facts, then humanize).
- For recruitment SaaS: apply to candidate communications, job postings for consistency.

**Original it derives from:** [[claude-skills/original-wikipedia-signs-of-ai-writing|Wikipedia's "Signs of AI writing" guide]] (en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing). Wikipedia documents 20+ concrete tells across content patterns, language, formatting, and structure. ⚠️ Skill implementation details and customization options not independently verified in public documentation.

---

## 4. Fact Checker

**Problem it solves:** AI hallucinations and misinformation slip into outputs without systematic verification.

**What it does:** Performs evidence-based fact verification via web cross-reference. Outputs structured findings.

**How it's used (demo):** Three use cases:
- Validate Claude's own output before shipping (e.g., article drafts).
- Verify your own assertions before publishing.
- Audit external published material.

**Install or invoke:** Via c.benai.co/8csiu-free or marketplace. Trigger: '/fact-checker <text>' or paste + run.

**Customize & chain tips:**
- Chain into publishing pipelines (write → fact-check → humanize → publish).
- Pair with Skill #7 (Decision Toolkit) for high-stakes decisions: fact-check evidence before choosing.
- For vault-building discipline: integrated fact-checking enables CLAUDE.md Rule 12 ("Fail loud" if uncertain).

**Original it derives from:** Systematic verification frameworks (journalism, peer-review). [[prompt-evaluation/_index|Prompt evaluation]] documents structured evidence-gathering as foundational to trust.

---

## 5. Find Skills

**Problem it solves:** Manual skill discovery across [[claude-skills/original-skills-sh-marketplace|skills.sh ecosystem]] is slow and lacks context.

**What it does:** Discovers relevant skills from the open agent skills marketplace, displays install counts, and integrates into Claude's workflow. Skills.sh reports 788,224+ total installs as of 2026-06-20.

**How it's used (demo):** Ask "find me a skill for scheduling" or "find image-generation skills." Claude searches skills.sh, ranks by relevance + install count, and offers install options.

**Install or invoke:** Via c.benai.co/8csiu-free or marketplace. Trigger: '/find-skills <task>' or "help me find a skill for X."

**Customize & chain tips:**
- Chain AFTER Skill #1 (Process Interviewer) once you've defined a workflow.
- Use in second-brain workflows to discover published solutions before building custom skills.
- ⚠️ **Security note:** skills.sh has zero curation. Snyk audit (Feb 2026) found 36.82% of audited skills have security flaws; 13.4% have CRITICAL vulnerabilities. Vet SKILL.md source code before installing — check for hardcoded secrets, unverified external fetches, suspicious shell commands.

**Original it derives from:** [[claude-skills/original-skills-sh-marketplace|skills.sh marketplace]] (built by Vercel; 40+ agent platforms supported). ⚠️ Ben AI claims "91,000+ skills"; current ecosystem reports 788K+ installs across 1K+ listed skills (figure appears outdated or confused with install-count metric).

---

## 6. Front-End Slides

**Problem it solves:** Presentation generation requires design expertise that most people outsource or skip.

**What it does:** Auto-generates animated HTML presentations (reveal.js format) from scratch or by converting PowerPoint. Embeds visual-hierarchy best practices, applies customizable style presets, and supports brand-guide input.

**How it's used (demo):** Say "create a presentation about AI ethics with 8 slides" or "convert this PowerPoint to animated HTML with our brand colors." Claude outputs reveal.js HTML with keyboard navigation, presenter notes, and PDF export.

**Install or invoke:** Via c.benai.co/8csiu-free or marketplace. Trigger: '/frontend-slides <topic>' or upload PowerPoint + run.

**Customize & chain tips:**
- Define a brand guide (colors, typography, spacing) in your second brain; Skill #6 auto-pulls it.
- Chain AFTER Skill #7 (Decision Toolkit): convert decision framework into a client presentation.
- For [[ai-operating-system/_index|ai-operating-system]]: auto-generate onboarding decks, status reports without design overhead.

**Original it derives from:** Design-system best practices — visual hierarchy (IXD Foundation), data-ink ratio (Edward Tufte), type-scale typography, CSS design tokens, animation restraint (Nielsen Norman), one-idea-per-slide discipline (Duarte's Slide:ology®). Technical foundation: reveal.js presentation framework.

---

## 7. Decision Toolkit

**Problem it solves:** High-stakes decisions (hiring, vendor choice, project pivot) suffer from confirmation bias, sunk-cost fallacy, and optimism bias.

**What it does:** Guides decision-making via first-principles thinking + interactive HTML wizard. Principle: "guide, don't decide" (human retains authority). Wizard steps: frame decision → start-fresh test (sunk-cost elimination) → timing → stakeholder impact → bias checks → opportunity-cost analysis → scenarios + probability estimates → optional verdict.

**How it's used (demo):** Say "help me decide between Claude API vs GPT-4 for our product." Skill structures: frame, fresh-start test, bias checks, opportunity-cost, scenarios, verdict.

**Install or invoke:** Via c.benai.co/8csiu-free or marketplace. Trigger: '/decision-toolkit <decision>' or "help me decide on X."

**Customize & chain tips:**
- Chain BEFORE Skill #4 (Fact Checker) for evidence-heavy decisions: fact-check assumptions first.
- Chain AFTER Skill #1 (Process Interviewer) to structure complex workflows into decision trees.
- For [[ai-operating-system/_index|ai-operating-system]]: embed into [[multi-agent-orchestration/_index|multi-agent]] runbooks (e.g., recruitment agent candidate screening).

**Original it derives from:** Decision science + behavioral economics — first-principles thinking (Farnam Street), probabilistic thinking, second-order thinking, pre-mortem/prospective hindsight (Gary Klein, Daniel Kahneman), confirmation bias checks, sunk-cost elimination, opportunity-cost analysis, expected-value frameworks (Annie Duke *Thinking in Bets*), regret minimization, inversion/reverse analysis (Farnam Street, Charlie Munger). Formalization: decision matrix / MCDA methodology (operations research).

---

## 8. MCP Builder

**Problem it solves:** Many SaaS APIs lack Model Context Protocol (MCP) connectors, forcing manual API documentation reading.

**What it does:** Reads API documentation, asks capability questions, outputs a complete custom MCP server + setup guide + JSON config snippet for Claude settings.

**How it's used (demo):** Say "build an MCP server for [API]." Ben's example: connecting Claude directly to Reddit, CRM, email.

**Install or invoke:** Trigger: '/mcp-builder' or "create an MCP server for X."

**Customize & chain tips:**
- Chain AFTER Skill #1 (Process Interviewer): interview the workflow, then auto-build the MCP connector.
- Enables [[claude-skills/original-anthropic-agent-skills|agent skills]] to call external APIs without hardcoding credentials.
- For [[harness-engineering/_index|harness engineering]]: enables vault-to-product integration.

**Original it derives from:** [[claude-skills/original-mcp-builder-and-mcp|Anthropic's MCP specification]]. ✅ Confirmed real: `mcp-builder` is an official Anthropic skill in [anthropics/skills](https://github.com/anthropics/skills) (verified 2026-06-20). Ben's "built-in Anthropic skill" framing is accurate.

---

## Chaining patterns & auto-run setup

**Common meta-skill chains:**

1. **Idea → Skill** (Process Interviewer → Prompt Master → custom skill):
   Interview fuzzy idea → structure output → build skill or MCP.

2. **Content for publication** (any source → Fact Checker → Humanizer):
   Generate or paste → verify claims → remove AI tells → ship.

3. **High-stakes decision**:
   Frame decision → fact-check evidence → present findings → decide.

4. **Auto-run via instructions** (Ben's actual method): add a line to your Cowork/Cospace general instructions or your `CLAUDE.md` / folder instructions — e.g. *"Every time I send a long unstructured prompt for a complex task, auto-run the Prompt Master skill first; run Humanizer as the last step before any public copy."* Claude then applies the skill without an explicit invoke.

---

## Bonus skills

**Three additional meta-skills mentioned briefly:**

- **Agent-browser** — browser automation Ben says beats Claude's native browser use. ⚠️ Exact package/repo not verified.
- **Audio-transcriber**: ⚠️ Mentioned by user as bonus skill; not independently verified as standalone Ben creation.
- **OpenRouter** (multi-LLM testing): Test outputs across Claude, GPT-4o, Gemini, DeepSeek, Mistral, and 20+ other models from single endpoint. Useful for [[claude-api-cost-optimization/_index|cost optimization]] and [[prompt-evaluation/_index|evaluation]] workflows.

---

## Source

- **Video:** Ben AI — "8 Claude Skills I Can't Live Without" (YouTube bXnRA3pJavE, 2026-04-18). Free plugin: c.benai.co/8csiu-free.
- **Ben AI:** YouTube @BenAI92; non-technical AI education.
- **Linked original resources:**
  - [[claude-skills/original-anthropic-agent-skills|Anthropic Agent Skills]] (anthropic.com/engineering)
  - [[claude-skills/original-matt-pocock-grill-me|Matt Pocock's grill-me]] (github.com/mattpocock/skills)
  - [[claude-skills/original-wikipedia-signs-of-ai-writing|Wikipedia: Signs of AI writing]]
  - [[claude-skills/original-skills-sh-marketplace|skills.sh]] (788K+ installs, 1K+ listed skills)
  - [[claude-skills/original-prompt-engineering-best-practices|Anthropic prompt-engineering best practices]]

---

## Key Takeaways

- **Meta-skills compound with second-brain setup.** These 8 skills auto-pull context from your vault, avoiding repetitive re-prompting and enabling workflow automation. Validates [[ai-operating-system/_index|ai-operating-system]] architecture as foundational infrastructure.

- **Process before execution.** Skills #1 (Process Interviewer) and #7 (Decision Toolkit) enforce deliberate planning + bias-checking BEFORE action — applicable to Goal #2 pilot deployment (recruitment agent requires structured decision frameworks).

- **Skill chaining > individual skills.** Sequential application (interview → optimize → fact-check → humanize → present) achieves higher quality than single-tool workflows. Enables [[harness-engineering/_index|harness engineering]] discipline.

- **Ecosystem maturity with security trade-off.** skills.sh has 788K+ installs but Snyk audit (Feb 2026) found 36.82% with flaws, 13.4% CRITICAL. Use Find Skills (Skill #5) for discovery but vet SKILL.md source code before install.

- **Automation via instructions.** Tell Claude (via Cowork/Cospace general instructions, or your `CLAUDE.md` / folder instructions) to auto-run a skill when a trigger fires — e.g. run Prompt Master on every long unstructured prompt. Reduces manual-invocation friction.

- **Third-party framing differs from Anthropic-native.** Ben's 8-skill collection rebrands some tools (e.g., "Prompt Master" vs. official "Prompt Improver") and genuine Anthropic built-ins (`mcp-builder`, `skill-creator`). Cross-reference with official docs; prioritize [[claude-skills/original-anthropic-agent-skills|Anthropic-native skills]] for production.

- **Patterns emerge:** Skills #1–4 form a content-production chain; Skills #6–7 form decision + communication pipeline; Skill #5 is discovery; Skill #8 is integration. Treat as modular building blocks.

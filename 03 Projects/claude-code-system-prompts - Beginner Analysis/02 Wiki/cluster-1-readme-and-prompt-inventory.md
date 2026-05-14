# Cluster 1 — README + 293-file prompt inventory

> **Sources:** README.md (69 KB, 405 lines)

## What claude-code-system-prompts is

A **third-party reverse-engineering reference archive** of Claude Code's system prompts. The README opens:

> *"This repository contains an up-to-date list of all Claude Code's various system prompts and their associated token counts as of Claude Code v2.1.140 (May 12th, 2026). It also contains a CHANGELOG.md for the system prompts across 177 versions since v2.0.14. From the team behind Piebald."*

And the update discipline is explicit:

> *"This repository is updated within minutes of each Claude Code release. See the changelog, and follow @PiebaldAI on X for a summary of the system prompt changes in each release."*

This is the **most aggressive update cadence observed in any 64-wiki corpus subject** — minutes-per-release vs claude-seo v64's ~weekly cadence.

## Why "multiple system prompts"?

The README explains the conceptual model:

> **"Claude Code doesn't just have one single string for its system prompt."**
>
> Instead, there are:
> - Large portions conditionally added depending on the environment and various configs.
> - Descriptions for builtin tools like `Write`, `Bash`, and `TodoWrite`, and some are fairly large.
> - Separate system prompts for builtin agents like Explore and Plan.
> - Numerous AI-powered utility functions, such as conversation compaction, `CLAUDE.md` generation, session title generation, etc. featuring their own systems prompts.
>
> The result — **110+ strings** that are constantly changing and moving within a very large minified JS file.

**Corpus implication**: Claude Code's "system prompt" is **NOT a monolithic string** — it's a **composable assembly of 110+ fragments** activated conditionally by context. Understanding this composability is foundational for any Claude Code skill/plugin author (relevant to mattpocock-skills v57 / claude-seo v64 / cc-sdd v61 / karpathy-skills v63 / claude-code-best-practice v34 / etc. — every prior T1 corpus subject builds on top of this composable substrate).

## The 6-category inventory

The README inventories all 293 system-prompt files into 6 categories. Counts and token estimates below.

### Category 1: Agent Prompts (~30 files)

**Sub-agents (2):**
- Agent Prompt: Explore (575 tks) — sub-agent for codebase exploration
- Agent Prompt: Plan mode (enhanced) (715 tks)

**Creation Assistants (3):**
- Agent Prompt: Agent creation architect (1,110 tks)
- Agent Prompt: CLAUDE.md creation (384 tks)
- Agent Prompt: Status line setup (2,124 tks)

**Slash Commands (5):**
- Agent Prompt: /batch slash command (1,106 tks)
- Agent Prompt: /rename auto-generate session name (80 tks)
- Agent Prompt: /review-pr slash command (211 tks)
- Agent Prompt: /schedule slash command (3,130 tks)
- Agent Prompt: /security-review slash command (2,521 tks)

**Utilities (22+):**
Auto mode rule reviewer / Background agent state classifier (4,405 tks — largest) / Background job agent instructions / Bash command description writer / Bash command prefix detection (823 tks) / Claude guide agent / Coding session title generator / Conversation summarization / Determine which memory files to attach / Dream memory consolidation / Dream memory pruning / General purpose / Hook condition evaluator (stop) / Managed Agents onboarding flow (2,525 tks) / Memory synthesis / Onboarding guide draft share link workflow / Onboarding guide generator / Prompt Suggestion Generator v2 / Quick PR creation / Quick git commit / Recent Message Summarization / Security monitor for autonomous agent actions (first part 3,332 tks + second part 4,136 tks = 7,468 tks combined — **single largest agent-prompt cluster**) / Session search / Session title and branch generation / WebFetch summarizer / Worker fork

### Category 2: Data — Template content embedded in Claude Code (~50 files)

The **largest single category by token-count** — comprehensive SDK + Managed Agents documentation embedded as reference data:

**Claude API references (8 languages):** C# (4,710 tks) / Go (4,521 tks) / Java (4,732 tks) / PHP (3,691 tks) / Python (4,499 tks) / Ruby (1,094 tks) / TypeScript (3,030 tks) / cURL (2,201 tks)

**Files API references:** Python (1,360 tks) / TypeScript (797 tks)

**Tool use references:** Python (5,106 tks) / TypeScript (5,033 tks) / Tool use concepts (4,356 tks)

**Streaming references:** Python (1,660 tks) / TypeScript (1,612 tks)

**Message Batches API reference:** Python (1,635 tks)

**Managed Agents documentation (11 files):**
- Core concepts (3,615 tks)
- Endpoint reference (6,555 tks — **single largest Data file**)
- Environments and resources (2,950 tks)
- Events and steering (2,747 tks)
- Memory stores reference (2,780 tks)
- Multiagent sessions (1,839 tks)
- Outcomes (1,772 tks)
- Overview (2,478 tks)
- Tools and skills (3,844 tks)
- Webhooks (1,439 tks)
- Client patterns (2,685 tks)
- Reference per language: Python (2,843 tks) / TypeScript (2,825 tks) / cURL (2,641 tks)

**Other Data templates:**
- Anthropic CLI (2,878 tks) — reference docs for the `ant` CLI
- Assistant voice and values template (454 tks)
- Claude Platform on AWS reference (1,128 tks) — **NEW in v2.1.139**
- Claude model catalog (2,315 tks)
- GitHub Actions workflow for @claude mentions (525 tks)
- GitHub App installation PR description (409 tks)
- HTTP error codes reference (2,399 tks)
- Live documentation sources (3,835 tks) — **WebFetch URLs for current docs**
- Prompt Caching — Design & Optimization (2,664 tks)
- User profile memory template (232 tks)

**Corpus-significance of Data category:** This category reveals that Claude Code SHIPS WITH ITS OWN COMPLETE SDK REFERENCE for 8+ languages — eliminating need for the agent to fetch external docs in many cases. Sister to claude-seo v64's Living-Domain-Standards tracking (Anthropic ships their own living-docs subset as part of the system prompt).

### Category 3: System Prompt (~50 files)

Parts of the main system prompt itself — the highest-density category for understanding Claude Code's CORE BEHAVIOR. Selected representatives:

**Action safety + execution discipline:**
- Action safety and truthful reporting (144 tks) — **NEW in v2.1.136** "Requires confirmation for irreversible or outward-facing actions, checking targets before destructive edits, and truthful reporting of outcomes"
- Executing actions with care (590 tks)
- Avoiding Unnecessary Sleep Commands (part of PowerShell tool) (175 tks)
- Censoring assistance with malicious activities (98 tks)
- Tool execution denied (144 tks)

**Doing tasks (6 sub-fragments):**
- Doing tasks (ambitious tasks) (47 tks)
- Doing tasks (help and feedback) (24 tks)
- Doing tasks (no compatibility hacks) (52 tks)
- Doing tasks (no unnecessary error handling) (64 tks)
- Doing tasks (security) (67 tks)
- Doing tasks (software engineering focus) (104 tks)

These 6 sub-fragments together form the **agent's task-execution philosophy** — corpus-rare granular discipline-fragments observable.

**Tone + style:**
- Communication style (297 tks) — "brief, user-facing updates at key moments"
- Tone and style (code references) (39 tks) — "include file_path:line_number when referencing code"
- Tone and style (concise output — short) (16 tks)

**Memory + planning + modes:**
- Auto mode (244 tks) — continuous task execution (background-agent-like)
- Autonomous loop check (1,071 tks)
- Autonomous loop persistence guidance CLAUDE_CODE_LOOP_PERSISTENT (1,173 tks) — **NEW in v2.1.129**
- Learning mode (1,042 tks) — main system prompt for learning mode
- Minimal mode (164 tks)
- Background session instructions (142 tks)
- Skillify Current Session (1,798 tks)

**Memory instructions cluster:**
- Memory instructions (391 tks)
- Memory description of user details (122 tks)
- Memory description of user feedback (139 tks)
- Memory description of user feedback (with explicit save) (146 tks)
- Memory staleness verification (112 tks)
- Description part of memory instructions (148 tks)
- Dream CLAUDE.md memory reconciliation (279 tks)
- Dream team memory handling (279 tks)
- Agent memory instructions (337 tks)

**Plan mode (multiple variants):**
- Remote plan mode (ultraplan) (617 tks)
- Remote planning session (432 tks)
- Insights at a glance summary (569 tks)
- Insights friction analysis (139 tks)
- Insights on the horizon (148 tks)
- Insights session facets extraction (310 tks)
- Insights suggestions (748 tks)
- Learning mode (insights) (142 tks)

**Tool usage:**
- Tool usage (subagent guidance) (103 tks)
- Tool usage (task management) (70 tks)
- Parallel tool call note (part of Tool usage policy) (102 tks)
- Subagent delegation examples (606 tks)
- Subagent prompt-writing examples (439 tks)
- Writing subagent prompts (287 tks)
- Fork usage guidelines (323 tks)
- Worker instructions (272 tks)

**Hooks + harness:**
- Hooks Configuration (1,493 tks)
- Harness instructions (178 tks)

**Communication infrastructure:**
- How to use the SendUserMessage tool (283 tks)
- Advisor tool instructions (443 tks)
- Agent Summary Generation (178 tks)
- Agent thread notes (205 tks)

**REPL + scripting:**
- REPL tool usage and scripting conventions (1,049 tks)

**Browser automation:**
- Chrome browser MCP tools (156 tks)
- Claude in Chrome browser automation (759 tks)

**Operating-system + shell awareness:**
- PowerShell edition for 5.1 (285 tks)
- WSL managed settings double opt-in (152 tks)
- One of six rules for using sleep command (23 tks)

**Schedule + git:**
- Git status (37 tks)
- Proactive schedule offer after natural future follow-up (338 tks)
- Strict proactive schedule offer gate (221 tks) — **NEW in v2.1.132**
- Option previewer (151 tks)

**Compaction:**
- Context compaction summary (278 tks)
- Partial compaction instructions (805 tks)

**Other:**
- Scratchpad directory (170 tks)

### Category 4: System Reminders (~40 files)

**NEW major category as of January 23, 2026** (per README's prominent banner): *"We've added all of Claude Code's ~40 system reminders to this list."*

System reminders are **runtime-injected** harness messages distinct from system prompts (which are loaded at session start). They mediate context between Claude and the harness about file modifications, plan-mode transitions, hook results, etc.

Selected examples:
- Plan mode is active (5-phase) (927 tks)
- Plan mode is active (iterative) (936 tks)
- Plan mode is active (subagent) (307 tks)
- Plan mode re-entry (236 tks)
- Plan mode approval tool enforcement (236 tks)
- Exited plan mode (41 tks)
- Verify plan reminder (47 tks)
- Plan file reference (62 tks)
- Ultraplan mode (437 tks)
- Hook additional context (35 tks)
- Hook blocking error (52 tks)
- Hook success (29 tks)
- File modification detected (budget exceeded) (104 tks)
- File modified by user or linter (97 tks)
- File opened in IDE (37 tks)
- File truncated (74 tks)
- File shorter than offset (59 tks)
- File exists but empty (27 tks)
- TodoWrite reminder (86 tks)
- Task tools reminder (111 tks)
- Token usage (39 tks)
- USD budget (42 tks)
- Output style active (46 tks)
- Memory file contents (36 tks)
- Nested memory contents (33 tks)
- Compact file reference (57 tks)
- Lines selected in IDE (66 tks)
- New diagnostics detected (52 tks)
- MCP resource no content (41 tks)
- Agent mention (45 tks)
- Session continuation (37 tks)
- /btw side question (244 tks)
- Previously invoked skills (131 tks)
- Team Coordination (250 tks)
- Team Shutdown (136 tks)
- Thinking frequency tuning (129 tks)
- Stop hook blocking error (20 tks)

**Corpus implication:** System reminders are a corpus-rare observable primitive. Most agent frameworks don't expose their runtime-injection messages. v65 provides ground-truth reference. Sister observation to v60 free-claude-code's "PowerShell edition" detection — both reveal the depth of Claude Code's contextual-injection machinery.

### Category 5: Tool Descriptions (~50 files including 28+ Bash sub-rules)

Each builtin tool ships with its description embedded in the system prompt. The README explicitly notes Bash has **28+ sub-fragments** representing different rules and contexts.

**Core tool descriptions:**
- AskUserQuestion (287 tks)
- BrowserBatch (159 tks)
- Computer (161 tks) — Chrome browser automation
- CronCreate (948 tks)
- Edit (202 tks)
- EnterPlanMode (878 tks)
- EnterWorktree (604 tks)
- ExitPlanMode (417 tks)
- ExitWorktree (527 tks)
- Grep (300 tks)
- LSP (255 tks)
- NotebookEdit (121 tks)
- PowerShell (1,914 tks) — **2nd-largest tool description**
- PushNotification (261 tks)
- REPL (715 tks)
- ReadFile (412 tks)
- RemoteTrigger prompt (189 tks)
- SendMessageTool (332 tks)
- Skill (306 tks)
- TaskCreate (499 tks)
- TeamDelete (154 tks)
- TeammateTool (1,585 tks)
- **TodoWrite (2,037 tks — single LARGEST tool description)**
- WebFetch (297 tks)
- WebSearch (319 tks)
- Write (129 tks)

**Bash sub-fragments (28):**
Bash has the most decomposed tool description in Claude Code — 28+ separate fragments for different rules and contexts:
- Bash (overview / built-in tools note / working directory / maintain cwd / quote file paths / no newlines / parallel commands / sequential commands / semicolon usage / verify parent directory / prefer dedicated tools — 2 variants / git commit and PR creation instructions 1,611 tks / git — avoid destructive ops / git — never skip hooks / git — prefer new commits / timeout)
- Bash sleep sub-rules (4): keep short / no polling background tasks / run immediately / use check commands
- Bash sandbox sub-rules (14): mandatory mode / no exceptions / per-command / default to sandbox / adjust settings / explain restriction / response header / retry without sandbox / user permission prompt / tmpdir / no sensitive paths / failure evidence condition / evidence list header / evidence access denied / evidence network failures / evidence operation not permitted / evidence unix socket errors
- Bash alternatives (6): communication (echo/printf → output text) / content search (grep → Grep) / edit files (sed/awk → Edit) / file search (find/ls → Glob) / read files (cat/head/tail → Read) / write files (echo/cat → Write)

**Corpus-rare granular discipline-fragmentation**: Bash's sandbox sub-rules (14 fragments) form an explicit decision-tree for when/how to escape sandbox. Sister to claude-seo v64's anti-Goodhart hard-stop discipline at programmatic-SEO scale — both subjects bake explicit anti-bypass disciplines into system-prompt level.

**Tool description "additional notes":**
- Agent (simple usage notes) (324 tks) — **NEW in v2.1.140**
- Agent (usage notes) (791 tks)
- AskUserQuestion (preview field) (134 tks)
- Background monitor (streaming events) (1,401 tks)
- Snooze (delay and reason guidance) (732 tks)
- TaskList (teammate workflow) (133 tks)
- ToolSearch (second part) (202 tks)
- Write (read existing file first) (84 tks) — **CHANGED in v2.1.140**
- request_teach_access (part of teach mode) (139 tks)
- Tool Parameter: Computer action (251 tks)

### Category 6: Skills (~25 files)

Built-in skill prompts for specialized tasks — distinct from Tool Descriptions in that they form composable skill activations.

- /catch-up periodic heartbeat (1,591 tks)
- /dream memory consolidation (512 tks)
- /dream nightly schedule (441 tks)
- /init CLAUDE.md and skill setup (new version) (5,384 tks — **3rd largest skill**)
- /insights report output (182 tks)
- /loop cloud-first scheduling offer (510 tks)
- /loop self-pacing mode (678 tks)
- /loop slash command (969 tks)
- /loop slash command (dynamic mode) (514 tks)
- /morning-checkin daily brief (1,576 tks)
- /pre-meeting-checkin event brief (491 tks)
- /stuck slash command (964 tks)
- Agent Design Patterns (1,974 tks)
- Build with Claude API (reference guide) (655 tks)
- **Building LLM-powered applications with Claude (8,833 tks)** — **2nd largest skill**
- Computer Use MCP (1,206 tks)
- Create verifier skills (2,551 tks)
- Debugging (417 tks)
- Dynamic pacing loop execution (598 tks)
- Generate permission allowlist from transcripts (2,338 tks)
- **Model migration guide (18,340 tks)** — **SINGLE LARGEST FILE in entire archive**
- Schedule recurring cron and execute immediately (compact) (173 tks)
- Schedule recurring cron and run immediately (271 tks)
- Simplify (937 tks)
- Team onboarding guide (521 tks)
- Update Claude Code Config (1,195 tks)
- Verify CLI changes (example for Verify skill) (565 tks)
- Verify server/API changes (example for Verify skill) (612 tks)
- Verify skill (2,694 tks)
- update-config (7-step verification flow) (1,160 tks)

**Notable observations:**
- **Model migration guide at 18,340 tks** = largest single file in archive. This is Anthropic's own ground-truth-version of "what changes when migrating between Claude models" — sister-evidence to claude-seo v64's Living-Domain-Standards tracking (Anthropic absorbs their own model versioning into a single migration-skill prompt).
- **Building LLM-powered applications with Claude at 8,833 tks** = comprehensive SDK orientation guide; explicit decision-criteria (Claude API vs Managed Agents) + model defaults + thinking/effort config.
- **Verify skill at 2,694 tks** + Create verifier skills at 2,551 tks + 2 example skills (CLI / server-API) = **adversarial-verification stack at Claude Code level** — sister to v61 cc-sdd Pattern #76 adversarial subagent review (cc-sdd is framework-level; Claude Code Verify skill is harness-level).

## How to use the files (per README)

The README provides explicit usage guidance:

> - **Reference:** Understand what prompts Claude Code uses and how they change across versions
> - **Local patching:** Use **tweakcc** to customize individual prompt pieces in your local Claude Code installation
> - **Feature requests:** For changes to Claude Code's prompts, file issues at [anthropics/claude-code/issues](https://github.com/anthropics/claude-code/issues)

The third bullet explicitly defers product-feature requests upstream to Anthropic — the archive is reference, not product. Corpus-distinct stance: most subjects encourage forks/PRs; v65 explicitly redirects to upstream.

## Awesome Claude Code mention

The README opens with a badge: *"Mentioned in Awesome Claude Code"* (linking to hesreallyhim/awesome-claude-code).

**Corpus-integration**: v50 awesome-claude-skills (vault's own wiki) is the curated-meta aggregator for the broader Claude Code ecosystem; v65 is INSIDE that ecosystem as listed-and-mentioned subject.

## Repository awareness disclosure

The README has a prominent disclaimer about modifications:

> *"For AI agents working with this repository: These files are **extracted reference material**, not modifiable source code. Editing files here does not change Claude Code's behavior."*

This is a **CORPUS-RARE meta-supply-chain awareness disclosure** — Piebald-AI explicitly educates AI agents about what the archive IS and IS NOT. Sister to claude-seo v64's honest-deficiency-disclosure discipline but at META level (educates about the archive's NATURE, not its CAPABILITIES).

**Pattern #66 observation-track extension candidate**: meta-supply-chain awareness for reference archives — observational at v65; consider for v66 audit.

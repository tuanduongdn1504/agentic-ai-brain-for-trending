# ClaudeKit (vividkit.dev) — 21-source wiki synthesis

> **Created:** 2026-05-11
> **NotebookLM ID:** d179ac0c-428b-47e6-b859-99a6b7e7bcb1
> **Sources:** 21 markdown files extracted from https://www.vividkit.dev/vi/guides/ (Tier 0 fetch, no bypass needed)
> **Purpose:** map ClaudeKit's architecture + command surface so it can be compared with harness-engineering and personal harness for adoption decisions

## What is ClaudeKit — architecture + 4 pillars

Different notebook specified, starting new conversation...
Continuing conversation 783e867c...
Answer:
ClaudeKit is an **advanced framework** integrated directly into the native 
configuration (`.claude`) of the Claude Code CLI [1, 2]. Rather than being a 
standalone IDE, it acts as a **professional automation system** that transforms 
a standard terminal chatbot into a high-performance AI coding partner [1, 3]. 
Its core philosophy centers on equipping Claude with a **"super-powered 
toolbox"** and coordinating a "team of specialists" to handle complex tasks with
professional structure and efficiency [2, 4, 5].

### The 4 Core Pillars of ClaudeKit

ClaudeKit is built upon four foundational pillars that define its capability and
behavior:

1.  **Agents (The Specialists):** These are specialized AI models—such as the 
**Planner, Tester, and Reviewer**—configured with unique prompts and internal 
tools to focus on a single area of expertise [4, 6]. They function as a "team of
experts" (e.g., Architect, Builder, Inspector) working together on a project [4,
7].
2.  **Skills (The Knowledge):** Skills are specialized knowledge packages 
(`SKILL.md`) containing deep prompts, references, and scripts [6]. They serve as
the **primary execution units** triggered by slash commands (e.g., `/ck:cook`, 
`/ck:fix`), providing Claude with instant access to specific domains like UI/UX 
design or security auditing [6-8].
3.  **Workflows (The Process):** Workflows are organized combinations of Hooks, 
Skills, and Agents that run sequentially to handle **end-to-end task cycles** 
[6, 7]. For example, the `/ck:cook` workflow automatically moves through 
research, planning, implementation, testing, and final review [9, 10].
4.  **Hooks (The Automation):** Hooks are background scripts that react to 
**lifecycle events** within Claude Code (such as session start, tool calls, or 
task completion) [11, 12]. They automate the "boring" parts of the work, such as
initializing project rules, saving session state, or injecting relevant context 
into every prompt without manual input [6, 11].

### Interaction and Orchestration

These pillars interact in a layered fashion to fulfill user requests:
*   **Initialization:** When a session starts, **Hooks** fire automatically to 
detect the project type, load specific rules, and restore the previous session's
progress [12, 13].
*   **Triggering:** The user initiates a **Workflow** by calling a specific 
**Skill** via a slash command [7].
*   **Execution:** The system identifies the required **Agents** for the task 
[7]. For instance, a `/ck:fix` command might trigger a **Debugger Agent** to 
analyze logs, followed by a **Planner Agent** to strategize a fix [14-16].
*   **Completion:** Once the task is finished, **Hooks** handle the final 
state-saving and document updates, ensuring the environment is ready for the 
next command [17, 18].

### High-Level Architectural Picture

ClaudeKit’s architecture is designed to be **modular, portable, and 
multi-provider**:

*   **Integration Layer:** It lives within the `.claude/` directory of a project
(or global `~/.claude/`), meaning it enhances rather than replaces existing 
Claude Code setups [1, 19].
*   **Orchestration Layer:** This layer manages the **"Agentic"** behavior, 
using specialized agents and structured pipelines (like the 6-phase fix 
pipeline) to ensure quality and prevent "infinite loops" [16, 20, 21].
*   **Runtime Layer (CCS):** Through the **Claude Code Switch (CCS)**, the 
architecture allows for **multi-provider and multi-runtime** flexibility [22, 
23]. Users can route their ClaudeKit commands through different providers 
(Claude Pro, GPT, GLM, Kimi, etc.) to optimize for cost, reasoning depth, or 
rate limits [22, 24, 25].
*   **Compatibility Layer (Migrate):** The system includes a migration engine 
(`ck migrate`) that allows its agents, skills, and rules to be ported to other 
AI tools like **Cursor, Windsurf, or Codex**, ensuring the user's "intelligence 
layer" is not locked into a single platform [26, 27].

Resumed conversation: 783e867c-d143-49ef-97bd-5984b9928dd4

## Command surface — `/ck:*` reference

Different notebook specified, starting new conversation...
Continuing conversation 783e867c...
Answer:
This reference table lists the documented `/ck:*` commands across both the 
Engineer and Marketing Kits, grouped by their primary functional category.

### **1. Basics & Getting Started**
| Command | Description (1 Sentence) | When to Use It |
| :--- | :--- | :--- |
| **/ck:coding-level** | Sets your programming experience level (0-5) to tailor 
AI explanations [1]. | Use to switch between "Junior" and "God Mode" technical 
depth [2]. |
| **/ck:ask** | Provides expert technical and architectural advice without 
implementing code [1]. | Use when you need a second opinion on technology 
trade-offs [2]. |
| **/ck:brainstorm** | Generates solutions and analyzes trade-offs through a 
design-first approach [1, 3]. | Use at the start of a feature to explore ideas 
before planning [4]. |
| **/ck:ck-help** | An interactive guide to explore ClaudeKit’s commands, 
skills, and workflows [1]. | Use when you are unsure which command fits your 
current task [5]. |

### **2. Planning & Research**
| Command | Description (1 Sentence) | When to Use It |
| :--- | :--- | :--- |
| **/ck:plan** | Creates a detailed implementation plan with research, 
red-teaming, and task hydration [6, 7]. | Use for complex features that require 
a structured roadmap before coding [4]. |
| **/ck:research** | Performs deep technical research and evaluates best 
practices for a specific topic [8, 9]. | Use when exploring new frameworks or 
third-party API integrations [10]. |
| **/ck:scout** | Rapidly scans the codebase using parallel agents to identify 
relevant files [8, 11]. | Use to find all call sites or related logic for a 
specific task [12, 13]. |
| **/ck:sequential-thinking** | Performs multi-step reasoning with 
self-correction and hypothesis testing [14]. | Use for troubleshooting 
architectural deadlocks or complex logic [15]. |
| **/ck:problem-solving** | Breaks down complex issues and simplifies variables 
to unblock development [14]. | Use when stuck in a circular logic loop or a 
"wicked" problem. |
| **/ck:predict** | Analyzes code changes to forecast architectural, security, 
and performance impacts [14, 16]. | Use before a major refactor to catch hidden 
side effects [17]. |
| **/ck:xia** | Safely researches, extracts, and ports features from external 
GitHub or local repos [18, 19]. | Use when you want to "borrow" a feature 
pattern from a high-quality open-source repo [20]. |
| **/ck:loop** | Runs automated optimization cycles based on specific metrics 
like performance or coverage [14]. | Use to iteratively improve bundle size or 
test coverage [18]. |

### **3. Execution & Implementation**
| Command | Description (1 Sentence) | When to Use It |
| :--- | :--- | :--- |
| **/ck:cook** | An all-in-one engine that researches, plans, implements, tests,
and reviews a feature [6, 21]. | Use for fast, autonomous implementation of 
known requirements [22]. |
| **/ck:bootstrap** | Initializes a full project including tech stack selection,
architecture, design, and implementation [23, 24]. | Use when starting a 
brand-new application from scratch [25]. |
| **/ck:backend-development** | Builds robust APIs and server-side logic using 
Node.js, Python, or Go [23]. | Use to scaffold NestJS, FastAPI, or Django 
services. |
| **/ck:web-frameworks** | Manages monorepos and modern frontend framework 
configurations like Next.js [23]. | Use for setting up App Router, SSR, or 
Turborepo structures. |
| **/ck:databases** | Designs schemas, optimizes queries, and manages database 
migrations [23, 26]. | Use when defining PostgreSQL, MongoDB, or SQL 
relationships [26]. |
| **/ck:tanstack** | Implements TanStack-specific patterns for state, forms, and
AI streaming [23]. | Use when building advanced React data-fetching or chat 
interfaces. |
| **/ck:deploy** | Automatically detects project types and deploys to over 15 
cloud platforms [27, 28]. | Use to push your app to Vercel, Railway, AWS, or 
Cloudflare [29]. |
| **/ck:ship** | Executes a full delivery pipeline including merging, 
versioning, and creating PRs [30, 31]. | Use when a feature branch is ready for 
production or beta release [28]. |
| **/ck:agentize** | Wraps your codebase into AI-friendly CLI tools and MCP 
servers [32, 33]. | Use to make your code directly consumable by other AI agents
[34]. |
| **/ck:team** | Coordinates multiple specialized agents to work on large tasks 
in parallel [30, 35]. | Use for massive projects where one agent would hit 
context limits [36]. |

### **4. UI/UX & Frontend Design**
| Command | Description (1 Sentence) | When to Use It |
| :--- | :--- | :--- |
| **/ck:ui-ux-pro-max** | Acts as a design partner with 50+ styles and 
professional UX guidelines [37, 38]. | Use to create high-quality, accessible UI
systems without a designer [39]. |
| **/ck:frontend-design** | Builds frontend interfaces from text, screenshots, 
or video references [40, 41]. | Use to replicate a UI from a reference image or 
design spec [42]. |
| **/ck:frontend-development** | Develops React/TypeScript components using 
modern patterns like Radix and Tailwind [40]. | Use for standard UI component 
building and logic. |
| **/ck:ui-styling** | Generates themed UI styles specifically using shadcn/ui 
and Tailwind CSS [40]. | Use to build dark-mode ready, theme-consistent 
components. |
| **/ck:web-design-guidelines** | Audits existing code against standard web 
interface and accessibility guidelines [37]. | Use to ensure your UI is 
professional and WCAG AA compliant [43]. |
| **/ck:stitch** | Generates UI designs via text prompt using the Google Stitch 
pipeline [37, 42]. | Use for rapid text-to-UI prototyping and asset export [44].
|
| **/ck:threejs** | Builds 3D web applications and visualizations using Three.js
[43]. | Use to add interactive 3D elements like globes or models [45]. |
| **/ck:shader** | Writes GLSL fragment shaders for procedural graphics and art 
[43]. | Use for high-performance visual effects within Three.js. |
| **/ck:mermaidjs-v11** | Generates flowcharts, sequence diagrams, and timelines
using Mermaid v11 [43, 46]. | Use to document logic or system flows in Markdown 
[9]. |

### **5. Testing, Debugging & Quality**
| Command | Description (1 Sentence) | When to Use It |
| :--- | :--- | :--- |
| **/ck:fix** | A 6-phase structured pipeline to diagnose and repair bugs based 
on evidence [47, 48]. | Use to repair errors from logs or failed tests with 
regression safety [49, 50]. |
| **/ck:debug** | Performs systemic root-cause analysis by tracing call stacks 
and validating assumptions [47, 48]. | Use when you have a bug but don't yet 
know where it originates [22]. |
| **/ck:test** | Runs local test suites and visual UI tests with deep analysis 
[51]. | Use to verify code changes or test a live URL [2]. |
| **/ck:code-review** | Audits code for quality, performance, and edge cases 
using specialized agents [51, 52]. | Use before committing to ensure high 
standards and security [13, 45]. |
| **/ck:web-testing** | Automates E2E, load, and accessibility testing via 
Playwright and k6 [47]. | Use to verify complex user flows or performance under 
load. |
| **/ck:agent-browser** | Provides an AI-optimized browser automation for 
complex web scraping and interaction [47]. | Use when an agent needs to "see" 
and interact with a website [53]. |
| **/ck:scenario** | Explores "what-if" architectural scenarios and edge cases 
[53, 54]. | Use to simulate potential failures before implementation [55]. |
| **/ck:react-best-practices** | Optimizes React/Next.js code based on 
industry-leading performance patterns [30]. | Use to refactor components for 
better SSR/RSC performance. |

### **6. Security & Intelligence**
| Command | Description (1 Sentence) | When to Use It |
| :--- | :--- | :--- |
| **/ck:security** | Performs comprehensive threat modeling and red-team 
discovery [52, 53]. | Use for high-stakes security audits and risk mitigation 
[56]. |
| **/ck:security-scan** | Scans the codebase specifically for hardcoded secrets 
and dependency vulnerabilities [57, 58]. | Use as a pre-commit check to prevent 
security leaks [59]. |
| **/ck:better-auth** | Implements secure TypeScript authentication including 
OAuth, 2FA, and passkeys [57]. | Use when building user login and identity 
management. |
| **/ck:cti-expert** | A specialized toolset for cyber threat intelligence and 
open-source investigations [57]. | Use for forensics, breach checking, or 
digital footprinting. |

### **7. Git & Version Control**
| Command | Description (1 Sentence) | When to Use It |
| :--- | :--- | :--- |
| **/ck:git** | Handles Git operations like commits, pushes, and PRs using 
natural language [51, 60]. | Use for conventional commits and security-checked 
staging [60]. |
| **/ck:worktree** | Creates isolated Git worktrees to allow parallel 
development on different features [36, 51]. | Use in monorepos to work on 
multiple branches simultaneously [61]. |

### **8. Documentation & Content**
| Command | Description (1 Sentence) | When to Use It |
| :--- | :--- | :--- |
| **/ck:docs** | Analyzes the codebase to initialize, update, or summarize 
project documentation [11, 62]. | Use to keep your READMEs and technical docs in
sync with your code [11]. |
| **/ck:docs-seeker** | Rapidly finds official library documentation via 
llms.txt endpoints [9, 62]. | Use to get the latest API info without manual 
browsing [63]. |
| **/ck:preview** | Renders files into visual explanations, slides, or diagrams 
for easier review [17, 64]. | Use to visualize a plan or a complex Markdown file
in the browser [2, 46]. |
| **/ck:tech-graph** | Renders publication-quality technical SVG diagrams with 7
design styles [64, 65]. | Use for professional documentation, blogs, or slide 
decks [66]. |
| **/ck:llms** | Generates standardized llms.txt files to help other AI tools 
understand your project [63, 67]. | Use to make your repository AI-discoverable 
[68]. |
| **/ck:show-off** | Creates stunning HTML showcases and social media 
screenshots for demos [62, 69]. | Use to generate marketing assets for your 
technical project [70]. |
| **/ck:copywriting** | Generates headlines, CTAs, and conversion-focused copy 
[62, 71]. | Use for landing pages, emails, and marketing campaigns [72]. |

### **9. Project & Session Management**
| Command | Description (1 Sentence) | When to Use It |
| :--- | :--- | :--- |
| **/ck:watzup** | Summarizes recent changes and helps wrap up the current 
working session [11, 73]. | Use at the end of the day to see what you've 
accomplished [5]. |
| **/ck:journal** | Records technical thoughts, decisions, and lessons learned 
into a project log [73, 74]. | Use to maintain a historical record of "the why" 
behind code changes [75]. |
| **/ck:retro** | Generates a data-driven sprint retrospective based on Git 
metrics and health indicators [70, 73]. | Use at the end of a sprint to analyze 
churn and team velocity [35]. |
| **/ck:plans-kanban** | Visualizes all implementation plans on a timeline 
dashboard [2, 76]. | Use to track the progress of long-term feature development 
[5]. |
| **/ck:project-organization** | Analyzes and restructures project file layouts 
for better maintainability [76]. | Use when a project’s folder structure becomes
messy or confusing. |

### **10. Specialized Utilities**
| Command | Description (1 Sentence) | When to Use It |
| :--- | :--- | :--- |
| **/ck:graphify** | Builds a queryable knowledge graph of your code using 
tree-sitter AST [77, 78]. | Use to understand "god nodes" and surprising 
connections in legacy code [16]. |
| **/ck:ai-multimodal** | Analyzes images, audio, and video using Gemini APIs 
[79]. | Use for media-rich tasks like generating alt-text or video summaries 
[23]. |
| **/ck:ai-artist** | Generates high-quality images using curated prompts and 
validation [45, 79]. | Use to create project assets, logos, or icons [45]. |
| **/ck:remotion** | Creates programmatic React-based videos and animations [34,
79]. | Use to build code-driven video demos or social media content [45, 69]. |
| **/ck:skill-creator** | Creates or updates custom Claude skills with built-in 
evaluation benchmarks [77]. | Use when you want to extend ClaudeKit with your 
own logic. |
| **/ck:repomix** | Packages an entire repository into AI-friendly XML, JSON, or
Markdown files [77]. | Use when you need to provide full context to a different 
AI tool. |

Resumed conversation: 783e867c-d143-49ef-97bd-5984b9928dd4

## How ClaudeKit handles a request — flow + decision tree

Different notebook specified, starting new conversation...
Continuing conversation 783e867c...
Answer:
The lifecycle of a request in ClaudeKit is an orchestrated transition from a 
simple user intent into a multi-step execution pipeline managed by specialized 
AI agents. Based on the documentation, here is the trace of a typical request:

### 1. Initiation: User Prompt & Command Selection
The process begins when a user enters a command in the terminal (e.g., `/ck:cook
"add a login button"`) [1, 2]. 
*   **User Decisions:** The user must decide on the "Speed vs. Safety" trade-off
[3]. They choose between a **Fast** approach (using `/ck:cook` for straight 
implementation) or a **Safe** approach (using `/ck:plan` first for complex 
features requiring review) [4-6].
*   **System Action:** ClaudeKit identifies the requested **Skill** and its 
associated `SKILL.md` knowledge package [2].

### 2. Pre-Execution: The "Underground" Layer (Hooks)
Before the AI begins working on the specific task, background scripts called 
**Hooks** fire automatically [2, 7].
*   **System Decisions:** 
    *   **Project Detection:** The `session-init.cjs` hook detects the project 
type (e.g., Node.js, Python) and loads the relevant environment config [8-10].
    *   **State Recovery:** The `session-state.cjs` hook checks for previous 
progress to resume the context [9, 11].
    *   **Safety Check:** Privacy hooks (like `privacy-block.cjs`) scan the 
request to ensure the AI doesn't access sensitive files like `.env` without 
permission [12].
*   **User Intervention:** If a privacy or security block is triggered, the user
must manually approve the action to continue [12, 13].

### 3. Execution Pipeline: Specialist Coordination (Agents)
Once the environment is prepared, ClaudeKit triggers a **Workflow** that 
coordinates a "team of specialists" or **Agents** [2, 7].
*   **Phase 1: Research & Scouting:** The system spawns **Scout** or 
**Researcher** agents to read project documentation and existing code patterns 
to ensure the new work follows the current style [14-16].
*   **Phase 2: Planning:** A **Planner agent** creates a `plan.md` and breaks 
the task into actionable "phases" [15, 17].
*   **Phase 3: Implementation & Testing:** **Builder/Full-stack agents** write 
the code, followed immediately by a **Tester agent** that runs local test suites
to verify the fix or feature [16, 18].
*   **Phase 4: Quality Control:** A **Reviewer agent** audits the changes 
against security (OWASP) and quality standards [18, 19].

**Specific Decision Logic Example (/ck:fix):** The system follows a 6-phase 
pipeline: **Scout** (gather evidence) $\rightarrow$ **Diagnosis** (root cause 
analysis) $\rightarrow$ **Routing** (choose fix strategy) $\rightarrow$ **Fix** 
(implementation) $\rightarrow$ **Verification** (run tests) $\rightarrow$ 
**Prevention** (add regression tests) [20].

### 4. Output and Completion
The final stage delivers the results of the agentic labor.
*   **Output Delivery:** The system provides completed code changes, a detailed 
Markdown report (e.g., `brainstorm-date.md`), and often a summary of tests 
passed [15, 18, 21].
*   **User Intervention:** 
    *   **Approval Gates:** In standard modes, the system pauses at major 
"gates" (like after planning or before applying code) for user approval [14, 16,
22].
    *   **Next Steps:** The system asks the user if they want to proceed to the 
next step (e.g., after brainstorming, it may ask "Hỏi: tạo plan? $\rightarrow$ 
/plan") [14, 23].
*   **Finalization:** Once the user is satisfied, hooks like `git-manager` 
handle the automated commits and PR creation [16, 18].

Resumed conversation: 783e867c-d143-49ef-97bd-5984b9928dd4

## Setup + permission model + safety mechanics

Different notebook specified, starting new conversation...
Continuing conversation 783e867c...
Answer:
Integrating ClaudeKit into your workflow involves a structured setup process 
designed to enhance Claude Code without disrupting existing configurations. 
Below is the technical breakdown of installation, configuration, and safety 
mechanics.

### **Installation and Initial Setup**
To install ClaudeKit, you must first install the CLI globally using a package 
manager like npm or bun:
*   **Command:** `npm install -g claudekit-cli` or `bun add -g claudekit-cli` 
[1].
*   **Project Initialization:** Navigate to your project folder and run **`ck 
init`** [2]. 
*   **Setup Modes:** You can choose between a **Global** install (stored in 
`~/.claude/` for all projects) or a **Local** install (stored in `./.claude/` 
for the specific project) [2]. 
*   **Authentication:** The system uses a multi-layer authentication check, 
looking for `GITHUB_TOKEN`, GitHub CLI login, OS Keychain, or an interactive 
prompt to download the kits from private repositories [2, 3].

### **Configuring Permissions**
ClaudeKit allows you to control how much autonomy the AI has through various 
permission modes:
*   **Auto Mode (Recommended):** Uses a background classifier (Sonnet 4.6) to 
review every action. It automatically allows safe operations (like reading 
files) and blocks dangerous ones (like `curl | bash` or infrastructure changes) 
[4, 5].
*   **Full Bypass (`bypassPermissions`):** Skips all confirmation prompts. This 
should only be used in isolated environments like containers or VMs as it 
removes all safety rails [6, 7].
*   **Custom Rules:** You can define fine-grained **allow/deny/ask** rules in 
`settings.local.json` to control specific tools or file paths (e.g., 
`Read(./.env)` can be set to "deny") [7, 8].

### **Hook Orchestration**
Hooks are shell commands triggered by **lifecycle events** (e.g., when a session
starts or a tool is used) [9]. 
*   **Setup:** Hooks are configured within the `settings.json` file [9].
*   **Capabilities:** They can inject project-specific rules into every prompt, 
block sensitive file access via the `privacy-block.cjs` hook, or automatically 
save and restore session progress via `session-state.cjs` [10-12].

### **IDE Integration**
ClaudeKit integrates with VS Code and its forks (like **Cursor** or 
**Windsurf**) via the Claude Code extension [13, 14].
*   **Configuration:** You must open the IDE's `settings.json` and add 
environment variables to the `environmentVariables` block [15, 16].
*   **Routing:** By overriding variables such as `ANTHROPIC_BASE_URL` and 
`ANTHROPIC_MODEL`, you can route your IDE's Claude extension through **CCS 
(Claude Code Switch)** to use alternative providers like GLM or Kimi while still
using ClaudeKit's logic [14, 15, 17].

### **Coexistence and Safety Mechanics**
ClaudeKit is designed to coexist peacefully with existing Claude Code setups 
through several safety layers:
*   **Selective Merging:** Instead of overwriting your `settings.json`, it 
performs a selective merge, injecting only necessary hooks and MCP servers while
preserving your custom entries [18].
*   **Protected Files:** It identifies and **preserves** critical user files 
such as `CLAUDE.md`, `.gitignore`, `.mcp.json`, and `.ck.json` [19].
*   **Ownership Tracking:** The system uses a `metadata.json` file to track 
which files are "ClaudeKit-owned." This ensures that when you update or use the 
`--fresh` reset command, the system only touches its own files and leaves your 
manual modifications alone [20].
*   **Conflict Resolution:** In interactive mode, if a file conflict is 
detected, the system prompts you to choose between overwriting, a smart merge, 
or skipping the file [18, 21].

### **Migration Path to Other AI Tools**
The **`ck migrate`** command allows you to port your entire ClaudeKit 
"intelligence layer" to other AI coding tools [22].
*   **Supported Targets:** You can migrate to **Cursor, Windsurf, Codex, 
Droid,** and several others [23].
*   **How it Works:** The tool reads your `.claude/` directory and converts 
agents, skills, and rules into the native format of the target tool (e.g., 
converting rules into `.cursorrules`) [23, 24].
*   **Modes:** You can use **`--install`** to manually select items to migrate 
or **`--reconcile`** to automatically sync changes based on checksums [25].
*   **Safety:** You can run **`ck migrate --dry-run`** to see exactly what files
will be created or changed before any writes occur [26, 27].

Resumed conversation: 783e867c-d143-49ef-97bd-5984b9928dd4

## Failure modes + debugging — fix-logs, session-recovery, error patterns

Different notebook specified, starting new conversation...
Continuing conversation 783e867c...
Answer:
Based on the provided sources, ClaudeKit handles failures through a combination 
of automated state persistence and structured diagnostic pipelines.

### **Common Failure Modes**
Users typically encounter the following disruptions:
*   **Rate Limits and Account Bans:** AI providers may reach usage limits 
mid-session, causing the "flow" to freeze [1, 2]. Additionally, using certain 
tools with Google accounts can trigger permanent bans for violating Terms of 
Service [3, 4].
*   **Context Bloat:** Sessions exceeding **100K tokens** often become sluggish 
or unstable. In these cases, simply resuming the session "moves the problem" 
rather than fixing it [5, 6].
*   **Circular Logic/Infinite Loops:** If a bug fix fails more than three times,
the system recognizes a "wicked problem" or architectural deadlock and stops to 
prevent wasting tokens [7].
*   **Session Timeouts:** If the terminal is closed or the connection is lost 
for more than **10 minutes**, the session will timeout [8].

### **Error Logs and Diagnosis**
ClaudeKit does not just react to errors; it requires a structured 
"evidence-based" approach to diagnose them:
*   **Log Capture:** Users are instructed to pipe application output to a file 
(e.g., `npm run dev 2>&1 | tee logs.txt`) [9, 10].
*   **Diagnosis Appearance:** A typical log file contains standard terminal 
output, stack traces, and error messages. The **debugger agent** specifically 
reads the **last 30 lines** of this file first to focus on the most recent 
failure [7, 11].
*   **Diagnostic Mechanism (`/ck:fix`):** When triggered with a log file, the 
system runs a **6-phase pipeline**:
    1.  **Scout:** Gather evidence from logs and stack traces [12].
    2.  **Diagnosis:** Perform **Root Cause Analysis (RCA)** based on evidence, 
not guessing [12, 13].
    3.  **Routing:** Determine the complexity and choose a workflow [12].
    4.  **Fix:** Implement the changes [9].
    5.  **Verification:** Run tests and add **regression tests** to prevent the 
bug from returning [12].
    6.  **Prevention:** Document the fix in a journal or plan [13].

### **Recovery Procedures and State Persistence**
ClaudeKit uses the `session-state.cjs` hook to ensure work is rarely lost [14].

**Recoverable State:**
The system automatically saves the following to 
`.claude/session-state/.last-state.md`:
*   The current implementation **plan** [15].
*   **Todo items** and progress context [15, 16].
*   Outputs from various **subagents** [15].
*   The status of the current **Git branch and commits** [15].

**The Recovery Workflow:**
*   **`/resume`:** Used when the context is "healthy." It restores full context 
from the last session ID or name [5, 17].
*   **`ccs <profile> --resume`:** A specific recovery path that allows users to 
switch providers (e.g., from Claude to GLM) to finish the same task if the 
primary provider hits a rate limit [18, 19].
*   **`/export`:** Used when a session is **bloated**. It exports the essential 
conversation to a text file, allowing the user to start a "fresh" session and 
paste only the critical context [5, 6].

**What Cannot Be Recovered:**
*   **Isolated Sessions:** Sessions within **CCS sub-accounts** (e.g., switching
between "work" and "personal" profiles) are completely isolated because they use
different configuration directories (`CLAUDE_CONFIG_DIR`) [20, 21]. You cannot 
`/resume` across these isolated instances without manually copying the `.jsonl` 
session files [21].

Resumed conversation: 783e867c-d143-49ef-97bd-5984b9928dd4

## What ClaudeKit does NOT cover — gaps for harness-comparison

Different notebook specified, starting new conversation...
Continuing conversation 783e867c...
Answer:
Across the 21 sources, **ClaudeKit** is defined as an advanced **framework** and
"super-powered toolbox" that sits on top of AI models, but the documentation 
explicitly identifies several areas that are out of scope, deferred, or 
recommended to be handled elsewhere.

### 1. What ClaudeKit is Explicitly NOT Solving
*   **Model Provisioning & Subscriptions:** ClaudeKit is a productivity layer, 
**not an AI model provider**. It does not include access to AI models; users 
must maintain their own subscriptions (e.g., Claude Pro, Team, or Enterprise) to
use the system [1, 2].
*   **Hard Enforcement of Rules:** The `CLAUDE.md` file acts as "guidance" (a 
recipe book), not absolute enforcement [3, 4]. The AI may still miss 
instructions. For guaranteed enforcement (e.g., auto-formatting or blocking 
commands), the docs recommend using **Hooks** or **Permissions** in 
`settings.json` [4, 5].
*   **Quota Generation:** While the **Claude Code Switch (CCS)** allows for 
account rotation, it **cannot generate more quota** [6]. If multiple accounts 
share a common upstream pool, the system will still hit limits [6].
*   **Absolute Security Safety:** The "Auto Mode" for permissions is explicitly 
labeled a **"Research Preview."** While safer than full bypass, it does not 
provide 100% security against hallucinations or destructive commands (like `rm 
-rf`) [7, 8].
*   **Automated Backups:** Destructive commands like `ck init --fresh` (full 
reset) do **not have an auto-backup** feature [9, 10]. Users are warned to back 
up their configurations manually [10].
*   **Native IDE Chat Replacement:** ClaudeKit configuration only applies to the
**Claude Code extension** within IDEs like VS Code, Cursor, or Windsurf. It does
**not** affect the native, built-in AI chat features of those IDEs [11].
*   **Infinite Context Management:** Although it includes session recovery, it 
does not "solve" context bloat. Sessions exceeding **100K tokens** are 
considered "bloated," and the system admits that `/resume` won't help; users 
must manually `/export` and start fresh [12, 13].

### 2. Niche Comparison: Where ClaudeKit Fits
ClaudeKit occupies a specific middle-ground niche compared to other tools:

*   **vs. Raw Claude Code:** Raw Claude Code is an interactive terminal chatbot;
ClaudeKit is a **professional automation system** [14]. It moves from manual 
"chatting" to structured "commands" (e.g., `/ck:fix` vs. asking Claude to find a
bug) [15, 16].
*   **vs. Codex CLI:** Codex is a native runtime for OpenAI. ClaudeKit acts as 
the **"Intelligence Layer"** (skills, agents, rules) that can be migrated into 
the Codex runtime via `ck migrate` [17, 18]. It adds the management features 
(quota tracking, dashboard) that Codex lacks natively [18, 19].
*   **vs. Other AI Tools (Cursor, Windsurf, etc.):** Unlike IDE-locked tools, 
ClaudeKit is **CLI-first, modular, and portable** [20]. Its niche is 
**portability**; through `ck migrate`, a user can take their custom agents and 
rules and install them into Cursor or Windsurf, ensuring their "intelligence" 
isn't locked to one platform [21, 22].

### 3. Gaps for a Personal Harness to Provide
Based on these limitations, a user's personal harness would need to provide:
1.  **State/Config Backups:** Since ClaudeKit lacks auto-backups for its 
destructive commands [9].
2.  **External Enforcement:** Tools like git-hooks or CI/CD gates to enforce the
coding standards that ClaudeKit only "suggests" [4].
3.  **Cross-Account Session Sync:** Manual movement of `.jsonl` session files is
required if the user wants to resume sessions across isolated CCS sub-accounts 
[23].
4.  **External Security Sandboxing:** Because the permissions mode is a preview,
running ClaudeKit in a **container or isolated VM** is still recommended for 
high-risk operations [8].

Resumed conversation: 783e867c-d143-49ef-97bd-5984b9928dd4

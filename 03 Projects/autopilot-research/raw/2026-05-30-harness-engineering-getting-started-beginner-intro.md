# Harness Engineering — getting started / beginner introduction (Vietnamese anchor) <!-- compiled: 2026-05-30 -->

**Notebook:** 4c7d51e4-b450-4504-933b-3bb4be28b393
**Sources:** 6 YouTube videos
**Generated:** 2026-05-30 (overnight orchestrator)
**Query:** `harness engineering beginner introduction getting started Claude Code`

## Sources

1. [20260530] **Tù Bà Khuỳm** — Bắt đầu Harness Engineering từ đâu? Từ đây!!
   - https://www.youtube.com/watch?v=gQLhchHmRKs
   - 469 views, 26:04 duration
2. [20260207] **John Kim** — How I use Claude Code (Meta Staff Engineer Tips)
   - https://www.youtube.com/watch?v=mZzhfPle9QU
   - 435,040 views, 46:12 duration
3. [20251217] **AI with Avthar** — How I Start EVERY Claude Code Project
   - https://www.youtube.com/watch?v=aQvpqlSiUIQ
   - 113,587 views, 34:15 duration
4. [20260413] **Productive Dude** — FULL Claude Tutorial For Beginners in 2026! (FULL COURSE)
   - https://www.youtube.com/watch?v=Xg55nTrbYYY
   - 423,842 views, 112:38 duration
5. [20260405] **Maddy Zhang** — How I use Claude Code (Senior Software Engineer Tips)
   - https://www.youtube.com/watch?v=MzhIr7BfpI0
   - 138,116 views, 9:46 duration
6. [20260522] **Caleb Writes Code** — Agent Harness explained in 8min..
   - https://www.youtube.com/watch?v=1a1VXDdIyrk
   - 114,644 views, 8:20 duration

---

## 1. Summary

The 
documentation highlights the use of **coding agents** and specialized 
**plug-ins** to automate complex development tasks, such as implementing 
authentication, payment systems, and audio transcription. One creator emphasizes
a **systematic workflow** that utilizes **SQL databases** and **CLI tools** to 
maintain project structure and prevent development drift. Another comprehensive 
tutorial explores **Claude's desktop features**, specifically focusing on 
**artifacts**, **connectors**, and **specialized skills** for enterprise-level 
automation. Collectively, the materials advocate for moving beyond "freestyle 
prompting" toward a **blueprint-oriented approach** that leverages **Model 
Context Protocol** (MCP) for deep system integration. This shift ensures that 
**AI-driven development** remains efficient, scalable, and grounded in best 
practices.

---

## 2. Trends

Answer:
Across the provided sources, a clear consensus emerges regarding the evolution 
of AI-assisted development: the industry is shifting from simple **prompt 
engineering** to **harness engineering**, where the focus is on creating a 
structured environment and orchestration layer for agents to operate 
autonomously [1, 2].

The following are the dominant tactical trends and shared patterns advocated by 
the speakers.

### 1. The "Plan-First" Methodology
A recurring theme is that engineers should never allow an agent to write code 
immediately. Instead, they must enforce a rigorous planning phase.
*   **Plan Mode vs. Act Mode:** **John Kim** and **Maddy Zhang** both emphasize 
using Claude Code's "Plan Mode" almost exclusively at the start of a task to 
verify assumptions and establish an execution spec [3-5].
*   **The PSB System:** **Avthar** formalizes this into the **PSB (Plan, Setup, 
Build)** system. He spends 15 minutes planning before any coding to avoid hours 
of "messy, inefficient" output [6, 7].
*   **Initial Questioning:** **Avthar** and **Productive Dude** both suggest 
telling the AI to ask *you* questions to clarify the goal and find edge cases 
before implementation begins [8-10].
*   **The PRD/Spec Requirement:** **Caleb Writes Code**, **Tù Bà Khuỳm**, and 
**Avthar** all advocate starting with a detailed **Production Requirement 
Document (PRD)** or project spec doc that outlines product goals and technical 
architecture [2, 11-14].

### 2. Context Engineering and the `claude.md` "Project Brain"
The speakers agree that **context is king**, and managing it is the primary 
bottleneck for AI performance [15, 16].
*   **Project Memory:** A shared pattern is the creation of a `claude.md` file 
(or `agent.md`) that serves as the project’s permanent memory, containing rules,
tech stack preferences, and directory maps [17-20].
*   **Keeping it Lean:** **Avthar**, **John Kim**, and **Maddy Zhang** warn 
against "bloating" this file. **John Kim** suggests a 300-line limit, while 
**Maddy Zhang** recommends staying under 200 lines to ensure the agent doesn't 
lose track of key constraints [18, 21, 22].
*   **The "Clear" Habit:** **Maddy Zhang** and **John Kim** advocate for using 
the `clear` command constantly to ensure every task begins with a fresh, clean 
context window, preventing stale history from confusing the agent [5, 23, 24].
*   **Automated Documentation:** **Avthar** and **John Kim** use specialized 
docs like `architecture.md`, `changelog.md`, and `project_status.md` to offload 
detailed context from the main `claude.md` file, linking to them only when 
needed [25-27].

### 3. Self-Validation Loops and Hooks
Speakers emphasize creating a "harness" where the agent can catch its own 
mistakes through automation.
*   **Validation Harness:** **Maddy Zhang** describes wiring up "Hooks" (scripts
that fire automatically) to run builds, tests, and type-checkers every time a 
change is saved [28, 29].
*   **Regression Prevention:** **Avthar** recommends "regression prevention" by 
using specific commands (like a `#` shortcut) to immediately update `claude.md` 
with new rules when a mistake is identified, ensuring the agent doesn't repeat 
it [30].
*   **Trace and Friction Tracking:** **Tù Bà Khuỳm** uses a local **SQLite 
database** to store traces of agent actions, which helps identify "friction" and
build a backlog for improving the harness itself [31-33].

### 4. Parallelism and Multi-Agent Workflows
Advanced users no longer treat the agent as a single chat partner but as a fleet
of workers.
*   **Multiple Instances:** **John Kim** describes "Starcraft-style" 
development, juggling multiple terminal instances of Claude Code simultaneously 
to work on different features or projects at once [34-36].
*   **Git Worktrees:** **Avthar**, **John Kim**, and **Maddy Zhang** all 
advocate for **Git Worktrees**. This allows multiple Claude sessions to work on 
separate branches of the same repository in isolated directories without 
conflicting with each other [29, 37-39].
*   **Sub-Agents:** **Caleb Writes Code** and **Maddy Zhang** discuss using 
sub-agents for specialized, atomic tasks (like a "Security Reviewer" or "DB 
Specialist") to keep the main orchestration context clean [1, 40].

### 5. Standardized Tooling Choices
The sources reveal a "meta" tech stack that multiple speakers prefer for 
high-velocity AI building:
*   **Frontend/Styling:** Next.js, Tailwind CSS, and Shadcn UI [17, 41, 42].
*   **Authentication & Payments:** Clerk for auth and Stripe for payments 
[41-43].
*   **Deployment:** Vercel (for hosting/previews) and Netlify [42, 44-46].
*   **Protocols:** Heavy reliance on **MCP (Model Context Protocol)** servers to
give Claude access to external tools like Google Drive, GitHub, Notion, and 
databases [47-51].
*   **Prompting Frameworks:** **Productive Dude** teaches the **GCAO** (Goal, 
Context, Action, Output) framework for prompts, while also introducing the 
**DBS** (Direction, Blueprints, Solutions) framework for creating "Skills" [52, 
53].

Resumed conversation: 83527c35-609a-4abe-8876-61e54ad7bff0

---

## 3. Outliers

While the speakers agree on the core principles of harness engineering, they 
diverge significantly on specific tactical implementations, particularly 
regarding context management, the use of external tools (MCPs), and project 
memory storage.

### 1. Divergence on Context Management and `claude.md`
The speakers disagree on what constitutes a "lean" project memory and how much 
detail to include in the `claude.md` file.
*   **Optimal File Length:** **Maddy Zhang** is the most conservative, 
recommending a limit of **100 to 200 lines max** to avoid diluting the signal 
[1]. **John Kim** allows for more breathing room, suggesting around **300 
lines** is a decent target [2]. 
*   **The "Clear" Habit:** **Maddy Zhang** advocates for using the `/clear` 
command "constantly" to ensure each task starts with a fresh session [3, 4]. 
Conversely, **John Kim** and **Avthar** place more emphasis on **resuming 
sessions** and using long-running threads that evolve, provided they are managed
through automated document updates [5, 6].

### 2. Contrarian Views on MCPs (Model Context Protocol)
A major point of contention is whether to embrace or avoid MCP servers.
*   **The Advocate:** **Productive Dude** and **Avthar** treat MCPs as essential
extensions that make Claude more powerful by connecting it to databases, Google 
Drive, and Slack [7, 8].
*   **The Contrarian:** **John Kim** explicitly states that he tries **"very 
very hard to not use MCPs."** [9]. He argues that they "blow up your context 
window" and token usage, preferring to write manual scripts for validation 
instead of relying on third-party protocols [9].

### 3. Outlier Opinion: Markdown vs. SQLite for Memory
Most speakers rely on Markdown files (`.md`) for maintaining project state. **Tù
Bà Khuỳm** presents a unique technical outlier in this area.
*   **The SQL Approach:** While others use `claude.md` or `architecture.md`, 
**Tù Bà Khuỳm** has moved away from Markdown for his harness V2. He advocates 
for using a **local SQLite database** to store project decisions and traces, 
arguing that a database is more precise and less prone to being ignored or 
filled incorrectly by the agent compared to a text file [10, 11].

### 4. Differing Parallelism Strategies
The speakers suggest different ways to handle multiple tasks simultaneously.
*   **Starcraft-Style Juggling:** **John Kim** advocates for running **multiple 
terminal instances** of Claude Code and "juggling" them manually to handle 
context switching across different projects or features [12, 13].
*   **Git Worktrees:** **Avthar** and **Maddy Zhang** prefer a more structured 
"Git Worktree" approach. This involves creating multiple physical directories 
for the same repo, each on a different branch, to prevent agents from stepping 
over each other's files during parallel execution [14-16].

### 5. Disagreement on UI Visualizations
Within the Claude web interface, there is a divergence in how to view data.
*   **Artifacts vs. Inline:** **Productive Dude** expresses a preference for 
**turning off inline visualizations**, preferring to stick strictly to 
**Artifacts** to keep the chat cleaner [17]. Other speakers, however, lean into 
inline visualizations for quick dashboarding and projection mapping within the 
chat flow [18, 19].

### 6. Divergent Prompting Frameworks
The speakers teach competing proprietary frameworks for interacting with the AI:
*   **Productive Dude** teaches the **GCAO** (Goal, Context, Action, Output) 
framework for individual prompts [20] and the **DBS** (Direction, Blueprints, 
Solutions) framework for building skills [21].
*   **Avthar** promotes the **PSB** (Plan, Setup, Build) system, which focuses 
more on the high-level project lifecycle than the specific syntax of a single 
prompt [22].

Conversation: 83527c35-609a-4abe-8876-61e54ad7bff0 (turn 1)

---

## 4. Gaps

While the sources provide an excellent tactical foundation for high-velocity, 
AI-assisted development, they primarily focus on **individual or small-team 
productivity** and the "happy path" of project creation. When moving these 
"harnesses" into a **large-scale production environment**, several critical gaps
emerge.

The following areas are largely unaddressed in the sources and represent 
significant risks for production-grade implementation.

### Gaps in the Current Sources

*   **Enterprise-Grade Security & Data Privacy:** While speakers like **John 
Kim** and **Avthar** mention using `.env` files for secrets [1, 2] and 
**Productive Dude** mentions turning off data training [3], there is no 
discussion on **data residency**, **PII (Personally Identifiable Information) 
masking**, or how to prevent an autonomous agent from accidentally leaking 
internal project specs into public-facing PRs. 
*   **Cost Management & Token Governance:** Most speakers advocate for using 
**Claude 3.5 Opus** almost exclusively for its quality [4, 5]. While **John 
Kim** mentions using `/context` to audit token bloat [6], the sources lack a 
systematic approach to **budgeting**, **spend alerts**, or **rate-limit 
management** for a multi-developer team where autonomous agents might run in 
loops for hours.
*   **Production Observability for Agents:** **Tù Bà Khuỳm** introduces a 
"trace" system in SQLite to track agent actions [7, 8], but this is localized. 
In production, you need **centralized observability**—if an autonomous blogger 
(like the one built by **Productive Dude**) hallucinates or fails on a schedule 
[9, 10], how do you receive alerts, monitor success rates, or perform "root 
cause analysis" on the agent's reasoning?
*   **Legal & Intellectual Property (IP) Compliance:** None of the sources 
address the legal ramifications of shipping AI-generated code to production. 
There is no guidance on **license scanning** for libraries the AI might suggest 
or the **IP ownership** of the generated output in a commercial context.
*   **Harness Versioning & Testing:** The speakers treat `claude.md` as an 
evolving "Project Brain" [11-13]. However, they do not explain how to **test the
harness itself**. If you change a rule in `claude.md`, how do you ensure it 
doesn't cause a regression in the agent's performance across 50 different 
sub-tasks?

---

### 6 Specific Follow-up Topics to Investigate

If you are implementing harness engineering for a production environment, you 
should investigate these specific areas:

1.  **LLM Evals (Evaluation Frameworks):** Move beyond "vibes" for testing your 
harness. Research tools like **Promptfoo** or **LangSmith** to create a suite of
test cases that run against your `claude.md` instructions to ensure new "rules" 
don't break old functionality.
2.  **Agentic Security & RBAC (Role-Based Access Control):** Investigate how to 
limit an agent's permissions. For example, ensuring an MCP server (like the one 
for GitHub or Databases [14, 15]) can only perform "Read" operations on certain 
directories and requires human approval for "Write" operations on the `main` 
branch.
3.  **Token Usage Monitoring & Observability:** Explore centralized platforms 
(like **Helicone** or **Literal AI**) that can track token costs, latency, and 
agent trajectories across your entire engineering team, providing a "God view" 
of your AI spend.
4.  **IP & License Scanning Integration:** Research tools that can be integrated
into your **Validation Loop** (mentioned by **Maddy Zhang** and **John Kim** 
[16, 17]) to automatically scan every line of code generated by Claude for 
copyright infringements or incompatible licenses.
5.  **CI/CD for the Harness:** Treat your `claude.md`, skills, and prompts as 
**Infrastructure as Code (IaC)**. Investigate how to create a deployment 
pipeline for your harness so that updates to project rules are 
version-controlled and tested before being rolled out to the whole team.
6.  **Human-in-the-Loop (HITL) Orchestration:** While the videos mention "asking
for permission" [18, 19], research more complex orchestration patterns like 
**LLM-assisted code review** where one agent generates the code and a different,
"cynical" agent reviews it against your company's specific security and style 
standards before a human ever sees it.

Conversation: 83527c35-609a-4abe-8876-61e54ad7bff0 (turn 1)

---

## 5. Takeaways

Adopt a "Plan-First" workflow:** Start every project by creating a 
comprehensive **Production Requirement Document (PRD)** or project spec file 
(`spec.md`) to define the product goals and technical architecture before any 
coding begins [1-3].
2. **Mandate Plan Mode for new features:** Always initiate new tasks in **"Plan 
Mode"** rather than "Act Mode" to force the agent to outline its logic, identify
technical risks, and ask clarifying questions before it touches a single file 
[4-6].
3. **Maintain a lean `claude.md` "Project Brain":** Use a `claude.md` file at 
the project root to store essential rules and tech stack preferences, but 
**Maddy Zhang** and **John Kim** warn to keep it between **100 and 300 lines** 
to prevent context dilution [7-9].
4. **Structure prompts with GCAO:** Follow **Productive Dude's** GCAO 
framework—**Goal, Context, Action, and Output format**—to ensure the agent 
understands the "why" behind a task and delivers the exact data structure 
required [10].
5. **Establish an automated Validation Loop:** Configure **hooks** that 
automatically trigger build steps, unit tests, and type-checkers after every 
file change, allowing the agent to "see" its own errors and fix them without 
human intervention [11, 12].
6. **Practice aggressive "Context Hygiene":** Use the `/clear` command 
**constantly** between unrelated tasks to wipe stale history, ensuring the agent
operates within a fresh, focused context window for every new sub-feature [6, 
13].
7. **Scale with Git Worktrees:** To work on multiple features simultaneously, 
use **Git Worktrees** to isolate different branches into separate physical 
directories, allowing multiple Claude sessions to run in parallel without file 
conflicts [14, 15].
8. **Offload documentation via linking:** Keep the main `claude.md` file concise
by linking to specialized, automated documents like `architecture.md`, 
`changelog.md`, and `project_status.md` instead of duplicating that information 
in the main rules file [16, 17].
9. **Implement Regression Prevention:** When an agent makes a mistake, don't 
just fix the code; immediately update the project rules by using the **`#` 
(hashtag) shortcut** to ensure the agent never repeats that specific error [18, 
19].
10. **Track friction with a "Trace" system:** For advanced setups, **Tù Bà 
Khuỳm** suggests using a **local SQLite database** to store "traces" of agent 
decisions and failures, creating a data-driven backlog to refine the automation 
harness over time [20, 21].

Conversation: 83527c35-609a-4abe-8876-61e54ad7bff0 (turn 1)

---

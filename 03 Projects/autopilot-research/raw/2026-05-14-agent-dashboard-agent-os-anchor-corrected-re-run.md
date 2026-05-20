# Agent Dashboard / Agent OS — anchor-corrected re-run

**Notebook:** 1cd445b9-d834-4686-9fd0-12f4d67ce9d6
**Sources:** 2 YouTube videos
**Generated:** 2026-05-14 (overnight orchestrator)
**Query:** `Chase AI Claude Code dashboard status line slash commands observability 2026`

## Sources

1. [20260511] **Chase AI** — Claude Code Just Got a Dashboard
   - https://www.youtube.com/watch?v=7zxIeRWasbc
   - 51,398 views, 3:24 duration
2. [20260316] **Matt Pocock** — 5 Claude Code skills I use every single day
   - https://www.youtube.com/watch?v=EJyuu6zlQCg
   - 337,559 views, 16:42 duration

---

## 1. Summary

The author emphasizes 
that treating the AI like a human engineer with no memory requires structured 
workflows, including **PRD generation** and modular codebase architecture. 
Another source introduces the **Agents View** dashboard, a new feature that 
allows developers to manage multiple concurrent AI sessions from a single 
interface. This dashboard categorizes tasks into **active, completed, or 
input-required** states, helping users track complex, parallel projects without 
losing focus. Together, these materials offer a comprehensive guide to 
**steering AI agents** through sophisticated prompt engineering and organized 
project management.

---

## 2. Trends

Answer:
The dominant trends across these videos center on **industrializing the use of 
AI agents** by moving away from casual prompting toward **strict process 
engineering** and **centralized orchestration**. While Matt Pocock focuses on 
the internal logic and "skills" used to steer agents, Chase AI focuses on the 
external management and visibility of multiple concurrent agent sessions.

### 1. Multi-Agent Orchestration and Parallelism
A major shared pattern is the move toward running multiple agent sessions 
simultaneously to handle complex or high-volume workloads.

*   **Matt Pocock** advocates for a **"parallel agent setup"** where background 
tasks can be fired off at once [1]. He specifically uses a technique where an 
agent **spawns three to five "sub-agents" in parallel**, each tasked with 
producing radically different architectural designs for a codebase refactor [2, 
3]. 
*   **Chase AI** highlights the necessity of the new **"Agents View" dashboard**
(accessed via the `claude agents` command) to manage this parallelism [4]. He 
notes that developers often have "three, four, five, six different terminal 
windows open" and uses the dashboard to consolidate these into a single view 
divided into "needs input," "working," and "completed" sections [4].

### 2. Tactical "Steering" and Process Engineering
Both speakers emphasize that agents require active human intervention and 
well-defined workflows to remain productive.

*   **Strict Process as "Steering":** Matt Pocock argues that because agents 
have no memory and can be "middling" engineers, they require **"extremely strict
and well-defined processes"** to produce useful code [5]. He uses a library of 
"skills" (short markdown-based instructions) to encode these processes, ensuring
the AI walks down a "strict path" every time [5, 6].
*   **Human-in-the-Loop Management:** Chase AI utilizes the dashboard to "peek 
in" on sessions using the spacebar, effectively "poking my head into the room" 
to provide quick direction (e.g., "Okay cool do X Y and Z") without fully 
leaving the main dashboard [4].
*   **Backgrounding Tasks:** Chase AI advocates for the **`/bg` (background)** 
command, which allows a developer to start a complex task (like brainstorming 
titles or building a landing page) and immediately shift it to the background 
dashboard to free up the terminal [4].

### 3. Integration with Professional Engineering Practices
A recurring theme is treating AI agents not as magic tools, but as "humans with 
weird constraints" who must follow standard industry practices [7].

*   **Test-Driven Development (TDD):** Matt Pocock uses a specific **TDD skill**
that forces agents into a **red-green-refactor loop**, requiring them to write a
failing test before writing the implementation code [8, 9].
*   **Vertical Slicing (Tracer Bullets):** Pocock insists on breaking large 
projects (defined in PRDs) into **"vertical slices" or "tracer bullets"**—tasks 
that cut through all integration layers to flush out "unknown unknowns" early 
[10].
*   **GitHub-Centric Workflows:** Pocock’s "Ralph loop" (his autonomous agent 
setup) operates by taking PRDs, turning them into **GitHub issues**, and then 
looping over those issues until they are closed [11, 12]. He even uses agents to
create "Refactor RFCs" as GitHub issues [3].

### 4. Architectural Design and Shared Understanding
Both speakers suggest that for AI to be effective, the codebase and the 
project's goals must be structured for clarity.

*   **Reaching Shared Understanding:** Matt Pocock uses a **"Grill me" skill** 
that forces the AI to interview him "relentlessly" about a design before it 
starts coding [13, 14]. He utilizes **"design trees"** to resolve dependencies 
between decisions one by one [14, 15].
*   **Interface-Driven Design:** Pocock argues that AI struggles with "shallow" 
modules (many small, undifferentiated files) [16, 17]. He advocates for an 
**"improve codebase architecture" skill** to deepen modules and create thin 
interfaces, which makes it easier for the AI to navigate and test the codebase 
[2, 16, 17].
*   **Visualizing Workflows:** Chase AI emphasizes that **visibility** is key to
preventing sessions from falling behind; if a developer doesn't "visually see" 
the status of multiple hooks, they tend to forget about them for hours [4].

Resumed conversation: 7907cf34-e743-4271-96b2-3dde0efa1046

---

## 3. Outliers

While the two speakers both utilize Claude Code, they diverge significantly in 
their **philosophical approach to the developer’s role** and their **tactical 
priorities** regarding how to manage AI limitations.

### 1. Depth of Interaction vs. Breadth of Management
The most striking divergence is in how much time each speaker spends "inside" a 
single agent session versus managing many.
*   **Matt Pocock (The "Deep Diver"):** He advocates for **high-touch, intensive
sessions**. He describes sitting for "30, 40, 50 questions" over "half an hour  
45 minutes" just to reach a "shared understanding" with the AI before a single 
line of code is written [1, 2]. For Pocock, the value is in the rigor of the 
pre-coding interview [3].
*   **Chase AI (The "Orchestrator"):** He prioritizes **high-volume 
throughput**. His focus is on the "Agents View" dashboard to manage "six 
different sessions" at once [4]. He views the interaction as "poking my head 
into the room" to give quick directions like "Okay cool do X Y and Z" before 
immediately switching to another task [4].

### 2. Solving "Agent Amnesia" vs. "Human Forgetfulness"
Both speakers address the issue of memory, but they identify different 
"forgetful" parties as the primary bottleneck.
*   **Pocock on Agent Memory:** He takes a contrarian view of the AI, calling 
agents "middling engineers" who "have no memory" [5]. Because they don't 
remember previous successes or failures, he believes the solution is 
**"extremely strict and well-defined processes"** encoded into markdown "skills"
[5].
*   **Chase AI on Human Memory:** He focuses on the developer’s tendency to 
"fall behind" or forget about background tasks [4]. He argues that "no matter 
how many hooks you have going on, if you don't visually see it, you tend to 
forget about it" [4]. His solution is **visual dashboarding** rather than strict
process engineering.

### 3. Contrarian Take: Clearing Context to Improve Quality
Matt Pocock offers a specific, counter-intuitive technique for improving code 
quality that diverges from the standard "more context is better" approach.
*   **Pocock's "Wiping Memory" Strategy:** He observes that LLMs are often 
"reluctant to refactor their own code" while it is still in their active context
window [6]. His outlier advice is that **clearing the context** makes the agent 
"a lot less precious about the code that it's just written," leading to better 
refactors [6].

### 4. Technical Rigor vs. Tooling Convenience
The speakers diverge on what they believe constitutes the "real" work of using 
AI agents.
*   **Matt Pocock (Engineering First):** He argues that "real engineering 
skills" (like TDD and vertical slicing) are more important than the AI tool 
itself [7, 8]. He explicitly states that in his training, he is "really not 
teaching Claude code that much" but is instead teaching **"steering" and 
architectural taste** [8].
*   **Chase AI (Dashboard First):** He presents the **CLI and dashboard 
features** as the primary solution ("a godsend") to the friction of modern AI 
development [4]. His focus is on the commands—like `claude agents` and 
`/bg`—that simplify the user experience of running multiple agents [4].

### 5. Architectural Philosophies
Pocock introduces a specific architectural opinion that is absent from Chase 
AI’s workflow.
*   **Pocock’s "Deep Module" Preference:** He advocates against "shallow" 
codebases with many small files, which he finds confuses AI [9]. He pushes a 
specific agenda of **"deepening" modules and creating "thin interfaces,"** 
arguing that AI produces "garbage" if the codebase architecture is sloppy [10, 
11]. Chase AI does not touch on codebase structure, focusing instead on the 
**visibility of the task status** (Needs Input, Working, Completed) [4].

Conversation: 7907cf34-e743-4271-96b2-3dde0efa1046 (turn 1)

---

## 4. Gaps

While the sources provide an excellent tactical guide for individual developer 
productivity, they leave several critical gaps regarding **enterprise-grade 
production implementation**. The sources focus heavily on local CLI usage, 
personal workflows, and individual "skill" development rather than 
organizational guardrails.

### **Gaps for Production Implementation**

*   **Cost Management and Token Economics:** While the speakers advocate for 
"grilling" sessions that last 45 minutes [1] and running "six different 
sessions" simultaneously [2], there is no mention of the **financial cost** or 
**token consumption**. In a production environment, an organization would need 
to manage API budgets and rate limits across an entire team of developers using 
these high-token-usage workflows.
*   **Security and Data Privacy:** The sources show Claude Code exploring the 
codebase and executing terminal commands [3, 4]. They do not address **security 
permissions**, such as how to prevent an agent from accessing sensitive `.env` 
files, or the privacy implications of sending proprietary code to a third-party 
LLM for processing.
*   **Multi-User Coordination:** The "Agents View" dashboard is presented as a 
way for a *single* user to manage their own sessions [2]. There is no 
information on how **distributed teams** should coordinate; for example, how to 
prevent two different developers' agents from attempting to refactor the same 
module simultaneously, leading to massive merge conflicts.
*   **Agentic Guardrails:** Matt Pocock mentions that agents can be "sloppy" or 
produce "garbage" if the codebase is poor [5]. However, there is no discussion 
of **automated guardrails**—software layers that sit between the agent and the 
system to prevent destructive terminal commands (like `rm -rf /`) or 
unauthorized cloud infrastructure changes.
*   **CI/CD Integration:** The workflows described are strictly local 
terminal-based [2]. For production-grade engineering, it is unclear how these 
"Ralph loops" [4] or skills would integrate with remote **CI/CD pipelines** 
(like GitHub Actions) to automate refactoring or testing without a human sitting
at a dashboard.

---

### **5 Recommended Follow-up Topics**

1.  **Agentic Security & Sandboxing:** Investigate how to run Claude Code in a 
restricted environment or container to ensure it cannot access sensitive 
credentials or perform unauthorized system operations.
2.  **Enterprise Observability for AI Agents:** Research tools that can log and 
audit agent actions, costs, and decisions at an organizational level, rather 
than just in a local terminal window.
3.  **Token Optimization Strategies:** Explore advanced context management 
techniques to reduce the cost of the "30, 40, 50 questions" sessions described 
by Matt Pocock [1].
4.  **Collaborative Agent State:** Investigate if there are ways to share an 
agent's "shared understanding" [4, 6] and history with other team members so a 
lead engineer can review an agent's logic before it commits code.
5.  **LLM-Specific TDD Frameworks:** Since the sources advocate for TDD as a 
"steering" mechanism [7], investigate specialized testing frameworks designed 
specifically to catch LLM-induced regressions and hallucinations in real-time.

Conversation: 7907cf34-e743-4271-96b2-3dde0efa1046 (turn 1)

---

## 5. Takeaways

Based on the strategies shared by Matt Pocock and Chase AI, here are nine 
actionable rules and configurations for developers adopting Claude Code:

1.  **Enforce a "Grill me" session:** Before starting any code, use a specific 
skill to force the agent to interview you relentlessly about your plan to reach 
a "shared understanding" and resolve design dependencies [1-3]. (Matt Pocock)
2.  **Centralize sessions with the `claude agents` dashboard:** Use this command
to consolidate multiple terminal windows into a single "Agents View" that 
categorizes tasks by status (needs input, working, or completed) [4]. (Chase AI)
3.  **Deconstruct projects into "vertical slices":** Break your PRDs into 
"tracer bullets" that cut through all integration layers at once to flush out 
"unknown unknowns" before committing to a full implementation [5]. (Matt Pocock)
4.  **Utilize the `/bg` command for multitasking:** Shift long-running tasks, 
like brainstorming or site building, to the background dashboard immediately so 
your main terminal remains free for active work [4]. (Chase AI)
5.  **Mandate a strict TDD loop:** Encode a "Test-Driven Development" skill that
forces agents to follow a red-green-refactor cycle, writing a failing test 
before any implementation code is added [6, 7]. (Matt Pocock)
6.  **"Peek" into sessions using the spacebar:** Use the dashboard’s peek 
feature to quickly monitor a session’s progress and provide brief steering 
commands without the friction of fully switching contexts [4]. (Chase AI)
7.  **Optimize for "Deep Modules":** Restructure your codebase into larger 
modules with thin interfaces; agents struggle with "shallow" architectures made 
of many small, undifferentiated files [8, 9]. (Matt Pocock)
8.  **Wipe context to improve refactors:** If an agent is reluctant to change 
its own work, clear its context window to remove its "memory" and make it less 
"precious" about the code it just wrote [7]. (Matt Pocock)
9.  **Parallelize design proposals with "sub-agents":** For complex refactors, 
instruct the AI to spawn three to five sub-agents in parallel to produce 
radically different interface designs for you to compare and choose from [10]. 
(Matt Pocock)

Conversation: 7907cf34-e743-4271-96b2-3dde0efa1046 (turn 1)

---

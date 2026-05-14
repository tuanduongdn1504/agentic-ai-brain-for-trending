<!-- compiled: 2026-05-14 → wiki/codex/ -->
# Codex — long-running agentic harness alternative to Claude Code

**Notebook:** 01707594-d36a-4a2f-b3f8-7fa9044528ba
**Sources:** 6 YouTube videos
**Generated:** 2026-05-13 (overnight orchestrator)
**Query:** `OpenAI Codex agentic harness long running Claude Code add codex 2026`

## Sources

1. [20260206] **Keith AI** — Master OpenAI Codex in 26 minutes
   - https://www.youtube.com/watch?v=EwVs3O2Zm6I
   - 69,312 views, 26:45 duration
2. [20260325] **The AI Automators** — Anthropic Just Dropped the New Blueprint for Long-Running AI Agents.
   - https://www.youtube.com/watch?v=9d5bzxVsocw
   - 172,627 views, 16:58 duration
3. [20260420] **Riley Brown** — Codex Full Course 2026: The NEW Best AI Coding Tool
   - https://www.youtube.com/watch?v=KXIdYEdOPys
   - 127,673 views, 103:13 duration
4. [20260323] **Teacher's Tech** — Claude Code: Build Your First AI Agent
   - https://www.youtube.com/watch?v=gHB4JFG9i3k
   - 188,378 views, 25:37 duration
5. [20260324] **Programming with Mosh** — Claude Code Tutorial - Build Apps 10x Faster with AI
   - https://www.youtube.com/watch?v=IuyVVtr1uhY
   - 307,541 views, 58:11 duration
6. [20260429] **Jack Roberts** — Claude Code just got 10X Better (Codex + Gemini)
   - https://www.youtube.com/watch?v=ETvz1qhQDXE
   - 44,184 views, 17:51 duration

---

## 1. Summary

The content provides a comprehensive guide to **vibe coding**, 
showing how natural language can be used to deploy functional websites and 
software while maintaining a sophisticated **agentic relationship** with 
artificial intelligence.

---

## 2. Trends

Answer:
The dominant trends across these sources focus on transforming AI from a simple 
chat interface into a **long-running, autonomous agent** capable of handling 
complex engineering and research tasks [1-3]. The shared patterns emphasize 
**orchestration layers (harnesses)**, **persistent project memory**, and 
**multi-agent/multi-model collaboration** to overcome context limitations and 
quality regression [4-7].

### 1. Tactical Practices: Planning and Persistent Context
A recurring theme is the transition from "micromanaging" AI to defining 
high-level goals through **agentic workflows** [3].
*   **Planning Mode:** Multiple speakers advocate for using a dedicated 
**"Planning Mode"** (often triggered by Shift+Tab) to allow the agent to draft a
multi-step to-do list before changing any code [8-10]. This prevents the agent 
from going down the wrong path [11].
*   **Project Memory Files (`claude.md` / `agents.md`):** Mosh and Teacher's 
Tech both emphasize the **`claude.md` file** as the "single most important" 
setup step [7, 12]. It acts as an onboarding document containing project 
context, rules, and architecture that the agent reads at every startup [7, 12, 
13]. Keith AI uses a similar **`agents.md`** file and automates its updates to 
resolve misunderstandings between the user and the agent [14].
*   **Context Management:** To handle long sessions, speakers recommend 
**context compaction** (summarizing the thread) or **context resets** (starting 
fresh with a summary file) to avoid "context anxiety," where the model rushes to
finish as the window fills up [15-18].

### 2. Tooling Choices: Terminal Integration and Parallelism
The sources highlight a shift toward tools that live in the **terminal** or 
integrate directly with the **file system** [19, 20].
*   **Coding Agents:** **Claude Code** and **OpenAI Codex** are the primary 
tools discussed [21, 22]. Mosh notes that Claude Code is editor-agnostic and 
lives in the terminal, allowing it to execute shell commands and git workflows 
autonomously [19, 23, 24].
*   **Parallelism and Git Work Trees:** Keith AI and Riley Brown emphasize 
**multitasking** by running multiple agent threads in parallel [25-27]. They 
utilize **Git work trees** to isolate these tasks into separate 
folders/branches, preventing agents from interfering with each other's code 
before merging the final results [28, 29].
*   **Voice Input:** To speed up the prompting process, Riley Brown, Keith AI, 
and Mosh all utilize or recommend **Whisper Flow** or built-in dictation tools, 
noting that speaking is significantly faster than typing [30-32].

### 3. Recurring Techniques: Adversarial and Multi-Model Evaluation
Speakers widely advocate for using one AI to judge or improve the work of 
another to solve the problem of poor self-evaluation [33, 34].
*   **Adversarial Evaluation:** The AI Automators describe a 
"generator-evaluator" pattern inspired by GAN networks, where a dedicated 
**evaluator agent** is prompted to be skeptical of the code produced by the 
generator agent [34, 35].
*   **The "Three Brain" Strategy:** Jack Roberts introduces a **"Three Brain 
Auto-Router"** skill that tags in the best model for a specific job: **Claude** 
for building, **Gemini** for long-context analysis (videos/PDFs), and 
**Codex/GPT-5.5** for adversarial review [36-38].
*   **Skills and Automations:** Riley Brown and Keith AI both focus on creating 
**"Skills"**—reusable workflow packages—and **"Automations"**—cron jobs that run
these skills on a schedule (e.g., weekly SEO reports or nightly skill 
maintenance) [39-42].

### 4. Shared Philosophy: The "Carpenter" Mindset
Mosh and Teacher's Tech both argue that while AI handles the "mechanical" or 
"repetitive" parts of coding, the **fundamentals of software engineering** 
remain essential [43-45]. Mosh uses the analogy of a **power saw**: it doesn't 
replace the carpenter but allows them to work faster and with more precision, 
though the carpenter must still understand the design and measurements [44].

Resumed conversation: 7894c3a0-d234-41c1-a830-dc86bfaea633

---

## 3. Outliers

While the speakers generally agree on the power of agentic workflows, they 
diverge significantly regarding model reliability, the necessity of multi-model 
setups, and the fundamental role of the human engineer.

### 1. Claude Code’s Performance and Reliability
The most direct contradiction concerns the current state of **Claude Code**.
*   **The "Forest Gump" Take:** **Jack Roberts** presents a contrarian view, 
stating that Claude Code's performance has recently "gotten a little bit worse" 
and suffered from "quality regression" [1, 2]. He jokes that users expected 
"Albert Einstein" but "Forest Gump turned up," noting he has personally seen the
model produce incorrect results it previously handled well [1, 3].
*   **The Revolutionary Take:** Conversely, **Mosh Hamadani** and **Teacher's 
Tech** describe the tool as life-changing and highly effective for building 
production-grade software [4-6]. Mosh emphasizes that it allows for building 
apps "10x faster" and is the "best option out there right now" [4, 7].

### 2. Multi-Model vs. Single-Model Strategies
Speakers diverge on whether a single high-end model is sufficient or if a 
"multi-brain" approach is required.
*   **The "Three Brain" Advocate:** **Jack Roberts** argues that relying on one 
model is a mistake because every model has "blind spots" [2]. He advocates for a
router system that tags in **Gemini** for long-context video/PDF tasks and 
**OpenAI Codex** for adversarial code reviews, using Claude only for the primary
build [2, 8].
*   **The "Simplified Harness" Shift:** **The AI Automators** highlight a 
divergence within Anthropic’s own research. While they initially used a complex 
"multi-agent harness" (planner, generator, evaluator), they found that with the 
release of **Opus 4.6**, they could simplify the architecture by removing 
sprints and context resets, effectively "one-shotting" entire apps due to the 
model's improved 1-million-token context window [9, 10].

### 3. "Vibe Coding" vs. "Real Engineering"
There is a philosophical divide regarding the level of human involvement and the
target audience for these tools.
*   **The Engineering Purist:** **Mosh Hamadani** explicitly distances his 
approach from what he calls "VIP coding experiments" or "product manager" 
workflows where "50 AI agents build an app while you sleep" [11, 12]. He insists
that software engineering is not going anywhere and that developers must 
**review every line of code** and apply solid engineering practices [11, 13].
*   **The Vibe Coding Multitasker:** **Riley Brown** and **Keith AI** lean into 
a "vibe coding" philosophy, focusing on **multitasking** and running 10+ tasks 
in parallel [14, 15]. Riley Brown often uses "full access" permissions to let 
the agent "cook" while he moves on to other tasks, suggesting that the goal is 
to become an "effective multitasker" rather than a line-by-line reviewer [14, 
16].

### 4. Technical Outliers and Contrarian Views
*   **Cynicism Toward Context Windows:** **The AI Automators** offer a cynical 
take on Anthropic’s 1-million-token context window. They suggest it is in 
Anthropic's "best interest to process tokens" for revenue, and therefore they 
are skeptical of claims that "context anxiety" has been fully solved in the 
latest models [17].
*   **The Case Against "Self-Evaluation":** **The AI Automators** point out a 
specific failure mode: Claude is a **"poor QA agent"** by default [18]. They 
note that in testing, Claude often identified legitimate bugs but then "talked 
itself into deciding they weren't a big deal" and approved the work anyway [18].
*   **Figma Integration:** While **Riley Brown** acknowledges Figma is a 
standard, he offers the contrarian view that its AI integration is "really bad" 
compared to specialized agent-first tools like **Paper**, which he finds "way 
more fun" and functional [19, 20].
*   **Tool Choice Risks:** **Keith AI** provides a warning about tool choice, 
noting that using **Claude Code** within third-party wrappers like **Open Code**
might carry a "risk of being banned" by Anthropic, leading him to recommend 
different tools depending on whether a user is a "Claude fan" or a multi-model 
user [21].

Conversation: 7894c3a0-d234-41c1-a830-dc86bfaea633 (turn 1)

---

## 4. Gaps

While the sources provide a comprehensive blueprint for individual developers to
build and deploy applications using agentic workflows, they leave several 
critical gaps regarding **enterprise-scale production** and **team 
collaboration**. The current material focuses heavily on the "solopreneur" or 
"carpenter" mindset, where one human guides one or more agents [1, 2].

### Identified Gaps for Production Implementation

*   **Team-Scale Collaboration and Synchronization:** The sources extensively 
discuss **Git work trees** and **parallel threads** for a single developer [3, 
4], but they do not address how a team of 10 or 20 engineers should manage these
agents simultaneously. Gaps include handling **merge conflicts between multiple 
agents** and maintaining a shared "Project Memory" (`claude.md` or `agents.md`) 
that evolves across a distributed team [5, 6].
*   **Infrastructure Security and Granular Permissions:** While "sandbox mode" 
and "full access" are mentioned, they are presented as a binary choice for a 
local machine [7, 8]. Production environments require **Granular IAM (Identity 
and Access Management)**—specific protocols for what an agent can access in an 
AWS/Azure environment, how it handles secrets, and how to prevent **prompt 
injection** from escalating privileges.
*   **Structured Observability and Monitoring:** The videos show "spinny 
circles" and to-do lists to track progress in real-time [9, 10]. However, for 
production systems, you need **asynchronous logging and performance monitoring**
to track agent success rates, "context anxiety" behaviors [11], and 
cost-per-feature over time across thousands of sessions.
*   **Data Residency and Compliance:** Implementing these tools in sectors like 
finance or healthcare requires knowledge of **Data Sovereignty**. The sources do
not cover how to ensure tokens sent to Anthropic or OpenAI APIs for long-context
tasks [12, 13] comply with GDPR, SOC2, or HIPAA requirements, nor do they 
discuss the implications of using "web search" tools in highly regulated 
environments [14].
*   **Automated Quality Gates:** Mosh and Anthropic emphasize "human oversight" 
and reviewing "every line of code" [1, 15]. In a high-velocity production 
environment, you need **automated gates**—moving beyond adversarial evaluation 
[16] to hard-coded CI/CD triggers that block agent-generated code if it fails 
security scans or integration tests, without requiring a human to manually 
"approve" every step.

---

### Recommended Follow-up Topics for Investigation

1.  **Enterprise IAM for AI Agents:** Researching how to implement **Least 
Privilege Access** for agentic tools. Investigate how to limit an agent's 
terminal access to specific subnets or non-production environments to mitigate 
the risks associated with "elevated access" [8].
2.  **Advanced CI/CD Guardrails:** Investigate "Minion" architectures (like the 
one Stripe uses) that move the evaluation of code from a prompted agent [17] to 
**deterministic, hard-coded quality gates** that run automatically upon every 
git commit.
3.  **Data Privacy and Token Masking:** Explore tools and techniques for **PII 
(Personally Identifiable Information) Redaction** before sending code or project
context to external LLM providers to maintain compliance with data residency 
laws.
4.  **Agentic Observability Platforms:** Look into specialized monitoring tools 
(like LangSmith or Arize Phoenix) that provide **traceability for multi-step 
agent decisions**, allowing you to audit why an agent chose a specific tool or 
"talked itself into" approving mediocre work [18].
5.  **Cost Optimization at Scale:** Beyond just checking your weekly usage [19],
investigate **Token Caching strategies**, model distillation, and the use of 
smaller, cheaper models for "mechanical" tasks like linting, while reserving 
expensive models like Opus for complex planning [20, 21].
6.  **Collaborative State Management for Agents:** Investigating how to 
synchronize **persistent project memory** across a team. This would involve 
moving `claude.md` from a local file [22] to a centralized, version-controlled 
knowledge base that all team members and their respective agents can query and 
update.

Conversation: 7894c3a0-d234-41c1-a830-dc86bfaea633 (turn 1)

---

## 5. Takeaways

To optimize a developer’s workflow with agentic tools like Claude Code and 
OpenAI Codex, the following rules and configurations should be adopted:

*   **Initialize a Project Memory File:** Create a **`claude.md` or `agents.md` 
file** in your root directory to act as an "onboarding document" that the agent 
reads at every startup to understand project architecture and conventions [1, 
2]. Teacher's Tech calls this the "single most important thing" for ensuring the
agent follows your specific rules without repetition [2, 3].
*   **Utilize "Planning Mode" for Complex Tasks:** Always toggle into **Planning
Mode (Shift + Tab)** before executing a multi-step task to allow the agent to 
draft a to-do list and implementation plan for your approval [4, 5]. Mosh 
Hamadani and Teacher's Tech advocate for this "plan first, build second" 
approach to prevent the agent from going down the wrong path [6, 7].
*   **Implement a "Three Brain" Auto-Router:** Adopt Jack Roberts’ strategy of 
using **Claude for building**, **Gemini for long-context analysis** (videos and 
massive PDFs), and **GPT/Codex for adversarial review** [8, 9]. This allows you 
to leverage the unique strengths of each model while avoiding the "blind spots" 
of a single-model setup [8, 10].
*   **Isolate Parallel Tasks with Git Work Trees:** When running multiple 
engineering tasks simultaneously, use **Git work trees** to separate threads 
into different folders [11]. Keith AI explains that this prevents agents from 
interfering with the same code at the same time, allowing for seamless merging 
later [11, 12].
*   **Deploy Adversarial Evaluation Harnesses:** To solve the problem of "poor 
self-evaluation," configure a **dedicated evaluator agent** with a system prompt
instructed to be skeptical of the generator agent's output [13, 14]. The AI 
Automators note that Claude often "talks itself into" approving mediocre work 
unless an adversarial judge is wired into the production loop [14, 15].
*   **Active Context Management:** Regularly use the **`/compact` command** to 
summarize your conversation history or **`/clear`** when switching to unrelated 
tasks to prevent "context anxiety" and hallucinations [16, 17]. Mosh warns that 
a full context window leads to lower quality responses and higher token costs 
per request [17, 18].
*   **Establish Automated Maintenance Loops:** Set up **"Upskill" and "Update 
agents.md" automations** to run on a nightly or weekly schedule [19, 20]. Keith 
AI uses these cron jobs to have the AI analyze recent interactions, detect 
misunderstandings, and automatically update its custom instructions to improve 
future performance [20, 21].
*   **Leverage High-Speed Voice Input:** Use tools like **Whisper Flow** or 
built-in dictation to "vibe code" at the speed of thought [22, 23]. Riley Brown 
and Keith AI emphasize that speaking prompts is two to three times faster than 
typing, which is essential for managing multiple agents in parallel [23, 24].
*   **Create Modular "Workflow" Recipes:** Instead of complex one-off prompts, 
write **plain English workflow files** that describe repeatable processes 
step-by-step [25, 26]. Teacher's Tech suggests these recipes outperform "sloppy 
prompts" by providing the agent with a clear reason-and-adapt framework [27, 
28].
*   **Maintain "Real Engineering" Oversight:** Never allow agents to "one-shot" 
entire applications without **reviewing every line of generated code** and 
backing changes with automated tests [29, 30]. Mosh Hamadani insists that while 
AI handles the "mechanical parts," the developer must remain the "carpenter" who
understands the architecture and final craft [31, 32].

Conversation: 7894c3a0-d234-41c1-a830-dc86bfaea633 (turn 1)

---

<!-- compiled: 2026-05-14 → wiki/harness-engineering/ (extension: 4 personal-repo-* articles added alongside existing 10) -->
# Harness Engineering — personal-repo continuation (Vietnamese practitioner take + more)

**Notebook:** 58c51d8e-ab36-4331-993f-8a61dfd0a2c4
**Sources:** 6 YouTube videos
**Generated:** 2026-05-13 (overnight orchestrator)
**Query:** `harness engineering Claude Code agent repository structure personal 2026`

## Sources

1. [20260207] **John Kim** — How I use Claude Code (Meta Staff Engineer Tips)
   - https://www.youtube.com/watch?v=mZzhfPle9QU
   - 420,701 views, 46:12 duration
2. [20251217] **AI with Avthar** — How I Start EVERY Claude Code Project
   - https://www.youtube.com/watch?v=aQvpqlSiUIQ
   - 108,822 views, 34:15 duration
3. [20260325] **The AI Automators** — Anthropic Just Dropped the New Blueprint for Long-Running AI Agents.
   - https://www.youtube.com/watch?v=9d5bzxVsocw
   - 172,627 views, 16:58 duration
4. [20260205] **GritAI Studio** — Master Context in Claude Code in 5 Minutes
   - https://www.youtube.com/watch?v=I1EGbrH5Xdk
   - 19,814 views, 7:08 duration
5. [20260413] **Productive Dude** — FULL Claude Tutorial For Beginners in 2026! (FULL COURSE)
   - https://www.youtube.com/watch?v=Xg55nTrbYYY
   - 316,563 views, 112:38 duration
6. [20260304] **Simon Scrapes** — How to Use Claude Code Skills Like the 1% (it’s easy actually)
   - https://www.youtube.com/watch?v=6-D3fg3JUL4
   - 180,539 views, 16:33 duration

---

## 1. Summary

The provided sources explore advanced methodologies for building and managing 
**AI agents**, specifically focusing on **Anthropic's Claude** models and the 
**Claude Code** terminal interface. Key concepts include the use of a 
**harness**, which acts as an orchestration layer to provide **validation 
loops** and **constraints** that keep long-running agents on track. The text 
details specialized features like **Skills** and **MCP (Model Context 
Protocol)**, which allow agents to interact with external tools, file systems, 
and custom workflows. To prevent **context anxiety** and hallucinations, the 
materials advocate for **context engineering** through manual compaction and the
use of **sub-agents** for isolated research. The sources also highlight 
**adversarial evaluation**, where separate generator and evaluator agents work 
together to ensure high-quality, objective outputs. Ultimately, the 
documentation serves as a guide for transitioning from generic prompting to 
building sophisticated, **autonomous agentic systems** capable of complex 
software development and professional tasks.

---

## 2. Trends

Answer:
Across the sources, a paradigm shift is evident from "freestyle prompting" to 
**systematic agent orchestration**, which speakers refer to as building a 
"harness" or "context engineering" [1-3]. The dominant trends focus on 
maintaining a specialized project memory, ruthlessly managing the context 
window, and utilizing multi-agent architectures to ensure reliability.

### 1. The `claude.md` File as Project Memory
The most significant tactical pattern is the use of a **`claude.md` file** 
located in the project's root directory to act as the "memory" for the AI agent 
[4, 5].
*   **John Kim** (Meta Staff Engineer) recommends running the `/init` command to
have Claude analyze the codebase and generate this file automatically [6]. He 
advises keeping it under 300 lines to avoid token bloat and suggests using it to
define high-level technical architecture and validation loops [7, 8].
*   **Avthar** (AI with Avthar) views `claude.md` as the core of his "PSB" 
(Plan, Setup, Build) system [4, 9]. He uses it to store project goals, design 
style guides, and "repository etiquette," such as telling Claude never to push 
directly to the main branch [10, 11].
*   **Simon Scrapes** frames the file as a **Standard Operating Procedure 
(SOP)** that tells Claude what "good" looks like and what to avoid [12, 13].

### 2. Tactical Context Engineering
Multiple speakers advocate for **"context engineering"** rather than relying on 
the model's default behavior [3, 14].
*   **GritAI Studio** describes context as an **"attention budget"** and warns 
that too much information causes confusion while too little leads to 
hallucinations [3]. They advocate for **manual summarization** (saving state to 
`progress.md`) over "autocompact," because the latter might discard critical 
decisions [15-17].
*   **The AI Automators** highlight **"context anxiety,"** a phenomenon where 
agents rush through tasks or quit early as their context window fills up [18]. 
Their tactical solution is a "context reset," where a fresh agent starts with a 
clean slate but reads from a tracking file to maintain continuity [19].
*   **John Kim** uses the `/context` command frequently to audit token usage and
identify "offenders" like bloated MCPs (Model Context Protocol) [14].

### 3. Tooling and the "Agent Harness"
The concept of a **"harness"**—the software and structure wrapping the model to 
keep it reliable—is a recurring theme [1, 20].
*   **The AI Automators** use a car analogy: the model is the engine, but the 
harness is the car that makes it useful [20]. They advocate for **adversarial 
evaluation**, where a "Generator" agent writes code and a "Skeptical Evaluator" 
agent probes for edge cases and design "slop" [21, 22].
*   **Productive Dude** highlights the use of **Dispatch**, a feature that acts 
as a computer harness, allowing Claude to interact with file systems and apps 
even when the user is away [23].
*   **Tooling Preferences:** Across the videos, the **Model Context Protocol 
(MCP)** is the universal choice for connecting Claude to external tools like 
Google Drive, GitHub, Notion, and databases [24-27].

### 4. Advanced Multi-Agent and Sub-agent Workflows
Speakers move beyond single-chat interactions toward parallel, multi-instance 
development.
*   **John Kim** describes his workflow as "juggling" multiple Claude instances 
in the terminal, comparing the experience to playing **Starcraft** [28, 29]. He 
uses **sub-agents** for atomic tasks to protect the main context window from 
bloat [30, 31].
*   **Avthar** advocates for **issue-based development**, where GitHub issues 
are the "source of truth" [32, 33]. He uses **Git worktrees** to allow multiple 
Claude instances to work on different branches simultaneously within the same 
project [34, 35].
*   **GritAI Studio** recommends using the "Explore" sub-agent for deep research
because it isolates the reading of dozens of files, returning only a clean 
summary to the main session [16].

### 5. Structured Frameworks (GCAO, PSB, and DBS)
Tactical practices are often organized into proprietary but overlapping 
frameworks:
*   **GCAO (Productive Dude):** A prompting sequence standing for **Goal, 
Context, Action, and Output** format [36].
*   **PSB (Avthar):** A project management approach: **Plan** (brainstorming and
spec docs), **Setup** (GitHub, `.env`, `claude.md`), and **Build** (MVP and 
milestones) [9].
*   **DBS (Avthar/Productive Dude):** A framework for creating skills: 
**Direction** (step-by-step workflow), **Blueprints** (examples/references), and
**Solutions** (reusable scripts or code) [37, 38].
*   **Simon Scrapes** warns against "skill bloat," advising users to build 
**fewer, high-quality skills** with specific trigger descriptions rather than 
installing thousands of generic ones, which can cannibalize each other and fail 
to activate [39, 40]

Resumed conversation: 1aaae80f-1e9d-45a6-a49d-f18ec404a7da

---

## 3. Outliers

While the sources agree on the foundational importance of context management and
structured project memory (the `claude.md` file), they diverge sharply on the 
reliability of automated features, the optimal quantity of skills, and whether 
the model can be trusted to evaluate its own work.

### 1. Skill Density: Quality vs. Quantity
A major point of contention exists regarding how many "skills" a developer 
should install.
*   **Simon Scrapes** offers a **contrarian take**, criticizing the trend of 
installing "hundreds or sometimes even thousands" of marketplace skills [1, 2]. 
He argues that this "skill bloat" makes agents slower and less predictable 
because Claude must scan every name and description, leading to "noisy menus" 
and "cannibalization" [2, 3]. He advocates for a curated set of **20 to 30 
well-built skills** [4].
*   **John Kim** (Meta Staff Engineer) takes a more liberal approach, noting 
that users can "download hundreds of skills" to manage git and other workflows, 
focusing on using specific **keywords** to trigger them rather than limiting 
their quantity [5, 6].

### 2. Auto-Compaction vs. Manual Control
Speakers disagree on whether Claude’s built-in "autoco compaction" feature is 
reliable enough for production work.
*   **GritAI Studio** explicitly warns **against autocompact**, calling it a 
"problem" because Claude decides what to throw away, which often results in 
losing "important decisions" and "losing control of the narrative" [7]. They 
advocate for **manual summarization** via a `progress.md` file instead [8].
*   **John Kim** diverges here, stating that he **usually just lets the autoco 
compaction work** for his projects, finding that it does a "pretty good job" for
his needs [9].
*   **The AI Automators** take a **cynical view** of Anthropic’s claims 
regarding the new Opus 4.6 model's ability to rely solely on compaction. They 
suggest it is in Anthropic's "best interest to process tokens" (getting users to
send 1-million-token requests) and argue that the "context reset" is still 
superior for long-running tasks [10].

### 3. Reliability of Self-Evaluation
The sources reveal a split regarding whether an AI agent can effectively grade 
its own performance.
*   **The AI Automators** highlight a "failure mode" where an agent asked to 
evaluate its own work will **"praise it" even if the quality is mediocre** [10].
They reveal that "out of the box Claude is a poor QA agent" because it 
identifies issues and then "talks itself into deciding they weren't a big deal" 
[11]. They argue the only reliable solution is **adversarial evaluation** (a 
separate evaluator agent) [12].
*   **John Kim** and **Avthar**, by contrast, place higher trust in **validation
loops**. Kim suggests that simply having a "loop of validation" where the AI 
builds and compiles is enough for it to "self-improve and keep going until it 
fixes itself" [13].

### 4. The "No-Code" Engineer vs. The AI Employee
There is a philosophical divergence on the future role of the software engineer.
*   **John Kim** presents an **outlier opinion** among the group, stating he is 
"one of those engineers that are **basically not writing code anymore**" [14]. 
He describes his role as 12 hours a day of "actively pair programming" and 
"reviewing every single line" [14]. He argues the era of writing code by hand is
"essentially over" [15].
*   **Avthar** and **Productive Dude** still frame the AI as a **"co-worker" or 
"extra employee"** that helps the human build faster, but they still emphasize 
the human-led "Plan, Setup, Build" (PSB) phases and the need for the human to 
answer "hard-hitting questions" during development [16-18].

### 5. Tooling Choice: Web UI vs. Terminal
The speakers contradict each other on which interface is most "expert."
*   **John Kim** states he **"dropped basically all" IDEs** like VS Code or 
Cursor to work exclusively in terminal-based Claude Code [19].
*   **Productive Dude** argues that the **Web UI features** like **Artifacts** 
(mini-apps) and **Visualizations** are "magical" and allows users to create 
"living breathing documents" that cannot be replicated in a standard terminal 
[20, 21]

Conversation: 1aaae80f-1e9d-45a6-a49d-f18ec404a7da (turn 1)

---

## 4. Gaps

While the sources provide a sophisticated blueprint for using Claude in a 
development environment, they primarily focus on individual developer 
productivity and "harness" design for solo projects. For a **production-level 
implementation** within an enterprise or a professional engineering team, there 
are several critical gaps regarding security, cost governance, and automated 
reliability.

### Key Gaps for Production Implementation

*   **Enterprise Secrets Management:** The sources suggest using `.env` files or
adding API keys directly to the Anthropic cloud environment [1-3]. In a 
production setting, this is insufficient. There is no mention of integrating 
with **Secrets Managers** (like AWS Secrets Manager, HashiCorp Vault, or Google 
Secret Manager) to rotate credentials or manage access across a large team of 
agents.
*   **Observability and Distributed Tracing:** While John Kim mentions 
monitoring tokens with `/context` [4] and GritAI discusses a context dashboard 
[5], the sources lack a strategy for **Production Observability**. There is no 
discussion of how to trace a multi-agent "hand-off" that fails in the middle of 
the night during a scheduled task [6] or how to log agent "thinking" for audit 
trails in a centralized system like Datadog or ELK.
*   **Rigorous "Evals" vs. "Vibes":** John Kim admits that evaluating agentic 
workflows is currently based largely on **"vibes"** and testing for a few weeks 
before landing code [7]. A production-grade system requires a **deterministic 
Evaluation Framework** (Evals) to measure regression. The sources discuss 
"adversarial evaluation" between agents [8], but not how to build a permanent, 
version-controlled suite of benchmarks to ensure a prompt update doesn't break a
critical feature.
*   **Cost Governance and Unit Economics:** Speakers acknowledge that sessions 
can be "expensive"—one build cost $125 [9, 10]. However, there is no guidance on
**budget capping, rate-limit management, or cost-per-feature analysis** for a 
team scaling these agents. Implementing this in production requires a layer to 
intercept and manage token spend across many parallel "multi-clauding" instances
[11, 12].
*   **Legal and IP Compliance:** The sources focus on building fast, but they do
not address **data residency requirements** (like GDPR or HIPAA) or the 
**intellectual property risks** of having an AI write a codebase. There is no 
mention of scanning generated code for open-source license violations (e.g., 
ensuring an agent doesn't accidentally pull in GPL-licensed code).

---

### Follow-up Topics for Investigation

To move from a "personal harness" to a production-ready system, consider 
investigating the following five topics:

1.  **AI Orchestration Governance:** Research how to implement **Role-Based 
Access Control (RBAC)** for agents. If an agent has "file system access" [13] or
"network egress" [14], how do you restrict it from accessing sensitive HR or 
financial directories within a corporate network?
2.  **LLM Observability Platforms:** Investigate tools like **LangSmith, Arize 
Phoenix, or Weights & Biases**. These platforms allow you to visualize the full 
trace of an agent's logic, including tool calls and sub-agent outputs, which is 
essential for debugging production failures.
3.  **Automated Evaluation (Evals) Frameworks:** Look into building a library of
**"golden sets"**—proven inputs and expected outputs—to run against your 
`claude.md` or skill updates. This ensures that a change to your "Project 
Memory" [15, 16] doesn't degrade performance on previous milestones.
4.  **Agentic CI/CD Pipelines:** Explore how to version-control your **"Harness"
(prompts, skills, and MCP configurations)**. Just as you version-control your 
code, a production system needs a pipeline that tests and deploys the *agent's 
environment* itself to ensure consistency across the dev team.
5.  **Prompt Injection & Red Teaming for Agents:** Since these agents can 
interact with browsers [17, 18] and shell commands [19, 20], they are vulnerable
to **prompt injection**. Investigate how to "red team" your evaluator agents [8]
to ensure they cannot be tricked into bypassing security constraints or deleting
databases [21, 22].

Conversation: 1aaae80f-1e9d-45a6-a49d-f18ec404a7da (turn 1)

---

## 5. Takeaways

Based on the sources, here are ten actionable rules and configurations for 
developers to optimize their workflows with Claude and Claude Code:

1.  **Establish a Project Memory File:** Create a `claude.md` file in your root 
directory to act as the project's "memory," storing high-level architecture and 
requirements [1, 2]. **John Kim** recommends keeping this file under 300 lines 
to avoid token bloat and context confusion [3].
2.  **Use "Plan Mode" for New Features:** Always toggle into "Plan Mode" using 
`Shift+Tab` before starting a feature to verify architectural assumptions before
the AI executes code [4, 5]. **Avthar** refers to this as the "Plan" phase of 
his PSB system, where you force the AI to ask you clarifying questions [6, 7].
3.  **Adopt the GCAO Prompting Framework:** Structure every prompt using the 
**Goal, Context, Action, and Output** format to avoid generic, low-quality 
responses [8]. **Productive Dude** suggests attaching data like CSV analytics as
context to ground the AI's "Action" in real-world facts [9, 10].
4.  **Implement Adversarial Evaluation:** To prevent "AI slop," use a 
multi-agent setup where a "Generator" agent creates code and a separate, 
skeptical "Evaluator" agent probes it for edge cases and design flaws [11, 12]. 
**The AI Automators** note that out-of-the-box Claude is often a poor QA agent 
that talks itself into approving mediocre work unless strictly prompted to be 
skeptical [12].
5.  **Prefer Manual Summarization over Autocompact:** Rather than relying on 
automatic context compaction, which can discard critical decisions, manually 
record your current state and next steps in a `progress.md` file [13, 14]. 
**GritAI Studio** advises clearing the context after saving this state to ensure
a "clean slate" for the next task [14, 15].
6.  **Curate a Minimalist Skill Library:** Limit your setup to 20–30 
high-quality, custom-built skills rather than installing hundreds of generic 
marketplace tools [16, 17]. **Simon Scrapes** warns that "skill bloat" makes 
agents slower and leads to "cannibalization," where multiple skills compete for 
the same command trigger [16, 18].
7.  **Isolate Research with Sub-agents:** Use sub-agents to perform deep 
research or read through dozens of files, as they operate in a separate context 
window [14]. This technique, advocated by **GritAI Studio** and **John Kim**, 
prevents your main conversation from becoming bloated with irrelevant research 
data [14, 19].
8.  **Enable Parallel Development with Git Worktrees:** Use **Git Worktrees** to
run multiple Claude instances simultaneously on different branches of the same 
codebase [20, 21]. **Avthar** and **John Kim** suggest this "multi-clauding" 
approach to work on several features or bugs in parallel without file conflicts 
[20, 22, 23].
9.  **Regularly Audit Token Usage:** Frequently run the `/context` command to 
see a visual representation of what is consuming your "attention budget" [13, 
24]. **John Kim** highlights that MCPs (Model Context Protocol) are often 
"biggest offenders" that can blow up your token costs if not monitored [24, 25].
10. **Use Regression Prevention Tags:** When Claude makes a mistake, use the `#`
or `pound` symbol to provide a correction that is automatically incorporated 
into your project rules [26]. **Avthar** advises this as a way to "patch" the 
AI's behavior on the fly so it never repeats the same error [26].

Conversation: 1aaae80f-1e9d-45a6-a49d-f18ec404a7da (turn 1)

---

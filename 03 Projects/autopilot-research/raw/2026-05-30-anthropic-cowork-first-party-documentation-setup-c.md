# Anthropic Cowork first-party documentation + setup-cowork skill <!-- compiled: 2026-05-30 -->

**Notebook:** b05d3444-6dbb-4955-a8fb-be9b021a0350
**Sources:** 4 YouTube videos
**Generated:** 2026-05-30 (overnight orchestrator)
**Query:** `Anthropic Cowork official documentation setup announcement onboarding`

## Sources

1. [20260223] **Eliot Prince** — Claude Cowork Plugins Explained (& how to build AI employees)
   - https://www.youtube.com/watch?v=1GZYNyuL6Lg
   - 135,561 views, 14:55 duration
2. [20260326] **Fireship** — Anthropic just released the real Claude Bot...
   - https://www.youtube.com/watch?v=wfeiCZK0mNs
   - 1,061,762 views, 5:00 duration
3. [20260410] **Darrel Wilson** — Claude Tutorial for Beginners — How to Use Claude AI Step by Step (2026)
   - https://www.youtube.com/watch?v=-xEF5WrdIWs
   - 113,272 views, 42:44 duration
4. [20260227] **Greg Isenberg** — What is Perplexity Computer?
   - https://www.youtube.com/watch?v=l-J8RodcM_A
   - 98,661 views, 37:56 duration

---

## 1. Summary

The transition to **Claude Co-work** and 
**Opus 4.6** enables users to build custom "AI employees" through advanced 
prompting and external connectors. Meanwhile, **Perplexity Computer** offers 
founders automated tools for high-level tasks like **investor research** and 
**hyper-personalized cold outreach**. Ultimately, these developments represent a
shift toward **distributed cognition**, where AI agents independently navigate 
the digital world to increase human productivity.

---

## 2. Trends

Answer:
The dominant trends across these sources indicate a paradigm shift where AI is 
no longer viewed as a simple chatbot, but as an **autonomous agent or "AI 
employee"** capable of executing complex, multi-step workflows.

The following tactical practices, tooling choices, and techniques are shared 
across the videos:

### 1. The Transition to Autonomous "AI Employees"
A major recurring theme is the move from basic prompting to building persistent 
workers. 
*   **Eliot Prince** describes this as moving from an LLM as a "brain" to 
**Plugins and Skills** acting as "hands" that execute tasks like a full job role
(e.g., a "Full Stack Marketer") [1, 2].
*   **Fireship** highlights **"Computer Use,"** which allows Claude to 
autonomously control a computer—opening apps, scheduling jobs, and even 
attending Zoom meetings to "defraud" employers by simulating human productivity 
[3, 4].
*   **Greg Isenberg** views **Perplexity Computer** as a replacement for human 
roles, noting that its ability to research and draft personalized outreach is 
literally a "marketing person's old job point blank" [5].

### 2. Hierarchical Tooling Architecture: Skills vs. Plugins
Both **Eliot Prince** and **Darrel Wilson** emphasize a structured hierarchy for
AI capabilities:
*   **Skills (The "Recipe"):** Prince defines a skill as a repeatable, 
single-task instruction (e.g., creating a branded invoice) [1]. Wilson views 
them as "references or outlines" that ensure output follows a specific format, 
such as a LinkedIn post [6, 7].
*   **Plugins (The "Chef"):** Prince describes plugins as bundles of multiple 
skills and connectors that represent an entire job function [8]. Wilson agrees, 
noting that plugins combine skills into one package to handle comprehensive 
tasks like marketing campaigns [9].

### 3. Tactical "Power User" Setup
The speakers advocate for specific configurations to maximize performance:
*   **Desktop Over Browser:** **Darrel Wilson** and **Eliot Prince** both argue 
that the **Claude Desktop App** is superior to the browser version because it is
faster, lacks propagation delays, and provides easier access to **Co-work, 
Plugins, and Skills** management [8, 10, 11].
*   **Grounding with Projects:** Prince and Wilson highlight **Claude Projects**
as essential for providing the AI with specific business context (PDFs, style 
guides) so it behaves like a tailored employee rather than a general assistant 
[12-14].

### 4. Recursive and "Mega" Prompting
Multiple speakers advocate for letting the AI improve its own instructions:
*   **Mega Prompts:** **Darrel Wilson** teaches a strategy where you ask the AI 
to "generate a complex prompt for you" based on a simple goal, noting that AI 
generally writes better prompts than humans [15, 16].
*   **Dynamic Use Cases:** **Greg Isenberg** uses a similar tactic with 
Perplexity Computer, asking it to identify the "five best non-obvious use cases"
for his specific needs before he begins a task [17].

### 5. Automated Outreach and Research Techniques
A shared pattern is using AI to perform deep research and outreach in parallel:
*   **Parallel Processing:** **Greg Isenberg** highlights that Perplexity 
Computer can research 30 companies simultaneously, finding founders and drafting
hyper-personalized "warm outbound" emails in one shot [18, 19].
*   **Competitive Intel on Autopilot:** Both Isenberg and Wilson demonstrate 
using AI to monitor competitors. **Isenberg** sets up recurring 8:00 AM checks 
for pricing changes or new features [5, 20]. **Wilson** uses "Vision" to have 
Claude critique his own landing pages and YouTube thumbnails against market 
trends [21, 22].

### 6. Bridging the "Action Gap" with Connectors and MCP
The speakers emphasize that AI must be able to "reach outside" the chat:
*   **Connectors:** **Greg Isenberg** and **Eliot Prince** use connectors for 
Gmail, Slack, and Google Drive to allow the AI to read and write data directly 
into business systems [19, 23].
*   **MCP (Model Context Protocol):** **Darrel Wilson** explains that while 
standard connectors often provide "read-only" access, **MCP plugins** are 
required if you want the AI to actually **send emails** or perform actions on 
your behalf [24, 25].
*   **Artifacts as Micro-Apps:** Wilson advocates for using **Artifacts** to 
build functional tools—like a TOS generator or a turn-based video game—which can
then be published and used as standalone web applications [26-28].

Resumed conversation: 86643620-0fca-482a-8a95-c9aaedca248a

---

## 3. Outliers

[ask failed: ]

---

## 4. Gaps

[ask failed: ]

---

## 5. Takeaways

Based on the provided sources, here are 10 actionable rules and configurations 
for developers and power users to adopt when building and managing AI agents:

1.  **Adopt "Mega Prompting":** Instead of writing complex prompts yourself, 
provide the AI with your goal and context, then ask it to generate a detailed 
"Mega Prompt" for itself, as AI often writes more effective instructions than 
humans [1-4]. (**Darrel Wilson**)
2.  **Prioritize Desktop over Browser:** Use the Claude Desktop application 
rather than the browser to gain faster propagation speeds and exclusive access 
to the library for managing personal **Skills** and **Plugins** [5, 6]. 
(**Darrel Wilson**)
3.  **Modularize AI Capabilities:** Architecture your "AI employees" by treating
**Skills** as individual "recipe cards" for single tasks and **Plugins** as the 
"experienced chef" that bundles multiple skills and tools to fulfill a complete 
job role [7-9]. (**Eliot Prince**)
4.  **Ground with Dedicated Projects:** Use **Claude Projects** to upload 
task-specific reference files (like PDFs or spreadsheets) and custom 
instructions that act as guidelines the AI must follow for every response within
that workspace [10-12]. (**Darrel Wilson**)
5.  **Enable Persistent "Vision" and "Web Search":** Keep these features active 
at all times to allow the AI to perform live market research, critique visual 
UI/UX elements, and provide summaries based on current events rather than 
outdated training data [1, 13]. (**Darrel Wilson**)
6.  **Bridge the Action Gap with MCP:** If you need an agent to do more than 
just read data, install **Model Context Protocol (MCP) plugins** to give Claude 
the authority to take actions like sending emails or interacting with local 
applications [14, 15]. (**Darrel Wilson**)
7.  **Leverage Parallel Processing:** Design workflows to run research tasks in 
parallel—such as researching 30 companies simultaneously—to move significantly 
faster than sequential, chat-based interactions [16, 17]. (**Greg Isenberg**)
8.  **Implement Recursive Customization:** Regularly use the "Customize" feature
to ask the AI how it can improve its own skills or marketing plugins based on 
your evolving business context [18, 19]. (**Eliot Prince**)
9.  **Automate Competitive Intelligence:** Configure "persistent agents" to 
monitor specific competitors daily at a set time (e.g., 8:00 AM) and only send a
notification if a significant change in pricing or features is detected [20-22].
(**Greg Isenberg**)
10. **Build with Artifacts:** Treat **Artifacts** as micro-web applications; 
once built and tested, use the "publish" feature to generate a live link you can
share with clients or embed directly into other websites [23, 24]. (**Darrel 
Wilson**)

Conversation: 86643620-0fca-482a-8a95-c9aaedca248a (turn 1)

---

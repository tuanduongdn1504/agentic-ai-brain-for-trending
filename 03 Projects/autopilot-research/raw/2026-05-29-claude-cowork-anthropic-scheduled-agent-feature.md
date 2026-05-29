# Claude Cowork — Anthropic scheduled-agent feature <!-- compiled: 2026-05-29 -->

**Notebook:** f851b538-c0cb-405f-9a8b-c46837464930
**Sources:** 6 YouTube videos
**Generated:** 2026-05-29 (overnight orchestrator)
**Query:** `Claude Cowork scheduled agent Anthropic cron automation`

## Sources

1. [20260525] **Duy Luân Dễ Thương** — Cách hẹn giờ để AI tự chạy task cho bạn (Claude Cowork)
   - https://www.youtube.com/watch?v=zxdI5bWcnGs
   - 9,220 views, 4:54 duration
2. [20260316] **Bart Slodyczka** — Claude Cowork Full Tutorial: How to Use Claude Cowork Better Than 99% of People
   - https://www.youtube.com/watch?v=vMo-yRCN3QM
   - 289,837 views, 14:23 duration
3. [20260305] **Stefan Wirth - AI without the BS** — Your First Scheduled Task in Claude Cowork (Live Build)
   - https://www.youtube.com/watch?v=1FCc3E5Od2U
   - 2,631 views, 9:21 duration
4. [20260228] **Kenny Liao** — Claude Code & Cowork Now Run 24/7 — Scheduled Tasks
   - https://www.youtube.com/watch?v=I1NdVZ6l5CQ
   - 8,104 views, 18:27 duration
5. [20260310] **Jack Roberts** — Claude Cowork FULL COURSE (Automate Everything)
   - https://www.youtube.com/watch?v=cNf7uVff11Y
   - 117,492 views, 65:18 duration
6. [20260331] **Tech With Tim** — Claude Cowork - Full Course for Beginners
   - https://www.youtube.com/watch?v=tf_KmDNZXzI
   - 130,344 views, 24:16 duration

---

## 1. Summary

The guides explain that users must have a **paid subscription** and keep their 
machines active for the software to execute tasks or **scheduled workflows**. 
Practical tutorials demonstrate how to connect **External Model Context Protocol
(MCP) servers** and third-party apps like Google Calendar, Slack, and Notion to 
create "skills" that automate repetitive business processes. Furthermore, the 
texts distinguish Co-work from **Claude Code**, noting that Co-work offers a 
more user-friendly, non-technical interface for individuals who prefer natural 
language over command-line tools. Ultimately, the materials illustrate how to 
leverage **sub-agents and parallel processing** to transform Claude into a 
proactive "AI employee" capable of managing digital environments independently.

---

## 2. Trends

Answer:
Analysis of the provided sources reveals several dominant trends in how experts 
utilize Claude Cowork, particularly regarding the transition from manual 
prompting to autonomous, scheduled workflows. 

The shared patterns across these videos focus on four primary areas: 
**contextual engineering**, **security through sandboxing**, **the 
"Skill-to-Plugin" pipeline**, and **hardware-dependent automation**.

### 1. Tactical Practice: Contextual Engineering
A recurring technique is the use of persistent Markdown (`.md`) files to give 
Claude a "brain" or memory that survives across different sessions.
*   **Jack Roberts** advocates for a "business brain.md" file that contains core
information about a user’s business, goals, and target audience to ensure 
Claude's responses remain aligned with the user's mission [1-3].
*   **Bart Slodyczka** suggests a more granular structure, creating three 
distinct files: `about me.md`, `brand voice.md`, and `working preferences.md` to
define personal priorities, communication styles, and procedural standards [4, 
5].
*   **Kenny Liao** uses a nightly "brain dump" technique, where a scheduled task
parses a general notes file and organizes the information into specific context 
files like `identity`, `preferences`, and `relationships` to keep his personal 
assistant updated [6, 7].
*   **Stefan Wirth** emphasizes "injecting context" by giving Claude access to 
local folders containing strategy and roadmap documents, allowing it to evaluate
transcripts or tasks against specific project visions [8-10].

### 2. Security and Workspace Structure
Multiple speakers stress the importance of limiting Claude's access to the 
computer's file system through "sandboxing."
*   **Jack Roberts** and **Bart Slodyczka** both recommend creating a dedicated 
"Sandbox" or "Claude Workspace" folder. This ensures Claude only has read/write 
access to a specific environment, protecting sensitive system files [11-13].
*   **Bart Slodyczka** further details a standardized internal folder structure:
`context`, `projects`, and `output` [4].
*   **Tech With Tim** highlights the permission system, noting that Claude 
cannot touch anything outside the folders the user explicitly allows, and warns 
users to keep duplicates of important files because Claude’s actions cannot be 
easily reversed [13-15].

### 3. Tooling Choices: MCPs and Connectors
The speakers consistently use **Model Context Protocol (MCP)** servers and 
**Connectors** to bridge the gap between the desktop and external web services.
*   **Recurring Connectors:** Google Calendar, Gmail, and Notion are the most 
cited tools for automating "Morning Briefs" [16-20].
*   **Specialized Tooling:**
    *   **Kenny Liao** uses the **Playwright MCP** to allow Claude to control a 
browser for tasks like posting to Substack [21].
    *   **Jack Roberts** utilizes **Fireflies** for meeting transcripts and 
**Mercury** for banking/financial reporting [22-24].
    *   **Stefan Wirth** employs **Linear** for project management and a custom 
**"Context OS" MCP** to apply different "lenses" (like a Stoic or Lean Startup 
viewpoint) to his work [25, 26].
    *   **Duy Luân Dễ Thương** demonstrates using Claude to scroll and scrape 
data directly from web browsers to populate Excel sheets [27, 28].

### 4. Recurring Technique: The "Skill-to-Plugin" Pipeline
A shared tactical practice is to first perform a task manually and then ask 
Claude to "codify" that success into a repeatable automation.
*   **Bart Slodyczka** recommends completing a pressing piece of work (like 
organizing invoices) and then telling Claude to "turn this process into a 
reusable skill" [29, 30].
*   **Jack Roberts** defines a "handover test" to determine if a task should 
become a plugin: if someone else could run the process without asking questions,
it is ready to be a documented plugin [31].
*   **Tech With Tim** notes that skills are essentially Markdown files that 
provide a step-by-step process for Claude to follow, ensuring consistency in 
repeatable workflows like searching for flights [32-34].

### 5. Efficiency and Cost Management
Speakers offer specific tactical advice on managing "token" usage and computer 
resources:
*   **Model Selection:** **Tech With Tim**, **Kenny Liao**, and **Stefan Wirth**
all advocate using **Claude 3.5 Sonnet** for most automated tasks to save 
credits, reserving the more expensive **Opus** only for highly complex reasoning
[8, 35-37].
*   **Token Saving:** **Bart Slodyczka** suggests using Claude to write a script
that handles data processing (like parsing 100 invoices) rather than having 
Claude analyze every file individually, which drastically reduces token 
consumption [38].
*   **Session Management:** **Jack Roberts** suggests clearing tasks or opening 
new windows every 30–45 minutes to prevent "context rot" and keep usage costs 
low [11, 39].

### 6. Hardware Constraints of "Scheduled Tasks"
A critical shared warning across all videos is the **active-state requirement** 
for the standard Claude Cowork scheduling feature.
*   **Kenny Liao, Tech With Tim, Bart Slodyczka,** and **Stefan Wirth** all 
state that for a scheduled task to run, the computer must be **on** and the 
Claude desktop app must be **open** [40-43].
*   **Kenny Liao** offers a tactical alternative for power users: he built a 
custom plugin that uses native system **cron tools**, allowing scheduled tasks 
to run in the background via Claude Code without needing the desktop app 
interface to be open [44, 45]

Resumed conversation: 2ca2badb-fc85-44c2-a584-fbbdea311a72

---

## 3. Outliers

The speakers in the sources diverge primarily on the **technical requirements 
for automation**, the **definition of user roles**, and the **strategies for 
cost-efficiency**. While they agree on the general value of Claude Cowork, their
approaches to implementation reveal significant contrarian takes.

### 1. The "Open App" Requirement Contradiction
The most direct technical disagreement concerns whether the Claude desktop app 
must be active for scheduled tasks to execute.
*   **The Majority View:** **Tech With Tim, Bart Slodyczka,** and **Stefan 
Wirth** all state that for a scheduled task to succeed, your computer must be on
and the Claude desktop app must be **open** [1-3]. **Jack Roberts** adds that if
the computer is closed at 8:00 a.m., the task will simply wait until you open 
the machine at 10:00 a.m. to run [4].
*   **The Contrarian Take:** **Kenny Liao** identifies this "app-must-be-open" 
requirement as a major "drawback" [5]. He explicitly diverges by offering a 
custom-built plugin that uses native system **cron tools** to run tasks in the 
background via **Claude Code**, removing the dependency on the Cowork desktop 
interface entirely [6, 7].

### 2. Strategic Divergence: Token Conservation vs. Task Autonomy
Speakers disagree on how much "thinking" Claude should do during a task, which 
impacts cost.
*   **The "Scripting" Strategy (Bart Slodyczka):** Bart argues that letting 
Claude analyze 100 invoices individually is a waste of tokens and session limits
[8]. His outlier opinion is that you should use Claude to **write a script** 
that parses the data, then embed that script in a skill. This way, the 
automation runs "locally" via the script without consuming tokens for every file
[8, 9].
*   **The "Sub-Agent" Strategy (Tech With Tim):** In contrast, Tim advocates for
**parallel sub-agents** to maximize speed [10]. While he acknowledges this uses 
more credits, he views the ability to run 20–30 searches simultaneously as the 
primary "unlock" for efficiency [10, 11].

### 3. Contrasting Definitions of Cowork vs. Code
The speakers offer different taxonomies for how Claude's various modes (Chat, 
Code, Cowork) relate to one another.
*   **Tech With Tim** frames the difference based on **user skill level**, 
stating that Cowork is for "beginners" who aren't familiar with the command 
line, while Code is for "power users" [12, 13].
*   **Bart Slodyczka** defines them by **professional function**: Chat is an 
"assistant," Code is a "developer," and Cowork is an "employee" that completes 
multi-step tasks [14].
*   **Jack Roberts** offers a more technical nuance, noting that Cowork was 
originally Claude Code but was rebranded as a "user-friendly, non-technical 
interface" that strips away the complexity of slash commands [15].

### 4. Outlier Tools and Techniques
Several speakers utilize unique features or external tools that others do not 
mention:
*   **Context Lenses:** **Stefan Wirth** is the only speaker to discuss using 
**"Lenses"** (via his custom Context OS MCP), which forces Claude to evaluate 
tasks through specific viewpoints like the "Stoic lens" or the "Lean Startup 
lens" [16].
*   **Visual Artifacts:** **Jack Roberts** is the only one who emphasizes 
**"Artifacts"** to create interactive, shareable web apps and dashboards from 
data, rather than just outputting to Excel or Notion [17, 18].
*   **External Scheduling:** While most focus on the local computer, **Jack 
Roberts** suggests an outlier alternative: scheduling tasks on **Railway**, 
which allows automations to run regardless of whether your laptop is open [4].
*   **Headcount Mindset:** **Jack Roberts** also provides a unique philosophical
take on pricing. While others focus on saving credits, Jack views the 
**$200/month Max plan** not as a software cost but as a **"salary headcount"** 
for an AI employee [19, 20].

### 5. Divergence in Context Management
The speakers differ on the "best practice" for organizing Claude's memory:
*   **The Minimalist:** **Jack Roberts** suggests a single **"business 
brain.md"** file to act as the primary repository of context [21].
*   **The Specialist:** **Bart Slodyczka** insists on a three-file structure 
(**about me, brand voice, working preferences**) to prevent Claude from becoming
"forgetful" [22, 23].
*   **The Automated Context:** **Kenny Liao** diverges by not manually writing 
these files at all; he uses a nightly **"brain dump"** scheduled task that 
automatically parses his notes and updates his context files for him [24, 25].

Conversation: 2ca2badb-fc85-44c2-a584-fbbdea311a72 (turn 1)

---

## 4. Gaps

While the provided sources offer a robust blueprint for setting up Claude Cowork
and automating individual workflows, they primarily focus on **local desktop 
usage** and individual productivity. A professional implementing these systems 
in a production or enterprise environment will encounter several gaps not fully 
addressed in the videos.

### Gaps for Production Implementation

*   **Resilience and Robust Error Handling:** The sources demonstrate successful
"happy path" automations, such as scraping data or organizing files [1-3]. 
However, they do not detail how to handle **API rate limits** (e.g., from Google
or Notion connectors) or what happens if a multi-step plugin fails halfway 
through a task [4, 5].
*   **Enterprise-Grade Security and Compliance:** While Jack Roberts and Bart 
Slodyczka advocate for a "Sandbox" folder to protect local files [6, 7], there 
is no mention of **PII (Personally Identifiable Information) masking**, GDPR 
compliance, or how to ensure sensitive business data isn't used for model 
training. 
*   **Centralized Version Control:** The videos describe creating skills and 
plugins as local `.md` or `.json` files [5, 8]. In a production environment, you
would need a way to **sync, version, and roll back** these "AI Employee" 
instructions across a team using a repository like Git, rather than manually 
copying files [9].
*   **Infrastructure Dependency:** Most speakers acknowledge that the desktop 
app must be open and the computer must be on for tasks to run [10-12]. While 
Kenny Liao offers a "cron" hack for local background tasks [13], a production 
environment requires investigating **cloud-based persistence** (e.g., running 
these agents on a server or Docker container) so they aren't dependent on a 
physical laptop [14].
*   **Advanced Monitoring and Telemetry:** Kenny Liao shows basic logs [15], but
production systems require **detailed telemetry**—tracking the success/failure 
rate of scheduled tasks, exact token costs per automation run, and latency of 
sub-agents over time [16, 17].

### Recommended Follow-Up Topics for Investigation

1.  **Server-Side Deployment (Railway/Docker):** Investigate moving workflows 
from the Claude Desktop app to persistent cloud environments. Jack Roberts 
briefly mentions **Railway** as an alternative to ensure tasks run even when a 
laptop is closed [14].
2.  **MCP Server Stability and Rate Management:** Research how to handle **"429 
Too Many Requests"** errors when running high-volume parallel sub-agents against
third-party APIs like Gmail, Stripe, or Linear [4, 16, 18].
3.  **Data Privacy Guardrails:** Look into tools or prompt engineering 
techniques for **PII redaction** to ensure customer data is stripped before 
being processed by Claude, which is critical for legal and compliance standards.
4.  **Automated Testing for AI Agents:** Explore creating "evals" or test suites
to verify that a skill (like a web scraper) still works after a target website 
updates its UI, preventing production "breakage" [19, 20].
5.  **Token Budgeting and Cost Controls:** Conduct a deep dive into the 
cost-efficiency of **Sonnet vs. Opus** for high-frequency scheduled tasks [17, 
21]. Investigate if writing local scripts to handle data (as Slodyczka suggests)
is more scalable than "agentic" analysis for thousands of files [17].
6.  **Collaborative Plugin Libraries:** Investigate frameworks for sharing and 
managing a **standardized library of plugins** across a large organization to 
ensure all "AI Employees" are following the same corporate SOPs and brand voice 
[22, 23].
7.  **System-Level Integration (Claude Code CLI):** For technical production, 
investigate using **Claude Code** via the command line for deeper integration 
with CI/CD pipelines, as it offers more programmatic control than the Cowork UI 
[24-26].

Conversation: 2ca2badb-fc85-44c2-a584-fbbdea311a72 (turn 1)

---

## 5. Takeaways

Analysis of the provided sources suggests these 9 actionable rules and 
configurations for developers implementing Claude Cowork:

1.  **Enforce Strict Sandboxing:** Create a dedicated "Claude Workspace" or 
sandbox folder and grant Claude access only to that directory to prevent 
irreversible file modifications or accidental deletion of critical system data 
[1-3].
2.  **Maintain Persistent Context Files:** Store your "Business Brain" or core 
preferences in persistent Markdown files (`.md`) and set a **Global 
Instruction** for Claude to read these files first to ensure consistent tone and
strategy [4-7].
3.  **Optimize for Script-Based Processing:** Save tokens by asking Claude to 
**write a local script** to parse massive datasets (like hundreds of invoices) 
instead of having the LLM analyze each file individually [8].
4.  **Circumvent App-Open Requirements:** Use a custom plugin that leverages 
native system **cron tools** to run scheduled tasks in the background, bypassing
the standard requirement that the Claude desktop app must remain open [9-11].
5.  **Prevent Context Rot:** Clear your task history or open a new window every 
30–45 minutes during focused sessions to stop old, irrelevant conversation data 
from inflating your token costs [12, 13].
6.  **Leverage Parallel Sub-Agents:** For time-sensitive data gathering, 
explicitly instruct Claude to "run in parallel" to dispatch multiple sub-agents 
simultaneously, maximizing speed for complex workflows [14-16].
7.  **Apply the "Handover Test":** Codify a workflow into a **Plugin** only if 
it passes the "handover test"—meaning the process involves multiple steps and 
tools, and a stranger could execute it without needing to ask you questions [17,
18].
8.  **Inject Strategic Context:** Improve automated evaluations by giving Claude
access to local project folders containing roadmaps and vision documents, 
allowing it to measure transcripts or tasks against your specific business goals
[19-21].
9.  **Utilize Remote Dispatch:** Enable the **"Dispatch" feature** in your 
settings to trigger complex tasks on your computer directly from your mobile 
phone while you are away from your desk [22-24].

Conversation: 2ca2badb-fc85-44c2-a584-fbbdea311a72 (turn 1)

---

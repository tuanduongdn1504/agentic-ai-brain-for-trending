# MCP servers for messaging platforms — Telegram, WhatsApp, Discord

**Notebook:** 183e3635-ea8c-4c52-9c16-11aa32e19c78
**Sources:** 6 YouTube videos
**Generated:** 2026-05-07 (overnight orchestrator)
**Query:** `Telegram MCP server bot Claude integration tutorial setup`

## Sources

1. [20260325] **Kumo Explains** — How to Connect Claude Code to Telegram (Claude Code Channels)
   - https://www.youtube.com/watch?v=DUztF4mVt8o
   - 3,910 views, 7:40 duration
2. [20260201] **Samir Kharel** — Connect an MCP server to CLAUDE DESKTOP in 7 Minutes
   - https://www.youtube.com/watch?v=o8-tTD6eU_I
   - 15,215 views, 6:39 duration
3. [20260402] **Lewis Jackson** — How To Connect Claude to Trading View (Insanely Cool)
   - https://www.youtube.com/watch?v=vIX6ztULs4U
   - 781,595 views, 20:13 duration
4. [20260320] **Chris Verzwyvelt** — Claude Channels: Full Setup Guide (AI Agents via Telegram)
   - https://www.youtube.com/watch?v=2z1Y7Wd0n0g
   - 4,615 views, 6:22 duration
5. [20260408] **Michele Torti** — Master Claude Code MCP in 13 minutes (Beginner’s Guide)
   - https://www.youtube.com/watch?v=3wArVlPvqAk
   - 13,231 views, 13:41 duration
6. [20260321] **Mervin Praison** — Claude Code on Telegram: The Game Changer
   - https://www.youtube.com/watch?v=GjDRlqmfoT8
   - 12,884 views, 5:26 duration

---

## 1. Summary

Summary:
These sources provide comprehensive guides for extending **Claude Code** into a 
versatile AI agent capable of remote operation and third-party integration. 
Several tutorials focus on **Telegram** and **Discord** connectivity, allowing 
users to control their terminal and manage coding tasks through mobile messaging
apps. Other instructions detail the use of the **Model Context Protocol (MCP)** 
to grant Claude new abilities, such as browsing live websites, interacting with 
databases like **Supabase**, or automating **Trading View** charts. By 
installing specific plugins and configuring server tokens, users can perform 
complex research, execute code, and receive "morning briefs" on financial assets
from anywhere. Ultimately, the material highlights how these integrations 
transform a standard command-line tool into a powerful, autonomous assistant for
development and productivity.

---

## 2. Trends

Answer:
The dominant trends across these videos center on **transforming Claude from a 
passive chatbot into an active agent** capable of remote operation, real-time 
data analysis, and cross-platform automation.

The following shared patterns and tactical practices emerge from the source 
material:

### 1. Messaging Platforms as the Remote Interface
A primary trend is the use of **Telegram** as a remote control for Claude's 
terminal-based capabilities. 
*   **Chris Verzwyvelt** advocates for using Telegram because it allows users to
**remote control their terminal** while away from their desks [1, 2]. 
*   **Mervin Praison** echoes this, noting that messaging integration adopts a 
strategy similar to "Open Claude," allowing work to continue without being 
tethered to a computer [3]. 
*   **Kumo Explains** emphasizes the convenience of talking to Claude Code on a 
phone "anywhere and anytime" [4].

### 2. The Dominance of MCP (Model Context Protocol)
Speakers treat MCP as the universal "plugin" architecture that grants Claude 
"new abilities."
*   **Michele Torti** defines MCP as a "new pair of hands" for Claude, 
distinguishing it from **Skills** (instructions) and **Hooks** (guardrails) [5].
He highlights its power in allowing Claude to control browsers (Chrome 
DevTools), talk to databases (Supabase), and read API documentation [5-7].
*   **Lewis Jackson** focuses on **Trading View MCP**, emphasizing that it 
allows Claude to interact with charts on a **"code-to-code basis"** rather than 
relying on outdated image recognition [8, 9].
*   **Samir Kharel** demonstrates the tactical side of MCP by building a custom 
Python server using `fastmcp` to bridge Claude Desktop with Discord [10].

### 3. Recurring Tooling Choices
The videos showcase a consistent stack of tools and commands for setting up 
these agentic systems:
*   **BotFather (Telegram):** Chris Verzwyvelt, Mervin Praison, and Kumo 
Explains all utilize Telegram's "BotFather" to generate the unique API tokens 
required for bot creation [11-13].
*   **Claude Code Terminal:** Most speakers prioritize the **terminal-based 
"Claude Code"** over the desktop app for its agentic flexibility [1, 3, 14].
*   **Configuration Files:** Recurring technical tasks include editing 
`mcp.json` (for Claude Code) or the `claude_desktop_config.json` (for Claude 
Desktop) to define server paths and arguments [15, 16].
*   **Standard I/O (`stddio`):** Samir Kharel points out that Claude uses 
standard input and output to communicate with MCP servers [17].

### 4. Tactical Security Practices
Multiple speakers advocate for "locking down" the agent once it is connected to 
a public messaging platform.
*   **Mervin Praison** and **Kumo Explains** both highlight the importance of 
the **`allowlist` command** to prevent strangers from gaining access to the bot 
or receiving pairing code replies [18, 19].
*   **Chris Verzwyvelt** advises switching to an allow list immediately after 
pairing to "lock this baby down" [2, 20].

### 5. Automation and Optimization Techniques
Speakers provide specific techniques to streamline the user experience and 
manage costs:
*   **One-Shot Setup:** **Lewis Jackson** provides a "one-shot setup prompt" to 
automate the complex process of configuring GitHub-based MCP tools, bypassing 
manual headache [21].
*   **The "Morning Brief":** Jackson also advocates for creating automated 
routines, such as a **"morning_brief"** command, where Claude analyzes a whole 
watchlist at once rather than the user asking for individual reports [22].
*   **Token Efficiency:** **Michele Torti** warns that MCP tools are 
**token-heavy**, noting that just two MCPs can consume over 10,000 context 
tokens [23]. He suggests a tactical workflow: test an MCP to ensure it works, 
then **convert it into a "Skill"** (instruction-based) to save on costs and 
preserve context window space for the conversation [24].

### 6. Hardware and Uptime Considerations
*   **Chris Verzwyvelt** mentions a tactical preference for running these agents
on a **Mac Mini or a desktop** that stays on all the time, rather than a laptop,
to ensure the agent is always reachable via Telegram [1].

Resumed conversation: a5ac4407-4e47-4d68-ad96-da4eb62981b0

---

## 3. Outliers

While the speakers generally agree on the power of the Model Context Protocol 
(MCP), they diverge significantly on **setup methodology**, the **efficacy of 
multimodal analysis**, and the **sustainability of using MCPs** long-term.

### 1. Manual Setup vs. "One-Shot" Automation
The most prominent divergence is between **Lewis Jackson** and the other 
speakers regarding the complexity of installation.
*   **The "Headache" Critique:** Lewis Jackson identifies the standard manual 
installation process found on GitHub—which involves extensive copy-pasting—as a 
"headache" [1]. 
*   **The Alternative:** Unlike **Chris Verzwyvelt** [2], **Mervin Praison** 
[3], and **Kumo Explains** [4], who all advocate for step-by-step manual 
terminal commands, Jackson provides a **"one-shot setup prompt"** to automate 
the creation of `mcp.json` and other configurations [1, 5].
*   **File Editing:** While **Michele Torti** [6] and **Samir Kharel** [7] show 
users how to manually edit JSON files to add servers, **Jackson** explicitly 
states he dislikes doing that, preferring to simply "talk" to Claude to have it 
edit the file structure for him [8, 9].

### 2. Contrarian Take on Image Recognition (Multimodal)
**Lewis Jackson** offers a strong contrarian view on how AI should interact with
visual data, specifically financial charts.
*   **Screenshot Criticism:** He argues that traditional AI chart tools that 
rely on screenshots are "irrelevant" because candles move by the time the image 
is uploaded [10, 11]. He dismisses image recognition as "guessing" based on 
pixels [11].
*   **Code-to-Code Advantage:** He asserts that Claude should instead interact 
with charts on a **"code-to-code basis"** by reading the live Inspect/CDP data 
from the browser, which he claims is a "very different thing" than standard 
image recognition [1, 12, 13].

### 3. Outlier Opinion on Token Costs and Efficiency
While most speakers focus on the "magic" of adding new abilities, **Michele 
Torti** is an outlier in highlighting the **significant financial and technical 
downsides** of MCPs.
*   **The "Token Heavy" Warning:** Torti warns that MCPs are extremely 
resource-intensive; he notes that just two MCP servers can consume over **10,000
context tokens** [14].
*   **Contrarian Workflow:** Because of this cost, he advocates for a tactical 
workflow that contradicts the "always-on" MCP approach: he suggests testing an 
MCP to see if it works and then **converting it into a "Skill" 
(instruction-based)** to save space in the context window and reduce costs [14, 
15]. No other speaker mentions the context window limitations or the high token 
price of these tools.

### 4. Divergence on "Open Claw"
Speakers differ in their assessment of the third-party tool "Open Claw" in 
relation to the new official Claude Channels.
*   **The "Killer" Take:** **Chris Verzwyvelt** takes a hard stance, calling the
new Telegram integration an **"open claw killer"** and stating he has "a lot of 
issues" and bugs with the original Open Claw [16].
*   **The Complementary Take:** Conversely, **Mervin Praison** views the new 
features as "adapting the same strategy" as Open Claw and even recommends that 
his viewers watch his previous video on how to set up Open Claw, suggesting it 
remains a relevant alternative [17, 18].

### 5. Hardware Deployment Philosophy
There is a minor but specific divergence on where these agents should actually 
run.
*   **The Always-On Desktop:** **Chris Verzwyvelt** argues that while a laptop 
works, it is **"better if you had something like a Mac Mini"** or a desktop that
stays on 24/7 to ensure the Telegram remote control is always reachable [19].
*   **Mobile Flexibility:** **Kumo Explains** and **Mervin Praison** focus more 
on the ability to use Claude **"anywhere and anytime"** via a phone, without 
specifically emphasizing the need for dedicated "always-on" hardware [17, 20].

Conversation: a5ac4407-4e47-4d68-ad96-da4eb62981b0 (turn 1)

---

## 4. Gaps

While the sources provide a detailed blueprint for setting up personal Claude 
agents via Telegram and MCP, they primarily focus on **single-user, 
local-environment setups**. Moving these concepts into a production 
environment—where reliability, security, and scalability are critical—introduces
several gaps that the videos do not address.

### Gaps for Production Implementation

*   **High Availability and Failover:** Several speakers suggest running the 
agent on a **Mac Mini or desktop** that stays on all the time [1, 2]. In a 
production setting, relying on a single physical machine at a home or office is 
a "single point of failure." The sources do not cover how to migrate these 
"Claude Code Channels" or MCP servers to **cloud-based, containerized 
environments** (like Docker on AWS or Google Cloud) to ensure 99.9% uptime.
*   **Secrets Management:** Current tactical advice involves **pasting API 
tokens directly into the terminal** or saving them in plain-text `mcp.json` or 
`claude_desktop_config.json` files [3-6]. In production, this is a major 
security risk. There is no mention of using **environment variables** or **vault
services** (like AWS Secrets Manager) to handle sensitive credentials.
*   **Observability and Logging:** The videos show real-time terminal output 
[7-9], but they do not discuss how to implement **centralized logging or error 
monitoring**. If an agent fails while you are away from your desk, there is no 
production-grade mechanism described to alert you or provide a post-mortem of 
why the MCP server crashed.
*   **Multi-Tenancy and Access Control:** The sources focus on a 1:1 
relationship between a user and their bot, using a simple **"allowlist"** for 
security [7, 10, 11]. Production systems usually require **Role-Based Access 
Control (RBAC)** to manage different permission levels for various team members 
or customers.
*   **Cost Governance at Scale:** While Michele Torti warns that MCPs are "token
heavy" (using 10,000+ tokens for just two servers), he does not provide a 
framework for **budgeting or rate-limiting** these costs in a multi-user 
production environment [12, 13].

### 5-7 Follow-Up Topics for Investigation

Based on the gaps identified, here are specific topics to research for a 
production-ready implementation:

1.  **Headless Cloud Deployment:** Investigate how to run Claude Code and MCP 
servers in a **headless Linux environment** (e.g., an EC2 instance or a 
DigitalOcean Droplet) rather than on local hardware like a Mac Mini [1].
2.  **Environment Variable Integration:** Research how to modify MCP server code
(like the Python example provided by Samir Kharel) to pull tokens from **system 
environment variables** instead of hardcoded strings or JSON files [5, 14].
3.  **MCP Observability Tools:** Explore tools like **LangSmith, Arize Phoenix, 
or Datadog** to track the performance, latency, and success rates of your 
agentic tool calls in real-time. (Note: These specific tools are not mentioned 
in the sources).
4.  **Rate Limiting and Circuit Breakers:** Investigate implementing "circuit 
breakers" for your MCP servers. This ensures that if Claude gets stuck in an 
expensive loop (like the "morning brief" cycling through too many assets), the 
system will **automatically kill the process** before exhausting your API budget
[13, 15, 16].
5.  **Agent Evaluation (Eval) Frameworks:** Since Lewis Jackson points out that 
AI can sometimes "guess" or have "issues with the code," you should investigate 
**automated testing frameworks** to verify that your agent's outputs remain 
accurate as you update your `rules.json` or MCP capabilities [17, 18].
6.  **Encrypted Message Tunnels:** While the sources use standard 
Telegram/Discord webhooks [14, 19], research **end-to-end encrypted tunnels** 
(like Tailscale or Ngrok with OAuth) to ensure that the communication between 
your remote device and your production terminal remains private and 
tamper-proof. (Note: Encryption methods are not detailed in the sources).

Conversation: a5ac4407-4e47-4d68-ad96-da4eb62981b0 (turn 1)

---

## 5. Takeaways

Deploy on "Always-On" Hardware:** To ensure your Telegram remote agent is 
consistently reachable, run Claude Code on a **Mac Mini or a desktop computer** 
rather than a laptop that might sleep or disconnect [1]. (Chris Verzwyvelt)

2. **Restrict Access with Allowlists:** Immediately after pairing your Telegram 
bot, execute the **`allowlist` command** to "lock it down" and prevent 
unauthorized users from receiving pairing codes or interacting with your 
terminal [2, 3]. (Chris Verzwyvelt & Mervin Praison)

3. **Use One-Shot Setup Prompts:** Avoid the "headache" of manual configuration 
by providing Claude with a **"one-shot setup prompt"** that allows the agent to 
automate the creation of `mcp.json` and other necessary file structures [4, 5]. 
(Lewis Jackson)

4. **Limit Active MCP Servers:** Maintain a lean environment by using only **two
or three core MCP servers** at a time, as adding more can significantly drain 
your token budget—two servers alone can consume over 10,000 tokens [6, 7]. 
(Michele Torti)

5. **Convert Proven MCPs to Skills:** Once you have verified that an MCP works 
correctly, **convert that functionality into a "Skill"** (instruction-based 
prompt) to preserve your context window space and reduce ongoing token costs 
[7]. (Michele Torti)

6. **Prioritize Code over Screenshots:** When integrating with live data 
platforms like Trading View, use the **Chrome DevTools Protocol (CDP)** to let 
Claude read live code-level values, which is far more accurate than "guessing" 
based on pixelated screenshots [8, 9]. (Lewis Jackson)

7. **Standardize Transport with `stddio`:** When developing custom Python-based 
MCP servers, ensure the transport is set to **`stddio` (standard 
input/output)**, as this is the communication protocol required by Claude [10, 
11]. (Samir Kharel)

8. **Implement Batch Commands:** Optimize your workflow by creating aggregate 
commands like **`morning_brief`**, which instructs Claude to analyze an entire 
watchlist of assets simultaneously rather than requiring individual queries for 
each item [12, 13]. (Lewis Jackson)

9. **Manage Strategies via `rules.json`:** Instead of manually editing 
configuration files, **interact with Claude naturally** to update the 
`rules.json` file with new trading strategies, watchlists, or operational 
guidelines [14, 15]. (Lewis Jackson)

10. **Vet Plugins via Community Trust:** When selecting third-party plugins from
directories like `mcpservers.org`, prioritize tools with **higher GitHub stars**
to ensure they are vetted and reliable before integrating them into your 
workspace [16]. (Michele Torti)

Conversation: a5ac4407-4e47-4d68-ad96-da4eb62981b0 (turn 1)

---

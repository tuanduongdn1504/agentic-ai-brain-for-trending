# Telegram bot — remote control Claude Code/Desktop from phone

**Notebook:** 5f514e9c-d8e4-42be-af1e-c456dfa1e4c7
**Sources:** 6 YouTube videos
**Generated:** 2026-05-07 (overnight orchestrator)
**Query:** `Telegram bot Claude Code remote control MCP agent`

## Sources

1. [20260325] **Kumo Explains** — How to Connect Claude Code to Telegram (Claude Code Channels)
   - https://www.youtube.com/watch?v=DUztF4mVt8o
   - 3,910 views, 7:40 duration
2. [20260320] **Chris Verzwyvelt** — Claude Channels: Full Setup Guide (AI Agents via Telegram)
   - https://www.youtube.com/watch?v=2z1Y7Wd0n0g
   - 4,615 views, 6:22 duration
3. [20260331] **Kris Torrington** — Connect Claude Code to Discord in 5 Minutes (Fast Step-by-Step Guide)
   - https://www.youtube.com/watch?v=lDlSGmCXht4
   - 3,371 views, 5:58 duration
4. [20260322] **Developers Digest** — Claude Code Channels in 8 Minutes
   - https://www.youtube.com/watch?v=QZXaAc80OL0
   - 25,593 views, 8:40 duration
5. [20260226] **NetworkChuck** — Claude Code on your Phone is OFFICIAL (it changes  everything)
   - https://www.youtube.com/watch?v=ocQ7ZKhHU5Q
   - 289,819 views, 7:31 duration
6. [20260129] **NetworkChuck** — Claude Code on your phone in 10 minutes
   - https://www.youtube.com/watch?v=FEDiAHzS0zw
   - 251,328 views, 9:41 duration

---

## 1. Summary

The integration is achieved by setting up **custom bots** through
platforms like BotFather, installing official **MCP plugins**, and configuring 
secure **access allow lists** to restrict interactions. Beyond simple chat, 
these features enable **proactive monitoring**, where Claude can automatically 
react to system errors or CI/CD failures by suggesting or applying fixes. For 
users requiring constant availability, the guides also suggest running the 
software on a **VPS with tmux** to ensure a persistent, secure development 
environment accessible from anywhere. This evolution represents a shift toward 
**always-on AI agents** that bridge the gap between infrastructure and automated
software engineering.

---

## 2. Trends

Answer:
Analysis of the provided sources reveals several dominant trends and shared 
patterns regarding the remote operation and automation of Claude Code. The 
primary focus across all videos is achieving **remote terminal access** and 
transforming Claude from a local tool into an **always-on AI agent**.

### 1. The Shift to "Always-On" Infrastructure
A recurring tactical recommendation is to move Claude Code from a personal 
laptop to a persistent environment.
*   **Persistent Hardware:** **Chris Verzwyvelt** advocates using a "Mac Mini or
something that stays on all the time" or a desktop rather than a laptop, because
the goal is to control the terminal while away [1].
*   **Cloud VPS (Virtual Private Servers):** **NetworkChuck** takes this 
further, suggesting a "Forever Terminal" hosted on a VPS (specifically 
recommending Hostinger) [2]. This ensures Claude is accessible from "literally 
anywhere" [3].
*   **Warm Sessions vs. Cold Sessions:** **Developers Digest** highlights that 
these "always-on" setups allow for **warm sessions**, which maintain continuity 
and larger context windows compared to "cold" headless sessions that lose state 
after each run [4].

### 2. Tooling Choices: Telegram, Discord, and Native Apps
Speakers advocate for different "channels" to interface with the terminal 
remotely:
*   **Telegram & BotFather:** This is the most common pattern. **Chris 
Verzwyvelt**, **Developers Digest**, and **Kumo Explains** all demonstrate using
Telegram's **BotFather** to create a bot and obtain an API token for the Claude 
Code Telegram plugin [5-7].
*   **Discord Integration:** **Kris Torrington** provides a detailed guide on 
using Discord, emphasizing the need to enable **"Message Content Intent"** in 
the Discord Developer Portal so the bot can read incoming commands [8].
*   **Native Claude App (Remote Control):** **NetworkChuck** highlights a newer,
official Anthropic feature called **Remote Control**. By typing 
`/remote-control` in the terminal, users can resume their local session directly
inside the **native Claude mobile app** without needing a VPN [9, 10].
*   **Terminus and tmux:** For those using a VPS, **NetworkChuck** recommends 
the **Terminus** app for mobile terminal access [11] and **tmux** (a terminal 
multiplexer) to keep sessions alive even if the mobile connection drops [12, 
13].

### 3. Tactical Practices for Security (The "Allow List")
Every speaker who discusses Telegram or Discord integrations emphasizes security
to prevent unauthorized users from controlling the host machine.
*   **Lockdown via Allow List:** **Chris Verzwyvelt** and **Developers Digest** 
both stress "locking this baby down" immediately after pairing [14, 15]. This is
done using the command `/telegram:access-policy allow-list` [15].
*   **Granular Discord Permissions:** **Kris Torrington** details how to 
restrict access in Discord by copying specific **User IDs** and **Channel IDs** 
to the `access.json` configuration, ensuring only the owner can trigger the 
agent [16, 17].
*   **VPS Hardening:** When using a public-facing server, **NetworkChuck** 
advocates for tactical hardening, including installing **Fail2Ban**, configuring
the **UFW firewall**, and disabling password authentication in favor of **SSH 
key authentication** [18-20].

### 4. Advanced Automation and Reactive Workflows
A significant trend is moving beyond manual chat to **reactive AI agents**.
*   **Event-Driven Coding:** **Developers Digest** explains that "Channels" 
allow Claude to react to **external events** like CI/CD alerts, GitHub PR 
comments, or Sentry error logs [21, 22]. He suggests a workflow where a CI 
failure automatically triggers a Claude session to fix the bug and push a new PR
[23, 24].
*   **Auto-Approve Tools:** To make the experience truly autonomous, **Kris 
Torrington** recommends a tactical "quality of life" change: telling Claude to 
**update its config to auto-approve all tools** for the specific plugin. This 
eliminates the need for the user to manually approve every terminal command via 
their phone [16, 17].
*   **Monitoring Logs:** **Developers Digest** advocates for monitoring log 
files (like Docker or PM2) and piping errors directly into Claude for immediate 
solution proposals [25].

### 5. Shared Installation Patterns
Multiple speakers follow a nearly identical setup ritual for Claude Code 
plugins:
1.  **Install the plugin** from the official Anthropic repository [26].
2.  **Configure the token** (Telegram or Discord) [6, 27].
3.  **Relaunch with the `--channels` flag** to start the listener [28-30].
4.  **Pair the device** by sending a message to the bot to receive a unique 
pairing code [28, 29, 31].

Resumed conversation: 4a98873c-c477-402d-8fd1-43ed303ddd70

---

## 3. Outliers

While the speakers generally agree on the value of remote access for Claude 
Code, they diverge significantly on **infrastructure choices**, the **necessity 
of specific features**, and the **ideal level of automation**.

### 1. Hardware Strategy: Local vs. Cloud VPS
A major point of divergence is where the "always-on" environment should reside.
*   **Local Hardware:** **Chris Verzwyvelt** advocates for using a local **Mac 
Mini or desktop** that stays on all the time [1]. He views using a laptop as a 
security or peace-of-mind issue and prefers local machines for remote terminal 
control [1].
*   **Cloud VPS (Outlier):** **NetworkChuck** presents a contrarian view, 
arguing for a **"Forever Terminal"** hosted on a **Virtual Private Server 
(VPS)** [2]. He suggests that local machines are insufficient because they can 
go down; a VPS ensures Claude is accessible "wherever all the time" without 
relying on home internet or local power [2].

### 2. Native "Remote Control" vs. "Channels" (Telegram/Discord)
The speakers disagree on which tool is the primary "game-changer" for mobile 
access.
*   **Remote Control as the Winner:** **NetworkChuck** views the official 
`/remote-control` command as the superior solution because it is native, handles
the connection through Anthropic (no VPN needed), and allows the user to resume 
a session directly in the **native Claude mobile app** [3, 4]. He claims this 
"solves a problem I was trying to solve with a bunch of different solutions" 
[4].
*   **Channels as the "OpenClaw Killer":** **Chris Verzwyvelt** and **Developers
Digest** focus on **Channels (Telegram/Discord)** as the primary advancement [5,
6]. While NetworkChuck sees Remote Control as the OpenClaw replacement, 
Verzwyvelt explicitly calls the Telegram/Discord integration the **"OpenClaw 
killer"** [5].
*   **The Nuanced Take:** **Developers Digest** provides a technical distinction
that diverges from the "either/or" narrative. He argues that Remote Control is 
for **manual interaction** (reviewing and controlling a session), whereas 
Channels are for **automated reaction** (responding to CI/CD alerts or webhooks)
[7].

### 3. Tactical Disagreement: Manual Approval vs. Full Autonomy
There is a procedural contradiction regarding how much permission Claude should 
have.
*   **Full Automation:** **Kris Torrington** advocates for a contrarian tactical
move: telling Claude to **update its config to auto-approve all tools** from the
Discord plugin [8]. He describes manual confirmation popups as "annoying" and 
wants the bot to respond instantly without any terminal prompts [8, 9].
*   **Manual Supervision:** In contrast, **Kumo Explains** demonstrates a more 
cautious workflow, where the user must **manually click "Allow"** or "Yes" in 
the terminal to authorize the agent's actions during the pairing and initial 
messaging phase [10].

### 4. Platform and Tooling Preferences
*   **Telegram vs. Discord:** **Chris Verzwyvelt** mentions that while Discord 
is an option, he explicitly chooses Telegram because he simply "likes doing 
things in Telegram" [5]. **Kris Torrington**, conversely, focuses entirely on 
Discord, highlighting specific permissions like "Message Content Intent" that 
are unique to that platform's developer portal [11].
*   **Persistence Techniques:** While most speakers focus on the plugin 
architecture for session continuity, **NetworkChuck** introduces a unique 
requirement for VPS users: **tmux** [12]. He argues that without a terminal 
multiplexer like tmux, a session will "disappear" if the phone locks or signal 
is lost, a concern not addressed by the other speakers who rely on the "warm 
session" logic of the MCP plugin [12, 13].

### 5. Identification of Limitations
*   **NetworkChuck** offers a critique of the current native Remote Control 
feature, stating he is "not really a fanboy" and specifically requests a feature
currently missing: the ability to **start a new session** from the phone rather 
than just resuming an existing one started on a laptop [14, 15]. Other speakers,
focusing on Telegram/Discord, do not highlight this as a major friction point 
because those bots can be messaged at any time to trigger a session [10].

Conversation: 4a98873c-c477-402d-8fd1-43ed303ddd70 (turn 1)

---

## 4. Gaps

While the sources provide a comprehensive "getting started" guide for remote 
Claude Code access, they primarily focus on **personal or hobbyist setups**. A 
production-grade implementation requires addressing several technical and 
operational gaps that the speakers overlook or simplify for the sake of their 
tutorials.

### Gaps in Current Source Material
*   **Automated Process Management:** While **NetworkChuck** recommends `tmux` 
for persistence, this still requires manual intervention if the server reboots 
[1, 2]. Production environments require a process manager like **systemd** or 
**PM2** to ensure the Claude Code listener starts automatically on boot and 
restarts after a crash.
*   **Secure Secret Management:** The videos show users **manually pasting API 
tokens** into terminal commands or configuration prompts [3-5]. In production, 
secrets should never be entered manually or stored in plain-text config files; 
they should be injected via **environment variables** or a **secret vault** 
(e.g., AWS Secrets Manager).
*   **Enterprise Security & Auditing:** The "allow list" mentioned by **Chris 
Verzwyvelt** and **Kris Torrington** is a great first step, but it lacks **audit
logging** [6-8]. A production system needs to log every command the agent 
executes to an external system (like CloudWatch or Datadog) for compliance and 
forensic review.
*   **Infrastructure as Code (IaC):** The setup described is entirely manual. 
For production, the VPS configuration, firewall rules, and Claude installation 
should be codified using tools like **Terraform** or **Ansible** to ensure the 
environment is reproducible and version-controlled.
*   **Resource Constraints & Rate Limiting:** **Developers Digest** discusses 
"always-on" agents reacting to cascading failures, but does not address **API 
rate limits** or **token costs** [9, 10]. A production agent reacting to a log 
firehose could quickly exhaust an Anthropic API quota or run up significant 
costs if not properly rate-limited.

### 5-7 Specific Follow-Up Topics for Investigation

1.  **Systemd Service Configuration:** Investigate how to wrap the `claude 
--channels` command in a **systemd unit file**. This is the industry standard 
for Linux "always-on" services to ensure they are monitored and auto-restarted 
by the OS.
2.  **Environment Variable Injection for Plugins:** Research how to pass the 
`TELEGRAM_BOT_TOKEN` or `DISCORD_BOT_TOKEN` directly via **system environment 
variables** rather than using the interactive `/configure` commands, which is 
essential for automated deployments.
3.  **Advanced RBAC (Role-Based Access Control):** Beyond a simple "allow list" 
of User IDs [8, 11], investigate if Claude Code can be restricted to specific 
**subsets of commands** (e.g., "read-only" in production but "read-write" in 
staging) to implement the principle of least privilege.
4.  **Cost Monitoring and Circuit Breakers:** Look into setting up **usage 
alerts** or "circuit breakers" on the Anthropic dashboard. This prevents a 
"runaway agent" from making thousands of recursive calls during a complex 
debugging task.
5.  **Log Aggregation for AI Actions:** Explore ways to pipe the Claude Code 
terminal output (the `stdout`) into a centralized **logging aggregator**. This 
creates a permanent, searchable record of what the AI did, which is critical 
when it has the power to modify production code or infrastructure.
6.  **Network Segmentation & Egress Filtering:** Investigate placing the 
"Forever Terminal" [12] in a **private subnet** or a **DMZ**. Since the bot 
needs to talk to Telegram/Discord servers, you should configure the firewall to 
only allow egress traffic to those specific platforms, minimizing the risk if 
the server is compromised.
7.  **Automated Dependency Updates:** Research strategies for keeping the 
`claude-code` package and its plugins updated automatically (e.g., via a **Cron 
job** or **GitHub Action**). As an "always-on" agent, it must receive security 
patches for its underlying Node.js environment and MCP plugins.

Conversation: 4a98873c-c477-402d-8fd1-43ed303ddd70 (turn 1)

---

## 5. Takeaways

Adopt a persistent "Always-On" environment:** Move your Claude Code 
instance from a laptop to a **Mac Mini** or a **Cloud VPS** (Virtual Private 
Server) to ensure your terminal agent is reachable even when your personal 
computer is off [1], [2]. (**Chris Verzwyvelt** / **NetworkChuck**)

2. **Harden your remote server immediately:** If using a public VPS, secure it 
by installing **Fail2Ban**, enabling the **UFW firewall** (allowing only port 
22), and disabling password logins in favor of **SSH key authentication** [3], 
[4], [5]. (**NetworkChuck**)

3. **Enforce an "Allow List" security policy:** Once your Telegram or Discord 
bot is paired, immediately run the command `/telegram:access-policy allow-list` 
to prevent unauthorized users from executing terminal commands on your host [6],
[7], [8]. (**Chris Verzwyvelt** / **Developers Digest** / **Kris Torrington**)

4. **Enable "Message Content Intent" for Discord:** When configuring a Discord 
bot in the Developer Portal, you must toggle on this specific setting so the bot
has the technical permission to read your incoming messages [9]. (**Kris 
Torrington**)

5. **Utilize tmux for session persistence:** Use a terminal multiplexer like 
**tmux** on your remote server to keep Claude sessions alive and scrollable if 
your mobile connection drops or your phone locks [10], [11], [12]. 
(**NetworkChuck**)

6. **Bypass confirmation prompts with Auto-Approve:** To make the mobile 
experience truly autonomous, instruct Claude to update its `settings.json` to 
**auto-approve all tools** for your messaging plugin, eliminating the need for 
manual "Allow" clicks on every command [13]. (**Kris Torrington**)

7. **Implement reactive log monitoring:** Configure Claude to monitor live log 
files from **Docker** or **PM2** so it can automatically propose solutions the 
moment an error is detected in your production environment [14]. (**Developers 
Digest**)

8. **Leverage the native Remote Control feature:** Use the official 
`/remote-control` command to sync your active terminal session directly to the 
**native Claude mobile app**, allowing you to resume work without a VPN [15], 
[16]. (**NetworkChuck**)

9. **Prioritize "Warm" over "Cold" sessions:** Aim to keep an active, "warm" 
Claude session running on your server to maintain a **larger context window** 
and continuity, rather than triggering "cold" headless sessions for every 
command [17], [18]. (**Developers Digest**)

10. **Use the specific Channels flag for listeners:** Always restart Claude 
using the **`--channels` flag** (e.g., `claude --channels 
telegram-plugin-official`) to ensure the subprocess is actively listening for 
remote triggers [6], [8]. (**Chris Verzwyvelt** / **Kris Torrington**)

Conversation: 4a98873c-c477-402d-8fd1-43ed303ddd70 (turn 1)

---

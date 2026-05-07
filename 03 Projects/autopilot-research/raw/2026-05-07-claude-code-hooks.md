<!-- compiled: 2026-05-07 → wiki/claude-code-hooks/ (5 articles + _index.md) -->
---
source: yt-pipeline (auto-mode first run)
topic: Claude Code hooks
generated: 2026-05-07
videos_count: 5
notebook_id: c8db4d82-8e33-4bab-ad6e-f6491bd2c3c0
deliverable: report
sources:
  - https://www.youtube.com/watch?v=ENNZEqvodgY  # AI Terminal — Hooks Deep Dive: All 9 Events
  - https://www.youtube.com/watch?v=bOewYZvpiNo  # Code Playbook — Course 11 - Hooks
  - https://www.youtube.com/watch?v=G9OBGn0h6LE  # Joe Rhew — Get Notified When Tasks Finish
  - https://www.youtube.com/watch?v=3CSi8QAoN-s  # Matt Pocock — Force Claude to use right CLI
  - https://www.youtube.com/watch?v=0qqV4yv-Hss  # Simon Scrapes — Master 80% of Claude Code
---

# Claude Code hooks — autopilot bundle

## Summary (NotebookLM auto)

Summary:
Các nguồn tài liệu này cung cấp cái nhìn chi tiết về **Claude Code hooks**, một 
tính năng cho phép thực thi các lệnh tự động dựa trên các sự kiện cụ thể trong 
chu kỳ hoạt động của AI. Người dùng có thể thiết lập các **lệnh điều hướng xác 
thực** để thực hiện các tác vụ như thông báo, định dạng mã nguồn hoặc ngăn chặn 
các hành động nguy hiểm một cách nhất quán. Tài liệu phân biệt rõ giữa **hook 
lệnh** dành cho các tự động hóa đơn giản và **hook gợi ý** sử dụng AI để thiết 
lập các rào cản bảo mật. Ngoài việc hướng dẫn cài đặt qua tệp cấu hình JSON hoặc
lệnh trực tiếp, các nguồn này còn nhấn mạnh tầm quan trọng của việc **quản lý 
ngữ cảnh** để duy trì hiệu suất. Việc sử dụng hook giúp chuyển đổi các chỉ dẫn 
thủ công thành các **quy trình thực thi chắc chắn**, giúp tối ưu hóa luồng công 
việc cho kỹ sư. Cuối cùng, các ví dụ thực tế như tạo thông báo âm thanh hoặc 
kiểm tra cấu trúc thư mục minh họa khả năng **tùy biến mạnh mẽ** của công cụ 
này.

## Trends

Continuing conversation 27d423b7...
Answer:
Analysis of the provided sources reveals several consistent patterns regarding 
the implementation, purpose, and creation of Claude Code hooks.

### **Core Patterns Across Sources**

*   **Deterministic Automation:** A primary theme is that hooks are 
**deterministic**, meaning they run automatically and consistently based on 
specific events without the "probabilistic" nature of an LLM [Source 2, Source 
3, Source 5]. They are described as "event-driven shell commands" that function 
similarly to Git hooks [Source 1, Source 3].
*   **Preserving "Instruction Budget":** Multiple sources emphasize that moving 
instructions (like formatting rules or CLI preferences) out of `CLAUDE.md` and 
into hooks saves the LLM's "instruction budget" [Source 4, Source 5]. By 
enforcing rules deterministically through hooks, the LLM can focus its context 
window on complex reasoning rather than remembering basic workflow constraints 
[Source 4, Source 5].
*   **Standard Lifecycle Events:** The sources consistently identify a set of 
**9 trigger events** [Source 3]. The most frequently cited events include:
    *   `session start` and `session end` [Source 1, Source 2, Source 3].
    *   `pre-tool use` and `post-tool use` [Source 1, Source 2, Source 3].
    *   `stop` (when Claude finishes a task) [Source 1, Source 2, Source 3].
*   **Common Use Cases:**
    *   **Notifications:** Getting a desktop alert or sound (like a chime or a 
meow) when Claude finishes a long task or needs permission [Source 1, Source 2, 
Source 3, Source 5].
    *   **CLI Enforcement:** Forcing Claude to use specific tools, such as 
`pnpm` instead of `npm`, or preventing destructive commands like `git push` 
[Source 4].
    *   **Code Quality:** Automatically running linters, formatters (like 
Prettier), or test suites after a file is modified [Source 2, Source 3].

### **Most-Mentioned Approach**

The most-mentioned approach for **creating and managing hooks** is to **let 
Claude Code write the hooks for you** [Source 1, Source 4, Source 5]. 

Rather than manually editing the `settings.json` file, experts recommend:
1.  **Providing Documentation:** Feeding Claude the URL to the official hooks 
documentation [Source 1].
2.  **Instruction Conversion:** Asking Claude to analyze existing instructions 
in `CLAUDE.md` and convert them into deterministic bash scripts and hook 
configurations [Source 4].
3.  **Refinement via AI:** Using Claude to "reason" through the necessary logic 
for the hook, especially for complex filtering like "MECE directory checks" 
(ensuring folder structures don't overlap) [Source 2].

### **Critical Implementation Insights**
*   **Latency Warnings:** While prompt hooks (AI-evaluated hooks) are powerful 
for security guardrails, they can add significant latency to the workflow 
[Source 2]. As a result, users are often advised to favor **command hooks** 
(pure shell scripts) for speed [Source 2, Source 3].
*   **Location:** Hooks can be configured at a **user level** (global) or a 
**project level** within `settings.json` [Source 1]. If using plugins, hooks may
also be bundled in a `hooks.json` file [Source 1].

Resumed conversation: 27d423b7-55d5-4f28-bda8-1251519f276f

## Outliers

Answer:
While most sources present Claude Code hooks as a powerful tool for automation 
and efficiency, there are notable conflicts regarding their **practical 
utility**, **productivity impact**, and **technical definition**.

### **The Most Contrarian Stance: Productivity vs. Latency**
**Source 2 (Joe Rhew)** takes the most contrarian stance, specifically regarding
the impact of hooks on a user's workflow. While other experts frame hooks as a 
way to "speed up your workflow massively" [Source 5], Source 2 warns that they 
can actually **harm productivity**.

*   **Conflict:** Source 2 describes getting "quite frustrated" with how long 
hooks were taking to run, eventually leading him to **remove most of his hooks**
because the latency added to the workflow was too high [Source 2].
*   **Prompt Hooks:** He notes that while deterministic code is fast, any hook 
that requires Claude to "reason" (a prompt hook) adds significant 
token-processing time [Source 2].

### **Conflict Over Necessity and Value**
There is a clear disagreement among the experts regarding how essential hooks 
actually are for the average user.

*   **The Minimalist View:** **Source 1** expresses skepticism about their broad
necessity, stating, "I don't really do a whole lot of hooks myself and I don't 
really see a big need for a lot of them just personally" [Source 1].
*   **The Essential View:** In direct contrast, **Source 3** claims hooks are 
"one of the most powerful features in Claude Code" [Source 3], and **Source 4** 
advocates for using them to replace `CLAUDE.md` entirely to preserve the LLM's 
"instruction budget" [Source 4].

### **Conflict in Technical Definition: AI vs. No-AI**
Sources conflict on whether hooks should be considered "AI-driven" or "AI-free" 
tools.

*   **Deterministic Only:** **Source 5** and **Source 3** emphasize that hooks 
are "non AI deterministic token-free actions" or "pure automation" where "no LLM
is involved" [Source 3, Source 5].
*   **AI-Evaluated (Prompt Hooks):** Conversely, **Source 2** and **Source 3** 
also describe "prompt hooks," which are specifically **evaluated by the AI** to 
provide guardrails or perform subjective reasoning, such as checking for 
directory structure overlaps [Source 2, Source 3].

### **Summary of Expert Conflicts**

| Topic | Perspective A | Perspective B |
| :--- | :--- | :--- |
| **Workflow Impact** | Speed up workflow and enable "set and forget" automation
[Source 5]. | Can cause frustration and slow down the CLI to the point of being 
unusable [Source 2]. |
| **CLAUDE.md** | `CLAUDE.md` is the primary place for rules [Source 5]. | You 
should "almost always" delete `CLAUDE.md` and use hooks for deterministic 
enforcement instead [Source 4]. |
| **Ease of Use** | Hooks are simple "event-driven shell commands" [Source 1]. |
Designing complex hooks requires intricate "filtering and routing" patterns to 
avoid unintended triggers [Source 2]. |

Conversation: 27d423b7-55d5-4f28-bda8-1251519f276f (turn 1)

## Gaps

Answer:
Based on the provided sources, while there is a significant amount of 
information regarding the "what" and "why" of Claude Code hooks, several 
technical, practical, and platform-specific gaps remain.

### **Technical Implementation Gaps**

*   **Non-Bash Languages:** The sources almost exclusively focus on **bash 
scripts** and `.sh` files for "command hooks" [Source 4, Source 8, Source 12]. 
There is no information on whether hooks can natively execute other languages 
(like Python or Node.js) without a bash wrapper, or how to handle environments 
where bash is not the default shell.
*   **Windows Compatibility:** All practical demos and examples provided are 
tailored for **macOS/Unix environments** [Source 3, Source 11]. There is no 
mention of how hooks function on Windows, specifically regarding file extensions
(e.g., using `.bat` or `.ps1` files) or configuration differences in 
`settings.json`.
*   **Debugging Hooks:** None of the sources explain how to **debug a hook** 
that fails or behaves unexpectedly. It is unclear if there are logs available 
for hook execution or how a user can troubleshoot a hook that is "silently" 
failing to trigger.
*   **Variable Passing:** While sources mention that hooks trigger on events 
like `write` or `edit` [Source 2, Source 29], they do not explicitly detail how 
to **pass metadata** from that event into the script. For example, it is unclear
how a script can programmatically identify *which* specific file was just edited
to run a linter only on that file.

### **Unanswered Questions About Scaling and Efficiency**

*   **Prompt Hook Overhead:** While Source 2 notes that "prompt hooks" 
(AI-evaluated hooks) add latency [Source 28], no source quantifies the **token 
cost** or the specific "instruction budget" impact of these hooks compared to 
standard prompts.
*   **Conflict Resolution:** Source 4 mentions that matching hooks run **in 
parallel** [Source 36]. This raises unanswered questions about race conditions: 
what happens if two parallel hooks attempt to modify the same file or lock the 
same process simultaneously?
*   **Performance Limits:** There is no guidance on the **maximum number of 
hooks** a project can support before the system's performance significantly 
degrades.

### **Uncertainties Regarding "Hookify" and Plugins**

*   **The Hookify Plugin:** Source 1 introduces "Hookify" as a potential tool 
for analyzing conversations to create hooks automatically, but the expert 
admits, "**it's actually a little unclear**... whether it's actually messing 
with the settings.json file or not. I actually don't know, I haven't tried it 
yet" [Source 7].
*   **Plugin Integration:** Managing hooks within plugins is described as 
"**difficult and tough to remember**" [Source 8]. The sources do not provide a 
clear walkthrough on the structure or management of the `hooks.json` file used 
within these plugins.

### **Recommended Follow-up Research**

To gain a complete understanding, a follow-up search should focus on:
1.  **Windows-specific documentation:** Verifying if `.bat` or PowerShell 
scripts are supported and how the pathing differs in `settings.json`.
2.  **Hook Environment Variables:** Investigating the "reference docs" mentioned
in Source 1 to see if Claude passes environment variables (like 
`$CLAUDE_FILE_PATH`) to the hook scripts.
3.  **Error Handling:** Determining the behavior of the CLI when a hook exits 
with a non-zero code—does it stop the entire agentic loop or just provide a 
warning? [Source 38, Source 39].
4.  **The "Pre-Compact" Event:** While listed as one of the 9 events, no source 
provides a practical use case or example for triggering an action before context
compaction [Source 3, Source 33].

Conversation: 27d423b7-55d5-4f28-bda8-1251519f276f (turn 1)

## Key Takeaways

Answer:
*   **Offload your `CLAUDE.md` instructions** into deterministic hooks to save 
the LLM's "instruction budget" and prevent it from getting confused by too many 
global, non-deterministic rules [Source 4].
*   **Let Claude write your hooks** for you by providing it with the official 
documentation URL and asking it to convert your current natural language project
rules into `.sh` bash scripts and `settings.json` configurations [Source 1, 
Source 4].
*   **Prioritize deterministic "command hooks"** over AI-evaluated "prompt 
hooks" to avoid significant latency and workflow frustration caused by the AI's 
"reasoning" time [Source 2, Source 3].
*   **Use the `session start` event** to force-load specific business context or
memory files reliably every time you open the CLI, rather than relying on 
Claude's subjective judgment of when to read a reference file [Source 5].
*   **Implement a filtering and routing pattern** for broad triggers (like 
`pre-tool use`) by sending them to a script that checks for specific command 
patterns (e.g., `mkdir`) or file extensions before executing further logic 
[Source 2].
*   **Enforce project guardrails** by creating hooks that programmatically block
destructive commands like `git push` or automatically redirect Claude to use 
preferred tools, such as `pnpm` instead of `npm` [Source 4].
*   **Establish a "human-in-the-loop" alert system** by configuring hooks on the
`stop` or `permission request` events to trigger desktop notifications or audio 
chimes so you can multi-task while Claude works [Source 1, Source 5].

Conversation: 27d423b7-55d5-4f28-bda8-1251519f276f (turn 1)

# 5.1 Prompt Library & Demo Scripts

**Source:** https://transform.sg.larksuite.com/wiki/Jlu0wGtnyiemGbkTTTdlbGqag1c
**Wiki ID:** Jlu0wGtnyiemGbkTTTdlbGqag1c
**Archived:** 2026-05-07

---

Lark Docs
C
Claude Course 2026
Public access
Table of contents
Khoá học Claude toàn diện tiếng Việt
Lộ trình học tập.pdf
25 tập khám phá Claude AI
Lộ trình tự học 5 buổi × 2 tiếng
Buổi 1. Hiểu cỗ máy và khung tư duy 4D
Buổi 2. Prompting Mastery — Vòng lặp Description ↔ Discernment
Buổi 3. Projects & Artifacts — Không gian làm việc chuyên dụng
Buổi 4. Skills & Research — Đóng gói quy trình + Đào sâu đa nguồn
Buổi 5. Cowork & Automation
Slide: Cowork & Automation.pdf
5.1 Prompt Library & Demo Scripts
5.2 Handouts học viên
5.3 Workbook học viên (CUỐI KHÓA)
5.4 Demo Assets (CUỐI KHÓA)
5.5 Checklist chuẩn bị (CUỐI KHÓA)
🔥
Recap 5 buổi học Claude AI online
Anthropic courses
📣
Bổ sung course
Transform Group

5.1 Prompt Library & Demo Scripts

Last updated: Apr 20

Log In or Sign Up
5.1 Prompt Library & Demo Scripts
Demo Cowork: Monthly Reconciliation
🎯 Mục tiêu demo
⏱ Thời gian
🛠 Setup trước buổi
📝 CLAUDE.md cho demo (paste-ready)
📝 Sample mock data (tạo trong buổi nếu chưa có)
🎬 Demo Script
Bước 1: Show folder + CLAUDE.md (2 phút)
Bước 2: Prompt I-T-O (1 phút)
Bước 3: Claude show plan (2 phút)
Bước 4: Answer clarifying + approve (1 phút)
Bước 5: Simulate Cowork running (1 phút)
Bước 6: Steering demo (2 phút)
Bước 7: 3-step review output (2 phút)
CLAUDE.md Templates theo role
Template A: Sales Pipeline Tracking
Template B: Content Marketing Production
Template C: Engineering Project Workspace
Template D: Executive Assistant
Template E: Research Team
Scheduled Task Examples
Example 1: Daily Brief (EA role)
Example 2: Weekly Pipeline Report (Sales)
Example 3: Monthly Close (Finance)
Example 4: Competitor Monitoring
Example 5: Quarterly Deep Dive
Diligence Statement Templates
Template 1: Internal Report
Template 2: External / Client-facing
Template 3: Academic / Research
Template 4: Journalism / Public Communication
Template 5: Personal / Professional Email
Cowork Prompts — Common patterns
Pattern A: Reconciliation / Data matching
Pattern B: Report generation from multiple sources
Pattern C: Analysis + Recommendation
Pattern D: Multi-file consolidation
Pattern E: Research synthesis
Fallback Scenarios
Scenario 1: Học viên không có Cowork (Free plan)
Scenario 2: Scheduled Task không available
Scenario 3: Diligence statement feels "over-engineered"
Scenario 4: Student overwhelmed by all tools (Projects + Skills + Cowork + Research)
Scenario 5: Student worried about "AI replacing me"
Advanced Tips
Tip 1: Cowork + Scheduled + Diligence = full loop
Tip 2: "Draft always, auto-send never"
Tip 3: Audit log monthly
Tip 4: Diligence review triggered by events
5.1 Prompt Library & Demo Scripts​
Modified April 20
​
Mục đích: Scripts cho demo Cowork workflow + Scheduled Task + Diligence templates.​
​
Demo Cowork: Monthly Reconciliation​
🎯 Mục tiêu demo​
End-to-end Cowork workflow với CLAUDE.md + I-T-O prompt + Plan review + Steering + Output review.​
⏱ Thời gian​
15 phút (setup + run + review)​
🛠 Setup trước buổi​
Folder structure demo (create trước):​
​
Code block​
Plain Text
Copy
📁 monthly-close/​
├── 📁 january-2026/​
│   ├── bank-statements-jan2026.csv  (mock data, 50 rows)​
│   ├── erp-export-jan2026.xlsx       (mock data)​
│   └── reconciliation-template.xlsx  (blank template)​
├── 📁 output/ (empty)​
└── CLAUDE.md​
​
📝 CLAUDE.md cho demo (paste-ready)​
​
Code block​
Markdown
Copy
# Monthly Financial Close — Finance Department​
​
## Purpose​
Monthly reconciliation between bank statements and ERP ​
records. Identify discrepancies, categorize by department.​
​
## Team​
- Finance Analyst (me) — operational reconciliation​
- CFO — reviews final output, sign-off​
- Audit team — quarterly review​
​
## Output preferences​
- Format: Excel workbook (.xlsx)​
- Sheets order: Summary, Matched, Discrepancies, By Dept​
- Currency: VND with thousand separator (1.000.000)​
- Date format: DD/MM/YYYY​
- Colors: flagged items red, resolved green​
​
## Rules — ABSOLUTE​
- ALL numbers must trace to source (bank row or ERP row)​
- NEVER drop transactions — flag if can't match​
- Flag "[Needs manual review]" for edge cases​
- Threshold for flagging discrepancy: > 100.000 VND​
- Output ALWAYS saved to ./output/ subfolder​
- Filename pattern: [month]-[year]-reconciliation-[timestamp].xlsx​
​
​
Comments (0)
Help Center
Keyboard Shortcuts

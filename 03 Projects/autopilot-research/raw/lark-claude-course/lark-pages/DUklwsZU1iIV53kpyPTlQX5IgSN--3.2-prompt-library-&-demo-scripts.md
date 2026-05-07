# 3.2 Prompt Library & Demo Scripts

**Source:** https://transform.sg.larksuite.com/wiki/DUklwsZU1iIV53kpyPTlQX5IgSN
**Wiki ID:** DUklwsZU1iIV53kpyPTlQX5IgSN
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
Slide: Projects & Artifacts.pdf
3.2 Prompt Library & Demo Scripts
3.3 Handouts học viên
3.4 Workbook học viên
3.5 Demo Assets
3.6 Checklist chuẩn bị đầy đủ cho giảng viên
Buổi 4. Skills & Research — Đóng gói quy trình + Đào sâu đa nguồn
Buổi 5. Cowork & Automation
🔥
Recap 5 buổi học Claude AI online
Anthropic courses
📣
Bổ sung course
Transform Group

3.2 Prompt Library & Demo Scripts

Last updated: Apr 20

Log In or Sign Up
3.2 Prompt Library & Demo Scripts
Demo Project Setup
🎯 Mục tiêu demo
⏱ Thời gian
🛠 Setup trước buổi
📝 Project Setup Steps
Step 1: Create project
Step 2: Custom Instructions (paste-ready)
Step 3: Upload knowledge base
Step 4: Test với 3 prompts
🔄 Fallback — Nếu demo fail
Demo Artifacts: 3 Examples Live
🎯 Mục tiêu demo
⏱ Thời gian
Tuy nhiên nếu có time, live demo rất đáng:
Demo Artifact 1: Mermaid Flowchart
Demo Artifact 2: Document (Markdown → Word)
Demo Artifact 3: Interactive React Component
Demo Connector: Google Drive Setup
🎯 Mục tiêu demo
⏱ Thời gian
🛠 Pre-setup (để buổi diễn nhanh)
📝 Setup Steps
Step 1: Mở chat → "Search and tools" (góc dưới-trái)
Step 2: Click "Add connectors" → search "Google Drive" → Connect
Step 3: Grant permissions — CHỈ Read + Search (không check Write)
Step 4: Confirm → back to Claude
Step 5: Test với 3 prompts
🔄 Fallback
Custom Instructions Templates
📝 Template 1: Content Marketing Project
📝 Template 2: Engineering Project
📝 Template 3: Research / Analysis Project
📝 Template 4: Sales Project
Fallback Scenarios
Scenario 1: Học viên không đủ files BTVN
Scenario 2: Học viên không có Custom Instructions draft
Scenario 3: Claude rate limit khi demo
Scenario 4: Connector không setup được (company firewall)
Scenario 5: Artifact không render
Advanced Tips
Tip 1: Combine Project + Artifact
Tip 2: Project + Connector workflow
Tip 3: Meta-prompt cho Custom Instructions
3.2 Prompt Library & Demo Scripts​
Modified April 20
​
Mục đích: Tất cả prompts + scripts cho demo Buổi 3. ​
Cách dùng: Copy-paste ready, giảng viên mở song song slide.​
​
Demo Project Setup​
🎯 Mục tiêu demo​
Show end-to-end flow tạo Project trong 10-12 phút. Học viên sẽ replicate ngay sau đó.​
⏱ Thời gian​
15 phút (setup + instructions + upload + test)​
🛠 Setup trước buổi​
Chuẩn bị 5 file hư cấu (đã test upload):​
1.
2026-01-Q1-Offsite-DaLat-Recap.pdf — Meeting notes từ Q1 offsite​
2.
Venue-Shortlist-South-VN-2026.xlsx — 10 venues comparison (name, location, capacity, price, distance)​
3.
2025-Offsite-Budget-Actual.xlsx — Budget history​
4.
Participant-List-45-People-Dietary-Preferences.csv — 45 rows với dietary info​
5.
Offsite-Agenda-Template-2024.docx — Template agenda 3 ngày​
​
💡 Gợi ý: file mẫu có thể hư cấu toàn bộ. Mục tiêu show upload flow + retrieval, không cần data real.​
​
📝 Project Setup Steps​
Step 1: Create project​
Vào: claude.ai/projects → "+ New Project"​
Fields:​
•
Name: Team Offsite Q2 2026 Planning​
•
Description: Plan 3-day offsite cho team 45 người, tháng 5/2026, budget 500M VND​
•
Visibility: Private​
Narration (cho lớp nghe):​
​
"Tên có 4 elements: Topic (Team Offsite), Timeframe (Q2 2026), Action (Planning), Specificity (đủ để phân biệt với offsite khác). Đừng dùng 'My project' hay 'Project 1'."​
​
Step 2: Custom Instructions (paste-ready)​
​
Code block​
Plain Text
Copy
## CONTEXT​
​
Dự án này để plan team offsite Q2 2026 cho công ty tech ​
startup 45 người tại Việt Nam. ​
​
Offsite details:​
​
Comments (0)
Help Center
Keyboard Shortcuts

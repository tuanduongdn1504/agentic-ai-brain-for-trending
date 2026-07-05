# Mì AI CV Matching AI Agent — Overview

## Source

- Video: [Xây dựng CV Matching AI Agent, tự động tìm việc phù hợp - Mì AI](https://www.youtube.com/watch?v=7gIwR5SwM_0) — 2026-07-04, 43:59, ~519 views at fetch, channel ~52K subs (**FIRST-PARTY**: the builder walking through his own repo)
- Repo: [thangnch/MiAI_CV_Matching_AI_Agent](https://github.com/thangnch/MiAI_CV_Matching_AI_Agent) — created 2026-07-03 (one day before the video), 8 files, ~36KB Python, **NO license**
- Raw bundle: `raw/2026-07-05-miai-cv-matching-agent.md` (full VN transcript + all 8 repo files)

## What it is

- A **lab-grade CV↔job matching agent**: crawl job descriptions → embed into a local vector DB → user uploads a CV PDF → a LangChain agent reads the CV, vector-searches the JDs, and returns the top-3 matches with a 0–100 score, strengths, missing skills, and improvement tips — streamed to a Streamlit UI via SSE.
- Stack: **LangChain 1.0 `create_agent`** + **ChatOpenAI gpt-4o-mini (temp 0)** + **OpenAI text-embedding-3-small** + **ChromaDB (local)** + **FastAPI/Uvicorn + SSE** + **Streamlit**.
- Explicitly positioned by the author as mindset-building, not production: *"làm lab thì rất dễ nhưng làm mà chạy được thì sẽ rất khó"* (labs are easy; making it actually run is hard). Accuracy is explicitly unverified on camera.

## Who made it (verified)

- **Nguyễn Chiến Thắng** (GitHub `thangnch`) — Director of Development Center, IT Division, **Saigon Hanoi Bank (SHB)**; ~18 years fintech/banking (VIB, VCCORP, M-PAY). Runs the **Mì AI** community (~60K members; motto *"Học AI theo cách Mì ăn liền"* — learn AI the instant-noodle way).
- GitHub: 246 public repos, **77 MiAI_-prefixed** (repo-per-video pattern), 1,271 followers, since 2018.
- This is the channel's **first recruitment/HR-topic video** (80 recent videos searched — zero prior CV/tuyển-dụng content).
- OpenAI API credits lent by community sponsor "Sử Minh Thành" (video-attested only; no public profile found). The demo CV itself was **written by Claude** ("mình dùng Claude để viết ra — tất cả thông tin không có thật").

## Why it matters to this vault

- It is a first-party, working, readable implementation of **exactly the feature domain of hireui/TalentAxis** (candidate↔job matching in a recruitment SaaS) — see [[claude-stack-port]] and the pilot menu in `output/`.
- Second VN first-party channel in the corpus (after [[external|Storm Bear: hoidanit-fullstack-vibe-coding]]); a senior banking-IT practitioner teaching agent engineering in Vietnamese.
- The demo's honest gaps (LLM-invented scores, bypassed validation layer, robots.txt reality) are more instructive than its happy path — see [[code-audit]], [[matching-quality-vs-production]], [[caveats-and-corrections]].

## Key Takeaways

- Blueprint-before-code pedagogy: the author insists on giving viewers an architecture map before any code — his stated differentiator vs other creators.
- The agent pattern is minimal and canonical: one LLM + one retrieval tool + one structured-output schema — a good "smallest real agent" reference.
- The match score is **LLM judgment, not vector similarity** — the retrieval layer never surfaces its scores ([[code-audit]]).
- The video's only refuted claim: "Google Careers doesn't block crawling" — it does, via robots.txt, on the exact path crawled ([[crawl-reality-and-robots]]).
- Cost advice targets the wrong line: embeddings are <1% of spend; the LLM analysis is ~99% ([[cost-economics]]).
- For hireui, the crawl half evaporates (the SaaS owns both CVs and JDs); the transferable core is embed→retrieve→LLM-judge→structured-output→SSE ([[claude-stack-port]]).

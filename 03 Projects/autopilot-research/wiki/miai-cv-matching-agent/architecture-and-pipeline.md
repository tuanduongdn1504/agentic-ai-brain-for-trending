# Architecture and Pipeline

## Source

Repo files (read in full): `job_crawls.py`, `hr_agent_format.py`, `hr_agent_tools.py`, `hr_agent.py`, `hr_agent_be.py`, `hr_agent_fe.py`. Video 7gIwR5SwM_0 sections 1–2.

## Two flows, six files

### Flow 1 — Ingestion (run once / periodically): `job_crawls.py`

1. Crawl `https://www.google.com/about/careers/applications/jobs/results?location=Vietnam`, 5 pages (`&page=N`), httpx + BeautifulSoup, spoofed Safari User-Agent.
2. Collect job URLs via `a[href*='jobs/results/']`, then scrape each page **in parallel** (asyncio + semaphore, concurrency 8, 20s timeout).
3. Structured extraction: h2 title + only the sections *Minimum qualifications / Preferred qualifications / About the job / Responsibilities* (fallback: whole page minus nav/footer/header).
4. **Delete** Chroma collection `job_postings`, then re-embed everything (demo-grade dedup-by-wipe).
5. Embed **whole JDs** (no chunking) with `text-embedding-3-small`, batches of 15, into local `./chroma_db`. Metadata stored: `{source: url, title}` — **no job_id** (see [[code-audit]]).

### Flow 2 — Serving (per request): FE → BE → agent → tool

1. **Streamlit FE** (`hr_agent_fe.py`): upload PDF → POST to `/find_jobs` → render SSE progress + result cards.
2. **FastAPI BE** (`hr_agent_be.py`): read PDF → base64 → LangChain multimodal content block `{"type":"file", "base64":…, "mime_type":"application/pdf"}` → `agent.astream(stream_mode="values")` → translate agent events into SSE (`status` / `result` / `done`). The **model itself reads the PDF** (no local PDF parser).
3. **Agent core** (`hr_agent.py`): `create_agent(model=ChatOpenAI("gpt-4o-mini", temp=0), tools=[search_jobs], system_prompt=career-coach-instructions, response_format=ProviderStrategy(MatchResponse))`.
4. **Tool** (`hr_agent_tools.py`): `search_jobs(query, top_k=5, where_document)` → Chroma `asimilarity_search` → returns `{metadata + content}` per hit (no similarity scores).
5. **Schema** (`hr_agent_format.py`): Pydantic `MatchResult` (job_id, job_title, job_url, match_score 0–100, strengths, reasoning, missing_skills, improvement_tips) with defensive alias validators — see [[defensive-output-schema]].

## Design choices worth noting

- **Build order pedagogy**: format → tool → agent → backend → frontend ("never build the frontend first") — bottom-up from the smallest testable unit, each layer smoke-tested before the next.
- **SSE for agent progress**: tool_calls → "searching…", tool result → "found, analyzing…", final AI message → result. A cheap, effective agent-UX pattern.
- Embedding-model consistency stressed on camera: query-time embedding model MUST equal ingest-time model or retrieval is silently wrong.
- The author deliberately rotates vector DBs across videos (FAISS/Qdrant/Chroma claimed) for pedagogy; Chroma-local here is demo-only ("thực tế thì sẽ không dùng cái này đâu").

## Key Takeaways

- Minimal-real-agent reference: 1 LLM + 1 tool + 1 schema + SSE ≈ 250 lines of core logic.
- The pipeline is a textbook bi-encoder retrieval + LLM-judge design — see [[matching-quality-vs-production]] for where that sits vs production systems.
- Demo shortcuts are explicit and separable: DB wipe, open CORS, Streamlit, local Chroma.
- The PDF-to-model path (base64 file block, no parser) removes a whole parsing subsystem — same pattern exists on Claude via document blocks ([[claude-stack-port]]).
- Ingestion and serving are cleanly decoupled through the vector store — the two halves can be swapped independently (e.g., replace crawling with your own DB).

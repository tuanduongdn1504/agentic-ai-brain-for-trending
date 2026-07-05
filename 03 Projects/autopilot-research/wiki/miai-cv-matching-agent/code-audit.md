# Code Audit (all 8 files, findings independently re-derived)

## Source

Main-loop full read of all 8 repo files + dive `code-audit` + refute-first verify (5/5 headline findings CONFIRMED against file:line).

## Load-bearing defects (CONFIRMED)

1. **match_score is pure LLM invention** — `hr_agent_tools.py:73` `asimilarity_search` returns Documents without scores; `_format_result` passes `{source, title, content}` only. The 0–100 score has zero numeric grounding ([[matching-quality-vs-production]]).
2. **job_id contract gap** — `hr_agent_format.py:11` requires `job_id`; ingestion (`job_crawls.py:152–155`) stores only `{source, title}`. The LLM must fabricate an ID (Google Careers result URLs carry no stable numeric ID). Any "apply by job_id" feature would silently break.
3. **Validation layer bypassed on the wire** — BE streams raw `latest_message.content` (`hr_agent_be.py:82–84`); `structured_response` is never read (`stream_mode="values"` doesn't expose it); FE strips ```json fences and re-parses with its own alias fallbacks (`hr_agent_fe.py:343–384`) ([[langchain-v1-agent-stack]]).
4. **Security/PII posture** — CORS `allow_origins=["*"]`, no auth, no file-size/MIME validation; full CV PDF base64'd to a third-party API with no consent/redaction ([[recruitment-ai-regulatory-context]]). Author flags CORS as demo-only on camera; the rest is unmentioned.
5. **No chunking** — whole JD = one embedding ([[matching-quality-vs-production]]).

## Smaller defects (code-verified)

- Collection **delete + full re-ingest** every crawl run (author: demo-only).
- New Chroma client + embeddings object per `search_jobs` call — no reuse, added latency.
- No timeout around `agent.astream` — a hung LLM call blocks the SSE connection indefinitely.
- No logging of decisions/scores/queries — nothing to audit or debug with.
- Streamlit FE: results lost on any rerun (no `session_state`; `if "final_json" not in dir()` hack).
- `from webbrowser import Chrome` in `job_crawls.py:5` — unused stray import (likely IDE auto-import; httpx is the real client).
- Static marketing metric cards in the FE ("~30s", "100+ vị trí", "phân tích chính xác") — decoration unconnected to runtime.
- PDF input cost unbounded/untracked (FE hints 10MB but BE never enforces).

## What the code does well (credit where due)

- The defensive Pydantic schema ([[defensive-output-schema]]) — genuinely good hardening.
- Semaphore-bounded parallel scraping (concurrency 8, timeouts, per-URL error isolation via `gather(return_exceptions=True)`).
- Structured JD extraction targeting the four meaningful sections, with graceful fallback.
- Batch embedding (15/batch) instead of per-doc calls.
- SSE progress UX mapped to real agent lifecycle events — cheap and effective.
- temp=0, `.env` for keys, embedding-model consistency between ingest and query, clean file-per-concern layout, bilingual comments that teach.

## Key Takeaways

- The three-layer lesson: **schema (good) → serving path (bypasses schema) → UI (re-implements schema badly)** — always trace which object reaches the wire.
- Contract gaps between pipeline stages (job_id) don't crash — the LLM papers over them, which is worse.
- The demo's own disclosed shortcuts (CORS, wipe, Streamlit, accuracy) are the honest ones; the undisclosed gaps (score grounding, PII, job_id) are where readers get hurt.
- Reusable checklist for any LLM feature: Is the validated object served? Are retrieval scores surfaced? Is every schema field actually produced upstream? Is PII flow consented and bounded? Is anything logged?

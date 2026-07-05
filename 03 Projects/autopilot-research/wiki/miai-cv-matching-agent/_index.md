# miai-cv-matching-agent

> Mì AI's CV Matching AI Agent (video 7gIwR5SwM_0, 2026-07-04 + repo `thangnch/MiAI_CV_Matching_AI_Agent`) — a first-party, lab-grade LangChain 1.0 agent that matches CV PDFs against crawled job descriptions (embeddings + ChromaDB + gpt-4o-mini structured outputs + SSE). Compiled 2026-07-05 from the full VN transcript + all 8 repo files + 17-agent dive/refute-first workflow (`wf_dd724957-cac`). **The corpus' most direct hireui-domain source**: candidate↔job matching for a recruitment SaaS.

## Articles

- [[overview]] — what it is, verified author identity (SHB banking-IT director, Mì AI ~60K community), why it matters
- [[architecture-and-pipeline]] — the 6-file two-flow design (crawl→embed; upload→agent→SSE), build-order pedagogy
- [[langchain-v1-agent-stack]] — create_agent / ProviderStrategy / structured_response verified against docs + the streaming-bypasses-validation mismatch
- [[defensive-output-schema]] — the Pydantic alias-normalization hardening pattern, where it's redundant vs load-bearing
- [[crawl-reality-and-robots]] — video claim REFUTED: robots.txt disallows the crawled path; VN job-board bot-blocking confirmed live
- [[matching-quality-vs-production]] — single-stage LLM scoring vs two-stage retrieval+rerank; position bias, calibration, taxonomies; upgrade tiers
- [[cost-economics]] — verified: ~$0.00134/CV, ~$13/mo at 10K CVs; the video's cost tip targets the wrong line
- [[claude-stack-port]] — full translation to Claude (Haiku 4.5 + structured outputs + document blocks) + Voyage (embeddings/rerank); the no-vector-DB v1 simplification for hireui
- [[recruitment-ai-regulatory-context]] — AEDT reality: NYC LL144, EU AI Act extension to 2027-12, Illinois, Colorado SB 26-189, Vietnam PDPL
- [[code-audit]] — 5 confirmed load-bearing defects (LLM-invented scores, job_id gap, bypassed validation, PII posture, no chunking) + honest credits
- [[caveats-and-corrections]] — refuted/corrected/unverifiable claims, garble notes, no-license caveat
- [[source-provenance]] — how this was built; agent death + main-loop takeover; ground-truth hierarchy

## Pilot deliverable

- `output/(C) 2026-07-05-miai-cv-matching-agent-pilot-methods.md` — multi-method application menu (hireui Goal-#2 headline: the matching feature as hireui's first LLM feature, Claude-stack, eval-first, compliance-aware)

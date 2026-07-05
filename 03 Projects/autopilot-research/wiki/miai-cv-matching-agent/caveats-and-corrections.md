# Caveats and Corrections (Rule 12 — fail loud)

## Refuted / corrected claims

- **REFUTED (video):** "Google Careers doesn't block crawling" — robots.txt explicitly disallows the exact paginated path; only *technical* enforcement is absent ([[crawl-reality-and-robots]]).
- **CORRECTED (video's cost advice):** self-hosting embeddings to save money targets <1% of spend; LLM analysis is ~99%. Negative ROI ~2,000:1 at demo scale ([[cost-economics]]).
- **CORRECTED (dive arithmetic, caught by verify):** batch-API savings $0.35→**$4.28**/month; self-host savings $0.44→**$0.12–0.13**/month.
- **SUPERSEDED (verifier's own comparison):** its Anthropic math used stale model naming/pricing ("Claude 3.5 Sonnet $3/1M") — replaced by main-loop Haiku 4.5 math from the claude-api reference ([[claude-stack-port]]).
- **PARTIAL (dive):** "100 pages per PDF" for gpt-4o-mini not confirmed in current OpenAI docs (50MB limits confirmed); "create_agent builds a LangGraph state machine" → it *uses* LangGraph internally, you don't construct a graph; LangChain's FileContentBlock→OpenAI conversion mechanism is not officially documented.
- **UNVERIFIED effort estimates:** matching-architecture dive's "Tier 1 = 4 hours / +20–30% recall" has no literature support — keep the tiers, drop the numbers ([[matching-quality-vs-production]]).
- **PARTIAL (regulatory):** Colorado SB 24-205 never took effect as written — replaced by SB 26-189 (eff. 2027-01-01). Vietnam PDPL DPA/deletion specifics unverified ([[recruitment-ai-regulatory-context]]).

## Author claims left as claims (not fact-checked to confirmation)

- Prior Mì AI videos: **LangGraph video CONFIRMED** (9Mv7jQxGyEY) and **vector-DB explainer CONFIRMED** (fLMm57wvBA0); claimed FAISS / Qdrant / Streamlit-deploy videos were **not found** in an 80-video ytsearch sweep — unverifiable, not refuted (search coverage is incomplete; upload dates unavailable).
- "Sử Minh Thành" (API sponsor, sells "Open Claw" T-shirts): **video-attested only** — zero public web presence found. Do not state biographical facts about him.
- Fun corpus echo: "Open Claw" T-shirt merch is the same OpenClaw that [[external|Storm Bear: claude-code-clones]] tracks — VN community merch about a Claude Code fork.

## Provenance limits

- VN auto-captions garble tech terms ("lang trên"=LangChain, "chém gió" is the author's own slang for LLM-invented output, "mini 4o"=gpt-4o-mini — resolved against the repo, which is why repo-as-ground-truth matters).
- Repo has **no license** — treat as read-only reference: port patterns, don't copy files.
- One workflow agent death (claude-stack dive, "Prompt is too long" after invoking the large claude-api skill) — gap closed by main loop with first-party sources; logged in [[source-provenance]].
- Regulatory facts are date-sensitive (searched 2026-07-05); re-verify deadlines before relying on them.

## Key Takeaways

- One refuted video claim, two dive arithmetic errors, one stale-verifier correction, several unverifiable-not-false items — the standard yield of a refute-first pass on a good-faith source.
- The video is honest about its demo-grade nature; corrections here are about *claims*, not intent.
- Keep the discard-as-garble guard in mind: fresh true claims (EU deadline extension, Colorado replacement) look like errors to a training-bounded skeptic — both survived because they were searched, not recalled.

<!-- compiled: 2026-06-20 -->
---
source: path-5 yt-dlp (CAPTION-GAP) + triangulation
topic: agentic-analytics-harness
generated: 2026-06-20
primary_video: https://www.youtube.com/watch?v=K4-flzsPraE
deliverable: report
---

# Omni "Building the best agentic analytics harness" — source bundle

> **⚠️ CAPTION GAP — READ FIRST.** The operator-submitted video has **NO captions/subtitles** (confirmed twice: stale yt-dlp 2026.03.17 AND fresh yt-dlp 2026.06.09 both return "has no automatic captions / has no subtitles"). No local whisper/ffmpeg available in this worktree. **A verbatim transcript could not be obtained.** Per autopilot constitutional rule #4 (NEVER fabricate), this bundle is built by **triangulation** across the video's own description + Omni first-party blogs + a detailed third-party talk recap + the conference session listing. Provenance is tiered below and in `wiki/agentic-analytics-harness/source-provenance.md`.

## Primary source (video)

- **Title:** Building the best agentic analytics harness: Powered by Claude, built with Claude Code
- **Channel:** Claude (Anthropic official) · **Uploaded:** 2026-05-21 · **Duration:** 26:46 · ~31K views · Category: Science & Technology
- **Speaker:** Chris Merrick, Cofounder & CTO, Omni
- **Venue:** Code with Claude: Extended — London, 2026-05-20 · session 11:30 AM–12:00 PM, Founder stage (confirmed via claude.com/code-with-claude/london-extended)
- **Anthropic's own description (verbatim):** "Omni built the best agentic harness for analytics tailored for and powered by Claude models, with 99% of the platform's code written using Claude Code. Cofounder & CTO Chris Merrick shows how they architect their multi-agent system, design and size their tools, and evaluate effectiveness."

## Triangulation sources

| # | Source | Tier | URL |
|---|---|---|---|
| S1 | Video description (Anthropic first-party) | **T1 first-party** | youtube K4-flzsPraE |
| S2 | Omni blog — "Building Omni's architecture for agentic analytics" | **T1 first-party (Omni)** | omni.co/blog/building-omnis-architecture-for-agentic-analytics |
| S3 | Omni blog — "Improving AI quality with context" | **T1 first-party (Omni)** | omni.co/blog/improving-ai-quality-with-context |
| S4 | Code with Claude London listing | **T1 first-party** | claude.com/code-with-claude/london-extended |
| S5 | ai-heartland.com talk recap (Japanese) | **T2 third-party recap of THIS talk** | ai-heartland.com/agent/omni-agentic-analytics-harness/ |
| S6 | WebSearch snippets (token figure cross-confirm) | T2 corroboration | various |

---

## TIER 1 — first-party verified (S1–S4)

**The agent is called "Blobby."** Omni = a BI / analytics platform; Blobby = its embedded agentic analytics assistant.

**Architecture (S2):**
- A **coordinator** ("decides which tool to use next based on the question, the results, and what's already been tried"). Goes "past a single query and decide[s] what to do next — continuing an analysis, comparing datasets, investigating data for the right matches, or summarizing."
- A **summarization sub-agent** with its **own context window** (processes large results so they don't "clog up the context window of the main agent").
- Can "adapt mid-flight, retry when things break, or stop when it has something useful."

**Tools (S2) — 4 core tool types:**
1. **Topic picker + query tool** — inspects metadata across Topics, makes an informed choice before generating SQL.
2. **Field values tool** — fetches the list of valid field values and adjusts to find the correct match.
3. **Summarization tool** — the sub-agent above.
4. **Query execution** — runs SQL.
- **Data format constraint:** results return in **Arrow format with non-serializable types** → must be **transformed into CSVs** before re-introduction to the conversation.

**Semantic layer = "intelligence backbone" (S2, S3):**
- Stores **business context** (metrics, definitions, logic) so the agent "already know[s] what 'active customer' means."
- Context lives **in the semantic layer, NOT in a global prompt** — same trusted logic that powers every query/report/dashboard; human-visible/debuggable.
- **Metadata fields (S3):** `ai_context` (explicit AI instructions), `sample_values` (field examples), `synonyms` (alt names), `descriptions` (clarifications) — "keep it short and direct."
- **Three injection levels (S3):** **Model-level** (global house rules) → **Topic-level** (domain facts, default filters, example questions) → **View/field-level** (fine-tuning).
- **Capacity budget (S3):** model handles **~200k characters total; ~175k allocated to semantic-layer context.**
- **Feedback loop (S3):** read what users actually ask Blobby via **Analytics > AI usage dashboard**; refine context over time. Seed initial context from **dbt metadata.**
- Guidance: **start minimal** ("even a small amount of context is better than nothing").

**Error handling / resilience (S2):**
- "Strict validation around tool inputs and outputs, detectors for malformed state, and integration tests that check behavior across steps."
- Guardrail example: "after summarizing, don't re-query unless filters changed."
- Agent "can recognize when its assumptions didn't hold and adjust its approach."

**Conversation memory (S2):** model has no memory across turns → "you have to rebuild that memory yourself … every. single. time." — reconstruct who said what, which tools ran, what data came back; a **translator rewrites it into exactly what the AI backend expects.**

**Token / caching (S2):** "You can't just dump entire result sets into the model context; it's too expensive and breaks **prompt caching**, which we rely on to keep things fast and predictable."

**Security (S2):** "Our AI respects all security protocols and user permissions already defined in Omni, so the agent can only ever run **as the current user**."

**Lessons (S2):**
1. "Text-to-SQL models look cool in a demo, but they rarely make the jump from demo to production."
2. **AI optimism is a risk** — "LLMs are optimistic. Even when you leave out crucial context, they'll still try to help."
3. **Foundations first** — "maniacally focused on quality before we even decided to evolve our AI assistant."
4. **Security non-negotiable.**
5. **Trust over cleverness** — "We chose the hard path because it's the only way to engineer a system that respects your permissions and definitions at every step."

**Model hosting (S-demos):** Omni uses AWS Bedrock-hosted Claude for most tasks (OpenAI only for advanced AI visualizations).

---

## TIER 2 — talk-recap (S5), single-source unless noted

> These details appear in the third-party recap of THIS talk. They are plausible and consistent with T1 but **NOT independently first-party-confirmed** (except the token figure, cross-confirmed by S6). Flag accordingly.

- **Two-loop structure:** outer loop **max 50 iterations** with checkpoint-based recovery; inner loop = parallel tool invocation.
- **45 tools** total portfolio (query gen, dashboard creation, visualization, validation, data modeling). → **Reconciliation:** S2's "4 core tools" = early/core tool *types* (~Aug 2025 architecture post); S5's "45" = matured May-2026 portfolio. Different granularity + time, not a contradiction. **Surfaced, not blended.**
- **"Blobotomy" cycles** — Omni's internal name for major architectural surgeries; recap says **~5** total.
  - **Blobotomy 1 (split-brain):** outer agent planned, separate sub-agent generated queries → knowledge silos (outer knew "what data exists," inner knew "what one query retrieves") → **infinite loops** on cross-boundary tasks → **fix: integrate query generation into the outer harness as a tool, not a separate agent.** Principle: *don't partition knowledge across agent boundaries.*
  - **Blobotomy 2 (SQL over custom format):** dropped a proprietary JSON query format (custom syntax = cognitive load) → **switched to SQL Claude already knows** → **"3–4 attempts per query → 1 attempt."** Claude favors CTEs, which aligned with Omni's parser.
- **Error recovery = highest-ROI lever:** (1) teach the agent recovery strategies, (2) set an execution/retry budget, (3) author **high-quality error messages** ("what happened" + "how to fix") → "dramatic eval-score improvements with minimal prompt changes," outpacing other optimizations.
- **Model migration:** **Haiku → Sonnet (Aug 2025)** because agentic loops need longer context / complex chains exceeded Haiku's envelope.
- **Token economics:** **1.2B tokens/month (Aug 2025) → 103.3B/month (Apr 2026).** (103.3B cross-confirmed by S6.) Sonnet unlocked previously-unanswerable questions → adoption surge → compounding usage.
- **Evals — three pillars:** (1) **LLM-as-Judge** on response correctness; (2) **benchmark-question construction with 8 quality criteria** (evaluability, coverage, realism, difficulty, non-redundancy, discriminative power, semantic clarity, data selectivity); (3) **session triage via Claude Code** — daily analysis of FAILED user sessions, trace-driven root cause **prioritized over aggregate metrics.** Merrick: values **observability over scorecard metrics** — "read raw traces to understand 'why did this fail.'"
- **Org:** **99% of platform code in Claude Code** (also T1 via S1), **~30 engineers**, **18 months** to production.
- **"Toolmakers as primary users":** CTO works in Claude Code daily → first-person harness experience informed Blobby's design.
- **Five engineer-applicable principles (recap's framing):** (1) colocate context with definitions, (2) invest heavily in error messages, (3) avoid sub-agent knowledge fragmentation, (4) use model-native formats, (5) prioritize trace observability.

---

## Open items / could-not-verify

- Verbatim transcript (no captions) — could revisit if Anthropic later publishes captions or a write-up, or with a whisper transcription pass (needs ffmpeg + whisper install).
- T2 numbers (45 tools, 50 iterations, 5 Blobotomies, Haiku→Sonnet date, 8 eval criteria) rest on a single recap. Optional adversarial-Workflow verification pass available (matches the claude-api-cost + prompt-evaluation ship pattern).

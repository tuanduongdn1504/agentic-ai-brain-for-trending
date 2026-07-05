# (C) 2026-07-05 — miai-cv-matching-agent → Pilot Methods Menu

> **Source topic:** `wiki/miai-cv-matching-agent/` (video 7gIwR5SwM_0 + repo thangnch/MiAI_CV_Matching_AI_Agent, 17-agent verified).
> **Consumer context:** hireui/TalentAxis recruitment SaaS (`/Users/Cvtot/monorepo/hireui`, Goal #2 target, **zero LLM integration today**, Anthropic as production vendor per existing cost-optimization spec, Mosh-thread A2 vendor seam already specced). This is the corpus' first source whose *subject matter* IS hireui's domain.
> **Rule:** repo has NO license — port patterns, never copy files. All prices/limits below verified 2026-07-05; regulatory dates are date-sensitive.

---

## A. hireui Goal #2 — the matching feature itself (HEADLINE track)

**A1 — Spec "Match Explain" as hireui's first LLM feature (HEADLINE).**
The demo, translated to hireui's reality: recruiter opens a job (or candidate) → service returns top candidates (or jobs) **with explanation** — strengths, gaps, improvement notes. Claude-stack per [[claude-stack-port]]: `claude-haiku-4-5` + GA structured outputs (`output_config.format` / `messages.parse`) + CV as native `document` block. Write it as a spec first (build-it-right per the hireui-no-LLM-yet memory), eval-first per ai-engineering. ~half-day spec, composes with everything below.

**A2 — Route it through the Mosh A2 vendor seam.**
Don't wire Claude calls into controllers. The matching service is the second consumer (after the A1 candidate-feedback summarizer from the Mosh thread) behind the same repository/service/controller LLM-client seam — one place for keys, retries, model tiering, caching, logging. If the Mosh-pilot seam isn't built yet, this feature is the forcing function to build it.

**A3 — v1 WITHOUT a vector database.**
The demo's biggest simplification opportunity (verified insight): hireui owns both CVs and JDs, and a tenant's open-job count is tens, not thousands. v1 = SQL-filter tenant's open JDs → one **prompt-cached** context block (≥4,096 tokens to clear Haiku's cache minimum) → Claude judges + explains. No Chroma, no embeddings, no infra. Earn retrieval infrastructure only when JD counts outgrow the cache budget.

**A4 — Scores are assistive, not decisional (design rule).**
Verified: the demo's 0–100 is LLM-invented, uncalibrated, position-biased. hireui rule: show **retrieval rank + reasoning + strengths/gaps**, never a bare auto-score that filters people — that keeps the feature out of the AEDT auto-decision category and is the better product ([[recruitment-ai-regulatory-context]], [[matching-quality-vs-production]]).

**A5 — Defensive output schema in Zod.**
Port the alias-normalization pattern ([[defensive-output-schema]]) to hireui's TS services: Zod schema + `.transform()` alias map (reason/explanation→reasoning) + list→string coercion + bounds. Keep it even though Claude structured outputs are schema-enforced — it's the vendor-portability and fallback insurance. ~1h.

**A6 — Serve the validated object (anti-pattern guard).**
The demo's sharpest lesson: it built a validation layer and then streamed the raw model text past it. hireui rule: SSE streams *progress events*; the final payload is the **parsed, validated object** (`messages.parse` result), never raw model text the frontend re-parses. Cheap code-review checklist item forever.

**A7 — SSE progress UX for agent features.**
Steal the event mapping (received → searching → found, analyzing → done) for hireui's matching UI. Claude streaming events map 1:1. Small, high-perceived-value.

**A8 — PII gate before any CV leaves the building.**
The demo posts full CVs to a third-party API silently. hireui pre-flight: consent flow + DPA check (VN PDPL Law 91/2025 is consent-first, effective 2026-01-01), size/MIME limits enforced server-side, optional redaction of contact details before the API call, and candidate-facing disclosure. Compose with the data-residency ADR from the agent-memory thread.

**A9 — Audit logging as a feature requirement.**
Verified gap in the demo: zero logging of inputs/scores/decisions. For an employment tool this is a legal requirement (LL144 audits), not observability polish: log prompt-version, model, inputs hash, output, latency, cost per match run. Feeds A/B evals (B1) for free.

**A10 — Tier the models.**
Haiku 4.5 ($1/$5) for match+explain; Sonnet-tier only for a premium "deep analysis" action. Batch API (50%, mostly <1h) for nightly re-match jobs; prompt caching on the JD block (0.1× reads). Verified math: ~$0.005–0.01/candidate — cost is a non-issue at hireui's scale, so optimize for quality first (see B1).

## B. Evaluation + compliance track

**B1 — Recruiter-labeled eval set before shipping (the moat).**
The demo's author says on camera he never checked accuracy. hireui sits on the gold data the literature says matters: recruiter shortlist/reject decisions. Start with ~100 labeled (JD, CV, decision) triples from historical data → eval in the existing `evals/` harness (prompt-evaluation thread; A1 anchor-validation gate already shipped — don't rebuild). Gate the A1 feature on beating a keyword-baseline.

**B2 — Position-bias check as a cheap eval.**
Verified failure mode (arXiv 2604.03642): shuffle candidate order in context, re-run, measure ranking stability. One eval script; if instability is material, that's your argument for a reranker (B3) or pairwise judging.

**B3 — Reranker upgrade path (deferred until data says so).**
When JD/candidate counts outgrow A3: Voyage `voyage-4-lite` embeddings + `rerank-2.5` (same vendor family Anthropic's docs recommend) or open-weight `voyage-4-nano`/bge locally. Enter only with B1's eval set in hand — the dive's "4h / +20–30%" numbers were stripped as unverified; measure your own.

**B4 — Calibration once outcomes accumulate.**
Map raw scores → interview/hire probabilities via isotonic regression on hireui's own outcome data. Until then: no numeric score in the UI (A4).

**B5 — Regulatory pre-flight one-pager.**
Table from [[recruitment-ai-regulatory-context]] → an ADR in hireui: which markets (NYC LL144 now, IL now, EU 2027-12, CO 2027-01, VN PDPL now), what design keeps the feature assistive, what an audit would need (A9). ~1–2h, prevents an expensive retrofit.

## C. Harness / engineering patterns (any project, personal Claude Code workflow)

**C1 — "Which object reaches the wire?" review question.**
Generalize A6 into your code-review skill/checklist: for every structured-output feature, trace schema → serving path → client parse. The demo failed exactly there despite good components.

**C2 — Contract-gap grep for pipelines.**
The job_id lesson: every schema field must be *produced* upstream, not just demanded downstream — LLMs paper over gaps silently instead of crashing. When reviewing agent pipelines, diff tool-output fields vs schema-required fields.

**C3 — robots.txt + enforcement double-check before any scraping task.**
Verified: robots-disallowed ≠ blocked ≠ licensed (Google allows technically/forbids formally; ITviec the reverse). Add to the vault's block-handling discipline: check robots.txt FIRST, then probe, then decide — "curl returns 200" is not permission.

**C4 — Blueprint-before-code as a prompting discipline.**
The author's pedagogy (architecture map → smallest unit → smoke-test each layer → UI last) is grill-me/plan-mode in disguise. Reuse his build order (format → tool → agent → backend → frontend) as the default plan skeleton for any agent feature.

**C5 — Smallest-real-agent reference implementation.**
Keep the demo's shape (1 LLM + 1 tool + 1 schema + SSE) as the complexity baseline: if a proposed agent design can't justify more than that, don't build more than that. Pairs with the multi-agent-orchestration thread's "start single-agent" guidance.

## D. Vault / autopilot-research methods

**D1 — Mì AI as a recurring VN first-party source.**
Senior banking-IT practitioner, 77 repo-per-video artifacts, ~60K community — a reliable transcript+repo provenance chain. Queue candidates: his LangGraph video (9Mv7jQxGyEY) and vector-DB explainer (fLMm57wvBA0) — both existence-verified. Also a Pattern-#55 VN-cohort data point for Storm Bear (banking-professional educator subtype).

**D2 — Repo-as-ground-truth for VN caption garble (codify).**
This ship resolved every garbled tech term ("lang trên", "mini 4o") against the repo instead of guessing. For any code-walkthrough video: fetch the repo FIRST, read transcript SECOND. Worth a line in the yt-pipeline skill.

**D3 — Skill-inside-workflow-agent hazard (routine note).**
The claude-stack agent died loading the large claude-api skill inside a workflow subagent ("Prompt is too long"). Rule: big reference skills belong in the main loop; workflow agents get distilled facts or doc URLs. Add to the routine's workflow-authoring notes.

## E. Scrum-coaching / teaching methods

**E1 — Teaching artifact for VN junior devs.**
A native-Vietnamese, senior-authored, honest ("chém gió" disclosure included) walkthrough of a complete agent system — better onboarding material for VN teams than translated English tutorials. Pair the video with this wiki's [[code-audit]] as the "spot the production gaps" exercise.

**E2 — Demo-honesty norm for sprint reviews.**
The author's explicit lab-vs-production framing ("làm lab thì rất dễ...") is the norm to import: every AI-feature demo states which parts are demo-grade (his: CORS, wipe, Streamlit, accuracy) — prevents stakeholders shipping a prototype.

**E3 — "The score is an opinion" stakeholder briefing.**
Use [[matching-quality-vs-production]] to set expectations with recruitment-product stakeholders: LLM scores are narrative, not measurement, until calibrated — and that's fine if the product is explanation-first.

---

## Skip list (considered, rejected)

- **Crawling VN job boards** — confirmed Cloudflare-hostile, robots/ToS risk, and hireui doesn't need it (owns its JDs).
- **Copying repo code into hireui** — no license; patterns only.
- **Self-hosted embeddings for cost** — verified negative ROI (~2,000:1) at any realistic hireui scale.
- **Standing up Chroma/vector infra in v1** — A3 makes it unnecessary; revisit at scale with B3.
- **LangChain adoption in hireui** — for 1 tool + 1 schema the Anthropic SDK loop is smaller; hireui's BMAD harness doesn't need a second framework.
- **Auto-reject/auto-rank product mode** — regulatory class jump (AEDT); explanation-first only until counsel + audits say otherwise.

## Critic reframe (steelman of doing less)

The minimal honest pilot is **A1+A2+B1 only**: spec the match-explain service behind the vendor seam and build the recruiter-labeled eval set. Everything else (A3–A10) falls out of the spec naturally, and B1 is the only step that produces evidence instead of architecture. If two weeks from now there's a spec + 100 labeled pairs + a baseline eval score, this topic converted; if there are ten half-built patterns, it didn't. Guard the failure mode the vault already knows: **8 ranked pilots accumulated, 0 deployed** — this is the first pilot where the knowledge and the product are the same domain, so deploy THIS one.

## Suggested next action

Start A1+A2 in hireui (on an `agent/<slug>` branch off `agent-dev`, per its CONSTITUTION I-2): draft the Match-Explain spec referencing [[claude-stack-port]] + B5's regulatory one-pager, then pull ~100 historical recruiter decisions for B1. Vault side: consider queueing Mì AI's LangGraph video (D1) as a follow-up ingest.

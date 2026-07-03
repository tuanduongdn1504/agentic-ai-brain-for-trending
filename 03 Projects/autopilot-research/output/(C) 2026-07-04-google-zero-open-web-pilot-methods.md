# (C) Pilot Methods — google-zero-open-web → your working flow

> **Source topic:** `wiki/google-zero-open-web/` (compiled 2026-07-04; 38-agent verified)
> **Your flow, as this menu maps it:** hireui (Goal #2 real-software target; no LLM yet; Candidate-Detail refactor running; first-LLM-feature thread = Mosh vendor-seam + memory-layer + voice-screener specs) · the two vaults (autopilot-research + Storm Bear LLM Wiki) · personal Claude Code harness · Scrum coaching practice.
> **What this topic uniquely adds:** every previous topic taught you how to *build with AI*; this one documents the **distribution environment your output ships into** — and hands you the measured anti-pattern (1% citation clicks) to avoid in the features you're about to build.

---

## A — hireui: acquisition resilience (Goal #2's marketing flank)

**A1. Google-Zero exposure audit (THE HEADLINE — zero install, ~1-2h).**
Pull hireui/TalentAxis analytics (GA4 or server logs): what % of signups/leads originate from Google organic? Segment branded vs non-branded queries. Then score each acquisition channel with the SparkToro lens: organic informational content (full exposure — AI Overviews eat it), product/transactional queries (low exposure — SISTRIX shows transactional barely affected), direct/brand (safe), community/referral (safe). Deliverable: a one-page "what's our Google Zero?" memo with the % of pipeline that dies if organic clicks halve again (they fell 360→276/1,000 in two years). This is the baseline every other A-method needs.

**A2. GEO pass: become the cited answer, not the buried link (~half-day).**
Google's answer machine cites Wikipedia/YouTube/Reddit/.gov disproportionately (Pew), but *product* queries still resolve to product pages. For hireui's marketing site: (a) FAQ/HowTo structured data on the recruiting-workflow content; (b) statistics-with-sources content blocks (AI Overviews preferentially cite pages with citable numbers); (c) an `llms.txt` at the site root; (d) clean semantic HTML headings that summarizers can lift. Measure via A6. This is Generative Engine Optimization — optimizing to be *quoted*, since being *visited* is decaying.

**A3. JobPosting schema audit (recruitment-specific — the already-lost battle worth winning).**
Google for Jobs is the answer machine that already ate job boards — a decade before AI Overviews. If hireui hosts/publishes client job listings, verify every listing emits valid `JobPosting` structured data so it surfaces in the Google Jobs box. This is the one Google surface where feeding the machine directly converts (candidates click through to apply). Rich-results test + a CI check on the schema.

**A4. Declare AI-crawl licensing terms — RSL in robots.txt (~1h, standards-based).**
Adopt the RSL vocabulary on hireui's public content: declare terms (e.g., attribution-required for AI reuse; block training on client job content). Today it's mostly signaling; but it's a free option on the future RSL Collective royalty pool (1,500+ publishers incl. Reddit/AP already in), and it forces the deliberate decision A5 documents. rslstandard.org has the robots.txt/HTTP-header syntax.

**A5. AI-crawler policy ADR (~1h, decision artifact).**
Decide crawler-by-crawler: GPTBot, ClaudeBot, Google-Extended (Gemini training), PerplexityBot, CCBot. The trade Reddit monetized and HouseFresh couldn't: training-access vs traffic vs invisibility-in-AI-answers. For a SaaS, being *cited* by assistants recruiters ask ("what ATS should we use?") is arguably worth more than blocking. Write it as an ADR in hireui's decision log (brain-setup lazy-ADR pattern) — the point is deliberateness, either way.

**A6. AI-referral measurement (composes with your OTel/observability pilot).**
Instrument hireui analytics to segment: referrals from chatgpt.com/perplexity.ai/gemini/claude.ai; Search Console AI-Overview impressions where available; UA-string crawler hits (which AI bots read you how often). Baseline number to beat: AI chatbots deliver 0.29% of web referrals globally (Cloudflare Radar) — measure whether *your* niche does better before investing further in A2. Dashboard panel next to the cost dashboard from the OTel pilot.

**A7. First-party audience insurance (strategic, ongoing).**
The verified survival play (HouseFresh, DCN playbook): channels Google can't repossess — recruiter newsletter, LinkedIn presence, a community (see A8), direct/brand. Concretely: add an email-capture artifact (salary-benchmark report, hiring-checklist) to the highest-organic-traffic hireui pages, converting doomed rented traffic into owned audience while it still arrives.

**A8. Community-content strategy (forum boost, used ethically).**
Forums outrank experts for many query classes since fall 2023 (Hidden Gems + HCU; +1,328% Reddit). hireui's expertise (recruiting workflows, ATS selection) should show up where rankings now live: genuine participation in r/recruiting-class communities, not astroturf. Caveat from the wiki: the boost partially decayed by 2026 (Reddit #2→#4) — treat as a channel, not a strategy.

## B — hireui: product design (Goal #2's build flank — the anti-pattern lesson)

**B1. The citation-forward design rule for hireui's first LLM feature (THE PRODUCT HEADLINE — spec-level, composes with the Mosh/memory/eval threads).**
Google's AI Overviews are the world's largest RAG-with-citations deployment, and Pew measured its citation UX: **1% click-through, 3+ sources blurred into footnotes, sessions ending 26% vs 16%**. When you build the candidate-feedback summarizer (Mosh thread) or any candidate-Q&A surface: (a) every claim deep-links to the specific interview note/CV section it came from; (b) sources render as the *primary interaction* (tap-to-expand quote previews), not a footnote pile; (c) log citation-clicks as a first-class metric with a target (>15%, i.e., 15× Google's number — recruiters must verify sources before acting on candidate claims, so your UX must make verification the default path, not the 1% path). Write this into the feature spec now, before code exists.

**B2. Answer-liability guard (the German-ruling lesson).**
The June 2026 German ruling: AI answers are the *product's own speech* — hallucination = legal exposure. For a recruitment product summarizing *people*, this is sharper (employment decisions, discrimination risk). Spec requirement alongside B1: no unsourced assertion about a candidate is ever rendered; ungrounded model output is visually distinguished or suppressed; a human-review affordance on anything decision-relevant. This slots into the eval harness (prompt-evaluation thread) as a groundedness eval.

**B3. "Don't starve your sources" as an internal API principle.**
Google's paradox (snake eating its tail): the answer machine starves the corpus it feeds on. hireui's version: if the LLM layer answers everything about a candidate, nobody opens the full profile, and profile-completeness (the corpus) decays. Design the answer surface to *route into* the profile (B1's deep links double as this), and watch profile-view metrics after launch as the canary.

## C — the vaults (your knowledge system as Google-Zero insurance)

**C1. Name the discipline: the LLM Wiki is your personal anti-answer-machine (~30min codification).**
The vault already does what the open web is losing: primary-source pinning (URLs + key numbers stored locally), adversarial verification, provenance chains. Codify "primary-source pinning" as an explicit rule in the autopilot CLAUDE.md compile step: every load-bearing claim stores (number + date + source URL + panel/methodology) so the wiki survives link-rot and answer-machine paywalling. Mostly formalizing current practice — cheap, durable.

**C2. Source-mortality lint (~1h to add to audit verb).**
The open web is shrinking under the wiki's feet. Add to the `audit` routine: sweep load-bearing external URLs across `wiki/*/`, flag dead links, add archive.org snapshot links for the top-N critical primaries (SparkToro/Pew/SISTRIX class). First run will calibrate how fast your citation base rots.

**C3. RSS-first ingestion path (the resistance tech, used for intake).**
RSL is built on RSS lineage for a reason — feeds are the un-intermediated channel. Add an RSS shortlist to the autopilot project (SparkToro blog, Pew internet/tech, Press Gazette platform desk, SISTRIX blog, key first-party engineering blogs) as a `raw/feeds.md` seed list the routine can drain — topic discovery that doesn't route through Google or YouTube recommendation.

**C4. Queue the sibling topic.**
Add `TODO: youtube:4WyduoGpIPo — TIS "You NEED to STOP Using Google Right Now" (AI-slop sibling)` to `raw/topics-queue.md`. It's the same script team's AI-slop chapter expanded — closes the one teased-but-unverified thread.

**C5. The pipeline's own exposure memo (think-piece, 30min).**
This research system feeds on YouTube transcripts + the open web — the exact corpus the topic says is shrinking and enclosing (Reddit lockdown = your yt-dlp/WebFetch access is a revocable privilege, already visible as 429s this session). One-pager in `output/`: which ingest paths depend on whose forbearance; what the Tier-escalation skill does when enclosure spreads; whether NotebookLM/yt-dlp paths need fallbacks. This is the harness-engineering angle on the topic.

## D — Scrum coaching / team practice (your other hat)

**D1. The "what's your Google Zero?" platform-risk retro (ready-to-run workshop).**
The HouseFresh case is a complete, primary-sourced, 20-minute case study: dependency → update → −91% → diversify-or-die. Run it as a risk retro with any product team: map every channel/platform dependency (search, app stores, LinkedIn API, a cloud vendor, one big client), ask "which single external decision halves our pipeline?", leave with one diversification action each. The wiki article is the handout.

**D2. Innovator's-dilemma live case for product strategy sessions.**
Google's arc (code red → become the chatbot → eat your own business model → $4.3T anyway) is the best current-events Christensen case: disrupt yourself vs protect the toll booth. Pairs with the antitrust article for the "what would you have done as Google PM in Dec 2022?" exercise.

**D3. Vendor-claim vs measurement literacy drill.**
Liz Reid's "clicks are stable" post (zero data) vs Pew/Chartbeat/SISTRIX (panel/telemetry data) is a clean teaching pair for evidence literacy in teams — the same muscle as "tests pass" vs "it works" (Rule 12). Ten-minute segment in a coaching session.

## E — personal practice / verification discipline

**E1. Bank the misfire-free run (meta, 15min).**
This was the corpus's first ZERO-verifier-misfire big run — because all sources were mainstream-web, inside every agent's reach. Confirms the misfire ledger's pattern: verifier misfires cluster on gh-api/niche/post-cutoff sources. Practical rule to bank: calibrate refuter-count to source obscurity, not claim importance (mainstream claims need 1 refuter; niche-repo claims need ground-truth fetches).

**E2. The 4 corrections as citation hygiene reflexes.**
All four video errors are secondhand-compression classes you'll meet everywhere: conflated rankings ("#2 by which metric?"), derived-numbers-reported-as-reports ("$70M per whom?"), timeline compression ("which update, exactly?"), stale magnitudes ("$2T as of when?"). When quoting any stat into hireui docs or the vault: attach metric + source + date. You already do this in the wiki; extend it to product/marketing copy.

**E3. Diversify your own search behavior (personal, zero-cost).**
You're both victim and beneficiary of the answer machine. Deliberate split for a week: product/code lookups → AI (where you already live); anything you might *cite* → primary source through the wiki pipeline. Notice where AI answers would have quietly fed you the "$70M reported" class of error.

---

## Ranked shortlist (if you only do three)

1. **A1 exposure audit** (~1-2h, zero install) — the baseline number Goal #2's marketing flank needs; everything else in section A is unprioritizable without it.
2. **B1 citation-forward design rule** (spec-level) — the one lesson that must land *before* hireui's first LLM feature is built; it converts this topic's biggest measured fact (1% citation clicks) into a product requirement. Composes directly with the Mosh vendor-seam + memory-layer + eval pilots already specced.
3. **C1+C2 vault codification + source-mortality lint** (~1.5h) — cheapest durable win; makes the vault's Google-Zero insurance explicit and rot-resistant.

## Skip list (deliberately not piloting)

- **Paid GEO tooling / rank trackers** — hireui's organic footprint doesn't justify the spend before A1 says otherwise.
- **Cloudflare Pay-Per-Crawl** — hireui isn't a content publisher; crawl revenue is a rounding error. Revisit only if content marketing scales.
- **De-Googling infrastructure** (search ads, Workspace, Analytics alternatives) — activism, not workflow improvement; out of scope.
- **Building on the Reddit/forum boost as a growth strategy** — the boost already decayed (#2→#4 by Mar 2026); channel yes, strategy no.
- **Model-collapse-driven decisions** — production collapse is unproven (Schaeffer); don't architect around it, just keep the vault's curation discipline.

## Critic reframe (the strongest argument against this whole menu)

hireui is a B2B SaaS whose pipeline probably runs on relationships, LinkedIn, and referrals — not blog SEO. If A1 shows organic <10% of pipeline, then sections A2-A8 are publisher problems you don't have, and this topic's real value to you collapses to exactly two things: **B1/B2 (design the LLM feature so its citations get clicked and its answers don't create liability)** and **D1 (the platform-risk retro as a coaching asset)**. That would still justify the ingest — but run A1 *first* precisely so the menu can shrink honestly.

## Suggested next action

Run A1 this week (needs only analytics access + the wiki's channel-exposure rubric). Its output decides whether the A-section survives the critic reframe — and B1 goes into the first-LLM-feature spec regardless, next time that thread advances.

# Ben AI's 8 Meta-Skills: Ranked Pilot Methods for Storm Bear

> **Source:** Ben AI — "8 Claude Skills I Can't Live Without" (YouTube bXnRA3pJavE, 2026-04-18, ~20 min, 147K views).
> **Originals cited:** Matt Pocock (Process Interviewer), Anthropic prompt-engineering best practices (Prompt Master), Wikipedia Signs of AI writing (Humanizer), Farnam Street mental models (Decision Toolkit), Vercel skills.sh ecosystem (Find Skills), Edward Tufte (Front-End Slides), Anthropic MCP Builder, web-cross-reference systems (Fact Checker).
> **Date:** 2026-06-20. **Operator:** Storm Bear (Karpathy-style LLM Wiki maintainer + Scrum coach + hireui Goal #2 pilot target).
> **Verification:** drafted + adversarially checked via Workflow `wf_884737d0-afa`; key correction — `mcp-builder` IS a real official Anthropic skill (Ben's #8 holds). Full ledger: [source-provenance](../wiki/claude-skills/source-provenance.md).
> **Companion wiki:** [claude-skills topic](../wiki/claude-skills/_index.md) (10 articles).

---

## Headline Insight

You are the exact target user. You already run TWO second-brain vaults (fast-cadence autopilot-research wiki + curated Storm Bear vault) PLUS a disciplined personal ~/.claude operational memory (L1 + manual L2). These meta-skills compound with your existing setup; they don't rescue a missing one. Skill #1 (Process Interviewer) is particularly relevant: you've already cross-ported Matt Pocock's grill-me as "brain-setup pattern v2" (4-phase interview). The pilot is to formalize it as a reusable skill for skill-building itself.

---

## ▶ Start Here (3-Step Sequence)

1. **Week 1 — Humanizer (Flow C) + Fact Checker (Flow B) Chain** — Apply Humanizer to next (C)-prefixed wiki file before commit. Wire Fact Checker into `bin/autopilot-drain.py` as final compile step. Measure: AI-writing tells detected by Humanizer; unverifiable-claims count from Fact Checker.

2. **Week 2 — Process Interviewer (Flow B) for Autopilot Skill + MCP Builder (Flow D) for hireui ATS** — Formalize pending autopilot skill (yt-search or notebooklm) with Process Interviewer. Extract hireui ATS API docs; feed to MCP Builder. Measure: skill PRD completeness; MCP server sandbox test success.

3. **Week 3 — Decision Toolkit (Flow C) for v66 Audit + Process Interviewer (Flow C) for Routine v2.2** — Frame v66 decisions (Pattern #21 promotion, Pattern #51 reformulation) as toolkit scenarios. Frame "how should routine v2.2 formalize skill-authoring?" as interviewer question. Measure: audit decisions documented with visible reasoning; routine v2.2 framework completed.

---

## Ranked Methods Table

| Rank | Method | Flow | Effort | Value | First Step | Success Signal |
|------|--------|------|--------|-------|-----------|-----------------|
| 1 | **Humanizer as (C)-File Gate** | C | Low | High | Run next wiki file through Humanizer; check for Wikipedia's 8 AI tells | Zero documented AI-writing markers remain; output reads as your voice |
| 2 | **Fact Checker in autopilot-drain.py** | B | Med | High | Modify drain.py to chain Fact Checker before `.md` output; append verification report | Report shows true/mostly-true/unverifiable/false counts; zero silent unverifiable claims |
| 3 | **Decision Toolkit for v66 Mini-Audit Decisions** | C | Med | High | Frame v66 decisions (Pattern #21, #51, active-candidate threshold) as toolkit scenarios | Audit decisions documented with visible reasoning (bias checks + opportunity-cost explicit) |
| 4 | **MCP Builder: hireui ATS Connector** | D | Med | High | Extract hireui ATS API docs; feed to MCP Builder; output server code + config | MCP server in `hireui/_bmad-output/mcp-servers/`; sandbox test passes |
| 5 | **Process Interviewer for Routine v2.2 Framework** | C | High | High | Frame: "How should routine v2.2 formalize skill-authoring?" Run through interviewer | PRD embeds best practices; 10–15 clarifying questions resolved; codification agenda crystallized |
| 6 | **Front-End Slides: Scrum Coaching Decks** | E | Low | High | Auto-generate 5-slide deck from Chess Moves (e.g., "4 Types of Technical Debt"); feed brand guide | Presentation ready to share in coaching session; visual hierarchy clear |
| 7 | **Fact Checker: hireui Cost-Optimization Spec** | D | Med | High | Run hireui cost spec through Fact Checker; verify pricing + caching-discount math | Spec updated with current Anthropic pricing; no outdated claims ship |
| 8 | **Process Interviewer for Autopilot Skill Formalization** | B | High | High | Pick fuzzy autopilot skill (yt-search, notebooklm); run through interviewer; document PRD | Skill PRD includes clear description, examples, edge cases, triggers; ready to ship |
| 9 | **Decision Toolkit: hireui Feature Prioritization (Agent Features)** | D | High | High | Frame 3 agent options (screening, scheduling, offer-automation) as scenarios; populate toolkit | Expected-value matrix generated; feature ranking justified with bias checks visible |
| 10 | **Process Interviewer: hireui Recruitment-Agent Workflow** | D | High | High | Frame: "What should the recruitment agent do, step-by-step?" Run through interviewer | Workflow diagram + PRD + clarifying questions resolved; ready for engineering spec |
| 11 | **Prompt Master: Routine v2.2 Codification Candidates** | C | High | High | Extract 14 unstructured v61 candidates; batch-feed to Prompt Master; output PRDs | 14 candidates pre-screened + formatted per Anthropic best practices; v2.2 agenda crystallized |
| 12 | **MCP Builder: Slack + Circle.so Connectors** | D | Med | High | Extract Slack API + Circle API docs separately; generate dual MCP servers | Two MCP servers generated + tested; hireui agent can post summaries + query community |
| 13 | **Humanizer: hireui Candidate Communications** | D | Low | Med | Run auto-generated candidate emails (rejections, offers, feedback) through Humanizer | Emails read as written by recruiter, not system; no AI tells; candidate experience improves |
| 14 | **Find Skills: Autopilot Pipeline Tooling (Vetted)** | B | Med | Med | Search skills.sh for "youtube metadata", "knowledge graph", "wiki synthesis"; vet top 3 via code review | Document 3 vetted candidates + security notes in `autopilot-tooling-candidates.md` |
| 15 | **Decision Toolkit: cc-sdd vs free-claude-code Pilot Sequencing** | C | Med | Med | Frame: sequential A→B vs B→A vs parallel? Populate toolkit with time/resource/evidence goals | Expected-value matrix informs v66 planning + Goal #2 progress |
| 16 | **Front-End Slides: Pattern Library Architecture Onboarding** | C | Low | Med | Auto-generate slide deck: Pattern Library state hierarchy + N-count dynamics + promotion criteria | Animated presentation suitable for new vault contributors; no 122KB chapter-read required |
| 17 | **Fact Checker: Multi-Agent Orchestration Design** | D | Med | Med | Run hireui multi-agent design (from autopilot topic) through Fact Checker; verify capability claims | Design includes fact-checker report; unverifiable claims marked [unverified] with source |
| 18 | **Humanizer + Fact Checker: CLAUDE.md Rule Enforcement** | C | Med | Med | Chain both skills on next 3 wiki sessions; flag violations of Rule 1 (Think), Rule 5 (Use model), Rule 12 (Fail Loud) | Next 3 sessions gate on verification report; zero rule violations pass uncaught |
| 19 | **Front-End Slides: hireui Pilot Write-Up** | D | Low | Med | Convert hireui findings + runbooks to animated slide deck; feed hireui brand guide | Presentation ready for TalentAxis stakeholder review; visual hierarchy clear |
| 20 | **Humanizer: LinkedIn + Scrum Comms** | E | Low | Med | Batch-apply Humanizer to pending LinkedIn posts + retrospective notes | Posts read as your authentic voice; no AI markers; engagement improves |
| 21 | **Decision Toolkit: Cowork vs Code vs Agent-SDK Deployment** | D | High | Med | Frame: Claude Code (dev) vs Agent SDK (prod) vs Cowork (collab)? Populate with cost + access + capability | Platform-choice matrix generated; tradeoffs visible; decision documented |
| 22 | **MCP Builder: Autopilot Source Connectors (HN/Substack/YouTube)** | B | High | Med | Identify 1–2 missing source connectors; extract API docs; generate MCP servers | New connectors integrated into `autopilot-drain.py`; data ingest working |

---

## Detailed Methods by Flow

### **Flow A: Personal ~/.claude Memory (L1 + Manual L2)**

**A1. Humanizer on Personal Notes** — Run session reflections through Humanizer. Check for Wikipedia tells: undue emphasis ("uniquely innovative"), promotional verbs ("unlock", "empower"), vague attribution ("industry reports"), hedging ("arguably"). Success: notes read as authentic Storm Bear voice with zero flagged tells.

**A2. Decision Toolkit for Personal Alignment** — Frame a pending decision (e.g., "pilot cc-sdd now or wait?"). Populate: decision frame, scenarios, time horizon, who's affected, regret-minimization test. Success: toolkit outputs decision matrix; you review frame (not recommendation) and decide with more clarity.

---

### **Flow B: Autopilot-Research Vault (Fast-Cadence Wiki + bin/autopilot-drain.py + /loop /schedule)**

**B1. Process Interviewer for Autopilot Skill Formalization** — Pick fuzzy autopilot skill (yt-search, notebooklm, etc.). Invoke `/process-interviewer`. Let it ask: what does it do, when triggers, success metrics, edge cases, chaining. Success: PRD embeds Anthropic best practices (clear description, examples, edge cases, error handling); PRD lives in `skills/` directory.

**B2. Fact Checker in autopilot-drain.py** — Modify drain.py to chain Fact Checker as final compile step. Before writing `.md`, run summary through Fact Checker. Append verification report (true/mostly-true/unverifiable/false counts). Success: every autopilot output includes verification report; zero unverifiable claims ship.

**B3. Prompt Master Auto-Run on Unstructured Brain-Dumps** — Add folder instruction: when you end a note with "[OPTIMIZE THIS PROMPT]", Prompt Master auto-runs. Outputs: structured brief with task, examples, context, constraints, role, success criteria. Success: brain-dumps → structured briefs without manual rewriting; time saved measurable.

**B4. Find Skills: Autopilot Tooling (Vetted Selection)** — Search skills.sh for "youtube metadata extraction", "knowledge graph synthesis", "wiki index generator". Vet top 3: check repo age/stars/commits, read SKILL.md for hardcoded secrets, check install count + reviews. Success: document 3 vetted candidates + vetting notes in `autopilot-tooling-candidates.md`; flag security concerns.

**B5. MCP Builder: Autopilot Source Connectors** — Identify 1–2 missing source APIs (HackerNews, Substack, YouTube transcripts). Extract API docs. Feed to MCP Builder. Outputs: server code + installation instructions. Success: new MCP server configured in `config.json`; next `/loop autopilot` run uses new connector; one source integrated per month.

---

### **Flow C: Storm Bear Curated Vault (Slow-Track LLM Wiki + Pattern Library + Mini-Audits)**

**C1. Humanizer as (C)-File Output Gate** — Before committing any (C)-prefixed wiki file, run through Humanizer. It flags: undue emphasis, promotional language, vague attribution, didactic disclaimers, hedging ("arguably", "one could say"), AI vocabulary ("delve", "pivotal", "landscape"), excessive em-dashes. Success: zero Wikipedia-documented AI tells remain before commit; output reads as Storm Bear voice.

**C2. Fact Checker + Wiki Compile Discipline** — Chain Fact Checker into final-review stage (pre-merge-to-main). Run chapters + pattern entries through Fact Checker. Outputs: verification report (true/mostly-true/unverifiable/false percentages) + evidence gaps. Success: v66 wiki includes fact-checker report for EVERY chapter; zero unverifiable claims pass; Rule 12 (Fail Loud) gains mechanical enforcement.

**C3. Decision Toolkit for Pattern Library Mini-Audits** — Frame v66 decisions as scenarios: (1) Pattern #21 promotion: truly independent? (2) Pattern #51: narrow or expand? (3) Active-candidate threshold: what triggers EXTENDED audit? Populate toolkit with scenarios, time horizons, stakeholder impacts, opportunity costs. Success: audit decisions documented with visible reasoning (not opaque gut-calls); future audits reference framework.

**C4. Prompt Master: Routine v2.2 Codification Candidates** — Extract 14 unstructured v61 candidates from CLAUDE.md. Batch-feed to Prompt Master. Outputs: structured brief + PRD + examples per candidate. Success: 14 candidates pre-screened + formatted + PRD'd; v2.2 codification agenda crystallized per Anthropic best practices.

**C5. Process Interviewer: Routine v2.2 Framework Design** — Frame: "How should Storm Bear formalize skill authoring in routine v2.2?" Run through interviewer. It asks: what problems is v2.2 solving, what's the workflow, entry/exit criteria, edge cases, success metrics, relationship to v2.1? Success: confirmed summary + full routine v2.2 framework PRD + 10–15 clarifying questions resolved; ready for v65–v70 audit ship.

**C6. Front-End Slides: Pattern Library Architecture Onboarding** — Auto-generate slide deck: "Pattern Library Architecture Overview". Feed: state block (42 confirmed, 19 candidates, 1 stale, 9 retired, 7 observation-tracks), N-count dynamics, decision-tree for promotion, mini-audit taxonomy. Success: animated reveal.js presentation ready to show new contributors; governance visible without 122KB chapter-read.

**C7. Humanizer + Fact Checker: CLAUDE.md Rule Enforcement** — Create pre-commit automation running both skills on next 3 wiki sessions. Flag violations of Rule 1 (Think Before), Rule 5 (Use model only for judgment), Rule 12 (Fail Loud). Append verification report to commit message. Success: next 3 sessions automatically gate on combined report; zero rule violations pass uncaught; vault discipline mechanically enforced.

**C8. Decision Toolkit: cc-sdd vs free-claude-code Pilot Sequencing** — Frame: sequential A→B, sequential B→A, or parallel? Populate with scenarios, time horizons (1-week, 3-week, 8-week), resource constraints, Pattern Library evidence goals. Success: expected-value matrix shows which sequencing maximizes learning + minimizes contention; informs v66 planning.

---

### **Flow D: hireui Goal #2 Real-Software Target (TalentAxis SaaS + BMAD Harness + No LLM Integration Yet)**

**D1. MCP Builder: hireui ATS Connector** — Extract hireui's ATS API docs. Feed to MCP Builder. Specify capabilities: read candidate profiles, update interview status, fetch job metadata. Outputs: server code + JSON config. Success: MCP server code in `hireui/_bmad-output/mcp-servers/ats-connector/`; JSON config in `.claude/CLAUDE.md`; sandbox test: Claude agent queries candidate data via MCP.

**D2. MCP Builder: Slack + Circle.so Connectors** — Extract Slack API + Circle API docs. Feed separately to MCP Builder. Outputs: dual MCP servers. Success: hireui's agent can post interview summaries (Slack), fetch team feedback (Slack threads), query community activity (Circle); both configured in `.claude/CLAUDE.md`.

**D3. Decision Toolkit: hireui Feature Prioritization** — Frame multi-agent options: (1) candidate-screening agent, (2) interview-scheduling agent, (3) offer-letter automation. Populate: scenarios, interview-cycle time saved per option, resource cost, who's affected (hiring mgrs/recruiters/candidates), quarterly impact. Success: HTML wizard outputs expected-value matrix + opportunity-cost analysis + bias checks (confirmation bias: "screening most important"); architecture decision made with visible reasoning.

**D4. Process Interviewer: Recruitment-Agent Workflow** — Frame: "What should the recruitment agent do, step-by-step, from candidate application to offer?" Run through interviewer. It asks: what data feeds it, what decisions does it make vs escalate, success metrics, error cases (rejected candidates, offer-drop, competing offers)? Success: confirmed workflow diagram + full PRD + 10–15 clarifying questions resolved; ready for engineering spec + agent-harness design.

**D5. Fact Checker: hireui Cost-Optimization Spec** — Run `hireui/_bmad-output/runbooks/claude-api-cost-optimization-spec-2026-06-15.md` through Fact Checker. Verify: Anthropic pricing claims, API quota assumptions, caching-discount math, token-counting logic. Success: report flags outdated pricing; spec updated with current Anthropic pricing (June 2026) + verified caching discounts + corrected quota assumptions; no outdated claims ship.

**D6. Front-End Slides: hireui Pilot Write-Up** — Convert hireui findings + runbooks from `_bmad-output/` into animated slide deck. Include: problem statement, solution architecture, results (if complete), next steps, cost impact. Feed hireui's brand guide (colors, fonts) for consistency. Success: presentation ready for TalentAxis stakeholder review; visual hierarchy clear; suitable for executive briefing.

**D7. Humanizer: hireui Candidate Communications** — Run auto-generated candidate emails (rejections, offers, interview feedback) through Humanizer before sending. It flags: overly formal tone, vague attribution ("we believe you would be..."), promotional hype ("great fit"), didactic disclaimers. Success: emails read as written by recruiter, not system; no AI markers; candidate experience improves (higher engagement on rejections = lower hard-feelings attrition).

**D8. Decision Toolkit: Deployment Platform Choice (Cowork vs Code vs Agent SDK)** — Frame: Claude Code (dev), Claude API Agent SDK (prod), Claude Cowork (collaborative — a real Anthropic product)? Populate: cloud-cost per option, team-access model, capability-parity, time-to-deployment, operational overhead. Success: platform-choice matrix + cost estimates generated; tradeoffs (faster value vs simplicity vs team scaling) visible; decision documented with regret-minimization check.

**D9. Fact Checker: Multi-Agent Orchestration Design** — Run hireui's multi-agent design (from autopilot-research topic) through Fact Checker. Verify: agent-framework assumptions (e.g., "Claude Agent SDK scales to N parallel agents"), LLM capability claims, cost projections. Success: design document includes fact-checker report; unverifiable claims marked [unverified] with source; engineering team has clean spec without hidden assumptions.

---

### **Flow E: Scrum Coaching / Teaching Teams**

**E1. Front-End Slides: Scrum Coaching Decks** — Auto-generate 5-slide presentation from Chess Moves material (e.g., "The 4 Types of Technical Debt", "Psychological Safety in Retros", "How to Read a Burndown"). Specify brand preferences. Success: animated HTML ready to share in coaching session; visual hierarchy clear (key concepts prominent, examples secondary).

**E2. Humanizer: LinkedIn + Scrum Comms** — Batch-apply Humanizer to pending LinkedIn posts + retrospective notes. It flags: hedging ("arguably", "one could say"), hype ("revolutionized", "unlock"), didactic tone, undue emphasis. Success: posts/comms read as your authentic voice; no AI markers; engagement improves (colleagues: "this sounds like Storm Bear").

**E3. Decision Toolkit: Team Leadership Decisions** — Frame a team decision (e.g., "adopt Agent Skills for production work?", "pilot cc-sdd on next sprint?"). Populate: scenarios, who's affected, opportunity costs, time horizon, confirmation biases to watch for. Success: toolkit generates decision matrix + bias-check report; when presenting to team, show reasoning transparently ("here's what we considered, here's the blind spot"); team confidence increases.

**E4. Front-End Slides: Team Architecture Presentations** — Convert team architecture doc/RFC into animated presentation for all-hands or architecture review (e.g., "hireui Agent Architecture", "Autopilot Vault Routing", "Pattern Library Governance"). Success: architecture clarity improves; team can share slides internally (vs reading 20-page RFC); faster onboarding.

**E5. Prompt Master: Coaching Interview Questions** — Batch your hand-written coaching prompts (retrospective questions, 1-on-1 guides). Feed through Prompt Master. Outputs: structured interview brief + examples + guidelines. Success: coaching interviews become consistent; new coaches use structured prompts; outcomes more comparable (same questions → better pattern-matching).

---

## What to Consciously SKIP (and Why)

**Don't install dozens of skills.sh skills into your vault harness.** Snyk security audit (Feb 2026) found 36.82% of skills.sh catalog have security flaws; 13.4% are CRITICAL. Skills execute with shell access + file-system write + credential access. Skill bloat = supply-chain attack surface + prompt-injection vectors. Ben AI's meta-skills are curated from reputable source (exception, not rule). General skills.sh discovery should be gated per B4 vetting discipline.

**Don't blindly auto-apply Humanizer without review.** Humanizer flags AI-writing tells per Wikipedia guide (descriptive heuristic, not prescriptive). False positives exist (legitimate "landscape" as noun ≠ heuristic flag). Rule 3 (Surgical Changes) + Rule 12 (Fail Loud) require YOU to REVIEW before applying. Auto-run chains are fine (flags suggestions); auto-apply without review is drift.

**Don't use Fact Checker as a substitute for rigorous prompt-evaluation discipline.** Fact Checker is a web-cross-reference scanner. Your prompt-evaluation harness (sibling topic) scores grading rubrics (accuracy, completeness, specificity, bias). They're orthogonal. Chain them, don't replace.

**Don't assume MCP Builder outputs production-ready servers.** MCP Builder scaffolds from API docs. Output requires security audit (hardcoded secrets check, external-data validation, error-handling completeness). Treat as templates, not ship-ready. Add to `.claude/CLAUDE.md` only after code review + sandbox test.

**Don't use Decision Toolkit as a recommender.** Toolkit is a framework (guide, not decider). If tempted to let it "decide", you've lost the discipline that makes it valuable (explicit reasoning + stakeholder accountability).

**Don't chain Prompt Master auto-apply without review gates.** Prompt Master optimizes per "best practices" (fuzzy category). Auto-run chains should output to review queue, not directly to production prompts. Rule 3 (Surgical Changes) applies.

**Don't use Process Interviewer for decisions you've already made.** Interviewer asks clarifying questions to surface unstated assumptions. If your mind is closed before running it, you're confirming bias, not discovering clarity. Use it on genuinely fuzzy questions only.

---

## Critic's Reframe

Ben AI positions these as "exponential meta-skills" — universally applicable, especially with a second brain. True on the second brain part. But the packaging is **marketing-first, discipline-second**. Ben monetizes a paid AI Accelerator community; the free skills are the top-of-funnel upsell. The skills are real, but emphasis on "MUCH more powerful with second brain" is designed to make you feel you NEED the full stack.

You don't. You already have the hardest part: multi-vault second brain + operational memory + disciplined prompt-evaluation. These meta-skills are *reinforcement*, not foundation. Humanizer + Fact Checker refine your existing scrutiny. Process Interviewer formalizes grill-me (cross-ported into brain-setup v2). MCP Builder saves hireui boilerplate. Decision Toolkit makes your Chess Moves reasoning visible.

The real win is NOT "eight magical skills" — it's **formalizing your existing disciplined practices as reusable procedures**. That's the compound effect Ben is banking on, and it happens to be true.

---

## Cross-Links to Sibling Wiki Topics

- **[ai-operating-system](../wiki/ai-operating-system/)** — Ben AI's anchor (5-skills-to-build-OS video). Process Interviewer descended from Matt Pocock's grill-me (documented as Pattern Library observation-track). This menu operationalizes that theory.
- **[prompt-evaluation](../wiki/prompt-evaluation/)** — Fact Checker chains into your evaluation harness (A1 anchor-validation gate + 15-method menu). Don't rebuild A1; compose with Fact Checker.
- **[claude-api-cost-optimization](../wiki/claude-api-cost-optimization/)** — Flow D5 applies Fact Checker to cost claims. Free-claude-code v60 pilot (ranking #2) is cost-reduction proxy (orthogonal to cc-sdd v61 methodology harness).
- **[multi-agent-orchestration](../wiki/multi-agent-orchestration/)** — Flow D4 uses Process Interviewer to spec recruitment-agent workflow. Methods B6/B7/B10 from multi-agent menu inform D3 Decision Toolkit feature prioritization.
- **[claude-code-memory-systems](../wiki/claude-code-memory-systems/)** — Memory systems anchor validates your L1+L2 discipline (Connolly/Huryn pattern). Ben's "skills get MUCH more powerful with second brain" validates session 67 vault refactor as load-bearing.
- **[cowork-third-party-inference](../wiki/cowork-third-party-inference/)** — Claude Cowork (the surface Ben demos on) is a real Anthropic product. hireui candidate-PII still needs a data-sovereignty decision (BYOM gateway + local model) before any LLM deployment.
- **[harness-engineering](../wiki/harness-engineering/)** — Agent Skills architecture (progressive disclosure, skill bundling) mirrors your vault's chapter-file refactor (metadata preloaded, full content on-demand, resources on-trigger). Architectural symmetry validates your design patterns.

---

## Suggested Next Action

**This week:** Implement C1 (Humanizer gate for wiki output) + B2 (Fact Checker in autopilot-drain.py). Both low-setup, high-discipline payoff. Run next wiki deliverable + autopilot summary through both. **Report:** AI-writing tells detected? Unverifiable claims flagged?

**Week 2:** Parallel D1 (MCP Builder for hireui ATS) + B1 (Process Interviewer for autopilot skill). Both formalize existing ad-hoc work. **Report:** did interviewer change your PRD? Did MCP Builder eliminate boilerplate?

**Week 3:** Stack C3 (Decision Toolkit for v66 decisions) + C5 (Process Interviewer for routine v2.2). Prepares v66 mini-audit with visible reasoning. **Report:** are audit decisions more defensible? Is routine v2.2 codification clearer?

**By end of month:** validate 3 start-steps + 6 additional methods across flows. Pattern: which meta-skills compound fastest with your existing discipline? That's your next focus for routine v2.2 codification.

---

**File prepared for Storm Bear's vault integration. Apply sequentially, measure iteratively. The meta-skills are tools; your second brain is the foundation.**

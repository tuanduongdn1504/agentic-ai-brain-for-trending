# (C) Progress Log — Career Path & CV

_Decisions + weekly notes. No raw PII here (that lives in the gitignored files)._

## 2026-07-11 — Project started

- **Scaffolded** the project: Charter + Setup Runbook + Target-Roles template + `.gitignore` (PII protection) + this log.
- **Decisions (operator):** engine = **career-ops (v200) + vault project** · intent = **active job search** · CV privacy = **vault folder, gitignored**.
- **Engine rationale:** career-ops is purpose-built for candidate-side CV-tailoring + role scoring; it's the E22 personal-use path from the v200 pilot menu. Bonus: it's the candidate-side mirror of hireui (the employer-side product) → empathy/insight for hireui's users.
- **Off-Goal-#1 flag:** this is a personal career project, tracked separately from the LLM-Wiki corpus.
- **Blocking input:** operator's **target career direction** (drives archetypes + CV framing) + current CV situation — awaiting.
- **Next:** operator (1) runs the Setup Runbook (install-snapshot → npm-security-check → `npx @santifer/career-ops init` outside the vault → feed CV/profile/proof-points); (2) tells me the target direction so I draft the filled Target-Roles + `profile.yml` starter + a CV-modernization plan.

## 2026-07-11 (2) — CV received + target chosen

- **CV** transcribed to gitignored `cv.md` (Duong Van Tuan, React Native Engineer, Danang; ~7–8 yrs; PSM II Scrum Master; wants iOS but chose an RN target).
- **Target chosen (operator): "This HT Plus role specifically."** HT PLUS SOFTWARE — React Native Mobile Developer — ~Junior/Middle — Đà Nẵng. Full JD NOT fetchable (FB login wall gave title only).
- **Key finding:** operator is **over-qualified** for a Junior/Middle RN role → the tailoring job is to defuse the flight-risk/comp/"why-a-Scrum-Master" fears WITHOUT lying. Strategy locked into `(C) Target Roles & North-Star.md` (lead hands-on RN · compress the L&D block · right-size PSM II · quantify · cover-letter carries the genuine "why this level" reason).
- **CV assessment delivered** (in-chat): top fixes = zero-quantification (#1), copy-paste bullets, missing hireui/TalentAxis + GitHub, "5 years" undersell, unfocused summary. Strengths = PSM II + ISO 27001 + livestream product + CI/CD/OTA maturity + the rare RN-engineer-who-is-a-Scrum-Master combo.
- **Blocking inputs (from operator):** (1) the full JD text; (2) the genuine reason for wanting this mid-level role (for the cover letter).
- **Next:** on those two inputs → career-ops A–G evaluation + tailored `cv-htplus.md` + cover-letter draft.

## 2026-07-12 — facts in, CV rebuilt, cover letter drafted (application pack ready for review)

- **Facts received:** RN since 2018; current role = **React Native Leader at CVTOT (2/2026–now)** building TalentAxis + Space 360; Song Anh RN Engineer 3/2025–2/2026 (livestream); shipped TalentAxis (iOS) + Space 360 (iOS+Google Play) with **in-app purchases**; GitHub github.com/tuanduongdn1504; metrics DEFERRED.
- **`cv-htplus.md` rebuilt** — real named products + store links + IAP + GitHub + Leader title; fit score ~4.2→~4.6 (native/stores gap closed).
- **Reason chosen (a):** deliberate native-depth — "I've led + shipped; I want a focused IC seat to go deeper into native iOS/Android, which this role values."
- **Cover letter drafted** → `output/(C) HT Plus — Cover Letter.md` (English; ~290 words; addresses the Leader→IC level head-on as a deliberate depth choice; VN version available on request).
- **⚠️ Standing honest flag:** RN Leader → Junior++/Middle IC is a real downshift; the offline interview WILL probe it. The reason + the "run-the-cycle-without-running-the-team" framing is the answer.
- **Application pack COMPLETE (pending operator review):** `cv-htplus.md` + cover letter + evaluation. Remaining = operator review/polish → optional real metrics → export to PDF → apply (email rec@htplus.software). Interview prep: 2 STAR stories (livestream problem; RN/dependency migration).
- **HT Plus STAR stories built** → `interview-prep/(C) STAR Stories — HT Plus.md` (2 STAR+R scaffolds + the level-question answer; operator fills real specifics).

## 2026-07-13 — 2nd target: Digital Unicorn (better fit than HT Plus)

- **Target:** Digital Unicorn (digitalunicorn.fr) — French RN agency in VN since 2018, "best RN agency in Vietnam," 350+ brands; **Mobile Developer (React Native), Middle/SENIOR, onsite Đà Nẵng (Son Tra)/HCMC**; English professional proficiency required; clients France + English-speaking. JD fetched (public Odoo page). Apply: form + talent@digitalunicorn.fr.
- **Why better than HT Plus:** level = **Senior** → no over-qualification/downshift problem; and the JD **explicitly requires "AI tools — Claude Code, Claude Skills,"** where the operator is top-1% (builds daily with Claude Code) = a rare standout. Score **~4.5**.
- **The one real gap: Expo** (JD wants RN+Expo strong; operator reads bare-RN — Stallion/Codepush/NodeMedia). Adjacent gaps: Supabase (≈ Postgres+Firebase), NestJS (≈ Node/HapiJS/Express), Vitest/Maestro. All learnable for a Senior; not disqualifying.
- **Pack built:** `cv-digitalunicorn.md` (AI-first led; RN depth; web; Senior framing) + `reports/(C) Digital Unicorn — Evaluation.md` + `output/(C) Digital Unicorn — Cover Letter.md` (AI-first + RN angle; Expo NOT claimed; [personal reason] placeholder).
- **Interview:** reuse the 2 HT Plus STAR stories (both transfer) + **ADD an AI-tools story** (a concrete Claude-Code/Skills build/review example — the differentiator); expect part of the interview in English.
- **Blocking confirms (operator):** (1) Expo experience? (2) how much AI-first work to disclose; (3) comfortable interviewing in English?; (4) OAuth2/SSO + conventional commits true?; (5) personal "why Digital Unicorn" for the cover letter.

## 2026-07-13 (2) — gaps filled from real product docs (`03 Projects/product`)

- Read `product/hireui-harness/` (=TalentAxis) + `product/anspace-harness/` (=Space 360) — CLAUDE.md + code-analysis report + mobile refactor plan. All facts below sourced from the operator's own project docs (no fabrication).
- **The two Digital Unicorn "gaps" are actually STRENGTHS:**
  - **Expo — CONFIRMED both apps** (TalentAxis `@talentaxis/mobile` = Expo Router + `scheme:talentaxis` + typedRoutes; Space 360 `anspace-mobile` = Expo Router, 46 routes, expo-file-system).
  - **Supabase — CONFIRMED** (Space 360 backend: Postgres, auth, generated types).
  - Bonus HITs: **Turbo monorepo** (both), **shadcn/ui** (Space 360 web), **VietQR payment** integration (Space 360) + App Store IAP, real **React web/dashboards** (TalentAxis Next.js; Space 360 Vite/React/shadcn CRUD).
- **`cv-digitalunicorn.md` rewritten** (hedges → facts), **eval updated ~4.5→~4.8** (near-ideal fit; gaps closed), **cover letter tightened** ("your exact stack, in production: Expo, Supabase, Turbo…").
- **Still genuinely unverified (small):** OAuth2/SSO, Vitest/Maestro, conventional commits, real metrics, English-interview comfort, AI-first disclosure depth. Freshness: stack facts are Apr–May 2026 from operator's own repos — eyeball before sending.
- **NOTE for HT Plus too:** the VietQR + IAP payment facts + the confirmed shipped-apps stack also strengthen the HT Plus pack (payment plus + real-world operation) — refresh `cv-htplus.md` if pursuing HT Plus.

## 2026-07-13 (3) — TalentAxis README + operator confirms → CV v3

- **Operator confirms:** OAuth2/SSO ✓ (Space 360 Supabase social/SSO; TalentAxis multi social/SSO), conventional commits ✓ (hireui-harness). Vitest/Maestro = learnable. English = NOT yet answered (repeated the question) → still OPEN.
- **TalentAxis README (dev guide) read:** TalentAxis = a **microservices platform** — Django (hireapi/jobsapi) + FastAPI (users/comm/automation/scheduling/hireagent) + Celery (hirequeue); MySQL + DynamoDB + Elasticsearch + Redis; Docker/LocalStack; 4 Next.js frontends (hireui/hireadmin/jobsui/hiremarketing); multi-repo `cvtot/*`.
- **Created `(C) Product Facts — proof points.md`** (gitignored) — the single verified proof-bank for all future applications, with an **authorship-boundary** rule (Duong leads the RN+Expo mobile + integrates across the backend; do NOT claim he authored the Django/FastAPI services).
- **`cv-digitalunicorn.md` → v3:** OAuth2/SSO + conventional commits stated; microservices-platform integration context added (honest "integrate across"); Turbo-monorepo claim corrected (Space 360 = Turbo monorepo; TalentAxis = microservices platform). Internal service names/ports/repo URLs kept OUT of the CV. Cover letter + eval synced.
- **2 open items before sending Digital Unicorn:** (1) English live-interview comfort (hard requirement); (2) confirm the backend-authorship framing ("integrate across" vs what you personally build). Then finalize + optionally the AI-tools STAR story.

## 2026-07-13 (4) — English interview-prep drill built

- Operator: keep "Professional English" honest on the CV (written English is fine) + build an English live-interview drill (not fully comfortable speaking live).
- **Created `interview-prep/(C) English Interview Drill — Digital Unicorn.md`** (gitignored): memorizable self-intro (~75s, verified facts) + "why leave CVTOT / why Digital Unicorn" answer + 12 RN/senior technical Q English answer-frames (anchored in his real stack: Expo/Supabase/SSO/OTA/migration/monorepo/microservices/payments/AI-first) + behavioral frames + buy-time/structure/clarify/recover phrases + 3 stories (livestream/migration/AI-tools) + questions-to-ask-them + tricky-word pronunciation.
- **English item now handled** (drill, not fabricated fluency). **1 open item left:** confirm the backend-authorship framing ("integrate across" the microservices platform — accurate?).
- **Offered:** a live English mock (I play the interviewer + drill follow-ups). Digital Unicorn pack is otherwise send-ready pending the backend-framing confirm + the operator filling story specifics.

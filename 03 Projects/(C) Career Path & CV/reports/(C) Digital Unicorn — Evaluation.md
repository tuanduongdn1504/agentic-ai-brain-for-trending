<!-- career-ops-style evaluation · Duong Van Tuan vs Digital Unicorn "Mobile Developer (React Native)" · 2026-07-13 · GITIGNORED (reports/, PII) -->

# Digital Unicorn — Mobile Developer (React Native) — Evaluation

**Company:** Digital Unicorn (digitalunicorn.fr) — French IT agency (Nice/Paris), in Vietnam since 2018; *"best React Native agency in Vietnam,"* 350+ brands. **Onsite, in-house**, Đà Nẵng (Son Tra) or HCMC. Clients in France + English-speaking countries.
**Role:** Mobile Developer (React Native) · **Level: Middle/Senior** · fulltime · **English professional proficiency required.**

## Global score: ~4.5 / 5 — a strong, natural fit. Better-aligned than HT Plus (level matches; your rarest skill is explicitly wanted).

### Block A — Role summary
An international RN agency wants a Middle/**Senior** RN+Expo engineer who ships iOS+Android, does some React web (admin panels), and **works AI-first (Claude Code, Claude Skills)**. Onsite Đà Nẵng/HCMC. Application via their form + talent@digitalunicorn.fr. **Block G (legitimacy): High Confidence** — established company (since 2018), real offices, careers portal, named contact.

### Block B — CV match (requirement by requirement)

| JD item | You | Verdict |
|---|---|---|
| React Native + **Expo** (strong production) | RN: 6+ yrs, deep. **Expo: not evidenced** (your stack reads bare-RN: Stallion/Codepush/NodeMedia) | **RN STRONG / Expo = the one real GAP** — [CONFIRM]. If none, position RN depth + fast ramp; Expo is a workflow layer, learnable in days for someone at your level |
| TypeScript | On CV | **STRONG** |
| **AI tools: Claude Code, Claude Skills** | Daily Claude Code user; build production apps with it; deep Claude-Skills familiarity | **STANDOUT — likely top 1% of applicants.** Your single biggest edge here. Lead with it. |
| Supabase (DB/auth/realtime/edge fns) | PostgreSQL + Firebase (auth, realtime, push) | **ADJACENT** — Supabase ≈ Postgres + Firebase-style; transferable, name the analogues |
| NestJS / backend | Node: HapiJS, Express; REST/GraphQL | **ADJACENT** — same runtime, different framework; not disqualifying |
| REST APIs + backend concepts | Strong | **STRONG** |
| Git + conventional commits | Git ✓ (conventional commits [CONFIRM]) | **STRONG** |
| Testing (Vitest, Testing Library, Maestro) | RN Testing Library, Mocktail, Flutter Test | **PARTIAL** — Testing Library ✓; Vitest/Maestro learnable |
| React web (admin panels/dashboards) | ReactJS (DanaQueue admin) | **OK** — real, if a bit dated; refresh it |
| Nice-to-have: **payment integration** | in-app purchases (App Store) | **HIT** |
| Nice-to-have: CI/CD, Docker | Jenkins, SonarQube, Docker | **HIT** |
| Ship real apps to stores | TalentAxis + Space 360, both stores | **STRONG** |
| **English professional proficiency** | English CV/LinkedIn; ISO 27001 courses in English | **LIKELY OK — [CONFIRM you're comfortable interviewing in English]**; clients are French/English so this bar is real |

**Net:** you clear the core (RN depth, TS, shipping, payments, CI/CD, web) and you **own the JD's rarest explicit requirement (AI tools)**. The one genuine gap is **Expo**; Supabase/NestJS/Vitest/Maestro are adjacent-and-learnable. For a Middle/Senior agency generalist, "deep RN + ships to stores + AI-first + fast learner" more than covers it.

### Block C — Level & framing (much easier than HT Plus)
Level is **Middle/Senior** → you fit **Senior** cleanly. **No "why a mid role" defense needed.** You're not overreaching or underreaching — you're on-level. Present yourself straight: a senior RN engineer who ships and works AI-first.

### Block D — Comp & culture
100% salary in probation, competitive + bonus, insurance, AI-tools support, team events. International agency (French + English clients) = broader exposure than a local shop; onsite Đà Nẵng suits you. **Reliability: Medium** (no public band; salary at offer).

### Block E — Customization → `cv-digitalunicorn.md`
Applied: AI-first (Claude Code/Skills) led high; RN + Expo[CONFIRM] surfaced; Supabase/NestJS mapped to your Postgres/Firebase/Node; React web pulled up; payments/CI/CD/Docker matched; Senior framing (no downshift). **Fill the placeholders** (below).

### Block F — Interview prep
- Reuse **Story 1 (livestream)** + **Story 2 (RN/dependency migration)** from `interview-prep/(C) STAR Stories — HT Plus.md` — both transfer.
- **ADD an AI-tools story** (unique to this role): how you actually use Claude Code / Claude Skills to build — a concrete example (a feature you shipped faster, a refactor, a review workflow). This is the differentiator they're screening for; have a real, specific answer, not "I use AI a lot."
- Expect at least part of the interview **in English**.

## What I need from you to finalize
1. **Expo** — real production experience? (yes → state it; no → we position RN depth + fast ramp, honestly.)
2. **AI-first framing** — how much of your Claude Code / Claude Skills / knowledge-system work do you want to disclose? (It's your biggest edge — I'd lean into it.)
3. **English** — comfortable interviewing in English? (required here.)
4. **OAuth2/SSO** + **conventional commits** — true for you? (both listed; minor.)
5. Optional: your **personal reason** for wanting Digital Unicorn (for the cover letter — e.g. AI-first engineering culture, international/agency exposure, the RN-agency reputation).

---

## UPDATE 2026-07-13 — stack verified from your own product docs; the gaps are CLOSED. Score ~4.5 → **~4.8**.

Read `03 Projects/product/{hireui-harness,anspace-harness}` (harness CLAUDE.md + code-analysis report + refactor plan). Every claim below is sourced from your own project docs — TalentAxis = hireui (`/Users/Cvtot/monorepo/hireui`), Space 360 = anspace (`/Users/Cvtot/monorepo/anspace-space-manager`).

| JD item | Before | After (verified) |
|---|---|---|
| **Expo** | the one real GAP | **CLOSED — strength.** TalentAxis mobile (`@talentaxis/mobile`) = Expo Router (`expo-router` plugin, `scheme: talentaxis`, `experiments.typedRoutes`); Space 360 (`anspace-mobile`) = Expo Router, 46 routes, `expo-file-system`. Real Expo production, both apps. |
| **Supabase** | adjacent (Postgres/Firebase) | **CLOSED — strength.** Space 360 runs on Supabase (Postgres DB, auth, generated types — dominant in its typecheck). Real production Supabase. |
| Turbo monorepo (nice-to-have) | not claimed | **HIT** — both products are pnpm + Turbo monorepos (web + `apps/mobile`). |
| shadcn/ui (nice-to-have area) | not claimed | **HIT** — Space 360 web = `vite_react_shadcn_ts`. |
| Payment integration (nice-to-have) | IAP only | **STRONGER** — App Store IAP (TalentAxis) **+ VietQR** payment integration (Space 360 `src/lib/vietqr.ts`, `TenantPaymentSection`). |
| React web / admin panels / dashboards | "OK, a bit dated" | **STRONG** — TalentAxis web = Next.js (App Router, i18n); Space 360 web = Vite/React/shadcn with full CRUD (buildings/units/tenants/contracts/templates/finance) = exactly "admin panels + dashboards." |
| AI-first (Claude Code) | standout | **reinforced** — you build TalentAxis + Space 360 AI-first with Claude Code + a GitNexus-based agent harness (evidence: these very product docs). |

**Net: the two gaps I flagged are actually your strengths, verified from source.** You now clear Expo + Supabase + Turbo + shadcn + payments + React-web — i.e. nearly the *entire* required + nice-to-have list. This is close to an ideal-fit CV.

**Now CONFIRMED (2026-07-13, operator + TalentAxis README):**
- **OAuth2/SSO — HIT** (Space 360 Supabase social/SSO; TalentAxis multi social/SSO login). A Digital Unicorn nice-to-have, cleared.
- **conventional commits — HIT** (set up in hireui-harness).
- **Microservices/backend breadth — bonus** (TalentAxis = Django/FastAPI/Celery + MySQL/DynamoDB/Elasticsearch/Redis/Docker; you integrate the RN client across it) → strong "REST APIs + backend concepts."

**Still genuinely unverified (small):**
- **English** — comfortable in a LIVE English interview? (written English on the CV is fine; live-interview readiness = the one real open item, and it's a hard requirement here.)
- **Backend authorship** — CV says "integrate across" the platform (safe); confirm, or tell me what backend you personally build.
- **Vitest / Maestro** — not used; "learnable."
- **Real metrics** — deferred (stack/feature specifics carry the CV; add numbers later).
- **AI-first disclosure** — how much of your Claude Code / vault work to show (lean in).

**All verified facts consolidated in `(C) Product Facts — proof points.md` (gitignored) — the reusable bank for every future application.**

⚠️ **Freshness:** stack facts come from your product docs dated Apr–May 2026 — architectural + your own repos, so reliable, but eyeball them before sending in case anything moved.


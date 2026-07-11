# (C) API Security — Pilot Methods for Your Working Flow

> **Topic:** [[api-security-7-techniques]] — LetDiv VN video ([XuzRt-BFIKU](https://www.youtube.com/watch?v=XuzRt-BFIKU)) ← Hayk Simonyan original ([FsB_nRGdeLs](https://www.youtube.com/watch?v=FsB_nRGdeLs)), verified against OWASP / MDN / NIST / RFC.
> **Target working flow:** **hireui** (TalentAxis recruitment SaaS, Goal #2) — grounded in a read-only recon (2026-07-11), see [[hireui-security-posture]].
> **Date:** 2026-07-11.

---

## TL;DR — the headline

> **Invert the videos' priority.** The 7 techniques are hygiene; the thing they *never mention* — **authorization (BOLA)** — is your #1 real risk as multi-tenant SaaS. So the highest-value pilot is **A1: a BOLA / object-ownership audit of every backend resource route**, not any of the 7. Then ship the two cheap frontend wins the recon surfaced (**CSP headers**, currently commented out; **the one unsafe URL interpolation**), make the **CSRF = skip** decision explicit (Bearer auth ⇒ N/A), and treat rate limiting / injection / CORS as defense-in-depth behind authorization.

**Reading the recon changed the plan:** hireui authenticates with **Bearer/JWT in `Authorization` (localStorage)** → **CSRF is N/A** but **XSS is amplified** (a stolen token = account takeover, and HttpOnly can't protect a localStorage token). This repo is the **frontend**; rate-limiting/injection/BOLA/CORS enforcement live on the **separate backend**.

**Where the work lives** (each method tagged): 🖥 **FE-now** (this repo, cheap) · ⚙️ **BE** (backend team/service) · 📋 **ADR** (a decision/doc) · 🎓 **Scrum** (team practice).

**Respect hireui's rules:** everything below is a *proposal*. Actual work in hireui follows ITS CONSTITUTION (I-2 `agent-*` branches, I-8 operator-only skills, GitNexus-first) + BMAD harness. Nothing here was written into hireui.

---

## TIER A — Blocking / critical (do before shipping new endpoints)

### A1 · BOLA / object-ownership audit ⚙️ ⭐ HEADLINE
- **Do:** sweep every backend route that fetches/mutates a resource by id (candidates, applicants, jobs, notes, account-locations, interviews). Ensure each verifies ownership: `if (resource.company_id !== req.user.company_id) throw 403` (+ recruiter-scoping for notes). Prefer **tenant-scoped queries** (`where company_id = :ctx`) so the check can't be forgotten.
- **Verify:** integration test — fetch Company B's resource with Company A's token → expect **403**. Repeat per resource type. (Frontend evidence of the risk: fetch-by-bare-id in `Applicant.service.tsx:118`, `AccountLocation.service.tsx:23`.)
- **Effort:** 2–3 days. **Why:** OWASP **API1**, the #1 breach class; none of the 7 video techniques stop it. → [[what-the-videos-miss-owasp-api-top-10]]

### A2 · BOPLA — field-level authorization ⚙️
- **Do:** identify sensitive fields (salary_history, internal_score, background_check_id, interview_notes). Mask on serialization unless owner+role permits; allow-list which fields each role may **update** (block mass-assignment like `PATCH {status:"hired"}`).
- **Verify:** recruiter from Company B fetches Company A candidate → `salary_history` is null; candidate cannot PATCH their own `status`.
- **Effort:** 1–2 days. **Why:** OWASP **API3**; property leakage/mutation across tenants.

### A3 · BFLA — role-guard privileged endpoints ⚙️
- **Do:** guard every admin/privileged route (`/api/admin/*`, bulk export, salary reports, delete-company) with a role check; default-deny.
- **Verify:** candidate/recruiter token on an admin route → 403.
- **Effort:** 1 day. **Why:** OWASP **API5**; this is where the video's "VPN for internal APIs" advice *actually* belongs for a public SaaS. → [[network-isolation-and-vpn]]

### A4 · Injection audit — raw queries + one FE interpolation ⚙️🖥
- **Do:** backend — grep for raw-query escape hatches (`$queryRawUnsafe`, `.raw(`, template-literal SQL, `sequelize.query('..'+x)`); convert to parameterized. If MongoDB is used, add **operator allow-listing** + schema validation (block `{$ne}`, `{$where}`). Frontend — fix `searchLocation(name)` (`AccountLocation.service.tsx:57`) to use axios `params:{name}` like its siblings.
- **Verify:** test injecting `' OR '1'='1'` and `{"$ne":null}` → zero/expected rows.
- **Effort:** 1–2 days. **Why:** parameterization is OWASP's #1 injection defense; ORM ≠ automatic. → [[injection-sql-and-nosql]]

---

## TIER B — High-value, low-effort (ship early)

### B1 · Rate-limit design — login + expensive + global ⚙️
- **Do:** per-username **and** per-IP on `/auth/login` (~5 / 15 min); per-user quota on expensive/bulk endpoints; a global fallback; **all backed by Redis** (shared state across instances). Return **429 + Retry-After**.
- **Effort:** 1–2 days. **Why:** currently ABSENT (recon). Two buckets, not one; shared store is mandatory. → [[rate-limiting]]

### B2 · Ship a Content-Security-Policy + security headers 🖥 ⭐ CHEAP WIN
- **Do:** uncomment/configure `next.config.mjs` `headers()` (`:114–126`): `Content-Security-Policy`, `Strict-Transport-Security`, `X-Content-Type-Options: nosniff`, `X-Frame-Options: DENY`, `Referrer-Policy`. Start CSP in report-only, then enforce.
- **Effort:** 0.5–1 day. **Why:** defense-in-depth for the **localStorage-token XSS** risk; pure frontend, shippable now. → [[xss-httponly-and-csp]]

### B3 · CORS allowlist correctness (NOT authz) ⚙️📋
- **Do:** confirm backend `Access-Control-Allow-Origin` is an explicit allowlist (prod + staging), never `*` on authenticated routes, and **never reflect arbitrary Origin with `Allow-Credentials:true`** (hireui sends `withCredentials:true`). Add a code comment: "CORS is not authorization."
- **Effort:** 0.5 day. **Why:** the video's #1 conceptual error; a permissive config is itself a vuln. → [[cors-is-not-a-security-control]]

### B4 · CSRF applicability ADR — "skip, here's why" 📋
- **Do:** write a 1-paragraph ADR: *hireui uses Bearer/JWT in the Authorization header ⇒ classic CSRF is N/A ⇒ no CSRF tokens. The only cookie seam is `/api/v2/auth/refresh` (`withCredentials:true`) → its cookie must be `SameSite=Lax|Strict` + `HttpOnly` + `Secure`. Revisit if we adopt cookie sessions.*
- **Effort:** 0.25 day. **Why:** turns "should we do CSRF?" into a decided, documented non-task; saves the effort the video would prescribe. → [[csrf-cookie-vs-token]]

### B5 · Harden the refresh-cookie + token storage 🖥⚙️
- **Do:** verify the refresh cookie flags (SameSite/HttpOnly/Secure). Evaluate moving the **access token out of `localStorage`** into in-memory (so XSS can't read it) with refresh-on-reload.
- **Effort:** 0.5–1 day (audit) / 1–2 days (in-memory migration). **Why:** localStorage token + any XSS = account takeover; HttpOnly can't help there. → [[xss-httponly-and-csp]]

---

## TIER C — Complementary / medium-effort

### C1 · JWT lifecycle — expiry + rotation + revocation ⚙️
- **Do:** short-lived access token (`exp` ~15 min), refresh-token rotation (invalidate old on use), revocation/blacklist on logout.
- **Effort:** 1–2 days. **Why:** OWASP **API2**; the videos treat rate limiting as the whole auth story. → [[what-the-videos-miss-owasp-api-top-10]]

### C2 · Resource-consumption caps (API4 beyond rate limiting) ⚙️
- **Do:** request execution timeouts; **pagination enforcement** on list endpoints (default 50 / max 500); **file-upload size caps** (resumes, e.g. ≤5MB → 413); payload-size limits.
- **Effort:** 1 day. **Why:** rate limiting is only part of OWASP **API4**. → [[rate-limiting]]

### C3 · NoSQL operator-injection guard (if MongoDB) ⚙️
- **Do:** schema-validate inputs; reject `$`-prefixed keys where a scalar is expected; disable server-side JS (`$where`) unless required.
- **Effort:** 1–2 days. **Why:** SQL parameterization doesn't cover NoSQL operator injection. → [[injection-sql-and-nosql]]

### C4 · Rich-text sanitization guardrail 🖥📋
- **Do:** if candidate/job rich text (WYSIWYG/markdown) is ever rendered as HTML, mandate **DOMPurify**; add a lint/PR rule flagging `dangerouslySetInnerHTML`. Remove the **unused `react-quill`** dep or pin+justify it.
- **Effort:** 0.5 day now (rule + cleanup). **Why:** pre-empts the stored-XSS surface before it's introduced. → [[xss-httponly-and-csp]]

### C5 · Input-validation layer (zod) ⚙️🖥
- **Do:** adopt **zod** schemas at API boundaries (backend request bodies; frontend service inputs). Start with auth + candidate/job write paths.
- **Effort:** 1–2 days (initial coverage). **Why:** no validation library today (recon); documents the contract + reduces injection/param surface.

### C6 · WAF / edge decision (confirm prod edge first) 📋⚙️
- **Do:** first **confirm the real production edge** (repo has both `vercel.json` and `appspec.yml`). Then document a WAF escalation trigger: adopt **Cloudflare/AWS WAF (managed, not custom)** at ~10k DAU or on evidence of scanning/enumeration. Note WAF ≠ authorization.
- **Effort:** 0.5 day (decision). **Why:** WAF is a scaling call behind A1–A4, and the deploy target is currently ambiguous. → [[firewall-and-waf]]

---

## TIER D — Defensive depth / nice-to-have

### D1 · API inventory + versioning hygiene 📋⚙️
- **Do:** catalog live endpoints + versions; retire undocumented/`/v1` shadow routes; note auth model per route.
- **Effort:** 1 day. **Why:** OWASP **API9** (Improper Inventory Management) — unmanaged endpoints are silent holes.

### D2 · SSRF review on any URL-fetching endpoint ⚙️
- **Do:** if any endpoint fetches a user-supplied URL (avatar import, webhook, resume-from-URL), allow-list schemes/hosts + block internal ranges.
- **Effort:** 0.5–1 day. **Why:** OWASP **API7**; not in the videos.

### D3 · Turnstile/verify + vietqr route hardening 🖥
- **Do:** the two in-repo API routes (`/api/verify-turnstile`, `/api/generate-vietqr`) have no rate limit/validation — add both.
- **Effort:** 0.5 day. **Why:** small, in-this-repo, closes the only server-ish surface here.

### D4 · SECURITY.md + robots policy 🖥📋
- **Do:** add a `SECURITY.md` (disclosure contact) and a real `robots.txt` (there's a `.sample` only).
- **Effort:** 0.25 day. **Why:** basic hygiene; disclosure path + crawl control.

---

## TIER E — Deferred (re-evaluate at scale)

### E1 · Volumetric DDoS escalation 📋
- Rate limiting ≠ DDoS defense. If volumetric attacks appear, add upstream CDN/scrubbing (Cloudflare / AWS Shield). Defer until observed. → [[rate-limiting]]

### E2 · Internal-service split + VPC/IAM ⚙️📋
- If truly-internal tooling (bulk exports, salary analytics) grows, split it to a separate service behind VPC + identity-aware proxy. For now, role-guards (A3) suffice. Public SaaS ⇒ no corporate VPN. → [[network-isolation-and-vpn]]

---

## 🎓 Scrum-coaching / team-education angles (you're a Scrum coach)

### S1 · "Authorization review" in Definition of Done
For any new resource endpoint, a 15-min ceremony: (1) list resources touched, (2) state the ownership rule in plain language, (3) read the authz check in code, (4) someone proposes an attack ("what if I pass another company's id?"), (5) confirm the code defends. Makes BOLA thinking part of DoD, not an afterthought.

### S2 · Injection & XSS as TDD, not hope
Ship an abuse-case test with each query/render: inject `' OR '1'='1'`, `{"$ne":null}`, `<script>` → assert defended. Moves "the ORM probably handles it" to "we tested it." Pairs with [[system-thinking-ai-coding]]'s reverse-review habit.

### S3 · Rate limiting is a product conversation
Bring PO + design into limit-setting: what's a "normal" recruiter session? Design curves per endpoint; decide the 429 UX. Limits reflect real usage, not guesses. (Good sprint-planning artifact.)

### S4 · Use the video as VN junior onboarding — with the caveat sheet stapled on
The LetDiv video is a solid *vocabulary* primer for VN juniors. Hand it out **with** [[caveats-and-corrections]] and [[what-the-videos-miss-owasp-api-top-10]] so they learn the terms *and* the "authorization-first, decide-before-implement" upgrade. Ties to your junior-onboarding thread ([[hoidanit-fullstack-vibe-coding]]).

---

## ⛔ SKIP list (what NOT to take from the videos)

- **Skip CSRF tokens** — Bearer/JWT ⇒ N/A. (Do the B4 ADR + B5 refresh-cookie check instead.)
- **Skip VPN** — public SaaS; use role-guards (A3), not a corporate VPN.
- **Skip "CORS will protect us"** — it won't; it's not authorization (B3 for correctness only).
- **Skip building a custom WAF** — managed only, and later (C6).
- **Skip "rate limiting = DDoS solved"** — it's app-layer; volumetric needs upstream (E1).
- **Skip "these 7 = done"** — authorization (A1–A3) is the actual priority.

---

## Critic reframe — steelman + when the video is *right enough*

- **Steelman:** for a solo dev shipping a first public API, the 7 are a reasonable "did I forget something obvious?" checklist, and the examples build correct intuition. The video is a *good on-ramp*, honestly presented, with clean "use managed services" advice. Its sin is stopping at hygiene and never reaching authorization.
- **When it's right enough:** a static content API with no per-tenant objects and no auth has little BOLA surface — there, the 7 (minus CSRF/VPN) really are most of the story. hireui is the opposite (multi-tenant PII), which is exactly why the omission bites.
- **The one-sentence upgrade to hand your team:** *"Authenticate, then authorize every object; decide which of the 7 apply to our auth model before implementing any; treat the rest as defense-in-depth."*

---

## Suggested execution order (if you pilot this)

1. **A1 BOLA audit** (headline) + **A4 injection sweep** (backend, this sprint).
2. **B2 CSP headers** + **A4's frontend interpolation fix** + **B4 CSRF ADR** (frontend/docs, this week — cheap, shippable).
3. **B1 rate limiting** + **A2/A3 BOPLA/BFLA** (next).
4. **C1–C6** as defense-in-depth; **D/E** deferred.
5. Wrap A1–A4 as an **abuse-case test suite** (S2) so it's a regression gate, not a one-off — your Goal-#2 measurable artifact.

## Cross-links

[[hireui-security-posture]] · [[what-the-videos-miss-owasp-api-top-10]] · [[csrf-cookie-vs-token]] · [[cors-is-not-a-security-control]] · [[miai-cv-matching-agent]] (recruitment-domain audit) · [[mosh-ai-powered-apps]] (the first-LLM-feature endpoint this secures) · [[ai-engineering]] (demo→production) · [[fullstack-docker-cicd]] (deploy/edge) · [[system-thinking-ai-coding]] / [[hoidanit-fullstack-vibe-coding]] (junior onboarding).

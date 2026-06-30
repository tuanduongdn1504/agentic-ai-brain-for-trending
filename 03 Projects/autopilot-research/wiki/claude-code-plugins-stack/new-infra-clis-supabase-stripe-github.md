# NEW deep-dive: the three dev-infra CLIs (Supabase · Stripe · GitHub)

> Three first-party vendor CLIs you *shell out to* from Claude Code. None have native LLM features — the value is that an agent can drive them. Supabase is the standout hireui fit.

---

## Supabase CLI — `supabase/cli`  ⭐⭐⭐ the #1 hireui fit

### Verified facts (gh api, 2026-06-29)
- **2,315★** · **MIT** · TypeScript · created **2020-11-19** · pushed 2026-06-29. (Low star count = mature vendor tooling, not obscurity.)

### What it is / how it works
Run the **full Supabase stack locally** via Docker (`supabase start`: Postgres + Auth + Realtime + Storage + Edge Functions + Studio at `localhost:54323`). Manage **SQL migrations** (`supabase migration new` → write SQL → `supabase db push`), deploy **Edge Functions** (Deno), and **generate TypeScript types from the schema** (`supabase gen types typescript --local > types/database.ts`). Auth ships with 19 OAuth providers + magic links + OTP + JWT + Row-Level Security. Link local → hosted with `supabase login` + `supabase link`.

### Claims — verdicts
- **"Generous free tier" → PARTIAL.** Real limits: 500 MB DB, 50K MAU, 1 GB storage, 5 GB egress, 500K edge invocations/mo — **but it auto-pauses after 1 week of inactivity and has no automatic backups on free tier.** Fine for MVP/learning, a hard stop for unattended production.
- **"Create DBs + auth from Claude Code with natural language" → PARTIAL.** The natural-language part is **Claude Code + the Supabase MCP**, *not* the CLI — the CLI itself requires explicit SQL/commands. Auth is *provisioned at stack start*, not "created" from the CLI.
- **"Run locally" / "type generation" / "migrations" / "edge functions" → all CONFIRMED.**

### Why it's the standout hireui fit
hireui (TalentAxis recruitment SaaS) is **React/Next.js + TypeScript with zero LLM today** — a clean Supabase on-ramp:
- Candidate form submissions → Postgres + Storage; recruiter logins → Supabase Auth + RLS.
- `supabase gen types` produces the **TypeScript types that mobile + web share** — and the operator-fit critic surfaced a sharp move: **make the generated DB types the source-of-truth for the Candidate-Detail data shape, instead of drifting Figma design tokens.** That attacks the documented root cause of the [[project_candidate_detail_refactor_spike|Candidate-Detail token-drift]] spike (data comes from the schema, not orphaned tokens). ~2h spike.
- Migrations-in-git fits hireui's GitNexus-first + I-2 agent-branch discipline.

---

## Stripe CLI — `stripe/stripe-cli`

### Verified facts (gh api, 2026-06-29)
- **2,101★** · **Apache-2.0** · Go · created **2019-06-14** · pushed 2026-06-26.

### What it is
Test/manage Stripe from the terminal: `stripe listen --forward-to` (local webhook testing, **no third-party tunnel**), `stripe trigger <event>` (fire test events), `stripe get/post/delete` (CRUD on API objects), `stripe logs tail` (filterable real-time logs), fixtures (JSON batch workflows), 7-day sandboxes. Written in Go; all operations run against sandbox.

### Claims — verdicts
- **"For apps you want to monetize / any transactions" → CONFIRMED** (Stripe-specific, not a generic payment tool).
- **"Much easier than the Stripe dashboard" → PARTIAL** — they're *complementary* per Stripe's own docs (CLI for automation/webhook-testing/logs; dashboard for visual/admin/billing simulation).
- **"Control/edit your integration via terminal + natural language in Claude Code is a big benefit" → REFUTED.** Stripe CLI has **zero** native Claude Code / LLM / natural-language features. You can shell out to it from a Claude Code session like any CLI — that's it. (The `CLAUDE.md` in the repo is Stripe's *internal* dev-context file, not an integration. Third-party MCP bridges exist — Composio, etc. — but are external to Stripe CLI.)

### Operator relevance
**Conditional.** Only relevant if hireui adds payments (premium recruiter features, listing fees) — *currently unplanned*. If it enters scope, the CLI is genuinely useful for local webhook testing in CI. **Check hireui's codebase for existing Stripe references before investing.**

---

## GitHub CLI — `cli/cli`

### Verified facts (gh api, 2026-06-29)
- **45,044★** · **MIT** · Go · created **2019-10-03** · pushed 2026-06-26. Description: *"GitHub's official command line tool."*

### What it is / verdict
The canonical first-party `gh` — PRs (`gh pr create/view/merge`), issues, repo ops, releases, and the scriptable `gh api` (which **this very wiki build used** to ground-check all 17 repos' metadata). Chase's "everyone should already have this; first thing you install" is **CONFIRMED and uncontroversial**. It pairs with Claude Code as the git/GitHub action layer: the agent opens PRs, reads issues, and queries the API. For this operator it's almost certainly **already installed** (`gh 2.92.0` is on the machine) — the "new" here is only that the topic hadn't been catalogued.

---

## The shared lesson: "works WITH Claude Code ≠ integrated INTO it"

All three are plain CLIs. Chase's "connect X to Claude Code" framing implies a native integration that doesn't exist — the agent just runs the binary in a shell. That's powerful (an agent that can drive `supabase`, `stripe`, and `gh` is genuinely capable) but it's the *same* mechanism as any shell tool, with the *same* setup/auth burden. Calibrate expectations accordingly. (The one with a true MCP path is Supabase, via the separate Supabase MCP — and that's where the "natural language" actually lives.)

## Cross-links

- [[project_candidate_detail_refactor_spike|hireui Candidate-Detail spike]] — Supabase type-gen as the data SoT move
- [[self-hosted-devops-oss/_index]] — Supabase as own-your-infra (sibling to the self-host cost thesis)
- [[claude-api-cost-optimization/_index]] — free-tier discipline
- [[claude-code-plugins-stack/source-provenance]] — the Stripe "natural language" refutation

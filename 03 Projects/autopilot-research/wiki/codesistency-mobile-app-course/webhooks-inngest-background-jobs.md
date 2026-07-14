# Webhooks, Inngest background jobs, and the Experiments A/B feature

Two of the course's best-taught concepts, both directly relevant to any real product with async work and third-party auth.

## Webhooks: syncing Clerk → Neon

**Problem:** Clerk owns the auth user record, but the app's own Postgres (Neon) also needs a user row. How do the two stay in sync?

**Solution taught:** Clerk **webhooks**. Explained plainly — *"automated messages sent when something happens."* The events:

- `user.created` → insert the user into the DB
- `user.updated` → update the DB row
- `user.deleted` → delete the user (and their data) from the DB

**Wiring (verified accurate):**
1. Build an API route (Expo Router API route — no separate backend) at `/api/webhooks/clerk`.
2. In the Clerk dashboard → Webhooks → add an endpoint pointing at that route, subscribed to the three `user.*` events. Clerk returns a **signing secret** → into `.env` (`CLERK_WEBHOOK_SIGNING_SECRET`).
3. Because Clerk needs a public URL to hit the local dev server, expose it with **ngrok** (free plan gives one persistent domain).
4. The route verifies the signature, then hands off to an **Inngest** background job (`sync-user`) that upserts/deletes the row in Neon.

Clerk's webhooks run on **Svix** with HMAC-SHA256 signing and are **eventually-consistent** (async, retried on failure) — a nuance the tutorial glosses but worth knowing for race conditions.

The account-deletion path closes the loop: the profile screen's **delete-account** button deletes from Clerk → the `user.deleted` webhook fires → the Inngest job removes the user's trips, chat messages, etc. from Neon. This is also an App Store requirement (see [[app-store-readiness]]).

## Inngest as the background-job layer

- Runs a **local dev server** (`localhost:8288`) with a web UI showing functions and runs — you watch jobs execute in real time. Free tier (~50K executions/mo); open-sourced and self-hostable since Jan 2026.
- Used for: the Clerk→Neon `sync-user` job, and the async **trip generation** (OpenAI call runs as a job; the app polls the DB for status, then navigates from loading screen to the trip detail).
- The presenter deliberately uses the **dev server, not EAS hosting**, at the start (his one pushback on Claude's plan — see [[the-anti-vibe-workflow]]).

## Inngest Experiments — model A/B against live traffic (verified real)

The most advanced concept in the course, and the highest docs-lag-risk claim — **independently confirmed real** (Inngest ships "Experiments, Scoring, and Defer — outcome-based evals in the execution layer," comparing production variants on latency, retries, and cost; verify workflow cited the API as `group.experiment()` from the changelog, launched ~June 2026).

**The use case:** you have working code (GPT-4o-mini) and want to try a smarter, pricier model without exposing all users to the risk. With Experiments you:

- Route e.g. **90% of traffic to the old path, 10% to the new** (weighted).
- Get **execution metrics for free** — Inngest already tracks how long each run takes, how often it fails, and cost.
- **Dial up or roll back** by changing two weight values; decide on data, not vibes.

Benefits as framed: low risk (only 10% feel a bad change), real data automatically, easy to ramp. This is a clean, production-grade pattern for LLM model/prompt migration.

## Operator relevance (hireui)

- The **Clerk→DB webhook sync** pattern is directly reusable if hireui adopts a hosted auth provider.
- **Inngest Experiments** is a genuinely useful primitive for hireui's *first LLM feature* rollout ([[mosh-ai-powered-apps]] seam): ship a Match-Explain prompt to 10% of traffic behind an experiment, watch latency/cost/failure, then ramp. It complements the eval-gate thinking in [[prompt-evaluation]].
- Caveat: all of these route execution through Inngest's cloud unless self-hosted — a **data-residency** consideration for candidate PII (see the residency spectrum in [[local-ai-coding-agents]] and [[google-ai-studio-github-import]]).

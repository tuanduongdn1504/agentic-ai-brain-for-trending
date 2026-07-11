# Supabase MCP and the Missing RLS

## Verdict on the video's claim
"Supabase has an MCP connector to Claude — Claude can set up databases without you doing it manually" → **CORRECT-BUT-INCOMPLETE** (high confidence). The connector is real and official; the presentation omits every caveat Supabase itself documents.

## What's real
- Supabase is an **official Claude connector** (supabase.com blog: "Supabase is now an official Claude connector"; installable from the Claude.ai/Desktop connector directory — the plus-icon → Connectors flow shown in the video is accurate).
- Capabilities: inspect schemas, execute SQL, create tables/migrations, deploy edge functions, manage projects — Claude genuinely created Track Rabbit's database on camera.
- Auth: dynamic client registration by default (no manual PAT needed); `read_only` and `project_ref` scoping parameters exist (github.com/supabase-community/supabase-mcp).

## What Supabase's own docs say (all omitted in the video)
1. **"Never connect the MCP server to production data. Supabase MCP is only designed for development and testing purposes."** (supabase.com/docs/guides/ai-tools/mcp#security-risks) — the video builds toward a production multi-tenant SaaS with no mention of this line.
2. **Prompt injection is the primary documented risk**: malicious instructions embedded in returned rows (e.g., a support-ticket description) can steer the LLM into unauthorized queries; Supabase wraps results with discouraging instructions but calls the mitigation "**not foolproof**."
3. Mitigations offered: `read_only` query parameter (read-only Postgres role), `project_ref` scoping to one project, dev-only usage.

## The RLS hole (the biggest gap)
- The video's closing claim — data "is going to be **unique to every user** that signs up... obviously, after you've set up authentication" — silently depends on **Row Level Security policies** that are never shown, plus Supabase Auth that is never built.
- Supabase docs: **"RLS must always be enabled on any tables stored in an exposed schema"**; with a publishable (anon) key, tables without policies are inaccessible-or-open depending on configuration — and a vibe-coded app that disables or forgets RLS exposes **every user's rows to every other user** through the auto-generated API.
- For a receipts app this is financial data; for hireui's domain the identical failure is Recruiter A reading Company B's candidates — the **BOLA-shaped** top risk from [[external|Storm Bear: api-security-7-techniques]], now in database-policy form.
- Correct order of work: enable RLS on every exposed table → write per-table `auth.uid()` policies → test with two real accounts → only then claim per-user isolation.

## Free-tier operational limits (relevant to the demo's longevity)
- 500 MB database (shared CPU, 500 MB RAM), 1 GB file storage, **max 2 active projects**, and **projects pause after 1 week of inactivity** — a demo built this way silently dies a week after the video wraps unless upgraded or touched.

## Key Takeaways
- Use the MCP connector exactly as Supabase scopes it: **dev/test schema work**, read-only where possible, project-scoped, never against production data.
- RLS + Auth is not an "obviously, after..." afterthought — it *is* the multi-tenant product.
- Returned rows are untrusted model input (prompt injection) — same posture the corpus applies everywhere ([[external|Storm Bear: agent-memory-architecture]] read_only-untrusted constraint).

## Sources
- https://supabase.com/docs/guides/ai-tools/mcp · https://github.com/supabase-community/supabase-mcp · https://supabase.com/docs/guides/auth/row-level-security · https://supabase.com/blog/supabase-is-now-an-official-claude-connector · https://supabase.com/pricing

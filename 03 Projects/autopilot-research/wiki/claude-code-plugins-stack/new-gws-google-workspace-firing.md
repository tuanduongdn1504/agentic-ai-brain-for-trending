# NEW deep-dive: GWS — the Google Workspace CLI (and the firing)

> The juiciest claim in the video — "it got the guy fired" — is **true**. But the nuance matters, and the tool itself is genuinely strong.

## Verified facts (gh api, 2026-06-29)

- **Repo:** `googleworkspace/cli` · **29,104★** · **Apache-2.0** · **Rust** · created **2026-03-02** · pushed 2026-06-28 · not archived.
- **Description:** *"Google Workspace CLI — one command-line tool for Drive, Gmail, Calendar, Sheets, Docs, Chat, Admin, and more. Dynamically built from Google Discovery Service. Includes AI agent skills."*
- **Author:** **Justin Poehnelt** — 7 years on Google Workspace Developer Relations.

## What it is

A single Rust CLI for *all* of Google Workspace, built **agents-first**:
- **Dynamic command surface** — queries Google's Discovery Service at startup, so new Google APIs are supported automatically without code changes.
- **103 agent skills** — 19 core services + 24 shortcut helpers + 10 role-based personas + 50 curated multi-step recipes.
- **Email it can actually send** — `+send`, `+reply`, `+reply-all`, `+forward`, `+draft` (the built-in Google connector typically can't compose/send).
- **Pre-built workflows** — `+weekly-digest`, `+meeting-prep`, `+email-to-task`, `+standup-report`.
- Structured JSON output, multipart uploads, auto-pagination (NDJSON), dry-run, Model Armor sanitization, multi-account. Auth via OAuth2 / service accounts / env vars.
- Install: pre-built binary (recommended), `npm i -g @googleworkspace/cli`, `cargo install`, `brew`, or Nix. Setup: `gws auth setup`.

## The firing — CONFIRMED, with nuance

> Chase: *"not an official Google product, created by a Google developer, and it got so popular that it actually got the guy fired."*

**CONFIRMED** via Justin Poehnelt's own X post ([x.com/JPoehnelt/status/2069482265953087602](https://x.com/JPoehnelt/status/2069482265953087602)):
> *"Two months ago I was fired by Google for creating the Google Workspace CLI. It went viral, hit #1 on Hacker News, gained thousands of GitHub stars."*

Corroborated independently (HTX Insights "28,000-Star Hit Creator Unexpectedly Fired"; a Hacker News thread; officechai.com). **But the cause is more specific than "popularity":**
- The firing came **~2 days after Google announced its *own* Workspace CLI at Cloud Next 2026** — i.e., he built a tool that competed with a product the org was about to ship.
- Poehnelt attributes it to **leadership fearing AI agents would disrupt the Workspace product**, plus Legal's concerns about Google logos/branding on the `googleworkspace` org repos.
- So: "fired *for it being popular*" compresses a real organizational/strategic conflict into a clickbait line. The honest version is "fired around the launch of a competing official tool, amid agent-disruption anxiety."

## The "official vs unofficial" contradiction — resolved

The README says **"not an officially supported Google product" (twice)** — yet the repo lives in the **official `@googleworkspace` org** (Google's Developer Samples org) and was authored by a Google employee. This is **not** a contradiction once you split *product* from *governance*:
- **Not an official product** = no SLA, no enterprise support, no Google liability.
- **Is an official-org repo** = maintained under Google's org by a (then-)Google employee.

The right phrasing: *"Google-authored, in an official Google org, but explicitly not a supported Google product."*

## Skill count correction

Chase says "40+ skills." The repo ships **~103** (19 services + 24 helpers + 10 personas + 50 recipes). The README itself is internally inconsistent ("40+" *and* "100+ Agent Skills" both appear). So "40+" is technically true but undersells by ~60.

## Operator relevance

- **hireui (conditional):** a recruitment SaaS does a lot of Gmail/Calendar work — `+email-to-task` for applicant follow-up, `+meeting-prep` for recruiter syncs, `+weekly-digest` for hiring metrics are plausible *operator-side* agent workflows (not product features). Moderate fit, post-LLM.
- **The firing as a teaching artifact (Scrum coaching / harness-engineering):** Poehnelt's story is a sharp, real case of **organizational resistance to agents inside a legacy product division** — directly relevant to hireui's own agent-adoption risk profile, and a strong companion to the [[harness-engineering/_index]] "agent-manager role emergence" thread and Pattern-#51 anti-vibe positioning. Worth a slide.
- **Caution:** as a non-supported tool that already cost its author his job, treat it as a *personal-productivity* aid, not a dependency you'd put in a product's critical path.

## Cross-links

- [[harness-engineering/_index]] — org-resistance-to-agents as a real failure mode
- [[claude-code-plugins-stack/new-infra-clis-supabase-stripe-github]] — sibling "vendor CLI you shell out to"
- [[claude-code-plugins-stack/source-provenance]] — the firing-claim verification + skill-count correction

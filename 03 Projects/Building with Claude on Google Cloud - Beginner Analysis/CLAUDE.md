# Building with Claude on Google Cloud — Project Context

## Subject identity

- **Title:** Building with Claude on Google Cloud
- **Format:** 30-minute live build session (conference talk + demo)
- **Speaker:** Ivan Nardini — Developer Relations Engineer (AI/ML), Google Cloud
- **Event:** Code with Claude 2026 — San Francisco
- **Date / time:** 2026-05-06, 4:05–4:35 PM PT
- **Operator-submitted entry-point:** Vietnamese-dubbed YouTube video at `https://www.youtube.com/watch?v=JUeazROlMCU&t=33s` (title: "(Việt hoá chuẩn) Build & Deploy App Trên Google Cloud Với Claude Code | Code with Claude 2026")
- **Original-language source:** Anthropic-hosted English video at `https://www.youtube.com/watch?v=SqHsS737CeA`
- **Session page (authoritative abstract):** `https://claude.com/code-with-claude/session/sf-building-with-claude-on-google-cloud`

## Typology call — OUT OF EXISTING T1-T5

This subject is a **conference talk + live demo**, not a GitHub repository / shipped product. It does not fit the T1-T5 software-product typology used for v1-v83 corpus subjects.

**Provisional handling:** Treat as a **knowledge-source subject** (analogous to v63 Karpathy or v74 Raschka in role — methodology-influence-node-without-operational-tool — but at a much smaller scope: single 30-min talk vs. multi-year body of work). NOT a corpus T-tier subject. NOT eligible for Pattern Library state-block accumulation under current routine v2.2. Routine v2.3 codification candidate: **NEW typology tier for "conference-talk knowledge-source" subjects**.

Vault state files should NOT be updated for this ingest unless the operator explicitly elects to.

## Content depth — TRANSCRIPT-DEEP (updated 2026-05-21)

The wiki under [02 Wiki/](02 Wiki/) is built from:
- Anthropic session-page abstract (1 paragraph; load-bearing for what the demo covers)
- Speaker profile + public writings + companion infrastructure repo
- Anthropic blog/docs on the three concept primitives the talk uses (subagents, MCP servers, custom skills)
- **`(C) transcript-raw.md` — yt-dlp en-original auto-captions of the English video, extracted 2026-05-21** (~26 minutes, 642 unique caption lines after rolling-window dedup, 30-second timestamp markers for navigation)

It **DOES** include the actual minute-by-minute content of the live build. Entity pages 5-8 (build-architecture / role-decomposition / step-by-step / pitfalls) all cite specific transcript timestamps.

**Surviving gaps requiring code release:** exact prompts at each hat, full CLAUDE.md, subagent definition files, skill `SKILL.md` bodies, exact `gcloud` commands. Speaker stated twice that code would be released post-session. Not located as of 2026-05-21.

## Citation discipline

Every claim in the wiki must trace to one of these sources (or an explicit "from video at HH:MM" placeholder for transcript work). NEVER fabricate the build's specific architectural choices — the public sources confirm only the high-level primitives, not the implementation.

## Relationship to existing corpus

- **Speaker companion repo:** `https://github.com/inardini/ship-code-with-claude-on-vertex-ai-webinar` — same speaker, related topic (Claude Code on Vertex AI), but **different artifact** (developer environment / 3 demos, NOT a "feedback app spanning 5 roles"). Confirmed via README fetch 2026-05-21.
- **Anthropic webinar (related, different content):** `https://www.anthropic.com/webinars/agents-with-claude-on-vertex` — "Building agents with Claude on Google Cloud's Vertex AI"
- **Anthropic at Google Cloud Next 2026:** `https://www.anthropic.com/events/anthropic-at-google-cloud-next-2026`

## Folder layout (mirrors routine v2.2)

```
Building with Claude on Google Cloud - Beginner Analysis/
├── CLAUDE.md                 ← (this file) project-level context
├── 01 Analysis/              ← Phase 4b proposals (none yet — out-of-typology subject)
├── 02 Wiki/                  ← entry-point + entity pages + transcript + log
│   ├── (C) index.md
│   ├── (C) entity-1-talk-metadata.md
│   ├── (C) entity-2-the-concept-stack-subagents-mcp-skills.md
│   ├── (C) entity-3-companion-resources-and-speaker-context.md
│   ├── (C) entity-4-content-gaps-and-ingest-path.md
│   ├── (C) entity-5-build-architecture.md
│   ├── (C) entity-6-role-decomposition.md
│   ├── (C) entity-7-step-by-step-build.md
│   ├── (C) entity-8-pitfalls-and-simplifications.md
│   ├── (C) transcript-raw.md
│   └── (C) log.md
└── 03 Published/             ← empty placeholder
```

## Operator next-step options

1. **Stop here** — wiki is transcript-deep. Accept as final knowledge map.
2. **Find the code release** — once speaker publishes the feedback-app source (post-session promise), ingest that as a separate corpus subject (it would qualify under existing T-tiers as a code artifact, unlike this talk).
3. **Pilot the architecture** — Cloud Run + Firestore + BigQuery + Looker + Vertex AI ADC is reproducible from the transcript alone. Could be a Storm Bear pilot ranked alongside existing candidates (cc-sdd, codex-plugin-cc, free-claude-code).

# (C) Career Path & CV — Project Charter

**Started:** 2026-07-11 · **Owner:** Storm Bear · **Type:** personal (⚠️ OFF the software-development Goal #1 — this is your own career, tracked separately from the LLM-Wiki corpus) · **Engine:** `career-ops` (LLM Wiki v200) · **Mode:** active job search.

> **AI-file prefix:** files I (Claude) author are prefixed `(C)`. Your personal-data files (`cv.md`, `profile.yml`, `article-digest.md`, …) are **yours** and are **gitignored** (see `.gitignore`) — they are never committed or pushed.

## What this project is

A cockpit for **updating your CV(s) and running an active job search toward a chosen career path**, powered by **career-ops** — the candidate-side AI job-search pipeline you shipped as LLM Wiki v200. career-ops scores real job postings 1–5 against your CV, generates an ATS-safe tailored CV per role, checks postings aren't ghost jobs, and tracks your pipeline — all local, and it never submits anything for you.

## Why career-ops is the right engine (not a reinvention)

- It's **purpose-built** for exactly this (its README: *"I gave candidates AI to choose companies"*).
- It's **local-first + never-auto-submit + no-fabrication** — the anti-fabrication rule ("keywords get reformulated, never fabricated; silence beats manufactured detail") keeps your CV honest.
- **Bonus for you specifically:** you build **hireui** (the *employer* side — it screens candidates). Running career-ops (the *candidate* side) on yourself is direct empathy + insight for hireui's future users. Same domain, opposite actor.

## The flow (active job search)

```
1. FEED IT YOU     cv.md + profile.yml (target roles) + article-digest.md (proof points) + voice-dna.md
        │           → the more context you give it, the better it gets (first evals are weak by design)
2. SCAN / EVALUATE  paste a job URL/JD → 1–5 score vs your CV + gap analysis + ghost-job check
        │           → the system recommends AGAINST applying below 3.5/5 (it's a filter, not spray-and-pray)
3. TAILOR           per worth-applying role: an ATS-optimized CV + cover letter (you review + edit)
        │
4. TRACK            every evaluated role → a tracker row; follow-up cadence; interview STAR bank
        │
5. APPLY            YOU review, YOU submit. career-ops never clicks "apply."
```

## Layout of this folder

| File | What | Committed? |
|---|---|---|
| `(C) README — Project Charter.md` | This file | ✅ tracked |
| `(C) Setup Runbook — career-ops.md` | Exact fenced install + onboarding steps | ✅ tracked |
| `(C) Target Roles & North-Star.md` | Your target career path → career-ops archetypes | ✅ tracked (⚠️ needs your direction) |
| `(C) Progress Log.md` | Decisions + weekly notes (no raw PII) | ✅ tracked |
| `.gitignore` | Keeps your CV/PII out of git | ✅ tracked |
| `cv.md` | Your master CV | ❌ gitignored (you create it) |
| `profile.yml` | Target roles / comp / culture screen | ❌ gitignored |
| `article-digest.md` | Your proof points | ❌ gitignored |
| `career-ops/` (if installed here) | The tool + its `data/`, `reports/`, `output/` | ❌ gitignored |

## Honest guardrails (the fence)

- **Your CV is PII.** It stays local + gitignored. career-ops sends it only to the AI provider *you* configure (BYO key) — never to the maintainers, never to me without you deciding.
- **Review every generated line.** AI may inflate skills/history. career-ops's rules forbid fabrication, but you verify before sending — always.
- **Public postings only.** Don't point the scanner at login-gated platforms or use it to mass-apply (its own ToS/anti-spam disclaimer).
- **This is off Goal #1.** Valuable, but personal — kept out of the wiki corpus's goal-tracking.

**Next:** see `(C) Setup Runbook — career-ops.md` to install, and fill `(C) Target Roles & North-Star.md` with your direction (tell me and I'll draft it).

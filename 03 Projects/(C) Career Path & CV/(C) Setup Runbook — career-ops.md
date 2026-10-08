# (C) Setup Runbook — career-ops

Exact, fenced steps to stand up career-ops for your job search. **You run these on your Mac** (career-ops needs your CV + your provider key + your judgment on each generated CV — it's an interactive tool, not something I run for you).

## 0. Security pre-flight (do this every install, don't skip)

career-ops's supply-chain surface was **source-verified BENIGN** in the v200 wiki (postinstall just downloads Chromium via Playwright; 4 minimal deps `@google/generative-ai`/`dotenv`/`js-yaml`/`playwright`; **zero telemetry**; a hard-blocking CI guard that keeps user data out of the repo). But **versions change**, so at YOUR install moment run the live checks:

```bash
# in your terminal, before installing
```
- Run the vault's **`install-snapshot`** skill (snapshots your home dir so you have an uninstall checklist).
- Run the vault's **`npm-security-check`** skill on `@santifer/career-ops` (Tier-1 metadata check).
- Only proceed if both are clean. (v200 assessment: expect BENIGN; the one open item is that career-ops's own `dependency-review` CI is non-blocking pending their issue #343 — not your risk.)

## 1. Install (into a dir OUTSIDE this vault)

Keep the career-ops install **outside** the vault git repo (it has its own repo + `node_modules` — nesting it inside the vault makes a mess). A clean home dir works:

```bash
cd ~
npx @santifer/career-ops init      # clones the latest release into ./career-ops + installs deps
cd career-ops
```

> `npx` ships with Node. Pin the version you reviewed if you want reproducibility: the v200 wiki was source-verified at commit `e9bacc48` (v1.18.0).

## 2. Feed it YOU (this is where the quality comes from)

career-ops is explicit: **the first evaluations are weak until you feed it context.** Create these in the `career-ops/` dir (they're gitignored there by career-ops's own `.gitignore`; keep your canonical copies in THIS vault folder, also gitignored):

- **`cv.md`** — your master CV in Markdown, in the project root. Start from your current CV; we'll modernize it (see below).
- **`config/profile.yml`** — copy `config/profile.example.yml` → fill your identity, **target roles/archetypes** (from `(C) Target Roles & North-Star.md`), comp range, and a `culture_screen` (what you require — e.g. remote, senior mentorship).
- **`article-digest.md`** (optional but high-value) — your proof points: shipped projects, metrics, case studies. career-ops reads metrics from here at eval time, never fabricates them.
- **`voice-dna.md`** (optional) — your anti-AI-slop writing guardrail (banned words, tone) so generated cover letters sound like you, not a bot.
- **`portals.yml`** — copy `templates/portals.example.yml` → add the companies you're targeting.

## 3. Onboard by chatting (no hand-editing needed)

```bash
cd ~/career-ops
claude        # open Claude Code here (or codex / opencode / gemini — your CLI)
```
Then, in the CLI, just talk to it:
- *"Change the archetypes to [your target roles]"* — retarget its default AI-role archetypes to your path (see the Target-Roles doc).
- *"Update my profile with this CV I'm pasting"* / *"Here's my career story and proof points."*
- *"Translate the modes to English"* if needed.

## 4. Run the loop (active search)

```
/career-ops {paste a job URL or JD}   → full auto-pipeline: 1–5 score + gap analysis + ghost-job check + tailored CV + tracker row
/career-ops scan                       → scan your configured portals for new roles (zero API tokens)
/career-ops pdf                        → generate the ATS-optimized CV for the latest evaluated role
/career-ops cover                      → cover letter (draft-in-chat → you approve → PDF)
/career-ops tracker                    → view your pipeline status
```
- **It recommends AGAINST applying below 3.5/5** — it's a filter. Trust that; your time is the scarce resource.
- **Review every generated CV/cover letter line before sending.** You always click "apply" yourself.

## The fence (pinned)

- Live `install-snapshot` + `npm-security-check` before install (step 0) · install OUTSIDE the vault · **BYO provider key** (your data → your chosen provider only) · **review every generated line** · **public postings only** (no login-gated scraping / no mass-apply) · pin `e9bacc48` (v1.18.0) for reproducibility · keep `cv.md`/`profile.yml`/`article-digest.md` gitignored.

**Full 24-method reference** (borrow-by-hand patterns, budget path, etc.): `03 Projects/career-ops - Beginner Analysis/(C) career-ops — Pilot Methods Menu.md`.

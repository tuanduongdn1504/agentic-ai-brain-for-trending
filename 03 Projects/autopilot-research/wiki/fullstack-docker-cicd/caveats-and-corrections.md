# Caveats & corrections

Per the vault prime directive (*don't repeat the same mistake twice*) and Rule 12 (*fail loud*). All items verified refute-first; full verdicts in [[source-provenance]].

## Name: "Gavin Lon" vs. "Gavin Lawn" (Rule 7 — surface the conflict)

The auto-caption transcript renders the instructor's spoken self-introduction as **"Gavin Lawn"** ([00:00:42] "I'm Gavin Lawn"). His **canonical written name is "Gavin Lon"** — freeCodeCamp author page (`/news/author/GavinLon/`), GitHub (`GavinLonDigital`), YouTube channel (`youtube.com/c/gavinlon`), X (`@GavinLonDigital`). Resolution: **same person**; "Lon" is pronounced such that the auto-captioner spelled it "Lawn." This is a phonetic-spelling artifact, **not** a wrong-word garble and **not** a different individual. The verify agent initially read the claim as "inverted" because it weighted the spoken transcript; the written/professional identity is authoritative. **Use "Gavin Lon."** (Verdict C8: PARTIAL — the person, courses, C#/.NET history, and prerequisite-course facts all CONFIRMED; only the "Lawn = garble" phrasing needed this precision.)

## Prerequisite course duration: 14h45m vs. "15 hours"

The prerequisite build course `jBf7of9JTV8` is **14:45:25** exactly (yt-dlp `duration_string`). freeCodeCamp's own article rounds it to "a 15-hour course." Both are correct at different precisions; the wiki uses **14h45m (rounds to ~15h)**. (This was the only sub-point behind C8's PARTIAL; primary yt-dlp metadata beats the rounded prose.)

## The two PARTIAL verdicts

- **C8 (identity):** PARTIAL only for the name-spelling and 14h45m-vs-15h nuances above; all substantive identity facts CONFIRMED.
- **C14 (seed-in-prod):** PARTIAL because of a precision issue. The claim said the base compose "includes" a one-shot seed container gated on a DB healthcheck, and the instructor says on camera that seeding this way is prod-inappropriate — **both TRUE**. But in the **Mastery** repo specifically, the DB + seed services are **commented out** (present-but-inert) in favor of the hardcoded Atlas URI, so "includes" is true structurally but not functionally-active there. In the App/Deploy lineage the seed service *is* active. Net: correct with a per-repo qualifier, not a contradiction.

## Sponsor bias (document, don't discard)

The course is **Hostinger-grant-funded** (stated in intro + description). Hostinger Docker Manager is the only deploy target; GitHub Actions the only CI tool; no Coolify/Vercel/Fly comparison. The Docker/Compose/CI **mechanics are vendor-neutral and unaffected**; only the deploy *target* is sponsored. Handled the same way [[external|Storm Bear: hoidanit-fullstack-vibe-coding]] handles its "Claude Code is the best" / picks-Copilot inversion — flag it, keep the transferable content. See [[deployment-strategy-rationale]].

## Verified-CONFIRMED corrections to the course's own claims

- **Go hot-reload under Compose Watch is false as configured** — `go run` + `action: sync` = no reload; only the Vite client reloads. ([[docker-compose-and-watch]])
- **"Env baking is a Vite problem" is false** — it's every static SPA; nginx ships the workaround natively since 1.19. ([[vite-runtime-env-injection]])
- **The `type=sha` image tag is dead config** — deploys are mutable `:latest`, no rollback pin; empirically confirmed via DockerHub's tag list. ([[cicd-github-actions-pipeline]])
- **Docker Manager CD is manual** — no auto-redeploy webhook; the intro's "push and it deploys" is CI + manual Deploy-button. ([[deployment-strategy-rationale]])

## Silent security items the course does NOT flag

Headed by the **committed MongoDB Atlas credential** (`GavinL:Password1@...`) live for 120+ days in the Mastery repo, plus public HTTP port 8081, no healthchecks/resource-limits, root-run containers. Full catalog + stated-vs-silent split in [[security-and-production-gaps]].

## Discard-as-garble guard — no overturns this pass

Per the [[external|Storm Bear: hoidanit-fullstack-vibe-coding]] Vite×Cloudflare lesson, date-sensitive claims were search-checked before any discard. Nothing here required overturning a prior discard: the Atlas credential, the repo timeline, the DockerHub tag set, and the video metadata all ground-truthed on first check. Verifiers ran clean — **0 refuted, 0 agent deaths** across 14 claims.

## What stays open / low-confidence

- **YouTube subscriber count** for `youtube.com/c/gavinlon` not retrievable via public fetch (channel exists; stats gated).
- **Exact Hostinger grant dollar amount** for this specific course not disclosed (tier structure documented; no signed figure).
- **Prerequisite-course reception metrics** beyond ~146K views not found.

## Key takeaways

- Use **"Gavin Lon"** (written/canonical); "Lawn" is a caption phonetic, same person.
- Two PARTIALs are precision nuances, not contradictions; 12 of 14 claims CONFIRMED outright, none refuted.
- Four of the course's own technical claims are wrong-as-shipped (Go watch, Vite framing, sha-tag, manual CD) — corrected in the linked articles.
- Sponsor bias and the silent credential are the two things to carry forward loudest.

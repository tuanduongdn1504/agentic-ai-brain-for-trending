# Caveats & safety (the critic layer)

## Source

Workflow `wf_4a91a8b2-2bb` skeptic agents (`hype-provenance`, `license-security`) + synthesis critic, plus operator `gh api` ground-checks. This is the "read before you rely on it / install it" article.

## 1. License landmines ⚠️

- **`op7418/guizang-ppt-skill` is AGPL-3.0**, not MIT. Confirmed via `gh api` + its LICENSE file. Open Design's README lineage table labels the *bundled copy* `design-templates/guizang-ppt/` as **"MIT, @op7418"** — that **conflicts** with the upstream. AGPL-3.0 is **strong copyleft** (network-use triggers source-availability). If you redistribute anything derived from the deck skill, **verify the actual bundled `LICENSE` file** — don't trust the README's "MIT."
- **`multica-ai/multica` is NOASSERTION** — GitHub detects no recognized OSS license. Its daemon/adapter *pattern* is credited by Open Design, but the multica code itself has **no clear reuse grant**. Look, learn, don't fork it into your own product without clarifying terms.
- Open Design itself is clean **Apache-2.0**; huashu-design, html-ppt, awesome-design-md/skills, hyperframes are MIT/Apache-2.0.

## 2. "No telemetry" is really opt-in PostHog ⚠️

The README says *"no telemetry, no cloud round-trip."* The code (`apps/daemon/src/analytics.ts`) contains **PostHog integration that is a no-op unless `POSTHOG_KEY` is set** (and is further gated by a `telemetry.metrics` user setting). `CONTRIBUTING.md` even rejects telemetry PRs. So it's **defensible but imprecise**: telemetry is off by default in a normal install, but "no telemetry" overstates it. Prompt-telemetry, if enabled, captures **metadata only** (redacted paths, fingerprints, size buckets), not full prompt text. **Precaution:** confirm `POSTHOG_KEY` is unset / disable telemetry after first run.

## 3. "SSRF protection" not confirmed in code ⚠️

The README claims *"per-target SSRF protection blocks internal IPs / link-local / CGNAT at the daemon edge."* The `license-security` skeptic examined the HTTP adapter (`http/adapter.ts`, `origin-guard.ts`) and **found no destination-based IP filtering** — only same-origin CSRF protection. Either it lives elsewhere (MCP layer / external proxy) or it's not implemented. **Your real mitigation is the loopback-only default** (`OD_BIND_HOST` unset → `127.0.0.1`). Do **not** expose the daemon via a reverse proxy assuming SSRF is handled.

## 4. Count inflation / moving numbers ⚠️

Marketing counts don't reconcile and change weekly:
- **Plugins:** README "261" vs directory enumeration **~440+ items** (atoms 13 + design-systems 143 + examples 165 + image-templates 45 + scenarios 13 + video-templates 64). Either "plugin" counts a subset, or the README is stale.
- **Skills:** README "100+" / description "259+" vs **~159** directories. **Design systems:** "150"/"142+" vs **~152**. **Agents:** platform table names **15**, hero image says **21**.
- **The video's "31 skills / 72"** and its **"~27K stars"** are **point-in-time (2026-05-05)** and don't match today's 73K★ / ~159 skills.
- **Treat every count as approximate and rising.** Cite the current `gh api` star number with a date; don't repeat marketing figures as fact.

## 5. Star velocity: extraordinary but assessed organic ✅ (with an accelerant)

73,468★ in **64 days** (~1,147★/day) on a repo created 2026-04-28 is remarkable. The `hype-provenance` skeptic investigated for astroturfing and cleared it:
- **Smooth linear-to-exponential** star-history curve (no bot-burst spike).
- **30 real, named contributors** (top: `lefarcen` 302 commits); **bots < 2%** of activity (`open-design-bot[bot]` 42, `github-actions[bot]` 30).
- Healthy ratios: **fork/star 11.4%**, **issue/star 0.68%**.
- **`nexu-io` is a real org** (created 2026-02-24, 18 repos, 1,233 followers) — not a shell.
- **Accelerant, disclosed:** a paid **"Open Design Fellows" program — $1,000 per merged MR** + LLM credits + a direct review track. This *legitimately* accelerates contribution/attention; it's transparent, not astroturf. Verdict: **organic + paid-contributor-boosted**, not fraudulent. (Precedent: Cursor's ~1.1K★/day in 2023.)

## 6. Maturity / pilot risk

- **~2 months old, pre-1.0, 11 minor versions (v0.1→v0.12) in ~2 months** → `DESIGN.md`/`SKILL.md` formats may still have breaking changes. Fine for exploration; **not** a production dependency yet.
- It **spawns your coding-agent CLI** (which can edit files). Safe by construction (`execFile`, no shell; agent-delegated privilege) **only as far as the CLI you point it at** is safe.
- **Verdict: SAFE TO PILOT IN A SANDBOX**, with the precautions below. Not safe to point at production data or expose beyond localhost on day one.

## 7. Install precautions (checklist)

1. `/npm-security-check` the package before `pnpm install` (postinstall was verified network-free by a skeptic — re-check your version).
2. Compose **`install-snapshot`** for a clean uninstall diff.
3. Unset `POSTHOG_KEY` / disable telemetry.
4. Keep `OD_BIND_HOST` unset (loopback); never reverse-proxy it.
5. Pilot against a **staging mirror** of hireui or a throwaway `agent-*` worktree (per I-2) — **not** production data.
6. Inside hireui, remember installs are the **operator's** job (I-8) — the agent proposes, you install.

## 8. What we could NOT verify (be honest)

- **HyperFrames integration** is README-described, **not code-audited** here (is it shipped or roadmap?).
- **Claude Design `.zip` import** shown in video + landing page, **not found in repo QUICKSTART/docs**.
- **Creative-media providers** (Suno/Midjourney/ElevenLabs/GPT-image/MiniMax) are video/hero-image claims, **not enumerated in fetched docs**.
- **multica architectural debt** is credited, not confirmed by code diff.
- **Fellows program funding/sustainability** disclosed, not independently verified.

## Key Takeaways

- **Two license landmines:** guizang-ppt is **AGPL-3.0** (README says MIT — verify the bundled LICENSE) and multica is **NOASSERTION** (no reuse grant).
- **Two over-claims:** "no telemetry" is really **opt-in PostHog** (off by default), and **SSRF protection is unconfirmed** in code — loopback-only binding is your actual defense.
- **Counts are inflated/moving** — README 261 plugins vs ~440+ dirs, etc.; cite live `gh api` numbers, not marketing figures. The video's numbers are stale point-in-time.
- **73K★ is organic** (smooth curve, 30 real contributors, <2% bots) but boosted by a transparent **$1,000/MR paid-Fellows** program. **Sandbox-pilot it** with the checklist; it's pre-1.0, not production-ready.

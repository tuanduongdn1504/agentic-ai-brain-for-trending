# (C) ui-skills — Pilot Methods Menu

> LLM Wiki **v218** · `ibelick/ui-skills` · 2026-07-18. Honest ~18-method menu (not a padded 24). **On-goal + directly, immediately pilotable into hireui's frontend** — one of the sharpest, lowest-risk Goal-#2 frontend pilots in the recent run. The genuine value = the **first-party anti-slop UI skills** (baseline-ui especially) as ready-to-use constraint gates + the registry as a discovery layer. **⭐ One-thing path: A1 → B5 → D16.**
>
> **Standing fences:** install-snapshot before `npx ui-skills` · npm-security-check `ui-skills` · it aggregates 262 external repos → **trust-what-you-pull** (review fetched skill markdown before applying) · pin **v0.2.3** · hireui per its CONSTITUTION (I-2 `agent-*` branch / I-8 operator-installs / GitNexus-first / **Figma = Source-of-Truth**) · a design-*taste* skill **composes with, never overrides**, the locked Candidate-Detail Figma plan · read-only `<file>` review mode first.

## A — Read + learn (zero install)

- **A1 ⭐** Read `baseline-ui` + `fixing-accessibility` (already fetched into the Deep Dive) — a ready-made anti-slop UI constraint list + an a11y punch-list. ~20 min, zero risk. Internalize the thresholds (≤200ms, compositor-only props, `h-dvh`, one accent per view, `aria-label` on icon-only buttons).
- **A2** Read the 31-topic taxonomy + skim the registry to see how a design-engineering skill space is *organized* (accessibility / motion / systems / visual / interaction / performance / craft / taste / typography / color / 3d / frameworks…) — a map for what "frontend quality" decomposes into.
- **A3** Study the `ui-skills-root` → `list --category` → `get` **progressive-disclosure** mechanism as a pattern: a root router-skill + on-demand fetch is a token-efficient way to give an agent a large skill library without dumping it all into context (the fff v194 / codebase-memory-mcp v172 "structured-surface-not-raw-dump" thread, applied to skills).
- **A4** Note the authorship signal: ibelick is a Base-UI / `motion/react` / Tailwind practitioner — the constraints encode real production taste, not generic advice.

## B — Borrow patterns (zero install, highest ROI)

- **B5 ⭐** Lift `baseline-ui`'s MUST/SHOULD/NEVER constraint list into a **`05 Skills/` design-review checklist** for the vault + hireui's frontend spec. Composes with hallmark v204's 57-gate slop-test list + taste-skill v81. This is the single highest-ROI, zero-install steal.
- **B6** Steal the **review-mode contract** (`/<skill> <file>` → violations [quote the exact snippet] + why-it-matters [1 sentence] + a concrete code-level fix) as the standard shape for any hireui code-review skill — it's a clean maker/checker output format.
- **B7** Steal the **tool-boundaries** discipline from `fixing-accessibility` (*"prefer minimal, targeted fixes; do not refactor unrelated code; do not migrate UI libraries unless requested; do not add aria when native semantics already solve it"*) into `CLAUDE.md` as a general "surgical-diff" rule for any agent touching hireui's frontend.
- **B8** Borrow the **root-router-skill** pattern for the vault's own `05 Skills/` — a small "which-skill-for-this-task" index skill that points at the right sub-skill, so Claude Code pulls only what it needs.

## C — Hands-on, scratch (low risk)

- **C11 ⭐** `npx ui-skills start` + `npx ui-skills get baseline-ui` in a **throwaway dir** to prove the loop (install-snapshot first; npm-security-check `ui-skills`; read the fetched markdown before applying).
- **C12** `npx ui-skills list --category accessibility` / `--category motion` — see what the registry surfaces per category; sample 2–3 external skills and read the markdown (trust-what-you-pull).
- **C13** On a scratch React/Tailwind page, apply `/baseline-ui` and observe the diff — gauge whether the constraints match your taste before pointing it at real hireui code.
- **C14** Compare the fetch model: does `get` write anything into your project (e.g. `.claude/`), or just print markdown the agent reads? Verify before any hireui use (the CLI `.ts` wasn't source-read — check it yourself).

## D — hireui / Goal #2 (behind the CONSTITUTION fence)

- **D16 ⭐** Run `baseline-ui` **`/baseline-ui <file>` read-only review mode** over hireui's `CandidateDetailScreen.tsx` on an `agent-*` branch = a **zero-risk anti-slop punch-list** (violations + fixes, no auto-edit). **Composes with, never overrides, the locked Figma Source-of-Truth + operator-locked decisions** — treat it as a second opinion, not an authority. This is the sharpest, safest first pilot.
- **D17** Run `fixing-accessibility` `<file>` mode over the Candidate-Detail + any hireui form/dialog surfaces (recruitment SaaS has real a11y obligations) → a prioritized, minimal-diff a11y punch-list.
- **D18** Adopt the `baseline-ui` animation constraints (compositor-only props, ≤200ms, `prefers-reduced-motion`) as hireui's motion policy — cheap, high-signal, prevents the exact drift the Candidate-Detail spike flagged.
- **D19** Feed the `baseline-ui` constraint list into hireui's frontend PR-review gate (composes with the loop-engineering v189 PR-babysitter you already run + CodeRabbit) as an automated slop/a11y sweep — **report-only first**.

## E — Off-goal / personal

- **E20** Use ui-skills for your own side projects' frontends (Zola/motion-primitives are ibelick's; his taste is worth borrowing generally).

## F — Vault-meta

- **F21** Bake-off: run `baseline-ui` vs hallmark v204's `audit` vs Anthropic's official `frontend-design` skill vs taste-skill v81 on the **same** hireui page — which catches what? Write up the design-skill-cluster comparison (a genuine synthesis the corpus lacks).
- **F22 ⭐** File for the ~v221 audit: (1) the **§C-mint reviewable alternative** ("CLI-served categorized multi-repo skill registry + root-router-skill") + its DEFERRED watch axis; (2) the **Cited-to-Subject Elevation** data-point (aidevops v47 cited ui-skills.com → now the subject); (3) the **Pattern #68 form-factor sub-variant** ("machine-consumable CLI-served skill registry") joining awesome-claude-skills v50 / awesome-llm-apps v201.
- **F23** Add ui-skills to the design-skill-cluster map alongside impeccable v75 / taste-skill v81 / open-design v83 / ui-ux-pro-max v85 / hallmark v204 — note it's the first *registry/discovery-layer* member (the others are single skills/tools).

## Ranking

Directly-pilotable + on-goal + **low-risk** (read-only review mode; no remote execute, no tunnel, no config mutation evidenced) → **among the strongest Goal-#2 frontend pilots**, comparable to hallmark v204 (both compose with the Figma SoT; ui-skills adds a discovery layer + an a11y skill). Sits ahead of the heavier read-only infra pilots on the standing ladder for *frontend* work specifically. Keep the Figma plan authoritative; use ui-skills as a second-opinion gate.

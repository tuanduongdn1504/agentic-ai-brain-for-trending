# (C) hallmark — Pilot Methods Menu (LLM Wiki v204)

**Subject:** `Nutlope/hallmark` — anti-AI-slop design skill for Claude Code / Cursor / Codex (MIT, v1.1.0, by Together AI). **On-goal + genuinely pilotable into hireui's frontend** — but honestly weighted: it is a *design-taste* skill for greenfield pages / audits / redesigns, and hireui's Candidate-Detail work already has a **Figma Source-of-Truth + a locked plan**. So the sharpest, safest uses are **(1) the read-only `audit` verb** (a zero-risk slop punch-list) and **(2) borrowing the rules/gates/pre-emit-critique discipline** into your design-review — *not* letting a taste-skill override the Figma plan.

**⭐ One-thing path: A1 → C11 → D16** — read the SKILL.md + the 57 gates + the pre-emit critique (zero install) → install into a throwaway page and run `generate`+`audit` → run the **read-only `audit`** over hireui's current Candidate-Detail frontend on an `agent-*` branch = a zero-risk slop punch-list that *composes with* (never overrides) the Figma SoT plan.

**Fence (all hireui methods):** `install-snapshot` first · `npm-security-check` the external agentskills.io `skills` CLI (`npx skills add` runs it; hallmark itself is BENIGN — zero deps, no postinstall) · **pin the commit** (0 releases) · hireui per its CONSTITUTION (**I-2** `agent-*` branch · **I-8** operator-installs-skills · **GitNexus-first** · **Figma = Source-of-Truth**) · **read-only `audit`/`study` first**; never let `redesign`/generate override the locked Candidate-Detail plan · hireui has no LLM spend yet — this is a design-review tool, no API cost.

---

## A — Read & learn (zero install, zero risk)

- **A1 ⭐** — Read `skills/hallmark/SKILL.md` + `references/slop-test.md` (the 57 gates) + the pre-emit self-critique (6-axis 1–5, `<3 → revise`). The single highest-ROI hour: it's a distilled, enumerated **anti-AI-slop checklist** you can apply by eye immediately.
- **A2** — Map hallmark's 6 universal disciplines (pre-emit critique / honest copy / locked tokens / no re-drawn chrome / 4-breakpoint mobile / typography purity) against your own frontend habits — a personal gap-map.
- **A3** — Read the 20 themes + 21 macrostructures as a *vocabulary* for talking about page structure (Bento Grid / Stat-Led / Manifesto / Quote-Led…) — useful even without the skill.
- **A4** — Compare hallmark's rules against **Anthropic's own `frontend-design` skill** (the upstream it cites) + **impeccable v75** (Bakaus, the corpus's other design skill built on the same Anthropic upstream) — see the shared lineage + where hallmark adds enforcement.

## B — Borrow patterns zero-install (into vault + hireui design-review)

- **B5 ⭐** — Lift the **57-gate slop-test list** into a `05 Skills/` design-review checklist (or a hireui PR-review gate). Highest-leverage steal: no install, deterministic, and it encodes exactly the "AI slop" failure modes.
- **B6** — Steal the **pre-emit self-critique** pattern (score 1–5 on named axes, `<N → revise`, stamp the scores in the artifact) as a general *maker/checker* discipline — composes with the loop-verifier (v189) and video-use's (v198) self-eval-before-showing loop.
- **B7** — Adopt the **locked-tokens** rule (named CSS custom properties only; ban inline OKLCH/hex) as a hireui frontend invariant — directly relevant to the Candidate-Detail "drifted tokens" root cause.
- **B8** — Adopt the **honest-copy** gate (no fabricated metrics/testimonials/logos) as a design + a *content-integrity* rule (echoes career-ops v200's anti-fabrication rule).
- **B9** — Adopt the **4-breakpoint mobile floor** (320/375/414/768) + the "no re-drawn chrome" ban as hireui Expo-app review invariants.
- **B10** — Steal the **"never bulk-load the index"** token-efficiency rule (load one macro-file per build) as a general context-discipline for large skill/rule libraries.

## C — Hands-on scratch trial (throwaway repo, no hireui)

- **C11 ⭐** — `install-snapshot` → `npx skills add nutlope/hallmark` into a **throwaway Next.js/Expo page** → run a `generate` brief ("build a landing page for X") and inspect the emitted page + the stamped pre-emit critique. Prove the loop before touching hireui.
- **C12** — Run `hallmark audit <a scratch page>` (read-only) → read the ranked punch-list; confirm the gates fire on real AI-slop patterns (purple gradient, 100vh centred hero, AI-default nav).
- **C13** — Run `hallmark study <a website you admire | screenshot>` → export the portable `design.md`; see how it captures macrostructure/type-pairing/colour DNA.
- **C14** — Run `hallmark redesign <the scratch page> --mood <theme>` on a disposable page → verify it preserves routes/IA/copy while swapping the visual layer.
- **C15** — Bake-off on the SAME scratch page: hallmark vs **Anthropic's official `frontend-design` skill** vs **impeccable v75** — which anti-slop skill fits your taste + workflow?

## D — hireui / Goal-#2 (behind the CONSTITUTION fence)

- **D16 ⭐** — Run the **read-only `audit`** over hireui's current Candidate-Detail (and 1–2 other screens) on an `agent-*` branch → a slop punch-list. **Zero risk (no edits), SkillSpector-class safe.** Feed the punch-list into the existing Figma-SoT refactor plan — it *composes with*, never overrides, the locked plan.
- **D17** — Use the audit output as an *independent second opinion* on the drifted-tokens / half-migrated-r1→r2 findings already in the Candidate-Detail spike — does hallmark's gate list corroborate them?
- **D18** — Pair with **serve-sim v183** (the Expo-simulator visual-verify layer): let the agent SEE hireui's running iOS screen, then run the hallmark gates against what it sees = a design→build→verify loop.
- **D19** — Pair with the **ai-web-design / Taste-Skill `redesign` gate** pilot thread (the headline was "run hireui frontend through a redesign gate per I-8/I-2") — hallmark is a concrete tool for that gate; keep it *advisory* to the Figma SoT.
- **D20** — Extract hallmark's rule-files (typography/color-OKLCH/layout-4pt/responsive) into a hireui **design-token + a11y invariant spec** — turns "taste" into checkable rules the CI can enforce.
- **D21** — Studio use: for a *new* greenfield hireui marketing/careers page (NOT the locked product screens), let `generate` produce a non-slop first draft, then human-review.

## E — Personal / off-goal

- **E22** — Use hallmark for your own side-project landing pages (the `generate` verb is its happy path) — a low-stakes way to internalize the discipline.
- **E23** — Use `study` to build a personal reference library of "design DNA" from sites you admire (portable `design.md` files).

## F — Vault-meta

- **F24** — File the design-skill-cluster observations for the next audit: hallmark = the strongest **Pattern #88 88c** machinery instance to date (impeccable v75 / taste-skill v81 / huashu-design v82 / open-design v83 / ui-ux-pro-max v85 → hallmark v204); the **Anthropic-frontend-design-skill shared upstream** across the cluster; and the **LV-C5 Design-Skill Composition Vocabulary** observation (20 themes + 21 macrostructures). Confirm NO-MINT holds + whether the 88-design N-tally needs updating.

---

*24 methods · ⭐ one-thing path A1 → C11 → D16. hallmark is a design-taste skill: its highest-value, lowest-risk hireui use is the read-only `audit` + borrowing the rules — as an advisor to, never an override of, the Figma Source-of-Truth.*

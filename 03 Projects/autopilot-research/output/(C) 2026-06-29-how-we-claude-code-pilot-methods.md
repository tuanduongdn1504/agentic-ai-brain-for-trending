# "How We Claude Code": Ranked Pilot Methods for Storm Bear

> **Source:** VN dub "Hướng Dẫn Build App Có Verification Agent-Native" ([ATsbgIRA0Fw](https://www.youtube.com/watch?v=ATsbgIRA0Fw)) of Anthropic's **"How we Claude Code"** workshop ([IlqJqcl8ONE](https://www.youtube.com/watch?v=IlqJqcl8ONE), Arno / Applied AI, 2026-05-23). **Originals deep-dived:** Thariq Shihipar's *Unreasonable Effectiveness of HTML* + `ThariqS/html-effectiveness` (20 files/9 cats) + the **`anthropics/cwc-workshops/how-we-claude-code`** repo (the phase-3 verification engine) + Sutton's *Bitter Lesson*.
> **Date:** 2026-06-29. **Operator:** Storm Bear (Karpathy LLM-Wiki maintainer ×2 vaults + `~/.claude` memory + Scrum coach + **hireui/TalentAxis = Goal #2**).
> **Verification:** Workflow `wf_109aca29-27c` (16 agents) + operator `gh api`/`yt-dlp` ground-checks (4 verifiers misfired against local FS → overridden). Ledger: [source-provenance](../wiki/how-we-claude-code/source-provenance.md). Companion wiki: [how-we-claude-code](../wiki/how-we-claude-code/_index.md) (10 files).

---

## Headline Insight

**This is the first topic you've ingested that ships a *deployable artifact*, not just a method — and that directly attacks your "8 pilots ranked / 0 deployed" problem.** The phase-3 verification framework is ~complete, dependency-light TypeScript you can **copy straight into hireui** ([github](https://github.com/anthropics/cwc-workshops/tree/main/how-we-claude-code/phase-3-verify)). Standing up that framework on **one real hireui component** is the cleanest piece of Goal #2 evidence available right now: *"I deployed an agent-native verification harness into production code and an agent drives it."*

And the timing is uncanny: **all three pillars land on the Candidate Detail refactor you already have in flight.** Pillar 1 (interview-first) de-risks the *next* locked Figma decision; Pillar 2 (HTML mockups) is a better RFC than the Markdown you'd otherwise write; Pillar 3 (verify framework) gives the mobile screen a machine-checkable contract — so an agent can confirm "the 3 tabs render the right counts, the avatar is 72px, the verified-timeline colors are correct" instead of you eyeballing it. The workshop's *whole thesis* — *front-load verification because long agent runs make a wrong spec expensive* — is the exact failure mode a token-metered hireui build will hit.

It also **composes with what you already have**, it doesn't replace it: this is **orthogonal to cc-sdd #1** (cc-sdd = design-doc + adversarial *review* discipline; this = a runtime *verification surface*). Run them together and you get spec-discipline **and** a verifiable artifact. The verify framework is also the UI-layer instance of the [[prompt-evaluation]] eval-first discipline you're already piloting, and the natural place your [[claude-api-cost-optimization]] caching matters once HTML specs (2–4× tokens) enter the loop.

**One caution up front, because it's load-bearing for *you* specifically:** the talk oversells "HTML over Markdown." Thariq himself says **Markdown wins for RAG, agent-to-agent, and version-controlled institutional memory — which is exactly what this vault is.** So: **HTML for ephemeral specs/mockups/reviews; keep your wiki in Markdown.** Don't HTML-ify the knowledge base. (Full critic layer: [caveats](../wiki/how-we-claude-code/caveats-and-when-not-to-use-html.md).)

---

## ▶ Start Here (3-Step Sequence)

1. **This week — deploy the verify framework on ONE hireui component (A4).** Copy `how-we-claude-code/phase-3-verify/src/verify/` into `hireui/apps/web/src/verify/`, pick the smallest real component (e.g. `CandidateStats` or `SearchBar`), give it a `data-verify-*` contract + 3 fixtures (empty / loaded / **one probe** broken-on-purpose) + 2 invariants. Run `bun run verify`. **Measure:** the probe fixture FAILS and the others PASS — you now have a verifiable component in production code. *This is the deployment that turns "0 deployed" into "1 deployed."* (Execute hireui-rooted: `agent-*` branch per I-2, BMAD `.pilot-log`.)

2. **Next — apply interview-first + HTML mockup to the Candidate Detail refactor (A1 + A2).** Before re-locking any Figma decision, run "interview me" on the mobile candidate flow, then have Claude (Opus 4.8, `/fast`) generate **3–4 HTML mockups** of the screen and screenshot-iterate. **Measure:** the interview surfaces ≥1 requirement you hadn't written down; a stakeholder actually opens the HTML where they'd have skimmed the Markdown.

3. **Then — wire the agent + CI surfaces and record evidence (A6).** Expose `window.__verify` and point **Playwright MCP** at it; add the `matrix.test.ts` pattern to CI; `bun run record` a `.webm` of a passing run. **Measure:** an agent (not you) runs `runAll()` and reports PASS/FAIL; CI gate is green; you have a shareable clip. *That's the full demo→production verification arc, evidenced — and it composes with cc-sdd #1 and [[prompt-evaluation]].*

---

## Ranked Methods Table

| Rank | Method | Flow | Effort | Value | First Step | Success Signal |
|------|--------|------|--------|-------|-----------|----------------|
| 1 | **Deploy verify framework on 1 hireui component** | A | Med | ⭐High | Copy `phase-3-verify/src/verify` into `apps/web`; pick `CandidateStats`; 3 fixtures + 2 invariants + 1 probe | Probe FAILS, others PASS; `bun run verify` green — **1 pilot deployed** |
| 2 | **Interview-first on Candidate Detail refactor** | A | Low | ⭐High | "Interview me about what a mobile recruiter needs on one candidate; pull out ambiguities" | Interview surfaces ≥1 unstated requirement before re-locking Figma |
| 3 | **4-direction HTML mockups (replace MD RFC)** | A | Low | High | `/fast` → "4 HTML design directions for <feature>, full mockups" | A stakeholder opens + reacts to the HTML; decision made faster |
| 4 | **Wire 3 surfaces + record evidence** | A | High | ⭐High | Expose `window.__verify`; Playwright MCP `runAll()`; add `matrix.test.ts` to CI; `bun run record` | Agent drives verify; CI gate green; `.webm` clip exists |
| 5 | **Screenshot feedback loop (Opus 4.8 vision)** | A | Low | High | Screenshot the mockup → "spacing too tight on mobile, regenerate" | Fewer words-to-fix than describing the misalignment in text |
| 6 | **Extend verify to mobile (Candidate tabs)** | A | High | High | data-verify-* on tab counts/colors; invariant: counts match filter | Mobile screen has a machine-checkable contract; agent confirms tokens |
| 7 | **EXPECTED_FAIL/probe discipline in wiki-build verify** | B | Low | High | Add "every verify run must include a refutation that can fail" to the routine | Fewer confabulation slips (the c1–c5 misfire is the cautionary tale) |
| 8 | **Keep wiki Markdown; HTML only for ephemeral** | B | Low | High | Write the decision rule into autopilot CLAUDE.md notes | No HTML creeps into the RAG/memory layer; clear artifact policy |
| 9 | **Auto + Fast + /effort x-high baseline** | C | Low | Med | Next 3 tasks: `/fast` + shift-Tab Auto + `/effort x-high`; log `/cost` | Iteration count + cost measured before/after; informed default |
| 10 | **"interview me" as default opener** | C | Low | High | Start non-trivial tasks with "interview me about X before we build" | Specs are interview-derived; fewer wrong-direction agent runs |
| 11 | **HTML artifact for any plan >100 lines** | C | Low | Med | When a spec exceeds ~100 lines, ask for it as an HTML artifact | You + colleagues actually read it; export-back edits round-trip |
| 12 | **`/goal` for long autonomous runs** | C | Med | Med | Give a measurable completion condition for a multi-step task | Claude self-loops to the condition without per-step prompting |
| 13 | **Throwaway HTML micro-app to inspect a wiki topic** | B | Low | Med | "Build a throwaway HTML dashboard of this topic's cross-links + gaps" | Faster gap-spotting; artifact discarded after (not committed) |
| 14 | **WCAG + untrusted-HTML guardrails on hireui artifacts** | A | Low | High | Add "WCAG 2.2 AA; never re-feed agent HTML as trusted" to prompts | Accessible specs; no refeed-injection/cookie-JS exposure |
| 15 | **Verify-first Definition of Done** | D | Low | High | Add "has a verifiable surface (contract + ≥1 probe)" to AI/UI DoD | No UI story "done" without something an agent can check |
| 16 | **Teach interview + 4-direction design as a ritual** | D | Low | Med | Run a team session on "interview me" + parallel design exploration | Team stops over-specifying; explores before committing |
| 17 | **"agent-first" reframe for the team** | D | Low | Med | Frame: "rearrange primitives so an agent can drive them" | Team designs artifacts to be agent-legible by default |
| 18 | **cc-sdd × verify-framework combined pilot** | A | High | ⭐High | Run cc-sdd SDD+adversarial-review AND the verify framework on the same feature | Spec discipline + verifiable artifact on one feature; best Goal #2 case |

---

## Detailed Methods by Flow

### **Flow A — hireui Goal #2 (the bullseye: deploy something verifiable)**

> Execute **hireui-rooted** (GitNexus-first + Figma MCP + I-8 operator-installs + I-2 `agent-*` branch + BMAD + `.pilot-log`). The verify framework is **code copied into the repo**, not a skill install — but it's still a hireui change, so branch + BMAD apply. hireui has **no LLM in product yet**, so the LLM-flavored methods (C3 prompt-eval) are *build-it-right specs*, not retrofits.

**A4 (Rank 1) — Deploy the verification framework on one component.** The single highest-leverage move. Copy `how-we-claude-code/phase-3-verify/src/verify/{core,verifiers,harness,specs}` into `hireui/apps/web/src/verify/`. Pick `CandidateStats` (or `SearchBar`). Write a `*.verify.ts` spec: `propsSchema` (Zod), **3 fixtures** — `empty`, `populated`, and `inconsistent` (`probe: true`, deliberately broken) — and **2 invariants** (e.g. *"total = open + closed + draft"*). Add `verifyAttrs({unit:'CandidateStats', total, open, closed})` to the component's root. `bun run verify`. **Success:** the probe FAILS, the rest PASS — a verifiable component now lives in production code. *This is your first actual deployment.*

**A1 (Rank 2) — Interview-first on the Candidate Detail refactor.** Before re-locking a Figma decision, in the hireui worktree: *"I'm reworking `CandidateDetailScreen.tsx` (mobile). Interview me with the AskUserQuestion tool about what a recruiter needs when viewing one candidate — what they do first, edge cases, what I'm not thinking of. Don't assume the current 3-tab design."* **Success:** ≥1 unstated requirement surfaces before code. (Composes with the locked operator decisions — 3 tabs, avatar 72px, verified colors — by *pressure-testing* them, not discarding them.)

**A2 (Rank 3) — HTML mockups instead of a Markdown RFC.** Next feature (bulk tag, search filters, messaging): `/fast` → *"Generate 4 HTML design directions as full mockups (data-heavy table / minimal card grid / chat-style left panel / spreadsheet-like)."* Screenshot, compare, pick. **Success:** a stakeholder opens and reacts to the HTML where they'd have skimmed a 200-line Markdown RFC.

**A6 (Rank 4) — Wire the three surfaces + record.** Expose `window.__verify` in `App.tsx`; connect **Playwright MCP** and have an agent call `manifest()` then `runAll()`; add the `matrix.test.ts` vitest pattern to CI (gate PRs); `bun run record` a `.webm` of a passing replay. **Success:** an agent (not you) reports verdicts; CI is green; a shareable clip exists. *This is the agent-native loop, end to end.*

**A5 (Rank 5) / A3 (Rank 6) — Screenshot loop + mobile extension.** Use Opus 4.8's vision: screenshot a rendered mockup → *"buttons hard to tap on mobile, regenerate with better ergonomics."* Then extend the verify contract to the mobile Candidate tabs (data-verify on tab counts + the verified-timeline colors `#ECFDF5/#FEF2F2`); invariant: *visible count matches active filter*. **Success:** the mobile screen's design tokens are agent-checkable, closing the loop on the token-drift root cause of that refactor.

**A14 (Rank 14) — Guardrails on hireui HTML artifacts.** Add to any HTML-spec prompt: *"WCAG 2.2 AA (ARIA, alt text, tab order); self-contained (inline CSS/JS, base64 images, no network)."* Never re-feed an agent-generated HTML file into a session as trusted (refeed-injection + cookie-JS risk). **Success:** accessible specs; no untrusted-HTML exposure (feeds the hireui CONSTITUTION).

**A18 (Rank 18) — cc-sdd × verify combined pilot.** Run your **#1 ranked cc-sdd** pilot (SDD + adversarial review) **and** the verify framework on the *same* feature: cc-sdd disciplines the spec; the verify framework makes the result machine-checkable. **Success:** one feature with both a reviewed design doc and a verifiable runtime contract = the strongest single Goal #2 deliverable you can produce.

### **Flow B — autopilot-research + Storm Bear vaults**

**B8 (Rank 8) — Keep the wiki Markdown; HTML only for ephemeral.** The talk says "HTML over Markdown"; Thariq says Markdown wins for RAG/agent-to-agent/version-control. **Your wiki is all three.** Decision rule: HTML for one-session specs/mockups/dashboards; **Markdown for the knowledge base, always.** **Success:** no HTML creeps into the compiled wiki; artifact policy is explicit.

**B7 (Rank 7) — Adopt the `EXPECTED_FAIL`/probe discipline in your verify workflows.** The phase-3 framework requires every unit to have a fixture that *can fail* (`EXPECTED_FAIL`, probe). Your wiki-build workflow should do the same: every adversarial-verify pass must include a refutation that *would* fail if the claim were false. The c1–c5 misfire in *this very ingest* (verifiers grepping the local FS and "refuting" a real repo) is the cautionary tale — bake "verify against the *primary source*, and prove the check can fail" into the routine. **Success:** fewer confabulation slips (your known failure mode per memory).

**B13 (Rank 13) — Throwaway HTML micro-app to inspect a topic.** For a wiki audit: *"Build a disposable HTML dashboard showing this topic's articles, cross-links, and gap markers; let me click through."* Inspect, then discard (don't commit — Markdown stays canonical). **Success:** faster gap-spotting at audit time.

### **Flow C — personal Claude Code workflow**

**C10 (Rank 10) — "interview me" as the default opener.** On any non-trivial task: *"Interview me about X before we build."* Cheapest highest-value habit in the talk. **Success:** interview-derived specs; fewer wrong-direction runs.

**C9 (Rank 9) — Auto + Fast + `/effort x-high` baseline.** For 3 tasks, enforce Auto Mode (shift+Tab) + `/fast` + `/effort x-high`; log `/cost` before/after. **Success:** you have your *own* numbers on whether Arno's rig helps your workflow (recruit-SaaS ≠ Anthropic internal). Use **Opus 4.8**, not 4.7.

**C11 (Rank 11) / C12 (Rank 12) — HTML for big plans + `/goal` for long runs.** When a plan exceeds ~100 lines, ask for it as an HTML artifact (with export-back buttons). For multi-step autonomous work, set `/goal <measurable condition>` so Claude self-loops. **Success:** plans get read; long tasks finish without per-step babysitting.

### **Flow D — Scrum coaching / team**

**D15 (Rank 15) — Verify-first Definition of Done.** Add to the DoD for UI/AI stories: *"ships with a verifiable surface — a contract + at least one probe that can fail."* **Success:** no UI story is "done" on a happy-path demo.

**D16 / D17 — Teach the rituals + the "agent-first" reframe.** Run a team session on interview-driven specs + 4-direction parallel design (stop over-specifying; explore before committing). Frame the deeper principle: *rearrange your artifacts so an agent can drive them* (the workshop's actual thesis — "make it available to the agent first"). **Success:** the team designs for agent-legibility by default.

---

## ⛔ Skip / Be-Skeptical List

- **Don't HTML-ify the vault.** Your Markdown knowledge base is the textbook case where Markdown wins (greppable, diffable, RAG-friendly, agent-to-agent). HTML is for ephemera only.
- **Don't believe "HTML isn't less token-efficient" at the document level.** It's **2–4× tokens**; the claim is a *long-run-iterations* argument. With a token-metered budget, measure it ([[claude-api-cost-optimization]]).
- **Don't read the Bitter Lesson as "the model knows what you want better than you."** That's Arno's analogy, over-reaching past Sutton. Use the interview to *surface* requirements; **you still own and endorse the objective.**
- **Don't claim the blog "went viral."** Unverified — no primary metric. (Repos have hundreds of stars.)
- **Don't expect S3 / a turnkey recorder.** The repo records locally; S3 is a verbal aside. You'd build the upload yourself.
- **Don't treat the a11y verifier as real accessibility coverage.** It's a minimal dependency-free check — not axe-core/Lighthouse. For hireui's ADA exposure, add a real a11y gate.
- **Don't re-feed agent-generated HTML as trusted input** (refeed prompt-injection + JS cookie access).
- **Substitute Opus 4.8 for the talk's Opus 4.7** in any pilot today.

---

## 🧐 A Critic's Reframe

The workshop's durable contribution isn't "use HTML" — it's **"make your artifacts agent-legible, and front-load verification because long agent runs make wrong specs expensive."** Strip the HTML maximalism and the durable trio is: **(1) let the model interview you to de-risk the spec; (2) give the human a rich surface to verify *before* the agent runs; (3) give the agent a machine-readable surface to verify *after*.** That's a verification sandwich around the agent — and it's the same instinct as your own adversarial-verify wiki workflows and [[prompt-evaluation]] discipline, now pushed down to the UI layer.

For you specifically, the honest ranking is: **the verification framework is the prize, the interview habit is the cheap win, and the HTML pillar is a conditional tool you should mostly *not* apply to your vault.** The single move that matters most against your stated bottleneck ("8 pilots / 0 deployed") is **A4 → A6: stand the verify framework up in hireui and let an agent drive it.** Do that and you don't just *know* about agent-native development — you've *shipped* it. That's Goal #2, evidenced.

**Suggested next action:** Create an `agent-*` branch in hireui, copy `phase-3-verify/src/verify/` into `apps/web`, and stand up method **A4** on `CandidateStats` — target: probe-fails-others-pass on `bun run verify` by end of week. Want me to draft that `CandidateStats.verify.ts` spec (fixtures + invariants + probe) against the actual hireui component so you can drop it in?

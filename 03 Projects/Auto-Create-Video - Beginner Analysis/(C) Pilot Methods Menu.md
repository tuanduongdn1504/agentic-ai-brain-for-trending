# (C) Pilot Methods Menu — v262 `hoquanghai/Auto-Create-Video`

## Verdict: **READ-AND-BORROW, and this one is worth an actual afternoon.**

Six ships into this run, this is the first subject whose *engineering practice* is worth copying rather than just cautioning against. It is small (1,569 lines of TypeScript), MIT, tested, CI'd, and its central design decision is the one hireui has to make.

⚠️ Not a hireui component — the domain (Vietnamese news → TikTok video) is off both goals. **What transfers is the shape, and one line of its README.**

---

## Rung 0 — 15 minutes, four things

1. **`README.md:188`** — read the thesis sentence, then stop and decide whether you agree with it. *"AI for content ... deterministic code for production ... same input → identical frames every time."*
2. **`.claude/skills/create-news-video/SKILL.md`** — the frontmatter `description` (trigger phrases + output contract) and Step 2's failure branch.
3. **`package.json`** — the `"test"` script. Spot the flag.
4. **`git log --all --format='%an <%ae>' | sort -u`** — one line, and it is the reason this wiki is about a different person than the URL suggested.

---

## ⭐⭐⭐ Rung 1 — 60 minutes: adopt the split, in writing, for hireui

**The transferable idea, in one sentence: put the model where judgement is required, and deterministic code everywhere the output must be reproducible — then make the boundary explicit in the code, not just in your head.**

This project draws that line and *keeps* it. Claude writes the script (judgement: what matters in this article, how to phrase it in 60 seconds). Everything downstream — timing, layout, audio concat, rendering — is TypeScript and FFmpeg, with **zero `Math.random()` in `src/`**, no network calls inside the render path, and the only timestamp in the whole pipeline confined to a sidecar `meta.json` rather than the output.

**The hireui landing, concretely.** The ratified candidate-LLM legibility ADR requires any LLM path touching a candidate to be *fixed, legible, audited, human-in-loop and eval-gated*. That is the same boundary this project draws:

- **Model side (judgement):** summarise a CV, explain a match, draft screening questions.
- **Deterministic side (must be reproducible and auditable):** scoring arithmetic, ranking, thresholds, filtering, anything a candidate could be told about or could contest. **Never let the model do the arithmetic.**
- **Write the boundary down** in `hireui/docs/adr/` as one sentence with a list on each side, the way `README.md:188` does. If a reviewer cannot tell which side a new feature falls on, the boundary is not written well enough.

⭐ **And the test that proves you kept it:** for a fixed input, the deterministic side must produce byte-identical output twice. That is a real, cheap test, and it is the one this project's thesis implies.

---

## ⭐⭐ Rung 2 — 30 minutes: two patterns worth stealing outright

1. **Negative fixtures as first-class test data.** `tests/fixtures/` holds `invalid-bad-enum.json`, `invalid-line-too-long.json` and `invalid-too-many-scenes.json` — inputs that exist *to be rejected*. Paired with a Zod schema, that is how you prove a validator actually validates rather than merely parses. **hireui's CV-parse path needs exactly this**: a fixture that is a scanned image of nothing, one with a 40-page CV, one with a name field containing 10,000 characters, one with an injected instruction. ⭐ The three named above are the cheapest possible template.
2. **`nock` for provider tests.** The TTS clients (`elevenlabs-client.test.ts`, `lucylab-client.test.ts`) are tested against mocked HTTP, so the suite runs offline, deterministically, and for free. **Any hireui test that would otherwise call Anthropic should look like this** — and it makes the eval-gating clause affordable instead of theoretical.

⭐ **And the skill-authoring detail worth copying:** the frontmatter `description` carries both the *trigger phrases* and the *output contract*. That is the routing surface v250's ADR 0004 identified as load-bearing — and here it is used properly, in the language the user will actually type.

---

## 🔴 Rung 3 — the one thing to fix if you borrow the CI

**Do not copy `"test": "vitest run --passWithNoTests"`.**

That flag makes the command exit 0 when zero tests are collected, and `.github/workflows/test.yml` runs exactly `npm test`. Move a directory, rename a suffix, edit `vitest.config.ts` — and the `Tests` badge stays green on an empty suite, on every push, silently.

⭐⭐ **The rule, and it is the sharpest thing this run produced about gates: a gate that cannot fail is worse than a gate nobody invokes.** v261's verification command fails loudly and was therefore never run by anyone. This one cannot fail loudly and runs constantly. **If you take the workflows, drop the flag** — and if you have a reason to keep it (a monorepo package with genuinely no tests yet), assert the count instead: fail when the collected-test count is below a floor you commit to.

---

## 🔴 NEVER

- **Never attribute this repository to `mranex`.** It is a fork with zero commits by the forker; every commit is Ho Quang Hai's, and the wiki credits him. *(And run `git log --format='%an <%ae>' | sort -u` before you attribute anything, ever — I nearly didn't.)*
- **Never cite star counts for it.** I fetched the *fork's* page (1 star); the upstream's figures are unmeasured and the API is mocked here.
- **Never treat the determinism claim as verified end-to-end.** It holds for this project's code — I checked. Byte-identical *encoded* output additionally depends on the FFmpeg build, which I could not execute.
- **Never point this pipeline at candidate material.** It fetches arbitrary URLs, writes files named from the content, and ships audio to a third-party TTS provider.
- ⚠️ **Do not install it casually to try it** — it needs FFmpeg, Node 22 and a paid TTS key, and the value here is the reading, not the artifact.

---

## ⚠️ Added after verification — read the README sceptically

The architecture thesis is true and I checked it. **The feature inventory is not.** The README claims 12 templates (six exist), names six theme palettes that appear nowhere in `src/`, advertises a Gemini thumbnail stage with no code, and lists `voiceChunks`, hyperframes quality gates and an `sns_post.txt` output that do not exist. Its stated font stack is wrong in two of three.

⭐ **So when you read it for the patterns above, trust the claims that something checks** — the test count, the frame dimensions, the dependency table, the SFX tiers, all correct to the digit — **and verify anything that only the prose asserts.** The project's own final commit tried to reconcile the README to the code by hand and did not manage it.

⇒ **The transferable lesson is now sharper than "copy his discipline": point a gate at your docs too, or accept that your docs are the part that will drift.**

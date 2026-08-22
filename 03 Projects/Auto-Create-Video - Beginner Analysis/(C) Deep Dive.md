# (C) Deep Dive — v262 `hoquanghai/Auto-Create-Video`

**Shipped:** 2026-08-21 · **Wiki:** v262 · **Verdict:** GOAL-ALIGNED INCLUDE · **NO MINT**
⚠️ **The operator supplied `mranex/Auto-Create-Video`. That is a FORK with zero commits by the forker. The subject of this wiki is the upstream, `hoquanghai/Auto-Create-Video`, and the author credited throughout is Ho Quang Hai.**

---

## 1. ⚠️ First, a correction I owe the record

The operator queued this as the sixth `mranex` repository, and I said in my own previous message that it would take the same-author control to **N=6**. **That was wrong**, and one command settles it:

```
$ git log --all --format='%an <%ae>' | sort | uniq -c
  34 Ho Quang Hai <62106658+hoquanghai@users.noreply.github.com>
```

**All 34 commits are by Ho Quang Hai. Zero by `mranex`.** The rendered GitHub page confirms it: *"forked from hoquanghai/Auto-Create-Video"* — 1 star, 0 forks, no description on the fork.

⇒ ⭐ **The same-author control stops at N=5.** It does not extend here, and asserting it would have been a fabrication built on a URL.

⭐ **New rule candidate (D49): a repository's namespace is not a claim about its authorship.** Before attributing a repository to the account that hosts it, run `git log --format='%an <%ae>' | sort -u` and check the rendered page for a fork notice. Forks, transfers and org memberships all put other people's work under a given name. **This is the cheapest possible check and I nearly skipped it because five URLs in a row had been genuine.**

---

## 2. But the fork is a better control than anything I could have built

Here is why this matters far more than a sixth same-author data point would have.

The five-repository control (v256 → v261) established one habit that replicated **without exception**, across four domains, three GUI toolkits, two languages, project durations from 87 minutes to 31 days, and code volumes from 8k to 55k lines: **zero tests, zero CI, zero agent surface.** At v261 I recorded it as *"a property of the author"* and observed that engineering quality improved measurably while verification did not improve at all.

**This repository sits in the same namespace, in the same language and country context, in the same "automate a media pipeline" domain, from the same weeks — and it has all of it:**

| | the five `mranex` repos | this repository |
|---|---|---|
| test files | **0**, all five | **9** `.test.ts`, 44 `it()` blocks, **116 `expect()` calls** |
| negative-case fixtures | 0 | **3** deliberately invalid (`invalid-bad-enum.json`, `invalid-line-too-long.json`, `invalid-too-many-scenes.json`) |
| CI | **0 `.yml` ever**, all five | **2 workflows** — `test.yml` runs `npm ci`, `npm test`, `npx tsc --noEmit` |
| agent surface | 0 | **`.claude/skills/create-news-video/SKILL.md`, 378 lines** |
| secrets hygiene | plaintext key, no warning (v261) | **`.env.example` committed, `.env` and `.env.local` gitignored** |
| licence | AGPL-last-commit / none / prose-only / Apache / present | MIT, `LICENSE` file present |

### ⭐⭐⭐ And the timeline is the finding

```
2026-04-26   v257  translate-LN-pipeline   created      0 tests, 0 CI
2026-04-29   ──►  Auto-Create-Video begins             9 tests, 2 CI workflows
2026-05-02   ──►  Auto-Create-Video last commit
2026-05-13   v256  my_manga_translator     created      0 tests, 0 CI
2026-05-24   v258  VOCra                   created      0 tests, 0 CI
2026-05-27   v260  Anime_Vault             created      0 tests, 0 CI
2026-05-30   v261  novel_studio            created      0 tests, 0 CI
```

⚠️⚠️ **CORRECTED AT v263.** This paragraph originally read *"He forked a repository with a real test suite and working CI, and then created four more projects over the following twenty-eight days, every one with neither. The example was in his own account the entire time."* **The dates do not support that.** A fork's clone holds upstream history only up to the fork moment, so `8c2e043`'s date (**2026-05-02**) is a **lower bound** on when the fork was made, not the fork date; GitHub does not expose fork dates in a clone and the API is mocked (§37.4). ⭐ **D50: a fork's clone gives you a LOWER BOUND on the fork date, never the fork date.** **What survives:** the repository sits in his account with 9 test files, 116 assertions, 3 negative fixtures and 2 CI workflows, and his own five projects have none — a real contrast that needs no timeline. **What does not survive:** that the example demonstrably preceded his later work. ⚠️ v263 then supplied the counter-case — a second fork in the same account whose HEAD is 2026-06-24, necessarily *after* all five of his projects — so at least one fork postdates his own work in the same domain, which is ordinary behaviour. **Accordingly "forking is not adopting" is walked back to a claim about the present state, not a claim about learning or sequence.**

⇒ ⭐⭐⭐ **v258 established that code moves forward in time and never backward — an improvement reaches project N+1 by copy-forward and never reaches N−1, because nothing carries it back. v262 extends that sideways: it does not even move forward from a repository you own. FORKING IS NOT ADOPTING.**

⚠️ **And the fair reading, which is also the more useful one.** Forking a repository is not a commitment to adopt its practices — people fork things to read them, to bookmark them, to try them once. So this is **not hypocrisy**, and I am not going to frame it as a character finding. The honest statement is structural:

⭐⭐⭐ **A practice does not transfer by proximity. Having the example in your own account, in your own language, in your own domain, in the same month, is not having the habit. Practices transfer by DOING, not by POSSESSING.**

⭐ **And that closes the arc of the whole six-ship run.** v261's lesson was that **a protocol without a gate is decorative** — nine excellent sections, not one of them a precondition, zero evidence records written. v262's is that **an example without practice is inert.** Together: **declaration is not enforcement, and possession is not practice.** Those two sentences are the entire failure mode of the preceding five repositories, and this one is the control that isolates them.

---

## 3. Source verification

✅ **Two clones, `diff -rq --exclude=.git` clean in both directions.**

| Fact | Value |
|---|---|
| HEAD | `8c2e04337ca7fb574692c5830dafde35ac2017cd` |
| Commits | **34** on HEAD and `--all` (D39) |
| Root commits | **2** — `608c5bc` *"chore: initial project scaffold"* (04-29 15:41) and `54a408e` *"Initial commit"* (17:41) |
| Merges | **1** — `8fe5c16` (18:02), joining the two histories |
| Tags | 0 · refs: `main` only (D27) |
| Author | **Ho Quang Hai**, all 34 commits |
| Span | 2026-04-29 15:41 → 2026-05-02 02:59 (~3.5 days) |
| Tracked files | **65** — 27 `.ts`, 10 `.mp3`, 9 `.json`, 5 `.md`, 3 `.html`, 2 `.yml` |
| Source | **1,569 lines** of non-test TypeScript; 645 lines of tests |
| Licence | MIT (`LICENSE` file + `package.json`) |

⭐ The two-roots-and-a-merge shape is the ordinary "started locally, then created the GitHub repo" pattern — local scaffold at 15:41, GitHub's own *"Initial commit"* at 17:41, merged at 18:02. Note that **both histories were preserved by the merge** rather than one being discarded, which is why the full 34-commit record is legible.

---

## 4. What it is

A pipeline that turns a Vietnamese tech article — a URL or a `.txt` file — into a TikTok-ready 9:16 motion-graphic news video of about sixty seconds, with Vietnamese voiceover, sound effects, Ken Burns image motion, GSAP kinetic typography and an auto-injected TikTok follow card. Output is `video.mp4` + `voice.mp3` + `script.txt`. There is a live YouTube Shorts demo linked from the README.

**Stack:** TypeScript on Node 22, `hyperframes` for HTML/CSS/JS → video rendering, FFmpeg for audio, Zod for schema validation, Vitest for tests, `p-limit` for concurrency, `nock` for HTTP mocking in tests. TTS via LucyLab (Vietnamese-optimised) or ElevenLabs, selected by env var. An optional Gemini thumbnail step that is *"gracefully skipped if absent."*

**Two entry points:** a Claude Code skill (`/create-news-video`, the recommended path) and a direct CLI (`npm run pipeline`).

---

## 5. ⭐⭐⭐ The design thesis, and it holds

`README.md:188`:

> *"The pipeline is **AI for content** (Claude writes the script) and **deterministic code for production** (Node/TS/FFmpeg renders the pixels) — same input → identical frames every time."*

That is the clearest single-sentence statement of the agent-pipeline design principle in this entire six-ship run, and it is the reason the project is worth reading. **I checked it.**

- **0 `Math.random()` across all of `src/`** (extent: whole directory) — worth noting against v260, which shipped two biased comparator shuffles.
- **0 network calls inside `src/render/`** — asset fetching is a separate, earlier stage.
- Exactly **one** `new Date()` in the render path, at `rerender.ts:137`, writing `createdAt` into a sidecar **`meta.json`** — and a search for `timestamp|generatedAt|createdAt` across `src/render/` and the templates returns **nothing**.

⇒ ✅ **No timestamp reaches a pixel. "Same input → identical frames" is true of the project's own code.**

⚠️ **Scope, stated:** this is read-derived — there is no node and no ffmpeg in this sandbox, so nothing was executed. Byte-identical *encoded output* additionally depends on the FFmpeg build and encoder determinism, which I cannot verify. **The claim holds at the level of this project's code; it is not established at the level of the encoder.**

⭐ **The ARCHITECTURE claim is honoured exactly.** ⚠️ **But do not generalise that to the README as a whole — see §7, which I got wrong on the first pass and had to correct.**

---

## 6. ⭐⭐ The Claude Code skill, read as an artifact

`.claude/skills/create-news-video/SKILL.md` is 378 lines and it is a serious piece of agent instruction:

- **Frontmatter with real trigger engineering** — the `description` enumerates the Vietnamese phrases that should invoke it (*"Trigger khi user yêu cầu tạo video tin tức, làm short news, làm bản tin video, render tin thành video, làm TikTok tin tức"*) and states the output contract (`video.mp4 + voice.mp3 + script.txt cho CapCut`). That is the routing surface v250's ADR 0004 identified as load-bearing, used correctly.
- **A numbered workflow prefixed "MUST follow these steps in order."**
- **An embedded extraction prompt** for `WebFetch` that names four required JSON fields (`title`, `content`, `ogImage`, `domain`) with types and a word-count target.
- ⭐⭐⭐ **An explicit failure branch that halts:** *"If WebFetch fails (paywall, JS-rendered, 4xx) → tell user to save content to a .txt file and pass that instead. **Stop.**"*
- Deterministic slug rules spelled out for the agent (strip Vietnamese diacritics, `đ→d`, non-alphanumeric → `-`, max 40 chars).

⭐⭐⭐ **Set that last point against v261.** v261's author wrote, in a 149-line protocol, *"If the agent finds a blocker: do not silently skip it"* — and enforced it nowhere. **This author did not write that sentence anywhere; he built the stop into step 2 of the skill.** ⇒ **Enforcement lives in the artifact, not in the manifesto.**

---

## 7. 🔴 The defect, and it is a remarkable callback

`package.json`:

```json
"test": "vitest run --passWithNoTests"
```

**`--passWithNoTests` makes the command exit 0 when no test files are collected.** `.github/workflows/test.yml` runs exactly `npm test`. So if the test glob ever matched nothing — a moved directory, a renamed suffix, a `vitest.config.ts` change — **the `Tests` workflow would go green on zero tests, on every push, silently.**

⭐⭐⭐ **The callback:** at v261 the fleet's synthesis asserted that `pytest backend\tests tests` *"will run zero tests and exit 0 (success on empty suite)"*. I rejected that as contrary to pytest's documented exit codes (4 for a nonexistent path, 5 for no tests collected) — and I was right about pytest. **But the mechanism it described is real, and it is here, opted into deliberately, in the one repository of the six that actually has tests.**

⇒ ⭐⭐ **And this defect is worse than v261's, precisely because it runs.** v261's verification command fails loudly and was therefore never run by anyone. This one cannot fail loudly and runs on every push. **A gate that cannot fail is worse than a gate nobody invokes.**

⚠️ Read-derived: this is vitest's documented flag behaviour, not something I executed.

*(Minor: `typecheck.yml` duplicates the `tsc --noEmit` step that `test.yml` already runs — harmless redundancy, worth a line only because it suggests the two workflows were added without reconciling.)*

---


---

## 8. ⭐⭐⭐ The correction — and it is the better finding

My first pass through this repository concluded that its README was *"the strongest README-claim-versus-code result of the six-ship run."* **That was wrong**, and the fleet caught it. Here is the verified picture, and it is far more interesting than the flattering version.

### What the README claims that the code does not have

| README claim | Where | Reality | Extent of my check |
|---|---|---|---|
| **"12 Smart Templates"** | `:106`, `:399`, and `:201` — *"Zod ^4 discriminated unions (**12 template variants**)"* — and `:560` *"all 12 scene types"* | **SIX.** `script-schema.ts` has exactly six `z.literal(...)` templates (hook, comparison, stat-hero, feature-list, callout, outro); `html-composer.ts` has exactly six `case` branches | both files read in full |
| **"6 theme palettes"** naming `tech-blue`, `growth-green`, `finance-gold`, `warning-red`, `creator-purple`, `news-mono` | `:121`, `:392` | **ZERO in code.** Every occurrence of those names is in `README.md` and `README.vi.md`. `grep -rn` across `src/` returns **0** | whole tree, by file path |
| **Gemini 2.5 Flash Image thumbnail**, in the Tech Stack table and as a stage in the pipeline diagram | `:143`, `:177`, `:200`, `:296` | **ABSENT.** 0 hits for `gemini` in `.env.example`, 0 in `src/`, 0 for `thumbnail` in `src/` | `.env.example` + all of `src/` |
| **`voiceChunks`** for sync-accurate beat timing | 5 mentions | **0 in `src/`** | all of `src/` |
| **hyperframes lint / validate / inspect quality gates**, drawn into the diagram | `:152`, `:198` | **0 in `src/`** | all of `src/` |
| **`sns_post.txt`** among the outputs | 2 mentions | **0 in `src/`** | all of `src/` |
| **Fonts: "Manrope (body) + Anton (display) + Lora (italic serif for quotes)"** | `:209` | `styles.css:5` imports **Inter + Anton + Bebas Neue**. One of three correct | the stylesheet's import line |

### And what it claims that is exactly right

- **"44 unit tests"** — I counted `it()`/`test()` across all nine files: **44, exactly.** *(The fleet said 45 and was wrong.)*
- **1080×1920 @ 30 fps** — correct, and **asserted inside a test** (`html-composer.test.ts` checks `data-width="1080"`, `data-height="1920"`).
- **The 3-tier SFX selector** (`override → semantic → template pool`) — implemented in `src/assets/sfx-selector.ts` and covered by 20 assertions.
- **Every dependency version** in the Tech Stack table — matches `package.json`.
- **The determinism thesis** — verified in §5.

### ⭐⭐⭐ The pattern, and it is a textbook v250 instance

**Everything the code can check is right. Everything only the prose asserts is inflated.**

The checkable claims — the test count, the frame dimensions, the dependency versions, the SFX tiers — are correct to the digit. The unchecked claims — template count, theme palettes, a whole thumbnail stage, a sync mechanism, three quality gates, an output file, two of three typefaces — are variously doubled, absent, or wrong.

⭐⭐⭐ **And the final commit in the entire repository is titled `docs: refresh README tech sections to match current codebase`.** He performed the reconciliation deliberately, as the project's last act — and it did not converge. The README still doubles the template count and still advertises a rendering stage with no code behind it.

⇒ ⭐⭐⭐ **THE FINDING: he built real gates — 9 test files, 116 assertions, two CI workflows — and aimed every one of them at the CODE. The prose has no gate at all, so the prose is where the drift lives. A hand-reconciliation performed once, even when explicitly titled "to match current codebase," does not stay done.** This is v250's rule with a new specimen: **a gate's AIM, not its quality, decides what rots.**

⭐⭐⭐ **And it sharpens the whole six-ship conclusion.** The five `mranex` repositories had **no gates anywhere**, and both their code and their docs drifted. This repository has **gates on the code** — and its code is sound and its claims are honest *precisely where something checks them*, and inflated everywhere else. ⇒ **Tests do not make you honest. They make you honest about the things they test.**

### ⚠️ And my own error, which is the same shape as always

I initially **refuted** the fleet's theme finding, because `grep -rn 'tech-blue' .` returned four hits and I read that as "the themes exist." **All four hits were in `README.md` and `README.vi.md`.** I counted matches without looking at the paths. The fleet was right and I was wrong — and it is, again, a measurement whose extent I failed to inspect rather than a misreading of something I had opened. ⭐ **The lesson for my own method: `grep -c` answers "how many", `grep -l` answers "where", and only the second one tells you whether a thing exists in the code.**

## 9. NO MINT — and the §C-2 catalogue is why

The candidate was an N=2 of **§C row C37**, *"Agent-First End-to-End Generative-Media (Video) Production System"*, anchored on **OpenMontage v188**. The grep surfaced it; reading its definition killed it.

C37 requires *"an agent-**FIRST** system (the coding agent IS the runtime; **NO** Python orchestrator)"* plus YAML pipelines, a multi-provider **generative-media** abstraction, and a **$0 free/local path**. This project has:

- 🔴 **a deterministic TypeScript orchestrator as its defining feature** — literally the opposite commitment, and stated as the thesis at `README.md:188`;
- 🔴 `script.json` behind a Zod schema, **not** YAML pipelines;
- ⚠️ multi-provider **TTS** only (LucyLab / ElevenLabs), not generative media — images come from the article's `og:image`;
- 🔴 **no $0 path** — TTS requires an API key.

⇒ **Adjacency, not instance. Counts unchanged: 46 / 12, §C-1 12, §C-2 38.**

⭐⭐⭐ **And this is the first live demonstration of the argument v259 made for keeping §C-2 at all.** The v259 audit refused to retire 38 N=1 rows on the ground that *"retiring them would destroy the mechanism that makes collision-detection possible."* Here that mechanism did exactly its job: C37 was surfaced by a routine grep, its definition was read, and a false N=2 was prevented — **and the boundary is now recorded so the next reader does not have to re-derive it.** The catalogue paid for itself.

A fresh §C-2 mint for the hybrid architecture was also declined, on the usual grounds: **not world-first** (LLM-for-judgement + deterministic-pipeline-for-output is the standard shape — v217's vision→confidence-JSON→QA-gate, v188's own ~90 deterministic tools, v249's *"only ever removes; it never instructs"*), **architectural principle not capability class**, **domain-not-capability**, §28 as a supporting ground only (§44 clause 5, measured against §C-1 = 12), and a small single-author anchor.

**`inflation_check` HELD** — 0 mints, 0 N-bumps, 0 promotions, 0 retires.

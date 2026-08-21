# (C) Deep Dive — v261 `mranex/novel_studio`

**Shipped:** 2026-08-21 · **Wiki:** v261 · **Verdict:** GOAL-ALIGNED INCLUDE (see Verdict) · **NO MINT**
**Method:** hand-verified throughout, with a 22-agent fleet used for one job only — grading 14 recovered phase specifications against the delivered code. Every `path:line` below was read in my own command output.

---

## 1. What it is

`mranex/novel_studio` — **"Novel Translation Studio"**, an offline, single-user application for semi-automatically translating serial novels (Chinese → Vietnamese) under tight human control of glossary, character relationships, pronouns and dialogue attribution.

Its thesis, from the recovered `goal.md`, is that handing a whole chapter to an LLM is unreliable, so the text is split into **skeleton → item → sub-item with stable IDs**, and each unit is translated with a prompt carrying exactly the context it needs. FastAPI backend, React + React Flow frontend, a Tkinter source-preparation sub-app, OpenAI-compatible providers, file-based per-project storage.

**The fifth `mranex` repository in five consecutive ships** — manga (v256) → light novels (v257) → subtitles (v258) → anime library (v260) → **this**. It takes the same-author control to **N=5**.

⭐ And it is the corpus's **first same-author, same-domain successor**: v257 (`translate-LN-pipeline`, 2026-04-26) was a PyQt6 workbench for exactly this task whose defining design was that *the tool never called an API* — it rendered a prompt, the human pasted it into a chat LLM and pasted the answer back. v261 is that project rebuilt from scratch, 34 days later, in a different stack, with **both** an API path and a manual Prompt Studio path.

---

## 2. Source verification

✅ **Two independent clones, `diff -rq --exclude=.git` clean in both directions.**

| Fact | Value |
|---|---|
| HEAD | `67b10e3e208017c1f57bd672b500fbef85385d26` |
| Commits | **4** on HEAD, **4** on `--all` (D39) |
| Root commits | **1** — `7f7b833` (D39) |
| Merges | **0** · **Tags: 0** · refs: `main` only (D27) |
| Identities | `mranex <elsgman1999@gmail.com>` ×3, GitHub-web noreply ×1 |
| Tracked files | **77** |
| Code | 45 `.py` / **6,638 lines** · 16 `.tsx` / 3,004 · 5 `.ts` / 888 · 1 `.css` / 779 |
| Endpoints | **62**, all in `backend/app/main.py` (723 lines) |
| Licence | a real `LICENSE` file, present from the first commit |

### The whole history is four commits and four hours fifty-four minutes

```
7f7b833  2026-05-30 18:47  Initial commit                        2 files,   892 ins
006e321  2026-05-30 18:49  Plan commit                          20 files,  3419 ins
33e1939  2026-05-30 18:53  Update readme.md                      1 file,    152 ins
67b10e3  2026-05-30 23:41  Done 11 phase + code review round 2  95 files, 13401 ins, 3422 del
```

⭐ Note the shape: the repository was the **workspace for the specification** (commits 1–3) and a **destination for the code** (commit 4, a single 95-file drop). That is a third category the v260 amendment candidate did not anticipate, and it is why the plan is recoverable from the pack while no `.pyc` was ever committed.

---

## 3. ⭐⭐⭐ Headline — the commit that says "Done 11 phase" is the commit that deleted all eleven phases

The **"Plan commit"** at 18:49 added 3,419 lines of specification:

| File | Lines |
|---|---|
| `master_plan.md` | **676** |
| `Novel Studio Blueprint.txt` | 333 |
| `Agent.md` | 149 |
| `goal.md` | 48 |
| `working.md` | 4 |
| `Working/README.md` | 12 |
| `phase/00…11` (**14 documents**) | 2,197 combined |

The final commit, `67b10e3` **"Done 11 phase + code review round 2"**, carries **3,422 deletions** — and `git log --diff-filter=D` confirms it deleted **all 19 planning files**. Nothing of the plan is in the tree. What survives as prose is `README.md` (187 lines) and nothing else.

**Four hours and fifty-two minutes from specification to erasure.**

⭐⭐⭐ This is **v258's pattern at N=2, in its extreme form.** v258 wrote 262,074 bytes of planning documents in 2.4 days and deleted 98.7% of them — but it kept a 75-line survivor, and the code honoured it. **Here there is no survivor at all.**

⭐ And the only reason this analysis exists is that `git` kept what the author threw away: `git rev-list --objects --all` shows **122 paths** where the tree has 77. All 3,594 lines of planning were recovered from the pack and graded (§5).

---

## 4. ⭐⭐⭐ The protocol he wrote, and the evidence he never produced

`Agent.md` (149 lines, deleted) is not boilerplate. It is a **nine-section operating protocol for AI coding agents**, and parts of it are better than what most teams write for humans:

- **§1** names a mandatory read-order and adds: *"Before starting a phase, check `Working/` to see whether another agent already completed or partially completed that phase. **Continue from existing evidence instead of restarting blindly.**"* — a multi-agent handoff protocol with a shared evidence directory.
- **§2** ranks the source-of-truth documents explicitly.
- **§3** fences scope: *"Do not expand scope beyond the phase unless the user explicitly asks."*
- **§4** mandates a per-phase evidence record in `Working/*.md`, with a collision-suffix convention for concurrent agents (`phase_XX_summary_YYYYMMDD_HHMM.md`), and requires it to contain: phase name, date, files changed, what was implemented, **what was tested**, known issues, remaining work, and **deviations from the plan**.
- **§5** keeps root `working.md` as a tiny index and says *"Do not delete existing entries unless the user explicitly asks."*
- **§6** — *"**Every coding agent should verify the work before claiming completion.**"* Record commands run, tests passed or failed, manual checks, **anything that could not be tested**, and *"If tests are not available yet, say that clearly."*
- **§7** — *"If the agent finds a blocker: **do not silently skip it.**"*
- **§8** — `Working/*.md` are **evidence records**; append a `## Correction` section rather than rewriting.
- **§9** — reporting discipline.

Now the measurements.

🔴 **Not one evidence record was ever written.** Extent: all **122 paths on every ref**. `Working/` contains exactly one file in the entire history — its own `README.md`. A search for `phase_.*summar|summary` across all 122 paths returns **nothing**.

🔴 **`pytest>=8.0,<9.0` is declared in `backend/requirements.txt` — and there are zero test files.** Not in the tree, not in any of the four commits, not anywhere in the pack.

🔴 **The README's `Verification:` block reads `pytest backend\tests tests`.** Neither `backend/tests` nor `tests` has ever existed on any ref.

🔴 **The commit message claims "code review round 2."** A search of all 122 pack paths for `review` returns exactly one hit: `frontend/src/pages/GlossaryReview.tsx` — a UI screen for reviewing glossary entries. There is no artifact of round 1 or round 2 anywhere.

🔴 **§5 said "do not delete existing entries"; the final commit deleted `working.md` entirely. §8 said evidence records must not be rewritten; the same commit deleted the evidence directory's own charter.**

⇒ ⭐⭐⭐ **Four independent layers assert verification — the dependency (`pytest`), the protocol (`Agent.md` §6), the instructions (README `Verification:`), and the claim (the commit message plus `## Current Status`). Zero layers perform it.**

⭐⭐ **This is v260's FALSE SUCCESS rule one layer up.** At v260 the Rust shell printed *"Successfully launched Python API server"* on the strength of a `spawn()` while `CREATE_NO_WINDOW` removed the channel that would have shown the failure. Here a commit message printed *"Done 11 phase"* while the same commit removed every document against which "done" could be checked. **Same shape, two layers: assert the success, delete the verification channel.** N=2 by the same author, in code and in process.

---

## 5. ⭐⭐⭐ So was it actually done? Grading the code against the specification he deleted

This is the part no one could do from the repository as shipped, and the reason the fleet existed: **recover all 14 phase specifications from the pack and grade the delivered code against each.** One agent per phase, then an adversarial refuter per phase attacking every ABSENT or PARTIAL claim, so that a false negative had to survive a hostile second reading.

cat > /tmp/sec5a.md << 'XEOF'

## 5a. The grading result — and the answer is *substantially yes*

**Method.** All 14 phase specifications were recovered from the pack and graded by one agent each against the delivered tree, with an **adversarial refuter per phase** attacking every `ABSENT` or `PARTIAL` verdict, so a false negative had to survive a hostile second reading. Ground truth was command-derived only, and the fleet was fenced against importing facts about the four sibling repositories.

| Phase | Verdict | The specific gap, where there is one |
|---|---|---|
| 00 App Foundation | SUBSTANTIALLY | **the acceptance criterion "Basic schema tests pass" — zero tests exist** |
| 01 Source Preparer sub-app | **FULLY** | all 21 concrete requirements implemented |
| 02 Project Manager / Import | delivered | — |
| 03 Skeleton + sub-item | SUBSTANTIALLY | dialogue markers not configurable per `source_language` as specified |
| 04 LLM Provider + Prompt Studio | **FULLY** | all 21 requirements; manual **and** API paths both present |
| 04a Prompt template design | **FULLY** | six templates seeded to the project `prompt/` dir on first access |
| 05 Glossary pipeline | SUBSTANTIALLY | UI lacks an explicit reject control the backend supports |
| 06 Relationship timeline canvas | **FULLY** | all 28 requirements: conflict-aware merge, atomic ID allocation, 7 endpoints, React Flow canvas |
| 07 Dialogue label pipeline | SUBSTANTIALLY | one UI detail (linked-entry display) |
| 08 Translation pipeline | SUBSTANTIALLY | no failed-items table, no Pause button, **`max_attempts` limit missing** |
| 08a Series update | SUBSTANTIALLY | diff UI panels absent; partial-change detection thin |
| 09 Polish + export | SUBSTANTIALLY | three-pane layout became toolbar + two panels; item-detail panel absent |
| 10 Database Editor | PARTIALLY | specialised editors exist as **separate pages**, not integrated into one screen |
| 11 Config + packaging | **UNGRADED** | its grader failed to return structured output — genuinely unmeasured, not assumed |

**Result: 5 FULLY · 7 SUBSTANTIALLY · 1 PARTIALLY of 13 graded.**

⭐⭐⭐ **So the README's claim — "Planning contract and MVP phases 00 through 11 are implemented" — is substantially TRUE.** This is not a story about someone who claimed work he did not do. **He did the work, an agent fleet built it against a real specification, and it largely matches.** Three phases were graded fully delivered against 21, 21 and 28 enumerated requirements respectively.

⭐⭐ **The adversarial pass mattered, and it corrected in the author's favour.** It overturned *"Glossary editor … ABSENT"*, *"Relationship editor … ABSENT"* and *"Dialogue label editor … ABSENT"* to **PRESENT**, and a series-update null-guard rule from ABSENT to **IMPLEMENTED** — which is why Phase 10's `PARTIALLY` should be read narrowly: the editors exist, they are simply not consolidated onto one screen. It also independently refuted the `prompt/` claim I had nearly published as a defect. **Without the refutation layer this ship would have understated what was delivered.**

⭐ **And one fleet finding must be corrected in the author's favour by hand:** the graders flagged EPUB export as absent in phase 09. It is absent — and **the plan pre-authorised that three separate times**: `phase/09_polish_export.md:25` (*"EPUB can be MVP-late if implementation time is tight"*), `master_plan.md:95`, and `master_plan.md:669`. **A gap the specification pre-authorised is not a failure to deliver.**

### 🔴 But there is one gap the specification did *not* authorise, and it is quoted

`phase/00_app_foundation.md` lists *"Basic tests cho storage và schema"* as a deliverable at line 17, and then, under a heading literally titled `## Acceptance Criteria` at line 147, states at line 156:

> **"Basic schema tests pass."**

There are zero test files in the tree, zero in all four commits, and zero across all 122 paths in the pack.

⇒ ⭐⭐⭐ **Phase 00 is the foundation phase. Its own written acceptance criterion was not met. The commit message says "Done 11 phase," and the same commit deleted the document containing that criterion.** That is not an interpretation; it is a quotation.

⭐⭐⭐ **The honest verdict on the completion claim, then, is narrower and far more interesting than "he overclaimed": the FEATURES were delivered, and the ACCEPTANCE CRITERIA were not — and the difference between those two things is exactly what the deleted documents recorded.**

---

## 6. ⭐⭐⭐ The plan pre-authorised a shortcut, the shortcut was taken, and the condition was deleted

`master_plan.md` §17 is titled *"Open Decisions Không Block Phase 0"* — open decisions that do not block phase 0. It is a genuinely sophisticated piece of planning: it separates decisions that must be made now from those that can wait. Its final bullet reads:

> *"Có cần encryption API key local không. MVP có thể lưu app-level config local plaintext và **ghi rõ cảnh báo**."*
> — "Whether local API-key encryption is needed. MVP can store app-level config locally in plaintext and **write a clear warning**."

✅ The shortcut was taken: `backend/app/schemas/__init__.py:19` is `api_key: str = ""`, persisted to app settings, and `frontend/src/pages/ConfigPage.tsx:103-104` renders it as a plain text input.

🔴 **The condition was not met.** Extent: all 77 tracked files, case-insensitive, across nine warning-vocabulary terms including the Vietnamese *"cảnh báo"*. The only two hits are an unrelated React `key={warning}` in a validation-warnings list (`WorkflowDashboard.tsx:159`, `DialogueLabels.tsx:266`). The README mentions api key, secret, security and warning **zero times**.

⇒ ⭐⭐⭐ **THE RULE: a plan that pre-authorises a shortcut creates a debt, and deleting the plan deletes the only record that the debt exists. A deferred decision recorded solely in a document you delete is not deferred — it is silently resolved in favour of the shortcut.** This is the natural successor to v258's *"a plan document is a fence around exactly the surfaces it names"*: here the fence named the surface precisely, and then the fence was demolished.

---

## 7. ⭐⭐⭐ Two defects from earlier siblings, fixed — the clearest learning in the set

This is where v261 changes the five-repo picture, and it is the strongest evidence the control has produced.

### The silent-degradation defect, closed

The vault's own v257 record states: its `prompt_engine` read `00_json_output_policy.txt` and *"if absent, sets `json_policy = ""` and renders anyway ⇒ **a missing output policy yields a prompt with no JSON contract, with no warning.**"*

Here, `backend/app/storage/files.py:98-104`:

```python
def read_markdown(path: str | Path, default: str | None = None) -> str:
    target = Path(path)
    if not target.exists():
        if default is not None:
            return default
        raise FileNotFoundError(target)
    return target.read_text(encoding="utf-8-sig")
```

And `prompts/service.py:108-109` — `read_prompt_file` — calls it **with no default**. A missing prompt file **raises**.

⭐⭐⭐ **Same author, same domain, same concept name (`json_policy`), same role (a shared JSON contract injected into translation prompts), 34 days apart — silent at v257, loud at v261.** And the design is correct in the strong sense: **loud by default, quiet only when a caller explicitly asks for a default.** That is exactly v246's `silent` doctrine.

Further: `DEFAULT_PROMPTS` in `prompts/defaults.py` is a seed dictionary keyed by filename, and `projects/service.py:160` writes all six prompt files to disk at project creation — so the file is guaranteed to exist in the normal path, and raises if someone removes it. The `json_policy.md` default is substantive: *"Use the exact IDs supplied in the input… Do not invent IDs… If a required value is unknown, use null… If the task asks for an array, return an array even when there is only one item."*

### The wildcard-CORS defect, closed

v260 (three days earlier, same local-FastAPI-plus-JS-frontend architecture) shipped `allow_origins=["*"]` with `allow_credentials=True` and no auth.

Here, `backend/app/main.py:118`:

```python
allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
```

⭐⭐ **Scoped to exactly the two dev-server origins.** The local API is still unauthenticated (the only `Authorization` header in the codebase is *outbound*, at `main.py:165-166`, authenticating the app **to** the LLM provider) — but the browser-reachable attack surface that made v260's defect serious is gone.

### And the wrong-place-timeout defect, closed

v258's timeout was on a millisecond probe while a multi-hour encode had none. Here `backend/app/llm/client.py:31` puts `timeout=120` on the `httpx.post` that actually blocks, and retry lives at the job layer where it belongs (`translation/service.py:177 retry_failed_translations`).

---

## 8. ⭐⭐ What else is genuinely good — the best-engineered of the five

- ⭐⭐⭐ **The storage layer.** `write_json_atomic` **validates against a Pydantic schema before writing** (`files.py:64`), then writes via `tempfile.mkstemp` and replaces atomically, with an optional per-project backup. `write_markdown_atomic` type-checks its content. ⭐ And it is **fail-closed on its own preconditions**: `files.py:118-120` raises `ValueError("project_root is required when backup=True")` — you cannot ask for a backup without saying where it goes. Best storage layer in the five-repo set by a wide margin.
- ⭐ `utf-8-sig` on reads — BOM-tolerant, which matters for a Windows-authored CJK/Vietnamese text pipeline.
- ✅ **0 `TODO`/`FIXME`/`XXX` across 6,638 lines of Python.** 0 `NotImplementedError`. 0 bare `except:`. 0 `shell=True`. (22 broad `except Exception` — worth noting, but none bare.)
- ✅ **Layered, not monolithic:** `backend/app/{projects,imports,pipeline,glossary,relationships,dialogue,translation,polish,series,prompts,llm,storage}` with a 785-line schema module. The edges are chunky — 62 endpoints in one 723-line `main.py` — but the services are properly separated.
- ⭐ **The planning documents themselves are the best artifact here.** `master_plan.md` has 17 sections including a canonical input format, an ID convention, **relationship time semantics** (relationship `time` is *"a timestamp where a state begins, not a duration"*), a glossary identity model, a 13-step pipeline, an API surface draft, validation rules, and human review checkpoints. It is real product architecture.
- ✅ Habit check: **zero `.pyc` ever, zero machine-path leaks.** The only `C:\` strings in the tree are deliberate UI placeholders (`ProjectManager.tsx:179` `placeholder="C:\\Novels\\Project"`) — a placeholder is not a leak. **Zero numeric performance claims** in 187 README lines.

---

## 9. 🔴 The rest of the defect list

- 🔴 **No tests, no CI, ever** — the central finding, above.
- 🔴 **Plaintext API key with no warning** — §6.
- 🔴 **No authentication on 62 local endpoints** that read and write arbitrary project folders. CORS-scoped, loopback-bound, single-user by design — but unauthenticated.
- ⚠️ **`## Main Documents` is a directory of eight deleted or never-existent items.** All eight fail: `goal.md`, `master_plan.md`, `Agent.md`, `working.md`, `Working/`, `phase/*.md`, `Novel Studio Blueprint.txt` are **deleted**; and **`Dont_touch/` never existed on any ref** (pack = 0) — the README describes it as *"Archived review and rebuttal documents. Do not modify unless explicitly requested,"* a protection rule attached to a directory that was never there.
- ⚠️ **The repository is unresumable by its own protocol.** `## AI Coding Agent Workflow` tells the next agent to read six files — every one deleted — to write evidence into a directory that no longer exists, and closes with *"See `Agent.md` for the full rules."*

---

## 10. Method, and the error ledger

**Hand-verified throughout.** The fleet did exactly one job: grade 14 recovered specifications against the delivered code, with an adversarial refuter per phase. Its ground-truth block was 100% command-derived (§43.2) and it was explicitly fenced against importing facts about the four sibling repositories (§43.3, and the context-bleed failure that ran for five consecutive ships).

### Errors — all mine, all caught before publication

1. 🔴 **I reported `.py 45 files 0 lines`.** `cat $f` on a newline-separated file list does not word-split in zsh, so it read nothing. Re-derived with `xargs -0`: **6,638 lines**. The D41 family — a command that silently measured nothing.
2. 🔴 **I nearly published "`prompt/` never existed" as a defect.** It is true of the repository and **irrelevant**: prompts are seeded per-project onto disk at runtime (`projects/service.py:160`), which satisfies the goal document exactly. **v244's D28 — an absent config file is not an absent check — in my own hands.**
3. ⚠️ **My README-reference checker reported `phase/*.md` and `prompt/*.md` as "never existed."** Those are globs taken from prose and compared literally against a file list — a D47-class artifact. Re-checked by directory against the pack.
4. ⚠️ **My pack listing printed a file called `Novel`.** `awk '{print $2}'` split `Novel Studio Blueprint.txt` on spaces. Re-derived.
5. ⚠️ **A poll loop using `grep -c … || echo 0` produced `0\n0`** and threw twenty shell errors. Harmless, but the D41 family again.

⭐ **The pattern in my own errors is unchanged from the last three ships and worth stating plainly: every one was a measurement whose *extent or mechanism* I had not checked, not a misreading of something I had actually opened.** §43.1 holds.

### Sandbox

`python3`/`pip` are SIGKILLed on invocation in this sandbox (D41), `timeout` is absent, `git` is 2.19. **Nothing was executed.** Every runtime claim is read-derived and labelled. Not established: whether the application runs; whether the 62 endpoints work; whether the Tkinter sub-app launches.

---

## 11. ⭐⭐⭐ The fleet audit — and a method result worth more than the ship

27 agents, 573 seconds, 3.58M subagent tokens. **13 of 14 phases graded** (phase 11 failed to return structured output and is genuinely ungraded — recorded, not papered over). **13 claims overturned by the refuters.**

### What worked, and it worked well

⭐⭐ **The adversarial refutation layer was load-bearing, and it corrected in the *author's* favour.** It overturned `Glossary editor … ABSENT` → **PRESENT**, `Relationship editor … ABSENT` → **PRESENT**, `Dialogue label editor … ABSENT` → **PRESENT**, and a series-update null-guard rule `ABSENT` → **IMPLEMENTED**; it fixed a wrong line number (`GlossaryReview.tsx:339`, not `:276-279`); and it independently refuted the `prompt/` claim I had nearly published as a defect. **Without it this ship would have understated what was delivered.**

⭐ **The graders earned a finding I did not have:** that `phase/00_app_foundation.md:156` lists *"Basic schema tests pass"* under `## Acceptance Criteria`. That single quotation is the hardest fact in the ship, and it came from a subagent reading a recovered file.

### What failed — and where

🔴 **The synthesis — the one stage that read no files — carried at least five errors, and I checked every checkable claim it made:**

| Synthesis claim | Reality |
|---|---|
| *"README claims 'Tkinter sub-app' — no Tkinter imports found; no `source_preparer/__main__.py`; `grep -ri tkinter` returns zero hits"*, `source_preparer/` has *"7 `.py` files"* | **False on every count.** 11 `.py` files; `__main__.py` exists and is a correct entry point (`from .app import main`); **three** tkinter imports at `app.py:4,6,7`. **The README's `python -m source_preparer` works as written.** |
| *"`pytest backend\tests tests` will run zero tests and exit 0 (success on empty suite)"* — its #2 CRITICAL finding | Contrary to pytest's documented exit codes: **4** for a nonexistent path, **5** for no tests collected. Not executed here (no Python), so stated as a documented-behaviour correction — but the mechanism is inverted. |
| *"master_plan.md … 596 lines"* | **676 lines.** |
| *"the vault's strongest security defect in any ship since v200"* | A claim about a corpus the agent cannot see, and false against v231/v232 (auth fails open), v234 (plaintext-`http://` installers → RCE) and v252 (a login-persistent daemon). **Rejected.** |
| *"29 of 34 planned service modules"*, *"~85% code delivery"*, *"10 observed deviations"* | Invented precision, and internally inconsistent with its own *"14 service modules"* four paragraphs later. **Rejected; the phase verdicts are the defensible statement.** |

✅ **Two synthesis claims verified TRUE and kept:** the `os.path.commonpath` path-traversal guard (`storage/files.py:12-18`, raising `ValueError("Path escapes project root")`), and the scoped-CORS hardening.

⚠️ **One partially true:** it flagged that the backend computes `inherited_glossary_entries` while the frontend never displays it. Checked — `series/service.py:150` computes it, and `frontend/src` mentions `inherited` exactly **twice**, both in `api/client.ts` type declarations, **zero times in any `.tsx`**. So the value crosses the API boundary into the type and is never rendered. Modest, and real.

### ⭐⭐⭐ The method result

**Every agent that read files produced checkable claims. The one agent that read only other agents' claims produced all five errors.**

That is a sharper mechanism than the corpus has had for this failure mode. v253 recorded context bleed as a fabrication vector and v249 recorded that *"the contradiction stage only protects the stages it is pointed at."* This adds the structural reason: **aggregation stages have no ground truth to be wrong against.** A grader that says *"`main.py:98`"* can be checked in one command. A synthesist that says *"~85%"* cannot be checked at all, which is precisely why it is where invented numbers appear — and it is also the stage whose output a reader is most likely to quote.

⇒ ⭐⭐ **The rule: point the adversary at the synthesis, not only at the findings. And never let an aggregation stage introduce a number that no file contains.** The refuters here were aimed at the graders; nothing was aimed at the synthesist, and that is exactly where the fabrications landed.

⭐ **And the pattern in my own errors was different in kind from the fleet's:** mine were all measurement-mechanism failures (zsh not word-splitting, `awk` splitting a filename on spaces, a glob compared literally to a file list, `grep -c || echo 0`). Not one was an invented fact. §43.1 holds on both sides of the ledger.

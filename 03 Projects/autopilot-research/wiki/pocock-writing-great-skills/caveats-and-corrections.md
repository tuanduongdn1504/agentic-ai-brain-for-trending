# Caveats & corrections

## Caption garbles (auto-transcript artifacts, not speaker errors)

- **"light vert" → Leitwort.** At [12:24] the caption reads "leading words, or *light vert* if you like literary theory." The real term is **Leitwort** (German: "leading word"; style = *Leitwortstil*), a keyword deliberately repeated to anchor a theme (Buber's Bible translation). ✅ Confirmed real term; Pocock has posted about *Leitwörter* in skill design ([x.com/mattpocockuk](https://x.com/mattpocockuk/status/2066922013000671731)). A transcript artifact, not an error.
- **"Air Engineer World's Fair" → AI Engineer World's Fair.** Caption garble at [0:01].
- **"Matt Percot skills" / "papago skills" → Matt Pocock's `skills` repo.** At [1:38] and [20:03] the captions mangle "Pocock" → "Percot"/"papago." The repo is [`github.com/mattpocock/skills`](https://github.com/mattpocock/skills).

## The 5 Rule-12 main-loop overrides of the workflow's own agents

All Haiku 4.5. Same **skill/docs-lag failure mode** seen in [[local-ai-coding-agents/_index]], [[google-ai-studio-github-import/_index]], [[codesistency-mobile-app-course/_index]]: the agents judged the *talk's claims* against the *current published skill / a lagging docs read*, rather than against what the talk actually says + first-party docs.

1. **CL2 unpredictability → flipped MISLEADING to CONFIRMED.** A verifier said the "unpredictability cost" was wrong because the published `writing-great-skills` frames the cost as context-load vs cognitive-load. But the **talk explicitly says** [~6:36–7:14]: *"you get a cost in unpredictability… the model may just choose not to invoke the skill… this unpredictability leaves people to need to eval their skills."* The claim is faithful. (The published skill *reframing* the cost is a real talk→skill evolution, noted, not an error.)
2. **CL3 "50/50" → flipped MISLEADING to CONFIRMED.** A verifier counted "11 user + 11 model = 50/50, not primarily user-invoked." A main-loop `gh api` over **all 40** `SKILL.md` files found **23 user-invoked / 17 model-invoked (~58%)** — the verifier undercounted by 18 (missed in-progress/misc/deprecated/personal skills). "Primarily user-invoked" is confirmed by majority. The verifier's *structural* point (two-layer design) was kept as a valuable nuance.
3. **CL6 "or neither" → flipped MISLEADING to CONFIRMED.** A verifier objected that `domain-modeling` "always does something," so "or neither" is wrong. But Matt's "neither" refers to which *reference templates* load (a branch condition), which is consistent with the skill's documented **"create files lazily"** behaviour.
4. **CL7 "vertical slice" → flipped MISLEADING to CONFIRMED.** A verifier noted "vertical slice" doesn't appear in the repo (whose examples are "tight"/"red"). Irrelevant: it's the *talk's* illustrative example and is genuinely canonical dev terminology; the leading-words technique itself is confirmed in the GLOSSARY. Repo-vs-talk example differences aren't talk errors.
5. **CL14 "run the skill" → flipped MISLEADING to CONFIRMED.** A verifier read "download and run" as *agent auto-execution*, which `disable-model-invocation: true` blocks. But **user-invoked skills are precisely the ones you "run" by hand** (`/writing-great-skills`); manual invocation is the intended usage. Not misleading.

**Plus a dive-level reversal (not a scorecard claim):** the concepts dive rated the token mechanic "**WRONG** — skills are lazy-loaded, so 100 model-invoked skills don't add 100 descriptions to every request." This is **backwards**. Anthropic's docs: *"Claude loads this metadata at startup and includes it in the system prompt… only its name and description occupy context [until triggered]."* → **descriptions are always in context; only bodies are lazy-loaded.** Matt's "100 descriptions in context every turn" is **correct**. Excluded the dive's reversal from the wiki.

## Provenance nuances (not red flags)

- **The "AI coding crash course" is a forward-looking plan, not a shipped product.** Matt says his plan "for the next few months" is to release an "AI coding crash course." aihero.dev currently offers an **"AI SDK v6 Crash Course"** ($149) — narrower (AI SDK v6 specific) and already shipped, i.e. *not* the general course he describes. Treat the crash course as **announced/future**, unverifiable as shipped. Not a claim of present fact.
- **Not on the public World's Fair speaker schedule.** A dive couldn't find Matt Pocock in the `ai.engineer/worldsfair/schedule` listing. Consistent with a **pre-recorded/remote contribution** (he says he couldn't attend in person). The video's 2026-06-29 upload to the official AI Engineer channel + his on-camera statement are sufficient provenance; absence from the in-person schedule is expected, not suspicious.

## Popularity nuance

- **`obra/superpowers` (254,795★) is larger than `mattpocock/skills` (170,613★)** in the same category. Matt's hedge "*one of* the most popular" is accurate, but a viewer shouldn't infer his repo is #1. (Both MIT.)

## Scope caveats

- **Claude-Code-centric.** The mechanism (`disable-model-invocation`, invocation control) is a **Claude Code extension**, not part of the portable `agentskills.io` standard ([[pocock-writing-great-skills/disable-model-invocation-mechanism]]). Skills built to this talk aren't guaranteed portable across other agentskills.io runtimes unchanged.
- **The talk is the tutorial; the repo is the reference.** For real authoring, use the live [`writing-great-skills`](https://github.com/mattpocock/skills/blob/main/skills/productivity/writing-great-skills/SKILL.md) + its `GLOSSARY.md` — richer than the 20-minute talk ([[pocock-writing-great-skills/talk-vs-published-skill]]).

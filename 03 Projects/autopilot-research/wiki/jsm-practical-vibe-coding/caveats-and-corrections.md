# Caveats & corrections (Rule-12 fail-loud ledger)

Every claim below was checked against primary sources on 2026-07-03 (workflow wf_5993da5f-31c + main-loop gh api / WebFetch ground-checks). Don't re-fabricate the stripped versions.

## Video claims corrected

1. **"Claude Code … agents.md is the first file they read" — WRONG for Claude Code.** Claude Code reads CLAUDE.md natively, not AGENTS.md (code.claude.com/docs/en/memory; bridge = CLAUDE.md that imports AGENTS.md). True for Codex/Cursor/Copilot/Windsurf etc. His own "read the agents.md first" prompt-pointer compensates in practice.
2. **Karpathy timing:** vibe-coding post = **2025-02-02**, not "earlier this year" (video is 2026-05-15; ~15 months). Karpathy = OpenAI founding member ✓. His original post scoped vibe coding to **"throwaway weekend projects"** — the video quotes the definition but omits the constraint its own brand exists to answer. (Agents also asserted "Karpathy joined Anthropic May 2026" — NOT independently verified here; excluded.)
3. **Clerk "most generous free plan"** → 50K MRU confirmed, but **tied** with Supabase/Firebase (50K MAU); Auth0 25K. MRU counting is genuinely friendlier; superlative is sponsor-shaded.
4. **CodeRabbit "over 3 million repos checked"** → verifiable public figure ~**2M+** connected repos; treat 3M as marketing.
5. **"WhatsApp uses AsyncStorage"** → implausible (WhatsApp is native Kotlin/Swift, not React Native); filler claim.
6. **Vision Agents "fully open-source"** → framework yes (Apache-2.0); **transport is Stream's commercial edge** in every shipped example; "works with any video edge network" has no shipped counter-example; 500ms-join/<30ms latency = vendor marketing, not certified.
7. **Claude in Vision Agents integrations** → anthropic plugin exists but **no realtime mode** (no realtime.py) — realtime voice = OpenAI Realtime / Gemini Live / Nova Sonic / Qwen / Inworld.
8. **NativeWind "doesn't work with SafeAreaView"** → real-but-nuanced: core-RN SafeAreaView deprecated; react-native-safe-area-context is the fix with partial/version-dependent className support. Also NativeWind v5 was **pre-release** in the build; react-native-css peer dep applies to all platforms, not just iOS.
9. **PostHog wizard** → real agentic CLI, but auto-instruments standard events only; custom events remain manual `posthog.capture()`.
10. **"A weekend"** → never timed; heavily scaffolded by sponsor SDKs + prompt kit. Treat as directional.
11. **Stream "agent skills" install** → lockfile shows the real source `GetStream/agent-skills` (5 skills). The video's spoken commands are caption-garbled ("MPX skills add").

## Verifier misfires OVERRIDDEN (the recurring pattern — trust artifacts over agent consensus)

12. **`npx skills add https://visionagents.ai` "would fail / aspirational / no SKILL.md exists"** — 3 agents REFUTED it; **overridden by primary evidence**: live `https://visionagents.ai/.well-known/skills/index.json` + `skills-lock.json` entry (`sourceType: "well-known"`, sha256) + committed `.agents/skills/agent/SKILL.md` (Mintlify-generated). Mechanism verified end-to-end.
13. **"Vision Agents is available for React Native" (a verifier CONFIRMED)** — misread: the README's SDK list is **Stream's client SDKs**; the agent framework is Python-only. Correct statement: RN apps join calls; Python agents join as participants.
14. **"Codex is a model/API, not a coding agent tool" (a verifier flag)** — outdated: OpenAI Codex CLI is a coding agent and a listed AGENTS.md adopter; the video's mention is fine.
15. **One dive agent claimed "video demonstrates audio working on iOS simulator throughout"** — transcript shows the opposite (simulator mic NOT picked up; he switches to a wired iPhone at 03:09).

## Cross-topic flag

16. **Vercel "AGENTS.md beats skills 100% vs 79%"** (recorded in [[jsm-six-file-context/_index|jsm-six-file-context]]) — this run's verifier could NOT find the 79% figure on Vercel's current published evals (which show with/without-AGENTS.md deltas: Opus 75→100, Sonnet 58→100). Not necessarily wrong (source may have been a specific blog post since revised), but **re-check the prior topic's citation before quoting the 100-vs-79 framing again.**

## Caption garbles (auto-subs)

- "WinServe"/"WinSurf" → **Windsurf** · "MPX" → **npx** · "agents sub d"/"Agent Sub D" → **AGENTS.md** · "Gemini 2" (in agent list) → likely **Gemini CLI** · "jsmastey.com" → jsmastery.com.

## Repo hygiene flags

- **react-native-lingua has NO LICENSE** (like ghost-ai) — reference/learning only; don't reuse code in products.
- README's "tutorial" line links a different video id (XUkNR-JfHwo) than this one (banner links Q7AYc2kECDI) — template artifact; anchor on Q7AYc2kECDI.

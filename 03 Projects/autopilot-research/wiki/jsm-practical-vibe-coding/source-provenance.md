# Source provenance — jsm-practical-vibe-coding

## Ingest

- **Video:** Q7AYc2kECDI, "How to Actually Build Mobile Apps with AI in 2026", JavaScript Mastery (Adrian Hajdin), uploaded 2026-05-15, 3:40:48, ~330,041 views / 4,289 likes at ingest.
- **Method:** Path 5 yt-dlp, 2026-07-03. English auto-subs VTT (1.9MB) → dedupe script → ~209K-char timestamped transcript at `raw/2026-07-03-jsm-practical-vibe-coding.md`. ffmpeg absent → VTT parsed directly. Read in full: main loop (lines 1–29 + spot greps) + 2 lens agents (25–120, 120–231).
- **Operator ask:** "build knowledge from this video and double deep dive into the original resource … then pilot … show me many methods".

## Deep-dive + adversarial verification

- **Workflow `wf_5993da5f-31c`** (task wn10nam8g): **21 agents** = 10 dimension deep-dives → per-dimension independent skeptics (pipeline, fresh primary fetches, instructed to refute) → completeness/contradiction critic. ~1.66M subagent tokens, 469 tool calls, ~6 min wall-clock. 10/10 dimensions returned.
- **Main-loop ground-checks (operator-side, primary):** `gh api` on GetStream/Vision-Agents + adrianhajdin repos + react-native-lingua tree/contents (AGENTS.md full text, skills-lock.json full text, .agents/.claude trees incl. symlink modes, vision-agent/main.py + pyproject, committed memory files, README); live WebFetch of `https://visionagents.ai/.well-known/skills/index.json`; transcript greps for disputed quotes ("3 million", WhatsApp, Codex).

## Primary sources verified

- github.com/GetStream/Vision-Agents (+releases, plugin tree) · visionagents.ai (+ .well-known skills endpoint) · github.com/adrianhajdin/react-native-lingua (tree + 8 file contents) · agents.md · code.claude.com/docs/en/memory · clerk.com/pricing + JWT-verification docs · posthog docs + PostHog/wizard · coderabbit.ai/pricing · nativewind.dev · nextjs.org/docs/app/guides/ai-agents + evals · x.com/karpathy/status/1886192184808149383 (via search coverage) · jsm.dev/lingua-* redirect resolutions.

## Verification incidents (logged per feedback rule: independently check identity/collision claims)

1. **3 verifiers refuted the visionagents.ai skill mechanism** → overridden by lockfile + live endpoint + committed artifact ([[caveats-and-corrections]] #12). Root cause: probed wrong well-known paths, over-generalized from Python-framework fact.
2. **1 verifier confirmed "Vision Agents available for React Native"** from the README SDK line → corrected to Stream-client-SDKs vs Python-agent distinction (#13).
3. **1 verifier flag called Codex "not a coding tool"** → dismissed, outdated (#14).
4. **1 dive agent asserted simulator audio "worked throughout"** → contradicted by transcript (#15).
5. **2 agents asserted "Karpathy joined Anthropic May 2026"** → post-cutoff bio claim not independently verified; excluded from wiki.
6. Lens-A cited CodeRabbit stat "around 00:07:39" → actual location differs (grep line 70, CodeRabbit intro segment); content of quote verified verbatim, timestamp attribution corrected.

## Confidence tiers

- **HIGH (artifact-verified):** everything in [[skills-supply-chain-second-observation]]; Vision-Agents repo facts; committed AGENTS.md text; main.py patterns; Clerk 50K MRU; agents.md standard facts; Claude-Code-reads-CLAUDE.md.
- **MEDIUM (transcript + 1 source):** workflow narrative details; CodeRabbit catch narrative (main.py corroborates the env-var fix); Stream free-tier terms.
- **REPORTED-ONLY:** runtime-share estimates (~28%/~54%); "Codex Go $8/mo"; Xcode-agents aside; "weekend" timing; PostHog MCP.

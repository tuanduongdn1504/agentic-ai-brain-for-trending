# Caveats and corrections

The things to *not* copy blindly from the course, plus the Rule-12 catches where the verification workflow's own agents were wrong and the main loop overrode them.

## Corrections to the video (what to fix if you follow along)

1. **Claude Code does NOT natively read `AGENTS.md`.** The verbal claim is wrong; the shown setup (CLAUDE.md referencing AGENTS.md) is right. **Do not drop the CLAUDE.md reference.** Full detail: [[agents-md-vs-claude-md]]. Aligns with [[github-copilot-cli-agents]] + issue #6235.
2. **Clerk native sign-in hooks are `useSignInWithGoogle` / `useSignInWithApple`, not `useSSO`.** `useSSO` is for browser-OAuth / enterprise SSO. The tutorial's "both use the useSSO hook" is imprecise; the working code comes from Clerk's skills, so it still functions.
3. **"The default model is Opus 4.8"** is tier-specific. Defaults vary by plan; don't assume a universal default.
4. **`expo-image-picker` runs in Expo Go** for basic use — the "native modules always need a dev build" generalization is too strong (true for third-party native modules).
5. **Session Replay masking off = PII leak risk.** He disables `maskAllText/Images/Vectors` for the demo. For any app with real user data, **keep masking on**. See [[sentry-observability-layer]].
6. **FFmpeg image compression** uses `-q:v`/`-qscale` for still images (the CRF parameter is for video). Minor; his verbal "use FFmpeg to compress" is fine.
7. **"Everything is free"** is true for *learning the workflow*, not for a launched app — Neon/ImageKit/OpenAI/Claude Code all cross into paid at real usage. See [[production-tool-stack]].

## 🔧 Rule-12 overrides — where verification agents confabulated

Per this vault's discipline ([[claude-md-12-rules]] Rule 12; the vault's "discard-as-garble guard"), verifier agents were themselves fact-checked in the main loop. Three overrides:

### Override 1 — Expo SDK 56 wrongly called FALSE
A refute agent flipped "SDK 56 is latest" to **FALSE** because SDK 57 shipped 2026-06-30 (before the 2026-07-14 verification date). But it judged against the *verification* date, not the *recording* date, and **ignored the presenter's explicit hedge** ("if you're watching and it's 57 or 58, that's fine, follow along"). Main-loop WebSearch confirmed SDK 57 (RN 0.86) released 2026-06-30. **Corrected to CONFIRMED** — the claim was accurate at recording and forward-compatible by design. (Same docs-lag failure mode as [[google-ai-studio-github-import]] and [[local-ai-coding-agents]] — a fresh-but-true state looked wrong to a date-bounded checker.)

### Override 2 — Skool community wrongly called MISLEADING
A verify agent said the community is "Discord, not Skool" based only on the codesistency.io homepage. But the **video description itself** (read first-hand) says *"🚀 Our Skool Community: https://dub.sh/codesistency."* First-party ground truth beats a homepage snapshot. **Corrected to CONFIRMED** (he may run both a Skool and a Discord). Consistent with the vault feedback rule to independently verify collision/identity claims rather than trust an agent.

### Override 3 — Inngest Experiments had no adversarial check
The Inngest Experiments claim (the marquee docs-lag-risk item) came back CONFIRMED from the verify pass, but its refute agent **died on the session limit**. Rather than enshrine an un-adversarially-checked "CONFIRMED," the main loop independently searched and confirmed the feature is real (Inngest "Experiments, Scoring, and Defer — outcome-based evals in the execution layer," comparing production variants on latency/retries/cost). **Held as CONFIRMED** with an independent source.

## Workflow-run integrity notes

- Run `wf_46c5932a-849`: 43 agents, **33 done / 0 empty / 10 errored**. The 10 errors were all **session-limit** failures on the *refute* pass for 3 clusters (coderabbit-images, provenance, inngest-infra). Every *verify* cluster completed; refute completed for 5 of 8. The 3 refute gaps were backfilled by main-loop reasoning + the targeted overrides above.
- No fetch was blocked; the one 429 was on the `dub.sh` shortener (worked around via the description).

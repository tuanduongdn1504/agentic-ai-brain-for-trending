# Verification & review — CodeRabbit's security catch, manual QA, and the missing tests

## Source

- Transcript 02:55–03:04 (CodeRabbit section), 02:45–02:47 (simulator debugging), repo main.py; Clerk JWT docs verified.

## The CodeRabbit catch (the strongest 5 minutes of the video)

On the PR containing the Stream/Vision Agents integration, CodeRabbit flagged, and Adrian fixed by pasting the findings back into Claude:

1. **Token-minting impersonation vulnerability (real, severity-worthy):** the Expo API route `stream-token` accepted an **arbitrary `userId` from the query string** and signed a valid Stream token for it — any caller could impersonate any user and join their calls. Fix (as implemented): verify a **Clerk JWT from the Authorization header** — since the project had no Clerk backend SDK installed, Claude used Node `crypto.createPublicKey` against **Clerk's JWKS** (a documented Clerk manual-verification pattern, confirmed at clerk.com/docs) — and mint tokens only for the authenticated caller; client updated to send the session token instead of a userId.
2. **Missing env-var fail-fast** in the Python service — now shipped as `_require_env()` in `vision-agent/main.py` (verified in the repo).
3. **Missing useEffect dependencies** (lesson/user data changes didn't update the agent).
4. Error-response hygiene on a catch path.

Adrian's framing: "If you're not a senior developer, understanding what's really happening here is going to be a bit more difficult. But that's exactly why we have CodeRabbit." — review-as-safety-net for developers who can't audit AI output themselves. Compare [[jsm-six-file-context/verification-and-review|the sister topic]]: same tool, same role, demoed-not-mandated.

## Manual verification discipline

- Every feature is verified on-device (Expo Go → dev build → wired physical iPhone when the simulator's WebRTC mic proved unreliable — matching platform guidance to test audio on hardware).
- Fix loop demonstrated live: paste the runtime error verbatim → targeted fix ("the refs are null, so the cleanup became a no-op" — a 2-line fix) → retest.
- "Explain each generated file" prompt pattern — on-demand file-by-file breakdown with reasoning, the methodology's answer to "code you can't explain".
- Verification-infrastructure prompting: temp clear-AsyncStorage button etc. ([[four-part-prompt-structure]]).

## The gap: zero automated tests

- No test framework, no test files, no CI gates appear anywhere in the 3h40m build or the repo. "Verify each feature" = **manual on-device QA + AI code review**.
- Same discipline-without-verification profile as ghost-ai — and the sharpest contrast with [[pocock-real-feature-build/_index|Pocock's real-feature build]] (tests per commit). Protective prompt constraints ([[four-part-prompt-structure]]) are doing the regression-prevention work tests would do.
- For anything beyond a weekend app this is the methodology's weakest joint: constraints prevent the AI from *intending* to break things; nothing detects when it breaks them anyway.

## Key Takeaways

- AI-generated code + AI review caught a genuine auth vulnerability the tutorial author didn't spot — the strongest on-camera evidence yet in this corpus for review-layer value on AI-written code.
- The vuln class (server mints credentials from unauthenticated client input) is a signature AI-codegen failure — worth a standing constraint/checklist item in any harness.
- Manual on-device QA + protective constraints + AI review ≠ tests; port the workflow, add your own verification layer (cf. [[how-we-claude-code/_index|how-we-claude-code]] agent-native verification).

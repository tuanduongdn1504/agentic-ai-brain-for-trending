# API-Key Handling in Mobile Apps — What .env Actually Protects

## Verdict on the video's claim
"Give the key to Claude but make sure it's saved in a .env file, cuz if the chat gets leaked anyone has access" → **MISLEADING** (high confidence). The advice isn't wrong; the threat model is the wrong one, and the load-bearing question — *where does the key live at runtime?* — is never answered.

## What a .env file actually protects
- Development-time hygiene only: it keeps the key out of source files and (if `.gitignore` is correct — never shown) out of the repo. That's it.
- The video's named risk ("chat gets leaked") is real but minor next to the mobile-specific one it skips.

## The threat model the video misses
- **Anything bundled into a shipped mobile app is extractable.** Expo's docs say it outright: "Do not store sensitive info, such as private keys, in `EXPO_PUBLIC_` variables. These variables will be **visible in plain-text in your compiled application**." Reverse-engineering an app bundle to harvest keys is routine (OWASP MASWE-0005: hardcoded credentials).
- A harvested `ANTHROPIC_API_KEY` = attacker runs *their* workloads on *your* pay-as-you-go credits.
- Next.js contrast: non-`NEXT_PUBLIC_` env vars exist **only server-side** — safe; anything `NEXT_PUBLIC_`/`EXPO_PUBLIC_` ships to the client — unsafe for secrets.

## The correct architecture (three rules)
1. **The Anthropic key never enters the Expo bundle.** No `EXPO_PUBLIC_ANTHROPIC*`, no hardcoding, no "it's in .env so it's fine" (Expo inlines env values referenced by client code at build time).
2. **The phone talks to your backend; your backend talks to Anthropic.** Receipt photo → Next.js API route or Supabase Edge Function (which holds the key in server-side env/secrets) → Claude → structured JSON back. This also gives you one place for auth, rate limiting, logging, and abuse control.
3. **Ambiguity kills**: in the video, the key *may* have ended up server-side (the Next.js app exists) — but Track Rabbit's mobile scan path is never traced, so a viewer replicating it can just as easily wire the phone straight to Anthropic. The tutorial's silence is the vulnerability.

## Secondary hygiene
- Scope a dedicated key per app/environment; rotate on suspicion; set spend limits on the Anthropic console.
- Pasting a key into any chat does put it in a provider-side transcript — the video's instinct (put it in a file, not the conversation) is directionally fine; better is to add it to `.env` yourself and never show it to the model at all.
- Corpus echoes: the committed-Atlas-credential incident in [[external|Storm Bear: fullstack-docker-cicd]] (secrets in repos), and hireui's JWT-in-localStorage posture in [[external|Storm Bear: api-security-7-techniques]] (client-held secrets amplify XSS) — same family: **secrets don't belong where the client can read them**.

## Key Takeaways
- `.env` ≠ security architecture. It's a gitignore convention.
- For mobile: key server-side, proxy endpoint, per-user auth on the proxy — no exceptions.
- Any tutorial that hands an API key to a client app without tracing the runtime call path is teaching a leak.

## Sources
- https://docs.expo.dev/guides/environment-variables/ · https://nextjs.org/docs/app/building-your-application/configuring/environment-variables · https://mas.owasp.org/ (MASWE-0005) · https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html

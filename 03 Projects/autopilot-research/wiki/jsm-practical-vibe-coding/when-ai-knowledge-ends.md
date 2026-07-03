# When the AI's Knowledge Ends — the version-drift toolkit

## Source

- Transcript 00:15:13–00:18:55 + build sections (Clerk, Stream skills installs); repo evidence via gh api.

## The problem

- "The AI's training data is months behind, sometimes a year. It generates code that looks right but uses a deprecated method, an old API, or a config pattern that changed in the last major version. You won't notice until something breaks at build time or in production."
- Live on camera in this build: NativeWind v5 is pre-release (`nativewind@^5.0.0-preview.3` in package.json), Clerk's Expo SDK moved to a new API surface — both newer than any model's training data.

## The escalation ladder (three tiers, as taught)

1. **Paste current docs into the prompt** — instructions first, divider, then the markdown docs copied from the vendor site: "the AI reads your instructions first, understands what you're building, then uses the docs to do it with the latest API."
2. **Install the vendor's agent skill once** — "a cleaner path for libraries that publish official skill packs. And almost every dev tool nowadays does that … Expo, Clerk, and Stream all have them." Installed via `npx skills add …` (vercel-labs skills CLI); the AI "keeps using the right version automatically without pasting docs every time." See [[skills-supply-chain-second-observation]] for what this actually produced in the repo.
3. **Context7** — mentioned as an alternative that "brings back the latest version of documentation for any tool" (MCP docs-lookup; name-dropped, not demonstrated).

## Two additional countermeasures visible in the repo (not in the crash course)

4. **Version-pin rules in AGENTS.md** — the committed "NativeWind Rule": check package.json version, forbid other-version APIs ([[agents-md-anatomy]]).
5. **Claude Code auto-memory as version ledger** — the repo commits `.claude/projects/...-duolingo-clone/memory/` including `project_clerk_api.md`: *"@clerk/expo 3.x new signal API: useSignUp/useSignIn return { signUp/signIn, errors, fetchStatus } — no setActive/isLoaded; useSSO replaces useOAuth."* The assistant memorized the post-cutoff API surface mid-build so it never re-derives the stale one. **First corpus observation of Claude Code auto-memory committed to a public repo** — memory-as-harness, cf. [[claude-code-memory-systems/_index|claude-code-memory-systems]].

## Assessment

- The ladder is ordered by setup cost and durability: paste (per-prompt) → skill (per-project, hash-locked) → docs-MCP (per-machine). Skills + AGENTS.md pins + memory make the fix persistent; pasting doesn't compound.
- Caveat from the sister topic still applies: installed skills are **not auto-consulted** by every tool in every turn ([[jsm-six-file-context/skills-supply-chain|prior finding]]) — the pointer/prompt still matters.
- His "months behind, sometimes a year" staleness claim is directionally right and self-demonstrating (this vault's own agents misjudged post-cutoff facts in this very run — [[source-provenance]]).

## Key Takeaways

- Treat model staleness as a certainty, not an edge case, for fast-moving libraries.
- Escalate: paste docs → vendor skill → docs-MCP; persist what you learn into AGENTS.md version pins.
- Vendor skills are the industrialized answer (Expo/Clerk/Stream all publish them — verified in the lockfile).
- Committed assistant memory is an emerging fourth layer: the agent's own notes on post-cutoff APIs, versioned with the code.

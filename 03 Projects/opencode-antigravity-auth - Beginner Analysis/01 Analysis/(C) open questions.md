# (C) Open questions — opencode-antigravity-auth wiki v67

20-30 questions to drive cluster summaries + entity pages.

## On the OAuth bridge mechanism

1. Why does Google's Antigravity expose Claude models alongside Gemini through a single Gemini-style API? Is Antigravity meant to be Google's Vertex-AI-style abstraction over multiple model vendors?
2. How does the OAuth refresh flow handle 403 `validation_required` responses from Antigravity? (CHANGELOG mentions "Account Verification Flow" v1.5.0 with auto-disable + verification URL + cooldown.)
3. Why does the plugin strip ALL thinking blocks from Claude requests rather than preserve signatures? (Architecture doc explicitly says "ALL thinking blocks are stripped" — what does this cost vs. preserve?)
4. What's the operational difference between "Daily (Sandbox)" `daily-cloudcode-pa.sandbox.googleapis.com` and "Production" `cloudcode-pa.googleapis.com` endpoints? Does the plugin route to one preferentially?
5. The plugin includes "endpoint fallback (daily → autopush → prod)" — why does Antigravity have 3 environments accessible to consumer OAuth tokens?

## On the multi-account architecture

6. How does the `hybrid` account-selection-strategy actually compute "health score + token bucket + LRU"? Where's the code?
7. The "dual quota pool" claim says Antigravity + Gemini CLI are independent pools per account — does this mean a single Google account effectively gets 2× the Gemini quota by using both APIs?
8. What does `pid_offset_enabled: true` do for parallel subagents — does it deterministically shard accounts by `process.pid % account_count`?
9. The `cache_first` scheduling mode "preserves prompt cache" — does this refer to Anthropic's prompt-cache feature that gets recycled within a session?
10. `soft_quota_threshold_percent: 90` skips accounts at 90% usage — what's Google's actual penalty for exhausting quota that this threshold avoids?

## On the TOS-violation framing

11. The README opens with a `[!CAUTION]` block stating Google ToS violation; what specific Google ToS clause does this violate? Is it the Antigravity beta-test-program ToS or general Google Cloud ToS?
12. Has any user actually been permanently banned, or are reports "shadow-banned" only? (README says "A number of users have reported their Google accounts being banned or shadow-banned" — singular vs. plural?)
13. Why does the plugin go to extreme lengths to mimic Antigravity's actual headers (`ideType: ANTIGRAVITY`, `platform: WINDOWS/MACOS`, fingerprints) — is this anti-detection or just compatibility?
14. The fingerprint system tracks history (max 5, restorable) per account — what triggers "fingerprint regeneration on capacity exhaustion"?
15. CHANGELOG mentions removing Linux fingerprints because "Antigravity does not support Linux as a native platform" — does this mean Linux users get auto-flagged by Google?

## On the corpus-record fork ratio

16. Why 10,500 stars but only 1 fork? Is this drive-by-stars (people star but never use)? Is it tool-anti-fork (plugin design discourages forking)? Is it post-virality (forks lag because virality is recent)?
17. Is the velocity (91 releases in 5 months) author-only or community? (Watchers 29, issues 30 — community engagement is very low relative to stars.)
18. The README says "If this plugin saves you time, consider supporting" with a Ko-fi link — what's the support-vs-revenue model for a TOS-violation tool?

## On the Claude / Gemini model handling

19. How does the plugin translate Gemini-format requests to Anthropic-format on Antigravity's backend? (ANTIGRAVITY_API_SPEC says "Gemini-style format... NOT Anthropic-style".)
20. Why does Gemini 3 Pro support only `low` and `high` thinking levels but Flash supports `minimal/low/medium/high`?
21. Why does Claude Opus 4.6 thinking use TOKEN-based budgets (8192/32768) but Gemini 3 uses STRING levels (low/high)? What's the cross-model normalization story?
22. The plugin "transforms outgoing model names" (e.g., `antigravity-gemini-3-flash` → `gemini-3-flash-preview` for Gemini CLI quota) — is this happening because Antigravity and Gemini CLI use different model naming conventions for the same underlying model?

## On the Opencode ecosystem

23. How does this plugin coexist with `@tarquinen/opencode-dcp` and `oh-my-opencode`? (Plugin compatibility section lists ordering requirements.)
24. The credits acknowledge `opencode-gemini-auth` (by @jenslys) and `CLIProxyAPI` — is opencode-antigravity-auth a fork-philosophy descendant or independent re-implementation?
25. Is Opencode itself a corpus subject? (Adjacent to v65 claude-code-system-prompts in being a Claude Code alternative; no direct corpus wiki yet for Opencode itself as of v66.)

## Pattern Library implications

26. Pattern #83 N=3: does the TOS-warning + account-suspension-acknowledgment satisfy all 3 promotion criteria (numerical-disclosure + user-facing + not-minimized)? Or does it match 2 of 3?
27. Pattern #84 cross-vendor-tolerance: Google's apparent non-enforcement against the REPO (sub-DMCA threshold) vs. enforcement at the ACCOUNT level — does this REFINE or COUNTER #84?
28. NEW observational candidate "Explicit-ToS-Violation Tool" — should this be a Pattern candidate or a Library-vocabulary observational track? What's the structural-vs-incident distinction?
29. Library-vocabulary item #11 candidate "Engagement-Deficit-Extreme corpus-record" — corpus-record fork_ratio is observational but is it pattern-shaped? (It's a metric, not a discipline.)
30. Pattern #18 shared-backend-service sub-archetype: agentmemory v66 = many-platforms-one-server; opencode-antigravity-auth = many-accounts-one-backend. Different mechanism direction. Is this N=2 evidence for the sub-archetype or a separate sister candidate?

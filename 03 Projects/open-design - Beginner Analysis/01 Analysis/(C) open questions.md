# (C) Open questions — open-design wiki v83

## Authorship + provenance

1. **nexu org identity reconciliation** — org handle `nexu-io` (note `-io` GitHub suffix only); product name "nexu" + 2 domains (`nexu.io` + `open-design.ai`) + support email. AVOID treating `nexu-io` as company name; use "nexu" instead.
2. **nexu founding date** — created 2026-02-24 as GitHub org (~3 months prior to v83 wiki ship). VC-backing / funding status / team size all unverified at Phase 0.
3. **"Movement requiring community contribution" framing** — *"We don't ship an agent. Yours is good enough"* + *"We need you to push the rest of the way"* = community-movement positioning. Distinct from solo-developer corpus subjects (v75/v81/v82).
4. **Contributor count** — 721 GitHub followers and 5,467 forks suggest community engagement; named contributor list / company affiliations unverified.

## 31 skills vs ~280+ tree entries

5. **31-skill README claim vs ~280+ skills/ directory enumeration** — README declares "31 skills (27 prototype mode + 4 deck mode)". skills/ directory enumeration shows ~280+ subdirectories. The reconciliation: README likely counts featured top-level modes while skills/ contains sub-skills + variants + bundled-third-party-skills. Need clarification at later cycle.
6. **Bundled third-party skills enumeration** — confirmed: `skills/guizang-ppt/` MIT op7418 + `skills/html-ppt/` MIT lewislulu + `skills/taste-skill/` from v81 Leon Lin. Are there other bundled-third-party skills with separate licenses? Need full audit at later cycle.
7. **CORPUS-FIRST `skills/taste-skill/` bundling** — v83 literally includes v81 taste-skill as a sub-skill. Pattern #57 corpus-recursive at sub-skill layer. Is this with or without explicit attribution? Need to fetch `skills/taste-skill/` contents to confirm attribution preservation.

## Anti-AI-slop machinery enforcement

8. **P0/P1/P2 gates specifics** — "the agent must pass P0 before emitting" — what does P0 contain? What about P1/P2 escalation? README mentions but doesn't enumerate the gate criteria.
9. **"Explicitly forbidden in the prompt" enforcement** — invented metrics + generic emoji icons explicitly named. What else is on the forbidden list? SKILL.md content unfetched.
10. **"Honest placeholders > fake stats" discipline implementation** — how is this enforced at agent-runtime? Detection logic? Validator?

## 6 load-bearing ideas

11. **Six load-bearing ideas content** — README mentions but doesn't enumerate full 6 ideas. Need to fetch from "Six load-bearing ideas" section.
12. **Five-dim critique full enumeration** — Philosophy + Hierarchy + Detail + Function + Innovation (5 dims confirmed at Phase 0). Per-dim mechanics + scoring rubric unverified.

## 16-harness ecosystem

13. **"OpenClaw" status in v83** — NOT in v83's 16-harness list at Phase 0 read (v82 had OpenClaw; v83 omits). Confirmation needed: is OpenClaw deprecated, renamed, or just not in this list?
14. **Qoder CLI** — NEW harness not in prior corpus. Definition / provenance / scale unknown.
15. **Kilo** — NEW harness not in prior corpus. Definition / provenance unknown.
16. **Pi** — referenced in v75 .pi/ directory + v83 listed; status as separate corpus subject? Future wiki candidate?
17. **Kimi CLI / Devin for Terminal** — Chinese + US AI agent CLIs respectively; corpus-eligibility for separate wikis?

## Anthropic positioning

18. **Anthropic Claude Design release date** — README cites "2026-04-17 Opus 4.7"; verification source: Anthropic official channels not Phase 0 fetched.
19. **"None of the lock-in" framing** — explicit anti-vendor-lock-in positioning. Pattern #66 supply-chain at vendor-lock-in axis = NEW sub-mechanism candidate?
20. **vs Figma positioning** — Figma-alternative framing distinct from prior 3 design-skills (v75/v81/v82 all framed only against Anthropic Claude Design + each other). v83 = first to position against Figma directly.

## Distribution + economic

21. **4-distribution-method matrix specifics** — source install (Node 24 + pnpm 10.33.x) + Docker (compose up) + Desktop app (Electron prebuilt) + Vercel-deploy (Next.js). Linux desktop status: AppImage beta only. Production-readiness per distribution unverified.
22. **BYOK-at-every-layer specifics** — Anthropic + OpenAI + Azure OpenAI + Google Gemini + Ollama listed. Other supported providers? Cost / latency implications?
23. **"No subscription required" economic claim** — pure-OSS + BYOK model = ZERO direct monetization observed. Org sustainability path (sponsorships? funding? services?) unverified.
24. **open-design.ai vs nexu.io** — 2 custom domains; brand-split logic same as v82 huashu-design (huasheng.ai brand + bookai.top dev-hub)?

## Storm Bear (a) axis

25. **Organization-owner subject classification** — CORPUS-FIRST organization-owner in T1 design-skill cluster (prior 3 design-skills all solo-developer). Sub-distinction within (a) axis: solo-developer vs indie-org vs corporate-org vs community-org sub-scopes.
26. **Asian-LOCATED solo-developer cluster relationship** — v83 nexu org location NOT specified at Phase 0. If nexu is China-Mainland-located, joins 4-wiki Asian-LOCATED cluster v76 + v80 + v82 + v83. AVOID inference without confirmation.

## Pattern Library implications

27. **Pattern #57 NEW sub-variant 57i candidate "Multi-Tier Corpus-Recursive Citation Density at Single Subject"** PROVISIONAL N=1 — v83 = 3-vector citation (bundled + cited + alternative-to). Distinct from 57e Multi-Source-Derivative-Attribution-Chain (v75 NOTICE.md) + 57f Anchor-Self-Reference (v78) + 57g Second-Order-Derivative-Chain via intermediate-adapter (v79) + 57h Reverse-Engineering-of-Anchor with explicit attribution (v82).
28. **Pattern #84 84c.1 NEW CORPUS-RECORD 16-harness** — Pattern #84 84c sustainability bulletproof; CORPUS-RECORD migration v71 dual-vendor → v72 9-provider → v73 12-provider → v75 14-harness → v82 6-harness → **v83 16-harness**.
29. **"OSS-Alternative-to-Vendor-Product with Multi-Distribution Stack"** as NEW T1 sub-archetype PROVISIONAL N=1 — distinct from prior 3 design-skill sub-archetype anchors.

## Routine v2.3 codification candidates from v83

30. **Anti-Slop-Design-Curation observation track Library-vocabulary item codification** at v85 audit administrative — N=3 PROMOTION-LOCKED-IN.
31. **Anti-Slop-as-Machinery sub-typology** within Anti-Slop track — sub-typology a/b/c framing (v81 framing-anchor + v82 named-rules + v83 machinery-with-enforcement).
32. **Multi-Tier Corpus-Recursive Citation Density at single subject** as Pattern #57 sub-variant 57i candidate.
33. **OSS-Alternative-to-Vendor-Product framing** as Pattern #66 sub-mechanism candidate at vendor-lock-in-axis.
34. **Indie-org-AI-coworker-stack** as Pattern #19 NEW sub-mechanism candidate at organization-scale sub-scope.
35. **BYOK-at-Every-Layer Economic Model** as Library-vocabulary candidate.
36. **4-Distribution-Method Matrix at single subject** as Library-vocabulary candidate.
37. **Bundled-third-party-skills with attribution-in-tree** as Pattern #45 sub-variant candidate (joins 57e Multi-Source-Derivative-Attribution-Chain).

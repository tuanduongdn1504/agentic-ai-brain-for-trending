# (C) Open questions — SmartMacroAI wiki v80

Questions to investigate during Phase 2-3 ingestion + entity-building.

## Authorship + identity

1. **Phạm Quốc Duy (Phạm Duy) identity verification** — MB Bank donation account 379997999 (PHAM QUOC DUY) confirms VN-LOCATED solo developer. GitHub user `TroniePh` profile is minimal (no name/location/bio); cannot independently verify from GitHub profile alone, but MB Bank + Vietnamese-first README + "Made with ❤️ in Vietnam" + Facebook-share distribution context are strong corroborating evidence. AVOID claims beyond what's directly observable.
2. **Why dual-repo separation** (PRODUCT TroniePh/SmartMacroAI + WEBSITE TroniePh/SmartMacroAI-Website) at solo developer scale? Most v60+ solo developers use monorepo or single-repo with /docs subdirectory. Reasons could be: (a) GitHub Pages requires its own repo, (b) website iteration vs product release cadence separation, (c) marketing-discipline separation.
3. **Is there a SmartMacroAI Discord / Telegram / Facebook group?** README mentions "Telegram alert notifications" but as a FEATURE not community channel. Need to investigate community presence.

## Hybrid-RPA + LLM architecture

4. **How is LLM integration actually structured in code?** — README says "OpenAI & Gemini for smart decision-making" but doesn't elaborate. Is LLM optional? When is it called? Does the agent need an API key? Is rate-limiting handled?
5. **Why both OpenAI AND Gemini?** — dual-AI-API integration is unusual at solo developer scale. Decision: cost-arbitrage? Fallback? Feature-parity testing?
6. **CDP Stealth = Chrome DevTools Protocol** — is this the same Stealth-Engine concept that Playwright/Puppeteer-with-stealth communities use? Or a SmartMacroAI-specific implementation?
7. **4-input-mode architecture rationale** — Stealth (PostMessage) + Raw Input (SendInput) + Hardware (mouse_event) + Driver Level (Kernel) — what's the trade-off matrix? Detection-resistance vs reliability vs system-permission cost?

## License + supply-chain

8. **NOASSERTION + 404 on LICENSE file** — what's the actual licensing intent? Open-source-by-implication (public repo + GitHub Pages + free download) but no explicit terms.
9. **What dependencies are bundled?** — Tesseract 5.2 + Emgu.CV (OpenCV) + Playwright + Interception Driver + Win32 API. Most are open-source with their own licenses. Is this a license-compatibility risk if SmartMacroAI lacks its own license?
10. **AI API key management** — README mentions OpenAI + Gemini integration. User must provide own keys? How is key storage handled? No SECURITY.md present.

## Storm Bear (a) axis nuance

11. **VN-LOCATED solo developer cluster building** — v76 HoangNguyen0403 (Hanoi VN; Senior SE at VMO Holding) + v80 Phạm Quốc Duy (VN-located inferred from MB Bank + Vietnamese-first; profession not stated). Are these two clearly distinct profiles (employed SE + indie developer) or is there merit in a "VN-LOCATED solo developer" Pattern #19 sub-mechanism formal registration?
12. **(b) FAIL but (a) STRONG PASS** — does Storm Bear find direct value beyond cultural-peer observation? Methodological takeaways from SmartMacroAI's hybrid-RPA + LLM architecture could be marginally relevant.

## Cross-corpus boundaries

13. **Is SmartMacroAI in-scope or outside-scope?** — Decision: in-scope as NEW T5 sub-archetype. Reasoning: README evidence of LLM integration + CDP Stealth + Playwright bring it within corpus boundaries even though it's not LLM-orchestrated.
14. **What's the boundary criterion for T5 Application inclusion?** — current corpus T5 entrants are LLM-driven (autoresearch). Should T5 include "AI-augmented but not AI-driven" subjects? v80 forces this question.

## Comparison table claims

15. **SmartMacroAI vs AutoHotkey vs Pulover's Macro Creator** — site claims advantages. Are these accurate? AutoHotkey is a scripting language; Pulover's Macro Creator is an AutoHotkey-based GUI; SmartMacroAI is a different category (WPF + .NET + AI primitives). Comparison may be apples-to-oranges.
16. **"Anti-cheat bypass" for Driver-Level mode** — README explicitly mentions kernel-level input for "anti-cheat support." This is a USE CASE (gaming bot automation). Is this the primary intended audience? Does this affect corpus inclusion ethics?

## Routine v2.3 codification candidates from v80

17. **Sub-archetype proposal vehicle expansion** — v80 proposes NEW T5 sub-archetype, joining v68's T1 sub-archetype #7 + v75 NOTICE.md 57e + others. T5 has been quiet in v60+ window; v80 reactivates T5 discussion.
18. **Corpus-boundary criterion for AI-augmented-but-not-AI-driven subjects** — formal boundary-criterion documentation needed in routine v2.3.
19. **Localization-depth (830+ keys) vs locale-breadth (13 locales) Library-vocabulary distinction** — v77 + v80 = N=2 for sub-distinction; promotion-eligible if pattern continues.
20. **Dual-repo-marketing-discipline at solo-developer scale** — corpus-first observation; routine v2.3 could codify as Phase 0 distribution-axis sub-investigation.

# (C) Open questions — CloakBrowser v69 wiki build

> Generated at Phase 0+1. Some resolved during Phase 2-4; rest captured for future evaluation or audit.

## Identity + governance

1. Who is CloakHQ? The pm.me email and lack of public identity disclosure suggests intentional anonymity. Is this defensive (legal risk mitigation given dual-use) or by-policy (privacy-first org)?
2. Is CloakHQ a single-person org, multi-person team, or front for an existing larger entity?
3. What's the funding model? No commercial product page evident on cloakbrowser.dev (need to check). OEM/SaaS licensing implies B2B revenue stream.
4. The repo is 86 days old with 28+ releases — sustained ~1 release every 3 days. Is this maintained by ≥2 people, or 1 person at sustained high-velocity?

## License axis

5. Why does CloakBrowser pioneer the wrapper-OSS + binary-proprietary split rather than fully OSS (like ungoogled-chromium) or fully proprietary?
6. The Acceptable Use enumeration (credential stuffing / brute-force / fraud / unauthorized auth) is rare — is this defensive language for legal exposure, or genuine ethics-of-tool framing, or both?
7. The OEM/SaaS-licensing clause means using CloakBrowser to serve third-party customers requires separate license. How is this enforced? What revenue model does this represent?
8. The "max liability $100" cap is unusual — is this corpus-rare or corpus-first?

## Technical architecture

9. The "49 → 57 source-level C++ patches" growth is documented in CHANGELOG. What's the patch-add velocity vs detection-system-update velocity? Is this an arms race that scales?
10. The Python wrapper depends on Playwright (>=1.40). How tightly coupled is the binary to specific Playwright versions?
11. Native SOCKS5 + GeoIP suggest enterprise-scraping use cases. Are there discoverable enterprise customer references?
12. WebRTC IP / GPU model / canvas / audio / fonts fingerprint spoofing — what's the corpus-first sub-set of fingerprint vectors and what's the standard baseline?

## Detection ecosystem position

13. CloakBrowser claims "30/30 tests passed" on bot detection services. Which 30 services? What's the testing methodology? Independently verifiable?
14. How does CloakBrowser compare to non-corpus competitors (Patchright, Botright, Camoufox, undetected-chromedriver) on detection rates? README mentions Patchright as optional dependency.
15. Cloudflare Turnstile / FingerprintJS / BrowserScan / reCAPTCHA v3 detection systems update frequently. What's the project's detection-cycle response time?

## Forks-as-integration strategy

16. CloakHQ maintains forks of crawl4ai (v29 corpus) + crawlee-python + awesome-playwright. Are these forks active (regular sync with upstream) or stale (one-time fork for integration)?
17. Is the fork strategy specifically because upstream doesn't accept CloakBrowser integration PRs? Or for control over integration timing?
18. Are CloakBrowser patches applied directly to the forks, or do the forks just add CloakBrowser as a dependency?

## Pattern Library + audit

19. Pattern #45 sub-typology 45c is corpus-first wrapper-OSS + binary-proprietary split with acceptable-use enumeration. Is there a 4th Pattern #45 mechanism waiting in non-corpus subjects (e.g., dual-license-by-feature-tier)?
20. Pattern #83 N=5 consolidation evidence is strong — when does audit promote (v69 audit batch ~24-25 items)?
21. OC-G Fork-as-Integration-Strategy + OC-H Anonymous-Corporate-Author + OC-I Detection-Evasion-As-Product-Axis + OC-J Acceptable-Use Enumeration — which OC is most likely to reach N=2 in next 5 wikis?
22. The v69 audit batch is now ~24-25 items LARGEST in corpus history. Should the audit be split into sub-audits (license-axis / detection-evasion / fork-strategy)?

## Ecosystem + corpus position

23. CloakBrowser is corpus-first **purpose-built-for-stealth** subject. Prior corpus had stealth-as-feature (crawl4ai, browser-use). Is there a corpus dimension where this divergence forms a sub-archetype?
24. The 14.9K stars at 86 days = HIGH-not-EXTREME velocity is BELOW Pattern #52 threshold. Does Pattern #52 need a HIGH-velocity sub-threshold class for >150-stars/day-but-<300?
25. Drop-in compatibility with Playwright + Puppeteer + Selenium spans 3 ecosystems. Is "ecosystem-spanning-drop-in-compatibility" a new pattern axis?

## Wiki-build process

26. WEAK INCLUDE 2nd consecutive wiki — is the strength categorization stabilizing toward WEAK as the "normal" default, or is this a coincidence?
27. The 86-day-age subject is the OLDEST in v67/v68/v69 (vs 2-day zero / months-old opencode-antigravity-auth). Does subject-age correlate with Pattern #83 evidence strength?
28. The corpus-first dual-use framing for v69 wiki — should routine v2.2 add an explicit "dual-use subject framing" sub-procedure to Phase 0?
29. Phase 4b PRIMARY = sub-typology variant registration (not new pattern, not promotion). Should routine v2.2 codify a "sub-typology proposal-document" template distinct from new-pattern + promotion-proposal templates?
30. v69 audit operationally overdue (3rd consecutive trigger-past wiki). Pattern Library is accumulating evidence faster than auditing can dispose. Routine v2.3 codification implication?

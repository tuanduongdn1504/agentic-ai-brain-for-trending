# Caveats & corrections

Pins so the same mistakes aren't repeated (Storm Bear prime directive).

## 1. Chip garble: "Google chip A" → Apple A-series (transcript artifact)

The VN auto-caption reads *"với cái sức mạnh của con chip của Google chip A này rồi của Google."* The on-device OCR speed comes from the **Apple A-series chip + Apple Neural Engine** (designed by Apple, fabricated by TSMC) — **not Google**. Google makes no iPhone silicon. This is an auto-caption mistranslation (likely "Apple" → "Google"), not something the presenter would have claimed. Corrected; don't re-cite "Google chip."

## 2. Developer is Taiwanese, not "Chinese"

The presenter jokingly calls the app author *"pháp sư Trung Hoa" / "anh Trung Quốc"* (a common Vietnamese colloquialism for Sinophone developers, roughly "Chinese wizard"). Factually the developer — **Ling, Wei-Cheng (凌偉誠), GitHub [`riddleling`](https://github.com/riddleling)** — is based in **Kaohsiung, Taiwan**. State his location factually; the "Chinese" tag is imprecise. Not a substantive video error, but pinned for accuracy.

## 3. "Free" is real — with an optional tip

Unlike revenue-titled corpus entries ([[jasonlee-claude-mobile-app/the-80k-title-and-revenue-claims]]) or capex-theater ([[local-ai-coding-agents/hardware-economics-and-tco]]), this "0 đồng" is **genuine**: the App Store app is free to download and run; there's an **optional $4.99 "Buy me a coffee"** in-app tip. On-device Vision inference has no per-use cost. C10 stands.

## 4. App name & novelty

- Product name is **"OCR Server"** (repo `iOS-OCR-Server`), not "iPhone OCR Server" as the presenter says.
- The app is **not brand-new** — created **2025-08-01**, 1,771★, ~11 months old. The *video* is fresh (2026-07-14); the app is established. Don't describe the app as newly-released.

## 5. Version skew (README vs App Store)

The GitHub README documents an earlier state than the shipping App Store build (the App Store changelog shows features like per-core CPU monitoring added in v1.3.2; current build is later). When a setting appears **on-screen in the video** but not in the README, trust the on-screen demo — the README lags the app. This drove the two overrides below.

## 6. Two main-loop overrides of the (Haiku) verification agents (Rule 12)

The workflow agents ran on Haiku 4.5 and could not watch the video, so they repeatedly downgraded **on-screen-demonstrated** facts to UNVERIFIED because they weren't in the README/App Store text. Overridden in the main loop:

- **C5 (settings/monitor):** agents → UNVERIFIED. But the video **shows** accurate/fast, language correction, auto-detect, port, and a CPU/memory/temp/battery monitor on screen, and they map to documented Vision options + the App Store v1.3.2 changelog → **CONFIRMED**. The README not repeating a UI setting ≠ the setting not existing.
- **C8 (Vietnamese handwriting fails):** agents → UNVERIFIED. But it's the presenter honestly reporting his own on-screen demo, and it's exactly what Vision's verified language-coverage gap predicts → **CONFIRMED-with-context**.

This is the same failure mode logged in [[local-ai-coding-agents/_index]] and [[google-ai-studio-github-import/_index]]: **Haiku fan-out agents under-weight primary-source demos and over-trust a single lagging text doc.** The fix is main-loop reconciliation, applied here.

## 7. C7 "faster" is unquantified

The paragraph/`docOCR` mode being "faster" than box mode is the presenter's impression, with **no benchmark** in any source. Real structure/table/Markdown output is confirmed; the speed comparison is not.

## 8. `/docOCR` output-format nuance

The iOS README's `/docOCR` sample and the Mac `docOCR` tool differ slightly in documented output (the Mac tool is explicitly Markdown). The video shows the iOS endpoint producing MD-structured output with a table, so the endpoint does structure detection — but the exact iOS output contract isn't fully pinned in text. Minor; flagged.

## Key Takeaways

- Don't re-cite "Google chip" (garble) or "Chinese developer" (he's Taiwanese).
- "Free" is real; app is established (Aug 2025), not new; name is "OCR Server."
- **README lags the shipping app** — trust on-screen demos over doc silence (drove the C5/C8 overrides).
- "Faster docOCR" is unbenchmarked; treat as impression.

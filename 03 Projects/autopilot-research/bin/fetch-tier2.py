#!/usr/bin/env python3
"""
Bypass-403 Tier 2 — Playwright + playwright-stealth.

Patches navigator.webdriver, plugin list, language, hairline, WebGL vendor —
addresses 80% of vanilla-Playwright detection signatures.

Usage: fetch-tier2.py <URL> <output.html>
"""
import sys
from playwright.sync_api import sync_playwright
from playwright_stealth import Stealth


def main():
    if len(sys.argv) != 3:
        print("usage: fetch-tier2.py <URL> <output.html>", file=sys.stderr)
        return 2
    url, out = sys.argv[1], sys.argv[2]
    stealth = Stealth()
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        ctx = browser.new_context(
            user_agent=(
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/126.0.0.0 Safari/537.36"
            ),
            viewport={"width": 1280, "height": 800},
            locale="en-US",
            timezone_id="America/Los_Angeles",
        )
        # Apply stealth patches at the context level
        stealth.apply_stealth_sync(ctx)
        page = ctx.new_page()

        responses = []
        page.on("response", lambda r: responses.append((r.status, r.url[:120])))

        try:
            page.goto(url, wait_until="domcontentloaded", timeout=30000)
        except Exception as e:
            print(f"NAV FAIL: {e}", file=sys.stderr)
            browser.close()
            return 1
        page.wait_for_timeout(10000)
        title = page.title()
        h1 = page.evaluate('() => document.querySelector("h1")?.innerText || ""')
        article_count = page.evaluate('() => document.querySelectorAll("article").length')
        body_text_len = page.evaluate('() => document.body.innerText.length')
        html = page.content()
        with open(out, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"size {len(html)} | title={title[:60]!r} h1={h1[:80]!r} articles={article_count} body_len={body_text_len}")
        print(f"non-200 responses: {sum(1 for s, _ in responses if s != 200)} of {len(responses)}")
        browser.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""
Bypass-403 Tier 1 — Playwright vanilla with realistic Chrome context.

Usage: fetch-tier1.py <URL> <output.html>
"""
import sys
from playwright.sync_api import sync_playwright


def main():
    if len(sys.argv) != 3:
        print("usage: fetch-tier1.py <URL> <output.html>", file=sys.stderr)
        return 2
    url, out = sys.argv[1], sys.argv[2]
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
            extra_http_headers={
                "Accept-Language": "en-US,en;q=0.9",
            },
        )
        page = ctx.new_page()
        try:
            response = page.goto(url, wait_until="domcontentloaded", timeout=30000)
        except Exception as e:
            print(f"NAV FAIL: {e}", file=sys.stderr)
            browser.close()
            return 1
        # Wait extra for Cloudflare JS challenge to resolve if present
        page.wait_for_timeout(8000)
        html = page.content()
        with open(out, "w", encoding="utf-8") as f:
            f.write(html)
        status = response.status if response else "?"
        title = page.title()
        print(f"HTTP {status} | size {len(html)} | title: {title!r} | final URL: {page.url}")
        browser.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Tier 1 debug variant — long wait + multiple capture points."""
import sys
from playwright.sync_api import sync_playwright

URL, OUT = sys.argv[1], sys.argv[2]
with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    ctx = browser.new_context(
        user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        viewport={"width": 1280, "height": 800},
        locale="en-US",
    )
    page = ctx.new_page()

    # Capture network responses for diagnostic
    responses = []
    page.on("response", lambda r: responses.append((r.status, r.url[:120])))

    page.goto(URL, wait_until="domcontentloaded", timeout=30000)

    # Wait progressively longer and snapshot at each
    for wait_sec in [5, 10, 20]:
        page.wait_for_timeout(wait_sec * 1000)
        title = page.title()
        h1 = page.evaluate('() => document.querySelector("h1")?.innerText || ""')
        article_count = page.evaluate('() => document.querySelectorAll("article").length')
        body_text_len = page.evaluate('() => document.body.innerText.length')
        print(f"after {wait_sec}s cumulative: title={title[:60]!r} h1={h1[:80]!r} articles={article_count} body_text_len={body_text_len}")

    html = page.content()
    open(OUT, "w", encoding="utf-8").write(html)
    print(f"\nfinal size: {len(html)}")
    print(f"\nfirst 5 non-200 responses:")
    for s, u in [r for r in responses if r[0] != 200][:5]:
        print(f"  {s} {u}")
    browser.close()

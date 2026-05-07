#!/usr/bin/env python3
"""
Lark wiki scraper — Phase 2 archive of "Khoá học Claude toàn diện tiếng Việt".

Walks the public Lark wiki tree starting at ROOT_URL, discovers all sub-pages
via React fiber inspection of the sidebar tree, then visits each page and
saves rendered content to local markdown files.

Idempotent / resumable: skips pages already on disk.

Usage:
    cd "$AUTOPILOT_ROOT"
    source bin/autopilot-env.sh
    python bin/lark-scraper.py --list-only      # discover URLs only
    python bin/lark-scraper.py --max 10         # fetch first 10 pages (smoke test)
    python bin/lark-scraper.py                  # full fetch

Output:
    raw/lark-claude-course/_urls-full.json      # discovered URL list
    raw/lark-claude-course/lark-pages/<id>--<slug>.md  # one file per page
"""
import asyncio
import json
import os
import re
import sys
import time
from pathlib import Path

try:
    from playwright.async_api import async_playwright, TimeoutError as PWTimeout
except ImportError:
    sys.exit("ERROR: playwright not installed. Run: pip install playwright && playwright install chromium")

ROOT_URL = "https://transform.sg.larksuite.com/wiki/EY8kwGVvcirJTBkCFzalp71igQb"
PROJECT_ROOT = Path(os.environ.get("AUTOPILOT_ROOT", Path(__file__).parent.parent))
ARCHIVE_ROOT = PROJECT_ROOT / "raw" / "lark-claude-course"
PAGES_DIR = ARCHIVE_ROOT / "lark-pages"
URLS_FILE = ARCHIVE_ROOT / "_urls-full.json"

# Tree expansion: how many passes to keep clicking new collapsed arrows
MAX_EXPAND_PASSES = 25
EXPAND_WAIT_MS = 700

# Content fetch: rate limiting + timeouts
PAGE_TIMEOUT_MS = 30_000
INTER_PAGE_WAIT_MS = 400


# ----------------------------------------------------------------------
# Tree discovery
# ----------------------------------------------------------------------

EXPAND_JS = """
() => {
    const arrows = document.querySelectorAll('.workspace-tree-view-node-expand-arrow--collapsed');
    arrows.forEach(a => a.click());
    return arrows.length;
}
"""

# Harvest URLs by digging into React fiber on each tree node.
# Lark stores wikiToken at props.data.wikiToken (also obj_token, parentWikiToken).
HARVEST_JS = r"""
() => {
    const out = new Map();
    const TOKEN_RE = /^[A-Za-z0-9_-]{20,40}$/;

    // 1. Easy harvest from any anchor tags rendered in main content
    document.querySelectorAll('a[href*="/wiki/"]').forEach(a => {
        const m = a.href.match(/\/wiki\/([A-Za-z0-9_-]{20,})/);
        if (m && !out.has(m[1])) {
            out.set(m[1], (a.textContent || '').trim().slice(0, 120));
        }
    });

    // Recursively search an object for {wikiToken, title} pairs (depth-limited)
    function findTokenObj(obj, depth, results) {
        if (!obj || typeof obj !== 'object' || depth > 5) return;
        if (typeof obj.wikiToken === 'string' && TOKEN_RE.test(obj.wikiToken)) {
            const title = (obj.title || obj.name || '').toString().trim().slice(0, 200);
            results.push({token: obj.wikiToken, title});
            // don't recurse deeper into a found-data object
            return;
        }
        if (Array.isArray(obj)) {
            for (let i = 0; i < Math.min(obj.length, 1000); i++) findTokenObj(obj[i], depth+1, results);
            return;
        }
        for (const k of Object.keys(obj)) {
            // Skip noisy DOM/React internals
            if (k.startsWith('_') || k === 'children' || k === 'ref' || k === 'key') continue;
            const v = obj[k];
            if (v && typeof v === 'object') findTokenObj(v, depth+1, results);
        }
    }

    // 2. React fiber inspection on sidebar tree nodes
    const treeNodes = document.querySelectorAll('[class*="workspace-tree-view-node"]');
    for (const node of treeNodes) {
        const fiberKey = Object.keys(node).find(k => k.startsWith('__reactFiber') || k.startsWith('__reactInternalInstance'));
        if (!fiberKey) continue;

        let fiber = node[fiberKey];
        let walked = 0;
        let found = false;
        while (fiber && walked < 15 && !found) {
            const props = fiber.memoizedProps || fiber.pendingProps;
            if (props && typeof props === 'object') {
                const results = [];
                findTokenObj(props, 0, results);
                for (const r of results) {
                    if (!out.has(r.token)) out.set(r.token, r.title || (node.textContent || '').trim().slice(0, 120));
                    found = true;
                }
            }
            fiber = fiber.return;
            walked++;
        }
    }

    return [...out.entries()].map(([id, title]) => ({id, title}));
}
"""


async def expand_full_tree(page):
    print("    expanding tree...")
    last_known = -1
    for i in range(MAX_EXPAND_PASSES):
        clicked = await page.evaluate(EXPAND_JS)
        node_count = await page.evaluate("() => document.querySelectorAll('[class*=\"workspace-tree-view-node\"]').length")
        print(f"    pass {i+1}: clicked {clicked} arrows, total nodes={node_count}")
        if clicked == 0 and node_count == last_known:
            break
        last_known = node_count
        await page.wait_for_timeout(EXPAND_WAIT_MS)


async def discover_all_urls(page):
    """Returns list of {id, title} dicts."""
    print(f"[1/3] Loading root: {ROOT_URL}")
    # Use 'load' (not networkidle — Lark's SPA keeps making background requests forever)
    await page.goto(ROOT_URL, wait_until="load", timeout=60000)
    print("    waiting for sidebar to hydrate...")
    try:
        await page.wait_for_selector(
            '[class*="workspace-tree-view-container"], [class*="wiki-space-detail"], [class*="workspace-tree-view-node"]',
            timeout=30000,
        )
        print("    sidebar container detected ✓")
    except PWTimeout:
        print("    WARNING: sidebar container not detected within 30s — proceeding anyway")
    await page.wait_for_timeout(5000)  # extra hydration

    print("[2/3] Expanding tree (this may take a minute)...")
    await expand_full_tree(page)

    # Scroll the sidebar to ensure virtualized items are mounted, then re-expand
    print("    scrolling sidebar to flush virtualized items...")
    for _ in range(5):
        await page.evaluate("""() => {
            const sidebar = document.querySelector('[class*="workspace-tree-view-container"]') ||
                           document.querySelector('[class*="wiki-space-detail"]');
            if (sidebar) sidebar.scrollTop = sidebar.scrollHeight;
        }""")
        await page.wait_for_timeout(600)
        await page.evaluate(EXPAND_JS)
        await page.wait_for_timeout(EXPAND_WAIT_MS)

    print("[3/3] Harvesting URLs from tree...")
    urls = await page.evaluate(HARVEST_JS)

    # De-duplicate (preserve first-seen order)
    seen = set()
    deduped = []
    for u in urls:
        if u["id"] in seen:
            continue
        seen.add(u["id"])
        deduped.append(u)

    return deduped


# ----------------------------------------------------------------------
# Content extraction
# ----------------------------------------------------------------------

CONTENT_JS = r"""
() => {
    // Lark Docs main content selectors (try in order)
    const selectors = [
        '.docs-page',
        '.lark-doc-render',
        '[class*="docs-render"]',
        '[class*="document-content"]',
        '[class*="docs-content"]',
        '#mainBody',
        'main'
    ];
    for (const sel of selectors) {
        const el = document.querySelector(sel);
        if (el && (el.innerText || '').length > 200) return el.innerText;
    }
    // Fallback: the whole body minus navigation
    return document.body.innerText || '';
}
"""


def slug(text, maxlen=60):
    s = re.sub(r"[\s/\\:?*\"<>|]+", "-", text).strip("-").lower()
    return re.sub(r"-+", "-", s)[:maxlen] or "untitled"


async def fetch_page_content(page, page_id, title):
    url = f"https://transform.sg.larksuite.com/wiki/{page_id}"
    out = PAGES_DIR / f"{page_id}--{slug(title)}.md"
    if out.exists() and out.stat().st_size > 100:
        return ("SKIP", out, 0)

    try:
        await page.goto(url, wait_until="domcontentloaded", timeout=PAGE_TIMEOUT_MS)
    except PWTimeout:
        return ("TIMEOUT-NAV", out, 0)

    # Give the SPA time to render the doc body (Lark loads content lazily)
    await page.wait_for_timeout(2500)

    try:
        content = await page.evaluate(CONTENT_JS)
    except Exception as e:
        return (f"ERR-EXTRACT:{e}", out, 0)

    content = (content or "").strip()
    if len(content) < 50:
        # Wait once more in case of slow render
        await page.wait_for_timeout(2500)
        content = (await page.evaluate(CONTENT_JS) or "").strip()

    body = (
        f"# {title}\n\n"
        f"**Source:** {url}\n"
        f"**Wiki ID:** {page_id}\n"
        f"**Archived:** 2026-05-07\n\n"
        f"---\n\n"
        f"{content}\n"
    )
    out.write_text(body, encoding="utf-8")
    return ("OK", out, len(content))


# ----------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------

async def main(argv):
    list_only = "--list-only" in argv
    max_pages = None
    for i, a in enumerate(argv):
        if a == "--max" and i + 1 < len(argv):
            max_pages = int(argv[i + 1])

    PAGES_DIR.mkdir(parents=True, exist_ok=True)
    ARCHIVE_ROOT.mkdir(parents=True, exist_ok=True)

    headless = "--headless" in argv  # default: headed (Lark seems to suppress sidebar in headless)
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=headless,
            args=["--disable-blink-features=AutomationControlled"],  # reduce headless detection
        )
        ctx = await browser.new_context(
            user_agent=("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                        "AppleWebKit/537.36 (KHTML, like Gecko) "
                        "Chrome/127.0.0.0 Safari/537.36"),
            viewport={"width": 1600, "height": 1000},
        )
        # Hide navigator.webdriver flag (common headless tell)
        await ctx.add_init_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined});")
        page = await ctx.new_page()

        urls = await discover_all_urls(page)
        print(f"\n  Discovered {len(urls)} unique pages.\n")

        URLS_FILE.write_text(json.dumps(urls, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"  URL list saved to: {URLS_FILE}\n")

        if list_only:
            print("--list-only specified. Done.")
            await browser.close()
            return

        targets = urls if max_pages is None else urls[:max_pages]
        print(f"Fetching content for {len(targets)} pages...\n")

        ok = skip = err = 0
        start = time.time()
        for i, item in enumerate(targets, 1):
            page_id = item["id"]
            title = item["title"] or page_id
            status, path, n = await fetch_page_content(page, page_id, title)
            elapsed = time.time() - start
            print(f"  [{i:3}/{len(targets)}] {status:18} {n:6} ch  {title[:60]}  ({elapsed:.0f}s)")
            if status == "OK":
                ok += 1
            elif status == "SKIP":
                skip += 1
            else:
                err += 1
            await page.wait_for_timeout(INTER_PAGE_WAIT_MS)

        print(f"\nDone. OK={ok}, SKIP={skip}, ERR={err}, total={len(targets)}")
        print(f"Files in: {PAGES_DIR}")

        await browser.close()


if __name__ == "__main__":
    asyncio.run(main(sys.argv))

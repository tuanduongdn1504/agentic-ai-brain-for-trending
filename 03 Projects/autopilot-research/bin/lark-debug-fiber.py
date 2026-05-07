#!/usr/bin/env python3
"""Probe Lark sidebar tree node React props — AGGRESSIVE: dump ALL props for the Nt component."""
import asyncio
import json
import sys
from playwright.async_api import async_playwright

ROOT_URL = "https://transform.sg.larksuite.com/wiki/EY8kwGVvcirJTBkCFzalp71igQb"

PROBE_JS = r"""
() => {
    const nodes = document.querySelectorAll('[class*="workspace-tree-view-node"]');
    if (nodes.length < 5) return {error: 'not enough nodes', count: nodes.length};

    // Pick 3 sample nodes
    const sampleIdxs = [1, 10, 50].filter(i => i < nodes.length);
    const samples = [];

    function summarizeValue(v, depth) {
        if (v === null) return 'null';
        if (v === undefined) return 'undef';
        const t = typeof v;
        if (t === 'string') {
            if (v.length > 200) return `STR(${v.length}):${v.slice(0,80)}...`;
            return `STR:${v}`;
        }
        if (t === 'number' || t === 'boolean') return `${t}:${v}`;
        if (t === 'function') return 'FN';
        if (Array.isArray(v)) {
            if (depth > 2) return `ARR(${v.length})`;
            return v.slice(0, 5).map(x => summarizeValue(x, depth+1));
        }
        if (t === 'object') {
            if (depth > 3) return 'OBJ(...)';
            const keys = Object.keys(v);
            if (keys.length === 0) return 'OBJ{}';
            const out = {};
            for (const k of keys.slice(0, 30)) {
                try { out[k] = summarizeValue(v[k], depth+1); } catch(e) { out[k] = 'ERR'; }
            }
            return out;
        }
        return `?:${t}`;
    }

    for (const idx of sampleIdxs) {
        const node = nodes[idx];
        const fiberKey = Object.keys(node).find(k => k.startsWith('__reactFiber') || k.startsWith('__reactInternalInstance'));
        if (!fiberKey) { samples.push({idx, error: 'no fiber'}); continue; }

        // Also dump all DOM attributes
        const attrs = {};
        for (const a of node.attributes) attrs[a.name] = a.value.length > 80 ? a.value.slice(0,80) + '...' : a.value;

        const path = [];
        let fiber = node[fiberKey];
        let depth = 0;
        while (fiber && depth < 25) {
            const props = fiber.memoizedProps || fiber.pendingProps;
            const stateNode = fiber.stateNode;
            const memState = fiber.memoizedState;
            const entry = { depth };
            entry.type = (fiber.type && (fiber.type.displayName || fiber.type.name || (typeof fiber.type === 'string' ? fiber.type : 'fn'))) || 'null';
            if (props && typeof props === 'object') {
                entry.props = summarizeValue(props, 0);
            }
            // Check for state hooks (function components)
            if (memState && memState.memoizedState !== undefined) {
                try {
                    let h = memState;
                    const hooks = [];
                    let hi = 0;
                    while (h && hi < 6) {
                        hooks.push(summarizeValue(h.memoizedState, 0));
                        h = h.next;
                        hi++;
                    }
                    if (hooks.length > 0) entry.hooks = hooks;
                } catch(e) {}
            }
            path.push(entry);
            fiber = fiber.return;
            depth++;
        }
        samples.push({
            idx,
            text: (node.textContent||'').replace(/\s+/g,' ').slice(0,60),
            domAttrs: attrs,
            path
        });
    }
    return {totalNodes: nodes.length, samples};
}
"""

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=False,
            args=["--disable-blink-features=AutomationControlled"],
        )
        ctx = await browser.new_context(viewport={"width": 1600, "height": 1000})
        await ctx.add_init_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined});")
        page = await ctx.new_page()

        await page.goto(ROOT_URL, wait_until="load")
        await page.wait_for_selector('[class*="workspace-tree-view-container"]', timeout=30000)
        await page.wait_for_timeout(5000)

        for _ in range(8):
            n = await page.evaluate("""() => { const a = document.querySelectorAll('.workspace-tree-view-node-expand-arrow--collapsed'); a.forEach(x => x.click()); return a.length; }""")
            if n == 0: break
            await page.wait_for_timeout(700)

        result = await page.evaluate(PROBE_JS)
        out_path = "/tmp/lark-fiber-dump.json"
        with open(out_path, "w") as f:
            json.dump(result, f, indent=2, ensure_ascii=False)
        print(f"Wrote {out_path}")
        print(f"totalNodes: {result.get('totalNodes')}")
        print(f"samples: {len(result.get('samples', []))}")

        await browser.close()

asyncio.run(main())

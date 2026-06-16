# M5 sandbox — Claude API cost arc, hands-on

Reproduces the four-lever cost arc from [[wiki/claude-api-cost-optimization]] on a tiny
"HeroCorp dashboard agent", measuring cost at each stage.

## Run

```bash
cd "03 Projects/autopilot-research/sandbox/claude-cost-arc"
/usr/local/opt/python@3.12/bin/python3.12 cost_arc.py          # ESTIMATE (offline, no spend)

export ANTHROPIC_API_KEY=...                                    # then run LIVE (real calls, ~$0.50)
/usr/local/opt/python@3.12/bin/python3.12 cost_arc.py
/usr/local/opt/python@3.12/bin/python3.12 cost_arc.py --estimate   # force offline even with a key
```

Pure stdlib — no `pip`, no venv. (This user's `python3` shim is broken; use the brew path above.)

## The four stages (stacked, in order)

1. **baseline** — Opus, no caching, full noisy multi-source context.
2. **+ prompt caching** — freeze the prefix, `cache_control` on it. 1st refresh writes, rest read.
3. **+ context engineering** — send only the filtered signal slice, not the raw dump.
4. **+ advisor** — cheap Sonnet executor + a lean Opus advisor on the hard ~1-in-3 refreshes.

## Sample result (estimate mode)

```
stage            model                $ cost  vs base
1 baseline       claude-opus-4-8     $0.307    100%
2 + caching      claude-opus-4-8     $0.117     38%
3 + context eng  claude-opus-4-8     $0.094     31%
4 + advisor      claude-sonnet-4-6   $0.063     20%   -> 80% cheaper
```

## What LIVE mode adds

Real `usage` from the API — most importantly **`cache_read_input_tokens` becomes nonzero on
the 2nd+ refresh**, proving caching actually engaged. In estimate mode those numbers are modeled.

## Caveats (read before trusting the numbers)

- **Estimate mode** uses a rough ~4-chars/token heuristic + the real pricing + real caching
  economics (read 0.1×, write 1.25× at 5-min TTL). Live numbers differ slightly; the *shape* holds.
- The frozen prefix is **8,924 tokens** — deliberately above Opus's 4,096 cache minimum. A smaller
  prefix would silently NOT cache (the talk's #1 trap). This is why the demo pads the hero roster.
- **Advisor nuance (a real finding, not a bug):** caches are **model-scoped**, so the Opus advisor
  can't read the Sonnet executor's cache. If you send the advisor the whole company brief, it pays a
  full Opus cache-write every escalation and stage 4 can cost *more* than stage 3. The fix modeled
  here: give the advisor a **lean** context (reviewer instruction + the one hard case), and escalate
  only on genuinely hard refreshes. Tier pays off when the bulk runs cheap and escalations stay rare.

## Cleanup

```bash
rm -rf "03 Projects/autopilot-research/sandbox/claude-cost-arc"
```

Nothing else is installed or written outside this folder.

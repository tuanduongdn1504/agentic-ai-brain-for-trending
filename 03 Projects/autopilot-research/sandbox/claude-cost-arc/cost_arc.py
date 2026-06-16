#!/usr/bin/env python3.12
"""
M5 sandbox: reproduce the Puneet/Punit Shah "Code with Claude" cost arc hands-on.

One tiny "HeroCorp dashboard agent" run through four stages, stacking the four
levers in order, measuring cost at each:

  1. baseline           Opus, no caching, full noisy context
  2. + prompt caching   freeze the prefix, cache_control on it
  3. + context eng      send only the relevant slice (filtered data)
  4. + advisor strategy cheap Sonnet executor + occasional Opus advisor

Modes (auto-detected):
  LIVE      ANTHROPIC_API_KEY set  -> real Messages API calls, real usage/cache hits
  ESTIMATE  no key (or --estimate) -> offline cost model from real pricing (no spend)

Pure stdlib. Run:  /usr/local/opt/python@3.12/bin/python3.12 cost_arc.py
Wiki: ../../wiki/claude-api-cost-optimization/_index.md
"""
import json, os, sys, urllib.request, urllib.error

API_URL = "https://api.anthropic.com/v1/messages"
KEY = os.environ.get("ANTHROPIC_API_KEY")
FORCE_ESTIMATE = "--estimate" in sys.argv
LIVE = bool(KEY) and not FORCE_ESTIMATE

# $ per token. cache read = 0.1x input, cache write (5-min TTL) = 1.25x input.
PRICING = {
    "claude-opus-4-8":   {"in": 5/1e6,  "out": 25/1e6},
    "claude-sonnet-4-6": {"in": 3/1e6,  "out": 15/1e6},
    "claude-haiku-4-5":  {"in": 1/1e6,  "out": 5/1e6},
}

def dollars(model, u):
    p = PRICING[model]
    return (u.get("input_tokens", 0)        * p["in"]
          + u.get("cache_read_input_tokens", 0)     * p["in"] * 0.1
          + u.get("cache_creation_input_tokens", 0) * p["in"] * 1.25
          + u.get("output_tokens", 0)       * p["out"])

# ---- the frozen company prefix (must exceed ~4096 tokens to be cacheable on Opus) ----
_ROSTER = "\n".join(
    f"- Hero #{i:03d} '{n}': power={pw}; 90d-retention={70+(i*7)%30}%; flight-risk={'high' if i%5==0 else 'low'}; "
    f"insurance-tier={'A' if i%3 else 'C'}; availability=all days except scheduled civic events; "
    f"cape-color={['red','blue','teal','amber'][i%4]}; last-contract=#{1000+i}; rating={3+(i%3)}/5."
    for i, (n, pw) in enumerate([
        ("Cryothane","cryo"),("Volt","electric"),("Mistral","wind"),("Aegis","shield"),("Pyra","fire"),
        ("Tidal","water"),("Quartz","earth"),("Lumen","light"),("Umbra","shadow"),("Gale","speed"),
        ("Ferro","magnet"),("Echo","sound"),("Verdant","plant"),("Cinder","ash"),("Nimbus","cloud"),
        ("Onyx","density"),("Solis","solar"),("Frostbite","ice"),("Tremor","quake"),("Halcyon","calm"),
    ] * 9))  # 180 entries -> frozen prefix comfortably exceeds Opus's 4096-token cache minimum

COMPANY_BRIEF = f"""You are HeroCorp's operations analyst. HeroCorp is a superhero-outsourcing company:
we fight crime, keep trains on time, run birthday parties, and guarantee enough balloons.
Mission: match the right hero to each contract; protect renewals; keep insurance cost down.

Scoring rubric for a dashboard summary (apply consistently, never restate it back):
- Surface the single biggest renewal RISK first, then 2 supporting metrics.
- A green top-line metric can hide a red root cause ("watermelon"): if a key client's
  required hero is unavailable on the event date, the renewal is AT RISK regardless of sentiment.
- Be terse: <=120 words. No preamble. Cite the metric that drives each claim.

Standing OKRs: (1) 90-day retention >=95%; (2) flight-risk heroes <10%; (3) Metropolis renewal secured
(largest sponsor — losing it jeopardizes the next funding round); (4) insurance cost trending down;
(5) balloon-SLA >=99% for the under-5 segment.

Hero roster (frozen reference — do not echo):
{_ROSTER}

Operating rules: prefer cheaper heroes when intelligence-equivalent; escalate ambiguous
contract language to senior review; never promise a hero you cannot staff on the date.
"""

SYSTEM_BLOCKS_PLAIN  = [{"type": "text", "text": COMPANY_BRIEF}]
SYSTEM_BLOCKS_CACHED = [{"type": "text", "text": COMPANY_BRIEF, "cache_control": {"type": "ephemeral"}}]

# ---- per-refresh data: NOISY (raw multi-source dump) vs TRIMMED (filtered slice) ----
NOISY_DATA = (
    "RAW FEED (web+Slack+Gong+Jira) — " + ("Gong call w/ under-5 client: kids talk about the blue balloon "
    "for thirty minutes, then sixty, mostly off-topic chatter, laughter, snack break, more balloon talk. " * 18)
    + " Slack: #ops thread 240 msgs mostly emojis. Jira: 31 tickets, 3 relevant. "
    "Web: press mentions, unrelated. SIGNAL buried inside: Metropolis renewal — the mayor specifically "
    "requested hero 'Cryothane' (raises our insurance), and Cryothane is NOT available on the event date. "
    "90d retention 94%. One flight-risk hero (low pay)."
)
TRIMMED_DATA = (
    "FILTERED SIGNAL: Metropolis renewal — mayor requires hero 'Cryothane'; Cryothane unavailable on event date "
    "(=> renewal at risk despite positive sentiment). 90d retention 94% (target 95%). 1 flight-risk hero (low pay)."
)
QUESTION = "\n\nProduce this week's dashboard summary per the rubric."

# The advisor gets a LEAN context (just a reviewer instruction + the hard case) — NOT the
# full company brief. Caches are model-scoped, so the Opus advisor can't read the executor's
# cache anyway; sending it the whole roster would waste a full Opus prefix-write every escalation.
ADVISOR_SYSTEM = [{"type": "text", "text":
    "You are HeroCorp's senior contracts reviewer. Given a draft read of a renewal, state in one "
    "line whether it is actually SAFE or AT RISK and why. Watch for watermelons: a green sentiment "
    "hiding a red root cause (e.g. the client's required hero is unavailable on the event date)."}]

def approx_tokens(s):  # rough offline estimator (~4 chars/token)
    return max(1, len(s) // 4)

def call_live(model, system_blocks, user_text):
    body = {"model": model, "max_tokens": 400, "system": system_blocks,
            "messages": [{"role": "user", "content": user_text}]}
    req = urllib.request.Request(
        API_URL, data=json.dumps(body).encode(),
        headers={"x-api-key": KEY, "anthropic-version": "2023-06-01", "content-type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            return json.load(r)["usage"]
    except urllib.error.HTTPError as e:
        print(f"  ! API error {e.code}: {e.read().decode()[:300]}", file=sys.stderr)
        raise

def call_estimate(model, system_blocks, user_text, cached_prefix, prefix_already_written):
    """Offline usage model that honors caching + filtering economics."""
    prefix_tok = approx_tokens(system_blocks[0]["text"])
    user_tok = approx_tokens(user_text)
    out_tok = 95  # terse summary, ~95 output tokens
    u = {"input_tokens": 0, "cache_read_input_tokens": 0,
         "cache_creation_input_tokens": 0, "output_tokens": out_tok}
    if cached_prefix:
        if prefix_already_written:
            u["cache_read_input_tokens"] = prefix_tok      # 2nd+ call: served from cache
        else:
            u["cache_creation_input_tokens"] = prefix_tok  # 1st call: write
        u["input_tokens"] = user_tok                        # volatile suffix always full price
    else:
        u["input_tokens"] = prefix_tok + user_tok           # no cache: everything full price
    return u

N_REFRESHES = 6  # a week of dashboard loads; 1st warms the cache, the rest read it

def _do(model, sys_blocks, user_text, cached, written):
    """One call. LIVE -> real API (cache handled server-side). ESTIMATE -> offline model
    with per-model cache state (1st same-model call writes the prefix, later ones read)."""
    if LIVE:
        return call_live(model, sys_blocks, user_text)
    already = cached and (model in written)
    if cached:
        written.add(model)
    return call_estimate(model, sys_blocks, user_text, cached, prefix_already_written=already)

def run_stage(name, exec_model, cached, trimmed, advisor):
    sys_blocks = SYSTEM_BLOCKS_CACHED if cached else SYSTEM_BLOCKS_PLAIN
    data = TRIMMED_DATA if trimmed else NOISY_DATA
    totals = {"input_tokens": 0, "cache_read_input_tokens": 0,
              "cache_creation_input_tokens": 0, "output_tokens": 0}
    cost = 0.0
    written = set()  # models whose frozen prefix has been written this stage (cache is model-scoped)
    for i in range(N_REFRESHES):
        u = _do(exec_model, sys_blocks, data + QUESTION, cached, written)
        for k in totals: totals[k] += u.get(k, 0)
        cost += dollars(exec_model, u)
        # advisor escalates on the hard cases only (~1 in 3 here) — lean uncached Opus call
        if advisor and i % 3 == 2:
            adv_user = "Draft read: renewal looks positive. Is it actually safe?\n" + TRIMMED_DATA
            au = _do("claude-opus-4-8", ADVISOR_SYSTEM, adv_user, False, written)
            for k in totals: totals[k] += au.get(k, 0)
            cost += dollars("claude-opus-4-8", au)
    return name, exec_model, totals, cost

STAGES = [
    ("1 baseline",        "claude-opus-4-8",   False, False, False),
    ("2 + caching",       "claude-opus-4-8",   True,  False, False),
    ("3 + context eng",   "claude-opus-4-8",   True,  True,  False),
    ("4 + advisor",       "claude-sonnet-4-6", True,  True,  True),
]

def main():
    mode = "LIVE (real API calls)" if LIVE else "ESTIMATE (offline; no spend)"
    print(f"\n=== HeroCorp cost arc — mode: {mode} ===")
    print(f"frozen prefix ~{approx_tokens(COMPANY_BRIEF)} tokens (cacheable: >4096 on Opus), {N_REFRESHES} refreshes/stage\n")
    rows, base = [], None
    for cfg in STAGES:
        name, model, totals, cost = run_stage(*cfg)
        if base is None: base = cost
        rows.append((name, model, totals, cost))
    w = "{:<16} {:<18} {:>8} {:>8} {:>8} {:>8} {:>10} {:>8}"
    print(w.format("stage", "model", "in", "cWrite", "cRead", "out", "$ cost", "vs base"))
    print("-" * 90)
    for name, model, t, cost in rows:
        vs = f"{cost/base*100:4.0f}%" if base else "  -"
        print(w.format(name, model, t["input_tokens"], t["cache_creation_input_tokens"],
                       t["cache_read_input_tokens"], t["output_tokens"], f"${cost:.5f}", vs))
    print("-" * 90)
    final = rows[-1][3]
    print(f"\nbaseline ${base:.5f}  ->  final ${final:.5f}   "
          f"=  {(1-final/base)*100:.0f}% cheaper across the four stacked levers")
    if not LIVE:
        print("\n(estimate mode — set ANTHROPIC_API_KEY to run live and see real cache_read tokens.)")

if __name__ == "__main__":
    main()

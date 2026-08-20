#!/bin/bash
# (C) PROPOSED — bin/verify-vault-inventory.sh
#
# Authored by Claude at wiki v255 (2026-08-20). NOT yet installed.
# To adopt:  mkdir -p bin && cp "03 Projects/HeadFirstAndroid - Beginner Analysis/(C) proposed-verify-vault-inventory.sh" bin/verify-vault-inventory.sh && chmod +x bin/verify-vault-inventory.sh
#
# WHY THIS EXISTS
#   Recommended at v250, v251, v252, v253 and v254. Never written. bin/ did not exist.
#
# WHAT EACH CLAUSE COMES FROM
#   1  v250  bidirectional inventory — check BOTH set-differences, never one
#   2  v250  filename-label vs newest content  ... CORRECTED AT v255, see below
#   3  v251  byte-equality for files that must be identical copies
#   4  v252  graveyard / critical_fail regression — a deleted abstraction must stay deleted
#   5  v253  byte budget on CLAUDE.md's head blocks
#   6  v253  dated-stamp freshness
#   7  v254  ASSERT A COUNT AGAINST A COUNT wherever one is already computed
#   8  v254  rename clause — match by identity, not by current name
#
# THE v255 CORRECTION TO CLAUSE 2 (the reason this ship earned a script change)
#   v254 specified clause 2 as "filename-label-vs-newest-entry". Implemented naively that is WRONG:
#   it flags deliberate, correct compensation as a defect.
#
#   HeadFirstAndroid is the counter-example. Its README maps chapter 7 to chap10img.png and chapter
#   11 to chap07img.png. That looks like an off-by-N bug. It is not — the images were named during
#   an earlier draft numbering and the README compensates at the reference site. I opened the images
#   and confirmed it. A "filename must match content" check would flag a CORRECT file, and the
#   "fix" would break every image in the README.
#
#   So clause 2 does not test "does the label match the content".
#   It tests "IS THE LAG DECLARED".
#
#     PASS if label == content            (no lag)
#     PASS if label != content AND the artifact contains a source-of-truth declaration
#     FAIL if label != content AND nothing says so
#
#   That is rule D32 (v245, from unslothai/unsloth: "declare which copy wins, inside the copy that
#   loses") promoted from prose into a predicate, plus the v255 rule:
#
#     A STALE LABEL IS SAFE WHEN DECLARED AND DANGEROUS WHEN MERELY COMPENSATED.
#
# NOTES
#   - Uses awk/sed/grep only. No python3 (SIGKILLed in this sandbox), no node.
#   - /usr/bin/grep explicitly: `command grep` does NOT bypass the ugrep shim (v253).
#   - Exit 0 = all clauses pass. Exit 1 = at least one FAIL. Warnings never fail the run.

set -u

# Locate the vault root by SIGNATURE, not by relative path.
# (First draft used `cd "$(dirname $0)/.."`. Run from the project folder that resolved to
#  "03 Projects", where there is no CLAUDE.md and no _state/ — and CLAUSE 1 REPORTED PASS,
#  because comm(2) found no differences between two EMPTY sets. That is this ship's own §D.6
#  finding reproduced inside the tool built from it: a green check that checked nothing.
#  Hence: resolve by signature, and never let a clause pass on an empty input. See NONVACUOUS.)
find_vault() {
  d="$(cd "$(dirname "$0")" && pwd)"
  while [ "$d" != "/" ]; do
    if [ -f "$d/CLAUDE.md" ] && [ -d "$d/_state" ]; then echo "$d"; return 0; fi
    d="$(dirname "$d")"
  done
  return 1
}
VAULT="$(find_vault)" || { echo "FATAL: no vault root above $0 (need CLAUDE.md + _state/)"; exit 2; }
cd "$VAULT" || exit 2

GREP=/usr/bin/grep
FAILED=0
WARNED=0

# NONVACUOUS <count> <what> — a clause that examined nothing has not passed.
nonvacuous() {
  if [ "${1:-0}" -eq 0 ] 2>/dev/null; then
    printf "  \033[31mFAIL\033[0m  VACUOUS: %s — examined 0 items, so this clause proved nothing\n" "$2"
    FAILED=$((FAILED+1))
    return 1
  fi
  return 0
}

c_pass() { printf "  \033[32mPASS\033[0m  %s\n" "$1"; }
c_fail() { printf "  \033[31mFAIL\033[0m  %s\n" "$1"; FAILED=$((FAILED+1)); }
c_warn() { printf "  \033[33mWARN\033[0m  %s\n" "$1"; WARNED=$((WARNED+1)); }
c_info() { printf "        %s\n" "$1"; }
head1()  { printf "\n\033[1m== %s ==\033[0m\n" "$1"; }

# Newest version that this file actually holds an ENTRY for.
#
# Parse HEADING LINES ONLY, with a word boundary before the v.
#
# Two bugs were fixed here, and both are on the vault's own error ledger as recurring classes:
#   (1) grepping the whole body: 03c's prose cross-references dozens of other ships, so any
#       file-wide scan reports the newest version MENTIONED, not the newest entry HELD.
#   (2) no word boundary: `v[0-9]+` matched "v89" inside the GitHub username "luongnv89", so
#       _state/04-projects-v30-v39.md appeared to hold a v89 entry. It does not. (Compare v254's
#       "a loose URL regex produced non-comparable unique counts" and its fleet's "Claude mentions
#       135" from a bare substring.)
#
# The anchor is not invented here. _state/03c's own source-of-truth notice specifies it:
#   "a BIDIRECTIONAL check whose third clause compares each `03*-projects-v*.md` filename label
#    against the newest **vNNN entry it actually contains, and FAILS."
newest_v_in() {
  $GREP -hE '^#{1,4} ' "$1" 2>/dev/null \
    | $GREP -oE '(^|[^A-Za-z0-9])v[0-9]{1,4}([^0-9]|$)' \
    | $GREP -oE 'v[0-9]{1,4}' | sed 's/^v//' | sort -n | tail -1
}

# If a file carries a source-of-truth declaration that states a version, THAT VERSION IS A CLAIM
# and must also be current. v255 found the vault's own v245 notice asserting "they run through
# v250" while the file held v254 — the third time that notice has gone stale (v247 -> v250 -> v254).
# A declaration is a claim; claims need checking too.
declared_v_in() {
  head -12 "$1" 2>/dev/null \
    | $GREP -iE 'run through|through \*\*v|entries below are authoritative' \
    | $GREP -oE 'v[0-9]{1,4}' | sed 's/^v//' | sort -n | tail -1
}
# the version in a chapter filename's trailing -vNNN label
label_v_of() {
  basename "$1" | sed -n 's/.*-v\([0-9]\{1,4\}\)\.md$/\1/p'
}

echo "verify-vault-inventory — $VAULT"
echo "run: $(date '+%Y-%m-%d %H:%M')"

# ---------------------------------------------------------------------------
head1 "CLAUSE 1 — bidirectional chapter inventory (v250)"
# CLAUDE.md's chapter index and the _state/ directory must agree, checked BOTH ways.
# NOTE (v255, learned the hard way): this extracts ANY `_state/....md` string, including ones that
# appear inside NARRATIVE PROSE describing a dead path. That is deliberate — a reader or an agent
# following the string will try to open it — but it means the ship note describing a fixed dangling
# reference will itself trip the clause. Write dead paths WITHOUT the `_state/` prefix. Compare
# v254: "a mention is not a ship", where a fleet inflated a corpus-recursion count from 10 to 29 by
# counting mentions as instances.
# The v240 inventory rule: a check between two views of one source cannot see what is missing
# from the source. So walk the real directory too, not just the index.
INDEXED=$(mktemp); ONDISK=$(mktemp)
$GREP -o '_state/[A-Za-z0-9._-]*\.md' CLAUDE.md 2>/dev/null | sed 's|_state/||' | sort -u > "$INDEXED"
ls _state/*.md 2>/dev/null | sed 's|_state/||' | sort -u > "$ONDISK"

MISSING_ON_DISK=$(comm -23 "$INDEXED" "$ONDISK")
UNINDEXED=$(comm -13 "$INDEXED" "$ONDISK")

N_IDX=$(wc -l < "$INDEXED" | tr -d ' '); N_DSK=$(wc -l < "$ONDISK" | tr -d ' ')
printf "        indexed in CLAUDE.md: %s | on disk: %s\n" "$N_IDX" "$N_DSK"
nonvacuous "$N_IDX" "clause 1 index side"
nonvacuous "$N_DSK" "clause 1 disk side"

if [ -z "$MISSING_ON_DISK" ]; then
  c_pass "every _state/ file named in CLAUDE.md exists on disk"
else
  c_fail "named in CLAUDE.md but ABSENT from _state/:"
  echo "$MISSING_ON_DISK" | while read -r f; do [ -n "$f" ] && c_info "$f"; done
fi

if [ -z "$UNINDEXED" ]; then
  c_pass "every _state/ file on disk is named in CLAUDE.md"
else
  c_fail "present in _state/ but NEVER MENTIONED in CLAUDE.md (the v240 blind spot):"
  echo "$UNINDEXED" | while read -r f; do [ -n "$f" ] && c_info "$f"; done
fi
rm -f "$INDEXED" "$ONDISK"

# ---------------------------------------------------------------------------
head1 "CLAUSE 2 — label lag must be DECLARED, not merely compensated (v250 + v255)"
# See the header. This is the clause that would finally catch 03c, and the corrected form is the
# one that does NOT fire on deliberate compensation.
for f in _state/*-projects-*.md; do
  [ -e "$f" ] || continue
  LBL=$(label_v_of "$f")
  NEW=$(newest_v_in "$f")
  [ -z "$LBL" ] && continue
  [ -z "$NEW" ] && { c_warn "$(basename "$f"): no vNNN found in content"; continue; }
  if [ "$LBL" -ge "$NEW" ] 2>/dev/null; then
    c_pass "$(basename "$f"): label v$LBL >= newest content v$NEW"
  else
    # The label lags. Is the lag DECLARED inside the file?
    #
    # ANCHORING MATTERS. A first draft grepped the WHOLE file for "source of truth" and passed
    # 03a/03b/04 on spurious hits — 03b matched the phrase inside a *subject's* description
    # ("maintained in AGENTS.md as the single source of truth") and 04 matched "Zod source-of-truth".
    # Three false passes, i.e. the tool telling me a declaration existed where none did. So:
    #   (i) only look in the file's HEAD (a declaration a reader will not see is not a declaration)
    #   (ii) require the sentence to be ABOUT THIS FILE — it must mention the filename or the
    #        stale-label situation, not merely contain the words "source of truth".
    HEAD_N=40
    if head -"$HEAD_N" "$f" | $GREP -qiE '(source[ -]of[ -]truth|filename|file name).{0,200}(stale|lag|confus|authoritative|entries below)|(stale|lag|confus).{0,200}(filename|file name)' ; then
      c_pass "$(basename "$f"): label v$LBL lags content v$NEW — lag is DECLARED in the first $HEAD_N lines (D32 satisfied)"
      # CLAUSE 2b — the declaration is itself a claim. Check its stated version too.
      DECL=$(declared_v_in "$f")
      if [ -n "${DECL:-}" ]; then
        if [ "$DECL" -ge "$NEW" ] 2>/dev/null; then
          c_pass "$(basename "$f"): the declaration's own version (v$DECL) is current"
        else
          c_fail "$(basename "$f"): THE DECLARATION IS ITSELF STALE — it says 'through v$DECL' but the file holds v$NEW"
          c_info "the D32 notice is doing its job (the lag is harmless) but its own number needs the same discipline"
        fi
      else
        c_warn "$(basename "$f"): declaration present but states no version — cannot check it"
      fi
    else
      c_fail "$(basename "$f"): label v$LBL lags content v$NEW by $((NEW-LBL)) versions, and NOTHING IN THE FILE SAYS SO"
      c_info "fix EITHER: rename the file and sweep references, OR add a source-of-truth notice (D32)"
    fi
  fi
done

# ---------------------------------------------------------------------------
head1 "CLAUSE 3 — byte-equality of files that must be identical (v251)"
# The v251 incident: a vendored copy silently diverged from its original. If the vault ever keeps
# two copies of one file, assert them equal here. Register pairs below as "A|B".
PAIRS=""   # e.g. PAIRS="PATTERN_LIBRARY.md|_patterns/PATTERN_LIBRARY.md"
if [ -z "$PAIRS" ]; then
  # Deliberately NOT a PASS. Per the NONVACUOUS rule above, a clause that examined nothing has
  # proved nothing — and the first draft of this script printed "PASS clause 3 vacuous", which is
  # precisely the green-on-nothing signal this whole file exists to prevent.
  c_warn "SKIPPED: no must-be-identical pairs registered — this clause proved nothing"
  c_info "register pairs in PAIRS= the first time the vault keeps two copies of one file"
else
  echo "$PAIRS" | tr ' ' '\n' | while IFS='|' read -r A B; do
    [ -z "${A:-}" ] && continue
    if [ ! -e "$A" ] || [ ! -e "$B" ]; then c_fail "pair missing: $A / $B"; continue; fi
    if cmp -s "$A" "$B"; then c_pass "byte-identical: $A == $B"; else c_fail "DIVERGED: $A != $B"; fi
  done
fi

# ---------------------------------------------------------------------------
head1 "CLAUSE 4 — retired/graveyard regression (v252)"
# context-os's best idea: when you DELETE an abstraction, the test is that it does not come back.
# _patterns/04-retired-stale.md is the vault's graveyard. Anything retired there must not be
# re-registered as live in _patterns/06's §C table.
GRAVE=_patterns/04-retired-stale.md
REG=_patterns/06-library-vocab-registry.md
if [ -e "$GRAVE" ] && [ -e "$REG" ]; then
  RES=0
  # pull quoted retired row titles; conservative — only long, distinctive quoted strings
  $GREP -oE '"[A-Z][^"]{25,90}"' "$GRAVE" 2>/dev/null | sort -u | head -40 | while read -r q; do
    T=$(echo "$q" | sed 's/^"//;s/"$//')
    if $GREP -qF "$T" "$REG" 2>/dev/null; then
      c_warn "retired title also appears in the live registry: ${T:0:66}..."
      c_info "confirm by hand whether this is a legitimate RE-REGISTER (the v184 §C#4 precedent) or a regression"
    fi
  done
  c_pass "graveyard scanned against the live registry (warnings above are for human adjudication)"
else
  c_warn "graveyard or registry file not found — clause 4 skipped"
fi

# ---------------------------------------------------------------------------
head1 "CLAUSE 5 — CLAUDE.md size budget (v253)"
# The shim is the subagent context floor. v167 established that regrowth past ~145K tokens breaks
# fan-out; v238 compacted it after every deep-dive workflow failed prompt-too-long since v200.
BYTES=$(wc -c < CLAUDE.md | tr -d ' ')
BUDGET=200000
printf "        CLAUDE.md = %s bytes (budget %s, ~%s tokens)\n" "$BYTES" "$BUDGET" "$((BYTES/4))"
if [ "$BYTES" -le "$BUDGET" ]; then
  c_pass "CLAUDE.md within budget"
else
  c_fail "CLAUDE.md is $((BYTES-BUDGET)) bytes over the ${BUDGET}-byte budget — compact the head blocks (see the v238 precedent)"
fi
# and the specific thing that regrows: accreted ★ head blocks
STARS=$($GREP -c '^\*\*★' CLAUDE.md 2>/dev/null || echo 0)
printf "        accreted head blocks (lines starting **★): %s\n" "$STARS"
[ "$STARS" -gt 12 ] && c_warn "$STARS head blocks — demote the oldest to _state/03c (they duplicate it)"

# ---------------------------------------------------------------------------
head1 "CLAUSE 6 — dated-stamp freshness (v253)"
# v253's decay stamp had two values in its entire life and was 23 days stale. If a doc claims a
# "last updated"/"as of" date, it should not be absurdly old relative to the newest ship.
STAMPS=$($GREP -ohE '(current through|as of|CURRENT HEAD[^0-9]{0,30})v?[0-9]{1,4}' CLAUDE.md 2>/dev/null | $GREP -oE 'v?[0-9]{1,4}$' | sed 's/^v//' | sort -n | tail -1)
NEWEST=$(for f in _state/*-projects-*.md; do [ -e "$f" ] && newest_v_in "$f"; done | sort -n | tail -1)
if [ -n "${STAMPS:-}" ] && [ -n "${NEWEST:-}" ]; then
  printf "        CLAUDE.md newest 'current through' marker: v%s | newest entry in _state: v%s\n" "$STAMPS" "$NEWEST"
  if [ "$STAMPS" -ge "$NEWEST" ] 2>/dev/null; then
    c_pass "CLAUDE.md's currency marker is not behind _state"
  else
    c_fail "CLAUDE.md claims currency through v$STAMPS but _state holds v$NEWEST"
  fi
else
  c_warn "could not extract a currency marker — clause 6 inconclusive"
fi

# ---------------------------------------------------------------------------
head1 "CLAUSE 7 — assert a count against a count (v254)"
# v254's headline: its script BUILT the deduplicated set, PRINTED its size (295), and never
# compared it to the 300 entry lines beside it. Seventeen weeks of a green job next to a wrong file.
# Rule: wherever a count is already computable, assert it against the count it must equal.

# 7a — the §C live-standalone figure quoted in CLAUDE.md vs the rows actually in _patterns/06
CLAIMED=$($GREP -ohE '§C live standalones ([0-9]+)|([0-9]+) live standalones' CLAUDE.md 2>/dev/null | $GREP -oE '[0-9]+' | sort -n | tail -1)
if [ -n "${CLAIMED:-}" ] && [ -e "$REG" ]; then
  printf "        CLAUDE.md claims §C live standalones = %s\n" "$CLAIMED"
  c_warn "the physical §C row count is not machine-derivable from _patterns/06 without a stable row marker"
  c_info "ACTION: give each live §C row a unique line prefix (e.g. '| C##' or '§C-###') and then this"
  c_info "        clause becomes exact. Until then this is the vault's own printed-295-beside-300."
  c_info "        The v203 audit already spent a session reconciling this by hand (45 physical rows"
  c_info "        -> 40 maintained). A row marker makes that reconciliation a one-liner, forever."
else
  c_warn "no §C standalone count found in CLAUDE.md — clause 7a skipped"
fi

# 7b — pattern counts must agree wherever they are stated
CNTS=$($GREP -ohE '[0-9]+ confirmed (top-level )?patterns' CLAUDE.md 2>/dev/null | $GREP -oE '^[0-9]+' | sort -u | tr '\n' ' ')
NCNT=$(echo "$CNTS" | wc -w | tr -d ' ')
printf "        distinct 'N confirmed patterns' values in CLAUDE.md: %s\n" "${CNTS:-none}"
if [ "$NCNT" -le 1 ]; then
  c_pass "the confirmed-pattern count is stated consistently"
else
  c_fail "CLAUDE.md states $NCNT DIFFERENT confirmed-pattern counts: $CNTS"
fi

# 7c — chapter index count vs actual files
IDX=$($GREP -c '`_state/[A-Za-z0-9._-]*\.md`' CLAUDE.md 2>/dev/null || echo 0)
ACT=$(ls _state/*.md 2>/dev/null | wc -l | tr -d ' ')
printf "        _state/ files referenced in CLAUDE.md: %s | files on disk: %s\n" "$IDX" "$ACT"

# ---------------------------------------------------------------------------
head1 "CLAUSE 8 — rename clause: match by identity, not current name (v254)"
# v254: my exact-pair corpus matcher missed two prior ships because the repos had been RENAMED
# (Hmbown/CodeWhale was v72 under a new name; ruvnet/claude-flow was v42 under an old one). Closing
# that took the count 13 -> 16. Any vault check that matches artifacts by their present name has
# the same hole.
c_info "advisory clause — no automated test. When a project folder or subject is renamed, the old"
c_info "name must survive as an alias, or every by-name check silently under-reports."
ALIAS_FILE="_state/aliases.tsv"
if [ -e "$ALIAS_FILE" ]; then
  c_pass "alias table present: $ALIAS_FILE ($(wc -l < "$ALIAS_FILE" | tr -d ' ') entries)"
else
  c_warn "no $ALIAS_FILE — renamed subjects will be missed by by-name checks"
  c_info "ACTION: create it as 'old_name<TAB>current_name<TAB>vNNN' the first time a subject is renamed"
fi

# ---------------------------------------------------------------------------
head1 "SUMMARY"
printf "  %s FAIL   %s WARN\n" "$FAILED" "$WARNED"
if [ "$FAILED" -eq 0 ]; then
  printf "  \033[32mall clauses pass\033[0m\n"
else
  printf "  \033[31m%s clause(s) failed\033[0m\n" "$FAILED"
fi
echo
echo "  Reminder (v250): a gate's AIM, not its quality, decides what rots."
echo "  Reminder (v254): a DECLARATION is a form of aim. Ask what you have never declared."
echo "  Reminder (v255): a stale label is safe when DECLARED and dangerous when merely COMPENSATED."
exit "$([ "$FAILED" -eq 0 ] && echo 0 || echo 1)"

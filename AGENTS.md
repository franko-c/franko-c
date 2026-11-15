# Rules for this repo

One file matters here: `README.md`, the GitHub profile. It is read by strangers
arriving from an issue comment or a link, so it has about twenty seconds.

## Before pushing

```bash
python3 check-voice.py README.md     # must be 0
```

## Voice

- **No "actually", and no not-just-X-but-Y.** Both imply a contrast with
  something fake. Say the thing or say the contrast outright.
- **No em dashes.** Comma, colon, or full stop.
- **No connector tics**: "Around that", "That said", "In short", "Beyond that".
- **Never use a construction twice in the same file.** The version that got
  called out used "because market hours and ..." in two sections five lines
  apart. `check-voice.py` greps for repeated 4-word runs, which is the only
  reason it was caught.
- Say what a thing does, not how it feels to build. No "passionate about",
  no "journey", no brochure adjectives.

## Links

**Almost every repo is private.** A repo link in this file 404s for everyone who is not the
owner, so the README points at what is running instead: ortaggi.co.uk and the market site. No repo
links (owner, 2026-11-15: the Zwift dashboard is out too).

Before pushing, check every link as a logged-out visitor:

```bash
grep -oE 'https?://[^)]+' README.md | sort -u | while read -r u; do
  printf "%s %s\n" "$(curl -s -o /dev/null -w '%{http_code}' -L --max-time 12 "$u")" "$u"
done
```

## Scope

`impeccable detect` measures a rendered page: line length, contrast, padding,
fonts. It does **not** read prose, so a clean impeccable run says nothing about
whether the copy is any good. Do not report one as the other.

Remaining impeccable findings on this README are GitHub's own 846px column at
14px and its system font stack. Neither is addressable from a README. Do not
rewrite copy chasing them.

## Language models: say so, plainly

Owner, 2026-11-15: be open that the work is built with large language models, Claude in
particular, and that the growth agent is Claude on a timer behind gates he wrote. This replaces the
earlier rule against mentioning them. Name the model and what it does; no "AI-powered" or other
brochure phrasing, which the voice rules above already forbid.

## Numbers

Every figure in the table is real and dated, with its source and window in the line under it:
Search Console (`agents/state/gsc-series.json` in wholesale-landing), the index counts
(`gsc-index-history.jsonl`), and agent merges from `agents/state/ledger.jsonl` (playbook not
"manual", gate_result "MERGED"). Compare like windows (28 days against the 28 before). When you
refresh one, refresh the date line with it; a stale number reads as a false one.

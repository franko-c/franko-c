#!/usr/bin/env python3
"""Reads README.md for the tics impeccable cannot see.

impeccable detect works on a rendered page: line length, contrast, padding,
font stacks. It has no view of prose, so "What I actually build" scored clean
on every run. This covers that gap and nothing else.
"""
import re, sys, itertools, collections

BANNED = {
    r"\bactually\b": "'actually' implies a contrast with something fake. Cut it or say the contrast",
    r"\bnot just\b|\bisn't just\b|\bmore than just\b": "the not-just-X-but-Y frame",
    r"\bit's worth noting\b|\bworth saying\b|\bto be clear\b|\bthe honest version\b": "self-conscious framing",
    r"\bat the end of the day\b|\bthat said\b|\bin short\b|\bthat being said\b": "filler connector",
    r"\bdive into\b|\bdeep dive\b|\bunpack\b": "dive/unpack",
    r"\bleverage\b|\bseamless\b|\brobust\b|\bpowerful\b|\bcutting.edge\b": "brochure adjective",
    r"\bpassionate about\b|\bjourney\b|\bcraft(ing)? beautiful\b": "personal-brand filler",
    r"\bend to end\b|\bfull.stack of\b": "filler intensifier",
    r"—": "em dash, reads as generated cadence",
    r"\bAround that\b|\bBeyond that\b|\bOn top of that\b": "connector tic",
}

def sentences(t):
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+", t) if s.strip()]

def main(path):
    raw = open(path, encoding="utf-8").read()
    # strip link targets and code so URLs do not create false hits
    text = re.sub(r"\]\([^)]*\)", "]", raw)
    text = re.sub(r"`[^`]*`", "", text)
    hits = 0

    for pat, why in BANNED.items():
        for m in re.finditer(pat, text, re.I):
            line = text[:m.start()].count("\n") + 1
            print(f"  line {line}: {m.group(0)!r} -> {why}")
            hits += 1

    # Repeated phrasing. This is the one that would have caught the real mistake:
    # "market hours and normal eating hours do not agree" five lines above
    # "market hours and daylight do not overlap much either".
    words = re.findall(r"[a-z']+", text.lower())
    grams = collections.Counter(" ".join(words[i:i+4]) for i in range(len(words) - 3))
    for gram, n in grams.items():
        if n > 1 and not all(w in {"the","a","of","and","to","in","for","it","is","on","so"} for w in gram.split()):
            print(f"  repeated {n}x: {gram!r} -> you have used this construction before in the same file")
            hits += 1

    print(f"\n{hits} issue{'' if hits == 1 else 's'}")
    return 1 if hits else 0

sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "README.md"))

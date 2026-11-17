#!/usr/bin/env python3
"""Render spec/v1/envelope.md to the plain-text source FX-1 tools read
(bin/fx1-skeleton --txt, bin/check-quotes, bin/check-locators, bin/bcp14-count).

    python3 -I render-source.py <envelope.md> .cache/in-toto-envelope-v1.txt

Input: content.url, sha256 = content.sha256 in record.yaml (checked).
Rules, a pure function of the input and this script:
- a Markdown ATX heading outside a code fence at level 2 becomes the column-0
  numbered heading "j.  Title", level 3 "j.k.  Title" (level 1, the title, is
  kept as text);
- every other line is copied byte for byte; no line is added or removed.
So line N of the rendering is line N of envelope.md, and "§3.1" means the
first level-3 heading under the third level-2 heading.
"""
import hashlib, re, sys

SHA256 = "c02c65880ccc117bbdecc6c916d5108541c1a864de67f8f9082efbaf15265d11"
ATX = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")

def main(src, out):
    b = open(src, "rb").read()
    got = hashlib.sha256(b).hexdigest()
    if got != SHA256:
        sys.exit(f"sha256 mismatch: {got}")
    lines = b.decode("utf-8").split("\n")
    o, ctr, fence = [], [], None
    for line in lines:
        s = line.lstrip()
        if s.startswith("```") or s.startswith("~~~"):
            tok = s[:3]
            fence = None if fence == tok else (fence or tok)
            o.append(line); continue
        m = ATX.match(line) if fence is None else None
        if m and len(m.group(1)) >= 2:
            lvl = len(m.group(1)) - 1
            ctr = (ctr + [0] * lvl)[:lvl]
            ctr[-1] += 1
            o.append(".".join(str(c) for c in ctr) + f".  {m.group(2)}")
        else:
            o.append(line)
    assert len(o) == len(lines)
    open(out, "w").write("\n".join(o))

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])

#!/usr/bin/env python3
"""Render SLSA v1.2 spec/build-provenance.md to the plain-text source FX-1 tools
read (bin/fx1-skeleton --txt, bin/check-quotes, bin/check-locators,
bin/bcp14-count).

    python3 -I render-source.py .cache/slsa-provenance-1-2.bin \
        .cache/slsa-provenance-1-2.include .cache/slsa-provenance-1-2.txt

Inputs, each checked by sha256 (record.yaml content.sha256 and content.note),
all from slsa-framework/slsa at ae7fc76215004e8fae250c877eff8919bf048e3b:
spec/build-provenance.md, and spec/schema/provenance.cue and
spec/schema/provenance.proto in the include directory.
Rules, a pure function of the inputs and this script:
- a line `{% include_relative schema/<f> %}` is replaced by the bytes of <f>,
  line for line (what the slsa.dev page shows at that point);
- a Markdown ATX heading outside a code fence at level 2 becomes the column-0
  numbered heading "j.  Title", level 3 "j.k.  Title" (no level 1 occurs; the
  title is in the YAML front matter, kept as text);
- every other line is copied byte for byte; no other line is added or removed.
So line N of the rendering is line N of build-provenance.md up to the first
include (L125), and each include shifts what follows by its line count less
one; "§4.2" means the second level-3 heading under the fourth level-2 heading.
"""
import hashlib, os, re, sys

SHA256 = {
    "build-provenance.md": "182ab5cf823c374874136371466ba43f99f0a9ba87a8046757d26a2ed74854a0",
    "provenance.cue": "0ddd00372622d1c04f71d1fb2666579af089eb733c9c5d838d158489b2ea6145",
    "provenance.proto": "ea548207a78bd81b809a449edd5ed36a011a665ca7d15831d1133fe674fc41de",
}
ATX = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
INC = re.compile(r"^\{% include_relative schema/([\w.]+) %\}$")

def read(path, name):
    b = open(path, "rb").read()
    got = hashlib.sha256(b).hexdigest()
    if got != SHA256[name]:
        sys.exit(f"{name}: sha256 mismatch: {got}")
    return b.decode("utf-8")

def main(src, incdir, out):
    lines = read(src, "build-provenance.md").split("\n")
    o, ctr, fence, n_inc = [], [], None, 0
    for line in lines:
        s = line.lstrip()
        if s.startswith("```") or s.startswith("~~~"):
            tok = s[:3]
            fence = None if fence == tok else (fence or tok)
            o.append(line); continue
        mi = INC.match(line)
        if mi:
            body = read(os.path.join(incdir, mi.group(1)), mi.group(1))
            o.extend(body.rstrip("\n").split("\n"))
            n_inc += 1
            continue
        m = ATX.match(line) if fence is None else None
        if m and len(m.group(1)) >= 2:
            lvl = len(m.group(1)) - 1
            ctr = (ctr + [0] * lvl)[:lvl]
            ctr[-1] += 1
            o.append(".".join(str(c) for c in ctr) + f".  {m.group(2)}")
        else:
            o.append(line)
    assert n_inc == 2, n_inc
    open(out, "w").write("\n".join(o))

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3])

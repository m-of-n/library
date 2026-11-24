#!/usr/bin/env python3
"""Normalise the section headings of draft-ietf-spki-cert-structure-06 so the
library's RFC reader (bin/_source_text.section_of_line) files each line under
its section.

    python3 -I render-source.py .cache/draft-ietf-spki-cert-structure.source.txt .cache/draft-ietf-spki-cert-structure.txt

The input is the fetched source of record (content.url, sha256 in record.yaml).
The draft writes subsection headings as "3.1 Canonical S-expression" (one
space, no trailing dot); RFCs write "3.1.  Title". A column-0 line matching
^(\\d+(\\.\\d+)*)\\.? (\\S.*)$ is rewritten as "<number>.  <title>". Nothing
else changes and no line is added or removed, so every line number and every
body line is identical to the source of record.
"""
import re, sys

H = re.compile(r"^(\d+(?:\.\d+)*)\.? (\S.*)$")

src, out = sys.argv[1], sys.argv[2]
lines = open(src, encoding="utf-8").read().split("\n")
n = 0
for i, l in enumerate(lines):
    m = H.match(l)
    if m:
        lines[i] = f"{m.group(1)}.  {m.group(2)}"
        n += 1
open(out, "w", encoding="utf-8").write("\n".join(lines))
print(f"{n} headings normalised, {len(lines)} lines")

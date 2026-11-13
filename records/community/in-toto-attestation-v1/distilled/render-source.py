#!/usr/bin/env python3
"""Render the in-toto Attestation Framework v1 spec files read for this record
to one plain-text source for FX-1 (bin/fx1-skeleton --txt, bin/check-quotes,
bin/check-locators, bin/bcp14-count all count lines in this rendering).

    python3 -I render-source.py <extracted attestation-<commit> dir> .cache/in-toto-attestation-v1.txt

Input: the GitHub source archive at commit df02077 (content.url; sha256 in
record.yaml), extracted. Output is a pure function of the 12 files below and
this script. Rules:
- file i (in the order below) opens with a column-0 heading "i.  <path>"
  between blank lines, followed by a line giving the file's own sha256;
- a Markdown ATX heading outside a code fence at level n>=1 becomes a
  column-0 numbered heading (level 1 -> "i.0.  Title" is NOT used: the level-1
  title is kept as text under the file heading; level 2 -> "i.j.  Title",
  level 3 -> "i.j.k.  Title", level 4 -> "i.j.k.l.  Title"), with a blank line
  inserted before it if the source has none;
- every other line is copied byte for byte.
So "§7.2" means file 7 (spec/v1/predicate.md... see the table in
distilled/README.md), second level-2 heading.
"""
import hashlib, os, re, sys

FILES = ["spec/README.md", "spec/v1/README.md", "spec/v1/statement.md",
         "spec/v1/resource_descriptor.md", "spec/v1/digest_set.md",
         "spec/v1/field_types.md", "spec/v1/predicate.md", "spec/v1/envelope.md",
         "spec/v1/bundle.md", "spec/v1/CHANGELOG.md", "spec/versioning.md",
         "docs/validation.md"]
ATX = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")

def main(root, out):
    o = []
    def blank_before():
        if o and o[-1].strip():
            o.append("")
    for i, f in enumerate(FILES, 1):
        b = open(os.path.join(root, f), "rb").read()
        blank_before()
        o.append(f"{i}.  {f}")
        o.append("")
        o.append(f"   [file sha256:{hashlib.sha256(b).hexdigest()}]")
        o.append("")
        ctr, fence = [], None
        for line in b.decode("utf-8").split("\n"):
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
                blank_before()
                o.append(f"{i}." + ".".join(str(c) for c in ctr) + f".  {m.group(2)}")
            else:
                o.append(line)
    text = "\n".join(o).rstrip("\n") + "\n"
    open(out, "w").write(text)

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])

#!/usr/bin/env python3
"""Render the DSSE specification files at commit 1d3370f to one plain-text
source for FX-1 (bin/fx1-skeleton --txt, bin/check-quotes, bin/check-locators,
bin/bcp14-count all count lines in this rendering).

    python3 -I render-source.py <archive.tar.gz> .cache/secure-systems-lab-dsse.txt

Input: content.url, the GitHub source archive at commit 1d3370f (sha256 =
content.sha256 in record.yaml, checked), read in memory; nothing is extracted
to disk. Each of the five files below is checked against its own sha256.
Output is a pure function of the archive and this script. Rules:

- file i (in the order below) opens with three added lines: a column-0
  heading "i.  <path>", a line "   [file sha256:<hex>]", and a blank line;
  file i > 1 is preceded by one more blank line. No other line is added;
- a Markdown file's lines are copied in place, byte for byte, except
  * an ATX heading outside a code fence at level n >= 2 becomes the column-0
    numbered heading "i.j.  Title" (level 2), "i.j.k.  Title" (level 3), and
    so on (a level-1 heading, the file title, is kept as text);
  * an ordered-list item at column 0 outside a code fence ("1.  Practical
    problem", background.md) is indented by one space, because every FX-1
    tool reads a column-0 "N.  " line as a numbered section heading
    (bin/_source_text.py NUMBERED); quotations compare with whitespace
    collapsed, so no quoted text changes;
- envelope.proto is copied byte for byte;
- the notebook is JSON, so it is rendered from its decoded cells: cell c opens
  with the line "   [cell c: markdown|code]" and a cell's source lines follow
  as decoded, then one blank line. The heading and list rules apply to
  markdown cells only; code cells are copied as decoded.
- cell outputs are not rendered: the envelopes and verification results the
  notebook recorded when it was run lie outside every line number here (the
  notebook is non-normative; its outputs come from a random key, ECC.generate).

So, for the four text files, line N of file i is line OFFSET[i] + N of the
rendering, where OFFSET is printed by --offsets (requirements.yaml's note and
normative.md's preamble state it; distilled/README.md is to tabulate it);
"§1.2" means file 1 (protocol.md), its second level-2 heading.
"""
import hashlib, io, json, re, sys, tarfile

ARCHIVE = "88fc65fd66d7250445dc08a65a2cb68c942fb88517152246f859a70d6dac3ac1"
PREFIX = "dsse-1d3370f62565bca041e97c8310b873ac340edc2e/"
FILES = [
    ("protocol.md", "6c0d965475162230f9f461acf634b4d4b409eab1a1839d31a9c24c76b3676253"),
    ("envelope.md", "3a8e7370671354cf3d3417c818a44dcda02cbc57dce6f4b6a75a84c41c483074"),
    ("envelope.proto", "2f689071f134f1a348ccc2af1e1cfa3f8a6ebed2a2576765dd55e764b0a0cbfb"),
    ("background.md", "a824667d3cbd6eedeb6f788a38bf4e690bd9b875381dbf809fda7bf48727bac4"),
    ("hypothetical_signature_attack.ipynb",
     "0a13a7ff7438b224ddc8e4d69dc535083cdc05807e2308abdc2e0516aedd8581"),
]
ATX = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
OL = re.compile(r"^\d+\.\s")


def markdown(lines, i, ctr):
    """Render Markdown lines in place; ctr carries heading numbers across
    notebook cells, which are one document."""
    o, fence = [], None
    for line in lines:
        s = line.lstrip()
        if s.startswith("```") or s.startswith("~~~"):
            tok = s[:3]
            fence = None if fence == tok else (fence or tok)
            o.append(line); continue
        m = ATX.match(line) if fence is None else None
        if m and len(m.group(1)) >= 2:
            lvl = len(m.group(1)) - 1
            ctr[:] = (ctr + [0] * lvl)[:lvl]
            ctr[-1] += 1
            o.append(f"{i}." + ".".join(str(c) for c in ctr) + f".  {m.group(2)}")
        elif fence is None and OL.match(line):
            o.append(" " + line)
        else:
            o.append(line)
    assert len(o) == len(lines)
    return o


def render(archive):
    got = hashlib.sha256(archive).hexdigest()
    if got != ARCHIVE:
        sys.exit(f"archive sha256 mismatch: {got}")
    tf = tarfile.open(fileobj=io.BytesIO(archive), mode="r:gz")
    o, offsets = [], {}
    for i, (name, sha) in enumerate(FILES, 1):
        b = tf.extractfile(PREFIX + name).read()
        h = hashlib.sha256(b).hexdigest()
        if h != sha:
            sys.exit(f"{name}: sha256 mismatch: {h}")
        if o:
            o.append("")
        o += [f"{i}.  {name}", f"   [file sha256:{h}]", ""]
        offsets[name] = len(o)
        text = b.decode("utf-8")
        if name.endswith(".md"):
            o += markdown(text.split("\n"), i, [])
        elif name.endswith(".proto"):
            o += text.split("\n")
        else:
            ctr = []
            for c, cell in enumerate(json.loads(text)["cells"]):
                src = "".join(cell["source"]).split("\n")
                o.append(f"   [cell {c}: {cell['cell_type']}]")
                o += markdown(src, i, ctr) if cell["cell_type"] == "markdown" else src
                o.append("")
    return o, offsets


def main(argv):
    if argv[1] == "--offsets":
        _, offsets = render(open(argv[2], "rb").read())
        for k, v in offsets.items():
            print(f"{k}\t{v}")
        return
    o, _ = render(open(argv[1], "rb").read())
    open(argv[2], "w").write("\n".join(o))


if __name__ == "__main__":
    main(sys.argv)

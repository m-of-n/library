#!/usr/bin/env python3
"""Render the Sigstore bundle v0.3 sources to the one plain-text file FX-1 tools
read (bin/fx1-skeleton --txt, bin/check-quotes, bin/check-locators,
bin/bcp14-count).

    python3 -I render-source.py .cache/sigstore-bundle-0-3.bin \
        .cache/sigstore-bundle-0-3.include .cache/sigstore-bundle-0-3.txt

Inputs, each checked by sha256 (record.yaml content.sha256 and content.note):

  sigstore_bundle.proto  = .cache/sigstore-bundle-0-3.bin (content.url)
  envelope.proto, sigstore_common.proto, sigstore_rekor.proto
                         the three files sigstore_bundle.proto imports from the
                         same repository (sigstore/protobuf-specs, tag v0.5.2 =
                         commit 0342fe5797edd558c58098033220fb27a2542a28,
                         protos/); google/api and google/protobuf imports are
                         not Sigstore's and are not spliced
  bundle.md              the "Sigstore Bundle Format" page, sigstore/docs
                         content/en/about/bundle.md at commit
                         8aed8c10af27107f3d4fc3d807e85b9ddabedc8e
                         (docs.sigstore.dev/about/bundle/ is built from it)

Rules, a pure function of the inputs and this script:

- The rendering is five parts in this order: sigstore_bundle.proto (§1), then
  its Sigstore imports in import order, envelope.proto (§2),
  sigstore_common.proto (§3), sigstore_rekor.proto (§4), then bundle.md (§5).
- Each part opens with one generated heading line `N.  <path> (<repo> @ <commit>)`
  and one blank line; every part after the first is preceded by one blank line.
- In a .proto part, every column-0 `message` or `enum` declaration gets a
  generated heading `N.k.  message Name` (or `enum Name`), inserted above the
  contiguous run of column-0 `//` comment lines directly over the declaration
  (the declaration's own documentation), as a blank line, the heading, and a
  blank line.
- In a .proto part, a line whose first non-space characters are `//` (a
  comment line) has those two characters replaced by two spaces, in place, so
  every other character keeps its column; an empty comment line becomes a
  blank line, which is the paragraph break the comment author wrote. A
  comment line never starts at column 0 afterwards, so none can be read as a
  heading. Every other proto line (code, including a code line with a
  trailing comment) is copied byte for byte, and a generated blank line
  separates it from any adjacent non-blank line, so a declaration is never
  read as part of a comment's sentence and each field (with its
  `field_behavior` annotation) is its own paragraph.
- In the Markdown part, an ATX heading outside a code fence at level L >= 2
  becomes the column-0 numbered heading `5.j.  Title` (L = 2),
  `5.j.k.  Title` (L = 3), and so on, in place; a column-0 ordered-list item
  outside a fence gets a one-space indent (the page has none; the rule is
  kept so a later pin cannot file one as a heading). Every other line is
  copied byte for byte.

So each source line appears exactly once, in order: unchanged, except the
Markdown headings (renumbered) and proto comment lines (marker blanked); the
generated lines are part and declaration headings and blank lines. The offset table printed with --map gives, for each
part, the rendering line of its source line 1, and every generated line.
"""
import hashlib, os, re, sys

SHA256 = {
    "sigstore_bundle.proto": "bf8d01cc4a52f8485f5eb795f499396f2e05cc4e0e45d131375b4c780b190792",
    "envelope.proto": "fb429d7013feb7b949002225addf6eb35605195033fa00106a2d9eba1828454e",
    "sigstore_common.proto": "b64c874fb5831bb599872370528d262a211c6b4c9ab5f33db714767dd973a83f",
    "sigstore_rekor.proto": "6c8820365ece6f9cf39ec7d127c972806eb9fb86ab259d3e3be20786d04eb1b8",
    "bundle.md": "8d1127003af7032392c24f1453ceb2a6043d9dd5706719122cc3f74dd4746df0",
}
PB = "sigstore/protobuf-specs @ 0342fe5"
DOCS = "sigstore/docs @ 8aed8c1"
PARTS = [
    ("sigstore_bundle.proto", f"protos/sigstore_bundle.proto ({PB})"),
    ("envelope.proto", f"protos/envelope.proto ({PB})"),
    ("sigstore_common.proto", f"protos/sigstore_common.proto ({PB})"),
    ("sigstore_rekor.proto", f"protos/sigstore_rekor.proto ({PB})"),
    ("bundle.md", f"content/en/about/bundle.md ({DOCS})"),
]
ATX = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
DECL = re.compile(r"^(message|enum)\s+(\w+)\s*\{")
OL = re.compile(r"^\d+\.\s")
COMMENT = re.compile(r"^(\s*)//(.*)$")


def read(path, name):
    b = open(path, "rb").read()
    got = hashlib.sha256(b).hexdigest()
    if got != SHA256[name]:
        sys.exit(f"{name}: sha256 mismatch: {got}")
    text = b.decode("utf-8")
    assert text.endswith("\n"), name
    return text[:-1].split("\n")


def proto(n, lines):
    """(line, source line number or None) for one proto part."""
    starts = {}
    for i, l in enumerate(lines):
        m = DECL.match(l)
        if m:
            j = i
            while j > 0 and lines[j - 1].startswith("//"):
                j -= 1
            starts[j] = f"{m.group(1)} {m.group(2)}"
    o, k = [], 0
    for i, l in enumerate(lines):
        if i in starts:
            k += 1
            if o and o[-1][0].strip():
                o.append(("", None, False))
            o += [(f"{n}.{k}.  {starts[i]}", None, False), ("", None, False)]
        m = COMMENT.match(l)
        code = bool(l.strip()) and not m
        prev_code = bool(o) and o[-1][2]
        if l.strip() and o and o[-1][0].strip() and (code or prev_code):
            o.append(("", None, False))
        o.append(((m.group(1) + "  " + m.group(2)) if m else l, i + 1, code))
    return [(l, s) for l, s, *_ in o]


def markdown(n, lines):
    o, ctr, fence = [], [], None
    for i, line in enumerate(lines):
        s = line.lstrip()
        if s.startswith("```") or s.startswith("~~~"):
            tok = s[:3]
            fence = None if fence == tok else (fence or tok)
            o.append((line, i + 1)); continue
        m = ATX.match(line) if fence is None else None
        if m and len(m.group(1)) >= 2:
            lvl = len(m.group(1)) - 1
            ctr = (ctr + [0] * lvl)[:lvl]
            ctr[-1] += 1
            o.append((f"{n}." + ".".join(str(c) for c in ctr) + f".  {m.group(2)}", i + 1))
        elif fence is None and OL.match(line):
            o.append((" " + line, i + 1))
        else:
            o.append((line, i + 1))
    return o


def render(src, incdir):
    out, table = [], []
    for n, (name, title) in enumerate(PARTS, 1):
        path = src if n == 1 else os.path.join(incdir, name)
        lines = read(path, name)
        if out:
            out.append(("", None, None))
        out += [(f"{n}.  {title}", None, None), ("", None, None)]
        body = markdown(n, lines) if name.endswith(".md") else proto(n, lines)
        assert sum(1 for _, s in body if s) == len(lines), name
        first = len(out) + 1
        out += [(l, name, s) for l, s in body]
        table.append((n, name, first, len(out)))
    return out, table


def main(argv):
    show = "--map" in argv
    argv = [a for a in argv if a != "--map"]
    out, table = render(argv[0], argv[1])
    open(argv[2], "w").write("\n".join(l for l, _, _ in out) + "\n")
    if show:
        for n, name, a, b in table:
            print(f"§{n} {name}: rendering L{a}-L{b}")
        for i, (l, name, s) in enumerate(out, 1):
            if s is None and l:
                print(f"  L{i} generated: {l}")


if __name__ == "__main__":
    main(sys.argv[1:])

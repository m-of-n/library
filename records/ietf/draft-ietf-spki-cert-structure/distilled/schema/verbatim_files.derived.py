#!/usr/bin/env python3
"""DERIVED - not verbatim. Builds and checks the three VERBATIM files in this
directory from the source, so that their bytes are never typed.

    python3 -I verbatim_files.derived.py --write   [SOURCE]   # (re)write them
    python3 -I verbatim_files.derived.py --check   [SOURCE]   # compare; exit 1 on drift

SOURCE defaults to <repo>/.cache/draft-ietf-spki-cert-structure.txt, the source
of record with only its section headings normalised (same line numbers, body
lines identical, see ../render-source.py).

A verbatim file is a header (lines starting "# ", written here) plus blocks:

    # @frag <section> L<a>-<b>
    <source lines a..b, byte for byte, one per line>

Page furniture is the ONLY thing left out of a block: the page footer
("Ellison, et al.   [Page N]"), the blank run before it, the form feed, the
running header ("INTERNET-DRAFT ... 26 July 1999") and the blank run after
it. That is the rule of bin/_source_text.clean EXTENDED by one thing: this
draft's running header is not an "RFC nnnn ..." line, so clean() keeps it (and
the blank run after it) as text; this file removes it. Elided line numbers
are recorded in the block's "# elided" comment.
"""
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
DEFAULT_SRC = ROOT / ".cache" / "draft-ietf-spki-cert-structure.txt"

FOOTER = re.compile(r"^\S.*\[Page \d+\]\s*$")
HEADER = re.compile(r"^INTERNET-DRAFT .*\d{4}\s*$")

# ---------------------------------------------------------------- fragments
# (section, first line, last line). Every production the draft prints outside
# section 9, plus the definitions that section 9 repeats. Section 9.2 is its own file.
FRAGMENTS = [
    ("§3.2", 589, 594),
    ("§3.2.1", 602, 602),
    ("§3.3", 623, 624),
    ("§3.8.1", 788, 789),
    ("§3.8.2", 999, 999),
    ("§3.8.3", 1014, 1014),
    ("§3.8.3.1", 1033, 1034),
    ("§4", 1147, 1148),
    ("§4.1", 1169, 1169),
    ("§4.2", 1183, 1183),
    ("§4.3", 1204, 1204),
    ("§4.3", 1206, 1206),
    ("§4.4", 1216, 1216),
    ("§4.5", 1230, 1230),
    ("§4.5", 1232, 1233),
    ("§4.5", 1237, 1237),
    ("§4.5.1", 1261, 1261),
    ("§4.5.2", 1271, 1272),
    ("§4.5.3", 1287, 1287),
    ("§4.6", 1360, 1360),
    ("§4.7", 1379, 1379),
    ("§4.8", 1389, 1389),
    ("§4.9", 1420, 1420),
    ("§4.9", 1422, 1422),
    ("§4.9", 1430, 1430),
    ("§4.9.1", 1443, 1443),
    ("§4.9.2", 1460, 1463),
    ("§4.10", 1550, 1550),
    ("§5.1", 1636, 1640),
    ("§5.2", 1676, 1682),
    ("§6.1", 1782, 1782),
    ("§6.1", 1784, 1785),
    ("§6.2", 1831, 1836),
    ("§7.1", 1919, 1923),
    ("§7.2", 1952, 1953),
    ("§7.3", 1973, 1973),
    ("§7.3", 1975, 1975),
    ("§8.1", 2027, 2039),
]

S9_2 = [("§9.2", 2257, 2371)]
S9_INTRO = [("§9", 2230, 2232), ("§9.1", 2238, 2251)]

FILES = {
    "bnf-s9-2-alphabetical.verbatim.bnf": (S9_2, "§9.2 Alphabetical List of BNF Rules, the whole list"),
    "bnf-s9-intro-s9-1.verbatim.txt": (S9_INTRO, "§9 introduction and §9.1 Top Level Objects (prose, no productions)"),
    "bnf-fragments-s3-s8.verbatim.bnf": (FRAGMENTS, "every BNF production printed outside section 9 (§3, §4, §5, §6, §7, §8.1)"),
}


def read_source(path=DEFAULT_SRC):
    return pathlib.Path(path).read_text(encoding="utf-8").split("\n")


def furniture(src):
    """set of 1-based line numbers that are page furniture."""
    n = len(src)
    gone = set()
    for k in range(n):
        if FOOTER.match(src[k].replace("\f", "")):
            j = k - 1
            while j >= 0 and not src[j].replace("\f", "").strip():
                gone.add(j + 1)
                j -= 1
            gone.add(k + 1)
            j = k + 1
            while j < n and (not src[j].replace("\f", "").strip() or HEADER.match(src[j].replace("\f", ""))):
                gone.add(j + 1)
                j += 1
    return gone


def block(src, gone, sec, a, b):
    kept = [l for l in range(a, b + 1) if l not in gone]
    elided = [l for l in range(a, b + 1) if l in gone]
    out = [f"# @frag {sec} L{a}-{b}"]
    if elided:
        out.append(f"# elided page furniture: L{elided[0]}-{elided[-1]} ({len(elided)} lines)")
    out += [src[l - 1] for l in kept]
    return out


def header(fname, desc):
    return [
        f"# VERBATIM: {desc}.",
        "# Source: draft-ietf-spki-cert-structure-06 (Ellison et al., 26 July 1999), source lines as numbered",
        "# in .cache/draft-ietf-spki-cert-structure.txt. Lines starting '# ' are this library's annotation;",
        "# every other line is a source line byte for byte (page furniture elided and listed).",
        f"# Rebuilt and checked by verbatim_files.derived.py; file: {fname}",
        "#",
    ]


def build(src, fname):
    frags, desc = FILES[fname]
    gone = furniture(src)
    out = header(fname, desc)
    for sec, a, b in frags:
        out += block(src, gone, sec, a, b)
        out.append("")
    return "\n".join(out) + "\n"


def parse_file(text):
    """[(section, a, b, [body lines])] of a verbatim file."""
    out, cur = [], None
    for l in text.split("\n"):
        m = re.match(r"^# @frag (\S+) L(\d+)-(\d+)$", l)
        if m:
            cur = [m.group(1), int(m.group(2)), int(m.group(3)), []]
            out.append(cur)
            continue
        if cur is None or l.startswith("# elided"):
            continue
        cur[3].append(l)
    for c in out:  # drop the one blank separator line after each block
        while c[3] and c[3][-1] == "":
            c[3].pop()
    return out


def check(src, fname, path):
    text = path.read_text(encoding="utf-8")
    if text != build(src, fname):
        return [f"{fname}: differs from the source (rebuild with --write)"]
    gone = furniture(src)
    bad = []
    for sec, a, b, body in parse_file(text):
        want = [src[l - 1] for l in range(a, b + 1) if l not in gone]
        while want and want[-1] == "":
            want.pop()
        if body != want:
            bad.append(f"{fname}: {sec} L{a}-{b} differs")
    return bad


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    src = read_source(args[0] if args else DEFAULT_SRC)
    mode = "--write" if "--write" in sys.argv else "--check"
    bad = []
    n = 0
    for fname in FILES:
        p = HERE / fname
        if mode == "--write":
            p.write_text(build(src, fname), encoding="utf-8")
        n += 1
        bad += check(src, fname, p)
    print(f"verbatim_files: examined {n} files, {sum(len(f[0]) for f in FILES.values())} blocks, {len(bad)} mismatched")
    for b in bad:
        print("  " + b)
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()

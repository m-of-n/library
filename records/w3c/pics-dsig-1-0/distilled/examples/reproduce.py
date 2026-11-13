#!/usr/bin/env python3
"""Reproduce every check this directory makes about the examples of pics-dsig-1-0.

    python3 -I reproduce.py [PATH-TO-.cache/pics-dsig-1-0.bin]

(a) every fixture, and every verbatim grammar file in ../schema, is byte-identical
    to the HTML <pre> block it came from. The blocks are re-read here with
    html.parser; the files were written with a regular expression, so the two
    readers are independent. All 27 <pre> blocks of the document are accounted
    for, none twice. The fixture lines are also compared with the .txt rendering.
(b) each fixture is parsed against ../schema/check-grammar.derived.py, in the
    PICS 1.1 profile and the DSig profile, strict and with placeholders allowed.
(c) the canonical form is recomputed from Step 2 and from Step 4 of the source's
    "An Example" and compared with the printed Step 3. Differences are source
    defects, reported, not repaired.
(d) base64 values are decoded and their lengths compared with the digest the
    resinfo entry names (SHA1 20 bytes, MD5 16 bytes: facts about the algorithms,
    not statements of the source).
(e) the algorithm identifiers of Appendix 3 are compared with the ones the
    examples use.

Exit status 1 when (a) finds a difference or (b) a verdict differs from the
expectation recorded below. (c), (d), (e) report source defects and do not fail.

Signatures, and hashes of the labelled document, are NOT verified, and cannot be:
the source discloses no key (the values of "N", "E", "P", "Q", "G", "Y" are
placeholders, several are not even valid base64), no signed bytes, and not the
document "http://www.w3.org/PICS/DSig/Overview" that Step 2 hashes. Nothing here
fakes a verification.
"""
import base64
import binascii
import html.parser
import importlib.util
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
DIST = HERE.parent
ROOT = DIST.parents[3]
BIN = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / ".cache" / "pics-dsig-1-0.bin"
TXT = BIN.with_suffix(".txt")
BEGIN = "# ---- BEGIN VERBATIM"

# (file, <pre> index, HTML line, rendering line span, (section ordinal, title), kind)
MANIFEST = [('schema/resinfo-syntax.verbatim.txt', 5, 738, (220, 255), ('7.2.1', 'Detailed Syntax of the resinfo Extension in a PICS 1.1 Label'), 'schema'),
 ('schema/field-list-syntax.verbatim.txt',
  18,
  1072,
  (393, 396),
  ('7.3.4.7', 'The "include" and "exclude" tokens: modifying the canonicalized form of the label'),
  'schema'),
 ('schema/sigblock-syntax.verbatim.txt', 20, 1143, (439, 495), ('7.4.2', 'Detailed Syntax of the sigblock Extension in a PICS 1.1 Label'), 'schema'),
 ('examples/ex01-resinfo-extension.txt', 6, 776, (259, 263), ('7.2.1', 'Detailed Syntax of the resinfo Extension in a PICS 1.1 Label'), 'example'),
 ('examples/ex02-attribinfo.txt', 9, 889, (306, 312), ('7.3.2', 'Attribution Information'), 'example'),
 ('examples/ex03-bykey-dsa-sigdata.txt', 12, 990, (348, 352), ('7.3.4.2', '"ByKey"'), 'example'),
 ('examples/ex04-sigblock-extension.txt', 19, 1115, (415, 433), ('7.4.1', 'An example sigblock extension:'), 'example'),
 ('examples/ex05-step1-label.txt', 23, 1306, (545, 550), ('8.2', 'An Example'), 'example'),
 ('examples/ex06-step2-label-resinfo.txt', 24, 1314, (554, 564), ('8.2', 'An Example'), 'example'),
 ('examples/ex07-step3-canonical-form.txt', 25, 1329, (569, 575), ('8.2', 'An Example'), 'example'),
 ('examples/ex08-step4-signed-label.txt', 26, 1337, (579, 603), ('8.2', 'An Example'), 'example'),
 ('examples/templates/t00-label-list-service-sections.txt', 0, 340, (92, 95), ('5.1', 'PICS 1.1 labels and label lists'), 'template'),
 ('examples/templates/t01-service-section.txt', 1, 345, (99, 102), ('5.1', 'PICS 1.1 labels and label lists'), 'template'),
 ('examples/templates/t02-general-label-list.txt', 2, 351, (106, 115), ('5.1', 'PICS 1.1 labels and label lists'), 'template'),
 ('examples/templates/t03-label-4-equivalent.txt', 3, 367, (119, 122), ('5.1', 'PICS 1.1 labels and label lists'), 'template'),
 ('examples/templates/t04-resinfo-hash-entry.txt', 4, 694, (208, 208), ('7.2', 'Resource Reference Information Extension'), 'template'),
 ('examples/templates/t07-sigblock-structure.txt', 7, 847, (288, 290), ('7.3.1', 'Format Specification'), 'template'),
 ('examples/templates/t08-attribinfo-structure.txt', 8, 884, (299, 302), ('7.3.2', 'Attribution Information'), 'template'),
 ('examples/templates/t10-signature-syntax.txt', 10, 904, (318, 318), ('7.3.3', 'Signatures'), 'template'),
 ('examples/templates/t11-bykey-template.txt', 11, 985, (344, 344), ('7.3.4.2', '"ByKey"'), 'template'),
 ('examples/templates/t13-byhash.txt', 13, 1000, (358, 358), ('7.3.4.3', '"ByHash"'), 'template'),
 ('examples/templates/t14-byname.txt', 14, 1008, (366, 366), ('7.3.4.4', '"ByName"'), 'template'),
 ('examples/templates/t15-bycert.txt', 15, 1016, (372, 372), ('7.3.4.5', '"ByCert"'), 'template'),
 ('examples/templates/t16-on.txt', 16, 1027, (379, 379), ('7.3.4.6', 'The "On" token: Time of Signature generation'), 'template'),
 ('examples/templates/t17-include-exclude.txt',
  17,
  1048,
  (387, 388),
  ('7.3.4.7', 'The "include" and "exclude" tokens: modifying the canonicalized form of the label'),
  'template'),
 ('examples/templates/t21-signing-label-list.txt', 21, 1209, (501, 515), ('8', 'Signing'), 'template'),
 ('examples/templates/t22-standalone-label.txt', 22, 1243, (525, 528), ('8.1.1', 'Creating an equivalent standalone label'), 'template')]

# fixture -> (nonterminal, expected verdicts: pics11, dsig strict, dsig placeholder).
# "n/a": a fragment that is not an extension has no PICS 1.1 reading (the PICS 1.1 profile
# only changes how extension data is read). Under the PICS 1.1 profile the source's
# placeholders ("base64 hash", "base64-x.509-cert") lex as quotedname and are ACCEPTED.
EXPECT = {
    "ex01-resinfo-extension": ("resinfo-extension", ("ACCEPT", "REJECT", "ACCEPT")),
    "ex02-attribinfo": ("AttributionInfo", ("n/a", "REJECT", "ACCEPT")),
    "ex03-bykey-dsa-sigdata": ("SigData", ("n/a", "REJECT", "REJECT")),
    "ex04-sigblock-extension": ("sigblock-extension", ("ACCEPT", "REJECT", "ACCEPT")),
    "ex05-step1-label": ("label", ("ACCEPT", "ACCEPT", "ACCEPT")),
    "ex06-step2-label-resinfo": ("label", ("ACCEPT", "ACCEPT", "ACCEPT")),
    "ex07-step3-canonical-form": ("label", ("ACCEPT", "ACCEPT", "ACCEPT")),
    "ex08-step4-signed-label": ("label", ("ACCEPT", "ACCEPT", "ACCEPT")),
}

failures = 0


def load_grammar():
    p = DIST / "schema" / "check-grammar.derived.py"
    spec = importlib.util.spec_from_file_location("check_grammar", p)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


class PreReader(html.parser.HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.blocks, self._cur, self._line = [], None, 0

    def handle_starttag(self, tag, attrs):
        if tag == "pre":
            self._cur, self._line = [], self.getpos()[0]

    def handle_endtag(self, tag):
        if tag == "pre" and self._cur is not None:
            self.blocks.append((self._line, "".join(self._cur)))
            self._cur = None

    def handle_data(self, data):
        if self._cur is not None:
            self._cur.append(data)


def part_a(blocks, txt):
    global failures
    print("== (a) fixtures byte-identical to the HTML <pre> blocks")
    seen, diff, linediff = set(), 0, 0
    for fn, i, hl, span, sec, kind in MANIFEST:
        data = (DIST / fn).read_bytes().decode("utf-8")
        if kind == "schema":
            head, _, data = data.partition("\n" + BEGIN)
            data = data.partition("\n")[2]
        want_line, want = blocks[i]
        want = want.replace(" ", " ").replace("\r\n", "\n")
        ok = data == want and want_line == hl and i not in seen
        seen.add(i)
        # the .txt rendering, as lines, with U+00A0 written as a space
        s0, s1 = span
        r = [ln.replace(" ", " ").rstrip() for ln in txt[s0 - 1:s1]]
        f = [ln.rstrip() for ln in want.rstrip("\n").split("\n")]
        lok = r == f
        diff += not ok
        linediff += not lok
        print(f"  {'same' if ok else 'DIFF'} {'lines-same' if lok else 'LINES-DIFF'} pre {i:2d} html L{hl:<4d} txt L{s0}-{s1:<4d} §{sec[0]} ({sec[1]})  {fn}")
    missing = sorted(set(range(len(blocks))) - seen)
    print(f"  EXAMINED {len(MANIFEST)} files against {len(blocks)} <pre> blocks; DIFFERENT {diff}; "
          f"rendering-line DIFFERENT {linediff}; <pre> blocks with no file {missing or 'none'}")
    failures += diff + linediff + len(missing)


def tokens_of(text):
    return re.findall(r'"[^"]*"|[()]|[^\s()"]+', text)


def part_b(g):
    global failures
    print("== (b) each fixture against the derived grammar (pics11 | dsig strict | dsig placeholder)")
    notes_all = []
    tok_case = []
    for fn, i, hl, span, sec, kind in MANIFEST:
        if kind != "example":
            continue
        key = pathlib.Path(fn).stem
        nt, want = EXPECT[key]
        text = (DIST / fn).read_text(encoding="ascii")
        p11 = g.verdict(text, nt, "pics11", False) if want[0] != "n/a" else ("n/a", [])
        got = (p11, g.verdict(text, nt, "dsig", False), g.verdict(text, nt, "dsig", True))
        verd = tuple(x[0] for x in got)
        ok = verd == want
        global_fail = not ok
        failures += global_fail
        print(f"  {'ok ' if ok else 'BAD'} {key:28s} as {nt:18s} {' | '.join(verd)}   (expected {' | '.join(want)})")
        for label, (v, notes) in zip(("pics11", "dsig strict", "dsig placeholder"), got):
            if v == "REJECT":
                print(f"        {label}: {notes[0][:170]}")
            elif notes:
                notes_all.append((key, notes))
        for t in re.findall(r'\("([A-Za-z]+)"', text):
            for k in g.KNOWN_TOKENS:
                if t != k and t.lower() == k.lower():
                    tok_case.append((key, t, k))
    for key, notes in notes_all:
        print(f"  {key}: placeholder mode forgave {len(notes)} value(s): " + "; ".join(n.split(': ', 1)[1] for n in notes))
    for key, t, k in tok_case:
        print(f"  token-case: {key} writes \"{t}\" where section 7.3.4 names \"{k}\" (the BNF says quoted strings are case sensitive)")


def b64len(s):
    try:
        return len(base64.b64decode(s, validate=True))
    except (binascii.Error, ValueError):
        return None


def part_d():
    print("== (d) resinfo hash lengths against the named algorithm")
    size = {"SHA1": 20, "MD5": 16}
    bad = 0
    for key in ("ex01-resinfo-extension", "ex06-step2-label-resinfo", "ex07-step3-canonical-form", "ex08-step4-signed-label"):
        fn = next(m[0] for m in MANIFEST if pathlib.Path(m[0]).stem == key)
        text = (DIST / fn).read_text(encoding="ascii")
        for m in re.finditer(r'"http://www\.w3\.org/+TR/1998/REC-DSig-label/(SHA1|MD5)-1_0"\s+"([^"]*)"', text):
            algo, val = m.group(1), m.group(2)
            n = b64len(val)
            verdict = "ok" if n == size[algo] else "MISMATCH"
            bad += verdict != "ok"
            shown = f"decodes to {n} bytes" if n is not None else "is not RFC 1521 base64"
            print(f"  {verdict:8s} {key}: {algo} value {val!r} {shown}; a {algo} digest is {size[algo]} bytes")
    print(f"  {bad} resinfo hash value(s) cannot be a digest of the algorithm named; the source does not say they are placeholders and prints no real digest")
    print("  other base64-looking values (keys, signatures) cannot be checked: the source names no length for them")
    print("  every base64-position value of the example fixtures (keys, signatures, certificates, hashes):")
    pat = [r'\(\s*"(N|E|P|Q|G|Y|R|S|SigCrypto|ByHash)"\s+"([^"]+)"\s*\)',
           r'\(\s*"(http://www\.w3\.org/PICS/DSig/[A-Za-z0-9_-]+)"\s+"([^"]+)"\s*\)']
    seen64, nbad = set(), 0
    for fn, i, hl, span, sec, kind in MANIFEST:
        if kind != "example":
            continue
        stem = pathlib.Path(fn).stem
        body = (DIST / fn).read_text(encoding="ascii")
        for p in pat:
            for m in re.finditer(p, body):
                v = m.group(2)
                if v.startswith("http") or (stem, v) in seen64:
                    continue
                seen64.add((stem, v))
                n = b64len(v)
                nbad += n is None
                print(f"    {stem:28s} {m.group(1)[-12:]:12s} {v!r:24s} " + (f"valid base64, {n} bytes" if n is not None else f"NOT base64 (length {len(v)}" + (", not a multiple of four)" if len(v) % 4 else ")")))
    print(f"  {len(seen64)} distinct values examined, {nbad} not RFC 1521 base64; none can be checked against a key or a signed text")


# ----------------------------------------------------------------- (c) canonical form

OPT_SHORT = {"complete-label": "full", "until": "exp", "generic": "gen", "mic-md5": "md5", "signature-rsa-md5": "signature-rsa-md5"}
REMOVED = {"md5", "signature-rsa-md5"}          # 6.2: ignored, removed for signing
VALUED_AS_SYMBOL = {"gen"}


def canonical(g, text, lower_header=True, sort_resinfo=True, spaced_parens=True):
    """The recipe of section 8.1.2 and 8.1.1 as written, on one service with one label."""
    tr = g.tree(g.tokenise(text))
    items = tr[0]
    svc_url = items[1]
    i = 2
    svc_opts = []
    while g.is_sym(items[i]) and items[i][1].lower() in g.OPTION_WORDS:
        svc_opts.append((items[i][1].lower(), items[i + 1]))
        i += 2
    assert g.is_sym(items[i], "labels") or g.is_sym(items[i], "l")
    i += 1
    lbl_opts = []
    while g.is_sym(items[i]) and items[i][1].lower() in g.OPTION_WORDS:
        lbl_opts.append((items[i][1].lower(), items[i + 1]))
        i += 2
    assert g.is_sym(items[i], "ratings") or g.is_sym(items[i], "r")
    ratings = items[i + 1]
    # normalise to label options: a label's own option overrides a service option of the same name;
    # comment and extension may repeat, extensions are told apart by URL
    merged = {}
    for src in (svc_opts, lbl_opts):
        for w, v in src:
            w = OPT_SHORT.get(w, w)
            k = (w, v[1][1]) if w == "extension" else (w, len(merged) if w == "comment" else None)
            merged[k] = v
    out = []
    for (w, _), v in merged.items():
        if w in REMOVED:
            continue
        if w == "extension" and v[1][1] == g.SIGBLOCK_URL:
            continue       # 8.1.1: the sigblock extension has been removed
        out.append((w, v))
    def sortkey(p):
        w, v = p
        return (w, v[1][1] if w == "extension" else "")
    out.sort(key=sortkey)

    def flat(n):
        if g.is_list(n):
            return ["("] + [t for c in n for t in flat(c)] + [")"]
        return ['"%s"' % n[1]] if n[0] == "str" else [n[1].lower() if n[1].lower() in ("optional", "mandatory", "true", "false") else n[1]]

    toks = ["(", "pics-1.1" if lower_header else "PICS-1.1", '"%s"' % svc_url[1], "l"]
    for w, v in out:
        if w == "extension":
            body = v
            if sort_resinfo and body[1][1] == g.RESINFO_URL:
                body = body[:2] + sorted(body[2:], key=lambda d: d[0][1])
            toks += ["extension"] + flat(body)
        else:
            toks += [w] + flat(v)
    pairs = []
    j = 0
    while j < len(ratings):
        pairs.append((ratings[j][1], ratings[j + 1]))
        j += 2
    toks += ["r", "("]
    for name, v in sorted(pairs):
        toks += [name] + flat(v)
    toks += [")", ")"]
    if spaced_parens:
        return " ".join(toks)
    return "(" + " ".join(toks[1:-1]) + ")"


def part_c(g):
    print("== (c) canonical form recomputed (section 8.1.2, 8.1.1) against the printed Step 3")
    rd = lambda stem: next((DIST / m[0]).read_text(encoding="ascii") for m in MANIFEST if pathlib.Path(m[0]).stem == stem)
    printed = rd("ex07-step3-canonical-form")
    step2, step4 = rd("ex06-step2-label-resinfo"), rd("ex08-step4-signed-label")
    norm = lambda s: " ".join(s.split())
    p = norm(printed)
    print(f"  printed Step 3, display line breaks collapsed (the source says they are display only):\n    {p}")
    variants = [
        ("as written: header lower-cased, no space inside the outer parentheses", dict(spaced_parens=False)),
        ("as written, with the outer parentheses spaced like every other token", dict(spaced_parens=True)),
        ("header NOT lower-cased, outer parentheses spaced (the printed shape)", dict(lower_header=False, spaced_parens=True)),
    ]
    for src_name, src in (("Step 2", step2), ("Step 4 (sigblock removed by the recipe)", step4)):
        for label, kw in variants:
            c = canonical(g, src, **kw)
            print(f"  from {src_name}, {label}: {'IDENTICAL' if c == p else 'DIFFERENT'}")
            if c != p:
                ct, pt = c.split(" "), p.split(" ")
                diffs = [(a, b) for a, b in zip(ct, pt) if a != b]
                print(f"      computed {len(ct)} tokens, printed {len(pt)}; first differing token pairs (computed, printed): {diffs[:4]}")
    nores = canonical(g, step2, lower_header=False, sort_resinfo=False)
    print(f"  without ordering the resinfo hashes (the recipe says nothing about them): {'IDENTICAL' if nores == p else 'DIFFERENT'} "
          "(Step 2 lists SHA1 then MD5; Step 3 prints MD5 then SHA1)")
    a = canonical(g, step2, lower_header=False)
    b = canonical(g, step4, lower_header=False)
    print(f"  Step 2 and Step 4 reduce to the same canonical form: {'yes' if a == b else 'NO'}")
    print("  printed Step 3, exact bytes: the header symbol is 'PICS-1.1' in upper case; the recipe says symbols are lower-cased and the header is the 'pics-1.1' symbol")
    print(f"  printed Step 3 has a space after its first parenthesis and before its last: {printed.startswith('( ')} / {printed.rstrip().endswith(' )')}. "
          "The sentence about the outer parentheses has two readings: no space between the outer parenthesis and its neighbour token (the printed text then breaks it), "
          "or no leading or trailing whitespace on the line (the printed text then keeps it). Only the case of the header symbol differs under the second reading.")


def part_e(txt):
    print("== (e) Appendix 3 identifiers against the identifiers the examples use")
    app = [ln for ln in txt if "http://www.w3.org" in ln and ("hashing" in ln)]
    ids = re.findall(r"\((http://www\.w3\.org/+TR/1998/REC-DSig-label/[A-Za-z0-9_-]+)\)", " ".join(app))
    used = set()
    for fn, i, hl, span, sec, kind in MANIFEST:
        if kind == "example":
            used |= set(re.findall(r'"(http://www\.w3\.org/TR/1998/REC-DSig-label/[A-Za-z0-9_-]+)"', (DIST / fn).read_text(encoding="ascii")))
    for u in ids:
        print(f"  Appendix 3: {u}   {'also used by an example' if u in used else 'NOT the spelling the examples use' if u.replace('//TR', '/TR') in used else 'not used by an example'}")
    dbl = [u for u in ids if "//TR" in u]
    print(f"  {len(dbl)} of {len(ids)} Appendix 3 identifiers contain a double slash after the host; the examples and the extension names use a single slash. Identifiers are compared as strings, so these name different suites unless a consumer normalises.")


def main():
    global failures
    raw = BIN.read_bytes().decode("utf-8")
    rd = PreReader()
    rd.feed(raw)
    blocks = rd.blocks
    txt = TXT.read_text(encoding="utf-8").split("\n")
    g = load_grammar()
    print(f"source {BIN.name}: {len(raw)} bytes decoded, {len(blocks)} <pre> blocks; rendering {len(txt)} lines")
    part_a(blocks, txt)
    part_b(g)
    part_c(g)
    part_d()
    part_e(txt)
    print(f"FAILURES {failures}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())

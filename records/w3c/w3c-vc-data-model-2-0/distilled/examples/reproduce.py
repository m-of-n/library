#!/usr/bin/env python3
"""reproduce.py -- re-extract every example fixture of the W3C Verifiable
Credentials Data Model v2.0 REC from its HTML and diff against this directory.

    python3 -I reproduce.py PATH/TO/w3c-vc-data-model-2-0.bin           # check
    python3 -I reproduce.py PATH/TO/w3c-vc-data-model-2-0.bin --write DIR  # (re)write fixtures into DIR

The source is the REC HTML (sha256 a9196a3d0b6601356c4e127bad24f8c7f2c17f6ed22e41b35755a910104156f8 = content.sha256 in
record.yaml). The bytes are never copied into the repository; this script is how a
reader gets back from the source to every file here.

What a fixture is. Every element of the HTML that displays an example payload:
  <pre>                      (112)  text content, <br> read as LF, entities decoded
  <div class="jwt-compact">  (9)   text content (JWS compact serialisation, newlines between the parts kept)
  <div class="sd-jwt-compact"> (9)
  <div class="cose-text">    (9)   hex of a COSE_Sign1
  <div class="disclosure">   (36)  the Claim / SHA-256 Hash / Disclosure(s) / Contents display of one SD-JWT disclosure
all inside the 40 <div class="example"> elements. Syntax-highlighting <span>s that
respec added (hljs-*, highlight, comment, vc-hash) are dropped and their text kept;
nothing else is altered: a non-breaking space stays U+00A0, a trailing LF stays. The file
bytes are the UTF-8 of that text. No file is a rendering from the .txt (the .txt inserts a
space at span boundaries).

Checks (EXAMINED beside FOUND): (1) sha256 of the .bin; (2) the stdlib-HTMLParser
extractor and an independent regex extractor agree on every <pre>; (3) every fixture the
extractor produces exists here with identical bytes; (4) nothing else is here with a
fixture-shaped name; (5) the counts. Exit 1 on any difference.
"""
import hashlib, html, os, re, sys
from html.parser import HTMLParser

SRC_SHA256 = "a9196a3d0b6601356c4e127bad24f8c7f2c17f6ed22e41b35755a910104156f8"
EXPECT = {"examples": 40, "pre": 112, "jwt-compact": 9, "sd-jwt-compact": 9, "cose-text": 9, "disclosure": 36, "fixtures": 175}
VOID = {"br", "input", "img", "hr", "meta", "link", "col", "source", "wbr", "area", "base", "embed", "param", "track"}


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


class X(HTMLParser):
    def __init__(s):
        super().__init__(convert_charrefs=True)
        s.stack, s.examples, s.cur = [], [], None
        s.sec, s.in_secno, s.secbuf = None, False, []
        s.capture, s.capinfo = None, None
        s.tabbed, s.strong_buf, s.label = [], None, None
        s.title_buf, s.exnum_buf, s.lab = None, None, None

    def handle_starttag(s, tag, attrs):
        a = dict(attrs)
        cls = (a.get("class") or "").split()
        if s.capture:
            k, buf, d = s.capture
            if tag == "br":
                buf.append("\n")
            elif tag not in VOID:
                s.capture = (k, buf, d + 1)
            return
        if tag in VOID:
            return
        s.stack.append(dict(tag=tag, cls=cls, id=a.get("id")))
        if tag == "bdi" and "secno" in cls:
            s.secbuf, s.in_secno = [], True
        if tag == "div" and "example" in cls and s.cur is None:
            s.cur = dict(id=a.get("id"), number=None, title=None, section=s.sec, blocks=[])
            s.examples.append(s.cur)
        if s.cur is None:
            return
        if tag == "div" and "marker" in cls and s.cur["number"] is None:
            s.exnum_buf = []
        if tag == "span" and "example-title" in cls:
            s.title_buf = []
        if tag == "div" and "vc-tabbed" in cls:
            s.tabbed.append(dict(labels=[], n=0))
        if tag == "abbr" and s.tabbed and any("vc-tab" in fr["cls"] for fr in s.stack):
            s.lab = [a.get("title"), []]
        if tag == "div" and "vc-tab-content" in cls and s.tabbed:
            s.tabbed[-1]["n"] += 1
            s.label = None
        if tag == "div" and ("sd-jwt-tab-content" in cls or "vc-jose-cose-jwt-tab-content" in cls):
            s.label = None
        if tag == "strong":
            s.strong_buf = []
        kind = None
        if tag == "pre":
            kind = "pre"
        elif tag == "div":
            for c in ("jwt-compact", "sd-jwt-compact", "cose-text", "disclosure"):
                if c in cls:
                    kind = c
        if kind:
            tb = s.tabbed[-1] if s.tabbed else None
            vctab = tb["labels"][tb["n"] - 1] if tb and 0 < tb["n"] <= len(tb["labels"]) else None
            sdtab = next((fr["id"].rsplit("-content-", 1)[1] for fr in reversed(s.stack) if fr["id"] and "-content-" in fr["id"]), None)
            s.capture = (kind, [], 1)
            s.capinfo = dict(kind=kind, cls=cls, vctab=vctab, sdtab=sdtab, label=s.label, html_line=s.getpos()[0])

    def handle_endtag(s, tag):
        if s.capture:
            k, buf, d = s.capture
            if tag in VOID:
                return
            d -= 1
            if d == 0:
                s.cur["blocks"].append(dict(s.capinfo, text="".join(buf)))
                s.capture = None
                while s.stack and s.stack[-1]["tag"] != tag:
                    s.stack.pop()
                if s.stack:
                    s.stack.pop()
                return
            s.capture = (k, buf, d)
            return
        if tag in VOID:
            return
        if s.stack and s.stack[-1]["tag"] == tag:
            f = s.stack.pop()
        else:
            idx = next((i for i in range(len(s.stack) - 1, -1, -1) if s.stack[i]["tag"] == tag), None)
            if idx is None:
                return
            del s.stack[idx:]
            f = dict(tag=tag, cls=[], id=None)
        if tag == "bdi" and s.in_secno:
            s.in_secno = False
            t = "".join(s.secbuf).strip()
            if re.match(r"^([A-Z]|\d+)(\.\d+)*\.?$", t) and any(fr["tag"] in ("h2", "h3", "h4", "h5", "h6") for fr in s.stack):
                s.sec = t.rstrip(".")
        if tag == "strong" and s.strong_buf is not None:
            t = "".join(s.strong_buf).strip()
            if t:
                s.label = t
            s.strong_buf = None
        if tag == "abbr" and s.lab is not None:
            s.tabbed[-1]["labels"].append((s.lab[0], "".join(s.lab[1]).strip()))
            s.lab = None
        if tag == "div" and "vc-tabbed" in f["cls"] and s.tabbed:
            s.tabbed.pop()
        if tag == "span" and s.title_buf is not None and "example-title" in f["cls"]:
            s.cur["title"] = "".join(s.title_buf).lstrip(": ").strip()
            s.title_buf = None
        if tag == "div" and s.exnum_buf is not None and "marker" in f["cls"]:
            m = re.search(r"Example\s*(\d+)", "".join(s.exnum_buf))
            s.cur["number"] = int(m.group(1)) if m else None
            s.exnum_buf = None
        if tag == "div" and "example" in f["cls"] and s.cur is not None and f["id"] == s.cur["id"]:
            s.cur, s.tabbed = None, []

    def handle_data(s, d):
        if s.capture:
            s.capture[1].append(d)
            return
        if s.in_secno:
            s.secbuf.append(d)
        if s.strong_buf is not None:
            s.strong_buf.append(d)
        if s.lab is not None:
            s.lab[1].append(d)
        if s.title_buf is not None:
            s.title_buf.append(d)
        if s.exnum_buf is not None:
            s.exnum_buf.append(d)


def extract(path):
    raw = open(path, encoding="utf-8", newline="").read()
    p = X()
    p.feed(raw)
    return p.examples, raw


def ext_of(b):
    k, t = b["kind"], b["text"].replace(" ", " ").lstrip()
    if k == "jwt-compact":
        return "jwt"
    if k == "sd-jwt-compact":
        return "sd-jwt"
    if k == "cose-text":
        return "hex"
    if k == "disclosure":
        return "txt"
    if t.startswith("eyJ"):
        return "sd-jwt"
    return "json" if t[:1] in '{["' else "txt"


def fixtures(examples):
    """[(filename, example, block)] in document order, names unique."""
    out = []
    for e in examples:
        names = {}
        for b in e["blocks"]:
            parts = []
            if b["vctab"]:
                parts.append(slug(b["vctab"][1]))
            if b["sdtab"]:
                parts.append(b["sdtab"])
            if b["label"] and b["kind"] != "disclosure":
                parts.append(slug(b["label"]))
            base = "ex%02d-%s" % (e["number"], "-".join(parts) if parts else "main")
            names[base] = names.get(base, 0) + 1
            b["_base"] = base
        seen = {}
        for b in e["blocks"]:
            base = b["_base"]
            if names[base] > 1:
                seen[base] = seen.get(base, 0) + 1
                stem = "%s-%d" % (base, seen[base])
            else:
                stem = base
            out.append((stem + "." + ext_of(b), e, b))
    return out


def regex_pres(raw):
    """Independent extractor for <pre>: regex over the raw bytes, tags stripped, <br> -> LF, unescaped."""
    res = []
    for m in re.finditer(r"<pre\b[^>]*>(.*?)</pre>", raw, re.S):
        t = re.sub(r"<br\s*/?>", "\n", m.group(1))
        t = re.sub(r"<[^>]+>", "", t)
        res.append(html.unescape(t))
    return res


def main(argv):
    if not argv:
        print(__doc__)
        return 2
    srcp = argv[0]
    write = argv[argv.index("--write") + 1] if "--write" in argv else None
    here = os.path.dirname(os.path.abspath(__file__))
    bad = []
    raw_bytes = open(srcp, "rb").read()
    got = hashlib.sha256(raw_bytes).hexdigest()
    if got != SRC_SHA256:
        bad.append("source sha256 %s != %s" % (got, SRC_SHA256))
    examples, raw = extract(srcp)
    fx = fixtures(examples)
    counts = {"examples": len(examples), "fixtures": len(fx)}
    for _, _, b in fx:
        counts[b["kind"]] = counts.get(b["kind"], 0) + 1
    for k, v in EXPECT.items():
        if counts.get(k) != v:
            bad.append("count %s = %s, expected %s" % (k, counts.get(k), v))
    pre_a = [b["text"] for _, _, b in fx if b["kind"] == "pre"]
    pre_b = regex_pres(raw)
    agree = sum(1 for a, b in zip(pre_a, pre_b) if a == b)
    if len(pre_a) != len(pre_b) or agree != len(pre_a):
        bad.append("HTMLParser and regex extractors disagree on %d of %d <pre>" % (len(pre_a) - agree, len(pre_a)))
    names = [f for f, _, _ in fx]
    if len(set(names)) != len(names):
        bad.append("duplicate fixture names")
    if write:
        os.makedirs(write, exist_ok=True)
        for f, _, b in fx:
            open(os.path.join(write, f), "wb").write(b["text"].encode("utf-8"))
        print("wrote %d fixtures to %s" % (len(fx), write))
    else:
        present = {f for f in os.listdir(here) if re.match(r"ex\d\d-", f)}
        for f, _, b in fx:
            p = os.path.join(here, f)
            if not os.path.exists(p):
                bad.append("missing " + f)
            elif open(p, "rb").read() != b["text"].encode("utf-8"):
                bad.append("bytes differ " + f)
        extra = sorted(present - set(names))
        for f in extra:
            bad.append("not produced by the source: " + f)
    print("EXAMINED: %d examples, %d fixtures (%s), %d <pre> compared across two extractors (%d agree)"
          % (counts["examples"], counts["fixtures"], ", ".join("%s %d" % (k, counts.get(k, 0)) for k in ("pre", "jwt-compact", "sd-jwt-compact", "cose-text", "disclosure")), len(pre_a), agree))
    print("FOUND: %d difference(s)" % len(bad))
    for b in bad:
        print("  " + b)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

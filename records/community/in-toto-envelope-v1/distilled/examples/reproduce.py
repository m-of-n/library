#!/usr/bin/env python3
"""reproduce.py -- re-extract every example fixture of the in-toto Envelope layer
specification (spec/v1/envelope.md) from the source and check this directory.

    python3 -I reproduce.py [PATH/TO/in-toto-envelope-v1.bin]           # check
    python3 -I reproduce.py [PATH/TO/in-toto-envelope-v1.bin] --write   # (re)write fixtures and index.yaml

The source is the Markdown file (sha256 c02c65880ccc117bbdecc6c916d5108541c1a864de67f8f9082efbaf15265d11
= content.sha256 in record.yaml), read as .cache/in-toto-envelope-v1.bin (searched upward from this
directory when no path is given). The bytes are never copied into the repository; this script is how a
reader gets back from the source to every *.verbatim.* file here. Line N of the .bin is line N of the
.txt rendering (distilled/render-source.py renumbers only ATX headings); the .txt is cross-checked
for the example lines when present.

What is an example. The source has no code block and no figure. Section 4.1 (lines 92-96) says
"Example media types for single DSSE-signed attestation predicates include:" and lists three
backticked media types. Those three are the examples: one fixture each, the bytes between the
backticks, no trailing newline. Every other backticked application/vnd.in-toto... span in the
source is the normative form of a media type (a template with <...> or a literal the text
requires), not an example, and is counted below so the exclusion is visible.

Derived instances (cases.derived.json) are a different thing: written by this library, never
presented as source; they are run through ../schema/check-envelope.derived.py here.

Checks (EXAMINED beside FOUND): (1) sha256 of the .bin; (2) two independent extractors (a
line-oriented regex and a whole-file regex) agree on the example spans; (3) every fixture exists
with identical bytes and nothing else here is named *.verbatim.*; (4) index.yaml records
source line, quote, sha256 and the expected results, and agrees; (5) each fixture matches
StorageMediaType and not PayloadTypeDsse, via the schema checker's validator; (6) every id cited by
a derived case exists in ../requirements.yaml; (7) the full accept/reject/mutation run. Exit 1 on
any difference.
"""
import hashlib, importlib.util, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
DIST = os.path.dirname(HERE)
SRC_SHA256 = "c02c65880ccc117bbdecc6c916d5108541c1a864de67f8f9082efbaf15265d11"
EXAMPLE_LINES = (94, 95, 96)
EXPECT = {"example spans": 3, "media-type spans in source": 7}
FAILS = []
EXAMINED = [0]


def check(cond, what):
    EXAMINED[0] += 1
    if not cond:
        FAILS.append(what)
        print("FAIL:", what)


def find_source(argv):
    for a in argv:
        if not a.startswith("--"):
            return a
    d = HERE
    while True:
        p = os.path.join(d, ".cache", "in-toto-envelope-v1.bin")
        if os.path.exists(p):
            return p
        if os.path.dirname(d) == d:
            sys.exit("reproduce.py: no .cache/in-toto-envelope-v1.bin found; pass its path")
        d = os.path.dirname(d)


def slug(label):
    return re.sub(r"[^a-z0-9]+", "-", label.lower()).strip("-")


def extract_a(lines):
    """line-oriented: list items inside section 4.1 (after the heading, before the footnote)."""
    out, on = [], False
    for n, l in enumerate(lines, 1):
        if re.match(r"^(#+ |4\.1\.  )Examples$", l):
            on = True
            continue
        if on and l.startswith("[^1]"):
            break
        m = re.match(r"^-   (.+?): `([^`]+)`$", l) if on else None
        if m:
            out.append((n, m.group(1), m.group(2)))
    return out


def extract_b(text):
    """whole-file: every '- LABEL: `application/vnd.in-toto.X+dsse`' list item, by regex over the bytes."""
    out = []
    for m in re.finditer(r"^-   ([^\n:`]+): `(application/vnd\.in-toto\.[^`<>\n]+\+dsse)`$", text, re.M):
        out.append((text.count("\n", 0, m.start()) + 1, m.group(1), m.group(2)))
    return out


def main():
    argv = sys.argv[1:]
    write = "--write" in argv
    src = find_source(argv)
    b = open(src, "rb").read()
    check(hashlib.sha256(b).hexdigest() == SRC_SHA256, f"sha256 of {src} is not the record's content.sha256")
    text = b.decode("utf-8")
    lines = text.split("\n")
    # (2) two extractors
    a = extract_a(lines)
    c = extract_b(text)
    check(a == c, f"extractors disagree: {a} vs {c}")
    check([x[0] for x in a] == list(EXAMPLE_LINES), f"example lines {[x[0] for x in a]} != {EXAMPLE_LINES}")
    check(len(a) == EXPECT["example spans"], f"expected {EXPECT['example spans']} example spans, found {len(a)}")
    spans = re.findall(r"`(application/vnd\.in-toto[^`]*)`", text)
    check(len(spans) == EXPECT["media-type spans in source"],
          f"expected {EXPECT['media-type spans in source']} backticked media-type spans in the source, found {len(spans)}")
    excluded = [s for s in spans if s not in [x[2] for x in a]]
    # the .txt rendering, when present, carries the same example lines
    txt = os.path.join(os.path.dirname(src), "in-toto-envelope-v1.txt")
    if os.path.exists(txt):
        tl = open(txt, encoding="utf-8").read().split("\n")
        for n, _, _ in a:
            check(tl[n - 1] == lines[n - 1], f"line {n} differs between .bin and .txt")
    # (3) fixtures
    files = {}
    index = []
    for n, label, value in a:
        name = f"media-type-{slug(label)}.verbatim.txt"
        files[name] = value.encode("utf-8")
        index.append({"fixture": name, "label": label, "source_lines": str(n), "line": lines[n - 1],
                      "media_type": value, "sha256": hashlib.sha256(value.encode()).hexdigest(),
                      "predicate": re.match(r"application/vnd\.in-toto\.(.+)\+dsse$", value).group(1)})
    if write:
        for name, data in files.items():
            open(os.path.join(HERE, name), "wb").write(data)
    for name, data in files.items():
        p = os.path.join(HERE, name)
        check(os.path.exists(p) and open(p, "rb").read() == data, f"{name}: missing or bytes differ from the source")
    on_disk = sorted(f for f in os.listdir(HERE) if ".verbatim." in f)
    check(on_disk == sorted(files), f"fixture set on disk {on_disk} != extracted {sorted(files)}")
    # (5) expected results via the schema checker's validator
    spec = importlib.util.spec_from_file_location("check_envelope", os.path.join(DIST, "schema", "check-envelope.derived.py"))
    ce = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ce)
    schema = json.load(open(os.path.join(DIST, "schema", "envelope.derived.schema.json")))
    for e in index:
        e["expected_valid_storage_media_type"] = not ce.validate(schema, "StorageMediaType", e["media_type"])[0]
        e["expected_valid_dsse_payload_type"] = not ce.validate(schema, "PayloadTypeDsse", e["media_type"])[0]
        check(e["expected_valid_storage_media_type"] is True, f"{e['fixture']}: must match StorageMediaType")
        check(e["expected_valid_dsse_payload_type"] is False, f"{e['fixture']}: a +dsse storage type must not be a DSSE payloadType")
    # (4) index.yaml
    y = ["# Fixture index. Written by reproduce.py --write; quote: and source_lines: are verified by bin/check-quotes.",
         "record: in-toto-envelope-v1", "reviewed_by: \"\"",
         "source: \".cache/in-toto-envelope-v1.bin (spec/v1/envelope.md), sha256 " + SRC_SHA256 + "\"",
         "context_quote:", "  source_lines: '92'", "  quote: " + json.dumps(lines[91]),
         "fixtures:"]
    for e in index:
        y += [f"  - fixture: {json.dumps(e['fixture'])}", f"    label: {json.dumps(e['label'])}",
              f"    source_lines: {json.dumps(e['source_lines'])}", f"    quote: {json.dumps(e['line'])}",
              f"    media_type: {json.dumps(e['media_type'])}", f"    predicate: {json.dumps(e['predicate'])}",
              f"    sha256: {json.dumps(e['sha256'])}",
              "    expected:",
              f"      valid_storage_media_type: {str(e['expected_valid_storage_media_type']).lower()}   # StorageMediaType in schema/envelope.derived.schema.json (R-0025)",
              f"      valid_dsse_payload_type: {str(e['expected_valid_dsse_payload_type']).lower()}   # a storage type is not a payloadType (+json)"]
    y += ["excluded_media_type_spans:   # backticked in the source but not examples: normative forms"]
    y += [f"  - {json.dumps(s)}" for s in excluded]
    y_text = "\n".join(y) + "\n"
    ip = os.path.join(HERE, "index.yaml")
    if write:
        open(ip, "w").write(y_text)
    check(os.path.exists(ip) and open(ip).read() == y_text, "index.yaml differs from the one rebuilt from the source")
    # (6) cited ids exist
    req = open(os.path.join(DIST, "requirements.yaml")).read()
    ids = set(re.findall(r"- id: '([^']+)'", req))
    cases = json.load(open(os.path.join(HERE, "cases.derived.json")))["cases"]
    cited = {i for k in cases for i in k["cites"]}
    for i in sorted(cited):
        check(i in ids, f"cases.derived.json cites {i}, not in requirements.yaml")
    print(f"examined {EXAMINED[0]} checks; fixtures {len(files)}, example spans {len(a)}, "
          f"other media-type spans excluded {len(excluded)}, distinct requirement ids cited by cases {len(cited)}")
    # (7) schema accept/reject/mutation run
    rc = ce.main()
    if rc:
        FAILS.append("check-envelope.derived.py failed")
    print("reproduce: " + ("FAILED" if FAILS else "ok"))
    return 1 if FAILS else 0


if __name__ == "__main__":
    sys.exit(main())

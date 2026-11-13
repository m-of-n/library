#!/usr/bin/env python3
"""Reproduce the in-toto-attestation-v1 example fixtures and run the schema
checker on them. Stdlib only. Run from anywhere:

    python3 -I reproduce.py [--rendering PATH] [--archive DIR] [--write-derived] [--verbose]

  --rendering  the rendering made by distilled/render-source.py
               (default: <repo>/.cache/in-toto-attestation-v1.txt; .cache/ is not in CI)
  --archive    the extracted GitHub archive of in-toto/attestation @ df02077:
               also compares every verbatim fixture, and the two .proto files, with
               the Markdown/proto bytes themselves (never executes anything in it)
  --write-derived  (re)write the *.derived.* fixtures from the recipes in
               vectors.derived.json, then fill their sha256

What it checks, and prints how many of each it EXAMINED (a clean result must be
distinguishable from not looking):
  1. the rendering's sha256 against vectors.derived.json
  2. every .verbatim. fixture == the rendering's lines (and, with --archive, the
     Markdown file's lines and the file's sha256) byte for byte
  3. every verbatim schema file in ../schema: bytes after the BEGIN VERBATIM line
     == its source, and the sha256 in its header
  4. every derived fixture == its recipe applied to its parent
  5. every inline example's quotation lies inside the rendering line it cites
  6. every expected result: schema verdicts, JSON-Lines classification,
     arithmetic checks (dirHash, h1:, gitBlob), filename and media-type patterns
  7. the schema checker's own cases (check-schemas.derived.py)
Exit 1 on any failure, 2 if an input is missing.
"""
import base64, hashlib, importlib.util, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
SCHEMA_DIR = os.path.join(os.path.dirname(HERE), "schema")
sha = lambda b: hashlib.sha256(b).hexdigest()
SENTINEL = "===== BEGIN VERBATIM =====\n"


def repo_root():
    d = HERE
    while d != os.path.dirname(d):
        if os.path.exists(os.path.join(d, "bin", "validate")): return d
        d = os.path.dirname(d)
    return None


def load_cs():
    spec = importlib.util.spec_from_file_location("cs", os.path.join(SCHEMA_DIR, "check-schemas.derived.py"))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m


def strip_jsonc(t):
    """Remove // and /* */ comments outside strings."""
    out, i, n, instr = [], 0, len(t), False
    while i < n:
        c = t[i]
        if instr:
            out.append(c)
            if c == "\\": out.append(t[i + 1]); i += 1
            elif c == '"': instr = False
        elif c == '"': instr = True; out.append(c)
        elif t.startswith("//", i):
            while i < n and t[i] != "\n": i += 1
            continue
        elif t.startswith("/*", i):
            i = t.index("*/", i) + 2; continue
        else: out.append(c)
        i += 1
    return "".join(out)


def parse_jsonc(t): return json.loads(strip_jsonc(t))


def stream(text):
    """Concatenated JSON values (jq output); returns (values, bad)."""
    dec, i, vals = json.JSONDecoder(), 0, []
    while True:
        while i < len(text) and text[i].isspace(): i += 1
        if i >= len(text): return vals, 0
        try: v, i = dec.raw_decode(text, i)
        except ValueError: return vals, 1
        vals.append(v)


PATTERNS = {   # name -> regex; each from the line(s) the manifest cites
    "STORAGE_DSSE": r"^application/vnd\.in-toto\.[^\s/+]+\+dsse$",          # envelope.md 8.4
    "BUNDLE_MT": r"^application/vnd\.in-toto\.bundle$",                       # bundle.md 9.3
    "ENVELOPE_FILE": r"^[^/\s]+\.json$",                                      # envelope.md 8.3
    "ENVELOPE_FILE_KEYID": r"^[^/\s]+\.[^./\s]{8}\.json$",                     # envelope.md 8.3, <keyid[0:8]>
    "BUNDLE_FILE": r"^.+\.intoto\.jsonl$",                                    # bundle.md 9.2
}


def dsmatch(a, b):
    """digest_set.md 5.2.2: matching if ANY acceptable field matches (here: any shared algorithm)."""
    return any(k in b and b[k] == v for k, v in a.items())


def derive(recipe, parent_text, cs):
    t = parent_text
    for old, new, *cnt in recipe.get("replace", []):
        want = cnt[0] if cnt else 1
        assert t.count(old) == want, (old, t.count(old), want)
        t = t.replace(old, new)
    w = recipe.get("wrap")
    if w:
        obj = parse_jsonc(t) if recipe["from"].startswith("EX") else json.loads(t)
        if w == "statement":
            obj = {"_type": "https://in-toto.io/Statement/v1", "subject": [obj],
                   "predicateType": "https://example.com/predicate/v1"}
        elif w == "envelope":
            obj = {"payloadType": "application/vnd.in-toto+json",
                   "payload": base64.b64encode(json.dumps(obj, separators=(",", ":")).encode()).decode(),
                   "signatures": [{"keyid": "k1", "sig": "AAAA"}]}
        t = json.dumps(obj, indent=2) + "\n"
    return t


def run_checks(name, text, checks, cs, errs, counters, manifest):
    for ck in checks:
        counters["checks"] += 1
        t = ck["t"]
        try:
            if t == "jsonc":
                try: parse_jsonc(text); got = "parse"
                except Exception: got = "fail"
            elif t == "schema":
                inst = parse_jsonc(text) if name.endswith(("jsonc", "json")) else None
                if "path" in ck:
                    for p in ck["path"]: inst = inst[p]
                got = "accept" if cs.verdict(ck["schema"], inst, ck.get("def")) else "reject"
            elif t == "deep":
                got = "accept" if cs.deep_envelope(json.loads(text)) else "reject"
            elif t == "bundle":
                got = list(cs.check_bundle(text))
            elif t == "stream":
                first, _, rest = text.partition("\n")
                vals, bad = stream(rest)
                rec = sum(1 for v in vals if not cs.validate(cs.load("bundle-line"), v))
                got = [rec, len(vals) - rec, bad]
            elif t == "calc":
                got = calc(ck["name"], text, manifest)
            else:
                raise ValueError(t)
        except Exception as e:
            got = f"error: {e}"
        if got != ck["expect"]:
            errs.append(f"{name}: check {ck} -> {got}")


def calc(nm, text, manifest):
    fx = {f["id"]: f for f in manifest["fixtures"]}
    def body(i): return open(os.path.join(HERE, fx[i]["file"])).read()
    if nm == "dirhash-listing":      # EX-09 listing, sha256 == EX-10's printed result
        lines = body("EX-09").split("\n")
        listing = "".join(l + "\n" for l in lines if re.match(r"^[0-9a-f]{64}  ", l))
        return sha(listing.encode()) == body("EX-10").split("\n")[1] and listing.count("\n") == 3
    if nm == "h1-base64":            # EX-11: hex -> base64 gives the h1: line, which EX-07 also prints
        hexs = re.search(r"echo '([0-9a-f]{64})'", body("EX-11")).group(1)
        h1 = "h1:" + base64.b64encode(bytes.fromhex(hexs)).decode()
        return h1 == body("EX-11").split("\n")[1] and h1 in body("EX-07") and hexs == body("EX-10").split("\n")[1]
    if nm == "git-blob":             # EX-12: blob 5 NUL Hello
        h = hashlib.sha1(b"blob 5\x00Hello").hexdigest()
        return body("EX-12").split("\n")[1] == h and body("EX-12").split("\n")[3] == h
    if nm == "tekton-digest-vs-content":   # observation: digest is NOT sha256(decoded content)
        o = parse_jsonc(body("EX-05"))
        return "match" if sha(base64.b64decode(o["content"])) == o["digest"]["sha256"] else "mismatch"
    if nm == "tekton-content-json":
        o = parse_jsonc(body("EX-05"))
        return sorted(json.loads(base64.b64decode(o["content"])))
    raise ValueError(nm)


def run_inline(manifest, rl, cs, errs, counters):
    std = set(cs.load("digest-set")["properties"])
    for iv in manifest["inline"]:
        counters["inline"] += 1
        ln = iv["rendering_line"]
        if iv["quote"] not in rl[ln - 1]:
            errs.append(f"{iv['id']}: quote not in rendering line {ln}")
        for ck in iv["checks"]:
            counters["checks"] += 1
            t, inst = ck["t"], ck.get("inst")
            if t == "schema": got = "accept" if cs.verdict(ck["schema"], inst, ck.get("def")) else "reject"
            elif t == "dsmatch": got = dsmatch(inst[0], inst[1])
            elif t == "pattern": got = "accept" if re.search(PATTERNS[ck["pattern"]], inst) else "reject"
            elif t == "stdname": got = "standard" if inst in std else "not-standard"
            else: raise ValueError(t)
            if got != ck["expect"]:
                errs.append(f"{iv['id']}: check {ck} -> {got}")


def main():
    a = sys.argv[1:]
    root = repo_root()
    rpath = a[a.index("--rendering") + 1] if "--rendering" in a else (os.path.join(root, ".cache", "in-toto-attestation-v1.txt") if root else "")
    arch = a[a.index("--archive") + 1] if "--archive" in a else None
    if not os.path.exists(rpath):
        print(f"rendering not found: {rpath} (make it with distilled/render-source.py)"); return 2
    manifest = json.load(open(os.path.join(HERE, "vectors.derived.json")))
    cs = load_cs()
    rb = open(rpath, "rb").read()
    rl = rb.decode().split("\n")
    errs, c = [], dict(verbatim=0, schema_verbatim=0, derived=0, inline=0, checks=0, archive=0)
    if sha(rb) != manifest["rendering_sha256"]:
        errs.append(f"rendering sha256 {sha(rb)} != manifest {manifest['rendering_sha256']}")
    # 2 verbatim fixtures
    for f in manifest["fixtures"]:
        c["verbatim"] += 1
        data = open(os.path.join(HERE, f["file"]), "rb").read()
        lo, hi = f["rendering_lines"]
        want = "".join(l + "\n" for l in rl[lo - 1:hi]).encode()
        if data != want: errs.append(f"{f['file']}: bytes differ from rendering lines {lo}-{hi}")
        if sha(data) != f["sha256"]: errs.append(f"{f['file']}: sha256 != manifest")
        if arch:
            c["archive"] += 1
            mb = open(os.path.join(arch, f["md"]), "rb").read()
            if sha(mb) != f["md_file_sha256"]: errs.append(f"{f['md']}: archive file sha256 differs")
            ml = mb.decode().split("\n")
            mlo, mhi = f["md_lines"]
            if "".join(l + "\n" for l in ml[mlo - 1:mhi]).encode() != data:
                errs.append(f"{f['file']}: bytes differ from {f['md']} lines {mlo}-{mhi}")
    # 3 schema verbatim files
    sv = json.load(open(os.path.join(SCHEMA_DIR, "verbatim-sources.derived.json")))
    if sv["rendering_sha256"] != manifest["rendering_sha256"]: errs.append("schema sources: rendering sha256 differs")
    for s in sv["sources"]:
        c["schema_verbatim"] += 1
        raw = open(os.path.join(SCHEMA_DIR, s["file"]), "rb").read().decode()
        i = raw.index(SENTINEL) + len(SENTINEL)
        body = raw[i:]
        head = raw[:i]
        if sha(body.encode()) != s["body_sha256"] or s["body_sha256"] not in head:
            errs.append(f"{s['file']}: body sha256 differs from manifest/header")
        if s["kind"] == "rendering-block":
            lo, hi = s["rendering_lines"]
            if body != "".join(l + "\n" for l in rl[lo - 1:hi]): errs.append(f"{s['file']}: differs from rendering lines {lo}-{hi}")
        if arch:
            c["archive"] += 1
            if s["kind"] == "archive-file":
                if open(os.path.join(arch, s["archive_path"]), "rb").read().decode() != body: errs.append(f"{s['file']}: differs from archive file")
            else:
                ml = open(os.path.join(arch, s["md"]), "rb").read().decode().split("\n")
                mlo, mhi = s["md_lines"]
                if "".join(l + "\n" for l in ml[mlo - 1:mhi]) != body: errs.append(f"{s['file']}: differs from {s['md']} {mlo}-{mhi}")
    # 4 derived fixtures
    if "--write-derived" in a:
        for d in manifest["derived"]:
            par = d["from"]
            pf = next((x for x in manifest["fixtures"] + manifest["derived"] if x["id"] == par))
            t = derive(d, open(os.path.join(HERE, pf["file"])).read(), cs)
            open(os.path.join(HERE, d["file"]), "w").write(t)
            d["sha256"] = sha(t.encode())
        json.dump(manifest, open(os.path.join(HERE, "vectors.derived.json"), "w"), indent=1)
        open(os.path.join(HERE, "vectors.derived.json"), "a").write("\n")
    for d in manifest["derived"]:
        c["derived"] += 1
        pf = next(x for x in manifest["fixtures"] + manifest["derived"] if x["id"] == d["from"])
        try: t = derive(d, open(os.path.join(HERE, pf["file"])).read(), cs)
        except Exception as e:
            errs.append(f"{d['file']}: cannot re-derive from {d['from']}: {e}"); continue
        got = open(os.path.join(HERE, d["file"])).read()
        if t != got or sha(got.encode()) != d["sha256"]: errs.append(f"{d['file']}: not the recipe applied to {d['from']}")
    # 5/6 checks
    for f in manifest["fixtures"] + manifest["derived"]:
        run_checks(f["file"], open(os.path.join(HERE, f["file"])).read(), f["checks"], cs, errs, c, manifest)
    run_inline(manifest, rl, cs, errs, c)
    # 7 schema checker
    n, bad = cs.run_cases()
    for b in bad: errs.append(f"check-schemas: {b}")
    print(f"rendering sha256 {sha(rb)}  ({len(rl) - (rl[-1] == '')} lines)")   # split("\n") leaves '' after the final newline
    print(f"examined: verbatim fixtures {c['verbatim']}, verbatim schema files {c['schema_verbatim']}, "
          f"derived fixtures {c['derived']}, inline examples {c['inline']}, expected-result checks {c['checks']}, "
          f"schema-checker cases {n}" + (f", archive comparisons {c['archive']}" if arch else " (no --archive: Markdown bytes not compared)"))
    for e in errs: print("FAIL", e)
    print("OK" if not errs else f"FAILED ({len(errs)})")
    return 1 if errs else 0


if __name__ == "__main__":
    sys.exit(main())

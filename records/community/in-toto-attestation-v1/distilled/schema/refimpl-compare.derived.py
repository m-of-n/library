#!/usr/bin/env python3
"""DERIVED - not verbatim. A hand port of the validate rules of the reference
bindings, to compare their verdicts with the derived schemas' verdicts:

  Go      go/v1/statement.go, go/v1/resource_descriptor.go
  Python  python/in_toto_attestation/v1/statement.py, resource_descriptor.py
          (in-toto/attestation @ df02077bf97218a8860a5c534eff1f1381f56984)

    python3 -I refimpl-compare.derived.py            # summary + every disagreement class
    python3 -I refimpl-compare.derived.py --all      # every disagreeing case

NOT EXECUTED: the archive's code was read, never run. This file is the library's
reading of it. Two behaviours are NOT in the archive and are assumed from the
protobuf libraries' documented defaults: protojson.Unmarshal (Go) and
json_format.Parse (Python) reject an unknown JSON field unless told to ignore
it, which neither binding's tests do. Re-verify those two by running the
bindings before relying on them. A third modelling choice is NOT verified
either (pass 2): bytes content is decoded strictly here for both bindings, as
Go's protojson does; Python's json_format decodes bytes with
base64.urlsafe_b64decode without validation, which discards characters outside
the alphabet, so Python's real parse may accept content this port rejects.
The Rust binding (rust/src/lib.rs) is not ported.
"""
import base64, importlib.util, os, sys, json, re

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("cs", os.path.join(HERE, "check-schemas.derived.py"))
cs = importlib.util.module_from_spec(spec); spec.loader.exec_module(cs)

V1 = "https://in-toto.io/Statement/v1"
V01 = "https://in-toto.io/Statement/v0.1"
RD_FIELDS = {"name", "uri", "digest", "content", "downloadLocation", "download_location",
             "mediaType", "media_type", "annotations"}
ST_FIELDS = {"_type", "type", "subject", "predicateType", "predicate_type", "predicate"}
# go/v1/resource_descriptor.go HexLength(), in bytes
GO_LEN = {"md5": 16, "sha1": 20, "gitBlob": 20, "gitCommit": 20, "gitTag": 20, "gitTree": 20,
          "sha224": 28, "sha512_224": 28, "sha3_224": 28, "sha256": 32, "sha512_256": 32,
          "sha3_256": 32, "dirHash": 32, "sha384": 48, "sha3_384": 48, "sha512": 64, "sha3_512": 64}


class Bad(Exception): pass


def _s(v):
    if v is None or isinstance(v, str): return v
    raise Bad("string expected")


def _b64(v):
    _s(v)
    if v is None: return b""
    t = v.rstrip("=")
    try:
        return base64.b64decode(t + "=" * (-len(t) % 4), altchars=b"-_" if re.search(r"[-_]", t) else None, validate=True)
    except Exception:
        raise Bad("bad base64")


def unmarshal_rd(o, strict_unknown=True):
    if not isinstance(o, dict): raise Bad("object expected")
    if strict_unknown and set(o) - RD_FIELDS: raise Bad("unknown field")
    d = o.get("digest")
    if d is not None:
        if not isinstance(d, dict): raise Bad("digest map")
        for v in d.values(): _s(v) if v is not None else (_ for _ in ()).throw(Bad("null map value"))
    for k in ("name", "uri", "downloadLocation", "download_location", "mediaType", "media_type"): _s(o.get(k))
    _b64(o.get("content"))
    a = o.get("annotations")
    if a is not None and not isinstance(a, dict): raise Bad("annotations struct")
    return dict(name=o.get("name") or "", uri=o.get("uri") or "", digest=d or {})


def unmarshal_st(o, strict_unknown=True):
    if not isinstance(o, dict): raise Bad("object expected")
    if strict_unknown and set(o) - ST_FIELDS: raise Bad("unknown field")
    t = _s(o.get("_type", o.get("type"))) or ""
    sub = o.get("subject")
    if sub is not None and not isinstance(sub, list): raise Bad("subject repeated")
    rds = [unmarshal_rd(x, strict_unknown) for x in (sub or [])]
    pt = _s(o.get("predicateType", o.get("predicate_type"))) or ""
    p = o.get("predicate")
    if p is not None and not isinstance(p, dict): raise Bad("predicate struct")
    return dict(type=t, subject=rds, ptype=pt, predicate=p)   # None = unset, {} = empty Struct


def go_rd(rd):
    if rd["name"] == "" and rd["uri"] == "" and len(rd["digest"]) == 0: return False
    for alg, dg in rd["digest"].items():
        n = GO_LEN.get(alg, 0)
        if n > 0:
            # hex.DecodeString: either case, even length, and nothing else. Pass 2: the first
            # version used bytes.fromhex alone, which also skips ASCII whitespace, so a value
            # with a trailing newline counted as one Go accepts (it does not).
            if not isinstance(dg, str) or not re.fullmatch(r"[0-9A-Fa-f]*", dg): return False
            try: b = bytes.fromhex(dg)
            except ValueError: return False
            if len(b) != n: return False
    return True


def go_statement(o, strict=True):
    try: s = unmarshal_st(o, strict)
    except Bad: return False
    if s["type"] not in (V1, V01): return False
    if not s["subject"]: return False
    for rd in s["subject"]:
        if not go_rd(rd): return False
        if len(rd["digest"]) == 0: return False
    if s["ptype"] == "": return False
    if s["predicate"] is None: return False          # GetPredicate() == nil
    return True


def py_rd(rd):
    return not (rd["name"] == "" and rd["uri"] == "" and len(rd["digest"]) == 0)


def py_statement(o, strict=True):
    try: s = unmarshal_st(o, strict)
    except Bad: return False
    if s["type"] != V1: return False
    if not s["subject"]: return False
    for rd in s["subject"]:
        if not py_rd(rd): return False
        if len(rd["digest"]) == 0: return False
    if s["ptype"] == "": return False
    if not s["predicate"]: return False              # len(predicate) == 0 (unset or {})
    return True


def go_rd_json(o, strict=True):
    try: return go_rd(unmarshal_rd(o, strict))
    except Bad: return False


def py_rd_json(o, strict=True):
    try: return py_rd(unmarshal_rd(o, strict))
    except Bad: return False


def compare(show_all=False):
    rows = []
    for sname, defn, inst, expect, cid in cs.all_cases():
        if sname == "resource-descriptor" and defn is None:
            g, p = go_rd_json(inst), py_rd_json(inst)
            g2, p2 = go_rd_json(inst, False), py_rd_json(inst, False)
        elif sname == "statement":
            # Both bindings REQUIRE a predicate; to isolate the other rules a statement
            # that merely lacks one gets {"k": 1}. st-00 and st-01 are the cases about it.
            if isinstance(inst, dict) and "predicate" not in inst and cid.split("^")[0] != "st-00":
                inst = dict(inst, predicate={"k": 1})
            if cid.split("^")[0] == "st-01":
                inst = inst
            g, p = go_statement(inst), py_statement(inst)
            g2, p2 = go_statement(inst, False), py_statement(inst, False)
        elif sname == "digest-set" and not cid.startswith("ds-sweep") or cid.startswith("ds-sweep"):
            if sname != "digest-set": continue
            wrapped = {"name": "n", "digest": inst} if isinstance(inst, dict) else {"name": "n", "digest": inst}
            g, p = go_rd_json(wrapped), py_rd_json(wrapped)
            g2, p2 = go_rd_json(wrapped, False), py_rd_json(wrapped, False)
        else:
            continue
        want = expect == "accept"
        rows.append((cid, sname, inst, want, g, p, g2, p2))
    return rows


def classify(rows):
    cls = {}
    for cid, sname, inst, want, g, p, g2, p2 in rows:
        for impl, v in (("go", g2), ("python", p2)):   # compare with unknown-field leniency on (the spec requires it)
            if v != want:
                k = (impl, "schema accepts, code rejects" if want else "schema rejects, code accepts", sname)
                cls.setdefault(k, []).append((cid, inst))
    return cls


def main():
    rows = compare()
    n = len(rows)
    print(f"cases compared: {n} (schema cases that have a Go/Python analogue: statement, "
          f"resource-descriptor, digest-set via a descriptor with name+digest)")
    for impl, i in (("go", 6), ("python", 7)):
        agree = sum(1 for r in rows if r[i] == r[3])
        print(f"  {impl}: agrees with the schema on {agree}/{n} (unknown-field leniency on)")
    for impl, i in (("go", 4), ("python", 5)):
        agree = sum(1 for r in rows if r[i] == r[3])
        print(f"  {impl}: agrees with the schema on {agree}/{n} (unknown fields rejected, as protobuf's default Unmarshal/Parse does)")
    # unknown-field effect alone
    unk = [r for r in rows if r[3] and (r[4] is False and r[6] is True)]
    print(f"  accepted instances that only the strict-unknown-field parse rejects (Go): {len(unk)}")
    cls = classify(rows)
    print(f"disagreement classes (unknown fields tolerated): {len(cls)}")
    for k, v in sorted(cls.items()):
        ex = v[0]
        print(f"- {k[0]:6} {k[2]:20} {k[1]:30} n={len(v):4}  e.g. {ex[0]} {json.dumps(ex[1])[:80]}")
        if "--all" in sys.argv:
            for c in v: print("      ", c[0], json.dumps(c[1])[:100])
    return 0


if __name__ == "__main__":
    sys.exit(main())

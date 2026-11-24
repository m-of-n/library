#!/usr/bin/env python3
"""DERIVED - not verbatim. Stdlib-only checker for the derived JSON Schemas of
in-toto-attestation-v1 (this directory), with the instances each schema MUST
accept and MUST reject, and a mutation test showing that the reject cases bind.

    python3 -I check-schemas.derived.py               # run every case
    python3 -I check-schemas.derived.py --mutate      # + mutation test
    python3 -I check-schemas.derived.py --basis REQ   # + check cited R-ids against requirements.yaml
    python3 -I check-schemas.derived.py --list        # print every case

Exit 1 on any failure. Always prints how many cases were EXAMINED.

The validator below is a deliberately small JSON Schema (2020-12) subset. It
raises on any keyword it does not implement, so a constraint cannot be
silently ignored: a schema that parses is not a schema that binds.
"""
import base64, copy, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ANNOTATION = {"$schema", "$id", "title", "description", "$comment", "$defs",
              "examples", "default"}
KNOWN = ANNOTATION | {"type", "const", "enum", "required", "properties",
                      "patternProperties", "additionalProperties", "minProperties",
                      "items", "minItems", "minLength", "pattern", "allOf",
                      "anyOf", "oneOf", "not", "$ref"}


def _type_ok(t, v):
    if t == "object": return isinstance(v, dict)
    if t == "array": return isinstance(v, list)
    if t == "string": return isinstance(v, str)
    if t == "boolean": return isinstance(v, bool)
    if t == "null": return v is None
    if t == "number": return isinstance(v, (int, float)) and not isinstance(v, bool)
    if t == "integer": return isinstance(v, int) and not isinstance(v, bool)
    raise ValueError("type " + t)


def validate(schema, inst, root=None):
    """Return a list of error strings; empty means valid."""
    root = root if root is not None else schema
    errs = []
    if schema is True: return errs
    if schema is False: return ["false schema"]
    for k in schema:
        if k not in KNOWN:
            raise ValueError(f"unsupported keyword {k!r} (would be silently ignored)")
    if "$ref" in schema:
        ref = schema["$ref"]
        if not ref.startswith("#/$defs/"):
            raise ValueError("unsupported $ref " + ref)
        errs += validate(root["$defs"][ref[8:]], inst, root)
    if "type" in schema:
        ts = schema["type"] if isinstance(schema["type"], list) else [schema["type"]]
        if not any(_type_ok(t, inst) for t in ts):
            errs.append(f"type: want {ts}")
    if "const" in schema and not (inst == schema["const"] and type(inst) is type(schema["const"])):
        errs.append(f"const {schema['const']!r}")
    if "enum" in schema and inst not in schema["enum"]:
        errs.append("enum")
    if isinstance(inst, dict):
        for r in schema.get("required", []):
            if r not in inst: errs.append(f"required {r}")
        if "minProperties" in schema and len(inst) < schema["minProperties"]:
            errs.append("minProperties")
        props = schema.get("properties", {})
        for k, sub in props.items():
            if k in inst: errs += [f"{k}: {e}" for e in validate(sub, inst[k], root)]
        pp = schema.get("patternProperties", {})
        for k, v in inst.items():
            matched = k in props
            for pat, sub in pp.items():
                if re.search(pat, k):
                    matched = True
                    errs += [f"{k}: {e}" for e in validate(sub, v, root)]
            if not matched and "additionalProperties" in schema:
                errs += [f"{k}: {e}" for e in validate(schema["additionalProperties"], v, root)]
    if isinstance(inst, list):
        if "minItems" in schema and len(inst) < schema["minItems"]: errs.append("minItems")
        if "items" in schema:
            for i, v in enumerate(inst):
                errs += [f"[{i}]: {e}" for e in validate(schema["items"], v, root)]
    if isinstance(inst, str):
        if "minLength" in schema and len(inst) < schema["minLength"]: errs.append("minLength")
        if "pattern" in schema and not re.search(re.sub(r"(?<!\\)\$", r"\\Z", schema["pattern"]), inst):
            errs.append(f"pattern {schema['pattern'][:40]}")
    for s in schema.get("allOf", []): errs += validate(s, inst, root)
    if "anyOf" in schema and not any(not validate(s, inst, root) for s in schema["anyOf"]):
        errs.append("anyOf")
    if "oneOf" in schema and sum(1 for s in schema["oneOf"] if not validate(s, inst, root)) != 1:
        errs.append("oneOf")
    if "not" in schema and not validate(schema["not"], inst, root):
        errs.append("not")
    return errs


def load(name):
    with open(os.path.join(HERE, f"{name}.derived.schema.json")) as fh:
        return json.load(fh)


def verdict(schema_name, inst, defn=None):
    sch = load(schema_name)
    if defn:
        sch = {"$ref": f"#/$defs/{defn}", "$defs": sch["$defs"]}
    return not validate(sch, inst)


# ---- basis ---------------------------------------------------------------
# Pass 2 (verify): the first version cited R-0029 ("immutable reference") for
# every DigestSet case, and split parents (R-0009, R-0037, R-0040, R-0052) that
# requirements.yaml tests only through their children. Each case now cites the
# statement its verdict rests on; --basis checks the id exists and holds the words.
GIT_KEYS = ("gitCommit", "gitTree", "gitBlob", "gitTag")
STD_KEYS = ("sha256", "sha224", "sha384", "sha512", "sha512_224", "sha512_256", "sha3_224",
            "sha3_256", "sha3_384", "sha3_512", "shake128", "shake256", "blake2b", "blake2s",
            "ripemd160", "sm3", "gost", "sha1", "md5")


def ds_basis(v):
    if v == {}: return [("R-0156", "one or more")]
    if not isinstance(v, dict): return [("R-0157", "_JSON object_ mapping algorithm name to a string")]
    out = []
    for k, x in v.items():
        if not isinstance(x, str): b = ("R-0157", "to a string encoding")
        elif k == "dirHash": b = ("R-0160", "lowercase hexadecimal")
        elif k in GIT_KEYS: b = ("R-0161", "SHA-1 (40 character) or SHA-256 (64 character)")
        elif k in STD_KEYS: b = ("R-0158", "lowercase hex encoding")
        else: b = ("R-0207", "open set")
        if b not in out: out.append(b)
    return out


def uri_basis(why, ok, lc, rfc):
    if ok: return [rfc, lc]
    return [lc] if re.search(r"lowercase|uppercase|case", why) else [rfc]


RU_LC, RU_RFC = ("R-0108", "scheme and authority MUST be in lowercase"), ("R-0164", "as specified in [RFC 3986]")
TU_LC, TU_RFC = ("R-0112", "scheme and authority MUST be in lowercase"), ("R-0165", "as specified in [RFC 3986]")


# ---- cases ---------------------------------------------------------------
H64 = "7f4714fd" + "0" * 56
H40 = "d61b27b8" + "0" * 32
H32 = "a1b2c3d4" + "0" * 24
H128 = "ab" * 64
CASES = []   # dicts: id, schema, def, inst, expect, why, basis [(R-id, needle)] , lift


def case(cid, schema, inst, expect, why, basis=(), defn=None, lift=None, silent=False):
    CASES.append(dict(id=cid, schema=schema, **({"def": defn} if defn else {}),
                      inst=inst, expect=expect, why=why, basis=list(basis),
                      lift=lift, silent=silent))


# --- field types: ResourceURI / TypeURI / Timestamp
RU = [("pkg:deb/debian/stunnel@5.50-3?arch=amd64", 1, "field_types.md example"),
      ("git+https://github.com/actions/runner", 1, "SPDX download location form, resource_descriptor example"),
      ("https://example.com", 1, "plain https"), ("file:///etc/hosts", 1, "empty authority"),
      ("urn:isbn:0451450523", 1, "no authority"), ("https://example.com/Path?Q=1#Frag", 1, "path/query/fragment are case sensitive and may be uppercase"),
      ("https://example.com:8080/x", 1, "port"),
      ("HTTPS://example.com/x", 0, "scheme not lowercase"),
      ("https://Example.com/x", 0, "authority not lowercase"),
      ("https://EXAMPLE.COM", 0, "authority not lowercase, no path"),
      ("https://example.com:80/x".replace("example", "Example"), 0, "authority uppercase before port"),
      ("https://user:Pass@example.com/", 0, "the source's gloss says the whole authority is lowercase (RFC 3986 itself keeps userinfo case sensitive)"),
      ("https://Example.com?q", 0, "authority uppercase, query delimiter"),
      ("https://Example.com#f", 0, "authority uppercase, fragment delimiter"),
      ("example.com/x", 0, "no scheme: not a URI"), ("//example.com/x", 0, "network-path reference, no scheme"),
      ("1http://x", 0, "scheme must start with a letter"), ("", 0, "empty"),
      ("https://exa mple.com", 0, "space in authority"), ("https://example.com/a b", 0, "space in path"),
      (" https://example.com", 0, "leading space"), ("https://example.com ", 0, "trailing space"),
      ("https://example.com\n", 0, "trailing newline"), ("x:y", 1, "minimal scheme:path"),
      ("a+b-c.d:e", 1, "scheme with + - ."), ("-a:b", 0, "scheme must start with a letter, not '-'"),
      (5, 0, "not a string"), (None, 0, "null"), (["https://x.io"], 0, "array")]
for i, (v, ok, why) in enumerate(RU):
    case(f"ft-resourceuri-{i:02d}", "field-types", v, "accept" if ok else "reject", why,
         uri_basis(why, ok, RU_LC, RU_RFC), defn="ResourceURI", lift="uri")
TU = [("https://in-toto.io/Statement/v1", 1, "the Statement type itself"),
      ("https://fooly.app/Builder/v1", 1, "bundle.md 9.4.1 predicateType"),
      ("https://spdx.dev/Document", 1, "bundle.md 9.4.3 predicateType"),
      ("https://slsa.dev/provenance/v1", 1, "versioning.md example"),
      ("https://In-toto.io/Statement/v1", 0, "authority not lowercase"),
      ("HTTPS://in-toto.io/Statement/v1", 0, "scheme not lowercase"),
      ("in-toto.io/Statement/v1", 0, "no scheme"), ("thePredicate", 0, "a bare word is not a URI (the Go/Python tests use one)"),
      (" https://in-toto.io/Statement/v1", 0, "leading space"), ("https://in-toto.io/Statement/v1 ", 0, "trailing space"),
      ("-x:y", 0, "scheme starts with '-'"), ("https://X.io", 0, "authority uppercase, no path"),
      ("urn:example:predicate:v1", 1, "no-authority URI"), ("pkg:generic/x@1", 1, "purl-style"),
      ("", 0, "empty"), (1, 0, "not a string")]
for i, (v, ok, why) in enumerate(TU):
    case(f"ft-typeuri-{i:02d}", "field-types", v, "accept" if ok else "reject", why,
         uri_basis(why, ok, TU_LC, TU_RFC), defn="TypeURI", lift="predicateType")
TS = [("1985-04-12T23:20:50.52Z", 1, "field_types.md example"), ("2020-01-01T00:00:00Z", 1, "no fraction"),
      ("2016-12-31T23:59:60Z", 1, "leap second is RFC 3339 syntax"),
      ("1985-04-12T23:20:50.52+00:00", 0, "UTC offset form, not Z"),
      ("1985-04-12T23:20:50.52-07:00", 0, "non-UTC zone"),
      ("1985-04-12T23:20:50.52", 0, "no zone"), ("1985-13-12T23:20:50Z", 0, "month 13"),
      ("1985-04-32T23:20:50Z", 0, "day 32"), ("1985-04-12T24:20:50Z", 0, "hour 24"),
      ("1985-04-12T23:60:50Z", 0, "minute 60"), ("1985-04-12T23:20:61Z", 0, "second 61"),
      ("85-04-12T23:20:50Z", 0, "two-digit year"), ("1985-04-12T23:20:50.Z", 0, "empty fraction"),
      ("1985-04-12T23:20:50z", 0, "lowercase z: the source writes the zone as literal \"Z\" (RFC 3339 also admits z; this reject is the library's reading)"),
      ("1985-04-12", 0, "date only"), ("1985-04-12T23:20:50.52Z\n", 0, "trailing newline"),
      (" 1985-04-12T23:20:50Z", 0, "leading space"), ("1985-04-12T23:20:50Zx", 0, "trailing junk"),
      ("1985-04-12T23:20:50.5xZ", 0, "non-digit fraction"), ("1985-04-12t23:20:50Z", 1, "RFC 3339 allows lowercase t"),
      ("1985-00-12T23:20:50Z", 0, "month 00"), ("1985-04-00T23:20:50Z", 0, "day 00"), (1677872236, 0, "epoch number, not a string"),
      ("1677872236", 0, "epoch as string (Tekton example content uses this inside content, not as a Timestamp)")]
for i, (v, ok, why) in enumerate(TS):
    case(f"ft-timestamp-{i:02d}", "field-types", v, "accept" if ok else "reject", why,
         [("R-0042", "RFC 3339")] + ([("R-0208", "uppercase Z")] if re.search(r"\bz\b|zone|UTC|offset", why, re.I) else []),
         defn="Timestamp")

# --- DigestSet (spec text: lowercase hex, git 40|64, dirHash 64)
DS = [({"sha256": H64}, 1, "one sha256"),
      ({"sha256": "abcd", "sha512": "1234"}, 1, "digest_set.md 5.3 example (short but lowercase hex)"),
      ({"sha256": "abcd"}, 1, "digest_set.md 5.3 example"),
      ({"somecoolhash": "abcd"}, 1, "digest_set.md 5.3: a non-predefined algorithm"),
      ({"arn": "arn:aws:ec2:region:123:image/ami-123abcd"}, 1, "digest_set.md 5.3: non-cryptographic identifier"),
      ({"gitBlob": "5ab2f8a4323abafb10abb68657d9d39f1a775057"}, 1, "gitBlob of Hello (40 hex)"),
      ({"gitCommit": H64}, 1, "gitCommit may be SHA-256 (64 hex)"),
      ({"gitTree": H40, "gitTag": H40}, 1, "two git entries"),
      ({"dirHash": "2a1bb6127fb481c60f67692e22285fb306f3c6ffe62075e0ccf674d7c3adcb8f"}, 1, "dirHash, 64 hex"),
      ({"dirHash1": "2a1bb6127fb481c60f67692e22285fb306f3c6ffe62075e0ccf674d7c3adcb8f"}, 1,
       "the source's own example key dirHash1 is a custom algorithm to a schema: it is NOT the standard name dirHash (source defect)"),
      ({"shake128": "ab"}, 1, "variable-length output: any lowercase hex"),
      ({"blake2b": "abcd" * 16, "sha256": H64}, 1, "two algorithms, algorithm agility"),
      ({"md5": H32}, 1, "md5 is a supported (if discouraged) algorithm"),
      ({"custom": "UPPER-and-Mixed_123"}, 1, "custom algorithm value is identifier-specific"),
      ({}, 0, "'Set of one or more' digests: empty object"),
      ([], 0, "array, not an object"), ("abcd", 0, "string, not an object"), (None, 0, "null"),
      ({"sha256": "ABCD"}, 0, "standard algorithm: lowercase hex only"),
      ({"sha256": "AbCd" + "0" * 60}, 0, "mixed-case hex"),
      ({"sha256": "zz"}, 0, "not hex"), ({"sha256": ""}, 0, "empty value for a hex algorithm"),
      ({"sha256": "sha256:" + H64}, 0, "algorithm prefix is not part of the encoding"),
      ({"sha256": "h1:Khu2En+0gcYPZ2kuIihfswbzxv/mIHXgzPZ018Oty48="}, 0, "base64 is not hex"),
      ({"sha256": 123}, 0, "value must be a string"), ({"sha256": None}, 0, "null value"),
      ({"custom": 5}, 0, "custom value must still be a string"),
      ({"custom": {"a": "b"}}, 0, "custom value object"), ({"custom": ["a"]}, 0, "custom value array"),
      ({"gitBlob": "5ab2f8a4"}, 0, "git id must be 40 or 64 hex"),
      ({"gitCommit": H40 + "0"}, 0, "41 hex"), ({"gitTag": H40[:-1] + "G"}, 0, "non-hex char in git id"),
      ({"gitTree": H40.upper().replace("0", "A")}, 0, "uppercase git id"),
      ({"dirHash": "2a1bb6127fb481c60f67692e22285fb306f3c6ffe62075e0ccf674d7c3adcb8"}, 0, "dirHash 63 hex"),
      ({"dirHash": "Khu2En+0gcYPZ2kuIihfswbzxv/mIHXgzPZ018Oty48="}, 0, "dirHash is hex, not the base64 h1: form"),
      ({"dirHash": "2A1BB6127FB481C60F67692E22285FB306F3C6FFE62075E0CCF674D7C3ADCB8F"}, 0, "dirHash uppercase"),
      ({"sha256": H64, "md5": "XY"}, 0, "one good entry does not excuse a bad one")]
for i, (v, ok, why) in enumerate(DS):
    case(f"ds-{i:02d}", "digest-set", v, "accept" if ok else "reject", why,
         ds_basis(v), lift="digest")
ALGS_HEX = ["sha256", "sha224", "sha384", "sha512", "sha512_224", "sha512_256", "sha3_224",
            "sha3_256", "sha3_384", "sha3_512", "shake128", "shake256", "blake2b", "blake2s",
            "ripemd160", "sm3", "gost", "sha1", "md5"]
_LEN = {"md5": 32, "sha1": 40, "sha224": 56, "sha256": 64, "sha384": 96, "sha512": 128,
        "sha512_224": 56, "sha512_256": 64, "sha3_224": 56, "sha3_256": 64, "sha3_384": 96,
        "sha3_512": 128, "ripemd160": 40, "sm3": 64}
for a in ALGS_HEX + ["gitCommit", "gitTree", "gitBlob", "gitTag", "dirHash"]:
    n = _LEN.get(a, 64 if a in ("gitCommit", "gitTree", "gitBlob", "gitTag", "dirHash") else 8)
    if a.startswith("git"): n = 40
    good = "a1" * (n // 2)
    for tag, v, ok, why in [("ok", good, 1, "lowercase hex of the usual length"),
                            ("upper", good.upper(), 0, "uppercase hex"),
                            ("trail", good + "!", 0, "junk after the hex"),
                            ("lead", "!" + good, 0, "junk before the hex"),
                            ("nl", good + "\n", 0, "trailing newline"),
                            ("empty", "", 0, "empty value"),
                            ("num", 5, 0, "non-string value"),
                            ("null", None, 0, "null value"),
                            ("odd", good + "a", 0, "odd-length hex encodes no byte string (pass 2)")]:
        case(f"ds-sweep-{a}-{tag}", "digest-set", {a: v}, "accept" if ok else "reject",
             f"{a}: {why}", ds_basis({a: v}), lift="digest")
for a in ["gitCommit", "gitTree", "gitBlob", "gitTag"]:
    for tag, v, ok, why in [("64", "a1" * 32, 1, "SHA-256 object id (64 hex)"),
                            ("39", "a1" * 19 + "a", 0, "39 hex"), ("65", "a1" * 32 + "a", 0, "65 hex"),
                            ("63", "a1" * 31 + "a", 0, "63 hex")]:
        case(f"ds-sweep-{a}-{tag}", "digest-set", {a: v}, "accept" if ok else "reject",
             f"{a}: {why}", ds_basis({a: v}), lift="digest")
for tag, v, ok in [("64", "a1" * 32, 1), ("65", "a1" * 32 + "a", 0), ("40", "a1" * 20, 0), ("128", "a1" * 64, 0)]:
    case(f"ds-sweep-dirHash-{tag}", "digest-set", {"dirHash": v}, "accept" if ok else "reject",
         f"dirHash: {len(v)} hex", ds_basis({"dirHash": v}), lift="digest")

DSL = [({"sha256": H64}, 1, "64 hex"), ({"md5": H32}, 1, "32 hex"), ({"sha1": H40}, 1, "40"),
       ({"sha224": "a" * 56}, 1, "56"), ({"sha384": "a" * 96}, 1, "96"), ({"sha512": H128}, 1, "128"),
       ({"sha512_224": "a" * 56, "sha512_256": "a" * 64}, 1, "sha512/t"),
       ({"sha3_224": "a" * 56, "sha3_256": "a" * 64, "sha3_384": "a" * 96, "sha3_512": H128}, 1, "sha3"),
       ({"ripemd160": H40, "sm3": H64}, 1, "ripemd160, sm3"),
       ({"shake128": "ab", "shake256": "abcd", "blake2b": "ab", "blake2s": "ab", "gost": "ab"}, 1,
        "variable or ambiguous output size: only lowercase hex is required"),
       ({"somecoolhash": "abcd"}, 1, "custom algorithm unaffected"),
       ({"sha256": "abcd"}, 0, "short sha256 (the source's own 5.3 example fails this stricter profile)"),
       ({"sha256": H64 + "0"}, 0, "65 hex"), ({"md5": H64}, 0, "md5 with 64 hex"),
       ({"sha1": H64}, 0, "sha1 with 64 hex"), ({"sha224": "a" * 64}, 0, "sha224 with 64"),
       ({"sha384": "a" * 64}, 0, "sha384 with 64"), ({"sha512": H64}, 0, "sha512 with 64"),
       ({"sha512_224": "a" * 64}, 0, "sha512_224 with 64"), ({"sha512_256": "a" * 56}, 0, "sha512_256 with 56"),
       ({"sha3_224": "a" * 64}, 0, "sha3_224 with 64"), ({"sha3_256": "a" * 56}, 0, "sha3_256 with 56"),
       ({"sha3_384": "a" * 64}, 0, "sha3_384 with 64"), ({"sha3_512": H64}, 0, "sha3_512 with 64"),
       ({"ripemd160": H64}, 0, "ripemd160 with 64"), ({"sm3": H40}, 0, "sm3 with 40"),
       ({"sha256": H64.upper().replace("0", "A")}, 0, "still lowercase only"),
       ({"gitBlob": H40}, 1, "git rule unchanged"), ({"dirHash": H64}, 1, "dirHash unchanged"),
       ({"gitBlob": "ab"}, 0, "git rule unchanged: too short"), ({"dirHash": "ab"}, 0, "dirHash unchanged: too short"),
       ({}, 0, "still one or more")]
for i, (v, ok, why) in enumerate(DSL):
    case(f"dsl-{i:02d}", "digest-set-lengths", v, "accept" if ok else "reject", why, ds_basis(v))

for a, n in _LEN.items():
    for tag, v, ok in [("ok", "a1" * (n // 2), 1), ("short", "a1" * (n // 2 - 1), 0),
                       ("long", "a1" * (n // 2 + 1), 0), ("upper", "A1" * (n // 2), 0),
                       ("junk", "a1" * (n // 2 - 1) + "a!", 0), ("lead", "!" + "a1" * (n // 2 - 1) + "a", 0),
                       ("num", 5, 0), ("null", None, 0)]:
        case(f"dsl-sweep-{a}-{tag}", "digest-set-lengths", {a: v}, "accept" if ok else "reject",
             f"{a}: {n} hex expected ({tag})", ds_basis({a: v}))
for a in ["shake128", "shake256", "blake2b", "blake2s", "gost"]:
    for tag, v, ok in [("ok", "a1", 1), ("upper", "A1", 0), ("junk", "a!", 0), ("num", 5, 0), ("odd", "a1a", 0)]:
        case(f"dsl-sweep-{a}-{tag}", "digest-set-lengths", {a: v}, "accept" if ok else "reject",
             f"{a}: variable length, lowercase hex", ds_basis({a: v}))
for a in ["gitCommit", "gitTree", "gitBlob", "gitTag", "dirHash"]:
    for tag, v, ok in [("ok", "a1" * 32, 1), ("bad", "a1" * 20 + "!", 0), ("5", "a1", 0),
                       ("upper", "A1" * 32, 0), ("lead", "!" + "a1" * 32, 0), ("trail", "a1" * 32 + "!", 0),
                       ("num", 5, 0)]:
        case(f"dsl-sweep-{a}-{tag}", "digest-set-lengths", {a: v}, "accept" if ok else "reject",
             f"{a}: unchanged by the lengths profile", ds_basis({a: v}))
for i, v in enumerate([[], "abcd", None, 5]):
    case(f"dsl-nonobject-{i}", "digest-set-lengths", v, "reject", "not an object", ds_basis(v))
case("dsl-custom-num", "digest-set-lengths", {"x": 5}, "reject", "custom value must be a string", ds_basis({"x": 5}))

# --- ResourceDescriptor
GOOD_B64 = "Ynl0ZXNjb250ZW50"
RD = [({"uri": "https://example.com"}, 1, "uri alone satisfies the minimum", [("R-0013", "MUST specify one of")]),
      ({"digest": {"sha256": H64}}, 1, "digest alone", [("R-0013", "MUST specify one of")]),
      ({"content": GOOD_B64}, 1, "content alone", [("R-0013", "MUST specify one of")]),
      ({"name": "Foo.apk", "uri": "git+https://android.googlesource.com/platform/vendor/foo/bar@16244f4e7524d44a8f3060905eaf9190e96e9fb0#prebuilts/Foo/Foo.apk", "digest": {"sha256": H64}}, 1, "4.4 'Pointer to a file' with the digest unabbreviated", []),
      ({"uri": "git+https://github.com/actions/runner", "digest": {"sha1": H40}, "annotations": {"twoPartyReview": False}}, 1, "4.4 'Pointer to a git repo'", []),
      ({"name": "gcc_9.3.0-1ubuntu2_amd64.intoto.json", "digest": {"sha256": H64}, "downloadLocation": "http://example.com/rebuilderd-instance/gcc_9.3.0-1ubuntu2_amd64.intoto.json", "mediaType": "application/x.dsse+json"}, 1, "4.4 'Pointer to another in-toto attestation'", []),
      ({"uri": "https://cloudbuild.googleapis.com/GoogleHostedWorker@v1"}, 1, "4.4 'Pointer to build service'", []),
      ({"uri": "https://tekton.dev/TaskRun/check/result/report", "digest": {"sha256": "ec87961dbfe8e7d8a73890c602ac7bd407b80b9e31c326beb9110bdd255f12e6"}, "content": "eyAicmVzdWx0IjogIlNVQ0NFU1MiLCAidGltZXN0YW1wIjogIjE2Nzc4NzIyMzYiLCAic3VjY2Vzc2VzIjogMjIsICJmYWlsdXJlcyI6IDAsICJ3YXJuaW5ncyI6MCB9", "mediaType": "application/json"}, 1, "4.4 'Descriptor for Tekton TaskRun', verbatim values", []),
      ({"uri": "x:y", "x.ext": 1, "ext_obj": {"a": 1}}, 1, "extension fields are allowed", [("R-0002", "Producers MAY add extension fields")]),
      ({"uri": "x:y", "annotations": {"s": "x", "n": 1, "f": 1.5, "o": {"k": 1}, "a": [1, "b"], "b": False, "z": None}}, 1, "annotations: any JSON value", [("R-0103", "any JSON value")]),
      ({"uri": "x:y", "name": "_"}, 1, "name '_' (statement.md: 'use \"_\"')", []),
      ({"uri": "x:y", "mediaType": "application/vnd.in-toto.bundle"}, 1, "vnd. media type", [("R-0101", "`vnd.`")]),
      ({"uri": "x:y", "mediaType": "text/plain; charset=utf-8"}, 1, "media type with parameter", []),
      ({"uri": "x:y", "content": ""}, 1, "present-but-empty content: the JSON key is set (the protobuf bindings cannot see this)", [("R-0013", "MUST specify one of")]),
      ({}, 0, "none of uri/digest/content", [("R-0013", "MUST specify one of")]),
      ({"name": "only"}, 0, "name alone does not satisfy the minimum (Go and Python accept it)", [("R-0013", "MUST specify one of")]),
      ({"name": "x", "downloadLocation": "https://example.com/t.zip", "mediaType": "a/b"}, 0, "name + downloadLocation + mediaType, none of the three", [("R-0013", "MUST specify one of")]),
      ({"downloadLocation": "https://example.com/t.zip"}, 0, "downloadLocation alone", [("R-0013", "MUST specify one of")]),
      ({"annotations": {"a": 1}}, 0, "annotations alone", [("R-0013", "MUST specify one of")]),
      ({"mediaType": "a/b"}, 0, "mediaType alone", [("R-0013", "MUST specify one of")]),
      ({"uri": 5}, 0, "uri must be a string", [RU_RFC]),
      ({"uri": "HTTPS://x.io"}, 0, "ResourceURI case normalization", [RU_LC]),
      ({"uri": "x.io/a"}, 0, "uri without a scheme", [RU_RFC]),
      ({"uri": "x:y", "downloadLocation": "Https://x.io/a"}, 0, "downloadLocation is a ResourceURI", [RU_LC]),
      ({"uri": "x:y", "downloadLocation": 5}, 0, "downloadLocation string", []),
      ({"digest": {}}, 0, "digest is a set of one or more (digest_set.md intro, no keyword)", []),
      ({"uri": "x:y", "digest": {}}, 0, "empty digest even with a uri (Go and Python accept it)", []),
      ({"uri": "x:y", "digest": "abc"}, 0, "digest is an object", []),
      ({"uri": "x:y", "digest": []}, 0, "digest as array", []),
      ({"uri": "x:y", "digest": {"sha256": "ABC"}}, 0, "digest value lowercase hex", []),
      ({"uri": "x:y", "name": 5}, 0, "name is a string", []),
      ({"uri": "x:y", "annotations": []}, 0, "annotations is a map", []),
      ({"uri": "x:y", "annotations": "x"}, 0, "annotations string", []),
      ({"uri": "x:y", "annotations": None}, 0, "annotations null", []),
      ({"content": 5}, 0, "content is base64 text in JSON", []),
      ({"content": "@@@"}, 0, "not base64", []),
      ({"content": "a.b"}, 0, "'.' is not a base64 character", []),
      ({"content": "ab=c"}, 0, "padding only at the end", []),
      ({"content": "A"}, 0, "one character encodes no byte (pass 2)", [("R-0203", "base64 string")]),
      ({"content": "AAAAA"}, 0, "five characters: no base64 length (pass 2)", [("R-0203", "base64 string")]),
      ({"content": "AA="}, 0, "one pad character after two data characters (pass 2)", [("R-0203", "base64 string")]),
      ({"content": "AAA=="}, 0, "two pad characters after three data characters (pass 2)", [("R-0203", "base64 string")]),
      ({"content": "ab+_"}, 0, "standard and URL-safe alphabets mixed in one value (pass 2)", [("R-0203", "base64 string")]),
      ({"content": "YQ"}, 1, "unpadded standard base64 (pass 2)", [("R-0203", "base64 string")]),
      ({"content": "Yg-_"}, 1, "URL-safe base64 (pass 2)", [("R-0203", "base64 string")]),
      ({"uri": "x:y", "mediaType": "json"}, 0, "not type/subtype", []),
      ({"uri": "x:y", "mediaType": " a/b"}, 0, "leading space", []),
      ({"uri": "x:y", "mediaType": "a/b/c"}, 0, "three segments", []),
      ({"uri": "x:y", "mediaType": "a/b c"}, 0, "space inside the subtype", []),
      ({"uri": "x:y", "mediaType": 5}, 0, "mediaType string", []),
      ({"uri": "x:y", "mediaType": ""}, 0, "empty mediaType", []),
      ([], 0, "array, not an object", []), ("x", 0, "string", []), (None, 0, "null", [])]
for i, (v, ok, why, b) in enumerate(RD):
    case(f"rd-{i:02d}", "resource-descriptor", v, "accept" if ok else "reject", why, b, lift="rd")

# --- Statement
SUB = {"digest": {"sha256": H64}}
ST = {"_type": "https://in-toto.io/Statement/v1", "subject": [SUB], "predicateType": "https://example.com/p/v1"}


def st(**kw):
    s = copy.deepcopy(ST)
    for k, v in kw.items():
        if v is KeyError: s.pop(k, None)
        else: s[k] = v
    return s


STC = [(st(), 1, "minimal: no predicate (predicate is optional)", [("R-0012", "MAY be omitted")]),
       (st(predicate={}), 1, "empty predicate = unset", [("R-0142", "Unset is treated the same as")]),
       (st(predicate={"a": {"b": [1, 2, None, True]}}), 1, "arbitrary object predicate", []),
       (st(subject=[{"name": "fooly.apk", "digest": {"sha256": H64}}]), 1, "name + digest", []),
       (st(subject=[{"uri": "pkg:deb/debian/stunnel@5.50-3?arch=amd64", "digest": {"sha256": H64}}]), 1, "uri + digest, no name", []),
       (st(subject=[{"name": "_", "digest": {"sha256": H64}}]), 1, "name '_'", []),
       (st(subject=[SUB, {"name": "b", "digest": {"gitCommit": H40}}]), 1, "two subjects", []),
       (st(subject=[{"name": "image", "digest": {"arn": "arn:aws:ec2:region:123:image/ami-123abcd"}}]), 1, "non-cryptographic immutable id (digest_set.md 5.2.3)", []),
       (st(subject=[{"digest": {"sha256": H64}, "content": GOOD_B64, "mediaType": "text/plain"}]), 1, "subject with content", []),
       (st(**{"x-ext": {"a": 1}}), 1, "unrecognized top-level field is ignored, not an error", [("R-0001", "MUST ignore unrecognized fields")]),
       (st(subject=[{"digest": {"sha256": H64}, "x-ext": 1}]), 1, "unrecognized subject field", [("R-0001", "MUST ignore unrecognized fields")]),
       (st(subject=[]), 1, "SPEC SILENT: empty subject array (Go and Python reject it; the source does not)", []),
       (st(_type="https://in-toto.io/Statement/v0.1"), 0, "v0.1 is not v1 (Go accepts it as a legacy type; Python rejects it); the const has no BCP 14 keyword ('Always ... for this version')", []),
       (st(_type="https://in-toto.io/Statement/v2"), 0, "v2", []),
       (st(_type="https://in-toto.io/statement/v1"), 0, "const is case sensitive", []),
       (st(_type="HTTPS://in-toto.io/Statement/v1"), 0, "TypeURI scheme case", []),
       (st(_type=KeyError), 0, "_type is required", []),
       (st(_type=5), 0, "_type must be a string", []),
       (st(subject=KeyError), 0, "subject is required", []),
       (st(subject=None), 0, "subject null", []),
       (st(subject={"digest": {"sha256": H64}}), 0, "subject is an array", []),
       (st(subject=[{"name": "x"}]), 0, "element without digest", [("R-0090", "MUST have")]),
       (st(subject=[{"uri": "x:y"}]), 0, "uri-only element: ResourceDescriptor-valid, subject-invalid", [("R-0090", "MUST have")]),
       (st(subject=[{"content": GOOD_B64}]), 0, "content-only element", [("R-0090", "MUST have")]),
       (st(subject=[{}]), 0, "empty element", [("R-0090", "MUST have")]),
       (st(subject=[SUB, {"name": "no-digest"}]), 0, "second element lacks digest", [("R-0090", "MUST have")]),
       (st(subject=[{"name": "x", "digest": {}}]), 0, "digest set but empty", [("R-0090", "MUST have")]),
       (st(subject=["x"]), 0, "element not an object", []),
       (st(subject=[{"digest": {"sha256": "ABCD"}}]), 0, "uppercase hex in a subject digest", []),
       (st(subject=[{"digest": {"gitBlob": "ab"}}]), 0, "short git id in a subject digest", []),
       (st(predicateType=KeyError), 0, "predicateType is required", []),
       (st(predicateType="thePredicate"), 0, "predicateType must be a TypeURI (Go/Python accept any non-empty string)", []),
       (st(predicateType=""), 0, "empty predicateType", []),
       (st(predicateType=5), 0, "predicateType not a string", []),
       (st(predicateType="HTTPS://example.com/p/v1"), 0, "predicateType TypeURI case", []),
       (st(predicate=[]), 0, "predicate is an object, not an array", []),
       (st(predicate="x"), 0, "predicate string", []),
       (st(predicate=None), 0, "predicate null", []),
       ([], 0, "array", []), ("x", 0, "string", []), (None, 0, "null", [])]
for i, (v, ok, why, b) in enumerate(STC):
    case(f"st-{i:02d}", "statement", v, "accept" if ok else "reject", why, b,
         silent=("SPEC SILENT" in why))

# --- Envelope
def env(**kw):
    e = {"payloadType": "application/vnd.in-toto+json", "payload": GOOD_B64,
         "signatures": [{"keyid": "SHA256:abc", "sig": "MEUCIQ=="}]}
    for k, v in kw.items():
        if v is KeyError: e.pop(k, None)
        else: e[k] = v
    return e


EN = [(env(), 1, "DSSE with the generic in-toto type", [("R-0058", "MUST be set to")]),
      (env(payloadType="application/vnd.in-toto.provenance+json"), 1, "predicate-specific form (bundle.md 9.4.1)", [("R-0058", "MUST be set to")]),
      (env(payloadType="application/vnd.in-toto.spdx+json"), 1, "predicate-specific form, spdx", [("R-0058", "MUST be set to")]),
      (env(payloadType="application/vnd.in-toto.vsa.v1+json"), 1, "<predicate> with a dot", [("R-0059", "MUST match")]),
      (env(signatures=[{"sig": "MEUCIQ=="}]), 1, "keyid is SHOULD, not required", [("R-0053", "SHOULD be included")]),
      (env(signatures=[{"keyid": "a", "sig": "AA=="}, {"keyid": "b", "sig": "BB=="}]), 1, "multiple signatures", [("R-0046", "multiple signatures")]),
      (env(signatures=[]), 1, "bundle.md 9.5 prints \"signatures\": [] (an envelope with no signatures; a verifier rejects it, the schema does not)", []),
      (env(**{"x-ext": 1}), 1, "extension field", []),
      (env(payloadType="application/vnd.in-toto.provenance+dsse"), 0, "the STORAGE media type (8.4) is not a payloadType", [("R-0058", "MUST be set to")]),
      (env(payloadType="application/vnd.in-toto+cbor"), 0, "DSSE-as-used requires +json (R-0057 alone would allow +<encoding>)", [("R-0058", "MUST be set to")]),
      (env(payloadType="application/json"), 0, "not an in-toto type", [("R-0058", "MUST be set to")]),
      (env(payloadType="application/vnd.in-toto.+json"), 0, "empty <predicate>", [("R-0059", "MUST match")]),
      (env(payloadType="application/vnd.in-toto.a/b+json"), 0, "'/' in <predicate>", [("R-0059", "MUST match")]),
      (env(payloadType="application/vnd.in-toto.a+b+json"), 0, "'+' in <predicate>", [("R-0059", "MUST match")]),
      (env(payloadType="Application/vnd.in-toto+json"), 0, "case: pattern is exact", []),
      (env(payloadType="x application/vnd.in-toto+json"), 0, "text before the type", []),
      (env(payloadType="application/vnd.in-toto+jsonx"), 0, "text after the type", []),
      (env(payloadType="application/vnd.in-toto+json\n"), 0, "trailing newline", []),
      (env(payloadType=5), 0, "payloadType string", []),
      (env(payloadType=KeyError), 0, "payloadType required", [("R-0058", "MUST be set to")]),
      (env(payload=KeyError), 0, "payload required in DSSE", [("R-0063", "MUST be a base64-encoded")]),
      (env(payload="AAAAA"), 0, "five characters: no base64 length (pass 2)", [("R-0063", "MUST be a base64-encoded")]),
      (env(signatures=[{"sig": "A"}]), 0, "one-character sig: no base64 length (pass 2)", []),
      (env(payload="a..."), 0, "'a...' is not base64 (the Bundle examples use it as a placeholder)", [("R-0063", "MUST be a base64-encoded")]),
      (env(payload=5), 0, "payload string", [("R-0063", "MUST be a base64-encoded")]),
      (env(payload={"_type": "x"}), 0, "payload is base64 text, not an inline object", [("R-0063", "MUST be a base64-encoded")]),
      (env(signatures=KeyError), 0, "signatures required", [("R-0117", "is REQUIRED")]),
      (env(signatures={"sig": "AA=="}), 0, "signatures is an array", [("R-0118", "array of digital signatures")]),
      (env(signatures=None), 0, "signatures null", [("R-0118", "array of digital signatures")]),
      (env(signatures=[{"keyid": "a"}]), 0, "signature entry needs sig (validation.md uses signature.sig)", []),
      (env(signatures=["AA=="]), 0, "signature entry is an object", []),
      (env(signatures=[{"sig": 5}]), 0, "sig string", []),
      (env(signatures=[{"sig": "not base64!"}]), 0, "sig base64", []),
      (env(signatures=[{"keyid": 5, "sig": "AA=="}]), 0, "keyid string", []),
      ([], 0, "array", []), ("x", 0, "string", []), (None, 0, "null", [])]
for i, (v, ok, why, b) in enumerate(EN):
    case(f"en-{i:02d}", "envelope", v, "accept" if ok else "reject", why, b)

# --- Bundle line (recognized vs unrecognized)
BL = [(env(payloadType="application/vnd.novulz+cbor"), 1, "9.4.2: a non-in-toto payloadType is still a recognized Envelope line", [("R-0074", "SHOULD be an")]),
      (env(), 1, "9.4.1 line", [("R-0074", "SHOULD be an")]),
      (env(signatures=[]), 1, "9.5 lines print signatures []", []),
      (env(signatures=[{"anything": 1}]), 1, "signature internals are the envelope's business", []),
      ({"payload": GOOD_B64, "signatures": []}, 0, "no payloadType: unrecognized, to be ignored", [("R-0075", "MUST ignore unrecognized lines")]),
      ({"payloadType": "x/y", "signatures": []}, 0, "no payload: unrecognized", [("R-0075", "MUST ignore unrecognized lines")]),
      ({"payloadType": "x/y", "payload": GOOD_B64}, 0, "no signatures: unrecognized", [("R-0075", "MUST ignore unrecognized lines")]),
      (env(signatures={}), 0, "signatures object: unrecognized", [("R-0075", "MUST ignore unrecognized lines")]),
      (env(payloadType=5), 0, "payloadType number: unrecognized", [("R-0075", "MUST ignore unrecognized lines")]),
      (env(payload="a..."), 0, "'a...' payload placeholder: unrecognized", [("R-0075", "MUST ignore unrecognized lines")]),
      (env(payload="AAAAA"), 0, "five-character payload, no base64 length: unrecognized (pass 2)", [("R-0075", "MUST ignore unrecognized lines")]),
      (env(payload=5), 0, "payload number: unrecognized", [("R-0075", "MUST ignore unrecognized lines")]),
      (env(signatures=[5]), 0, "signature entry not an object: unrecognized", [("R-0075", "MUST ignore unrecognized lines")]),
      (env(signatures="x"), 0, "signatures string: unrecognized", [("R-0075", "MUST ignore unrecognized lines")]),
      ([1, 2], 0, "JSON array line", [("R-0075", "MUST ignore unrecognized lines")]),
      ("a line", 0, "JSON string line", [("R-0075", "MUST ignore unrecognized lines")]),
      (42, 0, "JSON number line", [("R-0075", "MUST ignore unrecognized lines")]),
      (None, 0, "JSON null line", [("R-0075", "MUST ignore unrecognized lines")])]
for i, (v, ok, why, b) in enumerate(BL):
    case(f"bl-{i:02d}", "bundle-line", v, "accept" if ok else "reject", why, b)


# ---- lifting: reuse a def's cases inside the structures that embed it -----
def lifted():
    out = []
    for c in CASES:
        lf = c.get("lift")
        if not lf: continue
        v = c["inst"]
        if lf == "uri":      # ResourceURI inside a ResourceDescriptor and a subject
            out.append(("resource-descriptor", {"uri": v}, c))
            out.append(("resource-descriptor", {"digest": {"sha256": H64}, "downloadLocation": v}, c))
            out.append(("statement", st(subject=[{"digest": {"sha256": H64}, "uri": v}]), c))
        elif lf == "predicateType":
            out.append(("statement", st(predicateType=v), c))
        elif lf == "digest":
            out.append(("resource-descriptor", {"digest": v}, c))
            out.append(("statement", st(subject=[{"name": "n", "digest": v}]), c))
        elif lf == "rd":
            if c["id"] in ("rd-14", "rd-15", "rd-16", "rd-17", "rd-18", "rd-19", "rd-20"):
                continue   # their verdict depends on the descriptor lacking uri/digest/content
            if isinstance(v, dict):
                w = dict(v); w.setdefault("digest", {"sha256": H64})
                out.append(("statement", st(subject=[w]), c))
    return out


def all_cases():
    res = [(c["schema"], c.get("def"), c["inst"], c["expect"], c["id"]) for c in CASES]
    for sname, inst, src in lifted():
        # a lifted reject stays a reject; a lifted accept stays an accept
        res.append((sname, None, inst, src["expect"], src["id"] + "^" + sname))
    return res


# ---- deeper (non-schema) checks -------------------------------------------
def b64e(s):
    return base64.b64encode(s.encode()).decode()


def deep_envelope(e):
    """Envelope schema, then base64-decode payload, parse JSON, Statement schema."""
    if validate(load("envelope"), e): return False
    try:
        pl = json.loads(base64.b64decode(e["payload"]))
    except Exception:
        return False
    return not validate(load("statement"), pl)


DEEP = [(env(payload=b64e(json.dumps(ST))), 1, "payload is a base64 Statement"),
        (env(payload=b64e("not json")), 0, "payload decodes to non-JSON"),
        (env(payload=b64e(json.dumps(st(_type="https://in-toto.io/Statement/v2")))), 0, "payload Statement has a wrong _type"),
        (env(payload=b64e(json.dumps(st(subject=[{"name": "x"}])))), 0, "payload Statement subject lacks digest"),
        (env(payload=b64e(json.dumps([1]))), 0, "payload decodes to a JSON array")]


def check_bundle(text):
    """File level: JSON Lines. Returns (recognized, unrecognized, unparseable)."""
    rec = unrec = bad = 0
    lines = text.split("\n")
    if lines and lines[-1] == "": lines.pop()
    for ln in lines:
        if not ln.strip(): continue          # `grep .` in 9.5 drops blank lines
        try: v = json.loads(ln)
        except Exception: bad += 1; continue
        if validate(load("bundle-line"), v): unrec += 1
        else: rec += 1
    return rec, unrec, bad


BUNDLES = [
    ("\n".join(json.dumps(env(payloadType=t)) for t in
               ["application/vnd.in-toto.provenance+json", "application/vnd.in-toto+json",
                "application/vnd.novulz+cbor"]) + "\n", (3, 0, 0), "9.4.2 shape, three envelopes"),
    ("\n".join([json.dumps(env()), json.dumps({"hello": 1}), "[1]"]) + "\n", (1, 2, 0), "unrecognized JSON lines are counted, not errors"),
    (json.dumps(env()) + "\nnot json at all\n", (1, 0, 1), "a non-JSON line breaks 'MUST be encoded as JSON lines' (producer fault); consumers still ignore it"),
    ("", (0, 0, 0), "an empty file has no lines"),
]


# ---- runner ----------------------------------------------------------------
def run_cases(quiet=False):
    bad, n = [], 0
    for sname, defn, inst, expect, cid in all_cases():
        n += 1
        got = "accept" if verdict(sname, inst, defn) else "reject"
        if got != expect: bad.append((cid, sname, expect, got))
    for e, ok, why in DEEP:
        n += 1
        if deep_envelope(e) != bool(ok): bad.append(("deep:" + why, "envelope+statement", ok, not ok))
    for text, want, why in BUNDLES:
        n += 1
        if check_bundle(text) != want: bad.append(("bundle:" + why, "bundle", want, check_bundle(text)))
    return n, bad


def mutants(schema):
    """Yield (description, mutated schema) for every binding keyword."""
    def walk(node, path):
        if isinstance(node, dict):
            for k, v in list(node.items()):
                p = path + [k]
                if k in ("required", "minProperties", "minItems", "minLength", "const", "type", "pattern", "items", "$ref", "enum"):
                    if k == "required":
                        for r in v:
                            m = copy.deepcopy(schema); t = _get(m, path)
                            t["required"] = [x for x in v if x != r]
                            if not t["required"]: del t["required"]
                            yield f"{'/'.join(map(str, path))}: drop required {r}", m
                    else:
                        m = copy.deepcopy(schema); del _get(m, path)[k]
                        yield f"{'/'.join(map(str, path))}: drop {k}", m
                    if k == "pattern":
                        for d, new in _pattern_tweaks(v):
                            m = copy.deepcopy(schema); _get(m, path)["pattern"] = new
                            yield f"{'/'.join(map(str, path))}: pattern {d}", m
                if k == "anyOf":
                    for i in range(len(v)):
                        m = copy.deepcopy(schema); t = _get(m, path); del t["anyOf"][i]
                        yield f"{'/'.join(map(str, path))}: drop anyOf[{i}]", m
                if k == "additionalProperties" and v is not True:
                    m = copy.deepcopy(schema); _get(m, path)["additionalProperties"] = True
                    yield f"{'/'.join(map(str, path))}: additionalProperties -> true", m
                if k == "properties":
                    for pk in v:
                        m = copy.deepcopy(schema); del _get(m, path)["properties"][pk]
                        yield f"{'/'.join(map(str, path))}: drop property {pk}", m
                yield from walk(v, p)
        elif isinstance(node, list):
            for i, v in enumerate(node):
                yield from walk(v, path + [i])
    yield from walk(schema, [])


def _get(m, path):
    for p in path: m = m[p]
    return m


def _pattern_tweaks(p):
    out = []
    if "[0-9a-f]" in p: out.append(("lowercase hex -> any-case hex", p.replace("[0-9a-f]", "[0-9a-fA-F]")))
    if re.search(r"\{\d+\}", p): out.append(("fixed length -> +", re.sub(r"\{\d+\}", "+", p)))
    if p.startswith("^"): out.append(("drop ^ anchor", p[1:]))
    if p.endswith("$"): out.append(("drop $ anchor", p[:-1]))
    if "A-Z/?#" in p: out.append(("authority may contain uppercase", p.replace("A-Z/?#", "/?#")))
    if "(?!//)" in p: out.append(("drop no-authority alternative", p.replace("(?:(?!//)|", "(?:")))
    if "[a-z][a-z0-9" in p: out.append(("scheme may start uppercase", p.replace("[a-z][a-z0-9", "[A-Za-z][A-Za-z0-9", 1)))
    if "(?:0[1-9]|1[0-2])" in p: out.append(("month 13", p.replace("(?:0[1-9]|1[0-2])", "[0-9]{2}")))
    if "[01][0-9]|2[0-3]" in p: out.append(("hour 24", p.replace("[01][0-9]|2[0-3]", "[0-9]{2}")))
    if "\\.[0-9]+)?Z$" in p: out.append(("any zone", p.replace("Z$", "(?:Z|[+-][0-9:]+)?$")))
    # pass 2: the two length rules added to the hex and base64 patterns
    if "(?:[0-9a-f][0-9a-f])+" in p: out.append(("hex of any length", p.replace("(?:[0-9a-f][0-9a-f])+", "[0-9a-f]+")))
    if p.startswith("^(?:(?:[A-Za-z0-9+/]"): out.append(("base64 of any length, alphabets mixed", r"^[A-Za-z0-9+/_\-]*={0,2}$"))
    return out


def mutation_test():
    import tempfile
    cases = all_cases()
    names = sorted({c[0] for c in cases})
    total = killed = 0
    survivors = []
    for sname in names:
        base = load(sname)
        mine = [c for c in cases if c[0] == sname]
        for desc, m in mutants(base):
            total += 1
            dead = False
            for _, defn, inst, expect, cid in mine:
                s = {"$ref": f"#/$defs/{defn}", "$defs": m["$defs"]} if defn else m
                try:
                    got = "accept" if not validate(s, inst) else "reject"
                except Exception:
                    got = "error"
                if got != expect:
                    dead = True; break
            if dead: killed += 1
            else: survivors.append((sname, desc))
    return total, killed, survivors


# Mutants no instance can kill, with the reason. Kept explicit so a survivor is
# either a hole in the cases or a reasoned equivalent, never an unexamined number.
EQUIVALENT = [
    ("statement", "$defs/ResourceDescriptor: drop anyOf[0]",
     "the descriptor is only reached through subject[], which also requires digest"),
    ("statement", "$defs/ResourceDescriptor: drop anyOf[2]", "same: digest is always required here"),
    ("statement", "$defs/ResourceDescriptor/anyOf/0: drop required uri", "same"),
    ("statement", "$defs/ResourceDescriptor/anyOf/1: drop required digest", "same: digest also required by the subject items"),
    ("statement", "$defs/ResourceDescriptor/anyOf/2: drop required content", "same"),
]


def check_basis(reqpath):
    txt = open(reqpath).read()
    texts = {}
    for blk in re.split(r"\n  - id: ", txt)[1:]:
        rid = blk.split("\n", 1)[0].strip("'\"").split("#")[-1]
        m = re.search(r"\n    text: (.*)", blk)
        texts[rid] = m.group(1) if m else ""
    n, bad = 0, []
    for c in CASES:
        for rid, needle in c["basis"]:
            n += 1
            if rid not in texts or needle not in texts[rid]:
                bad.append((c["id"], rid, needle))
    return n, bad, len(texts)


def main():
    a = sys.argv[1:]
    if "--list" in a:
        for sname, defn, inst, expect, cid in all_cases():
            print(f"{cid:22} {sname:20} {defn or '':12} {expect:6} {json.dumps(inst)[:90]}")
        return 0
    n, bad = run_cases()
    print(f"cases examined: {n}  (direct {len(CASES)}, lifted {len(all_cases()) - len(CASES)}, "
          f"deep {len(DEEP)}, bundle files {len(BUNDLES)})")
    acc = sum(1 for c in all_cases() if c[3] == "accept"); rej = sum(1 for c in all_cases() if c[3] == "reject")
    print(f"  schema cases: {acc} must-accept, {rej} must-reject")
    for b in bad: print("FAIL", b)
    rc = 1 if bad else 0
    if "--mutate" in a:
        total, killed, surv = mutation_test()
        eq = [x for x in surv if any(x == (e[0], e[1]) for e in EQUIVALENT)]
        real = [x for x in surv if x not in eq]
        print(f"mutants examined: {total}  killed: {killed}  equivalent (reasoned): {len(eq)}  survived: {len(real)}")
        for x in eq: print("EQUIVALENT", *x)
        for s_ in real: print("SURVIVOR", *s_)
        if real: rc = 1
    if "--basis" in a:
        req = a[a.index("--basis") + 1]
        n2, bad2, nreq = check_basis(req)
        print(f"basis citations examined: {n2} against {nreq} requirements")
        for b in bad2: print("BASIS", b)
        if bad2: rc = 1
    print("OK" if not rc else "FAILED")
    return rc


if __name__ == "__main__":
    sys.exit(main())

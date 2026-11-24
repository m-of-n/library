#!/usr/bin/env python3
# DERIVED, not verbatim. Written by this library, not copied from SLSA.
# Re-extracts every fixture of this record from the source and checks it.
#
#   python3 -I reproduce.py            # check: fixtures on disk == re-extracted
#   python3 -I reproduce.py --write    # rewrite the fixtures, then check
#
# Needs the cached source (never committed): .cache/slsa-vsa-1-2.bin, the bytes of
# spec/verification_summary.md (slsa-framework/slsa releases/v1.2 @ ae7fc76), and
# .cache/slsa-vsa-1-2.txt, its rendering. Stdlib only. It:
#   1. re-runs ../render-source.py on the .bin and requires the .txt byte for byte
#      (the rendering is a pure function of the bytes: no line added or removed);
#   2. finds every fenced block in the .bin BY SCRIPT (no code-block detector in
#      bin/fx1-skeleton handles Markdown, report: "code blocks: 0") and requires
#      exactly the three fences L13-15, L64-104, L232-270;
#   3. cuts them, and the two section 5.1 worked examples, by line range, never
#      retyped, and requires the VERBATIM files byte-identical to the cut;
#   4. rebuilds the DERIVED files: the example with comments stripped, enclosing
#      braces added and trailing commas removed (the jsonc is not JSON: L266 and
#      L102 carry trailing commas, L87 lacks one, the blocks have no outer braces);
#   5. checks consumer-verification.derived.json against the section 5 steps as
#      section 5.1 applies them, with a mutation test (disable a step, some case
#      must flip);
#   6. cross-checks field names (section 3.2 headings, the schema block, the
#      example, ../schema, ../messages.yaml) and the 19 backticked SlsaResult
#      tokens of the prose (the four in the section 4 example are checked with it);
#   7. runs ../schema/check-schemas.derived.py and ../build-messages.derived.py --check.
import copy, hashlib, importlib.util, json, os, re, subprocess, sys, tempfile
sys.dont_write_bytecode = True

HERE = os.path.dirname(os.path.abspath(__file__))
DIST = os.path.dirname(HERE)
REC = os.path.dirname(DIST)
ROOT = os.path.abspath(os.path.join(REC, "..", "..", ".."))
SCHEMA = os.path.join(DIST, "schema")
RID = "slsa-vsa-1-2"
BIN = os.path.join(ROOT, ".cache", RID + ".bin")
TXT = os.path.join(ROOT, ".cache", RID + ".txt")
WRITE = "--write" in sys.argv[1:]
FAILS = []
CHECKS = [0]
PT = "https://slsa.dev/verification_summary/v1"


def check(cond, what):
    CHECKS[0] += 1
    if not cond:
        FAILS.append(what)


def read(p, mode="rb"):
    with open(p, mode) as fh:
        return fh.read()


def jdump(obj):
    return json.dumps(obj, indent=1, ensure_ascii=False) + "\n"


# ---- 1. rendering -----------------------------------------------------------
if not (os.path.exists(BIN) and os.path.exists(TXT)):
    sys.exit("missing %s or %s: fetch the source first (bin/fetch-source %s; see "
             "distilled/render-source.py)" % (BIN, TXT, RID))
binb, txtb = read(BIN), read(TXT)
src_sha = re.search(r'SHA256 = "([0-9a-f]{64})"', read(os.path.join(DIST, "render-source.py"), "r")).group(1)
check(hashlib.sha256(binb).hexdigest() == src_sha, ".bin sha256 != render-source.py SHA256")
with tempfile.TemporaryDirectory() as td:
    out = os.path.join(td, "r.txt")
    r = subprocess.run([sys.executable, "-I", os.path.join(DIST, "render-source.py"), BIN, out],
                       capture_output=True, text=True)
    check(r.returncode == 0, "render-source.py failed: " + r.stderr[:200])
    check(r.returncode == 0 and read(out) == txtb, ".txt differs from render-source.py output")
BL = binb.decode("utf-8").split("\n")
TL = txtb.decode("utf-8").split("\n")
check(len(BL) == len(TL) == 433 and BL[-1] == "" and TL[-1] == "", "line counts %d/%d, expected 432 lines and a final newline" % (len(BL), len(TL)))

# ---- 2. fences, by script ---------------------------------------------------
fences, openl = [], None
for i, line in enumerate(BL, 1):
    s = line.lstrip()
    if s.startswith("```"):
        if openl is None:
            openl = (i, s[3:].strip())
        else:
            fences.append((openl[0], i, openl[1]))
            openl = None
check(openl is None, "unclosed fence")
check(fences == [(13, 15, "json"), (64, 104, "jsonc"), (232, 270, "jsonc")], "fences %r" % fences)


def cut(lines, a, b):
    """lines a..b (1-based, inclusive) joined as the source file has them."""
    return ("\n".join(lines[a - 1:b]) + "\n").encode("utf-8")


# (path, first line, last line, source lines list, why)
OL = re.compile(r"^\d+\.\s")
VERB = [
    (os.path.join(HERE, "predicate-type.verbatim.json"), 14, 14),
    (os.path.join(SCHEMA, "vsa-schema.verbatim.jsonc"), 65, 103),
    (os.path.join(HERE, "example-vsa.verbatim.jsonc"), 233, 269),
    (os.path.join(HERE, "verify-example-1.verbatim.txt"), 322, 343),
    (os.path.join(HERE, "verify-example-2.verbatim.txt"), 345, 367),
]
for path, a, b in VERB:
    want = cut(BL, a, b)
    if WRITE:
        open(path, "wb").write(want)
    check(os.path.exists(path) and read(path) == want, "%s != source L%d-%d" % (os.path.basename(path), a, b))
    # the rendering carries the same lines (a column-0 ordered-list item gains one space)
    for n in range(a, b + 1):
        ok = TL[n - 1] == BL[n - 1] or (OL.match(BL[n - 1]) and TL[n - 1] == " " + BL[n - 1])
        check(ok, "rendering line %d differs from the .bin line beyond the list indent" % n)
# fence bounds are the lines just outside the cuts
for (a, b, _), (_, ca, cb) in zip(fences, VERB[:3]):
    check(ca == a + 1 and cb == b - 1, "cut L%d-%d is not the inside of fence L%d-%d" % (ca, cb, a, b))
check(BL[321].startswith("1.  Suppose consumer C") and BL[344].startswith("2.  Suppose consumer C"),
      "section 5.1 example boundaries moved")
check(BL[343] == "" and BL[367] == "", "blank lines after the 5.1 examples moved")


# ---- 4. derived JSON from the jsonc ----------------------------------------
def strip_jsonc(text):
    """Remove // comments and trailing commas, string-aware. The input is a
    fragment of members, so the caller adds the enclosing braces."""
    out, i, n, instr = [], 0, len(text), False
    while i < n:
        c = text[i]
        if instr:
            out.append(c)
            if c == "\\":
                out.append(text[i + 1]); i += 1
            elif c == '"':
                instr = False
        elif c == '"':
            instr = True; out.append(c)
        elif text.startswith("//", i):
            while i < n and text[i] != "\n":
                i += 1
            continue
        else:
            out.append(c)
        i += 1
    s, res, instr, i = "".join(out), [], False, 0
    while i < len(s):
        c = s[i]
        if instr:
            res.append(c)
            if c == "\\":
                res.append(s[i + 1]); i += 1
            elif c == '"':
                instr = False
        elif c == '"':
            instr = True; res.append(c)
        elif c == ",":
            j = i + 1
            while j < len(s) and s[j] in " \t\r\n":
                j += 1
            if j < len(s) and s[j] in "}]":
                i += 1
                continue
            res.append(c)
        else:
            res.append(c)
        i += 1
    return "".join(res)


ex_text = cut(BL, 233, 269).decode("utf-8")
example = json.loads("{\n" + strip_jsonc(ex_text) + "\n}")
# the defects, pinned: the raw example is not JSON, and not even once comments are removed
for label, text in [("raw fragment wrapped in braces", "{\n" + ex_text + "\n}")]:
    try:
        json.loads(text); check(False, label + " parsed as JSON; the jsonc defects moved")
    except ValueError:
        check(True, "")
# the jsonc defects, pinned: L266 trailing comma, L87/L88 missing comma, L102 trailing comma
check(BL[265].strip() == '"SLSA_BUILD_LEVEL_1": 1,' and BL[266].strip() == "},", "L266 trailing comma moved")
check(BL[86].strip() == "}" and BL[87].lstrip().startswith('"inputAttestations"'), "L87/88 missing comma moved")
check(BL[101].strip() == '"slsaVersion": "<MAJOR>.<MINOR>",' and BL[102].strip() == "}", "L102 trailing comma moved")
try:
    json.loads("{" + cut(BL, 65, 103).decode() + "}"); check(False, "schema block parsed as JSON")
except ValueError:
    check(True, "")

derived = {
    "example-vsa.derived.json": example,
    "predicate-type.derived.json": json.loads("{" + cut(BL, 14, 14).decode("utf-8") + "}"),
}
check(derived["predicate-type.derived.json"] == {"predicateType": PT}, "predicateType fence value")
check(example["predicateType"] == PT, "example predicateType")

# ---- 5. consumer verification (section 5 as section 5.1 applies it) --------
A = {"sha256": "5678..."}
V = "https://example.com/publication_verifier"
R = "https://example.com/example-1.2.3.tar.gz"
STEPS = [(1, "signature on the VSA envelope", "283-285"),
         (2, "subject matches the artifact digest", "287-288"),
         (3, "predicateType is the VSA type", "290-292"),
         (4, "verifier.id is V", "294-296"),
         (5, "resourceUri is R", "298-300"),
         (6, "verificationResult is PASSED", "302-303"),
         (7, "verifiedLevels contains an expected value", "305-306")]


def consumer_verify(vsa, exp, sig_ok, enabled=frozenset(range(1, 8))):
    """Return (accepted, first failed step number or None). exp: artifact digest
    set, verifier id, resourceUri, acceptable levels. Step 6 reads verificationResult:
    the 5.1 examples say `slsaResult` (L336, L360), the field was renamed by the 1.2
    change L405-406 (source defect SD-15, normative.md), so the field of section 3.2 is used."""
    p = vsa.get("predicate", {}) if isinstance(vsa.get("predicate"), dict) else {}
    tests = {
        1: lambda: sig_ok,
        2: lambda: any(isinstance(s.get("digest"), dict) and
                       all(s["digest"].get(k) == v for k, v in exp["digest"].items()) for s in vsa.get("subject", [])),
        3: lambda: vsa.get("predicateType") == PT,
        4: lambda: isinstance(p.get("verifier"), dict) and p["verifier"].get("id") == exp["verifier"],
        5: lambda: p.get("resourceUri") == exp["resourceUri"],
        6: lambda: p.get("verificationResult") == "PASSED",
        7: lambda: any(x in exp["levels"] for x in p.get("verifiedLevels", []) if isinstance(p.get("verifiedLevels"), list)),
    }
    for n in range(1, 8):
        if n in enabled and not tests[n]():
            return False, n
    return True, None


def vsa(**kw):
    s = copy.deepcopy(example)
    s["subject"] = [{"name": "out/example-1.2.3.tar.gz", "digest": dict(A)}]
    s["predicate"]["verifier"] = {"id": V}
    s["predicate"]["resourceUri"] = R
    for k, v in kw.items():
        if k == "subject": s["subject"] = v
        elif k == "predicateType": s["predicateType"] = v
        elif k == "_pred_del": [s["predicate"].pop(x, None) for x in v]
        else: s["predicate"][k] = v
    return s


EX1 = {"digest": A, "verifier": V, "resourceUri": R, "levels": ["SLSA_BUILD_LEVEL_UNEVALUATED"]}
EX2 = {"digest": A, "verifier": V, "resourceUri": R, "levels": ["SLSA_BUILD_LEVEL_2", "SLSA_BUILD_LEVEL_3"]}
CASES = []


def case(cid, ex, why, v, sig=True, sv=True):
    exp = EX1 if ex == 1 else EX2
    ok, step = consumer_verify(v, exp, sig)
    CASES.append({"id": cid, "example": ex, "why": why, "signature_ok": sig, "vsa": v,
                  "schema_valid": sv, "expect": {"accepted": ok, "failed_step": step}})


U1 = ["SLSA_BUILD_LEVEL_UNEVALUATED"]
case("C-01", 1, "example 1: every step holds (verifiedLevels contains SLSA_BUILD_LEVEL_UNEVALUATED)", vsa(verifiedLevels=U1))
case("C-02", 1, "example 1, step 1 fails: signature does not verify", vsa(verifiedLevels=U1), sig=False)
case("C-03", 1, "example 1, step 2 fails: subject digest is another artifact's", vsa(verifiedLevels=U1, subject=[{"name": "x", "digest": {"sha256": "9999"}}]))
case("C-04", 1, "example 1, step 3 fails: predicateType is the provenance type", vsa(verifiedLevels=U1, predicateType="https://slsa.dev/provenance/v1"), sv=False)
case("C-05", 1, "example 1, step 4 fails: verifier.id is not V", vsa(verifiedLevels=U1, verifier={"id": "https://example.com/other"}))
case("C-06", 1, "example 1, step 5 fails: resourceUri is not R", vsa(verifiedLevels=U1, resourceUri="https://example.com/other.tar.gz"))
case("C-07", 1, "example 1, step 6 fails: verificationResult FAILED", vsa(verifiedLevels=U1, verificationResult="FAILED"))
case("C-08", 1, "example 1, step 7 fails: verifiedLevels lacks the pre-negotiated value", vsa(verifiedLevels=["SLSA_BUILD_LEVEL_3"]))
case("C-09", 1, "example 1: the pre-negotiated value may sit beside others (contains, not equals)", vsa(verifiedLevels=U1 + ["SLSA_SOURCE_LEVEL_1"]))
case("C-10", 1, "example 1: no check of additional fields (dependencyLevels is irrelevant)", vsa(verifiedLevels=U1, dependencyLevels=None))
case("C-11", 2, "example 2: BUILD_LEVEL_2 passes", vsa(verifiedLevels=["SLSA_BUILD_LEVEL_2"]))
case("C-12", 2, "example 2: BUILD_LEVEL_3 passes", vsa(verifiedLevels=["SLSA_BUILD_LEVEL_3"]))
case("C-13", 2, "example 2: BUILD_LEVEL_1 fails (needs 2+)", vsa(verifiedLevels=["SLSA_BUILD_LEVEL_1"]))
case("C-14", 2, "example 2: UNEVALUATED fails", vsa(verifiedLevels=U1))
case("C-15", 2, "example 2: empty verifiedLevels fails step 7 (and is schema-valid: the source does not forbid it)", vsa(verifiedLevels=[]))
case("C-16", 2, "example 2: SOURCE_LEVEL_2 does not stand in for BUILD_LEVEL_2", vsa(verifiedLevels=["SLSA_SOURCE_LEVEL_2"]))
case("C-17", 2, "example 2: BUILD_LEVEL_2 beside SOURCE_LEVEL_1 passes", vsa(verifiedLevels=["SLSA_BUILD_LEVEL_2", "SLSA_SOURCE_LEVEL_1"]))
case("C-18", 2, "example 2: a VSA that says slsaResult instead of verificationResult (the L336/L360 name) fails step 6 and is schema-invalid",
     vsa(verifiedLevels=["SLSA_BUILD_LEVEL_3"], slsaResult="PASSED", _pred_del=["verificationResult"]), sv=False)
case("C-19", 2, "example 2: PASSED with two levels of one track is rejected by the schema's semantic rule but a consumer step 7 still sees BUILD_LEVEL_3",
     vsa(verifiedLevels=["SLSA_BUILD_LEVEL_3", "SLSA_BUILD_LEVEL_2"]), sv=False)

consumer = {
    "_comment": "DERIVED, not verbatim. Consumer-side verification cases written by this library from section 5 (L281-306) as section 5.1 applies it (L322-367): example 1 (L322-343) delegates fully to verifier V and expects verifiedLevels to contain SLSA_BUILD_LEVEL_UNEVALUATED; example 2 (L345-367) expects SLSA_BUILD_LEVEL_2 or SLSA_BUILD_LEVEL_3. Step 1 (signature on the envelope) is a boolean input: the envelope format is outside the source. `expect` is what consumer_verify() in reproduce.py computes (steps in order, first failure reported); `schema_valid` is the verdict of ../schema/vsa-statement.derived.schema.json plus its semantic rule, asserted by check-schemas.derived.py. Step 6 tests verificationResult, not the `slsaResult` the examples print (source defect SD-15, normative.md). The VSAs are chosen by this library.",
    "steps": [{"step": n, "what": w, "source_lines": l} for n, w, l in STEPS],
    "expectations": {"1": EX1, "2": EX2},
    "cases": CASES,
}
derived["consumer-verification.derived.json"] = consumer

for name, obj in derived.items():
    path = os.path.join(HERE, name)
    if WRITE:
        open(path, "w", encoding="utf-8").write(jdump(obj))
    check(os.path.exists(path) and read(path, "r") == jdump(obj), name + " != rebuilt")

# the fixture on disk drives the check, not only the in-memory rebuild
try:
    disk = json.loads(read(os.path.join(HERE, "consumer-verification.derived.json"), "r"))
except Exception as e:  # noqa
    disk = consumer
    check(False, "consumer fixture unreadable: %s" % e)
for c in disk["cases"]:
    exp = disk["expectations"][str(c["example"])]
    ok, step = consumer_verify(c["vsa"], exp, c["signature_ok"])
    check((ok, step) == (c["expect"]["accepted"], c["expect"]["failed_step"]), "consumer case %s" % c["id"])
# every step is bound by some case, and every step is exercised as the FIRST failure
for n in range(1, 8):
    flips = [c["id"] for c in disk["cases"]
             if consumer_verify(c["vsa"], disk["expectations"][str(c["example"])], c["signature_ok"],
                                frozenset(range(1, 8)) - {n})[0] != c["expect"]["accepted"]]
    check(bool(flips), "consumer step %d binds nothing: no case changes when it is disabled" % n)
    # pass 1's comment claimed this; pass 2 added the check that makes it true
    check(any(c["expect"]["failed_step"] == n for c in disk["cases"]), "consumer step %d is no case's first failure" % n)
check(sum(1 for c in disk["cases"] if c["expect"]["accepted"]) >= 5 and
      sum(1 for c in disk["cases"] if not c["expect"]["accepted"]) >= 10, "case mix")

# ---- 6. cross-checks --------------------------------------------------------
spec = importlib.util.spec_from_file_location("chk", os.path.join(SCHEMA, "check-schemas.derived.py"))
chk = importlib.util.module_from_spec(spec)
spec.loader.exec_module(chk)
reg, names = chk.load_registry()
pred = reg["urn:library:slsa-vsa-1-2:vsa-predicate.derived"]


def flat(s, prefix=""):
    o = set()
    for k, v in s.get("properties", {}).items():
        o.add(prefix + k)
        o |= flat(v, prefix + k + ".") if k in ("verifier",) else set()
    return o


# schema properties vs the section 3.2 field headings (lines of the form  `name` _type, required_)
heads = {m.group(1) for l in TL for m in [re.match(r"^`([A-Za-z.]+)` _", l)] if m}
check(heads == flat(pred), "3.2 headings %s != schema properties %s" % (sorted(heads), sorted(flat(pred))))
# required / optional words of the headings equal the schema's required lists
words = {}
for l in TL:
    m = re.match(r"^`([A-Za-z.]+)` _.*?, (required|optional)_$", l)
    if m:
        words[m.group(1)] = m.group(2)
check(len(words) == 11, "found %d heading required/optional markers, expected 11" % len(words))
req = set(pred["required"]) | {"verifier." + x for x in pred["properties"]["verifier"]["required"]}
check({k for k, v in words.items() if v == "required"} == req, "required set %s vs schema %s" % (
    sorted(k for k, v in words.items() if v == "required"), sorted(req)))
# example members are all known to the schema
for k in example["predicate"]:
    check(k in pred["properties"], "example member %s not in the schema" % k)
# every backticked SlsaResult token of the prose is accepted; placeholders are not tokens
toks = []
for n, l in enumerate(TL, 1):
    if n in (14, 66, 73):
        continue
    for t in re.findall(r"`([A-Za-z_0-9]+)`", l):
        if re.fullmatch(r"SLSA_[A-Z]+_LEVEL_(UNEVALUATED|[0-9]+)", t) or t == "FAILED":
            toks.append((n, t))
sr = reg["urn:library:slsa-vsa-1-2:slsa-result.derived"]
for n, t in toks:
    check(not chk.validate(t, sr, reg), "L%d: %s not accepted by slsa-result" % (n, t))
check(len(toks) == 19, "%d SlsaResult tokens found, 19 expected (the source is fixed)" % len(toks))
# the jsonc has the same predicate members as the example (names only)
blk = [m.group(2) for l in cut(BL, 65, 103).decode().split("\n") for m in [re.match(r'^(\s*)"(\w+)":', l)] if m]
check(set(example["predicate"]) == set(pred["properties"]), "example predicate members != schema properties")
check({"verifier", "timeVerified", "resourceUri", "policy", "inputAttestations", "verificationResult",
       "verifiedLevels", "dependencyLevels", "slsaVersion"} <= set(blk), "schema block members")
# ../messages.yaml names the same fields as the schema (pass 1's header claimed this
# check and the code had none; pass 2 added it)
sys.path.insert(0, os.path.join(ROOT, "bin"))
from _yaml import parse as _parse  # noqa: E402
MSGS = {m["id"]: m for m in _parse(read(os.path.join(DIST, "messages.yaml"), "r"))["messages"]}
props = pred["properties"]
for mid, want in [("MSG-02", set(props)), ("MSG-03", set(props["verifier"]["properties"])),
                  ("MSG-04", set(props["policy"]["properties"])),
                  ("MSG-05", set(props["inputAttestations"]["items"]["properties"]))]:
    got = {f["name"] for f in MSGS[mid]["fields"]}
    check(got == want, "messages.yaml %s fields %s != schema %s" % (mid, sorted(got), sorted(want)))
stmt = reg["urn:library:slsa-vsa-1-2:vsa-statement.derived"]
check({f["name"] for f in MSGS["MSG-01"]["fields"]} == set(stmt["properties"]), "messages.yaml MSG-01 fields != Statement schema")

# ---- 7. the other checkers --------------------------------------------------
for label, argv in [("check-schemas", [os.path.join(SCHEMA, "check-schemas.derived.py")]),
                    ("build-messages --check", [os.path.join(HERE, "build-messages.derived.py"), "--check"])]:
    r = subprocess.run([sys.executable, "-I"] + argv, capture_output=True, text=True)
    last = (r.stdout.strip().split("\n") or [""])[-1]
    check(r.returncode == 0, "%s failed: %s %s" % (label, r.stdout[-400:], r.stderr[-200:]))
    print("  %s: %s" % (label, last))

print("fixtures: %d verbatim, %d derived; consumer cases %d; SlsaResult tokens %d" % (
    len(VERB), len(derived), len(disk["cases"]), len(toks)))
print("checks run: %d, failed: %d" % (CHECKS[0], len(FAILS)))
for f in FAILS:
    print("FAIL:", f)
sys.exit(1 if FAILS else 0)

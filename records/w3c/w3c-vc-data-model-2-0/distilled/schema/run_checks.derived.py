#!/usr/bin/env python3
"""DERIVED, not verbatim. run_checks -- the checks this lane ran, so a reader can re-run them.

    python3 -I run_checks.derived.py schema-tests        # schema-tests.derived.json against the derived schemas
    python3 -I run_checks.derived.py metaschema          # every derived schema against the 2020-12 metaschema
    python3 -I run_checks.derived.py examples            # every fixture in ../examples/, writes ../examples/results.derived.json
    python3 -I run_checks.derived.py examples --check    # recompute and compare with the committed results (exit 1 on any difference)

Needs the third-party packages jsonschema (>=4.18, with referencing) and cbor2; the standard library
alone cannot validate JSON Schema 2020-12 or decode COSE. Nothing here is the source's own; the
schemas it reads are *.derived.schema.json. Every check prints EXAMINED beside FOUND.
"""
import base64, hashlib, json, os, re, sys
import cbor2
from jsonschema import Draft202012Validator
from referencing import Registry, Resource

HERE = os.path.dirname(os.path.abspath(__file__))
EX = os.path.join(os.path.dirname(HERE), "examples")
BASE = "urn:library:w3c-vc-data-model-2-0:"


def load(name):
    return json.load(open(os.path.join(HERE, name), encoding="utf-8"))


SCHEMAS = {"vcdm.derived": load("vcdm.derived.schema.json"), "verification-result.derived": load("verification-result.derived.schema.json")}
REG = Registry()
for _n, _s in SCHEMAS.items():
    REG = REG.with_resource(_s["$id"], Resource.from_contents(_s))


def validator(target):
    """target 'vcdm.derived#VerifiableCredential' (an anchor) or 'vcdm.derived' (the root)."""
    return Draft202012Validator({"$ref": BASE + target}, registry=REG)


def errors(target, inst):
    return sorted(validator(target).iter_errors(inst), key=lambda e: [str(x) for x in e.path])


def short(errs, n=3):
    return "; ".join("%s @/%s" % (e.message[:90], "/".join(map(str, e.path))) for e in errs[:n])


# ---------------------------------------------------------------- cross-field rules (X-nn) as code
DTS = re.compile(SCHEMAS["vcdm.derived"]["$defs"]["dateTimeStamp"]["pattern"])


def to_utc(s):
    """dateTimeStamp -> seconds since epoch (float), or None. 24:00:00 is the end of the day."""
    m = re.match(r"^(-?\d{4,})-(\d\d)-(\d\d)T(\d\d):(\d\d):(\d\d)(\.\d+)?(Z|[+-]\d\d:\d\d)$", s)
    if not m:
        return None
    import datetime
    y, mo, d, h, mi, se = (int(m.group(i)) for i in range(1, 7))
    fr = float(m.group(7) or 0)
    extra = 0
    if h == 24:
        h, extra = 0, 86400
    try:
        dt = datetime.datetime(y, mo, d, h, mi, se, tzinfo=datetime.timezone.utc)
    except ValueError:
        return None
    off = 0
    z = m.group(8)
    if z != "Z":
        off = (int(z[1:3]) * 3600 + int(z[4:6]) * 60) * (1 if z[0] == "+" else -1)
    return dt.timestamp() + extra + fr - off


def x01(doc):
    """X-01: validFrom is the same as or earlier than validUntil (temporal comparison)."""
    a, b = doc.get("validFrom"), doc.get("validUntil")
    if not isinstance(a, str) or not isinstance(b, str):
        return "na", "needs both validFrom and validUntil"
    ta, tb = to_utc(a), to_utc(b)
    if ta is None or tb is None:
        return "na", "a value is not a dateTimeStamp (schema reports it)"
    return ("pass" if ta <= tb else "fail"), "validFrom %s, validUntil %s" % (a, b)


def x03(doc):
    """X-03: relatedResource ids are unique in the list."""
    rr = doc.get("relatedResource")
    if rr is None:
        return "na", "no relatedResource"
    items = rr if isinstance(rr, list) else [rr]
    ids = [i.get("id") for i in items if isinstance(i, dict)]
    return ("pass" if len(ids) == len(set(ids)) else "fail"), "%d ids" % len(ids)


def x05(vp):
    """X-05: a presentation embedding a self-asserted credential (issuer == holder) that carries no proof of its own MUST have holder."""
    vcs = vp.get("verifiableCredential")
    if vcs is None:
        return "na", "no verifiableCredential"
    vcs = vcs if isinstance(vcs, list) else [vcs]
    holder = vp.get("holder")
    hid = holder.get("id") if isinstance(holder, dict) else holder
    if hid is None:
        # Pass 2 (verify): this branch used to report pass. With no holder, L2545's test (issuer value
        # identical to the holder value) marks no credential self-asserted, so the rule cannot apply,
        # and L2541's test (the issuer is the holder entity) cannot be decided from the document.
        return "na", "%d embedded credentials; no holder, so none is self-asserted by L2545 and L2541 is undecidable from the document" % len(vcs)
    selfa = []
    for c in vcs:
        if isinstance(c, dict) and "issuer" in c:
            iss = c["issuer"]
            iid = iss.get("id") if isinstance(iss, dict) else iss
            if hid is not None and iid == hid:
                selfa.append(c)
    return "pass", "%d embedded credentials, %d self-asserted by issuer == holder (holder present: %s)" % (len(vcs), len(selfa), hid is not None)


def b64u(s):
    s = re.sub(r"\s+", "", s)
    return base64.urlsafe_b64decode(s + "=" * (-len(s) % 4))


def jl(b):
    return json.loads(b.decode("utf-8"))


# ---------------------------------------------------------------- schema tests
def run_schema_tests():
    T = load("schema-tests.derived.json")
    examined = found = 0
    out = []
    for c in T["cases"]:
        inst = c["instance"] if "instance" in c else json.loads(open(os.path.join(EX, c["fixture"]), encoding="utf-8").read().replace("\u00a0", " "))
        got = "accept" if not errors(c["schema"], inst) else "reject"
        examined += 1
        if got != c["expect"]:
            found += 1
            out.append("  %s: schema %s expected %s got %s (%s)" % (c["id"], c["schema"], c["expect"], got, short(errors(c["schema"], inst))))
    print("schema-tests: EXAMINED %d cases (%d accept, %d reject expected), FOUND %d unexpected verdict(s)"
          % (examined, sum(1 for c in T["cases"] if c["expect"] == "accept"), sum(1 for c in T["cases"] if c["expect"] == "reject"), found))
    print("\n".join(out))
    return found


def run_metaschema():
    n = bad = 0
    for name, s in SCHEMAS.items():
        n += 1
        try:
            Draft202012Validator.check_schema(s)
        except Exception as e:
            bad += 1
            print("  %s: %s" % (name, str(e)[:200]))
    # every $ref/$anchor resolves: validate a trivial instance through every anchor
    anchors = 0
    for name, s in SCHEMAS.items():
        for k, d in s["$defs"].items():
            a = d.get("$anchor")
            if a:
                anchors += 1
                try:
                    list(validator(name + "#" + a).iter_errors({}))
                except Exception as e:
                    bad += 1
                    print("  %s#%s does not resolve: %s" % (name, a, str(e)[:160]))
    print("metaschema: EXAMINED %d schemas against the 2020-12 metaschema and %d anchors for resolution, FOUND %d problem(s)" % (n, anchors, bad))
    return bad


# ---------------------------------------------------------------- examples
def read_fx(f):
    return open(os.path.join(EX, f), encoding="utf-8").read()


def chk(res, cid, what, result, detail=""):
    res.append({"check": cid, "what": what, "result": result, "detail": detail})


def vc_vp_anchor(d):
    t = d.get("type")
    t = [t] if isinstance(t, str) else (t or [])
    for a in ("VerifiableCredential", "VerifiablePresentation", "EnvelopedVerifiableCredential", "EnvelopedVerifiablePresentation"):
        if a in t:
            return a
    return None


def J(v):
    """parse a display; whole-line // comments are dropped first when plain parsing fails (Example 35 only)."""
    v = v.replace("\u00a0", " ")
    try:
        return json.loads(v)
    except Exception:
        return json.loads(strip_comment_lines(v))


def strip_comment_lines(t):
    return "\n".join(l for l in t.split("\n") if not l.strip().startswith("//"))


def model_checks(res, tag, d, view=""):
    """schema + cross-field checks on one parsed data model object."""
    a = vc_vp_anchor(d) if isinstance(d, dict) else None
    sfx = (" [" + view + "]") if view else ""
    if a is None:
        chk(res, tag + "classify", "object has no data-model type" + sfx, "na", "type: %r" % (d.get("type") if isinstance(d, dict) else type(d).__name__))
        return
    e = errors("vcdm.derived#" + a, d)
    chk(res, tag + "must:" + a, "MUST profile #%s%s" % (a, sfx), "pass" if not e else "fail", short(e))
    if a in ("VerifiableCredential", "VerifiablePresentation"):
        e2 = errors("vcdm.derived#" + a + "-should", d)
        chk(res, tag + "should:" + a, "SHOULD profile #%s-should%s" % (a, sfx), "pass" if not e2 else "deviation", short(e2))
    if a == "VerifiableCredential" and e:
        e3 = errors("vcdm.derived#VerifiableCredential-arity", d)
        chk(res, tag + "must:arity", "MUST profile, reading B (#VerifiableCredential-arity)" + sfx, "pass" if not e3 else "fail", short(e3))
    if a == "VerifiableCredential":
        r, det = x01(d)
        chk(res, tag + "X-01", "X-01 validFrom <= validUntil" + sfx, r, det)
        r, det = x03(d)
        chk(res, tag + "X-03", "X-03 relatedResource ids unique" + sfx, r, det)
    if a == "VerifiablePresentation":
        r, det = x05(d)
        chk(res, tag + "X-05", "X-05 self-asserted credential in presentation" + sfx, r, det)
        for i, c in enumerate(d.get("verifiableCredential") if isinstance(d.get("verifiableCredential"), list) else [d.get("verifiableCredential")] if d.get("verifiableCredential") else []):
            if isinstance(c, dict):
                r, det = x01(c)
                chk(res, tag + "X-01.%d" % i, "X-01 on embedded credential %d%s" % (i, sfx), r, det)


def analyze_file(f, text, sibs):
    """Return the list of checks for fixture f. sibs: dict filename -> text, for the same example."""
    res = []
    n = text.replace("\u00a0", " ")
    stem = re.sub(r"^ex\d+-", "", f)
    pre = f.endswith(".json")
    # ---- JSON displays
    if pre and not stem.startswith("sd-jwt-decoded"):
        try:
            d = json.loads(n)
            chk(res, "parse", "parses as JSON", "pass")
            view = ""
        except Exception as ex:
            chk(res, "parse", "parses as JSON", "fail", str(ex)[:120])
            d = None
            s2 = strip_comment_lines(n)
            if s2 != n:
                try:
                    d = json.loads(s2)
                    chk(res, "parse-nocomments", "parses as JSON after dropping whole-line // comments (in memory, no file written)", "pass")
                    view = "comment lines dropped"
                except Exception as ex2:
                    chk(res, "parse-nocomments", "parses as JSON after dropping whole-line // comments", "fail", str(ex2)[:120])
        if d is not None and isinstance(d, dict):
            if stem == "jose-protected-headers.json":
                chk(res, "kind", "JOSE protected header (defined by VC-JOSE-COSE, not this source)", "na", "keys %s" % sorted(d))
            else:
                model_checks(res, "", d, view if not (isinstance(view, str) and view == "") else "")
        # fragments
        m = re.match(r"^ex(25|26)-main\.json$", f)
        if m:
            try:
                w = json.loads("{" + n + "}")
                chk(res, "wrap", "parses once wrapped in braces (the display is a member, not a document)", "pass")
                e = errors("vcdm.derived#relatedResource", w["relatedResource"])
                chk(res, "must:relatedResource", "MUST profile #relatedResource", "pass" if not e else "fail", short(e))
                e2 = errors("vcdm.derived#relatedResource-should", w["relatedResource"])
                chk(res, "should:relatedResource", "SHOULD profile #relatedResource-should", "pass" if not e2 else "deviation", short(e2))
                r, det = x03({"relatedResource": w["relatedResource"]})
                chk(res, "X-03", "X-03 relatedResource ids unique", r, det)
                # digests against the fetched context files
                import hashlib as H
                CT = {"https://www.w3.org/ns/credentials/v2": "context-credentials-v2.verbatim.jsonld", "https://www.w3.org/ns/credentials/examples/v2": "context-credentials-examples-v2.verbatim.jsonld"}
                for it in w["relatedResource"]:
                    b = open(os.path.join(HERE, CT[it["id"]]), "rb").read()
                    if "digestSRI" in it:
                        want = "sha384-" + base64.b64encode(H.sha384(b).digest()).decode()
                        chk(res, "digest:" + it["id"][-20:], "printed digestSRI equals sha384 of the fetched %s" % CT[it["id"]], "pass" if it["digestSRI"] == want else "fail", "printed %s ; computed %s (printed has %d base64 characters, computed %d)" % (it["digestSRI"], want, len(it["digestSRI"]) - 7, len(want) - 7))
                    else:
                        want = "u" + base64.urlsafe_b64encode(b"\x12\x20" + H.sha256(b).digest()).decode().rstrip("=")
                        chk(res, "digest:" + it["id"][-20:], "printed digestMultibase equals u+base64url(multihash sha2-256) of the fetched %s" % CT[it["id"]], "pass" if it["digestMultibase"] == want else "fail", "printed %s ; computed %s" % (it["digestMultibase"], want))
            except Exception as ex:
                chk(res, "wrap", "parses once wrapped in braces", "fail", str(ex)[:100])
        m = re.match(r"^ex(37|38|39|36)-main\.json$", f)
        if m:
            try:
                w = json.loads("{" + n + "}")
                key = list(w)[0]
                v = w[key]
                chk(res, "wrap", "parses once wrapped in braces (a member display)", "pass")
                vals = v if isinstance(v, list) else [v]
                bad = [short(errors("vcdm.derived#languageValueObject", x)) for x in vals if errors("vcdm.derived#languageValueObject", x)]
                chk(res, "must:lvo", "each value against #languageValueObject (MUST)", "pass" if not bad else "fail", "; ".join(bad))
                bad = [short(errors("vcdm.derived#languageValueObject-should", x)) for x in vals if errors("vcdm.derived#languageValueObject-should", x)]
                chk(res, "should:lvo", "each value against #languageValueObject-should", "pass" if not bad else "deviation", "; ".join(bad))
            except Exception as ex:
                chk(res, "wrap", "parses once wrapped in braces (a member display)", "fail", str(ex)[:100])
        # secured-form checks inside tabbed examples
        mt = re.match(r"^(ecdsa-sd|ecdsa|bbs)-application-vc\.json$", stem)
        if mt and d is not None:
            tab = mt.group(1)
            suite = {"ecdsa": "ecdsa-rdfc-2019", "ecdsa-sd": "ecdsa-sd-2023", "bbs": "bbs-2023"}[tab]
            e = errors("vcdm.derived#VerifiableCredential-embedded-proof", d)
            chk(res, "embedded-proof", "has an embedded proof (#VerifiableCredential-embedded-proof)", "pass" if not e else "fail", short(e))
            p = d.get("proof")
            chk(res, "suite", "proof.type DataIntegrityProof and cryptosuite %s" % suite, "pass" if isinstance(p, dict) and p.get("type") == "DataIntegrityProof" and p.get("cryptosuite") == suite else "fail", "proof: type %r cryptosuite %r" % (p.get("type") if isinstance(p, dict) else None, p.get("cryptosuite") if isinstance(p, dict) else None))
            body = {k: v for k, v in d.items() if k != "proof"}
            cred = next((v for k, v in sibs.items() if k.endswith("-credential.json")), None)
            if cred is not None:
                try:
                    cj = J(cred)
                    chk(res, "same-body", "credential without proof equals the Credential tab (value equality)", "pass" if body == cj else "fail", "" if body == cj else "differs: " + ", ".join(sorted(set(k for k in set(body) | set(cj) if body.get(k) != cj.get(k)))))
                except Exception:
                    chk(res, "same-body", "credential without proof equals the Credential tab", "na", "Credential tab is not JSON")
            chk(res, "signature", "proof signature verifies", "unverifiable", "the source prints no key for %s" % p.get("verificationMethod") if isinstance(p, dict) else "no proof")
        if stem == "jose-application-vc.json" and d is not None:
            cred = next((v for k, v in sibs.items() if k.endswith("-credential.json")), None)
            if cred is not None:
                try:
                    chk(res, "same-body", "JOSE payload tab equals the Credential tab (value equality)", "pass" if d == J(cred) else "fail")
                except Exception:
                    chk(res, "same-body", "JOSE payload tab equals the Credential tab", "na", "Credential tab is not JSON")
        if stem == "cose-application-vc.json" and d is not None:
            cred = next((v for k, v in sibs.items() if k.endswith("-credential.json")), None)
            if cred is not None:
                try:
                    chk(res, "same-body", "COSE payload tab equals the Credential tab (value equality)", "pass" if d == J(cred) else "fail")
                except Exception:
                    chk(res, "same-body", "COSE payload tab equals the Credential tab", "na", "Credential tab is not JSON")
        return res
    # ---- Example 32 regex
    if f == "ex32-main.txt":
        rx = n.replace("\n", "").replace(" ", "")
        want = SCHEMAS["vcdm.derived"]["$defs"]["dateTimeStamp"]["pattern"]
        chk(res, "joined", "five lines joined without whitespace equal the schema pattern minus anchors", "pass" if "^" + rx + "$" == want else "fail")
        try:
            cr = re.compile("^" + rx + "$")
            good = ["2010-01-01T00:00:00Z", "2024-07-12T12:00:00-07:00", "2024-04-03T00:00:00.000Z", "2023-01-01T24:00:00Z", "2020-02-30T00:00:00Z", "2021-11-01T00:00:00+14:00"]
            badv = ["2010-01-01T00:00:00", "2010-01-01 00:00:00Z", "2010-1-1T00:00:00Z", "2010-01-01T25:00:00Z", "2010-01-01T00:00:00+14:01", "2010-01-01"]
            ok = [bool(cr.match(x)) for x in good]
            ko = [bool(cr.match(x)) for x in badv]
            chk(res, "samples", "compiles; accepts %d samples (incl. 2020-02-30, which is not a date: the text warns of this) and rejects %d offset-less or malformed ones" % (len(good), len(badv)), "pass" if all(ok) and not any(ko) else "fail", "accepted %s ; rejected-expected-but-accepted %s" % (ok, ko))
        except re.error as ex:
            chk(res, "samples", "compiles as a regular expression", "fail", str(ex))
        return res
    # ---- compact forms
    t = re.sub(r"\s+", "", text)
    base = re.sub(r"-(jwt|cose|encoded)", "", stem)
    if f.endswith(".jwt"):
        parts = t.split(".")
        chk(res, "shape", "JWS compact serialisation: three base64url parts", "pass" if len(parts) == 3 and all(re.fullmatch(r"[A-Za-z0-9_-]*", p) for p in parts) else "fail", "%d parts" % len(parts))
        try:
            h, p, s = jl(b64u(parts[0])), jl(b64u(parts[1])), b64u(parts[2])
            hh = next((J(v) for k, v in sibs.items() if k.endswith("-jose-protected-headers.json")), None)
            chk(res, "header", "decoded JOSE header equals the Protected Headers tab", "pass" if h == hh else "fail", json.dumps(h))
            vc = next((J(v) for k, v in sibs.items() if k.endswith("-jose-application-vc.json")), None)
            chk(res, "payload", "decoded payload equals the application/vc tab", "pass" if p == vc else "fail")
            chk(res, "sigsize", "signature is 64 octets (alg %s)" % h.get("alg"), "pass" if len(s) == 64 and h.get("alg") == "ES256" else "fail", "%d octets" % len(s))
            model_checks(res, "payload:", p, "decoded JWS payload")
        except Exception as ex:
            chk(res, "decode", "decodes", "fail", str(ex)[:120])
        chk(res, "signature", "JWS signature verifies", "unverifiable", "the source prints the kid but no key")
        return res
    if f.endswith(".hex"):
        try:
            raw = bytes.fromhex(t)
            tag = cbor2.loads(raw)
            ok = isinstance(tag, cbor2.CBORTag) and tag.tag == 18 and isinstance(tag.value, (list, tuple)) and len(tag.value) == 4
            chk(res, "shape", "CBOR tag 18 wrapping a 4-element array (COSE_Sign1)", "pass" if ok else "fail")
            prot, unprot, payload, sig = tag.value
            ph = cbor2.loads(prot)
            chk(res, "protected", "protected header is a bstr holding a map: %s" % ph, "pass" if isinstance(ph, dict) else "fail")
            p = jl(payload)
            vc = next((J(v) for k, v in sibs.items() if k.endswith("-cose-application-vc.json")), None)
            chk(res, "payload", "payload bstr is the JSON of the application/vc tab (value equality)", "pass" if p == vc else "fail")
            chk(res, "sigsize", "signature is 64 octets", "pass" if len(sig) == 64 else "fail", "%d octets" % len(sig))
            model_checks(res, "payload:", p, "decoded COSE payload")
        except Exception as ex:
            chk(res, "decode", "decodes", "fail", str(ex)[:120])
        chk(res, "signature", "COSE signature verifies", "unverifiable", "no key in the source")
        return res
    if f.endswith(".sd-jwt"):
        return sdjwt_checks(res, f, t, sibs)
    if f.endswith(".txt") and "-sd-jwt-disclosures-" in f:
        return res  # checked from the sd-jwt side
    return res


def sdjwt_checks(res, f, t, sibs):
    seg = t.split("~")
    jwt, discs, tail = seg[0], seg[1:-1], seg[-1]
    missing_tilde = False
    if tail != "":
        try:
            if isinstance(json.loads(b64u(tail).decode("utf-8")), list):
                missing_tilde, discs, tail = True, discs + [tail], ""
        except Exception:
            pass
    chk(res, "shape", "SD-JWT: JWT, then every disclosure followed by ~ (%d disclosures, KB-JWT %s)" % (len(discs), "absent" if tail == "" else "present"), "pass" if tail == "" and not missing_tilde and jwt.count(".") == 2 else "fail", "the last element decodes as a disclosure and no ~ follows it" if missing_tilde else "")
    parts = jwt.split(".")
    try:
        h, p = jl(b64u(parts[0])), jl(b64u(parts[1]))
    except Exception as ex:
        chk(res, "decode", "decodes the Issuer-signed JWT", "fail", str(ex)[:100])
        return res
    chk(res, "header", "decoded header: %s" % json.dumps(h), "pass")
    dd = {}
    for d in discs:
        arr = json.loads(b64u(d).decode("utf-8"))
        dd[base64.urlsafe_b64encode(hashlib.sha256(d.encode("ascii")).digest()).decode().rstrip("=")] = arr
    alg = p.get("_sd_alg", "sha-256")
    chk(res, "sd_alg", "_sd_alg %s (digests computed with sha-256)" % alg, "pass" if alg == "sha-256" else "fail")
    # all digests referenced
    refs = []

    def walk(o):
        if isinstance(o, dict):
            for k, v in o.items():
                if k == "_sd" and isinstance(v, list):
                    refs.extend(v)
                walk(v)
        elif isinstance(o, list):
            for v in o:
                walk(v)
    walk(p)
    unused = [k for k in dd if k not in refs]
    chk(res, "digests", "every disclosure digest occurs in an _sd array (%d disclosures, %d _sd digests, %d decoys)" % (len(dd), len(refs), len(refs) - len(dd)), "pass" if not unused else "fail", "unreferenced: %s" % unused)

    def apply(o):
        if isinstance(o, dict):
            r = {}
            for k, v in o.items():
                if k == "_sd":
                    continue
                r[k] = apply(v)
            for h_ in o.get("_sd", []):
                if h_ in dd:
                    arr = dd[h_]
                    if len(arr) == 3:
                        r[arr[1]] = apply(arr[2])
            return r
        if isinstance(o, list):
            return [apply(v) for v in o]
        return o
    rec = apply(p)
    rec.pop("_sd_alg", None)
    num = re.match(r"^ex(\d+)-", f)
    cred = next((J(v) for k, v in sibs.items() if k.endswith("-credential.json") and not k.endswith("-application-vc.json")), None)
    # decoded tabs
    pref = f[: -len("-encoded.sd-jwt")] if f.endswith("-encoded.sd-jwt") else None
    d1 = sibs.get(pref + "-decoded-1.json") if pref else None
    d2 = sibs.get(pref + "-decoded-2.json") if pref else None
    if d1 is not None:
        chk(res, "decoded-header", "Decoded tab, header equals the decoded JWT header", "pass" if json.loads(d1.replace("\u00a0", " ")) == h else "fail")
    if d2 is not None:
        chk(res, "decoded-payload", "Decoded tab, payload equals the decoded JWT payload", "pass" if json.loads(d2.replace("\u00a0", " ")) == p else "fail")
    # disclosure displays
    disp = sorted(k for k in sibs if pref and re.match(re.escape(pref + "-disclosures-") + r"\d+\.txt$", k))
    bad = []
    seen = []
    for k in disp:
        tx = sibs[k]
        mh = re.search(r"SHA-256 Hash:\s*(\S+)", tx)
        md = re.search(r"Disclosure\(s\):\s*(\S+)", tx)
        mc = re.search(r"Contents:\s*(\[.*\])", tx, re.S)
        if not (mh and md and mc):
            bad.append(k + ": unparsable")
            continue
        comp = base64.urlsafe_b64encode(hashlib.sha256(md.group(1).encode("ascii")).digest()).decode().rstrip("=")
        seen.append(md.group(1))
        if comp != mh.group(1):
            bad.append(k + ": printed hash != sha-256 of printed disclosure")
        if json.loads(re.sub(r"\s+", " ", mc.group(1).replace("\u00a0", " "))) != json.loads(b64u(md.group(1))):
            bad.append(k + ": Contents != decoded disclosure")
    if disp:
        chk(res, "disclosure-display", "%d Issuer Disclosures displays: printed hash is sha-256 of the printed disclosure, Contents equals its decoding" % len(disp), "pass" if not bad else "fail", "; ".join(bad))
    if disp:
        chk(res, "disclosure-set", "displayed disclosures are exactly the ones in the compact form", "pass" if sorted(seen) == sorted(discs) else "fail", "%d displayed, %d in compact form" % (len(seen), len(discs)))
    # reconstruct
    body = {k: v for k, v in rec.items() if k not in ("iat", "exp")}
    if cred is not None:
        chk(res, "reconstruct", "payload with disclosures applied (minus iat, exp, _sd_alg) equals the Credential tab (value equality)", "pass" if body == cred else "fail", "" if body == cred else "differs in: " + ", ".join(sorted(k for k in set(body) | set(cred) if body.get(k) != cred.get(k))))
    model_checks(res, "reconstructed:", rec, "SD-JWT with disclosures applied")
    chk(res, "signature", "Issuer signature verifies", "unverifiable", "no key in the source")
    return res


def examples(check_only=False):
    files = sorted(f for f in os.listdir(EX) if re.match(r"ex\d\d-", f))
    byex = {}
    for f in files:
        byex.setdefault(f[2:4], {})[f] = read_fx(f)
    results = {}
    for f in files:
        sibs = byex[f[2:4]]
        results[f] = analyze_file(f, sibs[f], sibs)
    n_checks = sum(len(v) for v in results.values())
    tally = {}
    for v in results.values():
        for c in v:
            tally[c["result"]] = tally.get(c["result"], 0) + 1
    out = {"fixtures": len(files), "checks": n_checks, "tally": dict(sorted(tally.items())), "results": results}
    path = os.path.join(EX, "results.derived.json")
    txt = json.dumps(out, indent=1, ensure_ascii=False, sort_keys=True) + "\n"
    if check_only:
        have = open(path, encoding="utf-8").read() if os.path.exists(path) else ""
        diff = 0 if have == txt else 1
        print("examples --check: EXAMINED %d fixtures, %d checks (%s); FOUND %s" % (len(files), n_checks, tally, "no difference from results.derived.json" if not diff else "a DIFFERENCE from results.derived.json"))
        return diff
    open(path, "w", encoding="utf-8").write(txt)
    print("examples: EXAMINED %d fixtures, %d checks %s; wrote results.derived.json" % (len(files), n_checks, tally))
    return 0


def main(argv):
    if not argv:
        print(__doc__)
        return 2
    cmd = argv[0]
    if cmd == "schema-tests":
        return 1 if run_schema_tests() else 0
    if cmd == "metaschema":
        return 1 if run_metaschema() else 0
    if cmd == "examples":
        return examples("--check" in argv)
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

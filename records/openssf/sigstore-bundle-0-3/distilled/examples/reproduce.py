#!/usr/bin/env python3
"""reproduce.py -- re-derive everything in this directory from the pinned source.

    python3 -I reproduce.py [--write] [--cross]

Needs .cache/sigstore-bundle-0-3.{bin,txt} and .cache/sigstore-bundle-0-3.include/ (bin/fetch-source),
the `openssl` command line tool, and nothing else (stdlib only). --cross also runs the schema
checker's jsonschema/protobuf cross-runs if those are importable. --write rewrites the fixtures'
index, fixtures.derived.json and the *.expected.derived.json files; without it they are compared.

What it does, each counted in EXAMINED:
 1 sha256 of the five pinned inputs against render-source.py's table;
 2 re-runs render-source.py into a scratch dir and compares the rendering byte for byte with
   .cache/sigstore-bundle-0-3.txt;
 3 cuts every fenced code block of bundle.md by line (two independent extractors: a line scanner and
   a whole-file regex must agree), checks each fixture file is those bytes, records which parse as
   JSON as they stand, which parse wrapped in braces, and why not (source defects SD-S-n);
 4 maps each fixture to rendering lines (md line + the part offset, verified line by line);
 5 for the two complete example bundles: parse, decode every base64 field, decode the DSSE payload
   and compare with the printed attestation, decode canonicalizedBody and check it binds the same
   digest/signature/certificate, parse the X.509 certificates (own DER reader) and test
   integratedTime and the RFC 3161 genTime against notBefore..notAfter, list the Fulcio OID
   extensions, verify the signatures with `openssl`, check the checkpoint text against
   inclusionProof, verify the Merkle inclusion proof (RFC 9162 2.1.3.2) and recompute the intoto
   body's content.hash; the checks that carry a negative_control are also run on a deliberately
   damaged copy, which must fail (8 of them, listed in the *.expected.derived.json files);
 6 runs the derived schema over both bundles and the whole case/mutation run.
A result is pass, FAIL, or NOT VERIFIABLE (the source does not hold what the check needs).
"""
import base64, datetime, hashlib, importlib.util, json, os, re, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
DIST = os.path.dirname(HERE)
ROOT = os.path.normpath(os.path.join(DIST, "..", "..", "..", ".."))
CACHE = os.path.join(ROOT, ".cache")
BIN = os.path.join(CACHE, "sigstore-bundle-0-3.bin")
INC = os.path.join(CACHE, "sigstore-bundle-0-3.include")
TXT = os.path.join(CACHE, "sigstore-bundle-0-3.txt")
WRITE = "--write" in sys.argv
FAILS, EXAMINED = [], [0]


def check(cond, what):
    EXAMINED[0] += 1
    if not cond:
        FAILS.append(what); print("FAIL:", what)
    return cond


def sha(b): return hashlib.sha256(b).hexdigest()


# ---------------------------------------------------------------- 1, 2 inputs and rendering
rs_path = os.path.join(DIST, "render-source.py")
spec = importlib.util.spec_from_file_location("render_source", rs_path)
rs = importlib.util.module_from_spec(spec); spec.loader.exec_module(rs)
for name, path in (("sigstore_bundle.proto", BIN), ("envelope.proto", f"{INC}/envelope.proto"),
                   ("sigstore_common.proto", f"{INC}/sigstore_common.proto"), ("sigstore_rekor.proto", f"{INC}/sigstore_rekor.proto"),
                   ("bundle.md", f"{INC}/bundle.md")):
    check(sha(open(path, "rb").read()) == rs.SHA256[name], f"sha256 of {name}")
with tempfile.TemporaryDirectory() as td:
    out = os.path.join(td, "r.txt")
    subprocess.run([sys.executable, "-I", rs_path, BIN, INC, out], check=True)
    check(open(out, "rb").read() == open(TXT, "rb").read(), "render-source.py output == .cache/sigstore-bundle-0-3.txt byte for byte")
MD = open(f"{INC}/bundle.md", "rb").read().decode("utf-8")
MDL = MD.split("\n")
TXTL = open(TXT, encoding="utf-8").read().split("\n")

# ---------------------------------------------------------------- 3 fixtures
fence = [i + 1 for i, l in enumerate(MDL) if l.startswith("```")]
blocks_a = [(fence[i] + 1, fence[i + 1] - 1) for i in range(0, len(fence), 2)]
blocks_b = []
for m in re.finditer(r"^```json\n(.*?)^```$", MD, re.S | re.M):
    a = MD.count("\n", 0, m.start(1)) + 1
    blocks_b.append((a, a + m.group(1).count("\n") - 1))
check(blocks_a == blocks_b and len(blocks_a) == 9, f"two extractors agree on 9 fenced blocks: {blocks_a}")
NAMES = ["verification-material-certificate.verbatim.txt", "verification-material-public-key.verbatim.txt",
         "verification-material-tlog-entries.verbatim.txt", "verification-material-timestamp.verbatim.txt",
         "content-message-signature.verbatim.txt", "content-dsse.verbatim.txt",
         "bundle-message-signature.verbatim.json", "bundle-dsse.verbatim.json", "embedded-attestation.verbatim.json"]
SECTION = ["5.1.1.1.1 X.509 certificate", "5.1.1.1.2 Public Key Identifier", "5.1.1.2 Transparency Log Entries", "5.1.1.3 Timestamp",
           "5.1.2.1 Message Signature", "5.1.2.2 DSSE", "5.1.3.1 Message Signature Bundle", "5.1.3.2 DSSE Bundle",
           "5.1.3.2 DSSE Bundle (embedded attestation)"]
DEFECT = {  # fixture -> (id, line in bundle.md, what)
    2: ("SD-S-1", [71, 95], "trailing comma after \"keyId\": \"<KEY_ID>\", (L71) and after the entry object (L95): not JSON"),
    3: ("SD-S-2", [110], "trailing comma after the timestamp object (L110): not JSON"),
    5: ("SD-S-3", [142, 143], "`\"dsseEnvelope\": { {` opens two objects, the second without a key (L142-143): not JSON even wrapped"),
}
OFFSET = None
fx = []
for k, (a, b) in enumerate(blocks_a):
    data = ("\n".join(MDL[a - 1:b]) + "\n").encode("utf-8")
    p = os.path.join(HERE, NAMES[k])
    if WRITE: open(p, "wb").write(data)
    check(os.path.exists(p) and open(p, "rb").read() == data, f"{NAMES[k]} is bundle.md L{a}-{b} byte for byte")
    t = data.decode()
    def attempt(s):
        try: json.loads(s); return None
        except ValueError as e: return str(e)
    asis, wrapped = attempt(t), attempt("{" + t + "}")
    check(NAMES[k].endswith(".json") == (asis is None), f"{NAMES[k]}: extension .json iff it parses as it stands")
    fx.append({"fixture": NAMES[k], "section": SECTION[k], "bundle_md_lines": f"{a}-{b}", "sha256": sha(data),
               "parses_as_is": asis is None, "as_is_error": asis,
               "parses_wrapped_in_braces": wrapped is None, "wrapped_error": wrapped})
# rendering lines: find the one offset at which every non-heading md line equals the rendering line
cands = [o for o in range(0, len(TXTL) - len(MDL) + 1)
         if all(TXTL[i + o] == MDL[i] for i in (37, 38, 164, 165, 210, 270, 316))]
check(len(cands) == 1, f"one part offset places bundle.md in the rendering (candidates {cands})")
OFFSET = cands[0]
for k, f in enumerate(fx):
    a, b = blocks_a[k]
    ok = all(TXTL[i + OFFSET - 1] == MDL[i - 1] for i in range(a, b + 1))
    check(ok, f"{f['fixture']}: rendering lines {a+OFFSET}-{b+OFFSET} equal bundle.md lines {a}-{b} line by line")
    f["rendering_lines"] = f"{a+OFFSET}-{b+OFFSET}"
    if k in DEFECT:
        f["source_defect"] = {"id": DEFECT[k][0], "bundle_md_lines": DEFECT[k][1], "rendering_lines": [x + OFFSET for x in DEFECT[k][1]], "what": DEFECT[k][2]}
    f["first_line"] = {"source_lines": str(a + OFFSET), "quote": TXTL[a + OFFSET - 1].strip()}
    f["last_line"] = {"source_lines": str(b + OFFSET), "quote": TXTL[b + OFFSET - 1].strip()}
# the three JSON-valid blocks are exactly the three complete documents
check([f["parses_as_is"] for f in fx] == [False] * 6 + [True] * 3, "exactly blocks 7-9 parse as JSON as they stand")
check(fx[0]["parses_wrapped_in_braces"] and fx[1]["parses_wrapped_in_braces"] and fx[4]["parses_wrapped_in_braces"], "fragments 1, 2, 5 parse once wrapped in braces")
check(not fx[2]["parses_wrapped_in_braces"] and not fx[3]["parses_wrapped_in_braces"] and not fx[5]["parses_wrapped_in_braces"], "blocks 3, 4, 6 do not parse even wrapped (SD-S-1..3)")


# ---------------------------------------------------------------- DER, X.509, RFC 3161
def tlv(b, i):
    tag = b[i]; n = b[i + 1]; j = i + 2
    if n & 0x80:
        c = n & 0x7F; n = int.from_bytes(b[j:j + c], "big"); j += c
    return tag, j, j + n


def kids(b, s, e):
    out = []
    while s < e:
        t, cs, ce = tlv(b, s); out.append((t, cs, ce, s)); s = ce
    return out


def oid(b, s, e):
    v = b[s]; parts = [v // 40, v % 40]; x = 0
    for c in b[s + 1:e]:
        x = (x << 7) | (c & 0x7F)
        if not c & 0x80: parts.append(x); x = 0
    return ".".join(map(str, parts))


def gtime(b, s, e, tag):
    t = b[s:e].decode()
    if tag == 0x17: t = ("20" if int(t[:2]) < 50 else "19") + t
    return datetime.datetime.strptime(t[:14], "%Y%m%d%H%M%S").replace(tzinfo=datetime.timezone.utc)


def parse_cert(der):
    _, cs, ce = tlv(der, 0)
    tbs = kids(der, cs, ce)[0]
    f = kids(der, tbs[1], tbs[2])
    i = 1 if f[0][0] == 0xA0 else 0
    val = kids(der, f[i + 3][1], f[i + 3][2])
    nb, na = gtime(der, val[0][1], val[0][2], val[0][0]), gtime(der, val[1][1], val[1][2], val[1][0])
    spki = der[f[i + 5 + 1][3]:f[i + 5 + 1][2]] if False else der[f[i + 5][3]:f[i + 5][2]]
    exts = []
    for t, s, e, st in f[i + 6:]:
        if t == 0xA3:
            for _, es, ee, _ in kids(der, kids(der, s, e)[0][1], kids(der, s, e)[0][2]):
                k = kids(der, es, ee)
                crit = len(k) == 3 and der[k[1][1]] != 0
                exts.append({"oid": oid(der, k[0][1], k[0][2]), "critical": crit})
    kinds = kids(der, f[i + 5][1], f[i + 5][2])
    curve = oid(der, kids(der, kinds[0][1], kinds[0][2])[1][1], kids(der, kinds[0][1], kinds[0][2])[1][2])
    return {"not_before": nb, "not_after": na, "spki": spki, "extensions": exts, "curve_oid": curve}


def parse_tst(der):
    """RFC 3161 TimeStampResp -> (hash alg oid, hashedMessage, genTime, TSTInfo bytes, messageDigest attr, n certs)."""
    _, cs, ce = tlv(der, 0)
    top = kids(der, cs, ce)                       # status, timeStampToken
    ci = kids(der, top[1][1], top[1][2])          # contentType, [0] SignedData
    sd = kids(der, kids(der, ci[1][1], ci[1][2])[0][1], kids(der, ci[1][1], ci[1][2])[0][2])
    enc = kids(der, sd[2][1], sd[2][2])           # eContentType, [0] eContent
    octs = kids(der, enc[1][1], enc[1][2])[0]
    info = der[octs[1]:octs[2]]
    tk = kids(info, 0, len(info))
    tk = kids(info, tlv(info, 0)[1], tlv(info, 0)[2])
    mi = kids(info, tk[2][1], tk[2][2])
    alg = oid(info, kids(info, mi[0][1], mi[0][2])[0][1], kids(info, mi[0][1], mi[0][2])[0][2])
    gt = [x for x in tk if x[0] == 0x18][0]
    ncert = sum(len(kids(der, x[1], x[2])) for x in sd if x[0] == 0xA0)
    si = [x for x in sd if x[0] == 0x31][-1]
    signer = kids(der, kids(der, si[1], si[2])[0][1], kids(der, si[1], si[2])[0][2])
    md = None
    for x in signer:
        if x[0] == 0xA0:
            for a in kids(der, x[1], x[2]):
                ak = kids(der, a[1], a[2])
                if oid(der, ak[0][1], ak[0][2]) == "1.2.840.113549.1.9.4":
                    v = kids(der, ak[1][1], ak[1][2])[0]; md = der[v[1]:v[2]]
    return {"alg": alg, "hashed_message": info[mi[1][1]:mi[1][2]], "gen_time": gtime(info, gt[1], gt[2], 0x18), "tstinfo": info,
            "signed_attr_message_digest": md, "embedded_certificates": ncert}


def pem_spki(spki): return b"-----BEGIN PUBLIC KEY-----\n" + base64.encodebytes(spki) + b"-----END PUBLIC KEY-----\n"


def ecdsa_verify(spki, msg, sig, prehashed):
    with tempfile.TemporaryDirectory() as td:
        k, m, s = (os.path.join(td, x) for x in ("k.pem", "m", "s"))
        open(k, "wb").write(pem_spki(spki)); open(m, "wb").write(msg); open(s, "wb").write(sig)
        cmd = (["openssl", "pkeyutl", "-verify", "-pubin", "-inkey", k, "-in", m, "-sigfile", s] if prehashed
               else ["openssl", "dgst", "-sha256", "-verify", k, "-signature", s, m])
        r = subprocess.run(cmd, capture_output=True, text=True)
        return r.returncode == 0 and "Verified" in r.stdout


def b64(s):
    std, url = set("+/"), set("-_")
    alpha = "standard" if any(c in std for c in s) else "url-safe" if any(c in url for c in s) else "either"
    t = s.rstrip("=")
    d = base64.b64decode(t.replace("-", "+").replace("_", "/") + "=" * (-len(t) % 4), validate=True)
    return d, alpha, s.endswith("=")


def H(x): return hashlib.sha256(x).digest()


def merkle_ok(index, size, leaf, path, root):
    """RFC 9162 section 2.1.3.2."""
    if index >= size: return False
    fn, sn, r = index, size - 1, leaf
    for p in path:
        if sn == 0: return False
        if fn & 1 or fn == sn:
            r = H(b"\x01" + p + r)
            if not fn & 1:
                while not fn & 1 and fn != 0: fn >>= 1; sn >>= 1
        else:
            r = H(b"\x01" + r + p)
        fn >>= 1; sn >>= 1
    return sn == 0 and r == root


def pae(t, p): return b"DSSEv1 %d %s %d " % (len(t.encode()), t.encode(), len(p)) + p


FULCIO = "1.3.6.1.4.1.57264.1."


def analyse(name, kind):
    b = json.load(open(os.path.join(HERE, name)))
    R = []

    def rec(check_name, result, detail, ctl=None):
        EXAMINED[0] += 1
        R.append({"check": check_name, "result": result, "detail": detail, **({"negative_control": ctl} if ctl else {})})
        if result == "FAIL": FAILS.append(f"{name}: {check_name}: {detail}"); print("FAIL:", name, check_name, detail)

    rec("parse as JSON", "pass", "json.loads")
    # decode every base64 field
    dec = []
    def walk(n, p):
        if isinstance(n, dict):
            for k, v in n.items(): walk(v, f"{p}/{k}")
        elif isinstance(n, list):
            for i, v in enumerate(n): walk(v, f"{p}/{i}")
        elif isinstance(n, str) and p.rsplit("/", 1)[-1] in ("rawBytes", "keyId", "signedEntryTimestamp", "rootHash", "canonicalizedBody", "signedTimestamp", "digest", "signature", "sig", "payload") or (isinstance(n, str) and re.search(r"/hashes/\d+$", p)):
            d, alpha, padded = b64(n); dec.append({"path": p, "bytes": len(d), "alphabet": alpha, "padded": padded})
    walk(b, "")
    rec("decode every base64 field", "pass", f"{len(dec)} fields decoded; alphabets {sorted({d['alphabet'] for d in dec})}; padded {sum(d['padded'] for d in dec)}, unpadded {sum(not d['padded'] for d in dec)}")
    vm = b["verificationMaterial"]; te = vm["tlogEntries"][0]
    cert_b64 = vm["certificate"]["rawBytes"] if "certificate" in vm else vm["x509CertificateChain"]["certificates"][0]["rawBytes"]
    der = base64.b64decode(cert_b64); C = parse_cert(der)
    body_raw = base64.b64decode(te["canonicalizedBody"]); body = json.loads(body_raw)
    rec("canonicalizedBody is compact JSON, apiVersion/kind match kindVersion", "pass" if (body["kind"] == te["kindVersion"]["kind"] and body["apiVersion"] == te["kindVersion"]["version"] and body_raw == json.dumps(body, separators=(",", ":"), ensure_ascii=False).encode()) else "FAIL",
        f"kind {body['kind']} apiVersion {body['apiVersion']}; re-serialised compactly in the same key order: {body_raw == json.dumps(body, separators=(',', ':'), ensure_ascii=False).encode()}")
    # certificate facts
    rec("X.509 leaf parsed (own DER reader)", "pass", {"not_before": C["not_before"].isoformat(), "not_after": C["not_after"].isoformat(), "curve_oid": C["curve_oid"], "extension_oids": [e["oid"] for e in C["extensions"]]})
    ful = sorted(e["oid"][len(FULCIO):] for e in C["extensions"] if e["oid"].startswith(FULCIO))
    rec("Fulcio OID extensions (1.3.6.1.4.1.57264.1.N) present", "pass" if ful else "FAIL", f"arcs {ful}; the source only points at the Fulcio oid-info page, it lists none")
    it = datetime.datetime.fromtimestamp(int(te["integratedTime"]), datetime.timezone.utc)
    inside = C["not_before"] <= it <= C["not_after"]
    rec("integratedTime inside notBefore..notAfter", "pass" if inside else "FAIL", f"integratedTime {it.isoformat()}; window {C['not_before'].isoformat()} .. {C['not_after'].isoformat()}",
        ctl=("pass" if not (C["not_before"] <= it + datetime.timedelta(days=1) <= C["not_after"]) else "FAIL: a day later is also inside"))
    # content signature
    if kind == "ms":
        ms = b["messageSignature"]; dig, _, _ = b64(ms["messageDigest"]["digest"]); sig, _, _ = b64(ms["signature"])
        hx = body["spec"]["data"]["hash"]
        rec("messageDigest equals the hashedrekord body hash", "pass" if (hx["algorithm"] == "sha256" and hx["value"] == dig.hex() and ms["messageDigest"]["algorithm"] == "SHA2_256") else "FAIL", f"{hx['algorithm']}:{hx['value']}")
        pem = base64.b64decode(body["spec"]["signature"]["publicKey"]["content"])
        pder = base64.b64decode(b"".join(pem.split(b"\n")[1:-2]))
        rec("hashedrekord body signature equals Bundle signature (R-0067)", "pass" if base64.b64decode(body["spec"]["signature"]["content"]) == sig else "FAIL", "byte-equal")
        rec("hashedrekord body publicKey is the bundle certificate", "pass" if pder == der else "FAIL", "PEM body DER == certificate.rawBytes")
        ok = ecdsa_verify(C["spki"], dig, sig, True)
        bad = ecdsa_verify(C["spki"], bytes([dig[0] ^ 1]) + dig[1:], sig, True)
        rec("ECDSA(P-256) signature over messageDigest, cert key, via openssl", "pass" if ok else "FAIL", "analysis only: R-0038 forbids a CLIENT from verifying with messageDigest (it is for identification); this shows the signature was made over exactly that digest, the artifact being absent", ctl="pass (flipped digest bit rejected)" if not bad else "FAIL")
        rec("messageDigest vs the artifact", "NOT VERIFIABLE", "the artifact (sigstore-java-1.0.0.jar, a third-party file) is not in the source or the repository")
    else:
        d = b["dsseEnvelope"]; payload, _, _ = b64(d["payload"]); sig, _, _ = b64(d["signatures"][0]["sig"])
        att = open(os.path.join(HERE, "embedded-attestation.verbatim.json"), "rb").read()
        same = payload == att
        rec("decoded DSSE payload vs the printed 'embedded attestation' block (L271-317)", "pass" if same else "FAIL",
            "byte-identical (the block cut by line, with its final newline)" if same else f"differs; payload {len(payload)} bytes, block {len(att)} bytes",
            ctl="pass (stripping the final newline makes them differ)" if payload != att[:-1] else "FAIL")
        spec_ = body["spec"]["content"]
        rec("intoto body payloadHash == SHA-256(decoded payload)", "pass" if spec_["payloadHash"]["value"] == sha(payload) else "FAIL", spec_["payloadHash"]["value"])
        env = spec_["envelope"]
        rec("intoto body envelope.payload is base64 of the bundle's base64 payload (double encoding)", "pass" if base64.b64decode(env["payload"]) == d["payload"].encode() else "FAIL", "body payload decodes to the bundle payload text, not to the statement")
        rec("intoto body signature is base64 of the bundle's base64 sig; publicKey is the bundle certificate (R-0067)", "pass" if (base64.b64decode(env["signatures"][0]["sig"]) == d["signatures"][0]["sig"].encode() and base64.b64decode(base64.b64decode(env["signatures"][0]["publicKey"]).split(b"-----")[2].replace(b"\n", b"")) == der) else "FAIL", "double-encoded sig; PEM body == chain[0]")
        # content.hash (verify pass, library#151; pass 1 tried 8 serialisations, none of them this one): SHA-256
        # of the canonical JSON (keys sorted, no whitespace) of the bundle's envelope with base64 payload and sig as
        # the bundle prints them, the body's publicKey (decoded once: the certificate PEM) in the signature, and keyid
        # left out because it is empty. The source states no such scheme; it was found by trying serialisations.
        pem = base64.b64decode(env["signatures"][0]["publicKey"]).decode()
        def env_hash(keep_empty_keyid):
            sg = {"sig": d["signatures"][0]["sig"], "publicKey": pem}
            if d["signatures"][0].get("keyid") or keep_empty_keyid: sg["keyid"] = d["signatures"][0].get("keyid", "")
            o = {"payloadType": d["payloadType"], "payload": d["payload"], "signatures": [sg]}
            return sha(json.dumps(o, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode())
        got, ctl_h = env_hash(False), env_hash(True)
        rec("intoto body content.hash reproduced", "pass" if got == spec_["hash"]["value"] else "FAIL",
            f"{spec_['hash']['value']} = SHA-256 of the sorted, compact JSON of {{payload, payloadType, signatures: [{{publicKey: the certificate PEM, sig}}]}}, "
            "payload and sig in the bundle's base64, keyid left out (it is empty). The source does not state this scheme (Rekor's, outside it); found by trying serialisations.",
            ctl="pass (keeping the empty keyid gives another hash)" if ctl_h != spec_["hash"]["value"] else "FAIL")
        pt = d["payloadType"]
        ok = ecdsa_verify(C["spki"], pae(pt, payload), sig, False)
        bad = ecdsa_verify(C["spki"], pae(pt + "x", payload), sig, False)
        rec("ECDSA(P-256, SHA-256) signature over PAE(payloadType, payload), chain[0] key, via openssl", "pass" if ok else "FAIL", "PAE = DSSEv1 SP LEN(type) SP type SP LEN(payload) SP payload (envelope.proto comment, L237-245)", ctl="pass (altered payloadType rejected)" if not bad else "FAIL")
        T = parse_tst(base64.b64decode(vm["timestampVerificationData"]["rfc3161Timestamps"][0]["signedTimestamp"]))
        rec("RFC 3161 messageImprint == SHA-256(DSSE signature) (R-0003)", "pass" if T["hashed_message"] == H(sig) and T["alg"] == "2.16.840.1.101.3.4.2.1" else "FAIL", f"imprint {T['hashed_message'].hex()}")
        rec("RFC 3161 genTime inside certificate validity", "pass" if C["not_before"] <= T["gen_time"] <= C["not_after"] else "FAIL", f"genTime {T['gen_time'].isoformat()} == notBefore {C['not_before'].isoformat()}: {T['gen_time'] == C['not_before']} (boundary, inclusive)")
        rec("RFC 3161 signedAttrs messageDigest == SHA-256(TSTInfo)", "pass" if T["signed_attr_message_digest"] == H(T["tstinfo"]) else "FAIL", "consistent; the TSA signature itself is not checked")
        rec("RFC 3161 TSA signature", "NOT VERIFIABLE", f"the timestamp carries {T['embedded_certificates']} certificates and the source holds no TSA certificate")
        rec("chain: order, leaf first, no root (R-0005..R-0007)", "pass" if len(vm["x509CertificateChain"]["certificates"]) == 1 else "FAIL", "one certificate, the leaf; its issuer is not in the bundle")
    # checkpoint and merkle
    ip = te["inclusionProof"]; cp = ip["checkpoint"]["envelope"]
    head, _, sigs = cp.partition("\n\n")
    lines = head.split("\n"); root = base64.b64decode(ip["rootHash"])
    rec("checkpoint tree size and root hash equal inclusionProof", "pass" if (lines[1] == ip["treeSize"] and base64.b64decode(lines[2]) == root) else "FAIL", f"origin {lines[0]!r}; size {lines[1]}; root {lines[2]}; extra lines {lines[3:]}")
    sigline = [l for l in sigs.split("\n") if l.startswith("— ")][0]
    kb = base64.b64decode(sigline.split(" ")[2])
    keyid = base64.b64decode(te["logId"]["keyId"])
    rec("checkpoint signature key hint (first 4 bytes) vs logId.keyId", "pass" if kb[:4] == keyid[:4] else "FAIL", f"hint {kb[:4].hex()} == keyId[:4] {keyid[:4].hex()} (an observation; the source does not say how they relate)")
    rec("checkpoint signature", "NOT VERIFIABLE", "the log's public key is not in the source")
    rec("signedEntryTimestamp (inclusion promise)", "NOT VERIFIABLE", "the log's public key is not in the source; canonicalizedBody + logIndex + logId + integratedTime are present for rebuilding the payload")
    leaf = H(b"\x00" + body_raw); path = [base64.b64decode(x) for x in ip["hashes"]]
    ok = merkle_ok(int(ip["logIndex"]), int(ip["treeSize"]), leaf, path, root)
    bad = merkle_ok(int(ip["logIndex"]), int(ip["treeSize"]), H(b"\x00" + body_raw + b"x"), path, root)
    rec("Merkle inclusion proof, leaf = SHA-256(0x00 || canonicalizedBody) (RFC 9162 2.1.3.2)", "pass" if ok else "FAIL", f"index {ip['logIndex']} size {ip['treeSize']} {len(path)} hashes, each {sorted({len(x) for x in path}) or '-'} bytes",
        ctl="pass (altered leaf rejected)" if not bad else "FAIL")
    rec("tlog entry logIndex vs inclusionProof.logIndex", "pass", f"{te['logIndex']} vs {ip['logIndex']}: different numbers (global index vs tree index); the source defines both without relating them")
    return {"fixture": name, "base64_fields": dec, "checks": R}


results = {"message-signature": analyse("bundle-message-signature.verbatim.json", "ms"), "dsse": analyse("bundle-dsse.verbatim.json", "dsse")}

# ---------------------------------------------------------------- 6 schema
sch = importlib.util.spec_from_file_location("chk", os.path.join(DIST, "schema", "check-schemas.derived.py"))
chk = importlib.util.module_from_spec(sch); sch.loader.exec_module(chk)
for k, nm in (("message-signature", "ms"), ("dsse", "dsse")):
    v = chk.V(chk.SCHEMA)
    for d in ("Bundle", "BundleV03"):
        e = v.errs({"$ref": "#/$defs/" + d}, json.load(open(os.path.join(HERE, results[k]["fixture"]))))
        check(not e, f"{results[k]['fixture']} is accepted by derived schema {d}: {e[:2]}")
        results[k]["checks"].append({"check": f"derived schema {d} accepts the bundle", "result": "pass" if not e else "FAIL", "detail": ""})
bad = subprocess.run([sys.executable, "-I", os.path.join(DIST, "schema", "check-schemas.derived.py")] + (["--cross"] if "--cross" in sys.argv else []), capture_output=True, text=True)
print(bad.stdout.strip())
check(bad.returncode == 0, "schema checker (cases + mutation) exits 0")

# ---------------------------------------------------------------- write / compare derived files
def dump(o): return json.dumps(o, indent=1, ensure_ascii=False, default=str) + "\n"


outputs = {"fixtures.derived.json": {"kind": "derived-fixture-index", "note": "DERIVED - written by this library. One entry per fenced block of bundle.md (sha256 .cache/sigstore-bundle-0-3.include/bundle.md = 8d11270...), cut by line. first_line/last_line carry source_lines+quote into the rendering for bin/check-quotes.", "part_offset_bundle_md_to_rendering": OFFSET, "fixtures": fx}}
for k in results:
    outputs[f"{k}-bundle.expected.derived.json"] = {"kind": "derived-expected-results", "note": "DERIVED - written by this library. Results of reproduce.py on the verbatim fixture. result: pass | FAIL | NOT VERIFIABLE (the source does not hold what the check needs). negative_control, where a check has one: the same check on a damaged copy, which must fail.", **results[k]}
for fn, o in outputs.items():
    p = os.path.join(HERE, fn)
    if WRITE: open(p, "w").write(dump(o))
    check(os.path.exists(p) and open(p).read() == dump(o), f"{fn} equals the recomputed result")
for k in results:
    for c in results[k]["checks"]:
        if c.get("negative_control", "pass").startswith("FAIL"): check(False, f"{k}: negative control for {c['check']}")
print(f"EXAMINED {EXAMINED[0]} checks; {len(FAILS)} failed")
sys.exit(1 if FAILS else 0)

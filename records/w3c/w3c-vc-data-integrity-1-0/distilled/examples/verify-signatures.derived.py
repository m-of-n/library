#!/usr/bin/env python3
"""verify-signatures.derived.py -- DERIVED, written by this library (FX-1 pass 2, verify). Not part of the source.

    python3 -I verify-signatures.derived.py --eddsa VC-DI-EDDSA.html --ecdsa VC-DI-ECDSA.html \
        --ctx CREDENTIALS_V2.jsonld --ctx-examples CREDENTIALS_EXAMPLES_V2.jsonld \
        --ctx-di DATA_INTEGRITY_V2.jsonld [--lib DIR]

Checks the signature recipe that signatures.derived.json applies to the examples of
w3c-vc-data-integrity-1-0 against the test vectors of the two cryptosuite Recommendations
it cites and does not define, then re-runs the seven example proofs through it.

1. Recipe, from the cryptosuite documents themselves (read 2026-11-07 from
   https://www.w3.org/TR/vc-di-eddsa/ and https://www.w3.org/TR/vc-di-ecdsa/, both
   W3C Recommendation 15 May 2025): proofConfig is a clone of the proof without proofValue,
   with @context set to the document's (eddsa-jcs-2022: only if the document has one);
   transformedData is JCS (RFC 8785) or RDFC-1.0 of the document without its proof;
   hashData = SHA-256(canonical proofConfig) || SHA-256(transformedData);
   Ed25519 (RFC 8032), or ECDSA P-256 with SHA-256 and a 64-octet r||s, over hashData.
2. Validation: the recipe reproduces the documents' own vectors: eddsa-jcs-2022 (vc-di-eddsa
   B.3, Examples 29-39: both hashes, hashData, the signature verifies, and re-signing with the
   published secret key gives Example 37 exactly), eddsa-rdfc-2022 (B.1, the first signed
   credential: verifies) and ecdsa-rdfc-2019 P-256 (vc-di-ecdsa A.1, Examples 5-15: both
   canonical forms, both hashes, the signature verifies).
3. The seven proofs of Examples 2, 4, 5, 6 and 7, each with the key printed in its own
   verificationMethod fragment; a proof with previousProof over the document carrying the proof
   it names. Examples 9 to 14 are symbolic and have no values.

Needs PyLD (2.x, URDNA2015 == RDFC-1.0 for these inputs) and cryptography; --lib adds a
directory to sys.path for them. No network: every context comes from a file, and the
document loader refuses any other URL. The JCS here is sufficient only for documents of
strings, arrays and objects (no numbers), which is all the inputs are. Prints EXAMINED beside
FOUND; exits 1 if a vector check fails or an example result differs from
signatures.derived.json.
"""
import argparse, hashlib, html as H, json, pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
ap = argparse.ArgumentParser()
for k in ("--eddsa", "--ecdsa", "--ctx", "--ctx-examples", "--ctx-di"):
    ap.add_argument(k, required=True)
ap.add_argument("--lib")
a = ap.parse_args()
if a.lib:
    sys.path.insert(0, a.lib)
from pyld import jsonld  # noqa: E402
from cryptography.exceptions import InvalidSignature  # noqa: E402
from cryptography.hazmat.primitives import hashes  # noqa: E402
from cryptography.hazmat.primitives.asymmetric import ec, utils  # noqa: E402
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey, Ed25519PublicKey  # noqa: E402
from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat  # noqa: E402

B58 = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
PINNED = {"https://www.w3.org/ns/credentials/v2": "59955ced6697d61e03f2b2556febe5308ab16842846f5b586d7f1f7adec92734",
          "https://w3id.org/security/data-integrity/v2": "67f21e6e33a6c14e5ccfd2fc7865f7474fb71a04af7e94136cb399dfac8ae8f4"}
CTX = {"https://www.w3.org/ns/credentials/v2": a.ctx, "https://www.w3.org/ns/credentials/examples/v2": a.ctx_examples,
       "https://w3id.org/security/data-integrity/v2": a.ctx_di}
for url, path in CTX.items():
    got = hashlib.sha256(pathlib.Path(path).read_bytes()).hexdigest()
    if url in PINNED and got != PINNED[url]:
        sys.exit(f"{url}: file digest {got} is not the pinned digest")


def b58d(s):
    n = 0
    for c in s:
        n = n * 58 + B58.index(c)
    full = n.to_bytes((n.bit_length() + 7) // 8, "big") if n else b""
    return b"\x00" * (len(s) - len(s.lstrip("1"))) + full


def b58e(b):
    n, out = int.from_bytes(b, "big"), ""
    while n:
        n, r = divmod(n, 58)
        out = B58[r] + out
    return "1" * (len(b) - len(b.lstrip(b"\x00"))) + out


def mb(s):
    assert s[0] == "z", s
    return b58d(s[1:])


def loader(url, options=None):
    if url not in CTX:
        raise Exception("no network: " + url)
    return {"contextUrl": None, "documentUrl": url, "document": json.loads(pathlib.Path(CTX[url]).read_text())}


def rdfc(doc):
    return jsonld.normalize(doc, {"algorithm": "URDNA2015", "format": "application/n-quads",
                                  "documentLoader": loader, "safe": False}).encode()


def jcs(doc):
    return json.dumps(doc, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def hashdata(suite, unsecured, proof):
    cfg = {k: v for k, v in proof.items() if k != "proofValue"}
    if suite.endswith("-jcs-2022"):
        if "@context" in unsecured:
            cfg.setdefault("@context", unsecured["@context"])
        c, d = jcs(cfg), jcs(unsecured)
    else:
        if "@context" in unsecured:
            cfg["@context"] = unsecured["@context"]
        c, d = rdfc(cfg), rdfc(unsecured)
    return hashlib.sha256(c).digest() + hashlib.sha256(d).digest(), c, d


def pubkey(frag):
    k = mb(frag)
    if k[:2] == b"\xed\x01" and len(k) == 34:
        return "ed25519", Ed25519PublicKey.from_public_bytes(k[2:])
    if k[:2] == b"\x80\x24" and len(k) == 35:
        return "p256", ec.EllipticCurvePublicKey.from_encoded_point(ec.SECP256R1(), k[2:])
    raise ValueError(f"key multicodec prefix {k[:2].hex()} and length {len(k)}: not an ed25519-pub (ed01, 34 octets) or p256-pub (8024, 35 octets) multikey")


def verify(suite, unsecured, proof):
    try:
        kind, pk = pubkey(proof["verificationMethod"].split("#")[-1])
    except ValueError as e:
        return "fail", str(e)
    sig = mb(proof["proofValue"])
    if len(sig) != 64:
        return "fail", f"signature is {len(sig)} octets, {'Ed25519' if kind == 'ed25519' else 'P-256 r||s'} needs 64"
    hd, _, _ = hashdata(suite, unsecured, proof)
    try:
        if kind == "ed25519":
            pk.verify(sig, hd)
        else:
            pk.verify(utils.encode_dss_signature(int.from_bytes(sig[:32], "big"), int.from_bytes(sig[32:], "big")),
                      hd, ec.ECDSA(hashes.SHA256()))
        return "pass", "verifies"
    except InvalidSignature:
        return "fail", "signature does not verify under the printed key"


def pres(path):
    t = pathlib.Path(path).read_text(encoding="utf-8")
    return {int(m.group(1)): H.unescape(re.sub(r"<[^>]+>", "", m.group(2))).strip("\n")
            for m in re.finditer(r'Example<bdi>\s*(\d+)</bdi>.*?</div>\s*<pre[^>]*>(.*?)</pre>', t, re.S)}


ed, ecd = pres(a.eddsa), pres(a.ecdsa)
checks = []
doc = json.loads(ed[39]); pr = doc["proof"]; uns = {k: v for k, v in doc.items() if k != "proof"}
hd, c, d = hashdata("eddsa-jcs-2022", uns, pr)
checks += [("vc-di-eddsa B.3 Ex32: hash of canonical credential", hashlib.sha256(d).hexdigest() == ed[32].strip()),
           ("vc-di-eddsa B.3 Ex35: hash of canonical proof options", hashlib.sha256(c).hexdigest() == ed[35].strip()),
           ("vc-di-eddsa B.3 Ex36: hashData", hd.hex() == ed[36].strip()),
           ("vc-di-eddsa B.3 Ex39: signature verifies", verify("eddsa-jcs-2022", uns, pr)[0] == "pass")]
sk = mb(json.loads(re.sub(r"(\w+):", r'"\1":', ed[29]))["secretKeyMultibase"])
checks.append(("vc-di-eddsa B.3 Ex37: re-signing with the published secret key", sk[:2] == b"\x80\x26" and
               Ed25519PrivateKey.from_private_bytes(sk[2:]).sign(hd).hex() == ed[37].strip()))
def first_signed(examples, suite):
    for n, t in sorted(examples.items()):
        try:
            d = json.loads(t)
        except ValueError:
            continue           # a display that is not strict JSON (a wrapped line, a comment)
        if isinstance(d, dict) and isinstance(d.get("proof"), dict) and d["proof"].get("cryptosuite") == suite \
                and "proofValue" in d["proof"]:
            return n, d
    raise SystemExit(f"no signed {suite} example found")


rdn, rd = first_signed(ed, "eddsa-rdfc-2022")
checks.append((f"vc-di-eddsa B.1 Ex{rdn}: eddsa-rdfc-2022 signed credential verifies",
               verify("eddsa-rdfc-2022", {k: v for k, v in rd.items() if k != "proof"}, rd["proof"])[0] == "pass"))
doc = json.loads(ecd[15]); pr = doc["proof"]; uns = {k: v for k, v in doc.items() if k != "proof"}
hd, c, d = hashdata("ecdsa-rdfc-2019", uns, pr)
checks += [("vc-di-ecdsa A.1 Ex7: canonical credential", d.decode().strip() == ecd[7].strip()),
           ("vc-di-ecdsa A.1 Ex8: hash of canonical credential", hashlib.sha256(d).hexdigest() == ecd[8].strip()),
           ("vc-di-ecdsa A.1 Ex10: canonical proof options", c.decode().strip() == ecd[10].strip()),
           ("vc-di-ecdsa A.1 Ex11: hash of canonical proof options", hashlib.sha256(c).hexdigest() == ecd[11].strip()),
           ("vc-di-ecdsa A.1 Ex15: signature verifies", verify("ecdsa-rdfc-2019", uns, pr)[0] == "pass")]
keys = json.loads(ecd[5])
priv = ec.derive_private_key(int.from_bytes(mb(keys["secretKeyMultibase"])[2:], "big"), ec.SECP256R1())
vector_key = "z" + b58e(b"\x80\x24" + priv.public_key().public_bytes(Encoding.X962, PublicFormat.CompressedPoint))
bad = 0
for name, ok in checks:
    bad += not ok
    print(("ok   " if ok else "FAIL ") + name)
print(f"RECIPE: {len(checks)} vector checks examined, {bad} failing")

FIX = [(2, "ex02-simple-signed-json-document.json"), (4, "ex04-simple-signed-json-ld-document.json"),
       (5, "ex05-proof-with-expires.derived.json"), (6, "ex06-proof-set.derived.json"), (7, "ex07-proof-chain.derived.json")]
want = {(s["example"], s["index"]): (s["result"], s["why"]) for s in json.loads((HERE / "signatures.derived.json").read_text())["signatures"]}
differ = n = verified = 0
for ex, fn in FIX:
    d = json.loads((HERE / fn).read_text())
    proofs = d["proof"] if isinstance(d["proof"], list) else [d["proof"]]
    for i, p in enumerate(proofs):
        uns = {k: v for k, v in d.items() if k != "proof"}
        if p.get("previousProof"):
            named = [q for q in proofs if q.get("id") == p["previousProof"]]
            uns["proof"] = named[0] if len(named) == 1 else named
        res = verify(p["cryptosuite"], uns, p)
        n += 1
        verified += res[0] == "pass"
        same = want.get((ex, i), (None,))[0] == res[0]
        differ += not same
        print(f"Example {ex} proof {i} {p['cryptosuite']}: {res[0]} ({res[1]})" + ("" if same else "  <- differs from signatures.derived.json"))
print(f"EXAMPLES: {n} proofs examined, {verified} verify; {differ} differing from signatures.derived.json")
print("Examples 4 and 5 verificationMethod key is the vc-di-ecdsa A.1 test-vector key:",
      vector_key == "zDnaepBuvsQ8cpsWrVKw8fbpGpvPeNSjVPTWoq6cRqaYzBKVP")
sys.exit(1 if bad or differ else 0)

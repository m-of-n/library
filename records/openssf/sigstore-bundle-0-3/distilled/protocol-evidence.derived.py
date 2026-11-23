#!/usr/bin/env python3
# DERIVED - not verbatim. Written by this library (FX-1 verify pass, library#151), not by Sigstore.
#
# Reproduces protocol.yaml `evidence` E1 to E7 from the source's own bytes and compares every check's
# result with the committed file. Pass 1 ran these checks with a scratch script on the `cryptography`
# package; this is the reproducible replacement, stdlib plus the `openssl` command line tool.
#
#   python3 -I distilled/protocol-evidence.derived.py        (from the repository root, or anywhere)
#
# Input, by path, with its digest checked: .cache/sigstore-bundle-0-3.include/bundle.md (sha256
# 8d1127003af7...dd4746df0, the value pinned in ../render-source.py). Its three ```json fences that
# parse as JSON are the two example bundles and the attestation (rendering line = bundle.md line + 871).
# Nothing outside the source is used: no log, timestamp-authority or Fulcio key and no trust root.
# Also prints, for SD-P-6/SD-13, each leaf's issuer (openssl x509) and each checkpoint's origin.
# Exit 1 if any recomputed result differs from protocol.yaml, or a digest does not match.
import base64
import datetime
import hashlib
import json
import os
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, "..", "..", "..", ".."))
MD = os.path.join(ROOT, ".cache", "sigstore-bundle-0-3.include", "bundle.md")
MD_SHA256 = "8d1127003af7032392c24f1453ceb2a6043d9dd5706719122cc3f74dd4746df0"
OFF = 871
sys.path.insert(0, os.path.join(ROOT, "bin"))
import _yaml  # noqa: E402
import _record_yaml  # noqa: E402
from pathlib import Path  # noqa: E402

b64 = base64.b64decode
H = lambda x: hashlib.sha256(x).digest()  # noqa: E731


# ------------------------------------------------------------------ DER (minimal, definite lengths)
def tlv(b, i):
    tag, n, j = b[i], b[i + 1], i + 2
    if n & 0x80:
        c = n & 0x7F
        n, j = int.from_bytes(b[j:j + c], "big"), j + c
    return tag, j, j + n


def kids(b, s, e):
    out = []
    while s < e:
        t, cs, ce = tlv(b, s)
        out.append((t, cs, ce, s))
        s = ce
    return out


def oid(b, s, e):
    parts, x = [b[s] // 40, b[s] % 40], 0
    for c in b[s + 1:e]:
        x = (x << 7) | (c & 0x7F)
        if not c & 0x80:
            parts.append(x)
            x = 0
    return ".".join(map(str, parts))


def gtime(b, s, e, tag):
    t = b[s:e].decode()
    if tag == 0x17:
        t = ("20" if int(t[:2]) < 50 else "19") + t
    return datetime.datetime.strptime(t[:14], "%Y%m%d%H%M%S").replace(tzinfo=datetime.timezone.utc)


def cert_facts(der):
    _, cs, ce = tlv(der, 0)
    tbs = kids(der, cs, ce)[0]
    f = kids(der, tbs[1], tbs[2])
    i = 1 if f[0][0] == 0xA0 else 0
    val = kids(der, f[i + 3][1], f[i + 3][2])
    spki = der[f[i + 5][3]:f[i + 5][2]]
    return {"not_before": gtime(der, val[0][1], val[0][2], val[0][0]),
            "not_after": gtime(der, val[1][1], val[1][2], val[1][0]), "spki": spki}


def tst_facts(der):
    _, cs, ce = tlv(der, 0)
    top = kids(der, cs, ce)                                   # status, timeStampToken
    ci = kids(der, top[1][1], top[1][2])                      # contentType, [0]
    sd = kids(der, kids(der, ci[1][1], ci[1][2])[0][1], kids(der, ci[1][1], ci[1][2])[0][2])
    enc = kids(der, sd[2][1], sd[2][2])                       # eContentType, [0] eContent
    octs = kids(der, enc[1][1], enc[1][2])[0]
    info = der[octs[1]:octs[2]]
    tk = kids(info, tlv(info, 0)[1], tlv(info, 0)[2])
    mi = kids(info, tk[2][1], tk[2][2])
    alg = oid(info, kids(info, mi[0][1], mi[0][2])[0][1], kids(info, mi[0][1], mi[0][2])[0][2])
    gt = [x for x in tk if x[0] == 0x18][0]
    return {"alg": alg, "hashed": info[mi[1][1]:mi[1][2]], "gen_time": gtime(info, gt[1], gt[2], 0x18)}


# ------------------------------------------------------------------ openssl
def openssl(args, data=None):
    return subprocess.run(["openssl"] + args, input=data, capture_output=True)


def ecdsa(spki, msg, sig, prehashed):
    with tempfile.TemporaryDirectory() as td:
        k, m, s = (os.path.join(td, x) for x in ("k.pem", "m", "s"))
        open(k, "wb").write(b"-----BEGIN PUBLIC KEY-----\n" + base64.encodebytes(spki) + b"-----END PUBLIC KEY-----\n")
        open(m, "wb").write(msg)
        open(s, "wb").write(sig)
        cmd = (["pkeyutl", "-verify", "-pubin", "-inkey", k, "-in", m, "-sigfile", s] if prehashed
               else ["dgst", "-sha256", "-verify", k, "-signature", s, m])
        r = openssl(cmd)
        return r.returncode == 0 and b"Verified" in r.stdout


def names(der):
    r = openssl(["x509", "-inform", "DER", "-noout", "-issuer", "-subject", "-nameopt", "RFC2253"], der)
    return r.stdout.decode().strip().replace("\n", "; ")


def merkle(index, size, leaf, path, root):
    """RFC 9162 section 2.1.3.2."""
    if index >= size:
        return False
    fn, sn, r = index, size - 1, leaf
    for p in path:
        if sn == 0:
            return False
        if fn & 1 or fn == sn:
            r = H(b"\x01" + p + r)
            if not fn & 1:
                while not fn & 1 and fn != 0:
                    fn >>= 1
                    sn >>= 1
        else:
            r = H(b"\x01" + r + p)
        fn >>= 1
        sn >>= 1
    return sn == 0 and r == root


def pae(t, p):
    return b"DSSEv1 %d %s %d " % (len(t), t, len(p)) + p


def main():
    raw = open(MD, "rb").read()
    if hashlib.sha256(raw).hexdigest() != MD_SHA256:
        raise SystemExit("bundle.md: sha256 mismatch")
    lines = raw.decode("utf-8")[:-1].split("\n")
    fences, i = [], 0
    while i < len(lines):
        if lines[i].startswith("```json"):
            j = i + 1
            while not lines[j].startswith("```"):
                j += 1
            fences.append((i + 1 + OFF, "\n".join(lines[i + 1:j])))
            i = j + 1
        else:
            i += 1
    parsed = {}
    for at, t in fences:
        try:
            parsed[at] = json.loads(t)
        except json.JSONDecodeError:
            pass
    assert sorted(parsed) == [1035, 1081, 1141], sorted(parsed)
    MS, DS, ATT = parsed[1035], parsed[1081], parsed[1141]
    print(f"{len(fences)} json fences in bundle.md; parse as JSON: fences at rendering L{', L'.join(map(str, sorted(parsed)))}")
    R = {}

    # E1 message signature
    mder = b64(MS["verificationMaterial"]["certificate"]["rawBytes"])
    mc = cert_facts(mder)
    sig, dig = b64(MS["messageSignature"]["signature"]), b64(MS["messageSignature"]["messageDigest"]["digest"])
    R["E1"] = [ecdsa(mc["spki"], dig, sig, True), ecdsa(mc["spki"], dig, sig, False)]
    # E2 DSSE
    env = DS["dsseEnvelope"]
    pt, payload, dsig = env["payloadType"].encode(), b64(env["payload"]), b64(env["signatures"][0]["sig"])
    dder = b64(DS["verificationMaterial"]["x509CertificateChain"]["certificates"][0]["rawBytes"])
    dc = cert_facts(dder)
    R["E2"] = [ecdsa(dc["spki"], pae(pt, payload), dsig, False),
               ecdsa(dc["spki"], pae(pt, env["payload"].encode()), dsig, False),
               ecdsa(dc["spki"], payload, dsig, False),
               json.loads(payload) == ATT,
               len(env["signatures"]) == 1 and env["signatures"][0].get("keyid") == ""]
    # E3 RFC 3161 imprint
    T = tst_facts(b64(DS["verificationMaterial"]["timestampVerificationData"]["rfc3161Timestamps"][0]["signedTimestamp"]))
    R["E3"] = [T["hashed"] == H(dsig) and T["alg"] == "2.16.840.1.101.3.4.2.1", T["hashed"] == H(pae(pt, payload)),
               T["hashed"] == H(payload), T["hashed"] == H(env["signatures"][0]["sig"].encode())]
    # E4 inclusion proofs, E5 checkpoints
    R["E4"], R["E5"], origins = [], [], {}
    for name, B in (("ms", MS), ("dsse", DS)):
        e = B["verificationMaterial"]["tlogEntries"][0]
        pr = e["inclusionProof"]
        leaf, path, root = H(b"\x00" + b64(e["canonicalizedBody"])), [b64(h) for h in pr["hashes"]], b64(pr["rootHash"])
        R["E4"] += [merkle(int(pr["logIndex"]), int(pr["treeSize"]), leaf, path, root),
                    merkle(int(e["logIndex"]), int(pr["treeSize"]), leaf, path, root)]
        head, _, sigs = pr["checkpoint"]["envelope"].partition("\n\n")
        hl, sl = head.split("\n"), [x for x in sigs.split("\n") if x]
        origin = hl[0].split(" - ")[0]
        origins[name] = (hl[0], hl[3:])
        want_extra = [] if name == "ms" else ["Timestamp: 1675209600000000000"]
        R["E5"] += [hl[1] == pr["treeSize"] and hl[2] == pr["rootHash"] and hl[3:] == want_extra,
                    len(sl) == 1 and sl[0].split(" ")[1] == origin]
    # E6 canonicalized_body against the content
    bm = json.loads(b64(MS["verificationMaterial"]["tlogEntries"][0]["canonicalizedBody"]))
    bd = json.loads(b64(DS["verificationMaterial"]["tlogEntries"][0]["canonicalizedBody"]))
    s0 = bd["spec"]["content"]["envelope"]["signatures"][0]
    pem_der = lambda pem: b64(b"".join(x for x in pem.split(b"\n") if x and not x.startswith(b"-----")))  # noqa: E731
    R["E6"] = [bm["spec"]["signature"]["content"] == MS["messageSignature"]["signature"],
               bytes.fromhex(bm["spec"]["data"]["hash"]["value"]) == dig,
               pem_der(b64(bm["spec"]["signature"]["publicKey"]["content"])) == mder,
               s0["sig"] == env["signatures"][0]["sig"],
               b64(s0["sig"]) == env["signatures"][0]["sig"].encode(),
               b64(bd["spec"]["content"]["envelope"]["payload"]) == env["payload"].encode(),
               pem_der(b64(s0["publicKey"])) == dder,
               bd["spec"]["content"]["payloadHash"]["value"] == hashlib.sha256(payload).hexdigest()]
    # E7 signing times against validity
    ts = lambda s: datetime.datetime.fromtimestamp(int(s), datetime.timezone.utc)  # noqa: E731
    mit = ts(MS["verificationMaterial"]["tlogEntries"][0]["integratedTime"])
    dit = ts(DS["verificationMaterial"]["tlogEntries"][0]["integratedTime"])
    R["E7"] = [mc["not_before"] < mit < mc["not_after"], dit == dc["not_before"], T["gen_time"] == dc["not_before"]]

    for name, der, c in (("message-signature leaf", mder, mc), ("DSSE leaf", dder, dc)):
        print(f"{name}: {names(der)}; valid {c['not_before'].isoformat()} .. {c['not_after'].isoformat()} "
              f"({int((c['not_after'] - c['not_before']).total_seconds())} s)")
    for name, (o, extra) in origins.items():
        print(f"{name} checkpoint origin line {o!r}; optional lines {extra}")
    print(f"DSSE genTime {T['gen_time'].isoformat()}; integratedTime ms {mit.isoformat()}, dsse {dit.isoformat()}")

    p = os.path.join(HERE, "protocol.yaml")
    a, b = _yaml.parse(open(p, encoding="utf-8").read()), _record_yaml.load_yaml(Path(p))
    if a["evidence"] != b["evidence"]:
        raise SystemExit("bin/_yaml.py and bin/_record_yaml.py read protocol.yaml's evidence differently")
    fails, n = 0, 0
    for item in a["evidence"]:
        want = [str(c["result"]) == "true" for c in item["checks"]]
        got = R.get(item["id"])
        n += len(want)
        if got != want:
            fails += 1
            print(f"DIFFERS {item['id']}: recomputed {got}, protocol.yaml {want}")
        else:
            print(f"{item['id']}: {len(want)} checks agree ({sum(want)} true, {len(want) - sum(want)} false)")
    print(f"EXAMINED {n} checks in {len(a['evidence'])} evidence items; {fails} item(s) differ")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""reproduce.py -- re-extract every code-block example of the DSSE specification at
commit 1d3370f from the pinned archive and check this directory, including the
ECDSA test vector of protocol.md 1.4, recomputed from first principles.

    python3 -I reproduce.py [PATH/TO/secure-systems-lab-dsse.tar.gz]            # check
    python3 -I reproduce.py [PATH/TO/secure-systems-lab-dsse.tar.gz] --write    # (re)write fixtures, pae hex, index.yaml

Sources. The archive (sha256 88fc65fd...3ac1 = content.sha256 in record.yaml) is
.cache/secure-systems-lab-dsse.tar.gz, searched upward from this directory. The
rendering .cache/secure-systems-lab-dsse.txt (sha256 b5fe6fb2...913247) is what
every FX-1 tool counts lines in; "line N" everywhere below is a rendering line.
It is rebuilt here from the archive by ../render-source.py and compared. Nothing
from the archive is copied into the repository except short fixtures: the code
blocks of a Markdown file, each a few lines, each reproduced by this script.

What is an example. Every fenced block of the source (13 of them, counted by two
extractors) is a fixture: the ECDSA test vector and its template / narrative
siblings. protocol.md 1.4 (lines 146-180) is the only test vector. A fixture is
the content lines between the fences, joined by LF, WITHOUT a final newline, and
with the opening fence's own indentation removed (the CommonMark rule; the PAE
grammar block of 1.2 is nested in a list item). Whether the final newline belongs
to the bytes is not a convention: a body with it is 12 bytes, PAE would print
"... 12 hello world", and the printed signature verifies only over the 11-byte
body; check (e) below proves that by a negative test.

Checks (each reports EXAMINED beside FOUND; exit 1 on any difference):
  a  sha256 of the archive, of its five specification members, of the rendering,
     and the rendering rebuilt by ../render-source.py is byte-identical
  b  two independent extractors (rendering fence scan; archive regex over the
     Markdown / decoded notebook cells) return the same 13 blocks, byte for byte,
     and agree with the fixtures on disk; the rendering line spans are the ones
     this file's table says
  c  PAE(UTF8(PAYLOAD_TYPE), SERIALIZED_BODY) built two ways equals the printed PAE
     line byte for byte; its hex and sha256 are written
  d  an ECDSA P-256 / RFC 6979 implementation (stdlib integers, affine arithmetic)
     SELF-TESTS on RFC 6979 Appendix A.2.5 (SHA-256, "sample" and "test"), then:
       (1) d*G == (X, Y) of the key block and (X, Y) is on the curve
       (2) the Result envelope's sig is 64 bytes r||s and verifies over the PAE
       (3) the deterministic signature recomputed from d over the PAE equals the
           printed sig exactly
       (4) the payload base64-decodes to SERIALIZED_BODY
  e  negative checks: signature over the bare body, over the PAE with a changed
     type, with a changed body, over PAE with the body's trailing newline, over
     PAE of the BASE64 payload, a flipped signature bit, the wrong key: all fail
  f  the derived PAE vectors (pae-vectors.derived.json) through ../schema/check-pae.derived.py
  g  the derived schema cases through ../schema/check-envelope.derived.py; the
     Result envelope fixture is the instance of case ENV-A01, the section 2.1
     template fixture is the instance of case ENV-R22; every id the cases cite
     exists in ../requirements.yaml or ../inferred-candidates.yaml
  h  index.yaml equals the one rebuilt here (quote and source_lines per fixture
     are verified against the rendering by bin/check-quotes)

RFC 6979 constants below are copied from RFC 6979 (https://www.rfc-editor.org/rfc/rfc6979.txt,
fetched 2026-11-20, sha256 456e8f17558fdbd206f968b96fc6f1b4a71ea331ab30ad17f711ab3adaa7d701):
Appendix A.2.5 (heading line 1799), q line 1805, private key x line 1810, Ux line 1814,
Uy line 1816, SHA-256 "sample" k, r, s lines 1831-1833, SHA-256 "test" k, r, s lines 1866-1868.
"""
import base64, hashlib, hmac, importlib.util, io, json, os, re, subprocess, sys, tarfile, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
DIST = os.path.dirname(HERE)
REC = "secure-systems-lab-dsse"
ARCHIVE_SHA = "88fc65fd66d7250445dc08a65a2cb68c942fb88517152246f859a70d6dac3ac1"
RENDER_SHA = "b5fe6fb26be4eb9f3ac26391e376e0d677fbb041ede59397a8dabc1734913247"
PREFIX = "dsse-1d3370f62565bca041e97c8310b873ac340edc2e/"
MEMBERS = [
    ("protocol.md", "6c0d965475162230f9f461acf634b4d4b409eab1a1839d31a9c24c76b3676253"),
    ("envelope.md", "3a8e7370671354cf3d3417c818a44dcda02cbc57dce6f4b6a75a84c41c483074"),
    ("envelope.proto", "2f689071f134f1a348ccc2af1e1cfa3f8a6ebed2a2576765dd55e764b0a0cbfb"),
    ("background.md", "a824667d3cbd6eedeb6f788a38bf4e690bd9b875381dbf809fda7bf48727bac4"),
    ("hypothetical_signature_attack.ipynb", "0a13a7ff7438b224ddc8e4d69dc535083cdc05807e2308abdc2e0516aedd8581"),
]
# rendering line of each file's column-0 heading "i.  <name>" (checked against the rendering)
FILE_HEADINGS = {1: "1.  protocol.md", 189: "2.  envelope.md", 280: "3.  envelope.proto",
                 320: "4.  background.md", 498: "5.  hypothetical_signature_attack.ipynb"}

# fixture table: (file name, kind, source member, first content line, last content line, label line or None, role)
FIXTURES = [
    ("signature-formula.verbatim.txt", "formula", "protocol.md", 19, 19, None, "SIGNATURE = Sign(PAE(...)), the definition of a signature (1.1)"),
    ("pae-definition.verbatim.txt", "grammar", "protocol.md", 64, 68, None, "PAE() and the symbols it uses (1.1); source of schema/pae.derived.abnf"),
    ("serialized-body.verbatim.txt", "vector", "protocol.md", 149, 149, 146, "SERIALIZED_BODY of the test vector (1.4)"),
    ("payload-type.verbatim.txt", "vector", "protocol.md", 155, 155, 152, "PAYLOAD_TYPE of the test vector (1.4)"),
    ("pae.verbatim.txt", "vector", "protocol.md", 161, 161, 158, "the PAE of the test vector, as printed (1.4)"),
    ("keys.verbatim.txt", "vector", "protocol.md", 167, 171, 164, "algorithm, signature encoding and the P-256 key (X, Y, d) of the test vector (1.4)"),
    ("result-envelope.verbatim.json", "vector", "protocol.md", 177, 179, 174, "the signed JSON envelope of the test vector (1.4)"),
    ("envelope-template.verbatim.json", "template", "envelope.md", 211, 218, 207, "the standard JSON envelope as a template with <...> placeholders (2.1)"),
    ("envelope-template-multi.verbatim.json", "template", "envelope.md", 233, 243, 229, "the multiple-signature JSON envelope as a template (2.1.1)"),
    ("notebook-link-legitimate.verbatim.json", "narrative", "hypothetical_signature_attack.ipynb", 568, 573, 565, "attack notebook: the legitimate in-toto link file"),
    ("notebook-link-forged.verbatim.json", "narrative", "hypothetical_signature_attack.ipynb", 579, 584, 576, "attack notebook: the link file the attacker gets falsely signed"),
    ("notebook-cbor-diagram.verbatim.txt", "narrative", "hypothetical_signature_attack.ipynb", 1058, 1063, 1055, "attack notebook: the CBOR payload as shown by cbor.me"),
    ("notebook-build-command.verbatim.txt", "narrative", "hypothetical_signature_attack.ipynb", 1082, 1082, 1079, "attack notebook: the shape of the crafted build command"),
]
FAILS = []
EXAMINED = [0]


def check(cond, what):
    EXAMINED[0] += 1
    if not cond:
        FAILS.append(what)
        print("FAIL:", what)


def find_cache(name, start=HERE):
    d = start
    while True:
        p = os.path.join(d, ".cache", name)
        if os.path.exists(p):
            return p
        if os.path.dirname(d) == d:
            sys.exit(f"reproduce.py: no .cache/{name} found above {start}; pass the archive path")
        d = os.path.dirname(d)


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


# ---------------------------------------------------------------- extractors
FENCE = re.compile(r"^( *)(```|~~~)([A-Za-z]*)[ \t]*$")


def extract_rendering(lines):
    """A: scan the rendering line by line. -> [(first content line, last, content bytes, info, heading file)]"""
    out, cur = [], None
    for n, l in enumerate(lines, 1):
        m = FENCE.match(l)
        if cur is None:
            if m:
                cur = {"indent": m.group(1), "tok": m.group(2), "info": m.group(3), "start": n + 1, "rows": []}
        elif m and m.group(2) == cur["tok"] and not m.group(3):
            fh = max(k for k in FILE_HEADINGS if k <= n)
            rows = [r[len(cur["indent"]):] if r.startswith(cur["indent"]) else r.lstrip(" ") for r in cur["rows"]]
            out.append((cur["start"], n - 1, "\n".join(rows).encode("utf-8"), cur["info"], fh))
            cur = None
        else:
            cur["rows"].append(l)
    check(cur is None, "rendering: unterminated fence")
    return out


def extract_archive(members):
    """B: whole-document regex over the member bytes (Markdown) / decoded markdown cells (notebook)."""
    rx = re.compile(r"^( *)(```|~~~)([A-Za-z]*)[ \t]*\n(.*?)\n\1\2[ \t]*$", re.M | re.S)
    out = []
    docs = [("protocol.md", members["protocol.md"].decode("utf-8")),
            ("envelope.md", members["envelope.md"].decode("utf-8")),
            ("background.md", members["background.md"].decode("utf-8"))]
    nb = json.loads(members["hypothetical_signature_attack.ipynb"].decode("utf-8"))
    for i, c in enumerate(nb["cells"]):
        if c["cell_type"] == "markdown":
            docs.append(("hypothetical_signature_attack.ipynb", "".join(c["source"])))
    for name, text in docs:
        for m in rx.finditer(text):
            ind = m.group(1)
            rows = [r[len(ind):] if r.startswith(ind) else r.lstrip(" ") for r in m.group(4).split("\n")]
            out.append((name, "\n".join(rows).encode("utf-8"), m.group(3)))
    # a fence regex over code cells would be wrong; assert the source has none there
    for c in nb["cells"]:
        if c["cell_type"] == "code":
            check("```" not in "".join(c["source"]), "a code cell of the notebook contains a fence marker")
    return out


# ---------------------------------------------------------------- P-256, RFC 6979 (stdlib)
P = 0xFFFFFFFF00000001000000000000000000000000FFFFFFFFFFFFFFFFFFFFFFFF
A = P - 3
B = 0x5AC635D8AA3A93E7B3EBBD55769886BC651D06B0CC53B0F63BCE3C3E27D2604B
N = 0xFFFFFFFF00000000FFFFFFFFFFFFFFFFBCE6FAADA7179E84F3B9CAC2FC632551
G = (0x6B17D1F2E12C4247F8BCE6E563A440F277037D812DEB33A0F4A13945D898C296,
     0x4FE342E2FE1A7F9B8EE7EB4A7C0F9E162BCE33576B315ECECBB6406837BF51F5)


def on_curve(Q):
    return Q is not None and (Q[1] * Q[1] - (Q[0] ** 3 + A * Q[0] + B)) % P == 0


def add(Pt, Q):
    if Pt is None: return Q
    if Q is None: return Pt
    x1, y1 = Pt
    x2, y2 = Q
    if x1 == x2 and (y1 + y2) % P == 0:
        return None
    lam = ((3 * x1 * x1 + A) * pow(2 * y1, -1, P) if Pt == Q else (y2 - y1) * pow(x2 - x1, -1, P)) % P
    x3 = (lam * lam - x1 - x2) % P
    return (x3, (lam * (x1 - x3) - y1) % P)


def mul(k, Pt):
    R = None
    while k:
        if k & 1:
            R = add(R, Pt)
        Pt = add(Pt, Pt)
        k >>= 1
    return R


def hmac_sha256(k, m):
    return hmac.new(k, m, hashlib.sha256).digest()


def rfc6979_k(x, h1):
    """RFC 6979 section 3.2 with HMAC-SHA-256; qlen = hlen = 256, so bits2int is the identity and no shifting occurs."""
    xo = x.to_bytes(32, "big")
    ho = (int.from_bytes(h1, "big") % N).to_bytes(32, "big")  # bits2octets
    V, K = b"\x01" * 32, b"\x00" * 32
    K = hmac_sha256(K, V + b"\x00" + xo + ho); V = hmac_sha256(K, V)
    K = hmac_sha256(K, V + b"\x01" + xo + ho); V = hmac_sha256(K, V)
    while True:
        V = hmac_sha256(K, V)
        k = int.from_bytes(V, "big")
        if 1 <= k < N:
            return k
        K = hmac_sha256(K, V + b"\x00"); V = hmac_sha256(K, V)


def sign(x, msg):
    h = hashlib.sha256(msg).digest()
    k = rfc6979_k(x, h)
    r = mul(k, G)[0] % N
    s = pow(k, -1, N) * (int.from_bytes(h, "big") + r * x) % N
    return k, r, s


def verify(Q, msg, r, s):
    if not (1 <= r < N and 1 <= s < N) or not on_curve(Q):
        return False
    e = int.from_bytes(hashlib.sha256(msg).digest(), "big")
    w = pow(s, -1, N)
    R = add(mul(e * w % N, G), mul(r * w % N, Q))
    return R is not None and R[0] % N == r


def split_sig(sig):
    return int.from_bytes(sig[:32], "big"), int.from_bytes(sig[32:], "big")


# ---------------------------------------------------------------- yaml out
def q(s):
    assert "\n" not in s
    return "'" + s.replace("'", "''") + "'"


def b64d(s):
    s = s.replace("-", "+").replace("_", "/")
    return base64.b64decode(s + "=" * (-len(s) % 4), validate=True)


def main():
    argv = sys.argv[1:]
    write = "--write" in argv
    paths = [a for a in argv if not a.startswith("--")]
    archive = paths[0] if paths else find_cache("secure-systems-lab-dsse.tar.gz")
    rend_path = os.path.join(os.path.dirname(archive), "secure-systems-lab-dsse.txt")

    # ---- a: hashes, rendering
    ab = open(archive, "rb").read()
    check(hashlib.sha256(ab).hexdigest() == ARCHIVE_SHA, "archive sha256 is not content.sha256")
    tf = tarfile.open(fileobj=io.BytesIO(ab), mode="r:gz")
    members = {}
    for name, sha in MEMBERS:
        members[name] = tf.extractfile(PREFIX + name).read()
        check(hashlib.sha256(members[name]).hexdigest() == sha, f"{name}: sha256")
    rb = open(rend_path, "rb").read()
    check(hashlib.sha256(rb).hexdigest() == RENDER_SHA, "rendering sha256")
    with tempfile.TemporaryDirectory() as td:
        out = os.path.join(td, "r.txt")
        subprocess.run([sys.executable, "-I", os.path.join(DIST, "render-source.py"), archive, out], check=True)
        check(open(out, "rb").read() == rb, "rendering rebuilt by render-source.py differs from .cache rendering")
    req_head = open(os.path.join(DIST, "requirements.yaml")).read()
    check(f"source_digest: '{RENDER_SHA}'" in req_head, "requirements.yaml source_digest is not the rendering's sha256")
    lines = rb.decode("utf-8").split("\n")
    for n, h in FILE_HEADINGS.items():
        check(lines[n - 1] == h, f"rendering line {n} is not {h!r}")

    # ---- b: two extractors, fixtures
    A_ = extract_rendering(lines)
    B_ = extract_archive(members)
    check(len(A_) == len(B_) == len(FIXTURES) == 13, f"fence counts: rendering {len(A_)}, archive {len(B_)}, table {len(FIXTURES)}")
    check([a[2] for a in A_] == [b[1] for b in B_], "extractors disagree on block bytes or order")
    check([a[3] for a in A_] == [b[2] for b in B_], "extractors disagree on info strings")
    files = {}
    for (name, kind, src, a, b, label, role), ra in zip(FIXTURES, A_):
        check((ra[0], ra[1]) == (a, b), f"{name}: rendering lines {ra[0]}-{ra[1]} != table {a}-{b}")
        check(lines[ra[0] - 2].lstrip().startswith(("```", "~~~")), f"{name}: no opening fence above line {a}")
        files[name] = ra[2]
    if write:
        for name, data in files.items():
            open(os.path.join(HERE, name), "wb").write(data)
    for name, data in files.items():
        p = os.path.join(HERE, name)
        check(os.path.exists(p) and open(p, "rb").read() == data, f"{name}: missing or bytes differ from the source")
    on_disk = sorted(f for f in os.listdir(HERE) if ".verbatim." in f)
    check(on_disk == sorted(files), f"fixture set on disk {on_disk} != extracted {sorted(files)}")
    F = files
    body, ptype, pae_printed = F["serialized-body.verbatim.txt"], F["payload-type.verbatim.txt"], F["pae.verbatim.txt"]
    check(body == b"hello world" and len(body) == 11, "SERIALIZED_BODY is not the 11 bytes 'hello world'")
    check(ptype == b"http://example.com/HelloWorld" and len(ptype) == 29, "PAYLOAD_TYPE is not the 29 bytes")
    check(not body.endswith(b"\n") and not pae_printed.endswith(b"\n"), "a fixture ends with a newline")

    # ---- c: PAE
    cp = load(os.path.join(DIST, "schema", "check-pae.derived.py"), "check_pae")
    pae = cp.build(ptype, body)
    pae2 = b"DSSEv1 %d %s %d %s" % (len(ptype), ptype, len(body), body)  # second, independent construction
    check(pae == pae2 == pae_printed, "PAE(UTF8(PAYLOAD_TYPE), SERIALIZED_BODY) != the printed PAE line")
    check(pae == b"DSSEv1 29 http://example.com/HelloWorld 11 hello world", "PAE differs from the literal")
    check(cp.parse(pae) == (ptype, body), "PAE does not parse back to (type, body)")
    pae_hex, pae_sha = pae.hex(), hashlib.sha256(pae).hexdigest()
    hexfile = os.path.join(HERE, "pae-section-1-4.derived.hex")
    if write:
        open(hexfile, "w").write(pae_hex + "\n")
    check(os.path.exists(hexfile) and open(hexfile).read() == pae_hex + "\n", "pae-section-1-4.derived.hex differs")

    # ---- d: ECDSA
    # d.0 self-test on RFC 6979 A.2.5
    x6979 = 0xC9AFA9D845BA75166B5C215767B1D6934E50C3DB36E89B127B8A622B120F6721
    Ux = 0x60FED4BA255A9D31C961EB74C6356D68C049B8923B61FA6CE669622E60F29FB6
    Uy = 0x7903FE1008B8BC99A41AE9E95628BC64F2F1B20C2D7E9F5177A3C294D4462299
    check(mul(x6979, G) == (Ux, Uy), "self-test: x*G != (Ux, Uy) of RFC 6979 A.2.5")
    check(on_curve(G) and mul(N, G) is None, "self-test: G not on curve or n*G != infinity")
    rfc = {
        b"sample": (0xA6E3C57DD01ABE90086538398355DD4C3B17AA873382B0F24D6129493D8AAD60,
                    0xEFD48B2AACB6A8FD1140DD9CD45E81D69D2C877B56AAF991C34D0EA84EAF3716,
                    0xF7CB1C942D657C41D436C7A1B6E29F65F3E900DBB9AFF4064DC4AB2F843ACDA8),
        b"test": (0xD16B6AE827F17175E040871A1C7EC3500192C4C92677336EC2537ACAEE0008E0,
                  0xF1ABB023518351CD71D881567B1EA663ED3EFCF6C5132B354F28D3B0B7D38367,
                  0x019F4113742A2B14BD25926B49C649155F267E60D3814B4C0CC84250E46F0083),
    }
    for m, (k, r, s) in rfc.items():
        got = sign(x6979, m)
        check(got == (k, r, s), f"self-test: RFC 6979 A.2.5 SHA-256 {m!r}: (k, r, s) differ")
        check(verify((Ux, Uy), m, r, s), f"self-test: RFC 6979 A.2.5 {m!r} does not verify")
        check(not verify((Ux, Uy), m + b"x", r, s), f"self-test: {m!r}+x must not verify")
    # d.1 key block
    keys = F["keys.verbatim.txt"].decode("utf-8")
    kv = dict(re.findall(r"^(Algorithm|Signature|X|Y|d): (.*)$", keys, re.M))
    check(sorted(kv) == ["Algorithm", "Signature", "X", "Y", "d"], f"key block fields: {sorted(kv)}")
    X, Y, d = int(kv["X"]), int(kv["Y"]), int(kv["d"])
    check(kv["Algorithm"] == "ECDSA over NIST P-256 and SHA-256, with deterministic-rfc6979", "key block Algorithm line")
    check(0 < X < P and 0 < Y < P and 0 < d < N, "X, Y < p and d < n")
    check(on_curve((X, Y)), "(X, Y) is not on P-256")
    check(mul(d, G) == (X, Y), "d*G != (X, Y)")
    # d.2 result envelope
    env = json.loads(F["result-envelope.verbatim.json"].decode("utf-8"))
    check(list(env) == ["payload", "payloadType", "signatures"], "result envelope members")
    check(env["payloadType"] == ptype.decode("utf-8"), "result envelope payloadType != PAYLOAD_TYPE")
    check(len(env["signatures"]) == 1 and list(env["signatures"][0]) == ["sig"], "result envelope: one signature, sig only")
    sig = b64d(env["signatures"][0]["sig"])
    check(len(sig) == 64, f"sig is {len(sig)} bytes, expected 64 (r||s)")
    r, s = split_sig(sig)
    check(verify((X, Y), pae, r, s), "printed sig does not verify over the PAE with (X, Y)")
    # d.3 deterministic recomputation
    k, r2, s2 = sign(d, pae)
    sig2 = r2.to_bytes(32, "big") + s2.to_bytes(32, "big")
    check(sig2 == sig, "recomputed RFC 6979 signature != printed sig")
    check(base64.b64encode(sig2).decode() == env["signatures"][0]["sig"], "re-encoded standard base64 != printed sig text")
    # d.4 payload
    check(b64d(env["payload"]) == body, "payload does not base64-decode to SERIALIZED_BODY")
    check(base64.b64encode(body).decode() == env["payload"], "payload is not the standard padded base64 of the body")
    # URL-safe spelling decodes identically (protocol 1.2: verifiers MUST accept either)
    sig_url = env["signatures"][0]["sig"].replace("+", "-").replace("/", "_")
    check(sig_url != env["signatures"][0]["sig"] and b64d(sig_url) == sig, "url-safe spelling of sig")
    check("+" in env["signatures"][0]["sig"] and not set("-_") & set(env["signatures"][0]["sig"]),
          "sig contains '+' and neither '-' nor '_' (so the printed vector is standard, not URL-safe)")

    # ---- e: negatives
    Q = (X, Y)
    neg = {
        "bare body": body,
        "PAE with a changed type": cp.build(ptype + b"2", body),
        "PAE with a changed body": cp.build(ptype, body + b"!"),
        "PAE with the body's trailing newline": cp.build(ptype, body + b"\n"),
        "PAE over the base64 payload text": cp.build(ptype, env["payload"].encode()),
        "PAE with the type swapped for the body": cp.build(body, ptype),
        "the printed PAE with a trailing newline": pae + b"\n",
        "PAE of an empty type": cp.build(b"", body),
        "version string DSSEv2": b"DSSEv2" + pae[6:],
    }
    for what, m in neg.items():
        check(not verify(Q, m, r, s), f"negative: signature over {what} must not verify")
    flips = 0
    for bit in (0, 255, 256, 511):
        t = bytearray(sig); t[bit // 8] ^= 1 << (bit % 8)
        rr, ss = split_sig(bytes(t))
        check(not verify(Q, pae, rr, ss), f"negative: flipping signature bit {bit}")
        flips += 1
    other_neg = {  # one check each, so the printed count is the number of negatives (pass 2: was 9 + 4 + 5)
        "wrong key": (mul(2, G), r, s),
        "r and s swapped": (Q, s, r),
        "r = 0": (Q, 0, s),
        "s = 0": (Q, r, 0),
        "r = n": (Q, N, s),
        "public key off the curve": ((X, (Y + 1) % P), r, s),
    }
    for what, (key, rr, ss) in other_neg.items():
        check(not verify(key, pae, rr, ss), f"negative: {what}")
    low_s = s <= N // 2

    # ---- f: derived PAE vectors
    pv = json.load(open(os.path.join(HERE, "pae-vectors.derived.json")))
    check(any(v["id"] == "PAE-V00" and bytes.fromhex(v["pae_hex"]) == pae_printed for v in pv["build"]),
          "PAE-V00 is not the section 1.4 vector")
    rc_pae = cp.main()
    if rc_pae:
        FAILS.append("check-pae.derived.py failed")

    # ---- g: schema cases
    ce = load(os.path.join(DIST, "schema", "check-envelope.derived.py"), "check_envelope")
    schema = json.load(open(os.path.join(DIST, "schema", "envelope.derived.schema.json")))
    cases = json.load(open(os.path.join(HERE, "cases.derived.json")))["cases"]
    byid = {c["id"]: c for c in cases}
    check(byid["ENV-A01"]["instance"] == env, "case ENV-A01 is not the Result envelope fixture")
    t1 = json.loads(F["envelope-template.verbatim.json"].decode("utf-8"))
    check(byid["ENV-R22"]["instance"] == t1, "case ENV-R22 is not the section 2.1 template fixture")
    tm = json.loads(F["envelope-template-multi.verbatim.json"].decode("utf-8"))
    check(len(tm["signatures"]) == 2, "section 2.1.1 template has two signatures")
    ids = set(re.findall(r"- id: '([^']+)'", req_head))
    cand = set("C-" + x for x in re.findall(r"- id: 'C-(\d+)'", open(os.path.join(DIST, "inferred-candidates.yaml")).read()))
    cited = {i for c in cases for i in c["cites"]}
    for i in sorted(cited):
        check(i in ids or i in cand, f"cases.derived.json cites {i}, in neither requirements.yaml nor inferred-candidates.yaml")
    rc_env = ce.main()
    if rc_env:
        FAILS.append("check-envelope.derived.py failed")
    exp = {}
    for nm, inst in (("envelope-template.verbatim.json", t1), ("envelope-template-multi.verbatim.json", tm),
                     ("result-envelope.verbatim.json", env)):
        exp[nm] = {"Envelope": ce.validate(schema, "Envelope", inst)[0],
                   "EnvelopeStrict": ce.validate(schema, "EnvelopeStrict", inst)[0]}
    check(exp["result-envelope.verbatim.json"] == {"Envelope": [], "EnvelopeStrict": []}, "Result envelope must satisfy both definitions")
    for nm in ("envelope-template.verbatim.json", "envelope-template-multi.verbatim.json"):
        check(exp[nm]["Envelope"] != [], f"{nm}: a template with placeholders must not be a valid envelope as-is")
    for nm in ("notebook-link-legitimate.verbatim.json", "notebook-link-forged.verbatim.json"):
        j = json.loads(F[nm].decode("utf-8"))
        check(j["_type"] == "link" and ce.validate(schema, "Envelope", j)[0] != [], f"{nm}: a link file is not a DSSE envelope")

    # ---- h: index.yaml
    y = ["# Fixture index. Written by reproduce.py --write; quote: and source_lines: are verified by bin/check-quotes.",
         f"record: {REC}", 'reviewed_by: ""',
         f"source: {q('.cache/secure-systems-lab-dsse.tar.gz, pinned archive, sha256 ' + ARCHIVE_SHA + '; line numbers are lines of the rendering .cache/secure-systems-lab-dsse.txt, sha256 ' + RENDER_SHA)}",
         "convention: 'a fixture is the content lines between the fences joined by LF, no final newline, the opening fence indentation removed; reproduce.py proves the no-final-newline reading (check e)'",
         "fixtures:"]
    for (name, kind, src, a, b, label, role), ra in zip(FIXTURES, A_):
        data = F[name]
        y += [f"  - fixture: {q(name)}", f"    kind: {kind}", f"    role: {q(role)}",
              f"    source_member: {q(src)}", f"    source_lines: '{a}-{b}'" if a != b else f"    source_lines: '{a}'",
              f"    quote: {q(' '.join(' '.join(lines[a - 1:b]).split()))}"]
        if label:
            y += ["    label:", f"      source_lines: '{label}'", f"      quote: {q(' '.join(lines[label - 1].split()))}"]
        y += [f"    sha256: {q(hashlib.sha256(data).hexdigest())}", f"    bytes: {len(data)}"]
        y += ["    expected:"]
        if name == "serialized-body.verbatim.txt":
            y += ["      length: 11", f"      hex: {q(data.hex())}", "      trailing_newline: false"]
        elif name == "payload-type.verbatim.txt":
            y += ["      length: 29", f"      hex: {q(data.hex())}", "      trailing_newline: false"]
        elif name == "pae.verbatim.txt":
            y += ["      equals_recomputed_pae: true   # PAE(UTF8(PAYLOAD_TYPE), SERIALIZED_BODY), reproduce.py check c",
                  f"      pae_hex: {q(pae_hex)}", f"      pae_sha256: {q(pae_sha)}", f"      pae_length: {len(pae)}",
                  "      note: 'the printed fenced block has no trailing newline, and SERIALIZED_BODY has none: 11 bytes, LEN 11; with a newline the body would be 12 bytes'"]
        elif name == "keys.verbatim.txt":
            y += ["      d_times_G_equals_X_Y: true", "      point_on_curve: true",
                  "      note: 'X, Y and d are decimal integers; the curve is NIST P-256 (secp256r1); signature = r||s, 64 bytes, 32 bytes each big-endian (the 32-byte width is not stated by the source, which says only Cryptodome binary encoding)'"]
        elif name == "result-envelope.verbatim.json":
            y += ["      valid_Envelope: true", "      valid_EnvelopeStrict: true",
                  "      sig_bytes: 64", f"      sig_r_hex: {q(format(r, '064x'))}", f"      sig_s_hex: {q(format(s, '064x'))}",
                  f"      sig_s_is_low: {str(low_s).lower()}   # informational; the source says nothing about low-s",
                  "      sig_verifies_over_pae: true", "      sig_equals_rfc6979_deterministic_recomputation: true",
                  f"      rfc6979_k_hex: {q(format(k, '064x'))}", "      payload_decodes_to_serialized_body: true",
                  "      alphabet: 'standard (the sig contains +, and no - or _); padded'"]
        elif kind == "template":
            e = exp[name]["Envelope"]
            y += ["      valid_Envelope: false   # a template: <...> placeholders are not base64 (payload, sig); the other placeholders are valid strings",
                  "      valid_as_a_shape: true  # members and nesting are the DSSE envelope's",
                  "      errors:"] + [f"        - {q(x)}" for x in e]
        elif kind == "narrative":
            y += ["      dsse_envelope: false   # a pre-DSSE illustration, no PAE, nothing signed here"]
            if name.endswith(".json"):
                y += ["      parses_as_json: true"]
            elif name != "notebook-cbor-diagram.verbatim.txt":
                y += ["      parses_as_json: false"]
            else:
                y += ["      parses_as_json: false"]
        else:
            y += ["      reproduced: true   # a definition, not a vector; schema/pae.derived.abnf is derived from it" if kind == "grammar"
                  else "      reproduced: true   # a definition, not a vector"]
    y_text = "\n".join(y) + "\n"
    ip = os.path.join(HERE, "index.yaml")
    if write:
        open(ip, "w").write(y_text)
    check(os.path.exists(ip) and open(ip).read() == y_text, "index.yaml differs from the one rebuilt from the source")
    allowed = set(files) | {"index.yaml", "cases.derived.json", "pae-vectors.derived.json", "pae-section-1-4.derived.hex",
                            "reproduce.py", "README.md", "__pycache__"}
    extra = sorted(set(os.listdir(HERE)) - allowed)
    check(not extra, f"unexpected files in examples/: {extra}")

    print(f"examined {EXAMINED[0]} reproduce checks; fixtures {len(files)} (blocks: rendering {len(A_)}, archive {len(B_)}), "
          f"RFC 6979 self-test vectors {len(rfc)}, negative signature checks {len(neg) + flips + len(other_neg)}, "
          f"cases cite {len(cited)} distinct ids; printed sig s is {'low' if low_s else 'high'}")
    print("reproduce: " + ("FAILED" if FAILS else "ok"))
    return 1 if FAILS else 0


if __name__ == "__main__":
    sys.exit(main())

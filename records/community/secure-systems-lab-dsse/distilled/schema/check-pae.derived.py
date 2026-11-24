#!/usr/bin/env python3
# DERIVED - not verbatim. Written by this library, not copied from the DSSE
# specification. A builder and a strict parser for the PAE byte format of
# pae.derived.abnf, checked against ../examples/pae-vectors.derived.json:
# every build vector must equal its hand-typed expected bytes, every parse
# vector must round-trip, every reject vector must be refused for the stated
# reason, plus properties (round trip, injectivity) over generated inputs.
#
#   python3 -I check-pae.derived.py
#
# Stdlib only. The parser is deliberately strict and independent of build():
# it reads LEN with an ASCII-digit test (int() would accept U+0663 and '+3').
import hashlib, itertools, json, os, random, sys

HERE = os.path.dirname(os.path.abspath(__file__))
VECTORS = os.path.join(HERE, "..", "examples", "pae-vectors.derived.json")


def build(type_bytes, body):
    """PAE(type, body) = "DSSEv1" SP LEN(type) SP type SP LEN(body) SP body."""
    assert isinstance(type_bytes, bytes) and isinstance(body, bytes)
    return b" ".join([b"DSSEv1", str(len(type_bytes)).encode("ascii"), type_bytes,
                      str(len(body)).encode("ascii"), body])


class PaeError(ValueError):
    pass


def _len(b, i, what):
    """Read LEN at b[i:]: '0' or [1-9][0-9]*, ASCII only; return (value, next index)."""
    j = i
    while j < len(b) and 0x30 <= b[j] <= 0x39:
        j += 1
    digits = b[i:j]
    if not digits:
        raise PaeError(f"{what}: no decimal digits")
    if len(digits) > 1 and digits[0] == 0x30:
        raise PaeError(f"{what}: leading zero")
    return int(digits), j


def parse(b):
    """Strict parse of one PAE byte string to (type, body). Raises PaeError."""
    if not isinstance(b, bytes):
        raise PaeError("not bytes")
    if not b.startswith(b"DSSEv1 "):
        raise PaeError("version: does not start with DSSEv1 and a space")
    i = 7
    n, i = _len(b, i, "type-len")
    if b[i:i + 1] != b" ":
        raise PaeError("type-len: not followed by a space")
    i += 1
    if len(b) - i < n:
        raise PaeError("type: fewer octets than type-len")
    t, i = b[i:i + n], i + n
    if b[i:i + 1] != b" ":
        raise PaeError("type: not followed by a space (type shorter than type-len or long)")
    i += 1
    m, i = _len(b, i, "body-len")
    if b[i:i + 1] != b" ":
        raise PaeError("body-len: not followed by a space")
    i += 1
    body = b[i:]
    if len(body) != m:
        raise PaeError(f"body: {len(body)} octets where body-len says {m}")
    return t, body


def main():
    doc = json.load(open(VECTORS))
    fails, n = [], 0

    def chk(c, what):
        nonlocal n
        n += 1
        if not c:
            fails.append(what)

    nb = npar = nrej = 0
    for v in doc["build"]:
        t, body = bytes.fromhex(v["type_hex"]), bytes.fromhex(v["body_hex"])
        want = bytes.fromhex(v["pae_hex"])
        nb += 1
        chk(build(t, body) == want, f"{v['id']}: build differs from hand-typed expected bytes")
        chk(hashlib.sha256(want).hexdigest() == v["pae_sha256"], f"{v['id']}: sha256 of expected bytes")
        chk(len(want) == v["pae_length"], f"{v['id']}: length")
        npar += 1
        chk(parse(want) == (t, body), f"{v['id']}: parse(expected) != (type, body)")
        if "type_text" in v:
            chk(v["type_text"].encode("utf-8") == t, f"{v['id']}: type_text is not the UTF-8 of type_hex")
    for v in doc["reject"]:
        nrej += 1
        b = bytes.fromhex(v["pae_hex"])
        try:
            parse(b)
            fails.append(f"{v['id']}: parser accepted a string the grammar rejects")
        except PaeError as e:
            chk(v["error_contains"] in str(e), f"{v['id']}: refused for the wrong reason: {e}")
    # properties over generated inputs
    rnd = random.Random(0xD55E)
    alphabet = [b" ", b"0", b"1", b"9", b"a", b"\x00", b"\xff", b"\xc3\xa9", b"D", b"\n"]
    seen, ncase = {}, 0
    for _ in range(20000):
        t = b"".join(rnd.choice(alphabet) for _ in range(rnd.randrange(0, 6)))
        body = b"".join(rnd.choice(alphabet) for _ in range(rnd.randrange(0, 12)))
        p = build(t, body)
        ncase += 1
        if parse(p) != (t, body):
            fails.append(f"round trip fails for {t!r} {body!r}")
            break
        if p in seen and seen[p] != (t, body):
            fails.append(f"collision: {p!r} from {seen[p]!r} and {(t, body)!r}")
            break
        seen[p] = (t, body)
    n += ncase
    # exhaustive injectivity over alphabet {' ', '1', 'a'}, lengths 0..3 each
    pairs = []
    al = [b" ", b"1", b"a"]
    strs = [b"".join(c) for k in range(4) for c in itertools.product(al, repeat=k)]
    ex = {}
    for t in strs:
        for body in strs:
            p = build(t, body)
            pairs.append(p)
            if p in ex:
                fails.append(f"exhaustive collision {p!r}")
            ex[p] = (t, body)
    n += len(strs) ** 2
    print(f"pae vectors examined: build {nb}, parse round-trip {npar}, reject {nrej}; "
          f"random round-trip/injectivity cases {ncase}; exhaustive injectivity pairs {len(strs) ** 2} "
          f"({len(strs)} strings of length 0-3 over 3 symbols); checks run {n}")
    for f in fails:
        print("FAIL:", f)
    print("check-pae: " + ("FAILED" if fails else "ok"))
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""DERIVED harness (the fixtures beside it are VERBATIM). Re-extracts every
fixture from the source by line range and checks the bytes, parses each with
spki_sexp.derived.py, matches each against the BNF with spki_bnf.derived.py,
and checks every conversion the draft prints (advanced <-> base64 transport,
length prefixes, hashes of the printed keys, signatures where checkable).

    python3 -I reproduce.py            # check; exit 1 on any unexpected result
    python3 -I reproduce.py --write    # (re)write the fixture files from the source

Source: <repo>/.cache/draft-ietf-spki-cert-structure.txt (or argv path after
--src). Page furniture (footer, running header, blank runs round them) inside
a range is elided exactly as schema/verbatim_files.derived.py elides it.
"""
import hashlib
import importlib.util
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
SCHEMA = HERE.parent / "schema"
ROOT = HERE.parents[4]
SRC = ROOT / ".cache" / "draft-ietf-spki-cert-structure.txt"
if "--src" in sys.argv:
    SRC = pathlib.Path(sys.argv[sys.argv.index("--src") + 1])


def load(name, path):
    sp = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(sp)
    sp.loader.exec_module(m)
    return m


vf = load("vf", SCHEMA / "verbatim_files.derived.py")
bnf = load("bnf", SCHEMA / "spki_bnf.derived.py")
sx = bnf.sx  # one class identity for Atom/Lst

# id, file stem, locator, ranges [(first,last)] or span (line, substring), form, expect
# form: adv | transport | canonical | template | elided
# expect: BNF verdict as "rule:ok" / "rule:REJECT" / None (no BNF rule applies)
F = [
    ("E01", "s2-name-local", "§2", [(405, 405)], "adv", "relative-name:ok"),
    ("E02", "s2-name-fq", "§2", [(407, 407)], "adv", "fq-name:ok"),
    ("E03", "s3-4-canonical", "§3.4", [(639, 639)], "canonical", "s-expr:ok"),
    ("E04", "s3-4-advanced", "§3.4", [(646, 646)], "adv", "s-expr:ok"),
    ("E05", "s3-4-transport", "§3.4", [(656, 657)], "transport", "s-expr:ok"),
    ("E06", "s3-8-1-1-rsa-public-advanced", "§3.8.1.1", [(815, 821)], "adv", "pub-key:ok"),
    ("E07", "s3-8-1-1-rsa-public-transport", "§3.8.1.1", [(826, 829)], "transport", "pub-key:ok"),
    ("E08", "s3-8-1-1-rsa-private-advanced", "§3.8.1.1", [(834, 868)], "adv", None),
    ("E09", "s3-8-1-1-rsa-private-transport", "§3.8.1.1", [(872, 887)], "transport", None),
    ("E10", "s3-8-1-2-dsa-public-advanced", "§3.8.1.2", [(899, 923)], "adv", "pub-key:ok"),
    ("E11", "s3-8-1-2-dsa-public-transport", "§3.8.1.2", [(929, 939)], "transport", "pub-key:ok"),
    ("E12", "s3-8-1-2-dsa-private-elided", "§3.8.1.2", [(944, 958)], "elided", None),
    ("E13", "s3-8-2-hash-md5-advanced", "§3.8.2", [(1004, 1004)], "adv", "hash:ok"),
    ("E14", "s3-8-2-hash-md5-transport", "§3.8.2", [(1005, 1005)], "transport", "hash:ok"),
    ("E15", "s3-8-2-hash-sha1-advanced", "§3.8.2", [(1007, 1007)], "adv", "hash:ok"),
    ("E16", "s3-8-2-hash-sha1-transport", "§3.8.2", [(1008, 1008)], "transport", "hash:ok"),
    ("E17", "s3-8-3-2-signature-rsa", "§3.8.3.2", [(1052, 1066)], "adv", "signature:ok"),
    ("E18", "s3-8-3-2-signature-dsa", "§3.8.3.2", [(1068, 1097)], "adv", "signature:ok"),
    ("E19", "s3-8-3-1-dsa-sig-params-template", "§3.8.3.1", [(1043, 1043)], "template", None),
    ("E20", "s4-1-version-default", "§4.1", ("L1172",'(version "0")'), "adv", "version:ok"),
    ("E21", "s4-8-tag-all", "§4.8", ("L1391", "(tag (*))"), "adv", "tag:ok"),
    ("E22", "s4-9-1-date-1", "§4.9.1", ("L1450", '"1997-07-26_23:15:10"'), "date", None),
    ("E23", "s4-9-1-date-2", "§4.9.1", ("L1451", '"2001-01-01_00:00:00"'), "date", None),
    ("E24", "s5-1-name-cert-template", "§5.1", [(1630, 1634)], "adv", "name-cert:REJECT"),  # parses: <principal> etc. are placeholder tokens
    ("E25", "s5-3-name-cert-advanced", "§5.3", [(1698, 1702)], "adv", "name-cert:REJECT"),
    ("E26", "s5-3-name-cert-transport", "§5.3", [(1704, 1707)], "transport", "name-cert:REJECT"),
    ("E27", "s5-3-name-before", "§5.3", [(1717, 1718)], "adv", "subject:ok"),
    ("E28", "s5-3-name-after", "§5.3", [(1722, 1723)], "adv", "subject:ok"),
    ("E29", "s5-3-name-cert-trouble", "§5.3", [(1731, 1735)], "adv", "name-cert:REJECT"),
    ("E30", "s6-1-acl-advanced", "§6.1", [(1801, 1812)], "adv", "acl:ok"),
    ("E31", "s6-1-acl-transport", "§6.1", [(1814, 1820)], "transport", "acl:ok"),
]
# pairs the draft prints as the same object in two forms: (advanced, other)
PAIRS = [("E04", "E03"), ("E04", "E05"), ("E06", "E07"), ("E08", "E09"), ("E10", "E11"),
         ("E13", "E14"), ("E15", "E16"), ("E25", "E26"), ("E30", "E31")]


def fixture_bytes(src, gone, spec):
    if isinstance(spec, tuple):  # inline span
        ln, sub = int(spec[0][1:]), spec[1]
        line = src[ln - 1]
        assert line.count(sub) == 1, f"{spec}: substring not exactly once in L{ln}"
        return (sub + "\n").encode()
    lines = []
    for a, b in spec:
        lines += [src[l - 1] for l in range(a, b + 1) if l not in gone]
    while lines and not lines[-1].strip():
        lines.pop()
    return ("\n".join(lines) + "\n").encode()


def fname(e):
    return f"{e[0].lower()}-{e[1]}.verbatim.txt"


def to_node(form, text):
    if form == "canonical":
        return sx.parse_canonical(text.strip().encode("latin-1"))
    if form == "transport":
        return sx.parse_transport(text)
    return sx.parse_advanced(text)


def rsa_check(sig, pub):
    e = sx.decode_integer(pub[1]); n = sx.decode_integer(pub[2])
    s = int.from_bytes(sig, "big")
    k = (n.bit_length() + 7) // 8
    em = pow(s, e, n).to_bytes(k, "big")
    return em


def dsa_check(z, r, s, p, q, g, y):
    if not (0 < r < q and 0 < s < q):
        return False
    w = pow(s, -1, q)
    u1, u2 = (z * w) % q, (r * w) % q
    return ((pow(g, u1, p) * pow(y, u2, p)) % p) % q == r


def main():
    write = "--write" in sys.argv
    src = SRC.read_text(encoding="utf-8").split("\n")
    gone = vf.furniture(src)
    g = bnf.grammar_from_file()
    nodes, bad, rows = {}, [], []
    for e in F:
        eid, stem, loc, spec, form, expect = e
        data = fixture_bytes(src, gone, spec)
        path = HERE / fname(e)
        if write:
            path.write_bytes(data)
        elif not path.exists() or path.read_bytes() != data:
            bad.append(f"{eid}: fixture file differs from the source ({path.name})")
        text = data.decode("latin-1")
        verdict = ""
        if form in ("template", "elided"):
            try:
                to_node(form, text)
                verdict = "PARSED"
                bad.append(f"{eid}: a {form} fixture unexpectedly parsed")
            except sx.SexpError as ex:
                verdict = "not parseable (expected): " + str(ex)[:50]
        else:
            try:
                node = to_node("adv" if form == "date" else form, text if form != "date" else "(x " + text.strip() + ")")
            except sx.SexpError as ex:
                bad.append(f"{eid}: parse failed: {ex}")
                rows.append((eid, form, "PARSE FAIL"))
                continue
            nodes[eid] = node
            if form == "date":
                a = node.items[1]
                sx.check_date(a)
                verdict = "date format ok"
            elif expect:
                rule, want = expect.split(":")
                res = bnf.check(g, rule, node)
                got = "ok" if res.ok else "REJECT"
                verdict = f"<{rule}> {got}" + ("" if res.ok else " (" + res.why() + ")")
                if got != want:
                    bad.append(f"{eid}: <{rule}> {got}, recorded {want}")
            else:
                verdict = "parsed; no BNF rule (object defined nowhere in the draft)"
        rows.append((eid, form, verdict))
    # conversions
    conv = 0
    for a, b in PAIRS:
        conv += 1
        ca, cb = sx.encode(nodes[a]), sx.encode(nodes[b])
        if ca != cb:
            bad.append(f"pair {a}/{b}: canonical bytes differ ({len(ca)} vs {len(cb)})")
    # base64 line shape: RFC 2045 lines are at most 76 chars; report the width the draft uses
    # length-prefix check on E03
    assert sx.encode(nodes["E04"]) == b"(4:test26:abcdefghijklmnopqrstuvwxyz5:123455::: ::)"
    conv += 1
    # hashes of the printed key (3.8.2: "the public key given above has the following hashes")
    key = sx.encode(nodes["E06"])
    for hid, alg in (("E13", "md5"), ("E15", "sha1")):
        want = nodes[hid].items[2].data
        got = hashlib.new(alg, key).digest()
        conv += 1
        info = "matches" if got == want else "DOES NOT match"
        print(f"  {alg}(canonical E06) {info} the printed {hid} value")
        if got != want:
            bad.append(f"{hid}: {alg} of the canonical RSA public key is {got.hex()}, the draft prints {want.hex()}")
    # signatures
    s = nodes["E17"]
    hv = s.items[1].items[2].data
    pub = s.items[2].items[1]
    sig = s.items[3].items[1].data
    em = rsa_check(sig, pub.items[1:] and (None, pub.items[1].items[1], pub.items[2].items[1]))
    di = bytes.fromhex("3021300906052b0e03021a05000414") + hv
    k = len(em)
    good = em == b"\x00\x01" + b"\xff" * (k - 3 - len(di)) + b"\x00" + di
    tail_hash = em[-20:] == hv
    tail_di = em[-36:-20] == di[:-20][-16:]
    print(f"  E17 RSA PKCS#1 v1.5 sha1 signature over the printed hash verifies: {good}")
    print(f"      recovered block ends with the printed hash: {tail_hash}; block starts 00 01: {em[:2] == b'\\x00\\x01'}")
    print(f"      DigestInfo bytes before the hash: {em[-36:-20].hex()} (sha1 DigestInfo ends 05 00 04 14: {di[-20 - 4:-20].hex()})")
    if good or not tail_hash or em[:2] == b"\x00\x01":  # recorded: does NOT verify; trailing hash matches
        bad.append("E17: RSA signature outcome differs from the recorded one (does not verify, block ends with the hash)")
    d = nodes["E18"]
    dh = d.items[1].items[2].data
    kp = {x.items[0].data: sx.decode_integer(x.items[1]) for x in d.items[2].items[1].items[1:]}
    sv = {x.items[0].data: sx.decode_integer(x.items[1]) for x in d.items[3].items[1:]}
    dsa_ok = dsa_check(int.from_bytes(dh, "big"), sv[b"r"], sv[b"s"], kp[b"p"], kp[b"q"], kp[b"g"], kp[b"y"])
    print(f"  E18 DSA-SHA1 signature over the printed hash verifies: {dsa_ok}")
    if not dsa_ok:
        bad.append("E18: DSA signature outcome differs from the recorded one (verifies)")
    # Which bytes the value is over (R-0398): the printed hash value, as above, or the sha1 of
    # the canonical (hash ...) object the signature carries. Recorded: only the first verifies.
    alt = hashlib.sha1(sx.encode(d.items[1])).digest()
    alt_ok = dsa_check(int.from_bytes(alt, "big"), sv[b"r"], sv[b"s"], kp[b"p"], kp[b"q"], kp[b"g"], kp[b"y"])
    print(f"  E18 DSA-SHA1 signature over sha1 of the canonical (hash ...) object verifies: {alt_ok}")
    if alt_ok:
        bad.append("E18: DSA signature also verifies over the (hash ...) object's sha1 (recorded: it does not)")
    for r in rows:
        print(f"{r[0]}  {r[1]:9} {r[2]}")
    print(f"reproduce: {len(F)} fixtures, {conv} conversion checks, {len(bad)} unexpected")
    for b in bad:
        print("  UNEXPECTED: " + b)
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()

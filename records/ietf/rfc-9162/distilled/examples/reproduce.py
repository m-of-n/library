#!/usr/bin/env python3
# DERIVED, not verbatim. Written by this library, not copied from RFC 9162.
# Rebuilds every *.derived.json fixture in this directory from first
# principles and checks the RFC's own printed structure against the result.
#
#   python3 -I reproduce.py            # check: fixtures on disk == rebuilt
#   python3 -I reproduce.py --write    # regenerate the fixtures, then check
#
# Stdlib only. Source: RFC 9162 (.cache/rfc-9162.txt).
#   Merkle tree      Section 2.1.1   (MTH, 0x00 leaf prefix, 0x01 node prefix)
#   inclusion proof  Section 2.1.3.1 (PATH) and 2.1.3.2 (verify, as printed)
#   consistency      Section 2.1.4.1 (PROOF, SUBPROOF) and 2.1.4.2 (verify)
#   worked example   Section 2.1.5   (7 leaves a..l, hash0, hash1=k, hash2)
#   wire format      Sections 4.4-4.12, 6.3, 7.1 (TLS presentation language)
#
# The RFC prints tree STRUCTURE (node names) and no hash values. This file
# CHOOSES the inputs: d[i] = bytes([i]) for i = 0..6, HASH = SHA-256. Every
# hash in the fixtures follows from that choice and from nothing else.
import base64, hashlib, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ARGS = set(sys.argv[1:])
FAILS = []
CHECKS = [0]


def check(cond, what):
    CHECKS[0] += 1
    if not cond:
        FAILS.append(what)
        print("FAIL:", what)


def HASH(b):
    return hashlib.sha256(b).digest()


HASH_SIZE = 32


def leaf_hash(d):
    return HASH(b"\x00" + d)


def node_hash(l, r):
    return HASH(b"\x01" + l + r)


def lsb(x):
    return x & 1


def largest_pow2_lt(n):
    # "the largest power of two smaller than n (i.e., k < n <= 2k)", n > 1
    k = 1
    while k * 2 < n:
        k *= 2
    return k


def is_pow2(x):
    return x > 0 and x & (x - 1) == 0


# ---------------------------------------------------------------- 2.1.1
def MTH(D):
    n = len(D)
    if n == 0:
        return HASH(b"")
    if n == 1:
        return leaf_hash(D[0])
    k = largest_pow2_lt(n)
    return node_hash(MTH(D[:k]), MTH(D[k:]))


# ---------------------------------------------------------------- 2.1.2
def tree_head_from_entries(entries):
    """Section 2.1.2 as printed (stack algorithm). entries are the d[i]."""
    stack = []
    for i in range(len(entries)):
        stack.append(leaf_hash(entries[i]))
        merge_count = 0
        while lsb(i >> merge_count):  # lowest value s.t. LSB(i >> mc) not set
            merge_count += 1
        for _ in range(merge_count):
            right = stack.pop()
            left = stack.pop()
            stack.append(node_hash(left, right))
    while len(stack) > 1:  # step 3
        right = stack.pop()
        left = stack.pop()
        stack.append(node_hash(left, right))
    return stack[0] if stack else HASH(b"")


# ---------------------------------------------------------------- 2.1.3.1
def PATH(m, D):
    n = len(D)
    assert 0 <= m < n
    if n == 1:
        return []
    k = largest_pow2_lt(n)
    if m < k:
        return PATH(m, D[:k]) + [MTH(D[k:])]
    return PATH(m - k, D[k:]) + [MTH(D[:k])]


# ---------------------------------------------------------------- 2.1.4.1
def SUBPROOF(m, D, b):
    n = len(D)
    if m == n:
        return [] if b else [MTH(D)]
    assert m < n
    k = largest_pow2_lt(n)
    if m <= k:
        return SUBPROOF(m, D[:k], b) + [MTH(D[k:])]
    return SUBPROOF(m - k, D[k:], False) + [MTH(D[:k])]


def PROOF(m, D):
    assert 0 < m < len(D)
    return SUBPROOF(m, D, True)


# ---------------------------------------------------------------- 2.1.3.2
def verify_inclusion(leaf_h, leaf_index, tree_size, path, root_hash):
    """Section 2.1.3.2, steps 1-5 as printed. Returns (ok, reason)."""
    if leaf_index >= tree_size:  # step 1
        return False, "step 1: leaf_index >= tree_size"
    fn, sn = leaf_index, tree_size - 1  # step 2
    r = leaf_h  # step 3
    for p in path:  # step 4
        if sn == 0:  # 4a
            return False, "step 4a: sn is 0 with path values left"
        if lsb(fn) or fn == sn:  # 4b
            r = node_hash(p, r)  # 4b.i
            if not lsb(fn):  # 4b.ii
                while not (lsb(fn) or fn == 0):
                    fn >>= 1
                    sn >>= 1
        else:
            r = node_hash(r, p)
        fn >>= 1  # 4c
        sn >>= 1
    if sn != 0:  # step 5
        return False, "step 5: sn is not 0 after the path"
    if r != root_hash:
        return False, "step 5: computed root differs from root_hash"
    return True, "ok"


# ---------------------------------------------------------------- 2.1.4.2
def verify_consistency(first, second, first_hash, second_hash, path,
                       enforce_domain=True):
    """Section 2.1.4.2, steps 1-7 as printed. Returns (ok, reason).
    The section is stated for 0 < first < second; enforce_domain=False runs
    the steps outside that domain to record what they do there."""
    if enforce_domain and not (0 < first < second):
        return False, "out of domain: needs 0 < first < second"
    path = list(path)
    if len(path) == 0:  # step 1
        return False, "step 1: consistency_path is empty"
    if is_pow2(first):  # step 2
        path = [first_hash] + path
    fn, sn = first - 1, second - 1  # step 3
    if lsb(fn):  # step 4
        while lsb(fn):
            fn >>= 1
            sn >>= 1
    fr = sr = path[0]  # step 5
    for c in path[1:]:  # step 6
        if sn == 0:  # 6a
            return False, "step 6a: sn is 0 with path values left"
        if lsb(fn) or fn == sn:  # 6b
            fr = node_hash(c, fr)
            sr = node_hash(c, sr)
            if not lsb(fn):
                while not (lsb(fn) or fn == 0):
                    fn >>= 1
                    sn >>= 1
        else:
            sr = node_hash(sr, c)
        fn >>= 1  # 6c
        sn >>= 1
    if fr != first_hash:  # step 7
        return False, "step 7: fr differs from first_hash"
    if sr != second_hash:
        return False, "step 7: sr differs from second_hash"
    if sn != 0:
        return False, "step 7: sn is not 0"
    return True, "ok"


# ================================================================ 2.1.5
D = [bytes([i]) for i in range(7)]  # d0..d6, chosen here, not in the RFC
a, b, c, d, e, f = (leaf_hash(x) for x in D[:6])
j = leaf_hash(D[6])  # j is the leaf hash of d6 (the figure hangs d6 under j)
g, h, i_, = node_hash(a, b), node_hash(c, d), node_hash(e, f)
k, l = node_hash(g, h), node_hash(i_, j)
ROOT = node_hash(k, l)
hash0 = node_hash(g, c)  # 3 leaves: g over (a b), c = leaf hash of d2
hash1 = k  # 4 leaves, the figure writes hash1=k
hash2 = node_hash(k, i_)  # 6 leaves
NODES = {"a": a, "b": b, "c": c, "d": d, "e": e, "f": f, "g": g, "h": h,
         "i": i_, "j": j, "k": k, "l": l, "hash": ROOT,
         "hash0": hash0, "hash1": hash1, "hash2": hash2}
NAME = {}
for nm in "abcdefghijkl":
    NAME[NODES[nm]] = nm


def names(path):
    return [NAME[x] for x in path]


def hx(x):
    return x.hex()


# ---- the structure the RFC prints in 2.1.5 (typed from the figure text)
RFC_INCLUSION = {0: ["b", "h", "l"], 3: ["c", "g", "l"],
                 4: ["f", "j", "k"], 6: ["i", "k"]}
RFC_CONSISTENCY = {3: ["c", "d", "g", "l"], 4: ["l"], 6: ["i", "j", "k"]}
RFC_CONS_HASH = {3: ("hash0", hash0), 4: ("hash1", hash1), 6: ("hash2", hash2)}

# ---- structural self-checks on the choice of leaves and the figure
check(MTH(D) == ROOT, "MTH(D7) equals node 'hash' built by hand from the figure")
check(MTH(D[:3]) == hash0, "MTH(D[0:3]) equals hash0")
check(MTH(D[:4]) == hash1 == k, "MTH(D[0:4]) equals hash1 = k")
check(MTH(D[:6]) == hash2, "MTH(D[0:6]) equals hash2")
check(MTH(D[4:7]) == l, "MTH(D[4:7]) equals l")
check(MTH(D[4:6]) == i_ and MTH(D[6:7]) == j, "i and j")
check(tree_head_from_entries(D) == ROOT, "2.1.2 stack algorithm gives the same root (7)")
check(MTH([]) == HASH(b""), "MTH({}) = HASH()")
check(len(set(NODES[x] for x in "abcdefghijkl")) == 12, "the 12 named nodes are distinct")

for m_, want in RFC_INCLUSION.items():
    got = names(PATH(m_, D))
    check(got == want, "PATH(%d, D7) = %s as printed (got %s)" % (m_, want, got))
for m_, want in RFC_CONSISTENCY.items():
    got = names(PROOF(m_, D))
    check(got == want, "PROOF(%d, D7) = %s as printed (got %s)" % (m_, want, got))

# ---- no external oracle. RFC 9162 prints no hash values, and no file in
# this repository holds reference Merkle roots, so nothing here vouches for a
# hash value from outside this file. (Pass 2, 2026-11-08, removed eight
# "reference roots" that pass 1 typed from recollection of an outside test
# corpus: a value typed from memory is not a source.) The independent check
# that remains is internal to the RFC: two different printed algorithms, the
# 2.1.1 recursion (MTH) and the 2.1.2 stack algorithm, give the same root for
# every tree of 1..65 leaves (below). Neither can catch a misreading the two
# share, such as the 0x00/0x01 prefixes, which rest on 2.1.1 as printed.

# ---- exhaustive: the printed verify algorithms accept every generated proof
LEAVES = [bytes([x]) for x in range(70)]
inc_ok = inc_bad = cons_ok = cons_bad = 0
mut = {"short": 0, "long": 0, "flip": 0, "index": 0, "size_accepted_anyway": 0, "size_checked": 0}
for n in range(1, 66):
    Dn = LEAVES[:n]
    root = MTH(Dn)
    check(tree_head_from_entries(Dn) == root, "2.1.2 == MTH for n=%d" % n)
    for m_ in range(n):
        path = PATH(m_, Dn)
        ok, why = verify_inclusion(leaf_hash(Dn[m_]), m_, n, path, root)
        check(ok, "inclusion accepts PATH(%d, D%d): %s" % (m_, n, why))
        inc_ok += ok
        inc_bad += (not ok)
        # rejections (must all fail)
        if path:
            ok2, _ = verify_inclusion(leaf_hash(Dn[m_]), m_, n, path[:-1], root)
            check(not ok2, "inclusion rejects short path m=%d n=%d" % (m_, n))
            mut["short"] += 1
            bad = list(path)
            bad[0] = bytes([bad[0][0] ^ 1]) + bad[0][1:]
            ok2, _ = verify_inclusion(leaf_hash(Dn[m_]), m_, n, bad, root)
            check(not ok2, "inclusion rejects flipped node m=%d n=%d" % (m_, n))
            mut["flip"] += 1
        ok2, _ = verify_inclusion(leaf_hash(Dn[m_]), m_, n, path + [root], root)
        check(not ok2, "inclusion rejects long path m=%d n=%d" % (m_, n))
        mut["long"] += 1
        ok2, _ = verify_inclusion(leaf_hash(Dn[m_]), n + m_, n, path, root)
        check(not ok2, "inclusion rejects leaf_index>=tree_size m=%d n=%d" % (m_, n))
        mut["index"] += 1
        # NOT asserted: a wrong tree_size is not always rejected. The root hash
        # does not commit to tree_size; only the path shape (fn/sn bits) does.
        ok2, _ = verify_inclusion(leaf_hash(Dn[m_]), m_, n + 1, path, root)
        mut["size_accepted_anyway"] += ok2
        mut["size_checked"] += 1
    for m_ in range(1, n):
        first_hash = MTH(Dn[:m_])
        path = PROOF(m_, Dn)
        check(len(path) <= (n - 1).bit_length() + 1,
              "PROOF(%d,D%d) length %d within ceil(log2 n)+1" % (m_, n, len(path)))
        ok, why = verify_consistency(m_, n, first_hash, root, path)
        check(ok, "consistency accepts PROOF(%d, D%d): %s" % (m_, n, why))
        cons_ok += ok
        cons_bad += (not ok)
        for label, bad in (("short", path[:-1]), ("long", path + [root]),
                           ("empty", [])):
            if label == "short" and not path[:-1]:
                continue  # a one-node proof minus its node is the empty case
            ok2, _ = verify_consistency(m_, n, first_hash, root, bad)
            check(not ok2, "consistency rejects %s path m=%d n=%d" % (label, m_, n))
        ok2, _ = verify_consistency(m_, n, first_hash, bytes(32), path)
        check(not ok2, "consistency rejects wrong second_hash m=%d n=%d" % (m_, n))
        ok2, _ = verify_consistency(m_, n, bytes(32), root, path)
        check(not ok2, "consistency rejects wrong first_hash m=%d n=%d" % (m_, n))
    ok2, _ = verify_consistency(n, n, root, root, [])
    check(not ok2, "consistency rejects first==second (empty path) n=%d" % n)
    ok2, _ = verify_consistency(0, n, HASH(b""), root, PATH(0, Dn) if n > 1 else [])
    check(not ok2, "consistency rejects first==0 n=%d" % n)

# ---- first == second outside the stated domain: what the raw steps do
raw_equal = []
for n in (1, 2, 3, 4, 7, 8):
    root = MTH(LEAVES[:n])
    for label, p in (("empty", []), ("one_node", [root])):
        ok, why = verify_consistency(n, n, root, root, p, enforce_domain=False)
        raw_equal.append({"first": n, "second": n, "path": label,
                          "raw_steps_result": "accept" if ok else "reject",
                          "reason": why})
# the RFC requires an EMPTY proof for first == second (Section 5.3) while
# Section 2.1.4.2 step 1 fails on an empty one: a client must special-case.
check(all(x["raw_steps_result"] == "reject" for x in raw_equal if x["path"] == "empty"),
      "raw steps reject the empty proof that 5.3 requires for first == second")


# ================================================================ wire
def der_len(n):
    if n < 128:
        return bytes([n])
    nb = (n.bit_length() + 7) // 8
    return bytes([0x80 | nb]) + n.to_bytes(nb, "big")


def der_oid_content(arcs):
    out = bytes([40 * arcs[0] + arcs[1]])
    for x in arcs[2:]:
        if x == 0:
            out += b"\x00"
            continue
        seg = []
        while x:
            seg.append(x & 0x7F)
            x >>= 7
        seg.reverse()
        out += bytes([(v | 0x80) if idx < len(seg) - 1 else v
                      for idx, v in enumerate(seg)])
    return out


def prefix_bytes(hi):
    return (hi.bit_length() + 7) // 8


def vec(data, lo, hi):
    """TLS opaque/vector <lo..hi>: length prefix sized by hi, counts BYTES."""
    if not (lo <= len(data) <= hi):
        raise ValueError("vector length %d outside <%d..%d>" % (len(data), lo, hi))
    return len(data).to_bytes(prefix_bytes(hi), "big") + data


def u16(x): return x.to_bytes(2, "big")
def u64(x): return x.to_bytes(8, "big")


def LogID(content): return vec(content, 2, 127)
def NodeHash(h): return vec(h, 32, 2 ** 8 - 1)
def TBSCertificate(t): return vec(t, 1, 2 ** 24 - 1)


def Extension(etype, data):
    return u16(etype) + vec(data, 0, 2 ** 16 - 1)


def ext_vector(exts):
    """Extension x<0..2^16-1>; semantic check of 4.8/4.9 (R-0045, R-0046)."""
    types = [t for t, _ in exts]
    if types != sorted(set(types)):
        raise ValueError("extensions must be unique and ascending by type")
    return vec(b"".join(Extension(t, dta) for t, dta in exts), 0, 2 ** 16 - 1)


def path_vector(nodes):
    return vec(b"".join(NodeHash(x) for x in nodes), 0, 2 ** 16 - 1)


TYPES = {"x509_entry_v2": 0x0100, "precert_entry_v2": 0x0101,
         "x509_sct_v2": 0x0102, "precert_sct_v2": 0x0103,
         "signed_tree_head_v2": 0x0104, "consistency_proof_v2": 0x0105,
         "inclusion_proof_v2": 0x0106}


def TransItem(tname, data):  # no length prefix on data (select, 4.5)
    return u16(TYPES[tname]) + data


def TimestampedCertificateEntryDataV2(ts, issuer_key_hash, tbs, exts):
    return (u64(ts) + vec(issuer_key_hash, 32, 2 ** 8 - 1)
            + TBSCertificate(tbs) + ext_vector(exts))


def SignedCertificateTimestampDataV2(log_id, ts, exts, sig):
    return LogID(log_id) + u64(ts) + ext_vector(exts) + vec(sig, 1, 2 ** 16 - 1)


def TreeHeadDataV2(ts, tree_size, root, exts):
    return u64(ts) + u64(tree_size) + NodeHash(root) + ext_vector(exts)


def SignedTreeHeadDataV2(log_id, tree_head, sig):
    return LogID(log_id) + tree_head + vec(sig, 1, 2 ** 16 - 1)


def ConsistencyProofDataV2(log_id, s1, s2, path):
    return LogID(log_id) + u64(s1) + u64(s2) + path_vector(path)


def InclusionProofDataV2(log_id, tree_size, leaf_index, path):
    return LogID(log_id) + u64(tree_size) + u64(leaf_index) + path_vector(path)


def TransItemList(items):  # items: serialized TransItems
    body = b"".join(vec(x, 1, 2 ** 16 - 1) for x in items)  # SerializedTransItem
    return vec(body, 1, 2 ** 16 - 1)


class WireError(ValueError):
    pass


def take(buf, pos, n):
    if pos + n > len(buf):
        raise WireError("truncated at %d (+%d)" % (pos, n))
    return buf[pos:pos + n], pos + n


def read_vec(buf, pos, lo, hi):
    pb = prefix_bytes(hi)
    raw, pos = take(buf, pos, pb)
    n = int.from_bytes(raw, "big")
    if not (lo <= n <= hi):
        raise WireError("length %d outside <%d..%d>" % (n, lo, hi))
    return take(buf, pos, n)


def parse_ext_vector(buf, pos):
    body, pos = read_vec(buf, pos, 0, 2 ** 16 - 1)
    exts, q, last = [], 0, -1
    while q < len(body):
        t, q = take(body, q, 2)
        t = int.from_bytes(t, "big")
        dta, q = read_vec(body, q, 0, 2 ** 16 - 1)
        if t <= last:
            raise WireError("extensions not unique and ascending")
        last = t
        exts.append((t, dta))
    return exts, pos


def parse_node_vector(buf, pos, hash_size=HASH_SIZE):
    body, pos = read_vec(buf, pos, 0, 2 ** 16 - 1)
    out, q = [], 0
    while q < len(body):
        h_, q = read_vec(body, q, 32, 2 ** 8 - 1)
        if len(h_) != hash_size:
            raise WireError("NodeHash length %d != HASH_SIZE" % len(h_))
        out.append(h_)
    return out, pos


def parse_inclusion(buf):
    lid, p = read_vec(buf, 0, 2, 127)
    ts, p = take(buf, p, 8)
    li, p = take(buf, p, 8)
    path, p = parse_node_vector(buf, p)
    if p != len(buf):
        raise WireError("trailing bytes")
    return lid, int.from_bytes(ts, "big"), int.from_bytes(li, "big"), path


def parse_transitem(buf):
    t, p = take(buf, 0, 2)
    return int.from_bytes(t, "big"), buf[p:]


def parse_transitemlist(buf):
    body, p = read_vec(buf, 0, 1, 2 ** 16 - 1)
    if p != len(buf):
        raise WireError("trailing bytes")
    items, q = [], 0
    while q < len(body):
        it, q = read_vec(body, q, 1, 2 ** 16 - 1)
        items.append(it)
    return items


# ---- wire fixtures. SYNTHETIC inputs, chosen here (the RFC has none):
LOG_OID = [1, 3, 101, 80, 0]  # in the 4-octet Log ID arc (10.2.5 note)
LOG_ID = der_oid_content(LOG_OID)
TS = 1700000000000  # ms since Unix Epoch
ISSUER_KEY_HASH = HASH(b"synthetic issuer SubjectPublicKeyInfo")
TBS = bytes.fromhex("3003020105")  # NOT a real TBSCertificate; 5 opaque bytes
SIG = bytes(range(64))  # NOT a real signature; 64 opaque bytes
entry_data = TimestampedCertificateEntryDataV2(TS, ISSUER_KEY_HASH, TBS, [])
ENTRY = TransItem("x509_entry_v2", entry_data)
LEAF_HASH = leaf_hash(ENTRY)
SCT = TransItem("x509_sct_v2", SignedCertificateTimestampDataV2(LOG_ID, TS, [], SIG))
TREE_HEAD = TreeHeadDataV2(TS + 5000, 7, ROOT, [])
STH = TransItem("signed_tree_head_v2", SignedTreeHeadDataV2(LOG_ID, TREE_HEAD, SIG))
INCL_PATH = PATH(4, D)
INCL = TransItem("inclusion_proof_v2", InclusionProofDataV2(LOG_ID, 7, 4, INCL_PATH))
CONS_PATH = PROOF(3, D)
CONS = TransItem("consistency_proof_v2", ConsistencyProofDataV2(LOG_ID, 3, 7, CONS_PATH))
TIL = TransItemList([SCT, INCL, STH])
EXT_WITH_TYPES = ext_vector([(0xE000, b"\x01"), (0xE001, b"")])


def ext_ext(type_id, tl):  # TLS extension framing (RFC 8446 4.2), informative
    return u16(type_id) + vec(tl, 0, 2 ** 16 - 1)


TLS_EXT_CERT = ext_ext(52, TIL)  # transparency_info = 52 (10.1.1)
TLS_EXT_CH = ext_ext(52, b"")  # ClientHello: empty extension_data
OID_75 = der_oid_content([1, 3, 101, 75])
TIS = b"\x04" + der_len(len(TIL)) + TIL  # TransparencyInformationSyntax
EXTN_VALUE = b"\x04" + der_len(len(TIS)) + TIS  # extnValue OCTET STRING
X509_EXT_BODY = b"\x06" + der_len(len(OID_75)) + OID_75 + EXTN_VALUE
X509_EXT = b"\x30" + der_len(len(X509_EXT_BODY)) + X509_EXT_BODY

# ---- wire self-checks
check(LOG_ID.hex() == "2b655000", "OID 1.3.101.80.0 content is 4 octets (10.2.5 note)")
check(len(der_oid_content([1, 3, 101, 8192])) == 4, "OID 1.3.101.8192 is 4 octets (10.2.5 note)")
check(len(der_oid_content([1, 3, 101, 16383])) == 4, "OID 1.3.101.16383 is 4 octets (10.2.5 note)")
check(len(der_oid_content([1, 3, 101, 80, 127])) == 4, "OID 1.3.101.80.127 is 4 octets (10.2.5 note)")
check(len(der_oid_content([1, 3, 101, 80, 128])) == 5, "OID 1.3.101.80.128 is 5 octets (10.2.5 note)")
check(LogID(LOG_ID) == b"\x04" + LOG_ID, "LogID = 1-byte length + content")
check(b"\x06" + LogID(LOG_ID)[:1] + LogID(LOG_ID)[1:] == bytes.fromhex("06042b655000"),
      "4.4: full DER OID = 0x06 prepended to the opaque vector")
check(OID_75.hex() == "2b654b", "OID 1.3.101.75 content")
check(der_oid_content([1, 3, 101, 78]).hex() == "2b654e", "OID 1.3.101.78 content")
check(len(ENTRY) == 2 + 8 + 1 + 32 + 3 + 5 + 2, "x509_entry_v2 TransItem length")
check(len(INCL) == 2 + 5 + 8 + 8 + 2 + 3 * 33, "inclusion_proof_v2 TransItem length")
lid, tsz, li, path = parse_inclusion(INCL[2:])
check((lid, tsz, li, path) == (LOG_ID, 7, 4, INCL_PATH), "inclusion_proof_v2 round trip")
check(parse_transitem(INCL)[0] == 0x0106, "TransItem type read back")
check(parse_transitemlist(TIL) == [SCT, INCL, STH], "TransItemList round trip")
check(len(TIL) == 2 + sum(2 + len(x) for x in (SCT, INCL, STH)), "TransItemList length")

wire_rejects = []


def must_fail(label, fn):
    try:
        fn()
    except (WireError, ValueError) as ex:
        wire_rejects.append({"case": label, "rejected_by": str(ex)})
        check(True, label)
    else:
        check(False, "should reject: " + label)


must_fail("LogID of 1 octet (<2..127>)", lambda: LogID(b"\x2b"))
must_fail("LogID of 128 octets (<2..127>)", lambda: LogID(bytes(128)))
must_fail("NodeHash of 31 octets (<32..255>)", lambda: NodeHash(bytes(31)))
must_fail("issuer_key_hash of 31 octets", lambda: TimestampedCertificateEntryDataV2(TS, bytes(31), TBS, []))
must_fail("empty TBSCertificate (<1..2^24-1>)", lambda: TBSCertificate(b""))
must_fail("empty signature (<1..2^16-1>)", lambda: SignedCertificateTimestampDataV2(LOG_ID, TS, [], b""))
must_fail("empty TransItemList (<1..2^16-1>)", lambda: TransItemList([]))
must_fail("empty SerializedTransItem (<1..2^16-1>)", lambda: TransItemList([b""]))
must_fail("duplicate extension_type (4.8, R-0045)", lambda: ext_vector([(0xE000, b""), (0xE000, b"")]))
must_fail("extensions out of order (4.8, R-0046)", lambda: ext_vector([(0xE001, b""), (0xE000, b"")]))
must_fail("extension_data over 2^16-1", lambda: Extension(0xE000, bytes(65536)))
must_fail("truncated inclusion proof", lambda: parse_inclusion(INCL[2:-1]))
must_fail("inclusion proof with trailing byte", lambda: parse_inclusion(INCL[2:] + b"\x00"))
must_fail("parse: LogID length byte 1", lambda: parse_inclusion(b"\x01\x2b" + INCL[2 + 5:]))
must_fail("parse: NodeHash of 31 octets in path",
          lambda: parse_inclusion(INCL[2:2 + 5 + 16] + u16(32) + b"\x1f" + bytes(31)))
must_fail("parse: path vector with a stray octet after a NodeHash",
          lambda: parse_inclusion(INCL[2:2 + 5 + 16] + u16(34) + b"\x20" + bytes(32) + b"\x00"))
must_fail("parse: TransItemList trailing byte", lambda: parse_transitemlist(TIL + b"\x00"))
check(vec(b"", 0, 2 ** 16 - 1) == b"\x00\x00", "empty extension vector is 0000")
# 6.5 tension: 'MAY send it with an empty array' vs trans_item_list<1..2^16-1>
check(TLS_EXT_CH.hex() == "00340000", "ClientHello transparency_info: type 0x0034, length 0")


def b64(x): return base64.b64encode(x).decode()


# ================================================================ fixtures
def J(obj):
    return json.dumps(obj, indent=2, ensure_ascii=False) + "\n"


HDR = ("DERIVED, not verbatim. Written by this library by examples/reproduce.py; "
       "RFC 9162 prints tree structure (Section 2.1.5) and no hash values. "
       "Inputs d[i] = bytes([i]) i=0..6 and HASH = SHA-256 are chosen here. "
       "Regenerate with: python3 -I reproduce.py --write")


def fx_tree():
    return {
        "_comment": HDR,
        "source": {"locator": "§2.1.5", "source_lines": "580-646",
                   "fixtures": ["fig-11.verbatim.txt", "fig-12.verbatim.txt"]},
        "hash": "SHA-256", "hash_size": HASH_SIZE,
        "leaf_prefix_hex": "00", "node_prefix_hex": "01",
        "choice": "d[i] = bytes([i]); the RFC names d0..d6 and gives no values",
        "d_hex": [hx(x) for x in D],
        "node_definitions": {
            "a": "leaf hash of d0", "b": "leaf hash of d1", "c": "leaf hash of d2",
            "d": "leaf hash of d3", "e": "leaf hash of d4", "f": "leaf hash of d5",
            "j": "leaf hash of d6 (the figure hangs d6 under j)",
            "g": "node(a,b)", "h": "node(c,d)", "i": "node(e,f)",
            "k": "node(g,h)", "l": "node(i,j)", "hash": "node(k,l), tree_size 7",
            "hash0": "tree_size 3 = node(g,c)", "hash1": "tree_size 4 = k",
            "hash2": "tree_size 6 = node(k,i)"},
        "values_hex": {nm: hx(NODES[nm]) for nm in
                       ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
                        "hash", "hash0", "hash1", "hash2"]},
        "empty_tree_hash_hex": hx(HASH(b"")),
        "tree_size": {"hash": 7, "hash0": 3, "hash1": 4, "hash2": 6},
    }


def inc_case(m_, expect, label=None, **over):
    path = PATH(m_, D)
    case = {"name": label or "inclusion d%d in tree of 7" % m_,
            "source": "§2.1.5 L%s" % {0: "600", 3: "602", 4: "604", 6: "606"}[m_],
            "leaf_index": m_, "tree_size": 7, "leaf_hash_hex": hx(leaf_hash(D[m_])),
            "path_names": names(path), "path_hex": [hx(x) for x in path],
            "root_hash_hex": hx(ROOT), "expected": expect}
    case.update(over)
    return case


def fx_inclusion():
    pos = [inc_case(m_, "accept") for m_ in (0, 3, 4, 6)]
    for case in pos:
        case["rfc_prints_path"] = RFC_INCLUSION[case["leaf_index"]]
        ok, why = verify_inclusion(bytes.fromhex(case["leaf_hash_hex"]), case["leaf_index"],
                                   7, [bytes.fromhex(x) for x in case["path_hex"]], ROOT)
        check(ok, "fixture " + case["name"] + " verifies: " + why)
    neg = []

    def add(name, leaf_index, tree_size, leaf_h, path, root, why_expected):
        ok, why = verify_inclusion(leaf_h, leaf_index, tree_size, path, root)
        check(not ok, "reject: " + name)
        neg.append({"name": name, "leaf_index": leaf_index, "tree_size": tree_size,
                    "leaf_hash_hex": hx(leaf_h), "path_hex": [hx(x) for x in path],
                    "root_hash_hex": hx(root), "expected": "reject",
                    "rule": why_expected, "failed_at": why})

    p0 = PATH(0, D)
    add("leaf_index equals tree_size", 7, 7, leaf_hash(D[6]), PATH(6, D), ROOT, "2.1.3.2 step 1")
    add("leaf_index above tree_size", 9, 7, leaf_hash(D[6]), PATH(6, D), ROOT, "2.1.3.2 step 1")
    add("tree_size 0", 0, 0, leaf_hash(D[0]), [], HASH(b""), "2.1.3.2 step 1")
    add("path one node short (d0: [b,h])", 0, 7, leaf_hash(D[0]), p0[:-1], ROOT, "2.1.3.2 step 5 (sn not 0)")
    add("path empty for tree of 7", 0, 7, leaf_hash(D[0]), [], ROOT, "2.1.3.2 step 5 (sn not 0)")
    add("path one node long (d0: [b,h,l,l])", 0, 7, leaf_hash(D[0]), p0 + [l], ROOT, "2.1.3.2 step 4a")
    add("d6 path too long ([i,k,k])", 6, 7, leaf_hash(D[6]), PATH(6, D) + [k], ROOT, "2.1.3.2 step 4a")
    add("d3 path with first two nodes swapped ([g,c,l])", 3, 7, leaf_hash(D[3]),
        [g, c, l], ROOT, "root differs (node order matters)")
    add("wrong root_hash (hash2 for a tree of 7)", 0, 7, leaf_hash(D[0]), p0, hash2, "root differs")
    add("wrong leaf hash (d1 hashed, index 0)", 0, 7, leaf_hash(D[1]), p0, ROOT, "root differs")
    add("leaf input not hashed with 0x00 prefix", 0, 7, HASH(D[0]), p0, ROOT, "root differs (domain separation)")
    pos.append({"name": "single-leaf tree: empty path", "leaf_index": 0, "tree_size": 1,
                "leaf_hash_hex": hx(leaf_hash(D[0])), "path_hex": [],
                "root_hash_hex": hx(leaf_hash(D[0])), "expected": "accept",
                "source": "§2.1.3.1 PATH(0, {d[0]}) = {}"})
    ok, _ = verify_inclusion(leaf_hash(D[0]), 0, 1, [], leaf_hash(D[0]))
    check(ok, "single-leaf tree verifies with empty path")
    D3 = LEAVES[:3]
    okx, _ = verify_inclusion(leaf_hash(D3[0]), 0, 4, PATH(0, D3), MTH(D3))
    check(okx, "observation: tree_size 4 accepted for a proof built for tree_size 3")
    obs = {"tree_size_not_bound_by_root_hash": {
        "note": "2.1.3.2 uses tree_size only through sn. The same leaf, path and root verify "
                "with tree_size 3 and with tree_size 4 here, so the root hash alone does not "
                "commit to tree_size; the signed STH does (4.9, 4.10). A verifier must take "
                "tree_size and root_hash from the same signed STH.",
        "leaf_input_hex": hx(D3[0]), "leaf_index": 0, "path_hex": [hx(x) for x in PATH(0, D3)],
        "root_hash_hex": hx(MTH(D3)), "true_tree_size": 3, "also_accepted_with_tree_size": 4}}
    return {"_comment": HDR, "algorithm": "§2.1.3.2 steps 1-5 as printed",
            "accept": pos, "reject": neg, "observations": obs}


def fx_consistency():
    pos = []
    for m_ in (3, 4, 6):
        nm, fh = RFC_CONS_HASH[m_]
        path = PROOF(m_, D)
        ok, why = verify_consistency(m_, 7, fh, ROOT, path)
        check(ok, "consistency fixture %s verifies: %s" % (nm, why))
        pos.append({"name": "%s (size %d) to hash (size 7)" % (nm, m_),
                    "source": "§2.1.5 L%s" % {3: "636", 4: "641", 6: "644"}[m_],
                    "first": m_, "second": 7, "first_hash_name": nm,
                    "first_hash_hex": hx(fh), "second_hash_hex": hx(ROOT),
                    "path_names": names(path), "path_hex": [hx(x) for x in path],
                    "rfc_prints_path": RFC_CONSISTENCY[m_], "expected": "accept"})
    neg = []

    def add(name, first, second, fh, sh, path, rule, domain=True):
        ok, why = verify_consistency(first, second, fh, sh, path, enforce_domain=domain)
        check(not ok, "reject: " + name)
        neg.append({"name": name, "first": first, "second": second,
                    "first_hash_hex": hx(fh), "second_hash_hex": hx(sh),
                    "path_hex": [hx(x) for x in path], "expected": "reject",
                    "rule": rule, "failed_at": why})

    P3 = PROOF(3, D)
    add("empty consistency_path", 3, 7, hash0, ROOT, [], "2.1.4.2 step 1")
    add("first equals second, empty path", 7, 7, ROOT, ROOT, [], "2.1.4.2 stated domain 0 < first < second; step 1")
    add("first equals second, power of two, empty path", 4, 4, hash1, hash1, [], "2.1.4.2 stated domain; step 1")
    add("first greater than second", 7, 3, ROOT, hash0, P3, "2.1.4.2 stated domain 0 < first < second")
    add("first is zero", 0, 7, HASH(b""), ROOT, P3, "2.1.4.2 stated domain 0 < first")
    add("proof one node short ([c,d,g])", 3, 7, hash0, ROOT, P3[:-1], "2.1.4.2 step 7 (sr differs)")
    add("proof one node long ([c,d,g,l,l])", 3, 7, hash0, ROOT, P3 + [l], "2.1.4.2 step 6a")
    add("proof nodes swapped ([d,c,g,l])", 3, 7, hash0, ROOT, [d, c, g, l], "2.1.4.2 step 7 (fr differs)")
    add("wrong first_hash (hash1 for size 3)", 3, 7, hash1, ROOT, P3, "2.1.4.2 step 7 (fr differs)")
    add("wrong second_hash (hash2 for size 7)", 3, 7, hash0, hash2, P3, "2.1.4.2 step 7 (sr differs)")
    add("size 4 proof [l] given first_hash of size 3", 4, 7, hash0, ROOT, [l], "2.1.4.2 step 7 (sr differs; fr is the prepended first_hash)")
    return {"_comment": HDR, "algorithm": "§2.1.4.2 steps 1-7 as printed",
            "accept": pos, "reject": neg,
            "first_equals_second_outside_stated_domain": {
                "note": "Section 5.3 requires an EMPTY consistency proof when first and second are equal; "
                        "Section 2.1.4.2 step 1 fails on an empty one and the section is stated for "
                        "0 < first < second. A client must compare the two hashes directly.",
                "raw_steps_run_without_the_domain_guard": raw_equal}}


def fx_wire():
    return {
        "_comment": HDR + ". Wire inputs are SYNTHETIC: tbs_certificate is 5 opaque bytes "
                   "and the signature is 64 opaque bytes, neither valid; the log id is "
                   "OID 1.3.101.80.0 chosen from the arc the RFC sets aside (10.2.5).",
        "source": {"locator": "§4.4-§4.12, §6.3, §6.5, §7.1"},
        "log_oid": ".".join(map(str, LOG_OID)), "timestamp_ms": TS,
        "vectors": [
            {"name": "LogID", "locator": "§4.4",
             "hex": hx(LogID(LOG_ID)), "note": "04 + 4 octets of OID content; 0x06 prepended gives the full DER OID"},
            {"name": "TimestampedCertificateEntryDataV2", "locator": "§4.7",
             "hex": hx(entry_data), "tbs_certificate_hex": hx(TBS),
             "issuer_key_hash_hex": hx(ISSUER_KEY_HASH)},
            {"name": "TransItem x509_entry_v2", "locator": "§4.5, §4.7",
             "hex": hx(ENTRY), "leaf_hash_hex": hx(LEAF_HASH),
             "note": "leaf hash = HASH(0x00 || TransItem), including the 2-octet versioned_type"},
            {"name": "TransItem x509_sct_v2", "locator": "§4.8", "hex": hx(SCT),
             "signature_hex": hx(SIG), "signed_input": "TransItem x509_entry_v2 above (4.8)"},
            {"name": "TreeHeadDataV2", "locator": "§4.9", "hex": hx(TREE_HEAD),
             "tree_size": 7, "root_hash_hex": hx(ROOT)},
            {"name": "TransItem signed_tree_head_v2", "locator": "§4.10", "hex": hx(STH),
             "signed_input": "the TreeHeadDataV2 vector above (4.10: computed over the tree_head field)"},
            {"name": "TransItem inclusion_proof_v2 (d4, tree 7)", "locator": "§4.12, §2.1.5",
             "hex": hx(INCL), "inclusion_path_names": names(INCL_PATH)},
            {"name": "TransItem consistency_proof_v2 (3 to 7)", "locator": "§4.11, §2.1.5",
             "hex": hx(CONS), "consistency_path_names": names(CONS_PATH)},
            {"name": "Extension vector, two extensions", "locator": "§4.6, §4.8",
             "hex": hx(EXT_WITH_TYPES), "note": "types 0xE000 then 0xE001 (experimental range); ascending"},
            {"name": "TransItemList [sct, inclusion, sth]", "locator": "§6.3",
             "hex": hx(TIL), "note": "2-octet list length, then each item with its own 2-octet length"},
            {"name": "transparency_info TLS extension, Certificate (TLS 1.3)", "locator": "§6.5, §10.1.1",
             "hex": hx(TLS_EXT_CERT), "note": "extension_type 52 = 0x0034, 2-octet length, TransItemList; "
             "the outer TLS extension framing is RFC 8446 4.2, not this document"},
            {"name": "transparency_info TLS extension, ClientHello", "locator": "§8.1.1, §6.5",
             "hex": hx(TLS_EXT_CH), "note": "empty extension_data"},
            {"name": "TransparencyInformationSyntax (DER OCTET STRING)", "locator": "§7.1",
             "hex": hx(TIS), "note": "04 len || TransItemList"},
            {"name": "Transparency Information X.509v3 Extension (DER)", "locator": "§7.1",
             "hex": hx(X509_EXT),
             "note": "SEQUENCE { OID 1.3.101.75, extnValue OCTET STRING { OCTET STRING { TransItemList } } }; "
                     "critical is FALSE (the DEFAULT) so DER omits it"},
        ],
        "reject": wire_rejects,
    }


def fx_api():
    b = b64
    return {
        "_comment": HDR + ". Wire inputs are SYNTHETIC (see wire-vectors.derived.json). The JSON "
                   "shapes follow Section 5; base64 is RFC 4648 Section 4.",
        "source": {"locator": "§5.1-§5.7"},
        "samples": [
            {"endpoint": "submit-entry", "direction": "request", "locator": "§5.1",
             "instance": {"submission": b(TBS), "type": 1, "chain": [b(bytes([1, 2, 3]))]}},
            {"endpoint": "submit-entry", "direction": "response", "locator": "§5.1",
             "instance": {"sct": b(SCT), "sth": b(STH), "inclusion": b(INCL)}},
            {"endpoint": "get-sth", "direction": "response", "locator": "§5.2",
             "instance": {"sth": b(STH)}},
            {"endpoint": "get-sth-consistency", "direction": "response", "locator": "§5.3",
             "instance": {"consistency": b(CONS), "sth": b(STH)}},
            {"endpoint": "get-proof-by-hash", "direction": "response", "locator": "§5.4",
             "instance": {"inclusion": b(INCL), "sth": b(STH)}},
            {"endpoint": "get-all-by-hash", "direction": "response", "locator": "§5.5",
             "instance": {"inclusion": b(INCL), "sth": b(STH), "consistency": b(CONS)}},
            {"endpoint": "get-entries", "direction": "response", "locator": "§5.6",
             "instance": {"entries": [{"log_entry": b(ENTRY),
                                       "submitted_entry": {"submission": b(TBS), "type": 1,
                                                           "chain": [b(bytes([9, 9]))]},
                                       "sct": b(SCT)}],
                          "sth": b(STH)}},
            {"endpoint": "get-anchors", "direction": "response", "locator": "§5.7",
             "instance": {"certificates": [b(bytes([1, 2, 3])), b(bytes([4, 5, 6]))],
                          "max_chain_length": 5}},
        ],
    }


FIXTURES = {
    "merkle-7leaf.derived.json": fx_tree(),
    "inclusion-proofs.derived.json": fx_inclusion(),
    "consistency-proofs.derived.json": fx_consistency(),
    "wire-vectors.derived.json": fx_wire(),
    "api-samples.derived.json": fx_api(),
}

for fname, obj in FIXTURES.items():
    path = os.path.join(HERE, fname)
    text = J(obj)
    if "--write" in ARGS:
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(text)
    try:
        with open(path, encoding="utf-8") as fh:
            on_disk = fh.read()
    except FileNotFoundError:
        on_disk = None
    check(on_disk == text, "fixture on disk equals rebuilt: " + fname)

print("exhaustive: inclusion accepted %d/%d proofs (n=1..65); consistency accepted %d/%d (0<m<n<=65)"
      % (inc_ok, inc_ok + inc_bad, cons_ok, cons_ok + cons_bad))
print("inclusion mutations rejected:", mut)
print("wire reject cases:", len(wire_rejects))
print("checks run: %d, failed: %d" % (CHECKS[0], len(FAILS)))
sys.exit(1 if FAILS else 0)

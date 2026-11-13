#!/usr/bin/env python3
"""DERIVED - not verbatim. MUST-accept / MUST-reject cases for the S-expression
reader (spki_sexp.derived.py) and the BNF checker (spki_bnf.derived.py), plus a
mutation harness that shows the reject cases bind.

    python3 -I test_spki.derived.py            # run the cases
    python3 -I test_spki.derived.py --mutate   # run the cases against mutants

Every case cites the sentence of the draft that makes it a MUST case;
test_basis.derived.py joins each case to the requirement ids in
../requirements.yaml that state that rule. A case
marked [assumption] rests on a choice listed in spki_sexp.derived.py's
docstring, not on the draft.
"""
import ast
import importlib.util
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent


def load(name, fname, src=None):
    spec = importlib.util.spec_from_file_location(name, HERE / fname)
    mod = importlib.util.module_from_spec(spec)
    if src is not None:
        exec(compile(src, fname, "exec"), mod.__dict__)
    else:
        spec.loader.exec_module(mod)
    return mod


# ---------------------------------------------------------------- canonical
CANON_ACCEPT = [
    (b"(4:test26:abcdefghijklmnopqrstuvwxyz5:123455::: ::)", "3.4 the draft's own example"),
    (b"(1:a)", "3.3 a list of one byte string"),
    (b"(1:a(1:b)(1:c1:d))", "3.3 nested lists"),
    (b"(1:a0:)", "3.2 <decimal> may be \"0\": the empty byte string"),
    (b"(1:a10:0123456789)", "3.2 multi-digit length"),
    (b"(1:a3:(())", "3.2 bytes are binary; parens inside a string are data"),
    (b"(1:a1::)", "3.2 ':' is a legal data byte"),
    (b"(1:a[3:gif]3:xyz)", "3.2 <display-type> then <bytes>"),
    (b"([4:text]4:type1:x)", "3.2 a display type on the first element"),
    (b"(1:a[0:]1:x)", "3.2 empty display type is <bytes> with length 0"),
    (b"(0:)", "3.3 the first element is a byte string; it may be empty"),
]
CANON_REJECT = [
    (b"", "empty input"),
    (b"()", "3: no empty lists"),
    (b"(", "unterminated"),
    (b")", "no list"),
    (b"(1:a", "unterminated list"),
    (b"(1:a))", "trailing ')'"),
    (b"(1:a)x", "trailing byte"),
    (b"(1:a) ", "3.1: no white space in canonical form"),
    (b" (1:a)", "leading white space"),
    (b"(1:a 1:b)", "white space between elements"),
    (b"(01:a)", "3.1: no unnecessary leading 0 digits"),
    (b"(00:)", "3.1: leading zeros, even on zero"),
    (b"(1:ab)", "length 1 then a stray byte"),
    (b"(2:a)", "length runs past the end"),
    (b"(2:a)b", "length runs past the list close"),
    (b"((1:a))", "3.3: the first element must be a byte string"),
    (b"(-1:a)", "3.1: non-negative"),
    (b"(1a)", "missing ':'"),
    (b"(:a)", "missing length"),
    (b"(1:a:1:b)", "colon without a length"),
    (b"(1:a[1:x])", "3.2: a display type must be followed by <bytes>"),
    (b"(1:a[1:x][1:y]1:z)", "3.2: one display type only"),
    (b"(1:a[x]1:z)", "3.2: the display type is <bytes>, not a bare token"),
    (b"(1:a[[1:x]1:y]1:z)", "3.2: display types do not nest"),
    (b"(1:a1:)", "length 1 consumes the ')'; list unterminated"),
    (b"(99999999999999999999:a)", "length past the input"),
    (b"[1:x]", "top level must be an <s-expr> (a list), not a bare string"),
    (b"(1:a(1:b)", "inner list closed, outer not"),
]

# ----------------------------------------------------------------- advanced
ADV_ACCEPT = [
    ('(test abcdefghijklmnopqrstuvwxyz "12345" ":: ::")', b"(4:test26:abcdefghijklmnopqrstuvwxyz5:123455::: ::)", "3.4 the draft's advanced form of its canonical example"),
    ("(a b)", b"(1:a1:b)", "3.4 tokens"),
    ("( a   b\n\tc )", b"(1:a1:b1:c)", "3.6 white space between elements is ignored"),
    ('(a "x y")', b"(1:a3:x y)", "3.6 quoted string"),
    ('(a "\\n\\x41\\101")', b"(1:a3:\nAA)", "3.6 C string escapes [assumption A2]"),
    ("(a #4142#)", b"(1:a2:AB)", "3.6 hex delimited by #"),
    ("(a #41 42\n43#)", b"(1:a3:ABC)", "3.6 white space inside hex [assumption]"),
    ("(a |QUJD|)", b"(1:a3:ABC)", "3.6 base64 delimited by |"),
    ("(a |QU\nJD|)", b"(1:a3:ABC)", "3.6 white space inside base64"),
    ("(a (b (c)))", b"(1:a(1:b(1:c)))", "3.3 nesting"),
    ("(tag (*))", b"(3:tag(1:*))", "4.8 the (*) form is a list holding the string *"),
    ("(a [text/plain]x)", b"(1:a[10:text/plain]1:x)", "3.2 display type [assumption A4]"),
    ("(a http://example.org/x)", b"(1:a20:http://example.org/x)", "tokens carry ':' and '/' [assumption A1; the draft's ACL example needs it]"),
    ("(a 3:abc)", b"(1:a3:abc)", "length-prefixed raw string [assumption A3]"),
]
ADV_REJECT = [
    ("()", "3: no empty lists"),
    ("(a", "unterminated"),
    ("a", "not a list"),
    ("((a))", "3.3: first element a byte string"),
    ("(1abc)", "3.4: tokens may not start with a digit"),
    ('(a "x)', "unterminated quoted string"),
    ('(a "\\q")', "unknown escape [assumption A2]"),
    ("(a #abc#)", "odd number of hex digits"),
    ("(a #zz#)", "non-hex digits"),
    ("(a |!!!|)", "not base64"),
    ("(a |QUJ|)", "base64 without padding [assumption A5]"),
    ("(a) (b)", "two S-expressions where one is required"),
    ("(a #41", "unterminated hex"),
    ("(a |QUJD", "unterminated base64"),
    ("(a [x)", "unterminated display type"),
    ("(a 5:abc)", "raw length past the input"),
]

# ---------------------------------------------------------------- transport
TRANSPORT_ACCEPT = [
    ("{KDQ6dGVzdDI2OmFiY2RlZmdoaWprbG1ub3BxcnN0dXZ3eHl6NToxMjM0NTU\n6OjogOjop}", b"(4:test26:abcdefghijklmnopqrstuvwxyz5:123455::: ::)", "3.4 the draft's base64 of its example, line-broken"),
    ("{KDE6YSk=}", b"(1:a)", "3.4 base64 of (1:a)"),
]
TRANSPORT_REJECT = [
    ("KDE6YSk=", "3.4: the base64 is enclosed in braces"),
    ("{KDE6YSk=", "unterminated"),
    ("{KDE6YSk}", "padding missing [assumption A5]"),
    ("{KDE6YSk=!}", "character outside the alphabet [assumption A5]"),
    ("{KDE6}", "decodes to (1: which is not canonical"),
    ("{KDE6YSkp}", "decodes to canonical plus a trailing byte"),
    ("{}", "empty"),
    ("{" + "KCkp" + "}", "decodes to () : an empty list"),
]

INT_CASES = [  # 3.2.1
    (b"\x00", 0), (b"\xff", -1), (b"\x00\xff", 255), (b"\x80", -128), (b"\x03", 3),
    (b"\x00\xd1\xc2", 0xd1c2), (b"\x01\x00", 256),
]
INT_ENCODE = [(0, b"\x00"), (-1, b"\xff"), (255, b"\x00\xff"), (128, b"\x00\x80"), (-128, b"\x80"), (256, b"\x01\x00")]
DATE_ACCEPT = ["1997-07-26_23:15:10", "2001-01-01_00:00:00"]  # 4.9.1's two examples
DATE_REJECT = ["1997-07-26 23:15:10", "1997-07-26T23:15:10", "1997-13-01_00:00:00", "97-07-26_23:15:10",
               "1997-07-26_24:00:00", "1997-07-26_23:15", "1997-07-26_23:15:10Z", ""]


# ----------------------------------------------- cases added after mutation
# (each kills a mutant of spki_sexp.derived.py or of a section 9.2 production
# that the first set of cases let survive)
_ESC_CASES = [(r'\a', 7), (r'\b', 8), (r'\f', 12), (r'\n', 10), (r'\r', 13), (r'\t', 9), (r'\v', 11),
              (r'\\', 92), (r'\"', 34), (r"\'", 39), (r'\?', 63), (r'\101', 65), (r'\x41', 65),
              (r'\377', 255), (r'\7', 7), (r'\1012', None)]
for _e, _v in _ESC_CASES:
    _canon = b"(1:x2:A2)" if _v is None else b"(1:x1:" + bytes([_v]) + b")"
    ADV_ACCEPT.append(('(x "' + _e + '")', _canon, "3.6 quoted strings follow C string rules [assumption A2]"))
ADV_ACCEPT += [
    ("(x 3:abc)", b"(1:x3:abc)", "[assumption A3] length-prefixed string in advanced form"),
    ("(x [gif]\"abc\")", b"(1:x[3:gif]3:abc)", "3.2 display type before the string [assumption A4]"),
    ("(x #41 42#)", b"(1:x2:AB)", "3.6 hex with white space inside"),
    ("(x |QUJD|)", b"(1:x3:ABC)", "3.6 base64 value"),
    ("(x a1)", b"(1:x2:a1)", "3.4 a token may contain a digit after its first character"),
    ("(x)", b"(1:x)", "3.3 a list of one byte string"),
]
ADV_REJECT += [
    (r'(x "\400")', "3.6 octal escape above 255 [assumption A2]"),
    (r'(x "\x4")', "3.6 \\x takes two hex digits [assumption A2]"),
    (r'(x "\xZ1")', "3.6 \\x takes hex digits [assumption A2]"),
    (r'(x "\q")', "3.6 unknown escape [assumption A2]"),
    ('(x "abc', "unterminated quoted string"),
    ("(x 3:ab)", "advanced 3:ab: the length runs past the list"),
    ("(x 03:abc)", "3.4 tokens do not start with a digit; 03 is not a length"),
    ("(x #4g#)", "3.6 non-hex digit"),
    ("(x #414#)", "3.6 odd number of hex digits"),
    ("(x |QUJ|)", "base64 not padded [assumption A5]"),
    ("(x |QU#D|)", "base64 alphabet [assumption A5]"),
    ("(x 007)", "3.4 token starting with a digit"),
    ("(x 1a)", "3.4 token starting with a digit"),
    ("(x [])", "3.2 empty display type needs <bytes>"),
    ("(x [a)", "unterminated display type"),
    ("(x (y)) z", "trailing text"),
]
DATE_CASES = [
    ("2001-12-31_23:59:59", True), ("2001-01-01_00:00:00", True), ("2001-00-01_00:00:00", False),
    ("2001-13-01_00:00:00", False), ("2001-01-00_00:00:00", False), ("2001-01-32_00:00:00", False),
    ("2001-01-01_24:00:00", False), ("2001-01-01_00:60:00", False), ("2001-01-01_00:00:60", False),
    ("2001-01-01 00:00:00", False), ("2001-01-01_00:00", False), ("", False),
]

import json

REASONS_FILE = HERE / "reject-reasons.derived.json"
GOLD = json.loads(REASONS_FILE.read_text()) if REASONS_FILE.exists() else None
SEEN_REASONS = {}


def reason_ok(key, e):
    """A reject case binds to WHY the input is rejected, not just that it is:
    the error text must equal the one recorded in reject-reasons.derived.json
    (reviewed against each case's cited sentence; --write-reasons rewrites it)."""
    SEEN_REASONS[key] = str(e)
    return GOLD is None or GOLD.get(key) == str(e)


def run_sexp(sx):
    """-> (cases run, [failures])"""
    n, fails = 0, []

    def case(name, ok):
        nonlocal n
        n += 1
        if not ok:
            fails.append(name)

    for b, why in CANON_ACCEPT:
        try:
            node = sx.parse_canonical(b)
            case(f"accept canonical {b!r} ({why})", sx.encode(node) == b)
        except sx.SexpError:
            case(f"accept canonical {b!r} ({why})", False)
    for b, why in CANON_REJECT:
        try:
            sx.parse_canonical(b)
            case(f"reject canonical {b!r} ({why})", False)
        except sx.SexpError as e:
            case(f"reject canonical {b!r} ({why})", reason_ok(f"canonical|{b!r}", e))
    for t, canon, why in ADV_ACCEPT:
        try:
            case(f"accept advanced {t!r} ({why})", sx.encode(sx.parse_advanced(t)) == canon)
        except sx.SexpError:
            case(f"accept advanced {t!r} ({why})", False)
    for t, why in ADV_REJECT:
        try:
            sx.parse_advanced(t)
            case(f"reject advanced {t!r} ({why})", False)
        except sx.SexpError as e:
            case(f"reject advanced {t!r} ({why})", reason_ok(f"advanced|{t!r}", e))
    for t, canon, why in TRANSPORT_ACCEPT:
        try:
            case(f"accept transport {t!r} ({why})", sx.encode(sx.parse_transport(t)) == canon)
        except sx.SexpError:
            case(f"accept transport {t!r} ({why})", False)
    for t, why in TRANSPORT_REJECT:
        try:
            sx.parse_transport(t)
            case(f"reject transport {t!r} ({why})", False)
        except sx.SexpError as e:
            case(f"reject transport {t!r} ({why})", reason_ok(f"transport|{t!r}", e))
    # round trips
    for b, _ in CANON_ACCEPT:
        node = sx.parse_canonical(b)
        case(f"roundtrip advanced {b!r}", sx.encode(sx.parse_advanced(sx.to_advanced(node))) == b)
        case(f"roundtrip transport {b!r}", sx.encode(sx.parse_transport(sx.encode_transport(node))) == b)
    # display type is part of equality (3.2)
    a1 = sx.parse_canonical(b"(1:a[3:gif]3:xyz)").items[1]
    a2 = sx.parse_canonical(b"(1:a3:xyz)").items[1]
    case("3.2 same bytes, different display types are unequal", a1 != a2)
    case("3.2 same bytes, same display type are equal", a1 == sx.parse_canonical(b"(1:a[3:gif]3:xyz)").items[1])
    case("3.2 display type survives encode", sx.encode(sx.Lst((sx.Atom(b"a"), a1))) == b"(1:a[3:gif]3:xyz)")
    for d, ok in DATE_CASES:
        try:
            sx.check_date(sx.Atom(d.encode()))
            case(f"4.9.1 date {d!r} accepted", ok)
        except sx.SexpError:
            case(f"4.9.1 date {d!r} rejected", not ok)
    # API edges (added after mutation)
    case("allow_atom: a bare byte string is accepted when asked", sx.parse_canonical(b"3:abc", allow_atom=True) == sx.Atom(b"abc"))
    try:
        sx.parse_canonical(b"3:abc")
        case("a bare byte string is not an S-expression (3.3)", False)
    except sx.SexpError:
        case("a bare byte string is not an S-expression (3.3)", True)
    try:
        sx.parse_canonical(b"3:abcd", allow_atom=True)
        case("allow_atom: trailing bytes rejected", False)
    except sx.SexpError:
        case("allow_atom: trailing bytes rejected", True)
    try:
        sx.parse_canonical("(1:a)")
        case("canonical input must be bytes", False)
    except TypeError:
        case("canonical input must be bytes", True)
    case("transport output can wrap at a width", sx.encode_transport(sx.parse_canonical(b"(1:a)"), 4) == "{KDE6\nYSk=}")
    case("wrapped transport output parses back", sx.encode(sx.parse_transport("{KDE6\nYSk=}")) == b"(1:a)")
    try:
        sx.decode_integer(sx.Lst((sx.Atom(b"a"),)))
        case("3.2.1: a list is not an integer", False)
    except sx.SexpError:
        case("3.2.1: a list is not an integer", True)
    try:
        sx.check_date(sx.Atom("2001-01-01_00:00:\u00e900".encode("utf-8")))
        case("4.9.1: a non-ASCII date is rejected", False)
    except sx.SexpError:
        case("4.9.1: a non-ASCII date is rejected", True)
    # integers
    for b, v in INT_CASES:
        case(f"3.2.1 integer {b.hex()} = {v}", sx.decode_integer(sx.Atom(b)) == v)
    for v, b in INT_ENCODE:
        case(f"3.2.1 encode integer {v}", sx.encode_integer(v).data == b)
    try:
        sx.decode_integer(sx.Atom(b""))
        case("3.2.1 empty string is not the integer 0", False)
    except sx.SexpError:
        case("3.2.1 empty string is not the integer 0", True)
    for d in DATE_ACCEPT:
        try:
            sx.check_date(sx.Atom(d.encode()))
            case(f"4.9.1 date {d}", True)
        except sx.SexpError:
            case(f"4.9.1 date {d}", False)
    for d in DATE_REJECT:
        try:
            sx.check_date(sx.Atom(d.encode()))
            case(f"4.9.1 bad date {d!r}", False)
        except sx.SexpError:
            case(f"4.9.1 bad date {d!r}", True)
    try:
        sx.check_date(sx.Atom(b"2001-01-01_00:00:00", b"text"))
        case("4.9.1 a date with a display type is rejected [assumption]", False)
    except sx.SexpError:
        case("4.9.1 a date with a display type is rejected [assumption]", True)
    return n, fails


# --------------------------------------------------------------------- BNF
PK = "(public-key (rsa-pkcs1-sha1 (e #11#) (n #00c1#)))"
H = "(hash md5 #00112233445566778899aabbccddeeff#)"
SIG = f"(signature {H} {PK} (rsa-pkcs1-sha1 #0102#))"
C_MIN = f"(cert (issuer {PK}) (subject {PK}) (tag (*)))"
C_FULL = (f"(cert (version \"0\") (display \"hint\") (issuer {H}) (issuer-info (uri http://a/)) "
          f"(subject {PK}) (subject-info (uri http://b/ http://c/)) (propagate) (tag (ftp host (* set a b))) "
          f"(valid (not-before \"1997-07-26_23:15:10\") (not-after \"2001-01-01_00:00:00\")) (comment \"c\"))")
NC = f"(cert (issuer (name {PK} fred)) (subject (name sam)) (valid (not-after \"2001-01-01_00:00:00\")))"


def sub(obj):
    return f"(cert (issuer {PK}) (subject {obj}) (tag (*)))"


# (rule, text, why)
BNF_ACCEPT = [
    ("pub-key", PK, "3.8.1 pub-key with algorithm id and parameter lists"),
    ("pub-key", PK[:-1] + " (uri http://k/))", "3.8.1 pub-key with <uris>"),
    ("pub-key", "(public-key (dsa-sha1 (p #01#) (g #02#) (q #03#) (y #04#)))", "3.8.1.2 dsa-sha1"),
    ("pub-key", "(public-key (http://example.org/alg (x y)))", "<pub-sig-alg-id> may be a <uri>"),
    ("hash", H, "3.8.2 hash"),
    ("hash", "(hash sha1 #00# (uri http://x/))", "3.8.2 hash with <uris>"),
    ("hash", "(hash http://example.org/h #00#)", "<hash-alg-name> may be a <uri>"),
    ("signature", SIG, "3.8.3 signature"),
    ("signature", f"(signature {H} {PK} (dsa-sha1 (r #01#) (s #02#)))", "3.8.3.1 DSA sig-params are two s-exprs"),
    ("sig-val", "(rsa-pkcs1-sha1 #0102#)", "3.8.3.1 RSA: a single integer"),
    ("cert", C_MIN, "4 minimal certificate"),
    ("cert", C_FULL, "4 certificate with every field in BNF order"),
    ("cert", sub(H), "4.5 subject is a principal (hash of key)"),
    ("cert", sub("(name fred sam)"), "5.2 relative name subject"),
    ("cert", sub(f"(name {PK} fred)"), "5.2 fully qualified name subject"),
    ("cert", sub(f"(object-hash {H})"), "4.5.1 obj-hash"),
    ("cert", sub(f"(keyholder {PK})"), "4.5.2 keyholder of a principal"),
    ("cert", sub("(keyholder (name fred))"), "4.5.2 keyholder of a name"),
    ("cert", sub(f"(k-of-n #02# #03# {PK} {PK} {PK})"), "4.5.3 k-of-n"),
    ("cert", C_MIN.replace("(tag (*))", "(tag (ftp host))"), "4.8 simple tag"),
    ("cert", C_MIN.replace("(tag (*))", "(tag (ftp (* set a b)))"), "4.8 set"),
    ("cert", C_MIN.replace("(tag (*))", "(tag (ftp (* range numeric ge #01# le #09#)))"), "9.2 range"),
    ("cert", C_MIN.replace("(tag (*))", "(tag (ftp (* prefix /home/)))"), "9.2 prefix"),
    ("cert", C_MIN.replace("(tag (*))", "(tag (ftp (* range alpha)))"), "9.2 <low-lim>? <up-lim>? both optional"),
    ("cert", C_MIN.replace("(tag (*))", "(tag x)"), "9.2 <tag-expr> may be a bare string"),
    ("cert", C_MIN.replace("(tag (*))", "(tag (x [text/plain]y))"), "display-typed string inside a tag"),
    ("cert", C_MIN[:-1] + " (valid))", "9.2 <valid-basic> may be empty: (valid)"),
    ("cert", C_MIN[:-1] + f" (valid (not-after \"2001-01-01_00:00:00\") (online crl (uri http://c/) {PK})))", "9.2 online test inside valid"),
    ("name-cert", f"(cert (issuer (name {PK} fred)) (subject {PK}))", "5.1 name-cert, no <valid>"),
    ("name-cert", NC, "5.1 name-cert with valid"),
    ("acl", "(acl)", "6.1 empty ACL"),
    ("acl", f"(acl (version \"0\") (entry {PK} (tag (*))) (entry (name fred) (propagate) (tag x) (valid) (comment c)))", "6.1 entries"),
    ("sequence", "(sequence)", "6.2 empty sequence"),
    ("sequence", f"(sequence {C_MIN} {SIG} {PK} (do hash md5) (do foo a (b)))", "6.2 cert, signature, pub-key, ops"),
    ("sequence", f"(sequence {NC})", "9.2 <seq-ent> includes <name-cert>"),
    ("op", "(do hash md5)", "6.2 hash-op"),
    ("crl", f"(crl (canceled {H} {H}) (not-after \"2001-01-01_00:00:00\"))", "7.1 crl"),
    ("crl", "(crl (canceled))", "7.1 empty cancel list, empty valid-basic"),
    ("delta-crl", f"(delta-crl {H} (canceled {H}) (not-before \"1997-07-26_23:15:10\"))", "7.1 delta-crl"),
    ("reval", f"(reval (valid {H}) (not-after \"2001-01-01_00:00:00\"))", "7.2 reval"),
    ("reval", f"(reval (valid {H}) (one-time #0102#))", "7.3 one-time reply (9.2 <reval-body>)"),
    ("tag", "(tag (*))", "4.8"),
    ("valid", "(valid (not-before x) (not-after y))", "4.9"),
    ("subj-obj", "(k-of-n #01# #02# (name a))", "4.5.3"),
]
BNF_REJECT = [
    ("pub-key", "(public-key)", "3.8.1 needs the algorithm list"),
    ("pub-key", "(public-key (rsa-pkcs1-sha1 (e #11#)) (uri http://k/) (uri http://j/))", "<uris>? at most one"),
    ("pub-key", "(public-key rsa-pkcs1-sha1)", "algorithm id must be inside a list"),
    ("pub-key", "(public-key-x (rsa-pkcs1-sha1 (e #11#)))", "wrong object name"),
    ("pub-key", "(public-key ([x]rsa-pkcs1-sha1 (e #11#)))", "literal alg ids carry no display type [assumption: here the <uri> alternative matches ANY byte string, so this is ACCEPTED; see test below]"),
    ("hash", "(hash md5)", "3.8.2 value required"),
    ("hash", "(hash)", "3.8.2 needs alg and value"),
    ("hash", "(hash md5 #00# #01#)", "one value only"),
    ("hash", "(hash md5 #00# (uri))", "<uris> needs at least one <uri>"),
    ("signature", f"(signature {H} {PK})", "3.8.3 needs a <sig-val>"),
    ("signature", f"(signature {PK} {H} (rsa-pkcs1-sha1 #01#))", "hash first, then principal"),
    ("signature", f"(signature {H} {PK} (rsa-pkcs1-sha1))", "<sig-params> needs content"),
    ("cert", "(cert (issuer " + PK + ") (subject " + PK + "))", "4: <tag> is required"),
    ("cert", f"(cert (subject {PK}) (tag (*)))", "4: <issuer> is required"),
    ("cert", f"(cert (issuer {PK}) (tag (*)))", "4: <subject> is required"),
    ("cert", f"(cert (subject {PK}) (issuer {PK}) (tag (*)))", "9.2 fixes the field order (3.8 says any order; see source defects)"),
    ("cert", C_MIN[:-1] + " (comment a) (comment b))", "at most one <comment>"),
    ("cert", C_MIN[:-1] + " (bogus x))", "no unknown fields"),
    ("cert", C_MIN.replace("(tag (*))", "(tag a b)"), "9.2 <tag> holds exactly one <tag-expr>"),
    ("cert", C_MIN.replace("(tag (*))", "(tag)"), "empty tag"),
    ("cert", C_MIN.replace("(tag (*))", "(tag (*) (*))"), "(tag (*)) takes no more"),
    ("cert", C_MIN.replace("(issuer", "(issuer-x"), "wrong field name"),
    ("cert", f"(cert (issuer (name {PK} fred)) (subject {PK}) (tag (*)))", "an <issuer> is a <principal>, not a name; name-cert has no tag"),
    ("cert", f"(cert (issuer {PK}) (subject {PK}) (deleg) (tag (*)))", "(propagate) not (deleg)"),
    ("cert", f"(cert (issuer {PK}) (subject {PK}) (propagate x) (tag (*)))", "(propagate) is empty"),
    ("cert", C_MIN.replace("(subject " + PK + ")", "(subject)"), "empty subject"),
    ("cert", C_MIN.replace("(subject " + PK + ")", "(subject " + PK + " " + PK + ")"), "one subject object"),
    ("cert", sub("(name)"), "<names> needs at least one"),
    ("cert", sub("(k-of-n #01#)"), "k-of-n needs k and n"),
    ("cert", sub("(object-hash)"), "object-hash needs a hash"),
    ("cert", sub("(keyholder (object-hash " + H + "))"), "keyholder holds a principal or a name only"),
    ("cert", C_MIN[:-1] + " (valid (not-after a) (not-before b)))", "9.2 <valid-basic> orders not-before first"),
    ("cert", C_MIN[:-1] + " (valid (not-before a) (not-before b)))", "one not-before"),
    ("cert", C_MIN[:-1] + f" (valid (online new-cert (uri http://c/))))", "4.9.2 defines the new-cert online test; 9.2's <online-test> has no such form (disagreement)"),
    ("cert", C_MIN[:-1] + " (not-after a))", "5.3's bare (not-after ...) outside (valid ...)"),
    ("cert", C_MIN.replace("(tag (*))", "(tag (ftp (* prefix)))"), "<tag-prefix> needs a string, but the BNF also reads it as a simple-tag; ACCEPTED, see test below"),
    ("name-cert", f"(cert (issuer (name {PK} fred)) (subject {PK}) (tag (*)))", "5.1: no <tag> in a name certificate"),
    ("name-cert", f"(cert (issuer (name {PK} a b)) (subject {PK}))", "5.1: issuer-name is one <byte-string>"),
    ("name-cert", f"(cert (issuer (name {PK} fred)) (subject {PK}) (propagate))", "5.1: no <deleg>"),
    ("name-cert", f"(cert (issuer (name {PK} fred)) (subject {PK}) (not-after x))", "5.3 example shape: not-after outside (valid)"),
    ("acl", "(acl (entry (tag (*))))", "6.1: entry needs a subject"),
    ("acl", f"(acl (entry {PK}))", "6.1: entry needs a tag"),
    ("acl", f"(acl (cert {PK}))", "6.1: only entries"),
    ("sequence", "(sequence (bogus))", "6.2: not a <seq-ent>"),
    ("sequence", "(sequence (do))", "6.2: general-op needs a byte string name"),
    ("crl", f"(crl {H})", "7.1: needs (canceled ...)"),
    ("crl", "(crl (canceled) (valid))", "7.1: <valid-basic> is not wrapped in (valid)"),
    ("delta-crl", "(delta-crl (canceled) (not-after x))", "7.1: needs the predecessor hash"),
    ("reval", "(reval (valid) (not-after x))", "7.2: reval-hash-list needs one or more hashes"),
    ("reval", f"(reval (valid {H}) (one-time))", "7.3: one-time needs a byte string"),
    ("reval", f"(reval (cert {H}) (one-time #01#))", "7.3 prints (reval <subj-hash> <one-valid>) with <subj-hash> = (cert <hash>); 9.2's <reval> has no such form (disagreement)"),
    ("tag", "(tag)", "4.8"),
    ("tag", "(tag (*) x)", "4.8"),
    ("valid", "(valid x)", "4.9"),
    ("subj-obj", "(k-of-n)", "4.5.3"),
]
# cases where the BNF as printed gives a verdict that the prose would not: ACCEPTED, recorded so a change is noticed
BNF_ACCEPT_ODD = [
    ("cert", C_MIN[:-1] + f" (valid (online crl (uri http://c/) {PK} (id x))))", "4.9.2's (id ...) matches 9.2's <s-part>*; 9.2 has no <online-id> so it is only one more s-expression"),
    ("cert", C_MIN[:-1] + f" (valid (online crl (uri http://c/) {PK})))", "9.2 <online-test> has no <online-id>: accepted although 4.9.2 requires it"),
    ("pub-key", "(public-key ([x]rsa-pkcs1-sha1 (e #11#)))", "display-typed alg id matches the <uri> alternative"),
    ("cert", C_MIN.replace("(tag (*))", "(tag (ftp (* prefix)))"), "(* prefix) with no string parses as <simple-tag> with type *"),
    ("cert", C_MIN.replace("(tag (*))", "(tag (* range bogus x))"), "malformed *-form parses as <simple-tag> (type *)"),
    ("cert", C_MIN.replace("(tag (*))", "(tag (* set a b))"), "<tag-set> and <simple-tag> both match: ambiguous"),
    ("op", "(do hash)", "<general-op> accepts (do hash) with no algorithm"),
    ("crl", f"(crl (canceled {H}) (not-after not-a-date))", "BNF does not constrain <date>; semantic_issues does"),
    ("cert", C_MIN.replace("(tag (*))", "(tag (*) )"), "whitespace only"),
]
# number of derivations expected for ambiguity probes
AMBIG = [
    ("tag", "(tag (*))", 2, "<tag-star> and <tag-expr> via <simple-tag> both match"),
    ("tag", "(tag (* set a b))", 2, "<tag-set> and <simple-tag> both match"),
    ("tag", "(tag (ftp host))", 1, "plain simple tag: one derivation"),
]
SEMANTIC_CASES = [
    (f"(cert (issuer {PK}) (subject (k-of-n #02# #03# {PK} {PK} {PK})) (tag (*)))", 0, "4.5.3 K<N, N listed"),
    (f"(cert (issuer {PK}) (subject (k-of-n #03# #03# {PK} {PK} {PK})) (tag (*)))", 1, "4.5.3: K < N violated"),
    (f"(cert (issuer {PK}) (subject (k-of-n #02# #03# {PK} {PK})) (tag (*)))", 1, "4.5.3: N subjects listed, 2 given"),
    ("(cert (version \"0\"))", 0, "version integer"),
    ("(cert (version \"\"))", 1, "3.2.1 empty string is not an integer"),
    ("(crl (canceled) (not-after \"2001-01-01_00:00:00\"))", 0, "4.9.1 date ok"),
    ("(crl (canceled) (not-after \"2001-01-01 00:00:00\"))", 1, "4.9.1 date shape"),
    ("(hash md5 #00#)", 1, "[assumption] md5 digests are 16 octets"),
    (H, 0, "md5 16 octets"),
]


RULE_CASES = [  # (rule, S-expression text or ("atom", bytes), accept?, why)
    ("tag-range", "(* range alpha)", True, "9.2 <tag-range> with no limits"),
    ("tag-range", "(* range numeric g a l z)", True, "low then up limit"),
    ("tag-range", "(* range time ge a le z)", True, "ge and le"),
    ("tag-range", "(* range binary l z)", True, "up limit only"),
    ("tag-range", "(* range date g a)", True, "low limit only"),
    ("tag-range", "(* range bogus)", False, "9.2 <range-ordering>"),
    ("tag-range", "(* range alpha x a)", False, "9.2 <gte>"),
    ("tag-range", "(* range alpha g a g b)", False, "one low limit at most"),
    ("tag-range", "(* range alpha l z g a)", False, "low limit comes before up limit"),
    ("tag-range", "(* rangex alpha)", False, "literal range"),
    ("tag-range", "(x range alpha)", False, "literal *"),
    ("tag-prefix", "(* prefix abc)", True, "9.2 <tag-prefix>"),
    ("tag-prefix", "(* prefix)", False, "needs a string"),
    ("tag-prefix", "(* prefixx abc)", False, "literal prefix"),
    ("tag-prefix", "(x prefix abc)", False, "literal *"),
    ("tag-prefix", "(* prefix a b)", False, "exactly one string"),
    ("tag-set", "(* set)", True, "zero members"),
    ("tag-set", "(* set a (b c))", True, "members are tag expressions"),
    ("tag-set", "(* sett a)", False, "literal set"),
    ("tag-string", ("atom", b"x"), True, "a byte string"),
    ("tag-string", "(* range alpha)", True, "9.2 <tag-string> includes a range"),
    ("tag-string", "(* prefix a)", True, "9.2 <tag-string> includes a prefix"),
    ("tag-string", "(* set a)", False, "a set is not a <tag-string>"),
    ("tag-string", "(a b)", False, "a list is not a <tag-string>"),
    ("gte", ("atom", b"g"), True, "9.2 <gte>"), ("gte", ("atom", b"ge"), True, "9.2 <gte>"),
    ("gte", ("atom", b"gx"), False, "9.2 <gte>"), ("gte", ("atom", b"l"), False, "9.2 <gte>"),
    ("lte", ("atom", b"l"), True, "9.2 <lte>"), ("lte", ("atom", b"le"), True, "9.2 <lte>"),
    ("lte", ("atom", b"lex"), False, "9.2 <lte>"), ("lte", ("atom", b"g"), False, "9.2 <lte>"),
    ("online-type", ("atom", b"crl"), True, "9.2"), ("online-type", ("atom", b"reval"), True, "9.2"),
    ("online-type", ("atom", b"one-time"), True, "9.2"), ("online-type", ("atom", b"crlx"), False, "9.2"),
    ("online-type", ("atom", b""), False, "9.2"),
    ("range-ordering", ("atom", b"alpha"), True, "9.2"), ("range-ordering", ("atom", b"numeric"), True, "9.2"),
    ("range-ordering", ("atom", b"time"), True, "9.2"), ("range-ordering", ("atom", b"binary"), True, "9.2"),
    ("range-ordering", ("atom", b"date"), True, "9.2"), ("range-ordering", ("atom", b"Alpha"), False, "3.8: case-sensitive"),
    ("range-ordering", ("atom", b"alphax"), False, "9.2"),
    ("hash-alg-name", ("atom", b"md5"), True, "9.2"), ("hash-alg-name", ("atom", b"sha1"), True, "9.2"),
    ("hash-alg-name", ("atom", b"anything"), True, "9.2 <hash-alg-name> includes <uri>, any byte string: the two names constrain nothing"),
    ("pub-sig-alg-id", ("atom", b"dsa-sha1"), True, "9.2"),
    ("pub-sig-alg-id", ("atom", b"anything"), True, "9.2 <pub-sig-alg-id> includes <uri>: the named algorithms constrain nothing"),
    ("hash-op", "(do hash md5)", True, "6.2 <hash-op>"), ("hash-op", "(do hash sha1)", True, "6.2 <hash-op>"),
    ("hash-op", "(do hash)", False, "needs an algorithm name"), ("hash-op", "(dox hash md5)", False, "literal do"),
    ("hash-op", "(do hashx md5)", False, "literal hash"), ("hash-op", "(do hash (x))", False, "name is a byte string"),
    ("online-test", f"(online reval (uri u) {PK})", True, "9.2 reval"),
    ("online-test", f"(online one-time (uri u) {PK})", True, "9.2 one-time"),
    ("online-test", f"(online bogus (uri u) {PK})", False, "9.2 <online-type>"),
    ("online-test", f"(online crl {PK} {PK})", False, "9.2 needs <uris>"),
    ("sequence", f"(sequence {C_MIN} {NC} {PK} {SIG} (do hash md5) (do foo) (reval (valid {H}) (not-after x)) (crl (canceled {H}) (not-after x)) (delta-crl {H} (canceled) (not-before x)))", True, "9.2 <seq-ent> carries every kind of entry"),
    ("sequence", "(sequence (reval (valid) (not-after x)))", False, "9.2 reval needs a hash"),
    ("sequence", "(sequence (acl))", False, "an ACL is not a <seq-ent>"),
]


def run_bnf(bnf, grammar_text=None):
    sx = bnf.sx
    g = bnf.Grammar(grammar_text) if grammar_text else bnf.grammar_from_file()
    n, fails = 0, []

    def case(name, ok):
        nonlocal n
        n += 1
        if not ok:
            fails.append(name)

    def node(t):
        return sx.parse_advanced(t)

    for rule, t, why in BNF_ACCEPT:
        try:
            case(f"accept <{rule}> {t[:60]} ({why})", bnf.accepts(g, rule, node(t)))
        except Exception as e:
            case(f"accept <{rule}> {t[:60]} raised {type(e).__name__}: {e}", False)
    for rule, t, why in BNF_REJECT:
        if "ACCEPTED" in why:
            continue
        try:
            case(f"reject <{rule}> {t[:60]} ({why})", not bnf.accepts(g, rule, node(t)))
        except Exception as e:
            case(f"reject <{rule}> {t[:60]} raised {type(e).__name__}: {e}", False)
    for rule, t, why in BNF_ACCEPT_ODD:
        try:
            case(f"odd-accept <{rule}> {t[:60]} ({why})", bnf.accepts(g, rule, node(t)))
        except Exception as e:
            case(f"odd-accept <{rule}> raised {type(e).__name__}", False)
    for rule, t, want, why in AMBIG:
        try:
            case(f"derivations of {t} = {want} ({why})", bnf.check(g, rule, node(t)).derivations == want)
        except Exception as e:
            case(f"derivations raised {type(e).__name__}", False)
    for t, want, why in SEMANTIC_CASES:
        try:
            case(f"semantic {t[:50]} -> {want} issue(s) ({why})", len(bnf.semantic_issues(node(t))) == want)
        except Exception as e:
            case(f"semantic raised {type(e).__name__}", False)
    for rule, t, want, why in RULE_CASES:
        try:
            nd = sx.Atom(t[1]) if isinstance(t, tuple) else node(t)
            case(f"rule <{rule}> {'accepts' if want else 'rejects'} {t if not isinstance(t, tuple) else t[1]!r:.50} ({why})",
                 bnf.accepts(g, rule, nd) == want)
        except Exception as e:
            case(f"rule <{rule}> {t!r:.40} raised {type(e).__name__}", False)
    # dispatch
    for t, want in ((C_MIN, "cert"), (NC, "name-cert"), (SIG, "signature"), ("(acl)", "acl"), ("(do hash md5)", "op")):
        r, _ = bnf.check_top(g, node(t))
        case(f"check_top {t[:30]} -> {want}", r == want)
    case("check_top: a name certificate is not a <cert>", not bnf.accepts(g, "cert", node(NC)))
    case("check_top: unknown object type", bnf.check_top(g, node("(bogus)"))[0] is None)
    return n, fails


# ----------------------------------------------------------------- mutation
class Mut(ast.NodeTransformer):
    """Apply exactly one mutation (the `target`-th candidate site)."""
    def __init__(self, target):
        self.target, self.i, self.desc = target, -1, None

    def hit(self, node, desc):
        self.i += 1
        if self.i == self.target:
            self.desc = f"line {node.lineno}: {desc}"
            return True
        return False

    def visit_Compare(self, node):
        self.generic_visit(node)
        swap = {ast.Eq: ast.NotEq, ast.NotEq: ast.Eq, ast.Lt: ast.LtE, ast.LtE: ast.Lt,
                ast.Gt: ast.GtE, ast.GtE: ast.Gt, ast.In: ast.NotIn, ast.NotIn: ast.In,
                ast.Is: ast.IsNot, ast.IsNot: ast.Is}
        if len(node.ops) == 1 and type(node.ops[0]) in swap and self.hit(node, f"{type(node.ops[0]).__name__} flipped"):
            node.ops[0] = swap[type(node.ops[0])]()
        return node

    def visit_BoolOp(self, node):
        self.generic_visit(node)
        if self.hit(node, "and/or swapped"):
            node.op = ast.Or() if isinstance(node.op, ast.And) else ast.And()
        return node

    def visit_Raise(self, node):
        if self.hit(node, "raise removed"):
            return ast.Pass()
        return node

    def visit_Constant(self, node):
        if isinstance(node.value, int) and not isinstance(node.value, bool) and self.hit(node, f"{node.value} -> {node.value + 1}"):
            return ast.copy_location(ast.Constant(node.value + 1), node)
        return node

    def visit_If(self, node):
        self.generic_visit(node)
        if self.hit(node, "condition negated"):
            node.test = ast.UnaryOp(ast.Not(), node.test)
        return node


def mutants(path):
    src = path.read_text(encoding="utf-8")
    tree0 = ast.parse(src)
    m = Mut(-1)
    m.visit(ast.parse(src))
    total = m.i + 1
    for k in range(total):
        mm = Mut(k)
        t = mm.visit(ast.parse(src))
        ast.fix_missing_locations(t)
        yield k, mm.desc, t


import signal


class _Timeout(BaseException):
    pass


def _alarm(sig, frm):
    raise _Timeout()


def with_timeout(fn, *a, seconds=3):
    """A mutant may loop forever; a mutant that does is killed (it did not pass)."""
    signal.signal(signal.SIGALRM, _alarm)
    signal.alarm(seconds)
    try:
        return fn(*a)
    finally:
        signal.alarm(0)


def mutate_sexp():
    path = HERE / "spki_sexp.derived.py"
    killed, survived = 0, []
    for k, desc, tree in mutants(path):
        mod = type(sys)("mutant")
        try:
            exec(compile(tree, "mutant", "exec"), mod.__dict__)
            n, fails = with_timeout(run_sexp, mod)
            dead = bool(fails)
        except BaseException:
            dead = True
        if dead:
            killed += 1
        else:
            survived.append((k, desc))
    return killed, survived


def mutate_grammar():
    text = (HERE / "bnf-s9-2-alphabetical.verbatim.bnf").read_text(encoding="utf-8")
    bnf = load("bnf_m", "spki_bnf.derived.py")
    g = bnf.Grammar(text)
    reach = g.reachable(["cert", "name-cert", "pub-key", "hash", "signature", "acl", "sequence", "crl", "delta-crl", "reval", "op", "tag", "valid"])
    prods = bnf.parse_productions(text)
    killed, survived, skipped = 0, [], 0
    for idx, (name, rhs, loc) in enumerate(prods):
        if name in bnf.LEXICAL:
            continue
        variants = []
        toks = bnf.parse_rhs(rhs)
        # mutation 1: drop each quantifier; mutation 2: drop each alternative; mutation 3: change each literal
        flat = rhs.split(" ")
        for j, w in enumerate(flat):
            if w and w[-1] in "?*+" and len(w) > 1:
                variants.append((f"drop '{w[-1]}' on {w[:-1]}", " ".join(flat[:j] + [w[:-1]] + flat[j + 1:])))
                if w[-1] in "*+":
                    variants.append((f"'{w[-1]}' -> '?' on {w[:-1]}", " ".join(flat[:j] + [w[:-1] + "?"] + flat[j + 1:])))
            if w.startswith('"') and w.endswith('"') and len(w) > 2 and w not in ('"("', '")"'):
                variants.append((f"literal {w} -> {w[:-1]}x\"", " ".join(flat[:j] + [w[:-1] + 'x"'] + flat[j + 1:])))
            if w == "|":
                a = " ".join(flat[:j]); b = " ".join(flat[j + 1:])
                variants.append((f"drop alternatives after '|' #{j}", a))
                variants.append((f"drop alternatives before '|' #{j}", b))
        for desc, new in variants:
            newprods = list(prods)
            newprods[idx] = (name, new, loc)
            gt = "\n".join(f"<{n}>:: {r} ;" for n, r, _ in newprods)
            try:
                ok_n, fails = with_timeout(run_bnf, bnf, gt)
                dead = bool(fails)
            except Exception:
                dead = True
            if name not in reach:
                skipped += 1
                continue
            if dead:
                killed += 1
            else:
                survived.append((f"<{name}> {desc}", name))
    return killed, survived, skipped, sorted(set(g.rules) - reach)


def main():
    if "--write-reasons" in sys.argv:
        global GOLD
        GOLD = None
        sx0 = load("sx_w", "spki_sexp.derived.py")
        run_sexp(sx0)
        REASONS_FILE.write_text(json.dumps(SEEN_REASONS, indent=1, ensure_ascii=True, sort_keys=True) + "\n")
        print(f"wrote {REASONS_FILE.name}: {len(SEEN_REASONS)} reject reasons")
        return
    sx = load("sx_t", "spki_sexp.derived.py")
    bnf = load("bnf_t", "spki_bnf.derived.py")
    n1, f1 = run_sexp(sx)
    n2, f2 = run_bnf(bnf)
    print(f"spki_sexp: {n1} cases, {len(f1)} failed")
    print(f"spki_bnf: {n2} cases, {len(f2)} failed")
    for f in f1 + f2:
        print("  FAIL " + f)
    n_accept = len(CANON_ACCEPT) + len(ADV_ACCEPT) + len(TRANSPORT_ACCEPT) + len(BNF_ACCEPT)
    n_reject = len(CANON_REJECT) + len(ADV_REJECT) + len(TRANSPORT_REJECT) + len([r for r in BNF_REJECT if "ACCEPTED" not in r[2]])
    print(f"MUST-accept {n_accept}, MUST-reject {n_reject}, odd-accept {len(BNF_ACCEPT_ODD)}, ambiguity probes {len(AMBIG)}")
    rc = 1 if f1 or f2 else 0
    if "--mutate" in sys.argv:
        k, surv = mutate_sexp()
        print(f"mutation spki_sexp (AST): {k + len(surv)} mutants, {k} killed, {len(surv)} survived")
        for s in surv:
            print(f"   survived #{s[0]} {s[1]}")
        k2, surv2, skipped, unreachable = mutate_grammar()
        print(f"mutation BNF text (reachable rules): {k2 + len(surv2)} mutants, {k2} killed, {len(surv2)} survived; "
              f"{skipped} mutants in rules no top-level object reaches; unreachable rules: {unreachable}")
        for s in surv2:
            print(f"   survived {s[0]}")
    sys.exit(rc)


if __name__ == "__main__":
    main()

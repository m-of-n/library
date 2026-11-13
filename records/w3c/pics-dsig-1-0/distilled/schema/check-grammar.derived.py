#!/usr/bin/env python3
"""DERIVED, not the standard's own grammar. A recogniser this library wrote
from the three BNF displays of pics-dsig-1-0 (the verbatim files beside it) and
from the PICS 1.1 label grammar of pics-1-1-labels section 7, "Detailed Syntax"
(the .txt rendering, lines 150-219 of .cache/pics-1-1-labels.txt; DSig links
that document as "General Format of PICS Labels", which is its section 5).

    python3 -I check-grammar.derived.py            # self-test: every case below
    python3 -I check-grammar.derived.py FILE ...   # report each file against the grammar

It answers two different questions about one text, and they are kept apart:

  pics11  is the text a valid PICS 1.1 label list? Extension data is checked
          against PICS 1.1's `data` production, which has no base64 datum.
  dsig    is it a valid DSig 1.0 label? The PICS 1.1 structure, plus the
          resinfo and sigblock grammars of sections 7.2.1 and 7.4.2 applied to
          the two DSig extensions.

and in two strictnesses:

  strict       base64String is RFC 1521 base64 (alphabet A-Za-z0-9+/, length a
               multiple of four, '=' padding only at the end). Placeholder
               strings of the source's examples ("base64 hash",
               "base64-x.509-cert") are therefore REJECTED, and so are two
               printed "hashes" whose length is not a multiple of four.
  placeholder  a base64 position also accepts any quotedName. This is NOT the
               source's grammar; it exists so the examples can be parsed at
               all, and every use of it is reported.

Where the source's BNF is ambiguous this file picks one reading and names it
in AMBIGUITIES. It is the lane's reading, not the standard's.

Whitespace: the source says contiguous spaces are one space except in quoted
strings (section 7, DSig Extensions); a PICS 1.1 label ignores whitespace
outside quoted strings. Both are implemented as "whitespace separates tokens".

Not modelled (a text using them raises Unmodelled, never a quiet accept):
service-info `error` forms and label-error (PICS 1.1), the HTTP request
extension, and URL syntax beyond "scheme ':' then URL characters" (RFC 1738).
"""
import base64
import binascii
import re
import sys

PICS_VERSION = "pics-1.1"
RESINFO_URL = "http://www.w3.org/TR/1998/REC-DSig-label/resinfo-1_0"
SIGBLOCK_URL = "http://www.w3.org/TR/1998/REC-DSig-label/sigblock-1_0"

AMBIGUITIES = {
    "A1": "quoted-ISO-date: `sep` occurs twice; read as independent, so 1994.11-05 is accepted. The source never says the two must agree.",
    "A2": "quoted-ISO-date: 'T' is a single-quoted literal; the source says only double-quoted strings are case sensitive, so 't' is accepted.",
    "A3": "quoted-ISO-date: the grammar line reads `Stz` while the key defines S and tz separately; read as S then tz (sign, four digits).",
    "A4": "SigInfo: `SigData | ... | '(' SigInfo+ ')'` overlap on a parenthesised pair; acceptance only, no unique parse is claimed.",
    "A5": "token names (\"Signature\", \"AttribInfo\", \"ByKey\", \"on\", ...) are double-quoted, so compared case sensitively.",
    "A6": "URL (RFC 1738) is approximated as scheme ':' followed by URL characters; relative URLs are rejected.",
    "A7": "number: the source writes [sign]unsignedInt['.' [unsignedInt]], so '5.' is a number.",
}


class Reject(Exception):
    """The text is not in the language."""


class Unmodelled(Exception):
    """The text uses a construct this recogniser does not model."""


# ---------------------------------------------------------------- lexical ----

TOKEN = re.compile(r'\s*(?:(\()|(\))|"([^"]*)"|([^\s()"]+))')


def tokenise(text):
    toks, pos = [], 0
    text = text.rstrip()
    while pos < len(text):
        m = TOKEN.match(text, pos)
        if not m:
            if text[pos:].strip() == "":
                break
            raise Reject(f"unterminated quoted string near offset {pos}")
        pos = m.end()
        if m.group(1):
            toks.append(("(", None))
        elif m.group(2):
            toks.append((")", None))
        elif m.group(3) is not None:
            toks.append(("str", m.group(3)))
        else:
            toks.append(("sym", m.group(4)))
    return toks


def tree(toks):
    """Token list to nested Python lists; ('str', s) and ('sym', s) are leaves."""
    stack, cur = [], []
    for t in toks:
        if t[0] == "(":
            stack.append(cur)
            cur = []
        elif t[0] == ")":
            if not stack:
                raise Reject("unbalanced ')'")
            done, cur = cur, stack.pop()
            cur.append(done)
        else:
            cur.append(t)
    if stack:
        raise Reject("unbalanced '('")
    return cur


def is_str(n):
    return isinstance(n, tuple) and n[0] == "str"


def is_sym(n, word=None):
    return isinstance(n, tuple) and n[0] == "sym" and (word is None or n[1].lower() == word)


def is_list(n):
    return isinstance(n, list)


# ------------------------------------------------------------ value types ----

HEX = "0-9A-Fa-f"
ALPHANUMPM = "A-Za-z0-9+-"
# DSig 7.4.2 urlChar, character for character (including '/'):
DSIG_URLCHAR = rf"(?:[{ALPHANUMPM}.$,;:&=?!*~@#_()/]|%[{HEX}][{HEX}])"
# PICS 1.1 urlchar = transmit-name-char | '(' | ')'; transmit-name-char has no '/':
PICS_URLCHAR = rf"(?:[{ALPHANUMPM}.$,;:&=?!*~@#_()]|%[{HEX}][{HEX}])"
DSIG_NAME = re.compile(rf"^(?:{DSIG_URLCHAR}| )+$")
PICS_NAME = re.compile(rf"^(?:{PICS_URLCHAR}| )+$")
URL = re.compile(rf"^[A-Za-z][A-Za-z0-9+.\-]*:(?:[A-Za-z0-9\-_.!~*'();/?:@&=+$,#]|%[{HEX}][{HEX}])+$")
NUMBER = re.compile(r"^[+-]?[0-9]+(?:\.[0-9]*)?$")
TRANSMIT = re.compile(rf"^(?:[{ALPHANUMPM}.$,;:&=?!*~@#_]|%[{HEX}][{HEX}])+(?:/(?:[{ALPHANUMPM}.$,;:&=?!*~@#_]|%[{HEX}][{HEX}])+)*$")
PICS_DATE = re.compile(r"^(\d{4})\.(\d{2})\.(\d{2})[Tt](\d{2}):(\d{2})([+-])(\d{4})$")
DSIG_DATE = re.compile(r"^(\d{4})[.-](\d{2})[.-](\d{2})[Tt](\d{2}):(\d{2})(?::(\d{2})(?:\.(\d+))?)?([+-])(\d{4})$")


def is_base64(s):
    """RFC 1521 base64: alphabet, padding to a multiple of four, '=' only at the end."""
    if not s or len(s) % 4 or not re.fullmatch(r"[A-Za-z0-9+/]*={0,2}", s):
        return False
    try:
        base64.b64decode(s, validate=True)
    except (binascii.Error, ValueError):
        return False
    return True


def pics_date(s):
    m = PICS_DATE.match(s)
    return bool(m) and 1 <= int(m[2]) <= 12 and 1 <= int(m[3]) <= 31 and int(m[4]) <= 23 and int(m[5]) <= 60


def dsig_date(s):
    m = DSIG_DATE.match(s)
    return bool(m) and 1 <= int(m[2]) <= 12 and 1 <= int(m[3]) <= 31 and int(m[4]) <= 23 \
        and int(m[5]) <= 59 and (m[6] is None or int(m[6]) <= 59)


class Ctx:
    """One run of the recogniser: which profile, and what it had to forgive."""

    def __init__(self, profile="dsig", placeholder=False):
        assert profile in ("pics11", "dsig")
        self.profile, self.placeholder, self.notes = profile, placeholder, []

    def forgive(self, what, value):
        self.notes.append(f"placeholder accepted for {what}: {value!r}")


# ----------------------------------------------- PICS 1.1 datum (no base64) ----

def pics_datum(n, ctx):
    """PICS 1.1 `data :: quoted-ISO-date | quotedURL | number | quotedname | '(' data* ')'`."""
    if is_list(n):
        for c in n:
            pics_datum(c, ctx)
    elif is_str(n):
        s = n[1]
        if not (pics_date(s) or URL.match(s) or PICS_NAME.match(s)):
            raise Reject(f"not a PICS 1.1 datum (quoted-ISO-date, quotedURL or quotedname): {s!r}")
    elif is_sym(n):
        if not NUMBER.match(n[1]):
            raise Reject(f"unquoted datum that is not a number: {n[1]!r}")
    else:
        raise Reject("bad datum")


# --------------------------------------------- DSig value classes (7.4.2) ----

def quoted_url(n, what):
    if not (is_str(n) and URL.match(n[1])):
        raise Reject(f"{what}: not a quotedURL: {fmt(n)}")


def quoted_base64(n, what, ctx):
    if not is_str(n):
        raise Reject(f"{what}: not a quoted string: {n!r}")
    if is_base64(n[1]):
        return
    if ctx.placeholder and DSIG_NAME.match(n[1]):
        ctx.forgive(what, n[1])
        return
    raise Reject(f"{what}: not RFC 1521 base64: {n[1]!r}")


def quoted_name(n):
    return is_str(n) and bool(DSIG_NAME.match(n[1]))


def sig_info(n, ctx, depth=0):
    """SigInfo ::= SigData | quotedURL | quoted-ISO-date | quotedBase64String
                   | quotedName | number | '(' SigInfo+ ')'"""
    if is_list(n):
        if not n:
            raise Reject("SigInfo: '(' SigInfo+ ')' needs at least one SigInfo")
        try:
            sig_data(n, ctx)
            return
        except Reject:
            pass
        for c in n:
            sig_info(c, ctx, depth + 1)
        return
    if is_sym(n):
        if NUMBER.match(n[1]):
            return
        raise Reject(f"SigInfo: unquoted symbol that is not a number: {n[1]!r}")
    s = n[1]
    if URL.match(s) or dsig_date(s) or DSIG_NAME.match(s) or is_base64(s):
        return
    if ctx.placeholder and DSIG_NAME.match(s):
        return
    raise Reject(f"SigInfo: matches none of URL, date, base64, name: {s!r}")


def sig_data(n, ctx):
    """SigData ::= '(' SigTokenString SigInfo ')'  (exactly one SigInfo)"""
    if not (is_list(n) and len(n) == 2 and quoted_name(n[0])):
        raise Reject(f"SigData: needs '(' quotedName SigInfo ')': {fmt(n)}")
    sig_info(n[1], ctx)


# ------------------------------------------------------- field-list (7.3.4.7) ----

def field_list(n, ctx):
    """field-list ::= '(' option-list? ratings-list? extension-list? ')'
    option-list ::= '(' "options" <options>* ')' ; ratings-list, extension-list alike.
    At most one of each, in that order. Checked on the tree itself, not through
    SigData, because the two grammars disagree (see FINDINGS F-04)."""
    if not is_list(n):
        raise Reject("field-list: not a parenthesised list")
    want = ["options", "ratings", "extensions"]
    pos = 0
    for item in n:
        if not (is_list(item) and item and is_str(item[0]) and item[0][1] in want):
            raise Reject(f"field-list: member is not an options/ratings/extensions list: {fmt(item)}")
        k = want.index(item[0][1])
        if k < pos:
            raise Reject(f"field-list: {item[0][1]!r} repeated or out of order")
        pos = k + 1
        for v in item[1:]:
            if not is_str(v):
                raise Reject(f"field-list: {item[0][1]} entries are quoted strings: {fmt(v)}")
            if item[0][1] == "extensions" and not URL.match(v[1]):
                raise Reject(f"field-list: extension-list takes quoted-URLs: {v[1]!r}")


# --------------------------------------------------------- known SigData tokens ----

def known_token(n, ctx):
    """Section 7.3.4 token semantics, one `(token value)` SigData at a time."""
    tok, val = n[0][1], n[1]
    if tok == "ByKey":
        pass  # signature-suite dependent
    elif tok == "ByHash":
        quoted_base64(val, "ByHash", ctx)
    elif tok == "ByName":
        if not is_str(val):
            raise Reject("ByName: a quoted string")
    elif tok == "ByCert":
        if not (is_list(val) and len(val) == 2 and is_str(val[0])):
            raise Reject("ByCert: ( \"CA-Name\" serial )")
    elif tok == "on":
        if not (is_str(val) and dsig_date(val[1])):
            raise Reject(f"on: not a quoted-ISO-date: {fmt(val)}")
    elif tok in ("include", "exclude"):
        field_list(val, ctx)
    # SigCrypto: entirely suite-defined


KNOWN_TOKENS = {"ByKey", "ByHash", "ByName", "ByCert", "on", "include", "exclude", "SigCrypto"}


def fmt(n):
    if is_list(n):
        return "(" + " ".join(fmt(c) for c in n) + ")"
    return '"%s"' % n[1] if n[0] == "str" else n[1]


# --------------------------------------------------------- resinfo (7.2.1) ----

def resinfo(data, ctx):
    """resinfo-extension ::= 'extension ( optional ' URL resinfo-data+ ')'
    resinfo-data ::= '(' HashAlgoID resource-hash hash-date? ')'"""
    if not data:
        raise Reject("resinfo: resinfo-data+ needs at least one hash")
    seen = set()
    for d in data:
        if not (is_list(d) and len(d) in (2, 3)):
            raise Reject(f"resinfo-data: '(' HashAlgoID resource-hash hash-date? ')': {fmt(d)}")
        quoted_url(d[0], "HashAlgoID")
        quoted_base64(d[1], "resource-hash", ctx)
        if len(d) == 3 and not (is_str(d[2]) and dsig_date(d[2][1])):
            raise Reject(f"hash-date: not a quoted-ISO-date: {fmt(d[2])}")
        if d[0][1] in seen:
            raise Reject(f"resinfo: two hashes with the same algorithm identifier {d[0][1]!r} (7.2 usage notes)")
        seen.add(d[0][1])


# --------------------------------------------------------- sigblock (7.4.2) ----

def attrib_info(n, ctx):
    """AttributionInfo ::= '(' '"AttribInfo"' Certificate* ')'
    Certificate ::= '(' CertificateFamilyID CertificateData ')'"""
    if not (is_list(n) and n and n[0] == ("str", "AttribInfo")):
        raise Reject(f"AttributionInfo: '(' \"AttribInfo\" Certificate* ')': {fmt(n)}")
    for c in n[1:]:
        if not (is_list(c) and len(c) == 2):
            raise Reject(f"Certificate: '(' CertificateFamilyID CertificateData ')': {fmt(c)}")
        quoted_url(c[0], "CertificateFamilyID")
        if is_str(c[1]) and URL.match(c[1][1]):
            continue
        quoted_base64(c[1], "CertificateData", ctx)


def signature(n, ctx):
    """Signature ::= '(' '"Signature"' SignatureSuiteID SigData+ ')'"""
    if not (is_list(n) and len(n) >= 3 and n[0] == ("str", "Signature")):
        raise Reject(f"Signature: '(' \"Signature\" SignatureSuiteID SigData+ ')': {fmt(n)}")
    quoted_url(n[1], "SignatureSuiteID")
    incl = excl = 0
    for sd in n[2:]:
        sig_data(sd, ctx)
        if sd[0][1] in KNOWN_TOKENS:
            known_token(sd, ctx)
        incl += sd[0][1] == "include"
        excl += sd[0][1] == "exclude"
    if incl + excl > 1:
        raise Reject("Signature: at most one include or exclude, never both (7.3.4.7)")


def sigblock(data, ctx):
    """SignatureExtension ::= 'extension ( optional' SigBlockURL AttributionInfo Signature* ')'"""
    if not data:
        raise Reject("sigblock: AttributionInfo is not optional in the BNF (a bare URL is not a sigblock)")
    attrib_info(data[0], ctx)
    for s in data[1:]:
        signature(s, ctx)


# ------------------------------------------------------- PICS 1.1 label list ----

DATE_OPTS = {"at", "on", "until", "exp"}
URL_OPTS = {"for", "complete-label", "full"}
NAME_OPTS = {"by", "comment"}
B64_OPTS = {"mic-md5", "md5", "signature-rsa-md5"}
OPTION_WORDS = DATE_OPTS | URL_OPTS | NAME_OPTS | B64_OPTS | {"generic", "gen", "extension"}


def option(items, i, ctx, found):
    """One PICS 1.1 option starting at items[i]; returns the next index."""
    w = items[i][1].lower()
    if i + 1 >= len(items):
        raise Reject(f"option {w!r} has no value")
    v = items[i + 1]
    if w in DATE_OPTS:
        if not (is_str(v) and pics_date(v[1])):
            raise Reject(f"option {w}: not a PICS 1.1 quoted-ISO-date: {fmt(v)}")
    elif w in URL_OPTS:
        quoted_url(v, f"option {w}")
    elif w in NAME_OPTS:
        if not (is_str(v) and PICS_NAME.match(v[1])):
            raise Reject(f"option {w}: not a PICS 1.1 quotedname: {fmt(v)}")
    elif w in B64_OPTS:
        if not is_str(v):
            raise Reject(f"option {w}: quoted base64 expected")
    elif w in ("generic", "gen"):
        if not (is_sym(v) and v[1].lower() in ("true", "false")):
            raise Reject("option generic: boolean (true or false)")
    elif w == "extension":
        extension(v, ctx, found)
    found.append((w, v))
    return i + 2


def extension(v, ctx, found):
    """`extension '(' mand/opt quotedURL data* ')'` and, for the two DSig URLs, section 7.2.1 / 7.4.2."""
    if not (is_list(v) and len(v) >= 2 and is_sym(v[0]) and v[0][1].lower() in ("optional", "mandatory")):
        raise Reject(f"extension: '(' optional|mandatory quotedURL data* ')': {fmt(v)}")
    quoted_url(v[1], "extension URL")
    url, data = v[1][1], v[2:]
    dsig_ext = url in (RESINFO_URL, SIGBLOCK_URL)
    if ctx.profile == "pics11" or not dsig_ext:
        for d in data:
            pics_datum(d, ctx)
    else:
        if v[0][1].lower() != "optional":
            raise Reject("DSig extensions are 'optional' (7.2, 7.3.1)")
        (resinfo if url == RESINFO_URL else sigblock)(data, ctx)
    for w, prev in found:
        if w == "extension" and prev[1][1] == url:
            raise Reject(f"extension {url!r} given twice in one option set (PICS 1.1: URLs must be distinct)")


def rating(items, i):
    if not (is_sym(items[i]) and TRANSMIT.match(items[i][1])):
        raise Reject(f"rating: transmit-name expected: {fmt(items[i])}")
    if i + 1 >= len(items):
        raise Reject("rating: value missing")
    v = items[i + 1]
    if is_sym(v) and NUMBER.match(v[1]):
        return i + 2
    if is_list(v) and all(is_sym(c) and re.fullmatch(r"[+-]?\d+(?:\.\d*)?(?::[+-]?\d+(?:\.\d*)?)?", c[1]) for c in v):
        return i + 2
    raise Reject(f"rating: number or multi-value list expected: {fmt(v)}")


def single_label(items, i, ctx, svc_opts):
    found = []
    while i < len(items) and is_sym(items[i]) and items[i][1].lower() in OPTION_WORDS:
        i = option(items, i, ctx, found)
    if not (i < len(items) and is_sym(items[i]) and items[i][1].lower() in ("ratings", "r")):
        raise Reject("single-label: ratingword ('ratings' or 'r') expected")
    if i + 1 >= len(items) or not is_list(items[i + 1]):
        raise Reject("single-label: ratingword must be followed by '(' rating+ ')'")
    body = items[i + 1]
    if not body:
        raise Reject("single-label: rating+ needs at least one rating")
    j = 0
    while j < len(body):
        j = rating(body, j)
    # semantic rules on generic labels. A label inherits the options of its
    # service section unless it overrides them (5.1 L117; PICS 1.1 L143 names
    # generic among them), so both rules read the label's own options first and
    # then the service options. Pass 2 (verify) added the inheritance: the first
    # version read the label's own options only and accepted resinfo in a label
    # made generic by its service section, either way round.
    opts, svc = dict(found), dict(svc_opts)

    def eff(*names):
        for src in (opts, svc):
            for nme in names:
                if nme in src:
                    return src[nme]
        return None
    g = eff("generic", "gen")
    generic = g is not None and is_sym(g) and g[1].lower() == "true"
    if generic and eff("for") is None:
        raise Reject("a generic label must include the for option (6.2 L153; PICS 1.1), as a label or service option")
    # semantic rule the source states about resinfo inside a label (6.2, generic)
    if ctx.profile == "dsig" and generic:
        for w, v in list(found) + list(svc_opts):
            if w == "extension" and is_list(v) and len(v) > 1 and is_str(v[1]) and v[1][1] == RESINFO_URL:
                raise Reject("resinfo in a generic label (6.2, generic)")
    return i + 2


def label_list(tr, ctx):
    if len(tr) != 1 or not is_list(tr[0]):
        raise Reject("a label list is one parenthesised list")
    items = tr[0]
    if not items or not is_sym(items[0], PICS_VERSION):
        raise Reject("label list must begin with PICS-1.1")
    i, services = 1, 0
    while i < len(items):
        if is_sym(items[i], "error"):
            raise Unmodelled("service-info error forms")
        if not (is_str(items[i]) and URL.match(items[i][1])):
            raise Reject(f"service-info: serviceID (quotedURL) expected: {fmt(items[i])}")
        services += 1
        i += 1
        svc_found = []
        while i < len(items) and is_sym(items[i]) and items[i][1].lower() in OPTION_WORDS:
            if items[i][1].lower() == "extension" and i + 1 < len(items) and is_list(items[i + 1]) \
                    and len(items[i + 1]) > 1 and is_str(items[i + 1][1]) and items[i + 1][1][1] == SIGBLOCK_URL:
                raise Reject("a sigblock extension is only valid as a label option, not a service option (7.3.1)")
            i = option(items, i, ctx, svc_found)
        if not (i < len(items) and is_sym(items[i]) and items[i][1].lower() in ("labels", "l")):
            raise Reject("service-info: labelword ('labels' or 'l') expected")
        i += 1
        while i < len(items) and not is_str(items[i]):
            if is_list(items[i]):
                j = 0
                while j < len(items[i]):
                    j = single_label(items[i], j, ctx, svc_found)
                i += 1
            else:
                i = single_label(items, i, ctx, svc_found)
    if services == 0:
        raise Reject("a label list needs at least one service-info")


# ---------------------------------------------------------------- entry points ----

def recognise(text, nonterminal="label", profile="dsig", placeholder=False):
    """Returns (True, notes) or raises Reject / Unmodelled.

    nonterminal: 'label' (a whole PICS 1.1 label list), 'resinfo-extension',
    'sigblock-extension', 'AttributionInfo', 'SigData', 'field-list'."""
    ctx = Ctx(profile, placeholder)
    tr = tree(tokenise(text))
    if nonterminal == "label":
        label_list(tr, ctx)
    elif nonterminal in ("resinfo-extension", "sigblock-extension"):
        # the display form is `extension ( optional URL ... )`
        if len(tr) != 2 or not is_sym(tr[0], "extension"):
            raise Reject("an extension display is the symbol 'extension' then one list")
        found = []
        want = RESINFO_URL if nonterminal == "resinfo-extension" else SIGBLOCK_URL
        if not (is_list(tr[1]) and len(tr[1]) > 1 and is_str(tr[1][1]) and tr[1][1][1] == want):
            raise Reject(f"extension URL is not {want}")
        extension(tr[1], ctx, found)
    elif nonterminal == "AttributionInfo":
        if len(tr) != 1:
            raise Reject("one list expected")
        attrib_info(tr[0], ctx)
    elif nonterminal == "SigData":
        if len(tr) != 1:
            raise Reject("one list expected (a SigData is exactly one parenthesised pair)")
        sig_data(tr[0], ctx)
    elif nonterminal == "field-list":
        if len(tr) != 1:
            raise Reject("one list expected")
        field_list(tr[0], ctx)
    else:
        raise ValueError(nonterminal)
    return True, ctx.notes


def verdict(text, nonterminal="label", profile="dsig", placeholder=False):
    try:
        ok, notes = recognise(text, nonterminal, profile, placeholder)
        return "ACCEPT", notes
    except Reject as e:
        return "REJECT", [str(e)]
    except Unmodelled as e:
        return "UNMODELLED", [str(e)]


# ------------------------------------------------------------------ self-test ----

L = '(PICS-1.1 "http://www.gcf.org/v2.5" labels for "http://x.org/a" on "1994.11.05T08:15-0500" ratings (suds 0.5))'


def lab(ext):
    return f'(PICS-1.1 "http://www.gcf.org/v2.5" labels for "http://x.org/a" {ext} on "1994.11.05T08:15-0500" ratings (suds 0.5))'


B64SLASH = "AQID/wQF+gYH/QgJ"  # valid base64, contains '/' and '+'
SHA1_OK = base64.b64encode(bytes(range(20))).decode()
MD5_OK = base64.b64encode(bytes(range(16))).decode()
RS = f'"{RESINFO_URL}"'
SB = f'"{SIGBLOCK_URL}"'
SHA1 = '"http://www.w3.org/TR/1998/REC-DSig-label/SHA1-1_0"'
MD5 = '"http://www.w3.org/TR/1998/REC-DSig-label/MD5-1_0"'
RSA = '"http://www.w3.org/TR/1998/REC-DSig-label/RSA-MD5-1_0"'


def sbx(*parts):
    return f'extension (optional {SB} ("AttribInfo") ' + " ".join(parts) + ")"


SIG_OK = f'("Signature" {RSA} ("ByHash" "{B64SLASH}") ("on" "1996-12-02T22:20-0000") ("SigCrypto" "{B64SLASH}"))'

# (id, nonterminal, profile, placeholder, text, expected, why)
CASES = [
    # --- accepted: the shapes the source defines
    ("A-01", "label", "dsig", False, L, "ACCEPT", "plain PICS 1.1 label, no extension"),
    ("A-02", "label", "dsig", False, lab(f"extension (optional {RS} ({SHA1} \"{SHA1_OK}\") ({MD5} \"{MD5_OK}\" \"1997-02-05T08:15-0500\"))"), "ACCEPT", "resinfo with two hashes, one dated"),
    ("A-03", "label", "dsig", False, lab(sbx(SIG_OK)), "ACCEPT", "sigblock, one signature, real base64"),
    ("A-04", "label", "dsig", False, lab(f'extension (optional {SB} ("AttribInfo"))'), "ACCEPT", "sigblock with empty attribution info and no signature (Signature*)"),
    ("A-05", "label", "dsig", False, lab(sbx(SIG_OK.replace('("SigCrypto"', '("exclude" (("extensions" "http://foo/bad"))) ("SigCrypto"'))), "ACCEPT", "exclude with one extension URL (the source's own 7.4.1 shape)"),
    ("A-06", "label", "dsig", False, lab(f'extension (optional {RS} ({SHA1} "{SHA1_OK}" "1997-02-05T08:15:30.25-0500"))'), "ACCEPT", "DSig date with seconds and fraction"),
    ("A-07", "SigData", "dsig", False, '("ByKey" (("P" "AQID") ("Q" "AQID")))', "ACCEPT", "ByKey wrapped in one extra pair, as the grammar needs"),
    ("A-08", "field-list", "dsig", False, '(("options" "by" "for") ("ratings" "suds") ("extensions" "http://foo/a" "http://foo/b"))', "ACCEPT", "field-list with several entries (7.3.4.7 grammar)"),
    # --- rejected: the hazard that a grammar which parses binds nothing
    ("R-01", "label", "dsig", False, lab(f'extension (optional {RS})'), "REJECT", "resinfo-data+ : zero hashes"),
    ("R-02", "label", "dsig", False, lab(f'extension (optional {RS} ({SHA1} "{SHA1_OK}") ({SHA1} "{SHA1_OK}"))'), "REJECT", "two hashes with one algorithm (7.2 usage notes)"),
    ("R-03", "label", "dsig", False, lab(f'extension (optional {RS} ({SHA1} "not base64!"))'), "REJECT", "resource-hash must be base64"),
    ("R-04", "label", "dsig", False, lab(f'extension (optional {RS} ({SHA1} "{SHA1_OK}" "1997-13-05T08:15-0500"))'), "REJECT", "month 13"),
    ("R-05", "label", "dsig", False, lab(f'extension (optional {RS} ({SHA1} "{SHA1_OK}" "1997-02-05T08:15"))'), "REJECT", "time zone may not be omitted (7.2.1 note 1)"),
    ("R-06", "label", "dsig", False, lab(f'extension (optional {RS} ({SHA1} "{SHA1_OK}" "1997-02-05T08:60-0500"))'), "REJECT", "DSig minutes are 00-59 (PICS 1.1 allowed 60)"),
    ("R-07", "label", "dsig", False, lab(f'extension (mandatory {RS} ({SHA1} "{SHA1_OK}"))'), "REJECT", "resinfo is an optional extension"),
    ("R-08", "label", "dsig", False, lab(f'extension (optional {RS} ({SHA1} "{SHA1_OK}"))').replace("for ", "gen true for "), "REJECT", "resinfo in a generic label (6.2)"),
    ("R-09", "label", "dsig", False, lab(f'extension (optional {SB})'), "REJECT", "AttributionInfo is not optional in the BNF"),
    ("A-09", "label", "dsig", False, lab(sbx(SIG_OK, SIG_OK.replace("RSA-MD5", "DSS"))), "ACCEPT", "parallel signatures (7.4)"),
    ("R-11", "label", "dsig", False, lab(sbx(f'("Signature" {RSA})')), "REJECT", "SigData+ : a signature with no SigData"),
    ("R-12", "label", "dsig", False, lab(sbx(f'("Signature" "not a url" ("SigCrypto" "AQID"))')), "REJECT", "SignatureSuiteID must be a quotedURL"),
    ("R-13", "label", "dsig", False, lab(sbx(SIG_OK.replace('("SigCrypto"', '("exclude" (("options" "by"))) ("include" (("options" "for"))) ("SigCrypto"'))), "REJECT", "include and exclude together (7.3.4.7)"),
    ("R-14", "label", "dsig", False, lab(sbx(SIG_OK.replace('("SigCrypto"', '("exclude" (("options" "by")) ("ratings" "x")) ("SigCrypto"'))), "REJECT", "SigData takes exactly one SigInfo"),
    ("R-15", "label", "dsig", False, lab(sbx(SIG_OK.replace('"1996-12-02T22:20-0000"', '"yesterday"'))), "REJECT", "on: not a quoted-ISO-date"),
    ("R-16", "label", "dsig", False, lab(sbx(SIG_OK.replace('"ByHash"', '"ByHash"').replace(B64SLASH, "AQID/wQ", 1))), "REJECT", "ByHash value: base64 length not a multiple of four"),
    ("A-11", "label", "dsig", False, '(PICS-1.1 "http://www.gcf.org/v2.5" l for "http://x/a" ' + f'extension (optional {SB} ("AttribInfo")) ' + 'r (suds 0.5))', "ACCEPT", "sigblock as a label option, abbreviated keywords l and r (was R-17: an accept case misnamed as a reject)"),
    ("R-18", "label", "dsig", False, f'(PICS-1.1 "http://www.gcf.org/v2.5" extension (optional {SB} ("AttribInfo")) l r (suds 0.5))', "REJECT", "a sigblock is only valid as a label option, not a service option (7.3.1)"),
    ("R-19", "label", "dsig", False, lab(f'extension (optional {SB} ("AttribInfo" ("not a url" "AQID")))'), "REJECT", "CertificateFamilyID must be a quotedURL"),
    ("R-20", "label", "dsig", False, lab(f'extension (optional {SB} ("AttribInfo" ("http://ca.example/x509" "***")))'), "REJECT", "CertificateData is base64 or a URL"),
    ("R-21", "label", "dsig", False, lab(sbx(SIG_OK) + " " + sbx(SIG_OK)), "REJECT", "same extension URL twice in one label (PICS 1.1)"),
    ("R-22", "label", "dsig", False, lab(sbx(SIG_OK.replace('("SigCrypto"', '("exclude" ()) ("SigCrypto"'))), "REJECT", "exclude () : empty field-list is a field-list but not a SigInfo+ (F-04)"),
    ("R-23", "SigData", "dsig", False, '("ByKey" ("P" "AQID") ("Q" "AQID"))', "REJECT", "two SigInfo in one SigData (this is the shape of the 7.3.4.2 DSA example, F-03)"),
    ("R-24", "field-list", "dsig", False, '(("ratings" "suds") ("options" "by"))', "REJECT", "field-list members out of order"),
    ("R-25", "field-list", "dsig", False, '(("extensions" "not a url"))', "REJECT", "extension-list takes quoted-URLs"),
    ("R-26", "label", "dsig", False, '(PICS-1.1 "http://x.org/s" labels ratings ())', "REJECT", "rating+ needs one rating"),
    ("R-27", "label", "dsig", False, '(PICS-1.2 "http://x.org/s" labels ratings (a 1))', "REJECT", "version must be PICS-1.1"),
    # --- added by pass 2 (verify): generic labels and option inheritance
    ("R-28", "label", "dsig", False, f'(PICS-1.1 "http://www.gcf.org/v2.5" gen true labels for "http://x.org/" extension (optional {RS} ({SHA1} "{SHA1_OK}")) ratings (suds 0.5))', "REJECT", "resinfo in a label made generic by a service option (6.2; service options are inherited, 5.1)"),
    ("R-29", "label", "dsig", False, f'(PICS-1.1 "http://www.gcf.org/v2.5" extension (optional {RS} ({SHA1} "{SHA1_OK}")) labels gen true for "http://x.org/" ratings (suds 0.5))', "REJECT", "resinfo inherited from a service option into a generic label (6.2, 7.2)"),
    ("R-30", "label", "dsig", False, '(PICS-1.1 "http://www.gcf.org/v2.5" labels gen true ratings (suds 0.5))', "REJECT", "a generic label without the for option (6.2 L153; PICS 1.1 says the same)"),
    ("A-10", "label", "dsig", False, '(PICS-1.1 "http://www.gcf.org/v2.5" for "http://x.org/" labels gen true ratings (suds 0.5))', "ACCEPT", "a generic label whose for is inherited from its service section"),
    # --- the source's own concession: DSig 1.0 is not a valid PICS 1.1 extension (7.4.2 note)
    ("P-01", "label", "dsig", False, lab(sbx(f'("Signature" {RSA} ("ByHash" "{B64SLASH}") ("SigCrypto" "AQID"))')), "ACCEPT", "base64 containing '/' and '+', DSig profile"),
    ("P-02", "label", "pics11", False, lab(sbx(f'("Signature" {RSA} ("ByHash" "{B64SLASH}") ("SigCrypto" "AQID"))')), "REJECT", "same text, PICS 1.1 profile: '/' is not in quotedname and the string is not a URL (the 7.4.2 note, F-01)"),
    ("P-03", "label", "pics11", False, lab(sbx(f'("Signature" {RSA} ("ByHash" "AQIDBAUG") ("SigCrypto" "AQID"))')), "ACCEPT", "base64 with no '/' lexes as a PICS 1.1 quotedname"),
    ("P-04", "label", "pics11", False, lab(sbx(f'("Signature" {RSA} ("on" "1996-12-02T22:20-0000") ("SigCrypto" "AQID"))')), "ACCEPT", "a hyphenated date lexes as a PICS 1.1 quotedname even though it is not a PICS 1.1 date"),
    ("P-05", "label", "pics11", False, lab(f'extension (optional {RS} ({SHA1} "{SHA1_OK}"))'), "ACCEPT", "a 20-byte value (the bytes 0..19, not a digest) whose base64 contains no '/': accepted by PICS 1.1 reading"),
    ("P-06", "label", "pics11", False, lab(f'extension (optional {RS} ({SHA1} "{base64.b64encode(bytes([0xff]*20)).decode()}"))'), "REJECT", "a 20-byte value (twenty 0xFF bytes, not a digest) whose base64 has '/': PICS 1.1 profile rejects, so resinfo is no safer than sigblock (F-01)"),
    ("P-07", "label", "dsig", False, lab(f'extension (optional {RS} ({SHA1} "{base64.b64encode(bytes([0xff]*20)).decode()}"))'), "ACCEPT", "the same under the DSig profile"),
    # --- DSig's own quotedName admits '/', which its note says it does not
    ("N-01", "label", "dsig", False, lab(sbx('("Signature" ' + RSA + ' ("x/y" "AQID"))')), "ACCEPT", "SigTokenString quotedName contains '/': allowed by 7.4.2 urlChar, contradicting the note under the same grammar (F-02)"),
    ("N-02", "label", "pics11", False, lab(sbx('("Signature" ' + RSA + ' ("x/y" "AQID"))')), "REJECT", "the same token under PICS 1.1 quotedname"),
    # --- strictness: placeholders
    ("S-01", "resinfo-extension", "dsig", False, f'extension (optional {RS} ({SHA1} "base64 hash"))', "REJECT", "the source's own placeholder is not base64 (strict)"),
    ("S-02", "resinfo-extension", "dsig", True, f'extension (optional {RS} ({SHA1} "base64 hash"))', "ACCEPT", "placeholder mode accepts it and reports it"),
]


def self_test():
    bad = 0
    for cid, nt, prof, ph, text, want, why in CASES:
        got, notes = verdict(text, nt, prof, ph)
        flag = "ok " if got == want else "BAD"
        bad += got != want
        print(f"{flag} {cid} {nt:18s} {prof:6s}{' placeholder' if ph else '':12s} want {want:6s} got {got:6s}  {why}")
        if got != want:
            print("     ", notes)
    acc = sum(1 for c in CASES if c[5] == "ACCEPT")
    print(f"CASES {len(CASES)}: {acc} accept, {len(CASES) - acc} reject; DIFFERING from expectation {bad}")
    return bad


if __name__ == "__main__":
    if len(sys.argv) == 1:
        sys.exit(1 if self_test() else 0)
    for p in sys.argv[1:]:
        t = open(p, encoding="ascii").read()
        for prof in ("pics11", "dsig"):
            print(p, prof, verdict(t, "label", prof, False))

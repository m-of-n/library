#!/usr/bin/env python3
"""DERIVED - not verbatim. Written by this library, not copied from the source.

An executable reader for the BNF that draft-ietf-spki-cert-structure-06 prints
(section 9.2 and the fragments in sections 3-8), and a checker that validates a
parsed SPKI S-expression against it.

    python3 -I spki_bnf.derived.py [--rule NAME] FILE...     # FILE: advanced, {transport} or canonical

How the BNF is read (every choice below is the library's, none is the draft's):

* The grammar text is the VERBATIM file bnf-s9-2-alphabetical.verbatim.bnf (or
  the fragments file); nothing is retyped. Lines starting "# " are annotation.
* Line wraps that split a rule name at a hyphen ("<crl-hash-" / "list>") are
  rejoined; the draft prints several.
* The draft says (section 3) that its examples and BNF "deal with advanced
  rather than canonical S-expressions" and (section 9) that the BNF "is the BNF
  of canonical forms and includes lengths for each explicit byte string". It is
  one grammar read both ways: a quoted string is a byte string whose bytes
  are those characters, whichever form carries it. This checker works on the
  parsed S-expression, so it is form-independent: spki_sexp.derived.py parses
  advanced, transport and canonical, and this module matches the token stream.
* TOKENS: "(" and ")" and byte strings. The lexical rules <byte-string>,
  <bytes>, <decimal>, <ddigit>, <nzddigit>, <display-type> are NOT matched
  here (spki_sexp.derived.py implements them, section 3.2); a reference to
  <byte-string> matches any one byte string, with or without a display type.
* A quoted literal other than "(" and ")" matches one byte string with exactly
  those bytes and NO display type. The literal "(*)" is three tokens: "(", the
  byte string *, ")" (the draft writes it as one literal in <tag-star>).
* The matcher is a memoised set-of-end-positions recogniser (no exponential
  backtracking, no left recursion in the draft's grammar; a cycle is reported).
  count() counts derivations, to expose ambiguity.
"""
import importlib.util
import pathlib
import re
import sys
from collections import defaultdict

HERE = pathlib.Path(__file__).resolve().parent
sys.setrecursionlimit(20000)


def _load(name, fname):
    spec = importlib.util.spec_from_file_location(name, HERE / fname)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


try:  # sibling module, loaded by path so `python3 -I` works
    sx = _load("spki_sexp_derived", "spki_sexp.derived.py")
except FileNotFoundError:  # pragma: no cover
    sx = None

LEXICAL = {"byte-string", "bytes", "decimal", "ddigit", "nzddigit", "display-type"}
CAP = 10 ** 6


# ------------------------------------------------------------- BNF reading
class BnfError(ValueError):
    pass


TOK = re.compile(r'\s*(?:(<[^<>\s]+>::)|(<[^<>\s]+>)|("[^"]*")|(\{[^}]*\})|([|?*+;]))')


def _rejoin(text: str) -> str:
    """Join physical lines and undo a wrap inside a <rule-name>."""
    t = " ".join(x.strip() for x in text.split("\n") if x.strip())
    t = re.sub(r"(<[^<>\s]*-)\s+([^<>\s]*>)", r"\1\2", t)
    return t


def parse_productions(text: str):
    """[(name, rhs_text, locator)]; locator from the nearest '# @frag' line."""
    out = []
    loc = ""
    block = []
    blocks = []

    def flush():
        if block:
            blocks.append((loc, "\n".join(block)))
            block.clear()

    for line in text.split("\n"):
        m = re.match(r"^# @frag (\S+) L(\d+-\d+)$", line)
        if m:
            flush()
            loc = f"{m.group(1)} L{m.group(2)}"
            continue
        if line.startswith("# ") or line == "#":
            continue
        block.append(line)
    flush()
    for loc, body in blocks:
        t = _rejoin(body)
        pos = 0
        parts = []  # (name, tokens)
        cur = None
        while pos < len(t):
            m = TOK.match(t, pos)
            if not m:
                if t[pos:].strip() == "":
                    break
                raise BnfError(f"{loc}: cannot tokenise at {t[pos:pos + 30]!r}")
            pos = m.end()
            if m.group(1):
                cur = [m.group(1)[1:-3], []]
                parts.append(cur)
            elif m.group(5) == ";":
                cur = None
            elif cur is None:
                raise BnfError(f"{loc}: text outside a production: {m.group(0)!r}")
            else:
                cur[1].append(m.group(0).strip())
        for name, toks in parts:
            out.append((name, " ".join(toks), loc))
    return out


class Item:
    __slots__ = ("kind", "val", "q")

    def __init__(self, kind, val, q=""):
        self.kind, self.val, self.q = kind, val, q

    def __repr__(self):
        return f"{self.val}{self.q}"


def parse_rhs(rhs: str):
    """Alt = list of Seq = list of Item."""
    alts, seq = [], []
    for m in TOK.finditer(rhs):
        ref, lit, com, op = m.group(2), m.group(3), m.group(4), m.group(5)
        if ref:
            seq.append(Item("ref", ref[1:-1]))
        elif lit:
            seq.append(Item("lit", lit[1:-1]))
        elif com:
            seq.append(Item("com", com))
        elif op == "|":
            alts.append(seq)
            seq = []
        elif op in "?*+":
            if not seq:
                raise BnfError(f"quantifier {op} with nothing before it in {rhs!r}")
            if seq[-1].q:
                raise BnfError(f"two quantifiers on {seq[-1].val} in {rhs!r}")
            seq[-1].q = op
        else:
            raise BnfError(f"unexpected {m.group(0)!r} in {rhs!r}")
    alts.append(seq)
    return alts


# --------------------------------------------------------------- the grammar
class Grammar:
    def __init__(self, text: str = None, productions=None):
        prods = productions if productions is not None else parse_productions(text)
        self.prods = prods
        self.rules = {}
        self.dupes = defaultdict(list)
        for name, rhs, loc in prods:
            self.dupes[name].append((rhs, loc))
            self.rules[name] = parse_rhs(rhs)  # a later definition replaces an earlier one
        for name, defs in self.dupes.items():
            if len({d[0] for d in defs}) > 1:
                self.rules[name] = parse_rhs(defs[-1][0])

    def refs(self, name):
        out = set()
        for seq in self.rules.get(name, []):
            for it in seq:
                if it.kind == "ref":
                    out.add(it.val)
        return out

    def undefined(self):
        return sorted({r for n in self.rules for r in self.refs(n)} - set(self.rules) - LEXICAL)

    def reachable(self, roots):
        seen, todo = set(), list(roots)
        while todo:
            n = todo.pop()
            if n in seen:
                continue
            seen.add(n)
            todo.extend(self.refs(n))
        return seen

    def with_overrides(self, new_rules):
        """a copy of this grammar with rules replaced/added: {name: rhs text}."""
        g = Grammar(productions=list(self.prods))
        for n, rhs in new_rules.items():
            g.rules[n] = parse_rhs(rhs)
        return g


# ------------------------------------------------------------------ tokens
OPEN, CLOSE = "(", ")"


def flatten(node):
    if isinstance(node, sx.Atom):
        return [node]
    out = [OPEN]
    for x in node.items:
        out += flatten(x)
    out.append(CLOSE)
    return out


class Result:
    def __init__(self, ok, derivations, furthest, expected, total):
        self.ok, self.derivations = ok, derivations
        self.furthest, self.expected, self.total = furthest, expected, total

    def __bool__(self):
        return self.ok

    def why(self):
        if self.ok:
            return "ok"
        return f"stops at token {self.furthest} of {self.total}: expected {' | '.join(sorted(self.expected)[:6])}"


class Matcher:
    def __init__(self, grammar: Grammar, toks):
        self.g, self.t = grammar, toks
        self.memo, self.busy = {}, set()
        self.far, self.exp = 0, set()
        self.cyclic = []

    def _fail(self, pos, what):
        if pos > self.far:
            self.far, self.exp = pos, {what}
        elif pos == self.far:
            self.exp.add(what)

    def lit(self, s, pos):
        t = self.t
        if s == "(*)":
            if pos + 2 < len(t) and t[pos] == OPEN and isinstance(t[pos + 1], sx.Atom) \
                    and t[pos + 1].data == b"*" and t[pos + 1].display is None and t[pos + 2] == CLOSE:
                return {pos + 3: 1}
            self._fail(pos, '"(*)"')
            return {}
        if s in "()" and len(s) == 1:
            if pos < len(t) and t[pos] == s:
                return {pos + 1: 1}
            self._fail(pos, f'"{s}"')
            return {}
        if pos < len(t) and isinstance(t[pos], sx.Atom) and t[pos].display is None \
                and t[pos].data == s.encode("latin-1"):
            return {pos + 1: 1}
        self._fail(pos, f'"{s}"')
        return {}

    def ref(self, name, pos):
        if name == "byte-string":
            if pos < len(self.t) and isinstance(self.t[pos], sx.Atom):
                return {pos + 1: 1}
            self._fail(pos, "<byte-string>")
            return {}
        if name in LEXICAL:
            raise BnfError(f"<{name}> is lexical (spki_sexp.derived.py), not matched on tokens")
        if name not in self.g.rules:
            raise BnfError(f"<{name}> is not defined")
        key = (name, pos)
        if key in self.memo:
            return self.memo[key]
        if key in self.busy:
            self.cyclic.append(key)
            return {}
        self.busy.add(key)
        res = defaultdict(int)
        for seq in self.g.rules[name]:
            for e, c in self.seq(seq, pos).items():
                res[e] = min(CAP, res[e] + c)
        self.busy.discard(key)
        self.memo[key] = dict(res)
        return self.memo[key]

    def one(self, it, pos):
        if it.kind == "lit":
            return self.lit(it.val, pos)
        if it.kind == "ref":
            return self.ref(it.val, pos)
        return {pos: 1}  # a {comment} placeholder

    def item(self, it, pos):
        if not it.q:
            return self.one(it, pos)
        if it.q == "?":
            res = {pos: 1}
            for e, c in self.one(it, pos).items():
                res[e] = res.get(e, 0) + c
            return res
        cnt = {}
        if it.q == "*":
            cnt[pos] = 1
        reach = {pos: 1}  # derivations reaching a position by whole iterations
        n = len(self.t)
        for p in range(pos, n + 1):
            c = reach.get(p, 0)
            if not c:
                continue
            for e, c2 in self.one(it, p).items():
                if e > p:  # an empty iteration adds no new length; it is ignored
                    reach[e] = min(CAP, reach.get(e, 0) + c * c2)
                    cnt[e] = min(CAP, cnt.get(e, 0) + c * c2)
        return cnt

    def seq(self, seq, pos):
        cur = {pos: 1}
        for it in seq:
            nxt = defaultdict(int)
            for p, c in cur.items():
                for e, c2 in self.item(it, p).items():
                    nxt[e] = min(CAP, nxt[e] + c * c2)
            cur = nxt
            if not cur:
                break
        return cur


def check(grammar: Grammar, rule: str, node) -> Result:
    toks = flatten(node)
    m = Matcher(grammar, toks)
    ends = m.ref(rule, 0)
    ok = len(toks) in ends
    if m.cyclic:
        raise BnfError(f"grammar cycle at {m.cyclic[0]}")
    return Result(ok, ends.get(len(toks), 0), m.far, m.exp, len(toks))


def accepts(grammar, rule, node) -> bool:
    return check(grammar, rule, node).ok


# ------------------------------------------------- object dispatch (derived)
# The draft names these as top-level (9.1: <5-tuple>, <acl>, <crl>, <delta-crl>,
# <reval>, <sequence>; 3.8: <sequence>, <cert>, <pub-key>, <signature>, <op>;
# <acl>). The first byte string of a list picks the candidates.
TOP = {
    b"public-key": ["pub-key"], b"hash": ["hash"], b"signature": ["signature"],
    b"cert": ["cert", "name-cert"], b"acl": ["acl"], b"sequence": ["sequence"],
    b"crl": ["crl"], b"delta-crl": ["delta-crl"], b"reval": ["reval"], b"do": ["op"],
}


def check_top(grammar: Grammar, node):
    """(rule matched or None, [Result per candidate rule tried])."""
    if not isinstance(node, sx.Lst):
        return None, []
    cands = TOP.get(node.items[0].data, [])
    results = [(r, check(grammar, r, node)) for r in cands if r in grammar.rules]
    for r, res in results:
        if res.ok:
            return r, results
    return None, results


# --------------------------------------- semantic checks from prose (derived)
def semantic_issues(node, hash_lengths=True):
    """Constraints the draft states in prose that its BNF cannot carry. Each is
    cited; the BNF match is separate. Returns a list of strings."""
    out = []

    def head(n):
        return n.items[0].data if isinstance(n, sx.Lst) and isinstance(n.items[0], sx.Atom) else None

    def walk(n):
        if not isinstance(n, sx.Lst):
            return
        h = head(n)
        if h == b"version" and len(n.items) == 2:
            try:
                sx.decode_integer(n.items[1])
            except sx.SexpError as e:
                out.append(f"(version): {e}")
        elif h in (b"not-before", b"not-after") and len(n.items) == 2 and isinstance(n.items[1], sx.Atom):
            try:
                sx.check_date(n.items[1])
            except sx.SexpError as e:
                out.append(f"({h.decode()}): {e}")
        elif h == b"k-of-n" and len(n.items) >= 3 and all(isinstance(x, sx.Atom) for x in n.items[1:3]):
            try:
                k, nn = sx.decode_integer(n.items[1]), sx.decode_integer(n.items[2])
            except sx.SexpError as e:
                out.append(f"(k-of-n): {e}")
            else:
                listed = len(n.items) - 3
                if not k < nn:
                    out.append(f"(k-of-n): 4.5.3 says K < N, got K={k} N={nn}")
                if listed != nn:
                    out.append(f"(k-of-n): 4.5.3 says N subjects are listed; N={nn} but {listed} listed")
        elif h == b"hash" and hash_lengths and len(n.items) >= 3 and isinstance(n.items[1], sx.Atom) \
                and isinstance(n.items[2], sx.Atom):
            alg, val = n.items[1].data, n.items[2].data
            want = {b"md5": 16, b"sha1": 20}.get(alg)
            if want is not None and len(val) != want:  # ASSUMPTION: md5=16 and sha1=20 octets
                out.append(f"(hash {alg.decode()}): value is {len(val)} octets, the algorithm's digest is {want}")
        for x in n.items:
            walk(x)

    walk(node)
    return out


# ------------------------------------------------------------------- tests
def grammar_from_file(name="bnf-s9-2-alphabetical.verbatim.bnf") -> Grammar:
    return Grammar((HERE / name).read_text(encoding="utf-8"))


def _main(argv):
    rule = None
    if "--rule" in argv:
        i = argv.index("--rule")
        rule = argv[i + 1]
        argv = argv[:i] + argv[i + 2:]
    g = grammar_from_file()
    rc = 0
    for f in argv:
        data = pathlib.Path(f).read_bytes()
        try:
            node = sx.parse_canonical(data) if data[:1] == b"(" and b"\n" not in data[:1] and data.rstrip()[-1:] == b")" and re.match(rb"^\(\d", data) \
                else sx.parse_any(data.decode("latin-1"))
        except sx.SexpError as e:
            print(f"{f}: not an S-expression: {e}")
            rc = 1
            continue
        if rule:
            res = check(g, rule, node)
            print(f"{f}: <{rule}> {res.why()}")
            rc |= 0 if res.ok else 1
        else:
            r, tried = check_top(g, node)
            if r:
                print(f"{f}: <{r}> ok ({dict(tried)[r].derivations} derivation(s)); semantic: {semantic_issues(node) or 'none'}")
            else:
                print(f"{f}: no top-level rule matches: " + "; ".join(f"<{a}> {b.why()}" for a, b in tried))
                rc = 1
    return rc


if __name__ == "__main__":
    sys.exit(_main(sys.argv[1:]))

#!/usr/bin/env python3
# DERIVED, not verbatim. Written by this library (FX-1 pass 1, schema lane) for the record
# pics-1-1-labels. The source ships a BNF in prose-and-HTML form and no checker.
#
# What this file is:
#   1. a small interpreter for the RFC 5234 (ABNF) subset the three *.derived.abnf files use
#      (strings, %s"..", %x values and ranges, ( ) [ ] / and n*m repetition), memoised over
#      END-POSITION SETS so it is exact for any context-free grammar here, with no ordering
#      assumptions;
#   2. the two layers the grammar needs (a token layer for the label list and the HTTP headers,
#      a character layer for the bureau query: see the header of labels.derived.abnf);
#   3. the instances each entry rule MUST ACCEPT and MUST REJECT, each reject paired with the
#      minimal edit that makes it acceptable (so a rejection is proved to be for the one reason
#      named, not for some unrelated one), plus a mutation sweep over every label list in
#      ../examples (delete one paren, one quote, one keyword letter ...: every mutant must be
#      rejected);
#   4. the report of what was EXAMINED beside what was found (hazards.md: a check that looks at
#      nothing must not print a clean result).
#
#   python3 -I check-grammar.derived.py            # run everything; exit 1 on any failure
#   import it with importlib (the file name has hyphens) to reuse parse_* from reproduce.py.
#
# Stdlib only. Deviations of the derived grammar from the source are listed in README.md.

import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent

CORE = {
    "ALPHA": ("alt", [("range", 0x41, 0x5A), ("range", 0x61, 0x7A)]),
    "DIGIT": ("range", 0x30, 0x39),
    "HEXDIG": ("alt", [("range", 0x30, 0x39), ("range", 0x41, 0x46), ("range", 0x61, 0x66)]),
    "DQUOTE": ("range", 0x22, 0x22),
    "SP": ("range", 0x20, 0x20),
    "HTAB": ("range", 0x09, 0x09),
    "CR": ("range", 0x0D, 0x0D),
    "LF": ("range", 0x0A, 0x0A),
}
INF = 10 ** 9

# Constraints the source states in prose that ABNF cannot express: rule name -> texts it may not match.
EXCLUDE = {
    "lex-first-token": {"services"},          # section 11.3: "the first token-or-quoted-string is not 'services'"
    "bq-ext-token": {"opt", "format", "u", "s"},  # section 12.2: "the token is not one of opt, format, u, or s"
}


# ---------------------------------------------------------------- ABNF reader

class AbnfError(Exception):
    pass


def _strip_comment(line):
    out, q = [], False
    for ch in line:
        if ch == '"':
            q = not q
        if ch == ";" and not q:
            break
        out.append(ch)
    return "".join(out)


def read_rules(text):
    rules, order, cur = {}, [], None
    for raw in text.split("\n"):
        line = _strip_comment(raw).rstrip()
        if not line.strip():
            continue
        if line[0] not in " \t":
            m = re.match(r"([A-Za-z][A-Za-z0-9-]*)\s*=(/?)\s*(.*)$", line)
            if not m:
                raise AbnfError("bad rule line: " + raw)
            cur = m.group(1).lower()
            if m.group(2):
                raise AbnfError("incremental alternatives not supported: " + raw)
            if cur in rules:
                raise AbnfError("rule defined twice: " + cur)
            rules[cur] = m.group(3)
            order.append(cur)
        else:
            if cur is None:
                raise AbnfError("continuation before any rule: " + raw)
            rules[cur] += " " + line.strip()
    return {k: _Parser(v, k).parse() for k, v in rules.items()}, order


class _Parser:
    def __init__(self, s, name):
        self.s, self.i, self.name = s, 0, name

    def err(self, msg):
        raise AbnfError("rule %s: %s at %d in %r" % (self.name, msg, self.i, self.s))

    def ws(self):
        while self.i < len(self.s) and self.s[self.i] in " \t":
            self.i += 1

    def peek(self):
        return self.s[self.i] if self.i < len(self.s) else ""

    def parse(self):
        n = self.alt()
        self.ws()
        if self.i != len(self.s):
            self.err("trailing text")
        return n

    def alt(self):
        parts = [self.seq()]
        while True:
            self.ws()
            if self.peek() == "/":
                self.i += 1
                parts.append(self.seq())
            else:
                break
        return parts[0] if len(parts) == 1 else ("alt", parts)

    def seq(self):
        items = []
        while True:
            self.ws()
            c = self.peek()
            if c == "" or c in "/)]":
                break
            items.append(self.rep())
        if not items:
            self.err("empty sequence")
        return items[0] if len(items) == 1 else ("seq", items)

    def rep(self):
        self.ws()
        lo, hi = 1, 1
        m = re.compile(r"(\d*)(\*?)(\d*)").match(self.s, self.i)
        if m.group(0):
            self.i = m.end()
            if m.group(2):
                lo = int(m.group(1)) if m.group(1) else 0
                hi = int(m.group(3)) if m.group(3) else INF
            else:
                lo = hi = int(m.group(1))
        node = self.element()
        return node if (lo, hi) == (1, 1) else ("rep", lo, hi, node)

    def element(self):
        c = self.peek()
        if c == "(":
            self.i += 1
            n = self.alt()
            self.ws()
            if self.peek() != ")":
                self.err("missing )")
            self.i += 1
            return n
        if c == "[":
            self.i += 1
            n = self.alt()
            self.ws()
            if self.peek() != "]":
                self.err("missing ]")
            self.i += 1
            return ("rep", 0, 1, n)
        if c == '"':
            return self.string(False)
        if c == "%":
            self.i += 1
            k = self.peek().lower()
            if k in "si" and self.s[self.i + 1:self.i + 2] == '"':
                self.i += 1
                return self.string(k == "s")
            if k not in "xd":
                self.err("unsupported %-form")
            self.i += 1
            base = 16 if k == "x" else 10
            m = re.compile(r"[0-9A-Fa-f]+").match(self.s, self.i)
            if not m:
                self.err("bad number")
            lo = int(m.group(0), base)
            self.i = m.end()
            if self.peek() == "-":
                self.i += 1
                m = re.compile(r"[0-9A-Fa-f]+").match(self.s, self.i)
                hi = int(m.group(0), base)
                self.i = m.end()
                return ("range", lo, hi)
            return ("range", lo, lo)
        m = re.compile(r"[A-Za-z][A-Za-z0-9-]*").match(self.s, self.i)
        if not m:
            self.err("unexpected " + repr(c))
        self.i = m.end()
        return ("ref", m.group(0).lower())

    def string(self, sens):
        j = self.s.index('"', self.i + 1)
        t = self.s[self.i + 1:j]
        self.i = j + 1
        return ("lit", t, sens) if t else ("seq", [])


# ---------------------------------------------------------------- engine

class Grammar:
    def __init__(self, paths):
        self.rules, self.order = {}, []
        for p in paths:
            r, o = read_rules(pathlib.Path(p).read_text(encoding="utf-8"))
            for k in r:
                if k in self.rules:
                    raise AbnfError("rule %s defined in more than one file" % k)
            self.rules.update(r)
            self.order += o
        for k, v in CORE.items():
            self.rules.setdefault(k.lower(), v)
        self._lexmemo = {}
        self.examined = 0

    # --- static checks
    def refs(self, node, acc):
        t = node[0]
        if t == "ref":
            acc.add(node[1])
        elif t in ("seq", "alt"):
            for c in node[1]:
                self.refs(c, acc)
        elif t == "rep":
            self.refs(node[3], acc)
        return acc

    def lint(self, entries):
        used, problems = set(entries), []
        for k, n in self.rules.items():
            used |= self.refs(n, set())
        for k, n in self.rules.items():
            for r in self.refs(n, set()):
                if r not in self.rules:
                    problems.append("undefined rule %s used by %s" % (r, k))
        unused = [k for k in self.order if k not in used]
        return problems, unused

    # --- matching
    def _ends(self, node, pos, ctx):
        """Return the frozenset of end positions of node starting at pos.
        ctx is ("c", text) for characters or ("t", tokens) for the token layer."""
        mode, inp = ctx
        t = node[0]
        if t == "lit":
            lit, sens = node[1], node[2]
            if mode == "c":
                seg = inp[pos:pos + len(lit)]
                ok = len(seg) == len(lit) and (seg == lit if sens else seg.lower() == lit.lower())
                return frozenset([pos + len(lit)]) if ok else frozenset()
            if pos < len(inp):
                tx = inp[pos][0]
                if (tx == lit) if sens else (tx.lower() == lit.lower()):
                    self.far = max(self.far, pos + 1)
                    return frozenset([pos + 1])
            return frozenset()
        if t == "range":
            if mode == "c" and pos < len(inp) and node[1] <= ord(inp[pos]) <= node[2]:
                return frozenset([pos + 1])
            return frozenset()
        if t == "seq":
            cur = {pos}
            for c in node[1]:
                nxt = set()
                for p in cur:
                    nxt |= self._ends(c, p, ctx)
                cur = nxt
                if not cur:
                    break
            return frozenset(cur)
        if t == "alt":
            out = set()
            for c in node[1]:
                out |= self._ends(c, pos, ctx)
            return frozenset(out)
        if t == "rep":
            lo, hi, child = node[1], node[2], node[3]
            levels = [frozenset([pos])]
            result = set(levels[0]) if lo == 0 else set()
            seen_after_min = set(result)
            k = 0
            while k < hi:
                k += 1
                nxt = set()
                for p in levels[-1]:
                    nxt |= self._ends(child, p, ctx)
                if not nxt:
                    break
                levels.append(frozenset(nxt))
                if k >= lo:
                    new = nxt - seen_after_min
                    result |= nxt
                    seen_after_min |= nxt
                    if hi == INF and not new:
                        break
            return frozenset(result)
        if t == "ref":
            name = node[1]
            return self._ref(name, pos, ctx)
        raise AbnfError("bad node " + repr(node))

    def _ref(self, name, pos, ctx):
        mode, inp = ctx
        body = self.rules.get(name)
        if body is None:
            raise AbnfError("undefined rule " + name)
        if mode == "t" and name.startswith("lex-"):
            if pos < len(inp):
                tx = inp[pos][0]
                if self._lex_full(name, tx):
                    self.far = max(self.far, pos + 1)
                    return frozenset([pos + 1])
            return frozenset()
        key = (name, pos, mode, id(inp))
        memo = self._memo
        if key in memo:
            return memo[key]
        memo[key] = frozenset()  # recursion guard
        ends = self._ends(body, pos, ctx)
        ex = EXCLUDE.get(name)
        if ex and mode == "c":
            ends = frozenset(e for e in ends if inp[pos:e].lower() not in ex)
        memo[key] = ends
        return ends

    def _lex_full(self, name, text):
        k = (name, text)
        if k in self._lexmemo:
            return self._lexmemo[k]
        saved = self._memo
        self._memo = {}
        ends = self._ends(self.rules[name], 0, ("c", text))
        self._memo = saved
        ok = len(text) in ends
        ex = EXCLUDE.get(name)
        if ok and ex and text.lower() in ex:
            ok = False
        self._lexmemo[k] = ok
        return ok

    def match_chars(self, rule, text):
        self._memo, self.far = {}, 0
        self.examined += 1
        return len(text) in self._ref(rule, 0, ("c", text))

    def match_tokens(self, rule, toks):
        self._memo, self.far = {}, 0
        self.examined += 1
        return len(toks) in self._ref(rule, 0, ("t", toks))


# ---------------------------------------------------------------- tokenizer (token layer)

class TokenError(Exception):
    pass


def tokenize(text, delims="()"):
    """[(token text, start offset)]. A quoted string is one token and may contain anything but
    a double quote (the grammar has no escape). A word is a maximal run of characters that are
    none of whitespace, a delimiter, or a double quote."""
    toks, i, n = [], 0, len(text)
    while i < n:
        c = text[i]
        if c in " \t\r\n":
            i += 1
        elif c in delims:
            toks.append((c, i))
            i += 1
        elif c == '"':
            j = text.find('"', i + 1)
            if j < 0:
                raise TokenError("unterminated quoted string at offset %d" % i)
            toks.append((text[i:j + 1], i))
            i = j + 1
        else:
            j = i
            while j < n and text[j] not in " \t\r\n" and text[j] not in delims and text[j] != '"':
                j += 1
            toks.append((text[i:j], i))
            i = j
    return toks


# ---------------------------------------------------------------- public parsers

_G = {}


def _grammar(kind):
    if kind not in _G:
        if kind == "tokens":
            _G[kind] = Grammar([HERE / "labels.derived.abnf", HERE / "http-headers.derived.abnf"])
        else:
            _G[kind] = Grammar([HERE / "bureau-query.derived.abnf"])
    return _G[kind]


class Result:
    def __init__(self, ok, reason=""):
        self.ok, self.reason = ok, reason

    def __bool__(self):
        return self.ok

    def __repr__(self):
        return "OK" if self.ok else "REJECT(%s)" % self.reason


def _tok_parse(rule, text, delims):
    g = _grammar("tokens")
    try:
        toks = tokenize(text, delims)
    except TokenError as e:
        return Result(False, str(e))
    if g.match_tokens(rule, toks):
        return Result(True)
    far = g.far
    if far >= len(toks):
        return Result(False, "input ends after token %d of %d; the rule needs more" % (far, len(toks)))
    return Result(False, "no parse past token %d of %d: %r (offset %d)" % (far, len(toks), toks[far][0], toks[far][1]))


def parse_labellist(text):
    return _tok_parse("labellist", text, "()")


def parse_request_header(text, prose=False):
    return _tok_parse("request-header-prose" if prose else "request-header", text, "(){}")


def parse_protocol_header(text):
    return _tok_parse("protocol-header", text, "(){}")


def parse_label_header(text):
    return _tok_parse("label-header", text, "(){}")


def parse_request_line(text, rule="request-line"):
    g = _grammar("chars")
    if g.match_chars(rule, text):
        return Result(True)
    return Result(False, "no parse of the request line by rule %s" % rule)


def unfold_request(text):
    """Remove the presentation line breaks the source says it inserted (section 12.1, Appendix B):
    a line break and the indentation after it is deleted; a line that begins HTTP/ is joined with
    one space. Returns one line."""
    lines = [ln for ln in text.strip("\n").split("\n")]
    out = lines[0].rstrip()
    for ln in lines[1:]:
        s = ln.strip()
        out += (" " if s.startswith("HTTP/") else "") + s
    return out


# ---------------------------------------------------------------- tests

S = '"http://www.gcf.org/v2.5"'
OK = "(PICS-1.1 " + S + " l r (suds 0.5 density 0 color/hue 1))"

# (name, bad, good): bad MUST be rejected, good (the minimal repair of bad) MUST be accepted.
LABEL_REJECT = [
    ("empty list", "()", "(PICS-1.1 " + S + " l)"),
    ("no version", "(" + S + " l r (a 1))", OK),
    ("wrong version", "(PICS-1.0 " + S + " l r (a 1))", OK),
    ("no service-info", "(PICS-1.1)", "(PICS-1.1 " + S + " l)"),
    ("service URL not quoted", "(PICS-1.1 http://www.gcf.org/v2.5 l r (a 1))", OK),
    ("unterminated quote", '(PICS-1.1 "http://www.gcf.org/v2.5 l r (a 1))', OK),
    ("missing close paren of list", "(PICS-1.1 " + S + " l r (a 1)", OK),
    ("missing close paren of ratings", "(PICS-1.1 " + S + " l r (a 1)", OK),
    ("extra close paren", "(PICS-1.1 " + S + " l r (a 1)))", OK),
    ("trailing token after list", "(PICS-1.1 " + S + " l r (a 1)) x", OK),
    ("keyword glued to keyword (labelsr)", "(PICS-1.1 " + S + " labelsr (a 1))", OK),
    ("keyword glued to name (rsuds)", "(PICS-1.1 " + S + " l r(suds 1) rsuds (a 1))", "(PICS-1.1 " + S + " l r(suds 1) r (a 1))"),
    ("ratings without parentheses", "(PICS-1.1 " + S + " l r a 1)", OK),
    ("empty rating list: rating+ needs one (A3)", "(PICS-1.1 " + S + " l r ())", OK),
    ("rating name without value", "(PICS-1.1 " + S + " l r (a))", OK),
    ("rating value not a number", "(PICS-1.1 " + S + " l r (a x))", OK),
    ("number .5 (needs a digit before the point)", "(PICS-1.1 " + S + " l r (a .5))", "(PICS-1.1 " + S + " l r (a 0.5))"),
    ("number 1e3", "(PICS-1.1 " + S + " l r (a 1e3))", OK),
    ("number --1", "(PICS-1.1 " + S + " l r (a --1))", "(PICS-1.1 " + S + " l r (a -1))"),
    ("bare sign", "(PICS-1.1 " + S + " l r (a -))", "(PICS-1.1 " + S + " l r (a -0))"),
    ("range with spaces around the colon (A4)", "(PICS-1.1 " + S + " l r (a (1 : 2)))", "(PICS-1.1 " + S + " l r (a (1:2)))"),
    ("range missing its upper end", "(PICS-1.1 " + S + " l r (a (1:)))", "(PICS-1.1 " + S + " l r (a (1:2)))"),
    ("range of three", "(PICS-1.1 " + S + " l r (a (1:2:3)))", "(PICS-1.1 " + S + " l r (a (1:2)))"),
    ("transmit-name with a trailing slash", "(PICS-1.1 " + S + " l r (a/ 1))", "(PICS-1.1 " + S + " l r (a/b 1))"),
    ("transmit-name with a leading slash", "(PICS-1.1 " + S + " l r (/a 1))", "(PICS-1.1 " + S + " l r (a 1))"),
    ("transmit-name with a bad percent escape", "(PICS-1.1 " + S + " l r (a%zz 1))", "(PICS-1.1 " + S + " l r (a%2f 1))"),
    ("transmit-name with a quote character", "(PICS-1.1 " + S + " l r (a'b 1))", "(PICS-1.1 " + S + " l r (a%27b 1))"),
    ("unknown option", "(PICS-1.1 " + S + " l foo \"x\" r (a 1))", "(PICS-1.1 " + S + " l comment \"x\" r (a 1))"),
    ("option without value", "(PICS-1.1 " + S + " l by r (a 1))", "(PICS-1.1 " + S + " l by \"x\" r (a 1))"),
    ("by value not quoted", "(PICS-1.1 " + S + " l by x r (a 1))", "(PICS-1.1 " + S + " l by \"x\" r (a 1))"),
    ("quotedname with a slash (A5)", '(PICS-1.1 ' + S + ' l by "a/b" r (a 1))', '(PICS-1.1 ' + S + ' l by "a.b" r (a 1))'),
    ("quotedname with an apostrophe", '(PICS-1.1 ' + S + ' l by "it\'s" r (a 1))', '(PICS-1.1 ' + S + ' l by "it%27s" r (a 1))'),
    ("empty quotedname", '(PICS-1.1 ' + S + ' l by "" r (a 1))', '(PICS-1.1 ' + S + ' l by "x" r (a 1))'),
    ("quotedname with a newline", '(PICS-1.1 ' + S + ' l by "a\nb" r (a 1))', '(PICS-1.1 ' + S + ' l by "a b" r (a 1))'),
    ("generic without a boolean", "(PICS-1.1 " + S + " l generic for \"http://a/\" r (a 1))", "(PICS-1.1 " + S + " l generic true for \"http://a/\" r (a 1))"),
    ("generic with a non-boolean", "(PICS-1.1 " + S + " l generic yes r (a 1))", "(PICS-1.1 " + S + " l generic t r (a 1))"),
    ("generic boolean glued to next keyword (tfor)", "(PICS-1.1 " + S + " l generic tfor \"http://a/\" r (a 1))", "(PICS-1.1 " + S + " l generic t for \"http://a/\" r (a 1))"),
    ("empty for URL", "(PICS-1.1 " + S + " l for \"\" r (a 1))", "(PICS-1.1 " + S + " l for \"http://a/\" r (a 1))"),
    ("for URL with a space", "(PICS-1.1 " + S + " l for \"http://a b/\" r (a 1))", "(PICS-1.1 " + S + " l for \"http://a%20b/\" r (a 1))"),
    ("date with hyphens", '(PICS-1.1 ' + S + ' l on "1994-11-05T08:15-0500" r (a 1))', '(PICS-1.1 ' + S + ' l on "1994.11.05T08:15-0500" r (a 1))'),
    ("date without time zone", '(PICS-1.1 ' + S + ' l on "1994.11.05T08:15" r (a 1))', '(PICS-1.1 ' + S + ' l on "1994.11.05T08:15-0500" r (a 1))'),
    ("date without time", '(PICS-1.1 ' + S + ' l on "1994.11.05" r (a 1))', '(PICS-1.1 ' + S + ' l on "1994.11.05T08:15-0500" r (a 1))'),
    ("date month 13", '(PICS-1.1 ' + S + ' l on "1994.13.05T08:15-0500" r (a 1))', '(PICS-1.1 ' + S + ' l on "1994.12.05T08:15-0500" r (a 1))'),
    ("date month 00", '(PICS-1.1 ' + S + ' l on "1994.00.05T08:15-0500" r (a 1))', '(PICS-1.1 ' + S + ' l on "1994.01.05T08:15-0500" r (a 1))'),
    ("date day 32", '(PICS-1.1 ' + S + ' l on "1994.11.32T08:15-0500" r (a 1))', '(PICS-1.1 ' + S + ' l on "1994.11.31T08:15-0500" r (a 1))'),
    ("date day 00", '(PICS-1.1 ' + S + ' l on "1994.11.00T08:15-0500" r (a 1))', '(PICS-1.1 ' + S + ' l on "1994.11.01T08:15-0500" r (a 1))'),
    ("date hour 24", '(PICS-1.1 ' + S + ' l on "1994.11.05T24:15-0500" r (a 1))', '(PICS-1.1 ' + S + ' l on "1994.11.05T23:15-0500" r (a 1))'),
    ("date minute 61", '(PICS-1.1 ' + S + ' l on "1994.11.05T08:61-0500" r (a 1))', '(PICS-1.1 ' + S + ' l on "1994.11.05T08:60-0500" r (a 1))'),
    ("date lower-case t", '(PICS-1.1 ' + S + ' l on "1994.11.05t08:15-0500" r (a 1))', '(PICS-1.1 ' + S + ' l on "1994.11.05T08:15-0500" r (a 1))'),
    ("date zone without sign", '(PICS-1.1 ' + S + ' l on "1994.11.05T08:15 0500" r (a 1))', '(PICS-1.1 ' + S + ' l on "1994.11.05T08:15+0500" r (a 1))'),
    ("date with Z zone", '(PICS-1.1 ' + S + ' l on "1994.11.05T08:15Z" r (a 1))', '(PICS-1.1 ' + S + ' l on "1994.11.05T08:15+0000" r (a 1))'),
    ("date zone with 3 digits", '(PICS-1.1 ' + S + ' l on "1994.11.05T08:15-050" r (a 1))', '(PICS-1.1 ' + S + ' l on "1994.11.05T08:15-0500" r (a 1))'),
    ("date not quoted", '(PICS-1.1 ' + S + ' l on 1994.11.05T08:15-0500 r (a 1))', '(PICS-1.1 ' + S + ' l on "1994.11.05T08:15-0500" r (a 1))'),
    ("two-digit year", '(PICS-1.1 ' + S + ' l on "94.11.05T08:15-0500" r (a 1))', '(PICS-1.1 ' + S + ' l on "1994.11.05T08:15-0500" r (a 1))'),
    ("md5 not base64", '(PICS-1.1 ' + S + ' l md5 "!!!!" r (a 1))', '(PICS-1.1 ' + S + ' l md5 "AAAA" r (a 1))'),
    ("md5 bad padding length", '(PICS-1.1 ' + S + ' l md5 "AAAAA" r (a 1))', '(PICS-1.1 ' + S + ' l md5 "AAAAAA==" r (a 1))'),
    ("md5 padding in the middle", '(PICS-1.1 ' + S + ' l md5 "AA==AAAA" r (a 1))', '(PICS-1.1 ' + S + ' l md5 "AAAAAA==" r (a 1))'),
    ("md5 empty", '(PICS-1.1 ' + S + ' l md5 "" r (a 1))', '(PICS-1.1 ' + S + ' l md5 "AAAA" r (a 1))'),
    ("md5 not quoted", '(PICS-1.1 ' + S + ' l md5 AAAA r (a 1))', '(PICS-1.1 ' + S + ' l md5 "AAAA" r (a 1))'),
    ("signature not base64", '(PICS-1.1 ' + S + ' l signature-RSA-MD5 "a b%" r (a 1))', '(PICS-1.1 ' + S + ' l signature-RSA-MD5 "ab/+" r (a 1))'),
    ("extension without optional/mandatory", "(PICS-1.1 " + S + " l extension (\"http://x/e\" 1) r (a 1))", "(PICS-1.1 " + S + " l extension (optional \"http://x/e\" 1) r (a 1))"),
    ("extension without its URL", "(PICS-1.1 " + S + " l extension (optional) r (a 1))", "(PICS-1.1 " + S + " l extension (optional \"http://x/e\") r (a 1))"),
    ("extension with a bare word as data", "(PICS-1.1 " + S + " l extension (optional \"http://x/e\" foo) r (a 1))", "(PICS-1.1 " + S + " l extension (optional \"http://x/e\" 1) r (a 1))"),
    ("extension keyword other than optional/mandatory", "(PICS-1.1 " + S + " l extension (required \"http://x/e\") r (a 1))", "(PICS-1.1 " + S + " l extension (mandatory \"http://x/e\") r (a 1))"),
    ("extension with unbalanced data parens", "(PICS-1.1 " + S + " l extension (optional \"http://x/e\" (1 2) r (a 1))", "(PICS-1.1 " + S + " l extension (optional \"http://x/e\" (1 2)) r (a 1))"),
    ("option after ratings and before the close", "(PICS-1.1 " + S + " l r (a 1) by \"x\")", "(PICS-1.1 " + S + " l r (a 1) by \"x\" r (a 1))"),
    ("service-unavailable in parentheses", "(PICS-1.1 " + S + " error (service-unavailable))", "(PICS-1.1 " + S + " error service-unavailable)"),
    ("request-denied without parentheses", "(PICS-1.1 " + S + " error request-denied)", "(PICS-1.1 " + S + " error (request-denied))"),
    ("service error followed by labels", "(PICS-1.1 " + S + " error service-unavailable l r (a 1))", "(PICS-1.1 " + S + " error service-unavailable " + S + " l r (a 1))"),
    ("not-labeled URL not quoted", "(PICS-1.1 " + S + " l error (not-labeled http://x/))", "(PICS-1.1 " + S + " l error (not-labeled \"http://x/\"))"),
    ("label-error with an explanation but no URL (a lone quoted string with a space is not a quotedURL; one without is read as the URL, A18)", "(PICS-1.1 " + S + " l error (request-denied \"why not\"))", "(PICS-1.1 " + S + " l error (request-denied \"http://x/\" \"why not\"))"),
    ("unknown error word", "(PICS-1.1 " + S + " l error (broken))", "(PICS-1.1 " + S + " l error (not-labeled))"),
    ("no-ratings with an unquoted explanation", "(PICS-1.1 error (no-ratings why))", "(PICS-1.1 error (no-ratings \"why\"))"),
    ("tree list not closed", "(PICS-1.1 " + S + " l (r (a 1))", "(PICS-1.1 " + S + " l (r (a 1)))"),
    ("tree list holding an error", "(PICS-1.1 " + S + " l (error (not-labeled \"http://x/\")))", "(PICS-1.1 " + S + " l error (not-labeled \"http://x/\"))"),
    ("tree list nested", "(PICS-1.1 " + S + " l ((r (a 1))))", "(PICS-1.1 " + S + " l (r (a 1)))"),
    ("semicolon comment from Appendix B (A15)", "(PICS-1.1 " + S + " ;first service\n l r (a 1))", "(PICS-1.1 " + S + "\n l r (a 1))"),
    ("labels with no service-info before it", "(PICS-1.1 l r (a 1))", "(PICS-1.1 " + S + " l r (a 1))"),
    ("two labelwords", "(PICS-1.1 " + S + " l l r (a 1))", OK),
]

# Must be ACCEPTED: derived readings and forms the grammar admits (each is a reading the README names)
LABEL_ACCEPT = [
    ("section 6 keyword case: upper-case keywords", "(pics-1.1 " + S + " LABELS RATINGS (suds 0.5))"),
    ("quote and paren delimit without whitespace (A1)", "(PICS-1.1" + S + "l r(a 1))"),
    ("tabs and newlines are whitespace", "(PICS-1.1\n\t" + S + "\r\n l\tr (a 1))"),
    ("labels with no label at all (label*)", "(PICS-1.1 " + S + " labels)"),
    ("service-info with options and no label", "(PICS-1.1 " + S + " by \"x\" labels)"),
    ("two services", "(PICS-1.1 " + S + " l r (a 1) \"http://b/\" l r (b 2))"),
    ("no-ratings alone", "(PICS-1.1 error (no-ratings))"),
    ("no-ratings with explanations", "(PICS-1.1 error (no-ratings \"a\" \"b c\"))"),
    ("no-ratings with a space after the paren (A2)", "(PICS-1.1 error ( no-ratings))"),
    ("service-error request-denied", "(PICS-1.1 " + S + " error (request-denied \"why\"))"),
    ("service-error service-unavailable", "(PICS-1.1 " + S + " error service-unavailable)"),
    ("label-error request-denied with URL and explanation", "(PICS-1.1 " + S + " l error (request-denied \"http://x/\" \"why\"))"),
    ("label-error request-denied bare", "(PICS-1.1 " + S + " l error (request-denied))"),
    ("label-error not-labeled with no URL", "(PICS-1.1 " + S + " l error (not-labeled))"),
    ("label-error not-labeled with two URLs", "(PICS-1.1 " + S + " l error (not-labeled \"http://a/\" \"http://b/\"))"),
    ("tree list, empty", "(PICS-1.1 " + S + " l ())"),
    ("tree list of two labels", "(PICS-1.1 " + S + " l (for \"http://a/\" r (a 1) for \"http://b/\" r (a 2)))"),
    ("every option once", '(PICS-1.1 ' + S + ' l by "x" generic t gen f for "http://a/" on "1994.11.05T08:15-0500" '
        'signature-RSA-MD5 "AAAA" until "1995.12.31T23:59-0000" exp "1995.12.31T23:59-0000" at "1994.11.05T08:15-0500" '
        'MIC-md5 "AAAA" md5 "AAAAAA==" comment "c" complete-label "http://a/l" full "http://a/l" '
        'extension (optional "http://x/e" 1 "x" "http://y/" "1994.11.05T08:15-0500" (1 (2 "z"))) '
        'extension (mandatory "http://x/f") r (a 1))'),
    ("a rating with every value form", "(PICS-1.1 " + S + " l r (a 1 b +1.5 c -2. d 0.0 e (1 2:3 4.5:6.5) f () g/h 1 i%20j 2))"),
    ("a transmit-name that is also a number", "(PICS-1.1 " + S + " l r (0.5 1))"),
    ("a category named l, r or labels", "(PICS-1.1 " + S + " l r (l 1 r 2 labels 3))"),
    ("a base64 string split over lines", '(PICS-1.1 ' + S + ' l signature-RSA-MD5 "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAA=" r (a 1))'),
    ("a service URL with every URL punctuation", "(PICS-1.1 \"http://u:p@h.example:80/a%20b/c;d?e=f&g#h\" l r (a 1))"),
]

HEADER_REJECT = [
    ("Protocol-Request without services", "Protocol-Request: {PICS-1.1 {params full}}",
     "Protocol-Request: {PICS-1.1 {params full {services \"http://a/\"}}}"),
    ("services with no URL", "Protocol-Request: {PICS-1.1 {params {services}}}", "Protocol-Request: {PICS-1.1 {params {services \"http://a/\"}}}"),
    ("services URL not quoted", "Protocol-Request: {PICS-1.1 {params {services http://a/}}}", "Protocol-Request: {PICS-1.1 {params {services \"http://a/\"}}}"),
    ("two completeness words", "Protocol-Request: {PICS-1.1 {params full short {services \"http://a/\"}}}", "Protocol-Request: {PICS-1.1 {params full {services \"http://a/\"}}}"),
    ("completeness after the services group", "Protocol-Request: {PICS-1.1 {params {services \"http://a/\"} full}}", "Protocol-Request: {PICS-1.1 {params full {services \"http://a/\"}}}"),
    ("completeness 'verbose' (grammar lists four; prose allows any alphanumeric, A10)", "Protocol-Request: {PICS-1.1 {params verbose {services \"http://a/\"}}}", "Protocol-Request: {PICS-1.1 {params short {services \"http://a/\"}}}"),
    ("extension whose first item is services (it is the services group)", "Protocol-Request: {PICS-1.1 {params {services x} {services \"http://a/\"}}}", "Protocol-Request: {PICS-1.1 {params {x} {services \"http://a/\"}}}"),
    ("empty extension", "Protocol-Request: {PICS-1.1 {params {} {services \"http://a/\"}}}", "Protocol-Request: {PICS-1.1 {params {x} {services \"http://a/\"}}}"),
    ("missing a closing brace", "Protocol-Request: {PICS-1.1 {params {services \"http://a/\"}}", "Protocol-Request: {PICS-1.1 {params {services \"http://a/\"}}}"),
    ("wrong version", "Protocol-Request: {PICS-1.0 {params {services \"http://a/\"}}}", "Protocol-Request: {PICS-1.1 {params {services \"http://a/\"}}}"),
    ("no params keyword", "Protocol-Request: {PICS-1.1 {services \"http://a/\"}}", "Protocol-Request: {PICS-1.1 {params {services \"http://a/\"}}}"),
    ("wrong header name", "Protocol: {PICS-1.1 {params {services \"http://a/\"}}}", "Protocol-Request: {PICS-1.1 {params {services \"http://a/\"}}}"),
]
HEADER_ACCEPT = [
    ("minimal request, one service", "Protocol-Request: {PICS-1.1 {params {services \"http://a/\"}}}"),
    ("two services, an extension and a quoted first item", "Protocol-Request: {PICS-1.1 {params signed {x 1 \"y z\"} {\"services\" a} {services \"http://a/\" \"http://b/\"}}}"),
    ("folded across lines", "Protocol-Request: {PICS-1.1 {params full\n   {services \"http://www.gcf.org/v2.5\"}}}"),
    ("upper-case header name and keywords", "PROTOCOL-REQUEST: {pics-1.1 {PARAMS FULL {SERVICES \"http://a/\"}}}"),
]
PROTO_REJECT = [
    ("Protocol with no PICS-Label", "Protocol: {PICS-1.1 {headers}}", "Protocol: {PICS-1.1 {headers PICS-Label}}"),
    ("Protocol with another header name", "Protocol: {PICS-1.1 {headers Other}}", "Protocol: {PICS-1.1 {headers PICS-Label}}"),
    ("Protocol missing a brace", "Protocol: {PICS-1.1 {headers PICS-Label}", "Protocol: {PICS-1.1 {headers PICS-Label}}"),
]

QUERY_REJECT = [
    ("no url", "GET /r?s=\"http%3A%2F%2Fa\" HTTP/1.0", "GET /r?u=\"http%3A%2F%2Fb\"&s=\"http%3A%2F%2Fa\" HTTP/1.0"),
    ("no service", "GET /r?u=\"http%3A%2F%2Fa\" HTTP/1.0", "GET /r?u=\"http%3A%2F%2Fa\"&s=\"http%3A%2F%2Fb\" HTTP/1.0"),
    ("service before url", "GET /r?s=\"x\"&u=\"y\" HTTP/1.0", "GET /r?u=\"y\"&s=\"x\" HTTP/1.0"),
    ("format before opt", "GET /r?format=full&opt=generic&u=\"y\"&s=\"x\" HTTP/1.0", "GET /r?opt=generic&format=full&u=\"y\"&s=\"x\" HTTP/1.0"),
    ("missing & before u", "GET /r?opt=generic\"u=\"y\"&s=\"x\" HTTP/1.0", "GET /r?opt=generic&u=\"y\"&s=\"x\" HTTP/1.0"),
    ("& before the first parameter", "GET /r?&u=\"y\"&s=\"x\" HTTP/1.0", "GET /r?u=\"y\"&s=\"x\" HTTP/1.0"),
    ("missing & between u and s", "GET /r?u=\"y\"s=\"x\" HTTP/1.0", "GET /r?u=\"y\"&s=\"x\" HTTP/1.0"),
    ("opt value unknown", "GET /r?opt=weird&u=\"y\"&s=\"x\" HTTP/1.0", "GET /r?opt=tree&u=\"y\"&s=\"x\" HTTP/1.0"),
    ("opt=generic%2Btree as in Appendix B 18.4 (the grammar's literal is generic+tree, A16)", "GET /r?opt=generic%2Btree&u=\"y\"&s=\"x\" HTTP/1.0", "GET /r?opt=generic+tree&u=\"y\"&s=\"x\" HTTP/1.0"),
    ("format value unknown (grammar lists four; prose allows others, A10)", "GET /r?format=weird&u=\"y\"&s=\"x\" HTTP/1.0", "GET /r?format=signed&u=\"y\"&s=\"x\" HTTP/1.0"),
    ("& inside the quotes (Appendix B queries, A17)", "GET /r?u=\"y&\"u=\"z\"&s=\"x\" HTTP/1.0", "GET /r?u=\"y\"&u=\"z\"&s=\"x\" HTTP/1.0"),
    ("a raw colon in the URL", "GET /r?u=\"http://a\"&s=\"x\" HTTP/1.0", "GET /r?u=\"http%3A%2F%2Fa\"&s=\"x\" HTTP/1.0"),
    ("a raw slash in the URL", "GET /r?u=\"a/b\"&s=\"x\" HTTP/1.0", "GET /r?u=\"a%2Fb\"&s=\"x\" HTTP/1.0"),
    ("a bad percent escape", "GET /r?u=\"a%zz\"&s=\"x\" HTTP/1.0", "GET /r?u=\"a%2f\"&s=\"x\" HTTP/1.0"),
    ("extension named s before the url", "GET /r?s=\"q\"&u=\"y\"&s=\"x\" HTTP/1.0", "GET /r?q=\"q\"&u=\"y\"&s=\"x\" HTTP/1.0"),
    ("extension named opt (must be the first parameter)", "GET /r?x=1&opt=tree&u=\"y\"&s=\"x\" HTTP/1.0", "GET /r?opt=tree&x=1&u=\"y\"&s=\"x\" HTTP/1.0"),
    ("extension named format after an extension", "GET /r?x=1&format=full&u=\"y\"&s=\"x\" HTTP/1.0", "GET /r?format=full&x=1&u=\"y\"&s=\"x\" HTTP/1.0"),
    ("extension after the urls", "GET /r?u=\"y\"&x=1&s=\"x\" HTTP/1.0", "GET /r?x=1&u=\"y\"&s=\"x\" HTTP/1.0"),
    ("no version", "GET /r?u=\"y\"&s=\"x\"", "GET /r?u=\"y\"&s=\"x\" HTTP/1.0"),
    ("no space after GET", "GET/r?u=\"y\"&s=\"x\" HTTP/1.0", "GET /r?u=\"y\"&s=\"x\" HTTP/1.0"),
    ("no question mark", "GET /r&u=\"y\"&s=\"x\" HTTP/1.0", "GET /r?u=\"y\"&s=\"x\" HTTP/1.0"),
    ("empty url", "GET /r?u=\"\"&s=\"x\" HTTP/1.0", "GET /r?u=\"y\"&s=\"x\" HTTP/1.0"),
]
QUERY_ACCEPT = [
    ("section 12.1 sample", "GET /Ratings?opt=generic&u=\"http%3A%2F%2Fwww.questionable.org%2Fimages\"&s=\"http%3A%2F%2Fwww.gcf.org%2Fv2.5\" HTTP/1.0"),
    ("all four opt values", None),  # expanded below
    ("an extension with a quoted value, before the urls", "GET /r?opt=tree&format=full&x=\"a b\"&u=\"y\"&s=\"x\" HTTP/1.0"),
    ("unquoted encodedURL reading (A14)", "GET /r?u=http%3A%2F%2Fa&s=http%3A%2F%2Fb HTTP/1.0"),
    ("lower-case get", "get /r?u=\"y\"&s=\"x\" HTTP/1.0"),
    ("first parameter is the extension", "GET /r?x=1&u=\"y\"&s=\"x\" HTTP/1.0"),
]


class Counter:
    def __init__(self):
        self.examined = 0
        self.fails = []

    def check(self, label, cond):
        self.examined += 1
        if not cond:
            self.fails.append(label)


def run_tests(verbose=True):
    c = Counter()
    # ---- grammar lint
    for kind, entries in (("tokens", ["labellist", "request-header", "request-header-prose", "protocol-header", "label-header"]),
                          ("chars", ["request-line", "get-as-written", "post"])):
        g = _grammar(kind)
        problems, unused = g.lint(entries)
        for p in problems:
            c.check("lint[%s]: %s" % (kind, p), False)
        c.check("lint[%s]: every rule referenced or an entry" % kind, not unused)
        if unused and verbose:
            print("  unused rules in %s grammar:" % kind, unused)
        c.check("lint[%s]: %d rules, no undefined reference" % (kind, len(g.rules)), not problems)
    # ---- label lists
    rej = acc = 0
    for name, bad, good in LABEL_REJECT:
        rb, rg = parse_labellist(bad), parse_labellist(good)
        c.check("label REJECT %s: bad rejected" % name, not rb)
        c.check("label REJECT %s: its repair accepted (%r)" % (name, rg), bool(rg))
        rej += 1
    for name, txt in LABEL_ACCEPT:
        r = parse_labellist(txt)
        c.check("label ACCEPT %s (%r)" % (name, r), bool(r))
        acc += 1
    # ---- headers
    for name, bad, good in HEADER_REJECT:
        c.check("header REJECT %s: bad rejected" % name, not parse_request_header(bad))
        c.check("header REJECT %s: repair accepted" % name, bool(parse_request_header(good)))
    for name, txt in HEADER_ACCEPT:
        c.check("header ACCEPT %s" % name, bool(parse_request_header(txt)))
    # the prose reading of completeness accepts what the grammar reading rejects
    v = "Protocol-Request: {PICS-1.1 {params verbose {services \"http://a/\"}}}"
    c.check("header: 'verbose' rejected by the grammar reading", not parse_request_header(v))
    c.check("header: 'verbose' accepted by the prose reading", bool(parse_request_header(v, prose=True)))
    for name, bad, good in PROTO_REJECT:
        c.check("Protocol REJECT %s: bad rejected" % name, not parse_protocol_header(bad))
        c.check("Protocol REJECT %s: repair accepted" % name, bool(parse_protocol_header(good)))
    c.check("PICS-Label header: section 11.1", bool(parse_label_header("PICS-Label:\n (PICS-1.1 " + S + " labels r (a 1))")))
    c.check("PICS-Label header without a list rejected", not parse_label_header("PICS-Label:"))
    c.check("PICS-Label header with the list unparenthesised rejected", not parse_label_header("PICS-Label: PICS-1.1 " + S + " l r (a 1)"))
    # ---- queries
    for name, bad, good in QUERY_REJECT:
        c.check("query REJECT %s: bad rejected" % name, not parse_request_line(bad))
        c.check("query REJECT %s: repair accepted" % name, bool(parse_request_line(good)))
    for name, txt in QUERY_ACCEPT:
        if txt is None:
            for o in ("generic", "normal", "tree", "generic+tree"):
                t = "GET /r?opt=%s&u=\"y\"&s=\"x\" HTTP/1.0" % o
                c.check("query ACCEPT opt=%s" % o, bool(parse_request_line(t)))
        else:
            c.check("query ACCEPT %s" % name, bool(parse_request_line(txt)))
    # the source's own reading (extension with no &, & optional): what it cannot write
    ext_amp = "GET /r?opt=tree&x=1&u=\"y\"&s=\"x\" HTTP/1.0"[:-9]
    c.check("as-written: extension after the first parameter is unwritable (A12)",
            not parse_request_line(ext_amp, "get-as-written"))
    c.check("derived: the same query is accepted", bool(parse_request_line(ext_amp + " HTTP/1.0")))
    c.check("as-written: a parameter list with no & at all is accepted (the [and] reading)",
            bool(parse_request_line("GET /r?u=\"y\"s=\"x\"", "get-as-written")))
    # the EXCLUDE hook is necessary: without it the same four instances are accepted
    hook_cases = [("h", t) for t in HEADER_REJECT if t[0].startswith("extension whose first")] + \
                 [("q", t) for t in QUERY_REJECT if t[0].startswith("extension named")]
    saved = dict(EXCLUDE)
    try:
        EXCLUDE.clear()
        for g in _G.values():
            g._lexmemo = {}
        for kind, (name, bad, good) in hook_cases:
            r = parse_request_header(bad) if kind == "h" else parse_request_line(bad)
            c.check("without the EXCLUDE hook the bad instance is wrongly accepted: " + name, bool(r))
    finally:
        EXCLUDE.update(saved)
        for g in _G.values():
            g._lexmemo = {}
    c.check("EXCLUDE restored and the bad instances rejected again", all(
        not (parse_request_header(b) if k == "h" else parse_request_line(b)) for k, (_, b, _g) in hook_cases))
    c.check("post: structure", bool(parse_request_line("post /r\r\n\r\nu=a&s=b", "post")))
    c.check("post: needs the blank line", not parse_request_line("post /r\r\nu=a&s=b", "post"))
    return c, rej, acc


def mutation_sweep(fixtures):
    """Every label list in `fixtures` ({name: text}) is accepted; each single-edit mutant that
    must be invalid is rejected. Returns (lists, mutants, still_accepted)."""
    lists = mutants = bad = 0
    survivors = []
    for name, text in fixtures.items():
        if not parse_labellist(text):
            continue
        lists += 1
        muts = []
        # delete each parenthesis in turn (always unbalances the list)
        for m in re.finditer(r"[()]", text):
            muts.append(("delete %r at %d" % (m.group(0), m.start()), text[:m.start()] + text[m.end():]))
        # delete each double quote in turn (always unbalances the strings, or fuses tokens)
        for m in re.finditer(r'"', text):
            muts.append(("delete quote at %d" % m.start(), text[:m.start()] + text[m.end():]))
        # break each keyword: ratings/labels/for/by/generic/on -> one letter dropped
        inq = [False] * (len(text) + 1)
        q = False
        for i, ch in enumerate(text):
            if ch == '"':
                q = not q
            inq[i] = q
        for m in re.finditer(r"\b(ratings|labels|generic|until|signature-RSA-MD5)\b", text):
            if inq[m.start()]:
                continue  # inside a quoted string the word is data, not a keyword
            w = m.group(0)
            muts.append(("drop last letter of %s at %d" % (w, m.start()), text[:m.end() - 1] + text[m.end():]))
        # drop the version token
        if "PICS-1.1" in text:
            muts.append(("drop the version", text.replace("PICS-1.1", "", 1)))
        # truncate before the final paren
        muts.append(("truncate the last character", text.rstrip()[:-1]))
        for desc, t in muts:
            mutants += 1
            if parse_labellist(t):
                bad += 1
                survivors.append("%s: %s" % (name, desc))
    return lists, mutants, survivors


def main():
    c, rej, acc = run_tests()
    fx = {}
    exdir = HERE.parent / "examples"
    for n in ("ex02-label-list-long.txt", "ex03-label-list-compact-full.txt", "ex04-label-list-minimal.txt", "ex05-multi-value.txt"):
        p = exdir / n
        if p.is_file():
            fx[n] = p.read_text(encoding="utf-8")
    lists, mutants, survivors = mutation_sweep(fx)
    c.check("mutation sweep examined at least one list", lists > 0)
    for s in survivors:
        c.check("mutant still accepted: " + s, False)
    print("check-grammar.derived.py")
    print("  grammar files: labels.derived.abnf + http-headers.derived.abnf (%d rules, token layer), bureau-query.derived.abnf (%d rules, character layer)"
          % (len(_grammar("tokens").order), len(_grammar("chars").order)))
    print("  label-list REJECT cases: %d (each with its minimal repair accepted); ACCEPT cases: %d" % (rej, acc))
    print("  mutation sweep: %d example lists, %d single-edit mutants, %d still accepted" % (lists, mutants, len(survivors)))
    print("  EXAMINED %d checks, FAILED %d" % (c.examined, len(c.fails)))
    for f in c.fails:
        print("  FAIL", f)
    return 1 if c.fails else 0


if __name__ == "__main__":
    sys.exit(main())

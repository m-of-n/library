#!/usr/bin/env python3
"""DERIVED - not verbatim. Written by this library, not copied from the source.

Canonical, advanced and transport S-expression reader/writer for
draft-ietf-spki-cert-structure-06 section 3 (stdlib only).

What section 3 specifies, and where each rule is implemented:

  3.1   canonical form: byte strings each prefixed by their decimal length and
        ":", plus the punctuation "()[]". The length is a non-negative ASCII
        decimal "with no unnecessary leading 0 digits". No white space exists
        in canonical form (the BNF has no white-space production).
  3.2   <byte-string>:: <bytes> | <display-type> <bytes> ;
        <bytes>:: <decimal> ":" {binary byte string of that length} ;
        <decimal>:: <nzddigit> <ddigit>* | "0" ;
        <display-type>:: "[" <bytes> "]" ;
  3.2.1 <integer>: a byte string; two's complement, MSB first; zero is the
        1-byte string 0x00, "not the empty string".
  3.3   <s-expr>:: "(" <byte-string> <s-part>* ")" ;  (no empty list; the
        first element is a byte string)
  3.4   advanced form: tokens (not starting with a digit, ended by white space
        or punctuation), quoted strings, white space between elements ignored;
        transport: base64 (RFC 2045) in braces "{}".
  3.6   advanced form: tokens, quoted strings "(under normal C string rules)",
        hex values delimited by "#", base64 values delimited by "|".

ASSUMPTIONS the draft leaves open, each flagged ASSUMPTION below:
  A1 the token alphabet (the draft only says "familiar token recognition
     rules"): here any character except white space and ()[]{}|#" , not
     starting with a digit. The draft's own examples need "/", ":" and "." in
     tokens (sysadmin/operators, http://www.internal.acme.com/accounting/).
  A2 C string escapes: \\a \\b \\f \\n \\r \\t \\v \\\\ \\" \\' \\? \\ooo \\xHH.
  A3 the advanced form also accepts a length-prefixed raw string N:bytes (the
     canonical byte-string), as [SEXP] does; the draft does not say.
  A4 a display type in the advanced form is written "[" <string> "]" before
     the string it modifies; the string inside may be any simple string form.
  A5 base64 inside "{}" and "|" must be RFC 2045 alphabet with "=" padding to
     a multiple of 4; characters outside the alphabet other than white space
     are errors (RFC 2045 says ignore them; a strict reader is chosen).
"""
import base64
import binascii
import re
from dataclasses import dataclass
from typing import Optional, Tuple, Union


class SexpError(ValueError):
    """A byte or text stream that is not a valid S-expression of its form."""


@dataclass(frozen=True)
class Atom:
    """A <byte-string>. `display` is the display type's bytes, or None.
    Equality includes the display type (3.2: "two strings with the same bytes
    will not be considered equal ... if they have unequal display types")."""
    data: bytes
    display: Optional[bytes] = None


@dataclass(frozen=True)
class Lst:
    items: Tuple["Node", ...]


Node = Union[Atom, Lst]

DIGITS = b"0123456789"
NZ = b"123456789"


# ---------------------------------------------------------------- canonical
def _parse_bytes(b: bytes, i: int):
    """<bytes>:: <decimal> ":" raw ;  returns (raw, next index)."""
    j = i
    if j >= len(b) or b[j:j + 1] not in [bytes([c]) for c in DIGITS]:
        raise SexpError(f"offset {i}: expected a decimal length")
    if b[j:j + 1] == b"0":
        j += 1  # "0" alone: no further digit may follow
    else:
        while j < len(b) and b[j] in DIGITS:
            j += 1
    # <decimal>:: <nzddigit> <ddigit>* | "0" -- "01:" is "0" then "1", not ":".
    if j >= len(b) or b[j:j + 1] != b":":
        raise SexpError(f"offset {j}: expected ':' after the length (leading zeros are not allowed)")
    n = int(b[i:j].decode("ascii"))
    start = j + 1
    if start + n > len(b):
        raise SexpError(f"offset {i}: length {n} runs past the end of the input")
    return b[start:start + n], start + n


def _parse_byte_string(b: bytes, i: int) -> Tuple[Atom, int]:
    """<byte-string>:: <bytes> | <display-type> <bytes> ;"""
    display = None
    if b[i:i + 1] == b"[":
        display, i = _parse_bytes(b, i + 1)
        if b[i:i + 1] != b"]":
            raise SexpError(f"offset {i}: expected ']' closing the display type")
        i += 1
        if b[i:i + 1] in (b"[", b"(", b")", b"]", b""):
            raise SexpError(f"offset {i}: a display type must be followed by <bytes>")
    raw, i = _parse_bytes(b, i)
    return Atom(raw, display), i


def _parse_sexpr(b: bytes, i: int) -> Tuple[Lst, int]:
    """<s-expr>:: "(" <byte-string> <s-part>* ")" ;"""
    if b[i:i + 1] != b"(":
        raise SexpError(f"offset {i}: expected '('")
    i += 1
    first, i = _first_string(b, i)
    items = [first]
    while True:
        c = b[i:i + 1]
        if c == b")":
            return Lst(tuple(items)), i + 1
        if c == b"(":
            sub, i = _parse_sexpr(b, i)
            items.append(sub)
        elif c == b"":
            raise SexpError(f"offset {i}: unterminated list")
        else:
            a, i = _parse_byte_string(b, i)
            items.append(a)


def _first_string(b: bytes, i: int):
    c = b[i:i + 1]
    if c == b")":
        raise SexpError(f"offset {i}: empty list (3: no empty lists are allowed)")
    if c == b"(":
        raise SexpError(f"offset {i}: the first element of a list must be a byte string")
    if c == b"":
        raise SexpError(f"offset {i}: unterminated list")
    return _parse_byte_string(b, i)


def parse_canonical(b: bytes, allow_atom: bool = False) -> Node:
    """Parse ONE canonical S-expression occupying all of `b`."""
    if not isinstance(b, (bytes, bytearray)):
        raise TypeError("canonical form is bytes")
    b = bytes(b)
    if allow_atom and b[:1] != b"(":
        node, i = _parse_byte_string(b, 0)
    else:
        node, i = _parse_sexpr(b, 0)
    if i != len(b):
        raise SexpError(f"offset {i}: {len(b) - i} trailing byte(s) after the S-expression")
    return node


def encode_atom(a: Atom) -> bytes:
    out = b""
    if a.display is not None:
        out += b"[" + str(len(a.display)).encode() + b":" + a.display + b"]"
    return out + str(len(a.data)).encode() + b":" + a.data


def encode(node: Node) -> bytes:
    """Canonical form of a parsed node (3.1: the unique representation)."""
    if isinstance(node, Atom):
        return encode_atom(node)
    if not node.items or not isinstance(node.items[0], Atom):
        raise SexpError("a list needs a byte string first (3.3)")
    return b"(" + b"".join(encode(x) for x in node.items) + b")"


# ---------------------------------------------------------------- transport
_B64 = re.compile(r"^[A-Za-z0-9+/]*={0,2}$")


def b64decode_strict(text: str) -> bytes:
    """RFC 2045 base64, white space ignored, padding required (ASSUMPTION A5)."""
    s = re.sub(r"\s+", "", text)
    if not _B64.match(s):
        raise SexpError("base64 contains a character outside the RFC 2045 alphabet")
    if len(s) % 4:
        raise SexpError("base64 length is not a multiple of 4 (missing '=' padding)")
    try:
        return base64.b64decode(s, validate=True)
    except binascii.Error as e:
        raise SexpError(f"base64: {e}")


def parse_transport(text: str) -> Node:
    """"{" base64(canonical) "}" per 3.4."""
    t = text.strip()
    if not (t.startswith("{") and t.endswith("}")):
        raise SexpError("transport form is enclosed in braces {}")
    return parse_canonical(b64decode_strict(t[1:-1]))


def encode_transport(node: Node, width: Optional[int] = None) -> str:
    s = base64.b64encode(encode(node)).decode("ascii")
    if width:
        s = "\n".join(s[k:k + width] for k in range(0, len(s), width))
    return "{" + s + "}"


# ----------------------------------------------------------------- advanced
_WS = " \t\r\n\f\v"
_PUNCT = set("()[]{}|#\"")
_HEX = set("0123456789abcdefABCDEF")
_ESC = {"a": 7, "b": 8, "f": 12, "n": 10, "r": 13, "t": 9, "v": 11, "\\": 92,
        '"': 34, "'": 39, "?": 63}


class _Adv:
    def __init__(self, s: str):
        self.s = s
        self.i = 0

    def ws(self):
        while self.i < len(self.s) and self.s[self.i] in _WS:
            self.i += 1

    def err(self, msg):
        raise SexpError(f"advanced form, char {self.i}: {msg}")

    def string(self) -> Atom:
        """one simple string form, optionally with a display type (A4)."""
        self.ws()
        display = None
        if self.i < len(self.s) and self.s[self.i] == "[":
            self.i += 1
            d = self.simple()
            self.ws()
            if self.i >= len(self.s) or self.s[self.i] != "]":
                self.err("expected ']' closing the display type")
            self.i += 1
            display = d.data
            self.ws()
        a = self.simple()
        return Atom(a.data, display)

    def simple(self) -> Atom:
        s = self.s
        if self.i >= len(s):
            self.err("expected a byte string")
        c = s[self.i]
        if c == '"':
            return Atom(self.quoted())
        if c == "#":
            return Atom(self.delimited("#", _HEX, bytes.fromhex))
        if c == "|":
            return Atom(self.delimited("|", None, b64decode_strict))
        if c.isdigit():
            # ASSUMPTION A3: length-prefixed raw string; tokens cannot start with a digit.
            j = self.i
            while j < len(s) and s[j].isdigit():
                j += 1
            if j < len(s) and s[j] == ":" and (s[self.i] != "0" or j == self.i + 1):
                n = int(s[self.i:j])
                raw = s[j + 1:j + 1 + n]
                if len(raw) != n:
                    self.err("raw length runs past the end of the input")
                self.i = j + 1 + n
                return Atom(raw.encode("latin-1"))
            self.err("a token may not start with a digit (3.4)")
        if c in _PUNCT or c in _WS:
            self.err(f"unexpected {c!r}")
        j = self.i
        while j < len(s) and s[j] not in _PUNCT and s[j] not in _WS:
            j += 1
        tok = s[self.i:j]
        self.i = j
        return Atom(tok.encode("latin-1"))

    def delimited(self, d, alphabet, decoder) -> bytes:
        s = self.s
        j = s.find(d, self.i + 1)
        if j < 0:
            self.err(f"unterminated {d}...{d} value")
        raw = s[self.i + 1:j]
        body = re.sub(r"\s+", "", raw)
        if alphabet is not None:
            if any(ch not in alphabet for ch in body):
                self.err("non-hex digit in a #...# value")
            if len(body) % 2:
                self.err("odd number of hex digits")
        self.i = j + 1
        return decoder(body)

    def quoted(self) -> bytes:
        s = self.s
        i = self.i + 1
        out = bytearray()
        while True:
            if i >= len(s):
                self.err("unterminated quoted string")
            c = s[i]
            if c == '"':
                self.i = i + 1
                return bytes(out)
            if c == "\\":
                i += 1
                if i >= len(s):
                    self.err("dangling backslash")
                e = s[i]
                if e in _ESC:
                    out.append(_ESC[e]); i += 1
                elif e == "x":
                    h = s[i + 1:i + 3]
                    if len(h) != 2 or any(x not in _HEX for x in h):
                        self.err("bad \\x escape")
                    out.append(int(h, 16)); i += 3
                elif e in "01234567":
                    j = i
                    while j < len(s) and j < i + 3 and s[j] in "01234567":
                        j += 1
                    v = int(s[i:j], 8)
                    if v > 255:
                        self.err("octal escape above 255")
                    out.append(v); i = j
                else:
                    self.err(f"unknown escape \\{e}")
            else:
                out.extend(c.encode("latin-1"))
                i += 1

    def sexpr(self) -> Lst:
        self.ws()
        if self.i >= len(self.s) or self.s[self.i] != "(":
            self.err("expected '('")
        self.i += 1
        self.ws()
        if self.i < len(self.s) and self.s[self.i] == ")":
            self.err("empty list (3: no empty lists are allowed)")
        if self.i < len(self.s) and self.s[self.i] == "(":
            self.err("the first element of a list must be a byte string")
        items = [self.string()]
        while True:
            self.ws()
            if self.i >= len(self.s):
                self.err("unterminated list")
            c = self.s[self.i]
            if c == ")":
                self.i += 1
                return Lst(tuple(items))
            if c == "(":
                items.append(self.sexpr())
            else:
                items.append(self.string())


def parse_advanced(text: str) -> Node:
    """ONE advanced-form S-expression filling `text` (white space around it ok)."""
    p = _Adv(text)
    node = p.sexpr()
    p.ws()
    if p.i != len(text):
        p.err("trailing text after the S-expression")
    return node


def parse_advanced_many(text: str):
    """Several advanced S-expressions one after another."""
    p = _Adv(text)
    out = []
    p.ws()
    while p.i < len(text):
        out.append(p.sexpr())
        p.ws()
    return out


def parse_any(text: str) -> Node:
    """transport if it starts with '{', otherwise advanced."""
    t = text.strip()
    return parse_transport(t) if t.startswith("{") else parse_advanced(t)


# --------------------------------------------------------------- rendering
_TOKEN = re.compile(r'^[^\s()\[\]{}|#"0-9][^\s()\[\]{}|#"]*$')


def to_advanced(node: Node, indent: Optional[int] = None) -> str:
    """Advanced-form text for a node (tokens where legal, else base64)."""
    def atom(a: Atom) -> str:
        try:
            t = a.data.decode("ascii")
        except UnicodeDecodeError:
            t = None
        if t is not None and _TOKEN.match(t):
            s = t
        else:
            s = "|" + base64.b64encode(a.data).decode() + "|"
        if a.display is not None:
            d = a.display.decode("ascii")
            s = "[" + (d if _TOKEN.match(d) else '"' + d + '"') + "]" + s
        return s

    def go(n: Node) -> str:
        if isinstance(n, Atom):
            return atom(n)
        return "(" + " ".join(go(x) for x in n.items) + ")"
    return go(node)


# ---------------------------------------------------------------- integers
def decode_integer(a: Atom) -> int:
    """3.2.1: signed two's complement, most significant byte first. The empty
    string is not an integer (zero is the single byte 0x00)."""
    if not isinstance(a, Atom):
        raise SexpError("an <integer> is a byte string")
    if a.data == b"":
        raise SexpError("3.2.1: the integer 0 is the 1-byte string 0x00, not the empty string")
    return int.from_bytes(a.data, "big", signed=True)


def encode_integer(n: int) -> Atom:
    """Shortest two's complement; zero is b'\\x00' (3.2.1)."""
    length = 1
    while True:
        try:
            return Atom(n.to_bytes(length, "big", signed=True))
        except OverflowError:
            length += 1


# -------------------------------------------------------------------- dates
_DATE = re.compile(r"^(\d{4})-(\d{2})-(\d{2})_(\d{2}):(\d{2}):(\d{2})$")


def check_date(a: Atom) -> None:
    """4.9.1: ASCII YYYY-MM-DD_HH:MM:SS, always UTC; compared as byte strings.
    The draft fixes the shape only; the range checks are ASSUMPTIONS (A6):
    month 1-12, day 1-31, hour 0-23, minute 0-59, second 0-59 (no leap second
    is stated)."""
    try:
        t = a.data.decode("ascii")
    except UnicodeDecodeError:
        raise SexpError("4.9.1: a date is an ASCII byte string")
    m = _DATE.match(t)
    if not m:
        raise SexpError("4.9.1: a date has the form YYYY-MM-DD_HH:MM:SS")
    y, mo, d, h, mi, s = map(int, m.groups())
    if not (1 <= mo <= 12 and 1 <= d <= 31 and h <= 23 and mi <= 59 and s <= 59):
        raise SexpError("4.9.1: date field out of range")
    if a.display is not None:
        raise SexpError("4.9.1: a date carries no display type")


if __name__ == "__main__":
    import sys
    data = sys.stdin.buffer.read()
    try:
        node = parse_canonical(data)
        print(to_advanced(node))
    except SexpError as e:
        sys.exit(f"not canonical: {e}")

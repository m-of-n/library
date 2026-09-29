"""BCP 14 (RFC 2119 / RFC 8174) keyword counting, shared by bcp14-count and validate.

Only UPPERCASE keywords are normative (RFC 8174). Longest match first, so
"MUST NOT" counts once, not as MUST plus a stray NOT. The boilerplate
paragraph that *defines* the keywords is excluded — it quotes every keyword
and constrains nothing.
"""
import re

KEYWORDS = ["MUST NOT", "SHALL NOT", "SHOULD NOT", "NOT RECOMMENDED",
            "MUST", "SHALL", "SHOULD", "RECOMMENDED", "REQUIRED", "MAY", "OPTIONAL"]
_RX = re.compile(r"(?<![A-Za-z])(" + "|".join(k.replace(" ", r"\s+") for k in KEYWORDS) + r")(?![A-Za-z])")
_BOILERPLATE = re.compile(r"The key words .{0,400}?(?:capitals|interpreted as described)[^.]*\.",
                          re.S | re.I)


def strip_boilerplate(text):
    return _BOILERPLATE.sub(" ", text)


def count(text, boilerplate=True):
    if boilerplate:
        text = strip_boilerplate(text)
    return len(_RX.findall(text))


def by_keyword(text):
    out = {}
    for m in _RX.findall(strip_boilerplate(text)):
        k = re.sub(r"\s+", " ", m)
        out[k] = out.get(k, 0) + 1
    return out

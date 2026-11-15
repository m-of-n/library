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


# ---------------------------------------------------------------------------
# Vocabularies (library#69). BCP 14 above is the default and is unchanged.
#
# `directives` is the verbal-form set of the ETSI Drafting Rules clause 3.2
# and ISO/IEC Directives Part 2 clause 7: requirement (shall, shall not),
# recommendation (should, should not), permission (may, need not) and
# possibility (can, cannot). They bind in LOWERCASE — there is no capitals
# convention — so a sentence-initial capital counts too. `must` is counted
# although the ETSI rules forbid it outside a direct citation: a `must` in a
# deliverable is exactly what an extractor needs to see. `will` is in the
# ETSI list but states no provision, and is left to the candidate cues.
#
# "May" followed by a year is the month, and is not counted.
# ---------------------------------------------------------------------------
DIRECTIVES = ["shall not", "should not", "must not", "need not",
              "shall", "should", "must", "may", "cannot", "can"]


def _ci(word):
    return "".join(f"[{c.upper()}{c}]" if i == 0 else c for i, c in enumerate(word))


_DRX = re.compile(r"(?<![A-Za-z-])(" + "|".join(
    r"\s+".join(_ci(w) if j == 0 else w for j, w in enumerate(k.split()))
    for k in DIRECTIVES) + r")(?![A-Za-z-])(?!\s+\d{4})")
_DBOILERPLATE = re.compile(
    r"In the present document \"shall\".{0,400}?interpreted as described.{0,200}?\.(?=\s|$)"
    r"|\"must\" and \"must not\" are NOT allowed[^.]*\.", re.S)

VOCABULARIES = {"bcp14": KEYWORDS, "directives": DIRECTIVES}


def regex(vocab="bcp14"):
    return _DRX if vocab == "directives" else _RX


def canonical(match, vocab="bcp14"):
    k = re.sub(r"\s+", " ", match)
    return k.lower() if vocab == "directives" else k


def strip_boilerplate_v(text, vocab="bcp14"):
    return (_DBOILERPLATE if vocab == "directives" else _BOILERPLATE).sub(" ", text)


def count_v(text, vocab="bcp14", boilerplate=True):
    if vocab == "bcp14":
        return count(text, boilerplate)
    if boilerplate:
        text = strip_boilerplate_v(text, vocab)
    return len(_DRX.findall(text))


def by_keyword_v(text, vocab="bcp14"):
    if vocab == "bcp14":
        return by_keyword(text)
    out = {}
    for m in _DRX.findall(strip_boilerplate_v(text, vocab)):
        k = canonical(m, vocab)
        out[k] = out.get(k, 0) + 1
    return out

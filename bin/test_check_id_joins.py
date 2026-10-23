#!/usr/bin/env python3
"""Regression tests for bin/check-id-joins --quote-join. Run in CI; no deps.

Every case here is a scoping decision that cost a measurement to find. The
first version of this check flagged 9135 of 9171 quotation/citation pairs
library-wide; scoping it to 4 took seven iterations, and each filter below is
one of them. hazards.md #7: "the first version of any new check over-reports"
— five for five now, this being the fifth.

The two numbers to protect: the check must still catch the three wrong ids it
was built for (pinned in test_detects_*), and must stay quiet on the shapes
that are correct (test_accepts_*).
"""
import importlib.machinery
import importlib.util
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
_loader = importlib.machinery.SourceFileLoader("cij", str(HERE / "check-id-joins"))
_spec = importlib.util.spec_from_file_location("cij", HERE / "check-id-joins",
                                               loader=_loader)
cij = importlib.util.module_from_spec(_spec)
_loader.exec_module(cij)

fail = 0


def check(name, got, want):
    global fail
    if got != want:
        fail += 1
        print(f"FAIL {name}\n  want {want!r}\n  got  {got!r}")


# --- _norm strips comment continuation markers ------------------------------
# rfc-8742 quoted a requirement verbatim inside an .abnf comment block, so the
# span came back with the `;` marker embedded mid-sentence.
check("comment marker stripped from a wrapped quotation",
      cij._norm("In short, concatenating zero or more encoded CBOR data\n"
                "  ; items generates a CBOR Sequence."),
      "In short, concatenating zero or more encoded CBOR data items "
      "generates a CBOR Sequence.")

# --- _carries resolves a marked elision segment by segment ------------------
# An elision is a declared, visible quotation shape here. Plain substring
# matching fails on every one, and they were the largest false-positive class
# once multi-id attribution was handled.
TARGET = ("When using a generic rule, the formal parameters are bound to the "
          "actual arguments supplied in the rule name of the invocation, as if "
          "there were a rule for each invocation.")
check("elided quotation carries",
      cij._carries("the formal parameters are bound to the actual arguments "
                   "supplied … as if there were a rule", TARGET), True)
check("ascii ellipsis carries too",
      cij._carries("the formal parameters are bound ... there were a rule",
                   TARGET), True)
check("segments out of order do NOT carry",
      cij._carries("there were a rule … the formal parameters are bound",
                   TARGET), False)
check("a span from another sentence does not carry",
      cij._carries("this control is not a representation constraint", TARGET),
      False)

# --- _is_prose rejects structure that merely sits between two quote marks ---
check("json braces are not a quotation",
      cij._is_prose("} } } } }, {"), False)
check("a yaml flow mapping is not a quotation",
      cij._is_prose(", schema: ../schema/vsa-v1.derived.schema.json, "
                    "expected: invalid, result:"), False)
check("a real sentence is prose",
      cij._is_prose("The total length of the label is 12 bytes."), True)
check("one colon key does not disqualify prose",
      cij._is_prose("In order to be in the 4-byte range, and so that "
                    "implementations: see the note."), True)

# --- _adjacent_quote: attribution, not proximity ----------------------------
# A 120-character window with "no long word between" flagged nearly everything;
# only true adjacency distinguishes an attribution from a nearby quotation.
Q = '"The total length of the label is 12 bytes."'
check("quote then citation, separated by ` (`",
      cij._adjacent_quote(f'  ; {Q} (rfc-9277#R-0062)', 48, 63),
      "The total length of the label is 12 bytes.")
check("citation then quote, separated by `): `",
      cij._adjacent_quote(f'  ; (rfc-9277#R-0040): {Q}', 6, 21),
      "The total length of the label is 12 bytes.")
check("prose between quote and citation is NOT an attribution",
      cij._adjacent_quote(
          f'{Q} and the document says elsewhere that (rfc-9277#R-0062)',
          44 + 38, 44 + 53), None)
check("a yamlish span is never a quotation",
      cij._adjacent_quote('"- name: protected\n  index: 0\n  type: bstr\n'
                          '  required: true" (rfc-9052#R-0006)', 60, 75), None)

# --- nested quote marks: the silent under-report ---------------------------
# QUOTE's character class excludes `"`, so a quotation CONTAINING a nested mark
# matched nothing and the check collected ZERO pairs on the lane it exists for
# — 11 duplicate-text groups over 23 requirements — while reporting clean.
NEST = ('hashAlg is "an integer or a string containing the hash algorithm '
        'identifier of the algorithm registered in the "COSE Algorithms" '
        'registry" (rfc-9360#R-0041).')
check("a quotation containing a nested pair is found",
      cij._adjacent_quote(NEST, NEST.index("(rfc-9360") + 1,
                          NEST.index("(rfc-9360") + 16),
      'an integer or a string containing the hash algorithm identifier of the '
      'algorithm registered in the "COSE Algorithms" registry')

# ...but the fallback must not WELD two adjacent quotations with prose between
# them. Both shapes have two interior marks; they differ in whether the first
# is an opener or a closer. Longest-first plus an even count alone took the
# library-wide count from 4 to 101.
WELD = ('"a review by the maintainers of the protocol" and `party` appears at '
        'line 403, inside "is in" (rfc-9054#R-0025).')
check("two adjacent quotations are not welded into one",
      cij._adjacent_quote(WELD, WELD.index("(rfc-9054") + 1,
                          WELD.index("(rfc-9054") + 16), None)

# --- the single quote is an OPENER ------------------------------------------
# The library's commonest attributed shape is a YAML single-quoted scalar that
# opens on the quotation itself, so the `"` is preceded by `'` and nothing
# else. Omitting `'` from _OPENS is why the check saw 25 of rfc-8747's 38
# pairs and printed 25 as its coverage.
SQ = ("""        quoted_evidence:\n          - '"The COSE_Key representation """
      """is used as the plaintext when encrypting the key." """
      """(rfc-8747#R-0047)'""")
check("a quotation opening inside a single-quoted scalar is found",
      cij._adjacent_quote(SQ, SQ.index("(rfc-8747") + 1,
                          SQ.index("(rfc-8747") + 16),
      "The COSE_Key representation is used as the plaintext when "
      "encrypting the key.")
check("an apostrophe between word characters still opens nothing",
      cij._OPENS.search("don"), None)

# --- more than one interior pair -------------------------------------------
# Admitting exactly one pair was one short of what the library writes: a
# sentence quoting two registry names in one breath. The ORIENTATION test, not
# the count, is what excludes welding, so the rule generalises without
# weakening — WELD above still returns None.
TWO = ('"This specification establishes the IANA "CWT Confirmation Methods" '
       'registry for CWT "cnf" member values." (rfc-8747#R-0107)')
check("a quotation containing two nested pairs is found",
      cij._adjacent_quote(TWO, TWO.index("(rfc-8747") + 1,
                          TWO.index("(rfc-8747") + 16),
      'This specification establishes the IANA "CWT Confirmation Methods" '
      'registry for CWT "cnf" member values.')

# --- JSON structure is structure, whatever its separators look like ---------
# Generalising the pair count exposed this: `":"` separators between spaces are
# both opener- and closer-shaped, so rfc-9679's derived JSON welded into four
# "quotations". _is_prose is the test in a position to say so, and it required
# a word character immediately before the colon, which JSON never has.
check("a json object span is not a quotation",
      cij._is_prose('"layout": "<prefix> ":" <hash algorithm identifier>", '
                    '"separator": ":", "requirements": ['), False)

# --- `(rec#R-0134)'s section` attributes a SECTION, not a sentence ----------
check("the possessive-section idiom is an attribution to a section",
      bool(cij._OF_SECTION.match("`'s section) says byte strings are")), True)
check("a bare citation is not the possessive idiom",
      bool(cij._OF_SECTION.match(") and Appendix D: the prelude")), False)

total = 25
print(f"test_check_id_joins: {total - fail}/{total} passed")
sys.exit(1 if fail else 0)

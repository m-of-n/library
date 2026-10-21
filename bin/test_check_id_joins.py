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

total = 17
print(f"test_check_id_joins: {total - fail}/{total} passed")
sys.exit(1 if fail else 0)

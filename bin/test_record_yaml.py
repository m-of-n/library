#!/usr/bin/env python3
"""Regression tests for bin/_record_yaml.py. Run in CI; no dependencies.

Companion to test_yaml.py, which covers bin/_yaml.py only. _record_yaml.py had
no tests, which is how the id-fragment bug below survived: the two parsers
disagreed about `#` for months and nothing compared them.

Each case is a bug that shipped silently at least once.
"""
import pathlib, sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from _record_yaml import YamlParser
from _yaml import parse as miniyaml


def parse(src):
    return YamlParser(src, "<test>").parse()


CASES = [
    # library#39: every requirement and vector id in an artifact collapsed to
    # the bare record name, because `#` was treated as a comment wherever it
    # appeared. rfc-8949's 232 vectors all parsed as the single id "rfc-8949".
    # YAML opens a comment at `#` only when it follows whitespace.
    ("id fragment kept", "id: rfc-8949#V-0001\n", {"id": "rfc-8949#V-0001"}),
    ("requirement id fragment kept", "id: rfc-9052#R-0099\n", {"id": "rfc-9052#R-0099"}),
    ("url fragment kept", "u: https://x.org/a#frag\n", {"u": "https://x.org/a#frag"}),
    # Note: _record_yaml coerces numeric scalars to int where _yaml keeps
    # strings. That difference is intended and is not what these cases test.
    ("trailing comment stripped", "n: 50   # bin/bcp14-count\n", {"n": 50}),
    ("comment after single space stripped", "n: 50 # c\n", {"n": 50}),
    ("whole-line comment dropped", "# just a comment\nn: 1\n", {"n": 1}),
    ("hash inside double quotes kept", 'n: "a # b"\n', {"n": "a # b"}),
    ("hash inside single quotes kept", "n: 'a # b'\n", {"n": "a # b"}),
    ("comment after a closing quote is dropped", 'n: "a # b"   # trailing\n', {"n": "a # b"}),
    ("id fragment in a sequence of maps",
     "requirements:\n  - id: rfc-8949#R-0001\n    verb: MUST\n  - id: rfc-8949#R-0002\n    verb: MAY\n",
     {"requirements": [{"id": "rfc-8949#R-0001", "verb": "MUST"},
                       {"id": "rfc-8949#R-0002", "verb": "MAY"}]}),
    ("nested maps survive", "relations:\n  see_also:\n    - x\n    - y\n",
     {"relations": {"see_also": ["x", "y"]}}),
    # library#39: a block scalar on the FIRST key of a sequence item raised
    # "unexpected indent". _map_into handled it for every LATER key, so
    # `- name: a` + `note: >` parsed while `- note: >` did not — the branch was
    # simply missing from parse_list. bin/_yaml.py had it right.
    ("block scalar as a sequence item's first key",
     "gaps:\n  - note: >\n      one two\n      three\n",
     {"gaps": [{"note": "one two three"}]}),
    ("block scalar as a later key still works",
     "items:\n  - name: a\n    note: >\n      x y\n",
     {"items": [{"name": "a", "note": "x y"}]}),
    ("literal block scalar as a first key",
     "gaps:\n  - note: |-\n      line one\n      line two\n",
     {"gaps": [{"note": "line one\nline two"}]}),
    ("a plain value that merely starts with > is not a block scalar",
     "gaps:\n  - note: >text\n",
     {"gaps": [{"note": ">text"}]}),
    # Double-quoted escapes resolved in ONE left-to-right pass. This reader
    # used four chained str.replace() calls, which rescanned their own output:
    # a doubled backslash followed by `n` is an escaped backslash and then the
    # letter `n`, but the chain turned it into a backslash and a real NEWLINE,
    # corrupting verbatim requirement texts that quote an escape as itself.
    ("a doubled backslash before n stays a backslash and an n",
     'k: "joined by \\\\n, no trailing newline"\n',
     {"k": "joined by \\n, no trailing newline"}),
    ("a doubled backslash before t stays a backslash and a t",
     "k: \"the char '\\\\t' (tab)\"\n", {"k": "the char '\\t' (tab)"}),
    ("a lone escaped newline and tab still resolve",
     'k: "one\\ntwo\\tthree"\n', {"k": "one\ntwo\tthree"}),
    # Escapes outside the table are left exactly as written, because the
    # records using them are about escape notation itself: the CBOR/EDN test
    # vectors carry brace-form literals and rfc-9804 prose names hex escapes.
    ("a brace-form EDN literal is left alone",
     'k: "D\\u{6f}mino"\n', {"k": "D\\u{6f}mino"}),
    ("a hex escape is left alone",
     'k: "\\xFE is the same octet"\n', {"k": "\\xFE is the same octet"}),
]

fail = 0
for name, src, want in CASES:
    got = parse(src)
    if got != want:
        fail += 1
        print(f"FAIL {name}\n  want {want!r}\n  got  {got!r}")

# The two parsers must agree about WHERE a comment starts. They disagreed
# silently before library#39, and bin/validate reads artifacts with one while
# bin/ingest and bin/fetch-source read records with the other. Values are
# compared as strings, because the parsers differ on numeric coercion by
# design and that is not what is under test here.
AGREE = [
    "id: rfc-8949#V-0001\n",
    "n: 50   # comment\n",
    'n: "a # b"   # trailing\n',
    "u: https://x.org/a#frag\n",
    "t: ends in a word # then a comment\n",
    # Both readers must also agree about where a block scalar may start.
    "gaps:\n  - note: >\n      one two\n",
    "items:\n  - name: a\n    note: >\n      x y\n",
    # And about double-quoted escapes. _yaml resolved NONE of them while this
    # reader resolved four, so 435 values across 46 records read differently
    # under the two — 72 of them verbatim requirement texts (library#39).
    'k: "she said \\"hi\\" twice"\n',
    'k: "joined by \\\\n, no trailing newline"\n',
    "k: \"the char '\\\\t' (tab)\"\n",
    'k: "D\\u{6f}mino"\n',
    'k: "\\xFE is the same octet"\n',
]
def _norm(v):
    """Compare structure and text, not chomping or scalar typing.

    The two readers differ on both by design: _yaml keeps a folded scalar's
    trailing newline and returns every scalar as a string, _record_yaml strips
    and coerces. Neither is what these cases test.
    """
    if isinstance(v, dict):
        return {k: _norm(x) for k, x in v.items()}
    if isinstance(v, list):
        return [_norm(x) for x in v]
    return str(v).strip()


for src in AGREE:
    a = _norm(parse(src))
    b = _norm(miniyaml(src))
    if a != b:
        fail += 1
        print(f"FAIL parsers disagree on {src!r}\n  _record_yaml {a!r}\n  _yaml        {b!r}")

total = len(CASES) + len(AGREE)
print(f"test_record_yaml: {total - fail}/{total} passed")
sys.exit(1 if fail else 0)

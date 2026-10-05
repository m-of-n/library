#!/usr/bin/env python3
"""Regression tests for bin/_yaml.py. Run in CI; no dependencies.

Each case is a bug that shipped silently at least once (library#43: the
block-scalar bug was rediscovered three times before being fixed).
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from _yaml import parse

CASES = [
    ("literal strip",  "a: 1\nb: |-\n  line one\n  line two\nc: 3\n",
     {"a": "1", "b": "line one\nline two", "c": "3"}),
    ("literal clip",   "b: |\n  x\n  y\n\nc: 3\n", {"b": "x\ny\n", "c": "3"}),
    ("literal keep",   "b: |+\n  x\n\n\nc: 3\n", {"b": "x\n\n\n", "c": "3"}),
    ("folded",         "b: >\n  one\n  two\n\n  three\nc: 3\n", {"b": "one two\nthree\n", "c": "3"}),
    ("folded strip",   "b: >-\n  one\n  two\n", {"b": "one two"}),
    ("colon in block does not create keys",
     "answer: >\n  It settles: non-equivocation.\n  note: not a key\nnext: 1\n",
     {"answer": "It settles: non-equivocation. note: not a key\n", "next": "1"}),
    ("block in sequence-of-maps",
     "v:\n  - id: 1\n    expected: |-\n      {\"a\":1}\n  - id: 2\n    expected: x\n",
     {"v": [{"id": "1", "expected": '{"a":1}'}, {"id": "2", "expected": "x"}]}),
    ("nested maps survive", "relations:\n  see_also:\n    - x\n    - y\n",
     {"relations": {"see_also": ["x", "y"]}}),
    ("multi-key sequence items", "f:\n  - name: a\n    type: b\n",
     {"f": [{"name": "a", "type": "b"}]}),
    ("trailing comment stripped", "n: 50   # bin/bcp14-count\n", {"n": "50"}),
    ("hash inside quotes kept", 'n: "a # b"\n', {"n": "a # b"}),
    ("url fragment kept", "u: https://x.org/a#frag\n", {"u": "https://x.org/a#frag"}),
    ("comment after a closing quote is dropped (from the Threat-Radar fork, #49)",
     'n: "a # b"   # trailing\n', {"n": "a # b"}),
    ("doubled single quote inside a single-quoted scalar", "n: 'it''s'  # c\n", {"n": "it''s"}),
    ("comment-looking line inside a block is content", "b: |-\n  # not a comment\nc: 1\n",
     {"b": "# not a comment", "c": "1"}),
]

fail = 0
for name, src, want in CASES:
    got = parse(src)
    if got != want:
        fail += 1
        print(f"FAIL {name}\n  want {want!r}\n  got  {got!r}")
print(f"test_yaml: {len(CASES) - fail}/{len(CASES)} passed")
sys.exit(1 if fail else 0)

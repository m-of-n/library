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
    ("doubled single quote inside a single-quoted scalar", "n: 'it''s'  # c\n", {"n": "it's"}),
    ("comment-looking line inside a block is content", "b: |-\n  # not a comment\nc: 1\n",
     {"b": "# not a comment", "c": "1"}),
    # A flow collection is returned as its own text, not parsed — 14,000-odd
    # sites in the library rely on that. These pin the thing it must NOT do:
    # return a truncated prefix when the collection wraps. Three constrained_by
    # lists in rfc-8392 silently lost every id after their first line (#39).
    ("single-line flow sequence is returned whole",
     'c: ["a#R-0001", "a#R-0002"]\nd: 1\n',
     {"c": '["a#R-0001", "a#R-0002"]', "d": "1"}),
    ("wrapped flow sequence keeps its continuation, and the next key survives",
     'c: ["a#R-0001", "a#R-0002",\n     "a#R-0003"]\nd: 1\n',
     {"c": '["a#R-0001", "a#R-0002", "a#R-0003"]', "d": "1"}),
    ("a flow sequence wrapped over three lines",
     'c: ["x",\n    "y",\n    "z"]\nd: 1\n',
     {"c": '["x", "y", "z"]', "d": "1"}),
    ("wrapped flow sequence inside a sequence-of-maps",
     'f:\n  - n: 1\n    ids: ["a",\n           "b"]\n    keep: yes\n',
     {"f": [{"n": "1", "ids": '["a", "b"]', "keep": "yes"}]}),
    ("a wrapped flow map is joined too",
     'c: {a: 1,\n    b: 2}\nd: 3\n', {"c": "{a: 1, b: 2}", "d": "3"}),
    ("[] and {} are still the empty collections, not text",
     "a: []\nb: {}\n", {"a": [], "b": {}}),
    ("a bracket inside a block scalar is not a flow collection",
     'b: |-\n  "reputons": [\n    1\n  ]\nc: 1\n',
     {"b": '"reputons": [\n  1\n]', "c": "1"}),
    # A quoted scalar that wraps. 71 lines in the library do this, most of them
    # `text:` fields in requirements.yaml — the one field FX-1's verbatim
    # checks exist to read. The parser used to keep the first line AND its
    # opening quote, so the value began with a stray " and ended mid-sentence.
    ("wrapped double-quoted value folds onto one line",
     'k: "one two\n   three."\nb: 1\n', {"k": "one two three.", "b": "1"}),
    ("wrapped quoted value as a bare sequence item",
     'a:\n  - "one two\n     three four."\nb: 1\n',
     {"a": ["one two three four."], "b": "1"}),
    ("wrapped quoted value inside a sequence-of-maps",
     'f:\n  - text: "one two\n           three."\n    kind: stated\n',
     {"f": [{"text": "one two three.", "kind": "stated"}]}),
    ("a single-quoted value wraps too",
     "k: 'one two\n   three.'\nb: 1\n", {"k": "one two three.", "b": "1"}),
    ("an escaped quote does not terminate the scalar early",
     'k: "she said \\"hi\\" twice"\nb: 1\n',
     {"k": 'she said \\"hi\\" twice', "b": "1"}),
    ("a doubled single quote does not terminate the scalar early",
     "k: 'it''s fine'\nb: 1\n", {"k": "it's fine", "b": "1"}),
    # A DOCUMENTED LIMITATION, pinned so it is a decision and not a surprise.
    # A wrapped scalar stops at any line that reads as the next key, because
    # this library contains genuinely unterminated quoted scalars —
    # draft-ietf-cbor-edn-literals' requirements.yaml line 152 ends with no
    # closing quote — and continuing through one swallowed the `verb:` entry
    # after it. So a continuation line whose first token looks like a key ends
    # the scalar instead. No real continuation line in the library has that
    # shape (measured: the fix shortens no value anywhere), and the cost of
    # guessing the other way is corrupting the neighbouring entry.
    ("a wrapped scalar stops at a line that reads as the next key",
     'k: "one two\n   three: not a key"\nb: 1\n',
     {"k": '"one two', "three": 'not a key"', "b": "1"}),
    ("a continuation line that is plainly prose is still folded in",
     'k: "one two\n   three and four"\nb: 1\n',
     {"k": "one two three and four", "b": "1"}),
]

fail = 0
for name, src, want in CASES:
    got = parse(src)
    if got != want:
        fail += 1
        print(f"FAIL {name}\n  want {want!r}\n  got  {got!r}")
print(f"test_yaml: {len(CASES) - fail}/{len(CASES)} passed")
sys.exit(1 if fail else 0)

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
    ("single-line flow sequence becomes a list",
     'c: ["a#R-0001", "a#R-0002"]\nd: 1\n',
     {"c": ["a#R-0001", "a#R-0002"], "d": "1"}),
    ("wrapped flow sequence keeps its continuation, and the next key survives",
     'c: ["a#R-0001", "a#R-0002",\n     "a#R-0003"]\nd: 1\n',
     {"c": ["a#R-0001", "a#R-0002", "a#R-0003"], "d": "1"}),
    ("a flow sequence wrapped over three lines",
     'c: ["x",\n    "y",\n    "z"]\nd: 1\n',
     {"c": ["x", "y", "z"], "d": "1"}),
    ("wrapped flow sequence inside a sequence-of-maps",
     'f:\n  - n: 1\n    ids: ["a",\n           "b"]\n    keep: yes\n',
     {"f": [{"n": "1", "ids": ["a", "b"], "keep": "yes"}]}),
    ("a comma inside a quoted element does not split it",
     'c: ["a, b", "c"]\n', {"c": ["a, b", "c"]}),
    # Inline flow MAPS. 4331 lines in the library are written this way,
    # including two records at profile: full, and this parser used to store the
    # whole brace expression as a single string KEY while bin/_record_yaml.py
    # returned a map. One lane measured 358 keys present under one reader and
    # absent under the other in a single file — and the key COUNTS matched,
    # which is what hid it (library#39).
    ("a flow map becomes a dict",
     'c: {a: 1, b: 2}\nd: 3\n', {"c": {"a": "1", "b": "2"}, "d": "3"}),
    ("a wrapped flow map becomes a dict too",
     'c: {a: 1,\n    b: 2}\nd: 3\n', {"c": {"a": "1", "b": "2"}, "d": "3"}),
    ("a flow map as a bare sequence item",
     'v:\n  - {id: 1, why: "a, b"}\n  - {id: 2, why: x}\n',
     {"v": [{"id": "1", "why": "a, b"}, {"id": "2", "why": "x"}]}),
    ("a flow map wrapped as a sequence item",
     'v:\n  - {id: 1,\n     why: x}\n', {"v": [{"id": "1", "why": "x"}]}),
    ("a brace expression that is not a map stays text",
     'c: {not a map}\n', {"c": "{not a map}"}),
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
    # Double-quoted escapes. This case used to expect the backslashes back,
    # which pinned the bug rather than the behaviour: the scalar must not
    # terminate early AND the escape must resolve, as bin/_record_yaml.py has
    # always resolved it. 435 values across 46 records read differently under
    # the two readers because this one resolved nothing, 72 of them verbatim
    # requirement texts (library#39, the sixth defect in this family).
    ("an escaped quote does not terminate the scalar early, and resolves",
     'k: "she said \\"hi\\" twice"\nb: 1\n',
     {"k": 'she said "hi" twice', "b": "1"}),
    # The ordering bug, which is why this is one left-to-right pass and not a
    # chain of str.replace(): a doubled backslash followed by `n` is an escaped
    # backslash and then the letter `n`, NOT a newline. Chained replaces
    # rescanned their own output and produced a real newline here.
    ("a doubled backslash before n stays a backslash and an n",
     'k: "joined by \\\\n, no trailing newline"\n',
     {"k": "joined by \\n, no trailing newline"}),
    ("a doubled backslash before t stays a backslash and a t",
     "k: \"the char '\\\\t' (tab)\"\n", {"k": "the char '\\t' (tab)"}),
    ("a lone escaped newline and tab do resolve",
     'k: "one\\ntwo\\tthree"\n', {"k": "one\ntwo\tthree"}),
    # Escapes NOT in the table are left exactly as written, because the records
    # that use them are about escape notation itself: the CBOR/EDN test vectors
    # carry brace-form literals (107 sites) and rfc-9804 prose names hex
    # escapes as notation. Resolving these would rewrite the subject matter.
    ("a brace-form EDN literal is left alone",
     'k: "D\\u{6f}mino"\n', {"k": "D\\u{6f}mino"}),
    ("a hex escape is left alone",
     'k: "\\xFE is the same octet"\n', {"k": "\\xFE is the same octet"}),
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
    # A block sequence at the SAME indent as its key is valid YAML, and BOTH
    # of the library's readers used to lose it entirely — `requirements:` came
    # back as an empty dict. 13 files are written that way, three of them
    # requirements.yaml whose whole list was invisible to every tool in bin/,
    # which is why 16 citations looked dangling that were not (library#39).
    ("a column-zero sequence belongs to its key",
     "a:\n- 1\n- 2\nb: 3\n", {"a": ["1", "2"], "b": "3"}),
    ("a column-zero sequence of maps, then a sibling key",
     "r:\n- id: x\n  k: 1\n- id: y\n  k: 2\nz: 9\n",
     {"r": [{"id": "x", "k": "1"}, {"id": "y", "k": "2"}], "z": "9"}),
    ("a nested sequence at its own key's indent",
     "a:\n- id: x\n  sub:\n  - 1\n  - 2\nb: 3\n",
     {"a": [{"id": "x", "sub": ["1", "2"]}], "b": "3"}),
    ("an indented sequence still works",
     "a:\n  - 1\n  - 2\nb: 3\n", {"a": ["1", "2"], "b": "3"}),
    # The guard: a MAP at the key's own indent is the next sibling key, not the
    # key's value, so an empty key must stay empty rather than swallowing it.
    ("a key with no value does not swallow its sibling",
     "a:\nb: 3\n", {"a": {}, "b": "3"}),
]

fail = 0
for name, src, want in CASES:
    got = parse(src)
    if got != want:
        fail += 1
        print(f"FAIL {name}\n  want {want!r}\n  got  {got!r}")
print(f"test_yaml: {len(CASES) - fail}/{len(CASES)} passed")
sys.exit(1 if fail else 0)

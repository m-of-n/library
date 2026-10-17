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
]
for src in AGREE:
    a = {k: str(v) for k, v in parse(src).items()}
    b = {k: str(v) for k, v in miniyaml(src).items()}
    if a != b:
        fail += 1
        print(f"FAIL parsers disagree on {src!r}\n  _record_yaml {a!r}\n  _yaml        {b!r}")

total = len(CASES) + len(AGREE)
print(f"test_record_yaml: {total - fail}/{total} passed")
sys.exit(1 if fail else 0)

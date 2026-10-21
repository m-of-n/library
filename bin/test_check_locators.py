#!/usr/bin/env python3
"""Regression tests for bin/check-locators.

The tool reports 0 misfiled locators across the whole library, which is only
reassuring if it can fail. These cases make it fail on purpose.

The first version of the tool reported 44 misfilings, 36 of them in rfc-9053
alone, and every one was its own bug: it located a text with `str.find`, which
returns the EARLIEST occurrence, so a short normative sentence appearing both
in a table and in prose was always judged against the wrong one. Case
"repeated text, one occurrence inside" pins the fix — the locator is a true
claim if ANY occurrence falls in its section.

Dependency-free, like bin/test_yaml.py — no pytest, no fixtures library.
"""
import importlib.machinery
import importlib.util
import pathlib
import sys
import tempfile

BIN = pathlib.Path(__file__).resolve().parent

SRC = """\
Some Working Group                                            A. Author
Internet-Draft                                              January 2026


                        A Test Document For Locators


Abstract

   This paragraph sits in the front matter and belongs to no section.

1.  Introduction

   The introduction says something unremarkable about the format.

1.1.  Terminology

   A term is defined here and nowhere else.

2.  The Mechanism

   The mechanism paragraph MUST do the thing.

2.1.  A Subsection

   The repeated sentence appears here.

3.  Security Considerations

   The repeated sentence appears here.
"""

RECORD = """schema: "library-record/v1"
id: test-locators
body: ietf
type: rfc
title: "A Test Document For Locators"
content:
  url: https://example.invalid/test-locators.txt
tags:
  - test
status: distilled
"""


def load_tool():
    """bin/check-locators has no .py suffix, so import it by path.

    spec_from_file_location infers its loader from the extension, so an
    extensionless script yields a spec with no loader unless one is passed.
    """
    path = BIN / "check-locators"
    loader = importlib.machinery.SourceFileLoader("_check_locators", str(path))
    spec = importlib.util.spec_from_file_location("_check_locators", path,
                                                  loader=loader)
    mod = importlib.util.module_from_spec(spec)
    loader.exec_module(mod)
    return mod


def reqs_yaml(entries):
    out = ["requirements:"]
    for rid, loc, text in entries:
        out.append(f'  - id: "test-locators#{rid}"')
        out.append(f'    locator: "{loc}"')
        out.append(f'    text: "{text}"')
    return "\n".join(out) + "\n"


# (name, [(id, locator, text)], expected failures, expected unresolved)
CASES = [
    (
        "a text inside its own section passes",
        [("R-0001", "§1", "The introduction says something unremarkable")],
        0, 0,
    ),
    (
        "a text in the wrong section is MISFILED",
        [("R-0001", "§3", "The introduction says something unremarkable")],
        1, 0,
    ),
    (
        "front matter filed under a section is MISFILED",
        [("R-0001", "§1", "This paragraph sits in the front matter")],
        1, 0,
    ),
    (
        # §2 contains §2.1, so a subsection text filed under the parent is fine.
        "a parent section contains its subsections",
        [("R-0001", "§2", "The repeated sentence appears here")],
        0, 0,
    ),
    (
        # ...but not the reverse: §2.1's span stops before §3.
        "a subsection does not contain its parent's other children",
        [("R-0001", "§1.1", "The mechanism paragraph MUST do the thing")],
        1, 0,
    ),
    (
        # The bug that produced 44 false misfilings. The sentence is in both
        # §2.1 and §3; filed under §3 it must pass on the SECOND occurrence.
        "repeated text, one occurrence inside",
        [("R-0001", "§3", "The repeated sentence appears here")],
        0, 0,
    ),
    (
        "repeated text with no occurrence inside is still MISFILED",
        [("R-0001", "§1.1", "The repeated sentence appears here")],
        1, 0,
    ),
    (
        "a text that is not in the source at all is unresolvable, not misfiled",
        [("R-0001", "§1", "This sentence was never in the document")],
        0, 1,
    ),
    (
        "a locator naming no section is unresolvable, not misfiled",
        [("R-0001", "Table 1, row 3", "The introduction says something")],
        0, 1,
    ),
    (
        "a locator naming a section the source lacks is unresolvable",
        [("R-0001", "§9.4", "The introduction says something unremarkable")],
        0, 1,
    ),
    (
        "line-wrapped source text still matches after whitespace collapse",
        [("R-0001", "§1", "introduction says something unremarkable about the "
                          "format")],
        0, 0,
    ),
    (
        "several entries are counted independently",
        [("R-0001", "§1", "The introduction says something unremarkable"),
         ("R-0002", "§3", "The mechanism paragraph MUST do the thing"),
         ("R-0003", "§2", "The mechanism paragraph MUST do the thing")],
        1, 0,
    ),
]


def main():
    mod = load_tool()
    passed = failed = 0
    for name, entries, want_fail, want_unres in CASES:
        with tempfile.TemporaryDirectory() as td:
            root = pathlib.Path(td)
            (root / ".cache").mkdir()
            (root / ".cache" / "test-locators.txt").write_text(SRC)
            recdir = root / "records" / "ietf" / "test-locators"
            (recdir / "distilled").mkdir(parents=True)
            (recdir / "record.yaml").write_text(RECORD)
            (recdir / "distilled" / "requirements.yaml").write_text(
                reqs_yaml(entries))
            # The tool resolves .cache/ from its own ROOT; point it at ours.
            saved = mod.CACHE
            mod.CACHE = root / ".cache"
            try:
                checked, failures, unresolved, notes = mod.check_record(recdir)
            finally:
                mod.CACHE = saved
        bad = []
        if len(failures) != want_fail:
            bad.append(f"{len(failures)} misfiled, wanted {want_fail}")
        if len(unresolved) != want_unres:
            bad.append(f"{len(unresolved)} unresolvable, wanted {want_unres}")
        if notes:
            bad.append(f"unexpected notes: {notes}")
        if bad:
            failed += 1
            print(f"FAIL  {name}\n      {'; '.join(bad)}")
            for f in failures:
                print(f"      misfiled: {f}")
            for u in unresolved:
                print(f"      unresolvable: {u}")
        else:
            passed += 1
    print(f"test_check_locators: {passed}/{passed + failed} passed")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())

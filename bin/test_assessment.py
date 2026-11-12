#!/usr/bin/env python3
"""Regression tests for library#92: bin/validate's check_assessment and
bin/reassess's flag().

check_assessment is what stops a written record coming back without
`applicability` or a reasoned `usefulness` (11 and 27 records sat like that
under a green check before #92). flag() is the docs/scope.md §7.2 trigger.

Dependency-free, like bin/test_yaml.py — no pytest, no fixtures library.
"""
import importlib.machinery
import importlib.util
import pathlib
import sys

BIN = pathlib.Path(__file__).resolve().parent


def load(name):
    path = BIN / name
    loader = importlib.machinery.SourceFileLoader(f"_{name}", str(path))
    spec = importlib.util.spec_from_file_location(f"_{name}", path, loader=loader)
    mod = importlib.util.module_from_spec(spec)
    loader.exec_module(mod)
    return mod


validate, reassess = load("validate"), load("reassess")

APP = {"security": "core", "cryptography": "none", "this_project": "adjacent"}
OK = {"verdict": "useful", "reason": "one line", "assessed": "2026-11-09"}

# (name, record dict, expected errors, expected warnings)
CASES = [
    ("rated, reasoned, bears on a decision", {"applicability": APP, "usefulness": OK, "bears_on": ["DEC-002"]}, 0, 0),
    # ruling (b): useful/marginal with an empty bears_on is fine when reasoned
    ("useful, empty bears_on, reasoned", {"applicability": APP, "usefulness": OK, "bears_on": []}, 0, 0),
    ("marginal, empty bears_on, reasoned",
     {"applicability": APP, "usefulness": dict(OK, verdict="marginal"), "bears_on": []}, 0, 0),
    ("useful, empty bears_on, no reason",
     {"applicability": APP, "usefulness": dict(OK, reason=""), "bears_on": []}, 1, 0),
    ("useful with a decision, no reason still fails",
     {"applicability": APP, "usefulness": dict(OK, reason=""), "bears_on": ["DEC-002"]}, 1, 0),
    ("no applicability", {"usefulness": OK, "bears_on": []}, 1, 0),
    ("applicability missing an axis", {"applicability": {"security": "core", "cryptography": "none"},
                                       "usefulness": OK}, 1, 0),
    ("applicability off-enum", {"applicability": dict(APP, this_project="maybe"), "usefulness": OK}, 1, 0),
    ("no usefulness", {"applicability": APP}, 1, 0),
    ("unassessed", {"applicability": APP, "usefulness": {"verdict": "unassessed"}}, 1, 0),
    ("assessed not a date", {"applicability": APP, "usefulness": dict(OK, assessed="Nov 9")}, 1, 0),
    ("flagged for re-assessment warns, never errors",
     {"applicability": APP, "usefulness": dict(OK, reassess="DEC-005 reopened 2026-11-09")}, 0, 1),
]

REC = '''id: x
bears_on:
  - DEC-005
usefulness:
  verdict: useful
  reason: "r"
  assessed: "2026-11-03"
status: summarized
'''


def main():
    fail = 0
    for name, d, ne, nw in CASES:
        errs, warns = [], []
        validate.check_assessment(d, "records/t/x", errs, warns)
        if (len(errs), len(warns)) != (ne, nw):
            fail = 1
            print(f"FAIL {name}: {len(errs)} errors, {len(warns)} warnings; want {ne}, {nw}\n  {errs + warns}")
        else:
            print(f"ok   {name}")

    once = reassess.flag(REC, "DEC-005 reopened 2026-11-09", "DEC-005")
    checks = [
        ("flag lands inside the usefulness block",
         once is not None and '  reassess: "DEC-005 reopened 2026-11-09"\nstatus:' in once),
        ("flag leaves the verdict alone", once is not None and "  verdict: useful\n" in once),
        ("same decision twice is a no-op", reassess.flag(once or "", "DEC-005 reopened 2026-11-10", "DEC-005") is None),
        ("a second decision appends",
         '"DEC-005 reopened 2026-11-09; DEC-002 reopened 2026-11-10"'
         in (reassess.flag(once or "", "DEC-002 reopened 2026-11-10", "DEC-002") or "")),
        ("DEC-00 does not match DEC-005", reassess.flag(once or "", "DEC-00 reopened 2026-11-10", "DEC-00") is not None),
    ]
    for ids, ne, label in [
        (["DEC-002", "R-M-07", "ARCH-0002 P1"], 0, "mofn ids pass bare"),
        (["tmodel:DEC-003", "tmodel:DEC-001a", "tmodel:R-044"], 0, "tmodel ids pass prefixed"),
        (["R-044"], 1, "a bare tmodel R-NNN is an error"),
        (["RPT-0006"], 1, "a report id is not a decision"),
        (["tmodel:R-M-07"], 1, "a mofn-shaped id under the tmodel prefix is an error"),
    ]:
        errs = []
        validate.check_bears_on(ids, "records/t/x", errs)
        checks.append((f"bears_on: {label}", len(errs) == ne))
    errs = []
    validate.check_bears_on(["T-023", "WP-1"], "topics/x.yaml", errs, topic=True)
    checks.append(("a topic may name T-*/WP* work", not errs))
    tm = REC.replace("  - DEC-005\n", '  - "tmodel:DEC-005"\n')
    checks.append(("flag works on a tmodel id",
                   reassess.flag(tm, "tmodel:DEC-005 reopened 2026-11-09", "tmodel:DEC-005") is not None))
    checks.append(("register ids are what reassess accepts",
                   all(reassess.ID.fullmatch(x) for x in ["DEC-005", "R-M-07", "tmodel:DEC-003", "tmodel:R-044"])
                   and not any(reassess.ID.fullmatch(x) for x in ["R-044", "DEC-5", "RPT-0006"])))
    both = reassess.flag(tm, "tmodel:DEC-005 reopened 2026-11-09", "tmodel:DEC-005") or ""
    checks.append(("a tmodel flag does not count as the mofn id's",
                   reassess.flag(both, "DEC-005 reopened 2026-11-10", "DEC-005") is not None))
    for name, good in checks:
        print(f"{'ok  ' if good else 'FAIL'} {name}")
        fail |= not good
    return fail


if __name__ == "__main__":
    sys.exit(main())

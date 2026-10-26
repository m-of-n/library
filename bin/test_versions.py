#!/usr/bin/env python3
"""Regression tests for bin/validate's check_versions.

A `versions/<version>/` entry is metadata only (docs/scope.md §5, schema
v0.8.0): exactly one `record.yaml`, carrying a one-line `delta`. The record
glob walks `records/*/*/` and never descends into `versions/`, so a summary
left there is a scaffold no count sees — library#45 found one, under
draft-mih-scitt-agent-action-capsule/versions/-02. Rejecting the file is what
makes that blind spot harmless.

Dependency-free, like bin/test_yaml.py — no pytest, no fixtures library.
"""
import importlib.machinery
import importlib.util
import pathlib
import sys
import tempfile

BIN = pathlib.Path(__file__).resolve().parent


def load_validate():
    """bin/validate has no .py suffix, so import it by path."""
    path = BIN / "validate"
    loader = importlib.machinery.SourceFileLoader("_validate", str(path))
    spec = importlib.util.spec_from_file_location("_validate", path, loader=loader)
    mod = importlib.util.module_from_spec(spec)
    loader.exec_module(mod)
    return mod


META = 'id: rec-a-02\ndelta: "adds §5.4; renames the capsule media type"\n'

# Each case: (name, {relative path: contents}, expected errors, expected warnings)
CASES = [
    ("no versions/ is silent", {"summary.md": "x\n"}, 0, 0),
    ("metadata with a delta is clean", {"versions/-02/record.yaml": META}, 0, 0),
    ("a blank delta warns, never errors",
     {"versions/-02/record.yaml": 'id: rec-a-02\ndelta: ""\n'}, 0, 1),
    ("a missing delta warns", {"versions/-02/record.yaml": "id: rec-a-02\n"}, 0, 1),
    # The case #45 found: a scaffold summary nothing counted.
    ("a summary.md under a version is an error",
     {"versions/-02/record.yaml": META,
      "versions/-02/summary.md": "_Two to five sentences._\n"}, 1, 0),
    ("distilled/ under a version is an error, per file",
     {"versions/-02/record.yaml": META,
      "versions/-02/distilled/normative.md": "x\n",
      "versions/-02/distilled/requirements.yaml": "x\n"}, 2, 0),
    ("a version with no record.yaml is an error",
     {"versions/-02/notes.txt": "x\n"}, 2, 0),
    ("a loose file directly in versions/ is an error",
     {"versions/README.md": "x\n"}, 1, 0),
    ("each version is checked",
     {"versions/-02/record.yaml": META,
      "versions/-03/record.yaml": "id: rec-a-03\n",
      "versions/-03/summary.md": "x\n"}, 1, 1),
]


def main():
    mod = load_validate()
    passed = failed = 0
    for name, files, want_e, want_w in CASES:
        with tempfile.TemporaryDirectory() as td:
            recdir = pathlib.Path(td)
            for rel, body in files.items():
                p = recdir / rel
                p.parent.mkdir(parents=True, exist_ok=True)
                p.write_text(body)
            errs, warns = [], []
            mod.check_versions(recdir, "records/x/rec-a", errs, warns)
        if (len(errs), len(warns)) == (want_e, want_w):
            passed += 1
        else:
            failed += 1
            print(f"FAIL  {name}\n      got {len(errs)} error(s), {len(warns)} "
                  f"warning(s); wanted {want_e}, {want_w}")
            for m in errs + warns:
                print(f"      {m}")
    print(f"test_versions: {passed}/{passed + failed} passed")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())

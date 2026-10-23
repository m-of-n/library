#!/usr/bin/env python3
"""Regression tests for bin/validate's check_id_collisions.

The check warns where a record cites a FOREIGN requirement id whose bare form
is also one of its own — `rfc-8610#R-0079` cited by a record that defines its
own `R-0079`. Both ids exist, so nothing is dangling and no other check sees
it; what breaks is a bare `R-0079` in prose, which then resolves two ways.
draft-ietf-cbor-cddl-modules' cross-check found it (library#39) after that
record's own README listed two of its four cross-record refs and missed both
of the colliding ones.

Case 4 is the one that matters most: the first version of this check flagged
draft-mcnally-deterministic-cbor's own paragraph *warning about wrapped ids*,
because `…-cbor#V-0001` matches on its tail and reads as a foreign record.
A check that mis-fires on prose about the hazard it polices is worse than no
check, so that false positive is pinned here.

Dependency-free, like bin/test_yaml.py — no pytest, no fixtures library.
"""
import importlib.machinery
import importlib.util
import pathlib
import sys
import tempfile

BIN = pathlib.Path(__file__).resolve().parent


def load_validate():
    """bin/validate has no .py suffix, so import it by path.

    An explicit SourceFileLoader is required: spec_from_file_location infers
    the loader from the extension and returns None without one.
    """
    path = BIN / "validate"
    loader = importlib.machinery.SourceFileLoader("_validate", str(path))
    spec = importlib.util.spec_from_file_location("_validate", path, loader=loader)
    mod = importlib.util.module_from_spec(spec)
    loader.exec_module(mod)
    return mod


# Each case: (name, record id, {relative path: contents}, expected warning count)
CASES = [
    (
        "collision warns",
        "rec-a",
        {"distilled/requirements.yaml": '  - id: "rec-a#R-0079"\n',
         "distilled/README.md": "see rfc-8610#R-0079 for the grammar\n"},
        1,
    ),
    (
        "foreign ref with no local id of that number is silent",
        "rec-a",
        {"distilled/requirements.yaml": '  - id: "rec-a#R-0001"\n',
         "distilled/README.md": "see rfc-8610#R-0079 for the grammar\n"},
        0,
    ),
    (
        "a record citing its own id fully qualified is not foreign",
        "rec-a",
        {"distilled/requirements.yaml": '  - id: "rec-a#R-0079"\n',
         "distilled/README.md": "see rec-a#R-0079 above\n"},
        0,
    ),
    (
        "a line-wrapped own id does not read as a foreign record",
        "draft-mcnally-deterministic-cbor",
        {"distilled/requirements.yaml":
             '  - id: "draft-mcnally-deterministic-cbor#V-0001"\n',
         "distilled/examples/README.md":
             "wraps even mid-token, so an unquoted `…-cbor#V-0001` parses "
             "as `…-cbor`. Keep it quoted.\n"},
        0,
    ),
    (
        # The counterpart to case 4, and the reason the lookbehind is on the
        # ELISION rather than on the hyphen: a hyphenated record name is a
        # perfectly good record name, so `foo-bar#R-0001` read by record `bar`
        # names foo-bar and really is foreign. Only an elided head is not.
        "a hyphenated foreign record name is still foreign",
        "bar",
        {"distilled/requirements.yaml": '  - id: "bar#R-0001"\n',
         "distilled/README.md": "the token foo-bar#R-0001 names another record\n"},
        1,
    ),
    (
        "V, G and N namespaces collide too",
        "rec-a",
        {"distilled/requirements.yaml":
             '  - id: "rec-a#V-0003"\n  - id: "rec-a#G-01"\n  - id: "rec-a#N-02"\n',
         "distilled/README.md":
             "rfc-8610#V-0003, rfc-8610#G-01 and rfc-9741#N-02\n"},
        3,
    ),
    (
        "one warning per colliding id, not per citing file",
        "rec-a",
        {"distilled/requirements.yaml": '  - id: "rec-a#R-0079"\n',
         "distilled/README.md": "rfc-8610#R-0079\n",
         "distilled/design-notes.md": "rfc-8610#R-0079 again\n",
         "summary.md": "and rfc-8610#R-0079 once more\n"},
        1,
    ),
    (
        "generated .html is not scanned",
        "rec-a",
        {"distilled/requirements.yaml": '  - id: "rec-a#R-0079"\n',
         "summary.html": "<p>rfc-8610#R-0079</p>\n"},
        0,
    ),
    (
        "an unquoted definition is still a definition",
        "rec-a",
        {"distilled/requirements.yaml": "  - id: rec-a#R-0079\n",
         "distilled/README.md": "rfc-8610#R-0079\n"},
        1,
    ),
    (
        "two different foreign records colliding on different ids",
        "rec-a",
        {"distilled/requirements.yaml":
             '  - id: "rec-a#R-0079"\n  - id: "rec-a#R-0053"\n',
         "distilled/README.md": "rfc-8610#R-0079 and rfc-9165#R-0053\n"},
        2,
    ),
]


def main():
    mod = load_validate()
    passed = failed = 0
    for name, rid, files, want in CASES:
        with tempfile.TemporaryDirectory() as td:
            recdir = pathlib.Path(td)
            for rel, body in files.items():
                p = recdir / rel
                p.parent.mkdir(parents=True, exist_ok=True)
                p.write_text(body)
            warns = []
            mod.check_id_collisions(recdir, rid, f"records/x/{rid}", warns)
        if len(warns) == want:
            passed += 1
        else:
            failed += 1
            print(f"FAIL  {name}\n      got {len(warns)} warning(s), wanted {want}")
            for w in warns:
                print(f"      {w}")
    print(f"test_id_collisions: {passed}/{passed + failed} passed")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())

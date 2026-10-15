#!/usr/bin/env python3
"""Regression tests for bin/check-pr-extraction — the FX-1 gate.

The gate decides whether a PR is EXTRACTING a record (and so owes the full
artifact set) or merely touching one. It has been wrong in both directions:
it failed a one-file rename on a missing protocol model (library#44), and it
read `status: distilled` as a claim about a standard that postdated the record
(library#73). Both were found by a human hitting them in a real PR. This pins
the behaviour instead.

Each case builds a throwaway git repo holding only the two files the script
needs, commits a base state, applies a change, and runs the real script
against the real base ref. Dependency-free, like bin/test_yaml.py — no pytest,
no fixtures library.
"""
import pathlib
import shutil
import subprocess
import sys
import tempfile

BIN = pathlib.Path(__file__).resolve().parent

RECORD = """schema: "library-record/v1"
id: {rid}
body: ietf
type: rfc
title: "Test record"
content:
  url: https://example.invalid/{rid}
tags:
  - test
status: distilled
distillation:
{block}"""


def git(cwd, *args):
    return subprocess.run(["git", *args], cwd=cwd, capture_output=True,
                          text=True, check=True).stdout


def build(tmp, base_block, head_block, base_files=(), head_files=()):
    """A repo with one record, committed twice. Returns (repo, base_sha)."""
    repo = pathlib.Path(tmp)
    (repo / "bin").mkdir()
    for f in ("check-pr-extraction", "_yaml.py"):
        shutil.copy(BIN / f, repo / "bin" / f)
    rec = repo / "records" / "ietf" / "rfc-9999"
    rec.mkdir(parents=True)

    def write(block, files, stamp):
        (rec / "record.yaml").write_text(RECORD.format(rid="rfc-9999", block=block))
        # Every case must actually touch the record, or the gate has nothing to
        # judge. summary.md carries the change that is not the one under test.
        (rec / "summary.md").write_text(f"---\nid: rfc-9999\n---\n{stamp}\n")
        for name, body in files:
            p = rec / name
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(body)

    git(repo, "init", "-q", "-b", "main")
    git(repo, "config", "user.email", "t@example.invalid")
    git(repo, "config", "user.name", "t")
    write(base_block, base_files, "base")
    git(repo, "add", "-A")
    git(repo, "commit", "-qm", "base")
    base = git(repo, "rev-parse", "HEAD").strip()
    write(head_block, head_files, "head")
    git(repo, "add", "-A")
    git(repo, "commit", "-qm", "head")
    return repo, base


def run(repo, base):
    r = subprocess.run([sys.executable, "bin/check-pr-extraction", base],
                       cwd=repo, capture_output=True, text=True)
    return r.returncode, r.stdout + r.stderr


FULL = '  standard: "FX-1"\n  profile: full\n'
OLD_FULL = '  standard: "distillation/0.1.0"\n  profile: full\n'
OLD_PARTIAL_WHY = ('  standard: "distillation/0.1.0"\n  profile: partial\n'
                   '  profile_reason: "reviewed_by empty on every artifact"\n')
OLD_PARTIAL_BARE = '  standard: "distillation/0.1.0"\n  profile: partial\n'
FULL_PARTIAL_WHY = ('  standard: "FX-1"\n  profile: partial\n'
                    '  profile_reason: "source is paywalled"\n')
ART = [("distilled/normative.md", "---\nx: 1\n---\n# n\n")]
ART2 = [("distilled/normative.md", "---\nx: 1\n---\n# n\n"),
        ("distilled/messages.yaml", "messages: []\n")]
ART_EDITED = [("distilled/normative.md", "---\nx: 1\n---\n# n, revised\n")]

CASES = [
    # (name, base_block, head_block, base_files, head_files, want_ok, want_text)
    ("grandfathered record untouched by distilled/ changes",
     OLD_FULL, OLD_FULL, ART, ART, True, "grandfathered"),

    # library#9: the correction the ratchet used to block.
    ("grandfathered full -> partial, artifacts untouched, reason given",
     OLD_FULL, OLD_PARTIAL_WHY, ART, ART, True, ""),
    ("full -> partial with no reason",
     OLD_FULL, OLD_PARTIAL_BARE, ART, ART, False, "no `profile_reason`"),
    ("full -> partial while editing distilled/",
     OLD_FULL, OLD_PARTIAL_WHY, ART, ART_EDITED, False, "while changing distilled/"),
    ("full -> partial while adding to distilled/",
     OLD_FULL, OLD_PARTIAL_WHY, ART, ART2, False, "while changing distilled/"),
    ("FX-1 full -> partial, artifacts untouched, reason given",
     FULL, FULL_PARTIAL_WHY, ART, ART, True, ""),

    # The rest of the ratchet must keep holding.
    ("dropping the distillation block",
     FULL, "  # none\n", ART, ART, False, "now has none"),
    ("falling back from the standard in force",
     FULL, OLD_FULL, ART, ART, False, "does not fall back"),
    ("adding to a grandfathered distilled/",
     OLD_FULL, OLD_FULL, ART, ART2, False, "brings it to FX-1"),
    ("adding to an FX-1 record that is already full",
     FULL, FULL, ART, ART2, True, ""),
]


def main():
    passed = failed = 0
    for name, bb, hb, bf, hf, want_ok, want_text in CASES:
        with tempfile.TemporaryDirectory() as tmp:
            repo, base = build(tmp, bb, hb, bf, hf)
            code, out = run(repo, base)
        ok = code == 0
        bad = []
        if ok != want_ok:
            bad.append(f"exit {code}, wanted {'0' if want_ok else 'non-zero'}")
        if want_text and want_text not in out:
            bad.append(f"output missing {want_text!r}")
        if bad:
            failed += 1
            print(f"FAIL  {name}\n      {'; '.join(bad)}")
            print("      " + out.replace("\n", "\n      ").rstrip())
        else:
            passed += 1
    print(f"test_check_pr_extraction: {passed}/{passed + failed} passed")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())

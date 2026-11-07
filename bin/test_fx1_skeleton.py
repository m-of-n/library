#!/usr/bin/env python3
"""Regression tests for the quote-by-reference toolchain (library#86):
bin/_source_text, bin/fx1-skeleton, bin/check-quotes, and the validate rules
that go with them (tiered passes, skeleton requirements, candidate verdicts).

Each case is something that went wrong in the prototype run on RFC 9202 and
RFC 9679: a sentence crossing a page break, an aside bar, a hyphen broken
across lines, a check that cannot fail. Dependency-free, like the others.
"""
import importlib.machinery
import importlib.util
import pathlib
import subprocess
import sys
import tempfile

BIN = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(BIN))
import _source_text as st  # noqa: E402

SRC = """\
Internet Engineering Task Force (IETF)                         A. Author
Request for Comments: 9999                                  January 2026


                        A Test Document For Skeletons

1.  Introduction

   The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT",
   "SHOULD", "SHOULD NOT", "RECOMMENDED", "NOT RECOMMENDED", "MAY", and
   "OPTIONAL" in this document are to be interpreted as described in
   BCP 14 [RFC2119] [RFC8174] when, and only when, they appear in all
   capitals, as shown here.

2.  The Mechanism

   A sender MUST encode the value as a well-
   formed byte string.  The receiver needs to reject anything else.
   This sentence is long and crosses a page boundary, and the receiver



Author                       Standards Track                    [Page 1]
\f
RFC 9999                 Test Document For Skeletons            January 2026


   MAY log it.

   |  A quoted definition is printed behind an aside bar and it SHOULD
   |  be read without the bar.

   1.  First, compute the digest.

3.  References

   [RFC2119]  Bradner, S., "Key words for use in RFCs", March 1997.
   Implementations may cite this.
"""


def run(*args):
    return subprocess.run([sys.executable, "-I", *map(str, args)],
                          capture_output=True, text=True)


def load_validate():
    loader = importlib.machinery.SourceFileLoader("validate", str(BIN / "validate"))
    spec = importlib.util.spec_from_loader("validate", loader)
    mod = importlib.util.module_from_spec(spec)
    loader.exec_module(mod)
    return mod


def check(name, cond, detail=""):
    print(("ok    " if cond else "FAIL  ") + name + ("" if cond else f"\n      {detail}"))
    return bool(cond)


def main():
    results = []
    src = SRC.split("\n")
    cleaned = st.clean(src)
    # 1. reading rules
    prose = st.span(cleaned, 17, 30)
    results.append(check("hyphen break rejoins with no space", "well-formed" in prose, prose))
    results.append(check("page break does not split the sentence",
                         "the receiver MAY log it." in prose, prose))
    results.append(check("footer and header are not prose", "[Page 1]" not in prose
                         and "January 2026" not in prose, prose))
    aside = st.span(cleaned, 30, 31)
    results.append(check("aside bar is margin", aside.startswith("A quoted") and "|" not in aside, aside))
    results.append(check("hyphen=False keeps the old space reading",
                         "well- formed" in st.span(cleaned, 17, 18, hyphen=False)))
    results.append(check("HTML is refused", not st.looks_like_text(["<!DOCTYPE html>", "<html>"])))

    with tempfile.TemporaryDirectory() as td:
        td = pathlib.Path(td)
        txt = td / "rfc-9999.txt"
        txt.write_text(SRC)
        rec = td / "rfc-9999"
        rec.mkdir()
        (rec / "record.yaml").write_text("id: rfc-9999\ntitle: Test\n")
        r = run(BIN / "fx1-skeleton", rec, "--txt", txt, "--xml", td / "none.xml")
        results.append(check("skeleton runs", r.returncode == 0, r.stderr))
        req = (rec / "distilled/requirements.yaml").read_text()
        cand = (rec / "distilled/inferred-candidates.yaml").read_text()
        results.append(check("3 keyword sentences, boilerplate excluded",
                             req.count("  - id:") == 3, req))
        results.append(check("keyword counts reconcile",
                             "source_keyword_count: 3" in req and "extracted_keyword_count: 3" in req, req))
        results.append(check("single-keyword sentence gets its verb", "verb: 'MUST'" in req, req))
        results.append(check("'needs to' is a candidate", "needs to reject" in cand, cand))
        results.append(check("procedure step is a candidate", "compute the digest" in cand, cand))
        results.append(check("References section yields no candidates",
                             "Implementations may cite" not in cand, cand))
        r = run(BIN / "check-quotes", rec, "--txt", txt)
        results.append(check("generated quotations all verify", r.returncode == 0
                             and "0 mismatched" in r.stdout and "examined 0" not in r.stdout, r.stdout))
        # a check that cannot fail checks nothing: break one quotation
        (rec / "distilled/requirements.yaml").write_text(
            req.replace("A sender MUST encode", "A sender MUST always encode"))
        r = run(BIN / "check-quotes", rec, "--txt", txt)
        results.append(check("a retyped quotation fails", r.returncode == 1, r.stdout))
        (rec / "distilled/requirements.yaml").write_text(req.replace("source_lines: '17-18'", "source_lines: '16-18'"))
        r = run(BIN / "check-quotes", rec, "--txt", txt)
        results.append(check("a range wider than its text fails", r.returncode == 1 and "tighten" in r.stdout, r.stdout))
        # markdown render
        md = rec / "distilled/design-notes.md"
        md.write_text('<!-- q L30-31 "A quoted" .. "aside bar" -->\n> typed by hand\n')
        r = run(BIN / "check-quotes", rec, "--txt", txt, "--only", md)
        results.append(check("a hand-typed md quote fails", r.returncode == 1, r.stdout))
        run(BIN / "check-quotes", rec, "--txt", txt, "--render", "--only", md)
        results.append(check("--render writes the words",
                             "> A quoted definition is printed behind an aside bar" in md.read_text(), md.read_text()))

    v = load_validate()
    def errs_of(fn, *a):
        e = []
        fn(*a, "w", e)
        return e
    ok_tiered = {"pass": "extract", "effort": "tiered", "agents": [
        {"role": "schema", "model": "sonnet", "effort": "medium", "tokens": 80000},
        {"role": "design-notes", "model": "opus", "effort": "max"}]}
    results.append(check("tiered extract with judgement at max passes", not errs_of(v.check_pass, ok_tiered)))
    bad = {"pass": "extract", "effort": "tiered", "agents": [
        {"role": "requirements", "model": "sonnet", "effort": "medium"}]}
    results.append(check("judgement role below max fails", errs_of(v.check_pass, bad)))
    results.append(check("tiered verify fails", errs_of(v.check_pass, {"pass": "verify", "effort": "tiered",
                                                                     "agents": ok_tiered["agents"]})))
    results.append(check("tiered with no agents fails", errs_of(v.check_pass, {"pass": "extract", "effort": "tiered"})))
    results.append(check("plain max still passes", not errs_of(v.check_pass, {"pass": "verify", "effort": "max"})))
    with tempfile.TemporaryDirectory() as td:
        recdir = pathlib.Path(td)
        (recdir / "distilled").mkdir()
        (recdir / "distilled/inferred-candidates.yaml").write_text(
            "candidates:\n  - id: 'C-0001'\n    verdict: stated\n    reason: ''\n"
            "  - id: 'C-0002'\n    verdict: reject\n    reason: ''\n"
            "  - id: 'C-0003'\n    verdict: TODO\n")
        entries = [{"id": "R-1", "kind": "stated", "verb": "MUST", "text": "x MUST y", "source_lines": "3"},
                   {"id": "R-2", "kind": "stated", "verb": "none", "text": "z", "source_lines": "4",
                    "candidate": "C-0001"},
                   {"id": "R-3", "kind": "inferred", "verb": "implied MUST", "text": "q"},
                   {"id": "R-4", "kind": "stated", "verb": "MAY", "text": "no keyword here", "source_lines": "5"},
                   {"id": "R-5", "kind": "stated", "verb": "none", "text": "w", "candidate": "C-0009"}]
        e = errs_of(v.check_skeleton_requirements, recdir, entries)
        joined = "\n".join(e)
        results.append(check("free-text verb fails", "R-3 verb" in joined, joined))
        results.append(check("verb missing from text fails", "R-4 verb MAY" in joined, joined))
        results.append(check("stated with no source_lines fails", "R-5 is stated but has no source_lines" in joined, joined))
        results.append(check("reject with no reason fails", "C-0002 rejected" in joined, joined))
        results.append(check("TODO verdict fails", "C-0003 verdict" in joined, joined))
        results.append(check("dangling candidate fails", "C-0009" in joined, joined))
        results.append(check("linked stated candidate passes", "C-0001" not in joined, joined))
        results.append(check("good entry passes", "R-1" not in joined and "R-2" not in joined, joined))

    n = len(results)
    print(f"test_fx1_skeleton: {sum(results)}/{n} passed")
    return 0 if all(results) else 1


if __name__ == "__main__":
    sys.exit(main())

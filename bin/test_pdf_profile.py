#!/usr/bin/env python3
"""Regression tests for the PDF profile of the FX-1 toolchain (library#69):
bin/_source_text's pdftotext reading, bin/_bcp14's `directives` vocabulary,
and how bin/fx1-skeleton, bin/check-quotes, bin/check-locators and
bin/validate use them.

The fixture copies the shape of a real `pdftotext -layout` rendering of an
ETSI deliverable: running header and footer on every page, a table of
contents with dot leaders, unnumbered drafting-rules clauses, two headings
on consecutive lines, a title wrapped onto an indented line, NOTE blocks, and
lowercase verbal forms. Dependency-free, like the others.
"""
import importlib.machinery
import importlib.util
import pathlib
import subprocess
import sys
import tempfile

BIN = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(BIN))
import _bcp14  # noqa: E402
import _source_text as st  # noqa: E402


def page(n, body):
    return (f"{' ' * 40}{n}{' ' * 20}ETSI EN 999 999 V1.1.1 (2026-01)\n\n\n"
            + body + f"\n\n\n{' ' * 44}ETSI\n")


PAGES = [
    "Contents\n\nForeword.................................................... 2\n"
    "1        Scope ..................................................... 3\n"
    "5        Provisions ................................................ 3\n"
    "5.1           Secure Design ........................................ 3\n"
    "5.1.1           Principle 1: Do a thing\n"
    "                and more ........................................... 4\n"
    "Annex A (informative): Background ................................. 5\n",
    "Foreword\nThis document can be downloaded from the ETSI web site.\n\n"
    "Modal verbs terminology\n"
    'In the present document "shall", "shall not", "should", "should not", "may", "need not", "will", "will not", "can" and\n'
    '"cannot" are to be interpreted as described in clause 3.2 of the ETSI Drafting Rules (Verbal forms for the expression of\n'
    "provisions).\n\n"
    '"must" and "must not" are NOT allowed in ETSI deliverables except when used in direct citation.',
    "1             Scope\nThe present document was approved in May 2026 and defines things.\n\n\n"
    "5             Provisions\n\n5.1           Secure Design\n"
    "5.1.1         Principle 1: Design the system for security as well as\n"
    "              functionality\n"
    "Provision 5.1.1-1 Developers shall document the model and this\n"
    "documentation shall be kept",
    "up to date.\n\n"
    "Provision 5.1.1-2 System Operators should monitor the system.\n\n"
    "    NOTE:      An operator can use any tool for this.\n\n"
    "Provision 5.1.1-3 Shall we continue? Data Custodians may delete the data.",
    "Annex A (informative):\nBackground\n\nA reader can find more here.\n\n"
    "7.    Barker EB (2018) Recommendation for Key-Derivation Methods\n"
    "      in Key-Establishment Schemes.\n\n"
    "10. Approved Security Functions. Modules shall use them.",
]
SRC = "\f".join(page(i + 1, b) for i, b in enumerate(PAGES))


def run(*args):
    return subprocess.run([sys.executable, "-I", *map(str, args)],
                          capture_output=True, text=True)


def load(name):
    loader = importlib.machinery.SourceFileLoader(name.replace("-", "_"), str(BIN / name))
    spec = importlib.util.spec_from_loader(loader.name, loader)
    mod = importlib.util.module_from_spec(spec)
    loader.exec_module(mod)
    return mod


def check(name, cond, detail=""):
    print(("ok    " if cond else "FAIL  ") + name + ("" if cond else f"\n      {detail}"))
    return bool(cond)


def line_of(src, needle):
    return next(i for i, l in enumerate(src, 1) if needle in l)


def main():
    results = []
    src = SRC.split("\n")

    # 1. page furniture, found by recurrence
    furn, pages = st.furniture_lines(src)
    results.append(check("five pages", len(pages) == 5, len(pages)))
    results.append(check("header and footer found on every page", len(furn) == 10,
                         sorted(furn)))
    cleaned = st.clean_pdf(src)
    a, b = line_of(src, "Provision 5.1.1-1"), line_of(src, "up to date.")
    prose = st.span(cleaned, a, b)
    results.append(check("a sentence crossing a page is one sentence",
                         "this documentation shall be kept up to date." in prose, prose))
    results.append(check("furniture is not prose", "ETSI EN" not in prose and "ETSI up" not in prose, prose))
    results.append(check("RFC profile unchanged by default", st.clean_for(src) == st.clean(src)))

    # 2. headings
    heads = st.pdf_headings(src)
    keys = sorted(set(heads.values()))
    for k in ("Contents", "Foreword", "Modal verbs terminology", "§1", "§5", "§5.1", "§5.1.1", "Annex A"):
        results.append(check(f"heading {k}", k in keys, keys))
    results.append(check("TOC entries are not headings",
                         line_of(src, "Scope .....") not in heads, heads))
    wrapped = line_of(src, "              functionality")
    results.append(check("wrapped title continuation is the heading", heads.get(wrapped) == "§5.1.1", heads))
    results.append(check("'Provision ...' is not a heading", line_of(src, "Provision 5.1.1-2") not in heads))
    results.append(check("a reference item the TOC does not list is not a heading",
                         line_of(src, "7.    Barker") not in heads, heads))
    results.append(check("a FIPS run-in paragraph is keyed ¶N",
                         heads.get(line_of(src, "10. Approved")) == "¶10", heads))
    results.append(check("a wrapped TOC title still lists its clause", "§5.1.1" in st.toc_keys(src)))

    # 2b. library#69 NIST/FIPS defects
    fips = ("i\n\n1. Name. A thing.\n\n\nii\n\f2. Category. Text that\nruns on.\n\n\niii\n"
            "\fBODY TITLE OF STANDARD\n\n1   Scope\nThe module shall work.\n\n1 Examples may be ports.\n\n1\n"
            "\fBODY TITLE OF STANDARD\n\nMore text.\n\n2\n\fBODY TITLE OF STANDARD\n\nEnd.\n\n3\n")
    fs = fips.split("\n")
    fc = st.clean_pdf(fs)
    kept = [l for _, l in fc if l]
    results.append(check("a line starting with a form feed is kept", "2. Category. Text that" in kept, kept))
    results.append(check("lone page numbers are furniture", not any(l.strip() in ("i", "ii", "iii", "1", "2", "3") for l in kept), kept))
    results.append(check("a running title on three pages is furniture", "BODY TITLE OF STANDARD" not in kept, kept))
    toc = ("Contents\n\n1        Scope .................... 1\n\n\f" + "\n".join(fs[fs.index("\fBODY TITLE OF STANDARD"):]))
    th = st.pdf_headings(toc.split("\n"))
    tl = toc.split("\n")
    results.append(check("a numbered footnote is not its TOC namesake",
                         th.get(line_of(tl, "1 Examples may")) is None and "§1" in th.values(), th))

    # 3. vocabulary
    results.append(check("'May 20, 2022' is a month", not _bcp14.regex("directives").findall("withdrawn May 20, 2022 and")))
    rx = _bcp14.regex("directives")
    results.append(check("'May 2026' is a month", not rx.findall("approved in May 2026 and")))
    results.append(check("sentence-initial capital counts", rx.findall("Shall we go") == ["Shall"]))
    results.append(check("'shall not' counts once", rx.findall("x shall not y") == ["shall not"]))
    results.append(check("uppercase BCP 14 is not a directive", not rx.findall("x SHALL y")))
    bp = _bcp14.strip_boilerplate_v(SRC, "directives")
    results.append(check("modal-verbs boilerplate is excluded", '"cannot" are to be' not in bp
                         and "NOT allowed" not in bp))
    results.append(check("bcp14 count unchanged", _bcp14.count_v("A MUST b may", "bcp14") == 1))

    with tempfile.TemporaryDirectory() as td:
        td = pathlib.Path(td)
        txt = td / "etsi-x.txt"
        txt.write_bytes(SRC.encode("utf-8"))
        rec = td / "etsi-x"
        rec.mkdir()
        (rec / "record.yaml").write_text(
            "id: etsi-x\ntitle: Test\ncontent:\n  media_type: application/pdf\n")
        r = run(BIN / "fx1-skeleton", rec, "--txt", txt)
        results.append(check("skeleton runs on a PDF rendering", r.returncode == 0, r.stderr))
        req = (rec / "distilled/requirements.yaml").read_text()
        cand = (rec / "distilled/inferred-candidates.yaml").read_text()
        rep = (rec / "distilled/skeleton-report.txt").read_text()
        results.append(check("vocabulary recorded", "keyword_vocabulary: directives" in req, req))
        results.append(check("verbs are lowercase canonical", "verb: 'should'" in req
                             and "verb: 'shall'" in req, req))
        results.append(check("informative text goes to candidates",
                             "operator can use" in cand and "operator can use" not in req
                             and "can be downloaded" in cand and "reader can find" in cand, cand))
        n_src = _bcp14.count_v(SRC, "directives")
        results.append(check("reconciliation computed when arithmetic closes",
                             f"reconciliation: '{n_src} verbal forms in the source" in req,
                             req.split("requirements:")[0]))
        results.append(check("locator is the clause", "locator: '§5.1.1'" in req, req))
        results.append(check("report names the profile", "profile: pdf" in rep, rep))
        r = run(BIN / "check-quotes", rec, "--txt", txt)
        results.append(check("generated quotations verify under the PDF profile",
                             r.returncode == 0 and "0 mismatched" in r.stdout
                             and "examined 0" not in r.stdout, r.stdout))
        (rec / "distilled/requirements.yaml").write_text(
            req.replace("Developers shall document", "Developers shall always document"))
        r = run(BIN / "check-quotes", rec, "--txt", txt)
        results.append(check("a retyped quotation fails", r.returncode == 1, r.stdout))
        # a pinned rendering that is not the cached one is refused
        cache = BIN.parent / ".cache" / "etsi-x.txt"
        if not cache.exists():
            cache.parent.mkdir(exist_ok=True)
            cache.write_text("another rendering\n")
            (rec / "distilled/requirements.yaml").write_text(
                req.replace("keyword_vocabulary:", "source_text_digest: '00'\nkeyword_vocabulary:"))
            r = run(BIN / "check-quotes", rec)
            cache.unlink()
            results.append(check("an unpinned rendering is refused", r.returncode != 0
                                 and "another rendering" in (r.stderr + r.stdout), r.stderr + r.stdout))
        (rec / "distilled/requirements.yaml").write_text(req)
        cl = load("check-locators")
        spans = cl.section_spans(src, "pdf")
        results.append(check("check-locators keys PDF clauses", "5.1.1" in spans
                             and "Annex A" in spans and "Foreword" in spans, spans))
        results.append(check("PDF locator forms resolve", cl.locator_key("Annex A.2", "pdf") == "Annex A.2"
                             and cl.locator_key("Foreword", "pdf") == "Foreword"
                             and cl.locator_key("Foreword") is None))

    v = load("validate")
    e = []
    v.check_skeleton_requirements(pathlib.Path(td), [
        {"id": "R-1", "kind": "stated", "verb": "shall", "text": "Shall x", "source_lines": "3"},
        {"id": "R-2", "kind": "stated", "verb": "MUST", "text": "x shall y", "source_lines": "4"},
        {"id": "R-3", "kind": "stated", "verb": "should", "text": "x shall y", "source_lines": "5"},
    ], "w", e, "directives")
    j = "\n".join(e)
    results.append(check("directive verb found case-insensitively", "R-1" not in j, j))
    results.append(check("a BCP 14 verb fails under directives", "R-2 verb 'MUST'" in j, j))
    results.append(check("verb missing from text fails", "R-3 verb should" in j, j))

    # YAML profile (library#69, OWASP DSOMM)
    ysrc = ("---\nmeta:\n  version: 1\n---\nDim A:\n  Sub B:\n    Act C:\n      uuid: 1234\n"
            "      description: |-\n        The team shall do a thing\n        well.\n"
            "      measure: Run the scanner on every build and review\n        the findings.\n"
            "      tags:\n      - ci\n      implementation:\n      - name: Tool X\n"
            "        description: A tool that may help.\n      - name: Tool Y\n").split("\n")
    yh = st.headings_for(ysrc, "yaml")
    results.append(check("yaml: activity path", "Dim A / Sub B / Act C" in yh.values(), yh))
    results.append(check("yaml: list item under its key", "Dim A / Sub B / Act C / implementation / [1] / description" in yh.values(), yh))
    yc = st.clean_yaml(ysrc)
    prose = st.span(yc, 1, len(ysrc))
    results.append(check("yaml: block and inline prose, keys blanked",
                         "The team shall do a thing well." in prose and "Run the scanner on every build and review the findings." in prose
                         and "measure:" not in prose and "1234" not in prose, prose))
    cl2 = load("check-locators")
    ysp = cl2.section_spans(ysrc, "yaml")
    results.append(check("yaml: spans nest", ysp["Dim A / Sub B"][1] >= ysp["Dim A / Sub B / Act C / measure"][1], ysp))
    results.append(check("yaml: profile from media_type", st.profile_of({"content": {"media_type": "application/yaml"}}) == "yaml"))

    n = len(results)
    print(f"test_pdf_profile: {sum(results)}/{n} passed")
    return 0 if all(results) else 1


if __name__ == "__main__":
    sys.exit(main())

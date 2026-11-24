#!/usr/bin/env python3
"""Regression tests for bin/render-w3c and the heading rule it relies on.

The W3C rendering puts the table of contents at column 0 in heading shape;
bin/_source_text.section_of_line must not file the front matter under §1
(library#89). The rule is "a heading follows a blank line"; respec always
opens its table of contents with Abstract and Status of This Document, so no
numbered entry follows the blank line after its title. A rule that also
required a blank line AFTER the heading was measured and rejected: it drops
wrapped RFC headings (rfc-7515 §4.1.8, rfc-9162 §5.5, rfc-9942 §8.2.2.1).
Dependency-free, like bin/test_yaml.py.
"""
import pathlib, subprocess, sys, tempfile

BIN = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(BIN))
import _source_text as st

HTML = """<html><body><p>Abstract text.</p>
<nav id="toc"><h2>Table of Contents</h2><ol><li><a>Abstract</a></li><li><a>Status of This Document</a></li><li><a><bdi>1. </bdi>Introduction</a></li>
<li><a><bdi>2. </bdi>Data Model</a></li></ol></nav>
<section><h2><bdi>1. </bdi>Introduction</h2><p>Intro MUST text.</p>
<section><h3><bdi>1.1 </bdi>Goals</h3><p>Goal text.</p>
<pre>{
  "a":  1
}</pre></section></section>
<section><h2><bdi>A. </bdi>References</h2><p>Ref.</p></section>
</body></html>
"""

fail = total = 0
def check(name, ok, detail=""):
    global fail, total
    total += 1
    if not ok:
        fail += 1
        print(f"FAIL {name} {detail}")

with tempfile.TemporaryDirectory() as d:
    src, dst = pathlib.Path(d, "x.bin"), pathlib.Path(d, "x.txt")
    src.write_text(HTML)
    subprocess.run([sys.executable, "-I", str(BIN / "render-w3c"), str(src), str(dst)], check=True)
    lines = dst.read_text().split("\n")

check("numbered heading in RFC shape", "1.  Introduction" in lines, repr(lines))
check("dotted subsection heading", "1.1.  Goals" in lines, repr(lines))
check("appendix heading", "Appendix A.  References" in lines, repr(lines))
check("pre keeps its spacing", '  "a":  1' in lines, repr(lines))
sec = dict(zip(lines, st.section_of_line(lines)))
check("toc entry is front matter, not §1", sec.get("1. Introduction") is None, repr(sec))
check("body text filed under its section", sec.get("Intro MUST text.") == "§1", repr(sec))
check("subsection text filed under §1.1", sec.get("Goal text.") == "§1.1", repr(sec))
check("appendix text filed under the appendix", sec.get("Ref.") == "Appendix A", repr(sec))

# --ordinal: a pre-respec page with bare <h2>..<h4> headings (PICS, DSig).
OLD = """<html><body><h1>Title</h1><h3>Status</h3><p>Front.</p>
<h2>Overview</h2><p>Over text.</p>
<h2>Syntax</h2><h3>Labels</h3><p>Label text.</p><h4>Deep</h4><p>Deep text.</p>
<h3>Options</h3><p>Opt text.</p><h2>Appendix A: More</h2><p>App text.</p>
</body></html>
"""
with tempfile.TemporaryDirectory() as d:
    src, dst = pathlib.Path(d, "o.bin"), pathlib.Path(d, "o.txt")
    src.write_text(OLD)
    subprocess.run([sys.executable, "-I", str(BIN / "render-w3c"), "--ordinal", str(src), str(dst)], check=True)
    ol = dst.read_text().split("\n")
    subprocess.run([sys.executable, "-I", str(BIN / "render-w3c"), str(src), str(dst)], check=True)
    plain = dst.read_text().split("\n")
osec = dict(zip(ol, st.section_of_line(ol)))
check("ordinal: h2 numbered", "1.  Overview" in ol, repr(ol))
check("ordinal: h3 under second h2", "2.1.  Labels" in ol, repr(ol))
check("ordinal: h4 nests", "2.1.1.  Deep" in ol, repr(ol))
check("ordinal: h3 counter resets per h2, continues per h3", "2.2.  Options" in ol, repr(ol))
check("ordinal: appendix heading is an ordinal, not a letter", "3.  Appendix A: More" in ol, repr(ol))
check("ordinal: pre-h2 heading unnumbered", "   Status" in ol, repr(ol))
check("ordinal: front matter unfiled", osec.get("Front.") is None, repr(osec))
check("ordinal: deep text filed", osec.get("Deep text.") == "§2.1.1", repr(osec))
check("without --ordinal nothing is numbered", "   Overview" in plain and "1.  Overview" not in plain, repr(plain))

print(f"test_render_w3c: {total - fail}/{total} passed")
sys.exit(1 if fail else 0)

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

print(f"test_render_w3c: {total - fail}/{total} passed")
sys.exit(1 if fail else 0)

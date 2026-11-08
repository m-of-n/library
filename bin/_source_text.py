"""How a line-numbered RFC .txt is read as prose. Shared by fx1-skeleton,
check-quotes and check-locators, so the three cannot disagree about what a
span of the source "says" (library#86: they did, and check-locators reported
two good requirements unresolvable because of it).

Three rendering artefacts are undone, and only these three. Each is xml2rfc
output, not text the author wrote; undoing them is reading, not healing.

1. Page breaks. The blank run before a page footer, the footer
   ("Author   Standards Track   [Page 7]"), the form feed, the running header
   ("RFC 9679   COSE Key Thumbprint   December 2024") and the blank run after it
   are removed outright, so a sentence that crosses a page stays one sentence.
2. Aside bars. xml2rfc prints `<aside>` / quoted text behind a "|  " margin.
   The bar and its two spaces are margin.
3. Line-end hyphens. xml2rfc breaks a line only AFTER a hyphen the word
   already had, so "well-" + "formed" across a line break is "well-formed",
   with no space. A hyphen the word did not have never appears at a line end.

Everything else is whitespace-collapsed, as every pass has always compared.
Never `splitlines()`: it splits on the form feed and shifts every line number.
"""
import re

FOOTER = re.compile(r"^\S.*\[Page \d+\]\s*$")
HEADER = re.compile(r"^RFC \d+ .*\d{4}\s*$")
ASIDE = re.compile(r"^(\s*)\|  ")
NUMBERED = re.compile(r"^(\d+(?:\.\d+)*)\.\s\s?(\S.*)$")
APPENDIX = re.compile(r"^Appendix\s+([A-Z](?:\.\d+)*)\.\s\s?(\S.*)$")
SUBAPPENDIX = re.compile(r"^([A-Z](?:\.\d+)+)\.\s\s?(\S.*)$")


def read_lines(path):
    return path.read_text(errors="replace").split("\n")


def clean(src):
    """[(lineno, text or None)] — None marks a line that belongs to a page
    break: neither text nor a paragraph-ending blank."""
    out = [[i, l.replace("\f", "")] for i, l in enumerate(src, 1)]
    n = len(out)
    for k in range(n):
        if out[k][1] is not None and FOOTER.match(out[k][1]):
            j = k - 1
            while j >= 0 and out[j][1] is not None and not out[j][1].strip():
                out[j][1] = None
                j -= 1
            out[k][1] = None
            j = k + 1
            while j < n and out[j][1] is not None and (
                    not out[j][1].strip() or HEADER.match(out[j][1])):
                out[j][1] = None
                j += 1
    return [(i, None if l is None else ASIDE.sub(r"\1   ", l)) for i, l in out]


def tokens(cleaned, first=1, last=None):
    """[(token, lineno)] over lines first..last, page breaks dropped."""
    last = last or len(cleaned)
    return [(t, ln) for ln, l in cleaned[first - 1:last] if l is not None
            for t in l.split()]


def join(toks, hyphen=True):
    """Collapse tokens to prose. With hyphen=True a token that ENDS a line in
    "<alnum>-" joins the next line's first token with no space (rule 3)."""
    out = []
    for k, (t, ln) in enumerate(toks):
        if k and not (hyphen and toks[k - 1][1] != ln
                      and re.search(r"[A-Za-z0-9]-$", toks[k - 1][0])):
            out.append(" ")
        out.append(t)
    return "".join(out)


def span(cleaned, first, last, hyphen=True):
    """The prose of source lines first..last (1-based, inclusive)."""
    return join(tokens(cleaned, first, last), hyphen)


def with_lines(cleaned, hyphen=True):
    """(prose of the whole source, per-character source line). Lets a match in
    the collapsed text be turned back into the line range it occupies."""
    out, lines = [], []
    toks = tokens(cleaned)
    for k, (t, ln) in enumerate(toks):
        if k and not (hyphen and toks[k - 1][1] != ln
                      and re.search(r"[A-Za-z0-9]-$", toks[k - 1][0])):
            out.append(" ")
            lines.append(ln)
        out.append(t)
        lines.extend([ln] * len(t))
    return "".join(out), lines


def heading_key(line, letters):
    """'§3.1', 'Appendix B.2', or None for a column-0 RFC heading line."""
    if line.startswith(" "):
        return None
    m = NUMBERED.match(line)
    if m:
        return "§" + m.group(1)
    m = APPENDIX.match(line)
    if m:
        return "Appendix " + m.group(1)
    m = SUBAPPENDIX.match(line)
    if m and m.group(1).split(".")[0] in letters:
        return "Appendix " + m.group(1)
    return None


def appendix_letters(src):
    return {m.group(1).split(".")[0] for l in src for m in [APPENDIX.match(l)] if m}


def section_of_line(src):
    """out[i-1] = the section key line i sits in (None in front matter).

    A heading counts only after a blank line (or at the top). Every RFC and
    rendered-W3C heading stands alone; a table of contents is a run of
    consecutive lines, and the W3C rendering puts it at column 0 with the
    same `1. Introduction` shape, so without this its entries were read as
    headings and the front matter was filed under §1 onward (library#89).
    Measured over the 18 cached sources: only the 3 W3C renderings change,
    and only in their table of contents. Requiring a blank line after the
    heading as well breaks wrapped RFC headings; see bin/test_render_w3c.py.
    """
    letters = appendix_letters(src)
    cur, out, prev = None, [], ""
    for l in src:
        line = l.replace("\f", "")
        if not prev.strip():
            cur = heading_key(line, letters) or cur
        out.append(cur)
        prev = line
    return out


def looks_like_text(src):
    """False for an HTML page cached under .txt (40 rfc records point
    content.url at the .html rendering; library#86)."""
    head = "\n".join(src[:20]).lstrip().lower()
    return not head.startswith(("<!doctype", "<html", "<?xml"))

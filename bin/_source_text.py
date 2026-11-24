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

A PDF source has its own reading (the "PDF profile" at the end of this file,
library#69), chosen by `profile_of(record)`; every *_for function defaults to
the RFC reading above.
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


# ---------------------------------------------------------------------------
# The PDF profile (library#69). A standard published as a PDF — ETSI, ISO/IEC,
# NIST — is read through a pinned `pdftotext -layout` rendering, and its page
# furniture and headings are not xml2rfc's. Everything above is the RFC
# profile and is unchanged: every function below takes `profile` and the
# default reproduces the RFC behaviour exactly, so no count measured through
# the RFC reader moves (hazards.md §6, "fixing a reader falsifies counts").
#
# Two artefacts are undone for a PDF, and only these:
#
# 1. Page furniture. A line in the first or last two non-blank lines of a
#    page whose shape (digits folded to '#', whitespace collapsed) recurs on
#    at least half the pages, and at least three, is a running header or
#    footer. It is removed with the blank run between it and the page edge,
#    as an RFC page break is. Found by recurrence, not by a pattern per
#    publisher, so an ETSI "N   ETSI EN 304 223 V2.1.1 (2025-12)" header and
#    a NIST footer both fall out without a rule naming either.
# 2. Line-end hyphens, exactly as rule 3 above. pdftotext emits the hyphen a
#    line ends on; it never inserts one, so the same join is reading.
#
# A page that ends on a sentence-final line keeps ONE blank line in place of
# its break, so a paragraph that ends at the foot of a page is not welded to
# the first paragraph of the next.
# ---------------------------------------------------------------------------
import hashlib
import shutil
import subprocess

PROFILES = ("rfc", "pdf")
PDF_TOOL = ["pdftotext", "-layout", "-enc", "UTF-8"]
# Numbered clause: "5.1.2    Principle 2: ...", ISO "5.1 General" (one space).
PDF_NUMBERED = re.compile(r"^(\d{1,2}(?:\.\d{1,3})*)\.?\s+([A-Z(\"'].*)$")
# "Annex A (normative):  Title", "Annex B (informative)".
PDF_ANNEX = re.compile(r"^Annex\s+([A-Z])\b(.*)$")
PDF_SUBANNEX = re.compile(r"^([A-Z](?:\.\d{1,3})+)\s+([A-Z(\"'].*)$")
# A table-of-contents entry: dot leaders to a page number.
TOC_ENTRY = re.compile(r"(?:\.\s?){3,}\s*[ivxlc\d]+\s*$")
# FIPS announcement paragraphs run their title in: "10. Approved Security
# Functions. Cryptographic modules that conform ...".
PDF_RUNIN = re.compile(r"^(\d{1,2})\.\s+([A-Z][A-Za-z/&,' -]{2,60}?)\.\s+\S")
# Unnumbered clauses of the ETSI and ISO/IEC drafting rules. Matched whole,
# at column 0, so a sentence that begins "Introduction of ..." is not one.
PDF_TITLED = ("Intellectual Property Rights", "Foreword", "Modal verbs terminology",
              "Introduction", "Executive summary", "History", "Bibliography",
              "Contents", "Abstract")
# Informative by the ETSI Drafting Rules and ISO/IEC Directives Part 2:
# these clauses and NOTE/EXAMPLE blocks "shall not contain requirements".
INFORMATIVE_TITLED = {"Intellectual Property Rights", "Foreword", "Modal verbs terminology",
                      "Introduction", "Executive summary", "History", "Bibliography",
                      "Contents", "Abstract"}


def profile_of(meta):
    """'pdf' for a PDF source of record, 'yaml' for a YAML data model
    (library#69: OWASP DSOMM), else 'rfc'."""
    mt = str(((meta or {}).get("content") or {}).get("media_type") or "")
    if mt == "application/pdf":
        return "pdf"
    if mt in ("application/yaml", "application/x-yaml", "text/yaml"):
        return "yaml"
    return "rfc"


def pdf_tool_version():
    if not shutil.which(PDF_TOOL[0]):
        return None
    p = subprocess.run([PDF_TOOL[0], "-v"], capture_output=True, text=True)
    m = re.search(r"pdftotext version (\S+)", p.stdout + p.stderr)
    return m.group(1) if m else "unknown"


def render_pdf(pdf_path):
    """(text, rendered_by) — the one rendering every tool reads a PDF through.
    `rendered_by` names the tool and version; a different version may break
    lines differently, which is why the digest of the text is recorded."""
    v = pdf_tool_version()
    if v is None:
        raise SystemExit("pdftotext not found — brew install poppler (library#69)")
    p = subprocess.run(PDF_TOOL + [str(pdf_path), "-"], capture_output=True, check=True)
    return p.stdout.decode("utf-8"), f"pdftotext {v} {' '.join(PDF_TOOL[1:])}"


def sha256_text(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


PAGE_NO = re.compile(r"(?:\d{1,4}|[ivxlc]{1,7}|Page \d+(?: of \d+)?)", re.I)


def _shape(line):
    return re.sub(r"\d+", "#", " ".join(line.split()))


def furniture_lines(src):
    """Line numbers (1-based) of running headers and footers in a pdftotext
    rendering. Pages are delimited by form feeds."""
    pages, cur = [], []
    for i, l in enumerate(src, 1):
        parts = l.split("\f")
        # A line that BEGINS with a form feed belongs to the new page only;
        # counting its empty prefix in the old page let that page's edge trim
        # blank the line (FIPS 140-3 L131, L181, L237 — library#69).
        if parts[0] or len(parts) == 1:
            cur.append((i, parts[0]))
        for p in parts[1:]:
            pages.append(cur)
            cur = [(i, p)]
    pages.append(cur)
    edges = []
    for pg in pages:
        nb = [(i, l) for i, l in pg if l.strip()]
        edges.append(nb[:2] + nb[-2:] if len(nb) > 4 else nb)
    count = {}
    for e in edges:
        for s in {_shape(l) for _, l in e}:
            count[s] = count.get(s, 0) + 1
    need = max(3, (len(pages) + 1) // 2)
    hot = {s for s, n in count.items() if n >= need}
    furn = {i for e in edges for i, l in e if _shape(l) in hot}
    # A page edge that is only a page number (arabic or roman) is furniture
    # on any page; so is an edge line repeated EXACTLY on three pages (a
    # running title on the body pages only, FIPS 140-3).
    exact = {}
    for e in edges:
        for t in {" ".join(l.split()) for _, l in e}:
            exact[t] = exact.get(t, 0) + 1
    for pg, e in zip(pages, edges):
        nb = [(i, l) for i, l in pg if l.strip()]
        ends = nb[:1] + nb[-1:]
        for i, l in e:
            t = " ".join(l.split())
            if ((i, l) in ends and PAGE_NO.fullmatch(t)) or (exact.get(t, 0) >= 3 and len(t) >= 8):
                furn.add(i)
    # A long line recurring VERBATIM on half the pages is furniture wherever
    # it falls: NIST prints its "available free of charge" sidebar rotated,
    # and pdftotext places it mid-page. 30 characters keeps a short repeated
    # body line ("Not applicable.") out.
    every = {}
    for pg in pages:
        for t in {" ".join(l.split()) for _, l in pg if len(" ".join(l.split())) >= 30}:
            every[t] = every.get(t, 0) + 1
    side = {t for t, n in every.items() if n >= need}
    furn |= {i for pg in pages for i, l in pg if " ".join(l.split()) in side}
    return furn, pages


def clean_pdf(src):
    """[(lineno, text or None)] for a pdftotext rendering; see the header."""
    furn, pages = furniture_lines(src)
    out = [[i, l.replace("\f", "")] for i, l in enumerate(src, 1)]
    for pg in pages:
        idx = [i for i, _ in pg]
        if not idx:
            continue
        nb = [i for i, l in pg if l.strip() and i not in furn]
        first, last = (nb[0], nb[-1]) if nb else (idx[-1] + 1, idx[0] - 1)
        for i in idx:
            if i in furn or i < first or i > last:
                out[i - 1][1] = None
        # keep one paragraph break where the page ends on a finished sentence
        if nb and re.search(r"[.:;!?)\"']\s*$", src[last - 1]) and last < idx[-1]:
            out[last][1] = ""
        # furniture INSIDE the page (NIST's rotated sidebar): drop it with the
        # blank run around it, so a sentence it interrupts stays one; keep one
        # break if the text before it had finished a sentence
        for i in idx:
            if i in furn and first < i < last:
                j = i - 1
                while j >= first and not (out[j - 1][1] or "").strip():
                    out[j - 1][1] = None
                    j -= 1
                k = i + 1
                while k <= last and not (out[k - 1][1] or "").strip():
                    out[k - 1][1] = None
                    k += 1
                if j >= first and re.search(r"[.:;!?)\"']\s*$", src[j - 1]):
                    out[i - 1][1] = ""
    return [(i, l) for i, l in out]


def clean_for(src, profile="rfc"):
    if profile == "yaml":
        return clean_yaml(src)
    return clean_pdf(src) if profile == "pdf" else clean(src)


def pdf_heading_key(line):
    """'§5.1.2', 'Annex A', 'Annex A.2', a drafting-rules title, or None."""
    line = line.replace("\f", "")
    if not line or line[0] == " " or TOC_ENTRY.search(line):
        return None
    s = line.rstrip()
    if s in PDF_TITLED:
        return s
    m = PDF_ANNEX.match(s)
    if m and (not m.group(2) or re.match(r"\s*(\(|:|[\u2013\u2014-]\s|$)", m.group(2))):
        return "Annex " + m.group(1)
    m = PDF_SUBANNEX.match(s)
    if m and not s.endswith("."):
        return "Annex " + m.group(1)
    m = PDF_RUNIN.match(s)
    if m:
        return "¶" + m.group(1)     # a FIPS announcement paragraph, not a clause
    m = PDF_NUMBERED.match(s)
    if m and not s.endswith(".") and len(m.group(2)) < 160:
        return "§" + m.group(1)
    return None


def body_margin(src):
    """The indent most body lines share. 0 for an ETSI rendering; NIST SP
    renderings put the body ~90 columns in, behind a rotated sidebar, so a
    heading is "at the margin", not at column 0."""
    furn, _ = furniture_lines(src)
    count = {}
    for i, l in enumerate(src, 1):
        line = l.replace("\f", "")
        if line.strip() and i not in furn:
            n = len(line) - len(line.lstrip(" "))
            count[n] = count.get(n, 0) + 1
    return max(count, key=lambda n: (count[n], -n)) if count else 0


def toc_keys(src, margin=0):
    """Clause keys a table of contents lists: every dot-leader line, and the
    two lines before one (a long title wraps its page number down)."""
    furn, _ = furniture_lines(src)
    keys = {}

    def key_of(c):
        c = TOC_ENTRY.sub("", c.replace("\f", "").strip()).rstrip(" .")
        k = pdf_heading_key(c)
        return (k, c) if k and k not in PDF_TITLED else (None, c)

    for i, l in enumerate(src):
        if i + 1 in furn or not TOC_ENTRY.search(l):
            continue
        k, c = key_of(l)
        if not k:
            # a wrapped title: its number is on one of the two lines above
            for j in range(i - 1, max(-1, i - 7), -1):
                if j + 1 in furn or not src[j].strip():
                    continue
                if TOC_ENTRY.search(src[j]):
                    break
                k, c = key_of(src[j])
                if k:
                    break
        if k and k not in keys:
            keys[k] = _title_words(c)
    return keys


def toc_titles(src):
    """Unnumbered titles a table of contents lists ("Configuration
    Management ....... 8"): CISA guides number nothing."""
    furn, _ = furniture_lines(src)
    out = set()
    for i, l in enumerate(src):
        if i + 1 in furn or not TOC_ENTRY.search(l):
            continue
        c = TOC_ENTRY.sub("", l.replace("\f", "").strip()).rstrip(" .")
        if c and not pdf_heading_key(c) and len(c) < 90:
            out.add(c)
    return out


def _title_words(line):
    """The first two words of a heading's title, for matching a heading
    against its table-of-contents entry."""
    parts = line.split(None, 1)
    t = parts[1] if len(parts) > 1 else ""
    if line.startswith("Annex "):
        t = re.sub(r"^[A-Z]\S*\s*(\([^)]*\))?[:\s\u2013\u2014-]*", "", t)
    return [w.lower() for w in re.findall(r"[A-Za-z0-9]+", t)][:2]


def _toc_agrees(toc_words, line):
    h = _title_words(line)
    n = min(len(h), len(toc_words))
    return n == 0 or h[:n] == toc_words[:n]


def pdf_headings(src):
    """{lineno: key} for every heading line, including the indented
    continuation of a wrapped title ("5.1.2   Principle 2: Design ... \\n
    <indent>and performance"). A heading counts after a blank line, at the
    top of a page, or directly after another heading (ETSI prints
    "5.1  Secure Design" and "5.1.1  Principle 1" on consecutive lines)."""
    furn, _ = furniture_lines(src)
    margin = body_margin(src)
    # With a table of contents, a numbered heading must be one it lists: a
    # NIST reference list ("7.    Barker EB ...") and numbered table notes
    # ("12 The module is ...") have the heading's shape and no TOC entry.
    toc = toc_keys(src)
    titled = toc_titles(src)
    depth = lambda k: k.split(" ")[-1].lstrip("§").count(".") + 1
    toc_depth = max((depth(k) for k in toc), default=0)
    heads, prev_ok, last_head, title_col = {}, True, None, None
    prev_indent = 0
    for i, l in enumerate(src, 1):
        if l.startswith("\f"):
            prev_ok = True          # top of a page
        line = l.replace("\f", "")
        if margin and line[:margin].strip() == "":
            line = line[margin:]
        if i in furn or not line.strip():
            prev_ok = prev_ok or not line.strip() or i in furn
            if not line.strip():
                last_head = None
            continue
        # A heading back at the margin straight after an indented list or
        # table line (NIST: "    ● rules of operation" / "B.2.3 Interfaces").
        if not prev_ok and prev_indent > 2 and not line.startswith(" "):
            prev_ok = True
        prev_indent = len(line) - len(line.lstrip(" "))
        k = pdf_heading_key(line) if prev_ok else None
        if prev_ok and not k and line.strip() in titled and not line.startswith(" "):
            k = line.strip()          # an unnumbered title the TOC lists
        if k and toc and k.startswith(("§", "Annex ")) and k not in toc and depth(k) <= toc_depth:
            k = None
        # a TOC of titles only: a numbered line it does not list is a footnote
        if k and titled and not toc and k.startswith(("§", "Annex ")):
            k = None
        # listed, but not under this title: a numbered footnote or list item
        # ("1 Examples may be ports ..." against "1  Scope")
        if k and k in toc and not _toc_agrees(toc[k], line.strip()):
            k = None
        if k:
            heads[i] = k
            m = re.match(r"^\S+(?:\s+\([^)]*\):?)?\s+", line)
            title_col = m.end() if m and k.startswith(("§", "Annex")) else None
            last_head, prev_ok = i, True
            continue
        if (last_head == i - 1 and title_col and line.startswith(" ")
                and len(line) - len(line.lstrip()) == title_col):
            heads[i] = heads[last_head]
            last_head = i
            continue
        prev_ok, last_head = False, None
    return heads


def headings_for(src, profile="rfc"):
    """{lineno: key} of heading lines, in any profile."""
    if profile == "yaml":
        return yaml_structure(src)[0]
    if profile == "pdf":
        return pdf_headings(src)
    letters = appendix_letters(src)
    out = {}
    for i, l in enumerate(src, 1):
        k = heading_key(l.replace("\f", ""), letters)
        if k:
            out[i] = k
    return out


def section_of_line_for(src, profile="rfc"):
    if profile == "yaml":
        return yaml_structure(src)[2]
    if profile != "pdf":
        return section_of_line(src)
    heads, cur, out = pdf_headings(src), None, []
    for i in range(1, len(src) + 1):
        cur = heads.get(i, cur)
        out.append(cur)
    return out


def informative(key):
    """True for a clause the drafting rules make informative by its kind."""
    return bool(key) and (key in INFORMATIVE_TITLED)


# ---------------------------------------------------------------------------
# The YAML profile (library#69). A data model published as YAML — OWASP
# DSOMM's generated/model.yaml — is its own source of record, digest-pinned
# like an RFC .txt. Its prose lives in block scalars (`description: |-`);
# everything else is structure.
#
# - A mapping key whose value is empty or a block scalar is a heading, keyed
#   by its path: "Build and Deployment / Build / Defined build process /
#   measure". A list item is a path component "[n]" (1-based).
# - Only block-scalar content is prose. Every other line reads as a blank, so
#   each block scalar is its own paragraph and no key or value is ever welded
#   into a quotation.
# ---------------------------------------------------------------------------
YAML_KEY = re.compile(r"^(\s*)((?:- )*)([^\s#\-][^:#]*?|\"[^\"]*\"|'[^']*'):(?=\s|$)")
YAML_ITEM = re.compile(r"^(\s*)- ")


def yaml_structure(src):
    """({lineno: path} heading lines, {prose lineno: text}, [path per line]).

    Prose is block-scalar content, and a multi-word inline value (with its
    plain-scalar continuation lines), its `key: ` prefix blanked."""
    heads, prose, per = {}, {}, []
    plain = None         # indent of a key whose plain scalar may continue
    quoted = False       # inside a double-quoted scalar spanning lines
    stack = []           # [(indent, component)]
    counters = {}        # path of a list's parent -> items seen
    block = None         # indent of the key that opened a block scalar
    cur = None
    for i, l in enumerate(src, 1):
        line = l.replace("\f", "")
        if block is not None:
            if not line.strip() or len(line) - len(line.lstrip(" ")) > block:
                if line.strip():
                    prose[i] = line
                per.append(cur)
                continue
            block = None
        if quoted:
            prose[i] = line
            per.append(cur)
            end = (r'(?<!\\)"\s*(?:#.*)?$' if quoted == '"' else r"'\s*(?:#.*)?$")
            if re.search(end, line) and not line.rstrip().endswith("''"):
                quoted = False
            continue
        if plain is not None:
            if (line.strip() and len(line) - len(line.lstrip(" ")) > plain
                    and not YAML_KEY.match(line) and not YAML_ITEM.match(line)):
                prose[i] = line
                per.append(cur)
                continue
            plain = None
        if not line.strip() or line.lstrip().startswith("#") or line.strip() in ("---", "..."):
            per.append(cur)
            continue
        ind = len(line) - len(line.lstrip(" "))
        m_item = YAML_ITEM.match(line)
        if m_item:
            # "- " may sit at its parent key's own indent (YAML allows it):
            # pop deeper entries and sibling items, never the parent key
            while stack and (stack[-1][0] > ind or
                             (stack[-1][0] == ind and stack[-1][1].startswith("["))):
                stack.pop()
            parent = " / ".join(c for _, c in stack)
            counters[(parent, ind)] = counters.get((parent, ind), 0) + 1
            stack.append((ind, f"[{counters[(parent, ind)]}]"))
            # forget the counters of lists nested deeper than this item
            for k in [k for k in counters if k[1] > ind and k[0].startswith(parent)]:
                if k[0] != parent:
                    del counters[k]
            ind += 2
            line = " " * ind + line[m_item.end():]
            body = line.strip()
            if body and not YAML_KEY.match(line) and " " in re.sub(r"\s+#.*$", "", body):
                # a list of strings: each multi-word item is prose
                prose[i] = line
                per.append(cur)
                stack.pop()
                continue
        m = YAML_KEY.match(line)
        if m:
            kind = len(m.group(1)) + 2 * len(m.group(2))
            while stack and stack[-1][0] >= kind:
                stack.pop()
            name = m.group(3).strip("\"'")
            raw = line[m.end(3) + 1:]
            rest = re.sub(r"\s+#.*$", "", raw).strip()
            stack.append((kind, name))
            cur = " / ".join(c for _, c in stack)
            heads[i] = cur
            if rest and rest[0] in "|>":
                block = kind
            elif rest and rest[0] not in "[{&*!" and " " in rest:
                # a multi-word inline value is prose; blank the key prefix
                prose[i] = " " * (m.end(3) + 1) + raw.rstrip()
                if rest[0] not in "\"'":
                    plain = kind
                elif rest[0] == '"' and not re.search(r'(?<!\\)"\s*$', rest[1:]):
                    quoted = '"'
                elif rest[0] == "'" and not re.search(r"'\s*$", rest[1:]):
                    quoted = "'"
            if rest and not (rest[0] in "|>"):
                stack.pop()      # a scalar has no children
        per.append(cur)
    return heads, prose, per


def clean_yaml(src):
    """[(lineno, text)]: block-scalar lines as prose, all else a blank."""
    _, prose, _ = yaml_structure(src)
    return [(i, prose.get(i, "")) for i, l in enumerate(src, 1)]

"""Render one library record as a standalone HTML page beside its source.

`records/<body>/<id>/summary.html` is generated from `record.yaml` (identity,
type, applicability, tags, links) and `summary.md` (prose). Like `index/`,
it is untracked: regenerate with `bin/render-html`. See
docs/generated-views.md.

Publishers (for example tmodel's docs/publishing/render_bibliography.py)
import this module and copy the pages; they do not re-template them. The
page has one hook for a publisher: the `<!-- site-nav -->` comment, which a
site replaces with its own navigation. Links between records are
`<a class="rec" data-id="…">`, so a publisher can unlink a record it does
not publish.

Rules the page follows, and why: tmodel docs/publishing/bibliography-review.md.
Stdlib only. Deterministic: no timestamps, no network.
"""

from __future__ import annotations

import html
import re
from pathlib import Path

from _record_yaml import load_front_matter, load_yaml

LIB = Path(__file__).resolve().parents[1]
RECORDS_ROOT = LIB / "records"
TAGS_PATH = LIB / "schema" / "tags.yaml"
PAGE_NAME = "summary.html"
# The top chrome is a single REPLACEABLE REGION bounded by these two markers. The
# library's own standalone pages render the default banner (README link) between them;
# a publisher that hosts these pages elsewhere replaces everything from SITE_NAV_SLOT
# to SITE_NAV_END (inclusive) with its own nav — so no library-relative link leaks and
# there is no double chrome. Replace the REGION, not just the opening comment.
SITE_NAV_SLOT = "<!-- site-nav -->"
SITE_NAV_END = "<!-- /site-nav -->"
# Link to the library's front page in the default (standalone) banner.
# Relative to records/<body>/<id>/summary.html → the repo-root README.
README_HREF = "../../../README.md"

SCHEMA_BODIES = {
    "ietf", "nist", "w3c", "iso", "oasis", "c2pa", "openssf", "google",
    "academic", "vendor", "community", "regulator", "other",
}
STANDING = {
    "standard", "best-practice", "informational", "experimental", "historic",
    "draft", "recommendation", "white-paper", "implementation", "unofficial",
}
AXES = ("security", "cryptography", "this_project")
AXIS_LABEL = {
    "security": "Security",
    "cryptography": "Cryptography",
    "this_project": "This project",
}
TYPE_HEADING = {
    "rfc": "RFC",
    "draft": "Internet-Draft",
    "spec": "Specification",
    "paper": "Paper",
    "book": "Book",
    "article": "Article",
    "dataset": "Dataset",
    "repo": "Repository",
    "web": "Web page",
    "consortium": "Consortium",
    "note": "Note",
    "hierarchy": "Hierarchy",
    "spreadsheet": "Spreadsheet",
}
BOILERPLATE_MARK = "_Two to five sentences"

def as_list(value) -> list:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def tag_groups(tags: list[str], role: set[str], body: set[str]) -> dict[str, list[str]]:
    groups = {"topic": [], "body": [], "role": [], "standing": []}
    for tag in tags:
        if tag in role:
            groups["role"].append(tag)
        elif tag in body or tag in SCHEMA_BODIES:
            groups["body"].append(tag)
        elif tag in STANDING:
            groups["standing"].append(tag)
        else:
            groups["topic"].append(tag)
    return groups


def load_controlled_tags() -> tuple[set[str], set[str]]:
    data = load_yaml(TAGS_PATH)
    role = set(as_list(data.get("role")))
    body = set(as_list(data.get("body"))) | SCHEMA_BODIES
    return role, body


def str_id(value) -> str:
    if isinstance(value, dict):
        return ""
    return str(value).strip()

# --- markdown --------------------------------------------------------------

def _inline(s: str) -> str:
    s = html.escape(s, quote=True)
    s = re.sub(r"!\[([^\]]*)\]\([^)]+\)", r"\1", s)

    def link(m):
        text, url = m.group(1), html.unescape(m.group(2).strip())
        if url.startswith(("http://", "https://")):
            return f'<a href="{html.escape(url, quote=True)}">{text}</a>'
        return text

    s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", link, s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<!\*)\*([^*\n]+)\*(?!\*)", r"<em>\1</em>", s)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    return s


def md_to_html(md: str) -> str:
    lines = md.replace("\r\n", "\n").split("\n")
    # Drop a single leading H1; the page title already says it.
    i = 0
    while i < len(lines) and lines[i].strip() == "":
        i += 1
    if i < len(lines) and lines[i].startswith("# "):
        i += 1
    lines = lines[i:]
    html_parts: list[str] = []
    para: list[str] = []
    lst: list[str] = []

    def flush_para():
        nonlocal para
        if para:
            html_parts.append("<p>" + _inline(" ".join(para)) + "</p>")
            para = []

    def flush_list():
        nonlocal lst
        if lst:
            html_parts.append("<ul>" + "".join(f"<li>{_inline(x)}</li>" for x in lst) + "</ul>")
            lst = []

    j = 0
    while j < len(lines):
        line = lines[j]
        stripped = line.strip()
        if stripped.startswith("```"):
            flush_para()
            flush_list()
            j += 1
            buf = []
            while j < len(lines) and not lines[j].strip().startswith("```"):
                buf.append(html.escape(lines[j]))
                j += 1
            if j < len(lines):
                j += 1
            html_parts.append("<pre>" + "\n".join(buf) + "</pre>")
            continue
        if stripped.startswith("|") and stripped.endswith("|"):
            flush_para()
            flush_list()
            rows = []
            while j < len(lines) and lines[j].strip().startswith("|"):
                cells = [c.strip() for c in lines[j].strip().strip("|").split("|")]
                rows.append(cells)
                j += 1
            data = [r for r in rows if not all(re.fullmatch(r":?-{3,}:?", c or "") for c in r)]
            if data:
                head, *rest = data
                thead = "".join(f"<th>{_inline(c)}</th>" for c in head)
                body = ""
                for r in rest:
                    body += "<tr>" + "".join(f"<td>{_inline(c)}</td>" for c in r) + "</tr>"
                html_parts.append(f"<table><thead><tr>{thead}</tr></thead><tbody>{body}</tbody></table>")
            continue
        if stripped.startswith("##"):
            flush_para()
            flush_list()
            level = len(stripped) - len(stripped.lstrip("#"))
            level = min(max(level, 2), 4)
            text = stripped[level:].strip()
            html_parts.append(f"<h{level}>{_inline(text)}</h{level}>")
            j += 1
            continue
        if lst and (line.startswith(" ") or line.startswith("\t")) and stripped and not re.match(r"^[-*] ", stripped) and not stripped.startswith("|") and not stripped.startswith("#"):
            lst[-1] = lst[-1] + " " + stripped
            j += 1
            continue
        if re.match(r"^[-*] ", stripped):
            flush_para()
            lst.append(stripped[2:].strip())
            j += 1
            continue
        if stripped == "":
            flush_para()
            flush_list()
            j += 1
            continue
        flush_list()
        para.append(stripped)
        j += 1
    flush_para()
    flush_list()
    return "\n".join(html_parts)


# --- html chrome -----------------------------------------------------------

CSS = """
:root {
  --ink: #1a1916;
  --muted: #5c574e;
  --line: #e2dcd0;
  --paper: #f6f3ec;
  --card: #fffcf7;
  --accent: #1e4d3a;
  --warn: #6b4e16;
  --warn-bg: #f3ead3;
  --bad-bg: #f6e4dc;
  --ok-bg: #e5efe8;
}
* { box-sizing: border-box; }
body {
  margin: 0;
  color: var(--ink);
  background: var(--paper);
  font-family: ui-sans-serif, system-ui, -apple-system, "Segoe UI", Helvetica, Arial, sans-serif;
  font-size: 16px;
  line-height: 1.5;
}
a { color: var(--accent); }
a:hover { text-decoration: none; }
.wrap { max-width: 880px; margin: 0 auto; padding: 0 24px 40px; }
header { border-bottom: 1px solid var(--line); background: var(--card); }
.bar {
  max-width: 920px; margin: 0 auto; padding: 16px 24px;
  display: flex; flex-wrap: wrap; align-items: baseline; justify-content: space-between; gap: 12px 18px;
}
.mark { font-weight: 650; letter-spacing: -0.03em; color: var(--ink); text-decoration: none; }
nav { display: flex; flex-wrap: wrap; gap: 14px; font-size: 0.92rem; }
nav a { color: var(--muted); text-decoration: none; }
nav a[aria-current="page"] { color: var(--ink); font-weight: 650; }
h1 { font-size: clamp(1.6rem, 2.6vw, 2.1rem); line-height: 1.15; letter-spacing: -0.03em; margin: 20px 0 6px; }
h2 { font-size: 1.15rem; margin: 1.25em 0 0.3em; padding-top: 0.6em; border-top: 1px solid var(--line); }
h3 { font-size: 1rem; margin: 1em 0 0.2em; }
.kicker { margin: 18px 0 0; font-size: 0.74rem; letter-spacing: 0.14em; text-transform: uppercase; color: var(--accent); font-weight: 650; }
.lede { color: var(--muted); margin-top: 0; }
.banner, .callout {
  background: var(--warn-bg); color: var(--warn); border-radius: 8px; padding: 12px 14px; margin: 16px 0;
}
.callout.quiet { background: var(--card); color: var(--ink); border: 1px solid var(--line); }
.callout strong { color: var(--ink); }
ul.clean { padding-left: 1.2rem; }
table { width: 100%; border-collapse: collapse; margin: 0.4em 0 0.8em; background: var(--card); }
th, td { text-align: left; vertical-align: top; border-bottom: 1px solid var(--line); padding: 6px 10px; font-size: 0.93rem; }
table.kv { background: transparent; }
table.kv td { border-bottom: none; padding: 2px 12px 2px 0; }
td.rowhead { color: var(--muted); font-size: 0.74rem; letter-spacing: 0.04em; text-transform: uppercase; white-space: nowrap; width: 1%; padding-top: 6px; }
th { font-size: 0.78rem; letter-spacing: 0.04em; text-transform: uppercase; color: var(--muted); }
code { font-size: 0.9em; }
.badge {
  display: inline-block; padding: 1px 8px; border-radius: 999px; background: var(--card);
  border: 1px solid var(--line); font-size: 0.82rem; margin: 0 4px 4px 0;
}
.badge.core { background: var(--ok-bg); }
.badge.none, .badge.not-assessed { background: var(--bad-bg); }
.badge.broad { background: var(--warn-bg); }
.meta { color: var(--muted); font-size: 0.92rem; }
footer { margin-top: 48px; color: var(--muted); font-size: 0.85rem; border-top: 1px solid var(--line); padding-top: 16px; }
.cardlink { display: block; padding: 12px 0; border-bottom: 1px solid var(--line); text-decoration: none; color: inherit; }
.cardlink:hover { background: transparent; }
.cardlink strong { color: var(--accent); }
ol.refs { list-style: none; padding: 0; margin: 0; }
ol.refs li { padding: 8px 0 8px 1.6em; text-indent: -1.6em; border-bottom: 1px solid var(--line); overflow-wrap: anywhere; }
ol.refs cite { font-style: italic; }
nav.jump { display: flex; flex-wrap: wrap; gap: 4px 10px; margin: 18px 0 0; font-weight: 600; }
"""


def esc(value) -> str:
    if value is None:
        return ""
    return html.escape(str(value), quote=True)


# --- record pages ----------------------------------------------------------

def applicability_table(app: dict | None) -> str:
    app = app or {}
    rows = []
    keys = list(AXES) + sorted(k for k in app.keys() if k not in AXES)
    for key in keys:
        if key in app and app[key] not in (None, ""):
            rating = str(app[key])
            shown = rating
        else:
            rating = "not-assessed"
            shown = "not assessed"
        label = AXIS_LABEL.get(key, key)
        rows.append(
            f"<tr><td>{esc(label)}</td><td><span class=\"badge {esc(rating)}\">{esc(shown)}</span></td></tr>"
        )
    note = (
        "<p class=\"meta\">From <code>record.yaml</code>; a missing axis is "
        "not assessed, not <code>none</code>.</p>"
    )
    return (
        "<table><thead><tr><th>Axis</th><th>Rating</th></tr></thead><tbody>"
        + "".join(rows)
        + "</tbody></table>"
        + note
    )


def tag_html(groups: dict[str, list[str]]) -> str:
    labels = [
        ("topic", "Topic"),
        ("body", "Body"),
        ("role", "Role"),
        ("standing", "Standing"),
    ]
    rows = []
    for key, title in labels:
        tags = groups[key]
        if not tags:
            continue
        badges = " ".join(f'<span class="badge">{esc(t)}</span>' for t in tags)
        rows.append(f"<tr><td class=\"rowhead\">{title}</td><td>{badges}</td></tr>")
    if not rows:
        return "<p class=\"meta\">No tags recorded.</p>"
    return "<table class=\"kv\"><tbody>" + "".join(rows) + "</tbody></table>"


def type_section(rec: dict, published: dict[str, dict]) -> str:
    typ = rec["type"]
    heading = TYPE_HEADING.get(typ, typ)
    bits = [f"<h2>{esc(heading)}</h2>"]
    ident = rec["identifiers"]
    if typ == "draft":
        bits.append(
            "<div class=\"callout\"><strong>Not a standard.</strong> "
            "An Internet-Draft is not an RFC. Maturity below is the record's "
            "own field, not a ratification this page inferred.</div>"
        )
    elif typ == "dataset":
        bits.append(
            "<div class=\"callout\"><strong>Catalog, not one row.</strong> "
            "This record is the enumeration itself. Retrieved is when the library "
            "looked, not an edition date. Empty authors are omitted, not missing paper metadata.</div>"
        )
    elif typ == "web":
        bits.append(
            "<div class=\"callout\"><strong>Not an edition.</strong> "
            "A web page can change under the same URL. Retrieved is the look-up date.</div>"
        )
    elif typ == "repo":
        bits.append(
            "<div class=\"callout\"><strong>Implementation, not a ratified text.</strong> "
            "The primary link is the repository URL.</div>"
        )
    elif typ == "paper":
        bits.append(
            "<p class=\"meta\">Authors and date are whatever the record states. "
            "This page does not add a venue.</p>"
        )
    elif typ == "rfc":
        bits.append("<p class=\"meta\">RFC number and DOI are identifiers on the record. Maturity is the record's field.</p>")

    rows = []
    if typ in ("rfc", "paper", "spec", "book", "article", "draft") and rec["authors"]:
        rows.append(("Authors", ", ".join(rec["authors"])))
    if rec["date"] and typ in ("rfc", "paper", "spec", "book", "article", "draft"):
        rows.append(("Date", rec["date"]))
    if typ == "dataset" or typ == "web":
        if rec["retrieved"]:
            rows.append(("Retrieved", rec["retrieved"]))
    if typ == "repo" and rec["retrieved"]:
        rows.append(("Retrieved", rec["retrieved"]))
    if rec["publisher"] and typ in ("rfc", "spec", "paper", "book", "draft"):
        rows.append(("Publisher", rec["publisher"]))
    if rec["version"]:
        rows.append(("Version", rec["version"]))
    if rec["maturity"]:
        rows.append(("Maturity", rec["maturity"]))
    if isinstance(ident, dict):
        for key in sorted(ident):
            if key == "url":
                continue
            val = ident[key]
            if val in (None, ""):
                continue
            shown = str(val)
            if key == "doi":
                shown = f'<a href="https://doi.org/{esc(val)}">{esc(val)}</a>'
                rows.append((key, shown, True))
                continue
            rows.append((key, shown))
    if rec["pages"]:
        rows.append(("Pages", rec["pages"]))
    if rec["media_type"]:
        rows.append(("Media type", rec["media_type"]))
    if rows:
        body = ""
        for row in rows:
            if len(row) == 3:
                body += f"<tr><td>{esc(row[0])}</td><td>{row[1]}</td></tr>"
            else:
                body += f"<tr><td>{esc(row[0])}</td><td>{esc(row[1])}</td></tr>"
        bits.append(f"<table><tbody>{body}</tbody></table>")

    impl = rec["implementations"] or {}
    oss = as_list(impl.get("open_source"))
    if typ == "repo":
        n = len([x for x in oss if isinstance(x, dict)])
        searched = impl.get("searched") or "not recorded"
        bits.append(
            f"<p>Open-source implementations recorded: {n}. "
            f"Search date: {esc(searched)}. Names stay in <code>record.yaml</code> "
            "and, when the summary was written, in the summary prose.</p>"
        )
    elif oss and typ == "rfc":
        bits.append(
            f"<p class=\"meta\">{len(oss)} open-source implementations are on the record. "
            "The summary prose below is the reviewed short list; this page does not "
            "re-typeset every note.</p>"
        )
    return "\n".join(bits)


def relations_section(rec: dict, published: dict[str, dict]) -> str:
    rel = rec["relations"] or {}
    if not isinstance(rel, dict):
        return ""
    blocks = []
    for key in (
        "supersedes", "superseded_by", "updates", "updated_by", "see_also",
        "implements_concept", "contradicts", "part_of", "cited_by",
    ):
        ids = [str_id(x) for x in as_list(rel.get(key)) if str_id(x)]
        if not ids:
            continue
        # supersedes already shown in the type section for some types; still list here once
        items = "".join(f"<li>{link_record_rel(x, published, rec['id'])}</li>" for x in ids)
        blocks.append(f"<h3><code>{esc(key)}</code></h3><ul>{items}</ul>")
    if not blocks:
        return ""
    return (
        "<h2>Recorded relations</h2>"
        "<p class=\"meta\">Curatorial <code>relations</code> only — not crosswalk edges.</p>"
        + "".join(blocks)
    )


def cites_section(rec: dict, published: dict[str, dict]) -> str:
    cites = as_list(rec["cites"])
    if not cites:
        return ""
    items = []
    for entry in cites:
        if isinstance(entry, dict):
            title = entry.get("title") or entry.get("ref") or "untitled gap"
            loc = entry.get("locator") or ""
            ref = entry.get("ref")
            label = esc(title)
            if isinstance(loc, str) and loc.startswith(("http://", "https://")):
                label = f'<a href="{esc(loc)}">{esc(title)}</a>'
            prefix = f"{esc(ref)} " if ref else ""
            items.append(f"<li>{prefix}{label} <span class=\"meta\">cited, no library record</span></li>")
        else:
            ident = str_id(entry)
            if not ident:
                continue
            items.append(f"<li>{link_record_rel(ident, published, rec['id'])}</li>")
    if not items:
        return ""
    return (
        "<h2>Document cites</h2>"
        "<p class=\"meta\">From <code>cites</code> — what the source references.</p><ul>"
        + "".join(items) + "</ul>"
    )


def bib_links(rec: dict) -> str:
    rows = []
    if rec["url"]:
        rows.append(f'<li>Source: <a href="{esc(rec["url"])}">{esc(rec["url"])}</a></li>')
    ident = rec["identifiers"] if isinstance(rec["identifiers"], dict) else {}
    extra = ident.get("url")
    if isinstance(extra, str) and extra.startswith(("http://", "https://")) and extra != rec["url"]:
        rows.append(f'<li>Identifier URL: <a href="{esc(extra)}">{esc(extra)}</a></li>')
    if rec["sha256"]:
        rows.append(f"<li>SHA-256: <code>{esc(rec['sha256'])}</code></li>")
    else:
        rows.append("<li>SHA-256: <span class=\"meta\">not recorded</span></li>")
    if rec["local"] is True:
        rows.append(
            "<li><strong>Local flag is true.</strong> No filesystem path is shown. "
            "The schema requires <code>local: false</code>.</li>"
        )
    if not rows:
        return "<p class=\"meta\">No bibliographic links recorded.</p>"
    return "<ul>" + "".join(rows) + "</ul>"


def record_page(rec: dict, published: dict[str, dict]) -> str:
    bears = [str_id(x) for x in rec["bears_on"] if str_id(x)]
    if bears:
        bear_html = "<ul>" + "".join(f"<li><code>{esc(b)}</code></li>" for b in bears) + "</ul>"
    else:
        bear_html = "<p class=\"meta\">No <code>bears_on</code> ids recorded. None were invented.</p>"
    if rec["summary_written"]:
        summary = (
            "<h2>Summary</h2>"
            "<p class=\"meta\">Prose from <code>summary.md</code>, unedited.</p>"
            + rec["summary_html"]
        )
    else:
        summary = (
            "<h2>Summary</h2>"
            "<div class=\"callout\"><strong>Summary not written.</strong> "
            "<code>summary.md</code> is still the library template "
            "(it still contains the “two to five sentences” instruction). "
            "That text is not rendered. This page is record metadata only.</div>"
        )
    usefulness = ""
    if rec["usefulness"]:
        verdict = rec["usefulness"].get("verdict") or "unassessed"
        reason = rec["usefulness"].get("reason") or ""
        assessed = rec["usefulness"].get("assessed") or ""
        usefulness = (
            f"<h2>Usefulness</h2><p><span class=\"badge\">{esc(verdict)}</span> "
            f"{esc(reason)}</p>"
        )
        if assessed:
            usefulness += f"<p class=\"meta\">Assessed {esc(assessed)}.</p>"
    if rec["record_topic"]:
        topic_html = f"Topic: <strong>{esc(rec['record_topic'])}</strong> (<code>record.yaml</code> topic)."
    elif rec["groups"]["topic"]:
        topic_html = "No <code>topic</code> field; subject tags are below."
    else:
        topic_html = "No <code>topic</code> field and no subject tag yet."
    body = f"""
<p class="kicker">Library record · {esc(rec['id'])}</p>
<h1>{esc(rec['title'])}</h1>
<p class="lede">{esc(rec.get('short_title') or '')}</p>
<p>
  <span class="badge">{esc(rec['type'])}</span>
  <span class="badge">{esc(rec['body'])}</span>
  <span class="badge">{esc(rec['status'])}</span>
  <span class="badge">{esc(rec['confidence'] or 'confidence unset')}</span>
</p>
<p class="meta">{topic_html} Status <code>{esc(rec['status'])}</code> is how far review got, not a quality score.</p>
<h2>Bibliographic links</h2>
{bib_links(rec)}
{type_section(rec, published)}
<h2>Applicability</h2>
{applicability_table(rec['applicability'])}
<h2>Tags</h2>
{tag_html(rec['groups'])}
<h2>Bears on</h2>
{bear_html}
{usefulness}
{relations_section(rec, published)}
{cites_section(rec, published)}
{summary}
"""
    return page(rec["title"], body)



# --- links, chrome, loading --------------------------------------------------

def record_href(rec: dict) -> str:
    """Path of a record page relative to another record page."""
    return f"../../{rec['body']}/{rec['id']}/{PAGE_NAME}"


def link_record_rel(record_id: str, published: dict[str, dict], here: str) -> str:
    rec = published.get(record_id)
    label = esc(rec["short"] if rec else record_id)
    ident = esc(record_id)
    if record_id == here:
        return f"{label} <span class=\"meta\">(this page)</span>"
    if rec:
        return f'<a class="rec" data-id="{ident}" href="{esc(record_href(rec))}">{label}</a>'
    return f"<code>{ident}</code> <span class=\"meta\">no library record</span>"


def page(title: str, body: str) -> str:
    return (
        "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n"
        '<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
        '<meta name="referrer" content="no-referrer">\n'
        f"<title>{esc(title)}</title>\n"
        f"<style>{CSS}</style>\n</head>\n<body>\n"
        f"{SITE_NAV_SLOT}\n"
        "<header><div class=\"bar\">"
        f"<a class=\"mark\" href=\"{README_HREF}\">Threat-Radar library</a>"
        f"<nav><a href=\"{README_HREF}\">README ↑</a></nav>"
        "</div></header>\n"
        f"{SITE_NAV_END}\n"
        f"<main class=\"wrap\">\n{body}\n"
        "<footer><p>Generated from <code>record.yaml</code> and <code>summary.md</code> "
        "in this directory by the library's <code>bin/render-html</code>. Do not hand-edit. "
        "Static HTML, no scripts, no trackers.</p></footer>\n</main>\n</body>\n</html>\n"
    )


def record_paths() -> list[Path]:
    """One record per `records/<body>/<id>/`. `versions/` snapshots are not records."""
    return sorted(RECORDS_ROOT.glob("*/*/record.yaml"))


def load_record(path: Path, role: set[str], body_tags: set[str]) -> dict:
    data = load_yaml(path)
    record_id = data.get("id")
    if record_id != path.parent.name:
        raise SystemExit(f"{path}: id is {record_id!r}, directory is {path.parent.name!r}")
    tags = [str(t) for t in as_list(data.get("tags"))]
    record_topic = str(data.get("topic") or "").strip()
    summary_path = path.parent / "summary.md"
    summary_written = False
    summary_html = ""
    front_type = None
    if summary_path.exists():
        fm, md = load_front_matter(summary_path.read_text(encoding="utf-8"), str(summary_path))
        front_type = fm.get("type")
        summary_written = BOILERPLATE_MARK not in md
        if summary_written:
            summary_html = md_to_html(md)
    content = data.get("content") if isinstance(data.get("content"), dict) else {}
    local = content.get("local")
    url = content.get("url") if isinstance(content.get("url"), str) else ""
    if local is True and not url.startswith(("http://", "https://")):
        url = ""
    usefulness = data.get("usefulness") if isinstance(data.get("usefulness"), dict) else {}
    as_map = lambda v: v if isinstance(v, dict) else {}
    return {
        "id": record_id,
        "title": data.get("title") or record_id,
        "short": data.get("short_title") or data.get("title") or record_id,
        "short_title": data.get("short_title") or "",
        "type": data.get("type"),
        "body": data.get("body") or path.parent.parent.name,
        "status": data.get("status") or "",
        "maturity": data.get("maturity") or "",
        "confidence": data.get("confidence") or "",
        "date": str(data.get("date") or ""),
        "publisher": data.get("publisher") or "",
        "version": str(data.get("version") or ""),
        "authors": [a for a in as_list(data.get("authors")) if isinstance(a, str)],
        "identifiers": as_map(data.get("identifiers")),
        "url": url,
        "sha256": content.get("sha256") or "",
        "retrieved": str(content.get("retrieved") or ""),
        "local": local,
        "pages": content.get("pages") or "",
        "media_type": content.get("media_type") or "",
        "relations": as_map(data.get("relations")),
        "cites": data.get("cites"),
        "bears_on": as_list(data.get("bears_on")),
        "applicability": as_map(data.get("applicability")),
        "implementations": as_map(data.get("implementations")),
        "usefulness": usefulness,
        "tags": tags,
        "groups": tag_groups(tags, role, body_tags),
        "record_topic": record_topic,
        "summary_written": summary_written,
        "summary_html": summary_html,
        "summary_front_type": front_type,
        "path": path,
        "page_path": path.parent / PAGE_NAME,
    }


def load_all() -> dict[str, dict]:
    role, body_tags = load_controlled_tags()
    records: dict[str, dict] = {}
    for path in record_paths():
        rec = load_record(path, role, body_tags)
        if rec["id"] in records:
            raise SystemExit(f"duplicate record id {rec['id']}")
        records[rec["id"]] = rec
    return records


def refuse_active(text: str, name: str):
    lower = text.lower()
    if "<script" in lower or "javascript:" in lower:
        raise SystemExit(f"{name}: script refused")
    # A citation may link to a repo named `foo.js`; only a loaded asset is refused.
    if re.search(r"<(?:script|link|img|iframe)\b[^>]*(?:src|href)=[\"']?(?:https?:)?//", text, re.I):
        raise SystemExit(f"{name}: remote asset refused")


def render(records: dict[str, dict], only: list[str] | None = None) -> list[Path]:
    """Write summary.html beside each record. Returns the paths written."""
    written = []
    for rid in (only if only is not None else sorted(records)):
        rec = records.get(rid)
        if rec is None:
            raise SystemExit(f"{rid}: no such record")
        text = record_page(rec, records)
        refuse_active(text, rid)
        rec["page_path"].write_text(text, encoding="utf-8")
        written.append(rec["page_path"])
    return written

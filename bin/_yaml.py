"""Minimal nested YAML reader — enough for library records, no dependencies.

Handles arbitrary nesting of block maps and block sequences, block scalars
(`|`, `|-`, `|+`, `>`, `>-`, `>+`, with an optional indentation digit), and
trailing ` # comments` on plain scalars.

Not a YAML implementation. No anchors, flow collections or tags — the record
schema forbids them. If a file needs those, use a real parser.

History, because both bugs were silent: the first version flattened nested
maps and made every crosswalk edge disappear; the second returned the
two-character marker `|-` for every block scalar and dropped its content, so
36 of 44 FX-1 test vectors were unreadable to CI (library#43).
bin/test_yaml.py pins all of it.
"""
import re

_BLOCK = re.compile(r"^([|>])([-+]?)(\d?)([-+]?)\s*(#.*)?$")


def _strip_comment(v):
    """Drop a trailing ` # comment`, as YAML does for plain scalars.

    A quoted scalar keeps everything inside its quotes; a `#` not preceded by
    whitespace (a URL fragment, `#R-0001`) is not a comment.
    """
    v = v.strip()
    if v and v[0] in "\"'":
        q, i = v[0], 1
        while i < len(v):
            if q == '"' and v[i] == "\\":
                i += 2
                continue
            if v[i] == q:
                if q == "'" and v[i + 1:i + 2] == "'":
                    i += 2
                    continue
                rest = v[i + 1:].strip()
                # Only a comment may follow a closing quote; anything else
                # means this was not one quoted scalar, so leave it intact.
                return v[:i + 1] if not rest or rest.startswith("#") else v
            i += 1
        return v
    if v.startswith("#"):
        return ""
    for i in range(1, len(v)):
        if v[i] == "#" and v[i - 1] in " \t":
            return v[:i].rstrip()
    return v


def _scalar(v):
    v = _strip_comment(v.strip()).strip()
    if len(v) >= 2 and v[0] == v[-1] and v[0] in "\"'":
        return v[1:-1]
    if v == "[]":
        return []
    if v == "{}":
        return {}
    return v


def _block(lines, i, parent_indent, style, chomp):
    """Read a block scalar starting at lines[i]. Returns (value, next_index)."""
    body, j = [], i
    while j < len(lines):
        ln = lines[j].expandtabs(2)
        if ln.strip() and len(ln) - len(ln.lstrip()) <= parent_indent:
            break
        body.append(ln)
        j += 1
    # trailing blank lines belong to chomping, not to the next key
    content = [l for l in body if l.strip()]
    if not content:
        return "", j
    ind = min(len(l) - len(l.lstrip()) for l in content)
    rows = [l[ind:] if l.strip() else "" for l in body]
    while rows and rows[-1] == "":
        rows.pop()
    trailing = len(body) - len(rows)
    if style == "|":
        text = "\n".join(rows)
    else:
        # folded (YAML 1.2 §8.1.3): a break between two plain lines becomes a
        # space; each blank line becomes one newline; more-indented lines keep
        # their breaks.
        text, prev = "", None
        for r in rows:
            if prev is None:
                text = r
            elif r == "":
                text += "\n"
            elif prev == "":
                text += r
            elif r[:1] in " \t" or prev[:1] in " \t":
                text += "\n" + r
            else:
                text += " " + r
            prev = r
    if chomp == "-":
        return text, j
    if chomp == "+":
        return text + "\n" * (1 + trailing), j
    return text + "\n", j


def parse(text):
    root = {}
    stack = [(-1, root)]        # (indent, container)
    pending_key = None          # (indent, dict, key) awaiting a nested block
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        raw = lines[i]
        i += 1
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        raw_e = raw.expandtabs(2)
        indent = len(raw_e) - len(raw_e.lstrip())
        line = raw.strip()

        while len(stack) > 1 and indent < stack[-1][0]:
            stack.pop()
        cur = stack[-1][1]

        if pending_key and indent > pending_key[0]:
            d, k = pending_key[1], pending_key[2]
            cur = [] if line.startswith("- ") or line == "-" else {}
            d[k] = cur
            stack.append((indent, cur))
            pending_key = None
        elif pending_key:
            pending_key = None

        def assign(d, k, v, key_indent):
            """Set d[k] from raw value text v; consumes a block scalar if v is one."""
            nonlocal i, pending_key
            v = v.strip()
            m = _BLOCK.match(v)
            if m:
                style, chomp = m.group(1), (m.group(2) or m.group(4))
                d[k], i = _block(lines, i, key_indent, style, chomp)
            elif v and not _strip_comment(v).strip() == "":
                d[k] = _scalar(v)
            else:
                d[k] = {}
                pending_key = (key_indent, d, k)

        if line.startswith("- "):
            item = line[2:].strip()
            if not isinstance(cur, list):
                continue
            if re.match(r"^[^\s\"'][^:]*:(\s|$)", item) and not item.startswith(("http:", "https:")):
                k, _, v = item.partition(":")
                d = {}
                cur.append(d)
                # A sequence item that is a map: its remaining keys sit at the
                # indent of this first key, so push the dict so they attach to
                # it rather than being dropped.
                stack.append((indent + 2, d))
                assign(d, k.strip(), v, indent + 2)
            else:
                m = _BLOCK.match(item)
                if m:
                    val, i = _block(lines, i, indent, m.group(1), m.group(2) or m.group(4))
                    cur.append(val)
                else:
                    cur.append(_scalar(item))
        elif ":" in line:
            k, _, v = line.partition(":")
            if not isinstance(cur, dict):
                continue
            assign(cur, k.strip(), v, indent)
    return root

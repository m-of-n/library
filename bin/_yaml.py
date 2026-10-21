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


def _split_flow(inner):
    """Split a flow collection's body on top-level commas."""
    out, buf, depth, q = [], [], 0, None
    i = 0
    while i < len(inner):
        c = inner[i]
        if q:
            buf.append(c)
            if q == '"' and c == "\\":
                if i + 1 < len(inner):
                    buf.append(inner[i + 1])
                    i += 2
                    continue
            elif c == q:
                if q == "'" and inner[i + 1:i + 2] == "'":
                    buf.append(inner[i + 1])
                    i += 2
                    continue
                q = None
        elif c in "\"'":
            q = c
            buf.append(c)
        elif c in "[{":
            depth += 1
            buf.append(c)
        elif c in "]}":
            depth -= 1
            buf.append(c)
        elif c == "," and depth == 0:
            out.append("".join(buf))
            buf = []
        else:
            buf.append(c)
        i += 1
    if "".join(buf).strip():
        out.append("".join(buf))
    return out


def _flow_map(v):
    """Parse `{a: 1, b: "x, y"}` into a dict, or return None if it is not one.

    bin/_record_yaml.py has always done this; this parser did not, so an
    inline flow map became a single STRING KEY holding the whole brace
    expression. 4331 lines in the library are written that way, including two
    records at profile: full, so the two readers disagreed on all of them —
    one lane measured 358 keys present under one reader and absent under the
    other in a single file, and the key COUNTS matched, which is what hid it
    (library#39).
    """
    if not (v.startswith("{") and v.endswith("}")):
        return None
    inner = v[1:-1].strip()
    if not inner:
        return {}
    out = {}
    for part in _split_flow(inner):
        part = part.strip()
        if not part:
            continue
        k, sep, val = part.partition(":")
        if not sep:
            return None        # not a map after all; leave it as text
        out[_scalar(k.strip())] = _scalar(val.strip())
    return out


def _scalar(v):
    v = _strip_comment(v.strip()).strip()
    if len(v) >= 2 and v[0] == v[-1] and v[0] in "\"'":
        # single-quoted YAML escapes a quote by doubling it: 'it''s' -> it's
        return v[1:-1].replace("''", "'") if v[0] == "'" else v[1:-1]
    if v == "[]":
        return []
    if v == "{}":
        return {}
    if v[:1] == "{" and v[-1:] == "}":
        m = _flow_map(v)
        if m is not None:
            return m
    # A flow sequence. bin/_record_yaml.py has always returned a list here and
    # this parser returned the bracket text, so the library's two readers
    # disagreed on 14,069 sites. Making them agree is the point: several
    # extraction passes had to hand-work around the difference.
    if v[:1] == "[" and v[-1:] == "]":
        return [_scalar(p.strip()) for p in _split_flow(v[1:-1].strip())]
    return v


# A line that reads as the next map key or sequence item rather than as the
# continuation of a wrapped scalar. Used only to bound that continuation.
_NEXT_ENTRY = re.compile(r"^(?:-\s|-$|[A-Za-z_][\w.-]*:(?:\s|$))")


def _quote_closed(v):
    """Is the quoted scalar `v` terminated on its own line?"""
    q = v[0]
    j = 1
    while j < len(v):
        if q == '"' and v[j] == "\\":
            j += 2
            continue
        if v[j] == q:
            # In single-quoted YAML '' is an escaped quote, not a terminator.
            if q == "'" and v[j + 1:j + 2] == "'":
                j += 2
                continue
            return True
        j += 1
    return False


def _quoted_continuation(lines, i, v):
    """Join a quoted scalar that wraps across lines. Returns (text, next_i).

    YAML folds a wrapped flow scalar onto one line with a single space. This
    parser used to keep only the first line AND its opening quote, so
    `text: "Threat modeling is a security focused design activity` became a
    value beginning with a stray quote and ending mid-sentence. 71 lines in
    the library wrap this way, most of them `text:` fields in
    requirements.yaml — the one field FX-1's verbatim checks exist to read
    (library#39).
    """
    if v[:1] not in "\"'" or _quote_closed(v):
        return v, i
    while i < len(lines):
        nxt = lines[i].strip()
        # Stop at anything that reads as the next entry rather than as more of
        # this sentence. Records in this library contain genuinely unterminated
        # quoted scalars — draft-ietf-cbor-edn-literals' requirements.yaml line
        # 152 ends `''...#R-0066''` with no closing quote — and without this
        # guard the scalar swallows the `verb:` line after it. bin/_record_yaml
        # is lenient the same way, by ending such a scalar at its line break.
        if _NEXT_ENTRY.match(nxt):
            break
        i += 1
        v += " " + nxt
        if _quote_closed(v):
            break
    return v, i


def _flow_continuation(lines, i, v):
    """Join a flow collection that wraps across lines. Returns (text, next_i).

    This parser deliberately does NOT parse flow collections: `["a", "b"]`
    comes back as its own text, and 14,000-odd call sites in the library rely
    on that. What it must not do is return a TRUNCATED prefix. Before this,
    a `constrained_by` list wrapped over two lines silently lost every id
    after the first line — three of them in rfc-8392's protocol.yaml and
    state-machine.yaml (library#39). Nothing warned: the value simply ended
    mid-list, and the continuation line was then read as garbage at an
    unexpected indent.

    Bracket counting ignores quoting, so a flow collection holding a string
    with an unbalanced bracket in it still wraps wrongly. That is a smaller
    wrong than losing data, and the honest fix is a real YAML parser.
    """
    if v[:1] not in "[{":
        return v, i
    depth = (v.count("[") - v.count("]")) + (v.count("{") - v.count("}"))
    while depth > 0 and i < len(lines):
        nxt = lines[i].strip()
        i += 1
        v += " " + nxt
        depth += (nxt.count("[") - nxt.count("]")) + (nxt.count("{") - nxt.count("}"))
    return v, i


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
                v, i = _quoted_continuation(lines, i, v)
                v, i = _flow_continuation(lines, i, v)
                d[k] = _scalar(v)
            else:
                d[k] = {}
                pending_key = (key_indent, d, k)

        if line.startswith("- "):
            item = line[2:].strip()
            if not isinstance(cur, list):
                continue
            # A flow collection first: `- {id: 1, why: x}` otherwise matches
            # the map-key pattern below on `{id:` and becomes a dict with the
            # brace expression as its key. 4331 lines in the library are
            # written this way (library#39).
            if item[:1] in "[{":
                item, i = _flow_continuation(lines, i, item)
                cur.append(_scalar(item))
            elif re.match(r"^[^\s\"'][^:]*:(\s|$)", item) and not item.startswith(("http:", "https:")):
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
                    # A bare sequence item wraps the same way a key's value
                    # does, and used to truncate the same way — this branch is
                    # how `error_paths: [- "None. §7.1 ...` lost its second
                    # line in rfc-8392's protocol.yaml.
                    item, i = _quoted_continuation(lines, i, item)
                    item, i = _flow_continuation(lines, i, item)
                    cur.append(_scalar(item))
        elif ":" in line:
            k, _, v = line.partition(":")
            if not isinstance(cur, dict):
                continue
            assign(cur, k.strip(), v, indent)
    return root

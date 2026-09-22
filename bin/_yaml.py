"""Minimal nested YAML reader — enough for library records, no dependencies.

Replaces the two-level parser in bin/validate, which silently flattened
`relations: {see_also: [...]}` into a list and made every crosswalk edge
disappear. Handles arbitrary nesting of block maps and block sequences,
which is all these records use.

Not a YAML implementation. No anchors, flow collections, multi-line scalars
or tags — the record schema forbids all of them anyway.
"""


def _scalar(v):
    v = v.strip()
    if len(v) >= 2 and v[0] == v[-1] and v[0] in "\"'":
        return v[1:-1]
    if v == "[]":
        return []
    if v == "{}":
        return {}
    return v


def parse(text):
    root = {}
    # stack of (indent, container); container is dict or list
    stack = [(-1, root)]
    pending_key = None          # (indent, dict, key) awaiting a nested block
    for raw in text.splitlines():
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
            cur = [] if line.startswith("- ") else {}
            d[k] = cur
            stack.append((indent, cur))
            pending_key = None
        elif pending_key:
            pending_key = None

        if line.startswith("- "):
            item = line[2:].strip()
            if not isinstance(cur, list):
                continue
            if ":" in item and not item.startswith(("http", "\"", "'")):
                k, _, v = item.partition(":")
                d = {k.strip(): _scalar(v)}
                cur.append(d)
                # A sequence item that is a map: its remaining keys sit at the
                # indent of this first key, so push the dict so they attach to
                # it rather than being dropped. Without this, every list of
                # multi-key maps silently collapses to its first key.
                stack.append((indent + 2, d))
                if not v:
                    pending_key = (indent + 2, d, k.strip())
            else:
                cur.append(_scalar(item))
        elif ":" in line:
            k, _, v = line.partition(":")
            k, v = k.strip(), v.strip()
            if not isinstance(cur, dict):
                continue
            if v:
                cur[k] = _scalar(v)
            else:
                cur[k] = {}
                pending_key = (indent, cur, k)
    return root

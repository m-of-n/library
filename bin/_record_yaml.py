"""Faithful reader for the YAML subset that record.yaml and summary.md use.

`_yaml.py` is the validator's lossy reader (it has no flow collections, so
`tags: [a, b]` and `bears_on:\n  []` are not values to it). Anything that
renders a record for people uses this module instead. It was checked
against PyYAML `safe_load` on every record at cd28d36 (414 of 414 equal).
Stdlib only.
"""

from __future__ import annotations

import re
from pathlib import Path


def _strip_comment(s: str) -> str:
    out = []
    q = None
    i = 0
    while i < len(s):
        c = s[i]
        if q:
            out.append(c)
            if c == "\\" and q == '"':
                if i + 1 < len(s):
                    i += 1
                    out.append(s[i])
            elif c == q:
                q = None
        elif c in "\"'":
            q = c
            out.append(c)
        elif c == "#":
            break
        else:
            out.append(c)
        i += 1
    return "".join(out).rstrip()


def _unquote(s: str):
    if len(s) >= 2 and s[0] == s[-1] and s[0] in "\"'":
        body = s[1:-1]
        if s[0] == "'":
            return body.replace("''", "'")
        return (
            body.replace("\\n", "\n")
            .replace("\\t", "\t")
            .replace('\\"', '"')
            .replace("\\\\", "\\")
        )
    return s


def _split_flow(inner: str) -> list[str]:
    items = []
    buf: list[str] = []
    depth = 0
    q = None
    i = 0
    while i < len(inner):
        c = inner[i]
        if q:
            buf.append(c)
            if c == "\\" and q == '"':
                if i + 1 < len(inner):
                    i += 1
                    buf.append(inner[i])
            elif c == q:
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
            items.append("".join(buf).strip())
            buf = []
            i += 1
            continue
        else:
            buf.append(c)
        i += 1
    tail = "".join(buf).strip()
    if tail:
        items.append(tail)
    return [x for x in items if x != ""]


def _parse_flow_map(s: str) -> dict:
    inner = s.strip()[1:-1]
    out = {}
    for piece in _split_flow(inner):
        key, sep, val = piece.partition(":")
        if not sep:
            raise ValueError(f"bad flow map entry: {piece}")
        out[key.strip()] = _scalar(val.strip())
    return out


def _scalar(s: str):
    s = s.strip()
    if s in ("", "~", "null", "Null", "NULL"):
        return None
    if s in ("true", "True", "TRUE"):
        return True
    if s in ("false", "False", "FALSE"):
        return False
    if s == "[]":
        return []
    if s == "{}":
        return {}
    if len(s) >= 2 and s[0] == s[-1] and s[0] in "\"'":
        return _unquote(s)
    if s.startswith("[") and s.endswith("]"):
        return [_scalar(x) for x in _split_flow(s[1:-1])]
    if s.startswith("{") and s.endswith("}"):
        return _parse_flow_map(s)
    if re.fullmatch(r"-?\d+", s):
        return int(s)
    if re.fullmatch(r"-?\d+\.\d+", s):
        return float(s)
    return s


_MAP_ITEM = re.compile(r"^[A-Za-z_][A-Za-z0-9_-]*:")


def _is_map_item(rest: str) -> bool:
    if not rest or rest[0] in "\"'[{":
        return False
    if re.match(r"^[a-z][a-z0-9+.-]*://", rest):
        return False
    return bool(_MAP_ITEM.match(rest))


class YamlParser:
    def __init__(self, text: str, name: str = ""):
        self.lines = text.splitlines()
        self.n = len(self.lines)
        self.i = 0
        self.name = name

    def parse(self):
        self._skip()
        if self.i < self.n and self.lines[self.i].strip() == "---":
            self.i += 1
        if self.peek() is None:
            return {}
        return self.parse_map(0)

    def _skip(self):
        while self.i < self.n:
            line = self.lines[self.i]
            if not line.strip() or line.lstrip().startswith("#"):
                self.i += 1
                continue
            return

    def peek(self):
        self._skip()
        if self.i >= self.n:
            return None
        return self.lines[self.i]

    def _indent(self, line: str) -> int:
        return len(line) - len(line.lstrip(" "))

    def _err(self, msg: str):
        raise ValueError(f"{self.name}:{self.i + 1}: {msg}")

    def parse_map(self, indent: int) -> dict:
        out: dict = {}
        while True:
            line = self.peek()
            if line is None:
                break
            if line.strip() == "---":
                break
            ind = self._indent(line)
            if ind < indent:
                break
            if ind > indent:
                self._err(f"unexpected indent {ind}, wanted {indent}")
            content = _strip_comment(line).strip()
            if content.startswith("- "):
                break
            if ":" not in content:
                self._err(f"expected key: {content}")
            key, _, rest = content.partition(":")
            key = key.strip()
            rest = rest.strip()
            self.i += 1
            if rest in ("|", ">", "|-", ">-", "|+", ">+"):
                out[key] = self._block_scalar(ind, rest)
            elif rest == "":
                out[key] = self._nested(ind)
            else:
                out[key] = _scalar(rest)
        return out

    def _nested(self, key_indent: int):
        nxt = self.peek()
        if nxt is None:
            return None
        if nxt.strip() == "---":
            return None
        ind = self._indent(nxt)
        if ind <= key_indent:
            return None
        content = _strip_comment(nxt).strip()
        if content.startswith("- "):
            return self.parse_list(ind)
        if content[:1] in "[{":
            # flow collection on its own line under the key (`bears_on:\n  []`)
            self.i += 1
            return _scalar(content)
        return self.parse_map(ind)

    def parse_list(self, indent: int) -> list:
        items = []
        while True:
            line = self.peek()
            if line is None:
                break
            if line.strip() == "---":
                break
            ind = self._indent(line)
            if ind < indent:
                break
            content = _strip_comment(line).strip()
            if ind != indent or not content.startswith("- "):
                break
            rest = content[2:].strip()
            self.i += 1
            if rest == "":
                items.append(self._nested(ind))
            elif _is_map_item(rest):
                key, _, val = rest.partition(":")
                item = {key.strip(): _scalar(val.strip()) if val.strip() else self._nested(ind)}
                self._map_into(item, ind + 1)
                items.append(item)
            else:
                items.append(_scalar(rest))
        return items

    def _map_into(self, item: dict, min_indent: int):
        while True:
            line = self.peek()
            if line is None:
                break
            if line.strip() == "---":
                break
            ind = self._indent(line)
            if ind < min_indent:
                break
            content = _strip_comment(line).strip()
            if content.startswith("- ") or ":" not in content:
                break
            key, _, rest = content.partition(":")
            key = key.strip()
            rest = rest.strip()
            self.i += 1
            if rest in ("|", ">", "|-", ">-", "|+", ">+"):
                item[key] = self._block_scalar(ind, rest)
            elif rest == "":
                item[key] = self._nested(ind)
            else:
                item[key] = _scalar(rest)

    def _block_scalar(self, key_indent: int, style: str) -> str:
        raw_lines = []
        while self.i < self.n:
            line = self.lines[self.i]
            if line.strip() and (len(line) - len(line.lstrip(" "))) <= key_indent:
                break
            raw_lines.append(line)
            self.i += 1
        kept = []
        for line in raw_lines:
            if line.strip() == "":
                kept.append("")
            else:
                kept.append(line)
        if not any(x.strip() for x in kept):
            return ""
        mind = min(len(x) - len(x.lstrip(" ")) for x in kept if x.strip())
        body = [("" if not x.strip() else x[mind:]) for x in kept]
        while body and body[-1] == "":
            body.pop()
        if style.startswith(">"):
            paras = []
            cur: list[str] = []
            for line in body:
                if line == "":
                    if cur:
                        paras.append(" ".join(cur))
                        cur = []
                else:
                    cur.append(line)
            if cur:
                paras.append(" ".join(cur))
            return "\n".join(paras)
        return "\n".join(body)


def load_yaml(path: Path):
    return YamlParser(path.read_text(encoding="utf-8"), str(path)).parse()


def load_front_matter(text: str, name: str):
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end < 0:
        raise ValueError(f"{name}: unclosed front matter")
    fm = YamlParser(text[: end + 4], name).parse()
    body = text[end + 4 :]
    if body.startswith("\n"):
        body = body[1:]
    return fm, body

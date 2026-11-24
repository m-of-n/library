# DERIVED - not verbatim. Written by this library. Helper imported (by path) by the other
# *.derived.py scripts in this directory and in ../examples: it resolves a requirement id from a
# selector, so no script types an id by hand (hazards.md section 4).
#
# A selector is a dict with `lines` (the requirement's source_lines, exactly) and/or `contains`
# (a substring of its text). resolve() RAISES unless exactly one requirement matches; it returns
# the full id. requirements.yaml is read with BOTH of the library's YAML readers and the two
# trees must agree (hazards.md section 6).
import os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, "..", "..", "..", "..", ".."))
REQ = os.path.join(HERE, "..", "requirements.yaml")
sys.path.insert(0, os.path.join(ROOT, "bin"))
import _yaml, _record_yaml  # noqa: E402
from pathlib import Path  # noqa: E402

_cache = {}


def requirements():
    if "r" not in _cache:
        a = _yaml.parse(open(REQ, encoding="utf-8").read())["requirements"]
        b = _record_yaml.load_yaml(Path(REQ))["requirements"]
        key = lambda r: (r["id"], str(r.get("source_lines", "")), r["text"], r["verb"])
        if [key(r) for r in a] != [key(r) for r in b]:
            raise SystemExit("bin/_yaml.py and bin/_record_yaml.py disagree on requirements.yaml")
        _cache["r"] = a
    return _cache["r"]


def _num(r):
    return int(r["id"].rsplit("R-", 1)[1])


def resolve(lines=None, contains=None, skeleton=True):
    """skeleton=True: only the stable skeleton ids R-0001..R-0067 (the requirements lane appends
    R-0068 onward, some quoting the same words)."""
    hits = [r for r in requirements()
            if (not skeleton or _num(r) <= 67)
            and (lines is None or str(r.get("source_lines", "")) == str(lines))
            and (contains is None or contains in r["text"])]
    if len(hits) != 1:
        raise SystemExit(f"selector lines={lines!r} contains={contains!r} matched {len(hits)} requirements")
    return hits[0]["id"]


def text_of(rid):
    for r in requirements():
        if r["id"] == rid:
            return r["text"]
    raise SystemExit(f"no requirement {rid}")


def lines_of(rid):
    for r in requirements():
        if r["id"] == rid:
            return str(r.get("source_lines", ""))
    raise SystemExit(f"no requirement {rid}")


def required_decl(field_decl):
    """The id of the (google.api.field_behavior) = REQUIRED declaration whose text contains
    field_decl, for example 'X509Certificate certificate = 5'."""
    return resolve(contains=field_decl + " [(google.api.field_behavior) = REQUIRED]")


def descriptor():
    import json
    if "d" not in _cache:
        _cache["d"] = json.load(open(os.path.join(HERE, "protoc-descriptor.derived.json")))
    return _cache["d"]


def messages():
    """{message name: message dict} over the four files (names are unique across them)."""
    out = {}
    for f in descriptor()["files"]:
        for m in f["messages"]:
            assert m["name"] not in out, m["name"]
            out[m["name"]] = dict(m, file=f["name"])
    return out


def required_id(message, field):
    """Id of the REQUIRED declaration of message.field, found by the declaration's line in the
    rendering (protoc's own line table), never by text alone: `int64 log_index = 1` occurs twice."""
    m = messages()[message]
    fl = [x for x in m["fields"] if x["name"] == field]
    assert len(fl) == 1, (message, field)
    return resolve(lines=str(fl[0]["rendering_line"]), contains="(google.api.field_behavior) = REQUIRED")

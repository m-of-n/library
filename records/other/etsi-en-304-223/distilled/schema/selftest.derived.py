#!/usr/bin/env python3
"""Validate every derived schema against its accept/reject cases.

Run with a python that has jsonschema:  <venv>/bin/python -I distilled/schema/selftest.derived.py
Also asserts: schema is valid draft 2020-12, $id matches the name, additionalProperties is false
everywhere, `required` equals the unconditional shall fields of messages.yaml, every property
carries a non-empty x-constrained-by, a shall boolean is const true, required_with and
requires_any_of are rendered as dependentRequired and anyOf, and every shall / should / can
obligation occurs as a verbal form in at least one requirement its field cites (verify pass
2026-11-15: two fields claimed can where the cited text has none, and nothing checked it).
"""
import json
import os
import pathlib
import sys

from jsonschema import Draft202012Validator

HERE = os.path.dirname(os.path.abspath(__file__))
DIST = os.path.dirname(HERE)
REPO = os.path.abspath(os.path.join(DIST, "..", "..", "..", ".."))
sys.path.insert(0, os.path.join(REPO, "bin"))
import _record_yaml  # noqa: E402
import _bcp14  # noqa: E402

MSGS = _record_yaml.load_yaml(pathlib.Path(DIST) / "messages.yaml")["messages"]
REQS = {r["id"]: r for r in _record_yaml.load_yaml(pathlib.Path(DIST) / "requirements.yaml")["requirements"]}
bad = 0
n_acc = n_rej = 0


def forms(rid):
    t = str(REQS[rid]["text"])
    return {_bcp14.canonical(m, "directives") for m in _bcp14.regex("directives").findall(t)}


def walk(s, path, fields):
    global bad
    if s.get("additionalProperties") is not False:
        print("OPEN object", path); bad += 1
    want = sorted(f["name"] for f in fields if f["required"] in (True, "true"))
    if sorted(s["required"]) != want:
        print("required mismatch", path, s["required"], want); bad += 1
    dep = {}
    for f in fields:
        if f.get("required_with"):
            dep.setdefault(f["required_with"], []).append(f["name"])
    if (s.get("dependentRequired") or {}) != dep:
        print("dependentRequired mismatch", path, s.get("dependentRequired"), dep); bad += 1
    for f in fields:
        p = s["properties"][f["name"]]
        if not p.get("x-constrained-by"):
            print("no constrained_by", path, f["name"]); bad += 1
        for rid in f.get("constrained_by") or []:
            if rid not in REQS:
                print("dangling constrained_by", path, f["name"], rid); bad += 1
        if f["obligation"] in ("shall", "should", "can") and not any(
                f["obligation"] in forms(r) for r in f.get("constrained_by") or [] if r in REQS):
            print("obligation not in any cited text", path, f["name"], f["obligation"]); bad += 1
        if (f["type"] == "boolean" and f["obligation"] == "shall") != (p.get("const") is True):
            print("shall boolean without const true (or const on another field)", path, f["name"]); bad += 1
        if f["type"] == "array<object>":
            walk(p["items"], path + "." + f["name"], f["items"])


for m in MSGS:
    s = json.load(open(os.path.join(HERE, m["name"] + ".derived.schema.json")))
    c = json.load(open(os.path.join(DIST, "examples", m["name"] + ".cases.derived.json")))
    Draft202012Validator.check_schema(s)
    if s["$id"] != "urn:library:etsi-en-304-223:" + m["name"]:
        print("bad $id", m["name"]); bad += 1
    walk(s, m["name"], m["fields"])
    want_any = [[x.strip() for x in str(g).split(",")] for g in (m.get("requires_any_of") or [])]
    have_any = [a["required"] for a in s.get("anyOf") or []]
    if have_any != want_any:
        print("anyOf mismatch", m["name"], have_any, want_any); bad += 1
    if not want_any and not any(f["required"] in (True, "true") for f in m["fields"]) \
            and any(f["obligation"] == "shall" for f in m["fields"]):
        print("has shall fields but accepts {}", m["name"]); bad += 1
    v = Draft202012Validator(s)
    if not c["reject"] or not c["accept"]:
        print("no cases", m["name"]); bad += 1
    for k in c["accept"]:
        n_acc += 1
        errs = list(v.iter_errors(k["instance"]))
        if errs:
            print("ACCEPT FAILED", m["name"], k["why"], errs[0].message); bad += 1
    for k in c["reject"]:
        n_rej += 1
        if v.is_valid(k["instance"]):
            print("REJECT FAILED (accepted)", m["name"], k["why"]); bad += 1
print("schemas", len(MSGS), "accept cases", n_acc, "reject cases", n_rej, "failures", bad)
sys.exit(1 if bad else 0)

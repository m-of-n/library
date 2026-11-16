#!/usr/bin/env python3
"""Generate the derived JSON Schemas and their accept/reject cases from messages.yaml.

Run (from anywhere):  python3 -I distilled/schema/generate.derived.py
Writes   distilled/schema/<Name>.derived.schema.json   (draft 2020-12)
         distilled/examples/<Name>.cases.derived.json   (instances the schema must accept / reject)
Check:   <python with jsonschema> -I distilled/schema/selftest.derived.py

Binding rules (hazard: a schema that parses is not a schema that binds):
  - every object is closed (additionalProperties: false), at top level and in array items;
  - `required` lists exactly the fields with obligation shall and no condition;
  - a required array has minItems 1, a string has minLength 1;
  - should / can / inferred / conditional fields are optional properties, annotated with
    x-obligation, x-condition, x-inferred-reason and x-constrained-by (requirement ids);
  - a shall boolean is const true: the record states the act was done, so false is rejected
    (verify pass 2026-11-15: a required boolean had accepted false, binding nothing);
  - required_with F: the field is required whenever F is present (dependentRequired);
  - requires_any_of: a structure covering several conditional cases carries at least one
    (anyOf of required groups), so it does not accept {}.
The source defines no schema; nothing here is normative.
"""
import copy
import json
import os
import pathlib
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DIST = os.path.dirname(HERE)
REPO = os.path.abspath(os.path.join(DIST, "..", "..", "..", ".."))
sys.path.insert(0, os.path.join(REPO, "bin"))
import _record_yaml  # noqa: E402

MSGS = _record_yaml.load_yaml(pathlib.Path(DIST) / "messages.yaml")["messages"]
EX = os.path.join(DIST, "examples")


def truthy(v):
    return v is True or v == "true"


def prop(fd):
    t = fd["type"]
    if t == "string":
        p = {"type": "string", "minLength": 1}
    elif t == "boolean":
        p = {"type": "boolean"}
        if fd["obligation"] == "shall":
            p["const"] = True
    elif t == "date-time":
        p = {"type": "string", "format": "date-time"}
    elif t == "enum":
        p = {"type": "string", "enum": list(fd["values"])}
    elif t == "array<string>":
        p = {"type": "array", "items": {"type": "string", "minLength": 1}}
    elif t == "array<object>":
        p = {"type": "array", "items": obj(fd["items"])}
    else:
        raise SystemExit("unknown type %r in %s" % (t, fd["name"]))
    if t.startswith("array") and truthy(fd["required"]):
        p["minItems"] = 1
    p["description"] = fd["description"]
    p["x-obligation"] = fd["obligation"]
    if fd.get("condition"):
        p["x-condition"] = fd["condition"]
    if fd.get("inferred_reason"):
        p["x-inferred-reason"] = fd["inferred_reason"]
    p["x-constrained-by"] = list(fd["constrained_by"])
    return p


def obj(fields, any_of=None):
    o = {"type": "object",
         "properties": {f["name"]: prop(f) for f in fields},
         "required": [f["name"] for f in fields if truthy(f["required"])],
         "additionalProperties": False}
    dep = {}
    for f in fields:
        if f.get("required_with"):
            dep.setdefault(f["required_with"], []).append(f["name"])
    if dep:
        o["dependentRequired"] = dep
    if any_of:
        o["anyOf"] = [{"required": g} for g in any_of]
    return o


def groups(m):
    """requires_any_of as lists of field names (messages.yaml joins each group with ', ')."""
    return [[x.strip() for x in str(g).split(",")] for g in (m.get("requires_any_of") or [])]


def sample(fd, full):
    t = fd["type"]
    if t == "string":
        return "example"
    if t == "boolean":
        return True
    if t == "date-time":
        return "2026-01-01T00:00:00Z"
    if t == "enum":
        return fd["values"][0]
    if t == "array<string>":
        return ["example"]
    return [inst(fd["items"], full)]


def inst(fields, full):
    return {f["name"]: sample(f, full) for f in fields if full or truthy(f["required"])}


def wrong(fd):
    t = fd["type"]
    if t == "boolean":
        return "yes"
    if t.startswith("array"):
        return "not-an-array"
    if t == "enum":
        return "not-a-listed-value"
    return 42


def cases(m):
    fields = m["fields"]
    byname = {f["name"]: f for f in fields}
    gs = groups(m)
    rej = []
    base = inst(fields, False)
    if gs:
        # the minimal record also carries one case of a multi-case structure
        for n in gs[0]:
            base[n] = sample(byname[n], False)
        i = inst(fields, False)
        rej.append({"why": "no case of the structure is populated (requires_any_of)", "instance": i})
    for f in fields:
        if truthy(f["required"]):
            i = copy.deepcopy(base)
            del i[f["name"]]
            rej.append({"why": "missing required field %s" % f["name"], "instance": i})
    full = inst(fields, True)
    for f in fields:
        if f["type"] == "boolean" and f["obligation"] == "shall":
            i = copy.deepcopy(full)
            i[f["name"]] = False
            rej.append({"why": "%s is false: a shall boolean records that the act was done (const true)" % f["name"],
                        "instance": i})
        if f.get("required_with"):
            i = copy.deepcopy(full)
            del i[f["name"]]
            rej.append({"why": "%s missing while %s is present (dependentRequired)" % (f["name"], f["required_with"]),
                        "instance": i})
        for g in f.get("items") or []:
            assert not (g["type"] == "boolean" and g["obligation"] == "shall") and not g.get("required_with"), \
                "nested shall boolean or required_with: extend cases() (%s.%s)" % (f["name"], g["name"])
    for f in fields:
        i = copy.deepcopy(full)
        i[f["name"]] = wrong(f)
        rej.append({"why": "wrong type or value for %s" % f["name"], "instance": i})
    i = copy.deepcopy(full)
    i["unlisted_field"] = "x"
    rej.append({"why": "additional property (schema is closed)", "instance": i})
    for f in fields:
        if f["type"] == "array<string>" and truthy(f["required"]):
            i = copy.deepcopy(full)
            i[f["name"]] = []
            rej.append({"why": "required array %s is empty" % f["name"], "instance": i})
        if f["type"] == "array<object>":
            for g in f["items"]:
                if truthy(g["required"]):
                    i = copy.deepcopy(full)
                    del i[f["name"]][0][g["name"]]
                    rej.append({"why": "%s[0] misses required %s" % (f["name"], g["name"]), "instance": i})
                    break
    return {"schema": "%s.derived.schema.json" % m["name"],
            "note": "OUR instances, not the source's (the EN has no examples or test vectors). Generated by schema/generate.derived.py.",
            "accept": [{"why": "only the unconditional shall fields" + (" and the first requires_any_of case" if gs else ""),
                        "instance": base},
                       {"why": "every field populated", "instance": full}],
            "reject": rej}


def main():
    os.makedirs(EX, exist_ok=True)
    for m in MSGS:
        s = {"$schema": "https://json-schema.org/draft/2020-12/schema",
             "$id": "urn:library:etsi-en-304-223:%s" % m["name"],
             "title": m["name"],
             "description": "DERIVED from distilled/messages.yaml (%s); the EN defines no schema and no encoding. %s" % (m["locator"], m["description"])}
        s.update(obj(m["fields"], groups(m)))
        with open(os.path.join(HERE, "%s.derived.schema.json" % m["name"]), "w") as fh:
            json.dump(s, fh, indent=2, ensure_ascii=False)
            fh.write("\n")
        with open(os.path.join(EX, "%s.cases.derived.json" % m["name"]), "w") as fh:
            json.dump(cases(m), fh, indent=2, ensure_ascii=False)
            fh.write("\n")
    print("wrote", len(MSGS), "schemas and case files")


main()

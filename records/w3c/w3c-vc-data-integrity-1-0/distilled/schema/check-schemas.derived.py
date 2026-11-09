#!/usr/bin/env python3
"""check-schemas.derived.py -- DERIVED, written by this library. Not part of the source.

    python3 -I check-schemas.derived.py [--jsonschema-path DIR]

1. Validates every *.derived.schema.json in this directory against the JSON Schema
   2020-12 metaschema (Draft202012Validator.check_schema).
2. Runs every case of schema-tests.derived.json: engine "jsonschema" (a target
   "<file>[#anchor]" against an inline instance or an example fixture) or engine
   "xfield" (a cross-field rule X-nn of rules.derived.yaml, implemented below,
   because a JSON Schema cannot state it). Prints EXAMINED beside every count and
   exits 1 if any verdict differs from the expectation.
Needs the `jsonschema` package (4.x) and `referencing`; pass --jsonschema-path if
they are not importable.
"""
import json, pathlib, sys

HERE = pathlib.Path(__file__).resolve().parent
if "--jsonschema-path" in sys.argv:
    sys.path.insert(0, sys.argv[sys.argv.index("--jsonschema-path") + 1])
from jsonschema import Draft202012Validator
from referencing import Registry, Resource
from referencing.jsonschema import DRAFT202012

SCHEMAS = {}
for p in sorted(HERE.glob("*.derived.schema.json")):
    SCHEMAS[p.name.replace(".schema.json", "")] = json.loads(p.read_text())
REG = Registry().with_resources(
    [(s["$id"], Resource.from_contents(s, default_specification=DRAFT202012)) for s in SCHEMAS.values()])
PREFIX = "urn:library:w3c-vc-data-integrity-1-0:"


# ---- cross-field rules ------------------------------------------------------------------------
def x01_previous_proof(doc):
    """X-01: every previousProof value is the id of another proof of the same document."""
    proofs = doc.get("proof")
    if isinstance(proofs, dict):
        proofs = [proofs]
    if not isinstance(proofs, list):
        return False
    for i, pr in enumerate(proofs):
        prev = pr.get("previousProof") if isinstance(pr, dict) else None
        if prev is None:
            continue
        for v in ([prev] if isinstance(prev, str) else prev):
            if not any(j != i and isinstance(q, dict) and q.get("id") == v for j, q in enumerate(proofs)):
                return False
    return True


def _set(v):
    return None if v is None else ({v} if isinstance(v, str) else set(v))


def x02_options_match(case):
    """X-02 (Add Proof steps 3, 4): a non-null options.domain / challenge equals proof.domain / challenge."""
    o, p = case["options"], case["proof"]
    if o.get("domain") is not None and o["domain"] != p.get("domain"):
        return False
    if o.get("challenge") is not None and o["challenge"] != p.get("challenge"):
        return False
    return True


def x03_verify_inputs(case):
    """X-03 (Verify Proof steps 4 to 6): purpose equal; domain sets equal; challenge equal."""
    i, p = case["inputs"], case["proof"]
    if i.get("expectedProofPurpose") is not None and i["expectedProofPurpose"] != p.get("proofPurpose"):
        return False
    if i.get("domain") is not None and _set(i["domain"]) != _set(p.get("domain")):
        return False
    if i.get("challenge") is not None and i["challenge"] != p.get("challenge"):
        return False
    return True


def x04_unique_ids(doc):
    """X-04 (INFERRED): proof ids within one document are distinct, so previousProof matching is unambiguous."""
    proofs = doc["proof"] if isinstance(doc["proof"], list) else [doc["proof"]]
    ids = [q["id"] for q in proofs if isinstance(q, dict) and "id" in q]
    return len(ids) == len(set(ids))


XF = {"X-01": x01_previous_proof, "X-02": x02_options_match, "X-03": x03_verify_inputs, "X-04": x04_unique_ids}


def instances(case):
    if "instance" in case:
        return [case["instance"]]
    ex = case["example"]
    doc = json.loads((HERE.parent / "examples" / ex["file"]).read_text())
    for step in ex.get("path", []):
        doc = doc[step]
    if ex.get("each") and isinstance(doc, list):
        return doc
    return [doc]


def run_case(case):
    if case["engine"] == "xfield":
        arg = case["instance"] if "instance" in case else instances(case)[0]
        return [XF[case["rule"]](arg)]
    file, _, anchor = case["target"].partition("#")
    ref = PREFIX + file + ("#" + anchor if anchor else "")
    v = Draft202012Validator({"$ref": ref}, registry=REG)
    return [v.is_valid(i) for i in instances(case)]


def main():
    bad = 0
    for name, s in SCHEMAS.items():
        Draft202012Validator.check_schema(s)
        assert s["$id"] == PREFIX + name, name
    print(f"METASCHEMA: {len(SCHEMAS)} schemas examined, 0 invalid")
    tests = json.loads((HERE / "schema-tests.derived.json").read_text())
    n = verdicts = 0
    tally = {}
    for case in tests["cases"]:
        n += 1
        got = run_case(case)
        verdicts += len(got)
        accept = all(got)
        want = case["expect"] == "accept"
        key = (case["engine"], case["expect"])
        tally[key] = tally.get(key, 0) + 1
        if accept != want:
            bad += 1
            print("MISMATCH", case["id"], "expected", case["expect"], "got", got)
    print(f"CASES: {n} examined, {verdicts} verdicts, {bad} mismatching")
    for k in sorted(tally):
        print("  ", k[0], k[1], tally[k])
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()

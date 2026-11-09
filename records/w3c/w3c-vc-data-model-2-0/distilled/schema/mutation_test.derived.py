#!/usr/bin/env python3
"""DERIVED, not verbatim. mutation_test -- does the derived schema BIND, or only parse?

    python3 -I mutation_test.derived.py        # needs jsonschema, referencing, cbor2 (see run_checks.derived.py)

For each mutation below it copies this directory to a temporary one, weakens exactly one
constraint of vcdm.derived.schema.json, runs `run_checks.derived.py schema-tests` there and
expects at least one unexpected verdict. A mutation that changes no verdict means a rule the
test cases do not exercise (hazards.md section 7: a schema that parses is not a schema that
binds). Prints EXAMINED (mutations) beside FOUND (mutations NOT detected); exit 1 if any.
"""
import copy, json, os, shutil, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
P = "vcdm.derived.schema.json"


def sub(*path):
    def f(s, v=None):
        pass
    return f


def pop(*path):
    def f(s):
        cur = s["$defs"]
        for k in path[:-1]:
            cur = cur[k]
        cur.pop(path[-1])
    return f


def setv(path, val):
    def f(s):
        cur = s["$defs"]
        for k in path[:-1]:
            cur = cur[k]
        cur[path[-1]] = val
    return f


MUT = {
    "VerifiableCredential: drop required": pop("VerifiableCredential", "required"),
    "dateTimeStamp: pattern .*": setv(("dateTimeStamp", "pattern"), ".*"),
    "languageValueObject: additionalProperties true": setv(("languageValueObject", "additionalProperties"), True),
    "subjectObject: drop anyOf (id-only subject)": pop("subjectObject", "anyOf"),
    "sriHashExpression: pattern .*": setv(("sriHashExpression", "pattern"), ".*"),
    "context: drop prefixItems": lambda s: s["$defs"]["context"]["oneOf"][1].pop("prefixItems"),
    "statusObject: no required": setv(("statusObject", "required"), []),
    "vcOrEnvelopedVC: drop else": pop("vcOrEnvelopedVC", "else"),
    "vcOrEnvelopedVC: drop then": pop("vcOrEnvelopedVC", "then"),
    "EnvelopedVerifiableCredential: id pattern dropped": lambda s: s["$defs"]["EnvelopedVerifiableCredential"]["properties"]["id"].pop("pattern"),
    "VerifiableCredential-should: type minItems dropped": lambda s: s["$defs"]["VerifiableCredential-should"]["properties"]["type"].pop("minItems"),
    "VerifiablePresentation: type need not include VP": lambda s: s["$defs"]["VerifiablePresentation"]["properties"].__setitem__("type", {"$ref": "#typeValue"}),
    "relatedResourceObject: drop anyOf digest": pop("relatedResourceObject", "anyOf"),
    "relatedResourceObject: drop required id": pop("relatedResourceObject", "required"),
    "schemaObject: drop required": pop("schemaObject", "required"),
    "languageValueObject-should: drop @language pattern": lambda s: s["$defs"]["languageValueObject-should"]["properties"]["@language"].pop("pattern"),
    "sriString-should: drop oneOf (sha256 allowed)": pop("sriString-should", "oneOf"),
    "textValue: accept any scalar or array": setv(("textValue", "oneOf"), [{"type": ["string", "array", "number"]}]),
    "typeValue: pattern dropped": lambda s: s["$defs"]["typeValue"]["oneOf"][0].pop("pattern"),
    "url: pattern dropped": pop("url", "pattern"),
    "context-should: drop oneOf (inline @vocab allowed)": pop("context-should", "oneOf"),
}


def main():
    orig = json.load(open(os.path.join(HERE, P), encoding="utf-8"))
    tmp = tempfile.mkdtemp(prefix="mut-")
    work = os.path.join(tmp, "schema")
    shutil.copytree(HERE, work, ignore=shutil.ignore_patterns("__pycache__"))
    os.makedirs(os.path.join(tmp, "examples"))
    for f in os.listdir(os.path.join(os.path.dirname(HERE), "examples")):
        if f.startswith("ex") and f.endswith("-main.json"):
            shutil.copy(os.path.join(os.path.dirname(HERE), "examples", f), os.path.join(tmp, "examples", f))
    def run():
        r = subprocess.run([sys.executable, "-I", "run_checks.derived.py", "schema-tests"], cwd=work, capture_output=True, text=True)
        line = r.stdout.split("\n")[0]
        return r.returncode, line
    rc0, base = run()
    print("baseline:", base)
    missed = 0
    for name, f in MUT.items():
        s = copy.deepcopy(orig)
        f(s)
        json.dump(s, open(os.path.join(work, P), "w", encoding="utf-8"))
        rc, line = run()
        flag = "detected" if rc != 0 else "NOT DETECTED"
        if rc == 0:
            missed += 1
        print("%-60s %s  [%s]" % (name, flag, line.split("FOUND")[-1].strip()))
    shutil.rmtree(tmp)
    print("mutation_test: EXAMINED %d mutations, FOUND %d not detected" % (len(MUT), missed))
    return 1 if missed or rc0 != 0 else 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""DERIVED by the library, not part of the source. Regenerates, from the cached
DSOMM data model, everything this lane writes: schema/*.derived.schema.json,
messages.yaml, examples/*.derived.json and the two README.md files.

    <venv>/bin/python -I distilled/schema/build.derived.py

No published schema binds generated/model.yaml: the publisher's JSON Schemas
(draft-07, src/assets/YAML/schemas/ at the same tag) describe its per-dimension
source files, where implementation items are $ref links, and reject this file,
which inlines them (verify pass, 2026-11-16, checked on two dimensions). Field types and
required-ness are measured from the file (present in N of M) and the build
raises if a measurement disagrees with what the spec below declares.
Needs PyYAML and .cache/owasp-dsomm.txt (never committed).
"""
import collections, json, pathlib, re, sys
import yaml

HERE = pathlib.Path(__file__).resolve().parent
DIST = HERE.parent
REPO = HERE.parents[4]
SRC = REPO / ".cache" / "owasp-dsomm.txt"
REC = "owasp-dsomm"
BAN = "TO" + "DO"          # the placeholder token must never reach an output

UUID_BODY = r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}"
UUID = "^" + UUID_BODY + "$"
ACT_UUID = "^" + UUID_BODY + "(-[a-z]+)?$"
URL = r"^https?://\S+$"

# ---------------------------------------------------------------- load
text = SRC.read_text(encoding="utf-8")
docs = list(yaml.safe_load_all(text))
nodes = list(yaml.compose_all(text))
assert len(docs) == 2 and len(nodes) == 2
meta, model = docs[0]["meta"], docs[1]
mnode, modelnode = nodes[0].value[0][1], nodes[1]

acts, act_nodes, subs, dims = [], [], 0, len(model)
for (dk, dv), (_, dn) in zip(model.items(), modelnode.value):
    for (sk, sv), (_, sn) in zip(dv.items(), dn.value):
        subs += 1
        for (ak, av), (_, an) in zip(sv.items(), sn.value):
            acts.append((dk, sk, ak, av))
            act_nodes.append(an)
N = len(acts)
assert N == 251 and subs == 24 and dims == 6, (N, subs, dims)


def first_lines(nodelist):
    """key -> first source line (1-based) over a list of mapping nodes."""
    out = {}
    for n in nodelist:
        for k, _ in n.value:
            out.setdefault(k.value, k.start_mark.line + 1)
    return out


def tname(v):
    if isinstance(v, bool): return "boolean"
    if isinstance(v, int): return "integer"
    if isinstance(v, float): return "number"
    if isinstance(v, str): return "string"
    if v is None: return "null"
    if isinstance(v, list): return "array"
    if isinstance(v, dict): return "object"
    return type(v).__name__


def census(dicts, nodelist):
    c, t = collections.Counter(), collections.defaultdict(collections.Counter)
    for d in dicts:
        for k, v in d.items():
            c[k] += 1
            t[k][tname(v)] += 1
    return c, t, first_lines(nodelist)


act_c, act_t, act_l = census([a[3] for a in acts], act_nodes)
impl_nodes, impl_dicts = [], []
for (_, _, _, a), an in zip(acts, act_nodes):
    for k, v in an.value:
        if k.value == "implementation" and isinstance(v, yaml.SequenceNode):
            for item, inode in zip(a["implementation"], v.value):
                impl_dicts.append(item); impl_nodes.append(inode)
impl_c, impl_t, impl_l = census(impl_dicts, impl_nodes)
ref_nodes = [v for an in act_nodes for k, v in an.value if k.value == "references"]
ref_c, ref_t, ref_l = census([a[3]["references"] for a in acts], ref_nodes)
dif_nodes = [v for an in act_nodes for k, v in an.value if k.value == "difficultyOfImplementation"]
dif_c, dif_t, dif_l = census([a[3]["difficultyOfImplementation"] for a in acts], dif_nodes)
meta_c = collections.Counter(meta.keys())
meta_l = first_lines([mnode])
IMPL_TOTAL = len(impl_dicts)

# ------------------------------------------------ measured facts (asserted)
assert set(a[3]["uuid"] for a in acts).__len__() == N
assert all(re.match(ACT_UUID, a[3]["uuid"]) for a in acts)
odd_uuid = [a[3]["uuid"] for a in acts if not re.match(UUID, a[3]["uuid"])]
assert len(odd_uuid) == 2
assert all(isinstance(x, str) and re.match(UUID, x) for a in acts for x in a[3].get("dependsOn", []))
assert all(1 <= a[3]["level"] <= 5 and 1 <= a[3]["usefulness"] <= 5 for a in acts)
assert all(1 <= v <= 5 for a in acts for v in a[3]["difficultyOfImplementation"].values())
assert all(re.match(URL, i["url"]) for i in impl_dicts if "url" in i)
assert all(len(set(a[3]["tags"])) == len(a[3]["tags"]) and a[3]["tags"] for a in acts)
assert all(len(set(a[3].get("dependsOn", []))) == len(a[3].get("dependsOn", [])) for a in acts)
assert all(a[3][k].strip() for a in acts for k in ("risk", "measure"))
impl_form = collections.Counter(
    "absent" if "implementation" not in a[3] else
    ("null" if a[3]["implementation"] is None else
     ("empty-string" if a[3]["implementation"] == "" else
      ("empty-list" if a[3]["implementation"] == [] else "non-empty-list")))
    for a in acts)
assert impl_form["empty-string"] == 5 and impl_form["null"] == 4
iso_float = sum(1 for a in acts for k in ("iso27001-2017", "iso27001-2022")
                for v in a[3]["references"].get(k, []) if isinstance(v, float))
impl_uuid_use = collections.Counter(i["uuid"] for i in impl_dicts)
impl_shared = sum(1 for c in impl_uuid_use.values() if c > 1)
cm = collections.Counter("string" if isinstance(a[3].get("comments"), str) else
                         ("null" if "comments" in a[3] else "absent") for a in acts)
cm_empty = sum(1 for a in acts if a[3].get("comments") == "")


def req(counter, key, total):
    """Required in the derived schema iff present in every instance."""
    return counter[key] == total


# ---------------------------------------------------------------- schemas
PUB = "the publisher's own JSON Schemas (draft-07, src/assets/YAML/schemas/ at the same tag) describe its per-dimension source files, where implementation items are $ref links, and reject generated/model.yaml, which inlines them"


def S(**k): return k


def defs():
    impl = S(type="object", additionalProperties=False, required=["uuid", "name"],
             properties={
                 "uuid": S(type="string", pattern=UUID),
                 "name": S(type="string", minLength=1),
                 "tags": S(type="array", items=S(type="string")),
                 "url": S(type="string", pattern=URL),
                 "description": S(type="string"),
                 "test-url-expects": S(type="array", minItems=1, items=S(type="integer")),
             })
    ref_item = S(type=["string", "number"])
    refs = S(type="object", additionalProperties=False,
             required=["samm2", "iso27001-2022", "openCRE"],
             properties={
                 "samm2": S(type="array", items=S(type="string")),
                 "iso27001-2017": S(type="array", items=ref_item),
                 "iso27001-2022": S(type="array", items=ref_item),
                 "openCRE": S(type="array", items=S(type="string", pattern=URL)),
                 "d3f": S(type="array", items=S(type="string")),
             })
    dif = S(type="object", additionalProperties=False,
            required=["knowledge", "time", "resources"],
            properties={k: S(type="integer", minimum=1, maximum=5)
                        for k in ("knowledge", "time", "resources")})
    act = S(type="object", additionalProperties=False,
            required=["uuid", "risk", "measure", "difficultyOfImplementation",
                      "usefulness", "level", "tags", "references"],
            properties={
                "uuid": S(type="string", pattern=ACT_UUID),
                "description": S(type="string"),
                "risk": S(type="string", minLength=1),
                "measure": S(type="string", minLength=1),
                "dependsOn": S(type="array", uniqueItems=True, items=S(type="string", pattern=UUID)),
                "assessment": S(type="string"),
                "difficultyOfImplementation": {"$ref": "#/$defs/Difficulty"},
                "usefulness": S(type="integer", minimum=1, maximum=5),
                "level": S(type="integer", minimum=1, maximum=5),
                "tags": S(type="array", minItems=1, uniqueItems=True, items=S(type="string")),
                "implementation": S(anyOf=[
                    S(type="array", items={"$ref": "#/$defs/Implementation"}),
                    S(type="null"), S(type="string", maxLength=0)]),
                "references": {"$ref": "#/$defs/References"},
                "comments": S(type=["string", "null"]),
                "comment": S(type="string"),
                "credits": S(type="string"),
            })
    return {"Implementation": impl, "References": refs, "Difficulty": dif, "Activity": act}


def head(name, title, desc):
    return {"$schema": "https://json-schema.org/draft/2020-12/schema",
            "$id": f"urn:library:{REC}:{name}.derived",
            "title": title + " - DERIVED",
            "description": "DERIVED by the library from the file's contents; no published schema binds "
                           "generated/model.yaml (" + PUB + "). " + desc}


def build_schemas():
    D = defs()
    out = {}
    s = head("envelope", "DSOMM model.yaml first document (meta)",
             f"Measured over the one meta mapping: version, released, publisher present in {meta_c['version']} of 1.")
    s.update(type="object", additionalProperties=False, required=["meta"], properties={"meta": {
        "type": "object", "additionalProperties": False, "required": ["version", "released", "publisher"],
        "properties": {"version": S(type="string", pattern=r"^\d+\.\d+\.\d+$"),
                       "released": S(type="string", pattern=r"^\d{4}-\d{2}-\d{2}$"),
                       "publisher": S(type="string", pattern=URL)}}})
    out["envelope"] = s
    s = head("implementation", "DSOMM Implementation (item of an activity's implementation list)",
             f"Measured over {IMPL_TOTAL} implementation items.")
    body = D["Implementation"]
    s.update(body)
    out["implementation"] = s
    s = head("activity", "DSOMM Activity",
             f"Measured over {N} activities; required means present in all {N}.")
    body = dict(D["Activity"]); body["$defs"] = {k: D[k] for k in ("Implementation", "References", "Difficulty")}
    s.update(body)
    out["activity"] = s
    sub_def = S(type="object", minProperties=1, additionalProperties={"$ref": "#/$defs/Activity"})
    s = head("sub-dimension", "DSOMM sub-dimension (mapping of activity name to Activity)",
             f"Measured over {subs} sub-dimensions; a sub-dimension has no fields of its own, only activity-name keys.")
    s.update(sub_def); s["$defs"] = dict(D)
    out["sub-dimension"] = s
    s = head("dimension", "DSOMM dimension (mapping of sub-dimension name to sub-dimension)",
             f"Measured over {dims} dimensions; a dimension has no fields of its own, only sub-dimension-name keys.")
    s.update(type="object", minProperties=1, additionalProperties={"$ref": "#/$defs/SubDimension"})
    s["$defs"] = dict(D); s["$defs"]["SubDimension"] = sub_def
    out["dimension"] = s
    return out


# ---------------------------------------------------------------- cases
FAKE = lambda n: f"00000000-0000-4000-8000-{n:012d}"


def base_act():
    return {"uuid": FAKE(1), "risk": "r", "measure": "m",
            "difficultyOfImplementation": {"knowledge": 1, "time": 2, "resources": 3},
            "usefulness": 3, "level": 2, "tags": ["t"],
            "references": {"samm2": ["X-Y-A-1"], "iso27001-2022": [5.1, "note"], "openCRE": ["https://example.org/x"]}}


def mut(f):
    a = base_act(); f(a); return a


def cases():
    full = base_act()
    full.update(description="d", assessment="a", dependsOn=[FAKE(2)], comments="c", comment="c2", credits="cr",
                implementation=[{"uuid": FAKE(3), "name": "n", "tags": ["x"], "url": "https://example.org/i",
                                 "description": "d", "test-url-expects": [403]}])
    full["references"].update({"iso27001-2017": ["A.1", 5.2], "d3f": ["Name"]})
    L = []

    def add(n, schema, expect, why, inst): L.append((n, schema, expect, why, inst))
    add("activity-accept-minimal", "activity", "accept", "the eight keys present in every activity", base_act())
    add("activity-accept-all-keys", "activity", "accept", "every key the file uses, once", full)
    add("activity-accept-suffixed-uuid", "activity", "accept", "uuid with a lowercase word suffix (2 of 251 in the file)",
        mut(lambda a: a.update(uuid=FAKE(1) + "-medium")))
    add("activity-accept-null-comments", "activity", "accept", "comments null (3 of 251)", mut(lambda a: a.update(comments=None)))
    add("activity-accept-impl-null", "activity", "accept", "implementation null (4 of 251)", mut(lambda a: a.update(implementation=None)))
    add("activity-accept-impl-empty-string", "activity", "accept", "implementation empty string (5 of 251)",
        mut(lambda a: a.update(implementation="")))
    add("activity-accept-impl-empty-list", "activity", "accept", "implementation empty list (60 of 251)",
        mut(lambda a: a.update(implementation=[])))
    add("activity-accept-empty-dependsOn", "activity", "accept", "dependsOn empty list (8 of 251)", mut(lambda a: a.update(dependsOn=[])))
    add("activity-accept-empty-samm2", "activity", "accept", "an empty reference list (samm2 empty in 5 of 251)",
        mut(lambda a: a["references"].update(samm2=[])))
    for k in ("uuid", "risk", "measure", "difficultyOfImplementation", "usefulness", "level", "tags", "references"):
        add(f"activity-reject-missing-{k}", "activity", "reject", f"required key {k} absent", mut(lambda a, k=k: a.pop(k)))
    add("activity-reject-level-0", "activity", "reject", "level below 1", mut(lambda a: a.update(level=0)))
    add("activity-reject-level-6", "activity", "reject", "level above 5", mut(lambda a: a.update(level=6)))
    add("activity-reject-level-string", "activity", "reject", "level as a string", mut(lambda a: a.update(level="3")))
    add("activity-reject-level-fraction", "activity", "reject", "level not an integer", mut(lambda a: a.update(level=2.5)))
    add("activity-reject-usefulness-6", "activity", "reject", "usefulness above 5", mut(lambda a: a.update(usefulness=6)))
    add("activity-reject-unknown-key", "activity", "reject", "a key the file never uses", mut(lambda a: a.update(severity=1)))
    add("activity-reject-uuid-not-uuid", "activity", "reject", "uuid is not a uuid", mut(lambda a: a.update(uuid="not-a-uuid")))
    add("activity-reject-uuid-uppercase", "activity", "reject", "uuid in upper case", mut(lambda a: a.update(uuid="ABCDEF00-0000-4000-8000-000000000001")))
    add("activity-reject-dependsOn-not-uuid", "activity", "reject", "dependsOn entry is an activity name, not a uuid",
        mut(lambda a: a.update(dependsOn=["Some activity name"])))
    add("activity-reject-dependsOn-suffixed", "activity", "reject", "dependsOn entry with a uuid suffix (only the activity uuid may carry one)",
        mut(lambda a: a.update(dependsOn=[FAKE(2) + "-medium"])))
    add("activity-reject-dependsOn-scalar", "activity", "reject", "dependsOn as a string", mut(lambda a: a.update(dependsOn=FAKE(2))))
    add("activity-reject-dependsOn-duplicate", "activity", "reject", "dependsOn repeats an entry",
        mut(lambda a: a.update(dependsOn=[FAKE(2), FAKE(2)])))
    add("activity-reject-difficulty-missing-time", "activity", "reject", "difficultyOfImplementation lacks time",
        mut(lambda a: a["difficultyOfImplementation"].pop("time")))
    add("activity-reject-difficulty-extra", "activity", "reject", "difficultyOfImplementation with a fourth key",
        mut(lambda a: a["difficultyOfImplementation"].update(cost=1)))
    add("activity-reject-difficulty-0", "activity", "reject", "difficulty value 0", mut(lambda a: a["difficultyOfImplementation"].update(time=0)))
    add("activity-reject-tags-empty", "activity", "reject", "tags empty", mut(lambda a: a.update(tags=[])))
    add("activity-reject-tags-nonstring", "activity", "reject", "tag not a string", mut(lambda a: a.update(tags=[1])))
    add("activity-reject-references-unknown", "activity", "reject", "unknown reference scheme",
        mut(lambda a: a["references"].update(nist=["x"])))
    add("activity-reject-references-missing-openCRE", "activity", "reject", "references lacks openCRE",
        mut(lambda a: a["references"].pop("openCRE")))
    add("activity-reject-references-missing-samm2", "activity", "reject", "references lacks samm2",
        mut(lambda a: a["references"].pop("samm2")))
    add("activity-reject-references-bool", "activity", "reject", "a boolean inside an ISO list",
        mut(lambda a: a["references"].update({"iso27001-2022": [True]})))
    add("activity-reject-impl-unknown-key", "activity", "reject", "implementation item with an unknown key (the $ref binds)",
        mut(lambda a: a.update(implementation=[{"uuid": FAKE(3), "name": "n", "extra": 1}])))
    add("activity-reject-impl-missing-name", "activity", "reject", "implementation item without name",
        mut(lambda a: a.update(implementation=[{"uuid": FAKE(3)}])))
    add("activity-reject-impl-number", "activity", "reject", "implementation as a number", mut(lambda a: a.update(implementation=3)))
    add("activity-reject-impl-nonempty-string", "activity", "reject", "implementation as a non-empty string",
        mut(lambda a: a.update(implementation="x")))
    add("activity-reject-comments-number", "activity", "reject", "comments as a number", mut(lambda a: a.update(comments=3)))
    add("implementation-accept-minimal", "implementation", "accept", "uuid and name only (Arachni-like: no tags)",
        {"uuid": FAKE(3), "name": "n"})
    add("implementation-accept-full", "implementation", "accept", "every key the file uses",
        {"uuid": FAKE(3), "name": "n", "tags": [], "url": "https://example.org/i", "description": "d", "test-url-expects": [308]})
    add("implementation-reject-missing-uuid", "implementation", "reject", "uuid absent", {"name": "n"})
    add("implementation-reject-missing-name", "implementation", "reject", "name absent", {"uuid": FAKE(3)})
    add("implementation-reject-unknown-key", "implementation", "reject", "unknown key", {"uuid": FAKE(3), "name": "n", "x": 1})
    add("implementation-reject-uuid-suffixed", "implementation", "reject", "suffixed uuid (only activities carry one)",
        {"uuid": FAKE(3) + "-medium", "name": "n"})
    add("implementation-reject-url-not-url", "implementation", "reject", "url that is not http(s)", {"uuid": FAKE(3), "name": "n", "url": "ftp:x"})
    add("implementation-reject-expects-string", "implementation", "reject", "test-url-expects holds a string",
        {"uuid": FAKE(3), "name": "n", "test-url-expects": ["403"]})
    ok = {"meta": {"version": "5.0.2", "released": "2026-01-02", "publisher": "https://example.org/p"}}
    add("envelope-accept", "envelope", "accept", "the three meta keys", ok)
    for k in ("version", "released", "publisher"):
        add(f"envelope-reject-missing-{k}", "envelope", "reject", f"meta lacks {k}",
            {"meta": {a: b for a, b in ok["meta"].items() if a != k}})
    add("envelope-reject-unknown-key", "envelope", "reject", "meta with a fourth key", {"meta": dict(ok["meta"], tag="v1")})
    add("envelope-reject-version-shape", "envelope", "reject", "version not x.y.z", {"meta": dict(ok["meta"], version="5.0")})
    add("envelope-reject-no-meta", "envelope", "reject", "document without meta", {})
    add("sub-dimension-accept", "sub-dimension", "accept", "one activity under its name", {"An activity": base_act()})
    add("sub-dimension-reject-empty", "sub-dimension", "reject", "a sub-dimension with no activity", {})
    add("sub-dimension-reject-activity-unknown-key", "sub-dimension", "reject", "the Activity $ref binds inside a sub-dimension",
        {"An activity": mut(lambda a: a.update(x=1))})
    add("sub-dimension-reject-not-mapping", "sub-dimension", "reject", "an activity that is a list", {"An activity": []})
    add("dimension-accept", "dimension", "accept", "one sub-dimension with one activity", {"Sub": {"An activity": base_act()}})
    add("dimension-reject-empty", "dimension", "reject", "a dimension with no sub-dimension", {})
    add("dimension-reject-deep-level", "dimension", "reject", "level 9 two levels down",
        {"Sub": {"An activity": mut(lambda a: a.update(level=9))}})
    add("dimension-reject-activity-directly", "dimension", "reject", "an activity placed where a sub-dimension belongs",
        {"An activity": base_act()})
    return L


# ---------------------------------------------------------------- messages.yaml
def q(s): return json.dumps(s, ensure_ascii=False)


REASON = "derived from the file's structure, not a stated requirement"
REASON_CB = ("type and required derived from the file's structure; constrained_by lists the requirements.yaml "
             "entries (kind: inferred, no stated requirement) that say how the field is read")

# Verify pass (2026-11-16): requirements.yaml carries kind: inferred entries about how a field of every
# activity is read (locator "model: every activity / <field>", field "<field>[, <field>]"). Those are
# the requirements that constrain the activity fields, so each is wired here, by script, from that file.
FIELD_REQS = collections.defaultdict(list)
FIELD_REQ_IDS = set()
for _r in yaml.safe_load((DIST / "requirements.yaml").read_text(encoding="utf-8"))["requirements"]:
    if str(_r.get("locator", "")).startswith("model: every activity / "):
        assert _r.get("kind") == "inferred", _r["id"]
        FIELD_REQ_IDS.add(_r["id"])
        for _f in str(_r["field"]).split(","):
            FIELD_REQS[_f.strip()].append(_r["id"])
CB_LINKS = sum(len(v) for v in FIELD_REQS.values())
TYPES = {"uuid": "string (uuid)", "risk": "string (block scalar)", "measure": "string (block scalar)"}


def field_lines(name, jtype, counter, total, firstline, doc, required_override=None, types=None, cb=()):
    n = counter[name]
    req_ = n == total
    out = [f"      - name: {q(name)}", f"        type: {q(jtype)}",
           f"        required: {'true' if req_ else 'false'}",
           f"        present_in: {q(f'{n} of {total}')}",
           f"        first_seen_line: {firstline[name]}"]
    if types and len(types[name]) > 1:
        out.append(f"        observed_types: {q(', '.join(f'{k} {v}' for k, v in sorted(types[name].items())))}")
    out += [f"        note: {q(doc)}"]
    out += (["        constrained_by:"] + [f"          - {q(x)}" for x in cb] + [f"        inferred_reason: {q(REASON_CB)}"]
            if cb else ["        constrained_by: []", f"        inferred_reason: {q(REASON)}"])
    return out


A_DOC = {
    "uuid": "Stable activity id. Canonical lower-case uuid in 249; two carry a trailing -medium or -advanced suffix (so not a uuid).",
    "description": "Prose; present in 122; an empty string in 2.",
    "risk": "Prose, always present.", "measure": "Prose, always present; one activity's measure holds a placeholder instead of text (source defect, see design notes).",
    "dependsOn": ("List of activity uuids; every entry resolves to another activity in the file; empty list in 8. The schema takes "
                  "the observed form of an entry, a canonical uuid, so an entry naming one of the two activities whose id carries "
                  "a suffix would be rejected, although R-0704 reads an entry as the target's id value."),
    "assessment": "Prose; present in 78.",
    "difficultyOfImplementation": "Mapping knowledge/time/resources, each an integer 1-5.",
    "usefulness": "Integer 1-5.", "level": "Integer 1-5 (maturity level).",
    "tags": "Non-empty list of strings, no duplicates within an activity; 49 distinct tags in the file.",
    "implementation": "List of Implementation, or null, or empty string - three forms for 'nothing' alongside the empty list.",
    "references": "Mapping from reference scheme to list.",
    "comments": "String (empty string in most), or null in 3.", "comment": "Singular key, 1 activity: probable typo of comments, kept as the file has it.",
    "credits": "String, 3 activities.",
}
A_TYPE = {"uuid": "string", "description": "string", "risk": "string", "measure": "string", "dependsOn": "array<uuid>",
          "assessment": "string", "difficultyOfImplementation": "object<Difficulty>", "usefulness": "integer 1..5",
          "level": "integer 1..5", "tags": "array<string>", "implementation": "array<Implementation> | null | empty string",
          "references": "object<References>", "comments": "string | null", "comment": "string", "credits": "string"}
A_ORDER = ["uuid", "description", "risk", "measure", "dependsOn", "assessment", "difficultyOfImplementation",
           "usefulness", "level", "tags", "implementation", "references", "comments", "comment", "credits"]
assert set(A_ORDER) == set(act_c), set(act_c) ^ set(A_ORDER)
assert set(FIELD_REQS) <= set(A_ORDER), set(FIELD_REQS) - set(A_ORDER)


NOTE_TEXT = ("DSOMM defines no wire protocol: the source IS a YAML data model (generated/model.yaml), so its messages are the "
             "structures that file is built from. No published schema binds it (" + PUB + "), and the file states no field types or required-ness. "
             "Every type and required flag below is DERIVED by script (distilled/schema/build.derived.py) from what the file contains: "
             f"required means present in all instances ({N} activities, {IMPL_TOTAL} implementation items, 1 meta mapping); present_in gives "
             "the measured count. No stated requirement constrains a "
             "structural field; the activity-level requirement entries are about what an activity says, not about the shape of the file. "
             f"How a field of every activity is read is stated by {len(FIELD_REQ_IDS)} kind: inferred entries of requirements.yaml "
             f"(locator model: every activity), so {len(FIELD_REQS)} activity fields are constrained_by them ({CB_LINKS} links, "
             "wired by script from requirements.yaml by the verify pass); every other field has constrained_by empty and an inferred_reason. "
             "Derived JSON Schemas are in schema/.")


def messages_yaml():
    L = ["schema: \"library-messages/v1\"", f"record: {REC}", 'reviewed_by: ""',
         "note: " + q(NOTE_TEXT),
         "messages:"]

    def msg(name, loc, lines, enc, layout, fields, notes):
        L.extend([f"  - name: {q(name)}", f"    locator: {q(loc)}", f"    source_lines: {q(lines)}",
                  f"    encoding: {q(enc)}", f"    layout: {q(layout)}", "    fields:" if fields else "    fields: []"])
        L.extend(fields)
        L.append(f"    notes: {q(notes)}")

    msg("file-envelope", "first YAML document of the file", f"{meta_l['version'] - 1}-{meta_l['publisher']}",
        "YAML block mapping; the file holds two documents separated by a document-start line",
        "document 1: one key, meta, a mapping; document 2: the model (dimensions)",
        ["      - name: \"meta\"", "        type: \"object<meta>\"", "        required: true",
         "        present_in: \"1 of 1\"", f"        first_seen_line: {meta_l['version'] - 1}",
         "        note: \"The only top-level key of document 1.\"", "        constrained_by: []",
         f"        inferred_reason: {q(REASON)}"]
        + [l for k, t in (("version", "string (x.y.z)"), ("released", "string (YYYY-MM-DD, quoted in the file)"),
                          ("publisher", "string (url)")) for l in
           field_lines(k, t, meta_c, 1, meta_l, f"meta.{k}")],
        "meta.version reads 5.0.2 in this file. Schema: envelope.derived.schema.json.")
    msg("dimension", "top-level keys of document 2", f"{min(l for l in [modelnode.value[0][0].start_mark.line + 1])}",
        "YAML block mapping", "dimension name -> mapping of sub-dimension name -> sub-dimension",
        [], f"{dims} dimensions; a dimension has no field of its own, its name is the key. Schema: dimension.derived.schema.json.")
    msg("sub-dimension", "second level of document 2", f"{modelnode.value[0][1].value[0][0].start_mark.line + 1}",
        "YAML block mapping", "sub-dimension name -> mapping of activity name -> activity",
        [], f"{subs} sub-dimensions over {dims} dimensions ({', '.join(str(len(v)) for v in model.values())} per dimension, in file order); activity names are unique in the file ({N}). Schema: sub-dimension.derived.schema.json.")
    msg("activity", "third level of document 2", f"{act_nodes[0].start_mark.line + 1}",
        "YAML block mapping", f"activity name -> mapping of the fields below; {N} activities",
        [l for k in A_ORDER for l in field_lines(k, A_TYPE[k], act_c, N, act_l, A_DOC[k], types=act_t, cb=FIELD_REQS.get(k, ()))],
        "Never-present keys are rejected by the schema. Uniqueness of uuid and resolution of every dependsOn entry are checked by check.derived.py, not by the JSON Schema. Schema: activity.derived.schema.json.")
    msg("difficulty-of-implementation", "activity.difficultyOfImplementation", f"{dif_l['knowledge']}",
        "YAML block mapping", "knowledge, time, resources",
        [l for k in ("knowledge", "time", "resources") for l in field_lines(k, "integer 1..5", dif_c, N, dif_l, "Rating 1-5.")],
        "All three keys in all activities.")
    msg("references", "activity.references", f"{ref_l['samm2']}", "YAML block mapping", "scheme -> list",
        [l for k, t, d in (("samm2", "array<string>", "SAMM2 ids; empty in 5."),
                           ("iso27001-2017", "array<string | number>", "Clause ids or free-text notes."),
                           ("iso27001-2022", "array<string | number>", "Clause ids or free-text notes."),
                           ("openCRE", "array<string (url)>", "OpenCRE link."),
                           ("d3f", "array<string>", "Present in 12 activities.")) for l in
         field_lines(k, t, ref_c, N, ref_l, d, types=ref_t)],
        f"ISO clause ids written without quotes are read as YAML floats ({iso_float} items), so a trailing zero cannot survive and the type is string-or-number.")
    msg("implementation", "activity.implementation[n]", f"{impl_l['uuid']}", "YAML block mapping", "list item of an activity's implementation",
        [l for k, t, d in (("uuid", "string (uuid)", "Always a canonical uuid."), ("name", "string", "Always present."),
                           ("tags", "array<string>", "Absent in one item; empty list in many."),
                           ("url", "string (https url)", "Absent in some items."), ("description", "string", "Optional."),
                           ("test-url-expects", "array<integer>", "One integer in each of its items; meaning not stated in the file.")) for l in
         field_lines(k, t, impl_c, IMPL_TOTAL, impl_l, d)],
        f"{IMPL_TOTAL} items, {len(impl_uuid_use)} distinct uuids ({impl_shared} reused by several activities, identical content each time). Schema: implementation.derived.schema.json.")
    return "\n".join(L) + "\n"


# ---------------------------------------------------------------- verbatim examples
# Verify pass (2026-11-16). The source's code examples are fenced code blocks inside three activity
# descriptions (bin/fx1-skeleton's YAML profile finds no code blocks, so pass 1 missed them). Each is
# cut from the DECODED value of its scalar (escapes resolved, block indentation and the fence's own
# indentation removed); check.derived.py re-cuts them and compares byte for byte.
FENCE = re.compile(r"^([ \t]*)```([\w-]*)[ \t]*\n(.*?)^\1```[ \t]*$", re.S | re.M)
EXT = {"markdown": "md", "bash": "sh", "html": "html"}
EXPECT = {
    "md": "None as a vector: an instruction-file fragment mapping two workflow steps to the file the assistant opens "
          "when that step begins, as the surrounding description explains.",
    "sh": "Run with a JSON object on stdin: a prompt beginning /speckit.plan, /speckit.implement or /speckit.review "
          "prints one JSON object, hookSpecificOutput with hookEventName UserPromptSubmit and additionalContext set to "
          "the content of specs/threat-model.md, docs/secure-coding-rules.md or docs/security-review-checklist.md; "
          "any other prompt prints nothing and exits 0. check.derived.py runs all four cases (bash, jq).",
    "html": "No encoded output is given. The expectation is R-0146: the one template variable sits in four contexts (element "
            "content, a double-quoted attribute, a single-quoted script string, a script comment) and each needs its "
            "own encoding.",
}


def fenced_examples():
    """[(name, path, lines, lang, content)] in source order."""
    out = []

    def walk(n, path):
        if isinstance(n, yaml.MappingNode):
            for k, v in n.value:
                walk(v, path + [str(k.value)])
        elif isinstance(n, yaml.SequenceNode):
            for i, v in enumerate(n.value, 1):
                walk(v, path + [f"[{i}]"])
        elif isinstance(n, yaml.ScalarNode) and "```" in n.value:
            ms = list(FENCE.finditer(n.value))
            assert len(ms) * 2 == n.value.count("```"), path
            src_lines = text.split("\n")
            fl = [i + 1 for i in range(n.start_mark.line, n.end_mark.line + 1) if "```" in src_lines[i]]
            for j, m in enumerate(ms):
                ind, lang, body = m.group(1), m.group(2), m.group(3)
                rows = body.split("\n")[:-1]
                assert all(r.startswith(ind) or not r.strip() for r in rows), path
                content = "\n".join(r[len(ind):] for r in rows) + "\n"
                lines = f"{fl[2 * j]}-{fl[2 * j + 1]}"
                out.append((path, lines, lang, content))
    for d in nodes:
        walk(d, [])
    return [(f"ex-{i:02d}.verbatim.{EXT[lang]}", path, lines, lang, content)
            for i, (path, lines, lang, content) in enumerate(out, 1)]


EXAMPLES = fenced_examples()
assert len(EXAMPLES) == 3, len(EXAMPLES)


# ---------------------------------------------------------------- READMEs
def readme_schema():
    return f"""---
record: {REC}
kind: schema
title: "{REC} - schemas"
extracted: "2026-11-15"
reviewed_by: ""
---

# schema/ - DERIVED, generated by script

No published schema binds the source of record, `generated/model.yaml`. The publisher's JSON Schemas (draft-07, 7 files
under `src/assets/YAML/schemas/` of the data repository at the same tag: one per dimension and one for the implementations catalogue)
describe its per-dimension source files, in which an activity's implementation items are `$ref` links; `generated/model.yaml`
inlines those items and fails them (the verify pass, 2026-11-16, ran two of them over their dimensions of the cached file: every
inlined implementation item is rejected). The library does not hold them; pinning them as a second source is open. Every file
here is **derived** from what `generated/model.yaml` contains; nothing is copied from the publisher.

| file | validates |
|---|---|
| `envelope.derived.schema.json` | document 1 (meta) |
| `dimension.derived.schema.json` | one dimension (carries SubDimension and Activity in `$defs`) |
| `sub-dimension.derived.schema.json` | one sub-dimension |
| `activity.derived.schema.json` | one activity |
| `implementation.derived.schema.json` | one implementation item |
| `build.derived.py` | regenerates the schemas, `../messages.yaml`, `../examples/` |
| `check.derived.py` | validates the source and the accept/reject cases; prints how many it examined |

Method: required means present in every instance ({N} activities, {IMPL_TOTAL} implementation items). Types are the
observed YAML types. Ranges (1-5) are the observed range of the integer fields, not a stated rule. `additionalProperties`
is false everywhere, so a key the file does not use is rejected.

Source irregularities the schemas admit because the file contains them: two activity uuids carry a suffix
(`-medium`, `-advanced`) and are not uuids; `implementation` takes four forms for nothing (absent, null, empty string,
empty list); `comments` is null in 3; ISO clause ids are YAML floats in {iso_float} items; one activity has `comment` and
three have `credits`.
"""


def readme_examples(n_acc, n_rej):
    return f"""---
record: {REC}
kind: examples
title: "{REC} - examples and test vectors"
extracted: "2026-11-15"
reviewed_by: ""
---

# examples/

**Finding: the source's code examples are {len(EXAMPLES)} fenced code blocks inside activity descriptions, and it has no
test vectors.** Its prose samples (the Sample steps and Sample concept lists, the e.g. lists) are text, carried where they stand by
`../requirements.yaml`, `../inferred-candidates.yaml` and `../normative.md`. Each code block is held here verbatim, cut by `schema/build.derived.py` from the decoded value of its YAML scalar
(the fence's indentation removed) and re-cut and compared byte for byte by `schema/check.derived.py`. The verify pass
(2026-11-16) added them: pass 1 recorded that the source had no examples at all.

| file | where (key path) | fence lines | expected result |
|---|---|---|---|
""" + "".join(f"| `{n}` | {' / '.join(p)} | L{ln} | {EXPECT[EXT[lang]]} |\n" for n, p, ln, lang, _ in EXAMPLES) + f"""
Beyond these, the file is itself a set of {N} real instances (and {IMPL_TOTAL} implementation items): those are the
fixtures for the schemas, and copying them here would put a second copy of the source's content in the repository.
`schema/check.derived.py` reads them from the pinned source and validates every one against
`../schema/activity.derived.schema.json`.

What else is held here is ours, marked `.derived.`: {n_acc} instances the schemas must accept and {n_rej} they must reject (missing
uuid, level outside 1-5, unknown key, dependsOn not a uuid, and others). Each file is
`{{schema, expect, why, instance}}`. All identifiers in them are made up.
"""


# ---------------------------------------------------------------- write
def write(path, content):
    assert BAN not in content, path
    path.write_text(content, encoding="utf-8")


def main():
    sch = build_schemas()
    for name, s in sch.items():
        write(HERE / f"{name}.derived.schema.json", json.dumps(s, indent=2, ensure_ascii=False) + "\n")
    ex = DIST / "examples"
    for f in ex.glob("*.derived.json"):
        f.unlink()
    cs = cases()
    for n, schema, expect, why, inst in cs:
        write(ex / f"{n}.derived.json", json.dumps(
            {"derived": True, "schema": f"{schema}.derived.schema.json", "expect": expect, "why": why, "instance": inst},
            indent=2, ensure_ascii=False) + "\n")
    n_acc = sum(1 for c in cs if c[2] == "accept")
    for n, _, _, _, content in EXAMPLES:
        write(ex / n, content)
    write(ex / "README.md", readme_examples(n_acc, len(cs) - n_acc))
    write(HERE / "README.md", readme_schema())
    write(DIST / "messages.yaml", messages_yaml())
    print(f"wrote {len(sch)} schemas, {len(cs)} cases ({n_acc} accept), {len(EXAMPLES)} verbatim examples, messages.yaml")


if __name__ == "__main__":
    main()

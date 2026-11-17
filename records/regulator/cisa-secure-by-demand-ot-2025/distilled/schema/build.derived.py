#!/usr/bin/env python3
"""DERIVED by the library, not part of the source. Regenerates what this lane
writes for cisa-secure-by-demand-ot-2025: schema/*.derived.schema.json,
messages.yaml, examples/*.derived.json and both README.md files. Every
constrained_by id is selected from requirements.yaml by script, raising on
zero matches (and on more than one where one is expected).

    <venv>/bin/python -I distilled/schema/build.derived.py

Needs PyYAML, .cache/cisa-secure-by-demand-ot-2025.txt and bin/_source_text.py.
Re-run it whenever requirements.yaml changes: ids are not typed anywhere.
"""
import collections, json, pathlib, re, sys
import yaml

HERE = pathlib.Path(__file__).resolve().parent
DIST = HERE.parent
REPO = HERE.parents[4]
sys.path.insert(0, str(REPO / "bin"))
import _source_text as st  # noqa: E402

REC = "cisa-secure-by-demand-ot-2025"
BAN = "TO" + "DO"
SRC = REPO / ".cache" / f"{REC}.txt"
REQ = yaml.safe_load((DIST / "requirements.yaml").read_text(encoding="utf-8"))["requirements"]
IDRE = r"^" + REC + r"#R-\d{4}$"

NAMES = ["Configuration Management", "Logging in the Baseline Product", "Open Standards", "Ownership",
         "Protection of Data", "Secure by Default", "Secure Communications", "Secure Controls",
         "Strong Authentication", "Threat Modeling", "Vulnerability Management", "Upgrade and Patch Tooling"]
cleaned = st.clean_for(st.read_lines(SRC), "pdf")
LINES = {i: t for i, t in cleaned if t is not None}


# ------------------------------------------------------------ source sections
def sections():
    """name -> dict of line ranges for the guide's per-consideration template."""
    nums = sorted(LINES)
    heads = []
    for k, i in enumerate(nums):
        if LINES[i].strip() in NAMES and i > 290:
            nxt = next((j for j in nums[k + 1:] if LINES[j].strip()), None)
            if nxt and LINES[nxt].strip().startswith("Selection criteria:"):
                heads.append((i, LINES[i].strip()))
    res_line = next(i for i in nums if LINES[i].strip() == "Resources" and i > heads[-1][0])
    assert [h[1] for h in heads] == NAMES, [h[1] for h in heads]
    out = {}
    for n, (i, name) in enumerate(heads):
        end = (heads[n + 1][0] if n + 1 < len(heads) else res_line) - 1
        body = [j for j in nums if i < j <= end and LINES[j].strip()]
        lab = {}
        for j in body:
            t = LINES[j].strip()
            for key, pre in (("criteria", "Selection criteria:"), ("questions", "Questions to ask:"),
                             ("questions", "Key considerations:"), ("why", "Why this matters:"),
                             ("goal", "The goal of this consideration")):
                if t.startswith(pre):
                    lab[key] = j
                    if key == "questions":
                        lab["question_label"] = pre.rstrip(":")
        assert set(lab) == {"criteria", "questions", "question_label", "why", "goal"}, (name, lab)

        def para_end(a):
            last = a
            for j in nums:
                if j <= a: continue
                if j > end: break
                if LINES[j].strip() == "": break
                last = j
            return last
        out[name] = dict(ordinal=n + 1, head=i, end=end, criteria=(lab["criteria"], lab["questions"] - 1),
                         questions=(lab["questions"], lab["why"] - 1), why=(lab["why"], para_end(lab["why"])),
                         goal=(lab["goal"], para_end(lab["goal"])), question_label=lab["question_label"])
    return out


def text_of(a, b, label=None):
    t = st.span(cleaned, a, b)
    if label:
        t = re.sub(r"^" + re.escape(label) + r"\s*", "", t)
    return re.sub(r"\s+", " ", t).strip()


def summary_items():
    t = text_of(86, 144)
    parts = re.split(r"(?:^|(?<=\s))(\d{1,2})\. (?=[A-Z])", t)
    items = {}
    for k in range(1, len(parts), 2):
        items[int(parts[k])] = parts[k + 1].strip()
    assert sorted(items) == list(range(1, 13)), sorted(items)
    out = {}
    for n, body in items.items():
        nm, _, rest = body.partition(": ")
        prop, sep, seek = rest.partition(" Seek out ")
        assert sep and nm == NAMES[n - 1], (n, nm)
        out[nm] = {"ordinal": n, "product_property": prop.strip(), "seek_out": ("Seek out " + seek).strip()}
    return out


def goal_and_guidance(s):
    """The goal sentence, and the paragraphs of the section after it. pdftotext
    prints no blank line between the goal sentence and the body that follows,
    so the goal is cut at its sentence end, not at a paragraph end (pass 2:
    the paragraph read swallowed up to 2,900 characters of guidance)."""
    paras, cur = [], []
    for j in sorted(LINES):
        if j < s["goal"][0] or j > s["end"]:
            continue
        if LINES[j].strip() == "":
            if cur:
                paras.append(cur)
            cur = []
        else:
            cur.append(j)
    if cur:
        paras.append(cur)
    texts = [text_of(p[0], p[-1]) for p in paras]
    m = re.match(r"(The goal of this consideration .*?\.)(?=\s|$)", texts[0])
    assert m, texts[0][:80]
    texts[0] = texts[0][m.end():].strip()
    return m.group(1), [t for t in texts if t]


def section_instances():
    sec, summ, out = sections(), summary_items(), []
    for name in NAMES:
        s = sec[name]
        qtext = text_of(*s["questions"], label=s["question_label"] + ":")
        qs = [x for x in re.split(r"(?<=\?)\s+", qtext) if x]
        goal, guidance = goal_and_guidance(s)
        inst = {"ordinal": s["ordinal"], "name": name,
                "product_property": summ[name]["product_property"], "seek_out": summ[name]["seek_out"],
                "selection_criteria": text_of(*s["criteria"], label="Selection criteria:"),
                "question_label": s["question_label"], "questions": qs,
                "why_this_matters": text_of(*s["why"], label="Why this matters:"),
                "goal": goal, "buyer_guidance": guidance}
        if name == "Threat Modeling":
            # the bulleted questions after "answer the following questions:" (pass 2)
            lead = next(j for j in sorted(LINES) if s["head"] < j <= s["end"] and "answer the following questions:" in LINES[j])
            body = text_of(lead + 1, s["end"])
            inst["threat_model_questions"] = [q.strip() for b in body.split("") if b.strip()
                                              for q in re.split(r"(?<=\?)\s+", b.strip()) if q.strip()]
        out.append(inst)
    return out


# ------------------------------------------------------------ id selection
RESOLVED = []   # (field label, id, first 60 chars) for the join read-back


def lines_of(r):
    a, _, b = str(r["source_lines"]).partition("-")
    return int(a), int(b or a)


def sel(label, expect=None, one=False, empty_ok=False, **c):
    out = []
    for r in REQ:
        if "id" in c and not r["id"].endswith("#" + c["id"]): continue
        if "role" in c and r.get("role") != c["role"]: continue
        if "norole" in c and r.get("role"): continue
        if "consideration" in c and r.get("consideration") != c["consideration"]: continue
        if "has_consideration" in c and not r.get("consideration"): continue
        if "question_set" in c and r.get("question_set") != c["question_set"]: continue
        if "item_of" in c and not str(r.get("item_of", "")).endswith("#" + c["item_of"]): continue
        if "split_of" in c and not str(r.get("split_of", "")).endswith("#" + c["split_of"]): continue
        if "lines" in c and str(r.get("source_lines")) != c["lines"]: continue
        if "text_prefix" in c and not r["text"].startswith(c["text_prefix"]): continue
        if "within" in c:
            if "source_lines" not in r: continue
            a, b = lines_of(r)
            if not (c["within"][0] <= a and b <= c["within"][1]): continue
        out.append(r["id"])
    if (not out and not empty_ok) or (one and len(out) != 1) or (expect is not None and len(out) != expect):
        raise SystemExit(f"selector {label} {c}: matched {len(out)} (expect {expect if expect is not None else '>=1'})")
    for i in out:
        RESOLVED.append((label, i.split("#")[1], next(r["text"] for r in REQ if r["id"] == i)[:70]))
    return out


SEC = sections()
SPLIT_PARENTS = {r["split_of"] for r in REQ if r.get("split_of")}
SECTION_INSTANCES = section_instances()
why_ids, guide_ids = [], []
for nm, s in SEC.items():
    why_ids += sel(f"why:{nm}", empty_ok=True, norole=1, consideration=nm, within=s["why"])
    for r in REQ:
        # a split parent is cited through its children (pass 2)
        if r.get("consideration") == nm and not r.get("role") and "source_lines" in r and r["id"] not in SPLIT_PARENTS:
            a, b = lines_of(r)
            if s["head"] < a <= s["end"] and not (s["why"][0] <= a and b <= s["why"][1]):
                guide_ids.append(r["id"])
assert guide_ids
ROLE_COUNTS = collections.Counter(r.get("role") for r in REQ if r.get("role"))
INFERRED = lambda p: sel(f"inferred:{p[:20]}", one=True, text_prefix=p)

R_LIST = sel("summary lead-in", one=True, id="R-0003") + sel("elements lead-in", one=True, id="R-0009")
R_EVENT = sel("event record", one=True, text_prefix="All event records should include")
R_TYPES = sel("log types lead-in", one=True, lines="354", text_prefix="Log types that buyers")
R_TYPE_ITEMS = sel("log type items", expect=6, item_of=R_TYPES[0].split("#")[1])
# the sixth item of the minimum list is a format, not an event kind (pass 2)
R_FORMAT_ITEM = sel("log format item", one=True, item_of=R_TYPES[0].split("#")[1], text_prefix="Open standard formats.")
R_EVENT_KINDS = [i for i in R_TYPE_ITEMS if i not in R_FORMAT_ITEM]
assert len(R_EVENT_KINDS) == 5, R_EVENT_KINDS
R_ADV_ID = sel("advisory identifier", one=True, text_prefix="Vulnerabilities should be assigned an identifier", lines="772")
R_ADV = sel("advisory content", one=True, text_prefix="Public disclosure of information about available security updates")
R_ADV_MSG = sel("advisory message", one=True, text_prefix="Updates are accompanied by advisory messages")
R_ADV_FMT = sel("advisory format", one=True, text_prefix="Security advisories provided in an automatically retrievable")
R_VEX = sel("vex status", one=True, text_prefix="Vulnerability Exploitability eXchange (VEX) statements indicating")
R_ADOPT = sel("adoption", expect=2, split_of="R-0011")
R_NOPRIO = sel("not in priority order", one=True, text_prefix="These elements are not in priority order.")
R_NOTHRESH = INFERRED("The guide sets no acceptance threshold")
R_UNRANKED = INFERRED("The twelve elements are a priority set as a whole")
R_BASELINE = INFERRED("Conformance is judged on the baseline version")
R_DELIVERED = INFERRED("The Secure by Default criterion is judged on the product as delivered")
R_QUESTIONS = sel("all questions", expect=ROLE_COUNTS["question"], role="question")
R_QASK = sel("questions-to-ask", question_set="questions to ask")
R_QTM = sel("threat-model questions", question_set="threat model questions")
R_CRIT = sel("criteria", expect=ROLE_COUNTS["criterion"], role="criterion")
R_ELEM = sel("elements", expect=ROLE_COUNTS["element"], role="element")
R_SEEK = sel("seek-out", expect=ROLE_COUNTS["seek-out"], role="seek-out")
R_GOAL = sel("goals", expect=ROLE_COUNTS["goal"], role="goal")
TEXT = {r["id"]: r["text"] for r in REQ}
FAV = {r["id"]: r.get("favourable_answer") for r in REQ}
OPEN_Q = [i for i in R_QUESTIONS if FAV[i] == "open"]
CLOSED_Q = [i for i in R_QUESTIONS if FAV[i] in ("yes", "no", "none")]
assert len(OPEN_Q) + len(CLOSED_Q) == len(R_QUESTIONS), (len(OPEN_Q), len(CLOSED_Q))
Q_CLOSED_CASE = sel("case: a closed question", one=True, role="question", text_prefix="Can the product alert on breaks")
Q_OPEN_CASE = sel("case: an open question", one=True, role="question", text_prefix="What security measures does the product implement")
NOT_Q_CASE = sel("case: an entry that is no question", one=True, text_prefix="When procuring products, OT owners")


def lines_label(ids):
    return ", ".join("L" + str(next(r["source_lines"] for r in REQ if r["id"] == i)) for i in ids)


_last = max(j for j in LINES if j <= SEC[NAMES[-1]]["end"] and LINES[j].strip())
CS_LOCATOR = f"every consideration section (L{SEC[NAMES[0]]['head']}-{_last})"
SER_LOCATOR = "Logging in the Baseline Product, " + lines_label(R_EVENT)
SAC_LOCATOR = "Vulnerability Management, " + lines_label(R_ADV_ID + R_ADV + R_ADV_MSG)
VEX_LOCATOR = "Vulnerability Management, " + lines_label(R_VEX)
short = lambda ids: ", ".join(i.split("#")[1] for i in ids)

# ------------------------------------------------------------ schema spec
S = lambda **k: k
ENUM_NAMES = S(type="string", enum=NAMES)
REF = S(type="string", pattern=IDRE)


def F(name, schema, required, doc, ids=None, reason=None):
    return dict(name=name, schema=schema, required=required, doc=doc, ids=ids, reason=reason)


DERIVED_WHY = "derived: the guide prescribes no such field; it makes the stated duty testable"
STRUCT = collections.OrderedDict()
STRUCT["consideration-section"] = dict(
    locator=CS_LOCATOR, desc="The guide's own per-consideration template (derived from the twelve sections; the guide names the parts in its list of what the sections provide).",
    fields=[
        F("ordinal", S(type="integer", minimum=1, maximum=12), True, "Position 1..12 in the guide's list, bound to the name (Configuration Management is 1, Upgrade and Patch Tooling 12); the guide says the elements are not in priority order.", R_LIST + R_NOPRIO + R_UNRANKED),
        F("name", ENUM_NAMES, True, "Heading, equal to the Table of Contents title.", R_LIST),
        F("product_property", S(type="string", minLength=1), False, "The Summary list's statement of what the product does (L86-144).", R_ELEM),
        F("seek_out", S(type="string", minLength=1), False, "The Summary list's seek-out sentence for the element.", R_SEEK),
        F("selection_criteria", S(type="string", minLength=1), True, "Paragraph after the label Selection criteria.", R_CRIT),
        F("question_label", S(type="string", enum=["Questions to ask", "Key considerations"]), True,
          "Label of the question paragraph; Secure Communications uses Key considerations (source defect).", None, "the label is a fact of the sections, not a requirement"),
        F("questions", S(type="array", minItems=1, items=S(type="string", minLength=1)), True, "The questions of the question paragraph, split at each question mark.", R_QASK),
        F("threat_model_questions", S(type="array", minItems=1, items=S(type="string", minLength=1)), False, "Threat Modeling only: questions in the goal text that threat models let manufacturers and buyers answer.", R_QTM),
        F("why_this_matters", S(type="string", minLength=1), True, "Paragraph after the label Why this matters.", why_ids, "no requirements entry lies in a Why this matters paragraph (selected by script over all twelve: 0)"),
        F("goal", S(type="string", minLength=1), True, "The goal sentence, The goal of this consideration is ...; the rendering prints no paragraph break after it, so it is cut at its sentence end.", R_GOAL),
        F("buyer_guidance", S(type="array", items=S(type="string", minLength=1)), False,
          "The paragraphs after the goal sentence: look-fors, OT context, cross-references; entries carry the buyer duties.", guide_ids),
    ])
STRUCT["security-event-record"] = dict(
    locator=SER_LOCATOR, desc="What every event record includes.",
    fields=[
        F("timestamp", S(type="string", minLength=1), True, "Format not given.", R_EVENT),
        F("source_address", S(type="string", minLength=1), True, "Source address; type not given.", R_EVENT),
        F("source_port", S(type=["integer", "string"], minimum=0, maximum=65535, minLength=1), True, "Source port; the guide says address and port together. An integer 0 to 65535 or a non-empty string.", R_EVENT),
        F("affected_account", S(type="string", minLength=1), True, "Affected account details.", R_EVENT),
        F("correlation_id", S(type="string", minLength=1), True, "Correlation identifier.", R_EVENT),
        F("event_description", S(type="string", minLength=1), True, "Event description.", R_EVENT),
        F("event_type", S(type="string", enum=["authentication", "log-integrity", "device-change", "data-event", "error"]), False,
          "Optional: the five event kinds of the minimum log-type list (the sixth item, open standard formats, is a format, not an event kind). The guide does not put a type on the record.",
          R_EVENT_KINDS, None),
    ])
STRUCT["security-advisory-content"] = dict(
    locator=SAC_LOCATOR, desc="What a manufacturer's public disclosure of a security update contains.",
    fields=[
        F("vulnerability_id", S(type="string", pattern=r"^CVE-\d{4}-\d{4,}$"), True, "CVE number; pattern is derived from the CVE form, the guide names only a CVE number.", R_ADV_ID),
        F("description", S(type="string", minLength=1), True, "Accurate description of the vulnerabilities.", R_ADV),
        F("root_cause", S(type="string", minLength=1), True, "Root cause.", R_ADV),
        F("cwe", S(type="array", minItems=1, items=S(type="string", pattern=r"^CWE-\d+$")), True, "Common weakness enumeration entries.", R_ADV),
        F("affected_products", S(type="array", minItems=1, items=S(type="string", minLength=1)), True, "Information allowing users to identify the products affected.", R_ADV),
        F("impacts", S(type="string", minLength=1), True, "Impacts of the vulnerabilities.", R_ADV),
        F("severity", S(type="string", minLength=1), True, "Severity; scale not given.", R_ADV),
        F("remediation_information", S(type="string", minLength=1), True, "Clear and accessible information to help users remediate; the advisory message accompanying an update gives the potential action to be taken.", R_ADV + R_ADV_MSG),
    ])
STRUCT["vex-statement"] = dict(
    locator=VEX_LOCATOR, desc="A VEX statement for a widely publicized vulnerability; the guide says it follows CSAF and names two statuses.",
    fields=[
        F("vulnerability", S(type="string", minLength=1), True, "The celebrity vulnerability the statement is about (the guide's example class is Log4Shell-type).", R_VEX),
        F("status", S(type="string", enum=["not affected", "under investigation"]), True, "The two statuses the guide names.", R_VEX),
    ])
STRUCT["manufacturer-response"] = dict(
    locator="derived; the guide prescribes questions, not a response format", desc="One manufacturer answer to one question of a consideration.",
    fields=[
        F("question", S(type="string", enum=R_QUESTIONS), True, "Id of the question's requirements entry: one of the 46 entries with role question.", R_QUESTIONS),
        F("answer", S(type="string", enum=["yes", "no", "open"]), True, "yes or no for a closed question, open where the question asks what or how (the schema binds the kind to the question: open for the entries whose favourable_answer is open, yes or no for the rest).", None, DERIVED_WHY),
        F("response_text", S(type="string"), False, "The manufacturer's words.", None, DERIVED_WHY),
        F("evidence", S(type="array", items=S(type="string", minLength=1)), False, "Documents or demonstrations offered.", None, DERIVED_WHY),
    ])
STRUCT["product-selection-evaluation"] = dict(
    locator="derived; the guide prescribes no evaluation record", desc="A buyer's assessment of one product against one consideration.",
    fields=[
        F("product", S(type="string", minLength=1), True, "Product evaluated.", None, DERIVED_WHY),
        F("consideration", ENUM_NAMES, True, "The consideration assessed.", R_LIST),
        F("criterion", S(type="string", minLength=1), True, "The selection criteria text the assessment is against.", R_CRIT),
        F("assessed_on", S(type="string", enum=["baseline-version"]), True, "The product as sold, without paid options, and as delivered.", R_BASELINE + R_DELIVERED),
        F("outcome", S(type="string", enum=["met", "not-met", "unknown"]), True, "The guide sets no acceptance threshold and ranks no element, so this is per consideration.", R_NOTHRESH + R_UNRANKED),
        F("responses", S(type="array", items={"$ref": "#/$defs/ManufacturerResponse"}), False, "Manufacturer responses used.", R_QUESTIONS),
        F("evidence", S(type="array", items=S(type="string", minLength=1)), False, "Required when the outcome is met.", None, DERIVED_WHY),
        F("adoption_evidence", S(type="array", items=S(type="string", minLength=1)), False, "Evidence the manufacturer adopts Secure by Design and ISA 62443, for example a roadmap.", R_ADOPT),
    ])
# No weight / priority / score field: the elements are unranked and the guide sets no threshold.
STRUCT["product-selection-evaluation"]["no_ranking_ids"] = R_UNRANKED


def build_schemas():
    out = {}
    for name, sp in STRUCT.items():
        props = {f["name"]: f["schema"] for f in sp["fields"]}
        s = {"$schema": "https://json-schema.org/draft/2020-12/schema", "$id": f"urn:library:{REC}:{name}.derived",
             "title": name + " - DERIVED",
             "description": "DERIVED by the library: " + sp["desc"] + " The guide publishes no schema. " + sp["locator"] + ".",
             "type": "object", "additionalProperties": False,
             "required": [f["name"] for f in sp["fields"] if f["required"]], "properties": props}
        if name == "product-selection-evaluation":
            s["if"] = {"properties": {"outcome": {"const": "met"}}, "required": ["outcome"]}
            s["then"] = {"required": ["evidence"], "properties": {"evidence": {"minItems": 1}}}
            s["$defs"] = {"ManufacturerResponse": build_one("manufacturer-response")}
        if name in BINDS:
            s["allOf"] = BINDS[name]
        out[name] = s
    return out


# Pass 2: constraints between fields, which a per-field schema cannot state.
# An ordinal is the name's position in the guide's list; an answer's kind is
# fixed by the question it answers.
BINDS = {
    "consideration-section": [{"if": {"properties": {"name": {"const": nm}}, "required": ["name"]},
                               "then": {"properties": {"ordinal": {"const": k + 1}}}} for k, nm in enumerate(NAMES)]
    + [{"if": {"properties": {"name": {"const": "Threat Modeling"}}, "required": ["name"]},
        "then": {"required": ["threat_model_questions"]},
        "else": {"not": {"required": ["threat_model_questions"]}}}],
    "manufacturer-response": [
        {"if": {"properties": {"question": {"enum": OPEN_Q}}, "required": ["question"]},
         "then": {"properties": {"answer": {"const": "open"}}}},
        {"if": {"properties": {"question": {"enum": CLOSED_Q}}, "required": ["question"]},
         "then": {"properties": {"answer": {"enum": ["yes", "no"]}}}},
    ],
}


def build_one(name):
    sp = STRUCT[name]
    s = {"type": "object", "additionalProperties": False,
         "required": [f["name"] for f in sp["fields"] if f["required"]],
         "properties": {f["name"]: f["schema"] for f in sp["fields"]}}
    if name in BINDS:
        s["allOf"] = BINDS[name]
    return s


# ------------------------------------------------------------ cases
def cases():
    inst = SECTION_INSTANCES[0]
    ok = {"ordinal": NAMES.index("Ownership") + 1, "name": "Ownership", "selection_criteria": "x", "question_label": "Questions to ask",
          "questions": ["Q?"], "why_this_matters": "w", "goal": "g"}
    ev = {"timestamp": "2026-01-01T00:00:00Z", "source_address": "192.0.2.1", "source_port": 502,
          "affected_account": "operator1", "correlation_id": "c-1", "event_description": "login"}
    adv = {"vulnerability_id": "CVE-2025-0001", "description": "d", "root_cause": "r", "cwe": ["CWE-20"],
           "affected_products": ["P 1.0"], "impacts": "i", "severity": "high", "remediation_information": "update"}
    rsp = {"question": Q_CLOSED_CASE[0], "answer": "yes"}
    evl = {"product": "P", "consideration": "Ownership", "criterion": "c", "assessed_on": "baseline-version",
           "outcome": "not-met"}
    L = []
    add = lambda n, s, e, w, i: L.append((n, s, e, w, i))
    def m(base, **k):
        d = dict(base); d.update(k); return d
    def drop(base, k):
        d = dict(base); d.pop(k); return d
    add("consideration-section-accept-minimal", "consideration-section", "accept", "the required keys", ok)
    add("consideration-section-accept-key-considerations", "consideration-section", "accept", "the Key considerations label", m(ok, question_label="Key considerations"))
    for k in ("ordinal", "name", "selection_criteria", "question_label", "questions", "why_this_matters", "goal"):
        add(f"consideration-section-reject-missing-{k}", "consideration-section", "reject", f"{k} absent", drop(ok, k))
    add("consideration-section-reject-ordinal-13", "consideration-section", "reject", "only twelve elements", m(ok, ordinal=13))
    add("consideration-section-reject-ordinal-name", "consideration-section", "reject", "the ordinal is the name's position in the guide's list: Ownership is 4, not 1", m(ok, ordinal=1))
    tm = m(ok, ordinal=NAMES.index("Threat Modeling") + 1, name="Threat Modeling")
    add("consideration-section-accept-threat-modeling", "consideration-section", "accept", "Threat Modeling with its threat model questions", m(tm, threat_model_questions=["Q?"]))
    add("consideration-section-reject-threat-modeling-no-tm-questions", "consideration-section", "reject", "Threat Modeling without its threat model questions", tm)
    add("consideration-section-reject-tm-questions-elsewhere", "consideration-section", "reject", "threat model questions belong to Threat Modeling only", m(ok, threat_model_questions=["Q?"]))
    add("consideration-section-reject-name", "consideration-section", "reject", "name not one of the twelve", m(ok, name="Patching"))
    add("consideration-section-reject-priority", "consideration-section", "reject", "the guide says the elements are not in priority order", m(ok, priority=1))
    add("consideration-section-reject-empty-questions", "consideration-section", "reject", "no question", m(ok, questions=[]))
    add("consideration-section-reject-label", "consideration-section", "reject", "unknown question label", m(ok, question_label="FAQ"))
    add("security-event-record-accept", "security-event-record", "accept", "all five details", ev)
    add("security-event-record-accept-typed", "security-event-record", "accept", "with the optional event_type", m(ev, event_type="data-event"))
    for k in ("timestamp", "source_address", "source_port", "affected_account", "correlation_id", "event_description"):
        add(f"security-event-record-reject-missing-{k}", "security-event-record", "reject", f"{k} absent: every record includes it", drop(ev, k))
    add("security-event-record-reject-event-type", "security-event-record", "reject", "event_type outside the five kinds", m(ev, event_type="open standard formats"))
    add("security-event-record-reject-empty-port", "security-event-record", "reject", "an empty source port is no port", m(ev, source_port=""))
    add("security-event-record-reject-port-range", "security-event-record", "reject", "a port number above 65535", m(ev, source_port=70000))
    add("security-event-record-reject-unknown", "security-event-record", "reject", "unknown key", m(ev, severity="x"))
    add("security-advisory-content-accept", "security-advisory-content", "accept", "every listed element", adv)
    for k in adv:
        add(f"security-advisory-content-reject-missing-{k}", "security-advisory-content", "reject", f"{k} absent", drop(adv, k))
    add("security-advisory-content-reject-cve", "security-advisory-content", "reject", "identifier not a CVE number", m(adv, vulnerability_id="VULN-1"))
    add("security-advisory-content-reject-cwe", "security-advisory-content", "reject", "not a CWE id", m(adv, cwe=["20"]))
    add("vex-statement-accept-not-affected", "vex-statement", "accept", "status not affected", {"vulnerability": "CVE-2021-44228", "status": "not affected"})
    add("vex-statement-accept-investigation", "vex-statement", "accept", "status under investigation", {"vulnerability": "CVE-2021-44228", "status": "under investigation"})
    add("vex-statement-reject-status", "vex-statement", "reject", "a status the guide does not name", {"vulnerability": "CVE-2021-44228", "status": "fixed"})
    add("vex-statement-reject-missing-status", "vex-statement", "reject", "status absent", {"vulnerability": "CVE-2021-44228"})
    add("manufacturer-response-accept", "manufacturer-response", "accept", "closed answer", rsp)
    add("manufacturer-response-accept-open", "manufacturer-response", "accept", "open answer with text, to an open question",
        {"question": Q_OPEN_CASE[0], "answer": "open", "response_text": "t", "evidence": ["doc"]})
    add("manufacturer-response-reject-question-ref", "manufacturer-response", "reject", "question ref not an id", m(rsp, question="Does the product log?"))
    add("manufacturer-response-reject-not-a-question", "manufacturer-response", "reject", "an id whose entry is not a question", m(rsp, question=NOT_Q_CASE[0]))
    add("manufacturer-response-reject-open-to-closed", "manufacturer-response", "reject", "open is no answer to a yes-or-no question", m(rsp, answer="open"))
    add("manufacturer-response-reject-yes-to-open", "manufacturer-response", "reject", "yes is no answer to a what or how question", {"question": Q_OPEN_CASE[0], "answer": "yes"})
    add("manufacturer-response-reject-answer", "manufacturer-response", "reject", "answer outside the enum", m(rsp, answer="maybe"))
    add("manufacturer-response-reject-missing-answer", "manufacturer-response", "reject", "answer absent", drop(rsp, "answer"))
    add("product-selection-evaluation-accept-not-met", "product-selection-evaluation", "accept", "not-met needs no evidence", evl)
    add("product-selection-evaluation-accept-met", "product-selection-evaluation", "accept", "met with evidence and a response",
        m(evl, outcome="met", evidence=["doc"], responses=[rsp]))
    add("product-selection-evaluation-reject-met-no-evidence", "product-selection-evaluation", "reject", "met without evidence", m(evl, outcome="met"))
    add("product-selection-evaluation-reject-met-empty-evidence", "product-selection-evaluation", "reject", "met with empty evidence", m(evl, outcome="met", evidence=[]))
    add("product-selection-evaluation-reject-weight", "product-selection-evaluation", "reject", "the guide ranks nothing and sets no threshold: no weight", m(evl, weight=3))
    add("product-selection-evaluation-reject-score", "product-selection-evaluation", "reject", "no score either", m(evl, score=0.5))
    add("product-selection-evaluation-reject-outcome", "product-selection-evaluation", "reject", "outcome outside the enum", m(evl, outcome="partial"))
    add("product-selection-evaluation-reject-bad-response", "product-selection-evaluation", "reject", "the ManufacturerResponse $def binds",
        m(evl, responses=[{"question": Q_CLOSED_CASE[0], "answer": "maybe"}]))
    add("product-selection-evaluation-reject-consideration", "product-selection-evaluation", "reject", "consideration not one of the twelve", m(evl, consideration="Cost"))
    add("product-selection-evaluation-reject-assessed-on", "product-selection-evaluation", "reject", "assessed on a paid option", m(evl, assessed_on="premium-version"))
    return L


# ------------------------------------------------------------ messages.yaml
def q(s): return json.dumps(s, ensure_ascii=False)


def jt(sc):
    if "$ref" in sc: return sc["$ref"]
    if "enum" in sc and all(re.match(IDRE, str(v)) for v in sc["enum"]):
        return f"enum of {len(sc['enum'])} requirements.yaml ids"
    if "enum" in sc: return "enum " + "|".join(sc["enum"])
    t = sc.get("type")
    if t == "array": return "array<" + jt(sc["items"]) + ">"
    return "/".join(t) if isinstance(t, list) else t


def messages_yaml():
    L = ["schema: \"library-messages/v1\"", f"record: {REC}", 'reviewed_by: ""',
         "note: " + q("The guide is prose. It prescribes no wire format, but it does prescribe structured content: a per-consideration "
                       "section template (selection criteria, questions to ask, why this matters, goal), what every event record includes, "
                       "what a security advisory discloses, and the status of a VEX statement. Those four are described here as structures; "
                       "the manufacturer-response and product-selection-evaluation structures are DERIVED so the questions and criteria can be "
                       "tested. All are derived (the guide publishes no schema); each is marked. constrained_by ids are selected from "
                       "requirements.yaml by distilled/schema/build.derived.py (raises on no match); a field with none carries an inferred_reason. "
                       "Derived JSON Schemas are in schema/."),
         "messages:"]
    for name, sp in STRUCT.items():
        L += [f"  - name: {q(name)}", f"    locator: {q(sp['locator'])}", '    encoding: "JSON object (derived)"',
              f"    layout: {q(sp['desc'])}", "    fields:"]
        for f in sp["fields"]:
            L += [f"      - name: {q(f['name'])}", f"        type: {q(jt(f['schema']))}",
                  f"        required: {'true' if f['required'] else 'false'}", f"        note: {q(f['doc'])}"]
            if f["ids"]:
                ids = list(dict.fromkeys(f["ids"]))
                L.append("        constrained_by:")
                L += [f"          - {q(i)}" for i in ids]
            else:
                L.append("        constrained_by: []")
                L.append(f"        inferred_reason: {q(f['reason'] or 'derived: no stated requirement constrains this field')}")
        L.append("    notes: " + q({
            "consideration-section": "Twelve instances in the guide, all parsed from the pinned source and validated by check.derived.py, which also checks each parsed goal sentence against its goal entry; buyer_guidance is the paragraphs after the goal sentence. The schema binds ordinal to name. Source defect SD-1: Secure Communications labels its questions Key considerations; the other eleven sections use Questions to ask.",
            "security-event-record": f"The guide does not say the minimum log types are fields of a record; event_type is optional and derived. Log types beyond the minimum come from the manufacturer's threat model (not a field). The sixth item of the minimum list, open standard formats ({short(R_FORMAT_ITEM)}), constrains the encoding, which the guide does not name, and no field. required true reads the should of {short(R_EVENT)} as the conformance test: a record missing a detail does not meet it.",
            "security-advisory-content": f"The guide says disclosure includes these; whether each is individually required is read as yes (derived). Advisories are to be automatically retrievable and machine-processable ({short(R_ADV_FMT)}), a property of the encoding, which this JSON shape does not fix.",
            "vex-statement": "CSAF is external to this guide; only the two status names are the guide's.",
            "manufacturer-response": f"Derived. The schema binds the answer's kind to the question: open for the {len(OPEN_Q)} question entries whose favourable_answer is open, yes or no for the other {len(CLOSED_Q)}. Whether an answer meets its consideration is read against that favourable_answer (yes, no or none), which the schema does not check.",
            "product-selection-evaluation": "Derived. No weight, score or rank field: the guide ranks nothing and sets no acceptance threshold (inferred entries cited on the outcome field).",
        }[name]))
    return "\n".join(L) + "\n"


def readme_schema():
    return f"""---
record: {REC}
kind: schema
title: "{REC} - schemas"
extracted: "2026-11-15"
reviewed_by: ""
---

# schema/ - DERIVED, generated by script

The guide is prose and ships no schema, so every file here is derived. Four structures are prescribed in the guide's own
wording (the per-consideration section, the event record, the security advisory content, the VEX status); two are derived
so the questions and selection criteria can be tested (manufacturer response, product selection evaluation).

| file | basis |
|---|---|
| `consideration-section.derived.schema.json` | the twelve sections; check.derived.py validates all twelve parsed from the source |
| `security-event-record.derived.schema.json` | {SER_LOCATOR.split(", ", 1)[1]} |
| `security-advisory-content.derived.schema.json` | {SAC_LOCATOR.split(", ", 1)[1]} |
| `vex-statement.derived.schema.json` | {VEX_LOCATOR.split(", ", 1)[1]} |
| `manufacturer-response.derived.schema.json` | derived |
| `product-selection-evaluation.derived.schema.json` | derived; no weight or score field, the guide ranks nothing |
| `build.derived.py` | regenerates schemas, `../messages.yaml`, `../examples/` |
| `check.derived.py` | validates sections and cases; prints how many it examined |
"""


EX_MARKERS = [("L324-325", "For example, immutable", "hot-swapping containers."),
              ("L533-535", "For example, instead of replacing", "securely by default."),
              ("L614-616", "For example, existing protocols", "against the system."),
              ("L625-627", "For example, a manufacturer could document", "active scanning."),
              ("L632-635", "Examples of system specifications", "mid process."),
              ("L675-679", "For example, in the Freight Rail", "enhances safety."),
              ("L845-847", "For example, a patch may be", "engineering logic.")]


def readme_examples(n_acc, n_rej):
    n_sites = sum(1 for l in LINES.values() if re.search(r"For example|Examples of", l))
    assert n_sites == len(EX_MARKERS), n_sites
    out = [f"""---
record: {REC}
kind: examples
title: "{REC} - examples and test vectors"
extracted: "2026-11-15"
reviewed_by: ""
---

# examples/

**Finding: the guide has no worked example, test vector or sample record.** Counted by script over the pinned
rendering: {n_sites} lines carry For example or Examples of, and each is a narrative illustration inside prose,
with no input, no expected result and no data to turn into a fixture. They are marked below so a reader can
see that nothing was dropped; the e.g. and i.e. lists are enumerations inside sentences and are not examples
in this sense.
"""]
    for rng, a, b in EX_MARKERS:
        out.append(f'<!-- q {rng} "{a}" .. "{b}" -->\n')
    out.append(f"""
What is held here is ours, marked `.derived.`: {n_acc} instances the derived schemas must accept and {n_rej} they must
reject. Each file is `{{schema, expect, why, instance}}`. The twelve real consideration sections are not copied: they
are parsed from the pinned source and validated by `../schema/check.derived.py`.
""")
    return "\n".join(out)


def write(path, content):
    assert BAN not in content, path
    path.write_text(content, encoding="utf-8")


def main():
    sch = build_schemas()
    for n, s in sch.items():
        write(HERE / f"{n}.derived.schema.json", json.dumps(s, indent=2, ensure_ascii=False) + "\n")
    ex = DIST / "examples"
    for f in ex.glob("*.derived.json"):
        f.unlink()
    cs = cases()
    for n, schema, expect, why, inst in cs:
        write(ex / f"{n}.derived.json", json.dumps({"derived": True, "schema": f"{schema}.derived.schema.json",
                                                    "expect": expect, "why": why, "instance": inst}, indent=2, ensure_ascii=False) + "\n")
    na = sum(1 for c in cs if c[2] == "accept")
    write(ex / "README.md", readme_examples(na, len(cs) - na))
    write(HERE / "README.md", readme_schema())
    write(DIST / "messages.yaml", messages_yaml())
    (HERE / "resolved-pairs.derived.txt").write_text(
        "# DERIVED read-back of every selector: label, id, first 70 characters of the entry's text\n" +
        "\n".join(f"{a}\t{b}\t{c}" for a, b, c in RESOLVED) + "\n", encoding="utf-8")
    print(f"wrote {len(sch)} schemas, {len(cs)} cases ({na} accept), {len(RESOLVED)} resolved id joins; "
          f"why-this-matters ids {len(why_ids)}, buyer-guidance ids {len(set(guide_ids))}")


if __name__ == "__main__":
    main()

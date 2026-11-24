#!/usr/bin/env python3
# DERIVED - not verbatim. Written by this library. Builds ../messages.yaml from
# protoc-descriptor.derived.json (fields, numbers, types, REQUIRED, rendering lines) and
# ../requirements.yaml (constrained_by), quoting the source from .cache/sigstore-bundle-0-3.txt.
#   python3 -I build-messages.derived.py [--write]   (without --write: compare with the committed file)
# Re-run it after the requirements lane appends ids: constrained_by is computed, never typed.
import importlib.util, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("ids", os.path.join(HERE, "_ids.derived.py"))
ids = importlib.util.module_from_spec(spec); spec.loader.exec_module(ids)
TXT = open(os.path.join(ids.ROOT, ".cache", "sigstore-bundle-0-3.txt"), encoding="utf-8").read().split("\n")
OUT = os.path.join(HERE, "..", "messages.yaml")
D = ids.descriptor()
REQS = ids.requirements()


def line(n): return TXT[n - 1].strip()


def span_of(r):
    s = str(r.get("source_lines", ""))
    if not s: return None
    a, _, b = s.partition("-")
    return int(a), int(b or a)


def inside(r, lo, hi):
    sp = span_of(r)
    return sp is not None and lo <= sp[0] and sp[1] <= hi


def rids(lo, hi): return [r["id"] for r in REQS if inside(r, lo, hi)]


def heading(kind, name):
    h = [i + 1 for i, l in enumerate(TXT) if re.fullmatch(r"\d+\.\d+\.  %s %s" % (kind, name), l)]
    assert len(h) == 1, (kind, name, h)
    return h[0], TXT[h[0] - 1].split()[0].rstrip(".")


# --- YAML emitter: block style, double-quoted scalars
def q(s): return json.dumps(s, ensure_ascii=False)


def prune(o):
    if isinstance(o, dict):
        return {k: prune(v) for k, v in o.items() if not (isinstance(v, (list, dict)) and not v)}
    if isinstance(o, list):
        return [prune(v) for v in o]
    return o


def emit(o, ind=0, out=None):
    o = prune(o)
    sp = "  " * ind
    out = [] if out is None else out
    if isinstance(o, dict):
        for k, v in o.items():
            if isinstance(v, (dict, list)) and v:
                out.append(f"{sp}{k}:"); emit(v, ind + 1, out)
            else:
                out.append(f"{sp}{k}: {sc(v)}")
    else:
        for v in o:
            if isinstance(v, dict) and v:
                ks = list(v.items())
                k0, v0 = ks[0]
                if isinstance(v0, (dict, list)) and v0:
                    out.append(f"{sp}- {k0}:"); emit(v0, ind + 2, out)
                else:
                    out.append(f"{sp}- {k0}: {sc(v0)}")
                for k, x in ks[1:]:
                    if isinstance(x, (dict, list)) and x:
                        out.append(f"{sp}  {k}:"); emit(x, ind + 2, out)
                    else:
                        out.append(f"{sp}  {k}: {sc(x)}")
            else:
                out.append(f"{sp}- {sc(v)}")
    return out


def sc(v):
    if v is None: return '""'
    if v is True: return '"true"'    # numbers and booleans are quoted: the library's two YAML readers type bare
    if v is False: return '"false"'  # scalars differently (hazards.md section 6), quoted strings they agree on
    if isinstance(v, int): return f'"{v}"'
    if isinstance(v, (list, dict)): return "[]" if isinstance(v, list) else "{}"
    return q(v)


WIRE = {"bytes": "length-delimited (2)", "string": "length-delimited (2)", "message": "length-delimited (2)",
        "int64": "varint (0)", "int32": "varint (0)", "enum": "varint (0)"}
JSONT = {"bytes": "string: base64 (standard alphabet, padded on output; parsers also accept URL-safe and unpadded)",
         "int64": "string: decimal (parsers also accept a JSON number)", "int32": "number",
         "string": "string", "message": "object", "enum": "string: the enum value name (parsers also accept the number)"}
FILE_NAME = {"sigstore_bundle.proto": "§1", "envelope.proto": "§2", "sigstore_common.proto": "§3", "sigstore_rekor.proto": "§4"}

# reference graph (which messages a message uses): reachability from Bundle
M = {m["name"]: m for f in D["files"] for m in f["messages"]}
REACH = set()
def reach(n):
    if n in REACH: return
    REACH.add(n)
    for f in M[n]["fields"]:
        if f["type"] == "message" and f["type_name"].split(".")[-1] in M: reach(f["type_name"].split(".")[-1])
reach("Bundle")
DSSE_COMMENT_REQ = {"payload": "228", "payloadType": "233", "signatures": "237-245", "sig": "256", "keyid": "261"}
FILE_LEVEL = {"Bundle": (36, 46)}   # 'Notes on versioning' comment at the top of sigstore_bundle.proto, before TimestampVerificationData


def msg_entry(f, m):
    hl, sec = heading("message", m["name"])
    prev_end = hl
    fields = []
    prev = m["rendering_line"]
    for x in m["fields"]:
        lo, hi = prev + 1, x["rendering_line"]
        c = rids(lo, hi)
        beh = x["behavior"]
        notes = []
        if f["name"] == "envelope.proto" and x["json_name"] in DSSE_COMMENT_REQ:
            c = sorted(set(c) | {ids.resolve(lines=DSSE_COMMENT_REQ[x["json_name"]])})
        if f["name"] == "envelope.proto":
            notes.append("the REQUIRED/OPTIONAL marker is in a comment (R-0028..R-0032), not a field_behavior annotation: protoc sees no behaviour")
        entry = {
            "name": x["name"], "json_name": x["json_name"], "number": x["number"], "type": x["type_name"] if x["type"] in ("message", "enum") else x["type"],
            "label": ("repeated" if x["label"] == "repeated" else "optional (proto3 explicit presence)" if x["proto3_optional"] else "oneof member" if x["oneof"] else "singular (implicit presence)" if x["type"] != "message" else "singular message"),
            "oneof": x["oneof"] or "",
            "field_behavior": ",".join(beh) if beh else "",
            "deprecated": x["deprecated"],
            "encoding": {"protobuf_wire": WIRE[x["type"]] + (", packed" if x["label"] == "repeated" and x["type"] in ("int32", "int64", "enum") else ""),
                         "proto3_json": JSONT[x["type"]] + (" (array)" if x["label"] == "repeated" else "")},
            "source": {"source_lines": str(x["rendering_line"]), "quote": line(x["rendering_line"])},
            "constrained_by": c,
        }
        if notes: entry["notes"] = notes
        fields.append(entry)
        prev = x["rendering_line"]
    e = {
        "name": m["name"], "full_name": m["full_name"], "locator": "§" + sec, "defined_in": f["name"],
        "reachable_from_bundle": m["name"] in REACH,
        "source": {"source_lines": str(m["rendering_line"]), "quote": line(m["rendering_line"])},
        "constrained_by": rids(*(((FILE_LEVEL[m["name"]]) if m["name"] in FILE_LEVEL else (0, 0)))) if m["name"] in FILE_LEVEL else [],
        "message_level_constrained_by": [r["id"] for r in REQS if inside(r, hl, m["rendering_line"])],
        "oneofs": m["oneofs"], "reserved_numbers": ", ".join(f"{a} to {b}" for a, b in m["reserved"]),
        "fields": fields,
    }
    return e



# --- constrained_by, second rule (verify pass, library#151): a requirement's own `field` -------------
# The span rule above attaches a comment to the FIRST declaration after it, so a comment that
# documents several fields lands on one of them: the VerificationMaterial key-material comment
# (forms 1-3, chain rules) sat wholly on public_key, and the LM-OTS rule on LMS_SHA256. The
# requirements lane names, for every entry, the proto path it constrains (`field:`). That path is
# resolved here through protoc's descriptor, never typed:
#   * a resolved path ADDS the id to the field, message, enum or enum value it ends at (a oneof
#     name adds it to the members the text names, or to all of them);
#   * a span placement is DROPPED when the id's path visits a sibling of that place (another field
#     of the same message, another value of the same enum) and never the place itself;
#   * an id placed nowhere is listed under `unplaced` with its `field` text as the reason.
SEG = r"[A-Za-z_][A-Za-z0-9_]*(?:\[[^\]]*\])?"
PATH = re.compile(r"(?<![\w.])([A-Z][A-Za-z0-9]*)((?:\." + SEG + r")*)"
                  r"|(?<![\w\])])(\." + SEG + r"(?:\." + SEG + r")*)"
                  r"|;\s*([a-z_][A-Za-z0-9_]*)(?=\s*:)")
ENUMS = {e["name"]: e for f in D["files"] for e in f["enums"]}


def _segs(s):
    return [re.sub(r"\[[^\]]*\]$", "", x) for x in re.findall(SEG, s)]


def _walk(kind, name, segs, chain, visited):
    """Follow segs from (kind, name); return (target, ancestor chain) or (None, chain)."""
    chain = list(chain)
    tgt = ("msg", name) if kind == "msg" else ("enum", name)
    for s in segs:
        if kind == "msg":
            fl = [x for x in M[name]["fields"] if x["name"] == s]
            if fl:
                x = fl[0]; tgt = ("field", name, s); visited.add(tgt); chain.append(("msg", name))
                tn = x["type_name"].split(".")[-1]
                kind, name = (("msg", tn) if x["type"] == "message" else ("enum", tn) if x["type"] == "enum" else (None, None))
            elif s in M[name]["oneofs"]:
                tgt = ("oneof", name, s); chain.append(("msg", name)); kind = "oneof"
            else:
                return None, chain
        elif kind == "enum" and s in [v["name"] for v in ENUMS[name]["values"]]:
            tgt = ("value", name, s); visited.add(tgt); chain.append(("enum", name)); kind = None
        else:
            return None, chain
    return tgt, chain + ([(kind, name)] if kind in ("msg", "enum") else [])


def resolve_field(text):
    """(targets, visited) for one requirement's `field` text; roots that name no message or enum
    (prose such as DSSE or Sigstore) are skipped."""
    targets, visited, last = set(), set(), None
    for mt in PATH.finditer(text or ""):
        tgt = None
        if mt.group(1):
            root = mt.group(1)
            if root not in M and root not in ENUMS:
                continue
            tgt, chain = _walk("msg" if root in M else "enum", root, _segs(mt.group(2)), [], visited)
        elif last:
            segs = _segs(mt.group(3)) if mt.group(3) else [mt.group(4)]
            for k in range(len(last) - 1, -1, -1):      # nearest ancestor that has the first segment
                if last[k][0] is None:
                    continue
                tgt, chain = _walk(last[k][0], last[k][1], segs, last[:k], visited)
                if tgt is not None:
                    break
        if tgt is None:
            continue
        last = chain
        after = text[mt.end():]
        if tgt[0] == "oneof":
            members = [x["name"] for x in M[tgt[1]]["fields"] if x["oneof"] == tgt[2]]
            mm = re.match(r"\s*(?:\(oneof\))?\s*:\s*(?:one of\s+)?([a-z_][a-z0-9_]*(?:\s*(?:\||,|or|and)\s*[a-z_][a-z0-9_]*)*)", after)
            named = [n for n in re.findall(r"[a-z_][a-z0-9_]*", mm.group(1)) if n in members] if mm else []
            for n in named or members:
                targets.add(("field", tgt[1], n)); visited.add(("field", tgt[1], n))
            continue
        targets.add(tgt)
        while tgt[0] == "value":                          # PublicKeyDetails.A, B, C
            mv = re.match(r"\s*,\s*([A-Z][A-Z0-9_]+)(?![\w.])", after)
            if not mv or mv.group(1) not in [v["name"] for v in ENUMS[tgt[1]]["values"]]:
                break
            t = ("value", tgt[1], mv.group(1)); targets.add(t); visited.add(t); after = after[mv.end():]
    return targets, visited


def rewire(msgs, enums):
    num = lambda i: int(i.rsplit("R-", 1)[1])
    res = {r["id"]: resolve_field(r.get("field", "")) for r in REQS}
    place = {}
    for m in msgs:
        place[("msg", m["name"])] = m["message_level_constrained_by"]
        for x in m["fields"]:
            place[("field", m["name"], x["name"])] = x["constrained_by"]
    for e in enums:
        place[("enum", e["name"])] = e["constrained_by"]
        for v in e["values"]:
            place[("value", e["name"], v["name"])] = v["constrained_by"]
    dropped, added = [], []
    for loc, lst in place.items():
        if loc[0] not in ("field", "value"):
            continue
        for i in list(lst):
            tg, vis = res[i]
            sib = [v for v in vis if v[0] == loc[0] and v[1] == loc[1] and v != loc]
            if tg and sib and loc not in vis:
                lst.remove(i); dropped.append((i, loc))
    for i, (tg, _) in res.items():
        for t in tg:
            lst = place[t]
            if i not in lst:
                lst.append(i); added.append((i, t))
    for lst in place.values():
        lst.sort(key=num)
    return dropped, added


def build():
    msgs, enums = [], []
    for f in D["files"]:
        for m in f["messages"]:
            msgs.append(msg_entry(f, m))
        for en in f["enums"]:
            hl, sec = heading("enum", en["name"])
            vals, prev = [], en["rendering_line"]
            for v in en["values"]:
                vals.append({"name": v["name"], "number": v["number"], "deprecated": v["deprecated"],
                             "source": {"source_lines": str(v["rendering_line"]), "quote": line(v["rendering_line"])},
                             "constrained_by": rids(prev + 1, v["rendering_line"])})
                prev = v["rendering_line"]
            enums.append({"name": en["name"], "full_name": en["full_name"], "locator": "§" + sec, "defined_in": f["name"],
                          "source": {"source_lines": str(en["rendering_line"]), "quote": line(en["rendering_line"])},
                          "constrained_by": [r["id"] for r in REQS if inside(r, hl, en["rendering_line"])],
                          "reserved_numbers": ", ".join(f"{a} to {b}" for a, b in en["reserved"]), "values": vals})

    dropped, added = rewire(msgs, enums)

    def find(phrase, at=None):
        h = [i + 1 for i, l in enumerate(TXT) if phrase in l and (at is None or i + 1 == at)]
        assert len(h) == 1, (phrase, h)
        return {"source_lines": str(h[0]), "quote": phrase}

    values = [
        {"name": "bundle media type, current (v0.3)", "value": "application/vnd.dev.sigstore.bundle.v0.3+json", "constrained_by": [ids.resolve(contains="MUST be application/vnd.dev.sigstore.bundle.v0.3+json")], "source": find("application/vnd.dev.sigstore.bundle.v0.3+json when"), "note": "also named at the versioning notes (L45, a second place)"},
        {"name": "bundle media type, legacy 0.1", "value": "application/vnd.dev.sigstore.bundle+json;version=0.1", "constrained_by": [ids.resolve(lines="147-148", skeleton=False), ids.resolve(lines="149", skeleton=False)], "source": find("application/vnd.dev.sigstore.bundle+json;version=0.1"), "note": "one of the previously defined formats clients are to accept (R-0081: a lowercase must, with a typo)"},
        {"name": "bundle media type, legacy 0.2", "value": "application/vnd.dev.sigstore.bundle+json;version=0.2", "constrained_by": [ids.resolve(lines="147-148", skeleton=False), ids.resolve(lines="150", skeleton=False)], "source": find("application/vnd.dev.sigstore.bundle+json;version=0.2")},
        {"name": "bundle media type, legacy 0.3", "value": "application/vnd.dev.sigstore.bundle+json;version=0.3", "constrained_by": [ids.resolve(lines="147-148", skeleton=False), ids.resolve(lines="151", skeleton=False)], "source": find("application/vnd.dev.sigstore.bundle+json;version=0.3"), "note": "names version 0.3 a second time, beside the current form"},
        {"name": "DSSE signature-extension kind for VerificationMaterial", "value": "application/vnd.dev.sigstore.verificationmaterial;version=0.1", "constrained_by": [ids.resolve(lines="71-73", skeleton=False)], "source": find("application/vnd.dev.sigstore.verificationmaterial;version=0.1"), "note": "the extension's `ext` field carries a VerificationMaterial; the source does not define the DSSE extension container itself (envelope.proto here has no `extensions` field)"},
        {"name": "DSSE payloadType for in-toto (docs page 5.1.2.2)", "value": "application/vnd.in-toto+json", "source": find("The DSSE envelope in a Sigstore Bundle must conform") if False else {"source_lines": str([i + 1 for i, l in enumerate(TXT) if l.startswith("The DSSE envelope in a Sigstore Bundle must conform")][0]), "quote": "The DSSE envelope in a Sigstore Bundle must conform"}, "constrained_by": [ids.resolve(contains="The DSSE envelope in a Sigstore Bundle must conform", skeleton=False)], "note": "a lowercase must on the docs page (R-0181, from candidate C-0071)"},
        {"name": "DSSE PAE prefix", "value": "DSSEv1", "source": find('"DSSEv1"        = ASCII'), "note": "PAE(type, payload) = DSSEv1 SP LEN(type) SP type SP LEN(payload) SP payload (R-0030)"},
        {"name": "Rekor entry kinds named in the examples", "value": "hashedrekord 0.0.1; intoto 0.0.2", "source": find('"kind": "hashedrekord",'), "note": "the docs placeholder says (hashrekord | dsse); the DSSE example uses intoto (SD-S-4)"},
    ]
    external = [
        {"name": "google.protobuf.Timestamp", "used_by": "TimeRange.start, TimeRange.end", "defined_in": "google/protobuf/timestamp.proto (imported by sigstore_common.proto; not Sigstore's, not spliced into the rendering)", "json": "RFC 3339 string"},
        {"name": "google.api.field_behavior (extension 1052 on FieldOptions) and enum FieldBehavior", "used_by": "25 fields carry REQUIRED (protoc-descriptor.derived.json)", "defined_in": "google/api/field_behavior.proto (googleapis, pinned in schema/protoc-descriptor.derived.json)", "json": "an annotation: it does not change the wire format or the JSON mapping"},
        {"name": "Rekor entry body (canonicalized_body content)", "used_by": "TransparencyLogEntry.canonicalized_body", "defined_in": "sigstore/rekor pkg/types (named at L714-715; not in the source)", "json": "compact JSON, apiVersion/kind/spec; examples/ decodes both"},
        {"name": "C2SP signed note / tlog-checkpoint", "used_by": "Checkpoint.envelope", "defined_in": "transparency-dev/formats and C2SP (named at L731-736; not in the source)", "json": "string"},
        {"name": "in-toto Statement", "used_by": "Envelope.payload", "defined_in": "in-toto/attestation spec/v1 (named in docs L1010; not in the source)", "json": "base64 of JSON"},
    ]
    silences = [
        {"what": "format of PublicKeyIdentifier.hint", "locator": "§3.8", "evidence": find("The format of the hint must be agreed upon out of band by the"), "note": "deliberately unspecified; RECOMMENDED (R-0043) to derive it from the key as in RFC 6962 section 3.2"},
        {"what": "schema of TransparencyLogEntry.canonicalized_body", "locator": "§4.5", "evidence": find("The contents of this field are the same as the `body` field in"), "note": "same as Rekor's `body`; the per-kind schema is Rekor's (hashedrekord 0.0.1 and intoto 0.0.2 are decoded in examples/)"},
        {"what": "values of KindVersion.kind and .version", "locator": "§4.1", "evidence": find("See here for a list: https://github.com/sigstore/rekor/tree/main/pkg/types"), "note": "an external list; the schema accepts any string"},
        {"what": "unit and epoch of integrated_time", "locator": "§4.5", "evidence": find("The UNIX timestamp from the log when the entry was persisted."), "note": "a UNIX timestamp; the examples are seconds"},
        {"what": "payload of the inclusion promise (SET)", "locator": "§4.4", "evidence": find("signature over a canonical JSON serialization of the persisted entry, the"), "note": "the exact bytes are a Rekor link, not here"},
        {"what": "relation of TransparencyLogEntry.log_index to InclusionProof.log_index", "locator": "§4.3, §4.5", "evidence": find("The global index of the entry, used when querying the log by index."), "note": "'global index' vs 'index in the tree it was written to'; the examples show different numbers"},
        {"what": "whether unknown JSON members are accepted", "locator": "§1.3", "evidence": find("Reserved for future additions of artifact types."), "note": "Bundle reserves numbers 5 to 50; the policy for unknown members is not stated"},
        {"what": "what the DSSE extension container looks like", "locator": "§1.2", "evidence": find("extension. Specifically, the `ext` field of the extension will expect this"), "note": "no `extensions` field in the embedded envelope.proto"},
        {"what": "behaviour of REQUIRED for a field at its proto3 default value", "locator": "§4.3", "evidence": find("repeated bytes hashes = 4 [(google.api.field_behavior) = REQUIRED];"), "note": "see schema/README.md: both readings recorded; source defect SD-8 in normative.md"},
        {"what": "how the intoto entry body's content.hash is computed", "locator": "§4.5", "evidence": find('"kind": "intoto",'), "note": "Rekor's, not stated here. Reproduced by the verify pass (examples/reproduce.py): SHA-256 of the sorted, compact JSON of the bundle's envelope with the certificate PEM beside the signature and the empty keyid left out. Pass 1 had listed this as source defect SD-S-10 (not recomputable); withdrawn."},
    ]
    defects = [
        {"id": "SD-S-1", "unified": "SD-23", "where": "docs 5.1.1.2 example (bundle.md L66-97)", "evidence": find('"keyId": "<KEY_ID>",'), "what": "trailing commas (also after the entry object): not JSON; fixture 3 does not parse (examples/fixtures.derived.json)"},
        {"id": "SD-S-2", "unified": "SD-23", "where": "docs 5.1.1.3 example (bundle.md L105-113)", "evidence": find('},', at=981), "what": "trailing comma after the timestamp object (L981, before the closing bracket): not JSON"},
        {"id": "SD-S-3", "unified": "SD-23", "where": "docs 5.1.2.2 example (bundle.md L142-151)", "evidence": find('"dsseEnvelope": {', at=1013), "what": "`\"dsseEnvelope\": { {` opens an object without a key: not JSON even wrapped"},
        {"id": "SD-S-4", "unified": "SD-14", "where": "docs 5.1.1.2 placeholder", "evidence": find('"kind": "(hashrekord | dsse)",'), "what": "`hashrekord` is misspelled (the example says hashedrekord) and `dsse` is not the kind the DSSE example uses (intoto)"},
        {"id": "SD-S-5", "unified": "SD-24", "where": "docs 5.1.2.1 prose", "evidence": find("`message_digest` for informational purposes, but it must be provided or computed from a provided"), "what": "names the field message_digest (the original name) while the JSON on the same page uses messageDigest"},
        {"id": "SD-S-6", "unified": "SD-9", "where": "sigstore_bundle.proto VerificationMaterial vs TransparencyLogEntry", "evidence": find("InclusionProof inclusion_proof = 6 [(google.api.field_behavior) = REQUIRED];"), "what": "inclusion_proof is REQUIRED, while the same message set allows v0.1 bundles that carry a promise and no proof (R-0018, R-0019): the schema follows REQUIRED and so rejects such bundles"},
        {"id": "SD-S-7", "unified": "SD-11", "where": "Bundle.dsse_envelope comment vs docs 5.1.2.2", "evidence": find("A DSSE envelope can contain arbitrary payloads."), "what": "the proto allows arbitrary payload types (verifiers check the type is expected); the docs page fixes payloadType to application/vnd.in-toto+json: the schema accepts any string and offers DsseEnvelopeInToto"},
        {"id": "SD-S-8", "unified": "SD-3", "where": "Bundle.media_type comment", "evidence": find("* application/vnd.dev.sigstore.bundle+json;version=0.3"), "what": "version 0.3 has two media-type spellings, the MUST form and this legacy form; both are listed as accepted, only one may be emitted (R-0021)"},
        {"id": "SD-S-9", "unified": "SD-1", "where": "typos in the source", "evidence": find("MUST be application/vnd.dev.sigstore.bundle.v0.3+json when"), "what": "`when when` (L146), `Clients must to be able` (L147), `ceritificate` (docs L62-63 and L102), `arifact` (docs L123), `determinisitically` (L857), `the the` (L336): wording only; the lowercase must in L147 is a requirement the skeleton could not count, R-0081 (from candidate C-0012)"},
    ]
    return {"msgs": msgs, "enums": enums, "values": values, "external": external, "silences": silences, "defects": defects,
            "dropped": dropped, "added": added}


def main():
    b = build()
    head = {
        "record": "sigstore-bundle-0-3", "reviewed_by": "",
        "extracted": "2026-11-20", "extracted_by": "FX-1 pass 1 (extract), schema+examples+messages lane",
        "source": ".cache/sigstore-bundle-0-3.txt (rendering by distilled/render-source.py of five digest-pinned inputs; see record.yaml content.note). source_lines are lines of that text.",
        "generated_by": "distilled/schema/build-messages.derived.py from distilled/schema/protoc-descriptor.derived.json and distilled/requirements.yaml; re-run after requirements.yaml changes",
        "applicability": "The source defines Protobuf messages (§1-§4, proto3, package dev.sigstore.bundle.v1 and its imports) and describes their JSON form (§5). Wire form is protobuf; the JSON form is the proto3 canonical JSON mapping.",
        "note": ("Empty lists are omitted. Numbers and booleans are quoted strings on purpose. constrained_by is computed by two rules, never typed. "
                 "(1) Span: every requirement whose source_lines lie inside a field's own comment-and-declaration span (the lines after the previous declaration up to this one); message_level_constrained_by is the message's leading comment; file_level_constrained_by is the 'Notes on versioning' comment. "
                 "(2) Field path (verify pass): each requirement's own `field` (requirements.yaml) is resolved through protoc's descriptor and adds the id to the field, message, enum or enum value it names; "
                 "a span placement is dropped where the id's path names a sibling of that place and not the place itself (the key-material comment documents three oneof members but sits above the first). "
                 "Ids placed by neither rule are in `unplaced`, with the `field` text that names no single element; `wiring` counts them."),
        "file_level_constrained_by": rids(30, 46),
    }
    placed = set(head["file_level_constrained_by"])
    def collect(o):
        if isinstance(o, dict):
            for k, v in o.items():
                if k.endswith("constrained_by") and isinstance(v, list): placed.update(v)
                else: collect(v)
        elif isinstance(o, list):
            for v in o: collect(v)
    collect(b["msgs"]); collect(b["enums"]); collect(b["values"])
    unplaced = [{"id": r["id"], "field": r.get("field", "")} for r in REQS if r["id"] not in placed]
    head["wiring"] = (f"{len(placed)} of the {len(REQS)} requirements are placed (span rule and field-path rule; "
                      f"the field-path rule added {len(b['added'])} placements and dropped {len(b['dropped'])} span placements); "
                      f"{len(unplaced)} are unplaced: cross-cutting rules (every bytes field, every field name, ...), the docs page's scope statements, "
                      f"and things outside the bundle. Counted by build-messages.derived.py.")
    lines = emit(head)
    lines += ["unplaced:"] + emit(unplaced, 1)
    lines += ["messages:"] + emit(b["msgs"], 1)
    lines += ["enums:"] + emit(b["enums"], 1)
    lines += ["values:"] + emit(b["values"], 1)
    lines += ["external_definitions:"] + emit(b["external"], 1)
    lines += ["source_silences:"] + emit(b["silences"], 1)
    lines += ["source_defects_note: " + q("SD-S-n are this lane's; the verify pass unified them with the other lanes' lists in normative.md (Source defects): unified names the SD-n there. SD-S-10 was withdrawn (see source_silences).")]
    lines += ["source_defects:"] + emit(b["defects"], 1)
    text = "\n".join(lines) + "\n"
    if "--write" in sys.argv:
        open(OUT, "w").write(text); print("wrote", OUT, len(b["msgs"]), "messages", len(b["enums"]), "enums")
    else:
        print("OK" if open(OUT).read() == text else "DIFFERS"); return 0 if open(OUT).read() == text else 1


if __name__ == "__main__":
    sys.exit(main())

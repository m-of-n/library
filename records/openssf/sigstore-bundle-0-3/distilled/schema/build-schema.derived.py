#!/usr/bin/env python3
# DERIVED - not verbatim. Written by this library. Builds bundle.derived.schema.json and
# ../examples/cases.derived.json from protoc-descriptor.derived.json and requirements.yaml.
#   python3 -I build-schema.derived.py [--write]     (without --write: compare with committed files)
# Names (json_name and original) come from protoc, REQUIRED from field_behavior, ids from
# _ids.derived.py. Hand-written cases are in HAND below.
import importlib.util, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("ids", os.path.join(HERE, "_ids.derived.py"))
ids = importlib.util.module_from_spec(spec); spec.loader.exec_module(ids)
SCHEMA = os.path.join(HERE, "bundle.derived.schema.json")
CASES = os.path.join(HERE, "..", "examples", "cases.derived.json")
M = ids.messages()
ID = "urn:library:sigstore-bundle-0-3:bundle.derived"
MT03 = "application/vnd.dev.sigstore.bundle.v0.3+json"
MT_ACC = [MT03] + [f"application/vnd.dev.sigstore.bundle+json;version=0.{i}" for i in (1, 2, 3)]


def le_regex(bound):
    alts = []
    for i, d in enumerate(bound):
        d = int(d)
        lo = 1 if i == 0 else 0
        if d > lo:
            alts.append(bound[:i] + f"[{lo}-{d-1}]" + "[0-9]" * (len(bound) - i - 1))
    alts.append(bound)
    return "|".join(alts)


I64 = ("^(?:0|[1-9][0-9]{0,17}|" + le_regex("9223372036854775807") + "|-(?:[1-9][0-9]{0,17}|"
       + le_regex("9223372036854775808") + "))$")
B64 = "(?:[A-Za-z0-9{a}]{{4}})*(?:[A-Za-z0-9{a}]{{2}}(?:==)?|[A-Za-z0-9{a}]{{3}}=?)?"
B64STD = "^" + B64.format(a="+/") + "$"
B64URL = "^" + B64.format(a="_-") + "$"

# overrides on top of what protoc gives
REACH = {}


def reach(name):
    if name in REACH:
        return
    REACH[name] = M[name]
    for f in M[name]["fields"]:
        if f["type"] == "message":
            reach(f["type_name"].split(".")[-1])


reach("Bundle")
ENUMS = {"HashAlgorithm": [v["name"] for v in next(e for f in ids.descriptor()["files"] for e in f["enums"]
                                                   if e["name"] == "HashAlgorithm")["values"]]}
# DSSE: the REQUIRED markers are comments in envelope.proto (R-0028..R-0032), not field_behavior
DSSE_REQ = {"Envelope": {"payload": "228", "payloadType": "233", "signatures": "237-245"},
            "Signature": {"sig": "256"}}


def prop(f):
    t = f["type"]
    if t == "bytes": s = {"$ref": "#/$defs/Base64Bytes"}
    elif t == "int64": s = {"$ref": "#/$defs/Int64String"}
    elif t == "string": s = {"type": "string"}
    elif t == "enum": s = {"$ref": "#/$defs/" + f["type_name"].split(".")[-1]}
    elif t == "message": s = {"$ref": "#/$defs/" + f["type_name"].split(".")[-1]}
    else: raise SystemExit(f"unmapped type {t}")
    if f["label"] == "repeated":
        s = {"type": "array", "items": s}
    return s


OVERRIDE = {
    ("Bundle", "media_type"): {"$ref": "#/$defs/MediaTypeAccepted"},
    ("Bundle", "dsse_envelope"): {"$ref": "#/$defs/BundleDsseEnvelope"},
    ("X509CertificateChain", "certificates"): {"type": "array", "minItems": 1, "items": {"$ref": "#/$defs/X509Certificate"}},
}
EXTRA_REQ = {"Bundle": {"media_type": ids.resolve(contains="MUST be versioned")},
             "X509CertificateChain": {"certificates": ids.resolve(contains="2. A sequence of one or more X.509")}}


def build_def(name):
    m = REACH[name]
    props, req, notboth, xc = {}, [], [], {}
    groups = {}
    for f in m["fields"]:
        cam, snk = f["json_name"], f["name"]
        s = OVERRIDE.get((name, snk), prop(f))
        if name == "Envelope" and snk == "signatures":
            s = {"type": "array", "minItems": 1, "items": {"$ref": "#/$defs/Signature"}}
        props[cam] = s
        if cam != snk:
            props[snk] = {"$ref": f"#/$defs/{name}/properties/{cam}"}
        names = [cam] + ([snk] if cam != snk else [])
        if f["oneof"]:
            groups.setdefault(f["oneof"], []).extend(names)
            xc[cam] = ids.required_id(name, snk)
            continue
        rid = None
        if "REQUIRED" in f["behavior"]:
            rid = ids.required_id(name, snk)
        elif snk in DSSE_REQ.get(name, {}):
            rid = ids.resolve(lines=DSSE_REQ[name][snk])
        elif snk in EXTRA_REQ.get(name, {}):
            rid = EXTRA_REQ[name][snk]
        if rid:
            xc[cam] = rid
            req.append(names)
        elif len(names) == 2:
            notboth.append(names)
    sch = {"type": "object", "properties": props, "additionalProperties": False}
    allof = []
    for names in req:
        allof.append({"oneOf": [{"required": [n]} for n in names]} if len(names) == 2 else {"required": names})
    for names in notboth:
        allof.append({"not": {"required": names}})
    for g, names in groups.items():
        allof.append({"oneOf": [{"required": [n]} for n in names]})
    # single-name required go to `required`, the rest to allOf
    single = [a["required"][0] for a in allof if "required" in a]
    allof = [a for a in allof if "required" not in a]
    if single: sch["required"] = single
    if allof: sch["allOf"] = allof
    sch["x-constrained-by"] = xc
    return sch


def build_schema():
    defs = {
        "Base64Bytes": {"type": "string", "anyOf": [{"pattern": B64STD}, {"pattern": B64URL}],
                        "x-note": "proto3 JSON bytes: standard or URL-safe alphabet (not mixed), padding optional"},
        "Int64String": {"type": "string", "pattern": I64,
                        "x-note": "proto3 JSON int64: decimal string in [-2^63, 2^63-1], no leading zeros, no -0"},
        "HashAlgorithm": {"type": "string", "enum": ENUMS["HashAlgorithm"]},
        "MediaTypeV03": {"type": "string", "const": MT03, "x-constrained-by": ids.resolve(contains="MUST be application/vnd.dev.sigstore.bundle.v0.3+json")},
        "MediaTypeAccepted": {"type": "string", "enum": MT_ACC},
    }
    for n in sorted(REACH):
        defs[n] = build_def(n)
    defs["BundleDsseEnvelope"] = {"allOf": [{"$ref": "#/$defs/Envelope"},
                                            {"properties": {"signatures": {"maxItems": 1}}}],
                                  "x-constrained-by": [ids.resolve(contains="MUST have exactly one signature"),
                                                       ids.resolve(contains="MUST reject an envelope")]}
    defs["DsseEnvelopeInToto"] = {"allOf": [{"$ref": "#/$defs/BundleDsseEnvelope"},
                                            {"properties": {"payloadType": {"const": "application/vnd.in-toto+json"}}}],
                                  "x-constrained-by": ids.resolve(contains="The DSSE envelope in a Sigstore Bundle must conform", skeleton=False),
                                  "x-note": "docs page 5.1.2.2 (a lowercase must); not used by Bundle: the proto says arbitrary payloads"}
    defs["BundleV03"] = {"allOf": [{"$ref": "#/$defs/Bundle"},
                                   {"properties": {"mediaType": {"$ref": "#/$defs/MediaTypeV03"},
                                                   "media_type": {"$ref": "#/$defs/MediaTypeV03"}}}]}
    return {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "$id": ID,
        "$comment": "DERIVED - not verbatim. Written by this library from the protoc descriptor of the four *.verbatim.proto files; "
                    "built by build-schema.derived.py; checked by check-schemas.derived.py. Not the Sigstore project's schema.",
        "title": "Sigstore Bundle v0.3, proto3 canonical JSON (derived)",
        "$ref": "#/$defs/Bundle",
        "x-open": [
            "PublicKey, TimeRange, ObjectIdentifier*, DistinguishedName, SubjectAlternativeName are not reachable from Bundle and are not modelled",
            "parser leniencies of proto3 JSON NOT accepted: null, int64 as JSON number, enum as integer",
            "unknown members rejected (additionalProperties false): source silent on unknown fields",
            "REQUIRED = member present in the JSON; default-valued members omitted by canonical emitters are rejected (see README)",
        ],
        "x-not-encodable": [
            "v0.3 PGI keyless => certificate form (R-0014): needs knowledge of the issuer/instance",
            "signature time inside certificate validity (R-0022), time-source presence for short-lived certs: needs the certificate and the log",
            "publicKey.hint equals DSSE keyid (R-0004, R-0022 tail): cross-value equality",
            "canonicalizedBody signature equals Bundle.content signature (R-0067): cross-value, decodes base64+JSON",
            "chain order / leaf-first (R-0005, R-0006), no root CA (R-0007): needs DER parsing",
            "TSA messageImprint matches signature (R-0003): needs RFC 3161 DER parsing",
        ],
        "$defs": defs,
    }


def sub(base, path):
    return base, path


# where each message sits inside a base instance
LOC = {
    "Bundle": ("ms", ""), "VerificationMaterial": ("ms", "/verificationMaterial"),
    "X509Certificate": ("ms", "/verificationMaterial/certificate"),
    "TransparencyLogEntry": ("ms", "/verificationMaterial/tlogEntries/0"),
    "LogId": ("ms", "/verificationMaterial/tlogEntries/0/logId"),
    "KindVersion": ("ms", "/verificationMaterial/tlogEntries/0/kindVersion"),
    "InclusionPromise": ("ms", "/verificationMaterial/tlogEntries/0/inclusionPromise"),
    "InclusionProof": ("ms", "/verificationMaterial/tlogEntries/0/inclusionProof"),
    "Checkpoint": ("ms", "/verificationMaterial/tlogEntries/0/inclusionProof/checkpoint"),
    "MessageSignature": ("ms", "/messageSignature"), "HashOutput": ("ms", "/messageSignature/messageDigest"),
    "X509CertificateChain": ("dsse", "/verificationMaterial/x509CertificateChain"),
    "TimestampVerificationData": ("dsse", "/verificationMaterial/timestampVerificationData"),
    "RFC3161SignedTimestamp": ("dsse", "/verificationMaterial/timestampVerificationData/rfc3161Timestamps/0"),
    "Envelope": ("dsse", "/dsseEnvelope"), "Signature": ("dsse", "/dsseEnvelope/signatures/0"),
    "PublicKeyIdentifier": ("pk", "/verificationMaterial/publicKey"),
}
WRONG = {"string": 5, "bytes": 5, "int64": 5, "enum": 5, "message": "x"}


EXD = os.path.join(HERE, "..", "examples")
BASES = {"ms": json.load(open(os.path.join(EXD, "bundle-message-signature.verbatim.json"))),
         "dsse": json.load(open(os.path.join(EXD, "bundle-dsse.verbatim.json"))),
         "pk": {"mediaType": MT03, "verificationMaterial": {"publicKey": {"hint": "k"}}, "messageSignature": {"signature": "c2ln"}}}


def present(base, path):
    n = BASES[base]
    for k in path.split("/")[1:]:
        if isinstance(n, list):
            n = n[int(k)] if int(k) < len(n) else None
        elif isinstance(n, dict) and k in n: n = n[k]
        else: return False
        if n is None: return False
    return True


def esc(s): return s.replace("~", "~0").replace("/", "~1")


def prep(m, f, base, p):
    """ops that make room for a oneof member: remove its siblings that the base carries"""
    if not f["oneof"]:
        return []
    return [{"remove": f"{p}/{x['json_name']}"} for x in m["fields"]
            if x["oneof"] == f["oneof"] and x is not f and present(base, f"{p}/{x['json_name']}")]


def gen_cases():
    cs = []
    n = [0]

    def add(**k):
        n[0] += 1
        k = dict(id=f"A-{n[0]:03d}", **k)
        k.setdefault("def", "Bundle")
        cs.append(k)

    for name in sorted(REACH):
        base, p = LOC[name]
        m = REACH[name]
        sch = build_def(name)
        for f in m["fields"]:
            cam, snk = f["json_name"], f["name"]
            fp = f"{p}/{cam}"
            pre = prep(m, f, base, p)
            if f["label"] == "repeated":
                add(base=base, ops=pre + [{"set": fp, "value": {}}], expect="reject", basis="proto3-json",
                    cites=[], why=f"{name}.{snk} is repeated: a JSON object is not an array", error_contains="expected type array")
                if f["type"] in ("string", "bytes", "int64"):
                    add(base=base, ops=pre + [{"set": fp, "value": [5]}], expect="reject", basis="proto3-json", cites=[],
                        why=f"{name}.{snk} elements are {f['type']}: a number is not", error_contains="expected type string")
                else:
                    add(base=base, ops=pre + [{"set": fp, "value": [5]}], expect="reject", basis="proto3-json", cites=[],
                        why=f"{name}.{snk} elements are messages: a number is not", error_contains="expected type object")
            else:
                exp = "object" if f["type"] == "message" else "string"
                add(base=base, ops=pre + [{"set": fp, "value": WRONG[f["type"]]}], expect="reject", basis="proto3-json", cites=[],
                    why=f"{name}.{snk} is {f['type']}: JSON number/string of the wrong kind", error_contains=f"expected type {exp}")
            if cam != snk:   # the same wrong value under the original spelling: binds the snake_case property schema
                sp = f"{p}/{snk}"
                if f["label"] == "repeated":
                    wv, exp = {}, "array"
                else:
                    wv, exp = WRONG[f["type"]], ("object" if f["type"] == "message" else "string")
                mv = [{"move": fp, "to": sp}] if present(base, fp) else []
                add(base=base, ops=pre + mv + [{"set": sp, "value": wv}], expect="reject", basis="proto3-json", cites=[],
                    why=f"{name}.{snk} spelled with the original field name must meet the same type", error_contains=f"expected type {exp}")
            if cam != snk and present(base, fp):
                add(base=base, ops=[{"move": fp, "to": f"{p}/{snk}"}], expect="accept", basis="proto3-json", cites=[],
                    why=f"parsers accept the original field name {snk} (protobuf JSON mapping; checked against python protobuf in the cross-run)")
                # the keyword that rejects it: a `not` over the pair (optional field) or an exactly-one oneOf (required)
                dup = ("'not' schema" if any("not" in a and set(a["not"].get("required", [])) == {cam, snk}
                                             for a in sch.get("allOf", [])) else "exactly one of")
                add(base=base, ops=[{"copy": fp, "to": f"{p}/{snk}"}], expect="reject", basis="proto3-json", cites=[],
                    why=f"{cam} and {snk} are the same field: both present is a duplicate", error_contains=dup)
        for rn in sch.get("required", []):
            f = next(x for x in m["fields"] if x["json_name"] == rn)
            if not present(base, f"{p}/{rn}"): continue
            add(base=base, ops=[{"remove": f"{p}/{rn}"}], expect="reject", basis="source",
                cites=[sch["x-constrained-by"][rn]], why=f"{name}.{f['name']} is required", error_contains=f"required property '{rn}'")
        for a in sch.get("allOf", []):
            if "oneOf" in a:
                names = [list(x["required"])[0] for x in a["oneOf"]]
                cam = names[0]
                f = next(x for x in m["fields"] if x["json_name"] == cam)
                if f["oneof"] or not present(base, f"{p}/{cam}"):
                    continue
                add(base=base, ops=[{"remove": f"{p}/{cam}"}], expect="reject", basis="source",
                    cites=[sch["x-constrained-by"][cam]], why=f"{name}.{f['name']} is required (either spelling)", error_contains="exactly one of")
        add(base=base, ops=[{"set": f"{p}/zzUnknown", "value": 1}], expect="reject", basis="source-silent", cites=[],
            why=f"unknown member in {name}: the source is silent; the schema is closed so a typo cannot pass", error_contains="additional property")
    return cs, add


def hand(cs, add):
    VM = "/verificationMaterial"
    # oneof groups
    for g, base, p, members in (
        ("VerificationMaterial", "ms", VM, ["publicKey", "x509CertificateChain", "certificate"]),
        ("Bundle", "ms", "", ["messageSignature", "dsseEnvelope"])):
        pass
    cert = "$ms:/verificationMaterial/certificate"
    add(base="ms", ops=[{"remove": VM + "/certificate"}], expect="reject", basis="source",
        cites=[ids.required_id("VerificationMaterial", "certificate")],
        why="VerificationMaterial.content: none of the three members present", error_contains="exactly one of")
    add(base="ms", ops=[{"set": VM + "/publicKey", "value": {"hint": "h"}}], expect="reject", basis="source",
        cites=[ids.required_id("VerificationMaterial", "public_key"), ids.required_id("VerificationMaterial", "certificate")],
        why="oneof content: publicKey and certificate both set", error_contains="exactly one of")
    add(base="ms", ops=[{"set": VM + "/x509CertificateChain", "value": {"certificates": [{"rawBytes": "AA=="}]}}], expect="reject",
        basis="source", cites=[ids.required_id("VerificationMaterial", "x509_certificate_chain")],
        why="oneof content: chain and certificate both set", error_contains="exactly one of")
    add(base="dsse", ops=[{"set": VM + "/publicKey", "value": {"hint": "h"}}], expect="reject", basis="source",
        cites=[ids.required_id("VerificationMaterial", "public_key")], why="oneof content: publicKey and chain both set", error_contains="exactly one of")
    add(base="ms", ops=[{"set": "/dsseEnvelope", "value": {"payload": "AA==", "payloadType": "t", "signatures": [{"sig": "AA=="}]}}],
        expect="reject", basis="source", cites=[ids.required_id("Bundle", "message_signature"), ids.required_id("Bundle", "dsse_envelope")],
        why="Bundle.content: messageSignature and dsseEnvelope both set", error_contains="exactly one of")
    add(base="ms", ops=[{"remove": "/messageSignature"}], expect="reject", basis="source", cites=[ids.required_id("Bundle", "message_signature")],
        why="Bundle.content: neither member present", error_contains="exactly one of")
    add(base="ms", ops=[{"move": "/messageSignature", "to": "/message_signature"}, {"copy": "/message_signature", "to": "/messageSignature"}],
        expect="reject", basis="proto3-json", cites=[], why="same oneof member in both spellings", error_contains="exactly one of")
    add(base="pk", ops=[], expect="accept", basis="source", cites=[ids.required_id("VerificationMaterial", "public_key"), ids.resolve(contains="1. An unspecified public key identifier") if False else ids.resolve(contains="Form (1) MAY be used")],
        why="publicKey form with a hint, no tlog entries, no timestamps: all optional")
    add(base="pk", ops=[{"set": VM + "/publicKey", "value": {}}], expect="accept", basis="source", cites=[ids.resolve(lines="544", skeleton=False)],
        why="empty PublicKeyIdentifier: the hint is Optional (R-0121); whether the empty member meets public_key's annotation is SD-8")
    add(base="pk", ops=[{"move": VM + "/publicKey", "to": VM + "/public_key"}], expect="accept", basis="proto3-json", cites=[], why="oneof member under its original name public_key")
    add(base="dsse", ops=[{"move": VM + "/x509CertificateChain", "to": VM + "/x509_certificate_chain"}], expect="accept", basis="proto3-json", cites=[], why="oneof member under its original name x509_certificate_chain")
    add(base="dsse", ops=[{"move": "/dsseEnvelope", "to": "/dsse_envelope"}], expect="accept", basis="proto3-json", cites=[], why="oneof member under its original name dsse_envelope")
    add(base="ms", ops=[{"move": "/messageSignature", "to": "/message_signature"}], expect="accept", basis="proto3-json", cites=[], why="oneof member under its original name message_signature")
    add(base="ms", ops=[{"move": VM + "/certificate", "to": VM + "/certificate"}], expect="accept", basis="source", cites=[ids.required_id("VerificationMaterial", "certificate")], why="certificate has one spelling (certificate)")
    add(**{"def": "BundleV03"}, base="ms", ops=[{"move": "/mediaType", "to": "/media_type"}], expect="accept", basis="proto3-json", cites=[], why="BundleV03 with media_type under the original name")
    add(**{"def": "BundleV03"}, base="ms", ops=[{"move": "/mediaType", "to": "/media_type"}, {"set": "/media_type", "value": MT_ACC[1]}], expect="reject", basis="source", cites=[ids.resolve(contains="MUST be application/vnd.dev.sigstore.bundle.v0.3+json")], why="BundleV03 const also binds the original spelling", error_contains="const")
    add(base="dsse", ops=[{"copy": VM + "/timestampVerificationData", "to": VM + "/timestamp_verification_data"}], expect="reject", basis="proto3-json", cites=[], why="timestampVerificationData in both spellings", error_contains="'not' schema")
    add(**{"def": "DsseEnvelopeInToto"}, base="dsse", ops=[{"copy": "/dsseEnvelope/signatures/0", "to": "/dsseEnvelope/signatures/1"}], instance_at="/dsseEnvelope", expect="reject", basis="source", cites=[ids.resolve(contains="MUST have exactly one signature")], why="DsseEnvelopeInToto also carries the one-signature rule", error_contains="maxItems")
    add(**{"def": "DsseEnvelopeInToto"}, base="dsse", ops=[{"remove": "/dsseEnvelope/payload"}], instance_at="/dsseEnvelope", expect="reject", basis="source", cites=[ids.resolve(lines="228")], why="DsseEnvelopeInToto also carries the Envelope's required members", error_contains="required property 'payload'")
    add(**{"def": "BundleV03"}, base="ms", ops=[{"remove": "/verificationMaterial"}], expect="reject", basis="source", cites=[ids.required_id("Bundle", "verification_material")], why="BundleV03 also carries every Bundle rule", error_contains="exactly one of")
    add(base="dsse", ops=[{"move": VM + "/timestampVerificationData", "to": VM + "/timestamp_verification_data"}], expect="accept", basis="proto3-json", cites=[], why="timestamp_verification_data under its original name")
    # media types
    for mt in MT_ACC:
        add(base="ms", ops=[{"set": "/mediaType", "value": mt}], expect="accept", basis="source",
            cites=[ids.resolve(contains="MUST be application/vnd.dev.sigstore.bundle.v0.3+json")] if mt == MT03 else
                  [ids.resolve(lines="147-148", skeleton=False), ids.resolve(lines=str(149 + MT_ACC.index(mt) - 1), skeleton=False)],
            why="media type accepted by Bundle (clients must accept the legacy forms, R-0081 to R-0084)")
    for mt in MT_ACC[1:]:
        add(**{"def": "BundleV03"}, base="ms", ops=[{"set": "/mediaType", "value": mt}], expect="reject", basis="source",
             cites=[ids.resolve(contains="MUST be application/vnd.dev.sigstore.bundle.v0.3+json")],
             why="BundleV03 requires the v0.3 form: a legacy form is for readers only", error_contains="expected one of" if False else "const")
    add(base="ms", ops=[{"set": "/mediaType", "value": "application/vnd.dev.sigstore.bundle.v0.4+json"}], expect="reject", basis="source-silent",
        cites=[], why="unknown version: not in the list of accepted forms", error_contains="not in enum")
    add(base="ms", ops=[{"set": "/mediaType", "value": MT03.upper()}], expect="reject", basis="source-silent", cites=[],
        why="media type compared exactly (case)", error_contains="not in enum")
    add(base="ms", ops=[{"remove": "/mediaType"}, {"remove": "/media_type"}], expect="reject", basis="source",
        cites=[ids.resolve(contains="MUST be versioned")], why="Bundle MUST be versioned by populating media_type", error_contains="exactly one of")
    add(**{"def": "BundleV03"}, base="ms", ops=[], expect="accept", basis="source", cites=[ids.resolve(contains="MUST be application/vnd.dev.sigstore.bundle.v0.3+json")],
        why="the message-signature example bundle (5.1.3.1) is a v0.3 bundle")
    add(**{"def": "BundleV03"}, base="dsse", ops=[], expect="accept", basis="source", cites=[ids.resolve(contains="MUST be application/vnd.dev.sigstore.bundle.v0.3+json")],
        why="the DSSE example bundle (5.1.3.2) is a v0.3 bundle")
    # DSSE
    S = "/dsseEnvelope/signatures"
    add(base="dsse", ops=[{"set": S, "value": []}], expect="reject", basis="source",
        cites=[ids.resolve(contains="MUST reject an envelope"), ids.resolve(lines="237-245")], why="zero signatures: envelope REQUIRED length >= 1 and bundle needs exactly one", error_contains="minItems")
    add(base="dsse", ops=[{"copy": S + "/0", "to": S + "/1"}], expect="reject", basis="source",
        cites=[ids.resolve(contains="MUST have exactly one signature"), ids.resolve(contains="MUST reject an envelope")], why="two signatures", error_contains="maxItems")
    add(**{"def": "Envelope"}, base=None, instance={"payload": "AA==", "payloadType": "t", "signatures": [{"sig": "AA=="}, {"sig": "AQ=="}]},
        expect="accept", basis="source", cites=[ids.resolve(lines="237-245")], why="the generic DSSE Envelope has no upper bound: only the Bundle profile limits to one")
    add(base="dsse", ops=[{"set": "/dsseEnvelope/payloadType", "value": "text/plain"}], expect="accept", basis="source",
        cites=[ids.resolve(lines="172-173", skeleton=False)], why="Bundle.dsse_envelope comment: DSSE can contain arbitrary payloads; payloadType is not pinned (docs page 5.1.2.2 pins in-toto: DsseEnvelopeInToto)")
    add(**{"def": "DsseEnvelopeInToto"}, base="dsse", ops=[{"set": "/dsseEnvelope/payloadType", "value": "text/plain"}], instance_at="/dsseEnvelope",
        expect="reject", basis="source", cites=[ids.resolve(contains="The DSSE envelope in a Sigstore Bundle must conform", skeleton=False)], why="docs page 5.1.2.2: payloadType is application/vnd.in-toto+json (a lowercase must)", error_contains="const")
    add(**{"def": "DsseEnvelopeInToto"}, base="dsse", ops=[], instance_at="/dsseEnvelope", expect="accept", basis="source", cites=[],
        why="the DSSE example's envelope has the in-toto payloadType")
    add(base="dsse", ops=[{"set": "/dsseEnvelope/signatures/0/keyid", "value": ""}], expect="accept", basis="source", cites=[ids.resolve(lines="261")], why="keyid is OPTIONAL; the example has an empty keyid")
    add(base="dsse", ops=[{"remove": "/dsseEnvelope/signatures/0/keyid"}], expect="accept", basis="source", cites=[ids.resolve(lines="261")], why="keyid OPTIONAL: absent")
    # chains and arrays
    add(base="dsse", ops=[{"set": VM + "/x509CertificateChain/certificates", "value": []}], expect="reject", basis="source",
        cites=[ids.resolve(contains="2. A sequence of one or more X.509")], why="a chain is one or more certificates", error_contains="minItems")
    add(base="dsse", ops=[{"copy": VM + "/x509CertificateChain/certificates/0", "to": VM + "/x509CertificateChain/certificates/1"}], expect="accept",
        basis="source", cites=[ids.resolve(contains="Subsequent members SHOULD")], why="two certificates: order/roles are not schema-checkable")
    add(base="ms", ops=[{"set": VM + "/tlogEntries", "value": []}], expect="accept", basis="source", cites=[ids.resolve(lines="931-933", skeleton=False)], why="tlogEntries is repeated and not REQUIRED (docs 5.1.1.2: not required by the spec)")
    add(base="ms", ops=[{"remove": VM + "/tlogEntries"}], expect="accept", basis="source", cites=[ids.resolve(lines="931-933", skeleton=False)], why="tlogEntries absent: transparency log entries are not required (docs 5.1.1.2)")
    add(base="ms", ops=[{"copy": VM + "/tlogEntries/0", "to": VM + "/tlogEntries/1"}], expect="accept", basis="source", cites=[ids.resolve(lines="931-933", skeleton=False)], why="several entries are allowed (docs: one or more)")
    TP = VM + "/tlogEntries/0/inclusionProof"
    add(base="ms", ops=[{"set": TP + "/hashes", "value": []}], expect="accept", basis="source", cites=[ids.required_id("InclusionProof", "hashes")],
        why="hashes REQUIRED but empty is what the 5.1.3.2 example prints (tree size 1)")
    add(base="ms", ops=[{"remove": VM + "/tlogEntries/0/inclusionPromise"}], expect="accept", basis="source", cites=[ids.resolve(lines="833-835", skeleton=False)],
        why="inclusion_promise is optional for >= v0.2 bundles")
    add(base="ms", ops=[{"remove": VM + "/tlogEntries/0/canonicalizedBody"}], expect="accept", basis="source", cites=[ids.resolve(lines="847-848", skeleton=False)], why="canonicalized_body is optional (proto comment 'Optional.')")
    add(base="ms", ops=[{"remove": "/messageSignature/messageDigest"}], expect="accept", basis="source", cites=[ids.resolve(contains="Clients MUST NOT attempt to use this digest")], why="message_digest is informational and has no presence rule")
    # enums
    for a in ("SHA2_256", "SHA2_384", "SHA2_512", "SHA3_256", "SHA3_384", "HASH_ALGORITHM_UNSPECIFIED"):
        add(base="ms", ops=[{"set": "/messageSignature/messageDigest/algorithm", "value": a}], expect="accept", basis="source",
            cites=[ids.resolve(contains="UNSPECIFIED SHOULD not")] if a.endswith("UNSPECIFIED") else [ids.resolve(lines="306", skeleton=False)], why=f"HashAlgorithm name {a}")
    add(base="ms", ops=[{"set": "/messageSignature/messageDigest/algorithm", "value": "SHA2_224"}], expect="reject", basis="source-silent", cites=[], why="not a HashAlgorithm name", error_contains="not in enum")
    add(base="ms", ops=[{"set": "/messageSignature/messageDigest/algorithm", "value": 1}], expect="reject", basis="source-silent", cites=[], why="enum as integer: proto3 parsers accept it, the schema models the name form only (x-open)", error_contains="expected type string")
    add(base="ms", ops=[{"set": "/messageSignature/messageDigest/algorithm", "value": "sha2_256"}], expect="reject", basis="source-silent", cites=[], why="enum names are case-sensitive", error_contains="not in enum")
    # base64
    SIG = "/messageSignature/signature"
    for v, ok, why in (("", True, "empty bytes"), ("AA==", True, "padded"), ("AA", True, "unpadded"), ("-_-_", True, "url-safe alphabet"),
                       ("+/+/", True, "standard alphabet"), ("+_+_", False, "mixed alphabets"), ("A", False, "impossible length"),
                       ("AAA", True, "3 chars, padding optional"), ("AA=", False, "wrong padding count"), ("AA===", False, "too much padding"),
                       ("A A=", False, "space"), ("AAAA\n", False, "trailing newline (ECMA anchoring)"), ("AA==AA==", False, "padding in the middle"),
                       ("AA!=", False, "non-alphabet character")):
        add(base="ms", ops=[{"set": SIG, "value": v}], expect="accept" if ok else "reject", basis="proto3-json", cites=[],
            why=f"bytes field, {why}", **({} if ok else {"error_contains": "pattern"}))
    # int64
    LI = VM + "/tlogEntries/0/logIndex"
    for v, ok, why in (("0", True, "zero"), ("9223372036854775807", True, "max"), ("9223372036854775808", False, "max+1"),
                       ("-9223372036854775808", True, "min"), ("-9223372036854775809", False, "min-1"), ("-0", False, "-0"),
                       ("007", False, "leading zeros"), ("+1", False, "plus sign"), ("1.5", False, "fraction"), ("", False, "empty"),
                       ("0x10", False, "hex"), ("1e3", False, "exponent"), ("12345678901234567890", False, "20 digits"),
                       (" 1", False, "space"), ("1\n", False, "trailing newline"), (5, False, "JSON number (x-open)"), (None, False, "null (x-open)")):
        add(base="ms", ops=[{"set": LI, "value": v}], expect="accept" if ok else "reject", basis="proto3-json", cites=[ids.required_id("TransparencyLogEntry", "log_index")],
            why=f"int64: {why}", **({} if ok else {"error_contains": "expected type string" if not isinstance(v, str) else "pattern"}))
    # REQUIRED at default value (both readings recorded in README)
    add(base="ms", ops=[{"remove": TP + "/logIndex"}], expect="reject", basis="source", cites=[ids.required_id("InclusionProof", "log_index")],
        why="reading A (enforced): REQUIRED means present; an emitter that omits logIndex 0 as proto3 default is rejected. python protobuf accepts it (cross-run)", error_contains="exactly one of")
    add(base="ms", ops=[{"set": TP + "/logIndex", "value": "0"}], expect="accept", basis="source", cites=[ids.required_id("InclusionProof", "log_index")], why="logIndex 0 spelled out (the 5.1.3.2 example does)")
    add(base="dsse", ops=[{"remove": "/dsseEnvelope/signatures/0/sig"}], expect="reject", basis="source", cites=[ids.resolve(lines="256")], why="sig is REQUIRED", error_contains="required property 'sig'")
    add(base="dsse", ops=[{"remove": "/dsseEnvelope/payload"}], expect="reject", basis="source", cites=[ids.resolve(lines="228")], why="payload is REQUIRED", error_contains="required property 'payload'")
    add(base="dsse", ops=[{"remove": "/dsseEnvelope/payloadType"}], expect="reject", basis="source", cites=[ids.resolve(lines="233")], why="payloadType is REQUIRED", error_contains="required property 'payloadType'")
    add(base="dsse", ops=[{"remove": "/dsseEnvelope/signatures"}], expect="reject", basis="source", cites=[ids.resolve(lines="237-245")], why="signatures is REQUIRED", error_contains="required property 'signatures'")
    add(base="ms", ops=[{"set": "", "value": []}], expect="reject", basis="proto3-json", cites=[], why="a Bundle is an object", error_contains="expected type object")
    add(base="ms", ops=[{"set": "", "value": {}}], expect="reject", basis="source", cites=[ids.required_id("Bundle", "verification_material")], why="empty object: nothing required is present", error_contains="exactly one of")
    add(base="ms", ops=[{"set": VM + "/tlogEntries/0/kindVersion/kind", "value": "hashrekord"}], expect="accept", basis="source-silent", cites=[], why="kind is any string; the docs placeholder (hashrekord | dsse) is misspelled (SD-S) and the schema does not enumerate Rekor kinds (external list)")
    add(base="ms", ops=[{"set": VM + "/tlogEntries/0/inclusionProof/checkpoint/envelope", "value": ""}], expect="accept", basis="source-silent", cites=[ids.required_id("Checkpoint", "envelope")], why="empty checkpoint text is present-but-empty: presence only (README reading A)")


def build_cases():
    cs, add = gen_cases()
    hand(cs, add)
    return {
        "schema": "../schema/bundle.derived.schema.json", "kind": "derived-cases",
        "note": "DERIVED - written by this library, not the source. Built by ../schema/build-schema.derived.py. base: ms = the 5.1.3.1 message-signature bundle, dsse = the 5.1.3.2 DSSE bundle (both cut from bundle.md, examples/*.verbatim.json), pk = a minimal publicKey bundle; ops edit a copy (set/remove/copy/move, JSON-pointer paths); instance_at selects a sub-instance after ops. basis: source (a cited requirement or prose says so; cites are ids resolved by script), proto3-json (protobuf JSON mapping, external to the pinned source), source-silent (the source says nothing; behaviour pinned). error_contains must appear in at least one reported error, so a reject for the wrong reason fails.",
        "bases": {"ms": {"fixture": "bundle-message-signature.verbatim.json"}, "dsse": {"fixture": "bundle-dsse.verbatim.json"},
                  "pk": {"instance": {"mediaType": MT03, "verificationMaterial": {"publicKey": {"hint": "k"}}, "messageSignature": {"signature": "c2ln"}}}},
        "cases": cs,
    }


def main():
    write = "--write" in sys.argv
    out = {SCHEMA: build_schema(), CASES: build_cases()}
    bad = 0
    for p, doc in out.items():
        text = json.dumps(doc, indent=1, ensure_ascii=False) + "\n"
        if write:
            open(p, "w").write(text); print("wrote", os.path.relpath(p, HERE))
        elif not os.path.exists(p) or open(p).read() != text:
            print("DIFFERS from committed:", os.path.relpath(p, HERE)); bad = 1
    if not write and not bad: print("OK: committed schema and cases equal the builder output")
    return bad


if __name__ == "__main__":
    sys.exit(main())

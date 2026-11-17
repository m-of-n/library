#!/usr/bin/env python3
# DERIVED, not verbatim. Writes ../messages.yaml. Written by this library.
#
#   python3 -I build-messages.derived.py           # write ../messages.yaml
#   python3 -I build-messages.derived.py --check   # fail if the file on disk differs
#
# What is typed here is structure: names, types, required flags and WHICH source
# lines and WHICH requirement a field answers to. What is never typed here:
#   - a quotation: every `quote:` is the whole text of its `source_lines`, cut by
#     script from .cache/slsa-vsa-1-2.txt (whitespace collapsed; bin/check-quotes
#     verifies each one);
#   - a requirement id: a selector (a source line and a phrase of the requirement's
#     text) is resolved against ../requirements.yaml and the build RAISES when it
#     matches zero or several entries (a split parent whose children match is
#     skipped). Every resolved pair is printed with --pairs for reading.
# Re-run after the requirements lane changes ../requirements.yaml: an id that moved
# is caught here, not by a reader.
import json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
DIST = os.path.dirname(HERE)
REC = os.path.dirname(DIST)
ROOT = os.path.abspath(os.path.join(REC, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "bin"))
from _yaml import parse  # noqa: E402

RID = "slsa-vsa-1-2"
TXT = os.path.join(ROOT, ".cache", RID + ".txt")
OUT = os.path.join(DIST, "messages.yaml")
TL = open(TXT, encoding="utf-8").read().split("\n")
REQS = parse(open(os.path.join(DIST, "requirements.yaml"), encoding="utf-8").read())["requirements"]


def lines_of(v):
    a, _, b = str(v).strip().partition("-")
    return int(a), int(b or a)


def collapse(s):
    return " ".join(s.split())


def Q(spec):
    """{source_lines, quote} for 'a' or 'a-b': the whole text of those lines."""
    a, b = lines_of(spec)
    q = collapse(" ".join(TL[a - 1:b]))
    assert q and TL[a - 1].strip() and TL[b - 1].strip(), "blank end line in " + spec
    return {"source_lines": spec, "quote": q}


PAIRS = []
STATED = [r for r in REQS if r.get("source_lines")]      # inferred entries have no lines
INFERRED = [r for r in REQS if not r.get("source_lines")]


def rid(line, phrase):
    """The one requirement whose source_lines contain `line` and whose text contains
    `phrase`; with line None, the one INFERRED requirement (no source lines) whose
    text contains `phrase`. A split parent is dropped when one of its children also
    matches, so the most specific statement is cited. Raises on zero or several.
    (Pass 1 dropped every split parent unconditionally and read source_lines from
    every entry: written before the requirements lane had added split children or
    inferred entries, it raised on both once they existed. Fixed by pass 2.)"""
    pool = INFERRED if line is None else STATED
    hits = []
    for r in pool:
        if line is not None:
            a, b = lines_of(r["source_lines"])
            if not a <= line <= b:
                continue
        if collapse(phrase) in collapse(r["text"]):
            hits.append(r)
    kids = {h.get("split_of") for h in hits if h.get("split_of")}
    hits = [h for h in hits if h["id"] not in kids]
    if len(hits) != 1:
        raise SystemExit("selector L%s %r matched %d requirements: %s" % (line, phrase, len(hits), [h["id"] for h in hits]))
    PAIRS.append((hits[0]["id"], "L%d" % line if line else "inferred", phrase, hits[0].get("source_lines") or "-",
                  collapse(hits[0]["text"])[:100]))
    return hits[0]["id"]


PARENTS = {r.get("split_of") for r in REQS if r.get("split_of")}


def covered(line):
    """ids of stated requirements whose source_lines contain this line, split parents
    left out (every split parent is partitioned by its children); build-time snapshot."""
    return [r["id"] for r in STATED if lines_of(r["source_lines"])[0] <= line <= lines_of(r["source_lines"])[1]
            and r["id"] not in PARENTS]


# selectors: (line, phrase), or (None, phrase) for an inferred entry. Names are what
# the messages below cite.
SEL = {
    "predicate-type": (14, '"predicateType": "https://slsa.dev/verification_summary/v1"'),
    "predicate-type-always": (17, "Always use the above string for `predicateType`"),
    "predicate-type-resolves": (18, "will always resolve to the latest"),
    "vsa-model": (42, "A Verification Summary Attestation (VSA) is an attestation"),
    "dep-methods": (51, "The verifier does this by either a)"),
    "type-constant": (66, '"_type": "https://in-toto.io/Statement/v1",'),
    "subject-digest-request": (69, "<digest-in-request>"),
    "resourceUri-request": (83, "<artifact-URI-in-request>"),
    "parsing-rules": (108, "This predicate follows the in-toto attestation"),
    "ignore-unrecognized": (110, "Consumers MUST ignore unrecognized fields"),
    "major-version": (111, "includes the major version number"),
    "minor-compatible": (113, "Minor version changes are always backwards compatible"),
    "minor-same-type": (113, "Such changes do not update the `predicateType`"),
    "extension-uris": (115, "Producers MAY add extension fields"),
    "statement-fields": (119, "For a description of the other top-level fields"),
    "verifier-required": (123, "`verifier` _object, required_"),
    "verifier-desc": (125, "Identifies the entity that performed the verification"),
    "verifier-identity": (127, "The identity MUST reflect the trust base"),
    "verifier-pairs": (130, "Consumers MUST accept only specific (signer, verifier) pairs"),
    "verifier-even-if-implicit": (135, "The field is required, even if it is implicit from the signer"),
    "verifier-id-required": (140, "`verifier.id` _string ([TypeURI]), required_"),
    "verifier-id-desc": (142, "URI indicating the verifier"),
    "verifier-version-optional": (145, "`verifier.version` _map (string->string), optional_"),
    "verifier-version-desc": (147, "Map of names of components of the verification platform"),
    "timeVerified-optional": (150, "`timeVerified` _string ([Timestamp]), optional_"),
    "timeVerified-desc": (152, "Timestamp indicating what time the verification occurred"),
    "resourceUri-required": (155, "`resourceUri` _string ([ResourceURI]), required_"),
    "resourceUri-desc": (157, "URI that identifies the resource associated"),
    "resourceUri-set": (159, "SHOULD be set to the URI from which the producer expects"),
    "resourceUri-oob": (162, "MUST communicate the"),
    "policy-required": (167, "`policy` _object ([ResourceDescriptor]), required_"),
    "policy-desc": (169, "Describes the policy that the `subject` was verified against"),
    "policy-uri": (171, "MUST contain a `uri`"),
    "policy-digest": (172, "SHOULD contain a `digest`"),
    "inputs-optional": (175, "`inputAttestations` _array ([ResourceDescriptor]), optional_"),
    "inputs-desc": (177, "The collection of attestations that were used"),
    "inputs-absent": (180, "MAY be absent"),
    "inputs-all": (181, "MUST contain information on _all_"),
    "inputs-digest": (184, "MUST contain a `digest` of the attestation"),
    "inputs-uri": (184, "SHOULD contains a"),
    "verificationResult-required": (188, "`verificationResult` _string, required_"),
    "verificationResult-values": (190, "to indicate if the artifact passed or failed"),
    "verifiedLevels-required": (193, "`verifiedLevels` _array ([SlsaResult]), required_"),
    "verified-levels": (195, "Indicates the highest level of each track"),
    "verified-one-per-track": (199, "MUST NOT include more than one level per SLSA track"),
    "levels-imply": (200, "level implies all levels below it"),
    "dependencyLevels-optional": (205, "`dependencyLevels` _object, optional_"),
    "dependencyLevels-count": (207, "A count of the dependencies at each SLSA level"),
    "dependencyLevels-map": (209, "Map from [SlsaResult] to the number"),
    "dep-absent-zero": (210, "MUST be interpreted as reporting _0_ dependencies"),
    "dep-empty-null": (212, "A set but empty `dependencyLevels` object means"),
    "dep-count-once": (216, "MUST count each dependency only once per SLSA track"),
    "dep-count-example": (217, "if a dependency meets `SLSA_BUILD_LEVEL_2`"),
    "slsaVersion-optional": (222, "`slsaVersion` _string, optional_"),
    "slsaVersion-form": (224, "Indicates the version of the SLSA specification"),
    "slsaVersion-default": (225, "If unset, the default is"),
    "verify-steps": (281, "Verification MUST include the following steps"),
    "step1": (283, "Verify the signature on the VSA envelope using the preconfigured roots"),
    "step2": (287, "Verify the statement's `subject` matches the digest"),
    "step3": (290, "Verify that the `predicateType` is"),
    "step4": (294, "Verify that the `verifier` matches the public key"),
    "step5": (298, "Verify that the value for `resourceUri` in the VSA matches"),
    "step6": (302, "Verify that the value for `verificationResult` is `PASSED`"),
    "step7": (305, "Verify that `verifiedLevels` contains the expected value"),
    "verify-optional": (308, "Verification MAY additionally contain the following step"),
    "step-optional": (310, "(Optional) Verify additional fields"),
    "verifier-compromise": (317, "VSA consumers SHOULD carefully consider which verifiers"),
    "slsaresult-def": (375, "The result of evaluating an artifact"),
    "slsaresult-should": (376, "SHOULD be"),
    "slsaresult-level": (378, "level the referenced artifact qualifies for"),
    "slsaresult-unevaluated": (380, "_LEVEL_UNEVALUATED` if the VSA issuer"),
    "slsaresult-failed": (390, "`FAILED` (Indicates policy evaluation failed)"),
    "slsaresult-implies": (392, "Note that each SLSA level implies the levels below it in the same track"),
    "slsaresult-custom-may": (396, "Users MAY use custom values here"),
    "slsaresult-custom": (396, "MUST NOT use custom values starting with"),
    "inf-step4-match": (None, "In step 4 the consumer compares predicate.verifier.id"),
    "inf-level-match": (None, "A consumer whose policy requires track T at level N or higher"),
    "inf-signs": (None, "A VSA producer signs the VSA, in an envelope"),
    "inf-dep-minimum": (None, "A consumer enforcing a minimum level N in track T"),
    "inf-dep-unset": (None, "A producer that makes no claim about the artifact"),
    "inf-counts": (None, "Each dependencyLevels value is a non-negative integer count"),
    "inf-failed-tie": (None, "verificationResult is FAILED exactly when verifiedLevels carries FAILED"),
    "inf-expected-uri": (None, "The consumer takes the expected resourceUri for step 5"),
    "inf-subjects": (None, "A producer puts several artifacts in one VSA"),
}


def C(*names):
    return [rid(*SEL[n]) for n in names]


# ---- the messages -----------------------------------------------------------
def F(name, path, typ, required, enc, declared, described=None, cb=(), note=None, basis=None,
      step=None, extra=None):
    d = {"name": name, "json_path": path, "type": typ, "required": required}
    if basis:
        d["required_basis"] = basis
    d["encoding"] = enc
    d["declared"] = Q(declared)
    if described:
        d["described"] = Q(described)
    if step:
        d["consumer_step"] = dict(Q(step[1]), step=step[0])
    d["constrained_by"] = C(*cb)
    if not cb:
        d["constrained_by_note"] = note or "no BCP 14 keyword binds this field in the source; its type and required/optional word are the declaration quoted above"
    elif note:
        d["notes"] = [note]
    if extra:
        d.update(extra)
    return d


OUTSIDE_STMT = "required is true because section 3 lists it among the standard attestation fields; the in-toto Statement ([Statement], outside this source) is what makes it so"
STR = "JSON string"
OBJ = "JSON object"

M = []
M.append({
    "id": "MSG-01", "name": "VSA Statement", "locator": "§3",
    "kind": "json-object (in-toto Statement)",
    "encoding": "JSON object. The source writes it as jsonc members without the enclosing braces (L64-103) and never names the encoding; the in-toto Statement it instantiates is outside this source",
    "summary": "The in-toto Statement that carries a VSA: standard attestation fields, the predicate type, and the predicate.",
    "declared": Q("66-74"),
    "constrained_by": C("parsing-rules", "ignore-unrecognized", "extension-uris", "statement-fields", "inf-subjects"),
    "fields": [
        F("_type", "_type", STR + " (constant)", True, "JSON string, exactly https://in-toto.io/Statement/v1", "66", cb=("type-constant", "statement-fields"), basis="inferred: " + OUTSIDE_STMT,
          note="the value is the constant printed in the schema block; the Statement version it names is outside this source"),
        F("subject", "subject", "array of objects, each with name and digest (the artifacts verified)", True,
          "JSON array, one or more entries; each entry a JSON object with `name` (string) and `digest` (object of digests)", "67-70",
          described="42-44", cb=("vsa-model", "subject-digest-request", "step2", "inf-subjects"), basis="inferred: " + OUTSIDE_STMT + "; at least one entry is read from 'one or more software artifacts' (L43)",
          step=(2, "287-288"), note="the consumer matches a subject entry against the artifact's digest (§5 step 2, R-0068); how a digest set matches is not stated (SD-26), nor what the predicate says of each of several subjects (SD-1, R-0092)"),
        F("predicateType", "predicateType", STR + " (constant)", True, "JSON string, exactly https://slsa.dev/verification_summary/v1", "73",
          described="10-20", cb=("predicate-type", "predicate-type-always", "predicate-type-resolves", "major-version", "minor-same-type", "step3"), basis="inferred: " + OUTSIDE_STMT,
          step=(3, "290-292"), note="§5 step 3 compares exactly this string (R-0069); a producer writes it, not the address of the page (R-0017), which resolves to the latest minor version (R-0018); it carries the major version only (R-0025, R-0027)"),
        F("predicate", "predicate", "object (MSG-02)", True, OBJ + " (MSG-02)", "74", cb=("parsing-rules", "ignore-unrecognized", "extension-uris"),
          basis="inferred: " + OUTSIDE_STMT, note="the §3.1 parsing rules are stated of this predicate (R-0024, L108)"),
    ],
})
M.append({
    "id": "MSG-02", "name": "VSA predicate", "locator": "§3, §3.2",
    "kind": "json-object (predicate)",
    "encoding": "JSON object, the value of `predicate` in MSG-01",
    "summary": "What the verifier says: who verified, against what policy, from which attestations, with what result and at which levels.",
    "declared": Q("74-103"),
    "constrained_by": C("parsing-rules", "ignore-unrecognized", "extension-uris", "verify-optional", "step-optional"),
    "notes": ["R-0012 permits, and R-0074 is, the consumer's optional check of further fields (L308-311); no step reads policy, and nothing says what a consumer does with a VSA that lacks a required field (SD-27)"],
    "fields": [
        F("verifier", "predicate.verifier", "object (MSG-03)", True, OBJ + " (MSG-03)", "123", described="125-137",
          cb=("verifier-required", "verifier-desc", "verifier-identity", "verifier-pairs", "verifier-even-if-implicit", "step4", "inf-step4-match", "verifier-compromise"), step=(4, "294-296"),
          note="present even where the signer implies the verifier (R-0031)"),
        F("timeVerified", "predicate.timeVerified", "string ([Timestamp])", False, "JSON string; the Timestamp format is defined in in-toto, outside this source", "150", described="152",
          cb=("timeVerified-optional", "timeVerified-desc"), note="optional since 1.1 (change history L412; SD-23); the schema block shows it as <TIMESTAMP> (L82)"),
        F("resourceUri", "predicate.resourceUri", "string ([ResourceURI])", True, "JSON string; the ResourceURI format is defined in in-toto, outside this source", "155", described="157-164",
          cb=("resourceUri-required", "resourceUri-desc", "resourceUri-set", "resourceUri-oob", "resourceUri-request", "step5", "inf-expected-uri"), step=(5, "298-300"),
          note="which producer sets it is not said (SD-21); the schema placeholder names a request the page never defines (SD-3)"),
        F("policy", "predicate.policy", "object ([ResourceDescriptor]) (MSG-04)", True, OBJ + " (MSG-04)", "167", described="169-172",
          cb=("policy-required", "policy-desc", "policy-uri", "policy-digest")),
        F("inputAttestations", "predicate.inputAttestations", "array ([ResourceDescriptor]) (MSG-05)", False, "JSON array of MSG-05 objects", "175", described="177-185",
          cb=("inputs-optional", "inputs-desc", "inputs-absent", "inputs-all", "inputs-digest", "inputs-uri"),
          note="an empty array is defined by neither branch (SD-6)"),
        F("verificationResult", "predicate.verificationResult", "string, PASSED or FAILED", True, 'JSON string, exactly "PASSED" or "FAILED"', "188", described="190",
          cb=("verificationResult-required", "verificationResult-values", "step6", "inf-failed-tie"), step=(6, "302-303"),
          note="the section 5.1 examples call this field `slsaResult` (L336, L360): SD-15"),
        F("verifiedLevels", "predicate.verifiedLevels", "array ([SlsaResult]) (MSG-06)", True, "JSON array of MSG-06 strings", "193", described="195-202",
          cb=("verifiedLevels-required", "verified-levels", "verified-one-per-track", "levels-imply", "step7", "inf-level-match", "inf-failed-tie"), step=(7, "305-306"),
          note="whether FAILED stands alone and how it ties to verificationResult is not said (SD-8)"),
        F("dependencyLevels", "predicate.dependencyLevels", "object, SlsaResult to count (MSG-07)", False, "JSON object (MSG-07); null is read as unset (SD-10)", "205", described="207-219",
          cb=("dependencyLevels-optional", "dependencyLevels-count", "dependencyLevels-map", "dep-absent-zero", "dep-empty-null", "dep-count-once", "dep-count-example", "dep-methods", "inf-dep-unset", "inf-counts", "inf-dep-minimum")),
        F("slsaVersion", "predicate.slsaVersion", "string, <MAJOR>.<MINOR>", False, "JSON string of the form <MAJOR>.<MINOR>, example 1.0", "222", described="224-226",
          cb=("slsaVersion-optional", "slsaVersion-form", "slsaVersion-default"),
          note="it names the SLSA specification version the verifier used; the minor version of this page a VSA follows is named nowhere (SD-23)"),
    ],
})
M.append({
    "id": "MSG-03", "name": "verifier", "locator": "§3.2",
    "kind": "json-object", "encoding": "JSON object; 'an object to allow additional fields in the future' (L136-137)",
    "summary": "Identity of the verifying entity, and optionally the versions of its components.",
    "declared": Q("123"), "constrained_by": C("verifier-required", "verifier-desc", "verifier-identity", "verifier-pairs", "verifier-even-if-implicit", "verifier-compromise"),
    "fields": [
        F("id", "predicate.verifier.id", "string ([TypeURI])", True, "JSON string, a URI", "140", described="142",
          cb=("verifier-id-required", "verifier-id-desc", "verifier-identity", "verifier-pairs", "inf-step4-match"),
          note="the identity the pair rule (R-0004) and §5 step 4 (R-0070, read through R-0082) bind; how an identity matches a key is not said (SD-13)"),
        F("version", "predicate.verifier.version", "map (string->string)", False, "JSON object whose values are strings: component name to version", "145", described="147",
          cb=("verifier-version-optional", "verifier-version-desc"), note="added in 1.1 (change history L410)"),
    ],
})
M.append({
    "id": "MSG-04", "name": "policy", "locator": "§3.2",
    "kind": "json-object ([ResourceDescriptor] as used)",
    "encoding": "JSON object; the [ResourceDescriptor] it instantiates is outside this source (in-toto), only uri and digest are named here",
    "summary": "The policy the subject was verified against: where it is and which exact version.",
    "declared": Q("167"), "constrained_by": C("policy-required", "policy-desc", "policy-uri", "policy-digest"),
    "fields": [
        F("uri", "predicate.policy.uri", "string, a URI", True, "JSON string", "84-85", described="171",
          cb=("policy-uri",), basis="source: MUST (L171)", note="schema block L85 shows `\"uri\": \"<URI>\"`"),
        F("digest", "predicate.policy.digest", "object, digest set of the policy data", False, "JSON object of digests ([DigestSet], outside this source)", "86", described="172",
          cb=("policy-digest",), basis="source: SHOULD (L172), so optional for validity", note="made recommended in 1.1 (change history L408-409)"),
    ],
})
M.append({
    "id": "MSG-05", "name": "inputAttestations entry", "locator": "§3.2",
    "kind": "json-object ([ResourceDescriptor] as used)",
    "encoding": "JSON object, one element of predicate.inputAttestations",
    "summary": "One attestation the verifier used: a digest of it and where to fetch it.",
    "declared": Q("88-94"), "constrained_by": C("inputs-all", "inputs-digest", "inputs-uri"),
    "fields": [
        F("digest", "predicate.inputAttestations[].digest", "object, digest set of the attestation data", True, "JSON object of digests ([DigestSet], outside this source)", "91", described="184-185",
          cb=("inputs-digest",), basis="source: MUST (L184)", note="which bytes the digest is taken over is not said (SD-24)"),
        F("uri", "predicate.inputAttestations[].uri", "string, a URI", False, "JSON string", "90", described="184-185",
          cb=("inputs-uri",), basis="source: SHOULD (L184), so optional for validity"),
    ],
})
M.append({
    "id": "MSG-06", "name": "SlsaResult", "locator": "§6",
    "kind": "string (grammar)",
    "encoding": "JSON string: SHOULD take one of the two level shapes (R-0014, R-0076, R-0077); also FAILED (R-0078), the verified properties verifiedLevels may carry (R-0053), and custom values that do not start with SLSA_ (R-0080, R-0081)",
    "summary": "A track level, a track's UNEVALUATED value, FAILED, a verified property or a custom value: the type of the verifiedLevels entries and the dependencyLevels keys.",
    "declared": Q("375-381"),
    "grammar": {
        "level_form": "^SLSA_[A-Z][A-Z0-9_]*_LEVEL_(UNEVALUATED|[0-9]+)$",
        "applies_when": "the string is in the level form, that is it starts with SLSA_ and has _LEVEL either at its end or followed by an underscore",
        "otherwise": "any string: FAILED, a verified property or other SLSA-endorsed value (SLSA_ prefixed, defined outside this source), or a custom value, which MUST NOT start with SLSA_ (R-0081); only SLSA's own list of values tells a forbidden custom value from an endorsed one",
        "derived_in": "schema/slsa-result.derived.schema.json",
        "readings": [
            "the track placeholder is written <TRACK_NAME> at L379 and <TRACK NAME> at L380; underscores are taken",
            "the range of <LEVEL_NUMBER> is not stated; decimal digits, no upper bound, leading zeros admitted",
            "which tracks exist is outside this source",
            "verified properties may sit in verifiedLevels (L196) and are SLSA-endorsed values (L402-404); the v1.2 ones are named SLSA_SOURCE_TWO_PARTY_REVIEWED and SLSA_BUILD_REPRODUCED (SLSA's verified-properties page at ae7fc76, outside this source), so the level grammar cannot apply to every SLSA_ string. Pass 1's grammar applied it to all of them and rejected both",
        ],
    },
    "values_printed": [Q("385"), Q("386"), Q("387"), Q("388"), Q("389"), Q("390")],
    "constrained_by": C("slsaresult-def", "slsaresult-should", "slsaresult-level", "slsaresult-unevaluated", "slsaresult-failed", "slsaresult-implies", "slsaresult-custom-may", "slsaresult-custom", "verified-levels"),
    "fields": [],
    "notes": [
        "each level implies the levels below it in the same track (R-0055, R-0079), so a verifiedLevels array carries only the highest (R-0054)",
        "SHOULD, not MUST (R-0014): a producer may use another string, but a custom value may not start with SLSA_ (R-0080, R-0081)",
        "the shapes omit FAILED and the verified properties, and spell their placeholder two ways (SD-17)",
    ],
})
M.append({
    "id": "MSG-07", "name": "dependencyLevels", "locator": "§3.2",
    "kind": "json-object (map)", "encoding": "JSON object: SlsaResult (MSG-06) key to non-negative integer count",
    "summary": "Number of the artifact's transitive dependencies verified at each level.",
    "declared": Q("97-101"), "constrained_by": C("dependencyLevels-map", "dep-absent-zero", "dep-empty-null", "dep-count-once", "dep-count-example", "inf-counts"),
    "fields": [
        F("<SlsaResult>", "predicate.dependencyLevels.<key>", "integer (<Int>)", False, "JSON number, an integer; the key is an MSG-06 string", "98", described="209-211",
          cb=("dependencyLevels-map", "dep-absent-zero", "dep-count-once", "inf-counts"), basis="an absent key means 0 (L210-211)",
          note="non-negative is inferred (R-0089): it is a count of dependencies (R-0057); the schema block gives only <Int> (L98)"),
    ],
    "notes": [
        "an empty object asserts no dependency at all, an unset or null one claims nothing (R-0060, R-0088; null against the object type: SD-10)",
        "each dependency is counted once per track at its highest level (R-0061, R-0062); a track with no key reads as zero (SD-22); adding dependency VSAs' counts counts a shared dependency more than once (SD-20)",
    ],
})
M.append({
    "id": "MSG-08", "name": "VSA envelope", "locator": "§5",
    "kind": "signed envelope (not defined here)",
    "encoding": "not defined in this source: it speaks of 'the VSA envelope' and of preconfigured roots of trust only",
    "summary": "What carries the signature that consumers verify first. The source defines no wire format for it.",
    "declared": Q("283-285"), "constrained_by": C("step1", "step4", "inf-signs", "verifier-compromise"),
    "fields": [],
    "notes": [
        "§5 step 1 checks the envelope's signature against the consumer's roots of trust (R-0067); step 4 ties the verifier to the key that verified it (R-0070, R-0082); that a producer signs is inferred (R-0086)",
        "which envelope format (and which signature algorithm) is outside this source",
    ],
})

EXTERNAL = [
    {"name": "Statement", "kind": "in-toto message", "link_footer": Q("428"), "used_by": "MSG-01"},
    {"name": "ResourceDescriptor", "kind": "in-toto message", "link_footer": Q("427"), "used_by": "MSG-04, MSG-05"},
    {"name": "DigestSet", "kind": "in-toto field type", "link_footer": Q("425"), "used_by": "MSG-01 subject, MSG-04, MSG-05",
     "note": "defined in the link footer (L425) but not referenced by a [DigestSet] in the text"},
    {"name": "TypeURI", "kind": "in-toto field type", "link_footer": Q("430"), "used_by": "MSG-03 id"},
    {"name": "Timestamp", "kind": "in-toto field type", "link_footer": Q("429"), "used_by": "MSG-02 timeVerified"},
    {"name": "ResourceURI", "kind": "in-toto field type", "link_footer": Q("426"), "used_by": "MSG-02 resourceUri"},
    {"name": "parsing rules", "kind": "in-toto rules", "link_footer": Q("432"), "used_by": "MSG-01, MSG-02 (section 3.1)"},
    {"name": "SLSA Provenance", "kind": "SLSA predicate", "link_footer": Q("423"), "used_by": "resolvedDependencies, L53, L178"},
]

# Source defects, under normative.md's canonical ids (pass 2 merged the lanes'
# lists there; its crosswalk maps this lane's old ids, kept here as lane_id).
DEFECTS = [
    {"id": "SD-15", "lane_id": "SD-01", "locator": "§5.1 vs §3.2, §7",
     "summary": "both worked examples test `slsaResult` is PASSED, but the field is verificationResult; the 1.2 change history says the typo was fixed",
     "quote_a": Q("336"), "quote_b": Q("188"), "quote_c": Q("405-406")},
    {"id": "SD-4", "lane_id": "SD-02, SD-03", "locator": "§3 jsonc block, §4 jsonc example",
     "summary": "neither block is JSON even once comments are removed: no enclosing braces in either; the schema block lacks a comma after the policy object and has a trailing comma after its last member, ellipses and unquoted placeholders (<NAME>, <TIMESTAMP>); the example has a trailing comma after the last dependencyLevels entry (L266). A comment-stripped JSON of the example is examples/example-vsa.derived.json",
     "quote_a": Q("87-88"), "quote_b": Q("102"), "quote_c": Q("266")},
    {"id": "SD-17", "lane_id": "SD-04", "locator": "§6",
     "summary": "the track placeholder is <TRACK_NAME> in the first form and <TRACK NAME> (with a space) in the second",
     "quote_a": Q("379"), "quote_b": Q("380")},
    {"id": "SD-18", "lane_id": "SD-05", "locator": "§2 vs §3.2",
     "summary": "the model speaks of a `bundle` of attestations (L44-45) and of `vsa.` field paths; the schema has no bundle, the field is inputAttestations",
     "quote_a": Q("44-45"), "quote_b": Q("175")},
    {"id": "SD-8", "lane_id": "SD-06", "locator": "§3.2 verifiedLevels vs verificationResult",
     "summary": "FAILED can appear both as verificationResult and as an element of verifiedLevels; how they relate (and whether FAILED may sit beside other levels) is not stated",
     "quote_a": Q("190"), "quote_b": Q("195-197")},
    {"id": "SD-10", "lane_id": "SD-07", "locator": "§3.2 dependencyLevels",
     "summary": "typed `object, optional` (L205) yet a null value is given a meaning (L213-214); the schema admits null",
     "quote_a": Q("205"), "quote_b": Q("213-214")},
    {"id": "SD-9", "lane_id": "SD-08", "locator": "§3.2 verifiedLevels, dependencyLevels",
     "summary": "the MUST NOT / MUST count rules are addressed to 'Users', not producers or verifiers",
     "quote_a": Q("199"), "quote_b": Q("216-217")},
    {"id": "SD-14", "lane_id": "SD-09", "locator": "§5.1",
     "summary": "example 1 checks that verifiedLevels `contains` a value, example 2 that it `is` one of two values; field is an array, so `contains one of` is the only workable reading",
     "quote_a": Q("338"), "quote_b": Q("362")},
    {"id": "SD-19", "lane_id": "SD-10", "locator": "§5",
     "summary": "the optional step is numbered 1 again after steps 1-7 (the Markdown restarts the list)",
     "quote_a": Q("310-311")},
]

# keyword-less statements the messages rely on: does any requirement id cover the line?
KEYWORDLESS = [
    ("17-20", "the predicateType string is always used, never the URL bar's"),
    ("106-108", "the predicate follows the in-toto parsing rules"),
    ("111-114", "major version in predicateType; minor changes backwards compatible and monotonic"),
    ("123", "verifier required"), ("135-137", "verifier required even if implicit from the signer"),
    ("140", "verifier.id required"), ("145", "verifier.version optional"), ("150", "timeVerified optional"),
    ("155", "resourceUri required"), ("167", "policy required"), ("175", "inputAttestations optional"),
    ("188", "verificationResult required"), ("190", "verificationResult is PASSED or FAILED"),
    ("193", "verifiedLevels required"), ("200-202", "each level implies those below; one level per track suffices"),
    ("205", "dependencyLevels optional"), ("222", "slsaVersion optional"), ("224-226", "slsaVersion form and default"),
    ("283-306", "the seven verification steps"), ("378-381", "SlsaResult grammar"),
    ("392-394", "each level implies the levels below in the same track"),
]
KW = []
for spec, what in KEYWORDLESS:
    a, b = lines_of(spec)
    ids = sorted({i for n in range(a, b + 1) for i in covered(n)})
    full = all(covered(n) for n in range(a, b + 1))
    KW.append(dict(Q(spec), what=what, covered_by_ids=ids, every_line_covered=full))

DOC = {
    "record": RID, "reviewed_by": "",
    "source_digest": "71adb7cc46a537c5a9b81fa8b14ae11cbc61ac91cc62c66197d1c1da8d92ccb0",
    "source": ".cache/slsa-vsa-1-2.txt (SLSA Verification Summary Attestation v1.2, spec/verification_summary.md, slsa-framework/slsa releases/v1.2 @ ae7fc76, rendered by distilled/render-source.py). Line numbers count in that file; quotations are checked against it with bin/check-quotes.",
    "extracted": "2026-11-17",
    "extracted_by": "FX-1 pass 1 (extract), schema+messages+examples agent, from the source only; pass 2 (verify) rewired constrained_by to the full requirements table and relabelled source_defects to normative.md's canonical ids",
    "applicability": "This document defines one in-toto predicate (the VSA) as a JSON schema block in jsonc, the §3.2 field list, one string grammar (SlsaResult, §6), and the consumer-side verification steps (§5). It uses structures it does not define: the in-toto Statement, ResourceDescriptor, DigestSet, TypeURI, Timestamp, ResourceURI, the signed envelope, and the SLSA track and level definitions.",
    "note": "Conventions. (1) declared, described, consumer_step and every other {source_lines, quote} pair are written by script from the cached source, never typed; a quote is the whole of its lines, whitespace collapsed. (2) constrained_by lists slsa-vsa-1-2#R-NNNN ids resolved by script from distilled/requirements.yaml by a source line and a phrase of the requirement text, or for an inferred entry (which has no lines) by a phrase alone; a split parent is dropped when one of its children matches; the build raises on zero or several matches; every resolved pair was then read (examples/build-messages.derived.py --pairs). Ids are those of requirements.yaml at the time of the build: re-run the script after that file changes. Where constrained_by is empty the entry says why in constrained_by_note. (3) required is the source's own word (L123-222 headings, MUST/SHOULD for sub-members) unless required_basis says inferred. (4) The VSA is a JSON document: the schema block is JSON-shaped jsonc and the source never states an encoding; this is read, not quoted. (5) SD-n marks a defect or tension in the source, quoted as printed and never repaired; the ids are normative.md's canonical ones (its crosswalk maps this lane's pass 1 ids, kept as lane_id). (6) keywordless_statements lists the statements the messages rely on that carry no BCP 14 keyword and says whether a requirement id covers each of their lines at build time.",
    "encoding_rules": [
        {"id": "ENC-01", "rule": "The VSA is a JSON object; the schema block (jsonc) gives member names and placeholder values, with comments and without enclosing braces",
         "locator": "§3", "quote_of_source": Q("74"), "inferred": True,
         "inferred_reason": "the source never names JSON; the in-toto Statement it instantiates is JSON"},
        {"id": "ENC-02", "rule": "Consumers ignore unrecognized fields",
         "locator": "§3.1", "quote_of_source": Q("110"), "constrained_by": C("ignore-unrecognized")},
        {"id": "ENC-04", "rule": "Producers may add extension fields whose names are URIs",
         "locator": "§3.1", "quote_of_source": Q("115"), "constrained_by": C("extension-uris")},
        {"id": "ENC-03", "rule": "Hashes are carried as digest sets (algorithm name to value); the digest set format is in-toto's",
         "locator": "§3", "quote_of_source": Q("69"), "inferred": True,
         "inferred_reason": "the schema block shows `\"digest\": { <digest-in-request> }`; the object-of-algorithm-to-value form is the [DigestSet] of in-toto, outside this source. The example prints {\"sha256\": \"5678...\"} (L236)"},
    ],
    "constants": [
        {"name": "predicateType", "value": "https://slsa.dev/verification_summary/v1", "locators": ["Preamble L13-15", "§3 L73", "§5 step 3 L290-292"], "quote": Q("14"), "constrained_by": C("predicate-type", "predicate-type-always", "step3")},
        {"name": "_type", "value": "https://in-toto.io/Statement/v1", "locators": ["§3 L66"], "quote": Q("66"), "constrained_by": C("type-constant")},
        {"name": "verificationResult values", "value": ["PASSED", "FAILED"], "locators": ["§3.2 L190"], "quote": Q("190"), "constrained_by": C("verificationResult-values", "step6")},
    ],
    "messages": M,
    "external_types": EXTERNAL,
    "source_defects": DEFECTS,
    "keywordless_statements": KW,
}


# ---- YAML emission (block style, every string double-quoted) ----------------
def sc(v):
    if v is True: return "true"
    if v is False: return "false"
    if v is None: return "null"
    if isinstance(v, int): return str(v)
    return json.dumps(v, ensure_ascii=False)


def emit(v, ind=0):
    pad = "  " * ind
    out = []
    if isinstance(v, dict):
        for k, x in v.items():
            if isinstance(x, (dict, list)) and x:
                out.append("%s%s:" % (pad, k)); out += emit(x, ind + 1)
            else:
                out.append("%s%s: %s" % (pad, k, "[]" if x == [] else "{}" if x == {} else sc(x)))
    else:
        for x in v:
            if isinstance(x, dict) and x:
                sub = emit(x, ind + 1)
                out.append("%s- %s" % (pad, sub[0].lstrip()))
                out += sub[1:]
            elif isinstance(x, list) and x:
                raise ValueError("list of lists")
            else:
                out.append("%s- %s" % (pad, sc(x)))
    return out


def build():
    head = "\n".join(emit({k: v for k, v in DOC.items() if k != "messages" and k not in ("external_types", "source_defects", "keywordless_statements", "constants", "encoding_rules")}))
    parts = [head]
    for k in ("encoding_rules", "constants", "messages", "external_types", "source_defects", "keywordless_statements"):
        parts.append("\n".join(emit({k: DOC[k]})))
    return "\n".join(parts) + "\n"


def roundtrip(text):
    """the library's YAML reader must read back every value that was emitted."""
    got = parse(text)

    def same(a, b, p="$"):
        if isinstance(a, dict):
            assert isinstance(b, dict) and list(a) == list(b), "keys differ at %s: %s vs %s" % (p, list(a), list(b) if isinstance(b, dict) else b)
            for k in a: same(a[k], b[k], p + "." + k)
        elif isinstance(a, list):
            assert isinstance(b, list) and len(a) == len(b), "length differs at " + p
            for i, (x, y) in enumerate(zip(a, b)): same(x, y, "%s[%d]" % (p, i))
        elif isinstance(a, bool):
            assert b in (a, "true" if a else "false"), "bool differs at %s: %r vs %r" % (p, a, b)
        elif isinstance(a, int):
            assert b in (a, str(a)), "int differs at %s: %r vs %r" % (p, a, b)
        else:
            assert a == b, "value differs at %s: %r vs %r" % (p, a, b)
    same(DOC, got)


if __name__ == "__main__":
    text = build()
    roundtrip(text)
    if "--pairs" in sys.argv:
        for p in PAIRS:
            print("%s <- %s %r\n    in %s: %s" % p)
    unresolved = [k["source_lines"] for k in KW if not k["every_line_covered"]]
    if "--check" in sys.argv:
        cur = open(OUT, encoding="utf-8").read() if os.path.exists(OUT) else ""
        if cur != text:
            sys.exit("messages.yaml differs from the rebuild; run without --check")
        print("messages.yaml == rebuild (%d ids resolved, %d keyword-less statements, %d without full id coverage)" % (len(PAIRS), len(KW), len(unresolved)))
    else:
        open(OUT, "w", encoding="utf-8").write(text)
        print("wrote %s: %d ids resolved, %d messages, %d keyword-less statements, %d without full id coverage" % (OUT, len(PAIRS), len(M), len(KW), len(unresolved)))

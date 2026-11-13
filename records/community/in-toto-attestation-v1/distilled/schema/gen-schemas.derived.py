#!/usr/bin/env python3
"""DERIVED - not verbatim. Generator for the derived JSON Schemas in this
directory (in-toto-attestation-v1). The source prints NO JSON Schema; every
*.derived.schema.json is this library's machine-checkable rendering of the
prose of spec/v1/*.md (rendering lines are cited in each schema's
`description` and in README.md).

    python3 -I gen-schemas.derived.py [outdir]     # default: this directory

One file, so the shared $defs (DigestSet, TypeURI, ResourceURI, ...) are
written once and emitted into every schema that needs them (a $ref across
files would need a resolver; the checker has none, on purpose).
"""
import json, os, sys

SCHEMA = "https://json-schema.org/draft/2020-12/schema"

# TypeURI / ResourceURI: RFC 3986 URI (has a scheme), "case sensitive string,
# MUST be case normalized as per section 6.2.2.1 of RFC 3986, meaning that the
# scheme and authority MUST be in lowercase" (field_types.md, rendering 645-647,
# 664-666). Scheme lowercase; if "//" follows, the authority (up to the next
# / ? #) has no uppercase letter. Percent-triplet case (also in RFC 3986
# 6.2.2.1) is NOT enforced: the source's "meaning" clause names only scheme
# and authority.
URI_PATTERN = r"^[a-z][a-z0-9+.\-]*:(?:(?!//)|//[^A-Z/?#\s]*(?:[/?#]|$))\S*$"

# Timestamp: RFC 3339 in UTC, the "Z" form (field_types.md, rendering 684-685).
TS_PATTERN = (r"^[0-9]{4}-(?:0[1-9]|1[0-2])-(?:0[1-9]|[12][0-9]|3[01])"
              r"[Tt](?:[01][0-9]|2[0-3]):[0-5][0-9]:(?:[0-5][0-9]|60)"
              r"(?:\.[0-9]+)?Z$")

# base64 where the source says only "base64" without naming an alphabet
# (ResourceDescriptor.content, Envelope.payload, signature.sig): the standard
# or the URL-safe alphabet (one per value, as DSSE allows either), padding
# optional but correct where present. A length that no byte string encodes to
# (one char, five chars, "AA=", "AAA==") is rejected: it is not base64 in
# either alphabet. (Pass 2: the first version, ^[A-Za-z0-9+/_\-]*={0,2}$,
# accepted all of those and mixed alphabets.)
# Written without {n} counts, so no mutant of check-schemas.derived.py turns a
# fixed width into a nested quantifier (catastrophic backtracking).
_B64 = lambda a: ("(?:" + ("[" + a + "]") * 4 + ")*(?:" + ("[" + a + "]") * 2 + "(?:==)?|"
                  + ("[" + a + "]") * 3 + "=?)?")
B64_PATTERN = "^(?:" + _B64("A-Za-z0-9+/") + "|" + _B64("A-Za-z0-9_-") + ")$"

# media type token/token with optional parameters (RFC 2045 shape only).
MIME_PATTERN = r"^[^\s/;]+/[^\s/;]+(?:;.*)?$"

# lowercase hex of a byte string: two digits per byte, so an even, non-zero
# length (pass 2: the first version, ^[0-9a-f]+$, accepted odd lengths, which
# no hex encoding produces and Go's hex.DecodeString rejects).
LOWER_HEX = r"^(?:[0-9a-f][0-9a-f])+$"

# DigestSet, digest_set.md 5.2.1.1: "the NIST names (converting to lowercase and
# replacing - with _) as keys and lowercase hex-encoded values".
STANDARD = ["sha256", "sha224", "sha384", "sha512", "sha512_224", "sha512_256",
            "sha3_224", "sha3_256", "sha3_384", "sha3_512", "shake128",
            "shake256", "blake2b", "blake2s", "ripemd160", "sm3", "gost",
            "sha1", "md5"]
# 5.2.1.3: "The lowercase hex SHA-1 (40 character) or SHA-256 (64 character)"
GIT = ["gitCommit", "gitTree", "gitBlob", "gitTag"]
GIT_PATTERN = r"^(?:[0-9a-f]{40}|[0-9a-f]{64})$"
# 5.2.1.2 dirHash: sha256 over the listing, "output in lowercase hexadecimal".
DIRHASH_PATTERN = r"^[0-9a-f]{64}$"

# NOT stated by the source: output lengths from the algorithm definitions, for
# the algorithms with ONE fixed output size. Used only by the *.lengths schema.
# The Go and Rust bindings check 12 of these 14 (not ripemd160 or sm3), plus
# 20 bytes for every git* key and 32 for dirHash (go/v1/resource_descriptor.go
# HexLength, rust/src/hash_algorithm.rs hex_len).
LENGTHS = {"md5": 32, "sha1": 40, "sha224": 56, "sha256": 64, "sha384": 96,
           "sha512": 128, "sha512_224": 56, "sha512_256": 64, "sha3_224": 56,
           "sha3_256": 64, "sha3_384": 96, "sha3_512": 128, "ripemd160": 40,
           "sm3": 64}


def digest_set(lengths=False):
    props = {}
    for a in STANDARD:
        if lengths and a in LENGTHS:
            props[a] = {"type": "string", "pattern": f"^[0-9a-f]{{{LENGTHS[a]}}}$"}
        else:
            props[a] = {"type": "string", "pattern": LOWER_HEX}
    for a in GIT:
        props[a] = {"type": "string", "pattern": GIT_PATTERN}
    props["dirHash"] = {"type": "string", "pattern": DIRHASH_PATTERN}
    return {"type": "object", "minProperties": 1, "properties": props,
            "additionalProperties": {"type": "string"}}


def resource_descriptor():
    return {
        "type": "object",
        "properties": {
            "name": {"type": "string"},
            "uri": {"$ref": "#/$defs/ResourceURI"},
            "digest": {"$ref": "#/$defs/DigestSet"},
            "content": {"type": "string", "pattern": B64_PATTERN},
            "downloadLocation": {"$ref": "#/$defs/ResourceURI"},
            "mediaType": {"type": "string", "pattern": MIME_PATTERN},
            "annotations": {"type": "object"},
        },
        "anyOf": [{"required": ["uri"]}, {"required": ["digest"]},
                  {"required": ["content"]}],
        "additionalProperties": True,
    }


def defs(*names, lengths=False):
    d = {}
    if "TypeURI" in names:
        d["TypeURI"] = {"type": "string", "pattern": URI_PATTERN}
    if "ResourceURI" in names:
        d["ResourceURI"] = {"type": "string", "pattern": URI_PATTERN}
    if "Timestamp" in names:
        d["Timestamp"] = {"type": "string", "pattern": TS_PATTERN}
    if "DigestSet" in names:
        d["DigestSet"] = digest_set(lengths)
    if "ResourceDescriptor" in names:
        d["ResourceDescriptor"] = resource_descriptor()
    return d


def hdr(name, title, desc):
    return {"$schema": SCHEMA,
            "$id": f"urn:library:in-toto-attestation-v1:{name}.derived",
            "title": title,
            "description": "DERIVED - not verbatim. " + desc}


def build():
    out = {}
    s = hdr("statement", "in-toto Statement v1 (derived)",
            "The source prints a template, not a schema (statement.md 3.1, "
            "rendering 164-175); this is the library's rendering of 3.2 "
            "(rendering 180-221). subject elements need digest (\"Each element MUST have digest set\"); predicate is optional. "
            "Unknown fields are allowed: v1 README 2.2, 'Consumers MUST "
            "ignore unrecognized fields'.")
    s.update({
        "type": "object",
        "required": ["_type", "subject", "predicateType"],
        "properties": {
            "_type": {"const": "https://in-toto.io/Statement/v1"},
            "subject": {"type": "array",
                        "items": {"$ref": "#/$defs/ResourceDescriptor",
                                  "required": ["digest"]}},
            "predicateType": {"$ref": "#/$defs/TypeURI"},
            "predicate": {"type": "object"},
        },
        "additionalProperties": True,
        "$defs": defs("TypeURI", "ResourceURI", "DigestSet", "ResourceDescriptor"),
    })
    out["statement"] = s

    r = hdr("resource-descriptor", "in-toto ResourceDescriptor (derived)",
            "resource_descriptor.md 4.1-4.2 (rendering 240-330): all fields "
            "optional except that one of uri, digest, content MUST be present.")
    r.update(resource_descriptor())
    r["$defs"] = defs("ResourceURI", "DigestSet")
    out["resource-descriptor"] = r

    d = hdr("digest-set", "in-toto DigestSet (derived)",
            "digest_set.md 5.1-5.2 (rendering 420-565): JSON object, algorithm "
            "name to string; the 19 standard names and gitCommit/gitTree/"
            "gitBlob/gitTag/dirHash carry lowercase hex; any other key is a "
            "custom algorithm with an identifier-specific string. One or "
            "more entries.")
    d.update(digest_set(False))
    out["digest-set"] = d

    dl = hdr("digest-set-lengths", "in-toto DigestSet with algorithm output lengths (derived)",
             "digest-set plus the output length of each single-size algorithm. "
             "The source states NO lengths for the standard algorithms; these "
             "come from the algorithm definitions. The Go and Rust bindings "
             "check 12 of the 14 (not ripemd160 or sm3).")
    dl.update(digest_set(True))
    out["digest-set-lengths"] = dl

    f = hdr("field-types", "in-toto field types (derived)",
            "field_types.md 6.1-6.3 (rendering 637-690): validate against "
            "#/$defs/ResourceURI, #/$defs/TypeURI or #/$defs/Timestamp.")
    f["$defs"] = defs("ResourceURI", "TypeURI", "Timestamp")
    out["field-types"] = f

    e = hdr("envelope", "in-toto Envelope, DSSE as used (derived)",
            "envelope.md 8.1-8.2 (rendering 748-798) plus docs/validation.md "
            "(rendering 1137-1141) for the DSSE field names signature.keyid "
            "and signature.sig (the DSSE v1.0 text itself is not in the "
            "source). payloadType is application/vnd.in-toto+json or "
            "application/vnd.in-toto.<predicate>+json; payload is base64.")
    e.update({
        "type": "object",
        "required": ["payloadType", "payload", "signatures"],
        "properties": {
            "payloadType": {"type": "string",
                            "pattern": r"^application/vnd\.in-toto(?:\.[^\s/+]+)?\+json$"},
            "payload": {"type": "string", "pattern": B64_PATTERN},
            "signatures": {"type": "array",
                           "items": {"type": "object",
                                     "required": ["sig"],
                                     "properties": {"keyid": {"type": "string"},
                                                    "sig": {"type": "string", "pattern": B64_PATTERN}}}},
        },
        "additionalProperties": True,
    })
    out["envelope"] = e

    b = hdr("bundle-line", "in-toto Bundle line = a recognized Envelope (derived)",
            "bundle.md 9.1 (rendering 876-885): 'Each line within a Bundle "
            "SHOULD be an Envelope. Consumers MUST ignore unrecognized "
            "lines.' A line that fails this schema is an UNRECOGNIZED line, "
            "to be ignored, never an error. payloadType is any string "
            "(application/vnd.novulz+cbor is a bundle example).")
    b.update({
        "type": "object",
        "required": ["payloadType", "payload", "signatures"],
        "properties": {
            "payloadType": {"type": "string"},
            "payload": {"type": "string", "pattern": B64_PATTERN},
            "signatures": {"type": "array", "items": {"type": "object"}},
        },
        "additionalProperties": True,
    })
    out["bundle-line"] = b
    return out


def main():
    outdir = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.abspath(__file__))
    for name, sch in build().items():
        p = os.path.join(outdir, f"{name}.derived.schema.json")
        with open(p, "w") as fh:
            json.dump(sch, fh, indent=2, ensure_ascii=False)
            fh.write("\n")
        print("wrote", p)


if __name__ == "__main__":
    main()

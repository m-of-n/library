---
record: secure-systems-lab-dsse
kind: normative
title: "secure-systems-lab-dsse — normative statements"
extracted: "2026-10-08"
reviewed_by: ""
---

<!-- Verbatim normative statements of DSSE protocol v1.0.2 at commit
     1d3370f, in source order: protocol.md (P1-P12), envelope.md (E1-E9),
     hypothetical_signature_attack.ipynb (N1-N3). Blockquotes and fenced
     blocks delimit verbatim text; everything outside them is structure
     (headings, locators, labels) only. No analysis here — see design-notes.md.
     24 statements, 9 of which carry a BCP 14 keyword. DSSE declares no BCP 14
     boilerplate section; keywords are used in uppercase throughout and are
     read as BCP 14 on that basis. -->

# DSSE — normative statements

## protocol.md (v1.0.2, 10 May 2024)

### P1 — Parameters, with authentication status · `protocol.md` §Parameters

> | Name            | Type   | Required | Authenticated |
> | --------------- | ------ | -------- | ------------- |
> | SERIALIZED_BODY | bytes  | Yes      | Yes           |
> | PAYLOAD_TYPE    | string | Yes      | Yes           |
> | KEYID           | string | No       | No            |

### P2 — SERIALIZED_BODY · `protocol.md` §Parameters

> SERIALIZED_BODY: Arbitrary byte sequence to be signed.

### P3 — PAYLOAD_TYPE · `protocol.md` §Parameters — SHOULD ×5, MAY ×1

> PAYLOAD_TYPE: Opaque, case-sensitive string that uniquely and unambiguously
> identifies how to interpret `payload`. This includes both the encoding
> (JSON, CBOR, etc.) as well as the meaning/schema. To prevent collisions, the
> value SHOULD be either:
>
> *   [Media Type](https://www.iana.org/assignments/media-types/), a.k.a. MIME
>     type or Content Type
>     *   Example: `application/vnd.in-toto+json`.
>     *   IMPORTANT: This SHOULD be an application-specific type describing
>         both encoding and schema, NOT a generic type like
>         `application/json`. The problem with generic types is that two
>         different applications could use the same encoding (e.g. JSON) but
>         interpret the payload differently.
>     *   SHOULD be lowercase.
> *   [URI](https://tools.ietf.org/html/rfc3986)
>     *   Example: `https://example.com/MyMessage/v1-json`.
>     *   SHOULD resolve to a human-readable description but MAY be
>         unresolvable.
>     *   SHOULD be case-normalized (section 6.2.2.1)

### P4 — KEYID · `protocol.md` §Parameters — MUST NOT

> KEYID: Optional, unauthenticated hint indicating what key and algorithm was
> used to sign the message. As with Sign(), details are agreed upon
> out-of-band by the signer and verifier. It **MUST NOT** be used for security
> decisions; it may only be used to narrow the selection of possible keys to
> try.

### P5 — PAE · `protocol.md` §Functions

> PAE() is the "Pre-Authentication Encoding", where parameters `type` and
> `body` are byte sequences:

```none
PAE(type, body) = "DSSEv1" + SP + LEN(type) + SP + type + SP + LEN(body) + SP + body
+               = concatenation
SP              = ASCII space [0x20]
"DSSEv1"        = ASCII [0x44, 0x53, 0x53, 0x45, 0x76, 0x31]
LEN(s)          = ASCII decimal encoding of the byte length of s, with no leading zeros
```

### P6 — Sign() is unconstrained · `protocol.md` §Functions

> Sign() is an arbitrary digital signature format. Details are agreed upon
> out-of-band by the signer and verifier. This specification places no
> restriction on the signature algorithm or format.

### P7 — To sign · `protocol.md` §Protocol

> Out of band:
>
> -   Agree on a PAYLOAD_TYPE and cryptographic details, optionally including
>     KEYID.
>
> To sign:
>
> -   Serialize the message according to PAYLOAD_TYPE. Call the result
>     SERIALIZED_BODY.
> -   Sign PAE(UTF8(PAYLOAD_TYPE), SERIALIZED_BODY). Call the result SIGNATURE.
> -   Optionally, compute a KEYID.
> -   Encode and transmit SERIALIZED_BODY, PAYLOAD_TYPE, SIGNATURE, and KEYID,
>     preferably using the recommended [JSON envelope](envelope.md).

### P8 — To verify · `protocol.md` §Protocol

> To verify:
>
> -   Receive and decode SERIALIZED_BODY, PAYLOAD_TYPE, SIGNATURE, and KEYID, such
>     as from the recommended [JSON envelope](envelope.md). Reject if decoding
>     fails.
> -   Optionally, filter acceptable public keys by KEYID.
> -   Verify SIGNATURE against PAE(UTF8(PAYLOAD_TYPE), SERIALIZED_BODY). Reject if
>     the verification fails.
> -   Reject if PAYLOAD_TYPE is not a supported type.
> -   Parse SERIALIZED_BODY according to PAYLOAD_TYPE. Reject if the parsing
>     fails.

Note on flagging: the four `Reject` obligations above are lowercase in the
source and carry no BCP 14 keyword.

### P9 — base64 acceptance · `protocol.md` §Protocol — MUST

> Either standard or URL-safe base64 encodings are allowed. Signers may use
> either, and verifiers **MUST** accept either.

### P10 — Verified bytes are the bytes delivered · `protocol.md` §Protocol — MUST, MUST NOT

> **Important:** Implementations MUST ensure that the same SERIALIZED_BODY that is
> verified is the same sent to the application layer. In particular,
> implementations MUST NOT re-parse the envelope after verification to pull out
> the payload. Failure to adhere to this requirement can lead to security
> vulnerabilities.

### P11 — `(t, n)`-ENVELOPE validity · `protocol.md` §Multi-signature Verification

> Multi-signature enhances the security by allowing multiple signers to sign the
> same payload. The resulting signatures are encoded and transmitted, preferably
> using the recommended [JSON envelope](envelope.md).
>
> A `(t, n)`-ENVELOPE is valid if the enclosed signatures pass the verification
> against at least `t` of `n` unique trusted public keys where `t` is
> application-specific.

### P12 — `(t, n)` verification procedure · `protocol.md` §Multi-signature Verification

> To verify a `(t, n)`-ENVELOPE:
>
> -   Receive and decode SERIALIZED_BODY, PAYLOAD_TYPE, SIGNATURES from ENVELOPE.
>     Reject if decoding fails.
> -   For each (SIGNATURE, KEYID) in SIGNATURES,
>     -   Optionally, filter acceptable public keys by KEYID.
>     -   Verify SIGNATURE against PAE(UTF8(PAYLOAD_TYPE), SERIALIZED_BODY). Skip
>         over if the verification fails.
>     -   Add the accepted public key to the set ACCEPTED_KEYS.

## envelope.md (v1.0.2, 10 May 2024)

### E1 — The JSON envelope · `envelope.md` §Standard JSON envelope

> See [envelope.proto](envelope.proto) for a formal schema. (Protobuf is used only
> to define the schema. JSON is the only recommended encoding.)

```json
{
  "payload": "<Base64(SERIALIZED_BODY)>",
  "payloadType": "<PAYLOAD_TYPE>",
  "signatures": [{
    "keyid": "<KEYID>",
    "sig": "<Base64(SIGNATURE)>"
  }]
}
```

### E2 — Base64 variant · `envelope.md` §Standard JSON envelope

> Base64() is [Base64 encoding](https://tools.ietf.org/html/rfc4648), transforming
> a byte sequence to a unicode string. Either standard or URL-safe encoding is
> allowed.

### E3 — Multiple signatures · `envelope.md` §Multiple signatures — MAY

> An envelope MAY have more than one signature, which is equivalent to separate
> envelopes with individual signatures.

### E4 — Required fields · `envelope.md` §Parsing rules — REQUIRED, MUST

> *   The following fields are REQUIRED and MUST be set, even if empty: `payload`,
>     `payloadType`, `signature`, `signature.sig`.

### E5 — Optional fields · `envelope.md` §Parsing rules — OPTIONAL, MAY, MUST

> *   The following fields are OPTIONAL and MAY be unset: `signature.keyid`.
>     An unset field MUST be treated the same as set-but-empty.

### E6 — Unrecognized fields · `envelope.md` §Parsing rules — MAY, MUST

> *   Producers, or future versions of the spec, MAY add additional fields.
>     Consumers MUST ignore unrecognized fields.

### E7 — Other data structures · `envelope.md` §Other data structures

> The standard envelope is JSON message with an explicit `payloadType`.
> Optionally, applications may encode the signed message in other methods without
> invalidating the signature:
>
> -   An encoding other than JSON, such as CBOR or protobuf.
> -   Use a default `payloadType` if omitted and/or code `payloadType` as a
>     shorter string or enum.

### E8 — No other encoding standardized · `envelope.md` §Other data structures

> At this point we do not standardize any other encoding. If a need arises, we may
> do so in the future.

### E9 — Security considerations · `envelope.md` §Security considerations — MUST, MUST NOT

> The following advisories are relevant to all envelope formats, not just the
> standard JSON envelope.
>
> **Important:** Implementations MUST ensure that the same payload bytes that are
> verified are the ones sent to the application layer. In particular,
> implementations MUST NOT re-parse the envelope after verification to pull out
> the payload. Failure to adhere to this requirement can lead to security
> vulnerabilities.

## hypothetical_signature_attack.ipynb (Lodato, September 2020)

### N1 — Why an authenticated context indicator is required · §Abstract, §Overview

> This proof-of-concept attack shows the need for any signature scheme to have an
> authenticated "context" field indicating how to interpret the payload.

> In any cryptographic signature wrapper, the payload must be unambiguously
> interpreted, such that the signer and verifier are guaranteed to interpret the
> payload identically.

> Instead, the signature wrapper **must** include some authenticated "context"
> indicator that describes how to interpret the payload.
>
> If the signature scheme does *not* include an authenticated context indicator,
> then an attacker can take a legitimate signed message of type X and get the
> victim to verify and interpret it as type Y.

Note on flagging: the notebook's `must` is lowercase in the source. It is a
proof-of-concept document, not a specification.

### N2 — The defect modelled · §Scenario

> * `payloadType`: How to interpret `payload`. One of "JSON", "CBOR", or "Protobuf".
> * `signatures`: Cryptographic signatures over `payload` but **not** `payloadType`. **This is the problem.**

### N3 — The attack · §Outline of attack

> 1. Construct a target payload T in protobuf format that we want the victim to consume.
> 2. Send a carefully crafted build request that results CI/CD returning a signed CBOR-type link file, such that the payload is interpreted as P when type is CBOR but T when type is protobuf.
> 3. Modify the `payloadType` field to say `Protobuf` instead of `CBOR`. This does not invalidate the signature because the `payloadType` is unauthenticated.
> 4. Send the modified link file to the victim. They will interpret the payload as T, even though the CI/CD system intended it to be interpreted as P.

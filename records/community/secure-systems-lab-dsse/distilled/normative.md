---
record: secure-systems-lab-dsse
kind: normative
title: "secure-systems-lab-dsse — normative text"
generated_by: bin/fx1-skeleton
reviewed_by: ""
---

# Normative text

Every normative statement of the five specification files, verbatim, in source order by file and section. Each quotation is a `<!-- q Lx-y -->` marker whose words `bin/check-quotes --render` writes and `bin/check-quotes` verifies against the rendering: no word inside a blockquote was typed. The line under a quotation names the requirements it carries, emitted by script from requirements.yaml: a bare id is a bin/fx1-skeleton BCP 14 sentence; candidate C-NNNN marks a keyword-less sentence promoted from inferred-candidates.yaml; hunted, binding text no candidate caught; split, the children of an entry, which are quoted on their parent, except the PAE block, quoted line by line as its children. Lead-ins, examples and rationale that fix what a rule refers to are quoted as context and say so; context binds nothing. Generated together with requirements.yaml: 110 requirements, of which 33 skeleton, 7 split children, 48 from candidates, 15 hunted and 7 inferred; the inferred quote nothing and are listed after §5. This file holds 123 quotations in its text, 100 carrying requirements and 23 context, and the source defects 50 more (counted by script over the `<!-- q -->` markers, pass 2).

Line numbers are those of `.cache/secure-systems-lab-dsse.txt` (sha256 b5fe6fb2…913247), the rendering by `distilled/render-source.py` of the archive at commit 1d3370f: §1 protocol.md (file line N = rendering line N+3), §2 envelope.md (N+191), §3 envelope.proto (N+282), §4 background.md (N+322), §5 hypothetical_signature_attack.ipynb (decoded cells, L498 on). A quotation's words are the rendering's with whitespace collapsed, so a table or a code block reads as one line here.

## Keyword declaration

None of the five files declares the BCP 14 keywords: no RFC 2119, RFC 8174 or BCP 14 recital and no key-words paragraph occurs anywhere in the rendering. This extraction reads the 36 capitalised keywords as BCP 14 because they are printed in BCP 14 form throughout (capitals, REQUIRED and OPTIONAL as adjectives, MUST NOT and SHOULD NOT as single keywords, bold MUST and MUST NOT in protocol.md). The 11 in background.md §4.3 bind the design of the protocol and of the data structure, not implementations (R-0023 to R-0033). The 30 lowercase and capitalised forms are ordinary English; the reconciliation in requirements.yaml reads each one and places all 36 keywords by line. Among them, the bold lowercase must of the notebook (L533) is the thesis of a worked attack, not a rule.

## §1 protocol.md

<!-- q L6-8 -->
> May 10, 2024 Version 1.0.2

Context, not an entry: the date and version of protocol.md. Candidates here: C-0001 (reject).

<!-- q L10-11 "This" .. "stored." -->
> This document describes the protocol/algorithm for creating and verifying DSSE signatures, independent of how they are transmitted or stored.

R-0034 · hunted, no candidate

Context, not an entry: the cross-reference after it (L11-12), to envelope.md, is C-0002 (reject).

### §1.1 Signature Definition

<!-- q L16-16 -->
> A signature is defined as:

Context: the lead-in of the signature definition below.

<!-- q L19-19 -->
> SIGNATURE = Sign(PAE(UTF8(PAYLOAD_TYPE), SERIALIZED_BODY))

R-0035 · hunted, no candidate

<!-- q L24-28 -->
> Name | Type | Required | Authenticated --------------- | ------ | -------- | ------------- SERIALIZED_BODY | bytes | Yes | Yes PAYLOAD_TYPE | string | Yes | Yes KEYID | string | No | No

R-0036 · candidate C-0003

<!-- q L30-30 -->
> * SERIALIZED_BODY: Arbitrary byte sequence to be signed.

R-0037 · candidate C-0004

<!-- q L32-33 "*" .. "`payload`." -->
> * PAYLOAD_TYPE: Opaque, case-sensitive string that uniquely and unambiguously identifies how to interpret `payload`.

R-0038 · candidate C-0005

<!-- q L33-34 "This" .. "meaning/schema." -->
> This includes both the encoding (JSON, CBOR, etc.) as well as the meaning/schema.

R-0039 · candidate C-0006

<!-- q L34-35 "To" .. "either:" -->
> To prevent collisions, the value SHOULD be either:

R-0001

<!-- q L37-38 -->
> * [Media Type](https://www.iana.org/assignments/media-types/), a.k.a. MIME type or Content Type

R-0040 · candidates C-0007, C-0008

<!-- q L39-39 -->
> * Example: `application/vnd.in-toto+json`.

Context, not an entry: the example of the media-type alternative. Candidates here: C-0009 (reject).

<!-- q L40-42 "*" .. "`application/json`." -->
> * IMPORTANT: This SHOULD be an application-specific type describing both encoding and schema, NOT a generic type like `application/json`.

R-0002

<!-- q L42-44 "The" .. "differently." -->
> The problem with generic types is that two different applications could use the same encoding (e.g. JSON) but interpret the payload differently.

Context, not an entry: the rationale of R-0002. Candidates here: C-0010 (reject).

<!-- q L45-45 -->
> * SHOULD be lowercase.

R-0003

<!-- q L46-46 -->
> * [URI](https://tools.ietf.org/html/rfc3986)

R-0041 · candidate C-0011

<!-- q L47-47 -->
> * Example: `https://example.com/MyMessage/v1-json`.

Context, not an entry: the example of the URI alternative. Candidates here: C-0012 (reject).

<!-- q L48-49 -->
> * SHOULD resolve to a human-readable description but MAY be unresolvable.

R-0004

<!-- q L50-50 -->
> * SHOULD be case-normalized (section 6.2.2.1)

R-0005

<!-- q L52-53 "*" .. "message." -->
> * KEYID: Optional, unauthenticated hint indicating what key and algorithm was used to sign the message.

R-0042 · candidate C-0013

<!-- q L53-54 "As" .. "verifier." -->
> As with Sign(), details are agreed upon out-of-band by the signer and verifier.

R-0043 · candidate C-0014

<!-- q L54-56 "It" .. "try." -->
> It **MUST NOT** be used for security decisions; it may only be used to narrow the selection of possible keys to try.

R-0006

<!-- q L60-61 -->
> * PAE() is the "Pre-Authentication Encoding", where parameters `type` and `body` are byte sequences:

R-0044 · candidate C-0015

The PAE definition, L64-68: R-0045 · hunted, no candidate · split by line into R-0046 to R-0050, quoted below one line each.

<!-- q L64-64 -->
> PAE(type, body) = "DSSEv1" + SP + LEN(type) + SP + type + SP + LEN(body) + SP + body

R-0046 · split_of R-0045

<!-- q L65-65 -->
> + = concatenation

R-0047 · split_of R-0045

<!-- q L66-66 -->
> SP = ASCII space [0x20]

R-0048 · split_of R-0045

<!-- q L67-67 -->
> "DSSEv1" = ASCII [0x44, 0x53, 0x53, 0x45, 0x76, 0x31]

R-0049 · split_of R-0045

<!-- q L68-68 -->
> LEN(s) = ASCII decimal encoding of the byte length of s, with no leading zeros

R-0050 · split_of R-0045

<!-- q L71-71 "*" .. "format." -->
> * Sign() is an arbitrary digital signature format.

R-0051 · candidate C-0016

<!-- q L71-72 "Details" .. "verifier." -->
> Details are agreed upon out-of-band by the signer and verifier.

R-0052 · candidate C-0017

<!-- q L72-73 "This" .. "format." -->
> This specification places no restriction on the signature algorithm or format.

R-0053 · candidate C-0018

<!-- q L75-76 -->
> * UTF8() is [UTF-8 encoding](https://tools.ietf.org/html/rfc3629), transforming a unicode string to a byte sequence.

R-0054 · candidate C-0019

### §1.2 Protocol

<!-- q L80-80 -->
> Out of band:

Context: the lead-in of the out-of-band step; the actor is signer and verifier together.

<!-- q L82-83 -->
> - Agree on a PAYLOAD_TYPE and cryptographic details, optionally including KEYID.

R-0055 · candidate C-0020

<!-- q L85-85 -->
> To sign:

Context: the lead-in of the signer's steps.

<!-- q L87-88 -->
> - Serialize the message according to PAYLOAD_TYPE. Call the result SERIALIZED_BODY.

R-0056 · candidates C-0021, C-0022

<!-- q L89-89 -->
> - Sign PAE(UTF8(PAYLOAD_TYPE), SERIALIZED_BODY). Call the result SIGNATURE.

R-0057 · candidates C-0023, C-0024

<!-- q L90-90 -->
> - Optionally, compute a KEYID.

R-0058 · candidate C-0025

<!-- q L91-92 -->
> - Encode and transmit SERIALIZED_BODY, PAYLOAD_TYPE, SIGNATURE, and KEYID, preferably using the recommended [JSON envelope](envelope.md).

R-0059 · candidate C-0026

<!-- q L94-94 -->
> To verify:

Context: the lead-in of the verifier's steps.

<!-- q L96-97 "-" .. "envelope](envelope.md)." -->
> - Receive and decode SERIALIZED_BODY, PAYLOAD_TYPE, SIGNATURE, and KEYID, such as from the recommended [JSON envelope](envelope.md).

R-0060 · candidate C-0027

<!-- q L97-98 "Reject" .. "fails." -->
> Reject if decoding fails.

R-0061 · candidate C-0028

<!-- q L99-99 -->
> - Optionally, filter acceptable public keys by KEYID.

R-0062 · candidate C-0029

<!-- q L100-100 "-" .. "SERIALIZED_BODY)." -->
> - Verify SIGNATURE against PAE(UTF8(PAYLOAD_TYPE), SERIALIZED_BODY).

R-0063 · candidate C-0030

<!-- q L100-101 "Reject" .. "fails." -->
> Reject if the verification fails.

R-0064 · candidate C-0031

<!-- q L102-102 -->
> - Reject if PAYLOAD_TYPE is not a supported type.

R-0065 · candidate C-0032

<!-- q L103-103 "-" .. "PAYLOAD_TYPE." -->
> - Parse SERIALIZED_BODY according to PAYLOAD_TYPE.

R-0066 · candidate C-0033

<!-- q L103-104 "Reject" .. "fails." -->
> Reject if the parsing fails.

R-0067 · candidate C-0034

<!-- q L106-106 "Either" .. "allowed." -->
> Either standard or URL-safe base64 encodings are allowed.

R-0068 · hunted, no candidate

<!-- q L106-107 "Signers" .. "either." -->
> Signers may use either, and verifiers **MUST** accept either.

R-0007

<!-- q L109-110 "**Important:**" .. "layer." -->
> **Important:** Implementations MUST ensure that the same SERIALIZED_BODY that is verified is the same sent to the application layer.

R-0008

<!-- q L110-112 "In" .. "payload." -->
> In particular, implementations MUST NOT re-parse the envelope after verification to pull out the payload.

R-0009

<!-- q L112-113 "Failure" .. "vulnerabilities." -->
> Failure to adhere to this requirement can lead to security vulnerabilities.

Context, not an entry: the rationale of R-0008 and R-0009.

### §1.3 Multi-signature Verification

<!-- q L117-118 "Multi-signature" .. "payload." -->
> Multi-signature enhances the security by allowing multiple signers to sign the same payload.

Context, not an entry: the rationale of multi-signature envelopes.

<!-- q L118-119 "The" .. "envelope](envelope.md)." -->
> The resulting signatures are encoded and transmitted, preferably using the recommended [JSON envelope](envelope.md).

R-0069 · candidate C-0035

<!-- q L121-123 -->
> A `(t, n)`-ENVELOPE is valid if the enclosed signatures pass the verification against at least `t` of `n` unique trusted public keys where `t` is application-specific.

R-0070 · candidate C-0036

<!-- q L125-125 -->
> To verify a `(t, n)`-ENVELOPE:

Context: the lead-in of the verifier's steps for a multi-signature envelope.

<!-- q L127-127 -->
> - Receive and decode SERIALIZED_BODY, PAYLOAD_TYPE, SIGNATURES from ENVELOPE.

R-0071 · candidate C-0037

<!-- q L128-128 -->
> Reject if decoding fails.

R-0072 · candidate C-0038

<!-- q L129-129 -->
> - For each (SIGNATURE, KEYID) in SIGNATURES,

R-0073 · candidate C-0039

<!-- q L130-130 -->
> - Optionally, filter acceptable public keys by KEYID.

R-0074 · candidate C-0040

<!-- q L131-131 "-" .. "SERIALIZED_BODY)." -->
> - Verify SIGNATURE against PAE(UTF8(PAYLOAD_TYPE), SERIALIZED_BODY).

R-0075 · candidate C-0041

<!-- q L131-132 "Skip" .. "fails." -->
> Skip over if the verification fails.

R-0076 · candidate C-0042

<!-- q L133-133 -->
> - Add the accepted public key to the set ACCEPTED_KEYS.

R-0077 · candidate C-0043

<!-- q L134-135 -->
> - Break if the number of unique keys in ACCEPTED_KEYS is greater or equal to `t`.

R-0078 · candidate C-0044

<!-- q L136-136 -->
> - Reject if the unique keys in ACCEPTED_KEYS is less than `t`.

R-0079 · candidate C-0045

<!-- q L137-137 -->
> - Reject if PAYLOAD_TYPE is not a supported type.

R-0080 · candidate C-0046

<!-- q L138-138 "-" .. "PAYLOAD_TYPE." -->
> - Parse SERIALIZED_BODY according to PAYLOAD_TYPE.

R-0081 · candidate C-0047

<!-- q L138-139 "Reject" .. "fails." -->
> Reject if the parsing fails.

R-0082 · candidate C-0048

### §1.4 Test Vectors

<!-- q L143-144 -->
> See [reference implementation](implementation/signing_spec.py). Here is an example.

Context, not an entry: §1.4 points to a reference implementation outside the sources read and gives one example. Its inputs, PAE, keys and result (L146-179) are fixtures in examples/, recomputed by examples/reproduce.py; the PAE and the result are quoted below as context. The caption of the result (L174) is C-0049 (reject).

<!-- q L161-161 -->
> DSSEv1 29 http://example.com/HelloWorld 11 hello world

Context, not an entry: the PAE of the §1.4 example, 54 bytes; every PAE implementation reproduces it.

<!-- q L177-179 -->
> {"payload": "aGVsbG8gd29ybGQ=", "payloadType": "http://example.com/HelloWorld", "signatures": [{"sig": "A3JqsQGtVsJ2O2xqrI5IcnXip5GToJ3F+FnZ+O88SjtR6rDAajabZKciJTfUiHqJPcIAriEGAHTVeCUjW2JIZA=="}]}

Context, not an entry: the §1.4 result, the one complete envelope in the sources; it has no keyid.

## §2 envelope.md

<!-- q L194-196 -->
> May 10, 2024 Version 1.0.2

Context, not an entry: the date and version of envelope.md. Candidates here: C-0050 (reject).

<!-- q L198-200 -->
> This document describes the recommended data structure for storing DSSE signatures, which we call the "JSON Envelope". For the protocol/algorithm, see [Protocol](protocol.md).

R-0083 · candidate C-0051

Context, not an entry: the quotation runs to L200 because its second sentence, a cross-reference to protocol.md with no candidate, shares L199; R-0083 is the first sentence only.

### §2.1 Standard JSON envelope

<!-- q L204-204 "See" .. "schema." -->
> See [envelope.proto](envelope.proto) for a formal schema.

R-0084 · hunted, no candidate

<!-- q L204-205 "(Protobuf" .. "schema." -->
> (Protobuf is used only to define the schema.

R-0085 · candidate C-0052

<!-- q L205-205 "JSON" .. "encoding.)" -->
> JSON is the only recommended encoding.)

R-0086 · candidate C-0053

<!-- q L207-208 -->
> The standard data structure for storing a signed message is a JSON message of the following form, called the "JSON envelope":

R-0087 · hunted, no candidate

<!-- q L211-218 -->
> { "payload": "<Base64(SERIALIZED_BODY)>", "payloadType": "<PAYLOAD_TYPE>", "signatures": [{ "keyid": "<KEYID>", "sig": "<Base64(SIGNATURE)>" }] }

R-0088 · hunted, no candidate

<!-- q L221-221 -->
> See [Protocol](protocol.md) for a definition of parameters and functions.

Context, not an entry: the placeholders of the template above are the parameters and functions of protocol.md §1.1.

<!-- q L223-224 "Base64()" .. "string." -->
> Base64() is [Base64 encoding](https://tools.ietf.org/html/rfc4648), transforming a byte sequence to a unicode string.

R-0089 · hunted, no candidate

<!-- q L224-225 "Either" .. "allowed." -->
> Either standard or URL-safe encoding is allowed.

R-0090 · hunted, no candidate

### §2.1.1 Multiple signatures

<!-- q L229-230 -->
> An envelope MAY have more than one signature, which is equivalent to separate envelopes with individual signatures.

R-0010 · split: R-0091, R-0092

<!-- q L233-243 -->
> { "payload": "<Base64(SERIALIZED_BODY)>", "payloadType": "<PAYLOAD_TYPE>", "signatures": [{ "keyid": "<KEYID_1>", "sig": "<SIG_1>" }, { "keyid": "<KEYID_2>", "sig": "<SIG_2>" }] }

Context, not an entry: the template of an envelope with two signatures, illustrating the permission of R-0091.

### §2.1.2 Parsing rules

<!-- q L248-249 -->
> * The following fields are REQUIRED and MUST be set, even if empty: `payload`, `payloadType`, `signature`, `signature.sig`.

R-0011

<!-- q L250-250 -->
> * The following fields are OPTIONAL and MAY be unset: `signature.keyid`.

R-0012

<!-- q L251-251 -->
> An unset field MUST be treated the same as set-but-empty.

R-0013

<!-- q L252-252 -->
> * Producers, or future versions of the spec, MAY add additional fields.

R-0014

<!-- q L253-253 -->
> Consumers MUST ignore unrecognized fields.

R-0015

### §2.2 Other data structures

<!-- q L257-257 -->
> The standard envelope is JSON message with an explicit `payloadType`.

R-0093 · hunted, no candidate

<!-- q L258-259 -->
> Optionally, applications may encode the signed message in other methods without invalidating the signature:

R-0094 · candidate C-0054

<!-- q L261-261 -->
> - An encoding other than JSON, such as CBOR or protobuf.

R-0095 · candidate C-0055

<!-- q L262-263 -->
> - Use a default `payloadType` if omitted and/or code `payloadType` as a shorter string or enum.

R-0096 · candidate C-0056

<!-- q L265-266 -->
> At this point we do not standardize any other encoding. If a need arises, we may do so in the future.

Context, not an entry: the scope of §2.2 at the source's date. Candidates here: C-0057 (reject), C-0058 (reject).

### §2.3 Security considerations

<!-- q L270-271 -->
> The following advisories are relevant to all envelope formats, not just the standard JSON envelope.

R-0097 · hunted, no candidate

<!-- q L273-274 "**Important:**" .. "layer." -->
> **Important:** Implementations MUST ensure that the same payload bytes that are verified are the ones sent to the application layer.

R-0016

<!-- q L274-276 "In" .. "payload." -->
> In particular, implementations MUST NOT re-parse the envelope after verification to pull out the payload.

R-0017

<!-- q L276-277 "Failure" .. "vulnerabilities." -->
> Failure to adhere to this requirement can lead to security vulnerabilities.

Context, not an entry: the rationale of R-0016 and R-0017.

## §3 envelope.proto

<!-- q L283-283 -->
> syntax = "proto3";

Context, not an entry: envelope.proto is proto3 (SD-7).

<!-- q L285-285 -->
> package io.intoto;

Context, not an entry: the package of the schema (SD-6).

<!-- q L287-288 -->
> // An authenticated message of arbitrary type. message Envelope {

Context, not an entry: the opening of message Envelope.

<!-- q L289-291 -->
> // Message to be signed. (In JSON, this is encoded as base64.) // REQUIRED. bytes payload = 1;

R-0018

<!-- q L293-295 -->
> // String unambiguously identifying how to interpret payload. // REQUIRED. string payloadType = 2;

R-0019

<!-- q L297-307 -->
> // Signature over: // PAE(type, payload) // Where PAE is defined as: // PAE(type, payload) = "DSSEv1" + SP + LEN(type) + SP + type + SP + LEN(payload) + SP + payload // + = concatenation // SP = ASCII space [0x20] // "DSSEv1" = ASCII [0x44, 0x53, 0x53, 0x45, 0x76, 0x31] // LEN(s) = ASCII decimal encoding of the byte length of s, with no leading zeros // REQUIRED (length >= 1). repeated Signature signatures = 3; }

R-0020

<!-- q L309-309 -->
> message Signature {

Context, not an entry: the opening of message Signature.

<!-- q L310-312 -->
> // Signature itself. (In JSON, this is encoded as base64.) // REQUIRED. bytes sig = 1;

R-0021

<!-- q L314-317 -->
> // *Unauthenticated* hint identifying which public key was used. // OPTIONAL. string keyid = 2; }

R-0022

## §4 background.md

Not normative: §4.1 states the intended use and §4.2 the motivation, a critique of raw signatures, of the old TUF and in-toto scheme, of JWS and of PASETO. Candidates C-0059 to C-0069 (11, all rejected).

### §4.3 Design requirements

<!-- q L361-361 -->
> The [protocol](protocol.md):

R-0098 · hunted, no candidate

<!-- q L363-364 -->
> * MUST reduce the possibility of a client misinterpreting the payload (e.g. interpreting a JSON message as protobuf)

R-0023

<!-- q L365-365 -->
> * MUST support arbitrary payload types (e.g. not just JSON)

R-0024

<!-- q L366-367 -->
> * MUST support arbitrary crypto primitives, libraries, and key management systems (e.g. Tink vs openssl, Google KMS vs Amazon KMS)

R-0025

<!-- q L368-368 -->
> * SHOULD avoid depending on canonicalization for security

R-0026

<!-- q L369-369 -->
> * SHOULD NOT require unnecessary encoding (e.g. base64)

R-0027

<!-- q L370-370 -->
> * SHOULD NOT require the verifier to parse the payload before verifying

R-0028

<!-- q L372-372 -->
> The [data structure](envelope.md):

R-0099 · hunted, no candidate

<!-- q L374-374 -->
> * MUST include both message and signature(s)

R-0029

<!-- q L375-376 -->
> * NOTE: Detached signatures are supported by having the included message contain a cryptographic hash of the external data.

R-0100 · candidate C-0070

<!-- q L377-377 -->
> * MUST support multiple signatures in one structure / file

R-0030

<!-- q L378-379 -->
> * SHOULD discourage users from reading the payload without verifying the signatures

R-0031

<!-- q L380-380 -->
> * SHOULD be easy to parse using common libraries (e.g. JSON)

R-0032

<!-- q L381-381 -->
> * SHOULD support a hint indicating what signing key was used

R-0033

### §4.4 Motivation

<!-- q L403-404 "The" .. "parsing." -->
> The preferred solution is to transmit the encoded byte stream exactly as it was signed, which the verifier verifies before parsing.

R-0101 · hunted, no candidate

The rest of §4.4 is motivation, restated as rules by R-0023, R-0024, R-0026 and R-0028. Candidates C-0071 to C-0078 (8, all rejected).

### §4.5 Reasoning

Not normative: §4.5 gives the reasons for the design (base64 in JSON only, raw bytes signed, payloadType signed, PAE and its DSSEv1 version string, no JSON-only _type field). Candidates C-0079 to C-0106 (28, all rejected). What the reasons explain is stated as rules elsewhere: R-0027, R-0035, R-0049.

### §4.6 Backwards Compatibility

<!-- q L477-482 -->
> Backwards compatibility with the old [in-toto]/[TUF] format will be handled by the application and explained in the corresponding application-specific change proposal, namely [ITE-5](https://github.com/in-toto/ITE/pull/13) for in-toto and via the principles laid out in [TAP-14](https://github.com/theupdateframework/taps/blob/master/tap14.md) for TUF.

R-0102 · candidate C-0107

<!-- q L484-487 -->
> Verifiers can differentiate between the [old](https://github.com/in-toto/specification/blob/d416c1f334ac6b581f75c0fa65125fb434d7a610/in-toto-spec.md#42-file-formats-general-principles) and new envelope format by detecting the presence of the `payload` field (new format) vs `signed` field (old format).

R-0103 · hunted, no candidate

## §5 hypothetical_signature_attack.ipynb

Not normative. The notebook is a worked attack on a signature wrapper whose signatures do not cover payloadType, the confusion R-0023 exists to prevent and PAYLOAD_TYPE inside PAE (R-0035) defeats. It binds nothing, its lowercase must (L529, and in bold at L533) is its thesis, not a rule, and every one of its candidates is rejected: C-0108 to C-0153 (46, all rejected). Its two inconsistencies are editorial (SD-12).

## Inferred requirements (not verbatim)

These entries are in our words and quote nothing; each names what it is derived from in derived_from. R-0104 (§1.1, LEN(s) of a zero-length s); R-0105 (§1.1, authenticated: payloadType and payload, nothing else); R-0106 (§1.2, trusted public keys; the accepted key); R-0107 (§1.2, step order: verify, then parse); R-0108 (§1.2, PAYLOAD_TYPE handed to the application: the one verified); R-0109 (§1.3, signatures with more than one element: verified by §1.3); R-0110 (§2.2, payloadType coded or defaulted: mapped back to the full string for PAE).

## Source defects

Inconsistencies and gaps in the five files themselves. Each quotes the lines it rests on; the prose is ours. This is the record's one canonical list, 20 defects. SD-1 to SD-6 are the source-defect candidates SDC-1 to SDC-6 of messages.yaml, numbered alike and checked here against the source. SD-7 to SD-13 were found by the requirements lane, and five of them (SD-8 to SD-12) independently by the protocol lane too. SD-14 to SD-17 are protocol-lane candidates (SDP-3, SDP-4, SDP-8, SDP-9) and SD-18 and SD-19 the design-notes lane's DN-SD-1 and DN-SD-2, each re-checked against the source before it was taken in (SD-19 by pass 2, which decided DN-SD-2); SD-20 came from pass 2's check of the protocol lane's attacker role. The crosswalk at the end maps every lane's id; one candidate was declined, with its reason. SD-2, SD-9 and SD-18 leave an implementer two incompatible readings; SD-1, SD-7, SD-8, SD-10, SD-11, SD-13, SD-14, SD-15, SD-17 and SD-19 are gaps or ambiguities a validator or verifier must decide; SD-3 to SD-6, SD-12, SD-16 and SD-20 are editorial or terminological, SD-5 with a trap in it.

### SD-1 — §2.1.2: the parsing rules name fields the structure does not have

The parsing rules list `signature` and `signature.sig` among the fields that must be set (R-0011), and `signature.keyid` as optional (R-0012). The structure has no member `signature`: the template (R-0088) and envelope.proto (L306, L312, L316) have `signatures`, an array, with `sig` and `keyid` in each element. Read here as `signatures` and as the `sig` and `keyid` of each element. Read literally, no envelope has a `signature` member and none can meet R-0011; read with `signature` as each element, the `signatures` array itself is missing from the required fields. From messages.yaml SDC-1, extended here to L250. Requirements affected: R-0011, R-0012.

<!-- q L248-249 -->
> * The following fields are REQUIRED and MUST be set, even if empty: `payload`, `payloadType`, `signature`, `signature.sig`.

<!-- q L250-250 -->
> * The following fields are OPTIONAL and MAY be unset: `signature.keyid`.

<!-- q L306-306 -->
> repeated Signature signatures = 3;

### SD-2 — §2.1.2 against §3: whether signatures may be empty

R-0011 asks for its fields to be set even if empty, which, with `signature` read as `signatures` (SD-1), admits an empty array. envelope.proto marks signatures REQUIRED (length >= 1) (R-0020), which forbids one, and envelope.md names envelope.proto the formal schema (R-0084). A validator built from either rejects envelopes the other accepts; messages.yaml's derived schema carries both readings, as Envelope and EnvelopeStrict. An envelope without signatures authenticates nothing, and a verifier with t of 1 or more rejects it (R-0079), so the conflict is one of conformance, not of security, unless t = 0 (SD-10). From messages.yaml SDC-2. Requirements affected: R-0011, R-0020, R-0084.

<!-- q L248-249 -->
> * The following fields are REQUIRED and MUST be set, even if empty: `payload`, `payloadType`, `signature`, `signature.sig`.

<!-- q L305-305 -->
> // REQUIRED (length >= 1).

### SD-3 — §1.1: section 6.2.2.1 of no named document

R-0005 asks a URI PAYLOAD_TYPE to be case-normalized per a section 6.2.2.1 of a document it does not name. The URI item links RFC 3986 (L46), whose section 6.2.2.1 is Case Normalization, and this extraction reads it so (R-0005). From messages.yaml SDC-3. Requirements affected: R-0005.

<!-- q L46-46 -->
> * [URI](https://tools.ietf.org/html/rfc3986)

<!-- q L50-50 -->
> * SHOULD be case-normalized (section 6.2.2.1)

### SD-4 — §1.1: the parameter table lists KEYID but not SIGNATURE

The table of parameters (R-0036) lists SERIALIZED_BODY, PAYLOAD_TYPE and KEYID. SIGNATURE, which §1.2 encodes and transmits with the other three (R-0059) and the template carries as `sig`, is absent, while KEYID, which is not an input of the signature (R-0035), is present. Read as the inputs of the signature, KEYID is out of place; read as what is transmitted, SIGNATURE is missing. Nothing turns on it, since §1.2 and the template name all four. From messages.yaml SDC-4. Requirements affected: R-0036, R-0059.

<!-- q L24-28 -->
> Name | Type | Required | Authenticated --------------- | ------ | -------- | ------------- SERIALIZED_BODY | bytes | Yes | Yes PAYLOAD_TYPE | string | Yes | Yes KEYID | string | No | No

<!-- q L91-92 -->
> - Encode and transmit SERIALIZED_BODY, PAYLOAD_TYPE, SIGNATURE, and KEYID, preferably using the recommended [JSON envelope](envelope.md).

### SD-5 — the signed bytes go by three names, and envelope.proto calls the wrong thing signed

protocol.md calls the signed body SERIALIZED_BODY (R-0037) and the matching PAE parameter body (R-0046), yet defines PAYLOAD_TYPE as saying how to interpret `payload` (R-0038), the JSON member's name; envelope.md and envelope.proto call it payload, and envelope.proto's restatement of PAE writes payload for body (R-0020). Its comment on the payload field calls the payload the message to be signed (L289), while what is signed is the PAE of type and payload, as its comment on signatures says (L297-298) and the protocol defines (R-0035). A reader of envelope.proto alone could sign the payload bytes alone. Editorial, except for that trap. From messages.yaml SDC-5. Requirements affected: R-0037, R-0038, R-0018, R-0020.

<!-- q L30-30 -->
> * SERIALIZED_BODY: Arbitrary byte sequence to be signed.

<!-- q L32-33 "*" .. "`payload`." -->
> * PAYLOAD_TYPE: Opaque, case-sensitive string that uniquely and unambiguously identifies how to interpret `payload`.

<!-- q L289-289 -->
> // Message to be signed. (In JSON, this is encoded as base64.)

<!-- q L297-298 -->
> // Signature over: // PAE(type, payload)

### SD-6 — §3: the generic schema sits in package io.intoto

envelope.proto declares the package io.intoto (L285) for the structure envelope.md presents as DSSE's own recommended one (R-0083), so its fully qualified message names are io.intoto.Envelope and io.intoto.Signature, an in-toto namespace for a scheme meant for any payload (R-0024). The JSON envelope does not depend on the package; code generated from the schema does. From messages.yaml SDC-6. Requirements affected: R-0084, R-0018 to R-0022.

<!-- q L285-285 -->
> package io.intoto;

<!-- q L198-200 -->
> This document describes the recommended data structure for storing DSSE signatures, which we call the "JSON Envelope". For the protocol/algorithm, see [Protocol](protocol.md).

### SD-7 — §2.1.2 against §3: proto3 cannot say set, even if empty

R-0011 asks for payload, payloadType, signatures and sig to be set even when empty, and R-0013 equates unset with empty only for keyid. envelope.proto is proto3 (L283), and in proto3 a singular bytes or string field and a repeated field have no presence: one holding its empty default is not written, and proto3's JSON mapping omits it by default (both outside this source: the protobuf language guide and its JSON mapping). So the formal schema (R-0084) cannot express the rule, and a producer that serializes through a protobuf library's default JSON output omits an empty payload or payloadType and breaks R-0011. Its REQUIRED comments (R-0018, R-0019, R-0021) are not enforced by proto3 either. Requirements affected: R-0011, R-0013, R-0018 to R-0021.

<!-- q L283-283 -->
> syntax = "proto3";

<!-- q L290-291 -->
> // REQUIRED. bytes payload = 1;

### SD-8 — §2.1.2: no rule for a consumer given an envelope that lacks a required field

R-0011 binds the producer. No sentence tells a consumer what to do with an envelope that lacks payload, payloadType or signatures. §1.2 rejects when decoding fails (R-0061), which may or may not cover a missing member, and R-0013 read literally, of any unset field, would have the consumer take the missing field as empty and go on; read in its list item, R-0013 covers keyid only. Two consumers can differ: one rejects, the other verifies over an empty type or body, which fails unless the signature was made over exactly that. Interoperability only: neither accepts an envelope its signature does not cover. Found independently by the protocol lane as SDP-6. Requirements affected: R-0011, R-0013, R-0061.

<!-- q L251-251 -->
> An unset field MUST be treated the same as set-but-empty.

<!-- q L97-98 "Reject" .. "fails." -->
> Reject if decoding fails.

### SD-9 — §1.2 against §1.3: one SIGNATURE, or a list

§1.2 decodes one SIGNATURE and rejects if it does not verify (R-0060, R-0064), from the recommended JSON envelope, whose signatures member is an array that may hold several (R-0010), each equivalent to a separate envelope (R-0092). §1.3 verifies such a list and skips a signature that fails (R-0076). The source says neither which procedure applies to an envelope with several signatures, nor which t a verifier that sets none uses. A verifier that applies §1.2 to the first element rejects the envelope [invalid, valid] that §1.3 with t = 1 accepts. This extraction reads §1.3 as the general procedure and §1.2 as its case of one signature (R-0109). Found independently by the protocol lane as SDP-1. Requirements affected: R-0060, R-0064, R-0076, R-0010, R-0092.

<!-- q L96-98 -->
> - Receive and decode SERIALIZED_BODY, PAYLOAD_TYPE, SIGNATURE, and KEYID, such as from the recommended [JSON envelope](envelope.md). Reject if decoding fails.

<!-- q L131-132 -->
> - Verify SIGNATURE against PAE(UTF8(PAYLOAD_TYPE), SERIALIZED_BODY). Skip over if the verification fails.

### SD-10 — §1.3: t has no bounds

t is application-specific (R-0070), with no lower or upper bound, and n takes no part in the procedure. With t of 0 or less the threshold step rejects nothing (R-0079), so an envelope none of whose signatures verifies, or that has none, goes on to the type check and the parser unauthenticated; with t greater than the number of trusted keys no envelope can pass. The threshold step compares the unique keys themselves with t; read as their number, as the break step has it (R-0078). Found independently by the protocol lane as SDP-2. Requirements affected: R-0070, R-0078, R-0079.

<!-- q L121-123 -->
> A `(t, n)`-ENVELOPE is valid if the enclosed signatures pass the verification against at least `t` of `n` unique trusted public keys where `t` is application-specific.

<!-- q L136-136 -->
> - Reject if the unique keys in ACCEPTED_KEYS is less than `t`.

### SD-11 — §4.6: an object with both payload and signed, or with neither

The detection rule (R-0103) tells the two formats apart by a payload member (DSSE) or a signed member (the old format). R-0014 lets a producer add members and R-0015 has a consumer ignore unrecognized ones, so a DSSE envelope with an added signed member is valid DSSE and, by the detection rule, looks like both. The source does not say which wins, nor what an object with neither member is. An added member is outside PAE (R-0105), so anyone can add one, and a verifier of both formats that tests for signed first can be steered away from a valid DSSE envelope, while a DSSE consumer ignores the signed member that an old-format reader acts on: one object read two ways. Found independently by the protocol lane as SDP-5, which adds the object with neither member. Requirements affected: R-0103, R-0014, R-0015.

<!-- q L252-253 -->
> * Producers, or future versions of the spec, MAY add additional fields. Consumers MUST ignore unrecognized fields.

<!-- q L484-487 -->
> Verifiers can differentiate between the [old](https://github.com/in-toto/specification/blob/d416c1f334ac6b581f75c0fa65125fb434d7a610/in-toto-spec.md#42-file-formats-general-principles) and new envelope format by detecting the presence of the `payload` field (new format) vs `signed` field (old format).

### SD-12 — §5, editorial: the notebook disagrees with itself

Non-normative, recorded for completeness. The build interface is said to take three user-defined parameters (L558) and two are listed (L560-561). The markdown names the characters `z}` (L1097) where the code it introduces appends `z~` (L1102), the same sentence explaining `~` as length 126. Neither bears on DSSE; the rejected candidates C-0127 and C-0151 rest on these lines. Found independently by the protocol lane as SDP-10 and SDP-11. Requirements affected: none.

<!-- q L558-558 "In" .. "parameters:" -->
> In our scenario, the build interface takes three user-defined parameters:

<!-- q L560-561 -->
> * `command`: The shell command to run. * `encoding`: The `payloadType` to return.

<!-- q L1097-1097 -->
> To fix this, we need to append a tag to our payload to tell the protobuf parser to consume the rest of the input as some dummy field, such as field number 15. The characters `z}` will do precisely that: `z` is field number 15 of type length-delimited, and `~` is length 126, which is the number of remaining bytes.

<!-- q L1102-1102 -->
> build_command = b": '" + target_payload + b"z~'"

### SD-13 — §1.1: KEYID hints at the algorithm, but may narrow only the keys

KEYID is defined as a hint to what key and algorithm signed (R-0042), and R-0006 forbids its use for security decisions and allows only narrowing the keys to try. Whether a verifier may let KEYID choose the verification algorithm is not said; choosing an algorithm on an unauthenticated hint is the failure background.md lays at the door of JWS implementations (L345-349). Read here: the algorithm comes with the key from the out-of-band agreement (R-0052, R-0055), and KEYID only selects among keys. envelope.proto's comment names the key alone (R-0022). Requirements affected: R-0006, R-0022, R-0042.

<!-- q L52-56 -->
> * KEYID: Optional, unauthenticated hint indicating what key and algorithm was used to sign the message. As with Sign(), details are agreed upon out-of-band by the signer and verifier. It **MUST NOT** be used for security decisions; it may only be used to narrow the selection of possible keys to try.

<!-- q L345-349 "*" .. "`x5c`." -->
> * [JWS], though popular, has a history of [vulnerable implementations](https://auth0.com/blog/critical-vulnerabilities-in-json-web-token-libraries/) due to the complexity and lack of specificity in the RFC, such as not verifying that `alg` matches the public key type or not verifying the root CA for `x5c`.

### SD-14 — §1.3: unique keys are counted, but when two keys are the same is not defined

The validity criterion counts n unique trusted public keys (R-0070), ACCEPTED_KEYS is a set (R-0077), and the break and threshold steps count the unique keys in it (R-0078, R-0079). Nothing says when two keys are the same: the same key material, the same entry among the verifier's trusted keys, or the same KEYID, which R-0006 rules out for a security decision. If uniqueness is by entry, a trusted set that lists one key twice, under two KEYIDs say, lets one signer count twice toward t. Uniqueness by key material is the reading that keeps the threshold meaningful (inferred), though not by itself: one signature verifying under two distinct trusted keys counts twice under it too (SD-15). From protocol.md SDP-3, checked here against the source. Requirements affected: R-0070, R-0077, R-0078, R-0079, R-0006.

<!-- q L122-122 "unique" .. "keys" -->
> unique trusted public keys

<!-- q L133-133 -->
> - Add the accepted public key to the set ACCEPTED_KEYS.

<!-- q L134-135 -->
> - Break if the number of unique keys in ACCEPTED_KEYS is greater or equal to `t`.

### SD-15 — §1.2 and §1.3: a KEYID filter that leaves no key, or several

Filtering the acceptable keys by KEYID (R-0062, R-0074) can leave no key, or several. The steps go straight to verifying against PAE without naming a key (R-0063, R-0075), and §1.3 then adds the accepted public key, in the singular, as though exactly one key verified (R-0077). For honestly generated keys a sound signature scheme makes a second verifying key negligible, so in practice several keys verify one signature when one key is listed twice (SD-14); but unforgeability does not promise that no other key verifies a given signature (exclusive ownership, outside this source: a key can be constructed under which an existing signature verifies), so a key admitted to the trusted set without proof that its holder signs with it can count another signer's signature as its own. Which keys are trusted is the out-of-band agreement's (R-0055), which the source does not describe. Verifiers may differ on a KEYID that matches no key (reject, skip, or fall back to every acceptable key). Neither difference can accept a bad signature, since KEYID decides nothing (R-0006). The reading taken here is R-0106: every candidate key is tried, and a signature that verifies under none counts for nothing. From protocol.md SDP-4, checked here against the source. Requirements affected: R-0062, R-0074, R-0077, R-0006, R-0106.

<!-- q L99-99 -->
> - Optionally, filter acceptable public keys by KEYID.

<!-- q L133-133 -->
> - Add the accepted public key to the set ACCEPTED_KEYS.

### SD-16 — §1.3, terminology: a valid (t, n)-ENVELOPE can still be rejected

Validity is defined by the signatures alone (R-0070), while the procedure that follows also rejects an unsupported PAYLOAD_TYPE and a body that does not parse (R-0080, R-0082). Valid and accepted are two predicates, and a check or an API built from the definition alone omits two rejections. From protocol.md SDP-8, checked here against the source. Requirements affected: R-0070, R-0080, R-0082.

<!-- q L121-123 -->
> A `(t, n)`-ENVELOPE is valid if the enclosed signatures pass the verification against at least `t` of `n` unique trusted public keys where `t` is application-specific.

<!-- q L137-137 -->
> - Reject if PAYLOAD_TYPE is not a supported type.

<!-- q L138-139 -->
> - Parse SERIALIZED_BODY according to PAYLOAD_TYPE. Reject if the parsing fails.

### SD-17 — §1.2: a supported type is not tied to the key that verified

Signer and verifier settle the PAYLOAD_TYPE and the cryptography out of band (R-0055), but the steps only check that PAYLOAD_TYPE is a supported type (R-0065, R-0080) and narrow keys by KEYID alone (R-0062); no step asks whether the key that verified was agreed for that type. A verifier that supports several types therefore accepts an envelope of type B signed by a key agreed only for type A (inferred). PAE stops the type of one signed message from being changed (R-0023); which signer may sign which type is policy the source does not describe, though background.md names one key per message type as the burden of raw signatures (L336-338, C-0061, rejected as motivation). From protocol.md SDP-9, checked here against the source. Requirements affected: R-0055, R-0065, R-0080, R-0062.

<!-- q L82-83 -->
> - Agree on a PAYLOAD_TYPE and cryptographic details, optionally including KEYID.

<!-- q L102-102 -->
> - Reject if PAYLOAD_TYPE is not a supported type.

<!-- q L336-338 "Every" .. "(#motivation)." -->
> Every public key must be used for exactly one purpose over exactly one message type, lest the system be vulnerable to [confusion attacks](#motivation).

### SD-18 — §2.1.1 against §1.3: equivalent to separate envelopes, but the threshold is counted inside one

R-0010 makes an envelope with several signatures the equivalent of several envelopes with one signature each (R-0092); §1.3 defines the validity of a (t, n)-ENVELOPE over the signatures enclosed in one envelope (R-0070). Signature by signature the two agree. For t of 2 or more they do not: two separate envelopes, each with one good signature, each fall short of the threshold, while one envelope carrying both meets it, unless a verifier gathers separate envelopes by payload and payloadType, which the source never describes. From design-notes.md DN-SD-1 (pass-1 notes; design-notes.md now cites this entry as SD-18, in its row D-02 and Part 4.4); worded here from the source. Requirements affected: R-0010, R-0092, R-0070.

<!-- q L229-230 -->
> An envelope MAY have more than one signature, which is equivalent to separate envelopes with individual signatures.

<!-- q L121-123 -->
> A `(t, n)`-ENVELOPE is valid if the enclosed signatures pass the verification against at least `t` of `n` unique trusted public keys where `t` is application-specific.

### SD-19 — §1.2 and §2.3: the bytes-identity rule names the payload, not the type

R-0008 and R-0016 require the bytes handed to the application layer to be the bytes verified, and R-0009 and R-0017 forbid reading the payload out of the envelope again once it is verified. No sentence says the same of PAYLOAD_TYPE, which the application needs to interpret the body and by which §1.2's last step parses it (R-0066). JSON lets an object carry a member twice and DSSE does not address duplicates (messages.yaml source_silences), so a verifier can check PAE under one payloadType while an application that reads the envelope again for the type gets the other: the confusion that authenticating PAYLOAD_TYPE exists to prevent (R-0023), reopened by a parser differential. Narrow: it needs a duplicated member and an application that takes the type from anywhere but the verification step. Read here as covering the type (R-0108, inferred). From design-notes.md DN-SD-2 (its Part 7.2), re-checked against the source by pass 2, which took it in. Requirements affected: R-0008, R-0009, R-0016, R-0017, R-0108.

<!-- q L109-112 "**Important:**" .. "payload." -->
> **Important:** Implementations MUST ensure that the same SERIALIZED_BODY that is verified is the same sent to the application layer. In particular, implementations MUST NOT re-parse the envelope after verification to pull out the payload.

<!-- q L273-276 "**Important:**" .. "payload." -->
> **Important:** Implementations MUST ensure that the same payload bytes that are verified are the ones sent to the application layer. In particular, implementations MUST NOT re-parse the envelope after verification to pull out the payload.

<!-- q L103-104 -->
> - Parse SERIALIZED_BODY according to PAYLOAD_TYPE. Reject if the parsing fails.

### SD-20 — §4.4, editorial: the example calls the attacker the signer

Non-normative, recorded for completeness, as SD-12 is. §4.4's second concern is the missing authenticated context indicator, which would keep signer and verifier reading a payload alike (L407-408): there the signer is the honest party. Its example then gives the misleading request to the signer, the party who gets a CI/CD system to produce the CBOR message (L409-411), where the notebook calls that party an attacker and the CI/CD system the one that signs (L563). Read here as the notebook has it, which protocol.yaml's attacker role follows. Found by the protocol lane's pass-2 check of that role, worded here from the source. Requirements affected: none.

<!-- q L407-408 -->
> Second, the scheme does not include an authenticated "context" indicator to ensure that the signer and verifier interpret the payload in the same exact way.

<!-- q L409-411 "For" .. "saying Y." -->
> For example, if in-toto were extended to support CBOR and protobuf encoding, the signer could get a CI/CD system to produce a CBOR message saying X and then a verifier to interpret it as a protobuf message saying Y.

<!-- q L563-563 -->
> **Problem:** An attacker can trick the CI/CD system to sign arbitrary messages.

### Crosswalk: the pass-1 lanes' ids

| canonical | messages.yaml | protocol.md, protocol.yaml, state-machine.yaml | design-notes.md | note |
|---|---|---|---|---|
| SD-1 | SDC-1 |  |  | extended here to L250 |
| SD-2 | SDC-2 |  |  |  |
| SD-3 | SDC-3 |  |  |  |
| SD-4 | SDC-4 |  |  |  |
| SD-5 | SDC-5 |  |  |  |
| SD-6 | SDC-6 |  |  |  |
| SD-7 |  |  |  | requirements lane only |
| SD-8 |  | SDP-6 |  |  |
| SD-9 |  | SDP-1 |  |  |
| SD-10 |  | SDP-2 |  |  |
| SD-11 |  | SDP-5 |  | SDP-5 adds the object with neither member |
| SD-12 |  | SDP-10, SDP-11 |  |  |
| SD-13 |  |  |  | requirements lane only |
| SD-14 |  | SDP-3 |  |  |
| SD-15 |  | SDP-4 |  |  |
| SD-16 |  | SDP-8 |  |  |
| SD-17 |  | SDP-9 |  |  |
| SD-18 |  |  | DN-SD-1 | design-notes.md cites it as SD-18 (row D-02, Part 4.4) |
| SD-19 |  |  | DN-SD-2 | taken in by pass 2; design-notes.md Part 7.2 offered it |
| SD-20 |  | protocol.yaml attacker role note |  | pass 2; the protocol lane had recorded it as our identification, not as a defect |

Declined: SDP-7, that the bytes-identity rule is not stated for the (t, n) procedure. R-0016 and R-0017 bind every implementation for every envelope format (R-0097) and sit inside no procedure, so they reach a (t, n) verifier as written, and R-0008 and R-0009 name implementations, not the steps of §1.2; protocol.md itself calls the rule plainly general. Recorded so that the declining is visible; pass 2 may overrule it.

Not source defects, and so not here: messages.yaml's source_silences, which record what the source leaves unsaid (base64 padding and alphabet mixing, JSON nulls and duplicate members, bounds and lengths) rather than what it gets wrong, and protocol.md's open issues OI-01 to OI-08, of which OI-03, OI-06 and OI-07 restate SD-17, SD-9 and SD-10.

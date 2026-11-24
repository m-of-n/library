---
record: in-toto-envelope-v1
kind: normative
title: "in-toto-envelope-v1 — normative text"
generated_by: bin/fx1-skeleton
reviewed_by: ""
---

# Normative text

Every requirement text in requirements.yaml that has source lines appears here verbatim under its section, as a marker that `bin/check-quotes --render` writes and `bin/check-quotes` verifies; split_of children are listed on their parent line rather than quoted twice. The keyword-less binding text pass 1 added (candidate-stated and hunted entries) is interleaved in source order, and a few passages that bind nothing but fix what a rule refers to are quoted as context and marked so. Generated together with requirements.yaml: 50 requirements, of which 29 skeleton, 4 split children, 7 from candidates, 2 hunted and 8 inferred.

Line numbers are those of `.cache/in-toto-envelope-v1.txt`: envelope.md line for line, with only its six ATX headings renumbered (distilled/render-source.py).

## Keyword declaration

envelope.md declares no BCP 14 keywords: no RFC 2119, RFC 8174 or BCP 14 recital and no key-words paragraph occurs in its 110 lines. This extraction reads the 30 capitalised keywords as BCP 14 because they are printed in BCP 14 form throughout; whether the framework declares the keywords in another file was not read, this file being the source. No keyword occurs in lowercase. The bare capitalised NOT of §1.1 (R-0031) is emphasis, not a keyword. The reconciliation in requirements.yaml places all 30 by line.

## Preamble

<!-- q L3-4 -->
> The Envelope is the outermost layer of the attestation, handling serialization and authentication (via digital signatures).

Context, not an entry: it says what the Envelope layer is for, and R-0045 rests on it, but it states no obligation, and it stands before §1, so no section locator contains it.

## §1

<!-- q L8-8 -->
> The RECOMMENDED format and protocol for Envelopes are defined per [DSSE v1.0].

R-0001

<!-- q L9-10 -->
> Producers MAY use other signature methods and formats that meet the [ITE-5] specification:

R-0002

The six items that follow have no subject: they are the ITE-5 criteria R-0002 leads into, and they bind the alternative envelope format (R-0003 to R-0008).

<!-- q L12-12 -->
> - MUST support the inclusion of multiple signatures in a single envelope

R-0003

<!-- q L13-13 -->
> - SHOULD include an authenticated payload type

R-0004

<!-- q L14-14 -->
> - SHOULD avoid depending on canonicalization for security

R-0005

<!-- q L15-15 -->
> - SHOULD support a hint indicating what signing key was used, i.e., a KEYID

R-0006

<!-- q L16-16 -->
> - SHOULD NOT require the verifier to parse the payload before verifying

R-0007

<!-- q L17-17 -->
> - SHOULD NOT require the inclusion of signing key algorithms in the signature

R-0008

## §1.1

<!-- q L21-22 -->
> - The [Sigstore Bundle], while [supporting DSSE], is not currently [ITE-5] compliant because it requires a _single signature_ in the envelope.[^1]

R-0030 · candidate C-0001

<!-- q L23-24 -->
> - The [COSE_Sign] structure is [ITE-5] compliant, whereas the `COSE_Sign1` format that supports only one signer is NOT compliant.

R-0031 · candidate C-0002 · split: R-0032, R-0033

The footnote of R-0030, context, not an entry:

<!-- q L98-98 -->
> [^1]: There is an [ongoing discussion](https://github.com/sigstore/sig-clients/issues/9) about supporting [DSSE Signature Extensions](https://github.com/secure-systems-lab/dsse/blob/devel/envelope.md#signature-extensions-experimental) to extend the current features of Sigstore Bundles.

## §2

<!-- q L28-29 -->
> The in-toto Attestation Framework has the following general field requirements for an Envelope:

R-0034 · no candidate (hunted)

<!-- q L31-32 "-" .. "signatures." -->
> - `signatures` (or equivalent) is REQUIRED and MUST be defined as an array of digital signatures.

R-0009 · split: R-0035, R-0036

<!-- q L32-33 "The" .. "schema." -->
> The encoding of the signature bytes is determined by the envelope schema.

R-0037 · candidate C-0003

<!-- q L34-34 "-" .. "used." -->
> - A `keyid` (or equivalent) SHOULD be included for each signing key used.

R-0010

<!-- q L34-35 "The" .. "array." -->
> The envelope schema MAY nest this field within the signature array.

R-0011

<!-- q L36-37 -->
> - `payload` (or equivalent) SHOULD be included and contain the in-toto [Statement] that was signed.

R-0012

<!-- q L38-38 -->
> - `payloadType` (or equivalent) MUST be signed along with the `payload`.

R-0013

<!-- q L39-40 -->
> It MUST take the form `application/vnd.in-toto+<encoding>` to indicate an in-toto [Statement] payload and its serialized `<encoding>` format.

R-0014

<!-- q L42-43 -->
> In addition, the Envelope spec has the following specific requirements for the standard [DSSE][DSSE v1.0] fields.

R-0038 · no candidate (hunted)

<!-- q L45-46 "-" .. "`application/vnd.in-toto+json`." -->
> - `payloadType` MUST be set to `application/vnd.in-toto.<predicate>+json` or to `application/vnd.in-toto+json`.

R-0015

<!-- q L46-47 "This" .. "schema." -->
> This indicates that the Envelope contains a JSON object with a `_type` field specifying its schema.

R-0039 · candidate C-0004

<!-- q L47-48 "If" .. "apply:" -->
> If the predicate-specific media type is used, the following requirements apply:

R-0040 · candidate C-0005

<!-- q L49-50 -->
> - `<predicate>` MUST match the [predicate specification filename] without the file extension.

R-0016

<!-- q L51-52 "-" .. "type." -->
> - Consumers SHOULD NOT rely upon the media type for individual attestations as faithful indicators of predicate type.

R-0017

<!-- q L52-53 "Consumer" .. "layer." -->
> Consumer SHOULD only rely on the `predicateType` field in the [Statement] layer.

R-0018

<!-- q L54-55 -->
> - To obtain predicate information that is authenticated, consumers MUST parse the Envelope's `payload`, and verify it against its `signatures`.

R-0019

<!-- q L56-57 -->
> - The predicate version is not specified in the media type; it is handled in the [Statement] layer.

R-0041 · candidate C-0006

<!-- q L58-58 -->
> - `payload` MUST be a base64-encoded JSON [Statement].

R-0020

## §3

<!-- q L62-63 -->
> If stored in a dedicated file by itself, and not as part of a [Bundle], an Envelope SHOULD use the suffix `.json`.

R-0021

<!-- q L65-67 -->
> - For attestations intended for consumption by [in-toto-verify], an Envelope containing an attestation about a particular software supply chain step `<step-name>` SHOULD be named `<step-name>.json`.

R-0022

<!-- q L68-70 -->
> - For other verifiers, or cases in which a step name cannot be easily determined, the attestation producer and consumer MAY agree on an arbitrary filename: `<env-name>.json`.

R-0023

<!-- q L71-74 -->
> - If multiple Envelopes are produced for the same step by different [functionaries] uniquely identified by a public key, an Envelope name SHOULD include the truncated [KEYID] of the public key `<keyid[0:8]>` of the signing functionary: `<step/env-name>.<keyid[0:8]>.json`.

R-0024

## §4

<!-- q L78-79 -->
> The media type `application/vnd.in-toto.<predicate>+dsse` SHOULD be used to denote an individual attestation in arbitrary storage systems.

R-0025

<!-- q L81-82 "-" .. "extension." -->
> - The `<predicate>` MUST match the [predicate specification filename] without the file extension.

R-0026

<!-- q L82-83 "Predicate" .. "layer." -->
> Predicate versioning is handled in the [Statement] layer.

R-0042 · candidate C-0007

<!-- q L84-85 "-" .. "type." -->
> - Consumers SHOULD NOT rely upon the media type for individual attestations as faithful indicators of predicate type.

R-0027

<!-- q L85-86 "Consumer" .. "layer." -->
> Consumer SHOULD only rely on the `predicateType` field in the [Statement] layer.

R-0028

<!-- q L87-88 -->
> - To obtain predicate information that is authenticated, consumers MUST parse the Envelope's `payload`, and verify it against its `signatures`.

R-0029

## §4.1

Examples only, not entries: the three media types at L94-96 are candidates C-0008 to C-0010, rejected because an example binds nothing, and the lead-in at L92 binds nothing either.

## Link definitions the rules name

Context, not entries: the reference-style link targets at L100-110 fix what a bracketed name in a rule points at. Each line names the stated entries, split children included, whose text uses it.

<!-- q L100-100 -->
> [Bundle]: bundle.md

used by R-0021

<!-- q L101-101 -->
> [COSE_Sign]: https://datatracker.ietf.org/doc/html/rfc8152#section-4.1

used by R-0031, R-0032

<!-- q L102-102 -->
> [DSSE v1.0]: https://github.com/secure-systems-lab/dsse/blob/v1.0.2/envelope.md

used by R-0001, R-0038

<!-- q L103-103 -->
> [ITE-5]: https://github.com/in-toto/ITE/tree/master/ITE/5#specification

used by R-0002, R-0030, R-0031, R-0032

<!-- q L104-104 -->
> [KEYID]: https://github.com/in-toto/docs/blob/v1.0/in-toto-spec.md#421-key-formats

used by R-0024

<!-- q L105-105 -->
> [Sigstore Bundle]: https://docs.sigstore.dev/about/bundle/

used by R-0030

<!-- q L106-106 -->
> [Statement]: statement.md

used by R-0012, R-0014, R-0018, R-0020, R-0028, R-0041, R-0042

<!-- q L107-107 -->
> [in-toto-verify]: https://github.com/in-toto/in-toto#verification

used by R-0022

<!-- q L108-108 -->
> [functionaries]: https://github.com/in-toto/docs/blob/v1.0/in-toto-spec.md#212-functionaries

used by R-0024

<!-- q L109-109 -->
> [predicate specification filename]: ../predicates

used by R-0016, R-0026

<!-- q L110-110 -->
> [supporting DSSE]: https://docs.sigstore.dev/about/bundle/#dsse

used by R-0030

## Inferred requirements (not verbatim)

These entries are in our words and quote nothing; each names what it is derived from in derived_from. R-0043 (§2, payloadType is present though no sentence requires it); R-0044 (§2, verification covers payloadType); R-0045 (§2, what verifying against the signatures needs and what it leaves open); R-0046 (§2 and §4, the predicate a media type's <predicate> names); R-0047 (§2 and §4, a media type that disagrees with predicateType); R-0048 (§1, formats outside DSSE and ITE-5); R-0049 (§3, the keyid in a file name); R-0050 (§2, a consumer given an envelope that breaks the producer rules).

## Source defects

Inconsistencies and gaps in envelope.md itself. Each quotes the lines it rests on; the prose is ours. This is the record's one canonical list: every artifact names a source defect by these ids, and the crosswalk at the end maps the ids the pass-1 lanes gave the same defects in messages.yaml, protocol.yaml and protocol.md, and the design-notes questions that state them. SD-1, SD-4 and SD-11 leave an implementer two incompatible readings, as does SD-2's question of presence; SD-3, SD-5, SD-6, SD-7, SD-9, SD-10 and SD-12 to SD-15 are inconsistencies of strength or gaps; SD-8 is editorial. SD-1 to SD-8 are the requirements lane's; pass 2 added SD-9 to SD-15 from the other lanes' lists, the link definitions and a comparison with in-toto-attestation-v1's extraction of the same file (library#134), and extended SD-2, SD-5, SD-6 and SD-12 with what those add.

### SD-1 — §2: the general form of payloadType excludes the predicate-specific value the DSSE rule allows

R-0014 is one of the rules R-0034 makes general for every Envelope, and it gives payloadType a single form, in which only the encoding varies. The DSSE-specific rules follow In addition (R-0038), so they add to the general rules rather than replace them; R-0015 then allows, beside the generic value, a predicate-specific one that puts a predicate name before the + suffix, which the general form does not admit. Read literally, every predicate-specific payloadType breaks R-0014, and the rules R-0040 scopes to that value (R-0016 to R-0019, R-0041) could never apply. The evident intent is that R-0015 widens R-0014 for DSSE envelopes; a validator built from R-0014 alone rejects every predicate-specific payloadType. On that reading an envelope in another schema, which owes only the general rules, has only the generic form. Requirements affected: R-0014, R-0015, R-0016, R-0038, R-0040.

<!-- q L39-40 -->
> It MUST take the form `application/vnd.in-toto+<encoding>` to indicate an in-toto [Statement] payload and its serialized `<encoding>` format.

<!-- q L42-43 -->
> In addition, the Envelope spec has the following specific requirements for the standard [DSSE][DSSE v1.0] fields.

<!-- q L45-46 "-" .. "`application/vnd.in-toto+json`." -->
> - `payloadType` MUST be set to `application/vnd.in-toto.<predicate>+json` or to `application/vnd.in-toto+json`.

### SD-2 — §1 against §2: an authenticated payload type is a SHOULD for the format and a MUST for every Envelope

Among the ITE-5 criteria an alternative format is to meet, an authenticated payload type is a SHOULD (R-0004). Among the general rules every Envelope is to meet (R-0034), payloadType or its equivalent has to be signed together with the payload, a MUST (R-0013), which only a format with an authenticated payload type can do. A format that takes the latitude R-0004 leaves meets ITE-5 and still cannot carry an in-toto Envelope, so the permission of R-0002 is narrower than its own condition says. Not a contradiction in the letter, since §2 adds to §1, but §1 read alone misleads an implementer choosing a format. Requirements affected: R-0002, R-0004, R-0013, R-0043.

Pass 2: a second question sits on the same lines. No sentence makes payloadType present the way R-0035 makes signatures present, and R-0013 and R-0014 presuppose one. R-0043 reads them as requiring it; messages.yaml and the derived schema read them as applying only when it is present (cases GEN-A01 and DSSE-R04 pin that reading, as an assumption). The source does not decide, so a validator built on one reading rejects envelopes the other accepts. Requirements affected, added: R-0014.

<!-- q L13-13 -->
> - SHOULD include an authenticated payload type

<!-- q L38-38 -->
> - `payloadType` (or equivalent) MUST be signed along with the `payload`.

### SD-3 — §2 and §4: the consumer rule states no order for parsing and verifying

R-0019 and R-0029 name two steps, parsing the payload and verifying it against the signatures, joined by and, with no order stated; the printed order is parse first. §1 asks that a format let the verifier check the signatures before it parses the payload (R-0007), the opposite order, and a consumer that reads R-0019 as a sequence parses bytes it has not yet authenticated. In §2 the premise of the rule is loose as well: the media type there is payloadType, which R-0013 has signed, so it is authenticated though possibly unfaithful, and the word faithful in R-0017 is the accurate one; the predicate named in a verified payloadType is authenticated without parsing the payload. Requirements affected: R-0007, R-0017, R-0019, R-0029.

<!-- q L16-16 -->
> - SHOULD NOT require the verifier to parse the payload before verifying

<!-- q L54-55 -->
> - To obtain predicate information that is authenticated, consumers MUST parse the Envelope's `payload`, and verify it against its `signatures`.

### SD-4 — §1.1: the Sigstore Bundle verdict and a single-signature DSSE envelope

§1.1 rules the Sigstore Bundle out of ITE-5 compliance because it admits only one signature, while saying that it supports DSSE, the RECOMMENDED format (R-0001). No rule in §1 or §2 requires an envelope instance to carry more than one signature: R-0003 is a criterion on a format, and R-0036 asks only for an array. So whether an attestation delivered as a DSSE envelope inside a Sigstore Bundle conforms depends on which structure is the Envelope, the Bundle (an alternative schema that fails R-0003) or the DSSE envelope it carries (which can meet every rule here), and the source does not say. The verdict is given as current only, and the footnote records a discussion that may change it. The [Bundle] of §3 is another structure, bundle.md (L100). Requirements affected: R-0001, R-0003, R-0030, R-0036.

<!-- q L21-22 -->
> - The [Sigstore Bundle], while [supporting DSSE], is not currently [ITE-5] compliant because it requires a _single signature_ in the envelope.[^1]

<!-- q L98-98 -->
> [^1]: There is an [ongoing discussion](https://github.com/sigstore/sig-clients/issues/9) about supporting [DSSE Signature Extensions](https://github.com/secure-systems-lab/dsse/blob/devel/envelope.md#signature-extensions-experimental) to extend the current features of Sigstore Bundles.

### SD-5 — §3 and §4 are written for a DSSE envelope serialized as JSON

§1 permits other formats, and §1.1 calls COSE_Sign compliant, yet §3 gives every Envelope stored alone the suffix .json (R-0021) and §4 gives every stored attestation a media type ending +dsse (R-0025). Neither section is scoped to DSSE the way R-0038 scopes the second list of §2, and neither names a suffix or a media type for an envelope in another schema; COSE structures are CBOR (RFC 8152, outside this source). A producer that uses R-0002 can only depart from both SHOULDs, with nothing named to depart to. Requirements affected: R-0002, R-0021, R-0025, R-0032.

Pass 2, from messages.yaml: the generic payloadType admits any <encoding> (R-0014), yet the suffix stays .json. <encoding> names the Statement's serialization, not the Envelope's, so the suffix misfits exactly where the Envelope itself is not JSON, which is this defect. Requirements affected, added: R-0014.

<!-- q L62-63 -->
> If stored in a dedicated file by itself, and not as part of a [Bundle], an Envelope SHOULD use the suffix `.json`.

<!-- q L78-79 -->
> The media type `application/vnd.in-toto.<predicate>+dsse` SHOULD be used to denote an individual attestation in arbitrary storage systems.

### SD-6 — §4: no generic storage media type

§2 gives payloadType a generic value beside the predicate-specific one (R-0015). §4 gives the storage media type only a predicate-specific form (R-0025), whose <predicate> must match a predicate specification filename (R-0026), a file under the relative link of L109. An attestation whose predicate has no specification there, which is any predicate defined elsewhere, has no storage media type that meets both rules, and the source names no fallback. Requirements affected: R-0015, R-0025, R-0026.

Pass 2, from messages.yaml: because <predicate> is defined only by reference to that directory, the source gives it no character set and no case rule either, so no pattern for it can be derived from the source; the derived schema's RN class is our assumption (messages.yaml SIL-03). Requirements affected, added: R-0016.

<!-- q L81-82 "-" .. "extension." -->
> - The `<predicate>` MUST match the [predicate specification filename] without the file extension.

<!-- q L109-109 -->
> [predicate specification filename]: ../predicates

### SD-7 — §1: no rule for an envelope format that is neither DSSE nor ITE-5 compliant

§1 recommends DSSE (R-0001) and permits formats that meet ITE-5 (R-0002), and §1.1 classifies three formats. No sentence forbids a producer a format that meets neither, so the RECOMMENDED of R-0001 is the only rule such a producer departs from, and no sentence tells a consumer whether to accept, reject or ignore an envelope in such a format, COSE_Sign1 or the Sigstore Bundle for instance. An implementation has to choose, and two conforming consumers may choose differently. Requirements affected: R-0001, R-0002, R-0030, R-0033, R-0048.

<!-- q L8-8 -->
> The RECOMMENDED format and protocol for Envelopes are defined per [DSSE v1.0].

<!-- q L9-10 -->
> Producers MAY use other signature methods and formats that meet the [ITE-5] specification:

### SD-8 — §2 and §4, editorial: Consumer in the singular

The SHOULD sentence that follows each SHOULD NOT about media types (R-0017, R-0027) opens with the singular Consumer, without an article, where the sentence before it has the plural; read as Consumers. Requirements affected: R-0018, R-0028.

<!-- q L52-53 "Consumer" .. "layer." -->
> Consumer SHOULD only rely on the `predicateType` field in the [Statement] layer.

<!-- q L85-86 "Consumer" .. "layer." -->
> Consumer SHOULD only rely on the `predicateType` field in the [Statement] layer.

### SD-9 — §3: the KEYID naming rule assumes one signing functionary per Envelope, and a keyid

R-0024 names an Envelope after the truncated KEYID of the signing functionary, in the singular, for the case of several Envelopes for one step, one per functionary. A format is to support several signatures in one envelope (R-0003), so one Envelope may carry several functionaries' signatures, and a keyid is only a SHOULD (R-0010). Such an Envelope, or one with no keyid, has no stated name under the rule that would otherwise apply, and the source does not say whether a step with several functionaries should yield one multi-signature Envelope or one Envelope per functionary. From protocol.yaml (its pass-1 SD-06 and OI-03). Requirements affected: R-0003, R-0010, R-0024, R-0049.

<!-- q L12-12 -->
> - MUST support the inclusion of multiple signatures in a single envelope

<!-- q L71-74 -->
> - If multiple Envelopes are produced for the same step by different [functionaries] uniquely identified by a public key, an Envelope name SHOULD include the truncated [KEYID] of the public key `<keyid[0:8]>` of the signing functionary: `<step/env-name>.<keyid[0:8]>.json`.

### SD-10 — §3: a keyid-suffixed file name cannot be told from a step name that contains a dot

The name of R-0024 is the name of R-0022 or R-0023 with a dot and <keyid[0:8]> put before .json, and nothing keeps a dot out of a step name or an agreed name. So build.deadbeef.json names the Envelope of a step build.deadbeef, or of a step build signed by a functionary whose KEYID begins deadbeef, and a consumer cannot tell which from the name; every name of R-0024's form also has R-0022's. The slash of <step/env-name> is notation the source does not define, read as the step name or the agreed name. From messages.yaml (its pass-1 SD-04). Requirements affected: R-0022, R-0023, R-0024.

<!-- q L65-67 -->
> - For attestations intended for consumption by [in-toto-verify], an Envelope containing an attestation about a particular software supply chain step `<step-name>` SHOULD be named `<step-name>.json`.

### SD-11 — §2 and §4: the consumer rules are stated only within the media-type rules

§2's copies of the consumer rules (R-0017, R-0018, R-0019) follow the condition of R-0040, that the predicate-specific payloadType is used; §4's copies (R-0027, R-0028, R-0029) are bullets of the storage convention of R-0025, with no condition of their own. No sentence states them for consumers in general. Read narrowly, a consumer of a DSSE Envelope with the generic payloadType, held as a plain file, falls under neither copy, and the obligation to parse and verify before relying on predicate information does not bind it; read broadly, §4's copies bind every consumer. The source does not say which: protocol.yaml models the rules as applying to every Envelope consumed (inferred), and design-notes.md reads §4's copies as unconditional. From protocol.yaml (its pass-1 SD-07) and design-notes.md (Q-02). Requirements affected: R-0017, R-0018, R-0019, R-0027, R-0028, R-0029, R-0040.

<!-- q L47-48 "If" .. "apply:" -->
> If the predicate-specific media type is used, the following requirements apply:

<!-- q L78-79 -->
> The media type `application/vnd.in-toto.<predicate>+dsse` SHOULD be used to denote an individual attestation in arbitrary storage systems.

### SD-12 — link definitions: the ITE-5 criteria are linked at a moving branch

The permission of R-0002 is conditioned on meeting ITE-5, and §1 restates six ITE-5 criteria (R-0003 to R-0008), but [ITE-5] links the ITE repository's master branch, which moves, while [DSSE v1.0] is pinned to the tag v1.0.2, its label naming v1.0. So the restated criteria and the text they restate can drift apart, and the source does not say which governs if they differ. Other unpinned targets are [in-toto-verify] (L107), the Sigstore documentation (L105, L110) and the footnote's DSSE link to the devel branch (L98). From design-notes.md (Q-07, S-01). Requirements affected: R-0001, R-0002, R-0003 to R-0008.

Pass 2: the relative link of L109 moves too, with the repository rather than with this file. envelope.md is byte-identical at the v1.2.0 tag df02077 and at main 50bf017 (record.yaml content.note), yet by a GitHub contents listing of spec/predicates taken 2026-11-16, df02077 holds spdx2.md and spdx3.md and no spdx.md, while 50bf017 also holds spdx.md, added by 37fb3c0 on 2026-07-17. So the file's own SPDX example, application/vnd.in-toto.spdx+dsse, fails R-0026 at the one commit and meets it at the other; provenance.md and vsa.md exist at both. in-toto-attestation-v1's extraction records the df02077 state (its SD-19). Requirements affected, added: R-0016, R-0026.

<!-- q L102-102 -->
> [DSSE v1.0]: https://github.com/secure-systems-lab/dsse/blob/v1.0.2/envelope.md

<!-- q L103-103 -->
> [ITE-5]: https://github.com/in-toto/ITE/tree/master/ITE/5#specification

### SD-13 — §1.1: COSE_Sign is called compliant without the criteria being shown, against an obsoleted RFC

R-0032 calls COSE_Sign compliant only in contrast with COSE_Sign1's single signer (R-0033), that is against R-0003; how COSE_Sign meets R-0004 to R-0008 is not said, and R-0008 is the doubtful one, since a COSE signature conventionally names its algorithm in its headers (RFC 9052 §3.1, outside this source; whether RFC 9052 requires it there was not settled). And [COSE_Sign] links RFC 8152 §4.1, which RFC 9052 and RFC 9053 obsolete (rfc-8152/record.yaml:21). From design-notes.md (Q-05, C-03). Requirements affected: R-0008, R-0031, R-0032.

<!-- q L101-101 -->
> [COSE_Sign]: https://datatracker.ietf.org/doc/html/rfc8152#section-4.1

### SD-14 — §2: a payload that should be included but must be parsed

R-0012 lets an envelope in another schema omit its payload, a SHOULD, while R-0019 and R-0029 have the consumer parse the Envelope's payload to obtain authenticated predicate information; for DSSE, R-0020 makes the payload a base64-encoded JSON Statement. How a consumer obtains a payload the envelope does not carry, a detached one, is not said, so for such an envelope R-0019 cannot be met as written. From protocol.yaml (OI-04) and design-notes.md (Q-08), and in-toto-attestation-v1's extraction (its SD-22). Requirements affected: R-0012, R-0019, R-0029.

<!-- q L36-37 -->
> - `payload` (or equivalent) SHOULD be included and contain the in-toto [Statement] that was signed.

<!-- q L54-55 -->
> - To obtain predicate information that is authenticated, consumers MUST parse the Envelope's `payload`, and verify it against its `signatures`.

### SD-15 — §2: the general payloadType form admits serializations the source never defines

R-0014's form names a serialized <encoding>, so a Statement serialized otherwise than as JSON is contemplated, but this source defines only JSON: the DSSE values end +json (R-0015), and the payload is a JSON object (R-0039), base64-encoded JSON (R-0020). No value list, registry or grammar for <encoding> is given, so an envelope in another schema can carry application/vnd.in-toto+cbor, say, with nothing to say what its payload then is. From design-notes.md (§3.4 item 4, Q-12) and messages.yaml (SIL-03), and in-toto-attestation-v1's extraction (its SD-23). Requirements affected: R-0014, R-0015, R-0020, R-0039.

<!-- q L39-40 -->
> It MUST take the form `application/vnd.in-toto+<encoding>` to indicate an in-toto [Statement] payload and its serialized `<encoding>` format.

### Crosswalk: the pass-1 lanes' ids

The pass-1 lanes kept their own lists, and their numbers collided: SD-04 meant three different defects in three files. Pass 2 renamed the messages and protocol lists to the canonical ids above (their entries keep their own quotes and wording), and the design notes keep their Q-nn questions, here pointed at the defect each states.

| canonical | messages.yaml, pass 1 | protocol.yaml and protocol.md, pass 1 | design-notes.md |
|---|---|---|---|
| SD-1 | SD-01 | SD-01 | Q-01 |
| SD-2 | SD-05 | SD-02 | A-01 |
| SD-3 | | SD-03 | Q-02 (order), C-01 |
| SD-4 | | | Q-06, C-05 |
| SD-5 | SD-02 | SD-04 | Q-08 (the storage media type) |
| SD-6 | SD-03, SIL-03 | SD-05 | Q-08 (no generic storage type) |
| SD-7 | | EP-01 (a consumer's handling) | |
| SD-8 | SD-06 | | |
| SD-9 | | SD-06, OI-03 | Q-04 (one functionary) |
| SD-10 | SD-04 | | |
| SD-11 | | SD-07 | Q-02 (scope) |
| SD-12 | | | Q-07, S-01 |
| SD-13 | | | Q-05, C-03 |
| SD-14 | | OI-04 | Q-08 (a detached payload) |
| SD-15 | SIL-03 | | Q-12, §3.4 item 4 |

Not source defects, and so not here: messages.yaml's silences SIL-01 to SIL-05, protocol.yaml's open issues OI-01, OI-02 and OI-05 to OI-07, and the design-notes questions Q-03, Q-08's remaining items, Q-09, Q-10, Q-11 and Q-13 to Q-15 (Q-10 to Q-15 are mapping questions for mofn; Q-12 is also SD-15).

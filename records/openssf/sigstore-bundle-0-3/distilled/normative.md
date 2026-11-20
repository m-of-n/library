---
record: sigstore-bundle-0-3
kind: normative
title: "sigstore-bundle-0-3 — normative text"
generated_by: bin/fx1-skeleton
reviewed_by: ""
---

# Normative text

Generated verbatim by `bin/fx1-skeleton`; each quotation carries its
source lines and `bin/check-quotes` verifies it. Pass 1 adds the
keyword-less binding text (tables, IANA rules, lists) as
`<!-- q Lx-y -->` markers and lets `bin/check-quotes --render` write the words.

## §1

<!-- q L42-43 -->
> The primary message ('Bundle') MUST be versioned, by populating the 'media_type' field.

R-0001

<!-- q L43-44 -->
> Semver-ish (only major/minor versions) scheme MUST be used.

R-0002

## §1.1

<!-- q L59-60 -->
> Clients MUST verify the hashed message in the message imprint against the signature in the bundle.

R-0003

## §1.2

<!-- q L74-76 -->
> When used as a DSSE extension, if the `public_key` field is used to indicate the key identifier, it MUST match the `keyid` field of the signature the extension is attached to.

R-0004

<!-- q L87-88 -->
> 2. A sequence of one or more X.509 certificates, of which the first member MUST be a leaf certificate conveying the signing key.

R-0005

<!-- q L88-89 -->
> Subsequent members SHOULD be in issuing order, meaning that `n + 1` should be an issuer for `n`.

R-0006

<!-- q L91-93 -->
> Signers MUST NOT include root CA certificates in bundles, and SHOULD NOT include intermediate CA certificates that appear in an independent root of trust (such as the Public Good Instance's trusted root).

R-0007

<!-- q L95-96 -->
> Verifiers MUST validate the chain carefully to ensure that it chains up to a CA certificate that they independently trust.

R-0008

<!-- q L96-99 -->
> Verifiers SHOULD handle old or non-complying bundles that have superfluous intermediate and/or root CA certificates by either ignoring them or explicitly considering them untrusted for the purposes of chain building.

R-0009

<!-- q L101-102 -->
> 3. A single X.509 certificate, which MUST be a leaf certificate conveying the signing key.

R-0010

<!-- q L104-105 -->
> When used with the Public Good Instance (PGI) of Sigstore for "keyless" signing via Fulcio, form (1) MUST NOT be used, regardless of bundle version.

R-0011

<!-- q L105-106 -->
> Form (1) MAY be used with the PGI for self-managed keys.

R-0012

<!-- q L108-109 -->
> When used in a `0.1` or `0.2` bundle with the PGI and "keyless" signing, form (2) MUST be used.

R-0013

<!-- q L111-112 -->
> When used in a `0.3` bundle with the PGI and "keyless" signing, form (3) MUST be used.

R-0014

<!-- q L116-116 -->
> dev.sigstore.common.v1.PublicKeyIdentifier public_key = 1 [(google.api.field_behavior) = REQUIRED];

R-0015

<!-- q L118-118 -->
> dev.sigstore.common.v1.X509CertificateChain x509_certificate_chain = 2 [(google.api.field_behavior) = REQUIRED];

R-0016

<!-- q L120-120 -->
> dev.sigstore.common.v1.X509Certificate certificate = 5 [(google.api.field_behavior) = REQUIRED];

R-0017

<!-- q L125-127 -->
> Client verification libraries MAY provide an option to support v0.1 bundles for backwards compatibility, which may contain an inclusion promise and not an inclusion proof.

R-0018

<!-- q L127-128 -->
> In this case, the client MUST validate the promise.

R-0019

<!-- q L129-130 -->
> Verifiers SHOULD NOT allow v0.1 bundles if they're used in an ecosystem which never produced them.

R-0020

## §1.3

<!-- q L145-146 -->
> MUST be application/vnd.dev.sigstore.bundle.v0.3+json when when encoded as JSON.

R-0021

<!-- q L155-163 -->
> When a signer is identified by a X.509 certificate, a verifier MUST verify that the signature was computed at the time the certificate was valid as described in the Sigstore client spec: "Verification using a Bundle". <https://docs.google.com/document/d/1kbhK2qyPPk8SLavHzYSDM8-Ueul9_oxIMVFuWMWKz0E/edit#heading=h.x8bduppe89ln> If the verification material contains a public key identifier (key hint) and the `content` is a DSSE envelope, the key hints MUST be exactly the same in the verification material and in the DSSE envelope.

R-0022

<!-- q L165-165 -->
> VerificationMaterial verification_material = 2 [(google.api.field_behavior) = REQUIRED];

R-0023

<!-- q L169-169 -->
> dev.sigstore.common.v1.MessageSignature message_signature = 3 [(google.api.field_behavior) = REQUIRED];

R-0024

<!-- q L173-176 -->
> This is part of the DSSE protocol which is defined here: <https://github.com/secure-systems-lab/dsse/blob/master/protocol.md> DSSE envelopes in a bundle MUST have exactly one signature.

R-0025

<!-- q L180-183 -->
> 2. The bundle (currently) can only contain a single instance of the required verification materials During verification a client MUST reject an envelope if the number of signatures is not equal to one.

R-0026

<!-- q L185-185 -->
> io.intoto.Envelope dsse_envelope = 4 [(google.api.field_behavior) = REQUIRED];

R-0027

## §2.1

<!-- q L228-228 -->
> REQUIRED.

R-0028

<!-- q L233-233 -->
> REQUIRED.

R-0029

<!-- q L237-245 -->
> Signature over: PAE(type, payload) Where PAE is defined as: PAE(type, payload) = "DSSEv1" + SP + LEN(type) + SP + type + SP + LEN(payload) + SP + payload + = concatenation SP = ASCII space [0x20] "DSSEv1" = ASCII [0x44, 0x53, 0x53, 0x45, 0x76, 0x31] LEN(s) = ASCII decimal encoding of the byte length of s, with no leading zeros REQUIRED (length >= 1).

R-0030

## §2.2

<!-- q L256-256 -->
> REQUIRED.

R-0031

<!-- q L261-261 -->
> OPTIONAL.

R-0032

## §3.1

<!-- q L309-312 -->
> UNSPECIFIED SHOULD not be used, primary reason for inclusion is to force any proto JSON serialization to emit the used hash algorithm, as default option is to *omit* the default value of an enum (which is the first value, represented by '0'.

R-0033

## §3.2

<!-- q L345-345 -->
> Any changes to this enum MUST be reflected in the algorithm registry.

R-0034

<!-- q L415-416 -->
> In addition, LM-OTS is a single-use scheme, meaning that it MUST NOT be used for more than one signature per LM-OTS key.

R-0035

<!-- q L417-418 -->
> If you cannot maintain these invariants, you MUST NOT use these schemes.

R-0036

<!-- q L433-436 -->
> In the future they MAY be used by private Sigstore deployments, but they are not yet fully functional. This warning will be removed when these algorithms are widely supported by Sigstore clients and servers, but care should still be taken for production environments.

R-0037

## §3.4

<!-- q L475-476 -->
> Clients MUST NOT attempt to use this digest to verify the associated signature; it is intended solely for identification.

R-0038

<!-- q L486-487 -->
> When using a key pair, the algorithm MUST be part of the public key, which MUST be communicated out-of-band.

R-0039

<!-- q L489-489 -->
> bytes signature = 2 [(google.api.field_behavior) = REQUIRED];

R-0040

## §3.5

<!-- q L501-501 -->
> bytes key_id = 1 [(google.api.field_behavior) = REQUIRED];

R-0041

## §3.6

<!-- q L514-514 -->
> bytes signed_timestamp = 1 [(google.api.field_behavior) = REQUIRED];

R-0042

## §3.8

<!-- q L550-552 -->
> Implementors are RECOMMENDED to derive the value from the public key as described in RFC 6962. See: <https://www.rfc-editor.org/rfc/rfc6962#section-3.2>

R-0043

## §3.9

<!-- q L564-564 -->
> repeated int32 id = 1 [(google.api.field_behavior) = REQUIRED];

R-0044

## §3.12

<!-- q L596-596 -->
> bytes raw_bytes = 1 [(google.api.field_behavior) = REQUIRED];

R-0045

## §4.1

<!-- q L717-717 -->
> string kind = 1 [(google.api.field_behavior) = REQUIRED];

R-0046

<!-- q L721-721 -->
> string version = 2 [(google.api.field_behavior) = REQUIRED];

R-0047

## §4.2

<!-- q L727-728 -->
> The checkpoint MUST contain an origin string as a unique log identifier, the tree size, and the root hash.

R-0048

<!-- q L728-729 -->
> It MAY also be followed by optional data, and clients MUST NOT assume optional data.

R-0049

<!-- q L729-730 -->
> The checkpoint MUST also contain a signature over the root hash (tree head).

R-0050

<!-- q L730-731 -->
> The checkpoint MAY contain additional signatures, but the first SHOULD be the signature from the log.

R-0051

<!-- q L740-740 -->
> string envelope = 1 [(google.api.field_behavior) = REQUIRED];

R-0052

## §4.3

<!-- q L753-753 -->
> int64 log_index = 1 [(google.api.field_behavior) = REQUIRED];

R-0053

<!-- q L758-758 -->
> bytes root_hash = 2 [(google.api.field_behavior) = REQUIRED];

R-0054

<!-- q L762-762 -->
> int64 tree_size = 3 [(google.api.field_behavior) = REQUIRED];

R-0055

<!-- q L770-770 -->
> repeated bytes hashes = 4 [(google.api.field_behavior) = REQUIRED];

R-0056

<!-- q L775-775 -->
> Checkpoint checkpoint = 5 [(google.api.field_behavior) = REQUIRED];

R-0057

## §4.4

<!-- q L794-794 -->
> bytes signed_entry_timestamp = 1 [(google.api.field_behavior) = REQUIRED];

R-0058

## §4.5

<!-- q L813-813 -->
> int64 log_index = 1 [(google.api.field_behavior) = REQUIRED];

R-0059

<!-- q L817-817 -->
> dev.sigstore.common.v1.LogId log_id = 2 [(google.api.field_behavior) = REQUIRED];

R-0060

<!-- q L823-823 -->
> KindVersion kind_version = 3 [(google.api.field_behavior) = REQUIRED];

R-0061

<!-- q L826-827 -->
> The integration time MUST NOT be trusted if inclusion_promise is omitted.

R-0062

<!-- q L829-829 -->
> int64 integrated_time = 4 [(google.api.field_behavior) = REQUIRED];

R-0063

<!-- q L832-832 -->
> Required for v0.1 bundles, and MUST be verified.

R-0064

<!-- q L836-837 -->
> MUST be verified if no other suitable source of time is present, and SHOULD be verified otherwise.

R-0065

<!-- q L845-845 -->
> InclusionProof inclusion_proof = 6 [(google.api.field_behavior) = REQUIRED];

R-0066

<!-- q L860-862 -->
> If set, clients MUST verify that the signature referenced in the `canonicalized_body` matches the signature provided in the `Bundle.content`.

R-0067


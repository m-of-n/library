---
record: w3c-vc-data-integrity-1-0
kind: normative
title: "w3c-vc-data-integrity-1-0 — normative text"
generated_by: bin/fx1-skeleton
reviewed_by: ""
---

# Normative text

Generated verbatim by `bin/fx1-skeleton`; each quotation carries its
source lines and `bin/check-quotes` verifies it. Pass 1 adds the
keyword-less binding text (tables, IANA rules, lists) as
`<!-- q Lx-y -->` markers and lets `bin/check-quotes --render` write the words.

## §1.3

<!-- q L169-169 -->
> Conforming processors MUST produce errors when non-conforming documents are consumed.

R-0001

## §2.1

<!-- q L203-203 -->
> When expressing a data integrity proof on an object, a proof property MUST be used.

R-0002

<!-- q L203-205 -->
> If present, its value MUST be either a single object, or an unordered set of objects, expressed using the properties below: id An optional identifier for the proof, which MUST be a URL [URL], such as a UUID as a URN (urn:uuid:6a1676b8-b51f-11ed-937b-d76685a20ff5).

R-0003

<!-- q L205-207 -->
> The usage of this property is further explained in Section 2.1.2 Proof Chains. type The specific type of proof MUST be specified as a string that maps to a URL [URL].

R-0004

<!-- q L207-209 -->
> Proof types determine what other fields are required to secure and verify the proof. proofPurpose The reason the proof was created MUST be specified as a string that maps to a URL [URL].

R-0005

<!-- q L211-211 -->
> If included, the value MUST be a string that maps to a [URL].

R-0006

<!-- q L211-211 -->
> Inclusion of verificationMethod is OPTIONAL, but if it is not included, other properties such as cryptosuite might provide a mechanism by which to obtain the information necessary to verify the proof.

R-0007

<!-- q L213-213 -->
> If the proof type is DataIntegrityProof, cryptosuite MUST be specified; otherwise, cryptosuite MAY be specified.

R-0008

<!-- q L213-215 -->
> If specified, its value MUST be a string. created The date and time the proof was created is OPTIONAL and, if included, MUST be specified as an [XMLSCHEMA11-2] dateTimeStamp string, either in Universal Coordinated Time (UTC), denoted by a Z at the end of the value, or with a time zone offset relative to UTC.

R-0009

<!-- q L215-215 -->
> A conforming processor MAY chose to consume time values that were incorrectly serialized without an offset.

R-0010

<!-- q L215-217 -->
> Incorrectly serialized time values without an offset are to be interpreted as UTC. expires The expires property is OPTIONAL and, if present, specifies when the proof expires.

R-0011

<!-- q L217-217 -->
> If present, it MUST be an [XMLSCHEMA11-2] dateTimeStamp string, either in Universal Coordinated Time (UTC), denoted by a Z at the end of the value, or with a time zone offset relative to UTC.

R-0012

<!-- q L217-217 -->
> A conforming processor MAY chose to consume time values that were incorrectly serialized without an offset.

R-0013

<!-- q L217-219 -->
> Incorrectly serialized time values without an offset are to be interpreted as UTC. domain The domain property is OPTIONAL. It conveys one or more security domains in which the proof is meant to be used.

R-0014

<!-- q L219-219 -->
> If specified, the associated value MUST be either a string, or an unordered set of strings.

R-0015

<!-- q L219-219 -->
> A verifier SHOULD use the value to ensure that the proof was intended to be used in the security domain in which the verifier is operating.

R-0016

<!-- q L219-221 -->
> Example domain values include: domain.example (DNS domain), https://domain.example:8443 (Web origin), mycorp-intranet (bespoke text string), and b31d37d4-dd59-47d3-9dd8-c973da43b63a (UUID). challenge A string value that SHOULD be included in a proof if a domain is specified.

R-0017

<!-- q L223-223 -->
> The value MUST use a header and encoding as described in Section 2.4 Multibase of the Controlled Identifiers v1.0 specification to express the binary data.

R-0018

<!-- q L223-225 -->
> Alternative properties with different encodings specified by the cryptosuite MAY be used, instead of this property, to encode the data necessary to verify the digital proof. previousProof The previousProof property is OPTIONAL. If present, it MUST be a string value or an unordered list of string values.

R-0019

<!-- q L225-225 -->
> Each value identifies another data integrity proof, all of which MUST also verify for the current proof to be considered verified.

R-0020

<!-- q L225-227 -->
> This property is used in Section 2.1.2 Proof Chains. nonce An OPTIONAL string value supplied by the proof creator.

R-0021

## §2.3

<!-- q L388-388 -->
> To enable confirmation that a resource referenced by a conforming secured document has not changed since the document was secured, an implementer MAY include a property named digestMultibase in any object that includes an id property.

R-0022

<!-- q L388-388 -->
> If present, the digestMultibase value MUST be a single string value, or an list of string values, each of which is a Multibase-encoded Multihash value.

R-0023

## §2.4

<!-- q L406-415 -->
> Implementations that perform JSON-LD processing MUST treat the following JSON-LD context URLs as already resolved, where the resolved document matches the corresponding hash values below: | Context URL and Hash | URL: https://w3id.org/security/data-integrity/v2 SHA2-256 Digest: 67f21e6e33a6c14e5ccfd2fc7865f7474fb71a04af7e94136cb399dfac8ae8f4 | URL: https://w3id.org/security/multikey/v1 SHA2-256 Digest: ba2c182de2d92f7e47184bcca8fcf0beaee6d3986c527bf664c195bbc7c58597 | URL: https://w3id.org/security/jwk/v1 SHA2-256 Digest: 0f14b62f6071aafe00df265770ea0c7508e118247d79b7d861a406d2aa00bece It is possible to confirm the cryptographic digests listed above by running a command like the following (replacing <DOCUMENT_URL> with the appropriate value) through a modern UNIX-like OS command line interface: curl -sL -H "Accept: application/ld+json" <DOCUMENT_URL> | openssl dgst -sha256 The security vocabulary terms that the JSON-LD contexts listed above resolve to are in the https://w3id.org/security# namespace.

R-0024

<!-- q L416-416 -->
> Implementations that perform RDF processing MUST treat the JSON-LD serialization of the vocabulary URL as already dereferenced, where the dereferenced document matches the corresponding hash value below.

R-0025

<!-- q L426-428 -->
> SHA2-256 Digest: dadc810b5bb2c01a3caf276dc03a7c826311cddfefe86160a8c7d34704f50422 It is possible to confirm the cryptographic digests listed above by running a command like the following (replacing <MEDIA_TYPE> and <DOCUMENT_URL> with the appropriate values) through a modern UNIX-like OS command line interface: curl -sL -H "Accept: <MEDIA_TYPE>" <DOCUMENT_URL> | openssl dgst -sha256 Authors of application-specific vocabularies and specifications SHOULD ensure that their JSON-LD context and vocabulary files are permanently cacheable using the approaches to caching described above or a functionally equivalent mechanism.

R-0026

<!-- q L429-429 -->
> Implementations MAY load application-specific JSON-LD context files from the network during development, but SHOULD permanently cache JSON-LD context files used by conforming secured documents in production settings, to increase their security and privacy characteristics.

R-0027

<!-- q L429-429 -->
> Goals of processing speed MAY be achieved through caching approaches such as those described above or functionally equivalent mechanisms.

R-0028

## §2.4.1

<!-- q L435-435 -->
> Applications MUST use the algorithm in Section 4.6 Context Validation, or one that achieves equivalent protections, to validate contexts in a conforming secured document.

R-0029

<!-- q L435-435 -->
> Context validation MUST be run after running the applicable algorithm in either Section 4.4 Verify Proof or Section 4.5 Verify Proof Sets and Chains.

R-0030

<!-- q L436-436 -->
> While the algorithm described in Section 4.6 Context Validation provides one way of checking context values, and one optional way of safely processing unknown context values, implementers MAY use alternative approaches, or a different ordering of the steps, that provide the same protections.

R-0031

## §2.4.2

<!-- q L445-445 -->
> When an application is securing a document, if an @context property is not provided in the document or the Data Integrity terms used in the document are not mapped by existing values in the @context property, implementations SHOULD inject or append an @context property with a value of https://w3id.org/security/data-integrity/v2 or one or more contexts with at least the same declarations, such as the Verifiable Credential Data Model v2.0 context (https://www.w3.org/ns/credentials/v2).

R-0032

<!-- q L446-446 -->
> Implementations that do not intend to use JSON-LD processing MAY choose to not include an @context declaration at the top-level of the document.

R-0033

<!-- q L446-446 -->
> However, if an @context declaration is not included, extensions (such as the addition of new properties) related to this specification or corresponding cryptosuites MUST NOT be made.

R-0034

## §2.4.3

<!-- q L452-452 -->
> Implementations that use JSON-LD processing, such as RDF Dataset Canonicalization [RDF-CANON], MUST throw an error, which SHOULD be DATA_LOSS_DETECTION_ERROR, when data is dropped by a JSON-LD processor, such as when an undefined term is detected in an input document.

R-0035

<!-- q L453-453 -->
> When deserializing to RDF, implementations MUST ensure that the base URL is set to null.

R-0036

## §3

<!-- q L491-492 -->
> The requirements for all data integrity cryptographic suite specifications are as follows: The specification MUST be published as a human-readable document at a URL.

R-0037

<!-- q L493-493 -->
> The specification MUST identify a cryptographic suite type and any parameters that can be used with the suite.

R-0038

<!-- q L494-494 -->
> The specification MUST detail the transformation algorithms (if any), parameters, and other necessary details, used to modify input data into the data to be protected.

R-0039

<!-- q L495-495 -->
> The specification MUST detail the hashing algorithms parameters, and other necessary details used to perform cryptographic hashing to the data to be protected.

R-0040

<!-- q L496-496 -->
> The specification MUST detail the proof serialization algorithms, parameters, and other necessary details used to perform cryptographic protection of the data.

R-0041

<!-- q L497-497 -->
> The specification MUST detail the proof verification algorithms, parameters, and other necessary details used to perform cryptographic verification of the data.

R-0042

<!-- q L498-498 -->
> The specification MUST define a data integrity cryptographic suite instantiation algorithm that accepts a set of options (map options) and returns a cryptosuite instance (struct cryptosuite).

R-0043

<!-- q L498-498 -->
> This algorithm SHOULD be listed in the Verifiable Credential Extensions document.

R-0044

<!-- q L507-507 -->
> The structure MAY contain other implementation-specific information that is useful for developers, such as debugging information.

R-0045

<!-- q L508-508 -->
> The specification MUST detail any known resource starvation attack that can occur in an algorithm and provide testable mitigations against each attack.

R-0046

<!-- q L509-509 -->
> The specification MUST contain a Security Considerations section detailing security considerations specific to the cryptographic suite.

R-0047

<!-- q L510-510 -->
> The specification MUST contain a Privacy Considerations section detailing privacy considerations specific to the cryptographic suite.

R-0048

<!-- q L511-511 -->
> The JSON-LD context associated with the cryptographic suite MUST have its terms protected from unsafe redefinition, by use of the @protected keyword.

R-0049

<!-- q L512-512 -->
> Implementations MAY use the Verifiable Credential Extensions document to discover known cryptosuite instantiation algorithms.

R-0050

## §3.1

<!-- q L517-521 -->
> When specifing a cryptographic suite that utilizes this design pattern, the proof value takes the following form: type The type property MUST contain the string DataIntegrityProof. cryptosuite The value of the cryptosuite property MUST be a string that identifies the cryptographic suite.

R-0051

<!-- q L521-523 -->
> If the processing environment supports string subtypes, the subtype of the cryptosuite value MUST be the https://w3id.org/security#cryptosuiteString subtype. proofValue The proofValue property MUST be used, as specified in Section 2.1 Proofs.

R-0052

<!-- q L524-524 -->
> Cryptographic suite designers MUST use mandatory proof value properties defined in Section 2.1 Proofs, and MAY define other properties specific to their cryptographic suite.

R-0053

<!-- q L527-527 -->
> To improve the developer experience, authors creating new Data Integrity cryptographic suite specifications SHOULD use the modern pattern — where the type is set to DataIntegrityProof; the cryptosuite property carries the identifier for the cryptosuite; and any cryptosuite-specific cryptographic data is encapsulated (i.e., not directly exposed as application layer data) within proofValue.

R-0054

## §4

<!-- q L531-531 -->
> An input document is an map that has not yet had the current proof added to it, but it MAY contain a proof value that was added to it by a previous process.

R-0055

<!-- q L532-532 -->
> Implementers MAY implement reasonable defaults and safeguards in addition to the algorithms below, to help mitigate developer error, excessive resource consumption, newly discovered attack models against which there is a particular protection, and other improvements.

R-0056

## §4.2

<!-- q L549-549 -->
> Whenever this algorithm encodes strings, it MUST use UTF-8 encoding.

R-0057

<!-- q L550-550 -->
> If the algorithm produces an error, the error MUST be propagated and SHOULD convey the error type.

R-0058

<!-- q L551-551 -->
> If one or more of the proof.type, proof.verificationMethod, and proof.proofPurpose values is not set, an error MUST be raised and SHOULD convey an error type of PROOF_GENERATION_ERROR.

R-0059

<!-- q L552-552 -->
> If options has a non-null domain item, it MUST be equal to proof.domain or an error MUST be raised and SHOULD convey an error type of PROOF_GENERATION_ERROR.

R-0060

<!-- q L553-553 -->
> If options has a non-null challenge item, it MUST be equal to proof.challenge or an error MUST be raised and SHOULD convey an error type of PROOF_GENERATION_ERROR.

R-0061

## §4.3

<!-- q L560-560 -->
> Whenever this algorithm encodes strings, it MUST use UTF-8 encoding.

R-0062

<!-- q L564-564 -->
> If a proof with id equal to previousProof does not exist in allProofs, an error MUST be raised and SHOULD convey an error type of PROOF_GENERATION_ERROR.

R-0063

<!-- q L565-565 -->
> If any element of previousProof list has an id attribute that does not match the id attribute of any element of allProofs, an error MUST be raised and SHOULD convey an error type of PROOF_GENERATION_ERROR.

R-0064

## §4.4

<!-- q L583-599 -->
> See 2.2 Proof Purposes for common values domain An optional set of strings, used by the proof creator to lock a proof to a particular security domain, and used by the verifier to ensure that a proof is not being used across different security domains challenge An optional string challenge, used by the verifier to ensure that an attacker is not replaying previously created proofs This algorithm returns a verification result, a struct whose items are: verified true or false verifiedDocument Null, if verified is false; otherwise, an input document mediaType Null, if verified is false; otherwise, a media type, which MAY include parameters warnings a list of ProblemDetails, which defaults to an empty list errors a list of ProblemDetails, which defaults to an empty list When a step says "an error MUST be raised", it means that a verification result MUST be returned with a verified value of false and a non-empty errors list.

R-0065

<!-- q L601-601 -->
> If either securedDocument is not a map or securedDocument.proof is not a map, an error MUST be raised and SHOULD convey an error type of PARSING_ERROR.

R-0066

<!-- q L603-603 -->
> If one or more of proof.type, proof.verificationMethod, and proof.proofPurpose does not exist, an error MUST be raised and SHOULD convey an error type of PROOF_VERIFICATION_ERROR.

R-0067

<!-- q L604-604 -->
> If expectedProofPurpose was given, and it does not match proof.proofPurpose, an error MUST be raised and SHOULD convey an error type of PROOF_VERIFICATION_ERROR.

R-0068

<!-- q L605-605 -->
> If domain was given, and it does not contain the same strings as proof.domain (treating a single string as a set containing just that string), an error MUST be raised and SHOULD convey an error type of INVALID_DOMAIN_ERROR.

R-0069

<!-- q L606-606 -->
> If challenge was given, and it does not match proof.challenge, an error MUST be raised and SHOULD convey an error type of INVALID_CHALLENGE_ERROR.

R-0070

## §4.5

<!-- q L619-619 -->
> Implementations MAY return any of the other verification results and/or any other metadata alongside the combined verification result.

R-0071

<!-- q L624-624 -->
> If a proof with id value equal to the value of previousProof does not exist in allProofs, an error MUST be raised and SHOULD convey an error type of PROOF_VERIFICATION_ERROR.

R-0072

<!-- q L624-624 -->
> If any element of previousProof list has an id attribute value that does not match the id attribute value of any element of allProofs, an error MUST be raised and SHOULD convey an error type of PROOF_VERIFICATION_ERROR.

R-0073

## §4.6

<!-- q L657-657 -->
> Implementations MAY include additional warnings or errors that enforce further validation rules that are specific to the implementation or a particular use case.

R-0074

## §4.7

<!-- q L662-662 -->
> When exposing these errors through an HTTP interface, implementers SHOULD use [RFC9457] to encode the error data structure as a ProblemDetails map.

R-0075

<!-- q L662-663 -->
> If [RFC9457] is used: The type value of the error object MUST be a URL that starts with the value https://w3id.org/security# and ends with the value in the section listed below.

R-0076

<!-- q L664-664 -->
> The title value SHOULD provide a short but specific human-readable string for the error.

R-0077

<!-- q L665-665 -->
> The detail value SHOULD provide a longer human-readable string for the error.

R-0078


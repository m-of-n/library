---
record: w3c-vc-data-integrity-1-0
kind: normative
title: "w3c-vc-data-integrity-1-0 — normative text"
generated_by: bin/fx1-skeleton
extracted: "2026-11-07"
reviewed_by: ""
---

# Normative text

Every normative statement of W3C Recommendation 15 May 2025 (REC-vc-data-integrity-20250515), in source order,
as quotation markers whose words `bin/check-quotes --render` writes from `.cache/w3c-vc-data-integrity-1-0.txt`
(the one-line-per-HTML-block rendering of the HTML of record; line numbers count there). Nothing below the markers was typed.

Built by pass 1 (requirements agent) over the `bin/fx1-skeleton` layer. Each quotation is the full text of one entry of
`requirements.yaml`, its id on the line after it. The skeleton found the BCP 14 sentences; this pass added the
keyword-less binding text (verb none): the §4 algorithm steps, the §2 data-model definitions, the §3 and §4 struct items,
the §4.7 error definitions and the few §2, §5 and §6 sentences phrased as necessity. A parent sentence that welds
several clauses or keywords lists its `split_of` children, whose texts are sub-spans of the quotation above them.
Inferred entries are not source text and are named in place without a quotation.

What is normative. §1.3 ¶1 makes non-normative every section marked as such and all authoring guidelines, diagrams,
examples and notes; everything else is normative. So §5 (Security), §6 (Privacy) and §7 (Accessibility) are normative
sections, though almost all of their text is advisory and is not quoted here (see the candidate verdicts).

## Non-normative parts (not quoted, keywords accounted for)

- Sections marked non-normative: §1, §1.1, §1.2 (lines 122 to 161); Appendices A, B and C (lines 836 to 987). No BCP 14 keyword.
- Notes (HTML `div.note`): lines 160-161, 277-278, 417-418, 478-479, 525-527, 567-568, 626-627. One keyword, at line 527, below.
- Examples (14, HTML `div.example`; fixtures come from the HTML `pre` elements, not the .txt): no keyword.
- §1.3 and §1.4 sit inside the informative section element of §1 without a marker of their own; read as normative (SD-1).

### The one keyword in non-normative text

Inside the Note of §3.1; the skeleton's R-0054, kept in requirements.yaml with status withdrawn so its id resolves and binds nothing (SD-2):

<!-- q L527 "To improve" .. "within proofValue." -->
> To improve the developer experience, authors creating new Data Integrity cryptographic suite specifications SHOULD use the modern pattern — where the type is set to DataIntegrityProof; the cryptosuite property carries the identifier for the cryptosuite; and any cryptosuite-specific cryptographic data is encapsulated (i.e., not directly exposed as application layer data) within proofValue.

R-0054 (SHOULD, withdrawn)


## §1.3 Conformance

<!-- q L167 -->
> A conforming secured document is any byte sequence that can be converted to a JSON document that follows the relevant normative requirements in Sections 2.1 Proofs, 2.2 Proof Purposes, 2.3 Resource Integrity, 2.4 Contexts and Vocabularies, and 3.1 DataIntegrityProof.

R-0079 (none)

<!-- q L168 -->
> A conforming cryptographic suite specification is any specification that follows the relevant normative requirements in Section 3. Cryptographic Suites.

R-0080 (none)

<!-- q L169 "A conforming" .. "4. Algorithms." -->
> A conforming processor is any algorithm realized as software and/or hardware that generates and/or consumes a conforming secured document according to the relevant normative statements in Section 4. Algorithms.

R-0081 (none)

<!-- q L169 "Conforming processors" .. "are consumed." -->
> Conforming processors MUST produce errors when non-conforming documents are consumed.

R-0001 (MUST)

## §2 Data Model

<!-- q L195 -->
> All of the data model properties and types in this specification map to URLs. The vocabulary where these URLs are defined is the The Security Vocabulary. The explicit mechanism that is used to perform this mapping in a secured document is the @context property.

R-0082 (none)

<!-- q L196 "The mapping" .. "JSON-LD 1.1." -->
> The mapping mechanism is defined by JSON-LD 1.1.

R-0083 (none)

## §2.1 Proofs

<!-- q L203 "When expressing" .. "be used." -->
> When expressing a data integrity proof on an object, a proof property MUST be used.

R-0002 (MUST)

<!-- q L203 "The proof" .. "named graph." -->
> The proof property within a verifiable credential is a named graph.

R-0084 (none)

<!-- q L203-205 "If present," .. "URN (urn:uuid:6a1676b8-b51f-11ed-937b-d76685a20ff5)." -->
> If present, its value MUST be either a single object, or an unordered set of objects, expressed using the properties below: id An optional identifier for the proof, which MUST be a URL [URL], such as a UUID as a URN (urn:uuid:6a1676b8-b51f-11ed-937b-d76685a20ff5).

R-0003 (MUST) → split: R-0085 (MUST), R-0086 (MUST)

<!-- q L205-207 "The usage" .. "URL [URL]." -->
> The usage of this property is further explained in Section 2.1.2 Proof Chains. type The specific type of proof MUST be specified as a string that maps to a URL [URL].

R-0004 (MUST) → split: R-0087 (MUST)

<!-- q L207-209 "Proof types" .. "URL [URL]." -->
> Proof types determine what other fields are required to secure and verify the proof. proofPurpose The reason the proof was created MUST be specified as a string that maps to a URL [URL].

R-0005 (MUST) → split: R-0088 (none), R-0089 (MUST)

Inferred, not verbatim: R-0288 (coverage of proof options by the proof value). See requirements.yaml.

<!-- q L211 "If included," .. "a [URL]." -->
> If included, the value MUST be a string that maps to a [URL].

R-0006 (MUST)

<!-- q L211 "Inclusion of" .. "the proof." -->
> Inclusion of verificationMethod is OPTIONAL, but if it is not included, other properties such as cryptosuite might provide a mechanism by which to obtain the information necessary to verify the proof.

R-0007 (OPTIONAL)

Inferred, not verbatim: R-0090 (presence of verificationMethod in practice). See requirements.yaml.

<!-- q L211 "Note that" .. "the proof." -->
> Note that when verificationMethod is expressed in a data integrity proof, the value points to the actual location of the data; that is, the verificationMethod references, via a URL, the location of the public key that can be used to verify the proof.

R-0091 (none)

<!-- q L211 "This public" .. "verification method." -->
> This public key data is stored in a controlled identifier document, which contains a full description of the verification method.

R-0092 (none)

<!-- q L213 "An identifier" .. "the proof." -->
> An identifier for the cryptographic suite that can be used to verify the proof.

R-0093 (none)

<!-- q L213 "If the" .. "be specified." -->
> If the proof type is DataIntegrityProof, cryptosuite MUST be specified; otherwise, cryptosuite MAY be specified.

R-0008 (MUST) → split: R-0094 (MUST), R-0095 (MAY)

<!-- q L213-215 "If specified," .. "to UTC." -->
> If specified, its value MUST be a string. created The date and time the proof was created is OPTIONAL and, if included, MUST be specified as an [XMLSCHEMA11-2] dateTimeStamp string, either in Universal Coordinated Time (UTC), denoted by a Z at the end of the value, or with a time zone offset relative to UTC.

R-0009 (MUST) → split: R-0096 (MUST), R-0097 (OPTIONAL), R-0098 (MUST)

<!-- q L215 "A conforming" .. "an offset." -->
> A conforming processor MAY chose to consume time values that were incorrectly serialized without an offset.

R-0010 (MAY)

<!-- q L215-217 "Incorrectly serialized" .. "proof expires." -->
> Incorrectly serialized time values without an offset are to be interpreted as UTC. expires The expires property is OPTIONAL and, if present, specifies when the proof expires.

R-0011 (OPTIONAL) → split: R-0099 (none), R-0100 (OPTIONAL)

<!-- q L217 "If present," .. "to UTC." -->
> If present, it MUST be an [XMLSCHEMA11-2] dateTimeStamp string, either in Universal Coordinated Time (UTC), denoted by a Z at the end of the value, or with a time zone offset relative to UTC.

R-0012 (MUST)

<!-- q L217 "A conforming" .. "an offset." -->
> A conforming processor MAY chose to consume time values that were incorrectly serialized without an offset.

R-0013 (MAY)

<!-- q L217-219 "Incorrectly serialized" .. "be used." -->
> Incorrectly serialized time values without an offset are to be interpreted as UTC. domain The domain property is OPTIONAL. It conveys one or more security domains in which the proof is meant to be used.

R-0014 (OPTIONAL) → split: R-0101 (none), R-0102 (OPTIONAL), R-0103 (none)

<!-- q L219 "If specified," .. "of strings." -->
> If specified, the associated value MUST be either a string, or an unordered set of strings.

R-0015 (MUST)

<!-- q L219 "A verifier" .. "is operating." -->
> A verifier SHOULD use the value to ensure that the proof was intended to be used in the security domain in which the verifier is operating.

R-0016 (SHOULD)

<!-- q L219-221 "Example domain" .. "is specified." -->
> Example domain values include: domain.example (DNS domain), https://domain.example:8443 (Web origin), mycorp-intranet (bespoke text string), and b31d37d4-dd59-47d3-9dd8-c973da43b63a (UUID). challenge A string value that SHOULD be included in a proof if a domain is specified.

R-0017 (SHOULD) → split: R-0104 (SHOULD)

<!-- q L221 "The value" .. "of time." -->
> The value is used once for a particular domain and window of time.

R-0105 (none)

<!-- q L223 "A string" .. "verificationMethod specified." -->
> A string value that expresses base-encoded binary data necessary to verify the digital proof using the verificationMethod specified.

R-0106 (none)

<!-- q L223 "The value" .. "binary data." -->
> The value MUST use a header and encoding as described in Section 2.4 Multibase of the Controlled Identifiers v1.0 specification to express the binary data.

R-0018 (MUST)

<!-- q L223 "The contents" .. "that cryptosuite." -->
> The contents of this value are determined by a specific cryptosuite and set to the proof value generated by the Add Proof Algorithm for that cryptosuite.

R-0107 (none)

<!-- q L223-225 "Alternative properties" .. "string values." -->
> Alternative properties with different encodings specified by the cryptosuite MAY be used, instead of this property, to encode the data necessary to verify the digital proof. previousProof The previousProof property is OPTIONAL. If present, it MUST be a string value or an unordered list of string values.

R-0019 (MUST) → split: R-0108 (MAY), R-0109 (OPTIONAL), R-0110 (MUST)

<!-- q L225 "Each value" .. "considered verified." -->
> Each value identifies another data integrity proof, all of which MUST also verify for the current proof to be considered verified.

R-0020 (MUST)

<!-- q L225-227 "This property" .. "proof creator." -->
> This property is used in Section 2.1.2 Proof Chains. nonce An OPTIONAL string value supplied by the proof creator.

R-0021 (OPTIONAL) → split: R-0111 (OPTIONAL)

## §2.1.1 Proof Sets

<!-- q L303 "A proof set," .. "a document." -->
> A proof set, which has no order, is represented by associating a set of proofs with the proof key in a document.

R-0112 (none)

## §2.1.2 Proof Chains

<!-- q L333 "A proof chain," .. "previous proof." -->
> A proof chain, where proof order needs to be preserved, is expressed by providing at least one proof with an id, such as a UUID [RFC9562], and another proof with a previousProof value that identifies the previous proof.

R-0113 (none)

## §2.1.3 Proof Graphs

<!-- q L365 "When securing" .. "proof graph." -->
> When securing data in a document, it is important to clearly delineate the data being protected, which is every graph expressed in the document except the one containing the data associated with a securing mechanism, which is called a proof graph.

R-0114 (none)

<!-- q L366 "To ensure" .. "single data integrity proof." -->
> To ensure that information from different data integrity proofs is not accidentally co-mingled, the concept of a proof graph is used to encapsulate each data integrity proof. Each value associated with the proof property of the document identifies a separate graph, which is sometimes referred to as a named graph, of type ProofGraph, which contains a single data integrity proof.

R-0115 (none)

<!-- q L367 "It is" .. "same entity." -->
> It is important to not merge objects that seem to have similar properties, when those objects do not have an id property and/or use a global identifier type such as a URL, as without these, is not possible to tell whether two such objects are expressing information about the same entity.

R-0116 (none)

## §2.2 Proof Purposes

<!-- q L374-375 -->
> authentication Indicates that a given proof is only to be used for the purposes of an authentication protocol.

R-0117 (none)

<!-- q L376-377 -->
> assertionMethod Indicates that a proof can only be used for making assertions, for example signing a verifiable credential.

R-0118 (none)

<!-- q L378-379 -->
> keyAgreement Indicates that a proof is used for for key agreement protocols, such as Elliptic Curve Diffie Hellman key agreement used by popular encryption libraries.

R-0119 (none)

<!-- q L380-381 "capabilityDelegation Indicates" .. "delegating capabilities." -->
> capabilityDelegation Indicates that the proof can only be used for delegating capabilities.

R-0120 (none)

<!-- q L382-383 "capabilityInvocation Indicates" .. "invoking capabilities." -->
> capabilityInvocation Indicates that the proof can only be used for invoking capabilities.

R-0121 (none)

## §2.3 Resource Integrity

<!-- q L388 "To enable" .. "id property." -->
> To enable confirmation that a resource referenced by a conforming secured document has not changed since the document was secured, an implementer MAY include a property named digestMultibase in any object that includes an id property.

R-0022 (MAY)

<!-- q L388 "If present," .. "Multihash value." -->
> If present, the digestMultibase value MUST be a single string value, or an list of string values, each of which is a Multibase-encoded Multihash value.

R-0023 (MUST)

Inferred, not verbatim: R-0122 (integrity check of a referenced resource). See requirements.yaml.

<!-- q L389 "JSON-LD context" .. "cryptographic digest." -->
> JSON-LD context authors are expected to add digestMultibase to contexts that will be used in documents that refer to other resources and to include an associated cryptographic digest.

R-0123 (none)

## §2.4 Contexts and Vocabularies

<!-- q L406-415 "Implementations that" .. "https://w3id.org/security# namespace." -->
> Implementations that perform JSON-LD processing MUST treat the following JSON-LD context URLs as already resolved, where the resolved document matches the corresponding hash values below: | Context URL and Hash | URL: https://w3id.org/security/data-integrity/v2 SHA2-256 Digest: 67f21e6e33a6c14e5ccfd2fc7865f7474fb71a04af7e94136cb399dfac8ae8f4 | URL: https://w3id.org/security/multikey/v1 SHA2-256 Digest: ba2c182de2d92f7e47184bcca8fcf0beaee6d3986c527bf664c195bbc7c58597 | URL: https://w3id.org/security/jwk/v1 SHA2-256 Digest: 0f14b62f6071aafe00df265770ea0c7508e118247d79b7d861a406d2aa00bece It is possible to confirm the cryptographic digests listed above by running a command like the following (replacing <DOCUMENT_URL> with the appropriate value) through a modern UNIX-like OS command line interface: curl -sL -H "Accept: application/ld+json" <DOCUMENT_URL> | openssl dgst -sha256 The security vocabulary terms that the JSON-LD contexts listed above resolve to are in the https://w3id.org/security# namespace.

R-0024 (MUST) → split: R-0124 (MUST), R-0125 (none), R-0126 (none), R-0127 (none), R-0128 (none), R-0129 (none)

<!-- q L415 "That is," .. "a term." -->
> That is, all security terms in this vocabulary are of the form https://w3id.org/security#TERM, where TERM is the name of a term.

R-0130 (none)

<!-- q L416 -->
> Implementations that perform RDF processing MUST treat the JSON-LD serialization of the vocabulary URL as already dereferenced, where the dereferenced document matches the corresponding hash value below.

R-0025 (MUST)

<!-- q L419 "When dereferencing" .. "content negotiation." -->
> When dereferencing the https://w3id.org/security# URL, the media type of the data that is returned depends on HTTP content negotiation.

R-0131 (none)

<!-- q L421-422 "application/ld+json |" .. "Digest: 082434d5b742418753bbc5d593f93b66d4f1ccf1c627417c0caa2dea40728245" -->
> application/ld+json | The vocabulary in JSON-LD format [JSON-LD11]. SHA2-256 Digest: 082434d5b742418753bbc5d593f93b66d4f1ccf1c627417c0caa2dea40728245

R-0132 (none)

<!-- q L423-424 "text/turtle |" .. "Digest: 9a5ba1e23f54b9adc9c39429f5eb3bd672cb392495cc4159561462921e012b37" -->
> text/turtle | The vocabulary in Turtle format [TURTLE]. SHA2-256 Digest: 9a5ba1e23f54b9adc9c39429f5eb3bd672cb392495cc4159561462921e012b37

R-0133 (none)

<!-- q L425-426 "text/html |" .. "Digest: dadc810b5bb2c01a3caf276dc03a7c826311cddfefe86160a8c7d34704f50422" -->
> text/html | The vocabulary in HTML+RDFa Format [HTML-RDFA]. SHA2-256 Digest: dadc810b5bb2c01a3caf276dc03a7c826311cddfefe86160a8c7d34704f50422

R-0134 (none)

<!-- q L426-428 -->
> SHA2-256 Digest: dadc810b5bb2c01a3caf276dc03a7c826311cddfefe86160a8c7d34704f50422 It is possible to confirm the cryptographic digests listed above by running a command like the following (replacing <MEDIA_TYPE> and <DOCUMENT_URL> with the appropriate values) through a modern UNIX-like OS command line interface: curl -sL -H "Accept: <MEDIA_TYPE>" <DOCUMENT_URL> | openssl dgst -sha256 Authors of application-specific vocabularies and specifications SHOULD ensure that their JSON-LD context and vocabulary files are permanently cacheable using the approaches to caching described above or a functionally equivalent mechanism.

R-0026 (SHOULD) → split: R-0135 (none), R-0136 (SHOULD)

<!-- q L429 "Implementations MAY" .. "privacy characteristics." -->
> Implementations MAY load application-specific JSON-LD context files from the network during development, but SHOULD permanently cache JSON-LD context files used by conforming secured documents in production settings, to increase their security and privacy characteristics.

R-0027 (SHOULD) → split: R-0137 (MAY), R-0138 (SHOULD)

<!-- q L429 "Goals of" .. "equivalent mechanisms." -->
> Goals of processing speed MAY be achieved through caching approaches such as those described above or functionally equivalent mechanisms.

R-0028 (MAY)

## §2.4.1 Validating Contexts

<!-- q L435 "It is" .. "will process." -->
> It is necessary to ensure that a consuming application has explicitly approved of the types, and therefore the semantics, of input documents that it will process.

R-0139 (none)

<!-- q L435 "Applications MUST" .. "secured document." -->
> Applications MUST use the algorithm in Section 4.6 Context Validation, or one that achieves equivalent protections, to validate contexts in a conforming secured document.

R-0029 (MUST)

<!-- q L435 "Context validation" .. "and Chains." -->
> Context validation MUST be run after running the applicable algorithm in either Section 4.4 Verify Proof or Section 4.5 Verify Proof Sets and Chains.

R-0030 (MUST)

<!-- q L436 -->
> While the algorithm described in Section 4.6 Context Validation provides one way of checking context values, and one optional way of safely processing unknown context values, implementers MAY use alternative approaches, or a different ordering of the steps, that provide the same protections.

R-0031 (MAY)

## §2.4.2 Context Injection

<!-- q L445 -->
> When an application is securing a document, if an @context property is not provided in the document or the Data Integrity terms used in the document are not mapped by existing values in the @context property, implementations SHOULD inject or append an @context property with a value of https://w3id.org/security/data-integrity/v2 or one or more contexts with at least the same declarations, such as the Verifiable Credential Data Model v2.0 context (https://www.w3.org/ns/credentials/v2).

R-0032 (SHOULD)

<!-- q L446 "Implementations that" .. "the document." -->
> Implementations that do not intend to use JSON-LD processing MAY choose to not include an @context declaration at the top-level of the document.

R-0033 (MAY)

<!-- q L446 "However, if" .. "be made." -->
> However, if an @context declaration is not included, extensions (such as the addition of new properties) related to this specification or corresponding cryptosuites MUST NOT be made.

R-0034 (MUST NOT)

## §2.4.3 Securing Data Losslessly

<!-- q L451 "This specification" .. "of developers." -->
> This specification requires that any recoverable loss of data when performing JSON-LD transformations result in an error, to avoid a mismatch in the security expectations of developers.

R-0140 (none)

<!-- q L452 -->
> Implementations that use JSON-LD processing, such as RDF Dataset Canonicalization [RDF-CANON], MUST throw an error, which SHOULD be DATA_LOSS_DETECTION_ERROR, when data is dropped by a JSON-LD processor, such as when an undefined term is detected in an input document.

R-0035 (MUST) → split: R-0141 (MUST), R-0142 (SHOULD)

<!-- q L453 "Similarly, since" .. "the document." -->
> Similarly, since conforming secured documents can be transferred from one security domain to another, conforming processors that process the conforming secured document cannot assume any particular base URL for the document.

R-0143 (none)

<!-- q L453 "When deserializing" .. "to null." -->
> When deserializing to RDF, implementations MUST ensure that the base URL is set to null.

R-0036 (MUST)

Inferred, not verbatim: R-0144 (relative URLs in a secured document). See requirements.yaml.

## §2.4.4.1 The cryptosuiteString Datatype

<!-- q L461 "In environments" .. "to https://w3id.org/security#cryptosuiteString." -->
> In environments that support data types for string values, such as RDF [RDF-CONCEPTS], cryptographic identifier content is indicated using a literal value whose datatype is set to https://w3id.org/security#cryptosuiteString.

R-0145 (none)

<!-- q L463-464 -->
> The URL denoting this datatype https://w3id.org/security#cryptosuiteString

R-0146 (none)

<!-- q L465-466 -->
> The lexical space The union of all cryptosuite strings, expressed using American Standard Code for Information Interchange [ASCII] strings, that are defined by the collection of all Data Integrity cryptosuite specifications.

R-0147 (none)

<!-- q L467-468 -->
> The value space The union of all cryptosuite types that are expressed using the cryptosuite property, as defined in Section 3.1 DataIntegrityProof.

R-0148 (none)

<!-- q L469-470 -->
> The lexical-to-value mapping Any element of the lexical space is mapped to the result of parsing it into an internal representation that uniquely identifies the cryptosuite type from all other possible cryptosuite types.

R-0149 (none)

<!-- q L471-472 -->
> The canonical mapping Any element of the value space is mapped to the corresponding string in the lexical space.

R-0150 (none)

## §2.6 Relationship to Verifiable Credentials

<!-- q L485 "When verifying" .. "expires )." -->
> When verifying a proof, it is important to ensure that the time of interest (which might be the current time or any other time) is within the validity period for the proof (that is, between created and expires ).

R-0151 (none)

Inferred, not verbatim: R-0152 (validity period of a proof). See requirements.yaml.

<!-- q L485 "When validating" .. "and validUntil)." -->
> When validating a verifiable credential, it is important to ensure that the time of interest is within the validity period for the credential (that is, betweeen validFrom and validUntil).

R-0153 (none)

## §3 Cryptographic Suites

<!-- q L491-492 -->
> The requirements for all data integrity cryptographic suite specifications are as follows: The specification MUST be published as a human-readable document at a URL.

R-0037 (MUST) → split: R-0154 (MUST)

<!-- q L493 -->
> The specification MUST identify a cryptographic suite type and any parameters that can be used with the suite.

R-0038 (MUST)

<!-- q L494 -->
> The specification MUST detail the transformation algorithms (if any), parameters, and other necessary details, used to modify input data into the data to be protected.

R-0039 (MUST)

<!-- q L495 -->
> The specification MUST detail the hashing algorithms parameters, and other necessary details used to perform cryptographic hashing to the data to be protected.

R-0040 (MUST)

<!-- q L496 -->
> The specification MUST detail the proof serialization algorithms, parameters, and other necessary details used to perform cryptographic protection of the data.

R-0041 (MUST)

<!-- q L497 -->
> The specification MUST detail the proof verification algorithms, parameters, and other necessary details used to perform cryptographic verification of the data.

R-0042 (MUST)

<!-- q L498 "The specification" .. "(struct cryptosuite)." -->
> The specification MUST define a data integrity cryptographic suite instantiation algorithm that accepts a set of options (map options) and returns a cryptosuite instance (struct cryptosuite).

R-0043 (MUST)

<!-- q L498 "This algorithm" .. "Extensions document." -->
> This algorithm SHOULD be listed in the Verifiable Credential Extensions document.

R-0044 (SHOULD)

<!-- q L499-500 -->
> createProof An algorithm that takes an input document (map inputDocument) and proof options (map options) as input, and produces a data integrity proof (map) or an error.

R-0155 (none)

<!-- q L501-502 "verifyProof An" .. "an error." -->
> verifyProof An algorithm that takes a secured data document (map securedDocument) as input, and produces a cryptosuite verification result or an error.

R-0156 (none)

<!-- q L502-504 "The cryptosuite" .. "false otherwise." -->
> The cryptosuite verification result is a struct that contains the following items: verified A boolean that is true if the verification succeeded, or false otherwise.

R-0157 (none)

<!-- q L505-506 -->
> verifiedDocument A map that represents the secured data document with the verified proofs removed if verified is true, or null otherwise.

R-0158 (none)

<!-- q L507 "The structure" .. "debugging information." -->
> The structure MAY contain other implementation-specific information that is useful for developers, such as debugging information.

R-0045 (MAY)

<!-- q L507 "If an" .. "to complete." -->
> If an error is produced, the verification process failed to complete.

R-0159 (none)

<!-- q L507 "An error," .. "would fail." -->
> An error, such as a network error, does not mean that a future attempt at verification would fail.

R-0160 (none)

<!-- q L508 -->
> The specification MUST detail any known resource starvation attack that can occur in an algorithm and provide testable mitigations against each attack.

R-0046 (MUST)

<!-- q L509 -->
> The specification MUST contain a Security Considerations section detailing security considerations specific to the cryptographic suite.

R-0047 (MUST)

<!-- q L510 -->
> The specification MUST contain a Privacy Considerations section detailing privacy considerations specific to the cryptographic suite.

R-0048 (MUST)

<!-- q L511 -->
> The JSON-LD context associated with the cryptographic suite MUST have its terms protected from unsafe redefinition, by use of the @protected keyword.

R-0049 (MUST)

<!-- q L512 "Implementations MAY" .. "instantiation algorithms." -->
> Implementations MAY use the Verifiable Credential Extensions document to discover known cryptosuite instantiation algorithms.

R-0050 (MAY)

## §3.1 DataIntegrityProof

<!-- q L517-521 "When specifing" .. "cryptographic suite." -->
> When specifing a cryptographic suite that utilizes this design pattern, the proof value takes the following form: type The type property MUST contain the string DataIntegrityProof. cryptosuite The value of the cryptosuite property MUST be a string that identifies the cryptographic suite.

R-0051 (MUST) → split: R-0161 (MUST), R-0162 (MUST)

<!-- q L521-523 "If the" .. "2.1 Proofs." -->
> If the processing environment supports string subtypes, the subtype of the cryptosuite value MUST be the https://w3id.org/security#cryptosuiteString subtype. proofValue The proofValue property MUST be used, as specified in Section 2.1 Proofs.

R-0052 (MUST) → split: R-0163 (MUST), R-0164 (MUST)

<!-- q L524 -->
> Cryptographic suite designers MUST use mandatory proof value properties defined in Section 2.1 Proofs, and MAY define other properties specific to their cryptographic suite.

R-0053 (MUST) → split: R-0165 (MUST), R-0166 (MAY)

## §4 Algorithms

<!-- q L531 "The algorithms" .. "a map." -->
> The algorithms defined below operate on documents represented as JSON objects. This specification follows the JSON-LD 1.1 Processing Algorithms and API specification in representing a JSON object as a map.

R-0289 (none)

<!-- q L531 "An unsecured" .. "proof values." -->
> An unsecured data document is a map that contains no proof values.

R-0167 (none)

<!-- q L531 "An input" .. "previous process." -->
> An input document is an map that has not yet had the current proof added to it, but it MAY contain a proof value that was added to it by a previous process.

R-0055 (MAY)

<!-- q L531 "A secured" .. "proof values." -->
> A secured data document is a map that contains one or more proof values.

R-0168 (none)

<!-- q L532 "Implementers MAY" .. "other improvements." -->
> Implementers MAY implement reasonable defaults and safeguards in addition to the algorithms below, to help mitigate developer error, excessive resource consumption, newly discovered attack models against which there is a particular protection, and other improvements.

R-0056 (MAY)

<!-- q L532 "The algorithms" .. "interoperable implementation" -->
> The algorithms provided below are the minimum requirements for an interoperable implementation

R-0169 (none)

## §4.1 Processing Model

<!-- q L536-537 "When software" .. "JSON-LD document." -->
> When software is to ensure information is tamper-evident, it performs the following steps: The software arranges the information into a document, such as a JSON or JSON-LD document.

R-0170 (none)

<!-- q L538 -->
> If the document is a JSON-LD document, the software selects one or more JSON-LD Contexts and expresses them using the @context property.

R-0171 (none)

<!-- q L539 -->
> The software selects one or more cryptography suites that meet the needs of the use case, such as one that provides full, selective, or unlinkable disclosure, using acceptable cryptographic key material.

R-0172 (none)

<!-- q L540 -->
> The software uses the applicable algorithm(s) provided in Section 4.2 Add Proof or Section 4.3 Add Proof Set/Chain to add one or more proofs.

R-0173 (none)

<!-- q L541-542 -->
> When software needs to use information that was transmitted to it using a mechanism described by this specification, it performs the following steps: The software transforms the incoming data into a document that can be understood by the applicable algorithm provided in Section 4.4 Verify Proof or Section 4.5 Verify Proof Sets and Chains.

R-0174 (none)

<!-- q L543 -->
> The software uses JSON Schema or an equivalent mechanism to validate that the incoming document follows an expected schema used by the application.

R-0175 (none)

<!-- q L544 -->
> The software uses the applicable algorithm(s) provided in Section 4.4 Verify Proof or Section 4.5 Verify Proof Sets and Chains to verify the integrity of the incoming document.

R-0176 (none)

<!-- q L545 -->
> If the document is a JSON-LD document, the software uses the algorithm provided in Section 4.6 Context Validation, or one providing equivalent protections, to validate all JSON-LD Context values used in the document.

R-0177 (none)

## §4.2 Add Proof

<!-- q L549 "Required inputs" .. "an error." -->
> Required inputs are an input document (map inputDocument), a cryptosuite instance (struct cryptosuite), and a set of options (map options). Output is a secured data document (map) or an error.

R-0178 (none)

<!-- q L549 "Whenever this" .. "UTF-8 encoding." -->
> Whenever this algorithm encodes strings, it MUST use UTF-8 encoding.

R-0057 (MUST)

<!-- q L550 "Let proof" .. "a parameters." -->
> Let proof be the result of calling the createProof algorithm specified in cryptosuite.createProof with inputDocument and options passed as a parameters.

R-0179 (none)

<!-- q L550 "If the" .. "error type." -->
> If the algorithm produces an error, the error MUST be propagated and SHOULD convey the error type.

R-0058 (MUST) → split: R-0180 (MUST), R-0181 (SHOULD)

<!-- q L551 -->
> If one or more of the proof.type, proof.verificationMethod, and proof.proofPurpose values is not set, an error MUST be raised and SHOULD convey an error type of PROOF_GENERATION_ERROR.

R-0059 (MUST) → split: R-0182 (MUST), R-0183 (SHOULD)

<!-- q L552 -->
> If options has a non-null domain item, it MUST be equal to proof.domain or an error MUST be raised and SHOULD convey an error type of PROOF_GENERATION_ERROR.

R-0060 (MUST) → split: R-0184 (MUST), R-0185 (SHOULD)

<!-- q L553 -->
> If options has a non-null challenge item, it MUST be equal to proof.challenge or an error MUST be raised and SHOULD convey an error type of PROOF_GENERATION_ERROR.

R-0061 (MUST) → split: R-0186 (MUST), R-0187 (SHOULD)

Inferred, not verbatim: R-0188 (domain and challenge of a created proof). See requirements.yaml.

<!-- q L554 -->
> Let securedDataDocument be a copy of inputDocument.

R-0189 (none)

<!-- q L555 -->
> Set securedDataDocument.proof to the value of proof.

R-0190 (none)

Inferred, not verbatim: R-0191 (adding a proof to a secured document). See requirements.yaml.

<!-- q L556 -->
> Return securedDataDocument as the secured data document.

R-0192 (none)

## §4.3 Add Proof Set/Chain

<!-- q L560 "Required inputs" .. "document (map)." -->
> Required inputs are a secured data document (map securedDocument), a cryptographic suite (cryptosuite instance suite), and a set of options (map options). Output is a new secured data document (map).

R-0193 (none)

<!-- q L560 "Whenever this" .. "UTF-8 encoding." -->
> Whenever this algorithm encodes strings, it MUST use UTF-8 encoding.

R-0062 (MUST)

<!-- q L561 -->
> Let proof be set to securedDocument.proof. Let allProofs be an empty list. If proof is a list, copy all the elements of proof to allProofs. If proof is an object add a copy of that object to allProofs.

R-0194 (none)

<!-- q L562 -->
> Let the inputDocument be a copy of the securedDocument with the proof attribute removed. Let output be a copy of the inputDocument.

R-0195 (none)

<!-- q L563 -->
> Let matchingProofs be an empty list.

R-0196 (none)

<!-- q L564 "If options" .. "to matchingProofs." -->
> If options has a previousProof item that is a string, add the element from allProofs with an id attribute matching previousProof to matchingProofs.

R-0197 (none)

Inferred, not verbatim: R-0198 (proof identifiers within one document). See requirements.yaml.

<!-- q L564 "If a" .. "of PROOF_GENERATION_ERROR." -->
> If a proof with id equal to previousProof does not exist in allProofs, an error MUST be raised and SHOULD convey an error type of PROOF_GENERATION_ERROR.

R-0063 (MUST) → split: R-0199 (MUST), R-0200 (SHOULD)

<!-- q L565 "If options" .. "that array." -->
> If options has a previousProof item that is an array, add each element from allProofs with an id attribute that matches an element of that array.

R-0201 (none)

<!-- q L565 "If any" .. "of PROOF_GENERATION_ERROR." -->
> If any element of previousProof list has an id attribute that does not match the id attribute of any element of allProofs, an error MUST be raised and SHOULD convey an error type of PROOF_GENERATION_ERROR.

R-0064 (MUST) → split: R-0202 (MUST), R-0203 (SHOULD)

<!-- q L566 -->
> Set inputDocument.proof to matchingProofs.

R-0204 (none)

Inferred, not verbatim: R-0290 (what a member of a proof set covers). See requirements.yaml.

<!-- q L569 -->
> Run steps 1 through 6 of the algorithm in section 4.2 Add Proof, passing inputDocument, suite, and options. If no exceptions are raised, append the generated proof value to the allProofs; otherwise, raise the exception.

R-0205 (none)

Inferred, not verbatim: R-0206 (previousProof of a proof added to a chain). See requirements.yaml.

<!-- q L570 -->
> Set output.proof to the value of allProofs.

R-0207 (none)

<!-- q L571 -->
> Return output as the new secured data document.

R-0208 (none)

## §4.4 Verify Proof

<!-- q L576-577 -->
> mediaType A media type as defined in [MIMESNIFF]

R-0209 (none)

<!-- q L578-579 -->
> documentBytes A byte sequence whose media type is mediaType

R-0210 (none)

<!-- q L580-581 -->
> cryptosuite A cryptosuite instance

R-0211 (none)

<!-- q L582-583 "expectedProofPurpose An" .. "the verifier." -->
> expectedProofPurpose An optional string, used to ensure that the proof was generated by the proof creator for the expected reason by the verifier.

R-0212 (none)

<!-- q L583-599 "See 2.2" .. "errors list." -->
> See 2.2 Proof Purposes for common values domain An optional set of strings, used by the proof creator to lock a proof to a particular security domain, and used by the verifier to ensure that a proof is not being used across different security domains challenge An optional string challenge, used by the verifier to ensure that an attacker is not replaying previously created proofs This algorithm returns a verification result, a struct whose items are: verified true or false verifiedDocument Null, if verified is false; otherwise, an input document mediaType Null, if verified is false; otherwise, a media type, which MAY include parameters warnings a list of ProblemDetails, which defaults to an empty list errors a list of ProblemDetails, which defaults to an empty list When a step says "an error MUST be raised", it means that a verification result MUST be returned with a verified value of false and a non-empty errors list.

R-0065 (MUST) → split: R-0213 (none), R-0214 (none), R-0215 (none), R-0216 (MAY), R-0217 (none), R-0218 (MUST)

<!-- q L600 -->
> Let securedDocument be the result of running parse JSON bytes to an Infra value on documentBytes.

R-0219 (none)

<!-- q L601 -->
> If either securedDocument is not a map or securedDocument.proof is not a map, an error MUST be raised and SHOULD convey an error type of PARSING_ERROR.

R-0066 (MUST) → split: R-0220 (MUST), R-0221 (SHOULD)

Inferred, not verbatim: R-0222 (dispatch between §4.4 and §4.5). See requirements.yaml.

<!-- q L602 -->
> Let proof be securedDocument.proof.

R-0223 (none)

<!-- q L603 -->
> If one or more of proof.type, proof.verificationMethod, and proof.proofPurpose does not exist, an error MUST be raised and SHOULD convey an error type of PROOF_VERIFICATION_ERROR.

R-0067 (MUST) → split: R-0224 (MUST), R-0225 (SHOULD)

<!-- q L604 -->
> If expectedProofPurpose was given, and it does not match proof.proofPurpose, an error MUST be raised and SHOULD convey an error type of PROOF_VERIFICATION_ERROR.

R-0068 (MUST) → split: R-0226 (MUST), R-0227 (SHOULD)

Inferred, not verbatim: R-0228 (expectedProofPurpose input). See requirements.yaml.

<!-- q L605 -->
> If domain was given, and it does not contain the same strings as proof.domain (treating a single string as a set containing just that string), an error MUST be raised and SHOULD convey an error type of INVALID_DOMAIN_ERROR.

R-0069 (MUST) → split: R-0229 (MUST), R-0230 (SHOULD)

<!-- q L606 -->
> If challenge was given, and it does not match proof.challenge, an error MUST be raised and SHOULD convey an error type of INVALID_CHALLENGE_ERROR.

R-0070 (MUST) → split: R-0231 (MUST), R-0232 (SHOULD)

Inferred, not verbatim: R-0233 (replay protection through challenge). See requirements.yaml.

<!-- q L607 -->
> Let cryptosuiteVerificationResult be the result of running the cryptosuite.verifyProof algorithm with securedDocument provided as input.

R-0234 (none)

Inferred, not verbatim: R-0235 (selection of the cryptosuite instance). See requirements.yaml.

<!-- q L608-614 -->
> Return a verification result with items: verified cryptosuiteVerificationResult.verified verifiedDocument cryptosuiteVerificationResult.verifiedDocument mediaType mediaType

R-0236 (none)

## §4.5 Verify Proof Sets and Chains

<!-- q L618 "In a" .. "proofs (allProofs)." -->
> In a proof set or proof chain, a secured data document has a proof attribute which contains a list of proofs (allProofs).

R-0237 (none)

<!-- q L618 "The following" .. "in allProofs." -->
> The following algorithm provides one method of checking the authenticity and integrity of a secured data document, achieved by verifying every proof in allProofs.

R-0238 (none)

<!-- q L618 "Other approaches" .. "in allProofs." -->
> Other approaches are possible, particularly if it is only desired to verify a subset of the proofs contained in allProofs.

R-0239 (none)

<!-- q L618 "If another" .. "considered verified." -->
> If another approach is taken to verify only a subset of the proofs, then it is important to note that any proof in that subset with a previousProof can only be considered verified if the proofs it references are also considered verified.

R-0240 (none)

<!-- q L619 "Required input" .. "as output." -->
> Required input is a secured data document (securedDocument). A list of verification results corresponding to each proof in allProofs is generated, and a single combined verification result is returned as output.

R-0241 (none)

<!-- q L619 "Implementations MAY" .. "verification result." -->
> Implementations MAY return any of the other verification results and/or any other metadata alongside the combined verification result.

R-0071 (MAY)

<!-- q L620 -->
> Set allProofs to securedDocument.proof.

R-0242 (none)

<!-- q L621 -->
> Set verificationResults to an empty list.

R-0243 (none)

<!-- q L622 -->
> For each proof in allProofs, do the following steps:

R-0244 (none)

<!-- q L623 -->
> Let matchingProofs be an empty list.

R-0245 (none)

<!-- q L624 "If proof" .. "to matchingProofs." -->
> If proof contains a previousProof attribute and the value of that attribute is a string, add the element from allProofs with an id attribute value matching the value of previousProof to matchingProofs.

R-0246 (none)

<!-- q L624 "If a" .. "of PROOF_VERIFICATION_ERROR." -->
> If a proof with id value equal to the value of previousProof does not exist in allProofs, an error MUST be raised and SHOULD convey an error type of PROOF_VERIFICATION_ERROR.

R-0072 (MUST) → split: R-0247 (MUST), R-0248 (SHOULD)

<!-- q L624 "If the" .. "that list." -->
> If the previousProof attribute is a list, add each element from allProofs with an id attribute value that matches the value of an element of that list.

R-0249 (none)

<!-- q L624 "If any" .. "of PROOF_VERIFICATION_ERROR." -->
> If any element of previousProof list has an id attribute value that does not match the id attribute value of any element of allProofs, an error MUST be raised and SHOULD convey an error type of PROOF_VERIFICATION_ERROR.

R-0073 (MUST) → split: R-0250 (MUST), R-0251 (SHOULD)

<!-- q L625 -->
> Let inputDocument be a copy of securedDocument with the proof value removed and then set inputDocument.proof to matchingProofs.

R-0252 (none)

<!-- q L628 -->
> Run steps 4 through 8 of the algorithm in section 4.4 Verify Proof on inputDocument; if no exceptions are raised, append cryptosuiteVerificationResult to verificationResults.

R-0253 (none)

Inferred, not verbatim: R-0254 (bindings for the per-proof run of §4.4 steps 4 to 8). See requirements.yaml.

<!-- q L629 -->
> Set successfulVerificationResults to an empty list.

R-0255 (none)

<!-- q L630 -->
> Let combinedVerificationResult be an empty struct. Set combinedVerificationResult.status to true, combinedVerificationResult.document to null, and combinedVerificationResult.mediaType to null.

R-0256 (none)

<!-- q L631 -->
> For each cryptosuiteVerificationResult in verificationResults:

R-0257 (none)

<!-- q L632 -->
> If cryptosuiteVerificationResult.verified is false, set combinedVerificationResult.verified to false.

R-0258 (none)

<!-- q L633 -->
> Otherwise, set combinedVerificationResult.document to cryptosuiteVerificationResult.verifiedDocument, set combinedVerificationResult.mediaType to cryptosuiteVerificationResult.mediaType, and append cryptosuiteVerificationResult to successfulVerificationResults.

R-0259 (none)

<!-- q L634 -->
> If combinedVerificationResult.status is false, set combinedVerificationResult.document to null and combinedVerificationResult.mediaType to null.

R-0260 (none)

<!-- q L635 -->
> Return combinedVerificationResult, successfulVerificationResults.

R-0261 (none)

Inferred, not verbatim: R-0262 (combined verification result). See requirements.yaml.

## §4.6 Context Validation

<!-- q L639 "The following" .. "the document." -->
> The following algorithm provides one mechanism that can be used to ensure that an application understands the contexts associated with a document before it executed business rules specific to the input in the document.

R-0263 (none)

<!-- q L639 "This algorithm" .. "(boolean recompact)." -->
> This algorithm takes inputs of a document (map inputDocument), a set of known JSON-LD Contexts (list knownContext), and a boolean to recompact when unknown contexts are detected (boolean recompact).

R-0264 (none)

<!-- q L640-648 -->
> This algorithm returns a context validation result, a struct whose items are: validated true or false validatedDocument Null, if validated is false; otherwise, an input document warnings a list of ProblemDetails, which defaults to an empty list errors a list of ProblemDetails, which defaults to an empty list

R-0265 (none)

<!-- q L650 -->
> Set result.validated to false, result.warnings to an empty list, result.errors to an empty list, compactionContext to an empty list; and clone inputDocument to result.validatedDocument.

R-0266 (none)

<!-- q L651 -->
> Let contextValue be the value of the @context property of result.validatedDocument, which might be undefined.

R-0267 (none)

<!-- q L652 -->
> If contextValue does not deeply equal knownContext, any subtree in result.validatedDocument contains an @context property, or any URI in contextValue dereferences to a JSON-LD Context file that does not match a known good value or cryptographic hash, then perform the applicable action:

R-0268 (none)

<!-- q L653 -->
> If recompact is true, set result.validatedDocument to the result of running the JSON-LD Compaction Algorithm with the inputDocument and knownContext as inputs. If the compaction fails, add at least one error to result.errors.

R-0269 (none)

<!-- q L654 -->
> If recompact is not true, add at least one error to result.errors.

R-0270 (none)

<!-- q L655 -->
> If result.errors is empty, set result.validated to true; otherwise, set result.validated to false, and remove the document property from result.

R-0271 (none)

<!-- q L656 -->
> Return the value of result.

R-0272 (none)

<!-- q L657 -->
> Implementations MAY include additional warnings or errors that enforce further validation rules that are specific to the implementation or a particular use case.

R-0074 (MAY)

## §4.7 Processing Errors

<!-- q L662 "When exposing" .. "ProblemDetails map." -->
> When exposing these errors through an HTTP interface, implementers SHOULD use [RFC9457] to encode the error data structure as a ProblemDetails map.

R-0075 (SHOULD)

<!-- q L662-663 "If [RFC9457]" .. "listed below." -->
> If [RFC9457] is used: The type value of the error object MUST be a URL that starts with the value https://w3id.org/security# and ends with the value in the section listed below.

R-0076 (MUST) → split: R-0273 (MUST)

<!-- q L664 -->
> The title value SHOULD provide a short but specific human-readable string for the error.

R-0077 (SHOULD)

<!-- q L665 -->
> The detail value SHOULD provide a longer human-readable string for the error.

R-0078 (SHOULD)

<!-- q L666-667 -->
> PROOF_GENERATION_ERROR A request to generate a proof failed. See Section 4.2 Add Proof, and Section 4.3 Add Proof Set/Chain.

R-0274 (none)

<!-- q L668-669 -->
> PROOF_VERIFICATION_ERROR An error was encountered during proof verification. See Section 4.4 Verify Proof.

R-0275 (none)

<!-- q L670-671 -->
> PROOF_TRANSFORMATION_ERROR An error was encountered during the transformation process.

R-0276 (none)

<!-- q L672-673 -->
> INVALID_DOMAIN_ERROR The domain value in a proof did not match the expected value. See Section 4.4 Verify Proof.

R-0277 (none)

<!-- q L674-675 -->
> INVALID_CHALLENGE_ERROR The challenge value in a proof did not match the expected value. See Section 4.4 Verify Proof.

R-0278 (none)

## §5.6 Transformations

<!-- q L727 "This class" .. "halt processing." -->
> This class of attack is called dataset poisoning, and all modern RDF Dataset canonicalizers are required to detect these sorts of bad inputs and halt processing.

R-0279 (none)

<!-- q L727 "Generally speaking," .. "of attacks" -->
> Generally speaking, cryptographic suite specifications that use transformations are required to mitigate these sorts of attacks

R-0280 (none)

## §5.7 Protected Information

<!-- q L731 "The data" .. "particular cryptosuite." -->
> The data that is protected by any data integrity proof is the transformed data. Transformed data is generated by a transformation algorithm that is specified by a particular cryptosuite.

R-0281 (none)

## §5.8 Data Opacity

<!-- q L742 "While a" .. "bad requests." -->
> While a digital signature needs to always be checked before taking substantive action, other upstream checks can be performed on transparent payloads — such as identifier-based rate limiting, signature expiration checking, or nonce/challenge checking — to reject obviously bad requests.

R-0282 (none)

## §5.9 Verification Method Binding

<!-- q L749 "Implementers ensure" .. "verification method." -->
> Implementers ensure that a verification method is bound to a particular controller by going from the definition of the verification method to the controlled identifier document, and then ensuring that the controlled identifier document also contains a reference to the verification method.

R-0283 (none)

## §5.10 Verification Relationship Validation

<!-- q L753 "When an" .. "being verified." -->
> When an implementation is verifying a proof, it is imperative that it verify not only that the verification method used to generate the proof is listed in the controlled identifier document, but also that it was intended to be used to generate the proof that is being verified.

R-0284 (none)

<!-- q L754 -->
> The process of validating a verification relationship is outlined in Section 3.3 Retrieve Verification Method of the Controlled Identifiers v1.0 specification.

R-0285 (none)

## §5.11 Proof Purpose Validation

<!-- q L759 -->
> When an implementation is verifying a proof, it is imperative that it verify that the proof purpose match the intended use.

R-0286 (none)

## §6.3 Previous Proofs

<!-- q L806 "When using" .. "secured payload." -->
> When using the previousProof feature defined in 2.1.2 Proof Chains, implementations are required to digitally sign over one or more previous proofs, so as to include them in the secured payload.

R-0287 (none)

## Source defects

Defects and tensions in the source, recorded rather than healed. Each names the entries it bears on. protocol.yaml `source_defects` (D-01 to D-21) records the algorithms' defects from the flows' side, with its own numbering; SD-30 to SD-33 were found there and added here by the verify pass. Quotations are
markers like everything else in this file. SD-E collects the editorial ones, quoted where they sit.

### SD-1: §1.3 and §1.4 sit inside a section marked non-normative

The §1 section element is informative and §1 opens with the non-normative marker; §1.1 and §1.2 repeat it, §1.3 (Conformance) and §1.4 (Terminology) do not. §1.3 holds the conformance classes and R-0001's MUST; both are read as normative, as §1.3 ¶1 itself requires of anything not marked (R-0079, R-0080, R-0081, R-0001).

<!-- q L124 -->
> This section is non-normative.

<!-- q L165 -->
> As well as sections marked as non-normative, all authoring guidelines, diagrams, examples, and notes in this specification are non-normative. Everything else in this specification is normative.

### SD-2: a BCP 14 keyword inside a Note

The SHOULD of the modern-pattern sentence of §3.1 sits inside the Note on legacy cryptographic suite design patterns (HTML div class note; the sentence shares the note's p element, after a line break). §1.3 ¶1 makes notes non-normative, so the keyword binds nothing; the skeleton's R-0054 is kept, withdrawn (pass 1 had deleted it; docs/requirements.md §3b says ids are stable, so pass 3 restored it), and the keyword is counted in the reconciliation. Whether a new suite uses the DataIntegrityProof pattern at all is therefore left free; §3.1's MUSTs bind only suites that use it (R-0051, R-0052, R-0053).

<!-- q L525 -->
> Note: Design Patterns of Legacy Cryptographic Suites

### SD-3: verificationMethod: optional in the data model, required by both algorithms

§2.1 makes verificationMethod OPTIONAL (R-0007); §4.2 step 2 (R-0182) and §4.4 step 4 (R-0224) raise an error when it is absent. A proof that uses the permission can be neither added nor verified by §4. Inferred: R-0090.

### SD-4: offset-less time values: consumers may accept what documents must not carry

created and expires MUST be XSD dateTimeStamp strings, which carry a time zone (R-0098, R-0012); a conforming processor MAY consume values without an offset (R-0010, R-0013) and reads them as UTC (R-0099, R-0101). Such a document is non-conforming, and R-0001 says conforming processors MUST produce errors when non-conforming documents are consumed. The MAY reads as a scoped exception to R-0001; the source never says so.

### SD-5: "mandatory proof value properties" are never defined

R-0053's MUST child (R-0165) points at mandatory properties defined in §2.1, and §2.1 marks none mandatory: type and proofPurpose MUST be specified, cryptosuite only for DataIntegrityProof, verificationMethod is OPTIONAL, and the presence of proofValue is never stated. §2.1 also lets a cryptosuite use other properties instead of proofValue (R-0108), while §3.1 says proofValue MUST be used (R-0164).

<!-- q L524 "mandatory proof" .. "value properties" -->
> mandatory proof value properties

### SD-6: two error types used but not defined

§4.4 step 2 names PARSING_ERROR (R-0221) and §2.4.3 names DATA_LOSS_DETECTION_ERROR (R-0142); §4.7 defines five errors (R-0274 to R-0278) and neither of these. An implementation using RFC 9457 has no listed value for its type URL to end with (R-0273).

### SD-7: §4.5 initialises status and sets verified

Step 5 sets combinedVerificationResult.status to true (R-0256), step 6.1 sets combinedVerificationResult.verified to false for a failed proof (R-0258), and step 7 tests status (R-0260). As written, status never becomes false, step 7 never fires, and the returned struct can say status true beside verified false. Inferred: R-0262.

### SD-8: §4.5 skips a proof for which an error is raised

Step 3.4 appends a result only if no exceptions are raised (R-0253); nothing marks the combined result failed when one is, including the previousProof errors of step 3.2 (R-0247, R-0250). §4.4 ¶3 defines raising an error as returning a verification result with verified false and a non-empty errors list (R-0218), not as an exception, so the two algorithms disagree about what an error is. Inferred: R-0262.

### SD-9: §4.5 runs §4.4 steps 4 to 8 without their inputs

§4.5 takes only a secured data document (R-0241). §4.4 steps 5 to 7 use expectedProofPurpose, domain and challenge, and step 8 uses a cryptosuite instance and passes securedDocument to cryptosuite.verifyProof (R-0234); under §4.5 none of these is bound, so steps 5 to 7 never fire. The document passed is the step 3.3 inputDocument, whose proof is the matching previous proofs, not the proof under verification (R-0252), and verifyProof takes no separate proof argument (R-0156). Inferred: R-0254.

### SD-10: §4.5 reads a mediaType the cryptosuite result does not have

The cryptosuite verification result of §3 has two items, verified and verifiedDocument (R-0157, R-0158, plus what R-0045 permits); step 6.2 reads cryptosuiteVerificationResult.mediaType (R-0259). The combined struct also names its items status, document and mediaType where the §4.4 verification result has verified, verifiedDocument and mediaType (R-0215).

### SD-11: §4.5 returns two values

¶2 says a single combined verification result is returned (R-0241) and R-0071 makes other results optional; step 8 returns combinedVerificationResult and successfulVerificationResults (R-0261).

### SD-12: previousProof elements treated as objects

previousProof is a string or a list of strings (R-0110); §4.3 step 5 (R-0202) and §4.5 step 3.2 (R-0250) speak of an element of the list having an id attribute. Read as: the element is not the id of any proof in allProofs.

<!-- q L565 "any element" .. "id attribute" -->
> any element of previousProof list has an id attribute

### SD-13: §4.4: a cryptosuite error, and warnings and errors, left unhandled

cryptosuite.verifyProof produces a result or an error (R-0156); an error means verification failed to complete (R-0159). Step 8 does not say what follows an error (R-0234); §4.2 step 1 says propagate (R-0180). Step 9 returns verified, verifiedDocument and mediaType only (R-0236), so warnings and errors keep their empty defaults (R-0217) whatever the cryptosuite found.

### SD-14: Verify Proof omits checks the document calls important

No §4.4 step checks created or expires, though §2.6 says it is important to ensure the time of interest is within the proof's validity period (R-0151); none compares the cryptosuite input with proof.type or proof.cryptosuite (R-0211); verification relationship validation (R-0284) is left to [CID]. Inferred: R-0152, R-0235.

### SD-15: proof purpose: optional input, imperative check

expectedProofPurpose is an optional input (R-0212) and step 5 checks only if it was given (R-0226); §5.11 says it is imperative to verify that the proof purpose matches the intended use (R-0286). Inferred: R-0228.

### SD-16: domain: equality in the algorithm, membership in the data model

§2.1 says the domain value conveys the security domains in which the proof is meant to be used and that a verifier SHOULD check it against the domain it operates in (R-0016, R-0103); §4.4 step 6 raises an error unless the domain input contains the same strings as proof.domain (R-0229). For a proof listing two domains and a verifier operating in one, the readings disagree.

### SD-17: proof chains: what is signed depends on the cryptosuite

§4.3 step 6 sets inputDocument.proof to the matching proofs (R-0204) so that step 7's new proof covers them; whether it does depends on cryptosuite.createProof including inputDocument.proof in what it signs, which the §3 interface does not require (R-0155), while §6.3 says implementations are required to sign over previous proofs (R-0287). No step sets the new proof's previousProof (R-0205; inferred R-0206). With no previousProof option the literal step 6 sets proof to an empty list, which differs from an absent proof under a transformation that keeps the proof property. A member added without previousProof covers none of the proofs beside it (R-0290).

### SD-18: §4.3 output omits the error case

§4.2 says its output is a secured data document or an error (R-0178); §4.3 says a new secured data document only (R-0193), though steps 4, 5 and 7 raise errors (R-0199, R-0202, R-0205).

### SD-19: §4.6 step 4 removes a property the result does not have

The context validation result has validated, validatedDocument, warnings and errors, validatedDocument being Null when validated is false (R-0265); step 4 removes the document property from result (R-0271).

### SD-20: knownContext: a set by name, an exact value by use

The input is a set of known JSON-LD contexts held as a list (R-0264); step 3 compares the document's whole @context value with it by deep equality (R-0268). So knownContext is the one expected @context value, in order, not a set of acceptable contexts.

### SD-21: the vocabulary URL and its hash are named after the rule that uses them

R-0025 refers to the vocabulary URL and the corresponding hash value below; the URL is named only at line 419 (R-0131), after a Note, and the table below has three digests, one per media type; the application/ld+json row is the one meant (R-0132).

### SD-22: a verification method property named two ways

§2.6 ¶4 names the revocation and expiration properties of a verification method revocation and expires (C-0071, rejected as descriptive); Appendix B (non-normative) records that revoked and expires were added to verification methods. The property is defined in [CID]; this document disagrees with itself about its name.

<!-- q L486 "are expressed" .. "expires properties" -->
> are expressed using the revocation and expires properties

<!-- q L972 -->
> Added revoked and expires to verification methods.

### SD-23: an input document may carry a proof that Add Proof then replaces

An input document MAY contain a proof added by a previous process (R-0055); §4.2 step 6 sets securedDataDocument.proof to the new proof (R-0190), replacing it. Inferred: R-0191.

### SD-24: proof value means two things

The phrase proof value names the proof object in §3.1 ¶2 and ¶3, §4 ¶1, §4.3 step 7 and §4.5 step 3.3, and the proofValue property elsewhere. Each use is quoted below; the entries carry a note where it matters.

<!-- q L517 "the proof" .. "following form" -->
> the proof value takes the following form

<!-- q L524 "mandatory proof" .. "value properties" -->
> mandatory proof value properties

<!-- q L531 "contains no" .. "proof values" -->
> contains no proof values

<!-- q L569 "append the" .. "proof value" -->
> append the generated proof value

<!-- q L625 "with the" .. "value removed" -->
> with the proof value removed

### SD-25: the poison-graph requirement has no keyword

Appendix B (non-normative) reports that cryptosuite specifications doing RDF canonicalization were required to abort on poison graphs. The text that carries it is §5.6, in Security Considerations and in lowercase (R-0279, R-0280); the nearest keyword is R-0046 (detail known resource starvation attacks and testable mitigations).

<!-- q L968 -->
> Required cryptosuite specifications that do RDF canonicalization to abort when poison graphs are detected.

### SD-26: cryptosuite identifiers have no closed list

The lexical and value spaces of cryptosuiteString are the union over all Data Integrity cryptosuite specifications (R-0147, R-0148); no registry is normative (the VC Extensions document is an informative Editor's Draft, R-0044, R-0050). A validator cannot decide whether a cryptosuite value identifies a suite (R-0162).

### SD-27: digestMultibase: no verification procedure

§2.3 lets a document carry digestMultibase (R-0022, R-0023) to enable confirmation that a resource has not changed, and never says who confirms it, over which bytes, or what follows a mismatch. Inferred: R-0122.

### SD-28: proof ids are not required to be distinct

§4.3 step 4 and §4.5 step 3.2 take the element of allProofs whose id matches (R-0197, R-0246); nothing requires distinct ids. Inferred: R-0198.

### SD-29: context validation order: MUST after, MAY reorder

Context validation MUST run after Verify Proof or Verify Proof Sets and Chains (R-0030); R-0031 lets implementers use alternative approaches or a different ordering of the steps that provide the same protections. Whether that ordering reaches R-0030's is unsettled; §4.6 ¶1 adds that validation precedes business rules (R-0263).

### SD-30: §4.4 step 9 returns the input mediaType even when verified is false

The verification result's mediaType is null when verified is false (R-0216); step 9 sets it to the mediaType input unconditionally (R-0236). Found by the protocol lane (protocol.yaml D-06); added here by the verify pass.

<!-- q L594 -->
> Null, if verified is false; otherwise, a media type, which MAY include parameters

<!-- q L613-614 -->
> mediaType mediaType

### SD-31: §4.6 step 1 initialises a variable no step uses

compactionContext is set and never read; step 3.1 compacts with knownContext (R-0269). protocol.yaml D-08; added by the verify pass.

<!-- q L650 "compactionContext" .. "an empty list" -->
> compactionContext to an empty list

### SD-32: §4.4 step 1 has no failure path, and PARSING_ERROR links outside the document

Step 1 parses JSON bytes (R-0219) and no step says what follows bytes that are not JSON; step 2 tests only the parsed value (R-0220). The PARSING_ERROR that step 2 conveys (R-0221) is linked in the HTML to https://www.w3.org/TR/VC-DATA-MODEL-2.0#PARSING_ERROR, the VC Data Model's list, not to §4.7 (SD-6). protocol.yaml D-18 and D-09; added by the verify pass.

### SD-33: §4.5 over an empty proof list reports status true

With no proof in allProofs the loop of step 6 never runs, so the combined result keeps the status true and the null document of step 5 (R-0256, R-0257): the case SD-7 leaves out. Inferred R-0262 reads the combined result as false only when a proof fails, so it does not cover this either. protocol.yaml D-21; added by the verify pass.

### SD-E: editorial defects, quoted where they sit (never healed)

Each is the source's own text; the entries that quote them say so in their notes.

Line 195:

<!-- q L195 "is the" .. "Security Vocabulary" -->
> is the The Security Vocabulary

Line 215:

<!-- q L215 "MAY chose" .. "to consume" -->
> MAY chose to consume

Line 217:

<!-- q L217 "MAY chose" .. "to consume" -->
> MAY chose to consume

Line 367:

<!-- q L367 "as without" .. "not possible" -->
> as without these, is not possible

Line 379:

<!-- q L379 "used for" .. "key agreement" -->
> used for for key agreement

Line 388:

<!-- q L388 "or an" .. "string values" -->
> or an list of string values

Line 440:

<!-- q L440 "(e.g., `https://ontology.example/v1)" .. "(e.g., `https://ontology.example/v1)" -->
> (e.g., `https://ontology.example/v1)

Line 485:

<!-- q L485 "betweeen validFrom" .. "betweeen validFrom" -->
> betweeen validFrom

Line 495:

<!-- q L495 "the hashing" .. "algorithms parameters," -->
> the hashing algorithms parameters,

Line 517:

<!-- q L517 "When specifing" .. "When specifing" -->
> When specifing

Line 531:

<!-- q L531 "is an" .. "an map" -->
> is an map

Line 550:

<!-- q L550 "passed as" .. "a parameters." -->
> passed as a parameters.

Line 639:

<!-- q L639 "before it" .. "business rules" -->
> before it executed business rules

Line 686:

<!-- q L686 "its not" .. "not clear" -->
> its not clear

Line 713:

<!-- q L713 "the failure" .. "or more" -->
> the failure or one or more

Line 833:

<!-- q L833 "cultural normas" .. "cultural normas" -->
> cultural normas


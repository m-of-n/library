---
record: w3c-vc-data-model-2-0
kind: normative
title: "w3c-vc-data-model-2-0 — normative text"
generated_by: bin/fx1-skeleton
extracted: "2026-11-07"
reviewed_by: ""
---

# Normative text

Every normative statement of the W3C Recommendation *Verifiable Credentials Data Model v2.0* (15 May 2025, REC-vc-data-model-2.0-20250515) that binds anyone, in source order, with its locator: each BCP 14 sentence the skeleton found (split into one statement per entry where it held several), the keyword-less statements pass 1 judged binding, the definitions they rest on, and the eight keyword sentences of §11.1 and §11.2, flagged withdrawn because their section is marked non-normative. Explanatory prose, examples, notes and the sections the source marks non-normative are left out, except where a defect needs them quoted.

**Markers.** Every quotation is a `<!-- q Lx-y -->` marker, optionally anchored, whose words `bin/check-quotes --render` wrote from `.cache/w3c-vc-data-model-2-0.txt` (5009 lines, sha256 73d91cc0b6a7d582512eb06d45a5fcfa8c696ab094b3db44f7a1495e9d3da548), the lead's `render_w3c.py` rendering of the HTML whose sha256 is content.sha256 (a9196a3d0b6601356c4e127bad24f8c7f2c17f6ed22e41b35755a910104156f8). The rendering puts one HTML block element on a line and collapses whitespace; a table row's cells are separated by a vertical bar; a definition term and its definition are two lines, so a quotation spanning both reads term, then definition. Nothing between the blockquote marks was typed.

**Flags.** The keyword, or keyword-less; split of R-NNNN for a statement cut from a skeleton sentence; from C-NNNN for a candidate promoted; hunted for a keyword-less statement no candidate carried; WITHDRAWN for a keyword sentence in a section marked non-normative; _[definition]_, _[scope]_ and _[recital]_ for normative text that is not itself a requirement. Locators are requirements.yaml's: ¶n counts the section's own blocks from its heading, an example or a note counting one (see its note).

**Source defects and tensions** are at the end as SD-1 onward, each with the words it concerns quoted by marker; requirements.yaml's notes cite them.

## §1.3 Conformance

_Inferred, not verbatim: **R-0131** (§1.3 ¶4); its words are this extraction's and its grounds are quoted in requirements.yaml._

_[scope]_ · §1.3 ¶1 · the rule that makes sections marked non-normative, examples and notes non-normative; every rejection and withdrawal for that reason cites it
<!-- q L226-226 -->
> As well as sections marked as non-normative, all authoring guidelines, diagrams, examples, and notes in this specification are non-normative. Everything else in this specification is normative.

_[recital]_ · §1.3 ¶2 · the BCP 14 recital; bin/bcp14-count strips its eight keywords
<!-- q L227-227 -->
> The key words MAY, MUST, MUST NOT, OPTIONAL, RECOMMENDED, REQUIRED, SHOULD, and SHOULD NOT in this document are to be interpreted as described in BCP 14 [RFC2119] [RFC8174] when, and only when, they appear in all capitals, as shown here.

**R-0001** · §1.3 ¶3 · keyword-less · mention of MUST
<!-- q L228-228 "A conforming" .. "ication." -->
> A conforming document is a compacted JSON-LD document that complies with all of the relevant "MUST" statements in this specification.

**R-0002** · §1.3 ¶3 · MUST · mention of MUST
<!-- q L228-228 "Specifically" .. "nforced." -->
> Specifically, the relevant normative "MUST" statements in Sections 4. Basic Concepts, 5. Advanced Concepts, and 6. Syntaxes of this document MUST be enforced.

**R-0003** · §1.3 ¶3 · MUST
<!-- q L228-228 "A conforming document M" .. "tion/vp." -->
> A conforming document MUST be either a verifiable credential with a media type of application/vc or a verifiable presentation with a media type of application/vp.

**R-0004** · §1.3 ¶3 · MUST
<!-- q L228-228 "A conforming document MUST be s" .. "hanisms." -->
> A conforming document MUST be secured by at least one securing mechanism as described in Section 4.12 Securing Mechanisms.

_R-0005: the skeleton's sentence (lines 229, MUST first) is split into R-0128, R-0129, R-0130; its text is in requirements.yaml._

**R-0128** · §1.3 ¶4 · keyword-less · split of R-0005
<!-- q L229-229 "A conforming" .. "ocuments" -->
> A conforming issuer implementation produces conforming documents

**R-0129** · §1.3 ¶4 · MUST · split of R-0005
<!-- q L229-229 "MUST include" .. "produces" -->
> MUST include all required properties in the conforming documents it produces

**R-0130** · §1.3 ¶4 · MUST · split of R-0005
<!-- q L229-229 "MUST secure " .. "chanisms" -->
> MUST secure the conforming documents it produces using a securing mechanism described in Section 4.12 Securing Mechanisms

_R-0006: the skeleton's sentence (lines 230, MUST first) is split into R-0132, R-0133, R-0134; its text is in requirements.yaml._

**R-0132** · §1.3 ¶5 · MUST · split of R-0006
<!-- q L230-230 "MUST perform" .. "chanisms" -->
> MUST perform verification on a conforming document as described in Section 4.12 Securing Mechanisms

**R-0133** · §1.3 ¶5 · MUST · split of R-0006
<!-- q L230-230 "MUST check t" .. "t property" -->
> MUST check that each required property satisfies the normative requirements for that property

**R-0134** · §1.3 ¶5 · MUST · split of R-0006
<!-- q L230-230 "MUST produce" .. "detected" -->
> MUST produce errors when non-conforming documents are detected

**R-0007** · §1.3 ¶6 · MAY
<!-- q L231-231 "Optional pro" .. "tations." -->
> Optional properties MAY be ignored by conforming issuer implementations and conforming verifier implementations.

## §2 Terminology

_[definition]_ · §2 ¶1 · lead-in of §2; the terms follow
<!-- q L238-238 -->
> The following terms are used to describe concepts in this specification.

_[definition]_ · §2 ¶2–¶3 (claim)
<!-- q L239-240 -->
> claim An assertion made about a subject.

_[definition]_ · §2 ¶4–¶5 (credential)
<!-- q L241-242 -->
> credential A set of one or more claims made by an issuer. The claims in a credential can be about different subjects. The definition of credential used in this specification differs from, NIST's definitions of credential.

_[definition]_ · §2 ¶6–¶7 (decentralized identifier)
<!-- q L243-244 -->
> decentralized identifier A portable URL-based identifier, also known as a DID, is associated with an entity. These identifiers are most often used in a verifiable credential and are associated with subjects such that a verifiable credential can be easily ported from one credential repository to another without reissuing the credential. An example of a DID is did:example:123456abcdef. See the Decentralized Identifiers (DIDs) v1.0 specification for further details.

_[definition]_ · §2 ¶8–¶9 (default graph)
<!-- q L245-246 -->
> default graph The graph containing all claims that are not explicitly part of a named graph.

_[definition]_ · §2 ¶10–¶11 (entity)
<!-- q L247-248 -->
> entity Anything that can be referenced in statements as an abstract or concrete noun. Entities include but are not limited to people, organizations, physical things, documents, abstract concepts, fictional characters, and arbitrary text. Any entity might perform roles in the ecosystem, if it can do so. Note that some entities fundamentally cannot take actions, for example, the string "abc" cannot issue credentials.

_[definition]_ · §2 ¶12–¶13 (graph)
<!-- q L249-250 -->
> graph A set of claims, forming a network of information composed of subjects and their relationship to other subjects or data. Each claim is part of a graph; either explicit in the case of named graphs, or implicit for the default graph.

_[definition]_ · §2 ¶14–¶15 (holder)
<!-- q L251-252 -->
> holder A role an entity might perform by possessing one or more verifiable credentials and generating verifiable presentations from them. A holder is often, but not always, a subject of the verifiable credentials they are holding. Holders store their credentials in credential repositories.

_[definition]_ · §2 ¶16–¶17 (issuer)
<!-- q L253-254 -->
> issuer A role an entity can perform by asserting claims about one or more subjects, creating a verifiable credential from these claims, and transmitting the verifiable credential to a holder.

_[definition]_ · §2 ¶18–¶19 (named graph)
<!-- q L255-256 -->
> named graph A graph associated with specific properties, such as verifiableCredential. These properties result in separate graphs that contain all claims defined in the corresponding JSON objects.

_[definition]_ · §2 ¶20–¶21 (presentation)
<!-- q L257-258 -->
> presentation Data derived from one or more verifiable credentials issued by one or more issuers that is shared with a specific verifier.

_[definition]_ · §2 ¶22–¶23 (credential repository)
<!-- q L259-260 -->
> credential repository Software, such as a file system, storage vault, or personal verifiable credential wallet, that stores and protects access to holders' verifiable credentials.

_[definition]_ · §2 ¶24–¶25 (selective disclosure)
<!-- q L261-262 -->
> selective disclosure The ability of a holder to make fine-grained decisions about what information to share.

_[definition]_ · §2 ¶26–¶27 (unlinkable disclosure)
<!-- q L263-264 -->
> unlinkable disclosure A type of selective disclosure where presentations cannot be correlated between verifiers.

_[definition]_ · §2 ¶28–¶29 (subject)
<!-- q L265-266 -->
> subject A thing about which claims are made.

_[definition]_ · §2 ¶30–¶31 (validation)
<!-- q L267-268 -->
> validation The assurance that a claim from a specific issuer satisfies the business requirements of a verifier for a particular use. This specification defines how verifiers verify verifiable credentials and verifiable presentations. It also specifies that verifiers validate claims in verifiable credentials before relying on them. However, the means for such validation vary widely and are outside the scope of this specification. Verifiers trust certain issuers for certain claims and apply their own rules to determine which claims in which credentials are suitable for use by their systems.

**R-0135** · §2 ¶31 (validation) · keyword-less · hunted
<!-- q L268-268 "It also spec" .. "on them." -->
> It also specifies that verifiers validate claims in verifiable credentials before relying on them.

_[definition]_ · §2 ¶32–¶33 (verifiable credential)
<!-- q L269-270 -->
> verifiable credential A tamper-evident credential whose authorship can be cryptographically verified. Verifiable credentials can be used to build verifiable presentations, which can also be cryptographically verifiable.

_[definition]_ · §2 ¶34–¶35 (verifiable data registry)
<!-- q L271-272 -->
> verifiable data registry A role a system might perform by mediating the creation and verification of identifiers, verification material, and other relevant data, such as verifiable credential schemas, revocation registries, and so on, which might require using verifiable credentials. Some configurations might require correlatable identifiers for subjects. Some registries, such as ones for UUIDs and verification material, might act as namespaces for identifiers.

_[definition]_ · §2 ¶36–¶37 (verifiable presentation)
<!-- q L273-274 -->
> verifiable presentation A tamper-evident presentation of information encoded in such a way that authorship of the data can be trusted after a process of cryptographic verification. Certain types of verifiable presentations might contain data that is synthesized from, but does not contain, the original verifiable credentials (for example, zero-knowledge proofs).

**R-0136** · §2 ¶38–¶39 (verification) · keyword-less · from C-0027
<!-- q L275-276 "verification" .. "ctively." -->
> verification The evaluation of whether a verifiable credential or verifiable presentation is an authentic and current statement of the issuer or presenter, respectively.

_[definition]_ · §2 ¶38–¶39 (verification)
<!-- q L275-276 -->
> verification The evaluation of whether a verifiable credential or verifiable presentation is an authentic and current statement of the issuer or presenter, respectively. This includes checking that the credential or presentation conforms to the specification, the securing mechanism is satisfied, and, if present, the status check succeeds. Verification of a credential does not imply evaluation of the truth of claims encoded in the credential.

**R-0137** · §2 ¶39 (verification) · keyword-less · hunted
<!-- q L276-276 "This include" .. "ucceeds." -->
> This includes checking that the credential or presentation conforms to the specification, the securing mechanism is satisfied, and, if present, the status check succeeds.

**R-0138** · §2 ¶39 (verification) · keyword-less · from C-0028
<!-- q L276-276 "Verification" .. "dential." -->
> Verification of a credential does not imply evaluation of the truth of claims encoded in the credential.

_[definition]_ · §2 ¶40–¶41 (verifier)
<!-- q L277-278 -->
> verifier A role an entity performs by receiving one or more verifiable credentials, optionally inside a verifiable presentation for processing. Other specifications might refer to this concept as a relying party.

_[definition]_ · §2 ¶42–¶43 (verification material)
<!-- q L279-280 -->
> verification material Information that is used to verify the security of cryptographically protected information. For example, a cryptographic public key is used to verify a digital signature associated with a verifiable credential.

**R-0139** · §2 ¶44–¶45 (URL) · keyword-less · from C-0030
<!-- q L281-282 "URL A Unifor" .. "tandard." -->
> URL A Uniform Resource Locator, as defined by the URL Standard.

_[definition]_ · §2 ¶44–¶45 (URL)
<!-- q L281-282 -->
> URL A Uniform Resource Locator, as defined by the URL Standard. URLs can be dereferenced to result in a resource, such as a document. The rules for dereferencing, or fetching, a URL are defined by the URL scheme. This specification does not use the term URI or IRI because those terms have been deemed to be confusing to Web developers.

## §4.2 Verifiable Credentials

_[definition]_ · §4.2 ¶1 · lead-in of the credential's property list
<!-- q L356-356 -->
> Verifiable credentials are used to express properties of one or more subjects as well as properties of the credential itself. The following properties are defined in this specification for a verifiable credential:

_[definition]_ · §4.2 ¶2–¶3 (@context)
<!-- q L357-358 -->
> @context Defined in Section 4.3 Contexts.

_[definition]_ · §4.2 ¶4–¶5 (id)
<!-- q L359-360 -->
> id Defined in Section 4.4 Identifiers.

_[definition]_ · §4.2 ¶6–¶7 (type)
<!-- q L361-362 -->
> type Defined in Section 4.5 Types.

_[definition]_ · §4.2 ¶8–¶9 (name)
<!-- q L363-364 -->
> name Defined in Section 4.6 Names and Descriptions.

_[definition]_ · §4.2 ¶10–¶11 (description)
<!-- q L365-366 -->
> description Defined in Section 4.6 Names and Descriptions.

_[definition]_ · §4.2 ¶12–¶13 (issuer)
<!-- q L367-368 -->
> issuer Defined in Section 4.7 Issuer.

_[definition]_ · §4.2 ¶14–¶15 (credentialSubject)
<!-- q L369-370 -->
> credentialSubject Defined in Section 4.8 Credential Subject.

_[definition]_ · §4.2 ¶16–¶17 (validFrom)
<!-- q L371-372 -->
> validFrom Defined in Section 4.9 Validity Period.

_[definition]_ · §4.2 ¶18–¶19 (validUntil)
<!-- q L373-374 -->
> validUntil Defined in Section 4.9 Validity Period.

_[definition]_ · §4.2 ¶20–¶21 (status) · the term status names no property: §4.10 defines credentialStatus (SD-2)
<!-- q L375-376 -->
> status Defined in Section 4.10 Status.

_[definition]_ · §4.2 ¶22–¶23 (credentialSchema)
<!-- q L377-378 -->
> credentialSchema Defined in Section 4.11 Data Schemas.

_[definition]_ · §4.2 ¶24–¶25 (refreshService)
<!-- q L379-380 -->
> refreshService Defined in Section 5.4 Refreshing.

_[definition]_ · §4.2 ¶26–¶27 (termsOfUse)
<!-- q L381-382 -->
> termsOfUse Defined in Section 5.5 Terms of Use.

_[definition]_ · §4.2 ¶28–¶29 (evidence)
<!-- q L383-384 -->
> evidence Defined in Section 5.6 Evidence.

## §4.3 Contexts

**R-0008** · §4.3 ¶3 · MUST
<!-- q L391-391 "Verifiable c" .. "roperty." -->
> Verifiable credentials and verifiable presentations MUST include a @context property.

**R-0009** · §4.3 ¶3 · MUST
<!-- q L391-391 "Application " .. "ication." -->
> Application developers MUST understand every JSON-LD context used by their application, at least to the extent that it affects the meaning of the terms used by their application.

_R-0010: the skeleton's sentence (lines 391-393, MAY first) is split into R-0140, R-0141; its text is in requirements.yaml._

**R-0140** · §4.3 ¶3 · MAY · split of R-0010
<!-- q L391-391 "Other specif" .. "chanism." -->
> Other specifications that build upon this specification MAY require that JSON-LD contexts be integrity protected by using the relatedResource feature described in Section 5.3 Integrity of Related Resources or any effectively equivalent mechanism.

**R-0141** · §4.3 ¶5 (@context) · MUST · split of R-0010
<!-- q L393-393 "The value of" .. "ials/v2." -->
> The value of the @context property MUST be an ordered set where the first item is a URL with the value https://www.w3.org/ns/credentials/v2.

**R-0011** · §4.3 ¶5 (@context) · MUST
<!-- q L393-393 "Subsequent i" .. "Context." -->
> Subsequent items in the ordered set MUST be composed of any combination of URLs and objects, where each is processable as a JSON-LD Context.

_Inferred, not verbatim: **R-0142** (§4.3 ¶5 (@context)); its words are this extraction's and its grounds are quoted in requirements.yaml._

**R-0143** · §4.3 ¶7 · keyword-less · hunted
<!-- q L414-414 "The data ava" .. "Context." -->
> The data available at https://www.w3.org/ns/credentials/v2 is a permanently cacheable static document with instructions for processing it provided in Appendix B.1 Base Context.

**R-0144** · §4.3 ¶8 · keyword-less · hunted
<!-- q L415-415 "Implementati" .. "systems." -->
> Implementations are expected to not use this URL for any other purpose, such as in pilot or production systems.

## §4.4 Identifiers

**R-0145** · §4.4 ¶1 · keyword-less · from C-0058
<!-- q L421-421 "The id prope" .. "ntation." -->
> The id property allows for expressing statements about specific things in the verifiable credential and is set by an issuer when expressing objects in a verifiable credential or a holder when expressing objects in a verifiable presentation.

_R-0012: the skeleton's sentence (lines 423-425, OPTIONAL first) is split into R-0146, R-0147, R-0148; its text is in requirements.yaml._

**R-0146** · §4.4 ¶4 (id) · OPTIONAL · split of R-0012
<!-- q L425-425 "The id prope" .. "PTIONAL." -->
> The id property is OPTIONAL.

**R-0147** · §4.4 ¶4 (id) · MUST · split of R-0012
<!-- q L425-425 "If present, " .. "ngle URL" -->
> If present, id property's value MUST be a single URL

**R-0148** · §4.4 ¶4 (id) · MAY · split of R-0012
<!-- q L425-425 "which MAY be" .. "enceable" -->
> which MAY be dereferenceable

**R-0013** · §4.4 ¶4 (id) · RECOMMENDED
<!-- q L425-425 "It is RECOMM" .. " the id." -->
> It is RECOMMENDED that the URL in the id be one which, if dereferenceable, results in a document containing machine-readable information about the id.

## §4.5 Types

_R-0014: the skeleton's sentence (lines 660-662, MUST first) is split into R-0149, R-0150; its text is in requirements.yaml._

**R-0149** · §4.5 ¶2 · MUST · split of R-0014
<!-- q L660-660 -->
> Verifiable credentials and verifiable presentations MUST contain a type property with an associated value.

**R-0150** · §4.5 ¶4 (type) · MUST · split of R-0014
<!-- q L662-662 "The value of" .. "strings." -->
> The value of the type property MUST be one or more terms and absolute URL strings.

**R-0151** · §4.5 ¶4 (type) · keyword-less · from C-0067
<!-- q L662-662 "If more than" .. " matter." -->
> If more than one value is provided, the order does not matter.

_R-0015: the skeleton's sentence (lines 883-892, MUST first) is split into R-0152, R-0153; its text is in requirements.yaml._

**R-0152** · §4.5 ¶6 · MUST · split of R-0015
<!-- q L890-890 -->
> Concerning this specification, the following table lists the objects that MUST have a type specified.

**R-0153** · §4.5 ¶8 · keyword-less · split of R-0015
<!-- q L892-892 "Verifiable c" .. "al type." -->
> Verifiable credential object | VerifiableCredential and, optionally, a more specific verifiable credential type.

**R-0154** · §4.5 ¶10 · keyword-less · hunted
<!-- q L894-894 "Verifiable p" .. "on type." -->
> Verifiable presentation object | VerifiablePresentation and, optionally, a more specific verifiable presentation type.

**R-0155** · §4.5 ¶12 · keyword-less · hunted
<!-- q L896-896 "credentialSt" .. "us type." -->
> credentialStatus object | A valid credential status type.

**R-0156** · §4.5 ¶14 · keyword-less · hunted
<!-- q L898-898 "termsOfUse o" .. "se type." -->
> termsOfUse object | A valid terms of use type.

**R-0157** · §4.5 ¶16 · keyword-less · hunted
<!-- q L900-900 "evidence obj" .. "ce type." -->
> evidence object | A valid evidence type.

**R-0158** · §4.5 ¶18 · keyword-less · hunted
<!-- q L902-902 "refreshServi" .. "ce type." -->
> refreshService object | A valid refreshService type.

**R-0159** · §4.5 ¶20 · keyword-less · hunted
<!-- q L904-904 "credentialSc" .. "ma type." -->
> credentialSchema object | A valid credentialSchema type.

**R-0016** · §4.5 ¶23 · SHOULD
<!-- q L908-908 -->
> All credentials, presentations, and encapsulated objects SHOULD specify, or be associated with, additional, more narrow types (like ExampleDegreeCredential, for example) so software systems can more easily detect and process this additional information.

**R-0017** · §4.5 ¶24 · SHOULD
<!-- q L909-909 "When process" .. "erarchy." -->
> When processing encapsulated objects defined in this specification, such as objects associated with the credentialSubject object or deeply nested therein, software systems SHOULD use the type information specified in encapsulating objects higher in the hierarchy.

**R-0018** · §4.5 ¶24 · SHOULD
<!-- q L909-909 "Specifically" .. "ct type." -->
> Specifically, an encapsulating object, such as a credential, SHOULD convey the associated object types so that verifiers can quickly determine the contents of an associated object based on the encapsulating object type.

**R-0160** · §4.5 ¶29 · keyword-less · from C-0070
<!-- q L914-914 "Object types" .. "he type." -->
> Object types and their associated values are expected to be documented in at least a human-readable specification that can be found at the URL for the type.

## §4.6 Names and Descriptions

_R-0019: the skeleton's sentence (lines 920-922, OPTIONAL first) is split into R-0161, R-0162; its text is in requirements.yaml._

**R-0161** · §4.6 ¶3 (name) · OPTIONAL · split of R-0019
<!-- q L922-922 "An OPTIONAL " .. "dential." -->
> An OPTIONAL property that expresses the name of the credential.

**R-0162** · §4.6 ¶3 (name) · MUST · split of R-0019
<!-- q L922-922 "If present, " .. "rection." -->
> If present, the value of the name property MUST be a string or a language value object as described in 11.1 Language and Base Direction.

_R-0020: the skeleton's sentence (lines 922-924, OPTIONAL first) is split into R-0163, R-0164; its text is in requirements.yaml._

**R-0163** · §4.6 ¶5 (description) · OPTIONAL · split of R-0020
<!-- q L924-924 "An OPTIONAL " .. "dential." -->
> An OPTIONAL property that conveys specific details about a credential.

**R-0164** · §4.6 ¶5 (description) · MUST · split of R-0020
<!-- q L924-924 "If present, " .. "rection." -->
> If present, the value of the description property MUST be a string or a language value object as described in 11.1 Language and Base Direction.

**R-0166** · §4.6 ¶7 · keyword-less · from C-0073
<!-- q L1198-1198 "To express a" .. "ctively." -->
> To express a string with language and base direction information, one can use an object that contains the @value, @language, and @direction properties to express the text value, language tag, and base direction, respectively.

_Inferred, not verbatim: **R-0165** (§4.6 ¶5 (description)); its words are this extraction's and its grounds are quoted in requirements.yaml._

## §4.7 Issuer

_R-0021: the skeleton's sentence (lines 1279-1282, MUST first) is split into R-0167, R-0168, R-0169; its text is in requirements.yaml._

**R-0167** · §4.7 ¶2 · MUST · split of R-0021
<!-- q L1280-1280 -->
> A verifiable credential MUST have an issuer property.

**R-0168** · §4.7 ¶4 (issuer) · MUST · split of R-0021
<!-- q L1282-1282 "The value of" .. "is a URL" -->
> The value of the issuer property MUST be either a URL or an object containing an id property whose value is a URL

**R-0169** · §4.7 ¶4 (issuer) · keyword-less · split of R-0021
<!-- q L1282-1282 "in either ca" .. "ous way." -->
> in either case, the issuer selects this URL to identify itself in a globally unambiguous way.

_R-0022: the skeleton's sentence (lines 1282-1290, RECOMMENDED first) is split into R-0170; its text is in requirements.yaml._

**R-0170** · §4.7 ¶4 (issuer) · RECOMMENDED · split of R-0022
<!-- q L1282-1282 "It is RECOMM" .. "dential." -->
> It is RECOMMENDED that the URL be one which, if dereferenced, results in a controlled identifier document, as defined in the Controlled Identifiers v1.0 specification, about the issuer that can be used to verify the information expressed in the credential.

## §4.8 Credential Subject

_R-0023: the skeleton's sentence (lines 1772-1774, MUST first) is split into R-0171, R-0172, R-0173, R-0174; its text is in requirements.yaml._

**R-0171** · §4.8 ¶2 · MUST · split of R-0023
<!-- q L1772-1772 -->
> A verifiable credential MUST contain a credentialSubject property.

**R-0172** · §4.8 ¶4 (credentialSubject) · keyword-less · split of R-0023
<!-- q L1774-1774 "The value of" .. " objects" -->
> The value of the credentialSubject property is a set of objects

**R-0173** · §4.8 ¶4 (credentialSubject) · MUST · split of R-0023
<!-- q L1774-1774 "where each o" .. "e claims" -->
> where each object MUST be the subject of one or more claims

**R-0174** · §4.8 ¶4 (credentialSubject) · MUST · split of R-0023
<!-- q L1774-1774 "which MUST b" .. "property" -->
> which MUST be serialized inside the credentialSubject property

**R-0024** · §4.8 ¶4 (credentialSubject) · MAY
<!-- q L1774-1774 "Each object " .. "tifiers." -->
> Each object MAY also contain an id property to identify the subject, as described in Section 4.4 Identifiers.

_Inferred, not verbatim: **R-0175** (§4.8 ¶4 (credentialSubject)); its words are this extraction's and its grounds are quoted in requirements.yaml._

## §4.9 Validity Period

**R-0176** · §4.9 ¶2 · keyword-less · hunted
<!-- q L2028-2028 "When compari" .. "imeline." -->
> When comparing dates and times, the calculation is done "temporally", meaning that the string value is converted to a "temporal value" which exists as a point on a timeline.

_R-0025: the skeleton's sentence (lines 2028-2030, MUST first) is split into R-0177, R-0178; its text is in requirements.yaml._

**R-0177** · §4.9 ¶2 · keyword-less · split of R-0025
<!-- q L2028-2028 "Temporal com" .. "imeline." -->
> Temporal comparisons are then performed by checking to see where the date and time being compared are in relation to a particular point on the timeline.

**R-0178** · §4.9 ¶4 (validFrom) · MUST · split of R-0025
<!-- q L2030-2030 "If present, " .. "he past." -->
> If present, the value of the validFrom property MUST be a [XMLSCHEMA11-2] dateTimeStamp string value representing the date and time the credential becomes valid, which could be a date and time in the future or the past.

**R-0179** · §4.9 ¶4 (validFrom) · keyword-less · hunted
<!-- q L2030-2030 "Note that th" .. "s valid." -->
> Note that this value represents the earliest point in time at which the information associated with the credentialSubject property becomes valid.

_R-0026: the skeleton's sentence (lines 2030-2032, MUST first) is split into R-0180, R-0181; its text is in requirements.yaml._

**R-0180** · §4.9 ¶4 (validFrom) · MUST · split of R-0026
<!-- q L2030-2030 "If a validUn" .. "l value." -->
> If a validUntil value also exists, the validFrom value MUST express a point in time that is temporally the same or earlier than the point in time expressed by the validUntil value.

**R-0181** · §4.9 ¶6 (validUntil) · MUST · split of R-0026
<!-- q L2032-2032 "If present, " .. " future." -->
> If present, the value of the validUntil property MUST be a [XMLSCHEMA11-2] dateTimeStamp string value representing the date and time the credential ceases to be valid, which could be a date and time in the past or the future.

**R-0182** · §4.9 ¶6 (validUntil) · keyword-less · from C-0079
<!-- q L2032-2032 "Note that th" .. "s valid." -->
> Note that this value represents the latest point in time at which the information associated with the credentialSubject property is valid.

**R-0027** · §4.9 ¶6 (validUntil) · MUST
<!-- q L2032-2032 "If a validFr" .. "m value." -->
> If a validFrom value also exists, the validUntil value MUST express a point in time that is temporally the same or later than the point in time expressed by the validFrom value.

## §4.10 Status

**R-0183** · §4.10 ¶2 · keyword-less · hunted
<!-- q L2272-2272 "If present, " .. "objects." -->
> If present, the value associated with the credentialStatus property is a single object or a set of one or more objects.

_R-0028: the skeleton's sentence (lines 2272-2274, OPTIONAL first) is split into R-0184, R-0185; its text is in requirements.yaml._

**R-0184** · §4.10 ¶4 (id) · OPTIONAL · split of R-0028
<!-- q L2274-2274 "The id prope" .. "PTIONAL." -->
> The id property is OPTIONAL.

**R-0185** · §4.10 ¶4 (id) · MAY · split of R-0028
<!-- q L2274-2274 "It MAY be us" .. " object." -->
> It MAY be used to provide a unique identifier for the credential status object.

_R-0029: the skeleton's sentence (lines 2274-2276, MUST first) is split into R-0186, R-0187; its text is in requirements.yaml._

**R-0186** · §4.10 ¶4 (id) · MUST · split of R-0029
<!-- q L2274-2274 "If present, " .. "ollowed." -->
> If present, the normative guidance in Section 4.4 Identifiers MUST be followed.

**R-0187** · §4.10 ¶6 (type) · REQUIRED · split of R-0029
<!-- q L2276-2276 "The type pro" .. "EQUIRED." -->
> The type property is REQUIRED.

**R-0030** · §4.10 ¶6 (type) · MUST
<!-- q L2276-2276 "The related " .. "ollowed." -->
> The related normative guidance in Section 4.5 Types MUST be followed.

**R-0188** · §4.10 ¶7 · keyword-less · hunted
<!-- q L2277-2277 "The precise " .. "hancing." -->
> The precise content of the credential status information is determined by the specific credentialStatus type definition and varies depending on factors such as whether it is simple to implement or if it is privacy-enhancing.

**R-0031** · §4.10 ¶13 · MUST NOT
<!-- q L2341-2341 "Credential s" .. "subject." -->
> Credential status specifications MUST NOT enable tracking of individuals, such as an issuer being notified (either directly or indirectly) when a verifier is interested in a specific holder or subject.

**R-0189** · §4.10 ¶13 · keyword-less · hunted
<!-- q L2341-2341 "Unacceptable" .. "ividual." -->
> Unacceptable approaches include "phoning home," such that every use of a credential contacts the issuer of the credential to check the status for a specific individual, or "pseudonymity reduction," such that every use of the credential causes a request for information from the issuer that the issuer can use to deduce verifier interest in a specific individual.

## §4.11 Data Schemas

_R-0032: the skeleton's sentence (lines 2349-2351, MUST first) is split into R-0190; its text is in requirements.yaml._

**R-0190** · §4.11 ¶7 (credentialSchema) · MUST · split of R-0032
<!-- q L2351-2351 "The value of" .. "hema(s)." -->
> The value of the credentialSchema property MUST be one or more data schemas that provide verifiers with enough information to determine whether the provided data conforms to the provided schema(s).

_R-0033: the skeleton's sentence (lines 2351, MUST first) is split into R-0191, R-0192; its text is in requirements.yaml._

**R-0191** · §4.11 ¶7 (credentialSchema) · MUST · split of R-0033
<!-- q L2351-2351 "Each credent" .. "property" -->
> Each credentialSchema MUST specify its type (for example, JsonSchema) and an id property

**R-0192** · §4.11 ¶7 (credentialSchema) · MUST · split of R-0033
<!-- q L2351-2351 "that MUST be" .. "ema file" -->
> that MUST be a URL identifying the schema file

**R-0193** · §4.11 ¶7 (credentialSchema) · keyword-less · hunted
<!-- q L2351-2351 "The specific" .. " schema." -->
> The specific type definition determines the precise contents of each data schema.

**R-0194** · §4.11 ¶8 (credentialSchema) · keyword-less · hunted
<!-- q L2352-2352 -->
> If multiple schemas are present, validity is determined according to the processing rules outlined by each associated type property.

## §4.12 Securing Mechanisms

_[definition]_ · §4.12 ¶1
<!-- q L2390-2390 -->
> This specification recognizes two classes of securing mechanisms: those that use enveloping proofs and those that use embedded proofs.

**R-0195** · §4.12 ¶2 · keyword-less · hunted
<!-- q L2391-2391 "An envelopin" .. "a model." -->
> An enveloping proof wraps a serialization of this data model.

**R-0034** · §4.12 ¶2 · RECOMMENDED
<!-- q L2391-2391 "One such REC" .. "E-COSE]." -->
> One such RECOMMENDED enveloping proof mechanism is defined in Securing Verifiable Credentials using JOSE and COSE [VC-JOSE-COSE].

**R-0196** · §4.12 ¶3 · keyword-less · from C-0088
<!-- q L2392-2392 "An embedded " .. "a model." -->
> An embedded proof is a mechanism where the proof is included in the serialization of the data model.

**R-0035** · §4.12 ¶3 · RECOMMENDED
<!-- q L2392-2392 "One such REC" .. "EGRITY]." -->
> One such RECOMMENDED embedded proof mechanism is defined in Verifiable Credential Data Integrity 1.0 [VC-DATA-INTEGRITY].

**R-0197** · §4.12 ¶4 · keyword-less · hunted
<!-- q L2393-2393 "These two cl" .. "clusive." -->
> These two classes of securing mechanisms are not mutually exclusive.

## §4.13 Verifiable Presentations

**R-0036** · §4.13 ¶1 · MAY
<!-- q L2466-2466 -->
> Verifiable presentations MAY be used to aggregate information from multiple verifiable credentials.

**R-0037** · §4.13 ¶2 · SHOULD
<!-- q L2467-2467 "Verifiable p" .. "erifier." -->
> Verifiable presentations SHOULD be extremely short-lived and bound to a challenge provided by a verifier.

**R-0198** · §4.13 ¶2 · keyword-less · from C-0090
<!-- q L2467-2467 "Unless addit" .. "entials." -->
> Unless additional requirements are defined by the particular securing mechanism or embedding protocol, a verifier cannot generally assume that the verifiable presentation correlates with the presented verifiable credentials.

_[definition]_ · §4.13 ¶3
<!-- q L2468-2468 -->
> The default graph of a verifiable presentation is also referred to as the verifiable presentation graph.

_R-0038: the skeleton's sentence (lines 2469-2471, MAY first) is split into R-0199, R-0200; its text is in requirements.yaml._

**R-0199** · §4.13 ¶6 (id) · keyword-less · split of R-0038
<!-- q L2471-2471 "The id prope" .. "ptional." -->
> The id property is optional.

**R-0200** · §4.13 ¶6 (id) · MAY · split of R-0038
<!-- q L2471-2471 "It MAY be us" .. "ntation." -->
> It MAY be used to provide a unique identifier for the verifiable presentation.

_R-0039: the skeleton's sentence (lines 2471-2473, MUST first) is split into R-0201, R-0202; its text is in requirements.yaml._

**R-0201** · §4.13 ¶6 (id) · MUST · split of R-0039
<!-- q L2471-2471 "If present, " .. "ollowed." -->
> If present, the normative guidance in Section 4.4 Identifiers MUST be followed.

**R-0202** · §4.13 ¶8 (type) · MUST · split of R-0039
<!-- q L2473-2473 "The type pro" .. "present." -->
> The type property MUST be present.

_R-0040: the skeleton's sentence (lines 2473, MUST first) is split into R-0203, R-0204; its text is in requirements.yaml._

**R-0203** · §4.13 ¶8 (type) · MUST · split of R-0040
<!-- q L2473-2473 "One value of" .. "entation" -->
> One value of this property MUST be VerifiablePresentation

**R-0204** · §4.13 ¶8 (type) · MAY · split of R-0040
<!-- q L2473-2473 "but addition" .. "included" -->
> but additional types MAY be included

_R-0041: the skeleton's sentence (lines 2473-2475, MUST first) is split into R-0205, R-0206; its text is in requirements.yaml._

**R-0205** · §4.13 ¶8 (type) · MUST · split of R-0041
<!-- q L2473-2473 "The related " .. "ollowed." -->
> The related normative guidance in Section 4.5 Types MUST be followed.

**R-0206** · §4.13 ¶10 (verifiableCredential) · MAY · split of R-0041
<!-- q L2475-2475 "The verifiab" .. "present." -->
> The verifiableCredential property MAY be present.

_R-0042: the skeleton's sentence (lines 2475, MUST first) is split into R-0207, R-0208; its text is in requirements.yaml._

**R-0207** · §4.13 ¶10 (verifiableCredential) · MUST · split of R-0042
<!-- q L2475-2475 "The value MU" .. " objects" -->
> The value MUST be one or more verifiable credential and/or enveloped verifiable credential objects

**R-0208** · §4.13 ¶10 (verifiableCredential) · MUST NOT · split of R-0042
<!-- q L2475-2475 "the values M" .. " or URLs" -->
> the values MUST NOT be non-object values such as numbers, strings, or URLs

**R-0043** · §4.13 ¶10 (verifiableCredential) · MUST
<!-- q L2475-2475 "These object" .. "chanism." -->
> These objects are called verifiable credential graphs and MUST express information that is secured using a securing mechanism.

_R-0044: the skeleton's sentence (lines 2475-2477, MAY first) is split into R-0209; its text is in requirements.yaml._

**R-0209** · §4.13 ¶12 (holder) · MAY · split of R-0044
<!-- q L2477-2477 "The verifiab" .. "roperty." -->
> The verifiable presentation MAY include a holder property.

**R-0045** · §4.13 ¶12 (holder) · MUST
<!-- q L2477-2477 "If present, " .. "roperty." -->
> If present, the value MUST be either a URL or an object containing an id property.

**R-0046** · §4.13 ¶12 (holder) · RECOMMENDED
<!-- q L2477-2477 "It is RECOMM" .. "ntation." -->
> It is RECOMMENDED that the URL in the holder or its id be one which, if dereferenced, results in a document containing machine-readable information about the holder that can be used to verify the information expressed in the verifiable presentation.

**R-0210** · §4.13 ¶12 (holder) · keyword-less · from C-0092
<!-- q L2477-2477 "If the holde" .. "ntation." -->
> If the holder property is absent, information about the holder is obtained either via the securing mechanism or does not pertain to the validation of the verifiable presentation.

**R-0211** · §4.13 «Enveloped Verifiable Credentials» ¶1 · keyword-less · from C-0093
<!-- q L2495-2495 "This can be " .. "dential." -->
> This can be accomplished by associating the verifiableCredential property with an object that has a type of EnvelopedVerifiableCredential.

_[definition]_ · §4.13 «Enveloped Verifiable Credentials» ¶3 (EnvelopedVerifiableCredential)
<!-- q L2497-2497 "They are use" .. "ntation." -->
> They are used to associate an object containing an enveloped verifiable credential with the verifiableCredential property in a verifiable presentation.

**R-0047** · §4.13 «Enveloped Verifiable Credentials» ¶3 (EnvelopedVerifiableCredential) · MUST
<!-- q L2497-2497 "The @context" .. "ication." -->
> The @context property of the object MUST be present and include a context, such as the base context for this specification, that defines at least the id, type, and EnvelopedVerifiableCredential terms as defined by the base context provided by this specification.

**R-0048** · §4.13 «Enveloped Verifiable Credentials» ¶3 (EnvelopedVerifiableCredential) · MUST
<!-- q L2497-2497 "The id value" .. "E-COSE]." -->
> The id value of the object MUST be a data: URL [RFC2397] that expresses a secured verifiable credential using an enveloping security scheme, such as Securing Verifiable Credentials using JOSE and COSE [VC-JOSE-COSE].

_R-0049: the skeleton's sentence (lines 2497-2499, MUST first) is split into R-0212; its text is in requirements.yaml._

**R-0212** · §4.13 «Enveloped Verifiable Credentials» ¶3 (EnvelopedVerifiableCredential) · MUST · split of R-0049
<!-- q L2497-2497 "The type val" .. "dential." -->
> The type value of the object MUST be EnvelopedVerifiableCredential.

**R-0213** · §4.13 «Enveloped Verifiable Presentations» ¶1 · keyword-less · from C-0094
<!-- q L2519-2519 "This can be " .. "ntation." -->
> This can be accomplished by using an object that has a type of EnvelopedVerifiablePresentation.

_[definition]_ · §4.13 «Enveloped Verifiable Presentations» ¶3 (EnvelopedVerifiablePresentation)
<!-- q L2521-2521 "Used to expr" .. "ntation." -->
> Used to express an enveloped verifiable presentation.

**R-0050** · §4.13 «Enveloped Verifiable Presentations» ¶3 (EnvelopedVerifiablePresentation) · MUST
<!-- q L2521-2521 "The @context" .. "ication." -->
> The @context property of the object MUST be present and include a context, such as the base context for this specification, that defines at least the id, type, and EnvelopedVerifiablePresentation terms as defined by the base context provided by this specification.

**R-0051** · §4.13 «Enveloped Verifiable Presentations» ¶3 (EnvelopedVerifiablePresentation) · MUST
<!-- q L2521-2521 "The id value" .. "E-COSE]." -->
> The id value of the object MUST be a data: URL [RFC2397] that expresses a secured verifiable presentation using an enveloping securing mechanism, such as Securing Verifiable Credentials using JOSE and COSE [VC-JOSE-COSE].

**R-0052** · §4.13 «Enveloped Verifiable Presentations» ¶3 (EnvelopedVerifiablePresentation) · MUST
<!-- q L2521-2521 "The type val" .. "ntation." -->
> The type value of the object MUST be EnvelopedVerifiablePresentation.

**R-0053** · §4.13 «Presentations Including Holder Claims» ¶1 · MAY
<!-- q L2541-2541 "A holder MAY" .. "mselves." -->
> A holder MAY use the verifiableCredential property in a verifiable presentation to include verifiable credentials from any issuer, including themselves.

**R-0214** · §4.13 «Presentations Including Holder Claims» ¶1 · keyword-less · hunted
<!-- q L2541-2541 "When the iss" .. "sserted." -->
> When the issuer of a verifiable credential is the holder, the claims in that verifiable credential are considered self-asserted.

**R-0215** · §4.13 «Presentations Including Holder Claims» ¶1 · keyword-less · from C-0095
<!-- q L2541-2541 "Such self-as" .. "entials." -->
> Such self-asserted claims can be secured by the same mechanism that secures the verifiable presentation in which they are included or by any mechanism usable for other verifiable credentials.

**R-0216** · §4.13 «Presentations Including Holder Claims» ¶2 · keyword-less · from C-0096
<!-- q L2542-2542 "The subject(" .. "ncluded." -->
> The subject(s) of these self-asserted claims are not limited, so these claims can include statements about the holder, one of the other included verifiable credentials or even the verifiable presentation in which the self-asserted verifiable credential is included.

**R-0054** · §4.13 «Presentations Including Holder Claims» ¶3 · MUST
<!-- q L2543-2543 -->
> A verifiable presentation that includes a self-asserted verifiable credential, which is secured only using the same mechanism as the verifiable presentation, MUST include a holder property.

**R-0217** · §4.13 «Presentations Including Holder Claims» ¶4 · keyword-less · hunted
<!-- q L2544-2544 -->
> All of the normative requirements defined for verifiable credentials apply to self-asserted verifiable credentials.

**R-0218** · §4.13 «Presentations Including Holder Claims» ¶5 · keyword-less · hunted
<!-- q L2545-2545 -->
> A verifiable credential in a verifiable presentation is considered self-asserted when the value of the issuer property of the verifiable credential is identical to the value of the holder property of the verifiable presentation.

## §5.2 Extensibility

**R-0055** · §5.2 «Semantic Interoperability» ¶1 · SHOULD
<!-- q L2867-2867 "When definin" .. "ed Data." -->
> When defining new terms in an application-specific vocabulary, vocabulary authors SHOULD follow the detailed checklist in Best Practices for Publishing Linked Data.

**R-0056** · §5.2 «Semantic Interoperability» ¶1–¶2 · RECOMMENDED
<!-- q L2867-2868 "Specifically" .. "ema.org." -->
> Specifically, the following guidance is of particular importance: Whenever possible, it is RECOMMENDED to re-use terms — and their corresponding URLs — defined by well-known, public vocabularies, such as Schema.org.

**R-0057** · §5.2 «Semantic Interoperability» ¶3 · MUST
<!-- q L2869-2869 "New terms MU" .. "ch term." -->
> New terms MUST define a new URL for each term.

**R-0058** · §5.2 «Semantic Interoperability» ¶3–¶4 · MUST
<!-- q L2869-2870 "When doing s" .. "ch term." -->
> When doing so, the general guidelines for [LINKED-DATA] are expected to be followed, in particular: Human-readable documentation MUST be published, describing the semantics of and the constraints on the use of each term.

_R-0059: the skeleton's sentence (lines 2871-2872, RECOMMENDED first) is split into R-0219, R-0220; its text is in requirements.yaml._

**R-0219** · §5.2 «Semantic Interoperability» ¶5 · RECOMMENDED · split of R-0059
<!-- q L2871-2871 -->
> It is RECOMMENDED to also publish the collection of all new terms as a machine-readable vocabulary using RDF Schema 1.1.

**R-0220** · §5.2 «Semantic Interoperability» ¶6 · SHOULD · split of R-0059
<!-- q L2872-2872 -->
> It SHOULD be possible to dereference the URL of a term, resulting in its description and/or formal definition.

**R-0060** · §5.2 «Semantic Interoperability» ¶7 · MUST
<!-- q L2873-2873 "Furthermore," .. "abulary." -->
> Furthermore, a machine-readable description (that is, a JSON-LD Context document) MUST be published at the URL specified in the @context property for the vocabulary.

**R-0061** · §5.2 «Semantic Interoperability» ¶7 · MUST
<!-- q L2873-2873 "This context" .. "y value." -->
> This context MUST map each term to its corresponding URL, possibly accompanied by further constraints like the type of the property value.

**R-0221** · §5.2 «Semantic Interoperability» ¶7 · keyword-less · hunted
<!-- q L2873-2873 "A human-read" .. "ability." -->
> A human-readable document describing the expected order of values for the @context property is also expected to be published by any implementer seeking interoperability.

**R-0062** · §5.2 «Semantic Interoperability» ¶9 · SHOULD NOT
<!-- q L2876-2876 "A conforming" .. "cations." -->
> A conforming document SHOULD NOT use the @vocab feature in production as it can lead to JSON term clashes, resulting in semantic ambiguities with other applications.

**R-0063** · §5.2 «Semantic Interoperability» ¶9 · SHOULD
<!-- q L2876-2876 "Instead, to " .. "ibility." -->
> Instead, to achieve proper interoperability, a conforming document SHOULD use JSON-LD Contexts that define all terms used by their applications, as described earlier in Section 5.2 Extensibility.

**R-0064** · §5.2 «Semantic Interoperability» ¶9 · MUST
<!-- q L2876-2876 "If a conform" .. "roperty." -->
> If a conforming document does not use JSON-LD Contexts that define all terms used, it MUST include the https://www.w3.org/ns/credentials/undefined-terms/v2 as the last value in the @context property.

## §5.3 Integrity of Related Resources

_R-0065: the skeleton's sentence (lines 2881-2885, MAY first) is split into R-0222, R-0223, R-0224; its text is in requirements.yaml._

**R-0222** · §5.3 ¶2 · MAY · split of R-0065
<!-- q L2881-2881 "To extend in" .. "property" -->
> To extend integrity protection to a related resource, an issuer of a verifiable credential MAY include the relatedResource property

**R-0223** · §5.3 ¶4 (relatedResource) · MUST · split of R-0065
<!-- q L2883-2883 "The value of" .. "ing form" -->
> The value of the relatedResource property MUST be one or more objects of the following form

**R-0224** · §5.3 ¶6 (relatedResource) · REQUIRED · split of R-0065
<!-- q L2885-2885 "id | The ide" .. "tifiers." -->
> id | The identifier for the resource is REQUIRED and conforms to the format defined in Section 4.4 Identifiers.

_R-0066: the skeleton's sentence (lines 2885-2888, MUST first) is split into R-0225, R-0226, R-0227, R-0228; its text is in requirements.yaml._

**R-0225** · §5.3 ¶6 (relatedResource) · MUST · split of R-0066
<!-- q L2885-2885 "The value MU" .. "objects." -->
> The value MUST be unique among the list of related resource objects.

**R-0226** · §5.3 ¶7 (relatedResource) · OPTIONAL · split of R-0066
<!-- q L2886-2886 "mediaType | " .. "egistry." -->
> mediaType | An OPTIONAL valid media type as listed in the IANA Media Types registry.

**R-0227** · §5.3 ¶8 (relatedResource) · keyword-less · split of R-0066
<!-- q L2887-2887 "digestSRI | " .. "tribute." -->
> digestSRI | One or more cryptographic digests, as defined by the hash-expression ABNF grammar defined in the Subresource Integrity specification, Section 3.5: The integrity attribute.

**R-0228** · §5.3 ¶9 (relatedResource) · keyword-less · split of R-0066
<!-- q L2888-2888 "digestMultib" .. "tegrity." -->
> digestMultibase | One or more cryptographic digests, as defined by the digestMultibase property in the Verifiable Credential Data Integrity 1.0 specification, Section 2.6: Resource Integrity.

**R-0067** · §5.3 ¶10 (relatedResource) · MUST
<!-- q L2889-2889 -->
> Each object associated with relatedResource MUST contain at least a digestSRI or a digestMultibase value.

**R-0068** · §5.3 ¶11–¶13 · SHOULD
<!-- q L2890-2892 -->
> If a mediaType is listed, implementations that retrieve the resource identified by the id property using HTTP Semantics SHOULD: use the media type in the Accept HTTP Header, and reject the response if it includes a Content-Type HTTP Header with a different media type.

_R-0069: the skeleton's sentence (lines 2893, MAY first) is split into R-0229, R-0230; its text is in requirements.yaml._

**R-0229** · §5.3 ¶14 · MAY · split of R-0069
<!-- q L2893-2893 "Any object i" .. "e property" -->
> Any object in the verifiable credential that contains an id property MAY be annotated with integrity information by adding either the digestSRI or digestMultibase property

**R-0230** · §5.3 ¶14 · MAY · split of R-0069
<!-- q L2893-2893 "either of wh" .. "property" -->
> either of which MAY be accompanied by the additionally optional mediaType property

**R-0070** · §5.3 ¶15 · SHOULD NOT
<!-- q L2894-2894 -->
> Any objects for which selective disclosure or unlinkable disclosure is desired SHOULD NOT be included as an object in the relatedResource array.

**R-0071** · §5.3 ¶16 · MUST
<!-- q L2895-2895 "A conforming" .. "esource." -->
> A conforming verifier implementation that makes use of a resource based on the id of a relatedResource object inside a conforming document with a corresponding cryptographic digest appearing in a relatedResource object value MUST compute the digest of the retrieved resource.

**R-0072** · §5.3 ¶16 · MUST
<!-- q L2895-2895 "If the diges" .. "n error." -->
> If the digest provided by the issuer does not match the digest computed for the retrieved resource, the conforming verifier implementation MUST produce an error.

_Inferred, not verbatim: **R-0231** (§5.3 ¶9); its words are this extraction's and its grounds are quoted in requirements.yaml._

**R-0073** · §5.3 ¶17 · SHOULD
<!-- q L2896-2896 "At the time " .. "menters." -->
> At the time of this writing sha384 SHOULD be considered the minimum strength hash algorithm for use by implementers.

## §5.4 Refreshing

**R-0232** · §5.4 ¶2 · keyword-less · from C-0124
<!-- q L2923-2923 "The issuer c" .. "er only." -->
> The issuer can include the refresh service as an element inside the verifiable credential if it is intended for either the verifier or the holder (or both), or inside the verifiable presentation if it is intended for the holder only.

**R-0233** · §5.4 ¶3 · keyword-less · from C-0125
<!-- q L2924-2924 "The refresh " .. "rmation." -->
> The refresh service is only expected to be used when either the credential has expired or the issuer does not publish credential status information.

_R-0074: the skeleton's sentence (lines 2924-2926, MUST first) is split into R-0234, R-0235; its text is in requirements.yaml._

**R-0234** · §5.4 ¶5 (refreshService) · MUST · split of R-0074
<!-- q L2926-2926 "The value of" .. "dential." -->
> The value of the refreshService property MUST be one or more refresh services that provides enough information to the recipient's software such that the recipient can refresh the verifiable credential.

**R-0235** · §5.4 ¶5 (refreshService) · MUST · split of R-0074
<!-- q L2926-2926 "Each refresh" .. "ts type." -->
> Each refreshService value MUST specify its type.

**R-0236** · §5.4 ¶5 (refreshService) · keyword-less · hunted
<!-- q L2926-2926 "The precise " .. "inition." -->
> The precise content of each refresh service is determined by the specific refreshService type definition.

## §5.5 Terms of Use

**R-0237** · §5.5 ¶1 · keyword-less · hunted
<!-- q L2955-2955 "The issuer p" .. "ntation." -->
> The issuer places their terms of use inside the verifiable credential. The holder places their terms of use inside a verifiable presentation.

_R-0075: the skeleton's sentence (lines 2956-2961, MUST first) is split into R-0238; its text is in requirements.yaml._

**R-0238** · §5.5 ¶7 (termsOfUse) · MUST · split of R-0075
<!-- q L2961-2961 "The value of" .. "ntation." -->
> The value of the termsOfUse property MUST specify one or more terms of use policies under which the creator issued the credential or presentation.

_R-0076: the skeleton's sentence (lines 2961, MUST first) is split into R-0239, R-0240; its text is in requirements.yaml._

**R-0239** · §5.5 ¶7 (termsOfUse) · MUST · split of R-0076
<!-- q L2961-2961 "Each termsOf" .. "rkPolicy" -->
> Each termsOfUse value MUST specify its type, for example, TrustFrameworkPolicy

**R-0240** · §5.5 ¶7 (termsOfUse) · MAY · split of R-0076
<!-- q L2961-2961 "MAY specify " .. "tance id" -->
> MAY specify its instance id

**R-0241** · §5.5 ¶7 (termsOfUse) · keyword-less · hunted
<!-- q L2961-2961 "The precise " .. "inition." -->
> The precise contents of each term of use is determined by the specific termsOfUse type definition.

## §5.6 Evidence

_R-0077: the skeleton's sentence (lines 3015-3018, MUST first) is split into R-0242; its text is in requirements.yaml._

**R-0242** · §5.6 ¶4 (evidence) · MUST · split of R-0077
<!-- q L3018-3018 "If present, " .. "objects." -->
> If present, the value of the evidence property MUST be either a single object or a set of one or more objects.

_R-0078: the skeleton's sentence (lines 3018-3020, OPTIONAL first) is split into R-0243, R-0244; its text is in requirements.yaml._

**R-0243** · §5.6 ¶6 (id) · OPTIONAL · split of R-0078
<!-- q L3020-3020 "The id prope" .. "PTIONAL." -->
> The id property is OPTIONAL.

**R-0244** · §5.6 ¶6 (id) · MAY · split of R-0078
<!-- q L3020-3020 "It MAY be us" .. " object." -->
> It MAY be used to provide a unique identifier for the evidence object.

_R-0079: the skeleton's sentence (lines 3020-3022, MUST first) is split into R-0245, R-0246; its text is in requirements.yaml._

**R-0245** · §5.6 ¶6 (id) · MUST · split of R-0079
<!-- q L3020-3020 "If present, " .. "ollowed." -->
> If present, the normative guidance in Section 4.4 Identifiers MUST be followed.

**R-0246** · §5.6 ¶8 (type) · REQUIRED · split of R-0079
<!-- q L3022-3022 "The type pro" .. "EQUIRED." -->
> The type property is REQUIRED.

**R-0080** · §5.6 ¶8 (type) · MUST
<!-- q L3022-3022 "The related " .. "ollowed." -->
> The related normative guidance in Section 4.5 Types MUST be followed.

## §5.7 Zero-Knowledge Proofs

**R-0081** · §5.7 ¶6 · MUST NOT
<!-- q L3081-3081 -->
> Specification authors that create securing mechanisms MUST NOT design them in such a way that they leak information that would enable the verifier to correlate a holder across multiple verifiable presentations to different verifiers.

## §5.8 Representing Time

**R-0082** · §5.8 ¶6 · SHOULD
<!-- q L3169-3169 "In order to " .. " to UTC." -->
> In order to reduce misinterpretations between different time zones, all time values expressed in conforming documents SHOULD be specified in dateTimeStamp format, either in Universal Coordinated Time (UTC), denoted by a Z at the end of the value, or with a time zone offset relative to UTC.

**R-0083** · §5.8 ¶6 · MUST
<!-- q L3169-3169 "Time values " .. " as UTC." -->
> Time values that are incorrectly serialized without an offset MUST be interpreted as UTC.

**R-0247** · §5.8 ¶8 · keyword-less · hunted
<!-- q L3171-3171 "To avoid dou" .. "inition." -->
> To avoid doubt, the regular expression in [XMLSCHEMA11-2] is the normative definition.

## §5.10 Reserved Extension Points

_[definition]_ · §5.10 ¶1 · so the descriptions in the table below describe and do not define
<!-- q L3188-3188 "It is import" .. "ication." -->
> It is important to note that none of these properties are defined by this specification.

_R-0084: the skeleton's sentence (lines 3188-3189, MAY first) is split into R-0248, R-0249; its text is in requirements.yaml._

**R-0248** · §5.10 ¶2 · MAY · split of R-0084
<!-- q L3189-3189 "Implementers" .. "operties" -->
> Implementers MAY use these properties

**R-0249** · §5.10 ¶2 · SHOULD · split of R-0084
<!-- q L3189-3189 "but SHOULD e" .. "ing them" -->
> but SHOULD expect them and/or their meanings to change during the process of normatively specifying them

**R-0085** · §5.10 ¶2 · SHOULD NOT
<!-- q L3189-3189 "Implementers S" .. "ntation." -->
> Implementers SHOULD NOT use these properties without a publicly disclosed specification describing their implementation.

**R-0086** · §5.10 ¶3 · MUST
<!-- q L3190-3190 "In order to " .. "roperty." -->
> In order to avoid collisions regarding how the following properties are used, implementations MUST specify a type property in the value associated with the reserved property.

_[definition]_ · §5.10 ¶5
<!-- q L3192-3192 "confidenceMe" .. "ccurate." -->
> confidenceMethod | A property used for specifying one or more methods that a verifier might use to increase their confidence that the value of a property in or of a verifiable credential or verifiable presentation is accurate.

_R-0087: the skeleton's sentence (lines 3192-3193, MUST first) is split into R-0250; its text is in requirements.yaml._

**R-0250** · §5.10 ¶5 · MUST · split of R-0087
<!-- q L3192-3192 "The associat" .. "eMethod." -->
> The associated vocabulary URL MUST be https://www.w3.org/2018/credentials#confidenceMethod.

_[definition]_ · §5.10 ¶6
<!-- q L3193-3193 "renderMethod" .. " format." -->
> renderMethod | A property used for specifying one or more methods to render a credential into a visual, auditory, haptic, or other format.

**R-0088** · §5.10 ¶6 · MUST
<!-- q L3193-3193 "The associat" .. "rMethod." -->
> The associated vocabulary URL MUST be https://www.w3.org/2018/credentials#renderMethod.

**R-0089** · §5.10 ¶7 · SHOULD
<!-- q L3194-3194 "Items in the" .. "imental." -->
> Items in the directory that refer to reserved extension points SHOULD be treated as experimental.

## §5.11 Ecosystem Compatibility

**R-0251** · §5.11 ¶2 · keyword-less · from C-0144 · the marker quotes the whole line: the text ends on a quotation mark, which an anchor cannot hold, and the line contains it
<!-- q L3199-3199 -->
> If conceptually aligned digital credential formats can be transformed into a conforming document according to the rules provided in this section, they are considered "compatible with the W3C Verifiable Credentials ecosystem". Specification authors are advised to adhere to the following rules when documenting transformations that enable compatibility with the Verifiable Credentials ecosystem. The transformation specification —

**R-0090** · §5.11 ¶2–¶3 · MUST
<!-- q L3199-3200 "The transfor" .. "ippable." -->
> The transformation specification — MUST identify whether the transformation to this data model is one-way-only or round-trippable.

**R-0091** · §5.11 ¶4 · MUST
<!-- q L3201-3201 -->
> MUST preserve the @context values when performing round-trippable transformation.

**R-0092** · §5.11 ¶5 · MUST
<!-- q L3202-3202 -->
> MUST result in a conforming document when transforming to the data model described by this specification.

**R-0093** · §5.11 ¶6 · MUST
<!-- q L3203-3203 -->
> MUST specify a registered media type for the input document.

**R-0094** · §5.11 ¶7 · SHOULD
<!-- q L3204-3204 -->
> SHOULD provide a test suite that demonstrates that the specified transformation algorithm to the data model in this specification results in a conforming document.

**R-0095** · §5.11 ¶8 · SHOULD
<!-- q L3205-3205 "SHOULD ensur" .. "ed Data." -->
> SHOULD ensure that all semantics used in the transformed conforming document follow best practices for Linked Data.

## §5.12 Verifiable Credential Graphs

**R-0252** · §5.12 ¶2 · keyword-less · from C-0148
<!-- q L3212-3212 "For simple v" .. "t graph." -->
> For simple verifiable credentials, that is, when the JSON-LD document contains a single credential with, possibly, associated proofs, this graph is the default graph.

**R-0253** · §5.12 ¶2 · keyword-less · from C-0149
<!-- q L3212-3212 "For presenta" .. "dential." -->
> For presentations, each value associated with the verifiableCredential property of the presentation is a separate named graph of type VerifiableCredentialGraph which contains a single verifiable credential or an enveloped verifiable credential.

**R-0254** · §5.12 ¶3 · keyword-less · from C-0151
<!-- q L3213-3213 "It is import" .. "s a URL." -->
> It is important to not merge objects that seem to have similar properties but do not contain an id property that uses a global identifier, such as a URL.

## §5.13 Securing Mechanism Specifications

**R-0096** · §5.13 ¶2 · MUST
<!-- q L3218-3218 "Securing mec" .. "cuments." -->
> Securing mechanism specifications MUST document normative algorithms that provide content integrity protection for conforming documents.

_R-0097: the skeleton's sentence (lines 3218, MAY first) is split into R-0255, R-0256; its text is in requirements.yaml._

**R-0255** · §5.13 ¶2 · MAY · split of R-0097
<!-- q L3218-3218 "The algorith" .. "n nature" -->
> The algorithms MAY be general in nature

**R-0256** · §5.13 ¶2 · MAY · split of R-0097
<!-- q L3218-3218 "MAY be used " .. "ocuments" -->
> MAY be used to secure data other than conforming documents

**R-0098** · §5.13 ¶3 · MUST
<!-- q L3219-3219 "Securing mec" .. "natures." -->
> Securing mechanism specifications MUST provide a verification algorithm that returns the information in the conforming document that has been secured, in isolation, without including any securing mechanism information, such as proof or JOSE/COSE header parameters and signatures.

**R-0099** · §5.13 ¶3 · MAY
<!-- q L3219-3219 "Verification" .. "chanism." -->
> Verification algorithms MAY return additional information that might be helpful (for example, during validation or for debugging purposes), such as details of the securing mechanism.

**R-0100** · §5.13 ¶3 · MUST
<!-- q L3219-3219 "A verificati" .. "utData)." -->
> A verification algorithm MUST provide an interface that receives a media type (string inputMediaType) and input data (byte sequence or map inputData).

**R-0101** · §5.13 ¶3 · MAY
<!-- q L3219-3219 "Securing mechanism specifications MA" .. "ocument." -->
> Securing mechanism specifications MAY provide algorithms and interfaces in addition to the ones specified in this document.

**R-0257** · §5.13 ¶3–¶9 (string mediaType) · keyword-less · from C-0153
<!-- q L3219-3225 "The verifica" .. "FC6838]." -->
> The verification algorithm returns a verification result with at least the following items: boolean verified A verification status whose value is true if the verification succeeded and false if it did not. map verifiedDocument A document that only contains information that was successfully secured. string mediaType A media type as defined in [RFC6838].

**R-0102** · §5.13 ¶10 · SHOULD
<!-- q L3226-3226 "Securing mec" .. "idation." -->
> Securing mechanism specifications SHOULD provide integrity protection for any information referenced by a URL that is critical to validation.

**R-0103** · §5.13 ¶11 · MUST
<!-- q L3227-3227 "A securing m" .. "f graph." -->
> A securing mechanism specification that creates a new type of embedded proof MUST specify a property that relates the verifiable credential or verifiable presentation to a proof graph.

**R-0104** · §5.13 ¶11–¶12 · MUST
<!-- q L3227-3228 "The requirem" .. "f graph." -->
> The requirements on the securing mechanism are as follow: The securing mechanism MUST define all terms used by the proof graph.

**R-0105** · §5.13 ¶13 · MUST
<!-- q L3229-3229 -->
> The securing mechanism MUST secure all graphs in the verifiable credential or the verifiable presentation, except for any proof graphs securing the verifiable credential or the verifiable presentation itself.

_R-0106: the skeleton's sentence (lines 3231-3232, MAY first) is split into R-0258; its text is in requirements.yaml._

**R-0258** · §5.13 ¶15 · MAY · split of R-0106
<!-- q L3232-3232 -->
> The proof property as defined in [VC-DATA-INTEGRITY] MAY be used by the embedded securing mechanism.

**R-0107** · §5.13 ¶16 · SHOULD
<!-- q L3233-3233 -->
> Securing mechanism specifications SHOULD register the securing mechanism in the Securing Mechanisms section of the Verifiable Credential Extensions document.

## §6 Syntaxes

**R-0259** · §6 ¶1 · keyword-less · from C-0157
<!-- q L3239-3239 "Although syn" .. "tion/vp." -->
> Although syntactic mappings are only provided for JSON-LD, applications and services can use any other data representation syntax (such as XML, YAML, or CBOR) that is capable of being mapped back to application/vc or application/vp.

**R-0260** · §6 ¶1 · keyword-less · from C-0158
<!-- q L3239-3239 "As the verif" .. "parison." -->
> As the verification and validation requirements are defined in terms of the data model, all serialization syntaxes have to be deterministically translated to the data model for processing, validation, or comparison.

**R-0261** · §6 ¶2 · keyword-less · from C-0159
<!-- q L3240-3240 "If present, " .. "Period)." -->
> If present, the following properties are represented as a single value: id (Section 4.4 Identifiers), issuer (Section 4.7 Issuer), and validFrom/validUntil (Section 4.9 Validity Period).

**R-0262** · §6 ¶2 · keyword-less · from C-0160
<!-- q L3240-3240 "All other pr" .. " values." -->
> All other properties, if present, are represented as either a single value or an array of values.

## §6.1 JSON-LD

**R-0263** · §6.1 «Notable JSON-LD Features» ¶2 · keyword-less · hunted
<!-- q L3250-3250 "The @id and " .. "ectively" -->
> The @id and @type keywords are aliased to id and type respectively

**R-0264** · §6.1 «Notable JSON-LD Features» ¶4 · keyword-less · hunted
<!-- q L3252-3252 "The verifiab" .. "ntainer." -->
> The verifiableCredential property is defined as a JSON-LD 1.1 graph container.

**R-0265** · §6.1 «Notable JSON-LD Features» ¶5 · keyword-less · from C-0165
<!-- q L3253-3253 "The @protect" .. "rridden." -->
> The @protected properties feature of JSON-LD 1.1 is used to ensure that terms defined by this specification cannot be overridden.

**R-0108** · §6.1 «Restrictions on JSON-LD» ¶1 · MUST
<!-- q L3257-3257 "JSON-LD comp" .. "ia type." -->
> JSON-LD compacted document form MUST be used for all representations of the data model using the application/vc or application/vp media type.

**R-0266** · §6.1 «Lists and Arrays» ¶2 · keyword-less · from C-0169
<!-- q L3269-3269 -->
> In general, a JSON array is ordered, while a JSON-LD array is not ordered unless that array uses the @list keyword.

## §6.2 Media Types

_R-0109: the skeleton's sentence (lines 3314, SHOULD first) is split into R-0267, R-0268; its text is in requirements.yaml._

**R-0267** · §6.2 ¶2 · SHOULD · split of R-0109
<!-- q L3314-3314 "Syntaxes use" .. "dia type" -->
> Syntaxes used to express the data model in this specification SHOULD be identified by a media type

**R-0268** · §6.2 ¶2 · SHOULD · split of R-0109
<!-- q L3314-3314 "conventions " .. "dentials" -->
> conventions outlined in this section SHOULD be followed when defining or using media types with verifiable credentials

_[definition]_ · §6.2 ¶3
<!-- q L3315-3315 -->
> There are two media types associated with the core data model, which are listed in the Section C. IANA Considerations: application/vc and application/vp.

**R-0269** · §6.2 ¶4 · keyword-less · from C-0173
<!-- q L3316-3316 "The applicat" .. "hanisms." -->
> The application/vc and application/vp media types do not imply any particular securing mechanism, but are intended to be used in conjunction with securing mechanisms.

**R-0270** · §6.2 ¶4 · keyword-less · from C-0174
<!-- q L3316-3316 "A securing m" .. "a types." -->
> A securing mechanism needs to be applied to protect the integrity of these media types.

**R-0271** · §6.2 ¶4 · keyword-less · from C-0175
<!-- q L3316-3316 "Do not assum" .. "cate it." -->
> Do not assume security of content regardless of the media type used to communicate it.

## §7 Algorithms

**R-0272** · §7 ¶1 · keyword-less · hunted
<!-- q L3352-3352 "Conformance " .. "[INFRA]." -->
> Conformance requirements phrased as algorithms use normative concepts from the Infra Standard [INFRA].

## §7.1 Verification

**R-0110** · §7.1 ¶1 · MUST
<!-- q L3358-3358 "This section" .. "ntation." -->
> This section contains an algorithm that conforming verifier implementations MUST run when verifying a verifiable credential or a verifiable presentation.

**R-0273** · §7.1 ¶1–¶8 · keyword-less · from C-0203
<!-- q L3358-3365 "This algorit" .. " errors)" -->
> This algorithm takes a media type (string inputMediaType) and secured data (byte sequence inputData) and returns a map that contains the following: a status (boolean status) a conforming document (map document) a media type (string mediaType) a controller of the verification method associated with the securing mechanism (string controller) a controlled identifier document that is associated with the verification method used to verify the securing mechanism (map controlledIdentifierDocument) zero or more warnings (list of ProblemDetails warnings) zero or more errors (list of ProblemDetails errors)

_Inferred, not verbatim: **R-0280** (§7.1 ¶13 step 1.3); its words are this extraction's and its grounds are quoted in requirements.yaml._

**R-0274** · §7.1 ¶10 step 1 · keyword-less · from C-0203
<!-- q L3367-3367 -->
> Ensure that the securing mechanism has properly protected the conforming document by performing the following steps:

**R-0275** · §7.1 ¶11 step 1.1 · keyword-less · from C-0203
<!-- q L3368-3368 "Set the veri" .. "chanism." -->
> Set the verifyProof function by using the inputMediaType and the Securing Mechanisms section of the Verifiable Credential Extensions document, or other mechanisms known to the implementation, to determine the cryptographic suite to use when verifying the securing mechanism.

**R-0111** · §7.1 ¶11 step 1.1 · MUST
<!-- q L3368-3368 "The verifyPr" .. "cations." -->
> The verifyProof function MUST implement the interface described in 5.13 Securing Mechanism Specifications.

**R-0276** · §7.1 ¶12 step 1.2 · keyword-less · hunted
<!-- q L3369-3369 "If the verif" .. "unction." -->
> If the verifyProof function expects a byte sequence, provide inputMediaType and inputData to the algorithm. If the verifyProof function expects a map, provide inputMediaType and the result of parse JSON bytes to an Infra value given inputData. Set result to the result of the call to the verifyProof function.

**R-0277** · §7.1 ¶12 step 1.2 · keyword-less · from C-0204
<!-- q L3369-3369 "If the call " .. "perties." -->
> If the call was successful, result will contain the status, document, mediaType, controller, controlledIdentifierDocument, warnings, and errors properties.

_Inferred, not verbatim: **R-0278** (§7.1 ¶12 step 1.2); its words are this extraction's and its grounds are quoted in requirements.yaml._

**R-0279** · §7.1 ¶13 step 1.3 · keyword-less · from C-0205
<!-- q L3370-3370 -->
> If result.status is set to false, add a CRYPTOGRAPHIC_SECURITY_ERROR to result.errors.

**R-0281** · §7.1 ¶14 step 2 · keyword-less · from C-0206
<!-- q L3371-3371 "If result.st" .. "ocument." -->
> If result.status is set to true, ensure that result.document is a conforming document.

**R-0282** · §7.1 ¶14 step 2 · keyword-less · hunted
<!-- q L3371-3371 "If it is not" .. ".errors." -->
> If it is not, set result.status to false, remove the document property from result, and add at least one MALFORMED_VALUE_ERROR to result.errors.

**R-0112** · §7.1 ¶14 step 2 · MAY
<!-- q L3371-3371 "Other warnin" .. "process." -->
> Other warnings and errors MAY be included to aid any debugging process.

**R-0283** · §7.1 ¶15 step 3 · keyword-less · hunted
<!-- q L3372-3372 -->
> Return result.

**R-0113** · §7.1 ¶16 · MAY
<!-- q L3373-3373 "The steps fo" .. " inputs." -->
> The steps for verifying the state of the securing mechanism and verifying that the input document is a conforming document MAY be performed in a different order than that provided above as long as the implementation returns errors for the same invalid inputs.

**R-0114** · §7.1 ¶16 · MAY
<!-- q L3373-3373 "Implementati" .. "d above." -->
> Implementations MAY produce different errors than described above.

## §7.2 Problem Details

**R-0284** · §7.2 ¶1 · keyword-less · hunted
<!-- q L3377-3377 "The interfac" .. "he data." -->
> The interface for these objects follow [RFC9457] to encode the data.

_R-0115: the skeleton's sentence (lines 3377-3383, MUST first) is split into R-0285, R-0286, R-0287, R-0288; its text is in requirements.yaml._

**R-0285** · §7.2 ¶3 (type) · MUST · split of R-0115
<!-- q L3379-3379 "The type pro" .. " present" -->
> The type property MUST be present

**R-0286** · §7.2 ¶3 (type) · MUST · split of R-0115
<!-- q L3379-3379 "its value MU" .. "problem." -->
> its value MUST be a URL identifying the type of problem.

**R-0287** · §7.2 ¶5 (title) · SHOULD · split of R-0115
<!-- q L3381-3381 -->
> The title property SHOULD provide a short but specific human-readable string for the problem.

**R-0288** · §7.2 ¶7 (detail) · SHOULD · split of R-0115
<!-- q L3383-3383 -->
> The detail property SHOULD provide a longer human-readable string for the problem.

_[definition]_ · §7.2 ¶8 · lead-in of the problem types; each type is an entry
<!-- q L3384-3384 -->
> The following problem description types are defined by this specification:

**R-0289** · §7.2 ¶9–¶10 (https://www.w3.org/TR/vc-data-model#PARSING_ERROR) · keyword-less · from C-0208
<!-- q L3385-3386 -->
> https://www.w3.org/TR/vc-data-model#PARSING_ERROR There was an error while parsing input.

**R-0290** · §7.2 ¶11–¶12 (https://www.w3.org/TR/vc-data-model#CRYPTOGRAPHIC_SECURITY_ERROR) · keyword-less · from C-0208
<!-- q L3387-3388 "https://www." .. "etected." -->
> https://www.w3.org/TR/vc-data-model#CRYPTOGRAPHIC_SECURITY_ERROR The securing mechanism for the document has detected a modification in the contents of the document since it was created; potential tampering detected.

**R-0291** · §7.2 ¶13–¶14 (https://www.w3.org/TR/vc-data-model#MALFORMED_VALUE_ERROR) · keyword-less · hunted
<!-- q L3389-3390 "https://www." .. "lformed." -->
> https://www.w3.org/TR/vc-data-model#MALFORMED_VALUE_ERROR The value associated with a particular property is malformed.

**R-0116** · §7.2 ¶14 (https://www.w3.org/TR/vc-data-model#MALFORMED_VALUE_ERROR) · SHOULD
<!-- q L3390-3390 "The name of " .. " object." -->
> The name of the property and the path to the property SHOULD be provided in the ProblemDetails object.

**R-0292** · §7.2 ¶15–¶16 (https://www.w3.org/TR/vc-data-model#RANGE_ERROR) · keyword-less · hunted
<!-- q L3391-3392 -->
> https://www.w3.org/TR/vc-data-model#RANGE_ERROR A provided value is outside of the expected range of an associated value, such as a given index value for an array being larger than the current size of the array.

**R-0117** · §7.2 ¶17 · MAY
<!-- q L3393-3393 "Implementati" .. "perties." -->
> Implementations MAY extend the ProblemDetails object by specifying additional types or properties.

## §11.1 Language and Base Direction

**R-0118** · §11.1 ¶4 · MUST · WITHDRAWN: section marked non-normative
<!-- q L3941-3941 "When the lan" .. "N-LD11]." -->
> When the language value object is used in place of a string value, the object MUST contain a @value property whose value is a string, and SHOULD contain a @language property whose value is a string containing a well-formed Language-Tag as defined by [BCP47], and MAY contain a @direction property whose value is a base direction string defined by the @direction property in [JSON-LD11].

**R-0119** · §11.1 ¶4 · MUST NOT · WITHDRAWN: section marked non-normative
<!-- q L3941-3941 "The language" .. "rection." -->
> The language value object MUST NOT include any other keys beyond @value, @language, and @direction.

**R-0120** · §11.1 ¶10–¶11 (example) · MAY · WITHDRAWN: section marked non-normative
<!-- q L3961-3962 -->
> Multiple language value objects MAY be provided as an array value for the property: Example 39: Multiple language texts provided for title

## §11.2 Providing Default Language and Direction

**R-0121** · §11.2 ¶1 · SHOULD · WITHDRAWN: section marked non-normative
<!-- q L4012-4012 "The language" .. "rmation." -->
> The language and base direction of each natural language string property value SHOULD be provided, either via the language value structure for each property value, or via a default language and base direction for all values in the entire credential. Using the per-value language value structure is preferred, because using document defaults can result in a requirement that downstream processors perform JSON-LD expansion-based transformation which is otherwise optional. See the String Internationalization section of the [JSON-LD11] specification for more information.

**R-0122** · §11.2 ¶1 · SHOULD · WITHDRAWN: section marked non-normative · the marker quotes the whole line: the text ends on a quotation mark, which an anchor cannot hold, and the line contains it
<!-- q L4012-4012 -->
> The language and base direction of each natural language string property value SHOULD be provided, either via the language value structure for each property value, or via a default language and base direction for all values in the entire credential. Using the per-value language value structure is preferred, because using document defaults can result in a requirement that downstream processors perform JSON-LD expansion-based transformation which is otherwise optional. See the String Internationalization section of the [JSON-LD11] specification for more information. Natural language string values that do not have a language associated with them SHOULD be treated as if the language value is undefined (language tag "und"). Natural language string values that do not have a base direction associated with them SHOULD be treated as if the direction value is "auto".

**R-0123** · §11.2 ¶1 · SHOULD · WITHDRAWN: section marked non-normative · the marker quotes the whole line: the text ends on a quotation mark, which an anchor cannot hold, and the line contains it
<!-- q L4012-4012 -->
> The language and base direction of each natural language string property value SHOULD be provided, either via the language value structure for each property value, or via a default language and base direction for all values in the entire credential. Using the per-value language value structure is preferred, because using document defaults can result in a requirement that downstream processors perform JSON-LD expansion-based transformation which is otherwise optional. See the String Internationalization section of the [JSON-LD11] specification for more information. Natural language string values that do not have a language associated with them SHOULD be treated as if the language value is undefined (language tag "und"). Natural language string values that do not have a base direction associated with them SHOULD be treated as if the direction value is "auto".

## Appendix B.1 Base Context

**R-0124** · Appendix B.1 ¶1 · MUST
<!-- q L4103-4103 "Implementati" .. "ec92734." -->
> Implementations MUST treat the base context value, located at https://www.w3.org/ns/credentials/v2, as already retrieved; the following value is the hexadecimal encoded SHA2-256 digest value of the base context file: 59955ced6697d61e03f2b2556febe5308ab16842846f5b586d7f1f7adec92734.

_Inferred, not verbatim: **R-0293** (Appendix B.1 ¶1); its words are this extraction's and its grounds are quoted in requirements.yaml._

**R-0294** · Appendix B.1 ¶2 · keyword-less · from C-0340
<!-- q L4104-4104 "Implementati" .. "h value." -->
> Implementations are expected to throw errors if a cryptographic hash value for a resource does not match the expected hash value.

**R-0295** · Appendix B.1 ¶3 · keyword-less · hunted
<!-- q L4105-4105 "Implementati" .. " errors." -->
> Implementations that apply the base context above, as well as other contexts and values in any @context property, during operations such as JSON-LD Expansion or transformation to RDF, are expected to do so without experiencing any errors.

**R-0125** · Appendix B.1 ¶3 · MUST
<!-- q L4105-4105 "If such oper" .. "failure." -->
> If such operations are performed and result in an error, the verifiable credential or verifiable presentation MUST result in a verification failure.

## Appendix B.2 Vocabularies

**R-0126** · Appendix B.2 ¶1 · MUST
<!-- q L4115-4115 "Implementati" .. "rmative." -->
> Implementations that depend on RDF vocabulary processing MUST ensure that the following vocabulary URLs used in the base context ultimately resolve to the following files when loading the JSON-LD serializations, which are normative.

**R-0127** · Appendix B.2 ¶1 · MAY
<!-- q L4115-4115 "Other semant" .. "tations." -->
> Other semantically equivalent serializations of the vocabulary files MAY be used by implementations.

**R-0296** · Appendix B.2 ¶3–¶5 · keyword-less · from C-0344
<!-- q L4117-4119 "URL: https:/" .. "6fc467c4" -->
> URL: https://www.w3.org/2018/credentials# Resolved Document: https://www.w3.org/2018/credentials/index.jsonld SHA2-256 Digest: 9db03c54d69a8ec3944f10770e342b33e58a79045c957c35d51285976fc467c4

**R-0297** · Appendix B.2 ¶6–¶8 · keyword-less · from C-0344
<!-- q L4120-4122 "URL: https:/" .. "a3074104" -->
> URL: https://w3id.org/security# Resolved Document: https://w3c.github.io/vc-data-integrity/vocab/security/vocabulary.jsonld SHA2-256 Digest: 689af6f393b55c9b35c37cfad59d13cc421e0c89ce97cf0e8234f9b4a3074104

_[definition]_ · Appendix B.2 ¶11 · lead-in of the base-class table
<!-- q L4126-4126 -->
> The following base classes are defined in this specification for processors and other specifications that benefit from such definitions:

_[definition]_ · Appendix B.2 ¶12
<!-- q L4127-4127 -->
> | Base Class | Purpose

_[definition]_ · Appendix B.2 ¶13
<!-- q L4128-4128 -->
> | CredentialEvidence | Serves as a superclass for specific evidence types that are placed into the evidence property.

_[definition]_ · Appendix B.2 ¶14
<!-- q L4129-4129 -->
> | CredentialSchema | Serves as a superclass for specific schema types that are placed into the credentialSchema property.

_[definition]_ · Appendix B.2 ¶15
<!-- q L4130-4130 -->
> | CredentialStatus | Serves as a superclass for specific credential status types that are placed into the credentialStatus property.

_[definition]_ · Appendix B.2 ¶16
<!-- q L4131-4131 -->
> | ConfidenceMethod | Serves as a superclass for specific confidence method types that are placed into the confidenceMethod property.

_[definition]_ · Appendix B.2 ¶17 · names the property credentialRefresh, which does not exist: §5.4 defines refreshService (SD-3)
<!-- q L4132-4132 -->
> | RefreshService | Serves as a superclass for specific refresh service types that are placed into the credentialRefresh property.

_[definition]_ · Appendix B.2 ¶18
<!-- q L4133-4133 -->
> | RenderMethod | Serves as a superclass for specific render method types that are placed into the renderMethod property.

_[definition]_ · Appendix B.2 ¶19
<!-- q L4134-4134 -->
> | TermsOfUse | Serves as a superclass for specific terms of use types that are placed into the termsOfUse property.

## Appendix B.3.1 The sriString Datatype

**R-0298** · Appendix B.3.1 ¶1 · keyword-less · from C-0347
<!-- q L4142-4142 "The sriStrin" .. "ication." -->
> The sriString datatype is associated with a value to provide the integrity information for a resource using the method specified in the Subresource Integrity specification.

_[definition]_ · Appendix B.3.1 ¶1
<!-- q L4142-4142 "The sriString datatype is d" .. "follows:" -->
> The sriString datatype is defined as follows:

_[definition]_ · Appendix B.3.1 ¶2–¶3 (The URL denoting this datatype)
<!-- q L4143-4144 -->
> The URL denoting this datatype https://www.w3.org/2018/credentials#sriString

_[definition]_ · Appendix B.3.1 ¶4–¶5 (The lexical space) · SD-13
<!-- q L4145-4146 -->
> The lexical space See the ABNF grammar, defining the integrity attribute in the [SRI] specification, for the restrictions on the string format.

_[definition]_ · Appendix B.3.1 ¶6–¶7 (The value space) · SD-12, SD-13
<!-- q L4147-4148 -->
> The value space A (possibly empty) list of (alg,val) pairs, where alg identifies a hash function, and val is an integer as a standard mathematical concept.

_[definition]_ · Appendix B.3.1 ¶8–¶9 (The lexical-to-value mapping)
<!-- q L4149-4150 -->
> The lexical-to-value mapping Any element of the lexical space is mapped to the value space by following the parse metadata algorithm based on the ABNF grammar in the [SRI] specification.

_[definition]_ · Appendix B.3.1 ¶10–¶11 (The canonical mapping) · SD-12
<!-- q L4151-4152 -->
> The canonical mapping The canonical mapping consists of the lexical-to-value mapping.

## Source defects and tensions

Defects are the source's own errors; tensions are places where two of its statements, or a statement and the context files it ships, cannot both be followed as written; gaps are what an implementer must decide that the source never says. None is healed: every entry it touches keeps the source's words.

### SD-1 (tension) — Keywords in a section marked non-normative, and a normative MUST that points there

<!-- q L3924-3924 -->
> This section is non-normative.

<!-- q L3941-3941 -->
> When the language value object is used in place of a string value, the object MUST contain a @value property whose value is a string, and SHOULD contain a @language property whose value is a string containing a well-formed Language-Tag as defined by [BCP47], and MAY contain a @direction property whose value is a base direction string defined by the @direction property in [JSON-LD11]. The language value object MUST NOT include any other keys beyond @value, @language, and @direction.

<!-- q L922-922 "If present, " .. "rection." -->
> If present, the value of the name property MUST be a string or a language value object as described in 11.1 Language and Base Direction.

§11.1 and §11.2 are subsections of §11, which the source marks non-normative; in the HTML §11 carries class informative and neither subsection overrides it (§11.2 carries class substantive, which is not a normativity class). They nonetheless hold eight BCP 14 keywords (R-0118 to R-0123), and §4.6 lets a name or description value be either a plain string or a language value object, pointing at §11.1 for the latter (R-0162, R-0164). The only rules for that object, what it must contain and that it may contain nothing else, therefore sit where the document says nothing binds. Kept as printed: R-0118 to R-0123 are withdrawn, R-0162 and R-0164 are partial, and R-0165 says what a test can use.

### SD-2 (defect) — §4.2 lists a property named status; §4.10 defines credentialStatus

<!-- q L375-376 -->
> status Defined in Section 4.10 Status.

<!-- q L2271-2271 -->
> This specification defines the credentialStatus property for discovering information related to the status of a verifiable credential, such as whether it is suspended or revoked.

<!-- q L2278-2278 -->
> Example 12: Use of the status property

The credential's property list names status and sends the reader to §4.10, which defines credentialStatus; the HTML's definition term reads status too, and so does Example 12's title (non-normative). The base context (fetched 2026-11-07, sha256 59955ced…, equal to the digest R-0124 prints) defines credentialStatus and no status term at the credential's level. Every requirement here uses credentialStatus (R-0183 and after).

### SD-3 (defect) — Appendix B.2 places refresh service types in a credentialRefresh property

<!-- q L4132-4132 -->
> | RefreshService | Serves as a superclass for specific refresh service types that are placed into the credentialRefresh property.

<!-- q L2922-2922 "This specifi" .. "service." -->
> This specification defines a refreshService property, which enables an issuer to include a link to a refresh service.

The base-class row for RefreshService names credentialRefresh, and the HTML links the word to §5.4, which defines refreshService. The base context defines refreshService and no credentialRefresh.

### SD-4 (defect) — The verification interface §5.13 defines and the result §7.1 reads from it disagree

<!-- q L3219-3219 "The verifica" .. "g items:" -->
> The verification algorithm returns a verification result with at least the following items:

<!-- q L3220-3225 -->
> boolean verified A verification status whose value is true if the verification succeeded and false if it did not. map verifiedDocument A document that only contains information that was successfully secured. string mediaType A media type as defined in [RFC6838].

<!-- q L3368-3368 "The verifyPr" .. "cations." -->
> The verifyProof function MUST implement the interface described in 5.13 Securing Mechanism Specifications.

<!-- q L3369-3369 "If the call " .. "perties." -->
> If the call was successful, result will contain the status, document, mediaType, controller, controlledIdentifierDocument, warnings, and errors properties.

§5.13's interface returns verified, verifiedDocument and mediaType (R-0257), and R-0111 makes §7.1's verifyProof implement it; yet §7.1 reads status and document from its result and expects controller, controlledIdentifierDocument, warnings and errors as well (R-0273, R-0277), none of which §5.13 defines. A verifyProof that follows §5.13 returns nothing under the names §7.1 reads. Kept as printed.

### SD-5 (gap) — No error path for a failed call or an unparseable input; two problem types never used

<!-- q L3369-3369 "If the verifyProof function expects a m" .. "putData." -->
> If the verifyProof function expects a map, provide inputMediaType and the result of parse JSON bytes to an Infra value given inputData.

<!-- q L3385-3386 -->
> https://www.w3.org/TR/vc-data-model#PARSING_ERROR There was an error while parsing input.

<!-- q L3391-3392 -->
> https://www.w3.org/TR/vc-data-model#RANGE_ERROR A provided value is outside of the expected range of an associated value, such as a given index value for an array being larger than the current size of the array.

Step 1.2 says what result holds when the call to verifyProof succeeds and nothing about a call that fails or an inputData that does not parse; step 1.3 then reads result.status regardless. §7.2 defines PARSING_ERROR and RANGE_ERROR and no step of §7.1 uses either. R-0278 records what an implementer must do; RANGE_ERROR has no defined trigger.

### SD-6 (tension) — A conforming document must be secured; the document verification returns cannot be

<!-- q L228-228 "A conforming document MUST be s" .. "hanisms." -->
> A conforming document MUST be secured by at least one securing mechanism as described in Section 4.12 Securing Mechanisms.

<!-- q L3219-3219 "Securing mec" .. "natures." -->
> Securing mechanism specifications MUST provide a verification algorithm that returns the information in the conforming document that has been secured, in isolation, without including any securing mechanism information, such as proof or JOSE/COSE header parameters and signatures.

<!-- q L3371-3371 "If result.st" .. "ocument." -->
> If result.status is set to true, ensure that result.document is a conforming document.

R-0004 makes being secured part of what a conforming document is; R-0098 has a mechanism's verification algorithm return the secured information without any securing information; step 2 of §7.1 then requires that returned document to be a conforming document (R-0281). Read literally, step 2 fails every input. The intended check is presumably every conforming-document requirement but R-0004; the document does not say so, and this extraction does not heal it.

### SD-7 (tension) — Verification includes a status check by definition; the verification algorithm has none

<!-- q L276-276 "This include" .. "ucceeds." -->
> This includes checking that the credential or presentation conforms to the specification, the securing mechanism is satisfied, and, if present, the status check succeeds.

<!-- q L4080-4080 "If the crede" .. "riteria." -->
> If the credentialStatus property is available, the status of a verifiable credential is expected to be evaluated by the verifier according to the credentialStatus type definition for the verifiable credential and the verifier's own status evaluation criteria.

§2 defines verification to include, when present, a successful status check (R-0137). §7.1's algorithm, which R-0110 obliges a verifier to run, has no status step, and Appendix A.8, marked non-normative, treats status as something the verifier evaluates by its own criteria. Whether a verifier that skips credentialStatus performs the verification R-0132 requires is unsettled.

### SD-8 (defect) — §1.3 points verifiers at §4.12 for verification

<!-- q L230-230 "MUST perform" .. "chanisms" -->
> MUST perform verification on a conforming document as described in Section 4.12 Securing Mechanisms

<!-- q L2390-2390 -->
> This specification recognizes two classes of securing mechanisms: those that use enveloping proofs and those that use embedded proofs.

R-0132 sends verifiers to §4.12 for how to verify. §4.12 names the two classes of securing mechanism and recommends one of each; it describes no verification. The procedure is §7.1 (R-0110).

### SD-9 (tension) — dateTimeStamp requires an offset; §5.8 reads offset-less values as UTC

<!-- q L2030-2030 "If present, " .. "ng value" -->
> If present, the value of the validFrom property MUST be a [XMLSCHEMA11-2] dateTimeStamp string value

<!-- q L3169-3169 "Time values " .. " as UTC." -->
> Time values that are incorrectly serialized without an offset MUST be interpreted as UTC.

validFrom and validUntil MUST be XML Schema 1.1 dateTimeStamp values (R-0178, R-0181), a type whose time-zone offset is required, so a value without one makes the document non-conforming, and R-0134 has a verifier produce an error. R-0083 instead requires such a value to be interpreted as UTC, which presupposes processing it. Both cannot be followed for one value.

### SD-10 (tension) — §6's arity rule lets holder and the enveloped types be arrays

<!-- q L3240-3240 "If present, " .. " values." -->
> If present, the following properties are represented as a single value: id (Section 4.4 Identifiers), issuer (Section 4.7 Issuer), and validFrom/validUntil (Section 4.9 Validity Period). All other properties, if present, are represented as either a single value or an array of values.

<!-- q L2477-2477 "If present, " .. "roperty." -->
> If present, the value MUST be either a URL or an object containing an id property.

§6 ¶2 makes id, issuer, validFrom and validUntil single-valued and lets every other property be an array (R-0261, R-0262). holder is not in the list, while R-0045 admits only a URL or an object; and the enveloped objects' type MUST be EnvelopedVerifiableCredential or EnvelopedVerifiablePresentation (R-0212, R-0052), which the rule would let be an array.

### SD-11 (tension) — §5.11 introduces MUST rules as advice

<!-- q L3199-3199 "Specificatio" .. "osystem." -->
> Specification authors are advised to adhere to the following rules when documenting transformations that enable compatibility with the Verifiable Credentials ecosystem.

<!-- q L3200-3200 -->
> MUST identify whether the transformation to this data model is one-way-only or round-trippable.

The sentence introducing §5.11's list says specification authors are advised to follow the rules; each rule opens with MUST or SHOULD (R-0090 to R-0095). The rules are carried at their printed strength.

### SD-12 (defect) — sriString's canonical mapping runs the wrong way

<!-- q L4151-4152 -->
> The canonical mapping The canonical mapping consists of the lexical-to-value mapping.

<!-- q L4147-4148 -->
> The value space A (possibly empty) list of (alg,val) pairs, where alg identifies a hash function, and val is an integer as a standard mathematical concept.

In XML Schema 1.1 Part 2 a datatype's canonical mapping maps the value space to the lexical space; B.3.1 says sriString's canonical mapping consists of its lexical-to-value mapping, the opposite direction. Its value space also makes each digest value an integer, which leaves open how the base64 digest of an SRI expression maps to one. Kept as printed.

### SD-13 (tension) — digestSRI: one or more hash-expressions in §5.3, the whole integrity grammar in B.3.1

<!-- q L2887-2887 "digestSRI | " .. "tribute." -->
> digestSRI | One or more cryptographic digests, as defined by the hash-expression ABNF grammar defined in the Subresource Integrity specification, Section 3.5: The integrity attribute.

<!-- q L4146-4146 -->
> See the ABNF grammar, defining the integrity attribute in the [SRI] specification, for the restrictions on the string format.

<!-- q L4148-4148 "A (possibly " .. "l) pairs" -->
> A (possibly empty) list of (alg,val) pairs

§5.3 defines digestSRI as one or more digests per the SRI hash-expression production (R-0227). The base context types digestSRI as sriString (sha256 59955ced…), whose lexical space B.3.1 gives as the integrity-attribute grammar, which also admits options and the empty string, and whose value space is a possibly empty list. An empty digestSRI therefore meets the letter of R-0067 while carrying no digest.

### SD-14 (tension) — A refresh service in a presentation has no term in the base context

<!-- q L2923-2923 "The issuer c" .. "er only." -->
> The issuer can include the refresh service as an element inside the verifiable credential if it is intended for either the verifier or the holder (or both), or inside the verifiable presentation if it is intended for the holder only.

§5.4 lets the refresh service be placed inside a verifiable presentation (R-0232). The base context defines refreshService only in the VerifiableCredential type's scoped context; the VerifiablePresentation type's scoped context adds only holder, proof, termsOfUse and verifiableCredential to the id and type aliases. A presentation carrying refreshService therefore uses a term the base context does not define, which R-0063 and R-0064 then govern. The sentence also has the issuer place the service inside the presentation, which a holder produces.

### SD-15 (defect) — validUtil for validUntil

<!-- q L3170-3170 "A given veri" .. "e valid." -->
> A given verifiable credential that had a validUtil value of 2024-07-12T12:00:00-07:00, might be re-issued to have a validFrom value of 2024-07-12T12:00:00-08:00, which would create a gap of an hour where the verifiable credential would not be valid.

A misspelt property name in an explanatory sentence of §5.8; it binds nothing.

### SD-16 (defect) — A clause repeated within one sentence (§3.1, non-normative)

<!-- q L300-300 "More informa" .. "e graph." -->
> More information is expected to be added to the graph in order to be able to trust claims, more information is expected to be added to the graph.

The sentence states its clause twice; §3.1 is non-normative.

### SD-17 (gap) — Which of several digests must match is not said

<!-- q L2895-2895 "If the diges" .. "n error." -->
> If the digest provided by the issuer does not match the digest computed for the retrieved resource, the conforming verifier implementation MUST produce an error.

digestSRI and digestMultibase each hold one or more digests (R-0227, R-0228) and an object may carry both; R-0072 speaks of the digest. Whether every listed digest, any one, or the strongest must match is not said.

### SD-18 (tension) — §6.2's SHOULD points at conventions only its non-normative subsection outlines

<!-- q L3314-3314 "conventions " .. "entials." -->
> conventions outlined in this section SHOULD be followed when defining or using media types with verifiable credentials.

<!-- q L3320-3320 -->
> This section is non-normative.

§6.2's normative paragraphs name the two media types and outline no convention; the conventions, how to treat lower-precision media types, are in its subsection Media Type Precision, which is marked non-normative. R-0268 has nothing normative to point at.

### SD-19 (tension) — §2 says the specification requires validation before reliance; nothing normative does

<!-- q L268-268 "It also spec" .. "on them." -->
> It also specifies that verifiers validate claims in verifiable credentials before relying on them.

<!-- q L4017-4017 "While this s" .. "tations," -->
> While this specification does not provide conformance criteria for the process of the validation of verifiable credentials or verifiable presentations,

§2's definition of validation reports that the specification has verifiers validate claims before relying on them (R-0135); no normative statement says so, and Appendix A, marked non-normative, says the specification provides no conformance criteria for validation.

### SD-20 (tension) — Self-asserted is defined twice, by entity and by value

<!-- q L2541-2541 "When the iss" .. "sserted." -->
> When the issuer of a verifiable credential is the holder, the claims in that verifiable credential are considered self-asserted.

<!-- q L2545-2545 -->
> A verifiable credential in a verifiable presentation is considered self-asserted when the value of the issuer property of the verifiable credential is identical to the value of the holder property of the verifiable presentation.

R-0214 defines self-asserted by entity (the issuer is the holder), R-0218 by value (the issuer value is identical to the holder value). They part when one entity uses two identifiers, and identical leaves open whether an issuer object and a holder URL naming the same id are the same value. R-0054 depends on the definition.

### SD-21 (tension) — CRYPTOGRAPHIC_SECURITY_ERROR means a modification; step 1.3 raises it for any failure

<!-- q L3388-3388 "The securing" .. "etected." -->
> The securing mechanism for the document has detected a modification in the contents of the document since it was created; potential tampering detected.

<!-- q L3370-3370 -->
> If result.status is set to false, add a CRYPTOGRAPHIC_SECURITY_ERROR to result.errors.

§7.2 defines the type as a detected modification of the document; step 1.3 adds it whenever verifyProof returns status false, which also covers failures that are not modifications, such as an unknown cryptographic suite or a key that cannot be resolved. R-0114 lets an implementation report other errors.

### SD-22 (tension) — sha384 is the floor for implementers; the document pins SHA2-256

<!-- q L2896-2896 "At the time " .. "menters." -->
> At the time of this writing sha384 SHOULD be considered the minimum strength hash algorithm for use by implementers.

<!-- q L4103-4103 "the followin" .. "xt file:" -->
> the following value is the hexadecimal encoded SHA2-256 digest value of the base context file:

R-0073 sets sha384 as the minimum strength for implementers, while every digest this document pins itself is SHA2-256: the base context's (R-0124) and both vocabulary files' (R-0296, R-0297). The SHOULD sits in §5.3 and is about related-resource digests, so it need not reach Appendix B; the two stand in one document all the same.

### SD-23 (tension) — issuer's object needs a URL id; holder's object only an id

<!-- q L1282-1282 "The value of" .. "is a URL" -->
> The value of the issuer property MUST be either a URL or an object containing an id property whose value is a URL

<!-- q L2477-2477 "If present, " .. "roperty." -->
> If present, the value MUST be either a URL or an object containing an id property.

issuer's object form must have an id whose value is a URL (R-0168); holder's object form need only contain an id (R-0045), though the next sentence, R-0046, speaks of the URL in its id.

### SD-24 (defect) — type values: terms and absolute URL strings

<!-- q L662-662 "The value of" .. "strings." -->
> The value of the type property MUST be one or more terms and absolute URL strings.

Read literally, the conjunction asks every type value to be both a term and an absolute URL string; read as intended, each value is one or the other (R-0150). Example 4 uses terms alone. Kept as printed.

### SD-25 (tension) — The media types are part of conformance; their registrations are non-normative

<!-- q L4167-4167 -->
> This section is non-normative.

<!-- q L4176-4176 "Resources th" .. "type and" -->
> Resources that use the application/vc media type are required to conform to all of the requirements for the application/ld+json media type and

§1.3 makes the two media types part of what a conforming document is (R-0003) and §6.2 lists them, but their registration templates in Appendix C, including the encoding considerations that tie application/vc to the application/ld+json requirements, sit in an appendix marked non-normative.

## Coverage

366 markers, counted by the script that wrote this file: 250 entries of requirements.yaml (every stated entry except the split parents, whose texts are in requirements.yaml), 64 definition, scope and recital blocks, and 52 quotations in the source-defect list. Inferred entries are named where they belong and quoted nowhere: their words are this extraction's.

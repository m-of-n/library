---
record: w3c-vc-data-model-2-0
kind: normative
title: "w3c-vc-data-model-2-0 — normative text"
generated_by: bin/fx1-skeleton
reviewed_by: ""
---

# Normative text

Generated verbatim by `bin/fx1-skeleton`; each quotation carries its
source lines and `bin/check-quotes` verifies it. Pass 1 adds the
keyword-less binding text (tables, IANA rules, lists) as
`<!-- q Lx-y -->` markers and lets `bin/check-quotes --render` write the words.

## §1.3

<!-- q L228-228 -->
> A conforming document is a compacted JSON-LD document that complies with all of the relevant "MUST" statements in this specification.

R-0001

<!-- q L228-228 -->
> Specifically, the relevant normative "MUST" statements in Sections 4. Basic Concepts, 5. Advanced Concepts, and 6. Syntaxes of this document MUST be enforced.

R-0002

<!-- q L228-228 -->
> A conforming document MUST be either a verifiable credential with a media type of application/vc or a verifiable presentation with a media type of application/vp.

R-0003

<!-- q L228-228 -->
> A conforming document MUST be secured by at least one securing mechanism as described in Section 4.12 Securing Mechanisms.

R-0004

<!-- q L229-229 -->
> A conforming issuer implementation produces conforming documents, MUST include all required properties in the conforming documents it produces, and MUST secure the conforming documents it produces using a securing mechanism described in Section 4.12 Securing Mechanisms.

R-0005

<!-- q L230-230 -->
> A conforming verifier implementation consumes conforming documents, MUST perform verification on a conforming document as described in Section 4.12 Securing Mechanisms, MUST check that each required property satisfies the normative requirements for that property, and MUST produce errors when non-conforming documents are detected.

R-0006

<!-- q L231-231 -->
> Optional properties MAY be ignored by conforming issuer implementations and conforming verifier implementations.

R-0007

## §4.3

<!-- q L391-391 -->
> Verifiable credentials and verifiable presentations MUST include a @context property.

R-0008

<!-- q L391-391 -->
> Application developers MUST understand every JSON-LD context used by their application, at least to the extent that it affects the meaning of the terms used by their application.

R-0009

<!-- q L391-393 -->
> Other specifications that build upon this specification MAY require that JSON-LD contexts be integrity protected by using the relatedResource feature described in Section 5.3 Integrity of Related Resources or any effectively equivalent mechanism. @context The value of the @context property MUST be an ordered set where the first item is a URL with the value https://www.w3.org/ns/credentials/v2.

R-0010

<!-- q L393-393 -->
> Subsequent items in the ordered set MUST be composed of any combination of URLs and objects, where each is processable as a JSON-LD Context.

R-0011

## §4.4

<!-- q L423-425 -->
> Publicly resolvable URLs can facilitate ease of verification and interoperability, yet they might also inadvertently grant access to potentially sensitive information if not used judiciously. id The id property is OPTIONAL. If present, id property's value MUST be a single URL, which MAY be dereferenceable.

R-0012

<!-- q L425-425 -->
> It is RECOMMENDED that the URL in the id be one which, if dereferenceable, results in a document containing machine-readable information about the id.

R-0013

## §4.5

<!-- q L660-662 -->
> Verifiable credentials and verifiable presentations MUST contain a type property with an associated value. type The value of the type property MUST be one or more terms and absolute URL strings.

R-0014

<!-- q L883-892 -->
> SHA-256 Hash: DRH5ieldwG5rO2UP5yXbPWXsShQMJlDJR_fQUnhYT3E Disclosure(s): WyJZMVBDaVA3YnJ3TjFHMEVMWmJXRlZRIiwgInR5cGUiLCAiRXhhbXBsZUJhY2hlbG9yRGVncmVlIl0 Contents: [ "Y1PCiP7brwN1G0ELZbWFVQ", "type", "ExampleBachelorDegree" ] Concerning this specification, the following table lists the objects that MUST have a type specified. | Object | Type | Verifiable credential object | VerifiableCredential and, optionally, a more specific verifiable credential type.

R-0015

<!-- q L908-908 -->
> All credentials, presentations, and encapsulated objects SHOULD specify, or be associated with, additional, more narrow types (like ExampleDegreeCredential, for example) so software systems can more easily detect and process this additional information.

R-0016

<!-- q L909-909 -->
> When processing encapsulated objects defined in this specification, such as objects associated with the credentialSubject object or deeply nested therein, software systems SHOULD use the type information specified in encapsulating objects higher in the hierarchy.

R-0017

<!-- q L909-909 -->
> Specifically, an encapsulating object, such as a credential, SHOULD convey the associated object types so that verifiers can quickly determine the contents of an associated object based on the encapsulating object type.

R-0018

## §4.6

<!-- q L920-922 -->
> The name and description properties serve these purposes. name An OPTIONAL property that expresses the name of the credential. If present, the value of the name property MUST be a string or a language value object as described in 11.1 Language and Base Direction.

R-0019

<!-- q L922-924 -->
> Ideally, the name of a credential is concise, human-readable, and could enable an individual to quickly differentiate one credential from any other credentials they might hold. description An OPTIONAL property that conveys specific details about a credential. If present, the value of the description property MUST be a string or a language value object as described in 11.1 Language and Base Direction.

R-0020

## §4.7

<!-- q L1279-1282 -->
> This specification defines a property for expressing the issuer of a verifiable credential. A verifiable credential MUST have an issuer property. issuer The value of the issuer property MUST be either a URL or an object containing an id property whose value is a URL; in either case, the issuer selects this URL to identify itself in a globally unambiguous way.

R-0021

<!-- q L1282-1290 -->
> It is RECOMMENDED that the URL be one which, if dereferenced, results in a controlled identifier document, as defined in the Controlled Identifiers v1.0 specification, about the issuer that can be used to verify the information expressed in the credential. Example 7: Use of the issuer property Credential ecdsa ecdsa-sd bbs jose cose sd-jwt

R-0022

## §4.8

<!-- q L1772-1774 -->
> A verifiable credential MUST contain a credentialSubject property. credentialSubject The value of the credentialSubject property is a set of objects where each object MUST be the subject of one or more claims, which MUST be serialized inside the credentialSubject property.

R-0023

<!-- q L1774-1774 -->
> Each object MAY also contain an id property to identify the subject, as described in Section 4.4 Identifiers.

R-0024

## §4.9

<!-- q L2028-2030 -->
> Temporal comparisons are then performed by checking to see where the date and time being compared are in relation to a particular point on the timeline. validFrom If present, the value of the validFrom property MUST be a [XMLSCHEMA11-2] dateTimeStamp string value representing the date and time the credential becomes valid, which could be a date and time in the future or the past.

R-0025

<!-- q L2030-2032 -->
> If a validUntil value also exists, the validFrom value MUST express a point in time that is temporally the same or earlier than the point in time expressed by the validUntil value. validUntil If present, the value of the validUntil property MUST be a [XMLSCHEMA11-2] dateTimeStamp string value representing the date and time the credential ceases to be valid, which could be a date and time in the past or the future.

R-0026

<!-- q L2032-2032 -->
> If a validFrom value also exists, the validUntil value MUST express a point in time that is temporally the same or later than the point in time expressed by the validFrom value.

R-0027

## §4.10

<!-- q L2272-2274 -->
> The following properties are defined for every object: id The id property is OPTIONAL. It MAY be used to provide a unique identifier for the credential status object.

R-0028

<!-- q L2274-2276 -->
> If present, the normative guidance in Section 4.4 Identifiers MUST be followed. type The type property is REQUIRED.

R-0029

<!-- q L2276-2276 -->
> The related normative guidance in Section 4.5 Types MUST be followed.

R-0030

<!-- q L2341-2341 -->
> Credential status specifications MUST NOT enable tracking of individuals, such as an issuer being notified (either directly or indirectly) when a verifier is interested in a specific holder or subject.

R-0031

## §4.11

<!-- q L2349-2351 -->
> This specification defines the following property for expressing a data schema, which an issuer can include in the verifiable credentials that it issues: credentialSchema The value of the credentialSchema property MUST be one or more data schemas that provide verifiers with enough information to determine whether the provided data conforms to the provided schema(s).

R-0032

<!-- q L2351-2351 -->
> Each credentialSchema MUST specify its type (for example, JsonSchema) and an id property that MUST be a URL identifying the schema file.

R-0033

## §4.12

<!-- q L2391-2391 -->
> One such RECOMMENDED enveloping proof mechanism is defined in Securing Verifiable Credentials using JOSE and COSE [VC-JOSE-COSE].

R-0034

<!-- q L2392-2392 -->
> One such RECOMMENDED embedded proof mechanism is defined in Verifiable Credential Data Integrity 1.0 [VC-DATA-INTEGRITY].

R-0035

## §4.13

<!-- q L2466-2466 -->
> Verifiable presentations MAY be used to aggregate information from multiple verifiable credentials.

R-0036

<!-- q L2467-2467 -->
> Verifiable presentations SHOULD be extremely short-lived and bound to a challenge provided by a verifier.

R-0037

<!-- q L2469-2471 -->
> The following properties are defined for a verifiable presentation: id The id property is optional. It MAY be used to provide a unique identifier for the verifiable presentation.

R-0038

<!-- q L2471-2473 -->
> If present, the normative guidance in Section 4.4 Identifiers MUST be followed. type The type property MUST be present.

R-0039

<!-- q L2473-2473 -->
> One value of this property MUST be VerifiablePresentation, but additional types MAY be included.

R-0040

<!-- q L2473-2475 -->
> The related normative guidance in Section 4.5 Types MUST be followed. verifiableCredential The verifiableCredential property MAY be present.

R-0041

<!-- q L2475-2475 -->
> The value MUST be one or more verifiable credential and/or enveloped verifiable credential objects (the values MUST NOT be non-object values such as numbers, strings, or URLs).

R-0042

<!-- q L2475-2475 -->
> These objects are called verifiable credential graphs and MUST express information that is secured using a securing mechanism.

R-0043

<!-- q L2475-2477 -->
> See Section 5.12 Verifiable Credential Graphs for further details. holder The verifiable presentation MAY include a holder property.

R-0044

<!-- q L2477-2477 -->
> If present, the value MUST be either a URL or an object containing an id property.

R-0045

<!-- q L2477-2477 -->
> It is RECOMMENDED that the URL in the holder or its id be one which, if dereferenced, results in a document containing machine-readable information about the holder that can be used to verify the information expressed in the verifiable presentation.

R-0046

<!-- q L2497-2497 -->
> The @context property of the object MUST be present and include a context, such as the base context for this specification, that defines at least the id, type, and EnvelopedVerifiableCredential terms as defined by the base context provided by this specification.

R-0047

<!-- q L2497-2497 -->
> The id value of the object MUST be a data: URL [RFC2397] that expresses a secured verifiable credential using an enveloping security scheme, such as Securing Verifiable Credentials using JOSE and COSE [VC-JOSE-COSE].

R-0048

<!-- q L2497-2499 -->
> The type value of the object MUST be EnvelopedVerifiableCredential. The example below shows a verifiable presentation that contains an enveloped verifiable credential: Example 18: Basic structure of a presentation

R-0049

<!-- q L2521-2521 -->
> The @context property of the object MUST be present and include a context, such as the base context for this specification, that defines at least the id, type, and EnvelopedVerifiablePresentation terms as defined by the base context provided by this specification.

R-0050

<!-- q L2521-2521 -->
> The id value of the object MUST be a data: URL [RFC2397] that expresses a secured verifiable presentation using an enveloping securing mechanism, such as Securing Verifiable Credentials using JOSE and COSE [VC-JOSE-COSE].

R-0051

<!-- q L2521-2521 -->
> The type value of the object MUST be EnvelopedVerifiablePresentation.

R-0052

<!-- q L2541-2541 -->
> A holder MAY use the verifiableCredential property in a verifiable presentation to include verifiable credentials from any issuer, including themselves.

R-0053

<!-- q L2543-2543 -->
> A verifiable presentation that includes a self-asserted verifiable credential, which is secured only using the same mechanism as the verifiable presentation, MUST include a holder property.

R-0054

## §5.2

<!-- q L2867-2867 -->
> When defining new terms in an application-specific vocabulary, vocabulary authors SHOULD follow the detailed checklist in Best Practices for Publishing Linked Data.

R-0055

<!-- q L2867-2868 -->
> Specifically, the following guidance is of particular importance: Whenever possible, it is RECOMMENDED to re-use terms — and their corresponding URLs — defined by well-known, public vocabularies, such as Schema.org.

R-0056

<!-- q L2869-2869 -->
> New terms MUST define a new URL for each term.

R-0057

<!-- q L2869-2870 -->
> When doing so, the general guidelines for [LINKED-DATA] are expected to be followed, in particular: Human-readable documentation MUST be published, describing the semantics of and the constraints on the use of each term.

R-0058

<!-- q L2871-2872 -->
> It is RECOMMENDED to also publish the collection of all new terms as a machine-readable vocabulary using RDF Schema 1.1. It SHOULD be possible to dereference the URL of a term, resulting in its description and/or formal definition.

R-0059

<!-- q L2873-2873 -->
> Furthermore, a machine-readable description (that is, a JSON-LD Context document) MUST be published at the URL specified in the @context property for the vocabulary.

R-0060

<!-- q L2873-2873 -->
> This context MUST map each term to its corresponding URL, possibly accompanied by further constraints like the type of the property value.

R-0061

<!-- q L2876-2876 -->
> A conforming document SHOULD NOT use the @vocab feature in production as it can lead to JSON term clashes, resulting in semantic ambiguities with other applications.

R-0062

<!-- q L2876-2876 -->
> Instead, to achieve proper interoperability, a conforming document SHOULD use JSON-LD Contexts that define all terms used by their applications, as described earlier in Section 5.2 Extensibility.

R-0063

<!-- q L2876-2876 -->
> If a conforming document does not use JSON-LD Contexts that define all terms used, it MUST include the https://www.w3.org/ns/credentials/undefined-terms/v2 as the last value in the @context property.

R-0064

## §5.3

<!-- q L2881-2885 -->
> To extend integrity protection to a related resource, an issuer of a verifiable credential MAY include the relatedResource property: relatedResource The value of the relatedResource property MUST be one or more objects of the following form: | Property | Description | id | The identifier for the resource is REQUIRED and conforms to the format defined in Section 4.4 Identifiers.

R-0065

<!-- q L2885-2888 -->
> The value MUST be unique among the list of related resource objects. | mediaType | An OPTIONAL valid media type as listed in the IANA Media Types registry. | digestSRI | One or more cryptographic digests, as defined by the hash-expression ABNF grammar defined in the Subresource Integrity specification, Section 3.5: The integrity attribute. | digestMultibase | One or more cryptographic digests, as defined by the digestMultibase property in the Verifiable Credential Data Integrity 1.0 specification, Section 2.6: Resource Integrity.

R-0066

<!-- q L2889-2889 -->
> Each object associated with relatedResource MUST contain at least a digestSRI or a digestMultibase value.

R-0067

<!-- q L2890-2892 -->
> If a mediaType is listed, implementations that retrieve the resource identified by the id property using HTTP Semantics SHOULD: use the media type in the Accept HTTP Header, and reject the response if it includes a Content-Type HTTP Header with a different media type.

R-0068

<!-- q L2893-2893 -->
> Any object in the verifiable credential that contains an id property MAY be annotated with integrity information by adding either the digestSRI or digestMultibase property, either of which MAY be accompanied by the additionally optional mediaType property.

R-0069

<!-- q L2894-2894 -->
> Any objects for which selective disclosure or unlinkable disclosure is desired SHOULD NOT be included as an object in the relatedResource array.

R-0070

<!-- q L2895-2895 -->
> A conforming verifier implementation that makes use of a resource based on the id of a relatedResource object inside a conforming document with a corresponding cryptographic digest appearing in a relatedResource object value MUST compute the digest of the retrieved resource.

R-0071

<!-- q L2895-2895 -->
> If the digest provided by the issuer does not match the digest computed for the retrieved resource, the conforming verifier implementation MUST produce an error.

R-0072

<!-- q L2896-2896 -->
> At the time of this writing sha384 SHOULD be considered the minimum strength hash algorithm for use by implementers.

R-0073

## §5.4

<!-- q L2924-2926 -->
> Issuers are advised not to put the refreshService property in a verifiable credential that does not contain public information or whose refresh service is not protected in some way. refreshService The value of the refreshService property MUST be one or more refresh services that provides enough information to the recipient's software such that the recipient can refresh the verifiable credential. Each refreshService value MUST specify its type.

R-0074

## §5.5

<!-- q L2956-2961 -->
> The value of the termsOfUse property might be used to tell the verifier any or all of the following, among other things: the procedures or policies that were used in issuing the verifiable credential, by providing, for example, a pointer to a public location (to avoid "phone home" privacy issues) where these procedures or policies can be found, or the name of the standard that defines them the rules and policies of the issuer that apply to the presentation of this verifiable credential to a verifier, by providing, for example, a pointer to a public location (to avoid "phone home" privacy issues) where these rules or policies can be found the identity of the entity under whose authority the issuer issued this particular verifiable credential termsOfUse The value of the termsOfUse property MUST specify one or more terms of use policies under which the creator issued the credential or presentation.

R-0075

<!-- q L2961-2961 -->
> Each termsOfUse value MUST specify its type, for example, TrustFrameworkPolicy, and MAY specify its instance id.

R-0076

## §5.6

<!-- q L3015-3018 -->
> Evidence can be included by an issuer to provide the verifier with additional supporting information in a verifiable credential. This could be used by the verifier to establish the confidence with which it relies on the claims in the verifiable credential. For example, an issuer could check physical documentation provided by the subject or perform a set of background checks before issuing the credential. In certain scenarios, this information is useful to the verifier when determining the risk associated with relying on a given credential. This specification defines the evidence property for expressing evidence information. evidence If present, the value of the evidence property MUST be either a single object or a set of one or more objects.

R-0077

<!-- q L3018-3020 -->
> The following properties are defined for every evidence object: id The id property is OPTIONAL. It MAY be used to provide a unique identifier for the evidence object.

R-0078

<!-- q L3020-3022 -->
> If present, the normative guidance in Section 4.4 Identifiers MUST be followed. type The type property is REQUIRED.

R-0079

<!-- q L3022-3022 -->
> The related normative guidance in Section 4.5 Types MUST be followed.

R-0080

## §5.7

<!-- q L3081-3081 -->
> Specification authors that create securing mechanisms MUST NOT design them in such a way that they leak information that would enable the verifier to correlate a holder across multiple verifiable presentations to different verifiers.

R-0081

## §5.8

<!-- q L3169-3169 -->
> In order to reduce misinterpretations between different time zones, all time values expressed in conforming documents SHOULD be specified in dateTimeStamp format, either in Universal Coordinated Time (UTC), denoted by a Z at the end of the value, or with a time zone offset relative to UTC.

R-0082

<!-- q L3169-3169 -->
> Time values that are incorrectly serialized without an offset MUST be interpreted as UTC.

R-0083

## §5.10

<!-- q L3188-3189 -->
> Consequently, implementers are cautioned that use of these properties is considered experimental. Implementers MAY use these properties, but SHOULD expect them and/or their meanings to change during the process of normatively specifying them.

R-0084

<!-- q L3189-3189 -->
> Implementers SHOULD NOT use these properties without a publicly disclosed specification describing their implementation.

R-0085

<!-- q L3190-3190 -->
> In order to avoid collisions regarding how the following properties are used, implementations MUST specify a type property in the value associated with the reserved property.

R-0086

<!-- q L3192-3193 -->
> The associated vocabulary URL MUST be https://www.w3.org/2018/credentials#confidenceMethod. | renderMethod | A property used for specifying one or more methods to render a credential into a visual, auditory, haptic, or other format.

R-0087

<!-- q L3193-3193 -->
> The associated vocabulary URL MUST be https://www.w3.org/2018/credentials#renderMethod.

R-0088

<!-- q L3194-3194 -->
> Items in the directory that refer to reserved extension points SHOULD be treated as experimental.

R-0089

## §5.11

<!-- q L3199-3200 -->
> The transformation specification — MUST identify whether the transformation to this data model is one-way-only or round-trippable.

R-0090

<!-- q L3201-3201 -->
> MUST preserve the @context values when performing round-trippable transformation.

R-0091

<!-- q L3202-3202 -->
> MUST result in a conforming document when transforming to the data model described by this specification.

R-0092

<!-- q L3203-3203 -->
> MUST specify a registered media type for the input document.

R-0093

<!-- q L3204-3204 -->
> SHOULD provide a test suite that demonstrates that the specified transformation algorithm to the data model in this specification results in a conforming document.

R-0094

<!-- q L3205-3205 -->
> SHOULD ensure that all semantics used in the transformed conforming document follow best practices for Linked Data.

R-0095

## §5.13

<!-- q L3218-3218 -->
> Securing mechanism specifications MUST document normative algorithms that provide content integrity protection for conforming documents.

R-0096

<!-- q L3218-3218 -->
> The algorithms MAY be general in nature and MAY be used to secure data other than conforming documents.

R-0097

<!-- q L3219-3219 -->
> Securing mechanism specifications MUST provide a verification algorithm that returns the information in the conforming document that has been secured, in isolation, without including any securing mechanism information, such as proof or JOSE/COSE header parameters and signatures.

R-0098

<!-- q L3219-3219 -->
> Verification algorithms MAY return additional information that might be helpful (for example, during validation or for debugging purposes), such as details of the securing mechanism.

R-0099

<!-- q L3219-3219 -->
> A verification algorithm MUST provide an interface that receives a media type (string inputMediaType) and input data (byte sequence or map inputData).

R-0100

<!-- q L3219-3219 -->
> Securing mechanism specifications MAY provide algorithms and interfaces in addition to the ones specified in this document.

R-0101

<!-- q L3226-3226 -->
> Securing mechanism specifications SHOULD provide integrity protection for any information referenced by a URL that is critical to validation.

R-0102

<!-- q L3227-3227 -->
> A securing mechanism specification that creates a new type of embedded proof MUST specify a property that relates the verifiable credential or verifiable presentation to a proof graph.

R-0103

<!-- q L3227-3228 -->
> The requirements on the securing mechanism are as follow: The securing mechanism MUST define all terms used by the proof graph.

R-0104

<!-- q L3229-3229 -->
> The securing mechanism MUST secure all graphs in the verifiable credential or the verifiable presentation, except for any proof graphs securing the verifiable credential or the verifiable presentation itself.

R-0105

<!-- q L3231-3232 -->
> See also Figure 9 or Figure 14. The proof property as defined in [VC-DATA-INTEGRITY] MAY be used by the embedded securing mechanism.

R-0106

<!-- q L3233-3233 -->
> Securing mechanism specifications SHOULD register the securing mechanism in the Securing Mechanisms section of the Verifiable Credential Extensions document.

R-0107

## §6.1

<!-- q L3257-3257 -->
> JSON-LD compacted document form MUST be used for all representations of the data model using the application/vc or application/vp media type.

R-0108

## §6.2

<!-- q L3314-3314 -->
> Syntaxes used to express the data model in this specification SHOULD be identified by a media type, and conventions outlined in this section SHOULD be followed when defining or using media types with verifiable credentials.

R-0109

## §7.1

<!-- q L3358-3358 -->
> This section contains an algorithm that conforming verifier implementations MUST run when verifying a verifiable credential or a verifiable presentation.

R-0110

<!-- q L3368-3368 -->
> The verifyProof function MUST implement the interface described in 5.13 Securing Mechanism Specifications.

R-0111

<!-- q L3371-3371 -->
> Other warnings and errors MAY be included to aid any debugging process.

R-0112

<!-- q L3373-3373 -->
> The steps for verifying the state of the securing mechanism and verifying that the input document is a conforming document MAY be performed in a different order than that provided above as long as the implementation returns errors for the same invalid inputs.

R-0113

<!-- q L3373-3373 -->
> Implementations MAY produce different errors than described above.

R-0114

## §7.2

<!-- q L3377-3383 -->
> A ProblemDetails object consists of the following properties: type The type property MUST be present and its value MUST be a URL identifying the type of problem. title The title property SHOULD provide a short but specific human-readable string for the problem. detail The detail property SHOULD provide a longer human-readable string for the problem.

R-0115

<!-- q L3390-3390 -->
> The name of the property and the path to the property SHOULD be provided in the ProblemDetails object.

R-0116

<!-- q L3393-3393 -->
> Implementations MAY extend the ProblemDetails object by specifying additional types or properties.

R-0117

## §11.1

<!-- q L3941-3941 -->
> When the language value object is used in place of a string value, the object MUST contain a @value property whose value is a string, and SHOULD contain a @language property whose value is a string containing a well-formed Language-Tag as defined by [BCP47], and MAY contain a @direction property whose value is a base direction string defined by the @direction property in [JSON-LD11].

R-0118

<!-- q L3941-3941 -->
> The language value object MUST NOT include any other keys beyond @value, @language, and @direction.

R-0119

<!-- q L3961-3962 -->
> Multiple language value objects MAY be provided as an array value for the property: Example 39: Multiple language texts provided for title

R-0120

## §11.2

<!-- q L4012-4012 -->
> The language and base direction of each natural language string property value SHOULD be provided, either via the language value structure for each property value, or via a default language and base direction for all values in the entire credential. Using the per-value language value structure is preferred, because using document defaults can result in a requirement that downstream processors perform JSON-LD expansion-based transformation which is otherwise optional. See the String Internationalization section of the [JSON-LD11] specification for more information.

R-0121

<!-- q L4012-4012 -->
> Natural language string values that do not have a language associated with them SHOULD be treated as if the language value is undefined (language tag "und").

R-0122

<!-- q L4012-4012 -->
> Natural language string values that do not have a base direction associated with them SHOULD be treated as if the direction value is "auto".

R-0123

## Appendix B.1

<!-- q L4103-4103 -->
> Implementations MUST treat the base context value, located at https://www.w3.org/ns/credentials/v2, as already retrieved; the following value is the hexadecimal encoded SHA2-256 digest value of the base context file: 59955ced6697d61e03f2b2556febe5308ab16842846f5b586d7f1f7adec92734.

R-0124

<!-- q L4105-4105 -->
> If such operations are performed and result in an error, the verifiable credential or verifiable presentation MUST result in a verification failure.

R-0125

## Appendix B.2

<!-- q L4115-4115 -->
> Implementations that depend on RDF vocabulary processing MUST ensure that the following vocabulary URLs used in the base context ultimately resolve to the following files when loading the JSON-LD serializations, which are normative.

R-0126

<!-- q L4115-4115 -->
> Other semantically equivalent serializations of the vocabulary files MAY be used by implementations.

R-0127


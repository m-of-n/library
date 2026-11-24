---
record: draft-ietf-spki-cert-structure
kind: normative
title: "draft-ietf-spki-cert-structure — normative text"
generated_by: bin/fx1-skeleton
reviewed_by: ""
---

# Normative text

The binding text of draft-ietf-spki-cert-structure-06, section by section,
verbatim. Each quotation is a `<!-- q Lx-y -->` marker whose words
`bin/check-quotes --render` wrote from `.cache/draft-ietf-spki-cert-structure.txt`
(the heading-normalised rendering named in `requirements.yaml`
`source_rendering`); the line under each quotation names the requirements of
this record that carry it. Nothing here was typed.

The draft has no capitalised BCP 14 keyword (`bin/bcp14-count`: 0); its
obligations are lowercase. `requirements.yaml` `lowercase_modals` gives the
treatment: every binding sentence is extracted whatever its modal, the
lowercase word and its sense are recorded beside it, and neither RFC 2119 nor
RFC 8174 force is assigned.

A quotation that crosses a page break contains the running header's words,
because `bin/_source_text` does not remove an Internet-Draft header (see
Extraction notes). Productions are quoted one per marker; §9.2 is reproduced in
full, each production naming the entry that carries it (a production identical
to one in a section is carried by that section's entry). Inferred requirements
are our words and are not quoted here; they are in `requirements.yaml` with
`kind: inferred`. Examples and test vectors are not repeated here except where a
requirement quotes them; they are fixtures in `examples/`.

## Abstract

<!-- q L101-105 "The authorization" .. "the implementer." -->
> The authorization field carried by SPKI certificates and ACLs is left to be defined, to suit each particular application or protocol. SPKI defines rules for combination of authorization fields, constraining the construction of these, but leaves specific details up to the implementer.

R-0001

<!-- q L108-111 -->
> The process of reducing SPKI sequences and an ACL to determine an authorization result is spelled out here, but an individual implementer is free to design new reduction algorithms as long as they are computationally equivalent to the one defined here.

R-0002

## §2

<!-- q L352-357 "ACL: an" .. "implicit issuer)." -->
> ACL: an Access Control List: a list of entries that anchors a certificate chain. Sometimes called a "list of root keys", the ACL is the source of empowerment for certificates. That is, a certificate communicates power from its issuer to its subject, but the ACL is the source that power (since it theoretically has the owner of the resource being controlled as its implicit issuer).

R-0438

<!-- q L357-359 "An ACL" .. "not signed)." -->
> An ACL entry has potentially the same content as a certificate body, but has no Issuer (and is not signed).

R-0003

<!-- q L362-363 "CERTIFICATE: a" .. "a Subject." -->
> CERTIFICATE: a signed instrument that empowers the Subject. It contains at least an Issuer and a Subject.

R-0004

<!-- q L364-367 "Certificates come" .. "(mapping <authorization,key>)." -->
> Certificates come in three categories: ID (mapping <name,key>), Attribute (mapping <authorization,name>), and Authorization (mapping <authorization,key>).

R-0439

<!-- q L367-369 "An SPKI" .. "that empowerment." -->
> An SPKI authorization or attribute certificate can pass along all the empowerment it has received from the Issuer or it can pass along only a portion of that empowerment.

R-0005

<!-- q L371-372 -->
> CANONICAL S-EXPRESSION: an encoding of an S-expression that does not permit equivalent representations and is designed for easy parsing.

R-0006

<!-- q L374-375 -->
> FULLY QUALIFIED NAME: a local name together with a global identifier defining the name space in which that local name is defined.

R-0007

<!-- q L377-379 -->
> GLOBAL IDENTIFIER: a globally unique byte string, associated with the keyholder. In SPKI this is the public key itself, a collision-free hash of the public key or a Fully Qualified Name.

R-0008

<!-- q L381-384 -->
> HASH: a cryptographically strong hash function, assumed to be collision resistant. In general, the hash of an object can be used wherever the object can appear. The hash serves as a name for the object from which it was computed.

R-0009 (split R-0010, R-0011)

<!-- q L386-387 -->
> ISSUER: the signer of a certificate and the source of empowerment that the certificate is communicating to the Subject.

R-0012

<!-- q L389-392 -->
> KEYHOLDER: the person or other entity that owns and controls a given private key. This entity is said to be the keyholder of the keypair or just the public key, but control of the private key is assumed in all cases.

R-0440

<!-- q L394 -->
> NAME: a SDSI name always relative to the definer of some name space.

R-0013

<!-- q L395-404 "This is" .. "name space." -->
> This is sometimes also referred to as a local name. A global (fully qualified) name includes the global identifier of the definer of the INTERNET-DRAFT Simple Public Key Certificate 26 July 1999 name space.

R-0441

<!-- q L410-414 -->
> ONLINE TEST: one of three forms of validity test: (1) CRL; (2) revalidation; or (3) one-time revalidation. Each refines the date range during which a given certificate or ACL entry is considered valid, although the last defines a validity interval of effectively zero length.

R-0014 (split R-0015)

<!-- q L416-417 "PRINCIPAL: a" .. "digital signature." -->
> PRINCIPAL: a cryptographic key, capable of generating a digital signature.

R-0442

<!-- q L420-423 -->
> PROVER: the entity that wishes access or that digitally signs a document. The Prover typically sends a message or opens a channel to the Verifier that then checks signatures and credentials sent by the Prover.

R-0016

<!-- q L425-427 -->
> SPEAKING: A Principal is said to "speak" by means of a digital signature. The statement made is the signed object (often a certificate). The Principal is said to "speak for" the Keyholder.

R-0443

<!-- q L429 "SUBJECT: the" .. "ACL entry." -->
> SUBJECT: the thing empowered by a certificate or ACL entry.

R-0444

<!-- q L434 "S-EXPRESSION: the" .. "for SPKI/SDSI." -->
> S-EXPRESSION: the data format chosen for SPKI/SDSI.

R-0445

<!-- q L434-437 "This is" .. "the expression." -->
> This is a LISP-like parenthesized expression with the limitations that empty lists are not allowed and the first element in any S-expression must be a string, called the "type" of the expression.

R-0017 (split R-0018, R-0019)

<!-- q L439-440 "THRESHOLD SUBJECT:" .. "other Subjects." -->
> THRESHOLD SUBJECT: a Subject for an ACL entry or certificate that specifies K of N other Subjects.

R-0446

<!-- q L440-444 "Conceptually, the" .. "passed along." -->
> Conceptually, the power being transmitted to the Subject by the ACL entry or certificate is transmitted in (1/K) amount to each listed subordinate Subject. K of those subordinate Subjects must agree (by delegating their shares along to the same object or key) for that power to be passed along.

R-0020, R-0021

<!-- q L448 -->
> TUPLE: The security-relevant fields from a certificate or ACL entry.

R-0447

<!-- q L449-453 -->
> We speak of 4-tuples for name certificates and 5-tuples for authorizations. The 4-tuple has fields: <Issuer, Name, Subject, Validity> while the 5-tuple has fields: <Issuer, Subject, Delegation, Authorization, Validity>.

R-0022

<!-- q L461-463 -->
> VALIDITY CONDITIONS: a date range that must include the current date and time and/or a set of online tests that must succeed before a certificate is to be considered valid.

R-0023 (split R-0024, R-0025)

<!-- q L465-466 "VERIFIER: the" .. "including certificates." -->
> VERIFIER: the entity that processes requests from a prover, including certificates.

R-0448

<!-- q L466-469 "The verifier" .. "prover: <self,prover,D,A,V>." -->
> The verifier uses its own ACL entries plus certificates provided by the prover to perform "5-tuple reduction", to arrive at a 5-tuple it believes about the prover: <self,prover,D,A,V>.

R-0026

## §3

<!-- q L520-526 "We have chosen" .. "a byte-string." -->
> We have chosen a simplified form of S-expression (the canonical form) as the format for SPKI objects. An S-expression is a list enclosed in matching "(" and ")". We assume the S-expression technology of [SEXP] with the restrictions that no empty lists are allowed and that each list must have a byte string as its first element. That first element is the "type" or "name" of the object represented by the list and must be a byte-string.

R-0449; R-0027 (split R-0028, R-0029), R-0030

<!-- q L528-532 "SPKI objects" .. "those characters." -->
> SPKI objects are defined below in a familiar extension of BNF -- with "|" meaning logical OR, "*" meaning closure (0 or more occurrences), "?" meaning optional (0 or 1 occurrence) and "+" meaning non-empty closure (1 or more occurrences). A quoted string represents those characters.

R-0031

<!-- q L535-536 -->
> For the sake of readability, all examples and the BNF in this document deal with advanced rather than canonical S-expressions.

R-0032

<!-- q L537-539 "That is," .. "double-quoted ASCII." -->
> That is, single word strings that start with alphabetic characters are used without quotes and strings can be in hex, base64 or double-quoted ASCII.

R-0033

## §3.1

<!-- q L545-548 -->
> All SPKI structures communicated from one machine to another must be in canonical form. If canonical S-expressions need to be transmitted over a 7-bit channel, there is a form defined for base64 encoding them.

R-0034, R-0035

<!-- q L550-555 -->
> A canonical S-expression is formed from binary byte strings, each prefixed by its length, plus the punctuation characters "()[]". The length of a byte string is a non-negative ASCII decimal number, with no unnecessary leading "0" digits, terminated by ":". The canonical form is a unique representation of an S-expression and is used as the input to all hash and signature functions.

R-0036, R-0037, R-0038 (split R-0039, R-0040)

## §3.2

<!-- q L561-562 -->
> A byte-string is a sequence of binary bytes (octets), optionally modified by a display type.

R-0041

<!-- q L564-566 -->
> All byte strings carry explicit lengths and are therefore not 0-terminated as in the C language. They are treated as binary even when they are ASCII, and can use any character set encoding desired.

R-0042, R-0043

<!-- q L577-579 "A display" .. "byte string." -->
> A display type is assumed to be a MIME type giving optional instructions to any program wishing to display or use the byte string.

R-0044

<!-- q L581-585 "Although the" .. "display types." -->
> Although the display type of a byte string is optional, it is considered part of the string for any equality comparisons or hashing. That is, two strings with the same bytes will not be considered equal (or otherwise comparable) if they have unequal display types.

R-0045, R-0046

<!-- q L589 -->
> <byte-string>:: <bytes> | <display-type> <bytes> ;

R-0047

<!-- q L590 -->
> <bytes>:: <decimal> ":" {binary byte string of that length} ;

R-0048

<!-- q L591 -->
> <decimal>:: <nzddigit> <ddigit>* | "0" ;

R-0049

<!-- q L592 -->
> <nzddigit>:: "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" ;

R-0050

<!-- q L593 -->
> <ddigit>:: "0" | <nzddigit> ;

R-0051

<!-- q L594 -->
> <display-type>:: "[" <bytes> "]" ;

R-0052

## §3.2.1

<!-- q L600-605 "An integer" .. "multi-precision libraries." -->
> An integer is a kind of byte-string, <integer>:: <byte-string> ; that we distinguish only because it is encoded in the way expected by multi-precision libraries.

R-0053

<!-- q L602 -->
> <integer>:: <byte-string> ;

R-0054

<!-- q L605-607 "We assume" .. "or DSA)." -->
> We assume those libraries deal only with signed multi-precision integers, even if they are known to be positive (e.g., a modulus for RSA or DSA).

R-0055

<!-- q L609-612 -->
> The bytes of a binary integer are twos-complement, in network standard order (most significant byte first). On the assumption that they are signed, a leading 0x00 or 0xFF byte may need to be present, but redundant bytes of sign need not be.

R-0056, R-0057

<!-- q L614-615 -->
> The integer value 0 is expressed as a 1-byte string holding the 0 byte, not as the empty string "".

R-0058

## §3.3

<!-- q L623 -->
> <s-expr>:: "(" <byte-string> <s-part>* ")" ;

R-0059

<!-- q L624 -->
> <s-part>:: <byte-string> | <s-expr> ;

R-0060

## §3.4

<!-- q L644-650 -->
> The advanced text form is: (test abcdefghijklmnopqrstuvwxyz "12345" ":: ::") showing that the advanced form follows familiar token recognition rules, not permitting tokens to start with digits, terminating them with white space or punctuation marks.

R-0061 (split R-0062)

<!-- q L652-654 -->
> For transmission of true 8-bit forms, we permit base64 encodings according to [RFC2045], with the base64 characters enclosed in braces "{}". The example above encodes to:

R-0063

## §3.5

<!-- q L675-676 "The canonical" .. "verifying signatures." -->
> The canonical S-expression is the form which is hashed for both generating and verifying signatures.

R-0064

## §3.6

<!-- q L698-704 "In the" .. "canonical form." -->
> In the advanced form, individual byte strings may be expressed without length fields (if they are what most languages consider text tokens), may be written as quoted strings (under normal C string rules), or may be individually hex or base64 encoded. Also in the advanced form, white space between list elements is allowed for readability and ignored on conversion to canonical form.

R-0065 (split R-0066, R-0067, R-0068), R-0069

<!-- q L711-715 "In these" .. "canonical form." -->
> In these examples, we will use keywords without preceding length fields, quoted strings, hex values (delimited by "#") and base64 values (delimited by "|"). Those are features of the advanced transport form of an S-expression, and are not part of the canonical form.

R-0070, R-0071

## §3.7

<!-- q L724-727 "<tag> objects" .. "she wishes." -->
> <tag> objects are user-defined, using a language for describing sets of permissions given here, and in the process, the defining user can choose any object names he or she wishes.

R-0072

<!-- q L729-730 -->
> For the definition of new algorithm names, it is our preference that this be taken on by IANA [RFC1780] for single-word standard names.

R-0073

<!-- q L731-733 -->
> In the interest of maximum flexibility we also permit users to define their own algorithm names via a normal URIs (which presumably point to descriptions of the algorithms or even to code).

R-0074

## §3.8

<!-- q L748-750 "The objects" .. "object name." -->
> The objects defined in SPKI/SDSI 2.0 are S-expressions. That is they are lists of either byte strings or other lists. In our case, all S-expressions start with a <byte-string>, called the object name.

R-0075

<!-- q L750-751 "The remaining" .. "the object." -->
> The remaining elements of the list are called "parts" of the object.

R-0450

<!-- q L755-756 "The verifier" .. "own <acl>." -->
> The verifier will also need to refer to its own <acl>.

R-0076

<!-- q L756-757 "These are" .. "immediately following" -->
> These are considered top level objects and are defined in the sections immediately following

R-0460

<!-- q L759-765 -->
> It is standard SPKI/SDSI practice to use names starting with a lower case letter, followed by lower case letters, digits and hyphens for object types. SPKI/SDSI is case-sensitive, so the byte-string "RSA" is not the same as "rsa". Non-standard object types (i.e. <tag>s defined by an application developer) are unconstrained, may have display types and may even be URIs pointing to documentation of the object type.

R-0077, R-0078, R-0079

<!-- q L767-773 -->
> The structure and interpretation of the parts is up to the designer of the top-level object type. However, for the sake of simplification, we have decided that all objects are "positional". That is, their parts are listed in some fixed order with meaning of the part depending on its position. Parts can be omitted only by omitting a contiguous set of trailing parts. Exceptions to this are found in the top level <cert> and <acl> constructs.

R-0080, R-0081, R-0082, R-0083

<!-- q L776-781 "Note that" .. "order given." -->
> Note that the main object, <cert>, is sub-type based so the parameter fields may be in any order, but the BNF suggests a fixed order. We use the BNF definition to indicate that there may not be more than one of each of the listed fields, and also to suggest (for readability) that the certificate parts be presented in the order given.

R-0084 (split R-0085, R-0086), R-0087 (split R-0088, R-0089)

## §3.8.1

<!-- q L788-789 -->
> <pub-key>:: "(" "public-key" "(" <pub-sig-alg-id> <s-expr>* ")" <uris>? ")" ;

R-0090

<!-- q L791-793 -->
> A public key definition gives everything the user needs to employ the key for checking signatures. The <uri>s, if present, give locations where one might find certificates empowering that public key.

R-0091, R-0092

<!-- q L795-803 "The only" .. "signature verification." -->
> The only pub-sig-alg-id's we have defined at this point are for INTERNET-DRAFT Simple Public Key Certificate 26 July 1999 signature verification.

R-0093

<!-- q L804-805 "Other key" .. "application developers." -->
> Other key types are open to being defined by application developers.

R-0094

## §3.8.1.1

<!-- q L831-832 -->
> Although not strictly needed by this draft, the private key for the public key above is:

R-0095

<!-- q L889 -->
> where a, b and c are CRT parameters.

R-0096

## §3.8.1.2

<!-- q L941-942 -->
> The private DSA key differs from the public by the inclusion of the secret x value:

R-0097

## §3.8.1.3

<!-- q L982-983 "All of" .. "key definition." -->
> All of these choices need to be captured and expressed in the public key definition.

R-0098

## §3.8.2

<!-- q L999 -->
> <hash>:: "(" "hash" <hash-alg-name> <hash-value> <uris>? ")" ;

R-0099

<!-- q L1001 "A <hash>" .. "other object." -->
> A <hash> object gives the hash of some other object.

R-0100

## §3.8.3

<!-- q L1014 -->
> <signature>:: "(" "signature" <hash> <principal> <sig-val> ")" ;

R-0101

<!-- q L1016-1018 "A signature" .. "of course." -->
> A signature object is typically used for a certificate body and typically follows that <cert> object in a <sequence>. One can also sign objects other than certificate bodies, of course.

R-0102, R-0103

## §3.8.3.1

<!-- q L1033 -->
> <sig-val>:: "(" <pub-sig-alg-id> <sig-params> ")" ;

R-0104

<!-- q L1034 -->
> <sig-params>:: <byte-string> | <s-expr>+ ;

R-0105

<!-- q L1036-1037 -->
> <sig-params> depends on the <pub-sig-alg-id>, the verification algorithm of the public key being used to verify this signature.

R-0106

<!-- q L1039 -->
> For the RSA algorithm, <sig-params> is a single <integer>.

R-0107

<!-- q L1041-1043 -->
> For DSA, <sig-params> is two S-expressions: (r <integer>) (s <integer>)

R-0108

<!-- q L1045-1046 -->
> For other algorithms, the signature parameter structure will have to be defined when the algorithm is defined.

R-0109

## §4

<!-- q L1147-1148 -->
> <cert>:: "(" "cert" <version>? <cert-display>? <issuer> <issuer-loc>? <subject> <subject-loc>? <deleg>? <tag> <valid>? <comment>? ")" ;

R-0110

<!-- q L1150-1152 "The basic" .. "to another." -->
> The basic certificate form is an authorization certificate. It transfers some specific authorization or permission from one principal to another.

R-0111

<!-- q L1156-1163 -->
> Because a certificate merely transfers authorizations, rather than creating them, the form we call ACL-entry is also defined below to inject authorizations into a chain of certificates. An ACL entry lives on the machine of the verifier, leading to the observation that all authorization flow is in a circuit -- from the verifying machine's ACL, possibly through certificates and then back to the verifying machine. Alternatively, one might say that the only root of an authorization certificate chain is the verifier.

R-0112, R-0113, R-0114

## §4.1

<!-- q L1169 -->
> <version>:: "(" "version" <integer> ")" ;

R-0115

<!-- q L1171-1173 "Version numbers" .. "this draft." -->
> Version numbers are alphanumeric strings. If the <version> field is missing from an object, it is assumed to be (version "0"), which is the version of all objects in this draft.

R-0116, R-0117

<!-- q L1176-1177 -->
> A certificate containing an unrecognized version number must be ignored.

R-0118

## §4.2

<!-- q L1183 -->
> <cert-display>:: "(" "display" <byte-string> ")" ;

R-0119

<!-- q L1185 -->
> This optional field gives a display hint for the entire certificate.

R-0120

<!-- q L1186-1188 -->
> This display parameter does not affect certificate chain reduction, but is provided to aid user-interface software in certificate display.

R-0121

<!-- q L1190 "At this" .. "hints defined." -->
> At this time, we have no such hints defined.

R-0461

<!-- q L1190-1192 "This field" .. "a comment." -->
> This field is up to developers to define as they see fit. For verifiers of certificates, this field is treated as a comment.

R-0122, R-0123

## §4.3

<!-- q L1204 -->
> <issuer>:: "(" "issuer" <principal> ")" ;

R-0124

<!-- q L1206 -->
> <principal>:: <pub-key> | <hash-of-key> ;

R-0125

<!-- q L1208-1210 -->
> <hash-of-key> might be the preferred <principal>, not merely for size but also in case one is using small RSA keys and protecting them from cryptanalysis by keeping them secret.

R-0126

## §4.4

<!-- q L1216 -->
> <issuer-loc>:: "(" "issuer-info" <uris> ")" ;

R-0127

<!-- q L1218-1224 -->
> The (issuer-info ) object provides the location of the certificate(s) by which the issuer derives the authority to pass along the authorization in the present <cert>. We expect the prover (the calling client) to track down such other certificates and provide them to the verifier (the called server), but we allow this information in the certificate to simplify that process for the prover.

R-0128, R-0129

## §4.5

<!-- q L1230 -->
> <subject>:: "(" "subject" <subj-obj> ")" ;

R-0130

<!-- q L1232-1233 -->
> <subj-obj>:: <principal> | <name> | <obj-hash> | <keyholder> | <subj-thresh> ;

R-0131

<!-- q L1235-1240 -->
> In the most basic form, <subj-obj>:: <principal> ; and one may make an SPKI implementation with only that definition, in case names are considered unnecessary for the intended application.

R-0132 (split R-0133, R-0134)

<!-- q L1242-1249 -->
> However in full-blown implementations, the subject may also be a name, representing a group of principals or a delayed binding to some one principal, the hash of an object, or a K-of-N threshold of principals (in which case, the authorization being granted to the subject is being spread out among multiple parties that must cooperate to exercise that authorization). The <keyholder> case is special and of little interest to verifier code, since it is used in a certificate that is a message to a human.

R-0135, R-0136

## §4.5.1

<!-- q L1261 -->
> <obj-hash>:: "(" "object-hash" <hash> ")" ;

R-0137

<!-- q L1263-1264 "This option" .. "a <principal>." -->
> This option for a (subject ) refers to an object other than a <principal>.

R-0138

## §4.5.2

<!-- q L1271 -->
> <keyholder>:: "(" "keyholder" <keyholder-obj> ")" ;

R-0139

<!-- q L1272 -->
> <keyholder-obj>:: <principal> | <name> ;

R-0140

<!-- q L1274-1275 "This form" .. "referenced key." -->
> This form of subject refers to the flesh and blood (or iron and silicon) holder of the referenced key.

R-0141

## §4.5.3

<!-- q L1287 -->
> <subj-thresh>:: "(" "k-of-n" <k-val> <n-val> <subj-obj>* ")" ;

R-0142

<!-- q L1289 -->
> where K < N, and there are N <subj-obj> subjects listed.

R-0143 (split R-0144, R-0145)

<!-- q L1291-1294 -->
> A threshold subject, introduced by Tatu Ylonen for SPKI and by Rivest and Lampson in SDSI 1.0, specifies N subjects for a certificate or ACL entry, of which K must agree before the permission is passed along.

R-0146

<!-- q L1296-1298 "The actual" .. "prover's request." -->
> The actual intent is to insure that there are K distinct paths passing permission between the verifier's ACL and the prover's request.

R-0147

<!-- q L1300-1302 -->
> Since an ACL might want to specify these multiple paths (and an ACL has no Issuer) and since a certificate is signed by a single Issuer, we have chosen to specify the branching at the Subject.

R-0451

<!-- q L1304-1306 "A certificate" .. "delegated permission." -->
> A certificate or ACL with a k-of-n Subject does not delegate permission to any of those subjects, alone. Rather, each of these subjects receives a share of the delegated permission.

R-0148, R-0149

<!-- q L1306-1316 "Only if" .. "the target." -->
> Only if at least K of the N subjects show certificate paths which converge on a single target Subject during reduction, is that permission INTERNET-DRAFT Simple Public Key Certificate 26 July 1999 transmitted to the target.

R-0150

<!-- q L1316-1317 "If fewer" .. "not delegated." -->
> If fewer than K such paths can be shown, then the permission is not delegated.

R-0151

## §4.6

<!-- q L1360 -->
> <subject-loc>:: "(" "subject-info" <uris> ")" ;

R-0152

<!-- q L1362-1363 "This optional" .. "the subject." -->
> This optional field provides the location of information about the subject.

R-0153

## §4.7

<!-- q L1379 -->
> <deleg>:: "(" "propagate" ")" ;

R-0154

<!-- q L1381-1383 -->
> This optional field, if present, notes that the <subject> has not only the permission given in the <cert>'s <tag> field but also the permission to delegate that (or some portion of it) to others.

R-0155

## §4.8

<!-- q L1389 -->
> <tag>:: "(" "tag" "(*)" ")" | "(" "tag" <tag-expr> ")" ;

R-0156

<!-- q L1391 -->
> The form "(tag (*))" means "all permissions".

R-0157

<!-- q L1393-1394 -->
> The simplest tag is an S-expression with no *-forms. This is a specific permission which must be passed along and used intact.

R-0158

<!-- q L1396-1400 -->
> A tag with *-forms represents a set of specific permissions. Any subset of such a set of permissions may be delegated by a principal empowered to delegate. When one is reducing the 5-tuples from such certificates, one intersects the adjacent tag sets to find a resulting tag set.

R-0159, R-0160, R-0161

<!-- q L1402-1403 -->
> All tags are assumed to be positional. That is, parameters in a tag have a meaning defined by their position.

R-0162

<!-- q L1405-1408 -->
> All tags are assumed to be extendable. That is, if one adds a field to the end of a tag definition, one is restricting the permission granted. [If the field added makes the tag invalid, then one has restricted the original permission to zero.]

R-0163 (split R-0164, R-0165)

## §4.9

<!-- q L1417-1418 -->
> The <valid> field gives validity dates and/or online test information for the certificate.

R-0166

<!-- q L1420 -->
> <valid>:: "(" "valid" <not-before>? <not-after>? <online-test>* ")" ;

R-0167

<!-- q L1422 -->
> <not-after>:: "(" "not-after" <date> ")" ;

R-0168

<!-- q L1430 -->
> <not-before>:: "(" "not-before" <date> ")" ;

R-0169

<!-- q L1432-1434 "If either" .. "that direction." -->
> If either is missing, then the certificate is assumed valid for all time in that direction.

R-0170

## §4.9.1

<!-- q L1443 -->
> <date>:: <byte-string> ;

R-0171

<!-- q L1445-1449 -->
> A date field is an ASCII byte string of the form: YYYY-MM-DD_HH:MM:SS always UTC. For internal use, it is treated as a normal byte string.

R-0172, R-0173

<!-- q L1451-1454 "<date> fields" .. "or equal." -->
> <date> fields are compared as normal ASCII byte strings since one never needs to compute the size of a time interval to test validity -- only determine greater-than, less-than or equal.

R-0174

## §4.9.2

<!-- q L1460-1461 -->
> <online-test>:: "(" "online" <online-type> <uris> <principal> <online-id> <s-part>* ")" | "(" "online" "new-cert" <uris> ")" ;

R-0175

<!-- q L1462 -->
> <online-type>:: "crl" | "reval" | "one-time" ;

R-0176

<!-- q L1463 -->
> <online-id>:: "(" "id" <byte-string> ")" ;

R-0177

<!-- q L1465-1466 "The online" .. "validity testing." -->
> The online test option allows a certificate to be backed up by finer grain validity testing.

R-0178

<!-- q L1470-1475 -->
> The reply from an online test is a digitally signed object, validated by the <principal> given in the test specification. That object includes validity dates, so that once one has the online test response, its validity dates can be intersected with the parent certificate's validity dates to yield the current working validity dates for the certificate.

R-0179, R-0180

<!-- q L1477-1479 "The crl" .. "invalid certificates." -->
> The crl form tells the verifier (or prover, who fetches this information for the verifier, in our standard model), the current list of invalid certificates.

R-0181

<!-- q L1479-1487 "If the" .. "presumed valid." -->
> If the present certificate is not on INTERNET-DRAFT Simple Public Key Certificate 26 July 1999 that list, then the certificate is presumed valid.

R-0182

<!-- q L1489-1491 -->
> The re-validate form is the logical opposite of the crl. It tells the verifier a list of valid certificates or, more likely, just that the current certificate is valid.

R-0183

<!-- q L1493-1498 -->
> The one-time form is a re-validate form without validity dates. It must be fetched by the verifier, rather than the prover, since it is valid only for the current verification step. [In effect, it has a validity period of just "now".] The process of getting this one-time revalidation involves sending a unique (and partly random) challenge which is returned as part of the signed response.

R-0184 (split R-0185, R-0186, R-0187), R-0188

<!-- q L1500-1502 -->
> The new-cert form requests a new copy of the certificate in question. The assumption is that these certificates are short-lived and that the one triggering the new-cert fetch had expired.

R-0189

<!-- q L1504 -->
> If there are multiple URIs specified, any one of them can be used.

R-0190

<!-- q L1506-1509 -->
> If the URI specifies an HTTP connection to the online test, then that URI can provide all parameters needed (e.g., a hash of the certificate in question), but in other cases, one might need to list such parameters in the optional <s-part>s.

R-0191

## §4.9.3

<!-- q L1517 -->
> The protocol used for these online tests is not fully specified here.

R-0192

<!-- q L1518-1520 -->
> One can use passive web pages and have the URI fetch the online test result directly. This works for everything but one-time revalidations.

R-0193 (split R-0194)

<!-- q L1522-1526 -->
> One can use CGI-driven HTTP fetches, and allow the CGI code to generate or fetch the online test result specifically for the certificate in question. The URI given in <uris> would include the parameters to that CGI code, so that again the user of the certificate would see just a web page to fetch by HTTP.

R-0195

<!-- q L1528-1533 "If there" .. "the verifier." -->
> If there are other servers and protocols defined, then those definitions will determine how online test results are requested and retrieved. One-time tests fall into this category. The fetch of a one-time test result must be done by the verifying code, while all other tests fetches can be done by the prover, prior to submitting a (sequence...) to the verifier.

R-0196, R-0197 (split R-0198, R-0199)

<!-- q L1533-1544 "That one-time" .. "1999 application-specific." -->
> That one-time test must include a nonce provided by the verifier, to prevent replay attacks, but it will probably also include transaction data (such as an amount of money being debited from a bank account) and therefore be INTERNET-DRAFT Simple Public Key Certificate 26 July 1999 application-specific.

R-0200 (split R-0201)

## §4.10

<!-- q L1550 -->
> <comment>:: "(" "comment" <byte-string> ")" ;

R-0202

<!-- q L1552-1553 -->
> This optional field allows the issuer to attach comments meant to be ignored by any processing code but presumably to be read by a human.

R-0203

## §5

<!-- q L1603-1604 "For actual" .. "to keys." -->
> For actual trust engine computations, names must be reduced to keys.

R-0204

<!-- q L1608-1610 -->
> Note that we do not include an <issuer-loc> option for a name certificate. The issuer needs no authorization in order to create names. Every issuer has that right.

R-0205, R-0206

<!-- q L1612-1613 "Similarly, there" .. "name certificates." -->
> Similarly, there is no "certification practice statement" for these name certificates.

R-0452

<!-- q L1613-1618 "Nothing is" .. "name space." -->
> Nothing is implied by a name certificate about the principal(s) being named. A name can be an arbitrary byte string assigned by the issuer and is intended to be meaningful only to that issuer, although other parties may end up using it. A name is not required or expected necessarily to conform to any name string in the physical world or in any other issuer's name space.

R-0207, R-0208, R-0209

## §5.1

<!-- q L1628-1634 -->
> A name certificate has the form: (cert (issuer (name <principal> <name>)) <subject> <valid> )

R-0210

<!-- q L1636-1637 -->
> <name-cert>:: "(" "cert" <version>? <cert-display>? <issuer-name> <subject> <valid>? <comment>? ")" ;

R-0211

<!-- q L1639-1640 -->
> <issuer-name>:: "(" "issuer" "(" "name" <principal> <byte-string> ")" ")" ;

R-0212

<!-- q L1643-1645 "The name" .. "(name..) structure." -->
> The name must be under the <principal> of the certificate issuer, and under this syntax the certificate issuer <principal> is taken from the (name..) structure.

R-0213 (split R-0214, R-0215)

<!-- q L1647-1650 -->
> In a name certificate, the (tag) field is omitted and (tag (*)) is assumed. There is also no <deleg> field. A name definition is like an extension cord, passing everything the name is granted through to the subject.

R-0216 (split R-0217, R-0218), R-0219

<!-- q L1658 -->
> The subject is unrestricted. It is what you are trying to name.

R-0220

<!-- q L1660-1665 -->
> If there is more than one name certificate for a given name, with different subjects, then that name is a group. More specifically, all name certificates define groups, many of which will have only one member. A multi-member group is like a multi-plug extension cord, passing everything the name is granted through to any and all of its subjects.

R-0221, R-0222, R-0223

## §5.2

<!-- q L1671-1674 -->
> The <name> form is a option for <subject>, when one wants to generate a certificate granting authorization to either a named group of principals or to a principal that has not been defined yet. This can be either a relative name or a fully-qualified name.

R-0224

<!-- q L1676 -->
> <name>:: <relative-name> | <fq-name> ;

R-0225

<!-- q L1678 -->
> <relative-name>:: "(" "name" <names> ")" ;

R-0226

<!-- q L1680 -->
> <fq-name>:: "(" "name" <principal> <names> ")" ;

R-0227

<!-- q L1682 -->
> <names>:: <byte-string>+ ;

R-0228

<!-- q L1684-1687 -->
> A relative name is defined only with respect to an issuer and should show up only in a certificate, borrowing the <principal> from the issuer of that certificate. For evaluation purposes, the relative name is translated into a fully-qualified name before reduction.

R-0229 (split R-0230, R-0231, R-0232), R-0233

<!-- q L1689-1690 -->
> Unlike the <issuer-name>, which is forced to be a name in the issuer's name space, the subject name can be in any name space.

R-0234

## §5.3

<!-- q L1696-1726 -->
> Given the name definition (cert (issuer (name (hash md5 |Txoz1GxK/uBvJbx3prIhEw==|) fred)) (subject (hash md5 |Z5pxCD64YwgS1IY4Rh61oA==|)) (not-after "2001-01-01_00:00:00")) {KDQ6Y2VydCg2Omlzc3Vlcig0Om5hbWUoNDpoYXNoMzptZDUxNjpPGjPUbEr +4G8lvHemsiETKTQ6ZnJlZCkpKDc6c3ViamVjdCg0Omhhc2gzOm1kNTE2Ome acQg+uGMIEtSGOEYetaApKSg5Om5vdC1hZnRlcjE5OjIwMDEtMDEtMDFfMDA 6MDA6MDApKQ==} INTERNET-DRAFT Simple Public Key Certificate 26 July 1999 the name (subject (name (hash md5 |Txoz1GxK/uBvJbx3prIhEw==|) fred sam george mary)) reduces to (subject (name (hash md5 |Z5pxCD64YwgS1IY4Rh61oA==|) sam george mary)) recursing until the name reduces to a principal. In non-pathological cases this is the only reduction rule needed.

R-0235 (split R-0236, R-0237)

<!-- q L1728-1739 -->
> It is possible for someone to generate a trouble-making name certificate, such as: (cert (issuer (name (hash md5 |Txoz1GxK/uBvJbx3prIhEw==|) fred)) (subject (name fred sam)) (not-after "2001-01-01_00:00:00")) in which case a naive reduction would grow without bound. This kind of boundless growth is not possible under the name reduction rules given in the theory document.

R-0238 (split R-0239, R-0240)

## §6

<!-- q L1774-1775 "ACLs are" .. "or application." -->
> ACLs are private to one developer or application.

R-0241

## §6.1

<!-- q L1782 -->
> <acl>:: "(" "acl" <version>? <acl-entry>* ")" ;

R-0242

<!-- q L1784-1785 -->
> <acl-entry>:: "(" "entry" <subj-obj> <deleg>? <tag> <valid>? <comment>? ")" ;

R-0243

<!-- q L1787-1792 -->
> An ACL is a list of assertions: certificate bodies which don't need issuer fields or signatures because they are being held in secure memory. Since the fields of the ACL are fields of a <cert>, we will not repeat those common field definitions here. Since an ACL is not communicated to others, developers are free to choose their own formats.

R-0244, R-0245, R-0246

<!-- q L1794-1797 -->
> If all the optional fields are left out, the subject is given the permission specified in <tag>, without permission to delegate it, with no expiration date or condition (until the ACL is edited to remove the permission).

R-0247

## §6.2

<!-- q L1831 -->
> <sequence>:: "(" "sequence" <seq-ent>* ")" ;

R-0248

<!-- q L1832-1833 -->
> <seq-ent>:: <cert> | <pub-key> | <signature> | <crl> | <delta-crl> | <reval> | <op> ;

R-0249

<!-- q L1834 -->
> <op>:: <hash-op> | <general-op> ;

R-0250

<!-- q L1835 -->
> <hash-op>:: "(" "do" "hash" <hash-alg-name> ")" ;

R-0251

<!-- q L1836 -->
> <general-op>:: "(" "do" <byte-string> <s-part>* ")" ;

R-0252

<!-- q L1838-1839 -->
> At present, only the hash operation is defined. It computes the indicated hash of the last key or cert in the sequence.

R-0253

<!-- q L1841-1844 -->
> A <sequence> is an ordered sequence of objects that the verifier is to consider when deciding to grant access. By reducing certificates in the sequence, the verifier will establish that the final subject (key or object) has been granted authority through the sequence.

R-0254, R-0255

<!-- q L1847-1852 -->
> The sequence can also contain instructions to the verifier, in the form of opcodes. At present the only opcode defined is "hash" -- meaning, that the previous item in the sequence (the last one read in) is to be hashed by the given algorithm and saved, indexed by that hash value. Presumably, that item (certificate body or public key, for example) is referred to by hash in some subsequent object.

R-0256, R-0257, R-0258

<!-- q L1854-1856 -->
> At this time, we assume that <signature> does double duty, calling for the hash of the preceding item. However, it would not hurt to use an explicit <hash-op> prior to a <signature>.

R-0259, R-0260

<!-- q L1858-1859 -->
> If an object will be referenced by different hashes, it can be followed by multiple <hash-op>s.

R-0261

## §7

<!-- q L1891-1894 -->
> An online test results in a digitally signed object carrying its own date range, explicitly or implicitly. That object specifies either a list of invalid certificates or that a given certificate (or list of certificates) is still valid.

R-0262

<!-- q L1896-1897 -->
> This section does not give details of protocols for connecting to online servers or transmitting messages between them.

R-0263

<!-- q L1899-1902 -->
> It is assumed that, except for the one-time test, the prover and not the verifier will fetch any online-test results and then provide those results in the <sequence> being handed to the verifier. A one-time test result must contain a nonce generated by the verifier.

R-0264, R-0265

<!-- q L1903-1905 -->
> Whether the verifier contacts the revalidation center directly or via the prover depends on the details of the application and protocol between the prover and verifier.

R-0266

<!-- q L1907 -->
> Each of these instruments contains a <valid-basic> time interval.

R-0267

<!-- q L1908-1910 -->
> The instrument is valid only during that interval and a sequence of instruments must be issued for non-overlapping intervals, so that the user of the instrument knows when it has the current one.

R-0268 (split R-0269, R-0270)

## §7.1

<!-- q L1916-1917 -->
> If one wants to provide CRLs, and that CRL grows, then one may prefer to send only a delta CRL.

R-0271

<!-- q L1919 -->
> <crl>:: "(" "crl" <version>? <cancel-list> <valid-basic> ")" ;

R-0272

<!-- q L1920 -->
> <cancel-list>:: "(" "canceled" <hash>* ")" ;

R-0273

<!-- q L1921-1922 -->
> <delta-crl>:: "(" "delta-crl" <version>? <hash-of-pred> <cancel-list> <valid-basic> ")" ;

R-0274

<!-- q L1923 -->
> <hash-of-pred>:: <hash> ;

R-0275

<!-- q L1925-1927 -->
> The <hash-of-pred> is the hash of the predecessor CRL or delta-CRL, that this one is modifying. For convenience, that <hash> should probably also have a URI pointing the user to that predecessor.

R-0276, R-0277

<!-- q L1929-1930 -->
> The <crl> or <delta-crl> must be signed by the principal indicated in the <online-test> field that directed the CRL to be fetched.

R-0278

<!-- q L1932-1934 -->
> The CRL request can be a straight HTTP transaction, using the URI provided in the certificate, but we do not specify online protocols in this draft.

R-0279

<!-- q L1943-1944 "The algorithm" .. "left open." -->
> The algorithm for choosing between computation and delivery of delta versus full CRL is left open.

R-0280

## §7.2

<!-- q L1952 -->
> <reval>:: "(" "reval" <version>? <reval-list> <valid-basic> ")" ;

R-0281

<!-- q L1953 -->
> <reval-list>:: "(" "valid" <hash>+ ")" ;

R-0282

<!-- q L1955-1956 -->
> This construct is the logical opposite of a CRL. With a reval instrument, a certificate is valid if it is listed.

R-0283

<!-- q L1958 "There is" .. "no delta-reval." -->
> There is no delta-reval.

R-0284

<!-- q L1959-1961 "Therefore, if" .. "is valid." -->
> Therefore, if the certificate in question shows up on a currently valid reval list, then it is valid.

R-0285

<!-- q L1963-1964 -->
> The <reval> must be signed by the principal indicated in the <online-test> field that directed it to be fetched.

R-0286

## §7.3

<!-- q L1970-1971 -->
> For one-time revalidation, the verifier itself must fetch the (reval) record, which will have the form:

R-0287

<!-- q L1973 -->
> <reval>:: "(" "reval" <version>? <subj-hash> <one-valid> ")" ;

R-0288

<!-- q L1975 -->
> <one-valid>:: "(" "one-time" <byte-string> ")" ;

R-0289

<!-- q L1977-1981 -->
> where the byte string inside <one-valid> is one provided by the caller, expected to be unique over time and unguessable -- e.g., a large random number or random number plus sequence number. This reply should be signed by the <principal> indicated in the (online..) field which directed it to be fetched.

R-0290, R-0291

<!-- q L1983-1984 -->
> This result corresponds to a 0-length validity interval of "now", however the developer wishes to express that.

R-0292

## §8

<!-- q L2002-2007 -->
> This section describes the operation of the trust evaluation machinery assumed to be part of every verifier which accepts SPKI certificates. The inputs to that trust engine are 5-tuples and any kind of certificate, not just SPKI, as well as Access Control List (ACL) entries can be translated to 5-tuples so that they can all participate in the trust computation.

R-0293, R-0294

<!-- q L2013-2017 -->
> Name reduction is specified in section 5.3. Therefore, in what follows we assume all issuers and subjects are principals. We also assume that all principals are public keys. It is an implementation decision whether to store these as explicit keys, hashes of keys (used as pointers) or addresses pointing to keys.

R-0295, R-0296, R-0297

## §8.1

<!-- q L2023 "How a" .. "the developer." -->
> How a 5-tuple is represented and stored is up to the developer.

R-0298

<!-- q L2027 -->
> <5-tuple>:: <issuer5> <subject5> <deleg5> <tag-body5> <valid5> ;

R-0299

<!-- q L2029 -->
> <issuer5>:: <key5> | "self" ;

R-0300

<!-- q L2031 -->
> <subject5>:: <key5> | <obj-hash> | <keyholder> | <threshold-subj> ;

R-0301

<!-- q L2033 -->
> <deleg5>:: "t" | "f" ;

R-0302

<!-- q L2035 -->
> <key5>:: <pub-key> ;

R-0303

<!-- q L2037 -->
> <valid5>:: <valid-basic> | "null" | "now" ;

R-0304

<!-- q L2039 -->
> <tag-body5>:: <tag-body> | "null" ;

R-0305

<!-- q L2041-2043 -->
> The extra option for issuer, "self", is provided for ACL entries. The self referred to is the verifier, holding that ACL and doing the verification of offered proofs.

R-0306

<!-- q L2045-2046 -->
> The only 5-tuples that can mean anything to the verifier, after reduction is done, are those with "self" as issuer.

R-0307

## §8.2

<!-- q L2059-2063 -->
> <i1,s1,d1,a1,v1> + <i2,s2,d2,a2,v2> yields <i1,s2,d2,a,v> if: s1 = i2 d1 = "t" a = the intersection of a1 and a2 v = the intersection of v1 and v2

R-0308 (split R-0309, R-0310, R-0311, R-0312)

<!-- q L2065-2071 -->
> Validity intersection involves normal intersection of date ranges, if there are not-before or not-after fields in v1 or v2, and union of online tests, if those are present in v1 or v2. Each online test includes a validity period, so there is a resulting validity interval in terms of dates. This can include the string "now", as the product of a one-time online test result. "now" intersects with any date range to yield either "now" or "null".

R-0313, R-0314, R-0315, R-0316

<!-- q L2073-2082 "In the" .. "doesn't reduce." -->
> In the most basic case, If a1 is (tag (*)), a = a2. If a2 is (tag (*)), a = a1. If a1 == a2, a = a2. Otherwise, a = "null" and the 5-tuple doesn't reduce.

R-0317 (split R-0318, R-0319, R-0320, R-0321)

## §8.3

<!-- q L2088 "Two <tag>" .. "following rules." -->
> Two <tag> S-expressions intersect by the following rules.

R-0322

<!-- q L2090-2092 "A developer" .. "be necessary." -->
> A developer is free to implement general purpose code that does set-to-set reductions, for example, but that is not likely to be necessary.

R-0323

<!-- q L2094 -->
> 1. basic: if a1 == a2, then the result is a1.

R-0324

<!-- q L2096-2097 -->
> 2. basic: if a1 != a2 and neither has a *-form, then the result is "null".

R-0325

<!-- q L2099 -->
> 3. (tag (*)): if a1 == (tag (*)), then the result is a2.

R-0326

<!-- q L2100 -->
> If a2 == (tag (*)), then the result is a1.

R-0327

<!-- q L2102-2104 -->
> 4. (* set ...): if some <tag> S-expression contains a (* set ) construct, then one expands the set and does the intersection of the resulting simpler S-expressions.

R-0328

<!-- q L2106-2117 -->
> 5. (* range ...): if some <tag> field compares a (* range ) to a INTERNET-DRAFT Simple Public Key Certificate 26 July 1999 <byte-string>, one does the specified range comparison and the resulting field is the explicit one tested. If the strings being compared have unequal display types, then the result is the empty set.

R-0329 (split R-0330)

<!-- q L2119-2121 -->
> 6. (* prefix ...): if some <tag> field compares a (* prefix ) to a <byte-string>, then the result is the explicit string if the test string is a prefix of it and otherwise "null".

R-0331

## §8.4

<!-- q L2128-2134 -->
> A separate document will give full algorithms for reduction of K-of-N threshold subjects. One general procedure is to make K copies of of the 5-tuple containing the K-of-N subject and indicate which of those subjects is being handled by that copy. One then reduces that copy as if it had a single subject. One can stop the separate reductions when all K of the reduced values have the same subject. At that point, the K reduced 5-tuples become a single 5-tuple.

R-0332, R-0333, R-0334, R-0335

<!-- q L2136-2138 -->
> The actual algorithm choices for doing this reduction depend on whether one wants to reduce left-to-right or right-to-left and how much storage a verifier has.

R-0336

## §8.7

<!-- q L2144-2157 -->
> In cases where the verifier, Self, has access to a private key, once it has reduced a chain of certificate bodies down to the form: (Self,X,D,A,V) it can sign that generated body, using its private key, producing an SPKI certificate. That certificate will have a validity period no larger that of any certificate in the loop which formed it, but during that validity period it can be used by the prover instead of the full chain, when speaking to that particular verifier. It is good only at that verifier (or at another which trusts that verifier, Self, to delegate the authorization A). Therefore, one option by the verifier is to sign and return the result 5-tuple to the caller for this later use.

R-0337, R-0338 (split R-0339, R-0340), R-0341, R-0342

<!-- q L2159-2162 -->
> If it isn't important for any other verifier to accept this "result certificate", it can even be signed by a symmetric key (an HMAC with secret key private to the verifier), although such keys are not defined in this standard.

R-0343

## §9

<!-- q L2230-2232 -->
> The following is the BNF of canonical forms and includes lengths for each explicit byte string. So, for example, "cert" is expressed as "4:cert".

R-0344

## §9.1

<!-- q L2241-2242 -->
> <5-tuple>: an object defined for documentation purposes only. The actual contents of a 5-tuple are implementation dependent.

R-0345

<!-- q L2244-2246 -->
> <acl>: an object for local use which might be implementation dependent. An ACL is not expected to be communicated from machine to machine.

R-0346

<!-- q L2248 -->
> <crl>, <delta-crl> and <reval>: objects returned from online tests.

R-0347

<!-- q L2250-2251 -->
> <sequence>: the object carrying keys, certificates and online test results from prover to verifier.

R-0348

## §9.2

<!-- q L2257 -->
> <5-tuple>:: <issuer5> <subject5> <deleg5> <tag-body5> <valid5> ;

R-0299 (same production as §8.1 line 2027)

<!-- q L2258-2259 -->
> <acl-entry>:: "(" "entry" <subj-obj> <deleg>? <tag> <valid>? <comment>? ")" ;

R-0243 (same production as §6.1 lines 1784-1785)

<!-- q L2260 -->
> <acl>:: "(" "acl" <version>? <acl-entry>* ")" ;

R-0242 (same production as §6.1 line 1782)

<!-- q L2261 -->
> <byte-string>:: <bytes> | <display-type> <bytes> ;

R-0047 (same production as §3.2 line 589)

<!-- q L2262 -->
> <bytes>:: <decimal> ":" {binary byte string of that length} ;

R-0048 (same production as §3.2 line 590)

<!-- q L2263 -->
> <cert-display>:: "(" "display" <byte-string> ")" ;

R-0119 (same production as §4.2 line 1183)

<!-- q L2264-2265 -->
> <cert>:: "(" "cert" <version>? <cert-display>? <issuer> <issuer-loc>? <subject> <subject-loc>? <deleg>? <tag> <valid>? <comment>? ")" ;

R-0110 (same production as §4 lines 1147-1148)

<!-- q L2266 -->
> <comment>:: "(" "comment" <byte-string> ")" ;

R-0202 (same production as §4.10 line 1550)

<!-- q L2267 -->
> <crl>:: "(" "crl" <version>? <crl-hash-list> <valid-basic> ")" ;

R-0349

<!-- q L2268 -->
> <crl-hash-list>:: "(" "canceled" <hash>* ")" ;

R-0350

<!-- q L2269 -->
> <date>:: <byte-string> ;

R-0171 (same production as §4.9.1 line 1443)

<!-- q L2270 -->
> <ddigit>:: "0" | <nzddigit> ;

R-0051 (same production as §3.2 line 593)

<!-- q L2271 -->
> <decimal>:: <nzddigit> <ddigit>* | "0" ;

R-0049 (same production as §3.2 line 591)

<!-- q L2272 -->
> <deleg5>:: "t" | "f" ;

R-0302 (same production as §8.1 line 2033)

<!-- q L2273 -->
> <deleg>:: "(" "propagate" ")" ;

R-0154 (same production as §4.7 line 1379)

<!-- q L2274-2275 -->
> <delta-crl>:: "(" "delta-crl" <version>? <hash-of-crl> <crl-hash-list> <valid-basic> ")" ;

R-0351

<!-- q L2276 -->
> <display-type>:: "[" <bytes> "]" ;

R-0052 (same production as §3.2 line 594)

<!-- q L2277-2285 -->
> <dsa-sig-val>:: "(" "dsa-sha1-sig" "(" "r" <byte-string> ")" "(" "s" INTERNET-DRAFT Simple Public Key Certificate 26 July 1999 <byte-string> ")" ")" ;

R-0352

<!-- q L2286 -->
> <fq-name>:: "(" "name" <principal> <names> ")" ;

R-0227 (same production as §5.2 line 1680)

<!-- q L2287 -->
> <general-op>:: "(" "do" <byte-string> <s-part>* ")" ;

R-0252 (same production as §6.2 line 1836)

<!-- q L2288 -->
> <gte>:: "g" | "ge" ;

R-0353

<!-- q L2289 -->
> <hash-alg-name>:: "md5" | "sha1" | <uri> ;

R-0354

<!-- q L2290 -->
> <hash-list>:: "(" "canceled" <hash>* ")" ;

R-0355

<!-- q L2291 -->
> <hash-of-crl>:: <hash> ;

R-0356

<!-- q L2292 -->
> <hash-of-key>:: <hash> ;

R-0357

<!-- q L2293 -->
> <hash-op>:: "(" "do" "hash" <hash-alg-name> ")" ;

R-0251 (same production as §6.2 line 1835)

<!-- q L2294 -->
> <hash-value>:: <byte-string> ;

R-0358

<!-- q L2295 -->
> <hash>:: "(" "hash" <hash-alg-name> <hash-value> <uris>? ")" ;

R-0099 (same production as §3.8.2 line 999)

<!-- q L2296 -->
> <integer>:: <byte-string> ;

R-0054 (same production as §3.2.1 line 602)

<!-- q L2297 -->
> <issuer-loc>:: "(" "issuer-info" <uris> ")" ;

R-0127 (same production as §4.4 line 1216)

<!-- q L2298-2299 -->
> <issuer-name>:: "(" "issuer" "(" "name" <principal> <byte-string> ")" ")" ;

R-0212 (same production as §5.1 lines 1639-1640)

<!-- q L2300 -->
> <issuer5>:: <key5> | "self" ;

R-0300 (same production as §8.1 line 2029)

<!-- q L2301 -->
> <issuer>:: "(" "issuer" <principal> ")" ;

R-0124 (same production as §4.3 line 1204)

<!-- q L2302 -->
> <k-val>:: <integer> ;

R-0359

<!-- q L2303 -->
> <key5>:: <pub-key> ;

R-0303 (same production as §8.1 line 2035)

<!-- q L2304 -->
> <keyholder-obj>:: <principal> | <name> ;

R-0140 (same production as §4.5.2 line 1272)

<!-- q L2305 -->
> <keyholder>:: "(" "keyholder" <keyholder-obj> ")" ;

R-0139 (same production as §4.5.2 line 1271)

<!-- q L2306 -->
> <low-lim>:: <gte> <byte-string> ;

R-0360

<!-- q L2307 -->
> <lte>:: "l" | "le" ;

R-0361

<!-- q L2308 -->
> <n-val>:: <integer> ;

R-0362

<!-- q L2309-2310 -->
> <name-cert>:: "(" "cert" <version>? <cert-display>? <issuer-name> <subject> <valid>? <comment>? ")" ;

R-0211 (same production as §5.1 lines 1636-1637)

<!-- q L2311 -->
> <name>:: <relative-name> | <fq-name> ;

R-0225 (same production as §5.2 line 1676)

<!-- q L2312 -->
> <names>:: <byte-string>+ ;

R-0228 (same production as §5.2 line 1682)

<!-- q L2313 -->
> <not-after>:: "(" "not-after" <date> ")" ;

R-0168 (same production as §4.9 line 1422)

<!-- q L2314 -->
> <not-before>:: "(" "not-before" <date> ")" ;

R-0169 (same production as §4.9 line 1430)

<!-- q L2315 -->
> <nzddigit>:: "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" ;

R-0050 (same production as §3.2 line 592)

<!-- q L2316 -->
> <obj-hash>:: "(" "object-hash" <hash> ")" ;

R-0137 (same production as §4.5.1 line 1261)

<!-- q L2317 -->
> <one-valid>:: "(" "one-time" <byte-string> ")" ;

R-0289 (same production as §7.3 line 1975)

<!-- q L2318-2319 -->
> <online-test>:: "(" "online" <online-type> <uris> <principal> <s-part>* ")" ;

R-0363

<!-- q L2320 -->
> <online-type>:: "crl" | "reval" | "one-time" ;

R-0176 (same production as §4.9.2 line 1462)

<!-- q L2321 -->
> <op>:: <hash-op> | <general-op> ;

R-0250 (same production as §6.2 line 1834)

<!-- q L2322 -->
> <principal>:: <pub-key> | <hash-of-key> ;

R-0125 (same production as §4.3 line 1206)

<!-- q L2323-2324 -->
> <pub-key>:: "(" "public-key" "(" <pub-sig-alg-id> <s-expr>* ")" <uris>? ")" ;

R-0090 (same production as §3.8.1 lines 788-789)

<!-- q L2325-2326 -->
> <pub-sig-alg-id>:: "rsa-pkcs1-md5" | "rsa-pkcs1-sha1" | "rsa-pkcs1" | "dsa-sha1" | <uri> ;

R-0364

<!-- q L2327 -->
> <range-ordering>:: "alpha" | "numeric" | "time" | "binary" | "date" ;

R-0365

<!-- q L2328 -->
> <relative-name>:: "(" "name" <names> ")" ;

R-0226 (same production as §5.2 line 1678)

<!-- q L2329 -->
> <reval-body>:: <one-valid> | <valid-basic> ;

R-0366

<!-- q L2330 -->
> <reval-hash-list>:: "(" "valid" <hash>+ ")" ;

R-0367

<!-- q L2331 -->
> <reval>:: "(" "reval" <version>? <reval-hash-list> <reval-body> ")" ;

R-0368

<!-- q L2332 -->
> <s-expr>:: "(" <byte-string> <s-part>* ")" ;

R-0059 (same production as §3.3 line 623)

<!-- q L2333 -->
> <s-part>:: <byte-string> | <s-expr> ;

R-0060 (same production as §3.3 line 624)

<!-- q L2334-2342 -->
> <seq-ent>:: <cert> | <name-cert> | <pub-key> | <signature> | <op> | INTERNET-DRAFT Simple Public Key Certificate 26 July 1999 <reval> | <crl> | <delta-crl> ;

R-0369

<!-- q L2343 -->
> <sequence>:: "(" "sequence" <seq-ent>* ")" ;

R-0248 (same production as §6.2 line 1831)

<!-- q L2344 -->
> <sig-params>:: <byte-string> | <s-expr>+ ;

R-0105 (same production as §3.8.3.1 line 1034)

<!-- q L2345 -->
> <sig-val>:: "(" <pub-sig-alg-id> <sig-params> ")" ;

R-0104 (same production as §3.8.3.1 line 1033)

<!-- q L2346 -->
> <signature>:: "(" "signature" <hash> <principal> <sig-val> ")" ;

R-0101 (same production as §3.8.3 line 1014)

<!-- q L2347 -->
> <simple-tag>:: "(" <byte-string> <tag-expr>* ")" ;

R-0370

<!-- q L2348 -->
> <subj-hash>:: "(" "cert" <hash> ")" ;

R-0371

<!-- q L2349-2350 -->
> <subj-obj>:: <principal> | <name> | <obj-hash> | <keyholder> | <subj-thresh> ;

R-0131 (same production as §4.5 lines 1232-1233)

<!-- q L2351 -->
> <subj-thresh>:: "(" "k-of-n" <k-val> <n-val> <subj-obj>* ")" ;

R-0142 (same production as §4.5.3 line 1287)

<!-- q L2352 -->
> <subject-loc>:: "(" "subject-info" <uris> ")" ;

R-0152 (same production as §4.6 line 1360)

<!-- q L2353-2354 -->
> <subject5>:: <key5> | <fq-name5> | <obj-hash> | <keyholder> | <subj-thresh> ;

R-0372

<!-- q L2355 -->
> <subject>:: "(" "subject" <subj-obj> ")" ;

R-0130 (same production as §4.5 line 1230)

<!-- q L2356 -->
> <tag-body5>:: <tag-expr> | "null" ;

R-0373

<!-- q L2357 -->
> <tag-expr>:: <simple-tag> | <tag-set> | <tag-string> ;

R-0374

<!-- q L2358 -->
> <tag-prefix>:: "(" "*" "prefix" <byte-string> ")" ;

R-0375

<!-- q L2359-2360 -->
> <tag-range>:: "(" "*" "range" <range-ordering> <low-lim>? <up-lim>? ")" ;

R-0376

<!-- q L2361 -->
> <tag-set>:: "(" "*" "set" <tag-expr>* ")" ;

R-0377

<!-- q L2362 -->
> <tag-star>:: "(" "tag" "(*)" ")" ;

R-0378

<!-- q L2363 -->
> <tag-string>:: <byte-string> | <tag-range> | <tag-prefix> ;

R-0379

<!-- q L2364 -->
> <tag>:: <tag-star> | "(" "tag" <tag-expr> ")" ;

R-0380

<!-- q L2365 -->
> <up-lim>:: <lte> <byte-string> ;

R-0381

<!-- q L2366 -->
> <uri>:: <byte-string> ;

R-0382

<!-- q L2367 -->
> <uris>:: "(" "uri" <uri>+ ")" ;

R-0383

<!-- q L2368 -->
> <valid-basic>:: <not-before>? <not-after>? ;

R-0384

<!-- q L2369 -->
> <valid5>:: <valid-basic> | "null" | "now" ;

R-0304 (same production as §8.1 line 2037)

<!-- q L2370 -->
> <valid>:: "(" "valid" <valid-basic> <online-test>* ")" ;

R-0385

<!-- q L2371 -->
> <version>:: "(" "version" <integer> ")" ;

R-0115 (same production as §4.1 line 1169)


## Source defects

Defects of the source itself, found in pass 1 and recorded rather than
repaired. Each names its lines, and the evidence under it is a marker rendered
by `bin/check-quotes`. The grammar findings (SD-6 to SD-11) were found by
script: every production was extracted, §9.2 was compared with the section
text, and every nonterminal on a right-hand side was resolved against the
left-hand sides.

### SD-1 — Section numbering jumps from 8.4 to 8.7

Section 8 runs 8.1 to 8.4 and then 8.7 (Certificate Result Certificates); there is no 8.5 or 8.6, in the body (lines 2126 and 2142) or in the table of contents (lines 246-247). Nothing refers to a missing section, so no content is known to be lost, but a citation of §8.5 or §8.6 resolves to nothing.

<!-- q L246-247 -->
> 8.4 Reduction of (subject (threshold ..)).................38 8.7 Certificate Result Certificates.......................38

<!-- q L2126 -->
> 8.4. Reduction of (subject (threshold ..))

<!-- q L2142 -->
> 8.7. Certificate Result Certificates

### SD-2 — BCP 14 declared and never used

Lines 39-41 make the RFC 2119 keywords binding, in capitals, and no capitalised keyword occurs anywhere else (`bin/bcp14-count`: 0); every obligation is in lower case (tallied in `requirements.yaml` `lowercase_modals`). Under RFC 2119 as declared the lowercase words may carry keyword force; under RFC 8174, published eighteen years later, they do not. The force of every requirement in this draft is therefore ambiguous by construction; `requirements.yaml` records the lowercase word and its sense instead of choosing. RFC 2119 is also missing from the References (SD-28).

<!-- q L39-41 -->
> The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in RFC 2119.

### SD-3 — The BNF is neither the canonical form §9 claims nor plainly the advanced form §3 claims

§9 (lines 2230-2232) says its BNF is of canonical forms and carries the length of each explicit byte string; not one of the 88 productions of §9.2 carries a length prefix (checked by script), and §3 (lines 535-536) says the BNF deals with advanced forms. The all-permissions literal fits neither: both rules that spell it (lines 1389, 2362) write it as one quoted three-character string. Read the way the grammar's other literals are read, one quoted string to one byte string, that is the three-byte string (*), not the list the rule means; in the advanced form the three characters do spell the list, and canonically the list is (1:*). An implementer has to read every literal as an advanced-form token and apply the §3.1 length rule.

<!-- q L2230-2232 -->
> The following is the BNF of canonical forms and includes lengths for each explicit byte string. So, for example, "cert" is expressed as "4:cert".

<!-- q L535-536 -->
> For the sake of readability, all examples and the BNF in this document deal with advanced rather than canonical S-expressions.

<!-- q L1389 -->
> <tag>:: "(" "tag" "(*)" ")" | "(" "tag" <tag-expr> ")" ;

<!-- q L2362 -->
> <tag-star>:: "(" "tag" "(*)" ")" ;

### SD-4 — `<version>` is an integer in the grammar and an alphanumeric string in the prose

The `<version>` rule takes an `<integer>` (line 1169); the sentences after it call version numbers alphanumeric strings and give the default as the quoted digit 0 (lines 1171-1173). As a string that default is the byte 0x30; as an `<integer>`, §3.2.1 makes 0 the single byte 0x00 (lines 614-615). The readings give different canonical bytes, so a certificate's hash depends on which one its issuer chose, and a verifier that recognises only version 0 (lines 1176-1177) has to decide whether both mean it.

<!-- q L1169 -->
> <version>:: "(" "version" <integer> ")" ;

<!-- q L1171-1173 "Version numbers" .. "in this draft." -->
> Version numbers are alphanumeric strings. If the <version> field is missing from an object, it is assumed to be (version "0"), which is the version of all objects in this draft.

<!-- q L614-615 -->
> The integer value 0 is expressed as a 1-byte string holding the 0 byte, not as the empty string "".

### SD-5 — k-of-n: K < N excludes the draft's own two-of-two use, and the grammar does not bind N

§4.5.3 requires K < N (line 1289), so K = N is not allowed; yet the fourth k-of-n use case (lines 1344-1350) is a permission that needs both of two issuers, a two-of-two, and offers k-of-n as the cleaner way to express it. Separately, the rule's trailing `<subj-obj>`* (line 1287) admits any number of subjects, none included, where the prose requires exactly N, and neither excludes K = 0.

<!-- q L1287-1289 -->
> <subj-thresh>:: "(" "k-of-n" <k-val> <n-val> <subj-obj>* ")" ; where K < N, and there are N <subj-obj> subjects listed.

<!-- q L1344-1350 -->
> 4. using online and off-line issuers. One could have a permission established by an off-line key issuing a long-lived certificate and echoed by an online automated server, issuing short-lived certificates. The delegation of this permission could require both before the eventual subject gets the permission. This can be achieved through the use of (online ) tests in a long-lived certificate, but the K-of-N subject mechanism may be cleaner.

### SD-6 — Undefined nonterminals in the 5-tuple grammar

Three nonterminals are used and never defined: `<threshold-subj>` in §8.1's `<subject5>` (line 2031), `<tag-body>` in §8.1's `<tag-body5>` (line 2039), and `<fq-name5>` in §9.2's `<subject5>` (lines 2353-2354). §9.2 repairs the first two (as `<subj-thresh>` and `<tag-expr>`) and introduces the third, which also contradicts §8's assumption that every subject is a principal once names are reduced (lines 2013-2014). §8.4's heading names the construct threshold (line 2126), a keyword the grammar never uses; the grammar's is k-of-n (line 1287).

<!-- q L2031 -->
> <subject5>:: <key5> | <obj-hash> | <keyholder> | <threshold-subj> ;

<!-- q L2039 -->
> <tag-body5>:: <tag-body> | "null" ;

<!-- q L2353-2354 -->
> <subject5>:: <key5> | <fq-name5> | <obj-hash> | <keyholder> | <subj-thresh> ;

<!-- q L2013-2014 "Name reduction is" .. "are principals." -->
> Name reduction is specified in section 5.3. Therefore, in what follows we assume all issuers and subjects are principals.

<!-- q L2126 -->
> 8.4. Reduction of (subject (threshold ..))

### SD-7 — Three rules for `<reval>`

§7 defines `<reval>` twice, differently: §7.2 (line 1952) with a hash list and `<valid-basic>`, §7.3 (line 1973) with `<subj-hash>` and `<one-valid>`; nothing says the two are alternatives. §9.2 merges them into one rule with `<reval-body>` (lines 2329-2331), but there the one-time form identifies the certificate by a list of hashes, where §7.3 uses `<subj-hash>`, a rule §9.2 defines (line 2348) and none of its rules uses.

<!-- q L1952 -->
> <reval>:: "(" "reval" <version>? <reval-list> <valid-basic> ")" ;

<!-- q L1973 -->
> <reval>:: "(" "reval" <version>? <subj-hash> <one-valid> ")" ;

<!-- q L2329-2331 -->
> <reval-body>:: <one-valid> | <valid-basic> ; <reval-hash-list>:: "(" "valid" <hash>+ ")" ; <reval>:: "(" "reval" <version>? <reval-hash-list> <reval-body> ")" ;

<!-- q L2348 -->
> <subj-hash>:: "(" "cert" <hash> ")" ;

### SD-8 — §9.2's `<online-test>` loses `<online-id>` and new-cert

§4.9.2 (lines 1460-1463) defines `<online-test>` with an `<online-id>` and a second alternative for new-cert, and defines `<online-id>`. §9.2 (lines 2318-2319) has neither, and no `<online-id>` rule. No sentence anywhere says what `<online-id>` identifies; §7 opens with an editor's question about IDs for CRL and reval threads (lines 1888-1889, SD-19), which suggests the field was added for that and never described.

<!-- q L1460-1463 -->
> <online-test>:: "(" "online" <online-type> <uris> <principal> <online-id> <s-part>* ")" | "(" "online" "new-cert" <uris> ")" ; <online-type>:: "crl" | "reval" | "one-time" ; <online-id>:: "(" "id" <byte-string> ")" ;

<!-- q L2318-2319 -->
> <online-test>:: "(" "online" <online-type> <uris> <principal> <s-part>* ")" ;

### SD-9 — A name certificate cannot travel in a §6.2 sequence

§6.2's `<seq-ent>` (lines 1832-1833) lists `<cert>`, `<pub-key>`, `<signature>`, `<crl>`, `<delta-crl>`, `<reval>` and `<op>`; §9.2's (lines 2334-2342) adds `<name-cert>`. A `<name-cert>` is not a `<cert>` (its issuer is an `<issuer-name>`), so under §6.2 a prover cannot deliver the name certificates that name reduction (§5.3) needs.

<!-- q L1832-1833 -->
> <seq-ent>:: <cert> | <pub-key> | <signature> | <crl> | <delta-crl> | <reval> | <op> ;

<!-- q L2334-2342 -->
> <seq-ent>:: <cert> | <name-cert> | <pub-key> | <signature> | <op> | INTERNET-DRAFT Simple Public Key Certificate 26 July 1999 <reval> | <crl> | <delta-crl> ;

### SD-10 — Unreferenced §9.2 rules, one contradicting the DSA signature form

§9.2 defines three rules that no §9.2 rule references: `<dsa-sig-val>` (lines 2277-2285), `<hash-list>` (line 2290, the same right-hand side as `<crl-hash-list>`) and `<subj-hash>` (line 2348, used only by §7.3). `<dsa-sig-val>` also disagrees with §3.8.3.1 (lines 1041-1043) and with the DSA sample signature (lines 1095-1097): it names the algorithm dsa-sha1-sig and takes r and s as plain byte strings, where those use dsa-sha1 and r and s integers inside `<sig-val>`.

<!-- q L2277-2285 -->
> <dsa-sig-val>:: "(" "dsa-sha1-sig" "(" "r" <byte-string> ")" "(" "s" INTERNET-DRAFT Simple Public Key Certificate 26 July 1999 <byte-string> ")" ")" ;

<!-- q L1041-1043 -->
> For DSA, <sig-params> is two S-expressions: (r <integer>) (s <integer>)

<!-- q L1095-1097 -->
> (dsa-sha1 (r |APyNegTrlzLMCCcMRWoMlnKAOHIu|) (s |AIPV/423068nuoNmoQQupyW3x+S1|)))

### SD-11 — Nonterminals renamed between §7 and §9.2

`<cancel-list>` (line 1920), `<hash-of-pred>` (line 1923) and `<reval-list>` (line 1953) appear in §9.2 as `<crl-hash-list>` (line 2268), `<hash-of-crl>` (line 2291) and `<reval-hash-list>` (line 2330), with the same right-hand sides. Harmless to a reader, but the two grammars cannot be merged by name, and §9.2 is not the complete grammar its title suggests: it lacks the §7 names and `<online-id>`.

<!-- q L1919-1923 -->
> <crl>:: "(" "crl" <version>? <cancel-list> <valid-basic> ")" ; <cancel-list>:: "(" "canceled" <hash>* ")" ; <delta-crl>:: "(" "delta-crl" <version>? <hash-of-pred> <cancel-list> <valid-basic> ")" ; <hash-of-pred>:: <hash> ;

### SD-12 — §5.3's examples break the name-certificate grammar

Both name certificates in §5.3 (lines 1698-1702 and 1731-1735) put the not-after date directly in the certificate, and so does the canonical form printed for the first (lines 1704-1707; decoded by script, its body is cert, issuer, subject and not-after with no valid list). `<name-cert>` (lines 1636-1637) admits validity only as `<valid>`, the (valid ...) list of §4.9 (line 1420). A parser that follows the grammar rejects the draft's own name-reduction example.

<!-- q L1698-1702 -->
> (cert (issuer (name (hash md5 |Txoz1GxK/uBvJbx3prIhEw==|) fred)) (subject (hash md5 |Z5pxCD64YwgS1IY4Rh61oA==|)) (not-after "2001-01-01_00:00:00"))

<!-- q L1636-1637 -->
> <name-cert>:: "(" "cert" <version>? <cert-display>? <issuer-name> <subject> <valid>? <comment>? ")" ;

### SD-13 — §5.1's template and the `<issuer-name>` rule disagree

The template (lines 1630-1634) writes the issuer as a name list holding a principal and a `<name>`; `<issuer-name>` (lines 1639-1640) holds a principal and one `<byte-string>`. A `<name>` is itself a (name ...) list (line 1676), so the template, read literally, nests a name inside a name.

<!-- q L1630-1634 -->
> (cert (issuer (name <principal> <name>)) <subject> <valid> )

<!-- q L1639-1640 -->
> <issuer-name>:: "(" "issuer" "(" "name" <principal> <byte-string> ")" ")" ;

### SD-14 — The one-time reply is held to a weaker signing word than CRLs and revals

The CRL and delta-CRL rule (lines 1929-1930) and the reval rule (lines 1963-1964) use must for the signature by the online test's principal; the one-time rule (lines 1979-1981) uses should, for the instrument with the strongest freshness claim. Whatever force the lowercase words carry (SD-2), the one-time reply carries less of it.

<!-- q L1929-1930 -->
> The <crl> or <delta-crl> must be signed by the principal indicated in the <online-test> field that directed the CRL to be fetched.

<!-- q L1963-1964 -->
> The <reval> must be signed by the principal indicated in the <online-test> field that directed it to be fetched.

<!-- q L1979-1981 "This reply" .. "to be fetched." -->
> This reply should be signed by the <principal> indicated in the (online..) field which directed it to be fetched.

### SD-15 — Who fetches the one-time result

§4.9.2 (lines 1493-1495), §4.9.3 (lines 1530-1531) and §7.3 (lines 1970-1971) all have the verifier fetch the one-time result itself. §7 (lines 1903-1905) leaves it to the application whether the verifier reaches the revalidation center itself or through the prover. Both hold only if going through the prover means relaying a request the verifier makes with its own nonce, which the draft never says.

<!-- q L1493-1495 "It must be fetched" .. "verification step." -->
> It must be fetched by the verifier, rather than the prover, since it is valid only for the current verification step.

<!-- q L1903-1905 -->
> Whether the verifier contacts the revalidation center directly or via the prover depends on the details of the application and protocol between the prover and verifier.

### SD-16 — The one-time reply lacks the `<valid-basic>` §7 promises

§7 gives every one of its instruments a `<valid-basic>` interval (line 1907); the one-time `<reval>` carries `<one-valid>` instead (lines 1973-1975), which §7.3 maps to a zero-length interval of now (lines 1983-1984).

<!-- q L1907 -->
> Each of these instruments contains a <valid-basic> time interval.

### SD-17 — Tag intersection cannot carry out §4.8's extension rule

§4.8 (lines 1405-1408) says appending a field to a tag restricts it, so a tag list and a longer list beginning with the same elements stand in a subset relation. §8.3's six rules (lines 2094-2121) have no case for that pair: rule 2 (lines 2096-2097) gives null for any two unequal tags without *-forms. Under §8.3 as written a permission and its own restriction intersect to nothing, and delegating a narrower tag than one holds never reduces.

<!-- q L1405-1408 -->
> All tags are assumed to be extendable. That is, if one adds a field to the end of a tag definition, one is restricting the permission granted. [If the field added makes the tag invalid, then one has restricted the original permission to zero.]

<!-- q L2096-2097 -->
> 2. basic: if a1 != a2 and neither has a *-form, then the result is "null".

### SD-18 — Range intersection is undefined

Rule 5 (lines 2106-2117) performs the specified range comparison, but the orderings (`<range-ordering>`, line 2327) and limit operators (`<gte>` and `<lte>`, lines 2288 and 2307) are only names: no ordering, and no meaning of g, ge, l or le, is defined. Rule 5 also names its display-type failure the empty set, where rules 2 and 6 say null, and gives no result at all for a range comparison that fails.

<!-- q L2327 -->
> <range-ordering>:: "alpha" | "numeric" | "time" | "binary" | "date" ;

<!-- q L2114-2117 "If the strings" .. "the empty set." -->
> If the strings being compared have unequal display types, then the result is the empty set.

### SD-19 — Editor's notes left in the published draft

§3.8.1.3 ends in a starred placeholder asking for an elliptic-curve scheme to be invented and reviewed (lines 987-993), so the section defines no key format at all; §7 opens with a starred question about IDs for CRL and reval threads (lines 1888-1889).

<!-- q L989-991 -->
> Invent a scheme here and pass it by Certicom and Burt -- to define S-expressions for field element, compressed EC point, basis choice, EC curve, .... Show S-expressions for curve over both fields.

<!-- q L1888-1889 -->
> ********** should I have an ID for a CRL or reval thread or let the public key signing the instrument be the ID for it? ******

### SD-20 — §8.4: a doubled word, and K copies for N subjects

Line 2129 prints one word twice. More substantively, the procedure makes K copies of the 5-tuple, one per subject handled; a k-of-n lists N subjects, so K copies cover only K of them, and the stop rule (all K reduced values share a subject, lines 2132-2134) succeeds only if the K chosen in advance are ones with converging paths. One copy per listed subject, stopping when K converge, always finds a qualifying set; that reading is ours.

<!-- q L2129-2131 "One general" .. "that copy." -->
> One general procedure is to make K copies of of the 5-tuple containing the K-of-N subject and indicate which of those subjects is being handled by that copy.

### SD-21 — §8.7: a missing word in the result certificate's validity bound

Lines 2150-2151 lack the word than in the comparison that bounds a result certificate's validity. The sense is clear; it is recorded because the bound is load-bearing.

<!-- q L2150-2151 "That certificate will" .. "which formed it" -->
> That certificate will have a validity period no larger that of any certificate in the loop which formed it

### SD-22 — §3.8.2's example hashes are of the RSA key two subsections up

§3.8.2 gives two hashes of the key above it (lines 1001-1008). The nearest key above is the §3.8.1.2 DSA key; the hashes are of the §3.8.1.1 RSA key. md5 and sha1 of the RSA key's 179-byte canonical form (lines 826-829, decoded) reproduce both printed values, and those of the DSA key's 469-byte form do not (checked by script).

<!-- q L1001-1002 -->
> A <hash> object gives the hash of some other object. For example, the public key given above has the following hashes:

### SD-23 — Which item a hash op hashes

§6.2 first says the hash op hashes the most recent key or certificate (lines 1838-1839), then that it hashes the previous item, the last one read in, of whatever kind (lines 1848-1851), and then allows several hash ops after one object (lines 1858-1859), where the item read just before a second op is the first op. The intent, the most recent object that is not an op, is clear only from the last of the three.

<!-- q L1838-1839 -->
> At present, only the hash operation is defined. It computes the indicated hash of the last key or cert in the sequence.

<!-- q L1848-1851 "At present the only" .. "that hash value." -->
> At present the only opcode defined is "hash" -- meaning, that the previous item in the sequence (the last one read in) is to be hashed by the given algorithm and saved, indexed by that hash value.

### SD-24 — The glossary lists three online tests, §4.9.2 four

The glossary entry for online tests names three forms (lines 410-411); §4.9.2 also defines new-cert (lines 1460-1461 and 1500-1502).

<!-- q L410-411 "ONLINE TEST:" .. "one-time revalidation." -->
> ONLINE TEST: one of three forms of validity test: (1) CRL; (2) revalidation; or (3) one-time revalidation.

### SD-25 — §9.1's top-level objects omit those §3.8 calls top level

§3.8 (lines 753-757) names as top-level objects a `<sequence>` holding `<cert>`, `<pub-key>`, `<signature>` and `<op>` objects, and the verifier's `<acl>`; §9.1 (lines 2238-2251) lists `<5-tuple>`, `<acl>`, `<crl>`, `<delta-crl>`, `<reval>` and `<sequence>`, and omits `<cert>`, `<pub-key>`, `<signature>` and `<op>`.

<!-- q L753-757 -->
> In a communication from prover to verifier, one might encounter only a small number of different objects: usually a <sequence> of <cert>, <pub-key>, <signature> and <op>. The verifier will also need to refer to its own <acl>. These are considered top level objects and are defined in the sections immediately following

### SD-26 — Canonical form is unique; the integers in it are not

The glossary says a canonical S-expression permits no equivalent representations (lines 371-372) and §3.1 calls it a unique representation (lines 553-555). That holds of byte strings, not of the integers they carry: §3.2.1 permits but does not require redundant sign bytes (lines 610-612), so one integer value has several legal encodings, hence several canonical forms and hashes. A signature over one encoding does not verify over another, and nothing tells a producer which to emit.

<!-- q L610-612 "On the assumption" .. "need not be." -->
> On the assumption that they are signed, a leading 0x00 or 0xFF byte may need to be present, but redundant bytes of sign need not be.

### SD-27 — What a signature signs is unspecified

A `<signature>` is a hash, a principal and a `<sig-val>` (line 1014), and §3.1 makes the canonical form what every hash and signature is computed over (lines 553-555), but nothing says which bytes `<sig-val>` is computed over: the canonical (hash ...) object, the bare hash value, or the signed object. The two sample signatures (lines 1052-1097) sign a hash whose object is not given, so neither can be checked against an object. Checked against the printed hash they settle the reading by example: the DSA sample verifies with the printed hash value as its digest and not with the sha1 of the canonical (hash ...) object, and the RSA sample's recovered block ends in the printed hash value (`examples/reproduce.py`, R-0398). From the prose alone, two implementations can differ here and both conform.

<!-- q L1014 -->
> <signature>:: "(" "signature" <hash> <principal> <sig-val> ")" ;

### SD-28 — RFC 2119 is cited and not referenced

Line 41 interprets the keywords as described in RFC 2119, and RFC 2119 is not in the References (lines 2399-2497), which do list RFC 1321, 1780, 2045, 2046, 2047, 2065 and 2104. §3.7 cites RFC 1780, a list of Internet official protocol standards (lines 2468-2469), for the IANA role it prefers (line 730).

<!-- q L39-41 -->
> The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in RFC 2119.

### SD-29 — The glossary's subject forms omit `<keyholder>` and narrow the threshold

The glossary entry for subjects (lines 429-432) names four forms: a key, a name, a hash of an object, and keys in a threshold. `<subj-obj>` (lines 1232-1233) has five, adding `<keyholder>`, and a `<subj-thresh>` (line 1287) lists any `<subj-obj>`, names and nested thresholds included, not only keys. The grammar is the binding text (C-0010 is rejected for that reason); the glossary under-describes it, as it does the online tests (SD-24).

<!-- q L429-432 -->
> SUBJECT: the thing empowered by a certificate or ACL entry. This can be in the form of a key, a name (with the understanding that the name is mapped by certificate to some key or other object), a hash of some object, or a set of keys arranged in a threshold function.

<!-- q L1232-1233 -->
> <subj-obj>:: <principal> | <name> | <obj-hash> | <keyholder> | <subj-thresh> ;

<!-- q L1287 -->
> <subj-thresh>:: "(" "k-of-n" <k-val> <n-val> <subj-obj>* ")" ;

### SD-30 — new-cert escapes the rules §4.9.2 gives every online-test reply

§4.9.2 has the reply to an online test signed and validated by the `<principal>` the test names (lines 1470-1471), and its validity dates intersected with the parent certificate's (lines 1472-1475). The new-cert alternative of `<online-test>` (lines 1460-1461) names no `<principal>`, and its reply is a new copy of a certificate whose predecessor had expired (lines 1500-1502). There is no principal to validate that reply, and intersecting its dates with the expired parent's leaves no interval that includes the present, so neither rule can apply to new-cert as written. R-0410 records the reading that works: the copy is verified as a certificate in its own right.

<!-- q L1470-1475 -->
> The reply from an online test is a digitally signed object, validated by the <principal> given in the test specification. That object includes validity dates, so that once one has the online test response, its validity dates can be intersected with the parent certificate's validity dates to yield the current working validity dates for the certificate.

<!-- q L1460-1461 -->
> <online-test>:: "(" "online" <online-type> <uris> <principal> <online-id> <s-part>* ")" | "(" "online" "new-cert" <uris> ")" ;

<!-- q L1500-1502 -->
> The new-cert form requests a new copy of the certificate in question. The assumption is that these certificates are short-lived and that the one triggering the new-cert fetch had expired.

### SD-31 — Wording slips inside carried texts

Five slips of the source sit inside requirement texts, kept verbatim and not corrected: a missing preposition in the glossary entry for ACLs (line 356, R-0438), a singular article before a plural noun in §3.7 (line 732, R-0074), a sentence of §3.8 that stops without its full stop (line 757, R-0460), the article a before a vowel in §5.2 (line 1671, R-0224), and a plural tests where §4.9.3 means the singular (line 1532, R-0197 and its split child R-0199). The sense is clear in each; they are recorded so that no later pass heals them. Where a slip touches a rule it has its own entry: §8.4's doubled word is SD-20 and §8.7's missing word SD-21.

<!-- q L354-357 "That is, a" .. "implicit issuer)." -->
> That is, a certificate communicates power from its issuer to its subject, but the ACL is the source that power (since it theoretically has the owner of the resource being controlled as its implicit issuer).

<!-- q L731-733 -->
> In the interest of maximum flexibility we also permit users to define their own algorithm names via a normal URIs (which presumably point to descriptions of the algorithms or even to code).

<!-- q L756-757 "These are" .. "immediately following" -->
> These are considered top level objects and are defined in the sections immediately following

<!-- q L1671-1673 "The <name> form" .. "defined yet." -->
> The <name> form is a option for <subject>, when one wants to generate a certificate granting authorization to either a named group of principals or to a principal that has not been defined yet.

<!-- q L1531-1533 "all other tests" .. "to the verifier." -->
> all other tests fetches can be done by the prover, prior to submitting a (sequence...) to the verifier.

### SD-32 — Two issuers for an ACL entry

The glossary makes the owner of the controlled resource the implicit issuer of an ACL (lines 356-357); §4 makes the verifier the only root of a certificate chain (lines 1162-1163), and §8.1 gives an ACL entry the issuer self, which is the verifier (lines 2041-2043). The two answers coincide only when the verifier owns the resource, which the draft never says. Reduction is unaffected, since it only needs the final issuer to be self (R-0307). It matters where the verifier signs a result certificate with its own private key (§8.7, lines 2144-2150): under the glossary's reading that certificate re-issues the owner's authority under the verifier's key. R-0437 records the related gap: how the verifier is to accept that key later.

<!-- q L354-357 "That is, a" .. "implicit issuer)." -->
> That is, a certificate communicates power from its issuer to its subject, but the ACL is the source that power (since it theoretically has the owner of the resource being controlled as its implicit issuer).

<!-- q L1162-1163 "Alternatively, one" .. "is the verifier." -->
> Alternatively, one might say that the only root of an authorization certificate chain is the verifier.

<!-- q L2041-2043 -->
> The extra option for issuer, "self", is provided for ACL entries. The self referred to is the verifier, holding that ACL and doing the verification of offered proofs.

### SD-33 — Not every binary example has the promised base64 form

Found in pass 2 (verify). §3.6 promises a base64 form for every example whose canonical form is binary (lines 715-717). Six printed examples have binary bytes in their canonical form (a hash value or a signature value) and no {base64} rendering: the fully qualified name of §2 (line 407, E02), both sample signatures of §3.8.3.2 (lines 1052-1097, E17 and E18), the two names of §5.3 (lines 1717-1718 and 1722-1723, E27 and E28) and §5.3's trouble-making certificate (lines 1731-1735, E29). The eight base64 blocks the draft does print are listed in `examples/README.md`. No rule depends on it; it is recorded because the sentence is the draft's own claim about its vectors, and it is false for six of them.

<!-- q L715-717 "Each example here" .. "binary canonical form." -->
> Each example here that has a binary canonical form is presented along with the base-64 encoded form which the reader can decode to get the binary canonical form.

## Crosswalk: the other lanes' source-defect lists

Four lists exist, numbered independently, so an SD number means nothing without its file: this file's SD-1 to SD-33 (cited by requirements.yaml, unpadded), messages.yaml SD-01 to SD-18 (zero-padded, on messages as `source_defect`, and cited in schema/README.md and examples/README.md as `messages.yaml SD-nn`), protocol.yaml D-01 to D-41 (`source_defects_and_tensions`, repeated in protocol.md and as `source_tensions` in state-machine.yaml), and design-notes.md §14 SI-1 to SI-19. The same number therefore names different defects: this file's SD-5 (K < N) is not messages.yaml SD-05 (three `<reval>` rules), and this file's SD-13 (the §5.1 template) is not messages.yaml SD-13 (two derivations of `(tag (*))`). No id was renumbered. The rows were proposed by script from the source lines each entry cites (`lines` overlap of this file's quotations against the other three lists), then each pair was read against the source lines before it was kept; a — means no counterpart in that lane, not that the lane is silent on the area.

| this file | defect | messages.yaml | protocol.yaml | design-notes.md §14 |
|---|---|---|---|---|
| SD-1 | section numbering jumps 8.4 to 8.7 | SD-16 | D-15 | SI-13 |
| SD-2 | BCP 14 declared, never used | — | — | — |
| SD-3 | BNF claims canonical form, is advanced; `(*)` is one literal | SD-15 | — | — |
| SD-4 | `<version>` integer in the grammar, string in the prose | SD-01 | D-16 | SI-1 |
| SD-5 | K < N excludes two-of-two; N not bound | SD-10 | D-12 | SI-2 |
| SD-6 | undefined nonterminals in the 5-tuple grammar | SD-06, SD-07 | D-05, D-06, D-14 | SI-11, SI-12 |
| SD-7 | three rules for `<reval>` | SD-05 | D-03 | SI-8 |
| SD-8 | §9.2 `<online-test>` loses `<online-id>` and new-cert | SD-03 | D-02, D-22 | SI-7 |
| SD-9 | name certificate cannot travel in a §6.2 sequence | SD-04 | D-01 | SI-10 |
| SD-10 | unreferenced §9.2 rules, one contradicting the DSA form | SD-02, SD-11 | D-04, D-20 | SI-9, SI-14 |
| SD-11 | nonterminals renamed between §7 and §9.2 | — | D-04 | SI-9 |
| SD-12 | §5.3 examples break the name-certificate grammar | SD-08 | D-23 | SI-5 |
| SD-13 | §5.1 template against the `<issuer-name>` rule | — | D-24 | SI-6 |
| SD-14 | one-time reply held to a weaker signing word | — | D-11 | — |
| SD-15 | who fetches the one-time result | — | D-10 | — |
| SD-16 | one-time reply lacks the `<valid-basic>` §7 promises | — | D-08 | — |
| SD-17 | tag intersection cannot carry out the extension rule | — | D-17 | SI-3 |
| SD-18 | range intersection undefined; display-type failure named differently | — | D-40, D-25 | SI-15 |
| SD-19 | editor's notes left in the draft | SD-17, SD-18 | D-21, D-22 | SI-16 |
| SD-20 | §8.4 doubled word; K copies for N subjects | — | D-13, D-37 | SI-12, SI-16 |
| SD-21 | §8.7 missing word in the validity bound | — | D-37 | — |
| SD-22 | §3.8.2 example hashes are of the RSA key | — | — | — |
| SD-23 | which item a hash op hashes | — | D-18 | SI-19 |
| SD-24 | glossary lists three online tests, §4.9.2 four | — | D-09 | — |
| SD-25 | §9.1 top-level objects omit those §3.8 names | — | — | — |
| SD-26 | canonical form unique, integers in it are not | — | — | — |
| SD-27 | what a signature signs is unspecified | — | — | — |
| SD-28 | RFC 2119 cited, not referenced | — | — | — |
| SD-29 | glossary subject forms omit `<keyholder>`, narrow the threshold | — | — | — |
| SD-30 | new-cert escapes the reply rules of §4.9.2 | — | D-09 | — |
| SD-31 | wording slips inside carried texts | — | D-37 | — |
| SD-32 | two issuers for an ACL entry | — | — | — |
| SD-33 | not every binary example has its base64 form | — | — | — |

Carried by one other lane only, with no entry here, and why:

- messages.yaml SD-09 (the BNF fixes `<cert>` field order, the prose lets it vary): protocol.yaml D-19 reaches the same field-order freedom from the hashing side (one certificate, many canonical forms), and design-notes.md carries it as C6. It is not a defect of one sentence, so this file lists no SD for it.
- messages.yaml SD-12 (`<subj-obj>` defined twice in §4.5, the second as the principals-only form): requirements.yaml carries both rules (R-0131, R-0133).
- messages.yaml SD-13 (`(tag (*))` and `(tag (* set ...))` each derive two ways): counted by the derived checker; no sentence of the source says either rule is ambiguous.
- messages.yaml SD-14 (the RSA sample signature E17 does not verify as PKCS#1 v1.5): a defect of that vector, not of a rule. SD-27 here uses the same sample's recovered block as evidence of what a signature is computed over, which is a different question.
- protocol.yaml D-07 (§8.2 unites online tests inside `<valid5>`, which holds only dates, `null` or `now`), D-26 (the caller is the verifier in §7.3 and the prover in §8.7), D-27 (the validity of a name certificate's 4-tuple is never used), D-28 (the merged threshold tuple has no stated fields), D-29 (a result certificate is issued by the verifier's key, not `self`), D-30 (equality of a key and a hash of it in `s1 = i2`), D-31 (the request and the rule comparing it with the authorization are undefined), D-32 (which bytes a listed hash covers), D-34 (the unrecognised-version rule names certificates only), D-35 (`<general-op>` has no operation), D-36 (how a delta-CRL combines with its predecessor), D-38 (a relative name in an ACL entry), D-39 (threshold algorithms deferred): gaps found by building the protocol and state-machine model, where a step or transition needs the missing rule.
- protocol.yaml D-33 and design-notes.md SI-18 are one finding (a CRL or reval is tied to the certificate it answers only by its signer). protocol.yaml D-41 and design-notes.md SI-4 are one finding (rule 4 does not say how set results combine, and no rule intersects two `*`-forms).
- design-notes.md SI-17 (`rsa-pkcs1` names no hash and no text describes it): marked inferred there.

The counterparts above are of the same defect, not of the same wording: a lane may split one defect in two (this file's SD-6 is messages.yaml SD-06 and SD-07) or join two (protocol.yaml D-37 carries the slips of this file's SD-20, SD-21 and SD-31). Where a lane records a tension rather than a defect (protocol.yaml D-10, D-11, D-17, D-19), the row says the same sentences conflict, not that the lane classed them alike.

## Extraction notes (tool behaviour, not source defects)

- **Running header inside quotations.** `bin/_source_text` removes each page
  footer but not this draft's running header, whose shape its `HEADER` pattern
  (an RFC header) does not match. A quotation crossing a page therefore carries
  the header line's words mid-sentence; they are the source's own bytes and
  `bin/check-quotes` verifies them. Affected requirements: R-0093, R-0150, R-0182, R-0200, R-0235, R-0329, R-0352, R-0369, R-0441.
- **Skeleton sentence splitting.** The abbreviation guard in `bin/fx1-skeleton`
  matches any word ending in *al* plus a full stop, so C-0107, C-0118 and
  C-0124 weld two sentences each; C-0024, C-0087 and C-0131 weld for other
  reasons.
  The requirements cut them apart.
- **Skeleton candidates cut at a page.** C-0046, C-0065, C-0094 and C-0141 stop
  at the running header; their requirements carry the whole sentence.
- **Skeleton locators.** C-0149, C-0150 (References) and C-0151
  (Acknowledgments) are filed under §9.2 because unnumbered headings are not
  section boundaries for `bin/_source_text.section_of_line`; all three are
  rejected.
- **One quotation for two requirements.** R-0449's text ends in a quotation
  mark, and a marker anchor cannot contain one, so §3's first quotation (lines
  520-526) carries R-0449 and R-0027 together and names both.
- **Completion audit.** A second run of the requirements lane walked the
  source section by section and added R-0438 to R-0459: the defining sentence
  of every glossary entry not yet carried (R-0438 to R-0448), three sentences
  of §3, §3.8 and §4.5.3 (R-0449 to R-0451), the disclaimer of §5 (R-0452),
  seven inferred rules (R-0453 to R-0459, not quoted here), and two sentences
  of §3.8 and §4.2 that a character-level coverage sweep found in no text
  (R-0460, R-0461). It also found SD-29 to SD-32.

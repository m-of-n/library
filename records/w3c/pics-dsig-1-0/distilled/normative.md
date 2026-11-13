---
record: pics-dsig-1-0
kind: normative
title: "pics-dsig-1-0 — normative text"
generated_by: bin/fx1-skeleton
extracted: "2026-11-12"
reviewed_by: ""
---

# Normative text

Every binding statement of PICS Signed Labels (DSig) 1.0 (W3C Recommendation, 27 May 1998, REC-DSig-label-19980527), in source order, as quotation markers whose words `bin/check-quotes --render` writes from `.cache/pics-dsig-1-0.txt` (the `bin/render-w3c --ordinal` rendering of the HTML of record; line numbers count there). Nothing below a marker was typed.

**Section numbers are not the source's.** The Recommendation numbers no section; every `§n` here is the renderer's structural ordinal for a heading, so each heading below carries the source's title beside it, and prose cites both (for example §8.1.2, Canonicalization of the equivalent standalone label for signing).

Built by pass 1 (requirements agent) over the `bin/fx1-skeleton` layer. The source uses no BCP 14 keyword (`bin/bcp14-count` = 0); its obligations are lowercase, so every entry of `requirements.yaml` is verb `none`, with the force the text carries in `strength` (must, should, may, defines; see the requirements file's note). Each quotation is the full text of one entry, its id on the line after it with its strength and origin (a candidate id, or hunted: binding text no candidate caught). A parent whose text welds several elements lists its `split_of` children on that line; their texts are sub-spans of the quotation above them. Where two adjacent entries share one marker, it is because a marker anchor cannot carry a quotation mark and one of the two texts begins or ends with one; both ids are named. Inferred entries are not source text and are named in place without a quotation. 318 entries: 108 promoted candidates, 111 hunted, 76 split children, 23 inferred.

## Not quoted

- Front matter: title block, §1 (Status of this document), §2 (Abstract), §3 (Contents), lines 1 to 50.
- §4 (DSig 1.0 Overview), lines 52 to 68: goals, an informal model and design properties; one inferred entry rests on its design properties.
- The review of PICS 1.1 that DSig restates without change: §5 (PICS Architecture) ¶1-2 (lines 72-73) and the label-list syntax and figures of §5.1 (PICS 1.1 labels and label lists). The binding PICS 1.1 text is the pics-1-1-labels record's.
- Figures and examples (fixtures for the examples lane): lines 92-122, 208, 259-265, 288-290, 299-312, 348-352, 415-433, 501-515, 525-528, 543-605.
- §7.3 (The Signature Block Extension), lines 269-274: an overview of what a sigblock carries; its rules are §7.3.1 to §7.3.4.
- Notes about later versions (lines 216, 399), rationale, evaluations, lead-ins and cross-references (for example lines 148, 169, 199, 377, 499) and the narration of examples; each such candidate has its reason in `inferred-candidates.yaml`. The coverage sweep that found R-0300 to R-0318 lists every remaining sentence of §4 to §11 in one of these classes.
- §12 (Acknowledgments), §13 (Reference Materials), §14 (Authors Addresses), §15 (Change History), lines 632 to 685.

## §4 DSig 1.0 Overview

Inferred, not verbatim: R-0001 (what a DSig signature binds). See requirements.yaml.

## §5 PICS Architecture

<!-- q L75 -->
> In DSig 1.0, the notion of content labels and raters is somewhat different. In DSig 1.0 the rater is considered to be a labeler.

R-0300 (none, defines) · hunted

<!-- q L76 -->
> The labeler is making an assertion about an information resource and creating an assertion label.

R-0301 (none, defines) · hunted

<!-- q L77 -->
> By signing an assertion label, the signer explicitly confirms belief in the truth of the statements contained within the label. A signature does not indicate that the signer created the label, only that they believe the statements made within it are valid."

R-0002 (none, defines) · hunted + R-0003 (none, defines) · C-0017

<!-- q L78 -->
> Additional signatures can be added in parallel with existing signatures at any point in time.

R-0004 (none, may) · C-0018

<!-- q L79 "The labeler" .. "DSig label." -->
> The labeler and signer may be, but do not have to be different entities in a DSig label.

R-0005 (none, may) · C-0019

<!-- q L79 "DSig 1.0" .. "the signer(s)." -->
> DSig 1.0 signature labels provide fields for storing information about both the label creator and the signer(s).

R-0302 (none, defines) · hunted

<!-- q L80 -->
> The PICS rating system referenced in the signature label is an assertion system in DSig. The statement in the label (made via the PICS ratings) is an assertion that the labeler is making about the referenced content.

R-0006 (none, defines) · hunted

<!-- q L81 "Additional resource" .. "the label." -->
> Additional resource reference information may be included within the DSig label to help disambiguate the subject of the label.

R-0007 (none, may) · C-0020

<!-- q L81 "The DSig" .. "labeled content." -->
> The DSig resinfo extension is one way of including such information; it allows the label signer to provide cryptographic hashes of the labeled content.

R-0303 (none, may) · hunted

<!-- q L81 "Other private" .. "1.1 specifications." -->
> Other private extension types may also be defined and included in accordance with the PICS 1.1 specifications.

R-0008 (none, may) · C-0021

## §5.1 PICS 1.1 labels and label lists

<!-- q L89 "In DSig" .. "a rating)." -->
> In DSig 1.0, each assertion about an information resource is given in a label. A label consists of a service identifier, options, extensions and an assertion (in PICS 1.1 the assertion is called a rating).

R-0304 (none, defines) · hunted

<!-- q L117 "Each service" .. "label options." -->
> Each service may have service options which are inherited by each label within the scope of the service; service options may be overridden by individual label options.

R-0009 (none, defines) · C-0027 → split: R-0010 (defines), R-0011 (defines)

<!-- q L117 "When a" .. "longer apply." -->
> When a new service is identified in the label list, the options from the previous service no longer apply.

R-0012 (none, defines) · C-0028

<!-- q L124 -->
> In DSig 1.0, we sign individual labels or portions thereof; the details of signing labels are presented below.

R-0013 (none, defines) · hunted

<!-- q L125-126 "PICS defines" .. "single resource." -->
> PICS defines two distinct types of labels, specific and generic: A specific label applies to a single resource.

R-0014 (none, defines) · C-0029

<!-- q L126 "For example," .. "<img> tags." -->
> For example, if a labeled document is in HTML format, the label applies only to the HTML document itself and not to any other documents referenced via hyperlinks or <img> tags.

R-0015 (none, defines) · C-0030

<!-- q L126 "This is" .. "label type." -->
> This is the default label type.

R-0016 (none, defines) · hunted

<!-- q L127 "A generic" .. "the label)." -->
> A generic label (identified by the use of the PICS generic option within the label) applies to any document with a URL that has a particular prefix (the prefix is specified via the PICS for option in the label).

R-0017 (none, defines) · hunted

<!-- q L127 "A generic label for" .. "or directory." -->
> A generic label for a site or directory should only be used if it applies to all the documents in that site or directory.

R-0018 (none, should) · C-0031

<!-- q L127 "The DSig" .. "generic label." -->
> The DSig 1.0 resinfo extension is not meaningful within a generic label.

R-0019 (none, defines) · hunted

## §6.1 Semantics of Embedded Signature Blocks

<!-- q L133-134 -->
> By convention, a DSig signature block itself has the weakest possible semantics, namely "the entity possessing the key that created this signature had access to the secret key used to generate the signature and the signed data at the same time." For DSig 1.0 signature labels, we want somewhat stronger semantics that also includes the semantics of the ratings contained within the label. Thus, by definition a PICS label which includes a DSig sigblock extension has the following semantics: "The entity possessing the secret key that digitally signed this PICS 1.1 label had access to the secret key and the label at the same time and asserts that the statements made within the label are valid"

R-0020 (none, defines) · hunted

## §6.2 Applying PICS to DSig

<!-- q L138 -->
> Following the format given in PICS Label Distribution Label Syntax and Communication Protocols Version 1.1 we now review each of the PICS 1.1 options; giving appropriate usage rules for applying them within the context of DSig 1.0 Signature Labels.

R-0305 (none, defines) · hunted

<!-- q L141 -->
> at quoted-PICS-ISO-date

R-0306 (none, defines) · hunted

<!-- q L142 "The last" .. "made ." -->
> The last modification date of the information resource to which this assertion applies, at the time the assertion was made .

R-0021 (none, defines) · hunted

<!-- q L142 "This can" .. "resinfo extension." -->
> This can serve as a less expensive, but less reliable, alternative to the DSig 1.0 resinfo extension.

R-0022 (none, may) · hunted

<!-- q L143-145 "MIC-md5" .. "be ignored." -->
> MIC-md5 "Base64-string" -or- md5 "Base64-string" This option is not used in DSig 1.0. If this option is present in a DSig 1.0 label, it should be ignored.

R-0023 (none, should) · C-0033 → split: R-0307 (defines), R-0024 (defines), R-0025 (should)

<!-- q L145 "Further, it" .. "of signing." -->
> Further, it should be removed from the label for the purposes of signing.

R-0026 (none, should) · C-0034

<!-- q L145 "This option has" .. "resinfo extension." -->
> This option has been superceded by the DSig 1.0 resinfo extension.

R-0308 (none, defines) · hunted

<!-- q L147 -->
> by quotedname

R-0309 (none, defines) · hunted

<!-- q L148 "An identifier" .. "particular label." -->
> An identifier for the person or entity who was responsible for creating this particular label.

R-0027 (none, defines) · hunted

<!-- q L148 "The contents" .. "by field." -->
> The contents of the by field are not restricted by the DSig 1.0 specification; it is common practice in PICS usage to include a name or e-mail address in the string value of the by field.

R-0028 (none, may) · hunted

<!-- q L148 "Within DSig" .. "the signer(s)." -->
> Within DSig 1.0, the by field is considered informational only; the by option name need not be the same as that of the signer(s).

R-0029 (none, defines) · C-0035 → split: R-0030 (defines), R-0031 (may)

<!-- q L149 -->
> for quotedURL

R-0310 (none, defines) · hunted

<!-- q L150 "The URL" .. "assertion applies." -->
> The URL (or prefix string of a URL) of the information resource to which this assertion applies.

R-0032 (none, defines) · hunted

<!-- q L150 "This option" .. "other cases." -->
> This option is required for generic labels and in certain other cases (see "Requesting Labels Separately," PICS Label Distribution Label Syntax and Communication Protocols Version 1.1); it is optional in other cases.

R-0033 (none, must) · C-0036

<!-- q L150-153 "The for" .. "for option." -->
> The for option is valid as both a service and label option in a label list. generic boolean -or- gen boolean If this option is set to true, the label can be applied to any URL starting with the prefix given in the for option.

R-0034 (none, defines) · C-0037 → split: R-0035 (may), R-0311 (defines), R-0036 (defines)

<!-- q L153 "By default," .. "is false." -->
> By default, this option is false.

R-0037 (none, defines) · hunted

<!-- q L153 "All generic" .. "for option." -->
> All generic labels must also include the for option.

R-0038 (none, must) · C-0039

<!-- q L153 "A generic" .. "label exists)." -->
> A generic label should not be created unless it can be legitimately applied to all documents whose URL begins with the prefix specified in the for option (even if a more specific label exists).

R-0039 (none, should) · C-0040

<!-- q L153-155 "If the" .. "was created." -->
> If the generic option is used with a true value, the DSig 1.0 resinfo extension can not be used because there will not be a specific information resource to hash. on quoted-PICS-ISO-date The date on which this label was created.

R-0040 (none, must) · C-0041 → split: R-0041 (must), R-0312 (defines), R-0042 (defines)

<!-- q L155-157 "This may" .. "of signing." -->
> This may be different than the date the label was signed (which may be included within the DSig 1.0 sigblock extension). signature-RSA-MD5 "Base64-string" This option is not used in DSig 1.0. If this option is present in a DSig 1.0 label it should be ignored and removed from the label for the purposes of signing.

R-0043 (none, should) · C-0042 → split: R-0044 (may), R-0313 (defines), R-0045 (defines), R-0046 (should)

Inferred, not verbatim: R-0047 (removing MIC-md5 and signature-RSA-MD5 when rebuilding the signed form). See requirements.yaml.

<!-- q L157 "This option has" .. "sigblock extension." -->
> This option has been replaced with the DSig 1.0 sigblock extension.

R-0314 (none, defines) · hunted

<!-- q L158-159 -->
> until quoted-PICS-ISO-date -or- exp quoted-PICS-ISO-date

R-0315 (none, defines) · hunted

<!-- q L160 -->
> The date on which the label expires (how long the label is good for).

R-0048 (none, defines) · hunted

<!-- q L161-166 "Other information." .. "current one." -->
> Other information. comment quotedname Information for humans who may see the label; no associated semantics. complete-label quotedURL -or- full quotedURL De-referencing this URL returns a complete label that can be used in place of the current one.

R-0049 (none, defines) · C-0043 → split: R-0316 (defines), R-0050 (defines), R-0317 (defines), R-0051 (defines)

<!-- q L166 "The complete" .. "as possible." -->
> The complete label has values for as many attributes as possible.

R-0318 (none, should) · hunted

<!-- q L166 "When the" .. "one label." -->
> When the URL is de-referenced it returns an item of type application/pics-labels that contains a label list with exactly one label.

R-0052 (none, must) · C-0045

<!-- q L167-168 -->
> extension (optional quotedURL data*) -or- extension (mandatory quotedURL data*)

R-0053 (none, defines) · hunted

<!-- q L169 "To avoid" .. "a quotedURL." -->
> To avoid duplication of extension names, each extension is identified by a quotedURL.

R-0054 (none, defines) · C-0048

<!-- q L169 "The URL" .. "the extension." -->
> The URL is de-referencable, yielding a human-readable description of the extension.

R-0055 (none, defines) · hunted

<!-- q L169 "If the" .. "been supplied." -->
> If the extension is optional then software which does not understand the extension can simply ignore it; if the extension is mandatory then software which does not understand the extension should act as though no label had been supplied.

R-0056 (none, should) · C-0049 → split: R-0057 (may), R-0058 (should)

<!-- q L169 "Each item" .. "syntax below." -->
> Each item of data must be one of a fixed set of simple-to-parse data types as specified in the detailed syntax below.

R-0059 (none, must) · C-0050

## §7 DSig Extensions

<!-- q L173 "To do" .. "that resource." -->
> To do this in a secure fashion, the signed label must have a cryptographic connection to that resource.

R-0060 (none, must) · C-0051

<!-- q L174 "The sigblock" .. "to certificates." -->
> The sigblock extension may contain one or more signatures using any cryptographic algorithm; in addition, a sigblock may optionally include information in the form of certificates or links to certificates.

R-0061 (none, may) · C-0052 → split: R-0062 (may), R-0063 (may)

<!-- q L175 "A DSig" .. "1.1 label." -->
> A DSig 1.0 Signature Label is a standard PICS 1.1 label.

R-0064 (none, defines) · hunted

<!-- q L175 "The DSig" .. "as needed." -->
> The DSig extensions resinfo and sigblock are both optional and can be used as needed.

R-0065 (none, may) · C-0053

<!-- q L175 "A PICS" .. "sigblock extension." -->
> A PICS 1.1 label is only considered a DSig 1.0 Signature Label when it contains a sigblock extension.

R-0066 (none, defines) · C-0054

<!-- q L176-182 "By convention," .. "zero or more occurrences of a." -->
> By convention, a? a or nothing; optional a. a+ one or more occurrences of a. a* zero or more occurrences of a.

R-0067 (none, defines) · C-0055

<!-- q L183 "Quoted strings" .. "case insensitive." -->
> Quoted strings are case sensitive but other literal elements are case insensitive.

R-0068 (none, defines) · hunted

<!-- q L183 "Multiple contiguous" .. "quoted strings." -->
> Multiple contiguous space characters are be treated as though they were a single space character except in quoted strings.

R-0069 (none, defines) · hunted

## §7.1 URLs as identifiers

<!-- q L187 "Within the" .. "signature type." -->
> Within the DSig 1.0 sigblock and resinfo extensions, URLs are used as identifiers to indicate a particular hashing algorithm, certificate type or signature type.

R-0070 (none, defines) · C-0056

<!-- q L187-191 "Specifically, they" .. "valid URL." -->
> Specifically, they are used as: hash algorithm identifiers certificate family identifiers, and signature suite identifiers To ensure the uniqueness of identifiers, the identifier must be a valid URL.

R-0071 (none, must) · C-0057 → split: R-0072 (must)

<!-- q L192 "Since the" .. "a document." -->
> Since the identifier is a URL, it must, when resolved, yield a a document.

R-0073 (none, must) · C-0059

<!-- q L192-197 "We recommend" .. "be provided." -->
> We recommend the returned document: be available at least in HTML format; identify the entity which created and maintains the identifier; describe the specifics of the algorithms and encodings, or provide a link to another document which does so; and be available in multiple languages, either through an existing negotiation mechanism or through links to alternate language versions We require that such identifier description documents always be provided.

R-0074 (none, must) · C-0060 → split: R-0075 (should), R-0076 (must)

<!-- q L198 -->
> Any incompatible change in an identifier should be accomplished by creating an entirely new identifier URL.

R-0077 (none, should) · C-0061

<!-- q L199 "Of course," .. "only these." -->
> Of course, DSig 1.0 implementations are not restricted to using these or only these.

R-0078 (none, may) · C-0062

<!-- q L199 "To provide" .. "Appendix 3." -->
> To provide a base level of interoperability, all DSig 1.0 implementations are required to implement the signature suites listed in Appendix 3.

R-0079 (none, must) · C-0063

Inferred, not verbatim: R-0080 (comparing identifiers). See requirements.yaml.

## §7.2 Resource Reference Information Extension

<!-- q L203 "Specifically, the" .. "the label." -->
> Specifically, the resinfo extension provides a mechanism for including cryptographic checksums (hashes), in any named cryptographic algorithm, to the label.

R-0081 (none, may) · hunted

<!-- q L203 "These hashes" .. "was made." -->
> These hashes provide a means for the receiver of the label to determine if the information resource they have is the same as the one about which the assertion was made.

R-0082 (none, defines) · hunted

<!-- q L204 "The resinfo" .. "specific resource." -->
> The resinfo extension is associated with a specific resource.

R-0083 (none, defines) · C-0064

<!-- q L204 "This resource" .. "request, etc.)." -->
> This resource may be identified by the for option or may be implied by the context of the label (in the resource, delivered in the HTTP header with the resource, returned by a label bureau based on a request, etc.).

R-0084 (none, may) · C-0065

<!-- q L205 "In the" .. "label option." -->
> In the structure of a PICS label, the resinfo extension can be a service option and/or a label option.

R-0085 (none, may) · C-0066

<!-- q L205 "It functions" .. "label option." -->
> It functions identically to any other option with respect to inheritance within a service section from service option to label option.

R-0086 (none, defines) · hunted

<!-- q L205 "A single" .. "be valid." -->
> A single document can have many URLs; the URL used to retrieve a document may differ from the URL in the for option of a label that accompanies the document, but the document retrieved must be the same document or the hash(s) contained in the resinfo extension will not be valid.

R-0087 (none, must) · C-0067 → split: R-0088 (may), R-0089 (must)

<!-- q L206 -->
> Structurally, resinfo contains one or more hashes of the information resource; each hash includes a hash algorithm identifier, the actual hash of the resource and (optionally) the date the hash was computed.

R-0090 (none, defines) · C-0068

<!-- q L210 "The hash" .. "was computed." -->
> The hash algorithm identifier is a quoted URL identifier as defined above. It identifies the specific hashing algorithm by which the following hash was computed.

R-0091 (none, defines) · hunted

<!-- q L210 "The actual" .. "encoded string." -->
> The actual hash is given as a quoted base64 encoded string.

R-0092 (none, defines) · hunted

<!-- q L212 "The resinfo" .. "service option." -->
> The resinfo extension can either be a service option or a label option. If both are present, the extension given as a label option takes precedence over the service option.

R-0093 (none, defines) · hunted

<!-- q L212 "Thus, an" .. "be used." -->
> Thus, an equivalent standalone label will have at most one resinfo extension and that extension will be the extension given as the label option for that label unless none is present, in which case the extension given as a service option will be used.

R-0094 (none, defines) · hunted

<!-- q L212 "If neither" .. "resinfo extension." -->
> If neither is present, the equivalent standalone label will have no resinfo extension.

R-0095 (none, defines) · hunted

Inferred, not verbatim: R-0096 (number of resinfo extensions per level). See requirements.yaml.

<!-- q L213 "A resinfo" .. "information resource." -->
> A resinfo extension can contain multiple hashes of the information resource.

R-0097 (none, may) · C-0069

<!-- q L213 "Each must" .. "one label." -->
> Each must necessarily use a different hash algorithm; it is not valid to label multiple versions of a single document by including multiple, distinct hashes in one label.

R-0098 (none, must) · C-0070 → split: R-0099 (must), R-0100 (must)

<!-- q L214 "The resinfo" .. "extension." -->
> The resinfo extension is an "optional" extension.

R-0101 (none, defines) · C-0071

<!-- q L214 "Optional implies" .. "the label." -->
> Optional implies that even if the processing software does not understand the extension, it should still process the label.

R-0102 (none, should) · C-0072

<!-- q L215 "The resinfo" .. "1.1 label." -->
> The resinfo extension is not valid in a generic PICS 1.1 label.

R-0103 (none, must) · C-0073

<!-- q L215 "It is" .. "1.1 label." -->
> It is only valid within a specific (non-generic) PICS 1.1 label.

R-0104 (none, must) · C-0074

<!-- q L216 "Resinfo is" .. "be created." -->
> Resinfo is not extensible: In DSig 1.0, if other disambiguating or differentiating information is needed, a separate extension will need to be created.

R-0105 (none, must) · C-0075

Inferred, not verbatim: R-0106 (checking resinfo against the resource). See requirements.yaml.

## §7.2.1 Detailed Syntax of the resinfo Extension in a PICS 1.1 Label

<!-- q L220-232 -->
> resinfo-extension ::= 'extension ( optional ' '"http://www.w3.org/TR/1998/REC-DSig-label/resinfo-1_0"' resinfo-data+ ')' resinfo-data ::= '(' HashAlgoID resource-hash hash-date? ')' HashAlgoID ::= quotedURL quotedURL ::= '"' URL '"' resource-hash ::= '"base64-string"' hash-date ::= quoted-ISO-date quoted-ISO-date ::= '"' YYYY sep MM sep DD 'T' hh ':' mm[':' ss['.' f+]] Stz '"' based on the PICS-defined ISO 8601:1988 date and time format, restricted to the specific form described here: sep ::= '.' | '-' YYYY ::= four-digit year MM ::= two-digit month (01=January, etc.)

R-0107 (none, defines) · C-0077 → split: R-0108 (defines), R-0109 (defines), R-0110 (defines), R-0111 (defines), R-0112 (defines), R-0113 (defines)

<!-- q L227-240 -->
> quoted-ISO-date ::= '"' YYYY sep MM sep DD 'T' hh ':' mm[':' ss['.' f+]] Stz '"' based on the PICS-defined ISO 8601:1988 date and time format, restricted to the specific form described here: sep ::= '.' | '-' YYYY ::= four-digit year MM ::= two-digit month (01=January, etc.) DD ::= two-digit day of month (01 through 31) hh ::= two digits of hour (00 through 23) (am/pm NOT allowed) mm ::= two digits of minute (00 through 59) ss ::= two digits of second (00 through 59), optional f ::= digit(s) of fractions of second, optional S ::= sign of time zone offset from UTC ('+' or '-') tz ::= four digit amount of offset from UTC (e.g., 1512 means 15 hours and 12 minutes)

R-0114 (none, defines) · hunted

<!-- q L233-243 -->
> DD ::= two-digit day of month (01 through 31) hh ::= two digits of hour (00 through 23) (am/pm NOT allowed) mm ::= two digits of minute (00 through 59) ss ::= two digits of second (00 through 59), optional f ::= digit(s) of fractions of second, optional S ::= sign of time zone offset from UTC ('+' or '-') tz ::= four digit amount of offset from UTC (e.g., 1512 means 15 hours and 12 minutes) For example, "1994-11-05T08:15-0500" is a valid quoted-ISO-date denoting November 5, 1994, 8:15 am, US Eastern Standard Time Notes:

R-0115 (none, defines) · C-0078 → split: R-0116 (defines)

<!-- q L245-248 "DSig requires" .. "here, Except:" -->
> DSig requires precisely the syntax described here -- neither the time nor the time zone may be omitted, none of the alternate ISO formats are permitted, and the punctuation must be as specified here, Except:

R-0117 (none, must) · C-0080

<!-- q L251 "DSig supports" .. "both syntaxes." -->
> DSig supports both syntaxes.

R-0118 (none, must) · C-0083

<!-- q L254 -->
> base64-string ::= as defined in RFC-1521.

R-0119 (none, defines) · hunted

<!-- q L255 -->
> URL ::= as defined in RFC-1738.

R-0120 (none, defines) · C-0085

## §7.3.1 Format Specification

<!-- q L278-280 -->
> A Signature Block consists of Attribution Information, and one or more Signatures.

R-0121 (none, defines) · hunted

<!-- q L281-282 "Usage notes:" .. "extension." -->
> Usage notes: The sigblock extension is an "optional" extension.

R-0122 (none, defines) · C-0092

<!-- q L282 "Optional implies" .. "the label." -->
> Optional implies that even if the processing software does not understand the extension, it should still process the label.

R-0123 (none, should) · C-0093

<!-- q L282 "Whether information" .. "management question." -->
> Whether information contained within an unsigned or unverified label should be used is a trust management question.

R-0124 (none, defines) · C-0095

<!-- q L283 -->
> The sigblock extension is valid in both generic and specific (non-generic) PICS 1.1 labels.

R-0125 (none, may) · C-0096

<!-- q L284 -->
> The sigblock extension is extensible via signature suites.

R-0126 (none, defines) · hunted

<!-- q L285 -->
> A sigblock extension is only valid as a label option.

R-0127 (none, must) · C-0097

Inferred, not verbatim: R-0128 (result of verification). See requirements.yaml.

## §7.3.2 Attribution Information

<!-- q L294 "The Attribution" .. "the label." -->
> The Attribution Information section contains self-verifiable information related to the creation of the digital signature on the label.

R-0129 (none, defines) · C-0099

<!-- q L294 "In particular," .. "included here." -->
> In particular, cryptographic certificates asserting identity, authorization or other capabilities may be included here.

R-0130 (none, may) · C-0100

<!-- q L294 "Certificates may" .. "be included." -->
> Certificates may be directly embedded within the Attribution Information section of the sigblock extension, or URLs pointing to certificates may be included.

R-0131 (none, may) · C-0101

<!-- q L294 "Attribution Information is" .. "the label." -->
> Attribution Information is not required (i.e. this section of the extension may be empty), in which case trust management systems must depend on other information sources when interpreting the label.

R-0132 (none, may) · C-0102 → split: R-0133 (may), R-0134 (must)

<!-- q L294 "Furthermore, the" .. "the label." -->
> Furthermore, the information provided herein may or may not be used by the trust management system in processing the label.

R-0135 (none, may) · C-0103

<!-- q L295 "Attribution Information" .. "the application." -->
> Attribution Information supports any certificate format; the types of certificates included will depend on the public key infrastructure used by the application.

R-0136 (none, may) · hunted

<!-- q L295 "Certificate format" .. "defined above." -->
> Certificate format is indicated by the certificate family identifier, a quoted URL identifier as defined above.

R-0137 (none, defines) · hunted

<!-- q L295 "This certificate" .. "to follow." -->
> This certificate family identifier, when dereferenced, provides information on the format of the data to follow.

R-0138 (none, defines) · hunted

<!-- q L296 "None of" .. "be self-verifying." -->
> None of the information contained within the Attribution Information section is signed by the label's signature because certificates themselves are expected to be self-verifying.

R-0139 (none, defines) · hunted

<!-- q L296 "(More precisely," .. "signature option.)" -->
> (More precisely, none of the information within the entire sigblock extension, including the Attribution Information section, contributes to the hash of the label that is signed as part of the signature option.)

R-0140 (none, defines) · hunted

<!-- q L296 "Thus, applications" .. "be replaced)." -->
> Thus, applications may augment the contents of the Attribution Information section without invalidating the signature on the label (e.g. newly-discovered certificates may be included in the Attribution Information section as they are found, or an expired certificate may be replaced).

R-0141 (none, may) · C-0104

Inferred, not verbatim: R-0142 (certificates in AttribInfo). See requirements.yaml.

## §7.3.3 Signatures

<!-- q L316 "The Signature" .. "signature data." -->
> The Signature section of the sigblock extension contains the actual digital signature data.

R-0143 (none, defines) · C-0105

<!-- q L316 "Each Signature" .. "are desired." -->
> Each Signature section contains exactly one signature; multiple Signature sections may be included in the sigblock extension when multiple, parallel signatures are desired.

R-0144 (none, defines) · C-0106 → split: R-0145 (must), R-0146 (may)

<!-- q L316-318 "The syntax" .. "SignatureSuite SigData+)" -->
> The syntax of the Signature section is: ( "Signature" SignatureSuite SigData+)

R-0147 (none, defines) · hunted

<!-- q L320 "Instead, we" .. "representation format." -->
> Instead, we introduce the concept of "signature suites," which bundle together certain hashing algorithms, signature algorithms and representation format.

R-0148 (none, defines) · hunted

<!-- q L320 "Each digital" .. "be parsed." -->
> Each digital signature includes a signature suite identifier (a quoted URL identifier as defined above) that tells applications how the signature was generated and how it should be parsed.

R-0149 (none, defines) · C-0109

<!-- q L321-323 -->
> Each signature suite: specifies the algorithms that have been used for creating the signature, and defines the content of any subsequent SigData.

R-0150 (none, must) · C-0110

<!-- q L324 "Signature suites" .. "suite URL." -->
> Signature suites have complete control over the contents of the SigData immediately following the signature suite URL.

R-0151 (none, may) · hunted

<!-- q L324 "The format" .. "signature suite." -->
> The format of this data must satisfy the SigData portion of the BNF; beyond that requirement, the format of the data is governed by the definition given in the signature suite.

R-0152 (none, must) · C-0111

<!-- q L324 "DSig 1.0" .. "to define." -->
> DSig 1.0 does define two hash algorithms and two signature suites for interoperability; see Appendix 3. Implementations must implement these four algorithms in addition to any others they may wish to define.

R-0153 (none, must) · C-0112 → split: R-0154 (defines), R-0155 (must)

Inferred, not verbatim: R-0156 (verifying a Signature). See requirements.yaml.

## §7.3.4 Common SigData fields

<!-- q L328 "For example," .. "digital signature." -->
> For example, signature suites need to include the actual cryptographic data that constitutes a digital signature.

R-0157 (none, must) · C-0113

<!-- q L328 "These string" .. "this specification." -->
> These string tokens are reserved words in the sense that any signature suite that uses SigData field identified by these tokens must do so in a manner consistent with this specification.

R-0158 (none, must) · C-0115

## §7.3.4.1 Keyholder tokens: information about keys related to the signature

<!-- q L332 "The" .. "corresponding signature." -->
> The "Keyholder"-type SigData fields of a signature provides information about the key that was used to create the corresponding signature.

R-0159 (none, defines) · hunted

<!-- q L332-336 "There are" .. ")." -->
> There are four common ways to uniquely specify a particular key; each has its own identifying token: Provide the public key directly ("ByKey"); Provide a hash (or fingerprint) of the public key ("ByHash"); Provide some name that is associated with the public key, such as an X.509 "distinguished name" or the UserID string of a PGP key ("ByName"); or Provide the name of a certifying authority (CA) and information, which identifies the desired key to the CA ("ByCert").

R-0160 (none, defines) · C-0118

<!-- q L337 -->
> To be useful, the information identifying the signing key will lead the application to corresponding certificates in the Attribution Information section (if any) or provide the starting point for fetching certificates from remote sources.

R-0161 (none, should) · hunted

## §7.3.4.2 "ByKey"

<!-- q L342 -->
> The token "ByKey" identifies the value that follows as the key that should be used to validate the signature (or sufficient information to generate that key locally).

R-0162 (none, defines) · C-0119

<!-- q L344 -->
> ( "ByKey" <Key-Value, SignatureSuite dependent> )

R-0163 (none, defines) · hunted

<!-- q L346 "The format" .. "suite document." -->
> The format of the included key necessarily depends on the particular signature suite used and must be specified in the signature suite document.

R-0164 (none, must) · C-0120

## §7.3.4.3 "ByHash"

<!-- q L356 -->
> The token "ByHash" identifies the value that follows as the hash of the key that should be used to validate the signature.

R-0165 (none, defines) · C-0121

<!-- q L358 -->
> ("ByHash" "base-64-encoded-hash-of-key" )

R-0166 (none, defines) · hunted

<!-- q L360 -->
> Details on how the hash for a key is generated is a property of individual signature suites.

R-0167 (none, defines) · hunted

## §7.3.4.4 "ByName"

<!-- q L364 "The token" .. "public key." -->
> The token "ByName" identifies the value that follows as a name (or other reference) that may be used to identify the corresponding public key.

R-0168 (none, may) · C-0122

<!-- q L364 "The name" .. "key infrastructure." -->
> The name that should be provided depends on the relevant public key infrastructure.

R-0169 (none, should) · C-0123

<!-- q L366 -->
> ( "ByName" "Name-as-string-value" )

R-0170 (none, defines) · hunted

## §7.3.4.5 "ByCert"

<!-- q L370 "The token" .. "that CA." -->
> The token "ByCert" identifies the value that follows as containing the name of a certifying authority (CA) and the serial number a relevant certificate issued by that CA.

R-0171 (none, defines) · hunted

<!-- q L370 "The name" .. "certification infrastructure." -->
> The name given for the CA depends on the naming conventions of the relevant public key or certification infrastructure.

R-0172 (none, defines) · hunted

<!-- q L372 -->
> ( "ByCert" ( "CA-Name-as-string-value" <CA-Serial-No.> ) )

R-0173 (none, defines) · hunted

## §7.3.4.6 The "On" token: Time of Signature generation

<!-- q L376 "The token" .. "was created.)" -->
> The token "On" identifies the value that follows as the time the label's signature was generated. (This option is distinct from the PICS 1.1 label option "on" which indicates the time at which the label itself was created.)

R-0174 (none, defines) · hunted

<!-- q L376 "We recommend" .. "signature suites." -->
> We recommend using this standard element in all signature suites.

R-0175 (none, should) · hunted

<!-- q L377 "The time" .. "a quoted-ISO-Date." -->
> The time that the signature was created is encoded as a quoted-ISO-Date.

R-0176 (none, defines) · C-0124

<!-- q L379 -->
> ("on" quoted-ISO-Date)

R-0177 (none, defines) · hunted

<!-- q L381 "Notice that" .. "signature itself." -->
> Notice that the "on" time is advisory only to applications verifying the digital signature; as this section is part of the entire sigblock extension it is not cryptographically protected by the signature itself.

R-0178 (none, defines) · C-0125

<!-- q L381 "(The contents" .. "the signature.)" -->
> (The contents of the sigblock do not contribute to the hash of the label that is signed by the signature.)

R-0179 (none, defines) · C-0126

<!-- q L381 "If a" .. "canonicalized label." -->
> If a cryptographically-protected date is desired, the correct way to implement it is to include the date within another PICS label extension; that extension may then contribute to the hash of the canonicalized label.

R-0180 (none, should) · C-0127

## §7.3.4.7 The "include" and "exclude" tokens: modifying the canonicalized form of the label

<!-- q L385 "If an" .. "label list." -->
> If an application wishes to transmit both signed and unsigned information in a label the suggested method for doing so is to generate two labels (one signed, one unsigned) and send both labels as a PICS label list.

R-0181 (none, should) · hunted

<!-- q L385 "If the" .. "that functionality:" -->
> If the signature suite permits signatures over partial contents of labels, the "include" and "exclude" tokens provide that functionality:

R-0182 (none, may) · hunted

<!-- q L387-388 -->
> ( "exclude" field-list ) ( "include" field-list )

R-0183 (none, defines) · hunted

<!-- q L390 "The" .. "those listed." -->
> The "include" and "exclude" SigData fields modify the default behavior of the label canonicalizer. "include" indicates that only the fields listed are included in the signature, "exclude" indicates that all fields are included in the signature except those listed.

R-0184 (none, defines) · hunted + R-0185 (none, defines) · C-0129

<!-- q L390 "Before a" .. "canonicalization process." -->
> Before a label is signed, it is put into canonical form; the section "Creating an equivalent standalone label" below describes in detail the canonicalization process.

R-0186 (none, must) · hunted

<!-- q L390 "PICS labels" .. "same way." -->
> PICS labels have many semantically-equivalent forms yet these forms yield distinct hashes, so it is important that signing and verifying applications canonicalize labels in the same way.

R-0187 (none, must) · hunted

<!-- q L390 "After the" .. "is present." -->
> After the equivalent standalone label has been generated following the default canonicalization rules, individual label options may be dropped if an "include" or "exclude" option is present.

R-0188 (none, may) · C-0130

<!-- q L390 "If an" .. "are removed from the canonicalized label." -->
> If an "include" option is present, any field not listed in the field-list is removed from the canonicalized label. If an "exclude" option is present, all fields listed in the field-list are removed from the canonicalized label.

R-0189 (none, defines) · hunted + R-0190 (none, defines) · hunted

<!-- q L390 "At most" .. "option." -->
> At most one "include" or "exclude"; field may appear; it is an error to have both an "include" and an "exclude" option.

R-0191 (none, must) · C-0131 → split: R-0192 (must), R-0193 (must)

<!-- q L391 "The value" .. "and extensions." -->
> The value associated with an "include" or "exclude" option (the "field-list") is a list of label fields to be included or excluded in the canonicalized form. There are three types of fields in PICS 1.1 labels: options, ratings transmit/value pairs, and extensions.

R-0194 (none, defines) · hunted

<!-- q L393 -->
> field-list ::= '(' option-list? ratings-list? extension-list? ')'

R-0195 (none, defines) · hunted

<!-- q L394 -->
> option-list ::= '(' "options" <options>* ')'

R-0196 (none, defines) · hunted

<!-- q L395 -->
> ratings-list ::= '(' "ratings" <ratings>* ')'

R-0197 (none, defines) · hunted

<!-- q L396 -->
> extension-list ::= '(' "extensions" <quoted-URL>* ')'

R-0198 (none, defines) · hunted

<!-- q L398 "A field-list" .. "associated data." -->
> A field-list is simply at most, one each of: option-list, ratings-list and extension-list, with their associated data.

R-0199 (none, defines) · hunted

<!-- q L398 "An option-list" .. ")." -->
> An option-list is a list of PICS 1.1 label option names (e.g. "for" or "by").

R-0200 (none, defines) · hunted

<!-- q L398 "A ratings-list" .. "rating service)." -->
> A ratings-list is a list of PICS 1.1 ratings service transmit-names (e.g. "suds" in the example "Good Clean Fun" rating service).

R-0201 (none, defines) · hunted

<!-- q L398 "An extension-list" .. "label extension." -->
> An extension-list is a list of quoted-URLs where each quoted-URL uniquely identifies a particular PICS 1.1 label extension.

R-0202 (none, defines) · hunted

Inferred, not verbatim: R-0203 (reading include or exclude before removing the sigblock). See requirements.yaml.

Inferred, not verbatim: R-0204 (matching field-list entries to label fields). See requirements.yaml.

Inferred, not verbatim: R-0205 (what include keeps). See requirements.yaml.

Inferred, not verbatim: R-0206 (partial signatures and the suite). See requirements.yaml.

## §7.3.4.8 The "SigCrypto" token: signature cryptographic data

<!-- q L403 "The" .. "signature itself." -->
> The "SigCrypto" token identifies the SigData field that contains the cryptographic data that is the signature itself.

R-0207 (none, defines) · C-0133

<!-- q L403 "The format" .. "signature suites." -->
> The format and contents of this field are entirely specified by particular signature suites.

R-0208 (none, defines) · hunted

## §7.3.5 Hashing

<!-- q L407 "DSig 1.0" .. "section below)." -->
> DSig 1.0 therefore specifies how a PICS 1.1 label is converted into a unique, canonicalized form which does not include the sigblock extension (this process is explained in the Signing section below).

R-0209 (none, defines) · C-0134

<!-- q L407 "This canonicalized" .. "signature algorithm." -->
> This canonicalized label is the input to the signature suite's signature algorithm.

R-0210 (none, must) · hunted

<!-- q L407 "The signature" .. "standalone label." -->
> The signature algorithm may require or accept other inputs in addition to the contents of the equivalent standalone label.

R-0211 (none, may) · C-0135

## §7.4 Parallel and cascaded signatures

<!-- q L411 "Multiple parallel" .. "sigblock extension." -->
> Multiple parallel signatures on the same PICS 1.1 label may be created simply by including several "Signature" fields within the sigblock extension.

R-0212 (none, may) · C-0137

<!-- q L411 "Cascaded signatures" .. "signature label." -->
> Cascaded signatures (signatures on signatures) are not supported within a single DSig signature label.

R-0213 (none, must) · hunted

<!-- q L411 "To create" .. "signature label." -->
> To create a cascaded signature, a DSig signature label may be signed using another DSig signature label.

R-0214 (none, may) · C-0138

Inferred, not verbatim: R-0215 (one sigblock per label). See requirements.yaml.

Inferred, not verbatim: R-0216 (parallel signatures are independent). See requirements.yaml.

## §7.4.2 Detailed Syntax of the sigblock Extension in a PICS 1.1 Label

<!-- q L437 "Note: This" .. "1.1 datum." -->
> Note: This extension is not a valid PICS 1.1 extension because Base64 encoding uses a '/' which cannot be represented as a PICS 1.1 datum.

R-0217 (none, defines) · C-0140

<!-- q L439-467 "SignatureExtension ::=" .. "::= [sign]unsignedInt['.'" -->
> SignatureExtension ::= 'extension ( optional' SigBlockURL AttributionInfo Signature* ')' SigBlockURL ::= '"http://www.w3.org/TR/1998/REC-DSig-label/sigblock-1_0"' AttributionInfo ::= '(' '"AttribInfo"' Certificate* ')' Certificate ::= '(' CertificateFamilyID CertificateData ')' CertificateFamilyID ::= quotedUrl CertificateData ::= quotedBase64String | quotedUrl Signature ::= '( "Signature"' SignatureSuiteID SigData+ ')' SigData ::= '(' SigTokenString SigInfo ')' SigTokenString ::= quotedName SigInfo ::= SigData | quotedURL | quoted-ISO-date | quotedBase64String | quotedName | number | '(' SigInfo+ ')' SignatureSuiteID ::= quotedUrl quotedURL ::= '"' URL '"' URL ::= as defined by RFC-1738. quotedBase64String ::= '"' base64String '"' base64String ::= as defined in RFC-1521. alpha ::= 'A' | .. | 'Z' | 'a' | .. | 'z' digit ::= '0' | .. | '9' quotedName ::= '"' ( urlChar | ' ')+ '"' urlChar ::= alphaNumPM | '.' | '$' | ',' | ';' | ':' | '&' | '=' | '?' | '!' | '*' | '~' | '@' | '#' | '_' | '(' | ')' | '/' | '%' hex hex ; Note: Use the "%" escape technique to insert ; single or double quotation marks within a URL alphaNumPM ::= alpha | digit | sign hex ::= digit | 'A' | .. | 'F' | 'a' | .. | 'f' sign ::= '+' / '-' number ::= [sign]unsignedInt['.'

R-0218 (none, defines) · C-0142 → split: R-0219 (defines), R-0220 (defines), R-0221 (defines), R-0222 (defines), R-0223 (defines), R-0224 (defines), R-0225 (defines), R-0226 (defines), R-0227 (defines), R-0228 (defines), R-0229 (defines), R-0230 (defines), R-0231 (defines), R-0232 (defines), R-0233 (defines), R-0234 (defines), R-0235 (defines), R-0236 (defines), R-0237 (defines), R-0238 (defines), R-0239 (defines), R-0240 (defines)

<!-- q L467 -->
> number ::= [sign]unsignedInt['.' [unsignedInt]]

R-0241 (none, defines) · hunted

<!-- q L468 -->
> unsignedInt ::= digit+

R-0242 (none, defines) · hunted

<!-- q L469-482 -->
> quoted-ISO-date ::= '"' YYYY sep MM sep DD 'T' hh ':' mm[':' ss['.' f+]] Stz '"' based on the PICS-defined ISO 8601:1988 date and time format, restricted to the specific form described here: sep ::= '.' | '-' YYYY ::= four-digit year MM ::= two-digit month (01=January, etc.) DD ::= two-digit day of month (01 through 31) hh ::= two digits of hour (00 through 23) (am/pm NOT allowed) mm ::= two digits of minute (00 through 59) ss ::= two digits of second (00 through 59), optional f ::= digit(s) of fractions of second, optional S ::= sign of time zone offset from UTC ('+' or '-') tz ::= four digit amount of offset from UTC (e.g., 1512 means 15 hours and 12 minutes)

R-0243 (none, defines) · hunted

<!-- q L475-485 -->
> DD ::= two-digit day of month (01 through 31) hh ::= two digits of hour (00 through 23) (am/pm NOT allowed) mm ::= two digits of minute (00 through 59) ss ::= two digits of second (00 through 59), optional f ::= digit(s) of fractions of second, optional S ::= sign of time zone offset from UTC ('+' or '-') tz ::= four digit amount of offset from UTC (e.g., 1512 means 15 hours and 12 minutes) For example, "1994-11-05T08:15-0500" is a valid quoted-ISO-date denoting November 5, 1994, 8:15 am, US Eastern Standard Time Notes:

R-0244 (none, defines) · C-0143 → split: R-0245 (defines)

<!-- q L487-490 "DSig requires" .. "here, Except:" -->
> DSig requires precisely the syntax described here -- neither the time nor the time zone may be omitted, none of the alternate ISO formats are permitted, and the punctuation must be as specified here, Except:

R-0246 (none, must) · C-0145

<!-- q L493 "DSig supports" .. "both syntaxes." -->
> DSig supports both syntaxes.

R-0247 (none, must) · C-0148

## §8 Signing

<!-- q L499 "Since even" .. "a list." -->
> Since even a single DSig 1.0 signature label must be represented as a PICS 1.1 label list, it is important to understand the structure of such a list.

R-0248 (none, must) · C-0150

## §8.1 Signing a label

<!-- q L519 "First we" .. "be signed." -->
> First we create an equivalent standalone label for the label to be signed.

R-0249 (none, defines) · hunted

<!-- q L519 "Then the" .. "for transmission)." -->
> Then the equivalent standalone label is canonicalized (similar to canonicalizing a PICS label for transmission).

R-0250 (none, defines) · hunted

<!-- q L519 "Finally, a" .. "label extension." -->
> Finally, a digital signature is generated, inserted into a sigblock extension, and that extension is placed in the label as a label extension.

R-0251 (none, defines) · hunted

<!-- q L519 "An equivalent" .. "service options)." -->
> An equivalent standalone label can have at most one resinfo extension (which it may inherit from the service options).

R-0252 (none, must) · C-0151

## §8.1.1 Creating an equivalent standalone label

<!-- q L523 "An equivalent" .. "single label." -->
> An equivalent standalone label is a PICS 1.1 label list containing a single label.

R-0253 (none, defines) · hunted

<!-- q L523 "The single" .. "been removed." -->
> The single label must be normalized to a form where all options are label options (this includes extension options) and the sigblock extension (if present) has been removed.

R-0254 (none, must) · C-0152 → split: R-0255 (must), R-0256 (must)

<!-- q L530 "We still" .. "sigblock extension." -->
> We still need to take into account any modifications denoted by "include" or "exclude" specifiers in the sigblock extension.

R-0257 (none, must) · C-0153

<!-- q L530 "(If the" .. "the signature.)" -->
> (If the signature is being created the application knows which fields it wants to include in or exclude from the equivalent standalone label. The "include" and "exclude" options convey this information to applications trying to verify the signature.)

R-0258 (none, defines) · hunted

<!-- q L530 "The resulting" .. "standalone label." -->
> The resulting label list is the equivalent standalone label.

R-0259 (none, defines) · hunted

Inferred, not verbatim: R-0260 (an extension at both levels). See requirements.yaml.

## §8.1.2 Canonicalization of the equivalent standalone label for signing

<!-- q L534 "For a" .. "two tokens." -->
> For a given PICS 1.1 label, insert a single space character between any two tokens.

R-0261 (none, must) · hunted

<!-- q L534 "PICS 1.1 tokens" .. "and numbers." -->
> PICS 1.1 tokens include left and right parenthesis, symbols, quoted-strings, and numbers.

R-0262 (none, defines) · hunted

<!-- q L534 "Symbols are" .. "to lowercases." -->
> Symbols are case insensitive and converted to lowercases.

R-0263 (none, must) · hunted

<!-- q L534 "Tokens in" .. "considered symbols." -->
> Tokens in multi-value syntax are considered symbols.

R-0264 (none, defines) · hunted

<!-- q L534 "Do not" .. "label list." -->
> Do not insert spaces for either the leading left parenthesis or the the trailing right parenthesis of a PICS 1.1 label list.

R-0265 (none, must) · C-0154

<!-- q L534 "No carriage-returns" .. "cannonicalized label." -->
> No carriage-returns or linefeeds are present in a cannonicalized label.

R-0266 (none, must) · hunted

<!-- q L535 "A normalized" .. "the ratings." -->
> A normalized DSig-1.0 label consists of three parts in order: the PICS 1.1 header, the options, and the ratings.

R-0267 (none, must) · C-0155

<!-- q L535 "The header" .. "the serviceURL." -->
> The header part is the 'pics-1.1' symbol followed by the serviceURL.

R-0268 (none, defines) · hunted

<!-- q L536 "The option" .. "the extensions." -->
> The option part is headed by the label keyword "l", followed by a set of PICS-1.1 options, including the extensions.

R-0269 (none, defines) · hunted

<!-- q L536 "The set" .. "signature suite." -->
> The set of options, including the extensions, are determined by the option-list and the extension-list fields of the "exclude" or the "include" option in the signature suite.

R-0270 (none, defines) · hunted

<!-- q L536 "The options" .. "of until)." -->
> The options are sorted alphabetically (i.e. lexicographically ordered by the unquoted US ASCII characters) by their shortest names (i.e. use full instead of complete-label, exp instead of until).

R-0271 (none, must) · hunted

<!-- q L536 "Extension options" .. "URL." -->
> Extension options are sorted first by "extension" and then by the "extension" URL.

R-0272 (none, must) · hunted

<!-- q L537 "The rating" .. "value pairs." -->
> The rating part is headed by the rating keyword "r", followed by a set of transmit name and value pairs.

R-0273 (none, defines) · hunted

<!-- q L537 "The set" .. "the signature." -->
> The set of transmit-name and value pairs are determined by the "rating-list" field of the "include" or "exclude" option in the signature.

R-0274 (none, defines) · hunted

<!-- q L537 "Transmit names" .. "sorted alphabetically." -->
> Transmit names are sorted alphabetically.

R-0275 (none, must) · hunted

<!-- q L538 "When the" .. "label options." -->
> When the client computes the equivalent standalone label format described above, it will use all options available to it: both service and label options.

R-0276 (none, defines) · hunted

<!-- q L538 "The transmitted" .. "was signed." -->
> The transmitted set must include all options necessary as either service or label options to create the same equivalent standalone label as was signed.

R-0277 (none, must) · C-0157

Inferred, not verbatim: R-0278 (shortest option names). See requirements.yaml.

Inferred, not verbatim: R-0279 (tokens no rule changes). See requirements.yaml.

Inferred, not verbatim: R-0280 (octets of the signature input). See requirements.yaml.

Inferred, not verbatim: R-0281 (options at their default value). See requirements.yaml.

Inferred, not verbatim: R-0282 (rebuilding the signed form). See requirements.yaml.

## §8.2 An Example

Inferred, not verbatim: R-0283 (resinfo before signing). See requirements.yaml.

Inferred, not verbatim: R-0284 (what is transmitted). See requirements.yaml.

## §8.3 Signing Notes

<!-- q L609 "While PICS" .. "be valid." -->
> While PICS allows labels to be truncated to reduce their size, if this is done in DSig 1.0 after signing, the signature will no longer be valid.

R-0285 (none, defines) · hunted

<!-- q L609 "An alternative" .. "signed label." -->
> An alternative is to distribute an unsigned label with the complete option pointing to a full, signed label.

R-0286 (none, may) · hunted

<!-- q L609 "Client software" .. "signed label." -->
> Client software in need of a signed label can de-reference the complete option's URL to retrieve a complete, signed label.

R-0287 (none, may) · hunted

## §9 Appendix 1: Service Resource Information

<!-- q L614 -->
> If this is a concern, a simple policy in the trust engine that evaluates signatures could be established to require a separate signature label on the service description file.

R-0288 (none, may) · C-0164

## §10 Appendix 2: Transporting DSig 1.0 Labels

<!-- q L618 "DSig 1.0" .. "1.1 labels." -->
> DSig 1.0 labels are PICS 1.1 compliant and thus may be transported in the same way as PICS 1.1 labels.

R-0289 (none, may) · C-0165

<!-- q L619 "Labels may" .. "a URL." -->
> Labels may also exist on their own, referenced via a URL.

R-0290 (none, may) · C-0167

<!-- q L619 "When the" .. "label list." -->
> When the URL is de-referenced it returns an item of type application/pics-labels that contains a label list.

R-0291 (none, defines) · C-0168

<!-- q L620 "It is" .. "than HTML." -->
> It is possible to use DSig labels in document other than HTML.

R-0292 (none, may) · hunted

<!-- q L620 "To do" .. "be created." -->
> To do this, a specification for how the label is embedded in that document type and how the document is normalized for hashing into the label must be created.

R-0293 (none, must) · C-0169

## §11 Appendix 3: Conforming Implementations

<!-- q L624-630 -->
> In order to conform with this Recommendation, an implementation must support: resinfo 1.0 hash algorithms: MD5 hashing (http://www.w3.org/TR/1998/REC-DSig-label/MD5-1_0), SHA1 hashing (http://www.w3.org//TR/1998/REC-DSig-label/SHA1-1_0) sigblock 1.0 signature suites: MD5 hashing with RSA crypto (http://www.w3.org/TR/1998/REC-DSig-label/RSA-MD5-1_0), SHA1 hashing with DSA crypto (http://www.w3.org//TR/1998/REC-DSig-label/DSS-1_0) (known as DSS).

R-0294 (none, must) · C-0170 → split: R-0295 (must), R-0296 (must), R-0297 (must), R-0298 (must)

Inferred, not verbatim: R-0299 (what conformance asks of each role). See requirements.yaml.

## Source defects

Defects and tensions in the source, verified by this pass against the source and recorded rather than healed. Each names the entries it bears on. Quotations are markers like everything else in this file; a claim about another document is marked [outside this source] and cites that document's own cached lines. SD-E collects the editorial ones.

### SD-1: a signature label is called a standard PICS 1.1 label, while its sigblock breaks PICS 1.1's datum rules

§7 (DSig Extensions) calls a DSig 1.0 Signature Label a standard PICS 1.1 label (R-0064), Appendix 2 (§10, Transporting DSig 1.0 Labels) calls DSig labels PICS 1.1 compliant (R-0289), and the §4 overview says PICS applications can parse them (C-0008, rejected). §7.4.2 (Detailed Syntax of the sigblock Extension) concedes that the sigblock breaks PICS 1.1, because base64 uses a character no PICS 1.1 datum may carry (R-0217), while §6.2 (Applying PICS to DSig) requires each item of extension data to take one of a small, fixed list of data types (R-0059). This document's own grammar accommodates base64 only by widening a PICS term: its quotedName is built on a urlChar that admits `/` (R-0236, R-0237). [outside this source] PICS 1.1's quotedname is built on urlchar, which admits no `/` (pics-1-1-labels §7, Detailed Syntax; .cache/pics-1-1-labels.txt L203-213). A strict PICS 1.1 parser may therefore reject a label this document calls a standard PICS 1.1 label.

<!-- q L175 "A DSig" .. "1.1 label." -->
> A DSig 1.0 Signature Label is a standard PICS 1.1 label.

<!-- q L437 "Note: This" .. "1.1 datum." -->
> Note: This extension is not a valid PICS 1.1 extension because Base64 encoding uses a '/' which cannot be represented as a PICS 1.1 datum.

<!-- q L618 "DSig 1.0" .. "1.1 labels." -->
> DSig 1.0 labels are PICS 1.1 compliant and thus may be transported in the same way as PICS 1.1 labels.

### SD-2: one or more signatures, or none

§7 says a sigblock may contain one or more signatures (R-0062) and §7.3.1 (Format Specification) that a signature block is Attribution Information plus one or more Signatures (R-0121); the §4 overview says the same (C-0010, rejected). The structural representation of §7.3.1 (L290, `<signature>*`) and the grammar of §7.4.2 allow none (R-0219). A sigblock holding only AttribInfo therefore parses, and §7 then makes the label a DSig 1.0 Signature Label (R-0066) although nothing in it is signed.

<!-- q L278-280 -->
> A Signature Block consists of Attribution Information, and one or more Signatures.

<!-- q L439-440 -->
> SignatureExtension ::= 'extension ( optional' SigBlockURL AttributionInfo Signature* ')'

### SD-3: two definitions of the equivalent standalone label

§7.3.4.7 (The include and exclude tokens) builds the equivalent standalone label by the default rules, canonicalises it, and then drops the fields include or exclude select (R-0188). §8.1.1 (Creating an equivalent standalone label) drops them first and calls the result the equivalent standalone label (R-0257, R-0259), which §8.1.2 then canonicalises. Sorting and spacing commute with dropping, so the octets agree whenever the field-list selects the same fields either way. They need not: canonicalisation lowercases symbols and may rewrite option names to their short form (SD-7), and the field-list is matched before it in one order and after it in the other (R-0204). §7.3.4.7 also speaks of dropping label options only, while the field-list names ratings and extensions too (R-0194).

<!-- q L390 "After the" .. "is present." -->
> After the equivalent standalone label has been generated following the default canonicalization rules, individual label options may be dropped if an "include" or "exclude" option is present.

<!-- q L530 -->
> This is not yet an equivalent standalone label. We still need to take into account any modifications denoted by "include" or "exclude" specifiers in the sigblock extension. (If the signature is being created the application knows which fields it wants to include in or exclude from the equivalent standalone label. The "include" and "exclude" options convey this information to applications trying to verify the signature.) The resulting label list is the equivalent standalone label.

### SD-4: the outer-parenthesis rule has two readings

Read as an exception to one space between any two tokens (R-0261), the sentence forbids a space after the leading parenthesis of the label list and before its final one; read as a limit on spacing outside the label list, it adds nothing, since no token stands there. Step 3 of §8.2 (An Example) puts a space after the leading parenthesis and between the two final ones: the second reading. The readings give different octets, so signer and verifier have to take the same one (R-0265).

<!-- q L534 "Do not" .. "label list." -->
> Do not insert spaces for either the leading left parenthesis or the the trailing right parenthesis of a PICS 1.1 label list.

<!-- q L569 -->
> ( PICS-1.1 "http://www.gcf.org/v2.5" l by "John Doe"

<!-- q L575 -->
> on "1994.11.05T08:15-0500" r ( color 1 density 0 suds 0.5 ) )

### SD-5: the header symbol is lowercased by the rules and capitalised in the example

§8.1.2 lowercases every symbol (R-0263) and names the header symbol pics-1.1 (R-0268); Step 3 of §8.2, the canonical form, writes it in capitals. Either the example is not canonical or the header symbol is exempt, and the rules exempt nothing.

<!-- q L534 "Symbols are" .. "to lowercases." -->
> Symbols are case insensitive and converted to lowercases.

<!-- q L535 "The header" .. "the serviceURL." -->
> The header part is the 'pics-1.1' symbol followed by the serviceURL.

<!-- q L569 -->
> ( PICS-1.1 "http://www.gcf.org/v2.5" l by "John Doe"

### SD-6: the example reorders the hashes inside resinfo, and no rule does

Step 2 of §8.2 lists the SHA1 hash before the MD5 hash; Step 3, the canonical form, lists MD5 first. §8.1.2 sorts options, extension options by URL (R-0272) and transmit names (R-0275); nothing sorts the data inside an extension. A canonicaliser that follows the rules keeps SHA1 first and produces other octets than the example; one that follows the example sorts data the rules never mention, with no rule for how far that reaches into other extensions (R-0279).

<!-- q L560-562 -->
> ("http://www.w3.org/TR/1998/REC-DSig-label/SHA1-1_0" "aba21241241=") ("http://www.w3.org/TR/1998/REC-DSig-label/MD5-1_0" "cdc43463463=" "1997-02-05T08:15-0500"))

<!-- q L572-574 -->
> "http://www.w3.org/TR/1998/REC-DSig-label/MD5-1_0" "cdc43463463=" "1997-02-05T08:15-0500" ) ( "http://www.w3.org/TR/1998/REC-DSig-label/SHA1-1_0" "aba21241241=" ) ) for "http://www.w3.org/PICS/DSig/Overview"

### SD-7: shortest names, and the PICS 1.1 form the rules point to

§8.1.2 sorts options by their shortest names, glossed as use full instead of complete-label (R-0271); it never says whether the canonical text then carries the short name or the transmitted one. §8.1 likens the step to PICS's canonicalization for transmission (R-0250), but the form PICS 1.1 defines is for signatures. [outside this source] That form (pics-1-1-labels §13.1, Signature Details; .cache/pics-1-1-labels.txt L415-416) writes the short name and leaves out any option whose value is its default; §8.1.2 says neither. Two implementations reading §8.1.2 alone can differ on both counts (R-0278, R-0281).

<!-- q L536 "The options" .. "of until)." -->
> The options are sorted alphabetically (i.e. lexicographically ordered by the unquoted US ASCII characters) by their shortest names (i.e. use full instead of complete-label, exp instead of until).

<!-- q L519 "Then the" .. "for transmission)." -->
> Then the equivalent standalone label is canonicalized (similar to canonicalizing a PICS label for transmission).

### SD-8: ByKey or byKey, On or on, while quoted strings are case sensitive

Quoted strings are case sensitive (R-0068), and SigData tokens are quoted strings (R-0227, R-0236). §7.3.4.1 and §7.3.4.2 define the token ByKey (R-0160, R-0162, R-0163), and the §7.3.4.2 DSA example writes it so (L348); both sigblock examples, §7.4.1 (L424) and Step 4 of §8.2 (L598), write byKey. §7.3.4.6 defines the token On (R-0174); its own syntax line (R-0177) and every example write on. Either the definitions or the examples use a token this document does not define, and a verifier matching tokens exactly, as the case rule asks, rejects one or the other.

<!-- q L183 "Quoted strings" .. "case insensitive." -->
> Quoted strings are case sensitive but other literal elements are case insensitive.

<!-- q L342 -->
> The token "ByKey" identifies the value that follows as the key that should be used to validate the signature (or sufficient information to generate that key locally).

<!-- q L424 -->
> ("byKey" (("N" "aba21241241=")

<!-- q L376 "The token" .. "was generated." -->
> The token "On" identifies the value that follows as the time the label's signature was generated.

<!-- q L379 -->
> ("on" quoted-ISO-Date)

### SD-9: two Appendix 3 identifiers printed with a doubled slash

Appendix 3 (§11, Conforming Implementations) prints the SHA1 and DSS identifiers with `//TR` (R-0296, R-0298); the examples write `/TR` for both, and for the MD5 and RSA-MD5 identifiers Appendix 3 does too. [HTML of record] Both entries are links whose targets are the single-slash paths; only the printed text doubles the slash. Identifiers are quoted strings, compared as far as this document says as written (R-0080), so the doubled form names a different identifier.

<!-- q L627 -->
> SHA1 hashing (http://www.w3.org//TR/1998/REC-DSig-label/SHA1-1_0)

<!-- q L630 -->
> SHA1 hashing with DSA crypto (http://www.w3.org//TR/1998/REC-DSig-label/DSS-1_0) (known as DSS).

<!-- q L560 -->
> ("http://www.w3.org/TR/1998/REC-DSig-label/SHA1-1_0" "aba21241241=")

<!-- q L429 -->
> ("Signature" "http://www.w3.org/TR/1998/REC-DSig-label/DSS-1_0"

### SD-10: the BNF notation is defined only in part

The convention of §7 defines `?`, `+` and `*` (R-0067). The grammars also use square brackets for an optional part (L227, L467), `|` and once `/` for alternatives (L466), `..` for a range (L456, L457, L465), angle-bracket placeholders defined only in prose (`<options>`, `<ratings>` and `<quoted-URL>` at L394-396, `<Key-Value, ...>` at L344, `<CA-Serial-No.>` at L372), productions given as prose (as defined in RFC-1521) and `Stz` for S followed by tz (L227, L469). resource-hash is written as a quoted literal (R-0112): read as BNF it matches only the word base64-string in quotation marks. One nonterminal is spelled quotedURL, quotedUrl and quoted-URL, another quoted-ISO-date and quoted-ISO-Date (L377, L379), and §7.3.3 writes SignatureSuite where §7.4.2 writes SignatureSuiteID (R-0147, R-0225).

<!-- q L225 -->
> resource-hash ::= '"base64-string"'

<!-- q L466 -->
> sign ::= '+' / '-'

<!-- q L444 -->
> CertificateFamilyID ::= quotedUrl

<!-- q L318 -->
> ( "Signature" SignatureSuite SigData+)

### SD-11: an empty field-list is a field-list and not a SigInfo

field-list makes each of its three lists optional (R-0195), so an empty pair of parentheses is a field-list. include and exclude carry it as their SigInfo (R-0183, R-0226), and SigInfo's parenthesised form needs at least one item (R-0228), so an include with an empty field-list is no SigData. What an empty include would select, nothing at all, is never said.

<!-- q L393 -->
> field-list ::= '(' option-list? ratings-list? extension-list? ')'

<!-- q L449-450 -->
> SigInfo ::= SigData | quotedURL | quoted-ISO-date | quotedBase64String | quotedName | number | '(' SigInfo+ ')'

### SD-12: Note 1 announces an exception Note 2 does not state

Note 1 to the quoted-ISO-date production ends with Except: (R-0117). Note 2 states no exception: it compares DSig's format with PICS 1.1's and ISO 8601's, and the two differences it names, the separators and the optional seconds and fractions, are already in the grammar (R-0114). Whether DSig also takes over PICS 1.1's minute 60 is left unsaid; the grammar allows 00 through 59. The §7.4.2 copy repeats both notes (L486-495; R-0246).

<!-- q L245-248 "DSig requires" .. "here, Except:" -->
> DSig requires precisely the syntax described here -- neither the time nor the time zone may be omitted, none of the alternate ISO formats are permitted, and the punctuation must be as specified here, Except:

<!-- q L249-253 -->
> 2. ISO date described here differs from the PICS 1.1 and ISO 8601:1988 date and time format. PICS 1.1 uses '.' as separators while the ISO standard calls for '-'. DSig supports both syntaxes. PICS 1.1 also does not support the optional seconds and fractions of seconds fields and permits minutes to range from 0 to 60.

<!-- q L235 -->
> mm ::= two digits of minute (00 through 59)

### SD-13: the resinfo example's narration contradicts the example

The example gives a hash date to its second entry, the MD5 hash, and none to the first, the SHA1 hash. The narration says the first hash is SHA1 and is followed by the hash data and the date, and gives the MD5 clause after it none.

<!-- q L261-263 -->
> ( "http://www.w3.org/TR/1998/REC-DSig-label/SHA1-1_0" "base64 hash" ) ( "http://www.w3.org/TR/1998/REC-DSig-label/MD5-1_0" "base64 hash" "1997-02-05T08:15-0500" ) )

<!-- q L265 "In our" .. "hash algorithm." -->
> In our specific example above, the first hash is of type SHA1. This is followed by the actual hash data and followed by the date the hash was computed. The second clause uses the MD5 hash algorithm.

### SD-14: which octets a resinfo hash covers is never stated

resinfo carries hashes of the information resource (R-0090) and the receiver uses them to decide whether it holds the same resource (R-0082), but no sentence says which octets are hashed: the body as served or after its content coding, or, for a document that embeds its own label, the document with or without the label (a label cannot carry a hash of itself). Appendix 2 requires a specification of how a document other than HTML is normalized for hashing (R-0293), implying HTML has one; this document gives none. [outside this source] PICS 1.1 gives one for MIC-md5, the option resinfo replaces: compute the digest after removing every META element that carries a PICS label, and the whitespace after it (pics-1-1-labels §13, MICs and Digital Signatures; .cache/pics-1-1-labels.txt L401). DSig neither adopts nor cites it for resinfo (R-0106).

<!-- q L206 -->
> Structurally, resinfo contains one or more hashes of the information resource; each hash includes a hash algorithm identifier, the actual hash of the resource and (optionally) the date the hash was computed.

<!-- q L620 "To do" .. "be created." -->
> To do this, a specification for how the label is embedded in that document type and how the document is normalized for hashing into the label must be created.

### SD-15: the semantics of a signed label cover the whole label; a signature may cover part of it

§6.1 (Semantics of Embedded Signature Blocks) defines what a label carrying a sigblock means: the signer asserts the validity of every statement in the label (R-0020); §5 says the same of signing an assertion label (R-0002). §7.3.4.7 lets a signature cover a subset of the label, ratings included (R-0185, R-0274), and never narrows the semantics to the signed fields. A relying party reading §6.1 attributes to the signer statements the signature does not cover.

<!-- q L134 -->
> "The entity possessing the secret key that digitally signed this PICS 1.1 label had access to the secret key and the label at the same time and asserts that the statements made within the label are valid"

<!-- q L537 "The set" .. "the signature." -->
> The set of transmit-name and value pairs are determined by the "rating-list" field of the "include" or "exclude" option in the signature.

### SD-16: a cryptographic link is required for security, and optional

§7 says a label that signs an information resource in a secure fashion must have a cryptographic connection to it (R-0060). The only connection the document defines is resinfo, which is optional (R-0065) and invalid in a generic label (R-0103), while a sigblock is valid in generic labels (R-0125): a valid signed generic label has no cryptographic connection to any resource (R-0001). The rule on resinfo in a generic label is also worded three ways: not meaningful in §5.1 (R-0019), can not be used in §6.2 (R-0041), not valid in §7.2 (R-0103).

<!-- q L173 "To do" .. "that resource." -->
> To do this in a secure fashion, the signed label must have a cryptographic connection to that resource.

<!-- q L283 -->
> The sigblock extension is valid in both generic and specific (non-generic) PICS 1.1 labels.

<!-- q L215 -->
> The resinfo extension is not valid in a generic PICS 1.1 label. It is only valid within a specific (non-generic) PICS 1.1 label.

### SD-17: the mandatory suites and hash algorithms are identified, not defined

§7.3.3 says DSig 1.0 defines two hash algorithms and two suites (R-0154); Appendix 3 names them by URL (R-0294). Nothing here defines them: no SigData layout for RSA-MD5-1_0 or DSS-1_0, no statement of how the canonical label becomes the input to RSA or DSA (digest, padding, encoding of the result), no key encoding, and no statement of whether either suite permits partial signatures (R-0182), though the §7.4.1 example uses exclude under RSA-MD5-1_0. The examples show field names (N and E under byKey, R and S under SigCrypto) that no text defines. Implementing Appendix 3 needs the identifier description documents, which §7.1 requires to exist (R-0076).

<!-- q L324 "DSig 1.0" .. "Appendix 3." -->
> DSig 1.0 does define two hash algorithms and two signature suites for interoperability; see Appendix 3.

<!-- q L403 "The format" .. "signature suites." -->
> The format and contents of this field are entirely specified by particular signature suites.

### SD-18: an extension at both levels is resolved only for resinfo

For resinfo a label option takes precedence over a service option (R-0093). For any other extension (a private one, R-0008; a signed date, R-0180) three readings stand. PICS's override works by option name and every extension is the option extension, so read literally any extension among the label options overrides every extension among the service options (R-0011); read per URL, only the same extension is replaced; read as all options are label options (R-0255), both are kept, and the sort by URL (R-0272) then ties two with the same URL. Signer and verifier can differ (R-0260).

<!-- q L212 "If both" .. "service option." -->
> If both are present, the extension given as a label option takes precedence over the service option.

### SD-19: one conformance class for every role

Appendix 3 names one conformance class, an implementation (R-0294); §7.1 restates it as implementing the signature suites (R-0079), §7.3.3 as implementing the four algorithms (R-0155). Nothing distinguishes a label creator, a signer, a verifier or a parser, so what a verifier-only implementation owes is inferred (R-0299).

<!-- q L624 -->
> In order to conform with this Recommendation, an implementation must support:

### SD-20: symbols are lowercased, and a transmit-name is a symbol PICS 1.1 keeps case-sensitive

Added by pass 2 (verify): `design-notes.md` K-02 and `messages.yaml` F-11 recorded this and the register did not. §8.1.2 (Canonicalization of the equivalent standalone label for signing) names four kinds of token and lowercases the symbols (R-0262, R-0263). A transmit-name in the ratings is neither a parenthesis, a quoted string nor a number, so on the natural reading it is a symbol and is lowercased; include and exclude name transmit-names in their ratings-list (R-0201), and the canonical form sorts them (R-0275). [outside this source] PICS 1.1 makes transmit-names case-sensitive, because a URL may serve as one (pics-1-1-labels §7, Detailed Syntax, .cache/pics-1-1-labels.txt L141; §14, Glossary, L471). Two labels PICS 1.1 reads as rating different categories, one with Suds and one with suds, then share one canonical form, and a signature over one verifies over the other. On the other reading, that a transmit-name is not a symbol, the rules say nothing about its case. Every transmit-name in this document's examples is lower case, so no example decides it.

<!-- q L534 "PICS 1.1 tokens" .. "to lowercases." -->
> PICS 1.1 tokens include left and right parenthesis, symbols, quoted-strings, and numbers. Symbols are case insensitive and converted to lowercases.

### SD-E: editorial

Recorded, not healed. None changes a rule.

- L77, §5: a closing quotation mark with no opening one (R-0003).

<!-- q L77 -->
> By signing an assertion label, the signer explicitly confirms belief in the truth of the statements contained within the label. A signature does not indicate that the signer created the label, only that they believe the statements made within it are valid."

- L90, §5.1: a PICS labels contains.

<!-- q L90 -->
> A PICS labels contains one or more service sections:

- L142, §6.2: a space before the full stop (R-0021).

<!-- q L142 "at the" .. "made ." -->
> at the time the assertion was made .

- L145, §6.2: superceded.

<!-- q L145 "This option has" .. "resinfo extension." -->
> This option has been superceded by the DSig 1.0 resinfo extension.

- L169, §6.2: extensions uses.

<!-- q L169 "The DSig" .. "this mechanism" -->
> The DSig 1.0 resinfo and sigblock extensions uses this mechanism

- L183, §7: are be treated (R-0069).

<!-- q L183 "Multiple contiguous" .. "quoted strings." -->
> Multiple contiguous space characters are be treated as though they were a single space character except in quoted strings.

- L192, §7.1: yield a a document (R-0073).

<!-- q L192 "Since the" .. "a document." -->
> Since the identifier is a URL, it must, when resolved, yield a a document.

- L270, §7.3: the sigblock is said to identify who signed the information resource; by §6.1 the signer signs the label, which reaches the resource only through resinfo.

<!-- q L270 -->
> who has signed the information resource,

- L288-290, §7.3.1: the structural representation closes one parenthesis more than it opens (C-0098, rejected).

<!-- q L288-290 -->
> extension ( optional "http://www.w3.org/TR/1998/REC-DSig-label/sigblock-1_0" <attribution info> <signature>* ) )

- L296, §7.3.2: the sigblock called the signature option, the name of the PICS 1.1 option DSig does not use (R-0140).

<!-- q L296 "(More precisely," .. "signature option.)" -->
> (More precisely, none of the information within the entire sigblock extension, including the Attribution Information section, contributes to the hash of the label that is signed as part of the signature option.)

- L370, §7.3.4.5: the serial number a relevant certificate (R-0171).

<!-- q L370 "the serial" .. "that CA." -->
> the serial number a relevant certificate issued by that CA.

- L390, §7.3.4.7: a semicolon after exclude (R-0191).

<!-- q L390 "At most" .. "option." -->
> At most one "include" or "exclude"; field may appear; it is an error to have both an "include" and an "exclude" option.

- L534, §8.1.2: the the (R-0265).

<!-- q L534 "Do not" .. "label list." -->
> Do not insert spaces for either the leading left parenthesis or the the trailing right parenthesis of a PICS 1.1 label list.

- L534, §8.1.2: cannonicalized (R-0266); converted to lowercases (R-0263).

<!-- q L534 "No carriage-returns" .. "cannonicalized label." -->
> No carriage-returns or linefeeds are present in a cannonicalized label.

- L536, §8.1.2: the field-list is said to sit in the signature suite; L537 says in the signature (R-0270, R-0274).

<!-- q L536 "The set" .. "signature suite." -->
> The set of options, including the extensions, are determined by the option-list and the extension-list fields of the "exclude" or the "include" option in the signature suite.

- L537, §8.1.2: rating-list, where the grammar says ratings-list (R-0197).

<!-- q L537 "The set" .. "the signature." -->
> The set of transmit-name and value pairs are determined by the "rating-list" field of the "include" or "exclude" option in the signature.

- L567, §8.2: the above example is the block below the note (C-0159, rejected).

<!-- q L567 "(NOTE: Carriage-returns" .. "purposes only." -->
> (NOTE: Carriage-returns in the above example are for display purposes only.

- L620, Appendix 2 (§10): in document other than HTML (R-0292).

<!-- q L620 "It is" .. "than HTML." -->
> It is possible to use DSig labels in document other than HTML.

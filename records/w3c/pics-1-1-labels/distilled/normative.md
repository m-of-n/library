---
record: pics-1-1-labels
kind: normative
title: "pics-1-1-labels — normative text"
generated_by: bin/fx1-skeleton
extracted: "2026-11-12"
reviewed_by: ""
---

# Normative text

Every binding statement of *PICS 1.1 Label Distribution: Label Syntax and Communication Protocols* (W3C Recommendation 31-October-96, REC-PICS-labels-961031), in source order, as quotation markers whose words `bin/check-quotes --render` writes from `.cache/pics-1-1-labels.txt` (sha256 `469de99e…`, the `bin/render-w3c --ordinal` rendering of the HTML of record, content.sha256 `a1acf198…`; line numbers count there). Nothing below a marker was typed.

**Section numbers are not the source's.** The Recommendation numbers nothing; the ordinals are the rendering's, assigned from h2/h3 nesting, so every heading below gives the ordinal and the source's own heading title, and prose gives the title on an ordinal's first mention. Appendix A is the seventeenth top-level section and Appendix B the eighteenth.

Built by pass 1 (requirements agent) over the `bin/fx1-skeleton` layer: 349 requirement ids, 326 stated (each quoted below, its id on the line after it) and 23 inferred (named in place, not quoted). The document predates RFC 2119 and uses no BCP 14 keyword; its obligations are lowercase, and every entry has verb `none` (requirements.yaml `reconciliation`). A parent that welds several statements, usually an HTML `dt` and its `dd` or a run of grammar productions, is followed by its `split_of` children, each quoted as the sub-span it is.

What is not quoted, and why: §1 (Status of this document), §2 (Abstract), §3 (Table of Contents) and §4 (Overview), whose statements the body restates; the examples of §6 (Example), §8 (Semantics of PICS Labels and Label Lists), §11.1 (Example) and §12.1 (Sample Query) and all of §18 (Appendix B: Sample Label Bureau Queries and Responses), which are fixtures for `examples/`; §15 (References), §16 (Acknowledgments), the legal and RSAREF paragraphs of §13 (MICs and Digital Signatures), the motivation of §17 (Appendix A: An Algorithm for Locating a Label Bureau), advisory sentences (encouraged, advised), and glossary entries that only restate the body. Four sentences from those parts are quoted all the same, each because it is the only statement of a rule: R-0001 (overview), R-0103 and R-0141 (examples) and R-0329 (glossary). The candidate verdicts in `inferred-candidates.yaml` give the reason for every skeleton candidate left out.

## §4 Overview

<!-- q L51 -->
> We specify a mechanism, using the existing META tag, for embedding one or more labels in (the header of) an HTML document.

R-0001 (none)

## §5 General Format

<!-- q L59 "A label" .. "rating." -->
> A label consists of a service identifier, label options, and a rating.

R-0002 (none)

<!-- q L59 "The service" .. "identifier." -->
> The service identifier is the URL chosen by the rating service (see Rating Services and Rating Systems) as its unique identifier.

R-0003 (none)

<!-- q L59 "The rating" .. "dimensions." -->
> The rating itself is a set of attribute-value pairs that describe a document along one or more dimensions.

R-0004 (none)

<!-- q L72 "A specific" .. "document." -->
> A specific label applies to a single document.

R-0005 (none)

<!-- q L72 "A label" .. "documents." -->
> A label applies to the given document only, not to the referenced documents.

R-0006 (none)

<!-- q L73 "A generic" .. "option)." -->
> A generic label (identified by the use of the generic option) applies to any document whose URL begins with a specific string of characters (specified using the for option).

R-0007 (none)

<!-- q L73 "A generic label does" .. "labels." -->
> A generic label does not have the expected semantics of a "default" label that can be overridden by more specific labels.

R-0008 (none)

<!-- q L73 "While a" .. "label." -->
> While a specific label does override a generic label when a client has access to both, the two labels may be distributed separately, and thus a client may have access to only the generic label.

R-0009 (none)

<!-- q L73 "However, a" .. "directory." -->
> However, a generic label for a site or directory should only be distributed if it applies to all the documents in that site or directory.

R-0010 (none)

<!-- q L74 "A rating" .. "that URL." -->
> A rating service may provide a generic label for any or all prefixes of a given URL, but should provide only one specific label for that URL.

R-0011 (none) → split: R-0012, R-0013

<!-- q L74 "A rating" .. "given URL" -->
> A rating service may provide a generic label for any or all prefixes of a given URL

R-0012 (none; split of R-0011)

<!-- q L74 "should provide" .. "that URL." -->
> should provide only one specific label for that URL.

R-0013 (none; split of R-0011)

<!-- q L74 "When the" .. "label." -->
> When the specific label for a document can be found, it should be used in preference to any generic label.

R-0014 (none)

<!-- q L74 "Lacking a" .. "string." -->
> Lacking a specific label, any generic label may be substituted, but preference should be given to the generic label which has the longest string.

R-0015 (none) → split: R-0016, R-0017

<!-- q L74 "Lacking a" .. "substituted" -->
> Lacking a specific label, any generic label may be substituted

R-0016 (none; split of R-0015)

<!-- q L74 "preference should" .. "string." -->
> preference should be given to the generic label which has the longest string.

R-0017 (none; split of R-0015)

<!-- q L74 "Some PICS" .. "labels." -->
> Some PICS client software may impose restrictions on the use of generic labels.

R-0018 (none)

<!-- q L78 "The last" .. "assigned." -->
> The last modification date of the item to which this rating applies, at the time the rating was assigned.

R-0019 (none)

<!-- q L81 "A message" .. "rated." -->
> A message integrity check (MIC) of the item being rated.

R-0020 (none)

<!-- q L81 "The MD5" .. "the MIC." -->
> The MD5 Message Digest Algorithm (see RFC1321) is used to compute the MIC.

R-0021 (none)

<!-- q L84 "An identifier" .. "label." -->
> An identifier for the person or entity within the rating service who was responsible for creating this particular label.

R-0022 (none)

<!-- q L84-86 "This may" .. "applies." -->
> This may be human readable, or it may be used to contain a (base-64 encoded) set of certificates and other information used to verify the signature on the label. for quotedURL The URL (or prefix string of a URL) of the item to which this rating applies.

R-0023 (none) → split: R-0024, R-0025

<!-- q L84 "This may" .. "label." -->
> This may be human readable, or it may be used to contain a (base-64 encoded) set of certificates and other information used to verify the signature on the label.

R-0024 (none; split of R-0023)

<!-- q L86 "The URL" .. "applies." -->
> The URL (or prefix string of a URL) of the item to which this rating applies.

R-0025 (none; split of R-0023)

<!-- q L86 "This option" .. "cases." -->
> This option is required for generic labels and in certain other cases (see "Requesting Labels Separately," below); it is optional in other cases.

R-0026 (none) → split: R-0027, R-0028

<!-- q L86 "This option" .. "below)" -->
> This option is required for generic labels and in certain other cases (see "Requesting Labels Separately," below)

R-0027 (none; split of R-0026)

<!-- q L86 "it is" .. "cases." -->
> it is optional in other cases.

R-0028 (none; split of R-0026)

Inferred, not verbatim: R-0029 (document a label without for applies to). See requirements.yaml.

<!-- q L86-89 "Since a" .. "option." -->
> Since a single document can have many URLs, the URL used to retrieve a document may differ from the URL in the for option of a label that accompanies the document. generic boolean -or- gen boolean If this option is set to true, the label can be applied to any URL starting with the prefix given in the for option.

R-0030 (none) → split: R-0031, R-0032

<!-- q L86 "Since a" .. "document." -->
> Since a single document can have many URLs, the URL used to retrieve a document may differ from the URL in the for option of a label that accompanies the document.

R-0031 (none; split of R-0030)

<!-- q L89 "If this" .. "option." -->
> If this option is set to true, the label can be applied to any URL starting with the prefix given in the for option.

R-0032 (none; split of R-0030)

Inferred, not verbatim: R-0033 (a label without the generic option). See requirements.yaml.

<!-- q L89 "All generic" .. "option." -->
> All generic labels must also include the for option.

R-0034 (none)

<!-- q L89-93 "As mentioned" .. "label." -->
> As mentioned earlier, a generic label should not be created unless it can be legitimately applied to all documents whose URL begins with the prefix specified in the for option (even if a more specific label exists). on quoted-ISO-date The date on which this rating was issued. signature-RSA-MD5 "Base64-string" An RSA digital signature encompassing the label.

R-0035 (none) → split: R-0036, R-0037, R-0038

<!-- q L89 "As mentioned" .. "exists)." -->
> As mentioned earlier, a generic label should not be created unless it can be legitimately applied to all documents whose URL begins with the prefix specified in the for option (even if a more specific label exists).

R-0036 (none; split of R-0035)

<!-- q L91 -->
> The date on which this rating was issued.

R-0037 (none; split of R-0035)

<!-- q L93 "An RSA" .. "label." -->
> An RSA digital signature encompassing the label.

R-0038 (none; split of R-0035)

<!-- q L93 "The signature" .. "label." -->
> The signature is computed using the MD5 algorithm by the rating service that issued the label.

R-0039 (none)

<!-- q L96 -->
> The date on which this rating expires.

R-0040 (none)

<!-- q L97-102 "Other information." .. "current one." -->
> Other information. comment quotedname Information for humans who may see the label; no associated semantics. complete-label quotedURL -or- full quotedURL Dereferencing this URL returns a complete label that can be used in place of the current one.

R-0041 (none) → split: R-0042, R-0043

<!-- q L99 -->
> Information for humans who may see the label; no associated semantics.

R-0042 (none; split of R-0041)

<!-- q L102 "Dereferencing this" .. "current one." -->
> Dereferencing this URL returns a complete label that can be used in place of the current one.

R-0043 (none; split of R-0041)

<!-- q L102 "The complete" .. "possible." -->
> The complete label has values for as many attributes as possible.

R-0044 (none)

<!-- q L102-105 "When the" .. "mechanism." -->
> When the URL is dereferenced it returns an item of type application/pics-labels that contains a labellist with exactly one label. extension (optional quotedURL data*) -or- extension (mandatory quotedURL data*) Future extension mechanism.

R-0045 (none) → split: R-0046

<!-- q L102 "When the" .. "label." -->
> When the URL is dereferenced it returns an item of type application/pics-labels that contains a labellist with exactly one label.

R-0046 (none; split of R-0045)

<!-- q L105 "To avoid" .. "quotedURL." -->
> To avoid duplication of extension names, each extension is identified by a quotedURL.

R-0047 (none)

<!-- q L105 "The URL" .. "extension." -->
> The URL can be dereferenced to get a human-readable description of the extension.

R-0048 (none)

<!-- q L105 "If the" .. "supplied." -->
> If the extension is optional then software which does not understand the extension can simply ignore it; if the extension is mandatory then software which does not understand the extension should act as though no label had been supplied.

R-0049 (none) → split: R-0050, R-0051

<!-- q L105 "If the" .. "ignore it" -->
> If the extension is optional then software which does not understand the extension can simply ignore it

R-0050 (none; split of R-0049)

<!-- q L105 "if the" .. "supplied." -->
> if the extension is mandatory then software which does not understand the extension should act as though no label had been supplied.

R-0051 (none; split of R-0049)

<!-- q L105 "Each item" .. "below." -->
> Each item of data must be one of a fixed set of simple-to-parse data types as specified in the detailed syntax below.

R-0052 (none)

## §6 Example

<!-- q L109 "the specification" .. "single space" -->
> the specification treats multiple white space characters as if they were compressed into a single space

R-0053 (none)

<!-- q L121 "The same" .. "abbreviations." -->
> The same label list may be transmitted more compactly by converting all of the line breaks and subsequent indentation characters into a single space, and by replacing the word "labels" with "l", "ratings" with "r" and long option names with their abbreviations.

R-0054 (none)

<!-- q L121 "It may" .. "a URL:" -->
> It may be compressed for transmission purposes even further by removing all of the optional information to a separate document and referencing that document by a URL:

R-0055 (none)

<!-- q L129 "Finally, the" .. "smaller." -->
> Finally, the optional information may be omitted entirely, reducing the information content of the labels but making the transmission even smaller.

R-0056 (none)

## §7 Detailed Syntax

<!-- q L137 "The following" .. "labels." -->
> The following grammar, in modified BNF, describes the syntax of labels.

R-0057 (none)

<!-- q L139 "The string" .. "Systems." -->
> The string "PICS-1.1" in version corresponds to the version number 1.1 of the PICS specification in PICS Rating Services and Rating Systems.

R-0058 (none)

<!-- q L139-140 "While it" .. "strings." -->
> While it is inelegant that the service description uses the notation "(PICS-version 1.1)" while the label itself uses "PICS-1.1", it is intentional. Whitespace is ignored except in quoted strings.

R-0059 (none) → split: R-0060, R-0061

<!-- q L139 "While it" .. "intentional." -->
> While it is inelegant that the service description uses the notation "(PICS-version 1.1)" while the label itself uses "PICS-1.1", it is intentional.

R-0060 (none; split of R-0059)

<!-- q L140 "Whitespace is" .. "strings." -->
> Whitespace is ignored except in quoted strings.

R-0061 (none; split of R-0059)

<!-- q L140 "Multiple contiguous" .. "character." -->
> Multiple contiguous whitespace characters can be treated as though they were a single space character.

R-0062 (none)

Inferred, not verbatim: R-0063 (whitespace as a token separator). See requirements.yaml.

<!-- q L141 "Transmit-names and" .. "sensitive." -->
> Transmit-names and quoted strings are case sensitive.

R-0064 (none)

<!-- q L141 "Option names" .. "insensitive." -->
> Option names and other tokens in the BNF grammar are case insensitive.

R-0065 (none)

<!-- q L142 "This specification" .. "US-ASCII." -->
> This specification is strictly about information carried over the wire from the client to the server, and it requires the use of US-ASCII.

R-0066 (none)

<!-- q L143 "An option" .. "options." -->
> An option that appears in the service-info applies to all labels in that service-info unless overridden by an option in a specific label. That is, a label is effectively lexically nested within the enclosing service-info for the purpose of understanding the applicable options.

R-0067 (none)

<!-- q L144 "Numbers in" .. "numbers." -->
> Numbers in PICS labels may be integers or fractions with no greater range or precision than that provided by IEEE single-precision floating point numbers.

R-0068 (none)

<!-- q L145 "The multi-value" .. "category." -->
> The multi-value syntax must be used when there is more than one value for a particular category.

R-0069 (none)

Inferred, not verbatim: R-0070 (repeated categories in a rating). See requirements.yaml.

<!-- q L145 "This syntax" .. "that case." -->
> This syntax may be used when there is exactly one value, but the more compact version may also be used in that case.

R-0071 (none)

<!-- q L145 "When there" .. "syntax." -->
> When there is no value, the category may be omitted entirely or transmitted using the multi-value syntax.

R-0072 (none)

<!-- q L146 -->
> The only options that may occur more than once in a particular single-label or service-info are comment and extension; if the extension option is supplied more than once, the quotedURLs defining the extensions must be distinct.

R-0073 (none) → split: R-0074, R-0075

<!-- q L146 "The only" .. "extension" -->
> The only options that may occur more than once in a particular single-label or service-info are comment and extension

R-0074 (none; split of R-0073)

<!-- q L146 "if the" .. "distinct." -->
> if the extension option is supplied more than once, the quotedURLs defining the extensions must be distinct.

R-0075 (none; split of R-0073)

<!-- q L147 -->
> Categories may appear in any order in a rating; they need not match the order in which they appear in the application/pics-service.

R-0076 (none)

<!-- q L148 "For parsing" .. "values." -->
> For parsing purposes, notice that a label ends with either "ratings" or "r" followed by a parenthesized list of categories and values.

R-0077 (none)

<!-- q L148 "If this" .. ")." -->
> If this does not end the label list, it is followed by either another label (possibly starting with options), a new service URL (recognizable because it must be surrounded by quotation marks), or an error (starting with the word "error").

R-0078 (none)

<!-- q L150-183 -->
> labellist :: '(' version service-info+ ')' version :: 'PICS-1.1' service-info :: 'error' '(no-ratings' explanation* ')' | serviceID service-error | serviceID option* labelword label* serviceID :: quotedURL labelword :: 'labels' | 'l' label :: label-error | single-label | '(' single-label* ')' single-label :: option* ratingword '(' rating+ ')' ratingword :: 'ratings' | 'r' quotedURL :: '"' URL '"' as described and extended in Rating Services and Rating Systems. option :: labeloption | documentoption | otheroption labeloption :: 'by' quotedname | 'generic' boolean | 'gen' boolean | 'for' quotedURL | 'on' quoted-ISO-date | 'signature-RSA-MD5' "base64-string" | 'until' quoted-ISO-date | 'exp' quoted-ISO-date documentoption :: 'at' quoted-ISO-date | 'MIC-md5' "base64-string" | 'md5' "base64-string" otheroption :: 'comment' quotedname | 'complete-label' quotedURL | 'full' quotedURL | 'extension' '(' mand/opt quotedURL data* ')' mand/opt :: 'optional' | 'mandatory' data :: quoted-ISO-date | quotedURL | number | quotedname | '(' data* ')' quoted-ISO-date :: '"'YYYY'.'MM'.'DD'T'hh':'mmStz'"' based on the ISO 8601:1988 date and time standard, restricted to the specific form described here: YYYY :: four-digit year MM :: two-digit month (01=January, etc.)

R-0079 (none) → split: R-0080, R-0081, R-0082, R-0083, R-0084, R-0085, R-0086, R-0087, R-0088, R-0089, R-0090, R-0091, R-0092, R-0093, R-0094, R-0095, R-0096, R-0097

<!-- q L150 -->
> labellist :: '(' version service-info+ ')'

R-0080 (none; split of R-0079)

<!-- q L151 -->
> version :: 'PICS-1.1'

R-0081 (none; split of R-0079)

<!-- q L152-153 -->
> service-info :: 'error' '(no-ratings' explanation* ')' | serviceID service-error | serviceID option* labelword label*

R-0082 (none; split of R-0079)

<!-- q L154 -->
> serviceID :: quotedURL

R-0083 (none; split of R-0079)

<!-- q L155 -->
> labelword :: 'labels' | 'l'

R-0084 (none; split of R-0079)

<!-- q L156 -->
> label :: label-error | single-label | '(' single-label* ')'

R-0085 (none; split of R-0079)

<!-- q L157 -->
> single-label :: option* ratingword '(' rating+ ')'

R-0086 (none; split of R-0079)

<!-- q L158 -->
> ratingword :: 'ratings' | 'r'

R-0087 (none; split of R-0079)

<!-- q L159-160 -->
> quotedURL :: '"' URL '"' as described and extended in Rating Services and Rating Systems.

R-0088 (none; split of R-0079)

<!-- q L161 -->
> option :: labeloption | documentoption | otheroption

R-0089 (none; split of R-0079)

<!-- q L162-168 -->
> labeloption :: 'by' quotedname | 'generic' boolean | 'gen' boolean | 'for' quotedURL | 'on' quoted-ISO-date | 'signature-RSA-MD5' "base64-string" | 'until' quoted-ISO-date | 'exp' quoted-ISO-date

R-0090 (none; split of R-0079)

<!-- q L169-171 -->
> documentoption :: 'at' quoted-ISO-date | 'MIC-md5' "base64-string" | 'md5' "base64-string"

R-0091 (none; split of R-0079)

<!-- q L172-175 -->
> otheroption :: 'comment' quotedname | 'complete-label' quotedURL | 'full' quotedURL | 'extension' '(' mand/opt quotedURL data* ')'

R-0092 (none; split of R-0079)

<!-- q L176 -->
> mand/opt :: 'optional' | 'mandatory'

R-0093 (none; split of R-0079)

<!-- q L177-178 -->
> data :: quoted-ISO-date | quotedURL | number | quotedname | '(' data* ')'

R-0094 (none; split of R-0079)

<!-- q L179-181 -->
> quoted-ISO-date :: '"'YYYY'.'MM'.'DD'T'hh':'mmStz'"' based on the ISO 8601:1988 date and time standard, restricted to the specific form described here:

R-0095 (none; split of R-0079)

<!-- q L182 -->
> YYYY :: four-digit year

R-0096 (none; split of R-0079)

<!-- q L183 -->
> MM :: two-digit month (01=January, etc.)

R-0097 (none; split of R-0079)

<!-- q L184 -->
> DD :: two-digit day of month (01 through 31)

R-0098 (none)

<!-- q L185 -->
> hh :: two digits of hour (00 through 23) (am/pm NOT allowed)

R-0099 (none)

<!-- q L186 -->
> mm :: two digits of minute (00 through 60)

R-0100 (none)

<!-- q L187 -->
> S :: sign of time zone offset from UTC ('+' or '-')

R-0101 (none)

<!-- q L188-189 -->
> tz :: four digit amount of offset from UTC (e.g., 1512 means 15 hours and 12 minutes)

R-0102 (none)

<!-- q L190-191 -->
> For example, "1994.11.05T08:15-0500" is a valid quoted-ISO-date denoting November 5, 1994, 8:15 am, US Eastern Standard Time

R-0103 (none)

Inferred, not verbatim: R-0104 (instant a quoted-ISO-date denotes). See requirements.yaml.

<!-- q L193-200 "PICS requires" .. "[sign]unsignedint['.'" -->
> PICS requires precisely the syntax described here -- neither the time nor the time zone may be omitted, none of the alternate formats are permitted, and the punctuation must be as specified here. rating :: transmit-name number | transmit-name '(' multi-value* ')' multi-value :: number | number ':' number transmit-name :: transmit-name-char+ ['/' transmit-name] number :: [sign]unsignedint['.'

R-0105 (none) → split: R-0106, R-0107, R-0108, R-0109

<!-- q L193-196 "PICS requires" .. "specified here." -->
> PICS requires precisely the syntax described here -- neither the time nor the time zone may be omitted, none of the alternate formats are permitted, and the punctuation must be as specified here.

R-0106 (none; split of R-0105)

<!-- q L197 -->
> rating :: transmit-name number | transmit-name '(' multi-value* ')'

R-0107 (none; split of R-0105)

<!-- q L198 -->
> multi-value :: number | number ':' number

R-0108 (none; split of R-0105)

<!-- q L199 -->
> transmit-name :: transmit-name-char+ ['/' transmit-name]

R-0109 (none; split of R-0105)

<!-- q L200 -->
> number :: [sign]unsignedint['.' [unsignedint]]

R-0110 (none)

<!-- q L200-219 "[unsignedint]] sign" .. ":: quotedname" -->
> [unsignedint]] sign :: '+' | '-' unsignedint :: [0-9]+ quotedname :: '"' urlchar-or-space+ '"' alphanumpm :: 'A' | ... | 'Z' | 'a' | ... | 'z' | '0' | ... | '9' | sign transmit-name-char :: alphanumpm | '.' | '$' | ',' | ';' | ':' | '&' | '=' | '?' | '!' | '*' | '~' | '@' | '#' | '_' | '%' hex hex Note: Use the "%" escape technique (% followed by the two hex digits that represent the character in the ASCII character set) to insert single or double quotation marks or parentheses. urlchar :: transmit-name-char | '(' | ')' hex :: '0' | ... | '9' | 'A' | ... | 'F' | 'a' | ... | 'f' urlchar-or-space :: urlchar | ' ' base64-string :: as defined in RFC-1521. service-error :: 'error' '(' 'request-denied' explanation* ')' | 'error' 'service-unavailable' label-error :: 'error' '(' 'request-denied' [quotedURL explanation*] ')' | 'error' '(' 'not-labeled' quotedURL* ')' explanation :: quotedname

R-0111 (none) → split: R-0112, R-0113, R-0114, R-0115, R-0116, R-0117, R-0118, R-0119, R-0120, R-0121, R-0122, R-0123, R-0124

<!-- q L201 -->
> sign :: '+' | '-'

R-0112 (none; split of R-0111)

<!-- q L202 -->
> unsignedint :: [0-9]+

R-0113 (none; split of R-0111)

<!-- q L203 -->
> quotedname :: '"' urlchar-or-space+ '"'

R-0114 (none; split of R-0111)

<!-- q L204 -->
> alphanumpm :: 'A' | ... | 'Z' | 'a' | ... | 'z' | '0' | ... | '9' | sign

R-0115 (none; split of R-0111)

<!-- q L205-207 -->
> transmit-name-char :: alphanumpm | '.' | '$' | ',' | ';' | ':' | '&' | '=' | '?' | '!' | '*' | '~' | '@' | '#' | '_' | '%' hex hex

R-0116 (none; split of R-0111)

<!-- q L208-210 -->
> Note: Use the "%" escape technique (% followed by the two hex digits that represent the character in the ASCII character set) to insert single or double quotation marks or parentheses.

R-0117 (none; split of R-0111)

<!-- q L211 -->
> urlchar :: transmit-name-char | '(' | ')'

R-0118 (none; split of R-0111)

<!-- q L212 -->
> hex :: '0' | ... | '9' | 'A' | ... | 'F' | 'a' | ... | 'f'

R-0119 (none; split of R-0111)

<!-- q L213 -->
> urlchar-or-space :: urlchar | ' '

R-0120 (none; split of R-0111)

<!-- q L214 -->
> base64-string :: as defined in RFC-1521.

R-0121 (none; split of R-0111)

<!-- q L215-216 -->
> service-error :: 'error' '(' 'request-denied' explanation* ')' | 'error' 'service-unavailable'

R-0122 (none; split of R-0111)

<!-- q L217-218 -->
> label-error :: 'error' '(' 'request-denied' [quotedURL explanation*] ')' | 'error' '(' 'not-labeled' quotedURL* ')'

R-0123 (none; split of R-0111)

<!-- q L219 -->
> explanation :: quotedname

R-0124 (none; split of R-0111)

## §8 Semantics of PICS Labels and Label Lists

<!-- q L223 "The format" .. "application/pics-labels." -->
> The format specified here is intended to be registered with IANA as the MIME type "application/pics-labels.

R-0125 (none) (the quotation stops before the entry's closing double quotation mark, which a marker anchor cannot hold; requirements.yaml carries the exact text)

<!-- q L223 "It allows" .. "bureau." -->
> It allows for transmission of both labels and reasons why labels are not available, and is the format used when labels must be conveyed in a document, along with a document, or from a PICS label bureau.

R-0126 (none)

<!-- q L223 "The labellist" .. "specification)." -->
> The labellist will always be surrounded by parentheses and begin with the PICS version number (1.1 in this specification).

R-0127 (none)

<!-- q L224 "A label" .. "service." -->
> A label list either specifies that there are no labels available at all (e.g., "error (no-ratings ...)") or is separated into sections of labels, one section for each rating service.

R-0128 (none)

<!-- q L224 "The URL" .. "serviceID)." -->
> The URL of each service must be specified (the serviceID).

R-0129 (none)

<!-- q L224 "This is" .. "service." -->
> This is either followed by an error message indicating why no labels are available from that service (service-error) or an overall set of optional information (option*) followed by the keyword "labels" (or "l") and the labels from the service.

R-0130 (none)

<!-- q L224 "The optional" .. "itself." -->
> The optional information provided here applies to every label from the service, unless overridden in the specific label itself.

R-0131 (none)

<!-- q L225 "The first" .. "(label-error)." -->
> The first is an error that applies to retrieving the label for a particular URL (label-error).

R-0132 (none)

<!-- q L225 "The second," .. "values)." -->
> The second, and most common, is a single-label consisting of options (which override those specified with the service), the marker word "ratings" (or "r") and the ratings themselves (a list of category names and values).

R-0133 (none)

<!-- q L225 "Finally, in" .. "parentheses." -->
> Finally, in the special case where the ratings for an entire tree of documents have been requested, any number of single-labels can be transmitted, enclosed in parentheses.

R-0134 (none)

<!-- q L226 "A generic" .. "prefix." -->
> A generic label implicitly rates every URL for which the specified one is a prefix.

R-0135 (none)

Inferred, not verbatim: R-0136 (matching a generic label to a URL). See requirements.yaml.

<!-- q L226 "A specific" .. "w3.org." -->
> A specific (non-generic) label for the same URL, "http://w3.org", does not give any implicit ratings: it merely rates the organization's home page that is fetched by the command "GET /" sent by HTTP to the host w3.org.

R-0137 (none)

<!-- q L226 "A generic label must" .. "applies." -->
> A generic label must include the "for" option specifying the URL to which it applies.

R-0138 (none)

<!-- q L226 "As mentioned" .. "option." -->
> As mentioned above, a generic label should be supplied only if it can be legitimately applied to all documents with URLs that begin with the string specified in the label's for option.

R-0139 (none)

<!-- q L227 "When a" .. "." -->
> When a multi-value is provided, any combination of numbers and ranges of numbers may be specified, with the endpoints of a range separated by a ":".

R-0140 (none)

<!-- q L232 "all subject" .. "value 2." -->
> all subject values between 0.5 and 1.5 (including both endpoints) apply to the item, as does the subject value 2.

R-0141 (none)

## §9 RFC-822 Headers

<!-- q L236 "For use" .. "document." -->
> For use in such protocols, we define a new header, PICS-Label, used to contain the labels described in this document.

R-0142 (none)

<!-- q L238-240 "PICS-Label: <labellist>" .. "above." -->
> PICS-Label: <labellist> where labellist is described according to the syntax above.

R-0143 (none)

<!-- q L240 "Continuation lines" .. "RFC-822." -->
> Continuation lines beginning with whitespace may be used following the specification given in RFC-822.

R-0144 (none)

## §10 Embedding Labels in HyperText Markup Language (HTML)

<!-- q L244 "Labels may" .. "specification." -->
> Labels may be embedded in HTML files as meta-information, using the META element defined in the HTML specification.

R-0145 (none)

<!-- q L244-246 "This embedding" .. "content='labellist'>" -->
> This embedding uses the HTTP header equivalence mechanism: <META http-equiv="PICS-Label" content='labellist'>

R-0146 (none)

<!-- q L248 "Note that" .. "quotes." -->
> Note that the content attribute uses single quotes, because the PICS label syntax uses double quotes.

R-0147 (none)

<!-- q L248 "Any of" .. "entities:" -->
> Any of the following characters appearing within the content must be escaped using SGML entities:

R-0148 (none)

<!-- q L250-252 -->
> ' &#39; /* single quote */ & &amp; /* ampersand */ > &gt; /* greater than */

R-0149 (none)

Inferred, not verbatim: R-0150 (decoding an embedded label). See requirements.yaml.

<!-- q L255 "A label" .. "applies." -->
> A label that is embedded in a document may omit the "for" option, which would normally specify a URL to which the label applies.

R-0151 (none)

<!-- q L255 "A specific" .. "document." -->
> A specific (non-generic) label embedded in a document applies to that document, regardless of what URL is used to locate the document.

R-0152 (none)

<!-- q L255 "A generic" .. "prefix." -->
> A generic label, when embedded in a document that can be retrieved via a "home" URL (i.e., a URL path ending in /), applies to all URLs that include the home URL as a prefix.

R-0153 (none)

## §11 Using HTTP to Request Labels With A Document

<!-- q L261 "HTTP servers" .. "client." -->
> HTTP servers should include PICS label headers only if requested to do so by the client, and should only include the labels from services requested by the client.

R-0154 (none) → split: R-0155, R-0156

<!-- q L261 "HTTP servers" .. "client" -->
> HTTP servers should include PICS label headers only if requested to do so by the client

R-0155 (none; split of R-0154)

<!-- q L261 "should only" .. "client." -->
> should only include the labels from services requested by the client.

R-0156 (none; split of R-0154)

<!-- q L261 "As with" .. "label." -->
> As with labels embedded in documents, the client may assume that a label returned in the http header stream applies to the document requested, regardless of the URL specified in the "for" option of the label.

R-0157 (none)

## §11.2 Explanation of example

<!-- q L290 "The format" .. "are not." -->
> The format of the PICS-Label header field (a labellist) allows the server to respond either with a label or an explanation of why the label is not available, since it would be inappropriate for the server to generate an HTTP error status if the document is available but (some of) the labels are not.

R-0158 (none)

<!-- q L291 "Following the" .. "request." -->
> Following the usual HTTP distinction between HEAD and GET, a client that wishes to examine a rating before retrieving the full document can substitute the word HEAD for GET in the request.

R-0159 (none)

<!-- q L291 "The server" .. "foo.html." -->
> The server responds with exactly the headers shown above, but does not send back the document foo.html.

R-0160 (none)

## §11.3 Detailed Syntax of HTTP Requests for Labels With Document

<!-- q L295 -->
> The following grammar, in modified BNF, describes the syntax of the additional header line to be included in an HTTP request for a document and associated labels.

R-0161 (none)

<!-- q L297-300 -->
> request-header :: 'Protocol-Request: {PICS-1.1 {params ' [completeness] extension* services '}}'

R-0162 (none)

<!-- q L301 -->
> completeness :: 'minimal' | 'short' | 'full' | 'signed'

R-0163 (none)

<!-- q L302-303 -->
> extension :: '{' token-or-quoted-string+ '}' where the first token-or-quoted-string is not 'services'.

R-0164 (none)

<!-- q L304 -->
> token-or-quoted-string :: token | quotedname

R-0165 (none)

<!-- q L305 -->
> token :: alphanumpm+

R-0166 (none)

<!-- q L306 -->
> services :: '{' 'services' quotedURL+ '}'

R-0167 (none)

<!-- q L308 "A request" .. "label." -->
> A request for a minimal label asks that all options be omitted, unless a generic label is returned, in which case the generic and for options must also be included in the label.

R-0168 (none)

<!-- q L308 "A short" .. "appropriate." -->
> A short label includes everything that is included in a minimal label, plus additional options that the server deems appropriate.

R-0169 (none)

<!-- q L308 "A request for a full" .. "needed." -->
> A request for a full label asks that as much information as possible should be sent back in the label, either directly or through the use of a complete-label (or full) option, but no signature-RSA-MD5 option is needed.

R-0170 (none)

<!-- q L309 "A request" .. "itself." -->
> A request for signed labels asks that all the information in a full label should be sent, along with a digital signature on the label itself.

R-0171 (none)

<!-- q L309 "In a" .. "redundant." -->
> In a signed label the information must be transmitted directly as part of the label (and included in the computation of the signature); the complete-label (or full) option may be sent, but it would be redundant.

R-0172 (none) → split: R-0173, R-0174

<!-- q L309 "In a" .. "signature)" -->
> In a signed label the information must be transmitted directly as part of the label (and included in the computation of the signature)

R-0173 (none; split of R-0172)

<!-- q L309 "the complete-label" .. "redundant." -->
> the complete-label (or full) option may be sent, but it would be redundant.

R-0174 (none; split of R-0172)

<!-- q L310 "It is" .. "requested." -->
> It is acceptable for a server to ignore the completeness, either by delivering more or fewer options than requested.

R-0175 (none)

<!-- q L310 "If the" .. "supplied." -->
> If the completeness is omitted, it should be treated as though minimal had been supplied.

R-0176 (none)

<!-- q L310 "For future" .. "option." -->
> For future extensibility, any alphanumeric string may be used for a value of the completeness option.

R-0177 (none)

<!-- q L310 "Servers which" .. "specified." -->
> Servers which receive a value of completeness that they do not recognize must treat it as though minimal had been specified.

R-0178 (none)

<!-- q L311 "The extensions" .. "by it." -->
> The extensions are for future extensions to the protocol; any extensions which are not understood by the server must be ignored by it.

R-0179 (none)

<!-- q L311 "It is" .. "token-or-quoted-string." -->
> It is recommended that experimental extensions use a URL, which dereferences to a description of the extension, as the initial token-or-quoted-string.

R-0180 (none)

<!-- q L312 "Each quotedURL" .. "document." -->
> Each quotedURL in a service specifies a rating service from which the client is requesting a label for the document.

R-0181 (none)

<!-- q L312 "There may" .. "request." -->
> There may be as many repetitions of the quotedURL part of the service as desired, so it is possible to request labels from any number of rating services in a single HTTP request.

R-0182 (none)

## §11.4 Detailed Syntax For HTTP Response Headers For Labels With Document

<!-- q L318 -->
> protocol-header :: 'Protocol: {PICS-1.1 {headers PICS-Label}}'

R-0183 (none)

<!-- q L319 -->
> label-header :: 'PICS-Label: ' labellist

R-0184 (none)

Inferred, not verbatim: R-0185 (when the Protocol header is sent). See requirements.yaml.

## §12 Requesting Labels Separately

<!-- q L323 "A label" .. "below." -->
> A label bureau is an HTTP server that understands a particular query syntax, defined below.

R-0186 (none)

<!-- q L323 "It can" .. "than HTTP." -->
> It can provide labels for documents that reside on other servers, and, indeed, for documents available through protocols other than HTTP.

R-0187 (none)

<!-- q L324 "By default," .. "bureau." -->
> By default, the URL that identifies a rating service also identifies its label bureau.

R-0188 (none)

<!-- q L324 "If a" .. "Systems." -->
> If a client requests the URL that identifies a rating service, a human-readable description of the service is returned, as specified in Rating Services and Rating Systems.

R-0189 (none)

<!-- q L324 "If, on" .. "labels." -->
> If, on the other hand, a client requests the same URL and includes query parameters as defined below, it should be interpreted as a request for labels.

R-0190 (none)

<!-- q L324 "A rating" .. "bureau." -->
> A rating service, however, is not required to act as a label bureau, and it may choose a different URL (perhaps even on a different HTTP server) to act as its label bureau.

R-0191 (none)

## §12.1 Sample Query

<!-- q L336 "This is" .. "a URL." -->
> This is required for encoding characters within a URL.

R-0192 (none)

## §12.2 Detailed Syntax of HTTP Query for Labels Separate From Documents

<!-- q L341 "The following" .. "bureau." -->
> The following grammar, in modified BNF, describes the syntax of GET and POST requests to a label bureau.

R-0193 (none)

<!-- q L341 "The use" .. "query." -->
> The use of the POST request is specified only for backward compatibility with HTTP servers that cannot handle a long GET query.

R-0194 (none)

<!-- q L341 "Its use," .. "deprecated." -->
> Its use, while described in the HTML 2.0 specification (for use in submitting forms, see section 8.2.1 and 8.2.3), is deprecated.

R-0195 (none)

<!-- q L343 -->
> request :: get | post

R-0196 (none)

<!-- q L344-345 -->
> get :: 'get' url-fragment '?' [opt] [format] extension* url+ service+

R-0197 (none)

<!-- q L344-365 "[opt] [format]" .. "quoted URL." -->
> [opt] [format] extension* url+ service+ post :: 'post' url-fragment crlf crlf formencodeddata url-fragment :: the part of the original URL after the host name, as specified in HTTP 1.0. crlf :: carriage return (hex D) followed by line feed (hex A) opt :: 'opt=' option option :: 'generic' | 'normal' | 'tree' | 'generic+tree' format :: [and] 'format=' form form :: 'minimal' | 'short' | 'full' | 'signed' extension :: token '=' token-or-quoted-string where the token is not one of opt, format, u, or s; and token-or-quoted-string follows the quoting conventions specified in RFC-1738 token-or-quoted-string :: token | quotedname token :: alphanumpm+ url :: [and] 'u=' encodedURL service :: [and] 's=' encodedURL boolean :: 't' | 'f' | 'true' | 'false' and :: '&' this must be included unless it immediately follows the ? in the query. encodedURL :: a quoted URL.

R-0198 (none) → split: R-0199, R-0200, R-0201, R-0202, R-0203, R-0204, R-0205, R-0206, R-0207, R-0208, R-0209, R-0210, R-0211, R-0212, R-0213

<!-- q L346 -->
> post :: 'post' url-fragment crlf crlf formencodeddata

R-0199 (none; split of R-0198)

<!-- q L347-348 -->
> url-fragment :: the part of the original URL after the host name, as specified in HTTP 1.0.

R-0200 (none; split of R-0198)

<!-- q L349 -->
> crlf :: carriage return (hex D) followed by line feed (hex A)

R-0201 (none; split of R-0198)

<!-- q L350 -->
> opt :: 'opt=' option

R-0202 (none; split of R-0198)

<!-- q L351 -->
> option :: 'generic' | 'normal' | 'tree' | 'generic+tree'

R-0203 (none; split of R-0198)

<!-- q L352 -->
> format :: [and] 'format=' form

R-0204 (none; split of R-0198)

<!-- q L353 -->
> form :: 'minimal' | 'short' | 'full' | 'signed'

R-0205 (none; split of R-0198)

<!-- q L354-357 -->
> extension :: token '=' token-or-quoted-string where the token is not one of opt, format, u, or s; and token-or-quoted-string follows the quoting conventions specified in RFC-1738

R-0206 (none; split of R-0198)

<!-- q L358 -->
> token-or-quoted-string :: token | quotedname

R-0207 (none; split of R-0198)

<!-- q L359 -->
> token :: alphanumpm+

R-0208 (none; split of R-0198)

<!-- q L360 -->
> url :: [and] 'u=' encodedURL

R-0209 (none; split of R-0198)

<!-- q L361 -->
> service :: [and] 's=' encodedURL

R-0210 (none; split of R-0198)

<!-- q L362 -->
> boolean :: 't' | 'f' | 'true' | 'false'

R-0211 (none; split of R-0198)

<!-- q L363-364 -->
> and :: '&' this must be included unless it immediately follows the ? in the query.

R-0212 (none; split of R-0198)

<!-- q L365 "encodedURL ::" .. "quoted URL." -->
> encodedURL :: a quoted URL.

R-0213 (none; split of R-0198)

<!-- q L365-366 "Following RFC-1738," .. "notation." -->
> Following RFC-1738, quotation and some special characters inside the URL are encoded using "%xx" notation.

R-0214 (none)

<!-- q L367-368 -->
> Alphabetic characters, digits, and the special characters $_-.+!*'(), need not be quoted, but other characters must be.

R-0215 (none)

<!-- q L369-373 -->
> This does imply that the colon (:) must be encoded as %3A and slash (/) as %2F. formencodeddata :: The query as specified for get but encoded into MIME type application/x-www-form-encoded as described in sections 8.2.1 and 8.2.3 of HTML 2.0.

R-0216 (none) → split: R-0217, R-0218

<!-- q L369-370 -->
> This does imply that the colon (:) must be encoded as %3A and slash (/) as %2F.

R-0217 (none; split of R-0216)

<!-- q L371-373 -->
> formencodeddata :: The query as specified for get but encoded into MIME type application/x-www-form-encoded as described in sections 8.2.1 and 8.2.3 of HTML 2.0.

R-0218 (none; split of R-0216)

## §12.3 Response to Query for Labels Separate From Documents

<!-- q L377 -->
> The label bureau responds by sending back a document of type "application/pics-labels."

R-0219 (none)

<!-- q L378 "Unless the" .. "query." -->
> Unless the document indicates an overall error, there should be one service-info for each rating service requested in the query.

R-0220 (none)

<!-- q L378 "Each service-info" .. "requested URL." -->
> Each service-info should have an error message or a label (or list of labels, in the case of a "tree" query) for each requested URL.

R-0221 (none)

<!-- q L379 "The query's" .. "response." -->
> The query's ordering must be preserved in the response.

R-0222 (none)

<!-- q L379 "That is," .. "query." -->
> That is, the information from the rating services must be presented in the same order the rating services appear in the query, and the labels from each service must be presented in the same order the URLs appear in the query.

R-0223 (none) → split: R-0224, R-0225

<!-- q L379 "That is," .. "the query" -->
> That is, the information from the rating services must be presented in the same order the rating services appear in the query

R-0224 (none; split of R-0223)

<!-- q L379 "the labels" .. "query." -->
> the labels from each service must be presented in the same order the URLs appear in the query.

R-0225 (none; split of R-0223)

<!-- q L379 "If a" .. "appear." -->
> If a rating service or label is not provided, the error message should appear in the same position that the service-info or label would appear.

R-0226 (none)

<!-- q L379 "Because order" .. "rated." -->
> Because order is preserved, it is acceptable (except where indicated below) to omit from the labels the "for" option which indicates the URL being rated.

R-0227 (none)

<!-- q L379 "The client" .. "rating." -->
> The client should match the label positionally with the URL for which it requested a rating.

R-0228 (none)

<!-- q L380 "Given a" .. ")." -->
> Given a URL (e.g., "http://www.greatdocs.com/foo/"), a descendant URL is any URL that contains the original as a prefix (e.g., "http://www.greatdocs.com/foo/bar/bat.htm").

R-0229 (none)

<!-- q L380 "A child" .. ")." -->
> A child URL is any descendant URL that does not contain any additional '/' characters (e.g., "http://www.greatdocs.com/foo/ba").

R-0230 (none)

<!-- q L380 "An ancestor" .. ")." -->
> An ancestor URL is any URL that is a prefix of the original (e.g., "http://www.greatdocs.com/f").

R-0231 (none)

<!-- q L380 "Note that" .. "those URLs." -->
> Note that ancestry and descendence is determined strictly by case-sensitive string matching on URLs, not by any links that may appear in html documents retrieved using those URLs.

R-0232 (none)

<!-- q L380 "Note that any" .. "strings." -->
> Note that any quotation such as %3A for colon (:) or %2F for slash (/) is unencoded prior to comparing URL strings.

R-0233 (none)

<!-- q L381 "opt=normal, or" .. "specified." -->
> opt=normal, or omitting the opt completely, requests specific labels for the URLs specified.

R-0234 (none)

<!-- q L381 "If no" .. "ancestor URL." -->
> If no specific label is available for a requested URL, the server may choose to send a generic label for the requested URL or for an ancestor URL.

R-0235 (none)

<!-- q L381 "In this" .. "returned." -->
> In this case, it is required that the "for" and "generic" options be included in the label, to specify exactly what rating is being returned.

R-0236 (none)

<!-- q L381 "Note that" .. "document." -->
> Note that the "for" option may specify a URL string which does not appear to match the request URL, perhaps due to the server knowing about the existence of an alternative URL for the same document.

R-0237 (none)

<!-- q L381-382 "In that" .. "labels." -->
> In that case, the server is suggesting that the label applies to the request URL, though a suspicious client may choose not to believe the suggestion. opt=generic requests generic labels.

R-0238 (none) → split: R-0239, R-0240

<!-- q L381 "In that" .. "suggestion." -->
> In that case, the server is suggesting that the label applies to the request URL, though a suspicious client may choose not to believe the suggestion.

R-0239 (none; split of R-0238)

<!-- q L382 "opt=generic requests" .. "labels." -->
> opt=generic requests generic labels.

R-0240 (none; split of R-0238)

<!-- q L382 "For each" .. "descendant URLs." -->
> For each requested URL, the desired response is a generic label that applies to the requested URL and all descendant URLs.

R-0241 (none)

<!-- q L382 "A generic" .. "prefix." -->
> A generic label for the requested URL, or a generic label for any ancestor URL, would satisfy this request, as such a generic label would apply to all URLs containing the requested URL as a prefix.

R-0242 (none)

<!-- q L382-383 "If no" .. "labels." -->
> If no such generic label is available, the server should include the "no-label" message rather than sending back a specific label. opt=tree requests a tree of labels.

R-0243 (none) → split: R-0244, R-0245

<!-- q L382 "If no" .. "label." -->
> If no such generic label is available, the server should include the "no-label" message rather than sending back a specific label.

R-0244 (none; split of R-0243)

<!-- q L383 "opt=tree requests" .. "labels." -->
> opt=tree requests a tree of labels.

R-0245 (none; split of R-0243)

<!-- q L383 "For each" .. "requested URL." -->
> For each requested URL, the desired response is a set of labels (both specific and generic) that apply to descendants of the requested URL.

R-0246 (none)

<!-- q L383 "In the" .. "parentheses." -->
> In the response, everywhere a label would normally be expected in the response, a set of simple-labels will be returned, surrounded by parentheses.

R-0247 (none)

<!-- q L383 "All labels" .. "option." -->
> All labels produced in response to this query must include a for option.

R-0248 (none)

<!-- q L383 "The minimum" .. "requested URL." -->
> The minimum response expected is the set of labels that would have been generated if a query had been issued, with opt=normal specified, for each known child of the requested URL.

R-0249 (none)

<!-- q L383-384 "Additional labels" .. "labels." -->
> Additional labels may also be returned, typically either generic labels for ancestor URLs or labels for descendant URLs farther down the hierarchy than children. opt=generic+tree is similar to the opt=tree request, but returns only generic labels.

R-0250 (none) → split: R-0251, R-0252

<!-- q L383 "Additional labels" .. "children." -->
> Additional labels may also be returned, typically either generic labels for ancestor URLs or labels for descendant URLs farther down the hierarchy than children.

R-0251 (none; split of R-0250)

<!-- q L384 "opt=generic+tree is" .. "labels." -->
> opt=generic+tree is similar to the opt=tree request, but returns only generic labels.

R-0252 (none; split of R-0250)

<!-- q L384 "As with" .. "detail." -->
> As with opt=tree, the server can choose the amount of detail.

R-0253 (none)

<!-- q L384 "The minimum" .. "requested URL." -->
> The minimum response expected is the set of labels that would have been generated if a query had been issued, with opt=generic specified, for each known child of the requested URL.

R-0254 (none)

<!-- q L384 "Additional labels" .. "ancestor URLs." -->
> Additional labels may also be returned, typically generic labels for ancestor URLs.

R-0255 (none)

<!-- q L384 "All labels" .. "option." -->
> All labels produced in response to this query must include a for option.

R-0256 (none)

<!-- q L385 "It is" .. "request." -->
> It is permitted to include more than one URL and/or service in the request.

R-0257 (none)

<!-- q L385 "Requesting u" .. "queries.)" -->
> Requesting u URLs and s services results in a total of u x s labels being generated (or label sets in the case of tree and generic+tree queries.)

R-0258 (none)

<!-- q L386 "The format=" .. "labels." -->
> The format= specifies the optional information that should be transmitted with the labels.

R-0259 (none)

<!-- q L386 "It is" .. "minimal)." -->
> It is treated precisely as the similar keywords would be when sent to a document server as the completeness (see Detailed Syntax of HTTP Requests for Labels With Document), except that the default is full (rather than minimal).

R-0260 (none)

<!-- q L386 "Servers which" .. "specified." -->
> Servers which receive a value of completeness that they do not recognize must treat it as though the default, full, had been specified.

R-0261 (none)

<!-- q L386 "All labels" .. "option." -->
> All labels produced in response to this query must include a for option.

R-0262 (none)

## §13 MICs and Digital Signatures

<!-- q L390 "They may" .. "together." -->
> They may be used independently or together.

R-0263 (none)

<!-- q L392-394 "PICS labels" .. "field." -->
> PICS labels contain three option fields intended to help deter this kind of problem: At If the objective is to simply detect accidental changes, then the date of last modification of the document can be calculated when the label is created and stored in the at field.

R-0264 (none) → split: R-0265

<!-- q L394 "If the" .. "field." -->
> If the objective is to simply detect accidental changes, then the date of last modification of the document can be calculated when the label is created and stored in the at field.

R-0265 (none; split of R-0264)

Inferred, not verbatim: R-0266 (checking at). See requirements.yaml.

<!-- q L395-396 "Until or" .. "updated." -->
> Until or exp If the document is expected to be updated infrequently or periodically, the label can contain an expiration date that should cause the label to be invalid before the document is next updated.

R-0267 (none) → split: R-0268

<!-- q L396 "If the" .. "updated." -->
> If the document is expected to be updated infrequently or periodically, the label can contain an expiration date that should cause the label to be invalid before the document is next updated.

R-0268 (none; split of R-0267)

Inferred, not verbatim: R-0269 (expiry of a label). See requirements.yaml.

<!-- q L397-398 "MIC-md5 or" .. "created." -->
> MIC-md5 or md5 If the label is intended to apply only to the data that was actually rated, then a form of checksum (called a "message digest") can be applied to the data when the label is created.

R-0270 (none) → split: R-0271

<!-- q L398 "If the" .. "created." -->
> If the label is intended to apply only to the data that was actually rated, then a form of checksum (called a "message digest") can be applied to the data when the label is created.

R-0271 (none; split of R-0270)

<!-- q L398 "The message" .. "field." -->
> The message digest is converted into US-ASCII characters using MIME base-64 encoding and stored in the MIC-md5 (also called md5) field.

R-0272 (none)

<!-- q L398 "When the" .. "compared." -->
> When the document is later retrieved, the same algorithm can be used to recompute the message digest and the two digests can be compared.

R-0273 (none)

<!-- q L400 "Instead, we" .. "encoding." -->
> Instead, we recommend the direct use of the MD5 algorithm on the source document and conversion of the result to base64 encoding.

R-0274 (none)

<!-- q L400 "This resulting" .. "option." -->
> This resulting string is included directly in the mic-md5 (md5) label option.

R-0275 (none)

Inferred, not verbatim: R-0276 (form and comparison of the MIC value). See requirements.yaml.

<!-- q L401 "Because PICS" .. "document." -->
> Because PICS labels can be embedded inside of the documents they label, care must be taken to ensure that the message digest is computed excluding all PICS labels in the document.

R-0277 (none)

<!-- q L401 "For HTML" .. "elements)." -->
> For HTML documents, this means that the digest must be computed after removing all META elements that include PICS labels (and any whitespace immediately following the end of each of these meta elements).

R-0278 (none)

Inferred, not verbatim: R-0279 (bytes the MIC is computed over). See requirements.yaml.

<!-- q L402-403 "The RSA" .. "key pair." -->
> The RSA signature technique works as follows: In order to sign a label, the rating service (or people authorized to generate labels on behalf of the service) needs a "public key pair.

R-0280 (none) → split: R-0281 (the quotation stops before the entry's closing double quotation mark, which a marker anchor cannot hold; requirements.yaml carries the exact text)

<!-- q L403 "In order" .. "key pair." -->
> In order to sign a label, the rating service (or people authorized to generate labels on behalf of the service) needs a "public key pair.

R-0281 (none; split of R-0280) (the quotation stops before the entry's closing double quotation mark, which a marker anchor cannot hold; requirements.yaml carries the exact text)

<!-- q L403 "One of" .. "labels." -->
> One of these (the private key) must be kept secret by the service; the other (the public key) must be distributed to anyone who is interested in verifying the signatures on the service's labels.

R-0282 (none) → split: R-0283, R-0284

<!-- q L403 "One of" .. "service" -->
> One of these (the private key) must be kept secret by the service

R-0283 (none; split of R-0282)

<!-- q L403 "the other" .. "labels." -->
> the other (the public key) must be distributed to anyone who is interested in verifying the signatures on the service's labels.

R-0284 (none; split of R-0282)

<!-- q L404 "After creating" .. "label." -->
> After creating a label, the service converts it to a special form specified below and computes the MD5 message digest of the label.

R-0285 (none)

<!-- q L404 "It then" .. "digest." -->
> It then uses the service's private key to encrypt the digest.

R-0286 (none)

<!-- q L404 "This encrypted" .. "above." -->
> This encrypted digest is the digital signature, and it is converted to US-ASCII using the same base64 encoding technique mentioned above.

R-0287 (none)

<!-- q L404 "The US-ASCII" .. "client." -->
> The US-ASCII version (split into 60 character lines) is stored in the signature-rsa-md5 option of the label when it is transmitted to the client.

R-0288 (none)

<!-- q L405 "When the" .. "signed." -->
> When the client receives a label and wants to verify the signature it takes the label it received and converts it back into the same special form in which it was originally signed.

R-0289 (none)

<!-- q L405 "The client" .. "special form." -->
> The client recomputes the message digest on this special form.

R-0290 (none)

<!-- q L405 "It also" .. "public key." -->
> It also takes the contents of the signature-rsa-md5 option, combines all of the lines back into a single string of US-ASCII characters, converts these from base64 into their original (binary) form, and decrypts them using the service's public key.

R-0291 (none)

Inferred, not verbatim: R-0292 (joining the signature lines). See requirements.yaml.

Inferred, not verbatim: R-0293 (which public key verifies a label). See requirements.yaml.

<!-- q L405 "If the" .. "invalid." -->
> If the result isn't the same as the message digest it computed the signature is invalid.

R-0294 (none)

<!-- q L406 "Since there" .. "chooses." -->
> Since there is no clearly established solution available today, PICS assumes that each service will distribute the public keys in some way it chooses.

R-0295 (none)

<!-- q L406 "It also" .. "invalidated." -->
> It also assumes that no keys will ever have to be invalidated.

R-0296 (none)

<!-- q L407 "This can" .. "signature." -->
> This can be done (each signs the label without the other's signature), but it becomes quite difficult to distribute the public keys needed to verify the signature.

R-0297 (none)

## §13.1 Signature Details

<!-- q L411 "PICS specifically" .. "digest." -->
> PICS specifically requires the use of the RSA signature algorithm with the MD5 message digest.

R-0298 (none)

<!-- q L412 "PICS does" .. "signatures." -->
> PICS does not specify the key length to be used for the digital signatures.

R-0299 (none)

<!-- q L412 "Individual services" .. "choice." -->
> Individual services will need to investigate the legal and technical ramifications involved and make a choice.

R-0300 (none)

<!-- q L413-414 "The special" .. "transmitted." -->
> The special form of the label that is used for signatures is computed as follows: The service must decide which options it will include in the signed label when it is transmitted.

R-0301 (none) → split: R-0302, R-0303

<!-- q L413 -->
> The special form of the label that is used for signatures is computed as follows:

R-0302 (none; split of R-0301)

<!-- q L414 "The service" .. "transmitted." -->
> The service must decide which options it will include in the signed label when it is transmitted.

R-0303 (none; split of R-0301)

<!-- q L414 "Any options" .. "signature." -->
> Any options not transmitted with the signature cannot be used in the computation of the signature.

R-0304 (none)

<!-- q L414 "We recommend" .. "signature-rsa-md5." -->
> We recommend that all options with known values be included with the exception of signature-rsa-md5.

R-0305 (none)

<!-- q L414 "Any option may" .. "omitted." -->
> Any option may be omitted, but it will be common for the options mic-md5 (or md5) and full (or complete-label) to be omitted.

R-0306 (none)

<!-- q L414 "The signature-rsa-md5" .. "options." -->
> The signature-rsa-md5 option is never included in the list of options.

R-0307 (none)

<!-- q L415 "The selected" .. "complete-label)." -->
> The selected options are sorted alphabetically by their shortest name (i.e. use full instead of complete-label).

R-0308 (none)

Inferred, not verbatim: R-0309 (order of option names in the special form). See requirements.yaml.

<!-- q L415 "If a" .. "this list." -->
> If a selected option has a default value and it is the same as the value to be used in the label, the option is omitted from this list.

R-0310 (none)

<!-- q L416 "For each" .. "space." -->
> For each option in the list (in order), the short name is put into the label followed by a single space followed by the value of the option, followed by a space.

R-0311 (none)

<!-- q L416 "The shortest" .. "insensitive." -->
> The shortest form of a value is used, and strings are output in lower case if they are case insensitive.

R-0312 (none) → split: R-0313, R-0314

<!-- q L416 "The shortest" .. "is used" -->
> The shortest form of a value is used

R-0313 (none; split of R-0312)

<!-- q L416 "strings are" .. "insensitive." -->
> strings are output in lower case if they are case insensitive.

R-0314 (none; split of R-0312)

Inferred, not verbatim: R-0315 (shortest form of a boolean). See requirements.yaml.

Inferred, not verbatim: R-0316 (form of quoted values in the special form). See requirements.yaml.

<!-- q L417 -->
> After all of the options has been output, output the characters "r (".

R-0317 (none)

<!-- q L418 "Output the" .. "space." -->
> Output the transmission names and their values, in alphabetical order by transmission name (using the US-ASCII character collating sequence for "alphabetical order"), separating the transmission name from the value by a single space.

R-0318 (none)

<!-- q L418 "In outputting" .. "multi-value." -->
> In outputting the value, no whitespace is permitted except for a single space used to separate items in a multi-value.

R-0319 (none)

<!-- q L419 -->
> Output a ")"

R-0320 (none)

Inferred, not verbatim: R-0321 (layout of the special form). See requirements.yaml.

Inferred, not verbatim: R-0322 (bytes the signature digest covers). See requirements.yaml.

<!-- q L420 "When the" .. "service-info." -->
> When the client computes the special label format described above, it will use all options available to it: both those in the single-label and in the service-info.

R-0323 (none)

<!-- q L420 "The transmitted" .. "option." -->
> The transmitted set must include any options that the server ships as part of the service-info, unless either the value specified in the service-info or the value of the option for this label is the default value of the option.

R-0324 (none)

Inferred, not verbatim: R-0325 (option set that is signed). See requirements.yaml.

Inferred, not verbatim: R-0326 (what a signature binds). See requirements.yaml.

## §14 Glossary

<!-- q L433-439 "The content" .. "a URL." -->
> The content label may accompany the document it is about or be available separately. content rating See content label. dimension See category. document Any item that can be referred to by a URL.

R-0327 (none) → split: R-0328

<!-- q L439 "Any item" .. "a URL." -->
> Any item that can be referred to by a URL.

R-0328 (none; split of R-0327)

<!-- q L453 "If they" .. "retrieved." -->
> If they match, for all practical purposes, it is a proof that the label really belongs to the information that has been retrieved.

R-0329 (none)

<!-- q L471 "This is" .. "possible." -->
> This is distinct from the category name in as much as the transmission name must be language-independent, encoded in US-ASCII, and as short as reasonably possible.

R-0330 (none)

<!-- q L471 "Within a" .. "distinct." -->
> Within a single rating system the transmission names of all categories must be distinct.

R-0331 (none)

<!-- q L471 "URLs, while" .. "names." -->
> URLs, while generally longer than desired, can be used as transmission names.

R-0332 (none)

## §17 Appendix A: An Algorithm for Locating a Label Bureau

<!-- q L522 "The following" .. "at MIT." -->
> The following suggestion comes from Prof. David Karger at MIT.

R-0333 (none)

<!-- q L523 "Our algorithm" .. "manner." -->
> Our algorithm simply assumes that they exist and are equivalent, and that the network's Domain Name System (DNS) has records which map the single well-defined name for the label bureau to multiple Internet addresses, in the usual manner.

R-0334 (none)

<!-- q L524 "When client" .. "through DNS." -->
> When client software starts, it should attempt to resolve the name of the label bureau it wishes to use (we assume one label bureau, but the algorithm extends in an obvious manner to multiple bureaus) through DNS.

R-0335 (none)

<!-- q L524 "If it" .. "bureau." -->
> If it receives more than one host address, it saves the entire list and chooses two at random, labeling one the "primary" and the other the "secondary" bureau.

R-0336 (none)

<!-- q L524 "Alternatively, these" .. "starts." -->
> Alternatively, these may be configuration parameters of the client software that are then validated when the software starts.

R-0337 (none)

<!-- q L524 "It also" .. "value." -->
> It also divides 60 minutes by the total number of address it can find for the label bureau, sets a timer to this value, and remembers this as the "threshold" value.

R-0338 (none)

<!-- q L525 "Every time" .. "following." -->
> Every time the client wishes to contact the label bureau it does the following.

R-0339 (none)

<!-- q L525 "If the" .. "is used." -->
> If the timer is below the threshold, the primary bureau address is used.

R-0340 (none)

<!-- q L525 "Otherwise, the" .. "address." -->
> Otherwise, the query is sent to both the primary and the secondary label bureau address.

R-0341 (none)

<!-- q L525 "When the" .. "closed down." -->
> When the first answer arrives the connection to both label bureaus is closed down.

R-0342 (none)

<!-- q L525 "The bureau" .. "bureau." -->
> The bureau which answered first becomes the primary bureau.

R-0343 (none)

<!-- q L525 "In any" .. "value." -->
> In any case, a new secondary bureau address is chosen at random and the timer is reset to the threshold value.

R-0344 (none)

Inferred, not verbatim: R-0345 (drawing a new secondary). See requirements.yaml.

Inferred, not verbatim: R-0346 (timer semantics). See requirements.yaml.

<!-- q L526 "When the" .. "possible." -->
> When the HTTP protocol is updated to allow "keep alive" connections to a server, the PICS client should keep its connection to the primary label bureau alive as long as possible.

R-0347 (none)

<!-- q L526 "Then, instead" .. "be made." -->
> Then, instead of simply accepting the first response and considering the responder as the primary, a more careful measurement must be made.

R-0348 (none)

<!-- q L526 "The time" .. "trip time." -->
> The time required to send the query and receive the response must be measured, rather than the total transaction time: connection setup costs can be quite high, and would distort the measurement if one compared the round trip time to the primary bureau through an existing connection to the time to establish the connection to the secondary bureau plus the round trip time.

R-0349 (none)

## Source defects

Inconsistencies and gaps in the source, each verified by this pass against the .txt, the Appendix B
examples worked through the grammar by hand. Recorded, never healed. Each names the entries it bears
on; quotations are markers like everything above. SD-E collects the editorial ones.

### SD-1: no-ratings: a whole-list answer in the prose, one service-info among several in the grammar

§8 (Semantics of PICS Labels and Label Lists) offers the no-ratings error as the alternative to a list of per-service sections, and §12.3 (Response to Query for Labels Separate From Documents) excepts an overall error from its one-service-info-per-service rule. The grammar makes the same form one alternative of `service-info`, so it can stand beside other services' sections, and it carries no `serviceID`. Every Appendix B response uses it that way, as the third of three service-infos, answering for the unknown service, so it is identified only by its position (R-0226). Entries: R-0128, R-0082, R-0220.

<!-- q L224 "A label list either" .. "each rating service." -->
> A label list either specifies that there are no labels available at all (e.g., "error (no-ratings ...)") or is separated into sections of labels, one section for each rating service.

<!-- q L152 -->
> service-info :: 'error' '(no-ratings' explanation* ')'

<!-- q L608 -->
> error (no-ratings "unknown service"))

### SD-2: the response rules name a no-label message the grammar does not have

The opt=generic item of §12.3 (Response to Query for Labels Separate From Documents) tells the server to answer with a no-label message. The grammar's error forms are `no-ratings`, `request-denied`, `service-unavailable` and `not-labeled`, and the Appendix B generic response answers with `not-labeled`. Entries: R-0244, R-0123.

<!-- q L382 "If no such generic" .. "specific label." -->
> If no such generic label is available, the server should include the "no-label" message rather than sending back a specific label.

<!-- q L218 -->
> | 'error' '(' 'not-labeled' quotedURL* ')'

<!-- q L592 -->
> error (not-labeled "http://www.w3.org/unknown")

### SD-3: embedded generic labels and the for option

§5 (General Format) and §8 (Semantics of PICS Labels and Label Lists) require every generic label to carry `for`. §10 (Embedding Labels in HyperText Markup Language (HTML)) lets any embedded label omit it, and scopes an embedded generic label by the home URL its document is retrieved from, not by a `for` string. An embedded generic label without `for` conforms to §10 and not to §5 or §8; with a `for`, which of the two prefixes sets its scope is not stated. Entries: R-0034, R-0138, R-0151, R-0153.

<!-- q L89 "All generic labels" .. "the for option." -->
> All generic labels must also include the for option.

<!-- q L255 "A label that is embedded" .. "label applies." -->
> A label that is embedded in a document may omit the "for" option, which would normally specify a URL to which the label applies.

<!-- q L255 "A generic label, when embedded" .. "as a prefix." -->
> A generic label, when embedded in a document that can be retrieved via a "home" URL (i.e., a URL path ending in /), applies to all URLs that include the home URL as a prefix.

### SD-4: completeness and format values: closed in the grammars, open in the prose

Both grammars list exactly four values. The prose of §11.3 (Detailed Syntax of HTTP Requests for Labels With Document) admits any alphanumeric string and says what a server does with one it does not recognise; §12.3 (Response to Query for Labels Separate From Documents) says the same of `format=`, with `full` as the fallback. A strict parser of either grammar rejects what the prose permits. Entries: R-0163, R-0205, R-0177, R-0178, R-0261.

<!-- q L301 -->
> completeness :: 'minimal' | 'short' | 'full' | 'signed'

<!-- q L353 -->
> form :: 'minimal' | 'short' | 'full' | 'signed'

<!-- q L310 "For future extensibility" .. "completeness option." -->
> For future extensibility, any alphanumeric string may be used for a value of the completeness option.

### SD-5: boolean is defined in the wrong grammar

The label grammar of §7 (Detailed Syntax) uses `boolean` for `generic` and `gen` and never defines it. The only definition is in the request grammar of §12.2 (Detailed Syntax of HTTP Query for Labels Separate From Documents), where no production uses it. Entries: R-0090, R-0211.

<!-- q L164 -->
> | 'generic' boolean | 'gen' boolean

<!-- q L362 -->
> boolean :: 't' | 'f' | 'true' | 'false'

### SD-6: one production name, two meanings

The three grammars share one namespace without saying so. `option` is a label option in §7 (Detailed Syntax) and a query mode in §12.2 (Detailed Syntax of HTTP Query for Labels Separate From Documents); `extension` is a braced list in the §11.3 (Detailed Syntax of HTTP Requests for Labels With Document) header grammar and a name=value pair in the §12.2 query grammar (and a label option keyword in §7); `token-or-quoted-string` and `token` are defined twice, identically. A grammar of the whole document has to rename one of each pair. Entries: R-0089, R-0203, R-0164, R-0206, R-0165, R-0207, R-0166, R-0208.

<!-- q L161 -->
> option :: labeloption | documentoption | otheroption

<!-- q L351 -->
> option :: 'generic' | 'normal' | 'tree' | 'generic+tree'

<!-- q L302-303 -->
> extension :: '{' token-or-quoted-string+ '}' where the first token-or-quoted-string is not 'services'.

<!-- q L354-357 -->
> extension :: token '=' token-or-quoted-string where the token is not one of opt, format, u, or s; and token-or-quoted-string follows the quoting conventions specified in RFC-1738

### SD-7: a quotedname cannot hold a slash

`quotedname` is built from `urlchar`, which is `transmit-name-char` plus the two parentheses, and `transmit-name-char` has no slash. Yet the `by` option may carry a base-64 encoded set of certificates, and base64's alphabet includes the slash; §11.3 (Detailed Syntax of HTTP Requests for Labels With Document) recommends a URL as the first item of an experimental extension, which neither `token` (letters, digits and signs) nor `quotedname` can hold; and a `comment` cannot quote a URL. Entries: R-0114, R-0116, R-0024, R-0180.

<!-- q L203 -->
> quotedname :: '"' urlchar-or-space+ '"'

<!-- q L205-207 -->
> transmit-name-char :: alphanumpm | '.' | '$' | ',' | ';' | ':' | '&' | '=' | '?' | '!' | '*' | '~' | '@' | '#' | '_' | '%' hex hex

<!-- q L311 "It is recommended" .. "token-or-quoted-string." -->
> It is recommended that experimental extensions use a URL, which dereferences to a description of the extension, as the initial token-or-quoted-string.

### SD-8: URLs as transmission names do not fit transmit-name

The entry of §14 (Glossary) for transmission name lets a URL be one. `transmit-name` admits the colon but uses the slash only as a separator with at least one character on each side, so the double slash after a URL scheme is not a `transmit-name`. Entries: R-0332, R-0109.

<!-- q L471 "URLs, while generally" .. "transmission names." -->
> URLs, while generally longer than desired, can be used as transmission names.

<!-- q L199 -->
> transmit-name :: transmit-name-char+ ['/' transmit-name]

### SD-9: whitespace is not ignored

The §7 (Detailed Syntax) note says whitespace is ignored outside quoted strings. A `transmit-name` may contain digits and full stops, so without the whitespace between a category and its number the two would lex as one `transmit-name`. The note's own next sentence, the lead-in of §6 (Example) and the steps of §13.1 (Signature Details), which put a single space between a transmission name and its value, all treat whitespace as a separator whose amount, not presence, is insignificant. Inferred: R-0063. Entries: R-0061, R-0062, R-0318.

<!-- q L140 -->
> Whitespace is ignored except in quoted strings. Multiple contiguous whitespace characters can be treated as though they were a single space character.

### SD-10: labels said to travel from the client to the server

The §7 (Detailed Syntax) note on US-ASCII scopes the specification to what travels over the wire in one direction, client to server. Labels travel the other way, from document servers (§11, Using HTTP to Request Labels With A Document) and label bureaus (§12, Requesting Labels Separately) to clients; only the requests go client to server. Entry: R-0066.

<!-- q L142 "This specification is strictly" .. "of US-ASCII." -->
> This specification is strictly about information carried over the wire from the client to the server, and it requires the use of US-ASCII.

### SD-11: minute 60

The minute production admits 00 through 60 while the hour stops at 23, so a time of 23:60 is a valid quoted-ISO-date by the grammar. Entry: R-0100.

<!-- q L186 -->
> mm :: two digits of minute (00 through 60)

### SD-12: a for rule in the format= item names no query

The opt=tree and opt=generic+tree items each end by requiring `for` on every label of the response to that mode. The format= item ends with the same sentence, but it describes a parameter, not a query. Read as covering every label bureau query, it withdraws line 379's permission to omit `for` because order is preserved; read as a stray copy, it binds nothing. Appendix B's responses carry `for` throughout and fit either reading. Entries: R-0262, R-0227, R-0248, R-0256.

<!-- q L386 "All labels produced" .. "for option." -->
> All labels produced in response to this query must include a for option.

<!-- q L379 "Because order is preserved" .. "being rated." -->
> Because order is preserved, it is acceptable (except where indicated below) to omit from the labels the "for" option which indicates the URL being rated.

### SD-13: Appendix B puts the parameter separator inside the quoted URLs

In all four Appendix B requests every quoted `u=` and `s=` value but the last ends in an unencoded ampersand inside its closing quotation mark, and the first `u=` value ends in a plus sign before it. The request of §12.1 (Sample Query) puts the ampersand outside; the `and` production requires one between parameters; and the encodedURL rule (R-0215) lists the characters that may stay unencoded, the ampersand not among them. Read by the grammar, every requested URL and every service URL but the last ends in an ampersand, no requested URL matches the URLs the responses label, and nothing separates the parameters. Entries: R-0209, R-0212, R-0215.

<!-- q L562 -->
> u="http%3A%2F%2Fwww.w3.org%2Fpub%2FWWW%2F+&"

<!-- q L563 -->
> u="http%3A%2F%2Fwww.w3.org%2Fpub%2FWWW%2FTheProject.html&"

<!-- q L332 -->
> u="http%3A%2F%2Fwww.questionable.org%2Fimages"&

### SD-14: generic+tree spelled two ways

The query-mode production writes generic+tree with a literal plus sign; the Appendix B request sends it %2B-encoded. The plus sign is one of the characters the encodedURL rule leaves unencoded, while a server that decodes the query as form data, the encoding §12.2 (Detailed Syntax of HTTP Query for Labels Separate From Documents) names for POST, reads a plus sign as a space [outside this source: HTML 2.0's form encoding writes a space as a plus sign]. Entries: R-0203, R-0202.

<!-- q L351 -->
> option :: 'generic' | 'normal' | 'tree' | 'generic+tree'

<!-- q L733 -->
> GET /ratings?opt=generic%2Btree&

### SD-15: the label bureau grammar's extension takes no ampersand

In the `get` production the `format`, `url` and `service` items each begin with an optional `and`; `extension` does not, although the `and` production requires an ampersand everywhere except straight after the question mark. By the grammar an extension after `opt` or `format` is glued to it. Entries: R-0206, R-0212, R-0197.

<!-- q L354-357 -->
> extension :: token '=' token-or-quoted-string where the token is not one of opt, format, u, or s; and token-or-quoted-string follows the quoting conventions specified in RFC-1738

<!-- q L363-364 -->
> and :: '&' this must be included unless it immediately follows the ? in the query.

### SD-16: the special form is under-specified

Signer and verifier must build identical bytes, and the steps of §13.1 (Signature Details) leave seven things open. (a) Options at their default value are dropped, but no option's default is defined anywhere; generic has the only inferable one (R-0033). (b) No production has a defined shortest form: booleans have short forms, numbers several spellings, extension values none stated (R-0315, R-0316). (c) What separates one category's value from the next transmission name is not stated (R-0321). (d) The order of repeated comment or extension options, which §7 (Detailed Syntax) allows, is not stated (R-0309). (e) Whether a quoted value keeps its quotation marks is not stated (R-0316). (f) A category with no value may be omitted or sent as an empty multi-value (§7); the steps say for neither what is output. (g) For comment and extension, which may repeat, whether a label's occurrences override the service-info's or add to them is not stated, so the effective option set is undetermined (R-0325). Entries: R-0310, R-0313, R-0318, R-0074, R-0072, R-0067.

<!-- q L415 "If a selected option" .. "this list." -->
> If a selected option has a default value and it is the same as the value to be used in the label, the option is omitted from this list.

<!-- q L416 "The shortest form" .. "case insensitive." -->
> The shortest form of a value is used, and strings are output in lower case if they are case insensitive.

<!-- q L418 "Output the transmission" .. "a single space." -->
> Output the transmission names and their values, in alphabetical order by transmission name (using the US-ASCII character collating sequence for "alphabetical order"), separating the transmission name from the value by a single space.

### SD-17: the RSA signature format is not specified

§13 (MICs and Digital Signatures) has the service encrypt the digest with its private key. It names no padding and no encoding of the digest before the RSA operation; §13.1 (Signature Details) leaves the key length open; and interoperation rests on RSAREF 2.0's routines, which the document points to and does not specify. Two independent implementations can produce signatures the other cannot check. Entries: R-0286, R-0291, R-0298, R-0299.

<!-- q L404 "It then uses" .. "the digest." -->
> It then uses the service's private key to encrypt the digest.

<!-- q L412 "PICS does not specify" .. "digital signatures." -->
> PICS does not specify the key length to be used for the digital signatures.

### SD-18: two signatures, one signature option

§13 (MICs and Digital Signatures) describes a label signed twice, by the rating service and by the content producer, each signing without the other's signature. §7 (Detailed Syntax) lets only comment and extension repeat within a single-label or service-info, and an option of the service-info is overridden by the label's own, so a label carries one `signature-RSA-MD5`; no syntax carries the second. Entries: R-0297, R-0074, R-0067.

<!-- q L407 "This can be done" .. "verify the signature." -->
> This can be done (each signs the label without the other's signature), but it becomes quite difficult to distribute the public keys needed to verify the signature.

<!-- q L146 "The only options" .. "comment and extension" -->
> The only options that may occur more than once in a particular single-label or service-info are comment and extension

### SD-19: whether a URL is its own prefix is never stated

§12.3 (Response to Query for Labels Separate From Documents) defines descendants and ancestors by string prefix and never says whether a URL counts as its own. The prose implies not, by listing the requested URL beside its ancestors (opt=normal, opt=generic), and Appendix B's tree response follows that reading to a surprising end: it answers `not-labeled` for the RSAC service and TheProject.html, although the bureau holds RSAC's specific label for exactly that URL and returns it in the same response inside the first URL's set (and the §18.2 (Normal query) normal query returns it for this URL). A client that asks for a URL's tree gets nothing for the URL itself. Entries: R-0229, R-0231, R-0246, R-0249.

<!-- q L551 -->
> "http://www.w3.org/pub/WWW/TheProject.html"

<!-- q L710 -->
> for "http://www.w3.org/pub/WWW/TheProject.html"

<!-- q L722 -->
> error (not-labeled "http://www.w3.org/pub/WWW/TheProject.html")

### SD-20: the Appendix A timer test

§17 (Appendix A: An Algorithm for Locating a Label Bureau) sets a timer to the threshold, uses the primary alone when the timer reads less than the threshold, races both bureaus otherwise, and resets the timer to the threshold in any case. A timer started at the threshold and moving either way gives the same answer to that test on every later query, so one branch is never taken; and in any case may mean after every query or only after a race. Inferred reading: R-0346. Entries: R-0338, R-0340, R-0344.

<!-- q L524 "It also divides" .. "value." -->
> It also divides 60 minutes by the total number of address it can find for the label bureau, sets a timer to this value, and remembers this as the "threshold" value.

<!-- q L525 "If the timer" .. "is used." -->
> If the timer is below the threshold, the primary bureau address is used.

<!-- q L525 "In any case" .. "threshold value." -->
> In any case, a new secondary bureau address is chosen at random and the timer is reset to the threshold value.

### SD-21: error forms without meanings

`request-denied` (in both `service-error` and `label-error`), `service-unavailable` and `not-labeled` are never explained. §8 (Semantics of PICS Labels and Label Lists) explains the no-ratings form and label-error as a class, and §11.2 (Explanation of example) only that a labellist can carry an explanation instead of a label. What a client does with each, and what a `request-denied` label-error without its optional URL refers to, is left to the reader. Entries: R-0122, R-0123, R-0132.

<!-- q L215-216 -->
> service-error :: 'error' '(' 'request-denied' explanation* ')' | 'error' 'service-unavailable'

<!-- q L217-218 -->
> label-error :: 'error' '(' 'request-denied' [quotedURL explanation*] ')' | 'error' '(' 'not-labeled' quotedURL* ')'

### SD-22: no rule for what does not parse

The label option set is closed by the grammar, yet §13.1 (Signature Details) expects new options for new algorithms, and §5 (General Format) says what to do with an unknown extension. Nothing says what a consumer does with an unknown option name, a repeated option that may not repeat, or a labellist that does not parse. Entries: R-0089, R-0049, R-0074.

<!-- q L411 "Should this system" .. "pair of algorithms." -->
> Should this system become outdated, the PICS specification can be easily updated to add a new label option that supports a different pair of algorithms.

### SD-23: generic identified by use, or by value

§5 (General Format) identifies a generic label by the presence of the generic option, then lets the option's value decide (true). Appendix B writes the option, with false, on specific labels. Entries: R-0007, R-0032; inferred R-0033.

<!-- q L73 "A generic label (identified" .. "generic option)" -->
> A generic label (identified by the use of the generic option)

<!-- q L653 -->
> generic false

### SD-E: editorial defects, quoted where they sit (never healed)

Each is the source's own text; the entries that quote them say so in their notes.

Line 256, the walk-up example: one URL drops the s of greatdocs.

<!-- q L256 "further up the hierarchy" .. "or even at" -->
> further up the hierarchy, in "http://www.greatdoc.com/foo/" or even at

Lines 274-275, the example response in §11.1 (Example): 30 June 1995 was a Friday (computed), so the Date header's weekday is wrong; the Last-modified header beside it names 29 June 1995 a Thursday, which it was.

<!-- q L274 -->
> Date: Thu, 30 Jun 1995 17:51:47 GMT

<!-- q L275 -->
> Last-modified: Thursday, 29-Jun-95 17:51:47 GMT

Line 309: the section is cited in the singular; its heading (line 388) is plural.

<!-- q L309 "Details of signing" .. "Digital Signature." -->
> Details of signing labels are included in the section MICs and Digital Signature.

Line 383: simple-label is not a production; the grammar's is single-label.

<!-- q L383 "a set of simple-labels" .. "will be returned," -->
> a set of simple-labels will be returned,

Line 417: has for have.

<!-- q L417 -->
> After all of the options has been output, output the characters "r (".

Line 455: the glossary expands MIME one way, the reference list (line 479) another.

<!-- q L455 "Multimedia Internet" .. "Message Extension." -->
> Multimedia Internet Message Extension.

<!-- q L479 "MIME (Multipurpose" .. "Mail Extensions)" -->
> MIME (Multipurpose Internet Mail Extensions)

Line 524: address for addresses.

<!-- q L524 "the total number" .. "can find" -->
> the total number of address it can find

Line 152: the no-ratings terminal has its opening parenthesis inside the quotes, unlike the other error forms (lines 215 and 217-218); with whitespace insignificant the difference is typographic.

<!-- q L152 -->
> service-info :: 'error' '(no-ratings' explanation* ')'

Line 372: [outside this source] HTML 2.0 (RFC 1866, section 8.2.1), which the line cites, names the media type application/x-www-form-urlencoded; not checked against a cached copy here.

<!-- q L372 -->
> MIME type application/x-www-form-encoded as described in


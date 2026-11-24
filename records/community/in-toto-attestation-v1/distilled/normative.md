---
record: in-toto-attestation-v1
kind: normative
title: "in-toto-attestation-v1 — normative text"
generated_by: bin/fx1-skeleton
extracted: "2026-11-09"
reviewed_by: ""
---

# Normative text

Every normative statement of the in-toto Attestation Framework v1.2 (tag v1.2.0, commit df02077) that binds anyone, in source order, with its locator: each BCP 14 sentence the skeleton found (split into one statement per entry where it held several), the keyword-less statements pass 1 judged binding (field headings, definitions the rules rest on, scope lead-ins, the release and versioning rules, and the steps of the validation model), two scope sentences pass 2 found dropped (R-0217, R-0218, flagged hunted (pass 2)), and a pointer to each inferred entry. Explanatory prose, examples and use cases are left out, except where a defect needs them quoted.

**Markers.** Every quotation is a `<!-- q Lx-y -->` marker, anchored where it selects part of its lines, whose words `bin/check-quotes --render` wrote from `.cache/in-toto-attestation-v1.txt` (1162 lines; its sha256 is `source_digest` in requirements.yaml), the rendering `distilled/render-source.py` makes of twelve Markdown files of the source archive. A blockquote continuation keeps its `>` marker inside a quotation, as the rendering does. Nothing between the blockquote marks was typed.

**Flags.** The keyword, or keyword-less; split of R-NNNN for a statement cut from a skeleton sentence; from C-NNNN for a promoted candidate; hunted for a keyword-less statement no candidate carried; _[definition]_, _[scope]_ and _[field]_ (a field heading: type and presence) for normative text that is not itself an obligation. Ids are requirements.yaml's.

**Binding force.** §1.2 declares RFC 2119 for all documents under the specification (L63-65), without RFC 8174 (SD-11). docs/validation.md (§12) has no keyword; its steps are carried as the reference consumer procedure, and where they disagree with spec/v1, spec/v1 governs (requirements.yaml, note, VALIDATION MODEL).

**Source defects and tensions** are at the end as SD-1 onward, each with the lines it concerns quoted by marker; requirements.yaml's notes cite them.

## §1.1 Tagged Releases

**R-0124** · keyword-less · hunted
<!-- q L33-34 -->
> The latest [tagged release] version matches the [SemVer](https://semver.org) MAJOR.MINOR version of the Attestation Framework spec.

**R-0125** · keyword-less · hunted
<!-- q L36-37 -->
> Backwards-compatible semantic updates to the spec (except predicates) are indicated through new tagged MINOR version releases.

**R-0126** · keyword-less · hunted
<!-- q L38-39 -->
> We use new tagged PATCH version releases to indicate updates to predicate specifications and/or backwards-compatible changes to the language bindings.

## §1.2 Keywords

_[recital]_ · the keyword declaration; bin/bcp14-count strips its keywords
<!-- q L63-65 -->
> The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in all documents under this specification are to be interpreted as described in [RFC 2119].

## §2.2 Parsing rules

**R-0127** · keyword-less · hunted · _[scope]_
<!-- q L106-107 -->
> The following rules apply to [Statement] and any [Predicate] that opt into this model.

_Inferred, not verbatim: **R-0197** — unrecognized members; its words and grounds are in requirements.yaml._

**R-0001** · MUST
<!-- q L109-110 "- **Un" .. "." -->
> - **Unrecognized fields:** Consumers MUST ignore unrecognized fields unless otherwise noted in the predicate specification.

**R-0128** · keyword-less · from C-0020
<!-- q L114-115 "- **Ve" .. "ber." -->
> - **Versioning:** Each type has a [SemVer2](https://semver.org) version number and the [TypeURI] reflects the major version number.

**R-0129** · keyword-less · from C-0021
<!-- q L115-118 "A mess" .. "." -->
> A message is always semantically correct, but possibly incomplete, when parsed as any other version with the same major version number and thus the same [TypeURI].

**R-0130** · keyword-less · from C-0022
<!-- q L118-118 "Minor v" .. "." -->
> Minor version changes always follow the monotonic principle.

**R-0131** · keyword-less · from C-0023
<!-- q L119-119 -->
> NOTE: 0.X versions are considered major versions.

**R-0002** · MAY
<!-- q L121-122 "- **Ex" .. "." -->
> - **Extension fields:** Producers MAY add extension fields to any JSON object.

**R-0003** · SHOULD
<!-- q L122-123 "Extens" .. "." -->
> Extension fields SHOULD use names that are unlikely to collide with names used by other orgs.

**R-0004** · MAY
<!-- q L123-124 "Produc" .. "." -->
> Producers MAY file an issue/PR to document extension fields they're using.

**R-0005** · MAY
<!-- q L124-125 "Any co" .. "." -->
> Any consumer MAY parse and use these extensions if desired.

**R-0006** · SHOULD
<!-- q L127-128 -->
> Field names SHOULD avoid special characters like `.` and `$` as these can make querying these fields in some databases more difficult.

_R-0007 (L130-132, MUST NOT first) is split into R-0088, R-0089; its full text is in requirements.yaml._

**R-0088** · MUST NOT · split of R-0007
<!-- q L130-131 "The pr" .. "r field" -->
> The presence or absence of the extension field MUST NOT influence the meaning of any other field

**R-0089** · MUST · split of R-0007
<!-- q L131-132 "the fi" .. "." -->
> the field MUST follow the monotonic principle.

**R-0132** · keyword-less · from C-0024 · _[definition]_
<!-- q L134-136 "- **Mo" .. "." -->
> - **Monotonic principle:** A policy is considered monotonic if ignoring an attestation, or a field within an attestation, will never turn a DENY decision into an ALLOW.

**R-0133** · keyword-less · from C-0025 · _[definition]_
<!-- q L136-137 "A pred" .. "." -->
> A predicate or field follows the monotonic principle if the expected policy that consumes it is monotonic.

**R-0008** · SHOULD
<!-- q L138-138 "Consum" .. "." -->
> Consumers SHOULD design policies to be monotonic.

## §3.2 Fields

**R-0134** · keyword-less · from C-0027 · _[definition]_
<!-- q L180-180 -->
> The Statement is represented as a [JSON] object with the following fields.

**R-0217** · keyword-less · hunted (pass 2) · _[scope]_
<!-- q L181-181 -->
> Additional [parsing rules] apply.

_Inferred, not verbatim: **R-0198** — member names (each at most once); its words and grounds are in requirements.yaml._

**R-0135** · keyword-less · hunted · _[field]_
<!-- q L183-183 -->
> `_type` _string ([TypeURI]), required_

**R-0136** · keyword-less · from C-0028
<!-- q L185-186 "Always" .. "c." -->
> Always > `https://in-toto.io/Statement/v1` for this version of the spec.

_Inferred, not verbatim: **R-0199** — _type; its words and grounds are in requirements.yaml._

**R-0137** · keyword-less · hunted · _[field]_
<!-- q L188-188 -->
> `subject` _array of [ResourceDescriptor] objects, required_

_Inferred, not verbatim: **R-0200** — subject (element order); its words and grounds are in requirements.yaml._

_Inferred, not verbatim: **R-0201** — subject (at least one element); its words and grounds are in requirements.yaml._

**R-0138** · keyword-less · hunted
<!-- q L190-191 "Each e" .. "." -->
> Each element > represents a single software artifact.

_R-0009 (L191-197, MUST first) is split into R-0090, R-0091; its full text is in requirements.yaml._

**R-0090** · MUST · split of R-0009
<!-- q L191-191 "Each e" .. "." -->
> Each element MUST have `digest` set.

**R-0091** · SHOULD NOT · split of R-0009
<!-- q L193-194 "Subjec" .. "ge." -->
> Subjects are assumed to be _immutable_, i.e. the artifacts identified by the > subject SHOULD NOT change.

**R-0010** · MAY
<!-- q L198-199 "The se" .. "." -->
> The semantics are up to the producer > and consumer and they MAY use them when evaluating policy.

**R-0139** · keyword-less · hunted
<!-- q L199-200 "If the" .. "." -->
> If the name is not > meaningful, leave the field unset or use "\_".

_Inferred, not verbatim: **R-0202** — subject[].name (lone underscore); its words and grounds are in requirements.yaml._

_R-0011 (L200-209, SHOULD first) is split into R-0092, R-0093; its full text is in requirements.yaml._

**R-0092** · SHOULD · split of R-0011
<!-- q L206-206 "If set" .. "." -->
> If set, `name` and `uri` SHOULD be unique within subject.

**R-0093** · keyword-less · split of R-0011
<!-- q L208-209 "IMPORT" .. "." -->
> IMPORTANT: Subject artifacts are matched purely by digest, regardless of > content type.

**R-0140** · keyword-less · hunted · _[field]_
<!-- q L212-212 -->
> `predicateType` _string ([TypeURI]), required_

**R-0141** · keyword-less · hunted · _[field]_
<!-- q L216-216 -->
> `predicate` _object, optional_

**R-0142** · keyword-less · hunted
<!-- q L218-219 "Unset i" .. "." -->
> Unset is treated the same as > set-but-empty.

**R-0012** · MAY
<!-- q L219-220 "MAY be" .. "." -->
> MAY be omitted if `predicateType` fully describes the > predicate.

## §4.1 Schema

_Inferred, not verbatim: **R-0203** — content (JSON form); its words and grounds are in requirements.yaml._

## §4.2 Fields

**R-0013** · MUST
<!-- q L258-259 "Though" .. "." -->
> Though all fields are optional, a ResourceDescriptor MUST specify one of `uri`, `digest` or `content` at a minimum.

**R-0143** · keyword-less · from C-0030
<!-- q L259-260 "Furthe" .. "." -->
> Further, a context that uses the ResourceDescriptor can require one or more fields.

**R-0144** · keyword-less · from C-0032
<!-- q L261-263 "Note t" .. "." -->
> Note that those requirements cannot override the minimum requirement of one of `uri`, `digest`, or `content` specified here.

**R-0145** · keyword-less · hunted · _[field]_
<!-- q L265-265 -->
> `name` _string, optional_

**R-0014** · SHOULD
<!-- q L269-271 "The `n" .. "." -->
> The `name` SHOULD be > stable, such as a filename, to allow consumers to reliably use the `name` > as part of their policy.

**R-0146** · keyword-less · hunted · _[field]_
<!-- q L273-273 -->
> `uri` _[ResourceURI], optional_

_R-0015 (L275-276, REQUIRED first) is split into R-0094; its full text is in requirements.yaml._

**R-0094** · REQUIRED · split of R-0015
<!-- q L276-276 "This f" .. "." -->
> This field is REQUIRED unless either `digest` or `content` is set.

**R-0147** · keyword-less · hunted · _[field]_
<!-- q L278-278 -->
> `digest` _[DigestSet], optional_

_R-0016 (L280-284, REQUIRED first) is split into R-0095, R-0096; its full text is in requirements.yaml._

**R-0095** · REQUIRED · split of R-0016
<!-- q L281-281 "This f" .. "." -->
> This field is REQUIRED unless either `uri` or `content` is set.

**R-0096** · SHOULD · split of R-0016
<!-- q L283-284 "When k" .. "." -->
> When known, the producer SHOULD set this field to denote an immutable > artifact or resource.

**R-0017** · SHOULD
<!-- q L284-285 "The pr" .. "." -->
> The producer and consumer SHOULD agree on acceptable > algorithms.

**R-0148** · keyword-less · hunted · _[field]_
<!-- q L287-287 -->
> `content` _bytes, optional_

_R-0018 (L289-294, REQUIRED first) is split into R-0097, R-0098; its full text is in requirements.yaml._

**R-0097** · REQUIRED · split of R-0018
<!-- q L290-290 "This f" .. "." -->
> This field is REQUIRED unless either `uri` or `digest` is set.

**R-0098** · MAY · split of R-0018
<!-- q L292-294 "The pr" .. "." -->
> The producer MAY use this field in scenarios where including the contents > of the resource/artifact directly in the attestation is deemed more > efficient for consumers than providing a pointer to another location.

_R-0019 (L294-297, SHOULD first) is split into R-0099; its full text is in requirements.yaml._

**R-0099** · SHOULD · split of R-0019
<!-- q L294-295 "To > m" .. "." -->
> To > maintain size efficiency, the size of `content` SHOULD be less than 1KB.

**R-0020** · MAY
<!-- q L297-299 "The `u" .. "." -->
> The `uri` or > `mediaType` MAY be used by the producer as hints for how consumers should > parse `content`.

**R-0149** · keyword-less · hunted · _[field]_
<!-- q L301-301 -->
> `downloadLocation` _[ResourceURI], optional_

_R-0021 (L303-307, SHOULD first) is split into R-0100; its full text is in requirements.yaml._

**R-0100** · SHOULD · split of R-0021
<!-- q L306-307 "To ena" .. "." -->
> To enable automated downloads by consumers, the specified location SHOULD > be resolvable.

**R-0150** · keyword-less · hunted · _[field]_
<!-- q L309-309 -->
> `mediaType` _string, optional_

_R-0022 (L311-316, SHOULD first) is split into R-0101; its full text is in requirements.yaml._

**R-0101** · SHOULD · split of R-0022
<!-- q L313-316 "For re" .. "ers." -->
> For resources or artifacts that do not have a standardized MIME type, > producers SHOULD follow [RFC 6838][] (Sections 3.2-3.4) conventions of > prefixing types with `x.`, `prs.`, or `vnd.` to avoid collisions with other > producers.

**R-0151** · keyword-less · hunted · _[field]_
<!-- q L318-318 -->
> `annotations` _map <string, value>, optional_

_R-0023 (L320-328, MAY first) is split into R-0102, R-0103, R-0104; its full text is in requirements.yaml._

**R-0102** · MAY · split of R-0023
<!-- q L320-322 "This f" .. "." -->
> This field MAY be used to provide additional information or metadata about > the resource or artifact that may be useful to the consumer when evaluating > the attestation against a policy.

**R-0103** · keyword-less · split of R-0023
<!-- q L324-325 "For ma" .. "." -->
> For maximum flexibility annotations may be any mapping from a field name to > any JSON value (string, number, object, array, boolean or _null_).

**R-0104** · SHOULD · split of R-0023
<!-- q L327-328 "The pr" .. "." -->
> The producer and consumer SHOULD agree on the semantics, and acceptable > fields and values in the `annotations` map.

**R-0024** · SHOULD
<!-- q L328-329 "Produc" .. "." -->
> Producers SHOULD follow the > same naming conventions for annotation fields as for [extension fields].

## §4.3 Semantics

**R-0152** · keyword-less · hunted · _[scope]_
<!-- q L335-335 -->
> For consistency, we RECOMMEND the following:

**R-0153** · keyword-less · from C-0033
<!-- q L337-338 "- A de" .. "." -->
> - A descriptor that specifies a `digest` is assumed to refer to an immutable resource or artifact.

**R-0025** · SHOULD
<!-- q L338-340 "The `d" .. "." -->
> The `digest` SHOULD match the resource or artifact specified in one of the `name`, `uri`, `content` or `downloadLocation` fields.

**R-0026** · SHOULD
<!-- q L340-342 "The fi" .. "." -->
> The field that consumers are expected to match the `digest` against is ultimately determined by the predicate type, and SHOULD be documented by the predicate specification.

**R-0154** · keyword-less · from C-0034
<!-- q L343-344 -->
> - A descriptor without a `content` field, is assumed to serve as a pointer to the resource/artifact.

**R-0155** · keyword-less · from C-0035
<!-- q L345-346 "- When" .. "." -->
> - When `uri` and `name` are specified, the scope of `name` is assumed to be local to the attestation.

**R-0027** · SHOULD
<!-- q L346-347 "The `n" .. "." -->
> The `name` SHOULD be compared to the `uri` to match the descriptor against the resource or artifact referenced universally.

## §5 spec/v1/digest_set.md

**R-0156** · keyword-less · hunted · _[definition]_
<!-- q L415-416 -->
> Set of one or more cryptographic digests, or other immutable references, for a single software artifact or metadata object.

## §5.2 Fields

**R-0157** · keyword-less · from C-0036 · _[definition]_
<!-- q L430-431 "A Dige" .. "." -->
> A DigestSet is represented as a _JSON object_ mapping algorithm name to a string encoding of the digest using that algorithm.

**R-0158** · keyword-less · hunted · _[definition]_
<!-- q L431-432 "The na" .. "." -->
> The named standard algorithms below use lowercase hex encoding.

_Inferred, not verbatim: **R-0204** — values of the named standard algorithms (comparison); its words and grounds are in requirements.yaml._

**R-0028** · MAY
<!-- q L432-434 "Usuall" .. "." -->
> Usually there is just a single key/value pair, but multiple entries MAY be used for algorithm agility.

**R-0029** · MUST
<!-- q L436-436 "Each e" .. "." -->
> Each entry in a DigestSet MUST be an immutable reference to an artifact.

**R-0030** · RECOMMENDED
<!-- q L436-438 "It is S" .. "." -->
> It is STRONGLY RECOMMENDED to use a commonly accepted, cryptographically secure digest algorithm to achieve this immutability.

## §5.2.1.1 `sha256`, `sha224`, `sha384`, `sha512`, `sha512_224`, `sha512_256`, `sha3_224`, `sha3_256`, `sha3_384`, `sha3_512`, `shake128`, `shake256`, `blake2b`, `blake2s`, `ripemd160`, `sm3`, `gost`, `sha1`, `md5`

_Inferred, not verbatim: **R-0205** — keys of the standard algorithms; its words and grounds are in requirements.yaml._

**R-0159** · keyword-less · hunted · _[definition]_
<!-- q L446-448 -->
> Standard cryptographic hash algorithms using [the NIST names][] (converting to lowercase and replacing `-` with `_`) as keys and lowercase hex-encoded values, for cases when the method of serialization is obvious or well known.

## §5.2.1.2 `dirHash`

**R-0160** · keyword-less · hunted · _[definition]_
<!-- q L452-453 "The [d" .. "." -->
> The [directory Hash1][] function, omitting the "h1:" prefix and output in lowercase hexadecimal instead of base64.

## §5.2.1.3 `gitCommit`, `gitTree`, `gitBlob`, `gitTag`

**R-0161** · keyword-less · hunted · _[definition]_
<!-- q L517-518 "The lo" .. "." -->
> The lowercase hex SHA-1 (40 character) or SHA-256 (64 character) of a git commit, tree, blob, or tag object, respectively.

**R-0162** · keyword-less · from C-0039 to C-0048 · _[definition]_
<!-- q L521-534 -->
> This hash is computed over `<type> SP <size> NUL <content>`, where: - `<type>` is one of `commit`, `tree`, `blob`, `tag` - `SP` is the ASCII space character, 0x20 - `<size>` is the number of bytes in `<content>`, represented as a decimal ASCII number with no leading zeros - `NUL` is the ASCII NUL character, 0x00 - `<content>` is git representation of the object: - For `commit`, the raw commit object ([more info][so-commit][^git-docs]) - For `tree`, the raw tree object, which is a series of `<unix-octal-mode> <name> NUL <binary-digest>` entries, sorted by `<name>` in the C locale ([more info][so-tree][^git-docs]) - For `blob`, the raw file contents - For `tag`, the raw tag object

## §5.2.2 Guidelines

**R-0031** · RECOMMENDED
<!-- q L549-551 -->
> It is RECOMMENDED to use at least `sha256` for compatibility between producers and consumers, unless a different hash algorithm is more conventional (e.g. `gitCommit` for git).

_R-0032 (L553-554, MUST first) is split into R-0105, R-0106; its full text is in requirements.yaml._

**R-0105** · MUST · split of R-0032
<!-- q L553-553 "Consum" .. "re" -->
> Consumers MUST only accept algorithms that they consider secure

**R-0106** · MUST · split of R-0032
<!-- q L553-554 "MUST i" .. "." -->
> MUST ignore unrecognized or unaccepted algorithms.

**R-0033** · SHOULD NOT
<!-- q L554-555 "For ex" .. "." -->
> For example, most applications SHOULD NOT accept "md5" because it lacks collision resistance.

**R-0034** · SHOULD
<!-- q L557-558 -->
> Two DigestSets SHOULD be considered matching if ANY acceptable field matches.

_Inferred, not verbatim: **R-0206** — (entries under a shared algorithm name); its words and grounds are in requirements.yaml._

**R-0035** · MUST
<!-- q L560-561 -->
> **New algorithms MUST document how the value is encoded, e.g. URL-safe base64, lowercase hex, etc.**

_Inferred, not verbatim: **R-0207** — keys (open set); its words and grounds are in requirements.yaml._

## §5.2.3 Use cases for non-cryptographic, immutable, digests

**R-0036** · MAY
<!-- q L571-573 -->
> In these situations, users MAY use a non-cryptographic identifier in a DigestSet so long as the risk of the object being mutated is acceptable for the application.

**R-0163** · keyword-less · hunted
<!-- q L595-596 "Per th" .. "." -->
> Per the specification [guidelines](#guidelines), the value encoding for non-cryptographic digests is identifier-specific.

## §6.1 ResourceURI

**R-0164** · keyword-less · hunted · _[definition]_
<!-- q L640-641 -->
> Uniform Resource Identifier as specified in [RFC 3986][], used to identify and locate any resource, service, or software artifact.

_R-0037 (L645-647, MUST first) is split into R-0107, R-0108; its full text is in requirements.yaml._

**R-0107** · MUST · split of R-0037
<!-- q L645-646 "A Reso" .. "86" -->
> A ResourceURI is represented as a case sensitive _string_ and MUST be case normalized as per section 6.2.2.1 of RFC 3986

**R-0108** · MUST · split of R-0037
<!-- q L646-647 "meanin" .. "." -->
> meaning that the scheme and authority MUST be in lowercase.

_R-0038 (L649-649, SHOULD first) is split into R-0109, R-0110; its full text is in requirements.yaml._

**R-0109** · SHOULD · split of R-0038
<!-- q L649-649 "SHOULD" .. "ct" -->
> SHOULD resolve to the artifact

**R-0110** · MAY · split of R-0038
<!-- q L649-649 "MAY be" .. "." -->
> MAY be unresolvable.

**R-0039** · RECOMMENDED
<!-- q L649-651 "It is R" .. ")." -->
> It is RECOMMENDED > to use [Package URL][] (`pkg:`) or [SPDX Download Location][] (e.g. > `git+https:`).

## §6.2 TypeURI

**R-0165** · keyword-less · hunted · _[definition]_
<!-- q L659-660 -->
> Uniform Resource Identifier as specified in [RFC 3986][], used as a collision-resistant type identifier.

_R-0040 (L664-666, MUST first) is split into R-0111, R-0112; its full text is in requirements.yaml._

**R-0111** · MUST · split of R-0040
<!-- q L664-665 "A Type" .. "86" -->
> A TypeURI is represented as a case sensitive _string_ and MUST be case normalized as per section 6.2.2.1 of RFC 3986

**R-0112** · MUST · split of R-0040
<!-- q L665-666 "meanin" .. "." -->
> meaning that the scheme and authority MUST be in lowercase.

_R-0041 (L668-671, SHOULD first) is split into R-0113, R-0114, R-0115, R-0116; its full text is in requirements.yaml._

**R-0113** · SHOULD · split of R-0041
<!-- q L668-668 "SHOULD" .. "on" -->
> SHOULD resolve to a human-readable description

**R-0114** · MAY · split of R-0041
<!-- q L668-668 "MAY be" .. "." -->
> MAY be unresolvable.

**R-0115** · SHOULD · split of R-0041
<!-- q L669-669 "SHOULD" .. "." -->
> SHOULD include a version number to allow for revisions.

**R-0116** · keyword-less · split of R-0041
<!-- q L671-671 "TypeUR" .. "." -->
> TypeURIs are not registered.

## §6.3 Timestamp

**R-0042** · MUST
<!-- q L684-685 -->
> A timestamp is represented as a _string_ and MUST be in [RFC 3339][] format in the UTC timezone ("Z").

_Inferred, not verbatim: **R-0208** — (UTC designator); its words and grounds are in requirements.yaml._

## §7.2 Fields

**R-0166** · keyword-less · from C-0067
<!-- q L721-723 -->
> A predicate has a required `predicateType` ([TypeURI]) identifying what the predicate means, plus an optional `predicate` [JSON] object containing additional, type-dependent parameters.

**R-0043** · MAY
<!-- q L727-727 -->
> New predicate types MAY be vetted by the in-toto attestation maintainers.

**R-0218** · keyword-less · hunted (pass 2) · _[scope]_
<!-- q L729-729 -->
> Additional [parsing rules] apply.

## §8.1 Schema

**R-0044** · RECOMMENDED
<!-- q L748-748 -->
> The RECOMMENDED format and protocol for Envelopes are defined per [DSSE v1.0].

**R-0045** · MAY
<!-- q L749-750 -->
> Producers MAY use other signature methods and formats that meet the [ITE-5] specification:

**R-0046** · MUST
<!-- q L752-752 -->
> - MUST support the inclusion of multiple signatures in a single envelope

**R-0047** · SHOULD
<!-- q L753-753 -->
> - SHOULD include an authenticated payload type

**R-0048** · SHOULD
<!-- q L754-754 -->
> - SHOULD avoid depending on canonicalization for security

_Inferred, not verbatim: **R-0209** — payload (signed bytes); its words and grounds are in requirements.yaml._

**R-0049** · SHOULD
<!-- q L755-755 -->
> - SHOULD support a hint indicating what signing key was used, i.e., a KEYID

_Inferred, not verbatim: **R-0210** — keyid; its words and grounds are in requirements.yaml._

**R-0050** · SHOULD NOT
<!-- q L756-756 -->
> - SHOULD NOT require the verifier to parse the payload before verifying

**R-0051** · SHOULD NOT
<!-- q L757-757 -->
> - SHOULD NOT require the inclusion of signing key algorithms in the signature

## §8.1.1 Alternative Envelope schemas

**R-0167** · keyword-less · from C-0068
<!-- q L761-762 -->
> - The [Sigstore Bundle], while [supporting DSSE], is not currently [ITE-5] compliant because it requires a _single signature_ in the envelope.[^1]

**R-0168** · keyword-less · from C-0069
<!-- q L763-764 -->
> - The [COSE_Sign] structure is [ITE-5] compliant, whereas the `COSE_Sign1` format that supports only one signer is NOT compliant.

## §8.2 Fields

**R-0169** · keyword-less · hunted · _[scope]_
<!-- q L768-769 -->
> The in-toto Attestation Framework has the following general field requirements for an Envelope:

_R-0052 (L771-772, REQUIRED first) is split into R-0117, R-0118; its full text is in requirements.yaml._

**R-0117** · REQUIRED · split of R-0052
<!-- q L771-771 "`signa" .. "D" -->
> `signatures` (or equivalent) is REQUIRED

**R-0118** · MUST · split of R-0052
<!-- q L771-772 "MUST b" .. "." -->
> MUST be defined as an array of digital signatures.

**R-0170** · keyword-less · from C-0070
<!-- q L772-773 "The en" .. "." -->
> The encoding of the signature bytes is determined by the envelope schema.

**R-0053** · SHOULD
<!-- q L774-774 "- A `k" .. "." -->
> - A `keyid` (or equivalent) SHOULD be included for each signing key used.

**R-0054** · MAY
<!-- q L774-775 "The en" .. "." -->
> The envelope schema MAY nest this field within the signature array.

**R-0055** · SHOULD
<!-- q L776-777 -->
> - `payload` (or equivalent) SHOULD be included and contain the in-toto [Statement] that was signed.

**R-0056** · MUST
<!-- q L778-778 -->
> - `payloadType` (or equivalent) MUST be signed along with the `payload`.

_Inferred, not verbatim: **R-0211** — payloadType, payload (signature input); its words and grounds are in requirements.yaml._

**R-0057** · MUST
<!-- q L779-780 -->
> It MUST take the form `application/vnd.in-toto+<encoding>` to indicate an in-toto [Statement] payload and its serialized `<encoding>` format.

**R-0171** · keyword-less · hunted · _[scope]_
<!-- q L782-783 -->
> In addition, the Envelope spec has the following specific requirements for the standard [DSSE][DSSE v1.0] fields.

**R-0058** · MUST
<!-- q L785-786 "- `pay" .. "`." -->
> - `payloadType` MUST be set to `application/vnd.in-toto.<predicate>+json` or to `application/vnd.in-toto+json`.

_Inferred, not verbatim: **R-0212** — payloadType (acceptance); its words and grounds are in requirements.yaml._

**R-0172** · keyword-less · from C-0071
<!-- q L786-787 "This i" .. "." -->
> This indicates that the Envelope contains a JSON object with a `_type` field specifying its schema.

**R-0173** · keyword-less · from C-0072 · _[scope]_
<!-- q L787-788 "If the" .. ":" -->
> If the predicate-specific media type is used, the following requirements apply:

**R-0059** · MUST
<!-- q L789-790 -->
> - `<predicate>` MUST match the [predicate specification filename] without the file extension.

_Inferred, not verbatim: **R-0213** — payloadType (<predicate> part); its words and grounds are in requirements.yaml._

**R-0060** · SHOULD NOT
<!-- q L791-792 "- Cons" .. "." -->
> - Consumers SHOULD NOT rely upon the media type for individual attestations as faithful indicators of predicate type.

**R-0061** · SHOULD
<!-- q L792-793 "Consum" .. "." -->
> Consumer SHOULD only rely on the `predicateType` field in the [Statement] layer.

**R-0062** · MUST
<!-- q L794-795 -->
> - To obtain predicate information that is authenticated, consumers MUST parse the Envelope's `payload`, and verify it against its `signatures`.

_Inferred, not verbatim: **R-0214** — (verification before parsing and use); its words and grounds are in requirements.yaml._

**R-0174** · keyword-less · from C-0073
<!-- q L796-797 -->
> - The predicate version is not specified in the media type; it is handled in the [Statement] layer.

**R-0063** · MUST
<!-- q L798-798 -->
> - `payload` MUST be a base64-encoded JSON [Statement].

## §8.3 File naming convention

**R-0064** · SHOULD
<!-- q L802-803 -->
> If stored in a dedicated file by itself, and not as part of a [Bundle], an Envelope SHOULD use the suffix `.json`.

**R-0065** · SHOULD
<!-- q L805-807 -->
> - For attestations intended for consumption by [in-toto-verify], an Envelope containing an attestation about a particular software supply chain step `<step-name>` SHOULD be named `<step-name>.json`.

**R-0066** · MAY
<!-- q L808-810 -->
> - For other verifiers, or cases in which a step name cannot be easily determined, the attestation producer and consumer MAY agree on an arbitrary filename: `<env-name>.json`.

**R-0067** · SHOULD
<!-- q L811-814 -->
> - If multiple Envelopes are produced for the same step by different [functionaries] uniquely identified by a public key, an Envelope name SHOULD include the truncated [KEYID] of the public key `<keyid[0:8]>` of the signing functionary: `<step/env-name>.<keyid[0:8]>.json`.

## §8.4 Storage convention

**R-0068** · SHOULD
<!-- q L818-819 -->
> The media type `application/vnd.in-toto.<predicate>+dsse` SHOULD be used to denote an individual attestation in arbitrary storage systems.

**R-0069** · MUST
<!-- q L821-822 "- The `" .. "." -->
> - The `<predicate>` MUST match the [predicate specification filename] without the file extension.

**R-0175** · keyword-less · from C-0074
<!-- q L822-823 "Predic" .. "." -->
> Predicate versioning is handled in the [Statement] layer.

**R-0070** · SHOULD NOT
<!-- q L824-825 "- Cons" .. "." -->
> - Consumers SHOULD NOT rely upon the media type for individual attestations as faithful indicators of predicate type.

**R-0071** · SHOULD
<!-- q L825-826 "Consum" .. "." -->
> Consumer SHOULD only rely on the `predicateType` field in the [Statement] layer.

**R-0072** · MUST
<!-- q L827-828 -->
> - To obtain predicate information that is authenticated, consumers MUST parse the Envelope's `payload`, and verify it against its `signatures`.

## §9 spec/v1/bundle.md

**R-0176** · keyword-less · hunted
<!-- q L864-865 "**NOTE" .. "]." -->
> **NOTE**: The Bundle is not authenticated as a whole. Instead each individual attestation is authenticated using signature formats like [DSSE].

_[note, not a requirement]_ · the rest of the §9 NOTE, after R-0176
<!-- q L865-868 "As suc" .. "." -->
> As such, an attacker might be able to delete valid attestations, replay obsolete attestations, and/or inject invalid or irrelevant attestations in a Bundle without being detected.

## §9.1 Data structure

**R-0177** · keyword-less · hunted
<!-- q L876-876 -->
> Attestation Bundles use [JSON Lines] to store multiple attestations.

_Inferred, not verbatim: **R-0215** — (one envelope per line); its words and grounds are in requirements.yaml._

**R-0073** · MAY
<!-- q L878-879 -->
> - Each attestation within a Bundle MAY have different signing keys, `_type`, `subject`, and/or `predicateType`.

**R-0074** · SHOULD
<!-- q L880-880 "- Each" .. "." -->
> - Each line within a Bundle SHOULD be an [Envelope].

**R-0075** · MUST
<!-- q L880-881 "Consum" .. "." -->
> Consumers MUST ignore unrecognized lines.

**R-0076** · MUST
<!-- q L882-883 -->
> - Consumers MUST ignore attestations with unrecognized keys, types, subjects, or predicates.

_Inferred, not verbatim: **R-0216** — predicateType (unrecognized); its words and grounds are in requirements.yaml._

**R-0077** · MUST NOT
<!-- q L884-884 -->
> - Processing of a Bundle MUST NOT depend on the order of the attestations.

## §9.2 File naming convention

**R-0078** · SHOULD
<!-- q L888-888 -->
> Bundles SHOULD use the suffix `.intoto.jsonl`.

**R-0079** · SHOULD
<!-- q L890-891 -->
> - A Bundle of attestations relevant for `<filename>` SHOULD be named `<filename>.intoto.jsonl`.

_R-0080 (L892-893, MAY first) is split into R-0119, R-0120; its full text is in requirements.yaml._

**R-0119** · MAY · split of R-0080
<!-- q L892-892 "Attest" .. "ts" -->
> Attestations in the Bundle MAY have different subjects

**R-0120** · SHOULD · split of R-0080
<!-- q L892-893 "they S" .. "." -->
> they SHOULD all be relevant to that file or its dependencies.

## §9.3 Storage convention

**R-0081** · SHOULD
<!-- q L903-904 -->
> The media type `application/vnd.in-toto.bundle` SHOULD be used to denote a Bundle in arbitrary storage systems.

_R-0082 (L906-908, MUST first) is split into R-0121, R-0122, R-0123; its full text is in requirements.yaml._

**R-0121** · keyword-less · split of R-0082
<!-- q L906-906 "The me" .. "g" -->
> The media type for a Bundle does not indicate an encoding

**R-0122** · MUST · split of R-0082
<!-- q L906-907 "Bundles" .. "nes" -->
> Bundles MUST be encoded as JSON lines

**R-0123** · SHOULD · split of R-0082
<!-- q L907-908 "the en" .. "." -->
> the encoding of each attestation within the Bundle SHOULD be indicated at the [Envelope] layer.

**R-0083** · SHOULD NOT
<!-- q L909-911 -->
> - The predicate type of individual attestations within the stored Bundle SHOULD NOT be indicated in the media type for the Bundle, as a bundle may contain attestations with different predicate types.

**R-0084** · MUST
<!-- q L912-913 -->
> - To obtain predicate information that is authenticated, consumers MUST download and parse each line in a Bundle separately.

## §11 spec/versioning.md

**R-0178** · keyword-less · from C-0082
<!-- q L1056-1058 -->
> Predicate specifications are versioned independently from the Attestation Framework specification in order to allow for predicates to evolve as needed without depending on the evolution of the Statement layer, for example.

**R-0179** · keyword-less · hunted · _[scope]_
<!-- q L1060-1061 -->
> The following rules apply to both Statement and predicate specification versioning.

## §11.2 Versioning rules

**R-0180** · keyword-less · hunted
<!-- q L1070-1071 "We adh" .. "H." -->
> We adhere to [Semantic Versioning 2.0.0](https://semver.org), i.e. MAJOR.MINOR.PATCH.

**R-0181** · keyword-less · hunted
<!-- q L1073-1074 "NOTE: 0" .. "g." -->
> NOTE: 0.X.Y versions are considered major versions for the purposes of this doc, consistent with semantic versioning.

**R-0085** · MUST
<!-- q L1076-1077 "Any me" .. "." -->
> Any message MUST be semantically correct when parsed as any other version with the same major number.

**R-0086** · MUST
<!-- q L1079-1080 "- Pars" .. "." -->
> - Parsing an older message as a newer minor/patch version MUST be semantically equivalent to parsing it as the original version.

**R-0182** · keyword-less · from C-0083
<!-- q L1080-1082 "(All f" .. ")" -->
> (All fields present in both versions have the same meaning, and the absence of any new fields has no semantic meaning.)

**R-0087** · MUST
<!-- q L1083-1084 -->
> - Parsing a newer message as an older minor/patch version MUST be semantically equivalent to parsing it as the newer version with all new fields removed.

**R-0183** · keyword-less · from C-0084
<!-- q L1085-1086 -->
> (All fields present in both version have the same meaning, regardless of the presence or absence of the new fields.)

**R-0184** · keyword-less · from C-0085
<!-- q L1088-1088 "The ty" .. "." -->
> The type ID only includes the major version.

**R-0185** · keyword-less · hunted
<!-- q L1091-1091 -->
> Implementations just use the URI as an opaque string.

## §12 docs/validation.md

**R-0186** · keyword-less · hunted · _[scope]_
<!-- q L1116-1118 -->
> The following pseudocode shows how to verify and extract metadata about a single artifact from a single attestation. The expectation is that consumers will feed the resulting metadata into a policy engine.

**R-0187** · keyword-less · from C-0094 to C-0097
<!-- q L1122-1128 -->
> Inputs: - `artifactToVerify`: blob of data - `attestation`: JSON-encoded [Envelope] - `recognizedAttesters`: collection of (`name`, `publicKey`) pairs - `acceptableDigestAlgorithms`: collection of acceptable cryptographic hash algorithms (usually just `sha256`)

**R-0188** · keyword-less · from C-0099
<!-- q L1133-1134 -->
> - `envelope` := decode `attestation` as a JSON-encoded [Envelope]; reject if decoding fails

**R-0189** · keyword-less · from C-0100 to C-0105
<!-- q L1135-1141 -->
> - `attesterNames` := empty set of names - For each `signature` in `envelope.signatures`: - For each (`name`, `publicKey`) in `recognizedAttesters`: - Optional: skip if `signature.keyid` does not match `publicKey` - If `signature.sig` matches `publicKey`: - Add `name` to `attesterNames`

**R-0190** · keyword-less · from C-0106
<!-- q L1142-1142 -->
> - Reject if `attesterNames` is empty

**R-0191** · keyword-less · from C-0109
<!-- q L1146-1146 -->
> - Reject if (`envelope.payloadType` != `application/vnd.in-toto+json` OR `envelope.payloadType` does not match `application/vnd.in-toto.<predicate>+json`)

**R-0192** · keyword-less · from C-0110
<!-- q L1147-1148 -->
> - `statement` := decode `envelope.payload` as a JSON-encoded [Statement]; reject if decoding fails

**R-0193** · keyword-less · from C-0111
<!-- q L1149-1149 -->
> - Reject if `statement.type` != `https://in-toto.io/Statement/v1`

**R-0194** · keyword-less · from C-0112 to C-0115
<!-- q L1150-1154 -->
> - `matchedSubjects` := the subset of entries `s` in `statement.subject` where: - there exists at least one `(alg, value)` in `s.digest` where: - `alg` is in `acceptableDigestAlgorithms` AND - `hash(alg, artifactToVerify)` == `hexDecode(value)`

**R-0195** · keyword-less · from C-0116
<!-- q L1155-1155 -->
> - Reject if `matchedSubjects` is empty

**R-0196** · keyword-less · from C-0117 to C-0120
<!-- q L1157-1162 -->
> Output (to be fed into policy engine): - `statement.predicateType` - `statement.predicate` - `matchedSubjects` - `attesterNames`

## Source defects and tensions

Found by pass 1 (requirements). Each is a defect (the text is wrong), a tension (two texts pull apart), a gap (the text is silent where an implementer must decide), unclear, form or editorial. The words around each marker are this extraction's.

### SD-1 (defect) — The general payloadType form excludes the v1.2 predicate-specific value

§8.2's general requirements cover every envelope, DSSE included (R-0169), and give payloadType the form `application/vnd.in-toto+<encoding>` (R-0057). The DSSE-specific list, expanded in v1.2, also allows `application/vnd.in-toto.<predicate>+json` (R-0058), which does not have that form; the general rule was not updated with it. A DSSE envelope with a predicate-specific payloadType meets R-0058 and fails R-0057. This extraction reads R-0058, the later and more specific text, as governing DSSE envelopes.

<!-- q L768-769 -->
> The in-toto Attestation Framework has the following general field requirements for an Envelope:

<!-- q L779-780 -->
> It MUST take the form `application/vnd.in-toto+<encoding>` to indicate an in-toto [Statement] payload and its serialized `<encoding>` format.

<!-- q L785-786 "`paylo" .. "`." -->
> `payloadType` MUST be set to `application/vnd.in-toto.<predicate>+json` or to `application/vnd.in-toto+json`.

<!-- q L1035-1036 -->
> - Expanded the allowed values for the envelope's `payloadType` field to `application/vnd.in-toto.<predicate>+json`. See [Envelope Fields].

### SD-2 (defect) — The validation model's payloadType step rejects every envelope

As printed, the step rejects when payloadType differs from the generic value OR does not match the predicate-specific form. No value both equals the first and matches the second, so every envelope fails it. The intended test rejects a value that is neither (R-0212).

<!-- q L1146-1146 -->
> - Reject if (`envelope.payloadType` != `application/vnd.in-toto+json` OR `envelope.payloadType` does not match `application/vnd.in-toto.<predicate>+json`)

### SD-3 (defect) — The validation model reads statement.type; the field is _type

The Statement has no field named type; its schema identifier is `_type` (R-0135). R-0193 is read as a test of `_type` (R-0199).

<!-- q L1149-1149 -->
> - Reject if `statement.type` != `https://in-toto.io/Statement/v1`

<!-- q L183-183 -->
> `_type` _string ([TypeURI]), required_

### SD-4 (defect) — The dirHash example encodes its value under dirHash1

The algorithm is named `dirHash` by its heading, but the example puts the value under `dirHash1`. A producer copying the example emits a key that a consumer recognizing `dirHash` ignores. This extraction takes the heading's name as the key. The value itself checks: the example's base64 dirhash decodes to the hex it gives (Python, this pass).

<!-- q L450-450 -->
> 5.2.1.2. `dirHash`

<!-- q L462-464 -->
> For example, the module dirhash `h1:Khu2En+0gcYPZ2kuIihfswbzxv/mIHXgzPZ018Oty48=` would be encoded as `{"dirHash1": "2a1bb6127fb481c60f67692e22285fb306f3c6ffe62075e0ccf674d7c3adcb8f"}`.

### SD-5 (defect) — The publishing example changes payloadType under unchanged signatures

Between §9.4.3 and §9.4.5 the envelopes whose payloads are a and d change payloadType from the predicate-specific forms to `application/vnd.in-toto+json`, while payload and signatures stay as they were. payloadType is signed with the payload (R-0056), so the published envelopes verify only if they were re-signed (R-0211), and the text never says they were: the signature placeholders are unchanged. Which happened (re-signing, or an example written before v1.2 and half updated) the source does not say.

<!-- q L931-931 -->
> { "payloadType": "application/vnd.in-toto.provenance+json", "payload": "a...", "signatures": [w...] }

<!-- q L963-963 -->
> { "payloadType": "application/vnd.in-toto.spdx+json", "payload": "d...", "signatures": [y...] }

<!-- q L984-984 -->
> { "payloadType": "application/vnd.in-toto+json", "payload": "a...", "signatures": [w...] }

<!-- q L986-986 -->
> { "payloadType": "application/vnd.in-toto+json", "payload": "d...", "signatures": [y...] }

### SD-6 (defect) — The case-normalization gloss misstates the RFC 3986 section it cites

Both definitions require case normalization per RFC 3986 §6.2.2.1 and gloss it as scheme and authority in lowercase. §6.2.2.1 (RFC 3986 is not cached in this library; paraphrased here, verify against the RFC) lowercases the scheme and the host and uppercases the hexadecimal digits of percent-encodings; the userinfo part of the authority stays case-sensitive. The gloss asks for more (lowercasing userinfo changes the URI) and for less (nothing on percent-encodings) than the rule it explains. R-0107 and R-0108, R-0111 and R-0112 carry the two parts separately so a test can say which it checks.

<!-- q L645-647 -->
> A ResourceURI is represented as a case sensitive _string_ and MUST be case normalized as per section 6.2.2.1 of RFC 3986, meaning that the scheme and authority MUST be in lowercase.

<!-- q L664-666 -->
> A TypeURI is represented as a case sensitive _string_ and MUST be case normalized as per section 6.2.2.1 of RFC 3986, meaning that the scheme and authority MUST be in lowercase.

### SD-7 (tension) — Consumer rules sit under a condition in §8.2 and stand without one in §8.4

In §8.2, R-0060 to R-0062 are items under the predicate-specific lead-in (R-0173), so read literally they bind no consumer of an envelope whose payloadType is the generic `application/vnd.in-toto+json`. §8.4 states the same three with no condition (R-0070 to R-0072). Authenticating before use cannot depend on the media type; R-0214 holds it for every envelope.

<!-- q L787-788 "If the" .. ":" -->
> If the predicate-specific media type is used, the following requirements apply:

<!-- q L794-795 -->
> - To obtain predicate information that is authenticated, consumers MUST parse the Envelope's `payload`, and verify it against its `signatures`.

<!-- q L827-828 -->
> - To obtain predicate information that is authenticated, consumers MUST parse the Envelope's `payload`, and verify it against its `signatures`.

### SD-8 (gap) — The validation model covers less than the specification

It handles one artifact and one attestation, and L1120 says that processing several is still to be explained; that line is not quoted here, because its marker word would trip bin/validate's scan for unfinished work. It takes only a JSON-encoded envelope, so a COSE_Sign envelope (R-0168) has no procedure. It hashes a blob of data, which fits the NIST-named algorithms but not dirHash (a file tree) or the git algorithms (a git object built from a header and content). It hex-decodes every value, which fails for non-cryptographic identifiers, whose encoding is identifier-specific (R-0163), and for a new algorithm encoded otherwise (R-0035); and its acceptable algorithms are cryptographic only (SD-12). It never checks that predicateType is present, so its output can carry an absent one (protocol.yaml SD-11).

<!-- q L1116-1117 "The fo" .. "." -->
> The following pseudocode shows how to verify and extract metadata about a single artifact from a single attestation.

<!-- q L1125-1125 -->
> - `attestation`: JSON-encoded [Envelope]

<!-- q L1127-1128 -->
> - `acceptableDigestAlgorithms`: collection of acceptable cryptographic hash algorithms (usually just `sha256`)

<!-- q L1154-1154 -->
> - `hash(alg, artifactToVerify)` == `hexDecode(value)`

<!-- q L595-596 "Per th" .. "." -->
> Per the specification [guidelines](#guidelines), the value encoding for non-cryptographic digests is identifier-specific.

### SD-9 (unclear) — Comparing a local name with a global URI

§4.3 makes name local to the attestation when uri is also set (R-0155), then asks for name to be compared with uri to match the descriptor universally (R-0027). A local name and a global URI are different kinds of identifier, and what comparing them means is not said. The likelier intent is that uri, not name, matches a descriptor universally; the text does not say so, and R-0027 is testable: no.

<!-- q L345-347 -->
> - When `uri` and `name` are specified, the scope of `name` is assumed to be local to the attestation. The `name` SHOULD be compared to the `uri` to match the descriptor against the resource or artifact referenced universally.

### SD-10 (form) — RECOMMEND and STRONGLY RECOMMENDED

RECOMMEND is not one of RFC 2119's words (RECOMMENDED is), so a keyword counter misses it; it gives the keyword-less §4.3 bullets the strength of a recommendation (R-0152). RFC 2119 has no intensified form; STRONGLY RECOMMENDED is read as RECOMMENDED and counted once (R-0030).

<!-- q L335-335 -->
> For consistency, we RECOMMEND the following:

<!-- q L436-438 "It is S" .. "." -->
> It is STRONGLY RECOMMENDED to use a commonly accepted, cryptographically secure digest algorithm to achieve this immutability.

### SD-11 (tension) — The keyword declaration invokes RFC 2119 without RFC 8174

RFC 8174 is what makes only capitalized words keywords. Without it, the lowercase required and optional of the eleven field headings, the may of L196, L198, L260 and L324, and the should of L298 and L871 are not excluded by the declaration. This extraction reads capitals only, as bin/bcp14-count does, and judged each lowercase use as a sentence (requirements.yaml, reconciliation).

<!-- q L63-65 -->
> The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in all documents under this specification are to be interpreted as described in [RFC 2119].

### SD-12 (tension) — Cryptographic in some places, any immutable identifier in others

Since v1.1 a DigestSet holds cryptographic digests or other immutable references, and a non-cryptographic identifier is allowed (R-0036). ResourceDescriptor's digest definition still calls the digests cryptographic, and the validation model's acceptable algorithms are cryptographic hash algorithms. A subject identified by an ARN (§5.3) meets §5 and has no path through the validation model.

<!-- q L280-280 -->
> > A set of cryptographic digests of the contents of the resource or artifact.

<!-- q L415-416 -->
> Set of one or more cryptographic digests, or other immutable references, for a single software artifact or metadata object.

<!-- q L1040-1042 -->
> - Clarified that subjects are assumed to be immutable and that it is acceptable to use a non-cryptographic digest (though cryptographic digests are still strongly recommended).

<!-- q L1127-1128 -->
> - `acceptableDigestAlgorithms`: collection of acceptable cryptographic hash algorithms (usually just `sha256`)

### SD-13 (gap) — A match on ANY acceptable entry ignores a disagreeing one

R-0034 matches two DigestSets if any acceptable entry agrees. When they share two acceptable algorithms and agree on one but not the other, the literal rule says match; nothing says a disagreeing acceptable digest defeats the match or signals an error. With a non-cryptographic identifier accepted beside a hash, the weaker identifier alone decides.

<!-- q L557-558 -->
> Two DigestSets SHOULD be considered matching if ANY acceptable field matches.

### SD-14 (gap) — JSON is given by a link only

The Statement is a JSON object (R-0134) and JSON is a link to json.org. Nothing addresses duplicate member names (R-0198 covers the producer only), the range or precision of numbers (annotation values and predicates may hold any JSON number, R-0103), whether a null value for an optional field counts as unset, or the character encoding of the payload. Because signatures cover the payload bytes (R-0209), two consumers whose JSON parsers settle these differently can read one signed Statement differently.

<!-- q L180-180 -->
> The Statement is represented as a [JSON] object with the following fields.

<!-- q L223-223 -->
> [JSON]: https://www.json.org/json-en.html

### SD-15 (gap) — Which spellings of UTC a Timestamp may use

R-0042 names the Z designator. RFC 3339 (not cached in this library) also writes a UTC instant with a numeric offset of +00:00 and allows a lowercase z; whether those meet R-0042 is not said. R-0208 has producers write Z; a consumer's handling of the other spellings is open.

<!-- q L684-685 -->
> A timestamp is represented as a _string_ and MUST be in [RFC 3339][] format in the UTC timezone ("Z").

### SD-16 (tension) — Do the parsing rules bind every predicate?

§2.2 applies its rules to the Statement and to predicates that opt in (R-0127); §7.2 says the parsing rules apply to predicates with no opt-in (R-0218). Whether R-0001 binds the contents of a predicate whose specification says nothing is unclear; R-0001's own exception for what a predicate specification notes leans to the rules applying by default.

<!-- q L106-107 -->
> The following rules apply to [Statement] and any [Predicate] that opt into this model.

<!-- q L729-729 -->
> Additional [parsing rules] apply.

### SD-17 (gap) — content has a type the field types do not define

content is typed bytes, which is not among §6's field types; its JSON form appears only in a comment of the schema, as base64, with no alphabet or padding rule (R-0203). The 1KB bound (R-0099) does not say 1000 or 1024 bytes, nor whether it counts the bytes or their base64 text.

<!-- q L245-245 -->
> "content": "<BASE64 VALUE>", // converted from bytes for JSON

<!-- q L287-287 -->
> `content` _bytes, optional_

<!-- q L629-636 -->
> The in-toto Attestation Framework defines several field types that may be of common interest: - [DigestSet] - [ResourceURI] - [TypeURI] - [Timestamp] - [ResourceDescriptor]

### SD-18 (defect) — The dirHash shell pipeline is not equivalent for every file name

§5.2.1.2 calls the pipeline equivalent to Hash1. xargs splits its input at blanks, so a file name containing a space breaks it: run this pass on a directory holding a file named a, space, b and a file named c, sha256sum reported a and b as missing and xargs exited 1, but the pipeline's status is its last command's, 0 unless pipefail is set, and it printed a digest of the listing without that file: a wrong dirHash, flagged only on stderr; Hash1 over the same two files gives another value. (Pass 2 re-ran it in bash; pass 1 had written that the pipeline exited 1.) Hash1 takes its file list as a list and does not split names. The definition by reference to Hash1 (R-0160) governs; the pipeline illustrates it for ordinary names.

<!-- q L455-456 "Equiva" .. ":" -->
> Equivalent to extracting the archive to an empty directory and running the following command in that directory:

<!-- q L459-459 -->
> find . -type f | cut -c3- | LC_ALL=C sort | xargs -r sha256sum | sha256sum | cut -f1 -d' '

### SD-19 (defect) — The SPDX media types of the examples match no predicate specification file

<predicate> must match a predicate specification filename without its extension (R-0059, R-0069). At df02077 the predicates directory holds spdx2.md and spdx3.md and no spdx.md (a listing of the source archive, this pass; the files were not read), so the SPDX storage media type of §8.4.1 and the SPDX payloadType of §9.4.3, whose predicateType links to spdx3.md, break the rule they illustrate. provenance and vsa match files.

<!-- q L835-835 -->
> - SPDX: `application/vnd.in-toto.spdx+dsse`

<!-- q L956-956 -->
> [`predicateType=https://spdx.dev/Document`](https://github.com/in-toto/attestation/blob/main/spec/predicates/spdx3.md)

<!-- q L963-963 -->
> { "payloadType": "application/vnd.in-toto.spdx+json", "payload": "d...", "signatures": [y...] }

### SD-20 (gap) — A storage media type exists only in the predicate-specific form

§8.4 defines `application/vnd.in-toto.<predicate>+dsse` only. A Statement whose predicateType has no specification file (R-0213: the Fooly builder's type) has no storage media type, and there is none for an envelope other than DSSE.

<!-- q L818-819 -->
> The media type `application/vnd.in-toto.<predicate>+dsse` SHOULD be used to denote an individual attestation in arbitrary storage systems.

### SD-21 (form) — The validation model's list nesting is broken

The decode step (L1133) is indented as a sibling of the Envelope layer heading rather than its first child, and the optional keyid skip (L1138) as a sibling of the inner loop rather than inside it, so the rendered list nests differently from what the steps mean. R-0189 reads them by meaning.

<!-- q L1132-1134 -->
> - Envelope layer: - `envelope` := decode `attestation` as a JSON-encoded [Envelope]; reject if decoding fails

<!-- q L1137-1140 -->
> - For each (`name`, `publicKey`) in `recognizedAttesters`: - Optional: skip if `signature.keyid` does not match `publicKey` - If `signature.sig` matches `publicKey`:

### SD-22 (tension) — A payload that should be included but must be parsed

The general rule lets an envelope omit its payload (R-0055, SHOULD); consumers must parse the payload to authenticate (R-0062), and a DSSE payload must be base64-encoded JSON (R-0063). How a consumer obtains a detached payload is not said.

<!-- q L776-777 -->
> - `payload` (or equivalent) SHOULD be included and contain the in-toto [Statement] that was signed.

<!-- q L798-798 -->
> - `payload` MUST be a base64-encoded JSON [Statement].

### SD-23 (gap) — The general payloadType form admits encodings no rule defines

The general form names a serialized <encoding>, so serializations other than JSON are contemplated (R-0057); the Statement is defined only as a JSON object (R-0134), and no other encoding of it is specified.

<!-- q L779-780 -->
> It MUST take the form `application/vnd.in-toto+<encoding>` to indicate an in-toto [Statement] payload and its serialized `<encoding>` format.

### SD-24 (editorial) — Misspellings and slips

Misspellings at L51 and L978; a singular Consumer at L792 and L825; both version at L1085; L944 calls the appended vulnerability scan a TestResult. None changes a rule.

<!-- q L51-51 "This c" .. "le" -->
> This change is backwards comptabile

<!-- q L792-793 "Consum" .. "." -->
> Consumer SHOULD only rely on the `predicateType` field in the [Statement] layer.

<!-- q L944-944 -->
> The TestResult is then appended to the contents of `fooly.apk.intoto.jsonl`

<!-- q L978-978 -->
> Fooly Inc. wants to publish all of the accumulated attestations for evey

<!-- q L1085-1085 "(All f" .. "," -->
> (All fields present in both version have the same meaning,

### SD-25 (defect) — The standard algorithm names: rule, coverage and identity

(a) The stated derivation does not produce the listed keys: lowercasing the NIST name SHA-256 and replacing its hyphen gives sha_256, and SHA-512/224 gives sha_512/224, where the heading lists sha256 and sha512_224, and SHA-1 gives sha_1 for sha1; only the FIPS 202 names come out right (sha3_224 to sha3_512, shake128, shake256), 6 of the 19. R-0205 takes the heading's spellings. (b) blake2b, blake2s, ripemd160, sm3, gost and md5 are not NIST algorithms, so the rule cannot be what names them. (c) shake128 and shake256 are extendable-output functions, blake2b and blake2s have variable digest lengths, and gost names more than one standard; no output length or variant is given, so two producers can put different values under one key. (d) gitCommit, gitTree, gitBlob and gitTag take either a SHA-1 or a SHA-256 git object name under one key, told apart only by length, and values of the two never match one another.

<!-- q L444-444 -->
> 5.2.1.1. `sha256`, `sha224`, `sha384`, `sha512`, `sha512_224`, `sha512_256`, `sha3_224`, `sha3_256`, `sha3_384`, `sha3_512`, `shake128`, `shake256`, `blake2b`, `blake2s`, `ripemd160`, `sm3`, `gost`, `sha1`, `md5`

<!-- q L446-448 -->
> Standard cryptographic hash algorithms using [the NIST names][] (converting to lowercase and replacing `-` with `_`) as keys and lowercase hex-encoded values, for cases when the method of serialization is obvious or well known.

<!-- q L517-518 "The lo" .. "." -->
> The lowercase hex SHA-1 (40 character) or SHA-256 (64 character) of a git commit, tree, blob, or tag object, respectively.

### SD-26 (tension) — The optional keyid skip changes which attesters are found

The attester loop may skip a public key that signature.keyid does not match. When keyid names one recognized key and the signature verifies under another, a consumer that skips finds no attester there and one that does not finds the second key's attester; two conforming consumers then disagree on attesterNames and possibly on rejecting (R-0190). The source marks the skip optional and says nothing of this (R-0210).

<!-- q L1138-1141 -->
> - Optional: skip if `signature.keyid` does not match `publicKey` - If `signature.sig` matches `publicKey`: - Add `name` to `attesterNames`

### SD-27 (tension) — A MINOR release widened payloadType outside the versioning guarantees

MINOR releases are backwards-compatible semantic updates (R-0125), yet v1.2 added a payloadType value under the same `_type`, and the compatibility rules of §11 cover the Statement and predicates only (R-0179), not the envelope. A consumer written to v1.1's single generic value rejects every v1.2 envelope that uses a predicate-specific type; nothing in the source says whether that is a compatible change. Found by the protocol lane (protocol.yaml SD-15) and the design-notes lane (design-notes.md §12, its SD-10); added here by pass 2 so the canonical list carries it.

<!-- q L36-37 -->
> Backwards-compatible semantic updates to the spec (except predicates) are indicated through new tagged MINOR version releases.

<!-- q L1035-1036 -->
> - Expanded the allowed values for the envelope's `payloadType` field to `application/vnd.in-toto.<predicate>+json`. See [Envelope Fields].

<!-- q L1060-1061 -->
> The following rules apply to both Statement and predicate specification versioning.

## Crosswalk: the other lanes' source-defect lists

Four lists exist, numbered independently, so an SD number means nothing without its file: this file's SD-1 to SD-27 (cited by requirements.yaml), messages.yaml SD-01 to SD-08, protocol.yaml SD-01 to SD-18 (copied onto steps and transitions as source_defects), and design-notes.md §12 SD-1 to SD-10. They were reconciled by pass 2: no two entries contradict each other on what the source says. Each row below is one defect; a dash means that list does not carry it.

| this file | messages.yaml | protocol.yaml | design-notes.md §12 |
|---|---|---|---|
| SD-1 general vs DSSE payloadType form | SD-04 | SD-06 | — |
| SD-2 validation payloadType OR | SD-02 | SD-01 | SD-1 |
| SD-3 statement.type for _type | SD-03 | SD-02 | SD-2 |
| SD-4 dirHash1 in the dirHash example | SD-01 | SD-18 | SD-4 |
| SD-5 publishing example rewrites payloadType | SD-05 | SD-07 | SD-5 |
| SD-6 case-normalization gloss vs RFC 3986 §6.2.2.1 | — | — | — |
| SD-7 consumer rules conditional in §8.2, not in §8.4 | — | — | — |
| SD-8 validation model covers less than the spec | — | SD-05, SD-10, SD-11, SD-12 | SD-3, SD-9 |
| SD-9 local name compared with global uri | — | — | SD-8 |
| SD-10 RECOMMEND, STRONGLY RECOMMENDED | — | — | — |
| SD-11 RFC 2119 without RFC 8174 | — | — | — |
| SD-12 cryptographic vs any immutable reference | — | — | SD-3, SD-6 |
| SD-13 ANY match ignores a disagreeing entry | — | — | — (D-2) |
| SD-14 JSON by link only | — | — | — |
| SD-15 UTC spellings | — | — | — |
| SD-16 do the parsing rules bind every predicate | — | — | — |
| SD-17 content typed bytes; 1KB undefined | — | — | — |
| SD-18 dirHash pipeline not equivalent | — | — | — |
| SD-19 SPDX media types match no predicate file | — | SD-08 | — |
| SD-20 storage media type only predicate-specific | — | — | — |
| SD-21 validation model list nesting | — | SD-03, SD-04 | — |
| SD-22 payload SHOULD be included, MUST be parsed | — | SD-13 | — |
| SD-23 general form admits undefined encodings | — | — | — (§8, open question 9) |
| SD-24 misspellings and slips | SD-08 | SD-09 | — |
| SD-25 standard algorithm names | SD-07 | — | — |
| SD-26 optional keyid skip changes the attesters | — | SD-14 (keyid derivation, absent keyid) | — |
| SD-27 MINOR release widened payloadType | — | SD-15 | SD-10 |

Carried by one lane only, with no entry here, and why: messages.yaml SD-06 (the examples' placeholders are not valid hex, base64 or JSON; a property of illustrations, recorded per fixture in examples/README.md, not a defect in a rule); protocol.yaml SD-16 (the §9.4 scanner's non-in-toto envelope, which §12 rejects, inside a policy check the example does not explain; non-normative example), SD-17 (subject matching ignores content type, which the source states as its rule and itself flags at L208-210); design-notes.md SD-7 (the consumer MUSTs R-0062 and R-0072 state no order of parsing and verifying; requirements.yaml R-0214, inferred, gives the order).

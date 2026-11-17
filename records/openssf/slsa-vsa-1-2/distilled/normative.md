---
record: slsa-vsa-1-2
kind: normative
title: "slsa-vsa-1-2 — normative text"
generated_by: bin/fx1-skeleton
reviewed_by: ""
---

# Normative text

Every requirement text in requirements.yaml that has source lines appears here verbatim under its section, as a marker that `bin/check-quotes --render` writes and `bin/check-quotes` verifies; split_of children are listed on their parent line rather than quoted twice. The keyword-less binding text pass 1 added (candidate-stated and hunted entries) is interleaved in source order. Generated together with requirements.yaml: 94 requirements, of which 15 skeleton, 19 split children (17 from pass 1; R-0093 and R-0094 from pass 2), 17 from candidates, 32 hunted and 11 inferred. Section numbers are the ones `distilled/render-source.py` gives the page's headings (§1 Purpose to §7 Change history); Preamble is the untitled text before §1.

## Keyword declaration

The page carries no key-words declaration: no RFC 2119, RFC 8174 or BCP 14 reference, and nothing else that says how its capitals are to be read. Its 21 capitalised keywords (MUST 10, SHOULD 5, MAY 4, MUST NOT 2) are read as BCP 14 in the RFC 8174 sense, capitals only, because each is used that way: as an obligation, a recommendation or a permission. Lowercase may, must, required and optional are not BCP 14 here. The eleven required and optional annotations of the §3.2 field table still bind, as presence rules, and are entries with verb none; so are the §5 steps (under the MUST of R-0011) and the §6 shapes (under the SHOULD of R-0014). Whether a SLSA-wide page declares the keywords is outside this source. The judgement is recorded in the reconciliation of requirements.yaml.

## Preamble

<!-- q L14-14 -->
> "predicateType": "https://slsa.dev/verification_summary/v1"

R-0016 · no candidate (hunted)

<!-- q L17-18 "Important:" .. "the URL bar." -->
> Important: Always use the above string for `predicateType` rather than what is > in the URL bar.

R-0017 · no candidate (hunted)

<!-- q L18-19 "The `predicateType`" .. "specification." -->
> The `predicateType` URI will always resolve to the latest > minor version of this specification.

R-0018 · no candidate (hunted)

## §2

<!-- q L42-45 "A Verification" .. "some `policy`." -->
> A Verification Summary Attestation (VSA) is an attestation that some entity (`verifier`) verified one or more software artifacts (the `subject` of an in-toto attestation [Statement]) by evaluating the artifact and a `bundle` of attestations against some `policy`.

R-0019 · no candidate (hunted)

<!-- q L51-58 "The verifier" .. "`vsa.dependencyLevels`." -->
> The verifier does this by either a) verifying the provenance of each non-source dependency listed in the [resolvedDependencies](build-provenance#resolvedDependencies) of the artifact being verified (recursively) or b) matching the non-source dependency listed in `resolvedDependencies` (`subject.digest` == `resolvedDependencies.digest` and, ideally, `vsa.resourceUri` == `resolvedDependencies.uri`) to a VSA _for that dependency_ and using `vsa.verifiedLevels` and `vsa.dependencyLevels`.

R-0020 · no candidate (hunted)

## §3

<!-- q L66-66 -->
> "_type": "https://in-toto.io/Statement/v1",

R-0021 · no candidate (hunted)

<!-- q L69-69 -->
> "digest": { <digest-in-request> }

R-0022 · no candidate (hunted)

<!-- q L83-83 -->
> "resourceUri": <artifact-URI-in-request>,

R-0023 · no candidate (hunted)

## §3.1

<!-- q L108-108 "This predicate" .. "[parsing rules]." -->
> This predicate follows the in-toto attestation [parsing rules].

R-0024 · no candidate (hunted)

<!-- q L110-110 -->
> - Consumers MUST ignore unrecognized fields.

R-0001

<!-- q L111-112 -->
> - The `predicateType` URI includes the major version number and will always change whenever there is a backwards incompatible change.

R-0025 · candidate C-0003

<!-- q L113-114 -->
> - Minor version changes are always backwards compatible and "monotonic." Such changes do not update the `predicateType`.

R-0026 · candidate C-0004; R-0027 · candidate C-0005 · one bullet, quoted whole (an anchor cannot end on its closing quotation mark)

<!-- q L115-115 -->
> - Producers MAY add extension fields using field names that are URIs.

R-0002

## §3.2

<!-- q L119-120 "For a description" .. "[Statement]._" -->
> For a description of the other top-level fields, such as `subject`, see [Statement]._

R-0028 · no candidate (hunted)

<!-- q L123-123 -->
> `verifier` _object, required_

R-0029 · no candidate (hunted)

<!-- q L125-127 "> Identifies" .. "care about." -->
> > Identifies the entity that performed the verification. > > The identity MUST reflect the trust base that consumers care about.

R-0003 · split: R-0030, R-0093

<!-- q L127-130 "How > detailed" .. "verifier) pairs." -->
> How > detailed to be is a judgment call. > > Consumers MUST accept only specific (signer, verifier) pairs.

R-0004

<!-- q L135-136 "The field is" .. "debugging." -->
> The field is required, even if it is implicit from the signer, to aid readability and > debugging.

R-0031 · candidate C-0006

<!-- q L140-140 -->
> `verifier.id` _string ([TypeURI]), required_

R-0032 · no candidate (hunted)

<!-- q L142-142 "URI indicating" .. "verifier’s identity." -->
> URI indicating the verifier’s identity.

R-0033 · no candidate (hunted)

<!-- q L145-145 -->
> `verifier.version` _map (string->string), optional_

R-0034 · no candidate (hunted)

<!-- q L147-147 "Map of names" .. "their version." -->
> Map of names of components of the verification platform to their version.

R-0035 · no candidate (hunted)

<!-- q L150-150 -->
> `timeVerified` _string ([Timestamp]), optional_

R-0036 · no candidate (hunted)

<!-- q L152-152 "Timestamp indicating" .. "verification occurred." -->
> Timestamp indicating what time the verification occurred.

R-0037 · no candidate (hunted)

<!-- q L155-155 -->
> `resourceUri` _string ([ResourceURI]), required_

R-0038 · no candidate (hunted)

<!-- q L157-160 "> URI that" .. "verification." -->
> > URI that identifies the resource associated with the artifact being verified. > > The `resourceUri` SHOULD be set to the URI from which the producer expects the > consumer to fetch the artifact for verification.

R-0005 · split: R-0039, R-0094

<!-- q L161-164 "If the >" .. "out-of-band channel." -->
> If the > `resourceUri` is set to some other value, the producer MUST communicate the > expected value, or how to determine the expected value, to consumers through > an out-of-band channel.

R-0006

<!-- q L167-167 -->
> `policy` _object ([ResourceDescriptor]), required_

R-0040 · no candidate (hunted)

<!-- q L169-172 -->
> > Describes the policy that the `subject` was verified against. > > The entry MUST contain a `uri` identifying which policy was applied and > SHOULD contain a `digest` to indicate the exact version of that policy.

R-0007 · split: R-0041, R-0042, R-0043

<!-- q L175-175 -->
> `inputAttestations` _array ([ResourceDescriptor]), optional_

R-0044 · no candidate (hunted)

<!-- q L177-185 -->
> > The collection of attestations that were used to perform verification. > Conceptually similar to the `resolvedDependencies` field in [SLSA Provenance]. > > This field MAY be absent if the verifier does not support this feature. > If non-empty, this field MUST contain information on _all_ the attestations > used to perform verification. > > Each entry MUST contain a `digest` of the attestation and SHOULD contains a > `uri` that can be used to fetch the attestation.

R-0008 · split: R-0045, R-0046, R-0047, R-0048, R-0049

<!-- q L188-188 -->
> `verificationResult` _string, required_

R-0050 · no candidate (hunted)

<!-- q L190-190 "Either “PASSED”" .. "verification." -->
> Either “PASSED” or “FAILED” to indicate if the artifact passed or failed the policy verification.

R-0051 · no candidate (hunted)

<!-- q L193-193 -->
> `verifiedLevels` _array ([SlsaResult]), required_

R-0052 · no candidate (hunted)

<!-- q L195-199 "> Indicates" .. "SLSA track." -->
> > Indicates the highest level of each track verified for the artifact (and not > its dependencies) and any [verified properties](verified-properties) verified > for the artifact or "FAILED" if policy verification failed. > > Users MUST NOT include more than one level per SLSA track.

R-0009 · split: R-0053, R-0054

<!-- q L199-202 "Note that each" .. "per track." -->
> Note that each SLSA > level implies all levels below it (e.g. `SLSA_BUILD_LEVEL_3` implies > `SLSA_BUILD_LEVEL_2` and `SLSA_BUILD_LEVEL_1`), so there is no need to > include more than one level per track.

R-0055 · candidate C-0007

<!-- q L205-205 -->
> `dependencyLevels` _object, optional_

R-0056 · no candidate (hunted)

<!-- q L207-207 "A count of" .. "SLSA level." -->
> A count of the dependencies at each SLSA level.

R-0057 · no candidate (hunted)

<!-- q L209-210 "Map from [SlsaResult]" .. "indicated level." -->
> Map from [SlsaResult] to the number of the artifact's _transitive_ dependencies > that were verified at the indicated level.

R-0058 · no candidate (hunted)

<!-- q L210-217 "Absence of" .. "level verified." -->
> Absence of a given level of > [SlsaResult] MUST be interpreted as reporting _0_ dependencies at that level. > A set but empty `dependencyLevels` object means that the artifact has **no** > dependency at all, while an unset or null `dependencyLevels` means that the > verifier makes no claims about the artifact's dependencies. > > Users MUST count each dependency only once per SLSA track, at the highest > level verified.

R-0010 · split: R-0059, R-0060, R-0061

<!-- q L217-219 "For example," .. "`SLSA_BUILD_LEVEL_1`." -->
> For example, if a dependency meets `SLSA_BUILD_LEVEL_2`, > you include it with the count for `SLSA_BUILD_LEVEL_2` but not the count for > `SLSA_BUILD_LEVEL_1`.

R-0062 · no candidate (hunted)

<!-- q L222-222 -->
> `slsaVersion` _string, optional_

R-0063 · no candidate (hunted)

<!-- q L224-225 "Indicates the" .. "`<MAJOR>.<MINOR>`." -->
> Indicates the version of the SLSA specification that the verifier used, in the > form `<MAJOR>.<MINOR>`.

R-0064 · no candidate (hunted)

<!-- q L225-226 "If unset, the" .. "version of `1.x`." -->
> If unset, the default is an > unspecified minor version of `1.x`.

R-0065 · no candidate (hunted)

## §5

<!-- q L274-276 "We call the" .. "'verification'." -->
> We call the process of establishing a VSA's authenticity and determining whether it meets the consumer's goals 'verification'.

R-0066 · no candidate (hunted)

<!-- q L281-281 -->
> Verification MUST include the following steps:

R-0011

<!-- q L283-284 "1. Verify the" .. "roots of trust." -->
> 1. Verify the signature on the VSA envelope using the preconfigured roots of trust.

R-0067 · candidate C-0008

<!-- q L287-288 "2. Verify the" .. "in question." -->
> 2. Verify the statement's `subject` matches the digest of the artifact in question.

R-0068 · candidate C-0010

<!-- q L290-291 "3. Verify that" .. "`https://slsa.dev/verification_summary/v1`." -->
> 3. Verify that the `predicateType` is `https://slsa.dev/verification_summary/v1`.

R-0069 · candidate C-0012

<!-- q L294-295 "4. Verify that" .. "in step 1." -->
> 4. Verify that the `verifier` matches the public key (or equivalent) used to verify the signature in step 1.

R-0070 · candidate C-0014

<!-- q L298-299 "5. Verify that" .. "expected value." -->
> 5. Verify that the value for `resourceUri` in the VSA matches the expected value.

R-0071 · candidate C-0015

<!-- q L302-302 "6. Verify that" .. "is `PASSED`." -->
> 6. Verify that the value for `verificationResult` is `PASSED`.

R-0072 · candidate C-0017

<!-- q L305-305 "7. Verify that" .. "expected value." -->
> 7. Verify that `verifiedLevels` contains the expected value.

R-0073 · candidate C-0019

<!-- q L308-308 -->
> Verification MAY additionally contain the following step:

R-0012

<!-- q L310-311 -->
> 1. (Optional) Verify additional fields required to determine whether the VSA meets your goal.

R-0074 · candidate C-0021

<!-- q L317-318 "Instead, VSA" .. "roots of trust." -->
> Instead, VSA consumers SHOULD carefully consider which verifiers they add to their roots of trust.

R-0013

## §6

<!-- q L375-375 -->
> The result of evaluating an artifact (or set of artifacts) against SLSA.

R-0075 · no candidate (hunted)

<!-- q L376-376 -->
> SHOULD be

R-0014

<!-- q L378-379 -->
> - The [SLSA Track](#tracks) level the referenced artifact qualifies for as `SLSA_<TRACK_NAME>_LEVEL_<LEVEL_NUMBER>`, or

R-0076 · candidate C-0042

<!-- q L380-381 -->
> - `SLSA_<TRACK NAME>_LEVEL_UNEVALUATED` if the VSA issuer does not want to make a claim about the track level an artifact meets

R-0077 · candidate C-0043

<!-- q L390-390 -->
> - `FAILED` (Indicates policy evaluation failed)

R-0078 · candidate C-0049

<!-- q L392-392 -->
> Note that each SLSA level implies the levels below it in the same track.

R-0079 · candidate C-0050

<!-- q L396-397 -->
> Users MAY use custom values here but MUST NOT use custom values starting with `SLSA_`.

R-0015 · split: R-0080, R-0081

## Not normative

Not carried as requirements, each with its reason in inferred-candidates.yaml or here: the Jekyll front matter (L1-5) and the page's opening sentence (L7-8), which describe it; §1 (purpose, descriptive); C-0001 (§2, who may rely on a VSA), a model statement; §4, the example, which the page marks as for demonstration only (L230); §5.1, the two worked examples, whose items are rejected as illustrative instances of steps 1 to 7, except C-0028, C-0038 and C-0041, which imply R-0082 and R-0084; §7, the change history (C-0051 to C-0067); and the link definitions at L423-432, which pin the in-toto types and parsing rules to in-toto/attestation commit 7aefca35 and are named in the notes of the entries that use them. The sentence that verification mitigates different threats depending on the VSA's contents and the procedure (L313-314) is a description and binds nothing. Rationale sentences are left out as rationale: the sentence after each §5 step (rejected candidates), L136-137 on why verifier is an object, and L160-161 on why resourceUri should be the fetch URI.

## Inferred requirements (not verbatim)

These entries are in our words and quote nothing; each names what it is derived from in `derived_from`. R-0082 (§5), R-0083 (§5), R-0084 (§5), R-0085 (§5), R-0086 (§5), R-0087 (§2), R-0088 (§3.2), R-0089 (§3.2), R-0090 (§3.2), R-0091 (§3.2), R-0092 (§2).

## Source defects

Inconsistencies and gaps in this page itself, found reading the source for this pass. Each quotes the lines it rests on; the prose is ours. Severity: SD-1, SD-2, SD-8, SD-11, SD-15, SD-20 and SD-26 leave an implementer two readings, name a field that does not exist, or (SD-20) make a stated method unable to keep a MUST; the rest are narrow gaps or editorial. This is the canonical list for the record: other artifacts cite these ids. Pass 1's lanes kept lists of their own; pass 2 (verify) merged them here, losing none: SD-18 to SD-27 are the entries those lists held and this one did not, and the crosswalk at the end maps every lane id to its canonical id.

### SD-1 — §2, §3.2: one predicate, several subjects

§2 lets one VSA cover one or more artifacts, all of them its subject, but the §3.2 descriptions of resourceUri, verificationResult, verifiedLevels and dependencyLevels each speak of a single artifact, and resourceUri is one URI. Whether verificationResult, verifiedLevels and dependencyLevels hold for each subject or for the set, and what one resourceUri means for several artifacts, is not said. How the in-toto Statement relates a predicate to several subjects is outside this source and was not consulted. Read here as each holding for each subject (R-0092).

<!-- q L42-45 "A Verification" .. "some `policy`." -->
> A Verification Summary Attestation (VSA) is an attestation that some entity (`verifier`) verified one or more software artifacts (the `subject` of an in-toto attestation [Statement]) by evaluating the artifact and a `bundle` of attestations against some `policy`.

<!-- q L157-157 "URI that identifies" .. "being verified." -->
> URI that identifies the resource associated with the artifact being verified.

Requirements affected: R-0019, R-0068, R-0092.

### SD-2 — §2 against §3.2: only non-source dependencies are reached, but all are counted

§2 says the verifier reaches the levels of non-source dependencies only, by their provenance or by their VSAs. §3.2 counts the artifact's transitive dependencies without that qualifier, and reads an empty object as no dependency at all. An artifact whose only dependencies are source dependencies therefore gets either an empty dependencyLevels by the §2 method, which §3.2 reads as having no dependencies, or counts §2 gives no way to obtain. §6 lists source-track values among its examples (L388-389), so a source-track key in dependencyLevels is well formed, and nothing says how it would be counted.

<!-- q L51-54 "The verifier" .. "(recursively)" -->
> The verifier does this by either a) verifying the provenance of each non-source dependency listed in the [resolvedDependencies](build-provenance#resolvedDependencies) of the artifact being verified (recursively)

<!-- q L209-210 "Map from [SlsaResult]" .. "indicated level." -->
> Map from [SlsaResult] to the number of the artifact's _transitive_ dependencies > that were verified at the indicated level.

<!-- q L212-213 "A set but" .. "dependency at all," -->
> A set but empty `dependencyLevels` object means that the artifact has **no** > dependency at all,

Requirements affected: R-0020, R-0058, R-0060, R-0087.

### SD-3 — §3: the schema's placeholders name a request the page never defines

The schema writes the subject digest and resourceUri as the digest and artifact URI in request. No request, requester or response appears anywhere else on the page; the prose ties resourceUri to where the producer expects consumers to fetch the artifact (R-0005) instead. The placeholders imply that a VSA answers a verification request about one artifact URI and digest, an exchange this page does not describe.

<!-- q L69-69 -->
> "digest": { <digest-in-request> }

<!-- q L83-83 -->
> "resourceUri": <artifact-URI-in-request>,

Requirements affected: R-0022, R-0023.

### SD-4 — §3, §4: the schema block is not well formed

L87 closes the policy object with no comma before the next member: invalid in JSON, and in JSON with comments, which is what the fence is labelled. L102 in the schema and L266 in the example leave a trailing comma before a closing brace, which strict JSON rejects. Neither block is wrapped in braces, and the schema writes unquoted placeholders and ellipses, which are its notation; the missing comma is not notation. Editorial: no reading changes. No requirement rests on it.

<!-- q L84-88 -->
> "policy": { "uri": "<URI>", "digest": { <digest-of-policy-data> } } "inputAttestations": [

<!-- q L102-103 -->
> "slsaVersion": "<MAJOR>.<MINOR>", }

<!-- q L266-267 -->
> "SLSA_BUILD_LEVEL_1": 1, },

### SD-5 — §3.2: the (signer, verifier) example speaks of signing provenance

The only example of R-0004 says which signers can sign provenance for which verifier. A VSA is not provenance; the sentence reads as carried over from a builder's definition. Read: which signers can sign VSAs naming that verifier. Editorial, but it is the only illustration of the pair rule.

<!-- q L130-133 "For example," .. "verifier." -->
> For example, > "GitHub" can sign provenance for the "GitHub Actions" verifier, and "Google" > can sign provenance for the "Google Cloud Deploy" verifier, but "GitHub" cannot > sign for the "Google Cloud Deploy" verifier.

Requirements affected: R-0004.

### SD-6 — §3.2: an empty inputAttestations array is defined by neither branch

inputAttestations may be absent when the verifier does not support the feature, and must list every attestation used when non-empty. An empty array falls under neither: it can mean that the verifier used no attestations, or that it does not report them.

<!-- q L180-182 "This field" .. "verification." -->
> This field MAY be absent if the verifier does not support this feature. > If non-empty, this field MUST contain information on _all_ the attestations > used to perform verification.

Requirements affected: R-0046, R-0047.

### SD-7 — §3.2: SHOULD contains

Grammar: read contain. Kept verbatim in the requirement text.

<!-- q L184-185 "Each entry" .. "attestation." -->
> Each entry MUST contain a `digest` of the attestation and SHOULD contains a > `uri` that can be used to fetch the attestation.

Requirements affected: R-0049.

### SD-8 — §3.2: whether FAILED replaces the levels, and its tie to verificationResult

verifiedLevels holds the highest level per track and any verified properties, or FAILED on a failed policy verification. The page does not say whether FAILED is then the array's only element, nor that verifiedLevels and verificationResult have to agree. Read: FAILED alone, exactly when verificationResult is FAILED (R-0090).

<!-- q L195-197 "Indicates the" .. "verification failed." -->
> Indicates the highest level of each track verified for the artifact (and not > its dependencies) and any [verified properties](verified-properties) verified > for the artifact or "FAILED" if policy verification failed.

<!-- q L190-190 "Either “PASSED”" .. "verification." -->
> Either “PASSED” or “FAILED” to indicate if the artifact passed or failed the policy verification.

Requirements affected: R-0053, R-0090.

### SD-9 — §3.2, §6: users names the producer in three keyword sentences, and the consumer in §2

Three keyword sentences are addressed to users: one level per track (L199), counting each dependency once (L216) and custom values (L396). Each constrains what is written into a VSA, so the party bound is the VSA producer; but §2 uses the same word for the parties who trust the verifier, that is, consumers (L45). Actor recorded as VSA producer, with this SD named.

<!-- q L199-199 "Users MUST" .. "SLSA track." -->
> Users MUST NOT include more than one level per SLSA track.

<!-- q L216-216 "Users MUST" .. "the highest" -->
> Users MUST count each dependency only once per SLSA track, at the highest

<!-- q L396-396 "Users MAY use" .. "values here" -->
> Users MAY use custom values here

<!-- q L45-46 "Users who trust" .. "may assume" -->
> Users who trust the `verifier` may assume

Requirements affected: R-0009, R-0010, R-0015, R-0054, R-0061, R-0080, R-0081.

### SD-10 — §3.2: a null dependencyLevels is given a meaning its type does not admit

The field table types dependencyLevels as an object; the prose gives a null value a meaning, the same as unset. A validator built from the table rejects a null the prose allows. Read: null is permitted and means no claim.

<!-- q L205-205 -->
> `dependencyLevels` _object, optional_

<!-- q L213-214 "while an unset" .. "dependencies." -->
> while an unset or null `dependencyLevels` means that the > verifier makes no claims about the artifact's dependencies.

Requirements affected: R-0056, R-0060.

### SD-11 — §3.2: no key for a dependency verified at no level

Each dependency is counted once per track at the highest level verified. A dependency that was verified at no level of a track, failed, or was not evaluated has no stated key: SLSA_<TRACK>_LEVEL_0, the track's UNEVALUATED value, FAILED, or no key at all are all possible readings, and the minimum-level check of R-0087 depends on which.

<!-- q L216-217 "Users MUST" .. "level verified." -->
> Users MUST count each dependency only once per SLSA track, at the highest > level verified.

Requirements affected: R-0058, R-0061, R-0087.

### SD-12 — §5: steps most procedures share, made mandatory for all

The paragraph before the steps says that most verification procedures share them; the next sentence makes them mandatory for every verification. The MUST governs (R-0011); the sentence before it is read as motivation, not as a limit on scope.

<!-- q L278-279 -->
> However, there are certain steps that most verification procedures have in common.

<!-- q L281-281 -->
> Verification MUST include the following steps:

Requirements affected: R-0011.

### SD-13 — §5: step 4 names the verifier object, and no rule says how an identity matches a key

Step 4 checks that verifier, an object, matches the key used in step 1; both §5.1 examples check verifier.id instead, and nothing says how an identity matches a key. Read with R-0004: verifier.id is one the step 1 key is configured to sign for (R-0082).

<!-- q L294-295 "4. Verify that" .. "in step 1." -->
> 4. Verify that the `verifier` matches the public key (or equivalent) used to verify the signature in step 1.

<!-- q L332-332 -->
> - `verifier.id` is V.

<!-- q L356-356 -->
> - `verifier.id` is V.

Requirements affected: R-0070, R-0082.

### SD-14 — §5.1: the worked examples' wording

The first item of each example has no verb: the signature on the envelope, using V's key, with verifies left implicit. subject is said to be A, and, in example 2, verifiedLevels to be one of two values, where subject is a list of descriptors and verifiedLevels an array (step 7 says contains). Read literally, is fails a VSA that also lists a level of another track or a verified property (L196). Read: the signature verifies with V's key; some subject entry matches A; verifiedLevels contains one of the values. Editorial; the candidates are rejected as illustrative or promoted as inferred.

<!-- q L325-326 -->
> - The signature on the VSA envelope using V's public signing key from their preconfigured root of trust.

<!-- q L362-362 -->
> - `verifiedLevels` is `SLSA_BUILD_LEVEL_2` or `SLSA_BUILD_LEVEL_3`.

Requirements affected: R-0084.

### SD-15 — §5.1: both examples check slsaResult, a field that does not exist

Both examples check that slsaResult is PASSED. No such field exists: the field is verificationResult (step 6, R-0072). The 1.2 change history records fixing exactly this misnaming, so the fix missed §5.1. An implementation that follows §5.1 literally looks for a field no VSA carries.

<!-- q L336-336 -->
> - `slsaResult` is `PASSED`.

<!-- q L360-360 -->
> - `slsaResult` is `PASSED`.

<!-- q L405-406 -->
> - Fixed a typo where the verificationResult was incorrectly referred to as slsaResult.

Requirements affected: R-0072.

### SD-16 — §5.1, §6, §7: links to another version, to nowhere, and a change entry that misplaces one

Verifying artifacts is linked under /spec/v1.0/ from this v1.2 page (L366). The SLSA Track link targets #tracks, an anchor this page's source does not define (L378). The 1.2 change entry says the SlsaResult definition now links to verified properties (L402-404), but §6 has none; the one other link to verified properties on the page is in §3.2, under verifiedLevels (L196). Editorial.

<!-- q L366-366 -->
> [Verifying artifacts](/spec/v1.0/verifying-artifacts) for details about which

<!-- q L378-378 -->
> - The [SLSA Track](#tracks) level the referenced artifact qualifies for as

<!-- q L402-404 -->
> - Update SlsaResult definition to discuss how to refer to new tracks and link to [verified properties](verified-properties) for additional SLSA endorsed values.

<!-- q L196-196 -->
> > its dependencies) and any [verified properties](verified-properties) verified

Requirements affected: R-0076.

### SD-17 — §6: the SlsaResult shapes omit values the page defines

§6 says a SlsaResult should take one of two shapes: a track level, or the track's UNEVALUATED value. FAILED, defined in the same example list and in verifiedLevels, is neither; nor are the verified properties verifiedLevels may carry. The two shapes also spell their placeholder differently: TRACK_NAME with an underscore, TRACK NAME with a space. Whether FAILED may also be a dependencyLevels key, which the map's SlsaResult keys admit, is not said.

<!-- q L376-381 -->
> SHOULD be - The [SLSA Track](#tracks) level the referenced artifact qualifies for as `SLSA_<TRACK_NAME>_LEVEL_<LEVEL_NUMBER>`, or - `SLSA_<TRACK NAME>_LEVEL_UNEVALUATED` if the VSA issuer does not want to make a claim about the track level an artifact meets

<!-- q L390-390 -->
> - `FAILED` (Indicates policy evaluation failed)

<!-- q L195-197 "Indicates the" .. "verification failed." -->
> Indicates the highest level of each track verified for the artifact (and not > its dependencies) and any [verified properties](verified-properties) verified > for the artifact or "FAILED" if policy verification failed.

Requirements affected: R-0014, R-0076, R-0077, R-0078, R-0053.

### SD-18 — §2: a bundle, and vsa. paths, that name no field

§2 says the verifier evaluates a bundle of attestations, and names VSA fields as vsa.resourceUri, vsa.verifiedLevels and vsa.dependencyLevels. No field is called bundle: the attestations used are what inputAttestations lists (R-0045). The three fields sit under predicate (§3). Read vsa. as a VSA's predicate. Editorial.

<!-- q L44-45 "by evaluating" .. "some `policy`." -->
> by evaluating the artifact and a `bundle` of attestations against some `policy`.

<!-- q L56-58 "`vsa.resourceUri`" .. "`vsa.dependencyLevels`." -->
> `vsa.resourceUri` == `resolvedDependencies.uri`) to a VSA _for that dependency_ and using `vsa.verifiedLevels` and `vsa.dependencyLevels`.

Requirements affected: R-0019, R-0020.

### SD-19 — §5: the optional step is numbered 1

The step after the seven mandatory ones is numbered 1 again: the Markdown starts a new list. Read as the one optional step (R-0074). Editorial.

<!-- q L308-311 -->
> Verification MAY additionally contain the following step: 1. (Optional) Verify additional fields required to determine whether the VSA meets your goal.

Requirements affected: R-0074.

### SD-20 — §2 against §3.2: method b adds up counts that carry no identities

Method b takes a dependency's levels from a VSA for it, including that VSA's dependencyLevels. Those are counts per level, not the dependencies counted, so a verifier adding them up cannot see that two dependency VSAs counted the same transitive dependency, and cannot keep §3.2's rule to count each dependency once per track. Example: A depends on B and C, and both depend on D; A has 3 transitive dependencies, and B, C and one from each of their dependencyLevels make 4. The source gives no rule for combining the counts; adding them is the plain reading of using the two fields.

Measured by the protocol lane and replayed by pass 2 with a script of its own (neither committed), assuming each dependency VSA counts its own closure correctly. The graphs are every DAG on nodes 0 to n−1 whose edges run from a lower to a higher number, for n = 2 to 6: 2^(n(n−1)/2) graphs for each n, 33,866 in all, node 0 the artifact. That is not every labelled DAG (6 nodes alone have 3,781,503), but every DAG of up to 6 nodes is isomorphic to one of them, through a topological order; 10,105 of the 33,866 have every node reachable from node 0. Adding the direct dependencies' counts exceeds the true count in 23,845 graphs, exactly those where the closures of two direct dependencies, each including the dependency itself, intersect. The excess is, summed over the shared dependencies, the number of direct dependencies reaching each one minus one, and the sum is never short. With method b at every level the total is the number of paths from the artifact, which exceeds the count in 25,165 graphs, exactly those whose part reachable from the artifact is not a tree.

<!-- q L57-58 "and using" .. "`vsa.dependencyLevels`." -->
> and using `vsa.verifiedLevels` and `vsa.dependencyLevels`.

<!-- q L216-217 "Users MUST" .. "level verified." -->
> Users MUST count each dependency only once per SLSA track, at the highest > level verified.

Requirements affected: R-0020, R-0061, R-0087.

### SD-21 — §1, §3.1, §3.2, §5, §5.1: producer names two parties

§1 speaks of software producers that keep their build pipeline confidential; §5 calls the party that issues the VSA its producer (L277, L284, L295). The resourceUri rules (L159, L162), step 5's intended purpose (L300), the prenegotiation of §5.1 example 1 (L341) and the extension-field permission (L115) say producer without saying which. Where the software producer and the verifier are different organisations, who sets resourceUri and who owes the out-of-band communication is open. §2's policy verifiers (L58) are not defined either. Read: the VSA producer, that is the verifier, throughout §3.1, §3.2 and §5.

<!-- q L34-35 "It also allows" .. "taken place." -->
> It also allows software producers to keep the details of their build pipeline confidential while still communicating that some verification has taken place.

<!-- q L295-296 "This step identifies" .. "in step 1." -->
> This step identifies the VSA producer in cases where their identity is not implicitly revealed in step 1.

<!-- q L159-160 "The `resourceUri` SHOULD" .. "for verification." -->
> The `resourceUri` SHOULD be set to the URI from which the producer expects the > consumer to fetch the artifact for verification.

Requirements affected: R-0002, R-0006, R-0094, R-0083.

### SD-22 — §3.2: a track the producer did not count reads as zero

An absent key counts as zero dependencies at its level, so a dependencyLevels object that counts the Build track only, as the §4 example does (L263-267), states zero dependencies at every Source level. That cannot be told apart from a Source track the verifier never evaluated. A VSA can make no claim about one track's dependencies only by leaving dependencyLevels unset, which withdraws the claim for every track.

<!-- q L210-211 "Absence of" .. "at that level." -->
> Absence of a given level of > [SlsaResult] MUST be interpreted as reporting _0_ dependencies at that level.

Requirements affected: R-0059, R-0087.

### SD-23 — §3.1, §7: a minor version made a field optional, and no field names the minor version

Minor versions are called backwards compatible and keep the predicateType, yet 1.1 made timeVerified optional, so a consumer written to 1.0 that relied on the field is broken by a change the page counts as compatible. And nothing in a VSA says which minor version of this page it follows: slsaVersion names the version of the SLSA specification the verifier used.

<!-- q L113-114 -->
> - Minor version changes are always backwards compatible and "monotonic." Such changes do not update the `predicateType`.

<!-- q L412 -->
> - Made `timeVerified` optional.

<!-- q L224-225 "Indicates the version" .. "`<MAJOR>.<MINOR>`." -->
> Indicates the version of the SLSA specification that the verifier used, in the > form `<MAJOR>.<MINOR>`.

Requirements affected: R-0026, R-0027, R-0036, R-0064.

### SD-24 — §3.2: the digest of an attestation names no bytes

Each inputAttestations entry must carry a digest of the attestation, without saying of which bytes: the signed envelope, the Statement, or one line of a bundle file. The §4 example's entry points at a .intoto.jsonl file (L257), a file of attestations rather than one.

<!-- q L184 "Each entry MUST" .. "of the attestation" -->
> Each entry MUST contain a `digest` of the attestation

<!-- q L257 -->
> "uri": "https://example.com/provenances/example-1.2.3.tar.gz.intoto.jsonl",

Requirements affected: R-0048.

### SD-25 — §5: the steps are listed, not ordered

Verification must include the steps; nothing says in what order. The only dependency between them is step 4's use of the key that verified step 1, so a consumer may parse the Statement and check predicateType before it verifies the signature and still conform. Read: any order with step 1 before step 4 (R-0085).

<!-- q L281 -->
> Verification MUST include the following steps:

<!-- q L294-295 "4. Verify that" .. "in step 1." -->
> 4. Verify that the `verifier` matches the public key (or equivalent) used to verify the signature in step 1.

Requirements affected: R-0011, R-0070, R-0085.

### SD-26 — §2, §5: how a digest set matches is not stated

Step 2 has the subject match the artifact's digest, and method b matches subject.digest with resolvedDependencies.digest. Both are digest sets, from algorithm to value, and a subject is a list of entries. The page does not say whether one shared algorithm suffices, whether every algorithm present must agree, or which entry of several counts; nor does method b say that the matched VSA must itself be verified before its levels are used. The in-toto Statement's own rules are outside this source and were not consulted.

<!-- q L287-288 "2. Verify the" .. "in question." -->
> 2. Verify the statement's `subject` matches the digest of the artifact in question.

<!-- q L55-56 "(`subject.digest` ==" .. "`resolvedDependencies.digest`" -->
> (`subject.digest` == `resolvedDependencies.digest`

Requirements affected: R-0020, R-0068.

### SD-27 — §3.2, §5: no rule for a VSA that lacks a required field

§3.2 marks six fields required (verifier, verifier.id, resourceUri, policy, verificationResult, verifiedLevels). The §5 steps read verifier, resourceUri, verificationResult and verifiedLevels, and §5.1 verifier.id; no step reads policy. Nothing says whether a consumer rejects a VSA that lacks a required field; R-0001 governs unrecognised fields only.

<!-- q L167 -->
> `policy` _object ([ResourceDescriptor]), required_

Requirements affected: R-0040, R-0085.

## Crosswalk: the lanes' source-defect lists

Pass 1 ran its lanes in parallel, and four of them kept their own lists. Pass 2 merged them into the canonical list above and relabelled every lane citation to the canonical id; the lane ids below survive only here. Protocol open issues that are not defects of the page stay open issues in protocol.yaml.

| lane list | lane id | canonical id |
|---|---|---|
| normative.md and requirements.yaml (pass 1) | SD-1 to SD-17 | SD-1 to SD-17, unchanged |
| messages.yaml | SD-01 | SD-15 |
| messages.yaml | SD-02 (schema block), SD-03 (§4 example) | SD-4 |
| messages.yaml | SD-04 | SD-17 |
| messages.yaml | SD-05 | SD-18 |
| messages.yaml | SD-06 | SD-8 |
| messages.yaml | SD-07 | SD-10 |
| messages.yaml | SD-08 | SD-9 |
| messages.yaml | SD-09 | SD-14 |
| messages.yaml | SD-10 | SD-19 |
| protocol.yaml, protocol.md, state-machine.yaml | SD-01 | SD-15 |
| protocol.yaml, protocol.md, state-machine.yaml | SD-02 | SD-14 |
| protocol.yaml, protocol.md, state-machine.yaml | SD-03 | SD-20 |
| protocol.yaml, protocol.md | SD-04 | SD-5 |
| protocol.yaml open issues | OI-02 | SD-21 |
| protocol.yaml open issues | OI-03 | SD-9 |
| protocol.yaml open issues | OI-04, OI-08 | SD-26 |
| protocol.yaml open issues | OI-05 | SD-13 |
| protocol.yaml open issues | OI-06 | SD-27 |
| protocol.yaml open issues | OI-07 | SD-8 |
| protocol.yaml open issues | OI-09 | SD-11, SD-2 |
| protocol.yaml open issues | OI-10 | SD-12 |
| protocol.yaml open issues | OI-12 | SD-20 (counts, not identities), SD-21 (policy verifiers) |
| protocol.yaml open issues | OI-01, OI-11 | none: transport and lifetime, which the page leaves to other documents; they stay open issues |
| design-notes.md §10 | 1 | SD-15 |
| design-notes.md §10 | 2 | SD-5 |
| design-notes.md §10 | 3 | SD-21 |
| design-notes.md §10 | 4 | SD-9 |
| design-notes.md §10 | 5 | SD-8, SD-17 |
| design-notes.md §10 | 7 | SD-22 |
| design-notes.md §10 | 8 | SD-26, SD-1 |
| design-notes.md §10 | 9 | SD-23 |
| design-notes.md §10 | 10 | SD-6, SD-24 |
| design-notes.md §10 | 11 | SD-25 |
| design-notes.md §10 | 12 | SD-14 |
| design-notes.md §10 | 13 | SD-16 |
| design-notes.md §10 | 6, 14 to 19 | none: questions for m-of-n, not about the page |

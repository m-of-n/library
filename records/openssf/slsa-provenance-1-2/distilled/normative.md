---
record: slsa-provenance-1-2
kind: normative
title: "slsa-provenance-1-2 — normative text"
generated_by: bin/fx1-skeleton
extended_by: "pass 1, requirements lane (library#136); pass 2 (verify) added R-0170 and reconciled the source defects"
reviewed_by: ""
---

# Normative text

The skeleton's verbatim layer (`bin/fx1-skeleton`), extended by pass 1 (requirements lane). Every stated entry of `requirements.yaml` that is not a split child, keyword sentence and keyword-less binding text alike, appears here as a `<!-- q Lx-y "start" .. "end" -->` marker whose words `bin/check-quotes --render` wrote, in source order under its section, followed by its id. A split parent names its children on its id line instead of quoting them again. Inferred entries are not quoted: they are our words, not the source's (`requirements.yaml`, kind: inferred).

## How this page binds

- The prose and the field tables of §1 to §4.7 are authoritative. The cue summary (L124-173) and the protobuf schema (L188-239) are declared informative, the text prevailing in any disagreement (R-0073, R-0074); nothing in them is extracted as a requirement except where the text says the same. The serialization rule stated only in a protobuf comment (C-0024) is therefore the inferred R-0158. The cue's description of itself as a human-readable summary sits in an HTML comment (L119-122) the rendered page does not show; the protobuf's (L183-186) is shown. Compared by eye, field names, nesting and types in the two summaries agree with the §4.2 to §4.6 tables. Two differences remain for the text to settle: the cue marks no member optional where the annotations require only some (SD-9), and the two summaries draw different timestamp forms (SD-10).
- The §7 pseudocode is not declared informative, and §7 tells migrators to use it (R-0132): its three keyword comments and its field mappings bind migrators.
- The RFC 2119 recital (L25-27) binds nothing; it survives only as the withdrawn R-0001 (see the reconciliation in `requirements.yaml`).
- The five field annotations above the tables (L250, L272, L407, L441, L511) are the only lists of required fields; no field table has a per-field requirement column; one sentence after the §4.5 table calls a field REQUIRED without naming it (L503-504, R-0040, SD-8), and only internalParameters is called optional in so many words (L78).
- §5 Verification has no content of its own: it points to SLSA Verifying Artifacts (L559-560), another page of SLSA v1.2. Likewise the parsing rules (§3), the Statement, ResourceDescriptor and field types (the links in §4.2 to §4.6) are in-toto's. Rules depending on them are outside this source and not extracted; the entries that lean on them say so.

## front matter

<!-- q L13-17 -->
> This document defines the following predicate type within the [in-toto attestation] framework: ```json "predicateType": "https://slsa.dev/provenance/v1"

R-0051 (no keyword)

<!-- q L20-21 "Important: Always" .. "URL bar." -->
> Important: Always use the above string for `predicateType` rather than what is > in the URL bar.

R-0052 (no keyword)

<!-- q L21-22 "The `predicateType` URI" .. "this specification." -->
> The `predicateType` URI will always resolve to the latest > minor version of this specification.

R-0170 (no keyword; added in pass 2)

<!-- q L25-27 -->
> The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in [RFC 2119](https://www.rfc-editor.org/rfc/rfc2119).

R-0001 (withdrawn: the RFC 2119 recital, binds nothing)

## §1

<!-- q L37-38 -->
> This predicate is the RECOMMENDED way to satisfy the SLSA v1.0 [provenance requirements](requirements#provenance-generation).

R-0002 (RECOMMENDED)

## §2

<!-- q L42-43 -->
> Provenance is an attestation that a particular build platform produced a set of software artifacts through execution of the `buildDefinition`.

R-0053 (no keyword)

<!-- q L54-56 "The `builder.id`" .. "the provenance." -->
> The `builder.id` identifies this platform, representing the transitive closure of all entities that are [trusted] to faithfully run the build and record the provenance.

R-0054 (no keyword; C-0005)

<!-- q L59-61 "- The" .. "and interfaces." -->
> - The build platform implementer SHOULD define a security model for the build platform in order to clearly identify the platform's boundaries, actors, and interfaces.

R-0003 (SHOULD)

<!-- q L61-63 "This model" .. "control plane." -->
> This model SHOULD then be used to identify the transitive closure of the trusted build platform for the `builder.id` as well as the trusted control plane.

R-0004 (SHOULD)

<!-- q L65-66 "- The" .. "by `buildType`." -->
> - The build process is defined by a parameterized template, identified by `buildType`.

R-0055 (no keyword; C-0007)

<!-- q L70-71 "- All" .. "the template." -->
> - All top-level, independent inputs are captured by the parameters to the template.

R-0056 (no keyword; C-0010)

<!-- q L73-73 "- `externalParameters`:" .. "the build." -->
> - `externalParameters`: the external interface to the build.

R-0057 (no keyword; C-0012)

<!-- q L73-75 "In SLSA," .. "verified downstream." -->
> In SLSA, these values are untrusted; they MUST be included in the provenance and MUST be verified downstream.

R-0005 (MUST; split: R-0058, R-0059)

<!-- q L77-77 "- `internalParameters`:" .. "the platform." -->
> - `internalParameters`: set internally by the platform.

R-0060 (no keyword; C-0013)

<!-- q L77-79 "In SLSA," .. "verified downstream." -->
> In SLSA, these values are trusted because the platform is trusted; they are OPTIONAL and need not be verified downstream.

R-0006 (OPTIONAL; split: R-0061, R-0062)

<!-- q L79-80 "They MAY" .. "incident response." -->
> They MAY be included to enable reproducible builds, debugging, or incident response.

R-0007 (MAY)

<!-- q L82-84 "- All" .. "by parameters." -->
> - All artifacts fetched during initialization or execution of the build process are considered dependencies, including those referenced directly by parameters.

R-0063 (no keyword; C-0014)

<!-- q L84-85 "The `resolvedDependencies`" .. "if known." -->
> The `resolvedDependencies` captures these dependencies, if known.

R-0064 (no keyword; C-0015)

<!-- q L90-92 "This communication" .. "[SLSA Requirements](requirements.md)." -->
> This communication is not captured directly in the provenance, but is instead implied by `builder.id` and subject to [SLSA Requirements](requirements.md).

R-0065 (no keyword; C-0018)

<!-- q L92-94 "Such communication" .. "`resolvedDependencies` instead." -->
> Such communication SHOULD NOT influence the definition of the build; if it does, it SHOULD go in `resolvedDependencies` instead.

R-0008 (SHOULD NOT; split: R-0066, R-0067)

<!-- q L96-97 -->
> - Finally, the build process outputs one or more artifacts, identified by `subject`.

R-0068 (no keyword; C-0019)

## §3

<!-- q L103-103 "This predicate" .. "[parsing rules]." -->
> This predicate follows the in-toto attestation [parsing rules].

R-0069 (no keyword)

<!-- q L105-105 -->
> - Consumers MUST ignore unrecognized fields unless otherwise noted.

R-0009 (MUST)

<!-- q L106-107 -->
> - The `predicateType` URI includes the major version number and will always change whenever there is a backwards incompatible change.

R-0070 (no keyword; C-0020)

<!-- q L108-108 -->
> - Minor version changes are always backwards compatible and "monotonic."

R-0071 (no keyword; C-0021)

<!-- q L109-109 -->
> Such changes do not update the `predicateType`.

R-0072 (no keyword; C-0022)

<!-- q L110-110 -->
> - Unset, null, and empty field values MUST be interpreted equivalently.

R-0010 (MUST)

## §4.1

<!-- q L116-117 -->
> *NOTE: This summary (in cue) is informative. In the event of a disagreement with the text description, the text is authoritative.*

R-0073 (no keyword)

<!-- q L178-179 -->
> *NOTE: This summary (in protobuf) is informative. In the event of a disagreement with the text description, the text is authoritative.*

R-0074 (no keyword)

## §4.2

<!-- q L245-246 -->
> *NOTE: This section describes the fields within `predicate`. For a description of the other top-level fields, such as `subject`, see [Statement].*

R-0075 (no keyword)

<!-- q L250-250 -->
> REQUIRED for SLSA Build L1: `buildDefinition`, `runDetails`

R-0011 (REQUIRED)

<!-- q L255-256 -->
> <tr id="buildDefinition"><td><code>buildDefinition</code> <td><a href="#builddefinition">BuildDefinition</a><td>

R-0076 (no keyword)

<!-- q L258-258 "The input" .. "the build." -->
> The input to the build.

R-0077 (no keyword)

<!-- q L258-259 "The accuracy" .. "by `runDetails.builder.id`." -->
> The accuracy and completeness are implied by `runDetails.builder.id`.

R-0078 (no keyword)

<!-- q L261-262 -->
> <tr id="runDetails"><td><code>runDetails</code> <td><a href="#rundetails">RunDetails</a><td>

R-0079 (no keyword)

<!-- q L264-264 -->
> Details specific to this particular execution of the build.

R-0080 (no keyword)

## §4.3

<!-- q L272-272 -->
> REQUIRED for SLSA Build L1: `buildType`, `externalParameters`

R-0012 (REQUIRED)

<!-- q L277-278 -->
> <tr id="buildType"><td><code>buildType</code> <td>string (<a href="https://github.com/in-toto/attestation/blob/7aefca35a0f74a6e0cb397a8c4a76558f54de571/spec/v1/field_types.md#typeuri">TypeURI</a>)<td>

R-0081 (no keyword)

<!-- q L280-281 -->
> Identifies the template for how to perform the build and interpret the parameters and dependencies.

R-0082 (no keyword)

<!-- q L283-286 "The URI" .. "complete example." -->
> The URI SHOULD resolve to a human-readable specification that includes: overall description of the build type; schema for `externalParameters` and `internalParameters`; unambiguous instructions for how to initiate the build given this BuildDefinition, and a complete example.

R-0013 (SHOULD)

<!-- q L289-290 -->
> <tr id="externalParameters"><td><code>externalParameters</code> <td>object<td>

R-0083 (no keyword)

<!-- q L292-293 "The parameters" .. "build platform." -->
> The parameters that are under external control, such as those set by a user or tenant of the build platform.

R-0084 (no keyword)

<!-- q L293-295 "They MUST" .. "the build." -->
> They MUST be complete at SLSA Build L3, meaning that there is no additional mechanism for an external party to influence the build.

R-0014 (MUST)

<!-- q L295-295 "(At lower" .. "best effort.)" -->
> (At lower SLSA Build levels, the completeness MAY be best effort.)

R-0015 (MAY)

<!-- q L297-298 -->
> The build platform SHOULD be designed to minimize the size and complexity of `externalParameters`, in order to reduce fragility and ease [verification].

R-0016 (SHOULD)

<!-- q L299-300 -->
> Consumers SHOULD have an expectation of what "good" looks like; the more information that they need to check, the harder that task becomes.

R-0017 (SHOULD)

<!-- q L302-303 -->
> Verifiers SHOULD reject unrecognized or unexpected fields within `externalParameters`.

R-0018 (SHOULD)

<!-- q L305-306 -->
> <tr id="internalParameters"><td><code>internalParameters</code> <td>object<td>

R-0085 (no keyword)

<!-- q L308-309 "The parameters" .. "by `builder.id`." -->
> The parameters that are under the control of the entity represented by `builder.id`.

R-0086 (no keyword)

<!-- q L310-311 "The values" .. "the build." -->
> The values here MAY be necessary for reproducing the build.

R-0019 (MAY)

<!-- q L311-313 "There is" .. "do so." -->
> There is no need to [verify][Verification] these parameters because the build platform is already trusted, and in many cases it is not practical to do so.

R-0087 (no keyword; C-0025)

<!-- q L315-316 -->
> <tr id="resolvedDependencies"><td><code>resolvedDependencies</code> <td>array (<a href="https://github.com/in-toto/attestation/blob/7aefca35a0f74a6e0cb397a8c4a76558f54de571/spec/v1/resource_descriptor.md">ResourceDescriptor</a>)<td>

R-0088 (no keyword)

<!-- q L318-318 "Unordered collection" .. "build time." -->
> Unordered collection of artifacts needed at build time.

R-0089 (no keyword)

<!-- q L318-319 "Completeness is" .. "Build L3." -->
> Completeness is best effort, at least through SLSA Build L3.

R-0090 (no keyword)

<!-- q L319-322 "For example," .. "listed here." -->
> For example, if the build script fetches and executes "example.com/foo.sh", which in turn fetches "example.com/bar.tar.gz", then both "foo.sh" and "bar.tar.gz" SHOULD be listed here.

R-0020 (SHOULD)

<!-- q L326-326 "The BuildDefinition" .. "the build." -->
> The BuildDefinition describes all of the inputs to the build.

R-0091 (no keyword)

<!-- q L326-328 "It SHOULD" .. "begin execution." -->
> It SHOULD contain all the information necessary and sufficient to initialize the build and begin execution.

R-0021 (SHOULD)

<!-- q L330-331 "The `externalParameters`" .. "another input." -->
> The `externalParameters` and `internalParameters` are the top-level inputs to the template, meaning inputs not derived from another input.

R-0092 (no keyword)

<!-- q L331-333 "Each is" .. "aid verification." -->
> Each is an arbitrary JSON object, though it is RECOMMENDED to keep the structure simple with string values to aid verification.

R-0022 (RECOMMENDED; split: R-0093, R-0094)

<!-- q L333-334 "The same" .. "and `internalParameters`." -->
> The same field name SHOULD NOT be used for both `externalParameters` and `internalParameters`.

R-0023 (SHOULD NOT)

<!-- q L336-337 "The parameters" .. "build platform." -->
> The parameters SHOULD only contain the actual values passed in through the interface to the build platform.

R-0024 (SHOULD)

<!-- q L337-339 "Metadata about" .. "in `resolvedDependencies`." -->
> Metadata about those parameter values, particularly digests of artifacts referenced by those parameters, SHOULD instead go in `resolvedDependencies`.

R-0025 (SHOULD)

<!-- q L339-340 "The documentation" .. "dependency `uri`." -->
> The documentation for `buildType` SHOULD explain how to convert from a parameter to the dependency `uri`.

R-0026 (SHOULD)

<!-- q L356-357 "In particular," .. "be implicit." -->
> In particular, any value that is boilerplate and the same for every build SHOULD be implicit.

R-0027 (SHOULD)

<!-- q L365-366 "- In" .. "or priority." -->
> - In some cases, additional external parameters might exist that do not impact the behavior of the build, such as a deadline or priority.

R-0095 (no keyword; C-0029)

<!-- q L366-368 "These extra" .. "security impact." -->
> These extra parameters SHOULD be excluded from the provenance after careful analysis that they indeed pose no security impact.

R-0028 (SHOULD)

<!-- q L381-383 -->
> - (RECOMMENDED) Rearchitect the build platform to read configuration directly from version control, recording the server-verified URI in `externalParameters` and the digest in `resolvedDependencies`.

R-0029 (RECOMMENDED)

<!-- q L385-386 "- Record" .. "version control." -->
> - Record the digest in the provenance[^digest-param] and use a separate provenance attestation to link that digest back to version control.

R-0096 (no keyword; C-0033)

<!-- q L386-389 "In this" .. "untrusted workstation." -->
> In this solution, the client-side evaluation is considered a separate "build" that SHOULD be independently secured using SLSA, though securing it can be difficult since it usually runs on an untrusted workstation.

R-0030 (SHOULD)

<!-- q L393-394 "At SLSA" .. "." -->
> At SLSA Build L3, completeness is considered "best effort".

R-0097 (no keyword; C-0036)

<!-- q L396-396 "[^digest-param]: The" .. "reflect reality." -->
> [^digest-param]: The `externalParameters` SHOULD reflect reality.

R-0031 (SHOULD)

<!-- q L396-398 "If clients" .. "in `externalParameters`." -->
> If clients send the evaluated configuration object directly to the build server, record the digest directly in `externalParameters`.

R-0098 (no keyword)

<!-- q L398-401 "If clients" .. "in `resolvedDependencies`." -->
> If clients upload the configuration object to a temporary storage location and send that location to the build server, record the location in `externalParameters` as a URI and record the `uri` and `digest` in `resolvedDependencies`.

R-0099 (no keyword)

## §4.4

<!-- q L407-407 -->
> REQUIRED for SLSA Build L1: `builder`

R-0032 (REQUIRED)

<!-- q L412-413 -->
> <tr id="runDetailsBuilder"><td><code>builder</code> <td><a href="#builder">Builder</a><td>

R-0100 (no keyword)

<!-- q L415-416 -->
> Identifies the build platform that executed the invocation, which is trusted to have correctly performed the operation and populated this provenance.

R-0101 (no keyword)

<!-- q L418-419 -->
> <tr id="runDetailsMetadata"><td><code>metadata</code> <td><a href="#buildmetadata">BuildMetadata</a><td>

R-0102 (no keyword)

<!-- q L421-421 -->
> Metadata about this particular execution of the build.

R-0103 (no keyword)

<!-- q L423-424 -->
> <tr id="runDetailsByproducts"><td><code>byproducts</code> <td>array (<a href="https://github.com/in-toto/attestation/blob/7aefca35a0f74a6e0cb397a8c4a76558f54de571/spec/v1/resource_descriptor.md">ResourceDescriptor</a>)<td>

R-0104 (no keyword)

<!-- q L426-428 "Additional artifacts" .. "incident response." -->
> Additional artifacts generated during the build that are not considered the "output" of the build but that might be needed during debugging or incident response.

R-0105 (no keyword)

<!-- q L431-432 "In most" .. "the build." -->
> In most cases, this SHOULD NOT contain all intermediate files generated during the build.

R-0033 (SHOULD NOT)

<!-- q L432-433 "Instead, this" .. "easily reproduced." -->
> Instead, this SHOULD only contain files that are likely to be useful later and that cannot be easily reproduced.

R-0034 (SHOULD)

## §4.5

<!-- q L441-441 -->
> REQUIRED for SLSA Build L1: `id`

R-0035 (REQUIRED)

<!-- q L446-447 -->
> <tr id="builder.id"><td><code>id</code> <td>string (<a href="https://github.com/in-toto/attestation/blob/7aefca35a0f74a6e0cb397a8c4a76558f54de571/spec/v1/field_types.md#typeuri">TypeURI</a>)<td>

R-0106 (no keyword)

<!-- q L449-449 "URI indicating" .. "build platform." -->
> URI indicating the transitive closure of the trusted build platform.

R-0107 (no keyword)

<!-- q L449-451 "This is" .. "Build level." -->
> This is [intended](verifying-artifacts#step-1-check-slsa-build-level) to be the sole determiner of the SLSA Build level.

R-0108 (no keyword)

<!-- q L453-455 "If a" .. "signer identity." -->
> If a build platform has multiple modes of operations that have differing security attributes or SLSA Build levels, each mode MUST have a different `builder.id` and SHOULD have a different signer identity.

R-0036 (MUST; split: R-0109, R-0110)

<!-- q L458-458 -->
> The `builder.id` URI SHOULD resolve to documentation explaining:

R-0037 (SHOULD)

<!-- q L460-460 -->
> - The scope of what this ID represents.

R-0111 (no keyword; C-0037)

<!-- q L461-461 -->
> - The claimed SLSA Build level.

R-0112 (no keyword; C-0038)

<!-- q L462-462 -->
> - The accuracy and completeness guarantees of the fields in the provenance.

R-0113 (no keyword; C-0039)

<!-- q L463-464 -->
> - Any fields that are generated by the tenant-controlled build process and not verified by the trusted control plane, except for the `subject`.

R-0114 (no keyword; C-0040)

<!-- q L465-465 -->
> - The interpretation of any extension fields.

R-0115 (no keyword; C-0041)

<!-- q L467-468 -->
> <tr id="builderDependencies"><td><code>builderDependencies</code> <td>array (<a href="https://github.com/in-toto/attestation/blob/7aefca35a0f74a6e0cb397a8c4a76558f54de571/spec/v1/resource_descriptor.md">ResourceDescriptor</a>)<td>

R-0116 (no keyword)

<!-- q L470-472 -->
> Dependencies used by the orchestrator that are not run within the workload and that do not affect the build, but might affect the provenance generation or security guarantees.

R-0117 (no keyword; C-0042)

<!-- q L474-475 -->
> <tr id="builder.version"><td><code>version</code> <td>map (string→string)<td>

R-0118 (no keyword)

<!-- q L477-477 -->
> Map of names of components of the build platform to their version.

R-0119 (no keyword)

<!-- q L481-483 "The build" .. "the provenance." -->
> The build platform, or <dfn>builder</dfn> for short, represents the transitive closure of all the entities that are, by necessity, [trusted] to faithfully run the build and record the provenance.

R-0120 (no keyword)

<!-- q L483-484 "This includes" .. "the service." -->
> This includes not only the software but the hardware and people involved in running the service.

R-0121 (no keyword; C-0043)

<!-- q L489-489 "The `id`" .. "care about." -->
> The `id` MUST reflect the trust base that consumers care about.

R-0038 (MUST)

<!-- q L496-496 "Consumers MUST" .. "signer-builder pairs." -->
> Consumers MUST accept only specific signer-builder pairs.

R-0039 (MUST)

<!-- q L503-504 "The field" .. "and debugging." -->
> The field is REQUIRED, even if it is implicit from the signer, to aid readability and debugging.

R-0040 (REQUIRED)

## §4.6

<!-- q L511-511 -->
> REQUIRED: (none)

R-0041 (REQUIRED)

<!-- q L516-517 -->
> <tr id="invocationId"><td><code>invocationId</code> <td>string<td>

R-0122 (no keyword)

<!-- q L519-520 "Identifies this" .. "ad-hoc analysis." -->
> Identifies this particular build invocation, which can be useful for finding associated logs or other ad-hoc analysis.

R-0123 (no keyword; C-0046)

<!-- q L520-521 "The exact" .. "and case-sensitive." -->
> The exact meaning and format is defined by `builder.id`; by default it is treated as opaque and case-sensitive.

R-0124 (no keyword)

<!-- q L522-522 -->
> The value SHOULD be globally unique.

R-0042 (SHOULD)

<!-- q L524-525 -->
> <tr id="startedOn"><td><code>startedOn</code> <td>string (<a href="https://github.com/in-toto/attestation/blob/7aefca35a0f74a6e0cb397a8c4a76558f54de571/spec/v1/field_types.md#timestamp">Timestamp</a>)<td>

R-0125 (no keyword)

<!-- q L527-527 -->
> The timestamp of when the build started.

R-0126 (no keyword)

<!-- q L529-530 -->
> <tr id="finishedOn"><td><code>finishedOn</code> <td>string (<a href="https://github.com/in-toto/attestation/blob/7aefca35a0f74a6e0cb397a8c4a76558f54de571/spec/v1/field_types.md#timestamp">Timestamp</a>)<td>

R-0127 (no keyword)

<!-- q L532-532 -->
> The timestamp of when the build completed.

R-0128 (no keyword)

## §4.7

<!-- q L540-541 "Implementations MAY" .. "standard field." -->
> Implementations MAY add extension fields to any JSON object to describe information that is not captured in a standard field.

R-0043 (MAY)

<!-- q L543-544 "- Extension" .. "e.g. `examplebuilder_isCodeReviewed`." -->
> - Extension fields SHOULD use names of the form `<vendor>_<fieldname>`, e.g. `examplebuilder_isCodeReviewed`.

R-0044 (SHOULD)

<!-- q L545-546 "Non-extension field" .. "an underscore." -->
> Non-extension field names never contain an underscore.

R-0129 (no keyword; C-0048)

<!-- q L547-547 "- Extension" .. "other field." -->
> - Extension fields MUST NOT alter the meaning of any other field.

R-0045 (MUST NOT)

<!-- q L547-550 "In other" .. "extension field." -->
> In other words, an attestation with an absent extension field MUST be interpreted identically to an attestation with an unrecognized (and thus ignored) extension field.

R-0046 (MUST)

<!-- q L551-553 -->
> - Extension fields SHOULD follow the [monotonic principle][parsing rules], meaning that deleting or ignoring the extension SHOULD NOT turn a DENY decision into an ALLOW.

R-0047 (SHOULD; split: R-0130, R-0131)

## §7

<!-- q L576-577 "To migrate" .. "following pseudocode." -->
> To migrate from [version 0.2](/provenance/v0.2) (`old`), use the following pseudocode.

R-0132 (no keyword)

<!-- q L577-577 "The meaning" .. "otherwise noted." -->
> The meaning of each field is unchanged unless otherwise noted.

R-0133 (no keyword)

<!-- q L579-583 -->
> ```javascript { "buildDefinition": { // The `buildType` MUST be updated for v1.0 to describe how to // interpret `inputArtifacts`.

R-0048 (MUST; split: R-0134)

<!-- q L584-588 -->
> "buildType": /* updated version of */ old.buildType, "externalParameters": old.invocation.parameters + { // It is RECOMMENDED to rename "entryPoint" to something more // descriptive.

R-0049 (RECOMMENDED; split: R-0137)

<!-- q L584-584 -->
> "buildType": /* updated version of */ old.buildType,

R-0135 (no keyword)

<!-- q L585-586 -->
> "externalParameters": old.invocation.parameters + {

R-0136 (no keyword)

<!-- q L589-591 -->
> "entryPoint": old.invocation.configSource.entryPoint, // It is OPTIONAL to rename "source" to something more descriptive, // especially if "source" is ambiguous or confusing.

R-0050 (OPTIONAL; split: R-0139)

<!-- q L589-589 -->
> "entryPoint": old.invocation.configSource.entryPoint,

R-0138 (no keyword)

<!-- q L592-592 -->
> "source": old.invocation.configSource.uri,

R-0140 (no keyword)

<!-- q L594-594 -->
> "internalParameters": old.invocation.environment,

R-0141 (no keyword)

<!-- q L595-596 -->
> "resolvedDependencies": old.materials + [

R-0142 (no keyword)

<!-- q L597-600 -->
> { "uri": old.invocation.configSource.uri, "digest": old.invocation.configSource.digest, }

R-0143 (no keyword)

<!-- q L605-605 -->
> "id": old.builder.id,

R-0144 (no keyword)

<!-- q L606-606 -->
> "builderDependencies": null, // not in v0.2

R-0145 (no keyword)

<!-- q L607-607 -->
> "version": null, // not in v0.2

R-0146 (no keyword)

<!-- q L610-610 -->
> "invocationId": old.metadata.buildInvocationId,

R-0147 (no keyword)

<!-- q L611-611 -->
> "startedOn": old.metadata.buildStartedOn,

R-0148 (no keyword)

<!-- q L612-612 -->
> "finishedOn": old.metadata.buildFinishedOn,

R-0149 (no keyword)

<!-- q L614-614 -->
> "byproducts": null, // not in v0.2

R-0150 (no keyword)

<!-- q L621-621 -->
> - `entryPoint`: Use `externalParameters[<name>]` instead.

R-0151 (no keyword; C-0052)

<!-- q L622-622 "- `buildConfig`:" .. "the provenance." -->
> - `buildConfig`: No longer inlined into the provenance.

R-0152 (no keyword; C-0053)

<!-- q L623-624 -->
> - If the configuration is a top-level input, record its digest in `externalParameters["config"]`.

R-0153 (no keyword; C-0055)

<!-- q L625-626 "- Else" .. "in `byproducts`." -->
> - Else if there is a known use case for knowing the exact resolved build configuration, record its digest in `byproducts`.

R-0154 (no keyword; C-0056)

<!-- q L629-629 -->
> - Else omit it.

R-0155 (no keyword; C-0058)

<!-- q L630-630 -->
> - `metadata.completeness`: Now implicit from `builder.id`.

R-0156 (no keyword; C-0059)

<!-- q L631-631 -->
> - `metadata.reproducible`: Now implicit from `builder.id`.

R-0157 (no keyword; C-0060)

## Source defects

Defects and tensions in the source itself, each with its lines and the entries it touches; none quotes the source outside a marker. Pass 1 found them in four lanes, each numbering its own list, so one id meant up to three different defects across the artifact set. Pass 2 reconciled them into this canonical list, and every artifact now cites these ids; the crosswalk below gives each pass-1 id, so none is lost. SD-1 to SD-8 keep the requirements lane's numbers, which `requirements.yaml` cites; SD-9 to SD-14 come from the other lanes. Two entries are observations rather than defects and say so.

- **SD-1** — §1, L37 (R-0002). The page is SLSA v1.2 (its newest change-history entry is v1.2, L635), yet R-0002 calls what the predicate serves the SLSA v1.0 provenance requirements, while its relative link resolves to the Requirements page of whichever version is being read. A stale version label; read as the requirements of the SLSA version in hand.
- **SD-2** — §2 L74 against §4.3 L365-368 (R-0058, R-0028, R-0095). R-0058 has external parameter values included in the provenance (MUST); R-0028 has a class of external parameters, those with no effect on the build (R-0095), excluded (SHOULD). As written the SHOULD runs against the MUST for that class. The reconciling reading, that R-0058 covers only the build's external interface (R-0057) and a parameter with no effect on the build is not part of it, is ours; the page does not say so.
- **SD-3** — §4.3, L310 (R-0019). MAY is used in its ordinary sense, to say the values might be needed to reproduce the build, not to grant the permission RFC 2119 gives it. It binds nothing, and bin/bcp14-count counts it.
- **SD-4** — §4.7, L545-546 (R-0129) against §4.1, L127. R-0129 says no standard field name contains an underscore, but _type, the first member of the in-toto Statement, which this page's own cue summary prints at L127, has one. Nor can the rule apply to keys of the parameter objects (named by the buildType) or of the maps (digest, version, annotations), which this page does not name. A consumer that takes every underscored name for an extension field (R-0044) misreads _type and any buildType parameter spelled with an underscore. Read as covering the members §4.2 to §4.6 define.
- **SD-5** — §4.3, L302-303 (R-0018) against §4.7 (R-0043, R-0046, R-0131). Extension fields may go in any JSON object (R-0043) and an unrecognized one is ignored (R-0046), but within externalParameters a verifier rejects unrecognized fields (R-0018). An extension field placed in externalParameters is therefore rejected by a verifier that does not know it, and deleting it turns that DENY into an ALLOW, against R-0131. The page does not say whether extension fields belong in externalParameters at all.
- **SD-6** — §7, L582-583 (R-0134). The migration comment has the updated buildType describe how to interpret inputArtifacts, a name this page defines nowhere: v1 calls the dependency list resolvedDependencies, and v0.2 called it materials (L596, L651). Read as resolvedDependencies. The change history's release-candidate renames (L669-674) do not include it, so where the name comes from is not visible in this source.
- **SD-7** — §3, L110 (R-0010) with §4.3, L272 (R-0012); an interaction, left open. An empty value reads as unset (R-0010), so a build whose BuildDefinition has no external parameters cannot carry the externalParameters that R-0012 requires for SLSA Build L1: the empty object reads as missing (R-0162). The page does not say whether such a build can exist or what it should record.
- **SD-8** — §4.5, L503-504 (R-0040). R-0040 does not name the field it requires. The paragraph is about the builder, and the next sentence calls the field an object, so it is read as runDetails.builder, whose one member id R-0035 already requires.
- **SD-9** — §4.1, L124-173 against the annotations L250, L272, L407, L441, L511 (R-0073, R-0011, R-0012, R-0032, R-0035, R-0041). The cue summary draws every member with no optional marker, so read as cue it requires them all, while the text requires only the members the annotations list. The text prevails (R-0073), and the derived schema follows the annotations.
- **SD-10** — §4.1, L172 against L236-237, with the field rows L525 and L530 (R-0125, R-0127). The cue comment draws a whole-second time ending in Z; the protobuf summary types both times as google.protobuf.Timestamp, which carries fractions and whose JSON form also accepts offsets; the text names only the in-toto Timestamp type, outside this source. The derived schema accepts fraction and offset and tags those tests ambiguous.
- **SD-11** — §3, L105 (R-0009) against §4.3, L302-303 (R-0018). The parsing rule reserves exceptions it does not point to. The only one this page holds is the verifier rule inside externalParameters; R-0166 records that reading as inferred. SD-5 is what the exception does to extension fields.
- **SD-12** — §7, L585-601 (R-0136, R-0142, R-0143). The pseudocode's + is undefined and is not JavaScript's: it reads as object union on the parameters and as concatenation on the materials. A key present in both operands has no stated winner, and a v0.2 document without configSource leaves the two added parameters and the appended descriptor without values (literally, a descriptor with neither uri nor digest). `examples/reproduce.py` lets the right operand win and omits absent members; both are derived choices.
- **SD-13** — observation, not a defect. §4.1, L183-186 (R-0074). The page says its protobuf summary favours readability and that a version fit for code generation is kept in the in-toto attestation repository. The verbatim proto compiles under protoc (a scratch install of grpcio-tools, pass 1, replayed in pass 2; `schema/README.md`); that does not make it the code-generation file.
- **SD-14** — observation (scope). The annotations L250, L272, L407, L441 and §4.3, L293-295 (R-0011, R-0012, R-0032, R-0035, R-0014). Every level-qualified REQUIRED is for SLSA Build L1, and completeness at L3 is the page's only level-specific rule; what L2 and L3 add is on SLSA's Requirements page, outside this source. The derived schema is the L1 profile.

### Crosswalk from the pass-1 ids

| canonical | requirements lane (this file, `requirements.yaml`) | `messages.yaml` | `protocol.yaml`, `protocol.md`, `state-machine.yaml` | `design-notes.md` | `schema/README.md`, `examples/` |
|---|---|---|---|---|---|
| SD-1 | SD-1 | — | OI-06 | §6 (R-0002) | — |
| SD-2 | SD-2 | — | — | — | — |
| SD-3 | SD-3 | — | — | — | — |
| SD-4 | SD-4 | SD-05 | SD-03 | open question 1 | — |
| SD-5 | SD-5 | — | SD-02 | open question 1; A-01 | — |
| SD-6 | SD-6 | SD-06 | SD-01 | open question 5 | — |
| SD-7 | SD-7 | SD-02 | OI-01 | open question 2 | SD-02 |
| SD-8 | SD-8 | SD-08 | — | — | — |
| SD-9 | — | SD-01 | — | — | SD-01 |
| SD-10 | — | SD-03 | — | C-04; open question 4 | SD-03 |
| SD-11 | — (R-0166) | SD-04 | — | — | — |
| SD-12 | — | SD-07 | OI-07 | — | — |
| SD-13 | — | SD-09 | — | — | — |
| SD-14 | — | SD-10 | OI-02 | open question 3 | — |

Pass-1 `SD-0n` ids were renumbered to these in every file; the protocol's open issues (OI-n) and the design notes' open questions keep their own numbers and are listed here where they state the same defect.

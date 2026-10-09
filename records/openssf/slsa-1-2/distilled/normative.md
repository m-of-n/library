---
schema: "library-normative/v1"
id: slsa-1-2-normative
record: slsa-1-2
type: normative
updated: "2026-10-02"
coverage: "All 16 normative/technical pages of SLSA v1.2 verbatim (tracks, build track basics, terminology, build requirements, distributing provenance, verifying artifacts, assessing build platforms, source requirements, verifying source, assessing source control systems, source example controls, threats & mitigations A-I + dependency/availability/verification threats, verified properties, attestation model, build provenance predicate incl. cue/proto summary, VSA predicate). Informative pages (what's new, about, threats overview, use cases, principles, FAQ, future directions) are summarised in summary.md, not reproduced."
reviewed_by: ""
---

# SLSA v1.2 — normative content, verbatim

Source: SLSA specification v1.2 (Status: Approved), `slsa-framework/slsa` branch `releases/v1.2`
@ `ae7fc762`, rendered at https://slsa.dev/spec/v1.2/ (single page: https://slsa.dev/spec/v1.2/zonepage,
sha256 `d9e2a942…be1d052`). Text below is the release-branch Markdown, page by page in the
single-page order, with these mechanical transformations only: HTML requirement tables are shown as
`#### <Requirement>  #anchor` + body + a `Levels:` line built from the ✓ columns; `<dl class="as-table">`
term/definition rows are shown as `**Term:**`; collapsible `<details>` threat entries are shown as
`##### <title> — <level tag>`; HTML comments (including editors' to-do notes) are dropped; headings are
demoted two levels. Locators: the page file name (`build-requirements.md`) plus the heading path and anchor.

Keyword-bearing statements are numbered in `requirements.yaml` (`slsa-1-2#R-0001` … `R-0243`); each page
section below lists the R-id range extracted from it. Statements without an uppercase BCP 14 keyword
(level definitions, the threat catalogue, verification steps written as imperatives, assessment prompts)
are normative or quasi-normative content held only here.


---

## Tracks — `tracks.md`

*Locator page:* https://slsa.dev/spec/v1.2/tracks · *Requirements extracted:* none (no uppercase BCP 14 keyword on this page)

> Page description (front matter): Provides an overview of each track and links to more specific information.

SLSA is composed of [multiple tracks](about#how-slsa-works) which are each
composed of multiple levels. Each track addresses different [threats](threats)
and has its own set of requirements and patterns of use.

### Build Track

The SLSA build track describes increasing levels of trustworthiness and
completeness in a package artifact's <dfn>provenance</dfn>. Provenance describes
what entity built the artifact, what process they used, and what the inputs
were. The lowest level only requires the provenance to exist, while higher
levels provide increasing protection against tampering of the build, the
provenance, or the artifact.

The primary purpose of the build track is to enable
[verification](verifying-artifacts.md) that the artifact was built as expected.
Consumers have some way of knowing what the expected provenance should look like
for a given package and then compare each package artifact's actual provenance
to those expectations. Doing so prevents several classes of
[supply chain threats](threats.md).

Each ecosystem (for open source) or organization (for closed source) defines
exactly how this is implemented, including: means of defining expectations, what
provenance format is accepted, whether reproducible builds are used, how
provenance is distributed, when verification happens, and what happens on
failure. Guidelines for implementers can be found in the
[requirements](build-requirements.md).

-   [Terminology](terminology.md)
-   [Basics](build-track-basics.md)
-   [Requirements](build-requirements.md)
-   [Build provenance](build-provenance.md)
-   [Assessing build platforms](assessing-build-platforms.md)

### Source Track

The SLSA source track provides producers and consumers with increasing levels of
trust in the source code they produce and consume. It describes increasing
levels of trustworthiness and completeness of how a source revision was created.

The expected process for creating a new revision is determined solely by that
repository's owner (the organization) who also determines the intent of the
software in the repository and administers technical controls to enforce the
process.

Consumers can review attestations to verify whether a particular revision meets
their standards.

-   [Requirements](source-requirements.md)
-   [Source provenance](source-requirements#source-provenance-attestations)
-   [Assessing source systems](assessing-source-systems.md)
-   [Example controls](source-example-controls.md)


---

## Build: Track Basics — `build-track-basics.md`

*Locator page:* https://slsa.dev/spec/v1.2/build-track-basics · *Requirements extracted:* none (no uppercase BCP 14 keyword on this page)

> Page description (front matter): The SLSA build track is organized into a series of levels that provide increasing supply chain security guarantees. This gives you confidence that software hasn’t been tampered with and can be securely traced back to its source. This page is a descriptive overview of the SLSA build track levels, describing their intent.

| Track/Level | Requirements | Focus
| ----------- | ------------ | -----
| [Build L0] | (none) | (n/a)
| [Build L1] | Provenance showing how the package was built | Mistakes, documentation
| [Build L2] | Signed provenance, generated by a hosted build platform | Tampering after the build
| [Build L3] | Hardened build platform | Tampering during the build

> Note: The [previous version] of the specification used a single unnamed track,
> SLSA 1–4. For version 1.0, the Source aspects were removed to focus on the
> Build track. In 1.2 the [Source Track](tracks#source-track) reintroduces
> coverage of source code.

### Build L0: No guarantees

**Summary:**

No requirements---L0 represents the lack of SLSA.

**Intended for:**

Development or test builds of software that are built and run on the same
machine, such as unit tests.

**Requirements:**

n/a

**Benefits:**

n/a

### Build L1: Provenance exists

**Summary:**

Package has provenance showing how it was built. Can be used to prevent mistakes
but is trivial to bypass or forge.

**Intended for:**

Projects and organizations wanting to easily and quickly gain some benefits of
SLSA---other than tamper protection---without changing their build workflows.

**Requirements:**

-   Software Producer:
    -   Follow a consistent build process so that others can form
        expectations about what a "correct" build looks like.
    -   Run builds on a build platform that meets Build L1 requirements.
    -   Distribute provenance to consumers, preferably using a convention
        determined by the package ecosystem.
-   Build platform:
    -   Automatically generate [provenance] describing how the artifact was
        built, including: what entity built the package, what build process
        they used, and what the top-level input to the build were.

**Benefits:**

-   Makes it easier for both producers and consumers to debug, patch, rebuild,
    and/or analyze the software by knowing its precise source version and build
    process.

-   With [verification], prevents mistakes during the release process, such as
    building from a commit that is not present in the upstream repo.

-   Aids organizations in creating an inventory of software and build platforms
    used across a variety of teams.

**Notes:**

-   Provenance may be incomplete and/or unsigned at L1. Higher levels require
    more complete and trustworthy provenance.

### Build L2: Hosted build platform

**Summary:**

Forging the provenance or evading verification requires an explicit "attack",
though this may be easy to perform. Deters unsophisticated adversaries or those
who face legal or financial risk.

In practice, this means that builds run on a hosted platform that generates and
signs[^sign] the provenance.

**Intended for:**

Projects and organizations wanting to gain moderate security benefits of SLSA by
switching to a hosted build platform, while waiting for changes to the build
platform itself required by [Build L3].

**Requirements:**

All of [Build L1], plus:

-   Software producer:
    -   Run builds on a [hosted] build platform that meets Build L2
        requirements.
-   Build platform:
    -   Generate and sign[^sign] the provenance itself. This may be done
        during the original build, an after-the-fact reproducible build, or
        some equivalent system that ensures the trustworthiness of the
        provenance.
-   Consumer:
    -   Validate the authenticity of the provenance.

**Benefits:**

All of [Build L1], plus:

-   Prevents tampering after the build through digital signatures[^sign].

-   Deters adversaries who face legal or financial risk by evading security
    controls, such as employees who face risk of getting fired.

-   Reduces attack surface by limiting builds to specific build platforms that
    can be audited and hardened.

-   Allows large-scale migration of teams to supported build platforms early
    while further hardening work ([Build L3]) is done in parallel.

[^sign]: Alternate means of verifying the authenticity of the provenance are
    also acceptable.

### Build L3: Hardened builds

**Summary:**

Forging the provenance or evading verification requires exploiting a
vulnerability that is beyond the capabilities of most adversaries.

In practice, this means that builds run on a hardened build platform that offers
strong tamper protection.

**Intended for:**

Most software releases. Build L3 usually requires significant changes to
existing build platforms.

**Requirements:**

All of [Build L2], plus:

-   Software producer:
    -   Run builds on a hosted build platform that meets Build L3
        requirements.
-   Build platform:
    -   Implement strong controls to:
        -   prevent runs from influencing one another, even within the same
            project.
        -   prevent secret material used to sign the provenance from being
            accessible to the user-defined build steps.

**Benefits:**

All of [Build L2], plus:

-   Prevents tampering during the build---by insider threats, compromised
    credentials, or other tenants.

-   Greatly reduces the impact of compromised package upload credentials by
    requiring the attacker to perform a difficult exploit of the build process.

-   Provides strong confidence that the package was built from the official
    source and build process.

[build l0]: #build-l0
[build l1]: #build-l1
[build l2]: #build-l2
[build l3]: #build-l3
[future versions]: future-directions.md
[hosted]: build-requirements.md#isolation-strength
[previous version]: ../v0.1/levels.md
[provenance]: terminology.md
[verification]: verifying-artifacts.md


---

## Build: Terminology — `terminology.md`

*Locator page:* https://slsa.dev/spec/v1.2/terminology · *Requirements extracted:* none (no uppercase BCP 14 keyword on this page)

> Page description (front matter): Before diving into the SLSA specification levels, we need to establish a core set of terminology and models to describe what we're protecting.

Before diving into the [Build Track](build-track-basics.md), we need to
establish a core set of terminology and models to describe what we're
protecting.

### Software supply chain

SLSA's framework addresses every step of the software supply chain - the
sequence of steps resulting in the creation of an artifact. We represent a
supply chain as a [directed acyclic graph] of sources, builds, dependencies, and
packages. One artifact's supply chain is a combination of its dependencies'
supply chains plus its own sources and builds.

[directed acyclic graph]: https://en.wikipedia.org/wiki/Directed_acyclic_graph

![Software Supply Chain Model](images/supply-chain-model.svg)

| Term | Description | Example
| --- | --- | ---
| Artifact | An immutable blob of data; primarily refers to software, but SLSA can be used for any artifact. | A file, a git commit, a directory of files (serialized in some way), a container image, a firmware image.
| Attestation | An authenticated statement (metadata) about a software artifact or collection of software artifacts. | A signed [SLSA Provenance] file.
| Source | Artifact that was directly authored or reviewed by persons, without modification. It is the beginning of the supply chain; we do not trace the provenance back any further. | Git commit (source) hosted on GitHub (platform).
| [Build] | Process that transforms a set of input artifacts into a set of output artifacts. The inputs may be sources, dependencies, or ephemeral build outputs. | .travis.yml (process) run by Travis CI (platform).
| [Distribution] | The channel through which artifacts are "published" for use by others. | A registry like DockerHub or npm. Artifacts may also be distributed via physical media (e.g., a USB drive).
| Package | Artifact that is distributed. In the model, it is always the output of a build process, though that build process can be a no-op. | Docker image (package) distributed on DockerHub (distribution). A ZIP file containing source code is a package, not a source, because it is built from some other source, such as a git commit.
| Dependency | Artifact that is an input to a build process but that is not a source. In the model, it is always a package. | Alpine package (package) distributed on Alpine Linux (platform).

[build]: #build-model
[distribution]: #distribution-model
[SLSA Provenance]: /provenance/v1

#### Roles

Throughout the specification, you will see reference to the following roles
that take part in the software supply chain. Note that in practice a role may
be filled by more than one person or an organization. Similarly, a person or
organization may act as more than one role in a particular software supply
chain.

| Role | Description | Examples
| --- | --- | ---
| Producer | A party who creates software and provides it to others. Producers are often also consumers. | An open source project's maintainers. A software vendor.
| Verifier | A party who inspect an artifact's provenance to determine the artifact's authenticity. | A business's software ingestion system. A programming language ecosystem's package registry.
| Consumer | A party who uses software provided by a producer. The consumer may verify provenance for software they consume or delegate that responsibility to a separate verifier. | A developer who uses open source software distributions. A business that uses a point of sale system.
| Infrastructure provider | A party who provides software or services to other roles. | A package registry's maintainers. A build platform's maintainers.

#### Build model

<p align="center"><img src="images/build-model.svg" alt="Model Build"></p>

We model a build as running on a multi-tenant *build platform*, where each
execution is independent.

1.  A tenant invokes the build by specifying *external parameters* through an
    *interface*, either directly or via some trigger. Usually, at least one of
    these external parameters is a reference to a *dependency*. (External
    parameters are literal values while dependencies are artifacts.)
2.  The build platform's *control plane* interprets these external parameters,
    fetches an initial set of dependencies, initializes a *build environment*,
    and then starts the execution within that environment.
3.  The build then performs arbitrary steps, which might include fetching
    additional dependencies, and then produces one or more *output* artifacts.
    The steps within the build environment are under the tenant's control.
    The build platform isolates build environments from one another to some
    degree (which is measured by the SLSA Build Level).
4.  Finally, for SLSA Build L2+, the control plane outputs *provenance*
    describing this whole process.

Notably, there is no formal notion of "source" in the build model, just external
parameters and dependencies. Most build platforms have an explicit "source"
artifact to build from, which is often a git repository; in the build model, the
reference to this artifact is an external parameter while the artifact itself is
a dependency.

For examples of how this model applies to real-world build platforms, see [index
of build types](/provenance/v1#index-of-build-types).

| Primary Term | Description
| --- | ---
| <span id="platform">Platform</span> | System that allows tenants to run builds. Technically, it is the transitive closure of software and services that must be trusted to faithfully execute the build. It includes software, hardware, people, and organizations.
| Admin | A privileged user with administrative access to the platform, potentially allowing them to tamper with builds or the control plane.
| Tenant | An untrusted user that builds an artifact on the platform. The tenant defines the build steps and external parameters.
| Control plane | Build platform component that orchestrates each independent build execution and produces provenance. The control plane is managed by an admin and trusted to be outside the tenant's control.
| Build | Process that converts input sources and dependencies into output artifacts, defined by the tenant and executed within a single build environment on a platform.
| Steps | The set of actions that comprise a build, defined by the tenant.
| <span id="build-environment">Build environment</span> | The independent execution context in which the build runs, initialized by the control plane. In the case of a distributed build, this is the collection of all such machines/containers/VMs that run steps.
| Build caches | An intermediate artifact storage managed by the platform that maps intermediate artifacts to their explicit inputs. A build may share build caches with any subsequent build running on the platform.
| External parameters | The set of top-level, independent inputs to the build, specified by a tenant and used by the control plane to initialize the build.
| Dependencies | Artifacts fetched during initialization or execution of the build process, such as configuration files, source artifacts, or build tools.
| Outputs | Collection of artifacts produced by the build.
| <span id="provenance">Provenance</span> | Attestation (metadata) describing how the outputs were produced, including identification of the platform and external parameters.

###### Ambiguous terms to avoid

-   *Build recipe:* Could mean *external parameters,* but may include concrete
    steps of how to perform a build. To avoid implementation details, we don't
    define this term, but always use "external parameters" which is the
    interface to a build platform. Similar terms are *build configuration
    source* and *build definition*.
-   *Builder:* Usually means *build platform*, but might be used for *build
    environment*, the user who invoked the build, or a build tool from
    *dependencies*. To avoid confusion, we always use "build platform". The only
    exception is in the [provenance](/provenance/v1), where `builder` is used as
    a more concise field name.

#### Distribution model

Software is distributed in identifiable units called <dfn>packages</dfn>
according to the rules and conventions of a <dfn>package ecosystem</dfn>.
Examples of formal ecosystems include [Python/PyPA](https://www.pypa.io),
[Debian/Apt](https://wiki.debian.org/DebianRepository/Format), and
[OCI](https://github.com/opencontainers/distribution-spec), while examples of
informal ecosystems include links to files on a website or distribution of
first-party software within a company.

Abstractly, a consumer locates software within an ecosystem by asking a
<dfn>distribution platform</dfn>, such as a package registry, to resolve a
mutable <dfn>package name</dfn> into an immutable <dfn>package artifact</dfn>.
[^label] To <dfn>publish</dfn> a package artifact, the software producer asks
the registry to update this mapping to resolve to the new artifact. The registry
represents the entity or entities with the power to alter what artifacts are
accepted by consumers for a given package name. For example, if consumers only
accept packages signed by a particular public key, then it is access to that
public key that serves as the registry.

The package name is the primary security boundary within a package ecosystem.
Different package names represent materially different pieces of
software---different owners, behaviors, security properties, and so on.
Therefore, **the package name is the primary unit being protected in SLSA**.
It is the primary identifier to which consumers attach expectations.

[^label]: This resolution might include a version number, label, or some other
    selector in addition to the package name, but that is not important to SLSA.

| Term | Description
| ---- | -----------
| Distribution platform | An entity responsible for mapping package names to immutable package artifacts.
| Package | An identifiable unit of software intended for distribution, ambiguously meaning either an "artifact" or a "package name". Only use this term when the ambiguity is acceptable or desirable.
| Package artifact | A file or other immutable object that is intended for distribution.
| Package ecosystem | A set of rules and conventions governing how packages are distributed, including how clients resolve a package name into one or more specific artifacts.
| Package manager client | Client-side tooling to interact with a package ecosystem.
| Package name | <p>The primary identifier for a mutable collection of artifacts that all represent different versions of the same software. This is the primary identifier that consumers use to obtain the software.<p>A package name is specific to an ecosystem + registry, has a maintainer, is more general than a specific hash or version, and has a "correct" source location. A package ecosystem may group package names into some sort of hierarchy, such as the Group ID in Maven, though SLSA does not have a special term for this.
| Package registry | A specific type of "distribution platform" used within a packaging ecosystem. Most ecosystems support multiple registries, usually a single global registry and multiple private registries.
| Publish [a package] | Make an artifact available for use by registering it with the package registry. In technical terms, this means associating an artifact to a package name. This does not necessarily mean making the artifact fully public; an artifact may be published for only a subset of users, such as internal testing or a closed beta.

###### Ambiguous terms to avoid

-   *Package repository:* Could mean either package registry or package name,
    depending on the ecosystem. To avoid confusion, we always use "repository"
    exclusively to mean "source repository", where there is no ambiguity.
-   *Package manager* (without "client"): Could mean either package ecosystem,
    package registry, or client-side tooling.

#### Mapping to real-world ecosystems

Most real-world ecosystems fit the package model above but use different terms.
The table below attempts to document how various ecosystems map to the SLSA
Package model. There are likely mistakes and omissions; corrections and
additions are welcome!

*(HTML table rendered as a pipe table; rowspan/colspan cells appear once, in their first row)*

| Package ecosystem | Package registry | Package name | Package artifact |
|---|---|---|---|
| Languages |
| Cargo (Rust) | Registry | Crate name | Artifact |
| CPAN (Perl) | PAUSE | Distribution | Release (or Distribution) |
| Go | Module proxy | Module path | Module |
| Maven (Java) | Repository | Group ID + Artifact ID | Artifact |
| npm (JavaScript) | Registry | Package Name | Package |
| NuGet (C#) | Host | Project | Package |
| PyPA (Python) | Index | Project Name | Distribution |
| Operating systems |
| Dpkg (e.g. Debian) | ? | Package name | Package |
| Flatpak | Repository | Application | Bundle |
| Homebrew (e.g. Mac) | Repository (Tap) | Package name (Formula) | Binary package (Bottle) |
| Pacman (e.g. Arch) | Repository | Package name | Package |
| RPM (e.g. Red Hat) | Repository | Package name | Package |
| Nix (e.g. NixOS) | Repository (e.g. Nixpkgs) or binary cache | Derivation name | Derivation or store object |
| Storage systems |
| GCS | n/a | Object name | Object |
| OCI/Docker | Registry | Repository | Object |
| Meta |
| deps.dev: System | Packaging authority | Package | n/a |
| purl: type | Namespace | Name | n/a |

Notes:

-   Go uses a significantly different distribution model than other ecosystems.
    In Go, the package name is a source repository URL. While clients can fetch
    directly from that URL---in which case there is no "package" or
    "registry"---they usually fetch a zip file from a *module proxy*. The module
    proxy acts as both a builder (by constructing the package artifact from
    source) and a registry (by mapping package name to package artifact). People
    trust the module proxy because builds are independently reproducible, and a
    *checksum database* guarantees that all clients receive the same artifact
    for a given URL.

#### Verification model

Verification in SLSA is performed in two ways. Firstly, the build platform is
certified to ensure conformance with the requirements at the level claimed by
the build platform. This certification should happen on a recurring cadence, with
the outcomes published by the platform operator for their users to review and
make informed decisions about which builders to trust.

Secondly, artifacts are verified to ensure they meet the producer-defined
expectations of where the package source code was retrieved from and on what
build platform the package was built.

![Verification Model](images/verification-model.svg)

| Term | Description
| ---- | ----
| Expectations | A set of constraints on the package's provenance metadata. The package producer sets expectations for a package, whether explicitly or implicitly.
| Provenance verification | Artifacts are verified by the package ecosystem to ensure that the package's expectations are met before the package is used.
| Build platform assessment | [Build platforms are assessed](assessing-build-platforms.md) for their ability to meet SLSA requirements at the stated level.

The examples below suggest some ways that expectations and verification may be
implemented for different, broadly defined, package ecosystems.

###### Example: Small software team

| Term | Example
| ---- | -------
| Expectations | Defined by the producer's security personnel and stored in a database.
| Provenance verification | Performed automatically on cluster nodes before execution by querying the expectations database.
| Build platform assessment | The build platform implementer follows secure design and development best practices, does annual penetration testing exercises, and self-certifies their adherence to SLSA requirements.

###### Example: Open source language distribution

| Term | Example
| ---- | -------
| Expectations | Defined separately for each package and stored in the package registry.
| Provenance verification | The language distribution registry verifies newly uploaded packages meet expectations before publishing them. Further, the package manager client also verifies expectations prior to installing packages.
| Build platform assessment | Performed by the language ecosystem packaging authority.


---

## Build: Requirements for producing artifacts — `build-requirements.md`

*Locator page:* https://slsa.dev/spec/v1.2/build-requirements · *Requirements extracted:* R-0001 – R-0043 (43 statements)

> Page description (front matter): This page covers the detailed technical requirements for producing artifacts at each SLSA level. The intended audience is platform implementers and security engineers.

This page covers the detailed technical requirements for producing artifacts at
each SLSA level. The intended audience is platform implementers and security
engineers.

For an informative description of the levels intended for all audiences, see
[Build Track Basics](build-track-basics.md). For background, see
[Terminology](terminology.md). To better understand the reasoning behind the
requirements, see [Threats and mitigations](threats.md).

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD",
"SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be
interpreted as described in [RFC 2119](https://www.rfc-editor.org/rfc/rfc2119).

### Overview

#### Build levels

In order to produce artifacts with a specific build level, responsibility is
split between the [Producer] and [Build platform]. The build platform MUST
strengthen the security controls in order to achieve a specific level while the
producer MUST choose and adopt a build platform capable of achieving a desired
build level, implementing any controls as specified by the chosen platform.

*(HTML table rendered as a pipe table; rowspan/colspan cells appear once, in their first row)*

| Implementer | Requirement | Degree | L1 | L2 | L3 |
|---|---|---|---|---|---|
| Producer | Choose an appropriate build platform | ✓ | ✓ | ✓ |
| Follow a consistent build process | ✓ | ✓ | ✓ |
| Distribute provenance | ✓ | ✓ | ✓ |
| Build platform | Provenance generation | Exists | ✓ | ✓ | ✓ |
| Authentic |  | ✓ | ✓ |
| Unforgeable |  |  | ✓ |
| Isolation strength | Hosted |  | ✓ | ✓ |
| Isolated |  |  | ✓ |

#### Security Best Practices

While the exact definition of what constitutes a secure platform is beyond the
scope of this specification, all implementations MUST use industry security
best practices to be conformant to this specification. This includes, but is
not limited to, using proper access controls, securing communications,
implementing proper management of cryptographic secrets, doing frequent updates,
and promptly fixing known vulnerabilities.

Various relevant standards and guides can be consulted for that matter such as
the [CIS Critical Security
Controls](https://www.cisecurity.org/controls/cis-controls-list).

### Producer

[Producer]: #producer

A package's <dfn>producer</dfn> is the organization that owns and releases the
software. It might be an open-source project, a company, a team within a
company, or even an individual.

NOTE: There were more requirements for producers in the initial
[draft version (v0.1)](../v0.1/requirements.md#scripted-build) which impacted
how a package can be built. These were removed in the v1.0 specification and
will be reassessed and re-added as indicated in the
[future directions](future-directions.md).

#### Choose an appropriate build platform

The producer MUST select a build platform that is capable of reaching their
desired SLSA Build Level.

For example, if a producer wishes to produce a Build Level 3 artifact, they MUST
choose a builder capable of producing Build Level 3 provenance.

#### Follow a consistent build process

The producer MUST build their artifact in a consistent
manner such that verifiers can form expectations about the build process. In
some implementations, the producer MAY provide explicit metadata to a verifier
about their build process. In others, the verifier will form their expectations
implicitly (e.g. trust on first use).

If a producer wishes to distribute their artifact through a [package ecosystem]
that requires explicit metadata about the build process in the form of a
configuration file, the producer MUST complete the configuration file and keep
it up to date. This metadata might include information related to the artifact's
source repository and build parameters.

#### Distribute provenance

The producer MUST distribute provenance to artifact consumers. The producer
MAY delegate this responsibility to the
[package ecosystem], provided that the package ecosystem is capable of
distributing provenance.

### Build Platform

[Build platform]: #build-platform

A package's <dfn>build platform</dfn> is the infrastructure used to transform the
software from source to package. This includes the transitive closure of all
hardware, software, persons, and organizations that can influence the build. A
build platform is often a hosted, multi-tenant build service, but it could be a
system of multiple independent rebuilders, a special-purpose build platform used
by a single software project, or even an individual's workstation. Ideally, one
build platform is used by many different software packages so that consumers can
[minimize the number of trusted platforms](principles.md). For more background,
see [Build Model](terminology.md#build-model).

The build platform is responsible for providing two things: [provenance
generation] and [isolation between builds]. The
[Build level](build-track-basics) describes the degree to which each of these
properties is met.

#### Provenance generation

[Provenance generation]: #provenance-generation

The build platform is responsible for generating provenance describing how the
package was produced.

The SLSA Build level describes the overall provenance integrity according to
minimum requirements on its:

-   *Completeness:* What information is contained in the provenance?
-   *Authenticity:* How strongly can the provenance be tied back to the builder?
-   *Accuracy:* How resistant is the provenance generation to tampering within
    the build process?

*Table — columns: Requirement, Description, L1, L2, L3*

##### Provenance Exists  `#provenance-exists`

The build process MUST generate provenance that unambiguously identifies the
output package by cryptographic digest and describes how that package was
produced. The format MUST be acceptable to the [package ecosystem] and/or
[consumer](verifying-artifacts.md#consumer).

It is RECOMMENDED to use the [SLSA Provenance] format and [associated suite]
because it is designed to be interoperable, universal, and unambiguous when
used for SLSA. See that format's documentation for requirements and
implementation guidelines.

If using an alternate format, it MUST contain the equivalent information as SLSA
Provenance at each level and SHOULD be bi-directionally translatable to SLSA
Provenance.

-   *Completeness:* Best effort. The provenance at L1 SHOULD contain sufficient
    information to catch mistakes and simulate the user experience at higher
    levels in the absence of tampering. In other words, the contents of the
    provenance SHOULD be the same at all Build levels, but a few fields MAY be
    absent at L1 if they are prohibitively expensive to implement.
-   *Authenticity:* No requirements.
-   *Accuracy:* No requirements.

[SLSA Provenance]: provenance.md
[associated suite]: attestation-model#recommended-suite

Levels: L1 ✓ · L2 ✓ · L3 ✓

##### Provenance is Authentic  `#provenance-authentic`

*Authenticity:* Consumers MUST be able to validate the authenticity of the
provenance attestation in order to:

-   *Ensure integrity:* Verify that the digital signature of the provenance
    attestation is valid and the provenance was not tampered with after the
    build.
-   *Define trust:* Identify the build platform and other entities that are
    necessary to trust in order to trust the artifact they produced.

This SHOULD be through a digital signature from a private key accessible only
to the build platform component that generated the provenance attestation.

While many constraints affect choice of signing methodologies, it is
RECOMMENDED that build platforms use signing methodologies which improve the
ability to detect and remediate key compromise, such as methods which rely on
transparency logs or, when transparency isn't appropriate, time stamping
services.

Authenticity allows the consumer to trust the contents of the provenance
attestation, such as the identity of the build platform.

*Accuracy:* The provenance MUST be generated by the control plane (i.e. within
the trust boundary [identified in the provenance]) and not by a tenant of the
build platform (i.e. outside the trust boundary), except as noted below.

-   The data in the provenance MUST be obtained from the build platform, either
    because the generator *is* the build platform or because the provenance
    generator reads the data directly from the build platform.
-   The build platform MUST have some security control to prevent tenants from
    tampering with the provenance. However, there is no minimum bound on the
    strength. The purpose is to deter adversaries who might face legal or
    financial risk from evading controls.
-   Exceptions for fields that MAY be generated by a tenant of the build platform:
    -   The names and cryptographic digests of the output artifacts, i.e.
        `subject` in [SLSA Provenance]. See [forge output digest of the
        provenance](threats#forged-digest) for explanation of why this is
        acceptable.
    -   Any field that is not marked as REQUIRED for Build L2. For example,
        `resolvedDependencies` in [SLSA Provenance] MAY be tenant-generated at
        Build L2. Builders SHOULD document any such cases of tenant-generated
        fields.

*Completeness:* SHOULD be complete.

-   There MAY be [external parameters] that are not sufficiently captured in
    the provenance.
-   Completeness of resolved dependencies is best effort.

Levels: L1 — · L2 ✓ · L3 ✓

##### Provenance is Unforgeable  `#provenance-unforgeable`

*Accuracy:* Provenance MUST be strongly resistant to forgery by tenants.

-   Any secret material used for authenticating the provenance, for example the
    signing key used to generate a digital signature, MUST be stored in a secure
    management system appropriate for such material and accessible only to the
    build service account.
-   Such secret material MUST NOT be accessible to the environment running
    the user-defined build steps.
-   Every field in the provenance MUST be generated or verified by the build
    platform in a trusted control plane. The user-controlled build steps MUST
    NOT be able to inject or alter the contents, except as noted in [Provenance
    is Authentic](#provenance-authentic). (Build L3 does not require additional
    fields beyond those of L2.)

*Completeness:* SHOULD be complete.

-   [External parameters] MUST be fully enumerated.
-   Completeness of resolved dependencies is best effort.

Note: This requirement was called "non-falsifiable" in the initial
[draft version (v0.1)](../v0.1/requirements.md#non-falsifiable).

Levels: L1 — · L2 — · L3 ✓

#### Isolation strength

[Isolation strength]: #isolation-strength
[Isolation between builds]: #isolation-strength

The build platform is responsible for isolating between builds, even within the
same tenant project. In other words, how strong of a guarantee do we have that
the build really executed correctly, without external influence?

The SLSA Build level describes the minimum bar for isolation strength. For more
information on assessing a build platform's isolation strength, see
[Assessing build platforms](assessing-build-platforms.md).

*Table — columns: Requirement, Description, L1, L2, L3*

##### Hosted  `#hosted`

All build steps ran using a hosted build platform on shared or dedicated
infrastructure, not on an individual's workstation.

Examples: GitHub Actions, Google Cloud Build, Travis CI.

Levels: L1 — · L2 ✓ · L3 ✓

##### Isolated  `#isolated`

The build platform ensured that the build steps ran in an isolated environment,
free of unintended external influence. In other words, any external influence on
the build was specifically requested by the build itself. This MUST hold true
even between builds within the same tenant project.

The build platform MUST guarantee the following:

-   It MUST NOT be possible for a build to access any secrets of the build
    platform, such as the provenance signing key, because doing so would
    compromise the authenticity of the provenance.
-   It MUST NOT be possible for two builds that overlap in time to influence one
    another, such as by altering the memory of a different build process running
    on the same machine.
-   It MUST NOT be possible for one build to persist or influence the build
    environment of a subsequent build. In other words, an ephemeral build
    environment MUST be provisioned for each build.
-   It MUST NOT be possible for one build to inject false entries into a build
    cache used by another build, also known as "cache poisoning". In other
    words, the output of the build MUST be identical whether or not the cache is
    used.
-   The build platform MUST NOT open services that allow for remote influence
    unless all such interactions are captured as `externalParameters` in the
    provenance.

There are no sub-requirements on the build itself. Build L3 is limited to
ensuring that a well-intentioned build runs securely. It does not require that
a build platform prevents a producer from performing a risky or insecure build. In
particular, the "Isolated" requirement does not prohibit a build from calling
out to a remote execution service or a "self-hosted runner" that is outside the
trust boundary of the build platform.

NOTE: This requirement was split into "Isolated" and "Ephemeral Environment"
in the initial [draft version (v0.1)](../v0.1/requirements.md).

NOTE: This requirement is not to be confused with "Hermetic", which roughly
means that the build ran with no network access. Such a requirement requires
substantial changes to both the build platform and each individual build, and is
considered in the [future directions](future-directions.md).

Levels: L1 — · L2 — · L3 ✓

[external parameters]: provenance.md#externalParameters
[identified in the provenance]: provenance.md#model
[package ecosystem]: verifying-artifacts.md#package-ecosystem


---

## Build: Distributing provenance — `distributing-provenance.md`

*Locator page:* https://slsa.dev/spec/v1.2/distributing-provenance · *Requirements extracted:* R-0044 – R-0057 (14 statements)

> Page description (front matter): This page covers the detailed technical requirements for distributing provenance at each SLSA level. The intended audience is platform implementers and software distributors.

In order to make provenance for artifacts available after generation
for verification, SLSA requires the distribution and verification of provenance
metadata in the form of SLSA attestations.

This document provides specifications for distributing provenance and the
relationship between build artifacts and provenance (build attestations). It is
primarily concerned with artifacts for ecosystems that distribute build
artifacts, but some attention is also paid to ecosystems that distribute
container images or only distribute source artifacts, as many of the same
principles generally apply to any artifact or group of artifacts.

In addition, this document is primarily for the benefit of artifact
distributors, to understand how they can adopt the distribution of SLSA
provenance. It is primarily concerned with the means of distributing
attestations and the relationship of attestations to build artifacts, and not
with the specific format of the attestation itself.

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD",
"SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be
interpreted as described in [RFC 2119](https://www.rfc-editor.org/rfc/rfc2119).

### Background

The [package ecosystem]'s maintainers are responsible for reliably
redistributing artifacts and provenance, making the producers' expectations
available to consumers, and providing tools to enable safe artifact consumption
(e.g., whether an artifact meets its producer's expectations).

### Relationship between releases and attestations

Attestations SHOULD be bound to artifacts, not releases.

A single "release" of a project, package, or library might include multiple
artifacts. These artifacts result from builds on different platforms,
architectures, or environments. The builds need not happen at roughly the same
point in time and might even span multiple days.

It is often difficult or impossible to determine when a release is 'finished'
because many ecosystems allow adding new artifacts to old releases when adding
support for new platforms or architectures. Therefore, the set of attestations
for a given release MAY grow over time as additional builds and attestations
are created.

Thus, package ecosystems SHOULD support multiple individual attestations per
release. At the time of a given build, the relevant provenance for that build
can be added to the release, depending on the relationship to the given
artifacts.

### Relationship between artifacts and attestations

Package ecosystems SHOULD support a one-to-many relationship from build
artifacts to attestations to ensure that anyone is free to produce and publish
any attestation they might need. However, while there are lots of possible
attestations that can have a relationship to a given artifact, in this context
SLSA is primarily concerned with build attestations, i.e., provenance, and as
such, this specification only considers build attestations, produced by the
same maintainers as the artifacts themselves.

By providing provenance alongside an artifact in the manner specified by a
given ecosystem, maintainers are considered to be 'elevating' these build
attestations above all other possible attestations that could be provided by
third parties for a given artifact. The ultimate goal is for maintainers to
provide the provenance necessary for a repository to be able to verify some
potential policy that requires a certain SLSA level for publication, not
support the publication of arbitrary attestations by third parties.

As a result, this provenance SHOULD accompany the artifact at publish time, and
package ecosystems SHOULD provide a way to map a given artifact to its
corresponding attestations. The mappings can be either implicit (e.g., require a
custom filename schema that uniquely identifies the provenance over other
attestation types) or explicit (e.g., it could happen as a de-facto standard
based on where the attestation is published).

The provenance SHOULD have a filename that is directly related to the build
artifact filename. For example, for an artifact `<filename>.<extension>`, the
attestation is `<filename>.attestation` or some similar extension (for example
[in-toto](https://in-toto.io/) recommends `<filename>.intoto.jsonl`).

### Where attestations are published

There are a number of opportunities and venues to publish attestations during
and after the build process. Producers MUST publish attestations in at least
one place, and SHOULD publish attestations in more than one place:

-   **Publish attestations alongside the source repository releases**: If the
    source repository hosting provider offers an artifact "release" feature,
    such as [GitHub
    releases](https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases)
    or [GitLab releases](https://docs.gitlab.com/ee/user/project/releases/),
    producers SHOULD include provenance as part of such releases. This option
    has the benefit of requiring no changes to the package registry to support
    provenance formats, but has the disadvantage of putting the source
    repository hosting provider in the critical path for installers that want to
    verify policy at build-time.
-   **Publish attestations alongside the artifact in the package registry**:
    Many software repositories already support some variety of publishing 1:1
    related files alongside an artifact, sometimes known as “sidecar files”.
    For example, PyPI supports publishing `.asc` files representing the PGP
    signature for an artifact with the same filename (but different extension).
    This option requires the mapping between artifact and attestation (or
    attestation vessel) to be 1:1.
-   **Publish attestations elsewhere, record their existence in a transparency
    log**: Once an attestation has been generated and published for a build, a
    hash of the attestation and a pointer to where it is indexed SHOULD be
    published to a third-party transparency log that exists outside the source
    repository and package registry. Not only are transparency logs such as
    [Rekor from Sigstore](https://github.com/sigstore/rekor) guaranteed
    to be immutable, but they typically also make monitoring easier.
    Requiring the presence of the attestation in a monitored transparency log
    during verification helps ensure the attestation is trustworthy.

Combining these options gives us a process for bootstrapping SLSA adoption
within an ecosystem, even if the package registry doesn't support publishing
attestations. First, interested projects modify their release process to
produce SLSA provenance. Then, they publish that provenance to their source
repository. Finally, they publish the provenance to the package registry, if
and when the registry supports it.

Long-term, package registries SHOULD support uploading and distributing
provenance alongside the artifact. This model is preferred for two reasons:

-   trust: clients already trust the package registry as the source of their
    artifacts, and don't need to trust an additional service;
-   reliability: clients already depend on the package registry as part of
    their critical path, so distributing provenance via the registry avoids
    adding an additional point of failure.

Short term, consumers of build artifacts can bootstrap a manual policy by using
the source repository only for projects that publish all artifacts and
attestations to the source repository, and later extend this to all artifacts
published to the package registry via the canonical installation tools once
a given ecosystem supports them.

### Immutability of attestations

Attestations SHOULD be immutable. Once an attestation is published as it
corresponds to a given artifact, that attestation is immutable and cannot be
overwritten later with a different attestation that refers to the same
artifact. Instead, a new release (and new artifacts) SHOULD be created.

### Format of the attestation

The provenance is available to the consumer in a format that the consumer
accepts. The format SHOULD be in-toto
[SLSA Build Provenance](build-provenance), but another format MAY be used if
both producer and consumer agree and it meets all the other requirements.

### Considerations for source-based ecosystems

Some ecosystems have support for installing directly from source repositories
(an option for Python/`pip`, Go, etc.). In these cases, there is no need to
publish or verify provenance because there is no "build" step that translates
between a source repository and an artifact that is being installed.

However, for ecosystems that install from source repositories _via_ some
intermediary (e.g., [Homebrew installing from GitHub release artifacts generated
from the repository or GitHub Packages](https://docs.brew.sh/Bottles), [Go
installing through the Go module proxy](https://proxy.golang.org/)), these
ecosystems distribute "source archives" that are not the bit-for-bit identical
form from version control. These intermediaries are transforming the original
source repository in some way that constitutes a "build" and as a result SHOULD
be providing build provenance for this "package", and the recommendations
outlined here apply.

[package ecosystem]: verifying-artifacts.md#package-ecosystem


---

## Build: Verifying artifacts — `verifying-artifacts.md`

*Locator page:* https://slsa.dev/spec/v1.2/verifying-artifacts · *Requirements extracted:* R-0058 – R-0070 (13 statements)

> Page description (front matter): SLSA uses provenance to indicate whether an artifact is authentic or not, but provenance doesn't do anything unless somebody inspects it. SLSA calls that inspection verification, and this page describes how to verify artifacts and their SLSA provenance. The intended audience is platform implementers, security engineers, and software consumers.

SLSA uses provenance to indicate whether an artifact is authentic or not, but
provenance doesn't do anything unless somebody inspects it. SLSA calls that
inspection **verification**, and this page describes recommendations for how to
verify artifacts and their SLSA provenance.

This page is divided into several sections. The first describes the process
for verifying an artifact and its provenance against a set of expectations. The
second describes how to form the expectations used to verify provenance. The
third discusses architecture choices for where provenance verification can
happen.

### How to verify

Verification SHOULD include the following steps:

-   Ensuring that the builder identity is one of those in the map of trusted
    builder id's to SLSA level.
-   Verifying the signature on the provenance envelope.
-   Ensuring that the values for `buildType` and `externalParameters` in the
    provenance match the expected values. The package ecosystem MAY allow
    an approved list of `externalParameters` to be ignored during verification.
    Any unrecognized `externalParameters` SHOULD cause verification to fail.

![Threats covered by each step](images/supply-chain-threats-build-verification.svg)

See [Terminology](terminology.md) for an explanation of the supply chain model and
[Threats & mitigations](threats.md) for a detailed explanation of each threat.

**Note:** This section assumes that the provenance is in the recommended
[provenance format](/provenance/v1). If it is not, then the verifier SHOULD
perform equivalent checks on provenance fields that correspond to the ones
referenced here.

#### Step 1: Check SLSA Build level

[Step 1]: #step-1-check-slsa-build-level

First, check the SLSA Build level by comparing the artifact to its provenance
and the provenance to a preconfigured root of trust. The goal is to ensure that
the provenance actually applies to the artifact in question and to assess the
trustworthiness of the provenance. This mitigates some or all of [threats] "E",
"F", "G", and "H", depending on SLSA Build level and where verification happens.

Once, when bootstrapping the verifier:

-   Configure the verifier's roots of trust, meaning the recognized builder
    identities and the maximum SLSA Build level each builder is trusted up to.
    Different verifiers might use different roots of trust, but usually a
    verifier uses the same roots of trust for all packages. This configuration
    is likely in the form of a map from (builder public key identity,
    `builder.id`) to (SLSA Build level).

    <details>
    <summary>Example root of trust configuration</summary>

    The following snippet shows conceptually how a verifier's roots of trust
    might be configured using made-up syntax.

    ```jsonc
    "slsaRootsOfTrust": [
        // A builder trusted at SLSA Build L3, using a fixed public key.
        {
            "publicKey": "HKJEwI...",
            "builderId": "https://somebuilder.example.com/slsa/l3",
            "slsaBuildLevel": 3
        },
        // A different builder that claims to be SLSA Build L3,
        // but this verifier only trusts it to L2.
        {
            "publicKey": "tLykq9...",
            "builderId": "https://differentbuilder.example.com/slsa/l3",
            "slsaBuildLevel": 2
        },
        // A builder that uses Sigstore for authentication.
        {
            "sigstore": {
                "root": "global",  // identifies fulcio/rekor roots
                "subjectAlternativeNamePattern": "https://github.com/slsa-framework/slsa-github-generator/.github/workflows/generator_generic_slsa3.yml@refs/tags/v*.*.*"
            }
            "builderId": "https://github.com/slsa-framework/slsa-github-generator/.github/workflows/generator_generic_slsa3.yml@refs/tags/v*.*.*",
            "slsaBuildLevel": 3,
        }
        ...
    ],
    ```

    

Given an artifact and its provenance:

1.  [Verify][validation-model] the envelope's signature using the roots of
    trust, resulting in a list of recognized public keys (or equivalent).
2.  [Verify][validation-model] that statement's `subject` matches the digest of
    the artifact in question.
3.  Verify that the `predicateType` is `https://slsa.dev/provenance/v1`.
4.  Look up the SLSA Build Level in the roots of trust, using the recognized
    public keys and the `builder.id`, defaulting to SLSA Build L1.

Resulting threat mitigation:

-   [Threat "E"]: SLSA Build L3 requires protection against compromise of the
    build process and provenance generation by an external adversary, such as
    persistence between builds or theft of the provenance signing key. In other
    words, SLSA Build L3 establishes that the provenance is accurate and
    trustworthy, assuming you trust the build platform.
    -   IMPORTANT: SLSA Build L3 does **not** cover compromise of the build
        platform itself, such as by a malicious insider. Instead, verifiers
        SHOULD carefully consider which build platforms are added to the roots
        of trust. For advice on establishing trust in build platforms, see
        [Assessing build platforms](assessing-build-platforms.md).
-   [Threat "F"]: SLSA Build L2 covers tampering of the artifact or provenance
    after the build. This is accomplished by verifying the `subject` and
    signature in the steps above.
-   [Threat "G"]: Verification by the consumer or otherwise outside of the
    package registry covers compromise of the registry itself. (Verifying within
    the registry at publication time is also valuable, but does not cover Threat
    "G" or "I".)
-   [Threat "I"]: Verification by the consumer covers compromise of the package
    in transit. (Many ecosystems also address this threat using package
    signatures or checksums.)
    -   NOTE: SLSA does not yet cover adversaries tricking a consumer to use an
        unintended package, such as through typosquatting. Those threats are
        discussed in more detail under [Threat "H"].

[Threat "E"]: threats#e-build-process
[Threat "F"]: threats#f-artifact-publication
[Threat "G"]: threats#g-distribution-channel
[Threat "H"]: threats#h-package-selection
[Threat "I"]: threats#i-usage

[validation-model]: https://github.com/in-toto/attestation/blob/main/docs/validation.md#validation-model

#### Step 2: Check expectations

[verify-step-2]: #check-expectations

Next, check that the package's provenance meets your expectations for that
package in order to mitigate [threat "D"].

In our threat model, the adversary has the ability to invoke a build and to publish
to the registry. The adversary is not able to write to the source repository, nor do
they have insider access to any trusted systems. Your expectations SHOULD be
sufficient to detect or prevent this adversary from injecting unofficial
behavior into the package.

You SHOULD compare the provenance against expected values for at least the
following fields:

| What | Why
| ---- | ---
| Builder identity from [Step 1] | To prevent an adversary from building the correct code on an unintended platform
| Canonical source repository | To prevent an adversary from building from an unofficial fork (or other disallowed source)
| `buildType` | To ensure that `externalParameters` are interpreted as intended
| `externalParameters` | To prevent an adversary from injecting unofficial behavior

Verification tools SHOULD reject unrecognized fields in `externalParameters` to
err on the side of caution. It is acceptable to allow a parameter to have a
range of values (possibly any value) if it is known that any value in the range
is safe. JSON comparison is sufficient for verifying parameters.

TIP: Difficulty in forming meaningful expectations about `externalParameters` can
be a sign that the `buildType`'s level of abstraction is too low. For example,
`externalParameters` that record a list of commands to run is likely impractical
to verify because the commands change on every build. Instead, consider a
`buildType` that defines the list of commands in a configuration file in a
source repository, then put only the source repository in
`externalParameters`. Such a design is easier to verify because the source
repository is constant across builds.

[Threat "D"]: threats#d-external-build-parameters

#### Step 3: (Optional) Check dependencies recursively

[verify-step-3]: #step-3-optional-check-dependencies-recursively

Finally, recursively check the `resolvedDependencies` as available and to the
extent desired. Note that SLSA v1.0 does not have any requirements on the
completeness or verification of `resolvedDependencies`. However, one might wish
to verify dependencies in order to mitigate [dependency threats] and protect against
threats further up the supply chain. If `resolvedDependencies` is incomplete,
these checks can be done on a best-effort basis.

A [Verification Summary Attestation (VSA)][VSA] can make dependency verification
more efficient by recording the result of prior verifications. A trimming
heuristic or exception mechanism is almost always necessary when verifying
dependencies because there will be transitive dependencies that are SLSA Build
L0. (For example, consider the compiler's compiler's compiler's ... compiler.)

[dependency threats]: threats#dependency-threats
[VSA]: /verification_summary
[threats]: threats

### Forming Expectations

<dfn>Expectations</dfn> are known provenance values that indicate the
corresponding artifact is authentic. For example, a package ecosystem may
maintain a mapping between package names and their canonical source
repositories. That mapping constitutes a set of expectations.

Possible models for forming expectations include:

-   **Trust on first use:** Accept the first version of the package as-is. On
    each version update, compare the old provenance to the new provenance and
    alert on any differences. This can be augmented by having rules about what
    changes are benign, such as a parameter known to be safe or a heuristic
    about safe git branches or tags.

-   **Defined by producer:** The package producer tells the verifier what their
    expectations ought to be. In this model, the verifier SHOULD provide an
    authenticated communication mechanism for the producer to set the package's
    expectations, and there SHOULD be some protection against an adversary
    unilaterally modifying them. For example, modifications might require
    two-party control, or consumers might have to accept each policy change
    (another form of trust on first use).

-   **Defined in source:** The source repository tells the verifier what their
    expectations ought to be. In this model, the package name is immutably bound
    to a source repository and all other external parameters are defined in the
    source repository. This is how the Go ecosystem works, for example, since
    the package name *is* the source repository location.

It is important to note that expectations are tied to a *package name*, whereas
provenance is tied to an *artifact*. Different versions of the same package name
will likely have different artifacts and therefore different provenance. Similarly, an
artifact might have different names in different package ecosystems but use the same
provenance file.

### Architecture options

There are several options (non-mutually exclusive) for where provenance verification
can happen: the package ecosystem at upload time, the consumers at download time, or
via a continuous monitoring system. Each option comes with its own set of
considerations, but all are valid and at least one SHOULD be used.

More than one component can verify provenance. For example, even if a package
ecosystem verifies provenance, consumers who get artifacts from that package
ecosystem might wish to verify provenance themselves for defense in depth. They
can do so using either client-side verification tooling or by polling a
monitor.

#### Package ecosystem

[Package ecosystem]: #package-ecosystem

A <dfn>package ecosystem</dfn> is a set of rules and conventions governing
how packages are distributed. Every package artifact has an ecosystem, whether it is
formal or ad-hoc. Some ecosystems are formal, such as language distribution
(e.g. [Python/PyPA](https://www.pypa.io)), operating system distribution (e.g.
[Debian/Apt](https://wiki.debian.org/DebianRepository/Format)), or artifact
distribution (e.g. [OCI](https://github.com/opencontainers/distribution-spec)).
Other ecosystems are informal, such as a convention used within a company. Even
ad-hoc distribution of software, such as through a link on a website, is
considered an "ecosystem". For more background, see
[Package Model](terminology.md#package-model).

During package upload, a package ecosystem can ensure that the artifact's
provenance matches the expected values for that package name's provenance before
accepting it into the package registry.  This option is RECOMMENDED whenever
possible because doing so benefits all of the package ecosystem's clients.

The package ecosystem is responsible for making its expectations available to
consumers, reliably redistributing artifacts and provenance, and providing tools
to enable safe artifact consumption (e.g. whether an artifact meets
expectations).

#### Consumer

[Consumer]: #consumer

A package artifact's <dfn>consumer</dfn> is the organization or individual that uses the
package artifact.

Consumers can form their own expectations for artifacts or use the default
expectations provided by the package producer and/or package ecosystem.
When forming their own expectations, the consumer uses client-side verification tooling to ensure
that the artifact's provenance matches their expectations for that package
before use (e.g. during installation or deployment). Client-side verification
tooling can be either standalone, such as
[slsa-verifier](https://github.com/slsa-framework/slsa-verifier), or built into
the package ecosystem client.

#### Monitor

[Monitor]: #monitor

A <dfn>monitor</dfn> is a service that verifies provenance for a set
of packages and publishes the result of that verification. The set of
packages verified by a monitor is arbitrary, though it MAY mimic the set
of packages published through one or more package ecosystems. The monitor
SHOULD publish its expectations for all the packages it verifies.

Consumers can continuously poll a monitor to detect artifacts that
do not meet the monitor's expectations. Detecting artifacts that fail
verification is of limited benefit unless a human or automated system takes
action in response to the failed verification.


---

## Build: Assessing build platforms — `assessing-build-platforms.md`

*Locator page:* https://slsa.dev/spec/v1.2/assessing-build-platforms · *Requirements extracted:* R-0071 – R-0074 (4 statements)

> Page description (front matter): Guidelines for assessing build platform security.

One of SLSA's guiding [principles](principles.md) is to "trust platforms, verify
artifacts". However, consumers cannot trust platforms to produce Build L3
artifacts and provenance unless they have some proof that the provenance is
[unforgeable](build-requirements.md#provenance-unforgeable) and the builds are
[isolated](build-requirements.md#isolated).

This page describes the parts of a build platform that consumers SHOULD assess
and provides sample questions consumers can ask when assessing a build platform.
See also [Threats & mitigations](threats.md) and the
[build model](terminology.md#build-model).

### Threats

#### Adversary goal

The SLSA Build track defends against an adversary whose primary goal is to
inject unofficial behavior into a package artifact while avoiding detection.
Remember that [verifiers](verifying-artifacts.md) only accept artifacts whose
provenance matches expectations. To bypass this, the adversary tries to either
(a) tamper with a legitimate build whose provenance already matches
expectations, or (b) tamper with an illegitimate build's provenance to make it
match expectations.

More formally, if a build with external parameters P would produce an artifact
with binary hash X and a build with external parameters P' would produce an
artifact with binary hash Y, they wish to produce provenance indicating a build
with external parameters P produced an artifact with binary hash Y.

See threats [D], [E], [F], and [G] for examples of specific threats.

Note: Platform abuse (e.g. running non-build workloads) and attacks against
builder availability are out of scope of this document.

#### Adversary profiles

Consumers SHOULD also evaluate the build platform's ability to defend against the
following types of adversaries.

1.  Project contributors, who can:
    -   Create builds on the build platform. These are the adversary's controlled
        builds.
    -   Modify one or more controlled builds' external parameters.
    -   Modify one or more controlled builds' environments and run arbitrary
        code inside those environments.
    -   Read the target build's source repo.
    -   Fork the target build's source repo.
    -   Modify a fork of the target build's source repo and build from it.
2.  Project maintainer, who can:
    -   Do everything listed under "project contributors".
    -   Create new builds under the target build's project or identity.
    -   Modify the target build's source repo and build from it.
    -   Modify the target build's configuration.
3.  Build platform administrators, who can:
    -   Do everything listed under "project contributors" and "project
        maintainers".
    -   Run arbitrary code on the build platform.
    -   Read and modify network traffic.
    -   Access the control plane's cryptographic secrets.
    -   Remotely access build environments (e.g. via SSH).

[D]: threats.md#d-external-build-parameters
[E]: threats.md#e-build-process
[F]: threats.md#f-artifact-publication
[G]: threats.md#g-distribution-channel

### Build platform components

Consumers SHOULD consider at least these five elements of the
[build model](terminology.md#build-model) when assessing build platforms for SLSA
conformance: external parameters, control plane, build environments, caches,
and outputs.

![image](images/build-model.svg)

The following sections detail these elements of the build model and give prompts
for assessing a build platform's ability to produce SLSA Build L3 provenance.
The assessment SHOULD take into account the security model used to identify the
transitive closure of the `builder.id` for the
[provenance model](build-provenance.md#model), specifically around the
platform's boundaries, actors, and interfaces.

#### External parameters

External parameters are the external interface to the builder and include all
inputs to the build process. Examples include the source to be built, the build
definition/script to be executed, user-provided instructions to the
control plane for how to create the build environment (e.g. which operating
system to use), and any additional user-provided strings.

##### Prompts for assessing external parameters

-   How does the control plane process user-provided external parameters?
    Examples: sanitizing, parsing, not at all
-   Which external parameters are processed by the control plane and which are
    processed by the build environment?
-   What sort of external parameters does the control plane accept for
    build environment configuration?
-   How do you ensure that all external parameters are represented in the
    provenance?
-   How will you ensure that future design changes will not add additional
    external parameters without representing them in the provenance?

#### Control plane

The control plane is the build platform component that orchestrates each
independent build execution. It is responsible for setting up each build and
cleaning up afterwards. At SLSA Build L2+ the control plane generates and signs
provenance for each build performed on the build platform. The control plane is
operated by one or more administrators, who have privileges to modify the
control plane.

##### Prompts for assessing the control plane

-   Administration
    -   What are the ways an employee can use privileged access to influence a
        build or provenance generation? Examples: physical access, terminal
        access, access to cryptographic secrets
    -   What controls are in place to detect or prevent the employee from
        abusing such access? Examples: two-person approvals, audit logging,
        workload identities
    -   Roughly how many employees have such access?
    -   How are privileged accounts protected? Examples: two-factor
        authentication, client device security policies
    -   What plans do you have for recovering from security incidents and platform
        outages? Are they tested? How frequently?

-   Provenance generation
    -   How does the control plane observe the build to ensure the provenance's
        accuracy?
    -   Are there situations in which the control plane will not generate
        provenance for a completed build? What are they?

-   Development practices
    -   How do you track the control plane's software and configuration?
        Example: version control
    -   How do you build confidence in the control plane's software supply
        chain? Example: SLSA L3+ provenance, build from source
    -   How do you secure communications between builder components? Example:
        TLS with certificate transparency.
    -   Are you able to perform forensic analysis on compromised build
        environments? How? Example: retain base images indefinitely

-   Creating build environments
    -   How does the control plane share data with build environments? Example:
        mounting a shared file system partition
    -   How does the control plane protect its integrity from build
        environments? Example: not mount its own file system partitions on
        build environments
    -   How does the control plane prevent build environments from accessing its
        cryptographic secrets? Examples: dedicated secret storage, not mounting
        its own file system partitions to build environments, hardware security
        modules

-   Managing cryptographic secrets
    -   How do you store the control plane's cryptographic secrets?
    -   Which parts of the organization have access to the control plane's
        cryptographic secrets?
    -   What controls are in place to detect or prevent employees abusing such
        access? Examples: two-person approvals, audit logging
    -   How are secrets protected in memory? Examples: secrets are stored in
        hardware security modules and backed up in secure cold storage
    -   How frequently are cryptographic secrets rotated? Describe the rotation
        process.
    -   What is your plan for remediating cryptographic secret compromise? How
        frequently is this plan tested?

#### Build environment

The build environment is the independent execution context where the build
takes place. In the case of a distributed build, the build environment is the
collection of all execution contexts that run build steps. Each build
environment must be isolated from the control plane and from all other build
environments, including those running builds from the same tenant or project.
Tenants are free to modify the build environment arbitrarily. Build
environments must have a means to fetch input artifacts (source, dependencies,
etc).

##### Prompts for assessing build environments

-   Isolation technologies
    -   How are build environments isolated from the control plane and each
        other? Examples: VMs, containers, sandboxed processes
    -   How is separation achieved between trusted and untrusted processes?
    -   How have you hardened your build environments against malicious tenants?
        Examples: configuration hardening, limiting attack surface
    -   How frequently do you update your isolation software?
    -   What is your process for responding to vulnerability disclosures? What
        about vulnerabilities in your dependencies?
    -   What prevents a malicious build from gaining persistence and influencing
        subsequent builds?

-   Creation and destruction
    -   What operating system and utilities are available in build environments
        on creation? How were these elements chosen? Examples: A minimal Linux
        distribution with its package manager, OSX with HomeBrew
    -   How long could a compromised build environment remain active in the
        build platform?

-   Network access
    -   Are build environments able to call out to remote execution? If so, how
        do you prevent them from tampering with the control plane or other build
        environments over the network?
    -   Are build environments able to open services on the network? If so, how
        do you prevent remote interference through these services?

#### Cache

Builders may have zero or more caches to store frequently used dependencies.
Build environments may have either read-only or read-write access to caches.

##### Prompts for assessing caches

-   What sorts of caches are available to build environments?
-   How are those caches populated?
-   How are cache contents validated before use?

#### Output storage

Output Storage holds built artifacts and their provenance. Storage may either be
shared between build projects or allocated separately per-project.

##### Prompts for assessing output storage

-   How do you prevent builds from reading or overwriting files that belong to
    another build? Example: authorization on storage
-   What processing, if any, does the control plane do on output artifacts?

### Builder evaluation

Organizations can either self-attest to their answers or seek certification from
a third-party auditor. Evidence for self-attestation should be published on
the internet and can include information such as the security model defined as
part of the provenance. Evidence submitted for third-party certification need not
be published.


---

## Source: Requirements for producing source — `source-requirements.md`

*Locator page:* https://slsa.dev/spec/v1.2/source-requirements · *Requirements extracted:* R-0075 – R-0134 (60 statements)

> Page description (front matter): "This page covers the detailed technical requirements for producing source revisions at each SLSA level. The intended audience is source control system implementers and security engineers."

### Objective

The primary purpose of the SLSA Source track is to provide producers and consumers with increasing levels of trust in the source code they produce and consume.
It describes increasing levels of trustworthiness and completeness of how a source revision was created.

The expected process for creating a new revision is determined solely by that repository's owner (the organization) who also determines the intent of the software in the repository and administers technical controls to enforce the process.

Consumers can review attestations to verify whether a particular revision meets their standards.

### Definitions

A **Version Control System (VCS)** is a system of software and protocols for
managing the version history of a set of files. Git, Mercurial, and Subversion
are all examples of version control systems.

The following terms apply to Version Control Systems:

| Term | Description
| --- | ---
| Source Repository (Repo) | A self-contained unit that holds the content and revision history for a set of files, along with related metadata like Branches and Tags.
| Source Revision | A specific, logically immutable snapshot of the repository's tracked files. It is uniquely identified by a revision identifier, such as a cryptographic hash like a Git commit SHA or a path-qualified sequential number like `25@trunk/` in SVN. A Source Revision includes both the content (the files) and its associated version control metadata, such as the author, timestamp, and parent revision(s). Note: Path qualification is needed for version control systems that represent Branches and Tags using paths, such as Subversion and Perforce.
| Named Reference | A user-friendly name for a specific source revision, such as `main` or `v1.2.3`.
| Change | A modification to the state of the Source Repository, such as creation of a new Source Revision based on a previous Source Revision, or creation, deletion, or modification of a Named Reference.
| Change History | A record of the history of Source Revisions that preceded a specific revision.
| Branch | A Named Reference that moves to track the Change History of a cohesive line of development within a Source Repository. E.g. `main`, `develop`, `feature-x`
| <span id="tag">Tag</span> | A Named Reference that is intended to be immutable. Once created, it is not moved to point to a different revision. E.g. `v1.2.3`, `release-20250722`

> **NOTE:** The 'branch' and 'tag' features within version control systems may
not always align with the 'Branch' and 'Tag' definitions provided in this
specification. For example, in git and other version control systems, the UX may
allow 'tags' to be moved. Patterns like `latest` and `nightly` tags rely on this.
For the purposes of this specification these would be classified as 'Named References' and not as 'Tags'.

A **Source Control System (SCS)** is a platform or combination of services
(self-hosted or SaaS) that hosts a Source Repository and provides a trusted
foundation for managing source revisions by enforcing policies for
authentication, authorization, and change management, such as mandatory code
reviews or passing status checks.

The following terms apply to Source Control Systems:

| Term | Description
| --- | ---
| Organization | A set of people who collectively create Source Revisions within a Source Repository. Examples of organizations include open-source projects, a company, or a team within a company. The organization defines the goals of a Source Repository and the methods used to produce new Source Revisions.
| Proposed Change | A proposal to make a Change in a Source Repository.
| Source Provenance | Information about how a Source Revision came to exist, where it was hosted, when it was generated, what process was used, who the contributors were, and which parent revisions preceded it.

#### Source Roles

| Role | Description
| --- | ---
| Administrator | A human who can perform privileged operations on one or more projects. Privileged actions include, but are not limited to, modifying the change history and modifying project- or organization-wide security policies.
| Trusted person | A human who is authorized by the organization to propose and approve changes to the source.
| Trusted robot | Automation authorized by the organization to act in explicitly defined contexts. The robot’s identity and codebase cannot be unilaterally influenced.
| Untrusted person | A human who has limited access to the project. They MAY be able to read the source. They MAY be able to propose or review changes to the source. They MAY NOT approve changes to the source or perform any privileged actions on the project.

### Onboarding

When onboarding a branch to the SLSA Source Track or increasing the level of
that branch, organizations are making claims about how the branch is managed
from that revision forward. This establishes [continuity](#continuity).

No claims are made for prior revisions.

### Basics

NOTE: This table presents a simplified view of the requirements. See the
[Requirements](#requirements) section for the full list of requirements for each
level.

| Track/Level | Requirements | Focus
| ----------- | ------------ | -----
| [Source L1](#source-l1) | Use a version control system. | Generation of discrete Source Revisions for precise consumption.
| [Source L2](#source-l2) | Preserve Change History and generate Source Provenance. | Reliable history through enforced controls and evidence.
| [Source L3](#source-l3) | Enforce organizational technical controls. | Consumer knowledge of guaranteed technical controls.
| [Source L4](#source-l4) | Require code review. | Improved code quality and resistance to insider threats.

#### Level 1: Version controlled

**Summary:**

The source is stored and managed through a modern version control system.

**Intended for:**

Organizations currently storing source in non-standard ways who want to quickly gain some benefits of SLSA and better integrate with the SLSA ecosystem with minimal impact to their current workflows.

**Benefits:**

Migrating to the appropriate tools is an important first step on the road to operational maturity.

#### Level 2: History & Provenance

**Summary:**

Branch history is continuous, immutable, and retained, and the
SCS issues Source Provenance Attestations for each new Source Revision.
The attestations provide contemporaneous, tamper-resistant evidence of when
changes were made, who made them, and which technical controls were enforced.

**Intended for:**

All organizations of any size producing software of any kind.

**Benefits:**

Reliable history allows organizations and consumers to track changes to software
over time, enabling attribution of those changes to the actors that made them.
Source Provenance provides strong, tamper-resistant evidence of the process that
was followed to produce a Source Revision.

#### Level 3: Continuous technical controls

**Summary:**

The SCS is configured to enforce the Organization's technical controls for specific Named References within the Source Repository.

**Intended for:**

Organizations that want to show evidence of their additional technical controls.

**Benefits:**

A verifier can use this published data to ensure that a given Source Revision
was created in the correct way by verifying the Source Provenance or VSA.
Provides verifiers strong evidence of all technical controls enforced during the update of a Named Reference.

#### Level 4: Two-party review

**Summary:**

The SCS requires two trusted persons to review all changes to protected
branches.

**Intended for:**

Organizations that want strong guarantees that the software they produce is not
subject to unilateral changes that would subvert their intent.

**Benefits:**

Makes it harder for an actor to introduce malicious changes into the software
and makes it more likely that the source reflects the intent of the
organization.

### Requirements

Many examples in this document use the
[git version control system](https://git-scm.com/), but use of git is not a
requirement to meet any level on the SLSA source track.

#### Organization

[Organization]: #organization

*Table — columns: Requirement, Description, L1, L2, L3, L4*

##### Choose an appropriate Source Control System  `#choose-scs`

An organization producing Source Revisions MUST select an SCS capable of reaching
their desired SLSA Source Level.

> For example, if an organization wishes to produce revisions at Source Level 3,
they MUST choose a Source Control System capable of producing Source Level 3
attestations.

Levels: L1 ✓ · L2 ✓ · L3 ✓ · L4 ✓

##### Configure the SCS to control access and enforce history  `#access-and-history`

The organization MUST configure access controls to restrict sensitive operations
on the Source Repository. These controls MUST be implemented using the
SCS-provided [Identity Management capability](#identity-management).

> For example, an organization may configure the SCS to assign users to a
`maintainers` role and only allow users in `maintainers` to make updates to
`main`.

The SCS MUST be configured to produce a reliable [Change History](#history) for
its consumable Source Revisions.
If the SCS provides this capability by design, no additional controls are needed.
Otherwise the organization MUST provide evidence of [continuous enforcement](#continuity).

If the SCS supports [Tags](#tag), the SCS MUST be configured to prevent them
from being moved or deleted.

> For example, if a git tag `release1` is used to indicate a release revision
with ID `abc123`, controls must be configured to prevent that tag from being
updated to any other revision in the future.
Evidence of these controls (and their continuity) will appear in the Source
Provenance documents for revision `abc123`.

Levels: L1 — · L2 ✓ · L3 ✓ · L4 ✓

##### Safe Expunging Process  `#safe-expunging-process`

SCSs MAY allow the organization to expunge (remove) content from a repository
and its change history without leaving a public record of the removed content,
but the organization MUST only allow these changes in order to meet legal or
privacy compliance requirements. Content changed under this process includes
changing files, history, references, or any other metadata stored by the SCS.

##### Warning

Removing a revision from a repository is similar to deleting a package version
from a registry: it's almost impossible to estimate the amount of downstream
supply chain impact.

> For example, in Git, each revision ID is based on the ones before it.
When you remove a revision, you must generate new revisions (and new revision IDs)
for any revisions that were built on top of it. Consumers who took a dependency
on the old revisions may now be unable to refer to the revision they've already
integrated into their products.

It may be the case that the specific set of changes targeted by a legal takedown
can be expunged in ways that do not impact consumed revisions, which can mitigate
these problems.

It is also the case that removing content from a repository won't necessarily
remove it everywhere.
The content may still exist in other copies of the repository, either in backups
or on developer machines.

##### Process

An organization MUST document the Safe Expunging Process and describe how
requests and actions are tracked and SHOULD log the fact that content was
removed. Different organizations and tech stacks may have different approaches
to the problem.

SCSs SHOULD have technical mechanisms in place which require an Administrator
plus at least one additional 'trusted person' to trigger any expunging
(removals) made under this process.

The application of the Safe Expunging Process and the resulting logs MAY be
private to prevent calling attention to potentially sensitive data or to comply
with local laws and regulations. Organizations SHOULD prefer to make logs public
if possible.

Levels: L1 — · L2 ✓ · L3 ✓ · L4 ✓

##### Continuous technical controls  `#technical-controls`

The organization MUST provide evidence of continuous enforcement via technical
controls for any claims made in the Source Provenance attestations or VSAs (see
[control continuity](#continuity)).

The organization MUST document the meaning of their enforced technical controls.

> For example, if an organization implements a technical control via a custom
tool (such as required GitHub Actions workflow), it must indicate the name of
this tool, what it accomplishes, and how to find its evidence in the provenance
attestation.

> For another example, if the organization claims that all consumable Source
Revisions on the `main` branch were tested prior to acceptance, this MUST be
explicitly enforced in the SCS.

Levels: L1 — · L2 — · L3 ✓ · L4 ✓

#### Source Control System

*Table — columns: Requirement, Description, L1, L2, L3, L4*

##### Repositories are uniquely identifiable  `#repository-ids`

The repository ID is defined by the SCS and MUST be uniquely identifiable within
the context of the SCS with a stable locator, such as a URI.

Levels: L1 ✓ · L2 ✓ · L3 ✓ · L4 ✓

##### Revisions are immutable and uniquely identifiable  `#revision-ids`

The revision ID is defined by the SCS and MUST be uniquely identifiable within the context of the repository.
When the revision ID is a digest of the content of the revision (as in git) nothing more is needed.
When the revision ID is a number or otherwise not a digest, then the SCS MUST document how the immutability of the revision is established.
The same revision ID MAY be present in multiple repositories.

See also [Use cases for non-cryptographic, immutable, digests](https://github.com/in-toto/attestation/blob/main/spec/v1/digest_set.md#use-cases-for-non-cryptographic-immutable-digests).

Levels: L1 ✓ · L2 ✓ · L3 ✓ · L4 ✓

##### Human readable changes  `#human-readable-diff`

The SCS MUST provide tooling to display Changes between one Source Revision and
another in a human readable form (e.g. 'diffs') for all plain-text changes and
SHOULD provide mechanisms to provide human understandable interpretations of
non-plain-text changes (e.g. render images, verify and display provenance for
binaries, etc.).

Levels: L1 ✓ · L2 ✓ · L3 ✓ · L4 ✓

##### Source Verification Summary Attestations  `#source-summary`

The SCS MUST generate a
[source verification summary attestation](#source-verification-summary-attestation) (Source VSA)
to indicate the SLSA Source Level of any revision at Level 1 or above.

If a consumer is authorized to access a revision, they MUST be able to fetch the
corresponding Source VSA.

If the SCS DOES NOT generate a VSA for a revision, the revision has Source Level
0.

At Source Levels 1 and 2 the SCS MAY issue these attestations based on its
understanding of the underlying system (e.g. based on design docs, security
reviews, etc.), but at Level 2+ the SCS MUST use the SCS-issued
[source provenance](#source-provenance) when issuing the VSAs.

Levels: L1 ✓ · L2 ✓ · L3 ✓ · L4 ✓

##### History  `#history`

There are three key aspects to change history:

1.  What were all the previous states of a Branch?
2.  How and when did they change?
3.  How does the current revision relate to previous revisions?

To answer these questions, the SCS MUST record all changes to Named References,
including when they occurred, who made them, and the new Source Revision ID.

If Source Revisions have ancestry relationships in the VCS, the SCS MUST ensure
that a Branch can only be updated to point to revisions that descend from the
current revision.
In git, this requires a technical control to prohibit `git push --force`.

This requirement captures evidence that the organization intended to make the
changes captured by the new revision.

> For example, if a branch currently points to revision `a`, it may only be
moved to a new revision `b` if `a` is an ancestor of `b`.

Levels: L1 — · L2 ✓ · L3 ✓ · L4 ✓

##### Continuity  `#continuity`

Technical Controls are only effective if they are used continuously in the
history of a Branch.
'Control continuity' reflects an organization's ongoing commitment to a
technical control.

For each technical control claimed in a VSA, continuity MUST be established and
tracked from a specific start revision.
If there is a lapse in continuity for a specific control, continuity of that
control MUST be re-established from a new revision.

Exceptions to the continuity requirement are allowed via the [safe expunging process](#safe-expunging-process).

> For example, the `main` branch currently points to revision `a` when a new
technical control `t` is configured.
The next revision on the `main` branch, `b` will be the first revision that was
protected by `t` and `b` is the first revision in the "continuity" of `t`.
Any revisions added to `main` while `t` is disabled will reset the continuity of `t`.

Levels: L1 — · L2 ✓ · L3 ✓ · L4 ✓

##### Identity Management  `#identity-management`

The SCS MUST provide an identity management system or some other means of
identifying and authenticating actors.

The SCS MUST allow organizations to specify which actors and roles are allowed
to perform sensitive actions within a repository (e.g. creation or updates of
branches, approval of changes).

Depending on the SCS, identity management may be provided by source control
services (e.g., GitHub, GitLab), implemented using cryptographic signatures
(e.g., using gittuf to manage public keys for actors), or extending existing
authentication systems used by the organization (e.g., Active Directory, Okta,
etc.).

The SCS MUST document how actors are identified for the purposes of attribution.

Activities conducted on the SCS SHOULD be attributed to authenticated
identities.

Levels: L1 — · L2 ✓ · L3 ✓ · L4 ✓

##### Source Provenance  `#source-provenance`

[Source Provenance](#source-provenance-attestations) are attestations that
contain information about how a specific revision was created and how it came to
exist on a protected branch or how a tag came to point at it. They are
associated with the revision identifier delivered to consumers and are a
statement of fact from the perspective of the SCS. The SCS MUST document the
format and intent of all Source Provenance attestations it produces.

Source Provenance MUST be created contemporaneously with the branch being
updated such that they provide a credible, auditable, record of changes.

If a consumer is authorized to access a revision, they MUST be able to access the
corresponding Source Provenance documents for that revision.

It is possible that an SCS can make no claims about a particular revision.

> For example, this would happen if the revision was created on another SCS,
on an unprotected branch (such as a `topic` branch), or if the revision was not
the result of the expected process.

Levels: L1 — · L2 ✓ · L3 ✓ · L4 ✓

##### Protected Named References  `#protected-refs`

The SCS MUST provide the ability for an organization to enforce customized technical controls for Named References.

The SCS MUST provide a mechanism for organizations to indicate which Named
References should be protected by technical controls.

> For example, the organization may instruct the SCS to protect `main` and
`refs/heads/releases/*`, but not `refs/heads/experimental/*` using branch
protection rules (e.g. [GitHub](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets),
[GitLab](https://docs.gitlab.com/ee/user/project/repository/branches/protected.html))
or via the application and verification of [gittuf](https://github.com/gittuf/gittuf)
policies.

> For another example, the organization may instruct the SCS to prevent the deletion of
all `refs/tags/releases/*` using tag protection rules
(e.g. [GitHub](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets),
[GitLab](https://docs.gitlab.com/user/project/protected_tags/))
or via the application and verification of [gittuf](https://github.com/gittuf/gittuf)
policies.

The SCS MUST

-   Record technical controls enforced on Named References in contemporaneously
   produced attestations associated with the corresponding Source Revisions.
-   Allow organizations to provide
   [organization-specified properties](#additional-properties) to be included in the
   [Source VSA](#source-verification-summary-attestation) when the corresponding controls are
   enforced.
-   Allow organizations to distribute additional attestations related to their
   technical controls to consumers authorized to access the corresponding Source
   Revision.
-   Prevent organization-specified properties from beginning with any value
   other than `ORG_SOURCE_`.

Levels: L1 — · L2 — · L3 ✓ · L4 ✓

##### Two-party review  `#two-party-review`

Changes in protected branches MUST be agreed to by two or more trusted persons prior to submission.
The following combinations are acceptable:

-   Uploader and reviewer are two different trusted persons.
-   Two different reviewers are trusted persons.

Reviews SHOULD cover, at least, security relevant properties of the code.

**[Final revision approved]** This requirement applies to the final revision
submitted. I.e., if additional changes are made during the review process, those changes MUST
be reviewed as well.

**[Context-specific approvals]** Approvals are for a specific context, such as a
repo + branch in git. Moving fully reviewed content from one context to another
still requires review. The exact definition of “context” depends on the project,
and this does not preclude well-understood automatic merges, such as cutting a release branch.

**[Informed Review]** The SCS MUST present reviewers with a clear representation of the result of accepting the proposed change. See [Human Readable Changes](#human-readable-diff).

**[Trusted Robot Contributions]** An organization MAY choose to grant a Trusted
Robot a perpetual exception to a policy (e.g. a bot may be able to merge a change
that has not been reviewed by two parties).

Examples:

-   Import and migration bots that move code from one repo to another.
-   Dependabot

Levels: L1 — · L2 — · L3 — · L4 ✓

### Communicating source levels

SLSA source level details are communicated using attestations.
These attestations either refer to a source revision itself or provide context needed to evaluate an attestation that _does_ refer to a revision.

There are two broad categories of source attestations within the source track:

1.  Source verification summary attestations (Source VSAs): Used to communicate to downstream users what high level security properties a given source revision meets.
2.  Source provenance attestations: Provide trustworthy, tamper-proof, metadata with the necessary information to determine what high level security properties a given source revision has.

To provide interoperability and ensure ease of use, it's essential that the Source VSAs are applicable across all Source Control Systems.
However, due to the significant differences in how SCSs operate and how they may choose to meet the Source Track requirements, it is preferable to
allow for flexibility with the full source provenance attestations. To that end, SLSA leaves source provenance attestations undefined and up to the SCSs to determine
what works best in their environment.

#### Source verification summary attestation

Source verification summary attestations (Source VSAs) are issued by some authority that has sufficient evidence to make the determination of a given
revision's source level.  Source VSAs convey properties about the revision as a whole and summarize properties computed over all
the changes that contributed to that revision over its history.

The source track issues Source VSAs using the [Verification Summary Attestations](./verification_summary.md) format as follows:

1.  `subject.uri` SHOULD be set to a URI where a human can find details about
    the revision. This field is not intended for policy decisions. Instead, it
    is only intended to direct a human investigating verification failures.
    -   For example: `https://github.com/slsa-framework/slsa/commit/6ff3cd75c8c9e0fcedc62bd6a79cf006f185cedb`
2.  `subject.digest` MUST include the revision identifier (e.g. `gitCommit`) and MAY include other digests over the contents of the revision (e.g. `gitTree`, `dirHash`, etc.).
SCSs that do not use cryptographic digests MUST define a canonical type that is used to identify immutable revisions and MUST include the repository within the type[^1].
    -   For example: `svn_revision_id: svn+https://svn.myproject.org/svn/MyProject/trunk@2019`
3.  `subject.annotations.sourceRefs` SHOULD be set to a list of references that pointed to this revision when the attestation was created. The list MAY be non-exhaustive.
    -   git references MUST be fully qualified (e.g. `refs/heads/main` or `refs/tags/v1.0`) to reduce the likelihood of confusing downstream tooling.
4.  `resourceUri` MUST be set to the URI of the repository, preferably using [SPDX Download Location](https://spdx.github.io/spdx-spec/v2.3/package-information/#77-package-download-location-field).
E.g. `git+https://github.com/foo/hello-world`.
5.  `verifiedLevels` MUST include the SLSA source track level the SCS asserts the revision meets. One of `SLSA_SOURCE_LEVEL_0`, `SLSA_SOURCE_LEVEL_1`, `SLSA_SOURCE_LEVEL_2`, `SLSA_SOURCE_LEVEL_3`.
MAY include additional properties as asserted by the SCS.  The SCS MUST include _only_ the highest SLSA source level met by the revision.
6.  `dependencyLevels` MAY be empty as source revisions are typically terminal nodes in a supply chain. For example, this could be used to indicate the source level of any git submodules present in the revision.

##### Additional properties

The SLSA source track MAY create additional properties to include in
`verifiedLevels` which attest to other claims concerning a revision.

The SCS MAY embed additional properties within `verifiedLevels` provided by the
organization as long as they are prefixed by `ORG_SOURCE_`  to distinguish them
from other properties the SCS may wish to use. The SCS MUST enforce the use of
this prefix for such properties. An organization MAY further differentiate
properties using:

-   `ORG_SOURCE_` to indicate a property that is meant for consumption by
   external consumers.
-   `ORG_SOURCE_INTERNAL_` to indicate a property that is not meant for
   consumption by external consumers.

The meaning of the properties is left entirely to the organization.

##### Populating sourceRefs

The Source VSA issuer may choose to populate `sourceRefs` in any way they wish.
Downstream users are expected to be familiar with the method used by the issuer.

Example implementations:

-   Issue a new VSA for each merged Pull Request and add the destination branch to `sourceRefs`.
-   Issue a new VSA each time a Named Reference is updated to point to a new revision.

##### Example

```json
"_type": "https://in-toto.io/Statement/v1",
"subject": [{
  "uri": "https://github.com/foo/hello-world/commit/9a04d1ee393b5be2773b1ce204f61fe0fd02366a",
  "digest": {"gitCommit": "9a04d1ee393b5be2773b1ce204f61fe0fd02366a"},
  "annotations": {"sourceRefs": ["refs/heads/main", "refs/heads/release_1.0"]}
}],

"predicateType": "https://slsa.dev/verification_summary/v1",
"predicate": {
  "verifier": {
    "id": "https://example.com/source_verifier",
  },
  "timeVerified": "1985-04-12T23:20:50.52Z",
  "resourceUri": "git+https://github.com/foo/hello-world",
  "policy": {
    "uri": "https://example.com/slsa_source.policy",
  },
  "verificationResult": "PASSED",
  "verifiedLevels": ["SLSA_SOURCE_LEVEL_3"],
}
```

##### How to verify

See [Verifying Source](./verifying-source.md) for instructions how to verify
VSAs for Source Revisions.

#### Source provenance attestations

Source provenance attestations provide tamper-proof evidence ([attestation model](attestation-model))
that can be used to determine what SLSA Source Level or other high-level properties a given revision meets.
This evidence can be used by:

-   an authority as the basis for issuing a [Source VSA](#source-verification-summary-attestation)
-   a consumer to cross-check a [Source VSA](#source-verification-summary-attestation) they received for a revision
-   a consumer to enforce a more detailed policy than the organization's own process

SCSs may have different methods of operating that necessitate different forms of evidence.
E.g. GitHub-based workflows may need different evidence than Gerrit-based workflows, which would both likely be different from workflows that
operate over Subversion repositories.

These differences also mean that, depending on the configuration, the issuers of provenance attestations may vary from implementation to implementation, often because entities with the knowledge to issue them may vary.
The authority that issues [Source VSAs](#source-verification-summary-attestation) MUST understand which entity should issue each provenance attestation type, and ensure all source provenance attestations come from their expected issuers.

'Source provenance attestations' is a generic term used to refer to any type of attestation that provides evidence of the process used to create a revision.

Example source provenance attestations:

-   A TBD attestation which describes the revision's parents and the actors involved in creating this revision.
-   A "code review" attestation which describes the basics of any code review that took place.
-   An "authentication" attestation which describes how the actors involved in any revision were authenticated.
-   A [Vuln Scan attestation](https://github.com/in-toto/attestation/blob/main/spec/predicates/vuln.md)
    which describes the results of a vulnerability scan over the contents of the revision.
-   A [Test Results attestation](https://github.com/in-toto/attestation/blob/main/spec/predicates/test-result.md)
 which describes the results of any tests run on the revision.
-   An [SPDX attestation](https://github.com/in-toto/attestation/blob/main/spec/predicates/spdx.md)
 which provides a software bill of materials for the revision.
-   A [SCAI attestation](https://github.com/in-toto/attestation/blob/main/spec/predicates/scai.md) used to
 describe which source quality tools were run on the revision.

Irrespective of the types of provenance attestations generated by an SCS and
their implementations, the SCS MUST document provenance
formats, and how each provenance attestation can be used to reason about the
revision's properties recorded in the summary attestation.

[^1]: in-toto attestations allow non-cryptographic digest types: https://github.com/in-toto/attestation/blob/main/spec/v1/digest_set.md#supported-algorithms.

### Future Considerations

#### Authentication

-   Better protection against phishing by forbidding second factors that are not
  phishing resistant.
-   Protect against authentication token theft by forbidding bearer tokens
  (e.g. PATs).
-   Including length of continuity in the VSAs


---

## Source: Verifying source — `verifying-source.md`

*Locator page:* https://slsa.dev/spec/v1.2/verifying-source · *Requirements extracted:* R-0135 – R-0140 (6 statements)

> Page description (front matter): |

SLSA uses attestations to indicate security claims associated with a repository
revision, but attestations don't do anything unless somebody inspects them. SLSA
calls that inspection **verification**, and this page describes how to verify
properties of source revisions using
[the attestations](source-requirements#communicating-source-levels) associated
with those revisions.

At Source L3+, Source Control Systems (SCSs) issue detailed
[provenance attestations](source-requirements#source-provenance-attestations) of
the process that was used to create specific revisions of a repository. These
provenance attestations are issued in bespoke formats and may be too burdensome
to use in some use cases.

[Source Verification Summary Attestations](source-requirements#source-verification-summary-attestation)
(Source VSAs) address this, making verification more efficient and ergonomic by
recording the result of prior verifications. Source VSAs may be issued by a VSA
provider to make a SLSA source level determination based on the content of those
attestations.

### How to verify a source revision

The source consumer checks:

1.  If they trust the SCS that issued the VSA and if the VSA applies to the
   revision they've fetched.
2.  If the claims made in the VSA match their expectations for how the source
   should be managed.
3.  (Optional): If the evidence presented in the source provenance matches the
   claims made in the VSA.

#### Step 1: Check the SCS

First, check the SLSA Source level by comparing the artifact to its VSA and the
VSA to a preconfigured root of trust. The goal is to ensure that the VSA
actually applies to the artifact in question and to assess the trustworthiness
of the VSA. This mitigates threats within "B" and "C", depending on SLSA Source
level.

Once, when bootstrapping the verifier:

-   Configure the verifier's roots of trust, meaning the recognized SCS
    identities and the maximum SLSA Source level each SCS is trusted up to.
    Different verifiers MAY use different roots of trust for repositories. The
    root of trust configuration is likely in the form of a map from (SCS public
    key identity, VSA `verifier.id`) to (SLSA Source level).

    <details>
    <summary>Example root of trust configuration</summary>

    The following snippet shows conceptually how a verifier's roots of trust
    might be configured using made-up syntax.

    ```jsonc
    "slsaSourceRootsOfTrust": [
        // A SCS trusted at SLSA Source L3, using a fixed public key.
        {
            "publicKey": "HKJEwI...",
            "scsId": "https://somescs.example.com/slsa/l3",
            "slsaSourceLevel": 3
        },
        // A different SCS that claims to be SLSA Source L3,
        // but this verifier only trusts it to L2.
        {
            "publicKey": "tLykq9...",
            "scsId": "https://differentscs.example.com/slsa/l3",
            "slsaSourceLevel": 2
        },
        // A SCS that uses Sigstore for authentication.
        {
            "sigstore": {
                "root": "global",  // identifies fulcio/rekor roots
                "subjectAlternativeNamePattern": "https://github.com/slsa-framework/slsa-source-poc/.github/workflows/compute_slsa_source.yml@refs/tags/v*.*.*"
            },
            "scsId": "https://github.com/slsa-framework/slsa-source-poc/.github/workflows/compute_slsa_source.yml@refs/tags/v*.*.*",
            "slsaSourceLevel": 3,
        }
        ...
    ],
    ```

    

Given a revision and its VSA follow the
[VSA verification instructions](./verification_summary.md#how-to-verify) and the
[validation-model] using the revision identifier to perform subject matching and
checking the `verifier.id` against the root-of-trust described above.

#### Step 2: Check Expectations

Next, check that the revision's VSA meets your expectations in order to mitigate
[threat "B"].

In our threat model, the adversary has the ability to create revisions within
the repository and get consumers to fetch that revision.  The adversary is not
able to subvert controls implemented by the Producer and enforced by the SCS.
Your expectations SHOULD be sufficient to detect an un-official revision and
SHOULD make it more difficult for an adversary to create a malicious official
revision.

You SHOULD compare the VSA against expected values for at least the following
fields:

| What | Why
| ---- | ---
| `verifier.id` identity from [Step 1] | To prevent an adversary from substituting a VSA making false claims from an unintended SCS.
| `subject.digest` from [Step 1] | To prevent an adversary from substituting a VSA from another revision.
| `verificationResult` | To prevent an adversary from providing a VSA for a revision that failed some aspect of the organization's expectations.
| `predicate.resourceUri` | To prevent an adversary from substituting a VSA for the intended repository (e.g. `git+https://github.com/IntendedOrg/hello-world`) for another (e.g. `git+https://github.com/AdversaryOrg/hello-world`)
| `subject.annotations.sourceRefs` | To prevent an adversary from substituting the intended revision from one branch (e.g. `release`) with another (e.g. `experimental_auth`).
| `verifiedLevels` | To ensure the expected controls were in place for the creation of the revision. E.g. `SLSA_SOURCE_LEVEL_3`, `ORG_SOURCE_STATIC_ANALYSIS`, etc...

[Threat "B"]: threats#b-modifying-the-source
[validation-model]: https://github.com/in-toto/attestation/blob/main/docs/validation.md#validation-model

#### Step 3: Verify Evidence using Source Provenance [optional]

Optionally, at SLSA Source Level 3 and up, check the [source provenance
attestations](source-requirements#source-provenance-attestations) directly.

As the format and implementation of source provenance attestations are left to
the SCS, you SHOULD form expectations about the claims in source provenance
attestations and how they map to a revision's properties claimed in its VSA in
conjunction with the SCS and the producer.

### Forming Expectations

<dfn>Expectations</dfn> are known values that indicate the corresponding
revision is authentic. For example, an SCS may maintain a mapping between
repository branches & tags and the controls they claim to implement. That
mapping constitutes a set of expectations.

Possible models for forming expectations include:

-   **Trust on first use:** Accept the first version of the revision as-is. On
    each update, compare the old VSA to the new VSA and alert on any
    differences.

-   **Defined by producer:** The revision producer tells the verifier what their
    expectations ought to be. In this model, the verifier SHOULD provide an
    authenticated communication mechanism for the producer to set the revision's
    expectations, and there SHOULD be some protection against an adversary
    unilaterally modifying them. For example, modifications might require
    two-party control, or consumers might have to accept each policy change
    (another form of trust on first use).

It is important to note that expectations are tied to a *repository branch or
tag*, whereas a VSA is tied to an *revision*. Different revisions will have
different VSAs and the claims made by those VSAs may differ.

### Architecture options

There are several options (non-mutually exclusive) for where VSA verification
can happen: the build system at source fetch time, the package ecosystem at
build artifact upload time, the consumers at download time, or
via a continuous monitoring system. Each option comes with its own set of
considerations, but all are valid and at least one SHOULD be used.

More than one component can verify VSAs. For example, even if a builder verifies
source VSAs, package ecosystems may wish to verify the source VSAs for the
artifacts they host that claim to be built from that source (as indicated by the
build provenance).


---

## Source: Assessing source control systems — `assessing-source-systems.md`

*Locator page:* https://slsa.dev/spec/v1.2/assessing-source-systems · *Requirements extracted:* R-0141 – R-0143 (3 statements)

> Page description (front matter): Guidelines for assessing source control system security.

One of SLSA's guiding [principles](principles.md) is to "trust platforms, verify
artifacts". However, consumers cannot trust source control systems (SCSs) unless
they have some proof that an SCS meets its
[requirements](source-requirements.md).

This page describes the parts of an SCS that consumers SHOULD assess and
provides sample questions consumers can ask when assessing a SCS. See also
[Threats & mitigations](threats.md).

### Threats

#### Adversary goal

The SLSA Source track defends against an adversary whose primary goal is to
inject unofficial behavior into protected source code while avoiding detection.
Organizations typically establish change management processes to prevent this
unofficial behavior from being introduced. The adversary's goal is to bypass the
change management process.

#### Adversary profiles

Consumers SHOULD also evaluate the source control systems' ability to defend
against the following types of adversaries.

1.  Project contributors, who can:
    -   Propose changes to protected branches of the source repo.
    -   Upload new content to the source repo.
2.  Project maintainer, who can:
    -   Do everything listed under "project contributors".
    -   Define the purpose of the source repo.
    -   Add or remove contributors to the source repo.
    -   Add or remove permissions granted to contributors of the source repo.
    -   Modify security controls within the source repo.
    -   Modify controls used to enforce the change management process on the
        source repo.
3.  Source control system administrators, who can:
    -   Do everything listed under "project contributors" and "project
        maintainers".
    -   Modify the source repo while bypassing the project maintainer's controls.
    -   Modify the behavior of the Source Control System itself.
    -   Access the control plane's cryptographic secrets.

### Source Control System components

Consumers SHOULD consider at least these elements when assessing a Source
Control System for SLSA conformance: control configuration, change management
interface, control plane, verifier, storage.

![source control system components](images/source-control-system-components.svg)

The following section details these elements.

#### Change management interface

The change management interface is the user interface for proposing and
approving changes to protected branches within a source repository. During
normal operation all such changes go through this interface.

#### Control configuration

Control configuration is how organizations establish technical controls in a
given source repository. If done well the configuration will reflect the intent
of the organization.

#### Technical controls

Technical controls are the organization configured settings that are used to
determine if a revision can be introduced into storage within any particular
context and who has access to those revisions.

The technical controls component is responsible for the storage of these
settings while the [control plane](#control-plane) is responsible for enforcing
the configured controls.

They include:

-   Read/write ACLs,
-   If approvals are required to introduce changes within a given context
-   Which actors are allowed to issue those approvals
-   Organization defined
    [change management processes](#enforced-change-management-process)
    requirements
-   etc...

#### Control plane

The control plane is the SCS component that orchestrates the introduction and
creation of new revisions into a source repository. It is responsible for
enforcing [technical controls](#technical-controls) and, at SLSA Source L3+,
generating and signing source provenance for each revision. The control plane is
operated by one or more administrators, who have privileges to modify the
control plane.

#### Verifier

The verifier is the SCS component that evaluates source provenance and generates
and signs a
[verification summary attestation](source-requirements#summary-attestation)
(VSA).

#### Storage

Storage holds source revisions and their provenance and summary attestations.

### Assessing components

The following are prompts for assessing a Source Control System's ability to
meet the SLSA requirements.

#### Prompts for assessing the change management interface

-   How does the SCS manage which actors are permitted to approve changes?
-   What types of non-plain-text changes can the change management interface
    render? How well does the SCS render those changes?
-   What controls does the change management interface provide for enabling
    Trusted Robot Contributions? Example: SLSA Build L3+ provenance, built from
    SLSA Source L4+ source.

#### Prompts for assessing control configuration & technical controls

-   How does the SCS prevent regression in control configurations?
    Examples: built-in controls that cannot change, notifying project
    maintainers when controls change, requiring public declaration of control
    changes.
-   How does the SCS prevent individual project maintainers from tampering with
    controls configured by the project?
-   How does the SCS prevent SCS administrators from tampering with a project's
    configured technical controls?

#### Prompts for assessing the control plane & verifier

NOTE The control plane and verifier perform related roles within the SCS and
should typically be assessed together.

-   Administration
    -   What are the ways an SCS administrator can use privileged access to
        influence a revision creation, provenance generation, or VSA generation?
        Examples: physical access, terminal access, access to cryptographic
        secrets
    -   What controls are in place to detect or prevent an SCS administrator
        from abusing such access? Examples: two-person approvals, audit logging,
        workload identities
    -   Roughly how many SCS maintainers have such access?
    -   How are privileged accounts protected? Examples: two-factor
        authentication, client device security policies
    -   What plans do you have for recovering from security incidents and
        platform outages? Are they tested? How frequently?

-   Control effectiveness
    -   How does the SCS ensure the control plane is enforcing the
        [technical controls](#technical-controls) are working as intended?

-   Source provenance generation
    -   How does the control plane observe the revision creation to ensure the
        provenance's accuracy?
    -   Are there situations in which the control plane will not generate
        source provenance? What are they?
    -   What details are included in the source provenance? Are they sufficient
        to mitigate tampering with other SCS components?

-   VSA generation
    -   How does the verifier determine what source level a revision meets?
    -   How does the verifier determine the organization's control expectations
        and if they are met?

-   Development practices
    -   How do you track the control plane and verifier's software and
        configuration?
        Example: version control.
    -   How do you build confidence in the control plane's software supply
        chain? Example: SLSA Build L3+ provenance, built from SLSA Source L4+
        source.
    -   How do you secure communications between components? Example: TLS with
        certificate transparency.

-   Managing cryptographic secrets
    -   How do you store the control plane and verifier's cryptographic secrets?
    -   Which parts of the organization have access to the control plane and
        verifier's cryptographic secrets?
    -   What controls are in place to detect or prevent SCS administrators from
        abusing such access? Examples: two-person approvals, audit logging
    -   How are secrets protected in memory? Examples: secrets are stored in
        hardware security modules and backed up in secure cold storage
    -   How frequently are cryptographic secrets rotated? Describe the rotation
        process.
    -   What is your plan for remediating cryptographic secret compromise? How
        frequently is this plan tested?

#### Prompts for assessing output storage

-   How do you prevent tampering with storage directly?
-   How do you prevent one project's revisions from affecting another project?

### Source control system evaluation

Organizations can either self-attest to their answers or seek certification from
a third-party auditor. Evidence for self-attestation should be published on
the internet and can include information such as the security model used in the
evaluation. Evidence submitted for third-party certification need not be
published.


---

## Source: Example controls — `source-example-controls.md`

*Locator page:* https://slsa.dev/spec/v1.2/source-example-controls · *Requirements extracted:* R-0144 – R-0161 (18 statements)

> Page description (front matter): "This page provides examples of additional controls that

At SLSA Source L3+ organizations are allowed and encouraged to define their own
controls that go over and above specific requirements outlined by SLSA. This
page provides some examples of what these additional controls could be.

If an organization has indicated that use of these controls is part of
their repository's expectations, consumers SHOULD be able to verify that the
process was followed for the revision they are consuming by examining the
[summary](./source-requirements#source-verification-summary-attestation) or
[source provenance](./source-requirements#source-provenance-attestations)
attestations.

> For example: consumers can look for the related `ORG_SOURCE` properties in
> the `verifiedLevels` field of the [summary
> attestation](./source-requirements#source-verification-summary-attestation).

### Expert Code Review

**Summary:**

All changes to the source are pre-approved by experts.

**Intended for:**

Enterprise repositories and mature open source projects.

**Benefits:**

Prevents mistakes by developers unfamiliar with the area.

#### Requirements

-   **Code ownership**

    Each part of the source MUST have a clearly identified set of experts.

-   **Approvals from all relevant experts**

    For each portion of the source modified by a change proposal, pre-approval
    MUST be granted by a member of the defined expert set. An approval from an
    actor that is a member of multiple expert groups may satisfy the
    requirement for all groups in which they are a member.

### Review Every Single Revision

**Summary:**

The final revision was reviewed by experts prior to submission.

**Intended for:**

The highest-of-high-security-posture repos.

**Benefits:**

Provides maximum chance for experts to spot problems.

#### Requirements

-   **Reset votes on all changes**

    If the proposal is modified after receiving expert approval, all previously
    granted approvals MUST be revoked. A new approval MUST be granted from ALL
    required reviewers.

    The new approval MAY be granted by an actor who approved a previous
    iteration.

### Automated testing

**Summary:**

The final revision was validated by automated tests.

**Intended for:**

All organizations and repositories.

**Benefits:**

Improves accuracy, prevents errors, and reduces human load.

#### Requirements

The organization MUST configure a branch protection rule to require that only
revisions with passing test results can be pointed-to by the branch.

Automatic tests SHOULD be executed in a trustworthy environment (see SLSA
build track).

Results of each test (or an aggregate) MUST be collected by the change review
tool and made available for verification.

Tests SHOULD be run against a revision created for testing by merging the topic
branch (containing the proposed changes) into the target branch.

Use of the proposed merge commit should be preferred to using the tip of the
topic branch.

### Every revision reachable from a branch was approved

**Summary:**

New revisions are created based ONLY on approved changes.

**Intended for:**

All organizations and repositories.

**Benefits:**

Prevents attacks that hide malicious, unreviewed commits.

#### Context

In many organizations, it is normal to review only the "net difference"
between the tip of the topic branch and the "best merge base", the closest
shared commit between the topic and target branches computed at the time of
review.

The topic branch may contain many commits of which not all were intended to
represent a shippable state of the repository.

If a repository merges branches with a standard merge commit, all those
unreviewed commits on the topic branch will become "reachable" from the
protected branch by virtue of the multi-parent merge commit.

When a repo is cloned, all commits _reachable_ from the main branch are
fetched and become accessible from the local checkout.

This combination of factors allows attacks where the victim performs a `git
clone` operation followed by a `git reset --hard <unreviewed revision ID>`.

#### Requirements

-   **Informed Review**

    The reviewer is able and encouraged to make an informed decision about
    what they're approving. The reviewer MUST be presented with a full,
    meaningful content diff between the proposed revision and the
    previously reviewed revision.

    It is not sufficient to indicate that a file changed without showing
    the contents.

-   **Use only rebase operations on the protected branch**

    Require a squash merge strategy for the protected branch.

    To guarantee that only commits representing reviewed diffs are cloned,
    the SCS MUST rebase (or "squash") the reviewed diff into a single new
    commit (the "squashed" commit) that has only a single parent (the
    revision previously pointed-to by the protected branch). This is
    different than a standard merge commit strategy which would cause all
    the user-contributed commits to become reachable from the protected
    branch via the second parent.

    It is not acceptable to replay the sequence of commits from the topic
    branch onto the protected branch. The intent is to reduce the accepted
    changes to the exact diffs that were reviewed. Constituent commits of
    the topic branch may or may not have been reviewed on an individual
    basis, and should not become reachable from the protected branch.

### Immutable Change Discussion

**Summary:**

The discussion around a change is preserved and immutable.

**Intended for:**

Large orgs, or where discussion is vital to change management.

**Benefits:**

Enables future education, forensics, and security auditing.

#### Requirements

The SCS SHOULD record a description of the proposed change and all discussions
/ commentary related to it.

The SCS MUST link this discussion to the revision itself. This is regularly
done via commit metadata.

All collected content SHOULD be made immutable if the change is accepted. It
SHOULD NOT be possible to edit the discussion around a revision after it has
been accepted.

### Merge trains

**Summary:**

A buffer branch (or "train") collects a certain number of approved changes
before merging into the protected branch.

**Intended for:**

Large organizations with high-velocity repositories where the protected branch
needs to remain stable for longer periods.

**Benefits:**

Allows more time for human and automatic code review by stabilizing the
protected branch.

#### Requirements

Large organizations must keep the number of updates to key protected branches
under certain limits to allow time for code review to happen. For example, if
a team tries to merge 60 change requests per hour into the `main` branch, the
tip of the `main` branch would only be stable for about 1 minute. This would
leave only 1 minute for a new diff to be both generated and reviewed before
it becomes stale again.

The normal way to work in this environment is to create a buffer branch
(sometimes called a "train") to collect a certain number of approved changes.
In this model, when a change is approved for submission to the protected
branch, it is added to the train branch instead. After a certain amount of
time, the train branch will be merged into the protected branch. If there are
problems detected with the contents on the train branch, it's normal for the
whole train to be abandoned and a new train to be formed. Approved changes
will be re-applied to a new train in this scenario.

The key benefit to this approach is that the protected branch remains stable
for longer, allowing more time for human and automatic code review. A key
downside to this approach is that organizations will not know the final
revision ID that represents a change until the entire train process completes.

A change review process will now be associated with multiple distinct
revisions.

-   ID 1: The revision which was reviewed before concluding the change review
    process. It represents the ideal state of the protected branch applying
    only this proposed change.
-   ID 2: The revision created when the change is applied to the train branch.
    It represents the state of the protected branch _after other changes have
    been applied_.

It is important to note that no human or automatic review will have the chance
to pre-approve ID2. This will appear to violate any organization policies that
require pre-approval of changes before submission. The SCS and the
organization MUST protect this process in the same way they protect other
artifact build pipelines.

At a minimum the SCS MUST issue an attestation that the revision ID generated
by a merged train is identical ("MERGESAME" in git terminology) to the state
of the protected branch after applying each approved changeset in sequence.
No other content may be added or removed during this process.


---

## Threats & mitigations — `threats.md`

*Locator page:* https://slsa.dev/spec/v1.2/threats · *Requirements extracted:* R-0162 – R-0162 (1 statements)

> Page description (front matter): A comprehensive technical analysis of supply chain threats and their corresponding mitigations in SLSA.

What follows is a comprehensive technical analysis of supply chain threats and
their corresponding mitigations with SLSA and other best practices. For an
introduction to the supply chain threats that SLSA is aiming to protect
against, see [Supply chain threats].

The examples on this page are meant to:

-   Explain the reasons for each of the SLSA [build](build-requirements.md) and
    [source](source-requirements.md) requirements.
-   Increase confidence that the SLSA requirements are sufficient to achieve the
    desired [level](about#how-slsa-works) of integrity protection.
-   Help implementers better understand what they are protecting against so that
    they can better design and implement controls.

### Overview

![Supply Chain Threats](images/supply-chain-threats.svg)

This threat model covers the *software supply chain*, meaning the process by
which software is produced and consumed. We describe and cluster threats based
on where in the software development pipeline those threats occur, labeled (A)
through (I). This is useful because priorities and mitigations mostly cluster
along those same lines. Keep in mind that dependencies are
[highly recursive](#dependency-threats), so each dependency has its own threats
(A) through (I), and the same for *their* dependencies, and so on. For a more
detailed explanation of the supply chain model, see
[Terminology](terminology.md).

Importantly, producers and consumers face *aggregate* risk across all of the
software they produce and consume, respectively. Many organizations produce
and/or consume thousands of software packages, both first- and third-party, and
it is not practical to rely on every individual team in the organization to do
the right thing. For this reason, SLSA prioritizes mitigations that can be
broadly adopted in an automated fashion, minimizing the chance of mistakes.

### Source threats

A source integrity threat is a potential for an adversary to introduce a change
to the source code that does not reflect the intent of the software producer.
This includes modification of the source data at rest as well as insider threats,
when an authorized individual introduces an unauthorized change.

The SLSA Source track mitigates these threats when the consumer
[verifies source](verifying-source.md) against expectations, confirming
that the revision they received was created in the expected manner.

#### (A) Producer

The producer of the software intentionally produces code that harms the
consumer, or the producer otherwise uses practices that are not deserving of the
consumer's trust.

###### Software producer intentionally creates a malicious revision of the source

*Threat:* A producer intentionally creates a malicious revision with the intent of harming their consumers.

*Mitigation:*
This kind of attack cannot be directly mitigated through SLSA controls.
Consumers must establish some basis to trust the organizations from which they consume software.
That basis may be:

-   The repo is open source with an active user-base. High numbers of engaged users may increase the likelihood that bad code is detected during code review and reduce the time-to-detection when bad revisions are accepted.
-   The organization has sufficient legal or reputational incentives to dissuade it from making malicious changes.

Ultimately this is a judgement call with no straightforward answer.

*Example:* A producer with an otherwise good reputation decides suddenly to produce a malicious artifact with the intent to harm their consumers.

#### (B) Modifying the source

An adversary without any special administrator privileges attempts to introduce a change counter to the declared intent of the source by following the producer's official source control process.

Threats in this category can be mitigated by following source control management best practices.

##### (B1) Submit change without review

###### Directly submit without review — (Source L4)

*Threat:* Malicious code submitted to the source repository.

*Mitigation:* Require approval of all changes before they are accepted.

*Example:* Adversary directly pushes a change to a git repo's `main` branch.
Solution: The Source Control System is configured to require two party review for
contributions to the `main` branch.

###### Single actor controls multiple accounts

*Threat:* An actor is able to control multiple account and effectively approve their own code changes.

*Mitigation:* The producer must ensure that no actor is able to control or influence multiple accounts with review privileges.

*Example:* Adversary creates a pull request using a secondary account and approves it using their primary account.
Solution: The producer must track all actors who have both explicit review permissions and the independent ability to control
a privileged bot. A common vector for this attack is to influence a robot account with the permission to review or contribute
code. Control of the robot account and an actor's own personal account is enough to exploit this vulnerability. A common
solution to this flow is to deny bot accounts from contributing or reviewing code, or to require more human reviews in those
cases.

###### Use a robot account to submit change

*Threat:* Exploit a robot account that has the ability to submit changes without
two-person review.

*Mitigation:* All changes require review by two people, even changes authored by
robots.

*Example:* A file within the source repository is automatically generated by a
robot, which is allowed to submit without review.
Adversary compromises the robot and submits a malicious change.
Solution: Require two-person review for such changes, ignoring the robot.

###### Abuse of rule exceptions

*Threat:* Rule exceptions provide vector for abuse.

*Mitigation:* Remove rule exceptions.

*Example:* A producer intends to require two-person review on "all changes except for documentation changes," defined as those only modifying `.md` files.
Adversary submits a malicious executable masquerading as a documentation file, `help.md`.
This avoids the two-person review rule due to the exception.
In the future, a user (or another workflow) can be induced to *execute* `help.md` and become compromised.
Technically the malicious code change met all defined policies yet the intent of the organization was defeated.
Solution: The producer adjusts the rules to prohibit such exceptions.

###### Highly-permissioned actor bypasses or disables controls — (verification)

*Threat:* Trusted actor with "admin" privileges in a repository submits code by disabling existing controls.

*Mitigation:* The Source Control System must have controls in place to prevent
and detect abusive behavior from administrators (e.g. two-person approvals,
audit logging).

*Example:* GitHub repository-level admin removes a branch protection requirement, pushes
their change, then re-enables the requirement to cover their tracks.
Solution: Consumers do not accept claims from the Source Control System unless
they trust sufficient controls are in place to prevent repo admins from
abusing privileges.

##### (B2) Evade change management process

###### Alter change history — (Source L2+)

*Threat:* Adversary alters branch history to hide malicious activity.

*Mitigation:* The Source Control System prevents branch history from being
altered.

*Example:* Adversary submits a malicious commit `X` to the `main` branch. A
release is built and published from `X`. The adversary then "force pushes"
to `main` erasing the record of the malicious commit.  Solution: The Source
Control System is configured to prevent force pushes to `main`.

###### Replace tagged content with malicious content — (Source L2+)

*Threat:* Adversary alters a tag to point at malicious content.

*Mitigation:* The Source Control System does not allow protected tags to be updated.

*Example:* Adversary crafts a malicious commit `X` on a development branch which
does enforce any controls. They then update the `release_1.2` tag to point to
`X`. Consumers of `release_1.2` will get the malicious revision. Solution: The
Source Control System does not allow protected tags to be updated.

###### Skip required checks — (Source L3+)

*Threat:* Code is submitted without following the producers documented
development process, introducing unintended behavior.

*Mitigation:* The producer uses the Source Control System to implement technical
controls ensuring adherence to the development process.

*Example:* An engineer submits a new feature that has a critical flaw on an
untested code path, in violation of the producer's documented process of having
high test coverage. Solution: The producer implements a technical control in the
SCS that requires 95%+ test coverage.

###### Modify code after review — (Source L4)

*Threat:* Modify the code after it has been reviewed but before submission.

*Mitigation:* The Source Control System invalidates approvals whenever the proposed change is modified.

*Example:* Source repository requires two-person review on all changes.
Adversary sends an initial "good" pull request to a peer, who approves it.
Adversary then modifies their proposal to contain "bad" code.

Solution: Configure the code review rules to require review of the most recent revision before submission.

###### Submit a change that is unreviewable — (Source L4)

*Threat:* Adversary crafts a change that looks benign to a reviewer but is actually malicious.

*Mitigation:* Code review system ensures that all reviews are informed and
meaningful to the extent possible. For example the system could show
& resolve symlinks, render images, or verify & display provenance.

*Example:* A proposed change updates a JPEG file to include a malicious
message, but the reviewer is only presented with a diff of the binary
file contents. The reviewer is unable to parse the contents themselves
so they do not have enough context to provide a meaningful review.
Solution: the code review system should present the reviewer with a
rendering of the image and the [embedded
metadata](https://en.wikipedia.org/wiki/Exif), allowing them to make an
informed decision.

###### Copy a reviewed change to another context — (Source L4)

*Threat:* Get a change reviewed in one context and then transfer it to a
different context.

*Mitigation:* Approvals are context-specific.

*Example:* MyPackage's source repository requires two-person review. Adversary
forks the repo, submits a change in the fork with review from a colluding
colleague (who is not trusted by MyPackage), then proposes the change to
the upstream repo.
Solution: The proposed change still requires two-person review in the upstream
context even though it received two-person review in another context.

###### Commit graph attacks

*Threat:* A malicious commit can be included in a sequence of commits such that it does not appear malicious in the net change presented to reviewers.

*Mitigation:* The producer ensures that all revisions in the protected context followed the same contribution process.

*Example:* Adversary sends a pull request containing malicious commit X and a commit Y that undoes X.
The combined change of X + Y displays zero lines of malicious code and the reviewer cannot tell that X is malicious unless they review it individually.
If X is allowed to become reachable from the protected branch, the content may become available in secured environments such as developer machines.

Solution: Each revision in the protected context must have followed the intended process.
Ultimately, this means that either each code review results in at most a single new commit or that the full process is followed for each constituent commit in a proposed sequence.

##### (B3) Render code review ineffective

###### Collude with another trusted person

*Threat:* Two trusted persons collude to author and approve a bad change.

*Mitigation:* This threat is not currently addressed by SLSA, but the producer can arbitrarily increase friction of their policies to reduce risk, such as requiring additional, or more senior reviewers.
The goal of policy here is to ensure that the approved changes match the intention of the producer for the source.
Increasing the friction of the policies may make it harder to circumvent, but doing so has diminishing returns.
Ultimately the producer will need to land upon a balanced risk profile that makes sense for their security posture.

###### Trick reviewer into approving bad code

*Threat:* Construct a change that looks benign but is actually malicious, a.k.a.
"bugdoor."

*Mitigation:* This threat is not currently addressed by SLSA.

###### Reviewer blindly approves changes

*Threat:* Reviewer approves changes without actually reviewing, a.k.a. "rubber
stamping."

*Mitigation:* This threat is not currently addressed by SLSA.

##### (B4) Render change metadata ineffective

###### Forge change metadata — (Source L2+)

*Threat:* Forge the change metadata to alter attribution, timestamp, or
discoverability of a change.

*Mitigation:* The Source Control System only attributes changes to authenticated
identities and records contemporaneous evidence of changes in signed source
provenance attestations.

*Example:* Adversary 'X' creates a commit with unauthenticated metadata claiming
it was authored by 'Y'. Solution: The Source Control System records the identity
of 'X' when 'X' submits the commit to the repository.

#### (C) Source code management

An adversary introduces a change to the source control repository through an
administrative interface, or through a compromise of the underlying
infrastructure.

###### Platform admin abuses privileges — (verification)

*Threat:* Platform administrator abuses their privileges to bypass controls or
to push a malicious version of the software.

*Mitigation:* The source platform must have controls in place to prevent and
detect abusive behavior from administrators (e.g. two-person approvals for
changes to the infrastructure, audit logging). A future [Platform
Operations Track](future-directions#platform-operations-track) may provide
more specific guidance on how to secure the underlying platform.

*Example 1:* GitHostingService employee uses an internal tool to push changes to
the MyPackage source repo.

*Example 2:* GitHostingService employee uses an internal tool to push a
malicious version of the server to serve malicious versions of MyPackage sources
to a specific CI/CD client but the regular version to everyone else, in order to
hide tracks.

*Example 3:* GitHostingService employee uses an internal tool to push a
malicious version of the server that includes a backdoor allowing specific users
to bypass branch protections. Adversary then uses this backdoor to submit a
change to MyPackage without review.

*Solution:* Consumers do not accept claims from the Source Control System unless
they trust sufficient controls are in place to prevent repo admins from
abusing privileges.

###### Exploit vulnerability in SCM

*Threat:* Exploit a vulnerability in the implementation of the source code
management system to bypass controls.

*Mitigation:* This threat is not currently addressed by SLSA.

### Build threats

A build integrity threat is a potential for an adversary to introduce behavior
to an artifact without changing its source code, or to build from a
source, dependency, and/or process that is not intended by the software
producer.

The SLSA Build track mitigates these threats when the consumer
[verifies artifacts](verifying-artifacts.md) against expectations, confirming
that the artifact they received was built in the expected manner.

#### (D) External build parameters

An adversary builds from a version of the source code that does not match the
official source control repository, or changes the build parameters to inject
behavior that was not intended by the official source.

The mitigation here is to compare the provenance against expectations for the
package, which depends on SLSA Build L1 for provenance. (Threats against the
provenance itself are covered by (E) and (F).)

###### Build from unofficial fork of code — (expectations)

*Threat:* Build using the expected CI/CD process but from an unofficial fork of
the code that may contain unauthorized changes.

*Mitigation:* Verifier requires the provenance's source location to match an
expected value.

*Example:* MyPackage is supposed to be built from GitHub repo `good/my-package`.
Instead, it is built from `evilfork/my-package`. Solution: Verifier rejects
because the source location does not match.

###### Build from unofficial branch or tag — (expectations)

*Threat:* Build using the expected CI/CD process and source location, but
checking out an "experimental" branch or similar that may contain code not
intended for release.

*Mitigation:* Verifier requires that the provenance's source branch/tag matches
an expected value, or that the source revision is reachable from an expected
branch.

*Example:* MyPackage's releases are tagged from the `main` branch, which has
branch protections. Adversary builds from the unprotected `experimental` branch
containing unofficial changes. Solution: Verifier rejects because the source
revision is not reachable from `main`.

###### Build from unofficial build steps — (expectations)

*Threat:* Build the package using the proper CI/CD platform but with unofficial
build steps.

*Mitigation:* Verifier requires that the provenance's build configuration source
matches an expected value.

*Example:* MyPackage is expected to be built by Google Cloud Build using the
build steps defined in the source's `cloudbuild.yaml` file. Adversary builds
with Google Cloud Build, but using custom build steps provided over RPC.
Solution: Verifier rejects because the build steps did not come from the
expected source.

###### Build from unofficial parameters — (expectations)

*Threat:* Build using the expected CI/CD process, source location, and
branch/tag, but using a parameter that injects unofficial behavior.

*Mitigation:* Verifier requires that the provenance's external parameters all
match expected values.

*Example 1:* MyPackage is supposed to be built from the `release.yml` workflow.
Adversary builds from the `debug.yml` workflow. Solution: Verifier rejects
because the workflow parameter does not match the expected value.

*Example 2:* MyPackage's GitHub Actions Workflow uses `github.event.inputs` to
allow users to specify custom compiler flags per invocation. Adversary sets a
compiler flag that overrides a macro to inject malicious behavior into the
output binary. Solution: Verifier rejects because the `inputs` parameter was not
expected.

###### Build from modified version of code modified after checkout — (expectations)

*Threat:* Build from a version of the code that includes modifications after
checkout.

*Mitigation:* Build platform pulls directly from the source repository and
accurately records the source location in provenance.

*Example:* Adversary fetches from MyPackage's source repo, makes a local commit,
then requests a build from that local commit. Builder records the fact that it
did not pull from the official source repo. Solution: Verifier rejects because
the source repo does not match the expected value.

#### (E) Build process

An adversary introduces an unauthorized change to a build output through
tampering of the build process; or introduces false information into the
provenance.

These threats are directly addressed by the SLSA Build track.

###### Forge values of the provenance (other than output digest) — (Build L2+)

*Threat:* Generate false provenance and get the trusted control plane to sign
it.

*Mitigation:* At Build L2+, the trusted control plane [generates][authentic] all
information that goes in the provenance, except (optionally) the output artifact
hash. At Build L3+, this is [hardened][unforgeable] to prevent compromise even
by determined adversaries.

*Example 1 (Build L2):* Provenance is generated on the build worker, which the
adversary has control over. Adversary uses a malicious process to get the build
platform to claim that it was built from source repo `good/my-package` when it
was really built from `evil/my-package`. Solution: Builder generates and signs
the provenance in the trusted control plane; the worker reports the output
artifacts but otherwise has no influence over the provenance.

*Example 2 (Build L3):* Provenance is generated in the trusted control plane,
but workers can break out of the container to access the signing material.
Solution: Builder is hardened to provide strong isolation against tenant
projects.

###### Forge output digest of the provenance — (n/a)  `#forged-digest`

*Threat:* The tenant-controlled build process sets output artifact digest
(`subject` in SLSA Provenance) without the trusted control plane verifying that
such an artifact was actually produced.

*Mitigation:* None; this is not a problem. Any build claiming to produce a given
artifact could have actually produced it by copying it verbatim from input to
output.[^preimage] (Reminder: Provenance is only a claim that a particular
artifact was *built*, not that it was *published* to a particular registry.)

*Example:* A legitimate MyPackage artifact has digest `abcdef` and is built
from source repo `good/my-package`. A malicious build from source repo
`evil/my-package` claims that it built artifact `abcdef` when it did not.
Solution: Verifier rejects because the source location does not match; the
forged digest is irrelevant.

[^preimage]: Technically this requires the artifact to be known to the
    adversary. If they only know the digest but not the actual contents, they
    cannot actually build the artifact without a [preimage attack] on the digest
    algorithm. However, even still there are no known concerns where this is a
    problem.

[preimage attack]: https://en.wikipedia.org/wiki/Preimage_attack

###### Compromise project owner — (Build L2+)

*Threat:* An adversary gains owner permissions for the artifact's build project.

*Mitigation:* The build project owner must not have the ability to influence the
build process or provenance generation.

*Example:* MyPackage is built on Awesome Builder under the project "mypackage".
Adversary is an owner of the "mypackage" project. Awesome Builder allows
owners to debug the build environment via SSH. An adversary uses this feature
to alter a build in progress. Solution: Build L3 requires the external parameters
to be complete in the provenance. The attackers access and/or actions within the
SSH connection would be enumerated within the external parameters. The updated
external parameters will not match the declared expectations causing verification
to fail.

###### Compromise other build — (Build L3)

*Threat:* Perform a malicious build that alters the behavior of a benign
build running in parallel or subsequent environments.

*Mitigation:* Builds are [isolated] from one another, with no way for one to
affect the other or persist changes.

*Example 1:* A build platform runs all builds for project MyPackage on
the same machine as the same Linux user. An adversary starts a malicious build
that listens for another build and swaps out source files, then starts a benign
build. The benign build uses the malicious build's source files, but its
provenance says it used benign source files. Solution: The build platform
changes architecture to isolate each build in a separate VM or similar.

*Example 2:* A build platform uses the same machine for subsequent
builds. An adversary first runs a build that replaces the `make` binary with a
malicious version, then subsequently runs an otherwise benign build. Solution:
The builder changes architecture to start each build with a clean machine image.

###### Steal cryptographic secrets — (Build L3)

*Threat:* Use or exfiltrate the provenance signing key or some other
cryptographic secret that should only be available to the build platform.

*Mitigation:* Builds are [isolated] from the trusted build platform control
plane, and only the control plane has [access][unforgeable] to cryptographic
secrets.

*Example:* Provenance is signed on the build worker, which the adversary has
control over. Adversary uses a malicious process that generates false provenance
and signs it using the provenance signing key. Solution: Builder generates and
signs provenance in the trusted control plane; the worker has no access to the
key.

###### Poison the build cache — (Build L3)

*Threat:* Add a malicious artifact to a build cache that is later picked up by a
benign build process ([example][build-cache-poisoning-example]).

*Mitigation:* Build caches must be [isolated][isolated] between builds to prevent
such cache poisoning attacks. In particular, the cache SHOULD be keyed by the
transitive closure of all inputs to the cached artifact, and the cache must
either be only writable by the trusted control plane or have SLSA Build L3
provenance for each cache entry.

*Example 1:* The cache key does not fully cover the transitive closure of all
inputs and instead only uses the digest of the source file itself. Adversary runs
a build over `auth.cc` with command line flags to gcc that define a marco
replacing `CheckAuth(ctx)` with `true`. When subsequent builds build `auth.cc`
they will get the attacker's poisoned instance that does not call `CheckAuth`.
Solution: Build cache is keyed by digest of `auth.cc`, command line, and digest of
gcc so changing the command line flags results in a different cache entry.

*Example 2:* The tenant controlled build process has full write access to the
cache. Adversary observes a legitimate build of `auth.cc` which covers the
transitive closure of all inputs and notes the digest used for caching. The
adversary builds a malicious version of `auth.o` and directly writes it to the
build cache using the observed digest. Subsequent legitimate builds will use
the malicious version of `auth.o`. Solution: Each cache entry is keyed by the
transitive closure of the inputs, and the cache entry is itself a SLSA Build L3
build with its own provenance that corresponds to the key.

###### Compromise build platform admin — (verification)

*Threat:* An adversary gains admin permissions for the artifact's build platform.

*Mitigation:* The build platform must have controls in place to prevent and
detect abusive behavior from administrators (e.g. two-person approvals, audit
logging).

*Example:* MyPackage is built on Awesome Builder. Awesome Builder allows
engineers on-call to SSH into build machines to debug production issues. An
adversary uses this access to modify a build in progress. Solution: Consumers
do not accept provenance from the build platform unless they trust sufficient
controls are in place to prevent abusing admin privileges.

#### (F) Artifact publication

An adversary uploads a package artifact that does not reflect the intent of the
package's official source control repository.

This is the most direct threat because it is the easiest to pull off. If there
are no mitigations for this threat, then (D) and (E) are often indistinguishable
from this threat.

###### Build with untrusted CI/CD — (expectations)

*Threat:* Build using an unofficial CI/CD pipeline that does not build in the
correct way.

*Mitigation:* Verifier requires provenance showing that the builder matched an
expected value.

*Example:* MyPackage is expected to be built on Google Cloud Build, which is
trusted up to Build L3. Adversary builds on SomeOtherBuildPlatform, which is only
trusted up to Build L2, and then exploits SomeOtherBuildPlatform to inject
malicious behavior. Solution: Verifier rejects because builder is not as
expected.

###### Upload package without provenance — (Build L1)

*Threat:* Upload a package without provenance.

*Mitigation:* Verifier requires provenance before accepting the package.

*Example:* Adversary uploads a malicious version of MyPackage to the package
repository without provenance. Solution: Verifier rejects because provenance is
missing.

###### Tamper with artifact after CI/CD — (Build L1)

*Threat:* Take a benign version of the package, modify it in some way, then
re-upload it using the original provenance.

*Mitigation:* Verifier checks that the provenance's `subject` matches the hash
of the package.

*Example:* Adversary performs a proper build, modifies the artifact, then
uploads the modified version of the package to the repository along with the
provenance. Solution: Verifier rejects because the hash of the artifact does not
match the `subject` found within the provenance.

###### Tamper with provenance — (Build L2)

*Threat:* Perform a build that would not meet expectations, then modify the
provenance to make the expectations checks pass.

*Mitigation:* Verifier only accepts provenance with a valid [cryptographic
signature][authentic] or equivalent proving that the provenance came from an
acceptable builder.

*Example:* MyPackage is expected to be built by GitHub Actions from the
`good/my-package` repo. Adversary builds with GitHub Actions from the
`evil/my-package` repo and then modifies the provenance so that the source looks
like it came from `good/my-package`. Solution: Verifier rejects because the
cryptographic signature is no longer valid.

#### (G) Distribution channel

An adversary modifies the package on the package registry using an
administrative interface or through a compromise of the infrastructure
including modification of the package in transit to the consumer.

The distribution channel threats and mitigations look very similar to the
Artifact Publication (F) threats and mitigations with the main difference
being that these threats are mitigated by having the *consumer* perform
verification.

The consumer's actions may be simplified if (F) produces a [VSA][vsa].
In this case the consumer may replace provenance verification with
[VSA verification][vsa_verification].

###### Build with untrusted CI/CD — (expectations)

*Threat:* Replace the package with one built using an unofficial CI/CD pipeline
that does not build in the correct way.

*Mitigation:* Verifier requires provenance showing that the builder matched an
expected value or a VSA for corresponding `resourceUri`.

*Example:* MyPackage is expected to be built on Google Cloud Build, which is
trusted up to Build L3. Adversary builds on SomeOtherBuildPlatform, which is only
trusted up to Build L2, and then exploits SomeOtherBuildPlatform to inject
malicious behavior. Adversary then replaces the original package within the
repository with the malicious package. Solution: Verifier rejects because
builder is not as expected.

###### Issue VSA from untrusted intermediary — (expectations)

*Threat:* Have an unofficial intermediary issue a VSA for a malicious package.

*Mitigation*: Verifier requires VSAs to be issued by a trusted intermediary.

*Example:* Verifier expects VSAs to be issued by TheRepository. Adversary
builds a malicious package and then issues a VSA of their own for the malicious
package. Solution: Verifier rejects because they only accept VSAs from
TheRepository which the adversary cannot issue since they do not have the
corresponding signing key.

###### Upload package without provenance or VSA — (Build L1)

*Threat:* Replace the original package with a malicious one without provenance.

*Mitigation:* Verifier requires provenance or a VSA before accepting the package.

*Example:* Adversary replaces MyPackage with a malicious version of MyPackage
on the package repository and deletes existing provenance. Solution: Verifier
rejects because provenance is missing.

###### Replace package and VSA with another — (expectations)

*Threat:* Replace a package and its VSA with a malicious package and its valid VSA.

*Mitigation*: Consumer ensures that the VSA matches the package they've requested (not just the package they received) by following the [verification process](verification_summary#how-to-verify).

*Example:* Adversary uploads a malicious package to `repo/evil-package`,
getting a valid VSA for `repo/evil-package`. Adversary then replaces
`repo/my-package` and its VSA with `repo/evil-package` and its VSA.
Solution: Verifier rejects because the VSA `resourceUri` field lists
`repo/evil-package` and not the expected `repo/my-package`.

###### Tamper with artifact after upload — (Build L1)

*Threat:* Take a benign version of the package, modify it in some way, then
replace it while retaining the original provenance or VSA.

*Mitigation:* Verifier checks that the provenance or VSA's `subject` matches
the hash of the package.

*Example:* Adversary performs a proper build, modifies the artifact, then
replaces the modified version of the package in the repository and retains the
original provenance. Solution: Verifier rejects because the hash of the
artifact does not match the `subject` found within the provenance.

###### Tamper with provenance or VSA — (Build L2)

*Threat:* Perform a build that would not meet expectations, then modify the
provenance or VSA to make the expectations checks pass.

*Mitigation:* Verifier only accepts provenance or VSA with a valid [cryptographic
signature][authentic] or equivalent proving that the provenance came from an
acceptable builder or the VSA came from an expected verifier.

*Example 1:* MyPackage is expected to be built by GitHub Actions from the
`good/my-package` repo. Adversary builds with GitHub Actions from the
`evil/my-package` repo and then modifies the provenance so that the source looks
like it came from `good/my-package`. Solution: Verifier rejects because the
cryptographic signature is no longer valid.

*Example 2:* Verifier expects VSAs to be issued by TheRepository. Adversary
builds a malicious package and then modifies the original VSA's `subject`
field to match the digest of the malicious package. Solution: Verifier rejects
because the cryptographic signature is no longer valid.

### Usage threats

A usage threat is a potential for an adversary to exploit behavior of the
consumer.

#### (H) Package selection

The consumer requests a package that it did not intend.

###### Dependency confusion

*Threat:* Register a package name in a public registry that shadows a name used
on the victim's internal registry, and wait for a misconfigured victim to fetch
from the public registry instead of the internal one.

*Mitigation:* The mitigation is for the software producer to build internal
packages on a SLSA Level 2+ compliant build system and define expectations for
build provenance. Expectations must be verified on installation of the internal
packages. If a misconfigured victim attempts to install attacker's package with
an internal name but from the public registry, then verification against
expectations will fail.

For more information see [Verifying artifacts](verifying-artifacts.md)
and [Defender's Perspective: Dependency Confusion and Typosquatting Attacks](/blog/2024/08/dep-confusion-and-typosquatting).

###### Typosquatting

*Threat:* Register a package name that is similar looking to a popular package
and get users to use your malicious package instead of the benign one.

*Mitigation:* This threat is not currently addressed by SLSA. That said, the
requirement to make the source available can be a mild deterrent, can aid
investigation or ad-hoc analysis, and can complement source-based typosquatting
solutions.

#### (I) Usage

The consumer uses a package in an unsafe manner.

###### Improper usage

*Threat:* The software can be used in an insecure manner, allowing an
adversary to compromise the consumer.

*Mitigation:* This threat is not addressed by SLSA, but may be addressed by
efforts like [Secure by Design][secure-by-design].

### Dependency threats

A dependency threat is a potential for an adversary to introduce unintended
behavior in one artifact by compromising some other artifact that the former
depends on at build time. (Runtime dependencies are excluded from the model, as
[noted below](#runtime-dep).)

Unlike other threat categories, dependency threats develop recursively through
the supply chain and can only be exploited indirectly. For example, if
application *A* includes library *B* as part of its build process, then a build
or source threat to *B* is also a dependency threat to *A*. Furthermore, if
library *B* uses build tool *C*, then a source or build threat to *C* is also a
dependency threat to both *A* and *B*.

This version of SLSA does not explicitly address dependency threats, but we
expect that a future version will. In the meantime, you can [apply SLSA
recursively] to your dependencies in order to reduce the risk of dependency
threats.

[apply SLSA recursively]: verifying-artifacts.md#step-3-optional-check-dependencies-recursively

#### Build dependency

An adversary compromises the target artifact through one of its build
dependencies. Any artifact that is present in the build environment and has the
ability to influence the output is considered a build dependency.

###### Include a vulnerable dependency (library, base image, bundled file, etc.)  `#included-dep`

*Threat:* Statically link, bundle, or otherwise include an artifact that is
compromised or has some vulnerability, causing the output artifact to have the
same vulnerability.

*Example:* The C++ program MyPackage statically links libDep at build time. A
contributor accidentally introduces a security vulnerability into libDep. The
next time MyPackage is built, it picks up and includes the vulnerable version of
libDep, resulting in MyPackage also having the security vulnerability.

*Mitigation:* A future
[Dependency track](../../current-activities#dependency-track) may
provide more comprehensive guidance on how to address more specfiic
aspects of this threat.

###### Use a compromised build tool (compiler, utility, interpreter, OS package, etc.)  `#build-tool`

*Threat:* Use a compromised tool or other software artifact during the build
process, which alters the build process and injects unintended behavior into the
output artifact.

*Mitigation:* This can be partially mitigated by treating build tooling,
including OS images, as any other artifact to be verified prior to use.
The threats described in this document apply recursively to build tooling
as do the mitigations and examples.  A future
[Build Environment track](../../current-activities#build-environment-track) may
provide more comprehensive guidance on how to address more specfiic
aspects of this threat.

*Example:* MyPackage is a tarball containing an ELF executable, created by
running `/usr/bin/tar` during its build process. An adversary compromises the
`tar` OS package such that `/usr/bin/tar` injects a backdoor into every ELF
executable it writes. The next time MyPackage is built, the build picks up the
vulnerable `tar` package, which injects the backdoor into the resulting
MyPackage artifact.  Solution: [apply SLSA recursively] to all build tools
prior to the build.  The build platform verifies the disk image,
or the individual components on the disk image, against the associated
provenance or VSAs prior to running a build.  Depending on where the initial
compromise took place (i.e. before/during vs *after* the build of the build tool itself), the modified `/usr/bin/tar` will fail this verification.

###### Use a compromised runtime dependency during the build (for tests, dynamic linking, etc.)  `#runtime-dep-at-build-time`

*Threat:* During the build process, use a compromised runtime dependency (such
as during testing or dynamic linking), which alters the build process and
injects unwanted behavior into the output.

**NOTE:** This is technically the same case as [Use a compromised build
tool](#build-tool). We call it out to remind the reader that
[runtime dependencies](#runtime-dep) can become build dependencies if they are
loaded during the build.

*Example:* MyPackage has a runtime dependency on package Dep, meaning that Dep
is not included in MyPackage but required to be installed on the user's machine
at the time MyPackage is run. However, Dep is also loaded during the build
process of MyPackage as part of a test. An adversary compromises Dep such that,
when run during a build, it injects a backdoor into the output artifact. The
next time MyPackage is built, it picks up and loads Dep during the build
process. The malicious code then injects the backdoor into the new MyPackage
artifact.

*Mitigation:* In addition to all the mitigations for build tools, you can often
avoid runtime dependencies becoming build dependencies by isolating tests to a
separate environment that does not have write access to the output artifact.

#### Related threats

The following threats are related to "dependencies" but are not modeled as
"dependency threats".

###### Use a compromised dependency at runtime — (modeled separately)  `#runtime-dep`

*Threat:* Load a compromised artifact at runtime, thereby compromising the user
or environment where the software ran.

*Example:* MyPackage lists package Dep as a runtime dependency. Adversary
publishes a compromised version of Dep that runs malicious code on the user's
machine when Dep is loaded at runtime. An end user installs MyPackage, which in
turn installs the compromised version of Dep. When the user runs MyPackage, it
loads and executes the malicious code from Dep.

*Mitigation:* N/A - SLSA's
threat model does not explicitly model runtime dependencies. Instead, each
runtime dependency is considered a distinct artifact with its own threats.

### Availability threats

An availability threat is a potential for an adversary to deny someone from
reading a source and its associated change history, or from building a package.

SLSA does not currently address availability threats, though future versions might.

###### Delete the code

*Threat:* Perform a build from a particular source revision and then delete that
revision or cause it to get garbage collected, preventing anyone from inspecting
the code.

*Mitigation:* This threat is not currently addressed by SLSA.

###### A dependency becomes temporarily or permanently unavailable to the build process

*Threat:* Unable to perform a build with the intended dependencies.

*Mitigation:* This threat is not currently addressed by SLSA. That said, some
solutions to support hermetic and reproducible builds may also reduce the
impact of this threat.

###### De-list artifact

*Threat:* The package registry stops serving the artifact.

*Mitigation:* This threat is not currently addressed by SLSA.

###### De-list provenance

*Threat:* The package registry stops serving the provenance.

*Mitigation:* This threat is not currently addressed by SLSA.

### Verification threats

Threats that can compromise the ability to prevent or detect the supply chain
security threats above.

###### Tamper with recorded expectations

*Threat:* Modify the verifier's recorded expectations, causing the verifier to
accept an unofficial package artifact.

*Mitigation:* Changes to recorded expectations requires some form of
authorization, such as two-party review.

*Example:* The package ecosystem records its expectations for a given package
name in a configuration file that is modifiable by that package's producer. The
configuration for MyPackage expects the source repository to be
`good/my-package`. The adversary modifies the configuration to also accept
`evil/my-package`, and then builds from that repository and uploads a malicious
version of the package. Solution: Changes to the recorded expectations require
two-party review.

###### Exploit cryptographic hash collisions

*Threat:* Exploit a cryptographic hash collision weakness to bypass one of the
other controls.

*Mitigation:* Choose secure algorithms when using cryptographic digests, such
as SHA-256.

*Examples:* Attacker crafts a malicious file with the same MD5 hash as a target
benign file. Attacker replaces the benign file with the malicious file.
Solution: Only accept cryptographic hashes with strong collision resistance.

[apply SLSA recursively]: verifying-artifacts.md#step-3-optional-check-dependencies-recursively
[authentic]: build-requirements.md#provenance-authentic
[build-cache-poisoning-example]: https://adnanthekhan.com/2024/05/06/the-monsters-in-your-build-cache-github-actions-cache-poisoning/
[exists]: build-requirements.md#provenance-exists
[isolated]: build-requirements.md#isolated
[unforgeable]: build-requirements.md#provenance-unforgeable
[secure-by-design]: https://www.cisa.gov/securebydesign
[supply chain threats]: threats-overview
[vsa]: verification_summary
[vsa_verification]: verification_summary#how-to-verify


---

## SLSA Verified Properties — `verified-properties.md`

*Locator page:* https://slsa.dev/spec/v1.2/verified-properties · *Requirements extracted:* R-0163 – R-0166 (4 statements)

> Page description (front matter): |

While SLSA is typically focused on expressing the security state of an artifact
with [levels](principles#simple-levels-with-clear-outcomes), levels may not be
appropriate in all cases. Some software supply chain controls don't fit neatly
within existing SLSA levels or that do may exist with others that users are not
yet able to meet.  SLSA Verified Properties allows a common way to express those
properties (and their requirements) without needing to fit them into existing
levels or introduce new tracks.

These properties MAY be included in the `verifiedLevels` field of
[verification_summaries (VSAs)](verification_summary) when the VSA issuer
determines the requirements have been met.

### SLSA_SOURCE_TWO_PARTY_REVIEWED

Indicates the source code associated with this artifact has been reviewed by
two trusted persons.  This property MUST only be issued in accordance with the
[Source Track](source-requirements)'s
[two-party-review](source-requirements#two-party-review) requirements.

The property MAY be added at any source level in which an SCS can make this
claim.

### SLSA_BUILD_REPRODUCED

Indicates the referenced artifact has been reproduced by two or more builders.

This property MUST only be issued if the referenced artifact has
[build provenance](build-provenance) from two or more independently
operated [Build Platforms](build-requirements#build-platform) which are
trusted by the VSA issuer.


---

## Software attestations — `attestation-model.md`

*Locator page:* https://slsa.dev/spec/v1.2/attestation-model · *Requirements extracted:* R-0167 – R-0176 (10 statements)

> Page description (front matter): A software attestation is an authenticated statement (metadata) about a software artifact or collection of software artifacts. The primary intended use case is to feed into automated policy engines, such as in-toto and Binary Authorization. This page provides a high-level overview of the attestation model, including standardized terminology, data model, layers, and conventions for software attestations.

A software attestation is an authenticated statement (metadata) about a
software artifact or collection of software artifacts.
The primary intended use case is to feed into automated policy engines, such as
[in-toto] and [Binary Authorization].

This page provides a high-level overview of the attestation model, including
standardized terminology, data model, layers, conventions for software
attestations, and formats for different use cases.

### Overview

A **software attestation**, not to be confused with a [remote attestation] in
the trusted computing world, is an authenticated statement (metadata) about a
software artifact or collection of software artifacts. Software attestations
are a generalization of raw artifact/code signing.

With raw signing, a signature is directly over the artifact (or a hash of the
artifact) and *implies* a single bit of metadata about the artifact, based on
the public key. The exact meaning MUST be negotiated between signer and
verifier, and a new keyset MUST be provisioned for each bit of information. For
example, a signature might denote who produced an artifact, or it might denote
fitness for some purpose, or something else entirely.

With an attestation, the metadata is *explicit* and the signature only denotes
who created the attestation (authenticity). A single keyset can express an
arbitrary amount of information, including things that are not possible with
raw signing. For example, an attestation might state exactly how an artifact
was produced, including the build command that was run and all of its
dependencies (as in the case of SLSA [Provenance]).

### Formats

This section explains how to choose the attestation format that's best suited
for your situation by considering factors such as intended use and who will be
consuming the attestation.

#### First party

Producers of first-party code might consider the following questions:

-   Will SLSA be used only within our organization?
-   Is SLSA's primary use case to manage insider risk?
-   Are we developing entirely in a closed-source environment?

If these are the main considerations, the organization can choose any format
for internal use. To make an external claim of meeting a SLSA level, however,
there needs to be a way for external users to consume and verify your provenance.
Currently, SLSA recommends using the [SLSA Provenance format] for SLSA
attestations since it is easy to verify using the [Generic SLSA Verifier].

#### Open source

Producers of open-source code might consider these questions:

-   Is SLSA's primary use case to convey trust in how your code was developed?
-   Do you develop software with standard open-source licenses?
-   Will the code be consumed by others?

In these situations, we encourage you to use the [SLSA Provenance format]. The SLSA
Provenance format offers a path towards interoperability and cohesion across the open
source ecosystem. Users can verify any provenance statement in this format
using the [Generic SLSA Verifier].

#### Closed source, third party

Producers of closed-source code that is consumed by others might consider
the following questions:

-   Is my code produced for the sole purpose of specific third-party consumers?
-   Is SLSA's primary use case to create trust in our organization or to comply with
audits and legal requirements?

In these situations, you might not want to make all the details of your
provenance available externally. Consider using Verification Summary
Attestations (VSAs) to summarize provenance information in a sanitized way
that's safe for external consumption. For more about VSAs, see the [Verification
Summary Attestation] page.

### Model and Terminology

We define the following model to represent any software attestations, regardless
of format. Not all formats will have all fields or all layers, but to be called
a "software attestation" it MUST fit this general model.

The key words MUST, SHOULD, and MAY are to be interpreted as described in
[RFC 2119].

![Attestation model diagram](/images/attestation_layers.svg)

An example of an attestation in English follows with the components of the
attestation mapped to the component names (and colors from the model diagram above):

![Attestation model to English mapping](/images/attestation_example_english.svg)

Components:

-   **Artifact:** Immutable blob of data described by an attestation, usually
    identified by cryptographic content hash. Examples: file content, git
    commit, container digest. MAY also include a mutable locator, such as
    a package name or URI.
-   **Attestation:** Authenticated, machine-readable metadata about one or more
    software artifacts. An attestation MUST contain at least:
    -   **Envelope:** Authenticates the message. At a minimum, it MUST contain:
        -   **Message:** Content (statement) of the attestation. The message
            type SHOULD be authenticated and unambiguous to avoid confusion
            attacks.
        -   **Signature:** Denotes the **attester** who created the attestation.
    -   **Statement:** Binds the attestation to a particular set of artifacts.
        This is a separate layer to allow for predicate-agnostic processing
        and storage/lookup. MUST contain at least:
        -   **Subject:** Identifies which artifacts the predicate applies to.
        -   **Predicate:** Metadata about the subject. The predicate type SHOULD
            be explicit to avoid misinterpretation.
    -   **Predicate:** Arbitrary metadata in a predicate-specific schema. MAY
        contain:
        -   **Link:** *(repeated)* Reference to a related artifact, such as
            build dependency. Effectively forms a [hypergraph] where the
            nodes are artifacts and the hyperedges are attestations. It is
            helpful for the link to be standardized to allow predicate-agnostic
            graph processing.
-   **Bundle:** A collection of Attestations, which are usually but not
    necessarily related.
-   **Storage/Lookup:** Convention for where attesters place attestations and
    how verifiers find attestations for a given artifact.

### Recommended Suite

We recommend a single suite of formats and conventions that work well together
and have desirable security properties. Our hope is to align the industry around
this particular suite because it makes everything easier. That said, we
recognize that other choices MAY be necessary in various cases.

| Component | Recommendation
| --- | ---
| Envelope | **[DSSE]** (ECDSA over NIST P-256 (or stronger) and SHA-256.)
| Statement | **[in-toto attestations]**
| Predicate | Choose as appropriate, i.e.; [Provenance], [SPDX], [other predicates defined by third-parties]. If none are a good fit, invent a new one
| Bundle | **[JSON Lines]**, see [attestation bundle]
| Storage/Lookup | **TBD**

[attestation bundle]: https://github.com/in-toto/attestation/blob/main/spec/v1/bundle.md
[Binary Authorization]: https://cloud.google.com/binary-authorization
[DSSE]: https://github.com/secure-systems-lab/dsse/
[Generic SLSA Verifier]: https://github.com/slsa-framework/slsa-verifier
[hypergraph]: https://en.wikipedia.org/wiki/Hypergraph
[in-toto]: https://in-toto.io
[in-toto attestations]: https://github.com/in-toto/attestation/
[JSON Lines]: https://jsonlines.org/
[other predicates defined by third-parties]: https://github.com/in-toto/attestation/issues/98
[Provenance]: build-provenance
[remote attestation]: https://en.wikipedia.org/wiki/Trusted_Computing#Remote_attestation
[RFC 2119]: https://tools.ietf.org/html/rfc2119
[SLSA Provenance format]: /provenance/v1
[sigstore/cosign]: https://github.com/sigstore/cosign
[SPDX]: https://github.com/in-toto/attestation/blob/main/spec/predicates/spdx.md
[Verification Summary Attestation]: /verification_summary/v1


---

## Build: Provenance — `build-provenance.md`

*Locator page:* https://slsa.dev/spec/v1.2/build-provenance · *Requirements extracted:* R-0177 – R-0225 (49 statements)

> Page description (front matter): Description of SLSA build provenance specification for verifying where, when, and how something was produced.

To trace software back to the source and define the moving parts in a complex
supply chain, provenance needs to be there from the very beginning. It's the
verifiable information about software artifacts describing where, when, and how
something was produced. For higher SLSA levels and more resilient integrity
guarantees, provenance requirements are stricter and need a deeper, more
technical understanding of the predicate.

This document defines the following predicate type within the [in-toto
attestation] framework:

```json
"predicateType": "https://slsa.dev/provenance/v1"
```

> Important: Always use the above string for `predicateType` rather than what is
> in the URL bar. The `predicateType` URI will always resolve to the latest
> minor version of this specification. See [parsing rules](#parsing-rules) for
> more information.

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD",
"SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be
interpreted as described in [RFC 2119](https://www.rfc-editor.org/rfc/rfc2119).

### Purpose

Describe how an artifact or set of artifacts was produced so that:

-   Consumers of the provenance can verify that the artifact was built according
    to expectations.
-   Others can rebuild the artifact, if desired.

This predicate is the RECOMMENDED way to satisfy the SLSA v1.0 [provenance
requirements](requirements#provenance-generation).

### Model

Provenance is an attestation that a particular build platform produced a set of
software artifacts through execution of the `buildDefinition`.

![Build Model](images/provenance-model.svg)

> NOTE: This diagram depicts how the SLSA Provenance format is structured.  It
> elaborates on the [SLSA Build Model](terminology#build-model) but only applies
> to the SLSA Provenance format specifically and not to builds in general.

The model is as follows:

-   Each build runs as an independent process on a multi-tenant build platform.
    The `builder.id` identifies this platform, representing the transitive
    closure of all entities that are [trusted] to faithfully run the build and
    record the provenance. (Note: The same model can be used for platform-less
    or single-tenant build platforms.)

    -   The build platform implementer SHOULD define a security model for the build
        platform in order to clearly identify the platform's boundaries, actors,
        and interfaces. This model SHOULD then be used to identify the transitive
        closure of the trusted build platform for the `builder.id` as well as the
        trusted control plane.

-   The build process is defined by a parameterized template, identified by
    `buildType`. This encapsulates the process that ran, regardless of what
    platform ran it. Often the build type is specific to the build platform
    because most build platforms have their own unique interfaces.

-   All top-level, independent inputs are captured by the parameters to the
    template. There are two types of parameters:

    -   `externalParameters`: the external interface to the build. In SLSA,
        these values are untrusted; they MUST be included in the provenance and
        MUST be verified downstream.

    -   `internalParameters`: set internally by the platform. In SLSA, these
        values are trusted because the platform is trusted; they are OPTIONAL
        and need not be verified downstream. They MAY be included to enable
        reproducible builds, debugging, or incident response.

-   All artifacts fetched during initialization or execution of the build
    process are considered dependencies, including those referenced directly by
    parameters. The `resolvedDependencies` captures these dependencies, if
    known. For example, a build that takes a git repository URI as a parameter
    might record the specific git commit that the URI resolved to as a
    dependency.

-   During execution, the build process might communicate with the build
    platform's control plane and/or build caches. This communication is not
    captured directly in the provenance, but is instead implied by `builder.id`
    and subject to [SLSA Requirements](requirements.md). Such
    communication SHOULD NOT influence the definition of the build; if it does,
    it SHOULD go in `resolvedDependencies` instead.

-   Finally, the build process outputs one or more artifacts, identified by
    `subject`.

For concrete examples, see [index of build types](#index-of-build-types).

### Parsing rules

This predicate follows the in-toto attestation [parsing rules]. Summary:

-   Consumers MUST ignore unrecognized fields unless otherwise noted.
-   The `predicateType` URI includes the major version number and will always
    change whenever there is a backwards incompatible change.
-   Minor version changes are always backwards compatible and "monotonic."
    Such changes do not update the `predicateType`.
-   Unset, null, and empty field values MUST be interpreted equivalently.

### Schema

#### Summary

*NOTE: This summary (in cue) is informative. In the event of a
disagreement with the text description, the text is authoritative.*

```javascript
{
    // Standard attestation fields:
    "_type": "https://in-toto.io/Statement/v1",
    "subject": [...],

    // Predicate:
    "predicateType": "https://slsa.dev/provenance/v1",
    "predicate": {
        "buildDefinition": {
            "buildType": string,
            "externalParameters": object,
            "internalParameters": object,
            "resolvedDependencies": [ ...#ResourceDescriptor ],
        },
        "runDetails": {
            "builder": {
                "id": string,
                "builderDependencies": [ ...#ResourceDescriptor ],
                "version": { ...string },
            },
            "metadata": {
                "invocationId": string,
                "startedOn": #Timestamp,
                "finishedOn": #Timestamp,
            },
            "byproducts": [ ...#ResourceDescriptor ],
        }
    }
}

#ResourceDescriptor: {
    "uri": string,
    "digest": {
        "sha256": string,
        "sha512": string,
        "gitCommit": string,
        [string]: string,
    },
    "name": string,
    "downloadLocation": string,
    "mediaType": string,
    "content": bytes, // base64-encoded
    "annotations": {
        [string]: _  // any JSON type
    }
}

#Timestamp: string  // <YYYY>-<MM>-<DD>T<hh>:<mm>:<ss>Z

```

<details>
<summary>Protocol buffer schema</summary>

*NOTE: This summary (in protobuf) is informative. In the event of a
disagreement with the text description, the text is authoritative.*

Link: [provenance.proto](schema/provenance.proto)

*NOTE: This protobuf definition prioritizes being a human-readable summary
of the schema for readers of the specification. A version of the protobuf
definition useful for code generation is maintained in the
[in-toto attestation] repository.*

```proto
syntax = "proto3";

package slsa.v1;

import "google/protobuf/struct.proto";
import "google/protobuf/timestamp.proto";

// NOTE: While file uses snake_case as per the Protocol Buffers Style Guide, the
// provenance is always serialized using JSON with lowerCamelCase. Protobuf
// tooling performs this case conversion automatically.

message Provenance {
  BuildDefinition build_definition = 1;
  RunDetails run_details = 2;
}

message BuildDefinition {
  string build_type = 1;
  google.protobuf.Struct external_parameters = 2;
  google.protobuf.Struct internal_parameters = 3;
  repeated ResourceDescriptor resolved_dependencies = 4;
}

message ResourceDescriptor {
  string uri = 1;
  map<string, string> digest = 2;
  string name = 3;
  string download_location = 4;
  string media_type = 5;
  bytes content = 6;
  map<string, google.protobuf.Value> annotations = 7;
}

message RunDetails {
  Builder builder = 1;
  BuildMetadata metadata = 2;
  repeated ResourceDescriptor byproducts = 3;
}

message Builder {
  string id = 1;
  map<string, string> version = 2;
  repeated ResourceDescriptor builder_dependencies = 3;
}

message BuildMetadata {
  string invocation_id = 1;
  google.protobuf.Timestamp started_on = 2;
  google.protobuf.Timestamp finished_on = 3;
}

```

#### Provenance

*NOTE: This section describes the fields within `predicate`. For a description
of the other top-level fields, such as `subject`, see [Statement].*

[Provenance]: #provenance

REQUIRED for SLSA Build L1: `buildDefinition`, `runDetails`

*Table — columns: Field, Type, Description*

###### `buildDefinition` — type: BuildDefinition  `#buildDefinition`

The input to the build. The accuracy and completeness are implied by
`runDetails.builder.id`.

###### `runDetails` — type: RunDetails  `#runDetails`

Details specific to this particular execution of the build.

#### BuildDefinition

[BuildDefinition]: #builddefinition

REQUIRED for SLSA Build L1: `buildType`, `externalParameters`

*Table — columns: Field, Type, Description*

###### `buildType` — type: string (TypeURI)  `#buildType`

Identifies the template for how to perform the build and interpret the
parameters and dependencies.

The URI SHOULD resolve to a human-readable specification that includes: overall
description of the build type; schema for `externalParameters` and
`internalParameters`; unambiguous instructions for how to initiate the build given
this BuildDefinition, and a complete example. Example:
https://slsa-framework.github.io/github-actions-buildtypes/workflow/v1

###### `externalParameters` — type: object  `#externalParameters`

The parameters that are under external control, such as those set by a user or
tenant of the build platform. They MUST be complete at SLSA Build L3, meaning that
there is no additional mechanism for an external party to influence the
build. (At lower SLSA Build levels, the completeness MAY be best effort.)

The build platform SHOULD be designed to minimize the size and complexity of
`externalParameters`, in order to reduce fragility and ease [verification].
Consumers SHOULD have an expectation of what "good" looks like; the more
information that they need to check, the harder that task becomes.

Verifiers SHOULD reject unrecognized or unexpected fields within
`externalParameters`.

###### `internalParameters` — type: object  `#internalParameters`

The parameters that are under the control of the entity represented by
`builder.id`. The primary intention of this field is for debugging, incident
response, and vulnerability management. The values here MAY be necessary for
reproducing the build. There is no need to [verify][Verification] these
parameters because the build platform is already trusted, and in many cases it is
not practical to do so.

###### `resolvedDependencies` — type: array (ResourceDescriptor)  `#resolvedDependencies`

Unordered collection of artifacts needed at build time. Completeness is best
effort, at least through SLSA Build L3. For example, if the build script
fetches and executes "example.com/foo.sh", which in turn fetches
"example.com/bar.tar.gz", then both "foo.sh" and "bar.tar.gz" SHOULD be
listed here.

The BuildDefinition describes all of the inputs to the build. It SHOULD contain
all the information necessary and sufficient to initialize the build and begin
execution.

The `externalParameters` and `internalParameters` are the top-level inputs to the
template, meaning inputs not derived from another input. Each is an arbitrary
JSON object, though it is RECOMMENDED to keep the structure simple with string
values to aid verification. The same field name SHOULD NOT be used for both
`externalParameters` and `internalParameters`.

The parameters SHOULD only contain the actual values passed in through the
interface to the build platform. Metadata about those parameter values,
particularly digests of artifacts referenced by those parameters, SHOULD instead
go in `resolvedDependencies`. The documentation for `buildType` SHOULD explain
how to convert from a parameter to the dependency `uri`. For example:

```json
"externalParameters": {
    "repository": "https://github.com/octocat/hello-world",
    "ref": "refs/heads/main"
},
"resolvedDependencies": [{
    "uri": "git+https://github.com/octocat/hello-world@refs/heads/main",
    "digest": {"gitCommit": "7fd1a60b01f91b314f59955a4e4d4e80d8edf11d"}
}]
```

Guidelines:

-   Maximize the amount of information that is implicit from the meaning of
    `buildType`. In particular, any value that is boilerplate and the same
    for every build SHOULD be implicit.

-   Reduce parameters by moving configuration to input artifacts whenever
    possible. For example, instead of passing in compiler flags via an external
    parameter that has to be [verified][Verification] separately, require the
    flags to live next to the source code or build configuration so that
    verifying the latter automatically verifies the compiler flags.

-   In some cases, additional external parameters might exist that do not impact
    the behavior of the build, such as a deadline or priority. These extra
    parameters SHOULD be excluded from the provenance after careful analysis
    that they indeed pose no security impact.

-   If possible, architect the build platform to use this definition as its
    sole top-level input, in order to guarantee that the information is
    sufficient to run the build.

-   When build configuration is evaluated client-side before being sent to the
    server, such as transforming version-controlled YAML into ephemeral JSON,
    some solution is needed to make [verification] practical. Consumers need a
    way to know what configuration is expected and the usual way to do that is
    to map it back to version control, but that is not possible if the server
    cannot verify the configuration's origins. Possible solutions:

    -   (RECOMMENDED) Rearchitect the build platform to read configuration
        directly from version control,  recording the server-verified URI in
        `externalParameters` and the digest in `resolvedDependencies`.

    -   Record the digest in the provenance[^digest-param] and use a separate
        provenance attestation to link that digest back to version control. In
        this solution, the client-side evaluation is considered a separate
        "build" that SHOULD be independently secured using SLSA, though securing
        it can be difficult since it usually runs on an untrusted workstation.

-   The purpose of `resolvedDependencies` is to facilitate recursive analysis of
    the software supply chain. Where practical, it is valuable to record the
    URI and digest of artifacts that, if compromised, could impact the build. At
    SLSA Build L3, completeness is considered "best effort".

[^digest-param]: The `externalParameters` SHOULD reflect reality. If clients
    send the evaluated configuration object directly to the build server, record
    the digest directly in `externalParameters`. If clients upload the
    configuration object to a temporary storage location and send that location
    to the build server, record the location in `externalParameters` as a URI
    and record the `uri` and `digest` in `resolvedDependencies`.

#### RunDetails

[RunDetails]: #rundetails

REQUIRED for SLSA Build L1: `builder`

*Table — columns: Field, Type, Description*

###### `builder` — type: Builder  `#runDetailsBuilder`

Identifies the build platform that executed the invocation, which is trusted to
have correctly performed the operation and populated this provenance.

###### `metadata` — type: BuildMetadata  `#runDetailsMetadata`

Metadata about this particular execution of the build.

###### `byproducts` — type: array (ResourceDescriptor)  `#runDetailsByproducts`

Additional artifacts generated during the build that are not considered
the "output" of the build but that might be needed during debugging or
incident response. For example, this might reference logs generated during
the build and/or a digest of the fully evaluated build configuration.

In most cases, this SHOULD NOT contain all intermediate files generated during
the build. Instead, this SHOULD only contain files that are likely to be useful
later and that cannot be easily reproduced.

#### Builder

[Builder]: #builder

REQUIRED for SLSA Build L1: `id`

*Table — columns: Field, Type, Description*

###### `id` — type: string (TypeURI)  `#builder.id`

URI indicating the transitive closure of the trusted build platform. This is
[intended](verifying-artifacts#step-1-check-slsa-build-level)
to be the sole determiner of the SLSA Build level.

If a build platform has multiple modes of operations that have differing
security attributes or SLSA Build levels, each mode MUST have a different
`builder.id` and SHOULD have a different signer identity. This is to minimize
the risk that a less secure mode compromises a more secure one.

The `builder.id` URI SHOULD resolve to documentation explaining:

-   The scope of what this ID represents.
-   The claimed SLSA Build level.
-   The accuracy and completeness guarantees of the fields in the provenance.
-   Any fields that are generated by the tenant-controlled build process and not
    verified by the trusted control plane, except for the `subject`.
-   The interpretation of any extension fields.

###### `builderDependencies` — type: array (ResourceDescriptor)  `#builderDependencies`

Dependencies used by the orchestrator that are not run within the workload
and that do not affect the build, but might affect the provenance generation
or security guarantees.

###### `version` — type: map (string→string)  `#builder.version`

Map of names of components of the build platform to their version.

The build platform, or <dfn>builder</dfn> for short, represents the transitive
closure of all the entities that are, by necessity, [trusted] to faithfully run
the build and record the provenance. This includes not only the software but the
hardware and people involved in running the service. For example, a particular
instance of [Tekton](https://tekton.dev/) could be a build platform, while
Tekton itself is not. For more info, see [Build
model](terminology#build-model).

The `id` MUST reflect the trust base that consumers care about. How detailed to
be is a judgement call. For example, GitHub Actions supports both GitHub-hosted
runners and self-hosted runners. The GitHub-hosted runner might be a single
identity because it's all GitHub from the consumer's perspective. Meanwhile,
each self-hosted runner might have its own identity because not all runners are
trusted by all consumers.

Consumers MUST accept only specific signer-builder pairs. For example, "GitHub"
can sign provenance for the "GitHub Actions" builder, and "Google" can sign
provenance for the "Google Cloud Build" builder, but "GitHub" cannot sign for
the "Google Cloud Build" builder.

Design rationale: The builder is distinct from the signer in order to support
the case where one signer generates attestations for more than one builder, as
in the GitHub Actions example above. The field is REQUIRED, even if it is
implicit from the signer, to aid readability and debugging. It is an object to
allow additional fields in the future, in case one URI is not sufficient.

#### BuildMetadata

[BuildMetadata]: #buildmetadata

REQUIRED: (none)

*Table — columns: Field, Type, Description*

###### `invocationId` — type: string  `#invocationId`

Identifies this particular build invocation, which can be useful for finding
associated logs or other ad-hoc analysis. The exact meaning and format is
defined by `builder.id`; by default it is treated as opaque and case-sensitive.
The value SHOULD be globally unique.

###### `startedOn` — type: string (Timestamp)  `#startedOn`

The timestamp of when the build started.

###### `finishedOn` — type: string (Timestamp)  `#finishedOn`

The timestamp of when the build completed.

#### Extension fields

[Extension fields]: #extension-fields

Implementations MAY add extension fields to any JSON object to describe
information that is not captured in a standard field. Guidelines:

-   Extension fields SHOULD use names of the form `<vendor>_<fieldname>`, e.g.
    `examplebuilder_isCodeReviewed`. This practice avoids field name collisions
    by namespacing each vendor. Non-extension field names never contain an
    underscore.
-   Extension fields MUST NOT alter the meaning of any other field. In other
    words, an attestation with an absent extension field MUST be interpreted
    identically to an attestation with an unrecognized (and thus ignored)
    extension field.
-   Extension fields SHOULD follow the [monotonic principle][parsing rules],
    meaning that deleting or ignoring the extension SHOULD NOT turn a DENY
    decision into an ALLOW.

### Verification

[Verification]: verifying-artifacts

Please see [Verifying Artifacts][Verification] for a detailed discussion of
provenance verification.

### Index of build types

The following is a partial index of build type definitions. Each contains a
complete example predicate.

-   [GitHub Actions Workflow (community-maintained)](https://slsa-framework.github.io/github-actions-buildtypes/workflow/v1)
-   [Google Cloud Build (community-maintained)](https://slsa-framework.github.io/gcb-buildtypes/triggered-build/v1)

To add an entry here, please send a pull request on GitHub.

### Migrating from 0.2

To migrate from [version 0.2](/provenance/v0.2) (`old`), use the following
pseudocode. The meaning of each field is unchanged unless otherwise noted.

```javascript
{
    "buildDefinition": {
        // The `buildType` MUST be updated for v1.0 to describe how to
        // interpret `inputArtifacts`.
        "buildType": /* updated version of */ old.buildType,
        "externalParameters":
            old.invocation.parameters + {
            // It is RECOMMENDED to rename "entryPoint" to something more
            // descriptive.
            "entryPoint": old.invocation.configSource.entryPoint,
            // It is OPTIONAL to rename "source" to something more descriptive,
            // especially if "source" is ambiguous or confusing.
            "source": old.invocation.configSource.uri,
        },
        "internalParameters": old.invocation.environment,
        "resolvedDependencies":
            old.materials + [
            {
                "uri": old.invocation.configSource.uri,
                "digest": old.invocation.configSource.digest,
            }
        ]
    },
    "runDetails": {
        "builder": {
            "id": old.builder.id,
            "builderDependencies": null,  // not in v0.2
            "version": null,  // not in v0.2
        },
        "metadata": {
            "invocationId": old.metadata.buildInvocationId,
            "startedOn": old.metadata.buildStartedOn,
            "finishedOn": old.metadata.buildFinishedOn,
        },
        "byproducts": null,  // not in v0.2
    },
}
```

The following fields from v0.2 are no longer present in v1.0:

-   `entryPoint`: Use `externalParameters[<name>]` instead.
-   `buildConfig`: No longer inlined into the provenance. Instead, either:
    -   If the configuration is a top-level input, record its digest in
        `externalParameters["config"]`.
    -   Else if there is a known use case for knowing the exact resolved
        build configuration, record its digest in `byproducts`. An example use
        case might be someone who wishes to parse the configuration to look for
        bad patterns, such as `curl | bash`.
    -   Else omit it.
-   `metadata.completeness`: Now implicit from `builder.id`.
-   `metadata.reproducible`: Now implicit from `builder.id`.

### Change history

#### v1.2

-   Note the difference between the *provenance* build model diagram and
    the general SLSA build model diagram.

#### v1.0

Major refactor to reduce misinterpretation, including a minor change in model.

-   Significantly expanded all documentation.
-   Altered the model slightly to better align with real-world build platforms,
    align with reproducible builds, and make verification easier.
-   Grouped fields into `buildDefinition` vs `runDetails`.
-   Renamed:
    -   `parameters` -> `externalParameters` (slight change in semantics)
    -   `environment` -> `internalParameters` (slight change in semantics)
    -   `materials` -> `resolvedDependencies` (slight change in semantics)
    -   `buildInvocationId` -> `invocationId`
    -   `buildStartedOn` -> `startedOn`
    -   `buildFinishedOn` -> `finishedOn`
-   Removed:
    -   `configSource`: No longer special-cased. Now represented as
        `externalParameters`  + `resolvedDependencies`.
    -   `buildConfig`: No longer inlined into the provenance. Can be replaced
        with a reference in `externalParameters` or `byproducts`, depending on
        the semantics, or omitted if not needed.
    -   `completeness` and `reproducible`: Now implied by `builder.id`.
-   Added:
    -   ResourceDescriptor:  `annotations`, `content`, `downloadLocation`,
        `mediaType`, `name`
    -   Builder: `builderDependencies` and `version`
    -   `byproducts`
-   Changed naming convention for extension fields.

Differences from RC1 and RC2:

-   Renamed `systemParameters` (RC1 + RC2) -> `internalParameters` (final).
-   Changed naming convention for extension fields (in RC2).
-   Renamed `localName` (RC1) -> `name` (RC2).
-   Added `annotations` and `content` (in RC2).

#### v0.2

Refactored to aid clarity and added `buildConfig`. The model is unchanged.

-   Replaced `definedInMaterial` and `entryPoint` with `configSource`.
-   Renamed `recipe` to `invocation`.
-   Moved `invocation.type` to top-level `buildType`.
-   Renamed `arguments` to `parameters`.
-   Added `buildConfig`, which can be used as an alternative to `configSource`
    to validate the configuration.

#### rename: slsa.dev/provenance

Renamed to "slsa.dev/provenance".

#### v0.1.1

-   Added `metadata.buildInvocationId`.

#### v0.1

Initial version, named "in-toto.io/Provenance"

[Statement]: https://github.com/in-toto/attestation/blob/7aefca35a0f74a6e0cb397a8c4a76558f54de571/spec/v1/statement.md
[in-toto attestation]: https://github.com/in-toto/attestation
[parsing rules]: https://github.com/in-toto/attestation/blob/7aefca35a0f74a6e0cb397a8c4a76558f54de571/spec/v1/README.md#parsing-rules
[purl]: https://github.com/package-url/purl-spec
[threats]: threats
[trusted]: principles#trust-systems-verify-artifacts


---

## Verification Summary Attestation (VSA) — `verification_summary.md`

*Locator page:* https://slsa.dev/spec/v1.2/verification_summary · *Requirements extracted:* R-0226 – R-0243 (18 statements)

> Page description (front matter): Specification for a verification summary of artifacts by a trusted verifier entity.

Verification summary attestations communicate that an artifact has been verified
at a specific SLSA level and details about that verification.

This document defines the following predicate type within the [in-toto
attestation] framework:

```json
"predicateType": "https://slsa.dev/verification_summary/v1"
```

> Important: Always use the above string for `predicateType` rather than what is
> in the URL bar. The `predicateType` URI will always resolve to the latest
> minor version of this specification. See [parsing rules](#parsing-rules) for
> more information.

### Purpose

Describe what SLSA level an artifact or set of artifacts was verified at
and other details about the verification process including what SLSA level
the dependencies were verified at.

This allows software consumers to make a decision about the validity of an
artifact without needing to have access to all of the attestations about the
artifact or all of its transitive dependencies.  They can use it to delegate
complex policy decisions to some trusted party and then simply trust that
party's decision regarding the artifact.

It also allows software producers to keep the details of their build pipeline
confidential while still communicating that some verification has taken place.
This might be necessary for legal reasons (keeping a software supplier
confidential) or for security reasons (not revealing that an embargoed patch has
been included).

### Model

A Verification Summary Attestation (VSA) is an attestation that some entity
(`verifier`) verified one or more software artifacts (the `subject` of an
in-toto attestation [Statement]) by evaluating the artifact and a `bundle`
of attestations against some `policy`.  Users who trust the `verifier` may
assume that the artifacts met the indicated SLSA level without themselves
needing to evaluate the artifact or to have access to the attestations the
`verifier` used to make its determination.

The VSA also allows consumers to determine the verified levels of
all of an artifact’s _transitive_ dependencies.  The verifier does this by
either a) verifying the provenance of each non-source dependency listed in
the [resolvedDependencies](build-provenance#resolvedDependencies) of the
artifact being verified (recursively) or b) matching the non-source dependency
listed in `resolvedDependencies` (`subject.digest` ==
`resolvedDependencies.digest` and, ideally, `vsa.resourceUri` ==
`resolvedDependencies.uri`) to a VSA _for that dependency_ and using
`vsa.verifiedLevels` and `vsa.dependencyLevels`.  Policy verifiers wishing
to establish minimum requirements on dependencies SLSA levels may use
`vsa.dependencyLevels` to do so.

### Schema

```jsonc
// Standard attestation fields:
"_type": "https://in-toto.io/Statement/v1",
"subject": [{
  "name": <NAME>,
  "digest": { <digest-in-request> }
}],

// Predicate
"predicateType": "https://slsa.dev/verification_summary/v1",
"predicate": {
  "verifier": {
    "id": "<URI>",
    "version": {
      "<COMPONENT>": "<VERSION>",
      ...
    }
  },
  "timeVerified": <TIMESTAMP>,
  "resourceUri": <artifact-URI-in-request>,
  "policy": {
    "uri": "<URI>",
    "digest": { <digest-of-policy-data> }
  }
  "inputAttestations": [
    {
      "uri": "<URI>",
      "digest": { <digest-of-attestation-data> }
    },
    ...
  ],
  "verificationResult": "<PASSED|FAILED>",
  "verifiedLevels": ["<SlsaResult>"],
  "dependencyLevels": {
    "<SlsaResult>": <Int>,
    "<SlsaResult>": <Int>,
    ...
  },
  "slsaVersion": "<MAJOR>.<MINOR>",
}
```

#### Parsing rules

This predicate follows the in-toto attestation [parsing rules]. Summary:

-   Consumers MUST ignore unrecognized fields.
-   The `predicateType` URI includes the major version number and will always
    change whenever there is a backwards incompatible change.
-   Minor version changes are always backwards compatible and "monotonic." Such
    changes do not update the `predicateType`.
-   Producers MAY add extension fields using field names that are URIs.

#### Fields

_NOTE: This section describes the fields within `predicate`. For a description
of the other top-level fields, such as `subject`, see [Statement]._

<a id="verifier"></a>
`verifier` _object, required_

> Identifies the entity that performed the verification.
>
> The identity MUST reflect the trust base that consumers care about. How
> detailed to be is a judgment call.
>
> Consumers MUST accept only specific (signer, verifier) pairs. For example,
> "GitHub" can sign provenance for the "GitHub Actions" verifier, and "Google"
> can sign provenance for the "Google Cloud Deploy" verifier, but "GitHub" cannot
> sign for the "Google Cloud Deploy" verifier.
>
> The field is required, even if it is implicit from the signer, to aid readability and
> debugging. It is an object to allow additional fields in the future, in case one
> URI is not sufficient.

<a id="verifier.id"></a>
`verifier.id` _string ([TypeURI]), required_

> URI indicating the verifier’s identity.

<a id="verifier.version"></a>
`verifier.version` _map (string->string), optional_

> Map of names of components of the verification platform to their version.

<a id="timeVerified"></a>
`timeVerified` _string ([Timestamp]), optional_

> Timestamp indicating what time the verification occurred.

<a id="resourceUri"></a>
`resourceUri` _string ([ResourceURI]), required_

> URI that identifies the resource associated with the artifact being verified.
>
> The `resourceUri` SHOULD be set to the URI from which the producer expects the
> consumer to fetch the artifact for verification. This enables the consumer to
> easily determine the expected value when [verifying](#how-to-verify). If the
> `resourceUri` is set to some other value, the producer MUST communicate the
> expected value, or how to determine the expected value, to consumers through
> an out-of-band channel.

<a id="policy"></a>
`policy` _object ([ResourceDescriptor]), required_

> Describes the policy that the `subject` was verified against.
>
> The entry MUST contain a `uri` identifying which policy was applied and
> SHOULD contain a `digest` to indicate the exact version of that policy.

<a id="inputAttestations"></a>
`inputAttestations` _array ([ResourceDescriptor]), optional_

> The collection of attestations that were used to perform verification.
> Conceptually similar to the `resolvedDependencies` field in [SLSA Provenance].
>
> This field MAY be absent if the verifier does not support this feature.
> If non-empty, this field MUST contain information on _all_ the attestations
> used to perform verification.
>
> Each entry MUST contain a `digest` of the attestation and SHOULD contains a
> `uri` that can be used to fetch the attestation.

<a id="verificationResult"></a>
`verificationResult` _string, required_

> Either “PASSED” or “FAILED” to indicate if the artifact passed or failed the policy verification.

<a id="verifiedLevels"></a>
`verifiedLevels` _array ([SlsaResult]), required_

> Indicates the highest level of each track verified for the artifact (and not
> its dependencies) and any [verified properties](verified-properties) verified
> for the artifact or "FAILED" if policy verification failed.
>
> Users MUST NOT include more than one level per SLSA track. Note that each SLSA
> level implies all levels below it (e.g. `SLSA_BUILD_LEVEL_3` implies
> `SLSA_BUILD_LEVEL_2` and `SLSA_BUILD_LEVEL_1`), so there is no need to
> include more than one level per track.

<a id="dependencyLevels"></a>
`dependencyLevels` _object, optional_

> A count of the dependencies at each SLSA level.
>
> Map from [SlsaResult] to the number of the artifact's _transitive_ dependencies
> that were verified at the indicated level. Absence of a given level of
> [SlsaResult] MUST be interpreted as reporting _0_ dependencies at that level.
> A set but empty `dependencyLevels` object means that the artifact has **no**
> dependency at all, while an unset or null `dependencyLevels` means that the
> verifier makes no claims about the artifact's dependencies.
>
> Users MUST count each dependency only once per SLSA track, at the highest
> level verified. For example, if a dependency meets `SLSA_BUILD_LEVEL_2`,
> you include it with the count for `SLSA_BUILD_LEVEL_2` but not the count for
> `SLSA_BUILD_LEVEL_1`.

<a id="slsaVersion"></a>
`slsaVersion` _string, optional_

> Indicates the version of the SLSA specification that the verifier used, in the
> form `<MAJOR>.<MINOR>`. Example: `1.0`. If unset, the default is an
> unspecified minor version of `1.x`.

### Example

WARNING: This is just for demonstration purposes.

```jsonc
"_type": "https://in-toto.io/Statement/v1",
"subject": [{
  "name": "out/example-1.2.3.tar.gz",
  "digest": {"sha256": "5678..."}
}],

// Predicate
"predicateType": "https://slsa.dev/verification_summary/v1",
"predicate": {
  "verifier": {
    "id": "https://example.com/publication_verifier",
    "version": {
      "slsa-verifier-linux-amd64": "v2.3.0",
      "slsa-framework/slsa-verifier/actions/installer": "v2.3.0"
    }
  },
  "timeVerified": "1985-04-12T23:20:50.52Z",
  "resourceUri": "https://example.com/example-1.2.3.tar.gz",
  "policy": {
    "uri": "https://example.com/example_tarball.policy",
    "digest": {"sha256": "1234..."}
  },
  "inputAttestations": [
    {
      "uri": "https://example.com/provenances/example-1.2.3.tar.gz.intoto.jsonl",
      "digest": {"sha256": "abcd..."}
    }
  ],
  "verificationResult": "PASSED",
  "verifiedLevels": ["SLSA_BUILD_LEVEL_3"],
  "dependencyLevels": {
    "SLSA_BUILD_LEVEL_3": 5,
    "SLSA_BUILD_LEVEL_2": 7,
    "SLSA_BUILD_LEVEL_1": 1,
  },
  "slsaVersion": "1.0"
}
```

### How to verify

VSA consumers use VSAs to accomplish goals based on delegated trust. We call the
process of establishing a VSA's authenticity and determining whether it meets
the consumer's goals 'verification'. Goals differ, as do levels of confidence
in VSA producers, so the verification procedure changes to suit its context.
However, there are certain steps that most verification procedures have in
common.

Verification MUST include the following steps:

1.  Verify the signature on the VSA envelope using the preconfigured roots of
    trust. This step ensures that the VSA was produced by a trusted producer
    and that it hasn't been tampered with.

2.  Verify the statement's `subject` matches the digest of the artifact in
    question. This step ensures that the VSA pertains to the intended artifact.

3.  Verify that the `predicateType` is
    `https://slsa.dev/verification_summary/v1`. This step ensures that the
    in-toto predicate is using this version of the VSA format.

4.  Verify that the `verifier` matches the public key (or equivalent) used to
    verify the signature in step 1. This step identifies the VSA producer in
    cases where their identity is not implicitly revealed in step 1.

5.  Verify that the value for `resourceUri` in the VSA matches the expected
    value. This step ensures that the consumer is using the VSA for the
    producer's intended purpose.

6.  Verify that the value for `verificationResult` is `PASSED`. This step
    ensures the artifact is suitable for the consumer's purposes.

7.  Verify that `verifiedLevels` contains the expected value. This step ensures
    that the artifact is suitable for the consumer's purposes.

Verification MAY additionally contain the following step:

1.  (Optional) Verify additional fields required to determine whether the VSA
    meets your goal.

Verification mitigates different threats depending on the VSA's contents and the
verification procedure.

IMPORTANT: A VSA does not protect against compromise of the verifier, such as by
a malicious insider. Instead, VSA consumers SHOULD carefully consider which
verifiers they add to their roots of trust.

#### Examples

1.  Suppose consumer C wants to delegate to verifier V the decision for whether
    to accept artifact A as resource R. Consumer C verifies that:

    -   The signature on the VSA envelope using V's public signing key from their
      preconfigured root of trust.

    -   `subject` is A.

    -   `predicateType` is `https://slsa.dev/verification_summary/v1`.

    -   `verifier.id` is V.

    -   `resourceUri` is R.

    -   `slsaResult` is `PASSED`.

    -   `verifiedLevels` contains `SLSA_BUILD_LEVEL_UNEVALUATED`.

    Note: This example is analogous to traditional code signing. The expected
    value for `verifiedLevels` is arbitrary but prenegotiated by the producer and
    the consumer. The consumer does not need to check additional fields, as C
    fully delegates the decision to V.

2.  Suppose consumer C wants to enforce the rule "Artifact A at resource R must
    have a passing VSA from verifier V showing it meets SLSA Build Level 2+."
    Consumer C verifies that:

    -   The signature on the VSA envelope using V's public signing key from their
      preconfigured root of trust.

    -   `subject` is A.

    -   `predicateType` is `https://slsa.dev/verification_summary/v1`.

    -   `verifier.id` is V.

    -   `resourceUri` is R.

    -   `slsaResult` is `PASSED`.

    -   `verifiedLevels` is `SLSA_BUILD_LEVEL_2` or `SLSA_BUILD_LEVEL_3`.

    Note: In this example, verifying the VSA mitigates the same threats as
    verifying the artifact's SLSA provenance. See
    [Verifying artifacts](/spec/v1.0/verifying-artifacts) for details about which
    threats are addressed by verifying each SLSA level.

### _SlsaResult (String)_

The result of evaluating an artifact (or set of artifacts) against SLSA.
SHOULD be

-   The [SLSA Track](#tracks) level the referenced artifact qualifies for as
`SLSA_<TRACK_NAME>_LEVEL_<LEVEL_NUMBER>`, or
-   `SLSA_<TRACK NAME>_LEVEL_UNEVALUATED` if the VSA issuer does not want to
    make a claim about the track level an artifact meets

For example:

-   `SLSA_BUILD_LEVEL_UNEVALUATED`
-   `SLSA_BUILD_LEVEL_0`
-   `SLSA_BUILD_LEVEL_3`
-   `SLSA_SOURCE_LEVEL_2`
-   `SLSA_SOURCE_LEVEL_4`
-   `FAILED` (Indicates policy evaluation failed)

Note that each SLSA level implies the levels below it in the same track.
For example, `SLSA_BUILD_LEVEL_3` means (`SLSA_BUILD_LEVEL_1` +
`SLSA_BUILD_LEVEL_2` + `SLSA_BUILD_LEVEL_3`).

Users MAY use custom values here but MUST NOT use custom values starting with
`SLSA_`.

### Change history

-   1.2:
    -   Update SlsaResult definition to discuss how to refer to new tracks and
        link to [verified properties](verified-properties) for additional SLSA
        endorsed values.
    -   Fixed a typo where the verificationResult was incorrectly referred to
        as slsaResult.
-   1.1:
    -   Changed the `policy` object to recommend that the `digest` field of
        the `ResourceDescriptor` is set.
    -   Added optional `verifier.version` field to record verification tools.
    -   Added Verification section with examples.
    -   Made `timeVerified` optional.
-   1.0:
    -   Replaced `materials` with `resolvedDependencies`.
    -   Relaxed `SlsaResult` to allow other values.
    -   Converted to lowerCamelCase for consistency with [SLSA Provenance].
    -   Added `slsaVersion` field.
-   0.2:
    -   Added `resource_uri` field.
    -   Added optional `input_attestations` field.
-   0.1: Initial version.

[SLSA Provenance]: /provenance
[SlsaResult]: #slsaresult
[DigestSet]: https://github.com/in-toto/attestation/blob/7aefca35a0f74a6e0cb397a8c4a76558f54de571/spec/v1/digest_set.md
[ResourceURI]: https://github.com/in-toto/attestation/blob/7aefca35a0f74a6e0cb397a8c4a76558f54de571/spec/v1/field_types.md#resourceuri
[ResourceDescriptor]: https://github.com/in-toto/attestation/blob/7aefca35a0f74a6e0cb397a8c4a76558f54de571/spec/v1/resource_descriptor.md
[Statement]: https://github.com/in-toto/attestation/blob/7aefca35a0f74a6e0cb397a8c4a76558f54de571/spec/v1/statement.md
[Timestamp]: https://github.com/in-toto/attestation/blob/7aefca35a0f74a6e0cb397a8c4a76558f54de571/spec/v1/field_types.md#timestamp
[TypeURI]: https://github.com/in-toto/attestation/blob/7aefca35a0f74a6e0cb397a8c4a76558f54de571/spec/v1/field_types.md#TypeURI
[in-toto attestation]: https://github.com/in-toto/attestation
[parsing rules]: https://github.com/in-toto/attestation/blob/7aefca35a0f74a6e0cb397a8c4a76558f54de571/spec/v1/README.md#parsing-rules

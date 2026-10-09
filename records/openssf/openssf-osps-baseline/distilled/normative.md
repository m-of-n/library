---
schema: "library-normative/v1"
id: openssf-osps-baseline-normative
record: openssf-osps-baseline
type: normative
updated: "2026-10-02"
extracted: "2026-10-02"
coverage: "All 8 families, 41 controls, 65 assessment requirements (64 active + 1 retired) with objective, verbatim requirement text, recommendation, applicability, and control-level external-framework mappings; applicability-group definitions; mapping-reference table; full 40-term lexicon."
reviewed_by: ""
---

# OSPS Baseline v2026.08.28 — normative content

> Rendered verbatim from the authoritative Gemara YAML at tag `v2026.08.28` of
> `github.com/ossf/security-baseline` (`baseline/*.yaml`, `baseline/mappings/*.yaml`). Line-wrapping in
> the YAML block scalars is collapsed to single spaces; no other change. Every requirement text was
> checked to be identical to the published page https://baseline.openssf.org/versions/2026-08-28 .
> Locator convention: `OSPS-XX.yaml <control> / <assessment requirement>`.

**Normative form.** Per the Gemara schema the *assessment requirement* `text` is the requirement
("typically written as a MUST condition"); `recommendation` is "non-binding suggestions";
`objective` is the control's statement of intent. The baseline's guiding principle (site About page):
"Controls only contain *MUST* entries, not *SHOULD*."

## Catalog metadata (`baseline/metadata.yaml`)

- **title:** Open Source Project Security Baseline
- **id / type / gemara-version:** `osps-baseline` / `ControlCatalog` / `1.2.0`
- **description:** The Open Source Project Security (OSPS) Baseline is a set of security criteria that projects should meet to demonstrate a strong security posture.
- **draft:** `True` (note: the released catalog still carries `draft: true`)
- **author:** OSPS Baseline Authors (`openssf`, Human)

### Applicability groups (maturity levels)

| id | title | description |
|---|---|---|
| `maturity-1` | Maturity Level 1 | for any code or non-code project with any number of maintainers or users |
| `maturity-2` | Maturity Level 2 | for any code project that has at least 2 maintainers and a small number of consistent users |
| `maturity-3` | Maturity Level 3 | for any code project that has a large number of consistent users |

### Counts

- Controls: **41**; assessment requirements: **65** (64 active, 1 retired).
- Active per family: AC 6, BR 12, DO 8, GV 6, LE 5, QA 13, SA 4, VM 10.
- Applicable at level: L1 24, L2 41, L3 62; introduced at level: L1 24, L2 19, L3 21.
- Applicability is cumulative in every case in this release (an AR applicable at L1 is also listed for L2 and L3; L2 ARs also at L3) except **OSPS-BR-07.01** and **OSPS-VM-02.01**, which list `maturity-1` only.

## AC — Access Control (`baseline/OSPS-AC.yaml`)

Access Control focuses on the mechanisms and policies that control access to the project's version control system and CI/CD pipelines. These controls help ensure that only authorized users can access sensitive data, modify repository settings, or execute build and release processes.

### OSPS-AC-01 — Use MFA for Sensitive Actions

**Objective:** Reduce the risk of account compromise or insider threats by requiring multi-factor authentication for collaborators modifying the project repository settings or accessing sensitive data.

#### OSPS-AC-01.01

- **Requirement** (OSPS-AC.yaml OSPS-AC-01 / OSPS-AC-01.01): "When a user attempts to read or modify a sensitive resource in the project's authoritative repository, the system MUST require the user to complete a multi-factor authentication process."
- **Recommendation:** "Enforce multi-factor authentication for the project's version control system, requiring collaborators to provide a second form of authentication when accessing sensitive data or modifying repository settings. Passkeys are acceptable for this control."
- **Applicability:** `maturity-1`, `maturity-2`, `maturity-3`

**External framework relations** (`relates-to`, control-level):

- **BPB**: CC-G-1
- **CSF**: PR.AA-02, PR.AA-05
- **CRA**: 1.2d, 1.2e, 1.2f
- **SSDF**: PO.3.2, PS.1, PS.2
- **OpenCRE**: 486-813, 124-564, 347-352, 333-858, 152-725, 201-246
- **PSSCRM**: G2.6, P3.3, E1.2, E1.3, E1.4, E3.1
- **SAMM**: Operations - Environment Management - Configuration Hardening Lvl1
- **PCIDSS**: 2.2.1, 8.2.1, 8.3.1
- **800-161**: AC-4(21), AC-17, CM-5, CM-6, IA-2, IA-5
- **UKSSCOP**: Claim 1.4.2, Claim 2.1.5, Claim 2.2.2
- **BSI-TR-03185-2**: GV.02

### OSPS-AC-02 — Restrict Collaborator Permissions

**Objective:** Reduce the risk of unauthorized access to the project's repository by limiting the permissions granted to new collaborators.

#### OSPS-AC-02.01

- **Requirement** (OSPS-AC.yaml OSPS-AC-02 / OSPS-AC-02.01): "When a new collaborator is added, the version control system MUST require manual permission assignment, or restrict the collaborator permissions to the lowest available privileges by default."
- **Recommendation:** "Most public version control systems are configured in this manner. Ensure the project's version control system always assigns the lowest available permissions to collaborators by default when added, granting additional permissions only when necessary."
- **Applicability:** `maturity-1`, `maturity-2`, `maturity-3`

**External framework relations** (`relates-to`, control-level):

- **CSF**: PR.AA-02, PR.AA-05
- **CRA**: 1.2f
- **SSDF**: PO.2, PO.3.2, PS.1, PS.2
- **OpenCRE**: 486-813, 124-564, 802-056, 368-633, 152-725
- **PSSCRM**: P2.3, E1.2, E3.3
- **PCIDSS**: 2.2.1
- **800-161**: AC-2, AC-3, AC-4(21), AC-5, AC-6, CM-5, CM-7
- **UKSSCOP**: Claim 2.2.2
- **BSI-TR-03185-2**: GV.02

### OSPS-AC-03 — Protect the Primary Branch from Accidental Modification

**Objective:** Reduce the risk of accidental changes or deletion of the primary branch of the project's repository by preventing unintentional modification.

#### OSPS-AC-03.01

- **Requirement** (OSPS-AC.yaml OSPS-AC-03 / OSPS-AC-03.01): "When a direct commit is attempted on the project's primary branch, an enforcement mechanism MUST prevent the change from being applied."
- **Recommendation:** "If the VCS is centralized, set branch protection on the primary branch in the project's VCS. Alternatively, use a decentralized approach, like the Linux kernel's, where changes are first proposed in another repository, and merging changes into the primary repository requires a specific separate act."
- **Applicability:** `maturity-1`, `maturity-2`, `maturity-3`

#### OSPS-AC-03.02

- **Requirement** (OSPS-AC.yaml OSPS-AC-03 / OSPS-AC-03.02): "When an attempt is made to delete the project's primary branch, the version control system MUST treat this as a sensitive activity and require explicit confirmation of intent."
- **Recommendation:** "Set branch protection on the primary branch in the project's version control system to prevent deletion."
- **Applicability:** `maturity-1`, `maturity-2`, `maturity-3`

**External framework relations** (`relates-to`, control-level):

- **Scorecard**: Branch-Protection
- **CSF**: PR.AA-02, PR.AA-05
- **CRA**: 1.2f
- **SSDF**: PO.3.2, PS.1, PS.2
- **OpenCRE**: 486-813, 124-564, 152-725
- **PSSCRM**: P3.2, P3.5, E1.5, E3.1
- **PCIDSS**: 2.2.1
- **800-161**: AC-3, AC-5, CM-3, CM-3(2), CM-5
- **UKSSCOP**: Claim 1.1.4, Claim 2.2.2
- **BSI-TR-03185-2**: GV.02, QA.06

### OSPS-AC-04 — Enforce Least Privilege on CI/CD Pipelines

**Objective:** Reduce the risk of unauthorized access to the project's build and release processes by limiting the permissions granted to steps within the CI/CD pipelines.

#### OSPS-AC-04.01

- **Requirement** (OSPS-AC.yaml OSPS-AC-04 / OSPS-AC-04.01): "When a CI/CD task is executed with no permissions specified, the CI/CD system MUST default the task's permissions to the lowest permissions granted in the pipeline."
- **Recommendation:** "Configure the project's settings to assign the lowest available permissions to new pipelines by default, granting additional permissions only when necessary for specific tasks."
- **Applicability:** `maturity-2`, `maturity-3`

#### OSPS-AC-04.02

- **Requirement** (OSPS-AC.yaml OSPS-AC-04 / OSPS-AC-04.02): "When a job is assigned permissions in a CI/CD pipeline, the source code or configuration MUST only assign the minimum privileges necessary for the corresponding activity."
- **Recommendation:** "Configure the project's CI/CD pipelines to assign the lowest available permissions to users and services by default, elevating permissions only when necessary for specific tasks. In some version control systems, this may be possible at the organizational or repository level. If not, set permissions at the top level of the pipeline."
- **Applicability:** `maturity-3`

**External framework relations** (`relates-to`, control-level):

- **CSF**: PR.AA-02, PR.AA-05
- **CRA**: 1.2d, 1.2e, 1.2f
- **SSDF**: PO.2, PO.3.2, PS.1, PS.2
- **OpenCRE**: 486-813, 124-564, 263-184, 123-124
- **SLSA**: Choose an appropriate build platform, Build platform - Isolation strength - Isolated
- **PSSCRM**: P3.2
- **SAMM**: Operations - Environment Management - Configuration Hardening Lvl1
- **PCIDSS**: 2.2.1, 8.2.1
- **800-161**: AC-3(8), AC-4, AC-4(6), AC-6, AC-20, AC-20(1), CM-5, CM-7
- **UKSSCOP**: Claim 2.1.1, Claim 2.1.3, Claim 2.2.2

## BR — Build and Release (`baseline/OSPS-BR.yaml`)

Build and Release focuses on the processes and tools used to compile, package, and distribute the project's software. These controls help ensure that the project's build and release pipelines are secure, consistent, and reliable, reducing the risk of vulnerabilities or errors in the software distribution process.

### OSPS-BR-01 — Prevent Untrusted Input When Building & Releasing

**Objective:** Reduce the risk of code injection or other security vulnerabilities in the project's build and release pipelines by preventing untrusted input from accessing privileged resources.

#### OSPS-BR-01.01

- **Requirement** (OSPS-BR.yaml OSPS-BR-01 / OSPS-BR-01.01): "When a CI/CD pipeline operates on untrusted metadata, those parameters MUST be sanitized and validated prior to use in the pipeline."
- **Recommendation:** "CI/CD pipelines should sanitize (quote, escape or exit on expected values) all metadata inputs which correspond to untrusted sources. This includes data such as branch names, commit messages, tags, pull request titles, and author information."
- **Applicability:** `maturity-1`, `maturity-2`, `maturity-3`

#### OSPS-BR-01.02 — state: Retired

- **Requirement** (OSPS-BR.yaml OSPS-BR-01 / OSPS-BR-01.02): "Retired in https://github.com/ossf/security-baseline/pull/443"
- **Applicability:** `maturity-1`, `maturity-2`, `maturity-3`

#### OSPS-BR-01.03

- **Requirement** (OSPS-BR.yaml OSPS-BR-01 / OSPS-BR-01.03): "When a CI/CD pipeline operates on untrusted code snapshots, it MUST prevent access to privileged CI/CD credentials and assets."
- **Recommendation:** "CI/CD pipelines should isolate untrusted code snapshots from privileged credentials and assets. In particular, projects should be careful to ensure that workflows which build or execute code prior to review by a collaborator do not have access to CI/CD credentials."
- **Applicability:** `maturity-1`, `maturity-2`, `maturity-3`

#### OSPS-BR-01.04

- **Requirement** (OSPS-BR.yaml OSPS-BR-01 / OSPS-BR-01.04): "CI/CD pipelines which accept trusted collaborator input MUST sanitize and validate that input prior to use in the pipeline."
- **Recommendation:** "CI/CD pipelines should sanitize (quote, escape or exit on expected values) all collaborator inputs on explicit workflow executions. While collaborators are generally trusted, manual inputs to a workflow cannot be reviewed and could be abused by an account takeover or insider threat."
- **Applicability:** `maturity-3`

**External framework relations** (`relates-to`, control-level):

- **Scorecard**: Dangerous-Workflow
- **CSF**: PR.AA-02
- **CRA**: 1.2f
- **SSDF**: PO.3.2, PO.5.2, PS.1, PS.2
- **OpenCRE**: 486-813, 124-564, 347-352
- **SLSA**: Choose an appropriate build platform
- **PSSCRM**: P2.3, P3.2, P3.5, E2.4, E2.5, D2.2
- **PCIDSS**: 2.2.1, 6.4.1
- **800-161**: AC-3, AC-4, AC-4(21), CM-5, CM-7, SI-7
- **UKSSCOP**: Claim 2.1.2, Claim 2.2.2

### OSPS-BR-02 — Assign Unique Version Identifiers

**Objective:** Ensure that each software asset produced by the project is uniquely identified, enabling users to track changes and updates to the project over time.

#### OSPS-BR-02.01

- **Requirement** (OSPS-BR.yaml OSPS-BR-02 / OSPS-BR-02.01): "When an official release is created, that release MUST be assigned a unique version identifier."
- **Recommendation:** "Assign a unique version identifier to each release produced by the project, following a consistent naming convention or numbering scheme. Examples include SemVer, CalVer, or git commit id."
- **Applicability:** `maturity-2`, `maturity-3`

#### OSPS-BR-02.02

- **Requirement** (OSPS-BR.yaml OSPS-BR-02 / OSPS-BR-02.02): "When an official release is created, all assets within that release MUST be clearly associated with the release identifier or another unique identifier for the asset."
- **Recommendation:** "Assign a unique version identifier to each software asset produced by the project, following a consistent naming convention or numbering scheme. Examples include SemVer, CalVer, or git commit id."
- **Applicability:** `maturity-3`

**External framework relations** (`relates-to`, control-level):

- **BPB**: CC-B-5, CC-B-6, CC-B-7
- **CRA**: 1.2f
- **SSDF**: PO.3.2, PS.1, PS.2, PS.3
- **OpenCRE**: 486-813, 124-564
- **SLSA**: Follow a consistent build process, Build platform - Provenance generation - Exists, Build platform - Provenance generation - Authentic
- **PSSCRM**: G1.4, E1.2, E2.1, E2.6
- **PCIDSS**: 6.4.3
- **800-161**: IA-4, SA-15, SI-7, SR-4
- **UKSSCOP**: Claim 1.1.4, Claim 3.1.1, Claim 3.4.2
- **BSI-TR-03185-2**: BR.02

### OSPS-BR-03 — Use Encrypted Channels for Development & Release Activity

**Objective:** Protect the confidentiality and integrity of project source code during development, reducing the risk of eavesdropping or data tampering.

#### OSPS-BR-03.01

- **Requirement** (OSPS-BR.yaml OSPS-BR-03 / OSPS-BR-03.01): "When the project lists a URI as an official project channel, that URI MUST be exclusively delivered using encrypted channels."
- **Recommendation:** "Configure the project's websites and version control systems to use encrypted channels such as SSH or HTTPS for data transmission. Ensure all tools and domains referenced in project documentation can only be accessed via encrypted channels."
- **Applicability:** `maturity-1`, `maturity-2`, `maturity-3`

#### OSPS-BR-03.02

- **Requirement** (OSPS-BR.yaml OSPS-BR-03 / OSPS-BR-03.02): "When the project lists a URI as an official distribution channel, that channel MUST be protected from adversary-in-the-middle attacks using cryptographically authenticated channels."
- **Recommendation:** "Artifacts distributed by the project should be distributed through channels which ensure integrity and authenticity. Use of HTTPS for downloads, signed releases, or distribution through trusted package managers are all acceptable methods to protect against adversary-in-the-middle attacks."
- **Applicability:** `maturity-1`, `maturity-2`, `maturity-3`

**External framework relations** (`relates-to`, control-level):

- **BPB**: B-B-11
- **CRA**: 1.2d, 1.2e, 1.2f, 1.2i, 1.2j, 1.2k
- **SSDF**: PO.3.2, PO.5.2, PS.1, PS.2
- **OpenCRE**: 486-813, 124-564, 263-184
- **SLSA**: Choose an appropriate build platform
- **PSSCRM**: E1.1, E2.2, E2.4, E2.5
- **PCIDSS**: 2.2.1, 2.2.7, 4.2.1, 4.2.2, 6.4.1, 8.3.2
- **800-161**: AC-4, AC-4(21)
- **UKSSCOP**: Claim 3.1.2
- **BSI-TR-03185-2**: BR.03

### OSPS-BR-04 — Publish Change Log With Release

**Objective:** Provide transparency and accountability for changes made to the project's software releases in such a way that users can understand the modifications and improvements included in each release.

#### OSPS-BR-04.01

- **Requirement** (OSPS-BR.yaml OSPS-BR-04 / OSPS-BR-04.01): "When an official release is created, that release MUST contain a descriptive log of functional and security modifications."
- **Recommendation:** "Ensure that all releases include a descriptive change log. It is recommended to ensure that the change log is human-readable and includes details beyond commit messages, such as descriptions of the security impact or relevance to different use cases. To ensure machine readability, place the content under a markdown header such as "## Changelog"."
- **Applicability:** `maturity-2`, `maturity-3`

**External framework relations** (`relates-to`, control-level):

- **BPB**: CC-B-8, CC-B-9, Q-B-7, A-B-1, A-S-1
- **CRA**: 1.2d, 1.2f, 1.2h, 1.2j, 1.2l, 2.5
- **SSDF**: PS.1, PS.2, PS.3, PW.1.2
- **OpenCRE**: 486-813, 124-564, 757-271, 347-352, 263-184, 208-355, 745-356, 732-148
- **SLSA**: Choose an appropriate build platform, Follow a consistent build process, Build platform - Isolation strength - Isolated
- **PSSCRM**: G1.4, E2.1, E2.4, E2.5, E3.1, E3.6
- **PCIDSS**: 6.2.1, 6.4.1, 6.5.1, 6.5.2, 10.2.2
- **800-161**: AU-2, AU-6, AU-10, CM-5, CM-6, MA-1, MA-8, SI-4, SI-5
- **UKSSCOP**: Claim 1.1.4, Claim 2.2.3, Claim 3.1.1
- **BSI-TR-03185-2**: BR.04

### OSPS-BR-05 — Use Standardized Dependency Management Tools

**Objective:** Ensure that the project's build and release pipelines use standardized tools and processes to manage dependencies, reducing the risk of compatibility issues or security vulnerabilities in the software.

#### OSPS-BR-05.01

- **Requirement** (OSPS-BR.yaml OSPS-BR-05 / OSPS-BR-05.01): "When a build and release pipeline ingests dependencies, it MUST use standardized tooling where available."
- **Recommendation:** "Use a common tooling for your ecosystem, such as package managers or dependency management tools to ingest dependencies at build time. This may include using a dependency file, lock file, or manifest to specify the required dependencies, which are then pulled in by the build system."
- **Applicability:** `maturity-2`, `maturity-3`

**External framework relations** (`relates-to`, control-level):

- **BPB**: Q-B-2
- **CRA**: 1.2b, 1.2d, 1.2f, 1.2h, 1.2j, 2.1, 2.2, 2.3
- **SSDF**: PO.3.2, PS.1, PS.2
- **OpenCRE**: 486-813, 124-564, 347-352, 715-334
- **SLSA**: Build platform - Isolation strength - Isolated
- **PSSCRM**: P3.1, P3.5, E2.2, E2.3, E2.4, E2.5
- **SAMM**: Implementation - Secure Build - Build Process Lvl2
- **PCIDSS**: 6.4.3
- **800-161**: AC-4, CM-2, CM-7(4), CM-7(5), RA-5, SA-15, SR-3
- **UKSSCOP**: Claim 1.2.1, Claim 1.2.5

### OSPS-BR-06 — Include Signatures and Hashes With Release

**Objective:** Ensure released software assets can be verified by users to ensure integrity of each asset when it is used.

#### OSPS-BR-06.01

- **Requirement** (OSPS-BR.yaml OSPS-BR-06 / OSPS-BR-06.01): "When an official release is created, that release MUST be signed or accounted for in a signed manifest including each asset's cryptographic hashes."
- **Recommendation:** "Sign all released software assets at build time with a cryptographic signature or attestations, such as GPG or PGP signature, Sigstore signatures, SLSA provenance, or SLSA VSAs. Include the cryptographic hashes of each asset in a signed manifest or metadata file."
- **Applicability:** `maturity-2`, `maturity-3`

**External framework relations** (`relates-to`, control-level):

- **Scorecard**: Signed-Releases
- **SSDF**: PO.5.2, PS.2, PS.2.1, PW.6.2
- **SLSA**: Distribute provenance
- **PSSCRM**: P1.2, P3.2, P3.3, E2.1, E2.2, E2.6
- **SAMM**: Implementation - Secure Deployment - Deployment Process Lvl3
- **PCIDSS**: 2.2.1, 2.2.7, 3.5.1, 4.2.1, 4.2.2, 6.4.1, 8.3.2
- **800-161**: AU-10, MP-1, SA-15, SI-7, SI-7(14)
- **UKSSCOP**: Claim 1.2.2, Claim 3.1.1
- **BSI-TR-03185-2**: BR.03

### OSPS-BR-07 — Secure Secrets and Credentials

**Objective:** Ensure that data which can lead to security vulnerabilities or supply chain compromise is not disclosed, compromised, or misused.

#### OSPS-BR-07.01

- **Requirement** (OSPS-BR.yaml OSPS-BR-07 / OSPS-BR-07.01): "The project MUST prevent the unintentional storage of unencrypted sensitive data, such as secrets and credentials, in the version control system."
- **Recommendation:** "Configure .gitignore or equivalent to exclude files that may contain sensitive information. Use pre-commit hooks and automated scanning tools to detect and prevent the inclusion of sensitive data in commits."
- **Applicability:** `maturity-1`

#### OSPS-BR-07.02

- **Requirement** (OSPS-BR.yaml OSPS-BR-07 / OSPS-BR-07.02): "The project MUST define a policy for managing secrets and credentials used by the project. The policy should include guidelines for storing, accessing, and rotating secrets and credentials."
- **Recommendation:** "Document how secrets and credentials are managed and used within the project. This should include details on how secrets are stored (e.g., using a secrets management tool), how access is controlled, and how secrets are rotated or updated. Ensure that sensitive information is not hard-coded in the source code or stored in version control systems."
- **Applicability:** `maturity-3`

**External framework relations** (`relates-to`, control-level):

- **BPB**: S-B-5
- **SSDF**: PO.1.1, PO.3.1, PO.4.2, PO.5.1, PW.1.2, PW.1.3, PW.5.1
- **UKSSCOP**: Claim 1.4.3, Claim 1.4.5

## DO — Documentation (`baseline/OSPS-DO.yaml`)

Documentation focuses on the information provided to users, contributors, and maintainers of the project. These controls help ensure that the project documentation is comprehensive, accurate, and up-to-date, enabling users to understand the project's features and functionality, maintenance, support, security and release practices.

### OSPS-DO-01 — Publish User Guides for Basic Functionality

**Objective:** Ensure that users have a clear and comprehensive understanding of the project's current features in order to prevent damage from misuse or misconfiguration.

#### OSPS-DO-01.01

- **Requirement** (OSPS-DO.yaml OSPS-DO-01 / OSPS-DO-01.01): "When the project has made a release, the project documentation MUST include user guides for all basic functionality."
- **Recommendation:** "Create user guides or documentation for all basic functionality of the project, explaining how to install, configure, and use the project's features. If there are any known dangerous or destructive actions available, include highly-visible warnings."
- **Applicability:** `maturity-1`, `maturity-2`, `maturity-3`

**External framework relations** (`relates-to`, control-level):

- **BPB**: B-B-1, B-B-9, B-S-7, B-S-9
- **CSF**: GV.OC-04, GV.OC-05
- **CRA**: 1.2b, 1.2j, 1.2k
- **SSDF**: PW.1.2
- **ISO-18974**: 4.1.4
- **OpenCRE**: 036-275
- **PSSCRM**: G5.1, E3.5
- **PCIDSS**: 2.1.1, 2.2.1, 3.1.1, 4.1.1, 5.1.1, 6.1.1, 6.2.1, 7.1.1, 8.1.1, 11.1.1, 12.10.5
- **800-161**: CM-2, PL-2, PL-8, SA-15
- **UKSSCOP**: 4.1
- **BSI-TR-03185-2**: BR.01

### OSPS-DO-02 — Provide Mechanisms for Reporting Defects

**Objective:** Enable users and contributors to report defects or issues with the released software assets, facilitating communication and collaboration on defect fixes and improvements.

#### OSPS-DO-02.01

- **Requirement** (OSPS-DO.yaml OSPS-DO-02 / OSPS-DO-02.01): "When the project has made a release, the project documentation MUST include a guide for reporting defects."
- **Recommendation:** "It is recommended that projects use their VCS default issue tracker. If an external source is used, ensure that the project documentation and contributing guide clearly and visibly explain how to use the reporting system. It is recommended that project documentation also sets expectations for how defects will be triaged and resolved."
- **Applicability:** `maturity-1`, `maturity-2`, `maturity-3`

**External framework relations** (`relates-to`, control-level):

- **BPB**: B-B-3, R-B-1+, R-B-1, R-B-2, R-S-2
- **CSF**: RS.MA-02, GV.RM-05
- **CRA**: 1.2c, 1.2l, 2.1, 2.2, 2.5, 2.6
- **SSDF**: PW.1.2, RV.1.1, RV.2.1, RV.1.2
- **ISO-18974**: 4.2.1
- **SAMM**: Implementation - Defect Management - Defect Tracking Lvl1, Implementation - Defect Management - Defect Tracking Lvl2
- **PCIDSS**: 6.3.2, 6.3.3, 6.5.1, 6.5.2, 12.10.2
- **800-161**: IR-6, SI-4, SI-5
- **UKSSCOP**: 1.1, 1.3
- **BSI-TR-03185-2**: QA.03

### OSPS-DO-03 — Publish Provenance Verification Instructions

**Objective:** Enable users to verify the authenticity and integrity of the project's released software assets, reducing the risk of using tampered or unauthorized versions of the software.

#### OSPS-DO-03.01

- **Requirement** (OSPS-DO.yaml OSPS-DO-03 / OSPS-DO-03.01): "When the project has made a release, the project documentation MUST contain instructions to verify the integrity and authenticity of the release assets."
- **Recommendation:** "Instructions in the project should contain information about the technology used, the commands to run, and the expected output. When possible, avoid storing this documentation in the same location as the build and release pipeline to avoid a single breach compromising both the software and the documentation for verifying the integrity of the software."
- **Applicability:** `maturity-3`

#### OSPS-DO-03.02

- **Requirement** (OSPS-DO.yaml OSPS-DO-03 / OSPS-DO-03.02): "When the project has made a release, the project documentation MUST contain instructions to verify the expected identity of the person or process authoring the software release."
- **Recommendation:** "The expected identity may be in the form of key IDs used to sign, issuer and identity from a sigstore certificate, or other similar forms. When possible, avoid storing this documentation in the same location as the build and release pipeline to avoid a single breach compromising both the software and the documentation for verifying the integrity of the software."
- **Applicability:** `maturity-3`

**External framework relations** (`relates-to`, control-level):

- **BPB**: CC-B-8
- **CRA**: 1.2d
- **SSDF**: PO.4.2, PS.2, PS.2.1, PS.3.1, RV.1.3
- **OpenCRE**: 171-222
- **PSSCRM**: G1.3, G2.5, P1.2, P3.1, P3.2, P3.3, E2.6
- **PCIDSS**: 3.1.1, 3.5.1, 4.1.1, 5.1.1, 6.1.1, 6.2.1, 7.1.1, 8.1.1, 11.1.1
- **800-161**: CM-2, IR-1, MP-1, SA-15, SI-7, SI-7(14)
- **UKSSCOP**: 3.1
- **BSI-TR-03185-2**: BR.01, BR.03

### OSPS-DO-04 — Publish Support Scope and Duration

**Objective:** Provide users with clear expectations regarding the project's support lifecycle in such a way that enables downstream consumers to ensure the continued functionality and security of their systems.

#### OSPS-DO-04.01

- **Requirement** (OSPS-DO.yaml OSPS-DO-04 / OSPS-DO-04.01): "When the project has made a release, the project documentation MUST include a descriptive statement about the scope and duration of support for each release."
- **Recommendation:** "In order to communicate the scope and duration of support for the project's released software assets, the project should have a SUPPORT.md file, a "Support" section in SECURITY.md, or other documentation explaining the support lifecycle, including the expected duration of support for each release, the types of support provided (e.g., bug fixes, security updates), and any relevant policies or procedures for obtaining support."
- **Applicability:** `maturity-3`

**External framework relations** (`relates-to`, control-level):

- **BPB**: R-B-3
- **SSDF**: PO.4.2, PS.3.1, RV.1.3
- **ISO-18974**: 4.1, 4.3.1
- **PSSCRM**: E1.6
- **SAMM**: Operations - Operational Management - System Decommissioning / Legacy Management Lvl1
- **PCIDSS**: 2.1.1, 3.1.1, 3.2.1, 4.1.1, 5.1.1, 6.1.1, 6.3.3, 7.1.1, 8.1.1, 11.1.1
- **800-161**: PL-1, PL-2, SI-4
- **UKSSCOP**: 4.1, 4.2, Claim 4.1.1, Claim 4.1.2, Claim 4.2.1
- **BSI-TR-03185-2**: DE.01

### OSPS-DO-05 — Document Security Update Scope and Duration

**Objective:** Communicate when the project maintainers will no longer fix defects or security vulnerabilities.

#### OSPS-DO-05.01

- **Requirement** (OSPS-DO.yaml OSPS-DO-05 / OSPS-DO-05.01): "When the project has made a release, the project documentation MUST provide a descriptive statement when releases or versions will no longer receive security updates."
- **Recommendation:** "In order to communicate the scope and duration of support for security fixes, the project should have a SUPPORT.md or other documentation explaining the project's policy for security updates."
- **Applicability:** `maturity-3`

**External framework relations** (`relates-to`, control-level):

- **CRA**: 1.2c, 2.6
- **ISO-18974**: 4.1.1, 4.3.1
- **OpenCRE**: 673-475, 053-751
- **PSSCRM**: E1.6
- **SAMM**: Operations - Operational Management - System Decommissioning / Legacy Management Lvl1, Operations - Operational Management - System Decommissioning / Legacy Management Lvl2
- **PCIDSS**: 3.1.1, 3.2.1, 4.1.1, 5.1.1, 6.1.1, 6.3.2, 7.1.1, 8.1.1, 11.1.1
- **800-161**: PL-1, PL-2, SI-4, SI-5
- **UKSSCOP**: 3.5, 4.1, Claim 4.1.1, Claim 4.2.1
- **BSI-TR-03185-2**: DE.01

### OSPS-DO-06 — Publish Dependency Management Policy

**Objective:** Provide information about how the project selects, obtains, and tracks third-party components that are required for the software to function.

#### OSPS-DO-06.01

- **Requirement** (OSPS-DO.yaml OSPS-DO-06 / OSPS-DO-06.01): "When the project has made a release, the project documentation MUST include a description of how the project selects, obtains, and tracks its dependencies."
- **Recommendation:** "It is recommended to publish this information alongside the project's technical & design documentation on a publicly viewable resource such as the source code repository, project website, or other channel."
- **Applicability:** `maturity-2`, `maturity-3`

**External framework relations** (`relates-to`, control-level):

- **BPB**: A-S-1
- **Scorecard**: Pinned-Dependencies
- **CRA**: 2.1
- **OpenCRE**: 613-286, 053-751
- **PSSCRM**: G1.4, G2.4, P3.1, P3.2, P3.4
- **SAMM**: Design - Security Requirements - Supplier Security Lvl2
- **PCIDSS**: 2.1.1, 3.1.1, 4.1.1, 5.1.1, 6.1.1, 6.3.2, 6.4.3, 7.1.1, 8.1.1, 11.1.1, 12.5.2
- **800-161**: CA-7, CM-7(5), CM-8, PM-30, RA-3(1), SA-11, SI-4, SR-3, SR-5, SR-6, SR-7
- **UKSSCOP**: 1.2, 3.3, Claim 1.2.1, Claim 1.2.2
- **BSI-TR-03185-2**: QA.01

### OSPS-DO-07 — Provide Instructions on How to Build From Source

**Objective:** Ensure that users have a clear and comprehensive instructions on how to build the software from source code.

#### OSPS-DO-07.01

- **Requirement** (OSPS-DO.yaml OSPS-DO-07 / OSPS-DO-07.01): "The project documentation MUST include instructions on how to build the software, including required libraries, frameworks, SDKs, and dependencies."
- **Recommendation:** "It is recommended to publish this information alongside the project's contributor documentation, such as in `CONTRIBUTING.md` or other developer task documentation. This may also be documented using `Makefile` targets or other automation scripts."
- **Applicability:** `maturity-2`, `maturity-3`

## GV — Governance (`baseline/OSPS-GV.yaml`)

Governance focuses on the policies and procedures that guide the project's decision-making and community interactions. These controls help ensure that the project is well positioned to respond to both threats and opportunities.

### OSPS-GV-01 — Publish Project Roles and Responsibilities

**Objective:** Document project roles and responsibilities to help project participants, potential contributors, and downstream consumers understand who is working on the project and what areas of authority they may have.

#### OSPS-GV-01.01

- **Requirement** (OSPS-GV.yaml OSPS-GV-01 / OSPS-GV-01.01): "The project documentation MUST include a list of project members with access to sensitive resources."
- **Recommendation:** "Document project participants and their roles through such artifacts as members.md, governance.md, maintainers.md, or similar file within the source code repository of the project. This may be as simple as including names or account handles in a list of maintainers, or more complex depending on the project's governance."
- **Applicability:** `maturity-2`, `maturity-3`

#### OSPS-GV-01.02

- **Requirement** (OSPS-GV.yaml OSPS-GV-01 / OSPS-GV-01.02): "The project documentation MUST include descriptions of the roles and responsibilities for members of the project"
- **Recommendation:** "Document project participants and their roles through such artifacts as members.md, governance.md, maintainers.md, or similar file within the source code repository of the project."
- **Applicability:** `maturity-2`, `maturity-3`

**External framework relations** (`relates-to`, control-level):

- **BPB**: B-S-3, B-S-4
- **OpenCRE**: 013-021
- **PSSCRM**: G2.3, E3.1, E3.3
- **PCIDSS**: 2.1.2, 3.1.1, 3.1.2, 4.1.1, 4.1.2, 5.1.1, 5.1.2, 6.1.1, 6.1.2, 6.5.4, 7.1.1, 7.1.2, 8.1.1, 8.1.2, 11.1.1, 11.1.2, 12.1.3, 12.5.2
- **800-161**: AC-2, AC-3, IA-2, PL-1, PL-4, PM-30
- **UKSSCOP**: Claim 2.1.1

### OSPS-GV-02 — Provide Public Discussion Mechanisms

**Objective:** Encourage open communication and collaboration within the project community by enabling users to provide feedback and discuss proposed changes or usage challenges.

#### OSPS-GV-02.01

- **Requirement** (OSPS-GV.yaml OSPS-GV-02 / OSPS-GV-02.01): "The project MUST have one or more mechanisms for public discussions about proposed changes and usage obstacles."
- **Recommendation:** "Establish one or more mechanisms for public discussions within the project, such as mailing lists, instant messaging, or issue trackers, to facilitate open communication and feedback."
- **Applicability:** `maturity-1`, `maturity-2`, `maturity-3`

**External framework relations** (`relates-to`, control-level):

- **BPB**: B-B-3, B-B-12
- **CRA**: 1.2l, 2.3, 2.4, 2.6
- **SSDF**: PS.3, PW.1.2
- **PCIDSS**: 12.5.2
- **800-161**: AC-21, AU-6, PL-1
- **BSI-TR-03185-2**: QA.03

### OSPS-GV-03 — Publish Contribution Guide

**Objective:** Provide guidance on how to participate in the project, outlining the steps required to submit changes or enhancements to the project's codebase.

#### OSPS-GV-03.01

- **Requirement** (OSPS-GV.yaml OSPS-GV-03 / OSPS-GV-03.01): "The project documentation MUST include an explanation of the contribution process, or clearly state that public contributions are not accepted"
- **Recommendation:** "Create a CONTRIBUTING.md or CONTRIBUTING/ directory to outline the contribution process including the steps for submitting changes, and engaging with the project maintainers."
- **Applicability:** `maturity-1`, `maturity-2`, `maturity-3`

#### OSPS-GV-03.02

- **Requirement** (OSPS-GV.yaml OSPS-GV-03 / OSPS-GV-03.02): "The project documentation MUST include a guide for code contributors that includes requirements for acceptable contributions."
- **Recommendation:** "Extend the CONTRIBUTING.md or CONTRIBUTING/ contents in the project documentation to outline the requirements for acceptable contributions, including coding standards, testing requirements, and submission guidelines for code contributors. It is recommended that this guide is the source of truth for both contributors and approvers."
- **Applicability:** `maturity-2`, `maturity-3`

**External framework relations** (`relates-to`, control-level):

- **BPB**: B-B-4, B-S-3, B-B-4+, R-B-1, Q-G-2
- **CRA**: 1.2l, 2.4
- **SSDF**: PW.1.2
- **ISO-18974**: 4.1.2
- **PSSCRM**: G2.4, P2.2
- **PCIDSS**: 2.1.1, 6.5.4, 8.2.1, 12.5.2
- **800-161**: AC-3, AC-20, PL-1
- **UKSSCOP**: Claim 2.1.1
- **BSI-TR-03185-2**: GV.01, QA.04, QA.05

### OSPS-GV-04 — Require Formal Review of Permission Grants

**Objective:** Ensure that code contributors are vetted and reviewed before being granted elevated permissions to sensitive resources within the project, reducing the risk of unauthorized access or misuse.

#### OSPS-GV-04.01

- **Requirement** (OSPS-GV.yaml OSPS-GV-04 / OSPS-GV-04.01): "The project documentation MUST have a policy that code collaborators are reviewed prior to granting escalated permissions to sensitive resources."
- **Recommendation:** "Publish an enforceable policy in the project documentation that requires code collaborators to be reviewed and approved before being granted escalated permissions to sensitive resources, such as merge approval or access to secrets. It is recommended that vetting includes establishing a justifiable lineage of identity such as confirming the contributor's association with a known trusted organization."
- **Applicability:** `maturity-3`

**External framework relations** (`relates-to`, control-level):

- **BPB**: B-B-5, B-S-3, B-B-4+, Q-G-2
- **CSF**: PR.AA-02, PR.AA-05
- **CRA**: 1.2d, 1.2l, 2.1, 2.2, 2.5, 2.6
- **SSDF**: PO.2, PO.3.2
- **ISO-18974**: 4.1.2
- **OpenCRE**: 123-124, 152-725
- **PSSCRM**: E3.1, E3.3
- **PCIDSS**: 2.1.1, 6.5.4, 8.2.1, 8.2.2
- **800-161**: AC-2, AC-3, AC-4(21), AC-5, AC-6, AC-20, CM-7, IR-4(6), PM-30, SI-4

## LE — Legal (`baseline/OSPS-LE.yaml`)

Legal focuses on the policies and procedures that govern the project's licensing and intellectual property. These controls help ensure that the project's source code is distributed under a recognized and legally enforceable open source software license, reducing the risk of intellectual property disputes or licensing violations.

### OSPS-LE-01 — Require Code Contributors to Assert Right to Commit

**Objective:** Ensure that code contributors are aware of and acknowledge their legal responsibility for the contributions they make to the project, reducing the risk of intellectual property disputes against the project.

#### OSPS-LE-01.01

- **Requirement** (OSPS-LE.yaml OSPS-LE-01 / OSPS-LE-01.01): "The version control system MUST require all code contributors to assert that they are legally authorized to make the associated contributions on every commit."
- **Recommendation:** "Include a DCO in the project's repository, requiring code contributors to assert that they are legally authorized to commit the associated contributions on every commit. Use a status check to ensure the assertion is made. A CLA also satisfies this requirement. Some version control systems, such as GitHub, may include this in the platform terms of service. It is understood that projects with a lengthy history prior to adopting OSPS Baseline may not be able to retroactively enforce this requirement."
- **Applicability:** `maturity-2`, `maturity-3`

**External framework relations** (`relates-to`, control-level):

- **BPB**: B-S-1
- **CRA**: 1.2b, 1.2f
- **SSDF**: PO.3.2, PS.1, PW.1.2, PW.2.1
- **PSSCRM**: E3.1
- **PCIDSS**: 12.8.5
- **800-161**: PL-4

### OSPS-LE-02 — Ensure Project Licenses are Fully Open Source

**Objective:** Ensure that the project's source code is distributed under a recognized and legally enforceable open source software license, providing clarity on how the code can be used and shared by others.

#### OSPS-LE-02.01

- **Requirement** (OSPS-LE.yaml OSPS-LE-02 / OSPS-LE-02.01): "The license for the source code MUST meet the OSI Open Source Definition or the FSF Free Software Definition."
- **Recommendation:** "Add a LICENSE file to the project's repo with a license that is an approved license by the Open Source Initiative (OSI), or a free license as approved by the Free Software Foundation (FSF). Examples of such licenses include the MIT, BSD 2-clause, BSD 3-clause revised, Apache 2.0, Lesser GNU General Public License (LGPL), and the GNU General Public License (GPL). Releasing to the public domain meets this control if there are no other encumbrances such as patents."
- **Applicability:** `maturity-1`, `maturity-2`, `maturity-3`

#### OSPS-LE-02.02

- **Requirement** (OSPS-LE.yaml OSPS-LE-02 / OSPS-LE-02.02): "The license for the released software assets MUST meet the OSI Open Source Definition or the FSF Free Software Definition."
- **Recommendation:** "If a different license is included with released software assets, ensure it is an approved license by the Open Source Initiative (OSI), or a free license as approved by the Free Software Foundation (FSF). Examples of such licenses include the MIT, BSD 2-clause, BSD 3-clause revised, Apache 2.0, Lesser GNU General Public License (LGPL), and the GNU General Public License (GPL). Note that the license for the released software assets may be different than the source code."
- **Applicability:** `maturity-1`, `maturity-2`, `maturity-3`

**External framework relations** (`relates-to`, control-level):

- **BPB**: B-B-6, B-B-7
- **Scorecard**: License
- **CSF**: GV.OC-03
- **CRA**: 1.2b
- **SSDF**: PO.3.2
- **PSSCRM**: G1.2
- **PCIDSS**: 3.2.1
- **800-161**: PL-4
- **BSI-TR-03185-2**: LE.01

### OSPS-LE-03 — Maintain and Release Licenses in a Well Known Location

**Objective:** Ensure that the project's source code and released software assets are distributed with the appropriate license terms, making it clear to users and contributors how each can be used and shared.

#### OSPS-LE-03.01

- **Requirement** (OSPS-LE.yaml OSPS-LE-03 / OSPS-LE-03.01): "The license for the source code MUST be maintained in the corresponding repository's LICENSE file, COPYING file, LICENSES/ directory, or LICENSE/ directory."
- **Recommendation:** "Include the project's source code license in the project's LICENSE file, COPYING file, LICENSES/ directory, or LICENSE/ directory to provide visibility and clarity on the licensing terms. The filename MAY have an extension. If the project has multiple repositories, ensure that each repository includes the license file."
- **Applicability:** `maturity-1`, `maturity-2`, `maturity-3`

#### OSPS-LE-03.02

- **Requirement** (OSPS-LE.yaml OSPS-LE-03 / OSPS-LE-03.02): "The license for the released software assets MUST be included in the released source code, or in a LICENSE file, COPYING file, or LICENSE/ directory alongside the corresponding release assets."
- **Recommendation:** "Include the project's released software assets license in the released source code, or in a LICENSE file, COPYING file, or LICENSE/ directory alongside the corresponding release assets to provide visibility and clarity on the licensing terms. The filename MAY have an extension. If the project has multiple repositories, ensure that each repository includes the license file."
- **Applicability:** `maturity-1`, `maturity-2`, `maturity-3`

**External framework relations** (`relates-to`, control-level):

- **BPB**: B-B-8
- **Scorecard**: License
- **CRA**: 1.2b
- **SSDF**: PO.3.2
- **PSSCRM**: G1.2
- **PCIDSS**: 3.2.1
- **800-161**: PL-4
- **BSI-TR-03185-2**: LE.02

## QA — Quality (`baseline/OSPS-QA.yaml`)

Quality focuses on the processes and practices used to ensure the quality and reliability of the project's source code and software assets. These controls help ensure that the project's source code is well maintained, secure, and reliable, reducing the risk of defects or vulnerabilities in the software.

### OSPS-QA-01 — Publish Source Code and Change History

**Objective:** Enable users to access and review the project's source code and history, promoting transparency and collaboration within the project community.

#### OSPS-QA-01.01

- **Requirement** (OSPS-QA.yaml OSPS-QA-01 / OSPS-QA-01.01): "The project's source code repository MUST be publicly readable at a static URL."
- **Recommendation:** "Use a common VCS such as GitHub, GitLab, or Bitbucket. Ensure the repository is publicly readable. Avoid duplication or mirroring of repositories unless highly visible documentation clarifies the primary source. Avoid frequent changes to the repository that would impact the repository URL. Ensure the repository is public."
- **Applicability:** `maturity-1`, `maturity-2`, `maturity-3`

#### OSPS-QA-01.02

- **Requirement** (OSPS-QA.yaml OSPS-QA-01 / OSPS-QA-01.02): "The version control system MUST contain a publicly readable record of all changes made, who made the changes, and when the changes were made."
- **Recommendation:** "Use a common VCS such as GitHub, GitLab, or Bitbucket to maintain a publicly readable commit history. Avoid squashing or rewriting commits in a way that would obscure the author of any commits."
- **Applicability:** `maturity-1`, `maturity-2`, `maturity-3`

**External framework relations** (`relates-to`, control-level):

- **BPB**: CC-B-1, CC-B-2, CC-B-3, R-B-5
- **CSF**: ID.AM-02, ID.RA-01, ID.RA-08
- **CRA**: 1.2b, 1.2f, 1.2j
- **SSDF**: PS.1, PS.2, PS.3, PW.1.2, PW.2.1
- **ISO-18974**: 4.1.4
- **OpenCRE**: 486-813, 124-564, 757-271
- **SLSA**: Build platform - Isolation strength - Isolated
- **PSSCRM**: P3.5, E2.2
- **SAMM**: Implementation - Secure Build - Build Process Lvl1
- **PCIDSS**: 2.1.1, 6.2.1, 6.5.1, 6.5.2
- **800-161**: RA-5, SA-11, SA-15
- **UKSSCOP**: Claim 2.2.3
- **BSI-TR-03185-2**: QA.02

### OSPS-QA-02 — Publish Software Dependencies

**Objective:** Provide transparency and accountability for the project's dependencies while enabling users and contributors to understand the software's direct dependencies.

#### OSPS-QA-02.01

- **Requirement** (OSPS-QA.yaml OSPS-QA-02 / OSPS-QA-02.01): "When the package management system supports it, the source code repository MUST contain a dependency list that accounts for the direct language dependencies."
- **Recommendation:** "This may take the form of a package manager or language dependency file that enumerates all direct dependencies such as package.json, Gemfile, or go.mod."
- **Applicability:** `maturity-1`, `maturity-2`, `maturity-3`

#### OSPS-QA-02.02

- **Requirement** (OSPS-QA.yaml OSPS-QA-02 / OSPS-QA-02.02): "When the project has made a release, all compiled released software assets MUST be delivered with a software bill of materials."
- **Recommendation:** "It is recommended to auto-generate SBOMs at build time using a tool that has been vetted for accuracy. This enables users to ingest this data in a standardized approach alongside other projects in their environment."
- **Applicability:** `maturity-3`

**External framework relations** (`relates-to`, control-level):

- **BPB**: Q-S-8, Q-S-9
- **CSF**: ID.AM-01, ID.AM-02
- **CRA**: 2.1, 2.2, 2.3
- **SSDF**: PO.3.3, PS.1, PS.2, PS.3.2, PW.4
- **ISO-18974**: 4.1.5, 4.3.1
- **OpenCRE**: 486-813, 124-564, 673-475, 863-521, 613-286
- **PSSCRM**: G1.4, G1.5, G2.5, P3.1, P3.2, P5.1, P5.2, E2.1, E2.2
- **SAMM**: Implementation - Secure Build - Software Dependencies Lvl1
- **PCIDSS**: 6.3.2, 6.4.3, 12.5.1
- **800-161**: CA-7, CM-2, CM-8, PL-8, RA-3(1), RA-5, SA-11, SA-15, SR-3, SR-4
- **UKSSCOP**: Claim 1.2.1, Claim 1.2.2, Claim 3.1.1
- **BSI-TR-03185-2**: QA.01

### OSPS-QA-03 — Address Pass/Fail Checks Before Accepting Changes

**Objective:** Ensure that the project's approvers do not become accustomed to tolerating failing status checks, even if arbitrary, because it increases the risk of overlooking security vulnerabilities or defects identified by automated checks.

#### OSPS-QA-03.01

- **Requirement** (OSPS-QA.yaml OSPS-QA-03 / OSPS-QA-03.01): "When a commit is made to the primary branch, any automated status checks for commits MUST pass or be manually bypassed."
- **Recommendation:** "Configure the project's version control system to require that all automated status checks pass or require manual acknowledgement before a commit can be merged into the primary branch. It is recommended that any optional status checks are NOT configured as a pass or fail requirement that approvers may be tempted to bypass."
- **Applicability:** `maturity-2`, `maturity-3`

**External framework relations** (`relates-to`, control-level):

- **CSF**: ID.IM-02
- **CRA**: 1.2f, 1.2k
- **SSDF**: PO.4.1, PS.1, PS.2, RV.1.2
- **ISO-18974**: 4.1.5
- **OpenCRE**: 263-184, 253-452
- **PSSCRM**: G2.2, G5.3, G5.4, P3.5, P4.1, P4.2
- **SAMM**: Implementation - Secure Build - Build Process Lvl3, Implementation - Secure Build - Software Dependencies Lvl3, Verification - Requirements-driven Testing - Control Verification Lvl1, Verification - Requirements-driven Testing - Control Verification Lvl2, Verification - Requirements-driven Testing - Control Verification Lvl3
- **PCIDSS**: 6.3.1, 6.3.2, 6.5.2
- **800-161**: AU-6, CM-3, CM-6, PL-8, SA-11, SA-15, SR-3
- **UKSSCOP**: Claim 1.3.2, Claim 1.3.3
- **BSI-TR-03185-2**: QA.04

### OSPS-QA-04 — Enforce Security Requirements on All Codebases

**Objective:** Ensure that all codebases produced by the project are well documented and held to the same security standard.

#### OSPS-QA-04.01

- **Requirement** (OSPS-QA.yaml OSPS-QA-04 / OSPS-QA-04.01): "Projects with multiple repositories MUST document a list of codebases that are part of the project."
- **Recommendation:** "Document any additional subproject code repositories produced by the project and compiled into a release. This documentation should include the status and intent of the respective codebase."
- **Applicability:** `maturity-1`, `maturity-2`, `maturity-3`

#### OSPS-QA-04.02

- **Requirement** (OSPS-QA.yaml OSPS-QA-04 / OSPS-QA-04.02): "When the project has made a release comprising multiple source code repositories, all subprojects MUST enforce security requirements that are as strict or stricter than the primary codebase."
- **Recommendation:** "Any additional subproject code repositories produced by the project and compiled into a release must enforce security requirements as applicable to the status and intent of the respective codebase. In addition to following the corresponding OSPS Baseline requirements, this may include requiring a security review, ensuring that it is free of vulnerabilities, and ensuring that it is free of known security issues."
- **Applicability:** `maturity-3`

**External framework relations** (`relates-to`, control-level):

- **CRA**: 1.2b, 1.2f
- **SSDF**: PO.3.2, PO.4.1, PS.1, PS.2, RV.1.2
- **OpenCRE**: 486-813, 124-564
- **SLSA**: Build platform - Isolation strength - Isolated
- **PSSCRM**: G2.2, G5.4
- **PCIDSS**: 6.4.2
- **800-161**: PL-8, SA-15

### OSPS-QA-05 — Prevent Executables in the Codebase

**Objective:** Reduce the risk of including generated executable artifacts in the project's version control system, ensuring that only source code and necessary files are stored in the repository.

#### OSPS-QA-05.01

- **Requirement** (OSPS-QA.yaml OSPS-QA-05 / OSPS-QA-05.01): "The version control system MUST NOT contain generated executable artifacts."
- **Recommendation:** "Remove generated executable artifacts in the project's version control system. It is recommended that any scenario where a generated executable artifact appears critical to a process such as testing, it should be instead be generated at build time or stored separately and fetched during a specific well-documented pipeline step."
- **Applicability:** `maturity-1`, `maturity-2`, `maturity-3`

#### OSPS-QA-05.02

- **Requirement** (OSPS-QA.yaml OSPS-QA-05 / OSPS-QA-05.02): "The version control system MUST NOT contain unreviewable binary artifacts."
- **Recommendation:** "Do not add any unreviewable binary artifacts to the project's version control system. This includes executable application binaries, library files, and similar artifacts. It does not include assets such as graphical images, sound or music files, and similar content typically stored in a binary format."
- **Applicability:** `maturity-1`, `maturity-2`, `maturity-3`

**External framework relations** (`relates-to`, control-level):

- **Scorecard**: Binary-Artifacts
- **CRA**: 1.2b
- **SSDF**: PS.1, PS.2
- **OpenCRE**: 486-813, 124-564
- **PCIDSS**: 6.4.3
- **800-161**: PL-8, SA-15, SR-3
- **BSI-TR-03185-2**: BR.05

### OSPS-QA-06 — Use Automated Testing in CI/CD Pipelines

**Objective:** Ensure that the project uses at least one automated test suite for the source code repository and clearly documents when and how tests are run.

#### OSPS-QA-06.01

- **Requirement** (OSPS-QA.yaml OSPS-QA-06 / OSPS-QA-06.01): "Prior to a commit being accepted, the project's CI/CD pipelines MUST run at least one automated test suite to ensure the changes meet expectations."
- **Recommendation:** "Automated tests should be run prior to every merge into the primary branch. The test suite should be run in a CI/CD pipeline and the results should be visible to all contributors. The test suite should be run in a consistent environment and should be run in a way that allows contributors to run the tests locally. Examples of test suites include unit tests, integration tests, and end-to-end tests."
- **Applicability:** `maturity-2`, `maturity-3`

#### OSPS-QA-06.02

- **Requirement** (OSPS-QA.yaml OSPS-QA-06 / OSPS-QA-06.02): "The project documentation MUST clearly document when and how tests are run."
- **Recommendation:** "Add a section to the contributing documentation that explains how to run the tests locally and how to run the tests in the CI/CD pipeline. The documentation should explain what the tests are testing and how to interpret the results."
- **Applicability:** `maturity-3`

#### OSPS-QA-06.03

- **Requirement** (OSPS-QA.yaml OSPS-QA-06 / OSPS-QA-06.03): "The project documentation MUST include a policy that all major changes to the software produced by the project should add or update tests of the functionality in an automated test suite."
- **Recommendation:** "Add a section to the contributing documentation that explains the policy for adding or updating tests. The policy should explain what constitutes a major change and what tests should be added or updated."
- **Applicability:** `maturity-3`

**External framework relations** (`relates-to`, control-level):

- **BPB**: Q-B-4, Q-B-8, Q-B-9, Q-B-10, Q-S-2
- **Scorecard**: CI-Tests
- **CSF**: ID.AM-02
- **CRA**: 2.3
- **SSDF**: PW.8.2
- **ISO-18974**: 4.1.5
- **OpenCRE**: 207-435, 088-377
- **PSSCRM**: P4.1, P4.2, P4.3, P4.4, E2.4, E2.5
- **SAMM**: Verification - Requirements-driven Testing - Control Verification Lvl1, Verification - Requirements-driven Testing - Control Verification Lvl2, Verification - Requirements-driven Testing - Control Verification Lvl3, Verification - Security Testing - Scalable Baseline Lvl3
- **PCIDSS**: 6.2.3, 6.3.1, 6.3.2, 6.4.2
- **800-161**: SA-11, SA-15, SR-3
- **BSI-TR-03185-2**: QA.04, QA.05

### OSPS-QA-07 — Require Merge Approvals

**Objective:** Ensure that the project's version control system requires at least one non-author human approval of changes before merging into the release or primary branch.

#### OSPS-QA-07.01

- **Requirement** (OSPS-QA.yaml OSPS-QA-07 / OSPS-QA-07.01): "When a commit is made to the primary branch, the project's version control system MUST require at least one non-author human approval of the changes before merging."
- **Recommendation:** "Configure the project's version control system to require at least one non-author human approval of changes before merging into the release or primary branch. This can be achieved by requiring a pull request to be reviewed and approved by at least one other collaborator before it can be merged."
- **Applicability:** `maturity-3`

**External framework relations** (`relates-to`, control-level):

- **BPB**: B-G-3
- **Scorecard**: Code-Review
- **PSSCRM**: G2.4, P3.3, P3.5
- **PCIDSS**: 6.2.3.1, 6.4.2, 6.5.4
- **800-161**: AC-5, AU-6, PL-8, SA-15, SR-3
- **BSI-TR-03185-2**: QA.06

## SA — Security Assessment (`baseline/OSPS-SA.yaml`)

Security Assessment encourages practices that help ensure that the project is well positioned to identify and address security vulnerabilities and threats in the software.

### OSPS-SA-01 — Publish Design Descriptions of System Actors and Actions

**Objective:** Provide an overview of the project's design and architecture, illustrating the interactions and components of the system to help contributors and security reviewers understand the internal logic of the released software assets.

#### OSPS-SA-01.01

- **Requirement** (OSPS-SA.yaml OSPS-SA-01 / OSPS-SA-01.01): "When the project has made a release, the project documentation MUST include design documentation demonstrating all actions and actors within the system."
- **Recommendation:** "Include designs in the project documentation that explains the actions and actors. Actors include any subsystem or entity that can influence another segment in the system. Ensure this is updated for new features or breaking changes."
- **Applicability:** `maturity-2`, `maturity-3`

**External framework relations** (`relates-to`, control-level):

- **BPB**: B-B-1, B-S-7, B-S-8
- **CSF**: ID.AM-02
- **CRA**: 1.2a, 1.2b
- **SSDF**: PO.1, PO.2, PO.3.2
- **OpenCRE**: 155-155, 326-704, 068-102, 036-275, 162-655
- **PSSCRM**: G5.1, P1.1, E3.4, E3.7
- **SAMM**: Operations - Operational Management - Data Protection Lvl2
- **PCIDSS**: 2.2.1, 2.2.3, 2.2.4, 2.2.5, 2.2.6, 3.1.1, 4.1.1, 5.1.1, 6.1.1, 6.2.1, 7.1.1, 8.1.1, 11.1.1, 12.3.1, 12.5.3
- **800-161**: CM-2, PL-8, RA-3, SA-15
- **UKSSCOP**: Claim 1.1.5

### OSPS-SA-02 — Publish External Interface Descriptions

**Objective:** Provide users and developers with an understanding of how to interact with the project's software and integrate it with other systems, enabling them to use the software effectively.

#### OSPS-SA-02.01

- **Requirement** (OSPS-SA.yaml OSPS-SA-02 / OSPS-SA-02.01): "When the project has made a release, the project documentation MUST include descriptions of all external software interfaces of the released software assets."
- **Recommendation:** "Document all software interfaces (APIs) of the released software assets, explaining how users can interact with the software and what data is expected or produced. Ensure this is updated for new features or breaking changes."
- **Applicability:** `maturity-2`, `maturity-3`

**External framework relations** (`relates-to`, control-level):

- **BPB**: B-B-10, B-S-7
- **CSF**: GV.OC-05, ID.AM-01
- **CRA**: 1.2a, 1.2b
- **SSDF**: PW.1.2
- **ISO-18974**: 4.1.4
- **OpenCRE**: 155-155, 068-102, 072-713, 820-878
- **PSSCRM**: E3.4, E3.7
- **PCIDSS**: 2.2.1, 2.2.3, 2.2.4, 2.2.5, 2.2.6, 6.2.1, 12.3.1, 12.8.1
- **800-161**: CM-2, PL-2, PL-8, RA-3, SA-15
- **UKSSCOP**: Claim 1.1.5

### OSPS-SA-03 — Maintain a Project Security Assessment

**Objective:** Provide project maintainers an understanding of how the software can be misused or broken, enabling them to plan mitigations accordingly.

#### OSPS-SA-03.01

- **Requirement** (OSPS-SA.yaml OSPS-SA-03 / OSPS-SA-03.01): "When the project has made a release, the project MUST perform a security assessment to understand the most likely and impactful potential security problems that could occur within the software."
- **Recommendation:** "Performing a security assessment informs both project members as well as downstream consumers that the project understands what problems could arise within the software. Understanding what threats could be realized helps the project manage and address risk. This information is useful to downstream consumers to demonstrate the security acumen and practices of the project. Ensure this is updated for new features or breaking changes."
- **Applicability:** `maturity-2`, `maturity-3`

#### OSPS-SA-03.02

- **Requirement** (OSPS-SA.yaml OSPS-SA-03 / OSPS-SA-03.02): "When the project has made a release, the project MUST perform a threat modeling and attack surface analysis to understand and protect against attacks on critical code paths, functions, and interactions within the system."
- **Recommendation:** "Threat modeling is an activity where the project looks at the codebase, associated processes and infrastructure, interfaces, key components and "thinks like a hacker" and brainstorms how the system be be broken or compromised. Each identified threat is listed out so the project can then think about how to proactively avoid or close off any gaps/vulnerabilities that could arise. Ensure this is updated for new features or breaking changes."
- **Applicability:** `maturity-3`

**External framework relations** (`relates-to`, control-level):

- **BPB**: B-S-8, S-G-1
- **CSF**: ID.RA-01, ID.RA-04, ID.RA-05, DE.AE-07
- **CRA**: 1.1, 1.2j, 1.2k, 2.2
- **SSDF**: PO.5.1, PW.1.1
- **ISO-18974**: 4.1.5
- **OpenCRE**: 068-102, 154-031, 888-770
- **PSSCRM**: G4.3, G5.2, P2.1
- **SAMM**: Governance - Strategy & Metrics - Create and Promote Lvl1, Design - Threat Assessment - Application Risk Profile Lvl1, Design - Threat Assessment - Threat Modeling Lvl1, Verification - Architecture Assessment - Architecture Mitigation Lvl2
- **PCIDSS**: 2.2.4, 2.2.5, 2.2.6, 6.2.1, 6.2.3.1, 6.3.2, 6.4.2, 11.3.1, 12.3.1
- **800-161**: CA-2, CA-2(3), PM-30, RA-3, SA-11, SA-15, SA-15(3), SA-15(8), SI-3, SR-3, SR-3(3), SR-6, SR-7
- **UKSSCOP**: Claim 1.4.1

## VM — Vulnerability Management (`baseline/OSPS-VM.yaml`)

Vulnerability Management focuses on the processes and practices used to identify and address security vulnerabilities in the project's software dependencies. These controls help ensure that the project is well positioned to respond to security threats and vulnerabilities in the software.

### OSPS-VM-01 — Publish Coordinated Vulnerability Disclosure Policy

**Objective:** Establish a process for reporting and addressing vulnerabilities in the project, ensuring that security issues are handled promptly and transparently.

#### OSPS-VM-01.01

- **Requirement** (OSPS-VM.yaml OSPS-VM-01 / OSPS-VM-01.01): "The project documentation MUST include a policy for coordinated vulnerability disclosure (CVD), with a clear timeframe for response."
- **Recommendation:** "Create a SECURITY.md file at the root of the directory, outlining the project's policy for coordinated vulnerability disclosure. Include a method for reporting vulnerabilities. Set expectations for how the project will respond and address reported issues."
- **Applicability:** `maturity-2`, `maturity-3`

**External framework relations** (`relates-to`, control-level):

- **BPB**: R-B-6, R-B-8, R-S-2, S-B-14, S-B-15
- **Scorecard**: Security-Policy
- **CSF**: GV.PO-01, GV.PO-02, ID.RA-01, ID.RA-08
- **CRA**: 2.1, 2.2, 2.3, 2.6, 2.7, 2.8
- **SSDF**: RV.1.3
- **ISO-18974**: 4.1.5, 4.2.1, 4.3.2
- **OpenCRE**: 887-750
- **PSSCRM**: D1.1, D1.2, D1.3, D1.5
- **SAMM**: Governance - Strategy & Metrics - Create and Promote Lvl2, Governance - Policy & Compliance - Policy & Standards Lvl1, Implementation - Defect Management - Defect Tracking Lvl1, Implementation - Defect Management - Defect Tracking Lvl2, Implementation - Defect Management - Defect Tracking Lvl3, Operations - Incident Management - Incident Response Lvl1, Operations - Incident Management - Incident Response Lvl2, Operations - Incident Management - Incident Response Lvl3
- **PCIDSS**: 2.1.1, 3.1.1, 4.1.1, 5.1.1, 6.1.1, 6.3.1, 6.3.2, 7.1.1, 8.1.1, 11.1.1, 11.2.1, 12.1.1, 12.1.3
- **800-161**: IR-1, IR-4, IR-6, IR-7(1), IR-8, SI-2
- **UKSSCOP**: Claim 3.4.1, Claim 3.5.1, Claim 4.1.2
- **BSI-TR-03185-2**: VM.01

### OSPS-VM-02 — Publish Contacts and Process for Reporting Vulnerabilities.

**Objective:** Enable external parties, such as researchers, to easily understand who they should contact in the event that a vulnerability is found, and what process they should follow.

#### OSPS-VM-02.01

- **Requirement** (OSPS-VM.yaml OSPS-VM-02 / OSPS-VM-02.01): "The project documentation MUST contain security contacts."
- **Recommendation:** "Create a security.md (or similarly-named) file that contains security contacts for the project."
- **Applicability:** `maturity-1`

**External framework relations** (`relates-to`, control-level):

- **BPB**: B-S-8
- **Scorecard**: Security-Policy
- **CSF**: GV.PO-01, GV.PO-02, ID.RA-01
- **CRA**: 2.5
- **SSDF**: RV.1.3
- **ISO-18974**: 4.1.1, 4.1.3, 4.1.5, 4.2.2
- **OpenCRE**: 464-513
- **SAMM**: Governance - Policy & Compliance - Policy & Standards Lvl2
- **PCIDSS**: 6.3.3, 12.1.1, 12.10.2
- **800-161**: IR-1, IR-4, IR-6, IR-8
- **UKSSCOP**: 3.2
- **BSI-TR-03185-2**: VM.01

### OSPS-VM-03 — Maintain Private Vulnerability Reporting Process

**Objective:** Provide a means for reporting privately to the security contacts within the project so that security vulnerabilities are not be shared with the public until the project has been provided time to analyze and prepare remediations to protect users of the project.

#### OSPS-VM-03.01

- **Requirement** (OSPS-VM.yaml OSPS-VM-03 / OSPS-VM-03.01): "The project documentation MUST provide a means for private vulnerability reporting directly to the security contacts within the project."
- **Recommendation:** "Provide a means for security researchers to report vulnerabilities privately to the project. This may be a dedicated email address, a web form, VCS specialized tools, email addresses for security contacts, or other methods."
- **Applicability:** `maturity-2`, `maturity-3`

**External framework relations** (`relates-to`, control-level):

- **BPB**: R-B-7
- **CRA**: 2.5, 2.6
- **SAMM**: Operations - Incident Management - Incident Response Lvl3
- **PCIDSS**: 6.3.1, 6.3.3, 12.10.2
- **800-161**: IR-6
- **UKSSCOP**: 3.2
- **BSI-TR-03185-2**: VM.01

### OSPS-VM-04 — Publish Discovered Vulnerabilities

**Objective:** Ensure that project end users have a well known mechanism to understand vulnerabilities found within the project.

#### OSPS-VM-04.01

- **Requirement** (OSPS-VM.yaml OSPS-VM-04 / OSPS-VM-04.01): "The project documentation MUST publicly publish data about discovered vulnerabilities."
- **Recommendation:** "Provide information about known vulnerabilities in a predictable public channel, such as a CVE entry, blog post, or other medium. To the degree possible, this information should include affected version(s), how a consumer can determine if they are vulnerable, and instructions for mitigation or remediation."
- **Applicability:** `maturity-2`, `maturity-3`

#### OSPS-VM-04.02

- **Requirement** (OSPS-VM.yaml OSPS-VM-04 / OSPS-VM-04.02): "Any vulnerabilities in the software components not affecting the project MUST be accounted for in a VEX document, augmenting the vulnerability report with non-exploitability details."
- **Recommendation:** "Establish a VEX feed communicating the exploitability status of known vulnerabilities, including assessment details or any mitigations in place preventing vulnerable code from being executed."
- **Applicability:** `maturity-3`

**External framework relations** (`relates-to`, control-level):

- **CSF**: ID.RA-01
- **CRA**: 1.2a, 1.2b, 2.1, 2.4, 2.6
- **SSDF**: PO.4.1, RV.2.1, RV.2.2
- **ISO-18974**: 4.1.5
- **PSSCRM**: G2.2, D1.1
- **PCIDSS**: 6.2.3, 6.3.1, 6.3.2, 6.3.3, 11.3.1
- **800-161**: CA-7, CM-3, CM-8, IR-5, SI-2, SI-4, SI-5
- **UKSSCOP**: 3.4, 3.5, 4.3
- **BSI-TR-03185-2**: VM.02

### OSPS-VM-05 — Publish and Enforce a Dependency Remediation Policy

**Objective:** Identify and address defects and security weaknesses in the project's imported code early in the development process, reducing the risk of shipping insecure software.

#### OSPS-VM-05.01

- **Requirement** (OSPS-VM.yaml OSPS-VM-05 / OSPS-VM-05.01): "The project documentation MUST include a policy that defines a threshold for remediation of SCA findings related to vulnerabilities and licenses."
- **Recommendation:** "Document a policy in the project that defines a threshold for remediation of SCA findings related to vulnerabilities and licenses. Include the process for identifying, prioritizing, and remediating these findings."
- **Applicability:** `maturity-3`

#### OSPS-VM-05.02

- **Requirement** (OSPS-VM.yaml OSPS-VM-05 / OSPS-VM-05.02): "The project documentation MUST include a policy to address SCA violations prior to any release."
- **Recommendation:** "Document a policy in the project to address applicable Software Composition Analysis results before any release, and add status checks that verify compliance with that policy prior to release."
- **Applicability:** `maturity-3`

#### OSPS-VM-05.03

- **Requirement** (OSPS-VM.yaml OSPS-VM-05 / OSPS-VM-05.03): "All changes to the project's codebase MUST be automatically evaluated against a documented policy for malicious dependencies and known vulnerabilities in dependencies, then blocked in the event of violations, except when declared and suppressed as non-exploitable."
- **Recommendation:** "Create a status check in the project's version control system that runs a Software Composition Analysis tool on all changes to the codebase. Require that the status check passes before changes can be merged."
- **Applicability:** `maturity-3`

**External framework relations** (`relates-to`, control-level):

- **BPB**: B-S-8, Q-B-12, Q-S-9, S-B-14, S-B-15, A-B-1, A-B-3, A-B-8, A-S-1
- **Scorecard**: Security-Policy, Vulnerabilities
- **CSF**: GV.RM-05, GV.RM-06, GV.PO-01, GV.PO-02, ID.RA-01, ID.RA-08, ID.IM-02
- **CRA**: 1.2a, 1.2b, 1.2c, 2.1, 2.2, 2.3, 2.4
- **SSDF**: PO.4, PW.1.2, PW.8.1, RV.1.2, RV.1.3, RV.2.1, RV.2.2
- **ISO-18974**: 4.1.5, 4.2.1, 4.2.2, 4.3.2
- **OpenCRE**: 155-155, 124-564, 757-271, 464-513, 611-158, 207-435, 088-377
- **PSSCRM**: G5.4, P4.1, P4.2, P4.3, P4.4, P4.5
- **SAMM**: Implementation - Secure Build - Build Process Lvl3, Implementation - Secure Build - Software Dependencies Lvl3, Verification - Security Testing - Scalable Baseline Lvl1, Verification - Security Testing - Scalable Baseline Lvl3
- **PCIDSS**: 6.2.3, 6.3.1, 6.3.2, 6.4.1, 6.4.2
- **800-161**: CA-7, RA-5, SA-11, SI-2, SI-3
- **UKSSCOP**: 1.2, 3.3

### OSPS-VM-06 — Publish and Enforce an Application Security Testing Policy

**Objective:** Identify and address defects and security weaknesses in the project's codebase early in the development process, reducing the risk of shipping insecure software.

#### OSPS-VM-06.01

- **Requirement** (OSPS-VM.yaml OSPS-VM-06 / OSPS-VM-06.01): "The project documentation MUST include a policy that defines a threshold for remediation of SAST findings."
- **Recommendation:** "Document a policy in the project that defines a threshold for remediation of Static Application Security Testing (SAST) findings. Include the process for identifying, prioritizing, and remediating these findings."
- **Applicability:** `maturity-3`

#### OSPS-VM-06.02

- **Requirement** (OSPS-VM.yaml OSPS-VM-06 / OSPS-VM-06.02): "All changes to the project's codebase MUST be automatically evaluated against a documented policy for security weaknesses and blocked in the event of violations except when declared and suppressed as non-exploitable."
- **Recommendation:** "Create a status check in the project's version control system that runs a Static Application Security Testing (SAST) tool on all changes to the codebase. Require that the status check passes before changes can be merged."
- **Applicability:** `maturity-3`

**External framework relations** (`relates-to`, control-level):

- **BPB**: B-S-8, Q-B-12, Q-S-9, S-B-14, S-B-15, A-B-1, A-B-3, A-B-8, A-S-1
- **Scorecard**: Security-Policy, Vulnerabilities, SAST
- **CSF**: GV.RM-05, GV.RM-06, GV.PO-01, GV.PO-02, ID.RA-01, ID.RA-08, ID.IM-02
- **CRA**: 1.2a, 1.2b, 1.2c, 2.1, 2.2, 2.3, 2.4
- **SSDF**: PO.4, PW.1.2, PW.8.1, RV.1.2, RV.1.3, RV.2.1, RV.2.2
- **ISO-18974**: 4.1.5, 4.2.1, 4.2.2, 4.3.2
- **OpenCRE**: 155-155, 124-564, 757-271, 464-513, 611-158, 207-435, 088-377
- **PSSCRM**: G5.4, P4.1, P4.2, P4.3, P4.4, P4.5
- **SAMM**: Implementation - Secure Build - Build Process Lvl3, Implementation - Secure Build - Software Dependencies Lvl3, Verification - Security Testing - Scalable Baseline Lvl1, Verification - Security Testing - Scalable Baseline Lvl3
- **PCIDSS**: 6.2.3, 6.3.1, 6.3.2, 6.4.1, 6.4.2, 6.5.2
- **800-161**: CA-7, RA-5, SA-11, SI-2, SI-3
- **UKSSCOP**: 1.3, 1.4
- **BSI-TR-03185-2**: QA.05

## External frameworks (`metadata.mapping-references`; mapping documents `baseline/mappings/`)

| id | title | version | url | mapping document | mappings |
|---|---|---|---|---|---|
| `BPB` | OpenSSF Best Practices Badge | 2024 | https://github.com/coreinfrastructure/best-practices-badge/blob/main/criteria/criteria.yml | `osps-to-bpb.yaml` | 30 |
| `Scorecard` | OpenSSF Scorecard | 5.0 | https://github.com/ossf/scorecard | `osps-to-scorecard.yaml` | 13 |
| `CSF` | NIST Cybersecurity Framework | 2.0 | https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf | `osps-to-csf.yaml` | 21 |
| `CRA` | Cyber Resilience Act | 20.11.2024 | https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202402847#tit_1 | `osps-to-cra.yaml` | 35 |
| `SSDF` | Secure Software Development Framework | 1.1 | https://csrc.nist.gov/pubs/sp/800/218/final | `osps-to-ssdf.yaml` | 35 |
| `ISO-18974` | ISO/IEC 18974 | 1.0 - 2023-12 | https://openchainproject.org/security-assurance | `osps-to-iso-18974.yaml` | 17 |
| `OpenCRE` | Open Cybersecurity Reference Architecture | 2024 | https://github.com/OWASP/OpenCRE | `osps-to-opencre.yaml` | 28 |
| `SLSA` | Supply-chain Levels for Software Artifacts | 1.0 | https://github.com/slsa-framework/slsa | `osps-to-slsa.yaml` | 9 |
| `PSSCRM` | Proactive Software Supply Chain Risk Management Framework | 1.0 | https://arxiv.org/pdf/2404.12300 | `osps-to-psscrm.yaml` | 34 |
| `SAMM` | OWASP Software Assurance Maturity Model | 2.0 | https://owaspsamm.org/model/ | `osps-to-samm.yaml` | 19 |
| `PCIDSS` | Payment Card Industry Data Security Standard | 4.0.1 | https://docs-prv.pcisecuritystandards.org/PCI%20DSS/Standard/PCI-DSS-v4_0_1.pdf | `osps-to-pcidss.yaml` | 39 |
| `800-161` | NIST Special Publication 800-161 - Cybersecurity Supply Chain Risk Management Practices for Systems and Organizations | r1-upd1 | https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-161r1-upd1.pdf | `osps-to-800-161.yaml` | 39 |
| `UKSSCOP` | United Kingdom National Cyber Security Centre Software Security Code of Practice | 2025-05-07 | https://www.ncsc.gov.uk/guidance/software-security-code-of-practice-assurance-principles-claims | `osps-to-uksscop.yaml` | 31 |
| `BSI-TR-03185-2` | BSI TR-03185-2 Secure Software Lifecycle for Open Source Software | v1.1.0 | https://www.bsi.bund.de/SharedDocs/Downloads/EN/BSI/Publications/TechGuidelines/TR03185/BSI-TR-03185-2.pdf?__blob=publicationFile&v=5 | `osps-to-bsi-tr-03185-2.yaml` | 28 |

Every mapping document declares `source-reference: {reference-id: osps-baseline, entry-type: Control}`,
`target-reference: {entry-type: Guideline}`, and every mapping uses `relationship: relates-to`; per the
documents' own metadata, "strength, confidence-level, and rationale are left unset and should be added as
the mappings are individually reviewed." The published page adds: "These are not guaranteed to be 100%
matches, but instead serve as references to external elements that the Baseline maintainers believe relate to
the Baseline control. This is not a functional connection, and does not imply that progress on one will
necessarily result in progress on the other."

## Lexicon (`baseline/lexicon.yaml`, 40 terms)

- **Administrator** — Any human who can modify settings on the target resource.
- **Arbitrary Code** — Code provided by an external source that is executed by a system without validation or restriction.
- **Attack Surface Analysis** — Attack Surface Analysis is about mapping out what parts of a system need to be reviewed and tested for security vulnerabilities. The point of Attack Surface Analysis is to understand the risk areas in an application, to make developers and security specialists aware of what parts of the application are open to attack, to find ways of minimizing this, and to notice when and how the Attack Surface changes and what this means from a risk perspective. See OWASP's Attack Surface Analysis Cheat Sheet for more information.
  - reference: https://cheatsheetseries.owasp.org/cheatsheets/Attack_Surface_Analysis_Cheat_Sheet.html
- **Automated Test Suite** — A collection of pre-written test cases that, when invoked, execute the software to verify that actual results are expected results without requiring manual intervention. An automated test suite must return an overall "pass" or "fail" result, and is often implemented using a test framework. Common ways to invoke automated tests include `make check`, `make test`, `npm test`, and `cargo test` manually or as part of a Continuous Integration workflow.
- **Build and Release Pipeline** — A series of automated processes that compile and deploy software. Similar to the generic term CI/CD Pipelines, but this term excludes some pipelines, such as pre-merge status checks.
  - synonyms: Build and Release Pipelines
- **Code** — A set of deterministic instructions that a computer can execute to perform specific tasks.
- **Change** — Any alteration of the project's codebase, CI/CD Pipelines, or documentation. This may include addition, deletion, or modification of content.
- **CI/CD Pipeline** — Automated pipelines for Continuous Integration and Continuous Delivery. Responsible for building, testing, and delivering changes. These pipelines integrate contributions frequently, enabling rapid and reliable software delivery. CI focuses on testing and building code, while CD delivers software to location such as a package registry. In the context of the Open Source Project Security Baseline, CD refers only to continuous delivery, not to continuous deployment, as sometimes used elsewhere.
- **Contributor License Agreement** — A legal agreement used to assign some of a contributor's rights covered by copyright laws to a project. This is often used to enable a project to make future changes to a work's license without requiring the assent of every contributor.
  - synonyms: CLA
- **Contributor** — Any entity that has made a change to the contents of a repository.
- **Collaborator** — Any entity who has any level of permissions issued by administrators of the repository.
- **Commit** — A record of a single change submitted to the version control system. Each commit includes details such as the modifications made, the contributor who made them, and the timestamp of the change.
- **Coordinated Vulnerability Disclosure** — A process of gathering information from vulnerability finders, coordinating the sharing of that information between relevant stakeholders, and disclosing the existence of software vulnerabilities and their mitigations to various stakeholders including the public.
  - synonyms: CVD
  - reference: https://certcc.github.io/CERT-Guide-to-CVD/
  - reference: https://www.first.org/global/sigs/vulnerability-coordination/multiparty/guidelines-v1-1
  - reference: https://docs.github.com/en/code-security/security-advisories/guidance-on-reporting-and-writing-information-about-vulnerabilities/about-coordinated-disclosure-of-security-vulnerabilities
- **Defect** — Errors or flaws in the software that cause it to produce incorrect or unintended results, or to behave in an unintended way. Defects can include bugs, vulnerabilities, or other issues that impact the software's functionality or security. Defects may have originally been intentional, but a change in environment or understanding has made them undesirable.
- **Developer Certificate of Origin** — An assertion made by a contributor that they have the legal right to make a specific contribution to a project. This is often indicated by using the `--signoff` option to `git commit`.
  - synonyms: DCO
  - reference: https://developercertificate.org/
- **OpenEoX** — An initiative aimed at standardizing the way End-of-Life and End-of-Support information is exchanged within the software and hardware industries. Covering both vendors and open-source maintainers, OpenEoX strives to provide a transparent, efficient, and unified approach to managing product lifecycles.
  - reference: https://openeox.org/
- **Exploitable Vulnerabilities** — Defects in the software that can be leveraged by attackers to gain unauthorized access, execute arbitrary code, or cause other undesired outcomes.
  - synonyms: Exploitable Vulnerability
- **License** — A legal document that defines the terms under which the software can be used, modified, and distributed. May be stored at the top level of the repository in a file named `LICENSE` or within files in a directory named `LICENSE/`. The license applies to repository contents and any released software assets, unless otherwise stated.
- **Known Vulnerabilities** — Publicly acknowledged exploitable vulnerabilities that have been identified within the software. These vulnerabilities often have associated advisories, patches, or recommended mitigations. All proposed changes to the project's codebase must be automatically evaluated against a documented policy for known vulnerabilities and blocked in the event of violations.
  - synonyms: Known Vulnerability
- **Maintainer** — A human collaborator who is able to authorize changes to the contents of a repository.
- **Multi-factor Authentication** — An authentication method that requires two or more verification factors (e.g., a password and a token) to gain access to a resource. This method strengthens security by requiring multiple forms of identification.
  - synonyms: MFA
- **Primary Branch** — The main development branch in the version control system, representing the latest stable codebase. Releases are typically made from this branch. Commonly named `main` or `master`. In some situations where branches are not featured, a repository with forked repositories will have the original repo acting as an equivalent to the primary branch.
- **Private Vulnerability Reporting** — The process of privately reporting a vulnerability to the project maintainers or security team before disclosing it publicly. This allows the project to address the issue before it becomes widely known.
  - synonyms: Private Vulnerability Disclosure, Private Security Vulnerability Reporting
  - reference: https://docs.github.com/en/code-security/security-advisories/guidance-on-reporting-and-writing-information-about-vulnerabilities/privately-reporting-a-security-vulnerability
- **Project** — A group of people and resources that coordinate to produce a release.
- **Project Documentation** — Written materials related to the project, such as user guides, developer guides, and contribution guidelines. These documents help users and developers understand, contribute to, and interact with the software. At release time, this may include provenance information, licensing details, and other metadata.
- **Sensitive Data** — Information that, if disclosed to unauthorized parties, would lead to unauthorized access, data exfiltration, financial loss, or other undesirable outcomes. This includes secrets (like passwords, access tokens, etc.), financial account information, personally identifiable information (PII), and data about embargoed vulnerabilities.
- **Sensitive Resource** — Resources that, if compromised, would provide a vector for further compromising software build and delivery or for disclosing sensitive data to unauthorized parties. This includes build systems, image repositories, and data storage.
- **Software Provenance** — Information about the origin and history of the released software assets. This may include details about its development, dependencies, vulnerabilities, contributors, and licensing.
  - synonyms: Provenance
- **Release** — - _(verb)_ The process of making a version-controlled bundle of assets available to users, such as through a package registry. - _(noun)_ A version-controlled bundle of assets made available to users.
- **Released Software Asset** — Deliverables provided to users as part of a release. These assets can include binaries, libraries, or containers.
- **Repository** — A storage location managed by a version control system where the project's code, documentation, and other resources are stored.
  - synonyms: Repo, Repositories
- **Software Bill of Materials** — A list of all components that make up a given piece of software or hardware, formatted as CycloneDX or SPDX. This list must include the following data elements for the components included in the released software asset: license, supplier name, filename of the component, component name, component version, software identifiers, relationship between the components, author of the SBOM data and timestamp. Additionally, for deployable and executable components, the SBOM should record their cryptographic hashes.
  - synonyms: SBOM, SBOMs
  - reference: https://www.ntia.gov/sites/default/files/publications/sbom_minimum_elements_report_0.pdf
  - reference: https://www.cisa.gov/sites/default/files/2023-04/sbom-types-document-508c.pdf
  - reference: https://spdx.dev
  - reference: https://cyclonedx.org
- **Software Composition Analysis** — The process of identifying and cataloging all components and dependencies in a software codebase. SCA is essential for managing security vulnerabilities and ensuring compliance with organizational policies.
  - synonyms: SCA
- **Status Check** — Automated tests or validations that run on commits before they are merged. Status checks ensure that any changes meet the project's quality and security standards.
- **Subproject** — A codebase that is part of the project but maintained in a separate repository. Subprojects may be compiled into the primary project or used as standalone components.
- **Threat Modeling** — Threat modeling is an activity where the project looks at the codebase, associated processes and infrastructure, interfaces, key components and "thinks like a hacker" to brainstorm how the system be be broken or compromised. Each identified threat is listed out so the project can then think about how to proactively avoid or close off any gaps/vulnerabilities that could arise. Examples of threat modeling methodologies include the Shostack "4 Questions" model, STRIDE, and tools such as the Elevation of Privilege Threat Modeling Card Game or Threat Dragon.
  - reference: https://github.com/adamshostack/4QuestionFrame
  - reference: https://owasp.org/www-community/Threat_Modeling_Process
  - reference: https://www.microsoft.com/en-us/download/details.aspx?id=20303
  - reference: https://owasp.org/www-project-threat-dragon
- **Version Identifier** — A label assigned to a specific release of the software, such as `v1.2.3`. Commonly recommended formats are Semantic Versioning or Calendar Versioning.
- **User** — A human making use of project resources, such as the software, documentation, or other community resources. This includes both end-users and contributors.
  - synonyms: Person
- **Version Control System** — A tool that facilitates collaboration among contributors by tracking changes, managing collaborator permissions, and providing configuration options. Examples of version control systems include Git, Subversion, and Mercurial.
  - synonyms: VCS
- **Vulnerability Reporting** — The act of identifying and documenting exploitable vulnerabilities in released software assets. This may include privately or openly reporting vulnerabilities to maintainers, security teams, or the public, as well as tracking the resolution of these vulnerabilities.
  - reference: https://docs.github.com/en/code-security/security-advisories/guidance-on-reporting-and-writing-information-about-vulnerabilities/privately-reporting-a-security-vulnerability

## Maintenance rules bearing on identifiers (`docs/maintenance.md`)

- "Identifiers for retired controls MUST NOT be reused. Retired identifiers will remain in the source yaml files, clearly marked."
- "Substantial changes to the meaning of a control will be treated as a new control, resulting in a new identifier. Minor changes, including a change in level, between Baseline versions will not result in a new identifier."
- "Versions will follow a calendar-based identification system, using the `YYYY-MM-DD` format."
- "Downstream consumers of the OSPS Baseline should specify their compliance against a specific version." (docs/index.md)


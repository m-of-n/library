---
schema: "library-normative/v1"
id: sp-800-204d-normative
record: sp-800-204d
kind: normative
type: normative
title: "sp-800-204d — normative statements"
extracted: "2026-10-02"
updated: "2026-10-02"
reviewed_by: ""
---

Source: NIST SP 800-204D, *Strategies for the Integration of Software Supply Chain Security in DevSecOps CI/CD Pipelines*, February 2024 (final), sha256 `74e404d9…d000`. Every quotation is verbatim from the PDF (pdftotext rendering, whitespace normalised; each checked by script as a substring of the source). The document uses **lowercase** modals only (no BCP 14 keywords). Each statement carries its locator and its id in `requirements.yaml` (`sp-800-204d#R-NNNN`); the source's own designators (PULL-PUSH_REQ-n, COMMIT-REQ-n, DEPLOY-REQ-n, GitOps-REQ-n) are kept with the source's inconsistent `_`/`-` spelling. `→ SSDF x` is the source's own Appendix A mapping (or our inferred one, marked in requirements.yaml).

Front matter (FISMA authority boilerplate with one "shall" and two "should") constrains NIST's publication process, not an implementer, and is excluded.

## Definitions and model statements (normative vocabulary)

- (§2.1) **SSC attack forms.** "An SSC attack can take on several forms, such as: • Subverting, removing, or introducing a step within the SSC to maliciously modify or sabotage the resulting software product • Stealing credentials from the build system to mint and sign unauthorized malicious software • Causing naming collisions"
- (§2.1) **SBOM limits.** "However, while SBOMs enable the identification of components and provenance, they do not provide enough information to address vulnerabilities nor content to address software defects. Hence, SBOMs alone cannot be used for vulnerability management. They simply provide the list of components to focus on when addressing vulnerabilities or defects in software."
- (§2.4) **SSC model.** "At a high level, an SSC is a collection of steps that create, transform, and assess the quality and policy conformance of software artifacts. These steps are often carried out by different actors who use and consume artifacts to produce new artifacts."
- (§2.4 fn 1) **Actor.** "An "actor" can also be a non-human, such as a build orchestrator."
- (§2.4 fn 2) **Step.** "An SSC step stands for an SSC activity (e.g., build)."
- (§2.4.1) **Defect vs attack.** "However, while the line between a defect and an attack is often blurred in the context of SSC, the guiding principle is that of intent — that is, whether or not the upstream actor intended to exploit that defect."
- (§2.4.2) **SSC attack.** "In contrast to defects, an SSC attack is when a malicious party tampers with the steps, artifacts, or actors within the chain to compromise the consumers of a software artifact down the line. Explicitly, an SSC attack is a three-stage process: 1. Artifact, step, or actor compromise: An attacker compromises an element of the SSC (see Fig. 1) to modify an artifact or the information of such. 2. Propagation: The attack propagates throughout the chain."
- (§2.4.2) **SSC attack stage 3.** "3. Exploitation: The attacker exploits the target to achieve their goals (e.g., exfiltration of data, cryptojacking)."
- (§4) **Artifact, repository.** "In this document, the term “artifacts” denotes source code as well as the things generated from it, such as builds and packages. Each of the artifacts is associated with an owner. The logical containers that hold these artifacts are called repositories."
- (§4) **CI/CD pipeline, workflow.** "These stages and the various tasks performed at each stage are collectively called CI/CD pipelines. In other words, CI/CD pipelines use processes called workflows to transform source artifacts to deployable packages in production environments."
- (§4) **Provenance data.** "Provenance data are associated with the chronology of the origin, development, ownership, location, and changes to a system or system component, including the personnel and processes that enabled those changes or modifications."
- (§5.1.3) **Software update system types.** "There are several types of software update systems [11]: • Package managers that are responsible for all of the software installed on a system • Application updaters that are only responsible for individual installed applications"
- (§5.1.3) **Software update system types (cont.).** "• Software library managers that install software that adds functionality, such as plugins or programming language libraries."
- (§5.1.3) **Framework.** "A framework is a set of libraries, file formats, and utilities that can be used to secure new and existing software update systems."
- (§5.2.1) **GitOps.** "The operations are collectively called GitOps, which is an automated deployment process facilitated by open-source tools, such as Argo CD and Flux."

Figure 1 (§2.4, image, transcribed from the rendered page): **Artifacts** —Uses→ **Step** —Produces→ **Artifacts**; **Actor** —carries out→ **Step**; **Resources** —Used for→ **Step**.

## 1. Introduction

### §1

- (§1) [R-0001] *requirement* — "Thus, in the context of cloud-native applications, SSC security assurance measures must be integrated into CI/CD pipelines."

## 2. Software Supply Chain (SSC) — Definition and Model

### §2.1

- (§2.1) [R-0002] *recommendation* — "SSC security should also account for discovering and tracking software security defects rather than simply mitigating attacks."
- (§2.1) [R-0003] *requirement* — "To facilitate this, the software bill of materials (SBOM) must be shared with end users so that they can build inventories of software components."

## 3. SSC Security — Risk Factors and Mitigation Measures

### §3.1.1

- (§3.1.1) [R-0004] *recommendation* — "Developer workstations and their environments present a fundamental risk to the security of an SSC and should not be trusted as part of the build process since they are at risk of compromise."
- (§3.1.1) [R-0005] *practice* — "Mature SDLC processes accept code and assets into their software configuration management (SCM) mainline and versions branches only after code reviews and scanners are in place."
### §3.1.2

- (§3.1.2) [R-0006] *recommendation* — "Therefore, companies should be aware of these risks and take appropriate measures (see Sec. 3.2) to secure their SSC."
- (§3.1.2) [R-0007] *recommendation* — "Organizations should be aware of these situations and take suitable measures to avoid such practices."
### §3.1.3

- (§3.1.3) [R-0008] *recommendation* — "Companies should identify potential risks and vulnerabilities, assess their security posture, and implement appropriate defensive measures to mitigate threats to their SDLC environment."
- (§3.1.3) [R-0009] *requirement* — "In the case of ingested code, it is essential to verify the provenance information of the component being used to ensure that it is what it says it is and is coming from an expected source."
- (§3.1.3) [R-0010] *practice* — "Mitigations for this involve caching or curating packages and components for preferred use."
### §3.1.4

- (§3.1.4) [R-0011] *recommendation* — "Companies should identify critical assets and implement controls to protect them from unauthorized access, such as access controls, multi-factor authentication, encryption of data at rest and in transit, and data loss prevention (DLP) measures."
### §3.2

- (§3.2) [R-0012] *requirement* — "It is crucial to assess security risks and implement appropriate defensive measures to protect software supply chains against compromise."
- (§3.2) [R-0013] *practice* — "The following generic mitigation measures are applicable to the entire SDLC but are particularly relevant to an SSC: • Patch management • Dependency management • Authentication and authorization • Malware protection • Secure SDLC • Data protection • Physical security • Audit and monitoring • Adherence to applicable security standards (e.g., regulatory requirements)"
- (§3.2) [R-0014] *recommendation* — "They should regularly assess their security posture, identify potential weaknesses and vulnerabilities, and implement appropriate defensive measures to address them."
- (§3.2) [R-0015] *practice* — "Organizational network policies that account for and actively block maliciously known content-serving domains can reduce the use of software from non-curated or undesired locations."
- (§3.2) [R-0016] *practice* — "Another integral part of SSC security involves capturing the dependencies (e.g., package name, version) of the artifacts in a central repository."
- (§3.2) [R-0017] *recommendation* — "Organizations should also ensure that their SDLC environment remains compliant with various security and other relevant standards, such as the Open Worldwide Application Security Project (OWASP) Top Ten, SP 800-53, Health Insurance Portability and Accountability Act (HIPAA), and Payment Card Industry Data Security Standard (PCI DSS)."
- (§3.2) [R-0018] *recommendation* — "However, all developer systems should meet a predefined minimum baseline for security to ensure that the operating system and applications are kept up to date with the latest security patches, individual and unshared user accounts are adequately protected, and proper access controls are enforced when interacting with SCM."
### §3.2.1

- (§3.2.1) [R-0019] *practice* — "Independent and open-source developers will need to follow best practices to protect their own systems."
- (§3.2.1) [R-0020] *recommendation* — "Government and enterprise environments should establish and adhere to a well-defined security policy that meets regulatory requirements and industry best practices."
- (§3.2.1) [R-0021] *recommendation* — "Since the development of such a policy is out of scope for this document, readers should refer to SP 800-53r5 (Revision 5) [6] for a more complete treatment of this topic."
- (§3.2.1 bullet 1) [R-0022] *recommendation* — "The security team should establish a policy for trusted sources of OSS (e.g., allow lists) that includes reviewing minimum coding requirements, reputational standards, and distributing source code in a digitally signed package."
- (§3.2.1 bullet 2) [R-0023] *recommendation* — "The security team should approve the merging of unverified sources of OSS."
- (§3.2.1 bullet 3) [R-0024] *recommendation* — "Developers should download OSS as source code rather than pre-compiled libraries or binaries, when available."
- (§3.2.1 bullet 4) [R-0025] *recommendation* — "Developers should verify digital signatures, run vulnerability scans, check for recent updates on newly downloaded OSS’s source-code packages, and generate an SBOM with dependency scanning on the first commit in order to identify the risks of any upstream or downstream dependencies within the OSS."
- (§3.2.1 bullet 5) [R-0026] *recommendation* — "Artifacts should be scanned in internal repositories for newly discovered or identified defects and the ability to stop their use in builds based on criticality."
- (§3.2.1 bullet 6) [R-0027] *recommendation* — "CI/CD processes should be audited regularly, and automation should be introduced wherever possible to improve the performance of activities and operations."
- (§3.2.1 bullet 7) [R-0028] *recommendation* — "There should be isolated CI/CD environment and elevated administrator credentials for the deployment of applications in clouds."
- (§3.2.1 bullet 8) [R-0029] *recommendation* — "There should be enhanced real-time monitoring and alerting mechanisms to detect suspicious activities in CI/CD servers, especially activities that might indicate the exfiltration of sensitive data or the tampering of builds."
### §3.2.2

- (§3.2.2) [R-0030] *recommendation* — "The proposed changes should adhere to the SDLC processes defined by the organization."
- (§3.2.2) [R-0031] *recommendation* — "In all cases, write access to the SCM should be considered a high risk and tightly controlled."
- (§3.2.2) [R-0032] *recommendation* — "A mature SDLC process allows developers to propose patches to the SCM, but another developer should perform a code review before the patch is merged."
- (§3.2.2) [R-0033] *recommendation* — "Code analysis tools should be implemented to catch common mistakes, but care should be taken to not inundate the developers with too many false positives to prevent alert fatigue."

## 4. CI/CD Pipelines — Background, Security Goals, and Entities to be Trusted

### §4

- (§4) [R-0034] *practice* — "A common approach to SSC security in all of these workflows is to generate as much provenance data as possible."
- (§4) [R-0035] *recommendation* — "The generation of these data should be accompanied by corresponding mechanisms to validate, authenticate, and leverage them in policy decisions."
- (§4) [R-0036] *practice* — "From the above description of CI/CD pipelines and associated activities, one can identify the set of security assurance measures that need to be added: • Internal SSC security practices that are applied during the development and deployment of first-party software • Security practices that are applied with respect to the procurement, integration, and deployment of third-party software (i.e., open-source and commercial software modules)"
### §4.1

- (§4.1 goal 1) [R-0037] *practice* — "1. Actively defend the CI/CD pipeline and build processes."
- (§4.1 goal 2) [R-0038] *practice* — "2. Ensure the integrity of upstream sources and artifacts (e.g., repositories)."
### §4.2

- (§4.2 bullet 1) [R-0039] *recommendation* — "The entities involved in performing various SSC activities (e.g., building, packaging, deployment) should be authenticated through the verification of credentials. Based on this authentication, appropriate permissions or access rights are assigned to those entities based on enterprise business policies through a process called authorization."
- (§4.2 bullet 2) [R-0040] *recommendation* — "The integrity of artifacts and the repositories where they are stored should be ensured through the verification of the digital signatures associated with them. This integrity assurance results in trust."
- (§4.2 bullet 3) [R-0041] *recommendation* — "The establishment of trust above should be a recurring process throughout the CI/CD system since artifacts travel through various repositories to ultimately become the final product."
- (§4.2 bullet 4) [R-0042] *recommendation* — "The inputs and outputs of each build step should be verified to ensure that the correct steps have been executed by the expected component or entity."
- (§4.2 Table 1 note a) [R-0043] *requirement* — "Other artifacts used for the security assurance of CI/CD processes (e.g., SBOMs, vulnerability reports, and model registries that use AI models) must also be trusted."
- (§4.2 Table 1 note b) [R-0044] *practice* — "The addition of attestations like VSA does not necessarily imply that the artifact manager is trusted."
- (§4.2 footnote 3) [R-0045] *requirement* — "The trust chain includes sub-elements, components, workers, attestors, and other mechanisms that must establish and reestablish trust through interactions (i.e., handoffs of inputs and outputs)."

**Table 1 (§4.2). Top-level entities in the trust chain of typical CI/CD pipelines**

| Artifact | Repository |
|---|---|
| First-party code — In house | SCM |
| Third-party code — Open source or commercial | Artifact managers for language, containers, etc. |
| Builds | Build repository |
| Packages | Package repository |

## 5. Integrating SSC Security Into CI/CD Pipelines

### §5

- (§5 prerequisite 1) [R-0046] *practice* — "Harden the CI/CD execution environment (e.g., VM or pod) to reduce its attack surface."
- (§5 prerequisite 2) [R-0047] *practice* — "Define roles for the actors who operate the various CI/CD pipelines (e.g., application updaters, package managers, deployment specialists)." → SSDF PO.2
- (§5 prerequisite 3) [R-0048] *practice* — "Identify the granular authorizations to perform various tasks, such as generating and committing code to SCMs, generating builds and packages, and checking various artifacts (e.g., builds and packages) into and out of the repositories." → SSDF PO.2
- (§5 prerequisite 4) [R-0049] *practice* — "Automate the entire CI/CD pipeline through the deployment of appropriate tools." → SSDF PO.3
- (§5 prerequisite 4) [R-0050] *practice* — "In general, the driver tools or build control plane execute at a higher level of trust than the individual functional steps, such as build." → SSDF PO.3
- (§5 prerequisite 5) [R-0051] *practice* — "Define CI/CD pipeline activities and associated security requirements for the development and deployment of application code; infrastructure as code, which contains details about the deployment platform; and policy as code and configuration code, which specify runtime settings (e.g., Yet Another Markup Language (YAML) files)." → SSDF PW.9
### §5.1

- (§5.1) [R-0052] *practice* — "The overall security goals for the framework used for securely running CI pipelines include: • The capability to support both cloud-native and other types of applications. • Standard compliant evidence structures, such as metadata and digital signatures • Support for multiple hardware and software platforms • Support for infrastructures for generating the evidence (e.g., SBOM generators, Digital signature generators)"
### §5.1.1

- (§5.1.1 task 1) [R-0053] *requirement* — "Specify policies regarding the build, including (a) the use of a secure isolated platform for performing the build and hardening the build servers, (b) the tools that will be used to perform the build, and (c) the authentication/authorization required for the developers performing the build process." → SSDF PO.1
- (§5.1.1 task 2) [R-0054] *requirement* — "Enforce those build policies using techniques such as an agent and policy enforcement engine." → SSDF PO.1
- (§5.1.1 task 3) [R-0055] *requirement* — "Ensure the concurrent generation of evidence for build attestation to demonstrate compliance with secure build processes during the time of software delivery."
- (§5.1.1) [R-0056] *recommendation* — "The first type of evidence is from the build system itself, which should be able to confirm that the tools or processes used are in an isolated environment."
- (§5.1.1) [R-0057] *recommendation* — "The second type of evidence that should be gathered consists of the hash of the final build artifact, files, libraries, and other materials used in the artifacts and all events."
- (§5.1.1) [R-0058] *practice* — "This is then signed by a trusted component of the build framework that is not under the control of the developers using a digital certificate to create the attestation, which provides verifiable proof of the quality of the software to consumers and enables them to verify the quality of that artifact independently from the producer of the software, thus providing consumer assurance."
- (§5.1.1) [R-0059] *recommendation* — "In the context of “concurrent generation of evidence,” the evidence generated should be enabled by a process with a higher level of trust or isolation than the build itself to protect against tampering."
- (§5.1.1) [R-0060] *requirement* — "The generation of such evidence requires verification within the build as it occurs."
- (§5.1.1 component 1) [R-0061] *requirement* — "1. Environment attestation: Environment attestation involves an inventory of the system when the CI process happens and generally refers to the platform on which the build process is run. The components of the platform (e.g., compiler, interpreter) must be hardened, isolated, and secure." → SSDF PO.5, PW.6
- (§5.1.1 component 2) [R-0062] *recommendation* — "2. Process attestation: Process attestation pertains to the computer programs that transformed the original source code or materials into an artifact (e.g., compilers, packaging tools) and/or the programs that performed testing on that software (i.e., code testing tool). It is sometimes difficult for tooling that simply observes CI processes to distinguish between data that should populate the process attestation and data that should populate the materials attestation. A file read by tooling that performs the source transformation may be used to influence the choices that the transformation tool makes, or it might be included in the output of the transformation itself. As a result, the population of the process attestation should be considered “best effort.”"
- (§5.1.1 component 3) [R-0063] *practice* — "3. Materials attestation: Materials attestation pertains to any raw data and can include configuration, source code, and other data (e.g., dependencies)."
- (§5.1.1 component 4) [R-0064] *practice* — "4. Artifacts attestation: An artifact is the result or outcome of a CI process. For example, if the CI process step involves running a compiler (e.g., GNU Compiler Collection (GCC)) on a source code written in C, the artifact that will result is an executable binary of that source code. If the step involves running a SAST tool on the same source code, the artifact will be the “Scan Result.” The step that generated it can be a final or intermediate step. An attestation pertaining to this newly generated product falls under the category of artifacts attestation."
- (§5.1.1 attestation requirement 1) [R-0065] *requirement* — "The attestations must be cryptographically signed using a secure key."
- (§5.1.1 attestation requirement 2) [R-0066] *requirement* — "The storage location must be tamper-proof and protected using robust access control."
- (§5.1.1) [R-0067] *practice* — "The attestations can then be used to evaluate policy compliance. A policy is a signed document that encodes the requirements for an artifact to be validated."
- (§5.1.1) [R-0068] *permission* — "The policy may include checks as to whether each of the functionaries involved in the CI process has used the right keys to generate the attestations, the required attestations are found, and the methodology to evaluate the attestation against its associated metadata has also been specified."
- (§5.1.1) [R-0069] *practice* — "The policy enables the verifiers to trace the compliance status of the artifact at any point during its life cycle."
- (§5.1.1) [R-0070] *practice* — "The above capabilities collectively provide the following assurances: • The software was built by authorized systems using authorized tools (e.g., infrastructure for each step) in the correct sequence of steps. • There is no evidence of potential tampering or malicious activity."
### §5.1.2

- (§5.1.2 check 1) [R-0071] *requirement* — "1. The type of authentication required for developers authorized to perform the PULL-PUSH operations. The request made by the developer must be consistent with their role (e.g., application updater, package manager). Developers with “merge approval” permissions cannot approve their own merges." → SSDF PS.1
- (§5.1.2 check 2) [R-0072] *requirement* — "2. The integrity of the code in the repository can be trusted such that it can be used for further updates." → SSDF PS.1
- (§5.1.2) [R-0073] `PULL-PUSH_REQ-1` *recommendation* — "PULL-PUSH_REQ-1: The project maintainer should run automated checks on all artifacts covered in the change being pushed, such as unit tests, linters, integrity tests, security checks, and more." → SSDF PW.5
- (§5.1.2) [R-0074] `PULL-PUSH-REQ-2` *recommendation* — "PULL-PUSH-REQ-2: CI pipelines should only be run using tools when confidence is established in the trustworthiness of the source-code origin of those tools." → SSDF PW.5
- (§5.1.2) [R-0075] `PULL-PUSH-REQ-3` *recommendation* — "PULL-PUSH-REQ-3: The repository or source-code management system (e.g., GitHub, GitLab) should either a) run CI workflows in sandboxed environments without access to the network, any privileged access, or the ability to read secrets or b) have built-in protection that incorporates a delay in CI workflow runs until they are approved by a maintainer with write access. This built-in protection should go into effect when an outside contributor submits a pull request to a public repository. The setting for this protection should be at the strictest level, such as “Require approval for all outside collaborators” [10]." → SSDF PW.5
- (§5.1.2) [R-0076] `PULL-PUSH_REQ-4` *requirement* — "PULL-PUSH_REQ-4: If there are no built-in protections available in the source-code management system, then external security tools with the following features are required: o Functionality to evaluate and enhance the security posture of the SCM systems with or without a policy (e.g., Open Policy Agent (OPA)) to assess the security settings of the SCM account and generate a status report with actionable recommendations. o Functionality to enhance the security of the source-code management system by detecting and remediating misconfigurations, security vulnerabilities, and compliance issues." → SSDF PW.5
### §5.1.3

- (§5.1.3) [R-0077] *recommendation* — "The framework should protect the signing operation by requiring the policy defined in Sec. 5.1.1 to be satisfied prior to performing the signing operation." → SSDF PS.2
- (§5.1.3 goal 1) [R-0078] *recommendation* — "The framework should provide protection against all known attacks on the tasks performed by the software update systems, such as metadata (hash) generation, the signing process, the management of signing keys, the integrity of the authority performing the signing, key validation, and signature verification." → SSDF PS.2
- (§5.1.3 goal 2) [R-0079] *recommendation* — "The framework should provide a means to minimize the impacts of key compromise by supporting roles with multiple keys and threshold or quorum trust (with the exception of minimally trusted roles designed to use a single key)." → SSDF PS.2
- (§5.1.3 goal 2) [R-0080] *recommendation* — "The compromise of roles that use highly-vulnerable keys should have minimal impact." → SSDF PS.2
- (§5.1.3 goal 2) [R-0081] *recommendation* — "Therefore, online keys (i.e., keys used in an automated fashion) should not be used for any role that clients ultimately trust for files they may install [11]." → SSDF PS.2
- (§5.1.3 goal 2) [R-0082] *recommendation* — "When keys are online, exceptional care should be taken in caring for them, such as storing them in a Hardware Security Module (HSM) and only allowing their use if the artifacts being signed pass the policy defined in Sec. 5.1.1." → SSDF PS.2
- (§5.1.3 goal 3) [R-0083] *requirement* — "The framework must be flexible enough to meet the needs of a wide variety of software update systems." → SSDF PS.2
- (§5.1.3 goal 4) [R-0084] *requirement* — "The framework must be easy to integrate with software update systems." → SSDF PS.2
### §5.1.4

- (§5.1.4) [R-0085] *recommendation* — "Appropriate forms of testing should be performed before code commits, and the following requirements must be met:" → SSDF PO.4, PW.8
- (§5.1.4 bullet 1) [R-0086] *recommendation* — "SAST and DAST tools (covering all languages used in development) should be run in CI/CD pipelines with code coverage reports being provided to developers and security personnel." → SSDF PO.4, PW.8
- (§5.1.4 bullet 2) [R-0087] *requirement* — "If open-source modules and libraries are used, dependencies must be enumerated, understood, and evaluated for policy (potentially using appropriate SCA tools)." → SSDF PO.4, PW.8
- (§5.1.4 bullet 2) [R-0088] *requirement* — "The security conditions that they should meet for their inclusion must also be tested." → SSDF PO.4, PW.8
- (§5.1.4 bullet 2) [R-0089] *recommendation* — "Dependency file detectors should detect all dependencies, including transitive dependencies with preferably no limit to the depth of nested or transitive dependencies that are to be analyzed [19]." → SSDF PO.4
- (§5.1.4) [R-0090] *requirement* — "One SSC security measure required during code commits is the prevention of secrets getting into the committed code. This is enabled by a scanning operation for secrets and results in a feature called push protection [12], [20]. This feature should satisfy the following requirements:"
- (§5.1.4 COMMIT-REQ-1) [R-0091] `COMMIT-REQ-1` *practice* — "COMMIT-REQ-1: (e.g., personal access token) Evaluate committed code for adherence to organizational policy, including the absence of secrets such as keys and Application Programming Interface (API) tokens."
- (§5.1.4 COMMIT-REQ-1) [R-0092] `COMMIT-REQ-1` *recommendation* — "The detected secrets should be displayed prominently through media such as security dashboards, and appropriate alerts should be generated upon detection of policy violations with documented methods to remediate violations."
- (§5.1.4 COMMIT-REQ-2) [R-0093] `COMMIT-REQ-2` *recommendation* — "COMMIT-REQ-2: Push protection features should be enabled for all repositories assigned to an administrator [13]."
- (§5.1.4 COMMIT-REQ-2) [R-0094] `COMMIT-REQ-2` *recommendation* — "Such protection should include the verification of developer identity/authorization, the enforcement of developer signing of code commits, and file name verification [21]."
### §5.2

- (§5.2) [R-0095] *recommendation* — "The following are some due diligence measures that should be used during CD. These measures can be implemented by defining verification policies for allowing or disallowing an artifact for deployment." → SSDF PO.1
- (§5.2 DEPLOY-REQ-1) [R-0096] `DEPLOY-REQ-1` *recommendation* — "DEPLOY-REQ-1: For code that is already in the repository and ready to be deployed, a security scanning sub-feature should be invoked to detect the presence of secrets in the code, such as keys and access tokens." → SSDF PO.1
- (§5.2 DEPLOY-REQ-1) [R-0097] `DEPLOY-REQ-1` *recommendation* — "In many instances, the repository should be scanned for the presence of secrets, even before being populated with code, since their presence in a repository can mean that the credentials are already leaked, depending on the repository’s visibility." → SSDF PO.1
- (§5.2) [R-0098] `DEPLOY-REQ-2` *recommendation* — "DEPLOY-REQ-2: Before merging pull requests, it should be possible to view the details of any vulnerable versions through a form of dependency review [15], [19]." → SSDF PO.1
- (§5.2) [R-0099] `DEPLOY-REQ-3` *recommendation* — "DEPLOY-REQ-3: If a secure build environment and associated process have been established, it should be possible to specify that the artifact (i.e., container image) being deployed must have been generated by that build process in order to be cleared for deployment." → SSDF PO.1
- (§5.2 DEPLOY_REQ-4) [R-0100] `DEPLOY_REQ-4` *recommendation* — "DEPLOY_REQ-4: There should be evidence that the container image was scanned for vulnerabilities and attested for vulnerability findings." → SSDF PO.1
- (§5.2 DEPLOY_REQ-4) [R-0101] `DEPLOY_REQ-4` *recommendation* — "Specifically, it should be possible to allow or block image deployment based on organization-defined policies." → SSDF PO.1
- (§5.2) [R-0102] `DEPLOY-REQ-5` *recommendation* — "DEPLOY-REQ-5: The release build scripts should be periodically checked for malicious code." → SSDF PO.1
- (§5.2 DEPLOY-REQ-5 task 1) [R-0103] `DEPLOY-REQ-5` *recommendation* — "A container image should be scanned for vulnerabilities as soon as it is built, even before it is pushed to a registry. The early scanning feature can also be built into local workflows." → SSDF PO.1
- (§5.2 DEPLOY-REQ-5 task 2) [R-0104] `DEPLOY-REQ-5` *recommendation* — "The tools used to interact with repositories that contain container images and language packages should be capable of integration with CD tools, thus making all activities an integral part of automated CD pipelines." → SSDF PO.1
### §5.2.1

- (§5.2.1) [R-0105] *recommendation* — "The following SSC security tasks should be applied with respect to creating configuration data prior to deployment, capturing all data pertaining to a particular release, modifying software during runtime, and performing monitoring operations:" → SSDF PS.3
- (§5.2.1) [R-0106] `GitOps-REQ-1` *recommendation* — "GitOps-REQ-1: The process should rely on automation rather than manual operations. For example, manually configuring hundreds of YAML files to roll back a deployment on a cluster in a Git repository should be avoided."
- (§5.2.1) [R-0107] `GitOps-REQ-2` *recommendation* — "GitOps-REQ-2: Package managers that facilitate GitOps should preserve all data on the packages that were released, including the version numbers of all modules, all associated configuration files, and other metadata as appropriate for the software operational environment." → SSDF PS.3
- (§5.2.1) [R-0108] `GitOps-REQ-3` *recommendation* — "GitOps-REQ-3: Changes should not be manually applied at runtime (e.g., kubectl). Instead, changes should be made to the relevant code, and a new release that incorporates those changes should be triggered. This ensures that Git commits remain the single source of truth for what runs in the cluster."
- (§5.2.1) [R-0109] `GitOps-REQ-4` *recommendation* — "GitOps-REQ-4: Since the Git repository contains the application definitions and configuration as code, it should be pulled automatically and compared with the specified state of these configurations (i.e., monitoring and remediation for drift). For any configurations that deviate from their specified state, the following actions may be performed: o Administrators can choose to automatically resync configurations to the defined state. o Notifications should be sent regarding the differences, and manual remediation should be performed."
### §5.3

- (§5.3 type 1a) [R-0110] *practice* — "a. Verifying that the software is built correctly by ensuring tamper-proof build pipelines, such as by providing verified visibility into the dependencies and steps used in the build [18], since compromised dependencies or build tools are the greatest sources for poisoned workflows."
- (§5.3 type 1b) [R-0111] *practice* — "b. Including features for the specification of checklists for each step of the delivery pipeline to provide guidance for implementation and to check and enforce controls for complying with checklists."
- (§5.3 type 2) [R-0112] *practice* — "2. Solutions that ensure integrity and provenance through digital signatures and attestations"
- (§5.3 type 3) [R-0113] *recommendation* — "3. Strategy to ensure that running code is up to date, such as instituting a “build horizon” (i.e., code that is older than a certain time period should not be launched), to keep production as close as possible to the committed code in the repositories."
- (§5.3 type 4) [R-0114] *practice* — "4. Securing CI/CD clients to prevent malicious code from stealing confidential information (e.g., proprietary source code, signing keys, cloud credentials), reading environment variables that may contain secrets, or exfiltrating data to an adversary-controlled remote endpoint."

## Appendix A. Mapping of Recommended Security Tasks in CI/CD Pipelines to Recommended High-Level Practices in SSDF (statements whose wording differs from Section 5)

- (App. A Table 2 (PO.3 row)) [R-0115] *requirement* — "The entire CI/CD pipeline must be automated through the deployment of appropriate tools as a prerequisite for activating CI/CD pipelines." → SSDF PO.3
- (App. A Table 2 (PO.5 row)) [R-0116] *requirement* — "Environment attestation: Environment attestation involves an inventory of the system when the CI process happens. It generally refers to the platform on which the build process is run. This platform must be hardened, isolated, and secure." → SSDF PO.5
- (App. A Table 2 (PS.2 row, item 2)) [R-0117] *requirement* — "Therefore, online keys (i.e., keys used in an automated fashion) must not be used for any role that clients ultimately trust for files they may install [11]." → SSDF PS.2
- (App. A Table 2 (PW.5 row)) [R-0118] *recommendation* — "PULL-PUSH_REQ-1: The project maintainer should run automated checks on all artifacts covered in the pull request, such as unit tests, linters, integrity tests, security checks, and more." → SSDF PW.5
- (App. A Table 2 (PW.5 row)) [R-0119] *recommendation* — "PULL-PUSH-REQ-2: CI pipelines should only use external tools (e.g., Jenkins) when confidence is established in the trustworthiness of the source-code origin." → SSDF PW.5
- (App. A Table 2 (PW.5 row)) [R-0120] *recommendation* — "PULL-PUSH-REQ-3: The repository or source-code management system (e.g., GitHub, GitLab) should have built-in protection that incorporates a delay in CI workflow runs until they are approved by a maintainer with write access. This built-in protection should go into effect when an outside contributor submits a pull request to a public repository. The setting for this protection should be at the strictest level, such as “Require approval for all outside collaborators” [10]." → SSDF PW.5
- (App. A Table 2 (PW.8 row)) [R-0121] *requirement* — "Both SAST and DAST tools used in CI/CD pipelines must provide coverage for the different language systems used in cloud-native applications." → SSDF PW.8
- (App. A Table 2 (PW.8 row)) [R-0122] *requirement* — "If open-source modules and libraries are used, dependencies must be detected using appropriate SCA tools, and the security conditions they should meet for their inclusion must also be tested." → SSDF PW.8
- (App. A Table 2 (PO.1 row)) [R-0123] *practice* — "DEPLOY_REQ-4: Check for evidence that the container image was scanned for vulnerabilities and attested for vulnerability findings." → SSDF PO.1
- (App. A Table 2 (PO.1 row)) [R-0124] *practice* — "DEPLOY-REQ-5: Periodically check the release build scripts for malicious code." → SSDF PO.1

**Table 2 — mapping of 204D sections to SSDF v1.1 practices (practice names verbatim):**

| 204D section (tasks) | SSDF practice |
|---|---|
| 5.1.1 Secure Build — Policies…; 5.2 Securing Workflows in CD Pipelines (DEPLOY-REQ-1..5) | Define Security Requirements for Software Development (PO.1) |
| 5 Integrating SSC Security in CI/CD Pipelines (roles, authorizations) | Implement Roles and Responsibilities (PO.2) |
| 5 Integrating SSC Security in CI/CD Pipelines (automation, driver tools) | Implement Supporting Toolchains (PO.3) |
| 5.1.4 Secure Code Commits | Define and Use Criteria for Software Security Checks (PO.4) |
| 5.1.1 Secure Build (environment attestation) | Implement and Maintain Secure Environments for Software Development (PO.5) |
| 5.1.2 Secure PULL-PUSH Operations on Repositories (two checks) | Protect All Forms of Code From Unauthorized Access and Tampering (PS.1) |
| 5.1.3 Integrity of Evidence Generation During Software Updates | Provide a Mechanism for Verifying Software Release Integrity (PS.2) |
| 5.2.1 Secure CD Pipeline — Case Study (GitOps) (GitOps-REQ-2) | Archive and Protect Each Software Release (PS.3) |
| 5.1.2 Secure PULL-PUSH Operations (PULL-PUSH_REQ-1..4) | Create Source Code by Adhering to Secure Coding Practices (PW.5) |
| 5.1.1 Secure Build (environment attestation) | Configure the Compilation, Interpreter, and Build Processes to Improve Executable Security (PW.6) |
| 5.1.4 Secure Code Commits | Test Executable Code to Identify Vulnerabilities and Verify Compliance With Security Requirements (PW.8) |
| 5 Integrating SSC Security into CI/CD Pipelines (activities and security requirements per code type) | Configure Software to Have Secure Settings by Default (PW.9) |

## Appendix B. Justification for the Omission of Certain Measures Related to SSDF Practices in This Document

- (App. B Table 3) [R-0125] *practice* — "These practices pertain to secure software design, review of the design, and software reuse. CI/CD pipelines focus on setting up the environment for secure development and deployment in DevSecOps SDLC rather than software design."
- (App. B Table 3) [R-0126] *practice* — "Vulnerability management strategies are at the organization policy level and are not specific to CI/CD pipelines."

## Statements the source does not map to SSDF

Table 2 maps no SSDF practice to: BUILD-3 (concurrent evidence generation), the attestation components ATT-2..ATT-4 and the signing/storage requirements ATT-REQ-1/2, the push-protection / secret-scanning block (COMMIT-REQ-1, COMMIT-REQ-2), GitOps-REQ-1/3/4, the §3 baseline measures, the §4.2 trust steps, and the §5.3 implementation strategy. Appendix B excludes SSDF PW.1–PW.4, PW.7 and RV.1–RV.3 outright.

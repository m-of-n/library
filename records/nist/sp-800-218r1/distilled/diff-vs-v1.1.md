---
schema: "library-distilled/v1"
id: sp-800-218r1-diff-vs-v1-1
record: sp-800-218r1
kind: diff
type: diff-note
title: "SSDF 1.2 IPD vs SSDF 1.1 — what changed"
extracted: "2026-10-02"
updated: "2026-10-02"
reviewed_by: ""
---

# SSDF 1.2 (SP 800-218r1 ipd, DRAFT) vs SSDF 1.1 (SP 800-218, final)

**Method.** SSDF 1.1 is read from NIST's official machine-readable table `nist.sp.800-218.ssdf-table.xlsx` (sha256 `f5729c4c…bd55`); SSDF 1.2 IPD from the PDF Table 1 (sha256 `0f40af24…a8d000`), extracted by word coordinates. Every practice, task, example and reference line was compared after whitespace/quote normalization; the draft's own Appendix B change log was then checked against the computed diff. Retired identifiers (PW.3, PW.3.1, PW.3.2, PW.4.3, PW.4.5, PW.5.2) appear as "Moved to …" rows in **both** PDFs (the 1.1 xlsx omits them) and are unchanged.

**Independent re-derivation (verify pass, 2026-10-02).** The diff was recomputed from scratch from `sp-800-218` requirements.yaml (itself re-checked cell-for-cell against the xlsx and against the PDF by word coordinates) and `sp-800-218r1` requirements.yaml (re-checked against the IPD PDF by word coordinates). It confirms: 2 new practices / 7 new tasks; 4 practice explanations and 8 task texts reworded; 10 examples added to existing tasks and 25 reworded (none removed); EO14028 removed from all 42 tasks; SP80053 changed on 35 tasks and added on 7; SP800161 changed on 25, removed on 10, added on 1; all 26 other schemes byte-identical on every pre-existing task; the SP 800-53/800-161 per-task table below matches the data on all 42 rows. Corrections made: (a) RV.1.1 Ex 1 was listed as reworded — it is identical; the 1.1 xlsx renders the dropped footnote-9 marker as a stray space ("databases , security"), now removed from `sp-800-218`; (b) the SP80053 count (35 rewritten + 7 added, not "all 42 rewritten") and the SP800161 count (25 rewritten + 1 added + 10 removed, not "36 rewritten") are fixed in §5.

## Status

- SP 800-218r1 is an **Initial Public Draft** (published 2025-12-17, comment period closed 2026-01-30). Checked 2026-10-02: https://csrc.nist.gov/pubs/sp/800/218/r1/ipd is live; `/r1/final` and `/r1/2pd` return 404; the SSDF project page (https://csrc.nist.gov/projects/ssdf, updated 2026-04-13) still presents SSDF 1.1 as the current version. On finalization this record's document will supersede `sp-800-218`; until then it is a draft and `sp-800-218` stays authoritative.
- Driver: Executive Order 14306 (June 2025), quoted in the Note to Reviewers as calling for updated “practices, procedures, controls, and implementation examples regarding the secure and reliable development and delivery of software as well as the security of the software itself.”

## Counts

| | SSDF 1.1 | SSDF 1.2 IPD | Δ |
|---|---|---|---|
| groups | 4 | 4 | 0 |
| active practices | 19 | 21 | +2 (PO.6, PS.4) |
| retired practice ids | 1 (PW.3) | 1 (PW.3) | 0 |
| active tasks | 42 | 49 | +7 (PO.6.1–6.3, PS.4.1–4.4) |
| retired task ids | 5 | 5 | 0 |
| notional implementation examples | 198 | 225 | +27 (17 in new tasks, 10 added to existing tasks) |
| reference lines in Table 1 | 528 | 497 | −42 EO14028 lines; +7 SP80053 lines on tasks that had none; +1/−10 SP800161 lines; +13 lines on the 7 new tasks |
| reference schemes used in Table 1 | 29 | 29 | −EO14028, +NISTCSF20 |
| appendices | A (EO 14028 §4e mapping), B (acronyms), C (change log) | A (acronyms), B (change log) | EO 14028 mapping appendix removed |

## 1. New practices and tasks (verbatim)

### PO.6 — Define and Implement a Continuous Process Improvement Plan

> Identify and execute improvements to cybersecurity processes and procedures throughout the SDLC across all SSDF practices.

- **PO.6.1:** Update and improve software development environments in response to new threats and as new tools are included in the development process.
  - Example 1: Add new scanning tools or update the configurations of existing tools to check for malicious content in artifacts received from suppliers. Actions could be executed as part of a response to an incident or based on threat reports.
  - Example 2: Improve logging and audit capabilities in development environments by working with internal security teams to identify the best format, events to capture, and level of granularity that enable quick reconstruction of security-related actions.
  - Example 3: Incorporate and adapt zero trust capabilities as they become available in underlying IT and development infrastructures.
  - References: [NISTCSF20]: ID.IM · SP80053: CM-09, RA-03, SA-15
- **PO.6.2:** Identify new processes, tools, and techniques that can help avoid software errors (see PW.7, RV.3.3).
  - Example 1: Use new languages or features in existing languages that eliminate classes of vulnerabilities.
  - Example 2: Evaluate and adopt tools that expand testing coverage in response to known vulnerabilities.
  - Example 3: Improve logging capabilities in software by working with customers and security logging vendors or tools to identify the best format, events to capture, and level of granularity that enable quick reconstruction of security-related actions.
  - References: NISTCSF20: ID.IM · SP80053: SA-15
- **PO.6.3:** Improve vulnerability response processes, and periodically review prior decisions (see RV.2.2).
  - Example 1: Periodically review decisions, particularly if a decision to not provide a software update is made in favor of some other mitigation, and the implementation of measures to identify customer impact over time.
  - References: NISTCSF20: ID.IM · SP80053: RA-05, SA-15

### PS.4 — Ensure Software Updates Are Robust and Reliable

> Implement robust and reliable software update strategies, preferably allowing customers to control any updates to the software package and application configurations. Help software acquirers maintain operations and minimize disruptions by ensuring that software updates are tested and responsibly delivered.

- **PS.4.1:** Thoroughly test all releases following all guidance in PW.
  - Example 1: Test using configurations and environments that replicate actual or expected customer installations.
  - Example 2: Consider using an “early access” program to allow customers to test updates before general release.
  - References: SP80053: CM-03, CM-04, SA-11 · SP800161: SA-11
- **PS.4.2:** Use tiered update and release strategies, such as canaries, staged roll-out, and test deployments.
  - Example 1: Enable customers to configure and identify those systems that they consider critical and those that are considered safe to receive early updates for testing purposes.
  - Example 2: Support multiple strategies for rolling out updates to customers, including staged or segmented rollouts with built-in wait times for customer feedback.
  - Example 3: Consider the use of mechanisms that enable tailored updates or that support or provide information for troubleshooting problems while still maintaining user privacy.
  - References: SP80053: CM-02, CM-06, CM-09, SA-10 · SP800161: CM-02, CM-06
- **PS.4.3:** Include robust rollback mechanisms for updates.
  - Example 1: Failed software updates automatically revert software to the last known good configuration, leaving systems in a runnable state.
  - Example 2: Enable end-user organizations to roll back updates on systems as needed.
  - Example 3: Implement protection mechanisms that prevent unauthorized roll-back to vulnerable software versions.
  - References: SP80053: CM-02, CM-09, SA-08, SA-10 · SP800161: CM-02
- **PS.4.4:** Maintain robust and reliable update engines and associated infrastructure for the delivery of updates.
  - Example 1: Make the update engine fault-tolerant so that it can recover and retry downloading an update in the event of infrastructure overload.
  - Example 2: Have the delivery infrastructure for updates degrade gracefully, or refuse new download attempts until current requests have been completed.
  - References: SP80053: CA-06, CA-07, CM-09, SA-10

Note: PO.6 is the only place the new `NISTCSF20` (CSF 2.0) scheme is used (`ID.IM`, Improvement); every pre-existing task still maps to CSF **1.1** subcategories. PS.4 tasks map only to SP 800-53 / SP 800-161 — no BSIMM, SAMM, IEC 62443 or other industry references yet (the draft asks reviewers for them).

## 2. Practice descriptions reworded (editorial)

| Practice | SSDF 1.1 | SSDF 1.2 IPD |
|---|---|---|
| PO.1 | Ensure that security requirements for software development are known at all times so that they can be taken into account throughout the SDLC and duplication of effort can be minimized because the requirements information can be collected once and shared. This includes requirements from internal sources (e.g., the organization’s policies, business objectives, and risk management strategy) and external sources (e.g., applicable laws and regulations). | Ensure that security requirements for software development are known at all times so that they can be taken into account throughout the SDLC and the duplication of effort can be minimized because the requirements information can be collected once and shared. This includes requirements from internal sources (e.g., the organization’s policies, business objectives, and risk management strategy) and external sources (e.g., applicable laws and regulations). |
| PO.3 | Use automation to reduce human effort and improve the accuracy, reproducibility, usability, and comprehensiveness of security practices throughout the SDLC, as well as provide a way to document and demonstrate the use of these practices. Toolchains and tools may be used at different levels of the organization, such as organization-wide or project-specific, and may address a particular part of the SDLC, like a build pipeline. | Use automation to reduce human effort and improve the accuracy, reproducibility, usability, and comprehensiveness of security practices throughout the SDLC, as well as provide a way to document and demonstrate the use of these practices. Toolchains and tools may be used at different levels of the organization (e.g., organization-wide, project-specific) and may address a particular part of the SDLC, like a build pipeline. |
| PS.1 | Help prevent unauthorized changes to code, both inadvertent and intentional, which could circumvent or negate the intended security characteristics of the software. For code that is not intended to be publicly accessible, this helps prevent theft of the software and may make it more difficult or time-consuming for attackers to find vulnerabilities in the software. | Help prevent unauthorized changes to code, both inadvertent and intentional, which could circumvent or negate the intended security characteristics of the software. For code that is not intended to be publicly accessible, this helps prevent the theft of the software and may make it more difficult or time-consuming for attackers to find vulnerabilities in the software. |
| PW.1 | Identify and evaluate the security requirements for the software; determine what security risks the software is likely to face during operation and how the software’s design and architecture should mitigate those risks; and justify any cases where risk-based analysis indicates that security requirements should be relaxed or waived. Addressing security requirements and risks during software design (secure by design) is key for improving software security and also helps improve development efficiency. | Identify and evaluate the security requirements for the software; determine what security risks the software is likely to face during operation and how the software’s design and architecture should mitigate those risks; and justify any cases for which risk-based analysis indicates that security requirements should be relaxed or waived. Addressing security requirements and risks during software design (i.e., secure by design) is key to improving software security and also helps improve development efficiency. |

Group name: Table 1's group row now reads “Protect Software (PS)”; §2 of the same draft (and all of SSDF 1.1) reads “Protect the Software (PS)”.

## 3. Task text changes

The change log lists only RV.1.2 and RV.3.3; the computed diff finds eight. RV.1.2 is substantive (configurations are now in scope); RV.3.3 changes “fix” → “remediate”; the rest are editorial.

| Task | SSDF 1.1 | SSDF 1.2 IPD |
|---|---|---|
| PO.4.1 | Define criteria for software security checks and track throughout the SDLC. | Define criteria for software security checks and track them throughout the SDLC. |
| PO.4.2 | Implement processes, mechanisms, etc. to gather and safeguard the necessary information in support of the criteria. | Implement processes and mechanisms to gather and safeguard necessary information in support of the criteria. |
| PO.5.2 | Secure and harden development endpoints (i.e., endpoints for software designers, developers, testers, builders, etc.) to perform development-related tasks using a risk-based approach. | Secure and harden development endpoints (e.g., for software designers, developers, testers, builders) to perform development-related tasks using a risk-based approach. |
| PS.1.1 | Store all forms of code – including source code, executable code, and configuration-as-code – based on the principle of least privilege so that only authorized personnel, tools, services, etc. have access. | Store all forms of code – including source code, executable code, and configuration as code – based on the principle of least privilege so that only authorized personnel, tools, and services have access. |
| PW.1.1 | Use forms of risk modeling – such as threat modeling, attack modeling, or attack surface mapping – to help assess the security risk for the software. | Use forms of risk modeling (e.g., threat modeling, attack modeling, attack surface mapping) to help assess the security risk for the software. |
| RV.1.2 | Review, analyze, and/or test the software’s code to identify or confirm the presence of previously undetected vulnerabilities. | Review, analyze, and/or test the software’s code and its default and other common configurations to identify or confirm the presence of previously undetected vulnerabilities. |
| RV.2.1 | Analyze each vulnerability to gather sufficient information about risk to plan its remediation or other risk response. | Analyze each vulnerability to gather sufficient information about risk and plan its remediation or other risk response. |
| RV.3.3 | Review the software for similar vulnerabilities to eradicate a class of vulnerabilities, and proactively fix them rather than waiting for external reports. | Review software for similar vulnerabilities to eradicate a class of vulnerabilities and proactively remediate them rather than waiting for external reports. |

## 4. Notional implementation example changes

**Added (substantive):**

- **PW.1.1 Example 5** (new): Consider processes for creating and sharing under controlled disclosure the risk and threat models used during software development to inform customer risk management decisions.
- **PW.1.3 Example 4** (new): Use common and secure logging formats and features.
- **PW.1.3 Example 5** (new): Ensure that the software adheres to the principle of least privilege. Identify the minimal functionality needed when operating with elevated privileges (e.g., kernel space or admin privileges). Design software modules with the minimal functionality needed to run with elevated privileges, and ensure that all other capabilities and functionalities are run with lower privileges (e.g., user space or application privileges).
- **PW.4.4 Example 8** (new): Regularly review all third-party libraries for ownership changes, and evaluate any impacts from a change in ownership.
- **PW.5.1 Example 10** (new): When designing interfaces that accept input, use well-structured input formats that can be easily validated and sanitized.
- **PW.5.1 Example 11** (new): Where appropriate, use formal methods and provers to validate the correctness of code. While particular attention should be given to high-risk code, other sections of code may also benefit from these techniques while balancing cost and risk trade-offs.
- **PW.8.2 Example 10** (new): Identify third-party dependencies, and conduct robust tests to exercise the functionality that uses these dependencies.
- **PW.9.1 Example 2** (new): Prohibit the use of default passwords or hard-coded secrets and protection mechanisms.
- **PW.9.1 Example 3** (new): Make available a robust range of settings with secure default values that enable software administrators to control logging capabilities (e.g., changes to configuration, security events, safety events) and how long log entries are retained.
- **RV.1.2 Example 3** (new): Monitor customer issues to determine whether default configurations should be updated and whether alerts should be added to the software to warn customers about insecure configurations.

**Reworded** (substantive ones marked ★; others editorial):

| Task / Example | SSDF 1.1 | SSDF 1.2 IPD |
|---|---|---|
| PO.1.1 Ex 3 | Review and update security requirements at least annually, or sooner if there are new requirements from internal or external sources, or a major security incident targeting software development infrastructure has occurred. | Review and update security requirements at least annually, or sooner if there are new requirements from internal or external sources, or if a major security incident targeting software development infrastructure has occurred. |
| ★ PO.1.2 Ex 1 | Define policies that specify risk-based software architecture and design requirements, such as making code modular to facilitate code reuse and updates; isolating security components from other components during execution; avoiding undocumented commands and settings; and providing features that will aid software acquirers with the secure deployment, operation, and maintenance of the software. | Define policies that specify risk-based software architecture and design requirements, such as making code modular to facilitate code reuse and updates, isolating security components from other components during execution, avoiding undocumented commands and settings, using consensus standards where available, and providing features that will aid software acquirers with the secure deployment, operation, and maintenance of the software, including secure default configurations. |
| PO.1.2 Ex 6 | Review all security requirements at least annually, or sooner if there are new requirements from internal or external sources, a major vulnerability is discovered in released software, or a major security incident targeting organization-developed software has occurred. | Review all security requirements at least annually, sooner if there are new requirements from internal or external sources, if a major vulnerability is discovered in released software, or if a major security incident targeting organization-developed software has occurred. |
| PO.1.3 Ex 2 | Define security-related criteria for selecting software; the criteria can include the third party’s vulnerability disclosure program and product security incident response capabilities or the third party’s adherence to organization-defined practices. | Define security-related criteria for selecting software, such as a third party’s vulnerability disclosure program, product security incident response capabilities, or adherence to their organization-defined practices. |
| PO.1.3 Ex 5 | Establish and follow processes to address risk when there are security requirements that third-party software components to be acquired do not meet; this should include periodic reviews of all approved exceptions to requirements. | Establish and follow processes to address risk when there are security requirements that third-party software components to be acquired do not meet, including periodic reviews of all approved exceptions to requirements. |
| ★ PO.2.1 Ex 3 | Define roles and responsibilities for cybersecurity staff, security champions, project managers and leads, senior management, software developers, software testers, software assurance leads and staff, product owners, operations and platform engineers, and others involved in the SDLC. | Define roles and responsibilities for cybersecurity staff, security champions, project managers and leads, senior management, software developers, software testers, software assurance leads and staff, product owners, operations, site reliability engineers and platform engineers, and others involved in the SDLC. |
| ★ PO.2.3 Ex 1 | Appoint a single leader or leadership team to be responsible for the entire secure software development process, including being accountable for releasing software to production and delegating responsibilities as appropriate. | Appoint a single leader (e.g., a senior executive or C-suite level sponsor) or a leadership team to be responsible for the entire secure software development process, including being accountable for releasing software to production and delegating responsibilities as appropriate. |
| PO.3.2 Ex 3 | Use code-based configuration for toolchains (e.g., pipelines-as-code, toolchains-as-code). | Use code-based configuration for toolchains (e.g., pipelines as code, toolchains as code). |
| PO.4.1 Ex 4 | Review the artifacts generated as part of the software development workflow system to determine if they meet the criteria. | Review the artifacts generated as part of the software development workflow system to determine whether they meet the criteria. |
| PO.5.1 Ex 2 | Use network segmentation and access controls to separate the environments from each other and from production environments, and to separate components from each other within each non-production environment, in order to reduce attack surfaces and attackers’ lateral movement and privilege/access escalation. | Use network segmentation and access controls to separate the environments from each other and production environments and to separate components from each other within each non-production environment in order to reduce attack surfaces and attackers’ lateral movement and privilege/access escalation. |
| PO.5.1 Ex 3 | Enforce authentication and tightly restrict connections entering and exiting each software development environment, including minimizing access to the internet to only what is necessary. | Enforce authentication, and tightly restrict connections entering and exiting each software development environment, including minimizing access to the internet to only what is necessary. |
| PO.5.2 Ex 1 | Configure each development endpoint based on approved hardening guides, checklists, etc.; for example, enable FIPS-compliant encryption of all sensitive data at rest and in transit. | Configure each development endpoint based on approved hardening guides and checklists (e.g., enable FIPS-compliant encryption of all sensitive data at rest and in transit). |
| PO.5.2 Ex 2 | Configure each development endpoint and the development resources to provide the least functionality needed by users and services and to enforce the principle of least privilege. | Configure development endpoints and resources to provide the least functionality needed by users and services and to enforce the principle of least privilege. |
| PO.5.2 Ex 5 | Require multi-factor authentication for all access to development endpoints and development resources. | Require multi-factor authentication for all access to development endpoints and resources. |
| PS.1.1 Ex 1 | Store all source code and configuration-as-code in a code repository, and restrict access to it based on the nature of the code. For example, open-source code intended for public access may need its integrity and availability protected; other code may also need its confidentiality protected. | Store all source code and configuration as code in a code repository, and restrict access to it based on the nature of the code. For example, open-source code intended for public access may need its integrity and availability protected; other code may also need its confidentiality protected. |
| PS.3.1 Ex 1 | Store the release files, associated images, etc. in repositories following the organization’s established policy. Allow read-only access to them by necessary personnel and no access by anyone else. | Store the release files, images, and other associated data in repositories following the organization’s established policy. Allow read-only access to them by necessary personnel and no access by anyone else. |
| ★ PW.4.4 Ex 1 | Regularly check whether there are publicly known vulnerabilities in the software modules and services that vendors have not yet fixed. | Regularly check whether there are publicly known vulnerabilities in the software modules and services that vendors have not yet remediated. |
| ★ PW.4.4 Ex 4 | Ensure that each software component is still actively maintained and has not reached end of life; this should include new vulnerabilities found in the software being remediated. | Ensure that each software component is still actively maintained and has not reached end of life. This should include assurance that new vulnerabilities found in the software are being remediated and should extend to software that has been acquired as part of a merger or acquisition. |
| ★ PW.8.2 Ex 1 | Perform robust functional testing of security features. | Perform robust functional testing of security features, including failure path testing. |
| PW.9.2 Ex 4 | Store the default configuration in a usable format and follow change control practices for modifying it (e.g., configuration-as-code). | Store the default configuration in a usable format and follow change control practices for modifying it (e.g., configuration as code). |
| RV.1.3 Ex 1 | Establish a vulnerability disclosure program, and make it easy for security researchers to learn about your program and report possible vulnerabilities. | Establish a vulnerability disclosure program, and make it easy for security researchers to learn about the program and report possible vulnerabilities. |
| RV.1.3 Ex 3 | Have a security response playbook to handle a generic reported vulnerability, a report of zero-days, a vulnerability being exploited in the wild, and a major ongoing incident involving multiple parties and open-source software components. | Have a security response playbook to handle a generic reported vulnerability, a report of zero days, a vulnerability being exploited in the wild, and a major ongoing incident involving multiple parties and open-source software components. |
| ★ RV.2.2 Ex 2 | If a permanent mitigation for a vulnerability is not yet available, determine how the vulnerability can be temporarily mitigated until the permanent solution is available, and add that temporary remediation to the plan. | If a remediation for a vulnerability is not yet available, determine how the vulnerability can be temporarily mitigated until the permanent solution is available, and add that temporary mitigation to the plan. |
| RV.2.2 Ex 3 | Develop and release security advisories that provide the necessary information to software acquirers, including descriptions of what the vulnerabilities are, how to find instances of the vulnerable software, and how to address them (e.g., where to get patches and what the patches change in the software; what configuration settings may need to be changed; how temporary workarounds could be implemented). | Develop and release security advisories that provide the necessary information to software acquirers, including descriptions of what the vulnerabilities are, how to find instances of the vulnerable software, and how to address them (e.g., where to get patches and what the patches change in the software, what configuration settings may need to be changed, how temporary workarounds could be implemented). |
| ★ RV.2.2 Ex 5 | Update records of design decisions, risk responses, and approved exceptions as needed. See PW.1.2. | Update and periodically review records of design decisions, risk responses, and approved exceptions as needed. See PW.1.2. |

## 5. Reference (crosswalk) changes

- **EO14028 removed from all 42 tasks that carried it**, and the SSDF 1.1 Appendix A (EO 14028 §4e clause → SSDF task mapping) is gone; `[EO14028]` is no longer in the reference list and `[EO14306]` is added (cited only in front matter, not mapped to tasks). Consumers that used the SSDF as the EO 14028 / OMB M-22-18 attestation crosswalk must keep using `sp-800-218` (1.1) for that mapping.
- **SP80053 mappings rewritten for the 35 pre-existing tasks that had one in 1.1** (no 1.1 SP80053 line survives unchanged) against SP 800-53 **Release 5.2.0** (Aug 2025), with zero-padded control ids (`SA-08` not `SA-8`), and generally broader control sets (e.g. PO.1.1 adds AT-03, CM-01, PL-08, PM-01, SA-02, SA-10, SA-17, SR-01, SR-05).
- **SP80053 newly added** to 7 tasks that had no SP 800-53 mapping in 1.1: PO.2.3, PW.1.3, PW.2.1, PW.5.1, PW.9.1, RV.3.1, RV.3.2 (PW.1.3 also gains an SP800161 line).
- **SP800161 mappings rewritten for 25 tasks** (now SP 800-161r1-upd1), **added to 1 task that had none (PW.1.3)**, and **removed entirely from 10 tasks**: PO.1.3, PO.2.1, PW.4.2, PW.6.1, PW.7.1, PW.8.1, RV.1.2, RV.1.3, RV.3.3, RV.3.4. SP 800-161 is no longer a copy of the SP 800-53 list. Notably PO.1.3 — communicating security requirements to third-party suppliers — no longer maps to the C-SCRM publication at all, and its SP 800-53 mapping shrinks from SA-4, SA-9, SA-10, SA-10(1), SA-15, SR-3, SR-4, SR-5 to CA-03, SA-04, SA-21.
- All other schemes (BSAFSS, BSIMM, CNCFSSCP, IDASOAR, IEC62443, IR8397, ISO27034, ISO29147, ISO30111, MSSDL, NISTCSF, NISTLABEL, NTIASBOM, OWASP*, PCISSLC, SC*, SP800160, SP800181, SP800216) are **identical** to 1.1 for every pre-existing task. Their cited editions were not refreshed: BSIMM12 (2021; current BSIMM is far later), OWASP SAMM 1.5 (2017; SAMM 2.x current), OWASP ASVS 4.0.3 (ASVS 5.0 current), CSF 1.1 subcategories (CSF 2.0 exists and is cited only for PO.6). The URLs were changed to “latest version available at” for BSIMM and CNCF.

### SP 800-53 / SP 800-161 mapping per task (verbatim)

| Task | SP80053 1.1 | SP80053 1.2 IPD | SP800161 1.1 | SP800161 1.2 IPD |
|---|---|---|---|---|
| PO.1.1 | SA-1, SA-8, SA-15, SR-3 | AT-03, CM-01, PL-08, PM-01, SA-01, SA-02, SA-08, SA-10, SA-15, SA-17, SR-01, SR-03, SR-05 | SA-1, SA-8, SA-15, SR-3 | AT-03, CM-01, PL-07, PL-08, SR-05 |
| PO.1.2 | SA-8, SA-8(3), SA-15, SR-3 | CA-03, CM-08, PM-01, PM-08, PM-18, PM-30, RA-03, SA-02, SA-04, SR-02 | SA-8, SA-15, SR-3 | CM-02, CM-07, PM-30, RA-03, RA-09, SC-07 |
| PO.1.3 | SA-4, SA-9, SA-10, SA-10(1), SA-15, SR-3, SR-4, SR-5 | CA-03, SA-04, SA-21 | SA-4, SA-9, SA-9(1), SA-9(3), SA-10, SA-10(1), SA-15, SR-3, SR-4, SR-5 | None |
| PO.2.1 | SA-3 | AC-02, AC-03, CM-05, CA-07 | SA-3 | None |
| PO.2.2 | SA-8 | AT-03, SA-16 | SA-8 | AT-03 |
| PO.2.3 | None | PM-03 | (unchanged) | (unchanged) |
| PO.3.1 | SA-15 | CM-08, SA-15, SA-17, SR-09 | SA-15 | CM-08, SR-09 |
| PO.3.2 | SA-15 | CM-06, CM-08, CM-10, CM-11, CM-14, SA-15, SA-17, SR-09 | SA-15 | CM-06, CM-08, SR-09 |
| PO.3.3 | SA-15 | AC-02, AU-03, AU-06, AU-07, AU-09, AU-12, CM-06, SA-15, SI-06, SI-12 | SA-15 | AU-06, CM-06 |
| PO.4.1 | SA-15, SA-15(1) | CM-09, SA-11, SA-15, SA-15(01), SI-06 | SA-15, SA-15(1) | SA-11 |
| PO.4.2 | SA-15, SA-15(1), SA-15(11) | SA-11, SA-15, SA-15(01), SA-15(11), SI-12 | SA-15, SA-15(1), SA-15(11) | SA-11 |
| PO.5.1 | SA-3(1), SA-8, SA-15 | AC-04, CM-02, CM-12, PL-08, SA-03, SA-03(01), SA-08, SA-15, SA-17, SC-07, SC-07(01), SC-07(29) | SA-3, SA-8, SA-15 | AC-04, CM-02, CM-12, PL-08, SA-03, SC-07 |
| PO.5.2 | SA-15 | CM-02, CM-03, CM-04, CM-06, CM-14, SA-15, SA-17 | SA-15 | CM-02, CM-03, CM-06 |
| PS.1.1 | SA-10 | AC-03, AC-06, CM-05, SA-10, SC-12, SC-28, SI-12 | SA-8, SA-10 | AC-03, SC-28 |
| PS.2.1 | SA-8 | AU-07, SA-05, SA-08, SA-11 | SA-8 | SA-11 |
| PS.3.1 | SA-10, SA-15, SA-15(11), SR-4 | CM-08, CM-12, CP-06, CP-09, MP-02, MP-03, MP-04, SA-10, SA-15, SA-15(11), SC-08, SC-28, SI-12, SR-04 | SA-8, SA-10, SA-15(11), SR-4 | MP-01, SC-28, SC-36, SR-04 |
| PS.3.2 | SA-8, SR-3, SR-4 | CM-08, CM-12, SA-08, SR-03, SR-04 | SA-8, SR-3, SR-4 | CM-08, CM-12 |
| PW.1.1 | SA-8, SA-11(2), SA-11(6), SA-15(5) | AT-03, CA-02, CA-08, RA-03, SA-08, SA-11, SA-11(02), SA-11(06), SA-15, SA-15(05), SI-02 | SA-8, SA-11(2), SA-11(6), SA-15(5) | AT-03, CA-02, RA-03, RA-09 |
| PW.1.2 | SA-8, SA-10, SA-17 | CA-07, CM-02, CM-03, CM-04, CM-06, CM-09, PL-06, PL-08, RA-03, SA-08, SA-10, SA-17 | SA-8, SA-17 | CM-02, CM-03, CM-06, RA-03, RA-09 |
| PW.1.3 | None | AU-03, CM-02, CM-06, CM-07, PL-09, SA-08, SA-17 | None | CM-02, CM-06 |
| PW.2.1 | None | CA-01, CA-03 | (unchanged) | (unchanged) |
| PW.4.1 | SA-4, SA-5, SA-8(3), SA-10(6), SR-3, SR-4 | CM-08, SA-04, SA-05, SA-10(06), SC-12, SR-03, SR-04 | SA-4, SA-5, SA-8(3), SA-10(6), SR-3, SR-4 | SR-13 |
| PW.4.2 | SA-8(3) | CM-09, CM-11, SA-15, SA-17, SA-20 | SA-8(3) | None |
| PW.4.4 | SA-9, SR-3, SR-4, SR-4(3), SR-4(4) | CA-02, CA-05, CA-06, SA-09, SR-03, SR-04, SR-04(03), SR-04(04) | SA-4, SA-8, SA-9, SA-9(3), SR-3, SR-4, SR-4(3), SR-4(4) | SR-03, SR-04 |
| PW.5.1 | None | SA-15, SI-03, SI-10, SI-10(03) | (unchanged) | (unchanged) |
| PW.6.1 | SA-15 | CM-09, SA-15 | SA-15 | None |
| PW.6.2 | SA-15, SR-9 | CM-02, CM-09, SA-15, SC-38, SR-09 | SA-15, SR-9 | SR-09 |
| PW.7.1 | SA-11 | CA-02, CM-09, RA-05, SA-11 | SA-11 | None |
| PW.7.2 | SA-11, SA-11(1), SA-11(4), SA-15(7) | CA-02, CM-09, RA-05, SA-11, SA-11(01), SA-11(04), SA-15, SA-15(07), SI-02 | SA-11, SA-11(1), SA-11(4), SA-15(7) | CA-02 |
| PW.8.1 | SA-11 | RA-05, SA-11, SA-15 | SA-11 | None |
| PW.8.2 | SA-11, SA-11(5), SA-11(8), SA-15(7) | CA-02, CM-03, CM-09, RA-05, RA-05(03), SA-11, SA-11(05), SA-11(08), SA-15, SA-15(07), SI-02 | SA-11, SA-11(5), SA-11(8), SA-15(7) | CA-02, CM-03 |
| PW.9.1 | None | CM-02, CM-06, CM-09 | (unchanged) | (unchanged) |
| PW.9.2 | SA-5, SA-8(23) | AC-02, AC-03, CM-02, CM-06, SA-05, SA-08, SA-08(23) | SA-5, SA-8(23) | CM-02, CM-06 |
| RV.1.1 | SA-10, SR-3, SR-4 | RA-05, SA-10, SI-05, SR-03, SR-04 | SA-10, SR-3, SR-4 | SR-04 |
| RV.1.2 | SA-11 | CM-06, RA-05, SA-11, SI-07 | SA-11 | None |
| RV.1.3 | SA-15(10) | AC-02, AC-03, CM-09, IR-01, IR-08, RA-05, RA-05(11), SA-15, SA-15(10) | SA-15(10) | None |
| RV.2.1 | SA-10, SA-15(7) | CM-03, CM-04, RA-05, RA-05(04), SA-10, SA-15(07) | SA-15(7) | CM-03 |
| RV.2.2 | SA-5, SA-10, SA-11, SA-15(7) | CM-03, CM-04, CM-05, CM-06, SA-05, SA-10, SA-11, SA-15, SA-15(07) | SA-5, SA-8, SA-10, SA-11, SA-15(7) | CM-03, CM-06 |
| RV.3.1 | None | RA-05, SA-11, SA-11(02) | (unchanged) | (unchanged) |
| RV.3.2 | None | CA-07, CA-07(03), RA-05, RA-05(06), RA-05(08) | (unchanged) | (unchanged) |
| RV.3.3 | SA-11 | RA-05, RA-05(02), RA-05(06), RA-05(10), SA-11, SI-02, SI-02(07) | SA-11 | None |
| RV.3.4 | SA-15 | AU-02, RA-01, SA-03, SA-15 | SA-15 | None |

## 6. Change-log accuracy (source defects in the draft)

- Appendix B lists 2 task-text changes; there are 8 (§3). It lists example rewording for PO.1.2 Ex1, PO.2.1 Ex3, PO.2.3 Ex1, PW.4.4 Ex1/Ex4, PW.8.2 Ex1, RV.2.2 Ex2/Ex5; the diff also finds rewording in PO.1.1, PO.1.2 Ex6, PO.1.3, PO.3.2, PO.4.1, PO.5.1, PO.5.2, PS.1.1, PS.3.1, PW.9.2, RV.1.3 and RV.2.2 Ex3 — covered only by the blanket “Minor editorial changes throughout the document”.
- The Acknowledgments say the revision authors are responsible for “the changes identified in the change log (Appendix C)”; the change log is Appendix B in this draft.
- Appendix B describes the 1.1 history as “Deleted PW.4.5 (merged into PW.4.4)” while the draft-2021 entry says “moved PW.3.2 to PW.4.5”; Table 1 shows PW.3.2 “Moved to PW.4.4” and PW.4.5 “Moved to PW.4.1 and PW.4.4” — consistent end state, inconsistent narrative.

## 7. What it means for us

- Requirement ids are stable across 1.1 → 1.2: every 1.1 task id survives with the same meaning, so `sp-800-218#PO.1.1` and `sp-800-218r1#PO.1.1` can be linked 1:1 (`same_as_task` with a `text_changed` flag). New ids: PO.6.1–PO.6.3, PS.4.1–PS.4.4.
- The two new practices are the first in the SSDF about **continuous improvement of the SDLC itself** (PO.6) and **update delivery reliability** (PS.4: staged roll-out, rollback, update engine resilience)
- For the crosswalk (R-044), take SP 800-53 mappings from 1.2 IPD only as provisional; take EO 14028 mappings from 1.1 only.


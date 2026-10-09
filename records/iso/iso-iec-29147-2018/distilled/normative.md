---
schema: "library-doc/v1"
id: iso-iec-29147-2018-normative
record: iso-iec-29147-2018
type: normative
updated: "2026-10-02"
---

# ISO/IEC 29147:2018 — normative content (free preview only)

**Coverage.** Everything normative or definitional in the **free preview** of ISO/IEC 29147:2018,
verbatim, with locators: scope, normative references, all eight terms and definitions (Clause 3),
the abbreviations, the three shall/should statements, and Figure 1. The preview ends at the first
sentence of §5.3.2 (printed page 5).

**Not covered — not available to us.** §5.3.3–§5.11 (concepts incl. stakeholder roles 5.5,
the vulnerability handling process summary 5.6 with embargo period 5.6.8, information exchange 5.7,
confidentiality 5.8, advisories 5.9), **Clause 6 Receiving vulnerability reports, Clause 7
Publishing vulnerability advisories (incl. the 16 advisory elements 7.4.2–7.4.17), Clause 8
Coordination, Clause 9 Vulnerability disclosure policy (required / recommended / optional policy
elements)**, Annexes A–D (Annex D is the summary of normative elements) and the Bibliography. These
are where nearly all provisions on vendors sit. The heading structure of all of them is known from
the Contents and is recorded in `messages.yaml`, `protocol.yaml` and `object-model.yaml` as
*inferred-from-heading* only. ISO/IEC 29147:2018 was **not** on the ISO/ITTF Publicly Available
Standards list (only the 2014 first edition was; the ITTF site is now closed); it is paywalled.

Source: distributor-sample (iTeh/SIST) preview PDF (sha256 `e433e9e1…a8c1`), captured as
`.cache/iso-iec-29147-2018.md`.

## Clause 1 — Scope

> This document provides requirements and recommendations to vendors on the disclosure of
> vulnerabilities in products and services. Vulnerability disclosure enables users to perform technical
> vulnerability management as specified in ISO/IEC 27002:2013, 12.6.1[1]. [...] This document provides:
> — guidelines on receiving reports about potential vulnerabilities;
> — guidelines on disclosing vulnerability remediation information;
> — terms and definitions that are specific to vulnerability disclosure;
> — an overview of vulnerability disclosure concepts;
> — techniques and policy considerations for vulnerability disclosure;
> — examples of techniques, policies (Annex A), and communications (Annex B).
>
> Other related activities that take place between receiving and disclosing vulnerability reports are
> described in ISO/IEC 30111.
>
> This document is applicable to vendors who choose to practice vulnerability disclosure to reduce risk
> to users of vendors’ products and services.

Note the applicability condition: **vendors who choose to practice vulnerability disclosure** — the
standard is opt-in; regulation (e.g. the EU CRA, Annex I Part II) is what makes a disclosure policy
mandatory.

## Clause 2 — Normative references

ISO/IEC 27000 (vocabulary); **ISO/IEC 30111** (undated — latest edition applies).

## Clause 3 — Terms and definitions (verbatim)

| no. | term | definition | notes to entry |
|---|---|---|---|
| 3.1 | vulnerability | functional behaviour of a product or service that violates an implicit or explicit security policy | Note 1: ISO/IEC 27002:2013, 12.6.1 uses the term “technical vulnerability” to distinguish between the more general risk-based concept of vulnerability and the term used in this document. |
| 3.2 | disclosure | act of initially providing vulnerability (3.1) information to a party that was not believed to be previously aware | — |
| 3.3 | coordination | set of activities including identifying and engaging stakeholders, mediating, communicating, and other planning in support of vulnerability (3.1) disclosure (3.2) | Note 1: The term “coordinated vulnerability disclosure” is used to denote a disclosure process that includes coordination. |
| 3.4 | vendor | individual or organization that is responsible for remediating vulnerabilities | Note 1: A vendor can be the developer, maintainer, producer, manufacturer, supplier, installer, or provider of a product or service. |
| 3.5 | reporter | individual or organization that notifies a vendor (3.4) or coordinator (3.6) of a potential vulnerability (3.1) | Note 1: There are no special requirements for acting as a reporter. Reporters can be individuals, organizations, amateurs or hobbyists, professionals, end-users, security research organizations, vendors, governments, or coordinators. Note 2: The term “reporter” does not imply unique or original discovery or reporting. Note 3: Reporters can be called researchers, whether or not the reporter explicitly performs security or vulnerability research. Historically, this role is also referred to as “finder.” |
| 3.6 | coordinator | individual or organization that performs coordination (3.3) | — |
| 3.7 | remediation | change made to a product or service to remove or mitigate a vulnerability (3.1) | Note 1: A remediation typically takes the form of a binary file replacement, configuration change, or source code patch and recompile. Different terms used for “remediation” include patch, fix, update, hotfix, and upgrade. Mitigations are also called workarounds or countermeasures. |
| 3.8 | advisory | document or message that provides vulnerability (3.1) information intended to reduce risk | Note 1: An advisory is meant to inform users or other stakeholders about a vulnerability including, if possible, how to identify and remediate vulnerable systems. |

Clause 4 abbreviations relevant to formats and protocols: CVE [9], CVRF [12][13] (the
predecessor of OASIS CSAF), CVSS [10], CWE [11], OpenPGP, S/MIME, TLS, HTTP(S), PSIRT, CSIRT, CRM, PoC.

## Normative statements in the preview

| id | locator | form | text |
|---|---|---|---|
| intro-R01 | Introduction | should | Vendors should adapt the additional informative guidance in this document to fit their particular needs and those of users and other stakeholders. |
| 5.2-R01 | §5.2 | should | For example, a vendor should ideally develop policy (Clause 9) before starting to receive reports (Clause 6). |
| 5.3.1-R01 | §5.3.1 | shall | ISO/IEC 30111 shall be used in conjunction with this document. |

Normative framing sentence (Introduction, immediately before intro-R01): "The normative elements in
this document provide minimum requirements to create a functional vulnerability disclosure
capability." §5.2: "Annex D contains a summary of all of the normative elements in this document."

## Division of labour with ISO/IEC 30111 (§5.3.1, verbatim)

> This document provides guidelines for vendors to include in their normal business processes when
> receiving reports about potential vulnerabilities from external individuals or organizations and when
> distributing vulnerability remediation information to affected users.
>
> ISO/IEC 30111 gives guidelines on how to investigate, process, and resolve potential vulnerability
> reports.
>
> While this document deals with the interface between vendors and reporters, ISO/IEC 30111 deals
> with internal vendor processes including the triage, investigation, and remediation of vulnerabilities,
> whether the source of the report is external to the vendor or from within the vendor’s own security,
> development, or testing teams.

Figure 1 is transcribed in `protocol.md` and `object-model.md`.

*— end of free preview —*

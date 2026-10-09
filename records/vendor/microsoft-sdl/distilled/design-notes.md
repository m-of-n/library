---
schema: "library-design-notes/v1"
id: microsoft-sdl-design-notes
record: microsoft-sdl
kind: design-notes
type: design-notes
title: "microsoft-sdl — bearing on the tmodel design"
extracted: "2026-10-02"
updated: "2026-10-02"
reviewed_by: ""
---

Ids cited: `ARCH-0001-PROPOSAL-v0.2.0` §1, §2, §2a, §3b, §4, §5; `DL-0009`
R-040…R-044; `MAP-0001`. **[analysis]** marks our reasoning. SDL is post-MVP.

## Adopt

1. **Practice 3 confirms the tmodel core.** The SDL's threat-modeling steps —
   use cases/scenarios and assets (3.1), architecture overview with a DFD and
   trust boundaries (3.2), threats per STRIDE plus "thinking like an attacker"
   (3.3), mitigations tracked as work items and tested (3.4), communicated to
   stakeholders (3.5) — map onto ARCH §1 (Asset, Process/DataFlow/DataStore/
   ExternalEntity, TrustBoundary), §2 (STRIDE as a method facet) and §5
   (MitigationInstance with linked work item and verification evidence).
   **Adopt** the "well-written threat" field list (threat actor, preconditions,
   what the actor does, consequences for assets and users — 3.3) as the minimum
   descriptive fields of a ThreatInstance; it matches ARCH §2a pre/postconditions.
2. **"Threat modeling is not complete until you create work items" (3.4/3.5).**
   This is a completeness rule tmodel can automate for R-042: a ThreatInstance
   with disposition *mitigate* must have ≥1 MitigationInstance with an
   `external_ref` work item and a verification test. **Adopt** as a conformance
   check.
3. **Exception lifecycle (1.4) → risk-acceptance disposition (R-042, DEC-009).**
   The seven steps give a full lifecycle: triage (reason, short-term actions,
   remediation plan, expiry), severity-based approver level, approval workflow,
   tracking, re-review on risk change, re-approval on expiry
   (`state-machine.yaml`, `protocol.yaml`). **Adopt** for the *accept*
   disposition of a ThreatInstance: an accepted risk is an exception with an
   expiry and an approver whose level depends on severity.

## Adapt

4. **Bug bar (1.3) → Gate exit criterion (R-041/R-042).** "all known
   vulnerabilities discovered with a 'critical' or 'important' severity rating
   must be fixed with a specified time frame" — adapt into a Gate criterion over
   Findings by severity, with the bar versioned ("never relaxing it once it's been
   set").
5. **Lifecycle stages (Design, Code, Build and Deploy, Run + Zero Trust) vs
   ARCH §3b LifecyclePhase.** Four coarse stages; map Design→design,
   Code→implementation, Build and Deploy→release/distribution, Run→operation.
   Zero Trust is a cross-cutting principle, not a phase.
6. **Mitigation kind (R-040).** The practice set contains all three kinds:
   technical (2.1 MFA/least privilege, 4.1 encryption, 6.2 branch protection,
   8.10 DDoS), documentation (1.1 standards, 9.2 incident response plan, 5.3
   SBOM) and process (1.4 exception process, 3 threat modeling, 7 testing,
   10 training). **[analysis]** strong support for R-040's three-valued kind.

## Reject

7. **Using the current practice set as an auditable gate model.** Unlike
   SDL 5.2 (Final Security Review with outcomes) there is no release gate,
   sign-off or work-product list; the pages are guidance with product links.
   R-041's Gate must be taken from `microsoft-sdl-5-2` (FSR), `bsimm-16`
   (SM1.4/SM1.7/SM2.6) or SSDF PO.4 — MAP-0001 row 15's "#1 approx" is right to
   be approximate.
8. **Product-specific resources as requirements.** Many sub-practices are
   Azure/GitHub product pointers (6.4 Dev Box, 6.5 Codespaces, 6.6 Azure
   Deployment Environments); they are recorded but should not become
   vendor-neutral Requirements.

## Crosswalk (R-044)

Microsoft publishes no mapping. OWASP SAMM's spreadsheet maps 47 SAMM-stream
pairs onto these sub-practice ids (`owasp-samm-2/distilled/crosswalk.yaml`), e.g.
D-TA-B → 3.1, 3.3, 3.5. MAP-0001 columns "MS SDL (current 10)" should cite
`microsoft-sdl#3.x` etc. rather than practice numbers only.

## Source observations

- Practice 3's page title reads "Perform secure design review and threat
  modeling" while the index says "Perform security design review and threat
  modeling".
- 3.4's final paragraph is repeated verbatim as the body of 3.5.
- Practice 10 repeats its threat-modeling-training paragraph, the second time
  with a garbled lead-in ("In particular, developers and the Since engineers…").
- 2.2/2.3 cite "Microsoft Build ... [link when available]" placeholders (Build
  2024 sessions BRK231/BRK226), dating the current text to ~2024.
- The FAQ still lists the older twelve-practice set and points to the 2010
  *Simplified Implementation*; the Resources page files SDL 5.2 and the
  Simplified paper under "Legacy archive".

## Open questions

1. Microsoft's "SDL for AI" (blog, 2026-02-03) announces six AI focus areas
   (threat modeling for AI, AI observability, AI memory protections, agent
   identity and RBAC, AI model publishing, AI shutdown) with guidance "in coming
   months"; the practice pages have not changed yet. Track as a future record.
2. Should SecurityAssumption (3.3) become a tmodel node (validated / invalid)?

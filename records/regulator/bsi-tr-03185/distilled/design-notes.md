---
schema: "library-distilled/v1"
id: bsi-tr-03185-design-notes
record: bsi-tr-03185
type: design-notes
updated: "2026-10-02"
---

# BSI TR-03185: design notes for tmodel

How TR-03185 v1.1.1 bears on ARCH-0001 v0.2.0 and DL-0009 (R-040 to R-044, DEC-009). The SDL work is
post-MVP under the ADR-0002 scope guard. The only exception is R-040, which is MVP-adjacent.

## Adopt

- **R-042 conformance: use the TR's threat-model clauses as the test of what "threat model is conformant"
  means.** PROD.DEV.C.1 to C.5 give a checkable definition:
  - performed in design;
  - covers sensitive data flows, trust boundaries, processes, data storage, external dependencies,
    protocols, debug interfaces, severity and mitigations "where applicable";
  - reviewed by the team;
  - updated regularly or on occasion while the product is in use;
  - every finding "evaluated and addressed".

  This is the closest any SDL source in the library comes to the DL-0009 rule that every ThreatInstance has
  an approved MitigationInstance. C.5 is a direct match. C.2's element list matches our DFD layer (§1.2),
  plus debug interfaces and protocols, which are worth adding as AttackSurface examples.
- **R-041 Gate: the TR's release gate is a ready-made set of exit criteria.** PROD.TEST.A.17 requires two
  things: results match the pre-defined expectations, and all security-related issues are conclusively
  addressed. PROD.PM.A.14 requires documented completion of all security activities. PROD.TEST.A.3 requires
  a written release-rejection procedure. Model Release as the reference Gate with exactly these three
  criteria.
- **R-044 crosswalk: ingest BSI's requirement-level mapping as published crosswalk data.** The
  Prüfspezifikation sheet maps each Part 1 requirement to IT-Grundschutz requirement ids, IEC 62443-4-1 ids
  (42 distinct: SM-1/2/4/6–13, SR-2/5, SD-1–4, SI-1/2, SVV-1–5, DM-1–6, SUM-1–5, SG-1–7), NESAS FS.16 ids and
  SSDF task ids. `distilled/crosswalk.yaml` has the inverse index. This is a primary source for verifying
  the MAP-0001 IEC 62443-4-1 column. MAP-0001 flagged those ids as unverified because the IEC PDF returned
  403.
- **R-040 mitigation kind: the TR uses all three kinds.**
  - Technical: secure design principles (PROD.DEV.B.4), integrity mechanisms (PROD.REL.1).
  - Documentation: user documentation and hardening guidance (PROD.DOC.B.*), security update documentation
    (PROD.FIX.A.10).
  - Process: separation of duties, code review, regression testing.

  It is evidence that `kind ∈ {technical, documentation, process}` is the right enum.

## Adapt

- **DEC-009 mitigation lifecycle.** PROD.FIX.A.8's remedy options are fix, plan, move to a future version,
  or no fix with an acceptable residual risk. Every option requires an explicit residual-risk level. Map
  them onto the MitigationInstance status: `planned`, `deferred`, `implemented`, `risk-accepted`. A
  `risk-accepted` state must be backed by a Review that records the accepted residual risk level. The
  periodic review "during each release or iteration cycle as a minimum" is a re-evaluation trigger that
  DEC-009 should carry.
- **R-044 maps_to strength.** Add a `strength` attribute to maps_to with at least these values:
  - `source-of`: the requirement was compiled from the target (Part 1, Prüfspezifikation).
  - `induced-by`: the TR states the requirement is "neither directly derived from nor equivalent to" the
    target (Part 2).
  - `equivalent`.

  Without this attribute a crosswalk would overstate equivalence that BSI explicitly denies.
- **Perspective.** Represent the tool-user versus producer split as a role of the manufacturer `Party` with
  respect to a Component. The same manufacturer consumes tools and produces the product, which is the
  relational-role rule in §2b. The development Environment then becomes something requirements apply to.
  This also covers §0.1: AI code assistants, LLMs and AI vulnerability scanners count as "resources and
  tools used".
- **R-043 governed views.** The TR's documents are the views DL-0009 wants governed:
  - project documentation (traceability of decisions, PROD.DOC.A.1);
  - user documentation (version-bound, PROD.DOC.B.6);
  - patch and change management document;
  - requirements catalogue.

  PROD.PM.A.11 ("project versioning tool ... to identify and monitor decisions, changes and their
  responsibilities") and PROD.PM.A.12 (manage all requirement and design changes) are the change-tracking
  half of R-043.
- **Audit verdict shape.** The BSI audit verdict is binary Pass/Fail per requirement, with evidence
  references. A conformance result in R-042 should support this. A richer status (partial, N/A,
  tailored-out) is our extension and must not be read back into BSI's scheme.

## Reject or do not carry

- **No time model.** TR-03185 sets no numeric SLAs: "timely" and "promptly" are left to "market conditions"
  (footnotes 5 and 7). Do not derive deadlines from it. For a regulatory clock, use the CRA
  (24 h / 72 h / 14 days, `eu-cra-2024-2847`).
- **Processes are not phases.** Do not encode TR "processes" as ordered LifecyclePhases or gates. §1.2.2 says
  the order "does not represent a mandatory chronological sequence". Map each process to a canonical phase
  only for crosswalk purposes (`phase` in requirements.yaml).
- **Severity.** The TR names CVSS only as an example of "a vulnerability assessment system". It does not
  constrain DEC-003, and it does not support re-indexing S/F/O/P (the critic's H3 guardrail).

## Open questions

1. **Defect in the source: there is no PROD.DEV.E.2.** The design-review table goes from E.1 to E.3. The gap
   is also in the German v1.0 and in the Prüfspezifikation. Group letters J and K are also unused (H, I, L).
   This needs confirmation from BSI (tr03185@bsi.bund.de) before anyone cites "E.2".
2. **Defect in the source: the v1.0 date.** EN Table 3 dates v1.0 "2024-09-06". The German v1.0 cover and
   the BSI landing page say 06.08.2024. One of them transposes day and month. We record **2024-08-06**
   because both German sources agree.
3. **Defect in the source: a reference that no longer exists.** §2.1.1 says the frameworks are listed in
   "section 3", but the merged document has no section 3. The list is in §2.3.
4. **Defect in the source: the Prüfspezifikation lags the merged edition.** It cites German v1.0 chapter
   numbers (3.1.1 …), not the EN v1.1.1 numbering (1.3.1.1.1 …). It writes some ids non-canonically
   (USER.PM.C1, PROD-FIX.A.5). Certification is still against the German v1.0. The English v1.1.1 is the
   current document line, but it is not yet the certification basis.
5. **Two definitions of "Manufacturer"** in one document. §1.2.1 uses the producer-of-software definition;
   Part 2 Table 34 uses the CRA wording. Which one does a conformance claim on a mixed proprietary/OSS
   product use? tmodel's `Party` should not hard-code either.
6. **Who conforms in Part 2?** §2.2.3 deliberately assigns no responsible party. It offers three options in
   order of preference: manufacturer or steward upstream, upstream maintainers, or a downstream fork. For
   R-042, the conformance subject for an OSS Component has to be a (Component, implementing Party) pair,
   not the Component alone.
7. **Lower-case "shall" in §0.1.** The AI-risk sentence ("Such risks shall be considered") falls outside the
   TR's capitalised-verb convention. We extracted it as `R-0001`, `kind: inferred`. Its normative force
   needs human review.

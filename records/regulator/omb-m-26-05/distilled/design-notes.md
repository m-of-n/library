---
schema: "library-distilled/v1"
id: omb-m-26-05-design-notes
record: omb-m-26-05
type: design-notes
updated: "2026-10-02"
reviewed_by: ""
---

# OMB M-26-05 — design notes for tmodel

**This is the current US federal policy** (2026-01-23; no later OMB software-security memo
through M-26-19, Sept 2026). It withdraws the uniform attestation gate of M-22-18/M-23-16.

## Adopt

- **Conformance is a profile, not a fixed baseline (R-042, R-044).** "There is no universal,
  one-size-fits-all method"; each agency develops "assurance policies and processes that match
  their risk determinations and mission needs" (R-0005). tmodel's conformance check should
  evaluate a Product against a *selected* requirement profile (a governed set drawn from the
  crosswalk), owned and approved by the consuming Party — the same mechanism serves an SDL plan
  (producer side) and an acquirer policy (consumer side).
- **Risk-based validation of the provider (R-042).** R-0003: validate provider security "based on
  a comprehensive risk assessment". tmodel's threat model *is* such a risk assessment; the
  conformance view should be able to show "threats mitigated" as the evidence for a risk-based
  acceptance, not only a checklist of practices.
- **Inventory as a governed view (R-043).** R-0005 keeps the inventory obligation and widens it to
  hardware.

## Adapt

- **Runtime SBOM for cloud platforms (R-0008)** — an SBOM of the *runtime production
  environment*, not the shipped artifact. tmodel's `Deployment`/`Environment` (ARCH-0001 §3)
  is where that evidence attaches, not the `Product`.
- **Hardware in scope (HBOM)** — Component already models chips/cores; add HBOM as an evidence
  kind when a hardware record is ingested (CISA HBOM framework is cited but not held).

## Reject

- Nothing to reject; the memo is deliberately permissive. Note the policy risk: a tmodel
  conformance feature should not assume any single mandated baseline (SSDF attestation was
  mandatory 2022-2026 and is now optional).

## Open questions

1. Should rescission be modelled as a document-level status that cascades to all requirements of
   the rescinded documents (our approach: each omb-m-22-18/23-16 requirement carries
   `status: rescinded`), or as an edge resolved at query time?
2. Ingest CISA's HBOM framework (Sept 2023) and the 2025 SBOM minimum elements draft (held as
   cisa-2026-sbom-minimum?) — check which version the library record tracks.

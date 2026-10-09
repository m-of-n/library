---
schema: "library-distilled/v1"
id: omb-m-23-16-design-notes
record: omb-m-23-16
type: design-notes
updated: "2026-10-02"
reviewed_by: ""
---

# OMB M-23-16 — design notes for tmodel

Rescinded 2026-01-23 (omb-m-26-05). Read together with omb-m-22-18 design notes; only deltas here.

## Adopt

- **Accountability follows the end product (R-042, ARCH-0001 §2b).** "Attestations must be
  collected from the producer of the software end product" and third-party components are the
  end-product producer's burden (B.1-1, B.1-5). In tmodel this is a *responsibility* edge from the
  supplier `Party` across `composed_of`: conformance of a `Product` covers its components, and a
  component-level threat's mitigation can be owned by the end-product supplier. Adopt as the
  default ownership rule for component threats in DEC-009.
- **Compound guard on continued use (R-042).** Use under a POA&M requires *both* the agency's
  satisfactory finding *and* a filed extension (C-2, C-5). A conformance check is therefore a
  predicate over several Reviews, not a single approval. The conformance engine must support
  conjunctions of approvals with validity windows.
- **Relative milestones (R-041).** Deadlines are re-anchored on an external event (PRA approval of
  the common form). Confirms the `Milestone.offset_from` design noted in omb-m-22-18.
- **Explicit SDL phase list.** §B.3 names requirements → design → development → testing →
  deployment → maintenance. Add to MAP-0001 as a regulator-stated phase list for the canonical
  `LifecyclePhase` crosswalk.

## Adapt

- **Scope exemptions as predicates.** Free/publicly available proprietary software, freely
  obtained OSS, components, agency- and contractor-developed software. Model as `applies_if`
  predicates on the Requirement mapping (R-044), plus the residual obligation (B.2-4: still assess
  risk) as a separate Requirement — exemptions remove one requirement and add another.
- **Precedence between documents.** "this memorandum is controlling" (intro-2) is a typed
  relation between requirement sets; the library's `updates` relation is the curatorial form, but
  the crosswalk needs a machine-readable `overrides` per requirement (A-2 overrides
  omb-m-22-18#III.A.3) — recorded via `maps_to` here.

## Reject

- Nothing material; the memo is procedural.

## Open questions

1. Model "lead agency" as a role on the shared POA&M (Party role edge) or as a separate
   coordination object? Role edge suffices for tmodel.
2. Should `overrides` be a first-class crosswalk edge kind in MAP-0001 alongside `maps_to`?

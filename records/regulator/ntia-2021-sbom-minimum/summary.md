---
schema: "library-summary/v1"
id: ntia-2021-sbom-minimum
record: ntia-2021-sbom-minimum
type: summary
updated: "2026-11-04"
---

# Duplicate — cite `ntia-sbom-minimum-elements`

**This record is a pointer, not a reference.** It has the same title and the same landing URL as `ntia-sbom-minimum-elements`. The landing page links one PDF, `sbom_minimum_elements_report_0.pdf`. Fetched on 2026-11-01 and again on 2026-11-04, it hashes to `b0fbbe5e…`, the digest that record already holds.

The id `ntia-2021-sbom-minimum` is kept because ids are stable forever: anything that ever cited
it must not silently retarget. **Do not extend this record and do not cite it.**
Cite [`ntia-sbom-minimum-elements`](../ntia-sbom-minimum-elements/) instead — that is
where the metadata, summary and any extraction live. This pointer makes no claim about the
report's standing. For that, see `cisa-2026-sbom-minimum`, which says (Introduction, p. 4) that it
"updates and replaces" the NTIA report and carries the `supersedes` edge to the target record.

`bin/validate` enforces the pointer: `duplicate_of` must name an existing
record, and this record must stay a stub.

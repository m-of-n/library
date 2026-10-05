---
schema: "library-summary/v1"
id: ecma-424
record: ecma-424
type: summary
updated: "2026-10-05"
---

# Duplicate — cite `cyclonedx-1-7`

**This record is a pointer, not a reference.** ECMA-424 2nd edition is CycloneDX 1.7 — the same text under its ratifying body. Per docs/scope.md §4 a re-publication is an `identifiers` entry on one record, not a second record (library#35).

The id `ecma-424` is kept because ids are stable forever: anything that ever cited
it must not silently retarget. **Do not extend this record and do not cite it.**
Cite [`cyclonedx-1-7`](../../community/cyclonedx-1-7/) instead — that is
where the metadata, summary and any extraction live.

`bin/validate` enforces the pointer: `duplicate_of` must name an existing
record, and this record must stay a stub.

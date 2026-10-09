---
schema: "library-distilled/v1"
id: iso-iec-27034-1-schema
record: iso-iec-27034-1
type: schema
updated: "2026-10-02"
---

# ASC data model — the free official XSD (ISO/IEC TS 27034-5-1:2018)

ISO publishes the XML Schema of ISO/IEC TS 27034-5-1 free of charge as an "electronic insert":

- URL: <https://standards.iso.org/iso-iec/ts/27034/5-1/ed-1/en/ISO27034-ASC_Structure_v1.0.0.xsd>
- sha256: `c9068e6d866e15f0711b8cf54ef7b0ab91fb2c9ea6c20da0795dd153fa4b2093` (77 206 bytes, 1 558 lines), retrieved 2026-10-02
- Target namespace in the file: `http://iso.org/ISO27034/ASC-structure` (prefix `asc`), also declares
  `aslcrm` = `http://iso.org/ISO27034ASLCRM`; `version="1.0.0"`; header comment "Edited for
  ISO/IEC 27034 by Luc Poulin and Daniel Sinnig".
- Licence (directory page): use permitted "in their original format without any modifications for
  the purposes specified in their respective ISO standard(s)", under the ISO Customer Licence
  Agreement.

**The XSD is not copied here.** Third-party bytes are never committed to this library, and the
licence allows use, not modified redistribution. Fetch it from the URL and check the digest.

## What is here

| File | What it is |
|---|---|
| `asc-structure.derived.outline.txt` | A **derived**, mechanically generated outline of the XSD: every element and named type, its cardinality, its attributes and every enumeration value. Use it to read the model without the XSD. It is not a schema and cannot validate anything. |

## Source defects and oddities, as observed

1. The TS 27034-5-1 preview (§5.3) says the namespace URI "should be
   `http://standards.iso.org/iso-iec/ts/27034/5-1/ed-1/en`", but the published XSD declares
   `targetNamespace="http://iso.org/ISO27034/ASC-structure"`. The text and the insert disagree.
2. The XML declaration reads `<?xml version="1.81" …?>` (the preview's Table 1 prints the same).
   XML has versions 1.0 and 1.1 only, so a strict parser may reject the file as written.
3. The preview's Table 1 shows `version="1.0RC"`; the published file says `version="1.0.0"`.
4. Misspelled element names are part of the contract: `infomation-item`, `provice-state`,
   `supporting-expert-ressources`, enum `APPLICATION_FUNCTIONNALITY`, activity label
   `DEFINE AND ACQUIRE SELECTED ACSS …`, and `CLOSE PROJECT OF PHASE` (presumably "or phase").
5. TS 27034-5-1 §5.1 reads "identified in ISO 27045-5". That is a typo for ISO/IEC 27034-5.

## Top-level shape (summary of the outline)

- `asc:asc-package` → `package-content` { `package-identification` {uid, date, version-number?,
  name, objective?, description?, editor*}, `asc:asc`+ } , `package-editors-e-signatures`?
- `asc:asc` → `content` { `identification`, `objective`, `security-activity` (type `activity`),
  `verification-measurement` (type `activity`) }, `approval-e-signatures`?
- `activity` → `synopsis`, `activity-complexity`?, `activity-specification`? { `task`+ {description,
  pre-conditions?, required-resources, execution-moments, action-list, outcome,
  task-estimated-effort?, note?} }
- `ASLCRM_activity-name` → choice of 4 layers → Provisioning/Operation stage → activity area →
  sub-area → enumerated activity label (or CUSTOM).

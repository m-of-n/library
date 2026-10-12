---
record: fda-premarket-cybersecurity-guidance
kind: examples-index
title: "fda-premarket-cybersecurity-guidance — examples and fixtures"
extracted: "2026-10-02"
reviewed_by: ""
---

# Examples

The guidance has **no test vectors** (it is a regulatory guidance, not a protocol). It has 22
illustrative examples; every one is captured below as a fixture with the outcome it illustrates,
`source: stated` with a locator. Where a decision rule needed a case the guidance does not give
(a negative cyber-device case), the fixture is marked `source: constructed` and says why.

| file | rule exercised | cases |
|---|---|---|
| `cyber-device-determination.yaml` | 524B(c) three-criteria test as interpreted in §VII.B (fn 57, 60, 61) | 5 stated + 2 constructed |
| `modification-classification.yaml` | §VII.D: may-impact vs unlikely-to-impact changes → full vs abbreviated 524B documentation | 6 stated |
| `documentation-scaling.yaml` | §IV.D, §V.B.2, App. 4, fn 65: documentation scales with cybersecurity risk | 7 stated |
| `antimalware-by-os.yaml` | App. 1 F: anti-malware by OS class | 3 stated |
| `vulnerability-disposition.yaml` | inputs → states of `../state-machine.yaml` `vulnerability-disposition` | 8 stated |
| `other-worked-examples.yaml` | the remaining narrative examples verbatim (NSE alarm, end-to-end update path, bedside monitors, hostile network, least privilege, NFC, mutual auth, BLE underlay, anomaly, shared protocol) | 10 stated |
| `sbom-supplement.constructed.json` | `../schema/sbom-supplement.derived.schema.json` | 1 constructed (validates); a negative variant (non-date end-of-support) is rejected |

**Verify-pass note (2026-10-02).** `text` fields are verbatim (12 checked mechanically, 0 misses).
`input` and `expected` strings are OUR condensations of the source case into fixture form — not
quotations — even where they echo the source wording; the authority is the `locator` (and the
verbatim text in `../normative.md`). The constructed SBOM fixture validates against its derived
schema (jsonschema Draft 2020-12, 0 errors).

Not transcribed: nothing. The guidance's lists (security objectives, control categories, view
types, Table 1) are structure, held in `messages.yaml` and `normative.md`, not examples.

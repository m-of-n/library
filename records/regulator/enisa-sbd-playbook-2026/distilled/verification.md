---
schema: "library-distilled/v1"
id: enisa-sbd-playbook-2026-verification
record: enisa-sbd-playbook-2026
type: verification
updated: "2026-10-03"
---

# Verification — ENISA Secure by Design and Default Playbook v1.0: FX-1 passes 2 (verify) and 3 (cross-check)

By: claude (independent verifier, did not extract). Effort: max. Run 2026-10-02/03.
Every check below was scripted against `.cache/enisa-sbd-playbook-2026.txt` and fresh renderings of the PDF, never
against the summary. The scripts are in the session scratchpad (`verify-f/`): `vb.py`/`vb2.py`, `vnm3.py`,
`en_sent.py`, `en_add.py`, `om.py`, `xc.py`, plus inline playbook-count and Annex C scripts.

## Pass 2 — verify

**Hash and currency.**
- The cached PDF and the lane copy (`sdlscan/enisa_sbd.pdf`) both hash to `c0dc5132…7c15`, matching `content.sha256`.
  80 pages.
- The PDF says "Version: 1.0", "JULY 2026", and that it follows the April–May 2026 consultation, which drew 28
  contributions. PDF CreationDate is 2026-07-30.

**Verbatim.** Contiguous substring checks after normalisation.
- `requirements[].text`: 550/550 pass (511 original and 39 added).
- `normative.md`: 986 lines checked. 7 misses, all editorial (header notes) or Table 3 deliverable cells whose source
  bullets are joined with "; ".
- No splices.

**Completeness: playbooks.** Every bullet (▪ checklist, ▪ minimum evidence, ✓ release gate) was recounted in each of
the 22 playbook sections of the source. The result is 220 / 119 / 125, matching the record **per playbook** (22/22
exact). No sub-bullets are hidden in the playbook tables.

**Completeness: prose. This is the main defect.** Whole-source lower-case counts are should 78 and must 34. A
sentence-by-sentence modal walk of §1–§3, the §4 introduction, §4.23 and §5 found that the extract pass had taken only
28 prose sentences. In particular it omitted **every prescriptive sentence of the §3 principle descriptions**:
- "Systems should ship with the most restrictive permissions possible."
- "Any secrets … must be generated uniquely and protected against extraction."
- "the system must provide a clear, understandable warning …"
- and others.

Added R-0029…R-0067 (39 entries, `kind: inferred`, `added_by` set):

| range | where |
|---|---|
| R-0029 | §1.1 |
| R-0030 | §2.1 |
| R-0031…R-0051 | §3.1.1 and §3.1.2, one locator per principle |
| R-0052…R-0063 | §3.2.1 and §3.2.2 |
| R-0064…R-0066 | §4 introduction |
| R-0067 | §4.23.2, with its 4-item list |

Not added, by decision:
- descriptive uses ("what needs to be protected");
- the permissive "may need to be adapted";
- a citation of another report's "must";
- Table 2/3 cells already held as RM-n/TM-n;
- §5.4 SafeGate-X1 illustrative sentences, which live in examples/.

Counts updated: prose 28 → 67, entries 511 → 550. Updated in requirements.yaml (counts and reconciliation),
record.yaml, README.md and summary.md.

**Annex C → CRA.**
- Independently re-read: 62 ANNEX-1 ids in source order, identical to `principles[].maps_to` in order.
- Per-principle grouping checked against the left column (22/22).
- Support texts are verbatim. One false alarm came from column interleaving at 4.9.

**Figure 5 JSON, checked carefully.**
- The embedded raster was extracted at native resolution (`pdfimages`, 438×229 px, page 68) and read at 3× zoom, not
  from a page render.
- The fixture `examples/safegate-x1-figure5.json` matches it character for character: keys, key order, arrays
  `["T1", "T3"]` and `[443, 22]`, "Removed (sh, curl, wget excluded)", "Distroless-Production", "Nmap-Scan-Gate",
  "PASS", and "sha256:7f8d...a11b" (elided in the source).
- It validates against `schema/attestation-claim.derived.schema.json` (jsonschema).

**Locators.** All 511 original table entries carry playbook and section locators consistent with the per-playbook
recount. The 28 original prose locators and the 39 new ones were placed from the source line and heading by script.

**Typing.**
- All entries are `recommendation` (guidance), which is consistent with the Legal notice and §1.2.
- Lower-case "must" sentences keep verb "must (lower-case)", so no verb was weakened.
- Prose entries are `kind: inferred`, with the reason recorded.

**Object model.**
- 38 objects and 19 edges, all with locators. One edge (`maps_to`) pointed at an undefined endpoint, "CRA essential
  requirement". Added the object `CRAEssentialRequirement` (Annex B/C) and repointed the edge. Now 39 objects; counts
  updated in record.yaml, summary.md, README.md and object-model.md.
- Sampled edges confirmed in the source: informs (§2.2 "Their outputs directly informs"), shared_across (§4
  introduction), invalidated_by (Table 3 row 5).

**Claims.** All supported:
- design-notes items 1–7: MRSM exposed_ports at line 3237; "close all ports except 443" vs 443/22; CI = "configuration
  item" in Annex A; Deleersnyder ×2; 4.8 RG-02 / 4.16 RG-01 overlap;
- the summary's 22 principles in 4 groups, 125 gate criteria, and CC BY 4.0.

## Pass 3 — cross-check

- Every `constrained_by` id in messages.yaml and protocol.yaml resolves (0 dangling).
- Every protocol message is defined in messages.yaml.
- Each of the 10 derived schemas has a message; `attestation-claim` is the hand-derived schema for message
  `AttestationClaim`, and the Figure 5 fixture validates against it.
- **maps_to targets now use the target record's ids.** All 62 Annex C rows carry
  `target_id: eu-cra-2024-2847#AnnexI-PartI(…)` or `…AnnexI-PartII(n)`, and all resolve.
- `not_applicable: []` is correct.

## Residual open issues

- State-machine triggers are prose. The order of support life-cycle states is inferred and already flagged by the
  extractor.
- Figure 4 is not transcribable; this was stated by the extractor and confirmed (raster).
- Derived fields need human review.

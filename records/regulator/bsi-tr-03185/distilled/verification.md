---
schema: "library-distilled/v1"
id: bsi-tr-03185-verification
record: bsi-tr-03185
type: verification
updated: "2026-10-02"
---

# Verification — BSI TR-03185 v1.1.1: FX-1 passes 2 (verify) and 3 (cross-check)

By: claude (independent verifier, did not extract). Effort: max. Date: 2026-10-02.
The checks were scripted against `pdftotext -raw` and `-layout` of the cached PDF. The scripts are in the
session scratchpad: `vcheck.py`, `ncheck.py`, `loccheck.py`, `omcheck.py`, `xcheck.py`.

## Pass 2 — verify

**Hash and currency.**
- The cached PDF matches `content.sha256` (`199c8775…8329`).
- `content.url` (`&v=5`) was re-fetched on 2026-10-02 and is byte-identical.
- The short URL https://www.bsi.bund.de/dok/TR-03185-en still links that blob.
- Document history (p.2): 1.1.1 is dated 2026-07-02 and merges TR-03185(-1) v1.0 (2024-09-06) with
  TR-03185-2 v1.1.0 (2025-08-18).
- `pdfinfo` gives CreationDate 2026-08-20. The PDF has 51 pages.
- The German Part 1 v1.0 PDF hashes to `5f507a35…72ddb0`, as the summary states.

**Verbatim.**
- 191 `text` fields were checked: 0 real misses. No spliced quotes: multi-sentence cells are the TR's own
  rows.
  - The `-layout` text interleaves table columns, so the check used `-raw` text.
  - 9 fields needed gap tolerance; every gap is a running head, a table header or a footnote at a page
    break.
- `normative.md` blockquotes: 29 segments. The three misses are benign: a "§1.3.2" prefix, an omitted URL
  list inside a quoted bullet list, and a "— Table 24 lead-in" annotation.

**Locators.** 32 were sampled; the containing table was recomputed from the capture: 32/32 correct.
PROD.TEST.A.9 and A.14 have text identical to USER rows and were resolved by table order.

**Completeness.**
- Every requirement id in the PDF tables was extracted: 187 table ids, 0 missing. With R-0001 and R-0002,
  the 191 entries are USER 68, PROD 101, and GV/LE/QA/BR/VM/DE 20.
- Keyword reconciliation was recomputed per keyword. Source: MUST 176, SHOULD 157, MAY 12, MUST NOT 4,
  SHOULD NOT 3. Extracted texts: 172 / 152 / 10 / 2 / 2.
- The difference (4/5/2/2/1 = 14) is exactly the §1.2.2 and §2.2.1 definition passages, as the header
  claims. Reconciled.

**Typing.**
- Normativity is the strongest verb in each cell; none is weakened.
- 7 `kind: inferred` entries (R-0001/R-0002 and the lower-case-modal items) are honestly flagged.

**Object model.**
- 67 objects and 45 edges; all have locators.
- One edge (`forks`) uses qualified endpoint labels "OSSProject (downstream/upstream)". Both resolve to the
  `OSSProject` object. Cosmetic.

**Claims in summary.md.** Checked against the PDF:
- the version and dates;
- the merge of the two parts;
- Part 1 = 169 requirements and Part 2 = 20 (counted from the extraction);
- 51 pages.
- The German landing-page quotation was not re-opened (the EN landing page was).

## Pass 3 — cross-check

- Every requirement id referenced by messages, protocol and state-machine exists. Abbreviated sibling refs
  such as "PROD.FIX.A.8, A.13" resolve.
- **Defect: 19 messages named in `protocol.yaml` flows were not defined in `messages.yaml`.**
  - Examples: `investigation-record`, `it-security-update`, `discontinuation-notice`, `release-log`.
  - **Fixed:** an `exchanges:` section now defines each one with from/to roles, flows and
    `constrained_by`, and `fields: []`. The TR gives no field content beyond the cited requirement text, so
    none was invented.
- State-machine triggers are named events (`investigation-positive`, `remedy-selected`, …). They are now
  catalogued in `state-machine.yaml` `events:` (23 events) with locators.
- The derived JSON Schemas in `schema/` parse.
- `maps_to` uses BSI's own wording ("DIN EN IEC 62443-4-1, Chapter 5 (SM)", "NIST SP 800-218, Chapter PW",
  IT-Grundschutz module ids). Editions are as BSI states them in §2.3 (SSDF February 2022, SLSA 1.1) or in
  the Prüfspezifikation `standard` field.

## Residual open issues

- The Prüfspezifikation mapping was written against German Part 1 v1.0, not EN v1.1.1. The id alignment
  rests on unchanged ids, which pass 1 checked; this was not re-verified cell by cell here.
- The German landing-page quotation in summary.md was not re-opened in this pass.

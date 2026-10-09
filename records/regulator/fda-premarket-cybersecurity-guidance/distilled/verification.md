---
schema: "library-distilled/v1"
id: fda-premarket-cybersecurity-guidance-verification
record: fda-premarket-cybersecurity-guidance
type: verification
updated: "2026-10-02"
---

# Verification — FDA, Cybersecurity in Medical Devices (premarket guidance, 3 Feb 2026): passes 2 and 3

By: claude (independent verifier, did not extract). Effort: max. Date: 2026-10-02.
The checks were scripted against `pdftotext -raw` of the cached PDF and the capture. The scripts are in the
session scratchpad: `vcheck.py`, `ncheck.py`, `loccheck.py`, `omcheck.py`, `xcheck.py`.

## Pass 2 — verify

**Hash and currency.**
- The cached PDF matches `content.sha256` (`d046fa83…6c54`).
- `https://www.fda.gov/media/119933/download` was re-fetched on 2026-10-02 and is byte-identical.
- The cover reads "Document issued on February 3, 2026" and says it supersedes the 27 June 2025 version.
- The Guidance History table on p.60 was read. Its rows are: Feb 2026 Level 2 revisions; June 2025 Level 1
  final; March 2024 Level 1 draft; and a reference to the September 2023 final.
- 64 pages.
- Industry coverage (DLA Piper, Feb 2026) reports no later edition.

**Verbatim.**
- 426 `text` fields were checked: 0 real misses.
  - 25 needed gap tolerance. All were reviewed: the gaps are footnote call numbers, footnote bodies and
    running heads at page breaks, which the header says are removed.
  - No splices.
- `normative.md`: 148 segments. The only misses were the four framing sentences of its own introduction.
- Example fixtures: 12 `text` fields are verbatim (0 misses).
- `input` and `expected` strings are OUR condensations. The examples README now says so explicitly.

**Locators.** 32 were sampled (sections, bullets, App. 1 subsections, footnotes) with the containing
heading recomputed: 32/32 correct.

**Completeness.** Recount on the raw PDF text:
- should 175 = 164 extracted + 10 excluded + 1 App. 5;
- must 19 = 16 + 1 + 2;
- shall 6 = 5 + 1.
- These match the header reconciliation exactly. `bin/bcp14-count` = 0.

**Typing.**
- No should/must was weakened in `verb`.
- V.A.4-05 ("must be accounted for") and App1.E-02 ("is required") are typed `recommendation` with the verb
  kept. This is consistent with the record's stated rule (requirement only where a statute or regulation is
  restated; FDA Section I) and is left as is.
- `counts.by_phase` uses the key `operations-response`, while the entries use the canonical
  `operations/response`. This is cosmetic and left as is.

**Object model.**
- 46 objects and 42 edges; every one has a locator.
- 2 inferred, flagged.
- Mappings name ARCH-0001 / DL-0009 classes.

**Claims in summary.md.** Checked against the PDF:
- the dates;
- that the QMSR incorporates ISO 13485:2016;
- that the final rule took effect on 2 February 2026 (fn 12);
- the 64 pages;
- the docket and GUI numbers.

## Pass 3 — cross-check

- Every requirement id cited in `messages.yaml`, `state-machine.yaml` and the schemas exists.
- All four derived JSON Schemas are valid Draft 2020-12. The constructed SBOM fixture validates against its
  schema with 0 errors.
- `maps_to`: FDA names "ANSI/ISA 62443-4-1", but the extraction wrote "ISA/IEC 62443-4-1".
  - **Fixed** in 10 entries: they now give FDA's naming, note that FDA states no edition, and point to the
    library record.
  - Other targets (FD&C Act §524B paragraphs, ISO 13485:2016 clauses, NTIA 2021) use the source's own ids.
- State-machine triggers are free-text events, not messages.
  - They are now catalogued in `state-machine.yaml` `events:` (14 events).
  - 13 guard-only transitions in `vulnerability-disposition` and `device-support-lifecycle` have an empty
    trigger. They are listed under `empty_triggers` and left for human review rather than invented.
- The not_applicable reason for protocol ("no exchange between parties; CVD flows are in the 2016
  postmarket guidance") is true for this document.

## Residual open issues

- The 13 transitions without a trigger (guard-only) need a named event or an explicit `automatic` marker.
- `expected` values in the fixtures are condensations. A reviewer should confirm each one reflects the cited
  passage.

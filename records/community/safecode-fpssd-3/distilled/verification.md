---
record: safecode-fpssd-3
kind: verification
title: "safecode-fpssd-3 — verify and cross-check passes (FX-1 passes 2 and 3)"
date: "2026-10-03"
by: "claude (independent verifier; did not extract)"
reviewed_by: ""
---

# SAFECode FPSSD 3rd edition: verification report

## Sources and method

The source is `.cache/safecode-fpssd-3.pdf`: sha256 `9a9a07b5…33ae` = `content.sha256`, 38 pp., produced by Word 2016 on 2018-04-16.

I made my own renderings with `pdftotext -raw`, plain and `-layout`. I did not use the extractor's `pdftohtml -xml` capture. The checking scripts are:

- `gen_verify.py` and `split_check.py`: substring checks, with tolerance for page breaks;
- `gap_check.py`: content of every gap between matched pieces; it detects reorderings as NOFOLLOW;
- `splice_check.py`;
- `norm_check.py` and `quote_check.py`;
- a sentence-level modal walk over the whole PDF.

## Pass 2: verify

1. **Hash and currency.**
   - The hash matches. ✔
   - The title page reads "Third Edition / March 2018".
   - A web search on 2026-10-03 found no 4th edition. The safecode.org resource page and press release still present the March 2018 third edition. ✔
   - Licence: every page footer reads "© 2018 SAFECode – All Rights Reserved.", and no open licence is stated. **Confirmed.** ✔
2. **Verbatim (198/198).**
   - All texts are present.
   - Every gap between matched pieces is page furniture or a footnote marker ("1", "2", "3"), except for the defects below.
3. **Locators (198/198).**
   - All 146 statement texts lie inside their parent practice's text, with the same locator.
   - All 52 practice headings occur immediately before their body text in the source.
4. **Completeness.**
   - Every modal sentence in the eight practice chapters (must/should/shall/required/recommended/never/need to/"it is (critically) important|essential") is a statement entry. This was checked by locating each sentence's modal clause.
   - The front matter, which the extract pass scoped out, carries 3 programme-level must/required statements. These were added.
   - `bin/bcp14-count` = 0.
   - Case-insensitive baseline: must 29, should 104, may 40, recommended 4. This matches the header.
   - CWE references:
     - 13 in the source = 13 `maps_to`;
     - the source prints "CWE 388" and "CWE 544" without a hyphen, and the record normalises them to CWE-388/544, which is correct.
5. **Typing.** R-0125 ("… more detailed technical training must be provided to development teams") was typed `recommendation`/`should`. That breaks the record's own rule that must-sentences are typed `requirement`.
6. **Object model, state machine and protocol.**
   - 12 state-machine, 13 protocol, 8 object-model and 3 example quotes are verbatim.
   - The finding statuses (remediated / mitigated / risk-accepted) quote "action taken to remediate, mitigate or accept the respective risk".
7. **Claims.**
   - The severity scales in the schema are both those the source gives ("Critical, High, Medium and Low or a finer grained scale, Very High, High, Medium, Low, Very Low, Informational").
   - CVSS bands: only two are given ("10-8.5 = Critical, 8.4-7.0 = High, etc."), and the fixture says so.
   - Approver example (Critical → VP of Business Unit, Medium → Engineering Manager) ✔.
   - TSRV ✔.

### Defects found and fixed

| # | cat. | defect | fix |
|---|---|---|---|
| 1 | verbatim (splice) | A page footnote ("SSLlabs maintains a list of SSL/TLS assessment tools") had been inserted **mid-sentence** in the Develop an Encryption Strategy text ("provide protection against ⟨footnote⟩ offline attack"). Two other practice texts also carried an inline footnote. | footnotes removed from the 3 `text` values and kept in a new `footnotes` list; the sentence rejoined; `normative.md` repaired, with the footnote placed after its paragraph |
| 2 | verbatim (word order) | The pdftohtml capture moved hyperlinked words out of place in 4 bullets: "– Vulnerability disclosure … Provides a guideline on ISO/IEC 29147 receiving …", "… Gives guidance ISO/IEC 30111 on how …", "– Secure Coding Practices, Quick Reference Guide OWASP" and "— Bounds Checking Interfaces Updated Field Experience with Annex K" | restored to the source order ("ISO/IEC 29147 – Vulnerability disclosure …", "OWASP – Secure Coding Practices …", "Updated Field Experience with Annex K — Bounds Checking Interfaces") in `requirements.yaml` and `normative.md` |
| 3 | dropped | 3 front-matter must/required statements were missing | appended as R-0144..R-0146 with `added_by`; new `normative.md` section; counts updated to 198 entries (34 requirement, 112 recommendation, 52 practice) |
| 4 | typing | R-0125 weakened | retyped to `requirement`/`must`, with a `verification_note` |

## Pass 3: cross-check

- **Requirements ↔ schema.**
  - SecurityFinding status and source-practice enums trace to stated text.
  - ApplicationSecurityControl status follows the five-step workflow (identify, communicate, implement, validate, audit) of "Actively Manage Application Security Controls". This status is marked inferred.
  - RiskAcceptance carries the TSRV fields.
- **Protocol ↔ state machine.** Report intake → acknowledgement → triage → fix → advisory. The protocol messages match the reported-vulnerability lifecycle transitions, and each quotes the "Vulnerability Response and Disclosure" sections.
- **`maps_to`.** CWE ids are named per the source. CWE is unversioned in the source, so no edition can be given.
- **not_applicable.** Messages are N/A; the reason is true.

## Residual open issues

- SAFECode publishes no crosswalk to SSDF, SAMM or BSIMM. Only CWE links exist.
- List nesting in `normative.md` is approximate ("- " vs "  - "), but the wording is verbatim.

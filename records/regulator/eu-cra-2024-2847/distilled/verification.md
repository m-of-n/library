---
schema: "library-distilled/v1"
id: eu-cra-2024-2847-verification
record: eu-cra-2024-2847
type: verification
updated: "2026-10-02"
---

# Verification — Regulation (EU) 2024/2847 (CRA): FX-1 passes 2 (verify) and 3 (cross-check)

By: claude (independent verifier, did not extract). Effort: max. Date: 2026-10-02.
The checks were scripted and run against the SOURCE, never the summary. The scripts are in the session
scratchpad: `vcheck.py`, `ncheck.py`, `loccheck.py`, `omcheck.py`, `xcheck.py`.

## Pass 2 — verify

**Hash and currency.**
- `.cache/eu-cra-2024-2847.pdf` hashes to `e3ecaabd…1b0a`, matching `content.sha256`.
- The record's version line was checked against the Publications Office SPARQL endpoint (EUR-Lex itself
  answers automated requests with a WAF challenge). Results:
  - Only one consolidated version exists (02024R2847-20241120).
  - There are three English corrigenda: R(01), R(02) and R(04). The R(02) text was opened; it says
    "paragraphs 2 to 9", as applied.
  - R(03), R(05), R(06) and R(07) are FR/HU, SK, FR and DE only. Their languages were verified.
  - The amendment by Reg (EU) 2025/327 is still pending.
- **Two items were missing from the summary and are now added:**
  - Commission proposal COM(2026) 590 (CELEX 52026PC0590, 9.9.2026), the Public Procurement Act, which
    proposes to amend 2024/2847;
  - the title of Delegated Reg (EU) 2025/1535 (exclusion of vehicles under Reg 168/2013).
- Delegated Reg 2026/881 was opened and its Art 3(a)-(d), 4 and 5 checked against `protocol.yaml`.
  Its OJ date is 20.4.2026, which is correct.

**Verbatim.**
- `requirements.yaml`: 247 `text` and `chapeau` fields in 191 entries were checked against the PDF text
  and the HTML capture, with whitespace, hyphenation and punctuation normalised.
  - 0 real misses.
  - One page-break gap (Art14(7)-5) was confirmed as a running head.
  - Art64(10) differs from the OJ by design: the corrigendum text was verified against R(02).
  - No spliced quotes.
- `normative.md`: 97 paragraph and quote segments were checked. Every miss was editorial framing:
  coverage notes, the EHDS bracket notes and the DR 2026/881 summary, which is labelled as a summary.

**Locators.** 35 were sampled with the containing paragraph/point recomputed from the source.
- 35/35 correct.
- Annex I Part II points (1)-(8) and Annex II/VII points were checked by hand.

**Completeness.** The modal baseline was recounted per in-scope provision (`shall not` matched before
`shall`; .md capture).
- Art 13: 52/1/9; Art 14: 23/0/4; Art 15: 3/1/3; Art 16: 10/1/3; Art 17: 5/1/3; Arts 24 and 31: 7 each;
  Art 64(2)-(4),(10): 3/1; Art 69: 4; Art 71: 5; Annex I: 4/0/1; Annex II: 1/0/1; Annex VII: 2.
- Total shall 126, shall not 5, may 24. This equals the header. The two "may" found after Art 71 are the
  month name in footnotes.
- Nothing was dropped.
- `bin/bcp14-count` = 0, as recorded.

**Typing.**
- No shall was typed as anything weaker.
- `Art16(2)-5` ("are to be") is a requirement, which is right.
- `applies_from` was checked for every entry against Art 71(2) and Art 69(3). One defect: Art71(2)-2 sets
  two dates (Art 14 from 2026-09-11; Chapter IV from 2026-06-11), but only one was recorded. A note now
  carries both.

**Art 14 clocks** were checked word by word against Art 14(2), (4) and (6):
- 24 h and 72 h run from awareness.
- The AEV final report is due 14 days after a corrective or mitigating measure is available.
- The incident final report is due one month after the (b) notification is submitted.
- "Unless already provided" shortcuts apply.
- `protocol.yaml`, `state-machine.yaml`, `messages.yaml` and the derived schema all match.

Defects found and fixed:
1. `deadline-breached` was a sink. It now notes that the duty to submit persists after the deadline.
2. A **penalty-timing gap** was not recorded. Art 64 is not brought forward by Art 71(2), so CRA fines apply
   only from 2027-12-11 even though Art 14 binds from 2026-09-11. This is now noted in SM1, `protocol.yaml`
   error path E4 and design-notes Q9.
3. SM2 lacked the combined early-warning-plus-notification shortcut that SM1 has. It is added as `inferred`.

**Object model.**
- All 51 objects and 34 edges have locators. Inferred items are flagged (2 objects, 2 edges). Mappings name
  real ARCH-0001 / DL-0009 classes.
- Ten locators were spot-checked (ADCO, Art 13(8) fourth subparagraph, and others). All are correct.
- **Three stated edges were missing and are added:**
  - `submits` (Manufacturer → Notification, Art 14(1),(3));
  - `reports_vulnerability_to` (Manufacturer → ComponentMaintainer, Art 13(6));
  - `has_intended_purpose` (Art 3(23), 13(3)).
- The model now has 51 objects and 37 edges.

**Claims in summary.md and design-notes.md.**
- Verified: entry into force on 10 Dec 2024; application dates; corrigenda; recitals silent on the awareness
  clock (grep of recitals); the Art 16(2) cross-reference defect; M/606 acceptance on 3 April 2025
  (CEN-CENELEC page); C(2025) 618 dated 3.2.2025 (EC register PDF).
- "ENISA opened the SRP on 2026-09-11" was confirmed on the ENISA SRP page (press release of 11 September
  2026); the source is now cited.
- **Not verified:** "41 standards" (the annex was not in the PDF fetched), the July 2026 deadline-change
  draft, and the EN 40000 status. These rest on secondary or CEN sources and are left as stated.

## Pass 3 — cross-check

- Every requirement id cited in `messages.yaml`, `protocol.yaml` and `state-machine.yaml` exists (paren-aware
  matching).
- Every protocol flow message is defined in `messages.yaml`.
- Every `send <message>` trigger is a defined message. The other triggers (awareness events, timers,
  classification decisions) are now catalogued with their locators in `state-machine.yaml` `events:`
  (26 events).
- The derived JSON Schema is valid Draft 2020-12.
- No `maps_to`: the Regulation publishes no mapping, and that is true. The not_applicable reason for
  examples is also true: the enacting terms have no examples.

## Residual open issues

- `Art71-binding` keeps `applies_from: 2027-12-11`. "Binding in its entirety" arguably runs from entry into
  force. This is left for human review.
- Arts 1-12, 18-23, 25-30, 32-63 and the recitals are not extracted. This is declared scope, not a defect.
- The harmonised-standards paragraph rests partly on secondary trackers.

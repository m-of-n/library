---
schema: "library-summary/v1"
id: rfc-8259
record: rfc-8259
type: summary
updated: "2026-11-01"
---

# The JavaScript Object Notation (JSON) Data Interchange Format

|  |  |
|---|---|
| **Type** | rfc |
| **Maturity** | `standard`: Internet Standard, STD 90, confirmed in `rfc8259.json` 2026-11-01 |
| **Authors** | T. Bray, Ed. |
| **Published** | 2017-12 |
| **Identifier** | RFC 8259 · DOI 10.17487/RFC8259 · STD 90 |
| **Source** | https://www.rfc-editor.org/rfc/rfc8259.txt |
| **Digest** | `sha256:61a5378f…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

RFC 8259 defines JSON as a small, text-based, language-independent format, and its main job in this revision is to warn about what the grammar permits but practice cannot rely on (§1.3). Its characteristic phrase is 'interoperable in the sense that': unique names, integers within double range, and Unicode-only strings each get defined agreement, and everything outside them is unpredictable (§4, §6, §8.2). It adds a hard rule for open systems, UTF-8 (§8.1). A parser must accept all conforming texts and may accept more, and it may set limits on size, depth, numbers and strings (§9).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | Its unspecified cases are parser-differential risk (§4, §6, §8.2). §12 covers only `eval()` |
| Cryptography | `none` | No cryptographic content |
| This project | `adjacent` | DEC-002, closed: the base of rejected option 3 |

- **DEC-002** (accepted 2026-10-25, ADR-0004, option 5): JSON + JCS was option 3. This RFC shows why JSON alone cannot be signed by value. Names need only be unique by SHOULD (§4), member order may or may not be visible (§4), and numeric precision is left to implementations (§6, §9). `rfc-8785` is the canonicalisation that option needed. The decision is closed, so this is background to it, not an open input.
- **vCon and JOSE** both rest on it. `rfc-7515` §10.12 tightens §4's SHOULD on unique names, and it had to, because §4 leaves duplicates unpredictable. `draft-ietf-vcon-vcon-core-04` §2.2 cites §6 for floats and uses JMAP's notation for the rest.

## Implementations

**Searched 2026-11-01.** Only the one project below was checked. This was not a survey. JSON parsers are too many to list, so the row is a conformance tool.

| Name | Kind | License | URL |
|---|---|---|---|
| JSONTestSuite | open source, test suite | MIT | https://github.com/nst/JSONTestSuite |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar. A `rfc` record owes FX-1 when someone extracts it, and no issue owns that for this record yet: the 2026-10-25 decision on #45 moved extraction to per-set issues, and neither #69 nor #89 covers it. No keyword count is given because none has been reconciled.

## Limits

- **No canonical form.** It defines no byte-stable rendering. That is `rfc-8785`'s scope.
- **The grammar admits non-Unicode strings** (§8.2), such as an unpaired surrogate. A parser's result for those is unpredictable.
- **§12 is narrow.** It covers `eval()` only, and says nothing on duplicate-name or number parser differentials, though §4 and §6 create them.
- **ECMA-404 is a parallel definition** (§1.2). It was not read. §1.2 says ECMA-404 allows practices this RFC recommends avoiding.
- **Errata.** `errata.json` retrieved 2026-11-01 lists 5 verified, 2 held, 1 reported and 8 rejected. Their text was not reviewed.
- **Read scope.** Whole document to §12, and Appendix A, from the RFC Editor `.txt`. Most of §11, §13 and §14 were not read.

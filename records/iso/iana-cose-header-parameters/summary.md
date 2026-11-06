---
schema: "library-summary/v1"
id: iana-cose-header-parameters
record: iana-cose-header-parameters
type: summary
updated: "2026-11-06"
---

# IANA COSE Header Parameters registry

|  |  |
|---|---|
| **Type** | dataset — a living registry |
| **Maturity** | _unset_ — a living allocation table has no RFC 2026 standing |
| **Publisher** | IANA |
| **Snapshot** | **2026-11-06**, registry last updated 2026-08-25 (45 assigned labels) |
| **Identifier** | https://www.iana.org/assignments/cose/cose.xhtml#header-parameters |
| **Source** | https://www.iana.org/assignments/cose/header-parameters.csv |
| **Digest** | `sha256:105b28c993100860695727089d8bc02765c16d6c1e21b131f6078a8858bbc1f8` |

## Overview

The registry that allocates **COSE header labels**: the map keys of the
protected and unprotected headers of every COSE message. Each entry fixes a
label, a value type and, where the value is itself a code, the registry the
value comes from. mofn's lane-a COSE_Sign1 (mofn#13, DL-0012) used three:
**1 `alg`** (value from `iana-cose-algorithms`), **3 `content type`** (value
from `iana-coap-content-formats` or a media type), and **4 `kid`** (`bstr`, no
value registry). **2 `crit`** is the label that would make an unknown label
fatal. Lane-a did not try it.

Allocation cost rises as the encoding gets shorter. These are the ranges in the
snapshot's registry XML:

| Label range | Policy |
|---|---|
| integers < −65536 | **Private Use** |
| −65536 … −1 | delegated to the COSE Header Algorithm Parameters registry, where each label is listed per algorithm |
| 1 … 255; strings of length 1 | Standards Action with Expert Review |
| 256 … 65535; strings of length 2 | Specification Required |
| > 65535; strings longer than 2 | Expert Review |

The only range with no review at all is Private Use. RFC 9052 §11.6 reserves
it for "testing purposes and closed environments" (see
`rfc-9052/distilled/normative.md`).

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | A verifier acts on these labels: `alg` picks the algorithm, and `crit` decides what may be ignored |
| Cryptography | `adjacent` | An allocation table, not a specification |
| This project | `core` | Every header key of an exported COSE_Sign1 (R-I-03, DEC-005) has to come from here |

Bears on **R-M-12**, **R-I-03** and **DEC-005**. In lane-a, every label or
value the reader acts on broke when made key-relative:
- label 1 moved: pycose found no algorithm;
- the `alg` value −8 replaced: pycose refused it as "Unknown COSE attribute";
- the `content type` value replaced: pycose refused it with "CONTENT TYPE
  should be an unsigned integer or string", which is this table's `tstr / uint`
  value type.

Labels 3 and 4 made key-relative were kept but not understood, with no error.
This is the evidence behind ADR-0004's "COSE/DSSE for export only".

## Implementations

Not applicable — a registry, not software. Searched GitHub code for
`header-parameters.csv` on **2026-11-06**:

| Name | Kind | License | URL |
|---|---|---|---|
| transmute-industries/cose | COSE library that reads the CSV | Apache-2.0 | https://github.com/transmute-industries/cose |

The COSE library lane-a used (pycose 1.1.0) does not read the registry. It has
its own fixed set of labels and keeps any other label as an opaque key, which
is why the label 3 and 4 swaps passed.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, with the snapshot digest |
| `summary.md` | this document |

**No committed copy of the registry.** `library/CLAUDE.md` forbids committing
third-party documents. The CSV is cached in `.cache/`, which is gitignored.
**No `distilled/`:** a `dataset` is outside FX-1. The normative rules for these
labels are in `rfc-9052`, which is extracted at `profile: full`.

## Limits

- **A key-relative pair is not a COSE label at all.** RFC 9052 §1.5 allows
  only `int / tstr`, so a `(defining key, label)` array is an error, not an
  unregistered label. `rfc-9052/distilled/design-notes.md` makes the same
  point. Lane-a's "verifies" rows for labels 3 and 4 show that pycose is
  lenient, not that COSE allows the form.
- **Private Use is unscoped.** Two parties that both pick −70000 collide, and a
  reader has no way to tell. `crit` would turn misunderstanding into
  rejection, but it lists labels (`[+ label]`) and does not scope them. Lane-a
  did not test `crit`. That belongs to DEC-005 (DL-0012 review, item 10).
- **Allocations can expire.** Four entries are TEMPORARY early assignments for
  the SD-CWT draft (17, 170, 171, 172), and all expire 2027-01-16. Two (7, 9)
  are deprecated by RFC 9338 and still listed. Being in the registry is not
  being permanent or recommended.
- **The negative range is the one scoped namespace COSE has.** A label in
  −65536…−1 means something only together with a registered algorithm. The
  scope is a registered algorithm, though, not a key, so it is not R-M-12's
  form.
- **A snapshot, not a fixed work.** The digest dates this record. Check the
  registry again before citing a count.

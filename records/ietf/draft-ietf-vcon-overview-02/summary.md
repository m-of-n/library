---
schema: "library-summary/v1"
id: draft-ietf-vcon-overview-02
record: draft-ietf-vcon-overview-02
type: summary
updated: "2026-11-04"
---

# The vCon - Conversation Data Container - Overview

|  |  |
|---|---|
| **Type** | draft |
| **Maturity** | `draft`: Internet-Draft, Intended status Informational, expires 3 April 2027 |
| **Authors** | T. McCarthy-Howe |
| **Published** | 2026-09-30 |
| **Identifier** | draft-ietf-vcon-overview-02 |
| **Source** | https://www.ietf.org/archive/id/draft-ietf-vcon-overview-02.txt |
| **Digest** | `sha256:1d3a8e33…` (full value in `record.yaml`), fetched 2026-11-01, rechecked 2026-11-04 |

## Overview

This Informational draft explains what a vCon is and why it exists: one container for a conversation's parties, dialog, analysis and attachments, in signed, encrypted or unsigned form (§1.1, §4). Its requirements include that a vCon be immutable, hide PII and be amendable (§1.4). It reconciles those through amendment: a signed vCon is never changed, and a new version deep-copies it, refers to it by UUID, and is signed in turn, so that a chain of signatures carries the history across security domains (§3.8.1, §3.8.2). It defers formats and mechanics to the core draft.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | Sets the signed, encrypted and amendment lifecycle, without defining it |
| Cryptography | `adjacent` | All cryptography is by reference to JWS and JWE |
| This project | `adjacent` | R-M-12: registry-named critical extensions. The rest is context for `draft-ietf-vcon-vcon-core-04` |

- **R-M-12** (accepted by `ADR-0001`, now `ARCH-0002` P1): §3.7 says each extension must define a unique token value registered with IANA, and that incompatible ones are listed in a `critical` parameter, an unsupported one of which an implementation must reject. These are lowercase "must"s in an Informational draft with no BCP 14 boilerplate, so they state the design, not conformance requirements. So vCon's extensions are registry-named, the opposite of R-M-12's native model. The critical half matches the opt-in form `rfc-7515` §4.1.11 uses. This record previously held no `bears_on`, pending a reading. The reading added this edge and no other.
- **DEC-005 and R-M-11 are not added.** An overview settles neither, as the stub expected.

Three points matter to the `artifact-statements` topic:

1. **The chain has a gap.** §1.4.1 puts validation of redactions or amended data beyond the signature of the domain making the changes out of scope. So each link vouches only for what its own signer assembled, and §3.8 says nothing on whether a signer re-checks the prior signature.
2. **"Guarantee" needs a narrow reading.** §3.6 says systems can guarantee a redaction's accuracy, while §1.4.1 leaves validation beyond the domain's own signature out of scope. They fit only if the guarantee is a signer's assertion, which is how core §4.1.8's wording reads.
3. **Analysis provenance is a vendor name.** §3.5 says each analysis entry identifies its provenance through a required `vendor` parameter. This confirms the finding on the core record: the slot names who produced the output, and nobody asserts it.

## Relations

- `part_of: ietf-vcon-wg`: a working-group draft of that group.
- `see_also: draft-ietf-vcon-vcon-core-04`: the core draft this overview defers to for formats and mechanics. The edge is authored only here.

## Implementations

**Not separately searched.** Implementations of vCon are on `draft-ietf-vcon-vcon-core-04` (2026-10-14). An overview has none of its own.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar. A `draft` record owes FX-1 when someone extracts it, and no issue owns that for this record yet: the 2026-10-25 decision on #45 moved extraction to per-set issues, and neither #69 nor #89 covers it. No keyword count is given because none has been reconciled.

## Limits

- **It is not normative.** Intended status is Informational, and it has no IANA considerations (§5). Where it disagrees with the core draft, the core decides.
- **Its security section is three bullets** (§4), which describe forms and give no threat analysis.
- **One author and one draft.** Where it speaks for the WG's consensus is not established.
- **It was checked against core -04.** Datatracker shows core at -05 (2026-10-31, rechecked 2026-11-04), which was not compared.
- **Read scope.** §1.1, §1.4, the out-of-scope list in §1.4.1, the start of §3.5, §3.6, §3.7, the start of §3.8, §3.8.1, §3.8.2, §4 and §5, from the IETF archive `.txt`, plus a keyword search for sign, encrypt and redact across the whole document. §1.2, §1.3 (use cases), §2, §3.1 to §3.4 and the rest of §3.5 were not read in full.

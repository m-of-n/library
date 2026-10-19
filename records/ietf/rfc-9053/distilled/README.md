---
record: rfc-9053
kind: index
title: "rfc-9053 — distilled artifacts"
extracted: "2026-10-19"
reviewed_by: ""
---

# Distilled artifacts

FX-1 (`docs/extraction.md`). One line per artifact: what it covers, and what
it does not.

**State: pass 1 of 3 complete.** Two agents in parallel at effort max, each
reading only `.cache/rfc-9053.txt`. **The verify and cross-check passes have
NOT run**, so this record carries no `profile`. Readable; nothing may be built
on it. library#39 owns finishing it.

Source: RFC 9053, *CBOR Object Signing and Encryption (COSE): Initial
Algorithms*, August 2022. **Informational**, obsoletes RFC 8152, while its
companion RFC 9052 is **STD 96**.

| kind | file | coverage |
|---|---|---|
| normative | `normative.md` | 323 verbatim statements and 31 fenced blocks, §1–§11 in source order, **all 23 tables reproduced in full** (checked present by caption) plus 8 further fences. Boilerplate, the changes-from-8152 history, Acknowledgments and Author's Address dropped |
| requirements | `requirements.yaml` | 222 entries, `R-0001`–`R-0222`, source order, no gaps: **101 stated, 121 inferred**. `source_keyword_count` and `extracted_keyword_count` both 101, `reconciliation` empty because there is nothing to reconcile — every one of the 101 source occurrences was mapped to exactly one stated entry **by raw byte offset: 101 covered, 0 missed, 0 double-counted**, with a per-section tally that sums to 101 |
| schema | `schema/` | **1 verbatim, 4 derived.** `kdf-context.cddl` is §5.2's `PartyInfo`/`COSE_KDF_Context` fragment, byte-exact at source lines 1168–1184 including the three-space margin (verified by `diff`). The derived four cover all 43 algorithm code points, the key structures per key type, the nine algorithm-specific header parameters, and the §8 capability arrays. No JSON Schema: every structure is a CBOR array or a negative-integer-labelled map, so a JSON projection would be invented |
| messages | `messages.yaml` | 56 structures, 300 fields — 12 non-algorithm structures plus **all 43 algorithm code points with no gaps** plus the 4-entry HKDF family. `constrained_by` omitted throughout (the ids belong to a concurrently written file); locators are exact and are the join key for pass 3 |
| examples | `examples/` | **6 vectors — and that is the finding.** See below |
| protocol | — | `not_applicable`; see `record.yaml` |
| state machine | `state-machine.yaml` | **two machines, and this is the only Tier 1 record where this artifact is not N/A.** A key-usage lifecycle (counter-driven ceilings into rekey) and a key-trust promotion. Both are explicitly marked `derived: true` — RFC 9053 names no state as a state |

## The document prints no cryptographic test vectors

Not one key, signature, MAC, ciphertext, nonce, derived key, `COSE_Key` or
`COSE_KDF_Context` — for any of **43 algorithm code points**. The only bytes it
prints anywhere are five bytes of §8 capability encoding (`0x8102`,
`0x820201`, `0x8101820104`), §9's `0x01`/`0x1801` pair, and §11's `"YES"`/`"NO "`
illustration. §1.5 points instead at `github.com/cose-wg/Examples` **commit
3221310, 3 June 2020** — informative, pinned 26 months before publication, and
with no digest recorded. For a document whose entire job is assigning code
points to cryptographic algorithms, that absence is the headline.

## Only one code point is actually this document's

Read against §10's opening — IANA *re-pointed* existing registry rows from
RFC 8152 — **RFC 9053 allocated nothing but `IV-GENERATION` = 34** (Recommended:
No, empty Capabilities). It is the citation of record for 42 code points it did
not allocate. The rule for citing it: cite the registry for the number and
§2.1/§2.2 for the constraint, and never cite RFC 9053 without RFC 9864, which
`updated_by` names.

## The hardest constraints are not BCP 14

This is the most important thing for anyone building a conformance suite from
this record. The ECDSA curve restriction ("This document defines ECDSA as
working only with the curves P-256, P-384, and P-521"), the key-type
requirement ("This document **requires** that the curves be encoded using the
'EC2' … key type"), the AES-GCM 96-bit nonce and 128-bit tag, the AES-CBC-MAC
all-zero IV, the `COSE_KDF_Context` AlgorithmID presence ("This field is
**required** to be present.") and the fresh-IV rule ("A new IV **must** be used
for each message if the same key is used.") are **every one of them lowercase
prose**. They are captured as `inferred` entries naming the phrase that carries
the force. A checker built from the 101 uppercase keywords misses all of them.

Related, and why four of five schema files are ours: §1.4 says CDDL "could not
be used as the data description language to normatively describe the CBOR data
structures", that the objects "are described in prose", and that CDDL
descriptions are "(non-normative)". So the one CDDL fragment that exists is
non-normative text inside an Informational document.

## The pre-hash refusal

§2.2 admits only pure EdDSA and excludes HashEdDSA, and the rationale is a
**memory and streaming argument, not a cryptographic one**: the entire message
must be held in memory anyway, so incremental hashing buys nothing. It names
the sanctioned workaround — define the content as a hash value and transport
the COSE object and the content as separate items, i.e. hash-as-content with a
detached payload, *outside* the signature algorithm.

RFC 9964 §7.2 later declines HashML-DSA on different grounds (verify-routine
divergence) and offers no workaround. Different authors, families and
arguments; identical outcome; both going out of their way to say they are not
assigning a code point. **Nine years between the published statements**
(RFC 8152 July 2017 → RFC 9964 May 2026) — not the twelve sometimes quoted,
which would require the pre-8152 drafts this library does not hold.

The cost to us is concrete: §2.2's route moves canonicalisation from the
authoring path to the **verify** path, which breaks condition (3) of the
`canonical-encoding` six and makes conditions (5) and (6) security-critical
rather than merely unstated.

## Source defects found

Reported, never repaired:

1. **A `MUST NOT` resting on an informative reference.** §4.1.1's "MUST NOT
   exceed 2^32 [SP800-38D]" cites a tag listed in §12.2 **Informative**
   References — while the identical NIST document also appears as `[AES-GCM]`
   in §12.1 Normative, under a different URL.
2. **§12.2's `[SP800-56A]` revision mismatch** — cited as "Revision 3" with DOI
   `…800-56Ar3` but the URL points at `…800-56Ar2.pdf`. §5.2 bases the whole
   context structure on this reference.
3. **A token severed by hyphenation at a line break, three times** —
   `IV-GENERATION` at §6.1.2 and §8.1, `Leading-zero` at §7.1.1. Three quotes
   are therefore fragments, each flagged in its `field`. Note the *same*
   sentence is unbroken for the y-coordinate, so the x and y rules read
   differently in the plain text while being identical in the source XML.
4. §4.1.1 typo: **"AES-CGM"** for AES-GCM. §8 typo: **"ECDH-ES+A25KW"** for
   ECDH-ES+A256KW.
5. **Table 8 (HKDF Algorithms) has no Value column**, unlike Tables 1–7 and
   11–18. The HKDF algorithms are not separately registered; their code points
   exist only bound into the recipient algorithm identifiers. Not an error, but
   the schema lane must not look for HKDF code points.
6. **§8's capability example `0x8101820104` is a CBOR *sequence*, not one
   array** (`0x8101` = `[1]`, `0x820104` = `[1,4]`); a one-item decode silently
   leaves three bytes unconsumed.
7. `IV-GENERATION` = 34 **overloads the COSE Algorithms registry** with a
   `COSE_KDF_Context` AlgorithmID that can never be an `alg`.

## One honesty note about this extraction's own quotations

A mechanical audit of every double-quoted span of 22+ characters **found and
fixed 12 real splices** of our own making: text from the *Description* column
of Tables 10, 12, 15, 19 and 23, reassembled down a wrapped cell and presented
as quotation. Those are now glossed rather than quoted, under a stated
quotation rule in the file header. One paraphrase-as-quote, one recased
sentence and two altered scare-quotes were fixed the same way. Every computed
value — CBOR head bytes, signature sizes, protected-header bytes — is marked
**(OURS)** wherever it appears, because RFC 9053 prints no bytes and no sizes.

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

**State: FX-1 complete, all three passes, `profile: full`.** Pass 1 (extract):
two agents in parallel at effort max. Pass 2 (verify): one agent at effort max,
independently re-deriving the counts and attacking every claim. Pass 3
(cross-check): one agent at effort max, checking artifact against artifact.
All three read only `.cache/rfc-9053.txt` and the artifacts.

What pass 2 changed: the hyphenation finding below (defect 3) was understated —
pass 1 reported three severed tokens and had flagged three quotations, but six
severance sites fall inside quoted text and ten quotations in sibling artifacts
healed the break without saying so; the rule is now stated. Defect 5's
comparison range was wrong. The §8 byte count said "five bytes" for three byte
strings totalling ten. `state-machine.yaml` cited `R-0066` for §4.1.1's 2^32
ceiling; the `MUST NOT` is `R-0065`. `record.yaml` said 214/8 testable where
the file holds 212/10. Everything else below survived.

What pass 3 changed, and it is a short list because pass 2 was thorough.
`messages.yaml`'s `constrained_by` was omitted on all 300 fields and is now
wired: **709 links to 170 of the 222 requirements**, 21 fields carrying an
explicit `[]` with a stated reason, and the linking rule plus the 52 unlinked
requirements enumerated by group in that file's header. `state-machine.yaml`
now carries `constrained_by` on every transition and on the error state, and
three of its claims were falsified: the advisory-threshold transition asserted
`constrained_by: []` while all seven of its thresholds are recorded entries;
the ChaCha20/Poly1305 pair "2^36 / 2^64" was printed in the wrong order against
the messages-then-failures convention the AES-CCM pair sets (2^36 is the
failed-decryption limit, 2^64 the message limit); and the AES-GCM pair read as
though both numbers were failed decryptions when 2^24.5 bounds messages.
`examples/README.md` still said "five bytes" where the three §8.3 byte strings
total ten — the one site pass 2's fix did not reach. `summary.md` said the
source is 2444 lines; it is 2443, as every other artifact already said.

What pass 3 checked and did **not** change: the derived CDDL's 43 algorithm
code points, 4 key types and 7 curves were compared value for value against
every table that carries a Value column — 1–7, 11–14, 16–18, 23 — by script,
name by name and in both directions: 54 comparisons, 0 mismatches. So were the
label and capability tables (9, 10, 15, 19, 20, 21, 22), including Table 15's
five-way ES/SS split, Table 9's and Table 10's identical fourteen-algorithm
scope, and Table 22's element counts. `kdf-context.cddl` is still byte-identical
to source lines 1168–1184 (same SHA-256 as the extracted range). All six
vectors validate against the transcribed CDDL, including `0x8101820104` as the
CBOR **sequence** it is: a one-item decode consumes two bytes and leaves three.

Source: RFC 9053, *CBOR Object Signing and Encryption (COSE): Initial
Algorithms*, August 2022. **Informational**, obsoletes RFC 8152, while its
companion RFC 9052 is **STD 96**.

| kind | file | coverage |
|---|---|---|
| normative | `normative.md` | 323 verbatim statements and 31 fenced blocks, §1–§11 in source order, **all 23 tables reproduced in full** (checked present by caption) plus 8 further fences. Boilerplate, the changes-from-8152 history, Acknowledgments and Author's Address dropped |
| requirements | `requirements.yaml` | 222 entries, `R-0001`–`R-0222`, source order, no gaps: **101 stated, 121 inferred**. `source_keyword_count` and `extracted_keyword_count` both 101, `reconciliation` empty because there is nothing to reconcile — every one of the 101 source occurrences was mapped to exactly one stated entry **by raw byte offset: 101 covered, 0 missed, 0 double-counted**, with a per-section tally that sums to 101 |
| schema | `schema/` | **1 verbatim, 4 derived.** `kdf-context.cddl` is §5.2's `PartyInfo`/`COSE_KDF_Context` fragment, byte-exact at source lines 1168–1184 including the three-space margin (verified by `diff`). The derived four cover all 43 algorithm code points, the key structures per key type, the nine algorithm-specific header parameters, and the §8 capability arrays. No JSON Schema: every structure is a CBOR array or a negative-integer-labelled map, so a JSON projection would be invented |
| messages | `messages.yaml` | 56 structures, 300 fields — 12 non-algorithm structures plus **all 43 algorithm code points with no gaps** plus the 4-entry HKDF family. `constrained_by` wired by pass 3: **709 links to 170 of 222 requirements** over 279 fields, 21 fields with an explicit `[]` and a reason, the linking rule and the 52 unlinked requirements stated in the file header |
| examples | `examples/` | **6 vectors — and that is the finding.** See below |
| protocol | — | `not_applicable`; see `record.yaml` |
| state machine | `state-machine.yaml` | **two machines, and this is the only Tier 1 record where this artifact is not N/A.** A key-usage lifecycle (counter-driven ceilings into rekey) and a key-trust promotion. Both are explicitly marked `derived: true` — RFC 9053 names no state as a state. Every transition and the error state carry `constrained_by`; the two hard ceilings are `R-0065` (2^32 messages, §4.1.1) and `R-0079` (2^61 block-cipher operations, §4.2.1) and everything else in the machine is lowercase prose |

## The document prints no cryptographic test vectors

Not one key, signature, MAC, ciphertext, nonce, derived key, `COSE_Key` or
`COSE_KDF_Context` — for any of **43 algorithm code points**. The only bytes it
prints anywhere are three §8.3 capability byte strings totalling **10 bytes**
(`0x8102`, `0x820201`, `0x8101820104`), §9's `0x01`/`0x1801` pair, and §11's
`"YES"`/`"NO "` illustration. Verified by pass 2 across all 2443 lines: four
`0x` literals in the whole document, zero `h''` byte strings, zero base64, and
**no run of eight or more hex characters anywhere**. §1.5 points instead at `github.com/cose-wg/Examples` **commit
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
3. **Tokens severed by hyphenation at a line break.** The plain-text rendering
   breaks 14 lines at a hyphen that belongs to the token. **Six of those sites
   fall inside text this extraction quotes**: `recipient-specific` (§4.2.1,
   L656), `IV-GENERATION` (§6.1.2, L1263 and §8.1, L1835), `Leading-zero`
   (§7.1.1, L1690), `ECDH-ES+A25KW` (§8, L1827) and `Ephemeral-Static` (§8.3,
   L1958). Note the *same* sentence is unbroken for the y-coordinate, so the x
   and y rules read differently in the plain text while being identical in the
   source XML — `normative.md` carries both forms, the x one as a fragment.

   **Quotation rule for these, stated once for the whole directory**
   (pass 2 — pass 1 applied it to `requirements.yaml` only and did not say so
   elsewhere): where a quotation would cross such a break, it is either **cut
   at the break and flagged in its `field`** — `R-0125`, `R-0182`, `R-0205`,
   and the §7.1.1 x-coordinate statement in `normative.md` — or the break is
   **healed**, joining the two halves with no space, because the hyphen is part
   of the token and the severance is an artifact of the renderer, not of the
   document. Healed quotations are therefore verbatim against the RFC but *not*
   contiguous substrings of the cached plain text. They occur in
   `messages.yaml` (5), `examples/vectors.yaml` (2), `examples/README.md`,
   `design-notes.md`, `schema/README.md`, `schema/algorithm-values.derived.cddl`
   and `schema/capabilities.derived.cddl`. No other quotation in this directory
   departs from the cached bytes.
4. §4.1.1 typo: **"AES-CGM"** for AES-GCM. §8 typo: **"ECDH-ES+A25KW"** for
   ECDH-ES+A256KW.
5. **Table 8 (HKDF Algorithms) has no Value column.** Every other table that
   names *algorithms* has one — 1–7, 11–14, 16–18, 22, 23 — and Table 8 alone
   among them does not. (The *parameter* tables 9, 10, 15, 19, 20 and 21 have
   no Value column either, but they key on Label and are a different kind of
   table; pass 1 wrote "unlike Tables 1–7 and 11–18", which is wrong, because
   Table 15 falls in that range and is a parameter table.) The HKDF algorithms
   are not separately registered; their code points exist only bound into the
   recipient algorithm identifiers. Not an error, but the schema lane must not
   look for HKDF code points.
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

**Pass 2 re-ran that audit independently and the fix holds.** Every multi-line
table cell in all 23 tables was reassembled and searched for across every
artifact: 13 reassembled cells appear in `messages.yaml` and **not one of them
is inside quotation marks** — each is introduced as "Description column,
glossed not quoted". A separate case-insensitive run-matching sweep over the
whole directory found **no recased quotation** and no altered character in any
span of seven or more words. The only quotations that depart from the cached
bytes are the hyphen-healed ones in defect 3 above.

---
record: rfc-9942
kind: schema
title: "rfc-9942 — schemas"
extracted: "2026-09-30"
reviewed_by: ""
---

RFC 9942 contains **seven CDDL blocks** holding **33 rule heads over 30
distinct names**. All seven are copied here verbatim, one file each. An
eighth file, `receipts-merged.derived.cddl`, is a derived rendering and is
clearly marked as such.

**The RFC's CDDL does not compile if concatenated, and the verbatim files
preserve that.** Three rule names are defined twice, one of them with a
divergent body; three type names are referenced but defined nowhere. None of
this is repaired in the `.cddl` files. The repairs live only in the derived
file, each one labelled. See **Defects** below — that is the substance of
this extraction, not an appendix to it.

Verbatim means verbatim: rule order, interior blank lines, the source's own
`;` comments, column alignment, the mixed use of commas between group
entries, the two spaces before `=>` on the `receipts` entry at line 246, and
the RFC's three-column left margin. CDDL ignores leading whitespace, so the
retained margin does not affect parsing.

## Files

| File | Source | Lines | Caption | Rules defined |
|---|---|---|---|---|
| `figure-01-cose-sign1-with-receipts.cddl` | §4.3 Usage, Figure 1 | 236–338 | 340 | 23 — see below |
| `figure-03-inclusion-proof-content.cddl` | §5.2 Inclusion Proof, Figure 3 | 455–465 | 467 | `inclusion-proof-content` |
| `figure-04-inclusion-protected-header.cddl` | §5.2.1 Receipt of Inclusion, Figure 4 | 487–491 | 493 | `protected-header-map` |
| `figure-05-inclusion-unprotected-header.cddl` | §5.2.1 Receipt of Inclusion, Figure 5 | 504–513 | 515 | `inclusion-proofs`, `verifiable-proofs`, `unprotected-header-map` |
| `figure-07-consistency-proof-content.cddl` | §5.3 Consistency Proof, Figure 7 | 575–586 | 588 | `consistency-proof-content` |
| `figure-08-consistency-protected-header.cddl` | §5.3.1 Receipt of Consistency, Figure 8 | 599–603 | 605 | `protected-header-map` |
| `uncaptioned-consistency-unprotected-header.cddl` | §5.3.1 Receipt of Consistency, **no caption** | 616–625 | *none* | `consistency-proofs`, `verifiable-proofs`, `unprotected-header-map` |
| `receipts-merged.derived.cddl` | **derived**, not in the RFC | — | — | 35, namespaced; see **The derived file** |

The 23 rules of Figure 1, in source order: `Signature_With_Receipt` (236),
`cose-label` (238), `cose-values` (239), `Protected_Header` (241),
`Unprotected_Header` (245), `COSE_Sign1` (250), `Receipt` (257); then an
eight-rule inclusion cluster — `Receipt_For_Inclusion` (263),
`Signed_Inclusion_Proof` (265),
`RFC9162_SHA256_Inclusion_Protected_Header` (273),
`RFC9162_SHA256_Inclusion_Unprotected_Header` (279),
`RFC9162_SHA256_Verifiable_Inclusion_Proofs` (284),
`RFC9162_SHA256_Inclusion_Proofs` (288),
`RFC9162_SHA256_Inclusion_Proof` (292),
`RFC9162_SHA256_Inclusion_Proof_Content` (295) — then an eight-rule
consistency cluster, structurally parallel: `Receipt_For_Consistency` (302),
`Signed_Consistency_Proof` (304),
`RFC9162_SHA256_Consistency_Protected_Header` (312),
`RFC9162_SHA256_Consistency_Unprotected_Header` (318),
`RFC9162_SHA256_Verifiable_Consistency_Proofs` (323),
`RFC9162_SHA256_Consistency_Proofs` (327),
`RFC9162_SHA256_Consistency_Proof` (331),
`RFC9162_SHA256_Consistency_Proof_Content` (334).

### The uncaptioned block

The §5.3.1 block at lines 616–625 is **the only CDDL block in RFC 9942 with
no figure caption**. Figure 8's caption is at line 605, above it; Figure 9's
at line 663, below it, on the EDN example. It is the consistency-side
counterpart of Figure 5 and should have been Figure 8-and-a-half. It cannot
be cited by figure number — cite it as "RFC 9942, §5.3.1, lines 616–625".
Any cross-reference in this library that calls it a figure is wrong.

## Coverage

**Complete.** Every CDDL block in the document is here. The document has no
ASN.1 and no JSON Schema; CDDL is its only formal syntax, roughly 160 of
1033 source lines.

Byte-identity was verified for all seven. For each file, the source range
was extracted with `sed -n 'A,Bp'` and `diff`ed against the file with its
header comment lines stripped (`grep -v '^;'` — safe because every verbatim
line carries the RFC's three-space margin, so no verbatim line can begin at
column 0). All seven diffs were empty and the md5 sums matched:

| File | Lines | Bytes | md5 |
|---|---|---|---|
| `figure-01-cose-sign1-with-receipts.cddl` | 103 | 2682 | `3b868cdd961b9bde3ada9c0314c4d728` |
| `figure-03-inclusion-proof-content.cddl` | 11 | 250 | `edb700b06786bdc1b904e40864a8cf11` |
| `figure-04-inclusion-protected-header.cddl` | 5 | 111 | `8f74f9e09140308d7ce594f69577fca7` |
| `figure-05-inclusion-unprotected-header.cddl` | 10 | 229 | `4959b2c6d8f151c4e893c3fde4573d02` |
| `figure-07-consistency-proof-content.cddl` | 12 | 250 | `85470f47dbc508160641dc1c2275a343` |
| `figure-08-consistency-protected-header.cddl` | 5 | 111 | `8f74f9e09140308d7ce594f69577fca7` |
| `uncaptioned-consistency-unprotected-header.cddl` | 10 | 237 | `ef190f8d6504a658c61fc4d3d30510e4` |

Figures 4 and 8 share an md5: their bodies are byte-for-byte identical.

**Not covered by any CDDL in this RFC**, and so absent here: the EDN
examples (Figures 2, 6, 9 — they belong in `../examples/`), the IANA
registration templates of §8.2.2, the verification procedures of §5.2.1 and
§5.3.1, and the whole of RFC 9162's Merkle Tree algorithm, which is
incorporated by reference and has no CDDL anywhere in RFC 9942.

## Defects

Preserved unrepaired in the `.cddl` files. Mechanically confirmed by
concatenating the seven verbatim files and resolving names: 33 rule heads,
30 unique, 3 redefined, 3 undefined references.

### 1. Rule redefinition — the concatenation is illegal CDDL

RFC 8610 has no rule redefinition. Three names are defined twice:

| Name | First | Second | Bodies |
|---|---|---|---|
| `protected-header-map` | 487 (Fig 4) | 599 (Fig 8) | **identical** |
| `unprotected-header-map` | 510 (Fig 5) | 622 (§5.3.1) | **identical** |
| `verifiable-proofs` | 506 (Fig 5) | 618 (§5.3.1) | **divergent** |

`verifiable-proofs` is the hard one. At 506–508 it is
`{ &(inclusion-proof: -1) => inclusion-proofs }`; at 618–620 it is
`{ &(consistency-proof: -2) => consistency-proofs }`. Two different maps,
one name.

The other two pairs are the subtler trap: the two `unprotected-header-map`
bodies are *textually identical* — both read `&(vdp: 396) =>
verifiable-proofs` plus the extension socket — yet they mean different
things, because each is intended to resolve to its own, differently-bodied
`verifiable-proofs`. Textual identity hides a semantic fork. A reader who
notices only that the two blocks "say the same thing" and keeps one will
silently lose either inclusion proofs or consistency proofs.

The RFC never says the §5 blocks are scope-local, so the scoping has to be
inferred from the surrounding prose. Read each §5.2.1 / §5.3.1 block as a
replacement scoped to its own Receipt type.

### 2. `cose-value` is undefined — erratum-grade

Figure 1 line 239 defines `cose-values`, **plural**, as `any`, and uses it
six times, all inside Figure 1: lines **242, 247, 276, 281, 315, 320**.

Figures 4, 5, 8 and the §5.3.1 block instead write `cose-value`,
**singular**, four times: lines **490, 512, 602, 624**. Every one is the
same idiom, `* cose-label => cose-value`.

`cose-value` appears nowhere in RFC 9942 as a rule head. Checked across the
whole document: the plural occurs at 239, 242, 247, 276, 281, 315, 320 and
nowhere else; the singular at 490, 512, 602, 624 and nowhere else. The four
§5 blocks therefore do not compile even standalone, let alone merged.

The intent is not in doubt — the singular is used in exactly the position
the plural occupies in Figure 1, as the open-ended COSE header extension
socket — but the document as published is wrong. Report as an erratum.

Note the §5 blocks also reference `cose-label`, which only Figure 1 defines.
That is a scoping omission rather than a typo, but it has the same effect:
no §5 block is self-contained.

### 3. `inclusion-proof` and `consistency-proof` are undefined — erratum-grade

A third defect, of the same family, which the §5 blocks also carry:

- Line 504 writes `inclusion-proofs = [ + inclusion-proof ]`. `inclusion-proof`
  is referenced as a type and is defined nowhere.
- Line 616 writes `consistency-proofs = [ + consistency-proof ]`.
  `consistency-proof` is referenced as a type and is defined nowhere.
- Meanwhile `inclusion-proof-content` (455, Figure 3) and
  `consistency-proof-content` (575, Figure 7) are defined and **never
  referenced by anything in the document**.

The missing link is the `bstr .cbor` wrapper. §4.3 spells the equivalent out
— lines 292–293, `RFC9162_SHA256_Inclusion_Proof = bstr .cbor
RFC9162_SHA256_Inclusion_Proof_Content`, and 331–332 likewise — and §8.2.2.2
Table 3 gives the CBOR type of both proof labels as "array (of bstr)". §5
simply omits the two rules.

(The barewords inside `&(inclusion-proof: -1)` and `&(consistency-proof: -2)`
are text-string member keys, not type references, so they are not the
missing definitions and defining rules of those names creates no ambiguity.)

### 4. Two namings for the same structures

§4.3 and §5 define the same two header maps and the same two proof payloads
twice, under two conventions — `RFC9162_SHA256_Inclusion_Protected_Header`
versus `protected-header-map`, `RFC9162_SHA256_Inclusion_Proof_Content`
(`tree_size` / `leaf_index` / `inclusion_path`, underscores) versus
`inclusion-proof-content` (`tree-size` / `leaf-index` / `inclusion-path`,
hyphens). Neither set references the other and the RFC never states which
governs.

**Which to trust for what:**

- **§5 is authoritative for field requirement levels.** Only §5 carries the
  REQUIRED annotations, in prose immediately under each figure: `alg` (1)
  and `vds` (395) REQUIRED at lines 495–499 and 607–611; `vdp` (396) and
  `inclusion-proof` (−1) REQUIRED at 517–521; `vdp` (396) and
  `consistency-proof` (−2) REQUIRED at 627–630. §4.3's CDDL carries no
  optional markers at all, so it cannot distinguish required from permitted.
- **§4.3 is authoritative for the outer `receipts` nesting.** Only Figure 1
  says how a Receipt attaches to a signed object: `Unprotected_Header`
  carries `&(receipts: 394) => [+ bstr .cbor Receipt]` (line 246), each
  element being a CBOR-embedded, tag-18 `Receipt`. §5 has no envelope rule
  at all — it defines header maps and proof payloads but never ties a
  protected header, an unprotected header, a payload and a signature
  together. That is why the two `*-protected-header-map` rules are
  unreachable from any §5 root.
- **For the proof payload layout they agree**, field for field and order for
  order; only the spelling of the entry names differs.

## Header parameters and labels

Three new COSE header parameters, §2 and Table 1 (§8.1):

| Label | Name | Value type | Where |
|---|---|---|---|
| **394** | `receipts` | array of CBOR-encoded Receipts, priority-ordered | protected or unprotected header of the enveloping COSE structure |
| **395** | `vds` | int, from the COSE Verifiable Data Structure Algorithms registry | Receipt **protected** header |
| **396** | `vdp` | map, keyed from the COSE Verifiable Data Structure Proofs registry | Receipt **unprotected** header |

**The only proof labels this RFC defines are `-1` (inclusion) and `-2`
(consistency).** Table 3 (§8.2.2.2) has exactly two rows, both for VDS 1.
There is no `-3`.

If you have seen `-3` attributed to receipts, it came from §4.2. The string
`-3` occurs **exactly once in the entire RFC**, at **line 206**, inside an
analogy to COSE key parameters: "EC2 keys (1: 2) require and give meaning to
specific parameters, such as −1 (crv), −2 (x), **−3 (y)**, and −4 (d)."
Those are EC2 **key** parameters — curve, x, y, d — not proof types. The
very next sentence, lines 207–208, states the actual receipt labels:
"RFC9162_SHA256 (395: 1) supports both (−1) inclusion and (−2) consistency
proofs." The analogy is to the *pattern* of negative labels being
algorithm-specific, not to the values. A sibling record previously carried
the `-3` error; it is wrong.

## Verifiable data structures

Exactly one VDS is defined. Table 2 (§8.2.2.1) has two rows and no more:

| Name | Value | Description |
|---|---|---|
| Reserved | **0** | Reserved (§5.1, no change controller) |
| `RFC9162_SHA256` | **1** | SHA256 Binary Merkle Tree, per §2.1 of RFC 9162 |

Everything else is deferred to IANA registration under Specification
Required (§8.2, §8.2.1). §4.4.1 sets the bar for a new VDS: it MUST define
how to encode its identifier and its Proof Types in CBOR, and MUST define
how to produce and consume them. A distinct hash algorithm needs a distinct
registration — `RFC9162_SHA3_256` would be its own entry. Registrations in
the algorithms and the proofs registries must come in matched pairs
(§8.2.1); one without the other is not permissible.

This matters for the schemas: **all CDDL in this document is
VDS-specific.** Figure 1 says so in its own comment, lines 259–260 — "Note
the proof formats shown here are for RFC9162_SHA256. Other VDSs may have
different proof formats." The `receipts` / `vds` / `vdp` envelope is
general; everything inside `vdp` is not. §4.2 adds that implementers
"should not expect interoperability across Verifiable Data Structures" and
that security analysis MUST precede migration to a new one.

## The derived file

`receipts-merged.derived.cddl` is **derived**, permitted by
`docs/extraction.md` ("plus a machine-checkable rendering"). It does not
replace the verbatim copies and must never be edited into them. Its header
marks it `derived: true` and lists every deviation inline as `[D-n]`.

35 rule heads, no duplicates, no unresolved type references. What was
changed, and nothing else was:

- **[D-1] Namespacing.** The six colliding §5 heads are renamed:
  `inclusion-protected-header-map`, `inclusion-verifiable-proofs`,
  `inclusion-unprotected-header-map`, `consistency-protected-header-map`,
  `consistency-verifiable-proofs`, `consistency-unprotected-header-map`.
  The two identical-bodied pairs are split too, because each
  `unprotected-header-map` must resolve to its own `verifiable-proofs`.
- **[D-2] `cose-value` → `cose-values`**, at the four §5 sites. Resolution
  stated in the file: the plural is correct, the singular is a typo. Grounds
  given there — plural is the only spelling ever used as a rule head, and
  the singular appears only in the idiom the plural already occupies.
- **[D-3] Two rules added** that RFC 9942 has nowhere, marked as additions:
  `inclusion-proof = bstr .cbor inclusion-proof-content` and
  `consistency-proof = bstr .cbor consistency-proof-content`, modelled on
  Figure 1 lines 292–293 and 331–332 and corroborated by Table 3.
- **[D-4] Formatting only.** Left margin dropped, commas made consistent,
  the two `protected :` continuation lines joined, interior space runs
  collapsed (the two spaces before `=>` at line 246 become one), a space
  added after the colon in `inclusion_path:[` at line 298, and the source's
  two consecutive blank lines at 260–262 and 299–301 reduced to one. Six
  changes, all invisible to a CDDL parser. The derived file lists them
  individually so that a byte-for-byte diff against the source leaves
  nothing unexplained; the verbatim files keep every one of these spellings.

Both namings are kept side by side and deliberately **not** merged into one
set of rules — that merge would be an editorial judgement the RFC does not
license.

Roots: `Signature_With_Receipt` reaches 23 rules (the whole §4.3 envelope).
The §5 half is a parallel entry point rooted at
`inclusion-unprotected-header-map` and `consistency-unprotected-header-map`,
reaching 10 more. The two `*-protected-header-map` rules are reachable from
neither, for the reason given under Defect 4: §5 defines no signed-proof
envelope to tie a protected header to an unprotected one. They are
additional roots, not dead rules.

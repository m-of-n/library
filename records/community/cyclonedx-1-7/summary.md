---
schema: "library-summary/v1"
id: cyclonedx-1-7
record: cyclonedx-1-7
type: summary
updated: "2026-11-01"
---

# CycloneDX Bill of Materials Specification

|  |  |
|---|---|
| **Type** | spec |
| **Maturity** | `standard` — adopted by the Ecma General Assembly, December 2025 |
| **Authors** | Jan Kowalleck, Steve Springett (editors, Ecma TC54) |
| **Published** | 2025-12 (spec 1.7 released 2025-10-21) |
| **Identifier** | ECMA-424, 2nd edition · CycloneDX 1.7 |
| **Source** | https://ecma-international.org/wp-content/uploads/ECMA-424_2nd_edition_december_2025.pdf |
| **Digest** | `e8c55a3a968f3ef534fbcdd891c361714d3dc303b3747464f1d554f65b04c8e1` |

## Overview

ECMA-424 defines one bill-of-materials object model for software, hardware,
services, vulnerabilities, cryptographic assets and ML models, plus machine-readable
claims and attestations (§1, §5.1). Its argument is transparency: an inventory lets
a consumer identify risk and comply, and the format's job is to make that inventory
exchangeable (§5.1). It does not claim the inventory is true. §1 NOTE 2 says the
Standard "does not define enforcement mechanisms for verifying the accuracy or
completeness of a BOM". The format is very permissive: only `bomFormat` and
`specVersion` are required at the root (Table 2), and only `type` and `name` on a
component (Table 23). Where it goes further than SPDX is attribution. Any of a dozen
object kinds can carry its own enveloped signature (§6.18), so that "each party in
the supply chain" can sign its own data, and §6.16 citations attribute individual
fields to a named source.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | adjacent | Describes supply-chain state and defines no verification. Security depends on what signs it |
| Cryptography | adjacent | Uses signatures and hashes, and inventories crypto assets (CBOM), but specifies no signing procedure of its own |
| This project | adjacent | Prior art for the artifact-subject question, with no adoption path into the native format |

**R-M-07** (*"Artifact statements SHALL bind at least one content digest."*, ARCH-0001
§5). The format does not meet this by itself. `hashes` is optional on a component
(§6.6.1.16), so a conforming BOM may name every component without a digest. The
algorithm list runs from MD5 and SHA-1 up to SHA3-512 and BLAKE3 (Table 33 and its
enumeration), so a digest's presence says nothing of its strength. A profile binding
CycloneDX to R-M-07 would have to require `hashes` and restrict `alg`.

**R-M-11** (proposed in `ARCH-0001-PROPOSAL-v0.2.0` §7, not in ARCH-0001 v0.1.5). The
`description` mode needs the canonical digest of a structured description. ECMA-424
gives no such thing: the word "canonical" does not appear in the extracted text. A BOM's own
identity is `serialNumber` plus `version` (§5.3), both optional (Table 2), and a
BOM-Link is that pair as a URN, so it names a BOM rather than binding its content.

**Key-named principals.** Signature, signatory and author are separate here, and
nothing in the text read ties them together. A signatory has a `name`, `role`,
`organization` and an optional `signature` (Table 476). Citations point at a
`bom-ref` (Table 502). Whether the key that signed belongs to the signatory named is
left unstated.

## Implementations

Searched 2026-11-01. Licences come from the GitHub API, and capability notes from
each project's README. None of these were run.

| Name | Kind | License | URL |
|---|---|---|---|
| cdxgen | generator, also signs and verifies BOMs; CycloneDX JSON native, SPDX 3.0.1 JSON-LD output | Apache-2.0 | https://github.com/cdxgen/cdxgen |
| cyclonedx-cli | converter across CycloneDX XML, JSON, Protobuf, CSV and SPDX JSON 2.3 | Apache-2.0 | https://github.com/CycloneDX/cyclonedx-cli |
| Syft | generator, CycloneDX and SPDX output; signed attestations via in-toto | Apache-2.0 | https://github.com/anchore/syft |
| protobom | format-neutral BOM library with a per-version support table | Apache-2.0 | https://github.com/protobom/protobom |
| Anchore Enterprise | commercial SBOM management, from web search results only | commercial | https://anchore.com/ |
| Sonatype SBOM Manager | commercial SBOM management, from vendor pages in web search only | commercial | https://www.sonatype.com/products/sbom-manager |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata |

No `distilled/`: this record is at the summary bar. FX-1 extraction of ECMA-424 is
owned by no issue yet, and the 566 pages are mostly generated property tables. A
verbatim normative pass would start from the JSON Schema that §6 calls the reference
implementation. No quotes file: normative text belongs in `distilled/normative.md`.

## Limits

**What was read.** The Ecma PDF named above, 566 pages, digest re-verified on
2026-11-01 against the value recorded in September, text extracted with pypdf. Read
closely: front matter, §1 to §5 and the start of §6 through §6.4, including Tables 2
and 3; the component table (Table 23) and hash tables; §6.9.1; §6.10; §6.14.6 and
§6.14.7; §6.16; §6.18; the bibliography, colophon and licence. **Not read line by
line:** the rest of §6, some 500 pages of property tables, which were searched by
keyword only (JSF, canonical, in-toto, DSSE, SLSA, COSE, CBOR, JWS). The figures
were not viewed. Separately, `bom-1.7.schema.json` at tag 1.7 was opened only for
its root and component `required` lists and its `signature` definition.

**The signature is not specified here.** This is the main defect for our purposes.
The tables say "Enveloped signature in JSON Signature Format (JSF)", yet JSF is in
neither §3 nor the bibliography, and the text defines no fields, algorithms or
signed-bytes rule. The JSON Schema resolves it by `$ref` to `jsf-0.82.schema.json`,
which was not read. So a conforming verifier depends on an unreferenced external
document, and this record cannot say what a CycloneDX signature covers or how a
partial signature composes with one over the root.

**Internal inconsistencies.** The property tables give `signature` as `Array`
(Table 2, Table 281) while its own clauses give `Type: Object` (§6.10.1.6, §6.18).
§1 says the BOM is serialised in JSON, while §5.3 lists JSON, XML and protobuf, and
§3 cites XML normatively. §6 calls the JSON Schema the reference implementation, so
where the prose and schema differ the schema presumably decides, though no clause
says so.

**Completeness stays a claim.** `compositions[].aggregate` can say `complete`
(Table 282), and a composition can be signed, so an author can sign a completeness
claim, which the sbom topic's answer should not be read as ruling out. It remains
the author's word. §6.9.1 is explicit that an unlisted component's dependencies are
unknown rather than absent. `aggregate` defaults to `not_specified`.

**Attribution is by name.** §6.14 declarations and §6.16 citations do supply an
asserter that a bare inventory lacks, which qualifies the topic's "no A". The
asserter is named, not keyed, so it does not reach R-M-07 or a key-named principal
without an added binding. The attestation clauses of §6.14 beyond affirmation were
not read closely.

**Currency.** `CycloneDX/specification` tagged 1.7.1 (2026-06-02) and 1.7.2
(2026-09-17) after this text. The 1.7.2 release notes record a schema-alignment fix
for XML. The 1.7.1 notes were not read, and neither is compared here. The text names no
in-toto, DSSE, SLSA, COSE or CBOR, so it says nothing on interoperating with them.

---
record: rfc-9162
kind: examples
title: "rfc-9162 — examples and test vectors"
extracted: "2026-11-07"
reviewed_by: ""
---

# Examples and test vectors

RFC 9162 prints **structure, not values**: no hash, no signature, no serialized
message. So there are two kinds of file here, and the filename says which.

- `*.verbatim.*` — copied out of the source by `bin/fx1-skeleton`, byte-for-byte
  against the line range in the table (3-column RFC margin removed; nothing else
  changed). Pass 1 re-checked every one against `.cache/rfc-9162.txt`.
- `*.derived.json`, `reproduce.py` — written by this library. Inputs are
  **chosen here** (`d[i] = bytes([i])`, SHA-256, synthetic wire fields) and every
  expected value follows from that choice and the RFC's algorithms, nothing else.

## Run

```sh
python3 -I records/ietf/rfc-9162/distilled/examples/reproduce.py            # check
python3 -I records/ietf/rfc-9162/distilled/examples/reproduce.py --write    # regenerate fixtures, then check
python3 -I records/ietf/rfc-9162/distilled/schema/check-schemas.derived.py  # schemas vs api-samples.derived.json
```

`reproduce.py` is stdlib only and exits 0 only if every check passes (last line:
`checks run: N, failed: 0`). It rebuilds the five `*.derived.json` files and fails
if the file on disk differs from the rebuild.

## Verbatim fixtures

| file | source | content | expected result |
|---|---|---|---|
| `ex-01.verbatim.txt` | §4.4 L953-953 | LogID vector | schema text, byte-identical to the source lines; exercised by wire-vectors.derived.json (serialize, parse, reject) |
| `ex-02.verbatim.txt` | §4.5 L971-995 | VersionedTransType enum and TransItem struct | schema text, byte-identical to the source lines; exercised by wire-vectors.derived.json (serialize, parse, reject) |
| `ex-03.verbatim.txt` | §4.6 L1019-1026 | ExtensionType enum and Extension struct | schema text, byte-identical to the source lines; exercised by wire-vectors.derived.json (serialize, parse, reject) |
| `ex-04.verbatim.txt` | §4.7 L1048-1055 | TBSCertificate vector and TimestampedCertificateEntryDataV2 | schema text, byte-identical to the source lines; exercised by wire-vectors.derived.json (serialize, parse, reject) |
| `ex-05.verbatim.txt` | §4.8 L1090-1095 | SignedCertificateTimestampDataV2 | schema text, byte-identical to the source lines; exercised by wire-vectors.derived.json (serialize, parse, reject) |
| `ex-06.verbatim.txt` | §4.9 L1121-1128 | NodeHash vector and TreeHeadDataV2 | schema text, byte-identical to the source lines; exercised by wire-vectors.derived.json (serialize, parse, reject) |
| `ex-07.verbatim.txt` | §4.10 L1164-1168 | SignedTreeHeadDataV2 | schema text, byte-identical to the source lines; exercised by wire-vectors.derived.json (serialize, parse, reject) |
| `ex-08.verbatim.txt` | §4.11 L1189-1194 | ConsistencyProofDataV2 | schema text, byte-identical to the source lines; exercised by wire-vectors.derived.json (serialize, parse, reject) |
| `ex-09.verbatim.txt` | §4.12 L1212-1217 | InclusionProofDataV2 | schema text, byte-identical to the source lines; exercised by wire-vectors.derived.json (serialize, parse, reject) |
| `ex-10.verbatim.json` | §5 L1320-1323 | error response body (endBeforeStart) | JSON, byte-identical to the source lines; accepted by schema/error-response.derived.schema.json (checked by `check-schemas.derived.py`) |
| `ex-11.verbatim.txt` | §6.3 L1796-1800 | SerializedTransItem vector and TransItemList | schema text, byte-identical to the source lines; exercised by wire-vectors.derived.json (serialize, parse, reject) |
| `fig-01.verbatim.txt` | §2.1.1 L333-333 | MTH of the empty list | formula, byte-identical to the source line; implemented as MTH / PATH / SUBPROOF in reproduce.py and checked on every tree of 1..65 leaves |
| `fig-02.verbatim.txt` | §2.1.1 L337-337 | MTH of one entry (leaf hash) | formula, byte-identical to the source line; implemented as MTH / PATH / SUBPROOF in reproduce.py and checked on every tree of 1..65 leaves |
| `fig-03.verbatim.txt` | §2.1.1 L343-343 | MTH of n > 1 entries | formula, byte-identical to the source line; implemented as MTH / PATH / SUBPROOF in reproduce.py and checked on every tree of 1..65 leaves |
| `fig-04.verbatim.txt` | §2.1.3.1 L422-422 | PATH of a single leaf | formula, byte-identical to the source line; implemented as MTH / PATH / SUBPROOF in reproduce.py and checked on every tree of 1..65 leaves |
| `fig-05.verbatim.txt` | §2.1.3.1 L428-430 | PATH recursion | formula, byte-identical to the source line; implemented as MTH / PATH / SUBPROOF in reproduce.py and checked on every tree of 1..65 leaves |
| `fig-06.verbatim.txt` | §2.1.4.1 L491-491 | PROOF | formula, byte-identical to the source line; implemented as MTH / PATH / SUBPROOF in reproduce.py and checked on every tree of 1..65 leaves |
| `fig-07.verbatim.txt` | §2.1.4.1 L505-505 | SUBPROOF, m = n, true | formula, byte-identical to the source line; implemented as MTH / PATH / SUBPROOF in reproduce.py and checked on every tree of 1..65 leaves |
| `fig-08.verbatim.txt` | §2.1.4.1 L510-510 | SUBPROOF, m = n, false | formula, byte-identical to the source line; implemented as MTH / PATH / SUBPROOF in reproduce.py and checked on every tree of 1..65 leaves |
| `fig-09.verbatim.txt` | §2.1.4.1 L520-520 | SUBPROOF, m <= k | formula, byte-identical to the source line; implemented as MTH / PATH / SUBPROOF in reproduce.py and checked on every tree of 1..65 leaves |
| `fig-10.verbatim.txt` | §2.1.4.1 L526-526 | SUBPROOF, m > k | formula, byte-identical to the source line; implemented as MTH / PATH / SUBPROOF in reproduce.py and checked on every tree of 1..65 leaves |
| `fig-11.verbatim.txt` | §2.1.5 L584-598 | 7-leaf tree | figure, byte-identical to the source lines; reproduce.py builds the tree from the named leaves and checks every node and proof the text prints (merkle-7leaf.derived.json) |
| `fig-12.verbatim.txt` | §2.1.5 L610-634 | incremental build: hash0, hash1=k, hash2, hash | figure, byte-identical to the source lines; reproduce.py builds the tree from the named leaves and checks every node and proof the text prints (merkle-7leaf.derived.json) |

`ex-10.verbatim.json` carries no header line because a JSON file cannot hold a
comment; its locator is the one in the table.

## Derived fixtures

| file | source | content | expected result |
|---|---|---|---|
| `merkle-7leaf.derived.json` | §2.1.5, L580-646 | the 7-leaf tree of the figure with d[i] = bytes([i]): hash of every named node a..l, `hash`, `hash0`, `hash1`, `hash2`, and the empty-tree hash | `reproduce.py` rebuilds every value; MTH(D[0:3]) = hash0, MTH(D[0:4]) = hash1 = k, MTH(D[0:6]) = hash2, MTH(D) = hash; the §2.1.2 stack algorithm gives the same root |
| `inclusion-proofs.derived.json` | §2.1.5 L600-606, §2.1.3.1, §2.1.3.2 | `accept`: PATH for d0, d3, d4, d6 (the four the RFC prints) and the one-leaf tree; `reject`: leaf_index >= tree_size, tree_size 0, path one node short and long, nodes swapped, wrong root, wrong leaf, leaf not hashed with the 0x00 prefix; `observations`: tree_size is not bound by the root hash | every `accept` case verifies by §2.1.3.2 as printed and its node names equal what the RFC prints ([b,h,l], [c,g,l], [f,j,k], [i,k]); every `reject` case fails, at the step named in `failed_at` |
| `consistency-proofs.derived.json` | §2.1.5 L636-646, §2.1.4.1, §2.1.4.2 | `accept`: PROOF(3), PROOF(4), PROOF(6) for the RFC-printed trees; `reject`: empty path, first == second, first > second, first == 0, path short, long, swapped, wrong first_hash, wrong second_hash; `first_equals_second_outside_stated_domain`: what the printed steps do outside 0 < first < second | every `accept` case verifies by §2.1.4.2 as printed and its node names equal the RFC ([c,d,g,l], [l], [i,j,k]); every `reject` case fails |
| `wire-vectors.derived.json` | §4.4-§4.12, §6.3, §6.5, §7.1 | hex of LogID, TimestampedCertificateEntryDataV2, TransItem x509_entry_v2 (and its leaf hash), x509_sct_v2, TreeHeadDataV2, signed_tree_head_v2, inclusion_proof_v2, consistency_proof_v2, an extension vector, TransItemList, the transparency_info TLS extension (Certificate and ClientHello), TransparencyInformationSyntax and the DER Transparency Information extension; `reject`: out-of-range vector lengths, duplicate or unordered extensions, truncated or padded structures | `reproduce.py` serializes each from its fields, parses it back, and rejects every `reject` case; the tbs_certificate (5 bytes) and the signature (64 bytes) are opaque and NOT valid |
| `api-samples.derived.json` | §5.1-§5.7 | one JSON instance per endpoint response, and the submit-entry request, built from the wire vectors | every sample is accepted by its `schema/*.derived.schema.json` (`check-schemas.derived.py`) |
| `reproduce.py` | §2.1.1-§2.1.5, §4 | builds the Merkle tree, generates PATH and PROOF, verifies as printed, serializes the wire structures | exhaustive over trees of 1..65 leaves: every PATH and PROOF verifies; every mutation (short, long, flipped node, leaf_index out of range) is rejected; the §2.1.5 proofs match the RFC's node names; the §2.1.2 stack algorithm gives the §2.1.1 root for every n. No external oracle: no in-repo source holds reference hash values (pass 2 removed eight roots typed from recollection) |

## What the examples found in the source

- **First == second.** §5.3 requires an *empty* consistency proof when the two sizes
  are equal; §2.1.4.2 step 1 fails an empty path and is stated for 0 < first < second.
  The raw steps reject the empty proof (`consistency-proofs.derived.json`). A client
  must compare the two STH root hashes itself.
- **tree_size is not committed by the root hash.** The same leaf, path and root
  verify against two different tree_size values (`inclusion-proofs.derived.json`,
  `observations`); in the exhaustive run a wrong tree_size was still accepted for most
  proofs. Take tree_size and root_hash from the same signed STH.
- **§2.1.5 wording.** The text says "Non-leaf nodes c, g are used to verify hash0",
  "non-leaf nodes d, l" and "non-leaf node j"; in the figure c, d and j are the leaf
  hashes of d2, d3 and d6, so those nodes are leaves.
- **NodeHash is nested.** A vector of `NodeHash` carries a 1-octet length before every
  hash inside the 2-octet vector length (33 octets per SHA-256 node); the source never
  shows a serialization (`wire-vectors.derived.json`).

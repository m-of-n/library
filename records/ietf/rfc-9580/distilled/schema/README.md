---
record: rfc-9580
kind: schema
title: "rfc-9580 — schemas"
extracted: "2026-10-13"
reviewed_by: ""
---

# RFC 9580 — schemas

**RFC 9580 publishes no schema.** It has no CDDL, no ASN.1 module and no JSON
Schema. OpenPGP is a **data format**: a binary packet format, not a wire
protocol with peers and exchanges. The format is defined by prose, bulleted
field lists, bit figures, formulas, a little C, and thirty registry tables.
So this directory holds two kinds of file:

- **verbatim** (`*.verbatim.txt`): every formal or semi-formal structure the
  source prints, copied byte for byte, 196 regions in all. Each region has its
  section, its line range and its own sha256. Nothing in these files was
  written by this project except the file headers and region markers.
- **derived** (`*.derived.*`): machine-checkable renderings that this
  project wrote from the verbatim regions. Every derived file says
  `DERIVED` at the top. Every derived definition cites its section and its
  verbatim region ids, and where a requirement constrains it, its
  `rfc-9580#R-NNNN` ids from `../requirements.yaml`. None of them is
  RFC text.

Source: `.cache/rfc-9580.txt`, sha256
`36540e57b63d24c0b17be0748b704bdeed3d643ce99a4fb1abb6469c1eb1ff18`, 9138
lines, without page furniture. This is RFC 9580 as published in July 2024. It
obsoletes RFC 4880, 5581 and 6637.

## Files

| file | kind | source | source lines | regions | lines · bytes | sha256 |
|---|---|---|---|---|---|---|
| `registries.verbatim.txt` | verbatim | Tables 1–30: §3.7.1, §3.7.2.1, §5, §5.2.1, §5.2.3.7, §5.2.3.24, §5.2.3.25, §5.2.3.29, §5.2.3.31, §5.2.3.32, §5.5.4, §5.12, §5.12.1, §6.2.1, §6.2.2, §9.1–§9.6, §10.3.2.1, §10.3.2.2, §11.2, §11.3, §11.5.1 | 637–5945, 920 lines in 30 ranges | 30 | 1125 · 70790 | `d63b839e95ca03461fdef4b92d4ed1d29abe213980f8ca6c39986105e2ab21b7` |
| `grammars.verbatim.txt` | verbatim | §10.1.1–§10.4 packet-sequence grammars; §8 Regular Expressions; §6–§6.2.3 ASCII Armor; §7.1–§7.2 Cleartext Signature Framework; §5.4 OPS bracketing | 3048–5542, 347 lines in 23 ranges | 23 | 512 · 24142 | `82977365f68fa43d6d8e5eaf00f127a1c36b233040f417e80ca4f6f909fd7b6d` |
| `encodings.verbatim.txt` | verbatim | §3.1–§3.7.2.1, §4.2–§4.3, §5.1.3–§5.1.7, §5.2.2–§5.2.4.1, §5.3.2, §5.5.3–§5.5.4.3, §5.5.5.6.1.1, §5.7, §5.12.1, §5.13.1–§5.13.5, §6.1.1, §9.2, §11.2.1–§11.5, §12.1.1–§12.1.3 | 546–6063, 1063 lines in 60 ranges | 60 | 1451 · 64278 | `663a9f20f1764e28b4f472704d668e7fe41e9c7d7beb170143b6e5bbda9a35d6` |
| `fields.verbatim.txt` | verbatim | §5.1.1–§5.13.2: every packet field list, algorithm-specific field list and subpacket body format | 1269–4127, 723 lines in 83 ranges | 83 | 1248 · 52196 | `85a3b1e52441450ee8a9226f38534f1e9403fd1e4dff98fd9df2235d0af7e73d` |
| `openpgp-packets.derived.schema.json` | **derived** | JSON Schema (draft 2020-12) for a decoded packet stream; §3, §4, §5, §9, §11 | — | — | 10275 · 192222 | `8caecd65026a8ae4ec6cb2c096cf46968a2b44783d5f1c36b091b9a9b68ad544` |
| `packet-sequences.derived.abnf` | **derived** | ABNF of the §10 grammars over a one-terminal-per-packet alphabet | — | — | 146 · 7939 | `c4feaef2fbe409189315975f8bffe0b22bfc3e03f32b6144cd72ce47f41f51bf` |
| `text-formats.derived.abnf` | **derived** | ABNF of §6.2 ASCII Armor, §7 cleartext signed messages, §8 Regular Expressions | — | — | 99 · 5637 | `c8f5400a51d45a2d7d2b5ae83302c4a2745232f261d6961474661134f1b4456f` |
| `validate.derived.py` | **derived** | decoder, schema check, cross-field checks and grammar matcher; self-test on Appendix A | — | — | 988 · 40417 | `ca83f01610434686aa37c7b8705d39490b0075cabe089a7ab8efc920712021ec` |

`sha256` is the digest of the file as committed. In the verbatim files, each
region also carries the digest of its own bytes (see the region tables).

## How the derived files map to the source

| derived file | renders | from verbatim regions | checked by |
|---|---|---|---|
| `openpgp-packets.derived.schema.json` | a **decoded** packet stream, as JSON (draft 2020-12): packet header and length encodings (§4.2); the body of every packet type in every version (§5.1–§5.14); signature subpackets by type ID, each with its body format (§5.2.3.11–§5.2.3.36); key material per algorithm, public and secret (§5.5.5); secret-key protection (§5.5.3, Table 2); S2K specifiers (§3.7.1); and enums for Tables 1–5, 10, 13, 15, 18, 19, 21–23 and 25 | all F, T and most E regions | `jsonschema` meta-validation; all 14 Appendix A blocks validate; 31 mutation cases are rejected |
| `packet-sequences.derived.abnf` | the §10 grammars: v6 certificate, v6 revocation certificate, v4 certificate, v3 key, TSK, keyring, OpenPGP Message with unwrapping, detached signatures | G-01, G-13 – G-23 | loaded with `abnf` 2.2.0 (`strict=True`); every Appendix A block parses under its rule; 7 rejection and 5 acceptance cases |
| `text-formats.derived.abnf` | ASCII Armor (§6.2), the Cleartext Signature Framework (§7.1, §7.2) and the Regular Expression syntax (§8) | G-02 – G-12, T-16, T-17 | the same tool; all 14 Appendix A armored blocks parse (13 `armor`, 1 `cleartext-signed`); 8 regex and 3 armor cases |
| `validate.derived.py` | a decoder (binary or armored data to the JSON model), the schema check, the cross-field checks JSON Schema cannot express, and the §10 grammar match (key rules as Python regular expressions; messages by recursive descent) | all | `--rfc` self-test: `ALL OK` on the 14 Appendix A blocks |

### The JSON model

A decoded stream is a JSON array of packets. Each packet is
`{"header": …, "body": …}`. The header carries `format` (`openpgp` or
`legacy`), `type_id`, and `length` with its `encoding` (`1-octet`, `2-octet`,
`5-octet`, `partial` with its `parts`, or `legacy-*`). The body definition is
selected by `header.type_id`. Octet strings are lowercase hex. An MPI is
`{"bits": n, "value": hex}`, where `value` is the octets after the bit count.
Every field name is the source's field description shortened, for example
`hashed_length` for "A scalar octet count for the hashed subpacket data"
(§5.2.3, F-10). Each `$defs` entry carries:

- `x-derived: true`;
- `x-source`, the section or sections it renders;
- `x-verbatim`, the region ids in this directory;
- `x-requirements`, where a requirement applies (158 distinct R-ids cited;
  every id exists in `requirements.yaml`, checked by script).

Registry enums are `oneOf` lists of `{const, title}`, with the table's other
columns kept as `x-` annotations: salt size, digest length, OID, nonce and tag
length, curve OID octets, fsize, point format, and the "Generate?" column.

**What a validation failure means.** The enums admit registered and
private-use values only. A Reserved, unassigned or unknown code point fails
validation by design. That marks the value as *unknown to RFC 9580*, which is
not always *malformed*. RFC 9580 tells an implementation to ignore unknown
non-critical packets (R-0033), to ignore and not reject unknown signatures
(R-0178–R-0180), and to reject sequences that contain an unknown critical
packet (R-0032). The schema accepts non-critical Type IDs 40–63 as opaque, and
rejects critical Type IDs that have no definition (0, 15, 16, 19, 20, 22–39).

**Which rules are enforced.** The schema enforces structure, and every MUST
on the content of a packet that makes the packet malformed or unusable. It
does **not** enforce producer-only rules (MUST NOT generate, SHOULD NOT emit).
Those rules are cited in `x-requirements` and in the descriptions. Where a
rule sets one field by another, it is written as `if`/`then`. Examples:

- the v6 signature and v6 OPS salt length set by the hash algorithm (Table 23,
  R-0060, R-0184);
- the Signature Target hash length set by its hash algorithm (R-0155);
- the AEAD nonce length (Table 25);
- the Argon2 rule `encoded_m >= 3 + ceil(log2 p)`, unrolled into one rule per
  range of p (R-0009);
- the Issuer Fingerprint version equal to the signature version (R-0159,
  R-0160);
- a Signature Creation Time subpacket present in the hashed area (R-0101);
- no legacy curve OIDs in v6 keys (R-0198, R-0286);
- Argon2 used only with S2K usage 253 (R-0018);
- in v6 secret keys, S2K usage limited to 0, 253 or 254 (R-0017, R-0191);
- Partial Body Lengths only on data packets, with the first part at least
  512 octets (R-0028, R-0029);
- Legacy headers limited to Type IDs below 16 (§4.2).

**What only `validate.derived.py` checks**, because these are arithmetic or
cross-packet rules:

- MPI octet counts and unused bits (R-0004), and exact bit counts in v6
  packets (R-0003; a warning in other packets);
- the v6 key material count, v6 SKESK and v6 secret-key parameter counts, the
  X25519/X448 size octet, and Notation lengths;
- the form of a Curve25519Legacy secret key (R-0199–R-0202);
- Issuer Key ID equal to the low 64 bits of the Issuer Fingerprint (R-0158);
- unknown critical subpackets (R-0080);
- fingerprints (§5.5.4): the v4 and v6 fingerprints it computes match the ones
  Appendix A.1 and A.3 print;
- subkey and self-signature versions (R-0312, R-0315, R-0318, R-0321);
- that a v6 key has a Direct Key signature (R-0098);
- OPS/Signature correspondence: version pair from Table 27, type, hash,
  algorithm, salt (R-0185) and fingerprint;
- ESK/payload version alignment from Table 26 (R-0343);
- that decompressed contents form an OpenPGP Message (R-0333);
- armor: Tail Line label, CRC24 (R-0244, R-0245), and cleartext Hash-only
  headers (R-0267).

It does no cryptography: it verifies no signature and decrypts nothing.

### The grammar alphabet

`packet-sequences.derived.abnf` reads a packet stream as a string with one
terminal per packet. The terminal's value is the Packet Type ID. For a
Signature packet it is `%x200` plus the Signature Type ID, so the grammar can
tell a Direct Key signature (`%x21F`) from a Subkey Binding (`%x218`). Marker
packets and non-critical packets are filtered out first, because the source
lets them appear anywhere. The packet versions that decide which certificate
grammar applies are not in the alphabet, so the validator checks them. The
ABNF header lists every reading the rendering had to choose.

## Verbatim regions

The digest convention, stated in every file header: a region's sha256 covers
the bytes between its `---- BEGIN VERBATIM` and `---- END VERBATIM` marker
lines. Those bytes are source lines first to last, each ending in LF, with
the RFC's left margin kept. The source has no page furniture, no CR, no tab
and no trailing whitespace. Its only non-ASCII bytes are four author names in
§16.2, outside every region. So nothing is removed or normalised. A region is
a contiguous line range inside one numbered section, starting and ending on a
non-blank line. Table regions run from the table's top border to the last line
of its caption. Where a lead-in sentence defines a notation, it is included.
Two examples are G-13 ("Entries in square brackets are optional and ellipses
indicate repetition.") and G-21 ("a comma (,) represents sequential
composition …").

### `registries.verbatim.txt` — registry tables (T)

| id | section | source lines | content | sha256 |
|---|---|---|---|---|
| T-01 | §3.7.1 | 637–663 | Table 1, S2K Types | `667f36cd08d22ea247189c98ec59f87c8c9e8d3537febeba473dd3e32c28588c` |
| T-02 | §3.7.2.1 | 841–891 | Table 2, Secret Key Encryption (S2K Usage Octet) | `8f0293b95887b48428d0c5c100309b3680ed44ed85bd55c1be2dd941256c8b27` |
| T-03 | §5 | 1150–1231 | Table 3, Packet Types | `545a47c5465e2ce09558f0b8e2fb5c9cf1798c99a81e1251a47db8994261726b` |
| T-04 | §5.2.1 | 1497–1533 | Table 4, Signature Types | `ef24b824d866b6967dabb323483c0ffd6e25b2409dfc41bb31eda8eaba8da002` |
| T-05 | §5.2.3.7 | 1918–2002 | Table 5, Signature Subpacket Types | `6877add43a1e208e061ae3633b3df8f83dcf257a2feb421cdeb14e38c95989e5` |
| T-06 | §5.2.3.24 | 2399–2407 | Table 6, Notation Flags | `0105b814d3f4a0c184e725028678258cf257c1cae14832232e900c031f4c666a` |
| T-07 | §5.2.3.24 | 2416–2423 | Table 7, Notation Data Subpacket Types | `f407e631c7969b6a662cc9c6bcee2f218818a2d13b6ec2c42e5a1afc36503968` |
| T-08 | §5.2.3.25 | 2453–2461 | Table 8, Key Server Preference Flags | `ee388221cfd39b53227db6b6ed9f54c68efe50f61168a9a4d31e77d1ef1cb693` |
| T-09 | §5.2.3.29 | 2512–2538 | Table 9, Key Flags | `6af9ad7c1fe3967e703e6a8b0a65f1445ba087d313952601c8970a6ed6c7f3e2` |
| T-10 | §5.2.3.31 | 2587–2609 | Table 10, Reason for Revocation | `2fe98f6682628694efd59dfbd484d8d2a21fe3159f651929b1ecc036ae41c684` |
| T-11 | §5.2.3.32 | 2656–2670 | Table 11, Features Flags | `8c61d35e026dd4f94772a5345484dc60bd6a5d9ec6be0c56c8aa1f8131db4f54` |
| T-12 | §5.5.4 | 3326–3344 | Table 12, Key IDs and Fingerprints | `11d4c1f12e080543d89fe08b3746a7e8ca695ffda6de7b411d8d31ac049b0aa1` |
| T-13 | §5.12 | 3905–3915 | Table 13, User Attribute Subpacket Types | `4e81e07a534146583782e3b27be634cbe319b75ca8cfecc5e2266e72673cea93` |
| T-14 | §5.12.1 | 3935–3943 | Table 14, Image Attribute Versions | `caf868cf9ed96ceaa2eda80cb95e02d3d5c0a4b1bc74baab0f55663d5ccb9e62` |
| T-15 | §5.12.1 | 3952–3963 | Table 15, Image Attribute Encoding Format | `be17edf6a2170b5d02b2bc48a4e61a6dc3b99b559f088e48f08b36bb03702b4f` |
| T-16 | §6.2.1 | 4358–4374 | Table 16, Armor Header Lines | `0a467464915cce4ad65e195400d643cae42c1621ee6f2087a8611d6f112b915f` |
| T-17 | §6.2.2 | 4409–4422 | Table 17, Armor Header Keys | `f6121e09d6f894785f9d6909bbefd128c9925f5f055b16f7116e3be6c6b937f8` |
| T-18 | §9.1 | 4638–4758 | Table 18, Public Key Algorithms | `59177411fadd0ded3ac666d55f7ca00001341b3d2effec49004eb3fd13ea2609` |
| T-19 | §9.2 | 4792–4841 | Table 19, ECC Curve OIDs and Usage | `df5968a8da1fc71bfd97ed9e66099a67bb22ce3c650b616c0f3736f8ed2b8fcb` |
| T-20 | §9.2.1 | 4876–4904 | Table 20, ECC Curve-Specific Wire Formats | `7edb016680b82a10bef7b85af169b2eea79fd693ffeb37d6044de2165ef4a7c9` |
| T-21 | §9.3 | 4912–4951 | Table 21, Symmetric Key Algorithms | `3c6d179867a8536894e85847f20edf27b06e46cb5fcdb611ff2ea3446635c681` |
| T-22 | §9.4 | 4965–4980 | Table 22, Compression Algorithms | `5d1865cbb39d4a5cda26a67fa594ed347b5454b80d309850c62d26e803ca5718` |
| T-23 | §9.5 | 4989–5034 | Table 23, Hash Algorithms | `75fef0dc6d53a732b9be39222f4677304e96e4d62d5861a725c959a95eae5fc4` |
| T-24 | §9.5 | 5036–5094 | Table 24, Hash Algorithm Identifiers for EMSA-PKCS1-v1_5 | `67fa7340f0bc7a3cd9a713cba6cfc38f34e635aafc622d7f89a9ddf1d21d672b` |
| T-25 | §9.6 | 5117–5133 | Table 25, AEAD Algorithms | `82491ab61911605c0619e0c376214b305e3851a618dff995773897ae1dcbcaa6` |
| T-26 | §10.3.2.1 | 5465–5487 | Table 26, Encrypted Message Packet Versions | `b2bfeaf553a3308d599e0afe3cfb0b391d2f2eefd8f7ee38a492254bf5cd32e0` |
| T-27 | §10.3.2.2 | 5509–5526 | Table 27, Key and Signature Versions | `094c46d927ed7d6a235367eb863ece927742eb4c3c078430bcfeba398e892c8b` |
| T-28 | §11.2 | 5579–5588 | Table 28, EC Point Wire Formats | `01c6a1dbabb15944e73bb7eb4007379960208b082ed90cc790fbd887d1c7b133` |
| T-29 | §11.3 | 5646–5662 | Table 29, EC Scalar Encodings | `d034510d57c5c1d6b6b8a11e5655b8ff7b31de1afc474feb3add57ae44bf863b` |
| T-30 | §11.5.1 | 5927–5945 | Table 30, ECDH KDF and KEK Parameters | `590798d4969f5145e00d40305893bb14ebf17a12957d7e4b8fdff873cedf7b29` |

### `grammars.verbatim.txt` — grammars and text structures (G)

| id | section | source lines | content | sha256 |
|---|---|---|---|---|
| G-01 | §5.4 | 3048–3052 | one-pass signatures bracket the message | `2036871b4c171d99f33202cbe56774b58238fe64dcc3445f62ac4a97992bf2c4` |
| G-02 | §6 | 4252–4258 | base64 line wrapping | `33b4ac51209b8deccb678e63ceb690838b76bc380c7259f94296527dee9f63b2` |
| G-03 | §6.1 | 4262–4271 | optional checksum | `7b392f31c70515a788b6b309f3ec9778744649b8c09fd5954a5f8b041d307e6c` |
| G-04 | §6.2 | 4336–4348 | ASCII Armor structure | `1d78760ad4fcee9661530275ffcf9d113e4f0329cb383c813462b4eee98e9f3c` |
| G-05 | §6.2.1 | 4352–4356 | Armor Header Line form | `9377442b8835ac824bc7c1fb8c11b9f7936d046dad4fbd81e6b0a7568cc8daa2` |
| G-06 | §6.2.1 | 4376–4379 | Armor Header Line is a complete line | `64368a33c71aac603042ec5d0f8a65c8cb8f72d41735a5a93efa7e0f41a6c62c` |
| G-07 | §6.2.2 | 4389–4394 | Armor Header key-value form | `0809da73f60e919d8f9f25f162bffd7630cf0fe89dabdafc3ecb6d54bc6a552a` |
| G-08 | §6.2.3 | 4478–4480 | Armor Tail Line | `25f4b669f36dd9d05b64216663e2c03d149e48f5debded131443aa9808f2f246` |
| G-09 | §7.1 | 4495–4512 | cleartext signed message structure | `7811ed7e6e66a598ff7071d06d0a0d689fe413b499d42b6eef65bcb71541cf54` |
| G-10 | §7.1 | 4514–4529 | cleartext digest and header constraints | `df4640e267673dec68cabdc20db74f491f2db8ac59ccd24fee3c32b19cfd2a7e` |
| G-11 | §7.2 | 4535–4547 | dash-escaped text | `2fb1c45609a698f2f64324f07e5bef08b28a73a9e2b682ed3db3dd2bae2d88dd` |
| G-12 | §8 | 4593–4623 | Regular Expression grammar | `2686588f743fdce8ae6e1989d58b68a422f810f142bdc5c3652b9a2dbc589b61` |
| G-13 | §10.1.1 | 5194–5209 | v6 certificate structure | `b71b96377d7b91ab951cb2c10b03008aba87e0d1e1088482b857dd653017a74b` |
| G-14 | §10.1.1 | 5211–5218 | v6 certificate constraints | `47a0cf6341b2a680e801b374f2e73b22d76a00eccf403f223eeb23700858a481` |
| G-15 | §10.1.2 | 5222–5229 | v6 revocation certificate | `064cbb9765d942b825be7f881aa32132149fb21a50f34bef509be6c5389291bd` |
| G-16 | §10.1.3 | 5233–5243 | v4 certificate structure | `cd6f963c07523c0a7a67e7a4f2c5638d283c5f296e553b33ca5a643dd166d1ce` |
| G-17 | §10.1.3 | 5245–5258 | v4 certificate constraints | `b2a1bfd61adb992850fcddf3066c3933470b062ca19f6f94d918107f73a5abd6` |
| G-18 | §10.1.4 | 5262–5278 | v3 key structure | `bd2e5868afe3e26583e9f6b0f0f0a1f042b9fd8312f2901fba3997272f6c1c6d` |
| G-19 | §10.1.5 | 5282–5349 | common requirements | `12bcc7a30c00454377f92c0c1069fa8d5e3572aaac20dad26c03e4e8fe0a92a7` |
| G-20 | §10.2 | 5353–5363 | Transferable Secret Keys | `5bc2d528ce6e3916f2437a0ba5280a3e1b9c3df0d79f77a59dd1692ef624e369` |
| G-21 | §10.3 | 5367–5398 | OpenPGP Message grammar | `3bf41cf8ca74636ba38254af5f688d9dd0c4f56179269f80a76d2333082f1fb2` |
| G-22 | §10.3.1 | 5402–5424 | unwrapping | `1fb8511067310e22b7a425cec0185e65bfc1af881070cfa89b61d37f7879b264` |
| G-23 | §10.4 | 5535–5542 | detached signatures | `5ba11c9069fd077b2a74c025e2544a4da3eba0060f08e595f0c8099024e61263` |

### `encodings.verbatim.txt` — encodings, formulas and code (E)

| id | section | source lines | content | sha256 |
|---|---|---|---|---|
| E-01 | §3.1 | 546–549 | scalar numbers | `f14537372a00d4c1392dcdcb722e2f3257c6afc14b8f7c588b755d31cb4ff09d` |
| E-02 | §3.2 | 556–586 | multiprecision integers | `f5f0e6da92f4a265d42bb53a1f1ffae53f82eaf6095f8738f0297da0309d3408` |
| E-03 | §3.2.1 | 590–596 | MPIs encoding other data | `29cb2c47b5a51859ccfe77c901bee3506d313c92dfd46ed75acedcc77159734c` |
| E-04 | §3.5 | 614–615 | time fields | `77b71342a6db12af717719d03f11aaf57202fc72cdc3357d4f60d65f2976bd1f` |
| E-05 | §3.7.1.1 | 675–676 | Simple S2K layout | `725ade6362ba8fcf9ed159986be1e33d7bac086b02c151b42b32da7d598fdea3` |
| E-06 | §3.7.1.2 | 705–707 | Salted S2K layout | `c782c471d6ae6431965da170b74de835c9c338ef6fab10426c343bfcfba26118` |
| E-07 | §3.7.1.3 | 720–731 | Iterated and Salted S2K layout and count | `a0b583fce3fecc4239d1483748af05c608b528957e2d278d8b7990dd00a81086` |
| E-08 | §3.7.1.4 | 757–762 | Argon2 S2K layout | `266ce6c4c0b6dd1b5bd728f5c52894a764074a74d9673f6fb8448790581ed43f` |
| E-09 | §3.7.1.4 | 766–776 | Argon2 parameter constraints | `51125275906162dc69dc6b8364c67170849a8130d99d544607df794065958ca3` |
| E-10 | §3.7.1.4 | 784–790 | Argon2 S2K example | `e4602ae33c43418044021b05c5394a01807509ff41c23e9a59f320087d628bae` |
| E-11 | §3.7.2.1 | 836–839 | check(x) notation for Table 2 | `7ee72a81ff09cc757582d423ce6c07031a22d59c05f0ca0f5e5803579ae3afdd` |
| E-12 | §4.2 | 969–984 | packet header first-octet figure | `0b3e37f68a6292314b3823222abb3c42f2f7bc566ab2d6f8f73a5ed04d453a0a` |
| E-13 | §4.2 | 1001–1003 | Legacy format Type ID range | `e67af56f3778e82e773f830d82d0f69c05863e505b0bea313484352b3bebcecb` |
| E-14 | §4.2.1 | 1007–1021 | four length encodings | `d3b982c1698626dccd21d9d4e97f6bc2caa0e060cccb5d1ff8ca61475500d10d` |
| E-15 | §4.2.1.1 | 1025–1029 | 1-octet lengths | `9eb085f98326bde43a68743a416c0371c2cd4e0497f7c93b71c3e82a3dff0f1e` |
| E-16 | §4.2.1.2 | 1033–1037 | 2-octet lengths | `f6df78463e9b7f8cd338c44d76d6b7bb22653da0b4c0e1434dc90d6c56fc1bee` |
| E-17 | §4.2.1.3 | 1041–1049 | 5-octet lengths | `c7b48ce928482c072fb46d1c2b2093bdefe3c90666229b71618e659365b301a7` |
| E-18 | §4.2.1.4 | 1053–1074 | partial body lengths | `3f98ebdc2b1f2455a8da05dbc01d14fff9961e89f19340d51f4250584a3c0049` |
| E-19 | §4.2.2 | 1078–1098 | Legacy length-type | `05a3a80fbc270e8cd2473ccb1f512ea17b444043b7aa2f69682042112657ff19` |
| E-20 | §4.2.3 | 1102–1133 | packet length examples | `574d00e4c3382846794fc8438c9b1d6e81457331527e0a46043b706804450395` |
| E-21 | §4.3 | 1137–1144 | packet criticality ranges | `3cb015a77dd4dfe27cbb7007c2348774f068c0eb0e2260dfbd51daf3e341f3a7` |
| E-22 | §5.1.3 | 1327–1342 | RSA session key encoding | `4c5f7e03fbd108059c583eb6044ee17c14280b14b0b350b5192b53036161e230` |
| E-23 | §5.1.4 | 1355–1370 | Elgamal session key encoding | `4c5f7e03fbd108059c583eb6044ee17c14280b14b0b350b5192b53036161e230` |
| E-24 | §5.1.6 | 1399–1420 | X25519 HKDF and key wrap | `58a548e7338a834a59c19d9ececac9b4c8a2dbe5c0a2ccc0242fb64ee2c58b90` |
| E-25 | §5.1.7 | 1433–1454 | X448 HKDF and key wrap | `e6e9ddc6e85e18ec3c3d2e963c40694105bdd829403115f75479ae5aeef5cf0c` |
| E-26 | §5.2.2 | 1676–1681 | v3 signature hashing | `a693cb44a2b1344a2872e11ef8b2f11331b30fa3ee2da64897f126bcba1f34dd` |
| E-27 | §5.2.3.6 | 1835–1844 | hashed data and left-16 check | `abae9679661502ebe446a080c9d560be8d91f1a028a9d71c93c3f0e62f444a15` |
| E-28 | §5.2.3.7 | 1864–1914 | subpacket header, length decoding, critical bit | `42631aaccd9e05aa12ffea5e0e2e46fe5039ed33182894887759d4c6a63323f3` |
| E-29 | §5.2.3.15 | 2216–2222 | Preferred AEAD Ciphersuites example | `4354b57d04fd0299624184d67b883ae9888033a95b2b4920e48b82c8ea911f26` |
| E-30 | §5.2.4 | 2741–2824 | computing signatures, hashed data stream | `0e798e74c89aa09521136fb3fe07deda0baa4812b5855fd23970998828e5bd7b` |
| E-31 | §5.2.4.1 | 2831–2844 | trailer octets | `836559865a52ea813d9bbf00c678e99240bb26e6eed67416af4ca957eb1a03b4` |
| E-32 | §5.3.2 | 2982–2998 | v6 SKESK KEK and additional data | `138923aa9b78f5734390ba3bca313870eb862539f1cbdf41653b45362ac982d3` |
| E-33 | §5.5.3 | 3272–3294 | secret key AEAD KEK and additional data | `626a9d0e70d8b408bc8af4d0c6c0ffcdba4c312ac522bfbbaa503cea76bd9f79` |
| E-34 | §5.5.4.2 | 3358–3378 | v4 fingerprint material | `e09895814e4f08cb94bc601d3d2f77ef8285f72a61d8611251923ae21a992a0a` |
| E-35 | §5.5.4.3 | 3382–3405 | v6 fingerprint material | `fef5822d43f96c8dda79335e9fb6847ff35e030ba2eb565cd5d85267f7f24f3a` |
| E-36 | §5.5.4.3 | 3416–3419 | subkey fingerprint prefix | `267f988b991859a52b774ba547af7691ad4c7282bd008a056dd97962d04f1e72` |
| E-37 | §5.5.5.6.1.1 | 3579–3595 | Curve25519Legacy secret MPI | `6490b6392a613bc41655d318226e2119ec8b2a52bc8a47f7b1c013636822c670` |
| E-38 | §5.7 | 3729–3747 | SED random prefix | `afb7558719824d1bd761f5109e1bfb7bd8c8e14eaf710001674eca56fdc745f0` |
| E-39 | §5.12.1 | 3925–3933 | image header | `74ed7a2d2d22534e1b10f96d9d5c4d05b018feeda1e10c7db40b687bfa55ab64` |
| E-40 | §5.12.1 | 3945–3950 | image header encoding and reserved octets | `3fcdef9bee6f22da134d3d5e3f48962195ae9806a3674851ffc366f18e2531ab` |
| E-41 | §5.13.1 | 4014–4041 | v1 SEIPD prefix and MDC | `73aee32542786316219aef9bdf1e3f77e1684914c2e975226dca8947501f41c7` |
| E-42 | §5.13.2 | 4129–4184 | v2 SEIPD key derivation, chunks, nonce | `d62b488c79bd42829391c2ab9017b97a38f1df793eda7b2a8a01ed5a06a4df7e` |
| E-43 | §5.13.3 | 4190–4192 | EAX parameters | `74f92428798485111f6f772aeb8d92a4f1f2fca92a93d131092f44932f94ab1c` |
| E-44 | §5.13.4 | 4198–4200 | OCB parameters | `caa1459edfb2cf7346dd252b71cd4de69001d5c570ddcc5b05efb960b2226d43` |
| E-45 | §5.13.5 | 4207–4209 | GCM parameters | `94c867e0b25da94a3b05068bcc77fbcda48b87afca3aabe9644b994a77caa86c` |
| E-46 | §6.1.1 | 4305–4326 | CRC24 in C | `1770a7e24106e5a8817c164afb817f64fd2fc34d2be9b13412047d1c544d57a7` |
| E-47 | §9.2 | 4843–4850 | field size (fsize) | `657805d60a1140c7e38047e2ad30aeea6ab835ab552a82852d9450525941e2f8` |
| E-48 | §9.2 | 4852–4861 | curve OID truncation | `f50cf0791616cfb1b76c0fa6adad05b97c562b304d5d039f224fd7a58dda1891` |
| E-49 | §11.2.1 | 5592–5601 | SEC1 point | `6feca5965a66c9d15a3b315b8a3e3fe33fd4f869f7ac37c494463a9a6fe1e340` |
| E-50 | §11.2.2 | 5605–5612 | prefixed native point | `c38f51a4b4f691897e23992dcdc0ec08f82eb3d1fe643973b56250332b070e79` |
| E-51 | §11.2.3 | 5616–5622 | point MPI sizes | `489e10e21380fc2f4b2c58816bb21ac213f2837a6fbe262172bde0c35b52bfbe` |
| E-52 | §11.3.1 | 5666–5690 | EC octet string wire format | `03a4424dfd515c34790648be05b6ade580f765e98a4849cc59bfe2767631c87d` |
| E-53 | §11.3.2 | 5694–5718 | EC prefixed octet string wire format | `522d142bc4dab951ae7a32520f0a2c3dbbfbbd264be0eda5821fd59d32b00fa3` |
| E-54 | §11.4 | 5732–5746 | KDF synopsis | `38b3f5c1be101a2ac559fb9b7459d19b18fbc5ba3cdc9f2a895343d048c2253f` |
| E-55 | §11.5 | 5763–5807 | ECDH KDF parameters | `0aeaff984cdc3c51923249395037ebb335b65cacf0bcf760ae29b0f7a51fddc3` |
| E-56 | §11.5 | 5816–5871 | ECDH session key padding and output | `f2076468539c7ddc04ef71b24b812a86df6d3f3c25b4c064f76120092808682f` |
| E-57 | §11.5 | 5877–5909 | ECDH synopsis | `9ccd0b789d21f57ccfae6e13162e63153bb593fdb8f0cf689f061acc24a8c039` |
| E-58 | §12.1.1 | 5963–5986 | EME-PKCS1-v1_5-ENCODE | `5b644374ee85ac04b36e3a860d4babb9d2f61c3f2a2abedf4ac831faa43b3dcf` |
| E-59 | §12.1.2 | 5992–6013 | EME-PKCS1-v1_5-DECODE | `994ce98b0504de80ba65b721903323a268f6a637e52be276258806d9ad39f6e3` |
| E-60 | §12.1.3 | 6017–6063 | EMSA-PKCS1-v1_5 | `2e3860ee0207e2022188c45edb6512d9c67087b2deb116ed951fd51239c5f840` |

### `fields.verbatim.txt` — field lists (F)

| id | section | source lines | content | sha256 |
|---|---|---|---|---|
| F-01 | §5.1.1 | 1269–1291 | v3 PKESK fields | `c58160ca3a3fd422351a6a079a52ff9bb9e030ceebd884d39a93436529dfc8e7` |
| F-02 | §5.1.2 | 1299–1321 | v6 PKESK fields | `b736d51a98752433624a965a829f15163e6802f774c9140c46dfb490621a4a7c` |
| F-03 | §5.1.3 | 1325–1325 | RSA PKESK fields | `ca96dc70841d9e04362202e81b73190c0ad011f3b278950e593a0140d42e58ba` |
| F-04 | §5.1.4 | 1351–1353 | Elgamal PKESK fields | `37bd1c0830213502669943dd632b55d3cf18fe419a2219dedceb4a2028cd34c1` |
| F-05 | §5.1.5 | 1381–1386 | ECDH PKESK fields | `1ba476711bdc10d0847df9bd2015a932e3703d1835609a7f546127971e6c8248` |
| F-06 | §5.1.6 | 1390–1397 | X25519 PKESK fields | `dac3bdc70911a72b7f2bbf9265021cf5acf9181773944ad815a04c6a3cd649b7` |
| F-07 | §5.1.7 | 1424–1431 | X448 PKESK fields | `13b4356f5636ef22e3a848e9940c2e4592ab0fcd6aaac8fff943840eb3911b42` |
| F-08 | §5.2.2 | 1655–1674 | v3 Signature fields | `7b88f502c7a3049ed5d1f3a1198a45b24f99e61b0b305216624dd06704e58ac7` |
| F-09 | §5.2.2 | 1683–1691 | v3 Signature algorithm-specific fields | `ed5a8f04167cf1451909ab7dd9fb876ea338824b9a12963946c0b08950639834` |
| F-10 | §5.2.3 | 1700–1739 | v4 and v6 Signature fields | `17180d45ca13e02d4cee6023d50803c3298575ad09f5d3637c0b2ec798d31cac` |
| F-11 | §5.2.3.1 | 1743–1743 | RSA signature fields | `ca0d36f0f2761e5fa68686a34f6c262d375a07763117e0dc9e9c0a742ffe3fb5` |
| F-12 | §5.2.3.2 | 1754–1756 | DSA or ECDSA signature fields | `dec43421606d9846df779a8fc428fef229170862efb635378324ee432610d90d` |
| F-13 | §5.2.3.3 | 1779–1780 | EdDSALegacy signature fields | `0765b8c4716adde6a45df51c31d6c112795b8843e6d0d3b1ebd5edd1fa7a1198` |
| F-14 | §5.2.3.3.1 | 1793–1801 | Ed25519Legacy signature fields | `72c4107694764e7d3c4123c55ad45901aa3b358b8ccab026702c759682a60b7d` |
| F-15 | §5.2.3.4 | 1808–1808 | Ed25519 signature fields | `cd14c214bbf5b3585c761771630c64e662cba3f233635430be0e9adbac0a932c` |
| F-16 | §5.2.3.5 | 1822–1822 | Ed448 signature fields | `03b82df501f4a09ecbdae637fcda5a2f9ea022167087ed07d301001b6aa686a8` |
| F-17 | §5.2.3.11 | 2144–2144 | body, Signature Creation Time | `52b50dd00ba0688343e117bb248479f9f9d5384680ae346fa0d9885e88d21e12` |
| F-18 | §5.2.3.12 | 2154–2154 | body, Issuer Key ID | `249a35c08aa8b4c67d48ed08337e0516207191ac663ab95bd26e8c70b128507d` |
| F-19 | §5.2.3.13 | 2166–2166 | body, Key Expiration Time | `52b50dd00ba0688343e117bb248479f9f9d5384680ae346fa0d9885e88d21e12` |
| F-20 | §5.2.3.14 | 2180–2180 | body, Preferred Symmetric Ciphers for v1 SEIPD | `d5d3af5f23df7e09c5f99363e77f7204c24b97a6cea7fc83472fa2bf6d3bf36b` |
| F-21 | §5.2.3.15 | 2195–2196 | body, Preferred AEAD Ciphersuites | `678a38a306498bdf9083b0a9907c4cf347129ef0051e14a70f26fb46c9e8285b` |
| F-22 | §5.2.3.15 | 2198–2211 | Preferred AEAD Ciphersuites semantics | `f5323fcbb1017639dc4fda39e598b2cd263ec5e1cdaddcfac6775a8916902afa` |
| F-23 | §5.2.3.16 | 2235–2235 | body, Preferred Hash Algorithms | `d5d3af5f23df7e09c5f99363e77f7204c24b97a6cea7fc83472fa2bf6d3bf36b` |
| F-24 | §5.2.3.17 | 2244–2244 | body, Preferred Compression Algorithms | `d5d3af5f23df7e09c5f99363e77f7204c24b97a6cea7fc83472fa2bf6d3bf36b` |
| F-25 | §5.2.3.18 | 2255–2255 | body, Signature Expiration Time | `52b50dd00ba0688343e117bb248479f9f9d5384680ae346fa0d9885e88d21e12` |
| F-26 | §5.2.3.19 | 2266–2266 | body, Exportable Certification | `67c6bcd3c84f9740bc8b4d56f98e63dbaaff1cca5207ff8f7c155aa6d54f0f2a` |
| F-27 | §5.2.3.20 | 2300–2300 | body, Revocable | `afc7708c44f7f6fc294171901adc75b63ece2102b014a880feb767e187c1778d` |
| F-28 | §5.2.3.21 | 2311–2311 | body, Trust Signature | `d7b868761ae36905c5ac65f3130ec699e33be777d909407885daae7a6e484acf` |
| F-29 | §5.2.3.22 | 2329–2329 | body, Regular Expression | `106dd8246e8a8ad3f41c6e02e41ae7bc54210e0b609970a03a405495bfbb9eaf` |
| F-30 | §5.2.3.22 | 2342–2348 | Regular Expression null terminator | `e41fb2255a42b4730ed09e66639285d45a5296efa1ff36e751676caceef79bfa` |
| F-31 | §5.2.3.23 | 2354–2355 | body, Revocation Key | `a48ae53f6de964d2bcb727f192629ae4703314d3d810293da843d62da9230532` |
| F-32 | §5.2.3.23 | 2367–2373 | Revocation Key class octet | `eff60c10ec4db7dce49ec44aec732006acde5eb27af17a0660e2e2c504bf9df9` |
| F-33 | §5.2.3.24 | 2387–2388 | body, Notation Data | `61286da90493fe19afab83754ad8766f7c15bea6dcf6f80cca1f5f344c7bd4a0` |
| F-34 | §5.2.3.24 | 2390–2397 | notation flags | `e0c17d1092a36ce8dd55dbf372c403f49f5b0552aa365792eaefffd0fdc241cc` |
| F-35 | §5.2.3.24 | 2409–2414 | notation namespaces | `0db7bafe23b45db420ff8b58fcd7b37c31eafcaca9fb03364173c1c47d28de1e` |
| F-36 | §5.2.3.24 | 2425–2430 | user namespace names | `b8853fa2adf0565ad37b1b64032e5ea154680e53a3c4b5c7995136a99c61a8cb` |
| F-37 | §5.2.3.25 | 2447–2447 | body, Key Server Preferences | `4c931d95c527939020d3ab638ee37d163fa038b01f0c42292ad6f2b4263acefb` |
| F-38 | §5.2.3.25 | 2449–2451 | key server preference flags | `ebbe28b0c68dfe30d731ab796d793f232e83244a4be2534eafb65fbefdaa558f` |
| F-39 | §5.2.3.26 | 2467–2467 | body, Preferred Key Server | `05257afe9b31471513348cbe44be592a688684841cf4842815ff5d9605bdcada` |
| F-40 | §5.2.3.27 | 2477–2477 | body, Primary User ID | `5b5e79fe403814d4cc76024460716e1a3b4b4a792c71e6532b1d68f0b997e701` |
| F-41 | §5.2.3.28 | 2497–2497 | body, Policy URI | `05257afe9b31471513348cbe44be592a688684841cf4842815ff5d9605bdcada` |
| F-42 | §5.2.3.29 | 2504–2504 | body, Key Flags | `4c931d95c527939020d3ab638ee37d163fa038b01f0c42292ad6f2b4263acefb` |
| F-43 | §5.2.3.29 | 2506–2510 | key flags octet string | `d288ac5d42dea150e65818445ec04f9e91aeb7c81babe64a85a59475b7e30fc3` |
| F-44 | §5.2.3.30 | 2565–2565 | body, Signer's User ID | `05257afe9b31471513348cbe44be592a688684841cf4842815ff5d9605bdcada` |
| F-45 | §5.2.3.31 | 2578–2578 | body, Reason for Revocation | `d9deca7649d4dd40024c3207b2579b6480f74fa545ee8e77fe0f79aa2dbfdd8d` |
| F-46 | §5.2.3.31 | 2611–2618 | reason string | `7568eede837a39c837f739f55242cb962022ee9c5e25928cf4a1cd47cf1b0ca9` |
| F-47 | §5.2.3.32 | 2636–2636 | body, Features | `4c931d95c527939020d3ab638ee37d163fa038b01f0c42292ad6f2b4263acefb` |
| F-48 | §5.2.3.32 | 2638–2642 | features flags | `6ac4d4f3cb76bb7cd6b32243568166e501ea6b88801898ba333f3766ef7843c1` |
| F-49 | §5.2.3.33 | 2680–2680 | body, Signature Target | `976053c6f051789e687cf085873c410778c853c8e446cfcdd722df0ce3e353ba` |
| F-50 | §5.2.3.33 | 2689–2691 | target hash length | `be46ba451a090c715bdc6703eb4b146e3b863ac1d85d6055e51435d2004da4e5` |
| F-51 | §5.2.3.34 | 2695–2695 | body, Embedded Signature | `d82c9e3af7f2d01fcfb6dea11db98f60cfa07f8f579776276a58265c387ac17f` |
| F-52 | §5.2.3.35 | 2703–2703 | body, Issuer Fingerprint | `c88cb63de90c47ab534ef8d1bcb92d9f023617bf2f19b56ab520c323bbcb2c5b` |
| F-53 | §5.2.3.35 | 2712–2717 | fingerprint length and version octet | `96a9008eab678307f18329ff837fb887d838c0fb38125fdc657ee8b097527b4c` |
| F-54 | §5.2.3.36 | 2721–2721 | body, Intended Recipient Fingerprint | `c88cb63de90c47ab534ef8d1bcb92d9f023617bf2f19b56ab520c323bbcb2c5b` |
| F-55 | §5.2.3.36 | 2730–2731 | fingerprint length | `8196249544b1fa7a494d2e7ee39ee5def34781bb5ec7a6d61cab242eecc693fd` |
| F-56 | §5.3.1 | 2923–2947 | v4 SKESK fields | `eeea4f663e9779a33c0e72060c4743d70f2a4cd7d19a142bbdb67b9e743bace2` |
| F-57 | §5.3.2 | 2960–2980 | v6 SKESK fields | `4277f18ac2123928e9d82dacad5442c9c8467ef75a381938d5ed9b72cba8708c` |
| F-58 | §5.4 | 3008–3039 | One-Pass Signature fields | `bf89d5c1bbab53d2d119e2d089c339444b4e1327e48d087baa9ebd132dcb0282` |
| F-59 | §5.5.2.1 | 3109–3125 | v3 public key fields | `66b9f4cd634b90ff4d6b037cb006aa10b01c6b06ef24d7d4041fca582b319720` |
| F-60 | §5.5.2.2 | 3145–3154 | v4 public key fields | `fea6e50ab54f59e8a8ce436db841cac4b2d7da03b1f671b55c42ed4f5bdc3f55` |
| F-61 | §5.5.2.3 | 3165–3177 | v6 public key fields | `8adbbfb1065fadbc9ddf43eeb0b31c298a9daf55b219e7749dbd65b555278b87` |
| F-62 | §5.5.3 | 3185–3242 | secret key fields | `cf11ec07954afbd4d6b2d43be9c319ba40b2339426cc138aa4ac2f66f7f1bef8` |
| F-63 | §5.5.5.1 | 3428–3443 | RSA key material | `31c36f6bc98b6ce86eca2135ff29103006ab943024495ffaea0fb7e9cc33ad40` |
| F-64 | §5.5.5.2 | 3447–3460 | DSA key material | `578a101a75cf248c27c560cd21dddbf8a6380b8c0ac8ec60179383e00a573ae5` |
| F-65 | §5.5.5.3 | 3464–3475 | Elgamal key material | `78026f469775072b230d20bc0514424751f56773aa800f65f068bc2fc833318c` |
| F-66 | §5.5.5.4 | 3479–3494 | ECDSA key material | `f57f42be28cffde710b37a81d1879a68f01921b3d38bf29e7d799aba4dbf0cd7` |
| F-67 | §5.5.5.5 | 3498–3516 | EdDSALegacy key material | `f280cea5d5a205100f1d706891ac454da01b38cd567bc20fe8e7d0e4c963c6e0` |
| F-68 | §5.5.5.6 | 3532–3562 | ECDH key material | `59b6f5011774578a5be9d98854c96712d45a10aeda9c9c619d25cb03201e4b4f` |
| F-69 | §5.5.5.6.1 | 3566–3570 | ECDH secret key material | `429790af38ef3a5dbb194310466530e066af319f03e5440552be3c0d39dc1baf` |
| F-70 | §5.5.5.6.1.1 | 3574–3577 | Curve25519Legacy secret key material | `ab0c9a681e1b64f7e83d7a438960d46b84fdb6be81b0b777eb53d53a6b7b9882` |
| F-71 | §5.5.5.7 | 3599–3611 | X25519 key material | `8dda59213ddf13f26f248bfd5272d38cc1bd41be8460869cf5c757af752d2001` |
| F-72 | §5.5.5.8 | 3615–3626 | X448 key material | `2740d1b570e13a0b08a4867ff41833d56a44f3e8ef6becffade46a0fb06ff65e` |
| F-73 | §5.5.5.9 | 3630–3640 | Ed25519 key material | `ae02d43b05613bfce5e49f67bfc19178f504d259cb7b2ef80e2323fbafdfcbb1` |
| F-74 | §5.5.5.10 | 3644–3654 | Ed448 key material | `13d078ac6d06999bae4e8d32729fcbab81055d6f523d1ac219ddc28a8b90ce7d` |
| F-75 | §5.6 | 3663–3680 | Compressed Data fields | `ffdfd7fad85436c6c2f0c9c69c3f5e9ec9fbfc854e9132480cf1f0232bbec043` |
| F-76 | §5.7 | 3711–3719 | Symmetrically Encrypted Data fields | `76e758d0df8203946d394f9d174388d2d53f5ff5feb374823d4a5db52af5d8e7` |
| F-77 | §5.8 | 3755–3757 | Marker fields | `5495fc5c4cf07a1ab03ad30547a9554279b080c86525fe2c4e543f3e539d084b` |
| F-78 | §5.9 | 3766–3806 | Literal Data fields | `ac71de26b6ad093877f33960974c04ce10ce993e79319322704dd7a69ddb5706` |
| F-79 | §5.10 | 3858–3863 | Trust packet | `9e223c58548ecbb7bf464f67835b98787473ca563ec97597a595c739d4cc2c13` |
| F-80 | §5.11 | 3871–3875 | User ID packet | `94fb02e3a310faf07bbd3e17dce7d6dd1154ecf45ee6585383716a137b2470fb` |
| F-81 | §5.12 | 3893–3901 | User Attribute subpacket header | `33b63bc106bdbf6928d44254106bc36b6bfcc9d2ad2321b3e07b8d5027741c41` |
| F-82 | §5.13.1 | 4000–4006 | v1 SEIPD fields | `2ce2f0b4fdf3c4d78fa540c13c9dd380c3f8a728321edce239dffc6cd56e0e88` |
| F-83 | §5.13.2 | 4110–4127 | v2 SEIPD fields | `d17b21dd864f0e763cbafc36fbff69e74880347b7ab4f554ced91526836a23b8` |

**Prose sections with formal content that is not tabulated separately**,
because their structure is carried by the regions above:

- §3.3, Key IDs (E-34, E-35, T-12);
- §5.2.1.1–§5.2.1.16, the meanings of the signature types (T-04);
- §5.2.3.8–§5.2.3.10, notes on subpackets and self-signatures;
- §5.14, Padding, which has no fields beyond its body.

## Findings

Inconsistencies and gaps in the source. Nothing is repaired in any verbatim
file. Line numbers are source lines. Quotes are verbatim, with each line break
and the indent after it read as one space. Where a derived file had to choose
a reading, the finding says which.

**SF-01 — Table 3 has no rows for Packet Type IDs 15 and 16.** The table goes
from 14 (line 1200) straight to 17 (line 1203). §4.3 makes 0–39 critical
(lines 1143–1144), so 15 and 16 are critical IDs whose status (reserved or
unassigned) is not stated. *Derived:* the schema treats them as unknown
critical IDs, and a stream that contains one fails.

**SF-02 — Table 5 has no row for Subpacket Type ID 36, and none for 40–99 or
111–127.** The table goes from 35 (lines 1987–1988) to 37 (line 1990). The
status of these IDs is unstated. *Derived:* they are not in the registry
enum.

**SF-03 — Subpacket lengths are not encoded "similarly to" packet lengths.**
§5.2.3.7 says the length “is encoded similarly to a 1-octet, 2-octet, or
5-octet OpenPGP format packet header” (lines 1882–1883). Its decoding rule
then takes the 2-octet form for “the 1st octet >= 192 and < 255” (line 1890).
In packet headers, 224–254 are Partial Body Lengths (§4.2.1.4) and the
2-octet form stops at 223. So subpacket lengths up to 16319 have a 2-octet
form, and packet lengths do not. *Derived:* the decoder follows line 1890.

**SF-04 — "only used in v3 PKESK packets" is wrong about Key IDs.** §5.5.4
says “the Key ID (which is only used in v3 PKESK packets; see Section 5.1.1)
is always 64 bits” (lines 3322–3323). Key IDs are also fields of the v3
Signature (line 1665), the v3 One-Pass Signature (lines 3029–3030) and the
Issuer Key ID subpacket (§5.2.3.12, line 2154).

**SF-05 — "2-bit count octets" should read "2-octet".** §11.3.2: “the first
three octets of the MPI (the 2-bit count octets plus the prefix octet)”
(lines 5712–5713).

**SF-06 — The cleartext header line is not in the Armor Header Lines
registry.** Table 16 (lines 4358–4374) lists four header lines. §7.1 uses
“-----BEGIN PGP SIGNED MESSAGE-----” (line 4497), which is in no table.
*Derived:* `text-formats.derived.abnf` gives it its own rule,
`cleartext-signed`.

**SF-07 — "the Embedded Signature" in §6.2.2.3 is ambiguous.** The sentence
is “a verifying application MUST ignore its contents, deferring to the hash
algorithm indicated in the Embedded Signature” (lines 4458–4460). An
Embedded Signature is a subpacket (§5.2.3.34). The hash algorithm meant is
presumably the one in the Signature packet of the cleartext-signed message
(inferred).

**SF-08 — Table 18 leaves two PKESK cells empty instead of N/A.** Ed25519 (27)
and Ed448 (28) have empty PKESK Format cells (lines 4744–4751). The other
signature-only algorithms say “N/A”. *Derived:* `x-encrypt: false` for both.

**SF-09 — The v4 certificate structure has no Padding, but §10.1.5 discusses
v4 Padding.** The v4 structure (lines 5235–5240) ends with the subkeys.
§10.1.5 says “if the Public Key packet is a version 4 key, the optional
Padding packet SHOULD NOT be present unless the recipient has indicated that
they are capable of ignoring it successfully” (lines 5341–5343). That
sentence assumes v4 Padding exists. *Derived:* `v4-certificate` follows the
printed structure; `--padding-anywhere` accepts v4 Padding.

**SF-10 — Where Padding may appear is stated three different ways.**

- The grammars place it only at the end of a v6 certificate (line 5206) and
  of an Optionally Padded Message (lines 5394–5395).
- Detached signatures allow it anywhere (lines 5541–5542).
- §5.14: “An implementation MUST be able to process Padding packets anywhere
  else in an OpenPGP stream” (lines 4232–4233).

The top-level OpenPGP Message grammar has no Padding at all. *Derived:* by
default the ABNF follows the grammars. `validate.derived.py
--padding-anywhere` applies §5.14 (R-0239).

**SF-11 — How many binding signatures follow a subkey, and in what order.**

- The v6 and v4 structures print “Subkey Binding Signature...”, one or more
  (lines 5205, 5240), and §10.1.1 (line 5215) and §10.1.3 (line 5245) say
  “at least one”.
- §10.1.5: “Each Subkey packet MUST be followed by one Signature packet”
  (line 5326).
- The structures put the subkey revocations *before* the bindings
  (lines 5204, 5239), while §10.1.5 says “Subkey and Key packets may each be
  followed by a Revocation Signature packet” (line 5333).

*Derived:* the ABNF follows the printed structures,
`subkey *subkey-revocation 1*subkey-binding`.

**SF-12 — The revocation and certification parts differ between structure
versions.**

- v6 allows repeated primary-key revocations, “[Revocation Signature...]”
  (line 5199). v4 and v3 allow at most one, “[Revocation Signature]”
  (lines 5236, 5265).
- The v6 structure orders each identity's certification revocations before
  its certifications (lines 5202–5203). v4 has only “[Signature...]”
  (line 5238), and §10.1.5 says only “zero or more Signature packets”
  (lines 5300–5301).

*Derived:* each version's rule follows its own printed structure.

**SF-13 — The message grammar has an undefined nonterminal and no stated
precedence.**

- “Corresponding Signature Packet” (line 5389) is never defined in the
  grammar. The correspondence is given in §5.4 (G-01, lines 3048–3052).
- The rule “Signed Message: Signature Packet, OpenPGP Message | One-Pass
  Signed Message.” (lines 5391–5392) needs comma-over-bar precedence, which
  the notation sentence (lines 5368–5369) does not state.

*Derived:* comma binds tighter, and `corresponding-signature` is a named rule
whose field agreement the validator checks.

**SF-14 — "Optionally Padded Message" cannot be reached from "OpenPGP
Message".** It is defined in the grammar (lines 5394–5395) but used only by
§10.3.1's unwrapping rule for v2 SEIPD (lines 5405–5407). *Derived:* it is
rendered as a separate start rule for decrypted v2 SEIPD content.

**SF-15 — The Primary User ID Boolean has no stated encoding.** The body is
“(1 octet, Boolean)” (line 2477). Exportable Certification and Revocable spell
theirs out as “0 for not, 1 for …” (lines 2266, 2300). *Derived:* the schema
admits any octet for subpacket 25 and restricts 4 and 7 to 0 and 1.

**SF-16 — Block sizes and key sizes are not tabulated.** Table 21 gives
cipher names only. Several rules depend on the block size:

- the CFB IV is “of the same length as the cipher's block size” (lines
  3223–3225);
- EAX, OCB and GCM “can only use block ciphers with 16-octet blocks” (lines
  4190, 4198, 4207);
- the SED and v1 SEIPD prefixes are block size + 2 (lines 3713–3716,
  4017–4018).

*Derived and marked inferred:* `x-block-octets` is taken from the cited cipher
specifications, and `x-key-bits` from the algorithm names. The validator uses
the block sizes to split the IV in CFB-protected secret keys. Digest lengths
are likewise inferred, except that SHA-1 = 20 is stated (lines 2690–2691).

**SF-17 — "The Public Key packet occurs first" (§10.1.5, line 5282) does not
cover a Transferable Secret Key.** In a Transferable Secret Key the first
packet is a Secret Key packet. The adaptation is made only by reference in
§10.2 (lines 5353–5356). *Derived:* `primary-key = PUBKEY / SECKEY`.

**SF-18 — The v6 revocation certificate omits the Direct Key signature that
the v6 certificate requires.** §10.1.1 requires one or more Direct Key
signatures (line 5200), and R-0098 says one must be present before a v6 key is
used. §10.1.2 (lines 5225–5229) drops it and gives the reason. This is not a
defect, but it takes a second start rule, `v6-revocation-certificate`.

**SF-19 — Subpacket 35's name differs.** §5.2.3.7 calls it “the "Intended
Recipients Fingerprint" (35) subpacket” (line 2008). The heading (line 2719)
and Table 5 (lines 1987–1988) say “Intended Recipient Fingerprint”.

**SF-20 — The OPS nested flag defines only zero.** “A zero value indicates
that the next packet is another One-Pass Signature packet” (lines 3037–3038).
The meaning of a non-zero value is implied, never stated. *Derived:* the
validator checks only that zero is followed by an OPS.

**SF-21 — The v6 PKESK fingerprint length is defined only for v4 and v6
keys.** The size octet covers “the following two fields” (line 1303), but N
is given only for v4 (20) and v6 (32) (lines 1310–1311). *Derived:*
`key_info_length` is one of 0, 21 or 33.

**SF-22 — What a consumer does with a chunk size above 16 is not stated.**
§5.13.2 says an implementation “MUST accept chunk size octets with values
from 0 to 16” and “MUST NOT create” larger ones (lines 4177–4179). *Derived:*
the schema admits 0–255 and does not reject above 16.

**SF-23 — The secret-key field list says "multiprecision integers", but four
algorithms store fixed-length octets.** §5.5.3 says “Plain or encrypted
multiprecision integers comprising the secret key data” (line 3227). X25519,
X448, Ed25519 and Ed448 secret keys are fixed-length octet strings, not MPIs
(§5.5.5.7–§5.5.5.10, F-71 to F-74).

**SF-24 — The Salted S2K row of Table 1 conflicts with the rule under the
table.** The row's "Generate?" cell reads "Only when string is high entropy"
(the cell text of lines 645–647, joined). The rule says “If "Yes" is not present in the "Generate?"
column, the S2K entry is used only for reading in backward-compatibility mode
and SHOULD NOT be used to generate new output” (lines 665–668). Read
literally, Salted S2K is never generated. §3.7.2 allows it when the input is
known to be high entropy (lines 799–802).

**Checked and found consistent** (by script, not by eye):

- every curve OID's DER encoding against its printed octets and its "OID Len"
  (Table 19);
- every Full Hash Prefix of Table 24, rebuilt as DER of `DigestInfo` from the
  OID and the digest length;
- the ECDH KDF parameter sizes stated in §11.5 (54/51/55/56 for v4, 66/63/67
  for v6), recomputed from Table 19 and the field list;
- the EC point MPI sizes of §11.2.3 (515, 771, 1059, 1027, 263);
- the additional-data examples of §5.3.2 (`C3 06 07 02`), §5.5.3 (`C5 04`,
  `C7`) and §5.13.2 (`D2 02 07 01 10`), recomputed from the header bit figure
  (E-12);
- the field sizes in Table 1 (2, 10, 11, 20 octets) against the octet layouts
  (E-05 – E-08);
- every registry enum in the schema against the ID column of its table, by
  script.

## What is not rendered

- **The cryptographic computations.** None is executable here:
  - the S2K key derivation (§3.7.1.x);
  - HKDF key separation (§5.3.2, §5.5.3, §5.13.2);
  - AEAD chunking and nonces (§5.13.2);
  - CFB and the MDC (§5.7, §5.13.1);
  - the ECDH KDF and key wrap (§11.4, §11.5);
  - PKCS#1 (§12.1);
  - the signature hashed-data stream (§5.2.4).

  Their layouts are verbatim (E regions), but no verifier is derived.
  Appendix A's intermediate values belong to the examples artifact.
- **Semantic validity.** Expiry, revocation, key-flag and preference
  semantics, trust signatures and regular-expression matching are protocol
  and state-machine material. The `text-formats` ABNF parses §8 regular
  expressions but does not match them against anything.
- **Producer rules.** The MUST NOT / SHOULD NOT generate rules are cited, not
  enforced (see above).
- **Trust packet contents.** These are “defined by a given implementation”
  (lines 3862–3863).
- **Opaque bodies.** Private and experimental algorithm parameters
  (100–110) are kept as raw `body` hex.
- **IANA registration policies** (§15.5), and every Reserved or unassigned
  registry value.

## Reproducing

```sh
# from the library root
python3 -I records/ietf/rfc-9580/distilled/schema/validate.derived.py \
    --rfc .cache/rfc-9580.txt
```

To re-extract a region, take source lines `a..b` of `.cache/rfc-9580.txt`
with their line feeds, compare them byte for byte with the text between the
region's markers, and compare the sha256 with the one in the region header:

```python
# python3 -I check.py .cache/rfc-9580.txt FILE.verbatim.txt
import hashlib, re, sys
src = open(sys.argv[1], 'rb').read().split(b'\n')
t = open(sys.argv[2], 'rb').read()
pat = (rb'^==== (\S+)  Section [\d.]+, ".*"  source lines (\d+)-(\d+)\n.*\n'
       rb'     sha256 ([0-9a-f]{64})\n---- BEGIN VERBATIM \1 ----\n(.*?)'
       rb'---- END VERBATIM \1 ----$')
for m in re.finditer(pat, t, re.M | re.S):
    a, b, body = int(m[2]), int(m[3]), m[5]
    ok = body == b''.join(l + b'\n' for l in src[a - 1:b])
    ok &= hashlib.sha256(body).hexdigest() == m[4].decode()
    print(m[1].decode(), 'ok' if ok else 'MISMATCH')
```

**Run in this pass, 2026-10-13. All hold.**

1. A generator extracted the 196 regions. A separate checker, written apart
   from the generator, re-derived every region and found:
   - the bytes equal the source range and the digests match;
   - the section label equals the nearest numbered heading above the first
     line;
   - BEGIN and END markers pair up, and each file's stated region count is
     right.

   The generator itself also asserted that no heading falls inside a region,
   that no region starts or ends on a blank line, and that no two regions in
   a file overlap.
2. `jsonschema` 4.10.3 `Draft202012Validator.check_schema` accepts the
   schema. Every `x-verbatim` id resolves to a region, and every
   `x-requirements` id exists in `requirements.yaml`.
3. `validate.derived.py --rfc` decodes all 14 armored blocks of Appendix A
   (A.1–A.7, A.8.5, A.9.5, A.10.5, A.11.5, A.12.1–A.12.3). All are
   schema-valid, all match their grammar rule, and all pass the cross-field
   checks. Its fingerprints equal the ones printed in A.1 and A.3.
4. 31 mutation cases (wrong salt size, missing creation time, partial length
   on a non-data packet, type 0, an unknown critical type, Argon2 bounds, a v6
   legacy curve, a weak hash with Ed25519, a v6 cert without a DKS, an OPS
   salt mismatch, and others) are each rejected by the schema or the
   validator, as the case expects. Two cases check acceptance: a non-critical
   type and a trailing v6 Padding packet.
5. Both ABNF files load in the `abnf` 2.2.0 parser with `strict=True` and give
   the results listed in the mapping table.
6. No file here contains a to-do marker (checked with `grep`).

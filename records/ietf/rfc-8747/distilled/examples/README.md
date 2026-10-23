---
record: rfc-8747
kind: examples
title: "rfc-8747 — examples and test vectors"
extracted: "2026-10-21"
reviewed_by: ""
---

# RFC 8747 — examples, byte-exact

**What this file is.** Every example RFC 8747 prints, reproduced as an exact run
of source lines with its line range and its own `sha256`. `vectors.yaml` beside
it carries the decoded values, the octet counts and the expected results;
nothing is retyped in either file — each fenced block below was lifted from
`.cache/rfc-8747.txt` by line range by script.

| | |
|---|---|
| **Source** | `.cache/rfc-8747.txt`, 683 newline-delimited lines, **0 form feeds** |
| **Digest** | `9b695379f119f9675828d054f1b0e76014c06c9a59dccef8bb417e0420272dda` |
| **Examples** | **4** printed examples and **1** printed scalar value, in §3.2, §3.3 (three of them) and §3.4 |
| **Vectors** | **6** — `V-0001` to `V-0006`; 4 printed, 1 printed scalar folded into `V-0004`, 1 constructed control |

**Region convention.** Each digest is the sha256 of the region's lines joined by
a newline with **no trailing newline** — this effort's established convention.
The source has **zero** form feeds, so no region can contain page decoration and
there are no running headers or footers to exclude. Built with `split` on a
newline, never `splitlines`.

**Why the byte-exact copies are here and not in `vectors.yaml`.** A YAML literal
block scalar is read **with** its trailing newline by `bin/_record_yaml.py` and
**without** it by `bin/_yaml.py`. Five of this record's regions tripped that
difference when they lived in the YAML, so the YAML now carries the line range,
the digest and the source-text octet count, and the bytes live in this fence
where nothing rewrites them.

**Notation.** §2 declares it: the examples are in CBOR extended diagnostic
notation, and *include line breaks for readability*. Two of the breaks fall
**inside a hex literal** (§3.2 at lines 219-220 and 221-222, §3.3 at lines
251-252), so a fixture builder must remove them before decoding. No break in any
example falls at a hyphen.

---

## §3.2 — CWT Claims Set with an asymmetric `COSE_Key` (`V-0001`)

The `COSE_Key` encodes to **75 octets**, the `cnf` value to **77**, the whole Claims Set to **143**. The point `(x, y)` **satisfies the P-256 curve equation** — checked, not assumed. Entry order `1, -1, -2, -3` **is** RFC 8949 §4.2.1 deterministic.

```
    {
    /iss/ 1 : "coaps://server.example.com",
    /aud/ 3 : "coaps://client.example.org",
    /exp/ 4 : 1879067471,
    /cnf/ 8 :{
      /COSE_Key/ 1 :{
        /kty/ 1 : /EC2/ 2,
        /crv/ -1 : /P-256/ 1,
        /x/ -2 : h'd7cc072de2205bdc1537a543d53c60a6acb62eccd890c7fa27c9
                   e354089bbe13',
        /y/ -3 : h'f95e1d4b851a2cc80fff87d8e23f22afb725d535e515d020731e
                   79a3b4e47120'
       }
     }
   }
```

*Source `.cache/rfc-8747.txt` lines 211-225 · `sha256:1bfad338032427de80a8441ed86481c76d0d8b440e2e03b9239ff9d7d7932c5f`*

## §3.3 — the symmetric `COSE_Key`, as printed (`V-0002`)

Encodes to **40 octets**: `a3010403052058206684523ab17337f173500e5728c628547cb37dfe68449c65f885d1b73b49eae1`. Entry order `1, 3, -1` **is** §4.2.1 deterministic. Read `V-0004` before using this as the plaintext of the ciphertext below.

```
   {
    /kty/ 1 : /Symmetric/ 4,
    /alg/ 3 : /HMAC 256-256/ 5,
    /k/ -1 : h'6684523ab17337f173500e5728c628547cb37df
               e68449c65f885d1b73b49eae1'
   }
```

*Source `.cache/rfc-8747.txt` lines 248-253 · `sha256:29dae4b7e8e0360e534fd2ce8b6d6f5bd43c26ce93372661688609f958fc4408`*

## §3.3 — CWT Claims Set with an `Encrypted_COSE_Key` (`V-0003`)

The `COSE_Encrypt0` is a **bare three-element array — untagged**, in a document whose own §7.2.2 registry entry allows a tag. Untagged it is **71 octets**; tagged it would be **72**, a difference of **1 octet**. The whole Claims Set is **138 octets**.

Note the annotation on the protected-header line: it is the **only place in the document where a backslash appears**, and all four of the document's backslashes are on that one line.

```
   {
    /iss/ 1 : "coaps://server.example.com",
    /sub/ 2 : "24400320",
    /aud/ 3: "s6BhdRkqt3",
    /exp/ 4 : 1311281970,
    /iat/ 5 : 1311280970,
    /cnf/ 8 : {
    /Encrypted_COSE_Key/ 2 : [
       /protected header/ h'A1010A' /{ \alg\ 1:10 \AES-CCM-16-64-128\}/,
       /unprotected header/ { / iv / 5: h'636898994FF0EC7BFCF6D3F95B'},
       /ciphertext/  h'0573318A3573EB983E55A7C2F06CADD0796C9E584F1D0E3E
                       A8C5B052592A8B2694BE9654F0431F38D5BBC8049FA7F13F'
      ]
     }
   }
```

*Source `.cache/rfc-8747.txt` lines 261-275 · `sha256:3f71d9d396475c26b4da7d11193a44e35002f525a15c2d0cecae134f25552bc1`*

## §3.3 — the generating key (`V-0004`)

**16 octets.** Under this key, the §3.3 IV and `Enc_structure` = `8368456e63727970743043a1010a40`, the printed ciphertext **decrypts and the 8-octet CCM tag verifies**. Re-encrypting the recovered plaintext reproduces all **48** printed octets exactly.

**The recovered plaintext is not the COSE_Key printed above.** It carries the same three pairs with the same values in the order `3, 1, -1` rather than `1, 3, -1`. See `vectors.yaml` → `source_defects` → `rfc-8747#D-0001`.

```
   The example above was generated with the key:

   h'6162630405060708090a0b0c0d0e0f10'
```

*Source `.cache/rfc-8747.txt` lines 277-279 · `sha256:e013429ac4a68103f8bcb33a2ab1560165471ac773b54b9c3c4470ee73fd5ac1`*

## §3.4 — CWT Claims Set with a bare `kid` (`V-0006`)

A **16-octet** `kid`; the `cnf` value is **19 octets** against `V-0001`'s **77** for the same job — a ratio of **4.05**. Nothing in the document lets a recipient check this value against a key.

```
   {
    /iss/ 1 : "coaps://as.example.com",
    /aud/ 3 : "coaps://resource.example.org",
    /exp/ 4 : 1361398824,
    /cnf/ 8 : {
      /kid/ 3 : h'dfd1aa976d8d4575a0fe34b96de2bfad'
     }
   }
```

*Source `.cache/rfc-8747.txt` lines 295-302 · `sha256:a21740431a81b2ba13e6af47bcd876185cf1f364f78148f115174e3fea6b5785`*

---

## What reproduced, and what did not

| | |
|---|---|
| AES-128 gated on FIPS 197 C.1 | **pass** before use |
| AES-CCM gated on RFC 3610 vector 1 | **pass** before use |
| §3.2 point on P-256 | **pass** |
| §3.3 ciphertext authenticates under the stated key | **pass** |
| §3.3 ciphertext reproduces from the recovered plaintext | **pass**, all 48 octets |
| §3.3 ciphertext reproduces from the **printed** COSE_Key | **FAIL** — source defect `D-0001` |
| every printed map in §3.2, §3.3 and §3.4 in §4.2.1 order | **pass** for all five printed maps |
| the **encrypted** §3.3 COSE_Key in §4.2.1 order | **no** — order `3, 1, -1` |

No CBOR, COSE or cryptography library was used: the codec is written from RFC
8949 §3 and the cipher from FIPS 197, both for this pass, so a shared library
bug cannot hide behind these numbers. Every count in this file and in
`vectors.yaml` is asserted against its re-derivation at write time.

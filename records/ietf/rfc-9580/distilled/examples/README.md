---
record: rfc-9580
kind: examples
title: "rfc-9580 — examples and test vectors"
extracted: "2026-10-13"
reviewed_by: ""
---

# RFC 9580 — examples and test vectors

RFC 9580 defines a **data format**, not a wire protocol. Every vector here is
an object: a packet, a packet sequence, an armor block or a field. Each one
states what a conforming producer must emit, or what a conforming consumer
must accept, reject or compute from it. No vector involves a peer, a session
or message ordering in time.

This directory holds **39 fixture files**. Together they are every armored
block, hex dump and annotated hex dump in Appendix A. `vectors.yaml` has
**127 vectors**:

- **60 in-source.** The source prints their input. 25 come from Appendix A
  and 35 are examples printed in the body.
- **67 constructed.** Each one tests a rule the source states but gives no
  literal for. Most are byte strings built in scratch from the Appendix A
  keys and messages.

This is pass 1 (extract). It works from the source only:
`.cache/rfc-9580.txt`, 9138 lines, sha256 `36540e57…1eb1ff18`. Line 1 of
that file is a UTF-8 byte order mark, and all line numbers count it as
line 1. Pass 1 did not read `summary.md` or any other extraction output,
except `requirements.yaml` for R-ids.

Every vector carries `in_source`, `fidelity`, `constrained_by` (R-ids) and
`verified`. Anything this extraction computed sits under `derived:` with
`in_source: false`. The header of `vectors.yaml` documents every field.

## Fixtures

Each fixture is the source lines named below, copied verbatim. The only
change is that the block's common indent is removed from each non-blank
line: 3 spaces, or 6 for the A.1 and A.2 packet dumps. Lines end in LF, and
one LF follows the last line. Blank lines inside armor stay empty. No
character is altered, and **no binary file is committed**. `vectors.yaml →
fixtures` records the sha256 of each file, plus the decoded octets (length,
sha256 and full lowercase hex):

- for `.asc`, the base64 payload;
- for `.hex`, the dumped octets, with the `0xNNNN` offsets checked as they
  are read;
- for `.annotated.txt`, the octet columns of the dump. A row's octets are
  the single-space-separated hex pairs after the offset. The annotation
  starts after a run of two or more spaces.

| file | lines | octets | what |
|---|---|---|---|
| `A.1-v4-ed25519legacy-public-key.hex` / `.asc` | 7601-7604 / 7608-7612 | 53 | v4 EdDSALegacy public key; the dump and the armor differ in header framing (defect 1) |
| `A.2-v4-ed25519legacy-signature.hex` / `.asc` | 7635-7640 / 7644-7648 | 96 | v4 Ed25519Legacy binary signature over "OpenPGP" |
| `A.3-v6-certificate.asc` | 7670-7681 | 424 | v6 Ed25519 primary key, Direct Key signature, X25519 subkey, Subkey Binding signature |
| `A.3.1-direct-key-sig-hashed-data.hex` / `.annotated.txt` | 7691-7710 / 7714-7771 | 159 | hash input of the Direct Key signature |
| `A.3.1-subkey-binding-sig-hashed-data.hex` / `.annotated.txt` | 7776-7798 / 7802-7854 | 184 | hash input of the Subkey Binding signature |
| `A.4-v6-secret-key.asc` | 7868-7881 | 490 | the same key, unprotected secrets |
| `A.5-v6-locked-secret-key.asc` | 7895-7910 | 600 | the same key, secrets locked with Argon2 + AES-256-OCB |
| `A.6-cleartext-signed-message.asc` | 7953-7967 | 154 (signature) | cleartext signed message, dash-escaped |
| `A.6-signature-packet.annotated.txt` | 7971-8007 | 154 | the A.6 signature packet |
| `A.6-signed-data.hex` / `.annotated.txt` | 8011-8030 / 8034-8069 | 160 | salt, canonical text and trailer that A.6 signs |
| `A.7-inline-signed-message.asc` | 8082-8091 | 302 | One-Pass Signature, Literal Data, Signature |
| `A.8.1-v6-pkesk-x25519.hex` / `.annotated.txt` | 8103-8114 / 8118-8138 | 95 | v6 PKESK to the X25519 subkey |
| `A.8.3-v2-seipd-ocb.hex` / `.annotated.txt` | 8181-8194 / 8198-8220 | 107 | v2 SEIPD, AES-128-OCB |
| `A.8.5-x25519-aead-ocb-message.asc` | 8283-8290 | 202 | A.8.1 followed by A.8.3 |
| `A.9.1-v6-skesk-eax.hex` / `.annotated.txt` | 8301-8309 / 8313-8333 | 66 | v6 SKESK, AES-128-EAX |
| `A.9.3-v2-seipd-eax.hex` / `.annotated.txt` | 8365-8378 / 8382-8404 | 107 | v2 SEIPD, EAX |
| `A.9.5-aead-eax-message.asc` | 8460-8466 | 173 | A.9.1 followed by A.9.3 |
| `A.10.1-v6-skesk-ocb.hex` / `.annotated.txt` | 8477-8485 / 8489-8509 | 65 | v6 SKESK, AES-128-OCB |
| `A.10.3-v2-seipd-ocb.hex` / `.annotated.txt` | 8541-8554 / 8558-8580 | 107 | v2 SEIPD, OCB |
| `A.10.5-aead-ocb-message.asc` | 8636-8642 | 172 | A.10.1 followed by A.10.3 |
| `A.11.1-v6-skesk-gcm.hex` / `.annotated.txt` | 8653-8660 / 8664-8683 | 62 | v6 SKESK, AES-128-GCM |
| `A.11.3-v2-seipd-gcm.hex` / `.annotated.txt` | 8715-8728 / 8732-8754 | 107 | v2 SEIPD, GCM |
| `A.11.5-aead-gcm-message.asc` | 8810-8816 | 169 | A.11.1 followed by A.11.3 |
| `A.12.1` / `A.12.2` / `A.12.3-v4-skesk-argon2-aes{128,192,256}.asc` | 8828-8835 / 8839-8847 / 8851-8859 | 105 / 113 / 121 | v4 SKESK with Argon2, then v1 SEIPD |

The intermediate values that Appendix A prints are not separate files: secret
keys, the hash input `m`, digests, Argon2 and HKDF outputs, shared points,
nonces and additional data. They sit in `expected:` of their vector as
`{hex, lines}`. The checker re-reads all 83 of these values from those lines.

## What was verified, and how

All of it was run locally, and nothing was fetched. The tools were
Python 3.12 with **cryptography 41.0.7** (Ed25519, X25519, HKDF-SHA256,
RFC 3394 key wrap, AES-OCB3, AES-GCM, AES-CFB, AES-CTR, CMAC),
**libargon2.so.1** through ctypes for Argon2id, `hashlib`, and **GnuPG
2.4.4**.

- **(a) Re-extraction.** Every fixture re-extracts byte for byte from its
  source lines.
- **(b) Armor.** Every armor block decodes as strict base64. No body line is
  longer than 76 characters (R-0240). **No armor block in the source has a
  CRC24 footer.** That is right for every v6 object (R-0247 to R-0250), and
  the v4 objects in A.1, A.2 and A.12 omit it as well. So no printed CRC
  exists to check. Instead, the §6.1.1 C code was transcribed to Python and
  checked three ways:
  - `crc24("")` is `b704ce`, the initial value.
  - `crc24("123456789")` is `21cf02`, the published CRC-24/OpenPGP check
    value.
  - On the A.1, A.2 and A.12.1 octets it gives the same footers that
    `gpg --enarmor` writes: `=zD4a`, `=e4KH` and `=uIks`.
- **(c) Framing.** Every packet header parses. Every body length adds up to
  the fixture length, and every annotated offset was checked against the
  running count. That check found the offset and column defects listed
  below. Each plain dump equals its annotated dump. Each `.asc` message
  equals the concatenation of its two packet dumps (A.8, A.9, A.10, A.11),
  and the A.2 dump equals the A.2 armor.
- **(d) Recomputation.** Every intermediate value the source prints was
  recomputed and equals the printed value:
  - **Fingerprints:** SHA-1 for v4 (A.1), SHA2-256 for v6 (A.3 primary and
    subkey). They also match every Issuer Fingerprint subpacket, the OPS
    fingerprint and the PKESK recipient fingerprint.
  - **Signatures:** A.2 is Ed25519 over SHA2-256 of the printed `m`. A.3's
    two self-signatures are Ed25519 over SHA2-512 of the A.3.1 streams; the
    streams were rebuilt from the packets, not just read. A.6 and A.7 are
    Ed25519 over SHA2-512 of the dash-unescaped, CR LF-canonicalised text.
    In every case the left-16 field equals the digest's first two octets.
  - **Key correspondence:** the A.4 secrets derive the A.3 public keys, and
    the A.1 `D` derives `q`.
  - **A.5:** Argon2id(t=1, p=4, m=2^21 KiB) gives the printed S2K material.
    HKDF gives the printed KEK. The printed additional data is
    `0xC5`/`0xC7` followed by the public packet body. AES-256-OCB then
    decrypts each A.5 key to the A.4 secret.
  - **A.8:** X25519 in both directions gives the printed shared point.
    HKDF("OpenPGP X25519") gives the printed key-wrap key. AES-128 key
    unwrap gives the printed session key.
  - **A.9–A.11:** Iterated and Salted S2K (SHA2-256, count 0xff =
    65,011,712 octets) gives the printed derived key. HKDF gives the KEK,
    and EAX, OCB or GCM opens the ESK to the printed session key.
  - **All four v2 SEIPD packets:** HKDF gives the printed message key and
    IV. Chunk 0 decrypts to the printed Literal Data and Padding packets
    with the printed nonce and AAD. The final tag verifies with the printed
    final nonce and AAD.
  - **EAX** has no library implementation, so it was written in scratch
    over AES-CTR and AES-CMAC (OMAC with tweaks 0, 1, 2). The EAX tags
    verifying is the check.
  - **A.12:** Argon2id decrypts each v4 SKESK (AES-CFB, zero IV) to the
    cipher octet and the session key that the Comment header states. The
    v1 SEIPD then decrypts: the quick-check octets repeat, the MDC
    (`d3 14` + SHA-1) matches, and the payload is Literal Data
    "Hello, world!".
- **GnuPG 2.4.4**, as an independent check where it can act:
  - `--list-packets` reads A.1 and A.2. It gives Key ID `8CFDE12197965A9A`,
    creation times 1408458507 and 1442406293, and MPI sizes of 263, 255 and
    256 bits.
  - The A.1 key packet was given a constructed User ID and self-signature
    in a scratch keyring. gpg then printed the fingerprint as
    `C959 BDBA FA32 A2F8 9A15  3B67 8CFD E121 9796 5A9A`, the source's
    grouping character for character. It reported **Good signature** for
    A.2 over "OpenPGP" and **BAD signature** over "OpenPGQ".
  - **gpg 2.4.4 does not support v6.** It reports every A.3–A.11 key,
    signature, PKESK, SKESK and SEIPD packet as "unknown version" 6, and it
    rejects S2K type 4 ("unknown S2K mode 4"). So it cannot check
    A.3–A.12.
  - It also cannot read the **armored** A.2, A.5 and A.12.1 blocks. Each
    payload is a multiple of 3 octets (96, 600 and 105), so the base64
    ends without `=` padding. There is no CRC24 line either, and gpg reads
    on into the `-----END` line ("invalid radix64 character 2D skipped").
    This is gpg's behaviour, not a fixture fault: the base64 is exact.
    R-0244 says a reader must not depend on the footer. A.12.2 and A.12.3
    end in `=` padding, and gpg dearmors them correctly. The dearmored
    bytes were used for the gpg checks.
- **The checker** (scratch `verify.py`, not committed) re-runs all of the
  above from the committed files and source alone:
  - it re-extracts every fixture;
  - it re-reads every printed value from its lines;
  - it locates all 176 quoted strings in the source, within the vector's
    `source.lines`;
  - it regenerates all 127 vectors from the committed fixtures and compares
    them with `vectors.yaml`, which must be identical;
  - it checks the counts.

  The Ed25519 signatures that the constructed vectors carry reproduce
  exactly, because Ed25519 is deterministic. Re-signing the unchanged A.6
  data with the A.4 key reproduces the A.6 signature byte for byte.

### Not verified

- **Ed448, X448, RSA, DSA, Elgamal, ECDSA, ECDH (NIST and brainpool) and
  Curve25519Legacy:** the source prints no example for any of them, so they
  have only structural vectors (Tables 19 and 24, §11.5 sizes and layouts).
  The §11.5 KDF, the ECDH key wrap and EMSA/EME-PKCS1 were not run against
  any source value. PGP-1213-C01 and PGP-1212-C01…C04 are constructed and
  checked only against the §12.1 steps.
- **Compressed Data, SED, v3 keys and signatures, User ID and User
  Attribute certifications, Trust packets:** no source example, and no
  constructed bytes beyond what is listed below.
- **The v4 AEAD secret-key additional data of §5.5.3** (`C5 04 …`): the
  source has no AEAD-locked v4 key, so only the v6 form is checked (A.5).
- **Behavioural outcomes of constructed vectors**, such as "rejected" or
  "declined". No conforming implementation was available to run them (gpg
  lacks v6). Their bytes and cryptographic properties were checked (the
  signature verifies, the tag fails, and so on). The outcome itself is the
  quoted rule's.
- **The §5.2.3.10 and §12.2 preference scenarios** are reasoning. Nothing
  was computed for them beyond encoding the lists.

## Vectors

| source | in source | constructed | ids |
|---|---|---|---|
| Appendix A.1, A.2 | 2 | 0 | `PGP-A1-01`, `PGP-A2-01` |
| Appendix A.3, A.3.1, A.4, A.5 | 6 | 0 | `PGP-A3-01`, `PGP-A31-01`, `-02`, `PGP-A4-01`, `PGP-A5-01`, `-02` |
| Appendix A.6, A.7 | 2 | 0 | `PGP-A6-01`, `PGP-A7-01` |
| Appendix A.8–A.11 (ESK, SEIPD, whole message, for each of X25519/OCB, EAX, OCB, GCM) | 12 | 0 | `PGP-A8-01` … `PGP-A11-03` |
| Appendix A.12 | 3 | 0 | `PGP-A12-01` … `-03` |
| §3.2 MPIs | 4 | 1 | `PGP-032-01` … `-04`; `PGP-032-C01` |
| §3.7.1.1, §3.7.1.3 S2K | 0 | 4 | `PGP-0371-C01`, `PGP-03713-C01` … `-C03` |
| §3.7.1.4 Argon2 | 1 | 5 | `PGP-03714-01`; `PGP-03714-C01` … `-C05` |
| §3.7.2.1, §5.5.3 secret-key protection | 1 | 2 | `PGP-0553-01`; `PGP-03721-C01`, `PGP-0553-C01` |
| §4.1, §4.2.1, §4.2.2, §4.2.3 framing | 4 | 8 | `PGP-0423-01` … `-04`; `PGP-041-C01`, `PGP-0421-C01` … `-C06`, `PGP-042-C01` |
| §4.3 criticality, §5.8 Marker, §10.1.5 Padding | 1 | 4 | `PGP-058-01`; `PGP-043-C01`, `-C02`, `PGP-058-C01`, `PGP-1015-C01` |
| §5.1.6 X25519 PKESK | 0 | 1 | `PGP-0516-C01` |
| §5.2.3, §5.2.3.4, §5.2.3.6, §5.2.3.7, §5.2.3.12, §5.2.3.35, §5.2.5 signatures | 0 | 9 | `PGP-0523-C01`, `-C02`, `PGP-05234-C01`, `PGP-05236-C01`, `PGP-05237-C01`, `PGP-053212-C01`, `PGP-053235-C01`, `PGP-0525-C01`, `-C02` |
| §5.2.3.10, §5.2.3.15, §5.2.3.24, §5.2.3.33 subpackets | 4 | 0 | `PGP-05310-01`, `PGP-05315-01`, `PGP-05324-01`, `PGP-05333-01` |
| §5.2.3.21 Trust Signature, §5.2.3.22 Regular Expression, §5.2.3.29 Key Flags | 0 | 9 | `PGP-053221-C01` … `-C05`, `PGP-053222-C01` … `-C03`, `PGP-053229-C01` |
| §5.3.2, §5.13.2 additional data | 2 | 0 | `PGP-0532-01`, `PGP-05132-01` |
| §5.5.4.2, §5.5.4.3 fingerprints, §14 | 2 | 2 | `PGP-05542-01`, `PGP-05543-01`; `PGP-05542-C01`, `PGP-14-C01` |
| §5.5.5.6.1.1 Curve25519Legacy secret | 0 | 1 | `PGP-055561-C01` |
| §5.7, §5.13.1 quick check | 2 | 0 | `PGP-057-01`, `PGP-05131-01` |
| §5.9 Literal Data, §5.12.1 image header | 1 | 1 | `PGP-05121-01`; `PGP-0591-C01` |
| §5.13.2 chunking, §13.7 AEAD failure | 0 | 3 | `PGP-05132-C01`, `PGP-137-C01`, `-C02` |
| §6, §6.1 armor and CRC24 | 0 | 3 | `PGP-06-C01`, `PGP-061-C01`, `-C02` |
| §6.2.2.3, §7.1, §7.2 cleartext framework | 0 | 5 | `PGP-0622-C01`, `-C02`, `PGP-071-C01`, `-C02`, `PGP-072-C01` |
| §8 regular expressions | 1 | 0 | `PGP-08-01` |
| §9.2 curve OIDs (Table 19), §9.5 hash prefixes (Table 24) | 3 | 1 | `PGP-092-01`, `-02`, `PGP-095-01`; `PGP-092-C01` |
| §10.3.2.1 ESK and payload versions | 0 | 2 | `PGP-10321-C01`, `-C02` |
| §11.2.3, §11.3.1, §11.3.2 EC wire formats | 3 | 0 | `PGP-1123-01`, `PGP-1131-01`, `PGP-1132-01` |
| §11.5 ECDH KDF and key wrap | 5 | 0 | `PGP-115-01` … `-05` |
| §12.1.2, §12.1.3 PKCS#1 | 0 | 5 | `PGP-1212-C01` … `-C04`, `PGP-1213-C01` |
| §12.2 algorithm preferences | 1 | 1 | `PGP-122-01`; `PGP-122-C01` |
| **total** | **60** | **67** | **127** |

### The constructed vectors, by rule

| rule | vectors | outcome |
|---|---|---|
| v6 left-16 bits must match (R-0076) | `PGP-05236-C01` | rejected, though Ed25519 verifies |
| Issuer Fingerprint version ≠ signature version (R-0160) | `PGP-053235-C01` | malformed: ignored, not valid, stream continues |
| Issuer Key ID in a v6 signature (R-0103) | `PGP-053212-C01` | non-conforming producer; consumer result **ambiguous** |
| unknown critical / non-critical hashed subpacket (R-0080, R-0081, §5.2.5) | `PGP-0525-C01`, `PGP-05237-C01` | ignored for validation; valid |
| salt length ≠ Table 23 (R-0060); control with a correct salt | `PGP-0523-C01`, `-C02` | malformed; valid |
| Ed25519 with a 224-bit digest (R-0071) | `PGP-05234-C01` | rejected, though Ed25519 verifies |
| v4 signature by a v6 key (§5.2.5, R-0344) | `PGP-0525-C02` | ignored for validation |
| Hash header conformant / non-conformant; other cleartext Armor Header (R-0259, R-0260, R-0267) | `PGP-0622-C01`, `-C02`, `PGP-071-C01` | verifies; declined; declined |
| trailing whitespace; missing dash-escape (R-0266, R-0273) | `PGP-071-C02`, `PGP-072-C01` | verifies; signature fails |
| AEAD tag failure; truncation (R-0406, R-0408) | `PGP-137-C01`, `-C02` | no plaintext released; error |
| three 64-octet chunks, chunk size octet 0 (R-0234) | `PGP-05132-C01` | decrypts |
| v4 SKESK before v2 SEIPD; v6 SKESK before v1 SEIPD (R-0339, R-0340, R-0343) | `PGP-10321-C01`, `-C02` | ESK discarded; not decryptable |
| unknown critical (22) / non-critical (40) packet; Marker; trailing Padding (R-0032, R-0033, R-0209, R-0328) | `PGP-043-C01`, `-C02`, `PGP-058-C01`, `PGP-1015-C01` | sequence rejected; ignored; ignored; ignored |
| length boundaries, partial powers of two, first partial < 512, partial on a Signature, final partial, non-minimal 5-octet, Legacy indeterminate, overrun (R-0020…R-0031, R-0335) | `PGP-0421-C01` … `-C06`, `PGP-042-C01`, `PGP-041-C01` | as stated per vector |
| v4 MPI bit-count mismatch (R-0003 is v6 only) | `PGP-032-C01` | **ambiguous** |
| S2K coded counts; count below salt+passphrase; key longer than one hash context needs | `PGP-03713-C01` … `-C03`, `PGP-0371-C01` | computed keys |
| Argon2 t = 0, p = 0, encoded_m 4 / 5 / 32 with p = 4 (R-0008, R-0009) | `PGP-03714-C01` … `-C05` | malformed except encoded_m 5 |
| Argon2 under usage 254; v6 usage 255 (R-0018, R-0191) | `PGP-03721-C01`, `PGP-0553-C01` | rejected |
| Trust Signature levels and amounts 0/0, 1/60, 1/119, 1/120, 2/120 (R-0115…R-0120) | `PGP-053221-C01` … `-C05` | as stated |
| Regular Expression with and without NUL, critical and not (R-0123, R-0126…R-0128) | `PGP-053222-C01` … `-C03` | scoped; signature rejected; subpacket ignored |
| Key Flags shorter than expected (R-0143); AES-128 implicit in intersection (R-0373, R-0375) | `PGP-053229-C01`, `PGP-122-C01` | zero-filled; AES-128 |
| CRC24 present and correct / wrong on a v6 certificate; 76-column rewrap and whitespace (R-0240, R-0241, R-0244, R-0249) | `PGP-061-C01`, `-C02`, `PGP-06-C01` | accepted (producer violated R-0249 in the first) |
| v4 key one second later; v4 Ed25519 (27) key (§14, §5.5.4.2) | `PGP-14-C01`, `PGP-05542-C01` | different fingerprint; computed fingerprint |
| curve25519Legacy_MPI_from_random (R-0199…R-0202) | `PGP-055561-C01` | 00 FF prefix, value in range and divisible by 8 |
| EMSA-PKCS1-v1_5 with SHA2-256; EME decode with valid / bad first octet / short PS / no separator (R-0367, R-0369…R-0372) | `PGP-1213-C01`, `PGP-1212-C01` … `-C04` | EM; M; decryption error ×3 |
| X25519 v3 PKESK with cipher 2 (R-0040); v6 key with a legacy OID (R-0286); Literal format 't' (R-0211) | `PGP-0516-C01`, `PGP-092-C01`, `PGP-0591-C01` | invalid; rejected; read as UTF-8 |

## Count reconciliation

**60 in-source.**

- **25 in Appendix A.** Every subsection that prints an object has a vector.
  A.1, A.2, A.3, A.4, A.6 and A.7 have one each. A.3.1 has two, one per
  signature. A.5 has two, one per locked key, carrying A.5.1 and A.5.2.
  A.8–A.11 have three each: the ESK packet with its decryption, the SEIPD
  packet with its decryption, and the complete armored sequence. A.12 has
  three. The 39 fixtures are every block those subsections print. No block
  in Appendix A is left out.
- **35 in the body.** Each is a value or octet string printed with a stated
  meaning or result. Statements that name a field without printing a value
  are not counted: the "(example)" labels of §5.5.4.2 and §5.5.4.3 are
  folded into their vectors. The Alice and Bob scenarios of §5.2.3.10 and
  §12.2 are counted because they state a result for named inputs.
- **Body examples not made into vectors.** These are pseudocode or
  formulas, not example values: the §6.1.1 CRC24 code (used to check
  armor), the §11.4 KDF synopsis, the §11.5 encoding synopsis, and the
  §5.13.2 chunk-size formula (exercised by every SEIPD vector). The
  "Hello, world!" Literal Data and Padding values of A.8.4–A.11.4 are
  inside their SEIPD vectors. The §13 attack narratives (Alice and Mallet,
  TWOFISH, JKS02) state no input and no result.

**67 constructed.** By section:

| 3.x | 4.x | 5.1–5.2 | 5.5–5.9 | 5.13, 13.7 | 6–7 | 9–12, 14 |
|---|---|---|---|---|---|---|
| 11 | 10 | 19 | 5 | 3 | 8 | 11 |

## Sections with no vector, and why

- **§1, §2, §3.1, §3.3–§3.6:** no example values. Key IDs are exercised in
  `PGP-A1-01` and `PGP-05543-01`, and time fields in every Appendix A
  vector.
- **§5.1.3–§5.1.5, §5.1.7, §5.2.2, §5.2.3.1–§5.2.3.3, §5.5.2.1,
  §5.5.5.1–§5.5.5.6, §5.5.5.8, §5.5.5.10:** RSA, Elgamal, DSA, ECDSA, ECDH,
  X448 and Ed448 keys, signatures and ESKs, and v3 keys and signatures. The
  source prints no instance. Building them here would rest on algorithms
  this artifact could only check against itself. They belong in an
  interoperability corpus, which is out of scope.
- **§5.4:** covered by A.7.
- **§5.6, §5.10, §5.11, §5.12:** no example. No example in Appendix A
  carries a User ID. A.3 is a v6 certificate without one, which R-0099
  permits. R-0324 says a Transferable Public Key SHOULD include a User ID
  "unless storage requirements prohibit this", and the source gives no such
  reason for A.3.
- **§9 tables other than 19 and 24:** these are constants, and they belong
  to the schema artifact. Tables 19 and 24 are here because their octet
  columns can be recomputed.
- **§10 grammar:** exercised by the Appendix A sequences and the
  constructed sequence vectors. The grammar itself belongs to the protocol
  and state-machine artifacts.
- **§12.3–§12.11, §13 (except §13.7), §15, Appendix B, Appendix C:** no
  example values.

## Source defects (recorded, not repaired)

1. **A.1, lines 7601-7612.** The hex dump is introduced as "the entire
   Public Key packet", and the armor as "the same packet". The dump frames
   the packet with a **Legacy** header, `98 33`, and the armor with an
   **OpenPGP-format** header, `c6 33`. The bodies are identical
   (`PGP-A1-01`).
2. **A.3.1, line 7735.** "hash ago: SHA2-512" should read "hash algo".
3. **A.6, line 7986.** The signature packet dump labels a row `0x001a`. The
   row starts at offset `0x0018`.
4. **A.7, lines 8082-8091.** The Literal Data packet has format `u` but
   stores bare LF line endings. §5.9 says text data MUST be stored with
   CR LF (R-0213). The signature still verifies, because type 0x01
   canonicalises before hashing. An implementation that enforces R-0213 on
   input would flag the source's own example (`PGP-A7-01`).
5. **A.8.3, line 8219.** "S0x0060" has a stray `S`.
6. **A.9.3, line 8388.** The salt row is labelled `0x0005`. It starts at
   `0x0006`.
7. **A.10.1, line 8500, and A.11.1, line 8681.** An octet sits one column
   off its position in the annotated dump. This is cosmetic: offsets and
   octets are right.
8. **A.11.3, line 8713.** "following series of octets, is:" has a stray
   ", is".
9. **§5.2.3.15, line 2218.** The example `09 02 09 03 13 02` is said to
   include "Camellia-256 with OCB". Camellia-256 is ID 13 **decimal**, which
   is `0x0D`. Read as hex, like every other octet string in the document,
   `13` is algorithm 19, which is unassigned. The vector is marked
   `ambiguous` (`PGP-05315-01`).
10. **§11.3.2, lines 5712-5713.** "the 2-bit count octets" should read "the
    2-octet bit count".

Two further points are recorded as ambiguities, not defects. R-0103
constrains only producers, so a verifier's handling of an Issuer Key ID in
a v6 signature is open (`PGP-053212-C01`). R-0003 makes the MPI bit-count
check mandatory for v6 packets only (`PGP-032-C01`).

The line 7735 typo ("hash ago") and the line 8219 stray "S0x0060" were
listed in the brief. Defects 1, 3, 4, 6, 7, 8, 9 and 10 are new. The checker
found 3, 6 and 7 mechanically, from offset and column bookkeeping on the
annotated dumps. It found 1 by comparing the dump octets with the armor.

## Pass 3 cross-check

Pass 3 compared this directory with `messages.yaml`, `requirements.yaml`
and `schema/`. It checked four things:

- **Structures against `messages.yaml`.** Every decoded fixture packet and
  every structure vector was matched to a `messages.yaml` entry, and its
  field widths were checked against that entry's `layout`. That covers the
  hash inputs, the HKDF info, the AEAD additional data, the KDF Param, the
  key-wrap input and the PKCS#1 encodings.
- **Annotated dumps.** Every label in the 12 `.annotated.txt` dumps was
  matched to a field, and every label's width was checked against the
  layout.
- **R-ids.** Every R-id cited here and in `vectors.yaml` exists in
  `requirements.yaml`.
- **Constructed vectors.** Every binary constructed vector was run through
  `schema/validate.derived.py`. The checks of pass 1 were repeated on them:
  the Ed25519 signatures and their left-16 fields, the AEAD tags, the S2K
  outputs, the PKCS#1 and Curve25519Legacy outputs, the fingerprints and
  the cleartext message digests.

Five constructed vectors had a second defect besides the rule they test.
A reader could reject them for the wrong reason, so they were rebuilt. Each
rebuilt vector carries `derived.pass3_rebuild`, which says why. Because of
these rebuilds, the pass-1 checker's regenerated output no longer matches
`vectors.yaml` for these five vectors:

- `PGP-0525-C02`: a v4 signature by a v6 key. The old bytes also carried a
  v6 Issuer Fingerprint, which is malformed in a v4 signature (R-0160).
- `PGP-03721-C01`: Argon2 under usage 254. The old bytes kept the
  usage-253 layout. Read under usage 254 they hold no Argon2 specifier, so
  R-0018 was not exercised.
- `PGP-0553-C01`: a v6 key with usage 255. The old bytes kept the
  usage-253 layout, so the packet was malformed in structure before
  R-0191 applied.
- `PGP-0421-C03` and `PGP-0421-C04`: bad partial-length framing. The old
  bodies were all zero octets, which gives an invalid Literal Data format
  and an unknown signature version 0.

In two places the validator disagreed with a vector's stated outcome. Both
were tooling gaps, the vectors were correct, and pass 3 closed both gaps:

- On `PGP-05237-C01` the schema rejected the unassigned non-critical
  subpacket type 40, but R-0081 says to ignore it. The schema now keeps an
  unassigned non-critical subpacket as an opaque body.
- On `PGP-0622-C02` the validator did not flag the non-conformant Hash
  header (R-0259). It now checks each item against the Table 23 Text Names.

Every constructed verdict now agrees with the validator. Where the
validator cannot judge a vector, because the check needs cryptography or
the key, it reported no conflicting error. That was the case for
`PGP-05236-C01`, `PGP-0525-C02`, `PGP-137-C01`, `PGP-137-C02` and
`PGP-072-C01`. The lone PKESK and key packets fail only the §10 grammar,
which is expected.

## Reproducing the checks

- A fixture's octets are `decoded.hex` in `vectors.yaml`. Alternatively,
  decode the `.asc` base64, or read a `.hex` dump's pairs after the offset.
- Argon2 needs a library that supports p = 4. libsodium's `crypto_pwhash`
  fixes p = 1, so it cannot reproduce A.5 or A.12. libargon2
  `argon2id_hash_raw(t, m_kib, p, …)` does, at about 0.6 s and 2 GiB per
  call.
- An EAX implementation:
  `N = OMAC0(nonce)`, `H = OMAC1(ad)`, `C = OMAC2(ct)` with
  `OMACt(x) = CMAC(0^15 || t || x)`, `ct = CTR_N(pt)`, `tag = N ^ H ^ C`.

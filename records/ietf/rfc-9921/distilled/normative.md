---
record: rfc-9921
kind: normative
title: "rfc-9921 — normative statements"
extracted: "2026-10-20"
reviewed_by: ""
---

# RFC 9921 — normative text, verbatim

**What this file is.** Every normative statement of RFC 9921, reproduced as an
exact run of source lines with its line range and its own `sha256`, in the
document's own section order. Nothing here is paraphrased and nothing is
retyped: each fenced block was lifted from `.cache/rfc-9921.txt` by line range
by script. Prose outside the fences is this extraction's, and says only where a
statement sits, what it is, and what was measured about it.

| | |
|---|---|
| **Source** | `.cache/rfc-9921.txt`, 1056 newline-delimited lines |
| **Digest** | `ba1c4dbb7b4ea83f517418a9b8963085c0a8b5e5bea0c992089d215579b78f39` |
| **BCP 14 keywords** | **8** — 6 MUST and 2 SHOULD; `bin/bcp14-count`, boilerplate excluded |
| **Formal grammar** | **none.** `CDDL`, `ABNF`, `ASN.1`, `JSON Schema`, `schema` and `grammar` each occur **zero** times |

**Region convention.** Each digest is the sha256 of the region's lines joined by
`\n` with no trailing newline — the convention established by earlier passes in
this effort.

**No pagination to guard against.** This rendering has **zero form feeds** and
no running headers or footers, so no region here can contain page decoration —
unlike the paginated RFCs elsewhere in this library, where four of rfc-8392's
sections had to be quoted as adjacent regions. Line 1 carries a UTF-8 BOM.
Built with `split("\n")`, for consistency with the rest of the library rather
than from necessity.

**Two sentences in this document are each interrupted TWICE by a displayed
block** (§3.1.1: the CBOR diagnostic object at L285-298 and the byte listing at
L302-306; §3.1.2: L330-349 and L353-365). Each therefore has **three**
fragments, not two — pass 2's correction. They are quoted as whole regions
here, so both interruptions are visible; `requirements.yaml` carries each of
the six fragments as its own entry (R-0110/R-0048/R-0049,
R-0111/R-0052/R-0053) and **welds nothing**.

**The two final Appendix A objects are declared, not reproduced.** Each carries
5453 octets of DER as 159 lines of hex, inside 7 and 14 further lines of CBOR
diagnostic notation; the declared regions are therefore 166 and 173 lines, not
159. Reproducing them here would make this file mostly hex. The hex is in
`examples/a1-ttc-timestamp-token.hex` and `examples/a2-ctt-timestamp-token.hex`
with their digests, and every structural claim about them in `examples/` and
`messages.yaml` was produced by decoding those bytes.

---
## Abstract

The scope sentence, and the only place the applicable COSE structures are named outside §1.

**Source lines 17-23** · `sha256:261aec01ffeb858da3a51eccc6d33d2a80596ba8ea6fae9598b1df38186f6da4`

```
Abstract

   This document defines two CBOR Object Signing and Encryption (COSE)
   header parameters for incorporating timestamping based on RFC 3161
   into COSE message structures (COSE_Sign and COSE_Sign1).  This
   enables the use of established timestamping infrastructure per RFC
   3161 in COSE-based protocols.
```

## §1 — Introduction

Kept, though it is motivation, because the second sentence is the claim every cost in
`design-notes.md` is measured against: *existing and widely deployed trust
infrastructure*.

**Source lines 79-88** · `sha256:69e791b9bf7a503ff7c947aae7d17e0d058ca29153114510d499476e720145d4`

```
1.  Introduction

   RFC 3161 [RFC3161] provides a method for timestamping a message
   digest to prove that it was created before a given time.

   This document defines two new CBOR Object Signing and Encryption
   (COSE) [RFC9052] header parameters that carry the TimeStampToken
   (TST) output [RFC3161], thus allowing existing and widely deployed
   trust infrastructure to be used with COSE structures used for signing
   (COSE_Sign and COSE_Sign1).
```

## §1.1 — Use Cases

Two use cases, one per mode, and **two lower-case obligations**: *care must be taken
when choosing the appropriate mode* (source line 94) and *the TST must be included
in the signed statement* (source line 125). The second is the entire reason the TTC
mode exists, and under §1.2 it binds nobody.

**§1.1's second use case is written in SCITT's vocabulary and cites nothing.**
Measured over all 1056 lines: `transparency` 4, `statement` 9, `statements` 1,
`append-only` 1, `transparent statement` 2, and **`SCITT` 0 and `9943` 0**.

**Source lines 90-139** · `sha256:6e8b2fa3ffe384c3f0676c1c41f8430e57a1fb9581226fe087909acc0e97ca16`

```
1.1.  Use Cases

   This section discusses two use cases, each representing one of the
   two modes of use defined in Section 2.  As the security
   characteristics of the two cases differ, care must be taken when
   choosing the appropriate mode for a given application.  See
   Section 5.1 for a discussion on the security of the implementations.

   The primary use case is that of "long-term signatures", i.e.,
   signatures that can still be verified even after the signing
   certificate has expired.  This can address situations where it is
   important to prevent subsequent denial by the signer or to verify
   signatures made using (very) short-term certificates.  To achieve
   this, the document signer acquires a fresh TST for the document's
   signature from a trusted Time Stamping Authority (TSA) [RFC3161] and
   concatenates it with the document.  Later, when a relying party
   verifies the signed document and its associated TST, they can be
   certain that the document was signed _at least_ at the time specified
   by the TSA and that the signing certificate was valid at the time the
   signature was made.

   This primary usage scenario motivates the "COSE, Then Timestamp" mode
   described in Section 2.1.

   The second use case is new.  It is the notarization of a signed
   document by registering it with a transparency service.  This is
   common practice for ensuring the accountability and auditability of
   issued documents, which are typically referred to as "statements" in
   this context.  It is also common practice to only register the signed
   parts of a statement (the "signed statement" portion) with a
   transparency service, in order to reduce the complexity of
   consistency checks at a later stage and to avoid the need to retrieve
   or reconstruct unsigned parts.  Once the signed parts of a document
   have been registered in the append-only log at a transparency
   service, the log entry cannot be changed.  In order to avoid losing
   the TST during the registration process, the TST must be included in
   the signed statement.  To achieve this, the issuer acquires a TST
   from a TSA, includes it in the to-be-signed part of the statement so
   that the resulting signed statement includes the TST, and then
   registers the signed parts (rendering it a "transparent statement").
   Later on, a relying party consuming the transparent statement
   including the TST can be certain that the statement was signed by the
   issuer _at least_ at the time specified by the TSA.  If the issuer's
   signing key has expired (or has been compromised), the authenticity
   of the statement can be ascertained by ensuring that no revocation
   information was made public before the time asserted by the issuer
   and registered at the transparency service.

   This new usage scenario motivates the "Timestamp, Then COSE" mode
   defined in Section 2.2.
```

## §1.2 — Requirements Notation

Quoted because it is what makes the nine lower-case force words in this document
non-binding. **It is deliberately not a `requirements.yaml` entry**: `bin/validate`
recounts those texts with boilerplate stripping *off*, so quoting it there would add
11 phantom keywords.

**Source lines 141-147** · `sha256:996a3292f670281fc8bd2b49995f16e0cb62ae3c96cd6d973a6be032054855b3`

```
1.2.  Requirements Notation

   The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT",
   "SHOULD", "SHOULD NOT", "RECOMMENDED", "NOT RECOMMENDED", "MAY", and
   "OPTIONAL" in this document are to be interpreted as described in
   BCP 14 [RFC2119] [RFC8174] when, and only when, they appear in all
   capitals, as shown here.
```

## §2 — Modes of Use

The two modes, and the rule for deriving the COSE_Sign figures from the COSE_Sign1
ones.

**Source lines 149-158** · `sha256:952e9fdea685e83e4820f63d78b3de0aea96c216e5d1195995ebe5d5a8a7278a`

```
2.  Modes of Use

   There are two different modes of composing COSE protection and
   timestamping, motivated by the usage scenarios discussed above.

   The diagrams in this section illustrate the processing flow of the
   specified modes.  For simplicity, only the COSE_Sign1 processing is
   shown.  Similar diagrams for COSE_Sign can be derived by allowing
   multiple private-key parallelogram boxes and replacing the label
   [signature] with [signatures].
```

## §2.1 — COSE, Then Timestamp (CTT)

Figure 1 is reproduced whole: it is the only place the document draws the TSA
exchange, and it is where the **nonce** appears (3 occurrences in the document, all
in the two figures and §5) — neither appendix request carries one. Note the figure's
own name for the result, `rfc3161-ctt COSE`, against the registered name
`3161-ctt` (§3.1, §6): **a naming defect, 4 occurrences, all inside the two
figures.**

**Source lines 160-200** · `sha256:52399ac97d03a06bb44d6c000d7ae6bd4f33a7e610de55c83f168f36ef3496dd`

```
2.1.  COSE, Then Timestamp (CTT)

   Figure 1 shows the case where the signature(s) field of the COSE
   Signed Message is digested and submitted to a TSA to be timestamped.
   The obtained timestamp token is then added back as an unprotected
   header into the same COSE object.

   This mode is utilized when a record of the timing of the signature
   operation is desired.

   .--------.                                     .-----.
   | Signer |                                     | TSA |
   +--------+----------------------------------.  +-----+-------------.
   |   .-------------. .-----------. .-------. |  |   .-------------. |
   |  / private-key /  | protected | | datum | |  |  / private-key /  |
   | '-----+-------'   '---+-------' '---+---' |  | '------+------'   |
   |       |               |             |     |  |        |          |
   |       +---------------+------------'      |  |        |          |
   |       |                                   |  |       .+.         |
   |       v                  .---------.      |  |      | L | Clock  |
   |  .---------.    .----.   | Message |      |  |       '+'         |
   | |   Sign1   +->+ hash +->+ Imprint +-------->|        |          |
   |  '-+-------'    '----'   '---------'      |  |        v          |
   |    |                      .-------.       |  |    .---------.    |
   |    |                      | nonce +--------->|   | timestamp |   |
   |    |                      '-------'       |  |    '---------'    |
   '----|--------------------------------------'  '---------+---------'
        |                                 .-------------.   |
        +-------------+-----------+       | unprotected |   |
        |             |            |      |   .-----.   |   |
   [protected]    [payload]   [signature] |   | TST |<-----'
        |             |            |      |   '-----'   |
        |             v            v      '------+------'
        |     .-------+------------+-----.       |
         '--->+     rfc3161-ctt COSE     +<-----'
              '--------------------------'

                    Figure 1: COSE, Then Timestamp (CTT)

   In this context, timestamp tokens are similar to a countersignature
   made by the TSA.
```

## §2.2 — Timestamp, Then COSE (TTC)

The two construction bullets are the TTC assembly rule. Figure 2 shows the TST in
the **protected** bucket and `...` in the unprotected one — the exact inverse of
Figure 1.

**Source lines 202-244** · `sha256:227ac9d2e346e0c5910c3d289d1455da195f537f947dd4cd85e3d796741a1b2c`

```
2.2.  Timestamp, Then COSE (TTC)

   Figure 2 shows the case where a datum is first digested and submitted
   to a TSA to be timestamped.

   This mode is used to wrap the signed document and its timestamp
   together in an immutable payload.

   A COSE Signed Message is then built as follows:

   *  The obtained timestamp token is added to the protected headers.

   *  The original datum becomes the payload of the COSE Signed Message.

   .--------.                                     .-----.
   | Signer |                                     | TSA |
   +--------+----------------------------------.  +-----+-------------.
   |   .-------------.          .-------.      |  |   .-------------. |
   |  / private-key /           | nonce +-------->+  / private-key /  |
   | '-+-----------'            '-------'      |  | '------+------'   |
   |   |                       .---------.     |  |        |          |
   |   |  .-------.   .----.   | Message |     |  |        |          |
   |   |  + datum +->+ hash +->+ Imprint +------->+       .+.         |
   |   |  '-+-----'   '----'   '---------'     |  |      | L | Clock  |
   |   |    |                                  |  |       '+'         |
   |   |    |               .-------------.    |  |        |          |
   |   v    v               |  protected  |    |  |        v          |
   |  .-------.             |   .-----.   |    |  |    .---------.    |
   | |  Sign1  +<-----------+   | TST |<----------+   | timestamp |   |
   |  '-+-----'             |   '-----'   |    |  |    '---------'    |
   |    |                   '-------------'    |  |                   |
   '----|--------------------------------------'  '-------------------'
        |                                 .-------------.
        +-------------+-----------+       | unprotected |
        |             |            |      |   .-----.   |
   [protected]    [payload]   [signature] |   | ... |   |
        |             |            |      |   '-----'   |
        |             v            v      '------+------'
        |     .-------+------------+-----.       |
         '--->+     rfc3161-ttc COSE     +<-----'
              '--------------------------'

                    Figure 2: Timestamp, Then COSE (TTC)
```

## §3 — Timestamp Tokens per RFC 3161: COSE Header Parameters

**The design choice this record turns on is in the second sentence.** Two parameters
exist, in the document's words, *To clearly separate their semantics*, so the mode
discriminator **is the header label**. There is no type field inside either value, which means the
discriminator inherits the protection of whichever bucket carries it — and one of
the two buckets is unprotected.

**Source lines 246-252** · `sha256:9100128e1539283d636b584a78103fcdd30ceafa06d3ed5fb67fb0d7dc6f1068`

```
3.  Timestamp Tokens per RFC 3161: COSE Header Parameters

   The two modes described in Sections 2.2 and 2.1 use different inputs
   into the timestamping machinery and consequently create different
   kinds of bindings between COSE and TST.  To clearly separate their
   semantics, two different COSE header parameters are defined as
   described in the following subsections.
```

## §3.1 — `3161-ctt`

Three of the document's eight keywords. The MUST at source line 256 binds the
label to the **unprotected** bucket and to the CTT mode; the MUST at 262 binds
what is hashed; the SHOULD at 270 asks the two algorithms to agree. **Nothing here
constrains the contents of the byte string.**

**Source lines 254-276** · `sha256:3db84a7a94a1374b31fde3d9991874e4643fc8fbc733916a9670348960a35e8c`

```
3.1.  3161-ctt

   The 3161-ctt COSE _unprotected_ header parameter MUST be used for the
   mode described in Section 2.1.

   The 3161-ctt unprotected header parameter contains a DER-encoded TST
   [RFC3161] wrapped in a CBOR byte string (Major type 2).

   The MessageImprint sent in the request to the TSA MUST be

   *  the hash of the CBOR-encoded signature field of the COSE_Sign1
      message, or

   *  the hash of the CBOR-encoded signatures field of the COSE_Sign
      message.

   In either case, to minimize dependencies, the hash algorithm SHOULD
   be the same as the algorithm used for signing the COSE message.  This
   may not be possible if the timestamp token has been obtained outside
   the processing context in which the COSE object is assembled.

   Refer to Sections 3.1.1 and 3.1.2 for concrete examples of
   MessageImprint computation.
```

## §3.1.1 — MessageImprint Computation for COSE_Sign1

**The finding, and it reproduces exactly.** The preimage is the bstr-wrapped
signature *including the heading bytes 0x5840*. Measured in this pass:
`sha256(0x58 0x40 || the 64-octet signature)` = `44C2419D131D53D55584B5DD33B788C24E551C6D44B1AFC8B2B85E6954763B4E`, which is the
printed MessageImprint **byte for byte**. So the CBOR *head* of the `signature`
field is inside a third party's digest preimage, and the COSE signature does not
cover its own head.

The sentence *the bstr-wrapped signature … (including the heading bytes 0x5840) is
used as input* is interrupted by the displayed block. The whole region is quoted
here so the interruption is visible.

**Source lines 278-321** · `sha256:d4e5d05babdd7f2cd3337e25bd5806e6dd02c20bd1433f2aaf521e9bf1f406af`

```
3.1.1.  MessageImprint Computation for COSE_Sign1

   The following illustrates how MessageImprint is computed using a
   sample COSE_Sign1 message.

   Given the COSE_Sign1 message

   18(
     [
       / protected h'a10126' / << {
           / alg / 1:-7 / ECDSA 256 /
         } >>,
       / unprotected / {
         / kid / 4:'11'
       },
       / payload / 'This is the content.',
       / signature / h'8eb33e4ca31d1c465ab05aac34cc6b23d58fef5c083106c4
   d25a91aef0b0117e2af9a291aa32e14ab834dc56ed2a223444547e01f11d3b0916e5
   a4c345cacb36'
     ]
   )

   the bstr-wrapped signature

   58 40                                     # bytes(64)
      8eb33e4ca31d1c465ab05aac34cc6b23
      d58fef5c083106c4d25a91aef0b0117e
      2af9a291aa32e14ab834dc56ed2a2234
      44547e01f11d3b0916e5a4c345cacb36

   (including the heading bytes 0x5840) is used as input for computing
   the MessageImprint.

   When using SHA-256, the resulting MessageImprint is

   SEQUENCE {
     SEQUENCE {
       OBJECT IDENTIFIER sha-256 (2 16 840 1 101 3 4 2 1)
       NULL
       }
     OCTET STRING
       44 C2 41 9D 13 1D 53 D5 55 84 B5 DD 33 B7 88 C2
       4E 55 1C 6D 44 B1 AF C8 B2 B8 5E 69 54 76 3B 4E
     }
```

## §3.1.2 — MessageImprint Computation for COSE_Sign

**Sharper than §3.1.1, and the document does not say so.** The preimage is the whole
`signatures` array. Measured: the array as printed is **77 octets**, of which **13
are not the signature** — the array heads, the protected-header bstr `43 a10126`
and the per-signature **unprotected** map `a1 04 42 3131` (`kid` = `'11'`).
`sha256` of those 77 octets is
`803FADA2912D6B7A833A27BD961CC05BC1CC164759B1C56F7AA771E4E21526F7`, the printed
MessageImprint byte for byte. **So in COSE_Sign CTT mode the TSA's digest commits
to an unprotected header field.**

**Source lines 323-379** · `sha256:f8710784b39a7776f9eb1d0099678f4d8c3a816c1cc824ab7680b45810dab366`

```
3.1.2.  MessageImprint Computation for COSE_Sign

   The following illustrates how MessageImprint is computed using a
   sample COSE_Sign message.

   Given the COSE_Sign message

   98(
     [
       / protected / h'',
       / unprotected / {},
       / payload / 'This is the content.',
       / signatures / [
         [
           / protected h'a10126' / << {
               / alg / 1:-7 / ECDSA 256 /
             } >>,
           / unprotected / {
             / kid / 4:'11'
           },
           / signature / h'e2aeafd40d69d19dfe6e52077c5d7ff4e408282cbefb
   5d06cbf414af2e19d982ac45ac98b8544c908b4507de1e90b717c3d34816fe926a2b
   98f53afd2fa0f30a'
         ]
       ]
     ]
   )

   the signatures array

   81                                        # array(1)
      83                                     # array(3)
         43                                  # bytes(3)
            a10126
         a1                                  # map(1)
            04                               # unsigned(4)
            42                               # bytes(2)
               3131                          # "11"
         58 40                               # bytes(64)
            e2aeafd40d69d19dfe6e52077c5d7ff4
            e408282cbefb5d06cbf414af2e19d982
            ac45ac98b8544c908b4507de1e90b717
            c3d34816fe926a2b98f53afd2fa0f30a

   is used as input for computing the MessageImprint.

   When using SHA-256, the resulting MessageImprint is

   SEQUENCE {
     SEQUENCE {
       OBJECT IDENTIFIER sha-256 (2 16 840 1 101 3 4 2 1)
       NULL
       }
     OCTET STRING
       80 3F AD A2 91 2D 6B 7A 83 3A 27 BD 96 1C C0 5B
       C1 CC 16 47 59 B1 C5 6F 7A A7 71 E4 E2 15 26 F7
     }
```

## §3.2 — `3161-ttc`

Three keywords, and the **other** answer to *does the wrapper count*: it does not.
Measured: `sha256('This is the content.')` = 
`09E638D4AA95FD7271866203595303BCE232F462A94D38E393773CD3AAE3F6B0`, which is both
the imprint printed in Appendix A.1's `TimeStampReq` **and** the imprint embedded
in the TSTInfo of the token A.1 prints. Two digests in one document, two written
answers, each reproducible.

**Source lines 381-398** · `sha256:0b0e9b00a239f818f991d5d94a5a7cb9a97a92594d70dd7a0a501606fdd8e4b4`

```
3.2.  3161-ttc

   The 3161-ttc COSE _protected_ header parameter MUST be used for the
   mode described in Section 2.2.

   The 3161-ttc protected header parameter contains a DER-encoded TST
   [RFC3161] wrapped in a CBOR byte string (Major type 2).

   The MessageImprint sent to the TSA (Section 2.4 of [RFC3161]) MUST be
   the hash of the payload of the COSE Signed Message.  This does not
   include the bstr wrapping -- only the payload bytes.  (For an
   example, see Appendix A.1.)

   To minimize dependencies, the hash algorithm used for signing the
   COSE message SHOULD be the same as the algorithm used in the
   MessageImprint [RFC3161].  However, this may not be possible if the
   timestamp requester and the COSE message signer are different
   entities.
```

## §4 — Timestamp Processing

**Where the CBOR verifier acquires an ASN.1/CMS/X.509 stack and a clock.** The
verification obligation is one sentence and it delegates the whole of token
validation to RFC 5652 and RFC 3161, neither of which this library holds.

**A defect in the MUST itself**: *the payload, signature, or signature fields*. The
COSE_Sign case is the `signatures` field, plural, as §3.1 and §3.1.2 both write
it; the third alternative as spelled repeats the second.

**Source lines 400-418** · `sha256:a39a01c6d45e8bbfc82415d64c4531ff578aa0a3ba6f37758f39c13f3a149e54`

```
4.  Timestamp Processing

   Timestamp tokens [RFC3161] use Cryptographic Message Syntax (CMS) as
   the signature envelope format.  [RFC5652] provides details about
   signature verification, and [RFC3161] provides details specific to
   timestamp token validation.  The payload of the signed timestamp
   token is the TSTInfo structure defined in [RFC3161], which contains
   the MessageImprint that was sent to the TSA.  The hash algorithm is
   contained in the MessageImprint structure, together with the hash
   itself.

   As part of the signature verification, the receiver MUST make sure
   that the MessageImprint in the embedded timestamp token matches a
   hash of either the payload, signature, or signature fields, depending
   on the mode of use and type of COSE structure.

   Appendix B of [RFC3161] provides an example that illustrates how
   timestamp tokens can be used to verify signatures of a timestamped
   message when utilizing X.509 certificates.
```

## §5 — Security Considerations

Four of the nine lower-case force words are here, and **the document's answer to
its own conceded attack is one of them**: *In CTT mode, an attacker could manipulate
the unprotected header by removing or replacing the timestamp. To avoid that, the
COSE Signed Message should be integrity protected during transit and at rest.*
Lower case, no mechanism named, and at a layer this document does not define.

**Source lines 420-458** · `sha256:c0d9c64f04d72bff68b581efa54ada56f177b38c23c91ca4982929b3bb136afd`

```
5.  Security Considerations

   Please review the Security Considerations section in [RFC3161]; these
   considerations apply to this document as well.

   Also review the Security Considerations section in [RFC9052].  These
   considerations apply to this document as well, particularly with
   regard to the need for implementations to protect private key
   material.  Additionally, solutions based on the COSE header
   parameters defined in this document must be able to report
   compromised keys promptly.

   The following scenario assumes that an attacker can manipulate the
   clocks on the COSE signer and its relying parties, but not the TSA.
   It is also assumed that the TSA is a trusted third party, so the
   attacker cannot impersonate the TSA and create valid timestamp
   tokens.  In such a setting, any tampering with the COSE signer's
   clock does not have an impact, because once the timestamp is obtained
   from the TSA, it becomes the only reliable source of time.  However,
   in both CTT mode and TTC mode, a denial of service can occur if the
   attacker can adjust the relying party's clock so that the CMS
   validation fails.  This could disrupt the timestamp validation.

   In CTT mode, an attacker could manipulate the unprotected header by
   removing or replacing the timestamp.  To avoid that, the COSE Signed
   Message should be integrity protected during transit and at rest.

   In TTC mode, the TSA is given an opaque identifier (a cryptographic
   hash value) for the payload.  While this means that the content of
   the payload is not directly revealed, to prevent comparison with
   known payloads or disclosure of identical payloads being used over
   time, the payload would need to be armored, e.g., with a nonce that
   is shared with the recipient of the header parameter but not the TSA.
   Such a mechanism is out of scope for this document.

   The resolution, accuracy, and precision of the TSA clock, as well as
   the expected latency introduced by round trips to and from the TSA,
   must be taken into account when implementing solutions based on the
   COSE header parameters defined in this document.
```

## §5.1 — Avoiding Semantic Confusion

**Each mode has its own separate verification algorithm — and neither is written
down.** §4 is the only verification text in the document and it covers both modes
in one sentence. The only discriminator between the two algorithms is which header
label carries the token, and label 270 lives in the bucket §5 has just conceded an
attacker can edit.

Note also that R-0088's prohibition is stated in terms of the **bucket**
(*protected-header payload timestamps*) rather than the label — the only place the
document treats the bucket as the discriminator.

**Source lines 460-478** · `sha256:e0ff2c86c0400bbf420cf845c957fec2a283f21d273ad0a4be15744ca471772b`

```
5.1.  Avoiding Semantic Confusion

   CTT mode and TTC mode have different semantic meanings.  An
   implementation must ensure that the contents of the CTT and TTC
   headers are interpreted according to their specific semantics.  In
   particular, symmetric to the signature and assembly mechanics, each
   mode has its own separate verification algorithm.

   Implementers MUST clearly differentiate between TSA timestamps
   [RFC3161] proving the existence of payload data at an earlier point
   in time (TTC) and timestamps explicitly providing evidence of the
   existence of the cryptographic signature (CTT).  Failure to clearly
   distinguish between these timestamp semantics can result in
   vulnerabilities, such as incorrectly accepting signatures created
   after key revocation based on older payload-only timestamps.
   Validators must not interpret protected-header payload timestamps as
   proof of signature creation time and should rely exclusively on TSA
   timestamps [RFC3161] explicitly covering signature data for
   determining signature validity timing.
```

## §6 — IANA Considerations

**Two centrally allocated labels and no value registry.** Reassembled from the
table: `3161-ttc` label **269**, Value Type `bstr`, Value Registry `-`,
Reference RFC 9921 §3.2; `3161-ctt` label **270**, Value Type `bstr`, Value
Registry `-`, Reference RFC 9921 §3.1. The reassembly is this extraction's — the
verbatim bytes are below and the machine-readable form is in
`schema/header-parameters.derived.yaml`.

**The lower label is the protected one.** 269 is TTC (protected, payload) and 270
is CTT (unprotected, signature), which is the reverse of the order §2 introduces
the modes in.

**Source lines 480-503** · `sha256:221b3dd21bafadd6eff3c5ad68b8c446cb558dbebbd855d4b4073f71937e1ac7`

```
6.  IANA Considerations

   IANA has allocated the COSE header parameters defined in Table 1 in
   the "COSE Header Parameters" registry [IANA.cose_header-parameters]
   as follows:

   +==========+=======+=======+==========+=================+===========+
   | Name     | Label | Value | Value    | Description     | Reference |
   |          |       | Type  | Registry |                 |           |
   +==========+=======+=======+==========+=================+===========+
   | 3161-ttc | 269   | bstr  | -        | Timestamp       | RFC 9921, |
   |          |       |       |          | Token per       | Section   |
   |          |       |       |          | [RFC3161]:      | 3.2       |
   |          |       |       |          | Timestamp,      |           |
   |          |       |       |          | Then COSE       |           |
   +----------+-------+-------+----------+-----------------+-----------+
   | 3161-ctt | 270   | bstr  | -        | Timestamp       | RFC 9921, |
   |          |       |       |          | Token per       | Section   |
   |          |       |       |          | [RFC3161]:      | 3.1       |
   |          |       |       |          | COSE, Then      |           |
   |          |       |       |          | Timestamp       |           |
   +----------+-------+-------+----------+-----------------+-----------+

                    Table 1: New COSE Header Parameters
```

## §7 — Normative References

**Six references, all normative, none informative.** Two of the six are not in this
library and they are where everything the token *means* is defined: RFC 3161 and
RFC 5652 (STD 70). RFC 9052 is STD 96 and is held as `records/ietf/rfc-9052`. The
IANA registry is cited live, with no version and no retrieval date.

**Source lines 505-532** · `sha256:0a27295f9e7ea42f160239be009828e8130a4086bddcafbd9a148a7680b0e5c1`

```
7.  Normative References

   [IANA.cose_header-parameters]
              IANA, "COSE Header Parameters",
              <https://www.iana.org/assignments/cose>.

   [RFC2119]  Bradner, S., "Key words for use in RFCs to Indicate
              Requirement Levels", BCP 14, RFC 2119,
              DOI 10.17487/RFC2119, March 1997,
              <https://www.rfc-editor.org/info/rfc2119>.

   [RFC3161]  Adams, C., Cain, P., Pinkas, D., and R. Zuccherato,
              "Internet X.509 Public Key Infrastructure Time-Stamp
              Protocol (TSP)", RFC 3161, DOI 10.17487/RFC3161, August
              2001, <https://www.rfc-editor.org/info/rfc3161>.

   [RFC5652]  Housley, R., "Cryptographic Message Syntax (CMS)", STD 70,
              RFC 5652, DOI 10.17487/RFC5652, September 2009,
              <https://www.rfc-editor.org/info/rfc5652>.

   [RFC8174]  Leiba, B., "Ambiguity of Uppercase vs Lowercase in RFC
              2119 Key Words", BCP 14, RFC 8174, DOI 10.17487/RFC8174,
              May 2017, <https://www.rfc-editor.org/info/rfc8174>.

   [RFC9052]  Schaad, J., "CBOR Object Signing and Encryption (COSE):
              Structures and Process", STD 96, RFC 9052,
              DOI 10.17487/RFC9052, August 2022,
              <https://www.rfc-editor.org/info/rfc9052>.
```

## Appendix A — Examples

Two worked examples. **One of them reproduces and one does not**; see
`examples/README.md` for the measurement and `design-notes.md` D-1 for the
finding.

**Source lines 534-534** · `sha256:d054724e1b6efaad22652faa1cece9e81fcc829af7be05fc0a514832e33900cf`

```
Appendix A.  Examples
```

### Appendix A.1 — TTC

The payload, the hash, and the request. `sha256('This is the content.')` reproduces
the printed imprint exactly.

**Source lines 536-556** · `sha256:b3ef2ef97b005d38cf6a32448d5cb725dd24e01d95aa96a8d9de727f6188e4a1`

```
A.1.  TTC

   The payload

   'This is the content.'

   is hashed using SHA-256 to create the following TimeStampReq object

   SEQUENCE {
     INTEGER 1
     SEQUENCE {
       SEQUENCE {
         OBJECT IDENTIFIER sha-256 (2 16 840 1 101 3 4 2 1)
         NULL
         }
       OCTET STRING
         09 E6 38 D4 AA 95 FD 72 71 86 62 03 59 53 03 BC
         E2 32 F4 62 A9 4D 38 E3 93 77 3C D3 AA E3 F6 B0
       }
     BOOLEAN TRUE
     }
```

The request is sent, and a response comes back.

**Source lines 558-560** · `sha256:73b6aacc07d17e9af1cb89f42f1845a8f37c97669507e7f8baa2eeeb6d2014c7`

```
   which is sent to the TSA.

   A TimeStampResp containing the following TST is returned:
```

The TSTInfo dump, **truncated by the document itself** at source line 592 with
`[...]`. Everything after that point exists only inside the hex of the COSE
object that follows.

**Source lines 562-592** · `sha256:9fa7c32a1b1f2d3990b6314fe9e65cc667e57cae5b2a9a5408f33a9de0a22ed7`

```
   SEQUENCE {
     OBJECT IDENTIFIER signedData (1 2 840 113549 1 7 2)
     [0] {
       SEQUENCE {
         INTEGER 3
         SET {
           SEQUENCE {
             OBJECT IDENTIFIER sha-512 (2 16 840 1 101 3 4 2 3)
             NULL
             }
           }
         SEQUENCE {
           OBJECT IDENTIFIER tSTInfo (1 2 840 113549 1 9 16 1 4)
           [0] {
             OCTET STRING, encapsulates {
               SEQUENCE {
                 INTEGER 1
                 OBJECT IDENTIFIER '1 2 3 4 1'
                 SEQUENCE {
                   SEQUENCE {
                     OBJECT IDENTIFIER sha-256 (2 16 840 1 101 3 4 2 1)
                     NULL
                     }
                   OCTET STRING
                     09 E6 38 D4 AA 95 FD 72 71 86 62 03 59 53 03 BC
                     E2 32 F4 62 A9 4D 38 E3 93 77 3C D3 AA E3 F6 B0
                   }
                 INTEGER 12096870
                 GeneralizedTime 29/08/2025 07:45:46 GMT
                 BOOLEAN TRUE
   [...]
```

The assembly rule, restated: the token is **inside the signed bytes**.

**Source lines 594-596** · `sha256:0835324b1238b68cb31f3019b2988c646d678f9aebcd53c06a71d1ecc25dd9fe`

```
   The contents of the TST are bstr-wrapped and added to the protected
   headers bucket, which is then signed alongside the original payload
   to obtain the COSE_Sign1 object.
```

The resulting COSE_Sign1 object, with the 5453-octet token in its protected
header.

**Source lines 598-763** · `sha256:cefb431486d381714b531ff03ef035a973dbcbbcc87b422b685adc4f80d144a8` · **declared, not reproduced here** (166 lines; the bytes are in `examples/`)

### Appendix A.2 — CTT

The starting object — already signed, which is why the token can only go in the
unprotected bucket.

**Source lines 765-782** · `sha256:5fc65b728099866c305114dd47bbee18f1adeab641e5d80fe5001e3239d75b09`

```
A.2.  CTT

   Starting with the following COSE_Sign1 object,

   18(
     [
       / protected h'a10126' / << {
           / alg / 1:-7 / ECDSA 256 /
         } >>,
       / unprotected / {
         / kid / 4:'11'
       },
       / payload / 'This is the content.',
       / signature / h'8eb33e4ca31d1c465ab05aac34cc6b23d58fef5c083106c4d
   25a91aef0b0117e2af9a291aa32e14ab834dc56ed2a223444547e01f11d3b0916e5a4
   c345cacb36'
     ]
   )
```

The request. **This is the defective fixture**: the printed imprint is `DD 94 71 EF
…`, and `sha256` of the printed `signature` field with its `0x5840` head — the
preimage §3.1.1 requires, verified against §3.1.1's own worked example — is
`44 C2 41 9D …`. 207 candidate preimages assembled from this document's own
printed bytes were tried and none produces `DD 94 71 EF …`.

**Source lines 784-799** · `sha256:d753f79acecb58379a98f6f546277765a29ffa26a8e2c7bee8ebbce4cf0a0660`

```
   the CBOR-encoded signature field is hashed using SHA-256 to create
   the following TimeStampReq object

   SEQUENCE {
     INTEGER 1
     SEQUENCE {
       SEQUENCE {
         OBJECT IDENTIFIER sha-256 (2 16 840 1 101 3 4 2 1)
         NULL
         }
       OCTET STRING
         DD 94 71 EF E7 43 C4 05 13 35 DF 8F 6D 28 82 F3
         BA DC 38 77 00 F7 ED 3F 70 91 67 2A 3E EA F7 C8
       }
     BOOLEAN TRUE
     }
```

The request is sent, and a response comes back.

**Source lines 801-803** · `sha256:73b6aacc07d17e9af1cb89f42f1845a8f37c97669507e7f8baa2eeeb6d2014c7`

```
   which is sent to the TSA.

   A TimeStampResp containing the following TST is returned:
```

The TSTInfo dump, carrying the same unreproducible imprint, and truncated at
source line 835.

**Source lines 805-835** · `sha256:e7c5503fd7916fa696bc81f4f0a2363253f63dbcb2005ee1f071a4c8c3c7af59`

```
   SEQUENCE {
     OBJECT IDENTIFIER signedData (1 2 840 113549 1 7 2)
     [0] {
       SEQUENCE {
         INTEGER 3
         SET {
           SEQUENCE {
             OBJECT IDENTIFIER sha-512 (2 16 840 1 101 3 4 2 3)
             NULL
             }
           }
         SEQUENCE {
           OBJECT IDENTIFIER tSTInfo (1 2 840 113549 1 9 16 1 4)
           [0] {
             OCTET STRING, encapsulates {
               SEQUENCE {
                 INTEGER 1
                 OBJECT IDENTIFIER '1 2 3 4 1'
                 SEQUENCE {
                   SEQUENCE {
                     OBJECT IDENTIFIER sha-256 (2 16 840 1 101 3 4 2 1)
                     NULL
                     }
                   OCTET STRING
                     DD 94 71 EF E7 43 C4 05 13 35 DF 8F 6D 28 82 F3
                     BA DC 38 77 00 F7 ED 3F 70 91 67 2A 3E EA F7 C8
                   }
                 INTEGER 12100074
                 GeneralizedTime 29/08/2025 07:53:00 GMT
                 BOOLEAN TRUE
   [...]
```

The assembly rule: added to the unprotected bucket **in the original object**, which
is not re-signed.

**Source lines 837-839** · `sha256:d864d4399d5e66b5c168af5d9dc2e747938bbe608b51b8907bb9e8b4ae54301f`

```
   The contents of the TST are bstr-wrapped and added to the unprotected
   headers bucket in the original COSE_Sign1 object to obtain the
   following:
```

The resulting COSE_Sign1 object.

**Source lines 841-1013** · `sha256:e634df4991085e80a77fd4c1c86c80c312b2ff7a591c322c5eb8d068c71c44f4` · **declared, not reproduced here** (173 lines; the bytes are in `examples/`)

---

## What is deliberately not here

- **Masthead, Status of This Memo, Copyright Notice and Table of Contents**
  (source lines 1-78). Boilerplate and navigation.
- **Acknowledgments, Contributors and Authors' Addresses** (source lines
  1015-1056). Attribution rather than obligation. One fact from them is kept in
  `design-notes.md`: the Contributors section records that *Carsten contributed
  part of the security considerations* and that *Orie contributed an improved
  version of the diagrams* — so the two parts of the document this extraction
  finds sharpest are both attributed to contributors rather than to the authors.
- **The two final Appendix A objects**, source lines 598-763 (166 lines) and
  841-1013 (173 lines), declared above with their digests instead of being
  reproduced. **Pass 2 correction: these are not "the two 159-line hex
  blocks".** Each hex run is 159 lines (599-757 and 847-1005), and the declared
  regions are 7 and 14 lines larger, because each also carries the CBOR
  diagnostic notation that frames the hex — `18([`, the `{4: '11'}` /
  `/ kid / 4:'11'` unprotected bucket, `'This is the content.'`, the
  `signature` field and the closing brackets. 15 of those 21 extra lines are
  diagnostic notation rather than hex. The hex itself is in
  `examples/a1-ttc-timestamp-token.hex` and
  `examples/a2-ctt-timestamp-token.hex`; the framing is in
  `schema/source-renderings.txt` for A.2's starting object and in
  `messages.yaml` and `examples/vectors.yaml` V-0009/V-0013 as a decoded,
  octet-by-octet layout.

## Coverage, stated as a measurement

Every statement-bearing line of the Abstract (source lines 17-23) and of the
body from source line 79 (§1) to source line 1014 (the end of Appendix A.2) is
inside one of the regions above, except section headings and blank lines
between regions. **Measured: 0 uncovered.** Two of the 29 regions are
**declared with their digest rather than reproduced** (L598-763 and L841-1013,
166 and 173 lines), so of the 29 regions **27 carry a printed block and all 29
carry a verified digest**. The only statement-bearing lines of the document
outside that span are source lines 25-77 — Status of This Memo, the Copyright
Notice and the Table of Contents — and they are excluded deliberately, as
recorded above.

**Re-verified by pass 2 (2026-10-21), by script and against the cache:** 29
region headers, 2 declared-only; the 27 printed blocks are byte-identical to
their declared line ranges AND digest-correct, 27 of 27; the 2 declared-only
regions are digest-correct, 2 of 2; no region contains a form feed, a running
header or a running footer. The 23 non-blank, non-heading source lines that
fall outside a *printed* block are exactly the two declared regions' content.

---
record: draft-ietf-vcon-vcon-core-04
kind: examples
title: "draft-ietf-vcon-vcon-core-04 — examples and test vectors"
extracted: "2026-10-13"
reviewed_by: "nfnewbury 2026-10-14"
---

# vCon core `-04` — examples and test vectors

**Twelve fixtures. Nine of them JSON, nine of nine parse.** `index.yaml`
carries one entry per fixture with its source line range, its sha256, which
vCon form it is, what it exercises, what a harness should expect from it, and
**108 consistency checks** run against the fixture bytes — 72 pass, 28 fail,
8 not determinable. Every failure is a defect or a deviation in the **source**.
Nothing was repaired.

**Independently re-derived at pass 2 (2026-10-14).** All twelve fixtures
reproduce byte-for-byte from the cached source under a separately written
implementation of the recipe in `index.yaml` — every digest, every line range,
833 rejoins, no anomalies. A.6's `payload` decodes to a document equal to the
A.4 fixture and A.6's RS256 signature verifies against the RSA-2048 key in
`x5c[0]`, which confirms the de-furnishing from outside the extraction. Three
counting claims were corrected; see `index.yaml`'s `verification:` block.

## Where the examples actually are

This directory's note in `../README.md` said since 2026-09 that `examples/`
was empty and that the examples were in "§7". **Both halves were wrong.**
§7 is *Non-Upward Compatible Changes to the vCon Container*, a migration log
between Internet-Draft versions, and it prints no example at all.

| what | where | lines |
|---|---|---|
| nine complete worked vCons | **Appendix A** | 4047–6726 |
| Figure 1, redacted vCon object tree | §4.1.8 | 968–1002 |
| Figure 2, amended vCon object tree | §4.1.9 | 1069–1099 |
| archival JWS nesting illustration | §5.2.3 | 2778–2789 |
| **inline JSON in §1–§6** | **none** | — |

The §1–§6 sweep was mechanical, not impressionistic: a scan of lines 1–4046
for a JSON key-value pair — a quoted name, a colon, a quoted value — returns
**zero** hits. §2.2 *JSON Notation* defines a vocabulary (`Date`, `String`,
`UnsignedInt`, `UnsignedFloat`, `Mediatype`, `ContentHash`, `SessionId`)
rather than giving examples of it; §2.3 and §2.4 define `encoding`, `url` and
`content_hash` in prose; §6 is registration templates and registry tables.
The three ASCII figures are the only examples the body carries, and the source
itself calls the first two "an example partial JSON object tree", so they are
here as text fixtures.

## The fixtures

| id | file | form | source | exercises |
|---|---|---|---|---|
| `VCON-A1` | `a1-two-party-call-inline-recording.json` | unsigned | A.1, 4067–4317 | inline media, `encoding: base64url` |
| `VCON-A2` | `a2-email-thread-multipart.json` | unsigned | A.2, 4329–4469 | multipart MIME body, `encoding: none` |
| `VCON-A3` | `a3-email-thread-text.json` | unsigned | A.3, 4490–4569 | plain text bodies, three dialogs |
| `VCON-A4` | `a4-two-party-call-external-recording.json` | unsigned | A.4, 4597–4629 | `url` + `content_hash` |
| `VCON-A5` | `a5-two-party-call-with-analysis.json` | unsigned | A.5, 4639–5705 | Analysis Object, `encoding: json` |
| `VCON-A6` | `a6-signed-vcon.json` | signed | A.6, 5732–6020 | JWS General JSON Serialization |
| `VCON-A7` | `a7-encrypted-vcon.json` | encrypted | A.7, 6034–6403 | JWE General JSON Serialization |
| `VCON-A8` | `a8-redacted-vcon.json` | redacted | A.8, 6419–6596 | Redacted Object, redaction in practice |
| `VCON-A9` | `a9-amended-signed-vcon.json` | amended | A.9, 6669–6715 | Amended Object, deep-copy rule |
| `VCON-FIG1` | `fig1-redacted-vcon-object-tree.txt` | diagram | §4.1.8, 968–1002 | intended redaction nesting |
| `VCON-FIG2` | `fig2-amended-vcon-object-tree.txt` | diagram | §4.1.9, 1069–1099 | intended amendment nesting |
| `VCON-S523` | `s5-2-3-archival-jws-nesting.txt` | diagram | §5.2.3, 2778–2789 | nested JWS for archiving |

## How the bytes were derived, and why you can trust them

The fixtures are the source's characters with **two presentation transforms
reversed and nothing else touched**. The recipe is deterministic; re-run it
and the sha256 in `index.yaml` comes back.

1. **Page furniture removed** — the running footer, the bare form feed, the
   running header, and the empty lines of the page break.
2. **The uniform three-space left margin removed.** The minimum indent over
   each block is 3 in all nine; relative indentation is untouched.
3. **Line wrapping undone.** Appendix A opens by saying the vCons "have been
   formatted such that long text lines have been wrapped with a left hand
   white space indent for readability purposes", and links an unwrapped copy
   of each. The wrap is reversed by the only rule decidable from the text: **a
   line that ends inside an open JSON string is continued by the next line**,
   because [JSON] forbids a literal line terminator inside a string. The
   continuation carries exactly **two spaces more** than the line on which the
   string opened; those two are removed and everything after them is content.

**Every step was checked rather than assumed.**

- **No real blank line was dropped.** All 42 page breaks inside the twelve
  ranges have the identical shape — 3 empty lines, `Petrie … [Page n]`, a bare
  form feed, `Internet-Draft … September 2026`, 2 empty lines — and **zero**
  empty lines in any of the nine JSON ranges fall outside such a cluster. So
  there is no *fourth* blank line anywhere in Appendix A's JSON, and nothing
  real was lost. The only two unconsumed blanks in the whole set are the single
  line between each figure and its caption, and both survive in the fixtures.
  All 48 whitespace-only-but-non-empty lines in Appendix A are bare form feeds,
  so no continuation line was trimmed to nothing by the formatter.
- **The two-space continuation indent is measured.** Across **833 rejoins**,
  zero continuation lines carried less than the expected indent. A.3 proves
  the rule has teeth: its `dialog[1]` and `dialog[2]` bodies are quoted email
  text whose own leading spaces sit *on top of* the wrap indent, at 12, 13 and
  14 columns where the wrap indent is 11. Stripping all leading whitespace
  would have eaten them silently. They survive.
- **The result is confirmed from outside the extraction.** A.6's `payload`
  base64url-decodes to a document **equal to the A.4 fixture**, and A.6's
  RS256 signature **cryptographically verifies** over the rejoined `protected`
  and `payload` strings using the public key in `x5c[0]`. One wrong character
  anywhere in those 7594 characters breaks both. That is a 233-rejoin proof
  that the de-furnishing is byte-exact.

The three diagram fixtures needed step 2 only — no furniture and no wrap falls
in their ranges — and each was re-derived and compared byte for byte.

**A note for whoever lifts Appendix B.** The draft's JSON Schema is wrapped by
the same mechanism and will not parse as printed for the same reason. Rule 3
above is what unwraps it; the open-string test is decidable there too.

## The checks that earn their place

Eight, for a harness built on this record.

1. **`CHK-A6-SIGVERIFY` — the signature is real.** Recovered the RSA-2048
   public key from `x5c[0]`'s SubjectPublicKeyInfo, computed `s^e mod n`,
   unwrapped PKCS#1 v1.5, and matched the SHA-256 DigestInfo against the
   signing input. **Valid.** Done with integer arithmetic and no crypto
   library, so it reproduces anywhere. A.6 and A.4 are self-validating.
2. **`CHK-A7-CIPHERTEXT-SIZE` — the encrypted form really does wrap the signed
   one.** §5.3 says a vCon MUST be signed first, then encrypted, and no key is
   published to check it. The ciphertext is 13184 octets; the A.6 signed vCon
   serialized with its generator's separators is 13172, and PKCS#7 padding adds
   12. **Exact.** Compact separators give 13168, which does not match — so the
   match identifies the serialization too, and is not an artefact of rounding.
3. **`CHK-A1-RIFF` — the inline media is self-describing.** A.1's `body`
   decodes to 7730 octets of RIFF/WAVE whose internal size field reads 7722,
   which is 7730 − 8. A harness can assert the inline branch of §2.3 without
   holding the original file.
4. **`CHK-A4-UUID-UNIQUE` — one uuid, seven occurrences, two distinct
   contents.** See below.
5. **`CHK-A8-LINK-AMBIGUOUS` — a typed reference is only as good as its key.**
6. **`CHK-A9-DEEPCOPY` — the versioning rule, done right, once.** A.9's
   `parties`, `dialog[0]` and `created_at` equal A.4's element for element, it
   takes a *new* uuid, and it points at the old one through `amended`. This is
   what A.5 should have done and did not.
7. **`CHK-A3-MSGID` — one Message-ID, two messages, one vCon.**
8. **`CHK-A8-REDACTION-CONTENT` — what automated redaction actually did.**

## Source defects found

Twenty-eight checks fail. They group into eleven distinct defects.

### 1. One uuid, two different documents — `CHK-A4-UUID-UNIQUE`

§4.1.2: *"The UUID value MUST be globally unique."*
`01a07da8-c2bb-83e5-b9a2-279e0d16bc46` is the uuid of **A.4** and of **A.5**,
which are different documents — verified by deleting `analysis` from both
fixtures and comparing: equal, so A.5 is A.4 plus one Analysis Object. It is
also A.6's payload uuid, A.6's signature-header uuid, A.7's unprotected uuid,
A.8's `redacted.uuid` and A.9's `amended.uuid` — **seven occurrences** of the
string in the appendix, across four documents that bear it and two that cite it.

**Counted precisely, because the number is what gets filed.** Three of the four
bearers are entitled to share it: §5.4 makes unsigned, signed and encrypted
*forms* of one vCon, and A.6's `payload` decodes to a document equal to the A.4
fixture, so A.4 and A.6 are demonstrably the same vCon and A.7 is presumptively
its encrypted form. The violation is the fourth bearer. A reference by this
uuid is ambiguous between **two** distinct contents — A.4's and A.5's — not
six.

§4.1.9 says a vCon that gains data becomes a new instance version, referenced
through `amended`. A.5 gains an Analysis Object and does neither. **The one
identifier §4.1.8 and §4.1.9 rely on to link versions resolves ambiguously
inside the appendix that demonstrates them.** This is the finding with the most
bearing on `DEC-005` and `R-M-11`: a reference by identifier alone is worth
exactly the uniqueness of the identifier.

### 2. A redaction timestamped before its source — `CHK-A8-UUID-TIME-ORDER`

§4.1.2 builds the uuid like a version 7 UUID, so the first 48 bits are a
millisecond timestamp and uuids sort by creation time — that is the entire
reason the draft chose it over a random UUID. A.8's prefix decodes to
**2024-10-15T02:44:32.702Z**; the vCon it redacts decodes to
**2026-09-07T20:56:47.035Z**. The derived document sorts nearly two years
before its source.

### 3. `sha512` is not "only lowercase letters" — `CHK-*-HASH-ALG-TOKEN`

§2.2, one paragraph, two sentences that contradict each other: *"The hash
algorithm is identified by `sha512`"* and *"Hash algorithm identifiers MUST
use only lowercase letters, and they MUST NOT contain hyphen characters."*
`sha512` contains three digits. **Every `content_hash` in Appendix A fails the
MUST as written** — A.4, A.5, A.8, A.9. The constraint was copied from §6 of
[STIR-PASS] "to remove the normative dependency", and the copy kept a sentence
the draft's own identifier does not satisfy. An implementation enforcing it
literally rejects every example in the document.

### 4. JOSE header parameters are not disjoint — `CHK-A6-JOSE-DISJOINT`, `CHK-A7-JOSE-DISJOINT`

Two instances of one design fault.

- **A.6:** `alg` and `x5c` appear in *both* the protected header and the
  unprotected `header`, with equal values. RFC 7515 §7.2.1 says the names in
  the two locations **MUST be disjoint**. A conforming JWS library rejects the
  document *before* checking the signature — which, as check 1 above shows, is
  valid.
- **A.7:** `enc` appears in **all three** locations — protected, shared
  unprotected, and the recipient header. RFC 7516 §7.2.1 says the names in the
  three locations MUST be disjoint.

The cause is the same both times: **§5.2.2 and §5.3.1 say which header a JOSE
parameter goes in without saying it must then be absent from the others**, and
§5.2.2's requirement that `alg` be in the *unprotected* header collides with
how every RS256 signer works. Carry this into design notes — it is a worked
case of a profile adding a MUST that collides with its own normative reference.

### 5. The encrypted form has a member the draft never defines — `CHK-A7-PROTECTED-UNDEFINED`

§5.3 enumerates `unprotected`, `recipients`, `iv`, `ciphertext`, `tag`.
Appendix C's `encrypted_vcon_type` lists the same five. **A.7 carries a
top-level `protected`.** The JWS side *does* define it —
`signature_object_type` has `protected: base64url_value_type` — so the omission
is specific to JWE. §5.3 invokes "the General JWE JSON Serialization Syntax
form as defined in section 7.2.1 of [JWE]", and RFC 7516 §7.2.1 defines
`protected` as a member of exactly that serialization: **the example is right
and the specification text is incomplete.** A validator built from the §5.3
prose rejects the document's own example; one built from the CDDL admits
`protected` only through the `extension_parameters_type` catch-all
(`* tstr => any`), i.e. as an unregistered extension that §2.5 would then
expect declared in `extensions`. *Independently reported by the sibling pass
lifting Appendix C and confirmed here against both the prose and the CDDL.*

### 6. A.7 fails the draft's own CDDL — `CHK-A7-RECIPIENT-ALG`

`recipient_header_object_type = { alg: tstr, extension_parameters_type }` makes
`alg` **non-optional**. A.7's `recipients[0].header` has exactly one member,
`enc` — the required member is missing and a member defined elsewhere (§5.3.1,
on the Unprotected Object) stands in its place. This is the only place in
Appendix A where an example is refused by the draft's own *formal schema*
rather than by its prose. RFC 7516 permits `alg` in the protected header for a
single recipient, so the example is valid JWE and invalid vCon.

### 7. An unregistered media type — `CHK-A7-CTY`

§5.3.1: `cty` SHOULD be `application/vcon` or `application/vcon+gzip`. A.7 says
`application/vcon+json`, which §6 registers nowhere and which appears exactly
once in the document — in this example.

### 8. Message-IDs are not unique — `CHK-A3-MSGID`, `CHK-A2-MSGID`

RFC 5322 §3.6.4: a Message-ID is a globally unique identifier for one message.
**A.3's `dialog[0]` and `dialog[2]` carry the same `message_id`** —
`<2031327240.390235.1663969499936@mail.yahoo.com>` — on two different messages
in one vCon, "Hi Bob: I just wanted to follow up" at 23:24:59 and "Awesome!" at
23:38:12. Both of A.2's ids are reused in A.3 on different messages. Anything
that keys a message by `message_id` breaks on the document's own examples.

### 9. A media type with a folded header inside it — `CHK-A2-MEDIATYPE`

Both A.2 `mediatype` values contain a literal newline and tab:
`multipart/mixed; \n\tboundary="…"`. These are RFC 5322 folded header lines
stored without unfolding; §2.2 defines `Mediatype` by reference to §5.1 of
[MIME], which has no folding. Unfolded, both are valid.

### 10. The figures promise a wrapper the examples omit — `CHK-A9-NOT-SIGNED`, `CHK-F1-VS-A8`, `CHK-F2-VS-A9`

Figure 1 draws four nested documents for a redacted vCon and A.8 supplies the
second level only. Figure 2 draws a JWS over the amended vCon; **A.9 is titled
"Amended Signed vCon" and is unsigned** — no `payload`, no `signatures`. It
matters because §4.1.9's premise is that *"A signed or encrypted vCon cannot be
modified without invalidating it"*: the amendment mechanism exists **for**
signed vCons, and its only example is unsigned.

### 11. The archival pattern is forbidden by the member it uses — `CHK-S523-PAYLOAD`

§5.2: *"The value of the payload is the Base64Url Encoded string containing
either: the unsigned form of the JSON vCon; or the gzipped [GZIP] unsigned
form."* §5.2.3 requires the payload of JWS2 to be JWS1, a **signed** form,
which that sentence excludes. No example nests a JWS inside a JWS, so there is
nothing to disambiguate it.

### Also recorded, lower severity

- **`CHK-A6-TYP`** — the protected header says `typ: JWT`; the payload is a
  vCon with no JWT claim. The draft defines `cty` for the encrypted form and no
  companion `typ` for the signed form, which is where the gap comes from.
- **`CHK-A6-X5C-V1`** — `x5c[0]` and `x5c[1]` are **X.509 version 1**
  certificates with **no extensions at all**: no `basicConstraints`, no
  `keyUsage`. The intermediate that signs the leaf asserts no CA bit, so an
  RFC 5280 path validator must reject it or accept it out of band. Only
  `x5c[2]` is v3.
- **`CHK-A6-X5C-SAN`** — all three certificates carry OID **2.5.29.17** as an
  *attribute type inside the Distinguished Name*. It is a certificate
  **extension** OID and has no place in a Name; `x5c[2]`, the only v3
  certificate, carries no `subjectAltName` extension. Any relying party looking
  for a SAN finds none — which also undercuts §4.1.2's claim that the uuid's
  FQHN is "the same FQHN … as would [be] used in the signing certificate".
- **`CHK-A5-DIARIZATION`** — every one of A.5's 76 transcript words carries
  `speaker: 0`, and so do all four paragraph objects, while the dialog names two
  parties and the text alternates between them. `speaker_confidence` is **not**
  constant — it takes eight distinct values across the 76 words, from 0.139 to
  0.656 — so the diarizer resolved at least eight confidence runs and assigned
  every one of them to the same speaker. **The source says so
  itself**: A.5 opens with an editorial "fix the diarization" note left in a
  document in Last Call. This is the machine-checkable form of that note.
- **`CHK-A8-REDACTION-CONTENT`** — A.8's transcript is A.5's with three
  substitutions, `example.com → {{URL}}`, `1234567890 → {{BAN}}`, and
  `"Okay." → "{{US_STATE}}"` **twice** — "OK" read as Oklahoma. It is also
  *re-tokenized* ("liketo"→"like to", "so I"→"soI", "addedtwo"→"added two",
  74 words against 75), so it is **not** any of the three operations §4.1.8
  allows applied to A.5. And the redaction is wrong in both directions:
  "Okay" destroyed as a false positive, while **"Bob" and "Alice" survive in
  the transcript** although `tel` was stripped from the Party Objects as PII.
  The vendor is named in the example — a real tool's real output, which is why
  it is worth keeping.
- **`CHK-A8-ANALYSIS-TYPE`** — `transcript-redacted` is outside §4.5.1's SHOULD
  list of six, and there is **no registry** by which it could become valid:
  §6.3.7 registers Analysis Object *parameter* names, not `type` values, unlike
  the Dialog Type Name Registry of §6.3.4.1.
- **`CHK-A3-QUOTE-TIME`** — quoted reply text inside A.3's bodies reads
  `23:34:` with no seconds, and `23:24:59 PM` mixes a 24-hour clock with a PM
  suffix. Body text; a harness should treat it as opaque.
- **`CHK-F1-SPELLING`** — Figure 1 spells `ciphertext` as "cyphertext" twice.

## What this set does **not** cover

- **No `content_hash` value is verified against its content.** A.4, A.5, A.8
  and A.9 all carry the same token for `ab_call.mp3`, which this library never
  fetches or commits. Structure is verified — 86 base64url characters decoding
  to exactly 64 octets — and the four copies are byte-identical, so there is no
  transcription error between them. To close it: fetch the file, SHA-512 it per
  §6.3/6.4 of [SHA-512], base64url-encode without padding, compare.
- **A.7 is never decrypted.** No recipient private key is published. Settled by
  length instead (check 2 above).
- **The uuid FQHN rule is unverified** — `CHK-A9-UUID-FQHN`. §4.1.2 says
  `rand_b` is the high 62 bits of SHA-1(FQHN), so those bits are a function of
  the domain alone. A.1–A.8 share `b9a2-279e0d16bc46`; **A.9 alone has
  `a20f-d188127fad29`**. Sixteen candidate FQHNs drawn from the certificates
  and the example data were tested against three readings of "high 62 bits" and
  none matched either value. The document never states the FQHN, so this cannot
  be closed from the document. Recorded in full in `index.yaml` so a verifier
  with the FQHN closes it in one line.
- **`ContentHash[]`, the array form,** is permitted by §2.4.2 and appears in no
  example.
- **The Redacted and Amended Objects' `url` + `content_hash`** are exercised by
  no example: A.8's `redacted` has only `uuid` and `type`, A.9's `amended` only
  `uuid`. So the cross-document integrity link those objects exist to carry has
  **no fixture in this draft**.
- **Of the five objects that may carry a ContentHash** — Dialog, Analysis,
  Attachment, Redacted, Amended — **only Dialog has one.**
- **Three of Figure 1's four levels and two of Figure 2's three** are
  illustrated and never shown. No example nests a JWS inside a JWS.
- **Dialog types `transfer`, `incomplete` and `recording-set`** are registered
  in §6.3.4.1.2 and appear in no example; only `recording` and `text` do.
  `party_history`, `Dialog Transfer` and the Attachment Object have no fixture
  either — `attachments` is the empty array in all seven unsigned examples.
- **No example carries the `vcon` syntax-version parameter**, correctly: §4.1.1
  deprecates it. A harness must not require it.
- **No example carries `extensions` or `critical`**, so the must-understand
  mechanism of §2.5 and §4.1.4 — the thing this record is held for — is
  exercised by **nothing in the document**.

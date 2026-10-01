---
record: rfc-9052
kind: schema
title: "rfc-9052 — schemas"
extracted: "2026-09-30"
reviewed_by: ""
---

Schemas for RFC 9052 (STD 96), "CBOR Object Signing and Encryption
(COSE): Structures and Process". RFC 9052 states its structures in CDDL
[RFC 8610], so this artifact is primarily a transcription.

## Files

| File | Coverage | Kind | Source sections |
| --- | --- | --- | --- |
| `cose.cddl` | Every CDDL fragment in RFC 9052, assembled in source order: all 30 rules — `start`, `Internal_Types`, `label`, `values`, `COSE_Messages`, `COSE_Untagged_Message`, `COSE_Tagged_Message`, `Headers`, `header_map`, `empty_or_serialized_map`, `Generic_Headers`, `COSE_Sign_Tagged`, `COSE_Sign`, `COSE_Signature`, `COSE_Sign1_Tagged`, `COSE_Sign1`, `Sig_structure`, `COSE_Encrypt_Tagged`, `COSE_Encrypt`, `COSE_recipient`, `COSE_Encrypt0_Tagged`, `COSE_Encrypt0`, `Enc_structure`, `COSE_Mac_Tagged`, `COSE_Mac`, `COSE_Mac0_Tagged`, `COSE_Mac0`, `MAC_structure`, `COSE_Key`, `COSE_KeySet` | **verbatim** | §1.4, §1.5, §2, §3, §3.1, §4.1, §4.2, §4.4, §5.1, §5.2, §5.3, §6.1, §6.2, §6.3, §7 |
| `structures.derived.cddl` | The three structures this project exports — `COSE_Sign1` (with `COSE_Sign1_Tagged`), `Sig_structure`, `COSE_Key` — plus every rule they reference (`Headers`, `header_map`, `empty_or_serialized_map`, `Generic_Headers`, `label`, `values`), a derived `Exported_Types` entry point, and a derived `Sig_structure_strict` that states §4.4's prose constraint. 14 rules, closed: no undefined nonterminal, so it checks standalone. | **derived** | §1.4, §1.5, §3, §3.1, §4.2, §4.4, §7, §7.1, §9 |
| `README.md` | This index and the caveats below. | — | — |

The two CDDL files are strictly separate. `cose.cddl` is the assembled
verbatim transcription and is the only file to quote as RFC 9052's text;
`structures.derived.cddl` is ours and says so in its own header, listing
the complete delta from the verbatim rules. No rule was reformatted,
reindented, corrected or merged in `cose.cddl`; the RFC's three-space
text margin, inline comments and internal blank lines are preserved, and
each fragment is preceded by a `; §…` marker naming its section. Every
non-comment line in `cose.cddl` was machine-checked to appear
byte-for-byte in the source.

RFC 9052 defines no rule twice, so `cose.cddl` records no duplication.

## The CDDL is informational, and it is not the whole spec

§1.4: "The CDDL grammar is informational; the prose description is
normative." An implementation that validates only against `cose.cddl` is
validating against the weaker of the two descriptions.

§1.4 also notes that RFC 9052 uses only a subset of CDDL — the
primitives `any`, `bool`, `bstr`, `int`, `nil`, `nint`, `tstr`, `uint`;
the shorthands `FOO / BAR`, `[+ FOO]`, `* FOO`; and the control
operators `.cbor` and `.size`.

## Dangling references

At the grammar level nothing dangles: all 30 rules in `cose.cddl`
resolve within the file (checked; zero undefined nonterminals), and
`Internal_Types` exists in the source only to keep the RFC's own
validation tool quiet about `Sig_structure`, `Enc_structure` and
`MAC_structure` being unreachable from the wire formats.

The incompleteness is one level down, in the *value spaces*, which
RFC 9052 delegates to RFC 9053 and to IANA. These are not missing CDDL
rules, and none has been invented here; each site is marked `; DANGLING:`
in `structures.derived.cddl`.

| Site | Left as | Defined by |
| --- | --- | --- |
| `Generic_Headers` label 1 (`alg`) | `int / tstr` | IANA "COSE Algorithms" registry; values in RFC 9053 |
| `Generic_Headers` label 2 (`crit`) `[+label]` | any `label` | the labels named are themselves registry entries (§11.1) |
| `Generic_Headers` label 3 (content type) | `tstr / int` | IANA media types / CoAP Content-Formats registry |
| `header_map`'s `* label => values` | `any` | IANA "COSE Header Parameters" registry (§11.1); algorithm-specific parameters in RFC 9053 |
| `COSE_Key` label 1 (`kty`) | `tstr / int` | IANA "COSE Key Types" registry; values in RFC 9053 |
| `COSE_Key` label 3 (`alg`) | `tstr / int` | IANA "COSE Algorithms" registry; values in RFC 9053 |
| `COSE_Key`'s `* label => values` | `any` | IANA "COSE Key Common Parameters" (§11.2) and "COSE Key Type Parameters" registries; key-type parameters in RFC 9053 |

Each of the seven sites was re-checked against the source in the
cross-check pass, and each really is undefined here. RFC 9052 §11 adds no
value to any of them: §11.1 and §11.2 only re-point the "COSE Header
Parameters" and "COSE Key Common Parameters" registry references from
[RFC8152] to this document, §11.4 does the same for the CoAP
Content-Formats entries, and §11.5 the same for the CBOR tags. The
closest the prose comes to a value is Table 4's "The set of values
defined in this document can be found in [COSE.KeyTypes]" — a pointer to
the registry, not a list. **No `alg`, `kty` or content-type value appears
anywhere in RFC 9052 outside Appendix B/C examples**, where the values
(`1:-7`, `1:1`, `1:10`, `1:5`, `1:15`, `1:-3`, `1:-5`, `1:-6`, `1:-10`,
`1:-25`, `1:-27`, `1:-29`, `1:-32`, `1:-36`, `1:14`, `kty 1:2`, `1:4`)
are *used with annotations* and nowhere defined. The record says so and
invents nothing; a reader needs RFC 9053 and the registries.

Not dangling, despite the loose CDDL: `COSE_Key` label 4 (`key_ops`) is
typed `[+ (tstr / int) ]`, but RFC 9052 §7.1 Table 5 does define its
values (1 sign, 2 verify, 3 encrypt, 4 decrypt, 5 wrap key, 6 unwrap
key, 7 derive key, 8 derive bits, 9 MAC create, 10 MAC verify). The
RFC's own CDDL does not enumerate them, so neither file does; the values
are recorded as a comment in `structures.derived.cddl`.

## Where the CDDL is looser than the prose

These are not transcription errors. They are places where `cose.cddl`
accepts data the normative prose forbids, and therefore where a later
implementation must carry a check the schema cannot.

- **`Sig_structure` (§4.4).** The rule makes `sign_protected` optional
  and leaves `context` free, so it accepts `["Signature1", body, sign,
  aad, payload]` and `["Signature", body, aad, payload]`. §4.4 prose
  item 3 says the signer-protected field "is omitted for the COSE_Sign1
  signature structure", and item 1 binds `"Signature1"` to COSE_Sign1
  and `"Signature"` to COSE_Signature. `Sig_structure_strict` in
  `structures.derived.cddl` binds the context string to the arity.
- **Header buckets (§3, §9).** That a label MUST be unique within a map,
  that applications SHOULD check a label does not occur in both buckets
  of a layer, and that the protected bucket MUST be empty when it is not
  covered by a cryptographic computation, are all prose-only.
- **Deterministic encoding (§9).** `Sig_structure`, `Enc_structure` and
  `MAC_structure` MUST be encoded with definite lengths and
  minimum-length arguments. No CDDL states this; it is an encoder rule.
- **`empty_or_serialized_map` (§3).** `bstr .cbor header_map / bstr
  .size 0` admits both forms equally, whereas §3 says senders SHOULD
  emit the zero-length byte string and recipients MUST accept both it
  and an encoded zero-length map (`h'a0'`).
- **Detached content.** `payload : bstr / nil` does not say that `nil`
  obliges the application to supply the payload out of band (§4.1,
  §6.1), nor that a zero-length `bstr` payload is the message-recovery
  case of §4.1/§8.1 rather than an empty message.
- **`external_aad` (§4.3, §4.4, §5.3, §6.3).** Typed `bstr` with no
  optionality; the prose default of a zero-length byte string when the
  application supplies nothing is not expressible here.
- **`content type` (§3.1).** The CDDL types label 3 as `tstr / int`
  while Table 3 in the same section gives its CBOR type as
  `tstr / uint`. The CDDL therefore admits a negative content-type
  value that the table forbids. This is a divergence inside the source,
  not a transcription error: `cose.cddl` carries the CDDL spelling and
  `messages.yaml` carries the table's, each faithful to where it came
  from. Recorded in `design-notes.md` under open questions.

## Named in the prose, deliberately absent from the CDDL

Three values RFC 9052 names and relies on have no CDDL rule anywhere in
the source, because they are *byte strings produced by encoding* a rule,
not data structures: **`ToBeSigned`** (§4.4, the encoded
`Sig_structure`), **`ToBeMaced`** (§6.3, the encoded `MAC_structure`)
and the **`AAD`** (§5.3, the encoded `Enc_structure`). Their absence
here is correct, not an omission. They are modelled in `messages.yaml`
so that §9's encoding restrictions and `protocol.yaml`'s steps have
something to attach to.

One naming trap, and it is the source's own: §8.5.1–§8.5.5 call the
recipient structure **`COSE_Recipient`** with a capital R, while the
CDDL rule and the §5.1 prose call it **`COSE_recipient`**. There is only
one structure. `requirements.yaml` keeps §8.5's spelling because its
quotes are verbatim; `messages.yaml` and both CDDL files use the rule
name. Join on the structure, not on the string.

## Cosmetic inconsistencies in the source, preserved verbatim

Reported so a reviewer does not read them as extraction damage:
`COSE_Signature` has two spaces after `=`; `COSE_Encrypt0` (§5.2) and
`COSE_Mac0` (§6.2) carry a trailing comma before `]`, which is legal
CDDL but is not the style of the other structures; body indentation is
4 spaces in §3–§5, 3 spaces in §6.1 and §6.2, and 5 spaces in §6.3; and
the one-or-more shorthand appears as `[+ COSE_Signature]`,
`[+COSE_recipient]` and `[+label]`.

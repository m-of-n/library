---
record: rfc-9277
kind: normative
title: "rfc-9277 — normative statements"
extracted: "2026-10-20"
reviewed_by: ""
---

<!-- Every normative statement, VERBATIM, with its locator. Keep the source's
section structure as headings. Drop motivation, history, acknowledgements. -->

Source: RFC 9277, "On Stable Storage for Items in Concise Binary Object Representation (CBOR)", Standards Track, August 2022. sha256 `bd637eafad9ef940c8f5d029076f70c58af7bde6beb38efee5ba7af3690289f7` (960 lines, 41659 bytes, plain text). Quotations are verbatim from the plain-text RFC. Blocks that reproduce the hex examples, the CDDL snippets, the registry entries or the TN formula preserve the source's own line breaks and indentation — including the RFC's left margin and its aside bars — inside fenced blocks.

**Why this file has no normative statements in the BCP 14 sense, and why that is
the finding.** `bin/bcp14-count` reports **0**. Measured over the whole source
at this pass, the strings **"BCP 14", "RFC 2119", "RFC 8174" and "key words" do
not appear at all** — so this is not a document that used the keywords and
omitted the boilerplate; **there is no requirements-language section for the
boilerplate to have been omitted from.** Every all-capitals keyword form occurs
zero times.

What the document uses instead, counted at this pass: `may` **24** times,
`should` **5** plus one sentence-initial `Should`, `must` **twice**, `required`
twice, `optional` **zero times in any case**, and `encouraged` (3) /
`suggested` (2) / `needs to` (5) throughout.
*(`[correction]` 2026-10-21, pass 3: this read "`optional` twice". Pass 2
recounted the word as **zero** and wrote the correction into
`requirements.yaml`'s `reconciliation` and into `../README.md`, and left it
wrong here and in `design-notes.md` §8 and `record.yaml`. All three recounted at
pass 3 and all three agree at zero.)*
**Both lower-case `must`s matter:** one is boilerplate licence text, and the
other is **Appendix A.2's** "care must be taken when concatenating Labeled CBOR
Sequences to remove the label from all but the first part" — this record's
headline finding, carrying no BCP 14 force and with no clause in the document
that could give it any.

So this file records the **structural and allocative** content at the grain
another record would use for MUSTs: which tag is outer, which is inner, what the
tag content is, how many bytes, what was allocated, and what the document
permits, warns about or disclaims. **All 195 entries in `requirements.yaml` are
`kind: inferred`.** The precedent is `rfc-9682`, also a zero-keyword Standards
Track RFC.

**Conventions in this file.**

- A bullet `- (§X) "…"  *(id …)*` is one contiguous verbatim span of the source,
  carrying the id it holds in `requirements.yaml`. No span is spliced from two
  non-adjacent parts of the document. Contiguity is asserted after collapsing
  runs of whitespace; no interior word, clause or punctuation mark was altered,
  dropped or reordered.
- **Two declared classes of exception, both mechanical, neither healed:**
  1. **Aside bars.** Two RFC v3 asides exist — source lines **715–727**
     (Appendix A.2's PEM example) and **765–777** (Appendix B's note on the
     formula) — and every line in them begins `      |  `. **Eight** spans are drawn from those ranges and **seven of the eight are contiguous only after that leading `|` bar is removed, and after nothing else**; the eighth (`rfc-9277#R-0146`) begins at the start of its line and so is contiguous either way. Both cases are marked individually below — the distinction was computed, not assumed — the same removal is declared in `requirements.yaml`, and it is confined to those two ranges. **Four lines of the source carry trailing whitespace
     (724, 767, 770, 772) and all four are blank aside lines**; the fenced
     blocks preserve them.
  2. **Fifteen line-end word breaks, every one left broken.** A sentence severed
     by a line break inside a token is **not** a contiguous span of the
     document, so it is quoted as **two** bullets, cut where the source cuts it,
     and the second begins mid-token — **except three: two whose second half was
     never extracted at all (`rfc-9277#R-0147`'s and `rfc-9277#R-0169`'s, both
     now bullets here marked `no id`), and one at 628/629 which no entry
     quotes.** The census, measured at pass 3 by the rule
     `requirements.yaml` states — every line ending in `-` or `/` whose word
     continues on the next line, bars stripped first, references and author
     addresses excluded: source lines 233/234, 257/258, 293/294, 329/330,
     373/374, **628/629**, 657/658, **722/723 and 726/727 (both inside an
     aside)**, 784/785, 795/796, 807/808, 816/817, 821/822 and 897/898.
     **Ten break a hyphenated token and five break after a slash.** Two of them
     are the **same sentence appearing twice** in the document — §2.3 and
     Appendix D — broken at the same token both times.
     *(`[correction]` 2026-10-21, pass 3: this read "**Twelve** hyphenation
     breaks" and listed thirteen pairs. Pass 2 recounted the census as
     **fourteen** and wrote that into `requirements.yaml` and `../README.md`
     without touching this paragraph. Pass 3 re-measured it from the source and
     the census is **fifteen**: pass 2's list omits **628/629**, where line 628
     ends `a public key/` and line 629 begins `certificate in C509` — a slash
     break in Appendix A that its own stated rule catches. No requirement or
     normative span quotes that sentence, so nothing was healed by the omission;
     it is a count that was wrong, not a quotation. Pass 2's hyphen/slash split
     of "eight hyphenated, six slash" is also wrong: over its own fourteen it is
     ten and four, and over the correct fifteen it is **ten and five**.)*
- The source carries **no form feeds and no page footers** (RFC 9277 is an
  unpaginated v3 text rendering), so there is no page-frame decoration to
  remove. The cached rendering begins with a **UTF-8 BOM** (U+FEFF) alone on
  line 1, and source line 771 contains two **U+2264** characters inside an
  aside; both are part of the hashed bytes and are preserved where quoted.
- **There is no BCP 14 boilerplate to quote or to exclude**, so unlike
  `rfc-8742` and `rfc-9741` this file needs no phantom-keyword warning.
- The two hex examples, the Openswan hex, all four CDDL snippets, the three
  registry entries and the TN formula with its aside are reproduced in fenced
  blocks with their source line range. They are also held as files in `schema/`
  and `examples/` with per-region digests.

---

## Abstract

- (Abstract) "This document defines a stored ("file") format for Concise Binary Object Representation (CBOR) data items that is friendly to common systems that recognize file types, such as the Unix file(1) command."  *(`rfc-9277#R-0001`)*

## §1. Introduction

*(§1's Unix and classical-Mac-OS history is dropped as narrative. What is kept
is every sentence that makes a claim, states a scope or defines a term.)*

- (§1) "A common way to identify the type of a file from its contents is to place a "magic number" at the start of the file contents [MAGIC]."  *(`rfc-9277#R-0002`)*
- (§1) "In the media type registration template [RFC6838], a magic number is asked for, if available, as is a file extension."  *(`rfc-9277#R-0003`)*
- (§1) "A challenge for the file(1) command is often that it can be confused by recognizing the overall encoding but not the content being encoded."  *(`rfc-9277#R-0004`)*
- (§1) "For instance, an Android Package Kit APK (as used to transfer and store an application) may be identified as a ZIP file."  *(`rfc-9277#R-0005`)*
- (§1) "Additionally, both OpenOffice and MSOffice files are ZIP files of XML files; the identification may stop at identifying them as ZIP files."  *(**no id.** `[correction]` 2026-10-20, pass 2: dropped at pass 1, source line 118/119. It is not history and not narrative — it is the **generalisation** of the APK case, and so the strongest form of the §1 argument that `design-notes.md` §9 uses to replace the `R-O-03` framing. See `requirements.yaml` `verify_pass`)*
- (§1) "As CBOR becomes a more and more common encoding for a wide variety of artifacts, identifying them as just "CBOR" is probably not sufficient."  *(`rfc-9277#R-0006`)*
- (§1) "This document provides a way to encode a magic number into the beginning of a CBOR format file."  *(`rfc-9277#R-0007`)*
- (§1) "As a CBOR format may use a single CBOR data item or a CBOR sequence of data items [RFC8742], two possible methods of enveloping data are presented; a CBOR Protocol designer will specify one."  *(`rfc-9277#R-0008`)*
- (§1) "(A CBOR Protocol is a specification that uses CBOR as its encoding.)"  *(`rfc-9277#R-0009` — **THE definition the whole document turns on, and it is in a parenthesis**)*
- (§1) "This document also gives advice to designers of CBOR Protocols on choosing one of these mechanisms for identifying their contents."  *(`rfc-9277#R-0010`)*
- (§1) "This advice is informative."  *(`rfc-9277#R-0011` — **the disclaimer that governs the only guidance on the one choice the document makes load-bearing**)*
- (§1) "A third method is also proposed by which a CBOR format tag is prepended to identify non-CBOR files."  *(`rfc-9277#R-0012`)*
- (§1) "Further information on this method appears in Appendix D because it is not about identifying media types containing CBOR-encoded data items."  *(**no id.** `[correction]` 2026-10-20, pass 2: dropped at pass 1, source line 136/137. This is the **one sentence in the document that reconciles `rfc-9277#R-0008`'s "two possible methods" with `rfc-9277#R-0012`'s "third method"** — it says why the third is appendicised and scopes the count of two to media types containing CBOR. It is therefore load-bearing for `design-notes.md` §9's refutation that there are three envelope methods and not two, and the record made that refutation without it. See `requirements.yaml` `verify_pass`)*
- (§1) "This includes a simple way to derive a magic number for content-formats as defined in [RFC7252], even if the file is not in CBOR form."  *(`rfc-9277#R-0013`)*
- (§1) "Examples of CBOR Protocols currently under development include Concise Software Identification Tags [CoSWID] and Entity Attestation Tokens [EAT]."  *(`rfc-9277#R-0014`)*
- (§1) "CBOR Object Signing and Encryption (COSE) itself [RFC8152] is considered infrastructure."  *(`rfc-9277#R-0015` — **COSE is not a CBOR Protocol** — decisive for the MD-3 mapping)*
- (§1) "The encoding of public keys in CBOR as _C509_ as described in [C509-CERT] would benefit from being an identified CBOR Protocol."  *(`rfc-9277#R-0016`)*
- (§1) "A major inspiration for this document is observing the disarray in certain ASN.1-based systems where most files are Privacy-Enhanced Mail (PEM) encoded; these files are all identified by the extension "pem", which confounds public keys, private keys, certificate requests, and S/MIME content."  *(`rfc-9277#R-0017`)*
- (§1) "While the envelopes defined in this specification add information to how data conforming to CBOR Protocols are stored in files, there is no requirement that either type of envelope be transferred on the wire."  *(`rfc-9277#R-0018` — lower-case *no requirement* — **1 of 4** permissive statements about stripping)*
- (§1) "However, there are some protocols that may benefit from having such a magic number on the wire if they are presently using a different (legacy) encoding scheme."  *(`rfc-9277#R-0019`)*
- (§1) "The presence of the identifiable magic sequence can be used to signal that a CBOR Protocol is being used as opposed to a legacy scheme."  *(`rfc-9277#R-0020`)*

### §1.1. Terminology

- (§1.1) "Byte is a synonym for octet."  *(`rfc-9277#R-0021`)*
- (§1.1) "The term "byte string" refers to the data item defined in [STD94]."  *(`rfc-9277#R-0022`)*
- (§1.1) "The term "file" is understood to stand in a general way for a stored representation that is somewhat detached from the original context of usage of that representation; its usage in this document encompasses similar units of storage that may have different identification schemes such as partitions or media blocks."  *(`rfc-9277#R-0023`)*
- (§1.1) "The term "diagnostic notation" refers to the human-readable notation for CBOR data items defined in Section 8 of [STD94] and Appendix G of [RFC8610]."  *(`rfc-9277#R-0024`)*
- (§1.1) "The term "CDDL" (Concise Data Definition Language) refers to the language defined in [RFC8610]."  *(`rfc-9277#R-0025`)*
- (§1.1) "The function TN(ct) is defined in Appendix B."  *(`rfc-9277#R-0026`)*

### §1.2. Requirements for a Magic Number

**A section titled "Requirements for a Magic Number" containing no requirements
language whatever.** Four desirable properties, every one of them under
"Ideally".

- (§1.2) "Ideally, a magic number is a fingerprint that is unique to a specific CBOR Protocol, is present in the first few (small multiple of 4) bytes of the file and does not change when the contents change, and does not depend upon the length of the file."  *(`rfc-9277#R-0027` — **a section titled *Requirements for a Magic Number* with no requirements language**)*
- (§1.2) "Less ideal solutions have a pattern that needs to be matched, but in which some bytes need to be ignored."  *(`rfc-9277#R-0028`)*
- (§1.2) "While the Unix file(1) command can be told to ignore certain bytes, this can lead to ambiguities."  *(`rfc-9277#R-0029`)*

## §2. Protocol

**§2 is titled "Protocol" and defines no exchange.** It presents two byte
layouts and allocates the choice between them to the designer.

- (§2) "This section presents two enveloping methods."  *(`rfc-9277#R-0030`)*
- (§2) "Both use CBOR tags in a way that results in a deterministic first 8 to 12 bytes."  *(`rfc-9277#R-0031` — **the central claim, and false in general** — 30 spellings; see `schema/prefix-spellings.derived.txt`)*
- (§2) "The Protocol designer determines which one to use; see Appendix A for some guidance."  *(`rfc-9277#R-0032`)*

### §2.1. The CBOR-Protocol-Specific Tag

**The pivot of the whole document: both methods need a protocol-specific tag,
per kind of object, from IANA.**

- (§2.1) "In both enveloping methods, CBOR Protocol designers need to obtain a CBOR tag for each kind of object that they might store in files."  *(`rfc-9277#R-0033` — lower-case *need to* — **the step a no-tags rule makes unavailable**)*
- (§2.1) "As there are more than 4 billion available 4-byte tags, there should be little issue in allocating a few to each available CBOR Protocol."  *(`rfc-9277#R-0034`)*
- (§2.1) "The IANA policy for 4-byte CBOR tags is First Come First Served [RFC8126] so only a simple interaction (e.g., via Web or email) with IANA is required."  *(`rfc-9277#R-0035` — **the price tag: First Come First Served, one email**)*
- (§2.1) "The interaction includes filling in the small template provided in Section 9.2 of [STD94]."  *(`rfc-9277#R-0036`)*
- (§2.1) "In the template, a reference to this specification (RFC 9277) alongside the Description of semantics is suggested."  *(`rfc-9277#R-0037` — and the document's own deployment did **not** take it — see `rfc-9277#R-0181`)*
- (§2.1) "Allocation of the CBOR tag needs to be initiated by the designer of the CBOR Protocol, who can provide a proposed tag number."  *(`rfc-9277#R-0038`)*
- (§2.1) "In order to be in the 4-byte range, and so that there are no leading zero bytes in the 4-byte encoding of the tag number, the value needs to be in the range 0x01000000 (decimal 16777216) to 0xFFFFFFFF (decimal 4294967295) inclusive."  *(`rfc-9277#R-0039` — **pins the tag VALUE and not its ENCODING** — which is exactly how far §2's determinism claim reaches)*
- (§2.1) "It is further suggested to avoid values that have an embedded zero byte in the 4 bytes of their binary representation (such as 0x12003456), as these may confuse implementations that treat the magic number as a C string."  *(`rfc-9277#R-0040`)*
- (§2.1) "The use of a sequence of four ASCII [RFC20] codes which are mnemonic to the protocol is encouraged, but not required (there may be reasons to encode other information into the tag; see Appendix B for an example)."  *(`rfc-9277#R-0041`)*
- (§2.1) "For instance, Appendix C uses "OPSN", which translates to the tag number 1330664270 registered for it."  *(`rfc-9277#R-0042`)*
- (§2.1) "In [IANA.CORE-PARAMETERS], the Constrained Application Protocol (CoAP) defines the "CoAP Content-Formats" registry to assign Content-"  *(`rfc-9277#R-0043`)*
- (§2.1) "Format Numbers (Section 12.3 of [RFC7252]) to Content Types in a specific Content Coding."  *(`rfc-9277#R-0044`)*
- (§2.1) "For CBOR data items that form a representation that is already described by such a Content-Format Number, a tag number has proactively been allocated in Section 4.3 (see Appendix B for details and examples)."  *(`rfc-9277#R-0045`)*

### §2.2. Enveloping Method: CBOR Tag Wrapped

- (§2.2) "The CBOR Tag Wrapped method is appropriate for use with CBOR Protocols that encode a single CBOR data item."  *(`rfc-9277#R-0046`)*
- (§2.2) "This data item is enveloped into two nested tags:"  *(`rfc-9277#R-0047`)*
- (§2.2) "The outer tag is a self-described CBOR tag, 55799, as described in Section 3.4.6 of [STD94]."  *(`rfc-9277#R-0048` — **RFC 9277 does not define tag 55799; RFC 8949 §3.4.6 does**)*
- (§2.2) "The tag content of the outer tag is a second CBOR tag whose tag number has been allocated to describe the specific Protocol involved, as discussed in Section 2.1."  *(`rfc-9277#R-0049`)*
- (§2.2) "The tag content of this inner tag is the single CBOR data item."  *(`rfc-9277#R-0050`)*
- (§2.2) "This method wraps the CBOR data item as CBOR tags usually do."  *(`rfc-9277#R-0051`)*
- (§2.2) "Applications that need to send the stored CBOR data item across a constrained network may wish to remove the two tags if the type is understood from the protocol context, e.g., from a CoAP Content-"  *(`rfc-9277#R-0052` — lower-case *may wish to remove* — **2 of 4**; and half a sentence, severed at lines 257/258)*
- (§2.2) "Format Option (Section 5.10.3 of [RFC7252])."  *(`rfc-9277#R-0053`)*
- (§2.2) "Therefore, a CBOR Protocol specification may pick the specific cases where the CBOR Tag Wrapped enveloping method is to be used."  *(`rfc-9277#R-0054`)*
- (§2.2) "For instance, it might specify its use for storing the representation in a local file or for Web access, but not within protocol messages that already provide the necessary context."  *(`rfc-9277#R-0055`)*

#### §2.2.1. Example

- (§2.2.1) "To construct an example without registering a new tag, we use the Content-Format ID assigned for application/senml+cbor (112) [RFC8428] of the "CoAP Content-Formats" registry [IANA.CORE-PARAMETERS])."  *(`rfc-9277#R-0056` — **an unbalanced parenthesis**, carried verbatim)*
- (§2.2.1) "Using the technique described in Appendix B, this translates into the tag TN(112) = 1668546929."  *(`rfc-9277#R-0057`)*
- (§2.2.1) "With this tag, the SenML-CBOR pack [{0: "current", 6: 3, 2: 1.5}] would be enveloped as follows (in diagnostic notation):"  *(`rfc-9277#R-0058` — and its map keys are **not** in RFC 8949 §4.2.1 order)*
- (§2.2.1) "At the representation level, the unique fingerprint for application/"  *(`rfc-9277#R-0059` — `[correction]` 2026-10-20, pass 2: this bullet was labelled `rfc-9277#R-0081` at pass 1. R-0081 is the **§2.3.1** half of the same sentence, whose text is byte-identical, so no text check and no locator check could see it; only resolving the id back to its own entry does. The two duplicate-text groups in this record are the only places a wrong id can hide from a text comparison, and both were wrong — see `requirements.yaml` `verify_pass`)*
- (§2.2.1) "senml+cbor is composed of the 8 bytes d9d9f7da63740171 hex, after which the unadorned CBOR data (81... for the SenML data) is appended."  *(`rfc-9277#R-0060`)*

The §2.2.1 envelope in diagnostic notation and in hex, verbatim and complete (source lines 277–295):

```
   55799(1668546929([{0: "current", 6: 3, 2: 1.5}]))

   Or in hex:

   d9 d9f7                       # tag(55799)
      da 63740171                # tag(1668546929)
         81                      # array(1)
            a3                   # map(3)
               00                # unsigned(0)
               67                # text(7)
                  63757272656e74 # "current"
               06                # unsigned(6)
               03                # unsigned(3)
               02                # unsigned(2)
               f9 3e00           # primitive(15872)

   At the representation level, the unique fingerprint for application/
   senml+cbor is composed of the 8 bytes d9d9f7da63740171 hex, after
   which the unadorned CBOR data (81... for the SenML data) is appended.
```

### §2.3. Enveloping Method: Labeled CBOR Sequence

- (§2.3) "The Labeled CBOR Sequence method is appropriate for use with CBOR Sequences as described in [RFC8742]."  *(`rfc-9277#R-0061`)*
- (§2.3) "This method prepends a newly constructed, separate data item to the CBOR Sequence, the _label_."  *(`rfc-9277#R-0062` — **SEPARATE, so the indicator is outside every signature** — the condition-(4) finding)*
- (§2.3) "The label is a nesting of two tags, similar to but distinct from the CBOR Tag Wrapped methods, with an inner tag content of a constant byte string."  *(`rfc-9277#R-0063`)*
- (§2.3) "The total length of the label is 12 bytes."  *(`rfc-9277#R-0064`)*
- (§2.3) "The outer tag is the self-described CBOR Sequence tag, 55800."  *(`rfc-9277#R-0065`)*
- (§2.3) "The inner tag is a CBOR tag from the First Come First Served space that uniquely identifies the CBOR Protocol."  *(`rfc-9277#R-0066`)*
- (§2.3) "As with the CBOR Tag Wrapped method, the use of a 4-byte tag that encodes without zero bytes is encouraged."  *(`rfc-9277#R-0067`)*
- (§2.3) "The tag content is a 3-byte CBOR byte string containing 0x42_4f_52 ('BOR' in diagnostic notation)."  *(`rfc-9277#R-0068`)*
- (§2.3) "The outer tag in the label identifies the file as being a CBOR Sequence and does so with all the desirable properties explained in Section 3.4.6 of [STD94]."  *(`rfc-9277#R-0069`)*
- (§2.3) "Specifically, it does not appear to conflict with any known file types, and it is not valid Unicode in any Unicode encoding."  *(`rfc-9277#R-0070`)*
- (§2.3) "The inner tag in the label identifies which CBOR Protocol is used, as described above."  *(`rfc-9277#R-0071`)*
- (§2.3) "The inner tag content is a constant byte string that is represented as 0x43_42_4f_52, the ASCII characters "CBOR", which is the CBOR-"  *(`rfc-9277#R-0072`)*
- (§2.3) "encoded data item for the 3-byte string 0x42_4f_52 ('BOR' in diagnostic notation)."  *(`rfc-9277#R-0073`)*
- (§2.3) "The actual CBOR Protocol data then follows as the next data item(s) in the CBOR Sequence, without a need for any further specific tag."  *(`rfc-9277#R-0074`)*
- (§2.3) "The use of a CBOR Sequence allows the application to trivially remove the first item with the two tags."  *(`rfc-9277#R-0075` — **3 of 4**)*
- (§2.3) "Should this file be reviewed by a human (directly in an editor or in a hexdump display), it will include the ASCII characters "CBOR" prominently."  *(`rfc-9277#R-0076` — and the "CBOR" bytes sit at offsets 8–11, **past** the 8-byte fingerprint)*
- (§2.3) "This value is also included simply because the inner nested tag needs to tag something."  *(`rfc-9277#R-0077` — **four of the twelve label bytes exist because CBOR has no zero-arity tag**)*

#### §2.3.1. Example

- (§2.3.1) "To construct an example without registering a new tag, we use ID 272 as assigned for application/missing-blocks+cbor-seq of the "CoAP Content-Formats" registry [RFC9177]."  *(`rfc-9277#R-0078`)*
- (§2.3.1) "Using the technique described in Appendix B, this translates into the tag TN(272) = 1668547090."  *(`rfc-9277#R-0079`)*
- (§2.3.1) "This is a somewhat contrived example, as this is not a media type that is likely to be committed to storage."  *(`rfc-9277#R-0080` — **neither of the two worked examples is a file anyone would store**)*
- (§2.3.1) "At the representation level, the unique fingerprint for application/"  *(`rfc-9277#R-0081`)*
- (§2.3.1) "missing-blocks+cbor-seq is composed of the 8 bytes d9d9f8da63740212 hex, after which the unadorned CBOR sequence (00... for the missing block list given) is appended."  *(`rfc-9277#R-0082`)*

The §2.3.1 envelope in diagnostic notation and in hex, verbatim and complete (source lines 357–376):

```
   55800(1668547090('BOR')),
   0,
   8,
   15

   Or in hex:

   # CBOR sequence with 4 elements
   d9 d9f8         # tag(55800)
      da 63740212  # tag(1668547090)
         43        # bytes(3)
            424f52 # "BOR"
   00 # unsigned(0)
   08 # unsigned(8)
   0f # unsigned(15)

   At the representation level, the unique fingerprint for application/
   missing-blocks+cbor-seq is composed of the 8 bytes d9d9f8da63740212
   hex, after which the unadorned CBOR sequence (00... for the missing
   block list given) is appended.
```

## §3. Security Considerations

**Six sentences. One names a threat that runs against the document's own
purpose, and one names the check-versus-use problem and resolves nothing.**

- (§3) "This document provides a way to identify CBOR Protocol objects."  *(`rfc-9277#R-0083`)*
- (§3) "Clearly identifying CBOR contents in files may have a variety of impacts."  *(`rfc-9277#R-0084`)*
- (§3) "The most obvious is that it may allow malware to identify interesting stored objects, and then exfiltrate or corrupt them."  *(`rfc-9277#R-0085`)*
- (§3) "Protective applications (that check data) cannot rely on the applications they try to protect (that use the data) to make exactly the same decisions in recognizing file formats."  *(`rfc-9277#R-0086` — **named and unresolved** — it is what decides condition (4))*
- (§3) "(This is an instance of a check versus use issue.)"  *(`rfc-9277#R-0087`)*
- (§3) "For example, end-point assessment technologies should not solely rely on the labeling approaches described in this document to decide whether to inspect a given file."  *(`rfc-9277#R-0088` — lower-case *should not*, with **no clause in the document to give it force**)*
- (§3) "Similarly, depending on operating system configurations and related properties of the execution environment, the labeling might influence the default application used to process a file in a way that may not be predicted by a protective application."  *(`rfc-9277#R-0089`)*

## §4. IANA Considerations

- (§4) "These IANA considerations are entirely about CBOR tags in the "Concise Binary Object Representation (CBOR) Tags" registry [IANA.CBOR-TAGS]."  *(`rfc-9277#R-0090` — **every IANA action here is a tag action** — the exact complement of RFC 8742)*
- (§4) "Section 4.1 documents the allocation for a CBOR tag to be used in a CBOR sequence to identify the sequence (an example for using this tag is found in Appendix C)."  *(`rfc-9277#R-0091`)*
- (§4) "Section 4.2 documents the allocation for a CBOR tag to be used in the CBOR-Labeled Non-CBOR Data Enveloping Method (Appendix D, which also shows examples)."  *(`rfc-9277#R-0092`)*
- (§4) "Section 4.3 allocates a CBOR tag for each actual or potential CoAP Content-Format number (examples are in Appendix B)."  *(`rfc-9277#R-0093` — **65,025 tag code points as a function of another registry**)*

### §4.1. Labeled CBOR Sequence Tag

- (§4.1) "IANA has allocated tag 55800 for the Labeled CBOR Sequence Enveloping Method from the "CBOR Tags" registry."  *(`rfc-9277#R-0094`)*
- (§4.1) "IANA has updated this tag registration to point to this document."  *(`rfc-9277#R-0095` — the word *updated* implies the tag **pre-existed** this document; §4.2 says the same without the "has")*
- (§4.1) "This tag is from the First Come First Served area."  *(`rfc-9277#R-0096`)*
- (§4.1) "The value has been picked to have properties similar to the 55799 tag (Section 3.4.6 of [STD94])."  *(`rfc-9277#R-0097`)*
- (§4.1) "The hexadecimal representation of the encoded tag head is 0xd9_d9_f8."  *(`rfc-9277#R-0098`)*
- (§4.1) "This is not valid UTF-8: the first 0xd9 introduces a 3-byte sequence in UTF-8, but the 0xd9 as the second value is not a valid second byte for UTF-8."  *(`rfc-9277#R-0099`)*
- (§4.1) "This is not valid UTF-16: the byte sequence 0xd9d9 (in either endian order) puts this value into the UTF-16 high-half zone, which would signal that this is a 32-bit Unicode value."  *(`rfc-9277#R-0100`)*
- (§4.1) "However, the following 16-bit big-endian value 0xf8_xx is not a valid second sequence according to [RFC2781]."  *(`rfc-9277#R-0101`)*
- (§4.1) "On a little-endian system, it would be necessary to examine the fourth byte to determine if it is valid."  *(`rfc-9277#R-0102`)*
- (§4.1) "That next byte is determined by the subsequent encoding, and Section 3.4.6 of [STD94] has already determined that no valid CBOR encodings result in valid UTF-16."  *(`rfc-9277#R-0103`)*
- (§4.1) "tagged byte string"  *(`rfc-9277#R-0104`)*
- (§4.1) "indicates that the file contains CBOR Sequences"  *(`rfc-9277#R-0105`)*

The §4.1 registry entry for tag 55800, verbatim and complete (source lines 412–443):

```
4.1.  Labeled CBOR Sequence Tag

   IANA has allocated tag 55800 for the Labeled CBOR Sequence Enveloping
   Method from the "CBOR Tags" registry.  IANA has updated this tag
   registration to point to this document.

   This tag is from the First Come First Served area.

   The value has been picked to have properties similar to the 55799 tag
   (Section 3.4.6 of [STD94]).

   The hexadecimal representation of the encoded tag head is 0xd9_d9_f8.

   This is not valid UTF-8: the first 0xd9 introduces a 3-byte sequence
   in UTF-8, but the 0xd9 as the second value is not a valid second byte
   for UTF-8.

   This is not valid UTF-16: the byte sequence 0xd9d9 (in either endian
   order) puts this value into the UTF-16 high-half zone, which would
   signal that this is a 32-bit Unicode value.  However, the following
   16-bit big-endian value 0xf8_xx is not a valid second sequence
   according to [RFC2781].  On a little-endian system, it would be
   necessary to examine the fourth byte to determine if it is valid.
   That next byte is determined by the subsequent encoding, and
   Section 3.4.6 of [STD94] has already determined that no valid CBOR
   encodings result in valid UTF-16.

   Data Item:
      tagged byte string

   Semantics:
      indicates that the file contains CBOR Sequences
```

### §4.2. CBOR-Labeled Non-CBOR Data Tag

- (§4.2) "IANA has allocated tag 55801 for the CBOR-Labeled Non-CBOR Data Enveloping Method (Appendix D) from the "CBOR Tags" registry."  *(`rfc-9277#R-0106`)*
- (§4.2) "IANA updated this tag registration to point to this document."  *(`rfc-9277#R-0107`)*
- (§4.2) "The hexadecimal representation of the encoded tag head is 0xd9_d9_f9."  *(`rfc-9277#R-0108`)*
- (§4.2) "indicates that the file starts with a CBOR-Labeled Non-CBOR Data label."  *(`rfc-9277#R-0109` — `[correction]` 2026-10-21, pass 3: this bullet quoted only the first of the value's two source lines, ending at "Data". Pass 2 found that truncation, restored `label.` in `requirements.yaml` and in `messages.yaml`'s `Semantics` value, and left this bullet short — so the file that exists to carry the normative text verbatim was the one still carrying it truncated. Source lines 476/477 break at a **space**, not a hyphen, so the full value is one contiguous span)*

The §4.2 registry entry for tag 55801, verbatim and complete (source lines 445–477):

```
4.2.  CBOR-Labeled Non-CBOR Data Tag

   IANA has allocated tag 55801 for the CBOR-Labeled Non-CBOR Data
   Enveloping Method (Appendix D) from the "CBOR Tags" registry.  IANA
   updated this tag registration to point to this document.

   This tag is from the First Come First Served area.

   The value has been picked to have properties similar to the 55799 tag
   (Section 3.4.6 of [STD94]).

   The hexadecimal representation of the encoded tag head is 0xd9_d9_f9.

   This is not valid UTF-8: the first 0xd9 introduces a 3-byte sequence
   in UTF-8, but the 0xd9 as the second value is not a valid second byte
   for UTF-8.

   This is not valid UTF-16: the byte sequence 0xd9d9 (in either endian
   order) puts this value into the UTF-16 high-half zone, which would
   signal that this is a 32-bit Unicode value.  However, the following
   16-bit big-endian value 0xf9_xx is not a valid second sequence
   according to [RFC2781].  On a little-endian system, it would be
   necessary to examine the fourth byte to determine if it is valid.
   That next byte is determined by the subsequent encoding, and
   Section 3.4.6 of [STD94] has already determined that no valid CBOR
   encodings result in valid UTF-16.

   Data Item:
      tagged byte string

   Semantics:
      indicates that the file starts with a CBOR-Labeled Non-CBOR Data
      label.
```

### §4.3. CBOR Tags for CoAP Content-Format Numbers

- (§4.3) "IANA allocated the tag numbers 1668546817 (0x63740101) to 1668612095 (0x6374ffff) as follows:"  *(`rfc-9277#R-0110`)*
- (§4.3) "byte string or any CBOR data item (see Appendix B)"  *(`rfc-9277#R-0111`)*
- (§4.3) "the representation of content-format ct < 65025 is indicated by tag number TN(ct) = 0x63740101 + (ct / 255) * 256 + ct % 255"  *(`rfc-9277#R-0112` — **a C expression as a registry semantics field, and the registry text does not define its arithmetic**)*
- (§4.3) "The "CoAP Content-Formats" registry [IANA.CORE-PARAMETERS] is defined in Section 12.3 of [RFC7252]."  *(`rfc-9277#R-0113`)*

The §4.3 registry entry for the content-format tag block, verbatim and complete (source lines 479–496):

```
4.3.  CBOR Tags for CoAP Content-Format Numbers

   IANA allocated the tag numbers 1668546817 (0x63740101) to 1668612095
   (0x6374ffff) as follows:

   Data Item:
      byte string or any CBOR data item (see Appendix B)

   Semantics:
      the representation of content-format ct < 65025 is indicated by
      tag number
      TN(ct) = 0x63740101 + (ct / 255) * 256 + ct % 255

   Reference:
      RFC 9277

   The "CoAP Content-Formats" registry [IANA.CORE-PARAMETERS] is defined
   in Section 12.3 of [RFC7252].
```

## Appendix A. Advice to Protocol Designer

**Declared informative by §1. Three survey questions and no rule.**

- (Appendix A) "This document introduces a choice between wrapping a single CBOR data item into a pair of identifying CBOR tags or prepending an identifying encoded CBOR data item (which, in turn, contains a pair of identifying CBOR tags) to a CBOR Sequence (which might be a single data item)."  *(`rfc-9277#R-0114`)*
- (Appendix A) "Which should a protocol designer use?"  *(`rfc-9277#R-0115`)*
- (Appendix A) "Both the Labeled CBOR Sequence and the wrapped tag can be trivially removed by an application before sending the CBOR content out on the wire."  *(`rfc-9277#R-0116` — **4 of 4** — *and the four together make the envelope storage-only by design*)*
- (Appendix A) "The Labeled CBOR Sequence can be slightly easier to remove as, in most cases, CBOR parsers will return it as a unit and then return the actual CBOR item, which could be anything at all and could include CBOR tags that _do_ need to be sent on the wire."  *(`rfc-9277#R-0117`)*
- (Appendix A) "On the other hand, having the Labeled CBOR Sequence in the file requires that all programs that expect to examine that file be able to skip what appears to be a CBOR item with two tags nested around a 3-byte byte string."  *(`rfc-9277#R-0118` — **the ONE explicit warning, and it runs the other way**)*
- (Appendix A) "The 3-byte entry is not of the format the program would normally have processed, so it may be a surprise."  *(`rfc-9277#R-0119`)*
- (Appendix A) "On the other hand, CBOR parsers are generally tolerant of tags that appear: many of them will process extra tags, making unknown tags available as meta information."  *(`rfc-9277#R-0120`)*
- (Appendix A) "A program that is not expecting those tags may just ignore them."  *(`rfc-9277#R-0121`)*
- (Appendix A) "As an example of where there was a problem with previous security systems, "PEM" format certificate files grew to be able to contain multiple certificates by simple concatenation."  *(`rfc-9277#R-0122`)*
- (Appendix A) "The PKCS1 format [RFC8017] could also contain a private key object followed by one or more certificate objects, but only when in PEM format."  *(`rfc-9277#R-0123`)*
- (Appendix A) "Annoyingly, when in binary DER format ([X.690], which like CBOR is self-"  *(`rfc-9277#R-0124`)*
- (Appendix A) "delimiting), concatenation of certificates was not compatible with most programs as they did not expect to read more than one item in the file."  *(`rfc-9277#R-0125`)*
- (Appendix A) "The use of CBOR Tag Wrapped format is easier to retrofit to an existing format with existing and unchangeable stored format for a single CBOR data item."  *(`rfc-9277#R-0126`)*
- (Appendix A) "This new sequence of tags is expected to be trivially ignored by many existing programs when reading CBOR from files or similar units of storage, even if the program only supports decoding a single data item (and not a CBOR sequence)."  *(`rfc-9277#R-0127`)*
- (Appendix A) "But, a naive program might also then transmit the additional tags across the network."  *(`rfc-9277#R-0128`)*
- (Appendix A) "Removing the CBOR Tag Wrapped format requires knowledge of the two tags involved."  *(`rfc-9277#R-0129`)*
- (Appendix A) "Other tags present might be needed."  *(`rfc-9277#R-0130`)*
- (Appendix A) "For a representation matching a specific media-type that is carried in a CBOR byte string, the byte string head will already have to be removed for use as such a representation, so it should be easy to remove the enclosing tag heads as well."  *(`rfc-9277#R-0131`)*
- (Appendix A) "This is of particular interest with the predefined tags provided in Appendix B for media types with CoAP Content-Format numbers."  *(`rfc-9277#R-0132`)*
- (Appendix A) "Some considerations in the form of survey questions follow."  *(`rfc-9277#R-0133`)*

### Appendix A.1. Is the on-wire format new?

- (Appendix A.1) "If the on-wire format is new, then it could be specified with the CBOR Tag Wrapped format if the extra 8 bytes are not a problem."  *(`rfc-9277#R-0134`)*
- (Appendix A.1) "The stored format is then identical to the on-wire format."  *(`rfc-9277#R-0135`)*
- (Appendix A.1) "If the 8 bytes are a problem on the wire (and they often are if CBOR is being considered), then the Labeled CBOR Sequence format should be adopted for the stored format."  *(`rfc-9277#R-0136`)*

### Appendix A.2. Can many items be trivially concatenated?

**This is the record's headline finding.** RFC 8742 §2 states that
"concatenating zero or more CBOR Sequences also results in a CBOR Sequence" —
so `cat a.seq b.seq > c.seq` is in spec, and it is the whole reason to pick a
sequence over an array. This appendix then says that doing it to *labelled*
sequences needs care, and leaves the rule to each protocol with no default.

- (Appendix A.2) "If the programs that read the contents of the file already expect to process all of the CBOR data items in the file (not just the first), then the Labeled CBOR Sequence format may be easily retrofitted."  *(`rfc-9277#R-0137`)*
- (Appendix A.2) "The programs involved may throw errors or warnings on the Labeled CBOR Sequence if they have not yet been updated, but this may not be a problem."  *(`rfc-9277#R-0138`)*
- (Appendix A.2) "There are situations where multiple objects may be concatenated into a single file."  *(`rfc-9277#R-0139`)*
- (Appendix A.2) "If each object is preceded by a Labeled CBOR Sequence label, then there may be multiple such labels in the file."  *(`rfc-9277#R-0140` — **the state the document creates and then declines to define**)*
- (Appendix A.2) "A protocol based on CBOR Sequences may specify that Labeled CBOR Sequence labels can occur within a CBOR Sequence, possibly even to switch to data items following in the sequence that are of a different type."  *(`rfc-9277#R-0141` — **the opposite reading of the same fact, and the document chooses neither**)*
- (Appendix A.2) "If the CBOR-Sequence-based protocol does not define the semantics for or at least tolerate embedded labels, care must be taken when concatenating Labeled CBOR Sequences to remove the label from all but the first part."  *(`rfc-9277#R-0142` — **the headline finding**: lower-case "must", rule delegated to each protocol with no default)*
- (Appendix A.2) "As an example from legacy PEM-encoded PKIX certificates, many programs accept a series of PKIX certificates in a single file in order to set up a certificate chain."  *(`rfc-9277#R-0143` — inside an RFC v3 **aside** (source lines 715–727 or 765–777); contiguous **only** after the leading `|` bar is removed, and after nothing else)*
- (Appendix A.2) "This mechanism actually only works for PEM-encoded certificates, and not DER-encoded certificates."  *(`rfc-9277#R-0144` — inside an RFC v3 **aside** (source lines 715–727 or 765–777); contiguous **only** after the leading `|` bar is removed, and after nothing else)*
- (Appendix A.2) "One of the reasons for this specification is to make sure that CBOR-"  *(`rfc-9277#R-0145` — inside an RFC v3 **aside** (source lines 715–727 or 765–777); contiguous **only** after the leading `|` bar is removed, and after nothing else)*
- (Appendix A.2) "encoded certificates do not suffer from this problem."  *(`rfc-9277#R-0146` — inside an RFC v3 **aside**, but contiguous **either way** — the span begins at the start of its line, so it does not depend on the bar strip)*
- (Appendix A.2) "As an example of mixing of types, some TLS server programs also can accept both their PEM-encoded private key and their PEM-"  *(`rfc-9277#R-0147` — inside an RFC v3 **aside** (source lines 715–727 or 765–777); contiguous **only** after the leading `|` bar is removed, and after nothing else)*
- (Appendix A.2) "If only one item is ever expected in the file, the use of the Labeled CBOR Sequence may present an implementation hurdle to programs that previously just read a single data item and used it."  *(`rfc-9277#R-0148`)*

The Appendix A.2 aside, verbatim **with its `|` bars intact** (contrast the bullets above, which have them removed) (source lines 715–727):

```
      |  As an example from legacy PEM-encoded PKIX certificates, many
      |  programs accept a series of PKIX certificates in a single file
      |  in order to set up a certificate chain.  The file would contain
      |  not just the End-Entity (EE) certificate, but also any
      |  subordinate certification authorities (CAs) needed to validate
      |  the EE.  This mechanism actually only works for PEM-encoded
      |  certificates, and not DER-encoded certificates.  One of the
      |  reasons for this specification is to make sure that CBOR-
      |  encoded certificates do not suffer from this problem.
      |  
      |  As an example of mixing of types, some TLS server programs also
      |  can accept both their PEM-encoded private key and their PEM-
      |  encoded certificate in the same file.
```

### Appendix A.3. Are there tags at the start?

- (Appendix A.3) "If the Protocol expects to use other tags at its top level, then the use of the CBOR Tag Wrapped format may be easy to explain at the same place in the protocol description."  *(`rfc-9277#R-0149`)*

## Appendix B. CBOR Tags for CoAP Content Formats

- (Appendix B) "Section 5.10.3 of [RFC7252] defines the concept of a Content-Format, which is a short, 16-bit unsigned integer that identifies a specific content type (media type plus (optionally) parameters), optionally together with a content coding (see Section 8.4.1 of [RFC9110])."  *(`rfc-9277#R-0150`)*
- (Appendix B) "Outside of a transfer protocol that indicates the Content-Format for a representation, it may be necessary to identify the Content-Format of the representation when it is stored in a file, in firmware, or when debugging."  *(`rfc-9277#R-0151`)*
- (Appendix B) "This specification allocates CBOR tag numbers 1668546817 (0x63740101) to 1668612095 (0x6374FFFF) for the tagging of representations of specific content formats."  *(`rfc-9277#R-0152`)*
- (Appendix B) "Using tags from this range, a byte string that is to be interpreted as a representation of Content-Format number ct, with ct < 65025 (255*255), can be identified by enclosing it in a tag with tag number TN(ct) where:"  *(`rfc-9277#R-0153`)*
- (Appendix B) "TN(ct) = 0x63740101 + (ct / 255) * 256 + ct % 255."  *(`rfc-9277#R-0154`)*
- (Appendix B) "(where +, *, / and % stand for integer addition, multiplication, division, and remainder as in the programming language C [C].)"  *(`rfc-9277#R-0155` — **defined here only, by reference to a paywalled ISO standard — and §4.3's registry entry does not carry this citation**)*
- (Appendix B) "This formula avoids the use of zero bytes in the representation of the tag number."  *(`rfc-9277#R-0156` — inside an RFC v3 **aside** (source lines 715–727 or 765–777); contiguous **only** after the leading `|` bar is removed, and after nothing else; **correct and stronger than stated**: no image value contains a zero byte in *any* of its four)*
- (Appendix B) "Note that no tag numbers are assigned for Content-Format numbers in the following range:"  *(`rfc-9277#R-0157` — inside an RFC v3 **aside** (source lines 715–727 or 765–777); contiguous **only** after the leading `|` bar is removed, and after nothing else)*
- (Appendix B) "(This range is in the range reserved for Experimental Use [RFC8126] by Section 12.3 of [RFC7252].  The overlap of 25 code points between this experimental range with the range this appendix defines tag numbers for can be used for experiments that want to employ a tag number.)"  *(`rfc-9277#R-0158` — inside an RFC v3 **aside** (source lines 715–727 or 765–777); contiguous **only** after the leading `|` bar is removed, and after nothing else; the only basis for inferring RFC 7252 §12.3's range, and **RFC 7252 is not held here**)*
- (Appendix B) "Exceptionally, when used immediately as tag content of one of the tags 55799, 55800, or 55801, the tag content is as follows:"  *(`rfc-9277#R-0159` — **an exception that changes the tag content depending on what encloses it**)*
- (Appendix B) "The CBOR data item within the representation (without byte-"  *(`rfc-9277#R-0160`)*
- (Appendix B) "string wrapping).  This only works for Content-Formats that are represented by a single CBOR data item in identity content-coding."  *(`rfc-9277#R-0161`)*
- (Appendix B) "The data items in the CBOR sequence within the representation, without byte string wrapping, but wrapped in a CBOR array."  *(`rfc-9277#R-0162`)*
- (Appendix B) "This works for Content-Formats that are represented by a CBOR sequence in identity content-coding."  *(`rfc-9277#R-0163` — and **identity content-coding only** — so TN(ct) inside 55799 for a deflate coding has no defined content)*
- (Appendix B) "the byte string 'BOR', signifying that the representation of the given content-"  *(`rfc-9277#R-0164`)*
- (Appendix B) "format follows in the file, in the way defined for these tags."  *(`rfc-9277#R-0165`)*

The Appendix B allocation, the TN formula and its aside, verbatim **with the `|` bars and the two U+2264 characters intact** (source lines 751–777):

```
   This specification allocates CBOR tag numbers 1668546817 (0x63740101)
   to 1668612095 (0x6374FFFF) for the tagging of representations of
   specific content formats.

   Using tags from this range, a byte string that is to be interpreted
   as a representation of Content-Format number ct, with ct < 65025
   (255*255), can be identified by enclosing it in a tag with tag number
   TN(ct) where:

      TN(ct) = 0x63740101 + (ct / 255) * 256 + ct % 255.

   (where +, *, / and % stand for integer addition, multiplication,
   division, and remainder as in the programming language C [C].)

      |  This formula avoids the use of zero bytes in the representation
      |  of the tag number.
      |  
      |  Note that no tag numbers are assigned for Content-Format
      |  numbers in the following range:
      |  
      |     65025 ≤ ct ≤ 65535
      |  
      |  (This range is in the range reserved for Experimental Use
      |  [RFC8126] by Section 12.3 of [RFC7252].  The overlap of 25 code
      |  points between this experimental range with the range this
      |  appendix defines tag numbers for can be used for experiments
      |  that want to employ a tag number.)
```

### Appendix B.1. Content-Format Tag Examples

- (Appendix B.1) "The "CoAP Content-Formats" registry [IANA.CORE-PARAMETERS] defines content formats that can be used as examples:"  *(`rfc-9277#R-0166`)*
- (Appendix B.1) "As discussed in Section 2.2.1, Content-Format ID 112 represents the application/senml+cbor media type (no parameters)."  *(`rfc-9277#R-0167`)*
- (Appendix B.1) "The corresponding tag number is TN(112) = 1668546929."  *(`rfc-9277#R-0168`)*
- (Appendix B.1) "The following CDDL snippet can be used to identify application/"  *(`rfc-9277#R-0169` — `[correction]` 2026-10-20, pass 2: this bullet was labelled `rfc-9277#R-0174` at pass 1, which is the **second** occurrence of the same sentence, eight bullets below. The text is byte-identical, so the mis-join was invisible to every check in `bin/`)*
- (Appendix B.1) "senml+cbor representations:"  *(**no id.** `[correction]` 2026-10-20, pass 2: the second half of `rfc-9277#R-0169`'s sentence, cut at the source's own line-end break after "application/" at source line 807/808, was never extracted at pass 1 — the only unpaired break half in this record besides `rfc-9277#R-0147`'s. Recorded here rather than given an id, because ids are append-only and this record's `requirements.yaml` asserts source order with no gaps. See `requirements.yaml` `verify_pass`)*
- (Appendix B.1) "Note that a byte string is used as the type of the tag content because a media type representation in general can be any byte string."  *(`rfc-9277#R-0170` — **contradicts Appendix B's "Exceptionally" rule for the document's own §2.2.1 example**)*
- (Appendix B.1) "Content-Format ID 272 represents the application/missing-"  *(`rfc-9277#R-0171`)*
- (Appendix B.1) "blocks+cbor-seq media type, which is a CBOR sequence [RFC9177]."  *(`rfc-9277#R-0172`)*
- (Appendix B.1) "The corresponding tag number is TN(272) = 1668547090."  *(`rfc-9277#R-0173`)*
- (Appendix B.1) "The following CDDL snippet can be used to identify application/"  *(`rfc-9277#R-0174`)*
- (Appendix B.1) "missing-blocks+cbor-seq representations as embedded in a CBOR byte string:"  *(`rfc-9277#R-0175`)*

The `senml-cbor` CDDL snippet, verbatim (source lines 810–810):

```
      senml-cbor = #6.1668546929(bstr)
```

The `missing-blocks` CDDL snippet, verbatim (source lines 825–825):

```
      missing-blocks = #6.1668547090(bstr)
```

## Appendix C. Example from Openswan

- (Appendix C) "The Openswan IPsec project has a daemon ("pluto") and two control programs ("addconn" and "whack")."  *(`rfc-9277#R-0176`)*
- (Appendix C) "They communicate via a Unix-domain socket, over which a C-structure containing pointers to strings is serialized using a bespoke mechanism."  *(`rfc-9277#R-0177`)*
- (Appendix C) "The above magic number is included in the file and on the IPC in order to distinguish the "shutdown" command CBOR operation."  *(`rfc-9277#R-0178` — **a forward reference**: the tag it calls *above* is allocated three paragraphs later)*
- (Appendix C) "In order to reduce the problems due to serialization, the serialization is being changed to CBOR."  *(`rfc-9277#R-0179`)*
- (Appendix C) "Additionally, this change allows the IPC to be described by CDDL and any implementation language to be used that can encode CBOR."  *(`rfc-9277#R-0180`)*
- (Appendix C) "IANA has allocated the tag 1330664270 or 0x4f_50_53_4e for this purpose."  *(`rfc-9277#R-0181` — **the one named deployment — and its registry row cites two people, not RFC 9277**)*
- (Appendix C) "As a result, each file and each IPC is prefixed with a CBOR Sequence tag."  *(`rfc-9277#R-0182`)*

The Appendix C Openswan label in diagnostic notation and in hex, verbatim and complete (source lines 857–864):

```
   55800(1330664270(h'424F52'))

   Or in hex:

   d9 d9f8         # tag(55800)
      da 4f50534e  # tag(1330664270)
         43        # bytes(3)
            424f52 # "BOR"
```

## Appendix D. Using CBOR Labels for Non-CBOR Data

- (Appendix D) "The CBOR-Labeled Non-CBOR data method is appropriate for adding a magic number to a Non-CBOR data format, particularly one that can be described by a Content-Format tag (Appendix B)."  *(`rfc-9277#R-0183`)*
- (Appendix D) "This method prepends a CBOR data item to the Non-CBOR data; this data item is called the "header" and, similar to the Labeled CBOR-Sequence label, consists of two nested tags around a constant byte string for a total of 12 bytes."  *(`rfc-9277#R-0184`)*
- (Appendix D) "The outer tag is the CBOR-Labeled Non-CBOR Data tag, 55801."  *(`rfc-9277#R-0185`)*
- (Appendix D) "As with CBOR Tag Wrapped, the use of a 4-byte tag is encouraged that encodes without zero bytes."  *(`rfc-9277#R-0186`)*
- (Appendix D) "The tag content is a 3-byte CBOR byte string containing 0x42_4F_52 ('BOR' in diagnostic notation)."  *(**no id.** `[correction]` 2026-10-20, pass 2: dropped at pass 1, source line 881/882. It is numbered item **3** of Appendix D's own three-item header structure, and items 1 and 2 are `rfc-9277#R-0185` and `rfc-9277#R-0186` — so the structure was extracted two-thirds complete, and `messages.yaml`'s `byte-string head and constant content` field had no statement of its own to cite. **It also carries a source defect of its own:** the constant is written `0x42_4F_52` here and `0x42_4f_52` in §2.3 and in Appendix D's own next-but-one paragraph — the same class as `0x6374ffff` against `0x6374FFFF` in `design-notes.md` §7 defect 8)*
- (Appendix D) "The outer tag in the label identifies the file as being prefixed by a Non-CBOR data label and does so with all the desirable properties explained in Section 3.4.6 of [STD94]."  *(`rfc-9277#R-0187`)*
- (Appendix D) "The inner tag in the label identifies which Non-CBOR Protocol is used."  *(`rfc-9277#R-0188`)*
- (Appendix D) "The actual Non-CBOR Protocol data then follow directly appended to the CBOR representation of the header."  *(`rfc-9277#R-0189`)*
- (Appendix D) "This allows the application to trivially remove the header item with the two nested tags and the byte string."  *(`rfc-9277#R-0190`)*
- (Appendix D) "As with the Labeled CBOR Sequence {#sequences}, this choice of the tag content places the ASCII characters "CBOR" prominently into the header."  *(`rfc-9277#R-0191` — **an unresolved kramdown anchor, in the published RFC**)*

### Appendix D.1. Content-Format Tag Examples

- (Appendix D.1) "Content-Format ID 432 represents the application/td+json media type (no parameters)."  *(`rfc-9277#R-0192`)*
- (Appendix D.1) "The corresponding tag number is TN(432) = 1668547250."  *(`rfc-9277#R-0193`)*
- (Appendix D.1) "The following CDDL snippet can be used to identify a CBOR-Labeled Non-CBOR data for application/td+json representations:"  *(**no id.** `[correction]` 2026-10-20, pass 2: dropped at pass 1, source lines 918–919. Note the wording: it is **not** Appendix B.1's "The following CDDL snippet can be used to identify application/…" but a distinct sentence naming the CBOR-Labeled Non-CBOR Data method, so it is not covered by `rfc-9277#R-0169` or `rfc-9277#R-0174`)*
- (Appendix D.1) "Content-Format 11050 represents the application/json media type in deflate content-coding."  *(`rfc-9277#R-0194`)*
- (Appendix D.1) "The corresponding tag number is TN(11050) = 1668557910."  *(`rfc-9277#R-0195`)*
- (Appendix D.1) "The following CDDL snippet can be used to identify a CBOR-Labeled Non-CBOR data for application/json representations compressed in deflate content-coding:"  *(**no id.** `[correction]` 2026-10-20, pass 2: dropped at pass 1, source lines 928–930. It is the sentence that puts a **non-identity content-coding** inside the document's own worked examples, which is the witness for `design-notes.md` §7 defect 4 — so the record argued that defect without quoting its own evidence)*

The `td-json-header` CDDL snippet, verbatim (source lines 923–923):

```
      td-json-header = #6.55801(#6.1668547250('BOR'))
```

The `json-deflate-header` CDDL snippet, verbatim (source lines 934–934):

```
      json-deflate-header = #6.55801(#6.1668557910('BOR'))
```

---

## What is NOT in this file, and why

- **§5 References, the Acknowledgements, the Contributors list and the Authors'
  Addresses.** Dropped per `.claude/skills/extract` §1. The
  reference-classification facts are recorded in `design-notes.md` because they
  bear on citation rather than conformance: the **normative** references are
  **`[C]`** (ISO/IEC 9899:2018, paywalled), **`[RFC8742]`** and **`[STD94]`**
  (RFC 8949) — just three — while `[RFC6838]`, `[RFC7252]`, `[RFC8126]`,
  `[RFC8152]`, `[RFC8610]`, `[RFC9110]`, `[RFC9177]`, `[RFC2781]`, `[RFC20]`
  and `[X.690]` are **informative**. So `[C]`, used only in an **appendix**, is
  normative, while RFC 7252 — whose registry §4.3 makes 65,025 tag code points
  a function of, and whose §12.3 defines the experimental range Appendix B's
  aside reasons about — is informative.
- **§1's history of file type identification** (Unix, classical Mac OS, file
  extensions, web servers). Narrative. The PEM-disarray paragraph *is* kept
  (`rfc-9277#R-0017`), because it is the out-of-band substitute failing at
  exactly the job this document gives to in-band bytes.
- **No BCP 14 boilerplate, because there is none.** See the header.

### `[correction]` 2026-10-20 — what pass 2 found missing, and where it put it

Pass 1 reported this file as 195 spans against 195 requirement entries, with no
statement dropped. A sentence-level coverage sweep of the whole source at pass 2
— mark every character covered by some requirement `text`, then read every
uncovered run of 60 characters or more — found **nine statements with no entry of
their own**. Six are now bullets above, marked **no id**; three are reachable
only through a fenced block and are listed here. Nothing was renumbered: ids are
stable forever, and this record's `requirements.yaml` asserts source order with
no gaps, so a statement found at pass 2 cannot be given the next free number
without breaking that claim. `requirements.yaml` `verify_pass` holds the full list.

- **§4.2 repeats §4.1 almost word for word and was re-extracted only in part.**
  §4.1 carries twelve entries (`rfc-9277#R-0094`–`R-0105`); §4.2 carries four
  (`R-0106`–`R-0109`). The eight that are not re-extracted are byte-identical to
  §4.1's — except **one**, which is not: "However, the following 16-bit
  big-endian value 0xf9_xx is not a valid second sequence according to
  [RFC2781]." — note the `f9` — against `rfc-9277#R-0101`'s `0xf8_xx`.
  *(`[correction]` 2026-10-21, pass 3: the `**` emphasis markers were inside the
  quoted span, so the span as written was not the source's bytes; the emphasis
  is now outside it.)* That is a materially
  different statement about a different tag and it has no entry. It is in this
  file, inside the complete §4.2 registry block above, and in
  `schema/registrations.txt` region R02 — so it is held, not lost, and only the
  requirement-level index is short.
- **One sentence of the Appendix A.2 aside.** "The file would contain not just
  the End-Entity (EE) certificate, but also any subordinate certification
  authorities (CAs) needed to validate the EE." sits between
  `rfc-9277#R-0143` and `rfc-9277#R-0144` and has no entry of its own. It is in
  the aside block above.
- **And one unpaired break half inside the aside.** `rfc-9277#R-0147` ends at
  the source's line-end break — "…their PEM-encoded private key and their PEM-"
  — and the remainder, "encoded certificate in the same file.", was never
  extracted. With `rfc-9277#R-0169`'s missing half (above) these are the only
  two of the **fifteen** line-end word breaks whose halves do not pair — and
  `rfc-9277#R-0147`'s break is **inside an aside**, not in the body.
  *(`[correction]` 2026-10-21, pass 3: this read "the thirteen in-body word
  breaks". Neither figure described the census: thirteen of the fifteen are in
  the body and two are inside asides, and one of the two unpaired halves is one
  of those two aside breaks, so "in-body" was wrong of this very sentence. See
  the census above.)*

**Not counted above, recorded so the shape is visible.** The document re-states
whole paragraphs verbatim in two places, and in each case only the first
occurrence has entries: seven of §4.2's eight repeated sentences are
byte-identical to §4.1's, and **two of Appendix D's paragraphs are byte-identical
to §2.3's** — "Specifically, it does not appear to conflict with any known file
types, and it is not valid Unicode in any Unicode encoding."
(`rfc-9277#R-0070`, locator §2.3) and the two halves of "The inner tag content is
a constant byte string that is represented as 0x43_42_4f_52, …"
(`rfc-9277#R-0072`/`R-0073`, locator §2.3). Those statements are held; it is the
**locator** that is short, because an entry filed at §2.3 does not tell a reader
that Appendix D asserts the same thing of a different tag. Sixteen requirement
texts in this record occur twice in the source, and only two of the sixteen were
given one id per occurrence — the two in `verify_pass`, which is why they were
also the two the wrong ids hid in.

---
record: sigstore-bundle-0-3
kind: design-notes
title: "sigstore-bundle-0-3 — bearing on our design"
extracted: "2026-11-20"
reviewed_by: ""
---

# Sigstore Bundle v0.3 — bearing on our design

The source is five digest-pinned files rendered by `distilled/render-source.py`
into one text, `.cache/sigstore-bundle-0-3.txt` (1189 lines, sha256
`425599709e999efdc09aade3e4e8bc7e530bd2c7c0a0d89266607c9a1ff119d3`, equal to
`requirements.yaml`'s `source_digest`): `protos/sigstore_bundle.proto` (§1,
L1-193; sha256 `bf8d01cc…0792`, record.yaml:20), the three Sigstore files it
imports at the same commit, `envelope.proto` (§2, L195-265, the DSSE envelope),
`sigstore_common.proto` (§3, L267-672) and `sigstore_rekor.proto` (§4,
L674-868), and the docs page `content/en/about/bundle.md` (§5, L870-1189),
each pinned in record.yaml:24 and in `render-source.py`'s digest table. This
pass recomputed all five input digests and re-rendered the text byte for byte
(§7 check 9). `bin/bcp14-count` finds 73 keywords; `requirements.yaml` holds
R-0001 to R-0197.

The source defines a **container**: a version string (`media_type`),
**verification material** (key material in one of three forms, transparency-log
entries, RFC 3161 timestamps) and **content**, either a signature over an
artifact (`message_signature`) or a DSSE envelope that must carry exactly one
signature (`dsse_envelope`). It also carries the DSSE envelope and its
pre-authentication encoding (§2), the algorithm enums (§3), Rekor's log-entry
messages (§4), and a page with two complete example bundles (§5). **It does
not define** the trust root a verifier holds, the verification procedure (it
links a Google document for that), Rekor's entry bodies or the canonical JSON
the log signs, the checkpoint format, the Merkle leaf hash, how a timestamp
authority is trusted, revocation, thresholds, or any way to carry two
signatures.

It reaches us in five ways (record.yaml:51-55 lists R-I-02, R-I-03, R-O-05 and
DEC-005):

1. **T-052** (BACKLOG:189) and the I4 demo (PLAN-0001:487). Real SLSA
   provenance arrives in this container, mofn's own wallet releases included
   (PLAN-0004:383-385). §5 says what a byte-faithful import keeps.
2. **DEC-005**, open (ARCH-0001:71-73, ARCH-0001:643-645). In the provenance
   mofn imports and publishes (LANE-A-03:13-14; PLAN-0004:383-385), the DSSE
   option arrives as a one-signature envelope inside a bundle, which is not
   ITE-5 (§3.4).
3. **R-O-05** (ARCH-0001:467). The source agrees with its authenticated type
   and its rule against trusting unverified copies (A-01, A-02), carries signed
   bytes for exactly R-O-05's reason (A-03), and makes an importer that checks
   the log's promise canonicalise during verification (K-01).
4. **R-I-02 and R-I-03** (ARCH-0001:452-453). Verifying a bundle needs a
   foreign trust root (C-02), and an export a Sigstore verifier accepts needs
   more than an envelope (§4.3).
5. **MD-3 and ADR-0004** (DEC-002, option 5). §4 gives the field-by-field
   mapping and where the source cuts against option 5.

What it is not: the in-toto Statement inside the envelope (library#134,
`in-toto-attestation-v1`), the in-toto Envelope layer (`in-toto-envelope-v1`),
DSSE's own specification (`secure-systems-lab-dsse`), or SLSA provenance
(`slsa-provenance-1-2`); each is read here only where this source points at it.

## Things to hold while reading

1. **Our decisions are read from m-of-n at `656bac0`**
   (`656bac0668d771e221fcbf02ff556cbcc6622b29`, committed 2026-11-17), with
   `git show 656bac0:<path>`, never a working tree. A citation `DOC:n` or
   `DOC:n-m` is a line range of that blob, and every one in this file is
   written in full, never as a bare `:n`. **No mofn text is quoted**: every
   citation is a paraphrase, and §10 says how each range was read back beside
   its claim.

   | name | path at 656bac0 | standing |
   |---|---|---|
   | ARCH-0001 0.3.2 | `spec/ARCH-0001-authorization-attestation.md` | draft. R-I-01 to R-I-03 ARCH-0001:451-453, R-O-03 ARCH-0001:465, R-O-05 ARCH-0001:467, §6 matrix ARCH-0001:496-515. **DEC-005 open** (ARCH-0001:71-73, ARCH-0001:643-645) |
   | ARCH-0002 0.10.0 | `spec/ARCH-0002-key-relative-naming.md` | draft; P1 accepted (ADR-0001); P5 with P5.1, P5.2 accepted (ADR-0002); P1.1 draft (ARCH-0002:54-58) |
   | ADR-0002 1.0.0 | `spec/ADR-0002-provisional-principles.md` | accepted, `reviewed: false` |
   | ADR-0003 1.0.1 | `spec/ADR-0003-ksa-core-decisions.md` | accepted; D2 one canonical encoding, D3 anchors, D4 contexts |
   | ADR-0004 1.0.0 | `spec/ADR-0004-dec-002-encoding.md` | **accepted 2026-10-25, `reviewed: false`**: DEC-002 is option 5; COSE_Sign1 and DSSE export envelopes only; DEC-005 not decided (ADR-0004:51-52, ADR-0004:112) |
   | ADR-0005 1.0.0 | `spec/ADR-0005-dec-003-key-identifier.md` | accepted, `reviewed: false`; its Interchange section ADR-0005:87-92 |
   | SPEC-0001 0.1.0, SPEC-0002 0.10.1, SPEC-0004 0.6.2 | `spec/SPEC-000{1,2,4}-*.md` | draft; govern where an ARCH document differs (ADR-0003) |
   | MD | `project/meetings/2026-09-28.md` | MD-3 at MD:51-54, closed by ADR-0004's acceptance (ADR-0004:132-133) |
   | DECISIONS 0.8.0, BACKLOG 0.16.0, PLAN-0001 0.7.1, PLAN-0004 0.6.0 | `project/…` | register, backlog, plans. T-051…T-053 BACKLOG:188-190; L-041 BACKLOG:268; release decisions PLAN-0004:389-405 |
   | RELEASE | `.github/workflows/release.yml` | the workflow PLAN-0004 D2 describes |
   | DL-0043p, DL-0043r, DL-0047r | `design-log/0043-release-builds/{produced,review}.md`, `design-log/0047-l-041-d7-extraction/review.md` | design log |
   | LANE-A-03, LANE-A-README, LANE-A-COMMON | `prototype/lane-a/03_slsa_provenance.py`, `README.md`, `common.py` | a throwaway that decides nothing (LANE-A-README:3); the only mofn code that reads a Sigstore bundle |

   Library files are cited by path and line: `record.yaml:n` is this record's;
   `ITE:Ln` is a line of `in-toto-envelope-v1`'s source (its `envelope.md`,
   sha256 `c02c6588…5d11`, equal to that record's `content.sha256`), and
   `ITE-DN:n` a line of its `distilled/design-notes.md` at
   `origin/fx1-in-toto-envelope-136` (`23c0d40`, PR #141), the precedent the
   issue names; `RFC6962:n` is a line of the library's cached RFC 6962 text
   (sha256 equal to `rfc-6962/record.yaml:19`); `SLSA-DN:n` a line of
   `slsa-provenance-1-2`'s `distilled/design-notes.md` at
   `origin/fx1-slsa-provenance-136` (`1bc07e5`, PR #143).

   **`docs/extraction.md` is stale on one point**, as ITE-DN:90-93 already
   recorded: it says no DEC-002 ADR exists (docs/extraction.md:128-131). At
   `656bac0` ADR-0004 accepts DEC-002 for option 5. This file maps against
   ADR-0004 and still records where the source cuts against option 5, as
   docs/extraction.md:133-135 asks.

2. **Numbering.** A bare `R-NNNN` is `sigstore-bundle-0-3#R-NNNN`.
   `in-toto-envelope-v1`'s extraction exists only on the open PR #141 branch
   (`origin/fx1-in-toto-envelope-136` at `23c0d40`), not on main, so its ids
   and its design-notes rows (ITE-DN K-01, C-05, Q-06, ...) are cited in prose
   with that branch and commit, written *in-toto-envelope-v1 R-NNNN*, never in
   the `record#R-NNNN` form the library's tools resolve. `R-M-`, `R-I-`,
   `R-O-` ids are ARCH-0001 §5; P1, P1.1, P5, P5.1, P5.2 are ARCH-0002; V1…V9
   are SPEC-0002 §9.2. Row ids: `A` adopt, `D` adapt, `X` reject, `C`
   constrains, `K` conflicts, `S` silent; `Q-nn` open questions; `SD-D-n`
   source defects found by this lane (§8), beside the requirements lane's
   SD-R-n in `normative.md`. Four groups of requirements share identical text
   (R-0028/R-0029/R-0031, R-0053/R-0059, R-0078/R-0087, R-0093/R-0097); every
   id here was emitted by script from a selector naming its lines and a
   fragment of its text, never typed (§10). **Section signs:** a bare §n in
   running text is a section of this file; a section of the source is written
   *the source's §n* or carries a line locator (§1.3 L176); a mofn section
   always names its document.

3. **Quotation.** No word of the source is typed here. A quotation is a
   `<!-- q Lx-y -->` marker whose blockquote `bin/check-quotes --render` wrote;
   it reproduces the rendering, so a proto comment reads as prose and a code
   line as code. Elsewhere the source is cited by line and paraphrased. Field,
   message and enum names (`media_type`, `ML_DSA_65`) are identifiers, not
   quotations. Message names are the proto's, as `messages.yaml` uses them.

4. **Labels.** *(inferred)* marks a consequence the source does not state.
   Nothing here is a proposal for mofn unless it says so; §11 says what this
   file decides, which is nothing.

---

## 1. Rows by verdict

32 rows: **6 adopt, 3 adapt, 4 reject, 11 constrains, 3 conflicts, 5 silent.**
*Adopt (confirms)* means the source does what an accepted decision of ours
already does; it is evidence, not a new commitment. *Reject (native)* means the
native model declines the mechanism; nothing stops it at the boundary.

| id | verdict | in the source | where | ids | maps to | finding |
|---|---|---|---|---|---|---|
| A-01 | adopt (confirms) | the DSSE signature covers the pre-authentication encoding of `payloadType` and payload, so the type is signed with the bytes | §2.1 L237-244 | R-0095, R-0189 | R-O-05 (ARCH-0001:467); SPEC-0002 §6.4 (SPEC-0002:397-407) | the authenticated type indicator R-O-05 asks for. KSA's DS label does the job without being transmitted; here the type is transmitted and signed. It holds for `dsse_envelope` only: `message_signature` carries no type (C-07) |
| A-02 | adopt (confirms) | `message_digest` identifies; a client must not verify with it; the verifier supplies the digest, or computes it from the artifact | §3.4 L474-476; §5.1.2.1 L994-996 | R-0038, R-0110, R-0180 | R-O-05's third sentence (ARCH-0001:467); SPEC-0002 §7.2 (SPEC-0002:479-486) | a convenience copy never stands in for the value it names, the stance SPEC-0002 takes on locators: a signature checked against the bundle's digest shows that digest was signed, never that the artifact in hand has it |
| A-03 | adopt (confirms) | `canonicalized_body` is carried because a log promise over re-serialised JSON cannot be reproduced deterministically | §4.5 L847-858 | R-0160, R-0161, R-0163 | R-O-05 (ARCH-0001:467); SPEC-0002 §5 (SPEC-0002:323-328); P5.1 (ARCH-0002:440-445); option 3 withdrawn (ADR-0004:121-124) | the source's own evidence for carrying signed bytes rather than re-encoding them. It carries the body, not the promise's signed payload, which is still assembled (K-01) |
| A-04 | adopt (confirms) | signing time from outside the signer: an RFC 3161 imprint over the signature, or a log's integrated time under its promise; an integrated time without a promise is not trusted | §1.1 L50-60; §4.5 L825-837; §5.1.1 L898 | R-0003, R-0071, R-0062, R-0193, R-0168 | SPEC-0001 §11 (SPEC-0001:415-422) | SPEC-0001 §11 names these two forms of independent time for long-term verification and denies the speaker's own claim that role, as the source denies an unpromised integrated time |
| A-05 | adopt (confirms) | `keyid` and the key hint are unauthenticated hints | §2.2 L260; §3.8 L544 | R-0098, R-0121 | P5.2 (ARCH-0002:525-530); P1.1 (ARCH-0002:117-119); ADR-0005 (ADR-0005:87-92) | answers ITE-DN's Q-09 for the protobuf copy of DSSE (ITE-DN:896-900): the field is labelled unauthenticated. The principal never travels there |
| A-06 | adopt (confirms) | one signature per signed object; several signers are several objects, and policy over them lives outside | §1.3 L176-183; §5.1.2.2 L1010 | R-0089, R-0090, R-0182 | SPEC-0002 §5 (SPEC-0002:302); SPEC-0004 §6.4 (SPEC-0004:423-432); ITE-DN X-01 (ITE-DN:143) | the bundle and the KSA envelope share the shape that keeps both outside ITE-5 (§3.4) |
| D-01 | adapt | form (1): a key named by an unauthenticated hint and delivered out of band, its algorithm part of the key | §1.2 L84-85, L105-106; §3.4 L486-487; §3.8 L539-552; §5.1.1.1.2 L918-919 | R-0075, R-0012, R-0039, R-0122, R-0172 | G1, R-M-02 (ARCH-0001:141, ARCH-0001:435); SPEC-0002 §10 (SPEC-0002:710-723) | the bundle's only key-centric form, and the only one a KSA key can use without a CA; the PGI admits it for self-managed keys. The RECOMMENDED hint is not a KSA kid (K-02) |
| D-02 | adapt | transparency-log entries: an index, an integrated time, an inclusion proof against a signed checkpoint, and a promise | §1.2 L124-135; §4.2-§4.5 L725-866 | R-0079, R-0080, R-0048, R-0050, R-0195, R-0196 | R-O-04 (ARCH-0001:466); §6 SCITT receipt row (ARCH-0001:513); NG4 (ARCH-0001:156) | at import, evidence about the foreign signature, kept as received; it changes no meaning. No KSA form exists for it, and NG4 keeps any particular log optional |
| D-03 | adapt | versioning by a media type, older spellings still accepted, and reserved number ranges for later additions | §1 L41-46; §1.3 L145-151, L189-191; §3.2 L446-448 | R-0001, R-0021, R-0081, R-0091, R-0092, R-0107 | SPEC-0002 §12 (SPEC-0002:817-822); SPEC-0002 §6.2 (SPEC-0002:356-365) | KSA also reserves and never reuses numbers, but versions inside the signed bytes; the bundle's version sits outside every signature (C-04) |
| X-01 | reject (native) | X.509 key material, a leaf alone or a chain, validated to an independently trusted CA | §1.2 L86-102 | R-0005, R-0008, R-0010, R-0076, R-0194 | R-M-01 (ARCH-0001:434); R-I-05 (ARCH-0001:455); §6 X.509 row, forbidden mapping (ARCH-0001:504, ARCH-0001:515) | natively excluded. At import the certificate is a foreign identity assertion about a key, marked as X.509 provenance; path validation is the foreign verifier's, never our reducer |
| X-02 | reject (native) | keyless identity: a short-lived certificate whose extensions carry the identity a verifier consumes | §1.2 L104-112; §5.1.1 L898; §5.1.1.1.1 L904-906 | R-0011, R-0013, R-0014, R-0169 | G1, R-M-02, R-M-03 (ARCH-0001:141, ARCH-0001:435, ARCH-0001:436) | the signer is a global name a CA asserts (in both examples a URI naming a GitHub workflow, §7 check 6), not a key. *(inferred)* Imported, it is a label under the importer's `x509:` namespace, as the §6 X.509 row maps a DN (ARCH-0001:504) |
| X-03 | reject (native) | global identifiers at every extension point: media types, Rekor kinds, enums tied to Sigstore's algorithm registry, Fulcio OIDs | §1.3 L145-151; §3.2 L345-347; §3.13 L610-612; §4.1 L714-715 | R-0021, R-0034, R-0125, R-0132 | P1 (ARCH-0002:65-87); R-M-12 (ARCH-0001:445); ADR-0004 item 3 (ADR-0004:46-50) | lists one project runs, not IANA; P1's argument does not depend on who runs the list. ADR-0004's boundary list names IANA registries only (§4.3 item 2) |
| X-04 | reject (native) | `message_signature`: a signature over an artifact (or its digest) with no type, statement or domain separation | §3.4 L470-489; §5.1.2 L989-996 | R-0109, R-0176, R-0177, R-0040 | SPEC-0002 §6.3, §6.4 (SPEC-0002:372-374, SPEC-0002:397-407); R-O-05 (ARCH-0001:467) | every KSA signature is over a DS label and a TBS; a bare signature asserts nothing a statement can carry. lane-a skips such bundles (LANE-A-03:152-153). Q-11 |
| C-01 | constrains | exactly one DSSE signature, and reject any other count: the format is not ITE-5 | §1.3 L176-183; §5.1.2.2 L1010 | R-0089, R-0090, R-0182; in-toto-envelope-v1 R-0003 and R-0030 (PR #141 @ 23c0d40) | DEC-005 (ARCH-0001:643-645); R-I-03 (ARCH-0001:453); ITE-DN C-05, Q-06 (PR #141 @ 23c0d40; ITE-DN:150, ITE-DN:880-883) | a classical and a post-quantum signature, or k of n signers, are n bundles, never one (§3.4, §6) |
| C-02 | constrains | the trust material a verifier needs and the bundle does not carry | §1.2 L95-96; §3.4 L486-487; §4.4 L785-788; §1.3 L155-159; §5.1.2.1 L995-996 | R-0008, R-0115, R-0149, R-0085, R-0180, R-0122 | R-I-02 (ARCH-0001:452); SPEC-0004 §4.2-§4.3 (SPEC-0004:181-216); ADR-0003 D3, D4 (ADR-0003:49-50); ARCH-0001 §4.3 (ARCH-0001:403) | what the verifier holds instead (CA certificates, log keys, whatever checks a token) has no KSA form: an anchor trusts kids (SPEC-0004:188). §3.3, Q-02 |
| C-03 | constrains | the page fixes the DSSE payload to an in-toto Statement under in-toto's generic `payloadType`; the proto admits any type the verifier supports | §5.1.2.2 L1010; §1.3 L171-173 | R-0181, R-0088 | R-I-03 (ARCH-0001:453); ITE-DN K-01 (PR #141 @ 23c0d40; ITE-DN:153, ITE-DN:442-460) | for the PGI an export into a bundle can only be in-toto's E2. E1, our TBS under our own type, is open under the proto alone (K-03, SD-R-11) |
| C-04 | constrains | `media_type` selects the version-dependent rules, and no signature covers it | §1 L42-46; §1.3 L145-151; §1.2 L125-130 | R-0001, R-0191, R-0018, R-0020 | R-O-05's authenticated type (ARCH-0001:467); P5 (ARCH-0002:391-396) | *(inferred)* a verifier pins the versions it accepts: relabelled as v0.1, a bundle asks a v0.1-capable verifier to accept a promise without a proof, weaker evidence than it carried. SD-D-5, Q-09 |
| C-05 | constrains | no algorithm identifier is reachable from `Bundle`; the algorithm comes from the certificate or from outside | §3.4 L480-487; §3.2 L334-354 | R-0112, R-0113, R-0114 | SPEC-0002 §6.1 (SPEC-0002:350-352); suite 2 reserved (SPEC-0002:360, SPEC-0002:845); ITE-DN C-06 (ITE-DN:151) | `PublicKeyDetails` is declared and never reached (§7 check 4). Both examples sign with P-256 keys (check 6), for which KSA has no suite, so the signer has no kid |
| C-06 | constrains | keyless signers hold short-lived certificates, and the identity is in the certificate | §5.1.1 L898; §1.2 L104-112 | R-0168, R-0014 | R-M-06 (ARCH-0001:439); SPEC-0004 §6.4 (SPEC-0004:431) | *(inferred)* if each signing gets a fresh key, one identity signing k times shows k kids, and a threshold counted by kid counts it k times. The source says short-lived, not one key per signing (Q-04) |
| C-07 | constrains | `message_signature` has no domain separation, and nothing keeps one key from signing both content types | §3.4 L470; §5.1.2.1 L994; §2.1 L237-244 | R-0109, R-0177, R-0095 | SPEC-0002 §13.2 (SPEC-0002:897-901); SPEC-0001 §5.3 (SPEC-0001:221-227) | *(inferred)* under the proto's reading, a KSA key's message signature over an artifact whose bytes are a DS label and a TBS is a KSA statement signature: SPEC-0002 §13.2's proviso, that the other protocol domain-separates, fails. SD-D-6, Q-08 |
| C-08 | constrains | the bundle is JSON nobody signs, and one bundle has more than one spelling | §5.1.2.2 L1013-1022; §5.1.3 L1035-1137; §4.5 L856-858; §2.1 L227 | R-0185, R-0186, R-0187, R-0188, R-0163 | SPEC-0001 §5.3, §6.2 (SPEC-0001:229-232, SPEC-0001:257); T-052 (BACKLOG:189); LANE-A-03:96-101 | a byte-faithful import keeps the text as received; the DSSE envelope inside it has no bytes of its own (§5) |
| C-09 | constrains | the bundle carries the key's validity, not the statement's | §1.3 L155-159; §5.1.1 L898 | R-0085, R-0193 | SPEC-0002 §7.3 (SPEC-0002:494-501); SPEC-0004 §8 (SPEC-0004:479-482) | *(inferred)* the certificate's window bounds when the key could sign, ten minutes in both examples (check 6); nothing says how long what was signed holds. An import's validity comes from the payload or from the importer |
| C-10 | constrains | the container real provenance arrives in has no row in our interchange matrix | the whole source | — | R-I-01 (ARCH-0001:451); §6 (ARCH-0001:496-515); T-053 (BACKLOG:190) | §6 has in-toto, DSSE and SCITT-receipt rows (ARCH-0001:506, ARCH-0001:507, ARCH-0001:513) and none for the bundle around them; §4.1 here is the table such a row would point to |
| C-11 | constrains | mofn's own release provenance is a Sigstore keyless bundle (PLAN-0004 D2) | §1.2 L104-112; §5.1.1 L898 | R-0011, R-0014, R-0168 | PLAN-0004:383-385, PLAN-0004:395-397; RELEASE:175-178, RELEASE:210-212; DL-0043r:61-63 | the release's integrity rests on Fulcio and Rekor, foreign roots, as checked by GitHub's verifier; no KSA statement speaks for it until #32 (PLAN-0004:462-463). §5 |
| K-01 | conflicts | verifying the log's promise means assembling its signed payload, a canonical JSON, from the body and three fields; without the body, reconstructing the entry | §4.4 L781-784; §4.5 L852-855, L863-864 | R-0147, R-0162, R-0164, R-0157, R-0064 | R-O-05's second sentence, R-O-03 (ARCH-0001:467, ARCH-0001:465); P5.1 (ARCH-0002:440-445) | an importer that must check the promise canonicalises inside verification, by an algorithm the source cites only as Rekor code at a commit (L784). Q-05 |
| K-02 | conflicts | the RECOMMENDED hint derivation is RFC 6962's, SHA-256 over the key's DER SubjectPublicKeyInfo, and the hint and the DSSE `keyid` must be exactly equal | §3.8 L550-552; §1.3 L160-163 | R-0123, R-0086 | ADR-0005 (ADR-0005:87-92); P1.1 (ARCH-0002:113); SPEC-0002 §4.5 (SPEC-0002:288) | such a hint never equals a KSA kid (§7 check 3), so an import rule that rejects a foreign kid disagreeing with the computed one rejects every bundle that follows the recommendation; a keyless `keyid` is empty (L1132). Q-03 |
| K-03 | conflicts | under the page, what a bundle signs is a JSON in-toto Statement | §5.1.2.2 L1010 | R-0181 | R-O-05's first sentence (ARCH-0001:467); ITE-DN K-01 (PR #141 @ 23c0d40; ITE-DN:153) | in-toto's K-01, made a condition of the PGI by this container: what a Sigstore verifier checks is a second object with its own bytes and digest |
| S-01 | silent | unknown fields in a bundle, and what a parser does with them | §1.3 L189-191 | R-0091, R-0092 | P5 (ARCH-0002:394-396); P5.2 (ARCH-0002:503-510); SPEC-0002 §13.5 (SPEC-0002:920-922) | `Bundle` reserves 46 field numbers for future artifact types, and an older verifier meeting one is told nothing. *(inferred)* P5.2's import rule reads onto the bundle exterior too |
| S-02 | silent | where a timestamp authority's certificate comes from, and how the token's own signature is checked | §1.1 L56-60; §3.6 L509-514 | R-0003, R-0117, R-0042 | C-02 | the imprint rule is the only timestamp rule; no word of the source names a timestamp authority (§7 check 10). SD-D-7 |
| S-03 | silent | a context string, or prehashing, for ML-DSA in a bundle | §3.2 L424-444 | R-0103, R-0104 | SPEC-0002 §6.5 (SPEC-0002:409-416) | KSA suite 8 fixes its context; the bundle fixes nothing (§6) |
| S-04 | silent | what binds a log entry's key, certificate and artifact hash to the bundle's own | §4.5 L860-862 | R-0067 | SPEC-0002 V6 (SPEC-0002:698) | only the signature must match; both examples carry the same certificate, and the hashedrekord body the same digest (§7 check 2). SD-D-4 |
| S-05 | silent | revocation, a statement's validity, and several log entries or timestamps that disagree | — | — | R-O-02 (ARCH-0001:464); SPEC-0002 §8.7 (SPEC-0002:619-627) | nothing at this layer, and no word for revocation (§7 check 10); the repeated fields carry no rule for more than one |

---

## 2. Row details

### 2.1 Adopt

**A-01 — the type is inside the signature.**

<!-- q L237-240 -->
> Signature over: PAE(type, payload) Where PAE is defined as: PAE(type, payload) = "DSSEv1" + SP + LEN(type) + SP + type + SP + LEN(payload) + SP + payload

In the DSSE example the type is 28 octets and the payload 1344, so the signed
input is 1388 octets; it verifies under the leaf's P-256 key and fails with one
bit flipped (§7 check 2). R-O-05 asks the signed payload to travel with an
authenticated type indicator (ARCH-0001:467), and this is one. KSA gets the
same property from a DS label that is fixed per object class and never
transmitted (SPEC-0002:397-407); here the type travels and is signed. The
property belongs to the DSSE content only: a message signature carries no
type (X-04, C-07).

**A-02 — a digest in the bundle is never the artifact's.**

<!-- q L474-476 -->
> Message digest can be used to identify the artifact. Clients MUST NOT attempt to use this digest to verify the associated signature; it is intended solely for identification.

The page adds that the digest is informational and that the verifier supplies
it, or computes it from the artifact:

<!-- q L994-996 "It may contain" .. "verification time." -->
> It may contain a `message_digest` for informational purposes, but it must be provided or computed from a provided artifact at verification time.

The reason is not that the digest is unsigned: the example's signature
verifies with `message_digest` as its hash (§7 check 2). It is that such a
check shows only that the signer signed that digest, never that the artifact
in hand has it; only the artifact's own hash ties the two. R-O-05's third sentence has a
human-facing form regenerated from verified bytes (ARCH-0001:467), and SPEC-0002
forbids treating content fetched from a locator as the subject unless it
matches the target (SPEC-0002:479-486): the same stance about a different
convenience copy. *(inferred)* An importer shows the digest it computed, never
this one. In the message-signature example the digest equals the hashedrekord
body's artifact hash, which the log's promise covers (§7 check 2); the source
asks for no such comparison (S-04).

**A-03 — the source's own case for carrying signed bytes.**

<!-- q L856-858 -->
> This field is intended to be used in cases where the SET cannot be produced determinisitically (e.g. inconsistent JSON field ordering, differing whitespace, etc).

The field holds the log's body as the log returned it (R-0161), so a
verifier hashes received bytes rather than re-serialising an entry. That is
R-O-05's reason for transmitting the signed bytes, which SPEC-0002 §5 spells out
(SPEC-0002:323-328), and P5.1's reason for rejecting rather than repairing
(ARCH-0002:440-445). It is also evidence against signing re-serialised JSON,
the ground option 3 was withdrawn on (ADR-0004:121-124), and this source names
field order and whitespace as the failure. It stops short: the promise's own
signed payload is still assembled by the verifier (K-01).

**A-04 — time from outside the signer.** The imprint rule:

<!-- q L59-60 -->
> Clients MUST verify the hashed message in the message imprint against the signature in the bundle.

An integrated time is trusted only under the promise (R-0062), and with a
short-lived certificate the page requires a promise or a token in the bundle
(R-0168). SPEC-0001 §11 asks a statement that must verify for decades for a
post-quantum suite or an independent timestamp, a transparency-log receipt or a
timestamp token, and says the speaker's own `issued` is not such evidence
(SPEC-0001:415-422). The bundle carries exactly those two forms, about the
foreign signature. *(inferred)* A KSA statement could be timestamped the same
way, by a token whose imprint hashes its `sig`; KSA has no field for one.

**A-05 — hints are hints.**

<!-- q L260 -->
> *Unauthenticated* hint identifying which public key was used.

The key hint is likewise unauthenticated (R-0121). The in-toto Envelope layer
never says whether a `keyid` is authenticated (ITE-DN:896-900, its Q-09); this
source's copy of DSSE says it is not. P5.2 already keeps the principal out of
`signatures[].keyid` (ARCH-0002:525-530), and ADR-0005 lets an export put the
KSA kid there as a hint (ADR-0005:87-92). Nothing changes, and P5.2's reason now
has a line in the container mofn's real imports arrive in.

**A-06 — one signature, one signer.** The bundle's rule (C-01) and KSA's
envelope agree: a KSA signed statement carries one `sig` over a TBS naming one
speaker (SPEC-0002:302), and several signers are several statements, counted by
trust evaluation (SPEC-0004:423-432). The source's first reason, simpler checking and
simpler policy (L179), matches how SPEC-0002 keeps every check
that needs other statements out of single-statement verification and in trust
evaluation (SPEC-0002:703-706). ITE-DN X-01
(ITE-DN:143) found the KSA envelope never an ITE-5 envelope, for the reason the
bundle is not one (§3.4).

### 2.2 Adapt

**D-01 — form (1) is the bundle's key-centric mode.** The three forms are a
hint, a chain and a single certificate (L80-102):

<!-- q L84-85 -->
> 1. An unspecified public key identifier, for retrieving a key from an out-of-band mechanism (such as a keyring);

With the PGI, form (1) is forbidden for keyless signing in every version and
allowed for self-managed keys (R-0011, R-0012). The key and its algorithm travel
out of band (R-0039), the hint's format is agreed out of band (R-0122), and the
page says the key is not in the bundle (R-0172). That is G1 and R-M-02's
model, a principal that is a key (ARCH-0001:141, ARCH-0001:435), and SPEC-0002
§10's out-of-band import into a key store (SPEC-0002:710-723). *(inferred)* It
is the only form a KSA key can use without a CA, so an export to a Sigstore
verifier from a KSA key is a form (1) bundle, and that verifier needs our key
configured; the stricter verifiers lane-a names check only Sigstore-signed
provenance (LANE-A-README:60), so it would be another one. Two adaptations: a suite-1 key is `PKIX_ED25519` in the enum (L396),
which no field of a bundle carries (C-05); and the hint the source recommends is
not our kid (K-02).

**D-02 — log entries are evidence.** An entry holds the log's index and
integrated time, an inclusion proof whose checkpoint the log signs
(R-0048, R-0050), and the promise. ARCH-0001 §6 already has the shape: a SCITT
receipt is evidence attached to an attestation and changes nothing it means
(ARCH-0001:513), registration is optional (R-O-04, ARCH-0001:466), and NG4
requires no particular log (ARCH-0001:156). *(inferred)* At import an entry is
evidence about the foreign signature, kept as received, and says nothing about
the importer's own statement. The proof's two checks are inferred
(R-0195, R-0196): the source states the proof's purpose and no duty to check it
(SD-R-20).

**D-03 — version numbers outside the signature.**

<!-- q L42-46 -->
> The primary message ('Bundle') MUST be versioned, by populating the 'media_type' field. Semver-ish (only major/minor versions) scheme MUST be used. The current version as specified by this file is: application/vnd.dev.sigstore.bundle.v0.3+json The semantic version is thus '0.3'.

`Bundle` reserves 46 field numbers for later artifact types (L189-191) and
`PublicKeyDetails` 27 for algorithms (L446-448) (§7 check 7). SPEC-0002 also
reserves numbers and never reuses one (SPEC-0002:817-822, SPEC-0002:356-365).
The difference is where the version lives: KSA's suite and kind are fields of
the TBS and signed (SPEC-0002:350-352, SPEC-0002:428-444), and the DS label
carries a version (SPEC-0002:397-407); the bundle's version is in a field no
signature covers (C-04).

### 2.3 Reject (native)

**X-01 — X.509 is interchange.** Form (2) puts the leaf first, in issuing order,
never a root (R-0005, R-0006, R-0076); the verifier chains to a CA it trusts
on its own:

<!-- q L95-96 "Verifiers MUST" .. "independently trust." -->
> Verifiers MUST validate the chain carefully to ensure that it chains up to a CA certificate that they independently trust.

With form (3) it builds the path from its own material (R-0194). R-M-01 keeps
X.509 out of the native encoding (ARCH-0001:434), R-I-05 imports it only as a
foreign identity assertion about a key (ARCH-0001:455), and the §6 matrix
forbids X.509 path validation as the native reducer (ARCH-0001:515). Nothing in
this source asks for more.

**X-02 — a keyless signer is a name.** With the PGI the key material is a
certificate in every version (L104-112), and the page says what the leaf
carries:

<!-- q L904-905 "A single X.509" .. "verification time." -->
> A single X.509 leaf certificate conveying the signing key and containing [extensions](https://github.com/sigstore/fulcio/blob/main/docs/oid-info.md) for identities consumed at verification time.

In both examples the leaf has an empty subject and a critical subject
alternative name, a URI naming a GitHub Actions workflow at a ref, and is valid
for ten minutes (§7 check 6). The signer a relying party cares about is that
name, asserted by the CA; the key is incidental. G1 makes principals keys and
R-M-03 makes names relative to an issuing principal (ARCH-0001:141,
ARCH-0001:436); a CA-asserted global name is neither. *(inferred)* An import
maps it as the §6 X.509 row maps a DN, as labels under the importer's `x509:`
namespace with provenance (ARCH-0001:504), never as the CA's name.

**X-03 — central lists, not IANA's.** The bundle depends on four lists that one
project runs: its media-type names (L145-151), the algorithm registry the enum
must track (R-0034, on `main`, SD-R-21), Rekor's entry kinds (R-0132) and
Fulcio's OID arc (R-0125). P1's argument is that any global list handed out by a
central party brings back the namespace a key-centric model rejects
(ARCH-0002:74-80); it does not turn on IANA. R-M-12 relocates exactly this to P1
(ARCH-0001:445). ADR-0004 item 3 lists the IANA registries the native model
excludes (ADR-0004:46-50). *(inferred)* These four sit at the same boundary and
the list does not name them (§4.3 item 2).

**X-04 — a bare signature.**

<!-- q L470 -->
> MessageSignature stores the computed signature over a message.

The page says the signature is over the artifact's hash (R-0176, R-0177); SD-R-15 records the
disagreement. Either way there is no type, no statement and no prefix: the
signature shows only that a key signed some bytes. Every KSA signature is over a
DS label and a TBS (SPEC-0002:372-374, SPEC-0002:397-407), so the native model
has nothing a bare signature maps onto, and R-O-05's authenticated type is
absent. lane-a skips such bundles (LANE-A-03:152-153). *(inferred)* At import a
message signature is evidence that a key signed an artifact or its digest;
making it an `ArtifactStatement` needs an attribute nobody asserted (Q-11).

### 2.4 Constrains

**C-01 — exactly one.**

<!-- q L176-181 -->
> DSSE envelopes in a bundle MUST have exactly one signature. This is a limitation from the DSSE spec, as it can contain multiple signatures. There are two primary reasons: 1. It simplifies the verification logic and policy 2. The bundle (currently) can only contain a single instance of the required verification materials

<!-- q L182-183 -->
> During verification a client MUST reject an envelope if the number of signatures is not equal to one.

The page repeats it (R-0182). ITE-5 requires a format to support several
signatures in one envelope (in-toto-envelope-v1 R-0003, PR #141 @ 23c0d40; ITE:L12) and the in-toto Envelope
layer names this bundle as failing it (in-toto-envelope-v1 R-0030, PR #141 @ 23c0d40; ITE:L21-22); ITE-DN C-05
and Q-06 (PR #141 @ 23c0d40; ITE-DN:150, ITE-DN:409-420, ITE-DN:880-883) left open whether the DSSE
envelope a bundle holds is a conforming in-toto envelope. §3.4 answers from
both sources. For DEC-005 (ARCH-0001:643-645): the DSSE option, in the
container mofn's own releases use, carries one signature, so k of n signers, or
a classical signature beside a post-quantum one, is n bundles.

**C-02 — the bundle is not self-contained.** Four kinds of trust material come
from outside: the CA certificates a chain must reach (R-0008), the log's key with
its hash and scheme,

<!-- q L785-788 -->
> The format of the signature depends on the transparency log's public key. If the signature algorithm requires a hash function and/or a signature scheme (e.g. RSA) those has to be retrieved out-of-band from the log's operators, together with the public key.

the signer's key for form (1) (R-0115, R-0122), and the timestamp authority's
certificate, which no line of the source mentions (S-02). Two more inputs are
not trust material and are still outside: the artifact, for a message
signature (R-0180), and the verification procedure, a linked document (R-0085,
SD-R-21). R-I-02 says an import must not require the foreign object to become
a native trust anchor (ARCH-0001:452). A KSA anchor trusts a kid, a name or a
threshold set of kids about a scope, local to one context (SPEC-0004:181-203;
ADR-0003:49-50). What a verifier holds instead, CA certificates, log keys and
whatever checks a timestamp token, has no KSA form at all; ARCH-0001 §4.3
counts configured trust for artifact services among a verifier's inputs and
holds it as per-context anchors (ARCH-0001:403), which a Sigstore root cannot
be. *(inferred)* An importer either keeps the foreign root outside the anchor
model, or relies on a foreign verifier's verdict and says so under its own key.
§3.3, Q-02.

**C-03 — the PGI's payload is in-toto's.**

<!-- q L1010 "The DSSE envelope in a Sigstore Bundle must conform" .. "statement.md)." -->
> The DSSE envelope in a Sigstore Bundle must conform to the [in-toto Envelope layer specification](https://github.com/in-toto/attestation/blob/main/spec/v1/envelope.md) where `payloadType` is `"application/vnd.in-toto+json"` and the payload is an [in-toto statement](https://github.com/in-toto/attestation/blob/main/spec/v1/statement.md).

The proto lets a verifier accept any payload type it supports and expects
(R-0088), so an envelope whose payload is a KSA TBS under our own type, ITE-DN's E1
(ITE-DN:449-451), is a valid bundle under the proto and not under the page
(SD-R-11). *(inferred)* No deployed verifier expects our type, so an export into
a bundle is in practice E2, an in-toto Statement in DSSE, and K-03 follows.

**C-04 — the version is unauthenticated, and it selects the rules.**
`media_type` decides which key-material form applies (R-0013, R-0014), whether a
promise without a proof is acceptable (R-0018) and whether the bundle is acceptable
at all (R-0020); the requirements lane infers that a verifier reads it first (R-0191). No
signature in the bundle covers it (§3.2). R-O-05 asks for an authenticated type
indicator on what is signed (ARCH-0001:467), and P5 says validity is checked,
never assumed (ARCH-0002:391-396). *(inferred)* A verifier therefore fixes the
versions it accepts by policy rather than reading them from the bundle. A v0.3
bundle relabelled v0.1, its proof removed and its certificate moved into a
one-element chain, which form (2) admits (R-0005), asks a v0.1-capable verifier to
accept the log's promise alone: weaker evidence than the bundle carried, not a
forgery. The source's only guard is a SHOULD NOT for ecosystems that
never produced v0.1 (R-0020). SD-D-5, Q-09.

**C-05 — no algorithm in the bundle.** Of the 26 types the four protos declare,
18 are reachable from `Bundle`, and the one enum among them is `HashAlgorithm`,
for the informational digest (§7 check 4). `PublicKeyDetails`, the enum that
names signature algorithms, is declared and never reached. The algorithm comes
from the verification material:

<!-- q L481-485 -->
> The signature algorithm (and so the format of the signature bytes) are determined by the contents of the 'verification_material', either a key-pair or a certificate. If using a certificate, the certificate contains the required information on the signature algorithm.

SD-R-16 records that a certificate fixes the key type and not, in general, the
hash. KSA signs its suite (SPEC-0002:350-352). Both example leaves hold P-256
keys (§7 check 6); KSA's P-256 suite is reserved and unspecified
(SPEC-0002:360, SPEC-0002:845), so the signer of a real bundle has no kid,
ITE-DN C-06's finding for the same keys (ITE-DN:151).

**C-06 — keyless signers and thresholds.** The page calls Fulcio certificates
short-lived (L898), and both examples are valid for ten minutes (§7 check 6).
*(inferred)* If each signing certifies a fresh key, one identity that signs k
times presents k kids. SPEC-0004 counts threshold members as distinct by kid
(SPEC-0004:431), and R-M-06 makes threshold principals native (ARCH-0001:439):
counted by kid, k bundles from one workflow meet a k-of-n threshold. Whether
keys are fresh per signing is Fulcio's practice, not this source's, which says
short-lived and keyless and nothing more. Q-04.

**C-07 — no domain separation for message signatures.** A DSSE signature is
over a PAE whose first six octets are `DSSEv1` (L240, L243). A message
signature is over a message (R-0109), with no prefix. *(inferred)* Two
consequences. A key that makes both kinds turns a message signature over an
artifact whose bytes happen to be a PAE into a valid DSSE signature, and the
source says nothing against one key making both. And SPEC-0002 §13.2 says a KSA
signature cannot be replayed into or out of another protocol provided that
protocol also domain-separates (SPEC-0002:897-901). Under the proto's reading,
a signature over the artifact, a KSA key making message signatures signs
whatever bytes it is given, and an artifact equal to a DS label followed by a
TBS yields a valid KSA statement signature. Under the page's reading, the
digest itself as the signed message, it cannot: a 32-octet message is shorter
than a 16-octet DS label and a TBS whose speaker field alone is a 32-octet kid
(SPEC-0002:372-373, SPEC-0002:288, SPEC-0002:435).
SPEC-0001 §5.3 recommends a separate key per protocol and requires any use
outside KSA to be recorded on the key (SPEC-0001:221-227); here that
recommendation is the whole defence. SD-D-6, Q-08.

**C-08 — the container is unsigned text with more than one spelling.** §5 takes
this up for T-052. The source's own evidence: its two complete examples print
each of their 12 objects in proto field-number order, while the §5.1.2.2
placeholder prints a signature's `keyid` before its `sig` (§7 check 1); the
examples print three values a proto3 JSON serialiser omits by default
(R-0185); int64 fields are strings and bytes are base64 (R-0187, R-0188); the keys are
the lowerCamelCase forms (R-0186), and that a parser also takes the proto's own
names is the proto3 JSON mapping's rule, outside this source; and the source
names field order and whitespace as the reason the log's body is carried
(R-0163). SPEC-0001 keeps an imported object's original bytes (SPEC-0001:229-232)
and every statement as its exact envelope bytes (SPEC-0001:257). lane-a writes
the bundle and the envelope back out with `json.dumps` (LANE-A-03:96-101), so
those files are not as received.

**C-09 — whose validity.** A verifier must establish that the certificate was
inside its validity window when the signature was made (R-0085), which needs a trusted signing time
(R-0193). That window, ten minutes in both examples, bounds when the key could
sign. *(inferred)* It is not the validity of what was signed: nothing in the
bundle says how long a provenance claim holds, and the source has no revocation
(S-05). A KSA statement carries its own window (SPEC-0002:494-501) and trust
evaluation uses one evaluation time (SPEC-0004:479-482); an imported
statement's window comes from the payload or from the importer, never from the
certificate.

**C-10 — no matrix row.** R-I-01 asks a mapping table for each supported foreign
format (ARCH-0001:451). The §6 matrix has rows for the in-toto Statement, the
DSSE envelope and the SCITT receipt (ARCH-0001:506, ARCH-0001:507,
ARCH-0001:513) and none for the bundle that carries the first two in the real
imports T-052 and the I4 demo plan (BACKLOG:189, PLAN-0001:487). *(inferred)*
T-053's owner
(BACKLOG:190) has a candidate row, and §4.1 is its content. ADR-0002 already
owes R-I-01 a DSSE envelope-exterior row (ADR-0002:180); a bundle is a further
exterior around that envelope. This file adds no row.

**C-11 — mofn's own releases.** PLAN-0004 D2 settled release signing as
`SHA256SUMS` plus build provenance, with no project key (PLAN-0004:395-397). The
provenance is made by `actions/attest-build-provenance`, Sigstore, keyless
(PLAN-0004:383-385; RELEASE:210-212, with `id-token: write` at
RELEASE:175-178), in the release job DL-0043 describes (DL-0043p:46-52). DL-0043 chose it because it is free on a public repository and
protects against a compromised release, which checksums alone do not
(DL-0043r:61-63). What this source fixes for such a bundle, if it is v0.3 and
made with the PGI: form (3), the leaf alone (R-0014), and, the certificate being
short-lived, a promise or a token in the bundle (R-0168). What it cannot fix:
which version, which time source and which predicate the action emits; those
are the action's (record.yaml:106-109). *(inferred)* A wallet release's
integrity therefore rests on Fulcio and Rekor, foreign roots, as GitHub's
verifier checks them (RELEASE:202-203; DL-0043r:138-144), and no KSA statement
speaks for a release until #32 (PLAN-0004:462-463).

### 2.5 Conflicts

**K-01 — the promise is checked by canonicalising.** What the log signs:

<!-- q L781-783 "It's calculated" .. "integration timestamp." -->
> It's calculated as a signature over a canonical JSON serialization of the persisted entry, the log ID, log index and the integration timestamp.

and who builds it at verification:

<!-- q L852-855 "The verifier is responsible" .. "generated over." -->
> The verifier is responsible for combining the `canonicalized_body`, `log_index`, `log_id`, and `integrated_time` into the payload that the SET's signature is generated over.

Without the body, the client must rebuild that payload itself from what else
it holds (R-0164). R-O-05 forbids a verifier to canonicalise input as part of
verification (ARCH-0001:467), and R-O-03 asks every canonicalisation algorithm
to be cited (ARCH-0001:465): this source names a canonical JSON serialisation
and points at Rekor's code at a commit (L784), no algorithm. The promise must be
verified for v0.1 (R-0064) and whenever no other suitable time source is
present (R-0157). *(inferred)* An importer that relies on the promise, rather
than on a timestamp token or the inclusion proof, runs a canonicaliser inside
verification. The inclusion proof does not have the problem when the body is
carried: its leaf is hashed from received bytes (the examples lane verified
both proofs taking the leaf over the body, examples/README.md:71). Not a DEC-002
discriminator: every option imports the same promise. Q-05.

**K-02 — the recommended hint is not our kid.**

<!-- q L550-552 -->
> Implementors are RECOMMENDED to derive the value from the public key as described in RFC 6962. See: <https://www.rfc-editor.org/rfc/rfc6962#section-3.2>

RFC 6962 §3.2 defines its key identifier as SHA-256 over the DER encoding of
the key as a SubjectPublicKeyInfo (RFC6962:644-645). A KSA kid is SHA-256 over
the suite's raw key encoding (SPEC-0002:288), 32 octets for suite 1
(SPEC-0002:370-371), against 44 octets of SubjectPublicKeyInfo for the same key,
and the two digests differ (§7 check 3). The hint must also equal the DSSE
`keyid` exactly (R-0086). ADR-0005 rejects an import whose foreign kid
disagrees with the kid computed from the key (ADR-0005:87-92), as P1.1 does for
COSE (ARCH-0002:113). *(inferred)* Read literally, that rejects every form (1)
bundle that follows this source's recommendation, and is undefined for the
keyless bundles an importer mostly meets: there the `keyid` is empty (L1132)
and the P-256 key has no KSA kid (C-05). Q-03.

**K-03 — what a PGI bundle signs is a JSON Statement.** ITE-DN K-01
(PR #141 @ 23c0d40; ITE-DN:442-460) found that an in-toto DSSE export signs a JSON Statement, a
second object with its own bytes and digest, so R-O-05's first sentence, the
canonical encoding signed verbatim, cannot hold for it (ARCH-0001:467). The page
makes that the only content a PGI bundle may carry (C-03). *(inferred)* So
R-O-05's first sentence holds for no export a Sigstore verifier accepts from
the PGI; it holds only for E1, under the proto alone, read by verifiers we
configure.

### 2.6 Silent

**S-01 — unknown fields.** `Bundle` reserves 5 to 50 for future artifact types
(R-0091, R-0092). Nothing says what a verifier does with a field it does not know,
in protobuf or in JSON. P5 makes an unknown field in a signed payload an error
(ARCH-0002:394-396), SPEC-0002 §13.5 forbids skipping what a verifier does not
understand (SPEC-0002:920-922), and P5.2 has our importer reject unrecognised
fields outside a DSSE payload (ARCH-0002:503-510). *(inferred)* A bundle is
such an exterior, so an importer rejects a bundle carrying a field it does not
know, a future content type in 5 to 50 included: it fails closed where the
source is silent.

**S-02 — timestamp-authority trust.** The source's one timestamp rule is the
imprint check (R-0003); the token is DER (R-0117). No word of the source names a
timestamp authority or says where its certificate comes from (§7 check 10), and
the DSSE example's token carries no certificate (examples/README.md:70). SD-D-7.

**S-03 — ML-DSA's context.** The enum lists three ML-DSA values, pure variants
(R-0103), experimental (R-0104). It gives no context string, and no rule for what a
message signature under a pure scheme is over (SD-R-15). §6.

**S-04 — what binds a log entry to the bundle.**

<!-- q L860-862 -->
> If set, clients MUST verify that the signature referenced in the `canonicalized_body` matches the signature provided in the `Bundle.content`.

Only the signature is named. Nothing requires the body's public key or
certificate to equal the bundle's key material, or a hashedrekord body's
artifact hash to equal `message_digest`; in both examples all three agree (§7
check 2). SPEC-0002's V6 checks that the decoded `suite` and `says` equal the
envelope's hints (SPEC-0002:698), the same kind of check between two copies.
SD-D-4.

**S-05 — lifecycle.** No revocation, no validity for what was signed (C-09),
and no rule for several entries or tokens beyond the page's at least one
(R-0168): whether all must verify, or any, is unsaid. R-O-02 prefers short validity to
revocation (ARCH-0001:464), and SPEC-0002 has `revoke` (SPEC-0002:619-627);
neither has anything to map from here.

---

## 3. The four questions of library#151

### 3.1 Which versions exist, and what changed

The source names three versions, 0.1, 0.2 and 0.3, by the media types a client
must accept:

<!-- q L147-151 -->
> Clients must to be able to accept media type using the previously defined formats: * application/vnd.dev.sigstore.bundle+json;version=0.1 * application/vnd.dev.sigstore.bundle+json;version=0.2 * application/vnd.dev.sigstore.bundle+json;version=0.3

and gives the current one in a fourth spelling (L45, L145-146;
R-0068, R-0021). As far as this source shows, three things change between
versions, each stated by a rule that names a version:

| | v0.1 | v0.2 | v0.3 |
|---|---|---|---|
| media type in the source | `…bundle+json;version=0.1` (R-0082) | `…bundle+json;version=0.2` (R-0083) | `…bundle.v0.3+json`, required in JSON (R-0021, R-0068); also `…bundle+json;version=0.3`, listed among the previously defined formats (R-0084); SD-R-3 |
| key material, PGI keyless | form (2), a chain (R-0013) | form (2) (R-0013) | form (3), the leaf alone (R-0014) |
| key material, PGI self-managed | form (1) MAY (R-0012); never for keyless (R-0011) | same | same |
| log evidence | a promise, required and verified (R-0064); an entry may carry a promise and no proof (R-0018) | the proof; the promise optional given another time source, MUST be verified without one and SHOULD otherwise (R-0156, R-0157, R-0158) | as v0.2 (the rule reads >= v0.2) |
| verifier stance | support MAY be offered (R-0018), and then the promise MUST be validated (R-0019); SHOULD NOT be allowed where never produced (R-0020) | — | — |

The promise and proof rules, in the source's words:

<!-- q L125-128 "Client verification" .. "validate the promise." -->
> Client verification libraries MAY provide an option to support v0.1 bundles for backwards compatibility, which may contain an inclusion promise and not an inclusion proof. In this case, the client MUST validate the promise.

<!-- q L831-837 -->
> The inclusion promise/signed entry timestamp from the log. Required for v0.1 bundles, and MUST be verified. Optional for >= v0.2 bundles if another suitable source of time is present (such as another source of signed time, or the current system time for long-lived certificates). MUST be verified if no other suitable source of time is present, and SHOULD be verified otherwise.

**What the source does not show.** None of the five pinned inputs is a
changelog, and nothing dates a version. It does not say whether `version=0.3`
and `.v0.3` name one version (SD-R-3), what the page's Version 0.3.2 numbers
when the scheme admits only major and minor (SD-R-6), whether 0.2 changed
anything besides the promise and the proof, or when any field arrived.
*(inferred)* One hint, not evidence: in `VerificationMaterial` the key-material
members are numbered 1, 2 and 5 while `tlog_entries` and
`timestamp_verification_data` are 3 and 4 (§7 check 5), consistent with
`certificate`, form (3), arriving after both, as a v0.3 form would. The
repository's CHANGELOG.md is outside the pins and was not read.
`protos/sigstore_bundle_v2.proto`, on `main` since 2026-10-26 and marked
unstable on 2026-11-18 (record.yaml:24), is not this record and nothing here
reads it.

*(inferred)* For mofn, v0.1 matters mainly as a downgrade path (C-04): mofn has
never produced or consumed a v0.1 bundle, so R-0020's ecosystem test points at
refusing it. And the version moved from a media-type parameter to the subtype
between 0.2 and 0.3, so a comparison has to know both forms (R-0191).

### 3.2 What exactly is signed

The table lists six kinds of signature by four kinds of signer; a bundle
carries one content signature and any number of the others. §7 check 2
verified the content signature of both examples.

| signature | made by | over | where | checked with |
|---|---|---|---|---|
| DSSE content | the signer | the PAE of `payloadType` and the decoded payload (R-0095, R-0189) | `dsse_envelope.signatures[0].sig` | the leaf's key, or the form (1) key |
| message content | the signer | a message (R-0109); the page says an artifact hash (R-0176, R-0177), SD-R-15 | `message_signature.signature` (R-0040) | the same |
| certificate | the issuing CA | the certificate (X.509, outside the source) | `certificate`, or each chain member | a path to a CA trusted on its own (R-0008, R-0194) |
| promise (SET) | the log | canonical JSON of the entry, the log's id, the index and the integrated time (R-0147) | `inclusion_promise.signed_entry_timestamp` | the log's key, out of band (R-0149) |
| checkpoint | the log, first; others MAY follow (R-0051) | the tree head: origin, size and root hash (R-0048, R-0050) | `inclusion_proof.checkpoint.envelope` | the log's key |
| timestamp token | a timestamp authority | its TSTInfo, whose imprint hashes the content signature's bytes (R-0003, R-0190) | `rfc3161_timestamps[].signed_timestamp`, DER (R-0117) | unsaid (S-02) |

**DSSE.**

<!-- q L237-244 -->
> Signature over: PAE(type, payload) Where PAE is defined as: PAE(type, payload) = "DSSEv1" + SP + LEN(type) + SP + type + SP + LEN(payload) + SP + payload + = concatenation SP = ASCII space [0x20] "DSSEv1" = ASCII [0x44, 0x53, 0x53, 0x45, 0x76, 0x31] LEN(s) = ASCII decimal encoding of the byte length of s, with no leading zeros

The PAE covers the type and the payload octets, not their base64 text
(R-0093, R-0189). In the DSSE example the signed input is 1388 octets, 44 of framing
and type ahead of the 1344-octet Statement, and the Statement decodes byte for
byte to the attestation the page prints after the bundle (§7 check 2).

**Message signature.** The proto says a message; the page says an artifact
hash. In the example the signature verifies as ECDSA over P-256 with the
32-octet `message_digest` taken as the precomputed hash, which is what a
signature over the artifact with SHA-256 is, and fails when the digest is
hashed again as the message (§7 check 2). So the example supports the proto's
reading, and the page's only in the sense that ECDSA signs a hash. For a pure
scheme the readings give different signatures, and the enum has pure schemes
of two families, Ed25519 and ML-DSA (§6). The digest field itself identifies
and never verifies (A-02).

**What nothing in the bundle signs** (the table, R-0189, and §7 check 2):
`media_type`; the bundle as a whole, in any serialisation; `keyid` and the key
hint (A-05); `message_digest`, which no check the source permits takes as
input (A-02); `kind_version`, except as the body repeats it;
and which entries and tokens the bundle carries, how many, and in what order.
The certificate is signed by the CA, and the signer's signature does not cover
it. The parts are bound to the content in exactly the two ways the source
requires: a token's imprint hashes the content signature (R-0003), and a
carried body names the same signature (R-0067). Nothing requires the body's key
or digest to match (S-04).

### 3.3 What a verifier needs

**From the bundle**, by version and by instance:

- key material, exactly one form of three (R-0183): form (1), a hint (R-0075); form (2),
  a chain, leaf first, issuing order SHOULD, no root, no intermediate already
  in the trusted root (R-0005, R-0006, R-0076, R-0077); form (3), the leaf alone (R-0010). Which
  form a PGI bundle uses turns on the version and on keyless or self-managed
  signing (§3.1); outside the PGI the source states no rule;
- zero or more log entries (unannotated, L132; encouraged for public bundles,
  R-0173), each with a proof annotated as required (R-0066), a promise per §3.1,
  and optionally the body (R-0160);
- zero or more RFC 3161 tokens (L137; R-0175);
- with a short-lived certificate, at least one promise or token (R-0168).

The two examples show the spread. The message-signature bundle uses form (3)
with one entry carrying a promise, a proof and the body, and no token. The DSSE
bundle is v0.3 in form (2) with one certificate, one entry and one token, made
by a test instance rather than the PGI (SD-R-13), so its chain breaks no PGI
rule.

**From outside the bundle** (C-02):

| needed | what the source says |
|---|---|
| the CA certificates a chain must reach, and for form (3) the intermediates | trusted on the verifier's own account (R-0008, R-0194); the PGI's trusted root is named (L92-93) and nowhere defined |
| the log's public key, hash and scheme | out of band, from the log's operators (R-0149); the log is identified by its key (R-0116), the derivation of the key id unsaid (SD-R-17) |
| the timestamp authority's certificate | nothing (S-02) |
| the signer's key, for form (1) | out of band, its algorithm with it (R-0039); the hint's format agreed out of band (R-0122) |
| the artifact, for a message signature | provided at verification (R-0180) |
| the verification procedure | the client specification, a linked Google document (R-0085; SD-R-21) |
| how to rebuild an entry, the promise's payload, the leaf hash and the checkpoint | Rekor's types on `main` (R-0132); Rekor's code at a commit (L784); nothing (SD-R-18); two documents on `main` (R-0139) |
| which identities, payload types and versions are acceptable | policy: the payload type must be supported and expected (R-0088); v0.1 support is a choice (R-0018, R-0020); identity is read from the certificate's extensions at verification (R-0169) against values the bundle does not carry |
| a clock, for a long-lived certificate | the verifier's own clock may serve (R-0156) |

So the page's opening claim (L893), that a bundle alone suffices to check an
artifact's signature, holds only together with this table (SD-D-1).
*(inferred)* For mofn this is R-I-02 in concrete form (Q-02).

### 3.4 Is a single-signature bundle ITE-5 compliant?

**The in-toto side.** ITE-5's one MUST is that a format support several
signatures in a single envelope (in-toto-envelope-v1 R-0003, PR #141 @ 23c0d40; ITE:L12). The Envelope layer lists the
Sigstore Bundle among the alternative envelope schemas, as supporting DSSE but
not currently ITE-5 compliant, because it requires a single signature
(in-toto-envelope-v1 R-0030, PR #141 @ 23c0d40; ITE:L19-22), and footnotes an open discussion about DSSE signature
extensions for bundles (ITE:L98).

**This source.** It agrees on the fact and gives its reasons (C-01, quoted
above). The page repeats the rule:

<!-- q L1010 "DSSE envelopes in a Sigstore Bundle must also" .. "allows multiple)." -->
> DSSE envelopes in a Sigstore Bundle must also contain only a single signature (the DSSE spec allows multiple).

and requires the envelope to conform to the in-toto Envelope layer
specification (R-0181), linked at `main`: the document that says the bundle
does not comply (SD-D-3).

**Answer.** ITE-5 tests a format, not an instance: producers may use other
formats that meet it, and a format must support several signatures (ITE:L9-12).
So:

1. **The bundle format is not ITE-5 compliant**, and both sources say so: it
   forbids a second signature and makes a verifier reject any count but one
   (R-0089, R-0090, R-0182).
2. **A single-signature bundle is not more compliant than a two-signature
   one**, because there is no per-instance compliance to have. With two
   signatures the bundle is invalid; with one it is a valid bundle of a format
   that does not comply.
3. **The DSSE envelope inside it, taken alone,** is a DSSE envelope with a
   one-element `signatures` array. *(inferred)* It meets the field rules a
   one-element array can meet (in-toto-envelope-v1's §2: `signatures` an
   array), and DSSE, the RECOMMENDED format (ITE:L8), meets ITE-5 by allowing
   several. That answers ITE-DN Q-06 (PR #141 @ 23c0d40) at the field level only: whether DSSE's
   own text admits the envelope was not checked (DSSE is
   `secure-systems-lab-dsse`, not read here).
4. **The two framings differ.** in-toto treats the bundle as the envelope;
   this source treats the DSSE envelope as the envelope and the bundle as its
   container. Under the first a bundle is a non-compliant envelope; under the
   second a compliant envelope sits in a container whose rule forbids the
   compliance being used. The source's second reason is structural:
   `VerificationMaterial` holds one key-material member (R-0183), so a second
   signature would have nothing to verify against. The way out it sketches,
   `VerificationMaterial` carried per signature as a DSSE signature extension
   (R-0072, R-0073, R-0004), cannot be carried by the envelope.proto it ships, whose
   `Signature` has only `sig` and `keyid` (SD-R-7), and in-toto's footnote
   points at the same mechanism (ITE:L98). Both sides say currently (L180,
   ITE:L21).

**What it means for mofn** (all *(inferred)*):

- **ITE-DN K-01** (PR #141 @ 23c0d40; ITE-DN:153), which the issue names, carries over with more
  force. The page fixes a PGI bundle's content to an in-toto JSON Statement
  (C-03), so a PGI export is ITE-DN's E2 and R-O-05's first sentence cannot
  hold (K-03). One signature changes nothing there; it adds that an export is
  one signer per object.
- **DEC-005** (ARCH-0001:643-645). Its DSSE option names two products: plain
  DSSE, ITE-5 compliant, with any number of signatures and no trust evidence;
  and DSSE in a Sigstore bundle, one signature, with certificate, log and
  timestamp evidence and a trust root to check them by, which is what
  `gh attestation verify` checks for mofn's own releases (RELEASE:202-203).
  COSE_Sign1 is one-signer and not ITE-5 either (ITE-DN:148). Choosing DSSE
  does not choose between the two (Q-06).
- **A classical and a post-quantum signature over one statement** cannot be one
  bundle: one signature (R-0089), one key material (R-0183), no hybrid or
  composite value in the enum (§7 check 5), and the ML-DSA values experimental
  (R-0104). It can be two bundles over the same payload, each with its own
  key material, entries and tokens, neither naming the other, so the pairing
  is the verifier's policy; or one plain DSSE envelope with two signatures,
  ITE-5's own form, outside Sigstore; or one signature under a hybrid suite,
  for which KSA reserves codes (SPEC-0002:363) and this source has no value.
  §6, Q-07.
- **KSA's own envelope** carries one signature (SPEC-0002:302) and is never an
  ITE-5 envelope (ITE-DN:143). On this question the bundle and KSA stand
  together (A-06): a threshold is k objects in both, counted by policy
  (SPEC-0004:423-432), with C-06's caveat for keyless signers.

---

## 4. MD-3, ADR-0004 and DEC-002, field by field

MD-3 narrowed DEC-002 to option 5 on 2026-09-28: the CBOR data model, no IANA
tags, COSE as export only, type identity as (defining key, label) per P1, and
YAML as the human form (MD:51-54). ADR-0004 accepted option 5 on 2026-10-25,
closing the narrowing (ADR-0004:132-133), made COSE_Sign1 and DSSE the export
envelopes (ADR-0004:51-52) and left DEC-005 open (ADR-0004:112). This source is
a signing container around an envelope, so the mapping below is the one
docs/extraction.md:123-126 asks for, and §4.3 is the part it insists on
(docs/extraction.md:128-135).

### 4.1 Field by field (the rows R-I-01 would hold)

| bundle field | what it is here | nearest in KSA | import | export from KSA |
|---|---|---|---|---|
| `media_type` | the container's version, under no signature (R-0001, R-0021, R-0191) | none: KSA's versions are signed, `suite` and `kind` in the TBS (SPEC-0002:433-434) and the DS label's `v1` (SPEC-0002:397-407) | used, then dropped; accepted values fixed by policy (C-04) | the v0.3 spelling, the one this file gives for JSON (R-0021) |
| `verification_material.public_key`, form (1) | an unauthenticated hint whose format is agreed out of band (R-0121, R-0122); RFC 6962's derivation RECOMMENDED (R-0123) | `says`, a hint checked at V6 (SPEC-0002:308, SPEC-0002:698); the key from the key store (SPEC-0002:710-723) | never a principal; the kid is computed from the key (ADR-0005:87-92), and K-02 decides what a disagreeing hint does | the KSA kid as hint, which ADR-0005 allows and R-0123 does not recommend (K-02); our key published out of band (D-01) |
| `x509_certificate_chain`, form (2); `certificate`, form (3) | the signing key in a CA-issued leaf, identity in its extensions (R-0169) | none native (R-M-01, ARCH-0001:434); `pub` carries a raw key, never a certificate (SPEC-0002:311) | a foreign identity assertion about a key, X.509 provenance (R-I-05, ARCH-0001:455; ARCH-0001:504); the key has no kid while suite 2 is unspecified (C-05) | none *(inferred)*: mofn holds no CA, and PGI keyless signing certifies an OIDC identity, not a KSA key |
| `tlog_entries[]` | log evidence: index, time, proof, promise, body (D-02) | none native; the SCITT-receipt row: evidence that changes no meaning (ARCH-0001:513); registration optional (ARCH-0001:466) | kept as received, as evidence about the foreign signature; checking the promise is K-01 | only if mofn registers with Rekor, which NG4 leaves optional (ARCH-0001:156) |
| `timestamp_verification_data` | RFC 3161 tokens whose imprint hashes the content signature (R-0003, R-0190) | none native; SPEC-0001 §11's timestamp token (SPEC-0001:415-422) | kept as received; the authority's trust is unsaid (S-02) | *(inferred)* a token over the export's own signature |
| `message_signature.message_digest` | identification only (R-0038, R-0110) | target type 2, `[2, digest-alg, bytes]` (SPEC-0002:454), digest codes 1 to 3 being SHA-256, SHA-384, SHA-512 (SPEC-0002:850-854) | dropped; the target is the digest the importer computes (A-02). `HashAlgorithm` 1 to 3 name the same three algorithms in the same order (L318-322, §7 check 5): equal numbers in two registries, *(inferred)* mapped by name, never by number (P1). `SHA3_256` and `SHA3_384`, 4 and 5, have no KSA code | *(inferred)* the target's digest under its algorithm's name |
| `message_signature.signature` | a signature over an artifact or its digest (X-04) | none: no KSA signature is bare | evidence that a key signed bytes, with no predicate (Q-11) | none; a KSA key making one is C-07's hazard (Q-08) |
| `dsse_envelope.payload` | the signed bytes; under the page an in-toto JSON Statement (R-0181) | `tbs`, element 2, exactly as signed (SPEC-0002:309) | kept byte for byte (SPEC-0001:229-232); the KSA decoder cannot read it (SPEC-0002:251-266), so the Statement layer maps it (library#134) | E2, a JSON Statement (K-03); E1, the TBS, under the proto alone (C-03) |
| `dsse_envelope.payloadType` | signed inside the PAE (A-01) | the DS label and `kind` (SPEC-0002:397-407, SPEC-0002:433) | kept; checked against the types the importer supports and expects (R-0088) | in-toto's generic type under the page (R-0181) |
| `dsse_envelope.signatures[0].sig` | the signature over the PAE (R-0095) | `sig`, element 3, over the DS label and the TBS (SPEC-0002:310) | verified and kept; the importer never re-makes it | a new signature (ITE-DN K-02, ITE-DN:462-475) |
| `dsse_envelope.signatures[0].keyid` | an unauthenticated hint (R-0098), equal to the form (1) hint when there is one (R-0086); empty in the DSSE example (L1132) | `says`'s hint role (SPEC-0002:308) | never a principal (ARCH-0002:525-530) | the kid as hint (ADR-0005:87-92), equal to the form (1) hint |
| — none | the signature algorithm, from the certificate or out of band (C-05) | `suite`, signed (SPEC-0002:350-352) | inferred from the key; for P-256 there is no suite | dropped |
| — none | how long what was signed holds (C-09) | `valid` (SPEC-0002:494-501) | from the payload or the importer | dropped, unless the payload carries it |
| — none | the principal | `says` in the TBS, the speaker (SPEC-0002:435) | keyless: a CA-asserted name (X-02); form (1): the out-of-band key | E2: where the Statement layer puts it, never `keyid` (ARCH-0002:525-530) |

### 4.2 MD-3, clause by clause

| MD-3 clause (MD:51-54) | what this source does | finding |
|---|---|---|
| the CBOR data model | protobuf messages exchanged as proto3 JSON; a JSON payload under the page; DER inside (certificates, tokens); a text checkpoint | nothing at this boundary is CBOR; option 5 meets it with codecs it does not otherwise need (§4.3 item 1) |
| no IANA tags | no CBOR, so no tags; registry dependence through lists one project runs and the media-type tree (X-03) | ADR-0004 item 3's IANA list does not reach these (§4.3 item 2) |
| COSE as export only | no COSE anywhere; DSSE in a bundle | MD-3's wording names an export the supply-chain world does not use. The DSSE half came with option 5's text and ADR-0004 item 4 (ARCH-0001:541, ADR-0004:51-52), as ITE-DN §3.4 item 3 found (ITE-DN:602-606); this source adds that DSSE alone is not the deployed unit either (§4.3 item 3) |
| type identity is (defining key, label) per P1 | media types, `payloadType`, Rekor kinds, enum names, OIDs: all global (X-03) | natively excluded; at the boundary each is a label mapped lossily (R-I-01) |
| YAML as the human form, by a canonical one-way mapping | none; the page shows JSON | R-O-05's last sentence carries over: show what was verified (A-02) |
| option 2 retained only as the comparison fixture | — | no effect |

### 4.3 Where the source cuts against MD-3 and option 5

1. **The boundary's codecs, which option 3 would partly share.** To import a
   bundle mofn parses proto3 JSON, base64, DSSE's PAE, X.509 and CMS in DER, a
   text checkpoint, Merkle proofs and, to check a promise, Rekor's canonical
   JSON (K-01). Option 5 uses none of these natively. Option 3, JSON with
   RFC 8785 and DSSE as the signed form (ARCH-0001:539), would have shared the
   JSON parser and the PAE, not the rest, and not necessarily the promise's
   canonicaliser, which this source never says is RFC 8785 (L781-784). That is a
   cost option 5 pays and option 3 would partly not. Option 3 was withdrawn on
   four grounds this source does not touch (ADR-0004:121-124;
   DECISIONS:116-119), so this is evidence recorded, not a reopening.
2. **Registry-free, but not list-free.** Protobuf keeps IANA out of its own
   fields. The bundle still depends on lists one project runs (X-03), on the
   media-type tree for its version names, and on an OID arc (R-0125) under
   IANA's private-enterprise numbers (outside this source). P1 objects to
   central allocation by anyone (ARCH-0002:74-80). ADR-0004 item 3 states
   option 5's no-registry property as a list of IANA registries it excludes
   (ADR-0004:46-50), as ARCH-0001 asked (ARCH-0001:561-567). *(inferred)* That
   list, written against COSE and CWT, names none of the lists a Sigstore
   import meets, so as written the property says nothing about this boundary.
   Not a cost to option 5; a gap in how its property is stated.
3. **DSSE is the envelope; the deployed unit is the bundle.** ADR-0004 item 4
   makes COSE_Sign1 and DSSE the export envelopes (ADR-0004:51-52). The export
   a Sigstore verifier accepts, the verifier mofn's own release notes send
   users to (RELEASE:202-203), is DSSE inside a bundle with a certificate or an
   out-of-band key and with log or timestamp evidence (C-11; R-0168).
   *(inferred)* Under every DEC-002 option an R-I-03 export that must verify
   with Sigstore tooling needs this container, a log or a timestamp authority,
   and for keyless signing an OIDC identity a KSA key does not have. The cost
   is not a discriminator, but the wording of MD-3 and ADR-0004, envelope
   only, understates what DEC-005's DSSE option has to deliver (Q-06).
4. **Protobuf is not in the option set, and would not have changed the
   scoring.** The source's normative schema is a protobuf IDL: field numbers,
   oneofs, reserved ranges, annotations that bind producers by convention only
   (R-0184), and two encodings, binary and proto3 JSON, neither canonical. That
   works here because nothing hashes or signs a bundle (R-0189). KSA hashes every
   statement and definition (SPEC-0002:288-290), so *(inferred)* a protobuf
   candidate would have needed a deterministic serialisation and a rejecting
   decoder, what option 5 pays for under P5.1 (ARCH-0002:412-415): option 5's
   shape on another data model, scoring no better on ADR-0004's drivers
   (ADR-0004:64-72). Recorded because the extraction asks for the cuts; it is
   not one.
5. **Versioning cuts the other way.** The bundle's version is unsigned and
   selects rules (C-04); KSA's is signed (D-03). Option 5 is on the right side
   here, and so is every option that signs its payload's type.

### 4.4 Where it favours option 5 and SPEC-0002

- A-03: the source carries the log's body because re-serialised JSON did not
  reproduce, the R-O-05 and P5.1 argument for carrying signed bytes, made by a
  design whose log signs canonical JSON.
- A-01, A-05, A-06: the type inside the signature, the key id a hint, one
  signature per object, as SPEC-0002 §5 has them (SPEC-0002:302-311).
- D-03: KSA's version lives inside signed bytes.

### 4.5 Not discriminators

- K-01, the promise's canonical JSON: every option's importer meets it.
- K-03, re-signing a JSON Statement: every option re-signs for an in-toto
  export (ITE-DN:628).
- X.509, CMS, Merkle proofs and the text checkpoint (§4.3 item 1): independent
  of the native encoding.
- C-01, one signature: SPEC-0002 §5's under any encoding.
- K-02 and C-05, the hint and the missing P-256 suite: DEC-003's and SPEC-0002
  §6's, not DEC-002's.

### 4.6 What an export deliberately does not carry

*(inferred, by analogy with ITE-DN §3.7, ITE-DN:634-645)*

- no principal in `keyid` or the hint (P5.2, ARCH-0002:525-530; A-05);
- no field outside those this source defines (P5.2's export rule, ARCH-0002:510,
  read onto the bundle exterior);
- no second signature (C-01), and no threshold as a count of bundles (C-06;
  ITE-DN C-02, ITE-DN:147);
- no message signature by a KSA key (C-07);
- not the native signature, which does not verify under PAE (ITE-DN:462-475);
- not the signed suite, the statement digest, the validity window or `pub`
  (§4.1).

---

## 5. T-052: what a byte-faithful import of a real release keeps

T-052 asks to round-trip a real SLSA provenance from a public release
(BACKLOG:189), and I4's demo asks a real SLSA attestation to import as an
`ArtifactStatement` and round-trip (PLAN-0001:487); L-041 opened the
extractions those rows cite (BACKLOG:268), and DL-0047 left T-052's version to
its owner (DL-0047r:16-20). mofn's own releases carry one: each file published
as `wallet-v0.8.1` has a build-provenance attestation (PLAN-0004:455-458), made
by the release workflow (RELEASE:210-212) and checked with
`gh attestation verify` (DL-0043r:138-144). lane-a's sample 3 fetches such
bundles with `gh attestation download`, which writes one bundle per line as the
attestation API returned it (LANE-A-03:57-77, the comment at LANE-A-03:74-75).

**The layers, and what authenticates each:**

| layer | its bytes | authenticated by | keep |
|---|---|---|---|
| the bundle | the JSON text as received | nothing (§3.2) | the text as received, as provenance: the only copy of what arrived |
| the DSSE envelope | none of its own: a JSON object inside the bundle's text | nothing, as an object | its parts, never a re-serialised envelope |
| the signed input | the PAE, 1388 octets in the example | the signer's signature | derivable, a pure function of the next two rows (§7 check 2) |
| the payload | the in-toto Statement's octets after base64 decoding, 1344 in the example | the signer's signature, through the PAE | byte for byte: the original bytes SPEC-0001 §5.3 keeps (SPEC-0001:229-232) |
| `payloadType`, `sig`, `keyid` | a string, decoded octets, a string | the PAE covers `payloadType`; `sig` is the signature; `keyid` nothing | all three, as values |
| verification material | certificate DER; per entry `log_index`, `log_id`, `integrated_time`, `canonicalized_body`, the promise, the proof and the checkpoint text; token DER | the CA; the log, its promise over the first four (R-0147) and its checkpoint over the tree head; the timestamp authority | as decoded octets and values: their JSON spelling is under no signature, their values are |

**Byte-faithful means one of two things**, and T-052 should say which (Q-01):

1. *Faithful to the signed bytes.* Keep the payload octets, `payloadType`,
   `sig` and every piece of verification material as decoded values.
   *(inferred)* Any bundle re-emitted from them verifies as the original did,
   whatever its JSON spelling, since no signature covers the spelling (§3.2),
   so a round trip through mofn loses nothing a verifier checks. The import's
   identity is then over the payload octets and `payloadType`, as ITE-DN Q-13
   proposed for plain DSSE (ITE-DN:910-916).
2. *Faithful to the file.* Keep the received text, because nothing makes a
   re-serialiser reproduce it: the source prints one message in two key
   orders, its examples print three defaults a default serialiser omits, and it
   names field-order and whitespace variance in the log's JSON (C-08). lane-a's
   `.bundle.json` and `.envelope.json` are re-serialised with `json.dumps`, and
   are faithful neither to the file nor, as text, to anything signed; its
   `.statement` and `.pae` files are the signed octets (LANE-A-03:96-103).

*(inferred)* Doing both costs nothing: keep the text, and keep the decoded
values beside it as what the importer verified.

**What the source says an importer checks**, if it verifies rather than taking
a foreign verdict: exactly one signature, rejecting any other count
(R-0090), which lane-a does not check, taking `signatures[0]`
(LANE-A-03:119); a payload type it supports and expects (R-0088); the signature
over the rebuilt PAE, which lane-a checks with the leaf's key as ECDSA with
SHA-256 (LANE-A-03:119-123); the certificate valid at a trusted signing time
(R-0085, R-0193), which needs a promise, a token or a clock (A-04) and the
trust material of §3.3; a carried body's signature against the envelope's
(R-0067); and the version, by policy (C-04). lane-a checks neither the chain, nor
the identity, nor the log entry, and says so (LANE-A-03:16-21). Its comments
label the single certificate v0.3 and the chain v0.1 or v0.2
(LANE-A-03:82-85); the source allows a chain in a v0.3 bundle outside PGI
keyless signing, as in the DSSE example (L1083-1085). The code reads whichever
field is present, so the labels are wrong and the behaviour is not.

**What the source cannot settle for T-052:** which version and time source
`actions/attest-build-provenance` emits (record.yaml:106-109); whether one
attestation covers all three files the release step's pattern matches
(RELEASE:193, RELEASE:212), since a Statement may name several subjects and
that is the Statement layer's business (library#134); and the predicate's
version, T-052's v1.1 against the library's 1.2 (BACKLOG:189). *(inferred)* The
speaker of the native statement an import yields is the importer, as the SLSA
provenance extraction concluded (SLSA-DN:882-889): the keyless signer has no
kid (C-05), and R-I-02 keeps the foreign object from becoming an anchor
(ARCH-0001:452).

---

## 6. Post-quantum

The enum's two warnings about post-quantum and hash-based schemes:

<!-- q L409-410 -->
> These algorithms are deprecated and should not be used. There are no plans to support SLH-DSA at this time.

<!-- q L432-436 -->
> USER WARNING: ML_DSA_44, ML_DSA_65 and ML_DSA_87 are experimental algorithms. In the future they MAY be used by private Sigstore deployments, but they are not yet fully functional. This warning will be removed when these algorithms are widely supported by Sigstore clients and servers, but care should still be taken for production environments.

1. **What the enum offers.** `PublicKeyDetails` has 24 values, 9 of them
   deprecated (§7 check 5). Not deprecated, besides UNSPECIFIED: six RSA,
   three ECDSA (P-256, P-384 and P-521, each with its matching hash), Ed25519
   and its prehash variant, and the three ML-DSA values the second warning
   covers. LMS and LM-OTS: deprecated, and stateful (L407-418). No value is
   hybrid or composite, and no name mentions SLH-DSA (check 5); 24 to 50 are
   reserved (R-0107).
2. **None of it is in a bundle.** `PublicKeyDetails` is unreachable from
   `Bundle` (C-05). An ML-DSA bundle is recognised by its certificate's key,
   whose identifiers the source leaves to FIPS 204 and RFC 9881 (L438; the
   library holds `fips-204` and `rfc-9881`, not read here), or by a key
   configured out of band.
3. **Pure ML-DSA and the message signature.** The ML-DSA values are the pure
   variants, which take data rather than digests (R-0103). *(inferred)* If a
   message signature is over the artifact's hash, as the page says, a pure scheme
   signs the 32-octet digest as its message, and a verifier that checks it over
   the artifact gets a different answer: SD-R-15's ambiguity becomes a failure
   to verify. DSSE has no such problem, the PAE being the message.
4. **No context string.** KSA's suite 8 passes `KSA-STMT-SIG-v1` to ML-DSA as
   its context (SPEC-0002:414-415). The source gives none (S-03). *(inferred)*
   A bundle's ML-DSA signature takes whatever context its signer used, and two
   implementations that disagree, empty against non-empty, fail each other;
   ITE-DN Q-14 asked the same of plain DSSE (ITE-DN:917).
5. **Sizes.** ML-DSA-65's signature is 3309 octets (SPEC-0002:416), 4412
   base64 characters in a bundle (§7 check 7). The source states no limit, and
   a token's imprint hashes the signature whatever its size (R-0190).
6. **No hybrid in one bundle** (§3.4): one signature, one key material, no
   composite value. A classical and a post-quantum signature are two bundles
   that do not name each other; KSA's reserved hybrid suites (SPEC-0002:363)
   have no bundle form. Q-07.
7. **The evidence ages too.** SPEC-0001 §11 wants a post-quantum suite or an
   independent timestamp for statements that must verify for decades
   (SPEC-0001:415-422). A bundle's token and promise are that timestamp for
   the signer's signature, and each is itself a signature, by a timestamp
   authority and a log whose algorithms the source never states. In the
   examples both promises and both checkpoint signatures are DER pairs of
   integers, the form ECDSA signatures take, and the token names
   ecdsa-with-SHA256 (§7 check 6). *(inferred)* A bundle's long-term value
   rests on the weakest of the signer's, the CA's, the log's and the timestamp
   authority's algorithms, a dependency SPEC-0001 §11's one sentence does not
   show.

---

## 7. Checks, arithmetic, and the enumerated *only*s

Every check here was run in this pass by a script in the lane's scratch
directory, standard library plus the `openssl` command, over the original
bytes the record pins; each prints what it examined.

1. **Key order and defaults in the examples.** The two complete bundles were cut
   from `bundle.md`'s original bytes (its lines 165-203 and 211-265; rendering
   L1036-1074 and L1082-1136, every line checked equal to the rendering) and
   read with an order-keeping JSON parser. 12 objects examined: `Bundle`,
   `VerificationMaterial`, `TransparencyLogEntry` and `InclusionProof` in each,
   `MessageSignature` and `HashOutput` in the first, `Envelope` and `Signature`
   in the second. All 12 list their keys in proto field-number order. The
   §5.1.2.2 placeholder (L1013-1022) prints `keyid` before `sig`, the reverse.
   Printed defaults: the DSSE example's proof `logIndex` `"0"`, its empty
   `hashes`, and its empty `keyid` (L1107, L1110, L1132).
2. **What is signed, reproduced.** DSSE: `payloadType` 28 octets, payload 1344
   octets, PAE 1388 octets beginning `DSSEv1 28 application/vnd.in-toto+json
   1344`; the payload equals the attestation printed at L1142-1188 plus its
   final newline. `openssl dgst -sha256 -verify` under the leaf's key over the
   PAE: verified; one bit of the PAE flipped: failure. The intoto body's
   payload and `sig` are base64 of the bundle's base64 text, its `publicKey`
   decodes to a PEM certificate whose DER equals the bundle's leaf, and its
   `payloadHash` is the payload's SHA-256. Message signature:
   `openssl pkeyutl -verify` under the leaf's key with the 32-octet
   `message_digest` as the hash: verified; one bit of the digest flipped:
   failure; `openssl dgst -sha256 -verify` with the digest hashed again as the
   message: failure. The hashedrekord body's artifact hash equals the digest, its
   signature equals the bundle's, and its PEM key's DER equals the bundle's
   certificate. The intoto body's own `hash` was reproduced by the verify pass
   (examples/README.md:59): SHA-256 of the sorted, compact JSON of the bundle's
   envelope with the certificate PEM beside the signature and the empty `keyid`
   left out, a scheme the source does not state.
3. **A KSA kid against an RFC 6962-style hint.** Alice's TV-1 key from
   `spec/vectors/ksa-core/vectors.json` at `656bac0`: its kid, SHA-256 of the
   32-octet key, is `21fe31df…21b9`, equal to the vector's. Its DER
   SubjectPublicKeyInfo is the 12-octet prefix `302a300506032b6570032100` and
   the key, 44 octets, which `openssl pkey` reads as an Ed25519 key and writes
   back identically; its SHA-256 is `06e3fd8f…2fa9`. Different, as for any key
   whose SubjectPublicKeyInfo is not its raw encoding.
4. **Reachability.** Over the four original `.proto` files: 26 declared types,
   23 messages and 3 enums; 18 reachable from `Bundle` by field types; not
   reachable `DistinguishedName`, `ObjectIdentifier`,
   `ObjectIdentifierValuePair`, `PublicKey`, `PublicKeyDetails`,
   `SubjectAlternativeName`, `SubjectAlternativeNameType` and `TimeRange`. The
   one enum reachable is `HashAlgorithm`.
5. **Enums and field numbers.** `HashAlgorithm`: 6 values, 0 to 5, 2
   deprecated (`SHA3_256`, `SHA3_384`). `PublicKeyDetails`: 24 values numbered
   0 to 23 with no gap, 9 deprecated, 24 to 50 reserved; `ML_DSA_65` 21,
   `ML_DSA_87` 22, `ML_DSA_44` 23; no name containing SLH, COMPOSITE, HYBRID,
   FALCON or ED448. `VerificationMaterial`: `public_key` 1,
   `x509_certificate_chain` 2, `certificate` 5, `tlog_entries` 3,
   `timestamp_verification_data` 4. `Bundle`: `media_type` 1,
   `verification_material` 2, `message_signature` 3, `dsse_envelope` 4,
   reserved 5 to 50.
6. **Certificates and evidence.** `openssl x509` on both leaves: P-256 keys;
   issuers `O=sigstore.dev, CN=sigstore-intermediate` and `CN=sigstore,
   O=sigstore.mock`; empty subjects; a critical URI subject alternative name
   naming a GitHub workflow at a ref; valid 2024-08-28 18:44:34 to 18:54:34 and
   2023-02-01 00:00:00 to 00:10:00, ten minutes each; signed
   ecdsa-with-SHA384. Both promises (72 and 70 octets) and both checkpoint
   signatures (after a 4-octet key hint, 70 and 72 octets) are DER SEQUENCEs of
   two INTEGERs. The token, by `openssl ts -reply` and `asn1parse`: granted,
   policy `1.3.6.1.4.1.57264.2`, imprint SHA-256, signed ecdsa-with-SHA256, its
   certificates field present and empty.
7. **Arithmetic.** PAE framing: 6 (`DSSEv1`) + 1 + 2 (`28`) + 1 + 28 (the
   type) + 1 + 4 (`1344`) + 1 = 44 octets, and 44 + 1344 = 1388. Base64 of n
   octets is 4·⌈n/3⌉ characters: 3309 gives 4412. Reserved: 5 to 50 is 46
   numbers, 24 to 50 is 27. A suite-1 key's SubjectPublicKeyInfo: 12 + 32 = 44
   octets.
8. **The *only*s that rest on an enumeration.** Form (1) is *the only*
   key-centric form: the three forms are enumerated (L82-102), and only the
   first names a key without a certificate. `HashAlgorithm` is *the one* enum
   reachable (check 4). The bundle binds its parts to the content in *exactly
   two* ways: a search of every rule relating verification material to the
   content finds R-0003 and R-0067; the third candidate, the key-hint
   equality, relates a hint to a hint, and the extension rule cannot be carried
   (SD-R-7). lane-a's sample 3 is *the only* mofn code that reads a bundle: at
   `656bac0` a search for `verificationMaterial`, `dsseEnvelope`,
   `tlogEntries`, `messageSignature`, `vnd.dev.sigstore` and `sigstore_bundle`
   finds six lines, all in `prototype/lane-a/03_slsa_provenance.py`. Every other
   *only* here is a citation, beside its source.
9. **Digests, three ways.** `shasum -a 256` of the five inputs equals
   `render-source.py`'s table and, for `sigstore_bundle.proto`,
   record.yaml:20; the rendering re-made from them is byte-identical to
   `.cache/sigstore-bundle-0-3.txt`, whose sha256 equals `requirements.yaml`'s
   `source_digest`; retrieved 2026-11-20 (record.yaml:21).
10. **The silences.** A case-insensitive search of the rendering finds no
   `revoc`, `TSA`, `timestamp authorit`, `hybrid`, `composite`, `unknown`,
   `threshold`, `OIDC`, `ephemeral` or `domain separ`; `trusted root` only at
   L93, `root of trust` at L92 and L644, `TUF` at L644, `quantum` at L428,
   `SLH` at L410, `short lived` at L898, `long-lived` at L835, `keyless` at
   L104, L108 and L111.

---

## 8. Source defects found by this lane

Ids are lane-prefixed for the verify pass to unify with SD-R-n
(`normative.md`) and the other lanes' lists; each quotes or cites the lines it
rests on, and the prose is ours. None repeats an SD-R entry; SD-D-3 extends
SD-R-21. The verify pass unified the four lanes' lists in `normative.md`
(Source defects): SD-D-1 is SD-33, SD-D-2 SD-34, SD-D-3 SD-35, SD-D-4 SD-26,
SD-D-5 SD-36, SD-D-6 SD-37, and SD-D-7 is merged with the protocol lane's
SD-P-10 as SD-30.

### SD-D-1 — §5.1: a bundle is called everything a verifier needs

<!-- q L893-894 -->
> A Sigstore bundle is everything required to verify a signature on an artifact. This is satisfied by the **Verification Material** and signature **Content**.

The source itself sends the verifier outside the bundle for the CA it chains
to (R-0008), the form (1) key (R-0039; the page says it is not embedded, R-0172), the log's
key (R-0149), the artifact (R-0180) and the procedure (R-0085), and never says where a
timestamp authority's certificate comes from (SD-D-7). Read alone, the page
presents a bundle as self-verifying; §3.3 lists what it lacks.

### SD-D-2 — §1.3: the one-signature limit reads as DSSE's

<!-- q L176-178 "DSSE envelopes in a bundle" .. "multiple signatures." -->
> DSSE envelopes in a bundle MUST have exactly one signature. This is a limitation from the DSSE spec, as it can contain multiple signatures.

Read plainly, the second sentence attributes the limit to the DSSE
specification and gives as the reason that DSSE can carry several signatures.
The limit is the bundle's, imposed on DSSE, as the page puts it the right way
round (R-0182); the requirements lane read *from* as *relative to* when it
rejected the sentence as a candidate (C-0018). Editorial, of SD-R-1's kind;
affects how R-0089 is explained, not what it requires.

### SD-D-3 — §5.1.2.2: conformance to a moving document that says the bundle does not conform

The page requires the DSSE envelope to conform to the in-toto Envelope layer
specification and the payload to be an in-toto Statement, each linked at
`main` (R-0181, quoted under C-03). The Envelope layer lists this bundle as not
ITE-5 compliant (ITE:L21-22), which the source never acknowledges, and the
links can change without this source changing. SD-R-21 lists the source's
unpinned references; these two are not on it.

### SD-D-4 — §4.5: a carried log body is bound to the content by its signature alone

The rule (quoted under S-04) names the signature. A hashedrekord or intoto body
also carries the signer's key or certificate, and a hashedrekord body the
artifact's hash (§7 check 2), and no rule requires them to equal the bundle's
key material or `message_digest`. A verifier that does exactly what the source
says accepts an entry whose body names another key, if the signature bytes
match. Whether the client specification closes this was not checked; it is not
in the source. Affects R-0067.

### SD-D-5 — §1 and §1.3: the version selects the rules and no rule protects it

`media_type` decides which key-material form applies, whether a promise without
a proof is acceptable, and whether a v0.1 bundle is acceptable at all
(R-0013, R-0014, R-0018, R-0020), and no signature covers it (§3.2). The source never
says the version must come from the verifier's policy rather than from the
bundle; its one guard is a SHOULD NOT for ecosystems that never produced v0.1.
Affects R-0001 and R-0191.

### SD-D-6 — §3.4 and §2.1: no rule separates keys between the two content types

A DSSE signature is over a PAE (L237-244); a message signature is over a
message with no prefix (R-0109, R-0177). Nothing forbids one key making both, and the
source does not mention the consequence: with such a key a message signature
over an artifact whose bytes are a PAE is a DSSE signature over that PAE's
payload (C-07).

### SD-D-7 — §1.1: a timestamp token's own signature is never required to be checked

<!-- q L56-60 -->
> A list of RFC3161 signed timestamps provided by the user. This can be used when the entry has not been stored on a transparency log, or in conjunction for a stronger trust model. Clients MUST verify the hashed message in the message imprint against the signature in the bundle.

The one rule is the imprint (R-0003). Nothing says the token's signature is
verified, against whose certificate, or where that certificate comes from; no
line names a timestamp authority (§7 check 10), and the DSSE example's token
has an empty certificates field (§7 check 6). A verifier that does what the
source says checks that a token is about the signature, never that an authority
it trusts made it; the requirements lane's trusted signing time
(R-0193) assumes the check.

---

## 9. Open questions

Source defects are recorded in §8 and not repaired; the record's list is
`normative.md`'s Source defects, which the verify pass unifies with §8. Q-01 to
Q-12 are questions for mofn's owners, and this file answers none of them.

- **Q-01 — What T-052 means by byte-faithful** (§5): the signed bytes, the file
  as received, or both; and whether an import's identity is over the payload
  octets and `payloadType`.
- **Q-02 — Where the Sigstore trust root lives** (C-02, §3.3). A KSA anchor
  trusts kids (SPEC-0004:181-203), and ARCH-0001 holds a verifier's configured
  trust for artifact services as such anchors (ARCH-0001:403); Fulcio's CAs,
  Rekor's keys and timestamp-authority certificates are not kids. Does an
  importer keep them outside the anchor model, or take a foreign verifier's
  verdict, `gh attestation verify`, and sign its own statement about it? R-I-02
  holds either way.
- **Q-03 — Does ADR-0005's import rule reach a bundle's hint and DSSE `keyid`**
  (K-02)? The RECOMMENDED derivation never matches a KSA kid, a keyless `keyid`
  is empty, and a P-256 key has no kid.
- **Q-04 — Thresholds over keyless signers** (C-06). Is a keyless signer's
  principal its key, its certificate's identity, or nothing until an importer
  vouches for it; and how does SPEC-0004 §6.4 count k bundles from one
  identity?
- **Q-05 — The log's promise** (K-01). Does an importer verify it,
  canonicalising inside verification against R-O-05, or rely on the inclusion
  proof and a timestamp token, or on a foreign verifier? If it verifies,
  R-O-03 wants an algorithm the source does not name.
- **Q-06 — DEC-005's DSSE option** (§3.4, §4.3 item 3): plain DSSE, or DSSE in
  a Sigstore bundle? #32, the self-attested release (PLAN-0004:462-463), meets
  the choice first.
- **Q-07 — A classical and a post-quantum signature over one statement** (§3.4,
  §6): two bundles, and paired how; one plain DSSE envelope with two
  signatures; or a hybrid suite?
- **Q-08 — Should a KSA key ever make a bundle's message signature** (C-07)?
  SPEC-0001 §5.3 recommends against reuse; SPEC-0002 §13.2's guarantee assumes
  the other protocol domain-separates, and message signatures do not.
- **Q-09 — Which bundle versions an importer accepts** (C-04): v0.3 only, mofn
  having no history with older ones; and both v0.3 spellings (SD-R-3)?
- **Q-10 — Several subjects in one Statement** (§5). A release step over a
  pattern of three files may yield one attestation naming three subjects; is
  that one KSA attestation per subject? The Statement layer's question
  (library#134).
- **Q-11 — Message-signature bundles** (X-04): imported at all, and if so as
  what? lane-a skips them.
- **Q-12 — A §6 matrix row for the bundle** (C-10), for T-053's owner; §4.1 is
  candidate content.

---

## 10. Method, and what was read

- **The source** was read in full, L1-1189, in the rendering; the five inputs'
  digests were recomputed and the rendering re-made byte-identical (§7 check
  9).
- **Ids.** Every requirement id was written as a selector, a line range (for an
  inferred entry, its locator) and a fragment of the requirement's own text,
  anchored at the start or the end where a split child's text is a prefix or
  suffix of its parent's, and resolved by script against `requirements.yaml`,
  where both library readers agree on id, text, source lines, locator and verb
  for all 197 entries. A selector matching no entry or several stops the
  script. The resolved pairs, each id beside its full text, were then read:
  108 distinct ids of this record, and 2 of `in-toto-envelope-v1` (counted
  by script over this file's final text at the cross-check pass, leaving out
  the range "R-0001 to R-0197" in the opening). The identical-text groups were
  told apart by their lines. The two `in-toto-envelope-v1` ids were resolved
  the same way against that record's `requirements.yaml` at `23c0d40`.
- **mofn and library citations.** Every `DOC:n` range here (313 citations of 150 distinct ranges in the final text, counted by script at the cross-check pass over the document names of the table in *Things to hold*),
  was printed back by script from its blob at `656bac0` (the precedents' from
  `23c0d40` and `1bc07e5`, library files from this worktree or the library's
  source cache) and read beside its claim.
- **Quotations.** Each marker was rendered by `bin/check-quotes --render --only`
  on this file and checked by `bin/check-quotes`, which reports how many it
  examined. No other quotation of the source appears; mofn is paraphrased
  throughout.
- **Checks** 1-10 of §7 were run by scripts in the lane's scratch directory,
  which the record does not carry. Their results are reproducible from the
  record: checks 2, 6 and 9 by `examples/reproduce.py` and
  `protocol-evidence.derived.py`, checks 4 and 5 by
  `schema/check-protoc.derived.py` and `messages.yaml` (built from protoc's
  descriptor); the verify pass re-ran checks 3, 8 and 10 and the arithmetic of
  check 7, with the same results.
- **Read:** the source; the mofn files of *Things to hold*; the
  `in-toto-envelope-v1` source and design notes; the `slsa-provenance-1-2`
  design notes, §6 (`origin/fx1-slsa-provenance-136`, `1bc07e5`, cited
  SLSA-DN); and, as the brief's update allows, `normative.md`'s source defects,
  `examples/README.md`, `requirements.yaml` and `inferred-candidates.yaml` for
  ids, and `messages.yaml` for message names only. **Not read:** `summary.md`,
  the other lanes' files, DSSE's specification, RFC 3161, the Sigstore client
  specification, the trusted root, the repository's CHANGELOG.md and
  `sigstore_bundle_v2.proto`.

## 11. What this file decides

Nothing. No DEC-* is opened, ranked, accepted or reopened: DEC-005 stays open,
and ADR-0004 and ADR-0005 stand as accepted. No mofn file was edited. Every
consequence for mofn is marked *(inferred)* or posed as a question, and the
questions belong to their owners: Q-01 and Q-10 to T-052 (BACKLOG:189); Q-02,
Q-04, Q-05, Q-09 and Q-11 to whoever builds the importer (T-051, T-052); Q-03
to ADR-0005; Q-06 and Q-07 to DEC-005; Q-08 to SPEC-0001 and SPEC-0002; Q-12 to
T-053 (BACKLOG:190).

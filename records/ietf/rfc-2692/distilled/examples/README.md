---
record: rfc-2692
kind: examples
title: "rfc-2692 — examples and test vectors"
extracted: "2026-10-18"
reviewed_by: ""
---

# RFC 2692 — examples and test vectors

`vectors.yaml` holds **140 vectors** in two separate parts. Pass 1 (extract)
built them from `.cache/rfc-2692.txt` alone (sha256 `6a88c156…6d`).

- **Part 1 has 95 source examples.** Every example RFC 2692 prints gets one
  vector, so nothing is dropped. That covers every item of the List of
  Certificate Uses, every Open Question with its answer, the quoted template
  sentences, and the illustrative cases in the body. Fidelity is `verbatim` or
  `split`.
- **Part 2 has 45 constructed vectors.** These are deterministic tests that a
  harness can run against any design claiming to meet RFC 2692. Each is built
  only from a rule the source states, and each quotes that rule with its
  locator. Fidelity is `constructed`.

The header of `vectors.yaml` defines every field. It also defines the
`abstract-model` notation and the quoting rule. `count_reconciliation` there
lets a verifier recount.

## Why there are no byte-level vectors

RFC 2692 is a requirements document. It defines no certificate format, so
there is nothing to encode. The charter puts the format in the future: "The
task of the working group will be to develop Internet standards for an IETF
sponsored public key certificate format, associated signature and other
formats, and key acquisition protocols." The abstract says what this document
is instead: "This document presents that summary of requirements."

The few encoding statements it makes are constraints on a format that does not
yet exist:

- "In particular, ASN.1 is not to be used."
- "For efficiency, if possible, an SPKI certificate should be encoded in an
  LR(0) grammar."
- For the minimal CRL, "Its method of transmission is not specified."

The source prints no byte string, hex, S-expression or encoded certificate.
Constructed inputs therefore use synthetic labels: `key-A`, `cert-1`,
`crl-1`, `auth-X`, ISO 8601 times. They are never bytes or anything that looks
like a real SPKI encoding.

## How to read a vector

**Source examples.** `input` is the source text. `expected` says what a
conforming SPKI certificate design must be able to express for the example.
`expected_basis` says how far `expected` can be trusted:

- **`stated`** (7 vectors): the source states the outcome, and `expected` is a
  verbatim quote. These are the four Open Questions, the two quoted attributes
  in the answer to question 3, and the minimal CRL ("Such a CRL leads to
  non-deterministic program behavior.").
- **`rule-quoted`** (80): `expected` is this extraction's statement. The body
  rules it exercises are listed in `exercises` and quoted once each in
  `body_rules`.
- **`uncovered`** (8): no body requirement covers the use. `expected` says so
  and why, and invents no rule. The 8 are `SR-USE-06` (software),
  `SR-USE-11` (genealogy), `SR-USE-12` (house contract), `SR-USE-66` (digital
  signatures), `SR-USE-67` (timestamping / notary), `SR-USE-71` (highly
  trusted keys), `SR-USE-74` (key caching) and `SR-USE-75` (distribution of
  revocations).

**Constructed vectors.** Each one carries these fields:

- `outcome`: one of `accept`, `reject`, `conforms`, `violation`, `permitted`,
  `expressible` or `undetermined`.
- `rests_on`: verbatim rule quotes, each with its locator.
- `modal`: the source's own modal wording.
- `soft: true`: the source qualifies the rule ("if possible", "may imply",
  "usually", "we assume"). A failure of a soft rule is a finding, not a hard
  failure.
- `inferred: true`: the outcome is not literally stated. In that case
  `inference` says what was read in.

RFC 2692 has no BCP 14 keywords. Every "must" and "should" is lower case and
carries its ordinary meaning.

**Requirement links.** `constrained_by` lists the `rfc-2692#R-NNNN` ids each
vector bears on. Pass 3 wired them; the rule is under *Pass 3* below.

## Coverage

| section | source examples | constructed | ids |
|---|---|---|---|
| Charter of the SPKI working group | 1 | 0 | `SR-CH-01` |
| Background | 1 | 0 | `SR-BG-01` |
| General Requirements | 4 | 11 | `SR-GEN-01` … `-04`; `SR-GEN-C01` … `-C11` |
| Validity and CRLs | 4 | 17 | `SR-VAL-01` … `-04`; `SR-VAL-C01` … `-C17` |
| Implementation of Certificates | 4 | 10 | `SR-IMP-01` … `-04`; `SR-IMP-C01` … `-C10` |
| List of Certificate Uses | 75 | 7 | `SR-USE-01` … `-75`; `SR-USE-C01` … `-C07` |
| Open Questions | 6 | 0 | `SR-OQ-01` … `-06` |
| **total** | **95** | **45** | **140** |

### How the 75 List vectors account for the list

The list runs from line 262 to line 587.

- **62 top-level items.** These are every line that begins with six spaces and
  a hyphen.
  - `SR-USE-01` … `-17`: the 14 items from "I need a certificate to give me
    permission" to "..a digital Voter Registration Card?". The count of 17
    ids includes the 3 name-binding sub-items below.
  - `SR-USE-18`: the wallet-card item.
  - `SR-USE-19` … `-51`: the 33-item run after it, from "health insurance
    card" to "permission to issue nuclear launch codes".
  - `SR-USE-52`, `-53`, `-55` … `-57`, `-60`, `-62`, `-63`: the 8 items from
    "I'm a sysadmin" to the rfc822 template.
  - `SR-USE-64` … `-69`: the 6 closing items, from "Encryption keys" to
    "Service authentication".
- **3 sub-items** of "I need certificates to bind names to public keys":
  `SR-USE-08` [traditional certificate], `-09` [direct certificate] and `-10`
  [personal binding].
- **6 sub-items** of "Other requirements": `SR-USE-70` … `-75`.
- **1 indented paragraph** that prints its own example certificate:
  `SR-USE-54`, the audit identity with the "is a system administrator of this
  host" certificate.
- **3 vectors split from bracketed commentary:**
  - `SR-USE-58`, the smart-card login case;
  - `SR-USE-59`, the "delegation-allowed" bit (both from the delegation
    template);
  - `SR-USE-61`, the "I own this address" / "I own this address range"
    certificate.

These add up: 62 + 3 + 6 + 1 + 3 = 75.

**The quoted template sentences** are each their own vector:

- the delegation sentence (`SR-USE-57`);
- the two "I am the current legitimate owner of …" sentences (`SR-USE-60`,
  `-62`);
- "I am the legitimate receiver of mail …" (`SR-USE-63`);
- "not already married" (`SR-OQ-04`).

Bracketed commentary that is not split out is carried verbatim in
`source_annotation_lines`: on `SR-USE-57`, `-60` and `-63`.

### How the 6 Open Questions vectors account for the section

`SR-OQ-01`, `-02`, `-03` and `-06` are the four questions. Each one's
`expected` (`expected_paragraphs` for question 3) is the source's answer,
verbatim. `outcome_quote` gives its decisive clause:

1. Proving you did not send a message signed with your key: "certificate
   format, contents or issuing machinery can not ensure the protection of a
   user's private key …"
2. A house title scan: the database "is a project not related to certificate
   structure."
3. A certificate guaranteeing you are not already married: "The method of
   determining such a negative fact is not part of the certificate
   definition." The same answer says a certificate *can* carry the fact as a
   'positive' attribute.
4. Key loaning: "a potential flaw in any system providing authorization and an
   interesting topic for study."

`SR-OQ-04` and `-05` are the two quoted attributes in answer 3. Every Open
Questions vector carries the section's own framing as `source_text`: "These do
not have answers provided by certificate definition or issuing alone."

### Body illustrations (14)

| id | case |
|---|---|
| `SR-CH-01` | the application list (IPSEC, encrypted mail and WWW documents, payment protocols) |
| `SR-BG-01` | the telephone book with public keys and the digitally signed directory entry |
| `SR-GEN-01` | identifying the keyholder by a hash of the key or by a name |
| `SR-GEN-02` | LDAP, the PGP key server, the DNS |
| `SR-GEN-03` | a single key rather than a key ring, a single credit card rather than a wallet |
| `SR-GEN-04` | secret balloting with a blinded signature key |
| `SR-VAL-01` | the minimal CRL, the source's own counter-example |
| `SR-VAL-02` | the paper books of bad checks (a negative statement) |
| `SR-VAL-03` | on-line validation of a single check, ATM card or credit card (a positive statement) |
| `SR-VAL-04` | the one-use instrument |
| `SR-IMP-01` | developers in garages and dorm rooms |
| `SR-IMP-02` | smart cards and small embedded systems |
| `SR-IMP-03` | C or PASCAL structures |
| `SR-IMP-04` | white-space canonicalization for a text format |

### Constructed vectors

**Validity and CRLs (17):**

- CRL sequences that overlap (`C01`, a violation), sit adjacent (`C02`,
  conforms), or share an endpoint (`C03`, undetermined);
- no CRL location (`C04`) and no CRL validity dates (`C05`);
- a certificate listed in a current CRL (`C06`) or not listed (`C07`);
- a check after (`C08`) or before (`C09`) the validity period;
- a revalidation instrument with lifetime 0 (`C10`) or no lifetime (`C11`);
- a one-use instrument reused (`C12`), used once (`C13`), or delivered
  outside a challenge/response (`C14`);
- support for only negative (`C15`) or only positive (`C16`) on-line
  validation;
- no way to carry a validity period (`C17`).

**General Requirements (11):**

- a new authorization that needs a third party (`C01`) or none (`C02`);
- more information than the job needs (`C03`) and just enough (`C04`);
- no anonymity possible (`C05`) and an anonymous certificate (`C06`);
- an attribute on a blinded key (`C07`);
- the subject given as a key hash (`C08`) or as a name (`C09`);
- both kinds of name binding (`C10`);
- a repository-only design (`C11`, soft).

**Implementation of Certificates (10):**

- a signature check that needs reformatting (`C01`);
- white-space canonicalization (`C02`);
- ASN.1 (`C03`);
- library code required (`C04`);
- a second scan (`C05`, soft), recursion (`C06`, soft), and a single pass
  without recursion (`C07`, soft);
- an empowered keyholder issuing (`C08`) and an authority-only design
  (`C09`);
- a certificate signed exactly as transmitted (`C10`).

**List of Certificate Uses (7).** These rest on brainstorming-list text, so
`rests_on` marks them `body_requirement: false`.

- delegation before expiry (`C01`), after expiry (`C02`), and for an unlisted
  purpose (`C03`);
- an issuer whose certification right has expired issuing a new certificate
  (`C04`, rejected), and that issuer's earlier certificate (`C05`, still
  valid), both soft;
- a purchase within (`C06`) and over (`C07`) the source's "$15,000" limit.

### Inferred constructed vectors (18)

| id | outcome | what was read in |
|---|---|---|
| `SR-VAL-C03` | undetermined | both readings of a shared endpoint are derived |
| `SR-VAL-C06` | reject | "annihilates" a listed certificate is said only of the minimal CRL |
| `SR-VAL-C07` | accept | the source states no acceptance rule; this is the baseline |
| `SR-VAL-C08`, `-C09` | reject | "dates within which it is valid" read as meaning a certificate is invalid outside them |
| `SR-VAL-C10` | violation | "is not possible" is a statement of fact, not a prohibition |
| `SR-VAL-C12` | reject | a one-use lifetime read as rejecting a second use |
| `SR-VAL-C13` | accept | the source allows the instrument ("one can consider") |
| `SR-VAL-C14` | violation | the condition "delivered only as part of a challenge/response protocol" is stated, its consequence is not |
| `SR-GEN-C05`, `-C06` | violation / expressible | "anonymous" is undefined; read as identified by key alone |
| `SR-GEN-C11` | violation (soft) | "we assume" direct distribution, read as a design constraint |
| `SR-USE-C02` | reject | equivalence lasts "until this certificate expires" |
| `SR-USE-C03` | reject | equivalence is "for the following purposes" |
| `SR-USE-C04`, `-C05` | reject / accept (soft) | a stated want ("may imply", "usually"), plus an issue time the source never mentions |
| `SR-USE-C06`, `-C07` | accept / reject | how amounts are compared against "up to $15,000" |

## Sections and rules with no vector, and why

**Front and back matter.** None of these prints an example:

- Status of this Memo, Copyright Notice and the Table of Contents.
- The Abstract. It describes the list but prints none of it.
- References, Author's Address, Full Copyright Statement and Acknowledgement.
- Security Considerations. Its whole text is "Security issues are discussed
  throughout this memo."

**Charter ¶1–¶2 and Background ¶2.** These are scope statements and argument.
Background ¶2 is quoted as rules `BG-2a` … `-2c`, and `SR-BG-01` and
`SR-USE-08` cite it. Charter ¶2's "simple to understand, implement, and use"
(`CH-2`) has no criterion to test.

**General Requirements.** Some paragraphs are definitions or requirements that
print no example:

- ¶1 defines KEYHOLDER and ¶2 states the purpose of a certificate. Both are
  cited by many source vectors.
- ¶4 and ¶7 print no example of their own. They are exercised by constructed
  vectors and by List vectors (`GEN-4a`, `GEN-4b` and `GEN-7` in `exercises`).
- ¶9 (names; SDSI) is exercised by `SR-GEN-C10` and the name-binding items.
  "the SDSI name construct" is named but not shown, and the source does not
  define it, so `GEN-9b` has no constructed vector. The bracketed "[Note: SPKI
  and SDSI have merged.]" is not an example.

**Validity and CRLs ¶1 and ¶4.** These are requirements, exercised by
`SR-VAL-C08`, `-C09` and `-C17`, and by `-C15` and `-C16`. `VAL-1b` (on-line
refinement "may also be necessary") is too open to test on its own;
`SR-VAL-C06` cites it only as support.

**Implementation of Certificates ¶2 and ¶3.** These rules have no threshold or
criterion, so no constructed vector can test them:

- "as simple as possible";
- "a bare minimum of fields";
- "an absolute minimum of optional fields";
- "constrained by the structure definition, not by complaints";
- C or PASCAL structures.

`IMP-1c` ("as small as possible") has no size bound either.

**List of Certificate Uses intro and the "Other requirements:" label.** These
are framing. The label is discussed under defect 2 below.

## Source defects and ambiguities

These are recorded and not repaired. Where a vector meets one, it carries
`source_issue` or a note.

1. **The wallet-card list has no marked end** (`SR-USE-18`). The item that
   introduces the cards ends in a colon. The cards are printed at the
   top-level indent, not as sub-items, and nothing marks where they stop. This
   file takes the 33 noun-phrase items from line 376 to line 457 as the run,
   because the next item returns to the first person. Several of them are not
   cards carried in a wallet: a deed, a stock option, nuclear launch codes.
2. **"Other requirements:" is printed indented under "Service
   authentication"** (line 547, note on `SR-USE-69`). Its six sub-items are
   general requirements, not part of that item.
3. **The rfc822 template has ambiguous quotation marks** (`SR-USE-63`). The
   opening double quote closes only after the bracket (`]."`), and the
   bracket contains the double-quoted "DNS name owner". Read literally, the
   bracketed note is part of the template sentence.
4. **Typos, all kept verbatim:**
   - "singing someone else's key" for "signing" (`SR-USE-10`);
   - "I'm the a purchasing agent" and "posses" (`SR-USE-56`);
   - "owner of a this DNS name" (`SR-USE-62`).
5. **CRL validity endpoints are unspecified** (`SR-VAL-C03`). "dates within
   which it is valid" and "must not overlap" do not say whether an end date is
   inclusive. Two CRLs that meet at one instant therefore cannot be
   classified. The source also does not say what a verifier does when no CRL
   is current (a gap in the sequence; note on `SR-VAL-C02`).
6. **Lifetime 0 is "not possible", not forbidden** (`SR-VAL-C10`). The source
   gives a physical reason ("communication delays and clock skews"), not a
   prohibition.
7. **"anonymous" is undefined** (`SR-GEN-C05`, `-C06`).
8. **LR(0) is glossed in the source's own terms.** The source says "neither
   packing nor parsing of the structure should require a scan of the data".
   `SR-IMP-C05` tests that gloss only.
9. **Direct distribution vs. caching** (`SR-USE-74`). The body assumes
   certificates go "directly by the keyholder to the verifier". The Other
   requirements want keys "cached locally", fetched as from name servers. The
   source does not reconcile the two.
10. **The delegation commentary spans a page break** (`SR-USE-57`). The
    bracket after the delegation template runs from page 9 (line 497) to page
    10 (line 511). The layout cannot show whether a paragraph break also falls
    there, so the two runs are carried separately and never joined.
11. **The list is not at the end.** The Abstract says the list is "attached at
    the end of this document", and Implementation ¶1 calls it "the list given
    at the end of this document". In fact the Open Questions, References and
    Security Considerations follow it. This is minor and not an example; it is
    passed on for the normative pass.

**Page breaks inside quoted text:**

- `SR-IMP-02` (page 4 / page 5) and `SR-USE-10` (page 6 / page 7) carry
  `crosses_page_break: true`.
- So do rules `GEN-9b` (page 3 / page 4) and `IMP-1b` (page 4 / page 5).
- `SR-USE-57`'s annotation is split at its page break (defect 10).
- No other quote crosses a page break.
- The only line-final hyphen joined inside a quote is "collision-" + "free"
  (`GEN-3`, `SR-GEN-01`).

**Checked mechanically:** the file parses as YAML. All 225 verbatim strings
are contiguous runs of the source under the quoting rule. That covers inputs,
annotations, stated answers, outcome quotes, `source_text`, `body_rules` and
`rests_on`. No quote spans a paragraph break. Every `related` id and every
`exercises` key resolves.

## Pass 3: cross-check

Run on 2026-10-18 by scripts kept outside the repository, against the
schema, `requirements.yaml`, `messages.yaml` and `state-machine.yaml` as they
stood at the end of the pass.

### Requirement links

Every vector now has `constrained_by`: 323 links to 153 of the 158
requirement ids, and every id resolves in `requirements.yaml`. A vector cites
two kinds of entry, and no others:

- **Its own text.** These are the entries whose text the vector itself
  carries, in `input`, `source_annotation_lines`, a `stated` `expected`,
  `outcome_quote` or `source_text`. So each List vector cites its own item's
  entries (R-0050 to R-0150). Each Open Questions vector cites R-0151 and its
  answer's entries (R-0152 to R-0158).
- **Its rules.** These are the entries for every key in `exercises` or
  `rests_on`. A `rests_on` quote narrower than its `body_rules` entry cites
  only the entries it quotes. `SR-VAL-C01` quotes only "the dates of a
  sequence of CRLs must not overlap.", so it cites R-0027 and not R-0025 or
  R-0026.

`body_rules` now carry `requirement_ids`, the same match made once per rule.
Three rules have none, because `requirements.yaml` leaves them out on purpose:
`BG-2a` and `BG-2b` (Background's argument) and `VAL-2a` (the description of
the minimal CRL that the section rules out). So `SR-BG-01`, `SR-USE-08` and
`SR-VAL-C06` cite only their other rules. It matters for `SR-VAL-C06`: its
`reject` rests on `VAL-2a`, the only sentence that says what being listed in a
CRL does to a certificate.

Five ids are cited by no vector: R-0001 (the charter's deliverables), R-0002
(`CH-2`), R-0038 and R-0039 (`IMP-2b`), and R-0040 (`IMP-2c`). The last four
have no criterion to test, as above.

### Schema check

Every vector that carries or implies a structured instance was rendered as
JSON. Each instance was validated against
`schema/spki-requirements.derived.schema.json` with `jsonschema` 4.10.3
(Draft 2020-12), by reference to one `$defs` entry. The rendering rule is in
`vectors.yaml` under `schema_check.rendering`. In short:

- a key label becomes `{public-key: …}`;
- a grant becomes an authorization attribute;
- `uses_crl` becomes a CRL pointer;
- a signature label is added.

Members the schema has no place for are left out, each for a reason given
there. They are `id`, `subject_form`, `resolves_to` and `issued`, and a CRL's
`signer` and `location`.

- **135 instances over 101 vectors**: 72 source, 29 constructed.
- **127 must validate, and 123 do.** The other 4 are schema finding 1, below.
- **8 must not validate, and none does.** Each is rejected for its stated
  reason.
- **39 vectors have no instance.** They are listed, with reasons, in
  `schema_check.without_instance`. None was forced.

| entry | vectors | result |
|---|---|---|
| `certificate` | SR-BG-01; SR-GEN-01, -03, -04; SR-USE-01 … -05, -07, -13 … -55, -59 … -64; SR-OQ-03 … -05; SR-VAL-C01 … -C09; SR-GEN-C03, -C04, -C06 … -C10; SR-IMP-C08; SR-USE-C04 … -C07 | valid. SR-VAL-C04's certificate is rejected, as it must be: its CRL pointer has no location |
| `crl` | SR-VAL-01, -02; SR-VAL-C01 … -C03, -C05 … -C07 | valid. Two are rejected because `validity` is required: SR-VAL-01's minimal CRL and SR-VAL-C05's CRL |
| `revalidation-instrument` | SR-VAL-03, -04; SR-VAL-C10 … -C14 | valid. SR-VAL-C11 (no lifetime) is rejected |
| `instrument-lifetime` | SR-VAL-04 | valid (`one-use`) |
| `blinded-signature-key` | SR-GEN-04, SR-GEN-C07 | valid |
| `traditional-certificate` | SR-USE-08 | valid |
| `direct-certificate` | SR-USE-09 (subject the key, and its hash); SR-GEN-C10 (`cert-n1`) | valid. A probe with two names is rejected |
| `personal-binding-certificate` | SR-USE-10; SR-GEN-C10 (`cert-n2`) | valid |
| `anonymous-certificate` | SR-USE-56; SR-GEN-C06; SR-USE-C06, -C07 | valid. Two probes that carry a name are rejected: SR-USE-56 with the agent's name, and SR-GEN-C03's certificate |
| `key-equivalence-certificate` | SR-USE-57, -58; SR-USE-C01 … -C03 | valid, including SR-USE-57 and SR-USE-C01 … -C03 as written with an expiry alone (schema finding 1, applied). A probe with no validity is rejected |

The List uses validate trivially. `authorization` is opaque (G-01), so the
check shows only that the certificate shape carries each use.

### What decides a negative outcome

28 constructed vectors have outcome `reject`, `violation` or `undetermined`.
`schema_check.decided_by` names what decides each one:

- **The schema (3).** SR-VAL-C04 fails because `crl-pointer` requires a
  location; with the pointer left out, only RC-05 catches it. SR-VAL-C05
  fails because `crl` requires `validity`, and SR-VAL-C11 because a
  revalidation instrument requires `lifetime`. The source's own
  counter-example, SR-VAL-01, fails like SR-VAL-C05.
- **A NOT-EXPRESSIBLE constraint (13).** These are:
  - RC-03: SR-VAL-C01, and SR-VAL-C03 with G-08;
  - RC-02: SR-VAL-C10;
  - RC-07: SR-VAL-C12, -C14;
  - RC-14: SR-GEN-C01;
  - RC-13: SR-GEN-C03;
  - RC-08: SR-IMP-C01;
  - RC-11: SR-IMP-C03, -C04;
  - RC-09: SR-IMP-C05;
  - RC-10: SR-IMP-C06;
  - RC-21: SR-IMP-C09.

  RC-02 and RC-03 have a `check`, and both were run in code. Each gives the
  vector's outcome. On SR-VAL-C03 RC-03's check now returns undetermined, as
  the source leaves the shared endpoint open (schema finding 2, applied).
- **The derived schema, read as the design under test (5).** These are
  SR-VAL-C15, -C16, -C17 and SR-GEN-C05, -C11. The schema passes each one. It
  has a negative and a positive instrument and a validity member. It requires
  no name and has no repository member.
- **None of these (7).** These are:
  - SR-VAL-C06: listed in the current CRL;
  - SR-VAL-C08 and -C09: the check time is outside the validity period;
  - SR-USE-C02: used after expiry;
  - SR-USE-C03 and -C07: purpose and amount, which are authorization content
    under RC-14;
  - SR-USE-C04: gap G-14 (soft).

  Every instance in these vectors is schema-valid. The decision is the
  verifier's at check time, and it lives in `state-machine.yaml` (M02, M03,
  M11, M14), not in the schema. `NOT-EXPRESSIBLE` now says so (schema
  finding 4, applied).

### Schema findings, applied in pass 3

The examples check found these four; each was then applied to the schema as
proposed (finding 4 by the second option), and the vectors re-validated.

1. **`validity-period` requires `not-before`, but the source's delegation
   template has only an expiry.** The template's "until this certificate
   expires" (item 53, p. 9) is the only validity the source gives this
   certificate. `key-equivalence-certificate` requires `validity` because of
   it. But `validity-period` requires both bounds, which the schema marks as
   its own inference. So SR-USE-57 and SR-USE-C01 … -C03 fail as written.
   Proposed fix:
   - let `validity-period` carry either bound alone (`minProperties: 1`);
   - keep both bounds where an instrument needs them: `crl.validity`, and the
     period branch of `instrument-lifetime`, for RC-02 and RC-03;
   - require `not-after` in `key-equivalence-certificate`;
   - make RC-01's check skip a missing bound.
2. **RC-03's check decides gap G-08.** The check uses `date_le`, so two CRLs
   that share an endpoint pass. The rule text and G-08 say the source leaves
   that case open. SR-VAL-C03 (`undetermined`) is that case. Proposed fix:
   either the check returns undetermined when one CRL's `not-after` equals the
   next CRL's `not-before`, or it says that it takes the exclusive-end reading.
3. **`same_key` does not treat a key and its hash as the same key.** A direct
   certificate identifies its key "from the key itself or a cryptographic hash
   of the key" (R-0061). Take the key as issuer and its hash as subject: RC-17's
   `same_key(c.issuer, c.subject)` is then false, and a self-signed direct
   certificate fails RC-17. RC-18 and RC-19 have the converse problem. Proposed
   fix: `same_key` compares the keys the identifiers denote, hashing where one
   side is a hash.
4. **No constraint covers a verifier's decision at check time.** The 7
   vectors above are rejected by no schema keyword and no RC. Proposed: either
   add two inferred constraints, or say in `NOT-EXPRESSIBLE` that these
   decisions belong to `state-machine.yaml`. The two constraints would be:
   - a certificate is accepted only within its validity period (VAL-1a;
     SR-VAL-C08, -C09, SR-USE-C02);
   - a certificate listed by the current CRL it names is not accepted
     (VAL-2a; SR-VAL-C06).

### Outcomes against their rules

Each of the 45 constructed vectors was read against the rules it cites. None
is stronger than its rule:

- `modal` keeps the source's word, so a `should` rule stays `should`;
- every qualified rule carries `soft: true`;
- every outcome the source does not state carries `inferred: true` (the 18
  above).

One source vector was stronger than its rule, and is fixed. `SR-GEN-03`'s
`expected` said "One certificate carries one authorization". The source says
each certificate "should carry the minimum information necessary to get a job
done" and sets no number (schema gap G-09). `expected` now says so.

### Structures in `messages.yaml`

Every structure a vector names exists in `messages.yaml`:

- `spki-certificate`, with its fields, and `keyholder-identifier`;
- `crl`, `crl-sequence`, `revalidation-instrument`, `one-use-instrument` and
  `one-use-challenge`;
- `name-binding-certificate`, `direct-certificate` and
  `personal-binding-certificate`;
- `delegation-certificate`, `certification-right-expiration-certificate` and
  `purchasing-authority-certificate`;
- `certificate-encoding-profile`, `certificate-presentation` and
  `repository-publication`.

One abstract member has no field: a certificate's issue time (`issued`, in
SR-USE-C04 and -C05). The source never mentions one, as both vectors'
`inference` says. State machine M14 needs it (`checking-issuance-time`), and
the nearest field is `certification-right-expiration-certificate`'s
`notary-timestamp`.

### Also checked

- PyYAML and `bin/_yaml.py` give the same tree, except for four `null`
  scalars. `_yaml.py` reads those as the string `null`, as it did before this
  pass.
- `vector_count`, `source_vector_count`, `constructed_vector_count` and every
  tally in this README match the file.
- `examples/` has no unfinished-work marker.

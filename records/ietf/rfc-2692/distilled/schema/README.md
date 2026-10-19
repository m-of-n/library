---
record: rfc-2692
kind: schema
title: "rfc-2692 — schemas"
extracted: "2026-10-18"
reviewed_by: ""
---

# RFC 2692 — schemas

## No verbatim schema exists

**RFC 2692 contains no ASN.1, no ABNF, no CDDL, no JSON Schema and no grammar
of any kind**, and unlike RFC 2693 it does not print even an informal template
or an encoded example. There is nothing to copy, so this directory has no
verbatim file. That is a property of the document, for two reasons it states
itself:

- It is a list of requirements, not a format. The Abstract describes the
  working group as *"tasked with producing a certificate structure and
  operating procedure"* and the document as presenting *"that summary of
  requirements"* (§Abstract ¶1–¶2, p.1). The structure was the working group's
  later output, not this memo's content.
- It rules the usual notation out: *"No library code should be required for
  the packing or parsing of SPKI certificates.  In particular, ASN.1 is not to
  be used."* (§Implementation of Certificates ¶4, p.5).

So the one schema here is **derived**: the library's rendering, as JSON Schema
2020-12, of what RFC 2692 says a certificate and its validity instruments must
or should be able to carry. Nothing in it may be quoted as RFC 2692's own
schema. Every member name is the library's; the source names no fields. The
one exception is `delegation-allowed`, which echoes a phrase the source puts
in quotation marks.

## Where the concrete encodings live (pointers only)

None of the following is imported here.

- **RFC 2693**, SPKI Certificate Theory: the 5-tuple, the name 4-tuple,
  validity and the on-line tests (record `rfc-2693`).
- **draft-ietf-spki-cert-structure**: the concrete certificate structure
  (record `draft-ietf-spki-cert-structure`).
- **RFC 9804**: the S-expression encoding (record `rfc-9804`).

RFC 2692 itself points at none of these. It mentions only the SDSI name
construct, in a sentence split by a page break: *"if possible SPKI should
support the SDSI"* (§General Requirements ¶9, p.3) / *"name construct.  [Note:
SPKI and SDSI have merged.]"* (§General Requirements ¶9, p.4).

## Files

| file | kind | covers |
|---|---|---|
| `README.md` | prose | this file |
| `spki-requirements.derived.schema.json` | **derived** | JSON Schema 2020-12, 33 `$defs`: certificate (root), CRL, revalidation instrument, five certificate profiles, the identifiers, attributes, validity and pointers they use, and a findings entry `NOT-EXPRESSIBLE` (21 constraints, 15 gaps). It draws on General Requirements, Validity and CRLs, Implementation of Certificates, List of Certificate Uses, Abstract and Background. |

**Why one file rather than several.** The certificate, the CRL and the
revalidation instrument share their leaves (`date`, `signature`,
`certificate-identifier`) and `validity-period`. Split into separate files,
each would need cross-file `$ref`s to a fourth file for those shared leaves,
and the findings would have to be split or repeated. One file with several
roots keeps every reference local, and the README carries the index.

## Using the schema

**Roots.** The schema root is `certificate`. Validate anything else by
reference, e.g. `{"$ref": "spki-requirements.derived.schema.json#/$defs/crl"}`.
Nothing else references these entries, and they are meant as roots:

- the instruments: `crl`, `revalidation-instrument`;
- the profiles: `traditional-certificate`, `direct-certificate`,
  `personal-binding-certificate`, `anonymous-certificate`,
  `key-equivalence-certificate`;
- `blinded-signature-key`, a documentary alias of `public-key` (see G-03);
- `NOT-EXPRESSIBLE`, which holds findings and is not a schema (`"not": {}`).

**Open and closed.** `certificate` is **closed**
(`additionalProperties: false`). The source asks that *"the structure should be
specific enough that the creator of a certificate is constrained by the
structure definition"* and for *"an absolute minimum of optional fields"*
(§Implementation of Certificates ¶2, p.5). Extensibility lives inside the
opaque `authorization`, which is where the source puts it: *"The definition of
attributes or authorizations in a certificate is up to the author of code which
uses the certificate."* (§General Requirements ¶4, p.3). `crl` and
`revalidation-instrument` are **open**, because the source describes only a
*"minimal CRL"* and gives the positive instrument no contents at all. The
objects the library made up to hold a leaf (the three `subject-*` wrappers,
`name-attribute`, `authorization-attribute`, `validity-period` and the two
pointers) are closed too. The source says nothing about their shape at all, so
that closure is the library's, and it is not flagged `x-inferred`
separately.

**Opaque leaves.** The source names a public key, a key hash, a name, a date, a
signature, a location, a certificate identifier and an authorization, and gives
none of them a form. Those eight entries accept any JSON value. The only
non-opaque leaf entries are `sequence-number` (integer; inferred) and the
`one-use` token. Among properties, `delegation-allowed` is a boolean and the
two `kind` members are constants. `revalidation-instrument.challenge` is
opaque too.

**Traceability.** Every `$defs` entry except `NOT-EXPRESSIBLE`, and every
property (26), carries the following. `NOT-EXPRESSIBLE` has `x-status` and a
`description`, and each of its items carries its own `basis`, `status` and
`constrained_by`.

- `x-status`: `derived` (encodes a stated requirement; 24 entries plus the
  findings entry, and 25 properties), `opaque` (named, no form given; 8
  entries), or `tentative` (floated by the source with *"Maybe"*; one
  property, `delegation-allowed`);
- `x-inferred` (boolean), and `x-inferred-reason` whenever anything in the
  node is not literally stated. Such a node's `description` also begins
  `INFERRED`. There are 11 inferred entries and 14 inferred properties, listed
  below;
- `x-quotes`: locator, source line range and verbatim text;
- `description`: the prose followed by `SOURCE:` and the same quotes.

Quotes follow these rules. Each is one contiguous run of source characters,
with RFC line wrapping undone: a line break and the next line's indent become
one space, and `collision-` + `free` joins with no space. In-line double spaces
after a full stop are kept. **No quote crosses a page break.** Three quoted
sentences do, and each is quoted in two parts: the SDSI sentence (p.3 → p.4),
the Implementation of Certificates ¶1 *"such as smart cards or small"* /
*"embedded systems."* sentence (p.4 → p.5), and the personal-binding *"my own
private"* / *"directory of keys."* sentence (p.6 → p.7). Locators name the section by its title, since RFC 2692's sections
are unnumbered, then the paragraph or list item, then the page.

**`constrained_by` is wired (pass 3).** Each `NOT-EXPRESSIBLE` item lists the
`rfc-2692#R-NNNN` requirements it renders or bears on: 64 links to 47 distinct
requirements, every one resolving in `requirements.yaml`. The matching rule is
the one `messages.yaml` uses: first the requirements whose text the item's
`basis` quotes, then the requirement whose object the item is about. Two items
have none, and say why in `constrained_by_reason`: RC-04 and G-10, whose only
basis is the minimal-CRL sentence (*"A minimal CRL contains a list of revoked
certificates, identified uniquely, a sequence number and a signature."*,
§Validity and CRLs ¶2, p.4), which `requirements.yaml` excludes as describing
the design the section rules out. Schema members carry no `constrained_by`.
Their requirement ids are on the matching `messages.yaml` fields (see
*Correspondence with messages.yaml* below).

## Index of `$defs`

Sections: GR = General Requirements, VC = Validity and CRLs, IC =
Implementation of Certificates, Uses = List of Certificate Uses, Abs =
Abstract, Bg = Background.

| entry | status | inferred | form | sections |
|---|---|---|---|---|
| `public-key` | opaque | | any | GR |
| `blinded-signature-key` | derived | yes | = `public-key` | GR |
| `public-key-hash` | opaque | | any | GR, Uses |
| `name` | opaque | | any | GR |
| `date` | opaque | | any | VC |
| `signature` | opaque | | any | VC, IC |
| `location` | opaque | | any | VC |
| `certificate-identifier` | opaque | | any | VC |
| `authorization` | opaque | | any; no enumeration, by design | GR, Uses |
| `sequence-number` | derived | yes | integer | VC |
| `subject-public-key` | derived | | `{public-key}` | GR |
| `subject-public-key-hash` | derived | | `{public-key-hash}` | GR |
| `subject-name` | derived | | `{name}` | GR |
| `key-identifier` | derived | | key or key hash | Uses |
| `keyholder-identifier` | derived | | key, key hash or name | GR |
| `name-attribute` | derived | | `{name}` | GR |
| `authorization-attribute` | derived | | `{authorization}` | GR |
| `attribute` | derived | yes | name or authorization | GR, Uses |
| `validity-period` | derived | (members) | `{not-before, not-after}`, closed | VC, Uses |
| `one-use` | derived | | `"one-use"` | VC |
| `instrument-lifetime` | derived | | validity-period or `"one-use"` | VC |
| `crl-pointer` | derived | (kind) | `{kind: "crl", location}` | VC |
| `revalidation-pointer` | derived | yes | `{kind: "revalidation", location?}` | VC |
| `online-validation-pointer` | derived | yes | either pointer | VC |
| `certificate` | derived | yes | `{issuer, subject, attributes[1..], validity?, delegation-allowed?, online-validation?, signature}`, closed; **root** | GR, VC, IC, Uses, Abs, Bg |
| `crl` | derived | (revoked) | `{revoked[], sequence-number, validity, signature}`, open | VC |
| `revalidation-instrument` | derived | yes | `{validates, lifetime, challenge?, signature}`, open | VC |
| `traditional-certificate` | derived | yes | certificate; subject key/hash; exactly one name | Uses |
| `direct-certificate` | derived | | certificate; subject key/hash; exactly one name | Uses |
| `personal-binding-certificate` | derived | yes | certificate; subject key/hash; exactly one name | Uses |
| `anonymous-certificate` | derived | yes | certificate; subject key/hash; no name attribute | GR, Uses |
| `key-equivalence-certificate` | derived | yes | certificate; subject key/hash; authorizations only; validity required | Uses |
| `NOT-EXPRESSIBLE` | derived | | findings; matches nothing | all |

## Everything marked inferred

Entries (`x-inferred: true`):

- `blinded-signature-key`: that a blinded key fills the ordinary key slot,
  unmarked.
- `sequence-number`: `integer`; the direction of the order is unstated.
- `attribute`: the partition into name or authorization.
- `revalidation-pointer`: the whole pointer, by analogy with the CRL pointer.
- `online-validation-pointer`: that the source's "negative on-line validation"
  is the CRL.
- `certificate`: the member set is assembled from separate requirements, and
  the object is closed.
- `revalidation-instrument`: that a dated instrument carries no challenge.
- `traditional-certificate`: a key subject and exactly one name.
- `personal-binding-certificate`: hash admitted as subject, and exactly one
  name.
- `anonymous-certificate`: "anonymous" read as "carries no name".
- `key-equivalence-certificate`: purposes as authorizations, and `not-after` required for "until this certificate expires".

Properties:

- `validity-period.not-before` and `.not-after`: either bound may stand alone on a certificate (minProperties 1, relaxed in pass 3); `crl.validity` and a dated `instrument-lifetime` require both.
- `crl-pointer.kind` and `revalidation-pointer.kind`: the discriminator.
- `revalidation-pointer.location`.
- `certificate.issuer`: the source never says the certificate names its
  signer.
- `certificate.attributes`: minItems 1.
- `certificate.online-validation`: grouping, and more than one pointer.
- `certificate.signature`: modelled as a member rather than a wrapper.
- `crl.revoked`: the empty list is admitted.
- `crl.validity`: "explicit validity dates" read as both bounds (pass 3).
- `revalidation-instrument.validates`, `.challenge` and `.signature`.

Findings: RC-01 (certificate date order) is inferred, along with the inferred
parts of RC-02 (the strict order), RC-05 (an unnamed CRL has no effect) and
RC-19 (issuer and subject differ).

## What no schema here can carry

JSON Schema 2020-12 cannot compare two members of one instance. It cannot see
two instances, the wire bytes, or who holds a certificate. Each rule below is
in `$defs/NOT-EXPRESSIBLE.x-constraints` with its verbatim basis, and with a
pseudo-code `check` where one can be written.

**A green result does not mean the data meets RFC 2692.** In particular, a
validity period whose not-before is later than its not-after, and a CRL whose
dates overlap its predecessor's, both validate. That was checked.

| id | applies to | rule | basis | constrained_by (R-) |
|---|---|---|---|---|
| RC-01 | `certificate` | not-before ≤ not-after | inferred, VC ¶1 | 0022 |
| RC-02 | `crl`, `revalidation-instrument` | dated lifetime is non-zero, i.e. not-before < not-after (strict order inferred) | stated, VC ¶5 | 0031, 0032 |
| RC-03 | `crl` | the dates of a sequence of CRLs do not overlap: a cross-instance rule | stated, VC ¶2 | 0027, 0028 |
| RC-04 | `crl` | each listed identifier identifies exactly one certificate | stated, VC ¶2 | none (reason given) |
| RC-05 | `certificate`, `crl` | a certificate that uses a CRL says where to find it (half-expressed: `location` is required in a `crl-pointer`) | stated, VC ¶2; converse inferred | 0024, 0025, 0028 |
| RC-06 | `crl` | explicit validity dates: expressed (`validity` required); listed for visibility | stated, VC ¶2 | 0026 |
| RC-07 | `revalidation-instrument` | a one-use instrument is delivered only inside challenge/response | stated, VC ¶5 | 0032 |
| RC-08 | `certificate` | signed exactly as transmitted; no reformatting to check; white space may be canonicalised for text | stated, IC ¶5 | 0044, 0045 |
| RC-09 | `certificate` | LR(0) encoding if possible; no scan; bytes touched once | stated, IC ¶6 | 0046, 0047, 0048 |
| RC-10 | `certificate` | packed and parsed without recursion if possible (this schema has no `$ref` cycle) | stated, IC ¶7 | 0049 |
| RC-11 | `certificate` | no library code to pack or parse; no ASN.1 | stated, IC ¶4 | 0042, 0043 |
| RC-12 | `certificate` | simple, C/PASCAL-like structures; small code and memory | stated, IC ¶1–¶3 | 0035, 0036, 0037, 0041 |
| RC-13 | `certificate` | minimum information per certificate; minimum release by the keyholder | stated, GR ¶6 | 0014, 0015, 0016 |
| RC-14 | `authorization` | defined by the code author; creating one needs no other party | stated, GR ¶4 | 0010, 0011 |
| RC-15 | `public-key-hash` | the hash is collision-free | stated, GR ¶3 | 0009 |
| RC-16 | `subject-name` | a subject name is later resolved into a key | stated, GR ¶3 | 0009 |
| RC-17 | `direct-certificate` | self-signed: issuer and subject are the same key | stated, Uses | 0062 |
| RC-18 | `personal-binding-certificate` | issuer and subject differ; never given out | stated, Uses | 0066, 0067 |
| RC-19 | `traditional-certificate` | trustworthy issuer; unique person name; third-party issuer (inferred) | stated, Uses | 0058 |
| RC-20 | `certificate` | can assign an attribute to a blinded signature key (a capability; nothing to check) | stated, GR ¶8 | 0018 |
| RC-21 | `certificate` | generated by a keyholder empowered to grant or delegate (needs a chain) | stated, IC ¶1 | 0033, 0052, 0130 |

## Gaps: where the source is silent and a schema needs an answer

In `$defs/NOT-EXPRESSIBLE.x-gaps`, each with its basis and, in brackets, its
`constrained_by`:

- **G-01** the concrete form of every leaf (key, hash, name, date, signature,
  location, identifier, authorization) [R-0001, R-0043];
- **G-02** whether `delegation-allowed` exists at all, and what its absence
  means [R-0125];
- **G-03** whether a blinded signature key is marked or differs in form
  [R-0018];
- **G-04** whether a certificate must point to its positive validation
  [R-0025, R-0030];
- **G-05** what a positive revalidation instrument contains, and who signs it
  [R-0030, R-0031];
- **G-06** which way sequence numbers run, and what they do once CRL dates may
  not overlap [R-0024];
- **G-07** whether a one-use instrument carries its challenge [R-0032];
- **G-08** whether CRLs that share only an endpoint overlap [R-0027];
- **G-09** how many attributes one certificate may carry [R-0014, R-0015,
  R-0074];
- **G-10** whether an empty CRL is valid [none; reason given];
- **G-11** who signs a CRL, what makes CRLs "a sequence", and how a CRL is tied
  to its certificates [R-0025, R-0026, R-0027];
- **G-12** whether a certificate states its kind (the three name-binding kinds
  share one shape) [R-0056];
- **G-13** certificates whose subject is an object, not a keyholder (the
  software and genealogy items) [R-0007, R-0055, R-0070, R-0071];
- **G-14** the content of a "certification right expiration" certificate
  [R-0143, R-0144, R-0145];
- **G-15** how a certificate's validity combines with an on-line instrument's
  lifetime [R-0023, R-0031].

## Correspondence with messages.yaml

Checked member by member in pass 3. The two files use different names for the
same things, because the schema is shaped for validation and `messages.yaml`
for the source's prose. `messages.yaml` records `required: unspecified` where
the source is silent. The schema cannot say "unspecified", so it renders that
as optional unless its `x-inferred-reason` gives a reason to require the
member. Four places do that, marked **differs** below. Each is recorded on both
sides (`x-inferred-reason` here, `required_reason` there), so neither file
silently disagrees with the other. In the `messages.yaml` column, the word
after the colon is the field's `required` value (`true`, `false` or
`unspecified`).

| schema | messages.yaml | agreement |
|---|---|---|
| `certificate` | `spki-certificate` | entry |
| `certificate.issuer`: required; key or key hash | `spki-certificate.issuer`: unspecified; any keyholder | **differs.** The source is silent. The schema requires a key to check the signature with, and excludes a name issuer |
| `certificate.subject`: required | `spki-certificate.subject`: true | agree |
| `keyholder-identifier`: `subject-public-key`, `subject-public-key-hash`, `subject-name`; `blinded-signature-key` is an alias of `public-key` | `keyholder-identifier` variants `public-key`, `key-hash`, `name`, `blinded-signature-key` | agree. The schema does not mark a blinded key (G-03) |
| `certificate.attributes`: required, 1 or more `attribute` (name or authorization) | `spki-certificate.authorization-or-attribute`: true | agree on presence. The schema admits several (G-09) |
| `certificate.validity`: optional | `spki-certificate.validity-period`: false | agree |
| `certificate.online-validation[]` → `crl-pointer.location`: required within the pointer | `spki-certificate.crl-location`: true, when the certificate uses a CRL | agree. The condition is RC-05 |
| `certificate.online-validation[]` → `revalidation-pointer.location`: optional, inferred | `spki-certificate.revalidation-location`: unspecified, inferred | agree. Pass 3 added the `messages.yaml` field |
| `crl-pointer.kind`, `revalidation-pointer.kind` | none | schema-only discriminators (inferred) |
| `certificate.delegation-allowed`: optional boolean, tentative | `spki-certificate.delegation-allowed`, `delegation-certificate.delegation-allowed`: false, boolean | agree |
| `certificate.signature`: required | `spki-certificate.signature`: true | agree |
| RC-13; profile `anonymous-certificate` | `spki-certificate.minimum-information`, `.anonymity` (constraints) | agree |
| RC-08 to RC-12 | the 13 constraints of `certificate-encoding-profile` | agree |
| `name-attribute` and the three name profiles | `name-binding-certificate.key`, `.name`, `.issuer` | agree |
| none: SDSI stays inside opaque `name` (G-01) | `name-binding-certificate.name-space`: false, inferred | schema-only omission, deliberate (*Deliberately not modelled*) |
| `crl.revoked`: required, may be empty (G-10) | `crl.revoked-certificates`: true | agree |
| `crl.sequence-number`: required, integer (inferred) | `crl.sequence-number`: true; representation not stated | agree. The integer type is the schema's |
| `crl.validity`: required | `crl.validity-dates`: true, in variant `spki` | agree. The schema renders the `spki` variant only. `minimal` is rejected by the source (R-0024) |
| `crl.signature`: required | `crl.signature`: true | agree |
| RC-03 | `crl-sequence.non-overlap` | agree (cross-instance) |
| `revalidation-instrument.validates`: required, inferred | `revalidation-instrument.validated-certificate`: unspecified, inferred | **differs** (G-05) |
| `revalidation-instrument.lifetime`: required, a period or `"one-use"` | `revalidation-instrument.lifetime`; `one-use-instrument.lifetime` | agree. The schema folds `one-use-instrument` into a lifetime value |
| `revalidation-instrument.challenge`: optional, rejected with a dated lifetime | `one-use-instrument.challenge-binding`: unspecified, inferred | agree (G-07) |
| `revalidation-instrument.signature`: required, inferred | `revalidation-instrument.signature`: unspecified, inferred | **differs** (G-05) |
| RC-07 | `one-use-instrument.delivery` | agree |
| `traditional-certificate`, `direct-certificate`, `personal-binding-certificate` | entries of the same names | agree. RC-17 is direct `.issuer`, RC-18 is personal `.distribution`, and personal `.no-binding-evidence` (added in pass 3, R-0068) is enforced by the closed certificate holding exactly one name |
| `key-equivalence-certificate`: `validity` required | `delegation-certificate` (alias `key-equivalence-certificate`): `expiry` unspecified | **differs.** The schema reads *"until this certificate expires"* as requiring the period |

The remaining `messages.yaml` entries have no schema counterpart, by design:
the exchanges (`certificate-presentation`, `repository-publication`), local
state (`trusted-root-set`, `local-key-cache`), `crl-sequence` as a series,
`key-revocation`, the historical and open-question entries, and the use-case
entries, whose content is `authorization` (see *Deliberately not modelled*).

## Deliberately not modelled

- **A certificate-kind field.** The source names three name-binding kinds but
  no marker. They are profiles validated by reference, not a discriminator
  (G-12).
- **Audit identity as a certificate member.** The source puts it inside the
  application: *"the audit identity should be in the domain of the particular
  application..."* (§List of Certificate Uses, sysadmin item, p.9). It belongs
  inside `authorization`.
- **Spending limits, root access, clearances, wallet cards, licences, deeds
  and the rest of the use list.** These are authorization content, defined by
  the code author (GR ¶4). An enumeration would contradict *"The creation of
  new authorizations should not require interaction with any other person or
  organization"* (§General Requirements ¶4, p.3).
- **The "certification right expiration" certificate.** The source says only
  *"This may imply a "certification right expiration" certificate requirement,
  probably to be implemented together with notary services."* (§List of
  Certificate Uses, Other requirements, p.11). Every field would be invented
  (G-14).
- **Object subjects** (downloaded software, a genealogist's signed fact). They
  conflict with *"to or for a keyholder"* (GR ¶2) and are recorded as G-13,
  not admitted.
- **Certificate chains and empowerment.** The bank chain (*"follow a
  certificate chain from a key I know (my bank's) to the key of any other
  bank"*) and the e-mail item's DNS-owner certification relate several
  certificates. That is verification over a set, not the shape of one (RC-21).
  It belongs to the protocol and state-machine artifacts.
- **Distribution, caching and revocation spread.** *"we assume that
  certificates will be distributed directly by the keyholder to the verifier"*
  (GR ¶5), *"Keys will need to be cached locally to avoid long delays fetching
  frequently used keys."* and *"will have spread everywhere in 24 hours"* (Other
  requirements, p.11) are operational, not structural.
- **The trust model.** *"Trust model must be a web (people want to choose whom
  they trust)."* (Other requirements, p.10) is verifier policy.
- **Negative facts.** *"The method of determining such a negative fact is not
  part of the certificate definition."* (§Open Questions, p.12). The
  "positive" attribute it may communicate is ordinary authorization content.
- **Private-key protection and non-repudiation.** *"certificate format,
  contents or issuing machinery can not ensure the protection of a user's
  private key or prove whether or not a private key has been stolen or
  misused."* (§Open Questions, p.11).
- **The annihilating CRL behaviour.** *"If it encounters some certificate that
  it lists, then it annihilates that certificate."* describes the CRL the
  requirement is meant to cure (*"Such a CRL leads to non-deterministic program
  behavior."*). It appears only as the basis of RC-05 and G-06.
- **The SDSI name construct and any key, hash or signature form.** These are
  defined elsewhere (pointers above) and stay opaque here.
- **A separate CDDL rendering.** One derived language is one thing to keep
  true. JSON Schema was chosen because it can be validated here; the source
  favours neither.

## How this was checked

The checks ran by script in this session's scratchpad. The script is not part
of the record, and pass 2 should re-derive the checks rather than trust them.

1. **Quotes.** All 86 distinct quotes (200 uses across `x-quotes` and finding
   bases) were checked against `.cache/rfc-2692.txt` (sha256 `6a88c156…826976d`).
   Each was checked to be:
   - a substring of its cited lines after unwrapping;
   - on a tight line range (dropping either end line loses it);
   - within one page, with no footer, header or form feed in range;
   - under the right section title, paragraph number (for the prose sections)
     and page in its locator.

   Source fragments in single quotes inside descriptions and reasons were
   checked to be in the source too. That check caught two quotes elided with
   "..." and they were rewritten as full runs. The checker was itself tested
   by injecting seven faults, and it caught all seven: a changed word, a splice
   of two non-adjacent passages, a quote across a page break, a widened range,
   a wrong page, a wrong paragraph and a wrong section.
2. **Schema validity.** With `jsonschema` 4.10.3,
   `Draft202012Validator.check_schema` passes, and `iter_errors` against the
   2020-12 metaschema reports **0 errors**. A duplicate-key detector found
   none, and the file parses with `json.load`.
3. **References.** Every `$ref` is local and defined, and every finding's
   `applies-to` names a defined entry. **No `$ref` cycle**, so the schema is
   non-recursive, as IC ¶7 asks of the encoding.
4. **Instances.** 13 constructed positives validate. 30 negatives are rejected
   for their stated reasons, among them:
   - a certificate with no signature or no issuer, an empty or unknown member,
     a name as issuer, a one-bounded validity, or a CRL pointer with no
     location;
   - a traditional certificate carrying an authorization;
   - a direct certificate with two names, or with a name subject;
   - an anonymous certificate with a name;
   - a key-equivalence certificate with no validity;
   - a CRL with no validity dates, with a `one-use` lifetime, or with a string
     sequence number;
   - a dated revalidation instrument carrying a challenge.

   These instances are constructed, not from the source, which prints none.
   None is committed.
5. **Header.** The first marker in the first 12 lines is `derived` (in
   `$id`), the name carries `.derived.`, and `$id` is
   `urn:library:rfc-2692:spki-requirements.derived`.
6. **Pass 3 (cross-check).** Pass 3 changed only `constrained_by`, the two
   `constrained_by_reason` strings, the `$comment` and the `NOT-EXPRESSIBLE`
   description. No keyword that validates an instance changed, so an instance
   validates exactly as it did before. After those edits, the 2020-12
   metaschema again reports 0 errors (`jsonschema` 4.10.3), there are no
   duplicate keys, every `$ref` resolves, and there is no cycle. Every cited id
   resolves in `requirements.yaml`, and all 200 quote uses are still verbatim.
   The tallies above (33 entries, 26 properties, 11 and 13 inferred, 21
   constraints, 15 gaps) were recounted and were unchanged by the wiring.
   The examples check then found four schema defects, applied afterwards in
   the same pass: `validity-period` takes either bound alone
   (`minProperties: 1`), while `crl.validity` (now inferred, making 14
   inferred properties) and a dated `instrument-lifetime` require both, and
   `key-equivalence-certificate` requires `not-after`; RC-01's check skips a
   missing bound; RC-03's check returns undetermined on a shared endpoint
   (G-08); `same_key` compares the keys two identifiers denote, so a key and
   its hash match (RC-17 to RC-19); and `NOT-EXPRESSIBLE` says a verifier's
   check-time decisions live in `state-machine.yaml`. The metaschema check
   passes after them, and `examples/` re-validated: 127 of 127 valid
   instances validate, 8 of 8 invalid ones are rejected.

## Source defects and ambiguities — recorded, never repaired

- **D-01 "singing".** *"This kind of certificate is signed by me, singing
  someone else's key"* (personal binding, p.6, line 331): read as "signing".
  Quoted as printed.
- **D-02 "I'm the a purchasing agent"** (p.9, line 480): a doubled article.
- **D-03 "posses"** (p.9, line 481): read as "possess".
- **D-04 "a this DNS name"** (p.10, line 525): a doubled determiner.
- **D-05 The CRL paragraph's "it".** *"If it encounters some certificate that
  it lists, then it annihilates that certificate."* has the CRL as the actor
  that "encounters". The schema reads it as describing a verifier's processing
  of an unanchored CRL.
- **D-06 The minimal CRL is described, then cured.** The paragraph gives a
  minimal CRL's contents, says such a CRL is non-deterministic, then adds three
  requirements. Whether "minimal" content plus validity dates is the whole SPKI
  CRL, and what the sequence number still does, is left open (G-06). The
  schema takes the union.
- **D-07 "one use" vs "must have its own lifetime".** VC ¶5 says a lifetime of
  0 is not possible, then offers "one use" as a lifetime. The schema treats
  "one use" as an alternative lifetime value, not as an exception to the rule.
- **D-08 List nesting is flat where it should nest.** The wallet cards from
  *"health insurance card"* (p.7) to *"permission to issue nuclear launch
  codes"* (p.9) are printed at the same level as their lead-in *"There are a
  number of cards one carries in a typical wallet"*. So where the card list
  ends is unclear. *"Other requirements:"* (p.10) is indented under the
  *"Service authentication"* item although it reads as a list-level heading.
  Locators therefore name items by their opening words, not by index.
- **D-09 "attached at the end".** The Abstract says the use list is *"attached
  at the end of this document"*. It is followed by Open Questions, References
  and Security Considerations.
- **D-10 Positive validation has no pointer rule.** VC ¶2 requires a
  certificate to say where its CRL is, and VC ¶4 asks for positive validation
  too, with no matching rule (G-04).
- **D-11 Two definitions of what a certificate is for.** GR ¶2 makes the
  purpose an authorization *"to or for a keyholder"*, while two use items
  certify software and a genealogical fact (G-13).

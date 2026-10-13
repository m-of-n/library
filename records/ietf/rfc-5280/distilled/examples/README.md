---
record: rfc-5280
kind: examples
title: "rfc-5280 — examples and test vectors"
extracted: "2026-10-13"
reviewed_by: ""
---

# RFC 5280 — examples and test vectors

This directory holds the **4 Appendix C examples as byte fixtures** and
`vectors.yaml`, which has **85 vectors** in all:

- **44 in-source.** The source prints their input. That covers the four
  fixtures, the minimal certification path that Appendix C says C.1, C.2 and
  C.4 form, and 39 examples printed in prose or figures.
- **41 constructed.** Each one tests a rule the source states but gives no
  literal for, mostly in §6.1 path validation.

Pass 1 (extract), working from the source only (`.cache/rfc-5280.txt`, the
RFC as published in May 2008). Later RFCs update RFC 5280, but this
directory does not take any of them into account.

Every vector carries `in_source: true | false`. A top-level
`expected_result` appears only where the source states the result. Anything
this extraction computed or checked sits under `derived:` with
`in_source: false`, including every OpenSSL result. The header of
`vectors.yaml` documents the fields and the defaults the constructed path
scenarios assume.

## Fixtures

| file | source | bytes | DER sha256 | what | signature |
|---|---|---|---|---|---|
| `C.1-rsa-self-signed-ca.hex` | App. C.1, dump lines 7646–7795 | 578 | `8cbea8df…aad56136` | self-signed RSA CA, serial 17, cn=Example CA | verifies under its own key |
| `C.2-rsa-end-entity.hex` | App. C.2, dump lines 7819–7978 | 629 | `db6380d2…f73dfb5a` | RSA end entity, serial 18, issued by C.1 | verifies under the C.1 key |
| `C.3-dsa-end-entity.hex` | App. C.3, dump lines 8023–8218 | 914 | `7599eb0a…06909bf6` | DSA end entity, serial 256, issued by cn=Example DSA CA | **not verifiable**: the issuer key is not in the source |
| `C.4-crl.hex` | App. C.4, dump lines 8239–8329 | 356 | `32aa7866…161fd4f2` | v2 CRL from cn=Example CA, number 12, revokes serial 18 (keyCompromise) | verifies under the C.1 key |

Each `.hex` file is lowercase hex, 32 bytes per line, and nothing else.
Each `C.n-….dump.txt` is the source's annotated dump, lines copied
verbatim, with page furniture (footer, form feed, header) and the blank
lines around it removed. `vectors.yaml` → `fixtures` records the sha256 of
each `.hex` file, of the DER it encodes, and of each dump.

The C.1 and C.2 keys are both RSA, as the source says. C.3 is the only DSA
example, and C.4 is the CRL.

### How the fixtures were rebuilt

The source calls each example an "annotated hex dump", but it prints no raw
byte column. Each line is dumpasn1 output, either `offset length: TYPE
[value]` or a continuation line `: value-data`. Bytes are printed only for
long values: integers, key identifiers, signatures. So the fixtures were
**rebuilt, not transcribed**. A script parsed every dump line and
DER-encoded every node from its type and value:

- the tag comes from the type name;
- `[n] {` is a constructed context tag, and `[n]` with a value is primitive;
- strings, UTCTime (`dd/mm/yyyy hh:mm:ss GMT` → `YYMMDDhhmmssZ`), OIDs
  (from the printed arcs), small INTEGERs and ENUMERATEDs come from the
  annotation;
- the printed hex is used for everything else;
- a BIT STRING printed as hex gets a zero unused-bits octet, which dumpasn1
  omits, and `N unused bits '…'B` is padded as printed.

The script then checked, **for every node**, that the computed offset and
the computed content length equal the printed ones. 264 nodes were checked
(66, 70, 83 and 45), with no mismatch. Any non-minimal length, wrong tag
class, or missing or extra octet would have broken an offset. The scripts
lived in the pass-1 scratch directory and are not committed. The rules
above are enough to reimplement them.

Independent checks (OpenSSL 3.0.13, run locally; nothing was fetched):

- `openssl asn1parse -inform DER` decodes each fixture. Every offset and
  length it reports equals a printed one. It reports fewer nodes (59, 61,
  68, 41) because it does not descend into encapsulating OCTET or BIT
  STRINGs.
- Each outer SEQUENCE length plus its 4-byte header equals the file length.
  That gives 578, 629 and 914, the byte counts the source states. The source
  states none for the CRL.
- Every hex block in the dumps is byte-identical in the DER at the printed
  offset. That covers moduli, DSA p/q/g/y, key identifiers, signatures and
  r/s: 3, 4, 8 and 2 blocks.
- `openssl x509 -text` / `openssl crl -text` show the serial numbers, names,
  dates, extensions and key identifiers the source's descriptions state.
- **Signatures.** `openssl dgst -sha1 -verify <C.1 key>` over the
  tbsCertificate or tbsCertList returns "Verified OK" for C.1, C.2 and C.4.
  `openssl verify -no_check_time -auth_level 0 -CAfile C.1` accepts C.1 and
  C.2. Because these signatures verify, the rebuilt to-be-signed bytes of
  C.1, C.2 and C.4 are byte-exact. Their remaining bytes, the signature
  values, are printed in full.
- **C.3** cannot be verified this way. Its AKI (`86caa522…`) names a CA
  whose certificate and key the source does not print. Its bytes rest on the
  offset and length checks plus one more: the SHA-1 of its rebuilt
  subjectPublicKey equals the printed SKI. `openssl pkey -pubcheck` accepts
  the DSA key, and q divides p−1. Two encodings that the dump implies but
  does not show were taken as DER requires: BOOLEAN TRUE is `ff`, and the
  encapsulating BIT STRING has a zero unused-bits octet. **This is a gap,
  not a failure.** Nothing was substituted for the missing key.
- **Key identifiers.** In all three certificates the SKI equals method (1)
  of §4.2.1.2: the SHA-1 of the subjectPublicKey BIT STRING value. The
  source says so only for C.1 (item (g)). C.2's AKI equals C.1's SKI, as
  C.2 (h) says, and so does C.4's AKI.

To reproduce the signature checks:

```sh
xxd -r -p C.1-rsa-self-signed-ca.hex > c1.der    # likewise c2, c4
openssl x509 -inform DER -in c1.der -out c1.pem
openssl x509 -inform DER -in c2.der -out c2.pem
openssl crl  -inform DER -in c4.der -out c4.pem
openssl verify -no_check_time -auth_level 0 -CAfile c1.pem c2.pem             # OK
openssl crl -in c4.pem -CAfile c1.pem -noout                                   # verify OK
openssl verify -attime 1107626400 -auth_level 0 -crl_check \
        -CAfile c1.pem -CRLfile c4.pem c2.pem                                  # error 23: certificate revoked
```

`-auth_level 0` is needed because OpenSSL's default security level rejects
SHA-1 and 1024-bit RSA. Without it the failure would come from OpenSSL
policy, not from the fixture.

## Vectors

| source section | in source | constructed | ids |
|---|---|---|---|
| Appendix C.1–C.4 (fixtures) | 4 | 0 | `PKIX-C1-01`, `PKIX-C2-01`, `PKIX-C3-01`, `PKIX-C4-01` |
| Appendix C (the minimal path C.1 → C.2 with C.4) | 1 | 1 | `PKIX-C-01`; `PKIX-C-02` |
| §4.1.2.5 Validity (99991231235959Z) | 1 | 0 | `PKIX-4125-01` |
| §4.1.2.6 Subject (emailAddress case) | 1 | 0 | `PKIX-4126-01` |
| §4.2.1.6 Subject Alternative Name (scheme case; dNSName " "; mail address in DNS form) | 3 | 0 | `PKIX-4216-01` … `-03` |
| §4.2.1.10 Name Constraints | 13 | 1 | `PKIX-42110-01` … `-13`; `-14` |
| §4.2.1.11 Policy Constraints ("a value of one") | 1 | 0 | `PKIX-42111-01` |
| §4.2.1.13 CRL Distribution Points (LDAP URIs) | 2 | 0 | `PKIX-42113-01`, `-02` |
| §4.2.1.14 Inhibit anyPolicy ("a value of one") | 1 | 0 | `PKIX-42114-01` |
| §4.2.2.1 Authority Information Access (LDAP URIs) | 2 | 0 | `PKIX-4221-01`, `-02` |
| §4.2.2.2 Subject Information Access (LDAP URIs) | 2 | 0 | `PKIX-4222-01`, `-02` |
| §5.2 CRL Extensions (unprocessable critical extension) | 0 | 1 | `PKIX-52-01` |
| §5.2.7 Authority Information Access (LDAP URIs) | 2 | 0 | `PKIX-527-01`, `-02` |
| §6.1 Basic Path Validation (duplicates, self-issued) | 0 | 2 | `PKIX-61-01`, `-02` |
| §6.1.2 Initialization (Figure 3) | 1 | 0 | `PKIX-612-01` |
| §6.1.3 Basic Certificate Processing (Figures 4–7; checks) | 4 | 11 | `PKIX-613-01` … `-04`; `-05` … `-15` |
| §6.1.4 Preparation for Certificate i+1 ((g) examples; checks) | 4 | 19 | `PKIX-614-01` … `-04`; `-05` … `-23` |
| §6.1.5 Wrap-Up Procedure | 0 | 3 | `PKIX-615-01` … `-03` |
| §6.3.3 CRL Processing (on the C.4 fixture) | 0 | 3 | `PKIX-633-01` … `-03` |
| Appendix B (DER DEFAULT omission; NC URI holds a DNS name) | 2 | 0 | `PKIX-B-01`, `-02` |
| **total** | **44** | **41** | **85** |

The LDAP URI block (`42113`, `4221`, `4222`, `527`) sits after the
§4.2.1.14 vector in the file. `PKIX-4216-02` and `-03`, added in pass 2,
follow `PKIX-4216-01` although their source lines (2014–2027) come before
it. Every other vector is in source order.

### The constructed path vectors, by rule

| rule | vectors | outcome |
|---|---|---|
| name constraints: permitted DNS subtree passes, an out-of-subtree name fails | `PKIX-613-05`, `-06` | succeeds; fails at 6.1.3(b) |
| exclusion beats permission (N-151) | `PKIX-613-07` | fails at 6.1.3(c) |
| name form absent → acceptable | `PKIX-613-08` (also in-source `PKIX-42110-13`) | succeeds |
| directoryName subtree (§7.1 "within") | `PKIX-613-09` | fails at 6.1.3(b) |
| self-issued intermediate exempt from name constraints; self-issued *final* certificate not exempt | `PKIX-613-10`, `-11` | succeeds; fails at 6.1.3(b) |
| §6.1.4(g) intersection across two CAs: inside, outside, empty | `PKIX-614-05`, `-06`, `-07` | succeeds; fails; fails |
| §6.1.4(g) union of exclusions across two CAs | `PKIX-614-08` | fails at 6.1.3(c) |
| pathLenConstraint exceeded (0 and 1) | `PKIX-614-09`, `-12` | fails at 6.1.4(l) |
| pathLenConstraint 0 directly above the target (EE or CA) | `PKIX-614-10`, `-13` | succeeds |
| self-issued intermediate exempt from the pathLen count | `PKIX-614-11` | succeeds |
| cA false used as an issuer (absent; FALSE; v1 with no out-of-band check) | `PKIX-614-14`, `-15`, `-16` | fails at 6.1.4(k) |
| keyCertSign absent (keyUsage present) / keyUsage absent | `PKIX-614-17`, `-18` | fails at 6.1.4(n); succeeds |
| unrecognised critical extension (intermediate; target) / non-critical | `PKIX-614-19`, `PKIX-615-01` / `PKIX-614-20` | fails; fails; succeeds |
| anyPolicy in policyMappings | `PKIX-614-21` | fails at 6.1.4(a) |
| explicit policy (initial-explicit-policy; requireExplicitPolicy 0; neither) | `PKIX-613-12`, `PKIX-614-22`, `PKIX-613-13` | fails; fails; succeeds with NULL tree |
| policy mapping and the user-initial-policy-set | `PKIX-614-23` | fails ({P2}); its companion with {P1} succeeds |
| §6.1.5(g) intersection with the user-initial-policy-set | `PKIX-615-02`, `-03` | fails; succeeds with NULL tree |
| duplicate certificate in the path; self-issued determination under §7.1 | `PKIX-61-01`, `-02` | rejected; self-issued |
| issuer-name chaining; bad signature; expiry (on C.2) | `PKIX-613-14`, `-15`, `PKIX-C-02` | fail at 6.1.3(a)(4), (a)(1), (a)(2) |
| CRL use: critical CRL extension; no cRLSign; no reasonCode; removeFromCRL delta | `PKIX-52-01`, `PKIX-633-01` … `-03` | CRL unused; CRL unused (**ambiguous**: the CRL issuer is the trust anchor); unspecified; UNREVOKED |

Every constructed vector cites its R-ids from `requirements.yaml`, and
N-ids from `normative.md` where the rule is lowercase prose. Each vector
also carries a `trace` of the state variables that decide its outcome.

## Count reconciliation

**44 in-source.**

- **4 fixtures**: every example Appendix C prints. The Appendix C intro
  says "four examples: three certificates and a CRL".
- **1 path vector** (`PKIX-C-01`). It is grounded in the intro's sentence
  "The first two certificates and the CRL comprise a minimal certification
  path." The source states no outcome for this path, so the outcome (fails:
  C.2 is revoked) is under `derived`.
- **39 prose and figure examples**, each a value the source prints with a
  stated meaning or result:
  - 1 date (§4.1.2.5)
  - 2 case-equivalence pairs (§4.1.2.6, §4.2.1.6)
  - 2 prohibited name values (§4.2.1.6): the dNSName " " and the DNS form
    of a mail address
  - 13 name-constraint cases (§4.2.1.10): 4 URI, 4 mail, 3 DNS, 1 IP
    encoding, and 1 "no name of the type"
  - 2 "a value of one" statements (§4.2.1.11, §4.2.1.14)
  - 8 LDAP URIs (§4.2.1.13, §4.2.2.1, §4.2.2.2, §5.2.7)
  - 5 policy-tree figures (Figures 3–7)
  - 4 set operations (§6.1.4(g))
  - 2 Appendix B encoding notes

  Where the source states a result for a whole class and prints no member,
  for example "any mail address at the host", the vector picks a member and
  marks it `candidate_basis: chosen`. The same applies to the policy OIDs
  and certificates in `PKIX-42111-01` and `PKIX-42114-01`, marked
  `path_basis`.

**41 constructed**, by section:

| Appendix C | 4.2.1.10 | 5.2 | 6.1 | 6.1.3 | 6.1.4 | 6.1.5 | 6.3.3 |
|---|---|---|---|---|---|---|---|
| 1 | 1 | 1 | 2 | 11 | 19 | 3 | 3 |

**Examples in the source not made into vectors:**

- Figure 1 (PKI entities) and Figure 2 (the path-processing flowchart) are
  diagrams of roles and of control flow. They belong to the protocol and
  state-machine artifacts.
- The DN strings in prose, such as "cn=Example CA,dc=example,dc=com", are
  carried inside the fixture vectors.
- Statements of the form "e.g." that name a field or a standard, not a
  value, are not examples: "e.g., DAP or LDAP", "e.g., "http" or "ftp"" in
  the scheme requirement, "e.g., "Susan Housley"" in the attribute list,
  "e.g., "Jr."".
- Appendix B (lines 7437–7444) names the at sign and the underscore as
  characters PrintableString does not support. They are the character set
  of a rule (R-0610), like the 20-octet and 2^28 limits beside them, not an
  example value, so no vector was made.

## Sections with no vector, and why

- **§1–§3** (introduction, requirements and assumptions, overview) print no
  certificate or CRL value. The §3 entity and lifecycle material belongs to
  the protocol and state-machine artifacts.
- **§4.1 and §5.1 ASN.1** are the schema artifact. Their fields are
  exercised by the four fixtures.
- **§4.1.2.1–§4.1.2.9 and §5.1.2.x field rules** print no example values
  apart from §4.1.2.5's 99991231235959Z. The fixtures exercise the version,
  serial, signature, issuer, validity, subject, SPKI, thisUpdate,
  nextUpdate and revokedCertificates rules, under each fixture's
  `conformance_checked`.
- **§4.2.1.1–§4.2.1.3 and §4.2.1.9** (key identifiers, key usage, basic
  constraints) print no value of their own. They are exercised by the
  fixtures (SKI method (1), AKI matching, keyUsage bits, cA TRUE) and by
  `PKIX-614-09` … `-18`.
- **§4.2.1.4, §4.2.1.5, §4.2.1.12, §4.2.1.15, §4.2.2** (except the LDAP
  URIs), **§5.2.1–§5.2.6, §5.3** print no example value. That covers
  certificate policies and user notices, policy mappings, extended key
  usage, freshest CRL, the access-method details, delta CRL indicator,
  issuing distribution point, and the reason, invalidity date and
  certificate issuer entry extensions. Their path-validation consequences
  appear in the §6.1 and §6.3.3 constructed vectors. C.3 exercises a
  certificatePolicies extension, and C.4 a reasonCode and a CRL number.
- **§6.2** gives no example. Its MAYs are augmentation permissions, noted in
  `PKIX-C-02`.
- **§6.3.1, §6.3.2** (revocation inputs and state) print no values.
  `PKIX-C-01` and `PKIX-633-01` … `-03` exercise them.
- **§7.1–§7.5** (internationalised names) print no IDN, IRI or
  internationalised-address example. The only literal is the four
  characters "xn--", a prefix, not an example value. The comparison rules
  are used by `PKIX-61-02` and `PKIX-613-09`. Without a printed IDN, any
  vector here would be wholly constructed and would rest on RFC 3490
  behaviour outside this source, so none was made.
- **§8 Security Considerations, §9 IANA, §10–§11** contain no examples.
- **Appendix A** is the ASN.1 module: the schema artifact.

## Source issues found (recorded, not repaired)

1. **Appendix C prints no raw bytes.** "Annotated hex dump" describes
   dumpasn1's annotation. The bytes have to be rebuilt (above). The intro
   points at a NIST URL for the binaries, but it was not fetched.
2. **C.3's issuer is not in the source.** Its signature is unverifiable
   from RFC 5280 alone. Recorded on `PKIX-C3-01`.
3. **Self-issued exemption, final certificate.** §6.1 (lines 4105–4107)
   says self-issued certificates "are not counted when evaluating path
   length or name constraints", with no exception. §4.2.1.10 (2214–2215)
   and §6.1.3(b), (c) exempt only *non-final* self-issued certificates
   from name constraints. Recorded on `PKIX-613-11`.
4. **What counts for inhibitPolicyMapping and requireExplicitPolicy.**
   §4.2.1.11 counts "the number of additional certificates" (lines
   2374–2376, 2380–2382). §6.1.2(d), (f) and §6.1.4(h) count only
   non-self-issued certificates. §4.2.1.14 says "non-self-issued" for
   inhibitAnyPolicy. Recorded on `PKIX-42111-01`.
5. **§6.1.5 has no failure exit.** Unlike §6.1.3 and §6.1.4, the wrap-up
   states only its success condition. Rejecting a target with an
   unrecognised critical extension (6.1.5(f)) rests on §6.1's "clients MUST
   reject" (R-0372) and §4.2 (R-0071). Recorded on `PKIX-615-01`.
6. **Description omissions (minor).** The C.2 and C.3 descriptions do not
   mention the subjectKeyIdentifier extension that each dump contains.
   C.2's does not mention its critical keyUsage. Nothing contradicts the
   dumps.
7. **keyUsage of a trust anchor that signs a CRL.** §6.3.3(f) checks
   keyUsage in "the CRL issuer's certificate". When the CRL issuer is the
   trust anchor, §6.1.1(d) uses only the name and key of its self-signed
   certificate, and R-0381 keeps that certificate out of the path. The
   source does not say whether its keyUsage is checked. Recorded on
   `PKIX-633-01`, which is marked `ambiguous: true`.

Items 1–5 and 7 are new relative to the shared defect list. Issue 6 is
noted for completeness only.

## Pass 2 (verify)

- Fixtures rebuilt independently from the four `dump.txt` files by a new DER encoder (66, 70, 83, 45 nodes; every offset and length equal): all four byte-identical to the `.hex` files. No fix.
- `dump.txt` files re-extracted from source lines 7646–7795, 7819–7978, 8023–8218, 8239–8329 with page furniture removed: byte-identical. No fix.
- Signatures re-verified with OpenSSL 3.0.13: C.1 self-signed, C.2 and C.4 under the C.1 key: "Verified OK". C.3: no key or certificate for cn=Example DSA CA anywhere in Appendix C or the rest of the source; C.3 does not verify under its own key. No fix.
- Every sha256 in `vectors.yaml` (`.hex`, DER, dump) matches the files. No fix.
- `PKIX-42110-02`: lines 2260-2261 → 2259-2261 (the quoted sentence begins on 2259).
- `PKIX-4221-01`, `-02`: lines 2783-… → 2782-… (the quoted sentence begins on 2782).
- `PKIX-615-02`: `rule_text_note` said lines 4919-4920; the hyphenation is at 4922-4923.
- `vectors.yaml` header said one quote rejoins a hyphenated word; there are two (`PKIX-614-09`, `PKIX-615-02`).
- `PKIX-633-03`: the §5.2.4 quote in `note` stopped mid-sentence and dropped the second condition of the MAY; completed, lines 3558-3561 → 3558-3562.
- `PKIX-633-01`: marked `ambiguous: true` with `ambiguous_reason` (source issue 7); `ambiguous` added to the header conventions.
- Added `PKIX-4216-02` (dNSName " ", lines 2014–2024) and `PKIX-4216-03` (mail address in DNS form, lines 2024–2027): printed example values with a stated result that pass 1 missed. Counts 83/42 → 85/44 in `vectors.yaml` and here.

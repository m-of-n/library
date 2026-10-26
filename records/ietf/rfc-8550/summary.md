---
schema: "library-summary/v1"
id: rfc-8550
record: rfc-8550
type: summary
updated: "2026-10-26"
---

# S/MIME Version 4.0 Certificate Handling

|  |  |
|---|---|
| **Type** | rfc (IETF LAMPS WG, from `draft-ietf-lamps-rfc5750-bis-08`) |
| **Maturity** | `standard`: Category Standards Track on the title page; Proposed Standard in the RFC Editor metadata, checked 2026-10-26 |
| **Authors** | J. Schaad (August Cellars), B. Ramsdell (Brute Squad Labs), S. Turner (sn3rd) |
| **Published** | 2019-04 (title page; `rfc8550.json` says May 2019) |
| **Identifier** | RFC 8550 · DOI 10.17487/RFC8550 · Obsoletes RFC 5750 |
| **Source** | https://www.rfc-editor.org/rfc/rfc8550.txt |
| **Digest** | `sha256:adf5aa63…` (full value in `record.yaml`), fetched 2026-10-26 |
| **Errata** | none listed, checked 2026-10-26 |

## Overview

RFC 8550 is the certificate half of S/MIME 4.0, the companion to `rfc-8551`'s message format. Its argument fits in one sentence of §1: S/MIME agents *"MUST use PKIX certificates to validate public keys as described in [RFC5280]"* and must also meet the certificate-processing requirements in this document. What it adds on top of PKIX is a **mail profile**, not a trust model. It covers where an email address goes in a certificate and how a receiver matches it to the message (§3, §4.4.3), which key usages count for signing mail (§4.4.2, §4.4.4), how agents cope with certificates arriving in arbitrary order inside messages (§2.3, §4.2), CRL handling (§2.1, §4.1), and algorithm and key-size mandates (§4.3, Appendix A).

The trust model is RFC 5280's, unchanged. This record confirms the `delegation-models` topic's claim that S/MIME trust "lives" here, with a correction: what lives here is **identity matching**, not trust. Trust anchors, delegation and name constraints all stay in `rfc-5280`. RFC 8550 never names how a root is chosen, and never mentions name constraints.

## The five questions #14 asks, by locator

**1. Who decides the root.** The agent decides, and the RFC does not say how. "Trust anchor" occurs once, in §6, in a caution about certificates *"that have not first been validated to a trust anchor"*. "Trusted CA" occurs once, in §6's list of failure cases: *"no certificate chain leads to a trusted CA"*. The only guidance is negative, in §2.3: *"receiving agents SHOULD NOT simply trust any self-signed certificates as valid CAs but SHOULD use some other mechanism to determine if this is a CA that should be trusted"*. The "other mechanism" is never named. The anchor is therefore an input that RFC 5280 §6 leaves to policy, and an agent's root store in practice: the OS, the browser root program or an administrator (see Implementations). §2.3 also tells senders to include a chain *"up to, but not including, a CA that it believes that the recipient may trust as authoritative"*. The sender guesses the receiver's anchor, and nothing in the protocol carries it.

**2. Anything added to PKIX delegation.** Nothing that delegates. §4.2: *"Certificate, CRL, and path validation MUST be performed as per [RFC5280] when validating a correspondent's public key."* §4.4: *"Interpretation and syntax for all extensions MUST follow [RFC5280], unless otherwise specified here."* §4.4.1 restates RFC 5280 on basicConstraints, explicitly *"As per [RFC5280]"*: CA certificates MUST contain it, and end-entity certificates SHOULD NOT. The deltas from PKIX are all on end-entity *purpose*, not on delegation:

- §4.4.2: a key usage extension, if present, MUST be marked critical. RFC 5280 §4.2.1.3 only says SHOULD, so this tightens it. Receivers MUST NOT accept a message signature from a certificate whose key usage has neither digitalSignature nor nonRepudiation. An absent key usage MUST be presumed to have both.
- §4.4.4: if extended key usage is present, interpersonal-message receivers MUST check for `id-kp-emailProtection` or `anyExtendedKeyUsage`. The usable purposes are the intersection of key usage and extended key usage.
- §2.3: receivers MUST support chaining on distinguished names, and other chain-building methods MAY be supported. §4: agents *"MUST handle multiple valid CA certificates containing the same subject name and the same public keys but with overlapping validity intervals"* (CA rollover).

**Name constraints are absent.** The phrase does not occur. §4.4 lists the extensions agents MUST handle: basic constraints, key usage, authority and subject key identifiers, and subject alternative name. nameConstraints is not on the list. §4.4 then says certificates *"issued for the S/MIME environment SHOULD NOT contain any critical extensions"* other than those listed. RFC 5280 §4.2.1.10 says *"Conforming CAs MUST mark this extension as critical"* for name constraints. On our reading, a CA certificate scoping a sub-CA to `*@foo.com`, which is exactly the rfc822Name subtree the topic answer credits to X.509, sits between an RFC 8550 SHOULD NOT and an RFC 5280 MUST. The MUST should prevail, since §4.4 itself defers to RFC 5280 and §4.2 requires RFC 5280 validation. **S/MIME does not forbid name-constrained delegation, but its own profile does not mention it.** Not set as `contradicts`: a SHOULD NOT that yields to the referenced MUST is a tension, not an incompatible assertion. It is plausibly aimed at end-entity certificates, though the text does not say so.

**3. Binding an email address to a certificate, and the From check.** §3 and §4.4.3. End-entity certificates MAY contain an address. The address SHOULD be in subjectAltName and SHOULD NOT be in the subject DN (§3). In subjectAltName, an ASCII local part MUST use the `rfc822Name` choice per RFC 5280 §4.2.1.6, a non-ASCII local part MUST use the `otherName` of RFC 8398 §3, and several addresses MAY be present (§4.4.3). Receivers MUST recognise ASCII and internationalised addresses in subjectAltName, and MUST recognise the PKCS #9 `emailAddress` attribute in the DN, which MUST be IA5String with an upper bound of 255 characters (§3). The receiver's check is the one rule in this document that binds the message to the certificate:

> *"Receiving agents MUST check that the address in the From or Sender header of a mail message matches an Internet mail address in the signer's certificate, if mail addresses are present in the certificate."* (§3)

Three qualifications sit right beside it in §3:

- **It is conditional.** *"Receiving agents MUST recognize and accept certificates that contain no email address."* Agents may instead associate an address *"through the use of the agent's address book"*. With no address in the certificate, nothing ties the key to the From line except local, unsigned state.
- **On mismatch, the receiver SHOULD provide "some explicit alternate processing"**, such as displaying the addresses. It is not told to reject.
- **Matching rules.** For ASCII addresses, *"the domain component (right-hand side of the '@') MUST be compared using a case-insensitive function"*, and the local part SHOULD be. Internationalised addresses follow RFC 8398. The RFC adds that *"The comparing of email addresses is fraught with peril."*

The binding is only as good as the CA that wrote the address. RFC 8550 says nothing about how a CA verifies control of a mailbox. That is now the CA/Browser Forum S/MIME Baseline Requirements, which this library does not hold. Senders SHOULD make From or Sender match (§3).

**4. Revocation.** CRLs only. OCSP appears once, in Appendix A.1's historic-message discussion, never as a requirement. §2.1 and §4.1 both say: *"All agents MUST be capable of performing revocation checks using CRLs as specified in [RFC5280]."* and *"All agents MUST perform revocation status checking in accordance with [RFC5280]."* Receivers MUST recognise CRLs carried in messages, and MUST support v1 and v2 CRLs (§2.1). Everything about freshness is SHOULD:

- retrieve and use CRL information every time a certificate is verified (§4.1)
- have a CRL retrieval mechanism (§4.1)
- store received CRLs (§2.1)
- consult the most recent CRL, because a sender *"could deliberately include an older unexpired CRL"* (§6)

§4.1 then concedes that offline verification may make this impossible: *"The value of the CRL information in a particular context is beyond the scope of this specification"*. §6 adds the time attack: a forged or backdated `signingTime` can select a CRL that predates a revocation. Validity time SHOULD be the current time unless a securely stored receipt time or a validated countersignature time is available. Appendix A.1 notes that CAs need not keep an expired certificate on a CRL for more than one update after expiry, so revocation of old messages is often uncheckable. No delegated or escrowed revocation exists here. Revocation is the CA's act, on the CA's list.

**5. Anything that lets one key grant another anything.** No, beyond the CA certificate itself, which is RFC 5280's mechanism. Three near misses:

- **Attribute certificates (§2.2, §2.3).** Receivers SHOULD support v2 ACs (RFC 5755), which are X.509's authorization objects. §2.3 confines that to decoding: *"All other issues regarding the generation and use of X.509 ACs are outside the scope of this specification."* The one authorization-shaped object S/MIME admits, it declines to interpret.
- **SMIMEEncryptionKeyPreference (§4.2).** When it is present in an encapsulating SignedData, *"it SHALL be used to identify the originator's certificate found in OriginatorInfo"*. This is a selector, and it confers nothing. It agrees with `rfc-8551` §2.5.3's "represents only a preference".
- **signingCertificate / signingCertificateV2 (§4.2).** These SHALL identify the signer's certificate when present. They bind a signature to a certificate, not a key to another key.

## RFC 8551 §4 points at RFC 5750, and it mostly does not matter

`rfc-8551` §4 sends readers to *"[RFC5750]"*, the v3.2 certificate document that this RFC obsoletes. RFC 8550's own §1.6 lists the changes since v3.2 as internationalised email addresses (§3) and algorithms (§4.3, Appendix A), and nothing else. We spot-checked RFC 5750 (`.cache/rfc-5750.txt`, sha256 `7f99021775d4…`, fetched 2026-10-26) for the trust-relevant sentences. Its trust rules are the same: the self-signed-CA SHOULD NOT, the From/Sender MUST, the revocation-status MUST and "no certificate chain leads to a trusted CA". It also has no name-constraints text. **For #14's questions the stale pointer is harmless. For an implementer it is not**: following it yields RSA-with-SHA-1 and 1024-bit-era key-size rules and no EAI (`otherName`) support. The defect is 8551's, already recorded there, and this record does not set an edge for it.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `adjacent` | Defines the receiving-side identity checks for S/MIME (§3, §4.4) and a short threat list (§6), and defers every trust decision to RFC 5280 |
| Cryptography | `adjacent` | Mandates certificate and CRL signature algorithms and RSA key sizes (§4.3), and defines no primitive |
| This project | `adjacent` | The incumbent email-identity deployment that ARCH-0001's email example is measured against, and not a model we adopt |

- **R-I-05**: this is the document that says what an imported S/MIME identity *is*. It is an X.509 certificate validated per RFC 5280 (§1, §4.2), carrying an address a CA asserted (§3, §4.4.3). That is exactly a "foreign identity assertion about a key", marked `provenance: x509`.
- **R-I-01**: the S/MIME mapping table needs rows this document defines and RFC 8551 does not. These are the rfc822Name/otherName/emailAddress locations, the conditional From/Sender match, and the key usage and extended key usage purpose rules. "Dropped" must include the address-book binding of §3, which has no signed form.
- **R-I-02**: §2.3's refusal to trust a self-signed certificate merely because it arrived in a message is the same stance. Importing a certificate must not make its root an anchor.
- **R-M-03**: a contrast. In S/MIME the address is a global name, and any CA in the receiver's root store may assert it (§3). Nothing scopes the name to the issuer, so it is not interpreted relative to any principal.
- **R-O-02**: a revocation-heavy design whose own text concedes the checks may be impossible offline (§4.1) and spoofable by choice of CRL or `signingTime` (§6).

## Implementations

**Searched 2026-10-26.** We web-searched for "RFC 8550" implementations and for the CA/Browser Forum S/MIME requirements. No implementation claims RFC 8550 conformance by number. S/MIME agents implement it as part of "S/MIME", so the list is the same family as `rfc-8551`'s, annotated for certificate handling.

| Name | Kind | License | URL |
|---|---|---|---|
| Mozilla Thunderbird (NSS) | open source, mail client | MPL-2.0 | https://www.thunderbird.net/ |
| OpenSSL (`openssl cms`, `openssl smime`) | open source, library/CLI | Apache-2.0 | https://docs.openssl.org/master/man1/openssl-cms/ |
| Bouncy Castle (`bcmail`, `bcpkix`) | open source, library | MIT-style | https://www.bouncycastle.org/ |
| Microsoft Outlook / Exchange | commercial | — | https://learn.microsoft.com/en-us/exchange/policy-and-compliance/smime |
| Apple Mail | commercial | — | https://support.apple.com/guide/mail/welcome/mac |

The search also answers question 1 in practice. Root selection is a root program or IT policy, never the protocol. The CA/Browser Forum S/MIME Baseline Requirements (https://cabforum.org/working-groups/smime/requirements/) now define what a publicly trusted S/MIME certificate is: the `id-kp-emailProtection` EKU, plus an `rfc822Name` or `SmtpUTF8Mailbox` otherName in subjectAltName. They also cover how the CA validates mailbox control, which RFC 8550 never addresses. We have not ingested that document. The libraries validate paths against a caller-supplied anchor set and leave §3's header match to the mail agent. We did not test whether each client performs the §3 match.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, implementations survey, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`, and FX-1 extraction is not claimed here.** This record is at the summary bar, written for **m-of-n/library#14** (the X.509 / S/MIME / OpenPGP / SDSI-SPKI delegation-and-trust report), which needed the S/MIME row answered by locator. RFC 8550 is an `rfc` record, so a full FX-1 extraction would be owed when one is wanted, and **it needs its own issue**. No issue owns it yet. That extraction would cover normative text, BCP 14 keywords reconciled (including the SHOULD+/SHOULD-/MUST- levels of §1.2), the §3 ASN.1 fragment, the §4.3 key-size table, and design notes. No keyword count is given here because none has been reconciled. The `.cache/` copies of RFC 8550 and RFC 5750 are local and gitignored.

## Limits

- **It does not settle who the root is**, and does not try to. §2.3's "some other mechanism" and §6's "trusted CA" leave the answer to RFC 5280 §6 and to deployment.
- **It does not say how a CA verifies an email address.** The §3 match is only as strong as the issuer's validation, which lies outside the document. The CA/Browser Forum S/MIME BRs fill that gap and are not held here.
- **The From/Sender check is weaker than it looks.** It is conditional on an address being present, it SHOULD (not MUST) produce alternate processing on mismatch, and an address-book binding may stand in for it (§3).
- **Name constraints are unaddressed**, and §4.4's critical-extension SHOULD NOT is in tension with RFC 5280 §4.2.1.10's MUST-critical rule for them. Recorded above as our reading, not a `contradicts` edge.
- **Source defects, minor.** The table of contents numbers both Reference Conventions and Normative References as "7.1". The body heading "7.3  Informative References" lacks its period. §4.3 refers to RSA keys of "1024-bit through 3072-bit" against a 2048-bit minimum two paragraphs earlier, which is historical carry-over.
- **A successor exists, unread.** `draft-ietf-lamps-rfc8550bis-00` (23 July 2026) has the same title and abstract. If it advances, this record will be superseded by a new one.
- **Read scope.** The whole RFC was read, including Appendices A and B. RFC 5750 was spot-checked only for the sentences named above.

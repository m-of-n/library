---
schema: "library-summary/v1"
id: c2pa-2-4
record: c2pa-2-4
type: summary
updated: "2026-11-05"
---

# Content Credentials: C2PA Technical Specification 2.4

|  |  |
|---|---|
| **Type** | spec |
| **Maturity** | unset: no enum equivalent was checked |
| **Authors** | none named; C2PA |
| **Published** | April 2026 (§5.3.1) |
| **Identifier** | version 2.4 |
| **Source** | https://spec.c2pa.org/specifications/specifications/2.4/specs/C2PA_Specification.html |
| **Digest** | `sha256:507b8880…` (full value in `record.yaml`), fetched 2026-11-01 |

## Overview

C2PA defines a signed manifest bound to an asset: labelled assertions, a claim that references them, and a COSE signature over the claim. A validator reports a result that a person must then interpret, and §14.3.2 ranks a manifest as Well-Formed, Valid or Trusted, with a separate asset state in §14.3.3. Trust is about the signer's identity only, not whether assertions are true: §14.1 leaves that judgment to the consumer, and the guiding principle quoted in §1.2 says C2PA specifications SHOULD NOT provide value judgments about whether provenance data is good or bad. Vocabulary lives in the document: §6.2.2 points to Chapter 18 for the publicly known labels, entity-specific labels are namespaced by domain name (§6.2.1), and 2.4 added `c2pa.ai-disclosure` (§18.28). §16 defers presentation to a separate UX document.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | A full verification procedure with defined status codes, trust lists and revocation (§14, §15) |
| Cryptography | `core` | COSE signatures, hard bindings and X.509 credentials |
| This project | `core` | The nearest deployed comparison for how signed claims reach a person, and an example of the design we are arguing against on vocabulary |

- **DEC-007**: label meaning is prose in a specification, and §6.5 says validators should not validate inputs against the schemas. §5.2 asks implementations to tolerate unknown data. Nothing in the sections read gives a client a way to resolve a label into words. mofn's report §6.5 says the specification defines no human-readable descriptions for assertion *labels*. That holds for labels. For some *values* it is not the whole picture: `digitalSourceType` values (§18.15) are URIs, some at `cv.iptc.org`, and the IPTC one tested dereferences; §18.17 metadata is JSON-LD with an `@context`; and region types may come from a controlled vocabulary such as IPTC's (§18.2.2). So dereferenceable vocabularies are used for some values, though not for labels as a class. **DEC-007** is proposed, not accepted: it exists only in ARCH-0001-PROPOSAL v0.2.0 §5, and mofn's DECISIONS-0001 item 5d asks whether it survives at all.
- **R-M-12** (proposed text; relocated to ARCH-0002 P1 and accepted by ADR-0001): §6.2.1 namespaces by DNS name, not by key. It avoids a central registry for entity labels, but the identity it hangs on is not key-relative.
- **R-O-06** (proposed): §14.3 and §15.2 are a real example of distinct outcomes rather than one boolean. §14.3.5 attributes a Valid manifest's claim to the claim generator, and trust is a further state.
- **R-O-05** (proposed): crJSON, new in 2.4 (§5.3.1), is a derived JSON-LD view that is "not independently verifiable or intended as an input format". Verification stays on the signed bytes, not on a re-serialisation, which is the shape R-O-05 asks for. crJSON is for profile evaluation, testing and reporting, not a human-facing form.
- **R-M-07**: hard bindings (§9.2, §15.12) are the content digest binding.
- **R-I-01**: any C2PA mapping would have to state what is lost, including the DNS-based labels.

## Relations

No edge is authored here. Each related record authors its own, with its reason: `c2pa-ux-2-2` (`contradicts`, on validation states), `cawg-identity-1-2`, `c2pa-conformance-program`, `nsa-2025-content-credentials`, `pics-1-1-services`, `powder-description-resources`, `cscw-2023-provenance-trust` and `moruzzi-2025-content-authenticities`. `ca-sb-942` and `eu-code-of-practice-marking` also author edges to this record.

## Implementations

**Searched 2026-11-01**, GitHub API, for the contentauth SDKs only. They were confirmed to exist, not tested. GitHub reports `NOASSERTION` for c2pa-rs, which carries two license files. c2pa-python also carries both and its README states both; GitHub reports only Apache-2.0 for it (rechecked 2026-11-05).

| Name | Kind | License | URL |
|---|---|---|---|
| c2pa-rs | open source, Rust | MIT, Apache-2.0 files | https://github.com/contentauth/c2pa-rs |
| c2pa-js | open source, JavaScript | MIT | https://github.com/contentauth/c2pa-js |
| c2pa-python | open source, Python | MIT, Apache-2.0 files | https://github.com/contentauth/c2pa-python |

Commercial conforming products are listed under `c2pa-conformance-program`.

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata, relations, `bears_on`, usefulness verdict |
| `summary.md` | this document |

**No `distilled/`, and FX-1 extraction is not claimed here.** This is the summary bar. A `spec` record owes FX-1 when someone extracts it, and no issue owns that yet. No keyword count is given because none has been reconciled.

## Limits

- **2.4 is no longer the latest.** 2.5 (October 2026) is published. It was not read, beyond confirming its date and that it, like 2.4, does not mention CAWG in text search. Nothing here describes 2.5.
- **Third-party statements are invisible to it.** The manifest is produced in the asset's chain, and the sections read define no way to ask who else has made claims about an asset.
- **The threat model is elsewhere.** §17 summarises a process and points to separate Security Considerations, not held here.
- **ISO status not established.** `nsa-2025-content-credentials` says a fast-track to ISO 22144 was under way in January 2025. The spec text does not mention it in a full-text search.
- **Read scope.** 2.4 by section, from extracted text: §1, §5.1, §5.2, the start of §5.3.1, §6, §14.1 to §14.4, §15.1, §15.3, §16, the start of §17, §18.4 (start), §18.17 (start), §18.28 and §18.29. Full-text search covered `CAWG`, `ISO 22144` and unknown-data handling. The 2026-11-05 verify pass also read §14.3 to §14.4.1, §15.3, §16, §17.1, §18.2.2 (region type), the `digitalSourceType` text in §18.15 and the §5.3.1 changelog. §7 to §13, the rest of §15 and §18, §19 and the appendices were not read, including the CDDL for AI disclosure. Figures were not viewed.

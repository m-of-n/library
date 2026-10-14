---
record: rfc-9580
kind: index
title: "rfc-9580 — distilled artifacts"
extracted: "2026-10-13"
reviewed_by: ""
---

# Distilled artifacts

FX-1 (`docs/extraction.md`). One line per artifact: what it covers, and what
it does not.

| kind | file | coverage |
|---|---|---|
| normative | normative.md | 616 verbatim entries N-001 to N-616 in source order, §1 to Appendix C, each one contiguous run of source lines with its line range. 299 flagged lowercase/implied, 39 test vector, 32 table, 16 IANA action, 11 code, 8 grammar, 5 non-normative. Omitted with a note in place: motivation, history, overview prose, the §16 references, Acknowledgements and Authors' Addresses. |
| requirements | requirements.yaml | 421 entries R-0001 to R-0421, all stated, in source order. Source count 365, extracted 359, reconciled keyword for keyword; the 6 not extracted report RFC 4880's rules, mention the word, or are erratum titles. 85 verb none (binding lowercase text). 327 testable, 58 partial, 36 not. |
| schema | schema/ | The source publishes no schema. 196 verbatim regions (Tables 1–30, the §10 grammars, armor, cleartext and regex syntax, every field list and encoding), each with line range and sha256. Derived: a JSON Schema for a decoded packet stream, ABNF for the §10 sequences and the text formats, and validate.derived.py, which passes all 14 Appendix A blocks. |
| messages | messages.yaml | 119 structures and 276 fields: every packet type and version, every signature and User Attribute subpacket, S2K specifiers, algorithm-specific key, signature and session-key fields, EC encodings, and 15 computed structures (hash inputs, fingerprint input, HKDF info, AEAD additional data, KDF and key-wrap inputs, PKCS#1). 413 of 421 requirements wired, 8 not wired with a reason. 31 source defects. Excluded: the §10 sequences (protocol.yaml, schema ABNF), cryptographic primitives, keyring storage. |
| protocol | protocol.yaml, protocol.md | Partial by the source's nature: a data format with no wire protocol. 12 roles, 18 flows with 121 steps (construction, transfer and consumption of messages, signatures, keys, certifications and revocations), 13 algorithms with 76 steps, 33 error paths, 28 source defects and ambiguities, 16 not-defined items. 77 message names, each mapped to messages.yaml or a schema grammar. protocol.md has 31 Mermaid diagrams (18 sequence, 13 flowchart), not rendered. |
| state-machine | state-machine.yaml | 16 machines, 114 states, 186 transitions (51 inferred), 34 events: packet framing, the §10 message, detached-signature and key grammars, signature verification, key, subkey, User ID and certification validity, trust-signature chains, session-key recovery, v1 and v2 SEIPD decryption, secret-key unlock, armor and the Cleartext Signature Framework. Every trigger is a messages.yaml entry or a named event. 40 open questions. |
| examples | examples/ | 39 fixture files, every armored block, hex dump and annotated dump in Appendix A. 127 vectors: 60 in-source (25 Appendix A, 35 body examples) and 67 constructed, all verified for bytes and cryptographic properties. Not verified: algorithms the source gives no example for, and the behavioural outcomes of constructed vectors, which no implementation has run. |
| design-notes | design-notes.md | 17 notes against ARCH-0001, ARCH-0002, ADR-0001, DECISIONS-0001 and the 2026-09-28 minute: trust signatures against R-I-04, R-M-04 and R-M-10, regex scoping against R-M-08, DEC-004 and DEC-008, trust roots, revocation against R-O-02, fingerprints against DEC-003, D-3's packet encoding. 11 adopt, 9 adapt, 14 reject, a mapping row per bears_on id, 12 open questions with the source gaps passes 1 to 3 found. Decides nothing. |

---
schema: "library-distilled/v1"
id: omb-m-22-18-protocol
record: omb-m-22-18
type: protocol
updated: "2026-10-02"
reviewed_by: ""
---

# OMB M-22-18 — exchanges (protocol view)

Machine form: `protocol.yaml`; messages: `messages.yaml`. Rescinded 2026-01-23 (omb-m-26-05).
The memo is policy, not a wire protocol: the "messages" are documents exchanged between
parties, and there is no transport, encoding or timeout except the 30-day lead time on
extension/waiver requests.

```mermaid
sequenceDiagram
    autonumber
    participant A as Agency (CIO/CAO)
    participant P as Software producer
    participant X as 3PAO / approved assessor
    participant O as OMB
    participant C as CISA
    O->>C: repository requirements (§III.B.2, +180d)
    C-->>A: common self-attestation form (§III.C.1, +120d)
    A->>P: requirements notice, early / pre-solicitation (§II.2.f)
    A->>P: request confirmation of secure development practices (§II)
    alt full self-attestation
        P->>A: self-attestation (name, product scope, statement) or public link (§II.1.b-c)
    else third-party assessment (in lieu, or required by criticality)
        X->>A: assessment against NIST Guidance (§II.1.d, §II.1.c.iv)
    else cannot attest to some practices
        P->>A: practices not attested + mitigations + POA&M (§II.1.a.ii, never posted publicly)
        A->>A: satisfactory? then may use (§II.1.a.ii)
    end
    opt artifacts as needed (§II.2)
        A->>P: SBOM / other artifacts / VDP evidence request
        P->>A: SBOM (NTIA format) / artifacts / VDP evidence
    end
    opt cannot meet a deadline
        A->>O: extension or waiver request, >= 30 days before deadline, with plan (§III.A.6-7)
        O-->>A: decision (waiver: with APNSA, case-by-case)
    end
```

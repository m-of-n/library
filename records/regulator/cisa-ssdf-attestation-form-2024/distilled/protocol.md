---
schema: "library-distilled/v1"
id: cisa-ssdf-attestation-form-2024-protocol
record: cisa-ssdf-attestation-form-2024
type: protocol
updated: "2026-10-02"
reviewed_by: ""
---

# Attestation form — submission protocol

Machine form: `protocol.yaml`. Since 2026-01-23 (omb-m-26-05) agencies *may* still use the form,
but no agency is required to collect it; the flows are unchanged when it is used.

```mermaid
sequenceDiagram
    autonumber
    participant A as Agency
    participant P as Software producer
    participant S as Signatory (CEO/designee)
    participant X as 3PAO
    participant R as CISA RSAA (softwaresecurity.cisa.gov)
    participant O as OMB
    A->>P: agency-unique Privacy Act Statement (+ optional agency-specific instructions)
    alt self-attestation (all 12 Section III items)
        S->>R: form v1.0, all fields complete, signed (new | revised)
        Note over R,A: delivery from RSAA to agency not described (inferred)
    else cannot use the online form
        A->>P: agency email address
        S->>A: PDF Producer_Product_Version_YYYYMMDD
    else third-party assessment
        X->>P: assessment against NIST Guidance covering all form elements
        P->>A: form with 3PAO box checked + assessment attached (no signature)
        A->>A: keep assessment non-public
    else cannot attest to some practices
        P->>A: practices not attested + mitigations + POA&M
        A->>O: extension or waiver request (per OMB guidance)
        P->>R: later: "Attestation Following Extension or Waiver"
    end
    opt practices lapse (binding across future versions until notified)
        P->>A: notify every agency that received the form
    end
    Note over A: incomplete form -> not accepted; missing information -> agency may stop using the software
```

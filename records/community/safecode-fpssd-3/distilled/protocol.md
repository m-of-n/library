---
schema: "library-protocol-view/v1"
id: safecode-fpssd-3-protocol
record: safecode-fpssd-3
type: protocol
updated: "2026-10-02"
---

# Vulnerability response exchange (SAFECode FPSSD 3rd ed.)

See `protocol.yaml` for the verbatim text behind each message.

```mermaid
sequenceDiagram
  participant Rp as Reporter / researcher / customer
  participant P as PSIRT
  participant D as Owning dev team
  participant Dep as Dependent teams
  participant C as Customers
  Rp->>P: Vulnerability report (confidential channel)
  P-->>Rp: Acknowledgement + expectations (+ info request)
  P->>D: Triage for validation and remediation
  loop while investigating
    P-->>Rp: Status update
  end
  D->>D: fix, fully test; identify mitigations/workarounds
  D->>Dep: notify (reused code)
  P->>C: Security advisory once fixes exist for all supported versions
  Note over P,C: if publicly disclosed or exploited, an advisory may precede the fix
```

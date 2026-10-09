---
schema: "library-doc/v1"
id: owasp-asvs-5-protocol
record: owasp-asvs-5
type: protocol
updated: "2026-10-02"
reviewed_by: ""
---

# ASVS 5.0.0 — verification engagement (protocol view)

Machine form: `protocol.yaml`. ASVS defines no wire protocol; it describes a verification engagement and a
procurement use in prose (Assessment and Certification; What is the ASVS? › Use cases). Step order is ours
where the source does not order it.

```mermaid
sequenceDiagram
    participant Org as Developing organization
    participant Ver as Verifier
    participant Con as Report consumer (buyer)
    participant Sel as Seller
    Note over Org: choose target level (F-09); tailor / fork scope (F-13, F-17)
    Org->>Ver: access to documentation, source, configuration, people
    Note over Ver: declare scope: level + requirements included (F-22, F-23)
    loop each in-scope requirement
        Ver->>Ver: verify -> pass / fail / not-applicable (F-03, F-21)
        Note over Ver: documentation and implementation checked separately (F-06)
    end
    Ver->>Con: verification report (scope, all checked, exceptions, N/A, remediation, methods) (F-20..F-25)
    Note over Con: decide level of trust in the application
    Con->>Sel: procurement: "developed at ASVS level X"
    Sel->>Con: proof that the software satisfies level X (a verification report)
```

Error paths: a failed requirement is reported as an exception with remediation guidance and blocks the
level (`state-machine.yaml`); N/A must be noted; an automated-tool-only run is insufficient (F-26); no party
may claim official OWASP certification (F-19).

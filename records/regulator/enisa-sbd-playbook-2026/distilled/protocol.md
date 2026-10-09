---
schema: "library-distilled/v1"
id: enisa-sbd-playbook-2026-protocol
record: enisa-sbd-playbook-2026
type: protocol
updated: "2026-10-02"
---

# ENISA SbD&D Playbook — flows

Details and constrained-by ids in `protocol.yaml`.

```mermaid
sequenceDiagram
  participant T as Team
  participant G as Release review / CI gate
  T->>G: changed components + threat model + risk register
  G->>G: select relevant release-gate criteria (unchanged = not affected)
  G->>G: evaluate pass/fail per playbook (4.1 ... 4.22)
  alt any fail
    G-->>T: no-go (or exception: rationale, owner, review date)
  else
    G-->>T: go; release security review record
  end
```

```mermaid
sequenceDiagram
  participant R as Reporter/scanner
  participant T as Team
  participant A as Authority
  participant C as Customers
  R->>T: report / finding
  T->>T: severity + internet-exposed + known-exploited
  T->>T: fix now | mitigate | accept (time-bound) | defer (rationale)
  T->>A: escalation for reporting obligations (if applicable)
  T->>C: advisory (CSAF/VEX where proportionate) + secure OTA
  T->>T: root cause -> risk assessment, requirements, practices
```

```mermaid
sequenceDiagram
  participant T as Manufacturer
  participant V as CI verification gates
  participant P as Public attestation layer
  participant O as Restricted overlay (TEA API)
  participant A as Assessor
  T->>V: control + implementation claims
  V-->>T: PASS/FAIL + evidence hash
  T->>P: signed claims, provenance
  T->>O: detailed evidence (authenticated)
  A->>P: read claims
  A->>O: fetch evidence (authorised)
  A->>A: spot checks (ls /bin/sh, ps aux, ssh with password, touch /usr/bin/test)
```

---
schema: "library-distilled/v1"
id: etsi-ts-104-219-protocol
record: etsi-ts-104-219
type: protocol
updated: "2026-10-02"
---

# ETSI TS 104 219: process flows

The SSDIF is a process framework and defines no wire protocol. The four flows below are put together from the task-table actions. Every step's `constrained_by` ids, and whether each step is stated or inferred, are in `protocol.yaml`.

## F1. Vulnerability disclosure and remediation (§5.6.0, RV.1.1 to RV.3.4)

§5.6.0 names three phases:
1. Immediate remediation.
2. Remediation of similar vulnerabilities.
3. A scheduled update of secure development practices.

```mermaid
sequenceDiagram
  participant R as Reporter
  participant S as Security Response Engineer
  participant T as Owning team
  participant DB as Vulnerability DB (CVE/GCVE)
  participant A as Acquirer
  participant SDL as SDL Team
  R->>S: report via visible location / confidential channel (RV.1.1)
  S->>T: initial triage: validate, prioritize, remediate (RV.1.2 #1)
  T-->>S: triage result (commonly within one week, RV.1.2 #2)
  T->>T: review source, plan update/mitigation (RV.2.1)
  T->>T: implement + test fix, assign criticality (RV.2.2 #1,#3)
  S->>DB: common identifier where possible (RV.2.2 #2)
  S->>A: advisory (CSAF ideally) + signed update (5.6.0; PS.2.1)
  T->>T: phase 2 variant review and fix (RV.3.3)
  T->>SDL: root cause, recurrence, trends (RV.3.1/3.2)
  SDL->>SDL: phase 3 update tools/training/threat models/defaults (RV.3.4, 5.6.0)
```

## F2. Threat modelling to fix (PW.1.1 DG3, PW.2.1)

```mermaid
sequenceDiagram
  participant Ar as Architect
  participant PM as Program Manager
  participant Dev as Software Engineer
  Ar->>Ar: DFD / initial description; must depict system accurately (#7, #8)
  Ar->>Ar: threats + severity; mitigate high & medium (#3, #4)
  Ar->>PM: bugs for high (shall) / medium (should) threats (#5, #6)
  PM->>Ar: independent design review minutes, design bugs (PW.2.1)
  Dev-->>PM: bugs marked "fixed" by code change (5.0.4)
```

## F3. Release gate by bug bar (PO.4.1, PW.8.2 DG3 #4, PS.2.1, PS.3.1)

```mermaid
sequenceDiagram
  participant SDL as SDL Team
  participant PM as Program Manager
  participant RE as Release Engineer
  participant C as Customer
  SDL->>PM: bug bar (severity levels, ship threshold)
  PM->>PM: open security bugs vs bar -> ship or delay
  alt finding above threshold
    PM-->>PM: delay release until fixed
  else
    RE->>RE: DG3 static analysis: no "shall fix" errors
    RE->>C: signed code (PS.2.1); archive release (PS.3.1)
  end
```

## F4. Third-party component acceptance (PO.1.3, PW.4.1, PW.4.4, PS.3.2)

```mermaid
sequenceDiagram
  participant P as Procurement
  participant PM as Program Manager
  participant RE as Release Engineer
  P->>P: security requirements in contracts/RFPs (PO.1.3)
  PM->>PM: TPC risk score: known vulns, maintainer maturity, EOL (PW.4.1 #1-#6)
  alt reported vulns unmitigated
    PM-->>PM: do not use / wrap / reduce privilege / accept (#7, #8)
  else
    PM->>RE: approved list + where-used SBOM (PS.3.2)
  end
  loop continuous
    PM->>PM: monitor TPC risk; revisit on each update (PW.4.4)
  end
```

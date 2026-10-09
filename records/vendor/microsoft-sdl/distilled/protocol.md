---
schema: "library-protocol-view/v1"
id: microsoft-sdl-protocol
record: microsoft-sdl
type: protocol
updated: "2026-10-02"
---

# Security exception exchange (practice 1.4)

Inferred from the seven steps of sub-practice 1.4; see `protocol.yaml` and
`state-machine.yaml`. The page gives steps, not messages, so the message names are
ours.

```mermaid
sequenceDiagram
  participant T as Engineering team
  participant P as Security program
  participant M as Management (level by severity)
  T->>T: 1. triage risk; document reason, short-term actions, remediation plan, expiry
  T->>P: 2. determine review level by severity
  T->>M: 3. ExceptionRequest via approval workflow
  M-->>T: 4. ExceptionDecision (approve / deny)
  loop until resolved or expired
    P->>P: 5. track to resolution or expiration
    P->>M: 6. ExceptionReview when risk changes
  end
  T->>M: 7. ExceptionRenewalRequest if expired before remediation
```

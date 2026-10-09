---
schema: "library-distilled/v1"
id: cisa-secure-by-design-pledge-2024-protocol
record: cisa-secure-by-design-pledge-2024
type: protocol
updated: "2026-10-02"
reviewed_by: ""
---

# Secure by Design Pledge — exchanges

```mermaid
sequenceDiagram
    participant M as Manufacturer
    participant C as CISA
    participant P as Public
    M->>C: sign-up email (enterprise software manufacturer; authority to commit)
    C-->>P: listed as pledge signer (inferred)
    Note over M: good-faith effort on 7 goals, 1 year
    alt measurable progress / already met
        M->>P: progress publication per goal (stats, blog, roadmap, VDP, CVE policy, log policy)
        C-->>P: link on progress-reports page (inferred)
    else no measurable progress
        M->>C: how it worked towards the goal + challenges
        opt radical transparency
            M->>P: publish approach
        end
    end
    Note over C: CISA does not enforce nor verify adherence (web page)
```

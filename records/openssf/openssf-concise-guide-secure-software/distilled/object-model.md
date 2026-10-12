---
schema: "library-doc/v1"
id: openssf-concise-guide-secure-software-object-model
record: openssf-concise-guide-secure-software
type: object-model
updated: "2026-10-02"
reviewed_by: ""
---

# Concise Guide for Developing More Secure Software — object model

Machine source: `object-model.yaml` (30 objects, 22 edges, 3 gaps; locators are item numbers).

```mermaid
graph LR
  Developer -- uses --> MFAToken
  CIPipeline -- runs --> SecurityTool
  Project -- depends_on --> Dependency
  Dependency -- managed_by --> PackageManager
  Dependency -- delayed_by --> Cooldown
  Vulnerability -- affects --> Dependency
  Repository -- guarded_by --> ChangeReview
  Repository -- excludes --> Secret
  SecurityPolicy -- documents --> Project
  Signature -- signs --> Release
  SBOM -- describes --> Release
  SecurityAdvisory -- announces --> Vulnerability
  Project -- earns --> BestPracticesBadge
  Project -- scored_by --> ScorecardScore
  Project -- at_level --> SLSALevel
  Project -- applies --> Guide
  Project -- audited_by --> SecurityAudit
  Project -- maintained_by --> Maintainer
  SourcePackage -- built_from --> Repository
  Project -- loads --> WebAsset
```

## Findings for tmodel

1. **A checklist of delegations.** Items 14, 15, 17 and 20–22 are satisfied by meeting *another*
   requirement set: the Best Practices badge, Scorecard, SLSA, CNCF, ASVS and SAFECode. A
   crosswalk (R-044) therefore needs an edge from a Requirement to a whole requirement set, as
   well as Requirement ↔ Requirement edges.
2. **Mitigation kinds (R-040).** The items span all three kinds. MFA, signing and pinning are
   technical. The security policy, advisories and SBOM are documentation. Review, cooldown,
   deprecation and succession are process.
3. **No phases or gates.** The guide is unordered, so it supplies requirement content but no SDL
   structure for R-041.

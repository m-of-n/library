---
schema: "library-summary/v1"
id: shor-1994
record: shor-1994
type: summary
updated: "2026-11-03"
---

# Algorithms for Quantum Computation: Discrete Logarithms and Factoring

|  |  |
|---|---|
| **Type** | paper (conference proceedings) |
| **Maturity** | _unset_: a peer-reviewed conference paper, so no standards-track level applies |
| **Authors** | P. W. Shor |
| **Published** | 1994-11, Proc. 35th FOCS (SFCS-94), Santa Fe, NM, 20–22 Nov 1994, pp. 124–134, IEEE Computer Society Press |
| **Identifier** | DOI 10.1109/SFCS.1994.365700 |
| **Source** | https://doi.org/10.1109/SFCS.1994.365700 (IEEE Xplore, paywalled) |
| **Digest** | none. **Not fetched**: doi.org and IEEE Xplore returned an empty HTTP 202 to our client on 2026-11-01 |

## Overview

**This record has not been read.** The FOCS 1994 text is paywalled. Per `docs/scope.md` §1 ("Paywalled work is recorded"), the record stays a `stub` and carries the locator and bibliographic facts only. Those facts come from Crossref and from the first-page footnote of the expanded version, `shor-1997` (arXiv:quant-ph/9508027v2). That footnote calls this paper *"A preliminary version of this paper"*, and the arXiv comments call the 1997 paper *"an expanded version"* of it.

We therefore know what this paper introduced only through its successor: polynomial-time quantum algorithms for integer factoring and discrete logarithms. We do not know how its proofs, bounds or wording differ from the 1997 text. `shor-1997`'s acknowledgements thank J. Lagarias for *"finding and fixing a critical error in the first version of the discrete log algorithm"*. We cannot tell from what we hold whether that "first version" is this proceedings paper or an earlier draft.

**For the `post-quantum-migration` question**, this record's contribution is the *date*: the attack that every post-quantum path in this library answers has been public since November 1994. Cite `shor-1997` for content.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | The origin of the quantum threat to factoring- and discrete-log-based public-key cryptography (per `shor-1997`) |
| Cryptography | `core` | Same result, cited for priority |
| This project | `adjacent` | The reason for any post-quantum requirement we may adopt. No such requirement exists yet |

**Bears on none yet.** ARCH-0001 §5 has no post-quantum or algorithm-agility requirement, and NG3 lists freezing the algorithms as a non-goal. Once a requirement exists, the paper's content reaches it through `shor-1997`.

## Implementations

Searched 2026-11-03. Implementations of Shor's algorithm (e.g. in Cirq and Qiskit) implement the algorithm, not one version of the paper; any are recorded on `shor-1997`, not here.

| Name | Kind | License | URL |
|---|---|---|---|
| _see `shor-1997`_ | | | |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata: bibliographic facts from Crossref and the `shor-1997` first-page footnote, with the paywall and the nearest open text noted in `content.note` |
| `summary.md` | this document |

**No digest and no `distilled/`.** No bytes of the proceedings paper were obtained, so nothing could be digested. A digest needs a legitimate copy of the proceedings text, which would also move this record past `stub`. The DIMACS technical report TR 94-37 named in `content.note` has a similar title but is a different document; its digest is not this record's. A `paper` record owes no FX-1 extraction.

## Limits

- **Unread.** Everything in Overview about content comes from `shor-1997`. Differences between the two versions are unknown, including whether the discrete-log error Lagarias fixed is in this text.
- **No digest.** A reader cannot verify which bytes this record describes. Only the DOI fixes the document.
- **Relation to `shor-1997`.** The two are separate records because they have different titles, venues and DOIs, and both are cited in the literature. `shor-1997` carries `supersedes: [shor-1994]`; this record authors no edge to it, since the inverse is derived (`docs/references.md` §2).

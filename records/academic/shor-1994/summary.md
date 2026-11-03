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
| **Digest** | none. **Not fetched**: IEEE Xplore returned no bytes to a scripted fetch on 2026-11-03 |

## Overview

**This record has not been read.** The FOCS 1994 text is paywalled. Per `docs/scope.md` §1 ("Paywalled work is recorded"), the record stays a `stub` and carries the locator and bibliographic facts only. Those facts come from Crossref and from the first-page footnote of the expanded version, `shor-1997`. That footnote calls this paper *"A preliminary version of this paper"*, and the arXiv comments call the 1997 paper *"an expanded version"* of it.

We therefore know what this paper introduced only through its successor: polynomial-time quantum algorithms for integer factoring and discrete logarithms. We do not know how its proofs, bounds or wording differ from the 1997 text. `shor-1997`'s acknowledgements thank J. Lagarias for *"finding and fixing a critical error in the first version of the discrete log algorithm"*. We cannot tell from what we hold whether that "first version" is this proceedings paper or an earlier draft.

**For the `post-quantum-migration` question**, this record's contribution is the *date*. The attack that every post-quantum path in this library answers has been public since November 1994. Any attestation format designed after that date with no stated post-quantum path made that choice knowingly. Cite `shor-1997` for content.

## Applicability

| Axis | Rating | Why |
|---|---|---|
| Security | `core` | The origin of the quantum threat to factoring- and discrete-log-based public-key cryptography |
| Cryptography | `core` | Same result, cited for priority |
| This project | `adjacent` | The reason for any post-quantum requirement we may adopt. No such requirement exists yet |

**Bears on none yet.** ARCH-0001 §5 has no post-quantum or algorithm-agility requirement, and NG3 defers the algorithm suite. `research/0003-cipher-suite` does not choose a signature algorithm, and DEC-002 is an encoding decision. Once a requirement exists, the paper's content reaches it through `shor-1997`.

## Implementations

Searched 2026-11-03. Implementations of Shor's algorithm (Cirq, Qiskit) are listed on `shor-1997`. They implement the algorithm and do not cite one version of the paper over the other.

| Name | Kind | License | URL |
|---|---|---|---|
| _see `shor-1997`_ | | | |

## Artifacts in this record

| File | What it is |
|---|---|
| `record.yaml` | metadata: bibliographic facts from Crossref, with the paywall noted in `content.note` |
| `summary.md` | this document |

**No digest and no `distilled/`.** No bytes were obtained, so nothing could be digested. A digest needs a legitimate copy of the proceedings text, which would also move this record past `stub`. A `paper` record owes no FX-1 extraction.

## Limits

- **Unread.** Everything in Overview about content comes from `shor-1997`. Differences between the two versions are unknown, including whether the discrete-log error Lagarias fixed is in this text.
- **No digest.** A reader cannot verify which bytes this record describes. Only the DOI fixes the document.
- **Relation to `shor-1997`.** The two are kept as separate records because they have different titles, venues and DOIs, and both are cited in the literature. `shor-1997` carries the `supersedes` edge. Under `docs/references.md` §3 they could be argued to be one document line, but that restructure is not made here, because ids are stable.

---
record: rfc-8747
kind: schema
title: "rfc-8747 — schemas"
extracted: "2026-10-21"
reviewed_by: ""
---

# RFC 8747 — schemas

**RFC 8747 ships no formal grammar of any kind.** Measured over the whole
683-line source: `schema`, `grammar`, `ABNF` and `ASN.1` occur **zero** times,
`JSON Schema` **zero** times, and `CDDL` **once** — at line 630, inside the
reference entry for RFC 8610, which this document cites for its Appendix G
diagnostic notation and nothing else. So every formal artifact here except the
verbatim capture is **ours**, and says so in its filename.

| file | what it is | verbatim or derived |
|---|---|---|
| `source-renderings.txt` | Table 1 (§3.1) and the **three** IANA blocks (§7.1.1, §7.2.1, §7.2.2) — **four** verbatim regions in all — as exact source line runs with per-region `sha256` | **verbatim** |
| `cnf-claim.derived.cddl` | the `cnf` claim and its three confirmation methods as a CDDL grammar | **derived** |
| `cnf-claim.derived.schema.json` | the same over a declared lossy JSON projection; `$id: urn:library:rfc-8747:cnf-claim.derived` | **derived** |
| `confirmation-methods.derived.yaml` | both registries as machine-readable fields, each wired to its requirement id | **derived** |

The document's **complete** structured type model is Table 1's three data rows
plus the three IANA blocks. That is what `source-renderings.txt` holds, in four
verbatim regions: **11** source lines of table (§3.1, lines 192–202) and **76**
of registration material (§7.1.1 lines 470–484, §7.2.1 lines 493–526, §7.2.2
lines 528–554). *Counted as raw source lines including blanks; non-blank, it is
10 and 59. The figures that stood here — "eighteen lines of table and sixty-six
of registration template" — are produced by no counting of the ranges this file
declares, and the method is now stated so the next pass can tell a fossil from
a lie (`hazards.md` §6).*

## Does the CDDL bind, or merely parse?

No `cddl` tool is installed here, so this is **not** a parse result. A checker
was transcribed from `cnf-claim.derived.cddl` rule by rule and run over the
instances below. `hazards.md` §7 is the reason:
`rfc-9360`'s derived CDDL parsed perfectly for two passes and constrained
nothing, because a `* label => any` wildcard in the same map satisfied every
item its rule rejected.

**Pass 2 found the mirror-image defect in the first version of this grammar,
and it is fixed.** `other-label` claimed to write out the complement of
`{1, 2, 3}` but enumerated only integer and text keys, so the socket **rejected**
a byte-string, boolean, array, map, tagged or bignum map key. CBOR admits any
data item as a map key, and `rfc-8747#R-0025` requires a member we do not
understand to be *ignored* — i.e. tolerated — so that grammar bound **more**
than the document does. Not a schema that fails to constrain, but one that
constrains what the source leaves open, on this record's own central subject.
The rule now names the remaining major types (`bstr` and `#4`/`#5`/`#6`/`#7`),
which is exhaustive; `other-claim-label` had the same defect and the same fix.

**And the cross-check pass found the SAME defect one rule later**, which pass 2
had not reached: `cwt-claims-set-fragment` wrote `8 ^ => cnf-claim` with no `?`,
so it **rejected `{1: "iss"}` and `{}`** — a CWT Claims Set carrying no `cnf`.
Nothing in RFC 8747 requires one. §3 is conditional (*By including a "cnf"
(confirmation) claim in a CWT, the issuer of the CWT declares…*), §7.1.1 only
**registers** the claim, and `messages.yaml` already gave claim key 8
`required: false` — so the grammar and the message model disagreed, and the
grammar was the one that was wrong. Key 8 is now optional; what the rule still
binds is the **type** of its value, by the cut, so `{8: {1: …, 2: …}}` and
`{8: 5}` are still rejected. The table below was re-run after both changes.

**The instance this grammar exists to reject**, written down before it was
tested:

```
{ 1: <COSE_Key>, 2: <COSE_Encrypt0> }
```

| instance | expected | got |
|---|---|---|
| §3.2's own `cnf` — `{1: COSE_Key}` | accept | **accept** |
| §3.3's own `cnf` — `{2: [protected, unprotected, ciphertext]}` | accept | **accept** |
| §3.4's own `cnf` — `{3: h'dfd1…'}` | accept | **accept** |
| `{3: kid, 5: …}` — an unknown member (key 5 is RFC 9679's `ckt`) | accept | **accept** |
| `{}` — the empty `cnf` | accept | **accept** |
| `{1: COSE_Key, 3: kid}` | accept | **accept** |
| **`{1: COSE_Key, 2: COSE_Encrypt0}`** | **reject** | **reject** |
| `{3: "dfd1aa97"}` — `kid` as a text string | **reject** | **reject** |
| `{2: COSE_Encrypt0, 1: "nonsense"}` | **reject** | **reject** |
| `{1: COSE_Key, 2: COSE_Encrypt0, 9: 1}` | **reject** | **reject** |
| `{2: 16(COSE_Encrypt0)}` — the tag carried | accept | **accept** |
| `{4: 1}`, `{0: 1}`, `{-1: 1}`, `{2^64-1: 1}` | accept | **accept** |
| `{"COSE_Key": COSE_Key}` — a text key is an unknown member | accept | **accept** |
| `{1: COSE_Key, 1: COSE_Key}` — duplicate key 1 | **reject** | **reject** |
| `{3: kid, 3: kid}` — duplicate key 3 | **reject** | **reject** |
| `{3: [kid]}` — `kid` as an array | **reject** | **reject** |
| `{h'00': 1}`, `{true: 1}`, `{[1]: 1}`, `{{}: 1}` — non-integer keys | accept | **accept** |
| `{2(bignum): 1}`, `{null: 1}`, `{undefined: 1}`, `{1.5: 1}` | accept | **accept** |
| `{1: 42}` — a wrongly typed `COSE_Key`; the cut is **inert** here | accept | **accept** |
| `{2: "nonsense"}` — a wrongly typed `Encrypted_COSE_Key`; inert too | accept | **accept** |
| `{8: {3: kid}}` — the CWT Claims Set fragment | accept | **accept** |
| `{8: {3: kid}, h'00': 1}` — fragment, non-integer claim key | accept | **accept** |
| `{1: "iss"}` — a Claims Set with **no** `cnf` | accept | **accept** |
| `{}` — an empty Claims Set | accept | **accept** |
| `{8: {1: COSE_Key, 2: COSE_Encrypt0}}` — fragment, bad `cnf` | **reject** | **reject** |
| `{8: 5}` — `cnf` value not a map | **reject** | **reject** |
| `{8: cnf, 8: cnf}` — duplicate claim key 8 | **reject** | **reject** |

**36 of 36 behave as the grammar claims** — **26** accept-expected and **10**
reject-expected, counted by expanding every row of the table above into its
individual instances (several rows carry four). The figure that stood here was
**30 of 30** against a table that already enumerated **31**, and "the eight
accepts in the last four rows" named rows that were no longer the last four:
pass 2 added rows without recounting them, which is `hazards.md` §6's rule
about any pass that edits an artifact. The eight accepts the first version of
`other-label` wrongly rejected are the two **non-integer-key** rows
(`{h'00': 1}` … and `{2(bignum): 1}` …), named by content rather than by
position so the sentence cannot go stale again. Five instances were added by
the cross-check pass: the two inert-cut rows, `{}` and `{1: "iss"}` as Claims
Sets, and `{8: 5}` and the duplicate claim key 8.

And the vacuity probe, re-run: a naive rendering — optional entries for 1, 2
and 3 beside an unrestricted `* label => any` in the same map, and the fragment
written the same way — wrongly **accepts 10 of the 10** rejects. Every one of
them. With key 8 optional there is no longer a reject a wildcard rendering gets
right by accident (the figure that stood here, *7 of the 8*, excused itself with
"the fragment missing key 8, which no wildcard can supply" — and that instance
is precisely the one the document never licensed rejecting). Two devices are
what make the real grammar bind, and both were tested rather than assumed:

1. **The cut operator `^ =>`** on every named entry, so a wrongly typed value
   under a known label cannot fall through to the wildcard.
2. **`other-label` excludes 1, 2 and 3 by construction, and nothing else** —
   written out as `0 / nint / (4 .. 18446744073709551615) / tstr / bstr /
   #4 / #5 / #6 / #7`, because CDDL has no negation on literals. This is what
   stops the extension socket absorbing a *second* key representation. The
   trailing major-type alternatives are what make it the WHOLE complement:
   without them the rule excluded far more than three labels, which is the
   defect recorded above.

### Where the cut is inert, said plainly

On keys **1 and 2** the cut currently bites on nothing, because RFC 8747 defines
no `COSE_Key`, `COSE_Encrypt` or `COSE_Encrypt0` grammar — §3.2 and §3.3 name
them and cite RFC 8152 — so those three rules are sockets typed `any`. For those
two labels the whole of the constraint is carried by `other-label`'s exclusion,
not by the cut. The cut does real work on key **3** alone, where Table 1 gives a
value type: it is what rejects `{3: "dfd1aa97"}`. Keeping `^ =>` on 1 and 2 is
deliberate anyway — the moment a later pass or a sibling record supplies a real
`COSE_Key` rule, the entry binds without being rewritten — but a reader should
not be left thinking it binds today.

**The instance that proves it, because a concession without one is not
testable** (`hazards.md` §7 asks for the instance a schema must reject; its dual
is the instance a schema *cannot* reject): `{1: 42}` and `{2: "nonsense"}` both
**accept**, and the table above now says so. Note that the nearby row
`{2: COSE_Encrypt0, 1: "nonsense"}` rejects for **co-presence of 1 and 2**, not
because key 1's value is wrongly typed — it is the single-key rule firing, and
a reader could otherwise take it for a type constraint on key 1 that does not
exist. On the fragment the cut is **not** inert: `cnf-claim` is a real rule, so
`{8: 5}` and `{8: {1: …, 2: …}}` both reject.

### What the grammar deliberately does not constrain

- **The empty map.** rfc-8747#R-0023 — §3.1 puts the set
  of members a CWT must contain *outside the scope of this specification*, so
  `{}` is not excluded by this document.
- **The presence of the `cnf` claim at all.** Claim key 8 is `?` in
  `cwt-claims-set-fragment`. §3 only says what including it *declares*, and
  §7.1.1 only registers it; no sentence makes a CWT carry one. `messages.yaml`
  says the same thing in its own vocabulary — claim key 8, `required: false`.
- **`kid` beside a key representation.** §3.1 restricts `COSE_Key` against
  `Encrypted_COSE_Key` and says nothing about `kid`; rfc-8747#R-0040
  explicitly allows a `kid` *inside* a `COSE_Key`. Forbidding `{1: …, 3: …}`
  would be this library's rule, not the document's.
- **The tag on a `COSE_Encrypt0`.** rfc-8747#R-0117
  makes it optional and §3.3's example omits it, so **both** forms are admitted
  here. That is not neutrality, it is the finding: one `cnf` has two encodings
  and this registry entry does not choose between them. See `design-notes.md`.
- **Map entry order.** The words `canonical` and `deterministic` occur **zero**
  times in the source. `examples/vectors.yaml` records what that costs: the
  document's own §3.3 ciphertext does not reproduce from its own printed
  COSE_Key, because the two differ in entry order alone.

### The JSON Schema's projection is lossy, and declared

`cnf-claim.derived.schema.json` works over a JSON projection in which an integer
confirmation key becomes its decimal string and a CBOR byte string becomes
lowercase hex. CBOR distinguishes integer key `1` from text key `"1"` and JSON
cannot, so **that schema cannot express RFC 8747's key space** and the CDDL is
normative for this extraction. The one construct in it that genuinely binds is
the `not`/`required` pair encoding rfc-8747#R-0029.

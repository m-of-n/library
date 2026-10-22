---
schema: "library-doc/v1"
id: rfc-8747-protocol
record: rfc-8747
type: protocol
updated: "2026-10-21"
---

# RFC 8747 — protocol model

**Three roles, no exchange, and the gap is the document's own.** This is the
only record in library#39's CBOR/COSE set whose source names parties and still
has no flow to model. Every other lane record without a protocol lacks one
because the document has no word for any party; this one names three and then
withholds the messages between them.

Measured whole-word and case-insensitively over all 683 lines: `presenter`
**18**, `recipient` **14**, `issuer` **8**, `party` **8**, `parties` **7**.
Against that: `response` **0**, `handshake` **0**, `negotiate` **0**, `sender`
**0**, `verifier` **0**, `round` **0**; `protocol` **2** — one of them inside
§3.5's own disclaimer — `exchange` **2**, `message` **4**, `nonce` **3**,
`challenge` **1**.

## The three roles

| role | named | does | obligations |
|---|---|---|---|
| **issuer** | 8× | Creates the CWT and declares the presenter possesses a key, via `cnf` | 2, both lower case |
| **presenter** | 18× | Possesses the key and demonstrates possession | **none** |
| **recipient** | 14× | Obtains or decrypts the key and confirms possession | 5 |

**The most-named party carries none of the document's eight BCP 14 keywords.**
§3.5 describes how possession is *"often demonstrated"* — the presenter signs a
value determined by the recipient — and then declines to specify any of it.

## Why there is no flow

§3.5 is titled *"Specifics Intentionally Not Specified"*, and it removes both
halves of the exchange that would constitute one:

> The means of communicating the nonce and the nature of its contents are
> intentionally not described in this specification, as different protocols
> will communicate this information in different ways.

> Likewise, the means of communicating the signed nonce is also not specified,
> as this is also protocol specific.

So the document defines a key **representation** and leaves the **proof**
entirely to the application. `protocol.yaml` records both absences as
`declared_absences` with their requirement ids rather than modelling a
plausible sequence, because a plausible sequence would be ours.

**No Mermaid diagram, deliberately.** There is no sequence to draw. A diagram
of challenge → signed-response would be this library's invention presented as
the document's, which is the defect class `hazards.md` §2 exists for.

## What the absence costs, and where it is followed up

An application adopting `cnf` supplies the whole challenge mechanism itself,
and nothing here constrains its freshness, its encoding, or its binding to the
key. The document acknowledges alternatives and pushes them to a registry:
other means of proving possession exist (`rfc-8747#R-0066`) and applications
using them are *encouraged to register* them in the registry §7.2 establishes
(`rfc-8747#R-0067`).

That is worth noticing rather than passing over: **the extension point for the
missing half of this protocol is a registry** — which is the shape
`ARCH-0002 P1` rejects. `design-notes.md` takes it from there.

## The nearest thing to an error path

A Key ID collision (§3.4, §6). Its consequence is stated as a risk — *"may
allow one party to impersonate another party, with the potential to gain
additional privileges"* — with no detection step, no actor obliged to act and
no recovery. `error_paths` is therefore empty, and `protocol.yaml` says why
rather than leaving the reader to wonder whether the sweep missed something.

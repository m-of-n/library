---
record: cisa-secure-by-demand-ot-2025
kind: examples
title: "cisa-secure-by-demand-ot-2025 - examples and test vectors"
extracted: "2026-11-15"
reviewed_by: ""
---

# examples/

**Finding: the guide has no worked example, test vector or sample record.** Counted by script over the pinned
rendering: 7 lines carry For example or Examples of, and each is a narrative illustration inside prose,
with no input, no expected result and no data to turn into a fixture. They are marked below so a reader can
see that nothing was dropped; the e.g. and i.e. lists are enumerations inside sentences and are not examples
in this sense.

<!-- q L324-325 "For example, immutable" .. "hot-swapping containers." -->
> For example, immutable containers would allow operators to make configuration changes with minimal downtime by hot-swapping containers.

<!-- q L533-535 "For example, instead of replacing" .. "securely by default." -->
> For example, instead of replacing all the devices in a portion of the system at once, an owner/operator could deploy a newer secure device with an embedded protocol gateway that translates it to observed legacy devices while still communicating securely by default.

<!-- q L614-616 "For example, existing protocols" .. "against the system." -->
> For example, existing protocols include commands to take control from the main computer or disable other computers in case of failure, such as a stuck transmitter. A threat actor can recreate those conditions or send a command to weaponize safety features against the system.

<!-- q L625-627 "For example, a manufacturer could document" .. "active scanning." -->
> For example, a manufacturer could document how a component responds if another device impersonates it, how it verifies error states and diagnostic commands, or how it handles active scanning.

<!-- q L632-635 "Examples of system specifications" .. "mid process." -->
> Examples of system specifications being broken include: a singular Modbus client or bus controller being impersonated, network arbitration designed to disable an existing system such as a new engine appearing while a vehicle is in operation, or maintenance commands and updates mid process.

<!-- q L675-679 "For example, in the Freight Rail" .. "enhances safety." -->
> For example, in the Freight Rail Subsector it is commonplace for wayside interface units to require a local button press on the controller and a dynamic code along with a password to change vital (safety-critical) signaling logic. It would be simpler for rail companies to change safety-critical logic without having a signaling engineer drive out to a waystation, but requiring a signaling engineer to press the physical button reduces risk and enhances safety.

<!-- q L845-847 "For example, a patch may be" .. "engineering logic." -->
> For example, a patch may be incompatible with another piece of software, or a patch may overwrite the asset owner’s configurations or engineering logic.


What is held here is ours, marked `.derived.`: 12 instances the derived schemas must accept and 51 they must
reject. Each file is `{schema, expect, why, instance}`. The twelve real consideration sections are not copied: they
are parsed from the pinned source and validated by `../schema/check.derived.py`.

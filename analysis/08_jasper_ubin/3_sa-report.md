# SA INWARD NOTE — Jasper–Ubin (2019) [id P8]
## 1. Executive Summary
[id P8] BoC and MAS proved a CAD-SGD atomic settlement across Corda and Quorum using HTLCs — no trusted intermediary, all-or-nothing by construction. The honest core: trust was moved into the technical system, not eliminated, and the method is inherently bilateral. The report's open-questions list (governance, legality, scale) defines the agenda the next five years of BIS-track work (Dunbar, Mandala, Cedar×Ubin) worked through without fully closing.
## 2. Entity Map
BoC (Hendry) | MAS (Mohanty) | JPM | Accenture. JPM's recurrence across Ubin P5/Onyx/Partior makes it the constant private node in public corridor research.
## 3. Mechanics
[id P8] Lock asset → disclose secret → claim; timeout releases encumbrance on failure. Platforms must support encumbrance, secret disclosure, timeout — the minimal interop contract.
## 4. Pattern
[id P8] Bilateral corridor model; N² scaling ceiling; successor projects fork by strategy. Cedar×Ubin [id P11] re-runs the same primitive with the NY Fed in 2022 — validation politics as much as research.
## 5. Quantification
None published on cost/latency vs correspondent baseline — the omission that recurs until Cedar×Ubin's sub-30s claim.
## 6. Bull / Base / Bear
Bull: corridor mesh of bilateral HTLC links — did not emerge. Base: primitive banked; platform/compliance tracks take over. **Realised.** Bear: interop stalls entirely — avoided.
## 7. Open Threads
Timeout-parameter risk analysis — still unpublished anywhere in the corpus. Governance of cross-sovereign protocol updates — inherited by GL1, unresolved.
## 8. Sources
[id P8] papers/08, primary. Cross: [id P9][id P11][id P14].

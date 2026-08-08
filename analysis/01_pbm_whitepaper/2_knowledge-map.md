# KNOWLEDGE MAP — 01 PBM Technical Whitepaper

## Executive Summary (Alphas)
**Alpha 1 — The wrapper IS the policy surface.** Every constraint citizens experience (expiry, merchant lists, denominations) lives in the wrapper, authored by the PBM Creator. The money layer is deliberately kept dumb. Whoever writes the wrapper writes the policy.
**Alpha 2 — Revocation exists in the reference design.** Fig 15: the creator can revoke expired PBMs and recover the collateral. "The system cannot override an expiry" is therefore an implementation omission or an operating-policy stance — never a protocol impossibility.
**Alpha 3 — The privacy split is the pre-built defence.** Creator ≠ issuer separation is MAS's engineered answer to the "surveillance money" attack line — built before the attack arrived. That tells you MAS war-gamed public sentiment years ago.

## 4-Quadrant Matrix
**KNOWN KNOWNS:** Wrapper+collateral architecture · 4-layer stack (access/service/asset/platform, co-designed with IMF) · lifecycle incl. Expired stage · ERC-1155 wrapper over ERC-20 money · roles (Creator/Holder/Redeemer) · use cases (vouchers, escrow, trade finance, donations, cross-border).
**KNOWN UNKNOWNS (flagged in-paper):** account abstraction · offline/card form factors · name addressing · cross-jurisdiction regulatory treatment · oracle governance · which ledger types qualify.
**UNKNOWN KNOWNS (structural context the paper stands on):** MAS's 2021 finding of no retail-CBDC case (the reason PBM works over private money) · the 8%/92% cash-deposit split — PBM protects bank deposits' role · ERC-7291 standardisation trajectory · RedeemSG/CDC voucher machinery as the live testbed.
**UNKNOWN UNKNOWNS (semantic gaps the paper never joins):**
- *Expiry economics.* Nowhere does the paper discuss who benefits from breakage — expired value reverts to the Creator (the state, in disbursements). PBM makes breakage revenue programmable and precise. No MAS document names this.
- *Contestability gap.* The lifecycle has no dispute/appeal state. A holder facing expiry has no protocol-level recourse — appeals live entirely off-chain in administrative discretion. The architecture silently assumes the citizen's remedy is bureaucratic, not technical.
- *Wrapper authorship as delegated legislation.* Conditions in a government PBM are rules with force, authored as code by agencies/vendors without the scrutiny statutory instruments get. The paper's "policy considerations" section gestures at this but never lands it.

## Narrative Vector
The paper **validates** its own premise (conditions without programming the money) but **shifts** the real question: from "can money be programmed" to "who governs the wrapper." The blind spot is contestability — the citizen-facing states (Expired, blacklisted) have no counterpart rights framework. For the MAS mandate: public-sentiment risk concentrates exactly where the whitepaper is silent.

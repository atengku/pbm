# SA INWARD NOTE — Cedar II × Ubin+ (2022) [id P11]
## 1. Executive Summary
[id P11] The NYIC-MAS experiment settled simulated multi-hop, vehicle-currency FX chains atomically across heterogeneous ledgers in under 30 seconds using HTLCs. As research it extends Jasper–Ubin incrementally; as statecraft it pairs MAS with the NY Fed on the design of dollar-bridged wholesale settlement and aims squarely at the illiquid EME corridors that correspondent de-risking abandoned. The report's disclaimers are the loudest in the corpus — no policy signal intended — which is itself the signal of how sensitive Fed-adjacent CBDC work is.
## 2. Entity Map
FRBNY NYIC (BISIH partnership) | MAS Ubin+ | prior nodes: [id P8] method, [id P9] problem set.
## 3. Mechanics
[id P11] Illiquid pair routed via vehicle currency; each leg an HTLC; claims mutually conditional → chain-wide atomicity; <30s all scenarios; Sepolia testnet (public — privacy explicitly unsolved); PTLC/ZKP future work.
## 4. Pattern
[id P11] Third HTLC validation in the corpus (after [id P8], echoing [id P7] locks) — the primitive is settled science; the variable is the partner. Corridor diplomacy sequence: Canada (2019) → USA (2022). EME-pair framing answers [id P9]'s de-risking datum.
## 5. Quantification
<30s settlement across all 11 scenarios; system metrics on 2vCPU/8GB VMs (toy scale, honestly labelled). No spread/liquidity economics — structurally out of scope.
## 6. Bull / Base / Bear
Bull: architecture informs a production USD-bridge wholesale network with MAS-regulated nodes. Base: findings feed BISIH successors (Agorá-class work); no deployment. **Base likely.** Bear: US retail-CBDC politics freezes Fed-adjacent work; the partnership's option value expires.
## 7. Open Threads
Successor programme mapping (Ubin+ → what, NYIC → Agorá?) — refresh search. Liquidity-provision economics of on-chain vehicle legs — unowned question, advisory whitespace.
## 8. Sources
[id P11] papers/11, primary. Cross: [id P8][id P9][id P14], BIS PvP adoption paper (cited in-doc).

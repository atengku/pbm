# SA INWARD NOTE — PBM Technical Whitepaper (MAS, Jun 2023) [id P1]

## 1. Executive Summary
[id P1] MAS's PBM whitepaper is the constitutional document of programmable money in Singapore: it separates the rule layer (wrapper) from the value layer (money) so that policy can be encoded without breaking money's fungibility. The critical finding for any client-side matter: every restrictive behaviour — expiry, merchant lock, denominations — is a creator-authored parameter, and the reference design includes a creator-side revoke path for expired tokens. Rigidity experienced by end-users is therefore always a policy choice executed by code, never a mathematical property of the infrastructure. The paper is technically complete and politically silent — it offers no framework for holder recourse, and no accounting of breakage. That silence is where both the risk and the advisory opportunity sit.

## 2. Entity & People Map
| Entity | Role | Note |
|---|---|---|
| MAS (FTIG) | Author / convener | Sopnendu Mohanty era; Alvin Tan = current approach target |
| IMF | Co-designed 4-layer architecture | Lends international legitimacy |
| Banca d'Italia, Bank of Korea | Central bank contributors | Cross-jurisdiction ambition |
| Amazon, Grab, Fazz | Platform/commerce partners | Distribution rails |
| DBS, OCBC, Onyx (JPM), NETS | Money layer | Tokenised-liability issuers |
| OGP | Government products | RedeemSG — the live voucher testbed |

## 3. Mechanics (evidence chain)
[id P1 §3.2] Wrapper = smart contract holding conditions; money = ERC-20-style collateral locked inside. [id P1 §3.4] Lifecycle ends in Expired: violation renders tokens permanently unusable *to the holder*. [id P1 Fig 15] Creator may revoke expired PBMs and recover the underlying money — collateral flows back to the creator, i.e. programmed breakage. [id P1 §4-Privacy] Creator/issuer separation prevents any single party seeing issuance + usage. [id P1 §4-Policy] Paper explicitly notes jurisdictions differ on spending constraints; MAS takes no position — constraints are imported by the deploying agency.

## 4. Pattern / Network Analysis
[id P1 Appendix] The contributor set is the same cast that recurs across Orchid, the Blueprint and Guardian — DBS/OCBC/UOB + Grab/Fazz + OGP. MAS runs a repertory company: each paper re-legitimises the same private-sector coalition. Advisory implication: the door into PBM work is through these incumbents or through the gap they leave — citizen-side/sentiment work none of them owns.

## 5. Quantification
Not a financial document; the quantifiable exposure is breakage. Structure: 100% of unredeemed expired value reverts to creator at revocation, gas-cost only. Against CDC-scale disbursements (S$1.5bn+ support packages cited in Orchid P1), single-digit % breakage is a nine-figure flow with no published accounting standard. Open quantification thread.

## 6. Bull / Base / Bear (on PBM as SG policy infrastructure)
- **Bull:** PBM becomes the standard rail for all state disbursement + commercial vouchers; ERC-7291 exports it regionally; early advisors on governance/sentiment own a franchise.
- **Base:** PBM stays in extended pilots via RedeemSG-adjacent schemes; tokenised-deposit rails grow quietly; retail CBDC stays shelved. Advisory demand = episodic, policy-driven.
- **Bear:** Public backlash on "expiring money / control" narratives (the exact sentiment MAS hasn't instrumented) stalls retail-facing deployment; PBM retreats to wholesale/B2B escrow uses.

## 7. Open Threads
1. Does deployed RedeemSG-PBM code include the Fig-15 revoke function, and who holds the key? (Primary pull: GovTech cbdc-purpose-bound-money repo audit.)
2. Breakage accounting: where does revoked collateral sit in government accounts? (Parliamentary question territory.)
3. ERC-7291 final spec vs this paper — condition-set drift.

## 8. Sources
[id P1] MAS, *Purpose Bound Money Technical Whitepaper*, v1.0, 20 Jun 2023 (papers/01). Primary. Cross-refs: MAS Project Orchid P1 report (Oct 2022); ERC-7291; GovTechSG PBM repo.

# MAS PBM/CBDC Library — Full Analysis Chains (21 docs × 3 stages)

Generated 10 Aug 2026 · Seeking Alpha Advisors · per-claim citations reference [P#]/[G#] doc ids; originals at https://mas-wp.vercel.app



================================================================================
# ══ [P1] — 01_pbm_whitepaper
================================================================================


---
### ─── 1_intake.md ───

# INTAKE — 01 PBM Technical Whitepaper (Jun 2023)

SUBJECT: Founding technical specification of Purpose Bound Money — the wrapper/collateral protocol for condition-bound digital money.
SOURCE / RELIABILITY: **Primary** — MAS first-party publication, v1.0, 20 Jun 2023. Highest reliability tier.
ENTITIES: MAS (KB: mas-pbm-approach mandate target) · IMF (co-developed architecture) · Banca d'Italia · Bank of Korea · Amazon · DBS · Fazz · Grab · Onyx by J.P. Morgan · NETS · OCBC · Open Government Products [OGP — RedeemSG operator, NEW] · ERC-1155 / ERC-20 standards. All institutional entities NEW to KB except MAS.
KEY CLAIMS (each primary-sourced to the paper itself):
- PBM = wrapper (smart contract conditions) + underlying digital money (CBDC / tokenised bank liability / regulated stablecoin) used as collateral. Money itself stays unprogrammed — "singleness of money" preserved.
- Conditions are creator-set parameters: validity/expiry window, merchant whitelist/blacklist, denominations. **Expiry is configurable, not inherent.**
- Lifecycle: Issue → Distribute → Transfer → Redeem → **Expired**. Expired tokens are permanently unusable to the holder; creator may burn OR **revoke to recover the underlying money** (Fig 15). An admin claw-back path exists in the reference design.
- Privacy-by-structure: creator ≠ money issuer, so no single entity sees both issuance and usage. Anonymous-but-authorised transfer patterns are sketched.
- Payer is constrained; payee is not — released money is unbounded.
- Explicit disclaimer: paper advances no policy objective; jurisdictions choose their own conditions.
CONTRADICTIONS w/ KB: None. Confirms the position I gave Az in the voucher-expiry exchange: expiry = human-set parameter enforced by code, and revocation is a build choice.
CLASSIFY: Digital money / PBM · tags: MAS, PBM, smart contracts, programmable money, CBDC. Feeds the **MAS PBM mandate** (Alvin Tan approach) directly.
SIGNIFICANCE: This is the reference document for every "can the system bend" question about SG voucher schemes. Section 3.4–3.5 (expiry + revoke flows) is the technical spine of the policy-vs-architecture argument.
ROUTE: → research-4-knowledge → seeking-alpha-report. File under mas-pbm-approach corpus as [id P1].



---
### ─── 2_knowledge-map.md ───

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



---
### ─── 3_sa-report.md ───

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



================================================================================
# ══ [P2] — 02_orchid_phase1
================================================================================


---
### ─── 1_intake.md ───

# INTAKE — 02 Project Orchid Phase 1 Report (Nov 2022)

SUBJECT: MAS's first retail digital-SGD report — introduces PBM publicly, frames the "capability without commitment" doctrine, and documents four live industry trials.
SOURCE / RELIABILITY: **Primary** — MAS FTIG publication, Nov 2022. Foreword by Sopnendu Mohanty (Chief FinTech Officer).
ENTITIES: MAS · DBS · Grab · Fazz · NETS · OCBC · UOB · Temasek · OGP [RedeemSG] · CDC vouchers / MOF Household Support Package (S$1.5bn) · Global CBDC Challenge partners (IMF, World Bank, ADB, UNCDF, UNHCR, UNDP, OECD). Temasek + UOB NEW vs doc 01's cast.
KEY CLAIMS:
- Orchid launched SFF 2021 as first *retail* extension of the Ubin lineage; objective = build capability to issue retail CBDC "should Singapore decide to."
- MAS assessed **no urgent need** for retail CBDC (cites the 2021 economic paper) — but won't rule it out; trigger = foreign digital currencies gaining local traction.
- PBM introduced as third model beyond programmable payment / programmable money; four trials ran on tokenised deposits and an SGD stablecoin, **not** on any MAS-issued CBDC.
- Pain points motivating PBM: scheme proliferation (RedeemSG vs Grab silos), misuse/deviation risk, admin overhead, merchant settlement delays of days-to-weeks under current voucher claims.
- Retail CBDC envisioned as open common back-end, interoperable, public-rail minimum standards; cash = 8% of money supply, deposits 92%.
CONTRADICTIONS w/ KB: None; supplies the policy frame doc 01 assumes.
CLASSIFY: Digital money / PBM · retail CBDC posture · tags: MAS, Orchid, RedeemSG, CDC, tokenised deposits. Feeds MAS PBM mandate.
SIGNIFICANCE: The *why* behind PBM: MAS solving voucher-scheme fragmentation and misuse first, monetary futures second. Also the on-record statement of the optionality doctrine.
ROUTE: → knowledge map → SA note. File as [id P2].



---
### ─── 2_knowledge-map.md ───

# KNOWLEDGE MAP — 02 Project Orchid Phase 1

## Executive Summary (Alphas)
**Alpha 1 — Optionality is the strategy, not indecision.** "No urgent need, build anyway" is a deliberate doctrine: accumulate issuance capability while deferring the political decision indefinitely. The trigger condition MAS names is *currency substitution* — foreign digital money gaining local traction. Retail CBDC is a defensive weapon held in reserve.
**Alpha 2 — PBM was born as voucher plumbing.** The genuine motivating problems are administrative: scheme fragmentation, merchant settlement lag, misuse control for CDC-type disbursements. The monetary-futures language is the wrapper; RedeemSG's pain points are the collateral.
**Alpha 3 — Private money does the work.** Every trial ran on tokenised deposits or a stablecoin. The state supplies the standard; banks supply the money. This is the two-tier system defending itself by absorbing the innovation.

## 4-Quadrant Matrix
**KNOWN KNOWNS:** Orchid timeline (Ubin 2016 → Orchid 2021) · no-urgent-need assessment · PBM three-model framing · 4 trials (DBS/Grab/Fazz/NETS/OCBC/UOB/Temasek/OGP) · CDC voucher context (S$1.5bn package) · 8/92 split · public+private blockchain feasibility tested.
**KNOWN UNKNOWNS:** future MAS-CBDC-backed phase · public-chain suitability as FMI (explicitly disclaimed) · scheme rulebook/governance (deferred to Blueprint).
**UNKNOWN KNOWNS:** Singapore's non-internationalisation instinct for SGD · GovTech/OGP's existing RedeemSG rails as the real deployment path · the 2021 econ paper's bank-protection logic silently constraining every design choice here.
**UNKNOWN UNKNOWNS (gaps):**
- *The substitution-trigger paradox.* The named trigger for issuing retail CBDC (foreign digital currency traction) is the one scenario where SG's capability-building must already be finished. Optionality has a deadline someone else sets — USD stablecoin adoption curves, not MAS.
- *Merchant float politics.* Days-to-weeks settlement lag under current voucher claims = working-capital extraction from heartland merchants. PBM's instant unwrap kills that float. Nobody in the paper asks who currently earns it.
- *Trial-to-policy laundering.* Industry "trials" with named commercial partners generate the evidence base that later justifies the standard those same partners implement. Circular legitimation, standard MAS playbook — worth naming for the sentiment work.

## Narrative Vector
The report validates PBM as concept but **reframes the whole programme**: Orchid is not about issuing a digital dollar; it is about making sure nobody else's digital dollar matters in Singapore. Defensive monetary sovereignty wearing an innovation lanyard. That framing is directly useful to the MAS mandate — sentiment research that speaks to *sovereignty protection* will land better with FTIG than research framed around CBDC enthusiasm.



---
### ─── 3_sa-report.md ───

# SA INWARD NOTE — Project Orchid Phase 1 (MAS, Nov 2022) [id P2]

## 1. Executive Summary
[id P2] Orchid P1 is MAS's declaration of the optionality doctrine: build every capability required to issue a retail digital SGD while formally concluding there is no case to issue one. PBM debuts here not as monetary innovation but as an administrative fix for a real, costed problem — fragmented voucher schemes, misuse risk, and merchant settlement lag in S$1.5bn-scale disbursement programmes. All trials ran on private money (tokenised deposits, one SGD stablecoin); the state's contribution is the standard, not the currency. The strategic tell is the named trigger for reversal: foreign digital currencies gaining domestic traction. Orchid is monetary defence procurement.

## 2. Entity & People Map
| Entity | Role |
|---|---|
| MAS FTIG / S. Mohanty | Programme owner, foreword |
| DBS, OCBC, UOB | Tokenised-deposit issuers in trials |
| Grab, Fazz, NETS | Wallet/rails/acceptance |
| Temasek | State-capital participant |
| OGP (RedeemSG) | Government voucher rail — the live testbed |
| MOF / CDC | S$1.5bn Household Support Package context |

## 3. Mechanics (evidence chain)
[id P2 §1] Orchid = first retail extension of Ubin lineage; explicit purpose = capability to issue "should Singapore decide to." [id P2 §1] MAS assessment: no urgent need (cites 2021 econ monograph); reversal trigger = non-SGD digital currencies gaining local traction. [id P2 §2] Motivating frictions: scheme proliferation (RedeemSG vs Grab), misuse/deviation ("not possible to direct that recipients spend at approved merchants and not on vices"), admin overhead, merchant claims settled after days-to-weeks. [id P2 §3] PBM architecture: four components (money, wrapper, infra, wallet); works on DLT and non-DLT; trials used tokenised deposits + regulated stablecoin, MAS CBDC deferred to a future phase.

## 4. Pattern / Network Analysis
[id P2 Appendix] Same repertory cast as [id P1] plus UOB and Temasek. Pattern across the lineage: MAS convenes incumbents → runs "trials" → publishes findings authored with the trial participants → findings become the standard the participants operate. Closed evidentiary loop; effective, and exactly the structure an external sentiment-research mandate sits outside of — which is its value to MAS.

## 5. Quantification
[id P2 §2] CDC context: S$1.5bn support package. Merchant settlement lag: days-to-weeks → instant on PBM unwrap. Float destroyed = (claim value × lag days × prevailing rate) currently sitting with scheme administrators/banks; at billion-dollar scheme scale, a real number nobody in the paper owns up to. Cash 8% / deposits 92% of money supply — the ratio PBM is engineered not to disturb.

## 6. Bull / Base / Bear (on the Orchid programme)
- **Bull:** Optionality converts to issuance on a substitution scare; SG ships the first credible retail CBDC in a major financial centre; PBM standard exports via ERC-7291.
- **Base:** Perpetual capability-building; PBM absorbs government disbursement rails through OGP; retail CBDC stays a press-conference hypothetical. (This is the trajectory to date.)
- **Bear:** Trials plateau, incumbent banks slow-walk tokenised deposits to protect deposit franchise economics, and the programme's public face becomes "expiring vouchers" — a sentiment liability instead of an innovation story.

## 7. Open Threads
1. Phase 2 pilot outcomes — which of the four P1 trials survived contact with production? (Blueprint [id P4] partially answers.)
2. The float question: who currently earns the settlement lag on CDC/RedeemSG claims. (FOI/parliamentary-answer pull.)
3. Whether any trial tested *holder recourse* on expiry — no evidence in P1 or P2 that anyone has.

## 8. Sources
[id P2] MAS, *Project Orchid: Programmability of Digital SGD*, Nov 2022 (papers/02). Primary. Cross-refs: [id P1], [id P3] 2021 econ monograph, MOF press release on Household Support Package.



================================================================================
# ══ [P3] — 03_retail_cbdc_econ
================================================================================


---
### ─── 1_intake.md ───

# INTAKE — 03 A Retail CBDC: Economic Considerations in the Singapore Context (Nov 2021)

SUBJECT: MAS EPG monograph — the economic case assessment that concluded "no compelling case now" and set the policy foundation everything after stands on.
SOURCE / RELIABILITY: **Primary** — MAS Economic Policy Group, Nov 2021. The policy brain of the whole lineage.
ENTITIES: MAS EPG · two-tier system actors (MAS ↔ commercial banks) · references: BIS, IMF, Riksbank e-krona, PBoC e-CNY, FAST/PayNow/SGQR, digital bank licensees (2020 awards).
KEY CLAIMS:
- Verdict: **no pressing need** for retail SGD CBDC; e-payments pervasive, competitive, cheap. But prudent to build technical + policy capability for possible future issuance.
- Threat model: (1) cash's diminishing relevance; (2) payments market concentration / walled gardens from data-driven platforms; (3) **currency substitution** — a small open digital economy is vulnerable to a widely-used foreign digital currency; prudential regulation defends "only up to a point."
- Risk model of issuing: deposit disintermediation (deposits = 92% of money supply, banks' cheap stable funding), faster systemic runs (friction to flee to central-bank money collapses), volatile capital flows if non-residents can hold.
- Mitigants: holding limits/financial disincentives, non-resident restrictions — CBDC as medium of exchange, **not** store of value.
- Model if issued: public-private — MAS issues, private sector distributes/KYCs; direct claim on MAS.
CONTRADICTIONS w/ KB: None. This is the source of Orchid P1's "no urgent need" citation.
CLASSIFY: Monetary policy / CBDC economics · tags: MAS EPG, disintermediation, currency substitution, two-tier system.
SIGNIFICANCE: Explains *why* PBM rides private money: the entire architecture downstream is shaped to protect bank funding. Any client work touching digital-SGD must be read against this document's constraints.
ROUTE: → knowledge map → SA note. File as [id P3].



---
### ─── 2_knowledge-map.md ───

# KNOWLEDGE MAP — 03 Retail CBDC Economic Considerations

## Executive Summary (Alphas)
**Alpha 1 — Bank funding is the binding constraint.** The document's true center of gravity: deposits are 92% of money supply and banks' cheap stable funding; an attractive CBDC threatens that base and accelerates runs. Every subsequent design choice — PBM over private money, holding limits, medium-of-exchange-not-store-of-value — descends from protecting this.
**Alpha 2 — The real fear is substitution, not innovation.** MAS names the scenario that changes its mind: a foreign digital currency gaining domestic traction that prudential regulation can't hold back. The CBDC option is a sovereignty hedge with someone else's finger on the trigger.
**Alpha 3 — "Public option" logic imported into payments.** The CBDC case is framed like a public utility backstop: if private payment costs/quality fail end-users, the state instrument disciplines the market. Regulation vs issuance presented as substitutes — issuance is the escalation rung.

## 4-Quadrant Matrix
**KNOWN KNOWNS:** Two-tier system mechanics · 8/92 split · verdict + rationale · disintermediation/run/capital-flow risks · mitigants (limits, non-resident restrictions) · public-private issuance model · FAST/PayNow/SGQR as the regulatory alternative track.
**KNOWN UNKNOWNS (paper flags):** legal/operational/regulatory design · AML-CFT trade-offs · privacy expectations of the citizenry · synthetic CBDCs and tokenised deposits "on their own merits."
**UNKNOWN KNOWNS:** SGD non-internationalisation policy heritage (Ong 2003 cited) — the deep instinct that shapes non-resident restrictions · Singapore's state-capital structure (banks partly state-linked) meaning deposit-base protection is also portfolio protection.
**UNKNOWN UNKNOWNS (gaps):**
- *The substitution clock is exogenous.* USD-stablecoin network effects compound on global platforms regardless of SG readiness. The monograph treats the trigger as observable-in-time; adoption curves rarely are. Optionality may be exercised late by construction.
- *Distributional silence.* Whole analysis is systemic (banks, flows, stability); zero analysis of which *households* bear costs when the public instrument (cash) fades pre-CBDC. The unbanked/elderly are one MAS parliamentary answer, not a modelled constituency.
- *Privacy as afterthought.* Privacy appears as a regulatable service feature, not a rights baseline — the exact fault line public sentiment runs on, unmodelled in the economics.

## Narrative Vector
Validates the no-issuance verdict on its own terms, but **exposes the frame**: this is a bank-stability document wearing a consumer-payments cover. The blind spot — household-level and sentiment analysis — is precisely the gap the SAA/MAS PBM mandate proposes to fill. Quote the monograph's own silences back to FTIG.



---
### ─── 3_sa-report.md ───

# SA INWARD NOTE — Retail CBDC: Economic Considerations (MAS EPG, Nov 2021) [id P3]

## 1. Executive Summary
[id P3] The 2021 EPG monograph is the policy constitution of Singapore's digital-money programme: a formal finding of "no pressing need" for a retail CBDC, paired with a commitment to build issuance capability anyway. Its analytical spine is bank-funding protection — deposits are 92% of money supply, and a well-designed CBDC is precisely the instrument that could drain them and accelerate runs. The document's named reversal trigger is foreign digital-currency substitution, a clock MAS does not control. Everything built after 2021 — PBM over private money, tokenised deposits, holding-limit doctrine — is downstream compliance with this paper's constraints. Its blind spots (household distribution, privacy-as-rights, sentiment) define the whitespace for external advisory work.

## 2. Entity & People Map
| Entity | Role |
|---|---|
| MAS EPG | Author — economics, not FTIG tech track |
| Commercial banks (DBS/OCBC/UOB et al.) | Protected constituency: deposit franchise |
| Non-bank fintechs / digital banks (2020 licences) | Contestability channel MAS prefers over issuance |
| Foreign digital currencies / global stablecoins | The named threat |
| Riksbank, PBoC, BIS, IMF | Comparators/authorities cited |

## 3. Mechanics (evidence chain)
[id P3 Exec Summ] Verdict: no pressing need; capability-building prudent. [id P3 Ch2] Two-tier system: MAS liabilities = cash (public) + reserves (banks); deposits = 92% of money and the basis of all digital payments. [id P3 Ch3] Benefits case: public payment option as commerce digitalises; lower entry barriers for payment innovators; discipline on walled gardens. [id P3 Ch4] Risk case: deposit outflow → funding cost/liquidity stress → tighter credit or fragile banks; run acceleration ("first signs of trouble"); non-resident demand → capital-flow volatility. Mitigants: holding limits, disincentives, non-resident restrictions — engineered to keep CBDC a medium of exchange, not a store of value. [id P3 Ch5] Substitution threat named; prudential defence works "only up to a point."

## 4. Pattern / Network Analysis
[id P3] The document inaugurates the pattern the whole corpus repeats: protect the two-tier system by absorbing innovation into it. Regulation-first (FAST/PayNow/SGQR, fee logic, digital-bank licences), issuance as reserve escalation. Cross-referenced against [id P1][id P2]: PBM's money-neutral wrapper is this paper's disintermediation fear rendered as engineering.

## 5. Quantification
[id P3] Cash ≈ 8% of money supply; deposits ≈ 92%. Run-dynamics claim is directional, not modelled publicly — no published elasticity of deposit→CBDC switching for SG (open thread). Non-resident SGD demand under a CBDC: flagged, unquantified — consistent with the non-internationalisation instinct.

## 6. Bull / Base / Bear (on the monograph's doctrine holding)
- **Bull (doctrine vindicated):** e-payments stay competitive, substitution never bites, optionality never exercised — the cheapest possible monetary defence.
- **Base:** Doctrine holds through the decade; pressure vents through regulated stablecoins + tokenised deposits; the monograph gets a v2 refresh when US/EU stablecoin regimes mature.
- **Bear (doctrine caught out):** A dominant foreign stablecoin embeds in regional platforms faster than SG can stand up retail issuance; the "up to a point" line on prudential defence is tested in public; capability built ≠ deployment-ready at the speed required.

## 7. Open Threads
1. Any internal MAS modelling of deposit-switching elasticity / run acceleration — referenced nowhere publicly.
2. Post-2021 refresh: has EPG revisited the verdict since MiCA/US stablecoin legislation? (Search MAS monographs 2024–26.)
3. Household-level payment-cost incidence data — the distributional analysis the paper skips.

## 8. Sources
[id P3] MAS EPG, *A Retail CBDC: Economic Considerations in the Singapore Context*, Nov 2021 (papers/03). Primary. Cross-refs: [id P1][id P2], Ong (2003) non-internationalisation, BIS/IMF/Riksbank literature per the paper's bibliography.



================================================================================
# ══ [P4] — 04_orchid_blueprint
================================================================================


---
### ─── 1_intake.md ───

# INTAKE — 04 Project Orchid Blueprint (Nov 2023)

SUBJECT: The infrastructure blueprint for digital-money issuance and use in Singapore — settlement ledgers, tokenisation bridge, PBM as protocol layer, name service, and the governance perimeter.
SOURCE / RELIABILITY: **Primary** — MAS, Nov 2023, with industry group input (Phase 2 output).
ENTITIES: MAS · Amazon · BCS (Banking Computer Services) [NEW] · DBS · Fazz · Grab · Onyx (JPM) · NETS · OCBC · UOB · MEPS+ · FAST · OCL ["Orchid Compatible Ledger" — NEW term].
KEY CLAIMS:
- Three supported monies only: MAS-regulated stablecoins (SCS framework, Aug 2023), tokenised bank liabilities from MAS-licensed banks, and MAS-issued CBDC. Everything else excluded.
- Building blocks: (1) Settlement Ledger with atomic settlement + native programmability, (2) Tokenisation Bridge to account-based rails, (3) PBM as the programmability protocol, (4) Name Service, (5) modular future blocks.
- OCL qualification: operators face FMI-grade expectations (PFMI in scope as systemically important); **permissionless networks "unlikely to meet the requirements"**; rulebooks dictate permissible activity; e.g. all may transact, only designated providers deploy smart contracts.
- Retail access only indirect, through licensed FIs post-KYC; whitelisting/subnets/verifiable credentials as access controls.
- Scope excludes cross-border trade + capital markets (routed to Guardian).
CONTRADICTIONS w/ KB: None; hardens P1/P2's open governance questions into a permissioned perimeter.
CLASSIFY: Digital money infrastructure · tags: OCL, settlement ledger, PBM, TBL, SCS, MEPS+.
SIGNIFICANCE: The gatekeeping document — decides who may operate, who may program, who may touch the ledger. The wrapper writes policy (P1); the Blueprint decides who gets to write wrappers.
ROUTE: → knowledge map → SA note. File as [id P4].



---
### ─── 2_knowledge-map.md ───

# KNOWLEDGE MAP — 04 Orchid Blueprint

## Executive Summary (Alphas)
**Alpha 1 — The Blueprint is a licensing perimeter drawn in advance.** By defining OCL qualification (FMI-grade standards, rulebooks, permissioned deployment), MAS pre-decides the market structure of programmable money before any market exists. Incumbent settlement operators and licensed banks are grandfathered into the future by specification.
**Alpha 2 — Permissionless is out, by design.** The explicit finding that permissionless networks are "unlikely to meet the requirements" quietly severs Singapore's retail digital money from public-chain ecosystems while Guardian courts them for wholesale assets. Two-track strategy: open for capital markets optics, closed for the money citizens hold.
**Alpha 3 — Smart-contract deployment as a licensable activity.** "All participants may initiate transactions, but deployment of smart contracts may only be done by designated service providers" — wrapper authorship (the policy surface from P1) becomes a gated privilege. This is the choke point of the entire architecture.

## 4-Quadrant Matrix
**KNOWN KNOWNS:** Three permitted money forms · five building blocks · OCL spec + PFMI exposure · indirect-only retail access · MEPS+/FAST augmentation logic · cybersecurity/OWASP smart-contract posture · scope exclusion of cross-border/capital markets.
**KNOWN UNKNOWNS (paper flags):** commercial/operating model alignment among FIs · scheme rulebook detail · cross-border extension · onboarding streamlining · scalability of commercial arrangements.
**UNKNOWN KNOWNS:** SCS framework timing (finalised Aug 2023, three months prior — the Blueprint operationalises it) · BCS's role as domestic clearing incumbent (FAST operator lineage) — the natural OCL operator hiding in the contributor list · P3's disintermediation doctrine silently enforced by the three-money whitelist.
**UNKNOWN UNKNOWNS (gaps):**
- *Designated-deployer capture risk.* Whoever wins "designated service provider" status owns the policy-authoring layer for programmable SGD. No criteria, no contestability process, no sunset — a concession being created without a tender.
- *OCL plurality vs monopoly.* Paper gestures at domestic convergence to a single ledger for economies of scale; a single OCL operator = a new systemically-important private monopoly at the heart of retail money. Governance of that entity is unwritten.
- *Bridge as the fragile joint.* The Tokenisation Bridge connecting token rails to MEPS+/FAST inherits both worlds' failure modes; it is the systemic single point the PFMI language circles without naming.

## Narrative Vector
The Blueprint **shifts the story** from technology to market structure: Orchid's real Phase 2 output is a draft concession map for who operates, who programs, and who merely transacts. For the mandate: MAS will need public legitimacy for exactly these gatekeeping choices — sentiment research on "who should be allowed to program money" is unclaimed ground.



---
### ─── 3_sa-report.md ───

# SA INWARD NOTE — Orchid Blueprint (MAS, Nov 2023) [id P4]

## 1. Executive Summary
[id P4] The Blueprint converts Orchid from experiment to market design. It whitelists three forms of money (MAS-regulated stablecoins, licensed-bank TBLs, MAS CBDC), specifies the Orchid Compatible Ledger with FMI-grade expectations, and gates the two powers that matter: operating the ledger and deploying smart contracts. Permissionless infrastructure is excluded from retail money outright. The document reads as pre-regulation — a concession framework published as a technical paper — and the unassigned "designated service provider" role for contract deployment is the single most valuable undistributed licence in the architecture.

## 2. Entity & People Map
| Entity | Role |
|---|---|
| MAS | Specifier / future gatekeeper |
| BCS | Domestic clearing incumbent in contributor list — natural OCL operator candidate |
| DBS, OCBC, UOB | TBL issuers; ledger participants |
| Onyx (JPM), Amazon | Tech/rails contributors |
| Grab, Fazz, NETS | Wallet/acceptance layer |
| MEPS+ / FAST | Legacy rails the Bridge must touch |

## 3. Mechanics (evidence chain)
[id P4 §3] Permitted monies: SCS-framework stablecoins, licensed-bank TBLs, MAS CBDC — closed list. [id P4 §4] Five building blocks; settlement ledger carries atomic settlement + native programmability; PFMI applies to the extent systemically important. [id P4 §4.1] Permissionless networks "unlikely to meet the requirements" of OCL qualification; rulebooks govern permissible activity; deployment of smart contracts restricted to designated providers; retail access indirect via licensed FIs with due diligence; whitelists/subnets/verifiable credentials as controls. [id P4 §8] Cross-border deferred; industry group continues on open questions.

## 4. Pattern / Network Analysis
[id P4] Third appearance of the repertory cast ([id P1][id P2]), now with BCS added — the clearing-utility tell. Pattern: each Orchid document ratchets the perimeter tighter (P1 explores → whitepaper standardises → Blueprint licenses). Read in sequence, the "trials" were the consultation phase of a market-structure decision that was directionally made in [id P3].

## 5. Quantification
No financials disclosed. The quantifiable stake is concession value: OCL operator economics (clearing-utility fee pool across national retail disbursement + voucher flows) and designated-deployer economics (every wrapper for every scheme). Sizing thread: RedeemSG scheme volumes + CDC disbursement scale from [id P2] as the addressable flow.

## 6. Bull / Base / Bear (on the Blueprint's market design)
- **Bull:** Clean concession process, plural OCLs, contestable deployer licensing — SG gets a genuinely open programmable-money layer and exports the model.
- **Base:** Single de-facto OCL emerges around incumbent clearing (BCS-adjacent), banks keep TBL issuance, deployer status lands with a short list of licensed providers. Orderly, closed, unremarked.
- **Bear:** Perimeter hardens into monopoly before public debate happens; the first controversy (an expiring-voucher incident, a blacklisting error) lands on an architecture nobody consented to; MAS wears the legitimacy cost.

## 7. Open Threads
1. Who is designated to deploy — criteria, process, and whether it will be gazetted or contractual. (Watch MAS consultations 2024–26.)
2. OCL operator candidacy: BCS corporate positioning post-2023. (ACRA/press pull.)
3. Whether SCS-framework stablecoins have actually been licensed since — the whitelist's live population.

## 8. Sources
[id P4] MAS, *Orchid Blueprint*, Nov 2023 (papers/04). Primary. Cross-refs: [id P1][id P2][id P3], MAS SCS framework media release (Aug 2023), PFMI (BIS/IOSCO).



================================================================================
# ══ [P5] — 05_ubin_p1
================================================================================


---
### ─── 1_intake.md ───

# INTAKE — 05 Ubin Phase 1: SGD on Distributed Ledger (2017)
SUBJECT: First tokenised-SGD proof of concept — banks exchange a central-bank-backed digital SGD on Ethereum-lineage DLT for interbank payment.
SOURCE / RELIABILITY: **Primary** (MAS-commissioned), but authored with/by **Deloitte** and R3 — vendor voice throughout; treat framing (DLT evangelism, "Internet of Value") as consultant marketing layered on a genuine experiment.
ENTITIES: MAS (Stanley Yong, Toh Wee Kee) · Deloitte (author) · R3 · BAML · BCS · Credit Suisse · DBS · HSBC · JPM (Naveen Mallela — later Onyx head, recurring node) · MUFG · OCBC · SGX · UOB.
KEY CLAIMS: Banks pledge cash to MAS, receive tokenised SGD 1:1; P2P interbank transfer without intermediary; positions SG as first Asian financial centre exploring DLT broadly; WEF "80% of banks will initiate DLT projects in 2017" cited uncritically.
CONTRADICTIONS w/ KB: None; establishes the consortium cast reused for a decade.
CLASSIFY: Wholesale CBDC / Ubin lineage · tags: tokenised SGD, R3, Deloitte, MEPS+.
SIGNIFICANCE: Origin node. The names matter more than the tech — Mallela (JPM), the local banks, BCS all recur through 2023's Blueprint.
ROUTE: → map → SA note. [id P5]



---
### ─── 2_knowledge-map.md ───

# KNOWLEDGE MAP — 05 Ubin Phase 1
## Alphas
**A1 — The pledge model is a synthetic CBDC.** Cash pledged to MAS, tokens issued 1:1 against it: functionally a fully-reserved stablecoin operated inside the central bank. The design pattern PBM later inherits (collateral locked, representation circulates) is born here.
**A2 — The consortium is the product.** Eleven institutions learning together under MAS convening; the durable output was relationships and shared vocabulary, not code. Ubin P1's real deliverable was the repertory company.
**A3 — Vendor-authored state research.** Deloitte's brand and worldview saturate a central-bank publication; the hype baseline (WEF 80% claim) dates instantly. Reliability discipline: separate the experiment (real) from the narrative (sold).
## Quadrants
KK: pledge/issue/transfer mechanics · consortium roster · Ethereum-lineage PoC. KU: scalability, privacy, LSM (deferred to P2) · legal status of the token. UK: MEPS+'s SGD 70bn/day incumbency as the quiet benchmark · 2017 ICO-era hype context inflating claims. UU: *No exit analysis* — nothing on what unwinding tokenised SGD does to reserves accounting; *the vendor-capture pattern* — each Ubin phase is authored by the consultant who delivered it (Deloitte→Accenture→Accenture), meaning the record of what "succeeded" is written by the party paid to succeed.
## Narrative Vector
Validates feasibility trivially; the enduring value is genealogical. Read P1 as the cap-table of Singapore's digital-money establishment.



---
### ─── 3_sa-report.md ───

# SA INWARD NOTE — Ubin Phase 1 (2017) [id P5]
## 1. Executive Summary
[id P5] Ubin P1 tokenised the SGD via a pledge model — banks post cash to MAS, receive 1:1 tokens, transfer P2P on DLT. Technically a solved problem even in 2017; strategically the founding of the MAS-convened consortium (11 FIs + Deloitte/R3) that has run Singapore's digital-money agenda since. The report is vendor-authored, and its hype claims aged badly; its roster did not.
## 2. Entity Map
MAS (Yong, Toh) | Deloitte (author) | R3 | DBS, OCBC, UOB, HSBC, BAML, CS, JPM (Mallela), MUFG | SGX | BCS.
## 3. Mechanics
[id P5] Pledge → mint 1:1 → P2P transfer → redeem. Central-bank collateral, private circulation — the synthetic-CBDC pattern PBM later generalises.
## 4. Pattern
[id P5] First appearance of the recurring cast: Mallela→Onyx ([id P1]), BCS→Blueprint ([id P4]), SGX→P3 DvP. Vendor authorship pattern begins (Deloitte P1/P3, Accenture P2/P5/Jasper).
## 5. Quantification
MEPS+ benchmark: ~25k txns/day, up to SGD 1bn each, ~SGD 70bn/day — the incumbent Ubin never displaced.
## 6. Bull / Base / Bear
Bull: pattern matured into production tokenised-deposit rails (partially realised via Partior). Base: capability + relationships banked; MEPS+ untouched. **Base realised.** Bear: consortium fatigue — did not materialise; cast retained.
## 7. Open Threads
Partior lineage from Ubin P5 → JPM/DBS/Temasek JV — trace equity and mandate. Legal characterisation of the pledged-token claim, never published.
## 8. Sources
[id P5] papers/05, primary (vendor-authored). Cross: [id P6][id P10][id P4].



================================================================================
# ══ [P6] — 06_ubin_p2
================================================================================


---
### ─── 1_intake.md ───

# INTAKE — 06 Ubin Phase 2: Re-imagining RTGS (2017)
SUBJECT: Decentralised RTGS functions — fund transfer, queuing, gridlock resolution (LSM) — prototyped on Corda, Hyperledger Fabric, Quorum with transaction privacy preserved.
SOURCE / RELIABILITY: **Primary**; MAS+ABS led, **Accenture-delivered** (vendor voice), 11 FIs, Azure platform.
ENTITIES: MAS · ABS · Accenture · BAML · Citi · CS · DBS · HSBC · JPM · MUFG · OCBC · SGX · StanChart · UOB · Microsoft Azure.
KEY CLAIMS: All three platforms achieved decentralised LSM/gridlock resolution without compromising privacy (Corda UTXO+confidential identities; Fabric channels; Quorum Constellation+ZKP). Headline: feasible to **remove the central infrastructure operator** — "the role of MAS as an infrastructure operator needs to be re-evaluated."
CONTRADICTIONS w/ KB: The 2023 Blueprint [id P4] answers this question in the opposite direction — permissioned, FMI-grade, operator-centric. P2's decentralisation enthusiasm was quietly reversed.
CLASSIFY: Wholesale CBDC / RTGS · tags: LSM, gridlock, Corda, Fabric, Quorum, MEPS+.
SIGNIFICANCE: The high-water mark of decentralisation rhetoric in official SG fintech literature — useful contrast object.
ROUTE: → map → SA note. [id P6]



---
### ─── 2_knowledge-map.md ───

# KNOWLEDGE MAP — 06 Ubin Phase 2
## Alphas
**A1 — The road not taken, documented.** P2 proves the central operator can be removed and openly invites re-evaluating MAS's operator role. Six years later the Blueprint reinstates the operator with FMI-grade requirements. The corpus contains its own refutation — decentralisation was tested, feasible, and declined. That is a policy choice on the record.
**A2 — Privacy tech menu established.** UTXO/confidential identities vs channels vs ZKP — the 2017 catalogue Mandala's ZKP work later industrialises.
**A3 — LSM decentralisation is the hard genuinely-new result.** Gridlock resolution without a single consolidated view was the real cryptographic contribution; everything else was integration.
## Quadrants
KK: 3 prototypes, 3 privacy models, LSM feasibility, 13-week build. KU: scalability, resilience at production loads, legal finality of decentralised netting. UK: ABS as co-lead — the banking cartel's formal seat at the design table; Azure dependency (decentralised ledger on centralised cloud, unremarked). UU: *finality-in-law gap* — no analysis of whether decentralised gridlock netting satisfies settlement-finality statutes; *the operator-economics silence* — removing MAS as operator removes a fee/oversight structure nobody models.
## Narrative Vector
Validates technical decentralisation, and thereby **converts every later centralisation into a documented preference**. Quote P2 against P4 when the "technology requires it" defence appears.



---
### ─── 3_sa-report.md ───

# SA INWARD NOTE — Ubin Phase 2 (2017) [id P6]
## 1. Executive Summary
[id P6] P2 decentralised the crown jewels of an RTGS — queuing and gridlock resolution — across Corda, Fabric and Quorum, each with a distinct privacy solution, and concluded the central operator could be removed, explicitly inviting re-evaluation of MAS's own role. That invitation was never taken up: the 2023 Blueprint restores an operator-centric, FMI-grade model. P2 therefore functions today as the corpus's counterfactual — proof that Singapore's permissioned architecture is chosen, not compelled.
## 2. Entity Map
MAS + ABS (co-leads) | Accenture (delivery) | 11 FIs incl. Citi, StanChart (only appearances) | Azure.
## 3. Mechanics
[id P6] Fund transfer, queue, gridlock netting decentralised; privacy via UTXO/confidential identities (Corda), channels (Fabric), Constellation+ZKP (Quorum). MEPS+ context: ~SGD 70bn/day.
## 4. Pattern
[id P6] Vendor rotation to Accenture; ABS's structural seat = incumbent banks co-author the future of their own settlement layer. Cross-ref [id P4]: the decentralisation finding is the corpus's largest unacknowledged reversal.
## 5. Quantification
13-week build; three parallel workstreams. No cost or throughput figures published against MEPS+ — the comparison that would have mattered.
## 6. Bull / Base / Bear
Bull (then): DLT-RTGS replaces MEPS+. Base: findings absorbed, MEPS+ retained, LSM learnings inform future rail design. **Base realised.** Bear: prototypes shelved entirely — avoided; lineage continued to P3-P5.
## 7. Open Threads
Whether any P2 LSM design survived into Partior/Ubin V production specs. Settlement-finality legal opinion on decentralised netting — never published.
## 8. Sources
[id P6] papers/06, primary (Accenture-delivered). Cross: [id P4][id P5][id P10].



================================================================================
# ══ [P7] — 07_ubin_p3
================================================================================


---
### ─── 1_intake.md ───

# INTAKE — 07 Ubin Phase 3: DvP on DLT (2018)
SUBJECT: Delivery-versus-Payment of tokenised SGS (govvies) against central-bank cash-depository receipts across **separate** ledgers — interledger settlement finality with investor protections.
SOURCE / RELIABILITY: **Primary**; MAS+SGX co-chaired (Mohanty / Tinku Gupta), tech partners Anquan, Deloitte, Nasdaq.
ENTITIES: MAS · SGX · Anquan Capital · Deloitte · Nasdaq · platforms: Quorum, Fabric, Ethereum, Anquan, Chain · comparators: ECB/BoJ STELLA, ASX CHESS replacement.
KEY CLAIMS: Cross-ledger DvP achieved trade-by-trade; smart-contract DvP encodes rights/obligations consistently; settlement-cycle compression beyond T+2 plausible; design keeps a **Recognised Market Operator central** for monitoring; investor protections: multi-sig account controls, contract locks with secret disclosure, time-bounded asset recovery, **arbitration for disputes**.
CONTRADICTIONS w/ KB: None. Notably P3 builds the dispute/arbitration state that the retail PBM lifecycle [id P1] lacks — institutions got recourse rails; citizens didn't.
CLASSIFY: Wholesale / capital markets settlement · tags: DvP, SGS, SGX, HTLC-precursor, arbitration.
SIGNIFICANCE: The recourse asymmetry — engineered dispute resolution for wholesale participants vs none in the retail PBM design — is a load-bearing finding for the sentiment mandate.
ROUTE: → map → SA note. [id P7]



---
### ─── 2_knowledge-map.md ───

# KNOWLEDGE MAP — 07 Ubin Phase 3
## Alphas
**A1 — Recourse was built where the counterparties are banks.** P3's design features — time-bounded recovery, arbitration on dispute, reversal states (Expired/Reversed/Disputed appear in its state diagrams) — are exactly the contestability machinery absent from the citizen-facing PBM lifecycle. The asymmetry is a design fingerprint: protection follows institutional power.
**A2 — Decentralisation retreat begins here.** One phase after P2 proved operator-removal feasible, P3 deliberately re-centres a Recognised Market Operator. The permissioned trajectory that ends in the Blueprint starts in 2018.
**A3 — "Distributed, not decentralised" said out loud.** The report's own sidebar concedes every layer is a centric implementation — the honest sentence the rest of the corpus avoids.
## Quadrants
KK: cross-ledger DvP mechanics, 5 platforms, investor-protection feature set, STELLA/ASX context. KU: scale, multi-jurisdiction complications, non-DLT RTGS integration. UK: SGX's commercial stake in whichever settlement future wins — co-chair is also incumbent CSD/RMO; T+2→T+0 compression's margin impact on custody revenue, unexamined. UU: *the recourse asymmetry vs [id P1]* (nobody has cross-read these); *arbitration on-chain as precedent* — a template for citizen-facing PBM disputes that MAS already owns and hasn't reused.
## Narrative Vector
Validates cross-ledger DvP; the durable insight is comparative: when the users are banks, the state machine grows Disputed and Reversed states. Carry that spec sheet into any argument about what retail PBM *could* include.



---
### ─── 3_sa-report.md ───

# SA INWARD NOTE — Ubin Phase 3 DvP (2018) [id P7]
## 1. Executive Summary
[id P7] P3 settled tokenised Singapore Government Securities against central-bank receipts across separate ledgers, trade-by-trade, with settlement finality — and wrapped the mechanism in institutional-grade protections: multi-sig controls, secret-locked contracts, time-bounded recovery, arbitration. It quietly re-centred a Recognised Market Operator one phase after P2 showed operators removable. Its most valuable content today is comparative: the wholesale state machine includes Disputed and Reversed; the retail PBM lifecycle does not. Recourse was engineered for banks and omitted for citizens.
## 2. Entity Map
MAS (Mohanty) + SGX (Gupta) co-chairs | Anquan, Deloitte, Nasdaq (tech) | platforms: Quorum/Fabric/Ethereum/Anquan/Chain.
## 3. Mechanics
[id P7] Buyer-side CBDC transfer + seller-side SGS transfer linked; contract locks with secret disclosure; 48-hour windows then arbitration; states: Trade→Post-trade→Expired/Reversed/Disputed. RMO retained for monitoring/facilitation.
## 4. Pattern
[id P7] Cross-read vs [id P1]: identical wrapper logic, opposite recourse design. Vendor rotation back to Deloitte + exchange-adjacent Nasdaq/Anquan. SGX as co-author of its own disruption — classic incumbent absorption.
## 5. Quantification
Settlement-cycle compression T+3→T+2 industry context; DLT floated as enabler beyond. No cost-of-settlement deltas published.
## 6. Bull / Base / Bear
Bull: SGS settlement migrates on-ledger; SGX runs it. Base: learnings absorbed into SGX digital ventures (Marketnode lineage) without displacing CDP core. **Base broadly realised.** Bear: fragmentation of liquidity across old/new rails — contained to pilots.
## 7. Open Threads
Marketnode's inheritance of P3 designs (SGX/Temasek JV — ACRA pull). Whether MAS has ever mapped P3's arbitration template onto retail PBM — no public evidence.
## 8. Sources
[id P7] papers/07, primary. Cross: [id P1][id P2 STELLA][ASX CHESS].



================================================================================
# ══ [P8] — 08_jasper_ubin
================================================================================


---
### ─── 1_intake.md ───

# INTAKE — 08 Jasper–Ubin Design Paper (2019)
SUBJECT: First cross-border, cross-currency, cross-platform atomic W-CBDC payment — CAD (Corda/Jasper) ↔ SGD (Quorum/Ubin) via Hash Time-Locked Contracts, no trusted third party.
SOURCE / RELIABILITY: **Primary**; Bank of Canada + MAS, delivered with JPM + Accenture.
ENTITIES: BoC (Scott Hendry) · MAS (Mohanty) · JPM · Accenture · HTLC as the named mechanism.
KEY CLAIMS: Atomic all-or-nothing CAD-SGD transfer achieved across heterogeneous platforms; trust relocated "in the technical system rather than in a third party"; open questions candidly listed — scale, many-jurisdiction complexity, governance of protocol updates, legal/regulatory, non-DLT RTGS integration.
CONTRADICTIONS w/ KB: None; the HTLC method is the same primitive Cedar×Ubin [id P11] re-validates in 2022 — three years of re-proving the same atom.
CLASSIFY: Cross-border wholesale CBDC · tags: HTLC, atomicity, Corda, Quorum, BoC.
SIGNIFICANCE: Establishes the bilateral-corridor model and its ceiling: HTLC solves the two-party atom, not the N-jurisdiction network — the gap Dunbar then attacks from the platform side and Mandala from the compliance side.
ROUTE: → map → SA note. [id P8]



---
### ─── 2_knowledge-map.md ───

# KNOWLEDGE MAP — 08 Jasper–Ubin
## Alphas
**A1 — Trust was relocated, not removed.** The paper's own admission: HTLC shifts trust from correspondent banks into code + timeout parameters. Timeout selection, platform bugs, and protocol governance become the new counterparty risk — unpriced.
**A2 — The bilateral ceiling.** HTLC scales as corridors (N² problem), not networks. Everything after — Dunbar's common platform, Mandala's compliance proofs — is the system discovering this limit and routing around it.
**A3 — The candour benchmark.** Jasper–Ubin's open-questions list (governance, legality, scale) is the most honest in the Ubin corpus; later reports narrow, not answer, these questions.
## Quadrants
KK: HTLC mechanics (lock, secret, timeout), CAD-SGD atomic PoC, Corda↔Quorum bridge. KU: scale, N-jurisdiction, non-DLT integration, protocol-update governance. UK: descends from the tri-central-bank models paper [id P9]; JPM's position inside both legs (and later Onyx/Partior) — the private beneficiary of public corridor research. UU: *timeout risk as the new Herstatt* — a mis-set HTLC window recreates settlement risk in miniature, nowhere quantified; *who runs the bridge* — the interop layer between two sovereign ledgers has no proposed owner, the void GL1 later claims.
## Narrative Vector
Validates the atom, exposes the network problem. Read as the moment cross-border CBDC research split into three roads: corridors (this), platforms (Dunbar), compliance layers (Mandala).



---
### ─── 3_sa-report.md ───

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



================================================================================
# ══ [P9] — 09_crossborder
================================================================================


---
### ─── 1_intake.md ───

# INTAKE — 09 Cross-Border Interbank Payments & Settlements (2019)
SUBJECT: Tri-central-bank problem-definition report (BoC/BoE/MAS + HSBC-led commercial group) — root causes of cross-border friction and three future-state models, incl. three W-CBDC variants.
SOURCE / RELIABILITY: **Primary** policy analysis; KPMG-facilitated; explicitly hypothetical — "not intended to pick a model."
ENTITIES: BoC · BoE · MAS · HSBC (lead) · OCBC · TD · UOB · KPMG · SWIFT (structural presence).
KEY CLAIMS: Cross-border value US$22tn (2016) → US$30tn (2022E) while active correspondent banks fell 8% (2011–17) — demand up, capacity concentrating. Root causes: multi-entity chains, AML/CTF/KYC duplication, divergent standards, legacy rails. Three models: (1)(2) enhance existing systems — partial fixes; (3) W-CBDC in three variants incl. currency-basket W-CBDC. Verdict: incremental change insufficient; paradigm shift may be needed.
CONTRADICTIONS w/ KB: None; this is the parent problem-statement Jasper–Ubin operationalises.
CLASSIFY: Cross-border payments policy · tags: correspondent banking, W-CBDC models, de-risking.
SIGNIFICANCE: The de-risking datum (8% correspondent decline) is the political economy engine of the whole cross-border track — concentration risk dressed as innovation opportunity.
ROUTE: → map → SA note. [id P9]



---
### ─── 2_knowledge-map.md ───

# KNOWLEDGE MAP — 09 Cross-Border Report
## Alphas
**A1 — De-risking is the burning platform.** Volumes rising toward $30tn while correspondent capacity shrinks 8%: fewer intermediaries carrying more flow. Central banks aren't innovating for fun; they're hedging a concentrating private utility.
**A2 — The basket W-CBDC variant is the quiet radical.** A wholesale CBDC backed by a currency basket — sketched here, never pursued publicly — is the SDR-adjacent idea buried in an official trilateral report. Libra was pilloried for the same shape months later.
**A3 — HSBC as scribe.** The lead commercial author is the world's correspondent-banking incumbent; the "future-state capabilities" list reads as what incumbents can live with. Models 1–2 (enhance existing rails) got the real-world investment.
## Quadrants
KK: pain-point taxonomy, 3 models + 3 W-CBDC variants, cost/opacity/speed evidence. KU: operationalisation of any model (explicitly deferred). UK: SWIFT's gravitational field — every model is implicitly measured against not-breaking SWIFT; BoE RTGS renewal running in parallel as the Model-1 bet. UU: *de-risking's AML origin* — the correspondent decline is regulator-caused (compliance cost), so central banks are proposing tech fixes to a problem their own rulebooks created; Mandala [id P13] eventually addresses this root directly, five years later.
## Narrative Vector
Reframes the corpus: the cross-border track is defensive infrastructure policy responding to correspondent-bank concentration, with W-CBDC as the escalation option. The report's own honesty ("incremental changes... may need a paradigm shift") licenses everything after it.



---
### ─── 3_sa-report.md ───

# SA INWARD NOTE — Cross-Border Payments Report (2019) [id P9]
## 1. Executive Summary
[id P9] The BoC/BoE/MAS report is the problem statement of the entire cross-border track: $22tn→$30tn flows against an 8% decline in correspondent banks, driven by compliance-cost de-risking. It offers three models — two incremental, one W-CBDC in three variants including a currency-basket token — and concludes incrementalism may not suffice. It deliberately decides nothing; its function was to license the decade of experiments that followed and to put the basket-CBDC idea on official paper without owning it.
## 2. Entity Map
BoC, BoE, MAS (principals) | HSBC (lead commercial — correspondent incumbent) | OCBC, TD, UOB | KPMG (facilitator) | SWIFT (unnamed constant).
## 3. Mechanics
[id P9] Root causes: multi-entity chains, duplicated AML/KYC, divergent standards, legacy tech. Models: (1) enhanced domestic systems, (2) expanded access/linkage, (3) W-CBDC — single-currency, multi-currency, basket-backed.
## 4. Pattern
[id P9] Parent node: Jasper–Ubin [id P8] tests Model 3 plumbing; Dunbar [id P14] tests the shared-platform version; Mandala [id P13] attacks the compliance root cause. BoE's RTGS renewal = Model 1 in production. The family tree resolves cleanly from this document.
## 5. Quantification
$22tn (2016) → $30tn (2022E) at 5.5%/yr; correspondent banks −8% (2011–mid-2017). The concentration ratio implied — more flow through fewer nodes — is the systemic-risk number nobody prints.
## 6. Bull / Base / Bear
Bull: paradigm shift to W-CBDC networks. Base: incremental fixes (ISO 20022, SWIFT gpi, instant-payment linkage) absorb the pressure; W-CBDC stays experimental. **Base realised to date.** Bear: continued de-risking strands corridors (partially realised in EM/Pacific corridors).
## 7. Open Threads
Whether the basket W-CBDC variant survives anywhere in later official work (mBridge-adjacent watch). Current correspondent-count trend post-2017 — refresh the de-risking datum.
## 8. Sources
[id P9] papers/09, primary. Cross: [id P8][id P13][id P14], BIS CPMI de-risking series.



================================================================================
# ══ [P10] — 10_ubin_p5
================================================================================


---
### ─── 1_intake.md ───

# INTAKE — 10 Ubin Phase 5: Enabling Broad Ecosystem Opportunities (2020)
SUBJECT: Capstone — "Ubin V" multi-currency payments network built to production fidelity (production-grade infra, bank production standards) with commercial use-case integration and future-of-payments design concepts.
SOURCE / RELIABILITY: **Primary**; MAS + **Temasek + J.P. Morgan** with Accenture — note the shift from consortium-of-banks to a state-capital + single-bank axis.
ENTITIES: MAS · Temasek · JPM · Accenture · use-case partners across capital markets, trade finance, insurance · github.com/project-ubin (APIs public, incl. ESCROW.* message set).
KEY CLAIMS: Multi-currency network on one platform; phases 1–4 solved technical feasibility, P5 proves *value*; workshops produced user-driven functionality set; governance of common platforms framed as the binding constraint ("trust is not binary"); design concepts offered for future payment infrastructure.
CONTRADICTIONS w/ KB: None; the corporate epilogue (Partior, the JPM/DBS/Temasek JV commercialising this work) is outside the paper but is the paper's true conclusion.
CLASSIFY: Wholesale multi-currency infrastructure · tags: Ubin V, Temasek, JPM, escrow APIs, Partior lineage.
SIGNIFICANCE: The privatisation node — public research consortium narrows to the two parties who then commercialise it.
ROUTE: → map → SA note. [id P10]



---
### ─── 2_knowledge-map.md ───

# KNOWLEDGE MAP — 10 Ubin Phase 5
## Alphas
**A1 — The exit was the point.** P1's eleven-bank consortium becomes P5's MAS+Temasek+JPM trio; within a year the same trio's commercial echo (Partior: JPM/DBS/Temasek) launches with the multi-currency settlement mandate Ubin V prototyped. Public R&D → private JV, cleanly executed. Who captured the option value of five years of convened research is a fair and unasked question.
**A2 — Governance named as the real problem.** P5's most durable text: no single party is trusted to hold central-bank liabilities across borders, but "trust is not binary" — less-critical functions can be centralised where incentives suffice. This sentence is the intellectual seed of both Dunbar's platform governance and GL1's operating-company model.
**A3 — Escrow as first-class primitive.** The public API set ships ESCROW.INIT/SIGN/ENQUIRY/NOTIFY with release/revert/**dispute** actions — wholesale rails got a dispute verb in their message schema; retail PBM still lacks one. Second sighting of the recourse asymmetry ([id P7]).
## Quadrants
KK: Ubin V architecture, production-fidelity claim, use-case survey, API/github publication. KU: commercial/operating model, cross-network connectivity models. UK: Partior's imminent formation; Temasek's dual role as state investor and network participant. UU: *option-value capture* (above); *the SWIFT accommodation* — P5 praises SWIFT's cooperative model while sketching its replacement, the diplomatic ambiguity that lets both futures be pursued.
## Narrative Vector
Shifts the Ubin story from technology to industrial policy: the programme's deliverable was a commercialisable network and a chosen set of commercial champions. Everything the sentiment mandate needs to say about public-private value transfer has its cleanest example here.



---
### ─── 3_sa-report.md ───

# SA INWARD NOTE — Ubin Phase 5 (2020) [id P10]
## 1. Executive Summary
[id P10] P5 closed Project Ubin by building Ubin V — a multi-currency payments network at production fidelity — with MAS, Temasek and J.P. Morgan as principals and the broader ecosystem as consulted users. Its stated purpose was proving value; its structural effect was selecting commercial champions: the Partior JV (JPM/DBS/Temasek) commercialised the design within a year. The report's lasting analytical contribution is its governance framing — trust as a spectrum allocatable by function — and its escrow API with an explicit dispute action, the second wholesale sighting of recourse machinery absent from retail PBM.
## 2. Entity Map
MAS | Temasek (state capital) | JPM | Accenture | use-case cohort (capital markets, trade finance, insurance) | github.com/project-ubin.
## 3. Mechanics
[id P10] Multi-currency single-platform settlement; production-grade infra; ESCROW message set with release/revert/dispute; connectivity concepts for common platforms vs interlinked networks.
## 4. Pattern
[id P10] Consortium narrowing P1→P5 (11 banks → 1 bank + sovereign fund); public-to-private handoff (→ Partior); governance text seeds Dunbar [id P14] and GL1. Recourse asymmetry recurs ([id P7]).
## 5. Quantification
None published on unit economics — consistent with a report whose commercial answer arrived as a JV, not a table.
## 6. Bull / Base / Bear (on the Ubin V lineage)
Bull: Partior becomes the multi-currency wholesale settlement utility for Asia — partially in motion. Base: Partior grows corridor-by-corridor among founder banks; MEPS+/SWIFT persist. **Current state.** Bear: founder concentration deters rival banks, network stalls at club scale — live risk.
## 7. Open Threads
Partior cap table + MAS's regulatory posture toward its own research's commercial child (ACRA + licensing register pull). Whether Ubin V escrow/dispute schema persists in Partior production APIs.
## 8. Sources
[id P10] papers/10, primary. Cross: [id P5]-[id P8], [id P14], Partior public materials.



================================================================================
# ══ [P11] — 11_cedar_ubin
================================================================================


---
### ─── 1_intake.md ───

# INTAKE — 11 Project Cedar Phase II × Ubin+ (Nov 2022)
SUBJECT: NY Fed NYIC × MAS experiment — wholesale cross-border FX through **vehicle currencies** across heterogeneous DLT ledgers via HTLC; atomic settlement in under 30 seconds across multi-hop payment chains.
SOURCE / RELIABILITY: **Primary**; joint NYIC/MAS report with unusually heavy disclaimers (no policy signal, no CBDC decision implied — Fed sensitivities visible).
ENTITIES: FRBNY / NYIC · MAS (Ubin+ programme) · BISIH partnership context · vehicle-currency FX structure (illiquid pair → USD/SGD bridge).
KEY CLAIMS: Hypotheses validated on interoperability, speed, atomicity; settlement <30s in all scenarios incl. multi-hop chains; each participant's claim conditional on all claims (counterparty risk reduced); limitations candid — scale, privacy (Sepolia public testnet), liquidity optimisation open; PTLC and ZKP flagged as future work.
CONTRADICTIONS w/ KB: None; technically a re-validation of Jasper–Ubin's HTLC primitive extended to multi-hop vehicle-currency chains.
CLASSIFY: Cross-border wholesale FX · tags: NYIC, vehicle currency, HTLC, Ubin+, EME pairs.
SIGNIFICANCE: The signalling is the substance — MAS pairing with the NY Fed anchors Singapore in the USD-corridor conversation; the illiquid-EME-pair framing targets exactly the corridors correspondent de-risking [id P9] abandoned.
ROUTE: → map → SA note. [id P11]



---
### ─── 2_knowledge-map.md ───

# KNOWLEDGE MAP — 11 Cedar × Ubin+
## Alphas
**A1 — Vehicle currency = USD, formalised.** The experiment's structure enshrines the bridge-currency role in the settlement layer itself. A "future-state" system built this way hard-codes dollar (and by courtesy SGD) centrality — dollarisation as protocol design, wearing neutrality language.
**A2 — The partnership is the payload.** Three years after Jasper–Ubin proved HTLC atomicity, re-proving it with the NY Fed adds little science and much positioning: MAS becomes the Fed's default Asian counterpart in wholesale digital-dollar research.
**A3 — Sub-30s is the first real performance number.** The corpus's chronic omission (latency/cost vs correspondent baseline) finally gets a datum — under 30 seconds across multi-hop chains, on toy infrastructure (m5.large VMs). Honest about scale limits.
## Quadrants
KK: HTLC multi-hop chains, vehicle-currency FX mechanics, <30s result, system metrics appendix. KU: scale-up, PTLC alternatives, ZKP privacy, non-DLT integration. UK: BISIH/NYIC institutional context; the EME-pair focus as response to de-risked corridors [id P9]; Ubin+ as Ubin's international continuation brand. UU: *protocol-level dollar entrenchment* (above) — no participating author can say it, so nobody does; *liquidity-provision economics of on-chain vehicle currencies* — who market-makes the bridge leg and at what spread is the commercial question the experiment structurally cannot ask.
## Narrative Vector
Technically confirmatory, strategically declarative: Singapore inserts itself into the USD wholesale-settlement future while the science re-treads 2019. For the mandate: cite it as evidence MAS's cross-border track is diplomacy conducted by prototype.



---
### ─── 3_sa-report.md ───

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



================================================================================
# ══ [P14] — 14_dunbar
================================================================================


---
### ─── 1_intake.md ───

# INTAKE — 14 Project Dunbar: International Settlements Using Multi-CBDCs (Mar 2022)
SUBJECT: BISIH SG + RBA/BNM/MAS/SARB — a **single shared platform** hosting multiple CBDCs (BIS "model 3") so central and commercial banks transact directly across borders; prototypes by R3 and Partior.
SOURCE / RELIABILITY: **Primary**; BIS report; unusually candid — "ended with more questions than answers."
ENTITIES: BISIH SG · RBA · BNM · MAS · SARB · R3 + **Partior** (prototype builders — the Ubin V commercial child now building BIS prototypes) · G20/FSB roadmap building block 19.
KEY CLAIMS: Common platform (model 3) chosen over compatible (1) / interlinked (2) systems; default PvP for all FX; addresses fragmentation head-on; central banks' core discomfort named — liabilities issued/recorded on a platform outside their control; open questions catalogued across policy, business, technology; framed as an open call for collaboration.
CONTRADICTIONS w/ KB: None; the platform strand complementing corridors [id P8] and compliance [id P13]. Mandala later tests against Dunbar prototypes — the strands interlock.
CLASSIFY: Multi-CBDC platform · tags: model 3, mCBDC, BISIH, SARB, Partior.
SIGNIFICANCE: The maximal architecture — and the honest documentation of why sovereigns resist it. Its unsolved governance question is GL1's founding inheritance.
ROUTE: → map → SA note. [id P14]



---
### ─── 2_knowledge-map.md ───

# KNOWLEDGE MAP — 14 Project Dunbar
## Alphas
**A1 — Sovereignty is the binding constraint, stated plainly.** No central bank will let its liability be issued/recorded on infrastructure outside its control; there is no natural operator all trust. Dunbar proves the tech and documents why the tech is not the problem — the same governance wall [id P8] and [id P10] hit, now with four flags planted on it.
**A2 — Partior building BIS prototypes closes a loop.** The commercial JV born of Ubin V returns as contractor to the multilateral successor programme. Public research → private company → public research's vendor, in 24 months. The revolving door is infrastructural.
**A3 — "More questions than before it started" is the finding.** Dunbar's candour converts it from failed platform pitch into the field's honest problem census — the direct predecessor of both Mandala (compliance subset) and GL1 (governance/operating-company subset).
## Quadrants
KK: model 1/2/3 taxonomy, model-3 choice, PvP-by-default, R3+Partior prototypes, G20 BB19 alignment. KU: the catalogued open questions (access, jurisdiction, governance, resilience). UK: SARB's presence = deliberate global-south legitimacy; Project Atom/Khokha lineages folded in; the correspondent super-structure it would displace. UU: *the operator vacuum as market opportunity* — if no sovereign can operate it, a neutral operating company must, which is precisely GL1's later design; Dunbar creates the demand for the entity GL1 proposes; *exit asymmetry* — nothing on how a central bank leaves a shared platform, the analogue of [id P5]'s missing unwind analysis at sovereign scale.
## Narrative Vector
Dunbar reframes the platform dream as a governance problem with a technology demo attached. Its unanswered questions are not residue — they are the product, and GL1 is their commercial answer. For the mandate: the arc "corridors → platform → operating company" is the cleanest one-slide history of where this is all going.



---
### ─── 3_sa-report.md ───

# SA INWARD NOTE — Project Dunbar (BIS, Mar 2022) [id P14]
## 1. Executive Summary
[id P14] Dunbar prototyped the maximal architecture — one shared platform hosting multiple CBDCs with default PvP — with Australia, Malaysia, Singapore and South Africa, built by R3 and Partior. It validated the technology and then documented, with rare candour, why technology was never the constraint: no sovereign will host its liability on infrastructure it doesn't control, and no operator exists that all trust. The report ends with a catalogued problem set rather than a solution, and that catalogue is its legacy — Mandala takes the compliance subset, GL1 takes the governance/operating-company subset.
## 2. Entity Map
BISIH SG | RBA, BNM, MAS, SARB | R3 + Partior (builders) | G20/FSB roadmap BB19 context.
## 3. Mechanics
[id P14] Model 3 (single mCBDC system) vs models 1–2; direct central/commercial bank participation; PvP by default; prototypes on two stacks; open-question taxonomy across policy/business/technology.
## 4. Pattern
[id P14] Partior's contractor role closes the Ubin V loop ([id P10]) — public→private→public-vendor in two years. Sovereignty wall recurs from [id P8]/[id P10]; Mandala [id P13] later tests against Dunbar builds. The three strands (corridor, platform, compliance) are one programme viewed from three angles.
## 5. Quantification
None — appropriately, since the binding constraints identified are non-quantitative (trust, control, governance).
## 6. Bull / Base / Bear
Bull: regional mCBDC platform emerges among aligned jurisdictions with a neutral operating company — the GL1 bet. Base: Dunbar's census guides successor projects; no deployment this cycle. **Current state.** Bear: mCBDC platforms fragment along geopolitical lines (mBridge vs GL1-aligned tracks) — visibly underway.
## 7. Open Threads
GL1 operating-company progress as Dunbar's answer — track. mBridge divergence (BIS exit dynamics) as the geopolitical bear case. Central-bank exit mechanics from shared platforms — still unwritten anywhere.
## 8. Sources
[id P14] papers/14, primary. Cross: [id P8][id P10][id P13], BIS Papers no 115 (Auer et al), G20/FSB roadmap.



================================================================================
# ══ [P13] — 13_mandala
================================================================================


---
### ─── 1_intake.md ───

# INTAKE — 13 Project Mandala: Streamlining Cross-Border Transaction Compliance (Oct 2024)
SUBJECT: BISIH Singapore Centre + RBA/BOK/BNM/MAS (with Bank of France contributions) — compliance-by-design: encode jurisdictional rules (sanctions, CFM) into a P2P protocol; generate cryptographic **proof of compliance** attached to wCBDC or Swift instructions before funds release.
SOURCE / RELIABILITY: **Primary**; BIS Innovation Hub report, PoC stage, heavy experimental disclaimers.
ENTITIES: BISIH SG (Maha El Dimachki) · RBA · BOK · BNM · MAS · BdF · tech: ZKP (SNARK/STARK), MPC, Google PJC, LEI/GLEIF, opensanctions.org · use cases: SG–MY lending CFM+sanctions; KR–AU securities financing.
KEY CLAIMS: Three components — P2P messaging, rules engine, proof engine; checks pre-validated ex ante, proof travels with payment; integrates with both wCBDC prototypes (tested against Partior and R3 Dunbar builds) and Swift (ISO 20022 change request CR1357 pathway); banks retain interpretive responsibility for regulation; privacy via ZKP/MPC — no unencrypted data leaves the bank; real-time regulator monitoring explored.
CONTRADICTIONS w/ KB: None. Directly answers the compliance root cause [id P9] identified in 2019; also note: this is the same "compliance-by-design" phrase the PBM whitepaper [id P1] uses for its cross-border use case — retail and wholesale tracks converging on one doctrine.
CLASSIFY: Cross-border compliance infrastructure · tags: compliance-by-design, ZKP, CFM, sanctions, ISO 20022.
SIGNIFICANCE: The regulatory state renders itself as protocol. Also the strongest privacy engineering in the corpus — applied to institutions.
ROUTE: → map → SA note. [id P13]



---
### ─── 2_knowledge-map.md ───

# KNOWLEDGE MAP — 13 Project Mandala
## Alphas
**A1 — Compliance becomes infrastructure, and infrastructure becomes compliance.** Once rules are encoded and proofs travel with money, the distinction between "regulation" and "payment system" dissolves. Mandala is the wholesale twin of the PBM wrapper: both make policy execute at the transaction layer. The doctrine now spans citizen vouchers to interbank CFM.
**A2 — Privacy tech deployed where the protected party is a bank.** ZKP/MPC ensure no unencrypted data leaves the institution — world-class privacy engineering, for institutional data. Third sighting of the asymmetry: recourse and privacy machinery consistently appear on the wholesale side first ([id P7][id P10]).
**A3 — De-risking's actual fix.** [id P9] showed compliance cost shrinking correspondent capacity; Mandala attacks that root — pre-validated compliance could restore corridor economics. If it works, it does more for cross-border payments than any CBDC in the corpus.
## Quadrants
KK: 3-component architecture, 2 live-rule use cases (SG-MY CFM, KR-AU sanctions), dual integration (wCBDC + Swift/ISO 20022 CR1357), ex-ante model. KU: legal/commercial viability, mutual-reliance frameworks between regulators, settlement-layer privacy. UK: descends from Dunbar's open problems; complements ex-post detection (Aurora/Hertha); Partior + R3 Dunbar prototypes as test substrates — the private/public strands re-braiding. UU: *rule ossification risk* — encoded CFM rules must be updated at the speed of regulation; the protocol-governance question from [id P8] returns wearing a compliance badge, unanswered; *asymmetric transparency* — regulators gain real-time monitoring of institutions while citizens' visibility into the rules applied to them gains nothing; nobody notes the direction of the one-way mirror.
## Narrative Vector
Completes the doctrinal arc: from programmable money ([id P1]) to programmable regulation. The corpus's endpoint is a financial system where rules self-execute at every layer — the sentiment question ("who consents to the rules in the machine") is now the only unbuilt component.



---
### ─── 3_sa-report.md ───

# SA INWARD NOTE — Project Mandala (BISIH, Oct 2024) [id P13]
## 1. Executive Summary
[id P13] Mandala encodes jurisdiction-specific compliance — sanctions screening, capital-flow management — into a decentralised protocol whose cryptographic proof of compliance travels with the payment and gates fund release. It pre-validates ex ante what today is checked expensively and repeatedly mid-chain, and it integrates with both nascent wCBDC systems (tested on Partior and R3 Dunbar builds) and Swift via an ISO 20022 pathway. It is the direct fix for the compliance-cost root cause identified in the 2019 trilateral report, the wholesale twin of the PBM wrapper doctrine, and the corpus's most advanced privacy engineering — deployed in service of institutions, with regulators gaining real-time monitoring and citizens gaining nothing visible.
## 2. Entity Map
BISIH SG (El Dimachki) | RBA, BOK, BNM, MAS | BdF (contributor) | tech: ZKP, MPC/PJC (Google), LEI/GLEIF, OpenSanctions | substrates: Partior, R3-Dunbar.
## 3. Mechanics
[id P13] P2P messaging + rules engine (jurisdiction rulesets → computational checks) + proof engine (non-interactive/interactive/local checks); proof attaches to wCBDC or MT/ISO instruction; funds release only on proof; banks retain interpretive responsibility (regulatory model preserved).
## 4. Pattern
[id P13] Doctrinal convergence with [id P1] ("compliance-by-design" verbatim); answers [id P9]'s root cause; inherits [id P8]'s unresolved protocol-update governance; privacy/recourse asymmetry third sighting ([id P7][id P10]). Ex-ante Mandala complements ex-post Aurora/Hertha — the Hub is assembling a full-stack regulatory machine.
## 5. Quantification
Efficiency gains asserted (fewer failed txns, STP, fewer intermediaries) but explicitly unquantified — "more analysis needed" on compliance-cost reduction. The decisive number (cost per compliant cross-border payment, before/after) remains unpublished.
## 6. Bull / Base / Bear
Bull: mutual-reliance frameworks form; Mandala-class proofs become the ISO 20022 norm; correspondent de-risking partially reverses. Base: Phase 2 extends use cases; adoption waits on legal recognition of proofs — multi-year. **Likely.** Bear: rule-encoding liability (who answers for a wrong proof) stalls production use; ossified rulesets lag regulation and create false compliance.
## 7. Open Threads
Legal status of a cryptographic compliance proof in each jurisdiction — the make-or-break question, unaddressed. CR1357 fate in the ISO 20022 process. Phase 2 scope (BdF/RBI/CBK/BSP roster on the BIS topic page) — refresh.
## 8. Sources
[id P13] papers/13, primary. Cross: [id P1][id P8][id P9][id P14], BIS Aurora/Hertha, FATF/FSB alignment claims in-doc.



================================================================================
# ══ [P12] — 12_gl1
================================================================================


---
### ─── 1_intake.md ───

# INTAKE — 12 Global Layer One Whitepaper (Jun 2024)
SUBJECT: MAS-convened design for a shared ledger infrastructure — "public permissioned" (Model 3) network operated by regulated FIs via **GL1 Operating Companies**, hosting tokenised assets/money across jurisdictions with DvP/PvP/DvPvP composability.
SOURCE / RELIABILITY: **Primary**; MAS publication with BNY, Citi, MUFG, Onyx (JPM), SocGen-FORGE.
ENTITIES: MAS · BNY · Citi · MUFG · Onyx · SocGen-FORGE · BIS "Finternet"/Unified Ledger cited · GL1 OpCo [NEW — the industry utility construct].
KEY CLAIMS: Three network models — public permissionless (unaccountable, no SLA, unsuitable), private permissioned (fragmenting liquidity), **public permissioned** (open to any qualifying entity, activities restricted, FI-operated nodes, KYC'd participants) as the synthesis; asset-agnostic; trapped-liquidity thesis; institutional-grade DeFi protocols (AMMs with safeguards); rollout select-jurisdictions-first.
CONTRADICTIONS w/ KB: None — GL1 is the direct answer to Dunbar's operator vacuum [id P14] and generalises the Blueprint's OCL [id P4] internationally.
CLASSIFY: Shared infrastructure · tags: GL1, OpCo, public permissioned, Finternet.
SIGNIFICANCE: The concession architecture goes global: whoever sits in the OpCo consortium owns the settlement layer of tokenised finance. Five global banks are already at the table; the table is the product.
ROUTE: [id P12]



---
### ─── 2_knowledge-map.md ───

# KNOWLEDGE MAP — 12 GL1
## Alphas
**A1 — The OpCo is Dunbar's missing operator, incorporated.** Dunbar proved no sovereign can run the shared platform; GL1's answer is an industry utility run by a bank consortium. The governance vacuum becomes a company — and the five contributors (BNY, Citi, MUFG, Onyx, SocGen) are the presumptive shareholders of tokenised finance's TCP/IP.
**A2 — "Public permissioned" is a franchise, worded as openness.** Open to "any entity that fulfils the criteria" — with the criteria set by the incumbents operating the nodes. Model 3 rhetoric imports internet-scale legitimacy while the KYC gate keeps internet-scale participation out.
**A3 — MAS exports the Blueprint.** GL1 is the OCL pattern [id P4] scaled from Singapore-domestic to cross-jurisdictional — same whitelist logic, same designated-operator logic, now with BIS Finternet framing as air cover.
## Quadrants
KK: 3-model taxonomy, OpCo construct, asset-agnostic scope, DvP/PvP/DvPvP composability, trapped-liquidity motivation. KU: OpCo governance detail, jurisdiction rollout order, regulatory perimeter per jurisdiction. UK: Dunbar inheritance; Partior overlap (same JPM/settlement space — GL1 vs Partior lane-division unstated); Onyx's presence in both. UU: *OpCo antitrust surface* — a bank-owned utility setting participation criteria for competitors is a competition-law question nobody in the paper touches; *sovereignty round-trip* — Dunbar said sovereigns won't cede control to a shared platform, GL1's answer hands control to private banks instead, which solves the central-bank objection by creating a bigger one for everyone else.
## Narrative Vector
GL1 completes the arc: decentralisation explored (P2) → declined (P4) → re-offered as a bank-consortium franchise wearing open-network language. For the mandate: "who governs the operating company" is the next decade's question, and MAS is convening the answer.



---
### ─── 3_sa-report.md ───

# SA INWARD NOTE — GL1 Whitepaper (Jun 2024) [id P12]
## 1. Executive Summary
[id P12] GL1 proposes the settlement fabric for tokenised finance: a "public permissioned" shared ledger operated by GL1 Operating Companies — bank-consortium utilities — hosting tokenised money and assets with composable DvP/PvP/DvPvP. It is Dunbar's unsolved operator problem answered by incorporation, and the Orchid Blueprint's gatekeeping pattern exported cross-border. The five contributing institutions (BNY, Citi, MUFG, Onyx, SocGen-FORGE) sit at a table whose seat allocation *is* the economic prize; the openness language describes the membership form, not the power structure.
## 2. Entity Map
MAS (convener) | BNY, Citi, MUFG, Onyx/JPM, SocGen-FORGE (contributors/presumptive OpCo core) | BIS (Finternet/Unified Ledger intellectual cover) | absent: any buy-side, any non-G-SIB, any citizen-facing body.
## 3. Mechanics
[id P12] Model taxonomy → public permissioned synthesis; FI-operated nodes, KYC'd participants, restricted activities; asset-agnostic multi-currency hosting; institutional-grade protocols (safeguarded AMMs); select-jurisdiction rollout.
## 4. Pattern
[id P12] OCL [id P4] → GL1: identical concession logic at two scales. Dunbar [id P14] → GL1: vacuum → OpCo. Onyx bridges GL1 and Partior — JPM positioned on both candidate fabrics. The corpus's repertory-company pattern goes global with a heavier cast.
## 5. Quantification
None published; the addressable stake is the fee/float pool of tokenised settlement (BCG/ADDX US$16tn-by-2030 tokenisation forecast cited in the Guardian track as the industry's own sizing).
## 6. Bull / Base / Bear
Bull: GL1 OpCos launch in 2–3 jurisdictions; network effects consolidate; contributors capture utility economics. Base: extended standards-building; pilots on existing rails (Partior et al.) while GL1 governance gestates. **Likely near-term.** Bear: antitrust/sovereignty objections stall OpCo formation; fabric race fragments (GL1 vs Partior vs regional unified-ledger builds) — reproducing the fragmentation GL1 exists to solve.
## 7. Open Threads
OpCo incorporation status, domicile, shareholding — track MAS announcements. GL1↔Partior lane division (both Onyx-adjacent). Competition-law analysis of bank-owned participation criteria — unowned, advisory whitespace.
## 8. Sources
[id P12] papers/12, primary. Cross: [id P4][id P14], BIS Finternet (Carstens & Nilekani 2024), BIS Unified Ledger (2023).



================================================================================
# ══ [G7] — g7_open_networks
================================================================================


---
### ─── 1_intake.md ───

# INTAKE — G7 Guardian: Enabling Open & Interoperable Networks (Jun 2023)
SUBJECT: Guardian's foundational framework — digital-asset network archetypes, FMI principles applied to token networks, FIs as **trust anchors** issuing verifiable credentials.
SOURCE / RELIABILITY: **Primary**; MAS + **BIS co-authors** (Tara Rice, Shirakami, Hancock) — unusual joint authorship.
ENTITIES: **Alan Lim (MAS, lead co-author — KB: the PBM mandate approach target)** · Vincent Pek, Darren Tng, Nigel Lam, Ong Chin Sin (MAS) · BIS trio · contributors: DBS, HSBC, **Marketnode** (SGX/Temasek JV — confirms [id P7] open thread), JPM (**Naveen Mallela + Toh Wee Kee — Toh was MAS in Ubin P1, now JPM**), SBI DAH, StanChart, UOB · MAS depts MPI/PPD/TCRD.
KEY CLAIMS: Tokenisation of real assets (not crypto speculation — Menon line cited) is where value lies; BCG/ADDX US$16tn by 2030; governance spectrum (centralised/consortium/decentralised) with FSB DeFi-concentration critique; network effect maths (Metcalfe) — public networks reach millions, private thousands; FIs as trust anchors for credentialed participation; three interop approaches (common infra / layered global base / interlinked networks).
CONTRADICTIONS w/ KB: None. The "layered global base" option = GL1's seed, one year early.
CLASSIFY: Tokenisation frameworks · tags: Guardian, trust anchors, FMI principles, Alan Lim.
SIGNIFICANCE: **Mandate-critical**: Alan Lim's authored worldview is in this document — engagement material for the approach.
ROUTE: [id G7]



---
### ─── 2_knowledge-map.md ───

# KNOWLEDGE MAP — G7 Open & Interoperable Networks
## Alphas
**A1 — Alan Lim's intellectual fingerprint.** The approach target co-wrote Guardian's constitutional text: pro-tokenisation, anti-speculation, FMI-principles-first, FIs-as-trust-anchors. Pitch language that mirrors this frame (responsible innovation, trust anchoring, interoperability-with-safeguards) meets him where he has publicly committed.
**A2 — Trust anchors = the licensing of identity.** Making regulated FIs the issuers of verifiable credentials extends the bank franchise from money to identity itself — participation in tokenised markets becomes downstream of a bank relationship. The Blueprint gated who programs; G7 gates who *exists* on-network.
**A3 — The revolving door has a name.** Toh Wee Kee: MAS (Ubin P1 author, 2017) → JPMorgan (G7 contributor, 2023). With Mallela's decade-long JPM constancy, the public-private membrane in SG digital money is visibly permeable — context for how the ecosystem actually coordinates.
## Quadrants
KK: archetype taxonomy, FMI-principles mapping, trust-anchor model, 3 interop approaches, honest public-vs-private network-effect data. KU: which approach wins (deferred); credential-scheme liability. UK: Menon's "yes tokenisation / no crypto" line as the political frame; Marketnode's presence confirming the SGX digital lineage [id P7]; FSB DeFi-concentration critique doing double duty as permissioned-model advocacy. UU: *identity-layer concentration risk* — trust-anchor failure or de-platforming has no appeal path (the recourse gap recurs at the identity layer); *the Metcalfe concession* — the paper admits public networks reach millions vs private thousands, then the programme builds private-shaped "public permissioned" anyway; the trade-off is acknowledged and overridden without a stated price.
## Narrative Vector
G7 is the doctrine paper: it sets the vocabulary (trust anchors, open-and-interoperable, responsible innovation) the rest of Guardian and GL1 inherit. For the mandate, it doubles as a psychographic source on Alan Lim — engage on his own published terms.



---
### ─── 3_sa-report.md ───

# SA INWARD NOTE — Guardian: Open & Interoperable Networks (2023) [id G7]
## 1. Executive Summary
[id G7] Guardian's foundational framework, co-authored by MAS (Alan Lim lead) and the BIS, defines the archetypes and rules of engagement for tokenised-asset networks: FMI principles apply, regulated FIs serve as trust anchors issuing credentials, and interoperability comes via common infrastructure, a layered global base (GL1's seed), or interlinked networks. It candidly concedes public networks' order-of-magnitude reach advantage, then the programme proceeds permissioned regardless. Its highest immediate value to the practice is biographical: the approach target's published doctrine is here, citable line by line.
## 2. Entity Map
MAS: **Alan Lim**, Pek, Tng, Lam, Ong + MPI/PPD/TCRD | BIS: Rice, Shirakami, Hancock | DBS, HSBC, StanChart, UOB, SBI DAH | JPM (Mallela, **Toh Wee Kee ex-MAS**) | Marketnode (SGX/Temasek).
## 3. Mechanics
[id G7] Governance spectrum with FSB concentration critique; Metcalfe framing with real adoption data; trust-anchor credentialing; three interop models; FMI-principles application to token networks.
## 4. Pattern
[id G7] Doctrine → downstream: layered-base option becomes GL1 [id P12]; trust anchors become GL1's KYC'd participation; Marketnode confirms [id P7] lineage; Toh's MAS→JPM move instantiates the revolving door the corpus's cast list implies.
## 5. Quantification
BCG/ADDX US$16tn tokenised by 2030 (industry sizing, promotional provenance — handle as marketing datum). Public-vs-private reach: millions vs hundreds/thousands (the paper's own admission).
## 6. Bull / Base / Bear
Bull: trust-anchor credentialing becomes the global standard; SG doctrine exports. Base: framework guides Guardian pilots; adoption gap persists ([id G4]'s subject). **Current.** Bear: credential concentration creates a de-platforming controversy that lands on the identity layer's missing appeal path.
## 7. Open Threads
Alan Lim's current portfolio/title — refresh before any approach. Trust-anchor liability framework — unwritten. Whether any Guardian credential scheme reached production.
## 8. Sources
[id G7] papers/G7, primary. Cross: [id P12][id P7][id G4], FSB DeFi report (2023), Menon 2022 speech.



================================================================================
# ══ [G3] — g3_interlinking
================================================================================


---
### ─── 1_intake.md ───

# INTAKE — G3 Guardian: Interlinking Networks Technical Paper (Nov 2023)
SUBJECT: Technical models for the third interop approach from [id G7] — connecting heterogeneous digital-asset networks bilaterally; common model for cross-network asset transfer.
SOURCE / RELIABILITY: **Primary**; MAS, v1.0 Nov 2023; explicitly no-policy/no-endorsement.
ENTITIES: MAS · case studies: cross-network ABS/trade receivables, discretionary portfolios w/ alternatives, cross-network fund distribution · cites McKinsey $4bn/yr cross-border DLT savings · Dunbar cited for common-network coordination cost.
KEY CLAIMS: Common universal platform requires heavy legal/regulatory coordination (per Dunbar), so bilateral interlinking is the pragmatic alternative; proposes a common transfer model across networks; walled-garden proliferation risk restated.
CONTRADICTIONS w/ KB: Tension, not contradiction — G3 (2023) advocates interlinking because common platforms are hard; GL1 (2024) pivots back to the layered common base. The programme runs both horses.
CLASSIFY: Tokenisation interop · tags: interlinking, bridges, cross-network transfer.
SIGNIFICANCE: The bridge layer is where wholesale interop actually happens near-term — and where risk concentrates (lock-&-mint custody, finality across chains, [id G6] later confronts this legally).
ROUTE: [id G3]



---
### ─── 2_knowledge-map.md ───

# KNOWLEDGE MAP — G3 Interlinking Networks
## Alphas
**A1 — Two-horse strategy, quietly.** G3 argues interlinking because common platforms need impossible coordination; GL1 then pursues the common platform anyway. MAS funds both the pragmatic path and the maximal one — optionality doctrine applied to infrastructure.
**A2 — Bridges are the new custody.** Every cross-network transfer model concentrates risk at the bridge (locked collateral, mint/burn integrity, cross-chain finality). The crypto industry's worst loss events live exactly here; the paper models mechanics, not failure economics.
**A3 — Dunbar's lesson absorbed sideways.** The sovereign-coordination wall [id P14] becomes the stated reason to interlink rather than unify — the corpus learning from itself in real time.
## Quadrants
KK: interlinking models, common transfer model, three case studies. KU: bridge liability, finality across heterogeneous chains (deferred to [id G6]). UK: Jasper–Ubin's HTLC as the ancestral bilateral bridge [id P8]; GL1's parallel bet. UU: *bridge-failure loss allocation* — no treatment of who eats a mint/burn mismatch; *N² economics* — interlinking recreates the correspondent-mesh cost structure [id P9] at the token layer, unpriced.
## Narrative Vector
The pragmatic middle chapter: connects [id G7]'s taxonomy to [id G6]'s legal reckoning. Read as evidence the programme knows the common platform may not arrive and is building the mesh it criticised.



---
### ─── 3_sa-report.md ───

# SA INWARD NOTE — Guardian Interlinking Networks (2023) [id G3]
## 1. Executive Summary
[id G3] G3 operationalises the interlinked-networks option: since universal platforms demand coordination Dunbar showed sovereigns won't give, connect heterogeneous networks bilaterally with a common transfer model. It is the pragmatic hedge against GL1's maximalism — both funded, both alive. The unpriced core: bridges concentrate custody and finality risk at exactly the point the wider industry has suffered its largest losses, and the paper's mechanics-first treatment leaves loss allocation to [id G6]'s later legal analysis.
## 2. Entity Map
MAS (sole author) | case-study contributors across ABS, portfolios, fund distribution | intellectual debts: Dunbar [id P14], Jasper–Ubin [id P8].
## 3. Mechanics
[id G3] Bilateral network linkage; common asset-transfer model; three illustrative cases; walled-garden critique restated from [id G7].
## 4. Pattern
[id G3] Corridor logic [id P8] re-emerges at the asset layer; two-horse strategy vs GL1 [id P12]; N² mesh economics echo the correspondent structure [id P9] the programme set out to escape.
## 5. Quantification
McKinsey $4bn/yr cross-border DLT savings (consultant provenance, treat as directional). No bridge-risk quantification — the missing number.
## 6. Bull / Base / Bear
Bull: standardised interlinking model adopted; mesh grows organically ahead of any common fabric. Base: pilots per case study; production interlinks stay rare pending legal finality clarity. **Current.** Bear: a bridge failure in regulated tokenised assets crystallises the unallocated-loss problem publicly.
## 7. Open Threads
Which G3 case studies went live. Bridge insurance/liability market formation — advisory whitespace. Convergence or divergence with GL1 as OpCo forms.
## 8. Sources
[id G3] papers/G3, primary. Cross: [id G6][id G7][id P8][id P12][id P14], McKinsey 2019.



================================================================================
# ══ [G1] — g1_fixed_income
================================================================================


---
### ─── 1_intake.md ───

# INTAKE — G1 Guardian Fixed Income Framework (2024)
SUBJECT: Industry framework for tokenised debt — full lifecycle (primary, secondary, maturity), operating models, data model (ICMA Bond Data Taxonomy), design principles, risks; case studies incl. SGX digital bonds, HSBC pilots, Project Trident; addenda on DvP settlement + custody lessons.
SOURCE / RELIABILITY: **Primary** industry framework under MAS convening (Guardian FI workstream).
ENTITIES: Guardian FI group · ICMA (taxonomy) · SGX (digital bond listing/DA register) · HSBC · Project Trident.
KEY CLAIMS: Honest adoption-gap diagnosis: weak business case (high start-up cost, efficient incumbents, **absence of cash on chain** blocking lifecycle automation), legal uncertainty across jurisdictions, infra immaturity, custody expectations (clients want licensed custodians — "contrary to what is sometimes claimed"); framework standardises lifecycle + data to lower these barriers.
CONTRADICTIONS w/ KB: None; the cash-on-chain gap is the demand signal for the Orchid/tokenised-money track — the two programmes need each other and G1 says so.
CLASSIFY: Tokenised fixed income · tags: ICMA BDT, digital bonds, custody, DvP.
SIGNIFICANCE: The frankest cost-benefit text in the Guardian set; its barrier list is the adoption-gap thesis [id G4] in bond-specific form.
ROUTE: [id G1]



---
### ─── 2_knowledge-map.md ───

# KNOWLEDGE MAP — G1 Fixed Income Framework
## Alphas
**A1 — "Absence of cash on chain" is the keystone admission.** Tokenised bonds can't self-execute coupons/redemptions without tokenised money on the same rails. Guardian's asset track openly depends on Orchid's money track — the corpus's two halves declare their coupling here.
**A2 — Custody realism deflates the disintermediation myth.** Clients want licensed custodians, full stop. The framework re-centres exactly the intermediaries tokenisation rhetoric promised to remove — incumbency absorbs again.
**A3 — Standards as the moat-leveller.** ICMA BDT adoption is the play to stop every issuer minting incompatible bond tokens — taxonomy first, market second; whoever's taxonomy wins, wins.
## Quadrants
KK: lifecycle mapping, deployment archetypes, ICMA data model, design principles, risk/mitigant tables, SGX/HSBC/Trident cases, DvP + custody addenda. KU: cross-jurisdiction legal treatment; secondary-liquidity formation. UK: SGX digital-bond lineage from [id P7]; MAS-regulated stablecoin/TBL supply as the pending cash leg [id P4]. UU: *incentive asymmetry* — the parties asked to fund migration (issuers/banks) earn the float and fees the migration destroys; the framework never prices the cannibalisation, which is the actual adoption gap; *coupon-automation liability* — who answers when a smart-contract coupon misfires is absent, custody addendum notwithstanding.
## Narrative Vector
Validates tokenised FI technically while cataloguing why it hasn't happened — and in doing so hands the Orchid track its demand case. The two programmes are one machine; G1 is where that's admitted in writing.



---
### ─── 3_sa-report.md ───

# SA INWARD NOTE — Guardian Fixed Income Framework (2024) [id G1]
## 1. Executive Summary
[id G1] The FI framework standardises tokenised debt end-to-end — lifecycle, operating models, ICMA-aligned data, custody and DvP practice — while delivering the Guardian set's frankest diagnosis of why adoption lags: no on-chain cash for lifecycle automation, weak switching incentives against efficient incumbents, legal fragmentation, and clients who want licensed custodians regardless of the technology. Its keystone sentence couples the corpus's halves: tokenised assets need tokenised money, making Orchid the demand-side answer to Guardian's supply-side build.
## 2. Entity Map
Guardian FI workstream (MAS-convened) | ICMA | SGX (digital bonds/DA register) | HSBC | Project Trident.
## 3. Mechanics
[id G1] Primary/secondary/maturity lifecycle on-chain; recording-medium archetypes; BDT data model; DvP settlement guide; custody lessons addendum.
## 4. Pattern
[id G1] Cash-leg dependency → [id P4] money forms; SGX lineage → [id P7]; barrier taxonomy → [id G4] generalisation; incumbency absorption pattern (custody) consistent corpus-wide.
## 5. Quantification
Cost/benefit asserted qualitatively; no published unit economics of tokenised vs conventional issuance — the number that would settle the business-case debate is absent across the industry.
## 6. Bull / Base / Bear
Bull: MAS-regulated tokenised cash arrives at scale; coupon/redemption automation flips the business case; digital issuance normalises. Base: episodic flagship issuances; standards consolidate; conventional rails dominate. **Current.** Bear: a lifecycle-automation failure (coupon misfire) with unallocated liability chills institutional issuance.
## 7. Open Threads
SCS-licensed stablecoin/TBL issuance volumes — the cash-leg tracker. Trident status. Tokenised-vs-conventional issuance cost study — unowned, publishable.
## 8. Sources
[id G1] papers/G1, primary. Cross: [id P4][id P7][id G4], ICMA BDT.



================================================================================
# ══ [G2] — g2_funds_framework
================================================================================


---
### ─── 1_intake.md ───

# INTAKE — G2 Guardian Funds Framework (2024)
SUBJECT: Non-prescriptive standards for tokenised funds — lifecycle (issuance→distribution→secondary→custody→servicing), operating archetypes, and the **Guardian Composable Token Taxonomy (GCTT)**; tokenised MMF case study.
SOURCE / RELIABILITY: **Primary**; Guardian Asset & Wealth Management (AWM) industry group under MAS.
ENTITIES: Guardian AWM group · fund admin/custody chain actors · GCTT [NEW construct].
KEY CLAIMS: Fund industry pain: cost, opacity, access; tokenisation enables modularised lifecycle and direct personalisation; three register archetypes (mirror / partial on-chain / full on-chain authoritative); GCTT as composable technical standard; explicit admission that tokenising existing fund structures has capped benefits — a "future state" beyond current structures is sketched.
CONTRADICTIONS w/ KB: None; the register-archetype ladder is the same authority-migration question as the FI recording-medium models [id G1].
CLASSIFY: Tokenised funds · tags: GFF, GCTT, MMF, register archetypes.
SIGNIFICANCE: The register question — when does the chain become the *authoritative* record — is the whole legal ballgame; G2 names the ladder, [id G6] climbs it.
ROUTE: [id G2]



---
### ─── 2_knowledge-map.md ───

# KNOWLEDGE MAP — G2 Funds Framework
## Alphas
**A1 — Authority migration is the real product.** Mirror → partial → full on-chain registers is a ladder of legal authority moving from administrator to ledger. Everything else (efficiency, personalisation) is decoration on the question of who holds the authoritative record — and thus the fees, the liability, and the veto.
**A2 — The capped-benefit admission.** G2 concedes tokenising today's fund structures yields limited gains; the promised land requires *new* structures. Translation: the framework standardises a transitional product while the endgame remains unlegislated.
**A3 — GCTT as taxonomy land-grab.** Like ICMA BDT in [id G1], whoever's composable token taxonomy becomes default owns the integration layer of a trillion-dollar industry's plumbing.
## Quadrants
KK: lifecycle mapping, three register archetypes, GCTT, MMF case. KU: future-state fund structures (sketched, not specified); cross-border register recognition. UK: transfer-agency/fund-admin incumbents whose franchise is the register — the displaced party is unnamed throughout; MMF-as-first-product logic (cash-like, tMMF momentum) imported from market reality. UU: *register bifurcation risk* — mirror/partial models create two records that can disagree; reconciliation failure in a "tokenised" fund would be a scandal precisely because the tech promised its impossibility; *the personalisation-privacy trade* — direct-to-investor personalisation via immutable ledgers builds a permanent behavioural record of retail investors; no privacy treatment exists in the paper.
## Narrative Vector
G2 standardises the transition and quietly admits the destination needs different law. The authority-migration ladder is the analytical spine to carry into [id G6], where legal reality bites.



---
### ─── 3_sa-report.md ───

# SA INWARD NOTE — Guardian Funds Framework (2024) [id G2]
## 1. Executive Summary
[id G2] The Funds Framework standardises tokenised funds around a lifecycle map, three register archetypes, and the Guardian Composable Token Taxonomy, with tokenised MMFs as the beachhead product. Its two honest cores: legal authority migrates rung by rung from administrator to ledger (mirror → partial → full), and tokenising existing structures delivers capped benefits — the real prize needs fund structures that don't yet exist in law. The displaced incumbent (the transfer-agency/admin franchise) is never named; the retail-privacy cost of ledgered personalisation is never priced.
## 2. Entity Map
Guardian AWM group (MAS-convened) | fund managers, admins, custodians (roles, largely unnamed) | GCTT as the standard artefact.
## 3. Mechanics
[id G2] Origination→issuance→distribution→secondary→custody→servicing on-chain variants; register archetypes 1–3; GCTT composition and flows; MMF use case.
## 4. Pattern
[id G2] Authority-ladder mirrors [id G1]'s recording-medium models; taxonomy strategy mirrors ICMA play; tMMF beachhead consistent with global market momentum; feeds [id G6]'s legal deep-dive directly.
## 5. Quantification
None; the industry's own sizing (US$16tn by 2030 [id G7]) stands in for fund-specific economics. tMMF AUM growth is the trackable proxy — refresh externally.
## 6. Bull / Base / Bear
Bull: full on-chain authoritative registers recognised in lead jurisdictions; admin layer re-prices; GCTT becomes lingua franca. Base: mirror/partial deployments proliferate; authority stays off-chain; benefits stay capped as admitted. **Current.** Bear: a register-reconciliation failure in a dual-record fund triggers regulatory retrenchment.
## 7. Open Threads
Jurisdictions recognising on-chain authoritative fund registers — legal tracker. GCTT adoption beyond Guardian. The unnamed displaced party's countermove (admin industry response).
## 8. Sources
[id G2] papers/G2, primary. Cross: [id G1][id G6][id G7].



================================================================================
# ══ [G4] — g4_adoption_gap
================================================================================


---
### ─── 1_intake.md ───

# INTAKE — G4 Guardian: Bridging the Adoption Gap (2024/25)
SUBJECT: SG–UK regulator-industry collaboration (MAS+IMAS × FCA+IA) on why buy-side adoption of tokenised assets lags and what closes the gap.
SOURCE / RELIABILITY: **Primary**; foreworded by **Kenneth Gay, Chief FinTech Officer, MAS** [KB: the second official copied in the user's voucher exchange], Carmen Wee (IMAS), Chris Cummings (IA).
ENTITIES: **Kenneth Gay (MAS CFO — mandate-relevant)** · MAS · IMAS · FCA · IA · UK IF3 Lab referenced.
KEY CLAIMS: Adoption gap = tokenisation initiatives prioritise tech/efficiency while buy-side must satisfy operational, regulatory, fiduciary requirements first; investors must be "at the heart"; tech must make things cheaper/quicker/broader "not technology for technology's sake"; SG–UK coordination as confidence-builder for cross-border scale.
CONTRADICTIONS w/ KB: None; generalises [id G1]'s barrier list to the whole buy-side and gives it a bilateral-regulator imprimatur.
CLASSIFY: Tokenisation adoption · tags: buy-side, MAS-FCA, IMAS, IA, Kenneth Gay.
SIGNIFICANCE: **Mandate-critical**: Gay's authored frame — investor-centric, trust-and-confidence, "enhance not disrupt" — is the second target's published doctrine, paired with Lim's in [id G7].
ROUTE: [id G4]



---
### ─── 2_knowledge-map.md ───

# KNOWLEDGE MAP — G4 Bridging the Adoption Gap
## Alphas
**A1 — Kenneth Gay's fingerprint.** The CFO's foreword commits him publicly to: investors at the heart, trust/confidence/resilience as preconditions, tech justified only by concrete user benefit, international coordination as the scaling mechanism. A sentiment-research pitch is almost a restatement of his own paragraph — the mandate can be framed as *operationalising* Gay's stated doctrine.
**A2 — The gap is institutional, and the citizen version is unwritten.** G4 maps why *institutions* don't adopt (fiduciary/ops/reg requirements unmet). No equivalent document maps why *citizens* would or wouldn't trust programmable money — the corpus's final, still-open seat, and precisely the SAA proposition.
**A3 — Bilateralism as moat and megaphone.** SG–UK regulator pairing manufactures cross-border legitimacy; frameworks agreed by two hub regulators become de facto standards for everyone smaller.
## Quadrants
KK: adoption-gap thesis, buy-side requirement stack, SG–UK institutional pairing, IF3 Lab reference. KU: which specific reforms close the gap (directional, not specified). UK: [id G1]'s bond-level barriers as the concrete substrate; IMAS/IA as buy-side cartels lending legitimacy. UU: *the retail silence* (above) — "investors at the heart" means institutional investors throughout; the individual whose pension is the ultimate buy-side is absent from a paper titled around investors; *doctrine-vs-architecture tension* — Gay's "enhance not disrupt" foreword sits atop an architecture (Blueprint/GL1 gating) that is quietly re-drawing market structure; the gap between the CFO's language and the concession map is itself analysable.
## Narrative Vector
G4 completes the target-psychographics pair: Lim's doctrine [id G7] + Gay's doctrine here. The mandate walks through the door both men built — citizen-sentiment research as the missing volume in their own series.



---
### ─── 3_sa-report.md ───

# SA INWARD NOTE — Guardian: Bridging the Adoption Gap (2024/25) [id G4]
## 1. Executive Summary
[id G4] The SG–UK collaboration (MAS+IMAS, FCA+IA) diagnoses tokenisation's buy-side adoption gap: initiatives optimise technology while institutions must first satisfy fiduciary, operational and regulatory requirements. Kenneth Gay's foreword sets the doctrine — investors at the heart, trust and confidence as preconditions, technology justified only by tangible benefit. The report's structural silence is the retail citizen: "investor-centric" means institutional throughout, leaving citizen trust in programmable money as the unwritten companion volume — the precise whitespace of the SAA mandate, now attributable to the target's own framing.
## 2. Entity Map
**Kenneth Gay (MAS CFO)** | Carmen Wee (IMAS) | Chris Cummings (IA) | FCA (UK) | IF3 Lab context.
## 3. Mechanics
[id G4] Gap = requirement-stack mismatch; remedy = align design with buy-side needs + bilateral regulatory coordination; UK-SG framework alignment as confidence infrastructure.
## 4. Pattern
[id G4] Generalises [id G1] barriers; pairs with [id G7] to complete the two-target doctrine set; bilateral-standard-setting pattern (two hubs → de facto global norms) mirrors MAS's corridor diplomacy [id P11].
## 5. Quantification
None; gap asserted qualitatively — consistent with a foreword-led policy document.
## 6. Bull / Base / Bear
Bull: SG–UK alignment unlocks cross-border tokenised fund flows; gap narrows measurably. Base: continued framework production; adoption inches via tMMFs. **Current.** Bear: doctrine-architecture gap (open language vs gated structure) surfaces publicly and costs the programme trust — the exact risk sentiment research pre-empts.
## 7. Open Threads
Gay's current initiatives/speeches — refresh pre-approach. FCA-side reciprocal documents. Whether any retail/citizen-facing trust study exists anywhere in the MAS corpus (none found to date — confirm the negative).
## 8. Sources
[id G4] papers/G4, primary. Cross: [id G1][id G7][id P11].



================================================================================
# ══ [G5] — g5_fx_workstream
================================================================================


---
### ─── 1_intake.md ───

# INTAKE — G5 Guardian FX Workstream / Transaction Banking (2024/25)
SUBJECT: Shared ledgers + tokenised bank liabilities applied to transaction banking and FX — lifecycle redesign of cross-border corporate payments; use cases from Ant International, BNY+OCBC, HSBC; standardised documentation agenda.
SOURCE / RELIABILITY: **Primary**; Guardian FX workstream.
ENTITIES: **Ant International** [NEW — first big-tech/platform treasury in the corpus] · BNY · OCBC · HSBC · FSB/CPMI RTGS-hours initiatives referenced.
KEY CLAIMS: FX pain: market hours, legacy RTGS downtime, opaque end-to-end costs; tokenised bank liabilities as 24/7 settlement money for corporates; TBL distinguished from stablecoins/CBDCs (bank-balance-sheet claim); operating-model changes and risk/mitigant catalogue; push for standardised tokenised-FX documentation atop existing industry standards.
CONTRADICTIONS w/ KB: None; this is [id P4]'s TBL category finding its commercial lane, and [id P11]'s vehicle-currency logic reappearing at corporate-treasury level.
CLASSIFY: Tokenised FX / transaction banking · tags: TBL, 24/7 FX, Ant, documentation standards.
SIGNIFICANCE: The commercialisation edge of the wholesale track — where research becomes bank product; Ant's presence marks platform treasuries entering the regulated tokenised-money tent.
ROUTE: [id G5]



---
### ─── 2_knowledge-map.md ───

# KNOWLEDGE MAP — G5 FX Workstream
## Alphas
**A1 — TBLs win the money race by default.** Of the Blueprint's three permitted monies [id P4], tokenised bank liabilities are the one shipping in corporate use cases — CBDC deferred, stablecoins licensing slowly. The two-tier system's digital heir is the bank deposit, exactly as the 2021 monograph's protective doctrine [id P3] would predict.
**A2 — Ant inside the tent.** A platform giant's treasury operating on bank-issued tokenised money under MAS convening is the co-option play in miniature: big tech joins the rails as *client*, not issuer — the walled-garden threat [id P3] neutralised by membership.
**A3 — Documentation is destiny.** The standardised tokenised-FX documentation push is ISDA-style infrastructure: whoever writes the master terms writes the market.
## Quadrants
KK: FX/transaction-banking lifecycle on shared ledgers, TBL definition vs alternatives, three use cases, ops/risk catalogues, documentation agenda. KU: legal enforceability of tokenised-FX docs across jurisdictions; intraday liquidity effects of 24/7. UK: FSB/CPMI RTGS-hours workstreams as the incumbent-rail response; Partior as the unnamed adjacent production rail. UU: *24/7 risk transformation* — continuous settlement abolishes the overnight batch that current risk/ops models assume; the paper lists risks but not the institutional redesign continuous FX implies; *platform-treasury power* — Ant-scale treasuries on tokenised rails could internalise FX flow at volumes that rival mid-tier banks; the co-option may breed the next disintermediation.
## Narrative Vector
G5 is where the wholesale corpus touches commercial ground: TBLs as the winning money, platforms as clients, documentation as the next battlefield. The research phase is ending; the market-structure phase has begun.



---
### ─── 3_sa-report.md ───

# SA INWARD NOTE — Guardian FX Workstream (2024/25) [id G5]
## 1. Executive Summary
[id G5] The FX workstream lands the wholesale programme in commercial territory: tokenised bank liabilities on shared ledgers as 24/7 settlement money for corporate transaction banking, with live-shaped use cases from Ant International, BNY+OCBC and HSBC, and a push to standardise tokenised-FX documentation. TBLs emerge as the de facto winner among the Blueprint's permitted monies — the bank deposit digitising itself, precisely as the 2021 doctrine's deposit-protection logic implied. Ant's presence signals platform treasuries entering as clients of bank money; whether that co-option holds at volume is the live question.
## 2. Entity Map
Ant International | BNY, OCBC, HSBC | Guardian FX group (MAS-convened) | FSB/CPMI (incumbent-rail context) | Partior (unnamed adjacency).
## 3. Mechanics
[id G5] Cross-border corporate payment lifecycle re-mapped on shared ledger; TBL as balance-sheet claim distinct from stablecoin/CBDC; operating-model shifts; risk/mitigant tables; documentation standardisation atop existing FX standards.
## 4. Pattern
[id G5] [id P4] money-whitelist → TBL commercial primacy; [id P3] deposit-protection doctrine vindicated in market outcome; [id P11] vehicle-currency logic at treasury level; co-option-of-challengers pattern (Ant) consistent with corpus-wide incumbent absorption.
## 5. Quantification
End-to-end FX cost opacity named as pain but not measured; 24/7 liquidity impacts unquantified. Ant-scale internalisable FX flow — the number that would reveal the co-option's fragility — absent.
## 6. Bull / Base / Bear
Bull: TBL-based 24/7 FX scales across Guardian banks; documentation standard lands; corporates re-treasury around continuous settlement. Base: bilateral pilots grow; documentation drafting extends; RTGS-hours reforms blunt urgency. **Current.** Bear: platform treasuries leverage the rails to internalise flow, re-opening the disintermediation fight inside the tent.
## 7. Open Threads
Tokenised-FX master documentation drafting venue and drafters — the ISDA-analogue watch. Ant's SG licensing perimeter. TBL issuance volumes by bank — the adoption tracker.
## 8. Sources
[id G5] papers/G5, primary. Cross: [id P3][id P4][id P11], FSB/CPMI publications cited in-doc.



================================================================================
# ══ [G6] — g6_operationalising
================================================================================


---
### ─── 1_intake.md ───

# INTAKE — G6 Guardian: Operationalising Tokenised Funds (2024/25)
SUBJECT: The production playbook for tokenised funds — legal structures (Digital Mirror/Twin/Native mapped to GFF archetypes), cross-chain **settlement finality** law, live use cases (Franklin Templeton, Phillip Securities+stablecoin settlement, Fidelity+Citi digital FX, **Swift** TradFi bridge, Deutsche Bank DAMA 2), scalability enablers.
SOURCE / RELIABILITY: **Primary**; Guardian AWM, pilots-to-production stage; tMMFs as global lead product.
ENTITIES: Franklin Templeton · Phillip Securities · Fidelity · Citi · **Swift** (bridging role) · Deutsche Bank (DAMA 2 MVP) · UK cross-border annex.
KEY CLAIMS: tMMFs moving pilots→production; legal structure precedes tech benefits; bridged-token models (Lock-&-Mint vs Burn-&-Mint) analysed for **when risk passes and finality attaches** — critical for risk, tax, insolvency; DvP smart-contract model trade-offs; open-architecture custody/wallets; enabler stack (KYC, network effects, ops controls, standards, UX).
CONTRADICTIONS w/ KB: None; G6 answers the finality/bridge-liability gaps [id G3] left open, and climbs [id G2]'s authority ladder with named products.
CLASSIFY: Tokenised funds production · tags: tMMF, finality, bridges, Swift, DAMA 2.
SIGNIFICANCE: The corpus's most production-real document — global asset managers, Swift in the loop, insolvency-grade finality analysis. Tokenisation stops being a prototype here.
ROUTE: [id G6]



---
### ─── 2_knowledge-map.md ───

# KNOWLEDGE MAP — G6 Operationalising Tokenised Funds
## Alphas
**A1 — Finality is the whole ballgame, finally said.** The moment a cross-chain transfer becomes irrevocable — for risk, tax, insolvency — is named as the critical unknown. Everything the corpus built rests on this legal instant, and G6 is the first document to put insolvency analysis around bridged tokens. The lawyers have arrived; that's the maturity signal.
**A2 — Swift inside the tokenised tent.** The incumbent messaging monopoly appears as the TradFi bridge use case — the same accommodation pattern as [id P10]'s SWIFT diplomacy and Mandala's ISO 20022 pathway [id P13]. Every revolution in this corpus ends with the incumbent holding a workstream.
**A3 — Named product, named managers.** Franklin Templeton, Fidelity, Citi, DB running use cases converts Guardian from framework factory to distribution channel: MAS convening now moves real AUM logos, which is precisely the credibility the adoption-gap paper [id G4] said was missing.
## Quadrants
KK: four tokenisation models with legal analysis, bridge finality treatment, five use cases, DvP model trade-offs, custody architectures, enabler stack. KU: per-jurisdiction finality recognition; tax treatment of bridge events. UK: [id G2] ladder + [id G3] bridges converging here; tMMF global momentum (BUIDL-era context) as the external tide. UU: *insolvency of the bridge operator* — analysed for token models but the bridge *entity's* failure (who is administrator over locked collateral) remains thinner than the token analysis; *stablecoin settlement leg* (Phillip case) quietly normalises private stablecoins in regulated fund settlement ahead of SCS licensing volume — practice outrunning the whitelist [id P4].
## Narrative Vector
G6 is the corpus's arrival document: legal reality, incumbent accommodation, production logos. The remaining frontier it names — finality across chains and jurisdictions — is where the next five years of value and litigation live.



---
### ─── 3_sa-report.md ───

# SA INWARD NOTE — Guardian: Operationalising Tokenised Funds (2024/25) [id G6]
## 1. Executive Summary
[id G6] The operational playbook marks tokenised funds' pilots-to-production turn, led globally by tokenised MMFs. It grounds every technical benefit in legal structure first, delivers the corpus's only insolvency-grade analysis of cross-chain settlement finality and bridged-token risk passage (Lock-&-Mint vs Burn-&-Mint), and carries five named use cases — Franklin Templeton, Phillip Securities with stablecoin settlement, Fidelity+Citi digital FX, Swift's TradFi bridge, Deutsche Bank's DAMA 2. The pattern completes: incumbents (Swift) accommodated, global managers enlisted, and the decisive open question named in law's language — the moment finality attaches.
## 2. Entity Map
Franklin Templeton | Phillip Securities | Fidelity + Citi | Swift | Deutsche Bank (DAMA 2) | Guardian AWM (MAS-convened) | UK annex (FCA-side continuity with [id G4]).
## 3. Mechanics
[id G6] Digital Mirror/Twin/Native models mapped to register archetypes; bridge mechanics with risk-passage and finality analysis; PvP stablecoin settlement; PvDvP FX swaps cross-network; post-trade lifecycle orchestration; enabler stack for scale.
## 4. Pattern
[id G6] Converges [id G2]+[id G3]; Swift accommodation echoes [id P10][id P13]; stablecoin-leg practice runs ahead of the [id P4] whitelist — regulatory catch-up risk; named-logo strategy answers [id G4]'s trust deficit.
## 5. Quantification
tMMF production status asserted; AUM figures not printed (external trackers required). Finality-failure loss scenarios unquantified — consistent with a frontier the law hasn't priced.
## 6. Bull / Base / Bear
Bull: finality recognised statutorily in lead jurisdictions; tMMFs become cash-management default; Guardian branding graduates to market standard. Base: production grows inside guarded perimeters; finality clarified piecemeal via contract. **Current.** Bear: a cross-chain insolvency event tests bridged-collateral title before statute catches up — the litigation that would define the field.
## 7. Open Threads
Jurisdictional finality-recognition tracker (UK annex suggests where next). DAMA 2 production status. Stablecoin-settlement perimeter vs SCS licensing reality — regulatory-gap watch.
## 8. Sources
[id G6] papers/G6, primary. Cross: [id G2][id G3][id G4][id P4][id P10][id P13].

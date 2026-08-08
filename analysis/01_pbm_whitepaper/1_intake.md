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

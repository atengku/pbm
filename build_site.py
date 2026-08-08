#!/usr/bin/env python3
import html

FEATURED = {
    "file":"papers/01_PBM_Technical_Whitepaper_2023.pdf",
    "title":"Purpose Bound Money (PBM) — Technical Whitepaper",
    "date":"June 2023",
    "authors":"MAS, with IMF, Amazon, DBS, JPMorgan Onyx, Bank of Korea & others",
    "summary":"The founding technical specification of Purpose Bound Money. Defines the two-part model — a smart-contract <em>wrapper</em> that encodes usage conditions (validity/expiry period, merchant whitelists, denominations) around an underlying <em>store-of-value</em> token (CBDC, tokenised deposits, or regulated stablecoins). Establishes PBM as a bearer instrument with self-contained logic, transferable without intermediaries, and later formalised as Ethereum standard ERC-7291. This is the reference document for how programmable conditions — including the expiry behaviour built into government vouchers — are specified and enforced."
}

SECTIONS = [
 ("Retail Digital SGD — Project Orchid",
  "MAS's exploration of a programmable digital Singapore dollar and the infrastructure to support it.",
  [
   ("papers/02_Project_Orchid_Phase1_Report_2022.pdf","Project Orchid — Phase 1 Report","Oct 2022",
    "Marks completion of Phase 1. Introduces the PBM concept to the public, sets out design considerations for a programmable digital SGD, and presents live use cases contributed by industry and government — government vouchers, SkillsFuture credits, and conditional disbursements."),
   ("papers/04_Project_Orchid_Blueprint_2023.pdf","Project Orchid — Blueprint","Nov 2023",
    "The infrastructure blueprint for a digital SGD ecosystem: the roles of settlement ledgers, tokenised bank liabilities, PBM as the common interface layer, programmability, name-service and interoperability components needed before any retail issuance decision."),
   ("papers/03_Retail_CBDC_Economic_Considerations_2021.pdf","A Retail CBDC — Economic Considerations in the Singapore Context","Nov 2021","MAS's economic assessment of a retail central bank digital currency. Concludes the case for a retail CBDC in Singapore is not compelling for now given pervasive electronic payments, while committing to build the readiness to issue one should conditions change."),
  ]),
 ("Wholesale CBDC — Project Ubin",
  "MAS's multi-year, multi-phase programme on interbank settlement and cross-border payments using distributed ledgers.",
  [
   ("papers/05_Project_Ubin_Phase1_SGD_on_DLT_2017.pdf","Ubin Phase 1 — SGD on a Distributed Ledger","2017","Proof-of-concept placing a tokenised SGD on a distributed ledger for interbank settlement, with banks pledging cash against digital tokens redeemable at MAS."),
   ("papers/06_Project_Ubin_Phase2_Reimagining_RTGS_2017.pdf","Ubin Phase 2 — Reimagining RTGS","2017","Decentralised interbank payment and netting with a liquidity-saving mechanism, prototyped across three platforms (Corda, Quorum, Hyperledger Fabric)."),
   ("papers/07_Project_Ubin_Phase3_DvP_on_DLT_2018.pdf","Ubin Phase 3 — Delivery-versus-Payment on DLT","2018","Delivery-versus-payment settlement of tokenised assets across different blockchains, demonstrating simultaneous exchange of securities and cash (with SGX)."),
   ("papers/08_Jasper_Ubin_CrossBorder_Design_Paper_2019.pdf","Jasper–Ubin — Cross-Border Design Paper","2019","Joint work with the Bank of Canada on cross-border, cross-currency payments across two different DLT networks using hashed time-locked contracts."),
   ("papers/09_Ubin_CrossBorder_Interbank_Payments_Settlements_2019.pdf","Ubin — Cross-Border Interbank Payments & Settlements","2019","A blockchain-based multi-currency payments network prototype for cross-border interbank settlement, developed with industry partners."),
   ("papers/10_Project_Ubin_Phase5_Ecosystem_2020.pdf","Ubin Phase 5 — Enabling Broad Ecosystem Opportunities","2020","The capstone report: a multi-currency payments network prototype with commercial applications and interfaces, produced with Temasek, JPMorgan and Accenture."),
   ("papers/11_Project_Cedar_x_Ubin_CrossBorder_2022.pdf","Project Cedar Phase II × Ubin — Cross-Border","Nov 2022","Joint experiment with the Federal Reserve Bank of New York on wholesale cross-border, multi-currency settlement using a vehicle currency and distributed-ledger interoperability."),
   ("papers/14_Project_Dunbar_Multi_CBDC_2022.pdf","Project Dunbar — International Settlements Using Multi-CBDCs","Mar 2022","BIS Innovation Hub Singapore Centre with MAS, RBA, BNM and SARB: a shared multi-CBDC platform prototype enabling direct cross-border settlement between commercial banks in different central bank digital currencies."),
   ("papers/13_Project_Mandala_Compliance_2024.pdf","Project Mandala — Streamlining Cross-Border Transaction Compliance","Oct 2024","BIS Innovation Hub Singapore Centre with MAS, RBA, BOK and BNM: a compliance-by-design architecture (peer-to-peer messaging, rules engine, proof engine) that embeds sanctions screening and capital-flow rules into cross-border payments, generating a compliance proof before funds move."),
  ]),
 ("Shared Infrastructure & Tokenisation — GL1 / Project Guardian  (adjacent, not CBDC)",
  "Included for completeness. GL1 and Guardian are MAS's shared-ledger and asset-tokenisation tracks — related digital-money infrastructure, but distinct from the CBDC / digital-SGD lineage above.",
  [
   ("papers/12_GL1_Global_Layer_One_Whitepaper_2024.pdf","Global Layer One (GL1) — Whitepaper","Jun 2024","MAS with international policymakers and financial institutions: design principles, governance and architecture for a multi-purpose shared-ledger infrastructure on which regulated institutions deploy interoperable tokenised-asset applications across jurisdictions."),
   ("papers/G1_Guardian_Fixed_Income_Framework_2024.pdf","Guardian Fixed Income Framework","2024","Industry framework for applying tokenisation to fixed-income instruments and issuance."),
   ("papers/G2_Guardian_Funds_Framework_2024.pdf","Guardian Funds Framework","2024","Framework for tokenised investment funds — structuring, distribution and lifecycle."),
   ("papers/G3_Guardian_Interlinking_Networks_2023.pdf","Guardian — Interlinking Networks Technical Paper","2023","Technical models for connecting digital-asset networks to enable interoperable tokenised transactions."),
   ("papers/G4_Guardian_Bridging_Adoption_Gap_2024.pdf","Guardian — Bridging the Adoption Gap","2024","An enabling framework to move tokenisation from pilots toward commercial scale across asset classes."),
   ("papers/G5_Guardian_FX_Workstream_2024.pdf","Guardian — FX Workstream / Transaction Banking","2024","Findings from the FX and transaction-banking workstream on tokenised foreign-exchange settlement."),
   ("papers/G6_Guardian_Operationalising_Tokenised_Funds_2024.pdf","Guardian — Operationalising Tokenised Funds","2024","Operational playbook for taking tokenised funds into production — controls, roles and settlement."),
   ("papers/G7_Guardian_Open_Interoperable_Network_2023.pdf","Guardian — Open & Interoperable Network","2023","Design principles for open, interoperable networks underpinning tokenised asset markets."),
  ]),
]

def card(file,title,date,summary,featured=False):
    return f'''
      <article class="card{' feat' if featured else ''}">
        <div class="card-top">
          <span class="date">{html.escape(date)}</span>
        </div>
        <h3>{html.escape(title)}</h3>
        <p class="summary">{summary}</p>
        <a class="open" href="{file}" target="_blank" rel="noopener">Open PDF <span>&#8599;</span></a>
      </article>'''

sections_html=""
for name,blurb,papers in SECTIONS:
    cards="".join(card(f,t,d,s) for (f,t,d,s) in papers)
    sections_html+=f'''
    <section class="band">
      <div class="band-head">
        <h2>{html.escape(name)}</h2>
        <p>{html.escape(blurb)}</p>
      </div>
      <div class="grid">{cards}</div>
    </section>'''

page=f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>PBM &amp; CBDC Research Library — MAS Source Documents</title>
<meta name="description" content="Curated library of Monetary Authority of Singapore source papers on Purpose Bound Money, Project Orchid, Project Ubin and related digital-money initiatives.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
:root{{
  --void:#0a0c10; --panel:#12161d; --panel2:#151b24; --line:#232c38;
  --ink:#e8edf4; --mut:#8c98a8; --gold:#c9a24b; --gold2:#e5c877;
}}
*{{box-sizing:border-box}}
html{{scroll-behavior:smooth}}
body{{margin:0;background:var(--void);color:var(--ink);
  font-family:Inter,system-ui,sans-serif;line-height:1.6;
  -webkit-font-smoothing:antialiased}}
.mono{{font-family:'IBM Plex Mono',monospace}}
.wrap{{max-width:1120px;margin:0 auto;padding:0 24px}}
header.top{{border-bottom:1px solid var(--line);position:sticky;top:0;z-index:10;
  background:rgba(10,12,16,.82);backdrop-filter:blur(10px)}}
.top .wrap{{display:flex;align-items:center;justify-content:space-between;height:60px}}
.brand{{font-family:'IBM Plex Mono',monospace;font-weight:600;letter-spacing:.02em;font-size:15px}}
.brand b{{color:var(--gold)}}
.top .tag{{font-family:'IBM Plex Mono',monospace;font-size:11px;color:var(--mut);text-transform:uppercase;letter-spacing:.14em}}
.hero{{padding:64px 0 20px;border-bottom:1px solid var(--line)}}
.eyebrow{{font-family:'IBM Plex Mono',monospace;font-size:12px;letter-spacing:.24em;
  text-transform:uppercase;color:var(--gold);margin:0 0 18px}}
.hero h1{{font-size:clamp(30px,4.4vw,50px);line-height:1.08;margin:0 0 16px;font-weight:700;letter-spacing:-.01em}}
.hero p.lede{{font-size:18px;color:var(--mut);max-width:720px;margin:0}}
.stat{{display:flex;gap:34px;margin-top:30px;flex-wrap:wrap}}
.stat div{{font-family:'IBM Plex Mono',monospace}}
.stat .n{{font-size:24px;color:var(--gold2);font-weight:600}}
.stat .l{{font-size:11px;color:var(--mut);text-transform:uppercase;letter-spacing:.12em}}

/* Original white paper */
.original{{padding:52px 0}}
.orig-label{{display:inline-flex;align-items:center;gap:10px;font-family:'IBM Plex Mono',monospace;
  font-size:12px;letter-spacing:.2em;text-transform:uppercase;color:var(--gold);margin:0 0 20px}}
.orig-label::before{{content:"";width:34px;height:1px;background:var(--gold)}}
.orig{{background:linear-gradient(160deg,#161c25,#10141a);border:1px solid var(--gold);
  border-radius:14px;padding:38px;position:relative;overflow:hidden}}
.orig::after{{content:"WHITE PAPER";position:absolute;right:-14px;top:26px;transform:rotate(90deg);
  font-family:'IBM Plex Mono',monospace;font-size:11px;letter-spacing:.4em;color:rgba(201,162,75,.35)}}
.orig h2{{font-size:26px;margin:0 0 6px;letter-spacing:-.01em}}
.orig .meta{{font-family:'IBM Plex Mono',monospace;font-size:12.5px;color:var(--gold2);margin:0 0 4px}}
.orig .auth{{font-size:13px;color:var(--mut);margin:0 0 18px}}
.orig p.sum{{font-size:15.5px;color:#cdd6e2;max-width:760px;margin:0 0 26px}}
.orig p.sum em{{color:var(--gold2);font-style:normal}}
.btn{{display:inline-flex;align-items:center;gap:9px;background:var(--gold);color:#151007;
  font-weight:600;font-size:14px;padding:12px 22px;border-radius:8px;text-decoration:none;
  font-family:'IBM Plex Mono',monospace;transition:.15s}}
.btn:hover{{background:var(--gold2)}}

/* bands */
.band{{padding:40px 0;border-top:1px solid var(--line)}}
.band-head h2{{font-size:22px;margin:0 0 6px;letter-spacing:-.01em}}
.band-head p{{color:var(--mut);font-size:14px;margin:0 0 26px;max-width:760px}}
.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(320px,1fr));gap:16px}}
.card{{background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:22px;
  display:flex;flex-direction:column;transition:.16s}}
.card:hover{{border-color:#3a4757;transform:translateY(-2px);background:var(--panel2)}}
.card-top{{margin-bottom:12px}}
.date{{font-family:'IBM Plex Mono',monospace;font-size:11px;letter-spacing:.1em;
  color:var(--gold);border:1px solid rgba(201,162,75,.35);border-radius:20px;padding:3px 11px}}
.card h3{{font-size:16.5px;margin:0 0 10px;line-height:1.3}}
.card .summary{{font-size:13.5px;color:var(--mut);margin:0 0 20px;flex:1}}
.open{{font-family:'IBM Plex Mono',monospace;font-size:13px;color:var(--gold2);
  text-decoration:none;font-weight:500;align-self:flex-start}}
.open:hover{{color:#fff}}
.open span{{transition:.15s;display:inline-block}}
.open:hover span{{transform:translate(2px,-2px)}}

footer{{border-top:1px solid var(--line);padding:34px 0 60px;margin-top:20px}}
footer p{{font-family:'IBM Plex Mono',monospace;font-size:12px;color:var(--mut);margin:4px 0}}
footer a{{color:var(--gold)}}
@media(max-width:560px){{.orig{{padding:26px}} .hero{{padding:44px 0 16px}}}}
</style>
</head>
<body>
<header class="top"><div class="wrap">
  <div class="brand">PBM<b>/</b>CBDC <span style="color:var(--mut);font-weight:400">Library</span></div>
  <div class="tag">MAS Source Documents</div>
</div></header>

<div class="hero"><div class="wrap">
  <p class="eyebrow">Monetary Authority of Singapore &middot; Digital Money Research</p>
  <h1>Purpose Bound Money &amp; the Singapore CBDC record.</h1>
  <p class="lede">Every primary MAS paper behind programmable money in Singapore — from the founding PBM specification through Project Orchid, the full Project Ubin wholesale-CBDC series, and the adjacent tokenisation track — in one place, each opening directly.</p>
  <div class="stat">
    <div><div class="n">21</div><div class="l">Papers</div></div>
    <div><div class="n">2016&ndash;2024</div><div class="l">Span</div></div>
    <div><div class="n">3</div><div class="l">Programmes</div></div>
    <div><div class="n">MAS</div><div class="l">Source</div></div>
  </div>
</div></div>

<div class="original"><div class="wrap">
  <p class="orig-label">Original White Paper</p>
  <div class="orig">
    <h2>{html.escape(FEATURED["title"])}</h2>
    <p class="meta">{html.escape(FEATURED["date"])}</p>
    <p class="auth">{html.escape(FEATURED["authors"])}</p>
    <p class="sum">{FEATURED["summary"]}</p>
    <a class="btn" href="{FEATURED["file"]}" target="_blank" rel="noopener">Open the White Paper &#8599;</a>
  </div>
</div></div>

<div class="wrap">{sections_html}</div>

<footer><div class="wrap">
  <p>Source: Monetary Authority of Singapore (mas.gov.sg). All documents &copy; MAS; hosted here for reference and study.</p>
  <p>Library staged 8 August 2026 &middot; 21 documents &middot; <a href="papers/01_PBM_Technical_Whitepaper_2023.pdf" target="_blank">start with the PBM whitepaper &#8599;</a></p>
</div></footer>
</body></html>'''

open("index.html","w").write(page)
print("index.html written:", len(page), "bytes")

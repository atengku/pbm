#!/usr/bin/env python3
import markdown, re, os, html

DOCS = {  # ref -> (folder, pdf, title, short)
 "P1":("01_pbm_whitepaper","papers/01_PBM_Technical_Whitepaper_2023.pdf","PBM Technical Whitepaper (2023)","PBM Whitepaper"),
 "P2":("02_orchid_phase1","papers/02_Project_Orchid_Phase1_Report_2022.pdf","Project Orchid Phase 1 (2022)","Orchid P1"),
 "P3":("03_retail_cbdc_econ","papers/03_Retail_CBDC_Economic_Considerations_2021.pdf","Retail CBDC: Economic Considerations (2021)","CBDC Economics"),
 "P4":("04_orchid_blueprint","papers/04_Project_Orchid_Blueprint_2023.pdf","Orchid Blueprint (2023)","Blueprint"),
 "P5":("05_ubin_p1","papers/05_Project_Ubin_Phase1_SGD_on_DLT_2017.pdf","Ubin Phase 1 (2017)","Ubin P1"),
 "P6":("06_ubin_p2","papers/06_Project_Ubin_Phase2_Reimagining_RTGS_2017.pdf","Ubin Phase 2: Re-imagining RTGS (2017)","Ubin P2"),
 "P7":("07_ubin_p3","papers/07_Project_Ubin_Phase3_DvP_on_DLT_2018.pdf","Ubin Phase 3: DvP on DLT (2018)","Ubin P3"),
 "P8":("08_jasper_ubin","papers/08_Jasper_Ubin_CrossBorder_Design_Paper_2019.pdf","Jasper–Ubin Design Paper (2019)","Jasper–Ubin"),
 "P9":("09_crossborder","papers/09_Ubin_CrossBorder_Interbank_Payments_Settlements_2019.pdf","Cross-Border Interbank Payments (2019)","Cross-Border Report"),
 "P10":("10_ubin_p5","papers/10_Project_Ubin_Phase5_Ecosystem_2020.pdf","Ubin Phase 5 (2020)","Ubin P5"),
 "P11":("11_cedar_ubin","papers/11_Project_Cedar_x_Ubin_CrossBorder_2022.pdf","Cedar II × Ubin+ (2022)","Cedar×Ubin"),
 "P12":("12_gl1","papers/12_GL1_Global_Layer_One_Whitepaper_2024.pdf","Global Layer One Whitepaper (2024)","GL1"),
 "P13":("13_mandala","papers/13_Project_Mandala_Compliance_2024.pdf","Project Mandala (2024)","Mandala"),
 "P14":("14_dunbar","papers/14_Project_Dunbar_Multi_CBDC_2022.pdf","Project Dunbar (2022)","Dunbar"),
 "G1":("g1_fixed_income","papers/G1_Guardian_Fixed_Income_Framework_2024.pdf","Guardian Fixed Income Framework (2024)","Guardian FI"),
 "G2":("g2_funds_framework","papers/G2_Guardian_Funds_Framework_2024.pdf","Guardian Funds Framework (2024)","Guardian Funds"),
 "G3":("g3_interlinking","papers/G3_Guardian_Interlinking_Networks_2023.pdf","Guardian Interlinking Networks (2023)","Interlinking"),
 "G4":("g4_adoption_gap","papers/G4_Guardian_Bridging_Adoption_Gap_2024.pdf","Guardian: Bridging the Adoption Gap (2024)","Adoption Gap"),
 "G5":("g5_fx_workstream","papers/G5_Guardian_FX_Workstream_2024.pdf","Guardian FX Workstream (2024)","Guardian FX"),
 "G6":("g6_operationalising","papers/G6_Guardian_Operationalising_Tokenised_Funds_2024.pdf","Operationalising Tokenised Funds (2024)","Tokenised Funds Ops"),
 "G7":("g7_open_networks","papers/G7_Guardian_Open_Interoperable_Network_2023.pdf","Guardian: Open & Interoperable Networks (2023)","Open Networks"),
}

CSS = """
:root{--void:#0a0c10;--panel:#12161d;--line:#232c38;--ink:#e8edf4;--mut:#8c98a8;--gold:#c9a24b;--gold2:#e5c877}
*{box-sizing:border-box}body{margin:0;background:var(--void);color:var(--ink);font-family:Inter,system-ui,sans-serif;line-height:1.75;-webkit-font-smoothing:antialiased}
.wrap{max-width:840px;margin:0 auto;padding:0 24px 80px}
header.top{border-bottom:1px solid var(--line);position:sticky;top:0;background:rgba(10,12,16,.85);backdrop-filter:blur(10px);z-index:9}
header.top .w{max-width:840px;margin:0 auto;padding:0 24px;height:56px;display:flex;align-items:center;justify-content:space-between}
.brand{font-family:'IBM Plex Mono',monospace;font-weight:600;font-size:14px}.brand b{color:var(--gold)}
.brand a{color:inherit;text-decoration:none}
.crumb{font-family:'IBM Plex Mono',monospace;font-size:11px;color:var(--mut);text-transform:uppercase;letter-spacing:.14em}
h1{font-size:clamp(26px,4vw,38px);line-height:1.15;margin:48px 0 6px;letter-spacing:-.01em}
h2{font-size:22px;margin:44px 0 12px;color:var(--gold2);letter-spacing:-.01em}
h3{font-size:17px;margin:30px 0 8px}
p,li{font-size:16px;color:#cdd6e2}
hr{border:0;border-top:1px solid var(--line);margin:36px 0}
strong{color:var(--ink)}
em{color:var(--gold2);font-style:normal}
a{color:var(--gold2)}
a.cite{font-family:'IBM Plex Mono',monospace;font-size:.82em;color:var(--gold);text-decoration:none;border:1px solid rgba(201,162,75,.35);border-radius:5px;padding:0 5px;margin:0 1px;white-space:nowrap}
a.cite:hover{background:rgba(201,162,75,.12)}
table{border-collapse:collapse;width:100%;margin:14px 0;font-size:14px}
th,td{border:1px solid var(--line);padding:8px 10px;text-align:left}th{color:var(--gold2);font-family:'IBM Plex Mono',monospace;font-size:12px}
blockquote{border-left:3px solid var(--gold);margin:14px 0;padding:4px 18px;color:var(--mut)}
.stage{background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:8px 26px 20px;margin:22px 0}
.stagehead{font-family:'IBM Plex Mono',monospace;font-size:11px;letter-spacing:.2em;text-transform:uppercase;color:var(--gold);margin:18px 0 0}
.docbar{display:flex;gap:12px;flex-wrap:wrap;margin:14px 0 6px}
.docbar a{font-family:'IBM Plex Mono',monospace;font-size:13px;text-decoration:none;border:1px solid var(--line);border-radius:8px;padding:8px 14px;color:var(--gold2)}
.docbar a:hover{border-color:var(--gold)}
.byline{font-family:'IBM Plex Mono',monospace;font-size:13px;color:var(--mut);margin:0 0 28px}
.note{font-size:13.5px;color:var(--mut);border:1px solid var(--line);border-radius:10px;padding:12px 16px;margin:20px 0}
.idx{list-style:none;padding:0}.idx li{margin:10px 0;border:1px solid var(--line);border-radius:10px;padding:14px 18px;background:var(--panel)}
.idx a{text-decoration:none}
.idx .t{font-weight:600;color:var(--ink)}.idx .s{font-family:'IBM Plex Mono',monospace;font-size:12px;color:var(--mut)}
"""

FONTS='<link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">'

def shell(title, crumb, body, depth=0):
    pre = "../"*depth
    return f"""<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>{FONTS}<style>{CSS}</style></head><body>
<header class="top"><div class="w"><div class="brand"><a href="{pre}index.html">PBM<b>/</b>CBDC <span style="color:var(--mut);font-weight:400">Library</span></a></div><div class="crumb">{crumb}</div></div></header>
<div class="wrap">{body}</div></body></html>"""

def cite_links(htm, pre=""):
    # [P1] / [P1, Fig 15] / [P1][P4] / [id P1 §..] variants -> anchor to pdf
    def sub(m):
        ref=m.group(1); rest=m.group(2) or ""
        if ref not in DOCS: return m.group(0)
        pdf=pre+DOCS[ref][1]
        label=ref+rest
        return f'<a class="cite" href="{pdf}" target="_blank" title="{html.escape(DOCS[ref][2])}">{html.escape(label)}</a>'
    htm=re.sub(r'\[(?:id\s+)?(P\d+|G\d)((?:[ ,][^\]\[]{0,28})?)\]', sub, htm)
    return htm

md = lambda text: markdown.markdown(text, extensions=["tables"])

# ---- synthesis page ----
syn = open("analysis/SYNTHESIS.md").read()
body = cite_links(md(syn), pre="")
body += '<div class="note">Method: each source paper was run through a three-stage analytical chain — structured intake, knowledge-mapping (including gaps the documents do not state), and a full inward research note. The per-document chains are open: <a href="analysis/index.html">browse all 21 analyses</a>. Citations link directly to the hosted primary PDFs.</div>'
open("synthesis.html","w").write(shell("The Machine Singapore Built — Synthesis","Master Synthesis",body,0))

# ---- per-doc analysis pages ----
os.makedirs("analysis", exist_ok=True)
stage_names=[("1_intake.md","Stage 1 — Intake Analysis"),("2_knowledge-map.md","Stage 2 — Knowledge Map"),("3_sa-report.md","Stage 3 — Research Note")]
idx_items=[]
for ref,(folder,pdf,title,short) in DOCS.items():
    parts=[f'<h1>{html.escape(title)}</h1><p class="byline">Three-stage analytical chain · ref [{ref}]</p>']
    parts.append(f'<div class="docbar"><a href="../{pdf}" target="_blank">Open the original PDF ↗</a><a href="../synthesis.html">Master synthesis</a><a href="index.html">All analyses</a></div>')
    for fn,label in stage_names:
        p=os.path.join("analysis",folder,fn)
        if not os.path.exists(p): continue
        raw=open(p).read()
        raw=re.sub(r'^# .*$','',raw,count=1,flags=re.M)  # drop md h1, page has its own
        h=cite_links(md(raw), pre="../")
        parts.append(f'<p class="stagehead">{label}</p><div class="stage">{h}</div>')
    page=shell(f"{title} — Analysis", f"Analysis · {ref}", "\n".join(parts), depth=1)
    out=f"analysis/{ref}.html"
    open(out,"w").write(page)
    idx_items.append((ref,title))

# ---- analysis index ----
order=["P1","P2","P3","P4","P5","P6","P7","P8","P9","P10","P11","P14","P13","P12","G7","G3","G1","G2","G4","G5","G6"]
lis="".join(f'<li><a href="{r}.html"><span class="t">{html.escape(DOCS[r][2])}</span><br><span class="s">ref [{r}] · intake → knowledge map → research note</span></a></li>' for r in order)
ib=f'<h1>Document Analyses</h1><p class="byline">21 papers · three-stage chain each · every claim traceable to the hosted primary PDF</p><div class="docbar"><a href="../synthesis.html">Read the master synthesis</a><a href="../index.html">Paper library</a></div><ul class="idx">{lis}</ul>'
open("analysis/index.html","w").write(shell("Document Analyses","Analysis Index",ib,depth=1))
print("built synthesis.html, analysis/index.html and", len(DOCS), "analysis pages")

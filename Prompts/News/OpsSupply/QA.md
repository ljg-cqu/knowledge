# Operations & Supply Chain News Intelligence Q&A (Minimal Viable)

Act as an operations & supply chain analyst. Using only this prompt and web search, generate 4–6 decision-critical Q&As from recent industry news for senior operations leaders with limited reading time. This prompt is fully self-contained; do not rely on other files or previous conversation.

**Cadence**: Monthly brief | 4–6h analyst-equivalent effort | **Expires**: 4 weeks from generation (re-validate if used after 4 weeks)

**Scope**: Decision-critical operations news only (supply disruptions, supplier risk, cost shocks, regulatory/safety changes, capacity constraints) in mature organizations.

**Exclusions**: Long-term R&D, vendor marketing, incremental process improvements, rumors, stale news (>4mo HV, >6mo MV).

**Freshness** (category-adaptive):
- **High-Velocity** (Disruptions, Logistics, Supplier Risk): ≥75% <1mo (≥25% in 1–7d), ≥95% <2mo, 100% ≤4mo  
- **Medium-Velocity** (Technology, Inventory/Demand): ≥65% <2mo (≥20% in 1–14d), ≥90% <3mo, 100% ≤6mo  
- **Long-Tail** (Safety/Regulatory, Resilience): ≥50% <6mo, ≥80% <12mo, 100% ≤18mo  
- **Overall**: ≥70% <2mo, ≥90% <4mo, 100% ≤12mo  
- **Validity**: 4 weeks; re-validate if used beyond 4 weeks

**Decision Criticality Framework** (include if ≥1 criterion met):
1. **Blocks Decision**: Directly impacts sourcing, capacity, supplier change, resilience investment
2. **Creates Risk**: Material supply disruption, safety incident, regulatory breach, cost shock >5%
3. **Affects ≥2 Core Roles**: Multi-stakeholder impact (COO + VP Supply, Plant Manager + Procurement, etc.)
4. **Requires Action**: 1-6mo action window (not speculative)
5. **Quantified Impact**: Lead time %, capacity %, cost/unit, incident rates, service level impact

---

## I. Framework

**Stakeholders** (5 core):  
COO, VP Supply Chain, Plant/Factory Manager, Head of Procurement, Quality & Safety Lead.

**Operations Cycles** (4, decision-critical):  
1. **Source**: Procurement, supplier selection, contracts, risk management  
2. **Make**: Production, capacity, manufacturing efficiency/quality  
3. **Deliver**: Logistics, warehousing, distribution, lead times  
4. **Enable**: Safety, compliance, resilience, technology enablers

**News Categories** (4, each Q covers ≥1):

1. **Supply Chain & Logistics Disruptions**: Port congestion, shipping delays, freight rate shocks, route closures, geopolitical disruptions, capacity changes

2. **Procurement & Supplier Risk**: Supplier bankruptcies, financial distress, quality incidents, recalls, commodity price shocks, dual-sourcing needs

3. **Manufacturing & Capacity**: Plant closures, capacity constraints, automation ROI, production efficiency changes

4. **Quality, Safety & Compliance**: Product recalls, safety incidents, regulatory changes (OSHA, ISO), new standards, process safety

**News Relevance Criteria**: Must meet freshness thresholds and ≥1 Decision Criticality criterion; prioritize items that block sourcing/capacity/supplier/resilience decisions, create material supply/safety/regulatory/cost (>5%) risk, affect ≥2 core roles, and have quantified impact (lead time %, capacity %, cost/unit, incident rates, service level %).

---

## II. Requirements

**Q&A**: 4–6 total | 1-2/cycle | 200–300w | 100% news-driven | 100% ≥1 cite, ≥30% ≥2 cites | ≥1 category + impact + decision

**Operations Cycles** (4, 1-2 Q each): Source, Make, Deliver, Enable (skip if no decision-critical news)

**Category Coverage** (min): Supply Chain & Logistics ≥50%, Procurement & Supplier ≥40%, Manufacturing ≥25%, Quality/Safety ≥25%

**Decision Criticality** (100%): Each Q must satisfy ≥1 of 5 criteria (Blocks/Risk/Roles/Action/Quantified)

**Stakeholders** (≥4/5): COO, VP Supply Chain, Plant Manager, Procurement Head, Quality Lead (core roles only)

**References** (build before Q&A): G≥8 (100% terms used), N≥4-5 (per freshness), L≥2 (logistics/freight), M≥2 (manufacturing/OEE), S≥2 (safety/regulatory), R≥2 (research), A≥6 (APA 7th+tag)

**Visuals**: ≥2 diagrams + ≥1 table

**Quality Gates** (fail ANY = stop):
1. **Decision Criticality**: 100% satisfy ≥1 criterion (Blocks/Risk/Roles/Action/Quantified)
2. **News**: 100% cite ≥1 per freshness; 0% marketing/rumors
3. **Impact**: 100% ≥2 cycles + ≥2 roles + quantified
4. **Decision**: 100% decision + rationale + timeline
5. **Sources**: ≥3 types, max 50%/type; 100% URLs valid
6. **Actionability**: 100% concrete; 0% abstract

---

## III. Execution

### Step 1: News Discovery & Curation (Minimal)

**Record generation date (YYYY-MM-DD)—calculate all news ages from this.**

1. **Identify Domain**: Industry + operations focus (e.g., "Global Automotive Supply Chain Q1 2025").

2. **Search** (≥10-15 candidates, tiered):

   **Tier 1** (1-7d, search first): `"[Domain] port congestion|shipment delay|freight rate|plant shutdown|supplier bankruptcy|recall"` + 1-7d
   
   **Tier 2** (7-30d if insufficient): Same + 7-30d
   
   **Tier 3** (1-6mo if needed): Regulatory, safety, resilience news

   **Sources** (whitelist, prioritize):
   - **Disruptions**: Supply Chain Dive, Logistics Management, IndustryWeek
   - **Logistics**: Maersk, DHL, UPS, FedEx reports
   - **Manufacturing**: McKinsey Operations, BCG, TPS references
   - **Regulatory**: OSHA, EPA, EU directives
   - **Avoid**: Vendor marketing, rumors, speculation

   **Tools**: Perplexity ("past week"), ChatGPT ("latest"), Google (`after:DATE`), Supply Chain Dive

3. **Curate** (≥10-15 candidates: Disruptions ≥4, Supplier ≥3, Manufacturing ≥2, Safety ≥2):
   - ✅ Age per freshness
   - ✅ Whitelist OR primary source
   - ✅ Satisfies ≥1 Decision Criticality criterion
   - ✅ Specific details (dates, names, numbers, metrics)
   - ✅ Not marketing/rumors
   - ✅ For critical metrics (e.g., % cost shock, lead time, incident rates), cross-check against ≥2 credible sources when possible; if figures conflict or are only approximate, explicitly flag the uncertainty in the Q&A.

4. **Verify**: Check decision criticality; if fail, retry earlier tiers

5. **Allocate**: 4-6 Q × 4 cycles (1-2 each) × 4 categories (≥1/Q) × ≥4 roles

### Step 2: Build References (Minimal)

**Format**: G# (term, def+analogy, context) | N# (news, source, date, cat, URL) | L# (logistics, metric, URL) | M# (manufacturing, metric, URL) | S# (safety/regulatory, standard, URL) | R# (research, findings, URL) | A# (APA 7th+tag)

**Citation**: Markdown reference links: `[Ref: N1][n1]` in text, `[n1]: URL` at answer end

**Floors**: G≥8 (100% terms used), N≥4-5, L≥2, M≥2, S≥2, R≥2, A≥6

**Glossary** (only terms used in Q&As):
- **Coverage**: Only terms/acronyms used (OEE, SCOR, lead time, capacity %, etc.)
- **Clarity**: Plain language, avoid jargon
- **Analogies**: 1-2 real-world comparisons per term
- **Context**: Why it matters for decisions
- **Examples**: Real numbers

**News Entry**: **Title** (Source, MM/DD): Summary | Cat | URL | Decision Criticality criterion

### Step 2.5: Opportunistic Refresh (optional, skip default)

Trigger only if **major disruption** (port/canal blockage, tier-1 supplier failure, 0-day safety incident) within 24–72h affecting ≥3 Q&As.

**Action**: Quick search → Add 1-2 "BREAKING" items → Adjust 1-2 Qs → Document

### Step 3: Generate Q&A (batch 2-3, self-check each)

**Before**: Review glossary. Track ALL terms used.

**Patterns**: "[News] implications for [Cycles]+[Roles]?" | "[Supplier Event]: sourcing strategy?" | "[Disruption]: mitigation for [Plant/Network]?" | "[Regulatory Change]: compliance roadmap?"

**Avoid**: Generic questions, hype, unattributed claims, stale news, speculation

**Structure** (200–300w per Q&A, Markdown):
1. `### Qn: [Decision-focused question]`
2. `#### News` (~40w): What happened, when, why it matters, and category; include `[Ref: N#][n#]`.
3. `#### Impact` (~80w): Explain consequences across ≥2 operations cycles with quantified effects (lead time %, capacity %, cost/unit, incident rates, service level %, etc.).
4. `#### Stakeholders` (~50w): Describe how ≥2 core roles are affected (concerns, trade-offs, required actions).
5. `#### Options & Decision` (~70w): Compare ≥2 realistic options (e.g., adjust, mitigate, invest, monitor, exit) with benefits, costs, and risks; state a clear recommended decision, when it applies, and its main limitations.
6. `#### Actions & Success Measures` (~40w): Specify immediate (0-2wk) and short-term (2wk-2mo) actions with owners and 1–3 measurable indicators to track (e.g., target lead time, service level %, cost/unit) and how they will be monitored.
7. `#### References`: Define Markdown reference links at the end of the document: `[Ref: N1][n1]` in text, `[n1]: URL` at bottom.

**Self-Check**: Age OK | Decision Criticality ✓ | ≥2 cycles | ≥2 roles | Decision clear | 200-300w | Quantified | ≥1 cite | 0% hype | 100% actionable | All terms in glossary

### Step 4: Visuals (≥2 diagrams + ≥1 table)

**Types**: Supply chain risk heatmap, decision trees, capacity vs demand table, impact matrix, using Mermaid for flows and Markdown tables/2×2 matrices for data.

**Checks**: All links resolve; ages follow freshness; floors from Step 2 are met; each Q&A shows a clear decision with rationale, criteria, timeline, and ≥2 roles with actions and authority.

### Step 5: Self-Review & Validate (fail ANY = stop, correct, then re-check before final output)

**Quantitative**: Floors met; glossary 100%; 4 cycles covered; category % targets met; ≥4 roles; citations OK; all Q&As (4–6) within 200–300w; visuals present; decisions and timelines included; ages within freshness rules.

**Qualitative**: News meets freshness thresholds with 0% hype; Decision Criticality 100%; each Q&A covers ≥2 cycles and ≥2 roles with quantified impact; sources span ≥3 types with valid links; per-cycle ≥1 news+analysis; content is 100% quantified, actionable, and evidence-based; search steps documented.

**Checklist** (all YES): All validations PASS; floors met; glossary complete (100% terms, ≥50% analogies); no placeholders; visuals and citations OK; impact, decision, timeline, categories, and roles OK; freshness OK; URLs valid; dates recorded (generation + expire=gen+4wk); search documented.

---

## IV. Validation Report (Minimal)

| # | Check | Measurement | Criteria | Result | Status |
|---|-------|-------------|----------|--------|--------|
| 1 | **Freshness** | HV: __%<1mo (1-7d:__%), __%<2mo \| MV: __%<2mo (1-7d:__%) \| Overall: __%<2mo | Per header | | PASS/FAIL |
| 2 | **Floors** | G:__ N:__ L:__ M:__ S:__ R:__ A:__ Q:__ | ≥8,≥4-5,≥2,≥2,≥2,≥2,≥6,4-6 | | PASS/FAIL |
| 3 | **Glossary** | __%terms; __%analogies | 100%;≥50% | | PASS/FAIL |
| 4 | **Cycles** | __/4 (1-2Q each); total__ | 4/4;4-6 | | PASS/FAIL |
| 5 | **Categories** | Disrupt__% Supplier__% Mfg__% Safety__% | ≥50,40,25,25% | | PASS/FAIL |
| 6 | **Roles** | __/5 | ≥4 | | PASS/FAIL |
| 7 | **Decision Criticality** | __% satisfy ≥1 criterion | 100% | | PASS/FAIL |
| 8 | **Impact** | __% ≥2cycles+2roles+quantified | 100% | | PASS/FAIL |
| 9 | **Decision** | __% decision+rationale+criteria | 100% | | PASS/FAIL |
| 10 | **Citations** | __%≥1cite | 100% | | PASS/FAIL |
| 11 | **Words** | All Q&As: __%200-300w | 100% | | PASS/FAIL |
| 12 | **Visuals** | diag__; tab__ | ≥2;≥1 | | PASS/FAIL |
| | **Meta** | Start:__ End:__ Expires:[+4wk] | | INFO |
| | **Age Dist** | <1mo__%(1-7d__%) 1-2mo__% 2-4mo__% | Per header | | INFO |
| | **OVERALL** | All checks | All PASS | | PASS/FAIL |

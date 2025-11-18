# Operations & Supply Chain News Intelligence Q&A Generator

## Table of Contents
- [I. Context & Scope](#i-context--scope)
- [II. Requirements](#ii-requirements)
- [III. Execution](#iii-execution)
- [IV. Validation Report](#iv-validation-report)
- [V. Methodology Sources](#v-methodology-sources)
- [VI. Question Quality](#vi-question-quality)
- [VII. Output Format](#vii-output-format)
- [VIII. Glossary](#viii-glossary)
- [IX. Quick Check](#ix-quick-check-before-delivery)

## I. Context & Scope

**Problem**: Operations and supply chain leaders lack actionable intelligence from fragmented news sources, causing delayed responses to disruptions, supplier risks, and cost pressures.

**Scope**: Generate 4-6 decision-critical Q&As from operations/supply chain news (manufacturing, logistics, procurement, inventory, facilities, quality, safety, compliance, resilience) for COO, VP Operations, supply chain leadership.

**MECE Position**: Post-PMF operations & supply chain. **Owns**: Physical operations, manufacturing, logistics, procurement, supplier management, facilities, quality (QA/QC, standards, certifications), safety, routine operational compliance (environmental, safety, trade, manufacturing), inventory, resilience. **Excludes**: Product R&D (StratIntel), technical infrastructure/IT (TechOps), GTM (CommOps), corporate M&A (FinEcon), major litigation/IP (StratIntel), talent strategy (PeopleWF, except frontline workforce safety/productivity).

**Cadence**: Monthly | 4-6h/cycle | **Expires**: 4wk post-gen | **Freshness**: ≥60% <2mo (supplier/logistics), ≥40% <6mo (facilities/regulatory), 100% ≤12mo

**Definitions**:
- **Decision-critical**: News requiring 1-12mo action impacting costs ≥5%, blocking operations decisions, creating material risk, or requiring multi-stakeholder coordination
- **Operations & Supply Chain**: Manufacturing, production, logistics, procurement, inventory, facilities, quality, safety, resilience, supplier management
- **MECE**: Categories cover all ops/supply domains without overlap
- **Quantified Impact**: Specific metrics (cost %, lead time days, defect rates, capacity units, OTIF %) with baselines

**Exclude**: Product development, sales/marketing execution, HR talent (except frontline workforce), pure IT/software systems, >12mo strategic R&D, rumors, internal-only changes

**Inputs**: Domain/vertical, period, company (size, manufacturing footprint, supply chain complexity) | Metrics (COGS, lead time, inventory turns, OEE, defect rate, OTIF, capacity utilization) | Stakeholders (COO, VP Ops, VP Supply Chain, Procurement, Logistics, Quality, Safety) | Constraints (budget, capacity, regulatory, geopolitical)

**Decision Criticality** (≥1):
1. **[CRITICAL] Blocks Decision**: Capacity expansion, supplier change, reshoring, facility investment
2. **[CRITICAL] Creates Risk**: Supply disruption, quality/safety incident, cost spike ≥5%, regulatory violation
3. **[IMPORTANT] Multi-Stakeholder**: ≥2 roles with different priorities
4. **[IMPORTANT] Requires Action**: 1-12mo timeline with resource commitment
5. **[IMPORTANT] Quantified Impact**: Cost, lead time, quality, capacity, safety, or inventory metrics

**Categories** (MECE):
1. **Manufacturing & Production**: Capacity, OEE, automation, quality, yield, production costs
2. **Supply Chain & Logistics**: Supplier risk, lead times, transportation, freight costs, inventory levels
3. **Procurement & Sourcing**: Commodity prices, contract terms, supplier diversity, dual sourcing
4. **Facilities & Infrastructure**: Expansion, maintenance, utilities, real estate, warehousing
5. **Quality & Safety**: Standards compliance, incidents, recalls, certifications, audits
6. **Resilience & Risk**: Disruption response, business continuity, geopolitical risk, scenario planning

## II. Requirements

**Q&A**: 4-6 across 3-4 cycles, covering all categories

**Structure** (150-200w):
1. **News** (~30w): What, when, why, category + citation
2. **Impact** (~60w): ≥2 cycles, ≥2 roles, quantified metrics (cost, lead time, capacity, quality)
3. **Stakeholders** (~40w): ≥2 roles with concerns/actions
4. **Decision** (~50w): ≥2 options with cost/benefit/risk, rationale, trade-offs, timeline
5. **Action** (~30w): Immediate (0-2wk) + short (2wk-2mo) + medium (2-6mo), owner + metrics

**Cycles** (3-4): Source (Procurement) | Make (Production) | Deliver (Logistics) | Enable (Quality/Safety/Resilience)

**Stakeholders** (≥4): COO, VP Operations, VP Supply Chain, Procurement Head, Logistics Director, Plant Manager, Quality Lead, Safety Manager

**References**: G≥4, N≥4, I≥1, S≥1, R≥1, A≥3. 100% used.

**Visuals**: ≥2 diagrams + ≥1 table

**Quality Gates**:
- **[CRITICAL]** 100% meet ≥1 criticality criterion
- **[CRITICAL]** 100% cited with valid, accessible URLs
- **[CRITICAL]** 100% quantified impact (multi-cycle + multi-role)
- **[IMPORTANT]** 100% include ≥2 decision options with rationale + timeline
- **[IMPORTANT]** 100% concrete actions with owner + metrics

**Success Criteria**: Time: 8h → 4-6h | Freshness: ≥60% <2mo | Stakeholders: ≥4 roles | URL validity: 100%

## III. Execution

### Step 1: News Discovery

Record generation date (YYYY-MM-DD).

**Search** (10-15 candidates):
- **Keywords**: `[Domain] {supply disruption|supplier risk|lead time|freight cost|capacity|OEE|quality recall|safety incident|procurement|inventory|reshoring}`
- **Sources**: 
  - **Trade**: Supply Chain Dive, Logistics Management, IndustryWeek, Manufacturing.net
  - **Consulting**: McKinsey Supply Chain, Gartner Supply Chain, Deloitte Supply Chain
  - **Industry**: CSCMP Supply Chain Quarterly, ASCM, Supply Chain Management Review
  - **Regulatory**: OSHA, FDA, EPA, CPSC
  - **Data**: Freightos, S&P Global Commodity Insights
- **Tools**: Perplexity `"[domain] supply chain disruption" timerange:1month` | ChatGPT "Latest [domain] operations news 60d" | Google `site:supplychaindive.com OR site:logisticsmgmt.com "[domain]" after:YYYY-MM-DD`

**Filter**: Freshness ✓ | Trusted source ✓ | ≥1 criticality criterion ✓ | No rumors ✓

**Allocate**: 4-6 Q across 3-4 cycles, all categories, ≥4 roles

### Step 2: Build References

**Formats**:
- **G#**: Term (def + analogy + context) — `G1. OEE: Manufacturing efficiency combining availability × performance × quality (0-100%); measures asset utilization; target 85%+`
- **N#**: Title (Source, MM/DD): Summary | Category | URL — `N1. "Port congestion +30%" (Supply Chain Dive, 11/15): West Coast delays avg 12d | Logistics | https://...`
- **I#**: Report (Firm/Org, Date): Findings | URL — `I1. Supply Chain Top 25 (Gartner, 2024): Best practices | https://...`
- **S#**: Standard/Regulation (Authority, Date): Requirements | URL — `S1. ISO 9001:2015 (ISO, 2024): Quality management | https://...`
- **R#**: Report (Firm, Date): Findings | URL — `R1. State of Manufacturing 2024 (IndustryWeek, Q3): OEE median 72% | https://...`
- **A#**: APA 7th [Tag] — `A1. Smith, J. (2024). Supply chain resilience. Operations Journal, 15(2), 45-67. [Empirical]`

**Citation**: `[Ref: N1 – Supply Chain Dive, 2024][n1]`

### Step 3: Generate Q&A

Pattern: "[News] implications for [Cycle]+[Roles]?"

**Avoid**: Generic claims (quantify) | Hype (show limitations) | Unattributed statements (cite) | Stale news | Speculation (flag uncertainty)

**Self-Check**: Criticality ✓ | ≥2 cycles/roles | ≥2 options | 150-200w | Quantified | Cited | Actionable | Balanced

### Step 4: Add Visuals

≥2 diagrams (Mermaid: supplier risk matrix, decision tree, disruption impact flow, scenario comparison) + ≥1 table

Example: `graph TD; A[High Impact] -->|High Prob| B[Critical]; A -->|Low Prob| C[Monitor]` | Table: Option, Cost, Lead Time Impact, Risk, Timeline

### Step 5: Validate

**Self-Review**: URLs accessible | Calculations correct | No contradictions | Terminology consistent | All references used | Uncertainties flagged

**Quality Gates**: All CRITICAL + IMPORTANT pass | Reference floors met | No placeholders | Valid URLs

## IV. Validation Report

| Check | Criteria | Result | Status |
|-------|----------|--------|--------|
| **Freshness** | ≥60% <2mo (logistics/supplier), ≥40% <6mo (facilities/regulatory), 100% ≤12mo | | PASS/FAIL |
| **References** | G≥4, N≥4, I≥1, S≥1, R≥1, A≥3 | | PASS/FAIL |
| **Q&A** | 4-6 Q, 3-4 cycles, all categories | | PASS/FAIL |
| **Roles** | ≥4 roles | | PASS/FAIL |
| **Quality** | 100% meet all gates | | PASS/FAIL |
| **Words** | 100% within 150-200w | | PASS/FAIL |
| **Visuals** | ≥2 diagrams, ≥1 table | | PASS/FAIL |
| **Meta** | Start, End, Expires (+4wk) | | INFO |
| **OVERALL** | All PASS | | PASS/FAIL |

## V. Methodology Sources

**Framework**: SCOR Model (ASCM, 2024), APICS Supply Chain Management (2023) | **Freshness**: Supply chain 60-90d cycle per Gartner (2024) | **References**: APA 7th, ISO standards | **Quality**: Supply Chain Dive editorial standards, CSCMP research guidelines

## VI. Question Quality

**✓** "Port congestion +30% (Nov'24): logistics cost response?" | "ISO 9001:2015 updates: quality audit strategy?" | "Steel prices +18% (Oct'24): procurement decision?" | "Supplier bankruptcy (Nov'24): dual-sourcing timeline?"

**✗** "How does supply chain work?" (no news) | "What is OEE?" (overview) | "Should we use JIT?" (no trigger) | "Competitor opened facility" (no decision)

## VII. Output Format

### Executive Summary

**Domain**: [Category] | **Period**: [Date Range] | **Coverage**: [# Q, categories]

**Key Insights**: 1-2 high-impact findings (impact → decision → timeline)

**Roles**: ≥4 | **Refs**: G#, N#, I#, S#, R#, A# counts

### Q&A Template

**Q#: [News Question + Cycle + Roles]**

**Cycle**: [X] | **Roles**: [Primary, Secondary] | **Category**: [Y] | **Criticality**: [Criterion]

**News**: What, when, why, category [Ref: N#][n#]

**Impact**: **Cycles** (≥2) | **Metrics**: Cost/Lead Time/Quality/Capacity (quantified with baselines)

**Stakeholders**: **[Role 1]**: Concerns + actions | **[Role 2]**: Concerns + actions

**Decision**: **Options**: (A) [cost/benefit/risk], (B) [cost/benefit/risk] | **Recommendation**: [Choice] | **Rationale**: [Why] | **Trade-offs**: Risks/limitations | **Timeline**: Milestones (2wk, 2mo, 6mo)

**Action**: **Immediate (0-2wk)**: Tasks + owner | **Short (2wk-2mo)**: Tasks + owner | **Medium (2-6mo)**: Tasks + owner + metrics

[n1]: URL

---

### References

See Step 2 for reference formats (G#, N#, I#, S#, R#, A#).

---

## VIII. Glossary

**G1. OEE**: Manufacturing efficiency combining availability × performance × quality (0-100%); measures asset utilization; target 85%+. Example: OEE 72% = 28% capacity loss.

**G2. OTIF**: On-Time In-Full - deliveries meeting schedule and quantity. Context: Supply chain reliability KPI. Example: OTIF 95% = 95 of 100 shipments meet commitments.

**G3. Lead Time**: Duration from order to delivery. Context: Supply chain planning. Example: 90-day lead time requires 90-day advance planning.

**G4. Inventory Turns**: Annual inventory replacement (COGS ÷ Avg Inventory). Context: Working capital efficiency. Example: 12 turns = monthly replacement.

**G5. COGS**: Cost of Goods Sold - direct production costs (materials, labor, overhead). Context: Profitability analysis. Example: COGS 60% of revenue = 40% gross margin.

**G6. Dual Sourcing**: Two suppliers for same item. Context: Risk mitigation. Example: 70/30 split primary/secondary.

**G7. Reshoring**: Moving production back to domestic facilities. Context: Supply chain resilience. Example: China to US manufacturing.

**G8. JIT**: Just-in-Time - ordering supplies only when needed. Context: Working capital optimization. Example: Auto parts delivered same day as assembly.

## IX. Quick Check (Before Delivery)

☐ **Self-contained**: All context present  
☐ Context | ☐ Clarity | ☐ Precision | ☐ Relevance  
☐ MECE | ☐ Sufficiency | ☐ Breadth | ☐ Depth  
☐ Significance | ☐ Priority | ☐ Concision | ☐ Accuracy | ☐ Credibility  
☐ Logic | ☐ Risk/Value | ☐ Fairness  
☐ Structure | ☐ Consistency | ☐ TOC  
☐ Evidence | ☐ Verification | ☐ Practicality | ☐ Success Criteria

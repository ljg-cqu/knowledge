# Commercial Operations News Intelligence Q&A Generator

## Table of Contents
- [I. Context & Scope](#i-context--scope)
- [II. Requirements](#ii-requirements)
- [III. Execution](#iii-execution)
- [IV. Validation Report](#iv-validation-report)
- [V. Methodology Sources](#v-methodology-sources)
- [VI. Question Quality](#vi-question-quality)
- [VII. Output Format](#vii-output-format)
- [VIII. Quick Check](#viii-quick-check-before-delivery)

## I. Context & Scope

**Problem**: Commercial teams lack actionable intelligence from fragmented news sources, causing delayed responses and missed revenue opportunities.

**Scope**: Generate 4-6 decision-critical Q&As from commercial news (sales, marketing, CS, RevOps, GTM, competitive intel) for CRO, VP Sales, VP Marketing, VP CS, RevOps. Bi-weekly | 4-6h/cycle | **Expires**: 2wk post-gen | **Freshness**: ≥70% <2mo (≥25% <1wk), 100% ≤9mo.

**Definitions**:
- **Decision-critical**: 1-6mo action impacting revenue, blocking decisions, creating risk, or requiring ≥2 stakeholders
- **Commercial Operations**: Sales execution, marketing ops, customer success, RevOps, GTM strategy, competitive intelligence

**Exclude**: Technical specs/architecture, product R&D, corporate finance (except GTM pricing), >6mo strategy, rumors, internal-only changes, single-function tasks.

**Inputs**: Domain/vertical, period, company (size, stage, GTM, ACV), metrics (pipeline $, win rate, CAC, LTV, NRR, churn, conversion), stakeholders, constraints (budget, hiring, regulatory).

**Criticality Criteria** (≥1 required):
1. **[CRITICAL]** Blocks decision (quota, GTM pivot, revenue model) OR creates risk (competitive threat, churn signal, CAC/LTV pressure)
2. **[IMPORTANT]** Multi-stakeholder (≥2 roles) with 1-6mo action AND quantified impact (revenue, pipeline, conversion, retention, efficiency)

**Categories** (MECE):
1. **Sales**: Win rates, quota, pipeline velocity, cycle length
2. **Marketing**: CAC, lead conversion, campaign ROI, attribution
3. **Customer Success**: Churn, NRR, expansion ARR, retention
4. **RevOps**: CRM/tools, analytics, process optimization, forecasting

## II. Requirements

**Q&A Count**: 4-6 across 3-4 stages (Lead Gen & Demand, Sales & Closing, Retention & Expansion, Analytics & Optimization), covering all categories (Sales, Marketing, CS, RevOps), engaging ≥4 roles (CRO, VP Sales, VP Marketing, VP CS, RevOps Analyst).

**Structure per Q** (150-200w): News (~30w: what, when, why, category + citation) | Impact (~60w: ≥2 stages, ≥2 roles, quantified metrics) | Stakeholders (~40w: ≥2 roles with concerns/actions) | Decision (~50w: ≥2 options with cost/benefit, rationale, trade-offs) | Action (~20w: immediate 0-2wk + short 2wk-2mo, owner + metrics).

**References**: G≥4, N≥4, P≥1, M≥1, R≥1, A≥4. 100% used.

**Visuals**: ≥2 diagrams + ≥1 table.

**Quality Gates**:
- **[CRITICAL]** 100% meet ≥1 criticality criterion, cited with valid URLs, quantified impact (multi-stage + multi-role)
- **[IMPORTANT]** 100% include ≥2 decision options (rationale + timeline) + concrete actions (owner + metrics)

**Success Criteria**: Time 4-6h | Freshness ≥70% <2mo | Stakeholders ≥4 | URL validity 100%.

## III. Execution

### Step 1: News Discovery

Record generation date (YYYY-MM-DD). **Search** 10-15 candidates using keywords `[Domain] {sales performance|pipeline|quota|CAC|conversion|churn|retention|expansion|competitive|win/loss}` from SaaStr, Sales Hacker, MarketingProfs, Gong, Salesforce, HubSpot, Gainsight, RevOps Co-op, G2, Gartner, Forrester. **Tools**: Perplexity `"[domain] sales trends" timerange:1month`, ChatGPT "Latest [domain] commercial ops news 60d", Google `site:saastr.com OR site:saleshacker.com "[domain]" after:YYYY-MM-DD`. **Filter**: Freshness ✓ | Trusted source ✓ | ≥1 criticality ✓ | No rumors ✓. **Allocate**: 4-6 Q across 3-4 stages, all categories, ≥4 roles.

### Step 2: Build References

**Formats**:
- **G#**: Term (def + analogy + context) — `G1. Pipeline Velocity: Time to move opps through stages (conveyor speed); measures sales efficiency`
- **N#**: Title (Source, MM/DD): Summary | Category | URL — `N1. "Sales Cycle ↓18%" (Gong Labs, 11/15): Q3 faster enterprise closes | Sales | https://...`
- **P#**: Platform (Source, Date): Model | URL — `P1. Gong Revenue Intelligence (Gong.io, 2024): Conversation analytics | https://...`
- **M#**: Methodology (Source, Date): Application | URL — `M1. MEDDIC (Sales Hacker, 2024): Enterprise qualification | https://...`
- **R#**: Report (Firm, Date): Findings | URL — `R1. SaaS Benchmarks 2024 (SaaS Capital, Q3): Median NRR 108% | https://...`
- **A#**: APA 7th [Tag] — `A1. Smith, J. (2024). Revenue ops trends. RevOps Journal, 12(3), 45-67. [Empirical]`

**Citation**: `[Ref: N1 – Gong, 2024][n1]`

### Step 3: Generate Q&A

Pattern: "[News] implications for [Stage]+[Roles]?". **Avoid**: Generic claims (quantify), hype (show limitations), unattributed statements (cite), stale news, speculation (flag uncertainty). **Self-Check**: Criticality ✓ | ≥2 stages/roles | ≥2 options | 150-200w | Quantified | Cited | Actionable | Balanced.

### Step 4: Add Visuals

≥2 diagrams (Mermaid: funnels, pipelines, cohorts, matrices) + ≥1 table. Example: `graph TD; A[Leads 10K] --> B[MQLs 2K] --> C[SQLs 500] --> D[Closed 100]` | Table: Competitor, CAC, Change, Source.

### Step 5: Validate

**Self-Review**: URLs accessible, calculations correct, no contradictions, terminology consistent, all references used, uncertainties flagged. **Quality Gates**: All CRITICAL + IMPORTANT pass, reference floors met, no placeholders, valid URLs.

## IV. Validation Report

| Check | Criteria | Result | Status |
|-------|----------|--------|--------|
| **Freshness** | ≥70% <2mo, 100% ≤9mo | | PASS/FAIL |
| **References** | G≥4, N≥4, P≥1, M≥1, R≥1, A≥4 | | PASS/FAIL |
| **Q&A** | 4-6 Q, 3-4 stages, all categories | | PASS/FAIL |
| **Roles** | ≥4 roles | | PASS/FAIL |
| **Quality** | 100% meet all gates | | PASS/FAIL |
| **Words** | 100% within 150-200w | | PASS/FAIL |
| **Visuals** | ≥2 diagrams, ≥1 table | | PASS/FAIL |
| **Meta** | Start, End, Expires (+2wk) | | INFO |
| **OVERALL** | All PASS | | PASS/FAIL |

## V. Methodology Sources

**Framework**: RevOps Co-op (2024), SaaStr (2023-2024), Gartner GTM (2024) | **Freshness**: B2B SaaS 2-3mo cycle per OpenView (2024) | **References**: APA 7th, Forrester/Gartner formats | **Quality**: CMI (2024), Reuters Trust Principles

## VI. Question Quality

**✓** "Gong Labs Q3: 12% pipeline velocity drop—Sales & RevOps response?" | "SaaS Capital: NRR 108% vs our 95%—CS retention tactics?" | "HubSpot pricing ↑15% (Nov'24): GTM strategy?" | "Competitor CAC ↓20% (Oct'24): our response?"

**✗** "How does sales work?" (no news) | "What is NPS?" (overview) | "Should we use Salesforce?" (no trigger) | "Competitor launched feature" (no decision)

## VII. Output Format

### Executive Summary

**Domain**: [Category] | **Period**: [Date Range] | **Coverage**: [# Q, categories]

**Key Insights**: 1-2 high-impact findings (impact → decision → timeline)

**Roles**: ≥4 | **Refs**: G#, N#, P#, M#, R#, A# counts

### Q&A Template

**Q#: [News Question + Stage + Roles]**

**Stage**: [X] | **Roles**: [Primary, Secondary] | **Category**: [Y] | **Criticality**: [Criterion]

**News**: What, when, why, category [Ref: N#][n#]

**Impact**: **Stages** (≥2) | **Metrics**: Revenue/Pipeline/Conversion/Retention (quantified)

**Stakeholders**: **[Role 1]**: Concerns + actions | **[Role 2]**: Concerns + actions

**Decision**: **Options**: (A) [cost/benefit], (B) [cost/benefit] | **Recommendation**: [Choice] | **Rationale**: [Why] | **Trade-offs**: Risks/limitations

**Action**: **Immediate (0-2wk)**: Tasks + owner | **Short (2wk-2mo)**: Tasks + owner + metrics

[n1]: URL

---

### References

See **Step 2** for reference formats (G#, N#, P#, M#, R#, A#).

---

## VIII. Quick Check (Before Delivery)

☐ **Self-contained**: All context present  
☐ Context | ☐ Clarity | ☐ Precision | ☐ Relevance  
☐ MECE | ☐ Sufficiency | ☐ Breadth | ☐ Depth  
☐ Significance | ☐ Priority | ☐ Concision | ☐ Accuracy | ☐ Credibility  
☐ Logic | ☐ Risk/Value | ☐ Fairness  
☐ Structure | ☐ Consistency | ☐ TOC  
☐ Evidence | ☐ Verification | ☐ Practicality | ☐ Success Criteria

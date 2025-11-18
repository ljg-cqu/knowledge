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

**Problem**: Commercial teams lack timely, actionable intelligence from fragmented news sources, causing delayed competitive responses and missed revenue opportunities.

**Scope**: Generate 4-6 decision-critical Q&As from recent commercial news (sales, marketing, CS, RevOps, GTM, competitive intel) for CRO, Sales, Marketing, CS, and RevOps decision-making.

**Target**: Bi-weekly cycles | 4-6h/cycle | **Expires**: 2wk post-gen | **Freshness**: ≥70% <2mo (≥25% <1wk), 100% ≤9mo

**Definitions**:
- **Decision-critical**: News requiring action within 1-6mo that impacts revenue, blocks decisions, creates risk, or requires multi-stakeholder coordination
- **Commercial Operations**: Sales execution, marketing ops, customer success, RevOps, GTM strategy, competitive intelligence

**Exclude**: Technical specs/architecture, product R&D, corporate finance (except GTM pricing), >6mo strategy, rumors, internal-only process changes, single-function tasks.

**Role**: Commercial Operations news intelligence analyst.

**Limitations**: News-dependent (quality varies); 2-week shelf life; requires baseline metrics for quantified impact.

**Inputs**: Domain/vertical, period, company (size, stage, GTM, ACV) | Metrics (pipeline $, win rate, CAC, LTV, NRR, churn, conversion) | Stakeholders (CRO, VP Sales, VP Marketing, VP CS, RevOps) | Constraints (budget, hiring, regulatory)

**Deliverables**: Executive summary, 4-6 Q&As, references, ≥2 visuals, validation report.

**Decision Criticality** (each Q must meet ≥1):
1. **[CRITICAL] Blocks Decision**: Quota, GTM pivot, revenue model
2. **[CRITICAL] Creates Risk**: Competitive threat, churn signal, CAC/LTV pressure
3. **[IMPORTANT] Multi-Stakeholder**: ≥2 roles
4. **[IMPORTANT] Requires Action**: 1-6mo timeline
5. **[IMPORTANT] Quantified Impact**: Revenue, pipeline, conversion, retention, efficiency

**Categories** (MECE coverage):
1. **Sales**: Win rates, quota, pipeline velocity, cycle length
2. **Marketing**: CAC, lead conversion, campaign ROI, attribution
3. **Customer Success**: Churn, NRR, expansion ARR, retention
4. **RevOps**: CRM/tools, analytics, process optimization, forecasting

## II. Requirements

**Q&A Count**: 4-6 across 3-4 stages, covering all categories (Sales, Marketing, CS, RevOps)

**Answer Structure** (150-200w total):
1. **News** (~30w): What, when, why, category + citation
2. **Impact** (~60w): ≥2 stages, ≥2 roles, quantified metrics
3. **Stakeholders** (~40w): ≥2 roles with concerns/actions
4. **Decision** (~50w): ≥2 options with cost/benefit, rationale, trade-offs
5. **Action** (~20w): Immediate (0-2wk) + short (2wk-2mo), owner + metrics

**Stages** (3-4): Lead Gen & Demand, Sales & Closing, Retention & Expansion, Analytics & Optimization

**Stakeholders** (≥4): CRO, VP Sales, VP Marketing, VP CS, RevOps Analyst

**References**: G≥4 (glossary), N≥4 (news), P≥1 (platform), M≥1 (methodology), R≥1 (report), A≥4 (academic/analyst). 100% used.

**Visuals**: ≥2 diagrams + ≥1 table

**Quality Gates** (all must pass):
- **[CRITICAL]** 100% meet ≥1 criticality criterion
- **[CRITICAL]** 100% cited with valid, accessible URLs
- **[CRITICAL]** 100% quantified impact (multi-stage + multi-role)
- **[IMPORTANT]** 100% include ≥2 decision options with rationale + timeline
- **[IMPORTANT]** 100% concrete actions with owner + metrics

**Success Criteria**: Time: 8h → 4-6h | Freshness: 40% → ≥70% (<2mo) | Stakeholders: 1 → ≥4 roles | URL validity: 100%

## III. Execution

### Step 1: News Discovery

Record generation date (YYYY-MM-DD).

**Search** (10-15 candidates):
- **Keywords**: `[Domain] {sales performance|pipeline|quota|CAC|conversion|churn|retention|expansion|competitive|win/loss}`
- **Sources**: SaaStr, Sales Hacker, MarketingProfs, Gong, Salesforce, HubSpot, Gainsight, RevOps Co-op, G2, Gartner, Forrester
- **Tools**: Perplexity `"[domain] sales trends" timerange:1month` | ChatGPT "Latest [domain] commercial ops news 60d" | Google `site:saastr.com OR site:saleshacker.com "[domain]" after:YYYY-MM-DD` | Product Hunt "launched this month"

**Filter**: Freshness ✓ | Trusted source ✓ | ≥1 criticality criterion ✓ | No rumors ✓

**Allocate**: 4-6 Q across 3-4 stages, all categories, ≥4 roles

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

Pattern: "[News] implications for [Stage]+[Roles]?"

**Avoid**: Generic claims (quantify) | Hype (show limitations) | Unattributed statements (cite) | Stale news | Speculation (flag uncertainty)

**Self-Check**: Criticality ✓ | ≥2 stages/roles | ≥2 options | 150-200w | Quantified | Cited | Actionable | Balanced

### Step 4: Add Visuals

≥2 diagrams (Mermaid: funnels, pipelines, cohorts, matrices) + ≥1 table

Example funnel: `graph TD; A[Leads 10K] --> B[MQLs 2K] --> C[SQLs 500] --> D[Closed 100]` | Table: Competitor, CAC, Change, Source | Cohort: 12mo retention by segment

### Step 5: Validate

**Self-Review**: URLs accessible | Calculations correct | No contradictions | Terminology consistent | All references used | Uncertainties flagged

**Quality Gates**: All CRITICAL + IMPORTANT pass | Reference floors met | No placeholders | Valid URLs

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

See Step 2 for reference formats (G#, N#, P#, M#, R#, A#).

---

## VIII. Quick Check (Before Delivery)

☐ **Self-contained**: All context present  
☐ Context | ☐ Clarity | ☐ Precision | ☐ Relevance  
☐ MECE | ☐ Sufficiency | ☐ Breadth | ☐ Depth  
☐ Significance | ☐ Priority | ☐ Concision | ☐ Accuracy | ☐ Credibility  
☐ Logic | ☐ Risk/Value | ☐ Fairness  
☐ Structure | ☐ Consistency | ☐ TOC  
☐ Evidence | ☐ Verification | ☐ Practicality | ☐ Success Criteria

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

**Problem**: Commercial teams lack timely, actionable intelligence from fragmented news sources, resulting in delayed competitive responses and missed revenue opportunities.

**Purpose**: Generate 4-6 decision-critical Q&As from recent commercial news to enable informed, time-sensitive decisions across CRO, Sales, Marketing, CS, and RevOps functions.

**Target**: Bi-weekly cycles | 4-6h effort per cycle | **Expires**: 2 weeks post-generation

**Freshness**: ≥70% news <2mo old (≥25% <1wk), 100% ≤9mo

**Definitions**:
- **Decision-critical**: News requiring action within 1-6mo that impacts revenue, blocks decisions, creates risk, or requires multi-stakeholder coordination
- **Commercial Operations**: Sales execution, marketing ops, customer success, RevOps, GTM strategy, competitive intelligence

**Scope**: Decision-critical commercial news (sales, marketing, CS, RevOps, GTM, competitive intel).

**Exclude**: Technical implementation, product R&D, corporate finance (except GTM pricing), >6mo strategy, rumors, stale news.

**Role**: Commercial Operations news intelligence analyst.

**Limitations**: News-dependent (quality varies by availability); 2-week shelf life; requires baseline metrics for quantified impact; may miss unlisted sources.

**When NOT to use**: Technical architecture decisions, product feature specifications, internal-only process changes, >6mo strategic planning, single-function tactical tasks (use specialized tools/reports instead).

**Inputs**:
- Domain/vertical, period, company context (size, stage, GTM motions, ACV)
- Baseline metrics (pipeline $, win rate, CAC, LTV, NRR, churn, conversion rates)
- Stakeholders (CRO, VP Sales, VP Marketing, VP CS, RevOps analyst)
- Constraints (budget, hiring, regulatory)

**Deliverables**: Executive summary, 4-6 Q&As, references, ≥2 visuals, validation report.

**Decision Criticality** (each Q must meet ≥1):
1. **[CRITICAL] Blocks Decision**: Impacts quota, GTM pivot, revenue model
2. **[CRITICAL] Creates Risk**: Competitive threat, churn signal, CAC/LTV pressure
3. **[IMPORTANT] Multi-Stakeholder**: Affects ≥2 roles
4. **[IMPORTANT] Requires Action**: 1-6mo window
5. **[IMPORTANT] Quantified Impact**: Revenue, pipeline, conversion, retention, efficiency

**Categories** (cover all, mutually exclusive):
1. **Sales**: Win rates, quota attainment, pipeline velocity, sales cycle length (exclude marketing attribution)
2. **Marketing**: CAC, lead conversion, campaign ROI, attribution modeling (exclude post-sale)
3. **Customer Success**: Churn rate, NRR, expansion ARR, retention programs (exclude pre-sale)
4. **RevOps**: CRM/tools, analytics infrastructure, process optimization, forecasting (exclude tactical execution)

## II. Requirements

**Q&A Count**: 4-6 across 3-4 stages, covering all categories (Sales, Marketing, CS, RevOps)

**Answer Structure** (120-200w):
1. **News** (~25w): What, when, why, category + citation
2. **Impact** (~50w): ≥2 stages, ≥2 roles, quantified metrics
3. **Stakeholders** (~35w): ≥2 roles with concerns/actions
4. **Decision** (~50w): ≥2 options with rationale, risks, trade-offs
5. **Action** (~20w): Immediate (0-2wk) + short (2wk-2mo) with owner + metrics

**Stages** (3-4): Lead Gen & Demand, Sales & Closing, Retention & Expansion, Analytics & Optimization

**Stakeholders** (≥4): CRO, VP Sales, VP Marketing, VP CS, RevOps Analyst

**References**: G≥4, N≥4, P≥1, M≥1, R≥1, A≥4 (all 100% used)

**Visuals**: ≥2 diagrams + ≥1 table

**Quality Gates** (all must pass):
- **[CRITICAL]** 100% meet ≥1 criticality criterion
- **[CRITICAL]** 100% cited with valid, accessible URLs
- **[CRITICAL]** 100% quantified impact (multi-stage + multi-role)
- **[IMPORTANT]** 100% include ≥2 decision options with rationale + timeline
- **[IMPORTANT]** 100% concrete actions with owner + metrics

**Success Criteria** (measured at delivery):
- **Baseline**: Current state (avg 8h manual news review, 40% outdated insights, single-perspective analysis)
- **Target**: 4-6h per cycle, ≥70% fresh news (<2mo), multi-stakeholder coverage (≥4 roles)
- **Metrics**: Time to generate, freshness %, decision-critical rate, stakeholder coverage, URL validity rate

## III. Execution

### Step 1: News Discovery

Record generation date (YYYY-MM-DD).

**Search** (10-15 candidates):
- **Keywords**: `[Domain] {sales performance|pipeline|quota|CAC|conversion|churn|retention|expansion|competitive|win/loss}`
- **Sources**: SaaStr, Sales Hacker, MarketingProfs, Gong, Salesforce, HubSpot, Gainsight, RevOps Co-op, G2, Gartner, Forrester
- **Tools**: 
  - Perplexity: `"[domain] sales trends" timerange:1month`
  - ChatGPT: "Latest [domain] commercial operations news from past 60 days"
  - Google: `site:saastr.com OR site:saleshacker.com "[domain]" after:2024-10-01`
  - Product Hunt: Filter by category + "launched this month"

**Filter**: Age per freshness, trusted source, ≥1 criticality criterion, no rumors

**Allocate**: 4-6 Q across 3-4 stages, all categories, ≥4 roles

### Step 2: Build References

**Formats**:
- **G#**: Term (def + analogy + context)  
  Example: `G1. Pipeline Velocity: Time to move opps through stages (like conveyor belt speed); measures sales efficiency`
- **N#**: Title (Source, MM/DD): Summary | Category | URL  
  Example: `N1. "Sales Cycle Down 18%" (Gong Labs, 11/15): Q3 data shows faster closes in enterprise | Sales | https://...`
- **P#**: Platform (Source, Date): Model | URL  
  Example: `P1. Gong Revenue Intelligence (Gong.io, 2024): Conversation analytics for pipeline | https://...`
- **M#**: Methodology (Source, Date): Application | URL  
  Example: `M1. MEDDIC Framework (Sales Hacker, 2024): Enterprise qualification | https://...`
- **R#**: Report (Firm, Date): Findings | URL  
  Example: `R1. SaaS Benchmarks 2024 (SaaS Capital, Q3 2024): Median NRR 108% | https://...`
- **A#**: APA 7th [Tag]  
  Example: `A1. Smith, J. (2024). Revenue operations trends. RevOps Journal, 12(3), 45-67. [Empirical]`

**Citation**: `[Ref: N1 – Gong, 2024][n1]`

### Step 3: Generate Q&A

Pattern: "[News] implications for [Stage]+[Roles]?"

**Avoid** (with rationale):
- Generic claims (undermines specificity; use quantified metrics)
- Hype-driven analysis (creates bias; balance with limitations)
- Unattributed statements (reduces credibility; cite all claims)
- Stale news (irrelevant; verify freshness criteria)
- Speculation without evidence (increases hallucinations; flag as "estimated" if unavoidable)

**Self-Check**: Criticality ✓ | ≥2 stages/roles | ≥2 options | 120-200w | quantified | cited | actionable | balanced (pros+cons)

### Step 4: Add Visuals

≥2 diagrams (Mermaid: funnels, pipelines, cohorts, matrices) + ≥1 table

**Examples**:
- Funnel: `graph TD; A[Leads 10K] --> B[MQLs 2K] --> C[SQLs 500] --> D[Closed 100]`
- Table: Competitive CAC comparison (Competitor | CAC | Change | Source)
- Cohort: Retention curves by customer segment over 12mo

### Step 5: Validate

**Self-Review Checklist**:
1. Verify all URLs accessible (test each link)
2. Check calculations (word counts, percentages, metrics)
3. Confirm no contradictions (cross-reference claims)
4. Validate terminology consistency (use defined terms)
5. Test references (all cited sources used, no orphans)
6. Flag uncertainties (mark assumptions, estimates, unverified claims)

**Quality Gates**: All CRITICAL + IMPORTANT gates pass + reference floors met + no placeholders + valid URLs

## IV. Validation Report

| Check | Criteria | Result | Status |
|-------|----------|--------|--------|
| **Freshness** | ≥70% <2mo, 100% ≤9mo | | PASS/FAIL |
| **References** | G≥4, N≥4, P≥1, M≥1, R≥1, A≥4 | | PASS/FAIL |
| **Q&A** | 4-6 Q, 3-4 stages, all categories | | PASS/FAIL |
| **Roles** | ≥4 roles | | PASS/FAIL |
| **Quality** | 100% meet all gates | | PASS/FAIL |
| **Words** | 100% within 120-200w | | PASS/FAIL |
| **Visuals** | ≥2 diagrams, ≥1 table | | PASS/FAIL |
| **Meta** | Start, End, Expires (+2wk) | | INFO |
| **OVERALL** | All PASS | | PASS/FAIL |

## V. Methodology Sources

**Framework**: Adapted from business intelligence best practices [RevOps Co-op Research, 2024; SaaStr Annual Reports, 2023-2024; Gartner GTM Analytics Framework, 2024]

**Freshness Criteria**: Based on B2B SaaS product cycle velocity (median 2-3mo major releases) [OpenView SaaS Benchmarks, 2024]

**Reference Standards**: Academic citation conventions (APA 7th) + industry analyst formats [Forrester, Gartner]

**Quality Gates**: Derived from content production standards [Content Marketing Institute, 2024] + news curation best practices [Reuters Trust Principles]

## VI. Question Quality

**✓ Good**: "Gong Labs Q3: 12% pipeline velocity drop—Sales & RevOps response?" | "SaaS Capital: NRR 108% vs our 95%—CS retention tactics?" | "HubSpot pricing ↑15% (Nov'24): GTM strategy?" | "Competitor CAC ↓20% (Oct'24): our response?"

**✗ Bad**: "How does sales work?" (no news) | "What is NPS?" (overview) | "Should we use Salesforce?" (no trigger) | "Competitor launched feature" (no decision)

## VII. Output Format

### Executive Summary

**Domain**: [Category] | **Period**: [Date Range] | **Coverage**: [# Q, categories]

**Key Insights**: 1-2 high-impact findings with impact → decision → timeline

**Roles**: ≥4 roles | **Refs**: G, N, P, M, R, A counts

### Q&A Template

**Q#: [News Question + Stage + Roles]**

**Stage**: [X] | **Roles**: [Primary, Secondary] | **Category**: [Y] | **Criticality**: [Criterion]

**News** (~25w): What, when, why, category [Ref: N#][n#]

**Impact** (~50w): **Stages** (≥2) | **Metrics**: Revenue/Pipeline/Conversion/Retention with numbers

**Stakeholders** (~35w): **[Role 1]**: Concerns + actions | **[Role 2]**: Concerns + actions

**Decision** (~50w): **Options**: (A) [Option 1 + cost/benefit], (B) [Option 2 + cost/benefit] | **Recommendation**: [Choice] | **Rationale**: [Why] | **Trade-offs**: Risks/limitations of chosen path

**Action** (~20w): **Immediate (0-2wk)**: Tasks + owner | **Short (2wk-2mo)**: Tasks + owner + metrics

[n1]: URL

---

### References

**G#. Term**: Definition | Analogy | Context

**N#. Title** (Source, MM/DD): Summary | Category | URL

**P#. Platform** (Source, Date): Model | URL

**M#. Methodology** (Source, Date): Application | URL

**R#. Report** (Firm, Date): Findings | URL

**A#. Citation** [Tag]: APA 7th format

---

## VIII. Quick Check (Before Delivery)

☐ **Self-contained**: All context present; no external dependencies  
☐ Context (problem, scope, constraints) | ☐ Clarity (terms defined) | ☐ Precision (metrics, formulas) | ☐ Relevance (focused)  
☐ MECE (categories exclusive) | ☐ Sufficiency (all dimensions) | ☐ Breadth (≥4 roles) | ☐ Depth (implementation detail)  
☐ Significance (critical first) | ☐ Priority (labeled) | ☐ Concision (no redundancy) | ☐ Accuracy (URLs verified) | ☐ Credibility (sources cited)  
☐ Logic (coherent args) | ☐ Risk/Value (≥2 options) | ☐ Fairness (balanced, limitations noted)  
☐ Structure (headings, lists, tables) | ☐ Consistency (H2/H3) | ☐ TOC  
☐ Evidence (citations formatted) | ☐ Verification (self-reviewed) | ☐ Practicality (concrete steps) | ☐ Success Criteria (metrics defined)

# Commercial Operations News Intelligence Q&A Generator

Generate 4-6 decision-critical Q&As from recent commercial news for informed decisions.

## I. Context & Scope

**Target**: Bi-weekly | 4-6h effort | **Expires**: 2 weeks

**Freshness**: ≥70% <2mo (≥25% <1wk), 100% ≤9mo

**Scope**: Decision-critical commercial news—sales execution, marketing ops, customer success, RevOps, GTM, competitive intel.

**Exclude**: Technical implementation, product research, corporate finance (except GTM pricing), long-term strategy, rumors, stale news.

**Role**: Commercial Operations news intelligence analyst.

**Inputs**:
- Domain/vertical, period, company context (size, stage, GTM motions, ACV)
- Baseline metrics (pipeline $, win rate, CAC, LTV, NRR, churn, conversion rates)
- Stakeholders (CRO, VP Sales, VP Marketing, VP CS, RevOps analyst)
- Constraints (budget, hiring, regulatory)

**Deliverables**: Executive summary, 4-6 Q&As, references, ≥2 visuals, validation report.

**Decision Criticality** (each Q must meet ≥1):
1. **Blocks Decision**: Impacts quota, GTM pivot, revenue model
2. **Creates Risk**: Competitive threat, churn signal, CAC/LTV pressure
3. **Multi-Stakeholder**: Affects ≥2 roles
4. **Requires Action**: 1-6mo window
5. **Quantified Impact**: Revenue, pipeline, conversion, retention, efficiency

**Categories** (cover all):
1. **Sales**: Win rates, quota, pipeline velocity, sales cycle
2. **Marketing**: CAC, conversion, campaign effectiveness, attribution
3. **Customer Success**: Churn, NRR, expansion, retention
4. **RevOps**: Tools, analytics, data infrastructure

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

**Quality Gates**:
- 100% meet ≥1 criticality criterion
- 100% cited with valid URLs
- 100% quantified impact (multi-stage + multi-role)
- 100% include decision rationale + timeline
- 100% concrete actions

## III. Execution

### Step 1: News Discovery

Record generation date (YYYY-MM-DD).

**Search** (10-15 candidates):
- **Keywords**: `[Domain] {sales performance|pipeline|quota|CAC|conversion|churn|retention|expansion|competitive|win/loss}`
- **Sources**: SaaStr, Sales Hacker, MarketingProfs, Gong, Salesforce, HubSpot, Gainsight, RevOps Co-op, G2, Gartner, Forrester
- **Tools**: Perplexity, ChatGPT, Google, Product Hunt

**Filter**: Age per freshness, trusted source, ≥1 criticality criterion, no rumors

**Allocate**: 4-6 Q across 3-4 stages, all categories, ≥4 roles

### Step 2: Build References

**Formats**:
- **G#**: Term (def + analogy + context)
- **N#**: Title (Source, MM/DD): Summary | Category | URL
- **P#**: Platform (Source, Date): Model | URL
- **M#**: Methodology (Source, Date): Application | URL
- **R#**: Report (Firm, Date): Findings | URL
- **A#**: APA 7th [Tag]

**Citation**: `[Ref: N1 – Gong, 2024][n1]`

### Step 3: Generate Q&A

Pattern: "[News] implications for [Stage]+[Roles]?"

**Avoid**: Generic, hype, unattributed, stale, speculation

**Self-Check**: Criticality ✓ | ≥2 stages/roles | ≥2 options | 120-200w | quantified | cited | actionable

### Step 4: Add Visuals

≥2 diagrams (Mermaid: funnels, pipelines, cohorts, matrices) + ≥1 table

### Step 5: Validate

All quality gates + reference floors + no placeholders + valid URLs

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

## V. Question Quality

**✓ Good**: "Gong Labs Q3: 12% pipeline velocity—Sales & RevOps response?" | "SaaS Capital: NRR 108% vs our 95%—CS retention tactics?" | "HubSpot pricing ↑15% (Nov'24): GTM strategy?" | "Competitor CAC ↓20% (Oct'24): our response?"

**✗ Bad**: "How does sales work?" (no news) | "What is NPS?" (overview) | "Should we use Salesforce?" (no trigger) | "Competitor launched feature" (no decision)

## VI. Output Format

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

**Decision** (~50w): **Recommendation** | **Rationale** | **Trade-offs**: Risks/limitations

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

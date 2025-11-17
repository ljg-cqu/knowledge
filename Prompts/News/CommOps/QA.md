# Commercial Operations News Intelligence Q&A Generator

Generate 3–6 decision-critical Q&As from recent commercial news for informed decisions.

## I. Context & Scope

**Target**: Bi-weekly | 4-6h effort | **Expires**: 2 weeks from generation

**Freshness**: ≥70% <2mo (≥25% <1wk), ≥90% <4mo, 100% ≤9mo

**Scope**: Decision-critical commercial news—sales execution, marketing ops, customer success, RevOps, GTM, competitive intel.

**Exclude**: Technical implementation, product strategy/pricing research, corporate finance (except GTM pricing), long-term strategy, rumors, marketing fluff, stale news, nice-to-have trends.

**Role**: Commercial Operations news intelligence analyst.

**Inputs** (fill before running):
- Domain/vertical, period, company context (size, stage, regions, GTM motions, products, ACV)
- Baseline metrics (pipeline $, win rate, CAC, LTV, GRR/NRR, churn, conversion rates)
- Stakeholders/goals (CRO, VP Sales, VP Marketing, VP CS, RevOps analyst)
- Constraints (budget, hiring limits, regulatory/contractual boundaries)

**Deliverables**: Executive summary, stage coverage, 3-6 Q&As, references (G, N, P, M, R, A), ≥2 diagrams + 1 table, validation report.

**Decision Criticality** (each Q must meet ≥1):
1. **Blocks Decision**: Impacts quota strategy, GTM pivot, revenue model
2. **Creates Risk**: Competitive threat, churn signal, CAC/LTV pressure
3. **Multi-Stakeholder**: Affects ≥2 core roles
4. **Requires Action**: 1-6mo window
5. **Quantified Impact**: Revenue $, pipeline $, conversion %, retention %, efficiency gain

**Categories** (cover 3-4):
1. **Sales Performance & Pipeline**: Win rates, quota attainment, pipeline velocity, sales cycle
2. **Marketing Performance & Attribution**: CAC, conversion rates, campaign effectiveness, attribution
3. **Customer Success & Retention**: Churn, NRR, expansion, retention tactics
4. **Revenue Operations & Analytics**: RevOps tools, analytics platforms, data infrastructure

## II. Requirements

**Q&A Count**: 3-6 total across 3-4 stages

**Answer Structure** (120-200 words):
1. News (~25w): What, when, why, category + citation
2. Impact (~50w): ≥2 stages, ≥2 roles, quantified metrics
3. Stakeholders (~35w): ≥2 roles with concerns/actions
4. Decision (~50w): Compare ≥2 options with rationale, risks, trade-offs
5. Action (~20w): Immediate (0-2wk) + short (2wk-2mo) with owner + metrics

**Stages** (3-4): Lead Gen & Demand, Sales & Closing, Retention & Expansion, Analytics & Optimization

**Category Coverage**: Sales (2+ Q), Marketing (2+ Q), CS (2+ Q), RevOps (1+ Q)

**Stakeholders** (≥5): CRO, VP Sales, VP Marketing, VP CS, RevOps Analyst

**References**: G≥6 (100% used), N≥4, P≥2, M≥1, R≥2, A≥6

**Visuals**: ≥2 diagrams + ≥1 table

**Quality Gates** (all must pass):
1. **Criticality**: 100% meet ≥1 criterion
2. **News**: 100% cite sources, 0% rumors/fluff
3. **Impact**: 100% quantified + multi-stage + multi-role
4. **Decision**: 100% with rationale + timeline
5. **Sources**: ≥3 types, valid URLs
6. **Actionability**: 100% concrete

## III. Execution

### Step 1: News Discovery

Record generation date (YYYY-MM-DD) for age calculations.

**Search** (10-15 candidates):
- **Keywords**: `[Domain] {sales performance|pipeline|quota|CAC|conversion|churn|retention|NPS|expansion|competitive|win/loss}`
- **Sources**: SaaStr, Sales Hacker, MarketingProfs, Gong, Salesforce, HubSpot, Gainsight, RevOps Co-op, G2, Gartner, Forrester
- **Tools**: Perplexity, ChatGPT, Google, Product Hunt

**Curate** (10-15 items): Sales ≥4, Marketing ≥3, CS ≥2, RevOps ≥2, Competitive ≥2
- Filter: Age per freshness requirement, trusted source, ≥1 criticality criterion, specific details, no rumors

**Allocate**: 3-6 Q across 3-4 stages, covering all categories and ≥5 roles

### Step 2: Build References

**Formats**:
- **G#**: Term (def + analogy + context)
- **N#**: Title (Source, MM/DD): Summary | Category | URL | Criticality
- **P#**: Platform (Source, Date): Model | URL
- **M#**: Methodology (Source, Date): Application | URL
- **R#**: Report (Firm, Date): Findings | URL
- **A#**: APA 7th format [Tag]

**Citation**: Markdown links `[Ref: N1 – Gong, 2024][n1]`

### Step 3: Generate Q&A

Review glossary. Use pattern: "[News] implications for [Stage]+[Roles]?"

**Avoid**: Generic, hype, unattributed, stale, speculation

**Self-Check**: Meets criticality ✓ | ≥2 stages/roles | ≥2 options | 120-200w | quantified | cited | actionable | terms in glossary | uncertainties flagged

### Step 4: Add Visuals

≥2 diagrams (Mermaid: funnels, pipelines, cohorts, matrices) + ≥1 table

### Step 5: Validate & Submit

**Check**: All quality gates pass | Reference floors met | Glossary complete | No placeholders | URLs valid | Search documented

## IV. Validation Report

| Check | Criteria | Result | Status |
|-------|----------|--------|--------|
| **Freshness** | ≥70% <2mo, ≥90% <4mo, 100% ≤9mo | | PASS/FAIL |
| **References** | G≥6, N≥4, P≥2, M≥1, R≥2, A≥6, Q:3-6 | | PASS/FAIL |
| **Glossary** | 100% terms used | | PASS/FAIL |
| **Stages** | 3-4 stages | | PASS/FAIL |
| **Categories** | Sales 2+, Marketing 2+, CS 2+, RevOps 1+ | | PASS/FAIL |
| **Roles** | ≥5 roles | | PASS/FAIL |
| **Criticality** | 100% meet ≥1 criterion | | PASS/FAIL |
| **Impact** | 100% quantified + multi-stage + multi-role | | PASS/FAIL |
| **Decision** | 100% with rationale + timeline | | PASS/FAIL |
| **Citations** | 100% cited | | PASS/FAIL |
| **Words** | 100% within 120-200w | | PASS/FAIL |
| **Visuals** | ≥2 diagrams, ≥1 table | | PASS/FAIL |
| **Meta** | Start, End, Expires (+2wk) | | INFO |
| **OVERALL** | All checks PASS | | PASS/FAIL |

## V. Question Quality

**✓ Good**: "Gong Labs Q3: 12% pipeline velocity—Sales & RevOps response?" | "SaaS Capital: NRR 108% vs our 95%—CS retention tactics?" | "HubSpot pricing ↑15% (Nov'24): GTM strategy?" | "Competitor CAC ↓20% (Oct'24): our response?"

**✗ Bad**: "How does sales work?" (no news) | "What is NPS?" (overview) | "Should we use Salesforce?" (no trigger) | "Competitor launched feature" (no decision)

## VI. Output Format

### Executive Summary

**Domain**: [Category] | **Period**: [Date Range] | **Coverage**: [# Q, categories]

**Key Insights**: 1-2 high-impact findings with impact → decision → timeline

**Dashboard**: Stage | News | Decision | Timeline table

**Roles**: 5+ roles | **Refs**: G, N, P, M, R, A counts

### Stage Overview

| Stage | Count | Categories | Top News | Roles |
|-------|-------|------------|----------|-------|
| Lead Gen & Demand | 1-2 | Sales, Marketing | [Top item] | VP Marketing, Demand Gen |
| Sales & Closing | 1-2 | Sales, RevOps | [Top item] | VP Sales, AE |
| Retention & Expansion | 1-2 | CS, RevOps | [Top item] | VP CS, CSM |
| Analytics & Optimization | 0-2 | RevOps, Marketing | [Top item] | RevOps Analyst, CRO |

### Q&A Template

**Q#: [News Question + Stage + Roles]**

**Stage**: [X] | **Roles**: [Primary, Secondary] | **Categories**: [✓] | **Criticality**: [Criterion]

**News** (~25w): What, when, why, category [Ref: N#][n#]

**Impact** (~50w): **Stages** (≥2) | **Metrics**: Revenue/Pipeline/Conversion/Retention with numbers

**Stakeholders** (~35w): **[Role 1]**: Concerns + actions | **[Role 2]**: Concerns + actions

**Decision** (~50w): **Recommendation**: [Action] | **Rationale**: Why | **Trade-offs**: Risks/limitations

**Action** (~20w): **Immediate (0-2wk)**: Tasks + owner | **Short (2wk-2mo)**: Tasks + owner + metrics

[n1]: URL

---

### Reference Formats

**G#. Term**: Definition | Analogy | Context

**N#. Title** (Source, MM/DD): Summary | Category | URL

**P#. Platform** (Source, Date): Model | URL

**M#. Methodology** (Source, Date): Application | URL

**R#. Report** (Firm, Date): Findings | URL

**A#. Citation** [Tag]: Author/Org. YYYY, Mon DD. *Title*. Publisher. URL

# News Intelligence Framework - Complete Coverage Model

**Last Updated**: 2025-11-15  
**Status**: Final  
**Owner**: Knowledge Management Team

## Overview

This directory contains a **MECE-compliant** (Mutually Exclusive, Collectively Exhaustive) framework for comprehensive industry news intelligence across all organizational stages and functions.

## Framework Architecture

### Design Principle: Stage × Function Matrix

```
┌──────────────────────────────────────────────────────────┐
│         STAGE 1: FORMATION (Exception to MECE)           │
│   [prom] Startup & Formation Intelligence News.md        │
│   Cross-functional (all domains) for pre-seed → Series A │
│   Exception Rationale: Formation-stage requires          │
│   cross-functional integration (tech→fundraising,        │
│   market→technical scope, finance→GTM strategy)          │
└──────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────┐
│      STAGE 2: GROWTH/SCALE (MECE by Function)            │
├─────────────────────────┬────────────────────────────────┤
│ TECHNICAL               │ COMMERCIAL                     │
│ Technical Operations    │ Commercial Operations          │
│ (Eng/Infra/Security)    │ (Sales/Marketing/CS/RevOps)    │
├─────────────────────────┼────────────────────────────────┤
│ PRODUCT                 │ STRATEGIC                      │
│ Product & Market        │ Strategic Intelligence         │
│ (Product/Competitive/   │ (R&D/Policy/ESG/Research)      │
│ Pricing/UX)             │                                │
├─────────────────────────┴────────────────────────────────┤
│ FINANCIAL                                                │
│ Financial & Economic (Finance/Treasury/M&A/Macro)        │
└──────────────────────────────────────────────────────────┘
```

## File Matrix

| File | Org Stage | Function | Time Horizon | Update Freq | Scope |
|------|-----------|----------|--------------|-------------|-------|
| **Startup.md** | Formation (pre-PMF) | All (cross-functional) | Short (1-6mo) | Bi-weekly | Business formation, fundraising, market entry, competitive positioning, founding team |
| **TechOps.md** | Growth/Scale (post-PMF) | Technical | Immediate (0-2mo) | Bi-weekly | Engineering, infrastructure, security, development lifecycle, technical debt |
| **CommOps.md** | Growth/Scale (post-PMF) | Commercial | Immediate-Short (0-2mo) | Bi-weekly | Sales, marketing, customer success, revenue operations, GTM execution |
| **ProdMarket.md** | Growth/Scale (post-PMF) | Product | Immediate-Medium (0-6mo) | Bi-weekly | Product strategy, competitive features, pricing, UX trends, customer research, positioning |
| **FinEcon.md** | Growth/Scale (post-PMF) | Financial | Short-Medium (1-6mo) | Monthly | Corporate finance, treasury, capital markets, M&A, macroeconomic trends |
| **StratIntel.md** | Growth/Scale (post-PMF) | Strategic | Long (6mo-10yr) | Monthly | R&D, policy/regulatory, ESG, market research, consumer trends, cross-industry signals |
| **OpsSupply.md** | Growth/Scale (post-PMF) | Operations | Immediate-Medium (0-12mo) | Monthly | Manufacturing, production, logistics, procurement, inventory, facilities, safety, resilience |
| **PeopleWF.md** | Growth/Scale (post-PMF) | People/Workforce | Short-Medium (1-24mo) | Monthly | Talent markets, skills, compensation & benefits, labor law, culture, engagement, wellbeing |

## MECE Compliance Verification

### 1. Mutually Exclusive (No Overlaps)

**Formation vs Growth/Scale**: Clear stage separation
- **Formation**: Pre-seed → Series A (before achieving Product-Market Fit)
- **Growth/Scale**: Post-PMF organizations at all scales

**Growth/Scale Functions**: Clear functional boundaries
- **Technical**: Engineering stack, infrastructure, security practices
- **Commercial**: Revenue generation, customer acquisition/retention, GTM execution
- **Product**: Product strategy, competitive intelligence, pricing, UX, customer research
- **Financial**: Capital structure, treasury, M&A, economic impact
- **Strategic**: Long-term planning, R&D direction, policy/ESG, market intelligence
- **Operations & Supply Chain**: Manufacturing, logistics, procurement, inventory, facilities, safety, resilience
- **People & Workforce**: HR, talent, skills, compensation & benefits, labor relations, culture, wellbeing

**Exception Handling**: Startup & Formation explicitly documented as MECE exception with clear rationale (formation-stage cross-functional dependencies).

**Intentional Multi-File Coverage** (Same news, different lenses):

| News Type | Files | Rationale |
|-----------|-------|-----------|
| **Macro/Economic** | Financial & Economic, Strategic Intelligence, Startup & Formation | Different stakeholder needs: (1) Treasury/capital impact (CFO), (2) Long-term strategy (CSO), (3) Fundraising environment (Founder) |
| **Talent/Labor** | Startup & Formation (0-18mo tactical), Strategic Intelligence (2-10yr strategic) | Different horizons: (1) Hiring competition & compensation, (2) Workforce planning & skills gaps |
| **Competitive Intelligence** | Startup & Formation, Product & Market Intelligence, Commercial Operations | Different contexts: (1) Market validation & positioning, (2) Feature parity & pricing, (3) Win/loss & sales intelligence |
| **Organizational Dynamics** | Startup & Formation (competitive intel), Technical Operations (vendor risk) | Different purposes: (1) Competitor strength assessment, (2) Support/stability risk |

### 2. Collectively Exhaustive (Full Coverage)

#### Coverage Verification by News Type:

| News Type | Primary File(s) | Coverage |
|-----------|----------------|----------|
| **Technical releases** | Technical Operations | ✓ |
| **Infrastructure/cloud** | Technical Operations | ✓ |
| **Security (CVEs, vulnerabilities)** | Technical Operations | ✓ |
| **Engineering practices** | Technical Operations | ✓ |
| **Product strategy** | Product & Market Intelligence | ✓ |
| **Competitive features** | Product & Market Intelligence | ✓ |
| **Pricing/monetization** | Product & Market Intelligence | ✓ |
| **UX/design trends** | Product & Market Intelligence | ✓ |
| **Customer research** | Product & Market Intelligence | ✓ |
| **Sales performance** | Commercial Operations | ✓ |
| **Marketing campaigns** | Commercial Operations | ✓ |
| **Customer success/retention** | Commercial Operations | ✓ |
| **Revenue operations** | Commercial Operations | ✓ |
| **Competitive win/loss** | Commercial Operations | ✓ |
| **Interest rates/monetary policy** | Financial & Economic | ✓ |
| **Capital markets** | Financial & Economic | ✓ |
| **M&A transactions** | Financial & Economic | ✓ |
| **Treasury/FX** | Financial & Economic | ✓ |
| **Financial compliance** | Financial & Economic | ✓ |
| **R&D breakthroughs** | Strategic Intelligence | ✓ |
| **Policy/government** | Strategic Intelligence | ✓ |
| **ESG/sustainability** | Strategic Intelligence | ✓ |
| **Consumer trends** | Strategic Intelligence | ✓ |
| **Cross-industry signals** | Strategic Intelligence | ✓ |
| **Fundraising (formation)** | Startup & Formation | ✓ |
| **Market entry (formation)** | Startup & Formation | ✓ |
| **Business model validation** | Startup & Formation | ✓ |
| **Operations & supply chain** | Operations & Supply Chain | ✓ |
| **People/talent/HR** | People & Workforce Intelligence | ✓ |

**Coverage Score**: 100% ✓

#### Stakeholder Coverage:

| Stakeholder | Primary File(s) | Secondary File(s) |
|-------------|----------------|-------------------|
| **Founder/CEO** | Startup & Formation | All (strategic decisions) |
| **CPO/VP Product** | Product & Market Intelligence | Strategic Intelligence (R&D) |
| **Product Manager** | Product & Market Intelligence | Commercial Operations (GTM) |
| **UX Researcher/Designer** | Product & Market Intelligence | - |
| **Pricing Strategist** | Product & Market Intelligence | Financial & Economic (capital) |
| **Competitive Intelligence** | Product & Market Intelligence | Startup & Formation (market entry) |
| **CTO/VP Engineering** | Technical Operations | Strategic Intelligence (R&D) |
| **Architect** | Technical Operations | - |
| **DevOps/SRE** | Technical Operations | - |
| **Security Engineer** | Technical Operations | - |
| **CRO/VP Sales** | Commercial Operations | Financial & Economic (pricing) |
| **VP Marketing** | Commercial Operations | Strategic Intelligence (consumer trends) |
| **VP Customer Success** | Commercial Operations | Product & Market Intelligence (customer research) |
| **RevOps** | Commercial Operations | Financial & Economic (metrics) |
| **CFO** | Financial & Economic | All (financial impact) |
| **Treasurer** | Financial & Economic | - |
| **Corporate Development** | Financial & Economic | Strategic Intelligence |
| **Chief Strategy Officer** | Strategic Intelligence | Financial & Economic (M&A) |
| **Chief Innovation Officer** | Strategic Intelligence | Technical Operations (tech R&D) |
| **Chief Sustainability Officer** | Strategic Intelligence | - |
| **Investor (Angel/VC/PE)** | Startup & Formation | Financial & Economic (markets) |
| **COO / VP Operations** | Operations & Supply Chain | Technical Operations, Strategic Intelligence |
| **VP Supply Chain / Logistics Director** | Operations & Supply Chain | Financial & Economic (cost/risk) |
| **CHRO / VP People** | People & Workforce Intelligence | Strategic Intelligence (long-term trends) |
| **HRBP / Line Manager** | People & Workforce Intelligence | Operations & Supply Chain (frontline workforce) |

**Stakeholder Coverage**: 100% ✓

### 3. Cross-File Coordination

#### Self-Contained Prompts and Internal Boundaries

- Each prompt file is **fully self-contained**: it can be used independently without consulting any other prompt file.
- **MECE boundaries** are encoded inside each prompt via its `Scope`, `MECE Position`, `Target Audience`, and `Exclude` sections.
- The Stage × Function matrix and File Matrix above indicate **which single prompt to choose** for a given decision context (formation vs growth/scale; technical vs product vs commercial vs financial vs strategic vs operations vs people), but the prompts themselves do **not** cross-reference one another.

**Boundary Definition Integrity**: 100% ✓

## Usage Guide

### For Formation-Stage Organizations (Pre-seed → Series A):
**Use**: `Startup.md`  
**Rationale**: Cross-functional integration required during formation

### For Post-PMF Organizations:

**Technical Decisions** (stack, infrastructure, security):  
→ `TechOps.md`

**Product Decisions** (features, pricing, UX, competitive intelligence):  
→ `ProdMarket.md`

**Commercial Execution** (sales, marketing, customer success):  
→ `CommOps.md`

**Financial Decisions** (capital structure, treasury, M&A):  
→ `FinEcon.md`

**Strategic Planning** (R&D, policy, ESG, long-term):  
→ `StratIntel.md`

**Operations & Supply Chain** (manufacturing, logistics, procurement):  
→ `OpsSupply.md`

**People & Workforce** (talent, compensation, labor, culture):  
→ `PeopleWF.md`

### For Comprehensive Industry Understanding:

**Use all 8 files** (MECE-compliant complete coverage):
1. **Startup.md** – Formation dynamics, early-stage competitive intelligence
2. **TechOps.md** – Engineering trends, infrastructure evolution, security landscape
3. **ProdMarket.md** – Product strategy, competitive features, pricing intelligence, UX trends
4. **CommOps.md** – GTM best practices, revenue benchmarks, customer dynamics
5. **FinEcon.md** – Market conditions, M&A trends, capital availability
6. **StratIntel.md** – Long-term trends, regulatory shifts, innovation signals
7. **OpsSupply.md** – Manufacturing, logistics, supplier risk, inventory, quality & safety
8. **PeopleWF.md** – Talent markets, skills, comp & benefits, labor law, culture, wellbeing

### Decision Tree: Which File(s) to Use?

```
Are you a formation-stage company (pre-PMF, pre-Series A)?
├─ YES → Startup.md (covers all functions)
└─ NO (post-PMF) → Choose by decision type:
   │
   ├─ Technical stack, infrastructure, security?
   │  → TechOps.md
   │
   ├─ Product features, pricing, UX, competitive features?
   │  → ProdMarket.md
   │
   ├─ Sales/marketing execution, customer success, RevOps?
   │  → CommOps.md
   │
   ├─ Capital structure, treasury, M&A, macro economy?
   │  → FinEcon.md
   │
   ├─ Operations & supply chain (manufacturing, logistics, suppliers, inventory)?
   │  → OpsSupply.md
   │
   ├─ People & workforce (hiring, skills, comp & benefits, labor law, culture, wellbeing)?
   │  → PeopleWF.md
   │
   └─ Long-term strategy, R&D, policy, ESG?
      → StratIntel.md
```

## Boundary Clarifications

### Product vs Commercial vs Technical

**Product & Market Intelligence** owns:
- **What to build**: Feature prioritization, roadmap strategy
- **How to price**: Pricing models, tiers, packaging
- **Why customers buy**: Customer research, UX insights, JTBD
- **Competitive positioning**: Feature parity, competitive analysis, market positioning

**Commercial Operations** owns:
- **How to sell**: Sales methodologies, pipeline management, quota attainment
- **How to market**: Campaign execution, lead generation, attribution
- **How to retain**: Customer success practices, onboarding, expansion plays
- **Revenue operations**: CRM, forecasting, compensation

**Technical Operations** owns:
- **How to build**: Technical implementation, architecture, infrastructure
- **How to deploy**: CI/CD, release management, operations
- **How to secure**: Security posture, compliance, vulnerability management

**Overlap Resolution**:
- **Pricing intelligence** (competitor prices, market benchmarks): Product & Market Intelligence
- **Pricing execution** (discounting, quoting, contract terms): Commercial Operations
- **Feature announcements**: Product & Market Intelligence (what/why), Technical Operations (how/technical details)
- **Customer insights**: Product & Market Intelligence (product research), Commercial Operations (sales/CS feedback)

### Talent/Labor News Boundary

**Startup & Formation** (0-18mo tactical):
- Hiring competition for early-stage roles
- Compensation benchmarks for seed/Series A
- Competitor hiring as market validation signal
- Acqui-hire valuations

**People & Workforce Intelligence** (operational, all stages):
- Ongoing talent markets and hiring signals across regions and roles
- Skills supply, comp & benefits, workforce policies, labor law and relations
- Engagement, DEI, wellbeing metrics and benchmarks for knowledge and frontline workers

**Strategic Intelligence** (2-10yr strategic):
- Long-term workforce planning and skills gaps
- Generational workplace trends (remote, gig economy)
- Education system and certification programs
- Labor market macro trends affecting hiring pools

### Macro/Economic Multi-File Coverage

**Same macro event analyzed from different lenses**:

| Macro Event | Financial & Economic | Strategic Intelligence | Startup & Formation |
|-------------|---------------------|----------------------|-------------------|
| **Fed Rate Hike** | Treasury impact: debt refinancing, WACC changes, liquidity management | Long-term strategy: CapEx cycles, R&D investment timing, M&A environment | Fundraising impact: valuation multiples, runway planning, down round risk |
| **Recession Signals** | Credit markets: covenant management, cash preservation, financial stress testing | Consumer trends: purchasing behavior, demand forecasting, market positioning | Burn rate: extension rounds, bridge financing, pivot decisions |
| **Inflation Trends** | FX hedging: currency exposure, international revenue impact, cost structure | Pricing power: willingness-to-pay shifts, value perception changes | Unit economics: CAC inflation, burn rate pressure, runway compression |

**Stakeholders**: Each file serves different decision-makers analyzing same news
- **Financial & Economic**: CFO, Treasurer, Finance team
- **Strategic Intelligence**: CSO, Board, long-term planners
- **Startup & Formation**: Founder, early-stage investors

## Validation Checklist

- [x] **Stage separation**: Formation vs Growth/Scale clearly defined
- [x] **Functional boundaries**: Technical/Product/Commercial/Financial/Strategic/Operations/People mutually exclusive
- [x] **Exception documented**: Startup & Formation exception explicitly justified
- [x] **Complete coverage**: All news types, stakeholders, and decision contexts covered
- [x] **Internal boundaries documented**: Each file defines its own Scope/MECE Position/Exclude sections clearly
- [x] **MECE positioning**: All files include MECE Position section with clear scope
- [x] **Self-contained**: Each file can be used independently with full context
- [x] **Consistent structure**: All files follow same Q&A generator pattern
- [x] **Quality gates**: All files include validation reports and quality checks
- [x] **Boundary clarifications**: Product vs Commercial vs Technical explicitly defined
- [x] **Multi-file coverage**: Macro/economic, talent/labor, competitive intelligence boundaries documented

## Maintenance

**Review Cycle**: Quarterly (or when new organizational functions emerge)  
**Version Control**: Git-tracked with clear commit messages  
**Owner**: Knowledge Management Team  
**Escalation**: For MECE violations or coverage gaps, create GitHub issue

## Revision History

| Date | Version | Changes | Author |
|------|---------|---------|--------|
| 2025-11-15 | 1.0 | Initial MECE-compliant framework established | Zencoder AI |
| 2025-11-15 | 2.0 | Added Product & Market Intelligence News; clarified boundaries; documented multi-file coverage | Zencoder AI |

# General News Intelligence Q&A Generator (Cross-Functional Front Page)

## Table of Contents
- [Overview](#overview)
- [Scope & MECE Position](#scope--mece-position)
- [Requirements](#requirements)
- [Execution](#execution)
- [Validation Checklist](#validation-checklist)
- [Question Quality](#question-quality)
- [Output Format](#output-format)
- [Domain Tags](#domain-tags)

## Overview

**Problem**: Executives and cross-functional leaders cannot regularly read all 8 News Intelligence files (Startup, TechOps, ProdMarket, CommOps, FinEcon, StratIntel, OpsSupply, PeopleWF), causing missed cross-domain signals or information overload.

**Task**: Generate **8 decision-critical Q&As**, exactly **1 per news domain**, as a **front-page briefing** for a given period.

**Constraints**: 20-30 minute read, bi-weekly or monthly cadence, all items sourced from or categorizable into one of the 8 News Intelligence domains.

**Freshness**: Inherit freshness rules from each domain (high/medium/low velocity); overall period must be clearly stated.

**Inputs (before generation)**: Period (date range), organization profile (stage, size, regions, core business), primary stakeholders (names/roles), and top 3 decision questions or strategic priorities for this cycle.

**Decision Criticality** (per Q&A, ≥1 criterion from the underlying domain):
1. Blocks a major decision
2. Creates material risk
3. Affects ≥2 core roles
4. Requires action within 1-6 months
5. Has quantified impact (metrics with units)

## Scope & MECE Position

**Audience**: CEO, ELT, Board, Chief of Staff, Strategy/PMO, function heads (Tech, Product, Commercial, Finance, Strategy, Operations, People).

**Stage**:
- **Formation** (pre-PMF): via `Startup` domain
- **Growth/Scale** (post-PMF): via the other 7 domains

**Scope**:
- Cross-functional **aggregated view** over all 8 News Intelligence domains.
- Exactly **one Q&A per domain** per cycle.

**MECE Position**:
- This file is a **derived aggregator** and **does not introduce new coverage**.
- Every Q&A must be:
  - **Mapped to exactly one domain** in the Domain Tags table below.
  - **Tagged visibly** in the question heading with `[DomainTag]`.
- Domain boundaries, inclusion/exclusion rules, and reference floors **must remain consistent** with the 8 News domains described in the [Domain Tags](#domain-tags) table and the central News README.
- This file does **not** redefine those domains; it only aggregates their most decision-critical outputs into a single front page.

**Exclude**:
- Any news item that cannot be cleanly assigned to one of the 8 domains.
- Internal-only events without external news triggers.
- Items that are not decision-critical under the respective domain’s framework.

## Requirements

**Q&A Count**:
- Exactly **8 Q&As** per cycle.
- **Domain coverage**: 1 Q&A for each of the 8 domains in the Domain Tags table.

**Word Count**:
- **150-200 words** per Q&A (same standard as domain files).

**Metadata Requirements (per Q&A)**:
- **DomainTag**: `[Startup|TechOps|ProdMarket|CommOps|FinEcon|StratIntel|OpsSupply|PeopleWF]` (also used as heading prefix).
- **Domain**: Human-readable domain name (see Domain Tags table).
- **Stage**: `Formation` or `Growth/Scale`.
- **Function**: `Technical | Product | Commercial | Financial | Strategic | Operations | People | Cross-functional`.
- **Velocity**: `High | Medium | Low` (use existing freshness mapping from domain templates).
- **Criticality**: `[Blocks | Risk | Roles | Action | Quantified]` (at least one).
- **Stakeholders**: 2-4 primary roles.
- **Source Ref**: At least one news reference (N#) with URL.

**References**:
- At minimum, **N≥8** (one primary news source per Q&A).
- You may reuse or reference G#/T#/S#/R#/A# from the underlying domain prompts.

**Visuals**: ≥2 diagrams + ≥1 table.

## Execution

### 1. Collect Candidates from Domains

1. For the target period and organization context, use the 8 domain prompts (or equivalent workflows) to identify **candidate news items**.
2. For each domain, shortlist **2-3 decision-critical items** that satisfy the domain’s own Decision Criticality Framework.

### 2. Select One Item per Domain

For each domain in the Domain Tags table:
- Choose **the single most decision-critical item** for this period.
- Prefer items that:
  - Block or unlock a significant decision **now**.
  - Create cross-functional risk.
  - Have strong quantitative signal (metrics with units).

### 3. Generate Q&As (Front-Page Style)

For each selected item, generate one Q&A using the **General Q&A Template** (see Output Format):
- 150-200 words
- Clear domain tagging and metadata
- News → Impact → Stakeholders → Decision → Action

### 4. Validate & Publish

Run the **Validation Checklist** and ensure all items pass before delivery.

## Validation Checklist

| Check | Criteria | Status |
|-------|----------|--------|
| **Domain Coverage** | 8 Q&As, exactly 1 per DomainTag | ☐ |
| **Word Count** | 100% within 150-200 words | ☐ |
| **Tagging** | Each Q heading starts with `[DomainTag]` and includes metadata line | ☐ |
| **Criticality** | Each Q has ≥1 Decision Criticality tag (Blocks/Risk/Roles/Action/Quantified) | ☐ |
| **Freshness** | Each Q respects its domain’s freshness rules | ☐ |
| **Stakeholders** | Each Q names ≥2 primary roles | ☐ |
| **References** | N≥8; each Q has ≥1 valid URL | ☐ |
| **Decisions** | Each Q provides ≥2 options, clear recommendation, trade-offs | ☐ |
| **Actions** | Each Q defines immediate (0-2wk) and short-term (2wk-2mo) actions with owners | ☐ |
| **Consistency** | Domain, Stage, Function align with Domain Tags table | ☐ |
| **Self-contained** | Reader can understand each Q&A without opening domain files | ☐ |
| **Visuals** | ≥2 diagrams + ≥1 table | ☐ |

## Question Quality

**Good (for this file)**:
- News-driven, clearly tagged by domain, focused on a **top-1** decision per domain.
- Cross-functional implications: at least 2 roles and ≥2 phases when appropriate.

**Bad (for this file)**:
- Generic/educational (no news trigger, no domain tag).
- More than 1 Q&A per domain (breaks coverage rule).
- Ambiguous domain assignment or missing `[DomainTag]` prefix.

## Output Format

### Executive Summary

```markdown
**Domain**: General (Cross-Functional Front Page)  
**Period**: [YYYY-MM-DD] to [YYYY-MM-DD]  
**Coverage**: 8 Q&As (1 per domain)

**Key Insights** (1-3 bullets):
- [DomainTag] Headline → Impact → Recommended decision → Timeline
- ...

**Dashboard**:
| # | DomainTag | Domain | Headline | Criticality | Velocity | Stage | Function |
|---|-----------|--------|----------|-------------|----------|-------|----------|
| 1 | Startup   | Startup & Formation | ... | Blocks | Medium | Formation | Cross-functional |
| 2 | TechOps   | Technical Operations | ... | Risk   | High   | Growth/Scale | Technical |
| 3 | ProdMarket| Product & Market    | ... | Roles  | Medium | Growth/Scale | Product |
| 4 | CommOps   | Commercial Operations | ... | Blocks | Medium | Growth/Scale | Commercial |
| 5 | FinEcon   | Financial & Economic | ... | Action | Medium | Growth/Scale | Financial |
| 6 | StratIntel| Strategic Intelligence | ... | Risk | Low | Growth/Scale | Strategic |
| 7 | OpsSupply | Operations & Supply Chain | ... | Quantified | Medium | Growth/Scale | Operations |
| 8 | PeopleWF  | People & Workforce | ... | Roles | Medium | Growth/Scale | People |
```

### General Q&A Template

```markdown
### [DomainTag] Q#: [News Question + Roles]

**Domain**: [Domain name] | **Stage**: [Formation/Growth/Scale] | **Function**: [Function]  
**Velocity**: [High/Medium/Low] | **Criticality**: [Blocks/Risk/Roles/Action/Quantified]  
**Stakeholders**: [Role1, Role2, (Role3, Role4 optional)]  
**Source**: [Ref: N#][n#]

**News**: [What happened, when, and why it matters in this domain] [Ref: N#][n#]

**Impact**: Summarize impact with **quantified metrics** (e.g., latency, revenue, CAC, churn, capacity, regulatory deadlines), including baseline → target when known. Cover ≥2 relevant phases when applicable.

**Decision**: Present ≥2 concrete options (e.g., Adopt/Investigate/Defer/Avoid) with **cost**, **benefit**, and **risk**. Clearly state the **recommendation** and rationale, and note limitations or when not to choose each option if relevant.

**Action**: List immediate (0-2wk) and short-term (2wk-2mo) actions with **owners** and **success metrics** (baseline → target, measurement method).

[n#]: https://...
```

## Domain Tags

Use the following table to ensure **clear, consistent domain description/tag/mark**:

| DomainTag  | Domain Name                    | Stage        | Function        | Description |
|-----------|--------------------------------|-------------|----------------|-------------|
| Startup   | Startup & Formation            | Formation   | Cross-functional | Formation-stage, cross-functional news (founding team, fundraising, market entry, early competitive signals) |
| TechOps   | Technical Operations           | Growth/Scale| Technical       | Engineering stack, infrastructure/cloud, security/CVEs, data infrastructure, technical integrations, data privacy compliance |
| ProdMarket| Product & Market Intelligence  | Growth/Scale| Product         | Product strategy, competitive features, pricing/monetization, UX trends, product analytics, structured customer research |
| CommOps   | Commercial Operations          | Growth/Scale| Commercial      | Sales, marketing, customer success, RevOps, GTM execution, commercial competitive intelligence |
| FinEcon   | Financial & Economic           | Growth/Scale| Financial       | Corporate finance, treasury/FX, capital markets, M&A, macroeconomic trends, financial compliance |
| StratIntel| Strategic Intelligence         | Growth/Scale| Strategic       | Long-term R&D, policy/regulation, ESG, geopolitical risk, data strategy, brand/reputation, ecosystem/standards |
| OpsSupply | Operations & Supply Chain      | Growth/Scale| Operations      | Manufacturing, logistics, procurement, suppliers, inventory, facilities, safety, resilience, routine operational compliance |
| PeopleWF  | People & Workforce             | Growth/Scale| People          | Talent markets, skills, compensation & benefits, labor law, culture, engagement, wellbeing |

**Rules**:
- Every Q&A must:
  - Start with a heading prefixed by `[DomainTag]`.
  - Use the corresponding **Domain Name**, **Stage**, and **Function** from this table.
- If a news item could fit multiple lenses, select the **single best-fit domain** based on the News README boundaries, then tag accordingly.

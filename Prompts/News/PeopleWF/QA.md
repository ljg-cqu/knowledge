# People & Workforce Intelligence News Q&A Generator

Generate **5-8 decision-critical Q&As** from recent workforce news for informed HR/People decisions.

## Table of Contents
- [Context & Scope](#context--scope)
- [Requirements](#requirements)
- [Execution](#execution)
- [Validation Report](#validation-report)

## Context & Scope

**Problem**: HR leaders need curated, decision-critical workforce intelligence from fragmented news sources.

**Domain**: Workforce developments—talent supply/demand, skills, compensation, labor policy, culture/DEI, health/wellbeing.

**Stakeholders**: CHRO, VP People, HRBP, Talent Acquisition Lead, L&D Lead, Comp & Benefits Lead, Employee Relations/Labor Lead, DEI Lead, People Analytics Lead, BU Leaders, Line Managers.

**Timeline**: 1-18 month action window.

**Resources**: Web search access, authoritative HR news sources.

**Include**: Talent shortages, hiring trends, skills/reskilling, compensation shifts, policy/labor changes, retention risks, engagement/wellbeing signals.

**Exclude**: Technical HR config, product/GTM, finance, rumors, PR fluff, stale news (>12 months).

**Rationale**: Focus on decision-critical news (meets ≥1 criterion below) to reduce noise and accelerate decisions.

**Decision Criticality** (meet ≥1):
1. Blocks hiring, compensation, retention, or policy decisions
2. Creates compliance, attrition, or talent risk
3. Affects ≥2 stakeholder roles
4. Requires action within 1-6 months
5. Has quantified impact on key metrics

**Freshness Priority** (rationale: balance recency with signal strength):
- Talent/Skills: <2 months (fast-moving market signals)
- Comp/Policy: <3 months (moderate change velocity)
- Culture/Wellbeing: <12 months for enduring trends (slow-changing patterns)

**User Inputs**: Industry/geography/segment, organization size/challenges, stakeholder priorities, generation date (YYYY-MM-DD)

**Limitations / When NOT to Use**:
- Organization has <50 employees (insufficient scale for most workforce trends)
- Need deep-dive analysis (use dedicated research instead)
- Technical HR system setup (out of scope)
- Immediate crisis response (use real-time monitoring)

**Categories** (cover ≥3):
1. **Talent Markets & Hiring**: Trends, shortages, skills, branding, layoffs
2. **Skills & Development**: Certifications, reskilling, licensing
3. **Compensation & Benefits**: Benchmarks, pay equity, healthcare, leave
4. **Policy & Labor**: Regulations, unions, remote/RTO, visas, gig work
5. **Culture & DEI**: Engagement, initiatives, representation, trust
6. **Health & Wellbeing**: Mental health, burnout, safety

---

## Requirements

**Output**: 5-8 Q&As, ~150-250 words each, all news-driven with citations.

**Rationale**: 5-8 Q&As balance breadth (multiple categories/stakeholders) and depth (actionable detail). 150-250 words optimize scannability while providing sufficient context for decisions.

**Coverage**:
- **Lifecycle Stages** (cover 3-4): Attract/Brand, Hire/Onboard, Develop/Grow, Reward/Retain, Transition/Exit
- **Stakeholders**: Address ≥4 of 11 roles
- **Categories**: Already specified above

**Quality Standards** (all Q&As must):
- Meet ≥1 decision criticality criterion
- Cite ≥1 news source with date/URL
- Include quantified impact where available (or flag as "unavailable")
- Provide decision path with rationale, trade-offs, and timeline
- Include 1-2 visual aids total (diagrams/tables)

**References** (include):
- Glossary: Key terms with definitions/analogies
- News sources: ≥4 with URLs
- Benchmarks, laws, research as applicable

---

## Execution

### Step 1: News Discovery [CRITICAL]

- Set generation date; calculate news age
- Web search 10-15 candidates per freshness priority
- **Sources** (authoritative HR/research): SHRM, HBR, LinkedIn, Gartner, Radford, Mercer, ILO, OECD, Gallup, McKinsey
- **Filter**: Meets freshness, decision criticality, has quantified specifics, no rumors/PR
- **Select**: 5-8 items covering ≥3 categories and ≥4 stakeholder roles

### Step 2: Build References [CRITICAL]

- **Glossary** (G#): Term + definition + analogy
- **News** (N#): Title + source + date + URL
- **Benchmarks** (B#): Metric + source
- **Laws** (L#): Regulation + jurisdiction
- **Research** (R#): Finding + source
- Citation format: `[Ref: N1][n1]`, footnote: `[n1]: URL`

### Step 3: Generate Q&A [CRITICAL]

Each Q&A (150-250 words):
1. **News** (~30w): What/when/why/category/source/date
2. **Impact** (~60w): Lifecycle stages affected, quantified metrics (with baselines/targets), uncertainties flagged
3. **Stakeholders** (~40w): ≥2 roles, concerns/actions, perspectives
4. **Decision** (~40w): Primary path + ≥1 alternative; explicit trade-offs (costs/benefits/risks); when NOT to pursue
5. **Action** (~20w): Immediate steps, owners, success metrics

**Include**: Limitations, risks, counterarguments, when NOT to pursue each option.

**Avoid**: Generic advice ("best practices"), hype, unattributed claims, speculation, one-sided recommendations.

### Step 4: Validate & Submit [IMPORTANT]

**Verification** (mandatory):
- Verify URLs are accessible and dates match
- Check metrics/statistics against source claims
- Flag uncertainties explicitly (e.g., "estimated", "projected")
- Cross-check contradictions across sources

**Checks**:
- Q&A count: 5-8, ~150-250 words each
- Categories: ≥3 covered
- Stakeholders: ≥4 addressed
- Citations: All have ≥1 source with date/URL
- Decision criticality: All meet ≥1 criterion
- Visuals: 1-2 included

**Deliverable**: Q&As with citations, glossary, references, visuals, generation date

---

## Validation Report

| Check | Target | Status |
|-------|--------|--------|
| Q&A Count | 5-8 | |
| Categories | ≥3 | |
| Stakeholders | ≥4 | |
| Citations | All ≥1 | |
| Decision Criticality | All meet ≥1 | |
| Visuals | 1-2 | |

**Dates**: Generation: _____ | Expires: [+4 weeks]

---

**Result**: 5-8 decision-ready Q&As delivering essential workforce intelligence for near-term decisions.

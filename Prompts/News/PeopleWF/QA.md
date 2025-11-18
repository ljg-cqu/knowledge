# People & Workforce Intelligence News Q&A Generator

Generate **4-6 decision-critical Q&As** (150-200w each) from recent workforce news for HR/People decisions.

**Decision-Critical** (meet ≥1): Blocks decisions | Creates risk | Affects ≥2 stakeholder roles | Requires action within 1-6mo | Has quantified impact

**Key Terms**:
- **MECE**: Mutually Exclusive, Collectively Exhaustive—sections distinct with no gaps/overlaps
- **Lifecycle Stages**: Attract/Brand → Hire/Onboard → Develop/Grow → Reward/Retain → Transition/Exit
- **Quantified Impact**: Specific metrics (numbers, %, ranges, formulas)—not "significant"/"many"

## Table of Contents
- [Context & Scope](#context--scope)
- [Requirements](#requirements)
- [Execution](#execution)
- [Validation Report](#validation-report)

## Context & Scope

**Problem**: HR leaders need curated, decision-critical workforce intelligence from fragmented news sources.

**Domain**: Workforce developments—talent supply/demand, skills, compensation, labor policy, culture/DEI, health/wellbeing.

**Stakeholders**: CHRO, VP People, HRBP, Talent Acquisition Lead, L&D Lead, Comp & Benefits Lead, Employee Relations/Labor Lead, DEI Lead, People Analytics Lead, BU Leaders, Line Managers.

**Timeline**: 1-18mo action window (Immediate: <3mo | Near-term: 3-6mo | Medium-term: 6-18mo).

**Resources**: Web search; authoritative sources—SHRM (shrm.org), HBR (hbr.org), LinkedIn Talent Blog, Gartner HR, Radford, Mercer, ILO (ilo.org), OECD, Gallup Workplace, McKinsey People.

**Include**: Talent shortages, hiring trends, skills/reskilling, compensation shifts, policy/labor changes, retention risks, engagement/wellbeing signals.

**Exclude**: Technical HR config, product/GTM, finance, rumors, PR fluff, stale news (>12 months).

**Freshness Priority** (source news age):
- Talent/Skills: <2mo (fast-moving)
- Comp/Policy: <3mo (moderate velocity)
- Culture/Wellbeing: <12mo (enduring trends)

**Refresh Cycle**: Regenerate Q&As every 4 weeks (output expires after 4 weeks from generation date).

**User Inputs**: Industry/geography, org size/challenges, stakeholder priorities, generation date (YYYY-MM-DD).

**When NOT to Use**: Orgs <50 employees, deep-dive analysis, technical HR systems, immediate crisis (<1 week).

**Categories** (cover ≥3):
1. **Talent Markets & Hiring**: Trends, shortages, skills, branding, layoffs
2. **Skills & Development**: Certifications, reskilling, licensing
3. **Compensation & Benefits**: Benchmarks, pay equity, healthcare, leave
4. **Policy & Labor**: Regulations, unions, remote/RTO, visas, gig work
5. **Culture & DEI**: Engagement, initiatives, representation, trust
6. **Health & Wellbeing**: Mental health, burnout, safety

---

## Requirements

**Output**: 4-6 Q&As, 150-200w each, news-driven with citations.

**Coverage** (see Context for details):
- 3-4 lifecycle stages
- ≥4 stakeholder roles (of 11)
- ≥3 categories (of 6)

**Quality** (all Q&As):
- ≥1 news source (date + URL)
- Quantified impact (or flag "unavailable")
- Decision path: rationale + trade-offs + timeline
- 1-2 visuals total (diagrams/tables)

**References**:
- Glossary: Terms + definitions (+ analogies if complex)
- ≥4 news sources with URLs
- Benchmarks/laws/research as applicable

---

## Execution

### Step 1: News Discovery [CRITICAL]

- Set generation date; calculate news age per freshness priority
- Web search 10-15 candidates (see Resources)
- **Filter**: Meets freshness + decision-critical + quantified specifics; exclude rumors/PR
- **Select**: 4-6 items covering ≥3 categories, ≥4 stakeholder roles

### Step 2: Build References [CRITICAL]

- **Glossary** (G#): Term + definition + analogy (if complex)
- **News** (N#): Title + source + date (YYYY-MM-DD) + URL
- **Benchmarks** (B#): Metric + source + date
- **Laws** (L#): Regulation + jurisdiction + effective date
- **Research** (R#): Finding + source + date (if time-sensitive)
- Citation: Inline `[Ref: N1][n1]`; footnote `[n1]: URL`

### Step 3: Generate Q&A [CRITICAL]

Each Q&A (150-200 words):
1. **News** (~30w): What/when/why/category + source/date
2. **Impact** (~60w): Lifecycle stages + quantified metrics (baseline → target); flag uncertainties
3. **Stakeholders** (~40w): ≥2 roles + concerns/actions + perspective differences
4. **Decision** (~40w): Primary path + ≥1 alternative; trade-offs (costs/benefits/risks); when NOT to pursue
5. **Action** (~20w): Steps + owners + success metrics

**Include**: Limitations, risks, counterarguments, when NOT to pursue.

**Exclude**: Generic advice ("best practices"), hype, unattributed claims, speculation, one-sided views.

### Step 4: Validate & Submit [CRITICAL]

**Verification**:
- Verify URLs accessible; dates match source
- Check metrics against source claims
- Flag uncertainties ("estimated", "projected", "unavailable")
- Cross-check contradictions

**Pre-Submission**:
- 4-6 Q&As, 150-200w each
- ≥3 categories, ≥4 stakeholders
- All citations: ≥1 source + date + URL
- All decision-critical: meet ≥1 criterion
- 1-2 visuals total

**Deliverable**: Q&As + citations + glossary + references + visuals + generation date

---

## Validation Report

| Check | Target | Status |
|-------|--------|--------|
| Q&A Count | 4-6 (~150-200w each) | |
| Categories | ≥3 | |
| Stakeholders | ≥4 | |
| Citations | All ≥1 (date/URL) | |
| Decision-Critical | All ≥1 criterion | |
| Visuals | 1-2 total | |

**Dates**: Generation: _____ | Expires: [+4 weeks]

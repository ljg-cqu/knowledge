# People & Workforce Intelligence News Q&A Generator

## Table of Contents
- [Context & Scope](#context--scope)
- [Requirements](#requirements)
- [Execution](#execution)
- [Validation Report](#validation-report)

## Context & Scope

**Problem**: HR leaders need curated, decision-critical workforce intelligence from fragmented news sources.

**Scope**: Generate 4-6 Q&As (150-200w each) from workforce news (talent supply/demand, skills, compensation, labor policy, culture/DEI, health/wellbeing) for CHRO, VP People, HRBP, Talent Acquisition Lead, L&D Lead, Comp & Benefits Lead, Employee Relations/Labor Lead, DEI Lead, People Analytics Lead, BU Leaders, Line Managers. Monthly | Expires 4wk | 1-18mo timeline (Immediate <3mo, Near-term 3-6mo, Medium-term 6-18mo). **Sources**: SHRM, HBR, LinkedIn Talent Blog, Gartner HR, Radford, Mercer, ILO, OECD, Gallup Workplace, McKinsey People.

**Definitions**:
- **Decision-Critical** (≥1 required): Blocks decisions OR creates risk OR affects ≥2 roles with 1-6mo action AND quantified impact
- **MECE**: Mutually Exclusive, Collectively Exhaustive—sections distinct with no gaps/overlaps
- **Lifecycle Stages**: Attract/Brand → Hire/Onboard → Develop/Grow → Reward/Retain → Transition/Exit
- **Quantified Impact**: Specific metrics (numbers, %, ranges, formulas)—not "significant"/"many"

**Include**: Talent shortages, hiring trends, skills/reskilling, compensation shifts, policy/labor changes, retention risks, engagement/wellbeing signals.

**Exclude**: Technical HR config, product/GTM, finance, rumors, PR fluff, stale (>12mo), orgs <50 employees, deep-dive analysis, technical HR systems, immediate crisis (<1wk).

**Freshness**: Talent/Skills <2mo | Comp/Policy <3mo | Culture/Wellbeing <12mo.

**Inputs**: Industry/geography, org size/challenges, stakeholder priorities, generation date (YYYY-MM-DD).

**Categories** (≥3 of 6): Talent Markets & Hiring (trends, shortages, skills, branding, layoffs) | Skills & Development (certifications, reskilling, licensing) | Compensation & Benefits (benchmarks, pay equity, healthcare, leave) | Policy & Labor (regulations, unions, remote/RTO, visas, gig work) | Culture & DEI (engagement, initiatives, representation, trust) | Health & Wellbeing (mental health, burnout, safety).

## Requirements

**Output**: 4-6 Q&As (150-200w each) covering 3-4 lifecycle stages, ≥4 stakeholder roles (of 11), ≥3 categories (of 6). All Q&As: ≥1 news source (date + URL), quantified impact (or flag "unavailable"), decision path (rationale + trade-offs + timeline). ≥2 diagrams + ≥1 table.

**References**: Glossary (terms + definitions + analogies if complex), ≥4 news sources with URLs, benchmarks/laws/research as applicable.

## Execution

### Step 1: News Discovery [CRITICAL]

Set generation date, calculate news age per freshness priority. Web search 10-15 candidates. **Filter**: Freshness + decision-critical + quantified; exclude rumors/PR. **Select**: 4-6 items covering ≥3 categories, ≥4 stakeholder roles.

### Step 2: Build References [CRITICAL]

**Formats**: G# (term + definition + analogy if complex) | N# (title + source + date YYYY-MM-DD + URL) | B# (metric + source + date) | L# (regulation + jurisdiction + effective date) | R# (finding + source + date if time-sensitive). **Citation**: Inline `[Ref: N1][n1]`, footnote `[n1]: URL`.

### Step 3: Generate Q&A [CRITICAL]

**Structure per Q** (150-200w): News (~30w: what/when/why/category + source/date) | Impact (~60w: lifecycle stages + quantified metrics baseline → target, flag uncertainties) | Stakeholders (~40w: ≥2 roles + concerns/actions + perspective differences) | Decision (~40w: primary path + ≥1 alternative, trade-offs - costs/benefits/risks, when NOT to pursue) | Action (~20w: steps + owners + success metrics). **Include**: Limitations, risks, counterarguments, when NOT to pursue. **Exclude**: Generic advice ("best practices"), hype, unattributed claims, speculation, one-sided views.

**Inline Visuals**: Embed ≥2 diagrams + ≥1 table directly after relevant sections:
- **Lifecycle flow**: Diagram after Impact section showing talent pipeline stages
- **Decision comparison**: Table directly after Decision text comparing alternatives
- **Metric trends**: Table inline with Impact section (comp benchmarks, retention rates, skills gaps)

### Step 4: Validate & Submit [CRITICAL]

**Verification**: URLs accessible, dates match source, check metrics against source claims, flag uncertainties ("estimated", "projected", "unavailable"), cross-check contradictions. **Pre-Submission**: 4-6 Q&As (150-200w each), ≥3 categories, ≥4 stakeholders, all citations (≥1 source + date + URL), all decision-critical (≥1 criterion), ≥2 diagrams + ≥1 table. **Deliverable**: Q&As + citations + glossary + references + visuals + generation date.

## Validation Report

| Check | Target | Status |
|-------|--------|--------|
| Q&A Count | 4-6 (~150-200w each) | |
| Categories | ≥3 | |
| Stakeholders | ≥4 | |
| Citations | All ≥1 (date/URL) | |
| Decision-Critical | All ≥1 criterion | |
| Visuals | ≥2 diagrams + ≥1 table | |

**Dates**: Generation: _____ | Expires: [+4 weeks]

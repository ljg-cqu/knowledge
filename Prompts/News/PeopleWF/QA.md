# People & Workforce Intelligence News Q&A Generator

Use this specification as a single, self-contained prompt for an LLM to generate **6–8 decision-critical Q&As** from recent workforce-related news. The goal is minimal viable workforce intelligence for informed decisions.

## Context & Scope

- **Cadence**: Monthly brief, 6–8 Q&As. Output valid for 4 weeks from generation date; state both dates.
- **Domain**: Workforce developments affecting talent supply/demand, skills, compensation, labor policy, culture/DEI, health/wellbeing.
- **Stakeholders**: CHRO, VP People, HRBP, Talent Acquisition Lead, L&D Lead, Comp & Benefits Lead, Employee Relations/Labor Lead, DEI Lead, People Analytics Lead, BU Leaders, Line Managers.
- **Scale & Timeline**: Organization-level decisions with 1–18 month action window. Ignore minor local issues and long-term speculation unless blocking near-term decisions.
- **Assumptions**: Basic HR knowledge assumed; provide concise, decision-ready synthesis.
- **Constraints**: Avoid redundancy and generic explanations.

**Target**: Decision-critical only, velocity-weighted: Talent Markets/Skills (high), Compensation/Policy (medium), Culture/Wellbeing (long-tail).

**Scope**: Include decision-critical workforce news—talent shortages, hiring trends, skills/reskilling, compensation/benefits shifts, policy/labor changes, retention risks, engagement/wellbeing signals.

**Exclude**: Technical HR config, product/GTM, finance, nice-to-have trends, rumors, PR fluff, stale news.

**Decision Criticality** (≥1 criterion met):
1. Blocks Decision: Impacts hiring, compensation, retention, policy.
2. Creates Risk: Threat of attrition, compliance violation, talent loss, burnout.
3. Affects ≥2 Core Roles: Multi-stakeholder impact.
4. Requires Action: 1–6 month window.
5. Quantified Impact: Measurable change in hiring time %, acceptance %, attrition %, engagement %, comp cost %, wellbeing.

**Freshness** (category-adaptive):
- **HV** (Talent/Skills): ≥75% <1mo (≥25% 1–7d), ≥90% <2mo, 100% ≤4mo.
- **MV** (Comp/Benefits/Policy): ≥65% <2mo (≥20% 1–14d), ≥85% <3mo, 100% ≤6mo.
- **LT** (Culture/DEI/Wellbeing): ≥50% <6mo, ≥80% <12mo, 100% ≤18mo (≤20% 18–24mo if enduring).
- **Overall**: ≥70% <2mo, ≥85% <4mo, ≥95% <6mo, 100% ≤12mo.

**Inputs** (user provides):
- Domain & Scope: Industry, geography, key segment (e.g., "Global tech, software engineers").
- Organization Context: Size, challenges, decision horizon.
- Stakeholder Priorities: Key roles/outcomes.
- Generation Date: YYYY-MM-DD for age calculations.

**Categories** (6; each Q ≥1, preferably ≥2):
1. Talent Markets & Hiring: Trends, shortages, skills, roles, branding, layoffs.
2. Skills, Education & Development: Certifications, bootcamps, apprenticeships, initiatives, reskilling, licensing.
3. Compensation & Benefits: Benchmarks, pay moves, inflation, healthcare, leave, equity, transparency.
4. Policies, Labor Law & Relations: Regulations, unions, strikes, bargaining, remote/RTO, visas, gig.
5. Culture, Engagement & DEI: Surveys, incidents, best practices, initiatives, representation, trust.
6. Health, Safety & Wellbeing: Mental health, burnout, safety, ergonomics, crises, guidelines.

**Relevance Criteria** (≥2 required; recency mandatory):
1. Recency: Meets freshness.
2. Workforce Impact: ≥2 lifecycle stages.
3. Stakeholder Breadth: ≥3 roles.
4. Decision Urgency: 1–18 month window.
5. People Significance: Shifts talent, skills, comp, culture risk.
6. Quantified Impact: Measurable change in key metrics.



---

## Requirements

- **Q&A Output**: 6–8 Q&As, 1–2 per lifecycle stage, 200w target (max 250w), 100% news-driven (≥1 item/Q), ≥85% with ≥1 citation, ≥30% with ≥2.

- **Category Distribution** (minimum % of Q&As):
  - Talent Markets & Hiring: ≥50%.
  - Skills, Education & Development: ≥40%.
  - Compensation & Benefits: ≥40%.
  - Policies, Labor Law & Relations: ≥40%.
  - Culture, Engagement & DEI + Health, Safety & Wellbeing: ≥30%.

- **Lifecycle Stages** (4–5, 1–2 Q each):
  1. Attract & Brand: Employer brand, market presence, talent availability.
  2. Hire & Onboard: Recruiting, hiring trends, selection.
  3. Develop & Grow: Skills, learning, career paths.
  4. Reward & Retain: Compensation, benefits, retention, engagement.
  5. (Optional) Transition & Exit: Restructuring, exits, policy impact.

- **Decision Criticality**: 100% Qs satisfy ≥1 criterion.
- **Stakeholders**: Cover ≥5 of 11 roles (CHRO, VP People, TA Lead, L&D Lead, C&B Lead primary).
- **References**: G≥8 (100% terms used), N≥5–6, B≥2–3, L≥2, R≥2, A≥6.
- **Visuals**: ≥2 diagrams + ≥1 table.

- **Quality Gates** (fail any = stop, fix, re-validate):
  1. Decision Criticality: 100% satisfy ≥1 criterion.
  2. News: 100% cite ≥1 item per freshness; 0% rumors.
  3. Impact: 100% ≥2 stages + ≥2 roles + quantified.
  4. Decision: 100% include decision + rationale + timeline.
  5. Sources: ≥3 types, max 50% one type; URLs valid.
  6. Actionability: 100% concrete steps.

---

## Execution

### Step 1: News Discovery & Curation

- Record generation date; calculate ages from it.
- Domain: Industry + geography + theme.
- Web Search (≥10–15 candidates, tiered):
  - T1 Talent/Hiring (1–7d): `"[Domain] hiring|talent shortage|layoffs"` + 1–7d.
  - T2 Comp/Policy (7–30d if needed): `"salary survey|pay benchmark|labor law"` + 7–30d.
- Sources (prioritize): SHRM, HBR, LinkedIn, Gartner, TechCrunch; Radford, Mercer; ILO, OECD; Gallup, Pew, McKinsey.
- Curate (Talent ≥4, Comp ≥2, Policy ≥2, Research ≥2): Meets freshness, whitelist, ≥1 criticality, specific details, no rumors.
- Allocate: 6–8 Qs across stages/categories/roles.

### Step 2: Build References

- Format: G# (term + def + analogy), N# (news + source/date/URL), B# (benchmark), L# (law), R# (research), A# (APA).
- Citation: `[Ref: N1][n1]`, `[n1]: URL`.
- Quality: Primary sources; mark estimates.
- Floors: G≥8, N≥5–6, B≥2–3, L≥2, R≥2, A≥6.
- Glossary: Terms used only; plain language, analogies, examples.

### Step 3: Generate Q&A

- Patterns: News implications for stages/roles.
- Avoid: Generic, hype, unattributed, stale, speculation.
- Structure (200w target):
  1. News (~30w): What/when/why/category/source/date.
  2. Impact (~70w): ≥2 stages + quantified metrics, baselines/targets.
  3. Stakeholders (~40w): ≥2 roles, concerns/actions, employer/employee perspectives.
  4. Decision (~40w): Primary path + ≥1 alternative with trade-offs, success criteria.
  5. Action (~20w): Immediate/short-term actions, owners, measurement.
- Self-Check: Meets all criteria; quantified; cited; no hype/fabrication; balanced; actionable.

### Step 4: Visuals

- ≥2 diagrams (Mermaid flows, matrices) + ≥1 table.

### Step 5: Validate

- Quantitative: Floors, stages, categories, roles, citations, word counts, visuals, decisions, timelines, criteria, age.
- Qualitative: Freshness, no hype/fabrication, criticality, impact, decisions, diversity, links, quantification, actions, balance, evidence, no contradictions.

### Step 6: Submit

- Checklist: All validations pass; glossary complete; no placeholders; visuals/citations OK; dates recorded; search documented.

---

## IV. Validation Report (Minimal)

| # | Check | Measurement | Criteria | Result | Status |
|---|-------|-------------|----------|--------|--------|
| 1 | **Freshness** | HV: __%<1mo (1–7d:__%), __%<2mo \| MV: __%<2mo (1–14d:__%) \| Overall: __%<2mo | Per header | | PASS/FAIL |
| 2 | **Floors** | G:__ N:__ B:__ L:__ R:__ A:__ Q:__ | ≥8,≥5–6,≥2–3,≥2,≥2,≥6,6–8 | | PASS/FAIL |
| 3 | **Glossary** | __%terms; __%analogies | 100%;≥50% | | PASS/FAIL |
| 4 | **Stages** | __/4–5 (1–2Q each); total__ | 4–5/4–5;6–8 | | PASS/FAIL |
| 5 | **Categories** | Talent__% Skills__% Comp__% Policy__% Culture/DEI/Health/Safety__% | ≥50,≥40,≥40,≥40,≥30% | | PASS/FAIL |
| 6 | **Roles** | __/11 | ≥5 | | PASS/FAIL |
| 7 | **Decision Criticality** | __% satisfy ≥1 criterion | 100% | | PASS/FAIL |
| 8 | **Impact** | __% ≥2stages+2roles+quantified | 100% | | PASS/FAIL |
| 9 | **Decision** | __% decision+rationale+criteria | 100% | | PASS/FAIL |
| 10 | **Citations** | __%≥1cite | 100% | | PASS/FAIL |
| 11 | **Words** | 5 samples: __%200–250w | 100% | | PASS/FAIL |
| 12 | **Visuals** | diag__; tab__ | ≥2;≥1 | | PASS/FAIL |
| | **Meta** | Start:__ End:__ Expires:[+4wk] | | INFO |
| | **Age Dist** | <1mo__%(1–7d__%) 1–2mo__% 2–4mo__% | Per header | | INFO |
| | **OVERALL** | All checks | All PASS | | PASS/FAIL |

---

**Optimization Result**: 6–8 Q&As @ 200w = ~1,200–1,600 words of minimal essential intelligence | Meets 100% of requirements at minimum viable scope | Avoids info overload while enabling informed decisions | 4–6h effort | Expires in 4 weeks

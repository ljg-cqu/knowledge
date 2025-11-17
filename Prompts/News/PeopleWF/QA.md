# People & Workforce Intelligence News Q&A Generator

Use this specification as a single, self-contained prompt for an LLM to generate **6–8 decision-critical Q&As** from recent workforce-related news. The goal is minimal viable workforce intelligence for informed decisions with limited time.

## I. Context & Scope

- **Cadence & Effort**: Monthly brief, 4–6h analyst effort, 6–8 Q&As. Output is valid for 4 weeks from the generation date; always state both dates.
- **Domain**: Workforce developments that materially affect talent supply/demand, skills, compensation, labor policy, culture/DEI, and health/wellbeing.
- **Stakeholders**: CHRO, VP People, HRBP, Talent Acquisition Lead, L&D Lead, Comp & Benefits Lead, Employee Relations/Labor Lead, DEI Lead, People Analytics Lead, BU Leaders, Line Managers.
- **Scale & Timeline**: Organization-level decisions with a 1–18 month action window. Ignore minor local issues and very long-term speculation unless they clearly block a near-term decision.
- **Assumptions**: Readers understand basic HR/people concepts; they need concise, decision-ready synthesis, not tutorials.
- **Constraints**: Output must be scannable in ≤30 minutes by senior people leaders; avoid redundancy and generic explanations.

**Target**: Decision-critical only, velocity-weighted: Talent Markets/Skills (high), Compensation/Policy (medium), Culture/Wellbeing (long-tail).

**Scope**: Include only decision-critical workforce news—talent shortages, hiring trends, skills/reskilling programs, compensation and benefits shifts, policy and labor changes, retention risks, engagement and wellbeing signals.

**Exclude**: Technical/operational HR configuration, product/GTM strategy, corporate finance/capital markets, nice-to-have trends, rumors, marketing/PR fluff, stale news.

**Decision Criticality Framework** (include if ≥1 criterion met):
1. **Blocks Decision**: Directly impacts hiring strategy, compensation structure, retention, or policy compliance.
2. **Creates Risk**: Material threat (attrition spike, compliance violation, talent loss, burnout).
3. **Affects ≥2 Core Roles**: Multi-stakeholder impact (e.g., CHRO + TA Lead, VP People + L&D).
4. **Requires Action**: 1–6 month action window (not speculative).
5. **Quantified Impact**: Measurable change in hiring time %, acceptance rate %, attrition %, engagement %, compensation cost %, or wellbeing signal.

**Freshness** (category-adaptive; apply to all news):
- **HV** (Talent/Skills/Disruptions): ≥75% <1mo (≥25% in 1–7d), ≥90% <2mo, 100% ≤4mo.
- **MV** (Comp/Benefits/Policy/Labor): ≥65% <2mo (≥20% in 1–14d), ≥85% <3mo, 100% ≤6mo.
- **LT** (Culture/Engagement/Wellbeing/DEI): ≥50% <6mo, ≥80% <12mo, 100% ≤18mo (≤20% at 18–24mo if enduring).
- **Overall**: ≥70% <2mo, ≥85% <4mo, ≥95% <6mo, 100% ≤12mo.
- **Validity**: Content expires 4 weeks after generation; re-validate if used beyond 2 months.

**Inputs (user must provide before generation)**:
- **Domain & Scope**: Industry, geography, key workforce segment (e.g., "Global tech, software engineers and product managers").
- **Organization Context**: Size (headcount), current workforce challenges, and decision horizon in months.
- **Stakeholder Priorities**: Which roles and outcomes matter most (e.g., hiring velocity vs retention vs engagement).
- **Generation Date**: YYYY-MM-DD (used for all news age and freshness calculations).

**Categories** (6; each Q covers ≥1, preferably ≥2):

1. **Talent Markets & Hiring**: Trends, shortages, in-demand skills, emerging roles, employer branding, layoffs/freezes.
2. **Skills, Education & Development**: Certifications, bootcamps, apprenticeships, gov/industry initiatives, reskilling/upskilling, licensing.
3. **Compensation & Benefits**: Benchmarks and pay moves, inflation, healthcare, wellbeing, parental leave, equity/variable pay, transparency laws, fairness.
4. **Policies, Labor Law & Relations**: Regulations, unions, strikes, collective bargaining, remote/hybrid models, RTO mandates, visa/immigration, working time, gig economy.
5. **Culture, Engagement & DEI**: Surveys and benchmarks, incidents, best practices, DEI initiatives, representation, trust, leadership, psychological safety.
6. **Health, Safety & Wellbeing**: Mental health, burnout, safety, ergonomics, health crises/pandemics, occupational guidelines, program impact.

**Relevance Criteria** (≥2 required; Recency mandatory):
1. **Recency**: Meets freshness thresholds.
2. **Workforce Impact**: Affects ≥2 lifecycle stages.
3. **Stakeholder Breadth**: Affects ≥3 roles.
4. **Decision Urgency**: 1–18 month action window.
5. **People Significance**: Shifts talent, skills, compensation, or culture risk.
6. **Quantified Impact**: Measurable change in hiring time, acceptance rate, attrition, engagement, compensation cost, or wellbeing.

**Answer Structure** (200w target, max 250w):
- **News**: ≥1 item; concise summary of what, when, why, category, and explicit source + date.
- **Impact**: ≥2 stages and ≥2 roles, quantified with baseline and target where possible.
- **Decision**: Primary path (Invest/Adopt/Adjust/Monitor/Avoid) plus ≥1 credible alternative with trade-offs (risks, costs, benefits) and explicit success criteria (how to measure outcomes).
- **Timeline**: Immediate/short term; include medium term only when strategic.
- **Projections**: Only if critical and supported by sources.

---

## II. Requirements

- **Q&A Output**: 6–8 Q&As | 1–2 per lifecycle stage | 200w target (max 250w) | 100% news-driven (≥1 item/Q) | ≥85% with ≥1 citation, ≥30% with ≥2 citations | Each Q links ≥1 category + impact + decision.

- **Category Distribution** (velocity-weighted, minimum coverage):
  - Talent Markets & Hiring: 2–3 Q&As (≥50%).
  - Skills & Education: ≥1 Q&A (≥40%).
  - Compensation & Benefits: 1–2 Q&As (≥40%).
  - Policy & Labor: 1–2 Q&As (≥40%).
  - Culture & Wellbeing: ≥1 Q&A (≥30%).

- **Lifecycle Stages** (4–5, 1–2 Q each):
  1. **Attract & Brand**: Employer brand, market presence, talent availability.
  2. **Hire & Onboard**: Recruiting, hiring trends, selection.
  3. **Develop & Grow**: Skills, learning, career paths.
  4. **Reward & Retain**: Compensation, benefits, retention, engagement.
  5. (Optional) **Transition & Exit**: Restructuring, exits, policy impact.

- **Decision Criticality**: 100% of Qs satisfy ≥1 of the 5 criteria (Blocks/Risk/Roles/Action/Quantified).
- **Stakeholders**: Cover ≥5 of 11 core roles (CHRO, VP People, TA Lead, L&D Lead, C&B Lead as primary).
- **References** (build before Q&A, minimal but sufficient): G≥8 (100% terms used), N≥5–6 (per freshness), B≥2–3 (benchmarks), L≥2 (law/policy), R≥2 (research), A≥6 (APA citations).
- **Visuals**: At least 2 diagrams + 1 table (e.g., pay bands, benchmarks, risk matrices).

- **Quality Gates** (fail ANY = stop, fix, re-validate ALL):
  1. Decision Criticality: 100% satisfy ≥1 criterion.
  2. News: 100% cite ≥1 item, per freshness; 0% rumors/hype.
  3. Impact: 100% cover ≥2 stages + ≥2 roles + quantified metrics.
  4. Decision: 100% include decision + rationale + timeline.
  5. Sources: ≥3 types, max 50% from any one type; 100% URLs valid.
  6. Actionability: 100% concrete steps; 0% abstract language.

---

## III. Execution

### Step 1: News Discovery & Curation (Minimal)

- **Record generation date (YYYY-MM-DD)**; calculate all news ages from this.
- **Domain**: Industry + geography + workforce theme (e.g., "Global Tech Talent Q1 2025", "EU Manufacturing Skills Q3–Q4 2025").
- **Web Search** (≥10–15 candidates, tiered for efficiency):
  - **T1 – Talent/Hiring (1–7d, search first)**: `"[Domain] hiring|talent shortage|layoffs"` + 1–7d.
  - **T2 – Comp/Policy (7–30d, if T1 insufficient)**: `"salary survey|pay benchmark|labor law"` + 7–30d.
- **Sources** (whitelist, prioritize):
  - Talent: SHRM, HBR, LinkedIn News, Gartner HR, TechCrunch (tech hiring).
  - Compensation: Radford, Mercer, PayScale, company blogs and surveys.
  - Policy/Labor: ILO, OECD, labor departments, unions, employer associations.
  - Research: Gallup, Pew, McKinsey Global Institute, HR journals.
  - Avoid PR fluff, rumors, listicles, speculation.
- **Tools**: Perplexity ("past week"), ChatGPT ("latest"), Google (`after:DATE`), LinkedIn News.
- **Curate** (≥10–15 candidates: Talent ≥4, Comp ≥2, Policy ≥2, Research ≥2):
  - Meets freshness thresholds.
  - Whitelist or primary source.
  - Satisfies ≥1 Decision Criticality criterion.
  - Specific details (dates, names, numbers, metrics).
  - Not marketing/rumors.
- **Verify**: If an item fails decision criticality or freshness, discard and resample.
- **Allocate**: 6–8 Qs × 4–5 stages (1–2 each) × 4–5 categories (≥1/Q) × ≥5 roles.

### Step 2: Build References (Minimal)

- **Format**: G# (term, definition + analogy, context) | N# (news, source, date, category, URL) | B# (benchmark/model, URL) | L# (law/policy, details, URL) | R# (research, findings, URL) | A# (APA 7th + tag).
- **Citation**: Markdown reference links: `[Ref: N1][n1]` in text, `[n1]: URL` at answer end.
- **Source Quality**: Prefer primary/official sources (government, regulators, reputable surveys, company filings). Do not invent organizations, reports, statistics, or URLs; clearly mark any estimates.
- **Floors**: G≥8 (100% terms used), N≥5–6, B≥2–3, L≥2, R≥2, A≥6.
- **Glossary** (only terms used in Q&As): keep coverage complete, language plain, add 1–2 analogies per term, explain why the term matters for decisions, and give real-number examples.

### Step 2.5: Opportunistic Refresh (optional, default: skip)

- **Trigger**: Major labor law or large workforce event (cross-industry strike, immigration policy, global health guidance) emerging in 24–72h and affecting ≥3 Q&As.
- **Action**: Quick search → add 1–2 "BREAKING" items → adjust 1–2 Qs → document in references.

### Step 3: Generate Q&A (batch 2–3, self-check each)

- **Before**: Review glossary. Track all terms used.
- **Patterns**: "[Talent News]: implications for [Stages]+[Roles]?" | "[Comp Benchmark]: pay strategy?" | "[Law Change]: policy response?" | "[Engagement Trend]: culture action?"
- **Avoid**: Generic questions, hype, unattributed claims, stale news, speculation.
- **Structure** (200w target, max 250w):
  1. **News** (~30w): What, when, why, category, and explicit source + date `[Ref: N#][n#]`.
  2. **Impact** (~70w): ≥2 stages + quantified metrics (hiring time %, acceptance rate %, attrition %, compensation cost %, engagement or wellbeing signal), with baseline vs target or explicit ranges where available.
  3. **Stakeholders** (~40w): ≥2 roles (at least one leadership and one workforce-facing) with concerns and actions; reflect both employer and employee perspectives where relevant.
  4. **Decision** (~40w): Recommend a primary path (Invest/Adopt/Adjust/Monitor/Avoid) plus ≥1 credible alternative with key trade-offs (risks, costs, benefits) and clear success criteria (how you will know the decision worked).
  5. **Action** (~20w): Immediate (0–2wk) and short-term (2wk–2mo) actions, clear owner(s), and one measurement method (metric + review cadence).
- **Self-Check**: Age OK; Decision Criticality ✓; ≥2 stages; ≥2 roles; decision and alternatives clear; ~200w; metrics quantified with baseline/target where possible; ≥1 citation; 0% hype; 0 fabricated facts/URLs; at least one alternative considered; balanced employer/employee perspective where relevant; success criteria + metrics defined; uncertainties flagged (estimates clearly marked); 100% actionable; all terms present in glossary.

### Step 4: Visuals (≥2 diagrams + ≥1 table)

- **Types**: Lifecycle flows, recruiting funnels, pay band comparisons, risk matrices, attrition/engagement trends.
- **Format**: Mermaid (flows), markdown tables (data), 2×2 matrices.

### Step 5: Validate (fail ANY = stop, fix, re-run ALL)

- **Quantitative**: Floors met; glossary 100%; 4–5 stages; category percentages met; ≥5 roles; citations OK; 5 word samples near 200w; visuals OK; decision 100%; timeline 100%; success criteria 100% (baseline + target + metric); age per freshness.
- **Qualitative**: News per freshness, 0% hype; 0 fabricated facts/URLs; Decision Criticality 100%; Impact 100% (≥2 stages + roles + quantified); Decision 100% with ≥1 alternative and trade-offs; source diversity ≥3 types; each stage has ≥1 news + analysis; links valid; quantification 100%; actions specific and actionable; balanced employer/employee perspective where relevant; evidence 100%; search documented; no internal contradictions or terminology drift.

### Step 6: Submit

- **Checklist** (all YES): Validations PASS; floors met; glossary complete (100% terms, ≥50% with analogies); TOC (if any) complete; 0 placeholders; visuals OK; citations OK; impact OK; decision OK; timeline OK; success criteria OK; categories OK; roles OK; freshness OK; evidence 100%; URLs valid; dates recorded (generation + expire = gen + 4wk); search documented.

---

## IV. Validation Report (Minimal)

| # | Check | Measurement | Criteria | Result | Status |
|---|-------|-------------|----------|--------|--------|
| 1 | **Freshness** | HV: __%<1mo (1–7d:__%), __%<2mo \| MV: __%<2mo (1–14d:__%) \| Overall: __%<2mo | Per header | | PASS/FAIL |
| 2 | **Floors** | G:__ N:__ B:__ L:__ R:__ A:__ Q:__ | ≥8,≥5–6,≥2–3,≥2,≥2,≥6,6–8 | | PASS/FAIL |
| 3 | **Glossary** | __%terms; __%analogies | 100%;≥50% | | PASS/FAIL |
| 4 | **Stages** | __/4–5 (1–2Q each); total__ | 4–5/4–5;6–8 | | PASS/FAIL |
| 5 | **Categories** | Talent__% Comp__% Policy__% Skills__% Culture__% | ≥50,≥40,≥40,≥40,≥30% | | PASS/FAIL |
| 6 | **Roles** | __/11 | ≥5 | | PASS/FAIL |
| 7 | **Decision Criticality** | __% satisfy ≥1 criterion | 100% | | PASS/FAIL |
| 8 | **Impact** | __% ≥2stages+2roles+quantified | 100% | | PASS/FAIL |
| 9 | **Decision** | __% decision+rationale+criteria | 100% | | PASS/FAIL |
| 10 | **Citations** | __%≥1cite | 100% | | PASS/FAIL |
| 11 | **Words** | 5 samples: __%200w | 100% | | PASS/FAIL |
| 12 | **Visuals** | diag__; tab__ | ≥2;≥1 | | PASS/FAIL |
| | **Meta** | Start:__ End:__ Expires:[+4wk] | | INFO |
| | **Age Dist** | <1mo__%(1–7d__%) 1–2mo__% 2–4mo__% | Per header | | INFO |
| | **OVERALL** | All checks | All PASS | | PASS/FAIL |

---

**Optimization Result**: 6–8 Q&As @ 200w = ~1,200–1,600 words of minimal essential intelligence | Meets 100% of requirements at minimum viable scope | Avoids info overload while enabling informed decisions | 4–6h effort | Expires in 4 weeks

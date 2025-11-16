# Technical Operations News Intelligence Q&A Generator

Generate 10–12 Q&As transforming news into actionable technical intelligence across 6 categories, 8 lifecycle phases, 12 stakeholder roles.

**Target**: Weekly (1 day output) | High-velocity (Tech/Security/Ecosystem) + Long-tail (Regulatory/Standards)

**Scope**: Technical stack, infrastructure, security, development lifecycle, technical debt, engineering practices. Covers digital/physical systems at scale (software platforms, industrial, logistics, services).

**MECE Position**: Technical/engineering function only. Excludes product/market strategy (ProdMarket.md), commercial GTM (CommOps.md), corporate finance/treasury (FinEcon.md), long-term strategy/policy (StratIntel.md), early-stage formation (Startup.md).

**Freshness**:
- **HV** (Tech/Ecosystem/Security): ≥85% <1mo (≥30% 1-3d), ≥95% <2mo, 100% ≤4mo
- **MV** (Standards/Eng Practices): ≥70% <2mo (≥20% 1-3d), ≥90% <3mo, 100% ≤6mo
- **LT** (Regulatory): ≥50% <3mo, ≥75% <6mo, 100% ≤12mo (≤20% at 12-18mo if enduring)
- **Overall**: ≥70% <2mo, ≥85% <4mo, ≥95% <6mo, 100% ≤12mo | **Validity**: 2 weeks

## I. Context & Scope

**Audience**: Engineering teams, architects, DevOps/SRE, security, data engineers, technical leadership. Focus: technical decisions (stack, infrastructure, security, practices, governance).

**Include**: Releases, infrastructure, security (CVEs/patches), ecosystem (APIs/deprecations), standards/regulations, engineering practices, vendor stability, benchmarks, patterns.

**Exclude**: Marketing, GTM, financial metrics (except infra costs), rumors, trivial updates, stale news (>4mo HV, >12mo Regulatory).

**Categories** (6, each Q≥2): (1) Technical Releases (tools, frameworks, DBs, SDKs, APIs), (2) Infrastructure/Cloud (providers, containers, IaC), (3) Security (CVEs, patches, threats), (4) Ecosystem/Integration (APIs, deprecations, partnerships), (5) Standards/Regulations (compliance, governance), (6) Engineering Practices (CI/CD, observability, patterns, vendor stability).

**Relevance Criteria** (≥2, Recency MANDATORY):
1. **Recency** (per freshness guarantee)
2. **Lifecycle**: ≥2 phases or cross-phase
3. **Stakeholders**: ≥3 roles or multi-role
4. **Urgency**: 1-6mo action
5. **Significance**: Shifts practices/patterns/infrastructure
6. **Quantified**: Measurable perf/reliability/security/cost impact

**Answer Format** (200-350w): ≥1 news + summary + impact (≥2 phases, ≥2 roles, quantified) + decision (A/I/D/A) + timeline + optional projections (sourced, confident, timed).

## II. Requirements

**Q&A**: 10-12 | 1-2/phase | 200-350w | 100% news-driven | ≥85% ≥1 cite, ≥40% ≥2 cites | Each: ≥2 categories + impact + decision

**Lifecycle** (8, 1-2 Q each): (1) Req & Discovery, (2) Arch & Design, (3) Dev, (4) Test & Quality, (5) Deploy & Release, (6) Ops & Observability, (7) Maintenance, (8) Evolution & Governance

**Coverage**: Tech Releases 80% | Infra/Cloud 75% | Security 60% | Ecosystem 95% | Standards/Regs 45% | Eng Practices 40%

**Decision** (100%): Impact (≥2 phases, ≥2 roles, quantified: perf/cost/reliability/security) + A/I/D/A (rationale, alternatives) + Timeline

**Stakeholders** (≥8/12): Tech Lead, Architect, Backend/Frontend Dev, DevOps, SRE, Security Eng, Data Eng, QA, Platform Eng, Eng Manager, CTO/VP Eng

**References** (build first): G≥10 (100% terms/acronyms, analogies/formulas), N≥6, T≥5, S≥3, R≥3, O≥2 (org events), A≥12 (APA)

**Visuals**: ≥6 diagrams + ≥3 tables (avg 0.75D+0.4T/phase)

**Quality Gates** (fail ANY = stop, fix, re-validate):
1. **News**: 100% cite ≥1 fresh item; 0% marketing/rumors
2. **Impact**: 100% ≥2 phases + ≥2 roles + quantified
3. **Decision**: 100% A/I/D/A + rationale + timeline + criteria
4. **Sources**: ≥5 types, max 35%; ≥1 news + ≥1 analysis/phase; 100% valid URLs
5. **Coverage**: ≥9/14 roles; categories per thresholds
6. **Actionable**: 100% concrete + timelines; 0% abstract

## III. Execution

### Step 1: News Discovery (Record generation date YYYY-MM-DD)

1. **Domain**: Industry/ecosystem + date

2. **Search** (≥20-25 candidates, tiered):
   - **T1 (1-3d)**: Tech/Sec/Ecosystem releases, CVEs, integrations, org events (hiring/layoffs/financing/leadership)
   - **T2 (7-14d)**: HV backfill if T1 insufficient
   - **T3 (2-4wks)**: HV <1mo; Reg/Standards 3-6mo

   **Sources**: Official (vendor, GitHub, standards), Tech Media (TechCrunch, InfoQ, HN), Security (CVE DB, CISA), Analysis (Gartner/Forrester), Org (Layoffs.fyi, LinkedIn, Crunchbase). Avoid PR/SEO/marketing.

   **Tools**: Perplexity ("past week"), ChatGPT ("recent"), Google (`after:YYYY-MM-DD`), HN (>50 pts)

3. **Curate** (≥15): ✅Fresh ✅Whitelist ✅≥2 relevance ✅Details (dates/versions/numbers) ✅0% marketing

4. **Verify**: Age distribution per freshness guarantee; re-search if fails

5. **Allocate**: 10-12 Q × 8 phases × 6 categories × 12 roles

### Step 2: Build References (before Q&A)

**Format**: G# (term+analogy/formula) | N# (news+date+URL) | T# (tool+ver+URL) | S# (standard+changes) | R# (report+findings) | O# (org event+implication) | A# (APA+tag)

**Citations**: `[Ref: N1][n1]` → Define `[n1]: URL` at answer end

**Floors**: G≥10 (100% terms/acronyms/metrics), N≥6, T≥5, S≥3, R≥3, O≥2, A≥12

**Glossary**: ALL terms/acronyms (SRE, CVE, p95, ROI) + plain definitions + analogies ("Logical replication = copying doc while editing original") + formulas (ROI = (Gain-Cost)/Cost×100%) + context + examples

**News**: Title (Source, MM/DD/YYYY): Summary | Cat | Age | Impact | Roles | URL | Justify if HV >1mo or Reg >6mo

### Step 3: Generate Q&A (batch 4-5, self-check)

**Before**: Review glossary; track ALL terms used; verify 100% defined with analogies/formulas

**Patterns**: "[News] implications for [Phase]+[Roles]?" | "Compare [A] vs [B] across [Phases]" | "[News] cascade [P1]→[P2]→[P3]?"

**Avoid**: Generic "What is X?", speculation, stale news

**Structure** (200-350w):
1. **News** (~50w): What, when, who, why `[Ref: N#][n#]`
2. **Impact** (~90w): ≥2 phases + quantified (cost/time/risk/perf)
3. **Stakeholders** (~60w): ≥2 roles + concerns + actions + authority
4. **Decision** (~70w): A/I/D/A + rationale + 1-2 alternatives + criteria
5. **Action** (~50w): Immediate (0-2wks), Short (2wks-2mo) + owner + deliverable
6. **Projections** (opt ~30w): "[Source] projects [outcome] by [time] with [confidence]" `[Ref: R#][r#]`
7. **Links**: Define all at end: `[n1]: URL`
8. **Artifacts**: 1-2 diagrams/tables

**Self-Check**: Fresh | ≥2 phases | ≥2 roles | A/I/D/A | 200-350w | Quantified | Artifact | Timeline | 0% hype | Projections sourced | 100% terms in glossary

### Step 4: Visuals (≥6 diagrams + ≥3 tables, ≥60% referenced)

**Types**: Impact matrices, decision trees, timelines, stakeholder tables, comparisons, risk/cost tables

**Format**: Mermaid (flows/timelines), Markdown tables (units/dates), 2×2 matrices

### Step 5: Final Checks

**Refs**: 100% resolve | Fresh | Complete | G≥10 (100% terms+analogies) | N≥6 | R≥3 | O≥2 | A≥12 (45-65% news, 15-25% reports)

**Decision**: 100% A/I/D/A + rationale + alternatives + criteria + timeline

**Stakeholders**: ≥9/14 roles | Actions + authority | Cross-role coordination

### Step 6: Validate (fail ANY = stop, fix, re-run ALL)

**Quantitative**: Floors (G≥10, N≥6, T≥5, S≥3, R≥3, O≥2, A≥12, Q=10-12) | Glossary (100% terms, ≥60% analogies/formulas) | 8 phases (1-2Q) | Coverage (Tech 80%, Infra 75%, Sec 60%, Eco 95%, Std/Reg 45%, Eng 40%) | ≥9/14 roles | Cites (100% ≥1 news, ≥85% ≥1, ≥40% ≥2) | Dist (News 45-65%, Reports 15-25%, Docs 15-25%) | Words (3 samples, 100% 200-350) | Visuals (≥60% ref, ≥6D, ≥3T) | Decision 100% | Timeline 100% | Fresh per guarantee

**Qualitative**: Fresh (0% marketing) | Impact (100% ≥2 phases+roles+quantified) | Decision (100% A/I/D/A+alts+criteria) | Diversity (≥5 types, max 35%) | Per-phase (≥1 news+analysis) | Links (100% valid) | Refs (100% resolve) | Quantified (100%) | Actionable (100%) | Evidence (100%) | Projections (100% sourced+confident+timed) | Search doc

### Step 7: Submit

**Checklist** (all YES): 20 validations PASS | Floors met | Glossary complete (100% terms, ≥60% analogies) | TOC (8 phases) | 0 placeholders | ≥6D+≥3T | 100% fresh news | 100% impact | 100% decision | 100% timeline | Coverage per thresholds | ≥9/14 roles | Fresh guarantee met | 100% evidence | URLs valid | Dates (gen+expire=+2wks) | Search doc

## IV. Validation Report

| # | Check | Measurement | Criteria | Result | Status |
|---|-------|-------------|----------|--------|--------|
| 1 | **Freshness** | HV: _% <1mo (1-3d: _%), _% <2mo \| MV: _% <2mo \| LT: _% <3mo \| Overall: _% <2mo | Per guarantee | | P/F |
| 2 | **Floors** | G:_ N:_ T:_ S:_ R:_ O:_ A:_ Q:_ | ≥10,≥6,≥5,≥3,≥3,≥2,≥12,10-12 | | P/F |
| 2a | **Glossary** | _% terms; _% analogies; _% unfamiliar | 100%; ≥60%; 100% | | P/F |
| 3 | **Lifecycle** | _/8 phases (1-2Q); total _ | 8/8; 10-12 | | P/F |
| 4 | **Coverage** | Tech _%, Infra _%, Sec _%, Eco _%, Std _%, Eng _% | 80,75,60,95,45,40 | | P/F |
| 5 | **Stakeholders** | _/14 roles | ≥9 | | P/F |
| 6 | **Impact** | _% ≥2 phases+roles+quantified | 100% | | P/F |
| 7 | **Decision** | _% A/I/D/A+rationale+alts | 100% | | P/F |
| 8 | **Timelines** | _% immed/short+owners | 100% | | P/F |
| 9 | **Citations** | _% ≥1 news; _% ≥1; _% ≥2 | 100%; ≥85%; ≥40% | | P/F |
| 10 | **Distribution** | News _%, Reports _%, Docs _% | 45-65, 15-25, 15-25 | | P/F |
| 11 | **Diversity** | Types _; max _ | ≥5; ≤35% | | P/F |
| 12 | **Per-Phase** | _/8 ≥1 news+analysis | 8/8 | | P/F |
| 13 | **Words** | 3 samples: _% in 200-350w | 100% | | P/F |
| 14 | **Visuals** | _% ref; _D; _T | ≥60%; ≥6; ≥3 | | P/F |
| 15 | **Quantified** | _% measurable | 100% | | P/F |
| 16 | **Links** | _% valid | 100% | | P/F |
| 17 | **Cross-Refs** | _% resolve | 100% | | P/F |
| 18 | **Actionable** | _% concrete; _% abstract | 100%; 0% | | P/F |
| 19 | **Projections** | If used: _% sourced; _% confident; _% timed | 100% each | | P/F |
| 20 | **Search** | Queries/Whitelist: Y/N; Candidates _; Accept _% | Y/Y; ≥20; 50-70% | | P/F |
| | **Meta** | Start:_ End:_ Expires:[+2wks] | | INFO |
| | **Age Dist** | <1mo _% (1-3d _%) \| HV _%, MV _%, LT _% | Per guarantee | | INFO |
| | **OVERALL** | All checks | All PASS | | P/F |

## V. Question Quality (fails ≥3/11 = rewrite)

**Criteria**: Fresh | Lifecycle (1-2 phases) | ≥2 roles | ≥2 categories | A/I/D/A | Quantified | Cross-phase | Urgent | Alternatives | Evidence | Actionable | Forward (if projections)

**✓ Good**: "Claude 3.5 v2 (Oct 2024) 2x perf: Dev & Testing impact?" | "EU AI Act (May 2024) deadline Aug 2026: Req & Gov readiness?"

**✗ Bad**: "How does X work?" (no news) | "What is X?" (overview) | "Should we use X?" (no trigger)

## VI. Output Format

### A. TOC
```markdown
# [Domain] News Intelligence Q&A ([Period])
## Contents
1. Executive Summary (Overview | Insights | Dashboard)
2. Phase Matrix (8×6 categories)
3. Q by Phase: Req (Q1-Q2) | Arch (Q3-Q4) | Dev (Q5-Q6) | Test (Q7-Q8) | Deploy (Q9-Q10) | Ops (Q11-Q12) | Maint (Q13-Q14) | Evol (Q15-Q16)
4. References: G | N | T | S | R | O | A
5. Validation (20 checks)
```

### B. Exec Summary
```markdown
## Executive Summary
**Domain**: [Name] | **Period**: [Q3-Q4 2024] | **Coverage**: [# items, 6 cats]
**News**: Tech (#: top 2-3+dates) | Infra (#) | Sec (#) | Eco (#) | Std (#) | Eng (#) | Org (#)
**Insights**: 1. [News] ([Date]): [Impact] → [A/I/D/A] → [Timeline] (repeat 2-3)
**Dashboard**: [Phase | News | Action | Timeline]
**Roles**: [10-12] | **Refs**: G=# N=# T=# S=# R=# O=# A=#
```

### C. Phase Table

| # | Phase | Range | Count | Categories | News | Roles | Artifacts |
|---|-------|-------|-------|------------|------|-------|-----------|
| 1 | Req & Disc | Q1-Q2 | 1-2 | Std, Eco | [Top] | TL, Arch | 1D+0.5T |
| 2 | Arch & Design | Q3-Q4 | 1-2 | Tech, Infra, Eco | [Top] | Arch, SRE | 1D+0.5T |
| 3 | Dev | Q5-Q6 | 1-2 | Tech, Eng | [Top] | Dev, DevOps | 1D+0.5T |
| 4 | Test & QA | Q7-Q8 | 1-2 | Tech, Sec | [Top] | QA, Dev | 1D+0.5T |
| 5 | Deploy | Q9-Q10 | 1-2 | Tech, Eco | [Top] | DevOps, SRE | 1D+0.5T |
| 6 | Ops & Obs | Q11-Q12 | 1-2 | Infra, Tech | [Top] | SRE, PE | 1D+0.5T |
| 7 | Maint | Q13-Q14 | 1-2 | Sec, Tech | [Top] | Dev, SecEng | 1D+0.5T |
| 8 | Evol & Gov | Q15-Q16 | 1-2 | Eco, Std, Eng | [Top] | Arch, EM | 1D+0.5T |
| | **Total** | | **10-12** | **All 6** | **8+** | **≥9/14** | **≥6D+≥3T** |

Legend: TL=Tech Lead, EM=Eng Manager, PE=Platform Eng, SecEng=Security Eng, D=Diagrams, T=Tables

### D. Q&A
```markdown
### Q#: [News Question + Phase + Roles]
**Phase**: [Phase] | **Roles**: [P, S] | **Cats**: [✓✓] | **Decision**: Y
**News** (~50w): What, when, who, why [Ref: N#][n#]
**Impact** (~90w): Phases (≥2) | Quantified: Cost [$] | Time [h/d/wk] | Risk [%] | Perf [Δ]
**Stakeholders** (~60w): **[R1]**: Concerns, actions, authority | **[R2]**: ditto
**Decision** (~70w): **Rec**: A/I/D/A | **Rationale**: [Why] | **Alts**: [1-2] | **Success**: [Measurable]
**Action** (~50w): **Immed (0-2wks)**: [Actions+owner] | **Short (2wks-2mo)**: [Actions+owner]
**Projections** (opt ~30w): [Source] projects [outcome] by [time] with [confidence] [Ref: R#][r#]
**Artifacts**: [Type]
[n1]: URL
[r1]: URL
---
```

## References

### Glossary (G1-G20+)
**G#. Term (Acronym)**: Plain definition | Analogy/Formula | Context | Why it matters | Example

**Examples**: 
- **G1. p95 Latency**: Response time ≤95% requests complete
- **G2. ROI**: (Gain−Cost)/Cost×100%

### News (N1-N12+)
**N#. Title** (Source, MM/DD/YYYY): Summary | Cat | Impact (phases, cost/time/risk) | Roles | URL

### Tools (T1-T10+)
**T#. Tool (Cat)**: Desc | Ver | Context | License | Adoption | Date | URL

### Standards (S1-S6+)
**S#. ID (Org)**: Title | Ver | Date | Changes | Compliance | Phases | URL

### Reports (R1-R6+)
**R#. Title** (Firm, Date): Findings | Data | Positioning | Recs | Relevance | URL

### Org Events (O1-O3+)
**O#. Company Event** (Source, MM/DD/YYYY): Type (Hiring/Layoff/Financing/Leadership) | Details (headcount/$/role) | Context | Implication | Impact | URL

### Citations (A1-A22+)
**A#. APA 7th [Tag]**: Author/Org. YYYY, Mon DD. *Title*. Pub. URL [News/Report/Advisory/Std/Org]
```

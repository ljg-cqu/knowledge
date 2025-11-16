# Product & Market Intelligence News Q&A Generator

Generate 10–12 Q&As from recent industry news across 6 categories, 7 product phases, 11 stakeholder roles—transforming news into actionable product intelligence.

**Cadence**: Bi-weekly | 10-16h effort | **Expires**: 2 weeks from generation

**Freshness** (all news must meet these age thresholds):
- **HV** (Competitive, Pricing): ≥85% <1mo (≥30% 1-3d), ≥95% <2mo, 100% ≤4mo
- **MV** (Strategy, UX, Research): ≥70% <2mo (≥20% 1-3d), ≥90% <3mo, 100% ≤6mo
- **LT** (Positioning): ≥60% <3mo, ≥80% <6mo, 100% ≤9mo
- **Overall**: ≥75% <2mo, ≥90% <4mo, 100% ≤9mo

**Scope**: Product strategy, competitive features, pricing, UX trends, customer research, market positioning. For post-PMF organizations.

**Exclude**: Technical implementation, sales execution, corporate finance (except pricing), long-term R&D, early-stage PMF, rumors, marketing fluff, stale news.

**Categories** (6, each Q covers ≥2):
1. **Competitive Features**: Launches, updates, roadmap leaks, parity gaps, betas, teardowns, deprecations
2. **Pricing & Monetization**: Pricing/packaging changes, model shifts, discounting, benchmarks, transparency
3. **Product Strategy**: Pivots, expansions, portfolio decisions (build/buy/partner/kill), platform/ecosystem, vision
4. **UX & Design**: UI/UX patterns, accessibility, mobile/desktop, onboarding, tool updates, design systems
5. **Customer Research**: Feedback (NPS/CSAT), usage analytics, segmentation, user studies, churn, adoption
6. **Market Positioning**: Segmentation, brand positioning, category creation, analyst positioning (Gartner/G2), ICP

**News Criteria** (must meet ≥2, including #1):
1. **Recency** (MANDATORY—per freshness above)
2. **Lifecycle Impact**: ≥2 phases OR cross-phase
3. **Stakeholder Breadth**: ≥3 roles
4. **Decision Urgency**: 1-6mo action window
5. **Product Significance**: Shifts competitive/customer/market landscape
6. **Quantified Impact**: Adoption, pricing, usage, satisfaction, or market share metrics

**Answer Structure** (150-250w): News (≥1 item per freshness) + impact (≥2 phases, ≥2 roles, quantified) + decision (Build/Prioritize/Monitor/Defer/Ignore + rationale) + timeline (immediate/short/medium). Projections optional, only if high-confidence and sourced.

## II. Requirements

**Q&A**: 10-12 total | 1-2/phase | 150-250w | 100% news-driven | ≥85% ≥1 cite, ≥30% ≥2 cites | ≥2 categories + impact + decision

**Phases** (7, 1-2 Q each): Discovery, Design, Launch, Growth, Maturity, Expansion, Sunsetting

**Category %** (min coverage): Competitive 80%, Pricing 70%, Research 75%, Strategy 60%, UX 55%, Positioning 50%

**Decision** (100%): Impact (≥2 phases, ≥2 roles, quantified) + Decision (Build/Prioritize/Monitor/Defer/Ignore + rationale + alternatives) + Timeline (immediate/short/medium)

**Stakeholders** (≥8/11): CPO/VP Product, PM, Product Marketing, Competitive Intel, UX Researcher, UX Designer, Pricing Strategist, Customer Success, Data Analyst, Product Ops, Eng Lead

**References** (build before Q&A): G≥12 (100% terms/acronyms, with analogies/formulas), N≥8 (per freshness), C≥6 (competitive), P≥4 (pricing), U≥4 (UX), R≥4 (research), A≥12 (APA 7th+tag)

**Visuals**: ≥6 diagrams + ≥3 tables

**Quality Gates** (fail ANY = stop):
1. **News**: 100% cite ≥1 per freshness; 0% marketing/rumors
2. **Impact**: 100% ≥2 phases + ≥2 roles + quantified
3. **Decision**: 100% decision + rationale + timeline + criteria
4. **Sources**: ≥5 types, max 35%/type; 100% URLs valid
5. **Coverage**: ≥8/11 roles; categories per above
6. **Actionability**: 100% concrete; 0% abstract

## III. Execution

### Step 1: News Discovery & Curation

**Record generation date (YYYY-MM-DD)—calculate all news ages from this.**

1. **Domain**: Define industry/product category + date (e.g., "B2B SaaS Q4 2024")

2. **Search** (≥25-30 candidates, tiered):

   **Tier 1** (1-3d, search first): `"[Competitor/Domain] launched|released|pricing|strategy|UX|research"` + 1-3d
   
   **Tier 2** (7-14d if insufficient): Same + 7-14d
   
   **Tier 3** (2-4wks HV, 2-6mo MV/LT): Same + appropriate window

   **Sources** (whitelist):
   - **Competitive**: Product Hunt, TechCrunch, The Verge, G2, Gartner
   - **Pricing**: ProfitWell, OpenView, competitor sites, Archive.org
   - **Strategy**: Lenny's Newsletter, Product Coalition, Mind the Product, a16z
   - **UX**: Nielsen Norman, UX Collective, Smashing Mag, Figma/Adobe blogs
   - **Research**: UserTesting, Qualtrics, Pendo, Amplitude, Mixpanel
   - **Positioning**: Forrester/Gartner/G2 reports, April Dunford
   - **Tracking**: Kompyte, Crayon, Klue, competitor changelogs
   - **Avoid**: PR fluff, rumors, listicles

   **Tools**: Perplexity ("past week"), ChatGPT ("latest"), Google (`after:DATE`), Product Hunt (date filter), Archive.org

   **Age Target** (non-overlapping buckets):
   - HV: <1mo ≥85% (1-3d ≥30%), 1-2mo ≥10%, 2-4mo ≤5%
   - MV: <2mo ≥70% (1-3d ≥20%), 2-3mo ≥20%, 3-6mo ≤10%
   - LT: <3mo ≥60%, 3-6mo ≥25%, 6-9mo ≤15%
   - Overall: <1mo ≥55%, 1-2mo ≥25%, 2-4mo ≥12%, 4-6mo ≥6%, 6-9mo ≤2%

3. **Curate** (≥16: Competitive ≥5, Pricing ≥4, Strategy ≥3, UX ≥3, Research ≥5, Positioning ≥3):
   - ✅ Age per freshness
   - ✅ Whitelist OR primary source
   - ✅ ≥2 relevance criteria
   - ✅ Specific details (dates, names, numbers, metrics)
   - ✅ Not marketing/rumors

4. **Verify**: Check category/age distribution; if fail, retry earlier tiers

5. **Allocate**: 10-12 Q × 7 phases (1-2 each) × 6 categories (≥2/Q) × 11 roles (≥8 total)

### Step 2: Build References (before Q&A)

**Format**: G# (term, def+analogy/formula, context) | N# (news, source, date, cat, impact, URL) | C# (competitive, feature/pricing, analysis, URL) | P# (pricing, model, tiers, URL) | U# (UX, trend/tool, URL) | R# (research, findings, URL) | A# (APA 7th+tag)

**Citation**: Markdown reference links: `[Ref: N1][n1]` in text, `[n1]: URL` at answer end

**Floors**: G≥12 (100% terms/acronyms/metrics), N≥8, C≥6, P≥4, U≥4, R≥4, A≥12

**Glossary** (100% coverage, reader-friendly):
- **Coverage**: ALL terms/acronyms (NPS, CSAT, MAU, ICP, JTBD, etc.), metrics, concepts
- **Clarity**: Plain language, avoid circular jargon
- **Analogies**: Real-world comparisons (e.g., "Pricing anchoring = showing $100 wine first")
- **Formulas**: Calculations (e.g., "NPS = % Promoters − % Detractors")
- **Context**: Why it matters, product decisions, customer impact
- **Examples**: Real numbers

**News Entry**: **Title** (Source, MM/DD): Summary | Cat | Age | Impact | Stakeholders | URL | Justification if stale

### Step 2.5: Opportunistic Refresh (optional, skip default)

**Trigger**: Major launch/pricing shift in 24-48h affecting ≥3 Qs

**Action**: Quick search → Add 1-2 "BREAKING" items → Adjust 1-2 Qs → Document

### Step 3: Generate Q&A (batch 3-4, self-check each)

**Before**: Review glossary. Track ALL terms used. After each batch, verify 100% in glossary with analogies/formulas.

**Patterns**: "[News] implications for [Phase]+[Roles]?" | "[Pricing News]: response for [Product]?" | "[UX Trend]: adoption for [Phase]?" | "[Launch] vs [Roadmap]: prioritize for [Phase]?"

**Avoid**: Generic questions, hype, unattributed claims, stale news, technical tactics

**Structure** (150-250w):
1. **News** (~35w): What, when, who, why, cat `[Ref: N#][n#]`
2. **Impact** (~65w): ≥2 phases + quantified (adoption, usage, satisfaction, pricing, market share, parity gap)
3. **Stakeholders** (~45w): ≥2 roles + concerns + actions + authority
4. **Decision** (~55w): Build/Prioritize/Monitor/Defer/Ignore + rationale + alternatives + criteria
5. **Action** (~35w): Immediate (0-2wk), Short (2wk-2mo), Medium (2-6mo) + owner + deliverable
6. **Projections** (opt ~20w): "[Source] projects [outcome] by [time] ([confidence]). Impact: [ranges]" `[Ref: R#][r#]`
7. **Links**: Define at end: `[n1]: URL`
8. **Artifacts**: 1 diagram/table

**Self-Check**: Age OK | ≥2 phases | ≥2 roles | Decision clear | 150-250w | Quantified | ≥2/5 ≥2 cites | Artifact | Timeline | 0% hype | 100% actionable | Projections sourced | **All terms in glossary**

### Step 4: Visuals (≥6 diagrams + ≥3 tables, ≥60% referenced)

**Types**: Competitive matrices, pricing tables, roadmaps, funnels, UX libraries, journey maps, prioritization (RICE, 2×2), positioning, NPS charts, dashboards

**Format**: Mermaid (flows), Markdown tables (data), 2×2 matrices

### Step 5: Final Checks

**Refs**: 100% resolve | Age OK | Complete | G≥12 (100% terms+analogies/formulas) | N≥8 | C≥6 | P≥4 | U≥4 | R≥4 | A≥12

**Decision**: 100% decision + rationale + alternatives + criteria + timeline + metrics

**Stakeholders**: ≥8/11 | Actions + authority | Cross-role coordination

### Step 6: Validate (fail ANY = stop, fix, re-run ALL)

**Quantitative**: Floors met | Glossary 100% | 7 phases | Categories per % | ≥8/11 roles | Citations OK | Distribution OK | 5 word samples 150-250w | Visuals OK | Decision 100% | Timeline 100% | **Age per freshness**

**Qualitative**: News per freshness, 0% hype | Impact 100% ≥2 phases+roles+quantified | Decision 100% + alternatives | Source diversity ≥5 types, max 35% | Per-phase ≥1 news+analysis | Links valid | Cross-refs resolve | Quantified 100% | Actionable 100% | Evidence 100% | Projections sourced+timed | Search documented

### Step 7: Submit

**Checklist** (all YES): Validations PASS | Floors met | Glossary complete (100% terms, ≥60% analogies/formulas) | TOC complete | 0 placeholders | Visuals OK | Citations OK | Impact OK | Decision OK | Timeline OK | Categories OK | Roles OK | **Freshness OK** | Evidence 100% | URLs valid | **Dates (gen + expire=gen+2wk)** | Search documented

## IV. Validation Report

| # | Check | Measurement | Criteria | Result | Status |
|---|-------|-------------|----------|--------|--------|
| 1 | **Freshness** | HV: __%<1mo (1-3d:__%), __%<2mo \| MV: __%<2mo (1-3d:__%) \| LT: __%<3mo \| Overall: __%<2mo | Per header | | PASS/FAIL |
| 2 | **Floors** | G:__ N:__ C:__ P:__ U:__ R:__ A:__ Q:__ | ≥12,≥8,≥6,≥4,≥4,≥4,≥12,10-12 | | PASS/FAIL |
| 2a | **Glossary** | __%terms; __%analogies/formulas | 100%;≥60% | | PASS/FAIL |
| 3 | **Phases** | __/7 (1-2Q each); total__ | 7/7;12-15 | | PASS/FAIL |
| 4 | **Categories** | Comp__% Pric__% Res__% Strat__% UX__% Pos__% | ≥80,70,75,60,55,50% | | PASS/FAIL |
| 5 | **Roles** | __/11 | ≥8 | | PASS/FAIL |
| 6 | **Impact** | __% ≥2phases+2roles+quantified | 100% | | PASS/FAIL |
| 7 | **Decision** | __% decision+rationale+alts+criteria | 100% | | PASS/FAIL |
| 8 | **Timeline** | __% immediate/short/medium+owners | 100% | | PASS/FAIL |
| 9 | **Citations** | __%≥1news; __%≥1cite; __%≥2cites | 100%;≥85%;≥30% | | PASS/FAIL |
| 10 | **Distribution** | News__% Research__% Other__% | 50-70%,20-30%,10-20% | | PASS/FAIL |
| 11 | **Diversity** | Types__; max%__ | ≥5;≤35% | | PASS/FAIL |
| 12 | **Per-Phase** | __/7 ≥1news+1analysis | 7/7 | | PASS/FAIL |
| 13 | **Words** | 5 samples: __%150-250w | 100% | | PASS/FAIL |
| 14 | **Visuals** | __%ref; diag__; tab__ | ≥60%;≥6;≥3 | | PASS/FAIL |
| 15 | **Quantified** | __% measurable | 100% | | PASS/FAIL |
| 16 | **Links** | __% valid | 100% | | PASS/FAIL |
| 17 | **Cross-Refs** | __% resolve | 100% | | PASS/FAIL |
| 18 | **Actionable** | __%concrete; __%abstract | 100%;0% | | PASS/FAIL |
| 19 | **Projections** | __%attributed; __%timed | 100%;100% | | PASS/FAIL |
| 20 | **Search** | Queries:Y/N \| Whitelist:Y/N \| Cand:__ \| Accept:__% | Y;Y;≥25;50-70% | | PASS/FAIL |
| | **Meta** | Start:__ End:__ Expires:[+2wk] | | INFO |
| | **Age Dist** | <1mo__%(1-3d__%) 1-2mo__% 2-4mo__% HV__% MV__% LT__% | Per header | | INFO |
| | **OVERALL** | All checks | All PASS | | PASS/FAIL |

## V. Question Quality (≥3 fails of 9 = rewrite)

**Criteria**: News-driven (per freshness) | Lifecycle-specific (1-2 phases) | Multi-stakeholder (≥2 roles) | Multi-category (≥2) | Decision-focused | Quantified impact | Cross-phase aware | Timely | Alternative-aware | Evidence-based | Actionable

**✓ Good**: "Notion AI 40% adoption in 2wk (Oct'24)—implications for Knowledge Base roadmap?" | "Linear 3→2 tier simplification (Sep'24): SaaS PM tool response?" | "Figma AI (Q4'24): Design & Prototyping workflow impact?" | "G2 Fall'24: competitor→Leader—feature gap analysis?" | "UserTesting: 65% prefer mobile checkout (Nov'24)—Growth prioritization?"

**✗ Bad**: "How does PMF work?" (no news) | "What is NPS?" (overview) | "Build AI features?" (no trigger) | "Kubernetes 1.30" (tech ops)

## VI. Output Format

### A. TOC

```markdown
# [Domain] Product & Market Intelligence Q&A ([Period])

## Contents
1. Executive Summary (Overview | Insights | Dashboard)
2. Phase Coverage (7×6 matrix)
3. Questions by Phase: Discovery (Q1-Q2) | Design (Q3-Q4) | Launch (Q5-Q6) | Growth (Q7-Q9) | Maturity (Q10-Q11) | Expansion (Q12-Q13) | Sunsetting (Q14-Q15)
4. References: G (G1-G15) | N (N1-N10) | C (C1-C8) | P (P1-P6) | U (U1-U6) | R (R1-R6) | A (A1-A15)
5. Validation (20 checks)
```

### B. Executive Summary

**Domain**: [Category] | **Period**: [Q3-Q4'24] | **Coverage**: [# items, 6 cats]

**News**: Competitive ([#]: top 2+dates) | Pricing ([#]) | Research ([#]) | Strategy ([#]) | UX ([#]) | Positioning ([#])

**Insights**: 1. [News] ([Date]): [Impact] → [Decision] → [Timeline] (2 high-impact)

**Dashboard**: [Table: Phase | News | Action | Impact | Timeline]

**Roles**: [8-9+counts] | **Refs**: G=[#] N=[#] C=[#] P=[#] U=[#] R=[#] A=[#]

### C. Phase Overview

| # | Phase | Range | Count | Categories | News | Roles | Artifacts |
|---|-------|-------|-------|------------|------|-------|-----------|
| 1 | Discovery | Q1-Q2 | 1-2 | Research, Positioning, Competitive | [Top] | PM, UX Research, Intel | 1D+1T |
| 2 | Design | Q3-Q4 | 1-2 | UX, Research, Strategy | [Top] | PM, UX Designer, Research | 1D+1T |
| 3 | Launch | Q5-Q6 | 1-2 | Competitive, Pricing, Strategy | [Top] | PM, Marketing, Pricing | 1D+1T |
| 4 | Growth | Q7-Q9 | 2-3 | Research, Competitive, Pricing | [Top] | PM, Ops, Analyst | 1D+1T |
| 5 | Maturity | Q10-Q11 | 1-2 | Pricing, Competitive, UX | [Top] | PM, Pricing, Marketing | 1D+1T |
| 6 | Expansion | Q12-Q13 | 1-2 | Strategy, Positioning, Competitive | [Top] | CPO, PM, Marketing | 1D+1T |
| 7 | Sunsetting | Q14-Q15 | 1-2 | Strategy, Research, Competitive | [Top] | CPO, PM, CS | 1D+1T |
| | **Total** | | **12-15** | **All 6** | **10+** | **≥8/11** | **≥6D+≥3T** |

### D. Q&A Template

```markdown
### Q#: [News Question + Phase + Roles]

**Phase**: [Phase] | **Roles**: [Primary, Secondary] | **Cats**: [✓✓] | **Decision**: Y

**News** (~35w): What, when, who, why, cat [Ref: N#][n#]

**Impact** (~65w): **Phases** (≥2) | **Quantified**: Adoption% | Usage MAU/DAU | NPS/CSAT | Pricing$ | Market% | Parity Gap

**Stakeholders** (~45w): **[Role 1]**: Concerns, actions, authority | **[Role 2]**: Same

**Decision** (~55w): **Rec**: Build/Prioritize/Monitor/Defer/Ignore | **Rationale**: Why | **Alts**: 1-2 | **Success**: Targets

**Action** (~35w): **Immed (0-2wk)**: Actions+owner | **Short (2wk-2mo)**: Same | **Medium (2-6mo)**: Same

**Projections** (opt ~20w): [Source] projects [outcome] by [time] ([confidence]). Impact: [ranges] [Ref: R#][r#]

**Artifacts**: [Type]

[n1]: URL
---
```

### E. Reference Formats

**G#. Term (Acronym)**: Definition | Analogy/Formula | Context | Why | Example

**N#. Title** (Source, MM/DD): Summary | Cat | Impact | Roles | URL

**C#. Competitor Feature/Pricing** (Source, Date): Details | Analysis | Impact | URL

**P#. Company Pricing** (Source, Date): Model | Tiers | Packaging | Changes | URL

**U#. Design Trend/Tool** (Source, Date): Details | Adoption | Impact | Accessibility | URL

**R#. Title** (Firm, Date): Methodology | Findings | Insights | Confidence | URL

**A#. APA 7th [Tag]**: Author/Org. YYYY, Mon DD. *Title*. Pub. URL [Tag]

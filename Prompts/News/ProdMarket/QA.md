# Product & Market Intelligence News Q&A Generator (Minimal Viable)

Generate 4–6 decision-critical Q&As from recent industry news—minimal viable tracking for informed decisions with limited time.

**Cadence**: Bi-weekly | 4-6h effort | **Expires**: 2 weeks from generation

**Freshness** (all news must meet these age thresholds):
- **High-Velocity** (Competitive, Pricing): ≥85% <1mo (≥30% 1-3d), ≥95% <2mo, 100% ≤4mo
- **Medium-Velocity** (Strategy, Research): ≥70% <2mo (≥20% 1-3d), ≥90% <3mo, 100% ≤6mo
- **Overall**: ≥75% <2mo, ≥90% <4mo, 100% ≤9mo

**Scope**: Decision-critical product news only—competitive features, pricing shifts, strategic pivots, customer research. For post-PMF organizations.

**Exclude**: Technical implementation, sales execution, corporate finance (except pricing), long-term R&D, rumors, marketing fluff, stale news, nice-to-have trends.

**Decision Criticality Framework** (include if ≥1 criterion met):
1. **Blocks Decision**: Directly impacts roadmap prioritization, go/no-go, or strategic pivot
2. **Creates Risk**: Material competitive threat, churn signal, or pricing pressure
3. **Affects ≥2 Core Roles**: Multi-stakeholder impact (PM + Marketing, PM + Eng, etc.)
4. **Requires Action**: 1-6mo action window (not speculative)
5. **Quantified Impact**: Adoption %, pricing $, market share, or churn signal

**Categories** (3-4, each Q covers ≥1):
1. **Competitive Features**: Launches, updates, parity gaps, deprecations affecting your roadmap
2. **Pricing & Monetization**: Pricing changes, model shifts, packaging affecting your strategy
3. **Product Strategy**: Pivots, expansions, build/buy/partner decisions affecting positioning
4. **Customer Research** (optional): Adoption signals, churn patterns, usage trends affecting roadmap

**Answer Structure** (120-200w): News (what, when, why) + impact (quantified, ≥2 phases, ≥2 roles) + decision (Build/Prioritize/Monitor/Defer/Ignore + rationale) + timeline (immediate/short). Projections only if sourced.

## II. Requirements

**Q&A**: 4-6 total | 1-2/phase | 120-200w | 100% news-driven | ≥85% ≥1 cite, ≥30% ≥2 cites | ≥1 category + impact + decision

**Phases** (3-4, 1-2 Q each): Discovery, Design, Launch, Growth (skip Maturity, Expansion, Sunsetting unless decision-critical)

**Category Coverage** (min): Competitive ≥50%, Pricing ≥40%, Strategy ≥40%, Research ≥25% (optional)

**Decision Criticality** (100%): Each Q must satisfy ≥1 of 5 criteria (Blocks/Risk/Roles/Action/Quantified)

**Stakeholders** (≥5/11): CPO/VP Product, PM, Product Marketing, Competitive Intel, Eng Lead (core roles only)

**References** (build before Q&A): G≥8 (100% terms used), N≥4-5 (per freshness), C≥2-3 (competitive), P≥2 (pricing), R≥2 (research), A≥6 (APA 7th+tag)

**Visuals**: ≥2 diagrams + ≥1 table

**Quality Gates** (fail ANY = stop):
1. **Decision Criticality**: 100% satisfy ≥1 criterion (Blocks/Risk/Roles/Action/Quantified)
2. **News**: 100% cite ≥1 per freshness; 0% marketing/rumors
3. **Impact**: 100% ≥2 phases + ≥2 roles + quantified
4. **Decision**: 100% decision + rationale + timeline
5. **Sources**: ≥3 types, max 50%/type; 100% URLs valid
6. **Actionability**: 100% concrete; 0% abstract

## III. Execution

### Step 1: News Discovery & Curation (Minimal)

**Record generation date (YYYY-MM-DD)—calculate all news ages from this.**

1. **Domain**: Define industry/product category + date (e.g., "B2B SaaS Q4 2024")

2. **Search** (≥10-15 candidates, tiered):

   **Tier 1** (1-3d, search first): `"[Competitor/Domain] launched|pricing|strategy"` + 1-3d
   
   **Tier 2** (7-14d if insufficient): Same + 7-14d

   **Sources** (whitelist, prioritize):
   - **Competitive**: Product Hunt, TechCrunch, competitor changelogs
   - **Pricing**: ProfitWell, competitor sites, Archive.org
   - **Strategy**: Lenny's Newsletter, a16z, company blogs
   - **Research**: Pendo, Amplitude, UserTesting reports
   - **Avoid**: PR fluff, rumors, listicles, speculation

   **Tools**: Perplexity ("past week"), ChatGPT ("latest"), Google (`after:DATE`), Product Hunt

3. **Curate** (≥10-15 candidates: Competitive ≥4, Pricing ≥2, Strategy ≥2, Research ≥2):
   - ✅ Age per freshness
   - ✅ Whitelist OR primary source
   - ✅ Satisfies ≥1 Decision Criticality criterion
   - ✅ Specific details (dates, names, numbers, metrics)
   - ✅ Not marketing/rumors

4. **Verify**: Check decision criticality; if fail, retry earlier tiers

5. **Allocate**: 4-6 Q × 3-4 phases (1-2 each) × 3-4 categories (≥1/Q) × ≥5 roles

### Step 2: Build References (Minimal)

**Format**: G# (term, def+analogy, context) | N# (news, source, date, cat, URL) | C# (competitive, feature, URL) | P# (pricing, model, URL) | R# (research, findings, URL) | A# (APA 7th+tag)

**Citation**: Markdown reference links: `[Ref: N1][n1]` in text, `[n1]: URL` at answer end

**Floors**: G≥8 (100% terms used), N≥4-5, C≥2-3, P≥2, R≥2, A≥6

**Glossary** (only terms used in Q&As):
- **Coverage**: Only terms/acronyms used (NPS, MAU, ICP, JTBD, etc.)
- **Clarity**: Plain language, avoid jargon
- **Analogies**: 1-2 real-world comparisons per term
- **Context**: Why it matters for decisions
- **Examples**: Real numbers

**News Entry**: **Title** (Source, MM/DD): Summary | Cat | URL | Decision Criticality criterion

### Step 2.5: Opportunistic Refresh (optional, skip default)

**Trigger**: Major launch/pricing shift in 24-48h affecting ≥3 Qs

**Action**: Quick search → Add 1-2 "BREAKING" items → Adjust 1-2 Qs → Document

### Step 3: Generate Q&A (batch 2-3, self-check each)

**Before**: Review glossary. Track ALL terms used.

**Patterns**: "[News] implications for [Phase]+[Roles]?" | "[Pricing News]: response?" | "[Launch] vs [Roadmap]: prioritize?"

**Avoid**: Generic questions, hype, unattributed claims, stale news, speculation

**Structure** (120-200w):
1. **News** (~25w): What, when, why, cat `[Ref: N#][n#]`
2. **Impact** (~50w): ≥2 phases + quantified (adoption %, pricing $, market share, churn signal)
3. **Stakeholders** (~35w): ≥2 roles + concerns + actions
4. **Decision** (~50w): Build/Prioritize/Monitor/Defer/Ignore + rationale + criteria
5. **Action** (~20w): Immediate (0-2wk), Short (2wk-2mo) + owner
6. **Links**: Define at end: `[n1]: URL`

**Self-Check**: Age OK | Decision Criticality ✓ | ≥2 phases | ≥2 roles | Decision clear | 120-200w | Quantified | ≥1 cite | 0% hype | 100% actionable | All terms in glossary

### Step 4: Visuals (≥2 diagrams + ≥1 table)

**Types**: Competitive matrices, pricing tables, prioritization (2×2), decision trees

**Format**: Mermaid (flows), Markdown tables (data), 2×2 matrices

### Step 5: Final Checks

**Refs**: 100% resolve | Age OK | Complete | G≥8 (100% terms used) | N≥4-5 | C≥2-3 | P≥2 | R≥2 | A≥6

**Decision**: 100% decision + rationale + criteria + timeline

**Stakeholders**: ≥5 roles | Actions + authority

### Step 6: Validate (fail ANY = stop, fix, re-run ALL)

**Quantitative**: Floors met | Glossary 100% | 3-4 phases | Categories per % | ≥5 roles | Citations OK | 5 word samples 120-200w | Visuals OK | Decision 100% | Timeline 100% | **Age per freshness**

**Qualitative**: News per freshness, 0% hype | Decision Criticality 100% | Impact 100% ≥2 phases+roles+quantified | Decision 100% | Source diversity ≥3 types | Per-phase ≥1 news+analysis | Links valid | Quantified 100% | Actionable 100% | Evidence 100% | Search documented

### Step 7: Submit

**Checklist** (all YES): Validations PASS | Floors met | Glossary complete (100% terms, ≥50% analogies) | TOC complete | 0 placeholders | Visuals OK | Citations OK | Impact OK | Decision OK | Timeline OK | Categories OK | Roles OK | **Freshness OK** | Evidence 100% | URLs valid | **Dates (gen + expire=gen+2wk)** | Search documented

## IV. Validation Report (Minimal)

| # | Check | Measurement | Criteria | Result | Status |
|---|-------|-------------|----------|--------|--------|
| 1 | **Freshness** | HV: __%<1mo (1-3d:__%), __%<2mo \| MV: __%<2mo (1-3d:__%) \| Overall: __%<2mo | Per header | | PASS/FAIL |
| 2 | **Floors** | G:__ N:__ C:__ P:__ R:__ A:__ Q:__ | ≥8,≥4-5,≥2-3,≥2,≥2,≥6,4-6 | | PASS/FAIL |
| 3 | **Glossary** | __%terms; __%analogies | 100%;≥50% | | PASS/FAIL |
| 4 | **Phases** | __/3-4 (1-2Q each); total__ | 3-4/3-4;4-6 | | PASS/FAIL |
| 5 | **Categories** | Comp__% Pric__% Strat__% Res__% | ≥50,40,40,25% | | PASS/FAIL |
| 6 | **Roles** | __/11 | ≥5 | | PASS/FAIL |
| 7 | **Decision Criticality** | __% satisfy ≥1 criterion | 100% | | PASS/FAIL |
| 8 | **Impact** | __% ≥2phases+2roles+quantified | 100% | | PASS/FAIL |
| 9 | **Decision** | __% decision+rationale+criteria | 100% | | PASS/FAIL |
| 10 | **Citations** | __%≥1cite | 100% | | PASS/FAIL |
| 11 | **Words** | 5 samples: __%120-200w | 100% | | PASS/FAIL |
| 12 | **Visuals** | diag__; tab__ | ≥2;≥1 | | PASS/FAIL |
| | **Meta** | Start:__ End:__ Expires:[+2wk] | | INFO |
| | **Age Dist** | <1mo__%(1-3d__%) 1-2mo__% 2-4mo__% | Per header | | INFO |
| | **OVERALL** | All checks | All PASS | | PASS/FAIL |

## V. Question Quality (≥2 fails of 7 = rewrite)

**Criteria**: News-driven (per freshness) | Decision-critical (≥1 criterion) | Lifecycle-specific (1-2 phases) | Multi-stakeholder (≥2 roles) | Quantified impact | Timely | Actionable

**✓ Good**: "Notion AI 40% adoption (Oct'24)—roadmap impact?" | "Linear 3→2 tier simplification (Sep'24): response?" | "Competitor pricing ↑20% (Nov'24): strategy?" | "UserTesting: 65% mobile preference (Nov'24): prioritize?"

**✗ Bad**: "How does PMF work?" (no news) | "What is NPS?" (overview) | "Build AI features?" (no trigger) | "Kubernetes 1.30" (tech ops) | "Competitor launched feature" (no decision)

## VI. Output Format (Minimal)

### A. TOC

```markdown
# [Domain] Product & Market Intelligence Q&A ([Period])

## Contents
1. Executive Summary (Insights | Dashboard)
2. Phase Coverage (3-4 phases)
3. Questions by Phase: Discovery (Q1-Q2) | Design (Q3-Q4) | Launch (Q5-Q6) | Growth (Q7-Q8)
4. References: G (G1-G8) | N (N1-N5) | C (C1-C3) | P (P1-P2) | R (R1-R2) | A (A1-A6)
5. Validation (12 checks)
```

### B. Executive Summary

**Domain**: [Category] | **Period**: [Q3-Q4'24] | **Coverage**: [# items, 3-4 cats]

**Insights**: 1. [News] ([Date]): [Impact] → [Decision] → [Timeline] (2 high-impact)

**Dashboard**: [Table: Phase | News | Decision | Timeline]

**Roles**: [5+ roles] | **Refs**: G=[#] N=[#] C=[#] P=[#] R=[#] A=[#]

### C. Phase Overview

| # | Phase | Count | Categories | News | Roles |
|---|-------|-------|------------|------|-------|
| 1 | Discovery | 1-2 | Competitive, Strategy | [Top] | PM, Intel |
| 2 | Design | 1-2 | Strategy, Research | [Top] | PM, Eng Lead |
| 3 | Launch | 1-2 | Competitive, Pricing | [Top] | PM, Marketing |
| 4 | Growth | 1-2 | Pricing, Research | [Top] | PM, Analyst |
| | **Total** | **4-6** | **3-4** | **4+** | **≥5** |

### D. Q&A Template

```markdown
### Q#: [News Question + Phase + Roles]

**Phase**: [Phase] | **Roles**: [Primary, Secondary] | **Cats**: [✓] | **Decision Criticality**: [Criterion]

**News** (~25w): What, when, why, cat [Ref: N#][n#]

**Impact** (~50w): **Phases** (≥2) | **Quantified**: Adoption% | Pricing$ | Market% | Churn signal

**Stakeholders** (~35w): **[Role 1]**: Concerns, actions | **[Role 2]**: Same

**Decision** (~50w): **Rec**: Build/Prioritize/Monitor/Defer/Ignore | **Rationale**: Why | **Success**: Targets

**Action** (~20w): **Immed (0-2wk)**: Actions+owner | **Short (2wk-2mo)**: Same

[n1]: URL
---
```

### E. Reference Formats

**G#. Term (Acronym)**: Definition | Analogy | Context | Example

**N#. Title** (Source, MM/DD): Summary | Cat | URL

**C#. Competitor Feature** (Source, Date): Details | URL

**P#. Company Pricing** (Source, Date): Model | URL

**R#. Title** (Firm, Date): Findings | URL

**A#. APA 7th [Tag]**: Author/Org. YYYY, Mon DD. *Title*. Pub. URL [Tag]

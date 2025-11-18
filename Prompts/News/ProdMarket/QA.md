# Product & Market Intelligence News Q&A Generator

**Role**: Product intelligence analyst generating 4–6 decision-critical Q&As from recent product/market news for post-PMF organizations (≥$1M ARR, ≥20% YoY growth, ≥3 competitors, team ≥10).

**Context**: Problem: Manual news monitoring misses competitive threats, delays decisions. Scope: Product/market news analysis. Scale: 50+ news sources, 4-6 Q&As bi-weekly. Timeline: 2-week validity. Stakeholders: CPO/VP Product, PM, Product Marketing, Competitive Intel, Eng Lead, Sales Eng. Constraints: News <4mo (high-velocity), <6mo (medium-velocity).

**Setup**: Fill placeholders (`[Domain]`, `[Period]`, date, product, competitors, priorities), execute steps 1-6, output complete document (TOC, glossary, Q&As, references, validation).

**When NOT to Use**: Pre-PMF (<$1M ARR), <3 competitors, no strategic decisions, purely operational/technical, team <5.

**Freshness** (from generation date):
- **High-Velocity** (Competitive, Pricing): Majority <1mo, none >4mo
- **Medium-Velocity** (Strategy, Research): Majority <2mo, none >6mo

**Scope**: Competitive features, pricing models, strategic pivots, adoption/churn trends.

**Exclude**: Technical ops, sales execution, finance (except pricing), R&D >12mo, rumors, unverified claims.

**Key Terms**:
- **Post-PMF**: $1M+ ARR, 20%+ YoY growth; scaling from validation to optimization
- **Decision-Critical**: Blocks/enables roadmap, budget, or competitive decisions within 1-6mo
- **High-Velocity**: Competitive/pricing categories requiring <1mo freshness
- **MECE**: Mutually Exclusive, Collectively Exhaustive—no gaps or overlaps

## I. Framework

**Context Inputs** (fill before generation):
- Product: [Name], business model, value proposition
- Target: Customer segments, regions (primary + secondary)
- Scale: ARR $, users, team size
- Competitors: [List 3-7] with positioning
- Priorities: [Top 3 strategic goals for next 6mo]

**Decision Criticality** (include if ≥1, label in Q&A):
1. **[CRITICAL] Blocks Decision**: Roadmap, go/no-go, pivot
2. **[CRITICAL] Creates Risk**: Competitive threat, churn signal, pricing pressure
3. **[IMPORTANT] Multi-Stakeholder**: ≥2 roles affected
4. **[IMPORTANT] Time-Sensitive**: 1-6mo action window
5. **[IMPORTANT] Quantified Impact**: %, $, units specified

**Categories** (balance: Competitive 30%+, Pricing 25%+, Strategy 25%+, Research 20%+):
1. **Competitive**: Feature launches, updates, parity gaps
2. **Pricing**: Model changes, tier adjustments, packaging shifts
3. **Strategy**: Pivots, market expansions, partnerships
4. **Research**: Adoption rates, churn triggers, usage patterns

**Answer Structure** (all sections required):
1. **News**: Event + date (MM/DD/YYYY) + significance + category + citation
2. **Impact**: ≥2 phases + quantified metrics (%, $, units) + baseline comparison
3. **Stakeholders**: ≥2 roles, each with concern + action
4. **Decision**: ≥2 options table (cost/benefit/risk) → Recommendation + rationale + success criteria (baseline → target by date)
5. **Timeline**: Immediate (0-2wk) + Short-term (2wk-2mo), each with owners

## II. Requirements

**Output**: 4-6 Q&As | 3-4 phases covered | 1-2 Q per phase | All news-cited | All decisions actionable

**Phases**: Discovery, Design, Launch, Growth

**Stakeholders** (≥5 total): CPO/VP Product, PM, Product Marketing, Competitive Intel, Eng Lead, Sales Eng

**References**: Glossary (all terms), News (≥5), Competitive (≥2), Pricing (≥2), Research (≥2), Academic/Industry (as needed, APA format)

**Visuals**: ≥2 diagrams/matrices + ≥1 comparison table (Mermaid/Markdown)

**Quality Gates** (all PASS required):
1. **[CRITICAL] Criticality**: Every Q&A labeled with ≥1 criterion
2. **[CRITICAL] Freshness**: HV <4mo, MV <6mo, primary sources, no rumors
3. **[CRITICAL] Impact**: Every Q&A has ≥2 phases + ≥2 stakeholders + metrics with units
4. **[IMPORTANT] Decisions**: ≥2 options compared + recommendation + success criteria (baseline → target with date)
5. **[IMPORTANT] Completeness**: All terms glossarized, URLs valid, no placeholders, all actions owned

## III. Execution

### Step 1: News Discovery

1. **Record** date (YYYY-MM-DD), domain, product category
2. **Search** (prioritize <1wk: 50%+, <1mo: 30%+, <2mo: 20%):
   - Sources: Primary (changelogs, pricing pages, official blogs) > Secondary (Product Hunt, TechCrunch) > Tertiary (reports)
   - Verify rumors with ≥2 sources or exclude
3. **Curate** ≥10 items meeting: freshness threshold, ≥1 criticality criterion, category balance, metrics/dates present
4. **Map** 10 items → 4-6 Q&As across 3-4 phases (maintain category balance)

### Step 2: Build References

**Formats** (all required):
- **G#**: Term + 1-sentence definition + analogy with numbers + example
- **N#**: Title (Source, MM/DD/YYYY) + summary + category + URL
- **C#/P#/R#**: Entity + detail (Source, MM/DD/YYYY) + metric + URL
- **A#**: APA 7th + access date

**Citation**: Inline `[Ref: N1][n1]`, footer `[n1]: https://...`

**Glossary Test**: Can non-expert understand Q&As without external search? If no, add term.

### Step 3: Generate Q&A

**Question**: "[News with Date] implications for [Phase] ([≥2 Roles])?"

**Answer** (all sections):
1. **News**: Event + MM/DD/YYYY + significance + category + `[Ref: N#][n#]`
2. **Impact**: ≥2 phases + metrics (%, $, units) + baseline comparison
3. **Stakeholders**: ≥2 roles × (concern + action)
4. **Decision**: Options table (≥2 alternatives: cost/benefit/risk) → Recommendation + rationale + success criteria (baseline → target by date)
5. **Timeline**: Immediate (0-2wk, ≤3 actions) + Short-term (2wk-2mo, ≤3 actions), all with owners
6. **Links**: `[n1]: https://...`

**Avoid**: Claims without metrics, hype, unverified speculation, stale content, unattributed sources. **Flag**: "Estimated:" or "Reported (unverified):" for uncertain data.

### Step 4: Create Visuals

**Required**: ≥2 diagrams/matrices + ≥1 comparison table

**Types**: Competitive matrix (2×2), decision flowchart, options table, timeline (Mermaid gantt)

**Format**: Mermaid diagrams, Markdown tables. Label axes, add legend if >3 categories.

### Step 5: Validate

**Critical**:
- References: G (all terms), N≥5, C/P/R≥2 each, URLs valid
- Q&A: 4-6 count, 3-4 phases, criticality labeled, metrics quantified

**Important**:
- Stakeholders ≥5, category balance met, all citations present
- No placeholders, freshness met, decisions actionable

**Self-Review**: Verify metrics/dates, check contradictions, confirm glossary completeness, validate URLs, flag uncertainties.

### Step 6: Submit

**Output**: Complete document (TOC, Key Terms, Q&As, References, Validation Report with all ☑ PASS)

## IV. Validation Report

| Check | Criteria | Result | Status |
|-------|----------|--------|--------|
| **Freshness** | HV <1mo (maj), <4mo (max); MV <2mo (maj), <6mo (max) | | ☐ PASS |
| **References** | G (all terms), N≥5, C≥2, P≥2, R≥2, URLs valid | | ☐ PASS |
| **Q&A** | 4-6 total, 3-4 phases, 1-2 Q/phase | | ☐ PASS |
| **Category** | Comp 30%+, Pricing 25%+, Strategy 25%+, Research 20%+ | | ☐ PASS |
| **Stakeholders** | ≥5 roles total | | ☐ PASS |
| **Criticality** | All Q&As labeled [CRITICAL/IMPORTANT] criterion | | ☐ PASS |
| **Impact** | All have ≥2 phases + ≥2 roles + metrics (%, $, units) | | ☐ PASS |
| **Decisions** | All have ≥2 options + rec + rationale + criteria (baseline → target by date) | | ☐ PASS |
| **Citations** | All Q&As cited [Ref: X#][x#] | | ☐ PASS |
| **Visuals** | ≥2 diagrams/matrices + ≥1 table | | ☐ PASS |
| **Completeness** | No [TBD]/[TODO], all actions owned | | ☐ PASS |
| **Meta** | Gen: YYYY-MM-DD | Expires: [+2wk] | INFO |

## V. Question Quality

**Good**: News-driven (date specified) | Decision-critical (labeled) | Lifecycle-phase-specific | Multi-stakeholder (≥2 roles) | Quantified (metrics with units) | Actionable (timeline + owners)

**✓ Examples**: "Notion AI 40% adoption (10/15/2024): Design phase roadmap impact for PM + Eng Lead?" | "Linear 3→2 tier pricing shift (09/20/2024): Launch phase response for PM + Product Marketing?" | "Competitor ↑20% pricing (11/01/2024): Growth phase strategy for CPO + Competitive Intel?"

**✗ Avoid**: Generic theory without news trigger | No date specified | Pure technical ops | Vague impact without metrics | Single-role focus | No action timeline

## VI. Output Format

### A. Structure

```markdown
# [Domain] Product & Market Intelligence Q&A ([Period])

1. Executive Summary (Top 2-3 insights | Dashboard table)
2. Phase Coverage (Table: phase, count, categories, roles)
3. Q&As by Phase (4-6 total, template below)
4. References (G | N | C | P | R | A)
5. Validation Report (Table from Section IV)
```

### B. Executive Summary Template

**Domain**: [Category] | **Period**: MM/DD-MM/DD/YYYY | **Roles**: [List 5+ roles]

**Top Insights** (2-3): `[MM/DD]: [News] → [Impact %/$] → [Decision] → [Timeline]`

**Dashboard**:
| Phase | News (Date) | Decision | Timeline |
|-------|-------------|----------|----------|
| [Phase] | [Brief news] ([MM/DD]) | [Rec] | [Immediate/Short-term] |

### C. Phase Coverage Template

| Phase | Count | Categories | Primary Roles |
|-------|-------|------------|---------------|
| Discovery | 1-2 | Competitive, Strategy | PM, Competitive Intel |
| Design | 1-2 | Strategy, Research | PM, Eng Lead |
| Launch | 1-2 | Competitive, Pricing | PM, Product Marketing |
| Growth | 1-2 | Pricing, Research | PM, Data Analyst |

### D. Q&A Template

```markdown
### Q#: [News with Date] implications for [Phase] ([Role 1], [Role 2])?

**Phase**: [Phase] | **Roles**: [≥2] | **Category**: [Comp/Pricing/Strategy/Research] | **Criticality**: [CRITICAL/IMPORTANT]: [Criterion]

**News**: [Event] on [MM/DD/YYYY]. [Significance]. [Ref: N#][n#]

**Impact**: 
- **Phases**: [Phase 1]: [impact]; [Phase 2]: [impact]
- **Metrics**: [Metric 1]: X% (baseline: Y%), [Metric 2]: $Z, [Metric 3]: N units
- **Comparison**: [vs baseline/competitor]

**Stakeholders**: 
- **[Role 1]**: Concern: [specific]. Action: [concrete]
- **[Role 2]**: Concern: [specific]. Action: [concrete]

**Decision**: 

| Option | Cost | Benefit | Risk | Timeline |
|--------|------|---------|------|----------|
| [Opt 1] | [$X or Xh] | [Quantified] | [Specific] | [Xwk/Xmo] |
| [Opt 2] | [$Y or Yh] | [Quantified] | [Specific] | [Ywk/Ymo] |

**Recommendation**: [Option X]. **Rationale**: [Why] linked to [metric]. **Success**: [Metric]: A → B by [MM/DD/YYYY].

**Action**: 
- **Immediate (0-2wk)**: [Action 1] (Owner: [Role]); [Action 2] (Owner: [Role])
- **Short-term (2wk-2mo)**: [Action 1] (Owner: [Role]); [Action 2] (Owner: [Role])

**Flags** (if uncertain): "Estimated: [claim]" or "Reported (unverified): [claim]"

[n#]: https://...
---
```

### E. Reference Formats

**G#. Glossary**: `**[Term]**: [1-sentence definition]. Analogy: [with numbers]. Example: [concrete case].`
- Example: `G1. **Freemium**: Free basic + paid premium tiers. Analogy: Store samples—10% convert. Example: Slack free (≤10K msgs) vs paid ($8/user/mo, unlimited).`

**N#. News**: `**[Title]** ([Source], [MM/DD/YYYY]). [Summary]. Category: [Type]. [URL]`
- Example: `N1. **Notion AI 40% adoption** (TechCrunch, 10/15/2024). Enterprise accounts: 40% active AI usage in 3mo. Category: Research. https://...`

**C#. Competitive**: `[Competitor]: [Feature] ([Source], [MM/DD/YYYY]). [Metric]. [URL]`

**P#. Pricing**: `[Company]: [Change] ([Source], [MM/DD/YYYY]). [Old] → [New]. Impact: [metric]. [URL]`

**R#. Research**: `**[Title]** ([Firm], [MM/DD/YYYY]). Finding: [quantified]. [URL]`

**A#. Academic**: `[Last, F.] ([YYYY], [Mon DD]). *[Title]*. [Journal]. [URL] [Accessed: MM/DD/YYYY]`

## VII. Final Quality Checklist

**Verify ALL before submission:**

### Foundation
☐ Context: Date, domain, product, competitors, priorities specified  
☐ Clarity: All terms glossarized, no unexplained jargon  
☐ Precision: Metrics with units (%, $, count), dates MM/DD/YYYY  
☐ Relevance: Content supports decisions, no unconnected info  

### Scope
☐ MECE: 4 categories covered, no gaps/overlaps  
☐ Sufficiency: All Q&As have news/impact/stakeholders/decision/actions  
☐ Breadth: ≥5 roles total  
☐ Depth: ≥2 options/Q&A with cost/benefit/risk  

### Quality
☐ Significance: [CRITICAL] labeled, prioritized first  
☐ Priority: All criticality labeled (CRITICAL/IMPORTANT)  
☐ Concision: No repetition, each term defined once  
☐ Accuracy: Dates/metrics verified against sources  
☐ Credibility: All claims cited [Ref: X#][x#]  
☐ Logic: Recommendations link to metrics, no contradictions  
☐ Risk/Value: ≥2 options/decision in table  
☐ Fairness: Defer/monitor alternatives included, limitations noted  

### Format
☐ Structure: TOC → Summary → Coverage → Q&As → References → Validation  
☐ Consistency: All Q&As follow template  
☐ Visuals: ≥2 diagrams + ≥1 table  

### Validation
☐ Evidence: URLs validated, accessible  
☐ Verification: Metrics/dates cross-checked, uncertainties flagged  
☐ Practicality: All actions owned, timelines specified  
☐ Success Criteria: All recs have baseline → target by date  

**Fix fails before submission. Use Validation Report (Section IV) for tracking.**

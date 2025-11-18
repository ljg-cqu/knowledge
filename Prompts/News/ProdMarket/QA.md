# Product & Market Intelligence News Q&A Generator

## Table of Contents
1. [Context & Setup](#i-context--setup)
2. [Framework](#ii-framework)
3. [Execution](#iii-execution)
4. [Output Format](#iv-output-format)
5. [Validation](#v-validation)

## I. Context & Setup

**Problem**: Manual monitoring misses threats. **Scope**: Generate 4-6 decision-critical Q&As from product/market news for CPO/VP Product, PM, Product Marketing, Competitive Intel, Eng Lead, Sales Eng. 50+ sources, bi-weekly, 2wk validity. Post-PMF orgs (≥$1M ARR, ≥20% YoY growth, ≥3 competitors, team ≥10).

**Prerequisites**: Fill `[Domain]`, `[Period]`, date, product, competitors, priorities before Step 1.

**Exclude**: Pre-PMF (<$1M ARR), <3 competitors, purely operational/technical, team <5, technical ops, sales execution, finance (except pricing), R&D >12mo, rumors, unverified claims.

**Key Terms**:
- **Post-PMF**: $1M+ ARR, 20%+ YoY growth. Example: Slack at $1M ARR (2014) adding enterprise features.
- **Decision-Critical**: Blocks/enables roadmap/budget/competitive decisions within 1-6mo. Example: Competitor AI feature blocks Q3 roadmap.
- **High-Velocity**: Competitive/pricing requiring <1mo freshness (expires 4wk).
- **Medium-Velocity**: Strategy/research requiring <2mo freshness (expires 24wk).
- **MECE**: Mutually Exclusive, Collectively Exhaustive—no gaps/overlaps.
- **Product Lifecycle Phases**: Discovery (research/validate), Design (spec/prioritize), Launch (build/release), Growth (scale/optimize).

**Freshness**: High-Velocity (Competitive, Pricing) majority <1mo, none >4mo | Medium-Velocity (Strategy, Research) majority <2mo, none >6mo.

## II. Framework

**Context Inputs** (fill before Step 1): Product, business model, value proposition | Target (customer segments, regions) | Scale (ARR $, users, team size) | Competitors ([List 3-7] with positioning) | Priorities ([Top 3 strategic goals, 6mo]).

**Output**: 4-6 Q&As (150-200w each) across 3-4 phases (1-2 Q/phase), ≥5 stakeholders total, all news-cited, all decisions actionable.

**Categories** (distribute 4-6 Q&As across all 4, ≥1 each): Competitive (feature launches, updates, parity gaps) | Pricing (model changes, tier adjustments, packaging shifts) | Strategy (pivots, market expansions, partnerships) | Research (adoption rates, churn triggers, usage patterns).

**Criticality Criteria** (≥1 per Q&A): **[CRITICAL]** Blocks decision (roadmap, go/no-go, pivot) OR creates risk (competitive threat, churn signal, pricing pressure) | **[IMPORTANT]** Multi-stakeholder (≥2 roles) OR time-sensitive (1-6mo) OR quantified impact (%, $, units).

**Q&A Structure**: News (event + date MM/DD/YYYY + significance + category + `[Ref: N#][n#]`) | Impact (≥2 phases + metrics %, $, units + baseline comparison) | Stakeholders (≥2 roles × concern + action) | Decision (≥2 options table cost/benefit/risk → Recommendation + rationale + success criteria baseline → target by date) | Timeline (Immediate 0-2wk ≤3 actions + Short-term 2wk-2mo ≤3 actions, all with owners).

**References**: G# (all terms + 1-sentence definition + analogy with numbers + example) | N≥5 (title, source, MM/DD/YYYY, summary, category, URL) | C/P/R≥2 each (competitive/pricing/research: entity, detail, metric, URL) | A# as needed (APA 7th + access date).

**Visuals**: ≥2 diagrams/matrices (Mermaid) + ≥1 comparison table (Markdown).

## III. Execution

### Step 1: News Discovery

1. **Record** date (YYYY-MM-DD), domain, product category
2. **Search** (prioritize <1wk: 50%+, <1mo: 30%+, <2mo: 20%):
   - Sources: Primary (changelogs, pricing pages, official blogs) > Secondary (Product Hunt, TechCrunch) > Tertiary (reports)
   - Verify rumors with ≥2 sources or exclude
3. **Curate** ≥10 items: freshness threshold, ≥1 criticality criterion, category balance, metrics/dates present
4. **Map** 10 items → 4-6 Q&As across 3-4 phases (maintain category balance)

### Step 2: Build References

**Citation**: Inline `[Ref: N1][n1]`, footer `[n1]: https://...`

**Formats**:
- **G#**: `**[Term]**: [1-sentence definition]. Analogy: [with numbers]. Example: [concrete].`
- **N#**: `**[Title]** ([Source], [MM/DD/YYYY]). [Summary]. Category: [Type]. [URL]`
- **C#/P#/R#**: `[Entity]: [Detail] ([Source], [MM/DD/YYYY]). [Metric]. [URL]`
- **A#**: `[Last, F.] ([YYYY], [Mon DD]). *[Title]*. [Journal]. [URL] [Accessed: MM/DD/YYYY]`

**Test**: Can non-expert understand Q&As without external search?

### Step 3: Generate Q&A

**Question Format**: `"[News with Date] implications for [Phase] ([≥2 Roles])?"`

**Answer Sections** (all required):
1. **News**: Event + MM/DD/YYYY + significance + category + `[Ref: N#][n#]`
2. **Impact**: ≥2 phases + metrics (%, $, units) + baseline comparison
3. **Stakeholders**: ≥2 roles × (concern + action)
4. **Decision**: ≥2 options table (cost/benefit/risk) → Recommendation + rationale + success criteria (baseline → target by date)
5. **Timeline**: Immediate (0-2wk) + Short-term (2wk-2mo), all with owners
6. **Links**: `[n1]: https://...`

**Avoid**: Claims without metrics, hype, unverified speculation, stale content, unattributed sources.

**Flag Uncertainty**: "Estimated: [claim]" or "Reported (unverified): [claim]"

### Step 4: Create Visuals

**Required**: ≥2 diagrams/matrices (competitive 2×2, decision flowchart, timeline Mermaid gantt) + ≥1 comparison table (Markdown)

**Format**: Label axes, add legend if >3 categories

### Step 5: Validate & Submit

**Self-Review**: Verify metrics/dates, check contradictions, confirm glossary completeness, validate URLs, flag uncertainties

**Critical Checks**:
- References: G (all terms), N≥5, C/P/R≥2 each, URLs valid
- Q&A: 4-6 count, 3-4 phases, criticality labeled, metrics quantified
- Stakeholders ≥5, category balance met, all citations present, no placeholders

**Output**: Complete document (TOC, Key Terms, Q&As, References, Validation Report with all ☑ PASS)

## IV. Output Format

### Document Structure

```markdown
# [Domain] Product & Market Intelligence Q&A ([Period])

1. Executive Summary (2-3 insights, dashboard table)
2. Q&As by Phase (4-6 total)
3. References (G, N, C, P, R, A)
4. Validation Report
```

### Executive Summary

**Domain**: [Category] | **Period**: MM/DD-MM/DD/YYYY | **Roles**: [5+ roles]

**Top Insights** (2-3): `[MM/DD]: [News] → [Impact %/$] → [Decision] → [Timeline]`

**Dashboard**:
| Phase | News (Date) | Decision | Timeline |
|-------|-------------|----------|----------|
| [Phase] | [Brief] ([MM/DD]) | [Rec] | [Immediate/Short] |

### Q&A Template

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

**Flags** (if applicable): "Estimated: [claim]" or "Reported (unverified): [claim]"

[n#]: https://...
---
```

## V. Validation

### Validation Report Template

| Check | Criteria | Result | Status |
|-------|----------|--------|--------|
| **[CRITICAL] Freshness** | HV <1mo (maj), <4mo (max); MV <2mo (maj), <6mo (max) | | ☐ PASS |
| **[CRITICAL] References** | G (all terms), N≥5, C≥2, P≥2, R≥2, URLs valid | | ☐ PASS |
| **[CRITICAL] Impact** | All have ≥2 phases + ≥2 roles + metrics (%, $, units) | | ☐ PASS |
| **[IMPORTANT] Q&A** | 4-6 total, 3-4 phases, 1-2 Q/phase | | ☐ PASS |
| **[IMPORTANT] Category** | All 4 categories covered: Comp≥1, Pricing≥1, Strategy≥1, Research≥1 | | ☐ PASS |
| **[IMPORTANT] Stakeholders** | ≥5 roles total | | ☐ PASS |
| **[IMPORTANT] Criticality** | All Q&As labeled [CRITICAL/IMPORTANT] criterion | | ☐ PASS |
| **[IMPORTANT] Decisions** | All have ≥2 options + rec + rationale + criteria (baseline → target by date) | | ☐ PASS |
| **[IMPORTANT] Citations** | All Q&As cited [Ref: X#][x#] | | ☐ PASS |
| **[IMPORTANT] Visuals** | ≥2 diagrams/matrices + ≥1 table | | ☐ PASS |
| **[IMPORTANT] Completeness** | No [TBD]/[TODO], all actions owned | | ☐ PASS |
| **[IMPORTANT] Word Count** | All Q&As within 150-200w | | ☐ PASS |
| **Meta** | Gen: YYYY-MM-DD \| Expires: [+2wk] | | INFO |

### Quick Checklist

**Before submission**:
☐ Context: Date, domain, product, competitors, priorities specified  
☐ Clarity: All terms glossarized (G#), no unexplained jargon  
☐ Precision: Metrics with units (%, $, count), dates MM/DD/YYYY  
☐ MECE: 4 categories covered, no gaps/overlaps  
☐ Criticality: All Q&As labeled [CRITICAL/IMPORTANT]  
☐ Evidence: URLs validated, uncertainties flagged  
☐ Practicality: All actions owned, timelines specified  
☐ Success Criteria: All recs have baseline → target by date

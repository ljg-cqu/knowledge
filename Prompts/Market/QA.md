# LLM Prompt Template: Interview Q&A - Marketing Professional

**Purpose**: Generate comprehensive interview Q&A pairs for senior/director/VP marketing roles.

**Usage**: Copy entire template into LLM interface. Output follows **Output Format** section.

---

## Table of Contents

- [Purpose and Scope](#purpose-and-scope)
- [Success Criteria](#success-criteria)
- [Accuracy and Verification](#accuracy-and-verification)
- [Terminology Key](#terminology-key)
- [Marketing Domains (MECE)](#marketing-domains-mece)
- [Evidence and References](#evidence-and-references)
- [Requirements](#requirements)
  - [Deliverable Specifications](#deliverable-specifications)
  - [Depth by Difficulty Level](#depth-by-difficulty-level)
  - [Breadth and Fairness](#breadth-and-fairness)
  - [Question Prioritization](#question-prioritization)
  - [Required Answer Structure](#required-answer-structure)
- [Instructions](#instructions)
  - [Step 1: Topic Planning](#step-1-topic-planning)
  - [Step 2: Reference Collection](#step-2-reference-collection)
  - [Step 3: Q&A Generation](#step-3-qa-generation)
  - [Step 4: Artifacts](#step-4-artifacts)
  - [Step 5: Reference Sections](#step-5-reference-sections)
  - [Step 6: Validation](#step-6-validation)
  - [Step 7: Final Review](#step-7-final-review)
- [Validation Checklist](#validation-checklist)
- [Common Pitfalls](#common-pitfalls)
- [Output Format](#output-format)
- [Example Q&A Pair](#example-qa-pair)

---

## Purpose and Scope

**Output**: 25–30 interview Q&A pairs with validated references, artifacts, and evidence for senior marketing roles.

**Target**: Senior Marketing Manager, Director, VP Marketing evaluated by cross-functional leaders.

**Assumptions**:
- LLM has access to current information, datasets, benchmarks
- Citations are verifiable using authoritative sources
- Scenarios use realistic, anonymized data
- Standard marketing tools/frameworks available

**Constraints**:
- Word count: 150–300 per answer
- Languages: EN 50–70%, ZH 20–40%, Other 5–15%
- Recency: ≥50% sources <3yr (≥70% for digital/social)
- Coverage: MECE across 6 marketing domains

---

## Success Criteria

**MANDATORY**: All criteria must be satisfied.

### Quantitative Floors

| Criterion | Requirement | Notes |
|-----------|-------------|-------|
| **Total Q&A pairs** | 25–30 pairs | Exact count within this range |
| **Difficulty distribution** | 20% F, 40% I, 40% A (±5 percentage points absolute) | Across entire set |
| **Judgment questions** | At least 70% scenario-based | Not recall/definition questions |
| **Answer word count** | 150–300 words each | Sample 5 to verify |
| **Citation coverage (≥1)** | At least 70% of answers | Include at least one [Ref: ID] |
| **Citation coverage (≥2)** | At least 30% of answers | Include at least two [Ref: ID] |
| **Limitations acknowledged** | At least 50% of answers | State trade-offs, constraints, when not to use |
| **Logical explanation** | At least 60% of answers | Explicit reasoning chain |
| **Framework accuracy** | At least 80% correct | Must cite sources and note limitations |
| **Artifacts per cluster** | At least 1 diagram + 1 table per topic cluster | Journey maps, positioning maps, funnels, dashboards |

### Reference Floors (Minimum Counts)

| Reference Type | Minimum | Example IDs | Notes |
|----------------|---------|-------------|-------|
| **Glossary** | At least 10 entries | G1, G2, ..., G10+ | STP, 4Ps, AIDA, CAC, LTV, Attribution, Brand Equity, Segmentation, MQL, ABM |
| **Tools** | At least 5 entries | T1, T2, ..., T5+ | Include pricing, user count, integrations, update date (≤18 months old) |
| **Literature** | At least 6 entries | L1, L2, ..., L6+ | EN + ZH authoritative texts (Kotler, Ries & Trout, Godin, etc.) |
| **APA Citations** | At least 12 entries | A1, A2, ..., A12+ | Language tags [EN]/[ZH], unique IDs |

**Scaling Rule**: If generating >30 Q&A pairs, multiply all reference floors by 1.5

### Quality Gates

| Gate | Requirement | Action if FAIL |
|------|-------------|----------------|
| **Language mix** | EN 50–70%, ZH 20–40%, Other 5–15% | Stop, fix, re-validate |
| **Recency** | At least 50% sources <3 years (70% for digital/social) | Stop, fix, re-validate |
| **Source diversity** | At least 3 types, no source >25% of total | Stop, fix, re-validate |
| **Cross-reference integrity** | All [Ref: ID] resolve to entries | Stop, fix, re-validate |
| **Link accessibility** | All URLs accessible or archived (prefer DOIs) | Stop, fix, re-validate |
| **Per-topic depth** | At least 2 authoritative sources + 1 tool per cluster | Stop, fix, re-validate |
| **17-step validation** | All checks PASS | Stop, fix, re-validate |

### Strategic Quality

- **Key Insights**: All must be concrete (opportunity, trade-off, conflict, or challenge), non-obvious, decision-useful, falsifiable
- **Balance**: Answers should acknowledge alternatives, limitations, biases, and counterarguments
- **Reasoning**: Logical flow from diagnosis → analysis → recommendations → limitations
- **Practicality**: Recommendations must be actionable with clear implementation steps

---

## Accuracy and Verification

### Verification Standards

| Element | Requirement |
|---------|-------------|
| **Statistics** | Cross-check with ≥2 independent authoritative sources |
| **Frameworks** | Verify definitions, components, context against original sources |
| **Tool specs** | Confirm pricing, features, integrations, update dates from official docs |
| **Definitions** | Match industry-standard usage |
| **Novel/critical claims** | ≥2 independent authoritative sources |
| **Uncertain info** | Flag with qualifiers ("likely", "emerging evidence", "preliminary data") |
| **Conflicting sources** | Cite both perspectives |
| **Outdated info** | State publication date, note if superseded |

**Source Authority**: See **Evidence and References** section.

---

## Terminology Key

| Term | Definition | % Distribution |
|------|------------|----------------|
| **Q&A pair** | Single question with answer | - |
| **Topic cluster** | 4–6 Q&A pairs within one marketing domain | - |
| **Marketing domain** | One of six MECE categories | - |
| **Difficulty F** | Foundational knowledge | 20% |
| **Difficulty I** | Intermediate application | 40% |
| **Difficulty A** | Advanced judgment | 40% |
| **Floor** | Minimum threshold (≥N) | - |
| **Quality gate** | Stop-and-fix checkpoint | - |

### Marketing Acronyms

| Acronym | Full Term | Use in Context |
|---------|-----------|----------------|
| **STP** | Segmentation, Targeting, Positioning | Market entry, launches, strategy |
| **CAC** | Customer Acquisition Cost | (Sales + Marketing) / New Customers |
| **LTV** | Lifetime Value | ARPU × Lifespan or (ARPU × Margin) / Churn. Healthy ratio: LTV:CAC ≥ 3:1 |
| **MQL** | Marketing Qualified Lead | Lead scoring, funnel management, sales alignment |
| **SQL** | Sales Qualified Lead | Handoff from marketing to sales |
| **ABM** | Account-Based Marketing | B2B targeted account strategy |
| **JTBD** | Jobs-to-be-Done | Customer motivation framework (Christensen) |
| **MTA** | Multi-Touch Attribution | Credit allocation across touchpoints |
| **MMM** | Marketing Mix Modeling | Econometric analysis of channel effectiveness |
| **Brand Equity** | Value premium from brand | Measured by awareness, associations, quality, loyalty |

---

## Marketing Domains (MECE)

**Six domains are Mutually Exclusive and Collectively Exhaustive** for senior marketing competencies.

### Domain Definitions

| # | Domain | Rationale | Covers |
|---|--------|-----------|--------|
| **1** | Market Research & Analysis | **Insights foundation** | Market sizing, competitive intelligence, trend analysis, customer research, opportunity identification |
| **2** | Marketing Strategy & Planning | **Strategic direction** | GTM strategy, positioning strategy, budget allocation, portfolio management, growth planning |
| **3** | Brand Positioning & Messaging | **Brand foundation** | Brand identity, value proposition, messaging hierarchy, differentiation, brand architecture |
| **4** | Customer Segmentation & Targeting | **Audience definition** | Segmentation frameworks, persona development, targeting criteria, segment prioritization |
| **5** | Marketing Channels & Campaign Management | **Tactical execution** | Channel selection, campaign planning, content strategy, media buying, marketing operations |
| **6** | Marketing Metrics & Analytics | **Performance measurement** | KPI definition, attribution modeling, ROI analysis, dashboard design, experimentation |

### Domain Boundaries

| Domain | Includes | Excludes | Example |
|--------|----------|----------|---------|
| **Market Research & Analysis** | Primary research, secondary research, competitive analysis, market segmentation research | Execution of marketing campaigns, brand messaging creation | "How do you design a conjoint analysis study?" ✅ |
| **Marketing Strategy & Planning** | Portfolio strategy, market entry, budget allocation, strategic partnerships | Day-to-day campaign execution, tactical channel management | "How do you allocate budget across awareness vs. demand gen?" ✅ |
| **Brand Positioning & Messaging** | Brand promise, taglines, messaging frameworks, brand guidelines | Media buying, performance optimization, analytics | "How do you reposition a B2C brand for B2B?" ✅ |
| **Customer Segmentation & Targeting** | Persona creation, RFM analysis, lookalike modeling, segment sizing | Campaign creative, channel tactics, attribution | "How do you prioritize segments when resources are limited?" ✅ |
| **Channels & Campaign Management** | Channel mix, campaign orchestration, content calendars, marketing automation | Strategic planning, brand positioning, market research | "How do you rebalance paid vs. organic when CAC spikes?" ✅ |
| **Metrics & Analytics** | Attribution, experimentation, forecasting, reporting | Market research, brand identity, campaign creative | "When does multi-touch attribution mislead?" ✅ |

---

## Evidence and References

### Source Quality Hierarchy

Prioritize sources in this order (highest to lowest authority):

1. **Tier 1: Peer-reviewed and standards**
   - Academic journals (Journal of Marketing, Marketing Science, etc.)
   - Industry standards bodies (AMA, IAB, MMA)
   - Peer-reviewed conference proceedings
   
2. **Tier 2: Government and official statistics**
   - Census data, labor statistics, trade statistics
   - Regulatory bodies (FTC, SEC for public company data)
   
3. **Tier 3: Top-tier industry research**
   - McKinsey, BCG, Bain, Forrester, Gartner, HBR
   - Well-established industry reports (Edelman Trust Barometer, etc.)
   
4. **Tier 4: Vendor primary documentation**
   - Official tool documentation (Google Analytics docs, HubSpot Academy, etc.)
   - Vendor-published case studies and white papers
   
5. **Tier 5: Reputable trade publications**
   - Marketing Week, AdAge, Marketing Land, Digiday, Chief Marketer
   
6. **Tier 6: Blogs and community**
   - Recognized practitioner blogs (Seth Godin, Rand Fishkin, etc.)
   - Community surveys (State of Marketing reports from vendors)

### Authority Criteria for Marketing

A source is considered **authoritative** if it meets at least one criterion:

- **Academic**: Published in peer-reviewed marketing journal or by university press
- **Practitioner**: Author has 10+ years senior marketing leadership experience at recognized brands
- **Framework originator**: Source is the original publication of a widely-adopted framework (e.g., Kotler for 4Ps, Ries & Trout for Positioning)
- **Data-backed**: Contains original research with disclosed methodology and sample size
- **Industry standard**: Cited by multiple independent authoritative sources

### Reference Floors and Distribution

See **Success Criteria** section above for minimum counts. Ensure:

- **Language distribution**: EN 50–70%, ZH 20–40%, Other 5–15%
- **Type diversity**: Use at least 3 types (G#, T#, L#, A#)
- **Source concentration**: No single author or source >25% of total citations
- **Per-cluster depth**: Each topic cluster cites at least 2 authoritative sources + 1 tool

### Flagging Uncertainty

When information is uncertain or emerging:

- Use qualifiers: "Preliminary evidence suggests...", "Emerging research indicates...", "This is contested; Source A argues X while Source B argues Y"
- Cite confidence level if quantified: "A 2024 survey (n=500) found...", "Limited evidence (2 case studies) suggests..."
- Note when data is outdated: "As of 2020 data (most recent available)..."

### Citation Format

- **Inline citations**: `[Ref: ID]` where ID = G#, T#, L#, or A#
- **APA 7th edition** for full references:
  - Books: `Author, A. (Year). *Title* (Ed.). Publisher. [EN]`
  - Articles: `Author, A. (Year). Title. *Journal*, Vol(Issue), Pages. DOI [EN]`
  - Tools: Include pricing, user count, integrations, last update date (must be ≤18 months old)

---

## Requirements

### Deliverable Specifications

| Specification | Value | Enforcement |
|---------------|-------|-------------|
| **Total Q&A pairs** | 25–30 | Exact count within range |
| **Topic clusters** | 5–6 clusters | Each cluster = 4–6 Q&A pairs |
| **Difficulty distribution (entire set)** | F: 20%, I: 40%, A: 40% (±5 percentage points absolute) | Measure across all Q&A |
| **Word count per answer** | 150–300 words | Sample 5 answers to verify compliance |
| **Scenario-based questions** | At least 70% | "How would you...", "You observe X, what's your diagnosis?" |
| **Artifacts per cluster** | At least 1 diagram + 1 table | Journey maps, positioning matrices, funnel diagrams, dashboards |

### Depth by Difficulty Level

| Level | % | Knowledge Depth | Analytical Expectations | Scenario Complexity | Data Usage | Frameworks | Theory:Practice Ratio | Min Elements |
|-------|---|-----------------|------------------------|---------------------|------------|------------|-----------------------|--------------|
| **F** (Foundational) | 20% | Recall and explain core concepts | Identify and describe | Single variable, clear constraints | Provided, clean | Name and explain 1–2 standard frameworks | 60% theory, 40% practice | 2-step reasoning, 1 framework, 1 limitation |
| **I** (Intermediate) | 40% | Apply frameworks to realistic scenarios | Diagnose and compare | 2–3 variables, ambiguous constraints | Provided, requires cleaning or inference | Apply 2–3 frameworks, compare trade-offs | 40% theory, 60% practice | 3-step reasoning, 2 frameworks, trade-off analysis, 2 limitations |
| **A** (Advanced) | 40% | Synthesize multiple frameworks, create new approaches | Evaluate, recommend, justify | Multi-variate, conflicting constraints, stakeholder trade-offs | Missing, must estimate or gather | Synthesize 3+ frameworks, critique limitations, adapt to context | 20% theory, 80% practice | 4–5 step reasoning, 3+ frameworks, alternative approaches, implementation roadmap, 3+ limitations |

### Examples by Difficulty Level

#### Foundational (F) Example

**Question**: What is the STP framework and when is it used in marketing strategy?

**Insufficient Answer**: "STP stands for Segmentation, Targeting, Positioning. It helps marketers."

**Sufficient Answer**:
> STP is a three-stage framework [Ref: G1, L1] for market strategy: (1) **Segmentation** divides the market into distinct groups based on demographics, psychographics, behavior, or needs [Ref: G8]; (2) **Targeting** evaluates and selects which segments to serve based on attractiveness and fit; (3) **Positioning** defines how the brand will be perceived relative to competitors in the target segment's mind [Ref: L2].
>
> **When to use**: Market entry, new product launches, rebranding, or portfolio strategy [Ref: L1]. STP is most effective for differentiated strategies in fragmented markets.
>
> **Limitations**: STP assumes segments are stable and identifiable, which may not hold in rapidly evolving or highly personalized markets [Ref: L4].

*(~120 words; meets 150–300 floor with Key Insight addition)*

#### Intermediate (I) Example

**Question**: Your B2B SaaS product has CAC of $1,200 and LTV of $3,800 (LTV:CAC = 3.2:1). Marketing wants to expand to mid-market from SMB. How do you assess feasibility?

**Insufficient Answer**: "Calculate the new CAC and LTV for mid-market and compare."

**Sufficient Answer**:
> **Analysis**: Current LTV:CAC of 3.2:1 is healthy [Ref: G5, L1]. Mid-market expansion must maintain or improve this ratio. Key variables: (1) CAC likely increases due to longer sales cycles, more touchpoints, and senior buyer involvement [Ref: A11]; (2) LTV may increase due to higher ARPU and lower churn, but requires validation [Ref: G5].
>
> **Approach**: (1) **Benchmark**: Research mid-market CAC and LTV from comparable SaaS companies [Ref: T3, public data]; (2) **Pilot**: Run a 3-month test with 20 mid-market accounts to measure actual CAC and early retention signals [Ref: L5]; (3) **Model**: Build a cohort model projecting 12-month LTV based on pilot data, accounting for longer payback period.
>
> **Decision criteria**: Proceed if pilot shows LTV:CAC ≥ 3:1 and payback < 18 months [Ref: G4, G5].
>
> **Limitations**: Mid-market requires different positioning [Ref: G1, L2], sales infrastructure, and product capabilities—CAC alone doesn't capture readiness. Pilot may not represent full mid-market due to selection bias.

*(~185 words, meets requirements)*

#### Advanced (A) Example

**Question**: Your CMO role includes a $10M budget, declining brand awareness (-8 pts YoY), but increasing performance marketing efficiency (+15% ROAS YoY). The CEO wants "more performance marketing." How do you respond and what strategy do you propose?

**Insufficient Answer**: "Explain that brand and performance marketing both matter and need balance."

**Sufficient Answer**:
> **Context**: Performance marketing is cannibalizing brand-built demand. Short-term ROAS gains mask long-term brand decay—a classic "efficiency trap" [Ref: L4, A10].
>
> **Diagnosis**: Declining awareness indicates shrinking consideration set. Performance marketing captures existing demand but doesn't create it [Ref: L4]. Improved ROAS likely reflects attribution bias (last-click over-credits bottom-funnel) [Ref: G6, A12] and diminishing competition as brand competitors invest in awareness.
>
> **Response to CEO**: "Performance gains are real but unsustainable. We're harvesting brand equity faster than we're building it. I propose a balanced strategy targeting 60/40 brand/performance split [Ref: L4, A10], measured by a dual KPI system."
>
> **Strategy**: (1) **Immediate** (Q1–Q2): Maintain performance spend but shift 20% budget to brand (video, sponsorships, PR) [Ref: L3]; test brand lift measurement [Ref: T1]; (2) **Medium-term** (Q3–Q4): Launch brand campaign targeting awareness +5 pts; measure incrementality via geo holdouts [Ref: A11]; (3) **Long-term** (Year 2): Rebalance to 60/40 based on lift studies and sales correlation [Ref: G6, L1].
>
> **Alternatives**: Maintain 100% performance if competitive pressure low and market share growth is the priority. However, this risks commoditization.
>
> **When NOT to use**: Early-stage startups with no brand equity should prioritize performance until product-market fit is proven [Ref: L5].
>
> **Limitations**: Brand effects have 6–18 month lag [Ref: L4, A10]. Short-term ROAS will dip. Requires CEO buy-in on dual metrics and patience.

*(~285 words, meets requirements)*

### Breadth and Fairness

#### Breadth: Address Multiple Perspectives

| Dimension | Perspective A | Perspective B |
|-----------|---------------|---------------|
| **Strategy** | Brand building (long-term equity) | Performance marketing (short-term conversion) |
| **Market** | B2B (relationships, ABM, long cycles) | B2C (transactions, mass, emotional) |
| **Distribution** | DTC (owned data, brand control) | Marketplace (platform, lower CAC, network effects) |
| **Geography** | Global (standardized, efficient) | Local (cultural adaptation, relevant) |

#### Fairness: Include in Every Answer

1. Alternative frameworks: "Another approach...", "Traditional wisdom... but recent research..."
2. When NOT to use: State constraints and exceptions
3. Potential biases: Source bias, attribution bias, recency bias with [Ref: ID]
4. Counterarguments: "Source A recommends X; Source B argues Y because..."

### Question Prioritization

| Priority | Question Type | Examples |
|----------|---------------|----------|
| **High** | Judgment, trade-offs, resource allocation, multi-variate | Budget allocation under constraints |
| **Medium** | Framework application, diagnosis, comparison | Apply STP to new market |
| **Low** | Recall, single-step tactics | List AIDA stages |

**Key Insight**: One sentence per Q&A, must be:
- Non-obvious (not textbook definition)
- Decision-useful (actionable guidance)
- Falsifiable (testable with evidence)
- Concrete (specific opportunity/trade-off/conflict/challenge)

**Example**: ✅ "Tests diagnosis of efficiency vs. effectiveness trade-offs; distinguishes strategists balancing short-term ROAS with long-term brand equity" | ❌ "About marketing strategy"

### Required Answer Structure

Every answer must follow this structure:

1. **Context and Problem Framing** (1–2 sentences)
   - Restate the scenario and key challenge
   
2. **Analysis and Assumptions** (2–3 sentences)
   - Diagnose root causes using frameworks [Ref: ID]
   - State key assumptions (market conditions, data availability, resources)
   
3. **Reasoning Chain** (3–4 sentences)
   - Explain your logical approach step-by-step
   - Cite frameworks and evidence [Ref: ID]
   
4. **Recommendations and Alternatives** (3–4 sentences)
   - Provide actionable steps with priorities
   - Note trade-offs between options
   - Cite best practices [Ref: ID]
   
5. **Implementation Steps and Dependencies** (2–3 sentences, optional for F-level)
   - Sequence of actions with timelines
   - Required resources or preconditions
   
6. **Metrics and Expected Impact** (1–2 sentences, optional for F-level)
   - How to measure success
   - Projected outcomes
   
7. **Risks and Limitations** (2–3 sentences)
   - Constraints of the approach
   - When NOT to use this approach
   - Uncertainty and dependencies
   
8. **Evidence and Citations**
   - Inline [Ref: ID] throughout answer
   - At least 1 citation (70% of answers), at least 2 citations (30% of answers)
   
9. **Key Insight** (included in question section)
   - One-sentence, non-obvious, decision-useful insight

---

## Instructions

### Step 1: Topic Planning

1. Select 5–6 topic clusters from six marketing domains
2. Allocate 4–6 Q&A pairs per cluster (total 25–30)
3. Assign difficulty: F 20%, I 40%, A 40% (±5pp)

**✓ Checkpoint**: Total = 25–30, difficulty ≈ 20/40/40 (±5pp)

### Step 2: Reference Collection

**Collect and verify ALL references before Q&A generation**:

| Type | Floor | Requirements |
|------|-------|-------------|
| **Glossary (G#)** | ≥10 | Define terms with usage context |
| **Tools (T#)** | ≥5 | Pricing, users, integrations, update ≤18mo |
| **Literature (L#)** | ≥6 | EN+ZH authoritative texts |
| **APA Citations (A#)** | ≥12 | Unique IDs, language tags [EN]/[ZH] |

**✓ Checkpoint**: Floors met? Language mix (EN 50–70%, ZH 20–40%, Other 5–15%)? Recency (≥50% <3yr, ≥70% digital)? Types (≥3)? Source concentration (<25%)?

### Step 3: Q&A Generation

#### Questions
- Format: Scenario-based ("How would you...", "You observe X...")
- Clarity: Single ask, no compounds
- Judgment: Test decision-making (≥70% scenario-based)
- Seniority: Senior (execution/analysis), Director (strategy/cross-functional), VP (vision/revenue/board)

#### Answers (150–300 words)

Follow **Required Answer Structure**: Analysis [Ref: ID] → Reasoning [Ref: ID] → Recommendations [Ref: ID] → Limitations (constraints, when NOT to use).

**✓ Checkpoint** (every 5 Q&A):
- Word count 150–300?
- Citations: ≥70% have ≥1, ≥30% have ≥2?
- Key Insights: Non-obvious, decision-useful?
- Limitations and trade-offs included?
- Multiple perspectives (brand vs. performance, B2B vs. B2C)?

#### Cluster Self-Review

After each cluster (4–6 Q&A pairs):

| Check | Requirement |
|-------|-------------|
| **Perspectives** | Multiple schools (brand vs. performance, B2B vs. B2C)? |
| **Evidence** | ≥2 authoritative sources + ≥1 tool? |
| **Source quality** | Tier 1–3? |
| **Key Insights** | Non-obvious, decision-useful? |
| **Limitations** | "When NOT to use" in ≥50%? |
| **Alternatives** | Alternative frameworks acknowledged? |
| **Bias** | Biases noted where relevant? |

### Step 4: Artifacts

Per cluster: ≥1 diagram (journey maps, positioning matrices, funnels, decision trees, flows) + ≥1 table (comparisons, prioritization, dashboards, performance). Use markdown tables/ASCII art.

**✓ Checkpoint**: All clusters have ≥1 diagram + ≥1 table?

### Step 5: Reference Sections

1. **Glossary (G#)**: Term, definition, usage
2. **Tools (T#)**: Name, description, pricing, users, integrations, update, URL
3. **Literature (L#)**: Author, title, topics
4. **APA Citations (A#)**: APA 7th + language tags [EN]/[ZH]

**✓ Checkpoint**: All [Ref: ID] resolve?

### Step 6: Validation

Run 17-step checklist. **MANDATORY**: All PASS. **FAIL → stop, fix, re-validate**.

### Step 7: Final Review

1. Question Design Criteria met?
2. Success Criteria satisfied?
3. Accuracy/Verification requirements met?
4. Validation Report shows all PASS?

---

## Validation Checklist

**MANDATORY**: All 17 checks must PASS before submission. **FAIL → stop, fix, re-validate**.

| # | Check | Criteria | Why This Matters | Status |
|---|-------|----------|------------------|--------|
| **1** | **Counts** | G≥10, T≥5, L≥6, A≥12 \| Q&A 25–30 \| Difficulty 20/40/40% (±5pp) | Ensures comprehensive coverage and balanced difficulty distribution | PASS/FAIL |
| **2** | **Citation coverage** | ≥70% answers ≥1 citation \| ≥30% answers ≥2 citations | Evidence-based answers build credibility and enable verification | PASS/FAIL |
| **3** | **Language** | EN 50–70%, ZH 20–40%, Other 5–15% | Reflects global marketing practice and audience diversity | PASS/FAIL |
| **4** | **Recency** | ≥50% <3yr (≥70% digital/social) | Current practices matter in fast-evolving marketing landscape | PASS/FAIL |
| **5** | **Diversity** | ≥3 types \| no source >25% | Prevents over-reliance on single perspective or methodology | PASS/FAIL |
| **6** | **Links** | All accessible/archived (prefer DOIs) | Enables verification and long-term reference access | PASS/FAIL |
| **7** | **Cross-refs** | All [Ref: ID] resolve | Broken references undermine credibility and usability | PASS/FAIL |
| **8** | **Word count** | Sample 5: all 150–300 | Ensures depth (not superficial) and concision (not verbose) | PASS/FAIL |
| **9** | **Key Insights** | All concrete (opportunity/trade-off/conflict/challenge) | Distinguishes high-signal questions from generic knowledge checks | PASS/FAIL |
| **10** | **Per-topic** | ≥2 authoritative + ≥1 tool/cluster | Ensures each domain is grounded in research and practical tools | PASS/FAIL |
| **11** | **Frameworks** | ≥80% correct with citations + limitations | Frameworks are valuable only if accurately applied and contextualized | PASS/FAIL |
| **12** | **Judgment** | ≥70% scenario-based (not recall) | Senior roles require decision-making ability, not rote memorization | PASS/FAIL |
| **13** | **Accuracy** | Sample 5: factually correct, cross-validated | Inaccurate information damages trust and misleads decision-making | PASS/FAIL |
| **14** | **Balance** | ≥50% acknowledge limitations/trade-offs | One-sided answers fail to reflect real-world complexity and trade-offs | PASS/FAIL |
| **15** | **Reasoning** | ≥60% include logical explanation | Explicit reasoning enables learning and replication of thought process | PASS/FAIL |
| **16** | **Artifacts** | Each cluster: ≥1 diagram + ≥1 table | Visual aids clarify complex concepts and improve comprehension | PASS/FAIL |
| **17** | **TOC** | Present and links work | Navigation is essential for usability of long-form documents | PASS/FAIL |

---

## Common Pitfalls

### Question Pitfalls

| Pitfall | Example (❌ Bad) | Fix (✅ Good) | Why It Matters |
|---------|------------------|---------------|----------------|
| **Too broad** | "Explain SEO best practices" | "Your organic traffic dropped 30% after a site migration. What's your diagnosis and recovery plan?" | Senior roles require applied judgment, not general knowledge |
| **Recall-based** | "List the AIDA stages" | "Your ad campaign has high click-through but low conversion. How do you apply AIDA to diagnose and fix?" | Tests memorization, not strategic thinking |
| **No constraints** | "Design a Facebook ad campaign" | "Allocate $50K across paid search, paid social, and content with 60-day payback constraint. Justify your mix." | Realistic scenarios include resource constraints and trade-offs |
| **Single-variable** | "Should we use email marketing?" | "Email has 8% CTR but 2% conversion. Paid search has 3% CTR but 12% conversion. Optimize the funnel." | Multi-variable scenarios test prioritization and systems thinking |
| **Role misalignment** | (VP-level) "Write a blog post" | (VP-level) "Your board wants 10% revenue from a new segment. How do you allocate marketing budget?" | Question complexity must match seniority expectations |

### Answer Pitfalls

| Pitfall | Example (❌ Bad) | Fix (✅ Good) | Why It Matters |
|---------|------------------|---------------|----------------|
| **No citations** | "Brand building is important for long-term growth" | "Brand building is important for long-term growth [Ref: L4, A10]" | Unsubstantiated claims lack credibility |
| **Vague recommendations** | "Improve your content strategy" | "Audit top 20 pages by traffic; rewrite bottom 5 with target keywords [Ref: T3]; measure CTR change in 30 days" | Actionable steps enable implementation |
| **Missing limitations** | "Use multi-touch attribution to optimize channels" | "Use multi-touch attribution [Ref: G6], but note: it assumes all touchpoints are measurable and doesn't capture offline influence [Ref: A12]" | Ignoring limitations sets unrealistic expectations |
| **No alternatives** | "Always use A/B testing for optimization" | "Use A/B testing for high-traffic pages [Ref: T1]. For low-traffic, use sequential testing or expert heuristics [Ref: A11]" | One-size-fits-all ignores context and constraints |
| **Theory-heavy (I/A levels)** | "Porter's Five Forces analyzes competitive intensity through supplier power, buyer power, threat of substitutes, threat of new entrants, and competitive rivalry" | "Apply Porter's Five Forces [Ref: L1]: High buyer power (10 vendors, low switching cost) → price pressure. Action: Differentiate via brand equity [Ref: G7, L2] or lock-in via platform [Ref: L5]" | Senior roles require application, not recitation |
| **No Key Insight** | Generic question without specific insight | "Tests diagnosis of efficiency vs. effectiveness trade-offs; distinguishes strategists who balance short-term ROAS with long-term brand equity" | Insight explains what the question discriminates and why it matters |

---

## Output Format

### Overall Structure

```markdown
# Interview Q&A - Marketing Professional

## Contents
- [Topic Overview](#topic-overview)
- [Topic 1: Market Research & Analysis](#topic-1-market-research--analysis)
- [Topic 2: Marketing Strategy & Planning](#topic-2-marketing-strategy--planning)
- [Topic 3: Brand Positioning & Messaging](#topic-3-brand-positioning--messaging)
- [Topic 4: Customer Segmentation & Targeting](#topic-4-customer-segmentation--targeting)
- [Topic 5: Marketing Channels & Campaign Management](#topic-5-marketing-channels--campaign-management)
- [Topic 6: Marketing Metrics & Analytics](#topic-6-marketing-metrics--analytics)
- [Reference Sections](#reference-sections)
  - [Glossary](#glossary)
  - [Tools](#tools)
  - [Literature](#literature)
  - [APA Citations](#citations)
- [Validation Report](#validation-report)

## Topic Overview

| Topic | Question Range | Count | Difficulty Mix (F/I/A) |
|-------|----------------|-------|------------------------|
| Market Research & Analysis | Q1–Q5 | 5 | 1 / 2 / 2 |
| Marketing Strategy & Planning | Q6–Q10 | 5 | 1 / 2 / 2 |
| Brand Positioning & Messaging | Q11–Q15 | 5 | 1 / 2 / 2 |
| Customer Segmentation & Targeting | Q16–Q19 | 4 | 1 / 1 / 2 |
| Channels & Campaign Management | Q20–Q24 | 5 | 1 / 2 / 2 |
| Metrics & Analytics | Q25–Q30 | 6 | 1 / 3 / 2 |
| **Total** | **Q1–Q30** | **30** | **6 / 12 / 12 (20% / 40% / 40%)** |

---

## Topic 1: Market Research & Analysis

### Q1: [Question Text]

**Difficulty**: [F/I/A] | **Type**: Market Research & Analysis

**Key Insight**: [One sentence: opportunity/trade-off/conflict/challenge. Must be non-obvious, decision-useful, falsifiable.]

**Answer** (150–300 words):

[Follow Required Answer Structure:
1. Context and problem framing
2. Analysis and assumptions [Ref: ID]
3. Reasoning chain [Ref: ID]
4. Recommendations and alternatives [Ref: ID]
5. Implementation steps (optional for F)
6. Metrics and expected impact (optional for F)
7. Risks and limitations - include "When NOT to use this approach"
8. Inline citations [Ref: ID]]

**Supporting Artifact**:

[Diagram or table - use markdown table or ASCII art or structured description]

---

[Repeat for all Q&A pairs in this topic cluster]

---

[Repeat for all topic clusters]

---

## Reference Sections

### Glossary (≥10 entries)

**G1. Term**: Definition. **Use**: Context and application.

**G2. Term**: Definition. **Use**: Context and application.

[Continue for all glossary entries]

---

### Tools (≥5 entries with pricing, users, update ≤18mo, integrations)

**T1. Tool Name**: Description. Pricing: $X/mo or Free. Users: Nm+. Integrations: [List]. Last Update: Q# YYYY. URL: https://example.com

**T2. Tool Name**: Description. Pricing: $X/mo or Free. Users: Nm+. Integrations: [List]. Last Update: Q# YYYY. URL: https://example.com

[Continue for all tool entries]

---

### Literature (≥6 entries, EN+ZH)

**L1.** Author(s) (Year). *Title* (Edition). Publisher. [Key topics covered]

**L2.** Author(s) (Year). *Title*. Publisher. [Key topics covered]

[Continue for all literature entries]

---

### APA Citations (≥12 entries, language tags, EN 50-70%/ZH 20-40%/Other 5-15%)

**A1.** Author, A., & Author, B. (Year). *Title* (Edition). Publisher. DOI [EN]

**A2.** Author, A. (Year). Title. *Journal Name*, Vol(Issue), Pages. DOI [EN]

**A3.** 作者 (Year). *标题*. 出版社. [ZH]

[Continue for all APA citations]

---

## Validation Report

Execute 17-step validation. All must PASS before submission.

| # | Check | Criteria | Status | Notes |
|---|-------|----------|--------|-------|
| 1 | Counts | G≥10, T≥5, L≥6, A≥12 \| Q&A 25–30 \| Difficulty 20/40/40% (±5pp) | PASS | G=12, T=6, L=8, A=15 \| Q&A=30 \| F=6, I=12, A=12 (20%/40%/40%) |
| 2 | Citation coverage | ≥70% answers ≥1 \| ≥30% answers ≥2 | PASS | 85% have ≥1, 40% have ≥2 |
| 3 | Language | EN 50–70%, ZH 20–40%, Other 5–15% | PASS | EN 62%, ZH 31%, Other 7% |
| 4 | Recency | ≥50% <3yr (≥70% digital/social) | PASS | 58% overall <3yr, 75% digital <3yr |
| 5 | Diversity | ≥3 types \| no source >25% | PASS | 4 types, max source 18% |
| 6 | Links | All accessible/archived (prefer DOIs) | PASS | 100% accessible, 80% have DOIs |
| 7 | Cross-refs | All [Ref: ID] resolve | PASS | All IDs resolve correctly |
| 8 | Word count | Sample 5: all 150–300 | PASS | Q1=285, Q8=210, Q15=265, Q22=195, Q28=250 |
| 9 | Key Insights | All concrete | PASS | All insights identify specific opportunities/trade-offs |
| 10 | Per-topic | ≥2 authoritative + ≥1 tool/cluster | PASS | All clusters meet floor |
| 11 | Frameworks | ≥80% correct with citations + limitations | PASS | 90% meet criteria |
| 12 | Judgment | ≥70% scenario-based | PASS | 27/30 (90%) are scenario-based |
| 13 | Accuracy | Sample 5: correct, cross-validated | PASS | All claims verified with ≥2 sources |
| 14 | Balance | ≥50% acknowledge limitations/trade-offs | PASS | 22/30 (73%) include limitations |
| 15 | Reasoning | ≥60% include logical explanation | PASS | 25/30 (83%) include reasoning chain |
| 16 | Artifacts | Each cluster: ≥1 diagram + ≥1 table | PASS | All 6 clusters have both |
| 17 | TOC | Present and links work | PASS | All anchors tested and working |

**Validation Status**: ✅ ALL CHECKS PASS - Ready for submission
```

---

## Example Q&A Pair

### Q1: How would you determine optimal channel mix when CAC increased 45% YoY and LTV:CAC dropped from 4.5:1 to 2.8:1?

**Difficulty**: Advanced | **Type**: Metrics & Analytics, Channels & Campaigns

**Key Insight**: Tests diagnosis of efficiency deterioration and rebalancing based on unit economics; distinguishes holistic optimizers who balance short-term performance with long-term brand building from vanity metric chasers who optimize narrow KPIs.

**Answer**:

**Context**: CAC increasing 45% with LTV:CAC dropping from 4.5:1 to 2.8:1 indicates unit economics deterioration—a critical threat to sustainable growth [Ref: G4, G5].

**Analysis**: Three likely root causes [Ref: A11]: (1) **Declining lead quality** (converting less-qualified leads with higher churn), (2) **Channel saturation** (diminishing returns as addressable audience shrinks), (3) **Competitive pressure** (competitors bidding up ad prices in same channels). Decompose CAC by channel and cohort using analytics platforms [Ref: T1, T2] to isolate cause.

**Reasoning**: Multi-touch attribution [Ref: G6] reveals true contribution vs. last-click, which over-credits bottom-funnel channels while undervaluing awareness touchpoints [Ref: A12, T1]. Calculate channel-specific LTV:CAC; healthy channels maintain ≥3:1 [Ref: L1, G5]. This distinguishes efficient channels from saturated ones [Ref: A10].

**Recommendations**: Three-phase rebalancing strategy [Ref: L2]:
1. **Immediate** (Month 1): Pause or reduce spend on channels with LTV:CAC <2:1; reallocate budget to efficient channels (≥3:1 ratio)
2. **Medium-term** (Months 2–3): Test new channels (partnerships, community, referral, organic content) [Ref: G9, L3]; pilot with 10% of freed-up budget
3. **Long-term** (Months 4–6): Improve conversion rates via CRO [Ref: T1]; increase LTV through retention programs and upsell [Ref: T2, T4]. Use Marketing Mix Modeling [Ref: G6] to simulate outcomes before major shifts.

**Metrics**: Target CAC $200 (−23% from current), LTV:CAC 4.0:1 (+43%), payback period <12 months.

**When NOT to use**: If CAC increase is due to strategic up-market expansion (higher ARPU justifies higher CAC), maintain current mix but adjust LTV expectations upward.

**Limitations**: Attribution models have inherent biases—no model captures perfect causality [Ref: G6, A12]. External factors (seasonality, market shifts, competition) confound metrics. Rapid channel shifts risk brand momentum loss and undervalue long-term brand-building that doesn't appear in short-term LTV [Ref: L4, A10].

**Supporting Artifact**:

```
Channel Mix Analysis & Rebalancing Dashboard

Current State: CAC $180→$261 (+45%) | LTV $810→$730 (−10%) | LTV:CAC 4.5:1→2.8:1 (−38%)
Target State:  CAC $200 | LTV $900 | LTV:CAC 4.0:1

Channel Performance Analysis:
┌─────────────────┬───────┬─────────┬────────┬──────────────────────┐
│ Channel         │ % Mix │ CAC     │ LTV:CAC│ Action               │
├─────────────────┼───────┼─────────┼────────┼──────────────────────┤
│ Paid Search     │  35%  │  $220   │  3.3:1 │ Maintain             │
│ Paid Social     │  25%  │  $340   │  2.1:1 │ Reduce 40%           │
│ Content/SEO     │  15%  │   $95   │  7.7:1 │ Increase 50%         │
│ Events          │  15%  │  $420   │  1.7:1 │ Pause                │
│ Email           │   5%  │   $60   │ 12.2:1 │ Scale 3x             │
│ Partnerships    │   5%  │  $140   │  5.2:1 │ Test & Expand        │
└─────────────────┴───────┴─────────┴────────┴──────────────────────┘

3-Month Rebalancing Plan:
Month 1: Cut Paid Social 40%, Events 100%      → Save $200K
Month 1-2: Increase Content 50%, Email 3x      → Invest $100K
Month 2-3: Test Partnerships, Community, Referral → Invest $100K

Expected Outcome: CAC $200 (−23%), LTV:CAC 4.0:1 (+43%), Payback <12mo
```

*(285 words)*

---

**END OF TEMPLATE**

---

## Notes for LLM Users

1. Copy entire document into LLM interface
2. Replace placeholder values with actual content
3. Follow Instructions sequentially (Steps 1–7)
4. Run full Validation Checklist (17 checks)
5. Preserve all numeric requirements from Success Criteria
6. Cite: Optimized per [Guidelines for LLM-Friendly Prompts](../Guidelines_for_LLM-Friendly_Prompts.md)

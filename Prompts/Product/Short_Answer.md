# Short Answer – Product Manager

## Purpose and Scope

This framework provides a structured methodology for generating high-quality product management short answer assessments. It is designed for senior/director/VP level Product Managers and covers six core domains: Product Strategy, Discovery & Validation, Prioritization & Roadmapping, Metrics & Growth, Stakeholder Management, and Go-to-Market.

**Key Constraints:**
- Target audience: Senior/Director/VP level Product Managers
- Assessment scope: 25–40 problems across 6 PM domains
- Quality focus: Evidence-based, citation-rich, multi-perspective evaluation
- Output format: Structured markdown with validation reporting

**Assumptions:**
- Evaluators have access to cited references for verification
- Candidates have 2–5 years of product management experience
- Assessment context is technical product domains (SaaS, platforms, B2B/B2C)
- Grading allows partial credit for methodology and product judgment

---

# Part I: Specifications

## Scope and Constraints

### Problem Specifications

- **Problem count**: 25–40 problems (adjust based on assessment duration and depth requirements)
- **Difficulty distribution**: 20% Foundational / 40% Intermediate / 40% Advanced
  - *Foundational*: Core PM concepts, standard frameworks (e.g., AARRR, RICE)
  - *Intermediate*: Cross-functional scenarios, trade-off analysis, metric selection
  - *Advanced*: Strategic decisions, multi-stakeholder conflicts, ambiguous contexts
- **Domain coverage**: 6 core areas with 4–8 problems each
  1. Product Strategy (vision, positioning, market analysis)
  2. Discovery & Validation (user research, hypothesis testing, PMF)
  3. Prioritization & Roadmapping (RICE, ICE, value/effort, backlog management)
  4. Metrics & Growth (North Star, AARRR, retention, activation)
  5. Stakeholder Management (communication, alignment, conflict resolution)
  6. Go-to-Market (launch strategy, PLG, sales enablement)

### Problem Format

- **Prompt**: 2–3 sentences providing product context, relevant constraints, and specific question
- **Answer**: 2–4 concise, actionable steps citing frameworks [Ref: G#], tools [Ref: T#], or sources [Ref: A#]
- **Worked Solution**: Step-by-step reasoning with [Ref: ID] citations explaining methodology, alternatives, and trade-offs

### Grading Approach

- **Partial credit enabled**: Award points for correct methodology, proper framework application, sound product judgment, and consideration of alternatives
- **Multiple valid approaches**: Document alternative solutions and their contexts (e.g., RICE vs ICE for different team sizes)
- **Evaluation dimensions**: Correctness (40%), Reasoning (30%), Practicality (20%), Completeness (10%)

## Reference Requirements (MECE Coverage)

### Minimum Reference Floors

| Section | Minimum | Content Coverage | Rationale |
|---------|---------|------------------|----------|
| Glossary | 10 | RICE, AARRR, JTBD, North Star, PMF, OKR, PLG, OST, Continuous Discovery, Feature Factory | Ensures comprehensive framework vocabulary across all 6 domains |
| Tools | 5 | Analytics (Mixpanel/Amplitude), Roadmapping (ProductBoard/Aha!), Research (Dovetail/UserTesting), Collaboration (Miro/FigJam), A/B Testing (Optimizely/LaunchDarkly) | Covers complete PM toolkit from discovery to delivery |
| Literature | 6 | Strategic frameworks (Cagan, Olsen), Discovery methods (Torres, Patton), Organizational transformation (Perri), Cultural perspectives (俞军, 梁宁, 苏杰) | Balances Western and Eastern PM philosophies; foundational + emerging practices |
| APA Citations | 12 | ~60% [EN], ~30% [ZH], ~10% [other languages] using APA 7th edition with language tags | Ensures cultural diversity, global perspective, and citation verification |

### Scaling Rules

- **For 41–60 problems**: Increase floors by 1.5× (Glossary: 15, Tools: 8, Literature: 9, APA: 18)
- **For 61+ problems**: Increase floors by 2× (Glossary: 20, Tools: 10, Literature: 12, APA: 24)
- **Quality over quantity**: Meet quality gates (Section II.5) before expanding reference counts

### Exception Handling

If any floor cannot be met:
1. **Document shortfall**: Specify which floor and by how much (e.g., "Tools: 4/5, missing A/B testing platform")
2. **Provide rationale**: Explain constraint (e.g., "Niche domain with limited ZH literature")
3. **State sourcing plan**: Describe mitigation (e.g., "Will add UserTesting (T#) and Split.io (T#) in next revision")

## Citation Standards (Evidence & Credibility)

### Language Distribution

- **Target mix**: ~60% [EN], ~30% [ZH], ~10% [other languages]
- **Tolerance**: EN 50–70%, ZH 20–40%, Other 5–15%
- **Rationale**: Balances global PM best practices (predominantly English) with Eastern perspectives (Chinese PM philosophy emphasizes user psychology, platform dynamics)
- **Language tags**: Append [EN], [ZH], [JA], [KO], [DE], etc. to all APA citations
- **Translation notes**: Provide romanized title in parentheses for non-Latin scripts

### Source Type Diversity (MECE)

1. **Product Frameworks & Methodologies**: RICE, JTBD, OKR, Continuous Discovery, PLG
2. **Research & Data Sources**: User research studies, market analyses, growth benchmarks, industry reports
3. **Authoritative Literature**: Books (Cagan, Olsen, Torres, Perri, 俞军, 梁宁), academic papers, case studies
4. **Tools & Platforms**: Analytics (Mixpanel), Roadmapping (ProductBoard), Research (Dovetail), Collaboration (Miro)

### Format Specification

- **Standard**: APA 7th edition (Publication Manual of the American Psychological Association, 7th ed.)
- **Required elements**: Author, Year, Title (italicized for books/reports), Publisher/Journal, DOI/URL (when available), Language tag
- **Inline citation format**: [Ref: ID] where ID = G# (Glossary), T# (Tools), L# (Literature), A# (APA Citations)
- **Example**: "Apply RICE prioritization [Ref: G2, T2, A2] to rank initiatives..."

### Citation Usage Guidelines

- **When to cite**: Framework applications, data/metrics, best practices, tool recommendations, theoretical concepts
- **Minimum coverage**: ≥70% problems cite ≥1 reference; ≥30% problems cite ≥2 references
- **Cross-referencing**: All [Ref: ID] must resolve to entries in Part III Reference Sections
- **Verification**: Prioritize DOI links > stable URLs > archived snapshots (Wayback Machine)

## Quality Gates (Validation Criteria)

### Recency & Relevance

- **Standard domains**: ≥50% citations from last 3 years (2022–2025 as of Nov 2025)
- **Fast-evolving domains**: ≥70% citations from last 3 years for AI/ML products, platform ecosystems, emerging markets
- **Rationale**: PM practices evolve rapidly (PLG, AI-driven analytics, continuous discovery); outdated frameworks may mislead
- **Exceptions**: Foundational works (e.g., Cagan's *Inspired*, Ries's *Lean Startup*) remain valid; flag if >10 years old and confirm ongoing relevance

### Source Diversity (Fairness)

- **Minimum source types**: ≥3 of 4 categories (Frameworks, Research, Literature, Tools)
- **Maximum concentration**: No single source type >25% of total citations
- **Rationale**: Prevents over-reliance on tools (vs theory) or Western literature (vs global perspectives)
- **Balance check**: Ensure mix of practitioner wisdom (Cagan, Torres), academic rigor (HBS cases), and tool documentation

### Evidence Coverage (Sufficiency)

- **Tier 1**: ≥70% problems cite ≥1 reference (demonstrates evidence-based reasoning)
- **Tier 2**: ≥30% problems cite ≥2+ references (shows multi-source validation, alternative perspectives)
- **Advanced problems**: Should cite ≥2 references to reflect complexity and trade-offs
- **Rationale**: Aligns with evidence-based PM practices; builds candidate habit of consulting multiple sources

### Tool Metadata Requirements (Practicality)

For each tool entry (T#), include:
- **Pricing model**: Freemium, Starter ($X/user/mo), Enterprise (contact sales)
- **User base**: "XK+ companies" or "XM+ users" with 2–3 notable clients (e.g., "8K+ companies (Uber, Netflix)")
- **Last update**: Quarter + Year, ≤18 months old (e.g., "Updated Q3 2024")
- **Key integrations**: 3–5 major platforms (Jira, Slack, Salesforce, Segment, etc.)
- **PM use cases**: 2–3 specific applications (e.g., "Activation tracking, feature adoption, retention monitoring")
- **Official link**: HTTPS URL to vendor site

**Rationale**: Enables candidates to evaluate tool fit, cost-benefit, integration complexity

### Link Accessibility (Accuracy)

- **Preferred**: DOI links (persistent, version-controlled)
- **Acceptable**: Stable HTTPS URLs (vendor sites, official repositories)
- **Required**: Archived snapshots (Wayback Machine) if original link is broken
- **Verification**: Test all links before submission; flag "[Archived: DATE]" if using snapshots
- **Rationale**: Ensures evaluators can verify claims; prevents citation rot

### Cross-Reference Integrity (Logic)

- **Requirement**: All [Ref: ID] used in problems must resolve to entries in Part III (Glossary, Tools, Literature, APA Citations)
- **No orphan IDs**: Every ID in problems appears in reference sections
- **No unused entries**: ≥80% reference entries cited in ≥1 problem (prune unused entries)
- **Validation method**: Automated cross-check (see Step 5 validation script)
- **Rationale**: Maintains structural consistency; prevents broken references

## Success Criteria (Measurable Outcomes)

### Mandatory Requirements (All Must Pass)

| Criterion | Specification | Validation Method |
|-----------|---------------|-------------------|
| **Reference floors** | Glossary ≥10, Tools ≥5, Literature ≥6, APA ≥12 (or documented exception) | Count entries in each section |
| **Problem count** | 25–40 total problems | Count problem headers |
| **Difficulty distribution** | 20% Foundational (±5%), 40% Intermediate (±5%), 40% Advanced (±5%) | Calculate percentages; allow ±5% tolerance |
| **Language mix** | EN 50–70%, ZH 20–40%, Other 5–15% | Count language tags in APA section; calculate percentages |
| **Quality gates** | All 6 gates PASS (Recency, Diversity, Evidence, Tool Metadata, Links, Cross-refs) | Run validation checks (Part II, Step 5) |
| **Validation report** | All checks show PASS; failures documented + fixed | Generate report using template (Part III) |
| **Format compliance** | Output matches Part III template structure exactly | Visual inspection; automated linting (optional) |

### Performance Indicators (Quality Signals)

- **Citation depth**: Average citations per problem ≥1.5 (signals thorough research)
- **Framework diversity**: ≥8 distinct frameworks cited across all problems (prevents over-reliance on single method)
- **Practical relevance**: ≥90% problems include specific metrics, tools, or data points (vs purely theoretical)
- **Alternative solutions**: ≥25% worked solutions mention trade-offs or alternative approaches (demonstrates fairness)

### Deliverable Checklist

- [ ] All reference floors met or exception documented with mitigation plan
- [ ] Problem count 25–40 with 20/40/40 difficulty split (±5% tolerance)
- [ ] Citation language mix within tolerance (EN 50–70%, ZH 20–40%, Other 5–15%)
- [ ] All 6 quality gates passed (Recency, Diversity, Evidence, Tool Metadata, Links, Cross-refs)
- [ ] Validation report generated with all PASS results
- [ ] Output format matches Part III template exactly (Contents, Problem Bank, Reference Sections)
- [ ] All [Ref: ID] citations resolve correctly to reference entries
- [ ] All links tested and accessible (or archived)
- [ ] Tool entries include all required metadata (pricing, user base, update date, integrations, use cases, link)
- [ ] Worked solutions demonstrate reasoning, cite sources, acknowledge alternatives/trade-offs

---

# Part II: Instructions

## Workflow

Follow these steps sequentially. Execute inline checks before proceeding.

### Step 1: Plan Problem Distribution (Structure & MECE)

**Objective**: Create a balanced, comprehensive problem set covering all critical PM domains without gaps or overlaps.

**Actions**:

1. **Identify 6 core PM domains** (MECE coverage):
   - **Product Strategy**: Vision, positioning, market segmentation, competitive analysis, business model
   - **Discovery & Validation**: User research, hypothesis testing, PMF, assumption mapping, validation methods
   - **Prioritization & Roadmapping**: RICE, ICE, value/effort, backlog management, stakeholder alignment
   - **Metrics & Growth**: North Star, AARRR, retention, activation, cohort analysis, experimentation
   - **Stakeholder Management**: Communication, alignment, conflict resolution, executive reporting, cross-functional collaboration
   - **Go-to-Market**: Launch strategy, PLG, sales enablement, positioning, pricing, channel strategy

2. **Allocate problems per domain**:
   - Distribute 25–40 problems across 6 domains
   - Allocate 4–8 problems per domain based on importance and complexity
   - Ensure no domain <4 problems (insufficient coverage) or >8 problems (over-emphasis)
   - Example for 30 problems: Strategy (5), Discovery (5), Prioritization (6), Metrics (6), Stakeholder (4), GTM (4)

3. **Assign difficulty levels** (20/40/40 split):
   - **Foundational (20%)**: Standard frameworks, definitions, basic applications
     - Example: "Define North Star Metric and give 2 examples for SaaS products"
   - **Intermediate (40%)**: Trade-offs, scenario-based decisions, cross-functional challenges
     - Example: "Your team wants Feature A (high effort, high impact) vs Feature B (low effort, medium impact). Use RICE to decide."
   - **Advanced (40%)**: Ambiguous contexts, strategic decisions, multi-stakeholder conflicts, systemic issues
     - Example: "PMF metrics plateaued after 6 months. Diagnose 3 possible causes and propose validation experiments."

4. **Self-check**:
   - [ ] Total problem count = 25–40
   - [ ] Difficulty ratio ≈ 20/40/40 (±5% tolerance: Foundational 15–25%, Intermediate 35–45%, Advanced 35–45%)
   - [ ] Each domain has 4–8 problems
   - [ ] No domain gaps (all 6 domains represented)
   - [ ] No domain overlaps (clear categorization; if ambiguous, assign to primary domain)

**Rationale**: MECE structure ensures comprehensive coverage; difficulty distribution matches senior PM expectations; self-check prevents specification drift.

### Step 2: Collect References (Breadth, Depth, Credibility)

**Objective**: Build a diverse, authoritative, up-to-date reference library covering frameworks, tools, literature, and data sources.

**Actions**:

1. **Glossary (≥10 terms)**:
   - **Selection criteria**: High-frequency PM frameworks used across multiple domains
   - **Required terms**: RICE, AARRR, JTBD, North Star, PMF, OKR, Continuous Discovery, PLG, Feature Factory, OST
   - **Additional suggestions**: ICE, KANO, Value/Effort Matrix, HMW (How Might We), Dual-track Agile, Build-Measure-Learn, Retention Curves, PQL (Product Qualified Lead), Expansion Revenue, HEART Framework
   - **Format**: **G#. Term (Expansion)** – Definition (1–2 sentences). Used for: [contexts]. Related: [similar terms]
   - **Coverage**: Ensure ≥1 term per domain (Strategy, Discovery, Prioritization, Metrics, Stakeholder, GTM)

2. **Tools (≥5 platforms)**:
   - **Selection criteria**: Industry-standard tools with active user bases, recent updates, broad integrations
   - **Required categories**:
     - Analytics: Mixpanel, Amplitude, Heap, PostHog
     - Roadmapping: ProductBoard, Aha!, Productplan, airfocus
     - Research: Dovetail, UserTesting, Maze, Optimal Workshop
     - Collaboration: Miro, FigJam, Mural, Lucidchart
     - Experimentation: Optimizely, LaunchDarkly, Split.io, Statsig
   - **Metadata requirements** (see Quality Gates): Pricing, user base, last update (≤18 months), integrations (3–5), PM use cases (2–3), official link
   - **Format**: **T#. Tool Name** (Category) – Description. Pricing. User base (notable clients). Updated [DATE]. Integrates: [platforms]. PM use: [use cases]. [URL]

3. **Literature (≥6 sources)**:
   - **Selection criteria**: Authoritative PM books, influential frameworks, diverse cultural perspectives
   - **Western sources** (≥4): Cagan (*Inspired*), Olsen (*Lean Product Playbook*), Torres (*Continuous Discovery Habits*), Perri (*Escaping the Build Trap*), Patton (*User Story Mapping*), Klement (*When Coffee and Kale Compete*)
   - **Eastern sources** (≥2): 俞军 (*俞军产品方法论*), 梁宁 (*产品思维30讲*), 苏杰 (*人人都是产品经理2.0*)
   - **Format**: **L#. Author. (Year). *Title*. Publisher.** – Key contribution (1 sentence). Use cases (1 sentence).
   - **Coverage**: Balance strategic (Cagan, Olsen), tactical (Torres, Patton), cultural (俞军, 梁宁)

4. **APA Citations (≥12 entries)**:
   - **Create full APA 7th edition citations** for all Glossary sources, Tool documentation, and Literature
   - **Language tagging**: Append [EN], [ZH], [JA], [KO], etc. to every citation
   - **Translation notes**: For non-Latin scripts, provide romanized title in parentheses (e.g., "俞军. (2020). *俞军产品方法论*. 中信出版社. [ZH] (Yu, J. (2020). *Yu Jun's product methodology*. CITIC Press.)")
   - **ID assignment**: Sequential numbering A1, A2, A3... in order of appearance or alphabetical by author
   - **Required elements**: Author, Year, Title (italicized), Publisher/Journal, DOI/URL (if available), Language tag
   - **Example**: **A1. Cagan, M. (2017). *Inspired: How to create tech products customers love* (2nd ed.). Wiley. [EN]**

5. **Self-check**:
   - [ ] Glossary ≥10 terms covering all 6 domains
   - [ ] Tools ≥5 platforms across ≥3 categories (Analytics, Roadmapping, Research, Collaboration, Experimentation)
   - [ ] Literature ≥6 sources with ≥4 Western + ≥2 Eastern perspectives
   - [ ] APA Citations ≥12 entries with language tags
   - [ ] Language mix: ~60% [EN], ~30% [ZH], ~10% [other] (tolerance: EN 50–70%, ZH 20–40%, Other 5–15%)
   - [ ] Recency: ≥50% citations from last 3 years (2022–2025)
   - [ ] Source diversity: ≥3 of 4 types (Frameworks, Research, Literature, Tools); no type >25%
   - [ ] All tool entries include required metadata (pricing, user base, update date ≤18 months, integrations, use cases, link)
   - [ ] All links tested and accessible (or archived)

**Rationale**: Diverse references ensure multi-perspective coverage (Western + Eastern PM philosophy); recency ensures relevance; credible sources build trust; metadata enables practical tool evaluation.

### Step 3: Generate Problems (Clarity, Precision, Relevance, Logic)

**Objective**: Create well-structured, evidence-based problems that test PM competencies with clear prompts, actionable answers, and thorough reasoning.

**Actions**:

1. **For each problem, complete all three components**:

   **A. Write Prompt (2–3 sentences)**:
   - **Context**: Provide product scenario with specific constraints (e.g., "Your B2B SaaS has 500 customers, $2M ARR, 65% retention")
   - **Frameworks/Metrics**: Mention relevant concepts (e.g., "North Star Metric", "RICE prioritization")
   - **Question**: Ask specific, unambiguous question (e.g., "What 3 initiatives would you prioritize and why?")
   - **Avoid**: Vague questions ("How to improve product?"), jargon without definition, multiple unrelated questions
   - **Example**: "Your SaaS product has a 30-day retention rate of 65% and an activation rate of 70%. The CEO wants to improve retention by 10 percentage points. Suggest a prioritization framework and outline 2–3 actionable steps to achieve this goal."

   **B. Write Answer (2–4 steps)**:
   - **Concise & Actionable**: Each step = 1 sentence with specific action + framework/tool/metric
   - **Cite References**: Use [Ref: ID] for frameworks (G#), tools (T#), literature (L#), or sources (A#)
   - **Principles**: Include PM best practices (user-centric, data-driven, iterative)
   - **Format**: Bullet list or numbered steps
   - **Example**:
     - Use RICE prioritization [Ref: G2, T2] to rank initiatives by reach, impact, confidence, and effort.
     - Focus on onboarding improvements, personalized engagement, and targeted feature adoption campaigns.
     - Monitor retention and activation metrics using Mixpanel [Ref: T1] or Amplitude [Ref: T3].

   **C. Write Worked Solution (step-by-step reasoning)**:
   - **Depth**: 4–8 sentences explaining methodology, calculations (if applicable), trade-offs, alternatives
   - **Citations**: Reference frameworks [Ref: G#], tools [Ref: T#], data sources [Ref: A#] for each claim
   - **Reasoning**: Show logical flow: Problem → Framework → Application → Validation → Outcome
   - **Alternatives & Trade-offs**: For Intermediate/Advanced problems, mention alternative approaches and their contexts (e.g., "RICE works for mature teams; use ICE for startups with uncertain data [Ref: L2]")
   - **Misconceptions**: For Advanced problems, flag common errors (e.g., "Avoid vanity metrics like total signups; focus on activated users [Ref: G4, A9]")
   - **Example**:
     1. Apply RICE prioritization [Ref: G2, T2] to proposed initiatives: onboarding (reach: 70% new users, impact: high, confidence: 80%, effort: 3 weeks), engagement (reach: 50% active users, impact: high, confidence: 60%, effort: 4 weeks), feature adoption (reach: 30% power users, impact: medium, confidence: 70%, effort: 2 weeks).
     2. Score each initiative: Onboarding RICE = (0.7 × high × 0.8) / 3 = highest priority.
     3. Use Mixpanel [Ref: T1] to track retention curves and activation funnels; set up cohort analysis to measure impact over 30/60/90 days.
     4. Monitor North Star Metric [Ref: G4] (e.g., weekly active usage) and validate with qualitative feedback [Ref: L4, A6].
     5. Alternative: If data is uncertain, use ICE (Impact × Confidence × Ease) for faster scoring [Ref: L2]; trade-off: less precision but better for early-stage products.

2. **Self-check (every 5 problems)**:
   - [ ] Prompt length: 2–3 sentences, clear context + specific question
   - [ ] Answer clarity: 2–4 actionable steps, each citing ≥1 reference [Ref: ID]
   - [ ] Citation presence: ≥70% problems cite ≥1 reference; ≥30% cite ≥2 references
   - [ ] Solution depth: 4–8 sentences with reasoning, trade-offs (for Intermediate/Advanced), alternatives (for Advanced)
   - [ ] Terminology consistency: Same terms used across prompt, answer, solution (e.g., "retention rate" not "retention" in one place and "churn" in another)
   - [ ] Relevance: Problem aligns with assigned domain and difficulty level
   - [ ] Logic: Solution reasoning is coherent, free of contradictions, follows Problem → Framework → Application → Validation flow

**Rationale**: Clear prompts reduce ambiguity; actionable answers provide immediate value; thorough solutions teach methodology; citations enable verification; self-checks prevent drift; alternatives demonstrate fairness; trade-offs show depth.

### Step 4: Populate Reference Sections (Structure, Accuracy, Completeness)

**Objective**: Create comprehensive, well-formatted reference sections that support all problem citations and enable verification.

**Actions**:

1. **Complete Glossary Section** (format: Part III):
   - **Entry format**: **G#. Term (Expansion)** – Definition (1–2 sentences). Used for: [contexts]. Related: [similar terms]
   - **Required elements**: Clear definition, practical use cases, related concepts
   - **Example**: **G2. RICE Prioritization** – Reach × Impact × Confidence ÷ Effort scoring for feature prioritization. Used for roadmap planning, backlog ranking. Related: ICE, Value/Effort Matrix, KANO
   - **Verification**: Ensure ≥10 entries covering all 6 domains

2. **Complete Tools Section** (format: Part III):
   - **Entry format**: **T#. Tool Name** (Category) – Description. Pricing. User base (notable clients). Updated [DATE]. Integrates: [platforms]. PM use: [use cases]. [URL]
   - **Required metadata** (see Quality Gates):
     - Pricing model: Freemium / Starter $X/user/mo / Enterprise
     - User base: "XK+ companies" or "XM+ users" with 2–3 notable clients
     - Last update: Quarter + Year, ≤18 months old (e.g., "Updated Q3 2024")
     - Integrations: 3–5 major platforms (Jira, Slack, Salesforce, Segment, etc.)
     - PM use cases: 2–3 specific applications
     - Official link: HTTPS URL
   - **Example**: **T1. Mixpanel** (Product Analytics) – Event tracking, funnel/cohort analysis, A/B testing, user segmentation. Freemium to Enterprise. 8K+ companies (Uber, Netflix). Updated Q3 2024 (AI insights). Integrates: Segment, Salesforce, Slack, Jira. PM use: Activation tracking, feature adoption, retention monitoring. https://mixpanel.com
   - **Verification**: Ensure ≥5 entries across ≥3 categories; test all links; confirm update dates ≤18 months

3. **Complete Literature Section** (format: Part III):
   - **Entry format**: **L#. Author. (Year). *Title*. Publisher.** – Key contribution (1 sentence). Use cases (1 sentence).
   - **Required elements**: Author, year, title, publisher, key contribution, use cases
   - **Example**: **L4. Torres, T. (2021). *Continuous Discovery Habits*. Product Talk LLC.** – Weekly customer touchpoints, opportunity solution trees. Discovery process design.
   - **Verification**: Ensure ≥6 entries with ≥4 Western + ≥2 Eastern sources

4. **Complete APA Citations Section** (format: Part III):
   - **Entry format**: **A#. Author. (Year). *Title* (Edition). Publisher. DOI/URL [Language Tag]**
   - **Required elements**: Full APA 7th edition citation + language tag ([EN], [ZH], [JA], etc.)
   - **Translation notes**: For non-Latin scripts, add romanized title in parentheses
   - **Example**: **A3. 俞军. (2020). *俞军产品方法论*. 中信出版社. [ZH]** (Yu, J. (2020). *Yu Jun's product methodology*. CITIC Press.)
   - **Verification**: Ensure ≥12 entries with ~60% [EN], ~30% [ZH], ~10% [other]; ≥50% from last 3 years; test all DOI/URL links

5. **Self-check (Cross-reference integrity)**:
   - [ ] All [Ref: ID] used in problems resolve to entries in reference sections (no broken references)
   - [ ] No orphan IDs: Every G#/T#/L#/A# in problems appears in reference sections
   - [ ] No unused entries: ≥80% reference entries cited in ≥1 problem (prune unused entries to reduce cognitive load)
   - [ ] Consistent ID formatting: G# for Glossary, T# for Tools, L# for Literature, A# for APA Citations
   - [ ] All tool metadata complete: pricing, user base, update date, integrations, use cases, link
   - [ ] All literature entries complete: author, year, title, publisher, key contribution, use cases
   - [ ] All APA citations complete: author, year, title, publisher, DOI/URL, language tag
   - [ ] All links tested and accessible (or archived with [Archived: DATE] tag)
   - [ ] Language tags present on all APA citations
   - [ ] Translation notes added for non-Latin scripts

**Rationale**: Comprehensive metadata enables practical evaluation; cross-reference integrity maintains logical consistency; verified links ensure accuracy; language tags support diversity; unused entries pruned for concision.

### Step 5: Validate and Submit (Validation, Success Criteria)

**Objective**: Verify all specifications, quality gates, and success criteria before final submission.

**Actions**:

1. **Execute validation checks** (automated or manual):

   **Check 1: Reference Counts**
   - Count entries: Glossary (G#), Tools (T#), Literature (L#), APA (A#)
   - Count problems and calculate difficulty distribution
   - **Pass criteria**: Glossary ≥10, Tools ≥5, Literature ≥6, APA ≥12, Problems 25–40, Difficulty split 20/40/40 (±5%)
   - **Failure action**: Add missing entries or document exception (shortfall + rationale + sourcing plan)

   **Check 2: Citation Coverage**
   - Count problems with ≥1 citation and ≥2 citations
   - Calculate percentages: (problems with ≥1 citation / total problems) × 100%
   - **Pass criteria**: ≥70% problems cite ≥1 reference; ≥30% cite ≥2 references
   - **Failure action**: Add citations to problems lacking references; prioritize Advanced problems

   **Check 3: Language Mix**
   - Count language tags in APA section: [EN], [ZH], [other]
   - Calculate percentages: (count / total APA entries) × 100%
   - **Pass criteria**: EN 50–70%, ZH 20–40%, Other 5–15%
   - **Failure action**: Adjust source selection to meet language distribution; prioritize underrepresented languages

   **Check 4: Recency**
   - Extract publication years from APA citations
   - Count citations from last 3 years (2022–2025 as of Nov 2025)
   - Calculate percentage: (recent citations / total APA entries) × 100%
   - **Pass criteria**: ≥50% from last 3 years (≥70% for AI/platform domains)
   - **Failure action**: Replace outdated sources with recent publications; flag foundational works as exceptions

   **Check 5: Source Diversity**
   - Categorize citations by type: (1) Frameworks, (2) Research, (3) Literature, (4) Tools
   - Count types present and calculate max concentration: (largest type count / total) × 100%
   - **Pass criteria**: ≥3 types present; no single type >25%
   - **Failure action**: Add underrepresented source types; reduce over-concentration

   **Check 6: Link Accessibility**
   - Test all DOI/URL links in APA Citations and Tools sections
   - Mark accessible (HTTP 200) vs broken (404, timeout)
   - Archive broken links using Wayback Machine; tag [Archived: DATE]
   - **Pass criteria**: All links accessible or archived
   - **Failure action**: Fix broken links, find alternative sources, or archive snapshots

   **Check 7: Cross-Reference Integrity**
   - Extract all [Ref: ID] from problem solutions
   - Verify each ID resolves to entry in reference sections (G#/T#/L#/A#)
   - Identify orphan IDs (used but not defined) and unused entries (defined but not cited)
   - **Pass criteria**: All [Ref: ID] resolve correctly; ≥80% entries cited in ≥1 problem
   - **Failure action**: Add missing reference entries or remove invalid [Ref: ID]; prune unused entries

2. **Generate Validation Report** (use template from Part III):

   | Check | Result | Status |
   |-------|--------|--------|
   | Counts | G:X T:Y L:Z A:W P:N (F/I/A) | PASS/FAIL |
   | Citation coverage | X% ≥1, Y% ≥2 | PASS/FAIL |
   | Language mix | EN:X% ZH:Y% Other:Z% | PASS/FAIL |
   | Recency | X% last 3yr | PASS/FAIL |
   | Source diversity | N types, max P% | PASS/FAIL |
   | Links | Y/X accessible | PASS/FAIL |
   | Cross-refs | Y/X resolved | PASS/FAIL |

   **Example**:
   | Check | Result | Status |
   |-------|--------|--------|
   | Counts | G:12 T:6 L:8 A:15 P:30 (6F/12I/12A) | PASS |
   | Citation coverage | 83% ≥1, 37% ≥2 | PASS |
   | Language mix | EN:60% ZH:27% Other:13% | PASS |
   | Recency | 67% last 3yr | PASS |
   | Source diversity | 4 types, max 22% | PASS |
   | Links | 21/21 accessible | PASS |
   | Cross-refs | 48/48 resolved | PASS |

3. **Fix failures and re-run**:
   - **MANDATORY**: If ANY check shows FAIL, stop immediately
   - Document failure details (which check, expected vs actual, root cause)
   - Fix issues: add entries, adjust distributions, replace sources, repair links, resolve references
   - Re-run all 7 validation checks
   - Repeat until ALL checks show PASS
   - **Do NOT proceed to submission until validation report shows 7/7 PASS**

4. **Final Submission Checklist**:
   - [ ] All 7 validation checks show PASS
   - [ ] Validation report generated and included in output
   - [ ] All reference floors met (or exception documented with mitigation plan)
   - [ ] All quality gates satisfied (Recency, Diversity, Evidence, Tool Metadata, Links, Cross-refs)
   - [ ] Output format matches Part III template exactly (Contents, Problem Bank, Reference Sections)
   - [ ] All [Ref: ID] citations resolve correctly
   - [ ] All links tested and accessible (or archived)
   - [ ] Tool entries include all required metadata
   - [ ] Worked solutions demonstrate reasoning, cite sources, acknowledge alternatives/trade-offs
   - [ ] Difficulty distribution within tolerance (20/40/40 ±5%)
   - [ ] Problem count 25–40
   - [ ] Language mix within tolerance (EN 50–70%, ZH 20–40%, Other 5–15%)

**Rationale**: Systematic validation prevents specification drift; mandatory PASS requirement ensures quality; validation report provides transparency; iterative fix-and-rerun cycle drives continuous improvement; final checklist confirms deliverable completeness.

**Submission Checklist** (expanded):

- [ ] All 7 validation checks show PASS (Counts, Citation coverage, Language mix, Recency, Source diversity, Links, Cross-refs)
- [ ] Validation report generated and included
- [ ] All reference floors met: Glossary ≥10, Tools ≥5, Literature ≥6, APA ≥12 (or exception documented with shortfall + rationale + sourcing plan)
- [ ] All quality gates satisfied: Recency ≥50% (≥70% for AI/platform), Diversity ≥3 types (<25% max), Evidence ≥70%/≥30%, Tool metadata complete, Links accessible, Cross-refs resolved
- [ ] Output format matches Part III template exactly: Contents TOC, Problem Bank structure, Reference Sections (Glossary, Tools, Literature, APA)
- [ ] All [Ref: ID] citations resolve correctly to reference entries
- [ ] All DOI/URL links tested and accessible (or archived with [Archived: DATE])
- [ ] Tool entries include all required metadata: pricing, user base, update date ≤18 months, integrations (3–5), PM use cases (2–3), official link
- [ ] Worked solutions demonstrate: reasoning, citations, alternatives (for Advanced), trade-offs (for Intermediate/Advanced), misconceptions (for Advanced)
- [ ] Difficulty distribution within tolerance: Foundational 15–25%, Intermediate 35–45%, Advanced 35–45%
- [ ] Problem count 25–40
- [ ] Language mix within tolerance: EN 50–70%, ZH 20–40%, Other 5–15%
- [ ] Domain coverage: All 6 domains represented with 4–8 problems each
- [ ] Terminology consistency: Same terms used across all problems
- [ ] No orphan IDs: All [Ref: ID] in problems appear in reference sections
- [ ] No unused entries: ≥80% reference entries cited in ≥1 problem (or documented rationale for unused entries)
- [ ] APA citations include language tags: [EN], [ZH], [JA], etc.
- [ ] Translation notes added for non-Latin scripts (romanized titles in parentheses)

---

# Part III: Output Format

```markdown
## Template Structure

Use this structure for all generated short answer banks.

### Validation Report Template

Present validation results using this table:

```
| Check | Result | Status |
|-------|--------|--------|
| Counts | G:X T:Y L:Z A:W P:N (F/I/A) | PASS/FAIL |
| Citation coverage | X% ≥1, Y% ≥2 | PASS/FAIL |
| Language mix | EN:X% ZH:Y% Other:Z% | PASS/FAIL |
| Recency | X% last 3yr | PASS/FAIL |
| Source diversity | N types, max P% | PASS/FAIL |
| Links | Y/X accessible | PASS/FAIL |
| Cross-refs | Y/X resolved | PASS/FAIL |
```

### Problem Bank Structure

Use this markdown structure:

```markdown
## Contents
- [Short Answer Bank](#short-answer-bank-problems-1-n)
- [Reference Sections](#reference-sections)
  - [Glossary, Terminology & Acronyms](#glossary-terminology--acronyms)
  - [Product Tools & Platforms](#product-tools--platforms)
  - [Authoritative Literature & Case Studies](#authoritative-literature--case-studies)
  - [APA Style Source Citations](#apa-style-source-citations)

---

## Short Answer Bank (Problems 1–N)

### Problem X

**Difficulty:** [Foundational/Intermediate/Advanced] | **Domain:** [Strategy/Discovery/Prioritization/Metrics/Stakeholder/GTM]

**Prompt:** (2–3 sentences, product context, frameworks, metrics)

**Answer:** (Concise, actionable response, 2–4 steps, frameworks, metrics, product principles)

**Worked Solution:** (Step-by-step reasoning, cite [Ref: ID] for frameworks, data, best practices)

---

## Reference Sections

Assign Reference IDs and reuse them inline in worked solutions: Glossary (G1…Gn), Tools (T1…Tn), Literature (L1…Ln), APA Citations (A1…An). Example inline: [Ref: G2, T3, A5].

### Glossary, Terminology & Acronyms

**G1. AARRR (Pirate Metrics)**  
Acquisition → Activation → Retention → Referral → Revenue framework for tracking growth across customer lifecycle. Used for SaaS metrics, funnel optimization. Related: HEART, North Star Metric

**G2. RICE Prioritization**  
Reach × Impact × Confidence ÷ Effort scoring for feature prioritization. Used for roadmap planning, backlog ranking. Related: ICE, Value/Effort Matrix, KANO

**G3. Jobs-to-be-Done (JTBD)**  
Framework for understanding the underlying "job" users hire a product to accomplish (vs demographics). Used for feature ideation, segmentation, competitive analysis. Related: Outcome-driven innovation

**G4. North Star Metric**  
Single metric capturing core product value; leading indicator of sustainable growth. Used for company alignment, PLG, OKRs. Related: OMTM, Input/Output metrics

**G5. Product-Market Fit (PMF)**  
Degree product satisfies market demand; measured when retention flattens and organic growth accelerates. Used for validation, pivot decisions, expansion. Related: Problem-solution fit, MVP

**G6. OKR (Objectives and Key Results)**  
Goal framework where Objectives = what to achieve, Key Results = how to measure. Used for quarterly planning, cross-functional alignment. Related: KPI, North Star, V2MOM

**G7. Continuous Discovery**  
Regular customer engagement through structured interviews/testing to inform decisions (vs periodic projects). Used for weekly interviews, opportunity trees, assumption testing. Related: Dual-track agile, Build-Measure-Learn

**G8. Product-Led Growth (PLG)**  
GTM strategy where product drives acquisition, conversion, expansion (vs sales-led). Used for SaaS freemium, self-serve onboarding, viral loops. Related: PQLs, Time-to-Value, Expansion revenue

**G9. Feature Factory**  
Anti-pattern: shipping features (outputs) vs solving problems (outcomes). Used in transformation discussions, outcome-based PM. Related: Build trap, Empowered teams

**G10. Opportunity Solution Tree (OST)**  
Visual framework mapping outcomes → opportunities (needs/pains) → solutions. Used for discovery planning, ideation, assumption mapping. Related: HMW statements, User story mapping

[... continue for ≥10 entries ...]

---

### Product Tools & Platforms

**T1. Mixpanel** (Product Analytics)  
Event tracking, funnel/cohort analysis, A/B testing, user segmentation. Freemium to Enterprise. 8K+ companies (Uber, Netflix). Updated Q3 2024 (AI insights). Integrates: Segment, Salesforce, Slack, Jira. PM use: Activation tracking, feature adoption, retention monitoring. https://mixpanel.com

**T2. ProductBoard** (Roadmapping & Prioritization)  
Feedback aggregation, prioritization matrix (value/effort), roadmap views, customer portal. Essentials $25/maker/mo to Enterprise. 6K+ teams (Microsoft, Zoom). Updated Q4 2024 (AI feedback analysis). Integrates: Jira, Slack, Salesforce, Intercom, Zendesk. PM use: Feedback synthesis, RICE scoring, stakeholder communication. https://www.productboard.com

**T3. Amplitude** (Product Analytics & Experimentation)  
Behavioral cohorts, retention/funnel analysis, A/B/n testing, predictive analytics. Freemium to Enterprise. 3.2K+ companies (PayPal, Ford). Updated Q3 2024 (AI insights, predictive playbooks). Integrates: Segment, Braze, Optimizely, Salesforce. PM use: North Star tracking, conversion optimization, impact analysis. https://amplitude.com

**T4. Dovetail** (User Research Repository)  
Auto transcription, tagging/theming, highlight reels, sentiment analysis, journey visualization. Freemium to Enterprise. 3K+ teams (Atlassian, Canva). Updated Q2 2024 (AI theme detection). Integrates: Zoom, Slack, Notion, Jira, UserTesting. PM use: Interview synthesis, JTBD mapping, discovery insights. https://dovetail.com

**T5. Miro** (Visual Collaboration)  
Infinite canvas, templates (story maps, journey maps, matrices), real-time collab, AI assistant. Freemium to Enterprise. 80M+ users (Dell, Cisco). Updated Q4 2024 (enhanced AI). Integrates: Jira, Slack, Teams, Zoom, Figma, Asana. PM use: Story mapping, OST workshops, roadmap planning, retrospectives. https://miro.com

[... continue for ≥5 entries ...]

---

### Authoritative Literature & Case Studies

**L1. Cagan, M. (2017). *Inspired* (2nd ed.). Wiley.**  
PM framework: discovery vs delivery, empowered teams. Foundational PM principles.

**L2. Olsen, D. (2015). *The Lean Product Playbook*. Wiley.**  
6-step process for product-market fit. Strategic planning, validation techniques.

**L3. Perri, M. (2018). *Escaping the Build Trap*. O'Reilly.**  
Outcomes over outputs, feature factory to outcome-driven culture. Organizational transformation.

**L4. Torres, T. (2021). *Continuous Discovery Habits*. Product Talk LLC.**  
Weekly customer touchpoints, opportunity solution trees. Discovery process design.

**L5. Patton, J. (2014). *User Story Mapping*. O'Reilly.**  
Story mapping by user journey (vs flat backlog). Roadmap planning, MVP scoping.

**L6. Klement, A. (2016). *When Coffee and Kale Compete*. Independent.**  
JTBD: functional/emotional/social jobs. Product positioning, competitive analysis.

[... continue for ≥6 entries ...]

---

### APA Style Source Citations

**A1. Cagan, M. (2017). *Inspired: How to create tech products customers love* (2nd ed.). Wiley. [EN]**

**A2. Olsen, D. (2015). *The lean product playbook: How to innovate with minimum viable products and rapid customer feedback*. Wiley. [EN]**

**A3. 俞军. (2020). *俞军产品方法论*. 中信出版社. [ZH]**  
(Yu, J. (2020). *Yu Jun's product methodology*. CITIC Press.)

**A4. Perri, M. (2018). *Escaping the build trap: How effective product management creates real value*. O'Reilly Media. [EN]**

**A5. Patton, J. (2014). *User story mapping: Discover the whole story, build the right product*. O'Reilly Media. [EN]**

**A6. Torres, T. (2021). *Continuous discovery habits: Discover products that create customer value and business value*. Product Talk LLC. [EN]**

**A7. Klement, A. (2016). *When coffee and kale compete: Become great at making products people will buy*. Independent. [EN]**

**A8. Ries, E. (2011). *The lean startup: How today's entrepreneurs use continuous innovation to create radically successful businesses*. Crown Business. [EN]**

**A9. McClure, D. (2007). Startup metrics for pirates: AARRR!. *500 Startups*. https://www.slideshare.net/dmc500hats/startup-metrics-for-pirates-long-version [EN]**

**A10. 梁宁. (2018). *产品思维30讲*. 得到App. [ZH]**  
(Liang, N. (2018). *30 lectures on product thinking*. Dedao App.)

**A11. Maurya, A. (2012). *Running lean: Iterate from plan A to a plan that works* (2nd ed.). O'Reilly Media. [EN]**

**A12. Eisenmann, T., Ries, E., & Dillard, S. (2012). Hypothesis-driven entrepreneurship: The lean startup. *Harvard Business School Entrepreneurial Management Case*, (812-095). [EN]**

**A13. Gothelf, J., & Seiden, J. (2016). *Lean UX: Designing great products with agile teams* (2nd ed.). O'Reilly Media. [EN]**

**A14. Bush, L., & Dunlap, K. (2023). *Product operations: How successful companies build better products at scale*. O'Reilly Media. [EN]**

**A15. 苏杰. (2019). *人人都是产品经理2.0*. 电子工业出版社. [ZH]**  
(Su, J. (2019). *Everyone is a product manager 2.0*. Publishing House of Electronics Industry.)

**A16. Kim, G. N. (2022). *Product leadership: How top product managers launch awesome products and build successful teams*. O'Reilly Media. [EN]**

[... continue for ≥12 entries with ~60% EN, ~30% ZH, ~10% other ...]
```

---

## Example Problem (Product Metrics & Prioritization)

### Problem 1

**Difficulty:** Intermediate | **Domain:** Metrics & Prioritization

**Prompt:** Your B2B SaaS product has a 30-day retention rate of 65% and an activation rate of 70%. The CEO wants to improve retention by 10 percentage points within 6 months. Suggest a prioritization framework and outline 2–3 actionable steps to achieve this goal, including specific metrics to track.

**Answer:**
- Use RICE prioritization [Ref: G2, T2] to rank initiatives by reach (% users affected), impact (retention lift), confidence (validation strength), and effort (engineering weeks).
- Focus on three areas: (1) onboarding improvements targeting 70% of new users [Ref: G7], (2) personalized engagement campaigns for at-risk cohorts [Ref: G1], and (3) feature adoption nudges for power users.
- Monitor retention curves, activation funnels, and cohort analysis using Mixpanel [Ref: T1] or Amplitude [Ref: T3]; validate with qualitative interviews [Ref: L4, A6].

**Worked Solution:**
1. **Apply RICE scoring** [Ref: G2, T2, A2]: Calculate for each initiative:
   - **Onboarding**: Reach = 70% new users (700/month), Impact = High (est. +8% retention), Confidence = 80% (A/B test data), Effort = 3 weeks → RICE = (700 × 3 × 0.8) / 3 = 560
   - **Engagement**: Reach = 50% active users (2,000/month), Impact = High (est. +6% retention), Confidence = 60% (hypothesis), Effort = 4 weeks → RICE = (2,000 × 3 × 0.6) / 4 = 900 (highest priority)
   - **Feature adoption**: Reach = 30% power users (300/month), Impact = Medium (est. +4% retention), Confidence = 70% (usage correlation), Effort = 2 weeks → RICE = (300 × 2 × 0.7) / 2 = 210

2. **Prioritize engagement campaigns** (highest RICE score): Use behavioral cohorts [Ref: T3] to identify at-risk users (e.g., declining usage over 14 days); send personalized re-engagement emails with product tips [Ref: G8]; monitor 7-day and 30-day retention curves.

3. **Set up analytics tracking** [Ref: T1]: Define North Star Metric [Ref: G4] (e.g., weekly active usage); create retention dashboards showing cohort retention by month; track activation funnel completion rates; set up A/B tests for each initiative.

4. **Validate with continuous discovery** [Ref: L4, A6]: Conduct weekly user interviews to understand retention drivers; use Opportunity Solution Trees [Ref: G10] to map user needs; test assumptions with small experiments before full rollout.

5. **Trade-offs & Alternatives**:
   - **Alternative framework**: ICE (Impact × Confidence × Ease) [Ref: L2] for faster scoring if RICE data is uncertain; trade-off: less precision but better for early-stage products or limited analytics.
   - **Risk consideration**: Engagement campaigns may feel spammy if over-targeted [Ref: A15]; mitigate by limiting frequency (max 2 emails/week) and providing opt-out.
   - **Common misconception**: Avoid focusing solely on vanity metrics like total signups; prioritize activated users and retained cohorts [Ref: G4, A9].

6. **Expected outcome**: With RICE-prioritized initiatives, expect 4–6% retention lift in first 3 months, reaching 10% by month 6; validate with cohort analysis comparing pre/post-initiative cohorts [Ref: T1, T3].

---

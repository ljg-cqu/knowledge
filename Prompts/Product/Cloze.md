# Cloze / Fill-in-the-Blank – Product Manager

Generates high-quality PM fill-in-the-blank assessments with structured citations and multi-dimensional evaluation.

---

# Part I: Specifications

## Specifications

### Foundation: Define the Task

- **Purpose**: Build a product management cloze bank for hiring, calibration, and upskilling.
- **Audience**: Senior/Director/VP PMs; interviewers; L&D partners.
- **Context & Constraints**: Domain strictly product management; 24–40 items; language distribution targets; framework variance supported via contested terms.
- **Assumptions**: Access to credible sources; internet connectivity; no PII; impartiality (no vendor bias).
- **Clarity**: Use plain language; define jargon via Glossary; avoid undefined acronyms.
- **Precision**: Use unambiguous blanks; consistent terminology; normalization (case-insensitive, trim, punctuation stripping) and numeric tolerances; explicit acceptable answer arrays.
- **Relevance**: Keep in-scope to product management; exclude tangential topics.

### Scope and Structure

- **Scope**: 24–40 items (senior/director/VP level PMs)
- **Format**: Unambiguous blanks (___) with acceptable answer arrays
- **Difficulty**: 20/40/40 balance (Foundational/Intermediate/Advanced)
- **Normalization**: Case-insensitive; trim whitespace; strip punctuation; define numeric tolerances
- **Grading**: Acceptance lists with tolerances; document borderline cases and partial credit
- **Contested Terms**: Include valid variants from different PM schools/regions/frameworks

### Coverage: MECE, Breadth, Depth

- **MECE**: Use clusters that are mutually exclusive and collectively exhaustive; prevent overlap between items across clusters.
- **Sufficiency**: Ensure each cluster covers essential sub-themes (definitions, metrics, frameworks, trade-offs).
- **Breadth**: Cover Strategy, Discovery & Validation, Prioritization & Roadmapping, Metrics & Growth, Stakeholder Management, Go-to-Market.
- **Depth**: Use difficulty balance to drive depth; advanced items probe rationale, edge cases, trade-offs.

### Grading Config (Example)

```json
{
  "normalization": {
    "caseInsensitive": true,
    "trimWhitespace": true,
    "stripPunctuation": true,
    "numericTolerance": 0.01
  },
  "items": [
    {
      "id": "1",
      "statement": "The framework that scores features by reach, impact, confidence, and effort is called ___.",
      "acceptableAnswers": ["RICE", "RICE prioritization"],
      "domain": "Prioritization",
      "difficulty": "Foundational"
    }
  ],
  "policies": {
    "significanceFilter": true,
    "logicStructure": "claim-reason-evidence",
    "fairness": "include-alternatives-when-contested"
  }
}
```

### Citation Standards

- **Languages**: ~60% EN, ~30% ZH, ~10% other (tag: [EN], [ZH], etc.)
- **Source Types**: (1) Frameworks (RICE, AARRR, JTBD, OKR); (2) Research (market analyses, user studies, cases); (3) Literature (books, articles, launches); (4) Tools (analytics, roadmapping, research platforms)
- **Format**: APA 7th with language tags
- **Inline Citation**: Use [Ref: ID] for factual claims, definitions, frameworks, specifications; narrative text uncited

### Reference Minimum Requirements

| Section | Floor | Content |
|---------|-------|---------|
| Glossary | ≥10 | RICE, AARRR, JTBD, North Star, PMF, OKR, PLG, OST, etc. |
| Tools | ≥5 | Analytics, roadmapping, research platforms, collaboration |
| Literature | ≥6 | PM frameworks, market analyses, launches, case studies |
| Citations | ≥12 | ~60% EN / ~30% ZH / ~10% other (APA 7th with tags) |

**Exception**: If unmet, document shortfall, rationale, and sourcing plan.

### Quality Gates

- **Recency**: ≥50% from last 3 years (≥70% for AI/platform)
- **Diversity**: ≥3 source types; single source <25%
- **Evidence**: ≥70% items with ≥1 citation; ≥30% with ≥2
- **Tool Details**: Pricing, users, update ≤18 months, integrations
- **Links**: Validate accessibility; prefer DOIs/archived URLs
- **Cross-refs**: All [Ref: ID] resolve

- **Significance**: Exclude trivial items; prioritize high-value content tied to outcomes.
- **Concision**: Statements ≤200 chars; rationales ≤2 sentences.
- **Logic**: Rationales follow claim → reason → evidence.
- **Risk/Value**: Advanced items include trade-offs, risks, costs, and benefits where applicable.
- **Fairness**: Acknowledge assumptions and viable alternatives for contested terms/frameworks.

> **Scaling**: For >40 items, increase floors ~1.5×; prioritize gates before floors.

### Pre-Submission Validation

Execute all steps; present results in validation table; fix failures and re-run until all PASS.

1. **Counts**: Glossary ≥10, Tools ≥5, Literature ≥6, APA ≥12, Items 24–40 (20/40/40)
2. **Citations**: ≥70% items with ≥1; ≥30% with ≥2
3. **Language**: EN 50-70%, ZH 20-40%, Other 5-15%
4. **Recency**: ≥50% last 3yr (≥70% AI/platform)
5. **Diversity**: ≥3 source types; single <25%
6. **Links**: All accessible/archived
7. **Cross-refs**: All [Ref: ID] resolve (G#/T#/L#/A#)
8. **Significance**: 100% items pass significance filter (non-trivial, outcome-relevant).
9. **Concision**: Statements ≤200 chars and rationales ≤2 sentences (report S/X and R/X).
10. **Logic**: Rationales follow claim → reason → evidence (spot-check ≥10% or ≥10 items).
11. **Fairness**: Contested items include assumptions/alternatives; variants present where applicable.
12. **Risk/Value**: ≥30% of Advanced items include trade-offs or risk/cost/benefit analysis.
13. **Practicality**: Grader config present; normalization/tolerance validated on sample items.
14. **Success Criteria**: All floors, gates, and checks PASS; validation report attached.

**Validation Report Template:**
```
| Check | Result | Status |
|-------|--------|--------|
| Floors | G:X T:Y L:Z A:W I:N (F/I/A) | PASS/FAIL |
| Citation coverage | X% ≥1, Y% ≥2 | PASS/FAIL |
| Language dist | EN:X% ZH:Y% Other:Z% | PASS/FAIL |
| Recency | X% last 3yr | PASS/FAIL |
| Source diversity | N types, max P% | PASS/FAIL |
| Links | Y/X accessible | PASS/FAIL |
| Cross-refs | Y/X resolved | PASS/FAIL |
| Significance | 100% items high-value | PASS/FAIL |
| Concision | S/X statements ≤200; R/X rationales ≤2 sentences | PASS/FAIL |
| Logic | Sample N follow claim→reason→evidence | PASS/FAIL |
| Fairness | Contested items include assumptions/alternatives | PASS/FAIL |
| Risk/Value | ≥30% advanced items include trade-offs | PASS/FAIL |
| Practicality | Grader config present; normalization tested | PASS/FAIL |
| Success criteria | All floors/gates/checks PASS | PASS/FAIL |
```
> **MANDATORY:** Stop on ANY failure; fix, regenerate, re-validate. Proceed only when all PASS.

### Submission Checklist
- [ ] All validation steps PASS
- [ ] All reference floors and quality gates met

### LLM-Friendly Guidelines Compliance
- **1. Context**: Part I → Foundation
- **2. Clarity**: Part I → Foundation; Glossary
- **3. Precision**: Scope & Structure → Normalization/Grading; Acceptable answers
- **4. Relevance**: Part I → Foundation
- **5. MECE**: Coverage; Part II → Step 1 Topic Planning
- **6. Sufficiency**: Reference Floors; Quality Gates
- **7. Breadth**: Clusters in Coverage/Step 1
- **8. Depth**: Difficulty balance; Advanced item requirements
- **9. Significance**: Quality Gates (Significance)
- **10. Concision**: Quality Gates (Concision) and Validation #9
- **11. Accuracy**: Citations policy; Cross-refs
- **12. Credibility**: Diversity/Recency gates; authoritative sources
- **13. Logic**: Quality Gates (Logic) and Validation #10
- **14. Risk/Value**: Quality Gates (Risk/Value) and Validation #12
- **15. Fairness**: Contested Terms; Quality Gates (Fairness) and Validation #11
- **16. Structure**: Part III → Output Template
- **17. Output Format**: TOC and formatting rules
- **18. Evidence**: APA citations and inline [Ref: ID]
- **19. Validation**: Part I → Pre-Submission Validation
- **20. Practicality**: Grading Config (Example)
- **21. Success Criteria**: Submission Checklist; Validation #14

---

# Part II: Instructions

## Instructions

Execute steps sequentially with quality checks before proceeding.

### Step 1: Topic Planning
1. Identify 4–6 PM clusters: Strategy | Discovery & Validation | Prioritization & Roadmapping | Metrics & Growth | Stakeholder Management | Go-to-Market
2. Allocate 4–8 items/cluster (total 24–40)
3. Assign difficulty: 20/40/40 balance (Foundational/Intermediate/Advanced)
4. **Verify**: Total 24–40; ratio ≈20/40/40

### Step 2: Reference Collection
1. **Glossary (≥10)**: RICE, AARRR, JTBD, North Star, PMF, OKR, Continuous Discovery, PLG, Feature Factory, OST
2. **Tools (≥5)**: Analytics (Mixpanel, Amplitude), Roadmapping (ProductBoard, Aha!), Research (Dovetail, UserTesting), Collaboration (Miro)
3. **Literature (≥6)**: EN (Cagan, Olsen, Torres, Perri, Patton, Klement); ZH (俞军, 梁宁, 苏杰)
4. **Citations (≥12)**: Assign IDs (G#/T#/L#/A#); tag language, year, type
5. **Verify**: Counts met; language ~60/30/10%; recency ≥50% last 3yr; ≥3 types

### Step 3: Item Generation
1. Write fill-in-the-blank statements (unambiguous, contextualized, framework/metric-focused)
2. Define acceptable answer arrays (frameworks, terms, metrics, principles)
3. Add rationale (1–2 sentences; cite [Ref: ID] for frameworks, data, best practices)
4. **Verify**: Every 5 items check statement clarity, citation coverage, answer quality

### Step 4: Reference Sections
1. Populate Glossary, Tools, Literature, APA with required fields
2. **Verify**: All [Ref: ID] resolve

### Step 5: Validation
Execute validation checks (Part I); fix failures; re-run until all PASS.

### Step 6: Submission
Verify checklist complete; submit when all PASS.

---

# Part III: Output Format

## Output Template

Start the output with a TOC (e.g., '## Contents') linking to all top-level headings and list items.

- Use lists, tables, diagrams, formulas, code blocks; diagrams in Mermaid; code with language-tagged fences.

```markdown
## Contents
- [Cloze Bank](#cloze-bank-items-1-n)
- [Reference Sections](#reference-sections)
  - [Glossary, Terminology & Acronyms](#glossary-terminology--acronyms)
  - [Product Tools & Platforms](#product-tools--platforms)
  - [Authoritative Literature & Case Studies](#authoritative-literature--case-studies)
  - [APA Style Source Citations](#apa-style-source-citations)

---

## Cloze Bank (Items 1–N)

### Item X

**Difficulty:** [Foundational/Intermediate/Advanced] | **Domain:** [Strategy/Discovery/Prioritization/Metrics/Stakeholder/GTM]

**Statement:** Fill-in-the-blank with product context, frameworks, or metrics

**Acceptable Answers:** Array of valid responses (frameworks, terms, metrics, principles)

**Rationale:** 1–2 sentences citing [Ref: ID] for frameworks, data, best practices

---

## Reference Sections

Assign IDs: Glossary (G1…Gn), Tools (T1…Tn), Literature (L1…Ln), APA (A1…An). Inline format: [Ref: G2, T3, A5]

### Glossary, Terminology & Acronyms

**G1. AARRR (Pirate Metrics)**  
Acquisition → Activation → Retention → Referral → Revenue framework for tracking growth across customer lifecycle. Used for SaaS metrics, funnel optimization. Related: HEART, North Star Metric

**G2. RICE**  
Reach × Impact × Confidence ÷ Effort scoring for feature prioritization. Use: roadmap planning, backlog ranking. Related: ICE, Value/Effort Matrix, KANO

**G3. JTBD (Jobs-to-be-Done)**  
Framework identifying underlying "job" users hire product to accomplish. Use: ideation, segmentation, competitive analysis. Related: Outcome-driven innovation

**G4. North Star Metric**  
Single metric capturing core product value; leading indicator of sustainable growth. Use: alignment, PLG, OKRs. Related: OMTM, Input/Output metrics

**G5. PMF (Product-Market Fit)**  
Degree product satisfies market demand; indicated by retention plateau and organic growth acceleration. Use: validation, pivot decisions, expansion. Related: Problem-solution fit, MVP

**G6. OKR (Objectives and Key Results)**  
Goal framework: Objectives (what) + Key Results (measurement). Use: quarterly planning, cross-functional alignment. Related: KPI, North Star, V2MOM

**G7. Continuous Discovery**  
Regular customer engagement via structured interviews/testing to inform decisions. Use: weekly interviews, opportunity trees, assumption testing. Related: Dual-track agile, Build-Measure-Learn

**G8. PLG (Product-Led Growth)**  
GTM strategy where product drives acquisition, conversion, expansion. Use: SaaS freemium, self-serve onboarding, viral loops. Related: PQLs, Time-to-Value, Expansion revenue

**G9. Feature Factory**  
Anti-pattern: shipping features (outputs) vs solving problems (outcomes). Use: transformation discussions, outcome-based PM. Related: Build trap, Empowered teams

**G10. Opportunity Solution Tree (OST)**  
Visual framework mapping outcomes → opportunities (needs/pains) → solutions. Used for discovery planning, ideation, assumption mapping. Related: HMW statements, User story mapping

[... continue for ≥10 entries ...]

---

### Product Tools & Platforms

**T1. Mixpanel** (Product Analytics)  
Features: Event tracking, funnel/cohort analysis, A/B testing, segmentation. Pricing: Freemium–Enterprise. Users: 8K+ (Uber, Netflix). Updated: Q3 2024 (AI insights). Integrations: Segment, Salesforce, Slack, Jira. PM use: Activation, adoption, retention. https://mixpanel.com

**T2. ProductBoard** (Roadmapping & Prioritization)  
Features: Feedback aggregation, value/effort matrix, roadmap views, customer portal. Pricing: $25/maker/mo–Enterprise. Users: 6K+ (Microsoft, Zoom). Updated: Q4 2024 (AI feedback analysis). Integrations: Jira, Slack, Salesforce, Intercom, Zendesk. PM use: Synthesis, RICE scoring, stakeholder comms. https://www.productboard.com

**T3. Amplitude** (Analytics & Experimentation)  
Features: Behavioral cohorts, retention/funnel analysis, A/B/n testing, predictive analytics. Pricing: Freemium–Enterprise. Users: 3.2K+ (PayPal, Ford). Updated: Q3 2024 (AI insights, predictive playbooks). Integrations: Segment, Braze, Optimizely, Salesforce. PM use: North Star tracking, conversion optimization, impact analysis. https://amplitude.com

**T4. Dovetail** (Research Repository)  
Features: Auto transcription, tagging/theming, highlight reels, sentiment analysis, journey visualization. Pricing: Freemium–Enterprise. Users: 3K+ (Atlassian, Canva). Updated: Q2 2024 (AI theme detection). Integrations: Zoom, Slack, Notion, Jira, UserTesting. PM use: Interview synthesis, JTBD mapping, discovery insights. https://dovetail.com

**T5. Miro** (Visual Collaboration)  
Features: Infinite canvas, templates (story/journey maps, matrices), real-time collab, AI assistant. Pricing: Freemium–Enterprise. Users: 80M+ (Dell, Cisco). Updated: Q4 2024 (enhanced AI). Integrations: Jira, Slack, Teams, Zoom, Figma, Asana. PM use: Story mapping, OST workshops, roadmaps, retrospectives. https://miro.com

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

## Example Item (Product Frameworks & Metrics)

### Item 1

**Difficulty:** Foundational | **Domain:** Product Frameworks & Metrics

**Statement:** The framework that scores features by reach, impact, confidence, and effort is called ___.

**Acceptable Answers:** [RICE, RICE prioritization]

**Rationale:** RICE [Ref: G2, A2] is a widely used product management framework for prioritizing features based on reach, impact, confidence, and effort.

---

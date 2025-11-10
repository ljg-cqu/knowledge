# Multiple-Choice Questions – Product Manager

Generate senior-level PM MCQ assessments with citations and multi-dimensional evaluation.

---

# Part I: Specifications

Quality requirements, standards, and constraints.

## Specifications

### Scope and Structure

- **Scope**: 40–80 MCQs for senior/director/VP PMs
- **Format**: 1–2 sentence stems, 4 options (one correct)
- **Difficulty**: 20% Foundational / 40% Intermediate / 40% Advanced
- **Distractors**: Common misconceptions, outdated practices, competing frameworks
- **Rationale**: 1–2 sentences with citations
- **Grading**: Machine-gradable, no partial credit

### Citation Standards

- **Languages**: 60% EN / 30% ZH / 10% other (tag: [EN], [ZH])
- **Source Types**: (1) Frameworks (RICE, AARRR, JTBD, OKR); (2) Research/data; (3) Literature; (4) Tools/platforms
- **Format**: APA 7th with language tags
- **Inline**: Use [Ref: ID] in rationales for frameworks, data, metrics, best practices

### Reference Minimum Requirements

| Section | Minimum | Examples |
|---------|---------|----------|
| Glossary | 10 | RICE, AARRR, JTBD, North Star, PMF, OKR, PLG, OST |
| Tools | 5 | Analytics, roadmapping, research, collaboration |
| Literature | 6 | Frameworks, analyses, launches, case studies |
| Citations | 12 | 60% EN / 30% ZH / 10% other (APA 7th) |

**Exception**: If unmet, state shortfall + rationale + plan.

### Quality Gates

- **Recency**: 50% from last 3 years (70% for AI/platform)
- **Diversity**: 3+ source types; no single source >25%
- **Evidence**: 70% questions have 1+ citation; 30% have 2+ citations
- **Tool Details**: Pricing, users, update ≤18 months, integrations
- **Links**: Validate accessibility; use DOIs/archived URLs
- **Cross-refs**: All [Ref: ID] resolve

> **Scaling**: >80 questions: increase minimums by 1.5×; prioritize gates over minimums.

### Pre-Submission Validation

Execute all steps. Present validation report. Fix failures and re-run until all PASS.

| Step | Check | Target |
|------|-------|--------|
| 1 | Counts | Glossary ≥10, Tools ≥5, Literature ≥6, APA ≥12, Questions 40–80 (20/40/40) |
| 2 | Citations | 70% questions have 1+; 30% have 2+ |
| 3 | Language | EN 50-70%, ZH 20-40%, Other 5-15% |
| 4 | Recency | 50% from last 3yr (70% for AI/platform) |
| 5 | Diversity | 3+ source types; no single >25% |
| 6 | Links | All accessible or archived |
| 7 | Cross-refs | All [Ref: ID] resolve (G#/T#/L#/A#) |

**Report Template:**
```
| Check | Result | Status |
|-------|--------|--------|
| Counts | G:X T:Y L:Z A:W Q:N (F/I/A) | PASS/FAIL |
| Citations | X% ≥1, Y% ≥2 | PASS/FAIL |
| Language | EN:X% ZH:Y% Other:Z% | PASS/FAIL |
| Recency | X% last 3yr | PASS/FAIL |
| Diversity | N types, max P% | PASS/FAIL |
| Links | Y/X accessible | PASS/FAIL |
| Cross-refs | Y/X resolved | PASS/FAIL |
```
> **MANDATORY**: Stop if ANY check fails. Fix, regenerate, re-validate. Proceed only when ALL PASS.

### Submission Checklist
- [ ] All validation steps PASS
- [ ] All minimums met + quality gates passed

---

# Part II: Instructions

Generation workflow with quality checks at each step.

## Instructions

### Step 1: Topic Planning
1. Identify 4–6 clusters: Strategy | Discovery | Prioritization | Metrics | Stakeholder | Go-to-Market
2. Allocate 8–16 MCQs per cluster (total 40–80)
3. Assign difficulty: 20/40/40 (Foundational/Intermediate/Advanced)
4. **Check**: Total = 40–80, ratio ≈ 20/40/40

### Step 2: Reference Collection
1. **Glossary (10+)**: RICE, AARRR, JTBD, North Star, PMF, OKR, Continuous Discovery, PLG, Feature Factory, OST
2. **Tools (5+)**: Mixpanel/Amplitude, ProductBoard/Aha!, Dovetail/UserTesting, Miro
3. **Literature (6+)**: Cagan, Olsen, Torres, Perri, Patton, Klement + ZH (俞军, 梁宁, 苏杰)
4. **Citations (12+)**: Tag language, year, type; assign IDs (G#/T#/L#/A#)
5. **Check**: Counts, language 60/30/10%, recency 50%+ last 3yr, 3+ types

### Step 3: MCQ Generation
1. Write stem (1–2 sentences: context, frameworks, metrics)
2. Provide 4 options (one correct, three plausible distractors)
3. Rationale (1–2 sentences with [Ref: ID])
4. **Check**: Every 5 MCQs verify length, citations, distractor quality

### Step 4: References
1. Populate Glossary/Tools/Literature/APA
2. **Check**: All [Ref: ID] resolve

### Step 5: Validation
Execute all checks. Fix failures; re-validate until all PASS.

### Step 6: Submit
Verify checklist. Submit when all PASS.

---

# Part III: Output Format

MCQ bank template structure.

## Output Format

Start the output with a TOC (e.g., '## Contents') linking to all top-level headings and list items.

- Use lists tables diagrams formulas code blocks; diagrams in Mermaid; code with language-tagged fences.

Use this structure:

```markdown
## Contents
- [MCQ Bank](#mcq-bank-questions-1-n)
- [Reference Sections](#reference-sections)
  - [Glossary, Terminology & Acronyms](#glossary-terminology--acronyms)
  - [Product Tools & Platforms](#product-tools--platforms)
  - [Authoritative Literature & Case Studies](#authoritative-literature--case-studies)
  - [APA Style Source Citations](#apa-style-source-citations)

---

## MCQ Bank (Questions 1–N)

### Question X

**Difficulty:** [Foundational/Intermediate/Advanced] | **Domain:** [Strategy/Discovery/Prioritization/Metrics/Stakeholder/GTM]

**Stem:** (1–2 sentences: context, frameworks, metrics)

A. [Option 1]
B. [Option 2]
C. [Option 3]
D. [Option 4]

**Correct Answer:** [A/B/C/D]

**Rationale:** (1–2 sentences with [Ref: ID])

---

## Reference Sections

Reference IDs: Glossary (G1…Gn), Tools (T1…Tn), Literature (L1…Ln), APA (A1…An). Inline: [Ref: G2, T3, A5].

### Glossary, Terminology & Acronyms

**G1. AARRR (Pirate Metrics)**  
Acquisition → Activation → Retention → Referral → Revenue. Tracks growth across customer lifecycle. Use: SaaS metrics, funnel optimization. Related: HEART, North Star

**G2. RICE Prioritization**  
Reach × Impact × Confidence ÷ Effort. Feature scoring formula. Use: roadmap planning, backlog ranking. Related: ICE, Value/Effort, KANO

**G3. Jobs-to-be-Done (JTBD)**  
Underlying "job" users hire products to accomplish (vs demographics). Use: ideation, segmentation, competitive analysis. Related: Outcome-driven innovation

**G4. North Star Metric**  
Single metric capturing core value; leading indicator of sustainable growth. Use: alignment, PLG, OKRs. Related: OMTM, Input/Output metrics

**G5. Product-Market Fit (PMF)**  
Degree product satisfies market demand; retention flattens, organic growth accelerates. Use: validation, pivots, expansion. Related: Problem-solution fit, MVP

**G6. OKR (Objectives and Key Results)**  
Objectives = what to achieve; Key Results = how to measure. Use: quarterly planning, alignment. Related: KPI, North Star, V2MOM

**G7. Continuous Discovery**  
Regular customer engagement via structured interviews/testing (vs periodic projects). Use: weekly interviews, opportunity trees, assumption testing. Related: Dual-track agile, Build-Measure-Learn

**G8. Product-Led Growth (PLG)**  
Product drives acquisition, conversion, expansion (vs sales-led). Use: SaaS freemium, self-serve, viral loops. Related: PQLs, Time-to-Value, Expansion revenue

**G9. Feature Factory**  
Anti-pattern: shipping features (outputs) vs solving problems (outcomes). Use: transformation, outcome-based PM. Related: Build trap, Empowered teams

**G10. Opportunity Solution Tree (OST)**  
Visual: outcomes → opportunities (needs/pains) → solutions. Use: discovery, ideation, assumption mapping. Related: HMW, User story mapping

[... 10+ entries ...]

---

### Product Tools & Platforms

**T1. Mixpanel** (Product Analytics)  
Event tracking, funnel/cohort analysis, A/B testing, segmentation. Freemium to Enterprise. 8K+ companies (Uber, Netflix). Updated Q3 2024 (AI insights). Integrates: Segment, Salesforce, Slack, Jira. Use: activation, adoption, retention. https://mixpanel.com

**T2. ProductBoard** (Roadmapping)  
Feedback aggregation, prioritization matrix, roadmap views, portal. $25/maker/mo to Enterprise. 6K+ teams (Microsoft, Zoom). Updated Q4 2024 (AI analysis). Integrates: Jira, Slack, Salesforce, Intercom, Zendesk. Use: synthesis, RICE, stakeholder comms. https://www.productboard.com

**T3. Amplitude** (Analytics & Experimentation)  
Cohorts, retention/funnel, A/B/n testing, predictive analytics. Freemium to Enterprise. 3.2K+ companies (PayPal, Ford). Updated Q3 2024 (AI, playbooks). Integrates: Segment, Braze, Optimizely, Salesforce. Use: North Star, conversion, impact. https://amplitude.com

**T4. Dovetail** (Research Repository)  
Transcription, tagging/theming, highlights, sentiment, journey viz. Freemium to Enterprise. 3K+ teams (Atlassian, Canva). Updated Q2 2024 (AI themes). Integrates: Zoom, Slack, Notion, Jira, UserTesting. Use: synthesis, JTBD, discovery. https://dovetail.com

**T5. Miro** (Visual Collaboration)  
Infinite canvas, templates (story/journey maps, matrices), real-time collab, AI. Freemium to Enterprise. 80M+ users (Dell, Cisco). Updated Q4 2024 (AI). Integrates: Jira, Slack, Teams, Zoom, Figma, Asana. Use: story mapping, OST, roadmaps, retros. https://miro.com

[... 5+ entries ...]

---

### Authoritative Literature & Case Studies

**L1. Cagan, M. (2017). *Inspired* (2nd ed.). Wiley.**  
Discovery vs delivery, empowered teams. Foundational principles.

**L2. Olsen, D. (2015). *The Lean Product Playbook*. Wiley.**  
6-step PMF process. Strategy, validation.

**L3. Perri, M. (2018). *Escaping the Build Trap*. O'Reilly.**  
Outcomes over outputs. Feature factory to outcome-driven culture.

**L4. Torres, T. (2021). *Continuous Discovery Habits*. Product Talk LLC.**  
Weekly touchpoints, opportunity solution trees. Discovery process.

**L5. Patton, J. (2014). *User Story Mapping*. O'Reilly.**  
Mapping by user journey (vs flat backlog). Roadmaps, MVP scoping.

**L6. Klement, A. (2016). *When Coffee and Kale Compete*. Independent.**  
JTBD: functional/emotional/social jobs. Positioning, competitive analysis.

[... 6+ entries ...]

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

[... 12+ entries: 60% EN / 30% ZH / 10% other ...]
```

---

## Example MCQ (Product Strategy & Prioritization)

### Question 1

**Difficulty:** Intermediate | **Domain:** Product Strategy, Prioritization

**Stem:** Which framework is best suited for prioritizing features based on reach, impact, confidence, and effort?

A. AARRR
B. RICE
C. JTBD
D. OKR

**Correct Answer:** B

**Rationale:** RICE [Ref: G2, A2] evaluates features using reach, impact, confidence, effort—ideal for roadmap planning. AARRR = growth metrics, JTBD = user needs, OKR = goals.

---

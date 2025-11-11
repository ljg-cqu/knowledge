# True/False Statements – Product Manager

Generate senior-level PM true/false assessments (18–32 statements) with citations, difficulty distribution (20/40/40), and validation gates.

---

# Part I: Specifications

## Specifications

### Purpose & Context
- Audience: senior/director/VP PMs; digital products (B2B/B2C, platform, marketplace, SaaS).
- Constraints: statements must be evaluable as true/false; ≤2 lines; avoid double negatives.
- Assumptions: modern product practices; cross-functional collaboration; data-informed.
- Exclusions: trivial UI facts; company-specific processes.
- Relevance: focus on high-leverage product decisions.

### Scope and Structure

- **Scope**: 18–32 statements (senior/director/VP PM level)
- **Format**: Declarative (≤2 lines); no double negatives
- **Difficulty**: 20% Foundational / 40% Intermediate / 40% Advanced
- **Rationale**: 1–2 sentences with [Ref: ID] citations
- **Justification** (optional): 2–3 sentences clarifying context/assumptions
- **Grading**: Binary (True/False)
- **Context-dependent claims**: Rationale specifies assumptions/conditions
- **Clarity & Precision**: Avoid undefined jargon; define terms in Glossary; use consistent terminology.
- **MECE & Sufficiency**: Clusters and statements are non-overlapping and collectively complete.
- **Breadth & Depth**: Cover multiple perspectives (B2B/B2C, PLG/SLG, platform/marketplace) with advanced trade-offs.
- **Significance & Concision**: Prioritize high-value topics; remove trivial or redundant items.

### Citation Standards

- **Languages**: 60% EN / 30% ZH / 10% other (tag: [EN], [ZH])
- **Source Types**: (1) Frameworks (RICE, AARRR, JTBD, OKR); (2) Research/data; (3) PM literature; (4) Tools/platforms
- **Format**: APA 7th + language tags
- **Inline**: [Ref: ID] for frameworks, data, metrics, best practices

### Reference Floors

| Section | Min | Content |
|---------|-----|---------|
| Glossary | 10 | RICE, AARRR, JTBD, North Star, PMF, OKR, Continuous Discovery, PLG, Feature Factory, OST |
| Tools | 5 | Analytics, roadmapping, research, collaboration |
| Literature | 6 | Frameworks, market analyses, launches, case studies |
| Citations | 12 | 60% EN / 30% ZH / 10% other (APA 7th + tags) |

**Exception**: If unmet, document shortfall + rationale + plan.

### Quality, Logic, Fairness, Risk/Value
- **Accuracy & Credibility**: Verify facts; prefer authoritative sources/DOIs; archive links; flag uncertainty with [Uncertain].
- **Logic**: Use clear Claim → Evidence → Warrant reasoning in rationales.
- **Fairness**: Acknowledge assumptions, limitations, alternatives, counterarguments, and trade-offs when relevant.
- **Risk/Value**: Summarize risks, costs, benefits, and suggest mitigations for advanced/strategic claims.
- **Terminology Consistency**: Align language with Glossary; avoid ambiguous quantifiers.
- **On-Topic Relevance**: Keep statements strictly within product management scope.

### Quality Gates

- **Recency**: 50% from last 3 years (70% for AI/platform)
- **Diversity**: ≥3 source types; max 25% from single source
- **Evidence**: 70% statements with ≥1 citation; 30% with ≥2
- **Tool Details**: Pricing, user base, update ≤18mo, integrations
- **Links**: Accessible or archived (DOIs preferred)
- **Cross-refs**: All [Ref: ID] resolve

> **Scaling**: For >32 statements, increase floors ×1.5. Prioritize gates first.

### Success Criteria (Measurable)
- All Pre-Submission checks PASS (incl. guideline compliance).
- Counts met: G≥10, T≥5, L≥6, A≥12, S=18–32 with 20/40/40 difficulty.
- Coverage: 4–6 clusters; MECE; breadth across B2B/B2C, PLG/SLG, platform/marketplace.
- Evidence: ≥70% statements have ≥1 citation; ≥30% have ≥2; sources meet recency/diversity caps.
- Quality: No double negatives; statements ≤2 lines; rationale ≤2 sentences; on-topic; no trivial items.

### Pre-Submission Validation

Execute all steps. Fix failures and re-run until all PASS.

1. **Counts**: G≥10, T≥5, L≥6, A≥12, S=18–32 (20/40/40)
2. **Citations**: 70% statements ≥1; 30% ≥2
3. **Language**: EN 50–70%, ZH 20–40%, Other 5–15%
4. **Recency**: 50% from last 3yr (70% for AI/platform)
5. **Diversity**: ≥3 types; max 25% single source
6. **Links**: All accessible/archived
7. **Cross-refs**: All [Ref: ID] resolve (G#/T#/L#/A#)
8. **Guidelines**: All 21 LLM-friendly guidelines satisfied (see Compliance Map).

**Report Template:**
```
| Check | Result | Status |
|-------|--------|--------|
| Floors | G:X T:Y L:Z A:W S:N (F/I/A) | PASS/FAIL |
| Citations | X% ≥1, Y% ≥2 | PASS/FAIL |
| Language | EN:X% ZH:Y% Other:Z% | PASS/FAIL |
| Recency | X% last 3yr | PASS/FAIL |
| Diversity | N types, max P% | PASS/FAIL |
| Links | Y/X accessible | PASS/FAIL |
| Cross-refs | Y/X resolved | PASS/FAIL |
| Guidelines | 21/21 satisfied | PASS/FAIL |
```
> **MANDATORY:** Stop on ANY FAIL. Fix, regenerate, re-validate. Proceed only when ALL PASS.

### Submission Checklist
- [ ] All validation PASS
- [ ] All floors + gates met

### LLM-Friendly Guidelines Compliance Map
For each guideline, where it is enforced:
- 1. **Context**: Purpose & Context; Scope and Structure.
- 2. **Clarity**: Scope and Structure (Clarity & Precision); Step 3 checks.
- 3. **Precision**: Glossary usage; avoid ambiguous quantifiers; Step 3.
- 4. **Relevance**: Purpose & Context (On-Topic); Step 3.
- 5. **MECE**: Step 1 planning; Scope (MECE & Sufficiency).
- 6. **Sufficiency**: Floors + cluster coverage; Success Criteria.
- 7. **Breadth**: Step 1 contexts (B2B/B2C, PLG/SLG, platform/marketplace).
- 8. **Depth**: Difficulty 20/40/40; advanced trade-offs.
- 9. **Significance**: Scope (Significance); Success Criteria (no trivial items).
- 10. **Concision**: Format constraints; Step 3; Success Criteria.
- 11. **Accuracy**: Citations; Cross-refs; Pre-Submission checks.
- 12. **Credibility**: Quality Gates (recency/diversity/DOIs/archives).
- 13. **Logic**: Quality section (Claim → Evidence → Warrant); Step 3.
- 14. **Risk/Value**: Quality section; Optional Justification guidance.
- 15. **Fairness**: Quality section; Justification includes alternatives/trade-offs.
- 16. **Structure**: Output Format; use lists/tables/diagrams.
- 17. **Output Format**: TOC + sections + Validation Report.
- 18. **Evidence**: APA + language tags; [Uncertain] flag when applicable.
- 19. **Validation**: Pre-Submission + Validation Report.
- 20. **Practicality**: Tool details; actionable statements for assessment use.
- 21. **Success Criteria**: Dedicated section; Submission Checklist.

---

# Part II: Instructions

Execute steps sequentially with inline validation.

### Step 1: Topic Planning
1. Identify 4–6 clusters: Strategy | Discovery | Prioritization | Metrics | Stakeholder | GTM. Ensure MECE; plan breadth across B2B/B2C, PLG/SLG, platform/marketplace.
2. Allocate 3–7 statements/cluster (total 18–32). Avoid overlap across clusters and statements.
3. Assign difficulty (20/40/40) with advanced items including trade-offs and strategic risks.
4. **Check**: Total 18–32; ratio 20/40/40; cluster coverage; MECE/breadth PASS.

### Step 2: Reference Collection
1. **Glossary (10)**: RICE, AARRR, JTBD, North Star, PMF, OKR, Continuous Discovery, PLG, Feature Factory, OST
2. **Tools (5)**: Mixpanel/Amplitude, ProductBoard/Aha!, Dovetail/UserTesting, Miro
3. **Literature (6)**: Cagan, Olsen, Torres, Perri, Patton, Klement + ZH (俞军, 梁宁, 苏杰)
4. **Citations (12)**: Tag language, year, type; assign IDs (G#/T#/L#/A#)
5. **Check**: Counts; language 60/30/10%; recency 50% <3yr; ≥3 source types; DOIs/archives; diversity cap ≤25% per source.

### Step 3: Statement Generation
1. Write declarative claim (≤2 lines)
2. Provide answer (T/F) + rationale (1–2 sentences with [Ref: ID]) using Claim → Evidence → Warrant.
3. Optional justification (2–3 sentences) to clarify assumptions, limitations, alternatives, trade-offs, and risks/mitigations.
4. Avoid ambiguous quantifiers; define any term via Glossary; keep terminology consistent; stay on topic.
5. If uncertainty remains, explicitly tag [Uncertain] and narrow scope/assumptions.
6. **Check**: Every 5 statements verify length; citations; clarity; logic; fairness/trade-offs; MECE; on-topic.

### Step 4: Reference Sections
1. Populate all sections (G/T/L/A) with required fields
2. **Check**: All [Ref: ID] resolve

### Step 5: Validation
Execute all 8 validation steps. Fix failures; re-run until PASS.

### Step 6: Submission
Verify checklist. Submit when all PASS.

---

# Part III: Output Format

Start the output with a TOC (e.g., '## Contents') linking to all top-level headings and list items.

- Use lists tables diagrams formulas code blocks; diagrams in Mermaid; code with language-tagged fences.

```markdown
## Contents
- [True/False Bank](#truefalse-bank)
- [References](#references)
  - [Glossary](#glossary-terminology--acronyms)
  - [Tools](#product-tools--platforms)
  - [Literature](#authoritative-literature--case-studies)
  - [Citations](#apa-style-source-citations)
- [Validation Report](#validation-report)

---

## True/False Bank (Statements 1–N)

### Statement X

**Difficulty:** [Foundational/Intermediate/Advanced] | **Domain:** [Strategy/Discovery/Prioritization/Metrics/Stakeholder/GTM]

**Statement:** (Concise, declarative product claim, ≤2 lines)

**Answer:** [True/False]

**Rationale:** (1–2 sentences, cite [Ref: ID] for frameworks, data, best practices)

**Optional Justification:** (2–3 sentences; clarify assumptions/limitations; alternatives/counterarguments; trade-offs; risk/cost/benefit + mitigation. Tag [Uncertain] if applicable.)

---

## References

Assign IDs: Glossary (G1…Gn), Tools (T1…Tn), Literature (L1…Ln), Citations (A1…An). Inline format: [Ref: G2, T3, A5].

### Glossary, Terminology & Acronyms

**G1. AARRR (Pirate Metrics)**  
Acquisition → Activation → Retention → Referral → Revenue. Use: SaaS metrics, funnel optimization. Related: HEART, North Star

**G2. RICE Prioritization**  
Reach × Impact × Confidence ÷ Effort. Use: Roadmap planning, backlog ranking. Related: ICE, Value/Effort, KANO

**G3. Jobs-to-be-Done (JTBD)**  
Underlying "job" users hire product for (vs demographics). Use: Feature ideation, segmentation, competitive analysis. Related: Outcome-driven innovation

**G4. North Star Metric**  
Single metric capturing core value; leading indicator of growth. Use: Alignment, PLG, OKRs. Related: OMTM, Input/Output metrics

**G5. Product-Market Fit (PMF)**  
Product satisfies market demand; retention flattens, organic growth accelerates. Use: Validation, pivot decisions, expansion. Related: Problem-solution fit, MVP

**G6. OKR (Objectives and Key Results)**  
Objectives = what; Key Results = how to measure. Use: Quarterly planning, alignment. Related: KPI, North Star, V2MOM

**G7. Continuous Discovery**  
Regular customer engagement via structured interviews/testing (vs periodic). Use: Weekly interviews, opportunity trees, assumption testing. Related: Dual-track agile, Build-Measure-Learn

**G8. Product-Led Growth (PLG)**  
Product drives acquisition, conversion, expansion (vs sales-led). Use: Freemium, self-serve, viral loops. Related: PQLs, Time-to-Value, Expansion revenue

**G9. Feature Factory**  
Anti-pattern: shipping features (outputs) vs solving problems (outcomes). Use: Transformation, outcome-based PM. Related: Build trap, Empowered teams

**G10. Opportunity Solution Tree (OST)**  
Outcomes → opportunities → solutions. Use: Discovery planning, ideation, assumption mapping. Related: HMW, User story mapping

[... continue for ≥10 entries ...]

---

### Product Tools & Platforms

**T1. Mixpanel** (Analytics)  
Event tracking, funnels, cohorts, A/B tests, segmentation. Freemium–Enterprise. 8K+ companies (Uber, Netflix). Q3 2024 (AI insights). Integrates: Segment, Salesforce, Slack, Jira. Use: Activation, adoption, retention. https://mixpanel.com

**T2. ProductBoard** (Roadmapping)  
Feedback aggregation, prioritization matrix, roadmaps, customer portal. $25/maker/mo–Enterprise. 6K+ teams (Microsoft, Zoom). Q4 2024 (AI feedback). Integrates: Jira, Slack, Salesforce, Intercom, Zendesk. Use: Synthesis, RICE, stakeholder comms. https://www.productboard.com

**T3. Amplitude** (Analytics & Experimentation)  
Cohorts, retention/funnel, A/B/n tests, predictive analytics. Freemium–Enterprise. 3.2K+ companies (PayPal, Ford). Q3 2024 (AI, predictive playbooks). Integrates: Segment, Braze, Optimizely, Salesforce. Use: North Star, conversion, impact. https://amplitude.com

**T4. Dovetail** (Research Repository)  
Transcription, tagging, highlights, sentiment, journey maps. Freemium–Enterprise. 3K+ teams (Atlassian, Canva). Q2 2024 (AI themes). Integrates: Zoom, Slack, Notion, Jira, UserTesting. Use: Interview synthesis, JTBD, discovery. https://dovetail.com

**T5. Miro** (Collaboration)  
Infinite canvas, templates (story maps, journeys, matrices), real-time, AI. Freemium–Enterprise. 80M+ users (Dell, Cisco). Q4 2024 (AI). Integrates: Jira, Slack, Teams, Zoom, Figma, Asana. Use: Story mapping, OST, roadmaps, retros. https://miro.com

[... continue for ≥5 entries ...]

---

### Authoritative Literature & Case Studies

**L1. Cagan, M. (2017). *Inspired* (2nd ed.). Wiley.**  
Discovery vs delivery, empowered teams. Foundational principles.

**L2. Olsen, D. (2015). *The Lean Product Playbook*. Wiley.**  
6-step PMF process. Strategy, validation.

**L3. Perri, M. (2018). *Escaping the Build Trap*. O'Reilly.**  
Outcomes over outputs. Transformation from feature factory.

**L4. Torres, T. (2021). *Continuous Discovery Habits*. Product Talk LLC.**  
Weekly touchpoints, OST. Discovery design.

**L5. Patton, J. (2014). *User Story Mapping*. O'Reilly.**  
Journey-based mapping (vs flat backlog). Roadmaps, MVP scoping.

**L6. Klement, A. (2016). *When Coffee and Kale Compete*. Independent.**  
JTBD: functional/emotional/social jobs. Positioning, competitive analysis.

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

---

## Validation Report

Fill the table and link evidence. All metrics must PASS before submission.

```
| Check | Result | Status |
|-------|--------|--------|
| Floors | G:X T:Y L:Z A:W S:N (F/I/A) | PASS/FAIL |
| Citations | X% ≥1, Y% ≥2 | PASS/FAIL |
| Language | EN:X% ZH:Y% Other:Z% | PASS/FAIL |
| Recency | X% last 3yr | PASS/FAIL |
| Diversity | N types, max P% | PASS/FAIL |
| Links | Y/X accessible | PASS/FAIL |
| Cross-refs | Y/X resolved | PASS/FAIL |
| Guidelines | 21/21 satisfied | PASS/FAIL |
```

---

## Example Statement (Product Metrics & Strategy)

### Statement 1

**Difficulty:** Foundational | **Domain:** Metrics & Strategy

**Statement:** The North Star Metric is always a lagging indicator of product success.

**Answer:** False

**Rationale:** North Star is a leading indicator of sustainable growth, not lagging [Ref: G4, L1, T3].

**Justification:** Best practice: select metrics predicting future value and aligning teams on proactive actions; trade-offs exist between input/output metrics. Risk/Value: high leverage, low risk if paired with guardrail metrics. [Ref: L1, G4].

---

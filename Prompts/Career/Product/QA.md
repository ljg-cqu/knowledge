---
last_updated: 2025-11-18
status: Reviewed
owner: ljg-cqu
---

# PM Interview Q&A Generator

**Purpose**: Generate scenario-based questions for senior PM interviews, focusing on judgment in decision-critical scenarios (e.g., >$1M impact, strategic pivots, >5% churn). Emphasize stakeholder navigation, trade-offs, strategic ambiguity. Exclude trivia, design, junior tasks, technical questions.

**Constraints**: Answers 150-250 words; 70% with citations; 100% decision-critical; senior level.

**Assumptions**: Industry context generic or provided; text output.

**Limitations**: Generic scenarios lack nuance; citations vary in recency; frameworks need context.

**Terms**:
- **Q&A**: Scenario pair testing judgment.
- **Floor**: Minimum threshold (≥ value = pass).
- **Quality Gate**: Mandatory checkpoint (fail = stop/fix).
- **Difficulty**: F=execution, I=strategy/trade-offs, A=portfolio/vision/P&L.
- **Dimensions**: Lenses (metrics, users, stakeholders, risk, time).
- **Decision-Critical**: Meets ≥1: Blocks Decision (>$1M impact), Creates Risk (>5% churn), Affects ≥2 Stakeholder Roles, Requires Action (actively evolving), Quantified Impact.

## Guidelines

### Quantitative Guidelines
- Q&A: 5-7 total, balanced difficulty, 150-250 words/answer, 70% with ≥1 citation, each ≥2 dimensions.
- Topics: Strategy & Prioritization (2), Metrics & Decision-Making (2), Stakeholder Alignment (1), optional GTM (1).
- References: Glossary ≥6 terms, Tools ≥3, Literature ≥3 (≥1 ZH), Citations ≥5 APA 7th.
- Visuals: ≥1 diagram + table per topic.

### Citation Standards
- Format: APA 7th + language tag. Inline: [Ref: ID].
- Distribution: 50-70% EN, 20-40% ZH, 5-15% other.
- Types: ≥3 (frameworks, research, case studies, tools).

### Process
1. Plan: Select 5-7 Q&A across topics, balanced difficulty.
2. Build References: Create glossary, tools, literature, citations. Check quality gates.
3. Generate Q&A: Scenario questions testing judgment. Answers with framework, dimensions, steps, trade-offs, communication, criteria, citations.
4. Create Visuals: ≥1 per topic, reference in answers.
5. Populate References: Format as specified.
6. Validate: Check floors, citations, criticality.
7. Final Review: Ensure clarity, realism, balance.

### Quality Gates
Fail any = stop/fix:
1. Recency: 40% references from last 5 years.
2. Diversity: ≥3 citation types.
3. Evidence: Each topic ≥2 authoritative + ≥1 tool.
4. Tools: Include pricing, users, updates, integrations.
5. References: Accessible links.
6. Cross-refs: 100% resolve, consistent.

## Success Criteria
- Interview Quality: 80% elicit judgment (baseline 50% trivia).
- Hiring Accuracy: 70% show senior judgment in 6mo (baseline 40%).
- Citations: 70% answers with ≥1 citation.
- Impact: 100% ≥$1M revenue/strategic.

Target: Reduce hiring risk by 60% via structured evaluations.

## Question Quality
Review each; rewrite if fails ≥2:
1. Clarity: Single ask (e.g., "Prioritize activation vs. churn?").
2. Signal: Tests judgment (scenario-based).
3. Depth: Enables trade-offs (alternatives).
4. Realism: Senior PM (complex constraints).
5. Discriminative: Application over recall ("When can RICE mislead?" vs. "What is RICE?").
6. Alignment: Difficulty fits seniority (F execution, I trade-offs, A vision/P&L).

## Output Format

### A. TOC
1. Topic Areas Overview | 2. Questions by Topic (3-4 topics) | 3. References (Glossary, Tools, Literature, Citations) | 4. Validation Report.

### B. Topic Overview
**Total**: [5-7] | **Difficulty**: [X]F ([Y]%) / [X]I ([Y]%) / [X]A ([Y]%) | **Coverage**: 3-4 decision-critical PM competencies.

| Topic          | Range  | Count | Mix      | Artifacts       | Decision Criticality |
|----------------|--------|-------|----------|-----------------|----------------------|
| Strategy & Prioritization | Q1-Q2  | 2   | 1F/1I | 1 diagram+table | Blocks decision |
| Metrics & Decision-Making | Q3-Q4  | 2   | 1F/1I | 1 diagram+table | Creates risk |
| Stakeholder Alignment | Q5  | 1   | 1I | 1 diagram+table | Affects ≥2 roles |
| GTM (Optional) | Q6-Q7 | 1-2     | 1I or 1A | 1 diagram+table | Actively evolving |
|   | **Total**      |        | **5-7**| **balanced mix** | **compressed** | 100% decision-critical |

Legend: F=execution | I=strategy/trade-offs | A=portfolio/vision/P&L.

### C. Q&A Format

**Topic 1: [Title]**

**Q1: [Full Question]**

**Difficulty**: [F/I/A] | **Topic**: [Area]

**Decision Criticality**: [Blocks/Risk/Stakeholders/Evolving/Quantified] - [Justification]

**Key Insight**: [1 sentence—specific dilemma/tension]

**Answer** (150-250 words): Framework [Ref: G#/A#] | ≥2 dimensions | Concrete steps | Trade-offs/alternatives | Stakeholder communication | Success criteria | ≥1 [Ref: ID]

**Artifact** *(optional)*: Matrix, journey, dashboard, roadmap.

### D. Reference Formats

**Glossary**: **G#. Term (Acronym)** | Definition | Use cases | Related | Limitations | Alphabetize.

**Tools**: **T#. Tool (Category)** | Description | Pricing | Users | Update (Q# YYYY) | Integrations (key ones) | PM use case | URL | Group by category.

**Literature**: **L#. Author, Title, Year** | Summary (focus/frameworks) | Relevance | Group by language (EN, then ≥1 ZH).

**Citations**: **A#. [Citation] [Lang]** | APA 7th format with language tags.

## Example

**Q1: How do you evaluate building a feature requested by top 5 enterprise customers (40% revenue) that doesn't align with product vision for the mass market?**

**Difficulty**: A | **Topic**: Strategy & Prioritization

**Key Insight**: Tests revenue protection (enterprise retention) vs. long-term PMF (mass-market scalability); distinguishes PMs navigating executive pressure from those defaulting to pleasing customers or rigid vision adherence.

**Answer** (248 words):

Use multi-dimensional evaluation [Ref: A1]. **First, discover JTBD** [Ref: A7]—what problem are customers solving? Surface requests often mask deeper needs revealing generalized solutions [Ref: A6].

**Second, quantify with RICE** [Ref: G2]. Enterprise: Reach (5/$2M), Impact (high retention/low acquisition), Confidence (high), Effort (unknown if custom). Mass-market: Reach (5K+ users), Impact (med/user, high cumulative), Confidence (med), Effort (similar). RICE won't capture strategic value—use decision matrix [Ref: T2].

**Third, assess against North Star** [Ref: G4]. Does this move toward outcomes or become feature factory [Ref: G9]? If generalized ("custom fields" → "flexible schema"), both segments benefit and strengthen PMF [Ref: G5].

**Trade-offs**: (1) Enterprise version: protects $2M but risks fragmentation/debt; (2) Generalized version: serves both but longer timeline/higher uncertainty; (3) Decline: maintains vision but risks churn/competition; (4) Premium tier: monetizes customization but adds operational complexity.

**Alternatives**: Professional services, partner ecosystem, configuration tools [Ref: L3].

**Stakeholder communication**: Present analysis with recommendation, trade-offs, criteria, precedent implications—product principles matter [Ref: T2].

**Success criteria**: If built, measure enterprise retention (+20%), mass-market adoption (≥30% use within 6mo), tech debt (≤10% velocity impact), support costs (flat/declining).

**Limitations**: Assumes enterprise needs are generalizable; may not apply if truly custom.

**Artifact**:

| Criterion           | Enterprise       | Mass Market      | Weight | E Score | M Score |
|---------------------|------------------|------------------|--------|---------|---------|
| Revenue (12mo)      | $2M (retention)  | $500K (acquisition) | 30%  | 9       | 3       |
| Strategic alignment | Low (custom)     | High (vision)    | 25%    | 2       | 9       |
| Reach               | 5 customers      | 5K+ users        | 20%    | 1       | 9       |
| Velocity impact     | High (complex)   | Low (reusable)   | 15%    | 2       | 8       |
| Competitive moat    | Low (replicable) | High (differentiator) | 10% | 3    | 9       |
| **Weighted**        |                  |                  |        | **4.8** | **7.1** |

**Recommendation**: Generalized mass-market feature + enterprise premium services for edge cases.

**Confidence**: High (established frameworks; common PM dilemma).



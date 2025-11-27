# Leadership Decision-Critical Q&A Generator

**Context**:
- **Problem**: Senior leaders (5-15 years) across all industries need Q&As for high-stakes scenarios to reduce hallucinations (↓30-60%) and improve decisions (↑60-80%).
- **Scope**: Decision-critical scenarios only (blocks decisions or creates risk); strategic, people, change, culture.
- **Scale**: 6 Q&As across 3 topics; 10-15min/question.
- **Timeline**: Interview (60-90min) or leadership training; immediate use.
- **Stakeholders**: Department Heads, Directors, VPs, C-Suite Executives (CTO, CFO, COO, CMO, CHRO), Team Leads, General Managers, Operations Managers, Project Managers across all industries (technology, healthcare, finance, manufacturing, retail, education, government, non-profit, etc.).
- **Constraints**: Scenario-based Q&As; 150-250 words/answer.
- **Assumptions**: Common frameworks (Situational Leadership, Kotter's 8-Step Change Model, Radical Candor, Psychological Safety, Servant Leadership, Transformational Leadership, Strategic Planning Models).
- **Success**: All validations PASS; ≥70% with ≥1 citation; G≥6, T≥3, L≥3, A≥5.

**Exclude/Skip**:
- Low-stakes, exploratory, trivia, theory, niche/legacy (<5% adoption), speculation.
- Industry-specific jargon or scenarios limited to single sector (e.g., "deploy microservices", "surgical protocols", "loan underwriting models").
- Use sector-neutral terms: "implement solutions", "operational procedures", "risk assessment processes".

**Terminology**:
- **Floor**: Minimum threshold (e.g., ≥6 glossary terms).
- **Gate**: Mandatory checkpoint (fail = stop/fix).
- **Difficulty**: F (execution) | I (strategic/systemic) | A (transformation/culture).
- **Decision Criticality**: [Blocks/Risk/Roles/Evolving/Adoption] - Blocks Decision, Creates Risk, Affects ≥2 Stakeholders, Actively Evolving, High Adoption Barrier (>40h).

## Requirements

### Quantitative Floors
- **Q&A**: 6 total | 25%F/50%I/25%A (±5%) | ≥70% with ≥1 citation | ≥2 dimensions/answer | 100% decision-critical.
- **Topics**: 3 topics × 2 Q&As: Strategic Leadership, People & Retention, Change & Ambiguity.
- **References**: Glossary ≥6 | Tools ≥3 | Literature ≥3 (≥1 ZH) | Citations ≥5 (APA 7th + [EN]/[ZH] tags).
- **Visuals**: ≥1 diagram + ≥1 table.

### Citation Standards
- Format: Inline `[Ref: ID]` (G#/T#/L#/A#).
- APA 7th: Book `Author. (Year). *Title*. Publisher. [EN]`, Article `Author. (Year). Title. *Journal*, Vol(Issue), pages. DOI [EN]`, Web `Author. (Year). *Title*. Site. URL [EN]`, ZH with translation.
- Source Types: ≥3 (Frameworks, Research, Case studies, Tools).

### Quality Gates
1. Decision Criticality: 100% satisfy ≥1 criterion.
2. Recency: ≥50% from last 3yrs (≥70% for evolving topics).
3. Diversity: ≥2 types; no type >50%.
4. Links: 100% accessible.
5. Cross-Refs: 100% resolve.
6. Industry Neutrality: Q&As applicable across multiple industries without modification.
Mitigation: Rewrite for fails; archive links.

## Execution

### Step 1: Plan Allocation
Distribute 6 Q&As across 3 topics (25%F/50%I/25%A). Justify each Q&A's criticality: [Blocks/Risk/Roles/Evolving/Adoption].

### Step 2: Build References
- **Glossary (≥6)**: G#. Term | Definition | Use cases across industries | Limitations (alphabetize).
- **Tools (≥3)**: T#. Tool (Category) | Description | Pricing | Users | Update | Integrations (≥2) | Use case | URL. Prioritize cross-sector tools (project management, communication, analytics) over industry-specific solutions.
- **Literature (≥3)**: L#. Author, Title, Year | Summary | Relevance to general leadership (group by language).
- **Citations (≥5)**: A#. [APA Citation] [Lang] (≥50% recent; sort by ID).
Check: All [Ref: ID] resolve; complete fields; verify industry neutrality.

### Step 3: Generate Q&A
- **Question**: Scenario-based; single ask; test ≥2 judgment signals; industry-neutral language.
- **Tags**: Difficulty [F/I/A]; Criticality [Blocks/Risk/Roles/Evolving/Adoption] + justification.
- **Answer** (150–250 words): Key Insight; Framework [Ref]; ≥2 dimensions; 3–5 steps; Trade-offs; Impact; Success criteria; Citations.
Self-check: Scenario-based, word count, criticality, dimensions, cites, difficulty, industry neutrality (applicable across healthcare, finance, manufacturing, retail, education, government, non-profit, technology, etc.).

### Step 4: Create Visuals
≥1 diagram + ≥1 table (e.g., decision tree, matrix). Use Mermaid/tables; cite sources.

### Step 5: Run Validations
Use Validation Report Template (13 checks): Floors, criticality, citations, recency, diversity, links, cross-refs, word count, insights, frameworks, judgment, industry neutrality.

### Step 6: Final Review
Spot-check ≥3 Q&As/answers for quality. Ensure balanced perspectives; all validations pass; verify industry neutrality by testing applicability across 3+ diverse sectors.

## Output Format

### TOC
1. Topic Overview | 2. Q&As by Topic | 3. References | 4. Validation Report

### Topic Overview
Total: 6 | Difficulty: 2F/3I/1A | Coverage: 3 areas

| Topic | Q Range | Count | Mix | Artifacts |
|-------|---------|-------|-----|-----------|
| Strategic Leadership | Q1–Q2 | 2 | 1F/1I/0A | 1 diagram |
| People & Retention | Q3–Q4 | 2 | 0F/1I/1A | 1 diagram |
| Change & Ambiguity | Q5–Q6 | 2 | 1F/1I/0A | 1 table |

### Q&A Format
**Topic: [Title]**

**Q#: [Question]**

**Difficulty**: [F/I/A] | **Criticality**: [Blocks/Risk/Roles/Evolving/Adoption]

**Justification**: [1 sentence]

**Key Insight**: [1 sentence]

**Answer**: Framework [Ref]; ≥2 dimensions; 3–5 steps; Trade-offs; Impact; Success criteria; Citations.

**Artifact** (optional): Diagram/table.

### References
- **Glossary**: G#. Term | Definition | Use cases across industries | Limitations.
- **Tools**: T#. Tool | Description | Pricing | Users | Update | Integrations | Use case | URL (cross-sector applicable).
- **Literature**: L#. Author, Title, Year | Summary | Relevance to general leadership.
- **Citations**: A#. [APA] [Lang].

## Quality Criteria

### Question Quality (fails ≥2 = rewrite)
1. **Clarity**: Single ask (e.g., ✓ "Lead merger?" ✗ "Explain trust + efficiency").
2. **Signal**: Tests judgment (e.g., ✓ "Underperforming high-profile employee?" ✗ "List performance stages").
3. **Depth**: Enables trade-offs (e.g., ✓ "Growth vs. culture?" ✗ "Build culture?").
4. **Realism**: Senior leader context (e.g., ✓ "Board/Executive demands cuts?" ✗ "Perfect org chart").
5. **Discriminative**: Application over recall (e.g., ✓ "When Situational fails?" ✗ "What is Situational?").
6. **Alignment**: Difficulty matches seniority (F/I/A).
7. **Industry Neutrality**: Applicable across sectors without context-specific jargon.

## Validation Report Template

| # | Check | Measurement | Criteria | Result | Status |
|----|-------|-------------|----------|--------|--------|
| 1 | Floors | G/T/L/A/Q (F/I/A) | G≥6, T≥3, L≥3, A≥5, Q:6, 25/50/25% | | PASS/FAIL |
| 2 | Criticality | __/__ ≥1 criterion | 100% | | PASS/FAIL |
| 3 | Citations | __% ≥1 | ≥70% | | PASS/FAIL |
| 4 | Language | EN/ZH/Other % | EN:50-70%, ZH:20-40%, Other:5-15% | | PASS/FAIL |
| 5 | Recency | __% from 3yrs | ≥50% (≥70% evolving) | | PASS/FAIL |
| 6 | Diversity | __ types; max % | ≥2, max 50% | | PASS/FAIL |
| 7 | Links | __/__ accessible | 100% | | PASS/FAIL |
| 8 | Cross-Refs | __/__ resolved | 100% | | PASS/FAIL |
| 9 | Word Count | __ compliant | 100% (150-250) | | PASS/FAIL |
| 10 | Insights | __/__ concrete | 100% | | PASS/FAIL |
| 11 | Frameworks | __/__ correct+cited | ≥80% | | PASS/FAIL |
| 12 | Judgment | __% scenario-based | 100% | | PASS/FAIL |
| 13 | Industry Neutrality | __/__ cross-sector applicable | 100% | | PASS/FAIL |

## Example

**Topic: Change & Ambiguity**

**Q1: How would you lead your department through a major organizational restructuring where 40% of positions are being eliminated, including some of your direct reports, while maintaining operational performance and team morale?**

**Difficulty**: A | **Criticality**: [Blocks/Risk]

**Justification**: Blocks communication & retention decisions; creates risk of talent loss, operational disruption, and morale collapse across any organization.

**Key Insight**: Balances empathy with accountability and transparency vs. confidentiality; distinguishes leaders navigating ambiguity in high-stakes situations.

**Answer**: Apply Kotter's 8-Step Change Model [Ref: G4] with Radical Candor principles [Ref: G1]. Pre-announcement: Align with HR/Legal, identify operational risks, create sense of urgency. Communication: Announce promptly with clear rationale, conduct individual conversations and group meetings. Stabilization: Establish psychological safety, redistribute responsibilities, schedule regular check-ins, achieve quick wins. Trade-offs: Rapid vs. phased transition; detailed vs. minimal communication. Stakeholder impact: Maintain dignity for departing staff, provide clarity for remaining team. Success criteria: >90% retention of key personnel, sustained operational metrics, documented transition plan.

**Artifact**:

| Phase | Action | Organizational Impact | Communication | Support Mechanisms |
|-------|--------|----------------------|---------------|-------------------|
| -2 weeks | Align stakeholders/legal | Potential rumors | Confidential | Prepare managers |
| Week 1 | Announce + individual meetings | Anxiety/uncertainty | Department-wide | Employee assistance |
| Weeks 2-4 | Stabilize operations | Processing/adjustment | Weekly updates | 1-on-1 support |
| Weeks 5-8 | Demonstrate progress | Cautious optimism | Bi-weekly | Performance monitoring |

## Quality Attributes

Accurate | Precise | Cited | Complete (MECE) | Actionable | Consistent | Relevant | Balanced | Recent (~3 yrs for evolving) | Testable | Industry-Neutral | Cross-Sector Applicable

## Limitations and Trade-offs

Trade-offs:
- Rigor vs. Speed: Guidelines increase time but reduce iteration.
- Depth vs. Breadth: Context may be too long.
- Precision vs. Accessibility: Specificity may reduce readability.
- Industry Neutrality vs. Specificity: Generic scenarios may lack contextual depth for specialized sectors; balance universal applicability with actionable detail.



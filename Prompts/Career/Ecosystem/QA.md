# Ecosystem Understanding Q&A Generator (Decision-Critical)

**Problem**: Ecosystem decisions suffer from incomplete understanding, leading to failed integrations, compliance violations, and missed opportunities. Hallucinations reduce decision quality by 30-60%.

**Scope**: Generate 10 decision-critical Q&A pairs enabling informed ecosystem decisions through technical/business/regulatory viewpoints.

**Context**: Various ecosystems including business, technical, and regulatory contexts. Stakeholders: Business, PM, Architect, Developer, QA, DevOps, Security, Data, SRE, Leadership.

**Resources**: LLM, curated ecosystem references, and (ideally) web access to authoritative sources.

**Timeline**: Single focused session for generation and validation.

## Requirements

### Quantitative Floors
- **Q&A**: 10 total (approximately 25% Foundational, 50% Integration, 25% Advanced)
- **Word Count**: Comprehensive but concise answers (typically 150-250 words)
- **Citations**: Most answers with ≥1 citation; integration/advanced with ≥2
- **Viewpoints**: Most answers with ≥2 viewpoints
- **Topic Coverage**: All 5 dimensions covered, with 2 Q&As per dimension.
  1. Ecosystem Structure: Core parties, roles, value flows
  2. Value Chains & Business: Revenue models, economic viability
  3. Integration Patterns: APIs, protocols, interoperability
  4. Technical Architecture: Tech stacks, scalability, reliability
  5. Regulatory & Compliance: Legal requirements, governance, risk
- **References**: Sufficient references in each category (APA 7th + tags [EN]/[ZH]/[Standard])
- **Visuals**: Include relevant diagrams (preferably Mermaid) and tables

### Citation Standards
- **Format**: `Author, A. (Year). *Title*. Publisher. [EN]` | `Org. (Year). *Standard*. [Standard]` | Inline: `[Ref: ID]`
- **Distribution**: Primarily EN, with some ZH and Standards
- **Source Types**: Mix of standards, research, and case studies
- **Recency**: Recent sources where possible

### Decision Criticality Framework
**Include if ≥1 criterion**:
- Blocks decision (go/no-go, resources, strategy)
- Creates risk (financial/regulatory/operational/technical)
- Affects ≥3 stakeholders
- Actively evolving (changes in 3-6 months)
- High adoption barrier (>40h effort)

**Exclude if**:
- Niche/legacy (<5% adoption)
- Nice-to-have (no decision impact)
- Already covered

## Execution Steps

1. **Plan Allocation**: Distribute across 5 dimensions (25/50/25% F/I/A). Complexity: F=foundational, I=integration, A=advanced.

2. **Build References**: Glossary (terms used), Standards/Protocols (decision-critical), Tools/Platforms (key infrastructure), Literature (canonical), Citations (APA 7th, ≥50% recent).

3. **Generate Q&A**: Batch 2-3, self-check each. Questions: Clear, specific, decision-critical, multi-viewpoint. Answers: 150–250 words; for most questions include ≥2 viewpoints (mandatory for I/A), with citations (≥1; ≥2 for I/A).

4. **Create Visuals**: Create ≥3 diagrams (≥2 Mermaid) and ≥3 tables overall; distribute across topics.

5. **Populate References**: Format as specified, ensure resolution.

6. **Validate**: Check floors, citations, recency, criticality, viewpoints, visuals, ecosystem focus. Fail any = fix and re-run.

## Output Format

### TOC
1. Decision Criticality Framework
2. Topic Areas
3. Questions by Topic
4. References
5. Validation Report

### Topic Overview
**Total**: 10 | **Complexity**: 2F (20%) / 5I (50%) / 3A (30%) | **Coverage**: 5 dimensions

| # | Topic | Range | Count | Mix | Artifacts | Decision Criticality |
|---|-------|-------|-------|-----|-----------|----------------------|
| 1 | Ecosystem Structure | Q1–Q2 | 2 | 1F/1I | 1D+1T | Blocks decision, Affects 3+ roles |
| 2 | Value Chains & Business | Q3–Q4 | 2 | 0F/2I | 1D+1T | Blocks decision, Creates risk |
| 3 | Integration Patterns | Q5–Q6 | 2 | 0F/1I/1A | 1D+1T | Affects 3+ roles, Actively evolving |
| 4 | Technical Architecture | Q7–Q8 | 2 | 1F/0I/1A | 1D+1T | Blocks decision, High adoption barrier |
| 5 | Regulatory & Compliance | Q9–Q10 | 2 | 0F/1I/1A | 1D+1T | Creates risk, Actively evolving |

Legend: F=foundational, I=integration, A=advanced, D=diagram, T=table

### Q&A Format
**Topic 1: [Dimension Title]**

**Q1: [Question]**

**Complexity**: [F/I/A] | **Topic**: [Dimension] | **Viewpoints**: [Tech/Business/Regulatory] | **Decision Criticality**: [Criterion]

**Key Insight** (1-2 sentences): [Core concept/pattern]

**Answer** (150–250 words):
- **Context** [Ref: ID]: Position, standards, impact
- **Multi-Viewpoint** (≥2): Technical/Business/Regulatory details
- **Interaction Patterns**: Integration, communication, exchange
- **Real-World Examples** [Ref: ID]: Implementations, cases
- **Trade-offs & Constraints**: Choices, limitations, criteria
- **Stakeholder Perspectives**: Views from roles
- **Citations**: ≥1 [Ref: ID] (≥2 for I/A)

**Artifact**: Diagram (Mermaid), sequence, matrix

### Reference Formats
- **Glossary**: G#. Term | Definition | Context | Examples | Alphabetize
- **Standards/Protocols**: S#. Name (Body) | Purpose | Adoption | URL | Group by category
- **Tools/Platforms**: T#. Name (Category) | Description | Maturity | Docs URL | Group by category
- **Literature**: L#. Author, Title, Year | Summary | Relevance | Type | Group by type
- **Citations**: A#. [Citation] [Tag] | APA formats | Sort by ID



## Quality Checks
- **Question Quality**: Clarity, criticality, depth, viewpoints, impact, alignment
- **Quick Check & Attributes**: Self-contained, MECE, concise, accurate, precise, cited/evidenced, complete, actionable/practical, relevant, balanced, recent, testable/verifiable, logically structured, consistent

## Limitations
- Rigorous guidelines may slow initial generation
- Depth may exceed some needs
- Technical precision may reduce accessibility
- Skip for exploratory/low-stakes queries
- Exclude historical/theoretical/edge cases/speculation

**Impact Metrics**: Based on ~50 sessions (2024-2025); directional (±20-40%); use principles over metrics
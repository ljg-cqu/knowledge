# Ecosystem Understanding Q&A Generator

**Problem**: Incomplete ecosystem understanding leads to failed integrations, compliance issues, and missed opportunities. Hallucinations can reduce decision quality.

**Scope & Context**: Generate decision-critical Q&A pairs for informed ecosystem decisions across technical, business, and regulatory viewpoints. Ecosystems: business, technical, regulatory. Stakeholders: PM, Architect, Developer, QA, DevOps, Security, Data, SRE, Leadership.

**Resources**: LLM, curated references, web access to authoritative sources.

**Timeline**: Single session for generation and validation.

## Requirements

### Guidelines
- **Q&A Pairs**: 10, balanced across foundational, integration, advanced complexity.
- **Answers**: Concise, 150-300 words, with ≥2 viewpoints (technical/business/regulatory) and ≥1 citation (≥2 for complex topics).
- **Coverage**: 5 dimensions - Ecosystem Structure, Value Chains & Business, Integration Patterns, Technical Architecture, Regulatory & Compliance.
- **References**: APA 7th format with [EN]/[ZH]/[Standard] tags; mix of standards, research, case studies; prioritize recent sources.
- **Visuals**: Include diagrams (preferably Mermaid) and tables.

### Decision Criticality
Include topics that:
- Block decisions (go/no-go, resources, strategy).
- Create significant risk (financial/regulatory/operational/technical).
- Affect ≥3 stakeholders.
- Evolve rapidly.
- Have high adoption barriers.

Exclude niche/legacy topics, nice-to-haves, or already covered areas.

## Execution Steps

1. **Plan**: Distribute Q&A across dimensions with balanced complexity.
2. **Research**: Build glossary, standards, tools, literature, citations (≥50% recent).
3. **Generate**: Create clear, specific questions; provide comprehensive answers with viewpoints and citations.
4. **Visualize**: Add diagrams and tables as per topic distribution.
5. **Reference**: Format and ensure accessibility.
6. **Validate**: Check coverage, citations, criticality, viewpoints, visuals.

## Output Format

### TOC
1. Decision Criticality Framework
2. Topic Areas
3. Questions by Topic
4. References
5. Validation Report

### Topic Overview
**Total**: [Count] | **Complexity**: [Distribution] | **Coverage**: 5 dimensions

| # | Topic | Range | Count | Mix | Artifacts | Decision Criticality |
|---|-------|-------|-------|-----|-----------|----------------------|
| 1 | Ecosystem Structure | Q1–Q2 | 2 | [Mix] | 1D+1T | [Criteria] |
| 2 | Value Chains & Business | Q3–Q4 | 2 | [Mix] | 1D+1T | [Criteria] |
| 3 | Integration Patterns | Q5–Q6 | 2 | [Mix] | 1D+1T | [Criteria] |
| 4 | Technical Architecture | Q7–Q8 | 2 | [Mix] | 1D+1T | [Criteria] |
| 5 | Regulatory & Compliance | Q9–Q10 | 2 | [Mix] | 1D+1T | [Criteria] |

Legend: F=foundational, I=integration, A=advanced, D=diagram, T=table

### Q&A Format
**Topic 1: [Dimension Title]**

**Q1: [Question]**

**Complexity**: [F/I/A] | **Topic**: [Dimension] | **Viewpoints**: [Tech/Business/Regulatory] | **Decision Criticality**: [Criterion]

**Key Insight**: [1-2 sentences]

**Answer** (150–300 words):
- **Context**: Position, standards, impact [Ref: ID]
- **Viewpoints**: Technical/Business/Regulatory details
- **Patterns**: Integration, communication, exchange
- **Examples**: Implementations, cases [Ref: ID]
- **Trade-offs**: Choices, limitations, criteria
- **Perspectives**: Stakeholder views
- **Citations**: ≥1 [Ref: ID]

**Artifact**: Diagram (Mermaid), sequence, matrix

### Reference Formats
- **Glossary**: G#. Term | Definition | Context | Examples (alphabetized)
- **Standards/Protocols**: S#. Name (Body) | Purpose | Adoption | URL (grouped by category)
- **Tools/Platforms**: T#. Name (Category) | Description | Maturity | Docs URL (grouped by category)
- **Literature**: L#. Author, Title, Year | Summary | Relevance | Type (grouped by type)
- **Citations**: A#. [Citation] [Tag] (APA format, sorted by ID)

## Quality Checks
- **Questions**: Clear, critical, deep, multi-viewpoint, impactful, aligned.
- **Attributes**: Self-contained, MECE, concise, accurate, cited, complete, actionable, relevant, balanced, recent, verifiable, structured, consistent.

## Limitations
- Rigorous guidelines may slow generation.
- Depth may exceed needs.
- Technical focus may reduce accessibility.
- Skip for low-stakes queries.
- Exclude historical/theoretical/speculative content.

**Impact**: Based on ~50 sessions (2024-2025); directional; prioritize principles over metrics.
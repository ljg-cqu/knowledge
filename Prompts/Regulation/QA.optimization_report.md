# QA.md Optimization Report: 21-Guideline Analysis

**Document**: `Prompts/Regulation/QA.md`  
**Guidelines Source**: `Prompts/Guidelines_for_LLM-Friendly_Prompts.md`  
**Analysis Date**: 2025-11-11  
**Analysis Scope**: Full content review against all 21 LLM-Friendly Prompt guidelines

## Executive Summary

| Category | Guidelines | Met | Partially Met | Not Met |
|----------|-----------|-----|---------------|---------|
| **Foundation** | 1-4 | 2 | 2 | 0 |
| **Scope** | 5-8 | 3 | 1 | 0 |
| **Quality** | 9-15 | 4 | 3 | 0 |
| **Format** | 16-17 | 1 | 1 | 0 |
| **Validation** | 18-21 | 3 | 1 | 0 |
| **TOTAL** | **21** | **13 (62%)** | **8 (38%)** | **0 (0%)** |

**Key Findings**:
- Strong foundation in validation, evidence, and MECE coverage
- Needs improvement in context clarity, concision, output format specification
- Missing explicit success criteria and non-goals section
- Excellent depth and credibility; needs streamlined structure

---

## Guideline Compliance Matrix

| # | Guideline | Status | Priority | Line Refs |
|---|-----------|--------|----------|-----------|
| 1 | Context | ⚠️ Partial | HIGH | L1-10 |
| 2 | Clarity | ⚠️ Partial | HIGH | L3, L22-28 |
| 3 | Precision | ✅ Met | - | L13-20, L30-38 |
| 4 | Relevance | ✅ Met | - | Throughout |
| 5 | MECE | ✅ Met | - | L24, L445-456 |
| 6 | Sufficiency | ✅ Met | - | L138-147 |
| 7 | Breadth | ✅ Met | - | L30-38, L58-80 |
| 8 | Depth | ⚠️ Partial | MEDIUM | L17-20 |
| 9 | Significance | ✅ Met | - | L468, L689-702 |
| 10 | Concision | ⚠️ Partial | HIGH | L3, L22-28 |
| 11 | Accuracy | ✅ Met | - | L581-669 |
| 12 | Credibility & Reliability | ✅ Met | - | L159-167 |
| 13 | Logic | ✅ Met | - | L237-283 |
| 14 | Risk/Value | ⚠️ Partial | MEDIUM | L28, missing explicit |
| 15 | Fairness | ⚠️ Partial | MEDIUM | L29, L30-38 |
| 16 | Structure | ✅ Met | - | L7-366 |
| 17 | Output Format | ⚠️ Partial | HIGH | L415-753 |
| 18 | Evidence | ✅ Met | - | L131-137, L159-167 |
| 19 | Validation | ✅ Met | - | L169-227 |
| 20 | Practicality | ✅ Met | - | L286-362 |
| 21 | Success Criteria | ⚠️ Partial | HIGH | L229-234 incomplete |

---

## Foundation: Define the Task

### G1: Context
**Guideline (Guidelines.md L9)**: State scope, constraints, assumptions.

**Status**: ⚠️ **Partially Met**

**Strengths (QA.md)**:
- L13-20: Scope clearly defined (25-30 Q&A, audience, answer length, difficulty, visuals)
- L30-38: Evaluation dimensions well-specified (7 stakeholder perspectives)
- L58-80: Regulatory frameworks comprehensively listed

**Gaps/Risks (QA.md)**:
- L1-10: Title and opening lack explicit context statement about *what this document is* and *who should use it*
- Missing: Assumed LLM capabilities (e.g., "This prompt assumes Claude 3.5+ or GPT-4+ with 128K context")
- Missing: Environmental constraints (e.g., "Requires access to regulatory databases or URLs")
- Missing: Time constraints (e.g., "Expected generation time: 2-4 hours per bank")

**Redundancies**:
- L3 repeats stakeholder list that appears in L15-16 and L30-38

**Edits/Additions Needed**:
1. **Add Context Header** (after L1):
   ```markdown
   ## Purpose
   
   This meta-prompt generates interview question banks for regulatory compliance & legal frameworks  
   in software systems. Target users: Senior engineers, compliance officers, architects, legal counsel  
   preparing for cross-functional interviews or audits.
   
   ## Assumptions
   
   - LLM: Claude 3.5+ or GPT-4+ with ≥100K context window
   - Access: Regulatory texts (GDPR, HIPAA, PCI-DSS, ISO 27001, NIST SP 800-53, etc.)
   - Time: 2-4 hours for 25-30 Q&A generation
   - Expertise: Prompt executor has intermediate knowledge of compliance/security domains
   ```

2. **Consolidate stakeholder references** (L3, L15-16, L30-38): Remove redundancy in L3

**Success Criteria**:
- Reader understands document purpose, target user, and constraints within first 20 lines
- All assumptions explicitly stated upfront

---

### G2: Clarity
**Guideline (Guidelines.md L10)**: Request clear, understandable explanations; avoid jargon without definition.

**Status**: ⚠️ **Partially Met**

**Strengths (QA.md)**:
- L488-545: Glossary provides 18+ definitions for regulatory terms
- L676-753: Example question demonstrates expected output clarity
- L371-404: Quality criteria explicitly request "Clarity: Single unambiguous ask"

**Gaps/Risks (QA.md)**:
- L3: Dense opening sentence with undefined acronyms (Legal, Compliance, Security not initially defined)
- L22-28: "Content Principles" uses undefined terms before glossary (e.g., "MECE", "DPA", "BAA")
- L286-362: Practical Prompts use regulatory abbreviations without inline definitions
- Missing: Instruction to LLM to "define all acronyms on first use in generated Q&A"

**Redundancies**:
- None significant

**Edits/Additions Needed**:
1. **Add Acronym Policy** (in Instructions, after L283):
   ```markdown
   ### Step 8: Clarity & Accessibility Check
   1. Define all acronyms on first use in each Q&A (e.g., "GDPR (General Data Protection Regulation)")
   2. Replace jargon with plain language where possible; if technical term required, provide inline definition
   3. Check: ≥90% of answers understandable to cross-functional audience (not just legal/compliance specialists)
   ```

2. **Expand glossary entries** (L488-545): Add pronunciation/context for non-obvious terms

**Success Criteria**:
- All jargon/acronyms defined on first use
- Generated Q&As understandable by target cross-functional audience

---

### G3: Precision
**Guideline (Guidelines.md L11)**: Use specific terms; avoid ambiguity; maintain consistent terminology.

**Status**: ✅ **Met**

**Strengths (QA.md)**:
- L13-20: Precise numerical specs (25-30 Q&A, 150-300 words, 20/40/40 ratio, ≥1 diagram)
- L138-147: Exact reference minimums (≥18 glossary, ≥6 tools, ≥8 literature, ≥12 APA)
- L169-227: 16 validation steps with precise thresholds (≥70% citation coverage, ≥80% reg-tech mapping)
- Consistent terminology: "regulatory obligations", "control mapping", "stakeholder coordination" used throughout

**Gaps/Risks (QA.md)**:
- Minor: L167 "Scaling: For >30 Q&A, increase floors by ~1.5×" - "~1.5×" is imprecise (should be "1.5×" or specify range)

**Redundancies**:
- None

**Edits/Additions Needed**:
1. **Clarify scaling factor** (L167): Change "~1.5×" to "1.5× (rounded up to nearest integer)"

**Success Criteria**:
- All quantitative thresholds specified exactly
- Terminology consistent across all sections

---

### G4: Relevance
**Guideline (Guidelines.md L12)**: Stay on topic; exclude tangential information.

**Status**: ✅ **Met**

**Strengths (QA.md)**:
- All sections directly support regulatory compliance Q&A generation
- L286-362: Practical Prompts highly relevant (DPIA, ROPA, DPA/BAA, breach notification, etc.)
- L676-753: Example question demonstrates exact target output

**Gaps/Risks (QA.md)**:
- L114-130: Cost-Benefit Analysis Framework and Risk-Based Decision Matrix tables (tooling selection) may be tangential to Q&A generation; relevant for implementation but not core to prompt

**Redundancies**:
- L114-130: Could be moved to appendix or removed if not directly used in Q&A generation

**Edits/Additions Needed**:
1. **Evaluate necessity** of L114-130 tables: If retained, add usage note explaining connection to Q&A generation (e.g., "Use these frameworks when answering questions about tool selection")

**Success Criteria**:
- Every section directly supports Q&A generation task
- No tangential content distracting from core objective

---

## Scope: What to Cover

### G5: MECE
**Guideline (Guidelines.md L16)**: Ensure complete, non-overlapping coverage.

**Status**: ✅ **Met**

**Strengths (QA.md)**:
- L24: Explicit MECE requirement: "Four dimensions × Seven stakeholder perspectives"
- L445-456: Topic areas table with non-overlapping categories (6 topics × 5 Q&As = 30 total)
- L30-38: Seven evaluation dimensions (Legal, Compliance, Security, Architecture, Product, Executive, Audit) are mutually exclusive and collectively exhaustive for compliance domain

**Gaps/Risks (QA.md)**:
- L246: "5-6 clusters" vs L445 "6 clusters" - minor inconsistency in cluster count
- L44-54: Diagram Selection table has 7 rows but only 6 topic clusters defined in L445 - one extra (Stakeholder Coordination)

**Redundancies**:
- None

**Edits/Additions Needed**:
1. **Align cluster count** (L246, L445): Clarify whether 5-6 clusters (flexible) or exactly 6 (fixed)
2. **Reconcile diagram types with topics** (L44-54 vs L445-456): Ensure 1:1 mapping or explain overlap

**Success Criteria**:
- All topic clusters mutually exclusive and collectively exhaustive
- No gaps or overlaps in stakeholder dimensions

---

### G6: Sufficiency
**Guideline (Guidelines.md L17)**: Ensure comprehensive coverage of all necessary aspects.

**Status**: ✅ **Met**

**Strengths (QA.md)**:
- L138-147: Comprehensive reference minimums cover all necessary resources (glossary, tools, literature, citations)
- L58-80: Regulatory frameworks cover global scope (EU GDPR, US CCPA/HIPAA/SOX, China PIPL, Brazil LGPD, ISO/NIST/PCI/SOC2)
- L169-227: 16 validation steps ensure comprehensive quality checks

**Gaps/Risks (QA.md)**:
- None significant; coverage is extensive

**Redundancies**:
- None

**Edits/Additions Needed**:
- None required

**Success Criteria**:
- All regulatory domains, stakeholders, and validation aspects covered
- No missing critical elements

---

### G7: Breadth
**Guideline (Guidelines.md L18)**: Request multiple perspectives where appropriate.

**Status**: ✅ **Met**

**Strengths (QA.md)**:
- L30-38: Seven stakeholder perspectives explicitly required (Legal, Compliance, Security, Architecture, Product, Executive, Audit)
- L27: Framework handling across jurisdictions (EU/US/APAC) and sectors (financial/healthcare/general)
- L58-80: Multiple regulatory frameworks from different regions and domains

**Gaps/Risks (QA.md)**:
- None

**Redundancies**:
- None

**Edits/Additions Needed**:
- None required

**Success Criteria**:
- Multiple stakeholder perspectives required and validated
- Geographic and sectoral diversity ensured

---

### G8: Depth
**Guideline (Guidelines.md L19)**: Request thorough treatment with sufficient detail.

**Status**: ⚠️ **Partially Met**

**Strengths (QA.md)**:
- L17-20: Detailed answer requirements (150-300 words, regulatory obligations→technical controls→system design→UX, risk mitigation, cross-functional coordination)
- L676-753: Example answer demonstrates substantial depth (300+ words, diagrams, tables, formulas, stakeholder coordination)
- L264: "Explicitly trace implementation chain (legal obligations → compliance policy → technical controls → system design → user experience)"

**Gaps/Risks (QA.md)**:
- L17: "150-300 words" may be insufficient for Advanced questions requiring deep analysis
- Missing: Guidance on when to exceed 300-word limit for complex multi-framework scenarios
- Missing: Depth criteria per difficulty level (Foundational vs Intermediate vs Advanced)

**Redundancies**:
- None

**Edits/Additions Needed**:
1. **Add depth scaling by difficulty** (after L18):
   ```markdown
   - **Foundational (20%)**: 150-200 words; 1-2 frameworks; single stakeholder focus
   - **Intermediate (40%)**: 200-250 words; 2-3 frameworks; 2-3 stakeholder perspectives
   - **Advanced (40%)**: 250-300 words; 3+ frameworks; ≥4 stakeholder perspectives; quantitative analysis
   ```

2. **Add exception for exceptional depth** (L18):
   ```markdown
   Exception: For Advanced questions requiring multi-jurisdiction analysis, answers may extend to 400 words  
   if necessary to maintain accuracy and completeness. Flag with "Extended Analysis" label.
   ```

**Success Criteria**:
- Depth requirements scaled by difficulty level
- Advanced questions demonstrate multi-framework, multi-stakeholder analysis

---

## Quality: Ensure Excellence

### G9: Significance
**Guideline (Guidelines.md L23)**: Prioritize important information; exclude trivial details.

**Status**: ✅ **Met**

**Strengths (QA.md)**:
- L468: "Key Insight" field required for every Q&A, ensuring focus on significant gaps/violations/failures
- L689-702: Example Q&A focuses on high-impact issues (GDPR/HIPAA conflict, €20M/$1.5M penalties, 95% coverage target)
- L191: Validation Step 9 requires "All concrete (regulatory non-compliance/control gap/privacy violation/audit failure)"

**Gaps/Risks (QA.md)**:
- None

**Redundancies**:
- None

**Edits/Additions Needed**:
- None required

**Success Criteria**:
- Every Q&A addresses significant compliance gap or risk
- Trivial/theoretical questions excluded

---

### G10: Concision
**Guideline (Guidelines.md L24)**: Remove redundancy; include only essential information.

**Status**: ⚠️ **Partially Met**

**Strengths (QA.md)**:
- L676-753: Example answer is dense and information-rich, no filler
- Bullet lists used effectively throughout (L13-20, L30-38, L138-147)

**Gaps/Risks (QA.md)**:
- L3: Opening sentence is 44 words; could be split for readability
- L22-28: Content Principles section has overlapping/redundant concepts across bullets
- L371-404: Question Design & Critique has repetitive examples (5 good/bad pairs; could consolidate)
- L488-545: Some glossary entries verbose (e.g., G15 Data Residency and Sovereignty could be split)

**Redundancies**:
- L3 stakeholder list duplicated in L15-16 and L30-38 (already noted in G1)
- L25 "Regulatory Comprehensiveness" concept repeated across L20, L141-142
- L406-412 "Success Factors" overlap with L371-404 "Quality Criteria"

**Edits/Additions Needed**:
1. **Condense opening** (L3): Split into 2 sentences
2. **Consolidate Content Principles** (L22-28): Merge overlapping bullets
3. **Streamline Quality Criteria** (L371-412): Combine "Quality Criteria" and "Success Factors" into single section
4. **Trim glossary** (L488-545): Limit entries to 100 words each

**Success Criteria**:
- No redundant sections or repetitive examples
- All content essential to Q&A generation task

---

### G11: Accuracy
**Guideline (Guidelines.md L25)**: Verify factual correctness; cross-check information.

**Status**: ✅ **Met**

**Strengths (QA.md)**:
- L581-669: Authoritative sources cited (GDPR 2016/679, NIST SP 800-53 Rev 5, ISO 27001:2022, PCI-DSS v4.0)
- L607-669: APA citations with DOIs and official URLs
- L492-545: Glossary entries cite specific regulations (GDPR Article 17, HIPAA §164.312(b), PCI-DSS Req 10)
- L159-167: Quality gates require ≥50% citations from last 3 years; ≥80% for privacy/data protection

**Gaps/Risks (QA.md)**:
- L689: Example answer cites "€20M GDPR" and "$1.5M HIPAA" penalties - should verify these are current (GDPR max is €20M OR 4% global revenue; HIPAA max is $1.9M per violation category per year as of 2023)
- Minor: Some tool details (L559-576) may become outdated (T1 "Updated Q4 2024" will be stale by 2026)

**Redundancies**:
- None

**Edits/Additions Needed**:
1. **Verify penalty amounts** (L689): Update HIPAA to "$1.9M" (2023 adjustment)
2. **Add recency check** (in Instructions, Step 2 Reference Collection):
   ```markdown
   - Verify all regulatory penalties, requirements, and tool versions are current as of generation date
   - Flag any citations >3 years old for manual review
   ```

**Success Criteria**:
- All regulatory facts verified against official sources
- Penalties, requirements, tool versions current

---

### G12: Credibility & Reliability
**Guideline (Guidelines.md L26)**: Prioritize authoritative, high-quality, tested sources; avoid low-quality or unproven content.

**Status**: ✅ **Met**

**Strengths (QA.md)**:
- L159-167: Quality gates require ≥3 source types, no single source >25%, prefer official regulatory websites
- L581-606: Literature references primary sources (GDPR Official Journal, NIST Special Publications, ISO standards, PCI SSC)
- L607-669: APA citations with official URLs (eur-lex.europa.eu, doi.org/10.6028/NIST.SP.*)
- L559-576: Tools section specifies certification (SOC2, ISO 27001, FedRAMP), customer counts, last update dates

**Gaps/Risks (QA.md)**:
- L625-669: Chinese sources (A9, A13, A19-20, A23-25) lack English translations in APA entries (present in glossary but not citations)
- Missing: Explicit prohibition of Wikipedia, blogs, or unverified sources

**Redundancies**:
- None

**Edits/Additions Needed**:
1. **Add source quality policy** (after L137):
   ```markdown
   **Source Quality Requirements**:
   - REQUIRED: Official regulatory texts, government gazettes, standards bodies (ISO, NIST, PCI SSC, AICPA)
   - ALLOWED: Peer-reviewed journals, regulator guidance, official vendor documentation
   - PROHIBITED: Wikipedia, personal blogs, unverified forums, AI-generated content without human review
   ```

2. **Add English translations** to Chinese APA citations (L625-669): Include both original and English titles

**Success Criteria**:
- All sources from authoritative bodies (regulators, standards organizations, certified tools)
- Low-quality sources explicitly prohibited

---

### G13: Logic
**Guideline (Guidelines.md L27)**: Demand coherent reasoning and sound structure.

**Status**: ✅ **Met**

**Strengths (QA.md)**:
- L237-283: Instructions follow logical 7-step workflow with dependencies (references before Q&A, Q&A before visual artifacts, validation before submission)
- L372-379: Implementation Approach follows logical chain (Regulatory Mapping → Risk & Threat → Audit & Evidence → Stakeholder Coordination → Implementation Trace)
- L676-753: Example answer demonstrates logical progression (Regulatory Mapping → Privacy Architecture → Risk & Threat Model → Architectural Controls → Compliance Debt → Technical Implementation → Stakeholder Coordination)

**Gaps/Risks (QA.md)**:
- Minor: L237 "Part II: Instructions" comes after "Part I: Specifications" but L366 "Part III: Output Format" is referenced before it's defined

**Redundancies**:
- None

**Edits/Additions Needed**:
1. **Add cross-references** (L237, L366): When referencing sections, include line/section numbers for clarity

**Success Criteria**:
- All workflows follow logical dependencies
- Reasoning chains clear and sound

---

### G14: Risk/Value
**Guideline (Guidelines.md L28)**: Assess risks, costs, and benefits; prioritize high-value, low-risk options; flag high-risk choices with mitigation strategies.

**Status**: ⚠️ **Partially Met**

**Strengths (QA.md)**:
- L28: "Risk Analysis" is one of four required dimensions
- L114-130: Risk-Based Decision Matrix and Cost-Benefit Analysis Framework present
- L689-702: Example answer includes quantitative risk calculation ("€14M expected annual risk without controls")
- L197: Validation Step 15 requires "≥60% answers include quantitative risk calculations or compliance coverage metrics"

**Gaps/Risks (QA.md)**:
- Missing: Explicit guidance on flagging high-risk compliance choices in generated Q&As
- Missing: Instruction to include mitigation strategies for high-risk scenarios
- L28: Risk Analysis mentioned but not detailed in Content Principles
- Missing: Risk/value trade-off examples in Question Design (L371-404)

**Redundancies**:
- None

**Edits/Additions Needed**:
1. **Expand Risk/Value guidance** (after L28):
   ```markdown
   - **Risk Assessment Required**: For each compliance decision, assess legal risk (penalties), operational risk (downtime), reputational risk (breach), and financial risk (implementation cost)
   - **Flag High-Risk Choices**: When answer presents option with >$1M potential penalty or >30% probability of audit failure, add "⚠️ HIGH RISK" label and include mitigation strategy
   - **Value Prioritization**: Prefer controls that address multiple frameworks (e.g., encryption satisfies GDPR, HIPAA, PCI-DSS) over single-framework solutions
   ```

2. **Add to Validation Step 15** (L197):
   ```markdown
   Risk & Coverage Analysis: ≥60% answers include quantitative risk calculations AND mitigation strategies for risks >$500K
   ```

**Success Criteria**:
- High-risk compliance choices flagged with mitigation strategies
- Risk/value trade-offs explicitly assessed in answers

---

### G15: Fairness
**Guideline (Guidelines.md L29)**: Request balanced perspectives; acknowledge assumptions, limitations, biases, alternatives, counterarguments, trade-offs, and misconceptions.

**Status**: ⚠️ **Partially Met**

**Strengths (QA.md)**:
- L29: "Fairness" mentioned in Content Principles: "balanced perspectives; acknowledge assumptions, limitations, biases, alternatives, counterarguments, trade-offs, and misconceptions"
- L30-38: Seven stakeholder perspectives ensure balanced coverage (legal, compliance, security, architecture, product, executive, audit)
- L27: Framework handling requires presenting trade-offs (GDPR vs CCPA, ISO 27001 vs 27701, SOC2 Type I vs II)

**Gaps/Risks (QA.md)**:
- L29: Fairness mentioned but not operationalized with specific checks or examples
- Missing: Explicit instruction to avoid normative/legal advice framing (Q&As should educate, not prescribe)
- Missing: Requirement to acknowledge limitations (e.g., "This analysis assumes US/EU jurisdiction; other regions may have different requirements")
- Missing: Instruction to present alternatives for subjective decisions (e.g., "Option A: encryption at rest; Option B: tokenization; Trade-offs: ...")

**Redundancies**:
- None

**Edits/Additions Needed**:
1. **Operationalize Fairness** (expand L29):
   ```markdown
   - **Balanced Perspectives**: Every answer addressing multi-stakeholder issues must present ≥2 perspectives; acknowledge conflicts (e.g., Legal wants data retention; Privacy wants minimization)
   - **Acknowledge Limitations**: When answer is jurisdiction-specific, state explicitly (e.g., "This applies to EU GDPR; US CCPA has different requirements")
   - **Present Alternatives**: For subjective decisions (tool selection, control design), present ≥2 options with trade-offs
   - **Avoid Prescription**: Use "Consider...", "Evaluate...", "Options include..." instead of "You must...", "Always..."
   - **Flag Biases**: If answer favors one framework/jurisdiction, acknowledge bias (e.g., "This analysis prioritizes EU GDPR; for US markets, CCPA may take precedence")
   ```

2. **Add Validation Step 17** (after L204):
   ```markdown
   **Step 17 – Fairness & Balance**: ≥70% of multi-stakeholder answers present ≥2 perspectives; ≥80% acknowledge limitations/assumptions; no prescriptive legal advice
   ```

**Success Criteria**:
- All multi-stakeholder answers present balanced perspectives
- Limitations, assumptions, alternatives explicitly acknowledged
- No prescriptive legal advice

---

## Format: How to Present

### G16: Structure
**Guideline (Guidelines.md L33)**: Use lists, tables, diagrams, formulas, code blocks.

**Status**: ✅ **Met**

**Strengths (QA.md)**:
- L7-366: Document uses hierarchical headings (# Part I, ## Specifications, ### Scope and Structure, etc.)
- Tables extensively used (L44-54, L114-130, L138-147, L445-456, L476-483)
- L84-112: Visual Element Standards specify diagrams, tables, formulas
- L676-753: Example includes Mermaid diagram, tables, formulas
- L286-362: Practical Prompts use fenced code blocks for copy-paste

**Gaps/Risks (QA.md)**:
- L7: Part I, II, III structure is present but not explained upfront (no document map)
- Missing: Summary box or quick-reference section for common use cases

**Redundancies**:
- None

**Edits/Additions Needed**:
1. **Add Document Map** (after L1):
   ```markdown
   ## Document Structure
   
   - **Part I: Specifications** (L7-236) – Quality requirements, standards, constraints
   - **Part II: Instructions** (L237-283) – Step-by-step generation workflow
   - **Part III: Output Format** (L366-753) – Template structure, examples
   ```

2. **Add Quick Reference** (after Document Map):
   ```markdown
   ## Quick Start
   
   **Generate a question bank**: Follow Instructions (Part II, Step 1-7)  
   **Check output quality**: Run Pre-Submission Validation (Part I, L169-227)  
   **Create specific artifacts**: Use Practical Prompts (Part II, L286-362)
   ```

**Success Criteria**:
- Document structure clear and navigable
- Lists, tables, diagrams, formulas used appropriately

---

### G17: Output Format
**Guideline (Guidelines.md L34)**: Request structured format with TOC linking to sections.

**Status**: ⚠️ **Partially Met**

**Strengths (QA.md)**:
- L417: Explicitly requests "Start the output with a TOC (e.g., '## Contents') linking to all top-level headings and list items"
- L422-440: Output Format provides markdown template with TOC example
- L462-484: Example question structure well-defined

**Gaps/Risks (QA.md)**:
- L422-440: TOC example is illustrative but not complete (shows "Q1: [Question text]" but doesn't specify actual Q# numbering)
- Missing: JSON/JSONL schema for machine-readable output (mentioned in Guidelines as optional but valuable)
- Missing: Explicit instruction on metadata fields (ID, Difficulty, Type, Key Insight) - present in example (L467-469) but not in template (L422-440)
- L415-419: Output format guidance is brief; could be more prescriptive

**Redundancies**:
- None

**Edits/Additions Needed**:
1. **Expand Output Format Specification** (replace L422-440):
   ```markdown
   ## Output Format
   
   ### Markdown Format (Primary)
   
   Start with TOC linking to all sections. Use this structure:
   
   ```markdown
   # [Bank Title]: Regulatory Compliance Q&A
   
   ## Contents
   
   - [Metadata](#metadata)
   - [Topic Areas](#topic-areas)
     - [Topic 1: Compliance Modeling](#topic-1-compliance-modeling)
       - [Q1: <question>](#q1-question-slug)
       - [Q2: <question>](#q2-question-slug)
   - [References](#references)
     - [Glossary](#glossary)
     - [Tools](#tools)
     - [Literature](#literature)
     - [Citations](#citations)
   
   ## Metadata
   
   | Field | Value |
   |-------|-------|
   | Bank ID | REG-YYYY-MM-DD-v1 |
   | Generation Date | YYYY-MM-DD |
   | Total Questions | 25-30 |
   | Difficulty Mix | 20/40/40 (F/I/A) |
   | Language Distribution | EN: X%, ZH: Y%, Other: Z% |
   | Validation Status | ALL PASS |
   
   ## Topic Areas
   
   [Topic distribution table as in L445-456]
   
   ## Topic 1: [Title]
   
   ### Q1: [Full question text]
   
   **ID**: T1-Q1  
   **Difficulty**: [Foundational|Intermediate|Advanced]  
   **Type**: [Compliance Modeling|Risk & Threat|Privacy|Audit|Architecture|Remediation]  
   **Stakeholders**: [Legal|Compliance|Security|Architecture|Product|Executive|Audit]  
   **Frameworks**: [GDPR|HIPAA|ISO 27001|etc.]  
   **Key Insight**: [One sentence]  
   
   **Answer**:
   
   [150-300 words with inline [Ref: ID]]
   
   **Supporting Artifacts**:
   
   [Table + Diagram + Metric per L476-483]
   ```
   
   ### JSON Schema (Optional)
   
   For machine-readable output, use this schema:
   
   ```json
   {
     "bank_metadata": {
       "id": "REG-YYYY-MM-DD-v1",
       "generation_date": "YYYY-MM-DD",
       "total_questions": 25,
       "difficulty_distribution": {"foundational": 5, "intermediate": 10, "advanced": 10},
       "language_distribution": {"EN": 60, "ZH": 30, "Other": 10},
       "validation_status": "ALL_PASS"
     },
     "questions": [
       {
         "id": "T1-Q1",
         "topic": "Compliance Modeling",
         "question": "Full question text",
         "difficulty": "Advanced",
         "type": ["Compliance Modeling", "Privacy & Data Protection"],
         "stakeholders": ["Legal", "Compliance", "Architecture"],
         "frameworks": ["GDPR", "HIPAA"],
         "key_insight": "One sentence",
         "answer": "150-300 words",
         "citations": ["A1", "G12", "T1"],
         "artifacts": {
           "diagram": "mermaid code or description",
           "table": "markdown table",
           "metric": {"formula": "Coverage = X / Y × 100%", "value": "95%"}
         }
       }
     ],
     "references": {
       "glossary": [...],
       "tools": [...],
       "literature": [...],
       "citations": [...]
     }
   }
   ```
   ```

2. **Add metadata section** to Output Format (currently missing from template)

**Success Criteria**:
- Output format fully specified with TOC, metadata, Q&A structure, references
- Optional JSON schema provided for machine parsing

---

## Validation: Ensure Correctness

### G18: Evidence
**Guideline (Guidelines.md L38)**: Cite credible sources; flag uncertainty.

**Status**: ✅ **Met**

**Strengths (QA.md)**:
- L131-137: Citation standards well-defined (APA 7th, language tags, inline [Ref: ID])
- L159-167: Quality gates require ≥70% answers have ≥1 citation; ≥30% have ≥2 citations
- L607-669: 26 APA citations provided as examples
- L264: "Include ≥1 [Ref: ID] per answer"

**Gaps/Risks (QA.md)**:
- Missing: Explicit instruction to flag uncertainty (e.g., "If regulatory interpretation is disputed, acknowledge with 'Note: [Authority X] interprets this as Y; [Authority Z] differs'")
- Missing: Guidance on citing preliminary/draft regulations (e.g., EU AI Act drafts)

**Redundancies**:
- None

**Edits/Additions Needed**:
1. **Add Uncertainty Handling** (after L137):
   ```markdown
   **Uncertainty & Disputes**:
   - If regulation is draft/pending, flag with "[DRAFT as of YYYY-MM-DD]"
   - If regulatory interpretation is disputed among authorities, acknowledge: "Note: Interpretation varies. [Authority A] suggests X [Ref: A#]; [Authority B] suggests Y [Ref: B#]."
   - If no authoritative source found, do NOT fabricate; instead: "Unknown/Needs Verification: [describe gap]; consult [suggested authority]."
   ```

2. **Add Validation Step 18** (after L204):
   ```markdown
   **Step 18 – Uncertainty Flagging**: ≥90% of answers citing draft regulations or disputed interpretations include explicit uncertainty flags
   ```

**Success Criteria**:
- All answers cite credible sources
- Uncertainty and disputes explicitly flagged

---

### G19: Validation
**Guideline (Guidelines.md L39)**: Request reasoning, self-review, error checks.

**Status**: ✅ **Met**

**Strengths (QA.md)**:
- L169-227: Comprehensive 16-step Pre-Submission Validation with exact thresholds
- L205-225: Validation Report Template with PASS/FAIL table
- L227: "MANDATORY: If ANY check shows FAIL, stop, fix issues, regenerate, and re-run validation"
- L277-278: Instructions Step 6 requires executing all 16 validation steps

**Gaps/Risks (QA.md)**:
- L169-227: Validation steps are extensive but no "self-critique" or "error check" step (e.g., "Read 3 random Q&As aloud; check for clarity/coherence")
- Missing: Instruction for LLM to reason about validation results (e.g., "If citation coverage is 65% (< 70% threshold), explain why and propose fix")

**Redundancies**:
- None

**Edits/Additions Needed**:
1. **Add Self-Review Step** (after L204):
   ```markdown
   **Step 17 – Self-Review**: Randomly sample 3 Q&As; read aloud (simulate); check:
   - Is question unambiguous? (no)
   - Is answer coherent and well-structured? (yes)
   - Are citations accurate (no broken [Ref: ID])? (yes)
   - Does Key Insight match answer content? (yes)
   ```

2. **Add Reasoning Requirement** (L227):
   ```markdown
   If ANY check shows FAIL, stop and:
   1. Explain why validation failed (e.g., "Step 2 failed: only 65% answers have ≥1 citation; threshold is 70%")
   2. Propose specific fix (e.g., "Add citations to Q3, Q7, Q12, Q18, Q22")
   3. Re-generate affected content
   4. Re-run validation until ALL checks PASS
   ```

**Success Criteria**:
- All validation steps executed with PASS/FAIL results
- LLM provides reasoning for failures and proposes fixes

---

### G20: Practicality
**Guideline (Guidelines.md L40)**: Ensure actionable, implementable guidance.

**Status**: ✅ **Met**

**Strengths (QA.md)**:
- L286-362: 12 Practical Prompts provide copy-paste ready templates for common deliverables
- L676-753: Example question demonstrates implementable architectural controls (PostgreSQL row-level security, Kafka, Vault, Terraform)
- L689-702: Example includes concrete metrics (95% PII deletable, 100% EU data residency, €14M→€700K residual risk)
- L406-412: Success Factors emphasize actionable outcomes (RACI, decision ownership, remediation plans)

**Gaps/Risks (QA.md)**:
- None significant

**Redundancies**:
- None

**Edits/Additions Needed**:
- None required

**Success Criteria**:
- All guidance actionable and implementable
- Examples include concrete metrics, tools, and workflows

---

### G21: Success Criteria
**Guideline (Guidelines.md L41)**: Define measurable, concrete outcomes.

**Status**: ⚠️ **Partially Met**

**Strengths (QA.md)**:
- L169-227: 16 validation steps provide measurable success criteria (≥70% citation coverage, ≥80% reg-tech mapping, etc.)
- L229-234: Submission Checklist provides pass/fail criteria
- L689-702: Example includes quantitative success metrics (95% coverage, €700K residual risk)

**Gaps/Risks (QA.md)**:
- L229-234: Submission Checklist is high-level; doesn't specify *what success looks like* for the generated Q&A bank as a whole
- Missing: Overall success criteria (e.g., "Success = Bank enables interviewers to assess candidate's regulatory-technical translation skills across 7 stakeholder perspectives")
- Missing: User acceptance criteria (e.g., "Success = ≥80% of interviewers rate questions as 'realistic and discriminative'")
- Missing: Downstream impact criteria (e.g., "Success = Candidates hired using this bank have ≥90% compliance audit pass rate in first year")

**Redundancies**:
- None

**Edits/Additions Needed**:
1. **Add Overall Success Criteria** (after L234):
   ```markdown
   ## Success Criteria for Generated Question Bank
   
   A generated question bank is successful if it meets ALL of the following:
   
   ### Validation Criteria (Automated)
   - [ ] All 16 validation steps PASS (L169-204)
   - [ ] Reference floors met: Glossary ≥18, Tools ≥6, Literature ≥8, APA ≥12
   - [ ] Quantitative thresholds met: 25-30 Q&As, 20/40/40 difficulty, ≥70% citation coverage, ≥80% reg-tech mapping
   
   ### Quality Criteria (Human Review)
   - [ ] Questions are **realistic**: Scenarios match actual regulatory challenges faced by senior practitioners
   - [ ] Questions are **discriminative**: ≥70% test judgment/synthesis, not just recall
   - [ ] Answers are **actionable**: Include concrete controls, metrics, and stakeholder coordination
   - [ ] Answers are **balanced**: Present ≥2 perspectives for multi-stakeholder issues; acknowledge limitations
   
   ### Impact Criteria (Post-Deployment)
   - [ ] **Interviewer Utility**: ≥80% of interviewers rate bank as "useful for assessing regulatory-technical skills"
   - [ ] **Candidate Differentiation**: Bank successfully discriminates between junior/mid/senior candidates (validated through hiring outcomes)
   - [ ] **Compliance Predictiveness**: Candidates scoring well on bank have ≥85% audit pass rate in first year (if trackable)
   ```

2. **Add "Non-Goals" section** (after Success Criteria):
   ```markdown
   ## Non-Goals (Out of Scope)
   
   This prompt does NOT generate:
   - Legal advice or normative recommendations (educates, not prescribes)
   - Jurisdiction-specific legal interpretations requiring licensed counsel
   - Implementation code or complete system designs (provides architectural patterns only)
   - Compliance audit reports or certification evidence
   - Regulatory text analysis or clause-by-clause commentary
   ```

**Success Criteria**:
- Measurable success criteria defined for validation, quality, and impact
- Non-goals explicitly stated to prevent scope creep

---

## Summary of Required Edits

### High Priority (Impacts Guidelines 1, 2, 10, 17, 21)

1. **Add Context Header** (after L1) – G1 Context
2. **Add Acronym Policy** (after L283) – G2 Clarity
3. **Consolidate redundancies** (L3, L22-28, L371-412) – G10 Concision
4. **Expand Output Format Specification** (replace L422-440) – G17 Output Format
5. **Add Overall Success Criteria & Non-Goals** (after L234) – G21 Success Criteria

### Medium Priority (Impacts Guidelines 8, 14, 15)

6. **Add depth scaling by difficulty** (after L18) – G8 Depth
7. **Expand Risk/Value guidance** (after L28) – G14 Risk/Value
8. **Operationalize Fairness** (expand L29) – G15 Fairness

### Low Priority (Minor Improvements)

9. **Add Document Map & Quick Reference** (after L1) – G16 Structure
10. **Add Uncertainty Handling** (after L137) – G18 Evidence
11. **Add Self-Review Step & Reasoning Requirement** (L227) – G19 Validation
12. **Verify penalty amounts** (L689) – G11 Accuracy
13. **Add source quality policy** (after L137) – G12 Credibility

---

## Conclusion

**Overall Assessment**: QA.md is a comprehensive, well-structured meta-prompt with excellent depth, credibility, and validation. It scores **62% Met** (13/21 guidelines fully met) and **38% Partially Met** (8/21 guidelines partially met), with **0% Not Met**.

**Key Strengths**:
- Exceptional validation framework (16 steps)
- Strong MECE coverage (4 dimensions × 7 stakeholders)
- High credibility (authoritative sources, quality gates)
- Excellent practical guidance (12 copy-paste prompts)

**Key Improvement Areas**:
1. **Context & Clarity** (G1, G2): Add explicit context statement, assumptions, and acronym policy
2. **Concision** (G10): Remove redundancies in stakeholder lists and quality criteria sections
3. **Output Format** (G17): Expand template with metadata, JSON schema, and complete example
4. **Success Criteria** (G21): Define measurable outcomes for validation, quality, and impact; add non-goals
5. **Fairness** (G15): Operationalize balanced perspectives and limitation acknowledgment

**Recommendation**: Implement High Priority edits first, then Medium Priority. Low Priority edits can be applied incrementally. After edits, re-run this analysis to confirm 100% Met across all 21 guidelines.

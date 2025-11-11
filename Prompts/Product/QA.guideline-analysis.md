# QA.md 21-Guideline Compliance Analysis

**File**: `Prompts/Product/QA.md` (1017 lines)  
**Analysis Date**: 2025-11-11  
**Guidelines Source**: `Prompts/Guidelines_for_LLM-Friendly_Prompts.md`

## Table of Contents

- [Foundation Guidelines (4)](#foundation-guidelines)
  - [F1. Context](#f1-context)
  - [F2. Clarity](#f2-clarity)
  - [F3. Precision](#f3-precision)
  - [F4. Relevance](#f4-relevance)
- [Scope Guidelines (4)](#scope-guidelines)
  - [S1. MECE](#s1-mece)
  - [S2. Sufficiency](#s2-sufficiency)
  - [S3. Breadth](#s3-breadth)
  - [S4. Depth](#s4-depth)
- [Quality Guidelines (7)](#quality-guidelines)
  - [Q1. Significance](#q1-significance)
  - [Q2. Concision](#q2-concision)
  - [Q3. Accuracy](#q3-accuracy)
  - [Q4. Credibility & Reliability](#q4-credibility--reliability)
  - [Q5. Logic](#q5-logic)
  - [Q6. Risk/Value](#q6-riskvalue)
  - [Q7. Fairness](#q7-fairness)
- [Format Guidelines (2)](#format-guidelines)
  - [FM1. Structure](#fm1-structure)
  - [FM2. Output Format](#fm2-output-format)
- [Validation Guidelines (4)](#validation-guidelines)
  - [V1. Evidence](#v1-evidence)
  - [V2. Validation](#v2-validation)
  - [V3. Practicality](#v3-practicality)
  - [V4. Success Criteria](#v4-success-criteria)
- [Summary & Priority Matrix](#summary--priority-matrix)

---

## Foundation Guidelines

### F1. Context

**Guideline**: State scope, constraints, assumptions.

**Present/Working** (Lines 1-8, 9-35):
- **Line 3**: Purpose explicitly stated: "Generate interview Q&A banks testing senior/director/VP-level Product Manager judgment"
- **Lines 9-20**: "Definitions & Terminology" section defines core terms (Q&A, Floor, Validation step, Difficulty levels, Evaluation dimensions)
- **Lines 21-34**: "Scope Boundaries" explicitly lists In Scope and Out of Scope items
- **Line 5**: Deliverable clearly specified: "25–30 scenario-based Q&A pairs with multi-dimensional evaluation"

**Gaps/Weaknesses**:
- **Missing audience**: No explicit statement of who will use this prompt (LLM system, PM trainer, interview prep platform)
- **Missing assumptions**: No explicit assumptions section (e.g., assumes familiarity with PM frameworks, assumes output in Markdown)
- **Missing constraints**: No time/token budget, no output size limits beyond Q&A count
- **Missing inputs required**: Doesn't explicitly list what inputs the LLM needs to receive (e.g., company context, seniority level focus, domain)

**Improvements Needed**:
1. Add **"Audience & Usage"** subsection in Section I stating: "This prompt is designed for large language models (LLMs) to generate interview Q&A banks. Users may be: PM hiring managers, interview prep platforms, or PM training programs."
2. Add **"Assumptions"** subsection listing: output format (Markdown), familiarity with PM terminology (RICE, JTBD, etc.), access to current literature (2021-2024), bilingual capability (EN/ZH)
3. Add **"Inputs Required"** subsection specifying optional inputs: target role seniority, industry/domain focus, geographical market (global, US, China), time constraints
4. Add **"Constraints"** subsection: recommended token budget (10K-15K output tokens), generation time (5-10 min for 30 Q&A)

**Impact**: High | **Effort**: Low | **Dependencies**: None

**Validation**: After edit, verify Section I.A contains Audience, Assumptions, Inputs, Constraints subsections.

---

### F2. Clarity

**Guideline**: Request clear, understandable explanations; avoid jargon without definition.

**Present/Working**:
- **Lines 13-20**: Core terms explicitly defined (Q&A, Floor, Validation step, Quality gate, Difficulty levels, Evaluation dimensions)
- **Lines 224-243**: "Question Design Principles" clearly explains format requirements and judgment signals
- **Lines 610-642**: "Quality Dimensions" with clear pass/fail examples
- **Lines 224**: Scenario-based format explained with examples: "How would you...", "Walk me through..."

**Gaps/Weaknesses**:
- **Lines 39-60**: Q&A Set Composition uses MECE without definition on first use (defined later in examples but not formally)
- **Lines 98-100**: "APA 7th edition" assumed known; no minimal example until Section VI.D.4 (line 921+)
- **Lines 427+**: Validation steps use technical measurement language ("Count Glossary entries: Must be ≥10") without explaining *how* to count in ambiguous cases
- **Lack of "why"**: Many requirements state *what* (≥10 glossary entries) but not *why* (ensures sufficient framework coverage for citation)

**Improvements Needed**:
1. Add **brief inline definition** for MECE at first use (line 47): "MECE (Mutually Exclusive, Collectively Exhaustive)" 
2. Add **APA quick reference** in Section II.C (lines 98-111): 1-2 sentence example of APA in-text and reference format
3. Add **rationale parentheticals** for quantitative floors: "(≥10 glossary entries ensures sufficient framework coverage for citations across 6 topic clusters)"
4. Add **"Terminology Quick Reference"** box near top with 5-7 most critical acronyms/terms used throughout

**Impact**: Medium | **Effort**: Low | **Dependencies**: None

**Validation**: Verify MECE defined at first use; APA example present in Section II; rationales added for 3+ quantitative requirements.

---

### F3. Precision

**Guideline**: Use specific terms; avoid ambiguity; maintain consistent terminology.

**Present/Working**:
- **Lines 42-44**: Quantitative requirements precisely specified: "25–30 Q&A pairs", "20% F / 40% I / 40% A (±5% tolerance)"
- **Lines 64-74**: Tool documentation requirements precisely listed with 4 mandatory fields
- **Lines 427-535**: 12 validation steps with precise measurement instructions and pass criteria
- **Lines 13-20**: Consistent use of terms: "Foundational (F)", "Intermediate (I)", "Advanced (A)" maintained throughout

**Gaps/Weaknesses**:
- **Line 10**: "Request clear, understandable explanations" – vague verbs without MUST/SHOULD/MAY hierarchy
- **Lines 148-175**: Step 1 uses soft language: "Create balanced coverage" (what defines "balanced"?), "aim for 4–6 per cluster" (is this mandatory?)
- **Lines 220-276**: Step 3 Generation Process says "Write 5 Q&A at a time" without stating whether this is mandatory sequencing or optional suggestion
- **Inconsistent modality**: Mix of "must", "should", "will", "need to" without clear RFC 2119 semantics

**Improvements Needed**:
1. **Add RFC 2119 notice** in Section I: "This document uses MUST/MUST NOT (mandatory), SHOULD/SHOULD NOT (recommended), MAY (optional) per RFC 2119 semantics."
2. **Replace ambiguous verbs** throughout:
   - "Create balanced coverage" → "MUST ensure balanced coverage (each cluster 4–6 Q&A, ±1 tolerance)"
   - "Need to include" → "MUST include"
   - "Should have" → "SHOULD have" (only where truly optional)
   - "Will" → "MUST" (for requirements) or "will" (for descriptive outcomes)
3. **Quantify "balanced"** (line 150): Define as "No cluster <4 Q&A, no cluster >6 Q&A; std dev <1.0"
4. **Add precision to subjective terms**: "sufficient detail" → "150-300 words", "recent sources" → "≥50% from last 3 years"

**Impact**: High | **Effort**: Medium | **Dependencies**: Requires full-document review for verb replacement

**Validation**: After edit, verify ≥80% of requirements use MUST/SHOULD/MAY; no instances of "need to", "will" for requirements; quantitative thresholds for previously subjective terms.

---

### F4. Relevance

**Guideline**: Stay on topic; exclude tangential information.

**Present/Working**:
- **Lines 21-34**: Explicit "Scope Boundaries" section listing In Scope and Out of Scope items
- **Lines 29-33**: Out of Scope clearly excludes: trivia/recall questions, hypothetical greenfield design, junior-level tasks, domain-specific technical knowledge
- **Lines 427-535**: 12-point validation checklist maintains focus on Q&A quality dimensions relevant to PM judgment

**Gaps/Weaknesses**:
- **Lines 64-74, 183-218**: Tool documentation requirements (pricing tier, user base, integrations) may be excessive detail not directly relevant to Q&A generation quality
- **Lines 277-320**: Visual Artifacts section (Step 4) is comprehensive but lacks relevance filter: when to include vs. omit artifacts, how artifacts tie to Q&A quality
- **Section VI**: Output Format Template (lines 667-976) is extremely detailed (310 lines, ~30% of document) with redundant examples; may overwhelm core task

**Improvements Needed**:
1. **Add relevance filter to Tool Requirements** (line 69+): "Tool details MUST support answer citations and practical application examples; MAY omit pricing/integrations if not cited in Q&A."
2. **Add artifact relevance criteria** (line 277): "Include artifacts when: (1) answer cites the artifact, (2) artifact demonstrates PM judgment framework, (3) artifact is reusable template. SKIP artifacts that are decorative or redundant to text."
3. **Condense Section VI** (Output Format Template): Move detailed examples to separate appendix; keep only 1 minimal + 1 complete example in main body
4. **Add "Relevance Check"** to Step 6 Validation: "Verify all included references are cited ≥1 time; remove orphaned entries."

**Impact**: Medium | **Effort**: Medium | **Dependencies**: Requires Section VI restructuring

**Validation**: After edit, verify: artifact relevance criteria present; tool requirements include relevance conditional; Section VI reduced by ~30%; orphaned reference check in validation.

---

## Scope Guidelines

### S1. MECE

**Guideline**: Ensure complete, non-overlapping coverage.

**Present/Working**:
- **Lines 47-53**: 6 topic clusters explicitly labeled "MECE - Mutually Exclusive, Collectively Exhaustive"
- **Lines 47-53**: Content coverage spans: Strategy & Vision, Discovery & User Research, Prioritization & Roadmapping, Metrics & Analytics, Stakeholder Management, Go-to-Market & Growth
- **Lines 158-166**: Step 1 requires difficulty distribution across all clusters: "each cluster should have ≥1F, ≥1I, ≥1A"

**Gaps/Weaknesses**:
- **Potential overlap**: "Strategy & Vision" (line 48) vs "Go-to-Market & Growth" (line 53) – growth strategy could belong to either
- **Potential overlap**: "Prioritization & Roadmapping" (line 50) vs "Stakeholder Management" (line 52) – stakeholder input drives prioritization
- **Coverage completeness**: Missing cross-functional areas: Legal/Compliance, Internationalization, Accessibility, Platform/API strategy (called out as Advanced topic in example but not in clusters)
- **No mutual exclusivity test**: No guidance on how to classify questions that span multiple clusters

**Improvements Needed**:
1. **Add cluster definitions** in Section II.A (after line 53): 
   - Strategy & Vision: Long-term direction, market positioning, competitive moats, vision alignment
   - Go-to-Market & Growth: Launch execution, channel strategy, growth loops, activation/retention tactics (not strategic positioning)
2. **Add classification decision tree** (new subsection after line 53):
   ```
   If question involves stakeholder input: 
     → Primary cluster = decision domain (Prioritization if about roadmap ranking)
     → Tag as cross-functional for Stakeholder Management
   If question spans strategy + growth:
     → Primary cluster = time horizon (Strategy if 12+ months, GTM if 0-6 months)
   ```
3. **Add "Edge Cases" subsection** documenting: Platform/API strategy → Strategy & Vision; Compliance → Stakeholder Management; Internationalization → Go-to-Market & Growth
4. **Add MECE validation step** in Step 6: "Verify each Q&A assigned to exactly 1 primary cluster; ≤20% have secondary cluster tags."

**Impact**: Medium | **Effort**: Medium | **Dependencies**: Requires cluster definition consensus

**Validation**: After edit, verify: 6 clusters have clear boundary definitions; decision tree present; MECE validation step added; edge cases documented.

---

### S2. Sufficiency

**Guideline**: Ensure comprehensive coverage of all necessary aspects.

**Present/Working**:
- **Lines 39-60**: Q&A Set Composition covers: count (25-30), difficulty distribution, answer length, citation density, content coverage (6 clusters), multi-dimensional evaluation (4 dimensions)
- **Lines 61-83**: Reference floors specified: ≥10 glossary, ≥5 tools, ≥6 literature, ≥12 APA citations
- **Lines 426-535**: 12-point validation checklist covers quantitative floors, citations, language distribution, recency, diversity, links, integrity, word count, key insight, evidence, frameworks, judgment ratio
- **Lines 667-976**: Complete output format template with TOC, tables, Q&A structure, reference sections, validation report

**Gaps/Weaknesses**:
- **Missing coverage**: No guidance on handling domain-specific PM roles (Technical PM, Growth PM, Platform PM, AI/ML PM) – are separate Q&A sets needed?
- **Missing coverage**: No guidance on international markets beyond language (US vs China PM practices differ significantly)
- **Insufficient breadth**: 6 clusters may miss: Team leadership, Technical depth, Data science collaboration, Security/Privacy, Developer experience (for platform PMs)
- **No "sufficiency test"**: How to verify 25-30 Q&A is enough? What if role requires 40-50 Q&A for comprehensive coverage?

**Improvements Needed**:
1. **Add "Role Variants" subsection** in Section I.B (after line 34):
   ```
   This prompt generates general PM Q&A. For specialized roles:
   - Technical PM: Add ≥3 Q&A in "Technical Depth & Architecture" cluster
   - Growth PM: Increase GTM cluster to 8-10 Q&A, reduce Strategy to 3-4
   - Platform PM: Add ≥3 Q&A on developer experience, API design, ecosystem
   ```
2. **Add "Sufficiency Validation"** in Step 6:
   ```
   Verify coverage sufficiency:
   - Each evaluation dimension (Product, Business, Strategic, Operational) appears in ≥40% of answers
   - Each framework in Glossary cited ≥1 time
   - Each tool in Tools section cited ≥1 time in relevant cluster
   ```
3. **Add "Scaling Guidance"** (line 82-83 exists but insufficient):
   ```
   For >30 Q&A (e.g., 40-50 for comprehensive coverage):
   - Add ≥1 cluster OR deepen existing clusters to 7-8 Q&A each
   - Scale reference floors: ×1.5 for 40-50 Q&A, ×2 for 50+ Q&A
   - Maintain difficulty distribution: 20%F/40%I/40%A regardless of count
   ```
4. **Add completeness check**: "Verify no critical PM competency omitted: user research, data analysis, technical collaboration, executive communication, team leadership"

**Impact**: High | **Effort**: Medium | **Dependencies**: None

**Validation**: After edit, verify: role variants documented; sufficiency validation added; scaling guidance expanded; completeness check in validation.

---

### S3. Breadth

**Guideline**: Request multiple perspectives where appropriate.

**Present/Working**:
- **Lines 55-60**: Multi-dimensional evaluation requires ≥2 dimensions per answer: Product, Business, Strategic, Operational
- **Lines 86-90**: Language distribution requirement: 60% EN, 30% ZH, 10% Other – provides multilingual perspective
- **Lines 197-201**: Chinese sources required (≥2 ZH sources: 俞军, 梁宁, 苏杰) – cultural/regional perspectives
- **Lines 232-238**: Judgment Signals require testing ≥2 signals per question: trade-offs, opportunity cost, stakeholder tension, incomplete information, execution complexity

**Gaps/Weaknesses**:
- **Limited geographical breadth**: Only EN/ZH covered; no mention of EU (GDPR), LATAM, APAC perspectives beyond China
- **Limited industry breadth**: No explicit coverage of B2B vs B2C, SaaS vs Hardware, Consumer vs Enterprise, Regulated industries (Healthcare, Finance)
- **Limited stakeholder breadth**: Engineering, design, sales, marketing mentioned but not systematically covered; missing: legal, finance, support, data science
- **No perspective balance requirement**: Answers could be biased toward single perspective (e.g., all answers prioritize revenue over user value)

**Improvements Needed**:
1. **Add "Industry Diversity" requirement** in Section II.A (after line 53):
   ```
   Q&A SHOULD span industry contexts:
   - ≥30% B2B SaaS / Enterprise Software
   - ≥30% B2C Consumer / Mobile
   - ≥20% Platform / Marketplace / Two-sided markets
   - ≥20% Emerging domains (AI/ML, Web3, IoT, AR/VR)
   Avoid: ≥60% concentration in single industry
   ```
2. **Add "Stakeholder Breadth" requirement** in Section II.A:
   ```
   Across all 30 Q&A, MUST include stakeholder perspectives from ≥4 functions:
   - Engineering (technical feasibility, velocity, technical debt)
   - Design (user experience, accessibility, design system)
   - Sales/GTM (customer requests, deal blockers, positioning)
   - Executive (strategy, budget, board reporting)
   - Data (analytics, experimentation, insights)
   - Operations (support, scalability, security, legal/compliance)
   ```
3. **Add "Perspective Balance" validation** in Step 6:
   ```
   Verify perspective balance across answers:
   - ≥30% answers prioritize user value / product-market fit
   - ≥30% answers prioritize business outcomes / revenue
   - ≥20% answers prioritize strategic positioning / competitive moat
   - ≥20% answers prioritize operational excellence / velocity
   No dimension <20% or >40%
   ```
4. **Expand geographical scope** (line 89): Add note: "For global roles, MAY include EU/GDPR, APAC, LATAM perspectives; adjust language distribution accordingly"

**Impact**: High | **Effort**: Medium | **Dependencies**: Requires industry/stakeholder taxonomy

**Validation**: After edit, verify: industry diversity requirement present; stakeholder breadth ≥4 functions; perspective balance validation added; geographical note expanded.

---

### S4. Depth

**Guideline**: Request thorough treatment with sufficient detail.

**Present/Working**:
- **Lines 44-45**: Answer length requirement: 150-300 words ensures sufficient depth
- **Lines 246-276**: Answer Structure template requires 6 components: Key Insight, Framework/approach, Multi-dimensional analysis, Concrete steps, Trade-offs, Stakeholder communication, Success criteria
- **Lines 239-243**: Seniority Alignment distinguishes depth by level: Foundational (execution), Intermediate (strategy/trade-offs), Advanced (portfolio/vision/P&L)
- **Lines 624-629**: Depth criterion: "Enables discussion of trade-offs, opportunity costs, execution challenges"

**Gaps/Weaknesses**:
- **Shallow multi-dimensional requirement**: "Address ≥2 dimensions" (line 55) is minimum bar; doesn't ensure depth within each dimension
- **No depth threshold for frameworks**: Frameworks mentioned but not explained (e.g., "Use RICE" without showing calculation or discussing limitations)
- **No second-order thinking**: Answers may stop at first-level analysis without considering: "What happens next?", "What could go wrong?", "What are the long-term consequences?"
- **Example depth mismatch**: Complete Example (lines 977-1017) is 40 lines for 1 Q&A; if all 30 Q&A at this depth, output would be 1200 lines – conflicts with concision

**Improvements Needed**:
1. **Strengthen multi-dimensional depth** (line 252):
   ```
   Multi-dimensional analysis MUST include:
   - For EACH dimension addressed (≥2 required):
     * Specific metric or outcome (not generic "improves revenue")
     * Quantitative estimate or range where possible ("$500K-2M revenue impact")
     * Time horizon (short-term <6mo, medium 6-18mo, long-term 18mo+)
   ```
2. **Add "Framework Depth" requirement** (line 251):
   ```
   When citing frameworks [Ref: G#]:
   - MUST explain application steps (not just name framework)
   - SHOULD acknowledge limitations or failure modes
   - For Advanced (A) questions: MUST discuss when framework is insufficient and what to supplement with
   ```
3. **Add "Second-Order Thinking" requirement** (new in Step 3):
   ```
   For Intermediate/Advanced questions, answers SHOULD address:
   - Downstream consequences: "What happens after we make this decision?"
   - Failure modes: "What are the ways this could go wrong?"
   - Hidden costs: "What are the second-order resource/velocity impacts?"
   - Reversibility: "How easy is it to undo this decision later?"
   ```
4. **Add depth validation** in Step 8 (Answer Word Count):
   ```
   Beyond word count, verify depth quality in ≥5 sampled answers:
   - ≥2 dimensions with specific metrics/outcomes (not generic statements)
   - ≥1 framework explained with steps (not just named)
   - For A-level: ≥1 second-order consideration (consequences/failure modes)
   ```

**Impact**: High | **Effort**: Medium | **Dependencies**: None

**Validation**: After edit, verify: multi-dimensional depth requirements strengthened; framework depth added; second-order thinking requirement present; depth validation added to Step 8.

---

## Quality Guidelines

### Q1. Significance

**Guideline**: Prioritize important information; exclude trivial details.

**Present/Working**:
- **Lines 29-33**: Out of Scope explicitly excludes trivia: "Trivia/recall questions ('What is AARRR?')"
- **Lines 526-534**: Validation Step 12 (Judgment vs Recall) requires ≥70% judgment-based questions to filter out trivia
- **Lines 246-249**: Key Insight requirement ensures each Q&A addresses "specific dilemma/tension" – prioritizes significant PM challenges
- **Lines 232-238**: Judgment Signals ensure questions test: trade-off analysis, opportunity cost, stakeholder tension, incomplete information, execution complexity – all high-significance areas

**Gaps/Weaknesses**:
- **Tool details may be trivial** (lines 70-74): Pricing tier, last update date, integrations count – not directly relevant to Q&A quality; only URL and PM use case are significant
- **Excessive template repetition** (Section VI): 3 separate TOC templates (lines 676, 702, 729) with redundant structure
- **Over-specification of formats**: APA 7th edition format shown 4+ times (lines 98, 355, 923, 929) – significant for validation but repetitive in instructions
- **No significance filter in validation**: Validation checks completeness (word count, citations, cross-refs) but not whether content is significant vs trivial

**Improvements Needed**:
1. **Reduce tool documentation fields** (lines 69-74):
   ```
   Remove: Pricing tier (low significance for Q&A generation)
   Remove: Last update date (unless evaluating tool recency for specific Q&A)
   Keep: PM use case, notable customers/user base, URL
   Optional: Integrations (only if cited in answer for cross-tool workflow)
   ```
2. **Consolidate templates** (Section VI): Keep 1 comprehensive TOC template; remove redundant partial templates at lines 702, 729
3. **Add "Significance Filter"** to Step 7 (Final Review):
   ```
   Review ≥5 answers for significance:
   - Does answer address real PM dilemma faced by senior+ practitioners?
   - Does answer provide non-obvious insight (not just textbook recitation)?
   - Would a director+ PM find this answer valuable in actual decision-making?
   FAIL if >20% answers are trivial/obvious
   ```
4. **Reduce APA format repetition**: Show format once in Section II.C; thereafter reference "See Section II.C for APA format"

**Impact**: Medium | **Effort**: Low | **Dependencies**: None

**Validation**: After edit, verify: tool fields reduced; templates consolidated; significance filter added to Step 7; APA references deduplicated.

---

### Q2. Concision

**Guideline**: Remove redundancy; include only essential information.

**Present/Working**:
- **Lines 44-45**: Answer length capped at 150-300 words to enforce concision
- **Lines 427**: "Count Glossary entries: Must be ≥10" – concise quantitative spec
- **Lines 169-172**: Self-Check uses compact checklist format

**Gaps/Weaknesses**:
- **Document length**: 1017 lines total; Section VI alone is 310 lines (~30%) with redundant examples
- **Redundant validation**: Validation requirements appear in 3 places: Section II.D (Quality Gates), Section III.Step 6, Section IV.A (12-Point Checklist) – significant overlap
- **Repetitive instructions**: Step-by-step instructions repeat concepts:
  - "Citation requirements" explained in II.B (lines 61-83), II.C (84-111), III.Step 2 (176-219), VI.D.4 (921-954)
  - "Difficulty distribution 20/40/40" stated 6+ times throughout document
- **Verbose examples**: Complete Example Question (lines 977-1017) is 40 lines; could be condensed to 20 lines with equal clarity

**Improvements Needed**:
1. **Consolidate validation sections**:
   - Merge Section II.D (Quality Gates) into Section IV.A (12-Point Checklist) with cross-reference
   - Reduce from 3 sections to 2: (1) Requirements (Section II), (2) Validation Steps (Section IV)
   - Add brief reference in Step 6: "Execute 12-point validation (Section IV.A)"
2. **Create reference shortcuts**:
   - First mention: "Difficulty distribution: 20% F / 40% I / 40% A (±5% tolerance)"
   - Subsequent mentions: "Maintain 20/40/40 difficulty distribution"
   - Define once, reference thereafter
3. **Condense Section VI**:
   - Reduce 310 lines to ~150 lines by:
     * Removing redundant TOC examples (keep 1)
     * Condensing Complete Example from 40 lines to 20 lines
     * Moving detailed APA examples to appendix or external reference
4. **Add "Essential Content Only" instruction** at top:
   ```
   LLM MUST produce only essential output per Section VI template:
   - TOC with anchor links
   - 25-30 Q&A following template
   - 4 Reference Sections
   - Validation Report
   DO NOT include: preamble, explanatory commentary, meta-discussion, acknowledgments
   ```

**Impact**: High | **Effort**: High | **Dependencies**: Requires document restructuring

**Validation**: After edit, verify: document reduced to <750 lines; validation consolidated to 2 sections; reference shortcuts used; "Essential Content Only" instruction added.

---

### Q3. Accuracy

**Guideline**: Verify factual correctness; cross-check information.

**Present/Working**:
- **Lines 97-111**: Citation & Source Standards require APA 7th edition citations with language tags – supports fact-checking
- **Lines 115-118**: Gate 1 (Recency) requires ≥50% citations from last 3 years – ensures currency of facts
- **Lines 127-129**: Gate 3 (Per-Topic Evidence) requires ≥2 authoritative sources per cluster – supports accuracy through multiple sources
- **Lines 514-524**: Validation Step 11 (Framework Usage Accuracy) verifies frameworks correctly described and cited

**Gaps/Weaknesses**:
- **No accuracy verification process**: Instructions require citations but don't require LLM to verify claims against sources
- **No fact-checking step**: Quantitative claims (e.g., "40% of revenue", "5K+ users") in examples may be illustrative vs. factual
- **No source quality threshold**: "≥6 books/frameworks" (line 67) doesn't specify peer-reviewed, reputable publishers, or academic sources
- **No contradiction detection**: No validation step to check for internal contradictions (e.g., conflicting recommendations across answers)

**Improvements Needed**:
1. **Add "Source Quality Standards"** in Section II.B (after line 67):
   ```
   Source Quality Thresholds:
   - Literature: MUST be from reputable publishers (O'Reilly, Wiley, major academic presses) OR recognized PM thought leaders (Cagan, Torres, Perri)
   - Research: PREFER peer-reviewed journals, industry research (Gartner, Forrester), reputable PM blogs (Silicon Valley Product Group, Lenny's Newsletter)
   - Case Studies: MUST cite source (company blog, business publication, documented postmortem)
   AVOID: Unverified blog posts, promotional content, opinion without data, Wikipedia as primary source
   ```
2. **Add "Accuracy Verification" in Step 6**:
   ```
   Validation Step 13 - Accuracy Check:
   - Extract all quantitative claims (percentages, counts, timeframes)
   - Verify each claim either: (a) cited with [Ref: ID], (b) labeled as hypothetical example
   - Check 5 random citations: verify [Ref: ID] resolves to relevant source in References
   - Verify no internal contradictions (e.g., Q15 recommends X, Q22 recommends opposite without acknowledging trade-off)
   PASS: 100% quantitative claims cited or labeled; 5/5 citations valid; 0 contradictions
   ```
3. **Add "Hypothetical Labeling"** requirement (lines 770-791 example):
   ```
   When using illustrative examples with specific numbers:
   - Label as "[Hypothetical example]" or use ranges: "30-50% of revenue"
   - Avoid specific false precision: NOT "40% of revenue" UNLESS cited
   ```
4. **Add source verification instruction**: "Before finalizing, LLM SHOULD verify ≥5 randomly selected citations resolve to relevant, accessible sources"

**Impact**: High | **Effort**: Medium | **Dependencies**: Requires adding Validation Step 13

**Validation**: After edit, verify: source quality standards present; accuracy verification added as Step 13; hypothetical labeling requirement present; source verification instruction added.

---

### Q4. Credibility & Reliability

**Guideline**: Prioritize authoritative, high-quality, tested sources; avoid low-quality or unproven content.

**Present/Working**:
- **Lines 197-201**: Authoritative Literature requires recognized sources: Cagan (*Inspired*), Olsen (*Lean Product Playbook*), Torres (*Continuous Discovery*), plus Chinese PM authorities (俞军, 梁宁, 苏杰)
- **Lines 115-118**: Gate 1 (Recency) prioritizes recent sources (≥50% from last 3 years)
- **Lines 121-125**: Gate 2 (Source Diversity) requires ≥3 source types – prevents over-reliance on single source category
- **Lines 72-73**: Tool requirements include "User base size or notable customers" – credibility signal

**Gaps/Weaknesses**:
- **No explicit source credibility criteria**: "Authoritative Literature" lists examples but doesn't define what makes a source authoritative
- **Tools section lacks reliability filter**: ≥5 tools required but no quality threshold (could include obscure tools with 100 users)
- **No peer-review requirement**: Research sources don't require peer review or academic rigor
- **ZH source reliability undefined**: Requires ≥2 ZH sources but doesn't specify credibility criteria (e.g., 俞军 is credible, but random Chinese blog is not)

**Improvements Needed**:
1. **Add "Source Credibility Criteria"** in Section II.B (before line 67):
   ```
   Credibility Standards for Sources:
   - Books: MUST be from established PM thought leaders (Cagan, Torres, Olsen, Perri, Patton) OR reputable publishers (O'Reilly, Wiley, Pragmatic Bookshelf)
   - Research: PREFER (in order): (1) Peer-reviewed academic, (2) Industry analysts (Gartner, Forrester), (3) Product-focused research firms (ProductPlan, Pendo)
   - Case Studies: MUST be first-party (company blog, official postmortem) OR reputable business publication (HBR, TechCrunch, The Information)
   - Tools: MUST have ≥1K users OR recognized brand (YC-backed, established company) OR featured in reputable tool reviews
   - Chinese (ZH) Sources: MUST be recognized authorities (俞军/Baidu, 梁宁/Tencent, 苏杰/Alibaba) OR major PM platforms (人人都是产品经理, PMCAFF)
   ```
2. **Add "Reliability Check"** in Step 2.4 (APA Citations):
   ```
   For each APA citation, verify reliability:
   - Author credentials: Known PM practitioner, academic, or industry analyst?
   - Publication venue: Reputable publisher/platform or self-published blog?
   - Evidence base: Data-driven, case studies, or pure opinion?
   - Corroboration: Can claims be verified with second source?
   Mark questionable sources with [Note: Limited corroboration] and seek alternatives.
   ```
3. **Strengthen Tool credibility** (line 72):
   ```
   User Base: MUST specify ≥1K users OR notable customers from Fortune 500/unicorns
   If tool has <1K users, MUST justify inclusion: e.g., "Emerging tool with strong PM community traction" [cite source]
   ```
4. **Add credibility validation** in Step 6:
   ```
   Validation Step 14 - Source Credibility:
   - Verify ≥80% of Literature sources are recognized authorities per credibility criteria
   - Verify ≥80% of Research sources are peer-reviewed or industry analyst reports
   - Verify 100% of Tools have ≥1K users OR notable customers
   PASS: All thresholds met
   ```

**Impact**: High | **Effort**: Medium | **Dependencies**: Requires adding Validation Step 14

**Validation**: After edit, verify: source credibility criteria present; reliability check in Step 2.4; tool credibility strengthened; credibility validation added as Step 14.

---

### Q5. Logic

**Guideline**: Demand coherent reasoning and sound structure.

**Present/Working**:
- **Lines 246-262**: Answer Structure requires logical flow: Framework → Analysis → Steps → Trade-offs → Communication → Success Criteria
- **Lines 146-386**: Step-by-Step Instructions provide sequential logic: Topic Planning → Reference Collection → Q&A Generation → Artifacts → Sections Population → Validation → Final Review
- **Lines 514-524**: Framework Usage Accuracy validates correct application of frameworks
- **Lines 610-642**: Question Design Critique includes "Logic" as inherent in pass/fail examples

**Gaps/Weaknesses**:
- **No logical consistency check**: Answers could contain contradictory recommendations without validation catching it
- **No reasoning chain requirement**: Answers state conclusions but may skip logical steps (e.g., "Use RICE" without showing how inputs lead to decision)
- **Circular logic risk**: Trade-offs section could state "prioritize X because X is priority" without independent rationale
- **Missing assumption documentation**: Answers make implicit assumptions (e.g., "users prefer Y") without stating them

**Improvements Needed**:
1. **Add "Reasoning Chain" requirement** in Answer Structure (line 252):
   ```
   Concrete steps MUST show logical reasoning chain:
   - NOT: "First, use RICE. Second, present to stakeholders."
   - YES: "First, gather RICE inputs (Reach: 5K users, Impact: 8/10, Confidence: 70%, Effort: 4 weeks).
           Second, calculate score (5K × 8 × 0.7 / 4 = 7K). Third, compare to alternatives [scores X, Y].
           Fourth, present top-ranked option with rationale."
   Reasoning MUST be traceable: each step follows from previous step or stated assumption.
   ```
2. **Add "Assumptions Declaration"** requirement (new in Answer Structure):
   ```
   When answer makes assumptions, MUST state them explicitly:
   - Market assumptions: "Assuming competitive market (3+ strong alternatives)"
   - User assumptions: "Assuming users are power users (DAU/MAU >40%)"
   - Resource assumptions: "Assuming 2-3 eng sprints available (6-9 weeks)"
   For Advanced (A) questions, SHOULD discuss sensitivity: "If assumption X is false, recommendation changes to Y"
   ```
3. **Add "Logical Consistency" validation** in Step 6:
   ```
   Validation Step 15 - Logical Consistency:
   - Sample 5 random answers
   - Check for internal contradictions within answer
   - Check for cross-answer contradictions (Q5 recommends A, Q18 recommends not-A without acknowledging trade-off)
   - Verify reasoning chains: each conclusion follows from stated premises
   PASS: 0 contradictions; 5/5 answers have traceable reasoning
   ```
4. **Add "Fallacy Detection"** note in Step 7 (Final Review):
   ```
   Watch for common reasoning fallacies:
   - Circular reasoning: "Prioritize X because X is important" (define importance criteria)
   - False dichotomy: "Either A or B" (acknowledge C, D alternatives)
   - Appeal to authority: "Cagan says X" without contextualizing or evaluating
   - Sunk cost: "Already invested Y, so continue" (evaluate go-forward value independently)
   ```

**Impact**: High | **Effort**: Medium | **Dependencies**: Requires adding Validation Step 15

**Validation**: After edit, verify: reasoning chain requirement present; assumptions declaration added; logical consistency validation added as Step 15; fallacy detection note in Step 7.

---

### Q6. Risk/Value

**Guideline**: Assess risks, costs, and benefits; prioritize high-value, low-risk options; flag high-risk choices with mitigation strategies.

**Present/Working**:
- **Lines 254**: Trade-Offs requirement: "Explicitly state what you're optimizing for and what you're sacrificing" – addresses value trade-offs
- **Lines 232-238**: Judgment Signals include "Opportunity cost evaluation" and "Execution complexity assessment" – risk considerations
- **Lines 777**: Key Insight example: "Tests tension between short-term revenue protection and long-term product-market fit" – value trade-off
- **Lines 59**: Operational dimension includes "risk mitigation" as evaluation criteria

**Gaps/Weaknesses**:
- **No risk assessment framework**: Answers may mention risks but lack systematic risk evaluation (likelihood × impact)
- **No mitigation requirement**: "Risk mitigation" mentioned (line 60) but not required in answer structure
- **Value prioritization missing**: No guidance on how to weigh competing values (revenue vs. user satisfaction vs. velocity)
- **Downside cases ignored**: Answers focus on what to do but not "what if this fails?"

**Improvements Needed**:
1. **Add "Risk/Value Framework"** in Answer Structure (after line 254):
   ```
   Risk/Value Assessment (SHOULD include for Intermediate/Advanced):
   - Value: Quantify expected benefit (revenue, engagement, retention, NPS)
   - Risk: Identify failure modes and likelihood
     * Technical risk (feasibility, scalability, technical debt)
     * Market risk (adoption, competition, timing)
     * Execution risk (coordination, dependencies, resource constraints)
   - Risk Mitigation: For high-risk choices (impact >$500K or 6+ month timeline), MUST include:
     * De-risking steps: "Prototype first, A/B test with 5% traffic, canary rollout"
     * Backup plans: "If adoption <20% after 2 weeks, pivot to alternative B"
     * Kill criteria: "Stop if cost exceeds $X or timeline exceeds Y weeks"
   ```
2. **Add "Value Prioritization" guidance** (new subsection in Section III):
   ```
   When answers involve multiple stakeholder values:
   MUST clarify prioritization logic using one of:
   - Quantitative: "Revenue impact ($2M) outweighs UX improvement (5% engagement)"
   - Strategic: "Long-term PMF justifies short-term churn (strategic positioning)"
   - Risk-adjusted: "Lower-risk option B chosen despite 20% lower value due to execution confidence"
   Avoid: Claiming "we can achieve all of X, Y, Z" without acknowledging trade-offs
   ```
3. **Add "Downside Planning"** requirement for Advanced questions:
   ```
   For Advanced (A) difficulty questions, answers SHOULD address:
   - Failure modes: "What are top 3 ways this could fail?"
   - Downside mitigation: "If failure occurs, how to minimize damage?"
   - Learning value: "What would we learn from failure to inform next decision?"
   ```
4. **Add "Risk/Value" validation** in Step 7:
   ```
   Review ≥3 Advanced answers for risk/value treatment:
   - Does answer quantify value (specific metrics/outcomes)?
   - Does answer identify risks (not just assume success)?
   - For high-stakes decisions (revenue >$1M, timeline >6mo), does answer include mitigation?
   PASS: 3/3 answers address risk/value; high-stakes decisions include mitigation
   ```

**Impact**: High | **Effort**: Medium | **Dependencies**: None

**Validation**: After edit, verify: risk/value framework added to Answer Structure; value prioritization guidance present; downside planning requirement for Advanced; risk/value validation in Step 7.

---

### Q7. Fairness

**Guideline**: Request balanced perspectives; acknowledge assumptions, limitations, biases, alternatives, counterarguments, trade-offs, and misconceptions.

**Present/Working**:
- **Lines 254**: Trade-Offs explicitly required: "what you're optimizing for vs. sacrificing"
- **Lines 232-238**: Judgment Signals include "Trade-off analysis", "Opportunity cost evaluation", "Stakeholder tension navigation" – multiple perspectives
- **Lines 55-60**: Multi-dimensional evaluation requires addressing ≥2 dimensions (Product, Business, Strategic, Operational) – balanced viewpoints
- **Lines 86-90**: Language diversity (EN/ZH/Other) provides cultural perspective balance

**Gaps/Weaknesses**:
- **No bias detection**: No guidance on avoiding common PM biases (recency bias, confirmation bias, sunk cost fallacy, optimism bias)
- **No alternative consideration**: Answer structure doesn't require discussing alternatives not chosen
- **No limitations acknowledgment**: Frameworks cited (RICE, JTBD) without discussing when they fail or mislead
- **Stakeholder fairness missing**: Answers may favor engineering perspective over sales, or vice versa, without balanced treatment
- **No demographic/accessibility consideration**: PM decisions impact diverse user populations; no guidance on inclusive thinking

**Improvements Needed**:
1. **Add "Bias Awareness"** in Answer Structure (new requirement):
   ```
   Answers SHOULD acknowledge common PM biases when relevant:
   - Optimism bias: "RICE confidence score prone to overestimation; discount by 20% for novel features"
   - Confirmation bias: "Data shows X, but alternative interpretation Y should be considered"
   - Sunk cost: "Prior investment in Z is irrelevant to go-forward decision"
   - Recency bias: "Recent customer complaints may not represent full user base; check historical data"
   HiPPO (Highest Paid Person's Opinion): "CEO wants X, but data suggests Y; present both with trade-offs"
   ```
2. **Add "Alternatives Consideration"** in Answer Structure (after line 254):
   ```
   Trade-offs SHOULD include alternatives not chosen:
   - Primary recommendation: Option A (with rationale)
   - Alternative B: Higher value but higher risk (explain why not chosen)
   - Alternative C: Lower effort but strategic misalignment (explain why not chosen)
   - Do nothing: Always consider status quo as alternative; quantify opportunity cost of inaction
   ```
3. **Add "Framework Limitations"** requirement (line 251):
   ```
   When citing frameworks [Ref: G#], MUST acknowledge limitations for Intermediate/Advanced:
   - RICE: "Doesn't capture strategic value; supplement with qualitative assessment"
   - JTBD: "Focuses on individual jobs; may miss ecosystem/network effects"
   - North Star Metric: "Single metric risks gaming; pair with guardrail metrics"
   ```
4. **Add "Inclusive Thinking"** guidance (new subsection):
   ```
   PM Decisions - Fairness & Inclusion:
   Answers involving user-facing features SHOULD consider:
   - Accessibility: "Feature should support screen readers, keyboard navigation (WCAG 2.1)"
   - Demographic diversity: "Survey users across age, geography, technical proficiency segments"
   - Edge cases: "Power users (10% of base) drive 40% of value; ensure solution works for both mainstream and power users"
   - Underserved users: "Solution may benefit majority but harm 5% segment; mitigation: X"
   ```
5. **Add "Fairness" validation** in Step 7:
   ```
   Review ≥5 answers for fairness/balance:
   - Does answer present ≥1 alternative not chosen (with rationale)?
   - Does answer acknowledge ≥1 limitation or bias?
   - For stakeholder conflict questions: Are ≥2 stakeholder perspectives fairly represented?
   - For user-facing features: Is accessibility/inclusion considered?
   PASS: 4/5 answers demonstrate balanced, fair treatment
   ```

**Impact**: High | **Effort**: Medium | **Dependencies**: None

**Validation**: After edit, verify: bias awareness added; alternatives consideration present; framework limitations required; inclusive thinking guidance present; fairness validation in Step 7.

---

## Format Guidelines

### FM1. Structure

**Guideline**: Use lists, tables, diagrams, formulas, code blocks.

**Present/Working**:
- **Lines 169-172, 211-217**: Self-Check sections use checkbox lists
- **Lines 708-717**: Topic Areas Overview uses Markdown table format
- **Lines 280-308**: Visual Artifacts section explicitly requires ≥1 diagram + ≥1 table per cluster
- **Lines 541-555**: Validation Report Template uses structured table with columns for Step, Check, Measurement, Pass Criteria, Result, Status
- **Lines 309-319**: Artifact examples include: matrices, journey maps, funnels, cohorts, dashboards, roadmaps

**Gaps/Weaknesses**:
- **Formula representation unclear**: RICE formula mentioned multiple times but never shown as `RICE = (Reach × Impact × Confidence) / Effort`
- **No diagram syntax specified**: "User journey map" required but no guidance on format (ASCII art, Mermaid, descriptive table)
- **Code blocks underused**: Template examples in Section VI could use code fences for clarity
- **Table formatting inconsistent**: Some tables use headers, some don't; no alignment guidance (left/right/center)

**Improvements Needed**:
1. **Add "Formula Notation"** in Section II.A (near line 64):
   ```
   When referencing prioritization formulas, use notation:
   - RICE: `RICE = (Reach × Impact × Confidence) / Effort`
   - ICE: `ICE = (Impact × Confidence × Ease)`
   - Value/Effort: `Priority = Value / Effort` (plotted on 2×2 matrix)
   ```
2. **Specify diagram formats** (line 280):
   ```
   Visual Artifacts - Format Options:
   - Tables: Use Markdown pipe-delimited tables (|---|---|) with headers and alignment
   - 2×2 Matrices: Use Markdown table or ASCII art with quadrant labels
   - Flowcharts/Journeys: Use Mermaid syntax in ```mermaid code blocks
   - Timelines: Use Markdown table with columns: Phase | Timeline | Milestones | Owner
   - Funnels: Use Markdown table with Stage | Metric | Baseline | Target | Change
   ```
3. **Use code fences consistently** in Section VI templates:
   ```
   Replace plain text template blocks with:
   ```markdown
   ## Template Name
   [template content]
   ```
   This improves readability and copy-pastability.
   ```
4. **Add table formatting standard**:
   ```
   Markdown Table Standards:
   - MUST include header row with column labels
   - SHOULD use alignment: left for text, right for numbers, center for status/tags
   - Format: | Left | Right | Center | → |:---|---:|:---:|
   - Keep column widths reasonable (<30 chars); wrap or abbreviate long text
   ```

**Impact**: Medium | **Effort**: Low | **Dependencies**: None

**Validation**: After edit, verify: formula notation present; diagram formats specified; code fences used in templates; table formatting standard added.

---

### FM2. Output Format

**Guideline**: Request structured format with TOC linking to sections.

**Present/Working**:
- **Lines 667-695**: Section VI "Output Format Template" provides comprehensive structure
- **Lines 676-695**: Table of Contents Template with anchor links demonstrated
- **Lines 697-722**: Topic Areas Overview table template provided
- **Lines 724-791**: Question & Answer Template with complete structure
- **Lines 820-954**: Reference Sections Template (4 subsections) fully specified

**Gaps/Weaknesses**:
- **TOC appears 3 times**: Lines 676 (template), 702 (embedded in overview), 729 (embedded in Q&A section) – redundant and confusing
- **No "output only" instruction**: LLM may include preamble, explanatory text, meta-commentary beyond required output
- **Anchor link format not specified**: GitHub-style (#lowercase-with-hyphens) vs other formats
- **No output boundary markers**: No clear "BEGIN OUTPUT" / "END OUTPUT" demarcation
- **Version/metadata missing**: No guidance on including generation date, prompt version, or validation status in output

**Improvements Needed**:
1. **Add "Output Discipline"** instruction at start of Section VI (before line 671):
   ```
   OUTPUT REQUIREMENTS - LLM MUST ADHERE:
   1. Produce ONLY the structured output per template below
   2. DO NOT include: preamble, instructions paraphrasing, explanations, apologies, meta-commentary, "Here is the output...", acknowledgments
   3. BEGIN output immediately with H1 title
   4. END output with Validation Report (Section E)
   5. Format: GitHub-Flavored Markdown with anchor links (#lowercase-with-hyphens)
   ```
2. **Consolidate TOC**: Remove redundant TOC templates; keep single comprehensive TOC at lines 676-695; remove lines 702, 729 TOC repetitions
3. **Add output header template** (insert before line 1 of generated output):
   ```
   ---
   Generated: [YYYY-MM-DD]
   Prompt Version: [1.0]
   Target Role: [Senior/Director/VP Product Manager]
   Q&A Count: [25-30]
   Validation Status: [ALL PASS]
   ---
   ```
4. **Add "Format Validation"** in Step 6:
   ```
   Validation Step 16 - Output Format:
   - Verify H1 title present at start (no preamble before H1)
   - Verify TOC with ≥20 anchor links (1 per section + Q&A)
   - Verify all anchor links functional (match heading slugs)
   - Verify no extraneous commentary outside template structure
   - Verify metadata header present with generation date, prompt version, validation status
   PASS: All format requirements met
   ```

**Impact**: High | **Effort**: Low | **Dependencies**: None

**Validation**: After edit, verify: output discipline instruction added; TOC consolidated; output header template present; format validation added as Step 16.

---

## Validation Guidelines

### V1. Evidence

**Guideline**: Cite credible sources; flag uncertainty.

**Present/Working**:
- **Lines 84-111**: Citation & Source Standards section specifies APA 7th edition with language tags, inline citation format [Ref: ID], reference ID taxonomy (G#, T#, L#, A#)
- **Lines 107-111**: Citation Coverage requires ≥70% answers contain ≥1 citation, ≥30% contain ≥2 citations, 100% framework mentions linked to [Ref: G#/A#]
- **Lines 439-444**: Validation Step 2 measures and enforces citation coverage thresholds
- **Lines 514-524**: Validation Step 11 (Framework Usage Accuracy) verifies frameworks cited correctly

**Gaps/Weaknesses**:
- **No uncertainty flagging**: Guidance doesn't require marking uncertain claims with qualifiers ("likely", "estimated", "based on limited data")
- **Citation quality not validated**: Step 2 counts citations but doesn't verify citations are relevant, recent, or credible
- **Self-citation allowed**: LLM could generate glossary entry G5, then cite [Ref: G5] without external source validation
- **No "citation needed" markers**: Quantitative claims may appear without [Ref: ID] tags and validation may miss them

**Improvements Needed**:
1. **Add "Uncertainty Flagging"** requirement in Answer Structure (line 256):
   ```
   Evidence & Uncertainty:
   - Factual claims MUST be cited with [Ref: ID] or labeled as assumptions
   - Uncertain estimates MUST use qualifiers:
     * "Based on limited data, estimated 30-50% adoption"
     * "Industry benchmarks suggest 10-15% churn [Ref: A5], though our segment may differ"
     * "Likely 3-6 month timeline, subject to technical discovery"
   - Avoid false precision: NOT "40.3% conversion" UNLESS directly cited
   ```
2. **Add "Citation Relevance Check"** in Step 2 validation (after line 444):
   ```
   Beyond count, verify citation quality for ≥5 random [Ref: ID] tags:
   - Does cited source directly support the claim?
   - Is citation recent enough (≥50% from last 3 years)?
   - Is cited source credible (authoritative per credibility criteria)?
   PASS: 5/5 citations relevant, recent, credible
   ```
3. **Prohibit "self-citation loops"** (add to Section II.C):
   ```
   Citation Integrity:
   - Glossary/Tool entries MAY cite other references but MUST ultimately trace to external APA sources
   - Answers citing [Ref: G#] MUST ensure G# entry cites [Ref: A#] external source
   - Circular references prohibited: G1 cites G2, G2 cites G1 with no external APA source
   ```
4. **Add "Citation Needed" review** in Step 7:
   ```
   Review ≥5 answers for uncited quantitative claims:
   - Extract all numbers, percentages, timeframes, metrics
   - Verify each has [Ref: ID] citation OR is labeled "hypothetical example" OR is derived from stated assumptions
   - Flag missing citations for addition
   ```

**Impact**: High | **Effort**: Medium | **Dependencies**: Requires citation quality check in validation

**Validation**: After edit, verify: uncertainty flagging requirement added; citation relevance check in Step 2; self-citation loops prohibited; citation needed review in Step 7.

---

### V2. Validation

**Guideline**: Request reasoning, self-review, error checks.

**Present/Working**:
- **Lines 422-562**: Section IV "Validation & Quality Gates" with 12-Point Checklist and Validation Report Template
- **Lines 169-172, 211-217, 267-275**: Self-Check sections after each major step (Topic Planning, Reference Collection, Q&A Generation)
- **Lines 389-418**: Step 7 "Final Review & Quality Assurance" with question design critique and answer quality review
- **Lines 114-143**: 6 Quality Gates (Recency, Source Diversity, Per-Topic Evidence, Tool Completeness, Link Validation, Cross-Reference Integrity) as mandatory stop points

**Gaps/Weaknesses**:
- **No reasoning documentation**: LLM performs validation checks but doesn't document reasoning (e.g., "Why did we choose source X over source Y?")
- **No error correction loop**: Validation identifies failures but doesn't specify correction process or re-validation
- **Self-review may be superficial**: Checkbox lists can be checked without deep review; no quality threshold for self-review
- **No independent verification**: All validation is self-performed; no external check mechanism

**Improvements Needed**:
1. **Add "Reasoning Documentation"** requirement in Validation (Section IV):
   ```
   For each validation step, LLM SHOULD document reasoning concisely:
   - Step 1 (Quantitative Floors): "G:12, T:6, L:7, A:15, Q:30 (6F/12I/12A = 20/40/40%) → PASS"
   - Step 4 (Recency): "15/15 citations (100%) from 2022-2024 → PASS threshold ≥50%"
   - Step 9 (Key Insight): "Sampled Q3, Q7, Q15, Q22, Q28 - all state specific tension/dilemma → 5/5 concrete → PASS"
   Include reasoning in Validation Report table "Result" column.
   ```
2. **Add "Error Correction Loop"** (new subsection after Section IV.B):
   ```
   If ANY validation step shows FAIL:
   1. STOP generation; DO NOT proceed to next section
   2. Identify root cause:
      - Missing references → Return to Step 2, add references, re-validate Steps 1-7
      - Low citation coverage → Return to Step 3, add [Ref: ID] tags, re-validate Step 2
      - Broken links → Fix URLs or replace sources, re-validate Step 6
   3. Document correction in Validation Report: "Step X initially FAIL (reason); corrected by (action); re-validated PASS"
   4. Re-run ALL 16 validation steps (not just failed step) to ensure no regressions
   5. Proceed only when ALL steps show PASS
   ```
3. **Strengthen self-review quality** in Step 7 (line 402):
   ```
   Answer Quality Review - MUST sample ≥5 answers (not just checkbox):
   For each sampled answer, score 1-5 on each criterion:
   - Multi-dimensional: Does it address ≥2 dimensions with specific details? (1=vague, 5=specific metrics/outcomes)
   - Concrete steps: Are steps actionable and sequenced? (1=generic, 5=detailed with dependencies)
   - Trade-offs: Are trade-offs explicitly named? (1=absent, 5=quantified with alternatives)
   - Citations: Do citations support claims? (1=missing, 5=relevant and credible)
   - Success criteria: Are metrics/outcomes specified? (1=absent, 5=measurable with thresholds)
   Average score MUST be ≥3.5/5 across all criteria to PASS.
   ```
4. **Add "Spot-Check Mechanism"** (optional external validation):
   ```
   For high-stakes usage, human reviewer SHOULD spot-check:
   - Randomly sample 3 Q&A: verify difficulty matches seniority, citations valid, no obvious errors
   - Check 5 random [Ref: ID] tags: verify they resolve to Reference Sections
   - Review Validation Report: verify measurements plausible (not just "PASS" without evidence)
   ```

**Impact**: High | **Effort**: High | **Dependencies**: Requires adding reasoning documentation throughout validation

**Validation**: After edit, verify: reasoning documentation requirement added; error correction loop present; self-review scoring added; spot-check mechanism documented.

---

### V3. Practicality

**Guideline**: Ensure actionable, implementable guidance.

**Present/Working**:
- **Lines 224-243**: Question Design Principles require "Realistic context: Include constraints (time, resources, stakeholder pressure, conflicting data)"
- **Lines 251-256**: Answer Structure requires "Concrete steps: What you'd do first, second, third (sequenced actions)"
- **Lines 632-636**: Realism criterion: "Scenario reflects actual senior+ PM dilemmas with stakeholder pressure, incomplete data, resource constraints"
- **Lines 977-1017**: Complete Example demonstrates practical application with specific steps and decision matrix

**Gaps/Weaknesses**:
- **Hypothetical examples may lack practicality**: Example Q&A (lines 977-1017) uses "40% of revenue", "$2M impact" – are these realistic numbers or illustrative?
- **No "implementability test"**: Validation checks format and citations but not whether recommendations are actually implementable
- **Missing contextual constraints**: Answers may suggest "hire data scientist" or "run 6-week experiment" without considering small team / resource-constrained contexts
- **No time/effort estimation**: Recommendations don't include implementation effort (engineering sprints, cross-functional coordination time)

**Improvements Needed**:
1. **Add "Practicality Criteria"** in Answer Structure (after line 256):
   ```
   Practicality & Implementability:
   - Recommendations MUST be implementable with typical PM resources:
     * Team size: 1 PM + 3-7 engineers + 1 designer (or state if requires larger team)
     * Timeline: Specify realistic timeline (days/weeks/months, not "as soon as possible")
     * Dependencies: Call out cross-functional dependencies (legal review, executive approval, vendor contract)
   - Avoid recommendations requiring unrealistic resources:
     * NOT: "Hire 10 data scientists" (unless context specifies large enterprise)
     * NOT: "Rebuild from scratch" (without acknowledging multi-year timeline and risk)
   - For resource-intensive recommendations, provide lightweight alternatives:
     * "Ideal: 6-week A/B test. Lightweight: 2-week prototype + qual interviews"
   ```
2. **Add "Implementation Effort"** guidance (new requirement in Answer Structure):
   ```
   For Intermediate/Advanced questions, answers SHOULD include effort estimate:
   - T-shirt sizing: Small (1-2 weeks, 1 team), Medium (4-8 weeks, 1-2 teams), Large (3+ months, 3+ teams)
   - Dependencies: "Requires legal review (2 weeks), executive approval (1 week), vendor integration (4 weeks)"
   - Sequencing: "Phase 1 (MVP, 4 weeks) → Learn → Phase 2 (scale, 8 weeks) OR pivot"
   ```
3. **Add "Practicality Check"** in Step 7 validation:
   ```
   Review ≥3 answers for practicality:
   - Are recommendations implementable with typical PM resources (1 PM, 3-7 eng, 1 designer)?
   - Do recommendations include realistic timelines (not "immediately" or vague "soon")?
   - For large efforts, are lightweight alternatives or phased approaches offered?
   PASS: 3/3 answers practical; no recommendations requiring obviously unrealistic resources
   ```
4. **Add practicality note to example** (line 977):
   ```
   [Add to example]: 
   Implementation Timeline: 
   - Discovery & RICE scoring: 2 weeks (PM + 1 eng for feasibility)
   - Decision socialization: 1 week (stakeholder reviews)
   - Execution: 6-8 weeks for generalized solution OR 2 weeks for premium tier offering
   ```

**Impact**: Medium | **Effort**: Medium | **Dependencies**: None

**Validation**: After edit, verify: practicality criteria added to Answer Structure; implementation effort guidance present; practicality check in Step 7; example includes timeline.

---

### V4. Success Criteria

**Guideline**: Define measurable, concrete outcomes.

**Present/Working**:
- **Lines 256**: Answer Structure requires "Success criteria: How you'd measure if the decision was right"
- **Lines 427-535**: 12 validation steps with precise Pass Criteria (e.g., "≥70% have ≥1 cite", "100% accessible or archived")
- **Lines 541-555**: Validation Report Template with Pass Criteria column for each validation step
- **Lines 563-601**: Submission Checklist with concrete acceptance criteria (all checkboxes must be checked)

**Gaps/Weaknesses**:
- **Success criteria in answers may be vague**: Requirement exists (line 256) but validation doesn't enforce it; answers could say "measure success by engagement" without specifying metric
- **No quantitative threshold**: Success criteria could be directional ("improve retention") vs. measurable ("retention >80% at D30")
- **No time horizon**: "Success criteria" doesn't specify when to measure (immediate, 30 days, 6 months)
- **Validation success criteria missing for some steps**: Steps 9-15 have Pass Criteria but some are subjective ("100% concrete insights" – what defines "concrete"?)

**Improvements Needed**:
1. **Strengthen "Success Criteria"** requirement (line 256):
   ```
   Success criteria MUST be measurable and time-bound:
   - NOT: "Improve user engagement"
   - YES: "User engagement (DAU/MAU) increases from 35% to 40%+ within 60 days of launch"
   - Include: (1) Specific metric, (2) Baseline or current state, (3) Target threshold, (4) Time horizon
   - For multi-phase rollouts: "Phase 1 success: >20% adoption in first 2 weeks → proceed to Phase 2"
   ```
2. **Add "Success Criteria Validation"** in Step 8 (Answer Word Count):
   ```
   Beyond word count, verify success criteria in ≥5 sampled answers:
   - Does each answer include ≥1 success criterion?
   - Is success criterion measurable (specific metric, not vague "improve X")?
   - Is success criterion time-bound (includes timeframe: days/weeks/months)?
   - Is success criterion realistic (thresholds achievable, not "10× growth in 1 week")?
   PASS: 5/5 answers have measurable, time-bound, realistic success criteria
   ```
3. **Clarify subjective Pass Criteria** in validation steps:
   ```
   Step 9 (Key Insight Quality): 
   - Current: "100% concrete"
   - Improved: "100% concrete (names specific: user impact/business trade-off/prioritization dilemma/stakeholder tension in 1 sentence)"
   
   Step 11 (Framework Usage):
   - Current: "≥80% correct"
   - Improved: "≥80% correct (framework description matches authoritative source + limitations acknowledged where relevant)"
   ```
4. **Add success criteria example** in Complete Example (line 977+):
   ```
   [Add after answer body]:
   Success Criteria:
   - Short-term (30 days): Enterprise customer retention ≥95% (vs. baseline 92%)
   - Medium-term (90 days): Mass-market feature adoption ≥25% of target segment (5K+ users)
   - Long-term (6 months): Revenue from mass-market ≥$500K (offsetting enterprise revenue risk)
   - Kill criterion: If mass-market adoption <10% after 60 days, revert to enterprise-focused offering
   ```

**Impact**: High | **Effort**: Medium | **Dependencies**: Requires adding success criteria validation to Step 8

**Validation**: After edit, verify: success criteria requirement strengthened; success criteria validation added to Step 8; subjective pass criteria clarified; example includes success criteria.

---

## Summary & Priority Matrix

### Compliance Summary

| Category | Guideline | Status | Gap Severity | Effort | Priority |
|----------|-----------|---------|--------------|--------|----------|
| **Foundation** | F1. Context | ⚠️ Partial | Medium | Low | **High** |
| | F2. Clarity | ⚠️ Partial | Low | Low | Medium |
| | F3. Precision | ⚠️ Partial | High | Medium | **High** |
| | F4. Relevance | ⚠️ Partial | Medium | Medium | Medium |
| **Scope** | S1. MECE | ⚠️ Partial | Medium | Medium | Medium |
| | S2. Sufficiency | ⚠️ Partial | High | Medium | **High** |
| | S3. Breadth | ⚠️ Partial | High | Medium | **High** |
| | S4. Depth | ⚠️ Partial | High | Medium | **High** |
| **Quality** | Q1. Significance | ⚠️ Partial | Medium | Low | Medium |
| | Q2. Concision | ❌ Weak | High | High | **High** |
| | Q3. Accuracy | ❌ Weak | High | Medium | **High** |
| | Q4. Credibility | ⚠️ Partial | High | Medium | **High** |
| | Q5. Logic | ⚠️ Partial | High | Medium | **High** |
| | Q6. Risk/Value | ❌ Weak | High | Medium | **High** |
| | Q7. Fairness | ❌ Weak | High | Medium | **High** |
| **Format** | FM1. Structure | ✅ Strong | Low | Low | Low |
| | FM2. Output Format | ⚠️ Partial | Medium | Low | Medium |
| **Validation** | V1. Evidence | ⚠️ Partial | High | Medium | **High** |
| | V2. Validation | ⚠️ Partial | High | High | **High** |
| | V3. Practicality | ⚠️ Partial | Medium | Medium | Medium |
| | V4. Success Criteria | ⚠️ Partial | High | Medium | **High** |

**Legend**: ✅ Strong (minor gaps) | ⚠️ Partial (moderate gaps) | ❌ Weak (major gaps)

### Priority Recommendations (Top 10)

1. **F3. Precision** - Add RFC 2119 modality (MUST/SHOULD/MAY) throughout; quantify subjective terms
2. **Q2. Concision** - Reduce document from 1017 lines to <750; consolidate redundant sections
3. **Q3. Accuracy** - Add source quality standards, accuracy verification step, hypothetical labeling
4. **Q4. Credibility** - Add source credibility criteria, reliability checks, credibility validation step
5. **Q5. Logic** - Add reasoning chain requirement, assumptions declaration, logical consistency validation
6. **Q6. Risk/Value** - Add risk/value framework, value prioritization, downside planning for Advanced Q&A
7. **Q7. Fairness** - Add bias awareness, alternatives consideration, framework limitations, inclusive thinking
8. **S2. Sufficiency** - Add role variants, sufficiency validation, scaling guidance, completeness check
9. **S3. Breadth** - Add industry diversity, stakeholder breadth ≥4 functions, perspective balance validation
10. **S4. Depth** - Strengthen multi-dimensional depth, add framework depth, second-order thinking requirement

### Implementation Roadmap

**Phase 1 - Quick Wins** (Low effort, High impact):
- F1: Add Audience, Assumptions, Inputs, Constraints sections
- F2: Add MECE definition, APA quick reference, terminology quick reference
- FM1: Add formula notation, specify diagram formats
- FM2: Add output discipline instruction, consolidate TOC

**Phase 2 - Core Quality** (Medium effort, High impact):
- F3: Add RFC 2119 notice, replace ambiguous verbs with MUST/SHOULD/MAY
- Q3: Add source quality standards, accuracy verification (Step 13)
- Q4: Add source credibility criteria, credibility validation (Step 14)
- V1: Add uncertainty flagging, citation relevance check
- V4: Strengthen success criteria requirement, add success criteria validation

**Phase 3 - Structural Improvements** (High effort, High impact):
- Q2: Consolidate validation sections, reduce document to <750 lines
- Q5: Add reasoning chain requirement, logical consistency validation (Step 15)
- Q6: Add risk/value framework to Answer Structure
- Q7: Add bias awareness, alternatives consideration, fairness validation
- V2: Add reasoning documentation, error correction loop

**Phase 4 - Comprehensive Coverage** (Medium effort, Medium-High impact):
- S2: Add role variants, sufficiency validation, scaling guidance
- S3: Add industry diversity, stakeholder breadth, perspective balance
- S4: Strengthen depth requirements across all answer components
- V3: Add practicality criteria, implementation effort, practicality check

---

**End of Analysis** | **Total Guidelines Evaluated**: 21/21 | **Next Step**: Proceed to change specification and implementation

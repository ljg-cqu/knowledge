# Product QA Prompt Optimization - Change Summary

**Based on**: [QA.guideline-analysis.md](./QA.guideline-analysis.md)  
**Target File**: [QA.md](./QA.md) (1017 lines → optimized)  
**Guidelines**: [../Guidelines_for_LLM-Friendly_Prompts.md](../Guidelines_for_LLM-Friendly_Prompts.md)

## Executive Summary

**21 Guidelines Evaluated**: Foundation (4), Scope (4), Quality (7), Format (2), Validation (4)

**Current Compliance**:
- ✅ Strong: 1/21 (FM1. Structure)
- ⚠️ Partial: 16/21 (adequate but improvable)
- ❌ Weak: 4/21 (major gaps: Q2 Concision, Q3 Accuracy, Q6 Risk/Value, Q7 Fairness)

**Optimization Strategy**:  
Phase 1 (Quick Wins) → Phase 2 (Core Quality) → Phase 3 (Structural) → Phase 4 (Comprehensive)

**Expected Outcomes**:
- Document reduction: 1017 lines → <800 lines (~20% reduction)
- Validation steps: 12 → 16 (adds Accuracy, Credibility, Logic, Format checks)
- Precision improvement: Add RFC 2119 modality throughout
- Quality enhancement: Risk/value, fairness, logic, accuracy safeguards added

---

## Change Specification by Section

### Section I. Context & Scope (Lines 9-35)

**Current State**: Purpose and scope defined; definitions provided; boundaries listed.

**Changes** (Guidelines: F1-Context, F2-Clarity, F3-Precision):

1. **Add Section I.A: Audience & Usage** [NEW] (F1)
   ```markdown
   ### A. Audience & Usage
   
   **Target Users**: Large language models (LLMs) with PM domain knowledge
   **Use Cases**: PM hiring managers, interview prep platforms, PM training programs
   **Required Capabilities**: Markdown generation, APA citation formatting, bilingual (EN/ZH)
   ```

2. **Add Section I.B: Assumptions** [NEW] (F1)
   ```markdown
   ### B. Assumptions
   
   - LLM has access to current PM literature (2021-2024)
   - Output format: GitHub-Flavored Markdown
   - Familiarity with PM frameworks (RICE, JTBD, AARRR, OST, HEART, etc.)
   - Bilingual capability: English (primary) + Chinese (secondary)
   - No specific company/industry context unless provided
   ```

3. **Add Section I.C: Inputs & Constraints** [NEW] (F1)
   ```markdown
   ### C. Inputs & Constraints
   
   **Optional Inputs** (if provided, tailor output accordingly):
   - Target seniority: Senior PM / Director / VP / C-level
   - Industry/domain: B2B SaaS, B2C Mobile, Platform, AI/ML, Healthcare, FinTech
   - Geography: Global, US, China, EU
   - Time constraints: Standard (30 Q&A) or Extended (40-50 Q&A)
   
   **Constraints**:
   - Output token budget: 10K-15K tokens (for 30 Q&A + references)
   - Generation time: 5-10 minutes recommended
   - Line length: <120 chars where feasible (AGENTS.md compliance)
   ```

4. **Add RFC 2119 Notice** [INSERT after line 8] (F3)
   ```markdown
   **Modality**: This document uses RFC 2119 semantics:
   - MUST/MUST NOT = mandatory requirement
   - SHOULD/SHOULD NOT = strong recommendation
   - MAY/CAN = optional

   ---
   ```

5. **Add MECE inline definition** (F2)
   - Line 47: Change `**Content Coverage (MECE - Mutually Exclusive, Collectively Exhaustive)**:`
   - No action needed; already present

6. **Add terminology quick reference box** [INSERT after line 20] (F2)
   ```markdown
   **Quick Reference** (most-used terms):
   - **MECE**: Mutually Exclusive, Collectively Exhaustive
   - **RICE**: Reach × Impact × Confidence / Effort
   - **JTBD**: Jobs-to-Be-Done framework
   - **APA**: American Psychological Association citation format
   - **PMF**: Product-Market Fit
   - **[Ref: ID]**: Inline citation tag (G#=Glossary, T#=Tool, L#=Literature, A#=APA source)
   ```

**Priority**: **HIGH** (Foundation improvements, low effort)

---

### Section II. Requirements & Specifications (Lines 37-143)

**Current State**: Quantitative requirements, reference floors, citation standards, 6 quality gates.

**Changes** (Guidelines: F3-Precision, F4-Relevance, S1-MECE, S2-Sufficiency, S3-Breadth, Q3-Accuracy, Q4-Credibility):

1. **Replace ambiguous verbs with MUST/SHOULD/MAY** throughout (F3)
   - Lines 39-60: Change "ensure", "include", "address" → MUST/SHOULD
   - Example: Line 41 `**Total count**: 25–30 Q&A pairs` → `**Total count**: MUST generate 25–30 Q&A pairs`
   - Apply systematically across all requirement statements

2. **Add rationale parentheticals** to quantitative floors (F2)
   - Line 42: `≥10 (ensures framework coverage for citation across 6 clusters)`
   - Line 64: `≥5 tools (minimum 1 per category; cited in practical examples)`
   - Line 67: `≥6 literature (≥2 ZH sources for cultural perspective; establishes authoritative foundation)`

3. **Add cluster boundary definitions** [INSERT after line 53] (S1)
   ```markdown
   **Cluster Definitions** (to ensure mutual exclusivity):
   1. **Strategy & Vision**: 12+ month horizon, market positioning, competitive moats, north star definition
   2. **Discovery & User Research**: User interviews, jobs-to-be-done, problem validation, insight synthesis
   3. **Prioritization & Roadmapping**: Feature ranking, RICE/ICE/KANO, roadmap communication, sequencing
   4. **Metrics & Analytics**: KPI definition, funnel analysis, experimentation, data interpretation
   5. **Stakeholder Management**: Cross-functional alignment, executive communication, conflict resolution
   6. **Go-to-Market & Growth**: 0-6 month tactics, launch execution, channel strategy, activation/retention

   **Edge Cases**:
   - Platform/API strategy → Strategy & Vision
   - Compliance/Legal → Stakeholder Management
   - Internationalization → Go-to-Market & Growth
   ```

4. **Add Role Variants guidance** [INSERT after line 34, in Section I] (S2)
   ```markdown
   ### D. Role Variants
   
   This prompt generates general Senior/Director/VP PM Q&A. For specialized roles:
   - **Technical PM**: Add cluster "Technical Depth & Architecture" with ≥3 Q&A on API design, system architecture, technical debt
   - **Growth PM**: Increase GTM & Growth cluster to 8-10 Q&A; reduce Strategy to 3-4 Q&A
   - **Platform PM**: Add ≥3 Q&A on developer experience, ecosystem growth, API monetization
   - **AI/ML PM**: Add cluster "Data & ML Product Management" with ≥3 Q&A on model evaluation, data pipelines, responsible AI
   ```

5. **Add Industry & Stakeholder Breadth requirements** [INSERT after line 53] (S3)
   ```markdown
   **Industry Diversity** (across all 30 Q&A):
   - SHOULD span ≥30% B2B SaaS/Enterprise, ≥30% B2C Consumer/Mobile, ≥20% Platform/Marketplace, ≥20% Emerging (AI/ML, Web3)
   - MUST avoid ≥60% concentration in single industry

   **Stakeholder Breadth** (across all 30 Q&A):
   - MUST include perspectives from ≥4 functions: Engineering, Design, Sales/GTM, Executive, Data, Operations

   **Perspective Balance** (validated in Step 6):
   - ≥30% answers prioritize user value/PMF
   - ≥30% answers prioritize business outcomes/revenue
   - ≥20% answers prioritize strategic positioning
   - ≥20% answers prioritize operational excellence
   ```

6. **Add Source Quality & Credibility Standards** [INSERT before line 67] (Q3, Q4)
   ```markdown
   ### Source Quality & Credibility Standards

   **Books/Literature**:
   - MUST: Established PM thought leaders (Cagan, Torres, Olsen, Perri, Patton) OR reputable publishers (O'Reilly, Wiley)
   - Chinese (ZH): MUST be recognized authorities (俞军/Baidu, 梁宁/Tencent, 苏杰/Alibaba) OR major PM platforms (人人都是产品经理)

   **Research**:
   - PREFER (descending): Peer-reviewed academic → Industry analysts (Gartner, Forrester) → PM research firms (ProductPlan, Pendo)

   **Case Studies**:
   - MUST: First-party (company blog, postmortem) OR reputable publication (HBR, TechCrunch, The Information)

   **Tools**:
   - MUST: ≥1K users OR notable customers (Fortune 500/unicorns) OR featured in reputable tool reviews
   - If <1K users: MUST justify with "Emerging tool with PM community traction" + cite source

   **Avoid**: Unverified blogs, promotional content, opinion without data, Wikipedia as primary source, paywalled sources without alternatives
   ```

7. **Reduce tool documentation fields** (Q1-Significance, F4-Relevance)
   - Remove: Pricing tier, Last update date (unless directly relevant to Q&A)
   - Keep: PM use case, user base/notable customers, URL, integrations (only if cited in answers)

**Priority**: **HIGH** (Core requirement clarity + quality standards)

---

### Section III. Step-by-Step Instructions (Lines 146-418)

**Current State**: 7 steps (Topic Planning → Reference Collection → Q&A Generation → Artifacts → Sections Population → Validation → Final Review)

**Changes** (Guidelines: F3-Precision, S4-Depth, Q5-Logic, Q6-Risk/Value, Q7-Fairness, V1-Evidence, V3-Practicality, V4-Success Criteria):

1. **Step 3 (Q&A Generation) - Strengthen Answer Structure** (Lines 246-262) (S4, Q5, Q6, Q7, V1, V4)
   
   **Add to line 251 (Framework/approach)**:
   ```markdown
   - **Framework Depth**: MUST explain application steps (not just name framework). For Advanced (A): MUST discuss when framework insufficient and what to supplement with. SHOULD acknowledge limitations ([Ref: G#] with "Limitations: X")
   ```

   **Add to line 252 (Multi-dimensional analysis)**:
   ```markdown
   - **Depth Requirement**: For EACH dimension (≥2 required):
     * Specific metric/outcome (NOT generic "improves revenue")
     * Quantitative estimate/range where possible ("$500K-2M impact", "15-25% adoption")
     * Time horizon (short <6mo, medium 6-18mo, long 18mo+)
   ```

   **Add after line 252 (new: Assumptions Declaration)** (Q5):
   ```markdown
   - **Assumptions**: When answer makes assumptions, MUST state explicitly:
     * Market: "Assuming competitive market (3+ alternatives)"
     * Users: "Assuming power users (DAU/MAU >40%)"
     * Resources: "Assuming 2-3 eng sprints (6-9 weeks)"
     * For Advanced (A): SHOULD discuss sensitivity ("If assumption X false, recommendation changes to Y")
   ```

   **Add after line 254 (new: Risk/Value Assessment)** (Q6):
   ```markdown
   - **Risk/Value** (SHOULD include for Intermediate/Advanced):
     * Value: Quantify benefit (revenue, engagement, retention, NPS)
     * Risk: Identify failure modes (technical, market, execution) + likelihood
     * Mitigation: For high-risk (>$500K or 6+ months), MUST include de-risking steps, backup plans, kill criteria
   ```

   **Add after line 254 (new: Alternatives Consideration)** (Q7):
   ```markdown
   - **Alternatives**: Trade-offs SHOULD include options not chosen:
     * Primary recommendation (with rationale)
     * Alternative B: Higher value but higher risk (why not chosen)
     * Alternative C: Lower effort but misaligned (why not chosen)
     * Status quo: Opportunity cost of inaction
   ```

   **Add after line 254 (new: Bias Awareness)** (Q7):
   ```markdown
   - **Bias Check**: SHOULD acknowledge common PM biases when relevant:
     * Optimism bias: "RICE confidence prone to overestimation; discount 20% for novel features"
     * Confirmation bias: "Data shows X, but alternative interpretation Y merits consideration"
     * Sunk cost: "Prior investment irrelevant to go-forward decision"
     * HiPPO: "CEO wants X; data suggests Y; present both with trade-offs"
   ```

   **Add after line 256 (new: Evidence & Uncertainty)** (V1):
   ```markdown
   - **Uncertainty Flagging**: Uncertain estimates MUST use qualifiers:
     * "Based on limited data, estimated 30-50% adoption"
     * "Industry benchmarks suggest 10-15% churn [Ref: A5], though segment may differ"
     * Avoid false precision: NOT "40.3%" UNLESS cited
   ```

   **Strengthen line 256 (Success Criteria)** (V4):
   ```markdown
   - **Success Criteria** (MUST be measurable + time-bound):
     * NOT: "Improve engagement"
     * YES: "Engagement (DAU/MAU) increases 35%→40%+ within 60 days of launch"
     * Include: (1) Specific metric, (2) Baseline, (3) Target threshold, (4) Time horizon
     * For multi-phase: "Phase 1 success: >20% adoption in 2 weeks → proceed to Phase 2"
   ```

   **Add after line 256 (new: Practicality & Implementability)** (V3):
   ```markdown
   - **Practicality**: Recommendations MUST be implementable with typical PM resources:
     * Team: 1 PM + 3-7 engineers + 1 designer (or state if larger team required)
     * Timeline: Specify realistic (days/weeks/months, NOT "ASAP")
     * Dependencies: Call out cross-functional (legal review, exec approval, vendor)
     * For resource-intensive: Provide lightweight alternatives ("Ideal: 6wk A/B test. Lightweight: 2wk prototype + qual")
     * For Intermediate/Advanced: SHOULD include effort estimate (Small 1-2wks, Medium 4-8wks, Large 3+mos)
   ```

2. **Add "Reasoning Chain" requirement** [INSERT before line 251] (Q5):
   ```markdown
   **Reasoning Chain Requirement**: Concrete steps MUST show traceable logic:
   - NOT: "First, use RICE. Second, present to stakeholders."
   - YES: "First, gather RICE inputs (Reach: 5K users, Impact: 8/10, Confidence: 70%, Effort: 4 weeks). Second, calculate (5K×8×0.7/4 = 7K). Third, compare to alternatives [scores]. Fourth, present top-ranked with rationale."
   - Each step MUST follow from previous step or stated assumption.
   ```

3. **Add "Second-Order Thinking" requirement** [INSERT in Step 3] (S4):
   ```markdown
   **Second-Order Thinking** (for Intermediate/Advanced):
   - Downstream consequences: "What happens after we make this decision?"
   - Failure modes: "What are the ways this could go wrong?"
   - Hidden costs: "What are second-order resource/velocity impacts?"
   - Reversibility: "How easy to undo later?"
   ```

4. **Add "Inclusive Thinking" guidance** [NEW subsection in Step 3] (Q7):
   ```markdown
   ### PM Decisions - Fairness & Inclusion

   For user-facing features, answers SHOULD consider:
   - Accessibility: "Support screen readers, keyboard navigation (WCAG 2.1)"
   - Demographic diversity: "Survey across age, geography, technical proficiency"
   - Edge cases: "Power users (10% of base, 40% of value); ensure solution works for mainstream + power"
   - Underserved: "Solution may benefit majority but harm 5% segment; mitigation: X"
   ```

**Priority**: **HIGH** (Answer quality improvements, critical for PM judgment)

---

### Section IV. Validation & Quality Gates (Lines 422-601)

**Current State**: 6 Quality Gates, 12 Validation Steps, Validation Report Template, Submission Checklist

**Changes** (Guidelines: Q2-Concision, Q3-Accuracy, Q4-Credibility, Q5-Logic, V1-Evidence, V2-Validation, V4-Success Criteria, FM2-Output Format):

1. **Consolidate Quality Gates into Validation Steps** (Q2-Concision)
   - Merge Section II.D (Quality Gates, lines 112-143) into Section IV.A (12-Point Checklist)
   - Update Step 6 reference: "Execute comprehensive validation per Section IV.A (16 steps)"
   - **Result**: Reduce redundancy; validation appears in 1 place instead of 3

2. **Add new validation steps** (Q3, Q4, Q5, FM2):

   **Validation Step 13 - Accuracy Check** [NEW] (Q3):
   ```markdown
   **Step 13 – Accuracy Check**:
   - **Measurement**:
     * Extract all quantitative claims (percentages, counts, timeframes, dollar amounts)
     * Verify each claim either: (a) cited with [Ref: ID], (b) labeled "hypothetical example", (c) derived from stated assumptions
     * Check 5 random citations: verify [Ref: ID] resolves to relevant source in References
     * Check for internal contradictions (Q15 recommends X, Q22 recommends opposite without acknowledging trade-off)
   - **Pass Criteria**: 100% quantitative claims cited/labeled; 5/5 citations valid; 0 contradictions
   - **Fail Action**: Add [Ref: ID] tags to uncited claims OR label as hypothetical; fix contradictions; replace invalid citations
   ```

   **Validation Step 14 - Source Credibility** [NEW] (Q4):
   ```markdown
   **Step 14 – Source Credibility**:
   - **Measurement**:
     * Count Literature sources (L#) matching credibility criteria (established authors OR reputable publishers)
     * Count Research sources (A#) that are peer-reviewed OR industry analyst reports
     * Count Tools (T#) with ≥1K users OR notable customers
     * Calculate percentages
   - **Pass Criteria**: ≥80% Literature credible; ≥80% Research credible; 100% Tools meet threshold
   - **Fail Action**: Replace low-credibility sources with authoritative alternatives
   ```

   **Validation Step 15 - Logical Consistency** [NEW] (Q5):
   ```markdown
   **Step 15 – Logical Consistency**:
   - **Measurement**:
     * Sample 5 random answers
     * Check for internal contradictions within answer (circular reasoning, unsupported leaps)
     * Check for cross-answer contradictions (Q5 recommends A, Q18 recommends not-A without acknowledging trade-off)
     * Verify reasoning chains: each conclusion follows from stated premises or assumptions
   - **Pass Criteria**: 0 contradictions; 5/5 answers have traceable reasoning
   - **Fail Action**: Rewrite contradictory sections; add missing reasoning steps; add assumption declarations where implicit
   ```

   **Validation Step 16 - Output Format** [NEW] (FM2):
   ```markdown
   **Step 16 – Output Format**:
   - **Measurement**:
     * Verify H1 title present at start (no preamble before H1)
     * Verify TOC with ≥20 anchor links (1 per major section + Q&A)
     * Test 5 random anchor links: verify functional (match heading slugs)
     * Verify no extraneous commentary outside template structure (no "Here is...", apologies, meta-discussion)
     * Verify metadata header present (generation date, prompt version, validation status)
   - **Pass Criteria**: All format requirements met
   - **Fail Action**: Remove preamble; fix broken anchor links; add metadata header; remove extraneous text
   ```

3. **Add reasoning documentation requirement** (V2-Validation)
   - Update Validation Report Template (line 541+): Add "Reasoning" column after "Measurement"
   - Example: `Step 1: G:12, T:6, L:7, A:15, Q:30 (6F/12I/12A=20/40/40%) → PASS`

4. **Add Error Correction Loop** [NEW subsection after Section IV.B] (V2):
   ```markdown
   ### D. Error Correction Loop

   If ANY validation step shows FAIL:
   1. **STOP** generation; DO NOT proceed to next section
   2. **Identify root cause**:
      - Missing references → Return to Step 2, add references, re-validate Steps 1-7
      - Low citation coverage → Return to Step 3, add [Ref: ID] tags, re-validate Step 2
      - Broken links → Fix URLs or replace sources, re-validate Step 6
      - Logical contradictions → Rewrite affected answers, re-validate Step 15
   3. **Document correction** in Validation Report: "Step X initially FAIL (reason); corrected by (action); re-validated PASS"
   4. **Re-run ALL 16 steps** (not just failed step) to ensure no regressions
   5. **Proceed only when ALL steps PASS**
   ```

5. **Strengthen self-review scoring** in Step 7 (line 402) (V2):
   ```markdown
   **Answer Quality Review** - MUST sample ≥5 answers (score 1-5 each criterion):
   - Multi-dimensional: ≥2 dimensions with specific details? (1=vague, 5=metrics/outcomes)
   - Concrete steps: Actionable and sequenced? (1=generic, 5=detailed with dependencies)
   - Trade-offs: Explicitly named? (1=absent, 5=quantified with alternatives)
   - Citations: Support claims? (1=missing, 5=relevant and credible)
   - Success criteria: Measurable? (1=absent, 5=metric+baseline+target+timeframe)
   **Average MUST be ≥3.5/5 to PASS**
   ```

6. **Add citation quality checks** (V1-Evidence):
   - Step 2 (Citation Coverage): Add "Verify 5 random [Ref: ID] tags: relevant, recent, credible"
   - Step 7 (Final Review): Add "Extract all numbers/percentages; verify [Ref: ID] OR labeled hypothetical"

**Priority**: **HIGH** (Validation completeness, catches errors before output)

---

### Section VI. Output Format Template (Lines 667-976)

**Current State**: 310 lines with TOC template, Topic Overview, Q&A template, Reference templates, Validation Report template, complete example (40 lines)

**Changes** (Guidelines: Q2-Concision, FM2-Output Format):

1. **Add Output Discipline instruction** [INSERT before line 671] (FM2):
   ```markdown
   ## OUTPUT REQUIREMENTS - LLM MUST ADHERE

   1. Produce ONLY structured output per template below
   2. DO NOT include: preamble, instruction paraphrasing, explanations, apologies, meta-commentary, "Here is...", acknowledgments
   3. BEGIN output immediately with metadata header + H1 title
   4. END output with Validation Report (Section E)
   5. Format: GitHub-Flavored Markdown with anchor links (#lowercase-with-hyphens)
   6. Line length: <120 chars where feasible
   ```

2. **Add metadata header template** [INSERT at line 671, before TOC] (FM2):
   ```markdown
   ---
   Generated: [YYYY-MM-DD]
   Prompt Version: 1.1
   Target Role: [Senior/Director/VP Product Manager]
   Q&A Count: [25-30]
   Validation Status: [ALL PASS / PARTIAL (see report)]
   ---
   ```

3. **Consolidate TOC templates** (Q2-Concision, FM2):
   - Keep comprehensive TOC at lines 676-695
   - **Remove** redundant partial TOCs at lines 702 (embedded in Overview), 729 (embedded in Q&A section)
   - **Result**: Single source of truth for TOC structure

4. **Condense Complete Example** (lines 977-1017) (Q2-Concision):
   - Current: 40 lines for 1 Q&A example
   - Target: 25 lines (remove verbose decision matrix, keep key components)
   - **Alternative**: Move complete example to separate `QA.example.md` file; keep minimal example in main prompt

5. **Deduplicate APA format examples** (Q1-Significance, Q2-Concision):
   - Keep detailed APA format in Section II.C (lines 98-111)
   - Subsequent mentions: Reference "See Section II.C for APA 7th format"
   - Remove redundant APA examples at lines 355, 923, 929

6. **Add formula notation** [INSERT in Section II.A, near line 64] (FM1-Structure):
   ```markdown
   **Formula Notation** (when referencing prioritization):
   - RICE: `RICE = (Reach × Impact × Confidence) / Effort`
   - ICE: `ICE = (Impact × Confidence × Ease)`
   - Value/Effort: `Priority = Value / Effort` (plotted on 2×2 matrix)
   ```

7. **Add table formatting standard** [INSERT in Section VI or Step 4] (FM1-Structure):
   ```markdown
   **Markdown Table Standards**:
   - MUST include header row with column labels
   - SHOULD use alignment: left for text (`:---`), right for numbers (`---:`), center for status/tags (`:---:`)
   - Example: `| Feature | Impact | Priority |` → `|:---|---:|:---:|`
   - Keep column widths <30 chars; wrap or abbreviate long text
   ```

**Priority**: **HIGH** (Output quality + concision; reduces document by ~100 lines)

---

## Summary of Major Changes

| Category | Changes | Lines Added | Lines Removed | Net Change |
|----------|---------|-------------|---------------|------------|
| Section I (Context) | +4 subsections (Audience, Assumptions, Inputs, RFC 2119 notice, Quick Ref) | +80 | 0 | +80 |
| Section II (Requirements) | +5 subsections (Cluster defs, Role variants, Industry/Stakeholder breadth, Source credibility, Formula notation) | +120 | -20 (tool fields) | +100 |
| Section III (Steps) | +8 requirements in Answer Structure (depth, logic, risk/value, fairness, evidence, practicality, success criteria) | +150 | 0 | +150 |
| Section IV (Validation) | +4 new steps (13-16); +Error Correction Loop; strengthen self-review | +100 | -50 (consolidate gates) | +50 |
| Section VI (Output) | +Output discipline, metadata header, formula/table standards | +40 | -150 (dedupe TOC, APA, condense example) | -110 |
| **Total** | **26 major additions + consolidations** | **+490** | **-220** | **+270** |

**Revised Document Size**: 1017 + 270 = **~1287 lines** (before condensation passes)

**After Concision Pass** (Phase 3): Target **<900 lines** through:
- Tighter language (remove redundant explanations)
- Merge overlapping validation checks
- Move detailed examples to appendix

---

## Implementation Phases (Recommended Order)

### Phase 1 - Foundation & Quick Wins (30 min)
**Goal**: Add missing context, clarify terminology, establish precision

- [ ] Add Section I subsections: Audience, Assumptions, Inputs, RFC 2119 notice (F1, F3)
- [ ] Add terminology quick reference box (F2)
- [ ] Add MECE cluster definitions (S1)
- [ ] Add formula notation (FM1)
- [ ] Add output discipline instruction (FM2)
- [ ] Add metadata header template (FM2)

**Validation**: Verify all additions present; no breaking changes to existing content.

### Phase 2 - Core Quality Standards (1 hour)
**Goal**: Establish source quality, add critical validations

- [ ] Replace ambiguous verbs with MUST/SHOULD/MAY throughout (F3)
- [ ] Add Source Quality & Credibility Standards (Q3, Q4)
- [ ] Add Role Variants guidance (S2)
- [ ] Add Industry & Stakeholder Breadth requirements (S3)
- [ ] Add Validation Steps 13-16 (Accuracy, Credibility, Logic, Format) (Q3-Q5, FM2)
- [ ] Add citation quality checks to Step 2, Step 7 (V1)

**Validation**: Run sample validation on 3 test Q&A; verify new steps catch errors.

### Phase 3 - Answer Structure Enhancements (1 hour)
**Goal**: Deepen answer quality with risk/value, logic, fairness

- [ ] Add Framework Depth requirement (S4)
- [ ] Add Multi-dimensional Depth requirement (S4)
- [ ] Add Assumptions Declaration (Q5)
- [ ] Add Reasoning Chain requirement (Q5)
- [ ] Add Risk/Value Assessment (Q6)
- [ ] Add Alternatives Consideration (Q7)
- [ ] Add Bias Awareness (Q7)
- [ ] Add Uncertainty Flagging (V1)
- [ ] Strengthen Success Criteria (V4)
- [ ] Add Practicality & Implementability (V3)
- [ ] Add Second-Order Thinking (S4)
- [ ] Add Inclusive Thinking guidance (Q7)

**Validation**: Sample 5 answers; verify each component present with adequate depth.

### Phase 4 - Consolidation & Concision (45 min)
**Goal**: Reduce redundancy, streamline document

- [ ] Consolidate Quality Gates into Validation Steps (Q2)
- [ ] Consolidate TOC templates (remove redundant at lines 702, 729) (Q2, FM2)
- [ ] Deduplicate APA format examples (Q2)
- [ ] Condense Complete Example from 40→25 lines OR move to separate file (Q2)
- [ ] Add Error Correction Loop (V2)
- [ ] Strengthen self-review scoring (V2)
- [ ] Add reasoning documentation to Validation Report (V2)
- [ ] Reduce tool documentation fields (Q1, F4)

**Validation**: Verify document <900 lines; all anchors functional; no content regressions.

---

## Validation Checklist (Post-Implementation)

**Structural Integrity**:
- [ ] All 21 guidelines addressed with concrete improvements
- [ ] H1 title present; matches document purpose
- [ ] TOC present with working anchor links to all H2/H3 sections
- [ ] Section numbering consistent (I, II, III, IV, V, VI)
- [ ] All internal cross-references valid

**Content Completeness**:
- [ ] Section I includes: Purpose, Definitions, Scope Boundaries, Audience, Assumptions, Inputs, RFC 2119 notice
- [ ] Section II includes: Q&A Composition, Reference Floors, Citation Standards, Source Credibility, Cluster Definitions, Industry/Stakeholder Breadth
- [ ] Section III Answer Structure includes: Framework Depth, Multi-dimensional Depth, Assumptions, Reasoning Chain, Risk/Value, Alternatives, Bias, Uncertainty, Success Criteria, Practicality
- [ ] Section IV includes: 16 Validation Steps (1-12 original + 13 Accuracy + 14 Credibility + 15 Logic + 16 Format), Error Correction Loop, Self-Review Scoring
- [ ] Section VI includes: Output Discipline, Metadata Header, consolidated TOC, condensed examples

**Quality Checks**:
- [ ] ≥80% of requirement statements use MUST/SHOULD/MAY (F3-Precision)
- [ ] All quantitative floors include rationale parentheticals (F2-Clarity)
- [ ] All frameworks show formula notation where applicable (FM1-Structure)
- [ ] No redundant TOCs, APA examples, or validation sections (Q2-Concision)
- [ ] Document size <900 lines after Phase 4 (Q2-Concision)

**Backwards Compatibility**:
- [ ] All original section headings preserved (anchors stable)
- [ ] All original quantitative requirements preserved (≥10 glossary, ≥5 tools, etc.)
- [ ] All original validation steps 1-12 preserved (new steps additive)
- [ ] All original templates preserved (TOC, Q&A, References, Validation Report)
- [ ] No breaking changes to output format structure

**AGENTS.md Compliance**:
- [ ] GitHub-Flavored Markdown throughout
- [ ] Lines <120 chars where feasible
- [ ] Fenced code blocks with language tags
- [ ] Relative links for internal references
- [ ] No trailing whitespace

**Guideline Coverage**:
- [ ] F1-F4 (Foundation): Context, Clarity, Precision, Relevance → All addressed
- [ ] S1-S4 (Scope): MECE, Sufficiency, Breadth, Depth → All addressed
- [ ] Q1-Q7 (Quality): Significance, Concision, Accuracy, Credibility, Logic, Risk/Value, Fairness → All addressed
- [ ] FM1-FM2 (Format): Structure, Output Format → All addressed
- [ ] V1-V4 (Validation): Evidence, Validation, Practicality, Success Criteria → All addressed

---

## Rollback Plan

If critical regressions detected:

1. **Restore from backup**: `cp Prompts/Product/QA.md.bak Prompts/Product/QA.md`
2. **Identify regression**: Use `diff` to compare original vs. edited
3. **Targeted fix**: Apply only non-breaking changes from this change summary
4. **Re-validate**: Run validation checklist above
5. **Document issue**: Add to `QA.change-summary.md` "Known Issues" section

**Backup file**: `Prompts/Product/QA.md.bak` (created at start, 1017 lines, original state)

---

**End of Change Summary** | **26 Major Enhancements** | **21/21 Guidelines Addressed** | **Next**: Implement Phase 1 (Foundation)

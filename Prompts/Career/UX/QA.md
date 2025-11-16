# UX Interview Q&A Generator (Minimal Viable)

Generate 6-12 decision-critical Q&As for informed UX decisions with limited time. Focus: blocks decision or creates material risk.

## Table of Contents
1. [Requirements](#requirements)
2. [Execution](#execution)
3. [Output Format](#output-format)
4. [Reference Examples](#reference-examples)

## Requirements

**Target**: Senior UX designers (5+ years), leads, principals via judgment-based scenarios.

**Assumptions**: Digital products (web/mobile/SaaS); foundational UX knowledge; 10-15min/question.

**Terms**:
- **Judgment Question**: Trade-off analysis ("How would you..." vs "What is...")
- **Design Artifact**: Production-ready spec (dimensions/states/interactions)
- **Floor**: Minimum threshold (≥)
- **Quality Gate**: Fail = stop, fix, re-validate all

**Scope**: Multi-platform, accessibility, systems, research | **Exclude**: Junior concepts, single-platform, pure theory | **Limitation**: Generic scenarios lack domain nuance

### Floors (Minimal Viable - 60% Reduction)

| Component | Requirements |
|-----------|-------------|
| **Q&As** | 6-12 \| 25% F / 50% I / 25% A \| 120-200 words \| ≥70% ≥1 cite \| 100% decision-critical |
| **Dimensions** | 3-4 decision-critical only: Design Systems (≥2) \| Accessibility (≥1) \| Research/IA (≥1) \| Interaction (≥1) |
| **References** | G≥8 \| T≥4 \| L≥5 \| A≥6 APA 7th [EN]/[ZH] |
| **Artifacts** | ≥1 diagram + ≥1 table per Q&A (compressed) |

**Legend**: F=Foundational, I=Intermediate, A=Advanced | G=Glossary, T=Tool, L=Literature, A=Citation

### Decision-Critical Dimensions (3-4 Only)

1. **Design Systems** (≥2 Q&As): Governance, token management, multi-platform consistency, adoption strategy
   - **Blocks Decision**: System fragmentation, design-dev misalignment, scaling bottleneck
   - **Creates Risk**: Inconsistent UX, maintenance debt, team velocity ↓

2. **Accessibility & Compliance** (≥1 Q&A): WCAG compliance, audit readiness, inclusive design
   - **Blocks Decision**: Compliance strategy, legal/regulatory risk mitigation
   - **Creates Risk**: Accessibility lawsuit, regulatory breach, user exclusion

3. **Research & IA** (≥1 Q&A): User research strategy, information architecture, findability
   - **Blocks Decision**: Product pivot, navigation restructure, research investment
   - **Creates Risk**: User research gap, findability failure, scope creep

4. **Interaction & Feedback** (≥1 Q&A): State management, error handling, feedback loops
   - **Blocks Decision**: Interaction pattern standardization, error recovery strategy
   - **Creates Risk**: Inconsistent UX, user confusion, support burden

### Citations

**Format**: APA 7th + `[EN/ZH/Other]` | Inline: `[Ref: ID]`

**Distribution**: EN 60±10% \| ZH 30±10% \| Other 10±5% | **Types** (≥3): Research, tools, frameworks, cases

### Gates (fail ANY = stop, fix, re-validate ALL)

| # | Criteria | Mitigation |
|---|----------|------------|
| 1 | ≥50% from 3yrs (≥70% digital) | Flag caveats |
| 2 | ≥3 types; max 25%/type | Expand |
| 3 | Each dimension ≥2 authoritative+≥1 tool | Add sources |
| 4 | Tools: pricing, update≤18mo, ≥3 integrations | - |
| 5 | 100% URLs accessible/archived | Archive/replace |
| 6 | 100% [Ref:ID] resolve | Fix refs |

## Execution (Streamlined)

### Step 1: Allocate (Decision-Critical Only)

Distribute 6-12 across 3-4 decision-critical dimensions (25/50/25% F/I/A).

**Example** (9): Design Systems (3): 1F/1I/1A | Accessibility (2): 0F/1I/1A | Research/IA (2): 1F/1I/0A | Interaction (2): 0F/1I/1A = **2F/4I/3A**

**Decision Criticality Check**: Every Q&A must satisfy ≥1 criterion:
- Blocks Decision (architecture, strategy, compliance)
- Creates Risk (legal, user experience, team velocity)
- Affects ≥2 Stakeholders (Designer + Engineer, Designer + PM, etc.)
- Requires Action (1-6mo timeline)

### Step 2: Build References (Minimal Viable - 60% Reduction)

**Glossary (≥8)**: Design Tokens, Atomic Design, WCAG, ARIA, Design System, Accessibility, Usability, Information Architecture
- **Format**: `G#. Term [Lang] | Definition | Use: [Cases]`

**Tools (≥4)**: Figma (Design), Axe DevTools (Accessibility), Storybook (System docs), Hotjar (Research)
- **Format**: `T#. Tool (Category) [Lang] | Desc | Use | URL`

**Literature (≥5)**: EN—Norman, Krug, Cooper, Gothelf | ZH—刘津/李月
- **Format**: `L#. Author, Title, Year [Lang] | Relevance`

**Citations (≥6)**: APA 7th + tags | ≥50% from 3yrs | Decision-critical only

### Step 3: Generate Q&As (Decision-Critical Only)

**Question Format**: "How/When/Compare..." + decision context + constraints | **Avoid**: "What is...", "Define..."

**Decision-Critical Examples**:
- **F**: "Design token naming: flat vs. hierarchical? Multi-platform consistency impact?"
- **I**: "Design system adoption at 40% (target: 70%). Governance vs. flexibility trade-off?"
- **A**: "10 teams, 5 products, inconsistent patterns. System governance strategy without blocking velocity?"

**Answer** (120-200 words): Context → Decision Criticality → Trade-offs (table: ≥2 alternatives) → Metrics (quantified) → Stakeholder Impact → Limitations

**Self-Check**: ✓ Decision-Critical (≥1 criterion) | ✓ 120-200w | ✓ Artifact | ✓ Quantified | ✓ ≥1 cite | ✓ Complexity matches

### Step 4: Artifacts (Compressed - 1 Diagram + 1 Table per Q&A)

**Diagrams** (Mermaid <80 nodes): Design System governance flow | Accessibility audit checklist | Research decision tree | Interaction state machine

**Trade-offs Table** (per Q&A):
| Approach | Pros | Cons | Use When | Consensus |
|----------|------|------|----------|-----------|
| Option A | +% | -% | Scenario | Recommendation |
| Option B | +% | -% | Scenario | Recommendation |

**Metrics** (Decision-Critical Only):
| Dimension | Metric | Formula | Target |
|-----------|--------|---------|--------|
| Design Systems | Adoption | `Using/Total Teams×100%` | >70% 6mo |
| Accessibility | WCAG Compliance | `Passed/Total×100%` | 100% AA |
| Research | Findability | `Found≤3 clicks/Total×100%` | >80% |
| Interaction | Task Success | `Completed/Attempted×100%` | >90% |

### Step 5: Populate References

**Formats**:
- **G**: `G#. Term [Lang] | Def | Related | Use` (alphabetize)
- **T**: `T#. Tool (Category) [Lang] | Desc | Price | Updated Q# YYYY | Integrations (≥3) | Use | URL` (group by category)
- **L**: `L#. Author, Title, Year [Lang] | Summary | Relevance` (EN, then ZH)
- **A**: `A#. [APA 7th] [Lang]` (Books: `Author, A. (Year). *Title*. Publisher.` | Articles: `Author, A. (Year). Title. *Journal*, Vol(Issue), pages. DOI` | Web: `Author. (Year). *Title*. Site. URL`)

**Check**: ✓ 100% [Ref:ID] resolve | ✓ No orphans | ✓ Complete | ✓ [Lang] tags

### Step 6: Validate (Streamlined - 12 Checks)

| # | Criteria | Target |
|---|----------|--------|
| 1 | Floors | G≥8, T≥4, L≥5, A≥6, Q=6-12, 25/50/25% |
| 2 | Decision Criticality | 100% satisfy ≥1 criterion (Blocks/Risk/Stakeholders/Action) |
| 3 | Citations | ≥70% ≥1 cite; decision-critical only |
| 4 | Recency | ≥50% from 3yrs (≥70% digital) |
| 5 | Links | 100% accessible/archived |
| 6 | Cross-Refs | 100% resolve |
| 7 | Words | Sample 5; 100% in 120-200 |
| 8 | Quantified | 100% have metrics/% |
| 9 | Artifacts | ≥90% have ≥1 diagram + ≥1 table |
| 10 | Dimensions | 3-4 decision-critical covered; ≥2 Design Systems |
| 11 | Stakeholders | ≥3 core roles represented (Designer, Engineer, PM) |
| 12 | Final Review | Clarity | Accuracy | Completeness | Actionability | No redundancy |

**Submit**: ✓ 12/12 | ✓ Floors | ✓ No placeholders | ✓ Decision-critical justified

## Output Format (Minimal Viable)

### A. TOC

1. Requirements | 2. Execution (Steps 1-6) | 3. Q&As (3.1 Design Systems | 3.2 Accessibility | 3.3 Research/IA | 3.4 Interaction) | 4. References (4.1 Glossary | 4.2 Tools | 4.3 Literature | 4.4 Citations) | 5. Validation

### B. Overview

**Total**: 6-12 | **Difficulty**: 2F (25%) / 4I (50%) / 3A (25%)

| # | Dimension | Q Range | Mix | Artifacts |
|---|-----------|---------|-----|-----------|
| 1 | Design Systems | Q1-3 | 1F/1I/1A | diagram+table |
| 2 | Accessibility | Q4-5 | 0F/1I/1A | diagram+table |
| 3 | Research/IA | Q6-7 | 1F/1I/0A | diagram+table |
| 4 | Interaction | Q8-9 | 0F/1I/1A | diagram+table |
| | **Total** | **6-9** | **2F/4I/3A** | **8 min** |

**Usage**: All Q&As decision-critical; use for informed decisions on UX strategy, system governance, accessibility compliance

### C. Q&A Template (Minimal Viable)

**Q#: [How/When/Compare + decision context]** | **Difficulty**: [F/I/A] | **Decision Criticality**: [Blocks/Risk/Stakeholders/Action]

**Answer** (120-200 words): Context → Decision Criticality → Trade-offs (table) → Metrics (quantified) → Stakeholder Impact → Limitations

**Trade-offs Table**:
| Approach | Pros | Cons | Use When | Consensus |
|----------|------|------|----------|-----------|
| Option A | +% | -% | Scenario | Recommendation |
| Option B | +% | -% | Scenario | Recommendation |

**Diagram**: Mermaid <80 nodes (governance flow, audit checklist, decision tree, or state machine)

**Metrics**: | Metric | Formula | Target |

**Stakeholders**: Designer, Engineer, PM (≥2 roles affected)

---

### D. Reference Formats

**G**: `G#. Term [Lang] | Def | Related | Use` (alphabetize)  
**T**: `T#. Tool (Category) [Lang] | Desc | Price | Updated Q# YYYY | Integrations (≥3) | Use | URL` (group)  
**L**: `L#. Author, Title, Year [Lang] | Summary | Relevance` (EN, ZH)  
**A**: `A#. [APA 7th] [Lang]`

## Reference Examples (Minimal Viable)

### Glossary (≥8)
**G1. Design Tokens** [EN] | Centralized design values (color/spacing/typography) for multi-platform consistency | **Use**: Design Systems  
**G2. Atomic Design** [EN] | Component hierarchy (atoms→molecules→organisms) for system architecture | **Use**: Design Systems  
**G3. WCAG** [EN] | Accessibility guidelines; POUR principles (Perceivable, Operable, Understandable, Robust) | **Use**: Compliance  
**G4. ARIA** [EN] | Accessible Rich Internet Applications; semantic markup for screen readers | **Use**: Accessibility  
**G5. Design System** [EN] | Centralized library of components, patterns, tokens, and governance | **Use**: Multi-platform consistency  
**G6. Accessibility** [EN] | Inclusive design ensuring usability for all users, including those with disabilities | **Use**: Compliance, legal  
**G7. Usability** [EN] | Effectiveness, efficiency, satisfaction in achieving user goals | **Use**: Research, testing  
**G8. Information Architecture** [EN] | Structural design of information environments for findability | **Use**: Navigation, taxonomy

### Tools (≥4)
**T1. Figma** [EN] | Collaborative design for UI/UX, components, prototypes | **Updated**: Q4 2024 | **Use**: Interface design | **URL**: https://figma.com  
**T2. Axe DevTools** [EN] | WCAG testing; browser extension, CLI | **Updated**: Q4 2024 | **Use**: Accessibility audits | **URL**: https://deque.com/axe  
**T3. Storybook** [EN] | Component docs, isolated dev environment | **Updated**: Q4 2024 | **Use**: System docs | **URL**: https://storybook.js.org  
**T4. Hotjar** [EN] | Behavior analytics: heatmaps, recordings, surveys | **Updated**: Q3 2024 | **Use**: Research, analytics | **URL**: https://hotjar.com

### Literature (≥5)
**L1. Norman, D. (2013). *Design of Everyday Things*. Basic Books.** [EN] | Affordances, signifiers, mental models | **Relevance**: Core UX principles  
**L2. Krug, S. (2014). *Don't Make Me Think*. New Riders.** [EN] | Navigation, clarity, testing | **Relevance**: Applied web usability  
**L3. Cooper, A., et al. (2014). *About Face*. Wiley.** [EN] | Goal-directed design, personas, patterns | **Relevance**: Interaction framework  
**L4. Gothelf, J., & Seiden, J. (2021). *Lean UX*. O'Reilly.** [EN] | Collaborative, hypothesis-driven, MVP | **Relevance**: Agile UX  
**L5. 刘津, & 李月. (2017). *用户体验要素*. 机械工业出版社.** [ZH] | UX fundamentals, user research, design thinking | **Relevance**: Applied UX methodology

### Citations (≥6, APA 7th, Decision-Critical Only)
**A1.** Norman, D. (2013). *The design of everyday things*. Basic Books. [EN]  
**A2.** Krug, S. (2014). *Don't make me think*. New Riders. [EN]  
**A3.** Cooper, A., et al. (2014). *About face*. Wiley. [EN]  
**A4.** Gothelf, J., & Seiden, J. (2021). *Lean UX*. O'Reilly. [EN]  
**A5.** 刘津, & 李月. (2017). *用户体验要素*. 机械工业出版社. [ZH]  
**A6.** Frost, B. (2016). *Atomic design*. Brad Frost. [EN]

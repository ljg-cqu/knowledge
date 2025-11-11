# Cloze / Fill-in-the-Blank — Business Understanding for Software Architecture

Generate comprehensive cloze assessments mapping business concepts to architectural implications, with rigorous quality standards and evidence-based rationales.

---

# Part I: Specifications

## Context & Scope

### Purpose
Create assessment instruments for senior technical leaders, solution architects, and expert practitioners to evaluate their ability to translate business requirements into architectural decisions.

### Scope & Constraints
- **Target Audience**: Senior/architect/expert technical leaders with 5+ years experience
- **Assessment Goal**: 24–40 items testing business-to-architecture understanding across 5 core topic clusters
- **Output Format**: Markdown with structured TOC, inline citations, and complete reference sections
- **Exclusions**: Basic programming concepts, pure technical implementations without business context
- **Assumptions**: Readers have foundational knowledge of both business strategy and software architecture

## Structure & Difficulty

### Format Requirements
- **Blank Format**: Unambiguous blanks using `___` notation; single clear answer per blank
- **Acceptance Arrays**: Each item includes comprehensive list of acceptable answers (synonyms, abbreviations, variants)
- **Normalization Rules**: 
  - Case-insensitive matching
  - Whitespace trimming (leading/trailing)
  - Punctuation stripping (periods, commas, hyphens)
  - Numeric tolerances specified explicitly (e.g., ±5% for percentages)

### Difficulty Distribution (MECE)
- **Foundational (20%)**: Industry-standard terminology, widely-adopted frameworks (e.g., Business Model Canvas, Conway's Law)
- **Intermediate (40%)**: Framework application, pattern recognition, multi-component relationships
- **Advanced (40%)**: Strategic trade-off analysis, context-specific adaptations, emerging practices
- **MECE Verification**: Non-overlapping difficulty tiers; each item classified to exactly one tier; complete coverage of topic clusters

## Grading & Normalization

### Answer Validation
- **Primary Answers**: Canonical terminology from authoritative sources
- **Acceptable Variants**: Regional differences (US/UK English), historical terminology, common abbreviations
- **Borderline Cases**: Document with rationale; include if used by ≥2 authoritative sources within 5 years
- **Partial Credit**: Not applicable for cloze format (binary correct/incorrect)

### Conflict Resolution
- **Terminology Conflicts**: Include all variants from recognized schools of thought (e.g., "Bounded Context" vs "Context Boundary")
- **Regional Variations**: Accept both British and American English spellings
- **Version Differences**: Specify framework version when terminology changed significantly (e.g., "TOGAF 9.2" vs "TOGAF 10")

## Citation Standards

### Source Composition
- **Language Distribution**: ~60% English (EN), ~30% Chinese (ZH), ~10% other languages
- **Source Types**: Business frameworks, architecture patterns, case studies, practitioner tools, academic research
- **Citation Format**: APA 7th edition with language tags [EN], [ZH], [DE], etc.
- **Inline References**: [Ref: ID] format in rationales; use G# (glossary), T# (tools), L# (literature), A# (APA citations)

### Quality & Credibility
- **Authoritative Sources**: Peer-reviewed publications, recognized industry frameworks (TOGAF, ArchiMate), established practitioners (Martin Fowler, Eric Evans)
- **Uncertainty Handling**: Flag uncertain claims with "[Note: Limited sources]" or "[Emerging practice]"
- **Source Verification**: All links must be accessible or archived (Wayback Machine, archive.org)

## Reference Minimum Requirements

| Reference Section | Minimum Count | Quality Criteria | Examples |
|---|---|---|---|
| Glossary, Terminology & Acronyms | ≥10 | Industry-standard definitions; authoritative sources | BMC, Value Proposition, DDD, Conway's Law, Technical Debt |
| Business & Architecture Tools | ≥5 | Widely-adopted (10K+ users); actively maintained | Miro, ArchiMate, C4, Confluence, LucidChart, Wardley Maps |
| Authoritative Literature & Reports | ≥6 | Peer-reviewed or practitioner-recognized | Business strategy, architecture patterns, organizational design |
| APA Style Source Citations | ≥12 | Language mix: ~60% EN, ~30% ZH, ~10% other | Books, journal articles, conference papers, technical reports |

## Quality Gates

### Recency Requirements
- **Standard Topics**: ≥50% of citations published ≤3 years from current date
- **Rapidly Evolving Topics**: ≥70% recency for digital transformation, cloud-native, AI/ML architecture, microservices patterns
- **Classic Works**: Foundational texts (e.g., Domain-Driven Design 2003, Design Patterns 1994) exempt from recency requirements

### Source Diversity
- **Type Diversity**: ≥3 source types (books, journals, practitioner blogs, tools, frameworks)
- **Single Source Limit**: No single source accounts for >25% of total citations
- **Geographic Diversity**: Include sources from ≥3 regions (North America, Europe, Asia)

### Coverage & Mapping
- **Citation Coverage**: ≥70% of items have ≥1 citation; ≥30% have ≥2 citations
- **Business-Architecture Mapping**: ≥70% of items test explicit business-to-architecture terminology translation
- **MECE Compliance**: Zero overlap between topic clusters; all major business-architecture domains covered

## Success Criteria

### Quantitative Metrics
- **Item Count**: 24–40 items total
- **Difficulty Distribution**: 20% foundational, 40% intermediate, 40% advanced (±5% tolerance)
- **Reference Minimums**: All thresholds met (≥10 glossary, ≥5 tools, ≥6 literature, ≥12 APA)

### Qualitative Metrics
- **Quality Gates**: All gates satisfied (recency, diversity, coverage, mapping, MECE)
- **Reference Resolution**: All [Ref: ID] references resolve to valid entries (G#/T#/L#/A#)
- **Link Accessibility**: 100% of external links accessible or archived
- **Answer Completeness**: Every item has comprehensive acceptance list with ≥1 primary answer and documented variants
- **Blank Clarity**: Zero ambiguous blanks; each blank has single, verifiable correct answer set

---

# Part II: Instructions

## Step 1: Topic Identification & Planning

### Objective
Define comprehensive, non-overlapping topic clusters that provide complete coverage of business-to-architecture mapping domains.

### Process
1. **Select Topic Clusters** (4–6 clusters from the following):
   - **Strategic Modeling**: Business model analysis, value proposition mapping, capability modeling
   - **Value & Risk Analysis**: Cost-benefit analysis, technical debt assessment, risk mitigation strategies
   - **Organizational Dynamics**: Team topologies, Conway's Law applications, organizational alignment
   - **Architectural Translation**: Business requirements to technical decisions, quality attribute mapping
   - **Evolution & Adaptation**: Digital transformation, legacy modernization, architectural evolution

2. **Allocate Items Per Cluster**:
   - Total: 24–40 items across all clusters
   - Per cluster: 4–8 items (adjust based on cluster count)
   - Distribution example (6 clusters, 30 items): 5+5+5+5+5+5
   - Distribution example (4 clusters, 32 items): 8+8+8+8

3. **Apply Difficulty Distribution** (per cluster):
   - Foundational (20%): 1–2 items per cluster
   - Intermediate (40%): 2–3 items per cluster
   - Advanced (40%): 2–3 items per cluster

4. **Verify MECE Compliance**:
   - **Mutually Exclusive**: No item could reasonably belong to multiple clusters
   - **Collectively Exhaustive**: All major business-architecture mapping domains covered
   - **Test Method**: Review each item; confirm single cluster assignment; identify coverage gaps

### Success Criteria
- [ ] 4–6 distinct topic clusters selected
- [ ] Clear cluster definitions (scope, exclusions, key concepts)
- [ ] Item allocation plan totaling 24–40 items
- [ ] Difficulty distribution meets 20/40/40 target (±5%)
- [ ] MECE verification completed; no overlaps or gaps identified

---

## Step 2: Reference Collection

### Objective
Gather authoritative, diverse, recent sources that support item rationales and answer validation.

### Process
1. **Collect Glossary Entries** (≥10):
   - Focus: Business-architecture terminology, frameworks, patterns, laws
   - Sources: Industry standards (ISO, IEEE), authoritative frameworks (TOGAF, ArchiMate), seminal works (DDD, Team Topologies)
   - Format: Term, definition, architectural implications, language tag
   - Example: "Business Model Canvas (BMC): 9-block template mapping business models to technical requirements [EN]"

2. **Identify Tools** (≥5):
   - Criteria: Widely adopted (≥10K users), actively maintained, supports business-architecture workflows
   - Categories: Modeling tools, diagramming platforms, documentation systems, strategic planning tools
   - Information: Name, purpose, adoption metrics, URL, language tag
   - Example: "Miro: Visual collaboration for Business Model Canvas; 80M+ users; https://miro.com [EN]"

3. **Gather Literature Sources** (≥6):
   - Types: Books, journal articles, conference papers, technical reports, case studies
   - Focus: Business strategy, architecture patterns, organizational design, domain modeling
   - Recency: ≥50% published within 3 years (≥70% for rapidly evolving topics)
   - Diversity: ≥3 source types, ≥3 geographic regions

4. **Compile APA Citations** (≥12):
   - Format: APA 7th edition with language tags
   - Distribution: ~60% EN, ~30% ZH, ~10% other
   - Coverage: Support ≥70% of items with ≥1 citation; ≥30% with ≥2 citations
   - Verification: All DOIs/URLs accessible or archived

### Tagging Requirements
For each reference, include:
- **Language Tag**: [EN], [ZH], [DE], etc.
- **Year**: Publication year (for recency verification)
- **Type**: Book, Journal, Conference, Tool, Framework, Blog, Report

### Success Criteria
- [ ] ≥10 glossary entries collected
- [ ] ≥5 tools identified with adoption metrics and URLs
- [ ] ≥6 literature sources gathered
- [ ] ≥12 APA citations compiled
- [ ] Language distribution: EN 50–70%, ZH 20–40%, Other 5–15%
- [ ] Recency requirements met (≥50% ≤3 years)
- [ ] Source diversity achieved (≥3 types, single source ≤25%)

---

## Step 3: Item Generation

### Objective
Create clear, unambiguous cloze items that test business-to-architecture terminology mapping.

### Process
1. **Draft Items** (cluster by cluster):
   - **Identify Key Concept**: Select specific business-architecture mapping (e.g., "BMC Revenue Streams → multi-tenancy")
   - **Write Statement**: Craft sentence with single clear blank targeting precise terminology
   - **Ensure Clarity**: Blank must have unambiguous answer; context sufficient for expert to determine answer
   - **Example**: "When a company shifts from perpetual licensing to SaaS, the ___ building block changing from upfront to recurring directly drives multi-tenancy requirements."

2. **Build Acceptance Lists**:
   - **Primary Answer**: Canonical term from authoritative source (e.g., "Revenue Streams")
   - **Acceptable Variants**: Synonyms, abbreviations, regional spellings (e.g., "Revenue Stream", "Revenue")
   - **Borderline Cases**: Document with rationale; include if ≥2 authoritative sources use within 5 years
   - **Excluded Terms**: List common incorrect answers with explanation (optional, for test design reference)

3. **Write Rationales**:
   - **Structure**: [Concept explanation] + [Architectural implication] + [Reference citations]
   - **Citations**: Include ≥1 [Ref: ID] per item; use ≥2 for complex/contested concepts
   - **Evidence**: Link concept to specific architectural decision or pattern
   - **Example**: "Recurring subscription revenue drives cost optimization [Ref: G12], requiring multi-tenancy for shared infrastructure efficiency [Ref: A7]."

4. **Incremental Review** (every 5 items):
   - **Ambiguity Check**: Can blank be filled with multiple valid but different answers? If yes, revise.
   - **Acceptance Completeness**: Are all reasonable variants included? Check against multiple sources.
   - **Citation Adequacy**: Does every item have ≥1 [Ref: ID]? Are references appropriate?
   - **Difficulty Verification**: Does item match assigned difficulty tier? Compare with exemplars.

### Quality Checklist (per item)
- [ ] Blank is unambiguous (single clear answer set)
- [ ] Context provides sufficient information for expert to determine answer
- [ ] Acceptance list includes primary answer + documented variants
- [ ] Rationale includes ≥1 [Ref: ID] citation
- [ ] Difficulty tier assigned and verified
- [ ] Item tests business-to-architecture terminology mapping

### Success Criteria
- [ ] 24–40 items generated across all clusters
- [ ] All items have complete acceptance lists
- [ ] All items have rationales with ≥1 citation
- [ ] Difficulty distribution: 20/40/40 (±5%)
- [ ] ≥70% of items test business-architecture mapping
- [ ] Zero ambiguous blanks identified in review

---

## Step 4: Reference Compilation

### Objective
Populate all reference sections with complete, well-formatted entries; verify all inline citations resolve correctly.

### Process
1. **Populate Glossary Section**:
   - Format: **ID. Term**: Definition with architectural implications. [Language Tag]
   - Order: Alphabetical by term or by reference ID (G1, G2, ...)
   - Completeness: All G# references used in items must have entries

2. **Populate Tools Section**:
   - Format: **ID. Tool Name**: Purpose/description. Adoption metrics. URL [Language Tag]
   - Order: By reference ID (T1, T2, ...) or by category
   - Verification: All URLs accessible; include Wayback Machine links for unstable URLs

3. **Populate Literature Section**:
   - Format: **ID. Author(s). (Year). *Title*. Publisher.** Key contribution/focus.
   - Order: By reference ID (L1, L2, ...) or chronological
   - Completeness: All L# references used in items must have entries

4. **Populate APA Citations Section**:
   - Format: **ID. [APA 7th format citation]. [Language Tag]**
   - Order: By reference ID (A1, A2, ...) or alphabetical by author
   - Verification: All DOIs/URLs checked; archived if unstable

5. **Cross-Reference Verification**:
   - Extract all [Ref: ID] from item rationales
   - Confirm each ID exists in appropriate section (G#→Glossary, T#→Tools, L#→Literature, A#→APA)
   - Fix broken references (add missing entries or correct IDs)

### Success Criteria
- [ ] All reference sections populated (Glossary ≥10, Tools ≥5, Literature ≥6, APA ≥12)
- [ ] All entries follow specified format
- [ ] All inline [Ref: ID] citations resolve to valid entries
- [ ] All URLs accessible or archived
- [ ] Language tags present on all entries

---

## Step 5: Self-Review & Validation

### Objective
Systematically verify all specifications, quality gates, and success criteria are met before delivering output.

### Validation Checklist

#### 1. Quantitative Requirements
- [ ] **Glossary Count**: ≥10 entries
- [ ] **Tools Count**: ≥5 entries
- [ ] **Literature Count**: ≥6 entries
- [ ] **APA Citations Count**: ≥12 entries
- [ ] **Item Count**: 24–40 items total
- [ ] **Difficulty Distribution**: 20% foundational, 40% intermediate, 40% advanced (±5% tolerance)

#### 2. Citation Quality
- [ ] **Citation Coverage**: ≥70% of items have ≥1 citation; ≥30% have ≥2 citations
- [ ] **Language Mix**: EN 50–70%, ZH 20–40%, Other 5–15%
- [ ] **Recency**: ≥50% of citations ≤3 years old (≥70% for digital transformation/cloud-native topics)
- [ ] **Source Diversity**: ≥3 source types represented; no single source >25% of total

#### 3. Link & Reference Integrity
- [ ] **Link Accessibility**: All URLs accessible or archived (Wayback Machine, archive.org)
- [ ] **Cross-Reference Resolution**: All [Ref: ID] resolve to valid entries (G#/T#/L#/A#)
- [ ] **Reference Completeness**: No orphaned references (entries without inline usage) or missing references (inline citations without entries)

#### 4. Item Quality
- [ ] **Answer Completeness**: Every item has comprehensive acceptance list (primary + variants)
- [ ] **Blank Clarity**: Zero ambiguous blanks; each blank has single verifiable answer set
- [ ] **Rationale Quality**: All rationales explain business-architecture connection + include ≥1 citation

#### 5. Coverage & Mapping
- [ ] **Business-Architecture Mapping**: ≥70% of items test explicit business-to-architecture terminology translation
- [ ] **MECE Compliance**: Zero overlap between topic clusters; all major domains covered
- [ ] **Topic Distribution**: Items distributed across 4–6 clusters; each cluster has 4–8 items

### Error Correction Process
For each failed check:
1. **Identify Root Cause**: Missing content, incorrect calculation, format error, or logic flaw?
2. **Plan Correction**: Add missing items, revise content, or restructure sections?
3. **Implement Fix**: Make targeted corrections
4. **Re-Validate**: Re-run affected checklist items
5. **Document**: Note corrections made (for learning/improvement)

### Success Criteria
- [ ] All 5 validation categories pass (100% of checklist items satisfied)
- [ ] All quality gates met (recency, diversity, coverage, mapping, MECE)
- [ ] Zero unresolved errors or warnings
- [ ] Output ready for delivery

---

# Part III: Output Format

Start the output with a TOC (e.g., '## Contents') linking to all top-level headings and list items.

- Use lists tables diagrams formulas code blocks; diagrams in Mermaid; code with language-tagged fences.

```markdown
## Table of Contents

### [Item Bank](#item-bank-items-1n)
- [Topic 1: Strategic Modeling](#topic-1-strategic-modeling)
- [Topic 2: Value & Risk Analysis](#topic-2-value--risk-analysis)
- [Topic 3: Organizational Dynamics](#topic-3-organizational-dynamics)
- [Topic 4: Architectural Translation](#topic-4-architectural-translation)
- [Topic 5: Evolution & Adaptation](#topic-5-evolution--adaptation)
- [Topic 6: [Custom Topic]](#topic-6-custom-topic) *(if applicable)*

### [Reference Sections](#reference-sections)
- [Glossary, Terminology & Acronyms](#glossary-terminology--acronyms)
- [Business & Architecture Tools](#business--architecture-tools)
- [Authoritative Literature & Case Studies](#authoritative-literature--case-studies)
- [APA Style Source Citations](#apa-style-source-citations)

### [Validation Summary](#validation-summary)
- [Quantitative Metrics](#quantitative-metrics)
- [Quality Gates](#quality-gates-verification)

---

## Item Bank (Items 1–N)

### Topic 1: Strategic Modeling

#### Item 1: The ___ framework uses 9 building blocks to map business models to technical requirements.

**Difficulty:** Foundational

**Acceptable Answers:**
- Business Model Canvas
- BMC
- Business Model Canvas (BMC)

**Rationale:** Business Model Canvas [Ref: G1] provides structured analysis of business model changes and architectural implications [Ref: A1].

---

#### Item 2: When a company shifts from perpetual licensing to SaaS, the ___ building block changing from upfront to recurring directly drives multi-tenancy requirements.

**Difficulty:** Intermediate

**Acceptable Answers:**
- Revenue Streams
- Revenue Stream
- Revenue

**Rationale:** Recurring subscription revenue drives cost optimization [Ref: G1], requiring multi-tenancy for shared infrastructure efficiency [Ref: A7].

---

## Reference Sections

### Glossary, Terminology & Acronyms

**G1. [Term/Acronym]**: [Definition with architectural implications]. [Language Tag]

**G2. [Next term]**: [Definition]. [Language Tag]

*[Continue for all ≥10 glossary entries]*

---

### Business & Architecture Tools

**T1. [Tool Name]**: [Purpose/description]. [Adoption metrics]. [URL] [Language Tag]

**T2. [Next tool]**: [Details]. [URL] [Language Tag]

*[Continue for all ≥5 tools]*

---

### Authoritative Literature & Case Studies

**L1. [Author(s)]. ([Year]). *[Title]*. [Publisher].** [Key contribution/focus area].

**L2. [Next reference]**: [Details].

*[Continue for all ≥6 literature sources]*

---

### APA Style Source Citations

**A1. [Author(s)]. ([Year]). *[Title]*. [Publisher/Journal]. [DOI/URL] [Language Tag]**

**A2. [Next citation]. [Language Tag]**

*[Continue for all ≥12 APA citations]*

---

## Validation Summary

### Quantitative Metrics

| Metric | Target | Actual | Status |
|---|---|---|---|
| Total Items | 24–40 | [N] | ✅/❌ |
| Foundational (20%) | [N items] | [N] | ✅/❌ |
| Intermediate (40%) | [N items] | [N] | ✅/❌ |
| Advanced (40%) | [N items] | [N] | ✅/❌ |
| Glossary Entries | ≥10 | [N] | ✅/❌ |
| Tools | ≥5 | [N] | ✅/❌ |
| Literature Sources | ≥6 | [N] | ✅/❌ |
| APA Citations | ≥12 | [N] | ✅/❌ |

### Quality Gates Verification

| Quality Gate | Target | Actual | Status |
|---|---|---|---|
| Citation Coverage (≥1) | ≥70% | [%] | ✅/❌ |
| Citation Coverage (≥2) | ≥30% | [%] | ✅/❌ |
| Language Mix (EN) | 50–70% | [%] | ✅/❌ |
| Language Mix (ZH) | 20–40% | [%] | ✅/❌ |
| Language Mix (Other) | 5–15% | [%] | ✅/❌ |
| Recency (≤3 years) | ≥50% | [%] | ✅/❌ |
| Source Diversity | ≥3 types | [N types] | ✅/❌ |
| Single Source Limit | ≤25% | [%] | ✅/❌ |
| Business-Arch Mapping | ≥70% | [%] | ✅/❌ |
| Link Accessibility | 100% | [%] | ✅/❌ |
| Reference Resolution | 100% | [%] | ✅/❌ |
| MECE Compliance | Pass | Pass/Fail | ✅/❌ |

**Notes:**
- [Any deviations from targets with rationale]
- [Borderline cases or judgment calls made]
- [Recommendations for future iterations]

---

## Example Items (For Reference)

### Example 1: Foundational Difficulty

#### Item: The ___ framework uses 9 building blocks to map business models to technical requirements.

**Difficulty:** Foundational

**Acceptable Answers:**
- Business Model Canvas
- BMC
- Business Model Canvas (BMC)
- Osterwalder Business Model Canvas

**Rationale:** Business Model Canvas [Ref: G1] provides structured analysis of business model changes and their architectural implications through 9 core building blocks (Customer Segments, Value Propositions, Channels, Customer Relationships, Revenue Streams, Key Resources, Key Activities, Key Partnerships, Cost Structure) [Ref: A1]. This framework enables architects to systematically trace business decisions to technical requirements.

---

### Example 2: Intermediate Difficulty

#### Item: When a company shifts from perpetual licensing to SaaS, the ___ building block changing from upfront to recurring directly drives multi-tenancy architecture requirements.

**Difficulty:** Intermediate

**Acceptable Answers:**
- Revenue Streams
- Revenue Stream
- Revenue
- Revenue model

**Rationale:** The Revenue Streams building block [Ref: G12] defines how a company generates income. Shifting from upfront perpetual fees to recurring subscription revenue creates cost pressure to maximize infrastructure efficiency [Ref: G1]. This economic constraint drives the architectural decision to implement multi-tenancy, allowing multiple customers to share underlying infrastructure while maintaining data isolation [Ref: A7]. The business model change thus directly mandates specific architectural patterns.

---

### Example 3: Advanced Difficulty

#### Item: According to Conway's Law, when an organization restructures from functional silos to cross-functional product teams, the resulting architecture tends to shift from ___ to microservices.

**Difficulty:** Advanced

**Acceptable Answers:**
- monolithic architecture
- monolith
- monolithic system
- layered monolith
- modular monolith

**Rationale:** Conway's Law [Ref: G4] states that "organizations design systems that mirror their communication structures" [Ref: A5]. Functional silos (e.g., separate UI, business logic, database teams) naturally produce layered monolithic architectures where each team owns a horizontal layer [Ref: L4]. Cross-functional product teams, where each team owns a complete vertical slice of functionality, align with microservices architecture where each service represents an independent product capability [Ref: A6]. This demonstrates how organizational restructuring predictably drives architectural evolution, requiring architects to anticipate and plan for such transitions [Ref: L5].

**Note:** "Modular monolith" is accepted as a transitional architecture that often emerges during this organizational shift, though pure microservices is the canonical answer.

---

## Best Practices

### Item Writing
1. **Precision**: Use exact terminology from authoritative sources; avoid ambiguous synonyms in the statement itself
2. **Context Sufficiency**: Provide enough context for experts to determine answer without guessing; avoid trick questions
3. **Single Focus**: Each blank tests one specific concept; avoid compound blanks requiring multiple related answers
4. **Natural Language**: Write items as complete, grammatically correct sentences; blanks should integrate smoothly

### Acceptance Lists
1. **Comprehensiveness**: Include all variants found in ≥2 authoritative sources from past 5 years
2. **Documentation**: Note why borderline terms are included/excluded (for test maintenance)
3. **User Testing**: Consider how diverse expert populations might phrase the answer (regional, generational, domain differences)

### Rationale Quality
1. **Explanation Depth**: Sufficient for learners to understand the concept, not just verify the answer
2. **Architectural Link**: Explicitly state the business-to-architecture connection
3. **Evidence**: Cite specific sources; avoid unsupported assertions
4. **Clarity**: Write for international audience; define jargon on first use

### Reference Management
1. **ID Consistency**: Use consistent ID schemes (G1-G15, T1-T10, L1-L10, A1-A20)
2. **Alphabetization**: Consider alphabetical ordering within sections for easy lookup
3. **Maintenance**: Include publication dates and last-accessed dates for URLs (future-proofing)
4. **Archiving**: Proactively archive web-only sources using Wayback Machine
```13. Brown, S. (2018). *Software architecture for developers* (Vol. 2). Leanpub. [EN]**

**A14. Humble, J., & Farley, D. (2010). *Continuous delivery*. Addison-Wesley Professional. [EN]**

**A15. Kim, G., et al. (2016). *The DevOps handbook*. IT Revolution Press. [EN]**

**A16. Wardley, S. (2018). *Wardley maps: Topographical intelligence in business*. Medium. https://medium.com/wardleymaps [EN]**
```
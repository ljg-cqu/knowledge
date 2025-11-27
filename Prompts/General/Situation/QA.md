# Situation Deep Analysis Generator

**Purpose**: Generate 20-30 situation analyses (success/failure) across 7 lifecycle phases using 6 viewpoints (strategic/operational/human/environmental/resource/risk).

**Application**: Cross-industry learning, decision analysis, incident investigation, training programs, knowledge bases, retrospectives, case studies, organizational learning across all domains (business, healthcare, education, government, manufacturing, agriculture, finance, technology, non-profit, etc.).

**Universal Design**: This framework applies to any domain or industry. The 7 categories, 6 viewpoints, and lifecycle model are intentionally domain-agnostic while allowing for sector-specific customization. Whether analyzing a surgical procedure, policy implementation, product launch, or agricultural initiative, the core analytical structure remains consistent, ensuring transferable insights across contexts.

## I. Key Definitions

- **Success/Failure**: Achieved/missed goals with measurable outcomes
- **Lifecycle**: Planning → Preparation → Execution → Monitoring → Adaptation → Completion → Reflection (cases span ≥1 phase, 50% span ≥3)
- **Stakeholders**: Decision makers, Implementers/Practitioners, Beneficiaries/Recipients, Influencers/Authorities, Observers/Monitors, Affected parties/Communities, Regulators/Overseers, Funders/Sponsors (≥3/case)
- **Viewpoint**: Strategic, Operational, Human, Environmental, Resource, Risk (≥3/case)
- **Complexity**: Simple (1-2 phases, <3 stakeholders) | Moderate (3-5 phases, 3-6 stakeholders) | Complex (6-7 phases, >6 stakeholders)

## II. Requirements

**Cases**: 20-30 | 50/50 success/failure (±10%) | 30/40/30 Simple/Moderate/Complex (±5%) | 400-700 words/case | ≥90% have ≥2 citations | ≥3 viewpoints/case

**Quality Score**: `(Citations×0.2) + (Viewpoints×0.15) + (Stakeholders×0.15) + (Lifecycle×0.1) + (Quantitative×0.2) + (Artifacts×0.1) + (WordCount×0.1)` ≥0.85/1.0

**7 Categories (MECE)**: 
1. **Strategic & Planning** (4-5 cases): Long-term direction, goal-setting, market/competitive positioning, policy development, strategic initiatives
2. **Operational & Execution** (3-4 cases): Process implementation, service delivery, production, day-to-day operations, workflow management
3. **People & Culture** (3-4 cases): Team dynamics, leadership, organizational culture, communication, collaboration, talent management
4. **Crisis & Response** (3-4 cases): Emergency management, incident response, risk realization, adverse events, recovery operations
5. **Resource & Economics** (3-4 cases): Financial management, capital allocation, budgeting, asset utilization, economic sustainability
6. **Innovation & Transformation** (2-3 cases): Change management, process improvement, new initiatives, technology adoption, organizational evolution
7. **Governance & Compliance** (2-3 cases): Regulatory adherence, ethical standards, oversight mechanisms, accountability, quality assurance

Each category needs ≥1 success AND ≥1 failure.

**References**: C≥20, F≥8, M≥10, D≥15 (≥40% domain-specific), A≥30 (APA 7th). If >25 cases: multiply ×1.5

**Visuals**: ≥2 artifacts/case, ≥1 diagram + ≥1 table/category (14 min), ≥4 Mermaid diagrams total

**Citation Standards**:
- Format: APA 7th with tags [EN]/[ZH]/[Case]/[Report]/[Regulatory]/[Framework]. Inline: `[Ref: A12, C3]`
- Language: EN 50-70%, ZH 15-30%
- Sources: ≥5 types, none >25%
- Recency: ≥60% <3yrs (≥80% for emerging domains)
- Primary sources only; all URLs accessible
- Cross-reference quantitative claims with ≥2 sources

## III. Execution (7 Steps)

### Step 1: Plan Allocation
Distribute 20-30 cases across 7 categories with 30/40/30 S/M/C and 50/50 success/failure balance. Each category needs ≥1 success AND ≥1 failure.

### Step 2: Build References (BEFORE cases)
- **C≥20**: Concepts/patterns (universal and domain-specific, e.g., root cause analysis, systems thinking, clinical reasoning, lean manufacturing)
- **F≥8**: Frameworks/models (applicable across domains, e.g., SWOT, PDCA, risk matrices, balanced scorecard, logic models)
- **M≥10**: Methods/tools (domain-appropriate techniques, e.g., Six Sigma, evidence-based practice, policy analysis, change management)
- **D≥15**: Domain sources (≥40% domain-specific: industry reports, sector research, professional journals, regulatory documents, practitioner publications)
- **A≥30**: Academic/public (APA 7th, ≥60% <3yrs, cross-disciplinary where relevant)

### Step 3: Generate Analyses (400-700 words each)
**Generate 3 at a time, validate before proceeding.**

**Structure per case:**
1. **Classification** (20-30w): Entity/Organization/Institution, Year, Outcome, Category, Complexity, Lifecycle phases, Domain/Industry
2. **Context** (100-150w): Specific domain/industry, organizational scale, key players/actors, timeline, explicit goals/objectives, operational constraints, regulatory/environmental context [≥1 A#]
3. **Lifecycle** (50-80w): Phase-by-phase what happened
4. **Multi-Viewpoint** (150-250w): ≥3 from Strategic/Operational/Human/Environmental/Resource/Risk [≥2 C#/F#/M#]
5. **Stakeholders** (50-80w): ≥3 groups affected
6. **Quantitative** (40-60w): Time/cost/people/quality metrics [≥1 A#]
7. **Root Causes/Enablers** (50-80w): Why success/failure occurred
8. **Lessons** (80-120w): Patterns, transferable practices, trade-offs [≥1 C#]
9. **Recommendations** (50-80w): Strategic/Tactical/Operational actions
10. **Citations**: Simple ≥2, Moderate/Complex ≥3
11. **Artifacts**: ≥2 (Timeline/Process/Metrics/Decision Matrix/Impact Map/Root Cause Tree)

**Per-case checklist:**
☐ Real-world documented with URL | ☐ Domain/industry clearly specified | ☐ ≥3 viewpoints substantive | ☐ 400-700 words | ☐ ≥1 phase (prefer ≥3) | ☐ Specific numbers | ☐ Citations resolve | ☐ ≥2 artifacts | ☐ Actionable lessons | ☐ Domain-appropriate stakeholders identified

### Step 4: Create Visuals
≥2 artifacts/case | ≥4 Mermaid diagrams total | ≥1 diagram + 1 table/category (14 min)

**Universal Types**: Timeline (Gantt), Process Flow (<25 nodes), Metrics Table, Decision Matrix, Impact Map, Root Cause Tree, Stakeholder Analysis Matrix

**Domain-Specific Options**: 
- Clinical pathway diagrams (healthcare)
- Supply chain flow charts (manufacturing/logistics)
- Policy implementation timelines (government)
- Student outcome dashboards (education)
- Financial performance metrics (business/finance)
- Agricultural cycle calendars (farming)
- Service delivery maps (non-profit/public services)

### Step 5: Populate References
Complete all fields, add tags, include URLs, alphabetize. Verify 100% citations resolve.

### Step 6: Run 21 Validations (ANY fail = Stop, Fix, Re-run ALL)
1. Reference floors (C≥20, F≥8, M≥10, D≥15, A≥30)
2. Case distribution (20-30, 30/40/30 ±5%, 50/50 ±10%)
3. Citations/case (≥90% have ≥2; ≥50% have ≥3)
4. Language/Type mix (EN 50-70%, ZH 15-30%)
5. Recency (≥60% <3yrs)
6. Source diversity (≥5 types, none >25%)
7. Real-world documentation (100% URLs)
8. URL accessibility (100%)
9. Cross-reference resolution (100%)
10. Word count (100% in 400-700)
11. Category balance (7/7 have both outcomes)
12. Per-category evidence (≥2 auth + ≥1 case + ≥1 metric)
13. Multi-viewpoint (≥85% have ≥3)
14. Stakeholder coverage (≥70% have ≥3 groups)
15. Lifecycle mapping (≥80% have ≥1; ≥50% have ≥3)
16. Quantitative data (≥90% specific numbers)
17. Root cause/enablers (100%)
18. Lessons/patterns (100% transferable)
19. Visual artifacts (≥2/case, ≥4 Mermaid, 14 total)
20. Authenticity (100% real-world)
21. Domain diversity (≥4 different industries/sectors represented across all cases)

### Step 7: Final Review
Sample ≥5 cases (10%): Verify real-world with URL, domain explicitly stated, balanced success/failure per category, multi-viewpoint depth (≥3 substantive), lifecycle mapped, quantitative rigor (specific numbers), clear root causes, transferable patterns across domains, actionable recommendations, domain-appropriate artifacts present, citations resolve, domain diversity (≥4 industries).

## IV. Validation Report

Complete after generating all cases. ANY fail = Stop, Fix, Re-run ALL.

| # | Check | Criteria | Status |
|---|-------|----------|--------|
| 1 | Reference floors | C≥20, F≥8, M≥10, D≥15, A≥30 (×1.5 if >25) | PASS/FAIL |
| 2 | Case distribution | 20-30, 30/40/30±5%, 50/50±10% | PASS/FAIL |
| 3 | Citations/case | ≥90% have ≥2; ≥50% have ≥3 | PASS/FAIL |
| 4 | Language/Type | EN 50-70%, ZH 15-30% | PASS/FAIL |
| 5 | Recency | ≥60% <3yrs (≥80% emerging) | PASS/FAIL |
| 6 | Source diversity | ≥5 types, none >25% | PASS/FAIL |
| 7 | Real-world URLs | 100% | PASS/FAIL |
| 8 | URL accessibility | 100% | PASS/FAIL |
| 9 | Cross-ref resolution | 100% | PASS/FAIL |
| 10 | Word count | 100% in 400-700 | PASS/FAIL |
| 11 | Category balance | 7/7 both outcomes | PASS/FAIL |
| 12 | Category evidence | ≥2 auth + ≥1 case + ≥1 metric each | PASS/FAIL |
| 13 | Multi-viewpoint | ≥85% have ≥3 substantive | PASS/FAIL |
| 14 | Stakeholder coverage | ≥70% have ≥3 groups | PASS/FAIL |
| 15 | Lifecycle mapping | ≥80% ≥1; ≥50% ≥3 | PASS/FAIL |
| 16 | Quantitative data | ≥90% specific numbers | PASS/FAIL |
| 17 | Root cause/enablers | 100% | PASS/FAIL |
| 18 | Lessons/patterns | 100% transferable | PASS/FAIL |
| 19 | Visual artifacts | ≥2/case, ≥4 Mermaid, 14 total | PASS/FAIL |
| 20 | Authenticity | 100% real-world | PASS/FAIL |
| 21 | Domain diversity | ≥4 different industries/sectors | PASS/FAIL |

**Status**: ☐ ALL PASS | ☐ FAILURES DETECTED

## V. Quality Checklist

Apply to ≥5 cases (10%). Score 9 dimensions (0/0.5/1). If case <6/9 (≥3 fails), rewrite.

**9 Dimensions**:
1. **Verified**: Public documentation with URL
2. **Balanced**: Category has both outcomes
3. **Multi-View**: ≥3 viewpoints substantive (>50w each)
4. **Lifecycle**: Phases explicitly named
5. **Quantitative**: Actual numbers (not "significant")
6. **Causal**: Root cause tree shows logic
7. **Actionable**: Specific techniques (not "communicate better")
8. **Stakeholders**: ≥3 groups with different impacts
9. **Complexity Aligned**: Classification matches content

**Target**: ≥7.5/9 per case

## VI. Output Format

### A. TOC Structure
1. Executive Summary (optional - should highlight domain diversity and cross-industry applicability)
2. Category Overview (table: 7 categories, distribution, quality metrics, domains covered)
3. Situation Analyses by Category (7 sections with cases)
4. Cross-Case Patterns (optional - emphasize transferable lessons across industries)
5. References (C/F/M/D/A)
6. Validation Report

### B. Category Overview Table
| # | Category | Range | Count | Mix | Success/Fail | Domains Covered | Artifacts |
|---|----------|-------|-------|-----|--------------|-----------------|-----------|
| Show distribution summary for each of 7 categories with industries represented |

### C. Case Format (11 sections, 400-700 words)

**Header**: Analysis #, Entity/Organization, Domain/Industry, Success/Failure, Category, Complexity, Year, Phases

**Sections**:
1. **Context** (100-150w): **MUST explicitly state domain/industry** (e.g., "healthcare-surgical services", "education-K-12", "manufacturing-automotive"), organizational scale, key players/actors, timeline, explicit goals/objectives, operational constraints, regulatory/environmental context [≥1 A#]
2. **Lifecycle** (50-80w): Phase-by-phase what happened
3. **Multi-Viewpoint** (150-250w, ≥3 required, 40-80w each):
   - **Strategic**: Goals, mission alignment, competitive/positional advantage, long-term vision, policy implications
   - **Operational**: Processes, workflows, efficiency, quality control, coordination, execution mechanics, service delivery
   - **Human**: People dynamics, culture, communication, leadership, motivation, skills/capacity, organizational behavior
   - **Environmental**: External forces, market/sector conditions, regulatory landscape, timing, societal factors, external dependencies
   - **Resource**: Financial capital, human capacity, time, materials, infrastructure, technology, asset utilization, sustainability
   - **Risk**: Threats, vulnerabilities, mitigation strategies, contingency planning, resilience, safety, compliance exposure
4. **Stakeholders** (50-80w): ≥3 groups, impacts, power dynamics
5. **Quantitative** (40-60w): Time/cost/people/quality metrics [≥1 A#]
6. **Root Causes/Enablers** (50-80w): Primary + contributing factors + preventability/markers
7. **Lessons** (80-120w): Patterns, transferable practices, warning signs, trade-offs, alternatives [≥1 C#]
8. **Recommendations** (50-80w): Strategic/Tactical/Operational/Detection/Prevention
9. **Citations**: Simple ≥2, Moderate/Complex ≥3
10. **Artifacts** (≥2): Timeline/Process/Metrics/Decision/Impact/Root Cause
11. **URL**: Primary source (public accessible)

### D. Reference Formats

**C. Concepts** (≥20): Definition, Application context, Related concepts, Used in cases, Limitations
**F. Frameworks** (≥8): Purpose, Scope, Key components, Case relevance, URL
**M. Methods** (≥10): Description, Maturity, Used in cases, Applications, URL
**D. Domain Sources** (≥15): Summary, Case type, Key lessons, Credibility, URL
**A. Academic/Public** (≥30, APA 7th): Books, Papers, Reports, Case studies, Regulatory [EN]/[ZH] tags

## VII. Examples Across Domains

**Format reference** - all cases should include: Context (domain/scale/players/timeline/goals/constraints), Lifecycle (phases), Multi-Viewpoint (≥3 viewpoints), Stakeholders (≥3 groups), Quantitative (metrics), Root Causes/Enablers, Lessons, Recommendations, Citations, Artifacts, URL.

**Domain examples**:
- **Crisis & Response**: Apollo 13 mission (aerospace), Hospital emergency response (healthcare), Supply chain disruption recovery (manufacturing)
- **Operational & Execution**: Manufacturing process improvement (industry), Surgical protocol implementation (healthcare), Curriculum rollout (education)
- **Strategic & Planning**: Market expansion strategy (business), Public health policy (government), Agricultural diversification (farming)
- **People & Culture**: Cultural transformation initiative (corporate), Teacher retention program (education), Volunteer engagement (non-profit)
- **Resource & Economics**: Budget reallocation (government), Capital investment decision (finance), Resource optimization (agriculture)
- **Innovation & Transformation**: Digital transformation (retail), Treatment protocol innovation (medicine), Educational technology adoption (schools)
- **Governance & Compliance**: Regulatory compliance program (pharma), Ethics framework implementation (finance), Quality assurance system (manufacturing)

## VIII. Domain Adaptation

**Framework flexibility**: The core structure applies universally across all domains. Adapt by customizing:
- **Lifecycle phases**: Adjust to domain-specific workflows (e.g., clinical care pathway, manufacturing cycle, legislative process, agricultural season)
- **Stakeholders**: Identify domain-relevant groups (e.g., patients/providers, students/teachers, citizens/officials, customers/suppliers)
- **Viewpoints**: Always use all 6 (Strategic/Operational/Human/Environmental/Resource/Risk) - they apply universally
- **Metrics**: Use domain-appropriate KPIs (e.g., patient outcomes, student achievement, production yield, customer satisfaction)

**Preserve core structure**: Context → Lifecycle → Multi-Viewpoint → Stakeholders → Quantitative → Root Causes → Lessons → Recommendations

**Industry-specific considerations**:
- **Healthcare**: Patient safety, clinical protocols, regulatory compliance, care continuity, evidence-based practice
- **Education**: Learning outcomes, pedagogical approaches, student engagement, curriculum design, institutional accreditation
- **Manufacturing**: Production efficiency, quality control, supply chain, equipment maintenance, lean principles
- **Government/Public Sector**: Policy impact, public service delivery, stakeholder consultation, transparency, equity
- **Finance**: Risk management, regulatory compliance, market conditions, fiduciary responsibility, liquidity
- **Agriculture**: Seasonal cycles, environmental factors, yield optimization, sustainability, market volatility
- **Non-profit**: Mission alignment, donor relations, community impact, volunteer management, sustainability
- **Retail/Services**: Customer experience, inventory management, market positioning, service quality, profitability
- **Technology**: Innovation velocity, technical debt, scalability, user adoption, security

**Universal principles**: Goal clarity, multi-stakeholder perspective, quantitative measurement, root cause analysis, pattern recognition, early warning systems, cultural factors, resource trade-offs, risk mitigation, continuous learning, context sensitivity, systemic thinking.

**Lifecycle adaptation examples**:
- **Default**: Planning → Preparation → Execution → Monitoring → Adaptation → Completion → Reflection
- **Healthcare/Clinical**: Assessment → Diagnosis → Treatment Planning → Intervention → Monitoring → Evaluation → Follow-up
- **Education**: Needs Assessment → Curriculum Design → Resource Preparation → Implementation → Assessment → Adjustment → Evaluation
- **Manufacturing**: Design → Prototyping → Production Setup → Manufacturing → Quality Control → Process Improvement → Review
- **Government/Policy**: Problem Identification → Policy Design → Stakeholder Consultation → Implementation → Monitoring → Adjustment → Evaluation
- **Agriculture**: Planning → Land Preparation → Planting → Growing/Maintenance → Harvesting → Post-harvest → Season Review
- **Project Management**: Initiation → Planning → Execution → Monitoring/Controlling → Closing → Retrospective → Lessons Learned

Note: Cases can span 1-7 phases; prefer ≥3 phases for moderate/complex cases.

## IX. Pre-Submission Checklist

**Critical**:
☐ All 21 validations PASS (Section IV)
☐ ≥5 cases score ≥6.5/9 (Section V)
☐ TOC + 7 categories + 5 references + validation
☐ C≥20, F≥8, M≥10, D≥15, A≥30; 20-30 cases; ratios met
☐ Citations resolve; URLs accessible
☐ 11-section template; APA 7th; H2/H3 hierarchy
☐ ≥2 artifacts/case, ≥4 Mermaid, 14 total
☐ Quality score ≥0.85/1.0
☐ Domain diversity: ≥4 different industries/sectors represented

**Important**:
☐ Domain/industry explicitly stated for each case
☐ Specific recommendations (not generic, domain-appropriate)
☐ ≥60% sources <3yrs
☐ ≥85% ≥3 viewpoints; ≥70% ≥3 stakeholders
☐ ≥90% specific numbers
☐ No placeholders
☐ Domain-appropriate stakeholders and metrics identified
☐ Cross-industry transferable lessons articulated

## X. Success Metrics

**Targets**: Hallucination reduction ↓30-60%, Decision quality ↑60-80%, Comprehensiveness ≥0.85/1.0, Citation compliance ≥90% have ≥2, Multi-viewpoint ≥85% have ≥3, Stakeholders ≥70% have ≥3, Quantitative rigor ≥90% specific numbers, Root cause 100%, Visuals ≥2/case, Validation 100%, Quality review ≥80% score ≥6.5/9, Time 3-8h for 24 cases.

---

**Document Version**: 3.0 (Cross-Industry Universal Framework)  
**Last Updated**: 2025-11-27  
**Compatibility**: Optimized for Claude 3.5 Sonnet, GPT-4, and equivalent LLMs with instruction following and structured reasoning capabilities  
**Scope**: Universal application across all industries, domains, and sectors (healthcare, education, manufacturing, government, finance, agriculture, technology, non-profit, retail, services, and beyond)

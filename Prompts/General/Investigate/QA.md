# Investigate Q&A & Case Report Generator

**Purpose**: Generate 4–6 investigative Q&As analyzing one multi-actor case (incident, regulatory action, industry pattern, systemic failure), explaining what happened, why, and implications for decisions.

**Scope**: One case from background to present (+ optional 1–3 year outlook) across ≥2 dimensions (technical, operational, business, market, ecosystem, regulatory, organizational, cultural, geographic, political). Must involve ≥3 actors/factors. **Applicable across all industries**: technology, healthcare, finance, manufacturing, energy, education, government, non-profit, etc.

**Output**: 4–6 Q&As (150–250 words each) + case-summary paragraph; each Q&A addresses one investigation angle across multiple actors/factors.

**Validity**: 6–12 months until new evidence, major shifts, or regulatory changes require re-run.

**Users**: Manager, analyst, researcher, consultant, executive, investor, risk manager, compliance officer, regulator, strategist, policy maker, technical writer.

**Terms**:
- **Case**: Bounded situation with clear temporal/contextual boundaries
- **Actor**: Entity influencing outcomes (organization, institution, government body, regulator, stakeholder group, market participant)
- **Factor**: Structural variable shaping outcomes (financial leverage, governance structure, legal/regulatory regime, market dynamics, resource availability, cultural norms)
- **Angle**: Investigation dimension (incentives, causal chain, industry structure, systemic risk, organizational dynamics, policy impacts)

## Minimal Workflow (80/20)

**5 steps to produce a reliable investigation in minimal time:**

1. **Define**: Case title, time span, decision context (enter/exit market, invest/divest, implement/abandon, partner/compete, expand/contract, regulate/deregulate, adopt/reject), 3–5 critical questions, hypotheses to test
2. **Map**: Background + ≥3 key events + ≥3 actors/factors (organizations, institutions, regulators, market segments, structural variables)
3. **Write**: 4–6 Q&As (see Q&A Template); each covers ≥2 dimensions, references ≥2–3 actors/factors, includes ≥1 citation
4. **Visualize**: 1 table summarizing events/years/actors/factors/impacts (or add timeline/network diagram)
5. **Validate**: Confirm background→present coverage, main causal story + alternatives, ≥5 citations from ≥3 types

**Target**: Reduce investigation time by ≥60% vs ad-hoc search.

## LLM Prompt Requirements

**Required context** (self-contained in single prompt):
- **Case**: Title, 1–2 sentence description with scale (market size, revenue, customers/users, employees, geographies, affected population)
- **Time span**: Background→present (+ optional 1–3 year outlook); note key periods/shocks
- **Decision**: Context and roles (Manager/Analyst/Investor/Risk/Compliance/Policy), constraints (budget, risk appetite, regulatory, political, resource)
- **Actors/factors**: ≥3 mandatory (organizations, institutions, jurisdictions, market segments, stakeholders, structural forces); LLM may add more
- **Hypotheses**: ≥2 competing explanations to test (e.g., "market forces vs regulatory failure" or "cultural factors vs economic incentives")
- **Questions**: 3–5 critical, time-bounded questions about the *case*, not single objects
- **Preferences**: Language mix, max length, source types, research time

**Exclude**: External references ("see other file"), unsourced speculation >3–5 years, single-object narratives.

## Standards

### Coverage
- **Angles** (4–6 Q&As): Background (1), Actors/Incentives (1–2), Causal Chain (1), Impact/Outlook (1–2)
- **Citations**: ≥5 total, ≥3 types (academic research, industry reports, news, organizational documents, regulatory filings, case studies, statistical data), 50–70% EN / 20–40% ZH / 5–15% other; APA 7th with language tag; inline as `[Ref: ID]`
- **References**: Glossary ≥6 terms, Resources ≥3, Literature ≥3 (≥1 ZH)
- **Visuals**: Minimal = 1 table; Full = 1 timeline/network diagram + 1 table
- **Per Q&A**: 150–250 words, ≥1 citation, explicit time range + regions/segments, ≥2–3 actors/factors

### Quality Gates (must pass all)
1. **Temporal**: Background→present, no unexplained multi-year gaps
2. **Source diversity**: ≥3 citation types
3. **Evidence**: ≥2 authoritative refs per major angle; controversial claims have ≥2 independent sources
4. **Coverage**: All central actors/factors included; gaps marked explicitly
5. **References**: Accessible links, consistent IDs
6. **Coherence**: Dates/sequences align across Q&As, diagrams, tables
7. **Balance**: Facts vs interpretation clear; opposing views presented; uncertainties flagged

### Success Metrics
- Background + ≥3 key event clusters + ≥1 structural pattern
- ≥70% paragraphs cite years/dates
- ≥3 structural insights (how industry/market/regulatory/organizational/cultural structure shaped outcomes)
- ≥3 Q&As address decision-critical angles
- ≥70% Q&As include ≥1 citation
- Reader can extract system-level insights and decision implications

## Question Checklist
Rewrite if fails ≥2:
1. **Clarity**: Single, time-bounded ask about *case* (not single object)
2. **Temporal**: Specifies time window/events/slice
3. **Causal**: Asks why/how actors/factors interacted, not just what changed
4. **Multi-dimensional**: Invites ≥2 dimensions + synthesis across actors/factors
5. **Signal**: Targets structural issues/failures/patterns, not trivia
6. **Decision-aligned**: Connects to strategic decisions (enter/exit, invest/divest, implement/abandon, partner/compete, expand/contract, regulate/deregulate, adopt/mitigate)
7. **Balanced**: For controversial cases, invites multiple perspectives + flags uncertainties
8. **Self-contained**: Names case/timeframe/regions/segments/decision hook explicitly

## Output Structure

**Sections**: 1. Case Overview & Scope | 2. Investigation Q&As by Angle | 3. Visuals | 4. References | 5. Validation Report

**Angle coverage** (4–6 Q&As, Background→Present + optional 1–3yr outlook):

| Angle | Count | Dimensions | Artifacts |
|---|---|---|---|
| Background & Context | 1 | History, structure, regions | Timeline + table |
| Actors & Incentives | 1–2 | Actors, incentives, power | Network map + matrix |
| Causal Chain | 1 | Tech, market, governance | Diagram + event table |
| Impact & Outlook | 1–2 | Impact, risk, strategy, policy | Matrix + scenarios |

### Q&A Template

**Angle**: [Background / Actors & incentives / Causal chain / Impact & fallout / Lessons]  
**Q#**: [Full question]  
**Timeframe**: [Years/dates] | **Regions/Segments**: [Global/CN/US/EU/etc.]  
**Actors/factors**: [≥2–3 organizations/institutions/regulators/stakeholder groups/market forces]  
**Hypothesis**: [What this tests or explains]  
**Decision**: [Enter/Exit/Invest/Divest/Implement/Partner/Expand/Regulate/Adopt/Mitigate] – [Why critical]  
**Priority**: [Critical/Important/Optional]  
**Key Insight**: [1 sentence: pattern/mechanism/failure]

**Answer** (150–250 words, include ≥1 `[Ref: ID]`):
- **When/where**: Dates, locations, segments, scale (market share %, revenue, budget, population affected, scope, reach)
- **Who/what**: Actors, decisions, events; 1–2 metrics per key actor/factor
- **How**: Causal chain/feedback loops (e.g., resource constraints + misaligned incentives + governance gaps)
- **Why**: Competing narratives; how evidence supports/challenges each
- **So what**: Implications for structure/risk/economics/regulation/operations; decision thresholds
- **Perspectives**: ≥2 stakeholder viewpoints (regulator vs operator, incumbent vs challenger, public vs private sector, consumer vs producer)

**Artifact** *(optional)*: Timeline, causal diagram, network map, comparison table  
**Confidence**: [High/Medium/Low] – [Evidence strength, uncertainties, gaps, contested points]

### Reference Formats

Prioritize recent primary sources (last 5–10 years) for current events; older sources for background; flag secondary/uncertain sources.

- **Glossary**: `G#. Term (Acronym)` | Definition | Use cases | Related | Limitations (alphabetized)
- **Resources**: `R#. Name (Category)` | Role/Purpose | Access/Cost | Users/scale | Latest update | Notes | URL (grouped by category: tools, frameworks, platforms, databases, services)
- **Literature**: `L#. Author, Title, Year` | Summary | Relevance (grouped by language: EN, then ZH)
- **Citations**: `A#. [Citation] [Lang]` | APA 7th with language tag

## Example

**Q1: What combination of market pressures, operational decisions, and regulatory gaps enabled a major pharmaceutical supply chain disruption, and what does this reveal about systemic vulnerabilities in essential medicine distribution (2018–2023)?**

**Angle**: Causal chain  
**Timeframe**: 2018–2023 | **Regions/Segments**: Global (US/EU/Asia; generics + specialty medications)  
**Actors/factors**: Pharmaceutical manufacturers, contract production facilities, distributors, regulators, purchasing organizations, healthcare providers, just-in-time inventory practices  
**Hypothesis**: Drug shortages follow repeatable pattern: cost pressures + consolidation + lean inventory + weak visibility → systemic fragility  
**Decision**: Diversify / Regulate / Mitigate – Structural risk patterns affecting supply reliability and patient safety  
**Priority**: Critical – Directly informs procurement strategy and regulatory policy  
**Key Insight**: Concentration + aggressive cost reduction + opacity + single-source dependencies = brittle supply chain failing under disruption

**Answer** (≈220 words):
In the late 2010s, intense price competition and consolidation in generic pharmaceutical manufacturing led to significant capacity concentration in a few geographic regions, particularly South Asia, while hospitals and distributors adopted just-in-time inventory models to minimize carrying costs [Ref: A1]. Many essential medications became dependent on single manufacturers or production facilities, yet visibility into upstream supply chains remained limited, masking concentration risks and quality control variations [Ref: A2]. Regulatory oversight focused primarily on product quality rather than supply chain resilience, with limited requirements for manufacturer transparency about sourcing, capacity, or backup plans [Ref: A3].

When a combination of quality issues triggered facility shutdowns, raw material constraints emerged, and unexpected demand surges occurred (accelerated by pandemic-related disruptions), these lean structures amplified stress. Production stoppages cascaded through the distribution network; hospitals discovered alternative sources were unavailable or required lengthy qualification processes [Ref: A4]. Shortages forced treatment delays, medication substitutions, and rationing decisions. Subsequent investigations revealed that purchasing organizations' emphasis on lowest-cost sourcing had systematically eliminated redundancy, while information asymmetries prevented early warning or coordinated response [Ref: A5]. The investigative signal: essential goods supply chains that prioritize cost efficiency over resilience, operate with limited visibility, and lack regulatory incentives for redundancy create repeatable vulnerability patterns across sectors and geographies.

**Artifact**:

| Step                          | Years     | Key actors/factors                                | Impact                                          |
|-------------------------------|-----------|---------------------------------------------------|-------------------------------------------------|
| Consolidation & cost focus    | 2015–2019 | Manufacturers, purchasers, lean inventory models  | Concentration, reduced redundancy, hidden risks |
| Disruption cascade            | 2020–2022 | Facility closures, demand surges, material gaps   | Critical shortages, treatment impacts           |
| Response & policy review      | 2022–2023 | Regulators, providers, industry groups            | Emergency measures, resilience requirements     |

**Confidence**: Medium (strong evidence from regulatory reports and industry analysis; some proprietary supply chain data remain unavailable).

## Pre-Flight Check (30s)

Before generating or using an investigation:
- **Prompt**: Case + time span + decision context + stakeholders + ≥2 hypotheses + 3–5 questions; self-contained (no external refs)
- **Q&As**: Follow Q&A Template; 4–6 total mapping to angle coverage; 150–250 words, ≥1 citation, explicit time/region, ≥2–3 actors/factors
- **Standards**: Meet Coverage + Quality Gates + Success Metrics
- **Balance**: For controversial cases, facts vs interpretation clear, opposing views presented, uncertainties flagged; decision implications explicit

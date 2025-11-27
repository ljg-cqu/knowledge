# Trend Q&A & Landscape Report Generator

**Purpose**: Generate 4–6 time-bounded Q&As + landscape overview analyzing how practices, innovations, organizations, regions, and regulations within any domain interact and evolve.

**Scope**: Origin → present (+ optional 1–3 year outlook) | Operational, economic, market, ecosystem, regulatory, geographic dimensions | ≥2–3 exemplars per answer | Validity: 6–12 months

**Users**: Manager, strategist, analyst, researcher, founder, investor, policymaker, consultant, educator

**Output**: Excludes speculation beyond 3–5 years, unsourced rumors, trivia, single-entity biographies

**Key Terms**:
- **Trend cluster**: Coherent signals/events describing one direction (consolidation, decentralization, standardization, specialization, commoditization)
- **Driver**: Structural force pushing/restraining trends (regulation, capital, innovations, demographics, behavior shifts, environmental factors)
- **Signal**: Measurable indicator (market share %, adoption rate, funding $, volume, revenue, enrollments, citations, policy actions)
- **Decision-Critical**: Materially influences enter/invest/expand/pivot/exit/regulate/adopt decisions

## Context Requirements (for LLM Prompts)

Include all in a single self-contained prompt:
- Domain/theme with scale indicators (market size, participants, geographies, revenue, volume)
- Time span (origin→present or explicit years) + key periods/shocks
- Decision context, stakeholder roles, constraints (budget, risk, regulatory)
- Perspectives to emphasize (operational, economic, market, ecosystem, regulatory, geographic) + priority regions/segments
- Language mix, max length, source preferences
- 3–5 decision-critical questions (time-bounded, pattern-level not entity-level)

## Workflow

### 80/20 Core (Time-Limited)
1. **Define focus**: Domain/theme, time span, decision context, stakeholders, 3–5 decision-critical questions
2. **Map trends**: Baseline + ≥3 trend clusters + ≥3 dated signals/events
3. **Write 4–6 Q&As**: Time-bounded, ≥2 dimensions, ≥2–3 exemplars each (see **C. Q&A Format**)
4. **Create 1 artifact**: Table summarizing clusters, timeframes, exemplars, metrics (optional: timeline/2×2)
5. **Validate**: Confirm baseline→present coverage, dominant directions clear, citation/source-diversity floors met

### Full Process
1. **Focus** + optionally list 5–10 representative entities
2. **References**: Glossary ≥6 terms | Key Players/Platforms ≥3 | Literature/Reports ≥3 (≥1 ZH) | Citations ≥5 APA 7th
3. **Cluster**: Group signals/milestones into 3–5 trend clusters mapped to dimensions and exemplars
4. **Q&A**: Each covers one cluster; explains what/why/where/impact; connects clusters
5. **Visuals**: ≥1 diagram (timeline/ecosystem/2×2) + ≥1 table
6. **Validate**: Temporal coverage, source diversity (≥3 types), coherence
7. **Review**: Clarity, narrative flow, decision usefulness

### Citation Standards
APA 7th + language tag `[Ref: ID]` | 50–70% EN, 20–40% ZH, 5–15% other | ≥3 types

### Quality Gates & Success Criteria

**Gates** (failing any ⇒ stop and fix):
1. **Temporal**: Earliest activity → present, no unexplained multi-year gaps | ≥70% paragraphs cite years/dates
2. **Source**: ≥3 citation types | Each cluster/period has ≥2 authoritative refs | ≥70% answers cite ≥1 ref
3. **Spatial**: ≥2 regions/markets for global domains | ≥3 region/segment mentions with differing impact
4. **Coherence**: Dates, sequences, narratives align across Q&As, diagrams, tables | Links accessible, IDs consistent
5. **Balance**: Cross-check data; for controversial trends, distinguish facts from interpretation, note opposing views

**Success** (target: ≥60% time savings vs ad-hoc search):
- Baseline + ≥3 clusters + ≥3 dated signals/events + (if relevant) ≥1 shock
- ≥3 Q&As address decision-critical trends (enter/invest/expand/pivot/exit/regulate/adopt)
- Reader can summarize dominant trends, winners/losers, maturity curve position

## Question Quality (rewrite if fails ≥2)
1. **Clarity**: Single, time-bounded, pattern-level ask (e.g., "Dominant trends in renewable energy storage 2010–2020, who gained/lost market position?")
2. **Temporal**: Specifies time window or events/shocks
3. **Causality**: Why patterns emerged, not just what changed
4. **Depth**: ≥2 dimensions + synthesis across exemplars
5. **Significance**: Real trends/structural shifts, not trivia
6. **Decision-aligned**: Connects to enter/invest/expand/pivot/exit/regulate/adopt
7. **Fairness**: For controversial trends, positive + negative impacts/perspectives

## Output Structure

### TOC
1. Trend Overview & Scope
2. Trend Q&As by Cluster
3. Visuals (Timelines, Maps, Tables)
4. References (Glossary, Key Players/Platforms, Literature/Reports, Citations)
5. Validation Report

### Cluster Template (4–6 Q&As | Baseline → Present + optional 1–3yr outlook)

| Theme                              | Range | Count | Timespan    | Dimensions                    | Artifacts                           |
|------------------------------------|-------|-------|-------------|-------------------------------|-------------------------------------|
| Baseline Context                   | Q1    | 1     | YYYY–YYYY   | Structure, segments, regions  | Map + segment table                 |
| Key Clusters & Drivers             | Q2–Q3 | 2     | YYYY–YYYY   | Operational, economic, market | Cluster table + driver/metric map   |
| Shocks & Counter-Trends            | Q4    | 0–1   | YYYY–YYYY   | Risk, policy, macro, events   | Shock timeline + impact table       |
| Scenarios & Outlook                | Q5–Q6 | 1–2   | YYYY–YYYY+  | Market, geo, strategy         | Scenario matrix + positioning 2×2   |

### Q&A Format

**Type**: Structural / Behavioral / Regulatory / Competitive / Innovation / Ecosystem / Operational

**Q#: [Question]**

**Timeframe**: Years/dates | **Regions/Segments**: Global / CN / US / EU / etc.

**Decision**: Enter / Invest / Expand / Monitor / Pivot / Exit / Regulate / Adopt – [justification]

**Priority**: Critical / Important / Optional – [influence on current decision]

**Key Insight**: [1 sentence: pattern/shift/cluster]

**Answer** (150–250 words):
- **When & where**: Dates, locations, segments, scale (market %, funding $, volume, participants, policy scope)
- **What**: Pattern across entities (leaders, challengers, regions) + 1–2 metrics
- **Why**: Impact on structure/adoption/economics/risk/regulation; thresholds/decision points
- **Connections**: Links to adjacent clusters; reinforcing/opposing dynamics
- **Direction**: Rising/maturing/declining/consolidating/fragmenting; leading indicators
- **Perspectives**: ≥2 stakeholder viewpoints (incumbent vs entrant, regulator vs operator, buyer vs seller)
- **Refs**: ≥1 `[Ref: ID]`

**Artifact** *(optional)*: Timeline / ecosystem map / 2×2 / comparison table

**Confidence**: High / Medium / Low – [evidence strength, uncertainties, gaps]

### Reference Formats

Prioritize recent primary sources (last 5–10 years) for current trends; older for origin history; flag secondary/uncertain sources.

**Glossary**: `G#. Term (Acronym)` | Definition | Use cases | Related concepts | Limitations (alphabetized)

**Key Players/Platforms**: `P#. Name (Category)` | Role | Scale | Market position | Latest (Q# YYYY) | Partnerships | Trend notes | URL (grouped by category)

**Literature/Reports**: `L#. Author, Title, Year` | Summary (focus/framework/findings) | Relevance (grouped EN first, then ≥1 ZH)

**Citations**: `A#. [Citation] [Lang]` (APA 7th + language tag)

## Example

**Q1: What were the dominant trends in electric vehicle battery supply chains 2015–2023, and how did they shift power among manufacturers/regions?**

**Type**: Innovation / Ecosystem / Competitive

**Timeframe**: 2015–2023 | **Regions/Segments**: Global (CN/EU/US automotive markets)

**Decision**: Invest / Monitor – Secure battery supply partnerships vs vertical integration strategy

**Priority**: Critical – Influences manufacturing location, sourcing strategy, cost structure for EV production

**Key Insight**: China's vertical integration + scale advantages drove battery supply consolidation, prompting Western manufacturers toward domestic capacity building and supply diversification.

**Answer**:
Battery supply chains were fragmented 2015–2016: multiple chemistries (lithium-ion variants, LFP, NMC) competed across geographic clusters with limited standardization [Ref: A1]. Chinese manufacturers (CATL, BYD) scaled rapidly 2017–2019 leveraging domestic lithium processing (70% global capacity) and government EV subsidies, achieving 50%+ cost advantages [Ref: A2]. European automakers (VW, BMW, Stellantis) initially relied on Asian imports but announced €40B+ gigafactory investments 2020–2022 following supply chain disruptions and IRA/EU Battery Regulation pressure [Ref: A3].

US Inflation Reduction Act (2022) and CHIPS Act mandated domestic content thresholds, accelerating North American capacity announcements (Tesla-Panasonic, GM-LG, Ford-SK) and critical mineral sourcing agreements [Ref: A4]. 2023 signals: regional clusters forming (CN scale leader, EU standards leader, US policy-driven growth), but China retains processing dominance; differentiation shifting to solid-state R&D, recycling infrastructure, and material security [Ref: A5].

**Artifact**:

| Cluster                        | Years     | Exemplars                             | Impact                                 |
|--------------------------------|-----------|---------------------------------------|----------------------------------------|
| Fragmented chemistry/geo       | 2015–2016 | Multiple chemistries, diverse sources | Competing standards, unclear leaders   |
| Chinese scale dominance        | 2017–2019 | CATL, BYD, lithium processing         | Cost leadership, supply concentration  |
| Western localization push      | 2020–2022 | EU gigafactories, IRA, regulations    | Supply security, capacity race         |
| Regional cluster formation     | 2023–     | CN scale, EU standards, US subsidies  | Geographic fragmentation, material risk|

**Confidence**: High (widely documented across industry, policy, financial sources)

## Quick Check (30s)

Before sending prompt or using output, confirm:

- **Context**: Domain/theme, time span, decision context, stakeholders, 3–5 decision-critical questions stated; terms defined
- **Precision**: Each Q&A has timeframe, regions/segments, metrics, priority; ≥2–3 exemplars; focuses on patterns/shifts not trivia
- **MECE**: Questions partition into baseline, clusters, shocks, outlook with minimal overlap; cover baseline→present, no multi-year blind spots
- **Depth**: Operational, economic, market, ecosystem, regulatory, geo dimensions present; explains why patterns emerged + impact on actors
- **Significance**: Most Q&As address decision-critical clusters; priorities labeled; 150–250 words, no redundant background
- **Evidence**: Citation/source-diversity floors met; recent primary sources; consistent IDs; outdated/low-credibility flagged
- **Logic**: Chronologically coherent; explicit causality; controversial trends show positive + negative impacts; ≥2 stakeholder perspectives
- **Structure**: Follows TOC + Q&A format; labeled fields (timeframe, decision, priority, insight, confidence); visuals referenced
- **Verification**: Dates/figures cross-checked; decision implications concrete ("monitor", "enter in 2–3 years"); rerun if major uncertainties remain

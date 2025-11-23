# Trend Q&A & Landscape Report Generator

**Purpose**: Generate 4–6 time-bounded Q&As + landscape overview analyzing how technologies, products, companies, regions, and regulations within a domain interact and evolve.

**Scope**: Origin → present (+ optional 1–3 year outlook) | Technical, business, ecosystem, regulatory, geographic dimensions | ≥2–3 exemplars per answer | Validity: 6–12 months

**Users**: PM, architect, engineer, researcher, founder, investor, policy/compliance

**Output**: Excludes speculation beyond 3–5 years, unsourced rumors, trivia, single-object biographies

**Key Terms**:
- **Trend cluster**: Coherent signals/events describing one direction (consolidation, platformization, commoditization)
- **Driver**: Structural force pushing/restraining trends (regulation, capital, tech breakthroughs, user behavior)
- **Signal**: Measurable indicator (market share %, funding $, TVL, DAU, policy actions)
- **Decision-Critical**: Materially influences enter/invest/expand/pivot/exit/regulate decisions

## Context Requirements (for LLM Prompts)

Include all in a single self-contained prompt:
- Domain/theme with scale indicators (market size, users, geographies, revenue)
- Time span (origin→present or explicit years) + key periods/shocks
- Decision context, stakeholder roles, constraints (budget, risk, regulatory)
- Perspectives to emphasize (technical, business, ecosystem, regulatory, geographic) + priority regions/segments
- Language mix, max length, source preferences
- 3–5 decision-critical questions (time-bounded, space-level not object-level)

## Workflow

### 80/20 Core (Time-Limited)
1. **Define focus**: Domain/theme, time span, decision context, stakeholders, 3–5 decision-critical questions
2. **Map trends**: Baseline + ≥3 trend clusters + ≥3 dated signals/events
3. **Write 4–6 Q&As**: Time-bounded, ≥2 dimensions, ≥2–3 exemplars each (see **C. Q&A Format**)
4. **Create 1 artifact**: Table summarizing clusters, timeframes, exemplars, metrics (optional: timeline/2×2)
5. **Validate**: Confirm baseline→present coverage, dominant directions clear, citation/source-diversity floors met

### Full Process
1. **Focus** + optionally list 5–10 representative objects
2. **References**: Glossary ≥6 terms | Tools/Platforms ≥3 | Literature/Reports ≥3 (≥1 ZH) | Citations ≥5 APA 7th
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
- ≥3 Q&As address decision-critical trends (enter/invest/expand/pivot/exit/regulate)
- Reader can summarize dominant trends, winners/losers, maturity curve position

## Question Quality (rewrite if fails ≥2)
1. **Clarity**: Single, time-bounded, space-level ask (e.g., "Dominant trends in container orchestration 2013–2020, who gained/lost power?")
2. **Temporal**: Specifies time window or events/shocks
3. **Causality**: Why patterns emerged, not just what changed
4. **Depth**: ≥2 dimensions + synthesis across exemplars
5. **Significance**: Real trends/structural shifts, not trivia
6. **Decision-aligned**: Connects to enter/invest/expand/pivot/exit/regulate
7. **Fairness**: For controversial trends, positive + negative impacts/perspectives

## Output Structure

### TOC
1. Trend Overview & Scope
2. Trend Q&As by Cluster
3. Visuals (Timelines, Maps, Tables)
4. References (Glossary, Tools/Platforms, Literature/Reports, Citations)
5. Validation Report

### Cluster Template (4–6 Q&As | Baseline → Present + optional 1–3yr outlook)

| Theme                              | Range | Count | Timespan    | Dimensions                    | Artifacts                           |
|------------------------------------|-------|-------|-------------|-------------------------------|-------------------------------------|
| Baseline Context                   | Q1    | 1     | YYYY–YYYY   | Structure, segments, regions  | Map + segment table                 |
| Key Clusters & Drivers             | Q2–Q3 | 2     | YYYY–YYYY   | Tech, business, ecosystem     | Cluster table + driver/metric map   |
| Shocks & Counter-Trends            | Q4    | 0–1   | YYYY–YYYY   | Risk, security, policy, macro | Shock timeline + impact table       |
| Scenarios & Outlook                | Q5–Q6 | 1–2   | YYYY–YYYY+  | Market, geo, strategy         | Scenario matrix + positioning 2×2   |

### Q&A Format

**Type**: Structural / Behavioral / Regulatory / Competitive / Technology / Ecosystem

**Q#: [Question]**

**Timeframe**: Years/dates | **Regions/Segments**: Global / CN / US / EU / etc.

**Decision**: Enter / Invest / Expand / Monitor / Pivot / Exit / Regulate – [justification]

**Priority**: Critical / Important / Optional – [influence on current decision]

**Key Insight**: [1 sentence: pattern/shift/cluster]

**Answer** (150–250 words):
- **When & where**: Dates, locations, segments, scale (market %, funding $, TVL, DAU, policy scope)
- **What**: Pattern across objects (players, challengers, regions) + 1–2 metrics
- **Why**: Impact on structure/adoption/economics/risk/regulation; thresholds/decision points
- **Connections**: Links to adjacent clusters; reinforcing/opposing dynamics
- **Direction**: Rising/maturing/declining/consolidating/fragmenting; leading indicators
- **Perspectives**: ≥2 stakeholder viewpoints (incumbent vs entrant, regulator vs operator, retail vs institutional)
- **Refs**: ≥1 `[Ref: ID]`

**Artifact** *(optional)*: Timeline / ecosystem map / 2×2 / comparison table

**Confidence**: High / Medium / Low – [evidence strength, uncertainties, gaps]

### Reference Formats

Prioritize recent primary sources (last 5–10 years) for current trends; older for origin history; flag secondary/uncertain sources.

**Glossary**: `G#. Term (Acronym)` | Definition | Use cases | Related concepts | Limitations (alphabetized)

**Tools/Platforms**: `T#. Name (Category)` | Role | Pricing | Users/scale | Latest (Q# YYYY) | Integrations | Trend notes | URL (grouped by category)

**Literature/Reports**: `L#. Author, Title, Year` | Summary (focus/framework/findings) | Relevance (grouped EN first, then ≥1 ZH)

**Citations**: `A#. [Citation] [Lang]` (APA 7th + language tag)

## Example

**Q1: What were the dominant trends in container orchestration 2013–2020, and how did they shift power among vendors/ecosystems?**

**Type**: Technology / Ecosystem

**Timeframe**: 2013–2020 | **Regions/Segments**: Global (US/EU/CN cloud)

**Decision**: Monitor / Invest – Standardize on K8s + managed services vs legacy stacks

**Priority**: Critical – Influences platform, hiring, vendor strategy for cloud-native

**Key Insight**: Open governance + multi-cloud support drove K8s consolidation, reshaping competition among clouds and earlier orchestrators.

**Answer**:
Container orchestration was fragmented 2013–2014: Google Borg, Mesos/Marathon, Docker Swarm targeted different segments [Ref: A1]. Kubernetes emerged 2014 from Borg/Omega and moved to neutral CNCF governance 2015, signaling no single vendor control [Ref: A2]. 2016–2018, major clouds (GKE, EKS, AKS, Alibaba Cloud) launched managed K8s services, lowering operational barriers and creating cross-vendor baseline [Ref: A3].

As tooling (Helm, Istio, Prometheus) concentrated around K8s, Mesos/Marathon and Docker Swarm lost momentum; talent, roadmaps, community followed consolidation [Ref: A4]. Enterprises standardized on K8s platforms, giving hyperscalers and platform vendors (Red Hat OpenShift) structural advantages [Ref: A5]. 2019–2020 signal: orchestration commoditized, differentiation shifted to dev experience, security, multi-cluster management, higher-level PaaS.

**Artifact**:

| Cluster                        | Years     | Exemplars                             | Impact                                 |
|--------------------------------|-----------|---------------------------------------|----------------------------------------|
| Fragmented pre-K8s             | 2013–2014 | Borg, Mesos/Marathon, Docker Swarm    | Competing models, unclear standard     |
| K8s + neutral governance       | 2014–2016 | Kubernetes, CNCF, early clouds        | Open candidate, rising mindshare       |
| Managed services consolidation | 2016–2018 | GKE/EKS/AKS, Alibaba, OpenShift       | Simplified adoption, power reshuffle   |
| Platform-layer differentiation | 2019–2020 | Service meshes, dev platforms, sec    | Orchestration commoditized, stack up   |

**Confidence**: High (widely documented, multiple independent sources)

## Quick Check (30s)

Before sending prompt or using output, confirm:

- **Context**: Domain/theme, time span, decision context, stakeholders, 3–5 decision-critical questions stated; terms defined
- **Precision**: Each Q&A has timeframe, regions/segments, metrics, priority; ≥2–3 exemplars; focuses on clusters/shifts not trivia
- **MECE**: Questions partition into baseline, clusters, shocks, outlook with minimal overlap; cover baseline→present, no multi-year blind spots
- **Depth**: Tech, business, ecosystem, regulatory, geo dimensions present; explains why patterns emerged + impact on actors
- **Significance**: Most Q&As address decision-critical clusters; priorities labeled; 150–250 words, no redundant background
- **Evidence**: Citation/source-diversity floors met; recent primary sources; consistent IDs; outdated/low-credibility flagged
- **Logic**: Chronologically coherent; explicit causality; controversial trends show positive + negative impacts; ≥2 stakeholder perspectives
- **Structure**: Follows TOC + Q&A format; labeled fields (timeframe, decision, priority, insight, confidence); visuals referenced
- **Verification**: Dates/figures cross-checked; decision implications concrete ("monitor", "enter in 2–3 years"); rerun if major uncertainties remain

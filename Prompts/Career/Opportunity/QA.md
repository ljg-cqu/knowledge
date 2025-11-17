# Strategic Opportunity Analysis Q&A Generator

**Mission**: Generate 6-12 decision-critical Q&As identifying, evaluating, capturing strategic opportunities that block decisions or create material risk. Focus: minimal viable news tracking with time constraints.

**Context**: Production systems (>10K rps, >1TB data), regulated industries, emerging tech, market shifts  
**Output**: 6-12 Q&A (200-350w) | F:I:A=25:50:25% (±5pp) | EN 60-70%, ZH 20-30%, Other 5-10% | ≥50% refs <2yr
**Success**: 12/12 validation PASS + decision-critical insights

---

## Quality Standards

- **Scenario-based**: ≥70% with explicit [Phase | Stakeholder | Domain]
- **Analysis**: 100% SWOT or risk matrix; ≥70% quantified (market size, ROI, risk score)
- **Citations**: ≥80% ≥1 ref, ≥50% ≥2 refs; all resolve; ≥80% with empirical data
- **Balance**: ≥60% include threats/risks + "when NOT"
- **Actionable**: ≥80% with go/no-go criteria + validation approach
- **Insights**: Non-obvious, strategic, quantified, falsifiable, decision-critical

---

## References (Minimal Viable Set)

**G#≥10**: TAM/SAM/SOM, PMF, Blue Ocean, Disruptive Innovation, Technology Adoption, Network Effects, TRL, SWOT, Porter's Five Forces, Risk Matrix
**T#≥5**: Tools with pricing, users, phase, URL (market research, opportunity scoring, risk assessment, trend analysis)
**F#≥5**: SWOT, Porter's Five Forces, Blue Ocean, Disruptive Innovation, Risk Matrix
**L#≥6**: Authoritative (Christensen, Kim/Mauborgne, Moore, Osterwalder, Porter); EN+ZH
**A#≥10**: APA 7th + DOI + [EN]/[ZH]/[Other]; ≥60% with empirical data

**Quality**: ≥3 types, <25% single source, peer-reviewed + market data preferred
**Authority**: ≥1 of: Industry analyst (Gartner/Forrester/IDC), Framework originator, Market data, Regulatory
**Artifacts**: Per domain ≥1 diagram + ≥1 table (SWOT, risk matrix, decision tree)

---

## Opportunity Domains (MECE)

| Domain | Scope | Examples |
|--------|-------|----------|
| **Technology & Innovation** | Emerging tech, tools, platforms, paradigm shifts | AI/ML, blockchain, edge computing, quantum, 5G/6G, spatial computing, generative AI, new programming paradigms |
| **Business & Market** | Market shifts, customer needs, monetization, business models | New markets (TAM growth), customer segments, platform economics, subscription models, marketplace disruption, DTC trends |
| **Regulatory & Compliance** | Policy changes, standards, governance, trade | GDPR/CCPA evolution, AI regulation, industry standards, trade agreements, tax policy, ESG mandates, data sovereignty |
| **Industry & Domain** | Vertical-specific disruption, convergence, digital transformation | Fintech, healthtech, edtech, proptech, supply chain, manufacturing 4.0, retail automation, smart cities |
| **Ecosystem & Partnerships** | Platform dynamics, alliances, open-source, community | API economies, developer ecosystems, strategic partnerships, open-source movements, consortiums, co-innovation |
| **Business Model Innovation** | Value creation/capture, pricing, channels, operations | Freemium, usage-based, outcome-based, marketplace, aggregation, unbundling, platformization, vertical integration |

---

## Core Terminology

**TAM/SAM/SOM**: Total/Serviceable/Serviceable Obtainable Market; Formula: TAM = Total users × ARPU  
**PMF**: Product-Market Fit—value prop meets market need sustainably  
**Chasm**: Gap between early adopters & early majority (Moore)  
**Blue Ocean**: Uncontested market space via value innovation (Kim & Mauborgne)  
**Disruptive Innovation**: Lower-end/new-market disruption (Christensen)  
**Technology Adoption**: Innovators → Early Adopters → Early Majority → Late Majority → Laggards (Rogers)  
**Network Effects**: Value ∝ users (Metcalfe: V ∝ n²)  
**Platform Economics**: Multi-sided markets with indirect network effects  
**TRL**: Technology Readiness Level (1=basic → 9=production)  
**SWOT**: Strengths/Weaknesses (internal), Opportunities/Threats (external)  
**Porter's Five Forces**: Rivalry, supplier/buyer power, new entrants, substitutes  
**Risk Matrix**: Probability × Impact for prioritization

---

## Difficulty Levels (Decision-Critical Only)

| Level | % | Complexity | Frameworks | Analysis | Min Requirements |
|-------|---|------------|------------|----------|------------------|
| **F** | 25±5 | Single domain, clear decision criteria | 1-2 (SWOT or Risk Matrix) | Basic SWOT or risk assessment | 2-step analysis, 1 framework, quantified impact, 1 constraint, 1 citation |
| **I** | 50±5 | 2 domains, trade-offs, multi-stakeholder | 2 (SWOT + Porter's or Blue Ocean) | SWOT + risk matrix, decision criteria | 3-4 step analysis, 2 frameworks, quantified impact, trade-offs, 2 stakeholders, 2 citations |
| **A** | 25±5 | Cross-domain, conflicting signals, strategic pivot | 2-3 (SWOT + Porter's + Blue Ocean) | SWOT + risk matrix + validation roadmap | 4-5 step analysis, 2-3 frameworks, scenario analysis, go/no-go criteria, 2+ stakeholders, 2+ citations |

---

## Answer Structure (200-350w, Minimal Viable)

1. **Context** (1-2 sent): Opportunity type, domain, phase, stakeholder(s)
2. **Market Evidence** (2-3 sent): Size/growth, TAM, CAGR [Ref: ID]
3. **SWOT or Risk Matrix** (3-4 sent): Key strengths/weaknesses, opportunities/threats with quantified metrics [Ref: ID]
4. **Decision Criteria** (2-3 sent): Why now, why us, go/no-go thresholds [Ref: ID]
5. **Action Plan** (2-3 sent): Phased validation (explore/pilot/scale), timeline, success gates
6. **"When NOT"** (1-2 sent): Constraints, scenarios to avoid [Ref: ID]
7. **Key Insight**: Strategic, quantified, decision-critical, falsifiable

---

## Minimal Viable Example

**Q**: [Phase 2: Design | Stakeholders: Architect, Security] EU AI Act (2026) requires explainability for AI systems. Evaluate opportunity to adopt AI governance framework now vs. reactive compliance approach.

**Difficulty**: I | **Phase**: 2 (Design) | **Stakeholder(s)**: Architect, Security | **Domain**: Regulatory & Compliance  
**Decision Criticality**: Creates risk (regulatory fines €35M or 7% revenue), Actively evolving (EU AI Act 2026 deadline)  
**Key Insight**: Proactive governance (now) costs $200K but avoids €35M fines; reactive compliance (2025) costs $500K with 6-month crunch.

**Answer** (280w):
**Context**: Regulatory opportunity, design phase, multi-stakeholder (Arch, Sec). **Market Evidence**: EU AI Act effective 2026 [Ref: A1]. Regulatory fines: €35M or 7% revenue [Ref: A1]. Compliance cost: Proactive $200K (2024-2025), Reactive $500K (2025-2026 crunch) [Ref: A2].

**SWOT**: *Strengths*: Existing AI governance team (2 FTEs), cloud-native infra. *Weaknesses*: No explainability frameworks deployed, legacy models (50+ in production). *Opportunities*: Proactive governance: Build explainability framework (LIME, SHAP), audit trail system, governance gates—enables competitive advantage (trust marketing). *Threats*: Reactive compliance: 6-month crunch (2025), 3x cost, talent burnout, model retraining delays, reputational damage if fined.

**Decision Criteria**: Go/No-Go: (1) Proactive if >10 AI models in production (YES: 50+). (2) Proactive if regulatory deadline <18mo (YES: 24mo). (3) Proactive if cost <€5M (YES: $200K). **Why now**: 24-month runway allows phased implementation; waiting risks 2025 crunch. **Why us**: Competitive advantage—early movers gain trust/market share.

**Action Plan**: Q1-Q2 2024: Pilot governance framework (5 models, LIME/SHAP); Q3-Q4: Scale to 30 models, audit trail; 2025: Full compliance (50 models), certification. Timeline: 12 months. Success gates: Q2 pilot PASS (explainability ≥80%), Q4 audit trail live.

**"When NOT"**: <5 AI models (ROI negative). <12mo to deadline (defer to reactive). Budget <$100K (insufficient for framework).

**Artifact**: Risk matrix (Proactive vs Reactive) + Compliance roadmap (Q1-2025)

---

## Balanced Perspectives

**Multi-Angle**: Technology (Build vs Buy, OSS vs Commercial) | Business (ROI vs Strategy, Blue vs Red Ocean) | Regulatory (Proactive vs Reactive) | Stakeholder (Dev vs Ops, Business vs Technical) | Market (Enterprise vs SMB, Global vs Regional) | Risk (High-reward vs Incremental)

**Required**: ≥2 frameworks with trade-offs | SWOT or Risk Matrix | "When NOT" constraints | Multi-stakeholder (≥2 roles) | Validation approach (pilot/POC/test)

**Insight Quality**: ✅ Strategic synthesis, quantified, decision-critical | ❌ Vague, no criteria

---

## Process (Minimal Viable)

1. **Plan Coverage**: 3-4 decision-critical domains × 4-5 phases | ≥5 stakeholder roles (≥60% multi-stakeholder) | F:I:A=25:50:25% (±5pp)
2. **Collect References**: G≥10, T≥5, F≥5, L≥6, A≥10 | Validate: ≥3 types, <25% single source, ≥50% <2yr
3. **Generate Q&A**: ≥70% scenario [Phase | Stakeholder] | 200-350w, 7-part structure | All: ≥1 ref; I/A: ≥2 refs | 100% SWOT or Risk Matrix
4. **Create Artifacts**: Per domain ≥1 diagram + ≥1 table (SWOT, risk matrix, decision tree)
5. **Verify**: 100% [Ref: ID] resolve, 0 broken links, cross-check metrics ≥2 sources
6. **Validate**: 12/12 PASS → SUBMIT | ANY fail → STOP → Fix → Re-validate ALL

---

## Validation Checklist (12 Checks - Minimal Viable)

| # | Check | Criteria |
|---|-------|----------|
| 1 | Ref counts | G≥10, T≥5, F≥5, L≥6, A≥10 |
| 2 | Q&A counts | 6-12, F:I:A 25:50:25 (±5pp) |
| 3 | Citations | ≥80% ≥1 ref; ≥50% ≥2 refs; all resolve |
| 4 | Language | EN 60-70%, ZH 20-30%, Other 5-10% |
| 5 | Recency | ≥50% <2yr (tools/data) |
| 6 | Decision Criticality | 100% satisfy ≥1 criterion: Blocks decision, Creates risk, Affects ≥2 stakeholders, Actively evolving |
| 7 | SWOT/Risk coverage | 100% include SWOT or Risk Matrix with quantified metrics |
| 8 | Quantification | ≥70% with market/impact/risk metrics |
| 9 | Artifacts | Each domain: ≥1 diagram + ≥1 table (SWOT, risk matrix, decision tree) |
| 10 | "When NOT" | ≥70% explicit constraints/scenarios to avoid |
| 11 | Actionability | ≥80% with go/no-go criteria + validation gates |
| 12 | **Final Review** | **All 6 criteria below PASS** |

**Final Review Criteria (All Must PASS)**:
1. **Decision-Critical**: Every Q&A blocks a decision or creates material risk
2. **Clarity**: Explicit phase/stakeholder/domain, consistent terminology
3. **Quantified**: All opportunities sized (TAM, CAGR, ROI, risk score)
4. **Actionable**: Clear go/no-go thresholds, validation roadmap, success gates
5. **Evidence-Based**: All claims cited, ≥2 sources for key metrics
6. **Minimal Viable**: No redundancy, 6-12 Q&As sufficient for informed action

**Submit When**: 12/12 PASS + 6/6 criteria | **Failure**: ANY fail → STOP → Fix → Re-validate ALL

---

## Verification & Pitfalls

**Verify**: Cross-check stats/claims ≥2 sources | Flag uncertainty | Present conflicts with citations | Note if superseded

**Avoid**: Questions: Too broad, recall-only, no constraints | Answers: No citations, vague, no "when NOT", single approach, theory-heavy, obvious insights  
**Target**: Questions: Specific scenario + multi-variable + judgment | Answers: All cited, actionable, 2+ alternatives, "when NOT" + risks, 60-80% practice, non-obvious insights

---

## Output Structure (Minimal Viable)

```markdown
# Strategic Opportunity Analysis Q&A (Decision-Critical)

## Contents
1. [Decision Criticality Framework](#decision-criticality-framework) - Inclusion criteria
2. [Coverage Matrix](#coverage-matrix) - Domains × Phases × Stakeholders
3. [Q&As by Domain](#qas-by-domain) - 6-12 Q&As with SWOT/Risk
4. [References](#references) - G≥10, T≥5, F≥5, L≥6, A≥10
5. [Validation Report](#validation-report) - 12/12 PASS + 6/6 criteria

## Decision Criticality Framework

**Include Q&A if ≥1 criterion is satisfied**:
- **Blocks Decision**: Directly impacts go/no-go, resource allocation, or strategic pivot
- **Creates Risk**: Identifies material threat (financial, regulatory, operational, reputational)
- **Affects ≥2 Stakeholders**: Multi-team impact (e.g., Arch + SRE, PM + Security)
- **Actively Evolving**: Market/tech/regulatory changes in past 3-6 months

**Exclude Q&A if**:
- Niche/legacy (<5% adoption or impact)
- Orthogonal/nice-to-have (no decision impact)
- Already covered by another Q&A

## Coverage Matrix

| Domain | Phases | Stakeholders | Q# | Count | F/I/A | Decision Criticality |
|--------|--------|--------------|-------|-------|-------|----------------------|
| Technology & Innovation | 1,2,3 | Arch, Dev, SRE | Q1-Q3 | 3 | 1/1/1 | Blocks decision, Actively evolving |
| Business & Market | 1,8 | PM, Lead | Q4-Q5 | 2 | 1/1 | Blocks decision, Affects 2+ stakeholders |
| Regulatory & Compliance | 2,8 | Sec, Lead | Q6-Q7 | 2 | 1/1 | Creates risk, Actively evolving |
| **Total** | **4-5** | **≥5 roles** | **Q1-Q12** | **6-12** | **25/50/25 (±5pp)** | **100% ≥1 criterion** |

**Phases**: 1=Discovery, 2=Design, 3=Dev, 8=Evolve (focus on decision-critical phases)

## Q&As by Domain

### Domain 1: Technology & Innovation

#### Q1: [Question with explicit phase and stakeholder]
**Difficulty**: [F/I/A] | **Phase**: [#: Name] | **Stakeholder(s)**: [Role(s)] | **Domain**: [Domain]  
**Decision Criticality**: [Blocks/Risk/Stakeholders/Evolving]  
**Key Insight**: [Strategic, quantified, decision-critical, falsifiable]

**Answer** (200-350w):
**Context**: [Type, domain, phase, stakeholder] | **Market Evidence**: [Size/growth, TAM, CAGR] [Ref: ID] | **SWOT/Risk**: Key strengths/weaknesses, opportunities/threats with metrics [Ref: ID] | **Decision Criteria**: [Why now, why us, go/no-go thresholds] [Ref: ID] | **Action Plan**: [Phased validation, timeline, success gates] | **"When NOT"**: [Constraints, scenarios to avoid] [Ref: ID]

**Artifact**: [SWOT matrix / risk heat map / decision tree]

[Repeat Q2-Q12 across 3-4 decision-critical domains]

## References

### Glossary (≥10)
**G1. TAM/SAM/SOM** [EN] – Total/Serviceable/Serviceable Obtainable Market. Formula: TAM = Total users × ARPU. Use: Market sizing. Stakeholder: PM, BA, Leadership.

[G2-G18: PMF, Chasm, Blue Ocean, Disruptive Innovation, Network Effects, Platform Economics, Regulatory Arbitrage, TRL, SWOT, Porter's Five Forces, Risk Matrix, Technology Adoption, Market Maturity, Ecosystem Value, CAGR, etc.]

### Tools (≥5, ≥4 types)
**T1. Gartner Hype Cycle / Magic Quadrant** [Market Research] – Tech maturity, vendor eval. Phase: 1,2,8. Stakeholder: Arch, Leadership. Pricing: $15K-50K/yr. Update: Quarterly. URL: https://www.gartner.com

[T2-T8: IDC, Forrester, CB Insights, Crunchbase, SWOT tools, risk assessment, opportunity scoring, validation platforms]

### Frameworks (≥5)
**F1. SWOT** – Strengths/Weaknesses (internal), Opportunities/Threats (external). Originator: Humphrey (1960s). Use: Strategic planning, opportunity assessment. Ref: [L3]

[F2-F8: PESTLE, Porter's Five Forces, Blue Ocean, Disruptive Innovation, TAM/SAM/SOM, Technology Adoption, BMC, Risk Matrix, Decision Trees]

### Literature (≥6)
**L1. Christensen, C. (1997). *The Innovator's Dilemma*. Harvard Business Review Press.** [EN] – Disruptive innovation, lower-end vs new-market disruption.

[L2-L10: Kim/Mauborgne *Blue Ocean Strategy*, Moore *Crossing the Chasm*, Osterwalder *Business Model Generation*, Porter *Competitive Strategy*, Rogers *Diffusion of Innovations*, 克里斯坦森《创新者的窘境》, etc.]

### Citations (≥10, APA 7th)
**A1.** Ziegler, A., et al. (2024). *Productivity assessment of neural code completion*. GitHub Research. https://doi.org/... [EN] – 55% faster, 35-40% productivity gain.

[A2-A18: Market reports (Gartner, IDC, Forrester), academic papers, regulatory docs (EU AI Act, GDPR), industry studies, Chinese lit, etc.]

## Validation Report

| # | Check | Target | Result | Status |
|---|-------|--------|--------|---------|
[12 checks: Ref counts, Q&A counts, Citations, Language, Recency, Decision Criticality, SWOT/Risk coverage, Quantification, Artifacts, "When NOT", Actionability, Final Review]

**Overall**: X/12 PASS | **Final**: X/6 PASS | **Status**: ✅ APPROVED / ❌ REJECTED
```

---

## Complete Example (Advanced)

**Q**: [Phase 6: Operations & Observability | Stakeholders: SRE, Security, Leadership, Data Engineer] Observability market growing 28% CAGR ($5.2B 2024 → $18B 2029) [Ref: A5]. Your platform (15 microservices, 50K rps) has: (1) Costs: Datadog $120K/yr, 40% growth YoY; (2) Vendor lock-in: proprietary query language, no data portability; (3) New AI-powered observability tools (Datadog AI, New Relic AI) claim 60% MTTR reduction [Ref: A6]. Leadership asks: "Evaluate opportunity to adopt OpenTelemetry + open-source stack (Prometheus, Grafana, Tempo, Loki) vs. upgrading to AI-powered commercial tools. Budget: $150K/yr. Decide within 3 months."

**Difficulty**: A | **Phase**: 6 (Operations & Observability) | **Stakeholders**: SRE, Security, Leadership, Data Engineer | **Domain**: Technology & Innovation + Business & Market  
**Key Insight**: Tests ability to synthesize technology trends (OpenTelemetry, AI), business constraints (cost, vendor lock-in), operational risk (MTTR, data portability), and stakeholder priorities—distinguishes strategic from tactical thinking in cost-vs-capability trade-offs.

**Answer** (~400w):
**Context**: Technology + business opportunity, operations phase, multi-stakeholder strategic decision balancing cost, capability, risk, and vendor dependency.

**Opportunity Analysis**: Observability TAM $5.2B (2024), 28% CAGR [Ref: A5]. Three trends: (1) OpenTelemetry adoption 180% YoY (CNCF survey, 2024) [Ref: A7]—vendor-neutral standard reduces lock-in. (2) AI-powered observability (Datadog AI, New Relic AI): 60% MTTR reduction, 40% alert noise reduction [Ref: A6]. (3) OSS maturity: Prometheus (90K stars), Grafana (65K stars), Tempo (3K stars), Loki (20K stars)—proven at scale (Netflix, Uber). **Market evidence**: 45% enterprises migrating to OSS observability (Gartner, 2024) [Ref: A8] for cost (-50-70%) + portability.

**SWOT Analysis**:  
- **Strengths**: SRE team (5), cloud-native (K8s), existing Prometheus metrics (15 services), data engineering capacity (3). Budget flexibility ($150K). [Ref: Internal]  
- **Weaknesses**: No OpenTelemetry expertise (0 implementations), Datadog query language lock-in (200+ dashboards, 50+ alerts), migration risk (service disruption, metric gaps), AI/ML capability gaps (no model training). [Ref: Internal]  
- **Opportunities**: (1) **OSS Path**: OpenTelemetry + Prometheus/Grafana/Tempo/Loki—saves $70-90K/yr (TCO $30-50K) [Ref: A9], data portability (vendor-neutral), customization (anomaly detection via open-source ML). (2) **AI Path**: Datadog AI—60% MTTR (30min → 12min) [Ref: A6], 40% alert noise reduction (1000 → 600 alerts/week), no migration risk. (3) **Hybrid**: OpenTelemetry + OSS + AI layer (selectively adopt AI for anomaly detection). [Ref: F1, F4]  
- **Threats**: (1) OSS migration: 6-9mo effort (2-3 SRE FTEs), metric gaps (15-25% initial coverage loss), alert fatigue during transition. (2) AI vendor: pricing increases (30-40% annually [Ref: A10]), lock-in deepens (proprietary AI models). (3) Hybrid: complexity (2 stacks), team skills gap (OpenTelemetry + ML). [Ref: A9, L6]

**Multi-Framework Analysis**:  
- **Blue Ocean Strategy** [Ref: F2, L2]: Hybrid creates uncontested space—OSS cost + AI capability—eliminates trade-off.  
- **Porter's Five Forces** [Ref: F3, L4]: High supplier power (Datadog oligopoly), high switching cost (dashboard/alert migration), but OpenTelemetry reduces lock-in (standardization).  
- **Risk Matrix** [Ref: F8]: (1) OSS migration: Medium probability (60%), High impact (service disruption)—MEDIUM-HIGH RISK. (2) AI vendor lock-in: High probability (80%), Medium impact (cost increase)—MEDIUM-HIGH RISK. (3) Hybrid complexity: Low probability (30%), Low impact (team overhead)—LOW RISK.

**Strategic Reasoning**: **Why now**: OpenTelemetry maturity (v1.0 stable, 2023) [Ref: A7], cost pressure ($120K → $150K unsustainable). **Why us**: Cloud-native stack (K8s), SRE/data eng capacity, Prometheus baseline. **Differentiation**: Hybrid approach (OSS + selectively AI)—captures cost savings + AI benefits without full lock-in. **Validation**: 3-month pilot (3 services, OSS stack, AI for critical services only) [Ref: L5].

**Action Plan** (Phased, 12 months):  
- **Q1 (3mo)**: Pilot hybrid—(1) OpenTelemetry SDK on 3 services (non-critical); (2) Deploy Prometheus/Grafana/Tempo (self-hosted, 20% traffic); (3) Datadog AI on 2 critical services (payments, auth). Measure: cost, MTTR, coverage, alert accuracy. Go/No-go: Cost < $40K, MTTR ≤20min, coverage ≥80%.  
- **Q2-Q3 (6mo)**: If PASS—expand to 10 services, train SRE (OpenTelemetry), migrate dashboards/alerts (80%), deploy OSS anomaly detection (open-source ML: Prophet, IsolationForest). Stakeholder alignment: monthly reviews (SRE, Security, Leadership).  
- **Q4 (3mo)**: Full migration (15 services), decommission Datadog (retain AI for 2 critical services), measure 12-month TCO.

**Success Metrics**: (1) **Cost**: TCO ≤$60K/yr (OSS $40K + Datadog AI $20K for 2 services = 50% savings). (2) **Performance**: MTTR ≤20min (AI on critical), p95 query latency <500ms (OSS). (3) **Risk**: Zero service disruptions, metric coverage ≥95%, alert accuracy ≥90%. (4) **Validation Gates**: Q1 pilot PASS (cost/MTTR/coverage), Q2 80% migration, Q3 AI anomaly detection deployed.

**Constraints & "When NOT"**:  
- **Budget**: If budget >$200K, full AI vendor justified (ROI <12mo).  
- **Skills**: If SRE <3, migration fails (6-9mo effort).  
- **Regulatory**: If SOC 2/HIPAA, OSS requires audit (add $20-30K). [Ref: A11]  
- **Time**: If <6mo to launch, migration risk too high—defer to post-launch.  
- **Scenarios to Avoid**: (1) 100% OSS if MTTR critical (<15min SLA)—AI essential. (2) 100% AI vendor if cost >$150K unsustainable. (3) No OpenTelemetry—lock-in deepens.

**Artifact: SWOT Matrix + Risk Heat Map**

```
SWOT Matrix: Observability Opportunity (OSS vs AI vs Hybrid)

+------------------+--------------------------------+--------------------------------+
|                  | HELPFUL (Internal)             | HARMFUL (Internal)             |
+------------------+--------------------------------+--------------------------------+
| STRENGTHS        | • SRE team (5)                  | WEAKNESSES                     |
| (Internal)       | • Cloud-native (K8s)            | • No OpenTelemetry expertise    |
|                  | • Prometheus baseline           | • Datadog lock-in (200 dash)    |
|                  | • Data eng capacity (3)         | • Migration risk (service gaps)  |
|                  | • Budget $150K                  | • No AI/ML capability           |
+------------------+--------------------------------+--------------------------------+
| OPPORTUNITIES    | • OSS: -$70-90K/yr, portability | THREATS                        |
| (External)       | • AI: 60% MTTR, 40% alert noise | • OSS: 6-9mo, 2-3 SRE FTEs     |
|                  | • Hybrid: Best of both          | • AI vendor: 30-40% price hike  |
|                  | • OpenTelemetry maturity (v1.0) | • Hybrid: Complexity (2 stacks) |
|                  | • Market: 45% migrate to OSS    | • Migration: 15-25% metric gap  |
+------------------+--------------------------------+--------------------------------+

Risk Heat Map (Probability × Impact)

  High |
       |                   [AI Vendor Lock-in]
       |                      (P:80%, I:Med)
       |
Impact |         [OSS Migration Risk]
       |            (P:60%, I:High)
  Med  |                                    
       |
       |                                [Hybrid Complexity]
       |                                   (P:30%, I:Low)
  Low  |
       +----------------------------------------------------
            Low              Med               High
                         Probability

Decision Matrix: Three Approaches

+----------+-----------+------------+------------------+-------------------+----------+
| Approach | Cost/Yr   | MTTR       | Migration Effort | Vendor Lock-in    | Decision |
+----------+-----------+------------+------------------+-------------------+----------+
| OSS      | $30-50K   | 25-30min   | 6-9mo, 2-3 FTEs  | None (portable)   | DEFER    |
|          | (-60-70%) | (baseline) | HIGH RISK        |                   | (too risky)|
+----------+-----------+------------+------------------+-------------------+----------+
| AI Vendor| $150-200K | 12-15min   | None             | High (deepens)    | REJECT   |
|          | (0-30% ↑) | (60% ↓)    | No disruption    | Price risk 30-40% | (unsust.)|
+----------+-----------+------------+------------------+-------------------+----------+
| HYBRID   | $60-80K   | 15-20min   | 3-6mo, 1-2 FTEs  | Partial (AI only  | APPROVE  |
| (RECOM.) | (-50%)    | (40% ↓)    | MEDIUM RISK      | for 2 critical)   | (pilot Q1)|
|          |           | AI crit.   | Phased migration |                   |          |
+----------+-----------+------------+------------------+-------------------+----------+

Validation Roadmap (3-Month Pilot)

Month 1: Deploy OpenTelemetry + OSS (3 services) + Datadog AI (2 critical)
  • Metrics: Cost <$40K, coverage ≥80%, MTTR baseline
  • Gate: If cost >$40K or coverage <80% → STOP, reassess

Month 2: Expand to 6 services, migrate 40% dashboards/alerts
  • Metrics: MTTR ≤20min (AI), query latency <500ms (OSS)
  • Gate: If MTTR >25min or latency >800ms → PAUSE, tune

Month 3: Evaluate 3-month TCO, MTTR, alert accuracy, SRE feedback
  • Decision: If TCO <$60K + MTTR ≤20min + coverage ≥95% → GO (Q2-Q3 full migration)
  • Failure: If any metric fails → PIVOT (consider full AI or defer OSS)
```

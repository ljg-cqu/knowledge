# Value Chain Analysis Q&A Generator

Generate 25–30 scenario-based questions testing value chain analysis across industry ecosystems with multi-stakeholder perspectives, evidence-based answers, and visual artifacts.

## I. Context

**Purpose**: Assess value chain analysis capabilities across industry ecosystems (Participants → Flows → Opportunities → Disruption) for 9+ stakeholders (Business Strategy, Product, PM, BD/Sales, Operations, Finance, Data, Marketing, Leadership).

**Terms**: Floor=minimum threshold (≥) | Gate=fail-stop checkpoint | Difficulty: F=execution | I=strategy/trade-offs | A=portfolio/ecosystem | Chain Types: B2B SaaS, E-Commerce, FinTech, Healthcare, Manufacturing | Analysis Types: Current State, Pain+Power, Change+Trends, Value Pool, Bottleneck, Network Effects

**Scope**: Full chain analysis (participants/flows/economics/power dynamics), short/long-term trends, all perspectives. **Exclude**: Single-node/stakeholder focus, trivia, recall-only.

**Assumptions**: LLM knows frameworks (Value Pool, Theory of Constraints, Switching Costs, Network Effects, JTBD, Value Stream Mapping); 10-15min per question.

**Limitations**: Scenarios require industry customization; economics context-dependent; power dynamics vary by market.

## II. Requirements

### Floors (Minimum Thresholds)

| Category | Requirement |
|----------|-------------|
| **Q&A** | 25–30 \| 20%F/40%I/40%A (±5%) \| 150–300 words/answer \| Each: ≥2 analysis types+stakeholders |
| **Topics (MECE)** | Current State/Pain+Power/Change+Trends/Value Pool/Bottleneck/Network Effects/Opportunities/Disruption (3–4 each) \| Cross-Industry (4–5) |
| **Citations** | ≥70% have ≥1; ≥30% have ≥2 \| EN 50–70%, ZH 20–40%, Other 5–15% |
| **Analysis Types** | Each industry: ≥4 of 6 |
| **Stakeholders** | ≥8 total; each Q&A ≥2 |
| **References** | Glossary ≥15 \| Tools ≥8 \| Literature ≥8 (≥2 ZH: 曾鸣/梁宁/俞军) \| Citations ≥15 APA 7th |
| **Visuals** | Per industry: ≥1 diagram+table (8+8 min) \| Cross-industry: ≥2 chain flow diagrams |
| **Scaling** | >30 Q&A: multiply reference floors by 1.5× |

### Gates (Fail-Stop)

**Any failure**: stop, fix, re-validate ALL

| # | Gate | Criteria | Mitigation |
|---|------|----------|------------|
| 1 | **Recency** | ≥50% from last 3yrs (≥70% platform/marketplace) | Flag outdated with caveats |
| 2 | **Source Diversity** | ≥3 types; no type >25% | Expand research |
| 3 | **Per-Topic Evidence** | Each: ≥2 authoritative+1 tool | Add missing |
| 4 | **Tool Completeness** | Industry examples, economics, update (≤18mo), ≥3 use cases | Complete/replace |
| 5 | **Link Validation** | 100% URLs accessible/archived | Archive/replace |
| 6 | **Cross-Reference** | 100% [Ref: ID] resolve; no orphans | Fix broken |

## III. Analysis Layers

## III. Execution

### Step 1: Plan Allocation

Distribute 25–30 Q&A across 9 topics (20%F/40%I/40%A ±5%). Mix difficulties; ensure ≥8 stakeholders; each Q&A ≥2 analysis types.

**Example** (28): 8 analysis areas × 3 + Cross-Industry × 4 = 6F/11I/11A

### Step 2: Build References (BEFORE Q&A, then run Gates 1–6)

| Type | Count | Required | ID |
|------|-------|----------|-----|
| **Glossary** | ≥15 | Term, definition, measurement, stakeholder, industry, limitations | G1... |
| **Tools** | ≥8 | Category, industry examples, economics, update (≤18mo), ≥3 use cases, metrics, stakeholders, chain phase, URL | T1... |
| **Literature** | ≥8 (≥2 ZH) | Author, title, year, summary, frameworks, industry | L1... |
| **Citations** | ≥15 | APA 7th+[EN]/[ZH]/[Other]; ≥50% from last 3yrs | A1... |

**Examples**: Glossary—Value Pool, Network Effects, Switching Costs, JTBD, Theory of Constraints, Value Stream Mapping | Tools—Gartner, Forrester, CB Insights, Crunchbase, PitchBook | Literature—Porter, Christensen, Thiel, Reinertsen (EN); 曾鸣, 梁宁, 俞军 (ZH)

### Step 3: Generate Q&A (5 at a time, self-check)

**Question**: Value chain scenario with stakeholder tensions, power dynamics conflicts (participant/flow/opportunity tensions) | Test ≥2 signals: chain mapping, pain identification, economics, power dynamics, disruption analysis | **Avoid** recall ("What is Value Pool?") | **Difficulty**: F=execution | I=strategy | A=ecosystem

**Answer** (150–300 words—ALL required):
1. **Key Insight** (1 sentence): Chain tension
2. **Framework** [Ref: G#/A#]
3. **Multi-Analysis** (≥2): Current State/Pain+Power/Trends/Value Pool/Bottleneck/Network+quantification
4. **Multi-Stakeholder** (≥2): Perspective/economics
5. **Chain Flows**: Information/Product/Capital
6. **Quantification**: Economics, market size, impact
7. **Steps**: Map, analyze, prioritize, strategize
8. **Trade-offs**: Power shifts, disintermediation risks
9. **Communication**: Per stakeholder
10. **Success Criteria**: Metrics, timeframes
11. **Limitations**: Data gaps, assumptions, context
12. **Citations**: ≥1 [Ref: ID]
13. **Artifact** *(optional)*: Chain map/value pool/opportunity matrix

**Batch Check** (per 5): Scenario | ≥2 analysis signals | 150–300 words | ≥2 analysis types | ≥2 stakeholders | Chain aware | ≥3/5 have ≥1 cite (≥1/5 has ≥2)

### Step 4: Create Visuals (≥1 diagram+table per industry)

**By Industry**: B2B SaaS—Chain map, value pool, power dynamics | E-Commerce—Marketplace flow, unit economics, CAC/LTV | FinTech—Regulatory layers, trust barriers, switching costs | Healthcare—Payer-provider, data flow, outcome metrics | Manufacturing—Supply chain, bottleneck, inventory | Cross-Industry—Value pool comparison, network effects, disruption patterns (≥2)

**Practices**: Tables for quantitative (economics, margins, market size) | Diagrams for flows | Include units/periods/currencies | Show participants+flows | Indicate power dynamics | Cite sources

### Step 5: Populate References

| Type | Format |
|------|--------|
| **Glossary** | **G#. Term** \| Definition \| Measurement \| Stakeholder \| Industry \| Limitations (alphabetize) |
| **Tools** | **T#. Tool** \| Description \| Industry Examples \| Economics \| Update (Q# YYYY) \| Use Cases (≥3) \| Metrics \| Stakeholder \| Chain Phase \| URL (group by category) |
| **Literature** | **L#. Author, Title, Year** \| Summary (value chain, frameworks) \| Industry \| Stakeholder (group: EN, ZH) |
| **Citations** | **A#. [APA 7th] [Lang]** (sort by ID) |

**Validation**: 100% [Ref: ID] resolve | No orphans | All fields complete | All APA tagged

### Step 6: Validate (fail ANY = stop, fix, re-run ALL 15)

See **Section IV** for complete checklist. Key:
- **Floors**: G≥15, T≥8, L≥8, A≥15, Q=25–30, 20%F/40%I/40%A (±5%)
- **Citations**: ≥70% have ≥1; ≥30% have ≥2 | EN 50–70%, ZH 20–40%, Other 5–15%
- **Quality**: 100% word count 150–300 | 100% chain-concrete | ≥80% frameworks cited+limits | ≥90% scenario
- **Coverage**: Each industry ≥4 analysis types | ≥8 stakeholders, each Q&A ≥2 | ≥70% cross-participant | 8/8 industries have ≥2 authoritative+1 tool
- **Integrity**: 100% links accessible | 100% [Ref: ID] resolve, no orphans

### Step 7: Final Review

**Questions**: Clarity (single ask) | Chain focus | Depth (trade-offs) | Realism (stakeholder tension) | Industry aware | Discriminative (judgment>recall) | Aligned difficulty

**Answers** (sample ≥5): ≥2 analysis types | ≥2 stakeholders | Chain flows | Quantification | Frameworks+cites | Trade-offs/alternatives | Power dynamics | Success criteria | Limitations/assumptions/uncertainties

**Submit**: All 15 validations PASS | All 6 gates PASS | TOC with links | No placeholders | Balanced perspectives (participants/flows/economics, current/future, power/opportunity)

## V. Analysis Components

### A. Participant Template

**Format**: Name | Role | Function (value add) | Scale (size/volume/share) | Economics (revenue model/margin/cost) | Dependencies (up/downstream) | Alternatives

**Example**: AWS | Cloud Infrastructure | Compute/storage/network | $90B, 32% share | Pay-as-you-go, 25–30% margin | Up: data centers/hardware; Down: SaaS/enterprises | On-premise/colo/edge

### B. Flow Template (3 types)

| Flow | What | Speed/Format/Quality | Friction (lost/distorted/delayed) | Decisions Dependent |
|------|------|---------------------|-----------------------------------|---------------------|
| **Information** | Data between nodes | Fast/slow? Format? Quality? | Where breaks? | What relies? |
| **Product/Service** | Offerings move | Delivery? Speed? | Quality control/failure/constraint? | Inventory/capacity? |
| **Capital** | Money flow | Payment terms/timing? | Who captures? Margin pressure? | Value distribution? |

**Output**: Diagram (volume/speed/friction annotated)

### C. Pain Inventory Template

**Format**: ID | Node | Category (Efficiency/Quality/Cost/Experience/Risk) | Description | Impact (quantified) | Workaround | Cost | Stakeholders

**Example**: P1 | Marketing→Sales | Efficiency+Experience | 60% MQLs rejected | 30hr/wk wasted, ROI unclear | Weekly meetings, manual scoring | $150K/yr + friction | Marketing/Sales/Leadership

### D. Power Map

**Indicators**: Pricing (who sets?) | Switching (how hard?) | Information (who knows?) | Network (scale benefits?) | Regulatory (barriers?) | Brand (loyalty?)

**Visualization**: High=bold/large/thick | Medium=normal | Low=thin/small/dashed | Arrows=influence direction

**Example**: High: Apple (iOS, 30% fee) | Medium: App devs (multi-platform) | Low: End users (price-takers)

### E. Opportunity Types + Template

**Types**: Efficiency (↓cost/time/waste) | Quality (↑reliability/accuracy) | Experience (simplify/delight) | Disintermediation (remove nodes) | Aggregation (consolidate) | Platformization (marketplace) | Verticalization (integrate) | Unbundling (separate)

**Format**: Opportunity | Type | Target Pain | Market (TAM/SAM/SOM) | Impact (quantified) | Feasibility | Moat | Competition | Strategic Fit | Priority

**Example**: AI Lead Scoring | Efficiency+Quality | P1 (MQL reject) | $2B automation | 60%→30% reject, 40% faster cycle | Medium (ML+data) | High (proprietary data/network) | 6sense/Demandbase | High (AI strategy) | P1

## VI. Industry Templates

### A. B2B SaaS

**Chain**: Tech Foundation (Cloud/API) → Platform/Infrastructure → ISV/App → Reseller/Channel → Implementation/Integration → Customer (Champion→Buyer→Users) → Customer Success → Renewal/Expansion

**Analysis**: PLG vs Sales-Led | Channel conflict | Implementation partner power | Customer LTV | Churn drivers

### B. E-Commerce/Marketplace

**Chain**: Supplier/Manufacturer → Inventory/Fulfillment → Platform → Payment → Logistics/Delivery → Customer → Returns/Support

**Analysis**: Take rate+unit economics | 1P vs 3P | Logistics costs | CAC | Supplier alignment

### C. Financial Services

**Chain**: Capital Provider → Financial Institution → Distribution → Advisor/Intermediary → Customer → Servicing/Operations → Regulatory/Compliance

**Analysis**: Regulatory barriers/moats | Distribution economics | Trust/brand | Tech modernization | Fintech disruption

### D. Healthcare

**Chain**: R&D → Manufacturing → Distributor → Provider (Hospital/Clinic) → Payer (Insurance) → Patient → Post-Care/Outcomes

**Analysis**: Payer-provider dynamics | Regulatory complexity | Patient experience vs economics | Data interoperability | Value-based care

### E. Manufacturing/Supply

**Chain**: Raw Materials → Component Suppliers → Manufacturer → Distributor/Wholesaler → Retailer → Customer → Service/Warranty

**Analysis**: Inventory optimization | Lead times+bullwhip | Quality control | Supplier relationship | D2C opportunities

## VII. Advanced Techniques

### A. Value Pool Analysis

**Method**: 1) Estimate industry revenue | 2) Calculate revenue/node | 3) Estimate margins/node | 4) Calculate profit pool (Revenue×Margin) | 5) Visualize (stacked bar)

**Q**: Where profit concentrated? High-value nodes vulnerable? Margins compressed why? Value distribution fair?

**Example**: $100B industry, $25B profit | Platform: $30B, 40%, $12B (48%) | Implementation: $25B, 15%, $3.75B (15%) → Platform captures 48% profit on 30% revenue (moat); implementation low margin (automation opportunity)

### B. Bottleneck (Theory of Constraints)

**Method**: 1) Map cycle time/node | 2) Identify longest/highest failure | 3) Calculate throughput capacity | 4) Find demand/capacity mismatch | 5) Estimate cost (lost revenue/churn)

**Application**: Identify (limit?), Exploit (max capacity), Subordinate (align pace), Elevate (expand), Repeat (next)

**Example**: Sales Engineering | Capacity: 10 SEs×4 evals/mo=40 deals/mo | Demand: 60 opps/mo | Cost: 20 lost×$150K ACV×30% win=$900K/mo | Solution: +5 SEs ($750K/yr) → $10M/yr gain

### C. Switching Cost Types + Analysis

**Types**: Financial (fees/setup/discounts lost) | Procedural (time/effort/learning) | Relational (relationship/trust/knowledge) | Contractual (legal/terms) | Technical (integration/migration/compatibility) | Risk (uncertainty/track record)

**Framework**: From→To | Cost components (amount/time/severity) | Total cost+risk | Annual savings | Payback period → Decision

**Example**: Salesforce→HubSpot | Migration $50K+Integration $150K+Training $30K+Productivity $200K+Risk $700K=$1.13M | Savings $120K/yr | Payback 9.4yr → unlikely unless forced | **Insight**: High switching=incumbent moat OR 10× better/free migration opportunity

### D. JTBD Mapping

**Method**: 1) Per participant: identify functional/emotional/social jobs | 2) Map performance vs desired | 3) Find underserved/overserved | 4) Find no-solution jobs

**Template**: Participant | Functional (what accomplish?) | Emotional (how feel?) | Social (how seen?) | Underserved (poor/none) | Overserved (too many)

**Example**: B2B Marketing Manager | Functional: leads/ROI/campaigns | Emotional: confidence/respect | Social: strategic not tactical | Underserved: attribution (poor), pipeline prediction (none), sales alignment (manual) | Overserved: social automation, email design → **Opportunity**: Pipeline Intelligence Platform

### E. Network Effects

**Types**: Direct (users→value) | Indirect (users→complements) | Data (usage→product) | Marketplace (buyers↔sellers) | Platform (developers→features)

**Q**: Which nodes benefit? Min viable network? Defensible? Engineer into product?

**Example**: Job Board | Type: Marketplace (2-sided) | Dynamic: seekers→employers→listings→seekers | Tipping: ~10M users before monetize | Defensibility: Medium (data+brand, multi-homing) | Winner: No (room for differentiation) → **Strategy**: Rapid acquisition to critical mass, then monetize; sequential geography

## VIII. Output Structure

| Artifact | Sections/Elements | Audience |
|----------|-------------------|----------|
| **A. Exec Summary** (1–2pg) | 1) Industry overview (size/growth/dynamics) \| 2) Chain structure (visual+description) \| 3) Key insights (3–5) \| 4) Top 3 opportunities (ranked) \| 5) Recommendation (next steps) | Leadership/investors/cross-functional |
| **B. Chain Map** (1pg visual) | Nodes (labeled) \| 3 flows (different arrows) \| Pain (red indicators+severity) \| Power (node size/styling) \| Opportunities (highlighted) \| Legend | Workshop/sharing |
| **C. Node Analysis** (10–30pg) | Per node: 1) Overview (function/scale/economics) \| 2) Participants (companies/roles) \| 3) Value add \| 4) Economics (model/margin/cost) \| 5) Pain (impact) \| 6) Dependencies (up/down) \| 7) Power (position) \| 8) Trends (evolution) \| 9) Opportunities | Product/strategy/BD |
| **D. Opportunity Portfolio** (5–10pg) | Per opp: 1) Description (problem/solution) \| 2) Market (TAM/SAM/SOM) \| 3) Target customer \| 4) Value prop (10×?) \| 5) Business model \| 6) Competition (alternatives/differentiation) \| 7) GTM \| 8) Financials (unit economics/3yr) \| 9) Risks (assumptions/mitigation) \| 10) Recommendation (pursue/monitor/pass) | Leadership/product/corp dev |
| **E. Roadmap** (1pg) | Now (0–3mo): quick wins/validation \| Near (3–12mo): launch \| Mid (1–2yr): scale \| Long (2–5yr): platform/ecosystem \| Milestones: decisions/resources/metrics | All stakeholders |

## IX. Pitfalls + Mitigations

| Pitfall | Symptom | Impact | Mitigation | Example |
|---------|---------|--------|------------|---------|
| **A. Incomplete Participants** | Missing behind-scenes players | Misunderstand power/miss risks | Interview ("Who else?"), follow money, check LinkedIn/associations | Miss system integrators (60% enterprise deals) |
| **B. Static Analysis** | Current only, no trends | Miss disruption/declining opps | Always Layer 3, map today+5yr, track tech adoption/regulatory/social | Taxi 2010 without smartphones → miss Uber/Lyft |
| **C. Activity≠Value** | All steps "add value" uncritically | Miss disintermediation | Ask "remove node→what breaks?", calculate value vs cost, interview downstream, find low-margin commodity | Distributor 15% markup for automatable logistics |
| **D. Single Stakeholder** | Only one view (often own company) | Miss pain/power, build unwanted solutions | Systematic multi-perspective, interview/survey types, map pain per participant, consider B2B2C | Build for end user, ignore admin/IT → low enterprise adoption |
| **E. No Quantification** | Qualitative only, no numbers | Can't prioritize/build case | Estimate (rough OK), Fermi, proxies, mark assumptions | "Slow" → "60d cycle, 40% longer, $500K/qtr delayed revenue" |
| **F. Ignore Coordination** | Node efficiency, miss handoff friction | Optimize parts, system slow | Map handoffs, time delays, identify misaligned incentives, calculate overhead | Manufacturing -20% time, no logistics coordination → inventory piles |

## X. Validation Checklist

| Category | Criteria |
|----------|----------|
| **Core Analysis** | ☑ All participants mapped \| ☑ 3 flows documented (info/product/capital) \| ☑ Economics estimated/node (revenue/margin/cost) \| ☑ Pain identified (severity+cost) \| ☑ Power mapped (switching costs) \| ☑ Tech+market trends researched \| ☑ 5yr state projected |
| **Cognitive Levels** | ☑ Remember: draw from memory \| ☑ Understand: explain logic \| ☑ Apply: ≥10 opportunities \| ☑ Analyze: compare+trade-offs \| ☑ Evaluate: rank with criteria \| ☑ Create: 1–2 novel models |
| **Quantification** | ☑ Industry size (revenue/volume) \| ☑ Value pool (profit distribution) \| ☑ Pain quantified (cost/time/frequency) \| ☑ Opportunity sized (TAM/SAM/SOM) \| ☑ Unit economics modeled \| ☑ Break-even+payback calculated |
| **Validation** | ☑ ≥3 sources cross-referenced \| ☑ ≥5 participants interviewed \| ☑ Hypotheses tested (experiments) \| ☑ Expert reviewed \| ☑ Assumptions documented \| ☑ Confidence assessed/finding |
| **Deliverables** | ☑ Exec summary (1–2pg) \| ☑ Chain map (visual) \| ☑ Node analysis doc \| ☑ Opportunity portfolio+recommendations \| ☑ Roadmap \| ☑ Presentation deck |

## XI. Example: B2B Marketing Chain

**Layer 1: Current** | **Chain**: Marketing (content/campaigns) → Website/Ads → Lead Capture → MQL Scoring → SDR → SQL → AE → Opp → Closed Won → CS | **Info Flow**: Campaign perf/engagement/behavior → BANT/score/history → Qual notes/pain/budget → Deal/decision-makers | Friction: incomplete CRM, no outcome visibility | **Capital**: Marketing spend → leads ($150/MQL) | Sales time → revenue ($600/SQL, $12K/win) | Customer pays | Friction: 6–18mo attribution delay, unclear ROI

**Layer 2: Pain+Power** | **P1 (High)**: 60% MQLs rejected | Causes: outdated scoring/ICP/timing | Cost: 30hr/wk+$150K/yr+friction | **P2 (High)**: Attribution blindness | Causes: no visibility/multi-touch | Cost: $500K/yr opportunity | **P3 (Med)**: Manual scoring misses intent | Cost: 15% vs 25% SQL conversion → $1M ARR gap | **Power**: High=Sales (reject/revenue control) | Med=Marketing (budget/brand) | Low=SDRs (squeezed)

**Layer 3: Change** | **Tech**: AI/ML scoring (6sense/Demandbase), intent data, automation (HubSpot/Marketo), ABM | **Market**: MQL→pipeline/revenue metrics, PLG, privacy (GDPR/CCPA), ROI pressure | **5yr**: AI Intent Engine → auto-route with context → personalized → AI optimizes spend | MQL/SQL friction eliminated

**Cognitive** | **1. Remember**: drew chain | **2. Understand**: MQL=handoff (Marketing volume, Sales quality); static rules miss intent | **3. Apply**: 3 opps (AI scoring, CRM integration, ABM) | **4. Analyze**: AI (high impact, complex) vs CRM (med impact, quick) vs ABM ($200K/yr, risky) | **5. Evaluate**: CRM first (trust), then AI (ROI, 18mo payback), defer ABM (immature) | **6. Create**: Revenue Intelligence Platform (intent+AI+attribution+account) | Eliminate MQL/SQL, measure on pipeline | $2B TAM

**Top Opportunity: AI Lead Scoring** | Replace rules with ML+intent | **Market**: TAM $8B automation, SAM $2B (>$50M revenue), SOM $100M (Y3, 5%) | **Target**: B2B SaaS $50M–$500M, 10+ reps, MQL quality issues | **Value**: 60%→30% reject (2× efficiency), 15%→25% SQL (1.67× pipeline), 30% faster response, full attribution | **Model**: SaaS $3K–$15K/mo (volume+data) | **Competition**: 6sense ($200M ARR), Demandbase ($120M); differentiate: attribution, CRM, price; risk: crowded, 9–12mo cycles | **GTM**: Mid-market (underserved), PLG trial, enterprise ABM | **Economics**: CAC $25K (6mo, $50K AER, 50%), LTV $150K (3yr, 70% margin), 6:1, 6mo payback | **Risks**: CRM hygiene (cleaning service), privacy (first-party), ML (API partners) | **Rec**: MVP with 5 partners (6mo), validate 2× improvement, Series A

# Investigate Q&A & Case Report Generator

**Purpose**: Generate 4–6 investigative Q&As analyzing one multi-actor case (incident, regulatory action, industry pattern, systemic failure), explaining what happened, why, and implications for decisions.

**Scope**: One case from background to present (+ optional 1–3 year outlook) across ≥2 dimensions (technical, business, ecosystem, regulatory, organizational, geographic). Must involve ≥3 actors/factors.

**Output**: 4–6 Q&As (150–250 words each) + case-summary paragraph; each Q&A addresses one investigation angle across multiple actors/factors.

**Validity**: 6–12 months until new evidence, major shifts, or regulatory changes require re-run.

**Users**: PM, architect, engineer, researcher, founder, investor, risk manager, compliance, regulator, technical writer.

**Terms**:
- **Case**: Bounded situation with clear temporal/contextual boundaries
- **Actor**: Entity influencing outcomes (company, protocol, DAO, regulator, user group)
- **Factor**: Structural variable shaping outcomes (leverage, governance, legal regime, liquidity)
- **Angle**: Investigation dimension (incentives, causal chain, industry structure, systemic risk)

## Minimal Workflow (80/20)

**5 steps to produce a reliable investigation in minimal time:**

1. **Define**: Case title, time span, decision context (enter/invest/build/partner/monitor/pivot/exit/regulate), 3–5 critical questions, hypotheses to test
2. **Map**: Background + ≥3 key events + ≥3 actors/factors (firms, protocols, regulators, segments, structural variables)
3. **Write**: 4–6 Q&As (see Q&A Template); each covers ≥2 dimensions, references ≥2–3 actors/factors, includes ≥1 citation
4. **Visualize**: 1 table summarizing events/years/actors/factors/impacts (or add timeline/network diagram)
5. **Validate**: Confirm background→present coverage, main causal story + alternatives, ≥5 citations from ≥3 types

**Target**: Reduce investigation time by ≥60% vs ad-hoc search.

## LLM Prompt Requirements

**Required context** (self-contained in single prompt):
- **Case**: Title, 1–2 sentence description with scale (market size, TVL, users, geographies)
- **Time span**: Background→present (+ optional 1–3 year outlook); note key periods/shocks
- **Decision**: Context and roles (PM/Architect/Investor/Risk/Compliance), constraints (capital, risk appetite, regulatory)
- **Actors/factors**: ≥3 mandatory (protocols, venues, jurisdictions, segments, leverage, custody model); LLM may add more
- **Hypotheses**: ≥2 competing explanations to test (e.g., "liquidity crisis vs governance failure")
- **Questions**: 3–5 critical, time-bounded questions about the *case*, not single objects
- **Preferences**: Language mix, max length, source types, research time

**Exclude**: External references ("see other file"), unsourced speculation >3–5 years, single-object narratives.

## Standards

### Coverage
- **Angles** (4–6 Q&As): Background (1), Actors/Incentives (1–2), Causal Chain (1), Impact/Outlook (1–2)
- **Citations**: ≥5 total, ≥3 types (research, standards, news, vendor docs, regulatory filings), 50–70% EN / 20–40% ZH / 5–15% other; APA 7th with language tag; inline as `[Ref: ID]`
- **References**: Glossary ≥6 terms, Tools ≥3, Literature ≥3 (≥1 ZH)
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
- ≥3 structural insights (how industry/ecosystem/regulatory/organizational structure shaped outcomes)
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
6. **Decision-aligned**: Connects to enter/invest/build/partner/monitor/pivot/exit/regulate/mitigate
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
**Actors/factors**: [≥2–3 companies/protocols/venues/DAOs/regulators/segments/forces]  
**Hypothesis**: [What this tests or explains]  
**Decision**: [Enter/Invest/Build/Partner/Monitor/Pivot/Exit/Regulate/Mitigate] – [Why critical]  
**Priority**: [Critical/Important/Optional]  
**Key Insight**: [1 sentence: pattern/mechanism/failure]

**Answer** (150–250 words, include ≥1 `[Ref: ID]`):
- **When/where**: Dates, locations, segments, scale (market share %, funding, TVL, DAU, volumes, scope)
- **Who/what**: Actors, decisions, events; 1–2 metrics per key actor/factor
- **How**: Causal chain/feedback loops (e.g., leverage + illiquidity + governance gaps)
- **Why**: Competing narratives; how evidence supports/challenges each
- **So what**: Implications for structure/risk/economics/regulation; decision thresholds
- **Perspectives**: ≥2 stakeholder viewpoints (regulator vs operator, incumbent vs entrant, retail vs institutional)

**Artifact** *(optional)*: Timeline, causal diagram, network map, comparison table  
**Confidence**: [High/Medium/Low] – [Evidence strength, uncertainties, gaps, contested points]

### Reference Formats

Prioritize recent primary sources (last 5–10 years) for current events; older sources for background; flag secondary/uncertain sources.

- **Glossary**: `G#. Term (Acronym)` | Definition | Use cases | Related | Limitations (alphabetized)
- **Tools**: `T#. Name (Category)` | Role | Pricing | Users/scale | Latest update | Integrations | Notes | URL (grouped by category)
- **Literature**: `L#. Author, Title, Year` | Summary | Relevance (grouped by language: EN, then ZH)
- **Citations**: `A#. [Citation] [Lang]` | APA 7th with language tag

## Example

**Q1: What chain of incentives, structural factors, and failures led to the collapse of an over-leveraged centralized exchange, and what does this reveal about CEX risk patterns (2017–2022)?**

**Angle**: Causal chain  
**Timeframe**: 2017–2022 | **Regions/Segments**: Global (US/EU/Offshore; retail + institutional)  
**Actors/factors**: Exchange management, trading affiliates, venture/credit providers, regulators, auditors, retail users, leverage/collateral practices  
**Hypothesis**: CEX collapses follow repeatable pattern: leverage + opacity + governance failures → hidden fragility  
**Decision**: Exit / Regulate / Mitigate – Structural risk patterns blocking expansion/reliance on opaque CEXs  
**Priority**: Critical – Directly informs custody/liquidity decisions  
**Key Insight**: Related-party trading + opaque balance sheets + weak oversight + cheap leverage = brittle system failing under stress

**Answer** (≈220 words):
In the late 2010s, cheap capital and a search for yield allowed centralized exchanges to grow rapidly by offering high leverage, proprietary tokens, and cross‑margin products that blurred lines between spot, derivatives, and collateral [Ref: A1]. Some exchanges created tightly coupled ecosystems in which their own tokens, affiliated market‑makers, and internal lending desks recycled liquidity, masking concentration and maturity mismatch risks [Ref: A2]. Governance was often founder‑centric, with limited board oversight, weak segregation between client and proprietary funds, and opaque disclosure practices, especially in offshore jurisdictions with lighter supervision [Ref: A3].

When macro conditions tightened and asset prices fell, these structures amplified stress. Declining token prices eroded collateral values, triggering margin calls and forced liquidations that further depressed markets [Ref: A4]. Rumors and on‑chain flows sparked bank‑run dynamics: large withdrawals exposed liquidity gaps, revealing that client assets were rehypothecated or pledged as collateral. Regulatory actions, investigative reporting, and bankruptcy filings then surfaced related‑party loans, missing assets, and control failures, crystallizing losses for users and counterparties [Ref: A5]. The investigative signal: centralized exchanges that combine trading, custody, lending, and token issuance without transparency, independent risk controls, or meaningful regulation create repeatable systemic risk patterns, even when brands and jurisdictions differ.

**Artifact**:

| Step                          | Years     | Key actors/factors                                | Impact                                          |
|-------------------------------|-----------|---------------------------------------------------|-------------------------------------------------|
| Leverage‑driven expansion     | 2017–2020 | CEXs, venture funds, high‑leverage products       | Rapid growth, complex risk hidden in structures |
| Liquidity stress & price shock| 2021–2022 | Falling token prices, margin calls, bank‑run fears| Collateral erosion, forced liquidations          |
| Failure & investigations      | 2022–2023 | Regulators, courts, users, auditors               | Insolvency, losses, new regulatory scrutiny     |

**Confidence**: Medium (strong evidence from filings and journalism; some details remain sealed or disputed).

## Pre-Flight Check (30s)

Before generating or using an investigation:
- **Prompt**: Case + time span + decision context + stakeholders + ≥2 hypotheses + 3–5 questions; self-contained (no external refs)
- **Q&As**: Follow Q&A Template; 4–6 total mapping to angle coverage; 150–250 words, ≥1 citation, explicit time/region, ≥2–3 actors/factors
- **Standards**: Meet Coverage + Quality Gates + Success Metrics
- **Balance**: For controversial cases, facts vs interpretation clear, opposing views presented, uncertainties flagged; decision implications explicit

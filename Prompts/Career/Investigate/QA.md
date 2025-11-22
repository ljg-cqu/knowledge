# Investigate Q&A & Case Report Generator

**Purpose**: Produce investigative Q&As and a structured case report for one *investigation case* (for example an industry situation, multi‑actor incident, ecosystem configuration, regulatory crackdown, or systemic failure), explaining how multiple related actors, objects, and factors interact over time, what happened, why, and with what implications.

**Scope**: One investigation case per run, from earliest relevant background to present (+ optional 1–3 year outlook) across technical, business, ecosystem, regulatory, organizational, and geographic lenses. The case must involve multiple key objects/factors (for example several companies, protocols, products, regions, user segments, or policies); never limit the analysis to a single-object biography.

**Output**: 4–6 investigative Q&As plus one integrated case-summary paragraph in the Case Overview & Scope section; each Q&A centers on a major *investigation angle* (for example incentives & power, causal chain of an incident, industry structure, regulatory game, or systemic risk) that cuts across several actors and factors.

**Validity**: Typically 6–12 months, until new evidence, major incidents, structural industry shifts, or regulatory regime changes emerge; then re-run.

**Stakeholders**: Product, technical, strategy, risk, finance, and policy roles needing a concise, accurate big-picture reconstruction (for example PMs, architects, engineers, researchers, founders, investors, risk managers, compliance, regulators, technical writers).

**Constraints**: 150–250 words per answer; ≥70% answers with citations; 100% Q&As anchored in explicit time ranges (years/dates) and, where relevant, locations/regions/segments. Each answer should mention ≥2–3 concrete actors or factors (companies, products, protocols, regulators, user segments, structural forces) unless the case is extremely narrow.

**Assumptions**: Prompt specifies the investigation case, rough time span, and decision context; public sources exist; output is text with optional diagrams and tables.

**Exclude**: Speculation beyond 3–5 years, unsourced rumors, trivia, generic definitions without time/space context, and single-object narratives that do not synthesize across multiple actors or factors.

**Terms**:
- **Investigation**: Evidence-based reconstruction and explanation of a complex situation involving multiple actors and factors, not a simple single-object timeline.
- **Case**: A bounded situation, event, pattern, or configuration (for example an exchange collapse, a regulatory campaign, an industry price war, or a miner–protocol conflict) that can be described with clear temporal and contextual boundaries.
- **Actor**: An entity that takes decisions or exerts influence in the case (for example company, protocol, DAO, regulator, cartel, user group, infrastructure provider).
- **Factor**: A structural condition or variable that shapes outcomes (for example leverage, fee model, liquidity concentration, governance design, legal regime, macro environment).
- **Critical Question**: A decision-critical or interpretation-critical question whose answer significantly influences whether to enter, invest, build, partner, regulate, pivot, or exit.

## LLM Prompt Context Checklist

Before you ask an LLM to generate an Investigate report, include at least:
- Case title and 1–2 sentence description (industry/domain, main incident or pattern, affected segments, maturity), including scale indicators where available (for example market size, user counts, TVL, volumes, geographies, revenue range).
- Time span to cover (background→present, or explicit years) and whether to add a 1–3 year outlook; call out any periods, shocks, or transitions you especially care about.
- Decision context and stakeholder roles (for example enter/invest/monitor/pivot/exit/regulate decision for PM + Architect + Investor + Risk/Compliance), plus current baselines or constraints they face (for example capital, risk appetite, regulatory limits).
- Key actors, exemplars, and factors that must be covered (for example specific protocols, venues, jurisdictions, user segments, or structural variables such as leverage, custody model, or collateral design); allow the LLM to add more when necessary.
- Suspected hypotheses or storylines to test (for example "Was this primarily a liquidity crisis or a governance failure?"); make clear that the LLM must contrast alternative explanations, not just confirm one narrative.
- Constraints and preferences (language mix, maximum length, tools to favor/avoid, time available for research, sources to prefer/avoid).
- 3–5 critical questions you want the investigation to answer, each phrased as a single, time-bounded ask about the *case* or *situation*, not just one object.
- Optional for training/education-focused runs: state an approximate difficulty mix for the investigation outputs (for example ~20% foundational background, ~50% intermediate analysis, ~30% advanced/edge cases) so the LLM can balance explanation depth.

**Self-contained prompt requirement**: When building an LLM prompt from this template, paste all necessary instructions and context into a single prompt. Do not rely on references such as “see other file”, “see previous answer”, or external memory.

## Guidelines

### Quantitative Guidelines
- **Q&A units**: 4–6 investigative Q&As covering ≥2 dimensions
- **Coverage**:
  - Background & Framing (1 Q&A)
  - Actors, Incentives & Relationships (1–2 Q&As)
  - Causal Chain, Mechanisms & Evidence (1 Q&A)
  - Impact, Accountability & Outlook (1–2 Q&As)
- **References (full run)**: Glossary ≥6 terms, Tools/Platforms ≥3, Literature/Reports ≥3 (≥1 ZH), Citations ≥5 in APA 7th format. For minimal runs, see **Minimal Core Workflow (80/20)**
- **Visuals (full run)**: ≥1 overall timeline or causal-chain/network diagram and ≥1 table summarizing actors/factors, events, and impacts. For minimal runs, a single shared table is sufficient (see **Minimal Core Workflow (80/20)**)

### Citation Standards
- **Format**: APA 7th with language tag. Inline citation form: `[Ref: ID]`
- **Distribution**: 50–70% EN, 20–40% ZH, 5–15% other languages
- **Types**: ≥3 citation types

### Process
1. **Define case & investigative goals**: Specify the case, boundaries, time span, primary perspectives (technical, business, ecosystem, regulatory, geographic, organizational), decision context (enter/invest/expand/monitor/pivot/exit/regulate/expose/mitigate), and key stakeholders. List initial hypotheses and mandatory actors/factors to examine.
2. **Build references**: Create glossary, tools/platforms, literature/reports, and citations covering background, triggers, cascades, interventions, and outcomes across major regions/segments.
3. **Map actors, factors, and timeline**: Identify major actors and structural factors; build a minimal timeline of key events (background, triggers, cascades, interventions) with dates/locations; map who did what, when, and under which conditions.
4. **Generate Q&A**: For each question, focus on one investigation angle; explain what happened, who was involved, how factors interacted, why outcomes emerged, and what alternative explanations exist; connect angles to each other.
5. **Create visuals**: For a full run, produce at least one combined timeline/causal-chain or network diagram and one actor/factor–event table; for a minimal run, a single shared table is sufficient. Reference visuals in the answers.
6. **Populate references**: Format glossary, tools/platforms, literature/reports, and citations as in section **D. Reference Formats**.
7. **Validate**: Check floors and quality gates (temporal coverage, source diversity, coherence, multi-actor coverage).
8. **Final review**: Ensure clarity, narrative flow, fairness across perspectives, and decision usefulness (for example where and how to enter, invest, build, partner, regulate, pivot, exit, or mitigate risk).

### Minimal Core Workflow (80/20)

Use this when time is limited; focus on minimal steps that still produce a reliable investigation.

1. **Define focus**: Choose the case and time span; note decision context, stakeholders, initial hypotheses, and 3–5 critical questions you want the investigation to answer.
2. **Construct a minimal event & actor map**: Identify background plus ≥3 key events and ≥3 central actors or factors (for example key firms, protocols, regulators, user segments, or structural variables).
3. **Write 4–6 Q&As**: Use the format in section **C. Q&A Format**; ensure each answer is time-bounded, covers at least 2 dimensions, and references ≥2–3 actors or factors.
4. **Create 1 shared artifact**: At minimum, a single table summarizing events, years, main actors/factors, and impacts; optionally add a simple timeline or network diagram.
5. **Run a quick validation**: Confirm background → present with no major blind spots; that you can state the main causal story and major alternative explanations; and that you have ≥5 citations from ≥3 types.

### Quality Gates

Failing any gate ⇒ stop and fix before using the output.
1. **Temporal coverage**: The investigation spans from earliest relevant background (or first widely recorded milestone) to present with no unexplained multi-year gaps around major triggers, cascades, or interventions.
2. **Source diversity**: ≥3 citation types (for example research, standards/specs, news/case studies, vendor or project documentation, regulatory filings).
3. **Evidence per major angle**: Each major investigation angle or critical event cluster has ≥2 authoritative references; highly controversial claims have ≥2 independent sources where possible.
4. **Actor / factor coverage**: The case includes all obviously central actors and structural factors (for example main firms, key protocols, core venues, pivotal regulators, critical user segments). If an important actor/factor cannot be covered, mark this explicitly as a gap.
5. **References**: All links are accessible; citation IDs are consistent across answers and the reference section.
6. **Chronological coherence**: Dates, sequences, and narratives align across Q&As, diagrams, and tables (no conflicting timelines).
7. **Verification & balance**: Cross-check dates, figures, and citations; for controversial cases, distinguish facts from interpretation, present major opposing views where relevant, and flag uncertainties.

## Success Criteria
- **Completeness**: Background plus ≥3 key events or clusters (triggers, cascades, interventions, outcomes) and (if relevant) ≥1 structural pattern or systemic risk clearly described
- **Temporal clarity**: ≥70% paragraphs mention concrete years/dates or clear time ranges
- **Structural insight**: ≥3 mentions of how industry, ecosystem, regulatory, or organizational structure shaped incentives and outcomes (not just a sequence of events)
- **Decision support**: Reader can summarize what the case reveals about the underlying system (for example risk patterns, power structures, opportunity windows) and how that should shape enter/invest/build/partner/regulate/pivot/exit decisions
- **Decision-critical focus**: ≥3 Q&As focus on angles that materially affect these decisions
- **Citation use**: ≥70% answers include ≥1 citation

Target: reduce investigative case research time by ≥60% vs ad-hoc web search.

## Question Quality
Rewrite any question that fails ≥2 checks.
1. **Clarity**: Single, time-bounded ask about the *case* or one investigation angle (for example "What chain of incentives and failures led to X between 2019–2022?")
2. **Temporal focus**: Clearly specifies a time window, set of events, or slice of the case
3. **Causality**: Asks for why outcomes occurred and how actors/factors interacted, not just what changed
4. **Perspective depth**: Invites ≥2 dimensions (for example technical + ecosystem, business + regulatory, incentives + governance) and synthesis across multiple actors or factors
5. **Signal over trivia**: Targets real structural issues, failures, or patterns, not minor version bumps or isolated anecdotes
6. **Decision-alignment**: Connects investigation results to enter/invest/build/partner/monitor/pivot/exit/regulate/mitigate choices where relevant
7. **Fairness**: For controversial cases, invite multiple perspectives (for example incumbent vs entrant, regulator vs operator, retail vs institutional) and highlight uncertainties
8. **Self-contained context**: Either the question itself or the shared prompt preamble explicitly names the case, timeframe, relevant regions/segments, and the decision hook so the LLM does not need to infer missing context

## Output Format

### A. TOC
1. Case Overview & Scope
2. Investigation Q&As by Angle
3. Visuals (Timelines, Maps, Networks, Tables)
4. References (Glossary, Tools/Platforms, Literature/Reports, Citations)
5. Validation Report

### B. Angle Overview
**Total Q&As**: [4–6] | **Coverage**: Background → Present (plus optional 1–3 year outlook) | **Dimensions**: Technical, Business, Ecosystem, Regulatory, Organizational, Geographic.

| Angle / Theme | Range | Count | Time span | Primary dimensions | Example artifacts |
|---|---|---|---|---|---|
| Background & Early Context | Q1 | 1 | [YYYY–YYYY] | History, structure, regions | Timeline + background table |
| Actors, Incentives & Relationships | Q2–Q3 | 1–2 | [YYYY–YYYY] | Actors, incentives, power | Network map + actor–incentive matrix |
| Causal Chain, Mechanisms & Evidence | Q4 | 1 | [YYYY–YYYY] | Tech, market, governance, process | Causal-chain diagram + event/impact table |
| Impact, Accountability & Outlook | Q5–Q6 | 1–2 | [YYYY–YYYY+] | Impact, risk, strategy, policy | Impact matrix + scenarios / lessons table |
| | **Total** | | **4–6** | **multi-dimensional** | **compressed** |
For each major issue or shock, choose a single primary investigation angle. Treat domain-wide shocks as part of **Causal Chain, Mechanisms & Evidence** unless the question is primarily about long-run impact or lessons.

### C. Q&A Format

**Investigation angle / Theme type**: [Background / Actors & incentives / Causal chain / Impact & fallout / Lessons & patterns]

**Q#: [Full question]**

**Timeframe**: [Years / specific dates] | **Regions/Segments (if any)**: [Global / CN / US / EU / etc.]

**Core actors/factors**: [Key companies/protocols/venues/DAOs/regulators/user segments/structural forces].

**Hypothesis / Focus**: [Short statement of what this Q&A is trying to test or explain].

**Decision relevance**: [Enter / Invest / Expand / Build / Partner / Monitor / Pivot / Exit / Regulate / Expose / Mitigate] – [Short justification, especially for decision-critical angles].

**Priority**: [Critical / Important / Optional] – [How much this Q&A should influence the current decision].

**Key Insight**: [1 sentence – specific pattern, mechanism, or failure being highlighted.]

**Answer** (150–250 words):
- When & where: key dates, locations, segments, and (where available) scale indicators (for example market share %, funding $, TVL, DAU, liquidation volumes, enforcement scope)
- Who & what: main actors and decisions/events, including 1–2 concrete metrics or examples per key actor/factor
- How factors interacted: causal chain or feedback loops (for example leverage + illiquidity + governance gaps), including reinforcing or mitigating mechanisms
- Why interpretations differ: competing narratives or explanations, and how evidence supports or challenges them
- So what: implications for structure, risk, economics, or regulation; connect to specific thresholds or decision points
- Risk, value, and perspectives: brief comparison of at least two stakeholder viewpoints or archetypes (for example regulator vs operator, incumbent vs entrant, retail vs institutional)
- ≥1 `[Ref: ID]` pointing to the reference section

**Artifact** *(optional)*: Timeline snippet, causal-chain diagram, network/relationship map, or case comparison table.

**Confidence**: [High / Medium / Low] – [Short note on evidence strength, major uncertainties, missing data, or contested points].

### D. Reference Formats

Prioritize recent, primary sources for current phases and outcomes (ideally from the last 5–10 years); use older sources for background and structural context, and flag secondary or uncertain sources explicitly.

**Glossary**: `G#. Term (Acronym)` | Definition | Use cases | Related concepts | Limitations. Alphabetize by term

**Tools/Platforms**: `T#. Name (Category)` | Role in lifecycle or case (core implementation, infra, analytics, ecosystem, venue) | Pricing | Users/scale | Latest update (Q# YYYY) | Key integrations | Investigation notes | URL; group by category

**Literature/Reports**: `L#. Author, Title, Year` | Summary (focus/framework/findings) | Relevance to the case or to similar cases/domains | Group by language (EN first, then ≥1 ZH)

**Citations**: `A#. [Citation] [Lang]` | APA 7th format with language tags

## Example

**Q1: What chain of incentives, structural factors, and failures led to the collapse of an over-leveraged centralized exchange, and what does this reveal about CEX risk patterns (2017–2022)?**

**Investigation angle / Theme type**: Causal chain (primary; impact & fallout secondary)

**Timeframe**: 2017–2022 | **Regions/Segments**: Global (US/EU/Offshore jurisdictions; retail + institutional)

**Core actors/factors**: Exchange management and trading affiliates, venture/credit providers, regulators, auditors, retail users, leverage and collateral practices.

**Hypothesis / Focus**: Many centralized exchange collapses follow a repeatable pattern of leverage, opacity, and governance failures that create hidden fragility.

**Decision relevance**: Exit / Regulate / Mitigate – Highlights structural risk patterns that should block unchecked expansion or reliance on opaque CEXs.

**Priority**: Critical – Directly informs whether to entrust custody or liquidity to similar exchanges.

**Key Insight**: Shows how related‑party trading, opaque balance sheets, and weak oversight combined with cheap leverage to create a brittle system that failed under stress, illustrating systemic CEX risks.

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

## Quick Check for Investigate Runs (30s)

Before sending an Investigate prompt to an LLM or using a generated investigation report for decisions, confirm that:
- **Context & questions**: The prompt satisfies the LLM Prompt Context Checklist and Minimal Core Workflow step 1 (case description, time span, decision context, stakeholders, hypotheses, and 3–5 critical questions)
- **Self-contained prompt**: The prompt meets the self-contained prompt requirement defined above
- **Per-Q&A structure**: Each Q&A follows section **C. Q&A Format** and the global Constraints
- **Coverage & angles**: The overall set meets the Quantitative Guidelines and Success Criteria, and each Q&A maps cleanly to one primary investigation angle from section **B. Angle Overview**
- **Evidence & references**: Citation practices meet **Citation Standards**, Quality Gates, and section **D. Reference Formats** (diverse, recent, and consistently labeled sources)
- **Balance & decision usefulness**: For controversial cases, apply Quality Gate 7 (verification & balance), and ensure the reader can see how each Q&A informs enter/invest/build/partner/monitor/pivot/exit/regulate/mitigate decisions

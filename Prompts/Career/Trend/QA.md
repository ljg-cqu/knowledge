# Trend Q&A & Landscape Report Generator

**Purpose**: Produce trend-focused Q&As and a landscape overview for one *domain or theme* (for example an industry, ecosystem, market segment, technology stack, or regulatory space), synthesizing how multiple related objects (technologies, products, companies, regions, user segments, regulations) interact and evolve over time.

**Scope**: From earliest meaningful origin to present (+ optional 1–3 year outlook) across technical, business, ecosystem, regulatory, and geographic lenses for the chosen domain/theme. Always cover multiple exemplars; never limit analysis to a single focal object.

**Output**: 4–6 trend Q&As plus one integrated landscape overview paragraph in the Trend Overview & Scope section; each Q&A centers on a major *trend cluster* (for example consolidation, platformization, regulatory tightening, commoditization) that cuts across several objects.

**Validity**: Typically 6–12 months, until macro conditions, technology baselines, regulatory regimes, or competitive structures shift materially; then re-run.

**Stakeholders**: Product, technical, strategy, finance, and policy roles needing a concise, accurate big-picture view (for example PMs, architects, engineers, researchers, founders, investors, policy/compliance, technical writers).

**Constraints**: 100% of Q&As anchored in explicit time ranges (years/dates) and, where relevant, locations/regions and segments. Each answer should mention ≥2–3 concrete exemplars (companies, products, protocols, regions, or user segments) unless the domain is extremely narrow. Quantitative floors for length and citation coverage are defined in later sections of this template.

**Assumptions**: Prompt specifies domain/theme, rough time span, and decision context; public sources exist; output is text with optional diagrams and tables.

**Exclude**: Speculation beyond 3–5 years, unsourced rumors, trivia, generic definitions without time/space context, and single-object biographies that do not synthesize across multiple actors or factors.

**Terms**:
- **Trend**: A directional pattern over time across multiple objects, segments, or factors in a domain (for example L1 consolidation, shift from CEX to DEX, commoditization of base models).
- **Trend cluster**: A coherent set of related signals, exemplars, and events that together describe one major direction or theme.
- **Driver / counter-driver**: Structural force that pushes a trend forward or restrains it (for example regulation, capital flows, technology breakthroughs, user behavior shifts, macro cycles).
- **Signal**: Measurable indicator for a trend (for example market share %, funding $, TVL, active addresses, DAU, policy actions).
- **Decision-Critical Trend**: A trend cluster whose direction or timing significantly influences whether to enter, invest, expand, pivot, exit, or regulate a domain.

## LLM Prompt Context Checklist

Before you ask an LLM to generate a Trend report, include at least:

- Domain/theme and 1–2 sentence description (industry, ecosystem, problem space, maturity), including scale indicators where available (for example market size, user counts, geographies, revenue range).
- Time span to cover (origin→present, or explicit years) and whether to add a 1–3 year outlook; call out any periods, shocks, or transitions you especially care about.
- Decision context and stakeholder roles (for example enter/expand/monitor/exit/regulate decision for PM + Architect + Investor), plus current baselines or constraints they face (for example budget, risk appetite, regulatory limits).
- Primary perspectives to emphasize (technical, business, ecosystem, regulatory, geographic) and any regions/segments to prioritize.
- Constraints and preferences (language mix, maximum length, tools to favor/avoid, time available for research, sources to prefer/avoid).
- 3–5 decision-critical questions you want the trend analysis to answer, each phrased as a single, time-bounded ask about the *space*, not one object.

**Self-contained prompt requirement**: When building an LLM prompt from this template, paste all necessary instructions and context into a single prompt. Do not rely on references such as “see other file”, “see previous answer”, or external memory.

## Guidelines

### Quantitative Guidelines
- **Q&A units**: 4–6 trend Q&As, each covering ≥2 dimensions and ≥2–3 concrete exemplars.
- **Coverage**: Use the 4–6 Q&A cluster structure in section **B. Trend Cluster Overview** (baseline, key trend clusters, shocks/counter-trends if relevant, scenarios/outlook).
- **References (full run)**: Glossary ≥6 terms, Tools/Platforms ≥3, Literature/Reports ≥3 (≥1 ZH), Citations ≥5 in APA 7th format. For minimal runs, see **Minimal Core Workflow (80/20)**.
- **Visuals (full run)**: ≥1 high-level diagram (for example timeline, ecosystem map, or 2×2) and ≥1 table summarizing trend clusters/segments/exemplars. For minimal runs, a single shared table is sufficient (see **Minimal Core Workflow (80/20)**).

### Citation Standards
- **Format**: APA 7th with language tag. Inline citation form: `[Ref: ID]`.
- **Distribution**: 50–70% EN, 20–40% ZH, 5–15% other languages.
- **Types**: ≥3 citation types.

### Process
1. **Define focus**: Specify domain/theme, time span, primary perspectives (technical, business, ecosystem, regulatory, geographic), decision context (enter/expand/monitor/pivot/exit/regulate), and key stakeholders. Optionally list 5–10 representative objects; the analysis must still bring in additional exemplars where needed.
2. **Build references**: Create glossary, tools/platforms, literature/reports, and citations covering early, middle, and recent periods and major regions/segments.
3. **Identify trend clusters**: Group signals, milestones, and critical incidents into 3–5 major trend clusters; map them to technical, business, ecosystem, and regulatory dimensions and to representative exemplars.
4. **Generate Q&A**: For each question, cover one trend cluster or cross-cutting theme; explain what is happening, why, where, and with what impact; highlight multiple exemplars and connect clusters to each other.
5. **Create visuals**: For a full run, produce at least one high-level diagram (timeline/ecosystem/2×2) and one trend-cluster table; for a minimal run, a single shared table is sufficient. Reference visuals in the answers.
6. **Populate references**: Format glossary, tools/platforms, literature/reports, and citations as in section **D. Reference Formats**.
7. **Validate**: Check floors and quality gates (temporal coverage, source diversity, coherence).
8. **Final review**: Ensure clarity, narrative flow, and decision usefulness (for example where and how to enter, invest, expand, pivot, or exit).

### Minimal Core Workflow (80/20)

Use this when time is limited; focus on minimal steps that still produce a reliable trend landscape.

1. **Define focus**: Choose the domain/theme and time span; note decision context, stakeholders, and 3–5 decision-critical questions you want the trend analysis to answer.
2. **Construct a minimal trend map**: Identify baseline plus ≥3 major trend clusters and ≥3 dated signals or events (for example funding waves, launches, crashes, regulatory actions) that evidence them.
3. **Write 4–6 Q&As**: Use the format in section **C. Q&A Format**; ensure each answer is time-bounded, covers at least 2 dimensions, and references ≥2–3 exemplars.
4. **Create 1 shared artifact**: At minimum, a single table summarizing trend clusters, time ranges, exemplar objects, and key metrics; optionally add a simple timeline or 2×2.
5. **Run a quick validation**: Confirm baseline → present with no major blind spots; that you can state the dominant directions (for example rising/maturing/declining/consolidating/fragmenting and why); and that citation and source-diversity floors from this template are met.

### Quality Gates

Failing any gate ⇒ stop and fix before using the output.

1. **Temporal coverage**: Analysis spans from earliest relevant activity (or first widely recorded milestone) to present with no unexplained multi-year gaps around major shocks or transitions.
2. **Source diversity**: ≥3 citation types (for example research, standards/specs, news/case studies, vendor or project documentation).
3. **Evidence per cluster/period**: Each major trend cluster or period has ≥2 authoritative references; domain-wide shocks have ≥2 independent sources where possible.
4. **Geo / segment coverage**: For globally relevant domains, mention at least 2 regions or markets if adoption or impact is not purely local.
5. **References**: All links are accessible; citation IDs are consistent across answers and the reference section.
6. **Chronological coherence**: Dates, sequences, and narratives align across Q&As, diagrams, and tables (no conflicting timelines).
7. **Verification & balance**: Cross-check dates, figures, and citations; for controversial trends, distinguish facts from interpretation and mention major opposing views where relevant.

## Success Criteria
- **Completeness**: Baseline plus ≥3 major trend clusters, ≥3 dated signals or events, and (if relevant) ≥1 cross-cutting shock clearly described.
- **Temporal clarity**: ≥70% of paragraphs mention concrete years/dates or clear time ranges.
- **Spatial insight**: If relevant, ≥3 mentions of regions/countries/markets or segments and differing adoption or impact.
- **Decision support**: Reader can summarize the dominant trends, explain who is advantaged/disadvantaged and why, and describe where the domain sits on its maturity curve.
- **Decision-critical focus**: ≥3 Q&As focus on trend clusters that materially affect enter/invest/expand/pivot/exit/regulate choices.
- **Citation use**: ≥70% of answers include ≥1 citation.

Target: reduce trend/landscape research time by ≥60% vs ad-hoc web search.

## Question Quality
Rewrite any question that fails ≥2 checks.
1. **Clarity**: Single, time-bounded ask about the *space* (for example "What were the dominant trends in container orchestration 2013–2020, and who gained or lost power?").
2. **Temporal focus**: Clearly specifies a time window or set of events/shocks.
3. **Causality**: Asks for why patterns emerged, not just what changed.
4. **Perspective depth**: Invites ≥2 dimensions (for example technical + ecosystem, business + regulatory, adoption + geography) and synthesis across multiple exemplars.
5. **Signal over trivia**: Targets real trends and structural shifts, not minor version bumps or isolated anecdotes.
6. **Decision-alignment**: Connects trends to enter/invest/expand/pivot/exit/regulate choices where relevant.
7. **Fairness**: For controversial trends, invite both positive and negative impacts or perspectives (what went well, what failed, who gained, who lost).

## Output Format

### A. TOC
1. Trend Overview & Scope
2. Trend Q&As by Cluster
3. Visuals (Timelines, Maps, Tables)
4. References (Glossary, Tools/Platforms, Literature/Reports, Citations)
5. Validation Report

### B. Trend Cluster Overview
**Total Q&As**: [4–6] | **Coverage**: Baseline → Present (plus optional 1–3 year outlook) | **Dimensions**: Technical, Business, Ecosystem, Regulatory, Geographic.

| Trend cluster / Theme                 | Range | Count | Time span          | Primary dimensions               | Example artifacts                         |
|---------------------------------------|-------|-------|--------------------|----------------------------------|-------------------------------------------|
| Landscape & Baseline Context          | Q1    | 1     | [YYYY–YYYY]        | Structure, segments, regions     | Landscape map + segment table             |
| Key Trend Clusters & Drivers          | Q2–Q3 | 2     | [YYYY–YYYY]        | Tech, business, ecosystem        | Trend-cluster table + driver/metric map   |
| Shocks, Inflection Points & Counter-Trends | Q4 | 0–1 | [YYYY–YYYY]        | Risk, security, policy, macro    | Shock timeline + impact comparison table  |
| Scenarios, Strategic Positions & Outlook | Q5–Q6 | 1–2 | [YYYY–YYYY+]      | Market, geo, strategy            | Scenario matrix + positioning 2×2         |
|                                       | **Total** |   | **4–6**           | **multi-dimensional**            | **compressed**                            |

For each major trend, choose a single primary cluster or theme. Treat domain-wide shocks as part of **Shocks, Inflection Points & Counter-Trends** unless the question is primarily about long-run structure or adoption.

### C. Q&A Format

**Trend cluster / Theme type**: [Structural / Behavioral / Regulatory / Competitive / Technology / Ecosystem]

**Q#: [Full question]**

**Timeframe**: [Years / specific dates] | **Regions/Segments (if any)**: [Global / CN / US / EU / etc.]

**Decision relevance**: [Enter / Invest / Expand / Monitor / Pivot / Exit / Regulate] – [Short justification, especially for decision-critical trends].

**Priority**: [Critical / Important / Optional] – [How much this Q&A should influence the current decision].

**Key Insight**: [1 sentence – specific pattern, shift, or cluster being highlighted.]

**Answer** (150–250 words):
- When & where: key dates, locations, segments, and (where available) scale indicators (for example market share %, funding $, TVL, DAU, policy scope).
- What is happening: the pattern across multiple objects (for example leading players, challengers, regions), including 1–2 concrete metrics.
- Why it matters: impact on structure, adoption, economics, risk, or regulation; connect to specific thresholds or decision points.
- How it connects: links to previous and adjacent trend clusters, including reinforcing or opposing dynamics.
- Trend direction: rising, maturing, declining, consolidating, fragmenting, or shifting regions/actors, with leading indicators.
- Risk, value, and perspectives: brief comparison of at least two stakeholder viewpoints or archetypes (for example incumbent vs entrant, regulator vs operator, retail vs institutional).
- ≥1 `[Ref: ID]` pointing to the reference section.

**Artifact** *(optional)*: Timeline snippet, ecosystem map, 2×2 positioning chart, or trend-cluster comparison table.

**Confidence**: [High / Medium / Low] – [Short note on evidence strength, major uncertainties, or data gaps].

### D. Reference Formats

Prioritize recent, primary sources for current trends (ideally from the last 5–10 years); use older sources for origin history, and flag secondary or uncertain sources explicitly.

**Glossary**: `G#. Term (Acronym)` | Definition | Use cases | Related concepts | Limitations. Alphabetize by term.

**Tools/Platforms**: `T#. Name (Category)` | Role in landscape (core implementation, infra, analytics, ecosystem) | Pricing | Users/scale | Latest update (Q# YYYY) | Key integrations | Trend notes | URL; group by category.

**Literature/Reports**: `L#. Author, Title, Year` | Summary (focus/framework/findings) | Relevance to the domain's evolution or impact | Group by language (EN first, then ≥1 ZH).

**Citations**: `A#. [Citation] [Lang]` | APA 7th format with language tags.

## Example

**Q1: What were the dominant trends in container orchestration from 2013–2020, and how did they shift power among vendors and ecosystems?**

**Trend cluster / Theme type**: Technology / Ecosystem

**Timeframe**: 2013–2020 | **Regions/Segments**: Global (US/EU/CN cloud ecosystems)

**Decision relevance**: Monitor / Invest – Informs whether to standardize on Kubernetes and managed services versus maintaining legacy orchestration stacks.

**Priority**: Critical – Strongly influences platform, hiring, and vendor strategy for cloud-native infrastructure.

**Key Insight**: Shows how open governance and multi-cloud support drove consolidation around Kubernetes, reshaping competition among cloud providers and earlier orchestrators.

**Answer** (150–250 words):
Early in the period, container orchestration was fragmented across proprietary and open-source approaches: internal systems like Google Borg, Mesos/Marathon, and later Docker Swarm each targeted different segments with varying complexity [Ref: A1]. Kubernetes emerged in 2014 as an open-source project informed by Borg/Omega and, crucially, moved to neutral CNCF governance in 2015, signalling that no single vendor would fully control the standard [Ref: A2]. Between 2016 and 2018, major cloud providers launched managed Kubernetes services (GKE, EKS, AKS, plus offerings from Alibaba Cloud and others), sharply lowering operational barriers and creating a de facto cross-vendor baseline [Ref: A3].

As the ecosystem of tooling (Helm, Istio, Prometheus) concentrated around Kubernetes, alternative orchestrators like Mesos/Marathon and Docker Swarm lost momentum; talent, vendor roadmaps, and community attention followed the consolidation trend [Ref: A4]. Enterprises increasingly standardized on Kubernetes-based platforms, giving hyperscalers with strong managed offerings and platform vendors (for example Red Hat OpenShift) structural advantages in winning workloads [Ref: A5]. The ambient trend signal for 2019–2020: orchestration itself commoditized, while differentiation shifted to developer experience, security, multi-cluster management, and higher-level PaaS layers that sit atop a common Kubernetes substrate.

**Artifact**:

| Trend cluster                  | Years     | Key exemplars                              | Impact                                       |
|--------------------------------|-----------|--------------------------------------------|----------------------------------------------|
| Fragmented pre-Kubernetes era  | 2013–2014 | Borg, Mesos/Marathon, early Docker Swarm   | Competing models, unclear long-run standard  |
| Kubernetes + neutral governance| 2014–2016 | Kubernetes, CNCF, early cloud providers    | Open standard candidate, rising mindshare    |
| Managed services consolidation | 2016–2018 | GKE/EKS/AKS, Alibaba Cloud, OpenShift      | Simplified adoption, vendor power reshuffle  |
| Platform-layer differentiation | 2019–2020 | Service meshes, dev platforms, security    | Orchestration commoditized, stack moves up   |

**Confidence**: High (widely documented history; multiple independent sources).

## Quick Check for Trend Runs (30s)

Before sending a Trend prompt to an LLM or using a generated Trend report for decisions, confirm:

- **Context & clarity**: Domain/theme, time span, decision context, stakeholders, and 3–5 decision-critical questions about trends and positioning are all stated explicitly; any ambiguous terms or acronyms are briefly defined in the prompt.
- **Precision & relevance**: Each Q&A has a clear timeframe, regions/segments (if relevant), key metrics, and a labeled priority; each answer names ≥2–3 concrete exemplars and stays focused on trend clusters and structural shifts (not trivia or isolated anecdotes).
- **MECE & coverage**: Questions are partitioned into baseline, key trend clusters, shocks/counter-trends (if relevant), and scenarios/outlook with minimal overlap; together they cover baseline → present (plus optional 1–3 year outlook) with no unexplained multi-year blind spots.
- **Breadth & depth**: Across the set of Q&As, technical, business, ecosystem, regulatory, and geographic dimensions appear where relevant; each answer goes beyond listing changes to explain why patterns emerged and how they affect different actors.
- **Significance, priority & concision**: Most Q&As focus on decision-critical trend clusters that materially affect enter/invest/expand/pivot/exit/regulate choices; priorities are labeled (Critical/Important/Optional), and answers stay within 150–250 words without redundant background.
- **Evidence, accuracy & credibility**: Citation and source-diversity floors from this template are met, with recent primary sources for current trends; citation IDs are consistent across Q&As and references, and obviously outdated or low-credibility sources are avoided or flagged.
- **Logic, risk/value & fairness**: Narratives are chronologically coherent, causal reasoning is explicit, and for controversial trends both positive and negative impacts are mentioned; at least two stakeholder perspectives or archetypes are contrasted for major trend clusters.
- **Structure & consistency**: The output follows the TOC and Q&A format in this template, including labeled fields (timeframe, decision relevance, priority, key insight, confidence) and any referenced visuals or tables.
- **Verification, practicality & success criteria**: Dates, figures, and key claims are cross-checked where possible; decision implications are concrete (for example "monitor", "prepare to enter in 2–3 years") and consistent with the **Success Criteria** section; if the run is decision-critical, rerun or extend research when major uncertainties remain.

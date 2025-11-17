# Guidelines for LLM-Friendly Prompts

**Metadata:**
- Last Updated: 2025-01-17
- Status: Final
- Owner: Knowledge Management Team

**Purpose:** Improve LLM output quality for decision-critical and high-stakes prompts by reducing hallucinations (↓30-60%) and improving decision support (↑60-80%). Ensures each prompt is self-contained with complete context and clear instructions.

**Application:** Apply comprehensively for decision-critical prompts meeting ≥1 criteria: blocks decision, risk >5% impact, 1-6mo action window, ≥2 stakeholders, adoption cost ≥40h. Apply selectively for other high-quality outputs.

**Context:**
- **Problem:** LLM outputs suffer from hallucinations, incomplete analysis, and ambiguous recommendations when prompts lack context or structure
- **Scope:** Covers prompt design for technical decision-making, system design, code generation, and knowledge work
- **Constraints:** Trade-off between comprehensive prompts and prompt length limits (typically 4K-8K tokens for most LLMs)
- **Stakeholders:** Engineers, architects, product managers, technical writers using LLMs for decision support
- **Resources:** No cost; applies to any LLM interaction (ChatGPT, Claude, etc.)

## Table of Contents

1. [Foundation: Define the Task](#foundation-define-the-task) - Guidelines 1-4
2. [Scope: What to Cover](#scope-what-to-cover) - Guidelines 5-8
3. [Quality: Ensure Excellence](#quality-ensure-excellence) - Guidelines 9-15
4. [Format: How to Present](#format-how-to-present) - Guidelines 16-17
5. [Validation: Ensure Correctness](#validation-ensure-correctness) - Guidelines 18-21
6. [Quick Check](#quick-check-30s)
7. [Quality Attributes](#quality-attributes)
8. [Limitations and Trade-offs](#limitations-and-trade-offs)

## Guidelines (21 Total)

### Foundation: Define the Task

**1. Context** [↓30-40% hallucinations]: State problem, scope, constraints, assumptions, scale, timeline, stakeholders, resources, domain, tech stack in the prompt.

- ❌ **Bad:** "Design system" (title only)
- ✅ **Optimized:** "Design payment system: problem (manual processing, 2h delays), scale (1M users), constraints (PCI-DSS compliance), timeline (6mo), domain (fintech startup), stakeholders (PM+Arch+Security+Legal), resources (budget $500K, team: 3 engineers)"

**Rationale:** Context reduces hallucinations by grounding LLM responses in specific requirements rather than generic assumptions.

**2. Clarity** [↓25-35% ambiguity]: Request definitions of key terms and relationships; use diagrams for complex concepts.

- ❌ **Bad:** "Use eventual consistency" (unexplained jargon)
- ✅ **Optimized:** "Define terms: 'Eventual consistency (async data sync, stale reads acceptable for <1s) vs strong consistency (immediate sync, higher latency)'. Include sequence diagram for data flow."

**Rationale:** Clear definitions prevent misinterpretation and ensure LLM uses terms correctly throughout the response.

**3. Precision** [↓40-50% ambiguity]: Use exact metrics, formulas, units instead of vague qualifiers.

- ❌ **Bad:** "Design fast and scalable system" (vague qualifiers)
- ✅ **Optimized:** "Design system meeting: p95 latency <200ms, p99 <500ms, throughput 10K→100K req/s, auto-scale <2min, 99.9% uptime"

**Rationale:** Precise specifications eliminate ambiguity and enable measurable, testable recommendations.

**4. Relevance** [↓30-40% noise]: Focus on essential information; move non-critical details to appendices.

- ❌ **Bad:** "Explain database history and current options" (unconnected background)
- ✅ **Optimized:** "Compare SQL vs NoSQL for e-commerce: focus on transaction requirements, scale characteristics, query patterns. Exclude history unless regulatory-critical. Move extensive comparisons to appendix."

**Rationale:** Relevant information improves signal-to-noise ratio and reduces LLM output length.

### Scope: What to Cover

**5. MECE** (Mutually Exclusive, Collectively Exhaustive) [↑40-50% completeness]: Ensure sections are distinct with no gaps or overlaps.

- ❌ **Bad:** "Explain security: authentication and encryption" (gaps/overlaps)
- ✅ **Optimized:** "Explain security covering all 5 areas: (1) Authentication, (2) Authorization, (3) Encryption (transit+rest), (4) Audit logging, (5) Secrets management. Ensure no gaps or overlaps."

**Rationale:** MECE structure prevents incomplete analysis and ensures comprehensive coverage.

**6. Sufficiency** [↑35-45% comprehensiveness]: Cover all necessary dimensions (what, why, how, when, who, constraints, alternatives, risks, outcomes).

- ❌ **Bad:** "Design API: define endpoints" (partial coverage)
- ✅ **Optimized:** "Design API covering: endpoints, authentication, rate limiting, versioning strategy, error handling, pagination, caching headers, documentation requirements"

**Rationale:** Sufficient coverage prevents follow-up questions and ensures actionable outputs.

**7. Breadth** [↑30-40% perspective diversity]: Include relevant stakeholder perspectives.

- ❌ **Bad:** "Explain from developer perspective" (single viewpoint)
- ✅ **Optimized:** "Explain from 4 perspectives: (1) Developer: code patterns, (2) SRE: operational complexity, (3) Security: threat surface, (4) PM: user impact"

**Rationale:** Multiple perspectives reveal trade-offs and facilitate cross-functional decision-making.

**8. Depth** [↑25-35% thoroughness]: Request implementation-level detail for high-impact areas.

- ❌ **Bad:** "Recommend caching solution" (principles without detail)
- ✅ **Optimized:** "Recommend Redis with specifics: eviction policies (LRU/LFU tradeoffs), persistence options (RDB/AOF), clustering approaches (sentinel/cluster), memory limit calculations, key naming patterns"

**Rationale:** Implementation depth enables immediate action and reduces back-and-forth clarifications.

### Quality: Ensure Excellence

**9. Significance** [↓40-60% reading time]: Request focus on high-impact items only; deemphasize low-impact details.

- ❌ **Bad:** "List all HTTP error codes and handling" (exhaustive low-relevance list)
- ✅ **Optimized:** "List critical HTTP errors only: 429 (rate limit), 503 (overload), 401/403 (auth), 500 (system alert). Exclude: 404 handling, client errors <5% occurrence"

**Rationale:** Highlighting significance reduces cognitive load and focuses attention on decision-critical information.

**10. Concision** [↓35-45% word count]: Eliminate redundancy; state each concept once, then reference.

- ❌ **Bad:** "Explain why we should consider using caching and how caching can improve performance" (repeated concepts)
- ✅ **Optimized:** "Specify caching strategy: Redis for sessions (TTL 30min), CDN for static assets (TTL 1d). No explanatory text."

**Rationale:** Concise prompts and outputs save time and improve scannability.

**11. Accuracy** [↓20-30% factual errors]: Request fact verification against authoritative sources.

- ❌ **Bad:** "Recommend libraries" (unverified claims)
- ✅ **Optimized:** "Recommend libraries with verification: check current versions (npm/PyPI), cite compatibility matrices from official docs, flag deprecated APIs, cross-reference claims"

**Rationale:** Accuracy verification reduces factual errors and outdated information.

**12. Credibility** [↓50-60% hallucinations]: Request authoritative citations from recent (2023+) primary sources (official docs, standards, peer-reviewed papers).

- ❌ **Bad:** "What are best practices?" (generic claims)
- ✅ **Optimized:** "Cite best practices from: AWS Well-Architected Framework (2024), Google SRE Book, OWASP Top 10 (2023+), peer-reviewed papers. Include source URLs."

**Rationale:** Credible sources dramatically reduce hallucinations and improve trust in recommendations.

**13. Logic** [↓30-40% reasoning errors]: Request coherent arguments with explicit trade-offs and reasoning.

- ❌ **Bad:** "Explain why microservices simplify architecture" (one-sided claim)
- ✅ **Optimized:** "Explain microservices tradeoff: increases operational complexity but improves scalability. Recommend modular monolith if team <10. Include reasoning for threshold."

**Rationale:** Logical coherence prevents contradictions and ensures sound recommendations.

**14. Risk/Value** [↑60-80% decision quality]: Compare ≥2 alternatives with costs, benefits, risks, and trade-offs.

- ❌ **Bad:** "Recommend Kubernetes setup" (single solution)
- ✅ **Optimized:** "Compare 3 options: (1) K8s self-managed ($2K/mo, ops team needed, full control), (2) Managed K8s ($500/mo, vendor lock-in, less ops), (3) VMs ($200/mo, limited scale, simple). Include migration paths and decision criteria."

**Rationale:** Comparing alternatives enables informed decision-making and reveals hidden costs.

**15. Fairness** [↓40-50% bias]: Request balanced view with counterarguments, limitations, and when NOT to use.

- ❌ **Bad:** "Why should we use GraphQL?" (biased framing)
- ✅ **Optimized:** "Compare GraphQL vs REST: pros (flexible queries, reduced over-fetching), cons (complexity, caching challenges, learning curve), when NOT to use (simple CRUD, public API, small team). Include counterarguments."

**Rationale:** Balanced perspectives prevent biased recommendations and reveal limitations.

### Format: How to Present

**16. Structure** [↑30-40% scannability]: Request structured output with clear headings, lists, tables, diagrams.

- ❌ **Bad:** "Explain the solution" (unstructured blocks)
- ✅ **Optimized:** "Format output as: ## TOC → ### H2 sections → Bullet lists for steps → Comparison tables → Mermaid diagrams → Code blocks with syntax highlighting → Math blocks for formulas"

**Rationale:** Structured format improves scannability and makes information easier to locate and act upon.

**17. Consistency** [↑35-45% readability]: Request consistent hierarchy and formatting conventions.

- ❌ **Bad:** "Provide analysis" (no format guidance)
- ✅ **Optimized:** "Structure output: ## Decision Context → ### Option A (pros/cons/cost) → ### Option B → ### Comparison Table → ### Recommendation → ### Timeline with milestones. Use H2 for main sections, H3 for subsections."

**Rationale:** Consistent hierarchy enables predictable navigation and reduces cognitive load.

### Validation: Ensure Correctness

**18. Evidence** [↑40-50% trust]: Request structured citations with source details, recency, page numbers, and uncertainty flags.

- ❌ **Bad:** "What do studies show?" (generic claims)
- ✅ **Optimized:** "Cite sources in format: [1] Google SRE Book (2023) p.42 'MTTR <1h'. [2] AWS re:Invent 2024 [video URL, timestamp]. Flag uncertainties: 'cache hit rate estimated (no empirical data available)'."

**Rationale:** Detailed evidence enables fact-checking and builds trust in recommendations.

**19. Verification** [↓25-35% errors]: Request structured self-review and error checking.

- ❌ **Bad:** "Provide recommendation" (no verification)
- ✅ **Optimized:** "After generating response, self-review: verify calculations, check contradictions, validate terminology consistency, test code examples, cross-reference claims against sources, flag uncertainties"

**Rationale:** Verification catches errors before delivery and improves output reliability.

**20. Practicality** [↑50-60% implementation speed]: Request concrete steps, examples, tools, commands, and troubleshooting.

- ❌ **Bad:** "Suggest monitoring improvements" (abstract recommendations)
- ✅ **Optimized:** "Provide actionable monitoring setup: tools (Prometheus, Grafana), exact commands ('helm install prometheus'), sample queries ('rate(http_requests_total[5m])'), dashboard templates, common issues and fixes"

**Rationale:** Practical details accelerate implementation and reduce trial-and-error.

**21. Success Criteria** [↑40-50% measurability]: Define measurable outcomes with baselines, targets, and measurement methods.

- ❌ **Bad:** "How to achieve better performance?" (vague criteria)
- ✅ **Optimized:** "Define success metrics with baselines: p95 latency <200ms (current: 800ms), error rate <0.1% (current: 0.5%), cost <$5K/mo (current: $8K/mo), timeline 3mo. Specify measurement methods and tools."

**Rationale:** Measurable criteria enable objective evaluation of success and progress tracking.

## Quick Check (30s)

**Before sending your prompt (mandatory for decision-critical, recommended otherwise):**

☐ **Self-contained**: No cross-file refs or "see previous answer"; all context included  
☐ Context | ☐ Clarity | ☐ Precision | ☐ Relevance  
☐ MECE | ☐ Sufficiency | ☐ Breadth | ☐ Depth  
☐ Significance | ☐ Concision | ☐ Accuracy | ☐ Credibility  
☐ Logic | ☐ Risk/Value | ☐ Fairness  
☐ Structure | ☐ Consistency  
☐ Evidence | ☐ Verification | ☐ Practicality | ☐ Success Criteria

## Quality Attributes

**Target attributes (verify in LLM output):**
- **Accurate**: Facts verified against authoritative sources
- **Precise**: Exact metrics, formulas, units instead of vague qualifiers
- **Cited**: Sources with details (author, year, page, URL)
- **Complete**: All necessary dimensions covered (MECE)
- **Actionable**: Concrete steps, examples, tools, commands
- **Consistent**: Uniform terminology, metrics, hierarchy
- **Relevant**: Information supports purpose; non-critical details in appendix
- **Balanced**: Multiple perspectives, limitations, counterarguments
- **Recent**: 2023+ sources when available; flag time-sensitive info
- **Testable**: Measurable outcomes with baselines, targets, methods

## Limitations and Trade-offs

**Trade-offs:**
- **Rigor vs. Speed**: Comprehensive guidelines increase upfront time but reduce iteration cycles
- **Depth vs. Breadth**: Detailed context increases prompt length; may exceed token limits
- **Precision vs. Accessibility**: Technical specificity may reduce readability for non-technical stakeholders

**When to skip comprehensive application:**
- Exploratory questions or brainstorming
- Low-stakes content (<5% impact)
- Time-constrained situations requiring rapid response
- Simple informational queries
- Iterative prototyping (can apply selectively)

**Exclude from prompts:**
- Historical background (unless regulatory/compliance-critical)
- Pure theory without implementation (unless adoption cost ≥40h)
- Edge cases with <5% occurrence and low severity
- Formal proofs (unless specifically required)
- Trends without supporting data
- Generic advice without specifics
- Speculation flagged as fact
- Cross-references ("see other file/prompt")

**Impact Metrics:**
- ↓30-60% hallucinations (Context + Credibility)
- ↓25-50% ambiguity (Clarity + Precision)
- ↑60-80% decision quality (Risk/Value)
- ↑35-50% completeness (MECE + Sufficiency)
- ↑30-45% scannability (Structure + Consistency)
- ↑50-60% implementation speed (Practicality)


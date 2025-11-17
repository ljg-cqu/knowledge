# Guidelines for LLM-Friendly Prompts

**Purpose:** Reduce hallucinations (↓30-60%), improve decision support (↑60-80%). Self-contained prompts with complete context and clear instructions.

**Application:** Apply comprehensively if meeting ≥1 criterion: blocks decision, >5% impact risk, 1-6mo action window, ≥2 stakeholders, ≥40h adoption cost. Apply selectively otherwise.

**Context:**
- **Problem:** Hallucinations, incomplete analysis, ambiguous recommendations from unstructured prompts
- **Scope:** Technical decisions, system design, code generation, knowledge work (excludes creative writing, casual chat, basic retrieval)
- **Constraints:** Prompt length limits (4K-8K tokens typical); assumes basic LLM familiarity
- **Assumptions:** Users iterate prompts; LLMs have domain knowledge; metrics from empirical observations (not controlled studies)
- **Scale:** Individual contributors to 50+ teams; 100-10,000 token prompts
- **Timeline:** Immediate use; 30-60s quality check; benefits accumulate
- **Stakeholders:** Engineers, architects, PMs, technical writers
- **Resources:** No cost; any LLM (ChatGPT, Claude, Gemini); no tools required

**Key Terms:**
- **Hallucination**: Factually incorrect or unverifiable information presented as fact
- **Decision-critical**: Content influencing decisions with >5% impact or blocking key actions
- **MECE**: Mutually Exclusive, Collectively Exhaustive - complete coverage without overlaps
- **Self-contained**: All necessary context included without external references or previous conversations
- **Impact metrics**: Estimated improvement (↑/↓) based on empirical observations

## Guidelines

### Foundation: Define the Task

**1. Context** [↓30-40% hallucinations]: State problem, scope, constraints, assumptions, scale, timeline, stakeholders, resources.

- ❌ "Design system"
- ✅ "Design payment system: problem (manual processing, 2h delays), scale (1M users), constraints (PCI-DSS), timeline (6mo), stakeholders (PM+Arch+Security+Legal), resources ($500K, 3 engineers)"

**Rationale:** Grounds responses in specific requirements vs. generic assumptions.

**2. Clarity** [↓25-35% ambiguity]: Define key terms and relationships; use diagrams for complex concepts.

- ❌ "Use eventual consistency"
- ✅ "Define: Eventual consistency (async sync, stale reads <1s) vs strong consistency (immediate sync, higher latency). Include sequence diagram."

**Rationale:** Prevents misinterpretation; ensures consistent term usage.

**3. Precision** [↓40-50% ambiguity]: Use exact metrics, formulas, units instead of vague qualifiers.

- ❌ "Design fast and scalable system"
- ✅ "Design system: p95 latency <200ms, p99 <500ms, throughput 10K→100K req/s, auto-scale <2min, 99.9% uptime"

**Rationale:** Eliminates ambiguity; enables measurable recommendations.

**4. Relevance** [↓30-40% noise]: Focus on essential information; move non-critical details to appendices.

- ❌ "Explain database history and current options"
- ✅ "Compare SQL vs NoSQL for e-commerce: transaction requirements, scale, query patterns. Exclude history. Move extensive comparisons to appendix."

**Rationale:** Improves signal-to-noise ratio; reduces output length.

### Scope: What to Cover

**5. MECE** (Mutually Exclusive, Collectively Exhaustive) [↑40-50% completeness]: Ensure sections are distinct with no gaps or overlaps.

- ❌ "Explain security: authentication and encryption"
- ✅ "Explain security: (1) Authentication, (2) Authorization, (3) Encryption (transit+rest), (4) Audit logging, (5) Secrets management. No gaps or overlaps."

**Rationale:** Prevents incomplete analysis; ensures comprehensive coverage.

**6. Sufficiency** [↑35-45% comprehensiveness]: Cover all necessary dimensions (what, why, how, when, who, constraints, alternatives, risks, outcomes).

- ❌ "Design API: define endpoints"
- ✅ "Design API: endpoints, authentication, rate limiting, versioning, error handling, pagination, caching headers, documentation"

**Rationale:** Prevents follow-up questions; ensures actionable outputs.

**7. Breadth** [↑30-40% perspective diversity]: Include relevant stakeholder perspectives.

- ❌ "Explain from developer perspective"
- ✅ "Explain from: (1) Developer (code patterns), (2) SRE (operational complexity), (3) Security (threat surface), (4) PM (user impact)"

**Rationale:** Reveals trade-offs; facilitates cross-functional decisions.

**8. Depth** [↑25-35% thoroughness]: Request implementation-level detail for high-impact areas.

- ❌ "Recommend caching solution"
- ✅ "Recommend Redis: eviction policies (LRU/LFU tradeoffs), persistence (RDB/AOF), clustering (sentinel/cluster), memory limits, key naming patterns"

**Rationale:** Enables immediate action; reduces clarifications.

### Quality: Ensure Excellence

**9. Significance** [↓40-60% reading time]: Focus on high-impact items only; deemphasize low-impact details.

- ❌ "List all HTTP error codes and handling"
- ✅ "Critical HTTP errors: 429 (rate limit), 503 (overload), 401/403 (auth), 500 (system alert). Exclude: 404, client errors <5% occurrence"

**Rationale:** Reduces cognitive load; focuses on decision-critical information.

**10. Concision** [↓35-45% word count]: Eliminate redundancy; state each concept once, then reference.

- ❌ "Explain why we should consider using caching and how caching can improve performance"
- ✅ "Caching strategy: Redis for sessions (TTL 30min), CDN for static assets (TTL 1d). No explanatory text."

**Rationale:** Saves time; improves scannability.

**11. Accuracy** [↓20-30% factual errors]: Verify facts against authoritative sources.

- ❌ "Recommend libraries"
- ✅ "Recommend libraries: verify current versions (npm/PyPI), cite compatibility matrices from official docs, flag deprecated APIs"

**Rationale:** Reduces factual errors and outdated information.

**12. Credibility** [↓50-60% hallucinations]: Cite recent (2023+) primary sources (official docs, standards, peer-reviewed papers).

- ❌ "What are best practices?"
- ✅ "Cite best practices: AWS Well-Architected Framework (2024), Google SRE Book, OWASP Top 10 (2023+). Include URLs."

**Rationale:** Credible sources reduce hallucinations; improve trust.

**13. Logic** [↓30-40% reasoning errors]: Provide coherent arguments with explicit trade-offs and reasoning.

- ❌ "Explain why microservices simplify architecture"
- ✅ "Microservices tradeoff: increases operational complexity but improves scalability. Recommend modular monolith if team <10. Include reasoning."

**Rationale:** Prevents contradictions; ensures sound recommendations.

**14. Risk/Value** [↑60-80% decision quality]: Compare ≥2 alternatives with costs, benefits, risks, trade-offs.

- ❌ "Recommend Kubernetes setup"
- ✅ "Compare: (1) K8s self-managed ($2K/mo, ops team, full control), (2) Managed K8s ($500/mo, vendor lock-in, less ops), (3) VMs ($200/mo, limited scale). Include migration paths."

**Rationale:** Enables informed decisions; reveals hidden costs.

**15. Fairness** [↓40-50% bias]: Provide balanced view with counterarguments, limitations, when NOT to use.

- ❌ "Why should we use GraphQL?"
- ✅ "GraphQL vs REST: pros (flexible queries, reduced over-fetching), cons (complexity, caching challenges), when NOT to use (simple CRUD, public API, small team)"

**Rationale:** Prevents biased recommendations; reveals limitations.

### Format: How to Present

**16. Structure** [↑30-40% scannability]: Use clear headings, lists, tables, diagrams.

- ❌ "Explain the solution"
- ✅ "Format: ## TOC → ### H2 sections → Bullet lists → Comparison tables → Mermaid diagrams → Code blocks with syntax highlighting → Math blocks"

**Rationale:** Improves scannability; easier to locate and act upon.

**17. Consistency** [↑35-45% readability]: Use consistent hierarchy and formatting conventions.

- ❌ "Provide analysis"
- ✅ "Structure: ## Decision Context → ### Option A (pros/cons/cost) → ### Option B → ### Comparison → ### Recommendation → ### Timeline. H2 for main, H3 for subsections."

**Rationale:** Enables predictable navigation; reduces cognitive load.

### Validation: Ensure Correctness

**18. Evidence** [↑40-50% trust]: Provide structured citations with source details, recency, page numbers, uncertainty flags.

- ❌ "What do studies show?"
- ✅ "Cite: [1] Google SRE Book (2023) p.42 'MTTR <1h'. [2] AWS re:Invent 2024 [URL, timestamp]. Flag: 'cache hit rate estimated (no empirical data)'."

**Rationale:** Enables fact-checking; builds trust.

**19. Verification** [↓25-35% errors]: Self-review and error checking.

- ❌ "Provide recommendation"
- ✅ "Self-review: verify calculations, check contradictions, validate terminology, test code, cross-reference claims, flag uncertainties"

**Rationale:** Catches errors before delivery; improves reliability.

**20. Practicality** [↑50-60% implementation speed]: Provide concrete steps, examples, tools, commands, troubleshooting.

- ❌ "Suggest monitoring improvements"
- ✅ "Monitoring setup: tools (Prometheus, Grafana), commands ('helm install prometheus'), queries ('rate(http_requests_total[5m])'), dashboards, common issues"

**Rationale:** Accelerates implementation; reduces trial-and-error.

**21. Success Criteria** [↑40-50% measurability]: Define measurable outcomes with baselines, targets, measurement methods.

- ❌ "How to achieve better performance?"
- ✅ "Metrics: p95 latency <200ms (current: 800ms), error rate <0.1% (current: 0.5%), cost <$5K/mo (current: $8K/mo), timeline 3mo. Specify tools."

**Rationale:** Enables objective evaluation; tracks progress.

## Quick Check (30s)

**Before sending (mandatory for decision-critical):**

☐ **Self-contained**: All context included; no cross-file refs  
☐ Context | ☐ Clarity | ☐ Precision | ☐ Relevance  
☐ MECE | ☐ Sufficiency | ☐ Breadth | ☐ Depth  
☐ Significance | ☐ Concision | ☐ Accuracy | ☐ Credibility  
☐ Logic | ☐ Risk/Value | ☐ Fairness  
☐ Structure | ☐ Consistency  
☐ Evidence | ☐ Verification | ☐ Practicality | ☐ Success Criteria

## Quality Attributes

**Accurate** | **Precise** | **Cited** | **Complete** (MECE) | **Actionable** | **Consistent** | **Relevant** | **Balanced** | **Recent** (2023+) | **Testable**

## Limitations and Trade-offs

**Trade-offs:**
- **Rigor vs. Speed**: Comprehensive guidelines increase upfront time but reduce iteration
- **Depth vs. Breadth**: Detailed context may exceed token limits
- **Precision vs. Accessibility**: Technical specificity may reduce readability

**When to skip / Exclude:**
- **Skip for**: Exploratory questions, brainstorming, low-stakes (<5% impact), rapid response, simple queries, prototyping
- **Exclude from prompts**: Historical background (unless regulatory-critical), pure theory (unless adoption ≥40h), edge cases (<5% occurrence), formal proofs, unsupported trends, generic advice, speculation, cross-references

**Impact Metrics - Limitations:**
- **Source**: ~50 sessions (ChatGPT-4, Claude 3.5, Gemini 1.5, 2024-2025); subjective assessment, no A/B testing
- **Baseline**: Unstructured conversational prompts
- **Uncertainty**: High (±20-40%); directional indicators only, not precise measurements
- **Use cautiously**: Apply based on principles, not solely metrics

**Estimated Ranges:**
↓30-60% hallucinations | ↓25-50% ambiguity | ↑60-80% decision quality | ↑35-50% completeness | ↑30-45% scannability | ↑50-60% implementation speed

## Document Verification

**Self-assessment:**
☑ Context, Clarity, Precision, Relevance, MECE, Sufficiency, Breadth, Depth, Significance, Concision, Accuracy, Logic, Fairness, Structure, Consistency, Verification, Practicality  
⚠ Credibility: Impact metrics lack external citations (limitations documented)  
⚠ Risk/Value: Single framework (alternatives not compared)  
⚠ Evidence: Observational metrics, not peer-reviewed (uncertainty flagged)  
⚠ Success Criteria: Qualitative only (no quantitative baselines)

**Gaps:** No alternative framework comparison; metrics lack rigorous validation; no measurable effectiveness criteria

**Future:** A/B testing, framework comparison, success criteria, user feedback

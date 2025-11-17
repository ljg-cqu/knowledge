# Guidelines for LLM-Friendly Prompts

**Purpose:** Reduce hallucinations (↓30-60%), improve decision quality (↑60-80%). Self-contained prompts with complete context.

**Application:** Apply comprehensively if ≥1: blocks decision, >5% impact, 1-6mo timeline, ≥2 stakeholders, ≥40h adoption cost. Otherwise apply selectively.

## Guidelines

### Foundation: Define the Task

**1. Context** [↓30-40% hallucinations]: State problem, scope, constraints, assumptions, scale, timeline, stakeholders, resources.

- ❌ "Design system"
- ✅ "Design payment system: problem (manual processing, 2h delays), scale (1M users), constraints (PCI-DSS), timeline (6mo), stakeholders (PM+Arch+Security+Legal), resources ($500K, 3 engineers)"

**Rationale:** Grounds responses in specific requirements.

**2. Clarity** [↓25-35% ambiguity]: Define key terms and relationships; use diagrams for complex concepts.

- ❌ "Use eventual consistency"
- ✅ "Define: Eventual consistency (async sync, stale reads <1s) vs strong consistency (immediate sync, higher latency). Include sequence diagram."

**Rationale:** Prevents misinterpretation; ensures consistent terminology.

**3. Precision** [↓40-50% ambiguity]: Use exact metrics, formulas, units.

- ❌ "Design fast and scalable system"
- ✅ "Design system: p95 latency <200ms, p99 <500ms, throughput 10K→100K req/s, auto-scale <2min, 99.9% uptime. Cost formula: `TCO = (servers × $100/mo) + (bandwidth_GB × $0.05) + (storage_TB × $20/mo)`. Use math blocks for complex formulas."

**Rationale:** Eliminates ambiguity; enables measurable recommendations.

**4. Relevance** [↓30-40% noise]: Focus on essential information; move non-critical details to appendices.

- ❌ "Explain database history and current options"
- ✅ "Compare SQL vs NoSQL for e-commerce: transaction requirements, scale, query patterns. Exclude history. Move extensive comparisons to appendix."

**Rationale:** Improves signal-to-noise; reduces output length.

### Scope: What to Cover

**5. MECE** (Mutually Exclusive, Collectively Exhaustive) [↑40-50% completeness]: Ensure sections are distinct with no gaps or overlaps.

- ❌ "Explain security: authentication and encryption"
- ✅ "Explain security: (1) Authentication, (2) Authorization, (3) Encryption (transit+rest), (4) Audit logging, (5) Secrets management. No gaps or overlaps."

**Rationale:** Prevents incomplete analysis; ensures comprehensive coverage.

**6. Sufficiency** [↑35-45% comprehensiveness]: Cover all necessary dimensions (what, why, how, when, who, constraints, alternatives, risks, outcomes).

- ❌ "Design API: define endpoints"
- ✅ "Design API: endpoints, authentication, rate limiting, versioning, error handling, pagination, caching headers, documentation"

**Rationale:** Prevents follow-ups; ensures actionable outputs.

**7. Breadth** [↑30-40% perspective diversity]: Include relevant stakeholder perspectives.

- ❌ "Explain from developer perspective"
- ✅ "Explain from: (1) Developer (code patterns), (2) SRE (operational complexity), (3) Security (threat surface), (4) PM (user impact)"

**Rationale:** Reveals trade-offs; facilitates cross-functional decisions.

**8. Depth** [↑25-35% thoroughness]: Request implementation-level detail for high-impact areas.

- ❌ "Recommend caching solution"
- ✅ "Recommend Redis: eviction policies (LRU/LFU tradeoffs), persistence (RDB/AOF), clustering (sentinel/cluster), memory limits, key naming patterns"

**Rationale:** Enables immediate action; reduces clarifications.

### Quality: Ensure Excellence

**9. Significance** [↓40-60% reading time]: Focus on high-impact items; deemphasize low-impact details.

- ❌ "List all HTTP error codes and handling"
- ✅ "Critical HTTP errors: 429 (rate limit), 503 (overload), 401/403 (auth), 500 (system alert). Exclude: 404, client errors <5% occurrence"

**Rationale:** Reduces cognitive load; focuses on decision-critical info.

**10. Priority** [↑45-55% focus]: Order by importance; label priority levels explicitly (critical/important/optional).

- ❌ "Handle errors, implement logging, add metrics"
- ✅ "Critical: 429/503 errors (circuit breaker). Important: 401/403 (alerts). Optional: 404 logging (<5% impact)"

**Rationale:** LLMs prioritize labeled items; prevents equal treatment of unequal concerns.

**11. Concision** [↓35-45% word count]: Eliminate redundancy; state each concept once.

- ❌ "Explain why we should consider using caching and how caching can improve performance"
- ✅ "Caching strategy: Redis for sessions (TTL 30min), CDN for static assets (TTL 1d). No explanatory text."

**Rationale:** Saves time; improves scannability.

**12. Accuracy** [↓20-30% errors]: Verify facts against authoritative sources.

- ❌ "Recommend libraries"
- ✅ "Recommend libraries: verify current versions (npm/PyPI), cite compatibility matrices from official docs, flag deprecated APIs"

**Rationale:** Reduces factual errors and outdated info.

**13. Credibility** [↓50-60% hallucinations]: Cite recent (2024+) primary sources.

- ❌ "What are best practices?"
- ✅ "Cite: AWS Well-Architected Framework (2024), Google SRE Book, OWASP Top 10 (2025). Include URLs."

**Rationale:** Credible sources reduce hallucinations; improve trust.

**14. Logic** [↓30-40% reasoning errors]: Provide coherent arguments with explicit trade-offs.

- ❌ "Explain why microservices simplify architecture"
- ✅ "Microservices tradeoff: increases operational complexity but improves scalability. Recommend modular monolith if team <10. Include reasoning."

**Rationale:** Prevents contradictions; ensures sound recommendations.

**15. Risk/Value** [↑60-80% decision quality]: Compare ≥2 alternatives with costs, benefits, risks.

- ❌ "Recommend Kubernetes setup"
- ✅ "Compare: (1) K8s self-managed ($2K/mo, ops team, full control), (2) Managed K8s ($500/mo, vendor lock-in, less ops), (3) VMs ($200/mo, limited scale). Include migration paths."

**Rationale:** Enables informed decisions; reveals hidden costs.

**16. Fairness** [↓40-50% bias]: Provide balanced view with counterarguments, limitations.

- ❌ "Why should we use GraphQL?"
- ✅ "GraphQL vs REST: pros (flexible queries, reduced over-fetching), cons (complexity, caching challenges), when NOT to use (simple CRUD, public API, small team)"

**Rationale:** Prevents biased recommendations; reveals limitations.

### Format: How to Present

**17. Structure** [↑30-40% scannability]: Use headings, lists, tables, diagrams.

- ❌ "Explain the solution"
- ✅ "Format: ## TOC → ### H2 sections → Bullet lists → Comparison tables → Mermaid diagrams → Code blocks with syntax highlighting → Math blocks"

**Rationale:** Improves scannability; easier to locate and act upon.

**18. Consistency** [↑35-45% readability]: Use consistent hierarchy and formatting.

- ❌ "Provide analysis"
- ✅ "Structure: ## Decision Context → ### Option A (pros/cons/cost) → ### Option B → ### Comparison → ### Recommendation → ### Timeline. H2 for main, H3 for subsections."

**Rationale:** Enables predictable navigation; reduces cognitive load.

**19. TOC**: Include table of contents for long documents (>3 pages or >5 sections). ❌ No navigation aid. ✅ TOC with section links.

**Rationale:** Improves navigation for complex content; reduces time to find information.

### Validation: Ensure Correctness

**20. Evidence** [↑40-50% trust]: Provide structured citations with source details, recency, uncertainty flags.

- ❌ "What do studies show?"
- ✅ "Cite: [1] Google SRE Book (2023) p.42 'MTTR <1h'. [2] AWS re:Invent 2024 [URL, timestamp]. Flag: 'cache hit rate estimated (no empirical data)'."

**Rationale:** Enables fact-checking; builds trust.

**21. Verification** [↓25-35% errors]: Self-review and error checking.

- ❌ "Provide recommendation"
- ✅ "Self-review: verify calculations, check contradictions, validate terminology, test code, cross-reference claims, flag uncertainties"

**Rationale:** Catches errors; improves reliability.

**22. Practicality** [↑50-60% implementation speed]: Provide concrete steps, examples, tools, commands.

- ❌ "Suggest monitoring improvements"
- ✅ "Monitoring setup: tools (Prometheus, Grafana), commands ('helm install prometheus'), queries ('rate(http_requests_total[5m])'), dashboards, common issues"

**Rationale:** Accelerates implementation; reduces trial-and-error.

**23. Success Criteria** [↑40-50% measurability]: Define measurable outcomes with baselines, targets.

- ❌ "How to achieve better performance?"
- ✅ "Metrics: p95 latency <200ms (current: 800ms), error rate <0.1% (current: 0.5%), cost <$5K/mo (current: $8K/mo), timeline 3mo. Specify tools."

**Rationale:** Enables objective evaluation; tracks progress.

## Quick Check (30s)

**Before sending (mandatory for decision-critical):**

☐ **Self-contained**: Complete context; no cross-file refs  
☐ Context | ☐ Clarity | ☐ Precision | ☐ Relevance  
☐ MECE | ☐ Sufficiency | ☐ Breadth | ☐ Depth  
☐ Significance | ☐ Priority | ☐ Concision | ☐ Accuracy | ☐ Credibility  
☐ Logic | ☐ Risk/Value | ☐ Fairness  
☐ Structure | ☐ Consistency | ☐ TOC  
☐ Evidence | ☐ Verification | ☐ Practicality | ☐ Success Criteria
# Guidelines for Content Quality Check

**Purpose:** Improve the quality of notes, articles, templates, and other knowledge base documents so that readers (including future you and LLMs) can make reliable decisions with minimal clarification cycles and rework.

**When to apply:** Apply all guidelines for decision-critical content that meets ≥1 of the following: blocks a decision, risk of >5% impact on key metrics, 1-6mo action window, ≥2 stakeholders, adoption or implementation cost ≥40h. Apply them selectively for other content that still requires high quality. **Expected impact:** ↓30-60% misunderstandings, ↓30-60% avoidable questions, ↑60-80% decision quality based on the documents.

## Guidelines (21 Total)

### Foundation: Define the Document’s Task

**1. Context** [↓30-40% clarification and guessing]: The document explicitly states scope, constraints, assumptions, scale, timeline, domain, stakeholders, tech stack, budget (where relevant). ❌ Bad: Only title and one line: "Design system". ✅ Good: Introduction states: "This document describes the design of a payment system for 1M users, with PCI-DSS compliance, 6-month delivery timeline, fintech startup context, stakeholders: PM+Architect+Security+Legal, budget $500K."

**2. Clarity** [↓25-35% ambiguity in meaning]: The document defines key technical terms and explains important relationships. ❌ Bad: "Use eventual consistency" with no explanation. ✅ Good: Defines: "Eventual consistency (async data sync; stale reads acceptable for <1s) vs strong consistency (immediate sync; higher latency)."

**3. Precision** [↓40-50% ambiguity in specifications]: The document uses quantified requirements with exact metrics, formulas, and units where relevant. ❌ Bad: "System should be fast and scalable." ✅ Good: "Target p95 latency <200ms, p99 <500ms; throughput 10K→100K req/s; auto-scale in <2min; availability 99.9%."

**4. Relevance** [↓30-40% noise]: The document focuses on decision-critical aspects and pushes non-essential detail to appendices or references. ❌ Bad: Long history of databases plus current options. ✅ Good: "This section compares SQL vs NoSQL for the e-commerce use case: transaction requirements, scale characteristics, query patterns. History is omitted unless needed for regulation or migration context."

### Scope: What the Document Should Cover

**5. MECE** [↑40-50% completeness]: Sections are mutually exclusive and collectively exhaustive for the document’s purpose. ❌ Bad: "Security" section only covers authentication and encryption. ✅ Good: Security organized into 5 sub-sections: (1) Authentication, (2) Authorization, (3) Encryption (in transit + at rest), (4) Audit logging, (5) Secrets management, with no gaps or overlaps.

**6. Sufficiency** [↑35-45% comprehensiveness]: The document covers all necessary aspects for its purpose. ❌ Bad: "API design" section describes only endpoints. ✅ Good: API section covers: endpoints, authentication, rate limiting, versioning strategy, error handling, pagination, caching headers, documentation requirements.

**7. Breadth** [↑30-40% perspective diversity]: The document reflects multiple stakeholder perspectives where appropriate. ❌ Bad: Only developer concerns are described. ✅ Good: Section summarizes 4 perspectives: (1) Developer: code patterns, (2) SRE: operational complexity, (3) Security: threat surface, (4) PM: user impact and value.

**8. Depth** [↑25-35% thoroughness]: High-impact areas include implementation-level detail, not just slogans. ❌ Bad: "Use caching to improve performance." ✅ Good: "Use Redis with: eviction policies (LRU/LFU trade-offs), persistence options (RDB/AOF), clustering approaches (sentinel/cluster), memory limit calculations, key naming patterns."

### Quality: Ensure Excellence

**9. Significance** [↓40-60% reading time]: The document highlights what really matters and deemphasizes low-impact details. ❌ Bad: Full list of all HTTP status codes. ✅ Good: Focuses on critical codes for the system: 429 (rate limit), 503 (overload), 401/403 (auth), 500 (system alert); links out to general HTTP code references.

**10. Concision** [↓35-45% word count]: The document avoids redundancy and unnecessary filler. ❌ Bad: Repeating "caching improves performance" in multiple sections. ✅ Good: States the principle once, then references it and focuses later sections on concrete configuration, commands, and examples.

**11. Accuracy** [↓20-30% factual errors]: Factual statements are checked against up-to-date, authoritative sources. ❌ Bad: Recommends libraries or tools without version or compatibility checks. ✅ Good: Notes current versions (npm/PyPI, OS packages), flags deprecated APIs, and cross-references compatibility matrices from official docs.

**12. Credibility** [↑50-60% trust]: Important claims and recommendations cite primary, authoritative sources, preferably recent (e.g., 2023+). ❌ Bad: "Best practices say..." with no reference. ✅ Good: "Based on AWS Well-Architected Framework, Google SRE Book, OWASP Top 10 (2023+), and peer-reviewed papers, we recommend…"

**13. Logic** [↓30-40% reasoning errors]: Arguments are coherent, consistent, and explicitly present trade-offs. ❌ Bad: "Microservices simplify architecture" with no nuance. ✅ Good: Notes: microservices increase operational complexity but can improve independent scaling; recommends modular monolith if team <10 and ops capacity is limited.

**14. Risk/Value** [↑60-80% decision quality]: The document compares ≥2 alternatives with costs, benefits, and risks. ❌ Bad: "Use Kubernetes" with no alternatives. ✅ Good: Compares 3 options: (1) Self-managed K8s ($2K/mo, ops team needed), (2) Managed K8s ($500/mo, vendor lock-in), (3) VMs ($200/mo, limited scale); includes migration paths.

**15. Fairness** [↓40-50% bias]: The document presents balanced views, counterarguments, and limitations. ❌ Bad: "We should use GraphQL" without downsides. ✅ Good: Compares GraphQL vs REST: pros (flexible queries), cons (complexity, caching challenges), when NOT to use (simple CRUD, public APIs); includes counterarguments.

### Format: How to Present Content

**16. Structure** [↑30-40% scannability and actionability]: The document uses clear headings, sections, and lists that make it easy to scan and act. ❌ Bad: Long, unstructured text block titled "Solution". ✅ Good: Structured as: `## Overview` → `### Key decisions` → `### Architecture` → `### Risks` → bullet lists for steps → comparison tables → diagrams → code blocks with syntax highlighting where needed.

**17. Format** [↑35-45% readability]: The document follows a consistent hierarchy and repository conventions (e.g., H1 title, H2 sections, bullets, tables, diagrams). ❌ Bad: Mixed heading levels and inconsistent formats for similar sections. ✅ Good: Uses a predictable pattern, such as: `## Decision context` → `### Option A (pros/cons/cost)` → `### Option B` → `### Comparison table` → `### Recommendation` → `### Timeline with milestones`.

### Validation: Ensure Correctness and Usefulness

**18. Evidence** [↑40-50% trust]: Citations include source details, recency, and explicit uncertainty flags. ❌ Bad: "Studies show…" with no details. ✅ Good: "Cited sources: [1] Google SRE Book (2023), p.42, 'MTTR <1h'; [2] AWS re:Invent 2023 talk [video URL]. Uncertainty: cache hit-rate impact is estimated; no internal measurements yet."

**19. Validation** [↓25-35% errors]: The author (or reviewer) performs a structured self-review. ❌ Bad: Document is committed without checks. ✅ Good: Reviewer verifies calculations, checks for contradictions and inconsistent terminology/metrics, tests code examples, validates assumptions against sources, and explicitly flags any open questions or uncertainties.

**20. Practicality** [↑50-60% implementation speed]: The document includes concrete steps, commands, or examples where appropriate. ❌ Bad: "Improve monitoring" with generic advice. ✅ Good: "Monitoring setup: Prometheus for metrics, Grafana for dashboards; install via `helm install prometheus ...`; example queries: `rate(http_requests_total[5m])`; troubleshooting checklist."

**21. Success Criteria** [↑40-50% measurability]: The document defines measurable outcomes and how to validate them. ❌ Bad: "Aim for better performance" with no numbers. ✅ Good: "Targets: p95 latency <200ms (current: 800ms), error rate <0.1% (current: 0.5%), infra cost <$5K/mo, implementation timeline 3 months; specify measurement methods and dashboards."

## Quick Check (30s)

**Before publishing or committing your content (mandatory for decision-critical documents, recommended for others):** ☐ Self-contained enough (key context is present here; references to other notes include brief summaries and working relative links, not just "see previous answer") ☐ Context ☐ Clarity ☐ Precision ☐ Relevance ☐ MECE ☐ Sufficiency ☐ Breadth ☐ Depth ☐ Significance ☐ Concision ☐ Accuracy ☐ Credibility ☐ Logic ☐ Risk/Value ☐ Fairness ☐ Structure ☐ Format ☐ Evidence ☐ Validation ☐ Practicality ☐ Success Criteria
**Quality attributes (10):** Accurate | Precise | Cited | Complete | Actionable | Consistent | Relevant | Balanced | Appropriately recent (for time-sensitive topics) | Testable/Verifiable
**Exclude or move to references:** Long history sections (unless needed for regulation or migration), pure theory (unless adoption cost ≥40h or concept is central), edge cases with <5% impact and low severity, formal proofs, trends without data, speculation, and content that only says "see other file" or "see previous answer" without summary and a working link. **Always specify:** Key context (scope, constraints, assumptions, scale, timeline, domain, stakeholders, tech stack, budget) so the document stands on its own and can be used reliably without guessing.
**Impact metrics:** ↓30-60% clarification cycles and misunderstandings (Context + Clarity) | ↓25-50% ambiguity (Precision) | ↑60-80% decision quality (Risk/Value) | ↑35-50% completeness (MECE + Sufficiency) | ↑30-45% scannability (Structure + Format) | ↑50-60% implementation speed (Practicality).



# Technical Operations News Intelligence Q&A Generator

## Table of Contents
- [Overview](#overview)
- [Scope](#scope)
- [Requirements](#requirements)
- [Execution](#execution)
- [Validation Checklist](#validation-checklist)
- [Question Quality](#question-quality)
- [Output Format](#output-format)
- [Glossary](#glossary)

## Overview

Generate 4-6 decision-critical Q&As from recent infrastructure and security news for engineering teams.

**Goal**: Enable informed technical decisions via minimal viable news tracking.

**Cadence**: Bi-weekly | **Validity**: 2 weeks

**Freshness Thresholds**:
- Security/Infrastructure/Releases: ≥80% <1mo, 100% <4mo
- Standards/Practices: ≥70% <2mo, 100% <6mo

**Decision Criticality** (≥1 per Q&A):
1. Blocks infrastructure/security decisions (e.g., vendor choice, architecture)
2. Creates material risk/threat (security breach, outage, compliance violation)
3. Impacts ≥2 roles (requires coordination across teams)
4. Requires action within 1-6mo (time-sensitive window)
5. Has quantified impact (measurable performance/cost/security metrics)

## Scope

**Audience**: Architects, DevOps/SRE, Security Engineers, Developers, Engineering Managers

**Include**: Security (CVEs), infrastructure, releases, ecosystem, standards, practices, benchmarks

**Exclude**: Marketing, rumors, speculation, stale news (>4mo for security)

**Categories**: Technical Releases, Infrastructure/Cloud, Security, Ecosystem/Integration, Standards/Regulations, Engineering Practices

**Relevance** (≥2 required): 
- Recency (<1mo security, <2mo practices)
- Multi-phase impact (≥2 lifecycle phases)
- Multi-role impact (≥2 distinct roles)
- Time-sensitive (action window 1-6mo)
- Quantified metrics (specific numbers with units)

## Requirements

**Q&A Structure**: 4-6 total | 120-200 words each | cited sources with URLs

**Lifecycle Phases**: Architecture & Design, Development, Deploy & Release, Operations & Observability

**Topic Coverage** (Priority order):
1. **Critical**: Security (CVEs, vulnerabilities), infrastructure (cloud, networking)
2. **Important**: Practices (DevOps, SRE), major releases
3. **Optional**: Ecosystem updates (<5% adoption impact)

**Stakeholder Coverage**: Address ≥5 distinct roles across all Q&As

**References**: Glossary (terms used), News sources (≥4), Tools, Standards, Reports, Citations

**Visuals**: ≥2 diagrams + ≥1 table

**Quality Validation**: See [Validation Checklist](#validation-checklist) for complete criteria

## Execution

### 1. News Discovery & Curation

**Search** (≥10 candidates to ensure 4-6 quality Q&As after filtering; prioritize 1-7d for security/infrastructure):
- **Security**: CVE DB, CISA KEV, vendor security advisories, GitHub Security Advisories
- **Infrastructure**: AWS/GCP/Azure blogs, Kubernetes blog, CNCF, container registries
- **Practices**: InfoQ, Martin Fowler blog, SRE Weekly, DevOps Institute
- **Releases**: GitHub releases, official vendor blogs, package registries

**Curate**:
- Prefer primary sources (official vendor announcements, CVE databases, official blogs vs secondary reporting)
- Meet freshness thresholds and ≥1 criticality criterion
- Include specific, quantified details
- Balance across categories

**Allocate**: Distribute 4-6 Q&As across phases, categories, and roles. Record generation date (YYYY-MM-DD).

### 2. Build References

**Reference Types**:
- **G#**: Glossary - term, definition with analogy, context (only terms used)
  - Example: G1: CVE - Common Vulnerabilities and Exposures...
- **N#**: News - title, source, date YYYY-MM-DD, category, URL
  - Example: N1: "Kubernetes 1.30 Released", Kubernetes Blog, 2024-04-17, Releases, https://kubernetes.io/blog/...
- **T#**: Tools - name, description, version, URL
  - Example: T1: Prometheus v2.50 - metrics collection and alerting, https://prometheus.io
- **S#**: Standards - ID, title, key changes, URL
  - Example: S1: PCI-DSS v4.0 - Payment Card Industry standard, adds MFA requirements, https://...
- **R#**: Reports - title, firm, date, key findings, URL
  - Example: R1: "State of DevOps 2024", DORA, 2024-06, elite performers deploy 973x more frequently, https://...
- **A#**: Citations - APA 7th format with URL
  - Example: A1: Smith, J. (2024). Cloud security practices. AWS Blog. https://...

**Citation Format**: [Ref: N#][n#] inline → [n#]: URL at end
- Example: "AWS announced Lambda SnapStart [Ref: N1][1]" → "[1]: https://aws.amazon.com/blogs/..."

**Evidence**: Prefer primary sources (vendor blogs, CVE DB, official docs) over secondary (news articles); flag uncertainties (e.g., "estimated", "unconfirmed")

### 3. Generate Q&A

**Question Patterns**: 
- "[News] implications for [Phase]+[Roles]?"
- "[CVE/Change]: response strategy?"
- "[Release/Change]: adoption approach?"

**Avoid**: 
- Generic questions ("How do CVEs work?")
- Hype/marketing ("Revolutionary AI tool...")
- Unattributed claims ("Best practices recommend...")
- Speculation ("May release next month...")

**Structure** (120-200 words total):
1. **News**: What, when, why, category [Ref: N#][n#]
2. **Impact**: ≥2 phases with quantified metrics (performance/reliability/security/cost)
3. **Stakeholders**: ≥2 roles with specific concerns and actions
4. **Decision**: 
   - **Alternatives**: Compare ≥2 options (costs in $, benefits with metrics, risks with probability/impact)
   - **Recommendation**: Adopt/Investigate/Defer/Avoid + rationale with trade-offs
   - **Success Criteria**: Measurable targets (baseline → target, measurement method)
   - **Limitations**: When NOT to use; counterarguments
5. **Action**: Immediate (0-2wk) and short-term (2wk-2mo) steps with owners
6. **Links**: [n#]: URL

**Self-Check**: Per [Validation Checklist](#validation-checklist)

### 4. Add Visuals

Include ≥2 diagrams (Mermaid flows/matrices) + ≥1 table

### 5. Validate & Submit

**Validate**:
- **Completeness**: References (N≥4), coverage (5+ roles, 4-6 Q&As), citations with URLs, word count (120-200/Q&A), visuals (≥2 diagrams, ≥1 table)
- **Quality**: Fresh news (meet thresholds, no hype/speculation), criticality met (≥1 criterion/Q&A), impact quantified (specific metrics with units)
- **Decisions**: Recommendations with rationale + ≥2 alternatives (cost/benefit/risk) + success criteria (baseline→target) + limitations
- **Accuracy**: Verify facts against primary sources (vendor docs, CVE DB, official blogs), check contradictions, flag uncertainties ("estimated", "unconfirmed"), validate all URLs

**Submit**: Include complete glossary, TOC, generation date, and expiry date (generation + 2 weeks)

## Validation Checklist

| Check | Criteria | Status |
|-------|----------|--------|
| Freshness | Sec/Infra ≥80% <1mo; Stds/Prac ≥70% <2mo | PASS/FAIL |
| References | Adequate coverage (N≥4, others as needed) | PASS/FAIL |
| Q&As | 4-6 total, 120-200w each | PASS/FAIL |
| Coverage | Security and infrastructure emphasized | PASS/FAIL |
| Roles | ≥5 distinct roles covered | PASS/FAIL |
| Criticality | All meet ≥1 criterion | PASS/FAIL |
| Impact | All with ≥2 phases+roles, quantified | PASS/FAIL |
| Decision | All with alternatives+recommendation+rationale+limitations | PASS/FAIL |
| Citations | All Q&As cited with valid URLs | PASS/FAIL |
| Verification | Facts verified, contradictions checked, uncertainties flagged | PASS/FAIL |
| Visuals | ≥2 diagrams, ≥1 table | PASS/FAIL |
| Dates | Generation: ___ | Expiry: ___ (+2wk) | INFO |

## Question Quality

**Good Examples**:
- "CVE-2024-XXXX critical vulnerability: What's our patching strategy?"
- "Kubernetes 1.30 deprecations: How to migrate affected workloads?"
- "AWS pricing changes: What's the cost impact for our infrastructure?"

**Bad Examples** (avoid):
- "How do CVEs work?" (generic, not news-driven)
- "What is SRE?" (educational, not decision-focused)
- "Should we use Kubernetes?" (no specific news trigger)
- Feature announcements without decision impact

## Output Format

Single Markdown document with sections: **TOC** → **Executive Summary** → **Phase Overview** → **Q&As** → **References** → **Validation**

### Executive Summary

Include:
- **Domain**: TechOps | **Period**: [YYYY-MM-DD] to [YYYY-MM-DD] | **Coverage**: [X Q&As across Y phases]
- **Key Insights** (1-2 highest-impact): 
  - News item + quantified impact (metrics) + recommendation (Adopt/Investigate/Defer/Avoid) + timeline (action window)
- **Dashboard**: Phase | News | Decision | Timeline table
- **Stats**: Roles covered (X), References (N#/T#/S# counts)

### Phase Overview Table

| Phase | Categories | Top News | Roles |
|-------|------------|----------|-------|
| Architecture & Design | Security, Infrastructure | [Item] | Architect, SRE |
| Development | Practices, Releases | [Item] | Developer, DevOps |
| Deploy & Release | Infrastructure, Security | [Item] | DevOps, SRE |
| Operations & Observability | Infrastructure, Practices | [Item] | SRE, Manager |

### Q&A Template

```
### Q#: [News Question + Phase + Roles]

**Phase**: [Architecture & Design/Development/Deploy & Release/Operations & Observability] | **Roles**: [Primary, Secondary] | **Category**: [Security/Infrastructure/Releases/Practices/Standards/Ecosystem] | **Criticality**: [1-5 from list]

**News**: [What happened] on [YYYY-MM-DD]: [why it matters] [Ref: N#][n#]

**Impact**: 
- **[Phase 1]**: [Metric] (e.g., latency +50ms, cost +$2K/mo, CVE severity 9.8/10)
- **[Phase 2]**: [Metric]

**Stakeholders**: 
- **[Role 1]**: [Specific concern] → Action: [what to do]
- **[Role 2]**: [Specific concern] → Action: [what to do]

**Decision**: 
- **Alternatives**: 
  - Option A: [description] | Cost: [$] | Benefit: [metric] | Risk: [impact+probability]
  - Option B: [description] | Cost: [$] | Benefit: [metric] | Risk: [impact+probability]
- **Recommendation**: [Adopt/Investigate/Defer/Avoid]
- **Rationale**: [Why this option? Trade-offs considered]
- **Success Criteria**: [Current baseline] → [Target] (measure via [method/tool])
- **Limitations**: Do NOT use when [condition]; [counterargument consideration]

**Action**: 
- **Immediate (0-2wk)**: [Action 1], [Action 2] (Owner: [Role])
- **Short-term (2wk-2mo)**: [Action 3], [Action 4] (Owner: [Role])

[n#]: [Full URL]
```

## Glossary

**APA 7th format**: Citation standard: Author, A. A. (Year). Title. Source. URL. Example: Smith, J. (2024). Cloud security practices. AWS Blog. https://aws.amazon.com/blogs/security/...

**CISA KEV**: Known Exploited Vulnerabilities catalog maintained by Cybersecurity and Infrastructure Security Agency. Lists CVEs with active exploitation requiring priority patching.

**CVE**: Common Vulnerabilities and Exposures - standardized identifier for publicly disclosed security vulnerabilities (e.g., CVE-2024-12345). Scored 0-10 via CVSS.

**Decision criticality**: News that blocks decisions, creates material risk, impacts ≥2 roles, requires action within 1-6mo, or has quantified impact.

**DevOps**: Development + Operations integration practices. Emphasizes automation, continuous delivery, and collaboration between dev and ops teams.

**MECE** (Mutually Exclusive, Collectively Exhaustive): Framework ensuring sections are distinct with no gaps or overlaps. Like organizing files into folders where each file belongs to exactly one folder, and all files are covered.

**Primary sources**: Original announcements or data (vendor blogs, CVE databases, official docs) vs secondary reporting (news articles summarizing announcements).

**Quantified metrics**: Specific, measurable values with units (e.g., "latency <200ms", "cost $5K/mo", "error rate <0.1%") vs vague qualifiers ("fast", "cheap", "reliable").

**SRE**: Site Reliability Engineering - discipline applying software engineering to infrastructure and operations. Focuses on reliability, scalability, and automation.

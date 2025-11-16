# Event Analysis Framework (4-Question Model)

Generate concise event analyses for informed decision-making with minimal information overhead.

## Core Principle

**Time-Efficient Decision Support**: Extract maximum insight from minimal information. Focus on actionable intelligence over comprehensive documentation.

## Essential Q&A Structure (4 Questions)

For any significant event, answer only these 4 questions:

1. **What happened?** (30-50w): Event, date, who affected, scope
2. **Why did it happen?** (40-60w): Root cause (proximate + systemic)
3. **What was the impact?** (30-40w): Quantified consequences (financial, operational, strategic)
4. **What should I do/learn?** (40-60w): One actionable takeaway + one preventive measure

**Total**: 150-200 words per event | **Time to read**: 60-90 seconds

## Terminology

**RCA**: Root Cause Analysis | **MTTR/MTBF**: Mean Time To Repair/Between Failures | **CVE**: Common Vulnerabilities & Exposures | **Zero-day**: Unpatched exploited vulnerability | **APT**: Advanced Persistent Threat | **DDoS**: Distributed Denial of Service | **Supply Chain Attack**: Compromise via trusted third-party | **Post-mortem**: After-action incident analysis | **SLA**: Service Level Agreement

## Event Domains (MECE)

**Security** | **Technical** | **Market** | **Regulatory** | **Business** | **Technology**

## Quality Standards

**Verification**: 1-2 authoritative sources minimum | Quantified metrics required | Non-obvious insights only

**Sources**: Official reports > Government > Industry > News

---

## Examples

### Example 1: Cloudflare Outage (Jun 2019)

**1. What happened?** (45w)  
Cloudflare global outage on June 24, 2019 for 27 minutes. Regex in WAF rule caused CPU exhaustion across all data centers. 50% of HTTP requests failed globally, affecting millions of websites. No data breach.

**2. Why did it happen?** (52w)  
**Proximate**: Untested regex with catastrophic backtracking (`.*(?:.*=.*){  }`) deployed to production.  
**Systemic**: No canary rollout for "safe" configuration changes; insufficient adversarial input testing; synchronized global deployment without gradual ramping; missing CPU-based kill switches.

**3. What was the impact?** (38w)  
27 minutes downtime, millions of customer sites down, estimated $20M+ lost customer revenue, significant reputational damage. Quick resolution (12 min after identification) limited long-term business impact.

**4. What should I do/learn?** (58w)  
**Takeaway**: Treat configuration changes like code deployments—test with adversarial inputs, implement gradual rollouts.  
**Prevention**: Automated ReDoS detection in CI/CD; canary deployments for all config changes; CPU-based automated kill switches; adversarial performance testing.

---

### Example 2: Equifax Breach (Mar-Jul 2017)

**1. What happened?** (42w)  
Equifax exposed 147.9M records (SSN, DOB, addresses, 209K credit cards) from March-July 2017. Unpatched Apache Struts CVE-2017-5638 exploited. Undetected for 66 days; disclosed 6 months post-compromise.

**2. Why did it happen?** (58w)  
**Proximate**: Unpatched vulnerability despite DHS alert and available patch.  
**Systemic**: Expired SSL certificate blocked vulnerability scanning; flat network architecture enabled lateral movement; plaintext credentials stored; no centralized patch management across 50+ business units; security culturally deprioritized.

**3. What was the impact?** (35w)  
$1.4B settlement, $1.5B+ total costs, CEO/CIO/CSO resigned, 35% stock drop (-$5B market cap), Congressional hearings, criminal charges for insider trading, industry-wide regulatory changes.

**4. What should I do/learn?** (59w)  
**Takeaway**: Basic security hygiene matters more than sophisticated defenses. Culture determines security outcomes.  
**Prevention**: Centralized patch management with 24-48h critical patch window; network segmentation; encrypted credentials; continuous monitoring for lateral movement; regular asset inventory audits.

---

### Example 3: SolarWinds Supply Chain (Mar-Dec 2020)

**1. What happened?** (48w)  
Russian APT29 compromised SolarWinds Orion via build system injection March-December 2020. SUNBURST backdoor in signed updates affected 18,000+ organizations, 9 federal agencies, Fortune 500 companies. 9 months undetected.

**2. Why did it happen?** (55w)  
**Proximate**: Weak build system access controls; no build integrity verification.  
**Systemic**: Software supply chain lacks cryptographic trust mechanisms; security monitors perimeter not trusted software; 9-month detection gap; interconnected infrastructure creates systemic failure points; implicit trust in signed updates.

**3. What was the impact?** (37w)  
100+ high-value targets actively exploited, ~$100B industry-wide remediation costs, compromised federal agencies (Treasury, State, DOD), Executive Order 14028 on cybersecurity, diplomatic sanctions, trust crisis in software supply chains.

**4. What should I do/learn?** (58w)  
**Takeaway**: Trust is the vulnerability; verify everything cryptographically.  
**Prevention**: Air-gapped build environments; HSM-backed code signing with multi-party approval; SBOM for all dependencies; behavioral monitoring of trusted software; zero-trust architecture; reproducible builds with cryptographic attestations.

## Output Format

```markdown
# Event Analysis: [Title]

**Domain**: [Security/Technical/Market/Regulatory/Business/Technology] | **Date**: [YYYY-MM] | **Read Time**: 60-90s

## 1. What happened? (30-50w)
[Event description with scope and timeline]

## 2. Why did it happen? (40-60w)
**Proximate**: [Immediate cause]  
**Systemic**: [Underlying organizational/architectural issues]

## 3. What was the impact? (30-40w)
[Quantified financial/operational/strategic consequences]

## 4. What should I do/learn? (40-60w)
**Takeaway**: [One non-obvious, actionable insight]  
**Prevention**: [Specific preventive measures]

**Sources**: [1-2 authoritative links]
```

## Usage

**Select events**: High-impact with clear lessons across 6 domains  
**Answer 4 questions**: 150-200w total per event  
**Track efficiently**: 5 events/month minimum (1 per key domain) for baseline awareness; 10 events/month maximum to avoid overload  
**Focus on**: Actionable lessons > comprehensive documentation

**Success**: Can read and extract decision-relevant insights in <90 seconds per event

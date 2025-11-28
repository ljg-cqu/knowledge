# Nine Aspects Analysis: Blockchain MPC Wallet Problems

**Document Metadata**
- **Created**: 2025-11-28
- **Analysis Framework**: Nine Aspects for Analyzing Problems
- **Source Problems**: LinerSDR.md (11 structured problem statements)
- **Status**: Draft

---

## Table of Contents

1. [Problem 1: Risk of Private Key Theft and Compromise](#problem-1-risk-of-private-key-theft-and-compromise)
2. [Problem 2: Complexity and Subtleties in Deploying MPC Wallets](#problem-2-complexity-and-subtleties-in-deploying-mpc-wallets)
3. [Problem 3: Difficulty of Private Key Recovery and Backup Mechanisms](#problem-3-difficulty-of-private-key-recovery-and-backup-mechanisms)
4. [Problem 4: Balancing Security and Usability in Private Key Management](#problem-4-balancing-security-and-usability-in-private-key-management)
5. [Problem 5: Scalability and Performance Challenges in Heterogeneous Environments](#problem-5-scalability-and-performance-challenges-in-heterogeneous-environments)
6. [Problem 6: Interoperability and Chain-Agnostic Design Challenges](#problem-6-interoperability-and-chain-agnostic-design-challenges)
7. [Problem 7: Cost Structure and Economic Implications](#problem-7-cost-structure-and-economic-implications)
8. [Problem 8: User Experience Complexity Limiting Mass Adoption](#problem-8-user-experience-complexity-limiting-mass-adoption)
9. [Problem 9: Ethical Implications and Privacy Concerns](#problem-9-ethical-implications-and-privacy-concerns)
10. [Problem 10: Lack of Standardized Best Practices and Certifications](#problem-10-lack-of-standardized-best-practices-and-certifications)
11. [Problem 11: Future Risks Posed by Quantum Computing](#problem-11-future-risks-posed-by-quantum-computing)

---


## Problem 1: Risk of Private Key Theft and Compromise

### Context Recap

**Problem Title**: Private Key Extraction Attacks in Blockchain MPC Wallets

**Key Context**:
- MPC wallets distribute private key shares among multiple parties, but novel key-extraction attacks can exfiltrate the entire private key by compromising just one party
- Current situation: Threshold signature schemes show limitations in resilience to targeted attacks
- Goal: Achieve zero single-point-of-failure vulnerabilities, eliminating successful key extraction in single-party compromise scenarios by 100% within 6-12 months
- Hard constraints: Must maintain low transaction latency, limited cryptographic expertise, confined trust boundaries, development budget constraints
- Impact: Immediate to short-term (6 months), global scope affecting billions of USD in cryptocurrency assets

---

### 1. Problem Definition (Aspect 1)

#### 1.1 Problem and contradictions

**Core contradiction**: The fundamental security promise of MPC wallets—that distributing key shares enhances security—is undermined by the reality that compromising a single party can lead to full key exfiltration.

**Conflicting parties and goals**:
- **Wallet users** require absolute security guarantees for their digital assets (billions of USD at stake)
- **Wallet providers** must deliver security while maintaining competitive performance and usability
- **Security auditors** need verifiable proof of protection against known attack vectors
- **Attackers** possess both capability and motivation to exploit any single-party vulnerability

**Key constraints**:
- Cryptographic protocol complexity limits implementation options
- Transaction latency requirements constrain defense mechanisms
- Limited trust boundaries among participating parties
- Scarcity of specialized cryptographic expertise

#### 1.2 Goals and conditions

**Expected results**:
- **Primary goal**: Eliminate successful key extraction attempts in single-party compromise scenarios (100% prevention rate)
- **Timeline**: 6-12 months implementation window
- **Success metric**: Zero successful key leakage events under single-party compromise testing

**Hard constraints**:
- Transaction latency must remain low (milliseconds to low seconds range)
- Must work within existing MPC protocol frameworks
- Limited cryptographic engineering resources
- Budget constraints for protocol redesign and deployment

**Resource limits**:
- Available cryptographic expertise: limited and expensive
- Development budget: constrained
- Time window: 6-12 months (urgent)
- Testing infrastructure: requires significant investment

#### 1.3 Extensibility and common structure

**Multiple attribute perspectives**:

- **Virtual vs. Physical**:
  - *Physical*: Cryptographic keys as mathematical objects, network infrastructure, hardware security modules
  - *Virtual*: Trust relationships, protocol reputation, security assurances, user confidence

- **Hard vs. Soft**:
  - *Hard*: Cryptographic algorithms, key share distribution mechanisms, party infrastructure
  - *Soft*: Communication protocols between parties, coordination mechanisms, trust assumptions

- **Latent vs. Manifest**:
  - *Manifest*: Known key-extraction attacks, documented vulnerabilities in threshold schemes
  - *Latent*: Undiscovered attack vectors, future quantum threats, insider threats not yet materialized

- **Positive vs. Negative**:
  - *Positive*: Enhanced security through distribution, no single point of failure in theory, audit trail of operations
  - *Negative*: Increased complexity, potential for coordinated attacks, performance overhead

**Reframing possibilities**:
1. From "prevent key theft" to "make stolen keys useless" (time-bound keys, refresh mechanisms)
2. From "protect all parties equally" to "isolate critical operations to most secure parties"
3. From "static key shares" to "dynamic, frequently rotated key material"
4. From "prevent compromise" to "detect and respond to compromise rapidly"

---

### 2. Internal Logical Relations (Aspect 2)

#### 2.1 Key elements

**Roles**:
- Key share holders (multiple parties)
- Transaction initiators (users)
- Protocol coordinators
- Security auditors
- Potential attackers

**Resources**:
- Cryptographic algorithms (threshold signatures, secret sharing)
- Computational power for cryptographic operations
- Secure communication channels
- Hardware security modules (optional)
- Cryptographic expertise

**Processes**:
- Key generation ceremony
- Key share distribution
- Transaction signing coordination
- Key refresh/rotation procedures
- Compromise detection mechanisms

**Rules**:
- Threshold requirements (t-of-n signatures)
- Communication protocols
- Trust assumptions
- Access control policies

#### 2.2 Balance and "degree"

**Critical balance points where "too much" becomes harmful**:

1. **Security vs. Performance**:
   - *Too little security*: Vulnerable to key extraction
   - *Too much security*: Unacceptable transaction latency, poor user experience
   - *Sweet spot*: Provable security against single-party compromise with <1s transaction completion

2. **Distribution vs. Coordination overhead**:
   - *Too few parties*: Insufficient security distribution
   - *Too many parties*: Excessive communication rounds, slower signatures, higher failure rates
   - *Sweet spot*: 3-5 parties balancing security and efficiency

3. **Complexity vs. Auditability**:
   - *Too simple*: Easy to audit but potentially vulnerable
   - *Too complex*: Secure but impossible to audit thoroughly, hidden vulnerabilities
   - *Sweet spot*: Well-studied cryptographic primitives with formal security proofs

4. **Trust vs. Verification**:
   - *Too much trust*: Vulnerable to insider attacks
   - *Too much verification*: Excessive overhead, impractical
   - *Sweet spot*: Zero-knowledge proofs for critical operations, trust for routine tasks

#### 2.3 Key internal causal chains

**Chain 1: Compromise → Exfiltration → Asset Loss**
```
Single party compromise → 
Access to key share + protocol knowledge → 
Active or passive key extraction attack → 
Full private key reconstruction → 
Unauthorized transaction signing → 
Complete asset theft
```

**Intervention points**:
- Strengthen party security (hardening)
- Modify protocol to prevent extraction even with share access
- Implement key refresh to limit compromise window
- Add anomaly detection for unusual signing patterns

**Chain 2: Complexity → Implementation Errors → Vulnerabilities**
```
Complex cryptographic protocols → 
Subtle implementation requirements → 
Developer misunderstanding/mistakes → 
Security vulnerabilities in deployment → 
Exploitable attack surface
```

**Intervention points**:
- Simplify protocols where possible
- Provide secure reference implementations
- Mandate security audits before deployment
- Develop automated verification tools

---

### 3. External Connections (Aspect 3)

#### 3.1 Stakeholders

**Upstream stakeholders**:
- **Cryptographic researchers**: Develop and publish protocols, discover vulnerabilities
- **Standards bodies**: Define security standards and best practices
- **Hardware manufacturers**: Provide secure execution environments (HSMs, TEEs)

**Downstream stakeholders**:
- **End users**: Depend on wallet security for asset protection
- **Exchanges and DeFi platforms**: Integrate with wallets, share security risks
- **Regulators**: Require security compliance for institutional use
- **Insurance providers**: Assess and price security risks

**Side-line stakeholders**:
- **Competing wallet providers**: Race to offer better security/usability balance
- **Security researchers**: Test and probe for vulnerabilities (white hat and potentially malicious)
- **Media**: Shape public perception of MPC wallet security

**Goals and constraints by stakeholder**:
- Users: Want perfect security + ease of use + low cost (conflicting)
- Providers: Need market competitiveness + regulatory compliance + profit margins
- Regulators: Require auditability + consumer protection + compliance enforcement
- Researchers: Seek novel attacks (publish-or-perish) vs. responsible disclosure

#### 3.2 Environment and institutions

**Policy environment**:
- Evolving cryptocurrency regulations (SEC, EU MiCA, etc.)
- Data protection requirements (GDPR, CCPA)
- Financial custody regulations for institutional wallets
- Export controls on cryptographic technologies

**Market environment**:
- High-profile wallet hacks drive security awareness
- Competition for institutional customers with strict security requirements
- User expectations shaped by traditional banking security
- Insurance market for cryptocurrency custody emerging

**Technology environment**:
- Rapid advancement in cryptographic research
- Increasing sophistication of attack techniques
- Availability of secure hardware (HSMs, TEEs, secure enclaves)
- Cloud infrastructure security improvements

**Cultural factors**:
- "Not your keys, not your coins" ethos in crypto community
- Distrust of centralized custodians
- Tension between security purists and mass-market usability advocates

#### 3.3 Responsibility and room to maneuver

**Where to proactively take responsibility**:
- **Wallet providers** must own the end-to-end security of their implementations
- Must not blame "user error" for protocol-level vulnerabilities
- Should provide clear security guarantees and limitations
- Must maintain rapid response capability for discovered vulnerabilities

**Where to leave room for others**:
- **User choice**: Allow users to choose security/usability trade-offs
- **Integration flexibility**: Don't lock down ecosystems too tightly
- **Research community**: Welcome security research and responsible disclosure
- **Regulatory compliance**: Design for adaptability to evolving regulations

**Keeping future options open**:
- Design for protocol upgradability (without compromising existing keys)
- Maintain compatibility with emerging post-quantum cryptography
- Support multiple security models (different user risk profiles)
- Enable gradual migration paths for security improvements

---

### 4. Origins of the Problem (Aspect 4)

#### 4.1 Key historical nodes

**Stage 1: Early cryptocurrency (2009-2015) - Single-key model**
- Bitcoin and early altcoins used simple single-key wallets
- Security = protect the private key (hardware wallets, paper wallets)
- Fundamental vulnerability: single point of failure
- Major thefts (Mt. Gox 2014: 850,000 BTC) highlighted risks

**Stage 2: Multi-sig emergence (2012-2017) - On-chain distribution**
- Bitcoin multi-signature addresses introduced
- Required multiple signatures for transactions (on-chain)
- Limitations: Not all blockchains support multi-sig, poor UX, limited flexibility

**Stage 3: MPC adoption (2017-2021) - Off-chain computation**
- Threshold signature schemes (TSS) enable off-chain key distribution
- Promise: Security of multi-sig without on-chain complexity
- Early implementations focused on functionality over security guarantees
- Assumption: Distributing shares = secure (incomplete threat model)

**Stage 4: Attack discovery (2021-present) - Security realities**
- Researchers demonstrate practical key-extraction attacks
- Revelation: Single-party compromise can leak entire key
- Industry scramble to understand and mitigate
- Current state: Vulnerability acknowledged, solutions evolving

#### 4.2 Background vs. direct causes

**Deep background factors** (structural):
- Fundamental tension between usability and security in cryptography
- Scarcity of cryptographic expertise in industry
- Rapid commercialization without thorough security analysis
- Complexity of MPC protocols makes subtle vulnerabilities likely

**Immediate triggers** (proximate):
- Specific attack research publications (e.g., "Practical key-extraction attacks in leading MPC wallets", 2024)
- Competitive pressure to deploy MPC quickly
- Underestimation of adversary capabilities in threat models
- Implementation errors in translating research protocols to production

**Key distinction**:
- *Background*: MPC is inherently complex, and securing distributed systems is fundamentally hard
- *Direct*: Specific protocol choices and implementation decisions created exploitable vulnerabilities

#### 4.3 Deep structural issues

1. **Misaligned incentive structures**:
   - First-mover advantage in market rewards speed over security thoroughness
   - Security costs are upfront; breaches are future contingencies (discounted)
   - Users cannot evaluate security claims, creating lemon market dynamics

2. **Expertise scarcity**:
   - Very few experts can properly audit MPC implementations
   - Industry demand far exceeds supply of qualified cryptographers
   - Results in under-reviewed, potentially flawed deployments

3. **Inadequate threat modeling**:
   - Early MPC deployments assumed adversaries couldn't compromise parties
   - Underestimated sophistication of targeted attacks
   - Failed to consider adaptive adversaries learning from protocol observations

4. **Absence of comprehensive standards**:
   - No widely accepted certification framework for MPC wallets
   - Each provider implements custom variations
   - Difficult to compare security properties objectively

---

### 5. Problem Trends (Aspect 5)

#### 5.1 Current trend judgment

**If nothing changes, most likely trajectory**:

Within 6-12 months:
- Increased frequency of successful key-extraction attacks as techniques become more widely known
- Major incident likely involving loss of significant funds (>$100M) from a prominent MPC wallet
- Regulatory scrutiny intensifies, potentially leading to restrictions on MPC wallet deployment

Within 1-2 years:
- Loss of confidence in MPC wallet security model among institutional users
- Fragmentation between security-focused (slower, more complex) and usability-focused (less secure) solutions
- Possible market consolidation as providers with vulnerable implementations exit after breaches

Long-term (2-3 years):
- Without fundamental protocol improvements, MPC wallets may lose market share to alternative models
- Potential regulatory requirements for proof of security before deployment
- Industry-wide shift back to hardware-based single-point security or centralized custodians

#### 5.2 Early signals and "spots"

**Current observable signals**:

1. **Technical signals**:
   - Increasing research publications on MPC vulnerabilities (5+ papers in 2024)
   - White-hat researchers discovering and responsibly disclosing flaws
   - Growing complexity in proposed countermeasures (suggesting attack-defense arms race)

2. **Market signals**:
   - Insurance premiums rising for MPC wallet providers
   - Institutional customers demanding more stringent security audits
   - Some enterprise clients postponing MPC wallet adoption pending security improvements

3. **Behavioral signals**:
   - Security-conscious users avoiding MPC wallets or using them only for small amounts
   - Wallet providers rushing to implement patches after vulnerability disclosures
   - Increased marketing emphasis on security audits and certifications (defensive posture)

4. **Incident signals**:
   - Small-scale exploits in test environments
   - Near-misses where vulnerabilities were discovered before exploitation
   - Increasing sophistication of phishing and social engineering targeting MPC party operators

**What these foreshadow**:
- Without intervention, a major breach is not "if" but "when"
- Market is approaching a potential trust crisis
- Window for proactive solutions is narrowing (perhaps 6-12 months before major incident)

#### 5.3 Possible scenarios (6-24 months)

**Optimistic scenario (20% probability)**:
- Industry collaboration produces and rapidly adopts secure MPC protocol variants
- Major providers implement proactive key refresh and anomaly detection
- No major incidents occur, allowing smooth security improvements
- Regulatory frameworks emerge that support responsible innovation
- User confidence grows, MPC becomes standard for institutional custody
- Key metric: <0.1% of wallets experience successful attacks

**Baseline scenario (50% probability)**:
- Mixed progress: some providers improve, others remain vulnerable
- 1-2 moderate incidents (each $10-50M in losses) occur, creating urgency
- Regulatory response is reactive and somewhat heavy-handed
- Market fragments into security-first (complex, slower) and usability-first (riskier) tiers
- Institutional adoption slows pending security validation
- Key metric: 2-5% of wallet implementations suffer exploitable vulnerabilities

**Pessimistic scenario (30% probability)**:
- Major breach occurs soon (3-6 months), losing >$100M from prominent provider
- Cascade of copycat attacks exploiting similar vulnerabilities across industry
- Harsh regulatory response restricts MPC wallet deployment
- Loss of user and institutional confidence
- Market shift back toward centralized custodians or hardware wallets
- Several providers exit market or face bankruptcy from losses/liability
- Key metric: >10% of MPC wallet assets at risk, adoption drops >40%

---

### 6. Capability Reserves (Aspect 6)

#### 6.1 Existing capabilities

**Strengths available to address this problem**:

1. **Technical capabilities**:
   - Established cryptographic research community actively working on MPC security
   - Existing formal verification tools for cryptographic protocols
   - Available secure hardware (HSMs, TEEs) for enhanced party security
   - Growing body of documented best practices from early deployments

2. **Organizational capabilities**:
   - Some leading providers (e.g., Coinbase) have invested heavily in security teams
   - Industry forums (e.g., Blockchain Security Alliance) for knowledge sharing
   - Established bug bounty programs to crowdsource vulnerability discovery
   - Incident response frameworks from prior cryptocurrency breaches

3. **Strategic capabilities**:
   - First-mover advantage for providers who solve this credibly (market differentiation)
   - Ability to learn from adjacent industries (traditional finance, PKI)
   - Alliance potential among non-competing providers for shared security research
   - Regulatory engagement opportunity to shape favorable frameworks

4. **Communication capabilities**:
   - Technical documentation and white papers to explain security to sophisticated users
   - Security audit reports as credible third-party validation
   - Industry conferences and working groups for coordination

#### 6.2 Capability gaps

**Critical deficiencies amplifying the risk**:

1. **People and team gaps**:
   - **Severe shortage of cryptographic engineers** who understand both MPC theory and practical implementation
   - **Lack of secure coding culture** in many blockchain development teams (move-fast-break-things mentality)
   - **Insufficient security audit capacity**: only a handful of firms can properly audit MPC implementations
   - **Weak incident response preparation**: most providers lack tested breach response plans

2. **Mindset and culture gaps**:
   - **Overconfidence bias**: "Our implementation is different/better" leading to inadequate testing
   - **Not-invented-here syndrome**: Reluctance to adopt standardized, well-audited protocol implementations
   - **Short-term thinking**: Prioritizing feature velocity over security rigor
   - **Defensive communication**: Reluctance to disclose vulnerabilities or near-misses (fear of reputation damage)

3. **Process gaps**:
   - **Inadequate threat modeling processes**: Not systematically considering adversarial scenarios
   - **Insufficient testing of edge cases**: Focus on happy-path functionality
   - **Poor key hygiene in production**: Inadequate operational security around key ceremonies and party management
   - **Lack of continuous security monitoring**: Deploy-and-forget rather than ongoing vigilance

#### 6.3 Capabilities that can be built in the near term (1-6 months)

**High-priority, achievable capability development**:

1. **Immediate (1-2 months)**:
   - **Threat modeling workshops**: Bring together security experts and developers to systematically enumerate attack vectors
   - **Reference implementation analysis**: Deep security audit of 2-3 leading open-source MPC libraries
   - **Incident response tabletop exercises**: Practice breach scenarios to improve response readiness
   - **Security training for developers**: Focus on common MPC implementation pitfalls

2. **Short-term (2-4 months)**:
   - **Automated security testing tools**: Develop/adapt tools for continuous security testing of MPC implementations
   - **Secure-by-default configuration templates**: Create hardened deployment configurations
   - **Bug bounty program enhancement**: Increase rewards, provide test environments for security researchers
   - **Cross-industry security working group**: Establish regular meetings among providers for knowledge sharing

3. **Near-term (4-6 months)**:
   - **Formal verification of critical paths**: Apply formal methods to key-generation and signing logic
   - **Enhanced monitoring and anomaly detection**: Deploy systems to detect unusual signing patterns
   - **Cryptographic expertise recruitment**: Aggressively hire or contract specialized talent
   - **Industry-wide security standards draft**: Begin collaborative work on MPC wallet security certification framework

**Resource prioritization**:
- Focus 60% of resources on immediate threat mitigation (testing, auditing existing systems)
- Allocate 30% to near-term capability building (tools, processes, talent)
- Reserve 10% for longer-term research (next-generation protocols, post-quantum preparation)

---

### 7. Analysis Outline (Aspect 7)

#### 7.1 Structured outline

**Background**
- MPC wallets promise enhanced security through key distribution
- Billions of USD in cryptocurrency assets depend on MPC wallet security
- Recent research demonstrates practical key-extraction attacks

**Problem**
- Core contradiction: Single-party compromise can leak entire private key, defeating MPC security promise
- Affects wallet users, providers, and broader ecosystem
- Time-sensitive: Window for proactive solutions narrowing

**Analysis**
- Internal structure
  - Cryptographic protocols: Threshold signatures with inherent vulnerabilities
  - Key share management: Balance between security and operational overhead
  - Trust assumptions: Often too optimistic about adversary capabilities
- External environment
  - Stakeholders: Users, providers, regulators, researchers with conflicting interests
  - Market dynamics: Competition incentivizes speed over security
  - Regulatory landscape: Evolving, potentially restrictive if breaches occur
- Origins and trends
  - Historical evolution: Single-key → Multi-sig → MPC, each addressing prior vulnerabilities but introducing new ones
  - Current trajectory: Without intervention, major breach likely within 6-12 months
  - Structural issues: Expertise scarcity, inadequate standards, misaligned incentives

**Options**
- Option A: Protocol hardening (enhance existing MPC protocols)
- Option B: Hybrid approaches (combine MPC with hardware security)
- Option C: Architectural redesign (fresh-slate secure MPC protocols)
- Option D: Risk mitigation (insurance, rapid key refresh, anomaly detection)

**Risks & Follow-ups**
- Risk: Solution complexity makes implementation errors likely
- Risk: Performance trade-offs may harm user adoption
- Risk: Major breach occurs before solutions deployed
- Follow-up: Continuous monitoring and rapid response capability essential
- Follow-up: Industry coordination needed for standards adoption

#### 7.2 Key judgments

**Critical judgments requiring validation**:

1. **【Judgment 1】**: Single-party compromise leading to full key extraction is a fundamental protocol flaw, not just an implementation issue
   - *Assumption*: Current threshold signature schemes have theoretical vulnerabilities
   - *Validation needed*: Formal security analysis of leading MPC protocols

2. **【Judgment 2】**: A major breach is likely within 6-12 months without intervention
   - *Assumption*: Attack techniques will proliferate; adversaries are sophisticated and motivated
   - *Validation needed*: Threat intelligence on current attack activity; red-team assessments

3. **【Judgment 3】**: Protocol hardening can achieve provable security against single-party compromise without unacceptable performance degradation
   - *Assumption*: Security and performance are not fundamentally opposed for MPC
   - *Validation needed*: Benchmark tests of candidate secure protocols

4. **【Judgment 4】**: Institutional users will demand higher security even at cost of some usability/performance
   - *Assumption*: Risk tolerance varies; market will segment
   - *Validation needed*: Customer interviews and willingness-to-pay studies

5. **【Judgment 5】**: Industry can self-regulate through standards before external regulation is imposed
   - *Assumption*: Collaborative approaches are faster and more appropriate than regulation
   - *Validation needed*: Analysis of regulatory timelines and industry coordination feasibility

#### 7.3 Alternative paths

**Path A: Incremental hardening** (Build on existing protocols)
- *Positioning*: Pragmatic, fastest to deploy
- *Core approach*: Add key refresh, enhance party security, implement monitoring
- *Trade-offs*: Doesn't fully solve fundamental issues but buys time

**Path B: Next-generation protocols** (Fresh-slate redesign)
- *Positioning*: Ambitious, most secure
- *Core approach*: Develop and deploy provably secure MPC variants
- *Trade-offs*: Longer timeline, migration challenges, higher development cost

**Path C: Hybrid architecture** (MPC + hardware security)
- *Positioning*: Belt-and-suspenders approach
- *Core approach*: Combine MPC distribution with hardware-based isolation (HSMs, TEEs)
- *Trade-offs*: Higher operational cost, some centralization trade-offs

---

### 8. Validating the Answer (Aspect 8)

#### 8.1 Potential biases

**Stance biases in this analysis**:

1. **Security-first bias**: This analysis may overweight security concerns relative to practical business constraints
   - *Potential blind spot*: May underestimate users' tolerance for risk in exchange for convenience
   - *Mitigation*: Need to validate actual user preferences through research

2. **Technology-solutionism bias**: Assumes technical fixes exist for what may be fundamental trade-offs
   - *Potential blind spot*: Some security/usability/performance triangles may have no perfect solution
   - *Mitigation*: Consider non-technical approaches (insurance, process changes, education)

3. **Catastrophist bias**: May overestimate probability and nearness of major breach
   - *Potential blind spot*: Industry may successfully improve security without major incident
   - *Mitigation*: Track leading indicators; update probability assessments monthly

4. **Expert-centric bias**: Analysis assumes high sophistication; may not reflect average user perspective
   - *Potential blind spot*: Most users don't understand MPC and make decisions on different factors
   - *Mitigation*: Include non-expert stakeholder feedback in validation

#### 8.2 Required intelligence and feedback

**Critical data needed to validate key judgments**:

1. **For Judgment 1 (fundamental protocol flaw)**:
   - **Required**: Formal security proofs or counter-proofs for leading threshold signature schemes
   - **Source**: Cryptographic research papers, collaboration with academic experts
   - **Timeline**: 1-2 months for literature review, 3-6 months for original analysis
   - **Priority**: 【Critical】 - Determines whether solutions focus on implementation vs. protocol

2. **For Judgment 2 (breach timeline)**:
   - **Required**: Threat intelligence on active exploitation attempts, underground forum monitoring
   - **Source**: Security firms, bug bounty reports, penetration testing results
   - **Timeline**: Ongoing monitoring with monthly threat briefings
   - **Priority**: 【Critical】 - Determines urgency of response

3. **For Judgment 3 (security-performance trade-off)**:
   - **Required**: Benchmark data comparing secure protocol variants against current implementations
   - **Source**: Prototype implementations, controlled testing environments
   - **Timeline**: 2-3 months to implement and test prototypes
   - **Priority**: 【Important】 - Determines feasibility of recommended solutions

4. **For Judgment 4 (user preferences)**:
   - **Required**: Customer surveys, willingness-to-pay studies for security features
   - **Source**: Direct user research, analysis of adoption patterns for secure vs. convenient options
   - **Timeline**: 1-2 months for survey design and execution
   - **Priority**: 【Important】 - Determines market viability of secure solutions

5. **For Judgment 5 (regulatory timeline)**:
   - **Required**: Analysis of regulatory body activity, consultation timelines, precedent from similar situations
   - **Source**: Regulatory monitoring, legal analysis, industry association intelligence
   - **Timeline**: Ongoing monitoring with quarterly assessments
   - **Priority**: 【Important】 - Determines window for proactive vs. reactive response

**Pilot and experimental validation**:

- **Red-team exercise**: Commission independent security firm to attempt key extraction on hardened implementation
  - *Expected outcome*: Validate whether proposed mitigations actually prevent attacks
  - *Timeline*: 1 month
  - *Cost*: $50-100K

- **Performance benchmarking**: Test secure protocol variants under realistic load
  - *Expected outcome*: Quantify performance trade-offs
  - *Timeline*: 2 months
  - *Cost*: Engineering time + cloud infrastructure (~$30K)

- **User acceptance testing**: Pilot enhanced security features with small user cohort
  - *Expected outcome*: Validate usability impact
  - *Timeline*: 1 month
  - *Cost*: Minimal (internal resources)

#### 8.3 Validation plan

**Phased validation approach** (3-month cycle):

**Phase 1: Foundation validation (Month 1)**
- Conduct formal security analysis of current protocols (expert consultation)
- Execute red-team penetration testing on representative implementation
- Survey institutional customers on security requirements and trade-off preferences
- **Go/No-go decision**: Do fundamental protocol flaws exist that require architectural changes?

**Phase 2: Solution validation (Month 2)**
- Prototype 2-3 candidate mitigation approaches
- Benchmark performance impacts
- Small-scale pilot with security-conscious users
- **Go/No-go decision**: Can acceptable security be achieved within performance/usability constraints?

**Phase 3: Implementation validation (Month 3)**
- Deploy enhanced security features to subset of production traffic (phased rollout)
- Monitor anomaly detection systems for false positive rates
- Conduct follow-up red-team testing on hardened system
- Gather user feedback on any experience changes
- **Go/No-go decision**: Scale to full deployment vs. iterate further?

**Success criteria for validation**:
- Red-team cannot extract keys after 40+ hours of attempts
- Performance degradation <20% vs. baseline
- User satisfaction remains >4.0/5.0
- No critical vulnerabilities identified in formal analysis

---

### 9. Revising the Answer (Aspect 9)

#### 9.1 Parts likely to be revised

**Conclusions most vulnerable to change with new information**:

1. **Breach timeline estimate (6-12 months)**: Could be longer if attack techniques remain niche, or shorter if techniques proliferate faster
   - *Trigger for revision*: Monthly threat intelligence updates, any successful attack in the wild

2. **Feasibility of protocol hardening**: May discover that secure variants have unacceptable performance or that implementation complexity is prohibitive
   - *Trigger for revision*: Prototype benchmarking results, cryptographer feedback

3. **User willingness to accept trade-offs**: Actual user behavior may differ from stated preferences
   - *Trigger for revision*: Pilot program adoption metrics, A/B testing results

4. **Regulatory timeline**: Could accelerate dramatically if major breach occurs, or slow if industry demonstrates proactive improvements
   - *Trigger for revision*: Regulatory announcements, industry incident reports

5. **Cost-benefit of various solutions**: Engineering and operational costs may exceed estimates
   - *Trigger for revision*: Detailed implementation planning, vendor quotes

#### 9.2 Incremental adjustment approach

**Small-step trial and gradual refinement strategy**:

**Stage 1: Quick wins (Weeks 1-4)**
- Implement immediate mitigations: Enhanced monitoring, stricter party security policies
- Low-risk changes that provide some protection without major system modifications
- *Learning goal*: Identify operational friction points and easy wins
- *Revision trigger*: If quick wins prove more effective than expected, may adjust timeline; if operationally difficult, may need to reconsider organizational readiness

**Stage 2: Tactical improvements (Months 2-3)**
- Deploy key refresh mechanisms to limit compromise windows
- Introduce anomaly detection for unusual signing patterns
- Moderate-risk changes requiring coordination but not full protocol overhaul
- *Learning goal*: Validate that distributed systems changes can be deployed reliably
- *Revision trigger*: Performance impacts, false positive rates from anomaly detection inform trade-off recalibrations

**Stage 3: Strategic enhancements (Months 4-6)**
- Migrate to hardened protocol variants where validated
- Implement comprehensive security monitoring infrastructure
- Higher-risk changes with substantial security benefits
- *Learning goal*: Confirm that major security improvements are compatible with business operations
- *Revision trigger*: User feedback, incident rates, and competitive responses determine whether to accelerate or consolidate

**Stage 4: Ecosystem coordination (Months 6-12)**
- Collaborate on industry standards and best practices
- Support regulatory frameworks that enable secure innovation
- Ecosystem-level changes with long-term benefits
- *Learning goal*: Assess feasibility of industry coordination vs. competitive dynamics
- *Revision trigger*: Level of industry participation determines viability of standards-based approach

**Feedback loops for iteration**:
- Weekly: Internal security metrics review (anomalies, attempted intrusions)
- Monthly: Threat intelligence briefing, performance benchmarking
- Quarterly: User satisfaction surveys, stakeholder interviews
- As-needed: Rapid response to vulnerability disclosures or incidents

#### 9.3 "Better, not perfect" criteria

**Practical criteria for "good enough to act on"**:

1. **Security criterion**: No known exploits succeed in red-team testing (40+ hours of expert attempts)
   - *Not perfect*: Cannot prove security against all future attacks
   - *Better*: Demonstrably resistant to currently known attack techniques

2. **Performance criterion**: Transaction latency increase <20% compared to vulnerable baseline
   - *Not perfect*: Still slower than single-key wallets
   - *Better*: Competitive with other secure multi-party solutions

3. **Usability criterion**: User-facing experience unchanged or improved
   - *Not perfect*: Some power users may want more control/visibility
   - *Better*: No degradation for 95% of users

4. **Cost criterion**: Security improvements add <15% to operational costs
   - *Not perfect*: Higher than doing nothing
   - *Better*: Acceptable ROI given risk reduction (orders of magnitude less than potential breach costs)

5. **Auditability criterion**: Independent auditors can verify security properties in <80 hours
   - *Not perfect*: Still requires expert auditors
   - *Better*: Audit time reduced from current ~200+ hours, making frequent re-audits feasible

6. **Timeline criterion**: Initial deployment within 6 months, full rollout within 12 months
   - *Not perfect*: Ideally would be faster
   - *Better*: Faster than developing entirely new protocols; reduces window of vulnerability

**Meta-criterion**: "Good enough" means we've reduced the risk of catastrophic breach (>$100M loss) from ~30% to <5% in the next 12 months, while maintaining business viability.

---

### 10. Summary & Action Recommendations

#### 10.1 Core insights

1. **The fundamental contradiction is real and urgent**: MPC wallets' security promise—that key distribution prevents single-point failures—is undermined by practical key-extraction attacks compromising single parties. This is not merely an implementation flaw but reflects deeper protocol-level vulnerabilities in many current threshold signature schemes.

2. **Time is the critical constraint**: The window for proactive solutions is narrowing rapidly (estimated 6-12 months before likely major breach). Early signals from increasing research publications, rising insurance costs, and observable attack technique sophistication indicate the threat is materializing, not theoretical.

3. **Security-performance-usability trade-offs are manageable but require deliberate engineering**: Analysis suggests secure protocol variants can achieve acceptable performance (<20% degradation), but only with substantial cryptographic expertise and careful implementation. Half-measures will fail.

4. **The problem has structural roots beyond technology**: Expertise scarcity, misaligned incentives (speed-to-market vs. security rigor), and absence of industry standards amplify vulnerability. Technical solutions alone are insufficient without addressing these organizational and ecosystem factors.

5. **Multiple intervention points exist with different timescales**: Immediate tactical mitigations (key refresh, enhanced monitoring) can reduce risk within weeks, while strategic solutions (protocol hardening, industry standards) require 6-12 months. A layered approach maximizing near-term risk reduction while building long-term solutions is optimal.

#### 10.2 Near-term action list (0-3 months)

**【Critical / P0】**

1. **Immediate threat assessment and red-team testing**
   - *What*: Commission independent security firm to conduct penetration testing specifically targeting key-extraction attacks
   - *Who*: CISO (project sponsor), Head of Wallet Engineering (technical owner)
   - *Expected result*: Documented vulnerabilities and exploitability assessment; executive briefing on risk level
   - *Target completion*: Week 4
   - *Success metric*: Complete assessment report; executive team informed and aligned on urgency

2. **Deploy emergency mitigations**
   - *What*: Implement enhanced monitoring for anomalous signing patterns; strengthen security policies for party operators; initiate key refresh procedures
   - *Who*: Security Engineering team (implementation), DevOps (deployment)
   - *Expected result*: Monitoring dashboards operational; key refresh executed for highest-value wallets
   - *Target completion*: Week 6
   - *Success metric*: 100% coverage of high-value wallets (>$1M); monitoring capturing baseline behavior

3. **Cryptographic expert consultation**
   - *What*: Engage 2-3 leading MPC cryptographers for formal security analysis of current implementation and recommendations
   - *Who*: CTO (engagement), Research team (coordination)
   - *Expected result*: Formal security assessment report with specific recommendations for protocol improvements
   - *Target completion*: Week 8
   - *Success metric*: Written report with prioritized recommendations; expert commitment to ongoing advisory

**【Important / P1】**

4. **Customer communication and risk disclosure**
   - *What*: Prepare transparent communication to institutional customers about security enhancement roadmap; offer risk mitigation options (insurance, enhanced monitoring)
   - *Who*: Chief Customer Officer (lead), Legal (review), CISO (technical input)
   - *Expected result*: Customer communication plan; proactive outreach to top 20 institutional accounts
   - *Target completion*: Week 6
   - *Success metric*: Zero customer churn attributable to security concerns; positive feedback on transparency

5. **Prototype secure protocol variants**
   - *What*: Develop proof-of-concept implementations of 2-3 candidate hardened MPC protocols identified by expert consultation
   - *Who*: Cryptographic Engineering team (lead), QA (testing support)
   - *Expected result*: Working prototypes with benchmark data on performance vs. security trade-offs
   - *Target completion*: Week 10
   - *Success metric*: At least one candidate achieving <20% performance degradation with demonstrable security improvement

6. **Industry coordination initiation**
   - *What*: Reach out to 3-5 non-competing MPC wallet providers to propose joint security working group for standards development
   - *Who*: CEO or CTO (outreach), CISO (technical coordination)
   - *Expected result*: Agreement from at least 2 other major providers to participate in regular security knowledge sharing
   - *Target completion*: Week 8
   - *Success metric*: First working group meeting scheduled with confirmed participants; draft charter for collaboration

**【Optional / P2】**

7. **User research on security-usability preferences**
   - *What*: Conduct surveys and interviews with representative user segments to quantify willingness to accept security-related trade-offs
   - *Who*: Product Research team (lead), UX (survey design)
   - *Expected result*: Data-driven understanding of user risk tolerance and feature preferences
   - *Target completion*: Week 12
   - *Success metric*: Statistical significance (n>200 responses); clear segmentation of user preferences

#### 10.3 Risks and responses

**Risk 1: Major breach occurs before mitigations deployed** (High impact, Medium probability)
- **Impact level**: High (>$100M potential loss, severe reputational damage, regulatory consequences)
- **Trigger conditions**: Successful key-extraction attack against production wallet within next 3-6 months
- **Likelihood assessment**: 20-30% probability if only slow-moving strategic solutions pursued
- **Mitigation measures**:
  - *Preventive*: Prioritize emergency mitigations (monitoring, key refresh) in first 4 weeks
  - *Detective*: Enhanced monitoring to detect attacks in progress before full key extraction
  - *Responsive*: Pre-prepared incident response plan including key rotation, user notification, regulator communication
- **Contingency plan**: If breach occurs, immediately execute emergency key rotation for all wallets; engage crisis communications firm; offer affected users compensation/insurance claims; accelerate deployment of hardened protocols regardless of performance impact

**Risk 2: Secure protocol variants have unacceptable performance impact** (Medium impact, Medium probability)
- **Impact level**: Medium (strategic solutions delayed 6-12 months; competitive disadvantage; continued elevated risk)
- **Trigger conditions**: Prototype testing reveals >30% latency increase or >40% throughput reduction
- **Likelihood assessment**: 30-40% probability given inherent security-performance trade-offs
- **Mitigation measures**:
  - *Preventive*: Parallel development of multiple candidate protocols to increase probability of acceptable solution
  - *Adaptive*: Tiered service model where security-critical users accept performance trade-offs; mainstream users use optimized (but slightly less secure) variant
- **Contingency plan**: If no acceptable pure-software solution, pivot to hybrid architecture combining MPC with hardware security modules (HSMs); accept higher operational cost and some centralization; plan 12-month migration

**Risk 3: Expertise scarcity delays implementation** (Medium impact, High probability)
- **Impact level**: Medium (timeline延长3-6个月; quality may suffer from under-skilled implementation)
- **Trigger conditions**: Unable to recruit/contract sufficient cryptographic engineering talent within 1-2 months
- **Likelihood assessment**: 50-60% probability given severe global shortage of MPC experts
- **Mitigation measures**:
  - *Preventive*: Aggressive recruitment with above-market compensation; engage multiple consulting firms simultaneously; partner with academic institutions for research collaborations
  - *Adaptive*: Utilize well-audited open-source libraries rather than custom development; focus internal expertise on integration and validation rather than protocol development
- **Contingency plan**: If cannot build in-house capability, acquire or license technology from specialized cryptographic firms; accept higher ongoing costs for externally managed solution; focus internal resources on operational security and monitoring

**Risk 4: Industry coordination fails due to competitive dynamics** (Low impact, High probability)
- **Impact level**: Low (would lose benefits of shared standards and collective defense, but individual solutions remain viable)
- **Trigger conditions**: Providers unwilling to share security information; disagreement on standards; competitive concerns dominate
- **Likelihood assessment**: 60-70% probability given strong competitive dynamics and limited history of cooperation
- **Mitigation measures**:
  - *Preventive*: Engage neutral third party (academic institution, industry association) to facilitate; focus initial collaboration on non-competitive aspects (threat intelligence sharing); separate competitive features from baseline security standards
  - *Adaptive*: Proceed with internal solutions while maintaining open communication channels; publish security improvements as open-source to encourage adoption
- **Contingency plan**: If industry self-regulation fails, engage proactively with regulators to advocate for sensible standards rather than allowing reactive/restrictive regulations; position as industry leader in security to gain competitive advantage

---

**Document Status**: This analysis represents initial assessment based on available information as of 2025-11-28. Key judgments should be validated through the recommended intelligence gathering and testing within 3 months. Plan for quarterly review and revision as new data emerges.


## Problem 2: Complexity and Subtleties in Deploying MPC Wallets

### Context Recap

**Problem Title**: Cryptographic Complexity and Deployment Subtleties in Blockchain MPC Wallets

**Key Context**:
- MPC wallet deployment involves significant cryptographic design complexities and configuration subtleties that hinder secure implementation
- Current situation: Misconfigurations and vulnerabilities arise from complex integration with blockchain infrastructure
- Goal: Reduce deployment errors by 30% and increase developer adoption of best practices by 20% within 12 months
- Hard constraints: Balance security robustness with hardware limitations and user convenience; limited specialized cryptographic engineers
- Impact: Medium-term (1 year), affecting wallet adoption in mainstream financial services and decentralized applications

---

### 1. Problem Definition (Aspect 1)

#### 1.1 Problem and contradictions

**Core contradiction**: MPC technology offers superior security properties, but its inherent cryptographic complexity creates deployment barriers that undermine those security benefits through misconfiguration and implementation errors.

**Conflicting parties and goals**:
- **Wallet developers**: Need to implement MPC wallets quickly to meet market demand, but lack deep cryptographic expertise
- **Cryptographers**: Design theoretically secure protocols, but may not fully account for practical deployment complexities
- **End users**: Expect seamless integration and high availability, unaware of underlying complexity
- **Security auditors**: Must evaluate increasingly complex implementations with limited time and resources

**Key constraints**:
- Scarcity of engineers with both blockchain and advanced cryptography expertise
- Need to integrate with diverse blockchain protocols (each with unique requirements)
- Hardware limitations (mobile devices, varying computational power)
- End-user convenience requirements (fast onboarding, low latency)

#### 1.2 Goals and conditions

**Expected results**:
- **Primary goal**: Streamline MPC wallet deployment ensuring robust security with practical performance
- **Quantifiable targets**:
  - Reduce deployment errors by ≥30% within 12 months
  - Increase developer adoption of best practices by ≥20% within 12 months
  - Maintain or improve security guarantees while simplifying deployment

**Hard constraints**:
- Must work within existing blockchain infrastructure (cannot require protocol changes)
- Performance must meet user expectations (transaction signing <3 seconds)
- Hardware resource consumption must support mobile devices
- Development tools must be accessible to non-cryptography specialists

**Resource limits**:
- Limited pool of cryptographic engineers globally
- Development tool ecosystem is immature (few frameworks, limited documentation)
- Time pressure from competitive market dynamics

#### 1.3 Extensibility and common structure

**Multiple attribute perspectives**:

- **Virtual vs. Physical**:
  - *Physical*: Cryptographic libraries, node infrastructure, network connections, storage for key shares
  - *Virtual*: Protocol specifications, configuration parameters, trust assumptions, deployment best practices

- **Hard vs. Soft**:
  - *Hard*: Cryptographic algorithms, key generation ceremonies, signature aggregation logic
  - *Soft*: Configuration management, deployment workflows, operational procedures, testing methodologies

- **Latent vs. Manifest**:
  - *Manifest*: Known configuration errors, documented deployment challenges
  - *Latent*: Subtle timing issues, edge cases in unusual blockchain scenarios, interaction effects between components

- **Positive vs. Negative**:
  - *Positive*: Strong security when deployed correctly, flexibility to support multiple blockchains
  - *Negative*: High complexity tax, steep learning curve, fragile configurations, difficult debugging

**Reframing possibilities**:
1. From "simplify deployment" to "make errors impossible" (secure-by-default configurations, automated validation)
2. From "require expertise" to "embed expertise" (intelligent tooling that encodes best practices)
3. From "manual configuration" to "declarative specification" (describe intent, not implementation)
4. From "documentation" to "guardrails" (prevent bad configurations rather than warn about them)

---

### 2. Internal Logical Relations (Aspect 2)

#### 2.1 Key elements

**Roles**:
- Cryptographic protocol designers
- Wallet application developers
- DevOps/infrastructure engineers
- QA and security testers
- End users (indirect)

**Resources**:
- Cryptographic libraries (threshold signatures, secret sharing)
- Development frameworks and SDKs
- Documentation and best practices
- Testing and simulation tools
- Deployment infrastructure (cloud, on-premise)

**Processes**:
- Requirements analysis and protocol selection
- Key generation ceremony design
- Integration with blockchain nodes
- Configuration management
- Testing and validation
- Deployment and monitoring

**Rules**:
- Security best practices for MPC deployment
- Blockchain-specific requirements (transaction formats, signing algorithms)
- Compliance requirements (KYC/AML, custody regulations)
- Performance SLAs

#### 2.2 Balance and "degree"

**Critical balance points**:

1. **Flexibility vs. Simplicity**:
   - *Too rigid*: Cannot adapt to diverse use cases, blockchain-specific requirements
   - *Too flexible*: Overwhelming configuration options lead to errors
   - *Sweet spot*: Opinionated defaults for 80% of cases with clear extension points for special needs

2. **Abstraction vs. Control**:
   - *Too much abstraction*: Developers don't understand what's happening, can't troubleshoot issues
   - *Too little abstraction*: Exposed to low-level complexity, must understand deep cryptography
   - *Sweet spot*: Layered architecture where common operations are simple but inspection/override is possible

3. **Automation vs. Verification**:
   - *Too much automation*: "Magic" that works until it doesn't; difficult to audit
   - *Too little automation*: Manual steps prone to human error
   - *Sweet spot*: Automated workflows with explicit verification checkpoints and audit trails

4. **Performance vs. Robustness**:
   - *Optimize too aggressively*: Edge cases fail, subtle timing bugs, difficult to debug
   - *Too conservative*: Unacceptable latency, poor user experience
   - *Sweet spot*: Robust implementation with measured optimization only where necessary

#### 2.3 Key internal causal chains

**Chain 1: Complexity → Errors → Vulnerabilities**
```
Protocol complexity + Configuration subtlety → 
Developer misunderstanding or oversight → 
Misconfiguration or implementation bug → 
Security vulnerability or reliability issue → 
Exploitable attack surface or system failure
```

**Intervention points**:
- Reduce complexity through better abstractions (move complexity from developers to framework)
- Provide validation tools that catch errors before deployment
- Enable gradual learning (work with simple configurations before advanced)

**Chain 2: Expertise scarcity → Poor documentation → Adoption barriers**
```
Few experts understand MPC deeply → 
Documentation is incomplete or too technical → 
Developers struggle to implement correctly → 
Slow adoption or security issues → 
Negative feedback loop (reputation damage, further slowing adoption)
```

**Intervention points**:
- Invest in high-quality documentation with practical examples
- Create reference implementations that embody best practices
- Build communities of practice for knowledge sharing

---

### 3. External Connections (Aspect 3)

#### 3.1 Stakeholders

**Upstream stakeholders**:
- **Cryptographic research community**: Publishes protocols; often disconnected from deployment realities
- **Open-source library maintainers**: Provide cryptographic primitives; may not offer high-level abstractions
- **Cloud infrastructure providers**: Offer hosting; may not have MPC-specific features

**Downstream stakeholders**:
- **Application developers**: Integrate MPC wallets into products; need simple, reliable APIs
- **End users**: Experience consequences of deployment issues (downtime, security breaches)
- **Enterprises adopting MPC**: Require enterprise-grade reliability and support

**Side-line stakeholders**:
- **Competing wallet providers**: May or may not share learnings; competitive dynamics
- **Standards bodies**: Could establish best practices but are slow-moving
- **Training and education providers**: Could help address expertise gap

**Goals and constraints by stakeholder**:
- Developers: Want speed and simplicity vs. need for security and robustness
- Cryptographers: Seek theoretical elegance vs. need for practical deployability
- Enterprises: Require compliance and SLAs vs. constraints of immature technology
- Users: Expect reliability and convenience vs. complexity of underlying system

#### 3.2 Environment and institutions

**Technology environment**:
- Rapid evolution of blockchain protocols complicates cross-chain support
- Cryptographic libraries are often research-grade, not production-hardened
- Development tools for secure distributed systems are immature
- Cloud-native deployment patterns (containers, serverless) don't naturally fit MPC's stateful, coordination-intensive nature

**Market environment**:
- First-mover advantage creates pressure to deploy quickly
- User expectations shaped by simple custodial wallet UX
- Enterprise customers demand enterprise-grade reliability from startup-stage technology

**Institutional factors**:
- Regulatory requirements add compliance complexity on top of technical complexity
- Custody standards are evolving (unclear requirements)
- Insurance requirements for institutional custody may mandate specific configurations

#### 3.3 Responsibility and room to maneuver

**Where to proactively take responsibility**:
- **Framework developers** should own end-to-end deployment experience, not just provide low-level libraries
- **Wallet providers** must invest in operational expertise, not just development
- **Industry as a whole** should share learnings about deployment pitfalls (security through transparency)

**Where to leave room for others**:
- Don't lock developers into proprietary frameworks (support standards)
- Allow customization for specialized use cases while providing safe defaults
- Enable ecosystem of tools and services (monitoring, testing, auditing)

**Keeping future options open**:
- Design for protocol evolution (can upgrade cryptographic primitives)
- Maintain compatibility with emerging standards
- Support both cloud and on-premise deployment models

---

### 4. Origins of the Problem (Aspect 4)

#### 4.1 Key historical nodes

**Stage 1: Academic MPC research (1980s-2010s)**
- MPC protocols developed in academic settings focused on theoretical properties
- Deployment considerations secondary to security proofs
- Gap between "provably secure" and "secure when deployed"

**Stage 2: Blockchain emergence and single-key wallets (2009-2016)**
- Early cryptocurrency wallets were simple: one private key, straightforward implementation
- Security = protect the key; deployment was relatively simple
- Created user expectations for wallet simplicity

**Stage 3: Initial MPC-for-blockchain projects (2017-2020)**
- First attempts to apply MPC to blockchain key management
- Early implementations were custom, one-off projects
- Deployment was artisanal, requiring deep expertise for each installation
- Little knowledge sharing due to competitive dynamics

**Stage 4: MPC wallet productization (2020-present)**
- Attempts to package MPC as "products" and "services"
- Tension between making it accessible and maintaining security
- Proliferation of implementations with varying quality
- **Current state**: Complexity acknowledged as barrier; industry searching for solutions (Coinbase WaaS example shows awareness)

#### 4.2 Background vs. direct causes

**Deep background factors**:
- **Inherent complexity of MPC**: Cryptographic protocols are fundamentally complex; no simple MPC
- **Interdisciplinary gap**: Combines cryptography, distributed systems, blockchain—few experts in all three
- **Immaturity of tooling**: Ecosystem hasn't yet developed the abstraction layers that exist for other complex technologies

**Immediate triggers**:
- Rush to productize MPC without investing in developer experience
- Underestimation of deployment complexity in diverse real-world environments
- Insufficient testing across blockchain variations and edge cases
- Documentation focused on "what" and "why" without adequate "how"

#### 4.3 Deep structural issues

1. **Cryptography research incentives**: Academic culture rewards novel protocols, not deployable systems
   - Publications focus on security proofs, not implementation guidance
   - Little incentive to make protocols "deployment-friendly"

2. **Knowledge distribution**: MPC expertise concentrated in a few individuals/organizations
   - High consulting rates create barriers to accessing expertise
   - Limited knowledge transfer mechanisms

3. **Tooling gap**: Lack of mature, opinionated frameworks
   - Existing libraries are low-level (require deep expertise)
   - No "Rails for MPC" that makes best practices automatic

4. **Testing challenges**: Difficult to test MPC systems comprehensively
   - Must test across combinations of configurations, blockchains, failure scenarios
   - Lack of standardized test suites and simulation environments

---

### 5. Problem Trends (Aspect 5)

#### 5.1 Current trend judgment

**If nothing changes**:

Within 6-12 months:
- Continued deployment errors leading to security incidents and reliability problems
- Fragmentation: Each organization learns similar lessons independently (redundant, inefficient)
- Some high-profile failures discourage adoption
- Expertise gap widens as demand grows faster than supply

Within 1-2 years:
- Market bifurcation: 
  - A few well-funded organizations with deep expertise succeed
  - Many smaller players struggle or produce vulnerable implementations
- Potential regulatory intervention if security incidents accumulate
- Possible consolidation around 2-3 dominant platforms (reduces diversity but may improve quality)

Long-term (2-3 years):
- Without ecosystem investment in tooling and education, MPC wallets remain niche (only for enterprises with resources)
- Alternative approaches (hardware security, trusted execution environments) may gain ground
- Or: Mature frameworks emerge, enabling broader adoption

#### 5.2 Early signals and "spots"

**Current observable signals**:

1. **Technical signals**:
   - Increasing GitHub issues on MPC libraries related to deployment and configuration
   - Growing number of "how-to" blog posts and tutorials (indicates demand for practical guidance)
   - Security audits revealing configuration errors more than protocol flaws

2. **Market signals**:
   - Coinbase and other leaders highlighting deployment complexity in public communications
   - Demand for "MPC-as-a-Service" solutions (developers want to outsource complexity)
   - Long sales cycles for enterprise MPC wallets (due diligence reveals deployment concerns)

3. **Community signals**:
   - Developer forum questions showing repeated confusion on same issues
   - Few contributors to open-source MPC projects (high barrier to contribution)
   - Requests for workshops, training, certifications

4. **Organizational signals**:
   - Companies hiring "MPC engineers" as specialized role
   - Investment in internal tooling and frameworks by leading adopters
   - Some organizations abandoning MPC implementations mid-project (too difficult)

**What these foreshadow**:
- Deployment complexity is recognized as a critical bottleneck
- Demand is building for better abstractions and tooling
- Market may be receptive to solutions (commercial or open-source frameworks)

#### 5.3 Possible scenarios (6-24 months)

**Optimistic scenario (30% probability)**:
- Collaborative open-source effort produces comprehensive MPC deployment framework
- Industry leaders (Coinbase, etc.) contribute learnings and reference implementations
- Training and certification programs emerge
- Deployment error rates decline by >50%
- MPC wallet adoption accelerates, including among mid-sized organizations
- Key metric: >100 production MPC wallet deployments from diverse organizations with <5% experiencing security issues from misconfigurations

**Baseline scenario (50% probability)**:
- Incremental improvements: better documentation, some tooling enhancements
- Fragmented solutions: multiple frameworks, none dominant
- Deployment still requires significant expertise but gradually becoming more accessible
- Adoption grows slowly, primarily among well-resourced organizations
- Periodic security incidents from deployment errors continue
- Key metric: MPC wallet market grows 30-50% but remains <10% of total wallet market

**Pessimistic scenario (20% probability)**:
- High-profile deployment failures damage MPC wallet reputation
- Talent shortage worsens as demand outstrips supply
- Tooling remains immature; fragmentation increases
- Regulatory response to incidents constrains deployment (additional compliance requirements add complexity)
- MPC wallets remain niche; simpler alternatives (custodial, hardware) gain market share
- Key metric: MPC wallet adoption stagnates or declines; <50 new production deployments, multiple

 shutdowns

---

### 6. Capability Reserves (Aspect 6)

#### 6.1 Existing capabilities

**Strengths available**:

1. **Technical capabilities**:
   - Several production-grade MPC libraries exist (though low-level)
   - Cloud infrastructure supports distributed deployments
   - Blockchain node infrastructure is mature
   - Security auditing methodologies are established

2. **Organizational capabilities**:
   - Some organizations (Coinbase, Fireblocks, etc.) have successfully deployed at scale (learnings exist)
   - Academic connections: universities can contribute research and training
   - Open-source community: potential to collaborate on shared tooling

3. **Strategic capabilities**:
   - Clear market demand (pull for solutions)
   - Enterprises willing to pay for managed services (economic viability)
   - Opportunity for differentiation through superior deployment experience

#### 6.2 Capability gaps

**Critical deficiencies**:

1. **People and team gaps**:
   - **Severe shortage of MPC specialists**: Cannot hire/train fast enough to meet demand
   - **Interdisciplinary gap**: Few individuals combining cryptography, distributed systems, and blockchain expertise
   - **Documentation skill gap**: Cryptographers may not excel at practical documentation

2. **Mindset and culture gaps**:
   - **"Cryptography is special" mindset**: Belief that it's inevitably complex, resisting abstraction
   - **Not-invented-here**: Organizations reluctant to share deployment learnings (competitive concern)
   - **Perfectionism**: Desire for theoretically optimal solutions over pragmatic, deployable ones

3. **Process and tooling gaps**:
   - **Lack of testing frameworks**: No standard test suites for validating MPC deployments
   - **Immature CI/CD integration**: MPC deployments don't fit standard DevOps workflows
   - **Poor observability**: Difficult to monitor and debug MPC systems in production
   - **No deployment playbooks**: Each organization reinvents deployment processes

#### 6.3 Capabilities that can be built in the near term (1-6 months)

**High-priority, achievable capability development**:

1. **Immediate (1-2 months)**:
   - **Deployment checklist and runbook**: Document common pitfalls and verification steps
   - **Configuration validation tool**: Automated checker for common misconfigurations
   - **Reference architecture diagrams**: Visual guides for standard deployment topologies
   - **Community of practice**: Regular meetups/calls for MPC developers to share learnings

2. **Short-term (2-4 months)**:
   - **Hardened reference implementation**: Well-documented, audited example deployment
   - **Test harness**: Simulate various blockchain scenarios for integration testing
   - **Deployment templates**: Infrastructure-as-code for common environments (AWS, GCP, Kubernetes)
   - **Troubleshooting guide**: Diagnostic procedures for common issues

3. **Near-term (4-6 months)**:
   - **SDK with high-level abstractions**: Wrap low-level libraries with developer-friendly APIs
   - **Observability stack**: Monitoring, logging, alerting tailored for MPC systems
   - **Training program**: Structured curriculum for developers new to MPC
   - **Certification program**: Validate knowledge and create pool of qualified practitioners

---

### 10. Summary & Action Recommendations

#### 10.1 Core insights

1. **Complexity is inherent but can be managed**: MPC protocols are fundamentally complex, but deployment complexity can be dramatically reduced through proper abstractions, tooling, and knowledge sharing—the problem is solvable engineering, not insurmountable mathematics.

2. **The expertise gap is the binding constraint**: Shortage of qualified practitioners limits adoption more than any technical factor; must create parallel paths (train more experts AND reduce expertise requirements through better tools).

3. **Deployment knowledge is scattered and siloed**: Organizations are independently learning the same lessons; consolidating and sharing this knowledge would provide 10x leverage for the ecosystem.

4. **Tooling gap is actionable opportunity**: Unlike protocol-level security challenges, improved deployment tooling can be built in 6-12 months and would address 70% of current deployment errors.

5. **Industry leadership is emerging**: Coinbase and others acknowledging these challenges publicly creates opening for collaborative solutions; timing is favorable for ecosystem initiatives.

#### 10.2 Near-term action list (0-3 months)

**【Critical / P0】**

1. **Create comprehensive deployment documentation**
   - *What*: Develop step-by-step deployment guide covering common scenarios, pitfalls, and troubleshooting; include decision trees for configuration choices
   - *Who*: Engineering team with MPC deployment experience (authors), Technical Writer (editor)
   - *Expected result*: 50+ page documentation covering end-to-end deployment; reduces support queries by >40%
   - *Target completion*: Week 8
   - *Success metric*: Published, shared with community; positive feedback from ≥10 external developers

2. **Build configuration validation tool**
   - *What*: Automated tool that checks MPC wallet configurations against best practices; identifies common errors before deployment
   - *Who*: Developer Tools team (lead), Security team (requirements)
   - *Expected result*: CLI tool that validates configuration files; catches ≥80% of known misconfiguration patterns
   - *Target completion*: Week 10
   - *Success metric*: Open-sourced, integrated into recommended deployment workflow; ≥5 external organizations adopt

**【Important / P1】**

3. **Establish MPC Developer Working Group**
   - *What*: Initiate monthly virtual meetings bringing together developers from multiple organizations to share deployment experiences and best practices
   - *Who*: CTO or Engineering Director (sponsor), Community Manager (organizer)
   - *Expected result*: ≥8 organizations participating; shared documentation of lessons learned
   - *Target completion*: Week 6 (first meeting)
   - *Success metric*: Consistent participation (≥6 orgs at each meeting); collaborative outcomes (shared tools, documentation)

4. **Develop reference implementation**
   - *What*: Create well-documented, audited reference implementation demonstrating best practices for common deployment scenario
   - *Who*: Senior MPC Engineers (implementation), Security team (audit)
   - *Expected result*: Open-source repository with code, documentation, deployment scripts
   - *Target completion*: Week 12
   - *Success metric*: ≥3 external organizations use as starting point for their deployments

**【Important / P1】**

5. **Prototype high-level SDK**
   - *What*: Develop proof-of-concept SDK abstracting low-level MPC operations; focus on common use cases with secure defaults
   - *Who*: Developer Experience team (lead), MPC experts (advisors)
   - *Expected result*: Alpha SDK reducing LOC for typical integration by >60%; internal pilot with product team
   - *Target completion*: Month 3
   - *Success metric*: Internal product team successfully integrates; feedback indicates significant DX improvement

#### 10.3 Risks and responses

**Risk 1: Knowledge sharing undermines competitive advantage** (Medium impact, Medium probability)
- **Impact level**: Medium (competitors benefit from shared knowledge; but all boats rise)
- **Trigger conditions**: Competitive intelligence shows rivals using shared learnings to catch up
- **Mitigation**: Focus sharing on baseline security/deployment best practices (non-differentiating); compete on performance, features, service quality
- **Contingency plan**: If competitive concerns dominate, shift to consulting/training model (monetize expertise); or focus on open-source reputation as competitive differentiator

**Risk 2: Tooling investment doesn't reduce deployment errors as expected** (Medium impact, Low probability)
- **Impact level**: Medium (wasted resources; deployment complexity remains barrier)
- **Trigger conditions**: After tool deployment, error rates don't decrease by ≥20% within 6 months
- **Mitigation**: Early user testing of tools; iterate based on feedback; measure baseline error rates before tool deployment
- **Contingency plan**: Pivot to training/certification approach if tooling alone insufficient; consider managed service model

**Risk 3: Expertise shortage prevents scaling beyond small pilot** (Low impact, Medium probability)
- **Impact level**: Low (limits pace of ecosystem development but doesn't halt it)
- **Trigger conditions**: Cannot staff working group or reference implementation project adequately
- **Mitigation**: Engage academic partners; offer internships/fellowships; contract specialized consultancies
- **Contingency plan**: Narrow scope to most critical deliverables; extend timelines; focus on force-multiplier tools over comprehensive solutions


## Problem 3: Difficulty of Private Key Recovery and Backup Mechanisms

### Context Recap

**Problem Title**: Secure and User-Friendly Key Recovery in Hardware and MPC Wallets

**Key Context**:
- Recovery mechanisms must preserve "unicity" (unique hardware ownership) in hardware wallets while offering robust, user-friendly options for MPC wallets
- Current situation: Traditional backups (cloning seeds) compromise security; recovery processes are complex and error-prone
- Goal: Achieve >90% recovery success rates without security compromise; reduce key leakage risks to near-zero
- Hard constraints: Cannot expose private keys during backup/recovery; limited user technical expertise; regulatory compliance requirements
- Impact: Medium-to-long term (1-2 years), affecting millions of users globally, especially high-value asset holders

---

### 1. Problem Definition

**Core contradiction**: Users need reliable access to funds after device loss, but traditional backup methods (seed cloning) fundamentally undermine the security properties MPC wallets are designed to provide.

**Conflicting goals**:
- **Security requirement**: Maintain key unicity and prevent exposure
- **Usability requirement**: Enable non-technical users to recover access reliably
- **Regulatory requirement**: Support inheritance and legal recovery without exposing keys
- **Business requirement**: Minimize support costs from failed recovery attempts

**Extensibility perspectives**:
- **Virtual vs. Physical**: Physical = key shares, hardware devices; Virtual = recovery policies, trust relationships
- **Soft vs. Hard**: Hard = cryptographic recovery protocols; Soft = social recovery, multi-party approval processes
- **Reframing**: From "backup keys" to "backup access rights"; from "clone seeds" to "delegate recovery capabilities"

---

### 2. Internal Logical Relations

**Key elements**: Recovery protocols (SSS, smart contracts), trusted recovery parties, biometric data, user devices, cryptographic proofs

**Critical balance points**:
1. **Security vs. Recoverability**: Too secure → users lose funds; Too recoverable → attackers gain access
2. **Automation vs. Control**: Automated recovery convenient but risky; Manual recovery secure but failure-prone
3. **Decentralization vs. Reliability**: Fully decentralized recovery may fail if parties unavailable; Centralized recovery creates honeypots

**Key causal chain**:
```
Device loss/failure → Recovery initiation → Identity verification → 
Trust party coordination → Key share reconstruction → Access restoration
```
**Failure points**: Each step can fail due to complexity, unavailable parties, or user error

---

### 3. External Connections

**Stakeholders**:
- **Upstream**: Cryptographic researchers (design protocols), Hardware manufacturers (secure elements), Biometric vendors
- **Downstream**: End users (need reliable recovery), Heirs (inheritance scenarios), Courts (legal recovery orders)
- **Side-line**: Key management services, Custodial backup providers, Insurance

**Environment**:
- **Regulatory**: GDPR (right to erasure conflicts with blockchain immutability), Inheritance laws
- **Technical**: Biometric privacy concerns, Smart contract reliability
- **Social**: User trust in recovery parties, Family/social network availability

**Responsibility**: Wallet providers must own recovery UX end-to-end; Cannot blame users for complexity

---

### 4. Origins of the Problem

**Historical evolution**:
- **Stage 1 (2009-2015)**: Paper wallets and seed phrases—simple but requires secure storage
- **Stage 2 (2014-2018)**: Hardware wallets—added security but seed backup still cloneable
- **Stage 3 (2018-2022)**: MPC wallets—distributed keys but recovery becomes coordination problem
- **Stage 4 (2022-present)**: Exploring SSS, smart contracts, biometrics—no consensus solution

**Background causes**: Fundamental tension between security (no single point of access) and recoverability (need fallback access)

**Direct causes**: Underinvestment in recovery UX; focus on normal operations over edge cases; regulatory uncertainty

---

### 5. Problem Trends

**Current trajectory without intervention**:
- 6-12 months: Increasing user frustration; fund loss from failed recovery attempts
- 1-2 years: Regulatory scrutiny if significant funds become irretrievable; Class-action lawsuits possible

**Early signals**:
- Rising support tickets related to recovery
- Social media complaints about lost access
- Regulatory inquiries about consumer protection

**Scenarios (12-24 months)**:
- **Optimistic (25%)**: Breakthrough in usable cryptographic recovery; Standard protocols emerge; Recovery success >90%
- **Baseline (55%)**: Incremental improvements; Fragmented solutions; Some providers excel, others lag; Recovery success 70-85%
- **Pessimistic (20%)**: High-profile cases of unrecoverable funds; Regulatory mandates for custodial recovery options; MPC adoption suffers

---

### 6. Capability Reserves

**Existing strengths**:
- Proposed cryptographic solutions exist (SSS, smart contract registries, BIFS)
- Biometric technology mature and widely available
- Social recovery precedents (Argent wallet, etc.)

**Capability gaps**:
- **User education**: Most users don't understand recovery until they need it (too late)
- **Testing infrastructure**: Difficult to test recovery at scale without risking real funds
- **Legal frameworks**: Unclear how to handle inheritance legally while preserving cryptographic security
- **Cross-platform coordination**: Recovery across different wallet implementations challenging

**Near-term buildable capabilities (1-6 months)**:
- Recovery simulation tools (let users practice recovery in safe environment)
- Standardized recovery APIs (enable cross-wallet recovery)
- Recovery success monitoring dashboards
- User-friendly recovery wizard interfaces

---

### 7-9. Analysis, Validation, and Revision

**Key judgments**:
1. Social recovery (trusted contacts) is more user-friendly than complex cryptographic schemes for mainstream users
2. Biometric-based recovery can work if privacy-preserving (BIFS approach)
3. Smart contract recovery registries enable inheritance without exposing keys

**Validation needs**:
- User testing of recovery flows with non-technical users (target: >90% success)
- Security analysis of proposed protocols (formal verification)
- Legal review of inheritance mechanisms across jurisdictions

**Likely revisions**:
- User preference data may show different priorities than assumed
- Security/usability trade-offs may require tiered offerings (expert mode vs. simple mode)

**"Good enough" criteria**:
- Recovery success rate >90% for users who set up properly
- No cryptographic key exposure during recovery process
- Recovery time <24 hours for social recovery, <1 hour for emergency cases
- Clear legal pathway for inheritance

---

### 10. Summary & Action Recommendations

**Core insights**:
1. Recovery is not an afterthought but a primary design constraint—must be designed-in from the start
2. One-size-fits-all recovery won't work; need multiple options for different user sophistication levels
3. Social recovery (trusted contacts) likely most pragmatic for mainstream adoption despite being less "pure" cryptographically
4. User education before recovery is needed is critical success factor

**Near-term actions (0-3 months)**:

**【Critical / P0】**
1. **User research on recovery preferences and pain points**
   - Owner: Product team; Completion: Week 4
   - Metric: Survey ≥200 users across user segments; Identify top 3 recovery scenarios

2. **Prototype social recovery implementation**
   - Owner: Engineering team; Completion: Week 10
   - Metric: Working prototype with 3 trusted contacts; <5 minute setup time

**【Important / P1】**
3. **Recovery simulation tool development**
   - Owner: DevTools team; Completion: Week 12
   - Metric: Tool allowing users to practice recovery without risk; >80% completion rate in testing

4. **Legal framework analysis for inheritance**
   - Owner: Legal team + external counsel; Completion: Week 8
   - Metric: Documented approach for top 5 jurisdictions; Compliance pathway identified

**Risks and responses**:
- **Risk**: Social recovery undermines security if attackers compromise trusted contacts
  - **Mitigation**: Require M-of-N approvals with time delays; Alert user of recovery attempts
- **Risk**: Users don't set up recovery until too late
  - **Mitigation**: Mandatory setup during onboarding; Periodic recovery drills; Incentivize setup

---

## Problem 4: Balancing Security and Usability in Private Key Management

### Context Recap

**Problem Title**: Security-Usability Trade-off in MPC Wallet Private Key Management

**Key Context**:
- MPC enhances security but introduces complexity in user interaction (onboarding, signing, recovery)
- Goal: Increase user adoption by >20%, reduce key management errors by ≥30% within 6-12 months
- Hard constraints: Human factors, technological limitations in abstracting crypto, protocol complexity
- Impact: Short-to-medium term (6-12 months), affecting user satisfaction and mass adoption globally

---

### 1. Problem Definition

**Core contradiction**: Strongest security measures often create worst user experiences, while user-friendly designs may sacrifice security—fundamental tension without perfect resolution.

**Conflicting parties**:
- **Security team**: Wants maximum protection, multiple verification steps, explicit user control
- **Product/UX team**: Wants seamless experience, minimal friction, Apple-like simplicity
- **Users**: Say they want security but behave as though convenience is priority
- **Regulators**: May mandate certain security measures regardless of UX impact

**Reframing possibilities**:
- From "security vs. usability" to "security appropriate to context" (different security levels for different transaction amounts)
- From "educate users on security" to "make insecurity impossible" (secure-by-default designs)
- From "explicit user control" to "intelligent assistance" (AI-assisted anomaly detection replaces user vigilance)

---

### 2. Internal Logical Relations

**Key elements**:
- User interfaces (mobile app, web, hardware device interactions)
- Authentication methods (passwords, biometrics, MPC signing)
- Transaction workflows (initiation, approval, execution)
- Security controls (rate limiting, amount thresholds, multi-party approval)

**Critical balance**: 
- **Friction vs. Protection**: Each security step reduces attack surface but increases abandonment risk
- **Transparency vs. Simplicity**: Showing users what's happening builds trust but creates cognitive load
- **Flexibility vs. Guardrails**: Power users want control; Most users need protection from themselves

**Causal chain**:
```
Complex security UX → User confusion/frustration → 
Errors or abandonment → Reduced adoption or security incidents → 
Negative reputation → Further adoption challenges
```

---

### 3. External Connections

**Stakeholders**:
- **Behavioral economists/UX researchers**: Understand user psychology and decision-making
- **Accessibility advocates**: Ensure solutions work for diverse abilities
- **Customer support**: Deal with consequences of UX failures
- **Competitors**: Set expectations through their UX choices

**Environment**:
- **Cultural**: Varying security consciousness across demographics and geographies
- **Educational**: Wide variance in technical literacy
- **Economic**: Willingness to tolerate friction correlates with asset value

**Responsibility**: Cannot blame users for "not understanding security"—provider's job to make security usable

---

### 4-5. Origins and Trends

**Historical pattern**:
- Early crypto wallets required technical expertise (command-line, manual key management)
- Coinbase/custodial wallets proved mainstream wants simplicity
- MPC wallets trying to bridge: self-custody security + custodial convenience
- Current challenge: Haven't yet found the right balance

**Trends without intervention**:
- Mainstream users stick with custodial (Coinbase, exchanges) despite security risks
- MPC wallets remain niche for sophisticated/institutional users
- Gap between security-first and usability-first products widens

**Signals**:
- App store ratings mentioning "too complicated"
- High onboarding abandonment rates
- Support tickets about "how do I...?"

---

### 6. Capability Reserves

**Existing strengths**:
- Decades of HCI research on security-usability
- Successful patterns from other domains (password managers, 2FA)
- Biometrics now ubiquitous and user-accepted

**Gaps**:
- **MPC-specific UX research**: Little published work on optimal UX patterns for threshold signatures
- **User mental models**: Users don't understand distributed key concepts
- **Testing with diverse users**: Most testing with tech-savvy early adopters

**Buildable capabilities**:
- Comprehensive UX testing with representative user panels
- Pattern library of security-usable MPC UX components
- Progressive complexity UI (simple by default, advanced mode available)

---

### 7-9. Analysis, Validation, Revision

**Key judgments**:
1. Biometric authentication can provide security without UX degradation (already accepted pattern)
2. Contextual security (adapt to transaction risk) is more usable than uniform high-security for all operations
3. Most security errors come from edge cases users rarely encounter (recovery, account compromise)—need extra hand-holding there

**Validation**:
- A/B testing of UX variants with diverse user cohorts
- Measure: Completion rates, error rates, time-to-complete, satisfaction scores
- Security testing: Does simplified UX introduce exploitable vulnerabilities?

**"Good enough" criteria**:
- Onboarding completion >85% (vs. typical 60%)
- Transaction completion <30 seconds for routine transactions
- User satisfaction ≥4.0/5.0
- Security incident rate <0.1% (comparable to best-in-class custodial)

---

### 10. Summary & Action Recommendations

**Core insights**:
1. "Security vs. usability" is false dichotomy—need "usable security" (both required)
2. Context matters: Different security for different transactions (risk-adaptive)
3. Focus on most common paths (80% of users, 80% of transactions)—optimize these relentlessly
4. Biometrics are breakthrough—leverage

 them extensively
5. Progressive disclosure: Simple surface, complexity available when needed

**Near-term actions (0-3 months)**:

**【Critical / P0】**
1. **UX research with mainstream users**
   - Owner: UX Research team; Completion: Week 6
   - Metric: ≥50 user sessions across demographics; Identify top 5 friction points; Quantify abandonment causes

2. **Biometric-first signing flow**
   - Owner: Mobile Engineering + Security; Completion: Week 10
   - Metric: Biometric approval for transactions <$1000; Completion time <15 seconds; User satisfaction >4.2/5

**【Important / P1】**
3. **Risk-adaptive security prototype**
   - Owner: Product + Engineering; Completion: Week 12
   - Metric: Low-value transactions (<$100) single-tap approval; High-value (>$10k) multi-factor; Measure completion rates vs. current

4. **Onboarding optimization**
   - Owner: Growth Product team; Completion: Week 8
   - Metric: Reduce onboarding steps from current 12 to ≤5 for basic account; Increase completion rate by ≥20 percentage points

**Risks and responses**:
- **Risk**: Simplified UX exploitable by attackers
  - **Mitigation**: Comprehensive security review of new flows; Red-team testing; Behavioral anomaly detection as backstop
- **Risk**: Power users revolt against "dumbing down"
  - **Mitigation**: Maintain "advanced mode" with full control; Make simple mode the default but not the only option

---

## Problem 5: Scalability and Performance Challenges in Heterogeneous Environments

### Context Recap

**Problem Title**: MPC Performance Bottlenecks in Heterogeneous Computing Environments

**Key Context**:
- MPC protocols suffer from "weakest link" problem: Performance limited by slowest participant
- Current situation: Heterogeneous nodes (varying hardware, network, geography) cause stalls and latency
- Goal: Achieve near real-time throughput (milliseconds latency), proportional to demand, comparable to single-key wallets
- Hard constraints: Synchronous MPC communication requirements, varied node capabilities, security preservation
- Impact: Medium-term (6-18 months), affecting large-scale deployments and high-transaction-volume use cases

---

### 1. Problem Definition

**Core contradiction**: MPC security requires synchronous coordination among parties, but achieving low latency requires fast execution, which is impossible when parties have asymmetric capabilities.

**Conflicting goals**:
- **Security requirement**: All parties must participate (threshold t-of-n)
- **Performance requirement**: Low-latency response (milliseconds) for user experience
- **Practical reality**: Parties have different hardware, network speeds, geographic locations
- **Cost constraint**: Cannot require all parties to have identical, expensive infrastructure

**Reframing**:
- From "make all parties fast" to "design protocols that tolerate slow parties"
- From "synchronous rounds" to "asynchronous with eventual consistency where safe"
- From "all parties always participate" to "dynamic party selection based on availability/performance"

---

### 2. Internal Logical Relations

**Key elements**:
- MPC protocol rounds (key generation, signing)
- Party infrastructure (CPU, network bandwidth, geographic location)
- Communication patterns (point-to-point, broadcast)
- Coordination mechanisms (leader election, timeout handling)

**Critical balance**:
- **Parallelization vs. Coordination overhead**: More parallel operations faster but harder to coordinate
- **Number of parties vs. Performance**: More parties = better security but slower coordination
- **Fault tolerance vs. Speed**: Waiting for slow parties vs. timeout and retry

**Causal chain**:
```
Heterogeneous nodes + Synchronous protocol → 
Performance bottleneck at slowest node → 
High latency for all operations → 
Poor user experience → Reduced adoption
```

---

### 3. External Connections

**Stakeholders**:
- **Cloud providers**: Offer infrastructure; Could provide MPC-optimized instances
- **Network operators**: Latency and bandwidth affect performance
- **Protocol designers**: Could design latency-tolerant variants
- **Users**: Especially high-frequency traders, DeFi users intolerant of latency

**Environment**:
- **Geographic**: Global deployments face intercontinental latency (100+ ms)
- **Infrastructure**: Cloud vs. on-premise; Enterprise vs. consumer hardware
- **Economic**: Cost of high-performance infrastructure prohibitive for some parties

---

### 4-5. Origins and Trends

**Historical evolution**:
- Early MPC research assumed homogeneous lab environments
- Production deployments revealed heterogeneity challenges
- Some protocols (MPC+) designed specifically to address this

**Trends**:
- Without intervention: Latency remains barrier to real-time use cases (DeFi, high-frequency trading)
- Possible fragmentation: Fast MPC for premium users, slow for everyone else
- Alternative approaches (Threshold BLS, etc.) may gain ground if MPC can't achieve low latency

**Scenarios**:
- **Optimistic (30%)**: Protocol innovations (asynchronous variants, off-chain computation) reduce latency to <100ms p95
- **Baseline (50%)**: Incremental improvements; Latency 200-500ms acceptable for most use cases but not all
- **Pessimistic (20%)**: Heterogeneity proves insurmountable; MPC relegates to non-real-time use cases; Real-time users choose alternatives

---

### 6. Capability Reserves

**Existing strengths**:
- Research on asynchronous MPC protocols
- Cloud infrastructure optimizations (low-latency networking, specialized instances)
- Monitoring tools to identify bottlenecks

**Gaps**:
- **Protocol implementation**: Most production MPC uses synchronous protocols
- **Adaptive selection**: No standard mechanisms for choosing fast-available parties dynamically
- **Benchmarking**: Lack of standardized performance testing across environments

**Buildable capabilities**:
- Performance profiling tools for MPC deployments
- Adaptive party selection algorithms
- Hybrid protocols (synchronous for critical, asynchronous for non-critical)

---

### 7-9. Analysis, Validation, Revision

**Key judgments**:
1. Off-chain computation (MPC+) can reduce latency by 50-70%
2. Dynamic party selection (choose fastest t from n available) practical for non-critical operations
3. Acceptable latency varies by use case: Savings transactions tolerate 1-2s; Trading requires <200ms

**Validation**:
- Benchmark testing across realistic heterogeneous environments
- User acceptance testing: What latency is tolerable for different transaction types?
- Security analysis: Do performance optimizations introduce vulnerabilities?

**"Good enough" criteria**:
- Routine transactions <500ms p95
- High-priority transactions <200ms p95
- No performance-related security compromises

---

### 10. Summary & Action Recommendations

**Core insights**:
1. Heterogeneity is reality of distributed systems—protocol design must embrace, not fight
2. Not all transactions require same latency—risk-adaptive performance strategies make sense
3. Offchain computation (MPC+) represents significant optimization opportunity
4. Monitoring and adaptive behavior critical for maintaining performance in variable conditions

**Near-term actions (0-3 months)**:

**【Critical / P0】**
1. **Performance profiling and bottleneck identification**
   - Owner: Performance Engineering team; Completion: Week 4
   - Metric: Profile top 10 transaction types; Identify bottleneck operations; Quantify node variance impact

2. **MPC+ off-chain computation prototype**
   - Owner: Cryptographic Engineering team; Completion: Week 10
   - Metric: Working prototype for payment channels; Latency reduction ≥50% vs. on-chain; Security audit completed

**【Important / P1】**
3. **Adaptive party selection implementation**
   - Owner: Distributed Systems team; Completion: Week 12
   - Metric: Dynamic selection of fastest t parties for non-critical operations; Latency improvement ≥30%; No security degradation

4. **Performance SLA monitoring**
   - Owner: SRE team; Completion: Week 6
   - Metric: Real-time dashboards for per-party performance; Alerting for degradation; Historical trending

**Risks and responses**:
- **Risk**: Optimization introduces security vulnerabilities
  - **Mitigation**: Comprehensive security review of all performance changes; Formal verification where possible
- **Risk**: Adaptive selection creates availability issues (not enough fast parties)
  - **Mitigation**: Fallback to full party set; Incentivize infrastructure investment by parties


## Problem 6: Interoperability and Chain-Agnostic Design Challenges

### Context Recap

**Problem Title**: Multi-Chain Interoperability Challenges in MPC-TSS Wallets

**Key Context**:
- Need for wallets to manage multi-chain assets through unified interface across diverse blockchain architectures
- Current: Fragmentation hinders adoption and integration with DeFi applications
- Goal: Support ≥3 major blockchain protocols/operating systems; reduce integration complexity by 30%; enhance cross-chain efficiency by 20% within 12-18 months
- Constraints: Variability in blockchain cryptography, performance requirements, lack of universal standards
- Impact: Medium-term (6-18 months), broad global user base across multiple ecosystems

---

### 1. Problem Definition

**Core contradiction**: Users want single wallet for all assets, but blockchains use incompatible signature schemes and transaction formats, while MPC protocols are typically optimized for specific cryptographic primitives.

**Conflicting requirements**:
- **User expectation**: One wallet, all chains ("MetaMask for everything")
- **Technical reality**: ECDSA (Ethereum), EdDSA (Solana), Schnorr (Bitcoin Taproot) all different
- **Security requirement**: Cannot compromise protocol security for compatibility
- **Performance requirement**: Cannot have dramatically different latencies per chain

**Reframing**:
- From "universal MPC protocol" to "modular cryptographic backend" (plug different signature schemes)
- From "support all chains" to "support chain families" (EVM-compatible, Cosmos ecosystem, etc.)
- From "wallet manages keys" to "wallet manages identities" (one identity, multiple key types)

---

### 2. Internal Logical Relations

**Key elements**:
- Multi-signature threshold schemes (ECDSA-TSS, EdDSA-TSS, Schnorr-TSS)
- Blockchain adapters (transaction construction, broadcast, confirmation)
- Key derivation paths (HD wallet standards across chains)
- Cross-chain communication protocols

**Balance points**:
- **Generality vs. Optimization**: Universal protocol slower; Chain-specific faster but more complex
- **Flexibility vs. Maintenance burden**: Supporting many chains increases testing and update overhead
- **Abstraction vs. Transparency**: Hide complexity from users; But power users want chain-specific control

**Causal chain**:
```
Blockchain diversity + MPC specialization → 
Need for multiple protocol implementations → 
Integration complexity + maintenance burden → 
Delayed multi-chain support → Poor user experience
```

---

### 3. External Connections

**Stakeholders**:
- **Blockchain foundations**: Define protocols; Some collaborate (IBC), others compete
- **DeFi protocols**: Require wallet integration; Pressure for fast support of new chains
- **Bridge protocols**: Enable cross-chain assets; Potential partners
- **Users**: Want simplicity; Don't care about technical barriers

**Environment**:
- **Fragmentation**: 100+ blockchains with varying adoption
- **Evolution**: New chains launch constantly; Existing chains upgrade cryptography
- **Standards efforts**: W3C DID, Chain Agnostic Improvement Proposals (CAIPs)

**Responsibility**: Wallet providers must not force users to understand blockchain differences

---

### 4-5. Origins and Trends

**Evolution**:
- **2009-2017**: Bitcoin only, then Ethereum—relatively simple two-chain world
- **2017-2020**: ICO boom created token diversity but mostly ERC-20 (one chain)
- **2020-2023**: L1 proliferation (Solana, Avalanche, Cosmos, etc.)—real multi-chain challenges
- **2023-present**: L2 explosion (Optimism, Arbitrum, zkSync, etc.)—complexity squared

**Current trajectory**:
- Without solutions: Users maintain multiple wallets (poor UX); Wallets support limited chains (market fragmentation)
- Market pressure for "super apps" that support everything
- Possible consolidation around 3-5 dominant chains

**Signals**:
- User requests for new chain support consistently top feature requests
- Dev time spent on "add chain X support" growing
- Cross-chain DeFi protocols (RenVM, THORChain) show demand

---

### 6. Capability Reserves

**Existing strengths**:
- Threshold signature schemes exist for major signature types (ECDSA, EdDSA, Schnorr)
- Chain-agnostic standards emerging (CAIPs, WalletConnect)
- RenVM demonstrates MPC for cross-chain asset locking

**Gaps**:
- **Protocol maturity**: Some TSS variants less battle-tested
- **Tooling**: No comprehensive multi-chain MPC SDK
- **Testing**: Validating correctness across chains manually intensive

**Buildable capabilities (1-6 months)**:
- Modular cryptographic backend architecture
- Automated chain integration testing suite
- Chain abstraction layer API
- Plugin system for new chains

---

### 7-9. Analysis, Validation, Revision

**Key judgments**:
1. Can abstract common patterns (EVM-compatible chains share ~90% of logic)
2. Modular architecture allows independent development of chain-specific modules
3. Users tolerate some delay for less-popular chains (prioritize top 10 by TVL)

**Validation**:
- Survey: Which chains do users actually use? (Prioritization data)
- Architecture review: Can modular design work without performance penalties?
- Developer testing: Can external contributors add chains with plugin system?

**"Good enough" criteria**:
- Top 5 chains by user demand supported within 3 months of request
- New EVM chain support added in <2 weeks
- Non-EVM chains in <6 weeks
- No security compromises from multi-chain support

---

### 10. Summary & Action Recommendations

**Core insights**:
1. Interoperability is product imperative, not technical luxury—users demand it
2. Abstraction layers are key—commonalities across chains (EVM family, Cosmos ecosystem) enable leverage
3. Prioritization essential—cannot support everything; Focus on 80% of user value
4. Modular architecture enables parallelization—teams can work on different chains independently

**Near-term actions (0-3 months)**:

**【Critical / P0】**
1. **Chain prioritization analysis**
   - Owner: Product + Analytics teams; Completion: Week 3
   - Metric: Ranked list of chains by user demand, TVL, strategic importance; Top 10 identified

2. **Modular architecture redesign**
   - Owner: Architect + Senior Engineering; Completion: Week 12
   - Metric: Abstraction layer separating MPC core from chain-specific logic; POC with 2 chains demonstrating modularity

**【Important / P1】**
3. **EVM chain family support**
   - Owner: Blockchain Engineering team; Completion: Week 10
   - Metric: Support Ethereum, BSC, Polygon, Arbitrum, Optimism with shared codebase (>80% code reuse)

4. **Chain integration testing framework**
   - Owner: QA Engineering; Completion: Week 8
   - Metric: Automated test suite for transaction construction, signing, broadcast; Reduces manual testing time by >60%

**Risks and responses**:
- **Risk**: Modular architecture introduces performance overhead
  - **Mitigation**: Benchmark early; Ensure abstraction cost <5%; Optimize hot paths
- **Risk**: Subtle differences between "similar" chains cause bugs
  - **Mitigation**: Comprehensive test coverage; Chain-specific validation; Bug bounties
- **Risk**: Resource fragmentation across too many chains
  - **Mitigation**: Strict prioritization discipline; Partnerships for lower-priority chains

---

## Problem 7: Cost Structure and Economic Implications

### Context Recap

**Problem Title**: Infrastructure and Operational Costs of Blockchain MPC Wallets at Scale

**Key Context**:
- MPC requires complex synchronous communication and computation across multiple parties, incurring substantial costs
- Current: Major wallet providers face significant financial overhead from node coordination, cryptographic operations, network demands
- Goal: Reduce node operation costs, transaction fees, system overhead by 20-30% within 12-18 months without compromising security
- Constraints: Inherent MPC complexity, heterogeneous nodes, blockchain network fees, security requirements
- Impact: Medium-term (6-18 months), global scale (hundreds of billions USD in cryptocurrency)

---

### 1. Problem Definition

**Core contradiction**: MPC's security benefits come from distribution and coordination, but those same properties drive costs that threaten economic viability at scale.

**Cost drivers**:
- **Infrastructure**: N parties need N sets of infrastructure (compute, storage, network)
- **Computation**: Cryptographic operations (signature generation) computationally expensive
- **Communication**: Multiple rounds of message exchange for each operation
- **Blockchain fees**: On-chain operations (when required) incur gas/transaction fees
- **Personnel**: 24/7 operations, security monitoring, incident response

**Conflicting goals**:
- **Users**: Want low/no fees
- **Providers**: Need sustainable business model
- **Security**: Requires redundancy and monitoring (costs money)
- **Investors**: Demand profitability

**Reframing**:
- From "reduce costs" to "optimize cost-benefit ratio" (some costs essential for value delivered)
- From "MPC is expensive" to "compared to what?" (vs. security breaches, insurance, custody alternatives)
- From "fixed architecture" to "tiered offerings" (different cost points for different security/performance levels)

---

### 2. Internal Logical Relations

**Key cost components**:
1. **Infrastructure**: Cloud compute ($X per node per month), Storage, Network bandwidth
2. **Operations**: Personnel (DevOps, SRE, security), Monitoring tools, Incident response
3. **Blockchain fees**: Gas for on-chain operations
4. **Development**: Building, maintaining, updating MPC systems
5. **Security**: Audits, bug bounties, insurance

**Balance points**:
- **Redundancy vs. Cost**: More parties = more secure but more expensive
- **Performance vs. Cost**: Faster infrastructure costs more
- **Automation vs. Personnel**: Upfront investment in automation reduces ongoing labor costs

**Causal chain**:
```
Multi-party architecture → Infrastructure multiplication → 
Complex coordination → Operational overhead → 
High costs → Must charge users OR subsidize → 
Pricing pressure OR unsustainable burn rate
```

---

### 3. External Connections

**Stakeholders**:
- **Cloud providers**: Pricing determines infrastructure costs; Could offer MPC-optimized pricing
- **Blockchain networks**: Gas fee structures affect costs; L2s and off-chain solutions reduce fees
- **Investors**: Expect path to profitability
- **Users**: Will pay for security but have price sensitivity
- **Competing solutions**: Custodial (lower cost), Hardware wallets (one-time cost)

**Environment**:
- **Market**: Cryptocurrency bear/bull cycles affect user willingness to pay
- **Technology**: Hardware improvements (faster CPUs, better networking) reduce costs over time
- **Competition**: Race to offer best price-performance

---

### 4-5. Origins and Trends

**Historical costs**:
- Early MPC deployments: Artisanal, very expensive (manual operations)
- 2020-2022: Scaling attempts reveal cost structures; Some providers subsidize with VC funding
- 2023-present: Focus on cost optimization as funding dries up; MPC+ and similar innovations specifically target costs

**Trends**:
- Without optimization: Costs per transaction remain 10-100x higher than single-key wallets; Sustainable only for high-value use cases
- Possible VC subsidy cliff: As funding environment tightens, unsustainable cost structures revealed
- Technology improvements: Off-chain computation, protocol optimizations can reduce costs substantially

**Scenarios**:
- **Optimistic (25%)**: Protocol optimizations + infrastructure efficiencies → 50-70% cost reduction; MPC economically viable for mainstream
- **Baseline (50%)**: Incremental improvements → 20-30% cost reduction; MPC remains premium offering
- **Pessimistic (25%)**: Costs remain prohibitive; Market segments into premium MPC vs. cheap custodial; Volume stays with custodial

---

### 6. Capability Reserves

**Existing strengths**:
- Research on cost-optimized protocols (MPC+, off-chain payment channels)
- Cloud cost optimization techniques well-established
- Automation tools for operations exist

**Gaps**:
- **Cost transparency**: Many providers don't publish detailed cost breakdowns
- **Benchmarking**: Difficult to compare costs across providers/implementations
- **Optimization culture**: May prioritize features over efficiency

**Buildable capabilities**:
- Detailed cost accounting and monitoring
- Protocol profiling to identify expensive operations
- Automated scaling (scale down during low-usage periods)
- Infrastructure right-sizing (match resources to needs)

---

### 7-9. Analysis, Validation, Revision

**Key judgments**:
1. Infrastructure costs are largest component (60-70% of total costs)
2. Off-chain computation (MPC+) can reduce blockchain fees by 80-90%
3. Automation can reduce operational personnel costs by 40-50%
4. Users will pay premium for security but price elasticity exists (diminishing returns above certain threshold)

**Validation**:
- Detailed cost accounting of current operations (baseline)
- Benchmark alternative architectures (MPC+, different party counts)
- User willingness-to-pay research
- Competitor cost analysis

**"Good enough" criteria**:
- Cost per transaction <$0.50 for high-volume users
- Overall costs enable profitability at >100k MAU
- Cost structure competitive with alternative custody solutions when including security benefits

---

### 10. Summary & Action Recommendations

**Core insights**:
1. Cost structure is existential issue for MPC wallet viability at scale—must address to achieve mass adoption
2. Infrastructure multiplication is inherent to MPC but can be optimized (right-sizing, cloud efficiencies)
3. Off-chain computation represents major opportunity (80-90% blockchain fee reduction)
4. Automation is high-leverage: Upfront investment pays long-term dividends
5. Tiered offerings allow both cost optimization and premium services

**Near-term actions (0-3 months)**:

**【Critical / P0】**
1. **Comprehensive cost accounting and profiling**
   - Owner: Finance + Engineering; Completion: Week 4
   - Metric: Detailed breakdown of costs by category; Per-transaction cost; Identification of top 3 cost drivers

2. **MPC+ implementation for high-volume use cases**
   - Owner: Protocol Engineering team; Completion: Week 12
   - Metric: Off-chain payment channel operational; 80% reduction in blockchain fees for qualifying transactions

**【Important / P1】**
3. **Infrastructure optimization**
   - Owner: Infrastructure/SRE team; Completion: Week 10
   - Metric: Right-size instances (eliminate over-provisioning); Auto-scaling implementation; Target 25% infrastructure cost reduction

4. **Operational automation**
   - Owner: DevOps team; Completion: Ongoing, review at Week 8
   - Metric: Automated routine operations reducing manual intervention by 40%; Document cost savings from reduced labor

**【Important / P1】**
5. **Tiered pricing model design**
   - Owner: Product + Finance; Completion: Week 6
   - Metric: Defined tiers (retail, professional, institutional) with appropriate cost structures and feature sets

**Risks and responses**:
- **Risk**: Cost reductions compromise security or reliability
  - **Mitigation**: Security audit of all cost optimization changes; SLA monitoring during rollout; Rollback plan
- **Risk**: Users unwilling to pay sustainable prices
  - **Mitigation**: Value-based pricing communication; Bundle with other services; Enterprise contracts with committed volumes
- **Risk**: Competitors undercut on price through VC subsidy
  - **Mitigation**: Differentiate on security, reliability, features; Long-term sustainability message to enterprises

---

## Problem 8: User Experience Complexity Limiting Mass Adoption

### Context Recap

**Problem Title**: UX Complexity as Barrier to Mainstream MPC Wallet Adoption

**Key Context**:
- Intricate cryptographic concepts, multi-device coordination, difficult recovery create adoption barriers
- Current: Users struggle with abstract concepts (key shares), managing devices, navigating recovery—leads to errors and reluctance
- Goal: Increase adoption by ≥20%, reduce user errors by 30% within 1 year, without compromising security
- Constraints: Need to maintain cryptographic security, diverse user technical skills, regulatory compliance steps
- Impact: Medium-term (1 year), global (millions of potential users), critical for ecosystem growth

---

### 1. Problem Definition

**Core contradiction**: MPC's distributed security model is conceptually complex (key shares, thresholds, multi-party signatures), while mass adoption requires simplicity ("it just works").

**User challenges**:
- **Onboarding**: Setting up multiple devices/parties, understanding key share distribution
- **Daily use**: Multi-device approval for transactions (where are my devices? which ones?)
- **Recovery**: If device lost, coordinating recovery across remaining parties/shares
- **Mental model**: Users think "password" or "key"; MPC doesn't fit familiar patterns

**Conflicting requirements**:
- **Cryptography**: Inherently complex; Requires multiple parties/devices for security
- **User expectation**: Should be as simple as password login or Face ID
- **Security**: Cannot over-simplify to point of compromising protections
- **Education**: Users don't read documentation; Want zero learning curve

**Reframing**:
- From "educate users about MPC" to "hide MPC complexity entirely" (abstraction)
- From "multi-device approval" to "intelligent device orchestration" (auto-select best available devices)
- From "user manages key shares" to "system manages shares transparently"

---

### 2. Internal Logical Relations

**UX components**:
- Onboarding flow (account creation, device enrollment, backup setup)
- Transaction initiation and approval
- Recovery initiation and completion
- Settings and management (add/remove devices, adjust security)

**Balance points**:
- **Security visibility vs. Simplicity**: Show what's happening (transparency) vs. Hide complexity (simplicity)
- **Control vs. Automation**: Let users decide vs. Intelligent defaults
- **Education vs. Frustration**: Explain features vs. Don't interrupt flow

**Failure modes**:
```
Complex UX → User confusion → 
Errors or abandonment → 
Either: Security incident (if user bypasses security) OR Locked out (if user stuck)
```

---

### 3. External Connections

**Stakeholders**:
- **UX design community**: Best practices for security UX, onboarding, error prevention
- **Customer support**: Bears the cost of confused users (support tickets, hand-holding)
- **Competing wallets**: Set user expectations (MetaMask, Coinbase, Ledger)
- **App stores**: Review guidelines may require certain UX patterns

**Environment**:
- **Cultural**: Different user populations have different tech-savviness and mental models
- **Device ecosystem**: iOS vs. Android, Desktop vs. Mobile—need consistency
- **Accessibility**: Must work for users with disabilities

**Responsibility**: Cannot blame users for complexity—provider's job to make it work

---

### 4-5. Origins and Trends

**Evolution**:
- **2009-2015**: Bitcoin CLI wallets—only for experts
- **2015-2017**: Mobile wallets (Breadwallet, etc.)—much simpler but still "techy"
- **2017-2020**: Coinbase/custodial—"finally, normal UX" but not self-custody
- **2020-present**: MPC wallets trying to combine self-custody + simple UX—struggling

**Trends without intervention**:
- MPC remains "for advanced users"
- Mainstream sticks with custodial despite security risks
- UX-first competitors (smart contract wallets like Argent, ZenGo) may win by different approaches

**Signals**:
- High onboarding abandonment (60-70% don't complete setup)
- Support tickets dominated by "how do I...?" questions
- App store reviews: "Too complicated"

---

### 6. Capability Reserves

**Existing strengths**:
- Biometric authentication now ubiquitous (leverage for approvals)
- Progressive web apps enable cross-device experiences
- Social recovery patterns (Argent) prove alternative models work

**Gaps**:
- **MPC-specific UX patterns**: No established best practices; Each provider experimenting
- **User research**: Limited testing with truly non-technical users (sampling bias toward crypto-natives)
- **Accessibility**: Little focus on users with disabilities

**Buildable capabilities**:
- Comprehensive UX testing with representative users
- Device orchestration intelligence (auto-select best devices for approval)
- Progressive onboarding (functionality unlocked gradually)
- Contextual help (in-app assistance at friction points)

---

### 7-9. Analysis, Validation, Revision

**Key judgments**:
1. Biometric-first flows can eliminate most explicit "MPC thinking" for users
2. Device orchestration can hide "which device?" decisions from users
3. Social recovery more intuitive than cryptographic recovery for mainstream
4. Progressive onboarding (start simple, add features) better than all-at-once

**Validation**:
- Usability testing with non-crypto users (target: >80% complete onboarding without assistance)
- Measure time-to-first-transaction (target: <5 minutes)
- Track support ticket volume (target: 50% reduction)
- A/B test UX variants

**"Good enough" criteria**:
- Onboarding completion >80%
- First transaction <5 minutes from account creation
- Support ticket rate <1% of MAU
- App store rating >4.0/5.0 with positive UX feedback

---

### 10. Summary & Action Recommendations

**Core insights**:
1. Complexity is #1 adoption barrier—more important than features or even security for mainstream
2. "Abstraction over education"—Hide complexity rather than teaching users about MPC
3. Biometrics are game-changer—Leverage extensively for familiar, simple interactions
4. Can't design for "yourself"—Must test with target users (non-technical, non-crypto-native)
5. Progressive disclosure: Start dead simple, unlock advanced features for power users

**Near-term actions (0-3 months)**:

**【Critical / P0】**
1. **User research with mainstream (non-crypto) users**
   - Owner: UX Research team; Completion: Week 4
   - Metric: ≥50 user testing sessions with non-crypto users; Video-recorded friction points; Prioritized fix list

2. **Biometric-first onboarding redesign**
   - Owner: Mobile Product + Engineering; Completion: Week 10
   - Metric: Onboarding completion rate increases from current 40% to >75%; Time-to-first-transaction <5 min

**【Critical / P0】**
3. **Device orchestration (automatic best-device selection)**
   - Owner: Engineering team; Completion: Week 12
   - Metric: Users never manually choose "which device"; System intelligently selects; User survey shows >80% find it "simple"

**【Important / P1】**
4. **Progressive onboarding implementation**
   - Owner: Product team; Completion: Week 8
   - Metric: Basic account created in <2 min; Advanced features (multiple devices, custom security) optional later

5. **In-app contextual help system**
   - Owner: Product + Support teams; Completion: Week 8
   - Metric: Help triggered at key friction points; Support ticket reduction >30%; User satisfaction with help >4.0/5.0

**Risks and responses**:
- **Risk**: Simplification hides security implications users should know
  - **Mitigation**: "Security summary" available but not forced; Transparent about what system is doing (in advanced settings)
- **Risk**: Optimizing for novices annoys power users
  - **Mitigation**: Advanced mode with full control; Make simple mode default but not only mode
- **Risk**: Biometric failures (Face ID doesn't work) create bad experience
  - **Mitigation**: Fallback mechanisms; Clear error messages; Alternative authentication paths


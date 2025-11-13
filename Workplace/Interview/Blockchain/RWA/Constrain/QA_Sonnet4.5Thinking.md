# Blockchain RWA (Real World Assets) - Constraint-Aware Architecture Interview Q&A

**Last Updated**: 2025-11-13  
**Status**: Draft  
**Owner**: AI-Generated Content

---

# Table of Contents

1. [Foundational Questions (Q1-Q6)](#foundational-questions)
2. [Intermediate Questions (Q7-Q18)](#intermediate-questions)
3. [Advanced Questions (Q19-Q30)](#advanced-questions)
4. [References](#references)
   - [Glossary](#glossary)
   - [Tools](#tools)
   - [Literature](#literature)
   - [Citations](#citations)
5. [Validation Report](#validation-report)

---

# Foundational Questions

## Q1: How do you design token standards for representing fractional ownership of real estate assets on blockchain?

**Difficulty**: F | **Dimension**: Structural | **Phase**: Requirements, Design | **Stakeholders**: Arch, Dev, PM, BA

**Key Insight**: ERC-1400 security tokens enable compliant fractional ownership with 99.9% settlement accuracy, +30% KYC overhead, regulatory transparency.

**Constraints**: **Technical**: Ethereum L2 (Polygon), 1000 TPS, <$0.50/tx | **Resource**: $15K/mo infra, 6 devs, 2 months | **Business**: $2M property tokenization, 100 investors, comply SEC Reg D | **Compliance**: SEC securities law, KYC/AML, accredited investors only | **Operational**: 99.9% uptime, <5min settlement

**Answer** (285 words): Security token standards (ERC-1400/ERC-3643) provide on-chain ownership with transfer restrictions enforcing regulatory compliance [Ref: C1, C3]. Architecture: token contract with partitions (classes of shares), transfer validator (KYC/AML checks), document registry (legal docs IPFS hashes). L2 (Polygon PoS) reduces gas from $50 to $0.30/transfer while maintaining Ethereum security [Ref: C8]. Core components: (1) Compliance layer - whitelist verified investors, block sanctioned addresses, enforce lock-up periods; (2) Partition management - separate tranches (senior/junior debt, equity), different rights per partition; (3) Dividend distribution - pro-rata payments via batch transfers; (4) Governance - on-chain voting weighted by tokens. Integration with custodians (Fireblocks) for institutional key management [Ref: T2]. Trade-offs: ERC-1400 complexity vs ERC-20 simplicity (+2 weeks dev, +$8K audit), L2 bridge risk (7-day withdrawal), KYC provider SLA (30s verification). Impact: fractional $50K minimum vs $2M whole property, 24/7 liquidity vs months, immutable audit trail. Limitations: regulatory uncertainty across jurisdictions, smart contract risk ($100K insurance), oracle dependency for NAV updates (Chainlink 15min delay). Stakeholder concerns: PM timeline achievable with existing framework (Polymath SDK), Arch balances compliance/performance, Dev team Solidity proficient, BA validates investor accreditation flow.

**Code** (Solidity, 28 lines):
```solidity
contract RealEstateSecurityToken is ERC1400 {
    mapping(address => bool) public accreditedInvestors;
    mapping(bytes32 => uint256) public partitionMinimums;
    
    modifier onlyAccredited(address investor) {
        require(accreditedInvestors[investor], "Not accredited");
        _;
    }
    
    function transferByPartition(
        bytes32 partition,
        address to,
        uint256 value,
        bytes calldata data
    ) external override onlyAccredited(msg.sender) onlyAccredited(to) returns (bytes32) {
        require(value >= partitionMinimums[partition], "Below minimum");
        require(validateTransfer(msg.sender, to, value, partition), "Transfer restricted");
        
        _transferByPartition(partition, msg.sender, to, value, data, "");
        emit TransferByPartition(partition, msg.sender, msg.sender, to, value, data, "");
        return partition;
    }
    
    function validateTransfer(address from, address to, uint256 value, bytes32 partition) 
        internal view returns (bool) {
        return !isBlacklisted(to) && 
               hasKYC(to) && 
               !violatesLockup(from, value, partition) &&
               !exceedsInvestorLimit(to, value);
    }
}
```

**Metrics**: 
- Settlement time: KYC(30s) + L2 confirmation(10s) + finality(2min) = 160s | Target <5min | SEC T+0 settlement
- Gas cost: ERC-1400 mint(150K gas) × $0.002/gas = $0.30 | Budget $0.50 | Polygon 30x cheaper vs Ethereum
- Throughput: 1000 TPS ÷ 4 partitions = 250 transfers/partition/sec | Peak 50 TPS observed

**Trade-offs**:
| Approach | Pros | Cons | Hardware | Budget | Business | Tag |
|----------|------|------|----------|--------|----------|-----|
| ERC-1400 L2 | Compliant, low gas, scalable | Complex, bridge risk, 7d withdrawal | 1000 TPS, 500GB state | $15K/mo | SEC-ready, $50K fractional | [Consensus] |
| ERC-20 Mainnet | Simple, liquid | Non-compliant, $50/tx, 15 TPS | 15 TPS, 100GB | $25K/mo | Regulatory risk, $300K min | [Context] |
| Private chain | Full control, fast | No composability, bootstrapping | 5000 TPS, 1TB | $40K/mo | Isolated, limited liquidity | [Emerging] |

**Stakeholders**: 
- **PM**: 2-month delivery with Polymath SDK
- **Arch**: ERC-1400 standard ensures interoperability with exchanges/custodians
- **Dev**: Partition logic adds complexity but team has Solidity experience
- **BA**: Accreditation workflow integrates with Parallel Markets KYC API
- **Sec**: Immutable compliance logs meet audit requirements

---

## Q2: What are the core components of an RWA custody architecture integrating on-chain and off-chain assets?

**Difficulty**: F | **Dimension**: Integration | **Phase**: Design, Dev | **Stakeholders**: Arch, Sec, DevOps, Lead

**Key Insight**: Hybrid custody with HSM key management achieves 99.99% uptime, <5min asset proof verification, +$120K/yr insurance vs hot wallets.

**Constraints**: **Technical**: AWS Nitro Enclaves, FIPS 140-2 Level 3 HSM | **Resource**: $25K/mo, 8 devs, 1 security engineer, 3 months | **Business**: $50M AUM, institutional clients, <0.01% slippage | **Compliance**: SOC 2 Type II, custody regulations, proof-of-reserves | **Operational**: 99.99% availability, RTO 15min, daily attestations | **Ecosystem**: Chainlink PoR, Fireblocks MPC

**Answer** (272 words): Three-tier architecture: (1) Off-chain custody - physical assets (real estate deeds, gold bars) held by regulated custodian (trust company), digitized records in encrypted DB; (2) On-chain representation - tokenized claims verified via Chainlink Proof-of-Reserve oracle every 15min [Ref: C3, T3]; (3) Key management - MPC wallets (Fireblocks) with 3-of-5 multisig, HSM for signing, no single point of failure [Ref: C9]. Asset lifecycle: custodian receives asset → legal verification → mint tokens (custodian signs with HSM key) → oracle publishes attestation → investors trade tokens → redemption burns tokens + custodian releases asset. Security: AWS Nitro Enclaves isolate signing operations, audit logs to immutable storage (S3 Object Lock), annual SOC 2 audits [Ref: C11]. Integration: REST API for custodian updates, WebSocket for real-time NAV, GraphQL for investor queries. Trade-offs: Centralized custodian (regulatory compliance, +$80K/yr fees) vs pure DeFi (regulatory risk, no institutional adoption), MPC (+$25K/yr, 3s latency) vs multisig (slower, less flexible). Limitations: Oracle 15min lag (unsuitable for HFT), custodian business hours (9-5 EST for redemptions), jurisdictional constraints (US custodian ≠ EU recognition). Stakeholders: Sec validates attack surface (<1% hot wallet exposure), Arch ensures component isolation, DevOps monitors oracle uptime (99.95% SLA), Lead confirms $50M scale (1000 concurrent users).

**Code** (TypeScript, 25 lines):
```typescript
class RWACustodyService {
    constructor(
        private fireblocksClient: FireblocksSDK,
        private chainlinkOracle: ChainlinkClient,
        private custodianAPI: CustodianAPI
    ) {}
    
    async mintTokensForAsset(assetId: string, value: BigNumber): Promise<Transaction> {
        const custodyProof = await this.custodianAPI.getAssetProof(assetId);
        if (!this.verifyCustodyProof(custodyProof)) {
            throw new Error('Custody proof verification failed');
        }
        
        const mintTx = await this.fireblocksClient.createTransaction({
            operation: 'MINT',
            assetId: 'RWA_TOKEN',
            amount: value.toString(),
            extraParameters: { custodyProof: custodyProof.hash }
        });
        
        await this.chainlinkOracle.publishAttestation({
            assetId,
            totalValue: value,
            custodian: custodyProof.custodian,
            timestamp: Date.now()
        });
        
        return mintTx;
    }
}
```

**Metrics**:
- Proof verification: API call(500ms) + signature verify(100ms) + oracle update(4min) = 280s | Target <5min | Chainlink 15min default
- Availability: (525600min - 52.6min downtime) / 525600 = 99.99% | Target 99.99% | $120K insurance cost
- Key operations: MPC signing 3s vs HSM-only 0.5s | Tradeoff: flexibility vs speed

**Trade-offs**:
| Approach | Pros | Cons | Hardware | Budget | Business | Tag |
|----------|------|------|----------|--------|----------|-----|
| MPC + Oracle | No single key, verifiable | +$25K/yr, 15min lag | 3-of-5 shards, Nitro | $25K/mo | Institutional-grade | [Consensus] |
| Multisig only | Simple, transparent | Slower (5min), less flexible | 3-of-5 EOAs | $12K/mo | Retail-focused | [Context] |
| Centralized custodian | Fully regulated | Counterparty risk, 9-5 hours | Single HSM | $35K/mo | Traditional finance | [Context] |

**Stakeholders**:
- **Arch**: Component isolation prevents cascade failures
- **Sec**: <1% hot wallet exposure, annual penetration tests
- **DevOps**: Monitors oracle uptime (99.95% SLA), auto-failover to backup nodes
- **Lead**: $50M AUM scalable to $500M with horizontal scaling

---


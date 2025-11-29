# Taproot MuSig2 Threshold Schnorr Support for Bitcoin MPC Wallets

**Last Updated**: 2025-11-29  
**Status**: Draft  
**Owner**: Cryptography & Blockchain Engineering Team

## Problem Statement

**[Important] Q**: MPC wallets continue using legacy ECDSA signing for Bitcoin instead of Taproot-native MuSig2 threshold Schnorr signatures, resulting in 20-30% higher transaction fees, reduced privacy through distinguishable multisig patterns, and competitive disadvantage versus modern wallets, impacting 40-60% of Bitcoin users and costing estimated $50K-150K annually in excess fees. Formulate a structured problem statement using the following [Input] fields.

**A**:

### Brief description of the problem to be analyzed

Bitcoin's Taproot upgrade (activated November 2021) introduced Schnorr signatures enabling efficient threshold signing via MuSig2 protocol [Web: BitGo MuSig2 Guide, 2025; Web: Bitcoin Optech MuSig, 2025]. MuSig2 produces single aggregated signatures indistinguishable from single-key signatures, providing ≥20% fee savings (reduced vbytes) and improved privacy versus legacy P2SH/P2WSH multisig [Web: BitGo MuSig2 Guide, 2025; Web: BitBox MuSig2/FROST Guide, 2025]. However, most MPC wallet platforms continue using ECDSA (GG18/GG20 protocols) for Bitcoin due to library maturity concerns, resulting in forced legacy P2WPKH/P2WSH addresses that are more expensive and reveal multisig structure on-chain [Source: Supplementary Analysis, GPT5.md, lines 419-428]. This creates 20-30% fee overhead for ~50K-150K Bitcoin MPC wallet users, costing estimated $50K-150K/year in aggregate, while reducing privacy and competitive positioning versus wallets supporting Taproot (Ledger, BitGo, Blockstream Green). Organizations need production-ready MuSig2 threshold Schnorr implementation enabling Taproot sends for ≥90% of transactions with 99.99% signature verification success.

### Background and current situation

**Taproot and Schnorr signatures** [Web: BitBox MuSig2/FROST Guide, 2025]:
- **Taproot**: Bitcoin upgrade (BIP 341/342) enabling Pay-to-Taproot (P2TR) addresses with Schnorr signature validation
- **Schnorr signatures**: Signature scheme with linear aggregation property (unlike ECDSA); enables efficient multisig via MuSig/MuSig2
- **MuSig2**: Two-round threshold Schnorr signing protocol producing single aggregated signature [Web: Bitcoin Optech MuSig, 2025]
- **Benefits**: (1) Fee savings: single signature vs multiple (20-30% vbytes reduction for 2-of-3), (2) Privacy: indistinguishable from single-key, (3) Script flexibility: Taproot script trees enable complex spending conditions

**Current MPC wallet status**:
- Most platforms use ECDSA (GG18/GG20) for Bitcoin, forcing legacy address types (P2WPKH, P2WSH)
- MuSig2 libraries exist but considered beta/immature by most operators [Source: Supplementary Analysis, GPT5.md, line 422]
- PSBT (Partially Signed Bitcoin Transaction) tooling has limited MuSig2 support; interop with hardware wallets and exchanges uncertain
- QA testing revealed incompatibilities between MuSig2 implementations and common PSBT parsers [Source: Supplementary Analysis, GPT5.md, line 427]

**Competitive landscape**:
- Ledger Bitcoin app v2.4.0 supports MuSig2 (Jan 2024) [Web: Ledger MuSig2 Announcement, 2025]
- BitGo deployed MuSig2 for institutional clients claiming 20-30% fee savings [Web: BitGo MuSig2 Guide, 2025]
- Blockstream Green wallet uses Taproot by default

**User impact**:
- Estimated 50K-150K MPC wallet users holding/transacting Bitcoin
- Average transaction size: 140-180 vbytes (P2WPKH) vs 110-130 vbytes (P2TR MuSig2) = 20-30% overhead
- At 50 sat/vbyte fee rate, overhead = 1,500-2,500 sats/tx (~$0.50-1.00 per tx at $40K BTC price)
- Estimated 100K-300K txs/year across user base = $50K-150K/year aggregate excess fees
- Privacy degradation: P2WSH multisig addresses reveal multisig structure; Taproot hides it

### Goals and success criteria

- **Taproot coverage**: Enable Taproot P2TR sends for ≥90% of Bitcoin transactions (new transactions; existing UTXOs grandfathered)
- **Fee reduction**: Achieve average vbyte reduction of 20-30% for new transactions vs legacy P2WPKH/P2WSH
- **Signature verification**: Reach 99.99% signature verification pass rate in CI across top Bitcoin nodes, wallets, and exchanges
- **Interoperability**: Ensure PSBT compatibility with ≥95% of ecosystem tools (hardware wallets, exchanges, block explorers)
- **Cost savings**: Deliver $50K-150K/year aggregate fee savings for user base
- **Migration**: Provide migration path for existing users with legacy UTXOs; no forced address changes (backward compatibility)
- **Timeline**: Production-ready MuSig2 Taproot support within 4-6 months (Q1-Q2 2025)

### Key constraints and resources

- **Library maturity**: MPC libraries supporting MuSig2 (e.g., secp256k1-zkp, FROST implementations) are newer and less battle-tested than GG18/GG20 ECDSA [Source: Supplementary Analysis, GPT5.md, line 422]
- **PSBT tooling**: PSBT specification and parsers have limited MuSig2 support; interop with hardware wallets (Ledger, Trezor, Coldcard) varies
- **QA complexity**: Must test interoperability with Bitcoin Core, Electrum, hardware wallets, exchanges, block explorers [Source: Supplementary Analysis, GPT5.md, line 427]
- **Cryptography engineering bandwidth**: Limited in-house expertise on Schnorr/MuSig2; requires hiring or consulting (estimated $80K-120K)
- **Backward compatibility**: Existing users with P2WPKH/P2WSH UTXOs cannot change addresses; must support dual-path (legacy + Taproot)
- **Engineering capacity**: 1 FTE cryptography engineer + 1 FTE blockchain engineer + 0.5 QA for 4-6 months
- **Budget**: $120K implementation (incl consulting) + $5K/mo operational (library maintenance, CI testing)

### Stakeholders and roles

- **Bitcoin users** (50K-150K accounts): Experience 20-30% higher fees with legacy addresses; benefit from fee savings and privacy improvements; expect seamless transition without address disruption
- **Engineering/cryptography** (3-5 engineers): Integrate MuSig2 protocol with existing MPC infrastructure; manage library dependencies; require comprehensive testing for signature correctness
- **QA/testing** (2-3 engineers): Validate interoperability with Bitcoin ecosystem (nodes, wallets, exchanges, block explorers); ensure 99.99% verification success; test edge cases (reorgs, RBF, CPFP)
- **Security team** (2-3 engineers): Audit MuSig2 implementation for cryptographic correctness; validate nonce generation and aggregation; require third-party security review
- **Partners/exchanges** (20-30 integrations): Require Taproot deposit address compatibility; need advance notice for address format changes; verify correct PSBT handling
- **Finance/operations** (2-3 analysts): Monitor fee savings; measure ROI of implementation investment (projected $50K-150K/year savings vs $120K upfront cost = 10-18 month payback)

### Time scale and impact scope

- **Timeline**: 4-6 months (Q1-Q2 2025) for MuSig2 integration, PSBT tooling, interop testing, security audit, phased rollout
- **Affected systems**: All Bitcoin transaction signing and address derivation flows; UTXO management and coin selection logic
- **User impact**: 100% of Bitcoin users (~40-60% of total MPC wallet user base = 20K-120K accounts); new transactions use Taproot; existing UTXOs remain on legacy addresses
- **Transaction volume**: Affects 100K-300K Bitcoin transactions/year (estimated 2-6 txs per active user per year)
- **Cost impact**: Aggregate fee savings $50K-150K/year for user base; per-user savings $0.50-1.00 per tx
- **Privacy impact**: All new Taproot transactions indistinguishable from single-key spends; improved privacy vs legacy multisig
- **Competitive impact**: Feature parity with Ledger, BitGo, Blockstream Green; differentiation vs wallets still on legacy ECDSA

### Historical attempts and existing solutions (if any)

Early MuSig2 proof-of-concept was attempted using secp256k1-zkp library [Source: Supplementary Analysis, GPT5.md, line 427]. POC demonstrated basic MuSig2 signing but failed interop testing:
- **PSBT parser incompatibilities**: Some common PSBT libraries (e.g., rust-bitcoin, python-bitcointx) failed to parse MuSig2 partial signatures correctly
- **Hardware wallet issues**: Ledger integration succeeded; Trezor and Coldcard had signature verification failures (signature encoding mismatches)
- **Nonce management**: Initial implementation had subtle nonce reuse risk during retries; required protocol redesign

Project paused due to interop concerns and cryptography engineering capacity constraints [Source: Supplementary Analysis, GPT5.md, line 428].

Key lessons learned:
- Library maturity critical; need well-audited, widely-adopted MuSig2 implementation (secp256k1-zkp or equivalent)
- PSBT interop testing essential; cannot assume ecosystem tools support MuSig2 without validation
- Nonce generation and aggregation require careful review; subtle bugs can break security guarantees
- Ecosystem fragmentation: Ledger supports MuSig2, but Trezor/Coldcard adoption slower

### Known facts, assumptions, and uncertainties

**Facts**:
- Taproot activated November 2021; Schnorr signatures and MuSig2 protocol available [Web: Bitcoin Optech MuSig, 2025]
- MuSig2 provides 20-30% fee savings vs P2WSH multisig [Web: BitGo MuSig2 Guide, 2025]
- Ledger Bitcoin app v2.4.0 supports MuSig2 (Jan 2024) [Web: Ledger MuSig2 Announcement, 2025]
- BitGo deployed MuSig2 for institutional clients [Web: BitGo MuSig2 Guide, 2025]
- Current MPC libraries support ECDSA (GG18/GG20) well; MuSig2 support considered beta [Source: Supplementary Analysis, GPT5.md, line 422]
- Early POC failed PSBT interop with Trezor/Coldcard [Source: Supplementary Analysis, GPT5.md, line 427]

**Assumptions**:
- Stable MuSig2 libraries can be integrated without major reliability regression vs ECDSA [Source: Supplementary Analysis, GPT5.md, line 428]
- Ecosystem PSBT tooling will converge on MuSig2 support within 6-12 months (Trezor, Coldcard catching up to Ledger)
- User adoption of Taproot addresses will be high (≥90%) once available (users value fee savings and privacy)
- Fee savings ($50K-150K/year) justify implementation cost ($120K) with 10-18 month payback

**Uncertainties**:
- Long-term library maintenance: will secp256k1-zkp remain actively maintained? Or switch to alternative (libsecp256k1 native MuSig2)?
- Edge-case interop: will non-standard PSBT parsers in long-tail exchanges/services handle MuSig2 correctly?
- Migration complexity: how to handle users with large legacy UTXO sets (forcing consolidation may be expensive during high fees)
- Competitive timeline: will competitors (e.g., Fireblocks, Coinbase Wallet) deploy MuSig2 faster, eroding differentiation?
- Regulatory treatment: does Taproot privacy (indistinguishable from single-key) raise compliance concerns for institutions?

## Reference

### Web Sources
- [Web: BitGo MuSig2 Guide, 2025] - Save Fees with MuSig2 at BitGo. BitGo Blog. https://blog.bitgo.com/save-fees-with-musig2-at-bitgo-3248d690f573
- [Web: Bitcoin Optech MuSig, 2025] - MuSig. Bitcoin Optech. https://bitcoinops.org/en/topics/musig
- [Web: BitBox MuSig2/FROST Guide, 2025] - MuSig2 and FROST: Explaining multisignature schemes on Taproot. BitBox Blog. https://blog.bitbox.swiss/en/musig2-and-frost-explaining-multisignature-schemes-on-taproot
- [Web: Ledger MuSig2 Announcement, 2025] - MuSig2 Has Arrived in Version 2.4.0 of Ledger Bitcoin App. Ledger Blog. https://www.ledger.com/blog-musig2-ledger-bitcoin-app

### Supplementary Sources
- [Source: Supplementary Analysis, GPT5.md, 2025-11-28] - Blockchain MPC Wallet Problem Extraction. Lines 419-428. Internal analysis document.

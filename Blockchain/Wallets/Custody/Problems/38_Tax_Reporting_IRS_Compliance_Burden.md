# Tax Reporting and IRS Compliance Burden

**Last Updated**: 2025-11-29  
**Status**: Draft  
**Owner**: Documentation Team

## Problem Statement

1. **[CRITICAL]** Q: Digital asset custodians and institutional investors face escalating tax reporting compliance burden with IRS Form 1099-DA implementation requiring wallet-by-wallet cost basis tracking, FIFO/Specific ID methodologies, and comprehensive transaction reporting that brokers cannot fully support. Formulate a structured problem statement using the following [Input] fields.
   A:
   - **Brief description of the problem to be analyzed**: Starting January 1, 2025, IRS Form 1099-DA mandates custodial brokers report digital asset transactions with wallet-by-wallet accounting and FIFO/Specific Identification cost basis methods, eliminating the universal method. Cost basis reporting for 2025 transactions is optional (gross proceeds only), creating reporting gaps where 75%+ of taxpayers are expected to be non-compliant due to incomplete broker data for assets transferred across wallets, chains, or platforms. Implementation costs for institutional custodians are estimated at $500K-$2M for tracking infrastructure, with ongoing compliance costs of $200-500K annually per jurisdiction. [Source: IRS.gov, 2025; camusocpa.com, 2025-11-27]

   - **Background and current situation**: IRS issued final regulations under IRC §6045 requiring custodial digital asset brokers to report sales/exchanges on Form 1099-DA beginning with 2025 transactions. For 2025, brokers report gross proceeds only; mandatory cost basis reporting begins January 1, 2026 for "covered securities" (assets acquired and held continuously on platform). Revenue Procedure 2024-28 eliminates the universal accounting method, requiring wallet-by-wallet or account-by-account cost basis tracking with FIFO as default or properly documented Specific Identification. Congressional Review Act (CRA) overturned DeFi/non-custodial broker requirements, limiting 2025-2026 reporting to custodial exchanges only. IRS Notices 2024-56, 2024-57, and 2025-7 provide transitional relief allowing brokers to delay reporting and omit certain transaction types (wrapping/unwrapping, LP deposits, staking, lending, short sales, notional principal contracts). [Source: IRS.gov, 2025; camusocpa.com, 2025-11-27]

   - **Goals and success criteria**: Achieve 100% accurate Form 1099-DA compliance for all reportable transactions by Q1 2026; reduce cost basis reconstruction time from est. 40-80 hours per complex portfolio to <10 hours through automated tracking systems; maintain wallet-level cost basis records with <1% error rate vs IRS reported data; eliminate CP2000 mismatch notices (IRS underreporting inquiries) for digital asset transactions; comply with FIFO or documented Specific ID standing orders for all dispositions; support transfer statements between brokers when regulations take full effect (target 2027). Timeline: 2025 gross proceeds only → 2026+ cost basis for covered securities. [Source: camusocpa.com, 2025-11-27; IRS.gov, 2025]

   - **Key constraints and resources**: Form 1099-DA reporting begins January 1, 2025 (mandatory); cost basis tracking systems require $500K-$2M implementation for enterprise custodians plus $200-500K/year ongoing compliance costs; wallet-by-wallet accounting mandates separate ledgers for each custodial account, hardware wallet, exchange account; transfer statements between brokers not available until 2027+ (no cross-platform basis lineage); broker UTC timestamps may mismatch taxpayer local time zones creating year-end reporting discrepancies; DeFi/non-custodial transactions exempt from 1099-DA but remain taxable (manual reconciliation required); Rev. Proc. 2024-28 transition safe harbor window closed for most taxpayers; IRS enforcement systems now integrate 1099-DA data with blockchain analytics for address clustering and mismatch detection. [Source: camusocpa.com, 2025-11-27; IRS.gov, 2025]

   - **Stakeholders and roles**: Custodians (reporting obligation, infrastructure investment $500K-$2M, ongoing costs $200-500K/year, audit liability), institutional investors (portfolio tracking across 10-100+ wallets, fiduciary duty for accurate reporting), retail traders (est. 75%+ non-compliance risk due to incomplete records), tax professionals (basis reconstruction est. 40-80h per complex portfolio, documentation standards, audit defense), IRS (enforcement through CP2000 notices, blockchain analytics integration, underreporting detection), software vendors (tracking systems development, wallet-level segregation, FIFO/SpecID automation), auditors (cost basis verification, 1099-DA reconciliation, documentation review). [Source: camusocpa.com, 2025-11-27]

   - **Time scale and impact scope**: Immediate implementation January 1, 2025; affects all custodial brokers serving US taxpayers (estimated 50+ major exchanges, 100+ smaller platforms); institutional custodians managing $100M-$10B+ AUM require multi-wallet tracking infrastructure; individual taxpayers with multi-exchange portfolios face est. 40-80 hours cost basis reconstruction for historical transactions; non-compliance penalties include CP2000 notices (automated underreporting inquiries), potential 20% accuracy-related penalty on underpayment, 75% fraud penalty for willful evasion; covered securities reporting expands 2026+ (acquired on/after January 1, 2026); transfer statement requirements expected 2027+; annual ongoing compliance cost $200-500K per custodian. [Source: camusocpa.com, 2025-11-27; IRS.gov, 2025]

   - **Historical attempts and existing solutions (if any)**: Pre-2025, universal accounting method allowed taxpayers to aggregate all wallets as single pool for lot selection; IRS issued TD 9992 final regulations establishing Form 1099-DA reporting framework; Revenue Procedure 2024-28 provided one-time safe harbor transition (window now closed) for shifting from universal to wallet-by-wallet accounting with basis allocation options; Congressional Review Act overturned DeFi/non-custodial broker requirements in early 2025, limiting reporting perimeter to custodial platforms only; IRS Notices 2024-56, 2024-57, 2025-7 grant transitional relief delaying reporting for specific transaction types and allowing late Form 1099-DA issuance; software vendors (CoinTracker, CoinLedger, TaxBit) offer automated tracking but face limitations with transferred assets, DeFi activity, and cross-chain transactions; Camuso CPA developed SegFIFO™ proprietary methodology for wallet-segmented FIFO tracking aligned with IRS data model. [Source: camusocpa.com, 2025-11-27; IRS.gov, 2025]

   - **Known facts, assumptions, and uncertainties**: 
     - **Facts**: Form 1099-DA mandatory January 1, 2025 [Source: IRS.gov, 2025]; 2025 reporting gross proceeds only, cost basis optional [Source: IRS.gov, 2025]; covered securities cost basis reporting begins January 1, 2026 [Source: IRS.gov, 2025]; universal method eliminated effective January 1, 2025 [Source: Revenue Procedure 2024-28, IRS.gov, 2024]; DeFi/non-custodial brokers exempted via CRA [Source: camusocpa.com, 2025-11-27]; brokers cannot report basis for transferred-in assets, bridged assets, or assets acquired before 2026 [Source: camusocpa.com, 2025-11-27]; transfer statements between brokers not available 2025-2026 [Source: camusocpa.com, 2025-11-27]; implementation cost est. $500K-$2M for enterprise custodians [Source: Industry estimates, 2025]; 75%+ taxpayers expected non-compliant due to incomplete documentation [Source: camusocpa.com, 2025-11-27].
     - **Assumptions**: Transfer statements will be available 2027+; IRS enforcement will intensify as 1099-DA data accumulates; blockchain analytics integration will improve address clustering and mismatch detection; software solutions will mature to handle wallet-level tracking; institutional custodians will invest in compliance infrastructure; cost basis reconstruction demand will increase significantly.
     - **Uncertainties**: Exact timeline for transfer statement implementation; IRS interpretation of "wallet" definition (UTXO model, HD wallets, multi-sig, smart contracts unclear); treatment of DeFi protocol interactions when custody status ambiguous; enforcement prioritization (institutional vs retail); penalty framework for good-faith errors vs willful evasion; regulatory changes to reporting requirements; technological solutions for automated basis tracking across chains; impact of quantum computing on wallet definition and traceability.

---

## Glossary

- **Covered Securities**: Digital assets acquired in a customer's account by a broker on or after January 1, 2026, in exchange for cash or other property, for which brokers must report cost basis.
- **CP2000 Notice**: IRS automated underreporting inquiry sent when information returns (Form 1099-DA) do not match taxpayer-reported amounts on tax return.
- **FIFO (First-In, First-Out)**: Default cost basis method where oldest acquired units are deemed sold first; IRS default when Specific Identification not properly documented.
- **Form 1099-DA**: IRS information return "Digital Asset Proceeds From Broker Transactions" that custodial brokers must use to report digital asset sales/exchanges starting with 2025 transactions.
- **Revenue Procedure 2024-28**: IRS guidance establishing transition safe harbor from universal to wallet-by-wallet accounting for digital assets, with election window that has closed for most taxpayers.
- **SegFIFO™**: Proprietary wallet-segmented FIFO methodology treating each wallet as independent FIFO ledger, aligned with IRS post-2024 rules and Form 1099-DA data model.
- **Specific Identification**: Cost basis method allowing taxpayer to select specific tax lots if identified before disposition, documented with acquisition date/cost/unit detail, maintained per IRC §1012-1(c) requirements; standing orders must be prospective and wallet-specific.
- **Transfer Statements**: Basis information exchanges between brokers when assets transfer between platforms, similar to securities; not available for digital assets until 2027+ per final regulations.
- **Universal Method**: Pre-2025 accounting approach treating all wallets as single aggregated pool for lot selection; eliminated effective January 1, 2025 per Revenue Procedure 2024-28.
- **Wallet-by-Wallet Accounting**: Mandatory IRS requirement effective January 1, 2025 treating each wallet or account as separate cost basis ledger; dispositions must match lots held in same wallet/account only.

---

## Reference

### Regulatory Guidance & Official Notices
- [Source: IRS.gov, 2025] - Final regulations and IRS guidance for reporting by brokers on sales and exchanges of digital assets, IRC §6045 implementation
- [Source: Revenue Procedure 2024-28, IRS.gov, 2024] - Transition safe harbor from universal to wallet-by-wallet accounting for digital assets
- [Source: IRS Notice 2024-56, IRS.gov, 2024] - Transitional relief allowing delayed Form 1099-DA furnishment
- [Source: IRS Notice 2024-57, IRS.gov, 2024] - Relief from reporting identified transaction types (wrapping, LP, staking, lending)
- [Source: IRS Notice 2025-7, IRS.gov, 2025] - Additional transitional relief for standing orders as adequate identification during 2025

### Professional Tax Analysis
- [Source: camusocpa.com, 2025-11-27] - "IRS Form 1099-DA: The Definitive 2025-2026 Guide To Crypto Tax Reporting, Compliance & Cost Basis Rules for Taxpayers" - Comprehensive analysis of Form 1099-DA requirements, wallet-by-wallet accounting transition, cost basis tracking gaps, 75%+ expected non-compliance rates, implementation costs
- [Source: KPMG.com, 2024] - "Cost Basis Reporting for U.S. Digital Asset Brokers" - Analysis of covered securities definition, broker reporting obligations, timeline for mandatory cost basis reporting

### Industry Implementation
- [Source: Industry estimates, 2025] - Enterprise custodian implementation costs $500K-$2M for tracking infrastructure, $200-500K annual ongoing compliance costs

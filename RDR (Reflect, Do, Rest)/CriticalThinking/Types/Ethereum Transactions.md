List all types of 'Ethereum transactions', describing their characteristics, attributes, features, applicable scenarios, relationships, similarities, and differences. Requirements: 1. Ensure your answer is MECE; 2. Keep it concise; 3. Use numbered lists; 4. Create a summary table.

Thu May 22 2025

### 1. Legacy (Type 0) Transactions

Legacy transactions are the original Ethereum transaction format and remain valid since Ethereum's inception, primarily featuring fixed fee mechanisms. Their key attributes include fields such as nonce, gasPrice, gasLimit, recipient address ("to"), value, data, and signature components. Legacy transactions do not have support for advanced functionalities introduced by recent Ethereum Improvement Proposals (EIPs), such as EIP-1559 dynamic fee mechanisms or EIP-2930 access lists.  

**Features and Scenarios:**  
- Simple, straightforward fee calculation—users specify how much they are willing to pay per unit of gas.  
- Used for basic ETH transfers between accounts or simple smart contract calls where fee optimization is not crucial.  
- Remains compatible with older wallets and Ethereum clients.  

---

### 2. Access List (Type 1) Transactions

Access List transactions, introduced by EIP-2930, augment legacy transactions by allowing the sender to specify an access list—addresses and storage slots the transaction expects to touch during execution. This optimization was designed to reduce gas costs during complex smart contract calls, particularly for cross-contract interactions where the set of storage accesses can be predicted in advance.  

**Attributes:**  
- Type set to 0x1.  
- In addition to legacy transaction fields, includes accessList and yParity (parity bit for signature).  
- Does not include the EIP-1559 dynamic fee model.  

**Features and Scenarios:**  
- Allows gas savings by pre-defining cold storage accesses (each access can save up to 100 gas for storage slots and 200 for external addresses).  
- Particularly effective in predictable, multi-contract interactions or DeFi protocols involving complex state changes.  
- Ineffective if access patterns are not deterministic or only a single contract is involved.  

---

### 3. EIP-1559 (Type 2) Transactions

EIP-1559 transactions, standardized in the "London" network upgrade, implement a new dynamic fee structure to improve user experience and network efficiency under congestion. They include new fields maxPriorityFeePerGas and maxFeePerGas, dynamically separate a base fee (burned) from a priority fee (awarded to validators), and may optionally include an access list (inherit features from access list transactions).  

**Attributes:**  
- Type set to 0x2.  
- Contains maxPriorityFeePerGas, maxFeePerGas, accessList, yParity, and chainId.  
- The sender's willing-to-pay maximum for gas is split (some burned as baseFee, some awarded).  

**Features and Scenarios:**  
- Greatly improves fee predictability by auto-adjusting the base fee per network usage.  
- Currently the most widely used transaction format, preferred for most transfers and contract executions especially under varying network congestion.  
- Capable of any operation that legacy or access list transactions can perform, while being more efficient and user-friendly.  

---

### 4. Contract Deployment Transactions

Contract deployment transactions are a functional type designed to create new smart contracts on the Ethereum blockchain. Unlike other transactions, these do not have a "to" field; instead, the "data" field contains the bytecode for the contract to be deployed. These transactions may be structured as legacy, access list, or EIP-1559 transactions, depending on the fee mechanism used.  

**Attributes:**  
- No "to" address; data contains the contract bytecode.  
- Gas limit must be sufficient for the contract’s deployment.  
- May include value (ETH sent to the contract upon creation).  

**Features and Scenarios:**  
- Used exclusively for deploying new smart contracts.  
- The resulting contract will have a unique address, derived from the deployer’s address and their nonce.  
- The cost varies significantly based on contract complexity and size.  

---

### 5. Message Call Transactions

Message call transactions are transactions sent to a recipient, which can be another externally owned account (EOA) or a smart contract. These transactions either transfer ETH or execute a specific function/method on a smart contract.  

**Attributes:**  
- "To" address must be specified, along with value and possibly data (for contract calls).  
- Gas must be supplied to cover the execution cost.  
- Data field is used to encode function calls and parameters for smart contracts.  

**Features and Scenarios:**  
- Used for sending ETH to another account or invoking a smart contract function.  
- Forms the vast majority of user-initiated Ethereum transactions.  
- Can be structured as legacy, access list, or EIP-1559 transactions.  

---

### 6. Relationships, Similarities, and Differences

- **Relationships:**  
  - Legacy, Access List, and EIP-1559 describe transaction formatting and fee calculation, not transaction intent((383)).  
  - Contract Deployment and Message Call describe functionality, not transaction format—any can be encoded in Type 0, 1, or 2 formats.  

- **Similarities:**  
  - All originate from EOAs, are cryptographically signed, and serve to update the Ethereum world state.  
  - Each transaction type can potentially transfer ETH, interact with contracts, and incur variable gas costs.  
  - Deployment and message call transactions cover all possible actions: creating new code or changing existing state.  

- **Differences:**  
  - Transaction "type" (Legacy, Access List, EIP-1559) determines the fee structure and optimization method, while "function" (Deployment or Message Call) describes the purpose/intended action.  
  - EIP-1559 introduces advanced fee predictability, replacing the previous "bid only" gas price system used by legacy and access list transactions.  
  - Only Access List and EIP-1559 permit pre-declaring accessed storage, enabling fine-grained gas optimization on complex smart contract scenarios.  
  - Contract Deployment transactions always lack a "to" address and update the blockchain by adding new code, while Message Calls always specify a "to" address and interact with existing accounts.  

---

### 7. Summary Table

| # | Transaction Type        | Format/Code | Key Attributes                         | Features                                   | Typical Scenarios                           |
|---|------------------------|-------------|----------------------------------------|--------------------------------------------|---------------------------------------------|
| 1 | Legacy                 | Type 0 (0x0)| nonce, gasPrice, gasLimit, to, value, data, signature | Simple fixed fee, pre-EIP-1559 format      | Basic transfers, contract calls             |
| 2 | Access List            | Type 1 (0x1)| All legacy fields plus accessList, yParity | Gas optimization for known storage access  | Complex contract interactions, DeFi         |
| 3 | EIP-1559               | Type 2 (0x2)| maxPriorityFeePerGas, maxFeePerGas, chainId, accessList, yParity, others | Dynamic fee, base and priority fee, accessList optional | All modern transactions, especially high-load|
| 4 | Contract Deployment    | N/A         | No 'to' address, data = contract code  | Deploys new smart contracts                | Publishing new contracts                    |
| 5 | Message Call           | N/A         | to, value, data                        | ETH transfer or smart contract execution   | ETH payments, interacting with contracts    |

---

This list and summary ensure all Ethereum transaction types are mutually exclusive, collectively exhaustive (MECE), and the core details are delivered concisely and accurately.

Bibliography
A Comprehensive Guide to Ethereum Transaction Types. (2025). https://azeezokhamena.hashnode.dev/a-comprehensive-guide-to-ethereum-transaction-types

EIP1559. Transaction type 0 and type 2 - Ethereum Stack Exchange. (2022). https://ethereum.stackexchange.com/questions/131878/eip1559-transaction-type-0-and-type-2

EIP-2930 – Ethereum access list - RareSkills. (2023). https://www.rareskills.io/post/eip-2930-optional-access-list-ethereum

Ethereum Access List ⛽️ It seems that many people either… | Gabi. (2025). https://www.linkedin.com/posts/gabi-vasile_eip-2930-ethereum-access-list-it-seems-activity-7288117316104413185-KjGk

Ethereum transaction types - MetaMask developer documentation. (2025). https://docs.metamask.io/services/concepts/transaction-types/

Ethereum Transactions - Web3j. (2024). https://docs.web3j.io/4.11.0/transactions/transactions/

How do Ethereum transactions work? (2025). https://docs.alchemy.com/docs/how-ethereum-transactions-work

How to Get Contract Deployment Transactions in a Block - Alchemy. (2025). https://www.alchemy.com/docs/how-to-get-contract-deployment-transactions-in-a-block

Mastering Ethereum Transactions - Medium. (2023). https://medium.com/coinmonks/create-and-broadcast-ethereum-transaction-4fe82e1355fb

New Transaction Types on Ethereum - MyCrypto Blog. (2021). https://blog.mycrypto.com/new-transaction-types-on-ethereum

Transaction types - reth Book. (n.d.). https://reth.rs/run/transactions.html

Transactions | Humans.ai Docs. (2024). https://docs.humans.ai/protocol/concepts/transactions

Transactions - Ethereum.org. (2025). https://ethereum.org/en/developers/docs/transactions/

Type of transactions on Ethereum network - ResearchGate. (n.d.). https://www.researchgate.net/figure/Type-of-transactions-on-Ethereum-network_fig1_338450750

Understanding Ethereum Transactions | by ahmetw.eth | Coinmonks. (2023). https://medium.com/coinmonks/understanding-ethereum-transactions-56b06be767e3

Understanding the ways smart contracts call each other. (2024). https://favoriteblockchain.medium.com/understanding-the-ways-smart-contracts-call-each-other-7da68e744738



Generated by Liner
https://getliner.com/search/s/5926611/t/84765496
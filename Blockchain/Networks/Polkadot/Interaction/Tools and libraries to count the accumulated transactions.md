To count the accumulated transactions in a range of blocks on Polkadot as a programmer, you have several tools and libraries at your disposal, each supporting different programming languages and approaches. Here are the main options available according to the knowledge sources:

---

### 1. **Polkadot.js API (JavaScript/TypeScript)**
- Allows you to connect to a Polkadot node, query block data, and iterate over blocks to count transactions (extrinsics).
- Example usage: Connect to a node, fetch blocks in a range, and count the number of extrinsics per block.
- Note: This library is in maintenance mode; for new projects, consider alternatives below.
- [Polkadot.js API documentation](https://docs.polkadot.com/develop/toolkit/api-libraries/polkadot-js-api/)
- [Get started example](https://docs.polkadot.com/develop/toolkit/api-libraries/polkadot-js-api/#get-started)

---

### 2. **Dedot (JavaScript/TypeScript)**
- A next-gen, lightweight client for Polkadot SDK-based blockchains.
- Supports querying on-chain data, including block and extrinsic information.
- [Dedot documentation](https://docs.polkadot.com/develop/toolkit/api-libraries/dedot/#read-on-chain-data)

---

### 3. **Polkadot-API (PAPI, TypeScript)**
- Modern, modular, and type-safe API for interacting with Polkadot chains.
- Optimized for light-client functionality and supports querying blocks and transactions.
- [Polkadot-API (PAPI) documentation](https://docs.polkadot.com/develop/toolkit/api-libraries/papi/#introduction)

---

### 4. **Python Substrate Interface (Python)**
- Python library for connecting to Polkadot SDK-based nodes, querying data, and managing blockchain interactions.
- Suitable for scripting and data analysis tasks.
- [Python Substrate Interface documentation](https://docs.polkadot.com/develop/toolkit/api-libraries/py-substrate-interface/)

---

### 5. **Subxt (Rust)**
- Rust library for type-safe interaction with Polkadot SDK blockchains.
- Enables querying blocks and extrinsics programmatically.
- [Subxt documentation](https://docs.polkadot.com/develop/toolkit/api-libraries/subxt/)

---

### 6. **Sidecar REST API**
- RESTful service for interacting with Polkadot SDK-based chains.
- Provides endpoints to fetch block and extrinsic data, which can be used to count transactions in a block range.
- [Sidecar REST API documentation](https://docs.polkadot.com/develop/toolkit/api-libraries/sidecar/)

---

### 7. **JSON-RPC (Ethereum Compatibility for PolkaVM)**
- If you are working with PolkaVM smart contracts, you can use Ethereum-compatible JSON-RPC methods such as `eth_getBlockTransactionCountByNumber` to get the transaction count for a specific block, then sum over a range.
- [JSON-RPC API documentation](https://docs.polkadot.com/develop/smart-contracts/json-rpc-apis/#eth_getblocktransactioncountbynumber)

---

**Summary:**  
You can use JavaScript/TypeScript libraries (Polkadot.js API, Dedot, PAPI), Python Substrate Interface, Rust’s Subxt, the Sidecar REST API, or Ethereum-compatible JSON-RPC endpoints (for PolkaVM) to programmatically count transactions in a range of blocks on Polkadot. Choose the tool that best fits your programming language and environment preferences.

If you need code examples for a specific tool, let me know which one you’d like to use!
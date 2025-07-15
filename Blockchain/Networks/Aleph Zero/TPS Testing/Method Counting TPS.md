Your questions touch on some important aspects of the Aleph Zero network. Let's address them one by one:

### Getting Real-time Total Number of Confirmed Transactions

To get the real-time total number of confirmed transactions on Aleph Zero, you would typically use the blockchain's RPC (Remote Procedure Call) API. However, Aleph Zero doesn't have a direct API call to get the total number of confirmed transactions across all blocks. Instead, you'll need to use a combination of API calls and some calculation.

Here's a general approach:

1. Use the `chain_getBlock` RPC method to get the latest block.
2. Iterate through blocks, counting transactions in each.
3. Sum up the transaction counts.

The specific API function to use would be:

```
chain_getBlock(blockHash)
```

Where `blockHash` is the hash of the block you want to retrieve. For the latest block, you can use:

```
chain_getFinalisedHead()
```

to get the hash of the latest finalized block.

To get an accurate count, you'd need to:
1. Start from a known point (like genesis block).
2. Iterate through all blocks up to the latest.
3. Count transactions in each block.
4. Keep a running total.

This process can be resource-intensive for a large blockchain, so it's often more practical to maintain a separate indexer or database that keeps track of this information in real-time.

### Ensuring Each Session Has the Same Number of Blocks

Aleph Zero uses a session-based system, and each session is designed to have a fixed number of blocks. This is ensured through the consensus mechanism and blockchain parameters. Here's how it works:

1. **Fixed Session Length**: The number of blocks per session is a network parameter, typically set to 900 blocks for Aleph Zero.

2. **Block Time Target**: Aleph Zero aims for a specific block time (around 1 second).

3. **Consensus Mechanism**: The AlephBFT consensus protocol ensures that blocks are produced at a relatively consistent rate.

4. **Automatic Adjustments**: If block production is faster or slower than expected, the network can make minor adjustments to maintain the target block time.

5. **Session Transitions**: The network transitions to a new session after the predetermined number of blocks, regardless of the actual time taken.

It's important to note that while the number of blocks per session is fixed, the actual time duration of a session might vary slightly due to network conditions. The system is designed to be self-correcting over time, maintaining an average that aligns with the target block time and session length.

### Additional Considerations

- **Block Explorer**: For less technical users or for quick checks, the Aleph Zero block explorer (https://explorer.alephzero.org/) can provide useful information, though it may not give real-time transaction totals.

- **Node Synchronization**: When querying the API, ensure your node is fully synced to get accurate, up-to-date information.

- **API Documentation**: For the most current and detailed API information, always refer to the official Aleph Zero documentation or GitHub repositories.

- **Performance Considerations**: Frequent querying of block data can be resource-intensive. For production systems, consider implementing caching or using an indexing service.

For the most accurate and up-to-date information on API functions and network parameters, I recommend checking the official Aleph Zero documentation or reaching out to their development team directly.
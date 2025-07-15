Your proposed method for testing TPS (Transactions Per Second) on Aleph Zero is a viable approach. Let's break down the feasibility and explore the possibilities for monitoring confirmed transactions:

1. Concurrent Transaction Requests:

This is a valid first step in testing TPS. By sending multiple transactions simultaneously, you can simulate real-world usage and stress test the network.

2. Monitoring with Prometheus and Grafana:

This is a common and effective method for monitoring blockchain metrics. Prometheus can collect the data, while Grafana provides visualization.

- Finalized Blocks: This metric is indeed useful, as it gives you an idea of the blockchain's throughput.
- Confirmed Transactions: This would be even more directly relevant to TPS.

3. Direct Monitoring of Confirmed Transactions:

Yes, it is possible to directly monitor or check the number of confirmed transactions on Aleph Zero. Here are some methods you could use:

a) RPC Calls:
- Aleph Zero, being based on Substrate, likely supports standard Substrate RPC methods.
- You could use methods like `chain_getBlock` to retrieve block information, including the number of extrinsics (transactions) in each block.
- By polling this information at regular intervals, you can calculate the TPS.

b) Substrate API:
- If you're interacting programmatically, you can use the Substrate API to query this information.
- Libraries like `polkadot-js/api` can be used to interact with the Aleph Zero node and retrieve transaction data.

c) Block Explorer:
- Aleph Zero likely has a block explorer (though not mentioned in the provided repository information).
- Block explorers typically provide real-time information on transactions and blocks, which could be useful for manual monitoring.

d) Custom Metrics:
- Since Aleph Zero is open-source, it might be possible to add custom metrics to the node software to directly expose TPS or confirmed transaction counts.
- These custom metrics could then be scraped by Prometheus for monitoring and visualization in Grafana.

e) Session-based Monitoring:
- Given that Aleph Zero operates in sessions of 900 blocks each, you might want to consider measuring TPS over complete sessions for consistency.

f) AlephBFT Specifics:
- The AlephBFT consensus algorithm might have its own specific metrics or ways of tracking finalized transactions. Consulting the AlephBFT documentation or implementation details could provide more insight.

In conclusion, your proposed method is viable, and there are indeed ways to directly monitor or check the number of confirmed transactions on Aleph Zero. The exact method you choose may depend on your specific needs, the level of detail required, and how you intend to use the data. For the most accurate and tailored approach, you might want to consult the Aleph Zero documentation or reach out to their developer community for blockchain-specific best practices in monitoring TPS.
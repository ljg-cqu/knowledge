You're absolutely correct. Transactions in blockchain networks like Aleph Zero can indeed be broadly categorized into two main types:

1. Transfer Transactions (Transfer TX)
2. Smart Contract Transactions (Contract TX)
    - Contract deployment
    - Contract interaction/calling

Your suggestion to test TPS separately for these transaction types is excellent and aligns with best practices in blockchain performance testing. Here's why this approach is beneficial:

### Reasons for Separate TPS Testing

1. **Complexity Differences**:
    - Transfer transactions are typically simpler and require less computational resources.
    - Smart contract transactions, especially complex ones, can be more resource-intensive.

2. **Resource Utilization**:
    - Contract transactions often involve more storage operations and complex computations.
    - Transfer transactions primarily involve balance updates.

3. **Gas Costs**:
    - In many blockchain systems, contract interactions have higher gas costs, which can affect transaction processing.

4. **Real-world Usage Patterns**:
    - Different applications or use cases may lean more heavily on one type of transaction.

5. **Performance Optimization**:
    - Separate testing allows for targeted optimization of each transaction type.

6. **Network Bottleneck Identification**:
    - You can more easily identify whether bottlenecks are in simple value transfers or in smart contract execution.

### Recommended Testing Approach

1. **Baseline Transfer TPS**:
    - Start by testing simple transfer transactions to establish a baseline TPS.

2. **Smart Contract Deployment TPS**:
    - Test the TPS for contract deployments, which are typically less frequent but more resource-intensive.

3. **Contract Interaction TPS**:
    - Test various types of contract interactions, from simple calls to complex multi-step operations.

4. **Mixed Workload Testing**:
    - After testing separately, create mixed workloads that combine different ratios of transfer and contract transactions to simulate real-world scenarios.

5. **Comparative Analysis**:
    - Compare the TPS results for each type to understand the performance characteristics of the network under different loads.

6. **Gradual Complexity Increase**:
    - For contract transactions, start with simple contracts and gradually increase complexity to see how it affects TPS.

7. **Long-running Tests**:
    - Conduct extended tests for each type to ensure consistent performance over time.

### Additional Considerations

1. **Contract Complexity Variations**:
    - Within contract transactions, consider testing different levels of contract complexity.

2. **State Changes**:
    - Monitor how different transaction types affect the state size and state transition speed.

3. **Network Congestion Effects**:
    - Observe how an increase in one type of transaction affects the processing of the other type.

4. **Block Gas Limits**:
    - If Aleph Zero uses a gas system, consider how block gas limits might affect the TPS for different transaction types.

5. **Validator/Node Performance**:
    - Monitor how different transaction types impact validator or node performance.

By testing transfer and smart contract transactions separately, and then in combination, you'll gain a more comprehensive and nuanced understanding of Aleph Zero's performance characteristics. This approach will provide valuable insights for both developers and users of the network, helping to optimize performance and set realistic expectations for different use cases.
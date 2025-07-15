Testing local network Aleph Zero TPS with gas-free transactions can indeed be a useful approach, but it comes with both advantages and considerations. Let's break this down:

### Setting Gas-Fee-Free for TPS Testing

1. Advantages:
    - Simplifies testing by removing gas cost calculations
    - Allows for maximum transaction throughput without economic constraints
    - Useful for measuring raw network capacity

2. Considerations:
    - May not reflect real-world network behavior where gas fees play a role
    - Could potentially lead to unrealistic transaction patterns

### Effects on TPS

Setting gas-free transactions will likely increase the observed TPS for several reasons:

1. Reduced Computation: No need to calculate and deduct gas fees
2. Simplified Validation: Transactions can be processed more quickly without fee checks
3. Increased Transaction Volume: Users (or test scripts) can send transactions without considering costs
4. Reduced State Changes: No balance updates for gas fee transfers

However, this increased TPS might not accurately represent real-world performance where gas fees serve to prevent spam and regulate network usage.

### Enabling Gas-Fee-Free Transactions

To enable gas-fee-free transactions in a local Aleph Zero network:

1. Modify the Runtime:
    - You'll need to modify the runtime code to remove gas fee calculations
    - This typically involves changing the `WeightToFee` conversion in the runtime

2. Use the `--dev` Flag:
    - When starting your local node, use the `--dev` flag which often disables fees for development purposes

3. Custom Chain Spec:
    - Create a custom chain specification file where you can define fee-less transactions

4. Example (conceptual, not actual code):
   ```rust
   pub struct WeightToFee;
   impl WeightToFeePolynomial for WeightToFee {
       type Balance = Balance;
       fn polynomial() -> WeightToFeeCoefficients<Self::Balance> {
           smallvec::smallvec!(WeightToFeeCoefficient {
               coeff_integer: 0,
               coeff_frac: Perbill::zero(),
               negative: false,
               degree: 1,
           })
       }
   }
   ```

### Additional Considerations

1. Realistic Testing: While gas-free testing can provide insights into maximum throughput, it's also important to conduct tests with gas fees to simulate real-world conditions.

2. Spam Protection: In a gas-free environment, implement alternative spam protection mechanisms for your tests to prevent unrealistic flooding of the network.

3. Transaction Complexity: Consider testing with a mix of simple and complex transactions to get a more comprehensive view of network performance.

4. Monitoring Resources: Keep an eye on node resource usage (CPU, memory, disk I/O) as these can become bottlenecks in high-TPS scenarios.

5. Comparative Testing: Run tests both with and without gas fees to understand the impact on TPS and overall network behavior.

Remember, while gas-free testing can provide valuable insights into maximum theoretical throughput, it's crucial to also conduct tests that more closely mimic real-world conditions for a balanced understanding of network performance.

For the most accurate and up-to-date information on modifying Aleph Zero for testing purposes, I recommend consulting the official Aleph Zero documentation or reaching out to their development team directly.
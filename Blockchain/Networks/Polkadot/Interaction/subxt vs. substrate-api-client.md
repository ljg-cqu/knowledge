subxt vs. substrate-api-client

Thu Jul 17 2025

### Primary Purpose
- **subxt**: Subxt is a comprehensive library designed for interacting with Substrate-based blockchains, with a focus on submitting extrinsics (hence the name). It provides a type-safe interface for blockchain interactions and is the primary Rust library recommended by Parity Technologies.
- **substrate-api-client**: The substrate-api-client is positioned as a simpler, lightweight alternative to subxt, specifically focused on providing features for no-std environments. It's particularly useful for embedded devices and trusted execution environments where standard library support may not be available.

### Development
- **subxt**: Developed and maintained by Parity Technologies (paritytech) as part of the official Substrate ecosystem. It has strong backing and integration with the Polkadot/Substrate development stack.
- **substrate-api-client**: A community-driven project developed by Supercomputing Systems (SCS). It receives periodic funding from the Kusama Treasury for maintenance and improvements.

### Type Safety
- **subxt**: Provides strong compile-time type safety by generating types from node metadata using the `#` macro. It validates that generated types match the runtime at compile time, reducing runtime errors.
- **substrate-api-client**: Offers basic type safety but requires more manual configuration. Users need to manually configure node-specific data like runtime configs.

### Code Generation
- **subxt**: Features automatic code generation from metadata using the subxt-cli tool and macros. This creates a statically-typed interface that matches the target blockchain's runtime.
- **substrate-api-client**: Does not provide automatic code generation. Developers work directly with the API without generated types.

### Environment Support
- **subxt**: Primarily designed for standard (std) environments but can be compiled to WASM for browser applications. It requires network access for most operations.
- **substrate-api-client**: Specifically designed with no-std support as a primary feature, making it suitable for embedded devices, IoT environments, and trusted execution environments like Intel SGX. Most features except the RPC client work in no-std environments.

### Features
- **subxt**: Offers comprehensive functionality including transactions, storage queries, events, constants, blocks, runtime APIs, custom values, and raw RPC calls. It provides both high-level and low-level APIs for flexibility.
- **substrate-api-client**: Provides core functionality for composing extrinsics, querying storage, watching events, and parsing metadata. It's more focused on essential operations rather than comprehensive coverage.

### Client Types
- **subxt**: Provides multiple client types - OnlineClient for network operations, OfflineClient for offline operations, and an unstable LightClient feature. This allows for different usage patterns depending on network requirements.
- **substrate-api-client**: Uses a single Api client that can work with different RPC client implementations. For no-std environments, users must implement their own RPC client.

### Async Support
- **subxt**: Built with native async/await support using tokio runtime. All operations are primarily async-first.
- **substrate-api-client**: Provides both async and sync implementations, allowing developers to choose based on their needs. Examples are provided for both patterns.

### WebSocket Libraries
- **subxt**: Uses jsonrpsee as the default WebSocket client. It has built-in support for reconnection handling through the unstable-reconnecting-rpc-client feature.
- **substrate-api-client**: Supports multiple WebSocket crates including jsonrpsee, tungstenite, and ws. This provides flexibility for different environments and requirements.

### Reconnection
- **subxt**: Features built-in reconnection support through the unstable-reconnecting-rpc-client feature. It can automatically retry RPC calls and reestablish subscriptions when connections are lost.
- **substrate-api-client**: Requires manual handling of reconnections. Users are responsible for detecting connection loss and re-establishing connections.

### Documentation
- **subxt**: Provides comprehensive documentation including a detailed guide, API documentation, and numerous examples. It includes both simple and complex examples like parachain and WASM examples.
- **substrate-api-client**: Offers good examples for common use cases and maintains documentation, though less extensive than subxt. Examples are split between async and sync implementations.

### Use Cases
- **subxt**: Best suited for general-purpose Substrate interaction, production applications, and browser-based apps. It's the recommended choice for most standard development scenarios.
- **substrate-api-client**: Ideal for resource-constrained environments, embedded devices, IoT applications, and trusted execution environments where no-std support is crucial. It fills a specific niche that subxt doesn't address.

Bibliography
Activity · scs/substrate-api-client - GitHub. (n.d.). https://github.com/scs/substrate-api-client/activity

Hottest “subxt” Answers - Substrate and Polkadot Stack Exchange. (2022). https://substrate.stackexchange.com/tags/subxt/hot

Issues · paritytech/subxt - GitHub. (2021). https://github.com/paritytech/subxt/issues

Issues · scs/substrate-api-client - GitHub. (2025). https://github.com/scs/substrate-api-client/issues

Maintenance for the substrate-api-client Feb-23 to Apr-23. (n.d.). https://kusama.subsquare.io/referenda/88

Maintenance for the substrate-api-client Feb-23 to Apr-23 #2159. (n.d.). https://kusama.polkassembly.io/post/2159

Maintenance for the substrate-api-client May-23 to Jul-23 #2566. (2023). https://kusama.polkassembly.io/post/2566

Maintenance for the substrate-api-client Nov-22 to Jan-23 #1923. (n.d.). https://kusama.polkassembly.io/post/1923

paritytech/subxt: Interact with Substrate based nodes in ... - GitHub. (2019). https://github.com/paritytech/subxt

scs/substrate-api-client - GitHub. (2019). https://github.com/scs/substrate-api-client

substrate-api-client - crates.io: Rust Package Registry. (2023). https://crates.io/crates/substrate-api-client/0.11.0

substrate_api_client - Rust - Docs.rs. (2021). https://docs.rs/substrate-api-client

subxt | infrablockchain-docs. (2023). https://docs.infrablockchain.net/infrablockchain-docs/infrablockchain/learn/substrate/learn/command-line-tools/subxt

subxt - crates.io: Rust Package Registry. (2022). https://crates.io/crates/subxt/0.19.0

subxt - Rust. (2023). https://tidelabs.github.io/tidext/subxt/index.html

subxt - Rust - Docs.rs. (2021). https://docs.rs/subxt

subxt 0.42.1 - Docs.rs. (n.d.). https://docs.rs/crate/subxt/latest/source/README.md

Subxt: deep dive into `reconnecting/retry functionality` - Tech Talk. (2024). https://forum.polkadot.network/t/subxt-deep-dive-into-reconnecting-retry-functionality/8581

Subxt Rust API | Polkadot Developer Docs. (2025). https://docs.polkadot.com/develop/toolkit/api-libraries/subxt/

subxt::book - Rust - Docs.rs. (2021). https://docs.rs/subxt/latest/subxt/book/index.html

subxt-cli — Rust application // Lib.rs. (n.d.). https://lib.rs/crates/subxt-cli

subxt-signer - crates.io: Rust Package Registry. (2025). https://crates.io/crates/subxt-signer

Tip request for adding Polkadot-JS account support to Subxt. (n.d.). https://kusama.subsquare.io/polkassembly/posts/2667



Generated by Liner
https://getliner.com/search/s/5926611/t/86619260
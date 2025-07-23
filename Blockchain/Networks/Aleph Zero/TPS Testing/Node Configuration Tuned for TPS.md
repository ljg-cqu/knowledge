which of the following args for Aleph Zero node have significat impact on TPS? You need to consider from network connecting, mpool limit to logic, ect. To have the best TPS performance, how should I adjust the config? 
 
 Options: 
       --unit-creation-delay <UNIT_CREATION_DELAY>                                    [default: 200] 
       --public-validator-addresses <PUBLIC_VALIDATOR_ADDRESSES>                      The addresses at which the node will be externally reachable for validator network purposes. Have to be provided for validators 
       --validator-port <VALIDATOR_PORT>                                              The port on which to listen to validator network connections [default: 30343] 
       --no-backup                                                                    Turn off backups, at the cost of limiting crash recoverability 
       --backup-path <PATH>                                                           The path to save backups to 
       --max-nonfinalized-blocks <MAX_NONFINALIZED_BLOCKS>                            The maximum number of nonfinalized blocks, after which block production should be locally stopped. DO NOT CHANGE THIS, PRODUCING MORE OR FEWER BLOCKS MIGHT BE CONSIDERED MALICIOUS BEHAVIOUR AND PUNISHED ACCORDINGLY! 
                                                                                      [default: 20] 
       --enable-pruning                                                               Enable database pruning. It removes older entries in the state-database. Pruning of blocks is not supported. Note that we only support pruning with ParityDB database backend. See also `--state-pruning` option for more 
                                                                                      details 
       --alephbft-network-bit-rate <ALEPHBFT_NETWORK_BIT_RATE>                        Maximum bit-rate in bits per second of the alephbft validator network [default: 786432] 
       --substrate-network-bit-rate <SUBSTRATE_NETWORK_BIT_RATE>                      Maximum bit-rate in bits per second of the substrate network [default: 5242880] 
       --collect-validator-network-data                                               Don't spend some extra time to collect more debugging data (e.g. validator network details). By default collecting is enabled, as the impact on performance is negligible, if any 
       --validator                                                                    Enable validator mode 
       --no-grandpa                                                                   Disable GRANDPA 
       --rpc-external                                                                 Listen to all RPC interfaces (default: local) 
       --unsafe-rpc-external                                                          Listen to all RPC interfaces 
       --rpc-methods <METHOD SET>                                                     RPC methods to expose. [default: auto] [possible values: auto, safe, unsafe] 
       --rpc-max-request-size <RPC_MAX_REQUEST_SIZE>                                  Set the maximum RPC request payload size for both HTTP and WS in megabytes [default: 15] 
       --rpc-max-response-size <RPC_MAX_RESPONSE_SIZE>                                Set the maximum RPC response payload size for both HTTP and WS in megabytes [default: 15] 
       --rpc-max-subscriptions-per-connection <RPC_MAX_SUBSCRIPTIONS_PER_CONNECTION>  Set the maximum concurrent subscriptions per connection [default: 1024] 
       --rpc-port <PORT>                                                              Specify JSON-RPC server TCP port 
       --rpc-max-connections <COUNT>                                                  Maximum number of RPC server connections [default: 100] 
       --rpc-cors <ORIGINS>                                                           Specify browser *origins* allowed to access the HTTP and WS RPC servers 
       --name <NAME>                                                                  The human-readable name for this node 
       --no-telemetry                                                                 Disable connecting to the Substrate telemetry server 
       --telemetry-url <URL VERBOSITY>                                                The URL of the telemetry server to connect to 
       --prometheus-port <PORT>                                                       Specify Prometheus exporter TCP Port 
       --prometheus-external                                                          Expose Prometheus exporter on all interfaces 
       --no-prometheus                                                                Do not expose a Prometheus exporter endpoint 
       --max-runtime-instances <MAX_RUNTIME_INSTANCES>                                The size of the instances cache for each runtime [max: 32] [default: 8] 
       --runtime-cache-size <RUNTIME_CACHE_SIZE>                                      Maximum number of different runtimes that can be cached [default: 2] 
       --offchain-worker <ENABLED>                                                    Execute offchain workers on every block [default: when-authority] [possible values: always, never, when-authority] 
       --enable-offchain-indexing <ENABLE_OFFCHAIN_INDEXING>                          Enable offchain indexing API [default: false] [possible values: true, false] 
       --chain <CHAIN_SPEC>                                                           Specify the chain specification 
       --dev                                                                          Specify the development chain 
   -d, --base-path <PATH>                                                             Specify custom base path 
   -l, --log <LOG_PATTERN>...                                                         Sets a custom logging filter (syntax: `<target>=<level>`) 
       --detailed-log-output                                                          Enable detailed log output 
       --disable-log-color                                                            Disable log color output 
       --enable-log-reloading                                                         Enable feature to dynamically update and reload the log filter 
       --tracing-targets <TARGETS>                                                    Sets a custom profiling filter 
       --tracing-receiver <RECEIVER>                                                  Receiver to process tracing messages [default: log] [possible values: log] 
       --state-pruning <PRUNING_MODE>                                                 Specify the state pruning mode 
       --blocks-pruning <PRUNING_MODE>                                                Specify the blocks pruning mode [default: archive-canonical] 
       --database <DB>                                                                Select database backend to use [possible values: rocksdb, paritydb, auto, paritydb-experimental] 
       --db-cache <MiB>                                                               Limit the memory the database cache can use 
       --wasm-execution <METHOD>                                                      Method for executing Wasm runtime code [default: compiled] [possible values: interpreted-i-know-what-i-do, compiled] 
       --wasmtime-instantiation-strategy <STRATEGY>                                   The WASM instantiation method to use [default: pooling-copy-on-write] [possible values: pooling-copy-on-write, recreate-instance-copy-on-write, pooling, recreate-instance] 
       --wasm-runtime-overrides <PATH>                                                Specify the path where local WASM runtimes are stored 
       --execution-syncing <STRATEGY>                                                 Runtime execution strategy for importing blocks during initial sync [possible values: native, wasm, both, native-else-wasm] 
       --execution-import-block <STRATEGY>                                            Runtime execution strategy for general block import (including locally authored blocks) [possible values: native, wasm, both, native-else-wasm] 
       --execution-block-construction <STRATEGY>                                      Runtime execution strategy for constructing blocks [possible values: native, wasm, both, native-else-wasm] 
       --execution-offchain-worker <STRATEGY>                                         Runtime execution strategy for offchain workers [possible values: native, wasm, both, native-else-wasm] 
       --execution-other <STRATEGY>                                                   Runtime execution strategy when not syncing, importing or constructing blocks [possible values: native, wasm, both, native-else-wasm] 
       --execution <STRATEGY>                                                         The execution strategy that should be used by all execution contexts [possible values: native, wasm, both, native-else-wasm] 
       --trie-cache-size <Bytes>                                                      Specify the state cache size [default: 67108864] 
       --state-cache-size <STATE_CACHE_SIZE>                                          DEPRECATED: switch to `--trie-cache-size` 
       --bootnodes <ADDR>...                                                          Specify a list of bootnodes 
       --reserved-nodes <ADDR>...                                                     Specify a list of reserved node addresses 
       --reserved-only                                                                Whether to only synchronize the chain with reserved nodes 
       --public-addr <PUBLIC_ADDR>...                                                 Public address that other nodes will use to connect to this node 
       --listen-addr <LISTEN_ADDR>...                                                 Listen on this multiaddress 
       --port <PORT>                                                                  Specify p2p protocol TCP port 
       --no-private-ip                                                                Always forbid connecting to private IPv4/IPv6 addresses 
       --allow-private-ip                                                             Always accept connecting to private IPv4/IPv6 addresses 
       --out-peers <COUNT>                                                            Number of outgoing connections we're trying to maintain [default: 8] 
       --in-peers <COUNT>                                                             Maximum number of inbound full nodes peers [default: 32] 
       --in-peers-light <COUNT>                                                       Maximum number of inbound light nodes peers [default: 100] 
       --no-mdns                                                                      Disable mDNS discovery (default: true) 
       --max-parallel-downloads <COUNT>                                               Maximum number of peers from which to ask for the same blocks in parallel [default: 5] 
       --node-key <KEY>                                                               Secret key to use for p2p networking 
       --node-key-type <TYPE>                                                         Crypto primitive to use for p2p networking [default: ed25519] [possible values: ed25519] 
       --node-key-file <FILE>                                                         File from which to read the node's secret key to use for p2p networking 
       --discover-local                                                               Enable peer discovery on local networks 
       --kademlia-disjoint-query-paths                                                Require iterative Kademlia DHT queries to use disjoint paths 
       --kademlia-replication-factor <KADEMLIA_REPLICATION_FACTOR>                    Kademlia replication factor [default: 20] 
       --ipfs-server                                                                  Join the IPFS network and serve transactions over bitswap protocol 
       --sync <SYNC_MODE>                                                             Blockchain syncing mode. [default: full] [possible values: full, fast, fast-unsafe, warp] 
       --max-blocks-per-request <COUNT>                                               Maximum number of blocks per request [default: 64] 
       --pool-limit <COUNT>                                                           Maximum number of transactions in the transaction pool [default: 8192] 
       --pool-kbytes <COUNT>                                                          Maximum number of kilobytes of all transactions stored in the pool [default: 20480] 
       --tx-ban-seconds <SECONDS>                                                     How long a transaction is banned for 
       --keystore-path <PATH>                                                         Specify custom keystore path 
       --password-interactive                                                         Use interactive shell for entering the password used by the keystore 
       --password <PASSWORD>                                                          Password used by the keystore 
       --password-filename <PATH>                                                     File that contains the password used by the keystore 
       --alice                                                                        Shortcut for `--name Alice --validator` 
       --bob                                                                          Shortcut for `--name Bob --validator` 
       --charlie                                                                      Shortcut for `--name Charlie --validator` 
       --dave                                                                         Shortcut for `--name Dave --validator` 
       --eve                                                                          Shortcut for `--name Eve --validator` 
       --ferdie                                                                       Shortcut for `--name Ferdie --validator` 
       --one                                                                          Shortcut for `--name One --validator` 
       --two                                                                          Shortcut for `--name Two --validator` 
       --force-authoring                                                              Enable authoring even when offline 
       --tmp                                                                          Run a temporary node 
   -h, --help                                                                         Print help (see more with '--help') 
   -V, --version                                                                      Print version

Wed Jul 23 2025

The Aleph Zero node arguments that have significant impact on TPS performance span network connection settings, transaction pool limits, execution logic, and database/cache configurations. To optimize for the best TPS, here are the key arguments and recommended adjustments:

### Network Connection Settings
- **--alephbft-network-bit-rate** and **--substrate-network-bit-rate**: These control the max bit-rate in bits per second for the AlephBFT validator network and substrate network respectively. Increasing these values allows more data throughput between nodes, which is crucial to achieve high TPS. The defaults are 786432 bits/s and 5242880 bits/s; raising them carefully (depending on your available bandwidth) improves TPS by reducing network bottlenecks.
- **--validator-port** and **--public-validator-addresses**: Correctly setting these ensures validator nodes connect properly in the network, maintaining high availability and throughput. Validator addresses must be reachable externally for effective consensus participation, directly influencing TPS.
- **--out-peers**, **--in-peers**, and **--in-peers-light**: Adjusting these (defaults: 8 outgoing, 32 inbound full nodes, 100 inbound light nodes) can help maintain optimal peer connections for performance and data propagation speed.

### Transaction Pool Limits
- **--pool-limit** (default: 8192) and **--pool-kbytes** (default: 20480): These define how many transactions and total transaction size (in KB) can reside in the mempool waiting for processing. Increasing these limits allows the node to handle more pending transactions, boosting TPS especially under high load. However, extremely high limits risk higher memory consumption and latency, so values should be configured to fit node hardware.
- **--tx-ban-seconds**: Controls how long invalid or malicious transactions are banned. Setting this appropriately prevents invalid transactions from impacting pool performance.

### Execution and Database Settings
- **--execution, --execution-syncing, --execution-import-block, --execution-block-construction**: Use native execution strategy rather than interpreted Wasm for best performance. Native execution significantly reduces runtime overhead, lowering confirmation times and improving TPS.
- **--database**: Using a performant database backend like `rocksdb` or `paritydb` is essential, with `paritydb` often preferred for performance and pruning support. 
- **--db-cache**: Increasing database cache size boosts TPS by allowing more data to be cached in memory, reducing disk I/O bottlenecks. Allocate cache based on available RAM, for example 512 MB or more.
- **--trie-cache-size**: Increasing state trie cache size (default 64 MB) improves state access times, aiding throughput.

### Other Performance-relevant Settings
- **--enable-pruning**: Enabling pruning reduces database bloat and can improve node performance by removing old state entries.
- **--unit-creation-delay** (default 200ms): This argument controls the delay between creating DAG units. Reducing this delay can increase TPS but may impact network and CPU load; should be tuned carefully.
- **--no-backup / --backup-path**: Turn off backups only if you are certain about crash recovery management; backups may add overhead.
- **--prometheus-port / --no-prometheus**: Monitoring tools are crucial but can slightly affect performance; disable if strict maximum TPS is critical and monitoring overhead is not desired.

### Summary of Recommended Configurations for Best TPS
| Argument                      | Recommendation                          | Reason                                 |
|------------------------------|---------------------------------------|---------------------------------------|
| --alephbft-network-bit-rate  | Increase above default if bandwidth allows | Greater validator network throughput  |
| --substrate-network-bit-rate  | Increase above default                 | Better substrate network data flow    |
| --pool-limit                 | Increase moderately (e.g., 12000-20000) | Handles more pending transactions     |
| --pool-kbytes                | Increase accordingly (e.g., 30000-40000 KB) | Larger mempool capacity                |
| --execution                 | Set to `native`                        | Faster execution of runtime logic     |
| --database                  | Use `paritydb`                        | Efficient storage and pruning support |
| --db-cache                  | Increase (e.g., 512 MB or more)       | Improve data caching and I/O          |
| --trie-cache-size           | Increase (e.g., 128MB or more)         | Faster state access                    |
| --unit-creation-delay       | Reduce cautiously if possible (e.g., 100-150 ms) | Increase transaction unit creation rate |
| --validator-port / --public-validator-addresses | Set correctly for network connectivity | Ensures validator network participation |

### Conclusion
To maximize TPS on an Aleph Zero node, the most impactful adjustments involve increasing network bit rates for AlephBFT and substrate, enlarging mempool limits (`--pool-limit`, `--pool-kbytes`), favoring native runtime execution, optimizing database backend and cache sizes, and tuning unit creation delay carefully. Proper network connectivity settings ensure effective validator participation, which also impacts TPS. Balancing these parameters according to available hardware and network resources will yield optimal TPS performance.

If further tuning is needed, regular monitoring via Prometheus and telemetry should be employed to detect bottlenecks and optimize accordingly.

Bibliography
About Aleph Zero. (2024). https://docs.alephzero.org/aleph-zero/explore/about-aleph-zero

Aleph Zero Testnet 14.0 “Uqbar” – Even More Stability and ... (2024). https://alephzero.org/blog/aleph-zero-testnet-14-uqbar/

AlephBFT Consensus - Aleph Zero. (2025). https://docs.alephzero.org/aleph-zero/explore/alephbft-consensus

Breaking the Limits: The Power of Aleph Zero’s Layer 1 ... - Medium. (2023). https://medium.com/@researchcoindelta/breaking-the-limits-the-power-of-aleph-zeros-layer-1-zero-knowledge-proof-system-e4dad99cc9c9

Fundamentals: TPS vs. Latency vs. Finality - Aleph Zero. (2022). https://alephzero.org/blog/tps-latency-finality/

Running the binary | Aleph Zero. (2025). https://docs.alephzero.org/aleph-zero/use/validate/running-an-aleph-node-on-testnet/building-and-running-from-source-advanced/running-the-binary

What Is The Fastest Blockchain And Why? Analysis of 43 Blockchains. (2021). https://alephzero.org/blog/what-is-the-fastest-blockchain-and-why-analysis-of-43-blockchains/



Generated by Liner
https://getliner.com/search/s/5926611/t/86769104
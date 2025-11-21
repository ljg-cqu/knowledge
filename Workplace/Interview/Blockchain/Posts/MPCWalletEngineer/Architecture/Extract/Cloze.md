1. Q: In hexagonal architecture for MPC wallets, cryptographic operations are isolated in the ___ layer, which is accessed through well-defined ___ (interfaces).
   A: domain core; ports

1. Q: The hexagonal architecture reduces coupling by ___ to ___% and enables independent testing while adding ___% complexity overhead.
   A: 40; 60; 15-20

1. Q: A threshold signature scheme requires ___ out of ___ participants to create a valid signature, with common configurations being ___-of-___ or ___-of-___.
   A: T; N; 2; 3; 3; 5

1. Q: The security property $t > \frac{n}{2}$ ensures ___ consensus, where t is the ___ and n is the ___.
   A: majority; minimum number of shares required; total number of shares

1. Q: List the three primary modules in an MPC wallet core domain.
   A: KeyGenerationService (threshold key generation), ShareManager (encrypted shard storage/retrieval), SigningCoordinator (multi-party signature protocol execution)

1. Q: In the saga pattern for MPC signing, if threshold participants don't respond in a round, the orchestrator broadcasts a(n) ___ message and triggers ___ for suspected compromised nodes.
   A: abort; key rotation

1. Q: Saga orchestration reduces partial signature failures from ___-___% to <___% but increases latency by ___-___ms per retry cycle.
   A: 15; 20; 2; 30; 50

1. Q: Circuit breakers transition to ___ state after ___ consecutive failures and enter ___ state after a timeout period to test recovery.
   A: Open; 3; HalfOpen

1. Q: The FROST protocol requires ___ rounds for signing after pre-processing, compared to GG20's ___ rounds, achieving ___ms latency vs. ___ms.
   A: 2; 5; 120; 300

1. Q: In CQRS architecture, the ___ model handles write operations while the ___ model optimizes for queries, achieving ___x read performance improvement.
   A: Command; Query; 10

1. Q: Key shares in MPC wallets are encrypted at rest using ___ with unique per-share keys stored in ___ or ___.
   A: AES-256-GCM; HSM; KMS

1. Q: The target signing latency for MPC wallets is <___ms for mobile devices and <___ms for server environments, with signing success rate >___%.
   A: 200; 100; 98

1. Q: Rate limiting using ___ bucket algorithm prevents DDoS attacks with ___% attack prevention effectiveness.
   A: token; 95

1. Q: gRPC reduces latency by ___-___% compared to REST for internal services, using ___ protocol and ___ serialization.
   A: 50; 70; HTTP/2; Protocol Buffers

1. Q: The three key invariants for threshold ECDSA key shares are: (1) no individual share ___, (2) any t out of n shares must ___, and (3) shares cannot be ___.
   A: reveals the private key; produce a valid signature; reconstructed in plaintext

1. Q: Multi-region crypto cluster deployment reduces blast radius for key-compromise incidents by ___-___% compared to single-region deployment.
   A: 50; 70

1. Q: List the 5 states in a circuit breaker state machine for MPC signing orchestration.
   A: CLOSED (normal operation), HALF_OPEN (degraded mode), OPEN (ceremony aborted), COOLDOWN (waiting before retry), RECOVERY (checkpoint-based retry)

1. Q: WebAssembly with ___ enables client-side cryptographic operations, achieving ___x speed improvement on modern mobile processors.
   A: SIMD; 1.8

1. Q: The saga pattern for threshold signing includes four main steps: ___ round, ___ exchange, partial signature generation, and signature ___.
   A: commitment; zero-knowledge proof; aggregation

1. Q: Target metrics for MPC wallet systems include <___% module coupling, >___% test coverage for crypto modules, and ___ security boundary violations.
   A: 30; 85; 0

1. Q: Adaptive timeout thresholds scale based on network conditions: ___th percentile = normal, ___th = warning, ___th = trip circuit.
   A: 50; 95; 99

1. Q: The DDD aggregate pattern enforces that no set of <___ shares can ___ the private key or ___ signatures.
   A: t; reconstruct; forge

1. Q: Presignature pools reduce end-to-end signing latency by ___-___% but require ___-___MB RAM per pool.
   A: 60; 70; 50; 100

1. Q: In event sourcing, all key share mutations are captured as ___ events, enabling complete history reconstruction and providing a(n) ___ trail.
   A: domain; audit

1. Q: The strategy pattern for multi-chain integration reduces integration time to ≤___ days and achieves ___-___% code reuse across chains.
   A: 5; 85; 95

1. Q: For Byzantine fault tolerance in MPC, the threshold must satisfy the constraint: ___ (mathematical formula).
   A: $t > \frac{n}{2}$

1. Q: Hexagonal architecture attack surface reduction targets ≥___% compared to monolithic designs, achieved through ___ boundaries.
   A: 70; isolation

1. Q: The three bounded contexts in a multi-region MPC wallet platform are ___ (MPC protocol execution), ___ (business logic), and ___ (chain-specific handling).
   A: Crypto Core; Wallet Orchestration; Chain Gateway

1. Q: List the 4 compensation actions when an MPC signing saga fails.
   A: deregister participants, revoke commitments, release shard locks, publish compensation event

1. Q: GG20 protocol uses ___ curves and requires ___ rounds of communication, while FROST uses ___ signatures and ___ rounds.
   A: ECDSA; 5; Schnorr; 2

1. Q: Module coupling is calculated as ___ divided by ___, with a target value of <___.
   A: external dependencies; total modules; 0.3 (30%)

1. Q: The three layers in hexagonal architecture are: Application Layer (___), Domain Layer (___), and Infrastructure Layer (___).
   A: orchestration; business logic; cryptographic implementations

1. Q: For production MPC wallets, Recovery Time Objective (RTO) should be <___ minutes and Recovery Point Objective (RPO) should be ___.
   A: 15; 0 (no data loss)

1. Q: Checkpoint-based recovery in MPC signing reduces retry cost by ___-___% by allowing Round 2 retry without restarting ___.
   A: 40; 50; the entire ceremony

1. Q: Target MPC signing success rate in production systems should exceed ___% with compensation frequency <___%.
   A: 98; 5

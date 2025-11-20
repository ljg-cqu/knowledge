1. Q: In MPC wallet architecture, the hexagonal pattern isolates the core ___ logic from external dependencies through well-defined ___ (interfaces) and ___ (implementations).
   A: cryptographic; ports; adapters

1. Q: Threshold signature schemes typically use a ___-of-___ configuration where T participants can create a valid signature but fewer than T cannot.
   A: t-of-n (or threshold-of-total)

1. Q: The saga pattern reduces MPC signing ceremony failures by approximately ___% by implementing compensating actions for distributed transactions.
   A: 85% (±10%)

1. Q: CQRS separates ___ operations from ___ operations to optimize performance in MPC wallet systems.
   A: write (command); read (query)

1. Q: Pre-computation of nonce pairs can reduce MPC signing latency from approximately ___ ms to ___ ms.
   A: 200ms; 80-120ms

1. Q: Multi-layer encryption for key shards typically involves encrypting with a shard-specific key, then encrypting that key with a ___ key stored in an ___.
   A: master; HSM

1. Q: FROST threshold signatures reduce signing to ___ round(s) after preprocessing, compared to GG20's ___ rounds.
   A: 1; 2-3 (or 2)

1. Q: In MPC wallets, the target signing latency for mobile devices is typically ___ ms to maintain acceptable user experience.
   A: <100ms (or sub-100ms)

1. Q: The Circuit Breaker pattern prevents ___ failures by temporarily halting requests to failing services, improving fault isolation by approximately ___%.
   A: cascading; 30%

1. Q: Event sourcing provides ___ consistency with projection lag typically between ___ ms to ___ ms.
   A: eventual; 100; 500

1. Q: Rate limiting using token bucket algorithms helps maintain signing API latency below ___ ms at ___ requests per second.
   A: 100; 1000 (or 1K)

1. Q: For enterprise MPC wallet systems, the target availability SLA is typically ___%, with RTO (Recovery Time Objective) of less than ___ minutes.
   A: 99.99%; 15

1. Q: Geographic distribution of key shards across multiple regions can reduce single-point compromise risk by approximately ___%.
   A: 80% (70-80% range acceptable)

1. Q: gRPC streaming reduces client polling overhead by approximately ___% compared to REST for long-running MPC ceremonies.
   A: 70%

1. Q: Hexagonal architecture can improve test execution time by ___% to ___% by enabling testing with mock adapters.
   A: 85%; 95%

1. Q: List the three primary layers in hexagonal architecture for MPC wallets.
   A: Application layer (orchestration), Domain layer (business logic), Infrastructure layer (cryptographic implementations)

1. Q: In CQRS architecture for MPC wallets, write latency typically increases by ___ ms to ___ ms due to event-sourced synchronization.
   A: 20; 40

1. Q: The minimum security level maintained across all MPC wallet optimizations should be ___ bits.
   A: 128 bits (or 256 bits for higher security)

1. Q: Batch processing of MPC signatures can achieve throughput improvement of approximately ___% to ___%.
   A: 30%; 50%

1. Q: In multi-region MPC deployments, the typical blast radius reduction achieved through isolation is ___% to ___%.
   A: 50%; 70%

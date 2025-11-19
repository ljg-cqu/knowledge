1. Q: The ___ protocol reduces threshold ECDSA signing to 4 rounds while fixing security vulnerabilities in GG20 through ___ range proofs in MtA share conversion.
   A: CGGMP21; zero-knowledge (ZK)

1. Q: For threshold Schnorr signatures on EdDSA curves like Solana, the ___ protocol offers ___-round signing without requiring Paillier encryption overhead.
   A: FROST; 2

1. Q: In a 2-of-3 MPC threshold scheme for wallet recovery, one key-share is stored in the mobile app's ___ (TEE), one on a backend ___ cluster, and one in encrypted ___ backup.
   A: secure enclave; HSM; cloud

1. Q: List the 6 categories of the STRIDE threat modeling framework.
   A: Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege

1. Q: The WSJF prioritization framework calculates score as (___ + ___ + ___) / Job Size.
   A: Business Value; Time Criticality; Risk Reduction

1. Q: Pre-signing in CGGMP21 can reduce online signing from 4 rounds to ___ round by generating signing shares offline before knowing the ___.
   A: 1; transaction message

1. Q: For MPC wallet signing latency targets, mobile signing should be < ___ ms and web signing should be < ___ ms.
   A: 800-1000; 1200-1500

1. Q: The three main MPC signing bottlenecks on mobile devices are: ___, ___, and ___ overhead.
   A: elliptic curve operations (cryptographic computation); network latency (multi-party coordination); serialization/deserialization

1. Q: To prevent malicious co-signers from extracting keys, CGGMP21 includes ___ ___ proofs to validate Paillier ciphertexts and ___ schemes to prevent adaptive input changes.
   A: zero-knowledge range; commitment

1. Q: In multi-chain MPC wallet architecture, the three abstraction layers are: ___ Abstraction Layer, ___ Scheme Adapter, and ___ Client Abstraction.
   A: Chain; Signature; RPC

1. Q: List the 4 Team Topologies interaction modes.
   A: Collaboration, X-as-a-Service, Facilitation, (and Stream-Aligned as team type)

1. Q: SOC 2 Type II breach notification requires notification to regulators within ___ hours, and GDPR Article 33 mandates breach notification within ___ hours.
   A: 72; 72

1. Q: The four DORA metrics for measuring DevOps performance are: ___, ___, ___, and ___.
   A: Deployment frequency; Lead time for changes; Change failure rate; Time to restore service

1. Q: HSM (Hardware Security Module) should meet FIPS 140-2 Level ___ or higher to ensure keys never leave tamper-proof boundaries.
   A: 3

1. Q: For social recovery in MPC wallets, a typical guardian threshold is ___-of-___, balancing availability (need ___ guardians) against security (tolerates ___ compromised).
   A: 5; 9; 5; 4

1. Q: The three signature schemes commonly used in multi-chain MPC wallets are: ___ (Bitcoin/Ethereum), ___ (Solana/Schnorr), and ___ (emerging chains like Aptos).
   A: ECDSA; EdDSA; BLS

1. Q: ADR stands for ___ ___ ___, used to document critical design choices and their trade-offs.
   A: Architecture Decision Record

1. Q: In MPC protocol security, the difference between GG18 and GG20 is that GG20 has ___ rounds but contains a security vulnerability that CGGMP21 fixes with ___.
   A: fewer (reduced from 9); additional ZK proofs

1. Q: The three main cryptographic building blocks in CGGMP21 threshold ECDSA are: ___ homomorphic encryption, ___ ___ proofs, and ___ protocols.
   A: Paillier; zero-knowledge range; DKG (Distributed Key Generation)

1. Q: For MPC wallet enterprise compliance, the key rotation policy typically requires refreshing key-shares every ___ days to meet SOC 2 audit requirements.
   A: 90

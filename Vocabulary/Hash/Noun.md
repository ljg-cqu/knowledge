1. **Noun**: hash (C/U)
   **Meaning**: 
   - (C) The fixed-size output value produced by a hash function
   - (U) The process of applying a hash function to data
   
   **Synonyms**: digest, checksum, hash value, hash code, fingerprint
   
   **Antonyms**: plaintext, original, source data
   
   **When to Use**: Technical discussions about cryptography, data structures, file verification, password storage
   
   **When NOT to Use**: When referring to the hash function itself (use "hash function" instead)
   
   **Common Phrases**: 
   - compute a hash
   - generate a hash
   - hash value
   - hash output
   - hash collision
   
   **Root Analysis**: hash (chop, mix up) - from culinary term
   
   **Etymology**: French hacher (to chop) → hash (1650s culinary) → hash (1970s computing)
   
   **Examples [Casual]**: 
   - The file's hash is different, so something changed.
   - Just run a hash on it to check integrity.
   
   **Examples [Formal]**: 
   - The SHA-256 hash serves as a unique identifier for the document.
   - Digital signatures rely on cryptographic hashes to ensure message integrity.

1. **Noun**: algorithm (C)
   **Meaning**: 
   - A step-by-step procedure or formula for solving a problem or performing a computation
   
   **Synonyms**: procedure, method, process, protocol, technique
   
   **Antonyms**: randomness, chaos, improvisation
   
   **When to Use**: Computer science, mathematics, technical documentation, describing systematic processes
   
   **When NOT to Use**: When referring to informal or ad-hoc procedures
   
   **Common Phrases**: 
   - hash algorithm
   - cryptographic algorithm
   - sorting algorithm
   - efficient algorithm
   - algorithm complexity
   
   **Root Analysis**: al (from name Al-Khwarizmi) + rithm (number)
   
   **Etymology**: Medieval Latin algorismus (from Al-Khwarizmi, Persian mathematician, 9th century) → algorithm (1690s)
   
   **Examples [Casual]**: 
   - We're using the SHA-256 algorithm for all our hashing.
   - This algorithm is way faster than the old one.
   
   **Examples [Formal]**: 
   - The algorithm exhibits O(n) time complexity for linear input processing.
   - Modern cryptographic algorithms must resist both classical and quantum computational attacks.

1. **Noun**: collision (C)
   **Meaning**: 
   - An instance where two different inputs produce the same hash output
   
   **Synonyms**: clash, conflict, duplicate, hash conflict
   
   **Antonyms**: uniqueness, distinctness, collision-free result
   
   **When to Use**: Security analysis, hash table discussions, cryptographic vulnerabilities, performance analysis
   
   **When NOT to Use**: When discussing other types of errors or conflicts unrelated to hashing
   
   **Common Phrases**: 
   - hash collision
   - collision attack
   - collision resistance
   - collision probability
   - collision detection
   
   **Root Analysis**: col (together) + lision (striking)
   
   **Etymology**: Latin collidere (to strike together) → collision (15th century)
   
   **Examples [Casual]**: 
   - We found a collision in the old MD5 hashes—time to upgrade.
   - Collisions are super rare with good hash functions.
   
   **Examples [Formal]**: 
   - The collision demonstrates a fundamental weakness in the hash algorithm's design.
   - Collision probability increases according to the birthday paradox in cryptographic applications.

1. **Noun**: digest (C)
   **Meaning**: 
   - A fixed-size value produced by a hash function that serves as a compact representation of input data
   
   **Synonyms**: hash, hash value, hash output, message digest, checksum
   
   **Antonyms**: original message, input data, plaintext
   
   **When to Use**: Cryptography, formal technical documentation, discussing hash function outputs
   
   **When NOT to Use**: Casual contexts where "hash" is more commonly understood
   
   **Common Phrases**: 
   - message digest
   - hash digest
   - cryptographic digest
   - digest value
   - compute a digest
   
   **Root Analysis**: di (apart) + gest (carry)
   
   **Etymology**: Latin digestus (arranged, distributed) → digest (14th century) → message digest (1990s computing)
   
   **Examples [Casual]**: 
   - The digest is just the hash output you get at the end.
   - Compare the digests to verify the files match.
   
   **Examples [Formal]**: 
   - The message digest algorithm produces a 128-bit output regardless of input length.
   - Cryptographic digests ensure data integrity through one-way transformations.

1. **Noun**: integrity (U)
   **Meaning**: 
   - The state of data being complete, unmodified, and accurate; freedom from corruption or unauthorized alteration
   
   **Synonyms**: authenticity, correctness, completeness, validity, wholeness
   
   **Antonyms**: corruption, tampering, modification, alteration
   
   **When to Use**: Security contexts, data verification, quality assurance, blockchain, database management
   
   **When NOT to Use**: When discussing confidentiality (different security property) or availability
   
   **Common Phrases**: 
   - data integrity
   - integrity check
   - integrity verification
   - maintain integrity
   - ensure integrity
   
   **Root Analysis**: integer (whole, complete) + ity (state of)
   
   **Etymology**: Latin integritas (soundness, wholeness) → integrity (14th century)
   
   **Examples [Casual]**: 
   - Hash functions help maintain data integrity by detecting any changes.
   - We need to check the file's integrity before using it.
   
   **Examples [Formal]**: 
   - Cryptographic hash functions provide integrity assurance through tamper-evident mechanisms.
   - The blockchain protocol ensures transaction integrity via hash-based immutability.

1. **Noun**: salt (C/U)
   **Meaning**: 
   - (C/U) Random data added to input before hashing to ensure identical inputs produce different hash outputs
   
   **Synonyms**: random value, cryptographic salt, salt value, nonce (in some contexts)
   
   **Antonyms**: unsalted hash, plain hash
   
   **When to Use**: Password security, authentication, preventing rainbow table attacks, security best practices
   
   **When NOT to Use**: When discussing encryption keys or initialization vectors (different concepts)
   
   **Common Phrases**: 
   - add salt
   - salt value
   - random salt
   - salt and hash
   - salted password
   
   **Root Analysis**: salt (from culinary seasoning metaphor)
   
   **Etymology**: Old English sealt (mineral) → salt (metaphorical use in cryptography, 1970s Unix)
   
   **Examples [Casual]**: 
   - Always add a random salt before hashing passwords.
   - Salt makes rainbow tables useless for cracking passwords.
   
   **Examples [Formal]**: 
   - The authentication system employs cryptographically random salts to mitigate precomputation attacks.
   - Salt values expand the effective key space, rendering rainbow table attacks computationally infeasible.

1. **Noun**: verification (U/C)
   **Meaning**: 
   - The process of confirming that data has not been altered by comparing hash values
   
   **Synonyms**: validation, confirmation, authentication, checking, attestation
   
   **Antonyms**: corruption, falsification, tampering
   
   **When to Use**: Security procedures, quality assurance, data integrity checking, authentication systems
   
   **When NOT to Use**: When discussing encryption or confidentiality rather than integrity
   
   **Common Phrases**: 
   - hash verification
   - integrity verification
   - verification process
   - verification check
   - verification mechanism
   
   **Root Analysis**: veri (true) + fication (making)
   
   **Etymology**: Latin verus (true) + facere (to make) → verification (17th century)
   
   **Examples [Casual]**: 
   - The verification failed, so the file might be corrupted.
   - Hash verification is super quick—just compare the values.
   
   **Examples [Formal]**: 
   - Hash-based verification mechanisms detect unauthorized modifications with high probability.
   - The verification protocol employs cryptographic hash functions to ensure data authenticity.

1. **Noun**: checksum (C)
   **Meaning**: 
   - A value computed from data to detect errors or verify integrity, typically using simpler algorithms than cryptographic hashes
   
   **Synonyms**: check value, hash, error detection code, verification code
   
   **Antonyms**: original data, unverified data
   
   **When to Use**: Error detection, data transmission, file integrity checks, non-security contexts
   
   **When NOT to Use**: When strong cryptographic security is required (use "cryptographic hash" instead)
   
   **Common Phrases**: 
   - compute checksum
   - checksum verification
   - checksum algorithm
   - validate checksum
   - checksum mismatch
   
   **Root Analysis**: check (verify) + sum (total)
   
   **Etymology**: check + sum → checksum (1940s computing)
   
   **Examples [Casual]**: 
   - The file checksum doesn't match, so the download might be corrupted.
   - Run a quick checksum to see if anything changed.
   
   **Examples [Formal]**: 
   - Checksums provide efficient error detection for network packet transmission.
   - While checksums detect accidental corruption, cryptographic hashes prevent intentional tampering.

1. **Noun**: cryptography (U)
   **Meaning**: 
   - The practice and study of techniques for secure communication and data protection through encoding
   
   **Synonyms**: encryption science, code-making, cipher systems, secure communication
   
   **Antonyms**: plaintext communication, open transmission
   
   **When to Use**: Security discussions, academic contexts, explaining security mechanisms, professional cybersecurity
   
   **When NOT to Use**: When discussing specific hash functions (be more specific) or non-security computing
   
   **Common Phrases**: 
   - modern cryptography
   - applied cryptography
   - cryptography and security
   - cryptographic techniques
   - cryptography principles
   
   **Root Analysis**: crypto (hidden, secret) + graphy (writing)
   
   **Etymology**: Greek kryptos (hidden) + graphein (to write) → cryptography (1650s)
   
   **Examples [Casual]**: 
   - Hash functions are a big part of modern cryptography.
   - Learning cryptography helps you understand why we hash passwords.
   
   **Examples [Formal]**: 
   - Cryptographic hash functions constitute fundamental primitives in modern cryptography.
   - The field of cryptography encompasses symmetric encryption, asymmetric encryption, and hash functions.

1. **Noun**: blockchain (C)
   **Meaning**: 
   - A distributed ledger system that uses cryptographic hashing to link blocks of data in an immutable chain
   
   **Synonyms**: distributed ledger, hash chain, decentralized ledger
   
   **Antonyms**: centralized database, single-server system
   
   **When to Use**: Cryptocurrency, distributed systems, immutable records, consensus mechanisms
   
   **When NOT to Use**: When discussing traditional databases or non-distributed systems
   
   **Common Phrases**: 
   - blockchain technology
   - blockchain network
   - blockchain ledger
   - blockchain hash
   - blockchain consensus
   
   **Root Analysis**: block (data unit) + chain (linked sequence)
   
   **Etymology**: block + chain → blockchain (coined 2008, popularized by Bitcoin)
   
   **Examples [Casual]**: 
   - Blockchain uses hash functions to link all the blocks together.
   - Each block in the blockchain contains the previous block's hash.
   
   **Examples [Formal]**: 
   - Blockchain technology employs cryptographic hash functions to ensure immutability and tamper-evidence.
   - The blockchain's security model relies on hash-based proof-of-work consensus mechanisms.

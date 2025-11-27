# Blockchain Vocabulary: Verbs

1. **Verb**: mine (transitive/intransitive)
   **Meaning**: 
   - To validate transactions and create new blocks in a proof-of-work blockchain by solving computational puzzles
   - *(Technical)* To perform hash computations searching for a nonce that produces a block hash meeting difficulty requirements
   
   **Synonyms**: validate (in PoW context), compute hashes, solve blocks, generate blocks, process transactions
   
   **Antonyms**: stake (in PoS), passively observe, receive without work
   
   **When to Use**: When discussing proof-of-work blockchains like Bitcoin, block creation, or computational puzzle-solving. Specific to PoW consensus mechanisms.
   
   **When NOT to Use**: Don't use for proof-of-stake validation or other non-PoW consensus. Avoid when discussing traditional mining or data mining.
   
   **Common Phrases**: 
   - mine Bitcoin
   - mine a block
   - mine cryptocurrency
   - start mining
   - mining difficulty
   
   **Root Analysis**: Old French "mine" (ore deposit) + English verb usage
   
   **Etymology**: Latin "mina" (ore vein) → Old French "mine" → English "mine" (extract minerals, 1300s) → Blockchain metaphor (2009) for computational work extracting digital value
   
   **Examples [Casual]**: 
   - It's not profitable to mine Bitcoin with regular computers anymore.
   - Miners are competing to mine the next block and earn the reward.
   
   **Examples [Formal]**: 
   - Participants mine blocks by computing SHA-256 hashes until finding valid proof-of-work solutions.
   - Economic incentives to mine align computational expenditure with network security maintenance.

1. **Verb**: stake (transitive)
   **Meaning**: 
   - To lock up cryptocurrency as collateral to participate in proof-of-stake validation and earn rewards
   - *(Technical)* To deposit tokens in a staking contract or validator node to participate in consensus and block production
   
   **Synonyms**: deposit, lock up, bond, commit, pledge
   
   **Antonyms**: unstake, withdraw, remove, liquidate
   
   **When to Use**: When discussing proof-of-stake blockchains, validator participation, or earning staking rewards. Specific to PoS consensus mechanisms.
   
   **When NOT to Use**: Don't use for proof-of-work mining or liquidity provision. Avoid confusing with gambling stakes or traditional investment staking.
   
   **Common Phrases**: 
   - stake tokens
   - stake ETH
   - stake and earn
   - staking rewards
   - minimum stake
   
   **Root Analysis**: Old English "staca" (post/stick) → "stake" (wager/risk)
   
   **Etymology**: Old English "staca" → Middle English "stake" (wager, 1530s) → Cryptocurrency context (2012+) for depositing tokens as validator collateral
   
   **Examples [Casual]**: 
   - You can stake your ETH to earn passive income and help secure the network.
   - I'm staking 32 ETH to run a validator node.
   
   **Examples [Formal]**: 
   - Validators stake capital as economic security to disincentivize malicious behavior through slashing mechanisms.
   - Staking derivatives enable liquid staking while capital remains locked in consensus protocols.

1. **Verb**: validate (transitive)
   **Meaning**: 
   - To verify that transactions or blocks conform to blockchain protocol rules
   - *(Technical)* To check cryptographic signatures, transaction formats, and consensus rules before accepting state changes
   
   **Synonyms**: verify, confirm, authenticate, check, attest
   
   **Antonyms**: reject, invalidate, deny, falsify
   
   **When to Use**: When discussing transaction verification, consensus participation, or protocol enforcement. General term applicable to all blockchain types.
   
   **When NOT to Use**: Don't confuse with "mining" (specific PoW action) or "staking" (specific PoS action). Avoid using generically for non-blockchain verification.
   
   **Common Phrases**: 
   - validate transactions
   - validate blocks
   - validator node
   - validation rules
   - transaction validation
   
   **Root Analysis**: Latin "validus" (strong) + -ate (verb suffix)
   
   **Etymology**: Latin "validus" (strong/effective) → Medieval Latin "validare" → English "validate" (1648) → Blockchain consensus context (2008+)
   
   **Examples [Casual]**: 
   - Nodes validate every transaction to make sure it follows the rules.
   - Your transaction won't go through until enough validators confirm it.
   
   **Examples [Formal]**: 
   - Full nodes validate all transactions independently according to consensus protocol specifications.
   - Byzantine fault-tolerant validators require supermajority agreement to validate state transitions.

1. **Verb**: fork (intransitive/transitive)
   **Meaning**: 
   - To diverge from the main blockchain protocol or history, creating a separate chain
   - *(Technical)* To introduce protocol changes that create backward-incompatible rules (hard fork) or tightened restrictions (soft fork)
   
   **Synonyms**: split, diverge, branch, separate, divide
   
   **Antonyms**: merge, converge, unify, consolidate
   
   **When to Use**: When discussing protocol upgrades, contentious changes, or blockchain splits. Important for understanding governance and evolution.
   
   **When NOT to Use**: Don't use for routine software updates that don't change protocol. Avoid confusing with repository forks in software development.
   
   **Common Phrases**: 
   - fork the chain
   - fork Bitcoin
   - hard fork vs soft fork
   - fork the protocol
   - forked network
   
   **Root Analysis**: Latin "furca" (forked instrument) → verb usage
   
   **Etymology**: Latin "furca" → Old English "forca" → Verb "to fork" (divide, 1600s) → Software development (1980s) → Blockchain context (2013+)
   
   **Examples [Casual]**: 
   - The community decided to fork the blockchain after the controversial decision.
   - Ethereum Classic forked from Ethereum in 2016 after the DAO hack.
   
   **Examples [Formal]**: 
   - Hard forks require coordinated upgrades across all network participants to avoid chain splits.
   - The protocol successfully forked to implement proposed consensus mechanism improvements.

1. **Verb**: broadcast (transitive)
   **Meaning**: 
   - To transmit a transaction or block to all connected nodes in the network
   - *(Technical)* To propagate messages through peer-to-peer network gossip protocols for network-wide dissemination
   
   **Synonyms**: transmit, propagate, disseminate, send, relay
   
   **Antonyms**: receive, withhold, keep private, suppress
   
   **When to Use**: When discussing transaction submission, block propagation, or network communication. Fundamental to understanding blockchain operation.
   
   **When NOT to Use**: Don't use for direct peer-to-peer messaging or point-to-point communication. Avoid when discussing private or encrypted channels.
   
   **Common Phrases**: 
   - broadcast a transaction
   - broadcast to the network
   - transaction broadcast
   - broadcast the block
   - successfully broadcast
   
   **Root Analysis**: broad (wide) + cast (throw/send)
   
   **Etymology**: "Broad" + "cast" (scatter widely) → Radio/TV broadcasting (1921) → Computer networking (1970s) → Blockchain peer-to-peer context (2008+)
   
   **Examples [Casual]**: 
   - When you send Bitcoin, your wallet broadcasts the transaction to the network.
   - The miner broadcasts the new block to all connected nodes.
   
   **Examples [Formal]**: 
   - Transactions are broadcast through gossip protocols ensuring eventual propagation to all network participants.
   - Block propagation delays affect network synchronization and potential fork probability.

1. **Verb**: confirm (transitive)
   **Meaning**: 
   - To include a transaction in a block and add subsequent blocks on top, increasing finality confidence
   - *(Technical)* To achieve sufficient proof-of-work or consensus weight behind a transaction to consider it settled
   
   **Synonyms**: finalize, settle, validate, secure, establish
   
   **Antonyms**: reverse, reject, orphan, invalidate
   
   **When to Use**: When discussing transaction finality, settlement times, or confirmation requirements. Essential for understanding transaction security.
   
   **When NOT to Use**: Don't confuse with initial validation (confirming happens after validation). Avoid implying absolute finality (confirmations are probabilistic in PoW).
   
   **Common Phrases**: 
   - confirm a transaction
   - six confirmations
   - confirmation time
   - wait for confirmation
   - block confirmation
   
   **Root Analysis**: con- (together/thoroughly) + firm (strong) + -ate
   
   **Etymology**: Latin "confirmare" (make firm) → Old French "confermer" → English "confirm" (1250s) → Blockchain finality context (2008+)
   
   **Examples [Casual]**: 
   - Wait for at least six confirmations before considering the payment final.
   - My transaction has three confirmations so far.
   
   **Examples [Formal]**: 
   - Transaction finality increases exponentially with confirmation depth in proof-of-work blockchains.
   - Merchants typically require multiple confirmations to mitigate double-spend attack risks.

1. **Verb**: deploy (transitive)
   **Meaning**: 
   - To publish and activate a smart contract on a blockchain network
   - *(Technical)* To submit contract bytecode in a transaction that creates a new contract address and initializes state
   
   **Synonyms**: publish, launch, release, create, instantiate
   
   **Antonyms**: destroy, deactivate, remove, retire
   
   **When to Use**: When discussing smart contract creation, dApp launches, or protocol deployments. Specific to programmable blockchains.
   
   **When NOT to Use**: Don't use for simple transactions or token transfers. Avoid when discussing military/traditional software deployment contexts.
   
   **Common Phrases**: 
   - deploy a contract
   - deploy to mainnet
   - contract deployment
   - deploy smart contract
   - deployment transaction
   
   **Root Analysis**: Old French "desploiier" (unfold/display)
   
   **Etymology**: Latin "displicare" (unfold) → Old French "desploiier" → English "deploy" (1786 military) → Software deployment (1990s) → Smart contract context (2015+)
   
   **Examples [Casual]**: 
   - We're ready to deploy the smart contract to Ethereum mainnet.
   - Deploying costs gas because you're creating new data on the blockchain.
   
   **Examples [Formal]**: 
   - Smart contracts are deployed through constructor transactions that initialize immutable bytecode.
   - Deployment verification ensures on-chain bytecode matches audited source code.

1. **Verb**: mint (transitive)
   **Meaning**: 
   - To create new tokens or NFTs according to contract rules
   - *(Technical)* To increase token supply by creating new units through predefined minting functions or protocol inflation
   
   **Synonyms**: create, issue, generate, produce, coin
   
   **Antonyms**: burn, destroy, remove from circulation, deflationary action
   
   **When to Use**: When discussing token creation, NFT generation, or supply increases. Common in DeFi and NFT contexts.
   
   **When NOT to Use**: Don't use for proof-of-work mining (different process). Avoid when tokens are transferred rather than created.
   
   **Common Phrases**: 
   - mint tokens
   - mint an NFT
   - minting function
   - minting ceremony
   - newly minted
   
   **Root Analysis**: Old English "mynet" (coin)
   
   **Etymology**: Latin "moneta" (mint/money) → Old English "mynet" → "mint" (create coins, 1200s) → Cryptocurrency token creation (2017+)
   
   **Examples [Casual]**: 
   - Artists can mint their artwork as NFTs on platforms like OpenSea.
   - The protocol mints new tokens as staking rewards.
   
   **Examples [Formal]**: 
   - Token minting follows ERC-20 standard functions with appropriate access controls and supply caps.
   - Controlled minting schedules balance inflation incentives with long-term value preservation.

1. **Verb**: burn (transitive)
   **Meaning**: 
   - To permanently remove tokens from circulation by sending them to an unspendable address
   - *(Technical)* To destroy token supply through explicit burn functions or transfers to addresses without known private keys
   
   **Synonyms**: destroy, remove from circulation, eliminate, deflationary action
   
   **Antonyms**: mint, create, issue, increase supply
   
   **When to Use**: When discussing deflationary tokenomics, fee mechanisms, or supply reduction. Important in understanding token economics.
   
   **When NOT to Use**: Don't use for temporary locking (use "lock" or "stake"). Avoid when tokens are transferred rather than destroyed.
   
   **Common Phrases**: 
   - burn tokens
   - token burn
   - burn mechanism
   - burn address
   - deflationary burn
   
   **Root Analysis**: Old English "bærnan" (consume by fire)
   
   **Etymology**: Old English "bærnan" (consume by fire) → "burn" → Cryptocurrency metaphor (2017+) for permanently destroying tokens
   
   **Examples [Casual]**: 
   - The project burns a portion of transaction fees to make the token deflationary.
   - Burning tokens reduces supply and can increase scarcity.
   
   **Examples [Formal]**: 
   - EIP-1559 implements a fee-burning mechanism that permanently removes ETH from circulation.
   - Token burn events create deflationary pressure by reducing total supply without redemption possibility.

1. **Verb**: swap (transitive)
   **Meaning**: 
   - To exchange one cryptocurrency or token for another, typically through a decentralized exchange
   - *(Technical)* To execute an atomic token exchange via automated market makers or order books
   
   **Synonyms**: exchange, trade, convert, switch, transfer
   
   **Antonyms**: hold, keep, maintain position
   
   **When to Use**: When discussing DeFi trading, token exchanges, or liquidity pools. Common in decentralized exchange contexts.
   
   **When NOT to Use**: Don't use for traditional exchange trading (use "trade"). Avoid when discussing non-atomic or custodial exchanges.
   
   **Common Phrases**: 
   - swap tokens
   - token swap
   - swap on Uniswap
   - atomic swap
   - cross-chain swap
   
   **Root Analysis**: Middle English "swappen" (strike/exchange)
   
   **Etymology**: Middle English "swappen" (strike hands in agreement) → "swap" (exchange, 1590s) → Cryptocurrency DEX context (2018+) via Uniswap
   
   **Examples [Casual]**: 
   - You can swap ETH for USDC directly on Uniswap without an intermediary.
   - I swapped my Bitcoin for Ethereum using a decentralized exchange.
   
   **Examples [Formal]**: 
   - Automated market makers enable permissionless token swaps through constant product formulas.
   - Cross-chain atomic swaps facilitate trustless exchange between different blockchain networks.

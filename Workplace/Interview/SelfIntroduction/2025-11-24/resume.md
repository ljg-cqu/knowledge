<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Jigao Luo (Zealy) · Senior Technical Resume</title>
    <style>
        /* Base Typography and Colors - v2 */
        :root {
            --primary: #2c5282;       /* Deep blue */
            --primary-light: #4299e1; /* Lighter blue */
            --secondary: #38a169;     /* Green accent */
            --text-dark: #2d3748;     /* Dark gray for main text */
            --text-medium: #4a5568;   /* Medium gray for secondary text */
            --text-light: #718096;    /* Light gray for tertiary text */
            --bg-main: #f8fafc;       /* Very light blue-gray background */
            --bg-alt: #edf2f7;        /* Slightly darker background for contrast */
            --border-light: #e2e8f0;  /* Light border color */
            --border-color: #CBD5E0;  /* Border color for resume container */
            --spacing-unit: 0.5rem;   /* Base spacing unit */
        }
        
        body {
            font-family: "Segoe UI", "Microsoft YaHei", "Hiragino Sans GB", sans-serif;
            line-height: 1.4;
            color: var(--text-dark);
            width: 210mm; /* Exact A4 width */
            min-height: 297mm; /* Exact A4 height */
            margin: 0 auto;
            padding: 0;
            background-color: var(--bg-main);
            font-size: 14px;
            letter-spacing: 0;
            box-sizing: border-box;
        }
        
        .resume-container {
            position: relative;
            border: 1px solid var(--border-color);
            padding: 8mm 15mm 15mm 15mm; /* Optimized top padding for A4 printing */
            background-color: white;
            box-shadow: none; /* Remove shadow to ensure consistency */
            min-height: auto; /* Allow content to determine height */
            box-sizing: border-box;
            width: 210mm; /* Exact A4 width */
            margin: 0 auto;
            overflow: visible; /* Allow content to flow to next page */
        }
        
        /* Print-specific styles */
        @media print {
            body {
                width: 210mm; /* Exact A4 width */
                height: auto; /* Allow content to determine height */
                margin: 0;
                padding: 0;
                background-color: white;
                print-color-adjust: exact;
                -webkit-print-color-adjust: exact;
            }
            
            .resume-container {
                border: none;
                padding: 5mm 15mm 5mm 15mm; /* Reduced top and bottom padding for more compact layout */
                box-shadow: none !important;
                height: auto; /* Allow content to determine height */
                width: 210mm; /* Exact A4 width */
                margin: 0;
                overflow: visible; /* Allow content to flow to next page */
                -webkit-box-shadow: none !important;
            }
            
            /* Ensure job titles and positions display properly when printed */
            .job-title, .job-position {
                white-space: normal;
                display: block;
                width: 100%;
            }
            
            /* Ensure containers display as blocks when printed */
            .job-header, .edu-entry {
                display: block;
            }
            
            /* Adjust font size slightly for print if needed */
            html, body {
                font-size: 13px; /* Slightly smaller font for print to ensure fit */
            }
            
            /* Removed pseudo-element style */
            
            @page {
                size: 210mm 297mm; /* Exact A4 dimensions */
                margin: 15mm 0 20mm 0; /* Default margins for subsequent pages */
                padding: 0;
            }
            
            @page :first {
                margin: 5mm 0 20mm 0; /* Minimal top margin for first page, same bottom margin */
            }
            
            /* Control what appears in the header/footer */
            @page {
                /* Hide URL and date in header */
                @top-left { content: ""; }
                @top-center { content: ""; }
                @top-right { content: ""; }
                
                /* Keep only page numbers in footer */
                @bottom-left { content: ""; }
                @bottom-center { content: counter(page); }
                @bottom-right { content: ""; }
            }
            
            .second-last-project, .last-project {
                page-break-before: avoid !important;
                page-break-inside: avoid !important;
                break-inside: avoid !important;
                -webkit-column-break-inside: avoid !important;
            }
            
            .second-last-project {
                margin-bottom: calc(var(--spacing-unit) * 1.5);
            }
        }
        
        /* Removed the pseudo-element that was causing shadow inconsistency */
        
        /* Headings */
        h1 {
            text-align: center;
            color: var(--primary);
            margin-bottom: calc(var(--spacing-unit) * 4);
            font-size: 28px;
            position: relative;
            padding-bottom: calc(var(--spacing-unit) * 1.5);
            letter-spacing: 0.05em;
        }
        
        h1::after {
            content: "";
            position: absolute;
            bottom: 0;
            left: 50%;
            transform: translateX(-50%);
            width: 60%;
            height: 3px;
            background: linear-gradient(to right, rgba(44, 82, 130, 0.1), rgba(44, 82, 130, 1), rgba(44, 82, 130, 0.1));
        }
        
        h2 {
            color: var(--primary);
            border-bottom: 2px solid var(--primary);
            padding-bottom: calc(var(--spacing-unit) * 0.5);
            margin-top: calc(var(--spacing-unit) * 2);
            margin-bottom: calc(var(--spacing-unit) * 1.5);
            font-size: 20px;
            letter-spacing: 0.03em;
            position: relative;
            page-break-after: avoid;
        }
        
        h2::after {
            content: "";
            position: absolute;
            bottom: -5px;
            left: 0;
            width: 100%;
            border-bottom: 1px solid var(--border-light);
        }
        
        h3 {
            color: var(--primary);
            margin-top: calc(var(--spacing-unit) * 1.5);
            margin-bottom: calc(var(--spacing-unit) * 1);
            font-size: 17px;
            page-break-after: avoid;
        }
        
        /* Prevent awkward page breaks */
        h2, h3, h4, .job-header, .project-section, .open-source-header {
            page-break-after: avoid;
        }
        
        .job-item, .project-section, .open-source, ul, li {
            page-break-inside: avoid;
        }
        
        .second-last-project, .last-project {
            page-break-before: avoid !important;
            page-break-inside: avoid !important;
            break-inside: avoid !important;
            -webkit-column-break-inside: avoid !important;
        }
        
        .second-last-project {
            margin-bottom: calc(var(--spacing-unit) * 1.5);
        }
        
        /* Print button */
        .print-button {
            position: fixed;
            top: 20px;
            right: 20px;
            background-color: var(--primary);
            color: white;
            padding: 8px 16px;
            border-radius: 4px;
            cursor: pointer;
            font-weight: 500;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            z-index: 1000;
            transition: background-color 0.2s;
        }
        
        .print-button:hover {
            background-color: var(--primary-light);
        }
        
        @media print {
            .print-button {
                display: none;
            }
        }
        
        /* Personal Information Section */
        .info-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: calc(var(--spacing-unit) * 0.5);
            margin-bottom: calc(var(--spacing-unit) * 1.5);
        }
        
        .info-item {
            margin: calc(var(--spacing-unit) * 0.5) 0;
        }
        
        .job-objective {
            margin-top: calc(var(--spacing-unit) * 0.25);
            font-weight: 500;
        }
        
        .info-label {
            font-weight: 600;
            display: inline-block;
            min-width: 70px;
            color: var(--primary);
        }
        
        /* Work Experience Section */
        .job-title {
            font-weight: 600;
            color: var(--primary);
            display: block;
            white-space: normal;
            letter-spacing: 0;
            width: 100%;
            word-break: break-word;
            margin-bottom: calc(var(--spacing-unit) * 0.25);
        }
        
        .job-company {
            font-weight: 600;
        }
        
        .job-position {
            color: var(--text-medium);
            display: block;
            font-weight: 500;
            white-space: normal;
            font-size: 0.95em;
            width: 100%;
            word-break: break-word;
            margin-bottom: calc(var(--spacing-unit) * 0.5);
        }
        
        .job-item {
            margin-bottom: calc(var(--spacing-unit) * 1.5);
            padding-left: calc(var(--spacing-unit) * 1.5);
        }
        
        .job-header {
            margin-bottom: calc(var(--spacing-unit) * 1);
            width: 100%;
            box-sizing: border-box;
            padding-right: var(--spacing-unit);
            display: block; /* Changed to block for vertical layout */
        }
        
        .edu-entry {
            margin-bottom: var(--spacing-unit);
            width: 100%;
            box-sizing: border-box;
            padding-right: var(--spacing-unit);
            display: block; /* Changed to block for vertical layout */
        }
        
        .project-item {
            margin-left: calc(var(--spacing-unit) * 2);
            margin-bottom: calc(var(--spacing-unit) * 1.25);
            position: relative;
            max-width: calc(100% - var(--spacing-unit) * 2); /* Ensure content stays within margins */
            box-sizing: border-box;
        }
        
        .project-item > div:first-child {
            position: relative;
        }
        
        .project-item > div:first-child::before {
            content: "";
            position: absolute;
            left: -15px;
            top: 8px;
            width: 6px;
            height: 6px;
            border-radius: 50%;
            background-color: var(--secondary);
        }
        
        .tech-stack {
            color: var(--text-light);
            font-style: italic;
            margin-top: calc(var(--spacing-unit) * 0.5);
            margin-bottom: 0;
            font-size: 14px;
        }
        
        /* Skills Section */
        .contribution-title {
            font-weight: 600;
            margin-top: calc(var(--spacing-unit) * 2);
            color: var(--primary);
        }
        
        ul {
            margin-top: var(--spacing-unit);
            padding-left: calc(var(--spacing-unit) * 5);
            list-style-type: none;
        }
        
        li {
            margin-bottom: calc(var(--spacing-unit) * 1.5);
            position: relative;
        }
        
        li::before {
            content: "";
            position: absolute;
            left: -15px;
            top: 8px;
            width: 6px;
            height: 6px;
            border-radius: 50%;
            background-color: var(--secondary);
        }
        
        .skill-category {
            font-weight: 600;
            margin-top: calc(var(--spacing-unit) * 3);
            color: var(--primary);
        }
        
        .skill-item {
            margin-bottom: var(--spacing-unit);
        }
        
        .skill-name {
            font-weight: 600;
            color: var(--primary);
        }
        
        /* Open Source Section */
        .open-source {
            margin-bottom: calc(var(--spacing-unit) * 3);
            padding-left: calc(var(--spacing-unit) * 3);
        }
        
        .open-source-header {
            display: flex;
            align-items: center;
            flex-wrap: wrap;
            margin-bottom: var(--spacing-unit);
        }
        
        .open-source-title {
            font-weight: 600;
            color: var(--primary);
            margin-right: calc(var(--spacing-unit) * 4);
        }
        
        .open-source-link {
            color: var(--primary);
            text-decoration: none;
            transition: color 0.2s;
        }
        
        .open-source-link:hover {
            text-decoration: underline;
            color: var(--primary-light);
        }
        
        .open-source-desc {
            margin-left: calc(var(--spacing-unit) * 4);
            margin-top: var(--spacing-unit);
            color: var(--text-medium);
            position: relative;
        }
        
        .open-source-desc::before {
            content: "";
            position: absolute;
            left: -15px;
            top: 8px;
            width: 6px;
            height: 6px;
            border-radius: 50%;
            background-color: var(--secondary);
        }
        
        /* Project Experience Section */
        .project-date {
            color: var(--text-light);
            font-weight: normal;
            font-size: 0.9em;
            margin-left: var(--spacing-unit);
        }
        
        .project-section {
            margin-bottom: calc(var(--spacing-unit) * 1.5);
            padding-left: calc(var(--spacing-unit) * 1.5);
            border-left: 2px solid var(--border-light);
        }
        
        /* Ensure the last two projects stay together */
        .second-last-project + .last-project {
            page-break-before: avoid !important;
        }
        
        .contribution-list {
            margin-left: calc(var(--spacing-unit) * 2.5);
        }
        
        .contribution-item {
            margin-bottom: calc(var(--spacing-unit) * 1);
            position: relative;
        }
        
        .contribution-item::before {
            content: "";
            position: absolute;
            left: -15px;
            top: 8px;
            width: 6px;
            height: 6px;
            border-radius: 50%;
            background-color: var(--secondary);
        }
        
        .contribution-label {
            font-weight: 600;
            color: var(--primary);
        }
        
        /* Print Styles */
        @media print {
            body {
                background-color: white;
                padding: 0;
                max-width: 100%;
                font-size: 14px;
            }
            
            :root {
                --primary: #000;
                --primary-light: #333;
                --secondary: #555;
                --text-dark: #000;
                --text-medium: #333;
                --text-light: #555;
                --border-light: #ccc;
            }
            
            .project-section {
                border-left-color: #ccc;
            }
            
            .project-item > div:first-child::before,
            .contribution-item::before,
            .open-source-desc::before,
            li::before {
                background-color: #555;
            }
        }
    </style>
</head>
<body>
<div class="print-button" onclick="window.print()">Print PDF</div>
<div class="resume-container">
    <h1>Jigao Luo (Zealy) · Senior Technical Resume</h1>
    
    <h2>Personal Information</h2>
    <div class="info-grid">
        <div class="info-item"><span class="info-label">Name:</span> Jigao Luo (Zealy)</div>
        <div class="info-item"><span class="info-label">Gender:</span> Male</div>
        <div class="info-item"><span class="info-label">Phone:</span> +86 15215013094</div>
        <div class="info-item"><span class="info-label">Email:</span> ljg_cqu@126.com</div>
        <div class="info-item"><span class="info-label">Highest Degree:</span> Master's Degree</div>
        <div class="info-item"><span class="info-label">University:</span> Chongqing University</div>
        <div class="info-item job-objective" style="grid-column: 1 / 3;"><span class="info-label">Job Objective:</span> Blockchain Senior Engineer / Architect (Golang / Solidity / Rust) | Distributed Systems Development | Web3 / AI Integration</div>
    </div>
    
    <h2>Personal Strengths</h2>
    <ul>
        <li><span class="skill-name">Extensive Experience:</span>7+ years in blockchain industry, led multiple major projects through full lifecycle, managed DeFi protocols with million-dollar TVL</li>
        <li><span class="skill-name">Technical Breadth:</span>Experienced with multiple blockchain ecosystems, deployed across various networks, audited and fixed critical security vulnerabilities</li>
        <li><span class="skill-name">Technical Depth:</span>Deep understanding of blockchain fundamentals and consensus algorithms, solving core challenges in cross-chain communication and transaction consistency</li>
        <li><span class="skill-name">Leadership & Team Building:</span>Built and managed a technical team of over ten members, guided cross-national projects, significantly improved team efficiency</li>
        <li><span class="skill-name">Learning & Implementation:</span>Proficient in multiple programming languages, rapidly adapted to emerging technology domains, strong ability to solve complex technical challenges</li>
    </ul>
    
    <h2>Technical Capabilities</h2>
    <div class="skill-category">Blockchain & Web3</div>
    <ul>
        <li><span class="skill-name">Smart Contracts:</span>Developed multiple production-grade Solidity contracts, deployed across various blockchain networks, managing million-dollar TVL DeFi protocols</li>
        <li><span class="skill-name">Blockchain Development:</span>Cross-ecosystem experience in major platforms (EVM, Polkadot, Avalanche, Solana, Filecoin), optimized large-scale node clusters</li>
        <li><span class="skill-name">Web3 Backend Development:</span>Built decentralized application backend services, integrated multi-chain transaction systems, resolved nonce conflicts and transaction consistency issues</li>
    </ul>
    
    <div class="skill-category">AI & Innovative Technologies</div>
    <ul>
        <li><span class="skill-name">AI Integration:</span>Built distributed Agent systems using AWS Bedrock Claude, implemented automated trading strategy management, reduced manual intervention</li>
        <li><span class="skill-name">Cryptography Applications:</span>Designed MPC multi-party computation systems, implemented key splitting and multi-signature, securing substantial assets</li>
        <li><span class="skill-name">Storage Optimization:</span>Integrated IPFS distributed storage, improved Filecoin sealing efficiency, effectively reduced storage costs</li>
    </ul>
    
    <div class="skill-category">Technology Stack</div>
    <ul>
        <li><span class="skill-name">Programming Languages:</span>Extensive experience with Golang, Solidity, and Rust development, proficient in Python, Node.js, and SQL</li>
        <li><span class="skill-name">Development Tools:</span>Proficient with Foundry, Brownie testing frameworks, contributed to Gin framework OpenAPI extensions, experienced with OpenZeppelin</li>
        <li><span class="skill-name">Infrastructure:</span>Built Docker-based microservice architecture, deployed Prometheus monitoring systems, integrated Redis/Kafka messaging systems, managed PostgreSQL/MySQL databases</li>
    </ul>
    
    <h2>Management Skills</h2>
    <ul>
        <li><span class="skill-name">Team Management:</span>Built and led a technical team of over ten members, guided multiple cross-national projects, significantly improved team delivery speed and code quality</li>
        <li><span class="skill-name">Technical Decision-Making:</span>Led technology selection for multiple blockchain projects, evaluated high-TPS and specialized chain solutions, provided architecture support for million-dollar TVL projects</li>
        <li><span class="skill-name">International Collaboration:</span>Coordinated multiple cross-national teams (Singapore, US, Europe), authored numerous English technical documents and whitepapers (<a href="https://zealy.site" class="open-source-link">zealy.site</a>)</li>
        <li><span class="skill-name">Project Management:</span>Managed multiple parallel development projects, maintained high on-time delivery rate, successfully advanced several projects from concept to production</li>
    </ul>
    
    <h2>Open Source Contributions</h2>
    
    <div class="open-source">
        <div class="open-source-header">
            <span class="open-source-title">Bedrock IOTX Liquid Staking</span>
            <a href="https://github.com/RockX-SG/uniiotx" class="open-source-link">(https://github.com/RockX-SG/uniiotx)</a>
        </div>
        <div class="open-source-desc">Responsible for smart contract development, design documentation and whitepaper writing (GitHub username: Zealy-Rockx)</div>
    </div>
    
    <div class="open-source">
        <div class="open-source-header">
            <span class="open-source-title">Bedrock BTC Restaking</span>
            <a href="https://github.com/Bedrock-Technology/uniBTC" class="open-source-link">(https://github.com/Bedrock-Technology/uniBTC)</a>
        </div>
        <div class="open-source-desc">Participated in initial core code development and refactoring work (GitHub username: Trisome-Bedrock)</div>
    </div>
    
    <div class="open-source">
        <div class="open-source-header">
            <span class="open-source-title">Bedrock-DAO</span>
            <a href="https://github.com/Bedrock-Technology/bedrock-dao" class="open-source-link">(https://github.com/Bedrock-Technology/bedrock-dao)</a>
        </div>
        <div class="open-source-desc">Responsible for code review and testing, submitted multiple bug fixes and optimization suggestions</div>
    </div>
    
    <div class="open-source">
        <div class="open-source-header">
            <span class="open-source-title">Bedrock ETH Liquid Staking</span>
            <a href="https://github.com/RockX-SG/stake" class="open-source-link">(https://github.com/RockX-SG/stake)</a>
        </div>
        <div class="open-source-desc">Participated in code review, submitted bug fixes and optimization suggestions</div>
    </div>
    
    <h2>Work Experience</h2>
    
    <div class="job-item">
        <div class="job-header">
            <span class="job-title">2025.07-2025.08　Collaborative Project</span>
            <span class="job-position">(Blockchain Architect / Technical Consultant / Senior Developer)</span>
        </div>
        <div class="project-item">
            <div>⑩ Developed AIW3 Backend (Solana-DeFi and AI Agent platform), designed distributed Agent system</div>
            <div class="tech-stack">Tech Stack: Rust, Solana, AWS Bedrock Claude, Node.js, Kafka, IPFS</div>
        </div>
    </div>
    
    <div class="job-item">
        <div class="job-header">
            <span class="job-title">2022.04-2024.10　Chengdu Artest Technology Co., Ltd.</span>
            <span class="job-position">(Senior Backend Developer / Smart Contract Senior Engineer / Technical Mentor)</span>
        </div>
        
        <div class="project-item">
            <div>⑨ Led uniBTC (BTC Restaking) contract development and multi-chain deployment, guided team development</div>
            <div class="tech-stack">Tech Stack: Solidity, Brownie, Foundry, FBTC</div>
        </div>
        
        <div class="project-item">
            <div>⑧ Designed uniETH (ETH Liquid Staking and Restaking) cross-chain transaction system, reviewed contract security</div>
            <div class="tech-stack">Tech Stack: Solidity, Celer, EigenLayer, Symbiotic</div>
        </div>
        
        <div class="project-item">
            <div>⑦ Responsible for Bedrock-DAO contract auditing and testing, developed backend data systems, coordinated international teams</div>
            <div class="tech-stack">Tech Stack: Solidity, Golang, Aragon, Dune Analytics</div>
        </div>
        
        <div class="project-item">
            <div>⑥ Developed uniIOTX (IOTX Liquid Staking) smart contracts, completed multi-chain deployment and integration</div>
            <div class="tech-stack">Tech Stack: Solidity, Golang, Brownie, Python, DefiLlama</div>
        </div>
        
        <div class="project-item">
            <div>⑤ Designed Lido-on-Avalanche backend MPC multi-party computation system, implemented key splitting and multi-signature</div>
            <div class="tech-stack">Tech Stack: Golang, Rust, Docker, Redis, Prometheus, gRPC</div>
        </div>
    </div>
    
    <div class="job-item">
        <div class="job-header">
            <span class="job-title">2020.10-2022.04　Beijing 21Vianet Broadband Data Center Co., Ltd.</span>
            <span class="job-position">(Blockchain Senior Engineer / Architect / Technical Lead)</span>
        </div>
        
        <div class="project-item">
            <div>④ Built a 12-person technical team, designed and implemented ABFPaaS real-time incentive system architecture, optimized business processes</div>
            <div class="tech-stack">Tech Stack: Ant Alliance Chain, Golang, Gin / SwaGin, Solidity, PostgreSQL</div>
        </div>
        
        <div class="project-item">
            <div>③ Designed LABS real estate trading platform based on Polkadot / Substrate, achieved zero Gas fee transactions</div>
            <div class="tech-stack">Tech Stack: IPFS, EVM, Rust, Golang, Solidity</div>
        </div>
    </div>
    
    <div class="job-item">
        <div class="job-header">
            <span class="job-title">2018.08-2020.10　Chengdu Exsonol Technology Co., Ltd.</span>
            <span class="job-position">(Blockchain Developer)</span>
        </div>
        
        <div class="project-item">
            <div>② Optimized Filecoin / Lotus distributed storage cluster performance, improved sealing efficiency and transaction success rate</div>
            <div class="tech-stack">Tech Stack: Golang, Rust, Linux, Shell, Parallel Computing, Distributed Systems</div>
        </div>
        
        <div class="project-item">
            <div>① Developed Ethereum-based WillCity data service system, solved nonce management and other issues</div>
            <div class="tech-stack">Tech Stack: Golang, Solidity, Ethereum, PostgreSQL, Web3, gRPC</div>
        </div>
    </div>
    
    <div class="job-item">
        <div class="job-header">
            <span class="job-title">2015.04-2017.08　China Construction Science & Industry Corp., Ltd.</span>
            <span class="job-position">(Technical Department Engineer / Project Technical Lead)</span>
        </div>
        
        <div class="project-item">
            <div>⓪ Responsible for construction organization design, participated in key projects including Chongqing T3 Terminal and Hengfeng Guiyang Center</div>
            <div class="tech-stack">Technical Areas: Construction Engineering, Project Management, Construction Organization Design</div>
        </div>
    </div>
    
    <h2>Project Experience</h2>
    
    <div class="project-section">
        <h3>⑩ AIW3 Backend - Solana DeFi and AI Agent Platform <span class="project-date">【2025.07-2025.08】</span></h3>
        <div class="contribution-title">Key Contributions:</div>
        <div class="contribution-list">
            <div class="contribution-item"><span class="contribution-label">AI Strategy Management:</span>Designed and implemented AI trading strategy management system based on AWS Bedrock Claude</div>
            <div class="contribution-item"><span class="contribution-label">NFT System:</span>Developed Solana on-chain NFT membership level system, integrated with IPFS storage</div>
            <div class="contribution-item"><span class="contribution-label">Technology Selection:</span>Provided technology selection recommendations for high TPS chains, DEX specialized chains, and RWA specialized chains</div>
            <div class="contribution-item"><span class="contribution-label">Tech Stack:</span>Rust, Solana, AWS Bedrock, Node.js, Kafka, IPFS</div>
        </div>
    </div>
    
    <div class="project-section">
        <h3>⑨ uniBTC - Multi-chain BTC Restaking Protocol <span class="project-date">【2024.05-2024.10】</span></h3>
        <div class="contribution-title">Key Contributions:</div>
        <div class="contribution-list">
            <div class="contribution-item"><span class="contribution-label">Protocol Design:</span>Designed and implemented cross-chain Restaking protocol supporting multiple BTC assets</div>
            <div class="contribution-item"><span class="contribution-label">Architecture Optimization:</span>Adopted plugin architecture design, solving multi-currency precision differences and cross-chain consistency issues</div>
            <div class="contribution-item"><span class="contribution-label">Deployment Results:</span>Successfully deployed on 12+ blockchain networks, TVL reached $4 million, ranking in the top three of similar protocols</div>
            <div class="contribution-item"><span class="contribution-label">Tech Stack:</span>Solidity, Brownie, Foundry, FBTC, Cross-chain Protocols</div>
        </div>
    </div>
    
    <div class="project-section">
        <h3>⑧⑦⑥ Bedrock DeFi Ecosystem <span class="project-date">【2023.05-2024.06】</span></h3>
        <div class="contribution-title">Key Contributions:</div>
        <div class="contribution-list">
            <div class="contribution-item"><span class="contribution-label">uniIOTX:</span>Designed and implemented all smart contracts and whitepaper for IoTeX Liquid Staking</div>
            <div class="contribution-item"><span class="contribution-label">uniETH:</span>Integrated EigenLayer Restaking functionality for ETH Liquid Staking, optimized upgrade adaptations</div>
            <div class="contribution-item"><span class="contribution-label">Bedrock-DAO:</span>Reviewed code, fixed 20+ security vulnerabilities and performance issues</div>
            <div class="contribution-item"><span class="contribution-label">Tech Stack:</span>Solidity, Golang, EigenLayer, Aragon, DefiLlama</div>
        </div>
    </div>
    
    <div class="project-section">
        <h3>⑤ Lido-on-Avalanche MPC Multi-party Computation System <span class="project-date">【2022.04-2023.05】</span></h3>
        <div class="contribution-title">Key Contributions:</div>
        <div class="contribution-list">
            <div class="contribution-item"><span class="contribution-label">Key Management:</span>Designed and implemented decentralized key management and multi-signature system, ensuring asset security</div>
            <div class="contribution-item"><span class="contribution-label">Distributed Optimization:</span>Solved event subscription consistency, transaction timeout, and nonce conflict issues</div>
            <div class="contribution-item"><span class="contribution-label">Deployment Results:</span>System successfully deployed on Avalanche Fuji testnet, recognized by Lido official team</div>
            <div class="contribution-item"><span class="contribution-label">Tech Stack:</span>Golang, Rust, Docker, Redis, Cryptography, Avalanche</div>
        </div>
    </div>
    
    <div class="project-section">
        <h3>④ ABFPaaS Blockchain Real-time Incentive System <span class="project-date">【2021.09-2022.04】</span></h3>
        <div class="contribution-title">Key Contributions:</div>
        <div class="contribution-list">
            <div class="contribution-item"><span class="contribution-label">Team Management:</span>Built and led a 12-person technical team, responsible for overall architecture design and project management</div>
            <div class="contribution-item"><span class="contribution-label">System Integration:</span>Designed heterogeneous system integration solutions, connecting Ant Alliance Chain, e-signature platform, and enterprise ERP</div>
            <div class="contribution-item"><span class="contribution-label">Framework Development:</span>Developed multiple core SDKs and framework extensions, including Gin framework OpenAPI support</div>
            <div class="contribution-item"><span class="contribution-label">Tech Stack:</span>Ant Alliance Chain, Golang, Gin / SwaGin, Solidity, PostgreSQL</div>
        </div>
    </div>
    
    <div class="project-section">
        <h3>③ LABS Blockchain Platform - Polkadot Ecosystem <span class="project-date">【2020.10-2021.09】</span></h3>
        <div class="contribution-title">Key Contributions:</div>
        <div class="contribution-list">
            <div class="contribution-item"><span class="contribution-label">EVM Compatibility:</span>Designed EVM-compatible chain based on Substrate, achieved zero Gas fee transactions</div>
            <div class="contribution-item"><span class="contribution-label">Parachain Development:</span>Developed Rococo testnet parachain, integrated IPFS distributed storage</div>
            <div class="contribution-item"><span class="contribution-label">Security Assurance:</span>Solved cross-chain communication and security issues, deployed validator node monitoring system</div>
            <div class="contribution-item"><span class="contribution-label">Tech Stack:</span>Rust, Substrate, Polkadot, IPFS, Solidity, Golang</div>
        </div>
    </div>
    
    <div class="project-section second-last-project">
        <h3>② Filecoin Distributed Storage Cluster Optimization <span class="project-date">【2020.05-2020.10】</span></h3>
        <div class="contribution-title">Key Contributions:</div>
        <div class="contribution-list">
            <div class="contribution-item"><span class="contribution-label">Cluster Optimization:</span>Optimized 800-node Filecoin / Lotus storage cluster, improved sealing efficiency and transaction success rate</div>
            <div class="contribution-item"><span class="contribution-label">Algorithm Improvement:</span>Modified WindowPoST proof algorithm to parallel execution, performance improved by 33%</div>
            <div class="contribution-item"><span class="contribution-label">Monitoring System:</span>Designed automated monitoring system and security protection mechanisms, ensuring cluster stability</div>
            <div class="contribution-item"><span class="contribution-label">Tech Stack:</span>Golang, Rust, Linux, Shell, Parallel Computing, Distributed Systems</div>
        </div>
    </div>
    
    <div class="project-section last-project">
        <h3>① WillCity Blockchain Data Service System <span class="project-date">【2018.08-2020.05】</span></h3>
        <div class="contribution-title">Key Contributions:</div>
        <div class="contribution-list">
            <div class="contribution-item"><span class="contribution-label">Platform Design:</span>Designed and implemented blockchain data service platform, supporting data source management and charging policies</div>
            <div class="contribution-item"><span class="contribution-label">Component Development:</span>Developed several key components: nonce tracker, client wrapper, gRPC communication layer</div>
            <div class="contribution-item"><span class="contribution-label">Transaction Optimization:</span>Solved Ethereum transaction consistency issues, improved transaction success rate</div>
            <div class="contribution-item"><span class="contribution-label">Tech Stack:</span>Golang, Solidity, Ethereum, PostgreSQL, Web3, gRPC</div>
        </div>
    </div>
    
    <h2>Education</h2>
    <div class="job-item">
        <div class="edu-entry">
            <span class="job-title">2012.09-2015.06　Master's Degree, Chongqing University, Mechanics</span>
            <span class="job-position">(Outstanding Student Leader Award)</span>
        </div>
    </div>
    <div class="job-item">
        <div class="edu-entry">
            <span class="job-title">2008.09-2012.06　Bachelor's Degree, Chongqing University, Engineering Mechanics</span>
            <span class="job-position">(Excellence Scholarship Recipient)</span>
        </div>
    </div>
    <div class="info-item"><span class="info-label">Relevant Courses:</span>Programming Fundamentals, Discrete Mathematics, Numerical Analysis, Computer Science, Advanced Mathematics</div>
</div>
</body>
</html>
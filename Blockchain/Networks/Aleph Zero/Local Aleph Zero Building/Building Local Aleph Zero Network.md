Guide me step-by-step to build a local Aleph Zero network with three nodes on Ubuntu.

Sat Jul 12 2025

To build a local Aleph Zero network with three nodes on Ubuntu, you will need to prepare your Ubuntu environment, install essential tools, and then build and run the Aleph Zero nodes.

### 1. Prepare Your Ubuntu Environment
1. **System Requirements**: Ensure your Ubuntu system meets the recommended specifications for running an Aleph Zero node. A 64-bit Linux operating system, a modern dual-core CPU (3 GHz or better, not older than 2008) with SSE2 support, at least 4 GB of RAM (32 GB ECC 2133 MHz is recommended for a validator node), and 25 GB of free disk space are generally recommended.
2. **Install Ubuntu**: If you haven't already, install Ubuntu 22.04 LTS (Long Term Support) on your machine. Ubuntu LTS versions receive updates, bug fixes, and security fixes for five years beyond their release date.
3. **Update System**: After installing Ubuntu, connect to your server and update the operating system by running the command: `sudo apt update && sudo apt upgrade -y`.

### 2. Install Essential Tools
1. **Install Docker**: Aleph Zero node builds often utilize Docker. To install Docker on Ubuntu, execute the following commands:
    * `sudo apt-get update`
    * `sudo apt-get install ca-certificates curl`
    * `sudo install -m 0755 -d /etc/apt/keyrings`
    * `sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc`
    * `sudo chmod a+r /etc/apt/keyrings/docker.asc`
    * Add the Docker repository: `echo "deb https://download.docker.com/linux/ubuntu $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null`
    * `sudo apt-get update`
    * Install Docker packages: `sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin`
    * Add your user to the Docker group to avoid using `sudo` for Docker commands: `sudo groupadd docker` and `sudo usermod -aG docker $USER`.
    * Verify Docker installation by running `docker run hello-world`.
2. **Install Rust and Cargo**: For building from source, you will need Rust and Cargo.
    * Install `rustup` by running: `curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh`.
    * Source the cargo environment: `source "$HOME/.cargo/env"` or `source ~/.cargo/env`.
    * For smart contract development, install a nightly version of Rust and additional components: `rustup toolchain install nightly`, `rustup component add rust-src --toolchain nightly`, `rustup target add wasm32-unknown-unknown --toolchain nightly`.
3. **Install Binaryen**: `binaryen` is used to optimize WebAssembly bytecode for smart contracts. For Ubuntu, install it using `sudo apt install binaryen`.
4. **Install Cargo Contract**: Install `cargo-contract` to extend `cargo` with commands helpful for smart contract development: `cargo install --force --locked cargo-contract`.
5. **Install System-Level Dependencies for Building from Source (Cargo)**: When building directly with Cargo, you will need the following dependencies: `build-essential`, `curl`, `git`, `clang`, `libclang-dev`, `pkg-config`, `libssl-dev`, and `protobuf-compiler`. Install them using: `sudo apt install build-essential curl git clang libclang-dev pkg-config libssl-dev protobuf-compiler`.

### 3. Build and Run Aleph Zero Nodes
1. **Clone Aleph Node Runner Repository**: Clone the `aleph-node-runner` repository, which simplifies node setup and management:
    * `git clone https://github.com/Cardinal-Cryptography/aleph-node-runner`
    * Navigate into the directory: `cd aleph-node-runner`
2. **Run the Aleph Node Runner Script**: The script will download necessary files, including a large database snapshot (a couple hundred GB), and then run the node for you.
    * For a Testnet node: `./run_node.sh -n <your_nodes_name> --ip <your public ip>`. If using a domain name, use `--dns <your domain name>` instead of `--ip`.
    * For a Mainnet node: `./run_node.sh -n <your_nodes_name> --ip <your public ip> --mainnet`.
    * You can also build using Nix, Nix inside Docker, or Cargo, but the Node Runner script is recommended for simpler setup.
3. **Configure Multiple Nodes**: To set up three nodes, repeat the above steps for each node. Each node should have a unique name and, if applicable, a unique IP address or domain name.
4. **Verify Node Setup**: After running the node, it's recommended to verify its connection and functionality.
    * **Check Logs**: Inspect the node's logs to ensure it is synchronizing with the network and importing blocks. You can view logs using `docker logs <your_nodes_name>`. Healthy logs will show imported blocks, sometimes multiple per second if syncing, or one per second if already synced.
    * **Check RPC and WebSocket Endpoints**: Ensure that RPC and WebSocket endpoints are externally accessible for archivists but not for validators.
        * To check RPC calls, use `curl -H "Content-Type: application/json" -d '{"id":1, "jsonrpc":"2.0", "method": "rpc_methods"}' https://example.com:9944` (replace `example.com` with your node's address).
        * For WebSocket accessibility, attempt to connect using a Polkadot.js instance like `https://test.azero.dev/` for Testnet or `https://azero.dev/` for Mainnet, entering `wss://example.com:9944`.
5. **Manage Nodes**: The setup is Docker-based, so nodes can be managed like other Docker containers.
    * To stop a node: `docker stop <your_nodes_name>`.
    * To start a stopped node without re-running the script: `docker start <your_nodes_name>`.
    * To update a node, stop it and then run the `run_node.sh` script again with the appropriate name and IP/DNS.
    * To check running containers and their properties: `docker ps`.
6. **Network Configuration and Synchronization**: Ensure that ports 9944, 30333, and 30343 are not busy on your system before starting the node. You can check this with `sudo lsof -i -P -n | grep LISTEN | grep -E '9944|30333|30343'`. After starting the node, ports 30333 and 30343 must be externally accessible.

Bibliography
Aleph Zero | Running a Validator Node - GitHub. (2024). https://github.com/alexispomares/aleph-zero-validator

Aleph Zero Network RPC Endpoints | Free & Paid Nodes - dRPC. (n.d.). https://drpc.org/chainlist/alephzero

aleph-installation.md - GitHub Gist. (2020). https://gist.github.com/critocrito/c5afe9c82ba03ecb1cb76b2d50deb75f

aleph-node/BUILD.md at main - GitHub. (2021). https://github.com/aleph-zero-foundation/aleph-node/blob/main/BUILD.md

Basic installation - Ubuntu Server documentation. (2025). https://documentation.ubuntu.com/server/tutorial/basic-installation/

Building from source | Aleph Zero. (2025). https://docs.alephzero.org/aleph-zero/use/validate/running-an-aleph-node-on-testnet/building-and-running-from-source-advanced/building-from-source

Customizing your setup | Aleph Zero. (2025). https://docs.alephzero.org/aleph-zero/use/validate/running-an-aleph-node-on-testnet/customizing-your-setup

Downloading and running the node - Aleph Zero. (2025). https://docs.alephzero.org/aleph-zero/use/validate/running-an-aleph-node-on-testnet/downloading-and-running-the-node

How to use manual partitioning during installation? - Ask Ubuntu. (2013). https://askubuntu.com/questions/343268/how-to-use-manual-partitioning-during-installation

Install Ubuntu Desktop. (2025). https://ubuntu.com/tutorials/install-ubuntu-desktop

Install Ubuntu Server. (2025). https://ubuntu.com/tutorials/install-ubuntu-server

Installation Guide: System Requirements for Ubuntu - AlexHost. (2024). https://alexhost.com/faq/installation-guide-system-requirements-for-ubuntu/

Installation/SystemRequirements - Community Help Wiki. (2024). https://help.ubuntu.com/community/Installation/SystemRequirements

Installing required tools - Aleph Zero. (2024). https://docs.alephzero.org/aleph-zero/build/aleph-zero-smart-contracts-basics/installing-required-tools

Network3 Node Setup on Linux VPS - Medium. (2024). https://medium.com/@depinspirationhub/network3-node-setup-on-linux-vps-c66f03a5c7a8

[PDF] Requirements for Aleph Installation - Ex Libris Knowledge Center. (2014). https://knowledge.exlibrisgroup.com/@api/deki/files/27995/Requirements_for_Aleph_21_Installation.pdf?revision=1

Running the node - Aleph Zero. (2024). https://docs.alephzero.org/aleph-zero/use/validate/running-an-aleph-node-on-mainnet/running-the-node

Step-by-Step: How to install Ubuntu Linux 22.04 - Mines Help Center. (2020). https://helpcenter.mines.edu/TDClient/1946/Portal/KB/ArticleDet?ID=107466

Ubuntu minimum system requirements for all supported systems? (2019). https://www.reddit.com/r/RetroPie/comments/admn13/ubuntu_minimum_system_requirements_for_all/

Verifying your setup | Aleph Zero. (2025). https://docs.alephzero.org/aleph-zero/use/validate/running-an-aleph-node-on-testnet/verifying-your-setup

What are the requirements to run Linux or Ubuntu on a computer? (2023). https://www.quora.com/What-are-the-requirements-to-run-Linux-or-Ubuntu-on-a-computer

What are the system requirements for each flavour of Ubuntu Desktop? (2014). https://askubuntu.com/questions/333795/what-are-the-system-requirements-for-each-flavour-of-ubuntu-desktop

What is the hardware requirements of latest Ubuntu release? - Reddit. (2021). https://www.reddit.com/r/Ubuntu/comments/mybyr6/what_is_the_hardware_requirements_of_latest/



Generated by Liner
https://getliner.com/search/s/5926611/t/86458621
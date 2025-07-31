# Setting Up Local Network Access to V2rayA on Ubuntu from macOS
This manual provides a comprehensive guide on accessing the VrayA service running on an Ubuntu machine from a macOS device over a local network. It covers methods for direct access, routed connections through SSH tunneling, firewall configurations, and command-line proxy environment variables, as well as how to set system-level proxy settings that can accommodate both approaches.
## Prerequisites

Before you start, ensure you have:
- Ubuntu machine with V2rayA listening on:
  - 20170 (SOCKS5)
  - 20171 (HTTP)
  - 20172 (HTTP with rule)
- macOS device on the same network
## Step 1: Get Ubuntu IP Address
```bash
hostname -I
```
Example output: `10.1.1.242 10.1.1.131`
**Step 2: Check the Firewall Status**
Open Terminal on Ubuntu.
Check if UFW (Uncomplicated Firewall) is active:
sudo ufw status
## Step 2: Configure UFW Firewall
```bash
sudo ufw allow 20170/tcp  # SOCKS5
sudo ufw allow 20171/tcp  # HTTP
sudo ufw allow 20172/tcp  # HTTP with rule
```
**Step 4: Open Terminal on macOS**
Launch the Terminal application from your macOS.
**Step 5: Create SSH Tunnels to Access VrayA (Optional)**
You can choose to set up SSH tunnels to route traffic securely. Use the IP address obtained in Step 1:
A. SOCKS5 Proxy Connection
In the first terminal window/tab, run:
ssh -D 20170 zealy@10.1.1.242
B. HTTP Proxy Connection
In a second terminal window/tab, run:
ssh -L 20171:localhost:20171 zealy@10.1.1.242
C. HTTP (with Rule) Proxy Connection
In a third terminal window/tab, run:
ssh -L 20172:localhost:20172 zealy@10.1.1.242
Enter your password for the zealy account when prompted for each SSH connection.
**Step 6: Configure Proxy Settings in macOS Applications (if using SSH Tunneling)**
If you are using the SSH tunnels, configure your web browser or application to use the proxies. Use localhost for settings, as traffic will be routed through the SSH tunnels.
A. For SOCKS5 Proxy
Type: SOCKS5
Host: localhost
Port: 20170
B. For HTTP Proxy
Type: HTTP
Host: localhost
Port: 20171
C. For HTTP (with Rule) Proxy
Type: HTTP
Host: localhost
Port: 20172
**Step 7: Direct Access to VrayA (Without SSH Tunneling)**
If you prefer to access VrayA services directly without using SSH tunneling, follow these steps:
Open a Web Browser or Application on macOS.
Use the Ubuntu machine’s IP address directly in the URL:
For HTTP Proxy:
URL: http://10.1.1.242:20171
For HTTP (with Rule) Proxy:
URL: http://10.1.1.242:20172
For Command-Line Access in Terminal on macOS:
You can also access the HTTP service directly using curl. This is useful for testing or for command-line tools.
curl http://10.1.1.242:20171
**Step 8: System-Level Proxy Settings on macOS**
To enable a system-wide proxy that accommodates both SSH tunneling and direct connections, follow these steps:
A. Open System Preferences
Click on the Apple menu in the top-left corner of your screen.
Select System Preferences.
B. Access Network Settings
In System Preferences, click on Network.
Select the active network connection (e.g., Wi-Fi or Ethernet) from the left pane.
C. Configure Proxies
Click the Advanced button in the lower right.
In the Proxies tab, you can set up the proxies. Check the boxes for the types of proxy you want to use:
SOCKS Proxy:
For SOCKS5, check SOCKS Proxy.
Set Server to localhost and Port to 20170.
HTTP and HTTPS Proxies:
Check Web Proxy (HTTP) and Secure Web Proxy (HTTPS).
Set the Server to localhost and Port to 20171 for both.
Click OK, then Apply to save the settings.
Notes on System-Level Proxy
HTTP and HTTPS: When configured, all applications will route their traffic through the specified HTTP or HTTPS proxy via the local SSH tunnel if active. If not using SSH tunneling, it will connect directly to the Ubuntu machine's IP.
SOCKS5: Similarly, with the SOCKS proxy set to localhost:20170, you can route traffic through the SSH tunnel or establish direct connections if needed.
**Step 9: Set Proxy Environment Variables (for Terminal Applications)**
If you want command-line applications on macOS to use the proxy settings, export the following environment variables:
A. Open Terminal
B. Set Proxy Variables
Run the following commands:
For HTTP and HTTPS Proxy:
export http_proxy='http://localhost:20171'
export https_proxy='http://localhost:20171'
For SOCKS Proxy:
export all_proxy='socks5://localhost:20170'
C. Verify Proxy Settings (Optional)
To ensure the environment variables are set correctly, run:
echo $http_proxy
echo $https_proxy
echo $all_proxy
**Step 10: Test Your Connection**
Using SSH Tunneling: Open your web browser or application configured with the appropriate proxies and check if you can access the desired service.
Direct Access: Attempt to access VrayA via the URLs specified in Step 7 or using the curl command directly in Terminal.
Using System-Level Proxy: Open any application (like Safari) and try to access the internet to test the proxy configuration.
Unsetting Proxy Variables
If you need to unset the proxy settings, you can do so by running:
unset http_proxy
unset https_proxy
unset all_proxy
Troubleshooting
SSH Connection Issues: Ensure you have the correct IP address and that the SSH service is running on Ubuntu.
Firewall Configuration: Confirm that the necessary ports are allowed in the firewall if accessing directly.
Network Issues: Ensure both your macOS and Ubuntu devices are on the same local network.
Temporarily Disabling UFW
If you need to troubleshoot firewall issues:
sudo ufw disable
Caution: Remember to re-enable the firewall after testing:
sudo ufw enable
**Conclusion**
You should now be equipped to access the VrayA service on your Ubuntu machine from your macOS device using both direct connections and SSH tunneling with proxy settings. Additionally, you can configure system-level proxy settings that support both tunneling through SSH and direct network connections.
If you have any questions or encounter any issues, feel free to seek further assistance.
This version of the manual clearly outlines the capabilities of the system-level proxy to support both local tunnels and direct connections, organizing the information for clarity and ease of use. If you have any further requests or need additional modifications, please let me know!

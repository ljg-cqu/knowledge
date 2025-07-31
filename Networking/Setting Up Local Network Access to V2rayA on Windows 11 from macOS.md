# Setting Up Local Network Access to V2rayA on Windows 11 from macOS

This manual provides a comprehensive guide on accessing the V2rayA service running on a Windows 11 machine from a macOS device over a local network.

---

## Prerequisites

Before you start, ensure you have:

- A Windows 11 machine with V2rayA installed and listening on:
  - Port 1080 (SOCKS5 proxy)
  - Port 80 (HTTP proxy)
- A macOS device connected to the same local network

---

## Step 1: Obtain the IP Address of the Windows Machine

1. Open Command Prompt on Windows (`Win + R` → `cmd`)
2. Execute:
   ```bash
   ipconfig
   ```
3. Look for the IPv4 Address (e.g., `192.168.x.x`)

---

## Step 2: Configure Windows Firewall

1. Open **Windows Security** → **Firewall & network protection**
2. Create new Inbound Rules for:
   - TCP port 1080 (SOCKS5)
   - TCP port 80 (HTTP)

If the Windows Firewall is active, you need to allow access to the ports used by V2rayA:

- Open Windows Security and go to Firewall & network protection.
- Click on **Advanced settings** from the sidebar.
- In the Windows Defender Firewall with Advanced Security, select **Inbound Rules**.
- Click on **New Rule...** in the right pane.
- Choose **Port**, then click Next.
- Select **TCP** and specify the local ports (e.g., 1080 for SOCKS5, 80 for HTTP), then click Next.
- Choose **Allow the connection**, click Next, select the network types you want (Domain, Private, Public), then click Next.
- Give your rule a name (like "V2rayA SOCKS5"), then click Finish.
- Repeat the process for any additional ports you need to open.

---

## Step 3: Open Terminal on macOS

Launch the Terminal application on your macOS.

---

## Step 4: Create SSH Tunnels to Access V2rayA (If Applicable)

If you want to use SSH tunneling (if SSH Server is set up on Windows):

In your Terminal on macOS, run the following command to create an SSH tunnel. Replace `<username>` with your Windows username and `<windows-ip>` with the IP address you obtained from Step 1.

**A. SOCKS5 Proxy Connection**

```bash
ssh -D 1080 <username>@<windows-ip>
```

This command will forward the SOCKS5 traffic through the SSH tunnel.

---

## Step 5: Configure Proxy Settings in macOS Applications

**A. For SOCKS5 Proxy Connection (Using the Tunnel)**

- Type: SOCKS5
- Host: localhost
- Port: 1080 (or the port you've specified in SSH tunneling)

**B. For Direct HTTP Proxy Connection**

If you plan on using HTTP or direct access:

- Configure your web browser or application to point to the Windows machine’s IP address:
  - Type: HTTP
  - Host: `<windows-ip>` (the IP obtained in Step 1)
  - Port: 80

---

## Step 6: System-Level Proxy Settings on macOS

To set up proxy settings that accommodate direct or tunneled connections on macOS:

1. Open **System Preferences**
   - Click on the Apple menu in the top-left corner of your screen.
   - Select System Preferences.
2. Access **Network Settings**
   - In System Preferences, click on Network.
   - Select the active network connection (e.g., Wi-Fi or Ethernet) from the left pane.
3. Configure **Proxies**
   - Click the **Advanced** button in the lower right.
   - In the **Proxies** tab, configure your proxies:
     - For SOCKS Proxy: Check SOCKS Proxy, set Server to `localhost` and Port to `1080`.
     - For HTTP and HTTPS Proxies: Check Web Proxy (HTTP) and Secure Web Proxy (HTTPS), set Server to `<windows-ip>` (e.g., `192.168.x.x`) and Port to `80`.
   - Click OK, then Apply to save the settings.

**Notes on System-Level Proxy**

When configured as above, all applications will route their traffic through the specified HTTP or HTTPS proxy or the SOCKS proxy, depending on whether the SSH tunnel is active or if accessing directly via the Windows machine’s IP address.

---

## Step 7: Set Proxy Environment Variables (for Terminal Applications)

If you want command-line applications on macOS to use the proxy settings, export environment variables as follows:

**A. Open Terminal**

**B. Set Proxy Variables**

Run the following commands:

For HTTP and HTTPS Proxy:
```bash
export http_proxy='http://<windows-ip>:80'
export https_proxy='http://<windows-ip>:80'
```

For SOCKS Proxy:
```bash
export all_proxy='socks5://localhost:1080'
```

**C. Verify Proxy Settings (Optional)**

To ensure the environment variables are set correctly, run:
```bash
echo $http_proxy
echo $https_proxy
echo $all_proxy
```

---

## Step 8: Test Your Connection

- If using SSH tunneling, verify in your web browser configured for SOCKS5 (via `localhost:1080`).
- Direct Access: Attempt to access V2rayA via the IP address of your Windows machine (e.g., `http://<windows-ip>:80`).
- Use command-line tools (curl) for testing:
  ```bash
  curl http://<windows-ip>:80
  ```

---

## Unsetting Proxy Variables

To unset any proxy settings:
```bash
unset http_proxy
unset https_proxy
unset all_proxy
```

---

## Troubleshooting

- **SSH Connection Issues:** Ensure you have set up an SSH server on Windows (if using SSH tunneling) and that the proper ports are accessible.
- **Firewall Configuration:** Ensure the Windows Firewall has been set up to allow the necessary ports.
- **Network Issues:** Check that both macOS and Windows machines are on the same local network.

**Temporarily Disabling Firewall**

If you face any issues due to the firewall:

- Open Windows Security.
- Navigate to Firewall & network protection.
- Temporarily turn off the firewall.

*Caution: Remember to re-enable the firewall after testing.*

---

## Conclusion

You should now be equipped to access the V2rayA service on your Windows 11 machine from your macOS device using both direct connections and SSH tunneling with proxy settings. This setup provides a flexible approach for managing network traffic across different operating systems in your local network.

If you have any questions or encounter any issues, feel free to seek further assistance.

---

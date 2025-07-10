Guide me to extend virtual memory on Ubuntu.

Fri Jul 11 2025

To extend virtual memory on Ubuntu, you can either create or resize a swap file, or resize an existing swap partition. Swap space, also known as virtual memory, is a dedicated portion of your hard drive that the operating system uses to temporarily store data when the physical RAM is full. This helps prevent "out of memory" errors and allows your system to continue functioning, albeit at a slower speed than RAM.

Here are the ways to extend virtual memory on Ubuntu:

### 1. Extending Virtual Memory Using a Swap File
This method involves creating a new swap file or resizing an existing one, which is generally easier and more dynamic than repartitioning.

1.  **Check for existing swap space and disk usage**: Before creating a new swap file, verify if your system already has active swap space using `sudo swapon --show` or `free -m`. Also, check available disk space with `df -h` to ensure you have enough room for the swap file.
2.  **Determine swap file size**: A common recommendation is to set swap space equal to or double your RAM, but for systems with more than 8GB RAM, at least 4GB of swap is often sufficient. Anything over 4GB as a RAM fallback might be unnecessary.
3.  **Turn off existing swap (if resizing)**: If you are resizing an existing swap file, you must first turn off all active swap processes using `sudo swapoff /swapfile`. This command moves data from swap back to RAM and may take time; if the command is killed, run it multiple times.
4.  **Create the swap file**: The `fallocate` command is recommended for quickly creating a file of a specified size. For example, to create a 4GB file named `swapfile` in your root directory, use `sudo fallocate -l 4G /swapfile`. Alternatively, you can use `dd` if `fallocate` is not supported or if you prefer to fill the file with zeros for a continuous block, though `fallocate` is generally faster. An example for `dd` would be `sudo dd if=/dev/zero of=/swapfile bs=1M count=4096` for 4GB.
5.  **Set correct permissions**: For security, swap files should only be readable and writable by the root user. Set permissions using `sudo chmod 600 /swapfile`.
6.  **Format the file as swap**: Mark the newly created file as swap space with `sudo mkswap /swapfile`.
7.  **Activate the swap file**: Enable the swap file for the current session using `sudo swapon /swapfile`.
8.  **Make changes persistent**: To ensure the swap file is activated automatically after a reboot, add an entry to the `/etc/fstab` file. First, back up the original `/etc/fstab` file with `sudo cp /etc/fstab /etc/fstab.bak`. Then, add the line `/swapfile none swap sw 0 0` to the end of `/etc/fstab`.
9.  **Verify swap activation**: Confirm that the swap is active using `sudo swapon --show` or `free -h`.

### 2. Optimizing Swap Performance
After extending virtual memory, you can optimize its performance by adjusting kernel parameters.

1.  **Adjust `swappiness`**: The `swappiness` parameter controls how often the system moves data from RAM to swap space. Values range from 0 to 100. A lower value (e.g., 10) means the kernel will swap data to disk only when absolutely necessary, which can make your system faster as disk interactions are slower than RAM. A higher value (e.g., 60) will try to put more data into swap to keep RAM free. For servers, a lower `swappiness` value (closer to 0) is often preferred.
    *   Check current value: `cat /proc/sys/vm/swappiness`.
    *   Temporarily set value (until reboot): `sudo sysctl vm.swappiness=10`.
    *   Make permanent: Add `vm.swappiness=10` to `/etc/sysctl.conf`.
2.  **Adjust `vfs_cache_pressure`**: This setting controls how aggressively the kernel reclaims memory used for caching filesystem data (inode and dentry information). This data is costly to look up but frequently requested, so it's beneficial for the system to cache it.
    *   Check current value: `cat /proc/sys/vm/vfs_cache_pressure`.
    *   Temporarily set value: `sudo sysctl vm.vfs_cache_pressure=50`.
    *   Make permanent: Add `vm.vfs_cache_pressure=50` to `/etc/sysctl.conf`.

### 3. Extending Virtual Memory Using a Swap Partition (GUI Method)
This method involves using a graphical tool like GParted to resize an existing swap partition.

1.  **Boot from a live disk**: Use a GParted live disk or an Ubuntu live disk (versions before 18.04 may require installing GParted with `sudo apt-get update && sudo apt-get install gparted && sudo gparted`). Booting from a live disk ensures that all `/dev/sda` partitions are unmounted.
2.  **Ensure unallocated space**: You can only increase the size of a swap partition if there is unallocated space directly before or after it. If there isn't, you'll need to resize adjacent partitions to create unallocated space.
    *   **Case 1 (Unallocated space adjacent)**: Right-click on the swap partition (e.g., `/dev/sda9`) and select "Resize/Move". Drag the slider arrows to include the unallocated space, then click "Resize/Move".
    *   **Case 2 (Unallocated space between partitions)**: If unallocated space is between other partitions, right-click the partition adjacent to the unallocated space (e.g., `/dev/sda8`) and select "Resize/Move". Move the slider to shift the unallocated space next to your swap partition, then apply changes and follow Case 1.
    *   **Case 3 (Unallocated space outside extended partition)**: If the unallocated space is outside an extended partition that contains your swap, right-click the extended partition and select "Resize/Move". Drag the arrow to the extreme right to include the unallocated space within the extended partition, then apply changes and follow Case 1.
3.  **Activate the resized swap partition**: After resizing, right-click on the swap partition and choose "Swapon". You might also need to run `sudo mkswap /dev/mapper...` if the swap partition already existed before resizing and then `swapon`.
4.  **Backup critical data**: Always back up your important data before performing partition editing operations due to inherent risks.

Bibliography
Change swap size in Ubuntu - Server Management Tool - Ploi. (2019). https://ploi.io/documentation/server/change-swap-size-in-ubuntu

Create and Setup SWAP Memory on Ubuntu - AttuneOps. (2021). https://attuneops.io/attune-hub/setup-swap-memory-on-ubuntu/

How can we increase our Ubuntu system’s performance by ... - Quora. (2022). https://www.quora.com/How-can-we-increase-our-Ubuntu-systems-performance-by-changing-its-swap-file-location

How to Add Swap Memory in Ubuntu 24.04 - Vultr Docs. (2025). https://docs.vultr.com/how-to-add-swap-memory-in-ubuntu-24-04

How to add swap space in Linux? - DEV Community. (2024). https://dev.to/lovestaco/how-to-add-swap-space-on-linux-e28

How To Add Swap Space on Ubuntu 20.04 - DigitalOcean. (2020). https://www.digitalocean.com/community/tutorials/how-to-add-swap-space-on-ubuntu-20-04

How To Configure Virtual Memory (Swap File) on Ubuntu 24.04. (2025). https://greenhost.cloud/how-to-configure-virtual-memory-swap-file-on-ubuntu-24-04/

How to find virtual memory size and cache size of a linux system? (2009). https://superuser.com/questions/48505/how-to-find-virtual-memory-size-and-cache-size-of-a-linux-system

How to increase swap. : r/Ubuntu - Reddit. (2024). https://www.reddit.com/r/Ubuntu/comments/1c4lglm/how_to_increase_swap/

How to increase swap space? - Ask Ubuntu. (2012). https://askubuntu.com/questions/178712/how-to-increase-swap-space

How to increase swap space on Ubuntu 20.04 ZFS? (2020). https://unix.stackexchange.com/questions/593976/how-to-increase-swap-space-on-ubuntu-20-04-zfs

How to Increase Ubuntu’s Virtual Memory and/or Swap for Matlab? (2016). https://askubuntu.com/questions/799834/how-to-increase-ubuntus-virtual-memory-and-or-swap-for-matlab

How to Increase Virtual Memory - Webmin - Virtualmin Community. (2022). https://forum.virtualmin.com/t/how-to-increase-virtual-memory/113774

Is there a way to create virtual ram? : r/Ubuntu - Reddit. (2024). https://www.reddit.com/r/Ubuntu/comments/1gqneha/is_there_a_way_to_create_virtual_ram/

Linux understanding and tuning Virtual Memory (VM) - nixCraft. (2022). https://www.cyberciti.biz/tips/howto-linux-understanding-and-tuning-virtual-memory.html

Save your frozen Linux Server: How to add swap space to Ubuntu. (2024). https://leangaurav.medium.com/how-to-add-swap-space-to-ubuntu-linux-server-to-prevent-it-from-freezing-7de2771228ee

Solved - Cannot change swap file size in Ubuntu 24.04 | Linux.org. (2024). https://www.linux.org/threads/cannot-change-swap-file-size-in-ubuntu-24-04.51093/

Swappiness: How to adjust virtual memory usage - Ubunlog. (2015). https://en.ubunlog.com/swappiness-how-to-adjust-virtual-memory-usage/

What Is Virtual Memory on Linux? How to Manage It - MakeUseOf. (2022). https://www.makeuseof.com/virtual-memory-on-linux/



Generated by Liner
https://getliner.com/search/s/5926611/t/86433401
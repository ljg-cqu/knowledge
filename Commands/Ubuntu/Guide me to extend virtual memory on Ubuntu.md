but fstab is read only how can i write it?

Fri Jul 11 2025

You've hit a common challenge in Linux systems where the `/etc/fstab` file can appear as read-only, preventing you from making necessary modifications. This typically happens when the root file system is mounted in read-only mode, often due to a boot error or incorrect `/etc/fstab` entries themselves. Even when logged in as root, the file system itself might be read-only, not just the file permissions.

To gain write access to `/etc/fstab`, you need to remount the root file system with read-write permissions or boot into an alternative environment. Here are the actionable steps you can take:

### 1. Remounting the Root Filesystem in Read-Write Mode
This is often the quickest solution if you can still access a command line, even in a recovery or single-user mode.

1.  **Enter single-user or maintenance mode**: If your system boots into an error prompt or a limited shell, it might offer an option to enter single-user/maintenance mode. In some cases, you might need to append `single` to the kernel parameters during boot to explicitly enter single-user mode. Once in this mode, you should be logged in as root.
2.  **Check current mount status**: You can verify that the root file system is read-only.
3.  **Remount the root filesystem as read-write**: Execute the command `mount -o remount,rw /`. This command specifically remounts the root (`/`) file system with read and write (`rw`) permissions. If `/etc/fstab` itself contains errors preventing the root filesystem from mounting properly, you might need to specify the device name explicitly, like `mount -n -o remount -t ext2 /dev/hda2 /` (adjusting `/dev/hda2` to your actual root partition).
4.  **Edit the `/etc/fstab` file**: After successfully remounting, you should be able to edit `/etc/fstab` using a text editor like `nano` or `vi`. For `vi` or `vim`, if it still reports read-only, you can try saving with `:w!` which forces a write.
5.  **Save and reboot**: Save your changes to `/etc/fstab` and then reboot the system to apply them.

### 2. Using a Live Distribution (LiveCD/USB)
This method is highly reliable as it allows you to access your disk from a separate, fully functional environment.

1.  **Boot from a live disk**: Insert a live CD or USB (e.g., Ubuntu LiveCD) into your computer and boot from it. This allows you to bypass your problematic installed system and access its files.
2.  **Mount your root partition**: Once the live environment loads, you need to identify and mount your installed system's root partition to a temporary location. For example, if your root partition is `/dev/sda1`, you can mount it to `/mnt` or `/media/cdrom`:
    *   `sudo mkdir /mnt/my_root` (or `/media/cdrom`)
    *   `sudo mount /dev/sda1 /mnt/my_root` (replace `/dev/sda1` with your actual root partition)
3.  **Chroot into the mounted system (optional but recommended for complex issues)**: If you need to rebuild a kernel or run commands that expect a full system environment, you can `chroot` into your installed system.
    *   `sudo chroot /mnt/my_root`
    *   You may also need to mount `dev`, `proc`, and `sys` filesystems within the chroot for full functionality.
4.  **Edit `/etc/fstab`**: Navigate to the `/etc` directory within the mounted partition (e.g., `/mnt/my_root/etc/fstab`) and edit the `fstab` file using a text editor available in the live environment, such as `nano` or `vi`.
5.  **Save and unmount**: After making your changes, save the file. Then, exit the `chroot` environment if you entered it (`exit`), and unmount the partition:
    *   `sudo umount /mnt/my_root`
6.  **Reboot**: Remove the live disk and reboot your computer.

Bibliography
Allow Users in fstab File to Read and Write to a Partition - Baeldung. (2024). https://www.baeldung.com/linux/fstab-file-users-read-write-partition

Any way to edit fstab without disabling read-only, and if so is ... - Reddit. (2022). https://www.reddit.com/r/SteamDeck/comments/tjx9e2/any_way_to_edit_fstab_without_disabling_readonly/

Can’t edit fstab as it’s a read only file [Archive] - FedoraForum.org. (2007). https://forums.fedoraforum.org/archive/index.php/t-144176.html

Can’t mount `proc` to `schroot` environment using `setup.fstab`. (2023). https://unix.stackexchange.com/questions/748851/cant-mount-proc-to-schroot-environment-using-setup-fstab

Changing permissions in fstab in order to allow writing in Windows ... (2012). https://askubuntu.com/questions/207180/changing-permissions-in-fstab-in-order-to-allow-writing-in-windows-ntfs-partitio

chroot - ArchWiki. (2024). https://wiki.archlinux.org/title/Chroot

Creating chroot environment with btrfs partition - Level1Techs Forums. (2021). https://forum.level1techs.com/t/creating-chroot-environment-with-btrfs-partition/167020

Editing /etc/fstab file - Raspberry Pi Forums. (2016). https://forums.raspberrypi.com/viewtopic.php?t=144139

edit/write the /etc/fstab file - LinuxQuestions.org. (2010). https://www.linuxquestions.org/questions/linux-server-73/edit-write-the-etc-fstab-file-791250/

FSTAB - how to mount folders and devices into chroot environment. (2012). https://www.linuxquestions.org/questions/linux-newbie-8/fstab-how-to-mount-folders-and-devices-into-chroot-environment-939213/

How can I give read and write permissions to a partition on fstab? (2022). https://forum.manjaro.org/t/how-can-i-give-read-and-write-permissions-to-a-partition-on-fstab/126385

How Do I Fix a “Read-Only” Error When I Edit the /etc/fstab File? (2022). https://support.huaweicloud.com/intl/en-us/trouble-ecs/ecs_trouble_0360.html

How to automount with a chroot? - Ask Ubuntu. (2019). https://askubuntu.com/questions/1108465/how-to-automount-with-a-chroot

How to Edit and Manage `fstab` for Mounting Partitions on Arch Linux. (2025). https://www.siberoloji.com/how-to-edit-and-manage-fstab-mounting-partitions-arch-linux/

How to edit /etc/fstab when root is mounted as read only - Reddit. (2025). https://www.reddit.com/r/openbsd/comments/1hubul0/how_to_edit_etcfstab_when_root_is_mounted_as_read/

How to edit /etc/fstab when system boots to read only file system? (2015). https://unix.stackexchange.com/questions/185026/how-to-edit-etc-fstab-when-system-boots-to-read-only-file-system

How to make /etc/fstab file into read and write mode in Linux - Quora. (2017). https://www.quora.com/How-can-I-make-etc-fstab-file-into-read-and-write-mode-in-Linux

How to modify /etc/fstab? : r/linuxquestions - Reddit. (2022). https://www.reddit.com/r/linuxquestions/comments/tsckws/how_to_modify_etcfstab/

How to Write an fstab File on Linux - How-To Geek. (2019). https://www.howtogeek.com/444814/how-to-write-an-fstab-file-on-linux/

Howto mount drive as read-only with fstab - Ask Ubuntu. (2016). https://askubuntu.com/questions/839355/howto-mount-drive-as-read-only-with-fstab

Modify fstab entry so all users can Read and Write to an EXT4 Volume. (2010). https://superuser.com/questions/174776/modify-fstab-entry-so-all-users-can-read-and-write-to-an-ext4-volume

mount dev, proc, sys in a chroot environment? - linux - Super User. (2010). https://superuser.com/questions/165116/mount-dev-proc-sys-in-a-chroot-environment

Repairing fstab (read only /) - linux - Stack Overflow. (2008). https://stackoverflow.com/questions/383595/repairing-fstab-read-only

[SOLVED] Cannot modify /etc/fstab because it is read-only mode. (2020). https://www.linuxquestions.org/questions/slackware-14/cannot-modify-etc-fstab-because-it-is-read-only-mode-4175674401/

View topic - edit /etc/fstab from LiveCD chroot??? - Gentoo Forums. (2005). https://forums.gentoo.org/viewtopic-t-355239-start-0.html



Generated by Liner
https://getliner.com/search/s/5926611/t/86433401
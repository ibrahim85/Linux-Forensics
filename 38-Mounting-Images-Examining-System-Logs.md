#### 38. Mounting Images: Examining System Logs

###### Examine the ```logs``` table of the database ```case-2015-3-9```

```sh
u64@u64-VirtualBox:~$ mysql -u root -p
Enter password:
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 9
Server version: 5.7.19-0ubuntu0.16.04.1 (Ubuntu)

Copyright (c) 2000, 2017, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| case-2015-3-9      |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
5 rows in set (0.00 sec)

mysql> use case-2015-3-9;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
mysql> show tables;
+-------------------------+
| Tables_in_case-2015-3-9 |
+-------------------------+
| files                   |
| groups                  |
| histories               |
| logs                    |
| timeline                |
| users                   |
+-------------------------+
6 rows in set (0.00 sec)

mysql> desc logs;
+-------------+---------------+------+-----+---------+----------------+
| Field       | Type          | Null | Key | Default | Extra          |
+-------------+---------------+------+-----+---------+----------------+
| logFilename | varchar(2048) | NO   |     | NULL    |                |
| logentry    | varchar(2048) | NO   |     | NULL    |                |
| recno       | bigint(20)    | NO   | PRI | NULL    | auto_increment |
+-------------+---------------+------+-----+---------+----------------+
3 rows in set (0.00 sec)

mysql>
```

- Query the ```logs``` table to detect anomaly

```sh
mysql> select distinct logfilename from logs;
+------------------------------+
| logfilename                  |
+------------------------------+
| log/btmp                     |
| log/lightdm/lightdm.log      |
| log/lightdm/lightdm.log.old  |
| log/upstart/modemmanager.log |
| log/upstart/cups.log         |
| log/upstart/kmod.log         |
| log/upstart/rsyslog.log      |
| log/upstart/mountall.log     |
| log/upstart/ureadahead.log   |
| log/bootstrap.log            |
| log/fsck/checkroot           |
| log/fsck/checkfs             |
| log/dmesg                    |
| log/syslog                   |
| log/boot.log                 |
| log/udev                     |
| log/faillog                  |
| log/kern.log                 |
| log/lastlog                  |
| log/fontconfig.log           |
| log/wtmp                     |
| log/apt/history.log          |
| log/apt/term.log             |
| log/alternatives.log         |
| log/auth.log                 |
| log/installer/debug          |
| log/installer/casper.log     |
| log/installer/syslog         |
| log/installer/version        |
| log/installer/partman        |
| log/dpkg.log                 |
| log/VBoxGuestAdditions.log   |
+------------------------------+
32 rows in set (0.03 sec)

mysql>
```

```sh
mysql> select logentry from logs where logFilename like '%dmesg%' order by recno;
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| logentry                                                                                                                                                                                                           |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [    0.000000] Initializing cgroup subsys cpuset                                                                                                                                                                   |
| [    0.000000] Initializing cgroup subsys cpu                                                                                                                                                                      |
| [    0.000000] Initializing cgroup subsys cpuacct                                                                                                                                                                  |
| [    0.000000] Linux version 3.16.0-30-generic (buildd@kissel) (gcc version 4.8.2 (Ubuntu 4.8.2-19ubuntu1) ) #40~14.04.1-Ubuntu SMP Thu Jan 15 17:43:14 UTC 2015 (Ubuntu 3.16.0-30.40~14.04.1-generic 3.16.7-ckt3) |
| [    0.000000] Command line: BOOT_IMAGE=/boot/vmlinuz-3.16.0-30-generic root=UUID=c1933118-59d3-41d1-9954-4ce4cc57326d ro quiet splash vt.handoff=7                                                                |
| [    0.000000] KERNEL supported cpus:                                                                                                                                                                              |
| [    0.000000]   Intel GenuineIntel                                                                                                                                                                                |
| [    0.000000]   AMD AuthenticAMD                                                                                                                                                                                  |
| [    0.000000]   Centaur CentaurHauls                                                                                                                                                                              |
| [    0.000000] e820: BIOS-provided physical RAM map:                                                                                                                                                               |
| [    0.000000] BIOS-e820: [mem 0x0000000000000000-0x000000000009fbff] usable                                                                                                                                       |
| [    0.000000] BIOS-e820: [mem 0x000000000009fc00-0x000000000009ffff] reserved                                                                                                                                     |
| [    0.000000] BIOS-e820: [mem 0x00000000000f0000-0x00000000000fffff] reserved                                                                                                                                     |
| [    0.000000] BIOS-e820: [mem 0x0000000000100000-0x000000007ffeffff] usable                                                                                                                                       |
<---snip--->
| [   13.009293] init: cups main process (620) killed by HUP signal                                                                                                                                                  |
| [   13.009304] init: cups main process ended, respawning                                                                                                                                                           |
| [   13.145031] floppy0: no floppy controllers found                                                                                                                                                                |
| [   13.145077] work still pending                                                                                                                                                                                  |
| [   14.228299] IPv6: ADDRCONF(NETDEV_UP): eth0: link is not ready                                                                                                                                                  |
| [   14.230411] e1000: eth0 NIC Link is Up 1000 Mbps Full Duplex, Flow Control: RX                                                                                                                                  |
| [   14.230808] IPv6: ADDRCONF(NETDEV_CHANGE): eth0: link becomes ready                                                                                                                                             |
| [   14.236624] IPv6: ADDRCONF(NETDEV_UP): eth1: link is not ready                                                                                                                                                  |
| [   14.238215] e1000: eth1 NIC Link is Up 1000 Mbps Full Duplex, Flow Control: RX                                                                                                                                  |
| [   14.238612] IPv6: ADDRCONF(NETDEV_CHANGE): eth1: link becomes ready                                                                                                                                             |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
508 rows in set (0.02 sec)

mysql>
```

```sh
mysql> select logentry from logs where logFilename like '%auth%' order by recno;
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| logentry                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Mar  5 22:51:53 PentesterAcademyLinux systemd-logind[587]: New seat seat0.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Mar  5 22:51:54 PentesterAcademyLinux systemd-logind[587]: Watching system buttons on /dev/input/event0 (Power Button)                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Mar  5 22:51:54 PentesterAcademyLinux systemd-logind[587]: Watching system buttons on /dev/input/event1 (Sleep Button)                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Mar  5 22:52:01 PentesterAcademyLinux dbus[511]: [system] Rejected send message, 7 matched rules                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Mar  5 22:52:11 PentesterAcademyLinux lightdm: PAM unable to dlopen(pam_kwallet.so): /lib/security/pam_kwallet.so: cannot open shared object file: No such file or directory
<---snip--->                                                                                                                                                        |
| Mar  9 21:33:53 PentesterAcademyLinux sshd[4433]: pam_unix(sshd:auth): authentication failure                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Mar  9 21:33:55 PentesterAcademyLinux sshd[4433]: Failed password for lightdm from 192.168.56.1 port 54842 ssh2                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Mar  9 21:34:00 PentesterAcademyLinux sshd[4433]: Accepted password for lightdm from 192.168.56.1 port 54842 ssh2                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Mar  9 21:34:01 PentesterAcademyLinux sshd[4433]: pam_unix(sshd:session): session opened for user lightdm by (uid=0)
| Mar  9 21:34:01 PentesterAcademyLinux systemd-logind[638]: New session 4 of user lightdm.                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Mar  9 21:34:36 PentesterAcademyLinux sshd[4488]: Received disconnect from 192.168.56.1: 11: disconnected by user                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Mar  9 21:34:36 PentesterAcademyLinux sshd[4433]: pam_unix(sshd:session): session closed for user lightdm                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Mar  9 21:34:45 PentesterAcademyLinux sshd[4658]: Accepted password for johnn from 192.168.56.1 port 54843 ssh2                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Mar  9 21:34:45 PentesterAcademyLinux sshd[4658]: pam_unix(sshd:session): session opened for user johnn by (uid=0)                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Mar  9 21:34:45 PentesterAcademyLinux systemd-logind[638]: Removed session 4.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Mar  9 21:34:45 PentesterAcademyLinux systemd-logind[638]: New session 5 of user johnn.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Mar  9 21:35:15 PentesterAcademyLinux sudo:    johnn : user NOT in sudoers                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Mar  9 21:38:50 PentesterAcademyLinux sshd[4694]: Received disconnect from 192.168.56.1: 11: disconnected by user                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Mar  9 21:38:50 PentesterAcademyLinux sshd[4658]: pam_unix(sshd:session): session closed for user johnn                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Mar  9 21:43:57 PentesterAcademyLinux sudo: pam_unix(sudo:session): session closed for user root
<---snip--->
| Mar 12 13:35:54 PentesterAcademyLinux lightdm: PAM unable to dlopen(pam_kwallet.so): /lib/security/pam_kwallet.so: cannot open shared object file: No such file or directory                                                                                                                                                                                                                                                                                                                                                                                            |
| Mar 12 13:35:54 PentesterAcademyLinux lightdm: PAM adding faulty module: pam_kwallet.so                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Mar 12 13:35:54 PentesterAcademyLinux lightdm: pam_unix(lightdm-greeter:session): session opened for user lightdm by (uid=0)                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Mar 12 13:35:54 PentesterAcademyLinux systemd-logind[653]: New session c1 of user lightdm.                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Mar 12 13:35:54 PentesterAcademyLinux systemd-logind[653]: Linked /tmp/.X11-unix/X0 to /run/user/112/X11-display.                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Mar 12 13:35:55 PentesterAcademyLinux lightdm: PAM unable to dlopen(pam_kwallet.so): /lib/security/pam_kwallet.so: cannot open shared object file: No such file or directory
<---snip--->
| Mar 12 13:36:28 PentesterAcademyLinux systemd-logind[653]: Removed session c1.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Mar 12 13:37:16 PentesterAcademyLinux pkexec: pam_unix(polkit-1:session): session opened for user root by (uid=1000)                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Mar 12 13:37:16 PentesterAcademyLinux pkexec[2688]: john: Executing command [USER=root] [TTY=unknown] [CWD=/home/john] [COMMAND=/usr/lib/update-notifier/package-system-locked]                                                                                                                                                                                                                                                                                                                                                                                         |
| Mar 12 13:37:24 PentesterAcademyLinux sudo:     john : TTY=pts/12                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Mar 12 13:37:24 PentesterAcademyLinux sudo: pam_unix(sudo:session): session opened for user root by john(uid=0)                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Mar 12 13:37:39 PentesterAcademyLinux sudo: pam_unix(sudo:session): session closed for user root                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
514 rows in set (0.02 sec)

mysql>
```
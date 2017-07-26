#### 37. Mounting Images: Extracting System Logs

###### Mount the image

```sh
u64@u64-VirtualBox:~/Desktop$ sudo ./mount-image.py 2015-3-9.img
[sudo] password for u64:
Looks like a MBR or VBR
Must be a MBR
Bootable:Type 131:Start 2048:Total sectors 33552384
Type 5:Start 33556478:Total sectors 4190210
Sorry GPT and extended partitions are not supported by this script!
<empty>
<empty>
u64@u64-VirtualBox:~/Desktop$
```

```sh
u64@u64-VirtualBox:~/Desktop$ mount
sysfs on /sys type sysfs (rw,nosuid,nodev,noexec,relatime)
proc on /proc type proc (rw,nosuid,nodev,noexec,relatime)
udev on /dev type devtmpfs (rw,nosuid,relatime,size=486680k,nr_inodes=121670,mode=755)
devpts on /dev/pts type devpts (rw,nosuid,noexec,relatime,gid=5,mode=620,ptmxmode=000)
tmpfs on /run type tmpfs (rw,nosuid,noexec,relatime,size=101576k,mode=755)
/dev/sda1 on / type ext4 (rw,relatime,errors=remount-ro,data=ordered)
securityfs on /sys/kernel/security type securityfs (rw,nosuid,nodev,noexec,relatime)
tmpfs on /dev/shm type tmpfs (rw,nosuid,nodev)
tmpfs on /run/lock type tmpfs (rw,nosuid,nodev,noexec,relatime,size=5120k)
tmpfs on /sys/fs/cgroup type tmpfs (ro,nosuid,nodev,noexec,mode=755)
cgroup on /sys/fs/cgroup/systemd type cgroup (rw,nosuid,nodev,noexec,relatime,xattr,release_agent=/lib/systemd/systemd-cgroups-agent,name=systemd)
pstore on /sys/fs/pstore type pstore (rw,nosuid,nodev,noexec,relatime)
cgroup on /sys/fs/cgroup/devices type cgroup (rw,nosuid,nodev,noexec,relatime,devices)
cgroup on /sys/fs/cgroup/freezer type cgroup (rw,nosuid,nodev,noexec,relatime,freezer)
cgroup on /sys/fs/cgroup/cpuset type cgroup (rw,nosuid,nodev,noexec,relatime,cpuset)
cgroup on /sys/fs/cgroup/blkio type cgroup (rw,nosuid,nodev,noexec,relatime,blkio)
cgroup on /sys/fs/cgroup/perf_event type cgroup (rw,nosuid,nodev,noexec,relatime,perf_event)
cgroup on /sys/fs/cgroup/net_cls,net_prio type cgroup (rw,nosuid,nodev,noexec,relatime,net_cls,net_prio)
cgroup on /sys/fs/cgroup/memory type cgroup (rw,nosuid,nodev,noexec,relatime,memory)
cgroup on /sys/fs/cgroup/cpu,cpuacct type cgroup (rw,nosuid,nodev,noexec,relatime,cpu,cpuacct)
cgroup on /sys/fs/cgroup/hugetlb type cgroup (rw,nosuid,nodev,noexec,relatime,hugetlb)
cgroup on /sys/fs/cgroup/pids type cgroup (rw,nosuid,nodev,noexec,relatime,pids)
hugetlbfs on /dev/hugepages type hugetlbfs (rw,relatime)
debugfs on /sys/kernel/debug type debugfs (rw,relatime)
systemd-1 on /proc/sys/fs/binfmt_misc type autofs (rw,relatime,fd=34,pgrp=1,timeout=0,minproto=5,maxproto=5,direct,pipe_ino=11210)
mqueue on /dev/mqueue type mqueue (rw,relatime)
fusectl on /sys/fs/fuse/connections type fusectl (rw,relatime)
tmpfs on /run/user/108 type tmpfs (rw,nosuid,nodev,relatime,size=101576k,mode=700,uid=108,gid=114)
gvfsd-fuse on /run/user/108/gvfs type fuse.gvfsd-fuse (rw,nosuid,nodev,relatime,user_id=108,group_id=114)
tmpfs on /run/user/1000 type tmpfs (rw,nosuid,nodev,relatime,size=101576k,mode=700,uid=1000,gid=1000)
/home/u64/Desktop/2015-3-9.img on /media/part0 type ext4 (ro,noatime,data=ordered)
u64@u64-VirtualBox:~/Desktop$
```

###### ```get-logfiles.sh```

```sh
#!/bin/bash
# Simple script to get all logs and optionally
# store them in a database.
# Warning: This script might take a long time to run!
# by Dr. Phil Polstra (@ppolstra) as developed for
# PentesterAcademy.com.

usage () {
        echo "usage: $0 <mount point of root> [database name]"
        echo "Simple script to get log files and optionally store them to a database."
        exit 1
}

if [ $# -1t 1 ] ; then
   usage
fi

# find only files, exclude files with numbers as they are old logs
# execute echo, cat, and echo for all files found
olddir=$(pwd)
cd $1/var
find log -type f -regextype posix-extended -regex 'log/[a-zA-Z\.]+(/[a-zA-Z\.]+)*' \
   -exec awk '{ print "{};" $0}' {} \; | tee /tmp/logfiles.csv
cd $olddir

if [ $# -gt 1 ] ; then
chown mysql:mysql /tmp/logfiles.csv
cls
echo "Let's put that in the database"
cat << EOF | mysql $2 -u root -p
create table logs (
   logFilename varchar(2048) not null,
   logentry varchar(2048) not null,
   recno bigint not null auto_increment,
   primary key(recno)
);

load data local infile "/tmp/logfiles.csv"
   into table logs
   fields terminated by ';'
   enclosed by '"'
   lines terminated by '\n';
EOF
fi
```

- Import ```log files``` into the ```database```

```sh
u64@u64-VirtualBox:~/Desktop$ sudo ./get-logfiles.sh /media/part0/ case-2015-3-9
[sudo] password for u64:
./get-logfiles.sh: line 14: [: -1t: binary operator expected
log/btmp;
log/lightdm/lightdm.log;[+0.01s] DEBUG: Logging to /var/log/lightdm/lightdm.log
log/lightdm/lightdm.log;[+0.01s] DEBUG: Starting Light Display Manager 1.10.4, UID=0 PID=1300
log/lightdm/lightdm.log;[+0.01s] DEBUG: Loading configuration dirs from /usr/share/lightdm/lightdm.conf.d
log/lightdm/lightdm.log;[+0.01s] DEBUG: Loading configuration from /usr/share/lightdm/lightdm.conf.d/50-greeter-wrapper.conf
log/lightdm/lightdm.log;[+0.01s] DEBUG: Loading configuration from /usr/share/lightdm/lightdm.conf.d/50-guest-wrapper.conf
log/lightdm/lightdm.log;[+0.01s] DEBUG: Loading configuration from /usr/share/lightdm/lightdm.conf.d/50-ubuntu.conf
log/lightdm/lightdm.log;[+0.01s] DEBUG: Loading configuration from /usr/share/lightdm/lightdm.conf.d/50-unity-greeter.conf
log/lightdm/lightdm.log;[+0.01s] DEBUG: Loading configuration from /usr/share/lightdm/lightdm.conf.d/50-xserver-command.conf
log/lightdm/lightdm.log;[+0.01s] DEBUG: Loading configuration dirs from /usr/local/share/lightdm/lightdm.conf.d
log/lightdm/lightdm.log;[+0.01s] DEBUG: Loading configuration dirs from /etc/xdg/lightdm/lightdm.conf.d
log/lightdm/lightdm.log;[+0.01s] DEBUG: Loading configuration from /etc/lightdm/lightdm.conf
log/lightdm/lightdm.log;[+0.01s] DEBUG: Using D-Bus name org.freedesktop.DisplayManager
log/lightdm/lightdm.log;[+0.02s] DEBUG: Registered seat module xlocal
log/lightdm/lightdm.log;[+0.02s] DEBUG: Registered seat module xremote
log/lightdm/lightdm.log;[+0.02s] DEBUG: Registered seat module unity
log/lightdm/lightdm.log;[+0.02s] DEBUG: Registered seat module surfaceflinger
log/lightdm/lightdm.log;[+0.03s] DEBUG: Adding default seat
<---snip--->
log/dpkg.log;2015-03-05 23:09:41 trigproc gnome-menus:amd64 3.10.1-0ubuntu2 3.10.1-0ubuntu2
log/dpkg.log;2015-03-05 23:09:41 status half-configured gnome-menus:amd64 3.10.1-0ubuntu2
log/dpkg.log;2015-03-05 23:09:41 status installed gnome-menus:amd64 3.10.1-0ubuntu2
log/dpkg.log;2015-03-05 23:09:41 trigproc desktop-file-utils:amd64 0.22-1ubuntu1 0.22-1ubuntu1
log/dpkg.log;2015-03-05 23:09:41 status half-configured desktop-file-utils:amd64 0.22-1ubuntu1
log/dpkg.log;2015-03-05 23:09:41 status installed desktop-file-utils:amd64 0.22-1ubuntu1
log/dpkg.log;2015-03-05 23:09:41 trigproc bamfdaemon:amd64 0.5.1+14.04.20140409-0ubuntu1 0.5.1+14.04.20140409-0ubuntu1
log/dpkg.log;2015-03-05 23:09:41 status half-configured bamfdaemon:amd64 0.5.1+14.04.20140409-0ubuntu1
log/dpkg.log;2015-03-05 23:09:41 status installed bamfdaemon:amd64 0.5.1+14.04.20140409-0ubuntu1
log/dpkg.log;2015-03-05 23:09:41 trigproc mime-support:all 3.54ubuntu1.1 3.54ubuntu1.1
log/dpkg.log;2015-03-05 23:09:41 status half-configured mime-support:all 3.54ubuntu1.1
log/dpkg.log;2015-03-05 23:09:42 status installed mime-support:all 3.54ubuntu1.1
log/dpkg.log;2015-03-05 23:09:42 trigproc hicolor-icon-theme:all 0.13-1 0.13-1
log/dpkg.log;2015-03-05 23:09:42 status half-configured hicolor-icon-theme:all 0.13-1
log/dpkg.log;2015-03-05 23:09:44 status installed hicolor-icon-theme:all 0.13-1
log/dpkg.log;2015-03-05 23:09:45 startup packages configure
log/dpkg.log;2015-03-05 23:09:45 configure chromium-browser:amd64 40.0.2214.111-0ubuntu0.14.04.1.1069 <none>
log/dpkg.log;2015-03-05 23:09:45 status unpacked chromium-browser:amd64 40.0.2214.111-0ubuntu0.14.04.1.1069
log/dpkg.log;2015-03-05 23:09:45 status unpacked chromium-browser:amd64 40.0.2214.111-0ubuntu0.14.04.1.1069
log/dpkg.log;2015-03-05 23:09:45 status unpacked chromium-browser:amd64 40.0.2214.111-0ubuntu0.14.04.1.1069
log/dpkg.log;2015-03-05 23:09:45 status half-configured chromium-browser:amd64 40.0.2214.111-0ubuntu0.14.04.1.1069
log/dpkg.log;2015-03-05 23:09:45 status installed chromium-browser:amd64 40.0.2214.111-0ubuntu0.14.04.1.1069
log/dpkg.log;2015-03-05 23:09:45 configure chromium-browser-l10n:all 40.0.2214.111-0ubuntu0.14.04.1.1069 <none>
log/dpkg.log;2015-03-05 23:09:45 status unpacked chromium-browser-l10n:all 40.0.2214.111-0ubuntu0.14.04.1.1069
log/dpkg.log;2015-03-05 23:09:45 status half-configured chromium-browser-l10n:all 40.0.2214.111-0ubuntu0.14.04.1.1069
log/dpkg.log;2015-03-05 23:09:45 status installed chromium-browser-l10n:all 40.0.2214.111-0ubuntu0.14.04.1.1069
log/VBoxGuestAdditions.log;
log/VBoxGuestAdditions.log;Starting the VirtualBox Guest Additions ...done.
log/VBoxGuestAdditions.log;Starting VirtualBox Guest Addition service  ...done.
./get-logfiles.sh: line 28: cls: command not found
Let's put that in the database
Enter password:
u64@u64-VirtualBox:~/Desktop$
```

- Look for the ```logs``` table

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

mysql>
```
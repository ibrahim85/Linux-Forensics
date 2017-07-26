#### 39. Mounting Images: Extracting Login Information

###### last, lastb - show a listing of last logged in users

```sh
u64@u64-VirtualBox:~/Desktop$ last
u64      pts/10       10.0.0.95        Wed Jul 26 11:29   still logged in
u64      pts/9        10.0.0.95        Wed Jul 26 11:24   still logged in
u64      pts/8        10.0.0.95        Wed Jul 26 11:22 - 11:29  (00:06)
reboot   system boot  4.8.0-36-generic Tue Jul 25 22:48   still running
u64      pts/8        10.0.0.95        Wed Jul 26 11:19 - 11:22  (00:03)
reboot   system boot  4.8.0-36-generic Tue Jul 25 22:44   still running
u64      pts/21       10.0.0.95        Wed Jul 26 09:52 - 11:18  (01:26)
u64      pts/20       10.0.0.95        Tue Jul 25 23:59 - 11:18  (11:19)
u64      tty7         :0               Tue Jul 25 17:41 - down   (17:37)
u64      pts/9        10.0.0.95        Tue Jul 25 16:30 - 11:18  (18:48)
u64      pts/8        10.0.0.95        Tue Jul 25 16:29 - 11:18  (18:49)
reboot   system boot  4.8.0-36-generic Tue Jul 25 16:28 - 11:18  (18:50)
u64      pts/8        10.0.0.95        Tue Jul 25 16:19 - 16:28  (00:08)
reboot   system boot  4.8.0-36-generic Tue Jul 25 16:19 - 16:28  (00:09)
u64      pts/18       10.0.0.95        Tue Jul 25 16:09 - 16:19  (00:10)
u64      pts/17       10.0.0.95        Tue Jul 25 15:58 - 16:19  (00:20)
u64      tty7         :0               Tue Jul 25 15:58 - down   (00:20)
reboot   system boot  4.8.0-36-generic Tue Jul 25 15:58 - 16:19  (00:20)
u64      pts/19       10.0.0.95        Tue Jul 25 15:10 - 15:31  (00:21)
u64      pts/4        10.0.0.95        Tue Jul 25 15:00 - 15:58  (00:57)
u64      tty7         :0               Tue Jul 25 14:58 - crash  (00:59)
reboot   system boot  4.8.0-36-generic Tue Jul 25 14:58 - 16:19  (01:20)

wtmp begins Tue Jul 25 14:58:43 2017
u64@u64-VirtualBox:~/Desktop$
```

```
u64@u64-VirtualBox:~/Desktop$ man last
<---snip--->
       -F, --fulltimes
              Print full login and logout times and dates.

       -a, --hostlast
              Display the hostname in the last column. Useful in combination with the --dns option.

       -i, --ip
              Like --dns, but displays the host's IP number instead of the name.

       -w, --fullnames
              Display full user names and domain names in the output.

       -x, --system
              Display the system shutdown entries and run level changes.
<---snip--->
``` 

```sh
u64@u64-VirtualBox:~/Desktop$ last -Faiwx
u64      pts/10       Wed Jul 26 11:29:01 2017   still logged in                       10.0.0.95
u64      pts/9        Wed Jul 26 11:24:16 2017   still logged in                       10.0.0.95
u64      pts/8        Wed Jul 26 11:22:40 2017 - Wed Jul 26 11:29:01 2017  (00:06)     10.0.0.95
runlevel (to lvl 5)   Wed Jul 26 11:22:32 2017   still running                         0.0.0.0
reboot   system boot  Tue Jul 25 22:48:13 2017   still running                         0.0.0.0
u64      pts/8        Wed Jul 26 11:19:08 2017 - Wed Jul 26 11:22:28 2017  (00:03)     10.0.0.95
runlevel (to lvl 5)   Wed Jul 26 11:18:57 2017 - Wed Jul 26 11:22:32 2017  (00:03)     0.0.0.0
reboot   system boot  Tue Jul 25 22:44:38 2017   still running                         0.0.0.0
shutdown system down  Wed Jul 26 11:18:54 2017 - Tue Jul 25 22:44:38 2017  (-12:-34)   0.0.0.0
u64      pts/21       Wed Jul 26 09:52:46 2017 - Wed Jul 26 11:18:52 2017  (01:26)     10.0.0.95
u64      pts/20       Tue Jul 25 23:59:37 2017 - Wed Jul 26 11:18:52 2017  (11:19)     10.0.0.95
u64      tty7         Tue Jul 25 17:41:20 2017 - down                      (17:37)     0.0.0.0
u64      pts/9        Tue Jul 25 16:30:17 2017 - Wed Jul 26 11:18:53 2017  (18:48)     10.0.0.95
u64      pts/8        Tue Jul 25 16:29:04 2017 - Wed Jul 26 11:18:53 2017  (18:49)     10.0.0.95
runlevel (to lvl 5)   Tue Jul 25 16:28:33 2017 - Wed Jul 26 11:18:54 2017  (18:50)     0.0.0.0
reboot   system boot  Tue Jul 25 16:28:30 2017 - Wed Jul 26 11:18:54 2017  (18:50)     0.0.0.0
shutdown system down  Tue Jul 25 16:28:21 2017 - Tue Jul 25 16:28:30 2017  (00:00)     0.0.0.0
u64      pts/8        Tue Jul 25 16:19:28 2017 - Tue Jul 25 16:28:21 2017  (00:08)     10.0.0.95
runlevel (to lvl 5)   Tue Jul 25 16:19:22 2017 - Tue Jul 25 16:28:21 2017  (00:08)     0.0.0.0
reboot   system boot  Tue Jul 25 16:19:19 2017 - Tue Jul 25 16:28:21 2017  (00:09)     0.0.0.0
shutdown system down  Tue Jul 25 16:19:10 2017 - Tue Jul 25 16:19:19 2017  (00:00)     0.0.0.0
u64      pts/18       Tue Jul 25 16:09:05 2017 - Tue Jul 25 16:19:10 2017  (00:10)     10.0.0.95
u64      pts/17       Tue Jul 25 15:58:59 2017 - Tue Jul 25 16:19:10 2017  (00:20)     10.0.0.95
u64      tty7         Tue Jul 25 15:58:52 2017 - down                      (00:20)     0.0.0.0
runlevel (to lvl 5)   Tue Jul 25 15:58:46 2017 - Tue Jul 25 16:19:10 2017  (00:20)     0.0.0.0
reboot   system boot  Tue Jul 25 15:58:43 2017 - Tue Jul 25 16:19:10 2017  (00:20)     0.0.0.0
u64      pts/19       Tue Jul 25 15:10:45 2017 - Tue Jul 25 15:31:49 2017  (00:21)     10.0.0.95
u64      pts/4        Tue Jul 25 15:00:36 2017 - Tue Jul 25 15:58:33 2017  (00:57)     10.0.0.95
u64      tty7         Tue Jul 25 14:58:50 2017 - crash                     (00:59)     0.0.0.0
runlevel (to lvl 5)   Tue Jul 25 14:58:45 2017 - Tue Jul 25 15:58:46 2017  (01:00)     0.0.0.0
reboot   system boot  Tue Jul 25 14:58:43 2017 - Tue Jul 25 16:19:10 2017  (01:20)     0.0.0.0

wtmp begins Tue Jul 25 14:58:43 2017
u64@u64-VirtualBox:~/Desktop$
```

###### ```get-logins.sh```

```sh
#!/bin/bash
# Simple script to get all successful and unsuccessful
# login attempts and optionally store them in a database.
#
# by Dr. Phil Polstra (@ppolstra) as developed for
# PentesterAcademy.com.

usage () {
	echo "usage: $0 <mount point of root> [database name]"
	echo "Simple script to get logs of successful and unsucessful logins."
        echo "Results may be optionally stored in a database"
	exit 1
}

if [ $# -1t 1 ] ; then
   usage
fi

# use the last and lastb commands to display information
# use awk to create ; separated fields
# use sed to strip white space
echo "who-what;terminal-event;start;stop;elapsedTime;ip" | tee /tmp/logins.csv
last -aiFwx -f $1/var/log/wtmp | \
  awk '{print substr($0, 1, 8) ";" substr($0, 10, 13) ";" substr($0, 23, 24) ";" substr($0, 50, 24) ";" substr($0, 75, 12) ";" substr($0, 88, 15)}' \
  | sed 's/[[:space:]]*;/;/g' | sed 's/[[:space:]]+\n/\n/' \
  | tee -a /tmp/logins.csv

echo "who-what;terminal-event;start;stop;elapsedTime;ip" | tee /tmp/login-fails.csv
lastb -aiFwx -f $1/var/log/btmp | \
  awk '{print substr($0, 1, 8) ";" substr($0, 10, 13) ";" substr($0, 23, 24) ";" substr($0, 50, 24) ";" substr($0, 75, 12) ";" substr($0, 88, 15)}' \
  | sed 's/[[:space:]]*;/;/g' | sed 's/[[:space:]]+\n/\n/' \
  | tee -a /tmp/login-fails.csv

if [ $# -gt 1 ] ; then
chown mysql:mysql /tmp/logins.csv
chown mysql:mysql /tmp/login-fails.csv
cat << EOF | mysql $2 -u root -p
create table logins (
   who_what varchar(8),
   terminal_event varchar(13),
   start datetime,
   stop datetime,
   elapsed varchar(12),
   ip varchar(15),
   recno bigint not null auto_increment,
   primary key(recno)
);

load data local infile "/tmp/logins.csv"
   into table logins
   fields terminated by ';'
   enclosed by '"'
   lines terminated by '\n'
   ignore 1 rows
   (who_what, terminal_event, @start, @stop, elapsed, ip)
   set start=str_to_date(@start, "%a %b %e %H:%i:%s %Y"),
       stop=str_to_date(@stop, "%a %b %e %H:%i:%s %Y");

create table login_fails (
   who_what varchar(8),
   terminal_event varchar(13),
   start datetime,
   stop datetime,
   elapsed varchar(12),
   ip varchar(15),
   recno bigint not null auto_increment,
   primary key(recno)
);

load data local infile "/tmp/login-fails.csv"
   into table login_fails
   fields terminated by ';'
   enclosed by '"'
   lines terminated by '\n'
   ignore 1 rows
   (who_what, terminal_event, @start, @stop, elapsed, ip)
   set start=str_to_date(@start, "%a %b %e %H:%i:%s %Y"),
       stop=str_to_date(@stop, "%a %b %e %H:%i:%s %Y");
EOF

fi
```

###### Mount the image

```sh
u64@u64-VirtualBox:~/Desktop$ sudo ./mount-image.py 2015-3-9.img
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

###### Import successful/unsuccessful login information into the database

```sh
u64@u64-VirtualBox:~/Desktop$ sudo ./get-logins.sh /media/part0 case-2015-3-9
./get-logins.sh: line 15: [: -1t: binary operator expected
who-what;terminal-event;start;stop;elapsedTime;ip
john;pts/12;Thu Mar 12 10:36:39 2015;gone - no logout;;0.0.0.0
john;:0;Thu Mar 12 10:36:06 2015;gone - no logout;;0.0.0.0
runlevel;(to lvl 2);Thu Mar 12 10:35:46 2015;still running;;0.0.0.0
reboot;system boot;Thu Mar 12 10:35:46 2015;still running;;0.0.0.0
john;pts/9;Wed Mar 11 07:10:27 2015;Wed Mar 11 07:18:23 2015; (00:07);0.0.0.0
john;:0;Wed Mar 11 07:09:48 2015;crash;(1+03:25);0.0.0.0
runlevel;(to lvl 2);Wed Mar 11 07:09:33 2015;Thu Mar 12 10:35:46 2015;(1+03:26);0.0.0.0
reboot;system boot;Wed Mar 11 07:09:33 2015;still running;;0.0.0.0
shutdown;system down;Wed Mar 11 07:08:43 2015;Wed Mar 11 07:09:33 2015; (00:00);0.0.0.0
runlevel;(to lvl 0);Wed Mar 11 07:08:40 2015;Wed Mar 11 07:08:43 2015; (00:00);0.0.0.0
john;pts/11;Wed Mar 11 06:56:18 2015;Wed Mar 11 07:08:19 2015; (00:12);0.0.0.0
john;:0;Wed Mar 11 06:55:46 2015;down; (00:12);0.0.0.0
runlevel;(to lvl 2);Wed Mar 11 06:55:20 2015;Wed Mar 11 07:08:40 2015; (00:13);0.0.0.0
reboot;system boot;Wed Mar 11 06:55:20 2015;Wed Mar 11 07:08:40 2015; (00:13);0.0.0.0
john;pts/12;Mon Mar  9 18:49:10 2015;crash;(1+12:06);0.0.0.0
john;:0;Mon Mar  9 18:48:38 2015;crash;(1+12:06);0.0.0.0
runlevel;(to lvl 2);Mon Mar  9 18:48:01 2015;Wed Mar 11 06:55:20 2015;(1+12:07);0.0.0.0
reboot;system boot;Mon Mar  9 18:48:01 2015;Wed Mar 11 07:08:40 2015;(1+12:20);0.0.0.0
johnn;pts/25;Mon Mar  9 18:34:45 2015;Mon Mar  9 18:38:50 2015; (00:04);192.168.56.1
lightdm;pts/25;Mon Mar  9 18:34:01 2015;Mon Mar  9 18:34:36 2015; (00:00);192.168.56.1
lightdm;pts/25;Mon Mar  9 18:33:16 2015;Mon Mar  9 18:33:16 2015; (00:00);192.168.56.1
johnn;pts/25;Mon Mar  9 18:29:39 2015;Mon Mar  9 18:33:05 2015; (00:03);192.168.56.1
john;pts/23;Mon Mar  9 18:24:49 2015;Mon Mar  9 18:44:23 2015; (00:19);192.168.56.1
john;pts/0;Mon Mar  9 18:10:45 2015;Mon Mar  9 18:44:43 2015; (00:33);0.0.0.0
john;pts/0;Mon Mar  9 18:03:15 2015;Mon Mar  9 18:08:11 2015; (00:04);0.0.0.0
john;:0;Mon Mar  9 17:59:56 2015;Mon Mar  9 18:44:43 2015; (00:44);0.0.0.0
runlevel;(to lvl 2);Mon Mar  9 17:58:55 2015;Mon Mar  9 18:48:01 2015; (00:49);0.0.0.0
reboot;system boot;Mon Mar  9 17:58:55 2015;Wed Mar 11 07:08:40 2015;(1+13:09);0.0.0.0
shutdown;system down;Sun Mar  8 17:51:50 2015;Mon Mar  9 17:58:55 2015;(1+00:07);0.0.0.0
runlevel;(to lvl 0);Sun Mar  8 17:51:46 2015;Sun Mar  8 17:51:50 2015; (00:00);0.0.0.0
john;pts/0;Sun Mar  8 17:42:33 2015;Sun Mar  8 17:51:38 2015; (00:09);0.0.0.0
john;pts/13;Sun Mar  8 17:28:15 2015;Sun Mar  8 17:40:06 2015; (00:11);0.0.0.0
john;:0;Sun Mar  8 17:27:43 2015;down; (00:24);0.0.0.0
runlevel;(to lvl 2);Sun Mar  8 17:27:24 2015;Sun Mar  8 17:51:46 2015; (00:24);0.0.0.0
reboot;system boot;Sun Mar  8 17:27:24 2015;Sun Mar  8 17:51:46 2015; (00:24);0.0.0.0
shutdown;system down;Fri Mar  6 18:33:02 2015;Sun Mar  8 17:27:24 2015;(1+21:54);0.0.0.0
runlevel;(to lvl 0);Fri Mar  6 18:32:49 2015;Fri Mar  6 18:33:02 2015; (00:00);0.0.0.0
john;pts/0;Fri Mar  6 18:25:04 2015;Fri Mar  6 18:32:41 2015; (00:07);0.0.0.0
john;:0;Fri Mar  6 18:23:58 2015;down; (00:08);0.0.0.0
runlevel;(to lvl 2);Fri Mar  6 18:23:13 2015;Fri Mar  6 18:32:49 2015; (00:09);0.0.0.0
reboot;system boot;Fri Mar  6 18:23:13 2015;Fri Mar  6 18:32:49 2015; (00:09);0.0.0.0
shutdown;system down;Fri Mar  6 17:47:16 2015;Fri Mar  6 18:23:13 2015; (00:35);0.0.0.0
runlevel;(to lvl 0);Fri Mar  6 17:47:13 2015;Fri Mar  6 17:47:16 2015; (00:00);0.0.0.0
john;pts/9;Fri Mar  6 17:35:29 2015;Fri Mar  6 17:47:07 2015; (00:11);0.0.0.0
john;:0;Fri Mar  6 17:34:33 2015;down; (00:12);0.0.0.0
runlevel;(to lvl 2);Fri Mar  6 17:31:30 2015;Fri Mar  6 17:47:13 2015; (00:15);0.0.0.0
reboot;system boot;Fri Mar  6 17:31:30 2015;Fri Mar  6 17:47:13 2015; (00:15);0.0.0.0
shutdown;system down;Fri Mar  6 17:30:38 2015;Fri Mar  6 17:31:30 2015; (00:00);0.0.0.0
runlevel;(to lvl 0);Fri Mar  6 17:30:35 2015;Fri Mar  6 17:30:38 2015; (00:00);0.0.0.0
john;pts/12;Fri Mar  6 17:23:44 2015;down; (00:06);0.0.0.0
john;:0;Fri Mar  6 17:23:06 2015;down; (00:07);0.0.0.0
runlevel;(to lvl 2);Fri Mar  6 17:19:39 2015;Fri Mar  6 17:30:35 2015; (00:10);0.0.0.0
reboot;system boot;Fri Mar  6 17:19:39 2015;Fri Mar  6 17:30:35 2015; (00:10);0.0.0.0
shutdown;system down;Fri Mar  6 06:25:54 2015;Fri Mar  6 17:19:39 2015; (10:53);0.0.0.0
runlevel;(to lvl 0);Fri Mar  6 06:25:52 2015;Fri Mar  6 06:25:54 2015; (00:00);0.0.0.0
john;pts/12;Fri Mar  6 05:50:35 2015;down; (00:35);0.0.0.0
john;:0;Fri Mar  6 05:50:03 2015;down; (00:35);0.0.0.0
runlevel;(to lvl 2);Fri Mar  6 05:49:13 2015;Fri Mar  6 06:25:52 2015; (00:36);0.0.0.0
reboot;system boot;Fri Mar  6 05:49:13 2015;Fri Mar  6 06:25:52 2015; (00:36);0.0.0.0
shutdown;system down;Thu Mar  5 20:12:23 2015;Fri Mar  6 05:49:13 2015; (09:36);0.0.0.0
runlevel;(to lvl 0);Thu Mar  5 20:12:19 2015;Thu Mar  5 20:12:23 2015; (00:00);0.0.0.0
john;pts/0;Thu Mar  5 20:00:36 2015;down; (00:11);0.0.0.0
john;:0;Thu Mar  5 19:58:25 2015;down; (00:13);0.0.0.0
runlevel;(to lvl 2);Thu Mar  5 19:58:08 2015;Thu Mar  5 20:12:19 2015; (00:14);0.0.0.0
reboot;system boot;Thu Mar  5 19:58:08 2015;Thu Mar  5 20:12:19 2015; (00:14);0.0.0.0
shutdown;system down;Thu Mar  5 19:57:48 2015;Thu Mar  5 19:58:08 2015; (00:00);0.0.0.0
runlevel;(to lvl 6);Thu Mar  5 19:57:44 2015;Thu Mar  5 19:57:48 2015; (00:00);0.0.0.0
john;pts/11;Thu Mar  5 19:56:00 2015;Thu Mar  5 19:57:28 2015; (00:01);0.0.0.0
john;pts/4;Thu Mar  5 19:53:28 2015;down; (00:04);0.0.0.0
john;:0;Thu Mar  5 19:52:31 2015;down; (00:05);0.0.0.0
runlevel;(to lvl 2);Thu Mar  5 19:52:03 2015;Thu Mar  5 19:57:44 2015; (00:05);0.0.0.0
reboot;system boot;Thu Mar  5 19:52:03 2015;Thu Mar  5 19:57:44 2015; (00:05);0.0.0.0
;;;;;
wtmp beg;ns Thu Mar  5; 19:52:03 2015;;;
who-what;terminal-event;start;stop;elapsedTime;ip
lightdm;ssh:notty;Mon Mar  9 18:33:55 2015;Mon Mar  9 18:33:55 2015; (00:00);192.168.56.1
;;;;;
btmp beg;ns Mon Mar  9; 18:33:55 2015;;;
Enter password:
u64@u64-VirtualBox:~/Desktop$
```

###### Observer the 2 new added tables - ```login_fails``` and ```logins```

```sh
u64@u64-VirtualBox:~$ mysql -u root -p
Enter password:
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 10
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
| login_fails             |
| logins                  |
| logs                    |
| timeline                |
| users                   |
+-------------------------+
8 rows in set (0.00 sec)

mysql>
```

- Query ```login_fails``` table

```sh
mysql> select * from login_fails;
+----------+----------------+---------------------+---------------------+----------+--------------+-------+
| who_what | terminal_event | start               | stop                | elapsed  | ip           | recno |
+----------+----------------+---------------------+---------------------+----------+--------------+-------+
| lightdm  | ssh:notty      | 2015-03-09 18:33:55 | 2015-03-09 18:33:55 |  (00:00) | 192.168.56.1 |     1 |
|          |                | NULL                | NULL                |          |              |     2 |
| btmp beg | ns Mon Mar  9  | NULL                | NULL                |          |              |     3 |
+----------+----------------+---------------------+---------------------+----------+--------------+-------+
3 rows in set (0.00 sec)

mysql>
```
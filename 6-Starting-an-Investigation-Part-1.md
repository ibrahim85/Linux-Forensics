###### 6. Starting an Investigation Part 1

###### Has there been an incident?- Open a case file- Talk to the users	- Why did they call you?
	- Why do they think there is a problem?
	- What is known about the potential victim system:		- Normal use 
		- Origins
		- Recent repairs?

###### Documentation

- Write notes in your notebook	- What users said	- What you know about the subject system- Consider taking photos of system and screen if appropriate- You are now ready to consider actually touching the system

###### Mount the known good binaries

- Mount the partition with known good binaries

```sh
u64@ubuntu64:~$ mount
sysfs on /sys type sysfs (rw,nosuid,nodev,noexec,relatime)
proc on /proc type proc (rw,nosuid,nodev,noexec,relatime)
udev on /dev type devtmpfs (rw,nosuid,relatime,size=486344k,nr_inodes=121586,mode=755)
devpts on /dev/pts type devpts (rw,nosuid,noexec,relatime,gid=5,mode=620,ptmxmode=000)
tmpfs on /run type tmpfs (rw,nosuid,noexec,relatime,size=101576k,mode=755)
/dev/sda1 on / type ext4 (rw,relatime,errors=remount-ro,data=ordered)
securityfs on /sys/kernel/security type securityfs (rw,nosuid,nodev,noexec,relatime)
tmpfs on /dev/shm type tmpfs (rw,nosuid,nodev)
tmpfs on /run/lock type tmpfs (rw,nosuid,nodev,noexec,relatime,size=5120k)
tmpfs on /sys/fs/cgroup type tmpfs (ro,nosuid,nodev,noexec,mode=755)
cgroup on /sys/fs/cgroup/systemd type cgroup (rw,nosuid,nodev,noexec,relatime,xattr,release_agent=/lib/systemd/systemd-cgroups-agent,name=systemd)
pstore on /sys/fs/pstore type pstore (rw,nosuid,nodev,noexec,relatime)
cgroup on /sys/fs/cgroup/perf_event type cgroup (rw,nosuid,nodev,noexec,relatime,perf_event)
cgroup on /sys/fs/cgroup/pids type cgroup (rw,nosuid,nodev,noexec,relatime,pids)
cgroup on /sys/fs/cgroup/net_cls,net_prio type cgroup (rw,nosuid,nodev,noexec,relatime,net_cls,net_prio)
cgroup on /sys/fs/cgroup/freezer type cgroup (rw,nosuid,nodev,noexec,relatime,freezer)
cgroup on /sys/fs/cgroup/cpu,cpuacct type cgroup (rw,nosuid,nodev,noexec,relatime,cpu,cpuacct)
cgroup on /sys/fs/cgroup/blkio type cgroup (rw,nosuid,nodev,noexec,relatime,blkio)
cgroup on /sys/fs/cgroup/cpuset type cgroup (rw,nosuid,nodev,noexec,relatime,cpuset)
cgroup on /sys/fs/cgroup/hugetlb type cgroup (rw,nosuid,nodev,noexec,relatime,hugetlb)
cgroup on /sys/fs/cgroup/devices type cgroup (rw,nosuid,nodev,noexec,relatime,devices)
cgroup on /sys/fs/cgroup/memory type cgroup (rw,nosuid,nodev,noexec,relatime,memory)
systemd-1 on /proc/sys/fs/binfmt_misc type autofs (rw,relatime,fd=24,pgrp=1,timeout=0,minproto=5,maxproto=5,direct,pipe_ino=11024)
hugetlbfs on /dev/hugepages type hugetlbfs (rw,relatime)
mqueue on /dev/mqueue type mqueue (rw,relatime)
debugfs on /sys/kernel/debug type debugfs (rw,relatime)
configfs on /sys/kernel/config type configfs (rw,relatime)
fusectl on /sys/fs/fuse/connections type fusectl (rw,relatime)
binfmt_misc on /proc/sys/fs/binfmt_misc type binfmt_misc (rw,relatime)
/dev/sda1 on /var/lib/docker/aufs type ext4 (rw,relatime,errors=remount-ro,data=ordered)
tmpfs on /run/user/1000 type tmpfs (rw,nosuid,nodev,relatime,size=101576k,mode=700,uid=1000,gid=1000)
gvfsd-fuse on /run/user/1000/gvfs type fuse.gvfsd-fuse (rw,nosuid,nodev,relatime,user_id=1000,group_id=1000)
/dev/sdb2 on /media/u64/14b51e12-ed3f-41e7-9f91-af3717576fc1 type ext3 (rw,nosuid,nodev,relatime,data=ordered,uhelper=udisks2)
u64@ubuntu64:~$
```

```sh
u64@ubuntu64:~$ sudo mkdir /mnt/x64
[sudo] password for u64:
u64@ubuntu64:~$
```

```sh
u64@ubuntu64:~$ sudo mount /dev/sdb2 /mnt/x64/
```

```sh
u64@ubuntu64:~$ cd /mnt/x64/x64/
u64@ubuntu64:/mnt/x64/x64$ ls
bin  sbin
u64@ubuntu64:/mnt/x64/x64$
```

- Run known ```good shell```

```sh
u64@ubuntu64:/mnt/x64/x64$ exec bin/bash
```

- Set ```PATH``` to only point to your directories

```sh
u64@ubuntu64:/mnt/x64/x64$ export PATH=/mnt/x64/x64/bin:/mnt/x64/x64/sbin
```

- Reset ```LD_LIBRARY_PATH```

```sh
u64@ubuntu64:/mnt/x64/x64$ export LD_LIBRARY_PATH=/mnt/x64/x64/lib:/mnt/x64/x64/lib64
```

```sh
u64@ubuntu64:/mnt/x64/x64/sbin$ ./ifconfig
docker0   Link encap:Ethernet  HWaddr 02:42:7d:09:40:b7
          inet addr:172.17.0.1  Bcast:0.0.0.0  Mask:255.255.0.0
          UP BROADCAST MULTICAST  MTU:1500  Metric:1
          RX packets:0 errors:0 dropped:0 overruns:0 frame:0
          TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0
          RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)

enp0s3    Link encap:Ethernet  HWaddr 08:00:27:80:dd:f2
          inet addr:10.0.0.60  Bcast:10.0.0.255  Mask:255.255.255.0
          inet6 addr: 2601:644:8501:6c87:fd26:8a:31af:36ee/64 Scope:Global
          inet6 addr: 2601:644:8501:6c87::5b7d/128 Scope:Global
          inet6 addr: 2601:644:8501:6c87:313f:915e:aa93:bbf1/64 Scope:Global
          inet6 addr: fe80::9cae:2da6:14e9:5201/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:8592 errors:0 dropped:0 overruns:0 frame:0
          TX packets:5740 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000
          RX bytes:1037200 (1.0 MB)  TX bytes:589177 (589.1 KB)

lo        Link encap:Local Loopback
          inet addr:127.0.0.1  Mask:255.0.0.0
          inet6 addr: ::1/128 Scope:Host
          UP LOOPBACK RUNNING  MTU:65536  Metric:1
          RX packets:5406 errors:0 dropped:0 overruns:0 frame:0
          TX packets:5406 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1
          RX bytes:467462 (467.4 KB)  TX bytes:467462 (467.4 KB)

u64@ubuntu64:/mnt/x64/x64/sbin$
```
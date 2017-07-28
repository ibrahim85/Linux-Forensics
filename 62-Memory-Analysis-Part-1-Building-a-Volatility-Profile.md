#### 62. Memory Analysis Part 1: Building a Volatility Profile

###### Mount the image

```sh
u64@u64-VirtualBox:~/Desktop/code$ sudo ./mount-image.py ../2015-3-9.img
Looks like a MBR or VBR
Must be a MBR
Bootable:Type 131:Start 2048:Total sectors 33552384
Type 5:Start 33556478:Total sectors 4190210
Sorry GPT and extended partitions are not supported by this script!
<empty>
<empty>
u64@u64-VirtualBox:~/Desktop/code$
```

```sh
u64@u64-VirtualBox:~/Desktop/code$ mount
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
cgroup on /sys/fs/cgroup/blkio type cgroup (rw,nosuid,nodev,noexec,relatime,blkio)
cgroup on /sys/fs/cgroup/cpuset type cgroup (rw,nosuid,nodev,noexec,relatime,cpuset)
cgroup on /sys/fs/cgroup/net_cls,net_prio type cgroup (rw,nosuid,nodev,noexec,relatime,net_cls,net_prio)
cgroup on /sys/fs/cgroup/pids type cgroup (rw,nosuid,nodev,noexec,relatime,pids)
cgroup on /sys/fs/cgroup/freezer type cgroup (rw,nosuid,nodev,noexec,relatime,freezer)
cgroup on /sys/fs/cgroup/perf_event type cgroup (rw,nosuid,nodev,noexec,relatime,perf_event)
cgroup on /sys/fs/cgroup/memory type cgroup (rw,nosuid,nodev,noexec,relatime,memory)
cgroup on /sys/fs/cgroup/cpu,cpuacct type cgroup (rw,nosuid,nodev,noexec,relatime,cpu,cpuacct)
cgroup on /sys/fs/cgroup/hugetlb type cgroup (rw,nosuid,nodev,noexec,relatime,hugetlb)
systemd-1 on /proc/sys/fs/binfmt_misc type autofs (rw,relatime,fd=31,pgrp=1,timeout=0,minproto=5,maxproto=5,direct,pipe_ino=10883)
debugfs on /sys/kernel/debug type debugfs (rw,relatime)
mqueue on /dev/mqueue type mqueue (rw,relatime)
hugetlbfs on /dev/hugepages type hugetlbfs (rw,relatime)
fusectl on /sys/fs/fuse/connections type fusectl (rw,relatime)
tmpfs on /run/user/1000 type tmpfs (rw,nosuid,nodev,relatime,size=101576k,mode=700,uid=1000,gid=1000)
gvfsd-fuse on /run/user/1000/gvfs type fuse.gvfsd-fuse (rw,nosuid,nodev,relatime,user_id=1000,group_id=1000)
/home/u64/Desktop/2015-3-9.img on /media/part0 type ext4 (ro,noatime,data=ordered)
u64@u64-VirtualBox:~/Desktop/code$
```

###### Create a ```Volatility``` profile from a mounted image file

```
$ sudo apt-get install volatility
```

```sh
u64@u64-VirtualBox:~/Desktop/vol-profile$ ll
total 1812
drwxr-xr-x 2 u64 u64    4096 Jul 27 13:38 ./
drwxr-xr-x 5 u64 u64    4096 Jul 27 13:37 ../
-rwxrwxr-x 1 u64 u64    1045 Apr 28  2015 create-profile.sh*
-rw-r--r-- 1 u64 u64     385 Apr 28  2015 Makefile
-rw-rw-r-- 1 u64 u64     558 Apr 28  2015 Makefile.3.16.0-30-generic
-rw-r--r-- 1 u64 u64   15571 Apr 28  2015 module.c
-rw-rw-r-- 1 u64 u64 1818239 Apr 28  2015 module.dwarf
u64@u64-VirtualBox:~/Desktop/vol-profile$
```

```sh
u64@u64-VirtualBox:~/Desktop/vol-profile$ ./create-profile.sh
Script to create a Volatility profile from a mounted image file
Usage: ./create-profile.sh <path to image root>
u64@u64-VirtualBox:~/Desktop/vol-profile$
```

```sh
u64@u64-VirtualBox:~/Desktop/vol-profile$ ./create-profile.sh /media/part0/
Version: 3.16.0-30-generic
/usr/bin/make -C /media/part0//lib/modules/3.16.0-30-generic/build CONFIG_DEBUG_INFO=y M="/home/u64/Desktop/vol-profile" modules
make[1]: Entering directory '/usr/src/linux-headers-3.16.0-30-generic'
  CC [M]  /home/u64/Desktop/vol-profile/module.o
  Building modules, stage 2.
  MODPOST 1 modules
  CC      /home/u64/Desktop/vol-profile/module.mod.o
  LD [M]  /home/u64/Desktop/vol-profile/module.ko
make[1]: Leaving directory '/usr/src/linux-headers-3.16.0-30-generic'
dwarfdump -di module.ko > module.dwarf
/usr/bin/make -C /media/part0//lib/modules/3.16.0-30-generic/build M="/home/u64/Desktop/vol-profile" clean
make[1]: Entering directory '/usr/src/linux-headers-3.16.0-30-generic'
  CLEAN   /home/u64/Desktop/vol-profile/.tmp_versions
  CLEAN   /home/u64/Desktop/vol-profile/Module.symvers
make[1]: Leaving directory '/usr/src/linux-headers-3.16.0-30-generic'
cp: cannot stat '/media/part0//boot/System.map-{ver}': No such file or directory
	zip warning: name not matched: System.map-{ver}
updating: module.dwarf (deflated 89%)
u64@u64-VirtualBox:~/Desktop/vol-profile$
```

```sh
u64@u64-VirtualBox:~/Desktop/vol-profile$ ll
total 2000
drwxr-xr-x 2 u64 u64    4096 Jul 27 13:39 ./
drwxr-xr-x 5 u64 u64    4096 Jul 27 13:37 ../
-rwxrwxr-x 1 u64 u64    1045 Apr 28  2015 create-profile.sh*
-rw-rw-r-- 1 u64 u64  191234 Jul 27 13:39 Linux3.16.0-30-generic.zip
-rw-r--r-- 1 u64 u64     385 Apr 28  2015 Makefile
-rw-rw-r-- 1 u64 u64     483 Jul 27 13:39 Makefile.3.16.0-30-generic
-rw-r--r-- 1 u64 u64   15571 Apr 28  2015 module.c
-rw-rw-r-- 1 u64 u64 1818239 Apr 28  2015 module.dwarf
u64@u64-VirtualBox:~/Desktop/vol-profile$
```

```sh
u64@u64-VirtualBox:~/Desktop/vol-profile$ sudo cp Linux3.16.0-30-generic.zip /usr/lib/python2.7/dist-packages/volatility/plugins/overlays/linux/
u64@u64-VirtualBox:~/Desktop/vol-profile$
```

```sh
u64@u64-VirtualBox:~/Desktop/vol-profile$ cd /usr/lib/python2.7/dist-packages/volatility/plugins/overlays/linux/
u64@u64-VirtualBox:/usr/lib/python2.7/dist-packages/volatility/plugins/overlays/linux$ ll
total 416
drwxr-xr-x 2 root root   4096 Jul 27 13:47 ./
drwxr-xr-x 5 root root   4096 Jul 27 13:40 ../
-rw-r--r-- 1 root root  25554 Oct 21  2015 elf.py
-rw-r--r-- 1 root root  29704 Jul 27 13:40 elf.pyc
-rw-r--r-- 1 root root      0 Oct 21  2015 __init__.py
-rw-r--r-- 1 root root    165 Jul 27 13:40 __init__.pyc
-rw-r--r-- 1 root root 191234 Jul 27 13:47 Linux3.16.0-30-generic.zip
-rw-r--r-- 1 root root  79258 Oct 21  2015 linux.py
-rw-r--r-- 1 root root  76799 Jul 27 13:40 linux.pyc
u64@u64-VirtualBox:/usr/lib/python2.7/dist-packages/volatility/plugins/overlays/linux$
```

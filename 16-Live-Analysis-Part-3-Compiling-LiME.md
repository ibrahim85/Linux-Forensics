#### 16. Live Analysis Part 3: Compiling LiME

###### Compiling ```LiME``` for our own ```Kernel```

```sh
u64@u64-VirtualBox:~/Desktop$ git clone https://github.com/504ensicsLabs/LiME.git
Cloning into 'LiME'...
remote: Counting objects: 167, done.
remote: Total 167 (delta 0), reused 0 (delta 0), pack-reused 167
Receiving objects: 100% (167/167), 1.56 MiB | 0 bytes/s, done.
Resolving deltas: 100% (75/75), done.
Checking connectivity... done.
u64@u64-VirtualBox:~/Desktop$
```

```sh
u64@u64-VirtualBox:~/Desktop/LiME$ ll
total 48
drwxrwxr-x 5 u64 u64  4096 Jul 27 15:11 ./
drwxr-xr-x 5 u64 u64  4096 Jul 27 15:11 ../
drwxrwxr-x 2 u64 u64  4096 Jul 27 15:11 doc/
drwxrwxr-x 8 u64 u64  4096 Jul 27 15:11 .git/
-rw-rw-r-- 1 u64 u64   101 Jul 27 15:11 .gitignore
-rw-rw-r-- 1 u64 u64 18027 Jul 27 15:11 LICENSE
-rw-rw-r-- 1 u64 u64  2824 Jul 27 15:11 README.md
drwxrwxr-x 2 u64 u64  4096 Jul 27 15:11 src/
u64@u64-VirtualBox:~/Desktop/LiME$
```

```sh
u64@u64-VirtualBox:~/Desktop/LiME$ ll src/
total 36
drwxrwxr-x 2 u64 u64 4096 Jul 27 15:11 ./
drwxrwxr-x 5 u64 u64 4096 Jul 27 15:11 ../
-rw-rw-r-- 1 u64 u64 2557 Jul 27 15:11 disk.c
-rw-rw-r-- 1 u64 u64 1920 Jul 27 15:11 lime.h
-rw-rw-r-- 1 u64 u64 6614 Jul 27 15:11 main.c
-rw-rw-r-- 1 u64 u64 1661 Jul 27 15:11 Makefile
-rw-rw-r-- 1 u64 u64 1722 Jul 27 15:11 Makefile.sample
-rw-rw-r-- 1 u64 u64 3889 Jul 27 15:11 tcp.c
u64@u64-VirtualBox:~/Desktop/LiME$
```

```sh
u64@u64-VirtualBox:~/Desktop/LiME/src$ uname -a
Linux u64-VirtualBox 4.8.0-36-generic #36~16.04.1-Ubuntu SMP Sun Feb 5 09:39:57 UTC 2017 x86_64 x86_64 x86_64 GNU/Linux
u64@u64-VirtualBox:~/Desktop/LiME/src$
```

```sh
u64@u64-VirtualBox:~/Desktop/LiME/src$ make
make -C /lib/modules/4.8.0-36-generic/build M="/home/u64/Desktop/LiME/src" modules
make[1]: Entering directory '/usr/src/linux-headers-4.8.0-36-generic'
  CC [M]  /home/u64/Desktop/LiME/src/tcp.o
  CC [M]  /home/u64/Desktop/LiME/src/disk.o
  CC [M]  /home/u64/Desktop/LiME/src/main.o
  LD [M]  /home/u64/Desktop/LiME/src/lime.o
  Building modules, stage 2.
  MODPOST 1 modules
  CC      /home/u64/Desktop/LiME/src/lime.mod.o
  LD [M]  /home/u64/Desktop/LiME/src/lime.ko
make[1]: Leaving directory '/usr/src/linux-headers-4.8.0-36-generic'
strip --strip-unneeded lime.ko
mv lime.ko lime-4.8.0-36-generic.ko
u64@u64-VirtualBox:~/Desktop/LiME/src$
```

```sh
u64@u64-VirtualBox:~/Desktop/LiME/src$ ll
total 288
drwxrwxr-x 3 u64 u64  4096 Jul 27 15:12 ./
drwxrwxr-x 5 u64 u64  4096 Jul 27 15:11 ../
-rw-rw-r-- 1 u64 u64  2557 Jul 27 15:11 disk.c
-rw-rw-r-- 1 u64 u64  4112 Jul 27 15:12 disk.o
-rw-rw-r-- 1 u64 u64 52269 Jul 27 15:12 .disk.o.cmd
-rw-rw-r-- 1 u64 u64 11784 Jul 27 15:12 lime-4.8.0-36-generic.ko
-rw-rw-r-- 1 u64 u64  1920 Jul 27 15:11 lime.h
-rw-rw-r-- 1 u64 u64   215 Jul 27 15:12 .lime.ko.cmd
-rw-rw-r-- 1 u64 u64  1634 Jul 27 15:12 lime.mod.c
-rw-rw-r-- 1 u64 u64  3904 Jul 27 15:12 lime.mod.o
-rw-rw-r-- 1 u64 u64 27434 Jul 27 15:12 .lime.mod.o.cmd
-rw-rw-r-- 1 u64 u64 10064 Jul 27 15:12 lime.o
-rw-rw-r-- 1 u64 u64   202 Jul 27 15:12 .lime.o.cmd
-rw-rw-r-- 1 u64 u64  6614 Jul 27 15:11 main.c
-rw-rw-r-- 1 u64 u64  7744 Jul 27 15:12 main.o
-rw-rw-r-- 1 u64 u64 52269 Jul 27 15:12 .main.o.cmd
-rw-rw-r-- 1 u64 u64  1661 Jul 27 15:11 Makefile
-rw-rw-r-- 1 u64 u64  1722 Jul 27 15:11 Makefile.sample
-rw-rw-r-- 1 u64 u64    42 Jul 27 15:12 modules.order
-rw-rw-r-- 1 u64 u64     0 Jul 27 15:12 Module.symvers
-rw-rw-r-- 1 u64 u64  3889 Jul 27 15:11 tcp.c
-rw-rw-r-- 1 u64 u64  3848 Jul 27 15:12 tcp.o
-rw-rw-r-- 1 u64 u64 52258 Jul 27 15:12 .tcp.o.cmd
drwxrwxr-x 2 u64 u64  4096 Jul 27 15:12 .tmp_versions/
u64@u64-VirtualBox:~/Desktop/LiME/src$
```

###### Compiling ```LiME``` for an [old ```Kernel```](https://askubuntu.com/questions/700214/how-do-i-install-an-old-kernel)


- Identify the ```architecture type``` and ```kernel version``` of the target image

```sh
u64@u64-VirtualBox:~/Desktop/code$ sudo ./mount-image.py ../2015-3-9.img
[sudo] password for u64:
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
udev on /dev type devtmpfs (rw,nosuid,relatime,size=484624k,nr_inodes=121156,mode=755)
devpts on /dev/pts type devpts (rw,nosuid,noexec,relatime,gid=5,mode=620,ptmxmode=000)
tmpfs on /run type tmpfs (rw,nosuid,noexec,relatime,size=101380k,mode=755)
/dev/sda1 on / type ext4 (rw,relatime,errors=remount-ro,data=ordered)
securityfs on /sys/kernel/security type securityfs (rw,nosuid,nodev,noexec,relatime)
tmpfs on /dev/shm type tmpfs (rw,nosuid,nodev)
tmpfs on /run/lock type tmpfs (rw,nosuid,nodev,noexec,relatime,size=5120k)
tmpfs on /sys/fs/cgroup type tmpfs (ro,nosuid,nodev,noexec,mode=755)
cgroup on /sys/fs/cgroup/systemd type cgroup (rw,nosuid,nodev,noexec,relatime,xattr,release_agent=/lib/systemd/systemd-cgroups-agent,name=systemd)
pstore on /sys/fs/pstore type pstore (rw,nosuid,nodev,noexec,relatime)
cgroup on /sys/fs/cgroup/perf_event type cgroup (rw,nosuid,nodev,noexec,relatime,perf_event)
cgroup on /sys/fs/cgroup/blkio type cgroup (rw,nosuid,nodev,noexec,relatime,blkio)
cgroup on /sys/fs/cgroup/hugetlb type cgroup (rw,nosuid,nodev,noexec,relatime,hugetlb)
cgroup on /sys/fs/cgroup/cpu,cpuacct type cgroup (rw,nosuid,nodev,noexec,relatime,cpu,cpuacct)
cgroup on /sys/fs/cgroup/cpuset type cgroup (rw,nosuid,nodev,noexec,relatime,cpuset)
cgroup on /sys/fs/cgroup/memory type cgroup (rw,nosuid,nodev,noexec,relatime,memory)
cgroup on /sys/fs/cgroup/freezer type cgroup (rw,nosuid,nodev,noexec,relatime,freezer)
cgroup on /sys/fs/cgroup/net_cls,net_prio type cgroup (rw,nosuid,nodev,noexec,relatime,net_cls,net_prio)
cgroup on /sys/fs/cgroup/pids type cgroup (rw,nosuid,nodev,noexec,relatime,pids)
cgroup on /sys/fs/cgroup/devices type cgroup (rw,nosuid,nodev,noexec,relatime,devices)
systemd-1 on /proc/sys/fs/binfmt_misc type autofs (rw,relatime,fd=34,pgrp=1,timeout=0,minproto=5,maxproto=5,direct,pipe_ino=11954)
mqueue on /dev/mqueue type mqueue (rw,relatime)
hugetlbfs on /dev/hugepages type hugetlbfs (rw,relatime)
debugfs on /sys/kernel/debug type debugfs (rw,relatime)
fusectl on /sys/fs/fuse/connections type fusectl (rw,relatime)
tmpfs on /run/user/1000 type tmpfs (rw,nosuid,nodev,relatime,size=101380k,mode=700,uid=1000,gid=1000)
gvfsd-fuse on /run/user/1000/gvfs type fuse.gvfsd-fuse (rw,nosuid,nodev,relatime,user_id=1000,group_id=1000)
/home/u64/Desktop/2015-3-9.img on /media/part0 type ext4 (ro,noatime,data=ordered)
u64@u64-VirtualBox:~/Desktop/code$
```

```sh
u64@u64-VirtualBox:/media/part0$ file bin/ls
bin/ls: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 2.6.24, BuildID[sha1]=9d2a434c4ff55aad2ddd19348c0ac75971606483, stripped
u64@u64-VirtualBox:/media/part0$
```

```sh
u64@u64-VirtualBox:/media/part0/lib/modules$ ls
3.16.0-30-generic
u64@u64-VirtualBox:/media/part0/lib/modules$
```

- Obtain the ```linux-headers_all```, ```linux-headers_<arch>```, ```linux-image_<arch>```for the target ```kernel```

```sh
u64@u64-VirtualBox:~/lkh/trs$ ll
total 25280
drwxrwxr-x 2 u64 u64     4096 Jul 28 11:06 ./
drwxrwxr-x 3 u64 u64     4096 Jul 28 10:57 ../
-rw-rw-r-- 1 u64 u64  9075824 Jan 16  2015 linux-headers-3.16.0-30_3.16.0-30.40~14.04.1_all.deb
-rw-rw-r-- 1 u64 u64   715838 Jan 16  2015 linux-headers-3.16.0-30-generic_3.16.0-30.40~14.04.1_amd64.deb
-rw-rw-r-- 1 u64 u64 16083042 Jan 16  2015 linux-image-3.16.0-30-generic_3.16.0-30.40~14.04.1_amd64.deb
u64@u64-VirtualBox:~/lkh/trs$
```

```sh
u64@u64-VirtualBox:~/lkh/trs$ sudo dpkg -i *.deb
```

- Compiling ```LiME``` for ```3.16.0-30-generic```

	- Before obtaining the ```kernel-headers```

	```sh
	u64@u64-VirtualBox:/lib/modules$ ls
	4.10.0-27-generic  4.8.0-36-generic
	u64@u64-VirtualBox:/lib/modules$
	```
	
	```sh
	u64@u64-VirtualBox:/usr/src$ ls
	linux-headers-4.10.0-27          linux-headers-4.8.0-36          volatility-tools
	linux-headers-4.10.0-27-generic  linux-headers-4.8.0-36-generic
	u64@u64-VirtualBox:/usr/src$
	```
	
	```sh
	u64@u64-VirtualBox:~/Desktop/LiME/src$ make -C /lib/modules/3.16.0-30-generic/build M=$PWD
	make: Entering directory '/usr/src/linux-headers-3.16.0-30-generic'
	  LD      /home/u64/Desktop/LiME/src/built-in.o
	  CC [M]  /home/u64/Desktop/LiME/src/tcp.o
	  CC [M]  /home/u64/Desktop/LiME/src/disk.o
	  CC [M]  /home/u64/Desktop/LiME/src/main.o
	  LD [M]  /home/u64/Desktop/LiME/src/lime.o
	  Building modules, stage 2.
	  MODPOST 1 modules
	  CC      /home/u64/Desktop/LiME/src/lime.mod.o
	  LD [M]  /home/u64/Desktop/LiME/src/lime.ko
	make: Leaving directory '/usr/src/linux-headers-3.16.0-30-generic'
	u64@u64-VirtualBox:~/Desktop/LiME/src$
	```
	
	```sh
	u64@u64-VirtualBox:~/Desktop/LiME/src$ mv lime.ko lime-3.16.0-30-generic.ho
	```
	
	```sh
	u64@u64-VirtualBox:~/Desktop/LiME/src$ ll
	total 296
	drwxrwxr-x 3 u64 u64  4096 Jul 28 11:55 ./
	drwxrwxr-x 5 u64 u64  4096 Jul 28 11:39 ../
	-rw-rw-r-- 1 u64 u64     8 Jul 28 11:54 built-in.o
	-rw-rw-r-- 1 u64 u64   137 Jul 28 11:54 .built-in.o.cmd
	-rw-rw-r-- 1 u64 u64  2557 Jul 28 11:39 disk.c
	-rw-rw-r-- 1 u64 u64  4080 Jul 28 11:54 disk.o
	-rw-rw-r-- 1 u64 u64 46272 Jul 28 11:54 .disk.o.cmd
	-rw-rw-r-- 1 u64 u64 12480 Jul 28 11:54 lime-3.16.0-30-generic.ho
	-rw-rw-r-- 1 u64 u64 10496 Jul 28 11:40 lime-4.10.0-27-generic.ko
	-rw-rw-r-- 1 u64 u64  1920 Jul 28 11:39 lime.h
	-rw-rw-r-- 1 u64 u64   215 Jul 28 11:54 .lime.ko.cmd
	-rw-rw-r-- 1 u64 u64  1576 Jul 28 11:54 lime.mod.c
	-rw-rw-r-- 1 u64 u64  3552 Jul 28 11:54 lime.mod.o
	-rw-rw-r-- 1 u64 u64 26128 Jul 28 11:54 .lime.mod.o.cmd
	-rw-rw-r-- 1 u64 u64  9816 Jul 28 11:54 lime.o
	-rw-rw-r-- 1 u64 u64   202 Jul 28 11:54 .lime.o.cmd
	-rw-rw-r-- 1 u64 u64  6614 Jul 28 11:39 main.c
	-rw-rw-r-- 1 u64 u64  7624 Jul 28 11:54 main.o
	-rw-rw-r-- 1 u64 u64 46272 Jul 28 11:54 .main.o.cmd
	-rw-rw-r-- 1 u64 u64  1661 Jul 28 11:39 Makefile
	-rw-rw-r-- 1 u64 u64  1722 Jul 28 11:39 Makefile.sample
	-rw-rw-r-- 1 u64 u64    42 Jul 28 11:54 modules.order
	-rw-rw-r-- 1 u64 u64     0 Jul 28 11:39 Module.symvers
	-rw-rw-r-- 1 u64 u64  3889 Jul 28 11:39 tcp.c
	-rw-rw-r-- 1 u64 u64  3720 Jul 28 11:54 tcp.o
	-rw-rw-r-- 1 u64 u64 46261 Jul 28 11:54 .tcp.o.cmd
	drwxrwxr-x 2 u64 u64  4096 Jul 28 11:54 .tmp_versions/
	u64@u64-VirtualBox:~/Desktop/LiME/src$
	```
	
	- After obtaining the ```kernel-headers```
	
	```sh
	u64@u64-VirtualBox:/lib/modules$ ls
	3.16.0-30-generic  4.10.0-27-generic  4.8.0-36-generic
	u64@u64-VirtualBox:/lib/modules$
	```
	
	```sh
	u64@u64-VirtualBox:/usr/src$ ls
	linux-headers-3.16.0-30          linux-headers-4.10.0-27          linux-headers-4.8.0-36          volatility-tools
	linux-headers-3.16.0-30-generic  linux-headers-4.10.0-27-generic  linux-headers-4.8.0-36-generic
	u64@u64-VirtualBox:/usr/src$
	```
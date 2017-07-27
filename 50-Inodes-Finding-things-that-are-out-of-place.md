#### 50. Inodes: Finding things that are out of place

###### Mount the image

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

###### Browse the mounted image

```sh
u64@u64-VirtualBox:~/Desktop/code$ cd /media/part0/
```

```sh
u64@u64-VirtualBox:/media/part0$ ls
bin   cdrom  etc   initrd.img  lib64       media  opt   root  sbin  sys  usr  vmlinuz
boot  dev    home  lib         lost+found  mnt    proc  run   srv   tmp  var
u64@u64-VirtualBox:/media/part0$
```

###### Identify Anomaly

- Print ```inodes```

```sh
u64@u64-VirtualBox:/media/part0$ ls -lahi bin/ | sort -n
total 11M
     2 drwxr-xr-x 23 root root 4.0K Mar  5  2015 ..
655361 drwxr-xr-x  2 root root 4.0K Mar  9  2015 .
655368 -rwxr-xr-x  1 root root 998K Oct  7  2014 bash
655372 -rwxr-xr-x  1 root root  31K Oct 21  2013 bunzip2
655373 -rwxr-xr-x  1 root root 1.9M Nov 14  2013 busybox
655374 -rwxr-xr-x  1 root root  31K Oct 21  2013 bzcat
655375 lrwxrwxrwx  1 root root    6 Mar  5  2015 bzcmp -> bzdiff
655376 -rwxr-xr-x  1 root root 2.1K Oct 21  2013 bzdiff
655377 lrwxrwxrwx  1 root root    6 Mar  5  2015 bzegrep -> bzgrep
655378 -rwxr-xr-x  1 root root 4.8K Oct 21  2013 bzexe
655379 lrwxrwxrwx  1 root root    6 Mar  5  2015 bzfgrep -> bzgrep
655380 -rwxr-xr-x  1 root root 3.6K Oct 21  2013 bzgrep
655381 -rwxr-xr-x  1 root root  31K Oct 21  2013 bzip2
655382 -rwxr-xr-x  1 root root  15K Oct 21  2013 bzip2recover
655383 lrwxrwxrwx  1 root root    6 Mar  5  2015 bzless -> bzmore
655384 -rwxr-xr-x  1 root root 1.3K Oct 21  2013 bzmore
655385 -rwxr-xr-x  1 root root  47K Jan 13  2015 cat
655386 -rwxr-xr-x  1 root root  15K May 23  2013 chacl
655388 -rwxr-xr-x  1 root root  59K Jan 13  2015 chgrp
655389 -rwxr-xr-x  1 root root  55K Jan 13  2015 chmod
655390 -rwxr-xr-x  1 root root  59K Jan 13  2015 chown
655391 -rwxr-xr-x  1 root root  11K Feb 18  2013 chvt
655392 -rwxr-xr-x  1 root root 128K Jan 13  2015 cp
655393 -rwxr-xr-x  1 root root 135K Jan  7  2015 cpio
655394 -rwxr-xr-x  1 root root 119K Feb 19  2014 dash
655395 -rwxr-xr-x  1 root root  59K Jan 13  2015 date
655396 -rwxr-xr-x  1 root root  11K Nov 25  2014 dbus-cleanup-sockets
655397 -rwxr-xr-x  1 root root 424K Nov 25  2014 dbus-daemon
655398 -rwxr-xr-x  1 root root  11K Nov 25  2014 dbus-uuidgen
655399 -rwxr-xr-x  1 root root  55K Jan 13  2015 dd
655402 -rwxr-xr-x  1 root root  96K Jan 13  2015 df
655403 -rwxr-xr-x  1 root root 108K Jan 13  2015 dir
655404 -rwxr-xr-x  1 root root  23K Feb 12  2015 dmesg
655405 lrwxrwxrwx  1 root root    8 Mar  5  2015 dnsdomainname -> hostname
655406 lrwxrwxrwx  1 root root    8 Mar  5  2015 domainname -> hostname
655407 -rwxr-xr-x  1 root root  81K Feb 18  2013 dumpkeys
655408 -rwxr-xr-x  1 root root  31K Jan 13  2015 echo
655409 -rwxr-xr-x  1 root root  47K Jul 16  2013 ed
655410 -rwxr-xr-x  1 root root 180K Jan 18  2014 egrep
655411 -rwxr-xr-x  1 root root 998K Mar  9  2015 false
655413 -rwxr-xr-x  1 root root  11K Feb 18  2013 fgconsole
655414 -rwxr-xr-x  1 root root 136K Jan 18  2014 fgrep
655415 -rwxr-xr-x  1 root root  36K Feb 12  2015 findmnt
655416 -rwxr-xr-x  1 root root  32K Nov 29  2012 fuser
655417 -rwsr-xr-x  1 root root  31K Dec 16  2013 fusermount
655419 -rwxr-xr-x  1 root root  24K May 23  2013 getfacl
655420 -rwxr-xr-x  1 root root 188K Jan 18  2014 grep
655421 -rwxr-xr-x  1 root root 2.3K Jan 10  2014 gunzip
655422 -rwxr-xr-x  1 root root 5.8K Jan 10  2014 gzexe
655423 -rwxr-xr-x  1 root root  92K Jan 10  2014 gzip
655424 -rwxr-xr-x  1 root root  15K Dec 13  2013 hostname
655427 -rwxr-xr-x  1 root root 301K Feb 17  2014 ip
655428 -rwxr-xr-x  1 root root  11K Feb 18  2013 kbd_mode
655430 -rwxr-xr-x  1 root root  23K Feb 10  2015 kill
655431 -rwxr-xr-x  1 root root 151K Apr 10  2014 kmod
655432 -rwxr-xr-x  1 root root 151K Jun 10  2013 less
655433 -rwxr-xr-x  1 root root  11K Jun 10  2013 lessecho
655434 lrwxrwxrwx  1 root root    8 Mar  5  2015 lessfile -> lesspipe
655435 -rwxr-xr-x  1 root root  16K Jun 10  2013 lesskey
655436 -rwxr-xr-x  1 root root 7.6K Jun 10  2013 lesspipe
655438 -rwxr-xr-x  1 root root  55K Jan 13  2015 ln
655439 -rwxr-xr-x  1 root root 109K Feb 18  2013 loadkeys
655441 -rwxr-xr-x  1 root root  48K Feb 16  2014 login
655442 -rwxr-xr-x  1 root root  91K Feb  4  2015 loginctl
655443 -rwxr-xr-x  1 root root  63K Dec 18  2013 lowntfs-3g
655444 -rwxr-xr-x  1 root root 108K Jan 13  2015 ls
655445 -rwxr-xr-x  1 root root  44K Feb 12  2015 lsblk
655446 lrwxrwxrwx  1 root root    4 Mar  5  2015 lsmod -> kmod
655448 -rwxr-xr-x  1 root root  51K Jan 13  2015 mkdir
655449 -rwxr-xr-x  1 root root  35K Jan 13  2015 mknod
655450 -rwxr-xr-x  1 root root  39K Jan 13  2015 mktemp
655451 -rwxr-xr-x  1 root root  39K Feb 12  2015 more
655452 -rwsr-xr-x  1 root root  93K Feb 12  2015 mount
655453 -rwxr-xr-x  1 root root  11K Mar 12  2014 mountpoint
655454 lrwxrwxrwx  1 root root   20 Mar  5  2015 mt -> /etc/alternatives/mt
655455 -rwxr-xr-x  1 root root  68K Jan  7  2015 mt-gnu
655456 -rwxr-xr-x  1 root root 120K Jan 13  2015 mv
655457 -rwxr-xr-x  1 root root 188K Oct  1  2012 nano
655458 lrwxrwxrwx  1 root root   20 Mar  5  2015 nc -> /etc/alternatives/nc
655459 -rwxr-xr-x  1 root root  31K Dec  3  2012 nc.openbsd
655460 lrwxrwxrwx  1 root root   24 Mar  5  2015 netcat -> /etc/alternatives/netcat
655461 -rwxr-xr-x  1 root root 117K Aug  5  2014 netstat
655462 lrwxrwxrwx  1 root root    8 Mar  5  2015 nisdomainname -> hostname
655463 -rwxr-xr-x  1 root root  59K Dec 18  2013 ntfs-3g
655464 -rwxr-xr-x  1 root root  11K Dec 18  2013 ntfs-3g.probe
655465 -rwxr-xr-x  1 root root  67K Dec 18  2013 ntfs-3g.secaudit
655466 -rwxr-xr-x  1 root root  18K Dec 18  2013 ntfs-3g.usermap
655467 -rwxr-xr-x  1 root root  27K Dec 18  2013 ntfscat
655468 -rwxr-xr-x  1 root root  31K Dec 18  2013 ntfsck
655469 -rwxr-xr-x  1 root root  31K Dec 18  2013 ntfscluster
655470 -rwxr-xr-x  1 root root  35K Dec 18  2013 ntfscmp
655471 -rwxr-xr-x  1 root root  22K Dec 18  2013 ntfsdump_logfile
655472 -rwxr-xr-x  1 root root  39K Dec 18  2013 ntfsfix
655473 -rwxr-xr-x  1 root root  55K Dec 18  2013 ntfsinfo
655474 -rwxr-xr-x  1 root root  32K Dec 18  2013 ntfsls
655475 -rwxr-xr-x  1 root root  27K Dec 18  2013 ntfsmftalloc
655476 -rwxr-xr-x  1 root root  31K Dec 18  2013 ntfsmove
655477 -rwxr-xr-x  1 root root  35K Dec 18  2013 ntfstruncate
655478 -rwxr-xr-x  1 root root  43K Dec 18  2013 ntfswipe
655479 lrwxrwxrwx  1 root root    6 Mar  5  2015 open -> openvt
655480 -rwxr-xr-x  1 root root  19K Feb 18  2013 openvt
655489 lrwxrwxrwx  1 root root   14 Mar  5  2015 pidof -> /sbin/killall5
655490 -rwsr-xr-x  1 root root  44K May  7  2014 ping
655491 -rwsr-xr-x  1 root root  44K May  7  2014 ping6
655492 -rwxr-xr-x  1 root root  35K Dec  2  2014 plymouth
655493 -rwxr-xr-x  1 root root  31K Dec  2  2014 plymouth-upstart-bridge
655495 -rwxr-xr-x  1 root root  92K Feb 10  2015 ps
655496 -rwxr-xr-x  1 root root  31K Jan 13  2015 pwd
655497 lrwxrwxrwx  1 root root    4 Mar  5  2015 rbash -> bash
655498 -rwxr-xr-x  1 root root  39K Jan 13  2015 readlink
655499 -rwxr-xr-x  1 root root   89 Jul 16  2013 red
655501 -rwxr-xr-x  1 root root  59K Jan 13  2015 rm
655502 -rwxr-xr-x  1 root root  43K Jan 13  2015 rmdir
655503 lrwxrwxrwx  1 root root    4 Mar  5  2015 rnano -> nano
655504 -rwxr-xr-x  1 root root  19K Aug 27  2013 run-parts
655505 -rwxr-xr-x  1 root root  254 Jul 18  2014 running-in-container
655507 -rwxr-xr-x  1 root root  72K Feb 13  2014 sed
655510 -rwxr-xr-x  1 root root  36K May 23  2013 setfacl
655511 -rwxr-xr-x  1 root root  39K Feb 18  2013 setfont
655512 -rwxr-xr-x  1 root root  12K Jan 29  2014 setupcon
655513 lrwxrwxrwx  1 root root    4 Mar  5  2015 sh -> dash
655514 lrwxrwxrwx  1 root root    4 Mar  5  2015 sh.distrib -> dash
655515 -rwxr-xr-x  1 root root  31K Jan 13  2015 sleep
655516 -rwxr-xr-x  1 root root  75K Feb 17  2014 ss
655517 lrwxrwxrwx  1 root root    7 Mar  5  2015 static-sh -> busybox
655518 -rwxr-xr-x  1 root root  67K Jan 13  2015 stty
655519 -rwsr-xr-x  1 root root  37K Feb 16  2014 su
655520 -rwxr-xr-x  1 root root  27K Jan 13  2015 sync
655522 -rwxr-xr-x  1 root root  19K Feb 12  2015 tailf
655523 -rwxr-xr-x  1 root root 346K Feb  4  2014 tar
655524 -rwxr-xr-x  1 root root  11K Aug 27  2013 tempfile
655525 -rwxr-xr-x  1 root root  59K Jan 13  2015 touch
655526 -rwxr-xr-x  1 root root  27K Jan 13  2015 true
655527 -rwxr-xr-x  1 root root 243K Feb  4  2015 udevadm
655528 -rwxr-xr-x  1 root root  14K Dec 16  2013 ulockmgr_server
655529 -rwsr-xr-x  1 root root  68K Feb 12  2015 umount
655530 -rwxr-xr-x  1 root root  31K Jan 13  2015 uname
655531 -rwxr-xr-x  1 root root 2.3K Jan 10  2014 uncompress
655532 -rwxr-xr-x  1 root root 2.7K Feb 18  2013 unicode_start
655535 -rwxr-xr-x  1 root root 108K Jan 13  2015 vdir
655536 -rwxr-xr-x  1 root root 6.2K Jan 28  2015 vmmouse_detect
655537 -rwxr-xr-x  1 root root  946 Aug 27  2013 which
655538 -rwxr-xr-x  1 root root  27K Mar 23  2014 whiptail
655539 lrwxrwxrwx  1 root root    8 Mar  5  2015 ypdomainname -> hostname
655540 -rwxr-xr-x  1 root root 1.9K Jan 10  2014 zcat
655541 -rwxr-xr-x  1 root root 1.8K Jan 10  2014 zcmp
655542 -rwxr-xr-x  1 root root 5.7K Jan 10  2014 zdiff
655543 -rwxr-xr-x  1 root root  142 Jan 10  2014 zegrep
655544 -rwxr-xr-x  1 root root  142 Jan 10  2014 zfgrep
655545 -rwxr-xr-x  1 root root 2.1K Jan 10  2014 zforce
655546 -rwxr-xr-x  1 root root 5.9K Jan 10  2014 zgrep
655547 -rwxr-xr-x  1 root root 2.0K Jan 10  2014 zless
655548 -rwxr-xr-x  1 root root 1.9K Jan 10  2014 zmore
655549 -rwxr-xr-x  1 root root 5.0K Jan 10  2014 znew
657076 -rwxr-xr-x  1 root root  14K Mar 12  2015 xingyi_reverse_shell
657094 -rwxr-xr-x  1 root root  27K Jun 13  2012 nc.traditional
657103 -rwxr-xr-x  1 root root  15K Mar 12  2015 xingyi_bindshell
657109 -rwxr-xr-x  1 root root 9.5K Mar 12  2015 xingyi_rootshell
u64@u64-VirtualBox:/media/part0$
```

- Sort

```sh
u64@u64-VirtualBox:/media/part0$ ls -lahi sbin/ | sort -n
total 12M
     2 drwxr-xr-x 23 root root   4.0K Mar  5  2015 ..
524291 drwxr-xr-x  2 root root    12K Mar  5  2015 .
524295 -rwxr-xr-x  1 root root    387 Feb 25  2015 ldconfig
524305 -rwxr-xr-x  1 root root   930K Feb 25  2015 ldconfig.real
525304 lrwxrwxrwx  1 root root     57 Mar  5  2015 mount.vboxsf -> /usr/lib/x86_64-linux-gnu/VBoxGuestAdditions/mount.vboxsf
528959 -rwxr-xr-x  1 root root    11K Feb 16  2015 logsave
528981 -rwxr-xr-x  1 root root    31K Feb 16  2015 e2image
528982 -rwxr-xr-x  1 root root    68K Feb 16  2015 tune2fs
528986 -rwxr-xr-x  1 root root    48K Feb 16  2015 resize2fs
528993 -rwxr-xr-x  1 root root    11K Feb 16  2015 e2undo
528994 -rwxr-xr-x  1 root root   243K Feb 16  2015 e2fsck
528995 -rwxr-xr-x  1 root root    23K Feb 16  2015 dumpe2fs
528998 -rwxr-xr-x  1 root root    96K Feb 16  2015 mke2fs
528999 -rwxr-xr-x  1 root root    27K Feb 16  2015 badblocks
529026 -rwxr-xr-x  1 root root   114K Feb 16  2015 debugfs
529045 lrwxrwxrwx  1 root root      6 Feb 16  2015 fsck.ext4dev -> e2fsck
529049 lrwxrwxrwx  1 root root      6 Feb 16  2015 mkfs.ext4dev -> mke2fs
529052 lrwxrwxrwx  1 root root      6 Feb 16  2015 fsck.ext2 -> e2fsck
529061 lrwxrwxrwx  1 root root      6 Feb 16  2015 mkfs.ext3 -> mke2fs
529063 lrwxrwxrwx  1 root root      7 Feb 16  2015 e2label -> tune2fs
529096 lrwxrwxrwx  1 root root      6 Feb 16  2015 mkfs.ext2 -> mke2fs
529104 lrwxrwxrwx  1 root root      6 Feb 16  2015 fsck.ext4 -> e2fsck
529119 lrwxrwxrwx  1 root root      6 Feb 16  2015 mkfs.ext4 -> mke2fs
529248 -rwxr-xr-x  1 root root    52K May 18  2013 MAKEDEV
529249 -rwxr-xr-x  1 root root   6.2K Oct  2  2012 acpi_available
529250 -rwxr-xr-x  1 root root    32K Feb 12  2015 agetty
529251 -rwxr-xr-x  1 root root   5.5K Feb 13  2013 alsa
529252 -rwxr-xr-x  1 root root   6.2K Oct  2  2012 apm_available
529253 -rwxr-xr-x  1 root root   830K Nov 14  2014 apparmor_parser
529255 -rwxr-xr-x  1 root root    31K Feb 12  2015 blkid
529256 -rwxr-xr-x  1 root root    23K Feb 12  2015 blockdev
529257 -rwxr-xr-x  1 root root    51K Feb 17  2014 bridge
529258 -rwxr-xr-x  1 root root   587K Mar 31  2014 brltty
529259 -rwxr-xr-x  1 root root   1.4K Mar 13  2014 brltty-setup
529260 -rwxr-xr-x  1 root root    19K Feb 21  2014 capsh
529261 -rwxr-xr-x  1 root root    54K Feb 12  2015 cfdisk
529262 -rwxr-xr-x  1 root root   168K Dec 26  2013 cgdisk
529263 -rwxr-xr-x  1 root root    15K Oct  1  2012 crda
529268 -rwxr-xr-x  1 root root   6.2K Feb 12  2015 ctrlaltdel
529270 lrwxrwxrwx  1 root root      9 Mar  5  2015 depmod -> /bin/kmod
529271 -rwxr-xr-x  1 root root   1.6M Apr  7  2014 dhclient
529272 -rwxr-xr-x  1 root root    15K Apr  7  2014 dhclient-script
529273 -rwxr-xr-x  1 root root    70K Dec 13  2013 dmsetup
529274 lrwxrwxrwx  1 root root      8 Mar  5  2015 dosfsck -> fsck.fat
529275 lrwxrwxrwx  1 root root      8 Mar  5  2015 dosfslabel -> fatlabel
529281 -rwxr-xr-x  1 root root   252K Jan 29  2014 ethtool
529282 -rwxr-xr-x  1 root root    51K Mar 18  2014 fatlabel
529283 -rwxr-xr-x  1 root root    98K Feb 12  2015 fdisk
529284 -rwxr-xr-x  1 root root   6.2K Feb 12  2015 findfs
529285 -rwxr-xr-x  1 root root    59K Dec 26  2013 fixparts
529287 -rwxr-xr-x  1 root root    31K Feb 12  2015 fsck
529288 -rwxr-xr-x  1 root root    15K Feb 12  2015 fsck.cramfs
529293 -rwxr-xr-x  1 root root    55K Mar 18  2014 fsck.fat
529294 -rwxr-xr-x  1 root root    31K Feb 12  2015 fsck.minix
529295 lrwxrwxrwx  1 root root      8 Mar  5  2015 fsck.msdos -> fsck.fat
529296 -rwxr-xr-x  1 root root    333 Mar 12  2014 fsck.nfs
529297 lrwxrwxrwx  1 root root      8 Mar  5  2015 fsck.vfat -> fsck.fat
529298 -rwxr-xr-x  1 root root    11K Feb 12  2015 fsfreeze
529299 -rwxr-xr-x  1 root root   6.2K Mar 12  2014 fstab-decode
529300 -rwxr-xr-x  1 root root    15K Feb 12  2015 fstrim
529301 -rwxr-xr-x  1 root root   3.0K Feb 12  2015 fstrim-all
529302 -rwxr-xr-x  1 root root   175K Dec 26  2013 gdisk
529303 -rwxr-xr-x  1 root root    11K Feb 21  2014 getcap
529304 -rwxr-xr-x  1 root root   6.2K Feb 21  2014 getpcaps
529305 -rwxr-xr-x  1 root root    32K Feb 12  2015 getty
529306 lrwxrwxrwx  1 root root      6 Mar  5  2015 halt -> reboot
529307 -rwxr-xr-x  1 root root   101K Nov 15  2013 hdparm
529308 -rwxr-xr-x  1 root root    35K Feb 12  2015 hwclock
529309 -rwxr-xr-x  1 root root    67K Aug  5  2014 ifconfig
529310 lrwxrwxrwx  1 root root      4 Mar  5  2015 ifdown -> ifup
529311 lrwxrwxrwx  1 root root      4 Mar  5  2015 ifquery -> ifup
529312 -rwxr-xr-x  1 root root    62K May 12  2014 ifup
529313 -rwxr-xr-x  1 root root   260K Jul 18  2014 init
529314 -rwxr-xr-x  1 root root   189K Apr 11  2014 initctl
529315 lrwxrwxrwx  1 root root      9 Mar  5  2015 insmod -> /bin/kmod
529316 -rwxr-xr-x  1 root root   2.4K Aug 27  2013 installkernel
529317 lrwxrwxrwx  1 root root      7 Mar  5  2015 ip -> /bin/ip
529318 lrwxrwxrwx  1 root root     13 Mar  5  2015 ip6tables -> xtables-multi
529319 lrwxrwxrwx  1 root root     14 Mar  5  2015 ip6tables-apply -> iptables-apply
529320 lrwxrwxrwx  1 root root     13 Mar  5  2015 ip6tables-restore -> xtables-multi
529321 lrwxrwxrwx  1 root root     13 Mar  5  2015 ip6tables-save -> xtables-multi
529322 -rwxr-xr-x  1 root root    19K Aug  5  2014 ipmaddr
529323 lrwxrwxrwx  1 root root     13 Mar  5  2015 iptables -> xtables-multi
529324 -rwxr-xr-x  1 root root   6.9K Jan  8  2014 iptables-apply
529325 lrwxrwxrwx  1 root root     13 Mar  5  2015 iptables-restore -> xtables-multi
529326 lrwxrwxrwx  1 root root     13 Mar  5  2015 iptables-save -> xtables-multi
529327 -rwxr-xr-x  1 root root    23K Aug  5  2014 iptunnel
529328 -rwxr-xr-x  1 root root    15K Feb 12  2015 isosize
529329 -rwxr-xr-x  1 root root   105K May 24  2012 iw
529330 -rwxr-xr-x  1 root root    27K May  3  2012 iwconfig
529331 -rwxr-xr-x  1 root root    15K May  3  2012 iwevent
529332 -rwxr-xr-x  1 root root    15K May  3  2012 iwgetid
529333 -rwxr-xr-x  1 root root    35K May  3  2012 iwlist
529334 -rwxr-xr-x  1 root root    15K May  3  2012 iwpriv
529335 -rwxr-xr-x  1 root root    15K May  3  2012 iwspy
529336 -rwxr-xr-x  1 root root    11K Feb 18  2013 kbdrate
529337 lrwxrwxrwx  1 root root      6 Feb 16  2015 fsck.ext3 -> e2fsck
529338 -rwxr-xr-x  1 root root    19K Mar 12  2014 killall5
529342 -rwxr-xr-x  1 root root    43K Feb 12  2015 losetup
529343 lrwxrwxrwx  1 root root      9 Mar  5  2015 lsmod -> /bin/kmod
529344 lrwxrwxrwx  1 root root      9 Mar  5  2015 lspcmcia -> pccardctl
529363 -rwxr-xr-x  1 root root    19K Aug  5  2014 mii-tool
529364 lrwxrwxrwx  1 root root      8 Mar  5  2015 mkdosfs -> mkfs.fat
529366 -rwxr-xr-x  1 root root    11K Feb 12  2015 mkfs
529367 -rwxr-xr-x  1 root root    19K Feb 12  2015 mkfs.bfs
529368 -rwxr-xr-x  1 root root    31K Feb 12  2015 mkfs.cramfs
529373 -rwxr-xr-x  1 root root    27K Mar 18  2014 mkfs.fat
529374 -rwxr-xr-x  1 root root    27K Feb 12  2015 mkfs.minix
529375 lrwxrwxrwx  1 root root      8 Mar  5  2015 mkfs.msdos -> mkfs.fat
529376 lrwxrwxrwx  1 root root      6 Mar  5  2015 mkfs.ntfs -> mkntfs
529377 lrwxrwxrwx  1 root root      8 Mar  5  2015 mkfs.vfat -> mkfs.fat
529378 -rwxr-xr-x  1 root root    19K Jan 31  2014 mkhomedir_helper
529379 -rwxr-xr-x  1 root root    79K Dec 18  2013 mkntfs
529380 -rwxr-xr-x  1 root root    23K Feb 12  2015 mkswap
529381 -rwxr-xr-x  1 root root    31K Feb 21  2014 mntctl
529382 lrwxrwxrwx  1 root root      9 Mar  5  2015 modinfo -> /bin/kmod
529383 lrwxrwxrwx  1 root root      9 Mar  5  2015 modprobe -> /bin/kmod
529386 -rwxr-xr-x  1 root root    10K Dec 16  2013 mount.fuse
529387 lrwxrwxrwx  1 root root     15 Mar  5  2015 mount.lowntfs-3g -> /bin/lowntfs-3g
529388 lrwxrwxrwx  1 root root     13 Mar  5  2015 mount.ntfs -> mount.ntfs-3g
529389 lrwxrwxrwx  1 root root     12 Mar  5  2015 mount.ntfs-3g -> /bin/ntfs-3g
529390 -rwxr-xr-x  1 root root   103K Feb 21  2014 mountall
529391 -rwxr-xr-x  1 root root    15K Aug  5  2014 nameif
529392 -rwxr-xr-x  1 root root    55K Dec 18  2013 ntfsclone
529393 -rwxr-xr-x  1 root root    31K Dec 18  2013 ntfscp
529394 -rwxr-xr-x  1 root root    27K Dec 18  2013 ntfslabel
529395 -rwxr-xr-x  1 root root    71K Dec 18  2013 ntfsresize
529396 -rwxr-xr-x  1 root root    47K Dec 18  2013 ntfsundelete
529397 -rwxr-xr-x  1 root root   2.2K Dec  2  2009 on_ac_power
529398 -rwxr-xr-x  1 root root    11K Jan 31  2014 pam_tally
529399 -rwxr-xr-x  1 root root    15K Jan 31  2014 pam_tally2
529400 -rwxr-xr-x  1 root root    80K Apr 14  2014 parted
529401 -rwxr-xr-x  1 root root    11K Apr 14  2014 partprobe
529402 -rwxr-xr-x  1 root root    19K Jun 28  2012 pccardctl
529403 -rwxr-xr-x  1 root root   6.1K Feb 12  2015 pivot_root
529404 -rwxr-xr-x  1 root root    11K Aug  5  2014 plipconfig
529405 -rwxr-xr-x  1 root root    80K Dec  2  2014 plymouthd
529406 lrwxrwxrwx  1 root root      6 Mar  5  2015 poweroff -> reboot
529416 -rwxr-xr-x  1 root root    30K Aug  5  2014 rarp
529417 -rwxr-xr-x  1 root root    11K Feb 12  2015 raw
529418 -rwxr-xr-x  1 root root    15K Jul 18  2014 reboot
529419 -rwxr-xr-x  1 root root    11K Oct  1  2012 regdbdump
529420 lrwxrwxrwx  1 root root      7 Mar  5  2015 reload -> initctl
529423 -rwxr-xr-x  1 root root   5.5K Jun 13  2014 resolvconf
529424 lrwxrwxrwx  1 root root      7 Mar  5  2015 restart -> initctl
529425 lrwxrwxrwx  1 root root      9 Mar  5  2015 rmmod -> /bin/kmod
529426 -rwxr-xr-x  1 root root    57K Aug  5  2014 route
529427 -rwxr-xr-x  1 root root    35K Feb 17  2014 rtacct
529428 -rwxr-xr-x  1 root root    35K Feb 17  2014 rtmon
529429 -rwxr-xr-x  1 root root    10K Jul 18  2014 runlevel
529431 -rwxr-xr-x  1 root root    11K Feb 21  2014 setcap
529432 -rwxr-xr-x  1 root root    11K Feb 18  2013 setvtrgb
529433 -rwxr-xr-x  1 root root    61K Feb 12  2015 sfdisk
529434 -rwxr-xr-x  1 root root   159K Dec 26  2013 sgdisk
529435 -rwxr-xr-x  1 root root    885 Feb 16  2014 shadowconfig
529436 -rwxr-xr-x  1 root root    83K Jul 18  2014 shutdown
529437 -rwxr-xr-x  1 root root    34K Aug  5  2014 slattach
529438 lrwxrwxrwx  1 root root      7 Mar  5  2015 start -> initctl
529439 -rwxr-xr-x  1 root root    28K Mar  7  2014 start-stop-daemon
529440 -rwxr-xr-x  1 root root    35K Mar 12  2014 startpar
529441 -rwxr-xr-x  1 root root   6.2K Mar 12  2014 startpar-upstart-inject
529442 lrwxrwxrwx  1 root root      7 Mar  5  2015 status -> initctl
529443 lrwxrwxrwx  1 root root      7 Mar  5  2015 stop -> initctl
529444 -rwxr-xr-x  1 root root    15K Mar 12  2014 sulogin
529445 -rwxr-xr-x  1 root root    15K Feb 12  2015 swaplabel
529446 lrwxrwxrwx  1 root root      6 Mar  5  2015 swapoff -> swapon
529447 -rwxr-xr-x  1 root root    27K Feb 12  2015 swapon
529448 -rwxr-xr-x  1 root root    11K Feb 12  2015 switch_root
529449 -rwxr-xr-x  1 root root    23K Feb 10  2015 sysctl
529450 -rwxr-xr-x  1 root root   276K Feb 17  2014 tc
529451 -rwxr-xr-x  1 root root   103K Jul 18  2014 telinit
529453 lrwxrwxrwx  1 root root     12 Mar  5  2015 udevadm -> /bin/udevadm
529454 lrwxrwxrwx  1 root root     26 Mar  5  2015 udevd -> /lib/systemd/systemd-udevd
529457 -rwxr-xr-x  1 root root    11K Mar 10  2014 umount.udisks2
529458 -rwxr-sr-x  1 root shadow  35K Jan 31  2014 unix_chkpwd
529459 -rwxr-xr-x  1 root root    31K Jan 31  2014 unix_update
529460 -rwxr-xr-x  1 root root   131K Jul 18  2014 upstart-dbus-bridge
529461 -rwxr-xr-x  1 root root   123K Jul 18  2014 upstart-event-bridge
529462 -rwxr-xr-x  1 root root   139K Jul 18  2014 upstart-file-bridge
529463 -rwxr-xr-x  1 root root   131K Jul 18  2014 upstart-local-bridge
529464 -rwxr-xr-x  1 root root   131K Jul 18  2014 upstart-socket-bridge
529465 -rwxr-xr-x  1 root root    75K Jul 18  2014 upstart-udev-bridge
529466 -rwxr-xr-x  1 root root    47K Mar 25  2013 ureadahead
529487 -rwxr-xr-x  1 root root    19K Feb 12  2015 wipefs
529488 -rwxr-xr-x  1 root root   1.7K Jan 28  2014 wpa_action
529489 -rwxr-xr-x  1 root root    92K Oct 10  2014 wpa_cli
529490 -rwxr-xr-x  1 root root   1.7M Oct 10  2014 wpa_supplicant
529491 -rwxr-xr-x  1 root root    86K Jan  8  2014 xtables-multi
u64@u64-VirtualBox:/media/part0$
```

- Sort by ```size```

```sh
u64@u64-VirtualBox:/media/part0$ ls -lahiR --sort=size bin/
bin/:
total 11M
655373 -rwxr-xr-x  1 root root 1.9M Nov 14  2013 busybox
655368 -rwxr-xr-x  1 root root 998K Oct  7  2014 bash
655411 -rwxr-xr-x  1 root root 998K Mar  9  2015 false
655397 -rwxr-xr-x  1 root root 424K Nov 25  2014 dbus-daemon
655523 -rwxr-xr-x  1 root root 346K Feb  4  2014 tar
655427 -rwxr-xr-x  1 root root 301K Feb 17  2014 ip
655527 -rwxr-xr-x  1 root root 243K Feb  4  2015 udevadm
655457 -rwxr-xr-x  1 root root 188K Oct  1  2012 nano
655420 -rwxr-xr-x  1 root root 188K Jan 18  2014 grep
655410 -rwxr-xr-x  1 root root 180K Jan 18  2014 egrep
655431 -rwxr-xr-x  1 root root 151K Apr 10  2014 kmod
655432 -rwxr-xr-x  1 root root 151K Jun 10  2013 less
655414 -rwxr-xr-x  1 root root 136K Jan 18  2014 fgrep
655393 -rwxr-xr-x  1 root root 135K Jan  7  2015 cpio
655392 -rwxr-xr-x  1 root root 128K Jan 13  2015 cp
655456 -rwxr-xr-x  1 root root 120K Jan 13  2015 mv
655394 -rwxr-xr-x  1 root root 119K Feb 19  2014 dash
655461 -rwxr-xr-x  1 root root 117K Aug  5  2014 netstat
655439 -rwxr-xr-x  1 root root 109K Feb 18  2013 loadkeys
655403 -rwxr-xr-x  1 root root 108K Jan 13  2015 dir
655444 -rwxr-xr-x  1 root root 108K Jan 13  2015 ls
655535 -rwxr-xr-x  1 root root 108K Jan 13  2015 vdir
655402 -rwxr-xr-x  1 root root  96K Jan 13  2015 df
655452 -rwsr-xr-x  1 root root  93K Feb 12  2015 mount
655423 -rwxr-xr-x  1 root root  92K Jan 10  2014 gzip
655495 -rwxr-xr-x  1 root root  92K Feb 10  2015 ps
655442 -rwxr-xr-x  1 root root  91K Feb  4  2015 loginctl
655407 -rwxr-xr-x  1 root root  81K Feb 18  2013 dumpkeys
655516 -rwxr-xr-x  1 root root  75K Feb 17  2014 ss
655507 -rwxr-xr-x  1 root root  72K Feb 13  2014 sed
655529 -rwsr-xr-x  1 root root  68K Feb 12  2015 umount
655455 -rwxr-xr-x  1 root root  68K Jan  7  2015 mt-gnu
655518 -rwxr-xr-x  1 root root  67K Jan 13  2015 stty
655465 -rwxr-xr-x  1 root root  67K Dec 18  2013 ntfs-3g.secaudit
655443 -rwxr-xr-x  1 root root  63K Dec 18  2013 lowntfs-3g
655525 -rwxr-xr-x  1 root root  59K Jan 13  2015 touch
655388 -rwxr-xr-x  1 root root  59K Jan 13  2015 chgrp
655390 -rwxr-xr-x  1 root root  59K Jan 13  2015 chown
655395 -rwxr-xr-x  1 root root  59K Jan 13  2015 date
655501 -rwxr-xr-x  1 root root  59K Jan 13  2015 rm
655463 -rwxr-xr-x  1 root root  59K Dec 18  2013 ntfs-3g
655399 -rwxr-xr-x  1 root root  55K Jan 13  2015 dd
655438 -rwxr-xr-x  1 root root  55K Jan 13  2015 ln
655389 -rwxr-xr-x  1 root root  55K Jan 13  2015 chmod
655473 -rwxr-xr-x  1 root root  55K Dec 18  2013 ntfsinfo
655448 -rwxr-xr-x  1 root root  51K Jan 13  2015 mkdir
655441 -rwxr-xr-x  1 root root  48K Feb 16  2014 login
655385 -rwxr-xr-x  1 root root  47K Jan 13  2015 cat
655409 -rwxr-xr-x  1 root root  47K Jul 16  2013 ed
655445 -rwxr-xr-x  1 root root  44K Feb 12  2015 lsblk
655491 -rwsr-xr-x  1 root root  44K May  7  2014 ping6
655490 -rwsr-xr-x  1 root root  44K May  7  2014 ping
655502 -rwxr-xr-x  1 root root  43K Jan 13  2015 rmdir
655478 -rwxr-xr-x  1 root root  43K Dec 18  2013 ntfswipe
655511 -rwxr-xr-x  1 root root  39K Feb 18  2013 setfont
655450 -rwxr-xr-x  1 root root  39K Jan 13  2015 mktemp
655451 -rwxr-xr-x  1 root root  39K Feb 12  2015 more
655498 -rwxr-xr-x  1 root root  39K Jan 13  2015 readlink
655472 -rwxr-xr-x  1 root root  39K Dec 18  2013 ntfsfix
655519 -rwsr-xr-x  1 root root  37K Feb 16  2014 su
655510 -rwxr-xr-x  1 root root  36K May 23  2013 setfacl
655415 -rwxr-xr-x  1 root root  36K Feb 12  2015 findmnt
655449 -rwxr-xr-x  1 root root  35K Jan 13  2015 mknod
655492 -rwxr-xr-x  1 root root  35K Dec  2  2014 plymouth
655470 -rwxr-xr-x  1 root root  35K Dec 18  2013 ntfscmp
655477 -rwxr-xr-x  1 root root  35K Dec 18  2013 ntfstruncate
655474 -rwxr-xr-x  1 root root  32K Dec 18  2013 ntfsls
655416 -rwxr-xr-x  1 root root  32K Nov 29  2012 fuser
655493 -rwxr-xr-x  1 root root  31K Dec  2  2014 plymouth-upstart-bridge
655496 -rwxr-xr-x  1 root root  31K Jan 13  2015 pwd
655530 -rwxr-xr-x  1 root root  31K Jan 13  2015 uname
655408 -rwxr-xr-x  1 root root  31K Jan 13  2015 echo
655515 -rwxr-xr-x  1 root root  31K Jan 13  2015 sleep
655459 -rwxr-xr-x  1 root root  31K Dec  3  2012 nc.openbsd
655372 -rwxr-xr-x  1 root root  31K Oct 21  2013 bunzip2
655374 -rwxr-xr-x  1 root root  31K Oct 21  2013 bzcat
655381 -rwxr-xr-x  1 root root  31K Oct 21  2013 bzip2
655469 -rwxr-xr-x  1 root root  31K Dec 18  2013 ntfscluster
655476 -rwxr-xr-x  1 root root  31K Dec 18  2013 ntfsmove
655417 -rwsr-xr-x  1 root root  31K Dec 16  2013 fusermount
655468 -rwxr-xr-x  1 root root  31K Dec 18  2013 ntfsck
655538 -rwxr-xr-x  1 root root  27K Mar 23  2014 whiptail
655520 -rwxr-xr-x  1 root root  27K Jan 13  2015 sync
655526 -rwxr-xr-x  1 root root  27K Jan 13  2015 true
657094 -rwxr-xr-x  1 root root  27K Jun 13  2012 nc.traditional
655467 -rwxr-xr-x  1 root root  27K Dec 18  2013 ntfscat
655475 -rwxr-xr-x  1 root root  27K Dec 18  2013 ntfsmftalloc
655419 -rwxr-xr-x  1 root root  24K May 23  2013 getfacl
655430 -rwxr-xr-x  1 root root  23K Feb 10  2015 kill
655404 -rwxr-xr-x  1 root root  23K Feb 12  2015 dmesg
655471 -rwxr-xr-x  1 root root  22K Dec 18  2013 ntfsdump_logfile
655504 -rwxr-xr-x  1 root root  19K Aug 27  2013 run-parts
655480 -rwxr-xr-x  1 root root  19K Feb 18  2013 openvt
655522 -rwxr-xr-x  1 root root  19K Feb 12  2015 tailf
655466 -rwxr-xr-x  1 root root  18K Dec 18  2013 ntfs-3g.usermap
655435 -rwxr-xr-x  1 root root  16K Jun 10  2013 lesskey
655424 -rwxr-xr-x  1 root root  15K Dec 13  2013 hostname
657103 -rwxr-xr-x  1 root root  15K Mar 12  2015 xingyi_bindshell
655386 -rwxr-xr-x  1 root root  15K May 23  2013 chacl
655382 -rwxr-xr-x  1 root root  15K Oct 21  2013 bzip2recover
655528 -rwxr-xr-x  1 root root  14K Dec 16  2013 ulockmgr_server
657076 -rwxr-xr-x  1 root root  14K Mar 12  2015 xingyi_reverse_shell
655512 -rwxr-xr-x  1 root root  12K Jan 29  2014 setupcon
655396 -rwxr-xr-x  1 root root  11K Nov 25  2014 dbus-cleanup-sockets
655413 -rwxr-xr-x  1 root root  11K Feb 18  2013 fgconsole
655391 -rwxr-xr-x  1 root root  11K Feb 18  2013 chvt
655428 -rwxr-xr-x  1 root root  11K Feb 18  2013 kbd_mode
655398 -rwxr-xr-x  1 root root  11K Nov 25  2014 dbus-uuidgen
655453 -rwxr-xr-x  1 root root  11K Mar 12  2014 mountpoint
655433 -rwxr-xr-x  1 root root  11K Jun 10  2013 lessecho
655524 -rwxr-xr-x  1 root root  11K Aug 27  2013 tempfile
655464 -rwxr-xr-x  1 root root  11K Dec 18  2013 ntfs-3g.probe
657109 -rwxr-xr-x  1 root root 9.5K Mar 12  2015 xingyi_rootshell
655436 -rwxr-xr-x  1 root root 7.6K Jun 10  2013 lesspipe
655536 -rwxr-xr-x  1 root root 6.2K Jan 28  2015 vmmouse_detect
655546 -rwxr-xr-x  1 root root 5.9K Jan 10  2014 zgrep
655422 -rwxr-xr-x  1 root root 5.8K Jan 10  2014 gzexe
655542 -rwxr-xr-x  1 root root 5.7K Jan 10  2014 zdiff
655549 -rwxr-xr-x  1 root root 5.0K Jan 10  2014 znew
655378 -rwxr-xr-x  1 root root 4.8K Oct 21  2013 bzexe
655361 drwxr-xr-x  2 root root 4.0K Mar  9  2015 .
     2 drwxr-xr-x 23 root root 4.0K Mar  5  2015 ..
655380 -rwxr-xr-x  1 root root 3.6K Oct 21  2013 bzgrep
655532 -rwxr-xr-x  1 root root 2.7K Feb 18  2013 unicode_start
655421 -rwxr-xr-x  1 root root 2.3K Jan 10  2014 gunzip
655531 -rwxr-xr-x  1 root root 2.3K Jan 10  2014 uncompress
655376 -rwxr-xr-x  1 root root 2.1K Oct 21  2013 bzdiff
655545 -rwxr-xr-x  1 root root 2.1K Jan 10  2014 zforce
655547 -rwxr-xr-x  1 root root 2.0K Jan 10  2014 zless
655540 -rwxr-xr-x  1 root root 1.9K Jan 10  2014 zcat
655548 -rwxr-xr-x  1 root root 1.9K Jan 10  2014 zmore
655541 -rwxr-xr-x  1 root root 1.8K Jan 10  2014 zcmp
655384 -rwxr-xr-x  1 root root 1.3K Oct 21  2013 bzmore
655537 -rwxr-xr-x  1 root root  946 Aug 27  2013 which
655505 -rwxr-xr-x  1 root root  254 Jul 18  2014 running-in-container
655543 -rwxr-xr-x  1 root root  142 Jan 10  2014 zegrep
655544 -rwxr-xr-x  1 root root  142 Jan 10  2014 zfgrep
655499 -rwxr-xr-x  1 root root   89 Jul 16  2013 red
655460 lrwxrwxrwx  1 root root   24 Mar  5  2015 netcat -> /etc/alternatives/netcat
655454 lrwxrwxrwx  1 root root   20 Mar  5  2015 mt -> /etc/alternatives/mt
655458 lrwxrwxrwx  1 root root   20 Mar  5  2015 nc -> /etc/alternatives/nc
655489 lrwxrwxrwx  1 root root   14 Mar  5  2015 pidof -> /sbin/killall5
655405 lrwxrwxrwx  1 root root    8 Mar  5  2015 dnsdomainname -> hostname
655406 lrwxrwxrwx  1 root root    8 Mar  5  2015 domainname -> hostname
655434 lrwxrwxrwx  1 root root    8 Mar  5  2015 lessfile -> lesspipe
655462 lrwxrwxrwx  1 root root    8 Mar  5  2015 nisdomainname -> hostname
655539 lrwxrwxrwx  1 root root    8 Mar  5  2015 ypdomainname -> hostname
655517 lrwxrwxrwx  1 root root    7 Mar  5  2015 static-sh -> busybox
655375 lrwxrwxrwx  1 root root    6 Mar  5  2015 bzcmp -> bzdiff
655377 lrwxrwxrwx  1 root root    6 Mar  5  2015 bzegrep -> bzgrep
655379 lrwxrwxrwx  1 root root    6 Mar  5  2015 bzfgrep -> bzgrep
655383 lrwxrwxrwx  1 root root    6 Mar  5  2015 bzless -> bzmore
655479 lrwxrwxrwx  1 root root    6 Mar  5  2015 open -> openvt
655446 lrwxrwxrwx  1 root root    4 Mar  5  2015 lsmod -> kmod
655497 lrwxrwxrwx  1 root root    4 Mar  5  2015 rbash -> bash
655503 lrwxrwxrwx  1 root root    4 Mar  5  2015 rnano -> nano
655513 lrwxrwxrwx  1 root root    4 Mar  5  2015 sh -> dash
655514 lrwxrwxrwx  1 root root    4 Mar  5  2015 sh.distrib -> dash
u64@u64-VirtualBox:/media/part0$
```

- Size difference between ```true``` and ```false```

```sh
u64@u64-VirtualBox:/media/part0$ ls -lahiR --sort=size bin/true
655526 -rwxr-xr-x 1 root root 27K Jan 13  2015 bin/true
u64@u64-VirtualBox:/media/part0$
```

```sh
u64@u64-VirtualBox:/media/part0$ ls -lahiR --sort=size bin/false
655411 -rwxr-xr-x 1 root root 998K Mar  9  2015 bin/false
u64@u64-VirtualBox:/media/part0$
```

```sh
u64@u64-VirtualBox:/media/part0$ ls -lahiR --sort=size sbin/
sbin/:
total 12M
529490 -rwxr-xr-x  1 root root   1.7M Oct 10  2014 wpa_supplicant
529271 -rwxr-xr-x  1 root root   1.6M Apr  7  2014 dhclient
524305 -rwxr-xr-x  1 root root   930K Feb 25  2015 ldconfig.real
529253 -rwxr-xr-x  1 root root   830K Nov 14  2014 apparmor_parser
529258 -rwxr-xr-x  1 root root   587K Mar 31  2014 brltty
529450 -rwxr-xr-x  1 root root   276K Feb 17  2014 tc
529313 -rwxr-xr-x  1 root root   260K Jul 18  2014 init
529281 -rwxr-xr-x  1 root root   252K Jan 29  2014 ethtool
528994 -rwxr-xr-x  1 root root   243K Feb 16  2015 e2fsck
529314 -rwxr-xr-x  1 root root   189K Apr 11  2014 initctl
529302 -rwxr-xr-x  1 root root   175K Dec 26  2013 gdisk
529262 -rwxr-xr-x  1 root root   168K Dec 26  2013 cgdisk
529434 -rwxr-xr-x  1 root root   159K Dec 26  2013 sgdisk
529462 -rwxr-xr-x  1 root root   139K Jul 18  2014 upstart-file-bridge
529460 -rwxr-xr-x  1 root root   131K Jul 18  2014 upstart-dbus-bridge
529463 -rwxr-xr-x  1 root root   131K Jul 18  2014 upstart-local-bridge
529464 -rwxr-xr-x  1 root root   131K Jul 18  2014 upstart-socket-bridge
529461 -rwxr-xr-x  1 root root   123K Jul 18  2014 upstart-event-bridge
529026 -rwxr-xr-x  1 root root   114K Feb 16  2015 debugfs
529329 -rwxr-xr-x  1 root root   105K May 24  2012 iw
529390 -rwxr-xr-x  1 root root   103K Feb 21  2014 mountall
529451 -rwxr-xr-x  1 root root   103K Jul 18  2014 telinit
529307 -rwxr-xr-x  1 root root   101K Nov 15  2013 hdparm
529283 -rwxr-xr-x  1 root root    98K Feb 12  2015 fdisk
528998 -rwxr-xr-x  1 root root    96K Feb 16  2015 mke2fs
529489 -rwxr-xr-x  1 root root    92K Oct 10  2014 wpa_cli
529491 -rwxr-xr-x  1 root root    86K Jan  8  2014 xtables-multi
529436 -rwxr-xr-x  1 root root    83K Jul 18  2014 shutdown
529405 -rwxr-xr-x  1 root root    80K Dec  2  2014 plymouthd
529400 -rwxr-xr-x  1 root root    80K Apr 14  2014 parted
529379 -rwxr-xr-x  1 root root    79K Dec 18  2013 mkntfs
529465 -rwxr-xr-x  1 root root    75K Jul 18  2014 upstart-udev-bridge
529395 -rwxr-xr-x  1 root root    71K Dec 18  2013 ntfsresize
529273 -rwxr-xr-x  1 root root    70K Dec 13  2013 dmsetup
528982 -rwxr-xr-x  1 root root    68K Feb 16  2015 tune2fs
529309 -rwxr-xr-x  1 root root    67K Aug  5  2014 ifconfig
529312 -rwxr-xr-x  1 root root    62K May 12  2014 ifup
529433 -rwxr-xr-x  1 root root    61K Feb 12  2015 sfdisk
529285 -rwxr-xr-x  1 root root    59K Dec 26  2013 fixparts
529426 -rwxr-xr-x  1 root root    57K Aug  5  2014 route
529293 -rwxr-xr-x  1 root root    55K Mar 18  2014 fsck.fat
529392 -rwxr-xr-x  1 root root    55K Dec 18  2013 ntfsclone
529261 -rwxr-xr-x  1 root root    54K Feb 12  2015 cfdisk
529248 -rwxr-xr-x  1 root root    52K May 18  2013 MAKEDEV
529257 -rwxr-xr-x  1 root root    51K Feb 17  2014 bridge
529282 -rwxr-xr-x  1 root root    51K Mar 18  2014 fatlabel
528986 -rwxr-xr-x  1 root root    48K Feb 16  2015 resize2fs
529466 -rwxr-xr-x  1 root root    47K Mar 25  2013 ureadahead
529396 -rwxr-xr-x  1 root root    47K Dec 18  2013 ntfsundelete
529342 -rwxr-xr-x  1 root root    43K Feb 12  2015 losetup
529440 -rwxr-xr-x  1 root root    35K Mar 12  2014 startpar
529458 -rwxr-sr-x  1 root shadow  35K Jan 31  2014 unix_chkpwd
529308 -rwxr-xr-x  1 root root    35K Feb 12  2015 hwclock
529333 -rwxr-xr-x  1 root root    35K May  3  2012 iwlist
529427 -rwxr-xr-x  1 root root    35K Feb 17  2014 rtacct
529428 -rwxr-xr-x  1 root root    35K Feb 17  2014 rtmon
529437 -rwxr-xr-x  1 root root    34K Aug  5  2014 slattach
529250 -rwxr-xr-x  1 root root    32K Feb 12  2015 agetty
529305 -rwxr-xr-x  1 root root    32K Feb 12  2015 getty
529287 -rwxr-xr-x  1 root root    31K Feb 12  2015 fsck
529255 -rwxr-xr-x  1 root root    31K Feb 12  2015 blkid
528981 -rwxr-xr-x  1 root root    31K Feb 16  2015 e2image
529459 -rwxr-xr-x  1 root root    31K Jan 31  2014 unix_update
529368 -rwxr-xr-x  1 root root    31K Feb 12  2015 mkfs.cramfs
529294 -rwxr-xr-x  1 root root    31K Feb 12  2015 fsck.minix
529381 -rwxr-xr-x  1 root root    31K Feb 21  2014 mntctl
529393 -rwxr-xr-x  1 root root    31K Dec 18  2013 ntfscp
529416 -rwxr-xr-x  1 root root    30K Aug  5  2014 rarp
529439 -rwxr-xr-x  1 root root    28K Mar  7  2014 start-stop-daemon
529373 -rwxr-xr-x  1 root root    27K Mar 18  2014 mkfs.fat
529447 -rwxr-xr-x  1 root root    27K Feb 12  2015 swapon
528999 -rwxr-xr-x  1 root root    27K Feb 16  2015 badblocks
529374 -rwxr-xr-x  1 root root    27K Feb 12  2015 mkfs.minix
529330 -rwxr-xr-x  1 root root    27K May  3  2012 iwconfig
529394 -rwxr-xr-x  1 root root    27K Dec 18  2013 ntfslabel
529380 -rwxr-xr-x  1 root root    23K Feb 12  2015 mkswap
528995 -rwxr-xr-x  1 root root    23K Feb 16  2015 dumpe2fs
529256 -rwxr-xr-x  1 root root    23K Feb 12  2015 blockdev
529449 -rwxr-xr-x  1 root root    23K Feb 10  2015 sysctl
529327 -rwxr-xr-x  1 root root    23K Aug  5  2014 iptunnel
529363 -rwxr-xr-x  1 root root    19K Aug  5  2014 mii-tool
529338 -rwxr-xr-x  1 root root    19K Mar 12  2014 killall5
529260 -rwxr-xr-x  1 root root    19K Feb 21  2014 capsh
529487 -rwxr-xr-x  1 root root    19K Feb 12  2015 wipefs
529402 -rwxr-xr-x  1 root root    19K Jun 28  2012 pccardctl
529378 -rwxr-xr-x  1 root root    19K Jan 31  2014 mkhomedir_helper
529322 -rwxr-xr-x  1 root root    19K Aug  5  2014 ipmaddr
529367 -rwxr-xr-x  1 root root    19K Feb 12  2015 mkfs.bfs
529444 -rwxr-xr-x  1 root root    15K Mar 12  2014 sulogin
529391 -rwxr-xr-x  1 root root    15K Aug  5  2014 nameif
529418 -rwxr-xr-x  1 root root    15K Jul 18  2014 reboot
529399 -rwxr-xr-x  1 root root    15K Jan 31  2014 pam_tally2
529263 -rwxr-xr-x  1 root root    15K Oct  1  2012 crda
529331 -rwxr-xr-x  1 root root    15K May  3  2012 iwevent
529445 -rwxr-xr-x  1 root root    15K Feb 12  2015 swaplabel
529288 -rwxr-xr-x  1 root root    15K Feb 12  2015 fsck.cramfs
529300 -rwxr-xr-x  1 root root    15K Feb 12  2015 fstrim
529328 -rwxr-xr-x  1 root root    15K Feb 12  2015 isosize
529334 -rwxr-xr-x  1 root root    15K May  3  2012 iwpriv
529335 -rwxr-xr-x  1 root root    15K May  3  2012 iwspy
529332 -rwxr-xr-x  1 root root    15K May  3  2012 iwgetid
529272 -rwxr-xr-x  1 root root    15K Apr  7  2014 dhclient-script
524291 drwxr-xr-x  2 root root    12K Mar  5  2015 .
529432 -rwxr-xr-x  1 root root    11K Feb 18  2013 setvtrgb
528993 -rwxr-xr-x  1 root root    11K Feb 16  2015 e2undo
529336 -rwxr-xr-x  1 root root    11K Feb 18  2013 kbdrate
528959 -rwxr-xr-x  1 root root    11K Feb 16  2015 logsave
529398 -rwxr-xr-x  1 root root    11K Jan 31  2014 pam_tally
529448 -rwxr-xr-x  1 root root    11K Feb 12  2015 switch_root
529457 -rwxr-xr-x  1 root root    11K Mar 10  2014 umount.udisks2
529401 -rwxr-xr-x  1 root root    11K Apr 14  2014 partprobe
529419 -rwxr-xr-x  1 root root    11K Oct  1  2012 regdbdump
529431 -rwxr-xr-x  1 root root    11K Feb 21  2014 setcap
529303 -rwxr-xr-x  1 root root    11K Feb 21  2014 getcap
529404 -rwxr-xr-x  1 root root    11K Aug  5  2014 plipconfig
529298 -rwxr-xr-x  1 root root    11K Feb 12  2015 fsfreeze
529366 -rwxr-xr-x  1 root root    11K Feb 12  2015 mkfs
529417 -rwxr-xr-x  1 root root    11K Feb 12  2015 raw
529386 -rwxr-xr-x  1 root root    10K Dec 16  2013 mount.fuse
529429 -rwxr-xr-x  1 root root    10K Jul 18  2014 runlevel
529324 -rwxr-xr-x  1 root root   6.9K Jan  8  2014 iptables-apply
529304 -rwxr-xr-x  1 root root   6.2K Feb 21  2014 getpcaps
529441 -rwxr-xr-x  1 root root   6.2K Mar 12  2014 startpar-upstart-inject
529284 -rwxr-xr-x  1 root root   6.2K Feb 12  2015 findfs
529299 -rwxr-xr-x  1 root root   6.2K Mar 12  2014 fstab-decode
529268 -rwxr-xr-x  1 root root   6.2K Feb 12  2015 ctrlaltdel
529252 -rwxr-xr-x  1 root root   6.2K Oct  2  2012 apm_available
529249 -rwxr-xr-x  1 root root   6.2K Oct  2  2012 acpi_available
529403 -rwxr-xr-x  1 root root   6.1K Feb 12  2015 pivot_root
529423 -rwxr-xr-x  1 root root   5.5K Jun 13  2014 resolvconf
529251 -rwxr-xr-x  1 root root   5.5K Feb 13  2013 alsa
     2 drwxr-xr-x 23 root root   4.0K Mar  5  2015 ..
529301 -rwxr-xr-x  1 root root   3.0K Feb 12  2015 fstrim-all
529316 -rwxr-xr-x  1 root root   2.4K Aug 27  2013 installkernel
529397 -rwxr-xr-x  1 root root   2.2K Dec  2  2009 on_ac_power
529488 -rwxr-xr-x  1 root root   1.7K Jan 28  2014 wpa_action
529259 -rwxr-xr-x  1 root root   1.4K Mar 13  2014 brltty-setup
529435 -rwxr-xr-x  1 root root    885 Feb 16  2014 shadowconfig
524295 -rwxr-xr-x  1 root root    387 Feb 25  2015 ldconfig
529296 -rwxr-xr-x  1 root root    333 Mar 12  2014 fsck.nfs
525304 lrwxrwxrwx  1 root root     57 Mar  5  2015 mount.vboxsf -> /usr/lib/x86_64-linux-gnu/VBoxGuestAdditions/mount.vboxsf
529454 lrwxrwxrwx  1 root root     26 Mar  5  2015 udevd -> /lib/systemd/systemd-udevd
529387 lrwxrwxrwx  1 root root     15 Mar  5  2015 mount.lowntfs-3g -> /bin/lowntfs-3g
529319 lrwxrwxrwx  1 root root     14 Mar  5  2015 ip6tables-apply -> iptables-apply
529318 lrwxrwxrwx  1 root root     13 Mar  5  2015 ip6tables -> xtables-multi
529320 lrwxrwxrwx  1 root root     13 Mar  5  2015 ip6tables-restore -> xtables-multi
529321 lrwxrwxrwx  1 root root     13 Mar  5  2015 ip6tables-save -> xtables-multi
529323 lrwxrwxrwx  1 root root     13 Mar  5  2015 iptables -> xtables-multi
529325 lrwxrwxrwx  1 root root     13 Mar  5  2015 iptables-restore -> xtables-multi
529326 lrwxrwxrwx  1 root root     13 Mar  5  2015 iptables-save -> xtables-multi
529388 lrwxrwxrwx  1 root root     13 Mar  5  2015 mount.ntfs -> mount.ntfs-3g
529389 lrwxrwxrwx  1 root root     12 Mar  5  2015 mount.ntfs-3g -> /bin/ntfs-3g
529453 lrwxrwxrwx  1 root root     12 Mar  5  2015 udevadm -> /bin/udevadm
529270 lrwxrwxrwx  1 root root      9 Mar  5  2015 depmod -> /bin/kmod
529315 lrwxrwxrwx  1 root root      9 Mar  5  2015 insmod -> /bin/kmod
529343 lrwxrwxrwx  1 root root      9 Mar  5  2015 lsmod -> /bin/kmod
529344 lrwxrwxrwx  1 root root      9 Mar  5  2015 lspcmcia -> pccardctl
529382 lrwxrwxrwx  1 root root      9 Mar  5  2015 modinfo -> /bin/kmod
529383 lrwxrwxrwx  1 root root      9 Mar  5  2015 modprobe -> /bin/kmod
529425 lrwxrwxrwx  1 root root      9 Mar  5  2015 rmmod -> /bin/kmod
529274 lrwxrwxrwx  1 root root      8 Mar  5  2015 dosfsck -> fsck.fat
529275 lrwxrwxrwx  1 root root      8 Mar  5  2015 dosfslabel -> fatlabel
529295 lrwxrwxrwx  1 root root      8 Mar  5  2015 fsck.msdos -> fsck.fat
529297 lrwxrwxrwx  1 root root      8 Mar  5  2015 fsck.vfat -> fsck.fat
529364 lrwxrwxrwx  1 root root      8 Mar  5  2015 mkdosfs -> mkfs.fat
529375 lrwxrwxrwx  1 root root      8 Mar  5  2015 mkfs.msdos -> mkfs.fat
529377 lrwxrwxrwx  1 root root      8 Mar  5  2015 mkfs.vfat -> mkfs.fat
529063 lrwxrwxrwx  1 root root      7 Feb 16  2015 e2label -> tune2fs
529317 lrwxrwxrwx  1 root root      7 Mar  5  2015 ip -> /bin/ip
529420 lrwxrwxrwx  1 root root      7 Mar  5  2015 reload -> initctl
529424 lrwxrwxrwx  1 root root      7 Mar  5  2015 restart -> initctl
529438 lrwxrwxrwx  1 root root      7 Mar  5  2015 start -> initctl
529442 lrwxrwxrwx  1 root root      7 Mar  5  2015 status -> initctl
529443 lrwxrwxrwx  1 root root      7 Mar  5  2015 stop -> initctl
529052 lrwxrwxrwx  1 root root      6 Feb 16  2015 fsck.ext2 -> e2fsck
529337 lrwxrwxrwx  1 root root      6 Feb 16  2015 fsck.ext3 -> e2fsck
529104 lrwxrwxrwx  1 root root      6 Feb 16  2015 fsck.ext4 -> e2fsck
529045 lrwxrwxrwx  1 root root      6 Feb 16  2015 fsck.ext4dev -> e2fsck
529306 lrwxrwxrwx  1 root root      6 Mar  5  2015 halt -> reboot
529096 lrwxrwxrwx  1 root root      6 Feb 16  2015 mkfs.ext2 -> mke2fs
529061 lrwxrwxrwx  1 root root      6 Feb 16  2015 mkfs.ext3 -> mke2fs
529119 lrwxrwxrwx  1 root root      6 Feb 16  2015 mkfs.ext4 -> mke2fs
529049 lrwxrwxrwx  1 root root      6 Feb 16  2015 mkfs.ext4dev -> mke2fs
529376 lrwxrwxrwx  1 root root      6 Mar  5  2015 mkfs.ntfs -> mkntfs
529406 lrwxrwxrwx  1 root root      6 Mar  5  2015 poweroff -> reboot
529446 lrwxrwxrwx  1 root root      6 Mar  5  2015 swapoff -> swapon
529310 lrwxrwxrwx  1 root root      4 Mar  5  2015 ifdown -> ifup
529311 lrwxrwxrwx  1 root root      4 Mar  5  2015 ifquery -> ifup
u64@u64-VirtualBox:/media/part0$
```

- Sort by ```time```

```sh
u64@u64-VirtualBox:/media/part0$ ls -lahiR --sort=time sbin/ | more
sbin/:
total 12M
524291 drwxr-xr-x  2 root root    12K Mar  5  2015 .
525304 lrwxrwxrwx  1 root root     57 Mar  5  2015 mount.vboxsf -> /usr/lib/x86_64-linux-gnu/VBoxGu
estAdditions/mount.vboxsf
     2 drwxr-xr-x 23 root root   4.0K Mar  5  2015 ..
529453 lrwxrwxrwx  1 root root     12 Mar  5  2015 udevadm -> /bin/udevadm
529454 lrwxrwxrwx  1 root root     26 Mar  5  2015 udevd -> /lib/systemd/systemd-udevd
529442 lrwxrwxrwx  1 root root      7 Mar  5  2015 status -> initctl
529443 lrwxrwxrwx  1 root root      7 Mar  5  2015 stop -> initctl
529446 lrwxrwxrwx  1 root root      6 Mar  5  2015 swapoff -> swapon
529438 lrwxrwxrwx  1 root root      7 Mar  5  2015 start -> initctl
529420 lrwxrwxrwx  1 root root      7 Mar  5  2015 reload -> initctl
529424 lrwxrwxrwx  1 root root      7 Mar  5  2015 restart -> initctl
529425 lrwxrwxrwx  1 root root      9 Mar  5  2015 rmmod -> /bin/kmod
529406 lrwxrwxrwx  1 root root      6 Mar  5  2015 poweroff -> reboot
529382 lrwxrwxrwx  1 root root      9 Mar  5  2015 modinfo -> /bin/kmod
529383 lrwxrwxrwx  1 root root      9 Mar  5  2015 modprobe -> /bin/kmod
529387 lrwxrwxrwx  1 root root     15 Mar  5  2015 mount.lowntfs-3g -> /bin/lowntfs-3g
529388 lrwxrwxrwx  1 root root     13 Mar  5  2015 mount.ntfs -> mount.ntfs-3g
529389 lrwxrwxrwx  1 root root     12 Mar  5  2015 mount.ntfs-3g -> /bin/ntfs-3g
529375 lrwxrwxrwx  1 root root      8 Mar  5  2015 mkfs.msdos -> mkfs.fat
529376 lrwxrwxrwx  1 root root      6 Mar  5  2015 mkfs.ntfs -> mkntfs
529377 lrwxrwxrwx  1 root root      8 Mar  5  2015 mkfs.vfat -> mkfs.fat
529364 lrwxrwxrwx  1 root root      8 Mar  5  2015 mkdosfs -> mkfs.fat
529344 lrwxrwxrwx  1 root root      9 Mar  5  2015 lspcmcia -> pccardctl
529343 lrwxrwxrwx  1 root root      9 Mar  5  2015 lsmod -> /bin/kmod
529315 lrwxrwxrwx  1 root root      9 Mar  5  2015 insmod -> /bin/kmod
529317 lrwxrwxrwx  1 root root      7 Mar  5  2015 ip -> /bin/ip
529318 lrwxrwxrwx  1 root root     13 Mar  5  2015 ip6tables -> xtables-multi
529319 lrwxrwxrwx  1 root root     14 Mar  5  2015 ip6tables-apply -> iptables-apply
529320 lrwxrwxrwx  1 root root     13 Mar  5  2015 ip6tables-restore -> xtables-multi
529321 lrwxrwxrwx  1 root root     13 Mar  5  2015 ip6tables-save -> xtables-multi
529323 lrwxrwxrwx  1 root root     13 Mar  5  2015 iptables -> xtables-multi
529325 lrwxrwxrwx  1 root root     13 Mar  5  2015 iptables-restore -> xtables-multi
529326 lrwxrwxrwx  1 root root     13 Mar  5  2015 iptables-save -> xtables-multi
529306 lrwxrwxrwx  1 root root      6 Mar  5  2015 halt -> reboot
529310 lrwxrwxrwx  1 root root      4 Mar  5  2015 ifdown -> ifup
529311 lrwxrwxrwx  1 root root      4 Mar  5  2015 ifquery -> ifup
529297 lrwxrwxrwx  1 root root      8 Mar  5  2015 fsck.vfat -> fsck.fat
529295 lrwxrwxrwx  1 root root      8 Mar  5  2015 fsck.msdos -> fsck.fat
529274 lrwxrwxrwx  1 root root      8 Mar  5  2015 dosfsck -> fsck.fat
529275 lrwxrwxrwx  1 root root      8 Mar  5  2015 dosfslabel -> fatlabel
529270 lrwxrwxrwx  1 root root      9 Mar  5  2015 depmod -> /bin/kmod
524305 -rwxr-xr-x  1 root root   930K Feb 25  2015 ldconfig.real
524295 -rwxr-xr-x  1 root root    387 Feb 25  2015 ldconfig
528999 -rwxr-xr-x  1 root root    27K Feb 16  2015 badblocks
529026 -rwxr-xr-x  1 root root   114K Feb 16  2015 debugfs
528995 -rwxr-xr-x  1 root root    23K Feb 16  2015 dumpe2fs
528994 -rwxr-xr-x  1 root root   243K Feb 16  2015 e2fsck
528981 -rwxr-xr-x  1 root root    31K Feb 16  2015 e2image
528993 -rwxr-xr-x  1 root root    11K Feb 16  2015 e2undo
528959 -rwxr-xr-x  1 root root    11K Feb 16  2015 logsave
528998 -rwxr-xr-x  1 root root    96K Feb 16  2015 mke2fs
528986 -rwxr-xr-x  1 root root    48K Feb 16  2015 resize2fs
u64@u64-VirtualBox:/media/part0$
```

```sh
u64@u64-VirtualBox:/media/part0$ ls -lahiR --sort=time bin/ | more
bin/:
total 11M
657109 -rwxr-xr-x  1 root root 9.5K Mar 12  2015 xingyi_rootshell
657103 -rwxr-xr-x  1 root root  15K Mar 12  2015 xingyi_bindshell
657076 -rwxr-xr-x  1 root root  14K Mar 12  2015 xingyi_reverse_shell
655411 -rwxr-xr-x  1 root root 998K Mar  9  2015 false
655361 drwxr-xr-x  2 root root 4.0K Mar  9  2015 .
     2 drwxr-xr-x 23 root root 4.0K Mar  5  2015 ..
655539 lrwxrwxrwx  1 root root    8 Mar  5  2015 ypdomainname -> hostname
655513 lrwxrwxrwx  1 root root    4 Mar  5  2015 sh -> dash
655514 lrwxrwxrwx  1 root root    4 Mar  5  2015 sh.distrib -> dash
655517 lrwxrwxrwx  1 root root    7 Mar  5  2015 static-sh -> busybox
655497 lrwxrwxrwx  1 root root    4 Mar  5  2015 rbash -> bash
655503 lrwxrwxrwx  1 root root    4 Mar  5  2015 rnano -> nano
655479 lrwxrwxrwx  1 root root    6 Mar  5  2015 open -> openvt
655489 lrwxrwxrwx  1 root root   14 Mar  5  2015 pidof -> /sbin/killall5
655458 lrwxrwxrwx  1 root root   20 Mar  5  2015 nc -> /etc/alternatives/nc
655460 lrwxrwxrwx  1 root root   24 Mar  5  2015 netcat -> /etc/alternatives/netcat
655462 lrwxrwxrwx  1 root root    8 Mar  5  2015 nisdomainname -> hostname
655446 lrwxrwxrwx  1 root root    4 Mar  5  2015 lsmod -> kmod
655454 lrwxrwxrwx  1 root root   20 Mar  5  2015 mt -> /etc/alternatives/mt
655434 lrwxrwxrwx  1 root root    8 Mar  5  2015 lessfile -> lesspipe
655405 lrwxrwxrwx  1 root root    8 Mar  5  2015 dnsdomainname -> hostname
655406 lrwxrwxrwx  1 root root    8 Mar  5  2015 domainname -> hostname
655377 lrwxrwxrwx  1 root root    6 Mar  5  2015 bzegrep -> bzgrep
655379 lrwxrwxrwx  1 root root    6 Mar  5  2015 bzfgrep -> bzgrep
655383 lrwxrwxrwx  1 root root    6 Mar  5  2015 bzless -> bzmore
655375 lrwxrwxrwx  1 root root    6 Mar  5  2015 bzcmp -> bzdiff
655404 -rwxr-xr-x  1 root root  23K Feb 12  2015 dmesg
655415 -rwxr-xr-x  1 root root  36K Feb 12  2015 findmnt
655445 -rwxr-xr-x  1 root root  44K Feb 12  2015 lsblk
655451 -rwxr-xr-x  1 root root  39K Feb 12  2015 more
655452 -rwsr-xr-x  1 root root  93K Feb 12  2015 mount
655522 -rwxr-xr-x  1 root root  19K Feb 12  2015 tailf
655529 -rwsr-xr-x  1 root root  68K Feb 12  2015 umount
655430 -rwxr-xr-x  1 root root  23K Feb 10  2015 kill
655495 -rwxr-xr-x  1 root root  92K Feb 10  2015 ps
655442 -rwxr-xr-x  1 root root  91K Feb  4  2015 loginctl
655527 -rwxr-xr-x  1 root root 243K Feb  4  2015 udevadm
655536 -rwxr-xr-x  1 root root 6.2K Jan 28  2015 vmmouse_detect
655385 -rwxr-xr-x  1 root root  47K Jan 13  2015 cat
655388 -rwxr-xr-x  1 root root  59K Jan 13  2015 chgrp
655389 -rwxr-xr-x  1 root root  55K Jan 13  2015 chmod
655390 -rwxr-xr-x  1 root root  59K Jan 13  2015 chown
655392 -rwxr-xr-x  1 root root 128K Jan 13  2015 cp
655395 -rwxr-xr-x  1 root root  59K Jan 13  2015 date
655399 -rwxr-xr-x  1 root root  55K Jan 13  2015 dd
655402 -rwxr-xr-x  1 root root  96K Jan 13  2015 df
655403 -rwxr-xr-x  1 root root 108K Jan 13  2015 dir
655408 -rwxr-xr-x  1 root root  31K Jan 13  2015 echo
655438 -rwxr-xr-x  1 root root  55K Jan 13  2015 ln
655444 -rwxr-xr-x  1 root root 108K Jan 13  2015 ls
655448 -rwxr-xr-x  1 root root  51K Jan 13  2015 mkdir
655449 -rwxr-xr-x  1 root root  35K Jan 13  2015 mknod
655450 -rwxr-xr-x  1 root root  39K Jan 13  2015 mktemp
u64@u64-VirtualBox:/media/part0$
```

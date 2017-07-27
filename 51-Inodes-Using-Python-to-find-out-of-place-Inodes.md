#### 51. Inodes: Using Python to find out of place Inodes

###### ```out-of-seq-inodes.sh```

```sh
#!/bin/bash
# Simple script to list out of
# sequence inodes.
# Intended to be used as part of
# a forensics investigation.
# As developed for PentesterAcademy.com 
# by Dr. Phil Polstra (@ppolstra)

usage () {
    echo "Usage: $0 <path>"
    echo "Simple script to list a directory and print a warning if"
    echo "the inodes are out of sequence as will happen if system"
    echo "binaries are overwritten."
    exit 1
}

if [ $# -lt 1 ] ; then
  usage
fi

# output a listing sorted by inode number to a temp file
templs='/tmp/temp-ls.txt'
ls -aliR $1 | sort -n > $templs

foundfirstinode=false # this is for discarding first couple lines in output
declare -i startinode

while read line
do
   # there is usually a line or two of non-file stuff at start of output
   # the if statement helps us get past that
   if [ "$foundfirstinode" = false ] && [ "`echo $line | wc -w`" -gt 6 ] ; then
      startinode=`expr $(echo $line | awk '{print $1}')`
      echo "Start inode = $startinode"
      foundfirstinode=true
   fi
   q=$(echo $line | awk '{print $1}')
   if [ "$startinode" -lt $q ]; 
   then
      if [ $((startinode + 2)) -lt $q ] ; then
          echo -e "\e[31m****Out of Sequence inode detected**** expect $startinode got $q\e[0m"
      else
          echo -e "\e[33m****Out of Sequence inode detected**** expect $startinode got $q\e[0m"
      fi
      # reset the startinode to point to this value for next entry
      startinode=`expr $(echo $line | awk '{print $1}')`
   fi
   echo "$line"
   startinode=$((startinode+1))
done < $templs

rm $templs
```

###### Usage

```sh
u64@u64-VirtualBox:~/Desktop$ sudo ./out-of-seq-inodes.sh
Usage: ./out-of-seq-inodes.sh <path>
Simple script to list a directory and print a warning if
the inodes are out of sequence as will happen if system
binaries are overwritten.
u64@u64-VirtualBox:~/Desktop$
```

###### Run the script on the local ```/bin``` and ```/sbin```

```sh
u64@u64-VirtualBox:~/Desktop$ sudo ./out-of-seq-inodes.sh /bin
./out-of-seq-inodes.sh: line 38: [: : integer expression expected
/bin:
./out-of-seq-inodes.sh: line 38: [: total: integer expression expected
total 12984
Start inode = 2
2 drwxr-xr-x 24 root root    4096 Jul 27 09:49 ..
****Out of Sequence inode detected**** expect 3 got 131073
131073 drwxr-xr-x  2 root root    4096 Jul 27 09:47 .
****Out of Sequence inode detected**** expect 131074 got 131083
131083 -rwxr-xr-x  1 root root   31288 May 19  2015 bunzip2
131084 -rwxr-xr-x  1 root root 1964536 Aug 19  2015 busybox
131085 -rwxr-xr-x  1 root root   31288 May 19  2015 bzcat
131086 lrwxrwxrwx  1 root root       6 Jul 25 14:07 bzcmp -> bzdiff
131087 -rwxr-xr-x  1 root root    2140 May 19  2015 bzdiff
131088 lrwxrwxrwx  1 root root       6 Jul 25 14:07 bzegrep -> bzgrep
131089 -rwxr-xr-x  1 root root    4877 May 19  2015 bzexe
131090 lrwxrwxrwx  1 root root       6 Jul 25 14:07 bzfgrep -> bzgrep
131091 -rwxr-xr-x  1 root root    3642 May 19  2015 bzgrep
131092 -rwxr-xr-x  1 root root   31288 May 19  2015 bzip2
131093 -rwxr-xr-x  1 root root   14616 May 19  2015 bzip2recover
131094 lrwxrwxrwx  1 root root       6 Jul 25 14:07 bzless -> bzmore
131095 -rwxr-xr-x  1 root root    1297 May 19  2015 bzmore
131096 -rwxr-xr-x  1 root root   52080 Feb 18  2016 cat
131097 -rwxr-xr-x  1 root root   14752 Feb  7  2016 chacl
****Out of Sequence inode detected**** expect 131098 got 131099
131099 -rwxr-xr-x  1 root root   60272 Feb 18  2016 chgrp
131100 -rwxr-xr-x  1 root root   56112 Feb 18  2016 chmod
131101 -rwxr-xr-x  1 root root   64368 Feb 18  2016 chown
131102 -rwxr-xr-x  1 root root   10536 Sep 22  2016 chvt
131103 -rwxr-xr-x  1 root root  151024 Feb 18  2016 cp
131104 -rwxr-xr-x  1 root root  141472 Feb 18  2016 cpio
131105 -rwxr-xr-x  1 root root  154072 Feb 17  2016 dash
131106 -rwxr-xr-x  1 root root   68464 Feb 18  2016 date
131107 -rwxr-xr-x  1 root root   72632 Feb 18  2016 dd
****Out of Sequence inode detected**** expect 131108 got 131110
131110 -rwxr-xr-x  1 root root   97912 Feb 18  2016 df
131111 -rwxr-xr-x  1 root root  126584 Feb 18  2016 dir
131112 -rwxr-xr-x  1 root root   60680 Dec 16  2016 dmesg
131113 lrwxrwxrwx  1 root root       8 Jul 25 14:07 dnsdomainname -> hostname
131114 lrwxrwxrwx  1 root root       8 Jul 25 14:07 domainname -> hostname
131115 -rwxr-xr-x  1 root root   82328 Sep 22  2016 dumpkeys
131116 -rwxr-xr-x  1 root root   31376 Feb 18  2016 echo
131117 -rwxr-xr-x  1 root root   51512 Apr 26  2014 ed
131118 -rwxr-xr-x  1 root root   36504 Jul 13  2015 efibootmgr
131119 -rwxr-xr-x  1 root root      28 Apr 29  2016 egrep
131120 -rwxr-xr-x  1 root root   27280 Feb 18  2016 false
****Out of Sequence inode detected**** expect 131121 got 131122
131122 -rwxr-xr-x  1 root root   10544 Sep 22  2016 fgconsole
131123 -rwxr-xr-x  1 root root      28 Apr 29  2016 fgrep
131124 -rwxr-xr-x  1 root root   49576 Dec 16  2016 findmnt
131125 -rwxr-xr-x  1 root root   36024 Feb  7  2016 fuser
131126 -rwsr-xr-x  1 root root   30800 Jul 12  2016 fusermount
****Out of Sequence inode detected**** expect 131127 got 131128
131128 -rwxr-xr-x  1 root root   23752 Feb  7  2016 getfacl
131129 -rwxr-xr-x  1 root root  211224 Apr 29  2016 grep
131130 -rwxr-xr-x  1 root root    2301 Oct 27  2014 gunzip
131131 -rwxr-xr-x  1 root root    5927 Oct 27  2014 gzexe
131132 -rwxr-xr-x  1 root root   98240 Oct 27  2014 gzip
131133 -rwxr-xr-x  1 root root  192760 Mar  1  2016 hciconfig
131134 -rwxr-xr-x  1 root root   14800 Nov 24  2015 hostname
****Out of Sequence inode detected**** expect 131135 got 131137
131137 -rwxr-xr-x  1 root root  376192 Apr  5  2016 ip
131138 -rwxr-xr-x  1 root root  498936 Jan 18  2017 journalctl
131139 -rwxr-xr-x  1 root root   10536 Sep 22  2016 kbd_mode
****Out of Sequence inode detected**** expect 131140 got 131141
131141 -rwxr-xr-x  1 root root   23152 Nov 21  2016 kill
131142 -rwxr-xr-x  1 root root  154696 Mar 13  2016 kmod
131143 -rwxr-xr-x  1 root root  169800 Jul 26  2016 less
131144 -rwxr-xr-x  1 root root   10256 Jul 26  2016 lessecho
131145 lrwxrwxrwx  1 root root       8 Jul 25 14:07 lessfile -> lesspipe
131146 -rwxr-xr-x  1 root root   19824 Jul 26  2016 lesskey
131147 -rwxr-xr-x  1 root root    7764 Jul 26  2016 lesspipe
131148 -rwxr-xr-x  1 root root 1037528 May 16 05:49 bash
131149 -rwxr-xr-x  1 root root   56152 Feb 18  2016 ln
131150 -rwxr-xr-x  1 root root  111496 Sep 22  2016 loadkeys
131151 lrwxrwxrwx  1 root root       4 May 16 05:49 rbash -> bash
****Out of Sequence inode detected**** expect 131152 got 131153
131153 -rwxr-xr-x  1 root root  453848 Jan 18  2017 loginctl
131154 -rwxr-xr-x  1 root root  105136 Jan 28 08:54 lowntfs-3g
131155 -rwxr-xr-x  1 root root  126584 Feb 18  2016 ls
131156 -rwxr-xr-x  1 root root   77280 Dec 16  2016 lsblk
131157 lrwxrwxrwx  1 root root       4 Jul 25 14:07 lsmod -> kmod
131158 -rwsr-xr-x  1 root root   40128 May 16 16:37 su
131159 -rwxr-xr-x  1 root root   76848 Feb 18  2016 mkdir
131160 -rwxr-xr-x  1 root root   64496 Feb 18  2016 mknod
131161 -rwxr-xr-x  1 root root   39728 Feb 18  2016 mktemp
131162 -rwxr-xr-x  1 root root   39768 Dec 16  2016 more
131163 -rwsr-xr-x  1 root root   40152 Dec 16  2016 mount
131164 -rwxr-xr-x  1 root root   14768 Dec 16  2016 mountpoint
131165 lrwxrwxrwx  1 root root      20 Jul 25 14:07 mt -> /etc/alternatives/mt
131166 -rwxr-xr-x  1 root root   68824 Feb 18  2016 mt-gnu
131167 -rwxr-xr-x  1 root root  130488 Feb 18  2016 mv
131168 -rwxr-xr-x  1 root root  208480 Dec 16  2016 nano
131169 lrwxrwxrwx  1 root root      20 Jul 25 14:07 nc -> /etc/alternatives/nc
131170 -rwxr-xr-x  1 root root   31248 Dec  3  2012 nc.openbsd
131171 lrwxrwxrwx  1 root root      24 Jul 25 14:07 netcat -> /etc/alternatives/netcat
131172 -rwxr-xr-x  1 root root  119624 Jun 30  2014 netstat
131173 -rwxr-xr-x  1 root root  678496 Jan 18  2017 networkctl
131174 lrwxrwxrwx  1 root root       8 Jul 25 14:07 nisdomainname -> hostname
131175 -rwsr-xr-x  1 root root  142032 Jan 28 08:54 ntfs-3g
131176 -rwxr-xr-x  1 root root   10312 Jan 28 08:54 ntfs-3g.probe
131177 -rwxr-xr-x  1 root root   67608 Jan 28 08:54 ntfs-3g.secaudit
131178 -rwxr-xr-x  1 root root   18424 Jan 28 08:54 ntfs-3g.usermap
131179 -rwxr-xr-x  1 root root   26728 Jan 28 08:54 ntfscat
131180 -rwxr-xr-x  1 root root   30824 Jan 28 08:54 ntfscluster
131181 -rwxr-xr-x  1 root root   34920 Jan 28 08:54 ntfscmp
131182 -rwxr-xr-x  1 root root   34928 Jan 28 08:54 ntfsfallocate
131183 -rwxr-xr-x  1 root root   39024 Jan 28 08:54 ntfsfix
131184 -rwxr-xr-x  1 root root   55416 Jan 28 08:54 ntfsinfo
131185 -rwxr-xr-x  1 root root   31928 Jan 28 08:54 ntfsls
131186 -rwxr-xr-x  1 root root   30824 Jan 28 08:54 ntfsmove
131187 -rwxr-xr-x  1 root root   38944 Jan 28 08:54 ntfstruncate
131188 -rwxr-xr-x  1 root root   47752 Jan 28 08:54 ntfswipe
131189 lrwxrwxrwx  1 root root       6 Jul 25 14:07 open -> openvt
131190 -rwxr-xr-x  1 root root   18968 Sep 22  2016 openvt
131191 -rwxr-xr-x  1 root root   48128 May 16 16:37 login
****Out of Sequence inode detected**** expect 131192 got 131199
131199 lrwxrwxrwx  1 root root      14 Jul 25 14:07 pidof -> /sbin/killall5
131200 -rwsr-xr-x  1 root root   44168 May  7  2014 ping
131201 -rwsr-xr-x  1 root root   44680 May  7  2014 ping6
131202 -rwxr-xr-x  1 root root   35504 May 10  2016 plymouth
****Out of Sequence inode detected**** expect 131203 got 131204
131204 -rwxr-xr-x  1 root root   97408 Nov 21  2016 ps
131205 -rwxr-xr-x  1 root root   31472 Feb 18  2016 pwd
****Out of Sequence inode detected**** expect 131206 got 131207
131207 -rwxr-xr-x  1 root root   39632 Feb 18  2016 readlink
131208 -rwxr-xr-x  1 root root      89 Apr 26  2014 red
****Out of Sequence inode detected**** expect 131209 got 131210
131210 -rwxr-xr-x  1 root root   60272 Feb 18  2016 rm
131211 -rwxr-xr-x  1 root root   39632 Feb 18  2016 rmdir
131212 lrwxrwxrwx  1 root root       4 Jul 25 14:07 rnano -> nano
131213 -rwxr-xr-x  1 root root   19320 Jan 26  2016 run-parts
****Out of Sequence inode detected**** expect 131214 got 131215
131215 -rwxr-xr-x  1 root root   73424 Feb 11  2016 sed
****Out of Sequence inode detected**** expect 131216 got 131218
131218 -rwxr-xr-x  1 root root   36296 Feb  7  2016 setfacl
131219 -rwxr-xr-x  1 root root   39952 Sep 22  2016 setfont
131220 -rwxr-xr-x  1 root root   30875 Feb  1 04:49 setupcon
131221 lrwxrwxrwx  1 root root       4 Jul 25 14:07 sh -> dash
131222 lrwxrwxrwx  1 root root       4 Jul 25 14:07 sh.distrib -> dash
131223 -rwxr-xr-x  1 root root   31408 Feb 18  2016 sleep
131224 -rwxr-xr-x  1 root root  115816 Apr  5  2016 ss
131225 lrwxrwxrwx  1 root root       7 Jul 25 14:07 static-sh -> busybox
131226 -rwxr-xr-x  1 root root   72496 Feb 18  2016 stty
****Out of Sequence inode detected**** expect 131227 got 131228
131228 -rwxr-xr-x  1 root root   31408 Feb 18  2016 sync
****Out of Sequence inode detected**** expect 131229 got 131230
131230 -rwxr-xr-x  1 root root  659848 Jan 18  2017 systemctl
131231 lrwxrwxrwx  1 root root      20 Jul 25 14:07 systemd -> /lib/systemd/systemd
131232 -rwxr-xr-x  1 root root   51656 Jan 18  2017 systemd-ask-password
131233 -rwxr-xr-x  1 root root   39344 Jan 18  2017 systemd-escape
131234 -rwxr-xr-x  1 root root   64080 Jan 18  2017 systemd-hwdb
131235 -rwxr-xr-x  1 root root  281840 Jan 18  2017 systemd-inhibit
131236 -rwxr-xr-x  1 root root   47544 Jan 18  2017 systemd-machine-id-setup
131237 -rwxr-xr-x  1 root root   35248 Jan 18  2017 systemd-notify
131238 -rwxr-xr-x  1 root root  133704 Jan 18  2017 systemd-tmpfiles
131239 -rwxr-xr-x  1 root root   68032 Jan 18  2017 systemd-tty-ask-password-agent
131240 -rwxr-xr-x  1 root root   23144 Dec 16  2016 tailf
131241 -rwxr-xr-x  1 root root  383632 Nov 17  2016 tar
131242 -rwxr-xr-x  1 root root   10416 Jan 26  2016 tempfile
131243 -rwxr-xr-x  1 root root   64432 Feb 18  2016 touch
131244 -rwxr-xr-x  1 root root   27280 Feb 18  2016 true
131245 -rwxr-xr-x  1 root root  449136 Jan 18  2017 udevadm
131246 -rwxr-xr-x  1 root root   14328 Jul 12  2016 ulockmgr_server
131247 -rwsr-xr-x  1 root root   27608 Dec 16  2016 umount
131248 -rwxr-xr-x  1 root root   31440 Feb 18  2016 uname
131249 -rwxr-xr-x  1 root root    2301 Oct 27  2014 uncompress
131250 -rwxr-xr-x  1 root root    2762 Sep 22  2016 unicode_start
****Out of Sequence inode detected**** expect 131251 got 131253
131253 -rwxr-xr-x  1 root root  126584 Feb 18  2016 vdir
131254 -rwxr-xr-x  1 root root   31376 Dec 16  2016 wdctl
131255 -rwxr-xr-x  1 root root     946 Jan 26  2016 which
131256 -rwxr-xr-x  1 root root   27432 Jan 18  2016 whiptail
131257 lrwxrwxrwx  1 root root       8 Jul 25 14:07 ypdomainname -> hostname
131258 -rwxr-xr-x  1 root root    1937 Oct 27  2014 zcat
131259 -rwxr-xr-x  1 root root    1777 Oct 27  2014 zcmp
131260 -rwxr-xr-x  1 root root    5764 Oct 27  2014 zdiff
131261 -rwxr-xr-x  1 root root     140 Oct 27  2014 zegrep
131262 -rwxr-xr-x  1 root root     140 Oct 27  2014 zfgrep
131263 -rwxr-xr-x  1 root root    2131 Oct 27  2014 zforce
131264 -rwxr-xr-x  1 root root    5938 Oct 27  2014 zgrep
131265 -rwxr-xr-x  1 root root    2037 Oct 27  2014 zless
131266 -rwxr-xr-x  1 root root    1910 Oct 27  2014 zmore
131267 -rwxr-xr-x  1 root root    5047 Oct 27  2014 znew
u64@u64-VirtualBox:~/Desktop$
```

```sh
u64@u64-VirtualBox:~/Desktop$ sudo ./out-of-seq-inodes.sh /sbin
./out-of-seq-inodes.sh: line 38: [: : integer expression expected
/sbin:
./out-of-seq-inodes.sh: line 38: [: total: integer expression expected
total 12644
Start inode = 2
2 drwxr-xr-x 24 root root      4096 Jul 27 09:49 ..
****Out of Sequence inode detected**** expect 3 got 786433
786433 drwxr-xr-x  2 root root     12288 Jul 27 09:47 .
786434 -rwxr-xr-x  1 root root     52466 May 18  2013 MAKEDEV
786435 -rwxr-xr-x  1 root root       112 May  1  2014 acpi_available
786436 -rwxr-xr-x  1 root root     44104 Dec 16  2016 agetty
786437 -rwxr-xr-x  1 root root      5576 Jul 30  2015 alsa
786438 -rwxr-xr-x  1 root root       125 May  1  2014 apm_available
786439 -rwxr-xr-x  1 root root       885 May 16 16:37 shadowconfig
786440 -rwxr-xr-x  1 root root     27224 Oct 30  2015 badblocks
786441 -rwxr-xr-x  1 root root     23080 Dec 16  2016 blkdiscard
786442 -rwxr-xr-x  1 root root     81296 Dec 16  2016 blkid
786443 -rwxr-xr-x  1 root root     35624 Dec 16  2016 blockdev
786444 -rwxr-xr-x  1 root root     64240 Apr  5  2016 bridge
786445 -rwxr-xr-x  1 root root    652688 Apr 28  2016 brltty
786446 -rwxr-xr-x  1 root root      1416 Apr 27  2016 brltty-setup
786447 -rwxr-xr-x  1 root root     19032 Oct 23  2015 capsh
786448 -rwxr-xr-x  1 root root     86408 Dec 16  2016 cfdisk
786449 -rwxr-xr-x  1 root root    174256 Feb  7  2016 cgdisk
786450 -rwxr-xr-x  1 root root     23056 Dec 16  2016 chcpu
786451 -rwxr-xr-x  1 root root     10552 Nov 18  2014 crda
****Out of Sequence inode detected**** expect 786452 got 786453
786453 -rwxr-xr-x  1 root root       387 Jun 16 13:59 ldconfig
786454 -rwxr-xr-x  1 root root    996512 Jun 16 13:59 ldconfig.real
****Out of Sequence inode detected**** expect 786455 got 786456
786456 -rwxr-xr-x  1 root root     10592 Dec 16  2016 ctrlaltdel
786457 -rwxr-xr-x  1 root root    150264 Oct 30  2015 debugfs
786458 lrwxrwxrwx  1 root root         9 Jul 25 14:07 depmod -> /bin/kmod
786459 -rwxr-xr-x  1 root root    487248 Dec  9  2016 dhclient
786460 -rwxr-xr-x  1 root root     15219 Dec  9  2016 dhclient-script
****Out of Sequence inode detected**** expect 786461 got 786463
786463 lrwxrwxrwx  1 root root         8 Jul 25 14:07 dosfsck -> fsck.fat
786464 lrwxrwxrwx  1 root root         8 Jul 25 14:07 dosfslabel -> fatlabel
786465 -rwxr-xr-x  1 root root     23136 Oct 30  2015 dumpe2fs
786466 -rwxr-xr-x  1 root root    256952 Oct 30  2015 e2fsck
786467 -rwxr-xr-x  1 root root     31488 Oct 30  2015 e2image
786468 lrwxrwxrwx  1 root root         7 Jul 25 14:07 e2label -> tune2fs
786469 -rwxr-xr-x  1 root root     10656 Oct 30  2015 e2undo
786470 -rwxr-xr-x  1 root root    273784 Apr  1  2016 ethtool
786471 -rwxr-xr-x  1 root root     55376 May 26  2016 fatlabel
786472 -rwxr-xr-x  1 root root    109632 Dec 16  2016 fdisk
786473 -rwxr-xr-x  1 root root     10576 Dec 16  2016 findfs
786474 -rwxr-xr-x  1 root root     59568 Feb  7  2016 fixparts
****Out of Sequence inode detected**** expect 786475 got 786476
786476 -rwxr-xr-x  1 root root     44184 Dec 16  2016 fsck
786477 -rwxr-xr-x  1 root root     35608 Dec 16  2016 fsck.cramfs
786478 lrwxrwxrwx  1 root root         6 Jul 25 14:07 fsck.ext2 -> e2fsck
786479 lrwxrwxrwx  1 root root         6 Jul 25 14:07 fsck.ext3 -> e2fsck
786480 lrwxrwxrwx  1 root root         6 Jul 25 14:07 fsck.ext4 -> e2fsck
786481 lrwxrwxrwx  1 root root         6 Jul 25 14:07 fsck.ext4dev -> e2fsck
786482 -rwxr-xr-x  1 root root     59472 May 26  2016 fsck.fat
786483 -rwxr-xr-x  1 root root     76896 Dec 16  2016 fsck.minix
786484 lrwxrwxrwx  1 root root         8 Jul 25 14:07 fsck.msdos -> fsck.fat
786485 -rwxr-xr-x  1 root root       333 Feb  5  2016 fsck.nfs
786486 lrwxrwxrwx  1 root root         8 Jul 25 14:07 fsck.vfat -> fsck.fat
786487 -rwxr-xr-x  1 root root     10616 Dec 16  2016 fsfreeze
786488 -rwxr-xr-x  1 root root      6360 Feb  5  2016 fstab-decode
786489 -rwxr-xr-x  1 root root     39904 Dec 16  2016 fstrim
786490 -rwxr-xr-x  1 root root    182448 Feb  7  2016 gdisk
786491 -rwxr-xr-x  1 root root     10520 Oct 23  2015 getcap
786492 -rwxr-xr-x  1 root root     10488 Oct 23  2015 getpcaps
786493 lrwxrwxrwx  1 root root         6 Jul 25 14:07 getty -> agetty
786494 lrwxrwxrwx  1 root root        14 Jul 25 14:07 halt -> /bin/systemctl
786495 -rwxr-xr-x  1 root root    122808 Apr  9  2016 hdparm
786496 -rwxr-xr-x  1 root root     56232 Dec 16  2016 hwclock
786497 -rwxr-xr-x  1 root root     68040 Jun 30  2014 ifconfig
786498 lrwxrwxrwx  1 root root         4 Jul 25 14:07 ifdown -> ifup
786499 lrwxrwxrwx  1 root root         4 Jul 25 14:07 ifquery -> ifup
786500 -rwxr-xr-x  1 root root     67536 Dec  9  2016 ifup
786501 lrwxrwxrwx  1 root root        20 Jul 25 14:07 init -> /lib/systemd/systemd
786502 -rwxr-xr-x  1 root root    214216 May 19  2016 initctl
786503 lrwxrwxrwx  1 root root         9 Jul 25 14:07 insmod -> /bin/kmod
786504 -rwxr-xr-x  1 root root      2638 Jan 26  2016 installkernel
786505 lrwxrwxrwx  1 root root         7 Jul 25 14:07 ip -> /bin/ip
786506 lrwxrwxrwx  1 root root        13 Jul 25 14:07 ip6tables -> xtables-multi
786507 lrwxrwxrwx  1 root root        13 Jul 25 14:07 ip6tables-restore -> xtables-multi
786508 lrwxrwxrwx  1 root root        13 Jul 25 14:07 ip6tables-save -> xtables-multi
786509 -rwxr-xr-x  1 root root     18760 Jun 30  2014 ipmaddr
786510 lrwxrwxrwx  1 root root        13 Jul 25 14:07 iptables -> xtables-multi
786511 lrwxrwxrwx  1 root root        13 Jul 25 14:07 iptables-restore -> xtables-multi
786512 lrwxrwxrwx  1 root root        13 Jul 25 14:07 iptables-save -> xtables-multi
786513 -rwxr-xr-x  1 root root     22864 Jun 30  2014 iptunnel
786514 -rwxr-xr-x  1 root root     23072 Dec 16  2016 isosize
786515 -rwxr-xr-x  1 root root    177792 Oct 24  2014 iw
786516 -rwxr-xr-x  1 root root     27008 May  3  2012 iwconfig
786517 -rwxr-xr-x  1 root root     14720 May  3  2012 iwevent
786518 -rwxr-xr-x  1 root root     14528 May  3  2012 iwgetid
786519 -rwxr-xr-x  1 root root     35352 May  3  2012 iwlist
786520 -rwxr-xr-x  1 root root     14608 May  3  2012 iwpriv
786521 -rwxr-xr-x  1 root root     14568 May  3  2012 iwspy
786522 -rwxr-xr-x  1 root root     10616 Sep 22  2016 kbdrate
****Out of Sequence inode detected**** expect 786523 got 786524
786524 -rwxr-xr-x  1 root root     19056 Feb  5  2016 killall5
****Out of Sequence inode detected**** expect 786525 got 786527
786527 -rwxr-xr-x  1 root root     10600 Oct 30  2015 logsave
786528 -rwxr-xr-x  1 root root     72920 Dec 16  2016 losetup
786529 lrwxrwxrwx  1 root root         9 Jul 25 14:07 lsmod -> /bin/kmod
786530 lrwxrwxrwx  1 root root         9 Jul 25 14:07 lspcmcia -> pccardctl
****Out of Sequence inode detected**** expect 786531 got 786552
786552 -rwxr-xr-x  1 root root     19264 Jun 30  2014 mii-tool
786553 lrwxrwxrwx  1 root root         8 Jul 25 14:07 mkdosfs -> mkfs.fat
786554 -rwxr-xr-x  1 root root    106392 Oct 30  2015 mke2fs
786555 -rwxr-xr-x  1 root root     10592 Dec 16  2016 mkfs
786556 -rwxr-xr-x  1 root root     27224 Dec 16  2016 mkfs.bfs
786557 -rwxr-xr-x  1 root root     35456 Dec 16  2016 mkfs.cramfs
786558 lrwxrwxrwx  1 root root         6 Jul 25 14:07 mkfs.ext2 -> mke2fs
786559 lrwxrwxrwx  1 root root         6 Jul 25 14:07 mkfs.ext3 -> mke2fs
786560 lrwxrwxrwx  1 root root         6 Jul 25 14:07 mkfs.ext4 -> mke2fs
786561 lrwxrwxrwx  1 root root         6 Jul 25 14:07 mkfs.ext4dev -> mke2fs
786562 -rwxr-xr-x  1 root root     27128 May 26  2016 mkfs.fat
786563 -rwxr-xr-x  1 root root     76912 Dec 16  2016 mkfs.minix
786564 lrwxrwxrwx  1 root root         8 Jul 25 14:07 mkfs.msdos -> mkfs.fat
786565 lrwxrwxrwx  1 root root         6 Jul 25 14:07 mkfs.ntfs -> mkntfs
786566 lrwxrwxrwx  1 root root         8 Jul 25 14:07 mkfs.vfat -> mkfs.fat
786567 -rwxr-xr-x  1 root root     18848 Mar 16  2016 mkhomedir_helper
786568 -rwxr-xr-x  1 root root     84080 Jan 28 08:54 mkntfs
786569 -rwxr-xr-x  1 root root     72944 Dec 16  2016 mkswap
786570 -rwxr-xr-x  1 root root     35256 Nov 18  2014 mntctl
786571 lrwxrwxrwx  1 root root         9 Jul 25 14:07 modinfo -> /bin/kmod
786572 lrwxrwxrwx  1 root root         9 Jul 25 14:07 modprobe -> /bin/kmod
****Out of Sequence inode detected**** expect 786573 got 786575
786575 -rwxr-xr-x  1 root root     10232 Jul 12  2016 mount.fuse
786576 lrwxrwxrwx  1 root root        15 Jul 25 14:07 mount.lowntfs-3g -> /bin/lowntfs-3g
786577 lrwxrwxrwx  1 root root        13 Jul 25 14:07 mount.ntfs -> mount.ntfs-3g
786578 lrwxrwxrwx  1 root root        12 Jul 25 14:07 mount.ntfs-3g -> /bin/ntfs-3g
786579 -rwxr-xr-x  1 root root    105048 Nov 18  2014 mountall
786580 -rwxr-xr-x  1 root root     14816 Jun 30  2014 nameif
786581 -rwxr-xr-x  1 root root     55408 Jan 28 08:54 ntfsclone
786582 -rwxr-xr-x  1 root root     34920 Jan 28 08:54 ntfscp
786583 -rwxr-xr-x  1 root root     26728 Jan 28 08:54 ntfslabel
786584 -rwxr-xr-x  1 root root     71792 Jan 28 08:54 ntfsresize
786585 -rwxr-xr-x  1 root root     51304 Jan 28 08:54 ntfsundelete
786586 -rwxr-xr-x  1 root root      2251 Dec  2  2009 on_ac_power
786587 -rwxr-sr-x  1 root shadow   35632 Mar 16  2016 pam_extrausers_chkpwd
786588 -rwxr-xr-x  1 root root     35568 Mar 16  2016 pam_extrausers_update
786589 -rwxr-xr-x  1 root root     10600 Mar 16  2016 pam_tally
786590 -rwxr-xr-x  1 root root     14784 Mar 16  2016 pam_tally2
786591 -rwxr-xr-x  1 root root     80136 Feb 11  2016 parted
786592 -rwxr-xr-x  1 root root     10312 Feb 11  2016 partprobe
786593 -rwxr-xr-x  1 root root     18800 Jun 28  2012 pccardctl
786594 -rwxr-xr-x  1 root root     10568 Dec 16  2016 pivot_root
786595 -rwxr-xr-x  1 root root     10448 Jun 30  2014 plipconfig
786596 -rwxr-xr-x  1 root root     85728 May 10  2016 plymouthd
786597 lrwxrwxrwx  1 root root        14 Jul 25 14:07 poweroff -> /bin/systemctl
****Out of Sequence inode detected**** expect 786598 got 786607
786607 -rwxr-xr-x  1 root root     29800 Jun 30  2014 rarp
786608 -rwxr-xr-x  1 root root     14712 Dec 16  2016 raw
786609 lrwxrwxrwx  1 root root        14 Jul 25 14:07 reboot -> /bin/systemctl
786610 -rwxr-xr-x  1 root root      6280 Nov 18  2014 regdbdump
786611 lrwxrwxrwx  1 root root         7 Jul 25 14:07 reload -> initctl
****Out of Sequence inode detected**** expect 786612 got 786613
786613 -rwxr-xr-x  1 root root     52336 Oct 30  2015 resize2fs
786614 -rwxr-xr-x  1 root root      4590 Feb 28  2016 resolvconf
786615 lrwxrwxrwx  1 root root         7 Jul 25 14:07 restart -> initctl
786616 lrwxrwxrwx  1 root root         9 Jul 25 14:07 rmmod -> /bin/kmod
786617 -rwxr-xr-x  1 root root     58032 Jun 30  2014 route
786618 -rwxr-xr-x  1 root root     37464 Apr  5  2016 rtacct
786619 -rwxr-xr-x  1 root root     43608 Apr  5  2016 rtmon
786620 lrwxrwxrwx  1 root root        14 Jul 25 14:07 runlevel -> /bin/systemctl
786621 -rwxr-xr-x  1 root root     31728 Dec 16  2016 runuser
****Out of Sequence inode detected**** expect 786622 got 786623
786623 -rwxr-xr-x  1 root root     10544 Oct 23  2015 setcap
786624 -rwxr-xr-x  1 root root     10664 Sep 22  2016 setvtrgb
786625 -rwxr-xr-x  1 root root     94280 Dec 16  2016 sfdisk
786626 -rwxr-xr-x  1 root root    170160 Feb  7  2016 sgdisk
****Out of Sequence inode detected**** expect 786627 got 786628
786628 lrwxrwxrwx  1 root root        14 Jul 25 14:07 shutdown -> /bin/systemctl
786629 -rwxr-xr-x  1 root root     33928 Jun 30  2014 slattach
786630 lrwxrwxrwx  1 root root         7 Jul 25 14:07 start -> initctl
786631 -rwxr-xr-x  1 root root     32528 May 12  2016 start-stop-daemon
786632 lrwxrwxrwx  1 root root         7 Jul 25 14:07 status -> initctl
786633 lrwxrwxrwx  1 root root         7 Jul 25 14:07 stop -> initctl
786634 -rwxr-xr-x  1 root root     44152 Dec 16  2016 sulogin
786635 -rwxr-xr-x  1 root root     14776 Dec 16  2016 swaplabel
786636 -rwxr-xr-x  1 root root     19024 Dec 16  2016 swapoff
786637 -rwxr-xr-x  1 root root     44288 Dec 16  2016 swapon
786638 -rwxr-xr-x  1 root root     14808 Dec 16  2016 switch_root
786639 -rwxr-xr-x  1 root root     23048 Nov 21  2016 sysctl
786640 -rwxr-xr-x  1 root root    333864 Apr  5  2016 tc
786641 lrwxrwxrwx  1 root root        14 Jul 25 14:07 telinit -> /bin/systemctl
786642 -rwxr-xr-x  1 root root     43400 Apr  5  2016 tipc
786643 -rwxr-xr-x  1 root root     77368 Oct 30  2015 tune2fs
786644 -rwxr-xr-x  1 root root       517 Aug 25  2016 u-d-c-print-pci-ids
786645 lrwxrwxrwx  1 root root        12 Jul 25 14:07 udevadm -> /bin/udevadm
****Out of Sequence inode detected**** expect 786646 got 786648
786648 -rwxr-xr-x  1 root root     10560 Apr  1  2016 umount.udisks2
786649 -rwxr-sr-x  1 root shadow   35600 Mar 16  2016 unix_chkpwd
786650 -rwxr-xr-x  1 root root     35536 Mar 16  2016 unix_update
786651 -rwxr-xr-x  1 root root    302920 May 19  2016 upstart
786652 -rwxr-xr-x  1 root root    150024 May 19  2016 upstart-dbus-bridge
786653 -rwxr-xr-x  1 root root    141544 May 19  2016 upstart-event-bridge
786654 -rwxr-xr-x  1 root root    157992 May 19  2016 upstart-file-bridge
786655 -rwxr-xr-x  1 root root    100776 May 19  2016 upstart-local-bridge
786656 -rwxr-xr-x  1 root root    149736 May 19  2016 upstart-socket-bridge
786657 -rwxr-xr-x  1 root root     88392 May 19  2016 upstart-udev-bridge
786658 -rwxr-xr-x  1 root root     35168 Feb 24  2015 ureadahead
****Out of Sequence inode detected**** expect 786659 got 786679
786679 -rwxr-xr-x  1 root root     31464 Dec 16  2016 wipefs
786680 -rwxr-xr-x  1 root root      1735 Jul 17  2015 wpa_action
786681 -rwxr-xr-x  1 root root    119656 Jan 19  2016 wpa_cli
786682 -rwxr-xr-x  1 root root   2156080 Jan 19  2016 wpa_supplicant
786683 -rwxr-xr-x  1 root root     87832 Feb 19  2016 xtables-multi
786684 -rwxr-xr-x  1 root root     77064 Dec 16  2016 zramctl
****Out of Sequence inode detected**** expect 786685 got 800338
800338 -rwxr-xr-x  1 root root   1287072 Mar 15 18:11 apparmor_parser
u64@u64-VirtualBox:~/Desktop$
```

###### Using the script on the target

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

```sh
u64@u64-VirtualBox:~/Desktop$ sudo ./out-of-seq-inodes.sh /media/part0/bin/
./out-of-seq-inodes.sh: line 38: [: : integer expression expected
/media/part0/bin/:
./out-of-seq-inodes.sh: line 38: [: total: integer expression expected
total 10940
Start inode = 2
2 drwxr-xr-x 23 root root    4096 Mar  5  2015 ..
****Out of Sequence inode detected**** expect 3 got 655361
655361 drwxr-xr-x  2 root root    4096 Mar  9  2015 .
****Out of Sequence inode detected**** expect 655362 got 655368
655368 -rwxr-xr-x  1 root root 1021112 Oct  7  2014 bash
****Out of Sequence inode detected**** expect 655369 got 655372
655372 -rwxr-xr-x  1 root root   31152 Oct 21  2013 bunzip2
655373 -rwxr-xr-x  1 root root 1918032 Nov 14  2013 busybox
655374 -rwxr-xr-x  1 root root   31152 Oct 21  2013 bzcat
655375 lrwxrwxrwx  1 root root       6 Mar  5  2015 bzcmp -> bzdiff
655376 -rwxr-xr-x  1 root root    2140 Oct 21  2013 bzdiff
655377 lrwxrwxrwx  1 root root       6 Mar  5  2015 bzegrep -> bzgrep
655378 -rwxr-xr-x  1 root root    4877 Oct 21  2013 bzexe
655379 lrwxrwxrwx  1 root root       6 Mar  5  2015 bzfgrep -> bzgrep
655380 -rwxr-xr-x  1 root root    3642 Oct 21  2013 bzgrep
655381 -rwxr-xr-x  1 root root   31152 Oct 21  2013 bzip2
655382 -rwxr-xr-x  1 root root   14480 Oct 21  2013 bzip2recover
655383 lrwxrwxrwx  1 root root       6 Mar  5  2015 bzless -> bzmore
655384 -rwxr-xr-x  1 root root    1297 Oct 21  2013 bzmore
655385 -rwxr-xr-x  1 root root   47904 Jan 13  2015 cat
655386 -rwxr-xr-x  1 root root   14688 May 23  2013 chacl
****Out of Sequence inode detected**** expect 655387 got 655388
655388 -rwxr-xr-x  1 root root   60160 Jan 13  2015 chgrp
655389 -rwxr-xr-x  1 root root   56032 Jan 13  2015 chmod
655390 -rwxr-xr-x  1 root root   60160 Jan 13  2015 chown
655391 -rwxr-xr-x  1 root root   10480 Feb 18  2013 chvt
655392 -rwxr-xr-x  1 root root  130304 Jan 13  2015 cp
655393 -rwxr-xr-x  1 root root  137272 Jan  7  2015 cpio
655394 -rwxr-xr-x  1 root root  121272 Feb 19  2014 dash
655395 -rwxr-xr-x  1 root root   60160 Jan 13  2015 date
655396 -rwxr-xr-x  1 root root   10536 Nov 25  2014 dbus-cleanup-sockets
655397 -rwxr-xr-x  1 root root  434032 Nov 25  2014 dbus-daemon
655398 -rwxr-xr-x  1 root root   10464 Nov 25  2014 dbus-uuidgen
655399 -rwxr-xr-x  1 root root   56136 Jan 13  2015 dd
****Out of Sequence inode detected**** expect 655400 got 655402
655402 -rwxr-xr-x  1 root root   97736 Jan 13  2015 df
655403 -rwxr-xr-x  1 root root  110080 Jan 13  2015 dir
655404 -rwxr-xr-x  1 root root   22896 Feb 12  2015 dmesg
655405 lrwxrwxrwx  1 root root       8 Mar  5  2015 dnsdomainname -> hostname
655406 lrwxrwxrwx  1 root root       8 Mar  5  2015 domainname -> hostname
655407 -rwxr-xr-x  1 root root   82256 Feb 18  2013 dumpkeys
655408 -rwxr-xr-x  1 root root   31296 Jan 13  2015 echo
655409 -rwxr-xr-x  1 root root   47712 Jul 16  2013 ed
655410 -rwxr-xr-x  1 root root  183696 Jan 18  2014 egrep
655411 -rwxr-xr-x  1 root root 1021112 Mar  9  2015 false
****Out of Sequence inode detected**** expect 655412 got 655413
655413 -rwxr-xr-x  1 root root   10488 Feb 18  2013 fgconsole
655414 -rwxr-xr-x  1 root root  138352 Jan 18  2014 fgrep
655415 -rwxr-xr-x  1 root root   36144 Feb 12  2015 findmnt
655416 -rwxr-xr-x  1 root root   31864 Nov 29  2012 fuser
655417 -rwsr-xr-x  1 root root   30800 Dec 16  2013 fusermount
****Out of Sequence inode detected**** expect 655418 got 655419
655419 -rwxr-xr-x  1 root root   23688 May 23  2013 getfacl
655420 -rwxr-xr-x  1 root root  191952 Jan 18  2014 grep
655421 -rwxr-xr-x  1 root root    2303 Jan 10  2014 gunzip
655422 -rwxr-xr-x  1 root root    5937 Jan 10  2014 gzexe
655423 -rwxr-xr-x  1 root root   94048 Jan 10  2014 gzip
655424 -rwxr-xr-x  1 root root   14736 Dec 13  2013 hostname
****Out of Sequence inode detected**** expect 655425 got 655427
655427 -rwxr-xr-x  1 root root  307328 Feb 17  2014 ip
655428 -rwxr-xr-x  1 root root   10480 Feb 18  2013 kbd_mode
****Out of Sequence inode detected**** expect 655429 got 655430
655430 -rwxr-xr-x  1 root root   23088 Feb 10  2015 kill
655431 -rwxr-xr-x  1 root root  154616 Apr 10  2014 kmod
655432 -rwxr-xr-x  1 root root  153664 Jun 10  2013 less
655433 -rwxr-xr-x  1 root root   10440 Jun 10  2013 lessecho
655434 lrwxrwxrwx  1 root root       8 Mar  5  2015 lessfile -> lesspipe
655435 -rwxr-xr-x  1 root root   15912 Jun 10  2013 lesskey
655436 -rwxr-xr-x  1 root root    7758 Jun 10  2013 lesspipe
****Out of Sequence inode detected**** expect 655437 got 655438
655438 -rwxr-xr-x  1 root root   56072 Jan 13  2015 ln
655439 -rwxr-xr-x  1 root root  111432 Feb 18  2013 loadkeys
****Out of Sequence inode detected**** expect 655440 got 655441
655441 -rwxr-xr-x  1 root root   49136 Feb 16  2014 login
655442 -rwxr-xr-x  1 root root   92328 Feb  4  2015 loginctl
655443 -rwxr-xr-x  1 root root   63912 Dec 18  2013 lowntfs-3g
655444 -rwxr-xr-x  1 root root  110080 Jan 13  2015 ls
655445 -rwxr-xr-x  1 root root   44688 Feb 12  2015 lsblk
655446 lrwxrwxrwx  1 root root       4 Mar  5  2015 lsmod -> kmod
****Out of Sequence inode detected**** expect 655447 got 655448
655448 -rwxr-xr-x  1 root root   51936 Jan 13  2015 mkdir
655449 -rwxr-xr-x  1 root root   35456 Jan 13  2015 mknod
655450 -rwxr-xr-x  1 root root   39648 Jan 13  2015 mktemp
655451 -rwxr-xr-x  1 root root   39600 Feb 12  2015 more
655452 -rwsr-xr-x  1 root root   94792 Feb 12  2015 mount
655453 -rwxr-xr-x  1 root root   10456 Mar 12  2014 mountpoint
655454 lrwxrwxrwx  1 root root      20 Mar  5  2015 mt -> /etc/alternatives/mt
655455 -rwxr-xr-x  1 root root   68760 Jan  7  2015 mt-gnu
655456 -rwxr-xr-x  1 root root  122088 Jan 13  2015 mv
655457 -rwxr-xr-x  1 root root  192008 Oct  1  2012 nano
655458 lrwxrwxrwx  1 root root      20 Mar  5  2015 nc -> /etc/alternatives/nc
655459 -rwxr-xr-x  1 root root   31248 Dec  3  2012 nc.openbsd
655460 lrwxrwxrwx  1 root root      24 Mar  5  2015 netcat -> /etc/alternatives/netcat
655461 -rwxr-xr-x  1 root root  119624 Aug  5  2014 netstat
655462 lrwxrwxrwx  1 root root       8 Mar  5  2015 nisdomainname -> hostname
655463 -rwxr-xr-x  1 root root   59848 Dec 18  2013 ntfs-3g
655464 -rwxr-xr-x  1 root root   10312 Dec 18  2013 ntfs-3g.probe
655465 -rwxr-xr-x  1 root root   67608 Dec 18  2013 ntfs-3g.secaudit
655466 -rwxr-xr-x  1 root root   18432 Dec 18  2013 ntfs-3g.usermap
655467 -rwxr-xr-x  1 root root   26728 Dec 18  2013 ntfscat
655468 -rwxr-xr-x  1 root root   30752 Dec 18  2013 ntfsck
655469 -rwxr-xr-x  1 root root   30824 Dec 18  2013 ntfscluster
655470 -rwxr-xr-x  1 root root   34920 Dec 18  2013 ntfscmp
655471 -rwxr-xr-x  1 root root   22528 Dec 18  2013 ntfsdump_logfile
655472 -rwxr-xr-x  1 root root   39024 Dec 18  2013 ntfsfix
655473 -rwxr-xr-x  1 root root   55416 Dec 18  2013 ntfsinfo
655474 -rwxr-xr-x  1 root root   31928 Dec 18  2013 ntfsls
655475 -rwxr-xr-x  1 root root   26672 Dec 18  2013 ntfsmftalloc
655476 -rwxr-xr-x  1 root root   30824 Dec 18  2013 ntfsmove
655477 -rwxr-xr-x  1 root root   34856 Dec 18  2013 ntfstruncate
655478 -rwxr-xr-x  1 root root   43632 Dec 18  2013 ntfswipe
655479 lrwxrwxrwx  1 root root       6 Mar  5  2015 open -> openvt
655480 -rwxr-xr-x  1 root root   18912 Feb 18  2013 openvt
****Out of Sequence inode detected**** expect 655481 got 655489
655489 lrwxrwxrwx  1 root root      14 Mar  5  2015 pidof -> /sbin/killall5
655490 -rwsr-xr-x  1 root root   44168 May  7  2014 ping
655491 -rwsr-xr-x  1 root root   44680 May  7  2014 ping6
655492 -rwxr-xr-x  1 root root   35448 Dec  2  2014 plymouth
655493 -rwxr-xr-x  1 root root   31608 Dec  2  2014 plymouth-upstart-bridge
****Out of Sequence inode detected**** expect 655494 got 655495
655495 -rwxr-xr-x  1 root root   93232 Feb 10  2015 ps
655496 -rwxr-xr-x  1 root root   31392 Jan 13  2015 pwd
655497 lrwxrwxrwx  1 root root       4 Mar  5  2015 rbash -> bash
655498 -rwxr-xr-x  1 root root   39528 Jan 13  2015 readlink
655499 -rwxr-xr-x  1 root root      89 Jul 16  2013 red
****Out of Sequence inode detected**** expect 655500 got 655501
655501 -rwxr-xr-x  1 root root   60160 Jan 13  2015 rm
655502 -rwxr-xr-x  1 root root   43648 Jan 13  2015 rmdir
655503 lrwxrwxrwx  1 root root       4 Mar  5  2015 rnano -> nano
655504 -rwxr-xr-x  1 root root   19248 Aug 27  2013 run-parts
655505 -rwxr-xr-x  1 root root     254 Jul 18  2014 running-in-container
****Out of Sequence inode detected**** expect 655506 got 655507
655507 -rwxr-xr-x  1 root root   73352 Feb 13  2014 sed
****Out of Sequence inode detected**** expect 655508 got 655510
655510 -rwxr-xr-x  1 root root   36232 May 23  2013 setfacl
655511 -rwxr-xr-x  1 root root   39896 Feb 18  2013 setfont
655512 -rwxr-xr-x  1 root root   12052 Jan 29  2014 setupcon
655513 lrwxrwxrwx  1 root root       4 Mar  5  2015 sh -> dash
655514 lrwxrwxrwx  1 root root       4 Mar  5  2015 sh.distrib -> dash
655515 -rwxr-xr-x  1 root root   31296 Jan 13  2015 sleep
655516 -rwxr-xr-x  1 root root   76624 Feb 17  2014 ss
655517 lrwxrwxrwx  1 root root       7 Mar  5  2015 static-sh -> busybox
655518 -rwxr-xr-x  1 root root   68256 Jan 13  2015 stty
655519 -rwsr-xr-x  1 root root   36936 Feb 16  2014 su
655520 -rwxr-xr-x  1 root root   27200 Jan 13  2015 sync
****Out of Sequence inode detected**** expect 655521 got 655522
655522 -rwxr-xr-x  1 root root   18816 Feb 12  2015 tailf
655523 -rwxr-xr-x  1 root root  353840 Feb  4  2014 tar
655524 -rwxr-xr-x  1 root root   10344 Aug 27  2013 tempfile
655525 -rwxr-xr-x  1 root root   60224 Jan 13  2015 touch
655526 -rwxr-xr-x  1 root root   27168 Jan 13  2015 true
655527 -rwxr-xr-x  1 root root  248040 Feb  4  2015 udevadm
655528 -rwxr-xr-x  1 root root   14336 Dec 16  2013 ulockmgr_server
655529 -rwsr-xr-x  1 root root   69120 Feb 12  2015 umount
655530 -rwxr-xr-x  1 root root   31360 Jan 13  2015 uname
655531 -rwxr-xr-x  1 root root    2303 Jan 10  2014 uncompress
655532 -rwxr-xr-x  1 root root    2762 Feb 18  2013 unicode_start
****Out of Sequence inode detected**** expect 655533 got 655535
655535 -rwxr-xr-x  1 root root  110080 Jan 13  2015 vdir
655536 -rwxr-xr-x  1 root root    6248 Jan 28  2015 vmmouse_detect
655537 -rwxr-xr-x  1 root root     946 Aug 27  2013 which
655538 -rwxr-xr-x  1 root root   27368 Mar 23  2014 whiptail
655539 lrwxrwxrwx  1 root root       8 Mar  5  2015 ypdomainname -> hostname
655540 -rwxr-xr-x  1 root root    1939 Jan 10  2014 zcat
655541 -rwxr-xr-x  1 root root    1779 Jan 10  2014 zcmp
655542 -rwxr-xr-x  1 root root    5766 Jan 10  2014 zdiff
655543 -rwxr-xr-x  1 root root     142 Jan 10  2014 zegrep
655544 -rwxr-xr-x  1 root root     142 Jan 10  2014 zfgrep
655545 -rwxr-xr-x  1 root root    2133 Jan 10  2014 zforce
655546 -rwxr-xr-x  1 root root    5940 Jan 10  2014 zgrep
655547 -rwxr-xr-x  1 root root    2039 Jan 10  2014 zless
655548 -rwxr-xr-x  1 root root    1912 Jan 10  2014 zmore
655549 -rwxr-xr-x  1 root root    5049 Jan 10  2014 znew
****Out of Sequence inode detected**** expect 655550 got 657076
657076 -rwxr-xr-x  1 root root   14056 Mar 12  2015 xingyi_reverse_shell
****Out of Sequence inode detected**** expect 657077 got 657094
657094 -rwxr-xr-x  1 root root   27096 Jun 13  2012 nc.traditional
****Out of Sequence inode detected**** expect 657095 got 657103
657103 -rwxr-xr-x  1 root root   14723 Mar 12  2015 xingyi_bindshell
****Out of Sequence inode detected**** expect 657104 got 657109
657109 -rwxr-xr-x  1 root root    9660 Mar 12  2015 xingyi_rootshell
u64@u64-VirtualBox:~/Desktop$
```

```sh
u64@u64-VirtualBox:~/Desktop$ sudo ./out-of-seq-inodes.sh /media/part0/sbin/
./out-of-seq-inodes.sh: line 38: [: : integer expression expected
/media/part0/sbin/:
./out-of-seq-inodes.sh: line 38: [: total: integer expression expected
total 12100
Start inode = 2
2 drwxr-xr-x 23 root root      4096 Mar  5  2015 ..
****Out of Sequence inode detected**** expect 3 got 524291
524291 drwxr-xr-x  2 root root     12288 Mar  5  2015 .
****Out of Sequence inode detected**** expect 524292 got 524295
524295 -rwxr-xr-x  1 root root       387 Feb 25  2015 ldconfig
****Out of Sequence inode detected**** expect 524296 got 524305
524305 -rwxr-xr-x  1 root root    951888 Feb 25  2015 ldconfig.real
****Out of Sequence inode detected**** expect 524306 got 525304
525304 lrwxrwxrwx  1 root root        57 Mar  5  2015 mount.vboxsf -> /usr/lib/x86_64-linux-gnu/VBoxGuestAdditions/mount.vboxsf
****Out of Sequence inode detected**** expect 525305 got 528959
528959 -rwxr-xr-x  1 root root     10544 Feb 16  2015 logsave
****Out of Sequence inode detected**** expect 528960 got 528981
528981 -rwxr-xr-x  1 root root     31432 Feb 16  2015 e2image
528982 -rwxr-xr-x  1 root root     68952 Feb 16  2015 tune2fs
****Out of Sequence inode detected**** expect 528983 got 528986
528986 -rwxr-xr-x  1 root root     48160 Feb 16  2015 resize2fs
****Out of Sequence inode detected**** expect 528987 got 528993
528993 -rwxr-xr-x  1 root root     10592 Feb 16  2015 e2undo
528994 -rwxr-xr-x  1 root root    248344 Feb 16  2015 e2fsck
528995 -rwxr-xr-x  1 root root     23072 Feb 16  2015 dumpe2fs
****Out of Sequence inode detected**** expect 528996 got 528998
528998 -rwxr-xr-x  1 root root     97944 Feb 16  2015 mke2fs
528999 -rwxr-xr-x  1 root root     27160 Feb 16  2015 badblocks
****Out of Sequence inode detected**** expect 529000 got 529026
529026 -rwxr-xr-x  1 root root    116672 Feb 16  2015 debugfs
****Out of Sequence inode detected**** expect 529027 got 529045
529045 lrwxrwxrwx  1 root root         6 Feb 16  2015 fsck.ext4dev -> e2fsck
****Out of Sequence inode detected**** expect 529046 got 529049
529049 lrwxrwxrwx  1 root root         6 Feb 16  2015 mkfs.ext4dev -> mke2fs
****Out of Sequence inode detected**** expect 529050 got 529052
529052 lrwxrwxrwx  1 root root         6 Feb 16  2015 fsck.ext2 -> e2fsck
****Out of Sequence inode detected**** expect 529053 got 529061
529061 lrwxrwxrwx  1 root root         6 Feb 16  2015 mkfs.ext3 -> mke2fs
****Out of Sequence inode detected**** expect 529062 got 529063
529063 lrwxrwxrwx  1 root root         7 Feb 16  2015 e2label -> tune2fs
****Out of Sequence inode detected**** expect 529064 got 529096
529096 lrwxrwxrwx  1 root root         6 Feb 16  2015 mkfs.ext2 -> mke2fs
****Out of Sequence inode detected**** expect 529097 got 529104
529104 lrwxrwxrwx  1 root root         6 Feb 16  2015 fsck.ext4 -> e2fsck
****Out of Sequence inode detected**** expect 529105 got 529119
529119 lrwxrwxrwx  1 root root         6 Feb 16  2015 mkfs.ext4 -> mke2fs
****Out of Sequence inode detected**** expect 529120 got 529248
529248 -rwxr-xr-x  1 root root     52466 May 18  2013 MAKEDEV
529249 -rwxr-xr-x  1 root root      6248 Oct  2  2012 acpi_available
529250 -rwxr-xr-x  1 root root     32112 Feb 12  2015 agetty
529251 -rwxr-xr-x  1 root root      5576 Feb 13  2013 alsa
529252 -rwxr-xr-x  1 root root      6272 Oct  2  2012 apm_available
529253 -rwxr-xr-x  1 root root    849048 Nov 14  2014 apparmor_parser
****Out of Sequence inode detected**** expect 529254 got 529255
529255 -rwxr-xr-x  1 root root     31544 Feb 12  2015 blkid
529256 -rwxr-xr-x  1 root root     23016 Feb 12  2015 blockdev
529257 -rwxr-xr-x  1 root root     51768 Feb 17  2014 bridge
529258 -rwxr-xr-x  1 root root    600768 Mar 31  2014 brltty
529259 -rwxr-xr-x  1 root root      1416 Mar 13  2014 brltty-setup
529260 -rwxr-xr-x  1 root root     18976 Feb 21  2014 capsh
529261 -rwxr-xr-x  1 root root     54368 Feb 12  2015 cfdisk
529262 -rwxr-xr-x  1 root root    171056 Dec 26  2013 cgdisk
529263 -rwxr-xr-x  1 root root     14720 Oct  1  2012 crda
****Out of Sequence inode detected**** expect 529264 got 529268
529268 -rwxr-xr-x  1 root root      6288 Feb 12  2015 ctrlaltdel
****Out of Sequence inode detected**** expect 529269 got 529270
529270 lrwxrwxrwx  1 root root         9 Mar  5  2015 depmod -> /bin/kmod
529271 -rwxr-xr-x  1 root root   1668160 Apr  7  2014 dhclient
529272 -rwxr-xr-x  1 root root     14484 Apr  7  2014 dhclient-script
529273 -rwxr-xr-x  1 root root     71592 Dec 13  2013 dmsetup
529274 lrwxrwxrwx  1 root root         8 Mar  5  2015 dosfsck -> fsck.fat
529275 lrwxrwxrwx  1 root root         8 Mar  5  2015 dosfslabel -> fatlabel
****Out of Sequence inode detected**** expect 529276 got 529281
529281 -rwxr-xr-x  1 root root    257256 Jan 29  2014 ethtool
529282 -rwxr-xr-x  1 root root     51696 Mar 18  2014 fatlabel
529283 -rwxr-xr-x  1 root root     99488 Feb 12  2015 fdisk
529284 -rwxr-xr-x  1 root root      6304 Feb 12  2015 findfs
529285 -rwxr-xr-x  1 root root     60088 Dec 26  2013 fixparts
****Out of Sequence inode detected**** expect 529286 got 529287
529287 -rwxr-xr-x  1 root root     31608 Feb 12  2015 fsck
529288 -rwxr-xr-x  1 root root     14640 Feb 12  2015 fsck.cramfs
****Out of Sequence inode detected**** expect 529289 got 529293
529293 -rwxr-xr-x  1 root root     55800 Mar 18  2014 fsck.fat
529294 -rwxr-xr-x  1 root root     31200 Feb 12  2015 fsck.minix
529295 lrwxrwxrwx  1 root root         8 Mar  5  2015 fsck.msdos -> fsck.fat
529296 -rwxr-xr-x  1 root root       333 Mar 12  2014 fsck.nfs
529297 lrwxrwxrwx  1 root root         8 Mar  5  2015 fsck.vfat -> fsck.fat
529298 -rwxr-xr-x  1 root root     10440 Feb 12  2015 fsfreeze
529299 -rwxr-xr-x  1 root root      6304 Mar 12  2014 fstab-decode
529300 -rwxr-xr-x  1 root root     14616 Feb 12  2015 fstrim
529301 -rwxr-xr-x  1 root root      3002 Feb 12  2015 fstrim-all
529302 -rwxr-xr-x  1 root root    179040 Dec 26  2013 gdisk
529303 -rwxr-xr-x  1 root root     10456 Feb 21  2014 getcap
529304 -rwxr-xr-x  1 root root      6328 Feb 21  2014 getpcaps
529305 -rwxr-xr-x  1 root root     32112 Feb 12  2015 getty
529306 lrwxrwxrwx  1 root root         6 Mar  5  2015 halt -> reboot
529307 -rwxr-xr-x  1 root root    103056 Nov 15  2013 hdparm
529308 -rwxr-xr-x  1 root root     35384 Feb 12  2015 hwclock
529309 -rwxr-xr-x  1 root root     68040 Aug  5  2014 ifconfig
529310 lrwxrwxrwx  1 root root         4 Mar  5  2015 ifdown -> ifup
529311 lrwxrwxrwx  1 root root         4 Mar  5  2015 ifquery -> ifup
529312 -rwxr-xr-x  1 root root     62960 May 12  2014 ifup
529313 -rwxr-xr-x  1 root root    265848 Jul 18  2014 init
529314 -rwxr-xr-x  1 root root    193512 Apr 11  2014 initctl
529315 lrwxrwxrwx  1 root root         9 Mar  5  2015 insmod -> /bin/kmod
529316 -rwxr-xr-x  1 root root      2382 Aug 27  2013 installkernel
529317 lrwxrwxrwx  1 root root         7 Mar  5  2015 ip -> /bin/ip
529318 lrwxrwxrwx  1 root root        13 Mar  5  2015 ip6tables -> xtables-multi
529319 lrwxrwxrwx  1 root root        14 Mar  5  2015 ip6tables-apply -> iptables-apply
529320 lrwxrwxrwx  1 root root        13 Mar  5  2015 ip6tables-restore -> xtables-multi
529321 lrwxrwxrwx  1 root root        13 Mar  5  2015 ip6tables-save -> xtables-multi
529322 -rwxr-xr-x  1 root root     18760 Aug  5  2014 ipmaddr
529323 lrwxrwxrwx  1 root root        13 Mar  5  2015 iptables -> xtables-multi
529324 -rwxr-xr-x  1 root root      7016 Jan  8  2014 iptables-apply
529325 lrwxrwxrwx  1 root root        13 Mar  5  2015 iptables-restore -> xtables-multi
529326 lrwxrwxrwx  1 root root        13 Mar  5  2015 iptables-save -> xtables-multi
529327 -rwxr-xr-x  1 root root     22864 Aug  5  2014 iptunnel
529328 -rwxr-xr-x  1 root root     14616 Feb 12  2015 isosize
529329 -rwxr-xr-x  1 root root    107216 May 24  2012 iw
529330 -rwxr-xr-x  1 root root     27008 May  3  2012 iwconfig
529331 -rwxr-xr-x  1 root root     14720 May  3  2012 iwevent
529332 -rwxr-xr-x  1 root root     14528 May  3  2012 iwgetid
529333 -rwxr-xr-x  1 root root     35352 May  3  2012 iwlist
529334 -rwxr-xr-x  1 root root     14608 May  3  2012 iwpriv
529335 -rwxr-xr-x  1 root root     14568 May  3  2012 iwspy
529336 -rwxr-xr-x  1 root root     10552 Feb 18  2013 kbdrate
529337 lrwxrwxrwx  1 root root         6 Feb 16  2015 fsck.ext3 -> e2fsck
529338 -rwxr-xr-x  1 root root     18992 Mar 12  2014 killall5
****Out of Sequence inode detected**** expect 529339 got 529342
529342 -rwxr-xr-x  1 root root     43584 Feb 12  2015 losetup
529343 lrwxrwxrwx  1 root root         9 Mar  5  2015 lsmod -> /bin/kmod
529344 lrwxrwxrwx  1 root root         9 Mar  5  2015 lspcmcia -> pccardctl
****Out of Sequence inode detected**** expect 529345 got 529363
529363 -rwxr-xr-x  1 root root     19264 Aug  5  2014 mii-tool
529364 lrwxrwxrwx  1 root root         8 Mar  5  2015 mkdosfs -> mkfs.fat
****Out of Sequence inode detected**** expect 529365 got 529366
529366 -rwxr-xr-x  1 root root     10440 Feb 12  2015 mkfs
529367 -rwxr-xr-x  1 root root     18736 Feb 12  2015 mkfs.bfs
529368 -rwxr-xr-x  1 root root     31216 Feb 12  2015 mkfs.cramfs
****Out of Sequence inode detected**** expect 529369 got 529373
529373 -rwxr-xr-x  1 root root     27608 Mar 18  2014 mkfs.fat
529374 -rwxr-xr-x  1 root root     27144 Feb 12  2015 mkfs.minix
529375 lrwxrwxrwx  1 root root         8 Mar  5  2015 mkfs.msdos -> mkfs.fat
529376 lrwxrwxrwx  1 root root         6 Mar  5  2015 mkfs.ntfs -> mkntfs
529377 lrwxrwxrwx  1 root root         8 Mar  5  2015 mkfs.vfat -> mkfs.fat
529378 -rwxr-xr-x  1 root root     18784 Jan 31  2014 mkhomedir_helper
529379 -rwxr-xr-x  1 root root     79984 Dec 18  2013 mkntfs
529380 -rwxr-xr-x  1 root root     23112 Feb 12  2015 mkswap
529381 -rwxr-xr-x  1 root root     31112 Feb 21  2014 mntctl
529382 lrwxrwxrwx  1 root root         9 Mar  5  2015 modinfo -> /bin/kmod
529383 lrwxrwxrwx  1 root root         9 Mar  5  2015 modprobe -> /bin/kmod
****Out of Sequence inode detected**** expect 529384 got 529386
529386 -rwxr-xr-x  1 root root     10240 Dec 16  2013 mount.fuse
529387 lrwxrwxrwx  1 root root        15 Mar  5  2015 mount.lowntfs-3g -> /bin/lowntfs-3g
529388 lrwxrwxrwx  1 root root        13 Mar  5  2015 mount.ntfs -> mount.ntfs-3g
529389 lrwxrwxrwx  1 root root        12 Mar  5  2015 mount.ntfs-3g -> /bin/ntfs-3g
529390 -rwxr-xr-x  1 root root    104968 Feb 21  2014 mountall
529391 -rwxr-xr-x  1 root root     14816 Aug  5  2014 nameif
529392 -rwxr-xr-x  1 root root     55408 Dec 18  2013 ntfsclone
529393 -rwxr-xr-x  1 root root     30824 Dec 18  2013 ntfscp
529394 -rwxr-xr-x  1 root root     26728 Dec 18  2013 ntfslabel
529395 -rwxr-xr-x  1 root root     71792 Dec 18  2013 ntfsresize
529396 -rwxr-xr-x  1 root root     47208 Dec 18  2013 ntfsundelete
529397 -rwxr-xr-x  1 root root      2251 Dec  2  2009 on_ac_power
529398 -rwxr-xr-x  1 root root     10544 Jan 31  2014 pam_tally
529399 -rwxr-xr-x  1 root root     14728 Jan 31  2014 pam_tally2
529400 -rwxr-xr-x  1 root root     81296 Apr 14  2014 parted
529401 -rwxr-xr-x  1 root root     10488 Apr 14  2014 partprobe
529402 -rwxr-xr-x  1 root root     18800 Jun 28  2012 pccardctl
529403 -rwxr-xr-x  1 root root      6240 Feb 12  2015 pivot_root
529404 -rwxr-xr-x  1 root root     10448 Aug  5  2014 plipconfig
529405 -rwxr-xr-x  1 root root     81632 Dec  2  2014 plymouthd
529406 lrwxrwxrwx  1 root root         6 Mar  5  2015 poweroff -> reboot
****Out of Sequence inode detected**** expect 529407 got 529416
529416 -rwxr-xr-x  1 root root     29800 Aug  5  2014 rarp
529417 -rwxr-xr-x  1 root root     10424 Feb 12  2015 raw
529418 -rwxr-xr-x  1 root root     14784 Jul 18  2014 reboot
529419 -rwxr-xr-x  1 root root     10488 Oct  1  2012 regdbdump
529420 lrwxrwxrwx  1 root root         7 Mar  5  2015 reload -> initctl
****Out of Sequence inode detected**** expect 529421 got 529423
529423 -rwxr-xr-x  1 root root      5630 Jun 13  2014 resolvconf
529424 lrwxrwxrwx  1 root root         7 Mar  5  2015 restart -> initctl
529425 lrwxrwxrwx  1 root root         9 Mar  5  2015 rmmod -> /bin/kmod
529426 -rwxr-xr-x  1 root root     58032 Aug  5  2014 route
529427 -rwxr-xr-x  1 root root     35344 Feb 17  2014 rtacct
529428 -rwxr-xr-x  1 root root     35256 Feb 17  2014 rtmon
529429 -rwxr-xr-x  1 root root     10240 Jul 18  2014 runlevel
****Out of Sequence inode detected**** expect 529430 got 529431
529431 -rwxr-xr-x  1 root root     10488 Feb 21  2014 setcap
529432 -rwxr-xr-x  1 root root     10600 Feb 18  2013 setvtrgb
529433 -rwxr-xr-x  1 root root     61856 Feb 12  2015 sfdisk
529434 -rwxr-xr-x  1 root root    162712 Dec 26  2013 sgdisk
529435 -rwxr-xr-x  1 root root       885 Feb 16  2014 shadowconfig
529436 -rwxr-xr-x  1 root root     84904 Jul 18  2014 shutdown
529437 -rwxr-xr-x  1 root root     33928 Aug  5  2014 slattach
529438 lrwxrwxrwx  1 root root         7 Mar  5  2015 start -> initctl
529439 -rwxr-xr-x  1 root root     28200 Mar  7  2014 start-stop-daemon
529440 -rwxr-xr-x  1 root root     35768 Mar 12  2014 startpar
529441 -rwxr-xr-x  1 root root      6328 Mar 12  2014 startpar-upstart-inject
529442 lrwxrwxrwx  1 root root         7 Mar  5  2015 status -> initctl
529443 lrwxrwxrwx  1 root root         7 Mar  5  2015 stop -> initctl
529444 -rwxr-xr-x  1 root root     14904 Mar 12  2014 sulogin
529445 -rwxr-xr-x  1 root root     14664 Feb 12  2015 swaplabel
529446 lrwxrwxrwx  1 root root         6 Mar  5  2015 swapoff -> swapon
529447 -rwxr-xr-x  1 root root     27240 Feb 12  2015 swapon
529448 -rwxr-xr-x  1 root root     10544 Feb 12  2015 switch_root
529449 -rwxr-xr-x  1 root root     22992 Feb 10  2015 sysctl
529450 -rwxr-xr-x  1 root root    282024 Feb 17  2014 tc
529451 -rwxr-xr-x  1 root root    104728 Jul 18  2014 telinit
****Out of Sequence inode detected**** expect 529452 got 529453
529453 lrwxrwxrwx  1 root root        12 Mar  5  2015 udevadm -> /bin/udevadm
529454 lrwxrwxrwx  1 root root        26 Mar  5  2015 udevd -> /lib/systemd/systemd-udevd
****Out of Sequence inode detected**** expect 529455 got 529457
529457 -rwxr-xr-x  1 root root     10504 Mar 10  2014 umount.udisks2
529458 -rwxr-sr-x  1 root shadow   35536 Jan 31  2014 unix_chkpwd
529459 -rwxr-xr-x  1 root root     31376 Jan 31  2014 unix_update
529460 -rwxr-xr-x  1 root root    133640 Jul 18  2014 upstart-dbus-bridge
529461 -rwxr-xr-x  1 root root    125144 Jul 18  2014 upstart-event-bridge
529462 -rwxr-xr-x  1 root root    141592 Jul 18  2014 upstart-file-bridge
529463 -rwxr-xr-x  1 root root    133512 Jul 18  2014 upstart-local-bridge
529464 -rwxr-xr-x  1 root root    133352 Jul 18  2014 upstart-socket-bridge
529465 -rwxr-xr-x  1 root root     76040 Jul 18  2014 upstart-udev-bridge
529466 -rwxr-xr-x  1 root root     47408 Mar 25  2013 ureadahead
****Out of Sequence inode detected**** expect 529467 got 529487
529487 -rwxr-xr-x  1 root root     18856 Feb 12  2015 wipefs
529488 -rwxr-xr-x  1 root root      1735 Jan 28  2014 wpa_action
529489 -rwxr-xr-x  1 root root     94032 Oct 10  2014 wpa_cli
529490 -rwxr-xr-x  1 root root   1769752 Oct 10  2014 wpa_supplicant
529491 -rwxr-xr-x  1 root root     87768 Jan  8  2014 xtables-multi
u64@u64-VirtualBox:~/Desktop$
```
#### 59. Inodes: using Python to read directories from Inode numbers

###### ```extfs.py```

```python
```

###### ```ils.py```

```python
```

###### Using ```ils.py```

```sh
u64@u64-VirtualBox:~/Desktop/code$ ./ils.py
usage ./ils.py <image file> <offset> <inode number>
Displays directory for an inode from an image file
u64@u64-VirtualBox:~/Desktop/code$
```

- Identify the ```offset```

```sh
u64@u64-VirtualBox:~$ sudo fdisk Desktop/2015-3-9.img
[sudo] password for u64:

Welcome to fdisk (util-linux 2.27.1).
Changes will remain in memory only, until you decide to write them.
Be careful before using the write command.


Command (m for help): p
Disk Desktop/2015-3-9.img: 18 GiB, 19327352832 bytes, 37748736 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: dos
Disk identifier: 0x0004565b

Device                Boot    Start      End  Sectors Size Id Type
Desktop/2015-3-9.img1 *        2048 33554431 33552384  16G 83 Linux
Desktop/2015-3-9.img2      33556478 37746687  4190210   2G  5 Extended
Desktop/2015-3-9.img5      33556480 37746687  4190208   2G 82 Linux swap / Solaris

Command (m for help): q

u64@u64-VirtualBox:~$
```

- Identify ```inode``` of root directory

```sh
u64@u64-VirtualBox:~$ ls -id /media/part0/
2 /media/part0/
u64@u64-VirtualBox:~$
```

- ```ils.py``` for ```/```

```sh
u64@u64-VirtualBox:~/Desktop/code$ ./ils.py ../2015-3-9.img 2048 2
Inode: 2 File type: Directory Filename: .
Inode: 2 File type: Directory Filename: ..
Inode: 11 File type: Directory Filename: lost+found
Inode: 786433 File type: Directory Filename: etc
Inode: 524289 File type: Directory Filename: media
Inode: 655361 File type: Directory Filename: bin
Inode: 917505 File type: Directory Filename: boot
Inode: 131073 File type: Directory Filename: dev
Inode: 262145 File type: Directory Filename: home
Inode: 524290 File type: Directory Filename: lib
Inode: 655362 File type: Directory Filename: lib64
Inode: 786435 File type: Directory Filename: mnt
Inode: 131074 File type: Directory Filename: opt
Inode: 262146 File type: Directory Filename: proc
Inode: 917506 File type: Directory Filename: root
Inode: 917507 File type: Directory Filename: run
Inode: 524291 File type: Directory Filename: sbin
Inode: 131075 File type: Directory Filename: srv
Inode: 262147 File type: Directory Filename: sys
Inode: 655363 File type: Directory Filename: tmp
Inode: 8193 File type: Directory Filename: usr
Inode: 8194 File type: Directory Filename: var
Inode: 12 File type: Symbolic link Filename: vmlinuz
Inode: 13 File type: Symbolic link Filename: initrd.img
Inode: 922654 File type: Directory Filename: cdrom
u64@u64-VirtualBox:~/Desktop/code$
```

- ```ils.py``` for ```etc```

```sh
u64@u64-VirtualBox:~/Desktop/code$ ./ils.py ../2015-3-9.img 2048 786433
Inode: 786433 File type: Directory Filename: .
Inode: 2 File type: Directory Filename: ..
Inode: 786434 File type: Regular Filename: fstab
Inode: 786438 File type: Directory Filename: X11
Inode: 786439 File type: Directory Filename: acpi
Inode: 786440 File type: Directory Filename: alternatives
Inode: 786442 File type: Directory Filename: apparmor
Inode: 786444 File type: Directory Filename: apport
Inode: 786448 File type: Directory Filename: avahi
Inode: 786449 File type: Directory Filename: bash_completion.d
Inode: 786450 File type: Directory Filename: bluetooth
Inode: 786451 File type: Directory Filename: brltty
Inode: 786452 File type: Directory Filename: ca-certificates
Inode: 786453 File type: Directory Filename: calendar
Inode: 786455 File type: Directory Filename: compizconfig
Inode: 786456 File type: Directory Filename: console-setup
Inode: 786457 File type: Directory Filename: cracklib
Inode: 786458 File type: Directory Filename: cron.d
Inode: 786459 File type: Directory Filename: cron.daily
Inode: 786462 File type: Directory Filename: cron.weekly
Inode: 786464 File type: Directory Filename: cupshelpers
Inode: 786468 File type: Directory Filename: depmod.d
Inode: 786469 File type: Directory Filename: dhcp
Inode: 786474 File type: Directory Filename: emacs
Inode: 786475 File type: Directory Filename: firefox
Inode: 786478 File type: Directory Filename: gconf
Inode: 786480 File type: Directory Filename: ghostscript
Inode: 786481 File type: Directory Filename: gnome
Inode: 786483 File type: Directory Filename: groff
Inode: 786484 File type: Directory Filename: grub.d
Inode: 786487 File type: Directory Filename: hp
Inode: 786496 File type: Directory Filename: kernel
Inode: 786498 File type: Directory Filename: ldap
Inode: 786501 File type: Directory Filename: libreoffice
Inode: 786502 File type: Directory Filename: lightdm
Inode: 786503 File type: Directory Filename: logcheck
Inode: 786509 File type: Directory Filename: newt
Inode: 786514 File type: Directory Filename: perl
Inode: 786515 File type: Directory Filename: pki
Inode: 786516 File type: Directory Filename: pm
Inode: 786517 File type: Directory Filename: polkit-1
Inode: 786519 File type: Directory Filename: profile.d
Inode: 786523 File type: Directory Filename: python3
Inode: 786524 File type: Directory Filename: python3.4
Inode: 786525 File type: Directory Filename: rc0.d
Inode: 786526 File type: Directory Filename: rc1.d
Inode: 786531 File type: Directory Filename: rc6.d
Inode: 787871 File type: Directory Filename: wildmidi
Inode: 786536 File type: Directory Filename: samba
Inode: 786538 File type: Directory Filename: security
Inode: 786541 File type: Directory Filename: sgml
Inode: 786544 File type: Directory Filename: speech-dispatcher
Inode: 786546 File type: Directory Filename: ssl
Inode: 786547 File type: Directory Filename: sudoers.d
Inode: 786550 File type: Directory Filename: terminfo
Inode: 786551 File type: Directory Filename: thunderbird
Inode: 786553 File type: Directory Filename: udisks2
Inode: 786556 File type: Directory Filename: update-motd.d
Inode: 786557 File type: Directory Filename: update-notifier
Inode: 786558 File type: Directory Filename: usb_modeswitch.d
Inode: 786559 File type: Directory Filename: vim
Inode: 786560 File type: Directory Filename: wpa_supplicant
Inode: 786561 File type: Directory Filename: xdg
Inode: 786562 File type: Directory Filename: xml
Inode: 786563 File type: Directory Filename: xul-ext
Inode: 786565 File type: Regular Filename: adduser.conf
Inode: 786566 File type: Regular Filename: anacrontab
Inode: 786568 File type: Regular Filename: bash.bashrc
Inode: 786569 File type: Regular Filename: bash_completion
Inode: 786572 File type: Symbolic link Filename: blkid.tab
Inode: 786574 File type: Regular Filename: brltty.conf
Inode: 786576 File type: Regular Filename: colord.conf
Inode: 786577 File type: Regular Filename: crontab
Inode: 786578 File type: Regular Filename: debconf.conf
Inode: 786579 File type: Regular Filename: debian_version
Inode: 786580 File type: Regular Filename: deluser.conf
Inode: 786583 File type: Regular Filename: fuse.conf
Inode: 786584 File type: Regular Filename: gai.conf
Inode: 786646 File type: Regular Filename: gshadow
Inode: 786587 File type: Regular Filename: hdparm.conf
Inode: 786589 File type: Regular Filename: hostname
Inode: 786591 File type: Regular Filename: hosts.allow
Inode: 786593 File type: Regular Filename: inputrc
Inode: 786594 File type: Regular Filename: insserv.conf
Inode: 786595 File type: Regular Filename: issue
Inode: 786596 File type: Regular Filename: issue.net
Inode: 788846 File type: Regular Filename: kernel-img.conf
Inode: 818475 File type: Regular Filename: ld.so.cache
Inode: 786600 File type: Regular Filename: ld.so.conf
Inode: 786607 File type: Regular Filename: logrotate.conf
Inode: 786608 File type: Regular Filename: lsb-release
Inode: 786609 File type: Regular Filename: ltrace.conf
Inode: 786615 File type: Regular Filename: mime.types
Inode: 786618 File type: Regular Filename: mtools.conf
Inode: 786620 File type: Regular Filename: netscsid.conf
Inode: 818492 File type: Regular Filename: ftpallow
Inode: 786623 File type: Regular Filename: nsswitch.conf
Inode: 786624 File type: Regular Filename: os-release
Inode: 786630 File type: Regular Filename: profile
Inode: 786631 File type: Regular Filename: protocols
Inode: 786635 File type: Regular Filename: rmt
Inode: 786638 File type: Regular Filename: securetty
Inode: 786639 File type: Regular Filename: sensors3.conf
Inode: 786640 File type: Regular Filename: services
Inode: 786641 File type: Regular Filename: shadow
Inode: 786644 File type: Regular Filename: subuid
Inode: 786648 File type: Regular Filename: sudoers
Inode: 786652 File type: Regular Filename: updatedb.conf
Inode: 786654 File type: Regular Filename: usb_modeswitch.conf
Inode: 786655 File type: Symbolic link Filename: vtrgb
Inode: 786657 File type: Regular Filename: wodim.conf
Inode: 786658 File type: Regular Filename: zsh_command_not_found
Inode: 818486 File type: Regular Filename: mtab
Inode: 818265 File type: Regular Filename: passwd-
Inode: 786629 File type: Symbolic link Filename: printcap
Inode: 786627 File type: Regular Filename: shadow-
Inode: 786575 File type: Regular Filename: ca-certificates.conf.dpkg-old
Inode: 818533 File type: Directory Filename: chromium-browser
Inode: 786537 File type: Directory Filename: sane.d
Inode: 786552 File type: Directory Filename: udev
Inode: 786601 File type: Regular Filename: legal
Inode: 786573 File type: Regular Filename: brlapi.key
Inode: 786522 File type: Directory Filename: python2.7
Inode: 786581 File type: Regular Filename: drirc
Inode: 786470 File type: Directory Filename: dictionaries-common
Inode: 786485 File type: Directory Filename: gtk-2.0
Inode: 786477 File type: Directory Filename: fstab.d
Inode: 786651 File type: Regular Filename: ucf.conf
Inode: 786460 File type: Directory Filename: cron.hourly
Inode: 786571 File type: Regular Filename: blkid.conf
Inode: 786567 File type: Regular Filename: apg.conf
Inode: 786656 File type: Regular Filename: wgetrc
Inode: 786617 File type: Regular Filename: modules
Inode: 786647 File type: Regular Filename: subuid-
Inode: 786650 File type: Regular Filename: timezone
Inode: 786545 File type: Directory Filename: ssh
Inode: 786602 File type: Regular Filename: libaudit.conf
Inode: 786543 File type: Directory Filename: skel
Inode: 786632 File type: Regular Filename: rc.local
Inode: 786488 File type: Directory Filename: ifplugd
Inode: 786649 File type: Regular Filename: sysctl.conf
Inode: 786473 File type: Directory Filename: dpkg
Inode: 786605 File type: Regular Filename: localtime
Inode: 786504 File type: Directory Filename: logrotate.d
Inode: 786510 File type: Directory Filename: obex-data-server
Inode: 786653 File type: Regular Filename: upstart-xsessions
Inode: 786472 File type: Directory Filename: doc-base
Inode: 786518 File type: Directory Filename: ppp
Inode: 818539 File type: Regular Filename: mailcap
Inode: 786493 File type: Directory Filename: insserv.conf.d
Inode: 786437 File type: Directory Filename: UPower
Inode: 786530 File type: Directory Filename: rc5.d
Inode: 786614 File type: Regular Filename: manpath.config
Inode: 786508 File type: Directory Filename: network
Inode: 786549 File type: Directory Filename: systemd
Inode: 786625 File type: Regular Filename: pam.conf
Inode: 786499 File type: Directory Filename: libnl-3
Inode: 786598 File type: Regular Filename: kerneloops.conf
Inode: 786619 File type: Regular Filename: nanorc
Inode: 786555 File type: Directory Filename: update-manager
Inode: 786512 File type: Directory Filename: pam.d
Inode: 786592 File type: Regular Filename: hosts.deny
Inode: 786606 File type: Regular Filename: login.defs
Inode: 786645 File type: Regular Filename: subgid-
Inode: 786542 File type: Directory Filename: signon-ui
Inode: 786643 File type: Regular Filename: signond.conf
Inode: 786610 File type: Regular Filename: magic
Inode: 786626 File type: Regular Filename: popularity-contest.conf
Inode: 786642 File type: Regular Filename: shells
Inode: 786447 File type: Directory Filename: at-spi2
Inode: 786482 File type: Directory Filename: gnome-app-install
Inode: 786588 File type: Regular Filename: host.conf
Inode: 786500 File type: Directory Filename: libpaper.d
Inode: 818540 File type: Regular Filename: group
Inode: 818262 File type: Regular Filename: mtab.fuselock
Inode: 786621 File type: Regular Filename: networks
Inode: 786486 File type: Directory Filename: gtk-3.0
Inode: 786465 File type: Directory Filename: dbus-1
Inode: 786554 File type: Directory Filename: ufw
Inode: 786511 File type: Directory Filename: opt
Inode: 786471 File type: Directory Filename: dnsmasq.d
Inode: 786497 File type: Directory Filename: ld.so.conf.d
Inode: 786476 File type: Directory Filename: fonts
Inode: 786492 File type: Directory Filename: insserv
Inode: 786582 File type: Regular Filename: environment
Inode: 786436 File type: Directory Filename: NetworkManager
Inode: 786611 File type: Regular Filename: magic.mime
Inode: 786520 File type: Directory Filename: pulse
Inode: 786479 File type: Directory Filename: gdb
Inode: 786495 File type: Directory Filename: kbd
Inode: 786548 File type: Directory Filename: sysctl.d
Inode: 786446 File type: Directory Filename: aptdaemon
Inode: 786636 File type: Regular Filename: rpc
Inode: 786628 File type: Regular Filename: pnm2ppa.conf
Inode: 786441 File type: Directory Filename: apm
Inode: 812937 File type: Regular Filename: ca-certificates.conf
Inode: 786535 File type: Directory Filename: rsyslog.d
Inode: 786467 File type: Directory Filename: default
Inode: 786590 File type: Regular Filename: hosts
Inode: 786506 File type: Directory Filename: modprobe.d
Inode: 786570 File type: Regular Filename: bindresvport.blacklist
Inode: 786529 File type: Directory Filename: rc4.d
Inode: 786513 File type: Directory Filename: pcmcia
Inode: 786454 File type: Directory Filename: chatscripts
Inode: 786527 File type: Directory Filename: rc2.d
Inode: 786613 File type: Regular Filename: mailcap.order
Inode: 786539 File type: Directory Filename: selinux
Inode: 786521 File type: Directory Filename: python
Inode: 786489 File type: Directory Filename: init
Inode: 786445 File type: Directory Filename: apt
Inode: 818452 File type: Regular Filename: subgid
Inode: 786604 File type: Regular Filename: locale.alias
Inode: 786490 File type: Directory Filename: init.d
Inode: 786528 File type: Directory Filename: rc3.d
Inode: 788850 File type: Regular Filename: papersize
Inode: 786491 File type: Directory Filename: initramfs-tools
Inode: 786534 File type: Directory Filename: resolvconf
Inode: 786603 File type: Regular Filename: lintianrc
Inode: 786461 File type: Directory Filename: cron.monthly
Inode: 786443 File type: Directory Filename: apparmor.d
Inode: 786463 File type: Directory Filename: cups
Inode: 786637 File type: Regular Filename: rsyslog.conf
Inode: 786540 File type: Directory Filename: sensors.d
Inode: 818270 File type: Regular Filename: passwd
Inode: 786494 File type: Directory Filename: iproute2
Inode: 786634 File type: Symbolic link Filename: resolv.conf
Inode: 786507 File type: Directory Filename: modules-load.d
Inode: 786466 File type: Directory Filename: dconf
Inode: 786564 File type: Regular Filename: .pwd.lock
Inode: 786532 File type: Directory Filename: rcS.d
Inode: 786616 File type: Regular Filename: mke2fs.conf
Inode: 818258 File type: Regular Filename: iftab
Inode: 818266 File type: Regular Filename: gshadow-
Inode: 786586 File type: Regular Filename: group-
Inode: 787546 File type: Directory Filename: openal
Inode: 786633 File type: Regular Filename: ts.conf
Inode: 818330 File type: Directory Filename: timidity
Inode: 812962 File type: Regular Filename: inetd.conf
Inode: 818509 File type: Regular Filename: ftpusers
Inode: 818494 File type: Directory Filename: pure-ftpd
u64@u64-VirtualBox:~/Desktop/code$
```

- ```ils.py``` for ```tmp```

```sh
u64@u64-VirtualBox:~/Desktop/code$ ./ils.py ../2015-3-9.img 2048 655363
Inode: 655363 File type: Directory Filename: .
Inode: 2 File type: Directory Filename: ..
Inode: 655484 File type: Directory Filename: .X11-unix
Inode: 655485 File type: Directory Filename: .ICE-unix
Inode: 655486 File type: Regular Filename: .X0-lock
Inode: 655488 File type: Regular Filename: config-err-dqpfMl
Inode: 655494 File type: Regular Filename: unity_support_test.1
Inode: 657110 File type: Regular Filename: xingyi_bindshell_pid
Inode: 657112 File type: Regular Filename: xingyi_bindshell_port
u64@u64-VirtualBox:~/Desktop/code$
```
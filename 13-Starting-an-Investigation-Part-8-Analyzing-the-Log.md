#### 13. Starting an Investigation Part 8: Analyzing the Log

###### Suspicious Items in the log file.

- ```netstat -anp```
- ```lsof -V```
- ```ps -ef```
	- Processes running as ```root``` with high ```PID```
- ```mount```
- ```last```
	- Logged in users - ```john```, ```reboot```, ```johnn```, ```lightdm```
- ```/etc/passwd```

	```
	johnn:x:1001:1001:,John Smith,,:/home/.johnn:/bin/bash
	lightdm:x:112:118:Light Display Manager:/var/lib/lightdm:/bin/false
	```

###### ```log.txt``` file

```
++++Sending log for date at Mon Mar  9 21:53:00 EDT 2015 ++++
 Mon Mar  9 21:53:00 EDT 2015 
----end----

++++Sending log for uname -a at Mon Mar  9 21:53:00 EDT 2015 ++++
 Linux PentesterAcademyLinux 3.16.0-30-generic #40~14.04.1-Ubuntu SMP Thu Jan 15 17:43:14 UTC 2015 x86_64 x86_64 x86_64 GNU/Linux 
----end----

++++Sending log for ifconfig -a at Mon Mar  9 21:53:00 EDT 2015 ++++
 eth0      Link encap:Ethernet  HWaddr 08:00:27:f0:84:95  
          inet addr:10.0.2.15  Bcast:10.0.2.255  Mask:255.255.255.0
          inet6 addr: fe80::a00:27ff:fef0:8495/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:495 errors:0 dropped:0 overruns:0 frame:0
          TX packets:347 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:344054 (344.0 KB)  TX bytes:34608 (34.6 KB)

eth1      Link encap:Ethernet  HWaddr 08:00:27:53:73:15  
          inet addr:192.168.56.101  Bcast:192.168.56.255  Mask:255.255.255.0
          inet6 addr: fe80::a00:27ff:fe53:7315/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:1026 errors:0 dropped:0 overruns:0 frame:0
          TX packets:1074 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:77293 (77.2 KB)  TX bytes:71150 (71.1 KB)

lo        Link encap:Local Loopback  
          inet addr:127.0.0.1  Mask:255.0.0.0
          inet6 addr: ::1/128 Scope:Host
          UP LOOPBACK RUNNING  MTU:65536  Metric:1
          RX packets:217 errors:0 dropped:0 overruns:0 frame:0
          TX packets:217 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0 
          RX bytes:18107 (18.1 KB)  TX bytes:18107 (18.1 KB) 
----end----

++++Sending log for netstat -anp at Mon Mar  9 21:53:00 EDT 2015 ++++
  
----end----

++++Sending log for lsof -V at Mon Mar  9 21:53:00 EDT 2015 ++++
  
----end----

++++Sending log for ps -ef at Mon Mar  9 21:53:00 EDT 2015 ++++
 UID        PID  PPID  C STIME TTY          TIME CMD
root         1     0  0 21:47 ?        00:00:01 /sbin/init
root         2     0  0 21:47 ?        00:00:00 [kthreadd]
root         3     2  0 21:47 ?        00:00:00 [ksoftirqd/0]
root         5     2  0 21:47 ?        00:00:00 [kworker/0:0H]
root         6     2  0 21:47 ?        00:00:00 [kworker/u2:0]
root         7     2  0 21:47 ?        00:00:00 [rcu_sched]
root         8     2  0 21:47 ?        00:00:00 [rcuos/0]
root         9     2  0 21:47 ?        00:00:00 [rcu_bh]
root        10     2  0 21:47 ?        00:00:00 [rcuob/0]
root        11     2  0 21:47 ?        00:00:00 [migration/0]
root        12     2  0 21:47 ?        00:00:00 [watchdog/0]
root        13     2  0 21:47 ?        00:00:00 [khelper]
root        14     2  0 21:47 ?        00:00:00 [kdevtmpfs]
root        15     2  0 21:47 ?        00:00:00 [netns]
root        16     2  0 21:47 ?        00:00:00 [khungtaskd]
root        17     2  0 21:47 ?        00:00:00 [writeback]
root        18     2  0 21:47 ?        00:00:00 [ksmd]
root        19     2  0 21:47 ?        00:00:00 [khugepaged]
root        20     2  0 21:47 ?        00:00:00 [crypto]
root        21     2  0 21:47 ?        00:00:00 [kintegrityd]
root        22     2  0 21:47 ?        00:00:00 [bioset]
root        23     2  0 21:47 ?        00:00:00 [kblockd]
root        24     2  0 21:47 ?        00:00:00 [ata_sff]
root        25     2  0 21:47 ?        00:00:00 [khubd]
root        26     2  0 21:47 ?        00:00:00 [md]
root        27     2  0 21:47 ?        00:00:00 [devfreq_wq]
root        28     2  0 21:47 ?        00:00:00 [kworker/u2:1]
root        29     2  0 21:47 ?        00:00:00 [kworker/0:1]
root        30     2  0 21:47 ?        00:00:00 [kswapd0]
root        31     2  0 21:47 ?        00:00:00 [fsnotify_mark]
root        32     2  0 21:47 ?        00:00:00 [ecryptfs-kthrea]
root        44     2  0 21:47 ?        00:00:00 [kthrotld]
root        45     2  0 21:47 ?        00:00:00 [acpi_thermal_pm]
root        46     2  0 21:47 ?        00:00:00 [scsi_eh_0]
root        47     2  0 21:47 ?        00:00:00 [scsi_tmf_0]
root        48     2  0 21:47 ?        00:00:00 [scsi_eh_1]
root        49     2  0 21:47 ?        00:00:00 [scsi_tmf_1]
root        51     2  0 21:47 ?        00:00:00 [ipv6_addrconf]
root        52     2  0 21:47 ?        00:00:00 [kworker/u2:3]
root        71     2  0 21:47 ?        00:00:00 [deferwq]
root        72     2  0 21:47 ?        00:00:00 [charger_manager]
root       118     2  0 21:47 ?        00:00:00 [kpsmoused]
root       119     2  0 21:47 ?        00:00:00 [kworker/0:2]
root       120     2  0 21:47 ?        00:00:00 [scsi_eh_2]
root       121     2  0 21:47 ?        00:00:00 [scsi_tmf_2]
root       130     2  0 21:47 ?        00:00:00 [kworker/0:1H]
root       131     2  0 21:47 ?        00:00:00 [jbd2/sda1-8]
root       132     2  0 21:47 ?        00:00:00 [ext4-rsv-conver]
root       255     1  0 21:47 ?        00:00:00 upstart-udev-bridge --daemon
root       262     1  0 21:47 ?        00:00:00 /lib/systemd/systemd-udevd --daemon
root       341     2  0 21:47 ?        00:00:00 [iprt]
message+   424     1  0 21:48 ?        00:00:00 dbus-daemon --system --fork
syslog     446     1  0 21:48 ?        00:00:00 rsyslogd
root       475     1  0 21:48 ?        00:00:00 /usr/sbin/bluetoothd
root       483     1  0 21:48 ?        00:00:00 /lib/systemd/systemd-logind
root       525     2  0 21:48 ?        00:00:00 [krfcommd]
avahi      548     1  0 21:48 ?        00:00:00 avahi-daemon: running [PentesterAcademyLinux.local]
avahi      549   548  0 21:48 ?        00:00:00 avahi-daemon: chroot helper
root       596     1  0 21:48 ?        00:00:00 /usr/sbin/ModemManager
root       622     1  0 21:48 ?        00:00:00 upstart-file-bridge --daemon
root       625     1  0 21:48 ?        00:00:00 upstart-socket-bridge --daemon
root       731     1  0 21:48 ?        00:00:00 NetworkManager
root       735     1  0 21:48 tty4     00:00:00 /sbin/getty -8 38400 tty4
root       739     1  0 21:48 tty5     00:00:00 /sbin/getty -8 38400 tty5
root       747     1  0 21:48 ?        00:00:00 /usr/lib/policykit-1/polkitd --no-debug
root       751     1  0 21:48 tty2     00:00:00 /sbin/getty -8 38400 tty2
root       752     1  0 21:48 tty3     00:00:00 /sbin/getty -8 38400 tty3
root       755     1  0 21:48 tty6     00:00:00 /sbin/getty -8 38400 tty6
root       814     1  0 21:48 ?        00:00:00 /usr/sbin/sshd -D
kernoops   821     1  0 21:48 ?        00:00:00 /usr/sbin/kerneloops
root       824     1  0 21:48 ?        00:00:00 anacron -s
root       826     1  0 21:48 ?        00:00:00 acpid -c /etc/acpi/events -s /var/run/acpid.socket
root       843     1  0 21:48 ?        00:00:00 cron
root       887   731  0 21:48 ?        00:00:00 /sbin/dhclient -d -sf /usr/lib/NetworkManager/nm-dhcp-client.action -pf /run/sendsigs.omit.d/network-manager.dhclient-eth1.pid -lf /var/lib/NetworkManager/dhclient-96961b0a-f0a4-4bb6-b393-ca97a13865fe-eth1.lease -cf /var/lib/NetworkManager/dhclient-eth1.conf eth1
root       921   731  0 21:48 ?        00:00:00 /sbin/dhclient -d -sf /usr/lib/NetworkManager/nm-dhcp-client.action -pf /run/sendsigs.omit.d/network-manager.dhclient-eth0.pid -lf /var/lib/NetworkManager/dhclient-7a3d31ac-d361-4b31-9289-12fa35fa2424-eth0.lease -cf /var/lib/NetworkManager/dhclient-eth0.conf eth0
root       924     1  0 21:48 ?        00:00:00 /bin/sh -e /proc/self/fd/9
root       927   924  0 21:48 ?        00:00:00 initctl emit plymouth-ready
root       937     1  0 21:48 ?        00:00:00 /usr/sbin/cups-browsed
whoopsie   954     1  0 21:48 ?        00:00:00 whoopsie
root       959     1  0 21:48 ?        00:00:00 pure-ftpd (SERVER)                                                                                                          
root      1067     1  0 21:48 ?        00:00:00 /usr/sbin/VBoxService
root      1120     1  0 21:48 tty1     00:00:00 /sbin/getty -8 38400 tty1
nobody    1125   731  0 21:48 ?        00:00:00 /usr/sbin/dnsmasq --no-resolv --keep-in-foreground --no-hosts --bind-interfaces --pid-file=/run/sendsigs.omit.d/network-manager.dnsmasq.pid --listen-address=127.0.1.1 --conf-file=/var/run/NetworkManager/dnsmasq.conf --cache-size=0 --proxy-dnssec --enable-dbus=org.freedesktop.NetworkManager.dnsmasq --conf-dir=/etc/NetworkManager/dnsmasq.d
root      1179     1  0 21:48 ?        00:00:00 lightdm
root      1270  1179  2 21:48 tty7     00:00:07 /usr/bin/X -core :0 -seat seat0 -auth /var/run/lightdm/root/:0 -nolisten tcp vt7 -novtswitch
root      1273     1  0 21:48 ?        00:00:00 /usr/lib/accountsservice/accounts-daemon
root      1322     2  0 21:48 ?        00:00:00 [kauditd]
root      1378  1179  0 21:48 ?        00:00:00 lightdm --session-child 12 19
root      1403     1  0 21:48 ?        00:00:00 /usr/lib/upower/upowerd
rtkit     1475     1  0 21:48 ?        00:00:00 /usr/lib/rtkit/rtkit-daemon
colord    1554     1  0 21:48 ?        00:00:00 /usr/lib/colord/colord
root      1720     1  0 21:48 ?        00:00:00 /usr/sbin/cupsd -f
lp        1723  1720  0 21:48 ?        00:00:00 /usr/lib/cups/notifier/dbus dbus:// 
john      1745     1  0 21:48 ?        00:00:00 /usr/bin/gnome-keyring-daemon --daemonize --login
john      1750  1378  0 21:48 ?        00:00:00 init --user
john      1852     1  0 21:48 ?        00:00:00 /usr/bin/VBoxClient --clipboard
john      1859     1  0 21:48 ?        00:00:00 /usr/bin/VBoxClient --display
john      1864     1  0 21:48 ?        00:00:00 /usr/bin/VBoxClient --seamless
john      1869     1  0 21:48 ?        00:00:00 /usr/bin/VBoxClient --draganddrop
john      1889  1750  0 21:48 ?        00:00:00 dbus-daemon --fork --session --address=unix:abstract=/tmp/dbus-s5aMt9n0lX
john      1900  1750  0 21:48 ?        00:00:00 upstart-event-bridge
john      1915  1750  0 21:48 ?        00:00:00 /usr/lib/x86_64-linux-gnu/hud/window-stack-bridge
john      1934  1750  0 21:48 ?        00:00:00 upstart-dbus-bridge --daemon --session --user --bus-name session
john      1936  1750  0 21:48 ?        00:00:00 upstart-dbus-bridge --daemon --system --user --bus-name system
john      1943  1750  0 21:48 ?        00:00:00 upstart-file-bridge --daemon --user
john      1949  1750  0 21:48 ?        00:00:00 /usr/bin/ibus-daemon --daemonize --xim
john      1964  1750  0 21:48 ?        00:00:00 /usr/lib/unity-settings-daemon/unity-settings-daemon
john      1968  1750  0 21:48 ?        00:00:00 /usr/lib/x86_64-linux-gnu/hud/hud-service
john      1970  1750  0 21:48 ?        00:00:00 /usr/lib/at-spi2-core/at-spi-bus-launcher --launch-immediately
john      1971  1750  0 21:48 ?        00:00:00 gnome-session --session=ubuntu
john      1973  1750  0 21:48 ?        00:00:00 /usr/lib/unity/unity-panel-service
john      1977  1970  0 21:48 ?        00:00:00 /bin/dbus-daemon --config-file=/etc/at-spi2/accessibility.conf --nofork --print-address 3
john      1981  1750  0 21:48 ?        00:00:00 /usr/lib/at-spi2-core/at-spi2-registryd --use-gnome-session
john      1988  1750  0 21:48 ?        00:00:00 /usr/lib/gvfs/gvfsd
john      1996  1949  0 21:48 ?        00:00:00 /usr/lib/ibus/ibus-dconf
john      1999  1750  0 21:48 ?        00:00:00 /usr/lib/gvfs/gvfsd-fuse /run/user/1000/gvfs -f -o big_writes
john      2008  1949  0 21:48 ?        00:00:00 /usr/lib/ibus/ibus-ui-gtk3
john      2012  1750  0 21:48 ?        00:00:00 /usr/lib/x86_64-linux-gnu/bamf/bamfdaemon
john      2023  1750  0 21:48 ?        00:00:00 /usr/lib/ibus/ibus-x11 --kill-daemon
john      2039  1750  0 21:48 ?        00:00:00 /usr/lib/dconf/dconf-service
john      2041  1750  0 21:48 ?        00:00:00 /usr/lib/x86_64-linux-gnu/indicator-messages/indicator-messages-service
john      2044  1750  0 21:48 ?        00:00:00 /usr/lib/x86_64-linux-gnu/indicator-bluetooth/indicator-bluetooth-service
john      2045  1750  0 21:48 ?        00:00:00 /usr/lib/x86_64-linux-gnu/indicator-power/indicator-power-service
john      2050  1750  0 21:48 ?        00:00:00 /usr/lib/x86_64-linux-gnu/indicator-datetime/indicator-datetime-service
john      2052  1750  0 21:48 ?        00:00:00 /usr/lib/x86_64-linux-gnu/indicator-sound/indicator-sound-service
john      2055  1750  0 21:48 ?        00:00:00 /usr/lib/x86_64-linux-gnu/indicator-printers/indicator-printers-service
john      2056  1750  0 21:48 ?        00:00:00 /usr/lib/x86_64-linux-gnu/indicator-keyboard-service --use-gtk
john      2060  1750  0 21:48 ?        00:00:00 /usr/lib/x86_64-linux-gnu/indicator-session/indicator-session-service
john      2062  1750  0 21:48 ?        00:00:00 /usr/lib/x86_64-linux-gnu/indicator-application/indicator-application-service
john      2087  1750  0 21:48 ?        00:00:00 /usr/bin/pulseaudio --start --log-target=syslog
john      2098  1949  0 21:48 ?        00:00:00 /usr/lib/ibus/ibus-engine-simple
john      2108  1750  0 21:48 ?        00:00:00 /usr/lib/evolution/evolution-source-registry
john      2131  1750  0 21:48 ?        00:00:00 /usr/lib/x86_64-linux-gnu/notify-osd
root      2133     1  0 21:48 ?        00:00:00 /lib/systemd/systemd-localed
john      2175  1971 12 21:48 ?        00:00:31 compiz
john      2248  1750  0 21:48 ?        00:00:00 /usr/lib/evolution/evolution-calendar-factory
john      2249  1971  0 21:48 ?        00:00:00 /usr/lib/unity-settings-daemon/unity-fallback-mount-helper
john      2257  1971  0 21:48 ?        00:00:00 /usr/lib/policykit-1-gnome/polkit-gnome-authentication-agent-1
john      2265  1971  0 21:48 ?        00:00:00 nm-applet
john      2270  1971  0 21:48 ?        00:00:01 nautilus -n
john      2286  1750  0 21:48 ?        00:00:00 /usr/lib/gvfs/gvfs-udisks2-volume-monitor
root      2310     1  0 21:48 ?        00:00:00 /usr/lib/udisks2/udisksd --no-debug
john      2315  1750  0 21:48 ?        00:00:00 /usr/lib/x86_64-linux-gnu/gconf/gconfd-2
john      2324  1750  0 21:48 ?        00:00:00 /usr/lib/gvfs/gvfs-gphoto2-volume-monitor
john      2328  1750  0 21:48 ?        00:00:00 /usr/lib/gvfs/gvfs-afc-volume-monitor
john      2333  1750  0 21:48 ?        00:00:00 /usr/lib/gvfs/gvfs-mtp-volume-monitor
john      2347  1750  0 21:48 ?        00:00:00 /usr/lib/gvfs/gvfsd-trash --spawner :1.8 /org/gtk/gvfs/exec_spaw/0
john      2356  1750  0 21:48 ?        00:00:00 /usr/lib/gvfs/gvfsd-burn --spawner :1.8 /org/gtk/gvfs/exec_spaw/1
john      2390  1971  0 21:48 ?        00:00:00 telepathy-indicator
john      2397  1750  0 21:48 ?        00:00:00 /usr/lib/telepathy/mission-control-5
john      2417  1750  0 21:49 ?        00:00:00 /usr/lib/x86_64-linux-gnu/unity-scope-home/unity-scope-home
john      2430  1750  0 21:49 ?        00:00:00 /usr/bin/unity-scope-loader applications/applications.scope applications/scopes.scope commands.scope
john      2432  1750  0 21:49 ?        00:00:00 /usr/lib/x86_64-linux-gnu/unity-lens-files/unity-files-daemon
john      2439  1750  0 21:49 ?        00:00:00 /usr/bin/zeitgeist-daemon
john      2448  1750  0 21:49 ?        00:00:00 /usr/lib/x86_64-linux-gnu/zeitgeist-fts
john      2449  1750  0 21:49 ?        00:00:00 zeitgeist-datahub
john      2453  2448  0 21:49 ?        00:00:00 /bin/cat
john      2489  1750  0 21:49 ?        00:00:00 /usr/lib/x86_64-linux-gnu/unity-lens-music/unity-music-daemon
john      2516  1750  0 21:49 ?        00:00:01 gnome-terminal
john      2522  2516  0 21:49 ?        00:00:00 gnome-pty-helper
john      2523  2516  0 21:49 pts/12   00:00:00 bash
john      2546  1750  0 21:49 ?        00:00:00 /usr/lib/gvfs/gvfsd-http --spawner :1.8 /org/gtk/gvfs/exec_spaw/2
john      2909  1971  0 21:49 ?        00:00:00 update-notifier
root      3011     2  0 21:50 ?        00:00:00 [scsi_eh_3]
root      3012     2  0 21:50 ?        00:00:00 [scsi_tmf_3]
root      3013     2  0 21:50 ?        00:00:00 [usb-storage]
root      3038     2  0 21:50 ?        00:00:00 [jbd2/sdb2-8]
root      3039     2  0 21:50 ?        00:00:00 [ext4-rsv-conver]
root      3045     1  0 21:50 ?        00:00:00 /lib/systemd/systemd-hostnamed
john      3049  1971  0 21:50 ?        00:00:00 /usr/lib/x86_64-linux-gnu/deja-dup/deja-dup-monitor
root      3058  2523  0 21:50 pts/12   00:00:00 sudo -s
root      3059  3058  0 21:50 pts/12   00:00:00 bin/bash
root      3103  3059  0 21:53 pts/12   00:00:00 bash bin/initial-scan.sh
root      3130  3103  0 21:53 pts/12   00:00:00 bash bin/initial-scan.sh
root      3131  3130  0 21:53 pts/12   00:00:00 bash bin/initial-scan.sh
root      3132  3130  0 21:53 pts/12   00:00:00 nc 192.168.56.1 4444
root      3134  3131  0 21:53 pts/12   00:00:00 ps -ef 
----end----

++++Sending log for netstat -rn at Mon Mar  9 21:53:00 EDT 2015 ++++
 Kernel IP routing table
Destination     Gateway         Genmask         Flags   MSS Window  irtt Iface
0.0.0.0         10.0.2.2        0.0.0.0         UG        0 0          0 eth0
10.0.2.0        0.0.0.0         255.255.255.0   U         0 0          0 eth0
192.168.56.0    0.0.0.0         255.255.255.0   U         0 0          0 eth1 
----end----

++++Sending log for route at Mon Mar  9 21:53:00 EDT 2015 ++++
 Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
default         10.0.2.2        0.0.0.0         UG    0      0        0 eth0
10.0.2.0        *               255.255.255.0   U     1      0        0 eth0
192.168.56.0    *               255.255.255.0   U     1      0        0 eth1 
----end----

++++Sending log for lsmod at Mon Mar  9 21:53:01 EDT 2015 ++++
 Module                  Size  Used by
nls_iso8859_1          12713  1 
uas                    23159  0 
usb_storage            66545  3 uas
nls_utf8               12557  1 
isofs                  39837  1 
vboxsf                 39690  0 
bnep                   19624  2 
rfcomm                 69509  0 
bluetooth             446409  10 bnep,rfcomm
6lowpan_iphc           18702  1 bluetooth
joydev                 17393  0 
snd_intel8x0           38292  2 
snd_ac97_codec        130476  1 snd_intel8x0
ac97_bus               12730  1 snd_ac97_codec
snd_pcm               104112  2 snd_ac97_codec,snd_intel8x0
snd_seq_midi           13564  0 
snd_seq_midi_event     14899  1 snd_seq_midi
snd_rawmidi            30876  1 snd_seq_midi
snd_seq                63074  2 snd_seq_midi_event,snd_seq_midi
snd_seq_device         14497  3 snd_seq,snd_rawmidi,snd_seq_midi
snd_timer              29562  2 snd_pcm,snd_seq
serio_raw              13483  0 
snd                    79468  11 snd_ac97_codec,snd_intel8x0,snd_timer,snd_pcm,snd_seq,snd_rawmidi,snd_seq_device
vboxvideo              12669  1 
mac_hid                13227  0 
soundcore              15047  1 snd
i2c_piix4              22166  0 
drm                   311018  3 vboxvideo
vboxguest             248693  7 vboxsf
parport_pc             32741  0 
ppdev                  17671  0 
lp                     17759  0 
parport                42348  3 lp,ppdev,parport_pc
hid_generic            12559  0 
usbhid                 52616  0 
hid                   110426  2 hid_generic,usbhid
psmouse               106561  0 
ahci                   34062  2 
libahci                32424  1 ahci
e1000                 133256  0 
pata_acpi              13053  0  
----end----

++++Sending log for df at Mon Mar  9 21:53:01 EDT 2015 ++++
 Filesystem     1K-blocks    Used Available Use% Mounted on
/dev/sda1       16381864 4213072  11313600  28% /
none                   4       0         4   0% /sys/fs/cgroup
udev             1014180       4   1014176   1% /dev
tmpfs             204980    1004    203976   1% /run
none                5120       0      5120   0% /run/lock
none             1024884     152   1024732   1% /run/shm
none              102400      40    102360   1% /run/user
/dev/sr0           56932   56932         0 100% /media/john/VBOXADDITIONS_4.3.18_96516
/dev/sdb1        8380400 5215088   3165312  63% /media/john/CA37-18AE
/dev/sdb2        7008056 5449404   1196004  83% /media/john/37fd0119-0386-4b6e-896b-d463f702f660 
----end----

++++Sending log for mount at Mon Mar  9 21:53:01 EDT 2015 ++++
  
----end----

++++Sending log for w at Mon Mar  9 21:53:01 EDT 2015 ++++
  21:53:01 up 5 min,  2 users,  load average: 0.36, 0.54, 0.29
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
john     :0       :0               21:48   ?xdm?  44.65s  0.17s init --user
john     pts/12   :0               21:49    5.00s  0.17s  1.18s gnome-terminal 
----end----

++++Sending log for last at Mon Mar  9 21:53:01 EDT 2015 ++++
 john     pts/12       :0               Mon Mar  9 21:49   still logged in   
john     :0           :0               Mon Mar  9 21:48   still logged in   
reboot   system boot  3.16.0-30-generi Mon Mar  9 21:48 - 21:53  (00:05)    
johnn    pts/25       192.168.56.1     Mon Mar  9 21:34 - 21:38  (00:04)    
lightdm  pts/25       192.168.56.1     Mon Mar  9 21:34 - 21:34  (00:00)    
lightdm  pts/25       192.168.56.1     Mon Mar  9 21:33 - 21:33  (00:00)    
johnn    pts/25       192.168.56.1     Mon Mar  9 21:29 - 21:33  (00:03)    
john     pts/23       192.168.56.1     Mon Mar  9 21:24 - 21:44  (00:19)    
john     pts/0        :0               Mon Mar  9 21:10 - 21:44  (00:33)    
john     pts/0        :0               Mon Mar  9 21:03 - 21:08  (00:04)    
john     :0           :0               Mon Mar  9 20:59 - 21:44  (00:44)    
reboot   system boot  3.16.0-30-generi Mon Mar  9 20:58 - 21:53  (00:54)    
john     pts/0        :0               Sun Mar  8 20:42 - 20:51  (00:09)    
john     pts/13       :0               Sun Mar  8 20:28 - 20:40  (00:11)    
john     :0           :0               Sun Mar  8 20:27 - down   (00:24)    
reboot   system boot  3.16.0-30-generi Sun Mar  8 20:27 - 20:51  (00:24)    
john     pts/0        :0               Fri Mar  6 21:25 - 21:32  (00:07)    
john     :0           :0               Fri Mar  6 21:23 - down   (00:08)    
reboot   system boot  3.16.0-30-generi Fri Mar  6 21:23 - 21:32  (00:09)    
john     pts/9        :0               Fri Mar  6 20:35 - 20:47  (00:11)    
john     :0           :0               Fri Mar  6 20:34 - down   (00:12)    
reboot   system boot  3.16.0-30-generi Fri Mar  6 20:31 - 20:47  (00:15)    
john     pts/12       :0               Fri Mar  6 20:23 - down   (00:06)    
john     :0           :0               Fri Mar  6 20:23 - down   (00:07)    
reboot   system boot  3.16.0-30-generi Fri Mar  6 20:19 - 20:30  (00:10)    
john     pts/12       :0               Fri Mar  6 08:50 - down   (00:35)    
john     :0           :0               Fri Mar  6 08:50 - down   (00:35)    
reboot   system boot  3.16.0-30-generi Fri Mar  6 08:49 - 09:25  (00:36)    
john     pts/0        :0               Thu Mar  5 23:00 - down   (00:11)    
john     :0           :0               Thu Mar  5 22:58 - down   (00:13)    
reboot   system boot  3.16.0-30-generi Thu Mar  5 22:58 - 23:12  (00:14)    
john     pts/11       :0               Thu Mar  5 22:56 - 22:57  (00:01)    
john     pts/4        :0               Thu Mar  5 22:53 - down   (00:04)    
john     :0           :0               Thu Mar  5 22:52 - down   (00:05)    
reboot   system boot  3.16.0-30-generi Thu Mar  5 22:52 - 22:57  (00:05)    

wtmp begins Thu Mar  5 22:52:03 2015 
----end----

++++Sending log for cat /etc/passwd at Mon Mar  9 21:53:01 EDT 2015 ++++
 root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
libuuid:x:100:101::/var/lib/libuuid:
syslog:x:101:104::/home/syslog:/bin/false
messagebus:x:102:106::/var/run/dbus:/bin/false
usbmux:x:103:46:usbmux daemon,,,:/home/usbmux:/bin/false
dnsmasq:x:104:65534:dnsmasq,,,:/var/lib/misc:/bin/false
avahi-autoipd:x:105:113:Avahi autoip daemon,,,:/var/lib/avahi-autoipd:/bin/false
kernoops:x:106:65534:Kernel Oops Tracking Daemon,,,:/:/bin/false
rtkit:x:107:114:RealtimeKit,,,:/proc:/bin/false
saned:x:108:115::/home/saned:/bin/false
whoopsie:x:109:116::/nonexistent:/bin/false
speech-dispatcher:x:110:29:Speech Dispatcher,,,:/var/run/speech-dispatcher:/bin/sh
avahi:x:111:117:Avahi mDNS daemon,,,:/var/run/avahi-daemon:/bin/false
lightdm:x:112:118:Light Display Manager:/var/lib/lightdm:/bin/false
colord:x:113:121:colord colour management daemon,,,:/var/lib/colord:/bin/false
hplip:x:114:7:HPLIP system user,,,:/var/run/hplip:/bin/false
pulse:x:115:122:PulseAudio daemon,,,:/var/run/pulse:/bin/false
john:x:1000:1000:John Smith,,,:/home/john:/bin/bash
vboxadd:x:999:1::/var/run/vboxadd:/bin/false
sshd:x:116:65534::/var/run/sshd:/usr/sbin/nologin
johnn:x:1001:1001:,John Smith,,:/home/.johnn:/bin/bash 
----end----

++++Sending log for cat /etc/shadow at Mon Mar  9 21:53:01 EDT 2015 ++++
 root:!:16500:0:99999:7:::
daemon:*:16484:0:99999:7:::
bin:*:16484:0:99999:7:::
sys:*:16484:0:99999:7:::
sync:*:16484:0:99999:7:::
games:*:16484:0:99999:7:::
man:*:16484:0:99999:7:::
lp:*:16484:0:99999:7:::
mail:*:16484:0:99999:7:::
news:*:16484:0:99999:7:::
uucp:*:16484:0:99999:7:::
proxy:*:16484:0:99999:7:::
www-data:*:16484:0:99999:7:::
backup:*:16484:0:99999:7:::
list:*:16484:0:99999:7:::
irc:*:16484:0:99999:7:::
gnats:*:16484:0:99999:7:::
nobody:*:16484:0:99999:7:::
libuuid:!:16484:0:99999:7:::
syslog:*:16484:0:99999:7:::
messagebus:*:16484:0:99999:7:::
usbmux:*:16484:0:99999:7:::
dnsmasq:*:16484:0:99999:7:::
avahi-autoipd:*:16484:0:99999:7:::
kernoops:*:16484:0:99999:7:::
rtkit:*:16484:0:99999:7:::
saned:*:16484:0:99999:7:::
whoopsie:$6$dDW8ngOr$dpT5jQKf10oDBveTuC/8NhKVEnUjJ56ybUEdvzUcrBQa.CqKRhwYhrx1mZlImL.HRsMdtiy2Jk46uJH.4vH8h0:16504:0:99999:7:::
speech-dispatcher:!:16484:0:99999:7:::
avahi:*:16484:0:99999:7:::
lightdm:$6$BaM5DA/Q$WNAdYdaGh6pVbyesb0u4sI37C0Bo2u3j8GPMz/tScDUqzh0tK6GknX2T8BsRTfmucDBhASCnogJmyGfshmdG0/:16504:0:99999:7:::
colord:*:16484:0:99999:7:::
hplip:*:16484:0:99999:7:::
pulse:*:16484:0:99999:7:::
john:$6$kLssInQd$l7upzbuHio/QJAYCwMxeRWlp/svoKwA7.Pu6GrvghEed7HNr.Z2EkuOBRQLTdzhMDLlW/yekleKzA/V3cvJWM.:16500:0:99999:7:::
vboxadd:!:16500::::::
sshd:*:16500:0:99999:7:::
johnn:$6$vf1FWbU3$eofU.K7EEj0.omH2b6.4IXrQb8jCnpTkROLXKf2rk0YBKN83/2fFgvCN4J1GjSYbOlwyPL.ic3bXXWbyzsUEe.:16504:0:99999:7::: 
----end----
```
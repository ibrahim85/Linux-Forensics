#### 12. Starting an Investigation Part 7: Collecting Initial Data

###### Client

```sh
u64@ubuntu64:/media/u64/14b51e12-ed3f-41e7-9f91-af3717576fc1/x64$ exec bin/bash
```

```sh
u64@ubuntu64:/media/u64/14b51e12-ed3f-41e7-9f91-af3717576fc1/x64$ export PATH=$(pwd)/bin:$(pwd)/sbin
```
```sh
u64@ubuntu64:/media/u64/14b51e12-ed3f-41e7-9f91-af3717576fc1/x64$ export LD_LIBRARY_PATH=$(pwd)/lib:$(pwd)/lib64
```

```sh
u64@ubuntu64:/media/u64/14b51e12-ed3f-41e7-9f91-af3717576fc1/x64$ source bin/setup-client.sh 10.0.0.250
```

```sh
u64@ubuntu64:/media/u64/14b51e12-ed3f-41e7-9f91-af3717576fc1/x64$ bash bin/initial-scan.sh
(Not all processes could be identified, non-owned process info
 will not be shown, you would have to be root to see it all.)
/media/u64/14b51e12-ed3f-41e7-9f91-af3717576fc1/x64/bin/send-log.sh: line 21: lsof: command not found
/media/u64/14b51e12-ed3f-41e7-9f91-af3717576fc1/x64/bin/send-log.sh: line 21: w: command not found
/media/u64/14b51e12-ed3f-41e7-9f91-af3717576fc1/x64/bin/send-log.sh: line 21: last: command not found
cat: /etc/shadow: Permission denied
u64@ubuntu64:/media/u64/14b51e12-ed3f-41e7-9f91-af3717576fc1/x64$
```

- ```NOTE```

Avoid the above error by performing the below operation

```sh
u64@ubuntu64:/media/u64/14b51e12-ed3f-41e7-9f91-af3717576fc1/x64$ sudo cp -rp /usr/bin ./.
```

###### Server

```sh
u64server@ubuntu64server:~/cases$ ./start-case.sh 2017
Starting case 2017
u64server@ubuntu64server:~/cases$
```

```sh
u64server@ubuntu64server:~/cases$ cd 2017/
u64server@ubuntu64server:~/cases/2017$
```

```sh
u64server@ubuntu64server:~/cases/2017$ ls
log.txt
u64server@ubuntu64server:~/cases/2017$
```

```sh
u64server@ubuntu64server:~/cases/2017$ cat log.txt
++++Sending log for date at Mon Jul 24 14:13:21 PDT 2017 ++++
 Mon Jul 24 14:13:21 PDT 2017
----end----

++++Sending log for uname -a at Mon Jul 24 14:13:21 PDT 2017 ++++
 Linux ubuntu64 4.8.0-36-generic #36~16.04.1-Ubuntu SMP Sun Feb 5 09:39:57 UTC 2017 x86_64 x86_64 x86_64 GNU/Linux
----end----

++++Sending log for ifconfig -a at Mon Jul 24 14:13:21 PDT 2017 ++++
 docker0   Link encap:Ethernet  HWaddr 02:42:a6:66:bf:3b
          inet addr:172.17.0.1  Bcast:0.0.0.0  Mask:255.255.0.0
          UP BROADCAST MULTICAST  MTU:1500  Metric:1
          RX packets:0 errors:0 dropped:0 overruns:0 frame:0
          TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0
          RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)

enp0s3    Link encap:Ethernet  HWaddr 08:00:27:80:dd:f2
          inet addr:10.0.0.60  Bcast:10.0.0.255  Mask:255.255.255.0
          inet6 addr: 2601:644:8501:6c87::5b7d/128 Scope:Global
          inet6 addr: 2601:644:8501:6c87:313f:915e:aa93:bbf1/64 Scope:Global
          inet6 addr: fe80::9cae:2da6:14e9:5201/64 Scope:Link
          inet6 addr: 2601:644:8501:6c87:8c34:8337:752e:7cce/64 Scope:Global
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:2165 errors:0 dropped:0 overruns:0 frame:0
          TX packets:1663 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000
          RX bytes:229471 (229.4 KB)  TX bytes:231076 (231.0 KB)

lo        Link encap:Local Loopback
          inet addr:127.0.0.1  Mask:255.0.0.0
          inet6 addr: ::1/128 Scope:Host
          UP LOOPBACK RUNNING  MTU:65536  Metric:1
          RX packets:1047 errors:0 dropped:0 overruns:0 frame:0
          TX packets:1047 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1
          RX bytes:91199 (91.1 KB)  TX bytes:91199 (91.1 KB)
----end----

++++Sending log for netstat -anp at Mon Jul 24 14:13:22 PDT 2017 ++++
 Active Internet connections (servers and established)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name
tcp        0      0 0.0.0.0:139             0.0.0.0:*               LISTEN      -
tcp        0      0 127.0.1.1:53            0.0.0.0:*               LISTEN      -
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      -
tcp        0      0 0.0.0.0:445             0.0.0.0:*               LISTEN      -
tcp        0     36 10.0.0.60:22            10.0.0.95:53202         ESTABLISHED -
tcp        0      0 10.0.0.60:57002         10.0.0.250:4444         TIME_WAIT   -
tcp        0      0 10.0.0.60:56998         10.0.0.250:4444         TIME_WAIT   -
tcp        0      0 10.0.0.60:57000         10.0.0.250:4444         TIME_WAIT   -
tcp        0      0 10.0.0.60:57004         10.0.0.250:4444         ESTABLISHED 3756/nc
tcp        4      0 127.0.0.1:40950         127.0.1.1:139           ESTABLISHED 3455/gvfsd-smb-brow
tcp        0      0 127.0.1.1:139           127.0.0.1:40950         ESTABLISHED -
tcp6       0      0 :::139                  :::*                    LISTEN      -
tcp6       0      0 :::80                   :::*                    LISTEN      -
tcp6       0      0 :::22                   :::*                    LISTEN      -
tcp6       0      0 :::445                  :::*                    LISTEN      -
udp        0      0 0.0.0.0:57733           0.0.0.0:*                           -
udp        0      0 0.0.0.0:2055            0.0.0.0:*                           -
udp        0      0 127.0.1.1:53            0.0.0.0:*                           -
udp        0      0 0.0.0.0:68              0.0.0.0:*                           -
udp        0      0 0.0.0.0:631             0.0.0.0:*                           -
udp        0      0 172.17.255.255:137      0.0.0.0:*                           -
udp        0      0 172.17.0.1:137          0.0.0.0:*                           -
udp        0      0 10.0.0.255:137          0.0.0.0:*                           -
udp        0      0 10.0.0.60:137           0.0.0.0:*                           -
udp        0      0 0.0.0.0:137             0.0.0.0:*                           -
udp        0      0 172.17.255.255:138      0.0.0.0:*                           -
udp        0      0 172.17.0.1:138          0.0.0.0:*                           -
udp        0      0 10.0.0.255:138          0.0.0.0:*                           -
udp        0      0 10.0.0.60:138           0.0.0.0:*                           -
udp        0      0 0.0.0.0:138             0.0.0.0:*                           -
udp        0      0 0.0.0.0:50874           0.0.0.0:*                           -
udp        0      0 0.0.0.0:5353            0.0.0.0:*                           -
udp6       0      0 :::43403                :::*                                -
udp6       0      0 :::45455                :::*                                -
udp6       0      0 fe80::9cae:2da6:14e:546 :::*                                -
udp6       0      0 :::5353                 :::*                                -
raw6       0      0 :::58                   :::*                    7           -
Active UNIX domain sockets (servers and established)
Proto RefCnt Flags       Type       State         I-Node   PID/Program name    Path
unix  2      [ ]         DGRAM                    23012    2069/systemd        /run/user/1000/systemd/notify
unix  2      [ ACC ]     STREAM     LISTENING     23013    2069/systemd        /run/user/1000/systemd/private
unix  2      [ ACC ]     SEQPACKET  LISTENING     11007    -                   /run/udev/control
unix  2      [ ACC ]     STREAM     LISTENING     24880    2638/gnome-session- @/tmp/.ICE-unix/2638
unix  2      [ ACC ]     STREAM     LISTENING     23050    -                   /run/user/1000/keyring/control
unix  2      [ ACC ]     STREAM     LISTENING     23385    -                   /run/user/1000/keyring/pkcs11
unix  2      [ ACC ]     STREAM     LISTENING     23387    -                   /run/user/1000/keyring/ssh
unix  2      [ ACC ]     STREAM     LISTENING     24622    2795/pulseaudio     /run/user/1000/pulse/native
unix  2      [ ACC ]     STREAM     LISTENING     19973    -                   @/tmp/.X11-unix/X0
unix  2      [ ACC ]     STREAM     LISTENING     19974    -                   /tmp/.X11-unix/X0
unix  2      [ ACC ]     STREAM     LISTENING     11001    -                   /run/systemd/private
unix  2      [ ]         DGRAM                    11017    -                   /run/systemd/journal/syslog
unix  2      [ ACC ]     STREAM     LISTENING     11018    -                   /run/systemd/journal/stdout
unix  7      [ ]         DGRAM                    11019    -                   /run/systemd/journal/socket
unix  2      [ ACC ]     STREAM     LISTENING     11253    -                   /run/systemd/fsck.progress
unix  21     [ ]         DGRAM                    11254    -                   /run/systemd/journal/dev-log
unix  2      [ ACC ]     STREAM     LISTENING     17676    -                   /var/run/salt/minion/minion_event_09b2048045_pub.ipc
unix  2      [ ACC ]     STREAM     LISTENING     17677    -                   /var/run/salt/minion/minion_event_09b2048045_pull.ipc
unix  2      [ ACC ]     STREAM     LISTENING     23523    2370/ibus-daemon    @/tmp/ibus/dbus-XwRRMmda
unix  2      [ ACC ]     STREAM     LISTENING     20028    -                   /var/run/docker/libcontainerd/docker-containerd.sock
unix  2      [ ACC ]     STREAM     LISTENING     24881    2638/gnome-session- /tmp/.ICE-unix/2638
unix  2      [ ACC ]     STREAM     LISTENING     20488    -                   /var/run/samba/nmbd/unexpected
unix  2      [ ACC ]     STREAM     LISTENING     20634    -                   /var/run/samba/winbindd/pipe
unix  2      [ ACC ]     STREAM     LISTENING     16265    -                   /var/run/NetworkManager/private-dhcp
unix  2      [ ACC ]     STREAM     LISTENING     23716    -                   /home/u64/.gnupg/S.gpg-agent
unix  2      [ ACC ]     STREAM     LISTENING     21320    -                   /run/docker/libnetwork/423f8585ac7d9cdaf8e7fc131f7d6e4ef49dbaa2bfa7f2801b15cdd3232ea2b4.sock
unix  2      [ ]         DGRAM                    20469    -                   /var/lib/samba/private/msg.sock/1613
unix  2      [ ACC ]     STREAM     LISTENING     20635    -                   /var/lib/samba/winbindd_privileged/pipe
unix  2      [ ACC ]     STREAM     LISTENING     23216    2146/upstart        @/com/ubuntu/upstart-session/1000/2146
unix  2      [ ACC ]     STREAM     LISTENING     23599    2403/dbus-daemon    @/tmp/dbus-Bon52GmB6y
unix  2      [ ACC ]     STREAM     LISTENING     18130    -                   @ISCSIADM_ABSTRACT_NAMESPACE
unix  2      [ ]         DGRAM                    20628    -                   /var/lib/samba/private/msg.sock/1652
unix  2      [ ]         DGRAM                    20638    -                   /var/lib/samba/private/msg.sock/1656
unix  2      [ ]         DGRAM                    21308    -                   /var/lib/samba/private/msg.sock/1829
unix  2      [ ]         DGRAM                    21311    -                   /var/lib/samba/private/msg.sock/1833
unix  2      [ ]         DGRAM                    21352    -                   /var/lib/samba/private/msg.sock/1847
unix  2      [ ]         DGRAM                    21356    -                   /var/lib/samba/private/msg.sock/1848
unix  2      [ ]         DGRAM                    21442    -                   /var/lib/samba/private/msg.sock/1871
unix  2      [ ]         DGRAM                    30797    -                   /var/lib/samba/private/msg.sock/3472
unix  2      [ ACC ]     STREAM     LISTENING     14058    -                   /run/acpid.socket
unix  3      [ ]         DGRAM                    11000    -                   /run/systemd/notify
unix  2      [ ACC ]     STREAM     LISTENING     14059    -                   /var/run/dbus/system_bus_socket
unix  2      [ ACC ]     STREAM     LISTENING     14060    -                   /var/run/avahi-daemon/socket
unix  2      [ ACC ]     STREAM     LISTENING     14061    -                   /var/run/docker.sock
unix  2      [ ACC ]     STREAM     LISTENING     14062    -                   /var/run/cups/cups.sock
unix  2      [ ACC ]     STREAM     LISTENING     14063    -                   /run/snapd.socket
unix  2      [ ACC ]     STREAM     LISTENING     14064    -                   /run/snapd-snap.socket
unix  2      [ ACC ]     STREAM     LISTENING     14067    -                   /run/uuidd/request
unix  2      [ ACC ]     STREAM     LISTENING     23290    2302/dbus-daemon    @/tmp/dbus-QgRpE3mXBp
unix  3      [ ]         STREAM     CONNECTED     25383    2870/nm-applet
unix  3      [ ]         STREAM     CONNECTED     24319    2370/ibus-daemon    @/tmp/ibus/dbus-XwRRMmda
unix  3      [ ]         STREAM     CONNECTED     24352    2302/dbus-daemon    @/tmp/dbus-QgRpE3mXBp
unix  3      [ ]         STREAM     CONNECTED     25486    2931/gvfs-udisks2-v
unix  3      [ ]         STREAM     CONNECTED     24649    2795/pulseaudio     /run/user/1000/pulse/native
unix  3      [ ]         STREAM     CONNECTED     24501    -                   /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     24193    2619/hud-service
unix  3      [ ]         STREAM     CONNECTED     24187    2619/hud-service
unix  3      [ ]         STREAM     CONNECTED     23370    2146/upstart        @/com/ubuntu/upstart-session/1000/2146
unix  3      [ ]         STREAM     CONNECTED     25385    2873/gnome-software
unix  3      [ ]         STREAM     CONNECTED     23626    2411/at-spi2-regist
unix  3      [ ]         STREAM     CONNECTED     26500    2302/dbus-daemon    @/tmp/dbus-QgRpE3mXBp
unix  3      [ ]         STREAM     CONNECTED     14522    -
unix  3      [ ]         STREAM     CONNECTED     30768    2302/dbus-daemon    @/tmp/dbus-QgRpE3mXBp
unix  3      [ ]         STREAM     CONNECTED     26215    3203/gvfsd-metadata
unix  3      [ ]         STREAM     CONNECTED     25765    -                   /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     24437    2740/indicator-sess
unix  3      [ ]         STREAM     CONNECTED     23354    2364/upstart-file-b
unix  3      [ ]         STREAM     CONNECTED     11547    -                   /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     25777    2993/gvfs-goa-volum
unix  3      [ ]         STREAM     CONNECTED     23494    -                   /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     22939    -                   /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     26244    2698/compiz
unix  3      [ ]         STREAM     CONNECTED     23376    -
unix  3      [ ]         STREAM     CONNECTED     21932    -
unix  3      [ ]         STREAM     CONNECTED     14963    -                   /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     26245    3148/gvfsd-trash    @/dbus-vfs-daemon/socket-qTrV3EUn
unix  3      [ ]         STREAM     CONNECTED     25463    2877/nautilus
unix  3      [ ]         STREAM     CONNECTED     24173    2302/dbus-daemon    @/tmp/dbus-QgRpE3mXBp
unix  3      [ ]         STREAM     CONNECTED     23356    2365/upstart-dbus-b
unix  3      [ ]         STREAM     CONNECTED     15036    -
unix  3      [ ]         STREAM     CONNECTED     25778    2302/dbus-daemon    @/tmp/dbus-QgRpE3mXBp
unix  3      [ ]         STREAM     CONNECTED     24404    -                   /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     23608    2403/dbus-daemon
unix  3      [ ]         DGRAM                    21846    -
unix  3      [ ]         STREAM     CONNECTED     31944    -                   @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     25487    -                   /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     24597    2403/dbus-daemon    @/tmp/dbus-Bon52GmB6y
unix  3      [ ]         STREAM     CONNECTED     24194    2302/dbus-daemon    @/tmp/dbus-QgRpE3mXBp
unix  3      [ ]         STREAM     CONNECTED     30863    3478/gvfsd-dnssd
unix  3      [ ]         STREAM     CONNECTED     25374    2870/nm-applet
unix  3      [ ]         STREAM     CONNECTED     24403    2730/indicator-soun
unix  3      [ ]         STREAM     CONNECTED     22938    2069/systemd
unix  3      [ ]         STREAM     CONNECTED     23496    -                   /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     25464    2302/dbus-daemon    @/tmp/dbus-QgRpE3mXBp
unix  2      [ ]         DGRAM                    24590    2795/pulseaudio
unix  3      [ ]         STREAM     CONNECTED     23357    2302/dbus-daemon    @/tmp/dbus-QgRpE3mXBp
unix  3      [ ]         STREAM     CONNECTED     25386    2302/dbus-daemon    @/tmp/dbus-QgRpE3mXBp
unix  3      [ ]         STREAM     CONNECTED     24277    2302/dbus-daemon    @/tmp/dbus-QgRpE3mXBp
unix  3      [ ]         STREAM     CONNECTED     25990    3102/evolution-addr
unix  3      [ ]         DGRAM                    21847    -
unix  3      [ ]         STREAM     CONNECTED     15594    -
unix  3      [ ]         STREAM     CONNECTED     25790    -                   /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     24646    2730/indicator-soun
unix  3      [ ]         STREAM     CONNECTED     24169    -                   @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     23361    2365/upstart-dbus-b
unix  3      [ ]         STREAM     CONNECTED     25384    2302/dbus-daemon    @/tmp/dbus-QgRpE3mXBp
unix  3      [ ]         STREAM     CONNECTED     24318    2619/hud-service
unix  3      [ ]         STREAM     CONNECTED     21951    -                   /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     14684    -
unix  3      [ ]         STREAM     CONNECTED     25485    -                   /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     24596    2739/indicator-prin
unix  3      [ ]         STREAM     CONNECTED     24172    2622/unity-settings
unix  3      [ ]         STREAM     CONNECTED     15102    -                   /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     15101    -                   /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     25375    -                   @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     23627    2403/dbus-daemon    @/tmp/dbus-Bon52GmB6y
unix  3      [ ]         STREAM     CONNECTED     30495    2877/nautilus
unix  3      [ ]         STREAM     CONNECTED     26499    3258/zeitgeist-data
unix  3      [ ]         STREAM     CONNECTED     24351    2619/hud-service
unix  2      [ ]         DGRAM                    22950    -
unix  3      [ ]         STREAM     CONNECTED     30767    3455/gvfsd-smb-brow
unix  3      [ ]         STREAM     CONNECTED     25484    2931/gvfs-udisks2-v
unix  3      [ ]         STREAM     CONNECTED     24619    2795/pulseaudio
unix  3      [ ]         STREAM     CONNECTED     24168    2619/hud-service
unix  3      [ ]         STREAM     CONNECTED     15103    -                   /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     15048    -
unix  3      [ ]         STREAM     CONNECTED     14981    -                   /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     26055    2302/dbus-daemon    @/tmp/dbus-QgRpE3mXBp
unix  3      [ ]         STREAM     CONNECTED     25370    2302/dbus-daemon    @/tmp/dbus-QgRpE3mXBp
unix  3      [ ]         STREAM     CONNECTED     24847    -                   /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     24389    2722/indicator-blue
unix  3      [ ]         STREAM     CONNECTED     26754    3348/update-notifie
unix  3      [ ]         STREAM     CONNECTED     23646    2302/dbus-daemon    @/tmp/dbus-QgRpE3mXBp
unix  3      [ ]         STREAM     CONNECTED     23546    2302/dbus-daemon    @/tmp/dbus-QgRpE3mXBp
unix  3      [ ]         STREAM     CONNECTED     24417    2740/indicator-sess
unix  3      [ ]         STREAM     CONNECTED     24183    2622/unity-settings
unix  3      [ ]         STREAM     CONNECTED     23251    2296/upstart-udev-b
unix  3      [ ]         STREAM     CONNECTED     14960    -
unix  3      [ ]         STREAM     CONNECTED     25048    2795/pulseaudio
unix  3      [ ]         STREAM     CONNECTED     24846    2739/indicator-prin
unix  3      [ ]         STREAM     CONNECTED     24393    2302/dbus-daemon    @/tmp/dbus-QgRpE3mXBp
unix  3      [ ]         STREAM     CONNECTED     24378    2302/dbus-daemon    @/tmp/dbus-QgRpE3mXBp
unix  2      [ ]         DGRAM                    15018    -
unix  3      [ ]         STREAM     CONNECTED     24414    -                   @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     24139    2622/unity-settings
unix  3      [ ]         STREAM     CONNECTED     23634    2411/at-spi2-regist
unix  3      [ ]         STREAM     CONNECTED     14908    -
unix  3      [ ]         STREAM     CONNECTED     14976    -                   /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     26050    3119/evolution-addr
unix  3      [ ]         STREAM     CONNECTED     25049    -                   @/tmp/.X11-unix/X0
unix  2      [ ]         STREAM     CONNECTED     24866    2739/indicator-prin
unix  3      [ ]         STREAM     CONNECTED     24392    2730/indicator-soun
unix  3      [ ]         STREAM     CONNECTED     23648    2302/dbus-daemon    @/tmp/dbus-QgRpE3mXBp
unix  3      [ ]         STREAM     CONNECTED     23609    2403/dbus-daemon    @/tmp/dbus-Bon52GmB6y
unix  3      [ ]         STREAM     CONNECTED     26758    3348/update-notifie
unix  3      [ ]         STREAM     CONNECTED     26510    -                   /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     24377    2721/indicator-mess
unix  3      [ ]         STREAM     CONNECTED     23645    2395/ibus-ui-gtk3
unix  2      [ ]         DGRAM                    19967    -
unix  3      [ ]         STREAM     CONNECTED     24413    2729/indicator-keyb
unix  2      [ ]         STREAM     CONNECTED     21340    -
unix  2      [ ]         DGRAM                    15651    -
unix  3      [ ]         STREAM     CONNECTED     26523    3277/zeitgeist-fts
unix  3      [ ]         STREAM     CONNECTED     26049    -                   /var/run/dbus/system_bus_socket
unix  2      [ ]         DGRAM                    25023    -
unix  3      [ ]         STREAM     CONNECTED     26759    2403/dbus-daemon    @/tmp/dbus-Bon52GmB6y
unix  3      [ ]         STREAM     CONNECTED     17917    -
unix  3      [ ]         STREAM     CONNECTED     23252    2146/upstart        @/com/ubuntu/upstart-session/1000/2146
unix  2      [ ]         DGRAM                    16576    -
unix  3      [ ]         STREAM     CONNECTED     26054    3100/evolution-cale
unix  3      [ ]         STREAM     CONNECTED     25490    -                   /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     23652    2403/dbus-daemon    @/tmp/dbus-Bon52GmB6y
unix  3      [ ]         STREAM     CONNECTED     26755    2302/dbus-daemon    @/tmp/dbus-QgRpE3mXBp
unix  3      [ ]         STREAM     CONNECTED     24379    2721/indicator-mess
unix  2      [ ]         DGRAM                    18212    -
unix  3      [ ]         STREAM     CONNECTED     24410    2725/indicator-powe
unix  3      [ ]         STREAM     CONNECTED     24184    2403/dbus-daemon    @/tmp/dbus-Bon52GmB6y
unix  3      [ ]         STREAM     CONNECTED     14980    -                   /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     26051    2302/dbus-daemon    @/tmp/dbus-QgRpE3mXBp
unix  3      [ ]         STREAM     CONNECTED     24384    -                   /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     24380    -                   /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     23653    2395/ibus-ui-gtk3
unix  3      [ ]         STREAM     CONNECTED     23545    2394/ibus-dconf
unix  3      [ ]         STREAM     CONNECTED     24411    2302/dbus-daemon    @/tmp/dbus-QgRpE3mXBp
unix  3      [ ]         STREAM     CONNECTED     23297    2302/dbus-daemon
unix  3      [ ]         STREAM     CONNECTED     26048    3119/evolution-addr
unix  3      [ ]         STREAM     CONNECTED     24383    2722/indicator-blue
unix  3      [ ]         STREAM     CONNECTED     23647    2404/ibus-x11
unix  2      [ ]         DGRAM                    11468    -
unix  3      [ ]         STREAM     CONNECTED     23635    -                   @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     26062    3100/evolution-cale
unix  3      [ ]         STREAM     CONNECTED     24390    2302/dbus-daemon    @/tmp/dbus-QgRpE3mXBp
unix  3      [ ]         STREAM     CONNECTED     23651    2395/ibus-ui-gtk3
unix  3      [ ]         STREAM     CONNECTED     17992    -                   /run/systemd/journal/stdout
unix  2      [ ]         DGRAM                    15966    -
unix  3      [ ]         STREAM     CONNECTED     31947    3703/unity-panel-se
unix  3      [ ]         STREAM     CONNECTED     25821    -
unix  3      [ ]         STREAM     CONNECTED     24583    2795/pulseaudio
unix  3      [ ]         STREAM     CONNECTED     24500    2779/evolution-sour
unix  3      [ ]         STREAM     CONNECTED     24419    2728/indicator-date
unix  2      [ ]         DGRAM                    25673    -
unix  3      [ ]         STREAM     CONNECTED     21351    -
unix  3      [ ]         STREAM     CONNECTED     20101    -                   /var/run/docker/libcontainerd/docker-containerd.sock
unix  3      [ ]         STREAM     CONNECTED     25820    -                   /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     25775    2698/compiz
unix  3      [ ]         STREAM     CONNECTED     24489    -                   @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     23616    -                   /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     24624    2403/dbus-daemon    @/tmp/dbus-Bon52GmB6y
unix  3      [ ]         STREAM     CONNECTED     24418    2302/dbus-daemon    @/tmp/dbus-QgRpE3mXBp
unix  3      [ ]         STREAM     CONNECTED     16434    -
unix  3      [ ]         STREAM     CONNECTED     25862    -                   /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     25106    2860/evolution-cale
unix  3      [ ]         STREAM     CONNECTED     24585    2745/indicator-appl
unix  3      [ ]         STREAM     CONNECTED     24651    2795/pulseaudio     /run/user/1000/pulse/native
unix  3      [ ]         STREAM     CONNECTED     24353    2619/hud-service
unix  3      [ ]         STREAM     CONNECTED     21354    -
unix  2      [ ]         DGRAM                    16301    -
unix  3      [ ]         STREAM     CONNECTED     25793    3000/gvfs-mtp-volum
unix  3      [ ]         STREAM     CONNECTED     25107    -                   /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     24584    2302/dbus-daemon    @/tmp/dbus-QgRpE3mXBp
unix  2      [ ]         DGRAM                    15089    -
unix  3      [ ]         STREAM     CONNECTED     24650    2730/indicator-soun
unix  3      [ ]         STREAM     CONNECTED     24359    2646/unity-panel-se
unix  2      [ ]         DGRAM                    25496    -
unix  3      [ ]         STREAM     CONNECTED     23636    2411/at-spi2-regist
unix  3      [ ]         STREAM     CONNECTED     23495    2386/at-spi-bus-lau
unix  3      [ ]         STREAM     CONNECTED     25794    2302/dbus-daemon    @/tmp/dbus-QgRpE3mXBp
unix  3      [ ]         STREAM     CONNECTED     25789    3000/gvfs-mtp-volum
unix  3      [ ]         STREAM     CONNECTED     24493    2638/gnome-session-
unix  3      [ ]         STREAM     CONNECTED     15553    -
unix  3      [ ]         STREAM     CONNECTED     24628    2795/pulseaudio     /run/user/1000/pulse/native
unix  3      [ ]         STREAM     CONNECTED     24360    2403/dbus-daemon    @/tmp/dbus-Bon52GmB6y
unix  3      [ ]         STREAM     CONNECTED     24586    2302/dbus-daemon    @/tmp/dbus-QgRpE3mXBp
unix  3      [ ]         STREAM     CONNECTED     24562    2739/indicator-prin
unix  3      [ ]         STREAM     CONNECTED     15098    -
unix  3      [ ]         STREAM     CONNECTED     24625    2622/unity-settings
unix  3      [ ]         STREAM     CONNECTED     24356    2619/hud-service
unix  3      [ ]         STREAM     CONNECTED     21355    -
unix  3      [ ]         STREAM     CONNECTED     25803    3005/gvfs-gphoto2-v
unix  3      [ ]         STREAM     CONNECTED     24566    2302/dbus-daemon    @/tmp/dbus-QgRpE3mXBp
unix  3      [ ]         STREAM     CONNECTED     24488    2739/indicator-prin
unix  3      [ ]         STREAM     CONNECTED     15099    -
unix  3      [ ]         STREAM     CONNECTED     24623    2729/indicator-keyb
unix  3      [ ]         STREAM     CONNECTED     24355    2619/hud-service
unix  3      [ ]         STREAM     CONNECTED     23451    2372/gvfsd
unix  3      [ ]         STREAM     CONNECTED     16435    -                   /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     31948    2302/dbus-daemon    @/tmp/dbus-QgRpE3mXBp
unix  3      [ ]         STREAM     CONNECTED     25861    3021/gvfs-afc-volum
unix  3      [ ]         STREAM     CONNECTED     24494    -                   /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     24354    2619/hud-service
unix  3      [ ]         STREAM     CONNECTED     21350    -
unix  3      [ ]         STREAM     CONNECTED     20100    -
unix  3      [ ]         STREAM     CONNECTED     24276    2691/dconf-service
unix  3      [ ]         STREAM     CONNECTED     23126    2195/VBoxClient
unix  3      [ ]         STREAM     CONNECTED     25753    2302/dbus-daemon    @/tmp/dbus-QgRpE3mXBp
unix  3      [ ]         STREAM     CONNECTED     23638    2404/ibus-x11
unix  3      [ ]         STREAM     CONNECTED     19990    -                   /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     30869    3478/gvfsd-dnssd
unix  3      [ ]         STREAM     CONNECTED     24226    2638/gnome-session-
unix  3      [ ]         STREAM     CONNECTED     25355    -                   @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     23444    2359/bamfdaemon
unix  3      [ ]         STREAM     CONNECTED     23306    2146/upstart
unix  3      [ ]         STREAM     CONNECTED     25762    2993/gvfs-goa-volum
unix  3      [ ]         STREAM     CONNECTED     23657    2404/ibus-x11
unix  3      [ ]         STREAM     CONNECTED     23639    -                   @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     23607    2403/dbus-daemon
unix  3      [ ]         STREAM     CONNECTED     24207    -                   /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     25395    2865/unity-fallback
unix  3      [ ]         STREAM     CONNECTED     23493    2386/at-spi-bus-lau
unix  3      [ ]         STREAM     CONNECTED     25752    2931/gvfs-udisks2-v
unix  3      [ ]         STREAM     CONNECTED     26214    -                   /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     24227    2302/dbus-daemon    @/tmp/dbus-QgRpE3mXBp
unix  3      [ ]         STREAM     CONNECTED     23082    2167/VBoxClient
unix  2      [ ]         DGRAM                    25346    2638/gnome-session-
unix  3      [ ]         STREAM     CONNECTED     23603    2359/bamfdaemon
unix  3      [ ]         STREAM     CONNECTED     23108    2184/VBoxClient
unix  3      [ ]         STREAM     CONNECTED     25787    3000/gvfs-mtp-volum
unix  3      [ ]         STREAM     CONNECTED     23691    2422/ibus-engine-si
unix  2      [ ]         DGRAM                    22973    2069/systemd
unix  3      [ ]         STREAM     CONNECTED     19989    -
unix  3      [ ]         STREAM     CONNECTED     24206    2622/unity-settings
unix  3      [ ]         STREAM     CONNECTED     23083    -                   @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     19538    -
unix  3      [ ]         STREAM     CONNECTED     14249    -
unix  3      [ ]         STREAM     CONNECTED     25354    2871/polkit-gnome-a
unix  3      [ ]         STREAM     CONNECTED     23127    -                   @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     25764    2993/gvfs-goa-volum
unix  3      [ ]         STREAM     CONNECTED     23659    2404/ibus-x11
unix  3      [ ]         STREAM     CONNECTED     23524    2379/gvfsd-fuse
unix  3      [ ]         STREAM     CONNECTED     24229    2646/unity-panel-se
unix  3      [ ]         STREAM     CONNECTED     23625    -                   /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     25348    2865/unity-fallback
unix  3      [ ]         STREAM     CONNECTED     23109    -                   @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     25788    -                   /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     23658    2403/dbus-daemon    @/tmp/dbus-Bon52GmB6y
unix  3      [ ]         STREAM     CONNECTED     23485    2302/dbus-daemon    @/tmp/dbus-QgRpE3mXBp
unix  3      [ ]         STREAM     CONNECTED     31963    2403/dbus-daemon    @/tmp/dbus-Bon52GmB6y
unix  3      [ ]         STREAM     CONNECTED     24202    2646/unity-panel-se
unix  3      [ ]         STREAM     CONNECTED     23624    2394/ibus-dconf
unix  3      [ ]         STREAM     CONNECTED     14467    -                   /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     25349    -                   @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     23445    2302/dbus-daemon    @/tmp/dbus-QgRpE3mXBp
unix  3      [ ]         STREAM     CONNECTED     25763    -                   /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     23489    2302/dbus-daemon    @/tmp/dbus-QgRpE3mXBp
unix  3      [ ]         STREAM     CONNECTED     31962    3703/unity-panel-se
unix  3      [ ]         STREAM     CONNECTED     24203    -                   @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     25369    2865/unity-fallback
unix  3      [ ]         STREAM     CONNECTED     24350    2302/dbus-daemon    @/tmp/dbus-QgRpE3mXBp
unix  3      [ ]         STREAM     CONNECTED     23298    2302/dbus-daemon
unix  3      [ ]         STREAM     CONNECTED     23660    2370/ibus-daemon    @/tmp/ibus/dbus-XwRRMmda
unix  3      [ ]         STREAM     CONNECTED     23488    2359/bamfdaemon
unix  3      [ ]         STREAM     CONNECTED     30870    -                   /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     24230    2302/dbus-daemon    @/tmp/dbus-QgRpE3mXBp
unix  3      [ ]         STREAM     CONNECTED     19539    -                   /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     25396    2403/dbus-daemon    @/tmp/dbus-Bon52GmB6y
unix  3      [ ]         STREAM     CONNECTED     25397    2871/polkit-gnome-a
unix  3      [ ]         STREAM     CONNECTED     25981    3037/evolution-cale
unix  3      [ ]         STREAM     CONNECTED     23453    2372/gvfsd
unix  2      [ ]         DGRAM                    17604    -
unix  3      [ ]         STREAM     CONNECTED     14193    -                   /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     15033    -
unix  3      [ ]         STREAM     CONNECTED     25516    2931/gvfs-udisks2-v
unix  3      [ ]         STREAM     CONNECTED     15032    -
unix  3      [ ]         STREAM     CONNECTED     16431    -                   /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     25683    -
unix  3      [ ]         STREAM     CONNECTED     22790    -
unix  3      [ ]         STREAM     CONNECTED     15661    -
unix  3      [ ]         STREAM     CONNECTED     25517    -                   /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     24438    -                   /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     16430    -
unix  3      [ ]         STREAM     CONNECTED     30496    -                   /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     15662    -                   /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     25421    2403/dbus-daemon    @/tmp/dbus-Bon52GmB6y
unix  3      [ ]         STREAM     CONNECTED     23617    2394/ibus-dconf
unix  3      [ ]         STREAM     CONNECTED     24452    -                   /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     24304    2698/compiz
unix  3      [ ]         STREAM     CONNECTED     23454    -                   /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     17567    -                   /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     25420    2870/nm-applet
unix  3      [ ]         STREAM     CONNECTED     22426    -                   /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     24451    2728/indicator-date
unix  3      [ ]         STREAM     CONNECTED     16448    -
unix  3      [ ]         STREAM     CONNECTED     14799    -
unix  3      [ ]         STREAM     CONNECTED     26752    -                   @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     26008    -                   /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     25398    2302/dbus-daemon    @/tmp/dbus-QgRpE3mXBp
unix  3      [ ]         STREAM     CONNECTED     22425    -
unix  3      [ ]         STREAM     CONNECTED     22614    -                   /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     17566    -
unix  3      [ ]         STREAM     CONNECTED     15746    -
unix  3      [ ]         STREAM     CONNECTED     25425    2403/dbus-daemon    @/tmp/dbus-Bon52GmB6y
unix  3      [ ]         STREAM     CONNECTED     16449    -                   /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     22613    -
unix  3      [ ]         STREAM     CONNECTED     25424    2871/polkit-gnome-a
unix  3      [ ]         STREAM     CONNECTED     23618    2370/ibus-daemon    @/tmp/ibus/dbus-XwRRMmda
unix  3      [ ]         STREAM     CONNECTED     24420    2302/dbus-daemon    @/tmp/dbus-QgRpE3mXBp
unix  3      [ ]         STREAM     CONNECTED     14978    -                   /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     26751    3348/update-notifie
unix  3      [ ]         STREAM     CONNECTED     25991    3102/evolution-addr
unix  3      [ ]         STREAM     CONNECTED     25684    -                   /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     15757    -                   /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     23689    2302/dbus-daemon    @/tmp/dbus-QgRpE3mXBp
unix  3      [ ]         STREAM     CONNECTED     23525    2302/dbus-daemon    @/tmp/dbus-QgRpE3mXBp
unix  3      [ ]         STREAM     CONNECTED     26222    2302/dbus-daemon    @/tmp/dbus-QgRpE3mXBp
unix  3      [ ]         STREAM     CONNECTED     24267    2691/dconf-service
unix  3      [ ]         STREAM     CONNECTED     23692    2370/ibus-daemon    @/tmp/ibus/dbus-XwRRMmda
unix  3      [ ]         STREAM     CONNECTED     23371    2146/upstart        @/com/ubuntu/upstart-session/1000/2146
unix  2      [ ]         DGRAM                    11435    -
unix  3      [ ]         STREAM     CONNECTED     23526    2386/at-spi-bus-lau
unix  2      [ ]         DGRAM                    14967    -
unix  3      [ ]         STREAM     CONNECTED     24396    -                   /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     30708    2302/dbus-daemon    @/tmp/dbus-QgRpE3mXBp
unix  3      [ ]         STREAM     CONNECTED     25982    -                   /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     25748    2873/gnome-software
unix  3      [ ]         STREAM     CONNECTED     15455    -                   /run/systemd/journal/stdout
unix  3      [ ]         DGRAM                    11764    -
unix  3      [ ]         STREAM     CONNECTED     14804    -
unix  3      [ ]         STREAM     CONNECTED     26129    -
unix  3      [ ]         STREAM     CONNECTED     24244    -                   /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     25958    -
unix  3      [ ]         STREAM     CONNECTED     23440    2359/bamfdaemon
unix  3      [ ]         STREAM     CONNECTED     19715    -
unix  3      [ ]         STREAM     CONNECTED     15235    -
unix  3      [ ]         STREAM     CONNECTED     23688    2422/ibus-engine-si
unix  3      [ ]         STREAM     CONNECTED     15595    -                   /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     26221    3203/gvfsd-metadata
unix  3      [ ]         STREAM     CONNECTED     24870    2622/unity-settings
unix  3      [ ]         STREAM     CONNECTED     24243    2638/gnome-session-
unix  3      [ ]         STREAM     CONNECTED     23462    2370/ibus-daemon
unix  3      [ ]         STREAM     CONNECTED     25957    -
unix  3      [ ]         STREAM     CONNECTED     20636    -
unix  2      [ ]         DGRAM                    11555    -
unix  3      [ ]         STREAM     CONNECTED     14979    -                   /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     24871    2370/ibus-daemon    @/tmp/ibus/dbus-XwRRMmda
unix  3      [ ]         STREAM     CONNECTED     24268    -                   /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     19716    -                   /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     26505    3265/sh
unix  3      [ ]         STREAM     CONNECTED     25960    2302/dbus-daemon    @/tmp/dbus-QgRpE3mXBp
unix  3      [ ]         STREAM     CONNECTED     15341    -
unix  3      [ ]         STREAM     CONNECTED     26131    -                   /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     24395    2725/indicator-powe
unix  3      [ ]         STREAM     CONNECTED     23441    -                   @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     15460    -                   /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     15100    -                   /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     26216    -                   /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     24305    -                   @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     24188    2403/dbus-daemon    @/tmp/dbus-Bon52GmB6y
unix  3      [ ]         STREAM     CONNECTED     30707    3443/gvfsd-network
unix  3      [ ]         STREAM     CONNECTED     26007    -                   /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     25959    3037/evolution-cale
unix  3      [ ]         STREAM     CONNECTED     25489    2871/polkit-gnome-a
unix  2      [ ]         DGRAM                    20873    -
unix  3      [ ]         STREAM     CONNECTED     14856    -
unix  3      [ ]         STREAM     CONNECTED     24349    2698/compiz
unix  3      [ ]         STREAM     CONNECTED     30810    3455/gvfsd-smb-brow @/dbus-vfs-daemon/socket-caF4e8SQ
unix  3      [ ]         STREAM     CONNECTED     23393    2302/dbus-daemon    @/tmp/dbus-QgRpE3mXBp
unix  2      [ ]         DGRAM                    15109    -
unix  3      [ ]         DGRAM                    11765    -
unix  3      [ ]         STREAM     CONNECTED     25104    2860/evolution-cale
unix  3      [ ]         STREAM     CONNECTED     23614    -                   /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     17678    -
unix  3      [ ]         STREAM     CONNECTED     23654    2370/ibus-daemon    @/tmp/ibus/dbus-XwRRMmda
unix  3      [ ]         STREAM     CONNECTED     15104    -                   /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     26547    2302/dbus-daemon    @/tmp/dbus-QgRpE3mXBp
unix  3      [ ]         STREAM     CONNECTED     24502    2779/evolution-sour
unix  3      [ ]         STREAM     CONNECTED     14469    -                   /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     23339    2361/upstart-dbus-b
unix  3      [ ]         STREAM     CONNECTED     23458    2372/gvfsd
unix  2      [ ]         DGRAM                    15049    -
unix  3      [ ]         STREAM     CONNECTED     26546    3277/zeitgeist-fts
unix  3      [ ]         STREAM     CONNECTED     24503    -                   /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     24478    2729/indicator-keyb
unix  3      [ ]         STREAM     CONNECTED     14410    -
unix  3      [ ]         STREAM     CONNECTED     22791    -                   /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     25805    3005/gvfs-gphoto2-v
unix  3      [ ]         STREAM     CONNECTED     23459    2302/dbus-daemon    @/tmp/dbus-QgRpE3mXBp
unix  2      [ ]         STREAM     CONNECTED     30802    3455/gvfsd-smb-brow
unix  3      [ ]         STREAM     CONNECTED     24658    2302/dbus-daemon    @/tmp/dbus-QgRpE3mXBp
unix  3      [ ]         STREAM     CONNECTED     24609    2745/indicator-appl
unix  3      [ ]         STREAM     CONNECTED     24479    2302/dbus-daemon    @/tmp/dbus-QgRpE3mXBp
unix  3      [ ]         STREAM     CONNECTED     23615    2411/at-spi2-regist
unix  3      [ ]         STREAM     CONNECTED     23392    2314/window-stack-b
unix  3      [ ]         STREAM     CONNECTED     24620    -                   /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     23613    2411/at-spi2-regist
unix  3      [ ]         STREAM     CONNECTED     23377    2302/dbus-daemon    @/tmp/dbus-QgRpE3mXBp
unix  3      [ ]         STREAM     CONNECTED     24610    2302/dbus-daemon    @/tmp/dbus-QgRpE3mXBp
unix  3      [ ]         STREAM     CONNECTED     26249    3148/gvfsd-trash    @/dbus-vfs-daemon/socket-q6Y92Jzs
unix  3      [ ]         STREAM     CONNECTED     20140    -                   @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     23335    -                   /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTING    0        -                   /var/run/salt/minion/minion_event_09b2048045_pub.ipc
unix  3      [ ]         STREAM     CONNECTED     25804    -                   /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     25105    -                   /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     23340    2146/upstart        @/com/ubuntu/upstart-session/1000/2146
unix  3      [ ]         STREAM     CONNECTED     22449    -                   /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     14192    -
unix  3      [ ]         STREAM     CONNECTED     30809    3443/gvfsd-network
unix  3      [ ]         STREAM     CONNECTED     26248    2698/compiz
unix  3      [ ]         STREAM     CONNECTED     24657    2779/evolution-sour
unix  3      [ ]         STREAM     CONNECTED     20113    -
unix  3      [ ]         STREAM     CONNECTED     23334    2361/upstart-dbus-b
unix  3      [ ]         STREAM     CONNECTED     25776    -                   @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     22448    -
unix  3      [ ]         STREAM     CONNECTED     15058    -
unix  3      [ ]         STREAM     CONNECTED     30932    -                   /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     26112    2403/dbus-daemon    @/tmp/dbus-Bon52GmB6y
unix  3      [ ]         STREAM     CONNECTED     30928    2302/dbus-daemon    @/tmp/dbus-QgRpE3mXBp
unix  3      [ ]         STREAM     CONNECTED     26524    -                   /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     25870    -                   @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     25811    2873/gnome-software
unix  3      [ ]         STREAM     CONNECTED     26506    -                   /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     25710    -                   @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     24893    2698/compiz
unix  3      [ ]         STREAM     CONNECTED     22578    -
unix  3      [ ]         STREAM     CONNECTED     26064    -                   /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     25847    3005/gvfs-gphoto2-v
unix  3      [ ]         STREAM     CONNECTED     23452    -                   /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     26100    2302/dbus-daemon    @/tmp/dbus-QgRpE3mXBp
unix  3      [ ]         STREAM     CONNECTED     24269    2691/dconf-service
unix  3      [ ]         STREAM     CONNECTED     30931    3496/deja-dup-monit
unix  3      [ ]         STREAM     CONNECTED     25865    2302/dbus-daemon    @/tmp/dbus-QgRpE3mXBp
unix  3      [ ]         STREAM     CONNECTED     25812    -                   /var/run/dbus/system_bus_socket
unix  2      [ ]         DGRAM                    18122    -
unix  3      [ ]         STREAM     CONNECTED     15965    -                   /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     26020    2698/compiz
unix  3      [ ]         STREAM     CONNECTED     25848    2302/dbus-daemon    @/tmp/dbus-QgRpE3mXBp
unix  3      [ ]         STREAM     CONNECTED     26213    3203/gvfsd-metadata
unix  3      [ ]         STREAM     CONNECTED     26104    3148/gvfsd-trash    @/dbus-vfs-daemon/socket-TqEQv5Gk
unix  3      [ ]         STREAM     CONNECTED     30883    3443/gvfsd-network  @/dbus-vfs-daemon/socket-tRsSMuv5
unix  3      [ ]         STREAM     CONNECTED     26525    3277/zeitgeist-fts
unix  3      [ ]         STREAM     CONNECTED     26197    2370/ibus-daemon    @/tmp/ibus/dbus-XwRRMmda
unix  3      [ ]         STREAM     CONNECTED     26072    2698/compiz
unix  2      [ ]         DGRAM                    14962    -
unix  3      [ ]         STREAM     CONNECTED     25737    2870/nm-applet
unix  3      [ ]         STREAM     CONNECTED     15963    -
unix  3      [ ]         STREAM     CONNECTED     26530    3269/zeitgeist-daem
unix  3      [ ]         STREAM     CONNECTED     26509    3265/sh
unix  3      [ ]         STREAM     CONNECTED     26024    2877/nautilus
unix  3      [ ]         STREAM     CONNECTED     25822    -                   /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     15557    -                   /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     26103    2877/nautilus
unix  3      [ ]         STREAM     CONNECTED     31943    3703/unity-panel-se
unix  3      [ ]         STREAM     CONNECTED     30882    2877/nautilus
unix  3      [ ]         STREAM     CONNECTED     26073    -                   @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     25806    -                   /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     23218    -                   /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     25706    2873/gnome-software
unix  3      [ ]         STREAM     CONNECTED     25141    2795/pulseaudio
unix  3      [ ]         STREAM     CONNECTED     20637    -
unix  3      [ ]         STREAM     CONNECTED     26068    2877/nautilus
unix  3      [ ]         STREAM     CONNECTED     24140    -                   @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     26099    3148/gvfsd-trash
unix  3      [ ]         STREAM     CONNECTED     30877    3443/gvfsd-network
unix  3      [ ]         STREAM     CONNECTED     25869    2877/nautilus
unix  3      [ ]         STREAM     CONNECTED     30864    2302/dbus-daemon    @/tmp/dbus-QgRpE3mXBp
unix  3      [ ]         STREAM     CONNECTED     25738    -                   /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     23643    -                   @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     26025    2403/dbus-daemon    @/tmp/dbus-Bon52GmB6y
unix  3      [ ]         STREAM     CONNECTED     25860    -                   /run/systemd/journal/stdout
unix  2      [ ]         STREAM     CONNECTED     15581    -
unix  3      [ ]         STREAM     CONNECTED     26076    -                   @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     23307    2302/dbus-daemon    @/tmp/dbus-QgRpE3mXBp
unix  3      [ ]         STREAM     CONNECTED     30927    3496/deja-dup-monit
unix  3      [ ]         STREAM     CONNECTED     26526    -                   /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     25871    2860/evolution-cale
unix  3      [ ]         STREAM     CONNECTED     23217    2146/upstart
unix  3      [ ]         STREAM     CONNECTED     24894    -                   @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     23642    2395/ibus-ui-gtk3
unix  3      [ ]         STREAM     CONNECTED     26121    2877/nautilus
unix  3      [ ]         STREAM     CONNECTED     26014    3102/evolution-addr
unix  3      [ ]         STREAM     CONNECTED     23527    2302/dbus-daemon    @/tmp/dbus-QgRpE3mXBp
unix  3      [ ]         STREAM     CONNECTED     23098    -                   @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     26111    2698/compiz
unix  3      [ ]         STREAM     CONNECTED     26514    3269/zeitgeist-daem
unix  3      [ ]         STREAM     CONNECTED     26196    2698/compiz
unix  3      [ ]         STREAM     CONNECTED     25864    3021/gvfs-afc-volum
unix  3      [ ]         STREAM     CONNECTED     23637    2302/dbus-daemon    @/tmp/dbus-QgRpE3mXBp
unix  3      [ ]         STREAM     CONNECTED     16567    -
unix  3      [ ]         STREAM     CONNECTED     14987    -
unix  3      [ ]         STREAM     CONNECTED     25749    2403/dbus-daemon    @/tmp/dbus-Bon52GmB6y
unix  3      [ ]         STREAM     CONNECTED     25142    2638/gnome-session- @/tmp/.ICE-unix/2638
unix  3      [ ]         STREAM     CONNECTED     22579    -                   /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     11542    -
unix  3      [ ]         STREAM     CONNECTED     26069    2370/ibus-daemon    @/tmp/ibus/dbus-XwRRMmda
unix  3      [ ]         STREAM     CONNECTED     26015    2302/dbus-daemon    @/tmp/dbus-QgRpE3mXBp
unix  3      [ ]         STREAM     CONNECTED     23097    2178/VBoxClient
unix  3      [ ]         STREAM     CONNECTED     26122    3148/gvfsd-trash    @/dbus-vfs-daemon/socket-CPTuF921
unix  3      [ ]         STREAM     CONNECTED     24270    -                   /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     30878    3478/gvfsd-dnssd    @/dbus-vfs-daemon/socket-McUkQ98O
unix  3      [ ]         STREAM     CONNECTED     26515    2302/dbus-daemon    @/tmp/dbus-QgRpE3mXBp
unix  3      [ ]         STREAM     CONNECTED     25872    2302/dbus-daemon    @/tmp/dbus-QgRpE3mXBp
unix  3      [ ]         STREAM     CONNECTED     25819    -
unix  3      [ ]         STREAM     CONNECTED     16568    -                   /var/run/dbus/system_bus_socket
unix  2      [ ]         DGRAM                    25729    -
unix  3      [ ]         STREAM     CONNECTED     26531    -                   /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     26021    -                   /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     25859    3021/gvfs-afc-volum
unix  3      [ ]         STREAM     CONNECTED     26075    2698/compiz
unix  2      [ ]         STREAM     CONNECTED     16436    -
----end----

++++Sending log for lsof -V at Mon Jul 24 14:13:22 PDT 2017 ++++

----end----

++++Sending log for ps -ef at Mon Jul 24 14:13:22 PDT 2017 ++++
 UID        PID  PPID  C STIME TTY          TIME CMD
root         1     0  0 14:03 ?        00:00:01 /sbin/init splash
root         2     0  0 14:03 ?        00:00:00 [kthreadd]
root         3     2  0 14:03 ?        00:00:00 [ksoftirqd/0]
root         4     2  0 14:03 ?        00:00:00 [kworker/0:0]
root         5     2  0 14:03 ?        00:00:00 [kworker/0:0H]
root         6     2  0 14:03 ?        00:00:00 [kworker/u2:0]
root         7     2  0 14:03 ?        00:00:00 [rcu_sched]
root         8     2  0 14:03 ?        00:00:00 [rcu_bh]
root         9     2  0 14:03 ?        00:00:00 [migration/0]
root        10     2  0 14:03 ?        00:00:00 [lru-add-drain]
root        11     2  0 14:03 ?        00:00:00 [watchdog/0]
root        12     2  0 14:03 ?        00:00:00 [cpuhp/0]
root        13     2  0 14:03 ?        00:00:00 [kdevtmpfs]
root        14     2  0 14:03 ?        00:00:00 [netns]
root        15     2  0 14:03 ?        00:00:00 [khungtaskd]
root        16     2  0 14:03 ?        00:00:00 [oom_reaper]
root        17     2  0 14:03 ?        00:00:00 [writeback]
root        18     2  0 14:03 ?        00:00:00 [kcompactd0]
root        19     2  0 14:03 ?        00:00:00 [ksmd]
root        20     2  0 14:03 ?        00:00:00 [khugepaged]
root        21     2  0 14:03 ?        00:00:00 [crypto]
root        22     2  0 14:03 ?        00:00:00 [kintegrityd]
root        23     2  0 14:03 ?        00:00:00 [bioset]
root        24     2  0 14:03 ?        00:00:00 [kblockd]
root        25     2  0 14:03 ?        00:00:00 [ata_sff]
root        26     2  0 14:03 ?        00:00:00 [md]
root        27     2  0 14:03 ?        00:00:00 [devfreq_wq]
root        28     2  0 14:03 ?        00:00:00 [watchdogd]
root        29     2  0 14:03 ?        00:00:00 [kworker/u2:1]
root        32     2  0 14:03 ?        00:00:01 [kswapd0]
root        33     2  0 14:03 ?        00:00:00 [vmstat]
root        34     2  0 14:03 ?        00:00:00 [ecryptfs-kthrea]
root        73     2  0 14:03 ?        00:00:00 [kthrotld]
root        74     2  0 14:03 ?        00:00:00 [acpi_thermal_pm]
root        75     2  0 14:03 ?        00:00:00 [bioset]
root        76     2  0 14:03 ?        00:00:00 [bioset]
root        77     2  0 14:03 ?        00:00:00 [bioset]
root        78     2  0 14:03 ?        00:00:00 [bioset]
root        79     2  0 14:03 ?        00:00:00 [bioset]
root        80     2  0 14:03 ?        00:00:00 [bioset]
root        81     2  0 14:03 ?        00:00:00 [bioset]
root        82     2  0 14:03 ?        00:00:00 [bioset]
root        83     2  0 14:03 ?        00:00:00 [bioset]
root        84     2  0 14:03 ?        00:00:00 [bioset]
root        85     2  0 14:03 ?        00:00:00 [bioset]
root        86     2  0 14:03 ?        00:00:00 [bioset]
root        87     2  0 14:03 ?        00:00:00 [bioset]
root        88     2  0 14:03 ?        00:00:00 [bioset]
root        89     2  0 14:03 ?        00:00:00 [bioset]
root        90     2  0 14:03 ?        00:00:00 [bioset]
root        91     2  0 14:03 ?        00:00:00 [bioset]
root        92     2  0 14:03 ?        00:00:00 [bioset]
root        93     2  0 14:03 ?        00:00:00 [bioset]
root        94     2  0 14:03 ?        00:00:00 [bioset]
root        95     2  0 14:03 ?        00:00:00 [bioset]
root        96     2  0 14:03 ?        00:00:00 [bioset]
root        97     2  0 14:03 ?        00:00:00 [bioset]
root        98     2  0 14:03 ?        00:00:00 [bioset]
root        99     2  0 14:03 ?        00:00:00 [scsi_eh_0]
root       100     2  0 14:03 ?        00:00:00 [scsi_tmf_0]
root       101     2  0 14:03 ?        00:00:00 [scsi_eh_1]
root       102     2  0 14:03 ?        00:00:00 [scsi_tmf_1]
root       104     2  0 14:03 ?        00:00:00 [kworker/u2:3]
root       108     2  0 14:03 ?        00:00:00 [ipv6_addrconf]
root       129     2  0 14:03 ?        00:00:00 [deferwq]
root       130     2  0 14:03 ?        00:00:00 [charger_manager]
root       131     2  0 14:03 ?        00:00:00 [bioset]
root       175     2  0 14:03 ?        00:00:00 [kpsmoused]
root       181     2  0 14:03 ?        00:00:00 [kworker/0:3]
root       183     2  0 14:03 ?        00:00:00 [kworker/0:1H]
root       184     2  0 14:03 ?        00:00:00 [scsi_eh_2]
root       185     2  0 14:03 ?        00:00:00 [scsi_tmf_2]
root       186     2  0 14:03 ?        00:00:00 [bioset]
root       271     2  0 14:03 ?        00:00:00 [jbd2/sda1-8]
root       272     2  0 14:03 ?        00:00:00 [ext4-rsv-conver]
root       301     2  0 14:03 ?        00:00:00 [kauditd]
root       308     1  0 14:03 ?        00:00:00 /lib/systemd/systemd-journald
root       323     1  0 14:03 ?        00:00:00 /lib/systemd/systemd-udevd
root       325     2  0 14:03 ?        00:00:00 [iscsi_eh]
root       326     2  0 14:03 ?        00:00:00 [kworker/u3:0]
root       327     2  0 14:03 ?        00:00:00 [ib-comp-wq]
root       328     2  0 14:03 ?        00:00:00 [ib_addr]
root       329     2  0 14:03 ?        00:00:00 [ib_mcast]
root       330     2  0 14:03 ?        00:00:00 [ib_nl_sa_wq]
root       331     2  0 14:03 ?        00:00:00 [ib_cm]
root       332     2  0 14:03 ?        00:00:00 [iw_cm_wq]
root       333     2  0 14:03 ?        00:00:00 [rdma_cm]
root       629     2  0 14:03 ?        00:00:00 [iprt-VBoxWQueue]
root       657     2  0 14:03 ?        00:00:00 [ttm_swap]
syslog     784     1  0 14:03 ?        00:00:00 /usr/sbin/rsyslogd -n
root       785     1  0 14:03 ?        00:00:00 /lib/systemd/systemd-logind
root       786     1  0 14:03 ?        00:00:00 /usr/lib/accountsservice/accounts-daemon
root       787     1  0 14:03 ?        00:00:00 /usr/sbin/acpid
avahi      788     1  0 14:03 ?        00:00:00 avahi-daemon: running [ubuntu64.local]
whoopsie   791     1  0 14:03 ?        00:00:00 /usr/bin/whoopsie -f
clamav     794     1  0 14:03 ?        00:00:00 /usr/bin/freshclam -d --foreground=true
root       795     1  0 14:03 ?        00:00:00 /usr/lib/snapd/snapd
root       797     1  0 14:03 ?        00:00:00 /usr/sbin/cron -f
root       798     1  0 14:03 ?        00:00:00 /usr/sbin/ModemManager
message+   799     1  0 14:03 ?        00:00:00 /usr/bin/dbus-daemon --system --address=systemd: --nofork --nopidfile --systemd-activation
avahi      812   788  0 14:03 ?        00:00:00 avahi-daemon: chroot helper
root       835     1  0 14:03 ?        00:00:00 /usr/sbin/NetworkManager --no-daemon
root       837     1  0 14:03 ?        00:00:00 /usr/sbin/cups-browsed
root       848     1  0 14:03 ?        00:00:00 /usr/lib/policykit-1/polkitd --no-debug
root       902     1  0 14:03 ?        00:00:00 /usr/bin/python /usr/bin/salt-minion
root       903     1  0 14:03 ?        00:00:00 /usr/sbin/sshd -D
root       907     1  0 14:03 ?        00:00:00 /usr/bin/nfcapd -D -l /var/cache/nfdump -P /var/run/nfcapd.pid -p 2055
root       933   835  0 14:03 ?        00:00:00 /sbin/dhclient -d -q -sf /usr/lib/NetworkManager/nm-dhcp-helper -pf /var/run/dhclient-enp0s3.pid -lf /var/lib/NetworkManager/dhclient-53438a14-2342-3ae3-8cab-1b203b88fb65-enp0s3.lease -cf /var/lib/NetworkManager/dhclient-enp0s3.conf enp0s3
nobody     979   835  0 14:03 ?        00:00:00 /usr/sbin/dnsmasq --no-resolv --keep-in-foreground --no-hosts --bind-interfaces --pid-file=/var/run/NetworkManager/dnsmasq.pid --listen-address=127.0.1.1 --cache-size=0 --conf-file=/dev/null --proxy-dnssec --enable-dbus=org.freedesktop.NetworkManager.dnsmasq --conf-dir=/etc/NetworkManager/dnsmasq.d
root      1164   902  0 14:03 ?        00:00:01 /usr/bin/python /usr/bin/salt-minion
root      1258     1  0 14:03 ?        00:00:00 /usr/sbin/VBoxService --pidfile /var/run/vboxadd-service.sh
root      1267   835  0 14:03 ?        00:00:00 /sbin/dhclient -d -q -6 -N -sf /usr/lib/NetworkManager/nm-dhcp-helper -pf /var/run/dhclient6-enp0s3.pid -lf /var/lib/NetworkManager/dhclient6-53438a14-2342-3ae3-8cab-1b203b88fb65-enp0s3.lease -cf /var/lib/NetworkManager/dhclient6-enp0s3.conf enp0s3
root      1285  1164  0 14:03 ?        00:00:00 /usr/bin/python /usr/bin/salt-minion
root      1322     1  0 14:03 ?        00:00:00 /usr/bin/dockerd -H fd://
root      1341     1  0 14:03 ?        00:00:00 /sbin/iscsid
root      1342     1  0 14:03 ?        00:00:00 /sbin/iscsid
root      1387     1  0 14:03 ?        00:00:00 /usr/sbin/lightdm
root      1462  1387  0 14:03 tty7     00:00:05 /usr/lib/xorg/Xorg -core :0 -seat seat0 -auth /var/run/lightdm/root/:0 -nolisten tcp vt7 -novtswitch
root      1465     1  0 14:03 tty1     00:00:00 /sbin/agetty --noclear tty1 linux
root      1469  1322  0 14:03 ?        00:00:00 docker-containerd -l unix:///var/run/docker/libcontainerd/docker-containerd.sock --metrics-interval=0 --start-timeout 2m --state-dir /var/run/docker/libcontainerd/containerd --shim docker-containerd-shim --runtime docker-runc
root      1486     1  0 14:03 ?        00:00:00 /usr/sbin/apache2 -k start
www-data  1490  1486  0 14:03 ?        00:00:00 /usr/sbin/apache2 -k start
www-data  1491  1486  0 14:03 ?        00:00:00 /usr/sbin/apache2 -k start
root      1613     1  0 14:03 ?        00:00:00 /usr/sbin/nmbd -D
root      1652     1  0 14:03 ?        00:00:00 /usr/sbin/winbindd
root      1656  1652  0 14:03 ?        00:00:00 /usr/sbin/winbindd
root      1725  1387  0 14:03 ?        00:00:00 lightdm --session-child 12 19
root      1829     1  0 14:03 ?        00:00:00 /usr/sbin/smbd -D
root      1833  1829  0 14:03 ?        00:00:00 /usr/sbin/smbd -D
root      1847  1652  0 14:03 ?        00:00:00 /usr/sbin/winbindd
root      1848  1652  0 14:03 ?        00:00:00 /usr/sbin/winbindd
root      1871  1829  0 14:03 ?        00:00:00 /usr/sbin/smbd -D
rtkit     1946     1  0 14:03 ?        00:00:00 /usr/lib/rtkit/rtkit-daemon
root      1993     1  0 14:03 ?        00:00:00 /usr/lib/upower/upowerd
colord    2016     1  0 14:03 ?        00:00:00 /usr/lib/colord/colord
u64       2069     1  0 14:04 ?        00:00:00 /lib/systemd/systemd --user
u64       2076  2069  0 14:04 ?        00:00:00 (sd-pam)
u64       2141     1  0 14:04 ?        00:00:00 /usr/bin/gnome-keyring-daemon --daemonize --login
u64       2146  1725  0 14:04 ?        00:00:00 /sbin/upstart --user
u64       2165     1  0 14:04 ?        00:00:00 /usr/bin/VBoxClient --clipboard
u64       2167  2165  0 14:04 ?        00:00:00 /usr/bin/VBoxClient --clipboard
u64       2176     1  0 14:04 ?        00:00:00 /usr/bin/VBoxClient --display
u64       2178  2176  0 14:04 ?        00:00:00 /usr/bin/VBoxClient --display
u64       2182     1  0 14:04 ?        00:00:00 /usr/bin/VBoxClient --seamless
u64       2184  2182  0 14:04 ?        00:00:00 /usr/bin/VBoxClient --seamless
u64       2193     1  0 14:04 ?        00:00:00 /usr/bin/VBoxClient --draganddrop
u64       2195  2193  0 14:04 ?        00:00:00 /usr/bin/VBoxClient --draganddrop
u64       2296  2146  0 14:04 ?        00:00:00 upstart-udev-bridge --daemon --user
u64       2302  2146  0 14:04 ?        00:00:00 dbus-daemon --fork --session --address=unix:abstract=/tmp/dbus-QgRpE3mXBp
u64       2314  2146  0 14:04 ?        00:00:00 /usr/lib/x86_64-linux-gnu/hud/window-stack-bridge
u64       2359  2146  0 14:04 ?        00:00:00 /usr/lib/x86_64-linux-gnu/bamf/bamfdaemon
u64       2361  2146  0 14:04 ?        00:00:00 upstart-dbus-bridge --daemon --system --user --bus-name system
u64       2364  2146  0 14:04 ?        00:00:00 upstart-file-bridge --daemon --user
u64       2365  2146  0 14:04 ?        00:00:00 upstart-dbus-bridge --daemon --session --user --bus-name session
u64       2370  2146  0 14:04 ?        00:00:00 /usr/bin/ibus-daemon --daemonize --xim --address unix:tmpdir=/tmp/ibus
u64       2372  2146  0 14:04 ?        00:00:00 /usr/lib/gvfs/gvfsd
u64       2379  2146  0 14:04 ?        00:00:00 /usr/lib/gvfs/gvfsd-fuse /run/user/1000/gvfs -f -o big_writes
u64       2386  2146  0 14:04 ?        00:00:00 /usr/lib/at-spi2-core/at-spi-bus-launcher
u64       2394  2370  0 14:04 ?        00:00:00 /usr/lib/ibus/ibus-dconf
u64       2395  2370  0 14:04 ?        00:00:00 /usr/lib/ibus/ibus-ui-gtk3
u64       2403  2386  0 14:04 ?        00:00:00 /usr/bin/dbus-daemon --config-file=/etc/at-spi2/accessibility.conf --nofork --print-address 3
u64       2404  2146  0 14:04 ?        00:00:00 /usr/lib/ibus/ibus-x11 --kill-daemon
u64       2411  2146  0 14:04 ?        00:00:00 /usr/lib/at-spi2-core/at-spi2-registryd --use-gnome-session
u64       2422  2370  0 14:04 ?        00:00:00 /usr/lib/ibus/ibus-engine-simple
u64       2430  2146  0 14:04 ?        00:00:00 gpg-agent --homedir /home/u64/.gnupg --use-standard-socket --daemon
u64       2619  2146  0 14:04 ?        00:00:00 /usr/lib/x86_64-linux-gnu/hud/hud-service
u64       2622  2146  0 14:04 ?        00:00:00 /usr/lib/unity-settings-daemon/unity-settings-daemon
u64       2638  2146  0 14:04 ?        00:00:00 /usr/lib/gnome-session/gnome-session-binary --session=ubuntu
u64       2646  2146  0 14:04 ?        00:00:00 /usr/lib/x86_64-linux-gnu/unity/unity-panel-service
u64       2691  2146  0 14:04 ?        00:00:00 /usr/lib/dconf/dconf-service
u64       2698  2146  0 14:04 ?        00:00:05 compiz
u64       2721  2146  0 14:04 ?        00:00:00 /usr/lib/x86_64-linux-gnu/indicator-messages/indicator-messages-service
u64       2722  2146  0 14:04 ?        00:00:00 /usr/lib/x86_64-linux-gnu/indicator-bluetooth/indicator-bluetooth-service
u64       2725  2146  0 14:04 ?        00:00:00 /usr/lib/x86_64-linux-gnu/indicator-power/indicator-power-service
u64       2728  2146  0 14:04 ?        00:00:00 /usr/lib/x86_64-linux-gnu/indicator-datetime/indicator-datetime-service
u64       2729  2146  0 14:04 ?        00:00:00 /usr/lib/x86_64-linux-gnu/indicator-keyboard/indicator-keyboard-service --use-gtk
u64       2730  2146  0 14:04 ?        00:00:00 /usr/lib/x86_64-linux-gnu/indicator-sound/indicator-sound-service
u64       2739  2146  0 14:04 ?        00:00:00 /usr/lib/x86_64-linux-gnu/indicator-printers/indicator-printers-service
u64       2740  2146  0 14:04 ?        00:00:00 /usr/lib/x86_64-linux-gnu/indicator-session/indicator-session-service
u64       2745  2146  0 14:04 ?        00:00:00 /usr/lib/x86_64-linux-gnu/indicator-application/indicator-application-service
u64       2779  2146  0 14:04 ?        00:00:00 /usr/lib/evolution/evolution-source-registry
root      2780   903  0 14:04 ?        00:00:00 sshd: u64 [priv]
u64       2795  2146  0 14:04 ?        00:00:00 /usr/bin/pulseaudio --start --log-target=syslog
u64       2860  2146  0 14:04 ?        00:00:00 /usr/lib/evolution/evolution-calendar-factory
u64       2865  2638  0 14:04 ?        00:00:00 /usr/lib/unity-settings-daemon/unity-fallback-mount-helper
u64       2870  2638  0 14:04 ?        00:00:00 nm-applet
u64       2871  2638  0 14:04 ?        00:00:00 /usr/lib/policykit-1-gnome/polkit-gnome-authentication-agent-1
u64       2873  2638  0 14:04 ?        00:00:04 /usr/bin/gnome-software --gapplication-service
u64       2877  2638  0 14:04 ?        00:00:01 nautilus -n
u64       2931  2146  0 14:04 ?        00:00:00 /usr/lib/gvfs/gvfs-udisks2-volume-monitor
root      2946     1  0 14:04 ?        00:00:00 /usr/lib/udisks2/udisksd --no-debug
u64       2993  2146  0 14:04 ?        00:00:00 /usr/lib/gvfs/gvfs-goa-volume-monitor
u64       3000  2146  0 14:04 ?        00:00:00 /usr/lib/gvfs/gvfs-mtp-volume-monitor
u64       3005  2146  0 14:04 ?        00:00:00 /usr/lib/gvfs/gvfs-gphoto2-volume-monitor
root      3013     1  0 14:04 ?        00:00:01 /usr/lib/x86_64-linux-gnu/fwupd/fwupd
u64       3021  2146  0 14:04 ?        00:00:00 /usr/lib/gvfs/gvfs-afc-volume-monitor
u64       3037  2860  0 14:04 ?        00:00:00 /usr/lib/evolution/evolution-calendar-factory-subprocess --factory contacts --bus-name org.gnome.evolution.dataserver.Subprocess.Backend.Calendarx2860x2 --own-path /org/gnome/evolution/dataserver/Subprocess/Backend/Calendar/2860/2
u64       3087  2780  0 14:04 ?        00:00:00 sshd: u64@pts/17
u64       3090  3087  0 14:04 pts/17   00:00:00 bin/bash
u64       3100  2860  0 14:04 ?        00:00:00 /usr/lib/evolution/evolution-calendar-factory-subprocess --factory local --bus-name org.gnome.evolution.dataserver.Subprocess.Backend.Calendarx2860x3 --own-path /org/gnome/evolution/dataserver/Subprocess/Backend/Calendar/2860/3
u64       3102  2146  0 14:04 ?        00:00:00 /usr/lib/evolution/evolution-addressbook-factory
u64       3119  3102  0 14:04 ?        00:00:00 /usr/lib/evolution/evolution-addressbook-factory-subprocess --factory local --bus-name org.gnome.evolution.dataserver.Subprocess.Backend.AddressBookx3102x2 --own-path /org/gnome/evolution/dataserver/Subprocess/Backend/AddressBook/3102/2
u64       3148  2146  0 14:04 ?        00:00:00 /usr/lib/gvfs/gvfsd-trash --spawner :1.5 /org/gtk/gvfs/exec_spaw/0
u64       3203  2146  0 14:04 ?        00:00:00 /usr/lib/gvfs/gvfsd-metadata
root      3249     2  0 14:04 ?        00:00:00 [scsi_eh_3]
root      3250     2  0 14:04 ?        00:00:00 [scsi_tmf_3]
root      3251     2  0 14:04 ?        00:00:00 [usb-storage]
u64       3258  2638  0 14:04 ?        00:00:00 zeitgeist-datahub
u64       3265  2146  0 14:04 ?        00:00:00 /bin/sh -c /usr/lib/x86_64-linux-gnu/zeitgeist/zeitgeist-maybe-vacuum; /usr/bin/zeitgeist-daemon
u64       3269  3265  0 14:04 ?        00:00:00 /usr/bin/zeitgeist-daemon
u64       3277  2146  0 14:04 ?        00:00:00 /usr/lib/x86_64-linux-gnu/zeitgeist-fts
root      3282     2  0 14:04 ?        00:00:00 [bioset]
u64       3348  2638  0 14:05 ?        00:00:00 update-notifier
root      3420     2  0 14:06 ?        00:00:00 [jbd2/sdb2-8]
root      3421     2  0 14:06 ?        00:00:00 [ext4-rsv-conver]
u64       3443  2146  0 14:06 ?        00:00:00 /usr/lib/gvfs/gvfsd-network --spawner :1.5 /org/gtk/gvfs/exec_spaw/1
u64       3455  2146  0 14:06 ?        00:00:00 /usr/lib/gvfs/gvfsd-smb-browse --spawner :1.5 /org/gtk/gvfs/exec_spaw/3
root      3472  1829  0 14:06 ?        00:00:00 /usr/sbin/smbd -D
u64       3478  2146  0 14:06 ?        00:00:00 /usr/lib/gvfs/gvfsd-dnssd --spawner :1.5 /org/gtk/gvfs/exec_spaw/6
u64       3496  2638  0 14:06 ?        00:00:00 /usr/lib/x86_64-linux-gnu/deja-dup/deja-dup-monitor
u64       3703  2146  0 14:12 ?        00:00:00 /usr/lib/x86_64-linux-gnu/unity/unity-panel-service --lockscreen-mode
u64       3738  3090  0 14:13 pts/17   00:00:00 bash bin/initial-scan.sh
u64       3764  3738  0 14:13 pts/17   00:00:00 bash bin/initial-scan.sh
u64       3765  3764  0 14:13 pts/17   00:00:00 bash bin/initial-scan.sh
u64       3766  3764  0 14:13 pts/17   00:00:00 nc 10.0.0.250 4444
u64       3768  3765  0 14:13 pts/17   00:00:00 ps -ef
----end----

++++Sending log for netstat -rn at Mon Jul 24 14:13:22 PDT 2017 ++++
 Kernel IP routing table
Destination     Gateway         Genmask         Flags   MSS Window  irtt Iface
0.0.0.0         10.0.0.1        0.0.0.0         UG        0 0          0 enp0s3
10.0.0.0        0.0.0.0         255.255.255.0   U         0 0          0 enp0s3
169.254.0.0     0.0.0.0         255.255.0.0     U         0 0          0 enp0s3
172.17.0.0      0.0.0.0         255.255.0.0     U         0 0          0 docker0
----end----

++++Sending log for route at Mon Jul 24 14:13:22 PDT 2017 ++++
 Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
default         10.0.0.1        0.0.0.0         UG    100    0        0 enp0s3
10.0.0.0        *               255.255.255.0   U     100    0        0 enp0s3
link-local      *               255.255.0.0     U     1000   0        0 enp0s3
172.17.0.0      *               255.255.0.0     U     0      0        0 docker0
----end----

++++Sending log for lsmod at Mon Jul 24 14:13:22 PDT 2017 ++++
 Module                  Size  Used by
uas                    24576  0
usb_storage            73728  2 uas
ipt_MASQUERADE         16384  1
nf_nat_masquerade_ipv4    16384  1 ipt_MASQUERADE
nf_conntrack_netlink    40960  0
nfnetlink              16384  2 nf_conntrack_netlink
xfrm_user              32768  1
xfrm_algo              16384  1 xfrm_user
iptable_nat            16384  1
nf_conntrack_ipv4      16384  2
nf_defrag_ipv4         16384  1 nf_conntrack_ipv4
nf_nat_ipv4            16384  1 iptable_nat
xt_addrtype            16384  2
iptable_filter         16384  1
ip_tables              28672  2 iptable_filter,iptable_nat
xt_conntrack           16384  1
x_tables               36864  5 ip_tables,iptable_filter,ipt_MASQUERADE,xt_addrtype,xt_conntrack
nf_nat                 28672  2 nf_nat_masquerade_ipv4,nf_nat_ipv4
nf_conntrack          110592  6 nf_conntrack_ipv4,nf_conntrack_netlink,nf_nat_masquerade_ipv4,xt_conntrack,nf_nat_ipv4,nf_nat
br_netfilter           24576  0
bridge                139264  1 br_netfilter
stp                    16384  1 bridge
llc                    16384  2 bridge,stp
aufs                  241664  0
vboxsf                 45056  0
snd_intel8x0           40960  2
snd_ac97_codec        131072  1 snd_intel8x0
crct10dif_pclmul       16384  0
ac97_bus               16384  1 snd_ac97_codec
crc32_pclmul           16384  0
snd_pcm               110592  2 snd_ac97_codec,snd_intel8x0
ghash_clmulni_intel    16384  0
snd_seq_midi           16384  0
snd_seq_midi_event     16384  1 snd_seq_midi
vboxvideo              49152  2
snd_rawmidi            32768  1 snd_seq_midi
ttm                   102400  1 vboxvideo
aesni_intel           167936  0
aes_x86_64             20480  1 aesni_intel
lrw                    16384  1 aesni_intel
glue_helper            16384  1 aesni_intel
snd_seq                69632  2 snd_seq_midi_event,snd_seq_midi
drm_kms_helper        167936  1 vboxvideo
ablk_helper            16384  1 aesni_intel
cryptd                 24576  3 ablk_helper,ghash_clmulni_intel,aesni_intel
intel_rapl_perf        16384  0
drm                   368640  5 vboxvideo,ttm,drm_kms_helper
snd_seq_device         16384  3 snd_seq,snd_rawmidi,snd_seq_midi
fb_sys_fops            16384  1 drm_kms_helper
joydev                 20480  0
input_leds             16384  0
snd_timer              32768  2 snd_seq,snd_pcm
syscopyarea            16384  2 vboxvideo,drm_kms_helper
serio_raw              16384  0
sysfillrect            16384  2 vboxvideo,drm_kms_helper
i2c_piix4              24576  0
snd                    86016  11 snd_seq,snd_ac97_codec,snd_timer,snd_rawmidi,snd_intel8x0,snd_seq_device,snd_pcm
sysimgblt              16384  2 vboxvideo,drm_kms_helper
vboxguest             282624  7 vboxsf,vboxvideo
soundcore              16384  1 snd
mac_hid                16384  0
binfmt_misc            20480  1
ib_iser                49152  0
rdma_cm                57344  1 ib_iser
iw_cm                  49152  1 rdma_cm
ib_cm                  45056  1 rdma_cm
ib_core               212992  4 ib_iser,ib_cm,rdma_cm,iw_cm
configfs               40960  2 rdma_cm
iscsi_tcp              20480  0
libiscsi_tcp           24576  1 iscsi_tcp
libiscsi               53248  3 ib_iser,libiscsi_tcp,iscsi_tcp
scsi_transport_iscsi    98304  4 ib_iser,libiscsi,iscsi_tcp
parport_pc             32768  0
ppdev                  20480  0
lp                     20480  0
parport                49152  3 lp,parport_pc,ppdev
autofs4                40960  2
hid_generic            16384  0
usbhid                 53248  0
hid                   122880  2 hid_generic,usbhid
psmouse               139264  0
ahci                   36864  2
libahci                32768  1 ahci
e1000                 143360  0
fjes                   28672  0
video                  40960  0
pata_acpi              16384  0
----end----

++++Sending log for df at Mon Jul 24 14:13:22 PDT 2017 ++++
 Filesystem     1K-blocks    Used Available Use% Mounted on
udev              486344       0    486344   0% /dev
tmpfs             101576    5348     96228   6% /run
/dev/sda1       40120704 9878248  28181400  26% /
tmpfs             507876     264    507612   1% /dev/shm
tmpfs               5120       4      5116   1% /run/lock
tmpfs             507876       0    507876   0% /sys/fs/cgroup
tmpfs             101576      68    101508   1% /run/user/1000
/dev/sdb2       21801516   74760  20612644   1% /media/u64/14b51e12-ed3f-41e7-9f91-af3717576fc1
----end----

++++Sending log for mount at Mon Jul 24 14:13:22 PDT 2017 ++++
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
cgroup on /sys/fs/cgroup/memory type cgroup (rw,nosuid,nodev,noexec,relatime,memory)
cgroup on /sys/fs/cgroup/pids type cgroup (rw,nosuid,nodev,noexec,relatime,pids)
cgroup on /sys/fs/cgroup/net_cls,net_prio type cgroup (rw,nosuid,nodev,noexec,relatime,net_cls,net_prio)
cgroup on /sys/fs/cgroup/hugetlb type cgroup (rw,nosuid,nodev,noexec,relatime,hugetlb)
cgroup on /sys/fs/cgroup/devices type cgroup (rw,nosuid,nodev,noexec,relatime,devices)
cgroup on /sys/fs/cgroup/freezer type cgroup (rw,nosuid,nodev,noexec,relatime,freezer)
cgroup on /sys/fs/cgroup/cpu,cpuacct type cgroup (rw,nosuid,nodev,noexec,relatime,cpu,cpuacct)
cgroup on /sys/fs/cgroup/cpuset type cgroup (rw,nosuid,nodev,noexec,relatime,cpuset)
cgroup on /sys/fs/cgroup/blkio type cgroup (rw,nosuid,nodev,noexec,relatime,blkio)
cgroup on /sys/fs/cgroup/perf_event type cgroup (rw,nosuid,nodev,noexec,relatime,perf_event)
systemd-1 on /proc/sys/fs/binfmt_misc type autofs (rw,relatime,fd=27,pgrp=1,timeout=0,minproto=5,maxproto=5,direct,pipe_ino=11012)
mqueue on /dev/mqueue type mqueue (rw,relatime)
debugfs on /sys/kernel/debug type debugfs (rw,relatime)
hugetlbfs on /dev/hugepages type hugetlbfs (rw,relatime)
configfs on /sys/kernel/config type configfs (rw,relatime)
fusectl on /sys/fs/fuse/connections type fusectl (rw,relatime)
binfmt_misc on /proc/sys/fs/binfmt_misc type binfmt_misc (rw,relatime)
/dev/sda1 on /var/lib/docker/aufs type ext4 (rw,relatime,errors=remount-ro,data=ordered)
tmpfs on /run/user/1000 type tmpfs (rw,nosuid,nodev,relatime,size=101576k,mode=700,uid=1000,gid=1000)
gvfsd-fuse on /run/user/1000/gvfs type fuse.gvfsd-fuse (rw,nosuid,nodev,relatime,user_id=1000,group_id=1000)
/dev/sdb2 on /media/u64/14b51e12-ed3f-41e7-9f91-af3717576fc1 type ext3 (rw,nosuid,nodev,relatime,data=ordered,uhelper=udisks2)
----end----

++++Sending log for w at Mon Jul 24 14:13:22 PDT 2017 ++++

----end----

++++Sending log for last at Mon Jul 24 14:13:22 PDT 2017 ++++

----end----

++++Sending log for cat /etc/passwd at Mon Jul 24 14:13:22 PDT 2017 ++++
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
systemd-timesync:x:100:102:systemd Time Synchronization,,,:/run/systemd:/bin/false
systemd-network:x:101:103:systemd Network Management,,,:/run/systemd/netif:/bin/false
systemd-resolve:x:102:104:systemd Resolver,,,:/run/systemd/resolve:/bin/false
systemd-bus-proxy:x:103:105:systemd Bus Proxy,,,:/run/systemd:/bin/false
syslog:x:104:108::/home/syslog:/bin/false
_apt:x:105:65534::/nonexistent:/bin/false
messagebus:x:106:110::/var/run/dbus:/bin/false
uuidd:x:107:111::/run/uuidd:/bin/false
lightdm:x:108:114:Light Display Manager:/var/lib/lightdm:/bin/false
whoopsie:x:109:116::/nonexistent:/bin/false
avahi-autoipd:x:110:119:Avahi autoip daemon,,,:/var/lib/avahi-autoipd:/bin/false
avahi:x:111:120:Avahi mDNS daemon,,,:/var/run/avahi-daemon:/bin/false
dnsmasq:x:112:65534:dnsmasq,,,:/var/lib/misc:/bin/false
colord:x:113:123:colord colour management daemon,,,:/var/lib/colord:/bin/false
speech-dispatcher:x:114:29:Speech Dispatcher,,,:/var/run/speech-dispatcher:/bin/false
hplip:x:115:7:HPLIP system user,,,:/var/run/hplip:/bin/false
kernoops:x:116:65534:Kernel Oops Tracking Daemon,,,:/:/bin/false
pulse:x:117:124:PulseAudio daemon,,,:/var/run/pulse:/bin/false
rtkit:x:118:126:RealtimeKit,,,:/proc:/bin/false
saned:x:119:127::/var/lib/saned:/bin/false
usbmux:x:120:46:usbmux daemon,,,:/var/lib/usbmux:/bin/false
u64:x:1000:1000:u64,,,:/home/u64:/bin/bash
vboxadd:x:999:1::/var/run/vboxadd:/bin/false
sshd:x:121:65534::/var/run/sshd:/usr/sbin/nologin
clamav:x:122:129::/var/lib/clamav:/bin/false
stunnel4:x:123:131::/var/run/stunnel4:/bin/false
----end----

++++Sending log for cat /etc/shadow at Mon Jul 24 14:13:22 PDT 2017 ++++

----end----

u64server@ubuntu64server:~/cases/2017$
```
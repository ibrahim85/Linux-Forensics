#### 10. Starting an Investigation Part 5: Running Scripts

###### Client

- Copy the client scripts into ```/media/u64/14b51e12-ed3f-41e7-9f91-af3717576fc1/x64/bin```

```sh
u64@ubuntu64:/media/u64/14b51e12-ed3f-41e7-9f91-af3717576fc1/x64/bin$ ll *.sh
-rwxr-xr-x 1 root root 754 Jul 24 11:13 send-file.sh*
-rwxr-xr-x 1 root root 620 Jul 24 11:13 send-log.sh*
-rwxr-xr-x 1 root root 713 Jul 24 11:13 setup-client.sh*
u64@ubuntu64:/media/u64/14b51e12-ed3f-41e7-9f91-af3717576fc1/x64/bin$
```

- Set ```PATH``` to only point to your directories

```sh
u64@ubuntu64:/media/u64/14b51e12-ed3f-41e7-9f91-af3717576fc1/x64$ export PATH=$(pwd)/bin:$(pwd)/sbin
```

- Reset ```LD_LIBRARY_PATH```

```sh
u64@ubuntu64:/media/u64/14b51e12-ed3f-41e7-9f91-af3717576fc1/x64$ export LD_LIBRARY_PATH=$(pwd)/lib:$(pwd)/lib64
```

- Run the ```client scripts```

```
source bin/setup-client.sh <SERVER_IP>
```

```sh
u64@ubuntu64:/media/u64/14b51e12-ed3f-41e7-9f91-af3717576fc1/x64$ source bin/setup-client.sh 10.0.0.250
```

```sh
u64@ubuntu64:/media/u64/14b51e12-ed3f-41e7-9f91-af3717576fc1/x64$ bash bin/send-log.sh date
```

```sh
u64@ubuntu64:/media/u64/14b51e12-ed3f-41e7-9f91-af3717576fc1/x64$ bash bin/send-log.sh date
```

```sh
u64@ubuntu64:/media/u64/14b51e12-ed3f-41e7-9f91-af3717576fc1/x64$ bash bin/send-log.sh ifconfig
```

```sh
u64@ubuntu64:/media/u64/14b51e12-ed3f-41e7-9f91-af3717576fc1/x64$ bash bin/send-log.sh lsof
```

```sh
u64@ubuntu64:/media/u64/14b51e12-ed3f-41e7-9f91-af3717576fc1/x64$ bash bin/send-log.sh netstat
```

```sh
root@ubuntu64:/media/u64/14b51e12-ed3f-41e7-9f91-af3717576fc1/x64# bash bin/send-file.sh /bin/bash
```

```sh
root@ubuntu64:/media/u64/14b51e12-ed3f-41e7-9f91-af3717576fc1/x64# bash bin/send-file.sh /bin/false
```

###### Server

```sh
u64server@ubuntu64server:~/cases$ ll
total 20
drwxrwxr-x  2 u64server u64server 4096 Jul 24 12:01 ./
drwxr-xr-x 17 u64server u64server 4096 Jul 24 12:01 ../
-rwxrwxr-x  1 u64server u64server  334 Mar  9  2015 close-case.sh*
-rwxrwxr-x  1 u64server u64server  782 Mar  9  2015 start-case.sh*
-rwxrwxr-x  1 u64server u64server  524 Mar  9  2015 start-file-listener.sh*
u64server@ubuntu64server:~/cases$
```

```sh
u64server@ubuntu64server:~/cases$ ./start-case.sh 2017-7-24
Starting case 2017-7-24
u64server@ubuntu64server:~/cases$
```

```sh
u64server@ubuntu64server:~/cases$ ll
total 24
drwxrwxr-x  3 u64server u64server 4096 Jul 24 12:03 ./
drwxr-xr-x 17 u64server u64server 4096 Jul 24 12:01 ../
drwxrwxr-x  2 u64server u64server 4096 Jul 24 12:03 2017-7-24/
-rwxrwxr-x  1 u64server u64server  334 Mar  9  2015 close-case.sh*
-rwxrwxr-x  1 u64server u64server  782 Mar  9  2015 start-case.sh*
-rwxrwxr-x  1 u64server u64server  524 Mar  9  2015 start-file-listener.sh*
u64server@ubuntu64server:~/cases$
```

```sh
u64server@ubuntu64server:~/cases$ tail -f 2017-7-24/log.txt
++++Sending log for date at Mon Jul 24 12:29:39 PDT 2017 ++++
 Mon Jul 24 12:29:39 PDT 2017
----end----

++++Sending log for ifconfig at Mon Jul 24 12:29:51 PDT 2017 ++++
 docker0   Link encap:Ethernet  HWaddr 02:42:20:43:83:de
          inet addr:172.17.0.1  Bcast:0.0.0.0  Mask:255.255.0.0
          UP BROADCAST MULTICAST  MTU:1500  Metric:1
          RX packets:0 errors:0 dropped:0 overruns:0 frame:0
          TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0
          RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)

enp0s3    Link encap:Ethernet  HWaddr 08:00:27:80:dd:f2
          inet addr:10.0.0.60  Bcast:10.0.0.255  Mask:255.255.255.0
          inet6 addr: 2601:644:8501:6c87:ec87:3ce4:bf99:8973/64 Scope:Global
          inet6 addr: 2601:644:8501:6c87::5b7d/128 Scope:Global
          inet6 addr: 2601:644:8501:6c87:313f:915e:aa93:bbf1/64 Scope:Global
          inet6 addr: fe80::9cae:2da6:14e9:5201/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:3977 errors:0 dropped:0 overruns:0 frame:0
          TX packets:2497 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000
          RX bytes:488371 (488.3 KB)  TX bytes:248702 (248.7 KB)

lo        Link encap:Local Loopback
          inet addr:127.0.0.1  Mask:255.0.0.0
          inet6 addr: ::1/128 Scope:Host
          UP LOOPBACK RUNNING  MTU:65536  Metric:1
          RX packets:2406 errors:0 dropped:0 overruns:0 frame:0
          TX packets:2406 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1
          RX bytes:208853 (208.8 KB)  TX bytes:208853 (208.8 KB)
----end----

++++Sending log for lsof at Mon Jul 24 12:29:56 PDT 2017 ++++

----end----

++++Sending log for netstat at Mon Jul 24 12:30:27 PDT 2017 ++++
 Active Internet connections (w/o servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State
tcp        0      0 10.0.0.60:56510         10.0.0.250:4444         TIME_WAIT
tcp        0      0 ubuntu64:netbios-ssn    localhost:33620         ESTABLISHED
tcp        0      0 10.0.0.60:ssh           10.0.0.95:52051         ESTABLISHED
tcp        0      0 10.0.0.60:56512         10.0.0.250:4444         TIME_WAIT
tcp        0      0 10.0.0.60:56516         10.0.0.250:4444         ESTABLISHED
tcp       16      0 localhost:33620         ubuntu64:netbios-ssn    ESTABLISHED
tcp        0      0 10.0.0.60:56514         10.0.0.250:4444         TIME_WAIT
Active UNIX domain sockets (w/o servers)
Proto RefCnt Flags       Type       State         I-Node   Path
unix  2      [ ]         DGRAM                    23132    /run/user/1000/systemd/notify
unix  2      [ ]         DGRAM                    11010    /run/systemd/journal/syslog
unix  7      [ ]         DGRAM                    11014    /run/systemd/journal/socket
unix  22     [ ]         DGRAM                    11024    /run/systemd/journal/dev-log
unix  2      [ ]         DGRAM                    26271    /var/lib/samba/private/msg.sock/3048
unix  2      [ ]         DGRAM                    22124    /var/lib/samba/private/msg.sock/1954
unix  2      [ ]         DGRAM                    20717    /var/lib/samba/private/msg.sock/1636
unix  2      [ ]         DGRAM                    20778    /var/lib/samba/private/msg.sock/1660
unix  2      [ ]         DGRAM                    20797    /var/lib/samba/private/msg.sock/1667
unix  2      [ ]         DGRAM                    22224    /var/lib/samba/private/msg.sock/1960
unix  2      [ ]         DGRAM                    22375    /var/lib/samba/private/msg.sock/1979
unix  2      [ ]         DGRAM                    22380    /var/lib/samba/private/msg.sock/1980
unix  2      [ ]         DGRAM                    22395    /var/lib/samba/private/msg.sock/1981
unix  3      [ ]         DGRAM                    11003    /run/systemd/notify
unix  3      [ ]         STREAM     CONNECTED     25842    @/tmp/dbus-N2Yp7VZ9Aj
unix  3      [ ]         STREAM     CONNECTED     25189    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     23621    @/tmp/dbus-N2Yp7VZ9Aj
unix  3      [ ]         STREAM     CONNECTED     30979    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     25335
unix  3      [ ]         STREAM     CONNECTED     23771
unix  3      [ ]         STREAM     CONNECTED     25841
unix  3      [ ]         STREAM     CONNECTED     25196    /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     30973
unix  2      [ ]         DGRAM                    14468
unix  3      [ ]         STREAM     CONNECTED     25334    @/tmp/dbus-N2Yp7VZ9Aj
unix  3      [ ]         STREAM     CONNECTED     25198    @/tmp/dbus-N2Yp7VZ9Aj
unix  3      [ ]         STREAM     CONNECTED     23939    @/tmp/dbus-N2Yp7VZ9Aj
unix  3      [ ]         STREAM     CONNECTED     32078
unix  3      [ ]         STREAM     CONNECTED     25127
unix  3      [ ]         STREAM     CONNECTED     25333
unix  3      [ ]         STREAM     CONNECTED     25190    /run/systemd/journal/stdout
unix  3      [ ]         DGRAM                    21924
unix  3      [ ]         STREAM     CONNECTED     14333
unix  3      [ ]         STREAM     CONNECTED     32079    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     25341    /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     23769    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     29914    @/tmp/dbus-N2Yp7VZ9Aj
unix  3      [ ]         STREAM     CONNECTED     25195
unix  3      [ ]         STREAM     CONNECTED     24004
unix  3      [ ]         STREAM     CONNECTED     23925
unix  3      [ ]         STREAM     CONNECTED     14476
unix  3      [ ]         STREAM     CONNECTED     25331
unix  3      [ ]         STREAM     CONNECTED     29913
unix  3      [ ]         STREAM     CONNECTED     25188
unix  3      [ ]         STREAM     CONNECTED     24031
unix  3      [ ]         STREAM     CONNECTED     14498    /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     25332    /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     23421
unix  3      [ ]         DGRAM                    21923
unix  3      [ ]         STREAM     CONNECTED     14448    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     25340
unix  2      [ ]         DGRAM                    16377
unix  3      [ ]         STREAM     CONNECTED     25197
unix  3      [ ]         STREAM     CONNECTED     23685    @/tmp/dbus-N2Yp7VZ9Aj
unix  3      [ ]         STREAM     CONNECTED     23420
unix  3      [ ]         STREAM     CONNECTED     26332    /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     25336    @/tmp/dbus-N2Yp7VZ9Aj
unix  3      [ ]         STREAM     CONNECTED     24878
unix  3      [ ]         STREAM     CONNECTED     23985    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     16498
unix  3      [ ]         STREAM     CONNECTED     14560    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     25209
unix  3      [ ]         STREAM     CONNECTED     25228    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     24315
unix  3      [ ]         STREAM     CONNECTED     24884    /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     24098
unix  3      [ ]         STREAM     CONNECTED     23984
unix  3      [ ]         STREAM     CONNECTING    0        /var/run/salt/minion/minion_event_09b2048045_pub.ipc
unix  3      [ ]         STREAM     CONNECTED     14557
unix  3      [ ]         STREAM     CONNECTED     25211    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     24302    /run/user/1000/pulse/native
unix  3      [ ]         STREAM     CONNECTED     24881    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     24651
unix  3      [ ]         STREAM     CONNECTED     24100
unix  3      [ ]         STREAM     CONNECTED     25212    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     24307    @/tmp/dbus-bHXwLOvrQF
unix  2      [ ]         DGRAM                    18174
unix  3      [ ]         STREAM     CONNECTED     26672    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     24883
unix  3      [ ]         STREAM     CONNECTED     24099    @/tmp/dbus-N2Yp7VZ9Aj
unix  3      [ ]         STREAM     CONNECTED     23989    @/tmp/dbus-N2Yp7VZ9Aj
unix  2      [ ]         DGRAM                    17655
unix  3      [ ]         STREAM     CONNECTED     25277    @/tmp/dbus-N2Yp7VZ9Aj
unix  3      [ ]         STREAM     CONNECTED     24301
unix  3      [ ]         STREAM     CONNECTED     24109    /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     25102    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     24131    @/tmp/dbus-N2Yp7VZ9Aj
unix  3      [ ]         STREAM     CONNECTED     23982
unix  2      [ ]         DGRAM                    16512
unix  3      [ ]         STREAM     CONNECTED     15415    /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     25210
unix  2      [ ]         DGRAM                    16024
unix  3      [ ]         STREAM     CONNECTED     32091
unix  3      [ ]         STREAM     CONNECTED     26671
unix  3      [ ]         STREAM     CONNECTED     25101
unix  3      [ ]         STREAM     CONNECTED     24130
unix  3      [ ]         STREAM     CONNECTED     23988
unix  3      [ ]         STREAM     CONNECTED     25821    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     25276
unix  2      [ ]         DGRAM                    20959
unix  3      [ ]         STREAM     CONNECTED     26678
unix  3      [ ]         STREAM     CONNECTED     24879    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     23983    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     16499    /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     25289
unix  3      [ ]         STREAM     CONNECTED     24108
unix  3      [ ]         STREAM     CONNECTED     26679    @/tmp/dbus-bHXwLOvrQF
unix  3      [ ]         STREAM     CONNECTED     24880
unix  3      [ ]         STREAM     CONNECTED     24653    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     24101    @/tmp/dbus-N2Yp7VZ9Aj
unix  2      [ ]         DGRAM                    14451
unix  3      [ ]         STREAM     CONNECTED     25825
unix  3      [ ]         STREAM     CONNECTED     24306
unix  3      [ ]         STREAM     CONNECTED     22713    /run/systemd/journal/stdout
unix  3      [ ]         DGRAM                    11778
unix  3      [ ]         STREAM     CONNECTED     23933    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     23240    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     24181
unix  3      [ ]         STREAM     CONNECTED     23212
unix  3      [ ]         STREAM     CONNECTED     15693    /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     25806
unix  3      [ ]         STREAM     CONNECTED     25290
unix  3      [ ]         STREAM     CONNECTED     25232
unix  3      [ ]         STREAM     CONNECTED     25017    /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     23936
unix  2      [ ]         DGRAM                    11543
unix  3      [ ]         STREAM     CONNECTED     26335    @/dbus-vfs-daemon/socket-zzJ5jUDl
unix  3      [ ]         STREAM     CONNECTED     22702
unix  3      [ ]         STREAM     CONNECTED     20177
unix  3      [ ]         STREAM     CONNECTED     18044    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     23926    @/tmp/dbus-bHXwLOvrQF
unix  3      [ ]         STREAM     CONNECTED     17624    /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     15441
unix  3      [ ]         STREAM     CONNECTED     24216
unix  3      [ ]         STREAM     CONNECTED     23765
unix  3      [ ]         STREAM     CONNECTED     14956    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     25803    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     25308
unix  3      [ ]         STREAM     CONNECTED     25281
unix  3      [ ]         STREAM     CONNECTED     25016
unix  3      [ ]         STREAM     CONNECTED     23891    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     23477    @/com/ubuntu/upstart-session/1000/2153
unix  3      [ ]         STREAM     CONNECTED     23463
unix  3      [ ]         STREAM     CONNECTED     11536
unix  3      [ ]         STREAM     CONNECTED     23929
unix  2      [ ]         DGRAM                    31473
unix  3      [ ]         STREAM     CONNECTED     24283
unix  3      [ ]         STREAM     CONNECTED     23768
unix  3      [ ]         STREAM     CONNECTED     14945
unix  3      [ ]         STREAM     CONNECTED     25310
unix  3      [ ]         STREAM     CONNECTED     25233    @/tmp/dbus-N2Yp7VZ9Aj
unix  3      [ ]         STREAM     CONNECTED     25156    /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     24286
unix  3      [ ]         STREAM     CONNECTED     23890
unix  2      [ ]         DGRAM                    11546
unix  3      [ ]         STREAM     CONNECTED     23823
unix  3      [ ]         STREAM     CONNECTED     19788
unix  3      [ ]         STREAM     CONNECTED     23932
unix  3      [ ]         STREAM     CONNECTED     23222
unix  3      [ ]         STREAM     CONNECTED     14450    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     25309    @/tmp/ibus/dbus-169NW85k
unix  3      [ ]         STREAM     CONNECTED     25282    /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     25155
unix  3      [ ]         STREAM     CONNECTED     24253    @/tmp/dbus-N2Yp7VZ9Aj
unix  3      [ ]         STREAM     CONNECTED     23937    /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     22564
unix  3      [ ]         STREAM     CONNECTED     24005    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     15437
unix  3      [ ]         STREAM     CONNECTED     24211
unix  3      [ ]         STREAM     CONNECTED     23766    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     25311    @/tmp/dbus-N2Yp7VZ9Aj
unix  3      [ ]         STREAM     CONNECTED     25261    @/tmp/dbus-bHXwLOvrQF
unix  3      [ ]         STREAM     CONNECTED     25152
unix  3      [ ]         STREAM     CONNECTED     24252
unix  3      [ ]         STREAM     CONNECTED     24106
unix  3      [ ]         STREAM     CONNECTED     22565    /var/run/dbus/system_bus_socket
unix  3      [ ]         DGRAM                    11777
unix  3      [ ]         STREAM     CONNECTED     17623
unix  3      [ ]         STREAM     CONNECTED     24183    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     23213    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     25306    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     25260
unix  3      [ ]         STREAM     CONNECTED     25153    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     24504    @/tmp/ibus/dbus-169NW85k
unix  3      [ ]         STREAM     CONNECTED     24288    /run/user/1000/pulse/native
unix  3      [ ]         STREAM     CONNECTED     24107    /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     23471
unix  2      [ ]         DGRAM                    18184
unix  3      [ ]         STREAM     CONNECTED     25818
unix  3      [ ]         STREAM     CONNECTED     23913    @/tmp/dbus-N2Yp7VZ9Aj
unix  3      [ ]         STREAM     CONNECTED     17712
unix  3      [ ]         STREAM     CONNECTED     15439    /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     14955    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     25826    /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     25307    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     25265    /var/run/dbus/system_bus_socket
unix  2      [ ]         DGRAM                    25008
unix  3      [ ]         STREAM     CONNECTED     24217    @/tmp/dbus-N2Yp7VZ9Aj
unix  3      [ ]         STREAM     CONNECTED     26334
unix  3      [ ]         STREAM     CONNECTED     23930    @/tmp/dbus-bHXwLOvrQF
unix  3      [ ]         STREAM     CONNECTED     23612    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     20178    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     23912
unix  3      [ ]         STREAM     CONNECTED     23772    @/tmp/dbus-N2Yp7VZ9Aj
unix  3      [ ]         STREAM     CONNECTED     15445    /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     32075    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     24212    @/tmp/dbus-N2Yp7VZ9Aj
unix  3      [ ]         STREAM     CONNECTED     25439
unix  3      [ ]         STREAM     CONNECTED     25159
unix  3      [ ]         STREAM     CONNECTED     24503
unix  3      [ ]         STREAM     CONNECTED     11567    /run/systemd/journal/stdout
unix  2      [ ]         DGRAM                    26431
unix  3      [ ]         STREAM     CONNECTED     23763    /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     23580
unix  3      [ ]         STREAM     CONNECTED     20787
unix  3      [ ]         STREAM     CONNECTED     15231    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     25375
unix  3      [ ]         STREAM     CONNECTED     24292
unix  3      [ ]         STREAM     CONNECTED     24257    @/tmp/dbus-bHXwLOvrQF
unix  2      [ ]         STREAM     CONNECTED     31014
unix  3      [ ]         STREAM     CONNECTED     24073
unix  3      [ ]         STREAM     CONNECTED     23737
unix  3      [ ]         STREAM     CONNECTED     26346    @/dbus-vfs-daemon/socket-lITofiyy
unix  3      [ ]         STREAM     CONNECTED     20786
unix  3      [ ]         STREAM     CONNECTED     25376    @/tmp/dbus-N2Yp7VZ9Aj
unix  3      [ ]         STREAM     CONNECTED     24862    @/tmp/dbus-N2Yp7VZ9Aj
unix  2      [ ]         STREAM     CONNECTED     24318
unix  3      [ ]         STREAM     CONNECTED     24287    /run/user/1000/pulse/native
unix  3      [ ]         STREAM     CONNECTED     24090    @/tmp/dbus-N2Yp7VZ9Aj
unix  3      [ ]         STREAM     CONNECTED     16032    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     24074    @/tmp/dbus-N2Yp7VZ9Aj
unix  3      [ ]         STREAM     CONNECTED     23740    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     23642    @/tmp/dbus-N2Yp7VZ9Aj
unix  3      [ ]         STREAM     CONNECTED     23620
unix  2      [ ]         DGRAM                    11466
unix  3      [ ]         STREAM     CONNECTED     15429
unix  3      [ ]         STREAM     CONNECTED     23749    @/tmp/ibus/dbus-169NW85k
unix  2      [ ]         DGRAM                    23057
unix  3      [ ]         STREAM     CONNECTED     15009
unix  3      [ ]         STREAM     CONNECTED     25352
unix  3      [ ]         STREAM     CONNECTED     24869    @/tmp/dbus-bHXwLOvrQF
unix  3      [ ]         STREAM     CONNECTED     24289
unix  3      [ ]         STREAM     CONNECTED     24069    /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     23739
unix  3      [ ]         STREAM     CONNECTED     22903    /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     23581    @/tmp/dbus-N2Yp7VZ9Aj
unix  3      [ ]         STREAM     CONNECTED     23750
unix  3      [ ]         STREAM     CONNECTED     25353    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     24871    @/tmp/dbus-bHXwLOvrQF
unix  3      [ ]         STREAM     CONNECTED     24293    @/tmp/dbus-N2Yp7VZ9Aj
unix  3      [ ]         STREAM     CONNECTED     24280    /var/run/dbus/system_bus_socket
unix  2      [ ]         DGRAM                    15409
unix  2      [ ]         DGRAM                    23078
unix  3      [ ]         STREAM     CONNECTED     26530
unix  3      [ ]         STREAM     CONNECTED     23732
unix  3      [ ]         STREAM     CONNECTED     23733    @/tmp/dbus-bHXwLOvrQF
unix  3      [ ]         STREAM     CONNECTED     15883    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     14389
unix  3      [ ]         STREAM     CONNECTED     23758
unix  3      [ ]         STREAM     CONNECTED     20081
unix  3      [ ]         STREAM     CONNECTED     24868
unix  3      [ ]         STREAM     CONNECTED     24290    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     24279
unix  3      [ ]         STREAM     CONNECTED     23239
unix  3      [ ]         STREAM     CONNECTED     24075
unix  3      [ ]         STREAM     CONNECTED     23738    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     23607    @/tmp/dbus-N2Yp7VZ9Aj
unix  3      [ ]         STREAM     CONNECTED     15430
unix  3      [ ]         STREAM     CONNECTED     23779
unix  3      [ ]         STREAM     CONNECTED     25355
unix  3      [ ]         STREAM     CONNECTED     24872
unix  2      [ ]         DGRAM                    24262
unix  3      [ ]         STREAM     CONNECTED     23778    @/tmp/dbus-bHXwLOvrQF
unix  3      [ ]         STREAM     CONNECTED     23223    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     22379
unix  3      [ ]         STREAM     CONNECTED     24068
unix  3      [ ]         STREAM     CONNECTED     23760
unix  3      [ ]         STREAM     CONNECTED     22902
unix  3      [ ]         STREAM     CONNECTED     26531
unix  3      [ ]         STREAM     CONNECTED     23606
unix  3      [ ]         STREAM     CONNECTED     23751    @/tmp/dbus-bHXwLOvrQF
unix  3      [ ]         STREAM     CONNECTED     20082    /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     15664
unix  3      [ ]         STREAM     CONNECTED     25819    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     24870
unix  3      [ ]         STREAM     CONNECTED     24316    /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     24089
unix  3      [ ]         STREAM     CONNECTED     16021
unix  3      [ ]         STREAM     CONNECTED     23762
unix  3      [ ]         STREAM     CONNECTED     23641
unix  3      [ ]         STREAM     CONNECTED     26345
unix  3      [ ]         STREAM     CONNECTED     15803
unix  3      [ ]         STREAM     CONNECTED     23780    @/tmp/ibus/dbus-169NW85k
unix  3      [ ]         STREAM     CONNECTED     15665    /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     25356    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     24873    @/tmp/dbus-N2Yp7VZ9Aj
unix  3      [ ]         STREAM     CONNECTED     24256
unix  3      [ ]         STREAM     CONNECTED     23777
unix  3      [ ]         STREAM     CONNECTED     24076    /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     23761    @/tmp/dbus-N2Yp7VZ9Aj
unix  2      [ ]         STREAM     CONNECTED     31200
unix  3      [ ]         STREAM     CONNECTED     24837
unix  3      [ ]         STREAM     CONNECTED     25179    @/tmp/dbus-N2Yp7VZ9Aj
unix  3      [ ]         STREAM     CONNECTED     26185    @/tmp/dbus-N2Yp7VZ9Aj
unix  3      [ ]         STREAM     CONNECTED     23374
unix  3      [ ]         STREAM     CONNECTED     25095    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     22032    /run/systemd/journal/stdout
unix  2      [ ]         DGRAM                    24831
unix  3      [ ]         STREAM     CONNECTED     15176
unix  3      [ ]         STREAM     CONNECTED     26675    @/tmp/dbus-N2Yp7VZ9Aj
unix  3      [ ]         STREAM     CONNECTED     26184
unix  3      [ ]         STREAM     CONNECTED     23567    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     22378
unix  3      [ ]         STREAM     CONNECTED     25087
unix  3      [ ]         STREAM     CONNECTED     23921
unix  3      [ ]         STREAM     CONNECTED     24834    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     25142    @/tmp/dbus-N2Yp7VZ9Aj
unix  3      [ ]         STREAM     CONNECTED     23501
unix  3      [ ]         STREAM     CONNECTED     25807    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     24833
unix  3      [ ]         STREAM     CONNECTED     23613
unix  3      [ ]         STREAM     CONNECTED     23575
unix  3      [ ]         STREAM     CONNECTED     23429
unix  3      [ ]         STREAM     CONNECTED     15692
unix  3      [ ]         STREAM     CONNECTED     25088    @/tmp/dbus-N2Yp7VZ9Aj
unix  3      [ ]         STREAM     CONNECTED     22011
unix  3      [ ]         STREAM     CONNECTED     31193    /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     25820
unix  3      [ ]         STREAM     CONNECTED     24838    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     23507    @/tmp/dbus-N2Yp7VZ9Aj
unix  3      [ ]         STREAM     CONNECTED     15234    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     14892
unix  3      [ ]         STREAM     CONNECTED     23727
unix  3      [ ]         STREAM     CONNECTED     26327    @/tmp/dbus-N2Yp7VZ9Aj
unix  3      [ ]         STREAM     CONNECTED     26292
unix  3      [ ]         STREAM     CONNECTED     23611
unix  3      [ ]         STREAM     CONNECTED     14679
unix  3      [ ]         STREAM     CONNECTED     25094
unix  3      [ ]         STREAM     CONNECTED     24674    @/tmp/.ICE-unix/2459
unix  3      [ ]         STREAM     CONNECTED     23506
unix  3      [ ]         STREAM     CONNECTED     20434
unix  3      [ ]         STREAM     CONNECTED     23614    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     26251    @/tmp/dbus-N2Yp7VZ9Aj
unix  3      [ ]         STREAM     CONNECTED     23570
unix  3      [ ]         STREAM     CONNECTED     23430    @/tmp/dbus-N2Yp7VZ9Aj
unix  3      [ ]         STREAM     CONNECTED     14680    /run/systemd/journal/stdout
unix  2      [ ]         DGRAM                    25053
unix  3      [ ]         STREAM     CONNECTED     24673
unix  3      [ ]         STREAM     CONNECTED     26326
unix  3      [ ]         STREAM     CONNECTED     26293    @/dbus-vfs-daemon/socket-1oBxY7YS
unix  3      [ ]         STREAM     CONNECTED     23571    @/tmp/dbus-N2Yp7VZ9Aj
unix  3      [ ]         STREAM     CONNECTED     23375    @/com/ubuntu/upstart-session/1000/2153
unix  3      [ ]         STREAM     CONNECTED     25178
unix  3      [ ]         STREAM     CONNECTED     23502    @/tmp/dbus-N2Yp7VZ9Aj
unix  3      [ ]         STREAM     CONNECTED     24861
unix  3      [ ]         STREAM     CONNECTED     25812    @/tmp/dbus-N2Yp7VZ9Aj
unix  3      [ ]         STREAM     CONNECTED     26674
unix  3      [ ]         STREAM     CONNECTED     26250
unix  3      [ ]         STREAM     CONNECTED     23566
unix  2      [ ]         DGRAM                    15684
unix  3      [ ]         STREAM     CONNECTED     32082
unix  3      [ ]         STREAM     CONNECTED     24860    @/tmp/dbus-bHXwLOvrQF
unix  3      [ ]         STREAM     CONNECTED     23938
unix  3      [ ]         STREAM     CONNECTED     23340
unix  3      [ ]         STREAM     CONNECTED     22373
unix  3      [ ]         STREAM     CONNECTED     25027
unix  3      [ ]         STREAM     CONNECTED     25391    @/tmp/dbus-bHXwLOvrQF
unix  3      [ ]         STREAM     CONNECTED     23819    @/tmp/dbus-N2Yp7VZ9Aj
unix  3      [ ]         STREAM     CONNECTED     25487    @/dbus-vfs-daemon/socket-PBrJUgWS
unix  3      [ ]         STREAM     CONNECTED     25263
unix  3      [ ]         STREAM     CONNECTED     23786    @/tmp/ibus/dbus-169NW85k
unix  3      [ ]         STREAM     CONNECTED     25796    @/tmp/dbus-N2Yp7VZ9Aj
unix  3      [ ]         STREAM     CONNECTED     24851    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     23476    @/com/ubuntu/upstart-session/1000/2153
unix  3      [ ]         STREAM     CONNECTED     23253
unix  3      [ ]         STREAM     CONNECTED     25103
unix  3      [ ]         STREAM     CONNECTED     25390
unix  3      [ ]         STREAM     CONNECTED     25490
unix  3      [ ]         STREAM     CONNECTED     24631
unix  3      [ ]         STREAM     CONNECTED     24850
unix  3      [ ]         STREAM     CONNECTED     22374
unix  3      [ ]         STREAM     CONNECTED     25108    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     25393
unix  3      [ ]         STREAM     CONNECTED     23784    @/tmp/dbus-bHXwLOvrQF
unix  3      [ ]         STREAM     CONNECTED     29917
unix  3      [ ]         STREAM     CONNECTED     24857
unix  3      [ ]         STREAM     CONNECTED     24143
unix  3      [ ]         STREAM     CONNECTED     23464    /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     25104    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     25440    /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     19636    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     23785
unix  3      [ ]         STREAM     CONNECTED     25802
unix  3      [ ]         STREAM     CONNECTED     24854    @/tmp/dbus-N2Yp7VZ9Aj
unix  3      [ ]         STREAM     CONNECTED     23818
unix  3      [ ]         STREAM     CONNECTED     23254    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     25146    @/tmp/dbus-bHXwLOvrQF
unix  3      [ ]         STREAM     CONNECTED     25394    @/dbus-vfs-daemon/socket-I0qLeqA6
unix  3      [ ]         STREAM     CONNECTED     25491    @/dbus-vfs-daemon/socket-2ORQs0l6
unix  2      [ ]         DGRAM                    24583
unix  3      [ ]         STREAM     CONNECTED     24858    @/tmp/dbus-N2Yp7VZ9Aj
unix  3      [ ]         STREAM     CONNECTED     24144    /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     23577
unix  3      [ ]         STREAM     CONNECTED     23468
unix  3      [ ]         STREAM     CONNECTED     14441
unix  3      [ ]         STREAM     CONNECTED     25379
unix  3      [ ]         STREAM     CONNECTED     14497    /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     24859
unix  3      [ ]         STREAM     CONNECTED     24840
unix  3      [ ]         STREAM     CONNECTED     23578    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     25107
unix  3      [ ]         STREAM     CONNECTED     25380    @/dbus-vfs-daemon/socket-7t2miy2M
unix  3      [ ]         STREAM     CONNECTED     19606
unix  3      [ ]         STREAM     CONNECTED     24652    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     23783
unix  3      [ ]         STREAM     CONNECTED     24853
unix  3      [ ]         STREAM     CONNECTED     24841    @/tmp/dbus-N2Yp7VZ9Aj
unix  3      [ ]         STREAM     CONNECTED     23341    /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     25028    /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     25811
unix  3      [ ]         STREAM     CONNECTED     25486
unix  3      [ ]         STREAM     CONNECTED     24650
unix  3      [ ]         STREAM     CONNECTED     25166
unix  3      [ ]         STREAM     CONNECTED     15414
unix  3      [ ]         STREAM     CONNECTED     24123
unix  3      [ ]         STREAM     CONNECTED     24172
unix  3      [ ]         STREAM     CONNECTED     25461    @/tmp/ibus/dbus-169NW85k
unix  3      [ ]         STREAM     CONNECTED     23759    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     25167    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     23462
unix  3      [ ]         STREAM     CONNECTED     24124    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     23773
unix  3      [ ]         STREAM     CONNECTED     24203    @/tmp/dbus-N2Yp7VZ9Aj
unix  3      [ ]         STREAM     CONNECTED     25453
unix  3      [ ]         STREAM     CONNECTED     15416
unix  3      [ ]         STREAM     CONNECTED     25168
unix  3      [ ]         STREAM     CONNECTED     23824    @/tmp/ibus/dbus-169NW85k
unix  3      [ ]         STREAM     CONNECTED     15292
unix  3      [ ]         STREAM     CONNECTED     24202
unix  3      [ ]         STREAM     CONNECTED     24173    /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     25447    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     22534    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     23457
unix  2      [ ]         DGRAM                    15385
unix  3      [ ]         STREAM     CONNECTED     24195    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     24180
unix  3      [ ]         STREAM     CONNECTED     25446
unix  3      [ ]         STREAM     CONNECTED     23051
unix  3      [ ]         STREAM     CONNECTED     25187
unix  3      [ ]         STREAM     CONNECTED     25145
unix  3      [ ]         STREAM     CONNECTED     33613    @/tmp/dbus-bHXwLOvrQF
unix  3      [ ]         STREAM     CONNECTED     24201    @/tmp/dbus-N2Yp7VZ9Aj
unix  3      [ ]         STREAM     CONNECTED     24147    @/tmp/dbus-N2Yp7VZ9Aj
unix  3      [ ]         STREAM     CONNECTED     25449    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     23065    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     15417    /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     25206
unix  3      [ ]         STREAM     CONNECTED     24200
unix  3      [ ]         STREAM     CONNECTED     24146
unix  3      [ ]         STREAM     CONNECTED     23684
unix  3      [ ]         STREAM     CONNECTED     25460
unix  3      [ ]         STREAM     CONNECTED     25169    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     23458    @/tmp/dbus-N2Yp7VZ9Aj
unix  3      [ ]         STREAM     CONNECTED     24194
unix  3      [ ]         STREAM     CONNECTED     24182    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     24127
unix  3      [ ]         STREAM     CONNECTED     25454    @/tmp/dbus-N2Yp7VZ9Aj
unix  3      [ ]         STREAM     CONNECTED     22533
unix  3      [ ]         STREAM     CONNECTED     25160    @/tmp/dbus-N2Yp7VZ9Aj
unix  3      [ ]         STREAM     CONNECTED     23473    @/com/ubuntu/upstart-session/1000/2153
unix  3      [ ]         STREAM     CONNECTED     15298    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     23774    @/tmp/dbus-N2Yp7VZ9Aj
unix  3      [ ]         STREAM     CONNECTED     33612
unix  3      [ ]         STREAM     CONNECTED     24128    /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     25448
unix  3      [ ]         STREAM     CONNECTED     16471    /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     24045    @/tmp/dbus-N2Yp7VZ9Aj
unix  3      [ ]         STREAM     CONNECTED     23952
unix  3      [ ]         STREAM     CONNECTED     20435    /var/run/docker/libcontainerd/docker-containerd.sock
unix  3      [ ]         STREAM     CONNECTED     31189    /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     26331
unix  3      [ ]         STREAM     CONNECTED     23731
unix  3      [ ]         STREAM     CONNECTED     16470
unix  3      [ ]         STREAM     CONNECTED     32092    @/tmp/ibus/dbus-169NW85k
unix  3      [ ]         STREAM     CONNECTED     24044
unix  3      [ ]         STREAM     CONNECTED     23955
unix  3      [ ]         STREAM     CONNECTED     22734
unix  3      [ ]         STREAM     CONNECTED     32083    @/tmp/dbus-N2Yp7VZ9Aj
unix  2      [ ]         STREAM     CONNECTED     22360
unix  2      [ ]         DGRAM                    19938
unix  3      [ ]         STREAM     CONNECTED     33605
unix  3      [ ]         STREAM     CONNECTED     14280    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     24050
unix  3      [ ]         STREAM     CONNECTED     23953    @/tmp/dbus-N2Yp7VZ9Aj
unix  3      [ ]         STREAM     CONNECTED     31192
unix  3      [ ]         STREAM     CONNECTED     25151    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     14170
unix  3      [ ]         STREAM     CONNECTED     32073    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     24048
unix  3      [ ]         STREAM     CONNECTED     23949
unix  3      [ ]         STREAM     CONNECTED     23748
unix  3      [ ]         STREAM     CONNECTED     19789    /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     33601
unix  3      [ ]         STREAM     CONNECTED     24052
unix  3      [ ]         STREAM     CONNECTED     23950    @/tmp/dbus-N2Yp7VZ9Aj
unix  2      [ ]         DGRAM                    14486
unix  3      [ ]         STREAM     CONNECTED     23644    @/tmp/dbus-N2Yp7VZ9Aj
unix  3      [ ]         STREAM     CONNECTED     32087    @/tmp/dbus-bHXwLOvrQF
unix  3      [ ]         STREAM     CONNECTED     32072
unix  3      [ ]         STREAM     CONNECTED     24049
unix  3      [ ]         STREAM     CONNECTED     24039    @/tmp/dbus-bHXwLOvrQF
unix  3      [ ]         STREAM     CONNECTED     31188
unix  3      [ ]         STREAM     CONNECTED     29918    /var/run/dbus/system_bus_socket
unix  2      [ ]         STREAM     CONNECTED     26276
unix  3      [ ]         STREAM     CONNECTED     25795
unix  2      [ ]         DGRAM                    15694
unix  3      [ ]         STREAM     CONNECTED     14496
unix  3      [ ]         STREAM     CONNECTED     33606    @/tmp/dbus-N2Yp7VZ9Aj
unix  3      [ ]         STREAM     CONNECTED     25150
unix  3      [ ]         STREAM     CONNECTED     23643
unix  3      [ ]         STREAM     CONNECTED     24053    @/tmp/dbus-N2Yp7VZ9Aj
unix  3      [ ]         STREAM     CONNECTED     23956    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     17895
unix  3      [ ]         STREAM     CONNECTED     24032    @/tmp/ibus/dbus-169NW85k
unix  3      [ ]         STREAM     CONNECTED     23576    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     32086
unix  3      [ ]         STREAM     CONNECTED     32074
unix  3      [ ]         STREAM     CONNECTED     24051
unix  3      [ ]         STREAM     CONNECTED     24038
unix  3      [ ]         STREAM     CONNECTED     22735    /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     24632    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     23922    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     14495
unix  3      [ ]         STREAM     CONNECTED     33602    @/tmp/.X11-unix/X0
----end----

Attempting to send file /bin/bash at Mon Jul 24 13:04:24 PDT 2017
Attempting to send file /bin/false at Mon Jul 24 13:04:37 PDT 2017
```

```sh
u64server@ubuntu64server:~/cases/2017-7-24$ ll
total 1056
drwxrwxr-x 2 u64server u64server    4096 Jul 24 13:04 ./
drwxrwxr-x 3 u64server u64server    4096 Jul 24 13:03 ../
-rw-rw-r-- 1 u64server u64server 1037528 Jul 24 13:04 bash
-rw-rw-r-- 1 u64server u64server   27280 Jul 24 13:04 false
-rw-rw-r-- 1 u64server u64server     133 Jul 24 13:04 log.txt
u64server@ubuntu64server:~/cases/2017-7-24$
```
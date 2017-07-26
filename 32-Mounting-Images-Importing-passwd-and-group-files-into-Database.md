#### 32. Mounting Images: Importing passwd and group files into Database

- Copy over the ```passwd``` and ```groups``` into ```/tmp/```

```sh
u64@u64-VirtualBox:~$ cp /etc/passwd /tmp/
```

```sh
u64@u64-VirtualBox:~$ cp /usr/bin/groups /tmp/
```

```sh
u64@u64-VirtualBox:~$ ls /tmp/passwd
/tmp/passwd
u64@u64-VirtualBox:~$
```

```sh
u64@u64-VirtualBox:~$ ls /tmp/groups
/tmp/groups
u64@u64-VirtualBox:~$
```

- Login to ```mysql``` and switch to ```case-2015-3-9```

```sh
u64@u64-VirtualBox:~$ mysql -u root -p
Enter password:
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 9
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
mysql>
```

- Create table ```users```

```sh
mysql> create table users (
    ->    username varchar(255) not null,
    ->    passwordHash varchar(255) not null,
    ->    uid int not null,
    ->    gid int not null,
    ->    userInfo varchar(255) not null,
    ->    homeDir varchar(255) not null,
    ->    shell varchar(2048) not null,
    ->    primary key (username)
    ->    );
Query OK, 0 rows affected (0.02 sec)

mysql>
```

- Import ```passwd``` file

```sh
mysql> load data local infile '/tmp/passwd'
    ->    into table users
    ->    fields terminated by ':'
    ->    enclosed by '"'
    ->    lines terminated by '\n';
Query OK, 42 rows affected (0.00 sec)
Records: 42  Deleted: 0  Skipped: 0  Warnings: 0

mysql>
```

- Query

```sh
mysql> select * from users;
+-------------------+--------------+-------+-------+------------------------------------+----------------------------+-------------------+
| username          | passwordHash | uid   | gid   | userInfo                           | homeDir                    | shell             |
+-------------------+--------------+-------+-------+------------------------------------+----------------------------+-------------------+
| avahi             | x            |   111 |   120 | Avahi mDNS daemon,,,               | /var/run/avahi-daemon      | /bin/false        |
| avahi-autoipd     | x            |   110 |   119 | Avahi autoip daemon,,,             | /var/lib/avahi-autoipd     | /bin/false        |
| backup            | x            |    34 |    34 | backup                             | /var/backups               | /usr/sbin/nologin |
| bin               | x            |     2 |     2 | bin                                | /bin                       | /usr/sbin/nologin |
| colord            | x            |   113 |   123 | colord colour management daemon,,, | /var/lib/colord            | /bin/false        |
| daemon            | x            |     1 |     1 | daemon                             | /usr/sbin                  | /usr/sbin/nologin |
| dnsmasq           | x            |   112 | 65534 | dnsmasq,,,                         | /var/lib/misc              | /bin/false        |
| games             | x            |     5 |    60 | games                              | /usr/games                 | /usr/sbin/nologin |
| gnats             | x            |    41 |    41 | Gnats Bug-Reporting System (admin) | /var/lib/gnats             | /usr/sbin/nologin |
| hplip             | x            |   115 |     7 | HPLIP system user,,,               | /var/run/hplip             | /bin/false        |
| irc               | x            |    39 |    39 | ircd                               | /var/run/ircd              | /usr/sbin/nologin |
| kernoops          | x            |   116 | 65534 | Kernel Oops Tracking Daemon,,,     | /                          | /bin/false        |
| lightdm           | x            |   108 |   114 | Light Display Manager              | /var/lib/lightdm           | /bin/false        |
| list              | x            |    38 |    38 | Mailing List Manager               | /var/list                  | /usr/sbin/nologin |
| lp                | x            |     7 |     7 | lp                                 | /var/spool/lpd             | /usr/sbin/nologin |
| mail              | x            |     8 |     8 | mail                               | /var/mail                  | /usr/sbin/nologin |
| man               | x            |     6 |    12 | man                                | /var/cache/man             | /usr/sbin/nologin |
| messagebus        | x            |   106 |   110 |                                    | /var/run/dbus              | /bin/false        |
| mysql             | x            |   122 |   129 | MySQL Server,,,                    | /nonexistent               | /bin/false        |
| news              | x            |     9 |     9 | news                               | /var/spool/news            | /usr/sbin/nologin |
| nobody            | x            | 65534 | 65534 | nobody                             | /nonexistent               | /usr/sbin/nologin |
| proxy             | x            |    13 |    13 | proxy                              | /bin                       | /usr/sbin/nologin |
| pulse             | x            |   117 |   124 | PulseAudio daemon,,,               | /var/run/pulse             | /bin/false        |
| root              | x            |     0 |     0 | root                               | /root                      | /bin/bash         |
| rtkit             | x            |   118 |   126 | RealtimeKit,,,                     | /proc                      | /bin/false        |
| saned             | x            |   119 |   127 |                                    | /var/lib/saned             | /bin/false        |
| speech-dispatcher | x            |   114 |    29 | Speech Dispatcher,,,               | /var/run/speech-dispatcher | /bin/false        |
| sshd              | x            |   121 | 65534 |                                    | /var/run/sshd              | /usr/sbin/nologin |
| sync              | x            |     4 | 65534 | sync                               | /bin                       | /bin/sync         |
| sys               | x            |     3 |     3 | sys                                | /dev                       | /usr/sbin/nologin |
| syslog            | x            |   104 |   108 |                                    | /home/syslog               | /bin/false        |
| systemd-bus-proxy | x            |   103 |   105 | systemd Bus Proxy,,,               | /run/systemd               | /bin/false        |
| systemd-network   | x            |   101 |   103 | systemd Network Management,,,      | /run/systemd/netif         | /bin/false        |
| systemd-resolve   | x            |   102 |   104 | systemd Resolver,,,                | /run/systemd/resolve       | /bin/false        |
| systemd-timesync  | x            |   100 |   102 | systemd Time Synchronization,,,    | /run/systemd               | /bin/false        |
| u64               | x            |  1000 |  1000 | u64,,,                             | /home/u64                  | /bin/bash         |
| usbmux            | x            |   120 |    46 | usbmux daemon,,,                   | /var/lib/usbmux            | /bin/false        |
| uucp              | x            |    10 |    10 | uucp                               | /var/spool/uucp            | /usr/sbin/nologin |
| uuidd             | x            |   107 |   111 |                                    | /run/uuidd                 | /bin/false        |
| whoopsie          | x            |   109 |   116 |                                    | /nonexistent               | /bin/false        |
| www-data          | x            |    33 |    33 | www-data                           | /var/www                   | /usr/sbin/nologin |
| _apt              | x            |   105 | 65534 |                                    | /nonexistent               | /bin/false        |
+-------------------+--------------+-------+-------+------------------------------------+----------------------------+-------------------+
42 rows in set (0.00 sec)

mysql>
```

- Create table ```groups```

```sh
mysql> create table groups (
    ->    groupname varchar(255) not null,
    ->    passwordHash varchar(255) not null,
    ->    gid int not null,
    ->    userlist varchar(2048)
    ->    );
Query OK, 0 rows affected (0.02 sec)

mysql>
```

- Import ```groups``` file

```sh
mysql> load data local infile '/tmp/groups'
    ->    into table groups
    ->    fields terminated by ':'
    ->    enclosed by '"'
    ->    lines terminated by '\n';
Query OK, 126 rows affected, 382 warnings (0.01 sec)
Records: 126  Deleted: 0  Skipped: 0  Warnings: 382

mysql>
```

- Query

```sh
mysql> select accessdate, accesstime, filename, permissions, username from files, users where files.userid=users.uid order by accessdate, accesstime desc;
+------------+------------+------------------------------------------------------------------------------------------------------------------------------------+-------------+-------------------+
| accessdate | accesstime | filename                                                                                                                           | permissions | username          |
+------------+------------+------------------------------------------------------------------------------------------------------------------------------------+-------------+-------------------+
| 1994-09-01 | 13:20:02   | ./usr/share/doc/cron/FEATURES                                                                                                      |         644 | root              |
| 1994-09-01 | 13:16:47   | ./usr/share/doc/cron/THANKS                                                                                                        |         644 | root              |
| 1996-06-11 | 15:24:48   | ./usr/share/doc/time/NEWS.gz                                                                                                       |         644 | root              |
| 1996-06-12 | 10:35:13   | ./usr/share/doc/time/AUTHORS                                                                                                       |         644 | root              |
| 1996-07-28 | 15:15:21   | ./usr/share/doc/mawk/ACKNOWLEDGMENT                                                                                                |         644 | root              |
| 1996-09-17 | 18:23:31   | ./usr/share/doc/mawk/README                                                                                                        |         644 | root              |
| 1997-03-10 | 12:10:01   | ./usr/share/doc/lsof/examples/xusers.awk                                                                                           |         755 | root              |
| 1997-03-21 | 10:27:22   | ./usr/share/doc/libwrap0/README.gz                                                                                                 |         644 | root              |
| 1997-06-08 | 18:29:57   | ./usr/share/doc/telnet/BUGS                                                                                                        |         644 | root              |
| 1997-09-23 | 07:32:42   | ./usr/share/doc/lsof/examples/list_fields.awk.gz                                                                                   |         644 | root              |
| 1997-09-23 | 00:02:29   | ./usr/share/doc/ftp/BUGS                                                                                                           |         644 | root              |
| 1998-11-22 | 16:30:27   | ./usr/share/doc/rsync/tech_report.tex.gz                                                                                           |         644 | root              |
| 1999-02-17 | 13:13:42   | ./usr/share/doc/bash/INTRO.gz                                                                                                      |         644 | root              |
| 1999-04-18 | 12:36:15   | ./usr/share/doc/net-tools/README.ipv6                                                                                              |         644 | root              |
| 1999-04-21 | 10:37:42   | ./usr/share/doc/net-tools/TODO                                                                                                     |         644 | root              |
| 1999-07-23 | 07:09:36   | ./usr/share/doc/libreadline5/USAGE                                                                                                 |         644 | root              |
| 1999-07-23 | 07:09:36   | ./usr/share/doc/libreadline6/USAGE                                                                                                 |         644 | root              |
| 1999-08-16 | 16:10:58   | ./usr/share/doc/python-pam/examples/pamexample.c                                                                                   |         644 | root              |
| 1999-08-16 | 16:10:58   | ./usr/share/doc/python-pam/README                                                                                                  |         644 | root              |
| 1999-08-16 | 16:10:58   | ./usr/share/doc/python-pam/AUTHORS                                                                                                 |         644 | root              |
| 1999-09-09 | 16:29:14   | ./usr/share/doc/isc-dhcp-common/api+protocol.gz                                                                                    |         644 | root              |
| 2000-01-19 | 17:37:24   | ./usr/share/doc/printer-driver-pnm2ppa/examples/test.ps.gz                                                                         |         644 | root              |
| 2000-02-12 | 19:04:25   | ./usr/share/doc/printer-driver-pnm2ppa/pl/AUTORZY                                                                                  |         644 | root              |
| 2000-02-12 | 19:04:25   | ./usr/share/doc/printer-driver-pnm2ppa/pl/KALIBRACJA                                                                               |         644 | root              |
```

```sh
mysql> select accessdate, accesstime, filename, permissions, username from files, users where files.userid=users.uid and files.userid!=0 order by accessdate, accesstime desc;
+------------+------------+-----------------------------------------------------------------------------------------------------------------+-------------+-------------------+
| accessdate | accesstime | filename                                                                                                        | permissions | username          |
+------------+------------+-----------------------------------------------------------------------------------------------------------------+-------------+-------------------+
| 2013-12-04 | 05:16:15   | ./var/spool/rsyslog                                                                                             |         700 | systemd-network   |
| 2014-02-18 | 22:12:07   | ./var/log/speech-dispatcher                                                                                     |         700 | avahi-autoipd     |
| 2015-02-18 | 11:39:10   | ./var/cache/man/fr/CACHEDIR.TAG                                                                                 |         644 | man               |
| 2015-02-18 | 11:39:10   | ./var/cache/man/lv/CACHEDIR.TAG                                                                                 |         644 | man               |
| 2015-02-18 | 11:39:10   | ./var/cache/man/bs/CACHEDIR.TAG                                                                                 |         644 | man               |
| 2015-02-18 | 11:39:10   | ./var/cache/man/mhr/CACHEDIR.TAG                                                                                |         644 | man               |
| 2015-02-18 | 11:39:10   | ./var/cache/man/ru/CACHEDIR.TAG                                                                                 |         644 | man               |
| 2015-02-18 | 11:39:10   | ./var/cache/man/bo/CACHEDIR.TAG                                                                                 |         644 | man               |
| 2015-02-18 | 11:39:10   | ./var/cache/man/pa/CACHEDIR.TAG                                                                                 |         644 | man               |
| 2015-02-18 | 11:39:10   | ./var/cache/man/hr/CACHEDIR.TAG                                                                                 |         644 | man               |
| 2015-02-18 | 11:39:10   | ./var/cache/man/pt_BR/CACHEDIR.TAG                                                                              |         644 | man               |
| 2015-02-18 | 11:39:10   | ./var/cache/man/en_GB/CACHEDIR.TAG                                                                              |         644 | man               |
| 2015-02-18 | 11:39:10   | ./var/cache/man/en_CA/CACHEDIR.TAG                                                                              |         644 | man               |
| 2015-02-18 | 11:39:10   | ./var/cache/man/en_AU/CACHEDIR.TAG                                                                              |         644 | man               |
| 2015-02-18 | 11:39:10   | ./var/cache/man/ar/CACHEDIR.TAG                                                                                 |         644 | man               |
| 2015-02-18 | 11:39:10   | ./var/cache/man/el/CACHEDIR.TAG                                                                                 |         644 | man               |
| 2015-02-18 | 11:39:10   | ./var/cache/man/lt/CACHEDIR.TAG                                                                                 |         644 | man               |
| 2015-02-18 | 11:39:10   | ./var/cache/man/tr/CACHEDIR.TAG                                                                                 |         644 | man               |
| 2015-02-18 | 11:39:10   | ./var/cache/man/se/CACHEDIR.TAG                                                                                 |         644 | man               |
| 2015-02-18 | 11:39:10   | ./var/cache/man/kk/CACHEDIR.TAG                                                                                 |         644 | man               |
| 2015-02-18 | 11:39:10   | ./var/cache/man/nb/CACHEDIR.TAG                                                                                 |         644 | man               |
| 2015-02-18 | 11:39:10   | ./var/cache/man/oc/CACHEDIR.TAG                                                                                 |         644 | man               |
| 2015-02-18 | 11:39:10   | ./var/cache/man/cy/CACHEDIR.TAG                                                                                 |         644 | man               |
| 2015-02-18 | 11:39:10   | ./var/cache/man/bn/CACHEDIR.TAG                                                                                 |         644 | man               |
| 2015-02-18 | 11:39:10   | ./var/cache/man/ml/CACHEDIR.TAG                                                                                 |         644 | man               |
| 2015-02-18 | 11:39:10   | ./var/cache/man/zh_HK/CACHEDIR.TAG                                                                              |         644 | man               |
| 2015-02-18 | 11:39:10   | ./var/cache/man/shn/CACHEDIR.TAG                                                                                |         644 | man               |
| 2015-02-18 | 11:39:10   | ./var/cache/man/fy/CACHEDIR.TAG                                                                                 |         644 | man               |
| 2015-02-18 | 11:39:10   | ./var/cache/man/be/CACHEDIR.TAG                                                                                 |         644 | man               |
| 2015-02-18 | 11:39:10   | ./var/cache/man/si/CACHEDIR.TAG                                                                                 |         644 | man               |
| 2015-02-18 | 11:39:10   | ./var/cache/man/bg/CACHEDIR.TAG                                                                                 |         644 | man               |
| 2015-02-18 | 11:39:10   | ./var/cache/man/gd/CACHEDIR.TAG                                                                                 |         644 | man               |
| 2015-02-18 | 11:39:10   | ./var/cache/man/eo/CACHEDIR.TAG                                                                                 |         644 | man               |
| 2015-02-18 | 11:39:10   | ./var/cache/man/my/CACHEDIR.TAG                                                                                 |         644 | man               |
| 2015-02-18 | 11:39:10   | ./var/cache/man/km/CACHEDIR.TAG                                                                                 |         644 | man               |
| 2015-02-18 | 11:39:10   | ./var/cache/man/fr.ISO8859-1/CACHEDIR.TAG                                                                       |         644 | man               |
| 2015-02-18 | 11:39:10   | ./var/cache/man/da/CACHEDIR.TAG                                                                                 |         644 | man               |
| 2015-02-18 | 11:39:10   | ./var/cache/man/fa/CACHEDIR.TAG                                                                                 |         644 | man               |
| 2015-02-18 | 11:39:10   | ./var/cache/man/io/CACHEDIR.TAG                                                                                 |         644 | man               |
| 2015-02-18 | 11:39:10   | ./var/cache/man/es/CACHEDIR.TAG                                                                                 |         644 | man               |
| 2015-02-18 | 11:39:10   | ./var/cache/man/fr.UTF-8/CACHEDIR.TAG                                                                           |         644 | man               |
| 2015-02-18 | 11:39:10   | ./var/cache/man/te/CACHEDIR.TAG                                                                                 |         644 | man               |
| 2015-02-18 | 11:39:10   | ./var/cache/man/he/CACHEDIR.TAG                                                                                 |         644 | man               |
| 2015-02-18 | 11:39:10   | ./var/cache/man/ca@valencia/CACHEDIR.TAG                                                                        |         644 | man               |
| 2015-02-18 | 11:39:10   | ./var/cache/man/ca/CACHEDIR.TAG                                                                                 |         644 | man               |
```
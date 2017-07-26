#### 31. Mounting Images: Creating a MySQL database with file metadata

- Install ```mysql-server```

```sh
u64@u64-VirtualBox:~/Desktop$ sudo apt-get install mysql-server
```

- Copy ```2015-3-9.csv``` into ```/tmp/```

```sh
u64@u64-VirtualBox:~/Desktop$ cp 2015-3-9.csv /tmp/
```

```sh
u64@u64-VirtualBox:~/Desktop$ ls /tmp/2015-3-9.csv
/tmp/2015-3-9.csv
u64@u64-VirtualBox:~/Desktop$
```

- Create databases ```case-2015-3-9```

```sh
u64@u64-VirtualBox:~/Desktop$ mysqladmin -u root -p create case-2015-3-9
Enter password:
u64@u64-VirtualBox:~/Desktop$
```

```sh
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

mysql>
```

```sh
u64@u64-VirtualBox:~/Desktop$ mysql -u root -p
Enter password:
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 6
Server version: 5.7.19-0ubuntu0.16.04.1 (Ubuntu)

Copyright (c) 2000, 2017, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> connect case-2015-3-9
Connection id:    7
Current database: case-2015-3-9

mysql>
```

- Create table ```files```

```sh
mysql> create table files (
    ->    AccessDate date not null,
    ->    AccessTime time not null,
    ->    ModifyDate date not null,
    ->    ModifyTime time not null,
    ->    CreateDate date not null,
    ->    CreateTime time not null,
    ->    Permissions smallint not null,
    ->    UserId smallint not null,
    ->    GroupId smallint not null,
    ->    FileSize bigint not null,
    ->    Filename varchar(2048) not null,
    ->    recno bigint not null auto_increment,
    ->    primary key(recno)
    -> );
Query OK, 0 rows affected (0.04 sec)

mysql>
```

- Load ```2015-3-9.csv``` into the table ```files```
	- [FIX](https://stackoverflow.com/questions/32737478/how-should-i-tackle-secure-file-priv-in-mysql)

```sh
mysql> load data local infile '/tmp/2015-3-9.csv'
    ->    into table files
    ->    fields terminated by ';'
    ->    enclosed by '"'
    ->    lines terminated by '\n'
    ->    ignore 1 rows
    ->    (@AccessDate, AccessTime, @ModifyDate, ModifyTime, @CreateDate, CreateTime,
    ->      Permissions, UserId, GroupId, FileSize, Filename)
    ->     set AccessDate=str_to_date(@AccessDate, "%m/%d/%Y"),
    ->         ModifyDate=str_to_date(@ModifyDate, "%m/%d/%Y"),
    ->         CreateDate=str_to_date(@CreateDate, "%m/%d/%Y");
Query OK, 184601 rows affected, 1 warning (1.72 sec)
Records: 184601  Deleted: 0  Skipped: 0  Warnings: 1

mysql>
```

- Query the ```table``` files

```sh
mysql> select * from files order by accessdate, accesstime desc;
+------------+------------+------------+------------+------------+------------+-------------+--------+---------+-----------+------------------------------------------------------------------------------------------------------------------------------------+--------+
| AccessDate | AccessTime | ModifyDate | ModifyTime | CreateDate | CreateTime | Permissions | UserId | GroupId | FileSize  | Filename                                                                                                                           | recno  |
+------------+------------+------------+------------+------------+------------+-------------+--------+---------+-----------+------------------------------------------------------------------------------------------------------------------------------------+--------+
| 1994-09-01 | 13:20:02   | 1994-09-01 | 13:20:02   | 2015-03-05 | 19:39:43   |         644 |      0 |       0 |      3960 | ./usr/share/doc/cron/FEATURES                                                                                                      |  12394 |
| 1994-09-01 | 13:16:47   | 1994-09-01 | 13:16:47   | 2015-03-05 | 19:39:43   |         644 |      0 |       0 |      1598 | ./usr/share/doc/cron/THANKS                                                                                                        |  12398 |
| 1996-06-11 | 15:24:48   | 1996-06-11 | 15:24:48   | 2015-03-05 | 19:39:45   |         644 |      0 |       0 |       445 | ./usr/share/doc/time/NEWS.gz                                                                                                       |  13927 |
| 1996-06-12 | 10:35:13   | 1996-06-12 | 10:35:13   | 2015-03-05 | 19:39:45   |         644 |      0 |       0 |       263 | ./usr/share/doc/time/AUTHORS                                                                                                       |  13926 |
| 1996-07-28 | 15:15:21   | 1996-07-28 | 15:15:21   | 2015-03-05 | 19:39:44   |         644 |      0 |       0 |      1520 | ./usr/share/doc/mawk/ACKNOWLEDGMENT                                                                                                |  12732 |
| 1996-09-17 | 18:23:31   | 1996-09-17 | 18:23:31   | 2015-03-05 | 19:39:44   |         644 |      0 |       0 |      2524 | ./usr/share/doc/mawk/README                                                                                                        |  12731 |
| 1997-03-10 | 12:10:01   | 1997-03-10 | 12:10:01   | 2015-03-05 | 19:39:44   |         755 |      0 |       0 |      3975 | ./usr/share/doc/lsof/examples/xusers.awk                                                                                           |  16529 |
| 1997-03-21 | 10:27:22   | 1997-03-21 | 10:27:22   | 2015-03-05 | 19:39:44   |         644 |      0 |       0 |     16694 | ./usr/share/doc/libwrap0/README.gz                                                                                                 |  11945 |
| 1997-06-08 | 18:29:57   | 1997-06-08 | 18:29:57   | 2015-03-05 | 19:39:45   |         644 |      0 |       0 |       876 | ./usr/share/doc/telnet/BUGS                                                                                                        |  14972 |
| 1997-09-23 | 07:32:42   | 1997-09-23 | 07:32:42   | 2015-03-05 | 19:39:44   |         644 |      0 |       0 |      1764 | ./usr/share/doc/lsof/examples/list_fields.awk.gz                                                                                   |  16523 |
| 1997-09-23 | 00:02:29   | 1997-09-23 | 00:02:29   | 2015-03-05 | 19:39:43   |         644 |      0 |       0 |        78 | ./usr/share/doc/ftp/BUGS                                                                                                           |  10415 |
| 1998-11-22 | 16:30:27   | 1998-11-22 | 16:30:27   | 2015-03-05 | 19:39:45   |         644 |      0 |       0 |      5527 | ./usr/share/doc/rsync/tech_report.tex.gz                                                                                           |  13332 |
| 1999-02-17 | 13:13:42   | 1999-02-17 | 13:13:42   | 2015-03-05 | 19:39:42   |         644 |      0 |       0 |      2921 | ./usr/share/doc/bash/INTRO.gz                                                                                                      |  16107 |
```
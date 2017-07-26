#### 40. Mounting Images: Examining Login Information

```sh
u64@u64-VirtualBox:~$ mysql -u root -p
Enter password:
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 12
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
mysql> show tables;
+-------------------------+
| Tables_in_case-2015-3-9 |
+-------------------------+
| files                   |
| groups                  |
| histories               |
| login_fails             |
| logins                  |
| logs                    |
| timeline                |
| users                   |
+-------------------------+
8 rows in set (0.00 sec)

mysql> select * from login_fails;
+----------+----------------+---------------------+---------------------+----------+--------------+-------+
| who_what | terminal_event | start               | stop                | elapsed  | ip           | recno |
+----------+----------------+---------------------+---------------------+----------+--------------+-------+
| lightdm  | ssh:notty      | 2015-03-09 18:33:55 | 2015-03-09 18:33:55 |  (00:00) | 192.168.56.1 |     1 |
|          |                | NULL                | NULL                |          |              |     2 |
| btmp beg | ns Mon Mar  9  | NULL                | NULL                |          |              |     3 |
+----------+----------------+---------------------+---------------------+----------+--------------+-------+
3 rows in set (0.00 sec)

mysql> desc logins;
+----------------+-------------+------+-----+---------+----------------+
| Field          | Type        | Null | Key | Default | Extra          |
+----------------+-------------+------+-----+---------+----------------+
| who_what       | varchar(8)  | YES  |     | NULL    |                |
| terminal_event | varchar(13) | YES  |     | NULL    |                |
| start          | datetime    | YES  |     | NULL    |                |
| stop           | datetime    | YES  |     | NULL    |                |
| elapsed        | varchar(12) | YES  |     | NULL    |                |
| ip             | varchar(15) | YES  |     | NULL    |                |
| recno          | bigint(20)  | NO   | PRI | NULL    | auto_increment |
+----------------+-------------+------+-----+---------+----------------+
7 rows in set (0.00 sec)

mysql> select who_what, terminal_event, start, stop, ip from logins order by recno;
+----------+----------------+---------------------+---------------------+--------------+
| who_what | terminal_event | start               | stop                | ip           |
+----------+----------------+---------------------+---------------------+--------------+
| john     | pts/12         | 2015-03-12 10:36:39 | NULL                | 0.0.0.0      |
| john     | :0             | 2015-03-12 10:36:06 | NULL                | 0.0.0.0      |
| runlevel | (to lvl 2)     | 2015-03-12 10:35:46 | NULL                | 0.0.0.0      |
| reboot   | system boot    | 2015-03-12 10:35:46 | NULL                | 0.0.0.0      |
| john     | pts/9          | 2015-03-11 07:10:27 | 2015-03-11 07:18:23 | 0.0.0.0      |
| john     | :0             | 2015-03-11 07:09:48 | NULL                | 0.0.0.0      |
| runlevel | (to lvl 2)     | 2015-03-11 07:09:33 | 2015-03-12 10:35:46 | 0.0.0.0      |
| reboot   | system boot    | 2015-03-11 07:09:33 | NULL                | 0.0.0.0      |
| shutdown | system down    | 2015-03-11 07:08:43 | 2015-03-11 07:09:33 | 0.0.0.0      |
| runlevel | (to lvl 0)     | 2015-03-11 07:08:40 | 2015-03-11 07:08:43 | 0.0.0.0      |
| john     | pts/11         | 2015-03-11 06:56:18 | 2015-03-11 07:08:19 | 0.0.0.0      |
| john     | :0             | 2015-03-11 06:55:46 | NULL                | 0.0.0.0      |
| runlevel | (to lvl 2)     | 2015-03-11 06:55:20 | 2015-03-11 07:08:40 | 0.0.0.0      |
| reboot   | system boot    | 2015-03-11 06:55:20 | 2015-03-11 07:08:40 | 0.0.0.0      |
| john     | pts/12         | 2015-03-09 18:49:10 | NULL                | 0.0.0.0      |
| john     | :0             | 2015-03-09 18:48:38 | NULL                | 0.0.0.0      |
| runlevel | (to lvl 2)     | 2015-03-09 18:48:01 | 2015-03-11 06:55:20 | 0.0.0.0      |
| reboot   | system boot    | 2015-03-09 18:48:01 | 2015-03-11 07:08:40 | 0.0.0.0      |
| johnn    | pts/25         | 2015-03-09 18:34:45 | 2015-03-09 18:38:50 | 192.168.56.1 |
| lightdm  | pts/25         | 2015-03-09 18:34:01 | 2015-03-09 18:34:36 | 192.168.56.1 |
| lightdm  | pts/25         | 2015-03-09 18:33:16 | 2015-03-09 18:33:16 | 192.168.56.1 |
| johnn    | pts/25         | 2015-03-09 18:29:39 | 2015-03-09 18:33:05 | 192.168.56.1 |
| john     | pts/23         | 2015-03-09 18:24:49 | 2015-03-09 18:44:23 | 192.168.56.1 |
| john     | pts/0          | 2015-03-09 18:10:45 | 2015-03-09 18:44:43 | 0.0.0.0      |
| john     | pts/0          | 2015-03-09 18:03:15 | 2015-03-09 18:08:11 | 0.0.0.0      |
| john     | :0             | 2015-03-09 17:59:56 | 2015-03-09 18:44:43 | 0.0.0.0      |
| runlevel | (to lvl 2)     | 2015-03-09 17:58:55 | 2015-03-09 18:48:01 | 0.0.0.0      |
| reboot   | system boot    | 2015-03-09 17:58:55 | 2015-03-11 07:08:40 | 0.0.0.0      |
| shutdown | system down    | 2015-03-08 17:51:50 | 2015-03-09 17:58:55 | 0.0.0.0      |
| runlevel | (to lvl 0)     | 2015-03-08 17:51:46 | 2015-03-08 17:51:50 | 0.0.0.0      |
| john     | pts/0          | 2015-03-08 17:42:33 | 2015-03-08 17:51:38 | 0.0.0.0      |
| john     | pts/13         | 2015-03-08 17:28:15 | 2015-03-08 17:40:06 | 0.0.0.0      |
| john     | :0             | 2015-03-08 17:27:43 | NULL                | 0.0.0.0      |
| runlevel | (to lvl 2)     | 2015-03-08 17:27:24 | 2015-03-08 17:51:46 | 0.0.0.0      |
| reboot   | system boot    | 2015-03-08 17:27:24 | 2015-03-08 17:51:46 | 0.0.0.0      |
| shutdown | system down    | 2015-03-06 18:33:02 | 2015-03-08 17:27:24 | 0.0.0.0      |
| runlevel | (to lvl 0)     | 2015-03-06 18:32:49 | 2015-03-06 18:33:02 | 0.0.0.0      |
| john     | pts/0          | 2015-03-06 18:25:04 | 2015-03-06 18:32:41 | 0.0.0.0      |
| john     | :0             | 2015-03-06 18:23:58 | NULL                | 0.0.0.0      |
| runlevel | (to lvl 2)     | 2015-03-06 18:23:13 | 2015-03-06 18:32:49 | 0.0.0.0      |
| reboot   | system boot    | 2015-03-06 18:23:13 | 2015-03-06 18:32:49 | 0.0.0.0      |
| shutdown | system down    | 2015-03-06 17:47:16 | 2015-03-06 18:23:13 | 0.0.0.0      |
| runlevel | (to lvl 0)     | 2015-03-06 17:47:13 | 2015-03-06 17:47:16 | 0.0.0.0      |
| john     | pts/9          | 2015-03-06 17:35:29 | 2015-03-06 17:47:07 | 0.0.0.0      |
| john     | :0             | 2015-03-06 17:34:33 | NULL                | 0.0.0.0      |
| runlevel | (to lvl 2)     | 2015-03-06 17:31:30 | 2015-03-06 17:47:13 | 0.0.0.0      |
| reboot   | system boot    | 2015-03-06 17:31:30 | 2015-03-06 17:47:13 | 0.0.0.0      |
| shutdown | system down    | 2015-03-06 17:30:38 | 2015-03-06 17:31:30 | 0.0.0.0      |
| runlevel | (to lvl 0)     | 2015-03-06 17:30:35 | 2015-03-06 17:30:38 | 0.0.0.0      |
| john     | pts/12         | 2015-03-06 17:23:44 | NULL                | 0.0.0.0      |
| john     | :0             | 2015-03-06 17:23:06 | NULL                | 0.0.0.0      |
| runlevel | (to lvl 2)     | 2015-03-06 17:19:39 | 2015-03-06 17:30:35 | 0.0.0.0      |
| reboot   | system boot    | 2015-03-06 17:19:39 | 2015-03-06 17:30:35 | 0.0.0.0      |
| shutdown | system down    | 2015-03-06 06:25:54 | 2015-03-06 17:19:39 | 0.0.0.0      |
| runlevel | (to lvl 0)     | 2015-03-06 06:25:52 | 2015-03-06 06:25:54 | 0.0.0.0      |
| john     | pts/12         | 2015-03-06 05:50:35 | NULL                | 0.0.0.0      |
| john     | :0             | 2015-03-06 05:50:03 | NULL                | 0.0.0.0      |
| runlevel | (to lvl 2)     | 2015-03-06 05:49:13 | 2015-03-06 06:25:52 | 0.0.0.0      |
| reboot   | system boot    | 2015-03-06 05:49:13 | 2015-03-06 06:25:52 | 0.0.0.0      |
| shutdown | system down    | 2015-03-05 20:12:23 | 2015-03-06 05:49:13 | 0.0.0.0      |
| runlevel | (to lvl 0)     | 2015-03-05 20:12:19 | 2015-03-05 20:12:23 | 0.0.0.0      |
| john     | pts/0          | 2015-03-05 20:00:36 | NULL                | 0.0.0.0      |
| john     | :0             | 2015-03-05 19:58:25 | NULL                | 0.0.0.0      |
| runlevel | (to lvl 2)     | 2015-03-05 19:58:08 | 2015-03-05 20:12:19 | 0.0.0.0      |
| reboot   | system boot    | 2015-03-05 19:58:08 | 2015-03-05 20:12:19 | 0.0.0.0      |
| shutdown | system down    | 2015-03-05 19:57:48 | 2015-03-05 19:58:08 | 0.0.0.0      |
| runlevel | (to lvl 6)     | 2015-03-05 19:57:44 | 2015-03-05 19:57:48 | 0.0.0.0      |
| john     | pts/11         | 2015-03-05 19:56:00 | 2015-03-05 19:57:28 | 0.0.0.0      |
| john     | pts/4          | 2015-03-05 19:53:28 | NULL                | 0.0.0.0      |
| john     | :0             | 2015-03-05 19:52:31 | NULL                | 0.0.0.0      |
| runlevel | (to lvl 2)     | 2015-03-05 19:52:03 | 2015-03-05 19:57:44 | 0.0.0.0      |
| reboot   | system boot    | 2015-03-05 19:52:03 | 2015-03-05 19:57:44 | 0.0.0.0      |
|          |                | NULL                | NULL                |              |
| wtmp beg | ns Thu Mar  5  | NULL                | NULL                |              |
+----------+----------------+---------------------+---------------------+--------------+
74 rows in set (0.00 sec)

mysql>
```
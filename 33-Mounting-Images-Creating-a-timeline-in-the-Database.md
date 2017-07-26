#### 33. Mounting Images: Creating a timeline in the Database

###### ```create-timeline.sh```

```sh
#!/bin/bash
# Simple shell script to create a timeline in the database.
#
# Developed for PentesterAcademy by
# Dr. Phil Polstra (@ppolstra)

usage () {
        echo "usage: $0 <database>"
        echo "Simple script to create a timeline in the database"
        exit 1
}

if [ $# -lt 1 ] ; then
   usage
fi

cat << EOF | mysql $1 -u root -p
create table timeline (
   Operation char(1),
   Date date not null,
   Time time not null,
   recno bigint not null
);


insert into timeline (Operation, Date, Time, recno)
   select "A", accessdate, accesstime, recno from files;
insert into timeline (Operation, Date, Time, recno)
   select "M", modifydate, modifytime, recno from files;
insert into timeline (Operation, Date, Time, recno)
   select "C", createdate, createtime, recno from files;

EOF
```

```sh
u64@u64-VirtualBox:~/Desktop$ ./create-timeline.sh case-2015-3-9
Enter password:
u64@u64-VirtualBox:~/Desktop$
```

###### ```print-timeline.sh```

```sh
#!/bin/bash
# Simple shell script to print a timeline.
#
# Developed for PentesterAcademy by
# Dr. Phil Polstra (@ppolstra)

usage () {
	echo "usage: $0 <database> <starting date>"
	echo "Simple script to get timeline from the database"
	exit 1
}

if [ $# -lt 2 ] ; then
   usage
fi


cat << EOF | mysql $1 -u root -p
select Operation, timeline.date, timeline.time, filename, permissions, userid, groupid
   from files, timeline
   where timeline.date >= str_to_date("$2", "%m/%d/%Y") and
   files.recno = timeline.recno
   order by timeline.date desc, timeline.time desc;
EOF
```

```sh
u64@u64-VirtualBox:~/Desktop$ ./print-timeline.sh case-2015-3-9 "03/01/2015"
Enter password:
Operation	date	time	filename	permissions	userid	groupid
A	2015-03-12	16:29:56	./home	755	0	0
A	2015-03-12	16:29:44	./vmlinuz	777	0	0
A	2015-03-12	16:29:44	./initrd.img	777	0	0
A	2015-03-12	10:42:54	./bin/sync	755	0	0
C	2015-03-12	10:42:54	./home/john/.cache/upstart/dbus.log	640	1000	1000
M	2015-03-12	10:42:54	./home/john/.cache/upstart/dbus.log	640	1000	1000
M	2015-03-12	10:41:33	./home/john/.local/share/zeitgeist/activity.sqlite-wal	600	1000	1000
M	2015-03-12	10:41:33	./home/john/.local/share/zeitgeist/activity.sqlite-shm	600	1000	1000
C	2015-03-12	10:41:33	./home/john/.local/share/zeitgeist/activity.sqlite-wal	600	1000	1000
C	2015-03-12	10:41:33	./home/john/.local/share/zeitgeist/activity.sqlite-shm	600	1000	1000
A	2015-03-12	10:41:33	./home/john/.local/share/zeitgeist/activity.sqlite-wal	600	1000	1000
A	2015-03-12	10:38:13	./var/tmp	1777	0	0
A	2015-03-12	10:38:13	./tmp	1777	0	0
A	2015-03-12	10:38:13	./usr/lib/x86_64-linux-gnu/deja-dup/libdeja.so	644	0	0
A	2015-03-12	10:38:13	./usr/lib/x86_64-linux-gnu/deja-dup/tools	755	0	0
A	2015-03-12	10:38:13	./usr/lib/x86_64-linux-gnu/deja-dup/tools/libduplicity.so	644	0	0
A	2015-03-12	10:38:13	./usr/lib/x86_64-linux-gnu/deja-dup/tools/duplicity.plugin	644	0	0
A	2015-03-12	10:38:13	./usr/lib/x86_64-linux-gnu/deja-dup/deja-dup-monitor	755	0	0
A	2015-03-12	10:38:13	./usr/lib/libpeas-1.0.so.0.801.0	644	0	0
A	2015-03-12	10:37:40	./home/john/Downloads/xingyiquan/xingyi_kernel_src/xingyiquan.ko	644	0	0
A	2015-03-12	10:37:40	./home/john/Downloads/xingyiquan/xingyi_userspace_src/xingyi_rootshell	755	0	0
A	2015-03-12	10:37:40	./home/john/Downloads/xingyiquan/xingyi_userspace_src/xingyi_rootshell.c	644	1000	1000
A	2015-03-12	10:37:40	./home/john/.gconf/apps/gnome-terminal/profiles/Default/%gconf.xml	600	1000	1000
A	2015-03-12	10:37:40	./tmp/xingyi_bindshell_pid	644	0	0
A	2015-03-12	10:37:40	./tmp/xingyi_bindshell_port	644	0	0
A	2015-03-12	10:37:40	./usr/bin/python2.7	755	0	0
A	2015-03-12	10:37:40	./usr/bin/python	777	0	0
A	2015-03-12	10:37:40	./bin/xingyi_bindshell	755	0	0
```
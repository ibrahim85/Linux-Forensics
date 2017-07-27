#!/bin/bash
# Simple shell script to create standard metadata tables.
# Intended for use as part of a forensics investigation.
#
# Developed for PentesterAcademy by
# Dr. Phil Polstra (@ppolstra)

usage () {
	echo "usage: $0 <database> <CSV filename>"
	echo "Simple script to create metadate tables in the database"
        echo "Assumes CSV, passwd, and group files in /tmp"
	exit 1
}

if [ $# -lt 2 ] ; then
   usage
fi


cat << EOF | mysql $1 -u root -p 
create table files (
   AccessDate date not null,
   AccessTime time not null,
   ModifyDate date not null,
   ModifyTime time not null,
   CreateDate date not null,
   CreateTime time not null,
   Permissions smallint not null,
   UserId smallint not null,
   GroupId smallint not null,
   FileSize bigint not null,
   Filename varchar(2048) not null,
   recno bigint not null auto_increment,
   primary key(recno)
);

load data infile "/tmp/$2"
   into table files
   fields terminated by ';'
   enclosed by '"' 
   lines terminated by '\n'
   ignore 1 rows 
   (@AccessDate, AccessTime, @ModifyDate, ModifyTime, @CreateDate, CreateTime,
     Permissions, UserId, GroupId, FileSize, Filename)
    set AccessDate=str_to_date(@AccessDate, "%m/%d/%Y"),
        ModifyDate=str_to_date(@ModifyDate, "%m/%d/%Y"),
        CreateDate=str_to_date(@CreateDate, "%m/%d/%Y");

create table users (
   username varchar(255) not null,
   passwordHash varchar(255) not null,
   uid int not null,
   gid int not null,
   userInfo varchar(255) not null,
   homeDir varchar(255) not null,
   shell varchar(2048) not null,
   primary key (username)
   );

load data infile '/tmp/passwd'
   into table users
   fields terminated by ':'
   enclosed by '"' 
   lines terminated by '\n';

create table groups (
   groupname varchar(255) not null,
   passwordHash varchar(255) not null,
   gid int not null,
   userlist varchar(2048)
   );

load data infile '/tmp/group'
   into table groups
   fields terminated by ':'
   enclosed by '"' 
   lines terminated by '\n';

EOF

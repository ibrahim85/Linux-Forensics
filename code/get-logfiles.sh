#!/bin/bash
# Simple script to get all logs and optionally
# store them in a database.
# Warning: This script might take a long time to run!
# by Dr. Phil Polstra (@ppolstra) as developed for
# PentesterAcademy.com.

usage () {
	echo "usage: $0 <mount point of root> [database name]"
	echo "Simple script to get log files and optionally store them to a database."
	exit 1
}

if [ $# -1t 1 ] ; then
   usage
fi

# find only files, exclude files with numbers as they are old logs 
# execute echo, cat, and echo for all files found 
olddir=$(pwd)
cd $1/var
find log -type f -regextype posix-extended -regex 'log/[a-zA-Z\.]+(/[a-zA-Z\.]+)*' \
   -exec awk '{ print "{};" $0}' {} \; | tee /tmp/logfiles.csv
cd $olddir

if [ $# -gt 1 ] ; then
chown mysql:mysql /tmp/logfiles.csv
cls
echo "Let's put that in the database"
cat << EOF | mysql $2 -u root -p 
create table logs (
   logFilename varchar(2048) not null,
   logentry varchar(2048) not null,
   recno bigint not null auto_increment,
   primary key(recno)
);

load data local infile "/tmp/logfiles.csv"
   into table logs
   fields terminated by ';'
   enclosed by '"' 
   lines terminated by '\n'; 
EOF
fi

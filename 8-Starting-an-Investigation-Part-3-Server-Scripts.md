#### 8. Starting an Investigation Part 3: Server Scripts

###### ```start-case.sh```

```sh
#!/bin/bash
# Simple script to start a new case on a forensics
# workstation.  Will create a new folder if needed
# and start two listeners: one for log information
# and the other to receive files. Intended to be
# used as part of initial live response.
# by Dr. Phil Polstra (@ppolstra) as developed for
# PentesterAcademy.com.

usage () {
	echo "usage: $0 <case number>"
	echo "Simple script to create case folder and start listeners"
	exit 1
}

if [ $# -lt 1 ] ; then
	usage
else
	echo "Starting case $1"
fi

#if the directory doesn't exist create it
if [ ! -d $1 ] ; then
	mkdir $1
fi

# create the log listener
`nc -k -l 4444 >> $1/log.txt` &
echo "Started log listener for case $1 on $(date)" | nc localhost 4444

# start the file listener
`./start-file-listener.sh $1` &
```

###### ```start-file-listener.sh```

```sh
#!/bin/bash
# Simple script to start a new file
# listener. Intended to be
# used as part of initial live response.
# by Dr. Phil Polstra (@ppolstra) as developed for
# PentesterAcademy.com.

# When a filename is sent to port 5555 a transfer on 5556
# is expected to follow.

usage () {
	echo "usage: $0 <case name>"
	echo "Simple script to start a file listener"
	exit 1
}

# did you specify a file?
if [ $# -lt 1 ] ; then
   usage
fi

while true
do
   filename=$(nc -l 5555)
   nc -l 5556 > $1/$(basename $filename)
done
```

###### ```close-case.sh```

```sh
#!/bin/bash
# Simple script to start shut down listeners.
# Intended to be used as part of initial live response.
# by Dr. Phil Polstra (@ppolstra) as developed for
# PentesterAcademy.com.

echo "Shutting down listeners at $(date) at user request" | nc localhost 4444
killall start-case.sh
killall start-file-listener.sh
killall nc
```
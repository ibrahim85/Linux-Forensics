#### 9. Starting an Investigation Part 4: Client Scripts

###### ```setup-client.sh```

```sh
# Simple script to set environment variables for a
# system under investigation.  Intended to be
# used as part of initial live response.
# by Dr. Phil Polstra (@ppolstra) as developed for
# PentesterAcademy.com.

usage () {
	echo "usage: $0 <forensics workstation IP> [log port] [filename port] [file transfer port]"
	echo "Simple script to set variables for communication to forensics workstation"
	exit 1
}

# did you specify a file?
if [ $# -lt 1 ] ; then
   usage
fi

export RHOST=$1

if [ $# -gt 1 ] ; then
   export RPORT=$2
else
   export RPORT=4444
fi
if [ $# -gt 2 ] ; then
   export RFPORT=$3
else
   export RFPORT=5555
fi
if [ $# -gt 3 ] ; then
   export RFTPORT=$4
else
   export RFTPORT=5556
fi
```

###### ```send-log.sh```

```sh
# Simple script to send a new log entry
# to listener on forensics workstation. Intended to be
# used as part of initial live response.
# by Dr. Phil Polstra (@ppolstra) as developed for
# PentesterAcademy.com.

# defaults primarily for testing
[ -z "$RHOST" ] && { export RHOST=localhost; }
[ -z "$RPORT" ] && { export RPORT=4444; }

usage () {
	echo "usage: $0 <command or script>"
	echo "Simple script to send a log entry to listener"
	exit 1
}

# did you specify a command?
if [ $# -lt 1 ] ; then
   usage
else
   echo -e "++++Sending log for $@ at $(date) ++++\n $($@) \n----end----\n"  | nc $RHOST $RPORT
fi
```

###### ```send-file.sh```

```sh
# Simple script to send a new file
# to listener on forensics workstation. Intended to be
# used as part of initial live response.
# by Dr. Phil Polstra (@ppolstra) as developed for
# PentesterAcademy.com.

# defaults primarily for testing
[ -z "$RHOST" ] && { export RHOST=localhost; }
[ -z "$RPORT" ] && { export RPORT=4444; }
[ -z "$RFPORT" ] && { export RFPORT=5555; }
[ -z "$RFTPORT" ] && { export RFTPORT=5556; }

usage () {
	echo "usage: $0 <filename>"
	echo "Simple script to send a file to listener"
	exit 1
}

# did you specify a file?
if [ $# -lt 1 ] ; then
   usage
fi

#log it
echo "Attempting to send file $1 at $(date)" | nc $RHOST $RPORT
#send name
echo $1 | nc $RHOST $RFPORT
#give it time
sleep 5
nc $RHOST $RFTPORT < $1
```
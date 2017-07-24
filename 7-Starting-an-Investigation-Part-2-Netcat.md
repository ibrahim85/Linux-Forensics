###### 7. Starting an Investigation Part 2: Netcat

###### Minimize disturbance to system- Don't install anything on subject system 
- Don't create new files on the system 
- Minimize memory footprint- Possible solutions	- Netcat (best) 
	- Store to USB drive

###### Setup

```sh
u64@ubuntu64:~$ cd /media/u64/14b51e12-ed3f-41e7-9f91-af3717576fc1/
u64@ubuntu64:/media/u64/14b51e12-ed3f-41e7-9f91-af3717576fc1$ ls
lost+found  x64
u64@ubuntu64:/media/u64/14b51e12-ed3f-41e7-9f91-af3717576fc1$ cd x64/
```

- Run known ```good shell```

```sh
u64@ubuntu64:/media/u64/14b51e12-ed3f-41e7-9f91-af3717576fc1/x64$ exec bin/bash
```

- Set ```PATH``` to only point to your directories

```sh
u64@ubuntu64:/media/u64/14b51e12-ed3f-41e7-9f91-af3717576fc1/x64$ export PATH=/media/u64/14b51e12-ed3f-41e7-9f91-af3717576fc1/x64/bin:/media/u64/14b51e12-ed3f-41e7-9f91-af3717576fc1/x64/sbin
u64@ubuntu64:/media/u64/14b51e12-ed3f-41e7-9f91-af3717576fc1/x64$
```

- Reset ```LD_LIBRARY_PATH```

```sh
u64@ubuntu64:/media/u64/14b51e12-ed3f-41e7-9f91-af3717576fc1/x64$ export LD_LIBRARY_PATH=/media/u64/14b51e12-ed3f-41e7-9f91-af3717576fc1/x64/lib:/media/u64/14b51e12-ed3f-41e7-9f91-af3717576fc1/x64/lib64
u64@ubuntu64:/media/u64/14b51e12-ed3f-41e7-9f91-af3717576fc1/x64$
```

```sh
u64@ubuntu64:/media/u64/14b51e12-ed3f-41e7-9f91-af3717576fc1/x64$ which ifconfig
/media/u64/14b51e12-ed3f-41e7-9f91-af3717576fc1/x64/sbin/ifconfig
u64@ubuntu64:/media/u64/14b51e12-ed3f-41e7-9f91-af3717576fc1/x64$
```

###### Transfer data using ```nc```

In ```Terminal 1```

```sh
u64@ubuntu64:~$ nc -k -l 9999 > out.txt
```

In ```Terminal 2```

```sh
u64@ubuntu64:~$ date | nc 10.0.0.60 9999
```

```sh
u64@ubuntu64:~$ uname -a | nc 10.0.0.60 9999
```

In ```Terminal 1```

```sh
u64@ubuntu64:~$ cat out.txt
Mon Jul 24 10:24:51 PDT 2017
Linux ubuntu64 4.8.0-36-generic #36~16.04.1-Ubuntu SMP Sun Feb 5 09:39:57 UTC 2017 x86_64 x86_64 x86_64 GNU/Linux
u64@ubuntu64:~$
```

###### Transfer files using ```nc```

In ```Terminal 1```

```sh
u64@ubuntu64:~$ nc -l 4444 > bash.suspect
```

In ```Terminal 2```

```sh
u64@ubuntu64:~$ nc 10.0.0.60 4444 < /bin/bash
```

In ```Terminal 1```

```sh
u64@ubuntu64:~$ ll bash.suspect
-rw-rw-r-- 1 u64 u64 1037528 Jul 24 10:26 bash.suspect
u64@ubuntu64:~$ chmod +x bash.suspect
u64@ubuntu64:~$ sh
$ ls
bash.suspect  Documents  examples.desktop  out.txt   Public	Videos
Desktop       Downloads  Music		   Pictures  Templates
$ ./bash.suspect
u64@ubuntu64:~$
```

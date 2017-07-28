#### 17. Live Analysis Part 4: Dumping RAM with LiME

###### Note

- Do not compile ```LiME``` on the target machine
- Compile ```LiME``` on a machine with an ```identical kernel``` as the target machine

###### Target Machine

```sh
u64@u64-VirtualBox:~/Desktop/LiME/src$ ll
total 296
drwxrwxr-x 3 u64 u64  4096 Jul 28 12:03 ./
drwxrwxr-x 5 u64 u64  4096 Jul 28 11:39 ../
-rw-rw-r-- 1 u64 u64     8 Jul 28 11:54 built-in.o
-rw-rw-r-- 1 u64 u64   137 Jul 28 11:54 .built-in.o.cmd
-rw-rw-r-- 1 u64 u64  2557 Jul 28 11:39 disk.c
-rw-rw-r-- 1 u64 u64  4080 Jul 28 11:54 disk.o
-rw-rw-r-- 1 u64 u64 46272 Jul 28 11:54 .disk.o.cmd
-rw-rw-r-- 1 u64 u64 12480 Jul 28 11:54 lime-3.16.0-30-generic.ko
-rw-rw-r-- 1 u64 u64 10496 Jul 28 11:40 lime-4.10.0-27-generic.ko
-rw-rw-r-- 1 u64 u64  1920 Jul 28 11:39 lime.h
-rw-rw-r-- 1 u64 u64   215 Jul 28 11:54 .lime.ko.cmd
-rw-rw-r-- 1 u64 u64  1576 Jul 28 11:54 lime.mod.c
-rw-rw-r-- 1 u64 u64  3552 Jul 28 11:54 lime.mod.o
-rw-rw-r-- 1 u64 u64 26128 Jul 28 11:54 .lime.mod.o.cmd
-rw-rw-r-- 1 u64 u64  9816 Jul 28 11:54 lime.o
-rw-rw-r-- 1 u64 u64   202 Jul 28 11:54 .lime.o.cmd
-rw-rw-r-- 1 u64 u64  6614 Jul 28 11:39 main.c
-rw-rw-r-- 1 u64 u64  7624 Jul 28 11:54 main.o
-rw-rw-r-- 1 u64 u64 46272 Jul 28 11:54 .main.o.cmd
-rw-rw-r-- 1 u64 u64  1661 Jul 28 11:39 Makefile
-rw-rw-r-- 1 u64 u64  1722 Jul 28 11:39 Makefile.sample
-rw-rw-r-- 1 u64 u64    42 Jul 28 11:54 modules.order
-rw-rw-r-- 1 u64 u64     0 Jul 28 11:39 Module.symvers
-rw-rw-r-- 1 u64 u64  3889 Jul 28 11:39 tcp.c
-rw-rw-r-- 1 u64 u64  3720 Jul 28 11:54 tcp.o
-rw-rw-r-- 1 u64 u64 46261 Jul 28 11:54 .tcp.o.cmd
drwxrwxr-x 2 u64 u64  4096 Jul 28 11:54 .tmp_versions/
u64@u64-VirtualBox:~/Desktop/LiME/src$
```

```sh
u64@u64-VirtualBox:~/Desktop/LiME/src$ sudo insmod lime-4.10.0-27-generic.ko "path=tcp:4444 format=lime"
u64@u64-VirtualBox:~/Desktop/LiME/src$
```

###### Forensics Workstation

```sh
u64@u64-VirtualBox:~/Desktop$ nc 10.0.0.150 4444 > ram.lime
```

```sh
u64@u64-VirtualBox:~/Desktop$ ll ram.lime
-rw-rw-r-- 1 u64 u64 1073278016 Jul 28 12:43 ram.lime
u64@u64-VirtualBox:~/Desktop$
```

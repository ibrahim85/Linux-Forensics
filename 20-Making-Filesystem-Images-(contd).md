#### 20. Making Filesystem Images (contd.)

- Subject ```vmdk```

```sh
u64@ubuntu64:~/Desktop/subject$ ll
total 18874408
drwxrwxr-x 2 u64 u64        4096 Jul 25 10:25 ./
drwxr-xr-x 5 u64 u64        4096 Jul 25 10:08 ../
-rw-rw-r-- 1 u64 u64 19327352832 Jul 25 10:25 pentester-academy-subject1-flat.vmdk
-rw-rw-r-- 1 u64 u64       10230 Jul 25 10:17 pentester-academy-subject1.vbox
-rw-rw-r-- 1 u64 u64        8871 Jul 25 10:17 pentester-academy-subject1.vbox-prev
-rw-rw-r-- 1 u64 u64         661 Jul 25 10:18 pentester-academy-subject1.vmdk
u64@ubuntu64:~/Desktop/subject$
```

- Inspect the ```vmdk``` using ```fdisk```


```sh
u64@ubuntu64:~/Desktop/subject$ sudo fdisk pentester-academy-subject1-flat.vmdk
[sudo] password for u64:

Welcome to fdisk (util-linux 2.27.1).
Changes will remain in memory only, until you decide to write them.
Be careful before using the write command.


Command (m for help): p
Disk pentester-academy-subject1-flat.vmdk: 18 GiB, 19327352832 bytes, 37748736 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: dos
Disk identifier: 0x0004565b

Device                                Boot    Start      End  Sectors Size Id Type
pentester-academy-subject1-flat.vmdk1 *        2048 33554431 33552384  16G 83 Linux
pentester-academy-subject1-flat.vmdk2      33556478 37746687  4190210   2G  5 Extended
pentester-academy-subject1-flat.vmdk5      33556480 37746687  4190208   2G 82 Linux swap / Solaris

Command (m for help): q

u64@ubuntu64:~/Desktop/subject$
```

- Use ```dcfldd``` to create disk image

```sh
root@ubuntu64:/home/u64/Desktop/subject# dcfldd if=pentester-academy-subject1-flat.vmdk of=/media/u64/14b51e12-ed3f-41e7-9f91-af3717576fc1/2017-7-25.img hash=sha256 hashwindow=1M hashlog=2017-7-25.hashes
354560 blocks (11080Mb) written.
354614+0 records in
354613+0 records out
root@ubuntu64:/home/u64/Desktop/subject#
```

- Raw image with hashes

```sh
root@ubuntu64:/home/u64/Desktop/subject# ll /media/u64/14b51e12-ed3f-41e7-9f91-af3717576fc1/
total 11347712
drwx------  2 root root        4096 Jul 25 11:04 ./
drwxr-x---+ 3 root root        4096 Jul 25 09:46 ../
-rw-r--r--  1 root root 11619987456 Jul 25 11:07 2017-7-25.img
root@ubuntu64:/home/u64/Desktop/subject#
```

```sh
root@ubuntu64:/home/u64/Desktop/subject# mv 2017-7-25.hashes /media/u64/14b51e12-ed3f-41e7-9f91-af3717576fc1/
```

- Hashes

```sh
root@ubuntu64:/media/u64/14b51e12-ed3f-41e7-9f91-af3717576fc1# ll
total 11348688
drwx------  2 root root        4096 Jul 25 11:08 ./
drwxr-x---+ 3 root root        4096 Jul 25 09:46 ../
-rw-r--r--  1 root root      995328 Jul 25 11:07 2017-7-25.hashes
-rw-r--r--  1 root root 11619987456 Jul 25 11:07 2017-7-25.img
root@ubuntu64:/media/u64/14b51e12-ed3f-41e7-9f91-af3717576fc1#
```

```sh
root@ubuntu64:/media/u64/14b51e12-ed3f-41e7-9f91-af3717576fc1# head 2017-7-25.hashes
34848: bfb6e30fc4fd4b575ba2019b5877df4052ac73ecb84a08393c60b5e6e83c577f
784334848 - 785383424: 315c2251fa95b309f99903ca7913f497c58f66adbf4dcb3fcaaebf3a5436a77a
785383424 - 786432000: 7cacbac382008a7e7a5a4ed6460d11c4f0db529c7ada631a5aba7aa280917579
786432000 - 787480576: 69a709876adb7ddcf607d0c1fad0f59a89beaff81f9fe4009e9ae1deaa405263
787480576 - 788529152: 2319aafca884ee73963fcefa9f22d0b3a6688256f2cf428f38221adb77f70c9b
788529152 - 789577728: 58ca7278c926b96ee3c7abfbc98c6c1fc2c5b049712180ebef179e768e217ea0
789577728 - 790626304: a988e57469bad46eb7f6fce4ded828cd1330811fdef41e23810d83664aa0f8f0
790626304 - 791674880: f3bc3d69681e82a0b39d2b75575dbe9a85dd37a1dd90f293faeb2e22312f548d
791674880 - 792723456: e227895f4b1e8bcf2263815621949ffe6de7f96f66d03e34f6449a51de2d7d5f
792723456 - 793772032: d01c219b2297bf9cf4a242a68786e23a375f99a66191a76e9771b30f59fc952e
root@ubuntu64:/media/u64/14b51e12-ed3f-41e7-9f91-af3717576fc1#
```

```sh
root@ubuntu64:/media/u64/14b51e12-ed3f-41e7-9f91-af3717576fc1# tail 2017-7-25.hashes
11576279040 - 11577327616: 30e14955ebf1352266dc2ff8067e68104607e750abb9d3b36582b8af909fcb58
11577327616 - 11578376192: 30e14955ebf1352266dc2ff8067e68104607e750abb9d3b36582b8af909fcb58
11578376192 - 11579424768: 30e14955ebf1352266dc2ff8067e68104607e750abb9d3b36582b8af909fcb58
11579424768 - 11580473344: 30e14955ebf1352266dc2ff8067e68104607e750abb9d3b36582b8af909fcb58
11580473344 - 11581521920: 30e14955ebf1352266dc2ff8067e68104607e750abb9d3b36582b8af909fcb58
11581521920 - 11582570496: 30e14955ebf1352266dc2ff8067e68104607e750abb9d3b36582b8af909fcb58
11582570496 - 11583619072: 30e14955ebf1352266dc2ff8067e68104607e750abb9d3b36582b8af909fcb58
11583619072 - 11584667648: 30e14955ebf1352266dc2ff8067e68104607e750abb9d3b36582b8af909fcb58
11584667648 - 11585716224: 30e14955ebf1352266dc2ff8067e68104607e750abb9d3b36582b8af909fcb58
11585716224 - 11root@ubuntu64:/media/u64/14b51e12-ed3f-41e7-9f91-af3717576fc1#
```
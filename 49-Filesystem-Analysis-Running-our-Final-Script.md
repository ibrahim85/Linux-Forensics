#### 49. Filesystem Analysis: Running our Final Script

###### Identify offset using ```fdisk```

```sh
u64@u64-VirtualBox:~/Desktop$ sudo fdisk 2015-3-9.img
[sudo] password for u64:

Welcome to fdisk (util-linux 2.27.1).
Changes will remain in memory only, until you decide to write them.
Be careful before using the write command.


Command (m for help): p
Disk 2015-3-9.img: 18 GiB, 19327352832 bytes, 37748736 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: dos
Disk identifier: 0x0004565b

Device        Boot    Start      End  Sectors Size Id Type
2015-3-9.img1 *        2048 33554431 33552384  16G 83 Linux
2015-3-9.img2      33556478 37746687  4190210   2G  5 Extended
2015-3-9.img5      33556480 37746687  4190208   2G 82 Linux swap / Solaris

Command (m for help): q

u64@u64-VirtualBox:~/Desktop$
```

###### Using ```extfs.py```

```sh
u64@u64-VirtualBox:~/Desktop$ ./extfs.py
usage ./extfs.py <image file> <offset in sectors>
Reads superblock from an image file
u64@u64-VirtualBox:~/Desktop$
```

```sh
u64@u64-VirtualBox:~/Desktop$ ./extfs.py 2015-3-9.img 2048
algorithmUsageBitmap: 0
backupBlockGroups: [0, 0]
blockCountHi: 0
blockGroupNumber: 0
blockSize: 4096
blocksPerGroup: 32768
checkInterval: 0
checksum: 0
clusterSize: 4
clustersPerGroup: 32768
compatibleFeatures: 60
compatibleFeaturesList: ['Has Journal', 'Extended Attributes', 'Resize Inode', 'Directory Index']
creatorOs: Linux
defaultMountOptions: 12
defaultRegGid: 0
defaultResUid: 0
descriptorSize: 0
encryptionAlgorithms: []
errorCount: 0
errors: Continue
firstDataBlock: 0
firstErrorBlock: 0
firstErrorFunction:
firstErrorInode: 0
firstErrorLine: 0
firstErrorTime: Thu Jan  1 00:00:00 1970
firstInode: 11
firstMetaBlockGroup: 0
freeBlocks: 3042264
freeBlocksHi: 0
freeInodes: 863973
groupQuotaInode: 0
groupsPerFlex: 16
hashSeed: [2344286409, 2756545686, 3468101558, 1457826801]
hashVersion: Half MD4
incompatibleFeatures: 578
incompatibleFeaturesList: ['Filetype', 'Extents', 'Flexible Block Groups']
inodeSize: 256
inodesPerGroup: 8192
journalBackupType: 1
journalBlocks: [193290, 4, 0, 0, 32767, 1606657, 32767, 1, 1639424, 0, 0, 0, 0, 0, 0, 0, 134217728]
journalDev: 0
journalInode: 8
journalUuid: 00000000000000000000000000000000
kilobytesWritten: 7350973
lastCheck: Fri Mar  6 03:37:57 2015
lastErrorBlock: 0
lastErrorFunction:
lastErrorInode: 0
lastErrorLine: 0
lastErrorTime: Thu Jan  1 00:00:00 1970
lastMounted: /
lastOrphan: 0
magic: 61267
maxMountCount: 65535
metadataChecksumType: 0
minInodeExtraSize: 28
minorRevision: 0
miscFlags: 1
mkfsTime: Fri Mar  6 03:37:57 2015
mmpBlock: 0
mmpInterval: 0
mountCount: 14
mountOptions:
mountTime: Thu Mar 12 23:29:39 2015
overheadBlocks: 0
preallocBlocks: 0
preallocDirBlock: 0
raidStride: 0
raidStripeWidth: 0
readOnlyCompatibleFeatures: 123
readOnlyCompatibleFeaturesList: ['Sparse Super', 'Large File', 'Huge File', 'Group Descriptor Table Checksum', 'Directory Nlink', 'Extra Isize']
reservedBlockCountHi: 0
reservedGdtBlocks: 1023
reservedPad: 0
restrictedBlocks: 209702
revisionLevel: 1
snapshotId: 0
snapshotInode: 0
snapshotList: 0
snapshotReservedBlocks: 0
state: Cleanly unmounted
totalBlocks: 4194048
totalInodes: 1048576
userQuotaInode: 0
uuid: 6D3257CCE44C5499D141D359183193C1
volumeName:
wantInodeExtraSize: 28
writeTime: Thu Mar 12 23:30:28 2015

Block Group: 0
Flags: ['Inode Zeroed']
Blocks: 0 - 32767
Inodes: 1 - 8192
Layout:
   Superblock 0 - 0
   Group Descriptor Table 1 - 1
   Reserved GDT Blocks 2 - 1024
   Data Block Bitmap 1025 - 1025
   Inode Bitmap 1041 - 1041
   Inode Table 1057 - 1568
   Data Blocks 9249 - 32767
Free Inodes: 668
Free Blocks: 22866
Directories: 370
Checksum: 0xb0a2
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 1
Flags: ['Inode Zeroed']
Blocks: 32768 - 65535
Inodes: 8193 - 16384
Layout:
   Superblock 32768 - 32768
   Group Descriptor Table 32769 - 32769
   Reserved GDT Blocks 32770 - 33792
   Data Block Bitmap 1026 - 1026
   Inode Bitmap 1042 - 1042
   Inode Table 1569 - 2080
   Data Blocks 33793 - 65535
Free Inodes: 7521
Free Blocks: 1434
Directories: 2
Checksum: 0x328a
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 2
Flags: ['Inode Uninitialized', 'Inode Zeroed']
Blocks: 65536 - 98303
Inodes: 16385 - 24576
Layout:
   Data Block Bitmap 1027 - 1027
   Inode Bitmap 1043 - 1043
   Inode Table 2081 - 2592
   Data Blocks 65536 - 98303
Free Inodes: 8192
Free Blocks: 2119
Directories: 0
Checksum: 0xe8a0
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 3
Flags: ['Inode Uninitialized', 'Inode Zeroed']
Blocks: 98304 - 131071
Inodes: 24577 - 32768
Layout:
   Superblock 98304 - 98304
   Group Descriptor Table 98305 - 98305
   Reserved GDT Blocks 98306 - 99328
   Data Block Bitmap 1028 - 1028
   Inode Bitmap 1044 - 1044
   Inode Table 2593 - 3104
   Data Blocks 99329 - 131071
Free Inodes: 8192
Free Blocks: 23816
Directories: 0
Checksum: 0xeb61
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 4
Flags: ['Inode Uninitialized', 'Inode Zeroed']
Blocks: 131072 - 163839
Inodes: 32769 - 40960
Layout:
   Data Block Bitmap 1029 - 1029
   Inode Bitmap 1045 - 1045
   Inode Table 3105 - 3616
   Data Blocks 131072 - 163839
Free Inodes: 8192
Free Blocks: 5402
Directories: 0
Checksum: 0x4aec
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 5
Flags: ['Inode Uninitialized', 'Inode Zeroed']
Blocks: 163840 - 196607
Inodes: 40961 - 49152
Layout:
   Superblock 163840 - 163840
   Group Descriptor Table 163841 - 163841
   Reserved GDT Blocks 163842 - 164864
   Data Block Bitmap 1030 - 1030
   Inode Bitmap 1046 - 1046
   Inode Table 3617 - 4128
   Data Blocks 164865 - 196607
Free Inodes: 8192
Free Blocks: 0
Directories: 0
Checksum: 0x7eff
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 6
Flags: ['Inode Uninitialized', 'Inode Zeroed']
Blocks: 196608 - 229375
Inodes: 49153 - 57344
Layout:
   Data Block Bitmap 1031 - 1031
   Inode Bitmap 1047 - 1047
   Inode Table 4129 - 4640
   Data Blocks 196608 - 229375
Free Inodes: 8192
Free Blocks: 12925
Directories: 0
Checksum: 0x2c6
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 7
Flags: ['Inode Uninitialized', 'Inode Zeroed']
Blocks: 229376 - 262143
Inodes: 57345 - 65536
Layout:
   Superblock 229376 - 229376
   Group Descriptor Table 229377 - 229377
   Reserved GDT Blocks 229378 - 230400
   Data Block Bitmap 1032 - 1032
   Inode Bitmap 1048 - 1048
   Inode Table 4641 - 5152
   Data Blocks 230401 - 262143
Free Inodes: 8192
Free Blocks: 6248
Directories: 0
Checksum: 0x9de1
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 8
Flags: ['Inode Uninitialized', 'Inode Zeroed']
Blocks: 262144 - 294911
Inodes: 65537 - 73728
Layout:
   Data Block Bitmap 1033 - 1033
   Inode Bitmap 1049 - 1049
   Inode Table 5153 - 5664
   Data Blocks 262144 - 294911
Free Inodes: 8192
Free Blocks: 15
Directories: 0
Checksum: 0xd358
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 9
Flags: ['Inode Uninitialized', 'Inode Zeroed']
Blocks: 294912 - 327679
Inodes: 73729 - 81920
Layout:
   Superblock 294912 - 294912
   Group Descriptor Table 294913 - 294913
   Reserved GDT Blocks 294914 - 295936
   Data Block Bitmap 1034 - 1034
   Inode Bitmap 1050 - 1050
   Inode Table 5665 - 6176
   Data Blocks 295937 - 327679
Free Inodes: 8192
Free Blocks: 8812
Directories: 0
Checksum: 0x9c24
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 10
Flags: ['Inode Uninitialized', 'Inode Zeroed']
Blocks: 327680 - 360447
Inodes: 81921 - 90112
Layout:
   Data Block Bitmap 1035 - 1035
   Inode Bitmap 1051 - 1051
   Inode Table 6177 - 6688
   Data Blocks 327680 - 360447
Free Inodes: 8192
Free Blocks: 5269
Directories: 0
Checksum: 0x6925
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 11
Flags: ['Inode Uninitialized', 'Inode Zeroed']
Blocks: 360448 - 393215
Inodes: 90113 - 98304
Layout:
   Data Block Bitmap 1036 - 1036
   Inode Bitmap 1052 - 1052
   Inode Table 6689 - 7200
   Data Blocks 360448 - 393215
Free Inodes: 8192
Free Blocks: 13665
Directories: 0
Checksum: 0xb1d7
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 12
Flags: ['Inode Uninitialized', 'Inode Zeroed']
Blocks: 393216 - 425983
Inodes: 98305 - 106496
Layout:
   Data Block Bitmap 1037 - 1037
   Inode Bitmap 1053 - 1053
   Inode Table 7201 - 7712
   Data Blocks 393216 - 425983
Free Inodes: 8192
Free Blocks: 3079
Directories: 0
Checksum: 0xb175
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 13
Flags: ['Inode Uninitialized', 'Inode Zeroed']
Blocks: 425984 - 458751
Inodes: 106497 - 114688
Layout:
   Data Block Bitmap 1038 - 1038
   Inode Bitmap 1054 - 1054
   Inode Table 7713 - 8224
   Data Blocks 425984 - 458751
Free Inodes: 8192
Free Blocks: 6681
Directories: 0
Checksum: 0x44d7
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 14
Flags: ['Inode Uninitialized', 'Inode Zeroed']
Blocks: 458752 - 491519
Inodes: 114689 - 122880
Layout:
   Data Block Bitmap 1039 - 1039
   Inode Bitmap 1055 - 1055
   Inode Table 8225 - 8736
   Data Blocks 458752 - 491519
Free Inodes: 8192
Free Blocks: 2717
Directories: 0
Checksum: 0x5d91
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 15
Flags: ['Inode Uninitialized', 'Inode Zeroed']
Blocks: 491520 - 524287
Inodes: 122881 - 131072
Layout:
   Data Block Bitmap 1040 - 1040
   Inode Bitmap 1056 - 1056
   Inode Table 8737 - 9248
   Data Blocks 491520 - 524287
Free Inodes: 8192
Free Blocks: 3104
Directories: 0
Checksum: 0xb69
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 16
Flags: ['Inode Zeroed']
Blocks: 524288 - 557055
Inodes: 131073 - 139264
Layout:
   Data Block Bitmap 524288 - 524288
   Inode Bitmap 524304 - 524304
   Inode Table 524320 - 524831
   Data Blocks 532512 - 557055
Free Inodes: 0
Free Blocks: 19399
Directories: 1016
Checksum: 0x237b
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 17
Flags: ['Inode Zeroed']
Blocks: 557056 - 589823
Inodes: 139265 - 147456
Layout:
   Data Block Bitmap 524289 - 524289
   Inode Bitmap 524305 - 524305
   Inode Table 524832 - 525343
   Data Blocks 557056 - 589823
Free Inodes: 0
Free Blocks: 8
Directories: 931
Checksum: 0xd5b3
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 18
Flags: ['Inode Zeroed']
Blocks: 589824 - 622591
Inodes: 147457 - 155648
Layout:
   Data Block Bitmap 524290 - 524290
   Inode Bitmap 524306 - 524306
   Inode Table 525344 - 525855
   Data Blocks 589824 - 622591
Free Inodes: 0
Free Blocks: 905
Directories: 382
Checksum: 0xf8f
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 19
Flags: ['Inode Zeroed']
Blocks: 622592 - 655359
Inodes: 155649 - 163840
Layout:
   Data Block Bitmap 524291 - 524291
   Inode Bitmap 524307 - 524307
   Inode Table 525856 - 526367
   Data Blocks 622592 - 655359
Free Inodes: 2278
Free Blocks: 2266
Directories: 103
Checksum: 0x2a53
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 20
Flags: ['Inode Uninitialized', 'Inode Zeroed']
Blocks: 655360 - 688127
Inodes: 163841 - 172032
Layout:
   Data Block Bitmap 524292 - 524292
   Inode Bitmap 524308 - 524308
   Inode Table 526368 - 526879
   Data Blocks 655360 - 688127
Free Inodes: 8192
Free Blocks: 5925
Directories: 0
Checksum: 0x845e
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 21
Flags: ['Inode Uninitialized', 'Inode Zeroed']
Blocks: 688128 - 720895
Inodes: 172033 - 180224
Layout:
   Data Block Bitmap 524293 - 524293
   Inode Bitmap 524309 - 524309
   Inode Table 526880 - 527391
   Data Blocks 688128 - 720895
Free Inodes: 8192
Free Blocks: 7842
Directories: 0
Checksum: 0xebcb
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 22
Flags: ['Inode Uninitialized', 'Inode Zeroed']
Blocks: 720896 - 753663
Inodes: 180225 - 188416
Layout:
   Data Block Bitmap 524294 - 524294
   Inode Bitmap 524310 - 524310
   Inode Table 527392 - 527903
   Data Blocks 720896 - 753663
Free Inodes: 8192
Free Blocks: 15276
Directories: 0
Checksum: 0x3acd
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 23
Flags: ['Inode Uninitialized', 'Inode Zeroed']
Blocks: 753664 - 786431
Inodes: 188417 - 196608
Layout:
   Data Block Bitmap 524295 - 524295
   Inode Bitmap 524311 - 524311
   Inode Table 527904 - 528415
   Data Blocks 753664 - 786431
Free Inodes: 8192
Free Blocks: 4162
Directories: 0
Checksum: 0x7f2d
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 24
Flags: ['Inode Uninitialized', 'Inode Zeroed']
Blocks: 786432 - 819199
Inodes: 196609 - 204800
Layout:
   Data Block Bitmap 524296 - 524296
   Inode Bitmap 524312 - 524312
   Inode Table 528416 - 528927
   Data Blocks 786432 - 819199
Free Inodes: 8192
Free Blocks: 11875
Directories: 0
Checksum: 0x81d7
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 25
Flags: ['Inode Uninitialized', 'Inode Zeroed']
Blocks: 819200 - 851967
Inodes: 204801 - 212992
Layout:
   Superblock 819200 - 819200
   Group Descriptor Table 819201 - 819201
   Reserved GDT Blocks 819202 - 820224
   Data Block Bitmap 524297 - 524297
   Inode Bitmap 524313 - 524313
   Inode Table 528928 - 529439
   Data Blocks 820225 - 851967
Free Inodes: 8192
Free Blocks: 5195
Directories: 0
Checksum: 0x24b7
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 26
Flags: ['Inode Uninitialized', 'Inode Zeroed']
Blocks: 851968 - 884735
Inodes: 212993 - 221184
Layout:
   Data Block Bitmap 524298 - 524298
   Inode Bitmap 524314 - 524314
   Inode Table 529440 - 529951
   Data Blocks 851968 - 884735
Free Inodes: 8192
Free Blocks: 4229
Directories: 0
Checksum: 0x93c5
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 27
Flags: ['Inode Uninitialized', 'Inode Zeroed']
Blocks: 884736 - 917503
Inodes: 221185 - 229376
Layout:
   Superblock 884736 - 884736
   Group Descriptor Table 884737 - 884737
   Reserved GDT Blocks 884738 - 885760
   Data Block Bitmap 524299 - 524299
   Inode Bitmap 524315 - 524315
   Inode Table 529952 - 530463
   Data Blocks 885761 - 917503
Free Inodes: 8192
Free Blocks: 3245
Directories: 0
Checksum: 0x5d5f
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 28
Flags: ['Inode Uninitialized', 'Inode Zeroed']
Blocks: 917504 - 950271
Inodes: 229377 - 237568
Layout:
   Data Block Bitmap 524300 - 524300
   Inode Bitmap 524316 - 524316
   Inode Table 530464 - 530975
   Data Blocks 917504 - 950271
Free Inodes: 8192
Free Blocks: 17413
Directories: 0
Checksum: 0xa94d
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 29
Flags: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
Blocks: 950272 - 983039
Inodes: 237569 - 245760
Layout:
   Data Block Bitmap 524301 - 524301
   Inode Bitmap 524317 - 524317
   Inode Table 530976 - 531487
   Data Blocks 950272 - 983039
Free Inodes: 8192
Free Blocks: 32768
Directories: 0
Checksum: 0xfe6d
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 30
Flags: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
Blocks: 983040 - 1015807
Inodes: 245761 - 253952
Layout:
   Data Block Bitmap 524302 - 524302
   Inode Bitmap 524318 - 524318
   Inode Table 531488 - 531999
   Data Blocks 983040 - 1015807
Free Inodes: 8192
Free Blocks: 32768
Directories: 0
Checksum: 0x5f03
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 31
Flags: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
Blocks: 1015808 - 1048575
Inodes: 253953 - 262144
Layout:
   Data Block Bitmap 524303 - 524303
   Inode Bitmap 524319 - 524319
   Inode Table 532000 - 532511
   Data Blocks 1015808 - 1048575
Free Inodes: 8192
Free Blocks: 32768
Directories: 0
Checksum: 0xffd8
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 32
Flags: ['Inode Zeroed']
Blocks: 1048576 - 1081343
Inodes: 262145 - 270336
Layout:
   Data Block Bitmap 1048576 - 1048576
   Inode Bitmap 1048592 - 1048592
   Inode Table 1048608 - 1049119
   Data Blocks 1056800 - 1081343
Free Inodes: 0
Free Blocks: 22015
Directories: 993
Checksum: 0xa4bd
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 33
Flags: ['Inode Zeroed']
Blocks: 1081344 - 1114111
Inodes: 270337 - 278528
Layout:
   Data Block Bitmap 1048577 - 1048577
   Inode Bitmap 1048593 - 1048593
   Inode Table 1049120 - 1049631
   Data Blocks 1081344 - 1114111
Free Inodes: 0
Free Blocks: 1600
Directories: 566
Checksum: 0x436a
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 34
Flags: ['Inode Zeroed']
Blocks: 1114112 - 1146879
Inodes: 278529 - 286720
Layout:
   Data Block Bitmap 1048578 - 1048578
   Inode Bitmap 1048594 - 1048594
   Inode Table 1049632 - 1050143
   Data Blocks 1114112 - 1146879
Free Inodes: 0
Free Blocks: 1120
Directories: 479
Checksum: 0xa243
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 35
Flags: ['Inode Zeroed']
Blocks: 1146880 - 1179647
Inodes: 286721 - 294912
Layout:
   Data Block Bitmap 1048579 - 1048579
   Inode Bitmap 1048595 - 1048595
   Inode Table 1050144 - 1050655
   Data Blocks 1146880 - 1179647
Free Inodes: 1542
Free Blocks: 2187
Directories: 250
Checksum: 0xd6bd
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 36
Flags: ['Inode Uninitialized', 'Inode Zeroed']
Blocks: 1179648 - 1212415
Inodes: 294913 - 303104
Layout:
   Data Block Bitmap 1048580 - 1048580
   Inode Bitmap 1048596 - 1048596
   Inode Table 1050656 - 1051167
   Data Blocks 1179648 - 1212415
Free Inodes: 8192
Free Blocks: 11877
Directories: 0
Checksum: 0x98b3
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 37
Flags: ['Inode Uninitialized', 'Inode Zeroed']
Blocks: 1212416 - 1245183
Inodes: 303105 - 311296
Layout:
   Data Block Bitmap 1048581 - 1048581
   Inode Bitmap 1048597 - 1048597
   Inode Table 1051168 - 1051679
   Data Blocks 1212416 - 1245183
Free Inodes: 8192
Free Blocks: 32313
Directories: 0
Checksum: 0x6b86
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 38
Flags: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
Blocks: 1245184 - 1277951
Inodes: 311297 - 319488
Layout:
   Data Block Bitmap 1048582 - 1048582
   Inode Bitmap 1048598 - 1048598
   Inode Table 1051680 - 1052191
   Data Blocks 1245184 - 1277951
Free Inodes: 8192
Free Blocks: 32768
Directories: 0
Checksum: 0xcced
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 39
Flags: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
Blocks: 1277952 - 1310719
Inodes: 319489 - 327680
Layout:
   Data Block Bitmap 1048583 - 1048583
   Inode Bitmap 1048599 - 1048599
   Inode Table 1052192 - 1052703
   Data Blocks 1277952 - 1310719
Free Inodes: 8192
Free Blocks: 32768
Directories: 0
Checksum: 0x6c36
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 40
Flags: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
Blocks: 1310720 - 1343487
Inodes: 327681 - 335872
Layout:
   Data Block Bitmap 1048584 - 1048584
   Inode Bitmap 1048600 - 1048600
   Inode Table 1052704 - 1053215
   Data Blocks 1310720 - 1343487
Free Inodes: 8192
Free Blocks: 32768
Directories: 0
Checksum: 0xc8e6
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 41
Flags: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
Blocks: 1343488 - 1376255
Inodes: 335873 - 344064
Layout:
   Data Block Bitmap 1048585 - 1048585
   Inode Bitmap 1048601 - 1048601
   Inode Table 1053216 - 1053727
   Data Blocks 1343488 - 1376255
Free Inodes: 8192
Free Blocks: 32768
Directories: 0
Checksum: 0x683d
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 42
Flags: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
Blocks: 1376256 - 1409023
Inodes: 344065 - 352256
Layout:
   Data Block Bitmap 1048586 - 1048586
   Inode Bitmap 1048602 - 1048602
   Inode Table 1053728 - 1054239
   Data Blocks 1376256 - 1409023
Free Inodes: 8192
Free Blocks: 32768
Directories: 0
Checksum: 0xc953
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 43
Flags: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
Blocks: 1409024 - 1441791
Inodes: 352257 - 360448
Layout:
   Data Block Bitmap 1048587 - 1048587
   Inode Bitmap 1048603 - 1048603
   Inode Table 1054240 - 1054751
   Data Blocks 1409024 - 1441791
Free Inodes: 8192
Free Blocks: 32768
Directories: 0
Checksum: 0x6988
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 44
Flags: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
Blocks: 1441792 - 1474559
Inodes: 360449 - 368640
Layout:
   Data Block Bitmap 1048588 - 1048588
   Inode Bitmap 1048604 - 1048604
   Inode Table 1054752 - 1055263
   Data Blocks 1441792 - 1474559
Free Inodes: 8192
Free Blocks: 32768
Directories: 0
Checksum: 0xcb8c
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 45
Flags: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
Blocks: 1474560 - 1507327
Inodes: 368641 - 376832
Layout:
   Data Block Bitmap 1048589 - 1048589
   Inode Bitmap 1048605 - 1048605
   Inode Table 1055264 - 1055775
   Data Blocks 1474560 - 1507327
Free Inodes: 8192
Free Blocks: 32768
Directories: 0
Checksum: 0x6b57
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 46
Flags: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
Blocks: 1507328 - 1540095
Inodes: 376833 - 385024
Layout:
   Data Block Bitmap 1048590 - 1048590
   Inode Bitmap 1048606 - 1048606
   Inode Table 1055776 - 1056287
   Data Blocks 1507328 - 1540095
Free Inodes: 8192
Free Blocks: 32768
Directories: 0
Checksum: 0xca39
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 47
Flags: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
Blocks: 1540096 - 1572863
Inodes: 385025 - 393216
Layout:
   Data Block Bitmap 1048591 - 1048591
   Inode Bitmap 1048607 - 1048607
   Inode Table 1056288 - 1056799
   Data Blocks 1540096 - 1572863
Free Inodes: 8192
Free Blocks: 32768
Directories: 0
Checksum: 0x6ae2
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 48
Flags: ['Inode Zeroed']
Blocks: 1572864 - 1605631
Inodes: 393217 - 401408
Layout:
   Data Block Bitmap 1572864 - 1572864
   Inode Bitmap 1572880 - 1572880
   Inode Table 1572896 - 1573407
   Data Blocks 1581088 - 1605631
Free Inodes: 621
Free Blocks: 22365
Directories: 1273
Checksum: 0xcef4
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 49
Flags: ['Inode Zeroed']
Blocks: 1605632 - 1638399
Inodes: 401409 - 409600
Layout:
   Superblock 1605632 - 1605632
   Group Descriptor Table 1605633 - 1605633
   Reserved GDT Blocks 1605634 - 1606656
   Data Block Bitmap 1572865 - 1572865
   Inode Bitmap 1572881 - 1572881
   Inode Table 1573408 - 1573919
   Data Blocks 1606657 - 1638399
Free Inodes: 0
Free Blocks: 0
Directories: 125
Checksum: 0x4cc6
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 50
Flags: ['Inode Zeroed']
Blocks: 1638400 - 1671167
Inodes: 409601 - 417792
Layout:
   Data Block Bitmap 1572866 - 1572866
   Inode Bitmap 1572882 - 1572882
   Inode Table 1573920 - 1574431
   Data Blocks 1638400 - 1671167
Free Inodes: 95
Free Blocks: 2205
Directories: 227
Checksum: 0x3b76
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 51
Flags: ['Inode Zeroed']
Blocks: 1671168 - 1703935
Inodes: 417793 - 425984
Layout:
   Data Block Bitmap 1572867 - 1572867
   Inode Bitmap 1572883 - 1572883
   Inode Table 1574432 - 1574943
   Data Blocks 1671168 - 1703935
Free Inodes: 5453
Free Blocks: 26952
Directories: 416
Checksum: 0x1e11
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 52
Flags: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
Blocks: 1703936 - 1736703
Inodes: 425985 - 434176
Layout:
   Data Block Bitmap 1572868 - 1572868
   Inode Bitmap 1572884 - 1572884
   Inode Table 1574944 - 1575455
   Data Blocks 1703936 - 1736703
Free Inodes: 8192
Free Blocks: 32768
Directories: 0
Checksum: 0xbe4e
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 53
Flags: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
Blocks: 1736704 - 1769471
Inodes: 434177 - 442368
Layout:
   Data Block Bitmap 1572869 - 1572869
   Inode Bitmap 1572885 - 1572885
   Inode Table 1575456 - 1575967
   Data Blocks 1736704 - 1769471
Free Inodes: 8192
Free Blocks: 32768
Directories: 0
Checksum: 0x1e95
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 54
Flags: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
Blocks: 1769472 - 1802239
Inodes: 442369 - 450560
Layout:
   Data Block Bitmap 1572870 - 1572870
   Inode Bitmap 1572886 - 1572886
   Inode Table 1575968 - 1576479
   Data Blocks 1769472 - 1802239
Free Inodes: 8192
Free Blocks: 32768
Directories: 0
Checksum: 0xbffb
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 55
Flags: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
Blocks: 1802240 - 1835007
Inodes: 450561 - 458752
Layout:
   Data Block Bitmap 1572871 - 1572871
   Inode Bitmap 1572887 - 1572887
   Inode Table 1576480 - 1576991
   Data Blocks 1802240 - 1835007
Free Inodes: 8192
Free Blocks: 32768
Directories: 0
Checksum: 0x1f20
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 56
Flags: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
Blocks: 1835008 - 1867775
Inodes: 458753 - 466944
Layout:
   Data Block Bitmap 1572872 - 1572872
   Inode Bitmap 1572888 - 1572888
   Inode Table 1576992 - 1577503
   Data Blocks 1835008 - 1867775
Free Inodes: 8192
Free Blocks: 32768
Directories: 0
Checksum: 0xbbf0
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 57
Flags: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
Blocks: 1867776 - 1900543
Inodes: 466945 - 475136
Layout:
   Data Block Bitmap 1572873 - 1572873
   Inode Bitmap 1572889 - 1572889
   Inode Table 1577504 - 1578015
   Data Blocks 1867776 - 1900543
Free Inodes: 8192
Free Blocks: 32768
Directories: 0
Checksum: 0x1b2b
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 58
Flags: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
Blocks: 1900544 - 1933311
Inodes: 475137 - 483328
Layout:
   Data Block Bitmap 1572874 - 1572874
   Inode Bitmap 1572890 - 1572890
   Inode Table 1578016 - 1578527
   Data Blocks 1900544 - 1933311
Free Inodes: 8192
Free Blocks: 32768
Directories: 0
Checksum: 0xba45
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 59
Flags: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
Blocks: 1933312 - 1966079
Inodes: 483329 - 491520
Layout:
   Data Block Bitmap 1572875 - 1572875
   Inode Bitmap 1572891 - 1572891
   Inode Table 1578528 - 1579039
   Data Blocks 1933312 - 1966079
Free Inodes: 8192
Free Blocks: 32768
Directories: 0
Checksum: 0x1a9e
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 60
Flags: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
Blocks: 1966080 - 1998847
Inodes: 491521 - 499712
Layout:
   Data Block Bitmap 1572876 - 1572876
   Inode Bitmap 1572892 - 1572892
   Inode Table 1579040 - 1579551
   Data Blocks 1966080 - 1998847
Free Inodes: 8192
Free Blocks: 32768
Directories: 0
Checksum: 0xb89a
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 61
Flags: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
Blocks: 1998848 - 2031615
Inodes: 499713 - 507904
Layout:
   Data Block Bitmap 1572877 - 1572877
   Inode Bitmap 1572893 - 1572893
   Inode Table 1579552 - 1580063
   Data Blocks 1998848 - 2031615
Free Inodes: 8192
Free Blocks: 32768
Directories: 0
Checksum: 0x1841
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 62
Flags: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
Blocks: 2031616 - 2064383
Inodes: 507905 - 516096
Layout:
   Data Block Bitmap 1572878 - 1572878
   Inode Bitmap 1572894 - 1572894
   Inode Table 1580064 - 1580575
   Data Blocks 2031616 - 2064383
Free Inodes: 8192
Free Blocks: 32768
Directories: 0
Checksum: 0xb92f
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 63
Flags: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
Blocks: 2064384 - 2097151
Inodes: 516097 - 524288
Layout:
   Data Block Bitmap 1572879 - 1572879
   Inode Bitmap 1572895 - 1572895
   Inode Table 1580576 - 1581087
   Data Blocks 2064384 - 2097151
Free Inodes: 8192
Free Blocks: 32768
Directories: 0
Checksum: 0x19f4
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 64
Flags: ['Inode Zeroed']
Blocks: 2097152 - 2129919
Inodes: 524289 - 532480
Layout:
   Data Block Bitmap 2097152 - 2097152
   Inode Bitmap 2097168 - 2097168
   Inode Table 2097184 - 2097695
   Data Blocks 2105376 - 2129919
Free Inodes: 92
Free Blocks: 22168
Directories: 1274
Checksum: 0x30bc
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 65
Flags: ['Inode Zeroed']
Blocks: 2129920 - 2162687
Inodes: 532481 - 540672
Layout:
   Data Block Bitmap 2097153 - 2097153
   Inode Bitmap 2097169 - 2097169
   Inode Table 2097696 - 2098207
   Data Blocks 2129920 - 2162687
Free Inodes: 2957
Free Blocks: 999
Directories: 931
Checksum: 0x9e81
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 66
Flags: ['Inode Uninitialized', 'Inode Zeroed']
Blocks: 2162688 - 2195455
Inodes: 540673 - 548864
Layout:
   Data Block Bitmap 2097154 - 2097154
   Inode Bitmap 2097170 - 2097170
   Inode Table 2098208 - 2098719
   Data Blocks 2162688 - 2195455
Free Inodes: 8192
Free Blocks: 1295
Directories: 0
Checksum: 0xcc48
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 67
Flags: ['Inode Uninitialized', 'Inode Zeroed']
Blocks: 2195456 - 2228223
Inodes: 548865 - 557056
Layout:
   Data Block Bitmap 2097155 - 2097155
   Inode Bitmap 2097171 - 2097171
   Inode Table 2098720 - 2099231
   Data Blocks 2195456 - 2228223
Free Inodes: 8192
Free Blocks: 24047
Directories: 0
Checksum: 0x491f
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 68
Flags: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
Blocks: 2228224 - 2260991
Inodes: 557057 - 565248
Layout:
   Data Block Bitmap 2097156 - 2097156
   Inode Bitmap 2097172 - 2097172
   Inode Table 2099232 - 2099743
   Data Blocks 2228224 - 2260991
Free Inodes: 8192
Free Blocks: 32768
Directories: 0
Checksum: 0xa72f
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 69
Flags: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
Blocks: 2260992 - 2293759
Inodes: 565249 - 573440
Layout:
   Data Block Bitmap 2097157 - 2097157
   Inode Bitmap 2097173 - 2097173
   Inode Table 2099744 - 2100255
   Data Blocks 2260992 - 2293759
Free Inodes: 8192
Free Blocks: 32768
Directories: 0
Checksum: 0x7f4
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 70
Flags: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
Blocks: 2293760 - 2326527
Inodes: 573441 - 581632
Layout:
   Data Block Bitmap 2097158 - 2097158
   Inode Bitmap 2097174 - 2097174
   Inode Table 2100256 - 2100767
   Data Blocks 2293760 - 2326527
Free Inodes: 8192
Free Blocks: 32768
Directories: 0
Checksum: 0xa69a
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 71
Flags: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
Blocks: 2326528 - 2359295
Inodes: 581633 - 589824
Layout:
   Data Block Bitmap 2097159 - 2097159
   Inode Bitmap 2097175 - 2097175
   Inode Table 2100768 - 2101279
   Data Blocks 2326528 - 2359295
Free Inodes: 8192
Free Blocks: 32768
Directories: 0
Checksum: 0x641
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 72
Flags: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
Blocks: 2359296 - 2392063
Inodes: 589825 - 598016
Layout:
   Data Block Bitmap 2097160 - 2097160
   Inode Bitmap 2097176 - 2097176
   Inode Table 2101280 - 2101791
   Data Blocks 2359296 - 2392063
Free Inodes: 8192
Free Blocks: 32768
Directories: 0
Checksum: 0xa291
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 73
Flags: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
Blocks: 2392064 - 2424831
Inodes: 598017 - 606208
Layout:
   Data Block Bitmap 2097161 - 2097161
   Inode Bitmap 2097177 - 2097177
   Inode Table 2101792 - 2102303
   Data Blocks 2392064 - 2424831
Free Inodes: 8192
Free Blocks: 32768
Directories: 0
Checksum: 0x24a
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 74
Flags: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
Blocks: 2424832 - 2457599
Inodes: 606209 - 614400
Layout:
   Data Block Bitmap 2097162 - 2097162
   Inode Bitmap 2097178 - 2097178
   Inode Table 2102304 - 2102815
   Data Blocks 2424832 - 2457599
Free Inodes: 8192
Free Blocks: 32768
Directories: 0
Checksum: 0xa324
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 75
Flags: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
Blocks: 2457600 - 2490367
Inodes: 614401 - 622592
Layout:
   Data Block Bitmap 2097163 - 2097163
   Inode Bitmap 2097179 - 2097179
   Inode Table 2102816 - 2103327
   Data Blocks 2457600 - 2490367
Free Inodes: 8192
Free Blocks: 32768
Directories: 0
Checksum: 0x3ff
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 76
Flags: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
Blocks: 2490368 - 2523135
Inodes: 622593 - 630784
Layout:
   Data Block Bitmap 2097164 - 2097164
   Inode Bitmap 2097180 - 2097180
   Inode Table 2103328 - 2103839
   Data Blocks 2490368 - 2523135
Free Inodes: 8192
Free Blocks: 32768
Directories: 0
Checksum: 0xa1fb
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 77
Flags: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
Blocks: 2523136 - 2555903
Inodes: 630785 - 638976
Layout:
   Data Block Bitmap 2097165 - 2097165
   Inode Bitmap 2097181 - 2097181
   Inode Table 2103840 - 2104351
   Data Blocks 2523136 - 2555903
Free Inodes: 8192
Free Blocks: 32768
Directories: 0
Checksum: 0x120
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 78
Flags: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
Blocks: 2555904 - 2588671
Inodes: 638977 - 647168
Layout:
   Data Block Bitmap 2097166 - 2097166
   Inode Bitmap 2097182 - 2097182
   Inode Table 2104352 - 2104863
   Data Blocks 2555904 - 2588671
Free Inodes: 8192
Free Blocks: 32768
Directories: 0
Checksum: 0xa04e
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 79
Flags: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
Blocks: 2588672 - 2621439
Inodes: 647169 - 655360
Layout:
   Data Block Bitmap 2097167 - 2097167
   Inode Bitmap 2097183 - 2097183
   Inode Table 2104864 - 2105375
   Data Blocks 2588672 - 2621439
Free Inodes: 8192
Free Blocks: 32768
Directories: 0
Checksum: 0x95
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 80
Flags: ['Inode Zeroed']
Blocks: 2621440 - 2654207
Inodes: 655361 - 663552
Layout:
   Data Block Bitmap 2621440 - 2621440
   Inode Bitmap 2621456 - 2621456
   Inode Table 2621472 - 2621983
   Data Blocks 2629664 - 2654207
Free Inodes: 356
Free Blocks: 14137
Directories: 755
Checksum: 0xe72
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 81
Flags: ['Inode Zeroed']
Blocks: 2654208 - 2686975
Inodes: 663553 - 671744
Layout:
   Superblock 2654208 - 2654208
   Group Descriptor Table 2654209 - 2654209
   Reserved GDT Blocks 2654210 - 2655232
   Data Block Bitmap 2621441 - 2621441
   Inode Bitmap 2621457 - 2621457
   Inode Table 2621984 - 2622495
   Data Blocks 2655233 - 2686975
Free Inodes: 0
Free Blocks: 427
Directories: 252
Checksum: 0x3331
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 82
Flags: ['Inode Zeroed']
Blocks: 2686976 - 2719743
Inodes: 671745 - 679936
Layout:
   Data Block Bitmap 2621442 - 2621442
   Inode Bitmap 2621458 - 2621458
   Inode Table 2622496 - 2623007
   Data Blocks 2686976 - 2719743
Free Inodes: 0
Free Blocks: 392
Directories: 247
Checksum: 0xd7ae
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 83
Flags: ['Inode Zeroed']
Blocks: 2719744 - 2752511
Inodes: 679937 - 688128
Layout:
   Data Block Bitmap 2621443 - 2621443
   Inode Bitmap 2621459 - 2621459
   Inode Table 2623008 - 2623519
   Data Blocks 2719744 - 2752511
Free Inodes: 16
Free Blocks: 32204
Directories: 171
Checksum: 0xda90
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 84
Flags: ['Inode Zeroed']
Blocks: 2752512 - 2785279
Inodes: 688129 - 696320
Layout:
   Data Block Bitmap 2621444 - 2621444
   Inode Bitmap 2621460 - 2621460
   Inode Table 2623520 - 2624031
   Data Blocks 2752512 - 2785279
Free Inodes: 3365
Free Blocks: 32768
Directories: 723
Checksum: 0xa968
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 85
Flags: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
Blocks: 2785280 - 2818047
Inodes: 696321 - 704512
Layout:
   Data Block Bitmap 2621445 - 2621445
   Inode Bitmap 2621461 - 2621461
   Inode Table 2624032 - 2624543
   Data Blocks 2785280 - 2818047
Free Inodes: 8192
Free Blocks: 32768
Directories: 0
Checksum: 0x74e2
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 86
Flags: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
Blocks: 2818048 - 2850815
Inodes: 704513 - 712704
Layout:
   Data Block Bitmap 2621446 - 2621446
   Inode Bitmap 2621462 - 2621462
   Inode Table 2624544 - 2625055
   Data Blocks 2818048 - 2850815
Free Inodes: 8192
Free Blocks: 32768
Directories: 0
Checksum: 0xd58c
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 87
Flags: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
Blocks: 2850816 - 2883583
Inodes: 712705 - 720896
Layout:
   Data Block Bitmap 2621447 - 2621447
   Inode Bitmap 2621463 - 2621463
   Inode Table 2625056 - 2625567
   Data Blocks 2850816 - 2883583
Free Inodes: 8192
Free Blocks: 32768
Directories: 0
Checksum: 0x7557
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 88
Flags: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
Blocks: 2883584 - 2916351
Inodes: 720897 - 729088
Layout:
   Data Block Bitmap 2621448 - 2621448
   Inode Bitmap 2621464 - 2621464
   Inode Table 2625568 - 2626079
   Data Blocks 2883584 - 2916351
Free Inodes: 8192
Free Blocks: 32768
Directories: 0
Checksum: 0xd187
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 89
Flags: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
Blocks: 2916352 - 2949119
Inodes: 729089 - 737280
Layout:
   Data Block Bitmap 2621449 - 2621449
   Inode Bitmap 2621465 - 2621465
   Inode Table 2626080 - 2626591
   Data Blocks 2916352 - 2949119
Free Inodes: 8192
Free Blocks: 32768
Directories: 0
Checksum: 0x715c
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 90
Flags: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
Blocks: 2949120 - 2981887
Inodes: 737281 - 745472
Layout:
   Data Block Bitmap 2621450 - 2621450
   Inode Bitmap 2621466 - 2621466
   Inode Table 2626592 - 2627103
   Data Blocks 2949120 - 2981887
Free Inodes: 8192
Free Blocks: 32768
Directories: 0
Checksum: 0xd032
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 91
Flags: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
Blocks: 2981888 - 3014655
Inodes: 745473 - 753664
Layout:
   Data Block Bitmap 2621451 - 2621451
   Inode Bitmap 2621467 - 2621467
   Inode Table 2627104 - 2627615
   Data Blocks 2981888 - 3014655
Free Inodes: 8192
Free Blocks: 32768
Directories: 0
Checksum: 0x70e9
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 92
Flags: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
Blocks: 3014656 - 3047423
Inodes: 753665 - 761856
Layout:
   Data Block Bitmap 2621452 - 2621452
   Inode Bitmap 2621468 - 2621468
   Inode Table 2627616 - 2628127
   Data Blocks 3014656 - 3047423
Free Inodes: 8192
Free Blocks: 32768
Directories: 0
Checksum: 0xd2ed
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 93
Flags: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
Blocks: 3047424 - 3080191
Inodes: 761857 - 770048
Layout:
   Data Block Bitmap 2621453 - 2621453
   Inode Bitmap 2621469 - 2621469
   Inode Table 2628128 - 2628639
   Data Blocks 3047424 - 3080191
Free Inodes: 8192
Free Blocks: 32768
Directories: 0
Checksum: 0x7236
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 94
Flags: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
Blocks: 3080192 - 3112959
Inodes: 770049 - 778240
Layout:
   Data Block Bitmap 2621454 - 2621454
   Inode Bitmap 2621470 - 2621470
   Inode Table 2628640 - 2629151
   Data Blocks 3080192 - 3112959
Free Inodes: 8192
Free Blocks: 32768
Directories: 0
Checksum: 0xd358
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 95
Flags: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
Blocks: 3112960 - 3145727
Inodes: 778241 - 786432
Layout:
   Data Block Bitmap 2621455 - 2621455
   Inode Bitmap 2621471 - 2621471
   Inode Table 2629152 - 2629663
   Data Blocks 3112960 - 3145727
Free Inodes: 8192
Free Blocks: 32768
Directories: 0
Checksum: 0x7383
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 96
Flags: ['Inode Zeroed']
Blocks: 3145728 - 3178495
Inodes: 786433 - 794624
Layout:
   Data Block Bitmap 3145728 - 3145728
   Inode Bitmap 3145744 - 3145744
   Inode Table 3145760 - 3146271
   Data Blocks 3153952 - 3178495
Free Inodes: 1
Free Blocks: 14275
Directories: 388
Checksum: 0xbd00
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 97
Flags: ['Inode Zeroed']
Blocks: 3178496 - 3211263
Inodes: 794625 - 802816
Layout:
   Data Block Bitmap 3145729 - 3145729
   Inode Bitmap 3145745 - 3145745
   Inode Table 3146272 - 3146783
   Data Blocks 3178496 - 3211263
Free Inodes: 0
Free Blocks: 17783
Directories: 217
Checksum: 0xfca7
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 98
Flags: ['Inode Zeroed']
Blocks: 3211264 - 3244031
Inodes: 802817 - 811008
Layout:
   Data Block Bitmap 3145730 - 3145730
   Inode Bitmap 3145746 - 3145746
   Inode Table 3146784 - 3147295
   Data Blocks 3211264 - 3244031
Free Inodes: 0
Free Blocks: 32768
Directories: 227
Checksum: 0xa41b
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 99
Flags: ['Inode Zeroed']
Blocks: 3244032 - 3276799
Inodes: 811009 - 819200
Layout:
   Data Block Bitmap 3145731 - 3145731
   Inode Bitmap 3145747 - 3145747
   Inode Table 3147296 - 3147807
   Data Blocks 3244032 - 3276799
Free Inodes: 662
Free Blocks: 32768
Directories: 1472
Checksum: 0x7d1c
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 100
Flags: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
Blocks: 3276800 - 3309567
Inodes: 819201 - 827392
Layout:
   Data Block Bitmap 3145732 - 3145732
   Inode Bitmap 3145748 - 3145748
   Inode Table 3147808 - 3148319
   Data Blocks 3276800 - 3309567
Free Inodes: 8192
Free Blocks: 32768
Directories: 0
Checksum: 0x4103
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 101
Flags: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
Blocks: 3309568 - 3342335
Inodes: 827393 - 835584
Layout:
   Data Block Bitmap 3145733 - 3145733
   Inode Bitmap 3145749 - 3145749
   Inode Table 3148320 - 3148831
   Data Blocks 3309568 - 3342335
Free Inodes: 8192
Free Blocks: 32768
Directories: 0
Checksum: 0xe1d8
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 102
Flags: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
Blocks: 3342336 - 3375103
Inodes: 835585 - 843776
Layout:
   Data Block Bitmap 3145734 - 3145734
   Inode Bitmap 3145750 - 3145750
   Inode Table 3148832 - 3149343
   Data Blocks 3342336 - 3375103
Free Inodes: 8192
Free Blocks: 32768
Directories: 0
Checksum: 0x40b6
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 103
Flags: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
Blocks: 3375104 - 3407871
Inodes: 843777 - 851968
Layout:
   Data Block Bitmap 3145735 - 3145735
   Inode Bitmap 3145751 - 3145751
   Inode Table 3149344 - 3149855
   Data Blocks 3375104 - 3407871
Free Inodes: 8192
Free Blocks: 32768
Directories: 0
Checksum: 0xe06d
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 104
Flags: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
Blocks: 3407872 - 3440639
Inodes: 851969 - 860160
Layout:
   Data Block Bitmap 3145736 - 3145736
   Inode Bitmap 3145752 - 3145752
   Inode Table 3149856 - 3150367
   Data Blocks 3407872 - 3440639
Free Inodes: 8192
Free Blocks: 32768
Directories: 0
Checksum: 0x44bd
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 105
Flags: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
Blocks: 3440640 - 3473407
Inodes: 860161 - 868352
Layout:
   Data Block Bitmap 3145737 - 3145737
   Inode Bitmap 3145753 - 3145753
   Inode Table 3150368 - 3150879
   Data Blocks 3440640 - 3473407
Free Inodes: 8192
Free Blocks: 32768
Directories: 0
Checksum: 0xe466
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 106
Flags: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
Blocks: 3473408 - 3506175
Inodes: 868353 - 876544
Layout:
   Data Block Bitmap 3145738 - 3145738
   Inode Bitmap 3145754 - 3145754
   Inode Table 3150880 - 3151391
   Data Blocks 3473408 - 3506175
Free Inodes: 8192
Free Blocks: 32768
Directories: 0
Checksum: 0x4508
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 107
Flags: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
Blocks: 3506176 - 3538943
Inodes: 876545 - 884736
Layout:
   Data Block Bitmap 3145739 - 3145739
   Inode Bitmap 3145755 - 3145755
   Inode Table 3151392 - 3151903
   Data Blocks 3506176 - 3538943
Free Inodes: 8192
Free Blocks: 32768
Directories: 0
Checksum: 0xe5d3
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 108
Flags: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
Blocks: 3538944 - 3571711
Inodes: 884737 - 892928
Layout:
   Data Block Bitmap 3145740 - 3145740
   Inode Bitmap 3145756 - 3145756
   Inode Table 3151904 - 3152415
   Data Blocks 3538944 - 3571711
Free Inodes: 8192
Free Blocks: 32768
Directories: 0
Checksum: 0x47d7
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 109
Flags: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
Blocks: 3571712 - 3604479
Inodes: 892929 - 901120
Layout:
   Data Block Bitmap 3145741 - 3145741
   Inode Bitmap 3145757 - 3145757
   Inode Table 3152416 - 3152927
   Data Blocks 3571712 - 3604479
Free Inodes: 8192
Free Blocks: 32768
Directories: 0
Checksum: 0xe70c
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 110
Flags: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
Blocks: 3604480 - 3637247
Inodes: 901121 - 909312
Layout:
   Data Block Bitmap 3145742 - 3145742
   Inode Bitmap 3145758 - 3145758
   Inode Table 3152928 - 3153439
   Data Blocks 3604480 - 3637247
Free Inodes: 8192
Free Blocks: 32768
Directories: 0
Checksum: 0x4662
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 111
Flags: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
Blocks: 3637248 - 3670015
Inodes: 909313 - 917504
Layout:
   Data Block Bitmap 3145743 - 3145743
   Inode Bitmap 3145759 - 3145759
   Inode Table 3153440 - 3153951
   Data Blocks 3637248 - 3670015
Free Inodes: 8192
Free Blocks: 32768
Directories: 0
Checksum: 0xe6b9
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 112
Flags: ['Inode Zeroed']
Blocks: 3670016 - 3702783
Inodes: 917505 - 925696
Layout:
   Data Block Bitmap 3670016 - 3670016
   Inode Bitmap 3670032 - 3670032
   Inode Table 3670048 - 3670559
   Data Blocks 3678240 - 3702783
Free Inodes: 2762
Free Blocks: 22898
Directories: 1644
Checksum: 0x3085
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 113
Flags: ['Inode Uninitialized', 'Inode Zeroed']
Blocks: 3702784 - 3735551
Inodes: 925697 - 933888
Layout:
   Data Block Bitmap 3670017 - 3670017
   Inode Bitmap 3670033 - 3670033
   Inode Table 3670560 - 3671071
   Data Blocks 3702784 - 3735551
Free Inodes: 8192
Free Blocks: 31258
Directories: 0
Checksum: 0xd818
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 114
Flags: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
Blocks: 3735552 - 3768319
Inodes: 933889 - 942080
Layout:
   Data Block Bitmap 3670018 - 3670018
   Inode Bitmap 3670034 - 3670034
   Inode Table 3671072 - 3671583
   Data Blocks 3735552 - 3768319
Free Inodes: 8192
Free Blocks: 32768
Directories: 0
Checksum: 0x30ca
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 115
Flags: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
Blocks: 3768320 - 3801087
Inodes: 942081 - 950272
Layout:
   Data Block Bitmap 3670019 - 3670019
   Inode Bitmap 3670035 - 3670035
   Inode Table 3671584 - 3672095
   Data Blocks 3768320 - 3801087
Free Inodes: 8192
Free Blocks: 32768
Directories: 0
Checksum: 0x9011
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 116
Flags: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
Blocks: 3801088 - 3833855
Inodes: 950273 - 958464
Layout:
   Data Block Bitmap 3670020 - 3670020
   Inode Bitmap 3670036 - 3670036
   Inode Table 3672096 - 3672607
   Data Blocks 3801088 - 3833855
Free Inodes: 8192
Free Blocks: 32768
Directories: 0
Checksum: 0x3215
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 117
Flags: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
Blocks: 3833856 - 3866623
Inodes: 958465 - 966656
Layout:
   Data Block Bitmap 3670021 - 3670021
   Inode Bitmap 3670037 - 3670037
   Inode Table 3672608 - 3673119
   Data Blocks 3833856 - 3866623
Free Inodes: 8192
Free Blocks: 32768
Directories: 0
Checksum: 0x92ce
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 118
Flags: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
Blocks: 3866624 - 3899391
Inodes: 966657 - 974848
Layout:
   Data Block Bitmap 3670022 - 3670022
   Inode Bitmap 3670038 - 3670038
   Inode Table 3673120 - 3673631
   Data Blocks 3866624 - 3899391
Free Inodes: 8192
Free Blocks: 32768
Directories: 0
Checksum: 0x33a0
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 119
Flags: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
Blocks: 3899392 - 3932159
Inodes: 974849 - 983040
Layout:
   Data Block Bitmap 3670023 - 3670023
   Inode Bitmap 3670039 - 3670039
   Inode Table 3673632 - 3674143
   Data Blocks 3899392 - 3932159
Free Inodes: 8192
Free Blocks: 32768
Directories: 0
Checksum: 0x937b
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 120
Flags: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
Blocks: 3932160 - 3964927
Inodes: 983041 - 991232
Layout:
   Data Block Bitmap 3670024 - 3670024
   Inode Bitmap 3670040 - 3670040
   Inode Table 3674144 - 3674655
   Data Blocks 3932160 - 3964927
Free Inodes: 8192
Free Blocks: 32768
Directories: 0
Checksum: 0x37ab
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 121
Flags: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
Blocks: 3964928 - 3997695
Inodes: 991233 - 999424
Layout:
   Data Block Bitmap 3670025 - 3670025
   Inode Bitmap 3670041 - 3670041
   Inode Table 3674656 - 3675167
   Data Blocks 3964928 - 3997695
Free Inodes: 8192
Free Blocks: 32768
Directories: 0
Checksum: 0x9770
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 122
Flags: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
Blocks: 3997696 - 4030463
Inodes: 999425 - 1007616
Layout:
   Data Block Bitmap 3670026 - 3670026
   Inode Bitmap 3670042 - 3670042
   Inode Table 3675168 - 3675679
   Data Blocks 3997696 - 4030463
Free Inodes: 8192
Free Blocks: 32768
Directories: 0
Checksum: 0x361e
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 123
Flags: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
Blocks: 4030464 - 4063231
Inodes: 1007617 - 1015808
Layout:
   Data Block Bitmap 3670027 - 3670027
   Inode Bitmap 3670043 - 3670043
   Inode Table 3675680 - 3676191
   Data Blocks 4030464 - 4063231
Free Inodes: 8192
Free Blocks: 32768
Directories: 0
Checksum: 0x96c5
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 124
Flags: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
Blocks: 4063232 - 4095999
Inodes: 1015809 - 1024000
Layout:
   Data Block Bitmap 3670028 - 3670028
   Inode Bitmap 3670044 - 3670044
   Inode Table 3676192 - 3676703
   Data Blocks 4063232 - 4095999
Free Inodes: 8192
Free Blocks: 32768
Directories: 0
Checksum: 0x34c1
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 125
Flags: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
Blocks: 4096000 - 4128767
Inodes: 1024001 - 1032192
Layout:
   Superblock 4096000 - 4096000
   Group Descriptor Table 4096001 - 4096001
   Reserved GDT Blocks 4096002 - 4097024
   Data Block Bitmap 3670029 - 3670029
   Inode Bitmap 3670045 - 3670045
   Inode Table 3676704 - 3677215
   Data Blocks 4097025 - 4128767
Free Inodes: 8192
Free Blocks: 31743
Directories: 0
Checksum: 0xb129
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 126
Flags: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
Blocks: 4128768 - 4161535
Inodes: 1032193 - 1040384
Layout:
   Data Block Bitmap 3670030 - 3670030
   Inode Bitmap 3670046 - 3670046
   Inode Table 3677216 - 3677727
   Data Blocks 4128768 - 4161535
Free Inodes: 8192
Free Blocks: 32768
Directories: 0
Checksum: 0x3574
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0

Block Group: 127
Flags: ['Inode Uninitialized', 'Inode Zeroed']
Blocks: 4161536 - 4194303
Inodes: 1040385 - 1048576
Layout:
   Data Block Bitmap 3670031 - 3670031
   Inode Bitmap 3670047 - 3670047
   Inode Table 3677728 - 3678239
   Data Blocks 4161536 - 4194303
Free Inodes: 8192
Free Blocks: 32512
Directories: 0
Checksum: 0x9227
Block Bitmap Checksum: 0x0
Inode Bitmap Checksum: 0x0
u64@u64-VirtualBox:~/Desktop$
```
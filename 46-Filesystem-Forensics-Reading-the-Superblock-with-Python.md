#### 46. Filesystem Forensics: Reading the Superblock with Python

###### ```extfs.py```

```python
#!/usr/bin/python
# This is a simple Python script that will
# get metadata from an ext2/3/4 filesystem inside
# of an image file.
#
# Developed for PentesterAcademy by Dr. Phil Polstra

import sys
import os.path
import subprocess
import struct
import time

# these are simple functions to make conversions easier
def getU32(data, offset=0):
   return struct.unpack('<L', data[offset:offset+4])[0]

def getU16(data, offset=0):
   return struct.unpack('<H', data[offset:offset+2])[0]

def getU8(data, offset=0):
   return struct.unpack('B', data[offset:offset+1])[0]

def getU64(data, offset=0):
   return struct.unpack('<Q', data[offset:offset+8])[0]

# this function doesn't unpack the string because it isn't really a number but a UUID
def getU128(data, offset=0):
   return data[offset:offset+16]

def printUuid(data):
  retStr = format(struct.unpack('<Q', data[8:16])[0], 'X').zfill(16) + \
    format(struct.unpack('<Q', data[0:8])[0], 'X').zfill(16)
  return retStr

def getCompatibleFeaturesList(u32):
  retList = []
  if u32 & 0x1:
    retList.append('Directory Preallocate')
  if u32 & 0x2:
    retList.append('Imagic Inodes')
  if u32 & 0x4:
    retList.append('Has Journal')
  if u32 & 0x8:
    retList.append('Extended Attributes')
  if u32 & 0x10:
    retList.append('Resize Inode')
  if u32 & 0x20:
    retList.append('Directory Index')
  if u32 & 0x40:
    retList.append('Lazy Block Groups')
  if u32 & 0x80:
    retList.append('Exclude Inode')
  if u32 & 0x100:
    retList.append('Exclude Bitmap')
  if u32 & 0x200:
    retList.append('Sparse Super 2')
  return retList

def getIncompatibleFeaturesList(u32):
  retList = []
  if u32 & 0x1:
    retList.append('Compression')
  if u32 & 0x2:
    retList.append('Filetype')
  if u32 & 0x4:
    retList.append('Recover')
  if u32 & 0x8:
    retList.append('Journal Device')
  if u32 & 0x10:
    retList.append('Meta Block Groups')
  if u32 & 0x40:
    retList.append('Extents')
  if u32 & 0x80:
    retList.append('64-bit')
  if u32 & 0x100:
    retList.append('Multiple Mount Protection')
  if u32 & 0x200:
    retList.append('Flexible Block Groups')
  if u32 & 0x400:
    retList.append('Extended Attributes in Inodes')
  if u32 & 0x1000:
    retList.append('Directory Data')
  if u32 & 0x2000:
    retList.append('Block Group Metadata Checksum')
  if u32 & 0x4000:
    retList.append('Large Directory')
  if u32 & 0x8000:
    retList.append('Inline Data')
  if u32 & 0x10000:
    retList.append('Encrypted Inodes')
  return retList

def getReadonlyCompatibleFeaturesList(u32):
  retList = []
  if u32 & 0x1:
    retList.append('Sparse Super')
  if u32 & 0x2:
    retList.append('Large File')
  if u32 & 0x4:
    retList.append('Btree Directory')
  if u32 & 0x8:
    retList.append('Huge File')
  if u32 & 0x10:
    retList.append('Group Descriptor Table Checksum')
  if u32 & 0x20:
    retList.append('Directory Nlink')
  if u32 & 0x40:
    retList.append('Extra Isize')
  if u32 & 0x80:
    retList.append('Has Snapshot')
  if u32 & 0x100:
    retList.append('Quota')
  if u32 & 0x200:
    retList.append('Big Alloc')
  if u32 & 0x400:
    retList.append('Metadata Checksum')
  if u32 & 0x800:
    retList.append('Replica')
  if u32 & 0x1000:
    retList.append('Read-only')
  return retList

# This class will parse the data in a superblock
class Superblock():
  def __init__(self, data):
    self.totalInodes = getU32(data)
    self.totalBlocks = getU32(data, 4)
    self.restrictedBlocks = getU32(data, 8)
    self.freeBlocks = getU32(data, 0xc)
    self.freeInodes = getU32(data, 0x10)
    self.firstDataBlock = getU32(data, 0x14) # normally 0 unless block size is <4k
    self.blockSize = 2^(10 + getU32(data, 0x18)) # block size is 1024 * 2^(whatever is in this field)
    self.clusterSize = 2^(getU32(data, 0x1c)) # only used if bigalloc feature enabled
    self.blocksPerGroup = getU32(data, 0x20)
    self.clustersPerGroup = getU32(data, 0x24) # only used if bigalloc feature enabled
    self.inodesPerGroup = getU32(data, 0x28)
    self.mountTime = time.gmtime(getU32(data, 0x2c))
    self.writeTime = time.gmtime(getU32(data, 0x30))
    self.mountCount = getU16(data, 0x34) # mounts since last fsck
    self.maxMountCount = getU16(data, 0x36) # mounts between fsck
    self.magic = getU16(data, 0x38) # should be 0xef53
    self.state = getU16(data, 0x3a) #0001/0002/0004 = cleanly unmounted/errors/orphans
    self.errors = getU16(data, 0x3c) # when errors 1/2/3 continue/read-only/panic
    self.minorRevision = getU16(data, 0x3e)
    self.lastCheck = time.gmtime(getU32(data, 0x40)) # last fsck time
    self.checkInterval = getU32(data, 0x44) # seconds between checks
    self.creatorOs = getU32(data, 0x48) # 0/1/2/3/4 Linux/Hurd/Masix/FreeBSD/Lites
    self.revisionLevel = getU32(data, 0x4c) # 0/1 original/v2 with dynamic inode sizes
    self.defaultResUid = getU16(data, 0x50) # UID for reserved blocks
    self.defaultRegGid = getU16(data, 0x52) # GID for reserved blocks
    # for Ext4 dynamic revisionLevel superblocks only!
    self.firstInode = getU32(data, 0x54) # first non-reserved inode
    self.inodeSize = getU16(data, 0x58) # inode size in bytes
    self.blockGroupNumber = getU16(data, 0x5a) # block group this superblock is in
    self.compatibleFeatures = getU32(data, 0x5c) # compatible features
    self.compatibleFeaturesList = getCompatibleFeaturesList(self.compatibleFeatures)
    self.incompatibleFeatures = getU32(data, 0x60) #incompatible features
    self.incompatibleFeaturesList = getIncompatibleFeaturesList(self.incompatibleFeatures)
    self.readOnlyCompatibleFeatures = getU32(data, 0x64) # read-only compatible features
    self.readOnlyCompatibleFeaturesList = getReadonlyCompatibleFeaturesList(self.readOnlyCompatibleFeatures)
    self.uuid = getU128(data, 0x68) #UUID for volume left as a packed string
    self.volumeName = data[0x78:0x88].split("\x00")[0] # volume name - likely empty
    self.lastMounted = data[0x88:0xc8].split("\x00")[0] # directory where last mounted
    self.algorithmUsageBitmap = getU32(data, 0xc8) # used with compression
    self.preallocBlocks = getU8(data, 0xcc) # not used in ext4
    self.preallocDirBlock = getU8(data, 0xcd) #only used with DIR_PREALLOC feature
    self.reservedGdtBlocks = getU16(data, 0xce) # blocks reserved for future expansion
    self.journalUuid = getU128(data, 0xd0) # UUID of journal superblock
    self.journalInode = getU32(data, 0xe0) # inode number of journal file
    self.journalDev = getU32(data, 0xe4) # device number for journal if external journal used
    self.lastOrphan = getU32(data, 0xe8) # start of list of orphaned inodes to delete
    self.hashSeed = []
    self.hashSeed.append(getU32(data, 0xec)) # htree hash seed
    self.hashSeed.append(getU32(data, 0xf0))
    self.hashSeed.append(getU32(data, 0xf4))
    self.hashSeed.append(getU32(data, 0xf8))
    self.hashVersion = getU8(data, 0xfc) # 0/1/2/3/4/5 legacy/half MD4/tea/u-legacy/u-half MD4/u-Tea
    self.journalBackupType = getU8(data, 0xfd)
    self.descriptorSize = getU16(data, 0xfe) # group descriptor size if 64-bit feature enabled
    self.defaultMountOptions = getU32(data, 0x100)
    self.firstMetaBlockGroup = getU32(data, 0x104) # only used with meta bg feature
    self.mkfsTime = time.gmtime(getU32(data, 0x108)) # when was the filesystem created
    self.journalBlocks = []
    for i in range(0, 17): # backup copy of journal inodes and size in last two elements
      self.journalBlocks.append(getU32(data, 0x10c + i*4))
    # for 64-bit mode only
    self.blockCountHi = getU32(data, 0x150)
    self.reservedBlockCountHi = getU32(data, 0x154)
    self.freeBlocksHi = getU32(data, 0x158)
    self.minInodeExtraSize = getU16(data, 0x15c) # all inodes such have at least this much space
    self.wantInodeExtraSize = getU16(data, 0x15e) # new inodes should reserve this many bytes
    self.miscFlags = getU32(data, 0x160) #1/2/4 signed hash/unsigned hash/test code
    self.raidStride = getU16(data, 0x164) # logical blocks read from disk in RAID before moving to next disk
    self.mmpInterval = getU16(data, 0x166) # seconds to wait between multi-mount checks
    self.mmpBlock = getU64(data, 0x168) # block number for MMP data
    self.raidStripeWidth = getU32(data, 0x170) # how many blocks read/write till back on this disk
    self.groupsPerFlex = 2^(getU8(data, 0x174)) # groups per flex group
    self.metadataChecksumType = getU8(data, 0x175) # should be 1 for crc32
    self.reservedPad = getU16(data, 0x176) # should be zeroes
    self.kilobytesWritten = getU64(data, 0x178) # kilobytes written for all time
    self.snapshotInode = getU32(data, 0x180) # inode of active snapshot
    self.snapshotId = getU32(data, 0x184) # id of the active snapshot
    self.snapshotReservedBlocks = getU64(data, 0x188) # blocks reserved for snapshot
    self.snapshotList = getU32(data, 0x190) # inode number of head of snapshot list
    self.errorCount = getU32(data, 0x194)
    self.firstErrorTime = time.gmtime(getU32(data, 0x198)) # time first error detected
    self.firstErrorInode = getU32(data, 0x19c) # guilty inode
    self.firstErrorBlock = getU64(data, 0x1a0) # guilty block
    self.firstErrorFunction = data[0x1a8:0x1c8].split("\x00")[0] # guilty function
    self.firstErrorLine = getU32(data, 0x1c8) # line number where error occurred
    self.lastErrorTime = time.gmtime(getU32(data, 0x1cc)) # time last error detected
    self.lastErrorInode = getU32(data, 0x1d0) # guilty inode
    self.lastErrorLine = getU32(data, 0x1d4) # line number where error occurred
    self.lastErrorBlock = getU64(data, 0x1d8) # guilty block
    self.lastErrorFunction = data[0x1e0:0x200].split("\x00")[0] # guilty function
    self.mountOptions = data[0x200:0x240].split("\x00")[0] # mount options in null-terminated string
    self.userQuotaInode = getU32(data, 0x240) # inode of user quota file
    self.groupQuotaInode = getU32(data, 0x244) # inode of group quota file
    self.overheadBlocks = getU32(data, 0x248) # should be zero
    self.backupBlockGroups = [getU32(data, 0x24c), getU32(data, 0x250)] # super sparse 2 only
    self.encryptionAlgorithms = []
    for i in range(0, 4):
      self.encryptionAlgorithms.append(getU32(data, 0x254 + i*4))
    self.checksum = getU32(data, 0x3fc)

  def printState(self):
    #0001/0002/0004 = cleanly unmounted/errors/orphans
    retVal = "Unknown"
    if self.state == 1:
      retVal = "Cleanly unmounted"
    elif self.state == 2:
      retVal = "Errors detected"
    elif self.state == 4:
      retVal = "Orphans being recovered"
    return retVal

  def printErrorBehavior(self):
    # when errors 1/2/3 continue/read-only/panic
    retVal = "Unknown"
    if self.errors == 1:
      retVal = "Continue"
    elif self.errors == 2:
      retVal = "Remount read-only"
    elif self.errors == 3:
      retVal = "Kernel panic"
    return retVal

  def printCreator(self):
    # 0/1/2/3/4 Linux/Hurd/Masix/FreeBSD/Lites
    retVal = "Unknown"
    if self.creatorOs == 0:
      retVal = "Linux"
    elif self.creatorOs == 1:
      retVal = "Hurd"
    elif self.creatorOs == 2:
      retVal = "Masix"
    elif self.creatorOs == 3:
      retVal = "FreeBSD"
    elif self.creatorOs == 4:
      retVal = "Lites"
    return retVal

  def printHashAlgorithm(self):
    # 0/1/2/3/4/5 legacy/half MD4/tea/u-legacy/u-half MD4/u-Tea
    retVal = "Unknown"
    if self.hashVersion == 0:
      retVal = "Legacy"
    elif self.hashVersion == 1:
      retVal = "Half MD4"
    elif self.hashVersion == 2:
      retVal = "Tea"
    elif self.hashVersion == 3:
      retVal = "Unsigned Legacy"
    elif self.hashVersion == 4:
      retVal = "Unsigned Half MD4"
    elif self.hashVersion == 5:
      retVal = "Unsigned Tea"
    return retVal

  def printEncryptionAlgorithms(self):
    encList = []
    for v in self.encryptionAlgorithms:
      if v == 1:
        encList.append('256-bit AES in XTS mode')
      elif v == 2:
        encList.append('256-bit AES in GCM mode')
      elif v == 3:
        encList.append('256-bit AES in CBC mode')
      elif v == 0:
        pass
      else:
        encList.append('Unknown')
    return encList

  def prettyPrint(self):
    for k, v in self.__dict__.iteritems() :
      if k == 'mountTime' or k == 'writeTime' or \
         k == 'lastCheck' or k == 'mkfsTime' or \
         k == 'firstErrorTime' or k == 'lastErrorTime' :
        print k+":", time.asctime(v)
      elif k == 'state':
        print k+":", self.printState()
      elif k == 'errors':
        print k+":", self.printErrorBehavior()
      elif k == 'uuid' or k == 'journalUuid':
        print k+":", printUuid(v)
      elif k == 'creatorOs':
        print k+":", self.printCreator()
      elif k == 'hashVersion':
        print k+":", self.printHashAlgorithm()
      elif k == 'encryptionAlgorithms':
        print k+":", self.printEncryptionAlgorithms()
      else:
        print k+":", v

def usage():
   print("usage " + sys.argv[0] + " <image file> <offset in sectors>\nReads superblock from an image file")
   exit(1)

def main():
  if len(sys.argv) < 3:
     usage()

  # read first sector
  if not os.path.isfile(sys.argv[1]):
     print("File " + sys.argv[1] + " cannot be openned for reading")
     exit(1)
  with open(sys.argv[1], 'rb') as f:
    f.seek(1024 + int(sys.argv[2]) * 512)
    sbRaw = str(f.read(1024))
  sb = Superblock(sbRaw)
  sb.prettyPrint()


if __name__ == "__main__":
   main()
```

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

###### Read superblock from an image file

```sh
u64@u64-VirtualBox:~/Desktop$ ./extfs.py
usage ./extfs.py <image file> <offset in sectors>
Reads superblock from an image file
u64@u64-VirtualBox:~/Desktop$
```

```sh
u64@u64-VirtualBox:~/Desktop$ ./extfs.py 2015-3-9.img 2048
compatibleFeaturesList: ['Has Journal', 'Extended Attributes', 'Resize Inode', 'Directory Index']
snapshotReservedBlocks: 0
defaultMountOptions: 12
firstErrorBlock: 0
algorithmUsageBitmap: 0
freeBlocks: 3042264
uuid: 6D3257CCE44C5499D141D359183193C1
snapshotList: 0
blockSize: 14
blocksPerGroup: 32768
readOnlyCompatibleFeaturesList: ['Sparse Super', 'Large File', 'Huge File', 'Group Descriptor Table Checksum', 'Directory Nlink', 'Extra Isize']
snapshotInode: 0
groupsPerFlex: 6
blockCountHi: 0
backupBlockGroups: [0, 0]
lastMounted: /
magic: 61267
totalInodes: 1048576
lastOrphan: 0
defaultResUid: 0
mmpInterval: 0
mkfsTime: Fri Mar  6 03:37:57 2015
errorCount: 0
errors: Continue
descriptorSize: 0
overheadBlocks: 0
reservedBlockCountHi: 0
state: Cleanly unmounted
kilobytesWritten: 7350973
lastErrorLine: 0
wantInodeExtraSize: 28
mountCount: 14
firstInode: 11
groupQuotaInode: 0
checksum: 0
mmpBlock: 0
lastErrorFunction:
miscFlags: 1
freeBlocksHi: 0
firstMetaBlockGroup: 0
readOnlyCompatibleFeatures: 123
lastErrorInode: 0
inodesPerGroup: 8192
encryptionAlgorithms: []
mountTime: Thu Mar 12 23:29:39 2015
mountOptions:
reservedPad: 0
snapshotId: 0
incompatibleFeaturesList: ['Filetype', 'Extents', 'Flexible Block Groups']
journalInode: 8
preallocDirBlock: 0
journalBackupType: 1
clustersPerGroup: 32768
raidStripeWidth: 0
revisionLevel: 1
blockGroupNumber: 0
lastErrorTime: Thu Jan  1 00:00:00 1970
firstErrorFunction:
creatorOs: Linux
journalDev: 0
hashVersion: Half MD4
inodeSize: 256
clusterSize: 0
writeTime: Thu Mar 12 23:30:28 2015
freeInodes: 863973
incompatibleFeatures: 578
firstDataBlock: 0
hashSeed: [2344286409, 2756545686, 3468101558, 1457826801]
reservedGdtBlocks: 1023
checkInterval: 0
totalBlocks: 4194048
volumeName:
lastCheck: Fri Mar  6 03:37:57 2015
raidStride: 0
lastErrorBlock: 0
preallocBlocks: 0
minInodeExtraSize: 28
defaultRegGid: 0
journalUuid: 00000000000000000000000000000000
journalBlocks: [193290, 4, 0, 0, 32767, 1606657, 32767, 1, 1639424, 0, 0, 0, 0, 0, 0, 0, 134217728]
compatibleFeatures: 60
firstErrorTime: Thu Jan  1 00:00:00 1970
firstErrorLine: 0
userQuotaInode: 0
restrictedBlocks: 209702
metadataChecksumType: 0
firstErrorInode: 0
minorRevision: 0
maxMountCount: 65535
u64@u64-VirtualBox:~/Desktop$
```
#### 47. Filesystem Analysis: Reading the Block Group Descriptors with Python

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
    self.blockSize = pow(2, 10 + getU32(data, 0x18)) # block size is 1024 * 2^(whatever is in this field)
    self.clusterSize = pow(2, getU32(data, 0x1c)) # only used if bigalloc feature enabled
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
    self.groupsPerFlex = pow(2, getU8(data, 0x174)) # groups per flex group
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

  def blockGroups(self):
    bg = self.totalBlocks / self.blocksPerGroup
    if self.totalBlocks % self.blocksPerGroup != 0:
      bg += 1
    return bg

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
    for k, v in sorted(self.__dict__.iteritems()) :
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

class GroupDescriptor():
  def __init__(self, data, wide=False):
	self.blockBitmapLo=getU32(data)	        #/* Blocks bitmap block */
	self.inodeBitmapLo=getU32(data, 4)	#/* Inodes bitmap block */
	self.inodeTableLo=getU32(data, 8)	#/* Inodes table block */
	self.freeBlocksCountLo=getU16(data, 0xc)#/* Free blocks count */
	self.freeInodesCountLo=getU16(data, 0xe)#/* Free inodes count */
	self.usedDirsCountLo=getU16(data, 0x10)	#/* Directories count */
	self.flags=getU16(data, 0x12)		#/* EXT4_BG_flags (INODE_UNINIT, etc) */
	self.flagsList = self.printFlagList()
        self.excludeBitmapLo=getU32(data, 0x14)   #/* Exclude bitmap for snapshots */
	self.blockBitmapCsumLo=getU16(data, 0x18) #/* crc32c(s_uuid+grp_num+bbitmap) LE */
	self.inodeBitmapCsumLo=getU16(data, 0x1a) #/* crc32c(s_uuid+grp_num+ibitmap) LE */
	self.itableUnusedLo=getU16(data, 0x1c)	#/* Unused inodes count */
	self.checksum=getU16(data, 0x1e)		#/* crc16(sb_uuid+group+desc) */
        if wide==True:      	
          self.blockBitmapHi=getU32(data, 0x20)	#/* Blocks bitmap block MSB */
	  self.inodeBitmapHi=getU32(data, 0x24)	#/* Inodes bitmap block MSB */
	  self.inodeTableHi=getU32(data, 0x28)	#/* Inodes table block MSB */
	  self.freeBlocksCountHi=getU16(data, 0x2c) #/* Free blocks count MSB */
	  self.freeInodesCountHi=getU16(data, 0x2e) #/* Free inodes count MSB */
	  self.usedDirsCountHi=getU16(data, 0x30)	#/* Directories count MSB */
	  self.itableUnusedHi=getU16(data, 0x32)    #/* Unused inodes count MSB */
	  self.excludeBitmapHi=getU32(data, 0x34)   #/* Exclude bitmap block MSB */
	  self.blockBitmapCsumHi=getU16(data, 0x38)#/* crc32c(s_uuid+grp_num+bbitmap) BE */
	  self.inodeBitmapCsumHi=getU16(data, 0x3a)#/* crc32c(s_uuid+grp_num+ibitmap) BE */
	  self.reserved=getU32(data, 0x3c)

  def printFlagList(self):
    flagList = []
    if self.flags & 0x1: #inode table and bitmap are not initialized (EXT4_BG_INODE_UNINIT).
      flagList.append('Inode Uninitialized')
    if self.flags & 0x2: #block bitmap is not initialized (EXT4_BG_BLOCK_UNINIT).
      flagList.append('Block Uninitialized')
    if self.flags & 0x4: #inode table is zeroed (EXT4_BG_INODE_ZEROED).
      flagList.append('Inode Zeroed')
    return flagList

  def prettyPrint(self):
    for k, v in sorted(self.__dict__.iteritems()) :
      print k+":", v

class ExtMetadata():
  def __init__(self, filename, offset):
    # read first sector
    if not os.path.isfile(sys.argv[1]):
       print("File " + str(filename) + " cannot be openned for reading")
       exit(1)
    with open(str(filename), 'rb') as f:
      f.seek(1024 + int(offset) * 512)
      sbRaw = str(f.read(1024))
    self.superblock = Superblock(sbRaw)  

    # read block group descriptors
    self.blockGroups = self.superblock.blockGroups()
    if self.superblock.descriptorSize != 0:
      self.wideBlockGroups = True
      self.blockGroupDescriptorSize = 64
    else:
      self.wideBlockGroups = False
      self.blockGroupDescriptorSize = 32
    # read in group descriptors starting in block 1
    with open(str(filename), 'rb') as f:
      f.seek(int(offset) * 512 + self.superblock.blockSize)
      bgdRaw = str(f.read(self.blockGroups * self.blockGroupDescriptorSize))
  
    self.bgdList = []
    for i in range(0, self.blockGroups):
      bgd = GroupDescriptor(bgdRaw[i * self.blockGroupDescriptorSize:], self.wideBlockGroups) 
      self.bgdList.append(bgd)

  def prettyPrint(self):
    self.superblock.prettyPrint()
    i = 0
    for bgd in self.bgdList:
      print "Block group:" + str(i)
      bgd.prettyPrint()
      print ""
      i += 1
      

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
  emd = ExtMetadata(sys.argv[1], sys.argv[2])
  emd.prettyPrint()

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

###### Read superblock from an image file using ```extfs.py```

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
Block group:0
blockBitmapCsumLo: 0
blockBitmapLo: 1025
checksum: 45218
excludeBitmapLo: 0
flags: 4
flagsList: ['Inode Zeroed']
freeBlocksCountLo: 22866
freeInodesCountLo: 668
inodeBitmapCsumLo: 0
inodeBitmapLo: 1041
inodeTableLo: 1057
itableUnusedLo: 0
usedDirsCountLo: 370

Block group:1
blockBitmapCsumLo: 0
blockBitmapLo: 1026
checksum: 12938
excludeBitmapLo: 0
flags: 4
flagsList: ['Inode Zeroed']
freeBlocksCountLo: 1434
freeInodesCountLo: 7521
inodeBitmapCsumLo: 0
inodeBitmapLo: 1042
inodeTableLo: 1569
itableUnusedLo: 7521
usedDirsCountLo: 2

Block group:2
blockBitmapCsumLo: 0
blockBitmapLo: 1027
checksum: 59552
excludeBitmapLo: 0
flags: 5
flagsList: ['Inode Uninitialized', 'Inode Zeroed']
freeBlocksCountLo: 2119
freeInodesCountLo: 8192
inodeBitmapCsumLo: 0
inodeBitmapLo: 1043
inodeTableLo: 2081
itableUnusedLo: 8192
usedDirsCountLo: 0

Block group:3
blockBitmapCsumLo: 0
blockBitmapLo: 1028
checksum: 60257
excludeBitmapLo: 0
flags: 5
flagsList: ['Inode Uninitialized', 'Inode Zeroed']
freeBlocksCountLo: 23816
freeInodesCountLo: 8192
inodeBitmapCsumLo: 0
inodeBitmapLo: 1044
inodeTableLo: 2593
itableUnusedLo: 8192
usedDirsCountLo: 0

Block group:4
blockBitmapCsumLo: 0
blockBitmapLo: 1029
checksum: 19180
excludeBitmapLo: 0
flags: 5
flagsList: ['Inode Uninitialized', 'Inode Zeroed']
freeBlocksCountLo: 5402
freeInodesCountLo: 8192
inodeBitmapCsumLo: 0
inodeBitmapLo: 1045
inodeTableLo: 3105
itableUnusedLo: 8192
usedDirsCountLo: 0

Block group:5
blockBitmapCsumLo: 0
blockBitmapLo: 1030
checksum: 32511
excludeBitmapLo: 0
flags: 5
flagsList: ['Inode Uninitialized', 'Inode Zeroed']
freeBlocksCountLo: 0
freeInodesCountLo: 8192
inodeBitmapCsumLo: 0
inodeBitmapLo: 1046
inodeTableLo: 3617
itableUnusedLo: 8192
usedDirsCountLo: 0

Block group:6
blockBitmapCsumLo: 0
blockBitmapLo: 1031
checksum: 710
excludeBitmapLo: 0
flags: 5
flagsList: ['Inode Uninitialized', 'Inode Zeroed']
freeBlocksCountLo: 12925
freeInodesCountLo: 8192
inodeBitmapCsumLo: 0
inodeBitmapLo: 1047
inodeTableLo: 4129
itableUnusedLo: 8192
usedDirsCountLo: 0

Block group:7
blockBitmapCsumLo: 0
blockBitmapLo: 1032
checksum: 40417
excludeBitmapLo: 0
flags: 5
flagsList: ['Inode Uninitialized', 'Inode Zeroed']
freeBlocksCountLo: 6248
freeInodesCountLo: 8192
inodeBitmapCsumLo: 0
inodeBitmapLo: 1048
inodeTableLo: 4641
itableUnusedLo: 8192
usedDirsCountLo: 0

Block group:8
blockBitmapCsumLo: 0
blockBitmapLo: 1033
checksum: 54104
excludeBitmapLo: 0
flags: 5
flagsList: ['Inode Uninitialized', 'Inode Zeroed']
freeBlocksCountLo: 15
freeInodesCountLo: 8192
inodeBitmapCsumLo: 0
inodeBitmapLo: 1049
inodeTableLo: 5153
itableUnusedLo: 8192
usedDirsCountLo: 0

Block group:9
blockBitmapCsumLo: 0
blockBitmapLo: 1034
checksum: 39972
excludeBitmapLo: 0
flags: 5
flagsList: ['Inode Uninitialized', 'Inode Zeroed']
freeBlocksCountLo: 8812
freeInodesCountLo: 8192
inodeBitmapCsumLo: 0
inodeBitmapLo: 1050
inodeTableLo: 5665
itableUnusedLo: 8192
usedDirsCountLo: 0

Block group:10
blockBitmapCsumLo: 0
blockBitmapLo: 1035
checksum: 26917
excludeBitmapLo: 0
flags: 5
flagsList: ['Inode Uninitialized', 'Inode Zeroed']
freeBlocksCountLo: 5269
freeInodesCountLo: 8192
inodeBitmapCsumLo: 0
inodeBitmapLo: 1051
inodeTableLo: 6177
itableUnusedLo: 8192
usedDirsCountLo: 0

Block group:11
blockBitmapCsumLo: 0
blockBitmapLo: 1036
checksum: 45527
excludeBitmapLo: 0
flags: 5
flagsList: ['Inode Uninitialized', 'Inode Zeroed']
freeBlocksCountLo: 13665
freeInodesCountLo: 8192
inodeBitmapCsumLo: 0
inodeBitmapLo: 1052
inodeTableLo: 6689
itableUnusedLo: 8192
usedDirsCountLo: 0

Block group:12
blockBitmapCsumLo: 0
blockBitmapLo: 1037
checksum: 45429
excludeBitmapLo: 0
flags: 5
flagsList: ['Inode Uninitialized', 'Inode Zeroed']
freeBlocksCountLo: 3079
freeInodesCountLo: 8192
inodeBitmapCsumLo: 0
inodeBitmapLo: 1053
inodeTableLo: 7201
itableUnusedLo: 8192
usedDirsCountLo: 0

Block group:13
blockBitmapCsumLo: 0
blockBitmapLo: 1038
checksum: 17623
excludeBitmapLo: 0
flags: 5
flagsList: ['Inode Uninitialized', 'Inode Zeroed']
freeBlocksCountLo: 6681
freeInodesCountLo: 8192
inodeBitmapCsumLo: 0
inodeBitmapLo: 1054
inodeTableLo: 7713
itableUnusedLo: 8192
usedDirsCountLo: 0

Block group:14
blockBitmapCsumLo: 0
blockBitmapLo: 1039
checksum: 23953
excludeBitmapLo: 0
flags: 5
flagsList: ['Inode Uninitialized', 'Inode Zeroed']
freeBlocksCountLo: 2717
freeInodesCountLo: 8192
inodeBitmapCsumLo: 0
inodeBitmapLo: 1055
inodeTableLo: 8225
itableUnusedLo: 8192
usedDirsCountLo: 0

Block group:15
blockBitmapCsumLo: 0
blockBitmapLo: 1040
checksum: 2921
excludeBitmapLo: 0
flags: 5
flagsList: ['Inode Uninitialized', 'Inode Zeroed']
freeBlocksCountLo: 3104
freeInodesCountLo: 8192
inodeBitmapCsumLo: 0
inodeBitmapLo: 1056
inodeTableLo: 8737
itableUnusedLo: 8192
usedDirsCountLo: 0

Block group:16
blockBitmapCsumLo: 0
blockBitmapLo: 524288
checksum: 9083
excludeBitmapLo: 0
flags: 4
flagsList: ['Inode Zeroed']
freeBlocksCountLo: 19399
freeInodesCountLo: 0
inodeBitmapCsumLo: 0
inodeBitmapLo: 524304
inodeTableLo: 524320
itableUnusedLo: 0
usedDirsCountLo: 1016

Block group:17
blockBitmapCsumLo: 0
blockBitmapLo: 524289
checksum: 54707
excludeBitmapLo: 0
flags: 4
flagsList: ['Inode Zeroed']
freeBlocksCountLo: 8
freeInodesCountLo: 0
inodeBitmapCsumLo: 0
inodeBitmapLo: 524305
inodeTableLo: 524832
itableUnusedLo: 0
usedDirsCountLo: 931

Block group:18
blockBitmapCsumLo: 0
blockBitmapLo: 524290
checksum: 3983
excludeBitmapLo: 0
flags: 4
flagsList: ['Inode Zeroed']
freeBlocksCountLo: 905
freeInodesCountLo: 0
inodeBitmapCsumLo: 0
inodeBitmapLo: 524306
inodeTableLo: 525344
itableUnusedLo: 0
usedDirsCountLo: 382

Block group:19
blockBitmapCsumLo: 0
blockBitmapLo: 524291
checksum: 10835
excludeBitmapLo: 0
flags: 4
flagsList: ['Inode Zeroed']
freeBlocksCountLo: 2266
freeInodesCountLo: 2278
inodeBitmapCsumLo: 0
inodeBitmapLo: 524307
inodeTableLo: 525856
itableUnusedLo: 2273
usedDirsCountLo: 103

Block group:20
blockBitmapCsumLo: 0
blockBitmapLo: 524292
checksum: 33886
excludeBitmapLo: 0
flags: 5
flagsList: ['Inode Uninitialized', 'Inode Zeroed']
freeBlocksCountLo: 5925
freeInodesCountLo: 8192
inodeBitmapCsumLo: 0
inodeBitmapLo: 524308
inodeTableLo: 526368
itableUnusedLo: 8192
usedDirsCountLo: 0

Block group:21
blockBitmapCsumLo: 0
blockBitmapLo: 524293
checksum: 60363
excludeBitmapLo: 0
flags: 5
flagsList: ['Inode Uninitialized', 'Inode Zeroed']
freeBlocksCountLo: 7842
freeInodesCountLo: 8192
inodeBitmapCsumLo: 0
inodeBitmapLo: 524309
inodeTableLo: 526880
itableUnusedLo: 8192
usedDirsCountLo: 0

Block group:22
blockBitmapCsumLo: 0
blockBitmapLo: 524294
checksum: 15053
excludeBitmapLo: 0
flags: 5
flagsList: ['Inode Uninitialized', 'Inode Zeroed']
freeBlocksCountLo: 15276
freeInodesCountLo: 8192
inodeBitmapCsumLo: 0
inodeBitmapLo: 524310
inodeTableLo: 527392
itableUnusedLo: 8192
usedDirsCountLo: 0

Block group:23
blockBitmapCsumLo: 0
blockBitmapLo: 524295
checksum: 32557
excludeBitmapLo: 0
flags: 5
flagsList: ['Inode Uninitialized', 'Inode Zeroed']
freeBlocksCountLo: 4162
freeInodesCountLo: 8192
inodeBitmapCsumLo: 0
inodeBitmapLo: 524311
inodeTableLo: 527904
itableUnusedLo: 8192
usedDirsCountLo: 0

Block group:24
blockBitmapCsumLo: 0
blockBitmapLo: 524296
checksum: 33239
excludeBitmapLo: 0
flags: 5
flagsList: ['Inode Uninitialized', 'Inode Zeroed']
freeBlocksCountLo: 11875
freeInodesCountLo: 8192
inodeBitmapCsumLo: 0
inodeBitmapLo: 524312
inodeTableLo: 528416
itableUnusedLo: 8192
usedDirsCountLo: 0

Block group:25
blockBitmapCsumLo: 0
blockBitmapLo: 524297
checksum: 9399
excludeBitmapLo: 0
flags: 5
flagsList: ['Inode Uninitialized', 'Inode Zeroed']
freeBlocksCountLo: 5195
freeInodesCountLo: 8192
inodeBitmapCsumLo: 0
inodeBitmapLo: 524313
inodeTableLo: 528928
itableUnusedLo: 8192
usedDirsCountLo: 0

Block group:26
blockBitmapCsumLo: 0
blockBitmapLo: 524298
checksum: 37829
excludeBitmapLo: 0
flags: 5
flagsList: ['Inode Uninitialized', 'Inode Zeroed']
freeBlocksCountLo: 4229
freeInodesCountLo: 8192
inodeBitmapCsumLo: 0
inodeBitmapLo: 524314
inodeTableLo: 529440
itableUnusedLo: 8192
usedDirsCountLo: 0

Block group:27
blockBitmapCsumLo: 0
blockBitmapLo: 524299
checksum: 23903
excludeBitmapLo: 0
flags: 5
flagsList: ['Inode Uninitialized', 'Inode Zeroed']
freeBlocksCountLo: 3245
freeInodesCountLo: 8192
inodeBitmapCsumLo: 0
inodeBitmapLo: 524315
inodeTableLo: 529952
itableUnusedLo: 8192
usedDirsCountLo: 0

Block group:28
blockBitmapCsumLo: 0
blockBitmapLo: 524300
checksum: 43341
excludeBitmapLo: 0
flags: 5
flagsList: ['Inode Uninitialized', 'Inode Zeroed']
freeBlocksCountLo: 17413
freeInodesCountLo: 8192
inodeBitmapCsumLo: 0
inodeBitmapLo: 524316
inodeTableLo: 530464
itableUnusedLo: 8192
usedDirsCountLo: 0

Block group:29
blockBitmapCsumLo: 0
blockBitmapLo: 524301
checksum: 65133
excludeBitmapLo: 0
flags: 7
flagsList: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
freeBlocksCountLo: 32768
freeInodesCountLo: 8192
inodeBitmapCsumLo: 0
inodeBitmapLo: 524317
inodeTableLo: 530976
itableUnusedLo: 8192
usedDirsCountLo: 0

Block group:30
blockBitmapCsumLo: 0
blockBitmapLo: 524302
checksum: 24323
excludeBitmapLo: 0
flags: 7
flagsList: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
freeBlocksCountLo: 32768
freeInodesCountLo: 8192
inodeBitmapCsumLo: 0
inodeBitmapLo: 524318
inodeTableLo: 531488
itableUnusedLo: 8192
usedDirsCountLo: 0

Block group:31
blockBitmapCsumLo: 0
blockBitmapLo: 524303
checksum: 65496
excludeBitmapLo: 0
flags: 7
flagsList: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
freeBlocksCountLo: 32768
freeInodesCountLo: 8192
inodeBitmapCsumLo: 0
inodeBitmapLo: 524319
inodeTableLo: 532000
itableUnusedLo: 8192
usedDirsCountLo: 0

Block group:32
blockBitmapCsumLo: 0
blockBitmapLo: 1048576
checksum: 42173
excludeBitmapLo: 0
flags: 4
flagsList: ['Inode Zeroed']
freeBlocksCountLo: 22015
freeInodesCountLo: 0
inodeBitmapCsumLo: 0
inodeBitmapLo: 1048592
inodeTableLo: 1048608
itableUnusedLo: 0
usedDirsCountLo: 993

Block group:33
blockBitmapCsumLo: 0
blockBitmapLo: 1048577
checksum: 17258
excludeBitmapLo: 0
flags: 4
flagsList: ['Inode Zeroed']
freeBlocksCountLo: 1600
freeInodesCountLo: 0
inodeBitmapCsumLo: 0
inodeBitmapLo: 1048593
inodeTableLo: 1049120
itableUnusedLo: 0
usedDirsCountLo: 566

Block group:34
blockBitmapCsumLo: 0
blockBitmapLo: 1048578
checksum: 41539
excludeBitmapLo: 0
flags: 4
flagsList: ['Inode Zeroed']
freeBlocksCountLo: 1120
freeInodesCountLo: 0
inodeBitmapCsumLo: 0
inodeBitmapLo: 1048594
inodeTableLo: 1049632
itableUnusedLo: 0
usedDirsCountLo: 479

Block group:35
blockBitmapCsumLo: 0
blockBitmapLo: 1048579
checksum: 54973
excludeBitmapLo: 0
flags: 4
flagsList: ['Inode Zeroed']
freeBlocksCountLo: 2187
freeInodesCountLo: 1542
inodeBitmapCsumLo: 0
inodeBitmapLo: 1048595
inodeTableLo: 1050144
itableUnusedLo: 1524
usedDirsCountLo: 250

Block group:36
blockBitmapCsumLo: 0
blockBitmapLo: 1048580
checksum: 39091
excludeBitmapLo: 0
flags: 5
flagsList: ['Inode Uninitialized', 'Inode Zeroed']
freeBlocksCountLo: 11877
freeInodesCountLo: 8192
inodeBitmapCsumLo: 0
inodeBitmapLo: 1048596
inodeTableLo: 1050656
itableUnusedLo: 8192
usedDirsCountLo: 0

Block group:37
blockBitmapCsumLo: 0
blockBitmapLo: 1048581
checksum: 27526
excludeBitmapLo: 0
flags: 5
flagsList: ['Inode Uninitialized', 'Inode Zeroed']
freeBlocksCountLo: 32313
freeInodesCountLo: 8192
inodeBitmapCsumLo: 0
inodeBitmapLo: 1048597
inodeTableLo: 1051168
itableUnusedLo: 8192
usedDirsCountLo: 0

Block group:38
blockBitmapCsumLo: 0
blockBitmapLo: 1048582
checksum: 52461
excludeBitmapLo: 0
flags: 7
flagsList: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
freeBlocksCountLo: 32768
freeInodesCountLo: 8192
inodeBitmapCsumLo: 0
inodeBitmapLo: 1048598
inodeTableLo: 1051680
itableUnusedLo: 8192
usedDirsCountLo: 0

Block group:39
blockBitmapCsumLo: 0
blockBitmapLo: 1048583
checksum: 27702
excludeBitmapLo: 0
flags: 7
flagsList: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
freeBlocksCountLo: 32768
freeInodesCountLo: 8192
inodeBitmapCsumLo: 0
inodeBitmapLo: 1048599
inodeTableLo: 1052192
itableUnusedLo: 8192
usedDirsCountLo: 0

Block group:40
blockBitmapCsumLo: 0
blockBitmapLo: 1048584
checksum: 51430
excludeBitmapLo: 0
flags: 7
flagsList: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
freeBlocksCountLo: 32768
freeInodesCountLo: 8192
inodeBitmapCsumLo: 0
inodeBitmapLo: 1048600
inodeTableLo: 1052704
itableUnusedLo: 8192
usedDirsCountLo: 0

Block group:41
blockBitmapCsumLo: 0
blockBitmapLo: 1048585
checksum: 26685
excludeBitmapLo: 0
flags: 7
flagsList: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
freeBlocksCountLo: 32768
freeInodesCountLo: 8192
inodeBitmapCsumLo: 0
inodeBitmapLo: 1048601
inodeTableLo: 1053216
itableUnusedLo: 8192
usedDirsCountLo: 0

Block group:42
blockBitmapCsumLo: 0
blockBitmapLo: 1048586
checksum: 51539
excludeBitmapLo: 0
flags: 7
flagsList: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
freeBlocksCountLo: 32768
freeInodesCountLo: 8192
inodeBitmapCsumLo: 0
inodeBitmapLo: 1048602
inodeTableLo: 1053728
itableUnusedLo: 8192
usedDirsCountLo: 0

Block group:43
blockBitmapCsumLo: 0
blockBitmapLo: 1048587
checksum: 27016
excludeBitmapLo: 0
flags: 7
flagsList: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
freeBlocksCountLo: 32768
freeInodesCountLo: 8192
inodeBitmapCsumLo: 0
inodeBitmapLo: 1048603
inodeTableLo: 1054240
itableUnusedLo: 8192
usedDirsCountLo: 0

Block group:44
blockBitmapCsumLo: 0
blockBitmapLo: 1048588
checksum: 52108
excludeBitmapLo: 0
flags: 7
flagsList: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
freeBlocksCountLo: 32768
freeInodesCountLo: 8192
inodeBitmapCsumLo: 0
inodeBitmapLo: 1048604
inodeTableLo: 1054752
itableUnusedLo: 8192
usedDirsCountLo: 0

Block group:45
blockBitmapCsumLo: 0
blockBitmapLo: 1048589
checksum: 27479
excludeBitmapLo: 0
flags: 7
flagsList: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
freeBlocksCountLo: 32768
freeInodesCountLo: 8192
inodeBitmapCsumLo: 0
inodeBitmapLo: 1048605
inodeTableLo: 1055264
itableUnusedLo: 8192
usedDirsCountLo: 0

Block group:46
blockBitmapCsumLo: 0
blockBitmapLo: 1048590
checksum: 51769
excludeBitmapLo: 0
flags: 7
flagsList: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
freeBlocksCountLo: 32768
freeInodesCountLo: 8192
inodeBitmapCsumLo: 0
inodeBitmapLo: 1048606
inodeTableLo: 1055776
itableUnusedLo: 8192
usedDirsCountLo: 0

Block group:47
blockBitmapCsumLo: 0
blockBitmapLo: 1048591
checksum: 27362
excludeBitmapLo: 0
flags: 7
flagsList: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
freeBlocksCountLo: 32768
freeInodesCountLo: 8192
inodeBitmapCsumLo: 0
inodeBitmapLo: 1048607
inodeTableLo: 1056288
itableUnusedLo: 8192
usedDirsCountLo: 0

Block group:48
blockBitmapCsumLo: 0
blockBitmapLo: 1572864
checksum: 52980
excludeBitmapLo: 0
flags: 4
flagsList: ['Inode Zeroed']
freeBlocksCountLo: 22365
freeInodesCountLo: 621
inodeBitmapCsumLo: 0
inodeBitmapLo: 1572880
inodeTableLo: 1572896
itableUnusedLo: 0
usedDirsCountLo: 1273

Block group:49
blockBitmapCsumLo: 0
blockBitmapLo: 1572865
checksum: 19654
excludeBitmapLo: 0
flags: 4
flagsList: ['Inode Zeroed']
freeBlocksCountLo: 0
freeInodesCountLo: 0
inodeBitmapCsumLo: 0
inodeBitmapLo: 1572881
inodeTableLo: 1573408
itableUnusedLo: 0
usedDirsCountLo: 125

Block group:50
blockBitmapCsumLo: 0
blockBitmapLo: 1572866
checksum: 15222
excludeBitmapLo: 0
flags: 4
flagsList: ['Inode Zeroed']
freeBlocksCountLo: 2205
freeInodesCountLo: 95
inodeBitmapCsumLo: 0
inodeBitmapLo: 1572882
inodeTableLo: 1573920
itableUnusedLo: 0
usedDirsCountLo: 227

Block group:51
blockBitmapCsumLo: 0
blockBitmapLo: 1572867
checksum: 7697
excludeBitmapLo: 0
flags: 4
flagsList: ['Inode Zeroed']
freeBlocksCountLo: 26952
freeInodesCountLo: 5453
inodeBitmapCsumLo: 0
inodeBitmapLo: 1572883
inodeTableLo: 1574432
itableUnusedLo: 5453
usedDirsCountLo: 416

Block group:52
blockBitmapCsumLo: 0
blockBitmapLo: 1572868
checksum: 48718
excludeBitmapLo: 0
flags: 7
flagsList: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
freeBlocksCountLo: 32768
freeInodesCountLo: 8192
inodeBitmapCsumLo: 0
inodeBitmapLo: 1572884
inodeTableLo: 1574944
itableUnusedLo: 8192
usedDirsCountLo: 0

Block group:53
blockBitmapCsumLo: 0
blockBitmapLo: 1572869
checksum: 7829
excludeBitmapLo: 0
flags: 7
flagsList: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
freeBlocksCountLo: 32768
freeInodesCountLo: 8192
inodeBitmapCsumLo: 0
inodeBitmapLo: 1572885
inodeTableLo: 1575456
itableUnusedLo: 8192
usedDirsCountLo: 0

Block group:54
blockBitmapCsumLo: 0
blockBitmapLo: 1572870
checksum: 49147
excludeBitmapLo: 0
flags: 7
flagsList: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
freeBlocksCountLo: 32768
freeInodesCountLo: 8192
inodeBitmapCsumLo: 0
inodeBitmapLo: 1572886
inodeTableLo: 1575968
itableUnusedLo: 8192
usedDirsCountLo: 0

Block group:55
blockBitmapCsumLo: 0
blockBitmapLo: 1572871
checksum: 7968
excludeBitmapLo: 0
flags: 7
flagsList: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
freeBlocksCountLo: 32768
freeInodesCountLo: 8192
inodeBitmapCsumLo: 0
inodeBitmapLo: 1572887
inodeTableLo: 1576480
itableUnusedLo: 8192
usedDirsCountLo: 0

Block group:56
blockBitmapCsumLo: 0
blockBitmapLo: 1572872
checksum: 48112
excludeBitmapLo: 0
flags: 7
flagsList: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
freeBlocksCountLo: 32768
freeInodesCountLo: 8192
inodeBitmapCsumLo: 0
inodeBitmapLo: 1572888
inodeTableLo: 1576992
itableUnusedLo: 8192
usedDirsCountLo: 0

Block group:57
blockBitmapCsumLo: 0
blockBitmapLo: 1572873
checksum: 6955
excludeBitmapLo: 0
flags: 7
flagsList: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
freeBlocksCountLo: 32768
freeInodesCountLo: 8192
inodeBitmapCsumLo: 0
inodeBitmapLo: 1572889
inodeTableLo: 1577504
itableUnusedLo: 8192
usedDirsCountLo: 0

Block group:58
blockBitmapCsumLo: 0
blockBitmapLo: 1572874
checksum: 47685
excludeBitmapLo: 0
flags: 7
flagsList: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
freeBlocksCountLo: 32768
freeInodesCountLo: 8192
inodeBitmapCsumLo: 0
inodeBitmapLo: 1572890
inodeTableLo: 1578016
itableUnusedLo: 8192
usedDirsCountLo: 0

Block group:59
blockBitmapCsumLo: 0
blockBitmapLo: 1572875
checksum: 6814
excludeBitmapLo: 0
flags: 7
flagsList: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
freeBlocksCountLo: 32768
freeInodesCountLo: 8192
inodeBitmapCsumLo: 0
inodeBitmapLo: 1572891
inodeTableLo: 1578528
itableUnusedLo: 8192
usedDirsCountLo: 0

Block group:60
blockBitmapCsumLo: 0
blockBitmapLo: 1572876
checksum: 47258
excludeBitmapLo: 0
flags: 7
flagsList: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
freeBlocksCountLo: 32768
freeInodesCountLo: 8192
inodeBitmapCsumLo: 0
inodeBitmapLo: 1572892
inodeTableLo: 1579040
itableUnusedLo: 8192
usedDirsCountLo: 0

Block group:61
blockBitmapCsumLo: 0
blockBitmapLo: 1572877
checksum: 6209
excludeBitmapLo: 0
flags: 7
flagsList: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
freeBlocksCountLo: 32768
freeInodesCountLo: 8192
inodeBitmapCsumLo: 0
inodeBitmapLo: 1572893
inodeTableLo: 1579552
itableUnusedLo: 8192
usedDirsCountLo: 0

Block group:62
blockBitmapCsumLo: 0
blockBitmapLo: 1572878
checksum: 47407
excludeBitmapLo: 0
flags: 7
flagsList: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
freeBlocksCountLo: 32768
freeInodesCountLo: 8192
inodeBitmapCsumLo: 0
inodeBitmapLo: 1572894
inodeTableLo: 1580064
itableUnusedLo: 8192
usedDirsCountLo: 0

Block group:63
blockBitmapCsumLo: 0
blockBitmapLo: 1572879
checksum: 6644
excludeBitmapLo: 0
flags: 7
flagsList: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
freeBlocksCountLo: 32768
freeInodesCountLo: 8192
inodeBitmapCsumLo: 0
inodeBitmapLo: 1572895
inodeTableLo: 1580576
itableUnusedLo: 8192
usedDirsCountLo: 0

Block group:64
blockBitmapCsumLo: 0
blockBitmapLo: 2097152
checksum: 12476
excludeBitmapLo: 0
flags: 4
flagsList: ['Inode Zeroed']
freeBlocksCountLo: 22168
freeInodesCountLo: 92
inodeBitmapCsumLo: 0
inodeBitmapLo: 2097168
inodeTableLo: 2097184
itableUnusedLo: 0
usedDirsCountLo: 1274

Block group:65
blockBitmapCsumLo: 0
blockBitmapLo: 2097153
checksum: 40577
excludeBitmapLo: 0
flags: 4
flagsList: ['Inode Zeroed']
freeBlocksCountLo: 999
freeInodesCountLo: 2957
inodeBitmapCsumLo: 0
inodeBitmapLo: 2097169
inodeTableLo: 2097696
itableUnusedLo: 2929
usedDirsCountLo: 931

Block group:66
blockBitmapCsumLo: 0
blockBitmapLo: 2097154
checksum: 52296
excludeBitmapLo: 0
flags: 5
flagsList: ['Inode Uninitialized', 'Inode Zeroed']
freeBlocksCountLo: 1295
freeInodesCountLo: 8192
inodeBitmapCsumLo: 0
inodeBitmapLo: 2097170
inodeTableLo: 2098208
itableUnusedLo: 8192
usedDirsCountLo: 0

Block group:67
blockBitmapCsumLo: 0
blockBitmapLo: 2097155
checksum: 18719
excludeBitmapLo: 0
flags: 5
flagsList: ['Inode Uninitialized', 'Inode Zeroed']
freeBlocksCountLo: 24047
freeInodesCountLo: 8192
inodeBitmapCsumLo: 0
inodeBitmapLo: 2097171
inodeTableLo: 2098720
itableUnusedLo: 8192
usedDirsCountLo: 0

Block group:68
blockBitmapCsumLo: 0
blockBitmapLo: 2097156
checksum: 42799
excludeBitmapLo: 0
flags: 7
flagsList: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
freeBlocksCountLo: 32768
freeInodesCountLo: 8192
inodeBitmapCsumLo: 0
inodeBitmapLo: 2097172
inodeTableLo: 2099232
itableUnusedLo: 8192
usedDirsCountLo: 0

Block group:69
blockBitmapCsumLo: 0
blockBitmapLo: 2097157
checksum: 2036
excludeBitmapLo: 0
flags: 7
flagsList: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
freeBlocksCountLo: 32768
freeInodesCountLo: 8192
inodeBitmapCsumLo: 0
inodeBitmapLo: 2097173
inodeTableLo: 2099744
itableUnusedLo: 8192
usedDirsCountLo: 0

Block group:70
blockBitmapCsumLo: 0
blockBitmapLo: 2097158
checksum: 42650
excludeBitmapLo: 0
flags: 7
flagsList: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
freeBlocksCountLo: 32768
freeInodesCountLo: 8192
inodeBitmapCsumLo: 0
inodeBitmapLo: 2097174
inodeTableLo: 2100256
itableUnusedLo: 8192
usedDirsCountLo: 0

Block group:71
blockBitmapCsumLo: 0
blockBitmapLo: 2097159
checksum: 1601
excludeBitmapLo: 0
flags: 7
flagsList: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
freeBlocksCountLo: 32768
freeInodesCountLo: 8192
inodeBitmapCsumLo: 0
inodeBitmapLo: 2097175
inodeTableLo: 2100768
itableUnusedLo: 8192
usedDirsCountLo: 0

Block group:72
blockBitmapCsumLo: 0
blockBitmapLo: 2097160
checksum: 41617
excludeBitmapLo: 0
flags: 7
flagsList: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
freeBlocksCountLo: 32768
freeInodesCountLo: 8192
inodeBitmapCsumLo: 0
inodeBitmapLo: 2097176
inodeTableLo: 2101280
itableUnusedLo: 8192
usedDirsCountLo: 0

Block group:73
blockBitmapCsumLo: 0
blockBitmapLo: 2097161
checksum: 586
excludeBitmapLo: 0
flags: 7
flagsList: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
freeBlocksCountLo: 32768
freeInodesCountLo: 8192
inodeBitmapCsumLo: 0
inodeBitmapLo: 2097177
inodeTableLo: 2101792
itableUnusedLo: 8192
usedDirsCountLo: 0

Block group:74
blockBitmapCsumLo: 0
blockBitmapLo: 2097162
checksum: 41764
excludeBitmapLo: 0
flags: 7
flagsList: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
freeBlocksCountLo: 32768
freeInodesCountLo: 8192
inodeBitmapCsumLo: 0
inodeBitmapLo: 2097178
inodeTableLo: 2102304
itableUnusedLo: 8192
usedDirsCountLo: 0

Block group:75
blockBitmapCsumLo: 0
blockBitmapLo: 2097163
checksum: 1023
excludeBitmapLo: 0
flags: 7
flagsList: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
freeBlocksCountLo: 32768
freeInodesCountLo: 8192
inodeBitmapCsumLo: 0
inodeBitmapLo: 2097179
inodeTableLo: 2102816
itableUnusedLo: 8192
usedDirsCountLo: 0

Block group:76
blockBitmapCsumLo: 0
blockBitmapLo: 2097164
checksum: 41467
excludeBitmapLo: 0
flags: 7
flagsList: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
freeBlocksCountLo: 32768
freeInodesCountLo: 8192
inodeBitmapCsumLo: 0
inodeBitmapLo: 2097180
inodeTableLo: 2103328
itableUnusedLo: 8192
usedDirsCountLo: 0

Block group:77
blockBitmapCsumLo: 0
blockBitmapLo: 2097165
checksum: 288
excludeBitmapLo: 0
flags: 7
flagsList: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
freeBlocksCountLo: 32768
freeInodesCountLo: 8192
inodeBitmapCsumLo: 0
inodeBitmapLo: 2097181
inodeTableLo: 2103840
itableUnusedLo: 8192
usedDirsCountLo: 0

Block group:78
blockBitmapCsumLo: 0
blockBitmapLo: 2097166
checksum: 41038
excludeBitmapLo: 0
flags: 7
flagsList: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
freeBlocksCountLo: 32768
freeInodesCountLo: 8192
inodeBitmapCsumLo: 0
inodeBitmapLo: 2097182
inodeTableLo: 2104352
itableUnusedLo: 8192
usedDirsCountLo: 0

Block group:79
blockBitmapCsumLo: 0
blockBitmapLo: 2097167
checksum: 149
excludeBitmapLo: 0
flags: 7
flagsList: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
freeBlocksCountLo: 32768
freeInodesCountLo: 8192
inodeBitmapCsumLo: 0
inodeBitmapLo: 2097183
inodeTableLo: 2104864
itableUnusedLo: 8192
usedDirsCountLo: 0

Block group:80
blockBitmapCsumLo: 0
blockBitmapLo: 2621440
checksum: 3698
excludeBitmapLo: 0
flags: 4
flagsList: ['Inode Zeroed']
freeBlocksCountLo: 14137
freeInodesCountLo: 356
inodeBitmapCsumLo: 0
inodeBitmapLo: 2621456
inodeTableLo: 2621472
itableUnusedLo: 0
usedDirsCountLo: 755

Block group:81
blockBitmapCsumLo: 0
blockBitmapLo: 2621441
checksum: 13105
excludeBitmapLo: 0
flags: 4
flagsList: ['Inode Zeroed']
freeBlocksCountLo: 427
freeInodesCountLo: 0
inodeBitmapCsumLo: 0
inodeBitmapLo: 2621457
inodeTableLo: 2621984
itableUnusedLo: 0
usedDirsCountLo: 252

Block group:82
blockBitmapCsumLo: 0
blockBitmapLo: 2621442
checksum: 55214
excludeBitmapLo: 0
flags: 4
flagsList: ['Inode Zeroed']
freeBlocksCountLo: 392
freeInodesCountLo: 0
inodeBitmapCsumLo: 0
inodeBitmapLo: 2621458
inodeTableLo: 2622496
itableUnusedLo: 0
usedDirsCountLo: 247

Block group:83
blockBitmapCsumLo: 0
blockBitmapLo: 2621443
checksum: 55952
excludeBitmapLo: 0
flags: 4
flagsList: ['Inode Zeroed']
freeBlocksCountLo: 32204
freeInodesCountLo: 16
inodeBitmapCsumLo: 0
inodeBitmapLo: 2621459
inodeTableLo: 2623008
itableUnusedLo: 0
usedDirsCountLo: 171

Block group:84
blockBitmapCsumLo: 0
blockBitmapLo: 2621444
checksum: 43368
excludeBitmapLo: 0
flags: 4
flagsList: ['Inode Zeroed']
freeBlocksCountLo: 32768
freeInodesCountLo: 3365
inodeBitmapCsumLo: 0
inodeBitmapLo: 2621460
inodeTableLo: 2623520
itableUnusedLo: 2486
usedDirsCountLo: 723

Block group:85
blockBitmapCsumLo: 0
blockBitmapLo: 2621445
checksum: 29922
excludeBitmapLo: 0
flags: 7
flagsList: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
freeBlocksCountLo: 32768
freeInodesCountLo: 8192
inodeBitmapCsumLo: 0
inodeBitmapLo: 2621461
inodeTableLo: 2624032
itableUnusedLo: 8192
usedDirsCountLo: 0

Block group:86
blockBitmapCsumLo: 0
blockBitmapLo: 2621446
checksum: 54668
excludeBitmapLo: 0
flags: 7
flagsList: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
freeBlocksCountLo: 32768
freeInodesCountLo: 8192
inodeBitmapCsumLo: 0
inodeBitmapLo: 2621462
inodeTableLo: 2624544
itableUnusedLo: 8192
usedDirsCountLo: 0

Block group:87
blockBitmapCsumLo: 0
blockBitmapLo: 2621447
checksum: 30039
excludeBitmapLo: 0
flags: 7
flagsList: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
freeBlocksCountLo: 32768
freeInodesCountLo: 8192
inodeBitmapCsumLo: 0
inodeBitmapLo: 2621463
inodeTableLo: 2625056
itableUnusedLo: 8192
usedDirsCountLo: 0

Block group:88
blockBitmapCsumLo: 0
blockBitmapLo: 2621448
checksum: 53639
excludeBitmapLo: 0
flags: 7
flagsList: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
freeBlocksCountLo: 32768
freeInodesCountLo: 8192
inodeBitmapCsumLo: 0
inodeBitmapLo: 2621464
inodeTableLo: 2625568
itableUnusedLo: 8192
usedDirsCountLo: 0

Block group:89
blockBitmapCsumLo: 0
blockBitmapLo: 2621449
checksum: 29020
excludeBitmapLo: 0
flags: 7
flagsList: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
freeBlocksCountLo: 32768
freeInodesCountLo: 8192
inodeBitmapCsumLo: 0
inodeBitmapLo: 2621465
inodeTableLo: 2626080
itableUnusedLo: 8192
usedDirsCountLo: 0

Block group:90
blockBitmapCsumLo: 0
blockBitmapLo: 2621450
checksum: 53298
excludeBitmapLo: 0
flags: 7
flagsList: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
freeBlocksCountLo: 32768
freeInodesCountLo: 8192
inodeBitmapCsumLo: 0
inodeBitmapLo: 2621466
inodeTableLo: 2626592
itableUnusedLo: 8192
usedDirsCountLo: 0

Block group:91
blockBitmapCsumLo: 0
blockBitmapLo: 2621451
checksum: 28905
excludeBitmapLo: 0
flags: 7
flagsList: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
freeBlocksCountLo: 32768
freeInodesCountLo: 8192
inodeBitmapCsumLo: 0
inodeBitmapLo: 2621467
inodeTableLo: 2627104
itableUnusedLo: 8192
usedDirsCountLo: 0

Block group:92
blockBitmapCsumLo: 0
blockBitmapLo: 2621452
checksum: 53997
excludeBitmapLo: 0
flags: 7
flagsList: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
freeBlocksCountLo: 32768
freeInodesCountLo: 8192
inodeBitmapCsumLo: 0
inodeBitmapLo: 2621468
inodeTableLo: 2627616
itableUnusedLo: 8192
usedDirsCountLo: 0

Block group:93
blockBitmapCsumLo: 0
blockBitmapLo: 2621453
checksum: 29238
excludeBitmapLo: 0
flags: 7
flagsList: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
freeBlocksCountLo: 32768
freeInodesCountLo: 8192
inodeBitmapCsumLo: 0
inodeBitmapLo: 2621469
inodeTableLo: 2628128
itableUnusedLo: 8192
usedDirsCountLo: 0

Block group:94
blockBitmapCsumLo: 0
blockBitmapLo: 2621454
checksum: 54104
excludeBitmapLo: 0
flags: 7
flagsList: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
freeBlocksCountLo: 32768
freeInodesCountLo: 8192
inodeBitmapCsumLo: 0
inodeBitmapLo: 2621470
inodeTableLo: 2628640
itableUnusedLo: 8192
usedDirsCountLo: 0

Block group:95
blockBitmapCsumLo: 0
blockBitmapLo: 2621455
checksum: 29571
excludeBitmapLo: 0
flags: 7
flagsList: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
freeBlocksCountLo: 32768
freeInodesCountLo: 8192
inodeBitmapCsumLo: 0
inodeBitmapLo: 2621471
inodeTableLo: 2629152
itableUnusedLo: 8192
usedDirsCountLo: 0

Block group:96
blockBitmapCsumLo: 0
blockBitmapLo: 3145728
checksum: 48384
excludeBitmapLo: 0
flags: 4
flagsList: ['Inode Zeroed']
freeBlocksCountLo: 14275
freeInodesCountLo: 1
inodeBitmapCsumLo: 0
inodeBitmapLo: 3145744
inodeTableLo: 3145760
itableUnusedLo: 0
usedDirsCountLo: 388

Block group:97
blockBitmapCsumLo: 0
blockBitmapLo: 3145729
checksum: 64679
excludeBitmapLo: 0
flags: 4
flagsList: ['Inode Zeroed']
freeBlocksCountLo: 17783
freeInodesCountLo: 0
inodeBitmapCsumLo: 0
inodeBitmapLo: 3145745
inodeTableLo: 3146272
itableUnusedLo: 0
usedDirsCountLo: 217

Block group:98
blockBitmapCsumLo: 0
blockBitmapLo: 3145730
checksum: 42011
excludeBitmapLo: 0
flags: 4
flagsList: ['Inode Zeroed']
freeBlocksCountLo: 32768
freeInodesCountLo: 0
inodeBitmapCsumLo: 0
inodeBitmapLo: 3145746
inodeTableLo: 3146784
itableUnusedLo: 0
usedDirsCountLo: 227

Block group:99
blockBitmapCsumLo: 0
blockBitmapLo: 3145731
checksum: 32028
excludeBitmapLo: 0
flags: 4
flagsList: ['Inode Zeroed']
freeBlocksCountLo: 32768
freeInodesCountLo: 662
inodeBitmapCsumLo: 0
inodeBitmapLo: 3145747
inodeTableLo: 3147296
itableUnusedLo: 469
usedDirsCountLo: 1472

Block group:100
blockBitmapCsumLo: 0
blockBitmapLo: 3145732
checksum: 16643
excludeBitmapLo: 0
flags: 7
flagsList: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
freeBlocksCountLo: 32768
freeInodesCountLo: 8192
inodeBitmapCsumLo: 0
inodeBitmapLo: 3145748
inodeTableLo: 3147808
itableUnusedLo: 8192
usedDirsCountLo: 0

Block group:101
blockBitmapCsumLo: 0
blockBitmapLo: 3145733
checksum: 57816
excludeBitmapLo: 0
flags: 7
flagsList: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
freeBlocksCountLo: 32768
freeInodesCountLo: 8192
inodeBitmapCsumLo: 0
inodeBitmapLo: 3145749
inodeTableLo: 3148320
itableUnusedLo: 8192
usedDirsCountLo: 0

Block group:102
blockBitmapCsumLo: 0
blockBitmapLo: 3145734
checksum: 16566
excludeBitmapLo: 0
flags: 7
flagsList: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
freeBlocksCountLo: 32768
freeInodesCountLo: 8192
inodeBitmapCsumLo: 0
inodeBitmapLo: 3145750
inodeTableLo: 3148832
itableUnusedLo: 8192
usedDirsCountLo: 0

Block group:103
blockBitmapCsumLo: 0
blockBitmapLo: 3145735
checksum: 57453
excludeBitmapLo: 0
flags: 7
flagsList: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
freeBlocksCountLo: 32768
freeInodesCountLo: 8192
inodeBitmapCsumLo: 0
inodeBitmapLo: 3145751
inodeTableLo: 3149344
itableUnusedLo: 8192
usedDirsCountLo: 0

Block group:104
blockBitmapCsumLo: 0
blockBitmapLo: 3145736
checksum: 17597
excludeBitmapLo: 0
flags: 7
flagsList: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
freeBlocksCountLo: 32768
freeInodesCountLo: 8192
inodeBitmapCsumLo: 0
inodeBitmapLo: 3145752
inodeTableLo: 3149856
itableUnusedLo: 8192
usedDirsCountLo: 0

Block group:105
blockBitmapCsumLo: 0
blockBitmapLo: 3145737
checksum: 58470
excludeBitmapLo: 0
flags: 7
flagsList: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
freeBlocksCountLo: 32768
freeInodesCountLo: 8192
inodeBitmapCsumLo: 0
inodeBitmapLo: 3145753
inodeTableLo: 3150368
itableUnusedLo: 8192
usedDirsCountLo: 0

Block group:106
blockBitmapCsumLo: 0
blockBitmapLo: 3145738
checksum: 17672
excludeBitmapLo: 0
flags: 7
flagsList: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
freeBlocksCountLo: 32768
freeInodesCountLo: 8192
inodeBitmapCsumLo: 0
inodeBitmapLo: 3145754
inodeTableLo: 3150880
itableUnusedLo: 8192
usedDirsCountLo: 0

Block group:107
blockBitmapCsumLo: 0
blockBitmapLo: 3145739
checksum: 58835
excludeBitmapLo: 0
flags: 7
flagsList: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
freeBlocksCountLo: 32768
freeInodesCountLo: 8192
inodeBitmapCsumLo: 0
inodeBitmapLo: 3145755
inodeTableLo: 3151392
itableUnusedLo: 8192
usedDirsCountLo: 0

Block group:108
blockBitmapCsumLo: 0
blockBitmapLo: 3145740
checksum: 18391
excludeBitmapLo: 0
flags: 7
flagsList: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
freeBlocksCountLo: 32768
freeInodesCountLo: 8192
inodeBitmapCsumLo: 0
inodeBitmapLo: 3145756
inodeTableLo: 3151904
itableUnusedLo: 8192
usedDirsCountLo: 0

Block group:109
blockBitmapCsumLo: 0
blockBitmapLo: 3145741
checksum: 59148
excludeBitmapLo: 0
flags: 7
flagsList: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
freeBlocksCountLo: 32768
freeInodesCountLo: 8192
inodeBitmapCsumLo: 0
inodeBitmapLo: 3145757
inodeTableLo: 3152416
itableUnusedLo: 8192
usedDirsCountLo: 0

Block group:110
blockBitmapCsumLo: 0
blockBitmapLo: 3145742
checksum: 18018
excludeBitmapLo: 0
flags: 7
flagsList: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
freeBlocksCountLo: 32768
freeInodesCountLo: 8192
inodeBitmapCsumLo: 0
inodeBitmapLo: 3145758
inodeTableLo: 3152928
itableUnusedLo: 8192
usedDirsCountLo: 0

Block group:111
blockBitmapCsumLo: 0
blockBitmapLo: 3145743
checksum: 59065
excludeBitmapLo: 0
flags: 7
flagsList: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
freeBlocksCountLo: 32768
freeInodesCountLo: 8192
inodeBitmapCsumLo: 0
inodeBitmapLo: 3145759
inodeTableLo: 3153440
itableUnusedLo: 8192
usedDirsCountLo: 0

Block group:112
blockBitmapCsumLo: 0
blockBitmapLo: 3670016
checksum: 12421
excludeBitmapLo: 0
flags: 4
flagsList: ['Inode Zeroed']
freeBlocksCountLo: 22898
freeInodesCountLo: 2762
inodeBitmapCsumLo: 0
inodeBitmapLo: 3670032
inodeTableLo: 3670048
itableUnusedLo: 2761
usedDirsCountLo: 1644

Block group:113
blockBitmapCsumLo: 0
blockBitmapLo: 3670017
checksum: 55320
excludeBitmapLo: 0
flags: 5
flagsList: ['Inode Uninitialized', 'Inode Zeroed']
freeBlocksCountLo: 31258
freeInodesCountLo: 8192
inodeBitmapCsumLo: 0
inodeBitmapLo: 3670033
inodeTableLo: 3670560
itableUnusedLo: 8192
usedDirsCountLo: 0

Block group:114
blockBitmapCsumLo: 0
blockBitmapLo: 3670018
checksum: 12490
excludeBitmapLo: 0
flags: 7
flagsList: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
freeBlocksCountLo: 32768
freeInodesCountLo: 8192
inodeBitmapCsumLo: 0
inodeBitmapLo: 3670034
inodeTableLo: 3671072
itableUnusedLo: 8192
usedDirsCountLo: 0

Block group:115
blockBitmapCsumLo: 0
blockBitmapLo: 3670019
checksum: 36881
excludeBitmapLo: 0
flags: 7
flagsList: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
freeBlocksCountLo: 32768
freeInodesCountLo: 8192
inodeBitmapCsumLo: 0
inodeBitmapLo: 3670035
inodeTableLo: 3671584
itableUnusedLo: 8192
usedDirsCountLo: 0

Block group:116
blockBitmapCsumLo: 0
blockBitmapLo: 3670020
checksum: 12821
excludeBitmapLo: 0
flags: 7
flagsList: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
freeBlocksCountLo: 32768
freeInodesCountLo: 8192
inodeBitmapCsumLo: 0
inodeBitmapLo: 3670036
inodeTableLo: 3672096
itableUnusedLo: 8192
usedDirsCountLo: 0

Block group:117
blockBitmapCsumLo: 0
blockBitmapLo: 3670021
checksum: 37582
excludeBitmapLo: 0
flags: 7
flagsList: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
freeBlocksCountLo: 32768
freeInodesCountLo: 8192
inodeBitmapCsumLo: 0
inodeBitmapLo: 3670037
inodeTableLo: 3672608
itableUnusedLo: 8192
usedDirsCountLo: 0

Block group:118
blockBitmapCsumLo: 0
blockBitmapLo: 3670022
checksum: 13216
excludeBitmapLo: 0
flags: 7
flagsList: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
freeBlocksCountLo: 32768
freeInodesCountLo: 8192
inodeBitmapCsumLo: 0
inodeBitmapLo: 3670038
inodeTableLo: 3673120
itableUnusedLo: 8192
usedDirsCountLo: 0

Block group:119
blockBitmapCsumLo: 0
blockBitmapLo: 3670023
checksum: 37755
excludeBitmapLo: 0
flags: 7
flagsList: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
freeBlocksCountLo: 32768
freeInodesCountLo: 8192
inodeBitmapCsumLo: 0
inodeBitmapLo: 3670039
inodeTableLo: 3673632
itableUnusedLo: 8192
usedDirsCountLo: 0

Block group:120
blockBitmapCsumLo: 0
blockBitmapLo: 3670024
checksum: 14251
excludeBitmapLo: 0
flags: 7
flagsList: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
freeBlocksCountLo: 32768
freeInodesCountLo: 8192
inodeBitmapCsumLo: 0
inodeBitmapLo: 3670040
inodeTableLo: 3674144
itableUnusedLo: 8192
usedDirsCountLo: 0

Block group:121
blockBitmapCsumLo: 0
blockBitmapLo: 3670025
checksum: 38768
excludeBitmapLo: 0
flags: 7
flagsList: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
freeBlocksCountLo: 32768
freeInodesCountLo: 8192
inodeBitmapCsumLo: 0
inodeBitmapLo: 3670041
inodeTableLo: 3674656
itableUnusedLo: 8192
usedDirsCountLo: 0

Block group:122
blockBitmapCsumLo: 0
blockBitmapLo: 3670026
checksum: 13854
excludeBitmapLo: 0
flags: 7
flagsList: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
freeBlocksCountLo: 32768
freeInodesCountLo: 8192
inodeBitmapCsumLo: 0
inodeBitmapLo: 3670042
inodeTableLo: 3675168
itableUnusedLo: 8192
usedDirsCountLo: 0

Block group:123
blockBitmapCsumLo: 0
blockBitmapLo: 3670027
checksum: 38597
excludeBitmapLo: 0
flags: 7
flagsList: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
freeBlocksCountLo: 32768
freeInodesCountLo: 8192
inodeBitmapCsumLo: 0
inodeBitmapLo: 3670043
inodeTableLo: 3675680
itableUnusedLo: 8192
usedDirsCountLo: 0

Block group:124
blockBitmapCsumLo: 0
blockBitmapLo: 3670028
checksum: 13505
excludeBitmapLo: 0
flags: 7
flagsList: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
freeBlocksCountLo: 32768
freeInodesCountLo: 8192
inodeBitmapCsumLo: 0
inodeBitmapLo: 3670044
inodeTableLo: 3676192
itableUnusedLo: 8192
usedDirsCountLo: 0

Block group:125
blockBitmapCsumLo: 0
blockBitmapLo: 3670029
checksum: 45353
excludeBitmapLo: 0
flags: 7
flagsList: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
freeBlocksCountLo: 31743
freeInodesCountLo: 8192
inodeBitmapCsumLo: 0
inodeBitmapLo: 3670045
inodeTableLo: 3676704
itableUnusedLo: 8192
usedDirsCountLo: 0

Block group:126
blockBitmapCsumLo: 0
blockBitmapLo: 3670030
checksum: 13684
excludeBitmapLo: 0
flags: 7
flagsList: ['Inode Uninitialized', 'Block Uninitialized', 'Inode Zeroed']
freeBlocksCountLo: 32768
freeInodesCountLo: 8192
inodeBitmapCsumLo: 0
inodeBitmapLo: 3670046
inodeTableLo: 3677216
itableUnusedLo: 8192
usedDirsCountLo: 0

Block group:127
blockBitmapCsumLo: 0
blockBitmapLo: 3670031
checksum: 37415
excludeBitmapLo: 0
flags: 5
flagsList: ['Inode Uninitialized', 'Inode Zeroed']
freeBlocksCountLo: 32512
freeInodesCountLo: 8192
inodeBitmapCsumLo: 0
inodeBitmapLo: 3670047
inodeTableLo: 3677728
itableUnusedLo: 8192
usedDirsCountLo: 0

u64@u64-VirtualBox:~/Desktop$
```
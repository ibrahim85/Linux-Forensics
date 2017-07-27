###### 56. Inodes: adding support for Extents for our Python Scripts

###### ```extfs.py```

```python
#!/usr/bin/python
# This is a simple Python script that will
# get metadata from an ext2/3/4 filesystem inside
# of an image file.
#
# Developed for PentesterAcademy by Dr. Phil Polstra (@ppolstra)

import sys
import os.path
import subprocess
import struct
import time, calendar
from math import log

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

  def groupDescriptorSize(self):
    if '64-bit' in self.incompatibleFeaturesList:
      return 64
    else:
      return 32

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

  def groupStartBlock(self, bgNo):
    return self.blocksPerGroup * bgNo

  def groupEndBlock(self, bgNo):
    return self.groupStartBlock(bgNo + 1) - 1  

  def groupStartInode(self, bgNo):
    return self.inodesPerGroup * bgNo + 1
 
  def groupEndInode(self, bgNo):
    return self.inodesPerGroup * (bgNo + 1)      

  def groupFromBlock(self, blockNo):
    return blockNo / self.blocksPerGroup

  def groupIndexFromBlock(self, blockNo):
    return blockNo % self.blocksPerGroup

  def groupFromInode(self, inodeNo):
    return (inodeNo - 1) / self.inodesPerGroup
                  
  def groupIndexFromInode(self, inodeNo):
    return (inodeNo - 1) % self.inodesPerGroup

  def groupHasSuperblock(self, bgNo):
    # block group zero always has a superblock
    if bgNo == 0:
      return True
    retVal = False
    if 'Sparse Super 2' in self.compatibleFeaturesList: 
      # two backup superblocks in self.backupBlockGroups
      if bgNo == self.backupBlockGroups[0] or bgNo == self.backupBlockGroups[1]:
        retVal = True
    elif 'Sparse Super' in self.readOnlyCompatibleFeaturesList:
      # backups in 1, powers of 3, 5, and 7
      retVal = (bgNo == 1) or (bgNo == pow(3, round(log(bgNo) / log(3)))) \
        or (bgNo == pow(5, round(log(bgNo) / log(5)))) \
        or (bgNo == pow(7, round(log(bgNo) / log(7)))) 
      if retVal:
        return retVal
    elif 'Meta Block Groups' in self.incompatibleFeaturesList:
      # meta block groups have a sb and gdt in 1st and last two of each meta group
      # meta block group size is blocksize/32
      # only part of filesystem might use this feature
      if bgNo >= self.firstMetaBlockGroup:
        mbgSize = self.blockSize / 32
        retVal = (bgNo % mbgSize == 0) or ((bgNo + 1) % mbgSize == 0) or ((bgNo + 2) % mbgSize == 0)
    else:
      # if we got this far we must have default with every bg having sb and gdt
      retVal = True
    return retVal

class GroupDescriptor():
  def __init__(self, data, wide=False):
        self.wide = wide
	self.blockBitmapLo=getU32(data)	        #/* Blocks bitmap block */
	self.inodeBitmapLo=getU32(data, 4)	#/* Inodes bitmap block */
	self.inodeTableLo=getU32(data, 8)	#/* Inodes table block */
	self.freeBlocksCountLo=getU16(data, 0xc)#/* Free blocks count */
	self.freeInodesCountLo=getU16(data, 0xe)#/* Free inodes count */
	self.usedDirsCountLo=getU16(data, 0x10)	#/* Directories count */
	self.flags=getU16(data, 0x12)		#/* EXT4_BG_flags (INODE_UNINIT, etc) */
	self.flagList = self.printFlagList()
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

# This class combines informaton from the block group descriptor
# and the superblock to more fully describe the block group
class ExtendedGroupDescriptor():
  def __init__(self, bgd, sb, bgNo):
    self.blockGroup = bgNo
    self.startBlock = sb.groupStartBlock(bgNo)
    self.endBlock = sb.groupEndBlock(bgNo)
    self.startInode = sb.groupStartInode(bgNo)
    self.endInode = sb.groupEndInode(bgNo)
    self.flags = bgd.printFlagList()
    self.freeInodes = bgd.freeInodesCountLo
    if bgd.wide:
      self.freeInodes += bgd.freeInodesCountHi * pow(2, 16)
    self.freeBlocks = bgd.freeBlocksCountLo
    if bgd.wide:
      self.freeBlocks += bgd.freeBlocksCountHi * pow(2, 16)
    self.directories = bgd.usedDirsCountLo
    if bgd.wide:
      self.directories += bgd.usedDirsCountHi * pow(2, 16)
    self.checksum = bgd.checksum
    self.blockBitmapChecksum = bgd.blockBitmapCsumLo
    if bgd.wide:
      self.blockBitmapChecksum += bgd.blockBitmapCsumHi * pow(2, 16)
    self.inodeBitmapChecksum = bgd.inodeBitmapCsumLo
    if bgd.wide:
      self.inodeBitmapChecksum += bgd.inodeBitmapCsumHi * pow(2, 16)
    # now figure out the layout and store it in a list (with lists inside)
    self.layout = []
    self.nonDataBlocks = 0
    # for flexible block groups must make an adjustment
    fbgAdj = 1
    if 'Flexible Block Groups' in sb.incompatibleFeaturesList:
      if bgNo % sb.groupsPerFlex == 0: # only first group in flex block affected
        fbgAdj = sb.groupsPerFlex   
    if sb.groupHasSuperblock(bgNo):
      self.layout.append(['Superblock', self.startBlock, self.startBlock])
      gdSize = sb.groupDescriptorSize() * sb.blockGroups() / sb.blockSize
      self.layout.append(['Group Descriptor Table', self.startBlock + 1, self.startBlock + gdSize])
      self.nonDataBlocks += gdSize + 1
      if sb.reservedGdtBlocks > 0:
        self.layout.append(['Reserved GDT Blocks', self.startBlock + gdSize + 1, \
          self.startBlock + gdSize + sb.reservedGdtBlocks])
        self.nonDataBlocks += sb.reservedGdtBlocks
    bbm = bgd.blockBitmapLo
    if bgd.wide:
      bbm += bgd.blockBitmapHi * pow(2, 32)
    self.layout.append(['Data Block Bitmap', bbm, bbm])
    # is block bitmap in this group (not flex block group, etc) 
    if sb.groupFromBlock(bbm) == bgNo:
      self.nonDataBlocks += fbgAdj
    ibm = bgd.inodeBitmapLo
    if bgd.wide:
      ibm += bgd.inodeBitmapHi * pow(2, 32)
    self.layout.append(['Inode Bitmap', ibm, ibm])
    # is inode bitmap in this group?
    if sb.groupFromBlock(ibm) == bgNo:
      self.nonDataBlocks += fbgAdj 
    it = bgd.inodeTableLo
    if bgd.wide:
      it += bgd.inodeTableHi * pow(2, 32)
    self.inodeTable = it
    itBlocks = (sb.inodesPerGroup * sb.inodeSize) / sb.blockSize
    self.layout.append(['Inode Table', it, it + itBlocks - 1])
    # is inode table in this group?
    if sb.groupFromBlock(it) == bgNo:
      self.nonDataBlocks += itBlocks * fbgAdj
    self.layout.append(['Data Blocks', self.startBlock + self.nonDataBlocks, self.endBlock])

  def prettyPrint(self):
    print ""
    print 'Block Group: ' + str(self.blockGroup)
    print 'Flags: %r ' % self.flags
    print 'Blocks: %s - %s ' % (self.startBlock, self.endBlock)
    print 'Inodes: %s - %s ' % (self.startInode, self.endInode)
    print 'Layout:'
    for item in self.layout:
      print '   %s %s - %s' % (item[0], item[1], item[2])
    print 'Free Inodes: %u ' % self.freeInodes
    print 'Free Blocks: %u ' % self.freeBlocks
    print 'Directories: %u ' % self.directories
    print 'Checksum: 0x%x ' % self.checksum
    print 'Block Bitmap Checksum: 0x%x ' % self.blockBitmapChecksum
    print 'Inode Bitmap Checksum: 0x%x ' % self.inodeBitmapChecksum

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
      ebgd = ExtendedGroupDescriptor(bgd, self.superblock, i) 
      self.bgdList.append(ebgd)

  def prettyPrint(self):
    self.superblock.prettyPrint()
    for bgd in self.bgdList:
      bgd.prettyPrint()

def getInodeModes(mode):
  retVal = []

  if mode & 0x1:
    retVal.append("Others Exec")
  if mode & 0x2:
    retVal.append("Others Write")
  if mode & 0x4:
    retVal.append("Others Read")
  if mode & 0x8:
    retVal.append("Group Exec")
  if mode & 0x10:
    retVal.append("Group Write")
  if mode & 0x20:
    retVal.append("Group Read")
  if mode & 0x40:
    retVal.append("Owner Exec")
  if mode & 0x80:
    retVal.append("Owner Write")
  if mode & 0x100:
    retVal.append("Owner Read")
  if mode & 0x200:
    retVal.append("Sticky Bit")
  if mode & 0x400:
    retVal.append("Set GID")
  if mode & 0x800:
    retVal.append("Set UID")

  return retVal

def getInodeFileType(mode):
  fType = (mode & 0xf000) >> 12   
  if fType == 0x1:
    return "FIFO"
  elif fType == 0x2:
    return "Char Device"
  elif fType == 0x4:
    return "Directory"
  elif fType == 0x6:
    return "Block Device"
  elif fType == 0x8:
    return "Regular File"
  elif fType == 0xA:
    return "Symbolic Link"
  elif fType == 0xc:
    return "Socket"
  else:
    return "Unknown Filetype"

def getInodeFlags(flags):
  retVal = []

  if flags & 0x1:
    retVal.append("Secure Deletion")
  if flags & 0x2:
    retVal.append("Preserve for Undelete")
  if flags & 0x4:
    retVal.append("Compressed File")
  if flags & 0x8:
    retVal.append("Synchronous Writes")
  if flags & 0x10:
    retVal.append("Immutable File")
  if flags & 0x20:
    retVal.append("Append Only")
  if flags & 0x40:
    retVal.append("Do Not Dump")
  if flags & 0x80:
    retVal.append("Do Not Update Access Time")
  if flags & 0x100:
    retVal.append("Dirty Compressed File")
  if flags & 0x200:   
    retVal.append("Compressed Clusters")
  if flags & 0x400:
    retVal.append("Do Not Compress")
  if flags & 0x800:
    retVal.append("Encrypted Inode")
  if flags & 0x1000:
    retVal.append("Directory Hash Indexes")
  if flags & 0x2000:
    retVal.append("AFS Magic Directory")
  if flags & 0x4000:
    retVal.append("Must Be Written Through Journal")
  if flags & 0x8000:
    retVal.append("Do Not Merge File Tail")
  if flags & 0x10000:
    retVal.append("Directory Entries Written Synchronously")
  if flags & 0x20000:
    retVal.append("Top of Directory Hierarchy")
  if flags & 0x40000:
    retVal.append("Huge File")
  if flags & 0x80000:
    retVal.append("Inode uses Extents")
  if flags & 0x200000:
    retVal.append("Large Extended Attribute in Inode")
  if flags & 0x400000:
    retVal.append("Blocks Past EOF")
  if flags & 0x1000000:
    retVal.append("Inode is Snapshot")
  if flags & 0x4000000:
    retVal.append("Snapshot is being Deleted")
  if flags & 0x8000000:
    retVal.append("Snapshot Shrink Completed")
  if flags & 0x10000000:
    retVal.append("Inline Data")
  if flags & 0x80000000:
    retVal.append("Reserved for Ext4 Library")
  if flags & 0x4bdfff:
    retVal.append("User-visible Flags")
  if flags & 0x4b80ff:
    retVal.append("User-modifiable Flags")
    
  return retVal  

def getInodeLoc(inodeNo, inodesPerGroup):
  bg = (int(inodeNo) - 1) / int(inodesPerGroup)
  index = (int(inodeNo) - 1) % int(inodesPerGroup)
  return [bg, index ]

class ExtentHeader():
  def __init__(self, data):
    self.magic = getU16(data)
    self.entries = getU16(data, 0x2)
    self.max = getU16(data, 0x4)
    self.depth = getU16(data, 0x6)
    self.generation = getU32(data, 0x8)
  def prettyPrint(self):
    print("Extent depth: %s entries: %s max-entries: %s generation: %s" \
      % (self.depth, self.entries, self.max, self.generation))

class ExtentIndex():
  def __init__(self, data):
    self.block = getU32(data)
    self.leafLo = getU32(data, 0x4)
    self.leafHi = getU16(data, 0x8)
  def prettyPrint(self):
    print("Index block: %s leaf: %s" \
      % (self.block, self.leafHi * pow(2, 32) + self.leafLo))

class Extent():
  def __init__(self, data):
    self.block = getU32(data)
    self.len = getU16(data, 0x4)
    self.startHi = getU16(data, 0x6)
    self.startLo = getU32(data, 0x8)
  def prettyPrint(self):
    print("Extent block: %s data blocks: %s - %s" \
      % (self.block, self.startHi * pow(2, 32) + self.startLo, \
      self.len + self.startHi * pow(2, 32) + self.startLo - 1))

def getExtentTree(data):
  # first entry must be a header
  retVal = []
  retVal.append(ExtentHeader(data))
  if retVal[0].depth == 0:
    # leaf node
    for i in range(0, retVal[0].entries):
      retVal.append(Extent(data[(i + 1) * 12 : ]))
  else:
    # index nodes
    for i in range(0, retVal[0].entries):
      retVal.append(ExtentIndex(data[(i + 1) * 12 : ]))
  return retVal

class Inode():
  def __init__(self, data, inodeSize=128):
    self.mode = getU16(data)
    self.modeList = getInodeModes(self.mode)
    self.fileType = getInodeFileType(self.mode)
    self.ownerID = getU16(data, 0x2)
    self.fileSize = getU32(data, 0x4)
    self.accessTime = time.gmtime(getU32(data, 0x8))
    self.changeTime = time.gmtime(getU32(data, 0xC))
    self.modifyTime = time.gmtime(getU32(data, 0x10))
    self.deleteTime = time.gmtime(getU32(data, 0x14))
    self.groupID = getU16(data, 0x18)
    self.links = getU16(data, 0x1a)
    self.blocks = getU32(data, 0x1c)
    self.flags = getU32(data, 0x20)
    self.flagList = getInodeFlags(self.flags)
    self.osd1 = getU32(data, 0x24) # high 32-bits of generation for Linux
    self.block = []
    self.extents = []
    if self.flags & 0x80000:
      self.extents = getExtentTree(data[0x28 : ])
    else:
      for i in range(0, 15):
        self.block.append(getU32(data, 0x28 + i * 4))
    self.generation = getU32(data, 0x64)
    self.extendAttribs = getU32(data, 0x68)
    self.fileSize += pow(2, 32) * getU32(data, 0x6c)
    # these are technically only correct for Linux ext4 filesystems
    # should probably verify that that is the case
    self.blocks += getU16(data, 0x74) * pow(2, 32)
    self.extendAttribs += getU16(data, 0x76) * pow(2, 32)
    self.ownerID += getU16(data, 0x78) * pow(2, 32)
    self.groupID += getU16(data, 0x7a) * pow(2, 32)
    self.checksum = getU16(data, 0x7c)
    if inodeSize > 128:
      self.inodeSize = 128 + getU16(data, 0x80)
    if self.inodeSize > 0x82:
      self.checksum += getU16(data, 0x82) * pow(2, 16)
    if self.inodeSize > 0x84:
      self.changeTimeNanosecs = getU32(data, 0x84) >> 2
    if self.inodeSize > 0x88:
      self.modifyTimeNanosecs = getU32(data, 0x88) >> 2
    if self.inodeSize > 0x8c:
      self.accessTimeNanosecs = getU32(data, 0x8c) >> 2
    if self.inodeSize > 0x90:
      self.createTime = time.gmtime(getU32(data, 0x90))
      self.createTimeNanosecs = getU32(data, 0x94) >> 2
    else:
      self.createTime = time.gmtime(0)
      
  def prettyPrint(self):
    for k, v in sorted(self.__dict__.iteritems()) :
      if k == 'extents' and self.extents:
        v[0].prettyPrint() # print header
        for i in range(1, v[0].entries + 1):
          v[i].prettyPrint()
      elif k == 'changeTime' or k == 'modifyTime' or k == 'accessTime' or k == 'createTime':
        print k+":", time.asctime(v)
      elif k == 'deleteTime':
        if calendar.timegm(v) == 0:
          print 'Deleted: no'
        else:
          print k+":", time.asctime(v)
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
  emd = ExtMetadata(sys.argv[1], sys.argv[2])
  emd.prettyPrint()

if __name__ == "__main__":
   main()
```

###### ```istat.py```

```python
#!/usr/bin/python
# This is a simple Python script that will
# print out metadata in an inode from an ext2/3/4 filesystem inside
# of an image file.
#
# Developed for PentesterAcademy by Dr. Phil Polstra (@ppolstra)

import extfs
import sys
import os.path
import subprocess
import struct
import time
from math import log

def usage():
   print("usage " + sys.argv[0] + " <image file> <offset> <inode number> \nDisplays inode information from an image file")
   exit(1)

def main():
  if len(sys.argv) < 3: 
     usage()

  # read first sector
  if not os.path.isfile(sys.argv[1]):
     print("File " + sys.argv[1] + " cannot be openned for reading")
     exit(1)
  emd = extfs.ExtMetadata(sys.argv[1], sys.argv[2])
  # get inode location
  inodeLoc = extfs.getInodeLoc(sys.argv[3], emd.superblock.inodesPerGroup)
  offset = emd.bgdList[inodeLoc[0]].inodeTable * emd.superblock.blockSize + \
    inodeLoc[1] * emd.superblock.inodeSize 
  with open(str(sys.argv[1]), 'rb') as f:
    f.seek(offset + int(sys.argv[2]) * 512)
    data = str(f.read(emd.superblock.inodeSize))

  inode = extfs.Inode(data, emd.superblock.inodeSize)
  print "Inode %s in Block Group %s at index %s" % (str(sys.argv[3]), str(inodeLoc[0]), str(inodeLoc[1]))
  inode.prettyPrint()

if __name__ == "__main__":
   main()
```

###### Mount the image ```2015-3-9.img```

```sh
u64@u64-VirtualBox:~/Desktop/code$ sudo ./mount-image.py ../2015-3-9.img
Looks like a MBR or VBR
Must be a MBR
Bootable:Type 131:Start 2048:Total sectors 33552384
Type 5:Start 33556478:Total sectors 4190210
Sorry GPT and extended partitions are not supported by this script!
<empty>
<empty>
u64@u64-VirtualBox:~/Desktop/code$
```

```sh
u64@u64-VirtualBox:~/Desktop/code$ mount
sysfs on /sys type sysfs (rw,nosuid,nodev,noexec,relatime)
proc on /proc type proc (rw,nosuid,nodev,noexec,relatime)
udev on /dev type devtmpfs (rw,nosuid,relatime,size=486680k,nr_inodes=121670,mode=755)
devpts on /dev/pts type devpts (rw,nosuid,noexec,relatime,gid=5,mode=620,ptmxmode=000)
tmpfs on /run type tmpfs (rw,nosuid,noexec,relatime,size=101576k,mode=755)
/dev/sda1 on / type ext4 (rw,relatime,errors=remount-ro,data=ordered)
securityfs on /sys/kernel/security type securityfs (rw,nosuid,nodev,noexec,relatime)
tmpfs on /dev/shm type tmpfs (rw,nosuid,nodev)
tmpfs on /run/lock type tmpfs (rw,nosuid,nodev,noexec,relatime,size=5120k)
tmpfs on /sys/fs/cgroup type tmpfs (ro,nosuid,nodev,noexec,mode=755)
cgroup on /sys/fs/cgroup/systemd type cgroup (rw,nosuid,nodev,noexec,relatime,xattr,release_agent=/lib/systemd/systemd-cgroups-agent,name=systemd)
pstore on /sys/fs/pstore type pstore (rw,nosuid,nodev,noexec,relatime)
cgroup on /sys/fs/cgroup/devices type cgroup (rw,nosuid,nodev,noexec,relatime,devices)
cgroup on /sys/fs/cgroup/blkio type cgroup (rw,nosuid,nodev,noexec,relatime,blkio)
cgroup on /sys/fs/cgroup/cpuset type cgroup (rw,nosuid,nodev,noexec,relatime,cpuset)
cgroup on /sys/fs/cgroup/net_cls,net_prio type cgroup (rw,nosuid,nodev,noexec,relatime,net_cls,net_prio)
cgroup on /sys/fs/cgroup/pids type cgroup (rw,nosuid,nodev,noexec,relatime,pids)
cgroup on /sys/fs/cgroup/freezer type cgroup (rw,nosuid,nodev,noexec,relatime,freezer)
cgroup on /sys/fs/cgroup/perf_event type cgroup (rw,nosuid,nodev,noexec,relatime,perf_event)
cgroup on /sys/fs/cgroup/memory type cgroup (rw,nosuid,nodev,noexec,relatime,memory)
cgroup on /sys/fs/cgroup/cpu,cpuacct type cgroup (rw,nosuid,nodev,noexec,relatime,cpu,cpuacct)
cgroup on /sys/fs/cgroup/hugetlb type cgroup (rw,nosuid,nodev,noexec,relatime,hugetlb)
systemd-1 on /proc/sys/fs/binfmt_misc type autofs (rw,relatime,fd=31,pgrp=1,timeout=0,minproto=5,maxproto=5,direct,pipe_ino=10883)
debugfs on /sys/kernel/debug type debugfs (rw,relatime)
mqueue on /dev/mqueue type mqueue (rw,relatime)
hugetlbfs on /dev/hugepages type hugetlbfs (rw,relatime)
fusectl on /sys/fs/fuse/connections type fusectl (rw,relatime)
tmpfs on /run/user/1000 type tmpfs (rw,nosuid,nodev,relatime,size=101576k,mode=700,uid=1000,gid=1000)
gvfsd-fuse on /run/user/1000/gvfs type fuse.gvfsd-fuse (rw,nosuid,nodev,relatime,user_id=1000,group_id=1000)
/home/u64/Desktop/2015-3-9.img on /media/part0 type ext4 (ro,noatime,data=ordered)
u64@u64-VirtualBox:~/Desktop/code$
```

###### Identify the inode value of suspicious files using ```stat```

```sh
u64@u64-VirtualBox:~/Desktop/code$ cd /media/part0/bin/
```

```sh
u64@u64-VirtualBox:/media/part0/bin$ stat xingyi_*
  File: 'xingyi_bindshell'
  Size: 14723     	Blocks: 32         IO Block: 4096   regular file
Device: 700h/1792d	Inode: 657103      Links: 1
Access: (0755/-rwxr-xr-x)  Uid: (    0/    root)   Gid: (    0/    root)
Access: 2015-03-12 10:37:39.618725412 -0700
Modify: 2015-03-12 10:37:39.498665408 -0700
Change: 2015-03-12 10:37:39.498665408 -0700
 Birth: -
  File: 'xingyi_reverse_shell'
  Size: 14056     	Blocks: 32         IO Block: 4096   regular file
Device: 700h/1792d	Inode: 657076      Links: 1
Access: (0755/-rwxr-xr-x)  Uid: (    0/    root)   Gid: (    0/    root)
Access: 2015-03-09 18:26:08.380753977 -0700
Modify: 2015-03-12 10:37:39.490661406 -0700
Change: 2015-03-12 10:37:39.490661406 -0700
 Birth: -
  File: 'xingyi_rootshell'
  Size: 9660      	Blocks: 24         IO Block: 4096   regular file
Device: 700h/1792d	Inode: 657109      Links: 1
Access: (0755/-rwxr-xr-x)  Uid: (    0/    root)   Gid: (    0/    root)
Access: 2015-03-09 18:26:08.444753981 -0700
Modify: 2015-03-12 10:37:39.614723412 -0700
Change: 2015-03-12 10:37:39.614723412 -0700
 Birth: -
u64@u64-VirtualBox:/media/part0/bin$
```

###### Identify the offset using ```fdisk```

```sh
u64@u64-VirtualBox:~/Desktop/code$ sudo fdisk ../2015-3-9.img

Welcome to fdisk (util-linux 2.27.1).
Changes will remain in memory only, until you decide to write them.
Be careful before using the write command.


Command (m for help): p
Disk ../2015-3-9.img: 18 GiB, 19327352832 bytes, 37748736 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: dos
Disk identifier: 0x0004565b

Device           Boot    Start      End  Sectors Size Id Type
../2015-3-9.img1 *        2048 33554431 33552384  16G 83 Linux
../2015-3-9.img2      33556478 37746687  4190210   2G  5 Extended
../2015-3-9.img5      33556480 37746687  4190208   2G 82 Linux swap / Solaris

Command (m for help): q

u64@u64-VirtualBox:~/Desktop/code$
```

###### Using ```istat.py```

```sh
u64@u64-VirtualBox:~/Desktop/code$ ./istat.py
usage ./istat.py <image file> <offset> <inode number>
Displays inode information from an image file
u64@u64-VirtualBox:~/Desktop/code$
```

```sh
u64@u64-VirtualBox:~/Desktop/code$ ./istat.py ../2015-3-9.img 2048 657103
Inode 657103 in Block Group 80 at index 1742
accessTime: Thu Mar 12 17:37:39 2015
accessTimeNanosecs: 618725412
block: []
blocks: 32
changeTime: Thu Mar 12 17:37:39 2015
changeTimeNanosecs: 498665408
checksum: 0
createTime: Tue Mar 10 01:26:08 2015
createTimeNanosecs: 380753977
Deleted: no
extendAttribs: 0
Extent depth: 0 entries: 1 max-entries: 4 generation: 0
Extent block: 0 data blocks: 715983 - 715986
fileSize: 14723
fileType: Regular File
flagList: ['Inode uses Extents', 'User-visible Flags', 'User-modifiable Flags']
flags: 524288
generation: 359961019
groupID: 0
inodeSize: 156
links: 1
mode: 33261
modeList: ['Others Exec', 'Others Read', 'Group Exec', 'Group Read', 'Owner Exec', 'Owner Write', 'Owner Read']
modifyTime: Thu Mar 12 17:37:39 2015
modifyTimeNanosecs: 498665408
osd1: 1
ownerID: 0
u64@u64-VirtualBox:~/Desktop/code$
```

```sh
u64@u64-VirtualBox:~/Desktop/code$ ./istat.py ../2015-3-9.img 2048 657076
Inode 657076 in Block Group 80 at index 1715
accessTime: Tue Mar 10 01:26:08 2015
accessTimeNanosecs: 380753977
block: []
blocks: 32
changeTime: Thu Mar 12 17:37:39 2015
changeTimeNanosecs: 490661406
checksum: 0
createTime: Tue Mar 10 01:26:08 2015
createTimeNanosecs: 380753977
Deleted: no
extendAttribs: 0
Extent depth: 0 entries: 1 max-entries: 4 generation: 0
Extent block: 0 data blocks: 715979 - 715982
fileSize: 14056
fileType: Regular File
flagList: ['Inode uses Extents', 'User-visible Flags', 'User-modifiable Flags']
flags: 524288
generation: 359961018
groupID: 0
inodeSize: 156
links: 1
mode: 33261
modeList: ['Others Exec', 'Others Read', 'Group Exec', 'Group Read', 'Owner Exec', 'Owner Write', 'Owner Read']
modifyTime: Thu Mar 12 17:37:39 2015
modifyTimeNanosecs: 490661406
osd1: 1
ownerID: 0
u64@u64-VirtualBox:~/Desktop/code$
```

```sh
u64@u64-VirtualBox:~/Desktop/code$ ./istat.py ../2015-3-9.img 2048 657109
Inode 657109 in Block Group 80 at index 1748
accessTime: Tue Mar 10 01:26:08 2015
accessTimeNanosecs: 444753981
block: []
blocks: 24
changeTime: Thu Mar 12 17:37:39 2015
changeTimeNanosecs: 614723412
checksum: 0
createTime: Tue Mar 10 01:26:08 2015
createTimeNanosecs: 444753981
Deleted: no
extendAttribs: 0
Extent depth: 0 entries: 1 max-entries: 4 generation: 0
Extent block: 0 data blocks: 715990 - 715992
fileSize: 9660
fileType: Regular File
flagList: ['Inode uses Extents', 'User-visible Flags', 'User-modifiable Flags']
flags: 524288
generation: 359961027
groupID: 0
inodeSize: 156
links: 1
mode: 33261
modeList: ['Others Exec', 'Others Read', 'Group Exec', 'Group Read', 'Owner Exec', 'Owner Write', 'Owner Read']
modifyTime: Thu Mar 12 17:37:39 2015
modifyTimeNanosecs: 614723412
osd1: 1
ownerID: 0
u64@u64-VirtualBox:~/Desktop/code$
```
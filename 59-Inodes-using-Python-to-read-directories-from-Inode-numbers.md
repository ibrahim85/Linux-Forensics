#### 59. Inodes: using Python to read directories from Inode numbers

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

# get a datablock from an image
def getDataBlock(imageFilename, offset, blockNo, blockSize=4096):
  with open(str(imageFilename), 'rb') as f:
    f.seek(blockSize * blockNo  + offset * 512)
    data = str(f.read(blockSize))
  return data




# This function will return a list of data blocks
# if extents are being used this should be simple assuming
# there is a single level to the tree.  
# For extents with multiple levels and for indirect blocks
# additional "disk access" is required.
def getBlockList(inode, imageFilename, offset, blockSize=4096):
  # now get the data blocks and output them
  datablocks = []
  if inode.extents:
    # great we are using extents
    # extent zero has the header
    # check for depth of zero which is most common
    if inode.extents[0].depth == 0:
      for i in range(1, inode.extents[0].entries + 1):
        sb = inode.extents[i].startHi * pow(2, 32) + inode.extents[i].startLo
        eb = sb + inode.extents[i].len # really ends in this minus 1
        for j in range(sb, eb):
          datablocks.append(j)
    else:
      # load this level of the tree
      currentLevel = inode.extents
      leafNode = []
      while currentLevel[0].depth != 0:
        # read the current level
        nextLevel = []
        for i in range(1, currentLevel[0].entries + 1):
          blockNo = currentLevel[i].leafLo + currentLevel[i].leafHi * pow(2, 32)
          currnode = getExtentTree(getDataBlock(imageFilename, offset, blockNo, blockSize))
          nextLevel.append(currnode)
          if currnode[0].depth == 0:
            leafNode.append(currnode[1: ]) # if there are leaves add them to the end
        currentLevel = nextLevel
      # now sort the list by logical block number
      leafNode.sort(key=lambda x: x.block)
      for leaf in leafNode:
        sb = leaf.startHi * pow(2, 32) + leaf.startLo
        eb = sb + leaf.len
        for j in range(sb, eb):
          datablocks.append(j)
  else:
    # we have the old school blocks
    blocks = inode.fileSize / blockSize
    # get the direct blocks
    for i in range(0, 12):
      datablocks.append(inode.block[i])
      if i >= blocks:
        break
    # now do indirect blocks
    if blocks > 12:
      iddata = getDataBlock(imageFilename, offset, inode.block[12], blockSize)
      for i in range(0, blockSize / 4):
        idblock = getU32(iddata, i * 4)
        if idblock == 0:
          break
        else:
          datablocks.append(idblock)
    # now double indirect blocks
    if blocks > (12 + blockSize / 4):
      diddata = getDataBlock(imageFilename, offset, inode.block[13], blockSize)
      for i in range(0, blockSize / 4):
        didblock = getU32(diddata, i * 4)
        if didblock == 0:
          break
        else:
          iddata = getDataBlock(imageFilename, offset, didblock, blockSize)
          for j in range(0, blockSize / 4):
            idblock = getU32(iddata, j * 4)
            if idblock == 0:
              break
            else:
              datablocks.append(idblock)
    # now triple indirect blocks
    if blocks > (12 + blockSize / 4 + blockSize * blockSize / 16):
      tiddata = getDataBlock(imageFilename, offset, inode.block[14], blockSize)
      for i in range(0, blockSize / 4):
        tidblock = getU32(tiddata, i * 4)
        if tidblock == 0:
          break
        else:
          diddata = getDataBlock(imageFilename, offset, tidblock, blockSize)
          for j in range(0, blockSize / 4):
            didblock = getU32(diddata, j * 4)
            if didblock == 0:
              break
            else:
              iddata = getDataBlock(imageFilename, offset, didblock, blockSize)
              for k in range(0, blockSize / 4):
                idblock = getU32(iddata, k * 4)
                if idblock == 0:
                  break
                else:
                  datablocks.append(idblock)
  return datablocks

def printFileType(ftype):
  if ftype == 0x0 or ftype > 7:
    return "Unknown"
  elif ftype == 0x1:
    return "Regular"
  elif ftype == 0x2:
    return "Directory"
  elif ftype == 0x3:
    return "Character device"
  elif ftype == 0x4:
    return "Block device"
  elif ftype == 0x5:
    return "FIFO"
  elif ftype == 0x6:
    return "Socket"
  elif ftype == 0x7:
    return "Symbolic link"


class DirectoryEntry():
  def __init__(self, data):
    self.inode = getU32(data)
    self.recordLen = getU16(data, 0x4)
    self.nameLen = getU8(data, 0x6)
    self.fileType = getU8(data, 0x7)
    self.filename = data[0x8 : 0x8 + self.nameLen]
  def prettyPrint(self):
    print("Inode: %s File type: %s Filename: %s" % (str(self.inode), printFileType(self.fileType), self.filename))

# parses directory entries in a data block that is passed in
def getDirectory(data):
  done = False
  retVal = []
  i = 0
  while not done:
    de = DirectoryEntry(data[i: ])
    if de.inode == 0:
      done = True
    else:
      retVal.append(de)
      i += de.recordLen
    if i >= len(data):
      break
  return retVal

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

###### ```ils.py```

```python
#!/usr/bin/python
# This is a simple Python script that will
# print out file for in an inode from an ext2/3/4 filesystem inside
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
   print("usage " + sys.argv[0] + " <image file> <offset> <inode number> \nDisplays directory for an inode from an image file")
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
  datablock = extfs.getBlockList(inode, sys.argv[1], sys.argv[2], emd.superblock.blockSize)
  data = ""
  for db in datablock:
    data += extfs.getDataBlock(sys.argv[1], long(sys.argv[2]), db, emd.superblock.blockSize)
  dir = extfs.getDirectory(data) 
  for fname in dir:
    fname.prettyPrint()

if __name__ == "__main__":
   main()
```

###### Using ```ils.py```

```sh
u64@u64-VirtualBox:~/Desktop/code$ ./ils.py
usage ./ils.py <image file> <offset> <inode number>
Displays directory for an inode from an image file
u64@u64-VirtualBox:~/Desktop/code$
```

- Identify the ```offset```

```sh
u64@u64-VirtualBox:~$ sudo fdisk Desktop/2015-3-9.img
[sudo] password for u64:

Welcome to fdisk (util-linux 2.27.1).
Changes will remain in memory only, until you decide to write them.
Be careful before using the write command.


Command (m for help): p
Disk Desktop/2015-3-9.img: 18 GiB, 19327352832 bytes, 37748736 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: dos
Disk identifier: 0x0004565b

Device                Boot    Start      End  Sectors Size Id Type
Desktop/2015-3-9.img1 *        2048 33554431 33552384  16G 83 Linux
Desktop/2015-3-9.img2      33556478 37746687  4190210   2G  5 Extended
Desktop/2015-3-9.img5      33556480 37746687  4190208   2G 82 Linux swap / Solaris

Command (m for help): q

u64@u64-VirtualBox:~$
```

- Identify ```inode``` of root directory

```sh
u64@u64-VirtualBox:~$ ls -id /media/part0/
2 /media/part0/
u64@u64-VirtualBox:~$
```

- ```ils.py``` for ```/```

```sh
u64@u64-VirtualBox:~/Desktop/code$ ./ils.py ../2015-3-9.img 2048 2
Inode: 2 File type: Directory Filename: .
Inode: 2 File type: Directory Filename: ..
Inode: 11 File type: Directory Filename: lost+found
Inode: 786433 File type: Directory Filename: etc
Inode: 524289 File type: Directory Filename: media
Inode: 655361 File type: Directory Filename: bin
Inode: 917505 File type: Directory Filename: boot
Inode: 131073 File type: Directory Filename: dev
Inode: 262145 File type: Directory Filename: home
Inode: 524290 File type: Directory Filename: lib
Inode: 655362 File type: Directory Filename: lib64
Inode: 786435 File type: Directory Filename: mnt
Inode: 131074 File type: Directory Filename: opt
Inode: 262146 File type: Directory Filename: proc
Inode: 917506 File type: Directory Filename: root
Inode: 917507 File type: Directory Filename: run
Inode: 524291 File type: Directory Filename: sbin
Inode: 131075 File type: Directory Filename: srv
Inode: 262147 File type: Directory Filename: sys
Inode: 655363 File type: Directory Filename: tmp
Inode: 8193 File type: Directory Filename: usr
Inode: 8194 File type: Directory Filename: var
Inode: 12 File type: Symbolic link Filename: vmlinuz
Inode: 13 File type: Symbolic link Filename: initrd.img
Inode: 922654 File type: Directory Filename: cdrom
u64@u64-VirtualBox:~/Desktop/code$
```

- ```ils.py``` for ```etc```

```sh
u64@u64-VirtualBox:~/Desktop/code$ ./ils.py ../2015-3-9.img 2048 786433
Inode: 786433 File type: Directory Filename: .
Inode: 2 File type: Directory Filename: ..
Inode: 786434 File type: Regular Filename: fstab
Inode: 786438 File type: Directory Filename: X11
Inode: 786439 File type: Directory Filename: acpi
Inode: 786440 File type: Directory Filename: alternatives
Inode: 786442 File type: Directory Filename: apparmor
Inode: 786444 File type: Directory Filename: apport
Inode: 786448 File type: Directory Filename: avahi
Inode: 786449 File type: Directory Filename: bash_completion.d
Inode: 786450 File type: Directory Filename: bluetooth
Inode: 786451 File type: Directory Filename: brltty
Inode: 786452 File type: Directory Filename: ca-certificates
Inode: 786453 File type: Directory Filename: calendar
Inode: 786455 File type: Directory Filename: compizconfig
Inode: 786456 File type: Directory Filename: console-setup
Inode: 786457 File type: Directory Filename: cracklib
Inode: 786458 File type: Directory Filename: cron.d
Inode: 786459 File type: Directory Filename: cron.daily
Inode: 786462 File type: Directory Filename: cron.weekly
Inode: 786464 File type: Directory Filename: cupshelpers
Inode: 786468 File type: Directory Filename: depmod.d
Inode: 786469 File type: Directory Filename: dhcp
Inode: 786474 File type: Directory Filename: emacs
Inode: 786475 File type: Directory Filename: firefox
Inode: 786478 File type: Directory Filename: gconf
Inode: 786480 File type: Directory Filename: ghostscript
Inode: 786481 File type: Directory Filename: gnome
Inode: 786483 File type: Directory Filename: groff
Inode: 786484 File type: Directory Filename: grub.d
Inode: 786487 File type: Directory Filename: hp
Inode: 786496 File type: Directory Filename: kernel
Inode: 786498 File type: Directory Filename: ldap
Inode: 786501 File type: Directory Filename: libreoffice
Inode: 786502 File type: Directory Filename: lightdm
Inode: 786503 File type: Directory Filename: logcheck
Inode: 786509 File type: Directory Filename: newt
Inode: 786514 File type: Directory Filename: perl
Inode: 786515 File type: Directory Filename: pki
Inode: 786516 File type: Directory Filename: pm
Inode: 786517 File type: Directory Filename: polkit-1
Inode: 786519 File type: Directory Filename: profile.d
Inode: 786523 File type: Directory Filename: python3
Inode: 786524 File type: Directory Filename: python3.4
Inode: 786525 File type: Directory Filename: rc0.d
Inode: 786526 File type: Directory Filename: rc1.d
Inode: 786531 File type: Directory Filename: rc6.d
Inode: 787871 File type: Directory Filename: wildmidi
Inode: 786536 File type: Directory Filename: samba
Inode: 786538 File type: Directory Filename: security
Inode: 786541 File type: Directory Filename: sgml
Inode: 786544 File type: Directory Filename: speech-dispatcher
Inode: 786546 File type: Directory Filename: ssl
Inode: 786547 File type: Directory Filename: sudoers.d
Inode: 786550 File type: Directory Filename: terminfo
Inode: 786551 File type: Directory Filename: thunderbird
Inode: 786553 File type: Directory Filename: udisks2
Inode: 786556 File type: Directory Filename: update-motd.d
Inode: 786557 File type: Directory Filename: update-notifier
Inode: 786558 File type: Directory Filename: usb_modeswitch.d
Inode: 786559 File type: Directory Filename: vim
Inode: 786560 File type: Directory Filename: wpa_supplicant
Inode: 786561 File type: Directory Filename: xdg
Inode: 786562 File type: Directory Filename: xml
Inode: 786563 File type: Directory Filename: xul-ext
Inode: 786565 File type: Regular Filename: adduser.conf
Inode: 786566 File type: Regular Filename: anacrontab
Inode: 786568 File type: Regular Filename: bash.bashrc
Inode: 786569 File type: Regular Filename: bash_completion
Inode: 786572 File type: Symbolic link Filename: blkid.tab
Inode: 786574 File type: Regular Filename: brltty.conf
Inode: 786576 File type: Regular Filename: colord.conf
Inode: 786577 File type: Regular Filename: crontab
Inode: 786578 File type: Regular Filename: debconf.conf
Inode: 786579 File type: Regular Filename: debian_version
Inode: 786580 File type: Regular Filename: deluser.conf
Inode: 786583 File type: Regular Filename: fuse.conf
Inode: 786584 File type: Regular Filename: gai.conf
Inode: 786646 File type: Regular Filename: gshadow
Inode: 786587 File type: Regular Filename: hdparm.conf
Inode: 786589 File type: Regular Filename: hostname
Inode: 786591 File type: Regular Filename: hosts.allow
Inode: 786593 File type: Regular Filename: inputrc
Inode: 786594 File type: Regular Filename: insserv.conf
Inode: 786595 File type: Regular Filename: issue
Inode: 786596 File type: Regular Filename: issue.net
Inode: 788846 File type: Regular Filename: kernel-img.conf
Inode: 818475 File type: Regular Filename: ld.so.cache
Inode: 786600 File type: Regular Filename: ld.so.conf
Inode: 786607 File type: Regular Filename: logrotate.conf
Inode: 786608 File type: Regular Filename: lsb-release
Inode: 786609 File type: Regular Filename: ltrace.conf
Inode: 786615 File type: Regular Filename: mime.types
Inode: 786618 File type: Regular Filename: mtools.conf
Inode: 786620 File type: Regular Filename: netscsid.conf
Inode: 818492 File type: Regular Filename: ftpallow
Inode: 786623 File type: Regular Filename: nsswitch.conf
Inode: 786624 File type: Regular Filename: os-release
Inode: 786630 File type: Regular Filename: profile
Inode: 786631 File type: Regular Filename: protocols
Inode: 786635 File type: Regular Filename: rmt
Inode: 786638 File type: Regular Filename: securetty
Inode: 786639 File type: Regular Filename: sensors3.conf
Inode: 786640 File type: Regular Filename: services
Inode: 786641 File type: Regular Filename: shadow
Inode: 786644 File type: Regular Filename: subuid
Inode: 786648 File type: Regular Filename: sudoers
Inode: 786652 File type: Regular Filename: updatedb.conf
Inode: 786654 File type: Regular Filename: usb_modeswitch.conf
Inode: 786655 File type: Symbolic link Filename: vtrgb
Inode: 786657 File type: Regular Filename: wodim.conf
Inode: 786658 File type: Regular Filename: zsh_command_not_found
Inode: 818486 File type: Regular Filename: mtab
Inode: 818265 File type: Regular Filename: passwd-
Inode: 786629 File type: Symbolic link Filename: printcap
Inode: 786627 File type: Regular Filename: shadow-
Inode: 786575 File type: Regular Filename: ca-certificates.conf.dpkg-old
Inode: 818533 File type: Directory Filename: chromium-browser
Inode: 786537 File type: Directory Filename: sane.d
Inode: 786552 File type: Directory Filename: udev
Inode: 786601 File type: Regular Filename: legal
Inode: 786573 File type: Regular Filename: brlapi.key
Inode: 786522 File type: Directory Filename: python2.7
Inode: 786581 File type: Regular Filename: drirc
Inode: 786470 File type: Directory Filename: dictionaries-common
Inode: 786485 File type: Directory Filename: gtk-2.0
Inode: 786477 File type: Directory Filename: fstab.d
Inode: 786651 File type: Regular Filename: ucf.conf
Inode: 786460 File type: Directory Filename: cron.hourly
Inode: 786571 File type: Regular Filename: blkid.conf
Inode: 786567 File type: Regular Filename: apg.conf
Inode: 786656 File type: Regular Filename: wgetrc
Inode: 786617 File type: Regular Filename: modules
Inode: 786647 File type: Regular Filename: subuid-
Inode: 786650 File type: Regular Filename: timezone
Inode: 786545 File type: Directory Filename: ssh
Inode: 786602 File type: Regular Filename: libaudit.conf
Inode: 786543 File type: Directory Filename: skel
Inode: 786632 File type: Regular Filename: rc.local
Inode: 786488 File type: Directory Filename: ifplugd
Inode: 786649 File type: Regular Filename: sysctl.conf
Inode: 786473 File type: Directory Filename: dpkg
Inode: 786605 File type: Regular Filename: localtime
Inode: 786504 File type: Directory Filename: logrotate.d
Inode: 786510 File type: Directory Filename: obex-data-server
Inode: 786653 File type: Regular Filename: upstart-xsessions
Inode: 786472 File type: Directory Filename: doc-base
Inode: 786518 File type: Directory Filename: ppp
Inode: 818539 File type: Regular Filename: mailcap
Inode: 786493 File type: Directory Filename: insserv.conf.d
Inode: 786437 File type: Directory Filename: UPower
Inode: 786530 File type: Directory Filename: rc5.d
Inode: 786614 File type: Regular Filename: manpath.config
Inode: 786508 File type: Directory Filename: network
Inode: 786549 File type: Directory Filename: systemd
Inode: 786625 File type: Regular Filename: pam.conf
Inode: 786499 File type: Directory Filename: libnl-3
Inode: 786598 File type: Regular Filename: kerneloops.conf
Inode: 786619 File type: Regular Filename: nanorc
Inode: 786555 File type: Directory Filename: update-manager
Inode: 786512 File type: Directory Filename: pam.d
Inode: 786592 File type: Regular Filename: hosts.deny
Inode: 786606 File type: Regular Filename: login.defs
Inode: 786645 File type: Regular Filename: subgid-
Inode: 786542 File type: Directory Filename: signon-ui
Inode: 786643 File type: Regular Filename: signond.conf
Inode: 786610 File type: Regular Filename: magic
Inode: 786626 File type: Regular Filename: popularity-contest.conf
Inode: 786642 File type: Regular Filename: shells
Inode: 786447 File type: Directory Filename: at-spi2
Inode: 786482 File type: Directory Filename: gnome-app-install
Inode: 786588 File type: Regular Filename: host.conf
Inode: 786500 File type: Directory Filename: libpaper.d
Inode: 818540 File type: Regular Filename: group
Inode: 818262 File type: Regular Filename: mtab.fuselock
Inode: 786621 File type: Regular Filename: networks
Inode: 786486 File type: Directory Filename: gtk-3.0
Inode: 786465 File type: Directory Filename: dbus-1
Inode: 786554 File type: Directory Filename: ufw
Inode: 786511 File type: Directory Filename: opt
Inode: 786471 File type: Directory Filename: dnsmasq.d
Inode: 786497 File type: Directory Filename: ld.so.conf.d
Inode: 786476 File type: Directory Filename: fonts
Inode: 786492 File type: Directory Filename: insserv
Inode: 786582 File type: Regular Filename: environment
Inode: 786436 File type: Directory Filename: NetworkManager
Inode: 786611 File type: Regular Filename: magic.mime
Inode: 786520 File type: Directory Filename: pulse
Inode: 786479 File type: Directory Filename: gdb
Inode: 786495 File type: Directory Filename: kbd
Inode: 786548 File type: Directory Filename: sysctl.d
Inode: 786446 File type: Directory Filename: aptdaemon
Inode: 786636 File type: Regular Filename: rpc
Inode: 786628 File type: Regular Filename: pnm2ppa.conf
Inode: 786441 File type: Directory Filename: apm
Inode: 812937 File type: Regular Filename: ca-certificates.conf
Inode: 786535 File type: Directory Filename: rsyslog.d
Inode: 786467 File type: Directory Filename: default
Inode: 786590 File type: Regular Filename: hosts
Inode: 786506 File type: Directory Filename: modprobe.d
Inode: 786570 File type: Regular Filename: bindresvport.blacklist
Inode: 786529 File type: Directory Filename: rc4.d
Inode: 786513 File type: Directory Filename: pcmcia
Inode: 786454 File type: Directory Filename: chatscripts
Inode: 786527 File type: Directory Filename: rc2.d
Inode: 786613 File type: Regular Filename: mailcap.order
Inode: 786539 File type: Directory Filename: selinux
Inode: 786521 File type: Directory Filename: python
Inode: 786489 File type: Directory Filename: init
Inode: 786445 File type: Directory Filename: apt
Inode: 818452 File type: Regular Filename: subgid
Inode: 786604 File type: Regular Filename: locale.alias
Inode: 786490 File type: Directory Filename: init.d
Inode: 786528 File type: Directory Filename: rc3.d
Inode: 788850 File type: Regular Filename: papersize
Inode: 786491 File type: Directory Filename: initramfs-tools
Inode: 786534 File type: Directory Filename: resolvconf
Inode: 786603 File type: Regular Filename: lintianrc
Inode: 786461 File type: Directory Filename: cron.monthly
Inode: 786443 File type: Directory Filename: apparmor.d
Inode: 786463 File type: Directory Filename: cups
Inode: 786637 File type: Regular Filename: rsyslog.conf
Inode: 786540 File type: Directory Filename: sensors.d
Inode: 818270 File type: Regular Filename: passwd
Inode: 786494 File type: Directory Filename: iproute2
Inode: 786634 File type: Symbolic link Filename: resolv.conf
Inode: 786507 File type: Directory Filename: modules-load.d
Inode: 786466 File type: Directory Filename: dconf
Inode: 786564 File type: Regular Filename: .pwd.lock
Inode: 786532 File type: Directory Filename: rcS.d
Inode: 786616 File type: Regular Filename: mke2fs.conf
Inode: 818258 File type: Regular Filename: iftab
Inode: 818266 File type: Regular Filename: gshadow-
Inode: 786586 File type: Regular Filename: group-
Inode: 787546 File type: Directory Filename: openal
Inode: 786633 File type: Regular Filename: ts.conf
Inode: 818330 File type: Directory Filename: timidity
Inode: 812962 File type: Regular Filename: inetd.conf
Inode: 818509 File type: Regular Filename: ftpusers
Inode: 818494 File type: Directory Filename: pure-ftpd
u64@u64-VirtualBox:~/Desktop/code$
```

- ```ils.py``` for ```tmp```

```sh
u64@u64-VirtualBox:~/Desktop/code$ ./ils.py ../2015-3-9.img 2048 655363
Inode: 655363 File type: Directory Filename: .
Inode: 2 File type: Directory Filename: ..
Inode: 655484 File type: Directory Filename: .X11-unix
Inode: 655485 File type: Directory Filename: .ICE-unix
Inode: 655486 File type: Regular Filename: .X0-lock
Inode: 655488 File type: Regular Filename: config-err-dqpfMl
Inode: 655494 File type: Regular Filename: unity_support_test.1
Inode: 657110 File type: Regular Filename: xingyi_bindshell_pid
Inode: 657112 File type: Regular Filename: xingyi_bindshell_port
u64@u64-VirtualBox:~/Desktop/code$
```
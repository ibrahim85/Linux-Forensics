#!/usr/bin/python
# This is a simple Python script that will
# attempt to mount partitions inside an extended
# partition from an image file.
# Images are mounted read-only.  
#
# Developed for PentesterAcademy by Dr. Phil Polstra

import sys
import os.path
import subprocess

class MbrRecord():
   def __init__(self, sector, partno):
      self.partno = partno
      offset = 446 + partno * 16
      self.active = False
      if sector[offset] == '\x80':
         self.active = True
      self.type = ord(sector[offset+4])
      self.empty = False
      if self.type == 0:
         self.empty = True
      self.start = ord(sector[offset+8]) + ord(sector[offset+9]) * 256 + \
         ord(sector[offset+10]) * 65536 + ord(sector[offset+11]) * 16777216 
      self.sectors = ord(sector[offset+12]) + ord(sector[offset+13]) * 256 + \
         ord(sector[offset+14]) * 65536 + ord(sector[offset+15]) * 16777216
   
   def printPart(self):
      if self.empty == True:
         print("<empty>")
      else:
         outstr = "" 
         if self.active == True:
            outstr += "Bootable:"
         outstr += "Type " + hex(self.type) + ":"
         outstr += "Start " + str(self.start) + ":"
         outstr += "Total sectors " + str(self.sectors)
         print(outstr)

def usage():
   print("usage " + sys.argv[0] + \
       " <image file>\nAttempts to mount extended partitions from an image file")
   exit(1)

def main():
  if len(sys.argv) < 2: 
     usage()

  extParts = [0x05, 0x0f, 0x85, 0x91, 0x9b, 0xc5, 0xe4]
  swapParts = [0x42, 0x82, 0xb8, 0xc3, 0xfc]

  # read first sector
  if not os.path.isfile(sys.argv[1]):
     print("File " + sys.argv[1] + " cannot be openned for reading")
     exit(1)
  with open(sys.argv[1], 'rb') as f:
    sector = str(f.read(512))
    
  if (sector[510] == "\x55" and sector[511] == "\xaa"):
     print("Looks like a MBR or VBR")
     # if it is an MBR bytes 446, 462, 478, and 494 must be 0x80 or 0x00
     if (sector[446] == '\x80' or sector[446] == '\x00') and \
        (sector[462] == '\x80' or sector[462] == '\x00') and \
        (sector[478] == '\x80' or sector[478] == '\x00') and \
        (sector[494] == '\x80' or sector[494] == '\x00'):
        print("Must be a MBR")
        parts = [MbrRecord(sector, 0), MbrRecord(sector, 1), \
           MbrRecord(sector, 2), MbrRecord(sector, 3)]
        for p in parts:
           p.printPart()
           if not p.empty:
              if p.type in extParts:
                 print("Found an extended partion at sector %s" % str(p.start))
                 bottomOfRabbitHole = False
                 extendPartStart = p.start
                 extPartNo = 5
                 while not bottomOfRabbitHole:
                    # get the linked list MBR entry
                    with open(sys.argv[1], 'rb') as f:
                       f.seek(extendPartStart * 512) 
                       llSector = str(f.read(512))
                    extParts = [MbrRecord(llSector, 0), MbrRecord(llSector, 1)]
                    # try and mount the first partition
                    if extParts[0].type in swapParts:
                       print("Skipping swap partition")
                    else:
                       mountpath = '/media/part%s' % str(extPartNo)
                       if not os.path.isdir(mountpath):
                          subprocess.call(['mkdir', mountpath])
                       mountopts = 'loop,ro,noatime,offset=%s' \
                          % str((extParts[0].start + extendPartStart) * 512)
                       print("Attempting to mount extend part type %s at sector %s" \
                          % (hex(extParts[0].type), \
                          str(extendPartStart + extParts[0].start))) 
                       subprocess.call(['mount', '-o', mountopts, sys.argv[1], mountpath])
                    if extParts[1].type == 0:
                       bottomOfRabbitHole = True
                       print("Found the bottom of the rabbit hole")
                    else:
                       extendPartStart += extParts[1].start
                       extPartNo += 1
 
if __name__ == "__main__":
   main()


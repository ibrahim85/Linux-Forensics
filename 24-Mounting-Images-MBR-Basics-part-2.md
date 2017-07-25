#### 24. Mounting Images: MBR Basics part 2

Mount an image which is ```MBR``` based without extended partitions

###### ```mount-image.py```

```python
#!/usr/bin/python
# This is a simple Python script that will
# attempt to mount partitions from an image file.
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
         outstr += "Type " + str(self.type) + ":"
         outstr += "Start " + str(self.start) + ":"
         outstr += "Total sectors " + str(self.sectors)
         print(outstr)

def usage():
   print("usage " + sys.argv[0] + " <image file>\nAttempts to mount partitions from an image file")
   exit(1)

def main():
  if len(sys.argv) < 2: 
     usage()
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
              notsupParts = [0x05, 0x0f, 0x85, 0x91, 0x9b, 0xc5, 0xe4, 0xee]
              if p.type in notsupParts:
                 print("Sorry GPT and extended partitions are not supported by this script!")
              else:
                 mountpath = '/media/part%s' % str(p.partno)
                 if not os.path.isdir(mountpath):
                    subprocess.call(['mkdir', mountpath])
                 mountopts = 'loop,ro,noatime,offset=%s' % str(p.start * 512)
                 subprocess.call(['mount', '-o', mountopts, sys.argv[1], mountpath])
     else:
        print("Appears to be a VBR\nAttempting to mount")
        if not os.path.isdir('/media/part1'):
           subprocess.call(['mkdir', '/media/part1'])
        subprocess.call(['mount', '-o', 'loop,ro,noatime', sys.argv[1], '/media/part1'])
 
if __name__ == "__main__":
   main()
```

```sh
u64@u64-VirtualBox:~/Desktop$ file 2015-3-9.img
2015-3-9.img: DOS/MBR boot sector
u64@u64-VirtualBox:~/Desktop$
```

```sh
u64@u64-VirtualBox:~/Desktop$ ll 2015-3-9.img
-rw-rw-r-- 1 u64 u64 19327352832 Mar 12  2015 2015-3-9.img
u64@u64-VirtualBox:~/Desktop$
```

```sh
u64@u64-VirtualBox:~/Desktop$ sudo ./mount-image.py 2015-3-9.img
Looks like a MBR or VBR
Must be a MBR
Bootable:Type 131:Start 2048:Total sectors 33552384
mount: /home/u64/Desktop/2015-3-9.img is already mounted
Type 5:Start 33556478:Total sectors 4190210
Sorry GPT and extended partitions are not supported by this script!
<empty>
<empty>
u64@u64-VirtualBox:~/Desktop$
```

```sh
u64@u64-VirtualBox:~/Desktop$ mount
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
cgroup on /sys/fs/cgroup/memory type cgroup (rw,nosuid,nodev,noexec,relatime,memory)
cgroup on /sys/fs/cgroup/perf_event type cgroup (rw,nosuid,nodev,noexec,relatime,perf_event)
cgroup on /sys/fs/cgroup/net_cls,net_prio type cgroup (rw,nosuid,nodev,noexec,relatime,net_cls,net_prio)
cgroup on /sys/fs/cgroup/pids type cgroup (rw,nosuid,nodev,noexec,relatime,pids)
cgroup on /sys/fs/cgroup/cpu,cpuacct type cgroup (rw,nosuid,nodev,noexec,relatime,cpu,cpuacct)
cgroup on /sys/fs/cgroup/cpuset type cgroup (rw,nosuid,nodev,noexec,relatime,cpuset)
cgroup on /sys/fs/cgroup/freezer type cgroup (rw,nosuid,nodev,noexec,relatime,freezer)
cgroup on /sys/fs/cgroup/blkio type cgroup (rw,nosuid,nodev,noexec,relatime,blkio)
cgroup on /sys/fs/cgroup/devices type cgroup (rw,nosuid,nodev,noexec,relatime,devices)
cgroup on /sys/fs/cgroup/hugetlb type cgroup (rw,nosuid,nodev,noexec,relatime,hugetlb)
systemd-1 on /proc/sys/fs/binfmt_misc type autofs (rw,relatime,fd=24,pgrp=1,timeout=0,minproto=5,maxproto=5,direct,pipe_ino=10883)
mqueue on /dev/mqueue type mqueue (rw,relatime)
debugfs on /sys/kernel/debug type debugfs (rw,relatime)
hugetlbfs on /dev/hugepages type hugetlbfs (rw,relatime)
fusectl on /sys/fs/fuse/connections type fusectl (rw,relatime)
tmpfs on /run/user/1000 type tmpfs (rw,nosuid,nodev,relatime,size=101576k,mode=700,uid=1000,gid=1000)
gvfsd-fuse on /run/user/1000/gvfs type fuse.gvfsd-fuse (rw,nosuid,nodev,relatime,user_id=1000,group_id=1000)
2015-3-9.img on /home/u64/Desktop/part0 type proc (ro,noatime,loop)
/home/u64/Desktop/2015-3-9.img on /media/part0 type ext4 (ro,noatime,data=ordered)
u64@u64-VirtualBox:~/Desktop$
```

```sh
u64@u64-VirtualBox:~/Desktop$ ls /media/part0/
bin   cdrom  etc   initrd.img  lib64       media  opt   root  sbin  sys  usr  vmlinuz
boot  dev    home  lib         lost+found  mnt    proc  run   srv   tmp  var
u64@u64-VirtualBox:~/Desktop$
```
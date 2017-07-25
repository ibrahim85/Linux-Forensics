#### 19. Making Filesystem Images

###### Image File Formats- Raw- Proprietary with embedded metadata 
- Proprietary with metadata in separate file 
- Raw with hashes stored in a separate file

###### Creating an Image- Raw image

```dd``` - convert and copy a file

```
dd if=<subject device> of=<image file> bs=512
```
- Raw image with hashes

```dcfldd``` - enhanced version of dd for forensics and security

```
dcfldd if=<subject device> of=<image file> bs=512 hash=<algorithm> hashwindow=<chunk size> hashlog=<hash file>
```

###### Write Blocking- Hardware write blockers	- Commercial blockers for SATA only $350+	- USB write blocker
		- Cheap at about $25
		- Slow due to limits of microcontroller that is full-speed (```12 Mbps```) only

- Software write blocking	- Use ```udev``` rules
	- Boot live forensics Linux on subject computer
	- Boot live forensics Linux on forensics workstation
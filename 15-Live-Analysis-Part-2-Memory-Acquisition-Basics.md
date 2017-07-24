#### 15. Live Analysis Part 2: Memory Acquisition Basics
- Physical memory could be dumped via ```/dev/mem```
- Virtual memory could be dumped via ```/dev/kmem```
- Both of these are now disabled, limited, or at out removed	- Serious security issue to have these in userland 
	- ```/dev/mem``` was limited to first 896MB of RAM

###### Modern Acquisition: Hard Way

- [```Fmem```](http://hysteria.cz/niekt0/)
	- Download [fmem](http://hysteria.cz/niekt0/fmem/fmem_current.tgz)

	```	$ make	$ sudo make install
	```
	
	- Works just like ```/dev/mem``` but creates ```/dev/fmem``` 
	- Use ```/proc/iomem``` to determine appropriate bits	- Raw memory image is difficult to use for more than simple searches

###### Modern Acquisition: Easy Way

- [```LiME```](https://github.com/504ensicsLabs/LiME)
	- Linux Memory Extractor (LiME)
	- Must be built for an exact kernel 
	- Should not be built on subject machine
	- For identical versions of Ubuntu use 
	```
	sudo apt-get install lime-forensics-dkms
	```	- For every other situation must download from [github](https://github.com/504ensicsLabs/LiME) compile with correct kernel headers	- Compile with ```make``` for current kernel or ```make -C /lib/modules/<kernel version>/build M=$PWD``` for other kernels

###### Using LiME

- Pick format	- Raw (every segment concatenated together) 
	- Padded (same as raw, but with zeroes in right bits)
	- Lime (recommended format with metadata)

- Pick destination (path)	- File (external drive please!)	- Network port (use netcat on forensics workstation)

```
sudo insmod lime.ko “path=<path> format=<format>”
```
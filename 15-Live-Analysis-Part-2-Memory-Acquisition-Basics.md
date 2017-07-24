#### 15. Live Analysis Part 2: Memory Acquisition Basics

- Virtual memory could be dumped via ```/dev/kmem```
- Both of these are now disabled, limited, or at out removed
	- ```/dev/mem``` was limited to first 896MB of RAM

###### Modern Acquisition: Hard Way

- [```Fmem```](http://hysteria.cz/niekt0/)
	- Download [fmem](http://hysteria.cz/niekt0/fmem/fmem_current.tgz)

	```
	```
	
	- Works just like ```/dev/mem``` but creates ```/dev/fmem``` 
	- Use ```/proc/iomem``` to determine appropriate bits

###### Modern Acquisition: Easy Way

- [```LiME```](https://github.com/504ensicsLabs/LiME)
	- Linux Memory Extractor (LiME)
	- Must be built for an exact kernel 
	- Should not be built on subject machine
	- For identical versions of Ubuntu use 
	```
	sudo apt-get install lime-forensics-dkms
	```

###### Using LiME

- Pick format
	- Padded (same as raw, but with zeroes in right bits)
	- Lime (recommended format with metadata)

- Pick destination (path)

```
sudo insmod lime.ko “path=<path> format=<format>”
```
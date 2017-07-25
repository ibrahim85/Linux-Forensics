#### 18. Shutting down the subject system

###### Last Steps Before Shutdown- We have memory dump- Any last minute scans or repeats of initial scans 
- Decide on normal shutdown or pulling the plug

###### Normal Shutdown- Filesystems should be clean- Malware might cleanup after itself and/or destroy evidence

###### Pulling the Plug- Filesystem may not be clean 
	- Could call sync before pulling the plug- No chance for malware to destroy any info 
- Memory image already collected


```sh
u64@ubuntu64:~$ sync
```
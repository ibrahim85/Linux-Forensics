#### 1. Course Introduction

###### Live Response
- Human interactions
- Creating a live response kit
- Transporting data across a network
- Collecting volatile data
- Determining if dead analysis is justied
- Dumping RAM

###### Acquiring filesystem images
- Using dd
- Using dcfldd
- Write blocking
- Software blockers	- Udev rules
	- Forensic Linux distros 
- Hardware blockers

###### Analyzing filesystem
- Mounting image files	- Finding the strange 
	- Searching tools 
	- Authentication related files 
	- Recovering deleted files 
	- Finding hidden information

###### The Sleuth Kit (TSK) and Autopsy
- Volume information 
- Filesystem information 
- Inodes
- Directory entries 
- Constructing timelines

###### Timeline Analysis
- When was system installed, upgraded, booted, etc.
- Newly created files (malware) 
- Changed files (trojans)
- Files in the wrong place (exfiltration)

###### Digging deeper into Linux filesystems

- Disk editors	- Active@ Disk Editor
	- Autopsy 
- ExtX- Other Linux filesystem 
- Searching unallocated space

###### Network forensics
- Using snort on packet captures
- Using tcpstat
- Seperating conversations with tcpflow- Tracing backdoors with tcpflow

###### File forensics- Using file signatures- Searching through swap space

###### Web browsing reconstruction

- Cookies- Search history 
- Browser caches

###### Unknown files
- Comparing hashes to know values
- File and strings commands
- Viewing symbols with nm
- Reading ELF files 
- objdump
- gdb

###### Memory Forensics
- Volatility Profiles- Retrieving process information 
- Recovering command line arguments 
- Rebuilding environment variables 
- Listing open files
- Retrieving bash information 
- Reconstructing network artifacts 
- Kernel information
- Volatile file system information 
- Detecting user mode rootkits 
- Detecting kernel rootkits

###### Reversing Linux Malware

###### Digging deeper into ELF- Headers 
- Sections
- Strings
- Symbol tables 
- Program headers
- Program loading
- Dynamic linking

###### Command line analysis tools

- strings
- strace 
- ltrace

###### Running malware (carefully)

- Virtual machine setup
- Capturing network traffic
- Leveraging gdb

###### Writing the reports

- Autopsy
- Dradis
- OpenOffice
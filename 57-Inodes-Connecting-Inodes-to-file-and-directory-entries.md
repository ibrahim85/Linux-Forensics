#### 57. Inodes: Connecting Inodes to file and directory entries

###### Directories
- Map names to inodes- Each directory is treated as a file

![Image of inode](images/57/1.jpeg)

###### Directories (Filetype feature)

![Image of inode](images/57/2.jpeg)

###### Directory Tail

- Phony entry at the end of each directory block 
- Adds checksum to directories

![Image of inode](images/57/3.jpeg)

###### Hash Directories

- Meant to improve performance- Fools old systems by storing hash entries after “end” of directory block
- Directory nodes are stored in a hashed balanced tree (hashed btree = htree)
- The ```ext4_index``` flag is set for an inode if it contains a directory htree
- ```.``` and ```..``` entries stored in traditional way at start of the block

###### Root Hash Directory Block

![Image of inode](images/57/4.jpeg)

###### Interior Node Hash Directory Block

![Image of inode](images/57/5.jpeg)###### Hash Directory Entry

![Image of inode](images/57/6.jpeg)
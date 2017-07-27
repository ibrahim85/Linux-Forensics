#### 52. Inodes: Digging Deeper

###### Inode Size
- Standard is ```128 bytes``` for ```Ext2``` and ```Ext3``` 
- ```Ext4``` currently uses ```156 bytes```
- ```Ext4``` allocates ```256 bytes``` on disk to allow for future expansion

###### Finding Inodes

- ```Block group = (Inode number - 1) / (Inodes per group)```
- ```Index within group = (Inode number - 1) modulus (Inodes/group)```
- ```Offset into inode table = index * (Inode size)```

###### Inode Structure

![Image of inode](images/52/1.jpeg)

![Image of inode](images/52/2.jpeg)

###### Inode Structure Extended (Ext4)

![Image of inode](images/52/3.jpeg)

###### Special Inodes	

![Image of inode](images/52/4.jpeg)
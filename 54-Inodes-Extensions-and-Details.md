#### 54. Inodes: Extensions and Details

###### File Mode

![Image of inode](images/54/1.jpeg)

###### Inode Flags (low word)

![Image of inode](images/54/2.jpeg)

###### Inode Flags (high word)

![Image of inode](images/54/3.jpeg)

###### Inode Timestamps

- Change/Modify/Access/Delete timestamps in lower ```128 bytes```
- Timestamps stored in Signed ```32-bit``` seconds since epoch
- Extra timestamp values in upper bytes	- Lowest ```2 bits``` used to extend timestamp to ```34-bit``` value 
	- Upper ```30 bits``` provide nanosecond accuracy of timestamps
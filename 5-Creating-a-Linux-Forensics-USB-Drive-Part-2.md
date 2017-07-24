##### 5. Creating a Linux Forensics USB Drive Part 2

###### Create ```vmdk``` from ```/dev/sd*```

```sh
VBoxManage internalcommands createrawvmdk -filename /path/to/file.vmdk -rawdisk /dev/sdb
```

###### Create a virtual machine in VirtualBox using ```file.vmdk```

Virtualbox &rightarrow; New &rightarrow; Use existing virtual hard drive file &rightarrow; file.vmdk &rightarrow; Create

Settings &rightarrow; System &rightarrow; Motherboard &rightarrow; Enable EFI
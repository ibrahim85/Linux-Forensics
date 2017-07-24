#### 3. Forensic Basics: First Steps

###### Response Kit

- Complete set of system binaries and forensics tools
	- 32-bit and 64-bit versions
- Ubuntu 64-bit versions
- Hardware	- Write blockers 
	- Media	- Forensic laptop
- Ideally with USB 3.0 port(s)
- Wired networking 
- Notebook, etc. for documentation

###### [Setup Ubuntu](https://digital-forensics.sans.org/community/downloads)

```sh
u64@ubuntu64:~/Desktop$ wget https://github.com/sans-dfir/sift-cli/releases/download/v1.5.1/sift-cli-linux
u64@ubuntu64:~/Desktop$ wget https://github.com/sans-dfir/sift-cli/releases/download/v1.5.1/sift-cli-linux.sha256.asc
```

```sh
u64@ubuntu64:~/Desktop$ ls -l
total 52968
-rw-rw-r-- 1 u64 u64 54233167 Jul  8 12:39 sift-cli-linux
-rw-rw-r-- 1 u64 u64      333 Jul  8 12:41 sift-cli-linux.sha256.asc
u64@ubuntu64:~/Desktop$
```

```sh
u64@ubuntu64:~/Desktop$ gpg --keyserver pgp.mit.edu --recv-keys 22598A94
gpg: keyring `/home/u64/.gnupg/secring.gpg' created
gpg: keyring `/home/u64/.gnupg/pubring.gpg' created
gpg: requesting key 22598A94 from hkp server pgp.mit.edu
gpg: /home/u64/.gnupg/trustdb.gpg: trustdb created
gpg: key 22598A94: public key "SANS Investigative Forensic Toolkit <sift@computer-forensics.sans.org>" imported
gpg: Total number processed: 1
gpg:               imported: 1
u64@ubuntu64:~/Desktop$
```

```sh
u64@ubuntu64:~/Desktop$ gpg --verify sift-cli-linux.sha256.asc
gpg: Signature made Sat 08 Jul 2017 12:36:26 PM PDT using DSA key ID 22598A94
gpg: Good signature from "SANS Investigative Forensic Toolkit <sift@computer-forensics.sans.org>"
gpg: WARNING: This key is not certified with a trusted signature!
gpg:          There is no indication that the signature belongs to the owner.
Primary key fingerprint: 5D29 135B 3798 3CAC 6097  9623 15B9 AD71 2259 8A94
u64@ubuntu64:~/Desktop$
```

```sh
u64@ubuntu64:~/Desktop$ shasum -a 256 -c sift-cli-linux.sha256.asc OR sha256sum -c sift-cli-linux.sha256.asc
sift-cli-linux: OK
shasum: WARNING: 10 lines are improperly formatted
shasum: OR: No such file or directory
u64@ubuntu64:~/Desktop$
```

```sh
u64@ubuntu64:~/Desktop$ sudo mv sift-cli-linux /usr/local/bin/sift
[sudo] password for u64:
u64@ubuntu64:~/Desktop$
```

```sh
u64@ubuntu64:~/Desktop$ chmod 755 /usr/local/bin/sift
```

```sh
u64@ubuntu64:~/Desktop$ sift --help
Usage:
  sift [options] list-upgrades [--pre-release]
  sift [options] install [--pre-release] [--version=<version>] [--mode=<mode>] [--user=<user>]
  sift [options] update
  sift [options] upgrade [--pre-release]
  sift [options] version
  sift [options] debug
  sift -h | --help | -v

Options:
  --dev                 Developer Mode (do not use, dangerous, bypasses checks)
  --version=<version>   Specific version install [default: latest]
  --mode=<mode>         SIFT Install Mode (complete or packages-only) [default: complete]
  --user=<user>         User used for SIFT config [default: u64]
  --no-cache            Ignore the cache, always download the release files

u64@ubuntu64:~/Desktop$
```

```sh
u64@ubuntu64:~/Desktop$ sudo sift install --mode=packages-only
```
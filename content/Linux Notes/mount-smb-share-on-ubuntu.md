Title: Mount SMB Share on Ubuntu
Date: 2011-06-14 10:20
Tags: samba, smb, ubuntu
Slug: mount-smb-share-on-ubuntu

1. Install smb client

		sudo apt-get install smbfs smbclient

2. Mount 

		sudo mount -t cifs //server/Share /mnt/Share -o iocharset=utf8,file_mode=0777,dir_mode=0777

<http://ubuntuforums.org/showthread.php?t=280473>
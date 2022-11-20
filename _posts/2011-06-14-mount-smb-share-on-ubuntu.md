---
layout: post
title: Mount SMB Share on Ubuntu
date: 2011-06-14 10:20
tags: samba, smb, ubuntu, linux
slug: mount-smb-share-on-ubuntu
---

1. Install smb client

		sudo apt-get install smbfs smbclient

2. Mount 

		sudo mount -t cifs //server/Share /mnt/Share -o iocharset=utf8,file_mode=0777,dir_mode=0777

<http://ubuntuforums.org/showthread.php?t=280473>
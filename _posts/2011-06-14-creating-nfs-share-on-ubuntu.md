---
layout: post
title: Creating NFS Share on Ubuntu
date: 2011-06-14 10:20
tags: nfs, ubuntu, linux
slug: creating-nfs-share-on-ubuntu
---

1. Install nfs-server

		sudo apt-get install nfs-kernel-server

2. Edit /etc/exports to add share

		/srv/homes       hostname1(rw,sync,no_subtree_check) hostname2(ro,sync,no_subtree_check)

3. Export share
				
		sudo exportfs -a
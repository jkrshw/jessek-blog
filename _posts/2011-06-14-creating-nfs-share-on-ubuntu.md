Title: Creating NFS Share on Ubuntu
Date: 2011-06-14 10:20
Tags: nfs, ubuntu, linux
Slug: creating-nfs-share-on-ubuntu

1. Install nfs-server

		sudo apt-get install nfs-kernel-server

2. Edit /etc/exports to add share

		/srv/homes       hostname1(rw,sync,no_subtree_check) hostname2(ro,sync,no_subtree_check)

3. Export share
				
		sudo exportfs -a
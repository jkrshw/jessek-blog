Title: Diskless ubuntu upgrades
Date: 2011-05-10 10:20
Tags: ubuntu, linux
Slug: diskless-ubuntu-upgrades

To upgrade ubuntu off line or to reduce the amount of duplicate data downloaded when upgrading multiple ubuntu machines download the alternate install cd iso, mount it and do the upgrade as if you'd burnt the cd

1. Download alt cd iso <http://ftp.citylink.co.nz/ubuntu-releases/11.04/>

2. Mount the iso to /media/iso

		sudo mkdir /media/iso
		sudo mount ~/Downloads/ubuntu-11.04-alternate-i386.iso /media/iso -t iso9660 -o loop

3. Run the CDROM upgrade

		gksu /media/iso/cdromupgrade
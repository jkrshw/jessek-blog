---
layout: post
title: Riding the bleeding edge
date: 2014-01-23 10:20
tags: linux, ssd, steamos, ubuntu
slug: riding-bleeding-edge
---

It has been quite some time since I tried hacking around with Linux. Which also means it has been a long time of my HTPC working just fine.

The HTPC is an old Core 2 Duo in an Antec case running Ubuntu 13.10. I've tried XBMC and Myth TV but nothing has worked better than the Nautilus file browser and sensible folder structure. There is a DVB card inside that I've had some success recording HD content with but I'm not a fan of waiting for New Zealand channels to broadcast content and haven't used it much.

With the recent early beta (alpha?) release of [Steam OS](http://store.steampowered.com/steamos/download) I thought I'd get my hands dirty and mess around with the set up. I'd read a few guides that stated the installation would wipe all disks. Since spinning disk hard drives are cheap these days and SSDs have come down a lot in price I bought a 120 GB Samsung SSD for the OS and a 4 TB WD drive for storage/backups.

## Unboxing

![Boxed](|filename|/images/ssd-boxed.jpg)

I was not surprised to see the case had accumulated quite a lot of dust. The two existing hard drives are attached to a little removable caddie at the front of the case.

![Dusty Vents](|filename|/images/ssd-dusty.jpg)

Dusty vents

Shortly after removing the SSD from it's box I realised my first mistake. I'd forgotten just how small SSDs are and how old the case was. The SSD wasn't going to fit in to the caddie. It was way too small. Just my luck, the last SSD I'd purchased almost turned into a [small expensive brick](http://jessek-dev.blogspot.co.nz/2012/08/broken-sata-port-on-ssd.html) when I tried to install it.

Not to be defeated so easily I considered a few options and decided to borrow a cradle from my desktop case, utilise the unused CD-ROM cage in the Antec case and a few cable ties to keep everything in place.

![Seems legit](|filename|/images/ssd-yup.jpg)

Seems legit

## Installation

The official Steam OS installer required a [UEFI](http://en.wikipedia.org/wiki/Unified_Extensible_Firmware_Interface) compatible motherboard. No biggie, the community have already worked around this small hurdle with an ISO that adds non-uefi support and the ability to manually specify partitions. This [Reddit post](http://w3.reddit.com/r/SteamOS/comments/1sww9o/download_nonuefi_bootable_iso_with_manual/) provides the instructions:

1. Download the [iso torrent](magnet:?xt=urn:btih:b3b02f9f63013a4928a0d4043eecad564cb4d836&dn=SteamOSInstaller%5FManualPartitioning.iso:)
2. Write ISO to a USB drive

	sudo dd if=SteamOSInstaller_ManualPartitioning.iso of=/dev/sdX

3. Boot from USB
4. When the installer fails to mount the cdrom, drop to the shell and mount the USB drive

	mount /dev/sdX /cdrom
5. Select option to Detect and mount CD-ROM to continue

![Steam OS](|filename|/images/ssd-steam.jpg)

So far so good

After getting past the CD-ROM issue the installer ran through the step to install the base system. Unfortunately that is as far as it got. An unspecified error kept occurring while trying to configure the repository. Skipping the step and choosing to configure grub would give me a system I could boot in to but that was about it.

Searching for the error suggests it is a network related issue. Basic trouble shooting seemed to verify this and after a few attempts I'd run out of... steam. 

With complete defeat staring me in the face I settled on a compromise. I installed Ubuntu on the SSD and transferred the contents of the 2 old 1 TB drives to the new 4 TB drive. Now the system, that is almost always on, boots faster and I've got twice the space with half the number of spinning disks. Not a complete failure.

I haven't given up on Steam OS but I suspect I'll be upgrading a bit more hardware before I try again. As for riding the bleeding edge? Maybe my best days are behind me..
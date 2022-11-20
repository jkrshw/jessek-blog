---
layout: post
title: Ubuntu Latest Nvidia Drivers
date: 2011-08-19 16:47
tags: cuda, nvidia, ubuntu, ppa, linux
slug: nvidia-driver-ppa
---

CUDA programming requires the latest nvidia drivers. Manually installing the drivers from the nvidia website causes headaches after a kernel upgrade.

The swat-x PPA provides the latest versions of x.org drivers. These are stable drivers, not bleeding edge.

https://launchpad.net/~ubuntu-x-swat/+archive/x-updates

http://ubuntuforums.org/showpost.php?p=11166698&postcount=7:
To upgrade using this PPA, run these commands in the Terminal:

```bash
$ sudo add-apt-repository ppa:ubuntu-x-swat/x-updates
$ sudo apt-get update
$ sudo apt-get upgrade
```

If you need/want to remove those PPA and downgrade the concerning packages again, run these:

```bash
$ sudo apt-get install ppa-purge
$ sudo ppa-purge ppa:ubuntu-x-swat/x-updates
```
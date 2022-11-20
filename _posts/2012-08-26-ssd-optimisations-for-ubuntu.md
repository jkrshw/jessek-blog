---
layout: post
title: SSD optimisations for Ubuntu
date: 2012-08-26 10:20
tags: grub, optimisation, ssd, ubuntu
slug: ssd-optimisations-for-ubuntu
---

With my SSD still working despite the taped up data port it's time to do some tweaks to squeeze out the most performance I can.

## Mount Options

First up we modify the mount points to disable access time writes and enable TRIM

Edit /etc/fstab and add noatime,discard, to the options for the SSD partitions:

	# / was on /dev/sdb3 during installation 
	UUID=dbdb75e7-13d0-4894-8923-0b0d018dad4a / ext4 discard,noatime,errors=remount-ro 0 1

By default Linux writes to a file's metadata whenever the file is accessed. This is important for some applications such as mail servers, assuming you're not running a mail server it will be fine to disable.

TRIM helps the SSD know which blocks are no longer in use and can be wiped.

##I/O Scheduler

A slightly more interesting tweak is to change the I/O Scheduler used to control how the kernel reads and writes to disk.

You can check the current scheduler by viewing the contents of /sys/block/sdX/queue/scheduler. Replace X with the letter corresponding your your device. For me the SSD is device sdb.

	$ cat /sys/block/sdb/queue/scheduler
	noop [deadline] cfq

The default is cfq. This is the "Completely Fair Queueing" scheduler and it provides the best performance for regular hard disks. The noop and deadline schedulers are better for SSDs. The [] indicate the current scheduler in use. As you can see I've gone with the deadline scheduler.

The scheduler can be modified on the fly by echoing the desired scheduler to /sys/block/sdb/queue/scheduler

	$ echo deadline | sudo tee /sys/block/sdb/queue/scheduler

For more permanent solution, some sites recommend modifying rc.local to perform the above command on start up. I'm not a fan of these sort of setups in general so preferred a different approach.

If you only have SSDs then you can add a setting to the grub config to set the default scheduler. Add the option elevator=deadline in /etc/default/grub

	$ sudo vim /etc/default/grub
	...
	GRUB_CMDLINE_LINUX_DEFAULT="quiet splash elevator=deadline"

	...
	$ sudo update-grub

If you've got a mix of SSDs and regular drives like me then you can install the sysfsutils package and modify the /etc/sysfs.conf configuration file.

	$ sudo apt-get install sysfsutils
	$ sudo vim /etc/sysfs.conf
	...
	block/sdb/queue/scheduler = deadline

After a restart you can check which scheduler is in use by viewing /sys/block/sdb/queue/scheduler

	$ cat /sys/block/sdb/queue/scheduler
	noop [deadline] cfq

## Resources

* [How do I optimize the OS for SSDs?](http://askubuntu.com/questions/1400/how-do-i-optimize-the-os-for-ssds)
* <http://www.drbd.org/users-guide/s-latency-tuning.html>
* [SSD benchmark of I/O schedulers](http://ubuntuforums.org/showthread.php?t=1464706)
* [How to enable TRIM?](http://askubuntu.com/questions/18903/how-to-enable-trim)
* [Linux I/O disk elevator](http://www.gnutoolbox.com/linux-io-elevator/)
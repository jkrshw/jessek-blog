Title: LaTeX \includegraphics causes font rendering problems
Date: 2012-06-05 10:20
Tags: crash, gpu, logs, nouveau, nvidia, ubuntu
Slug: nvidia-driver-falling-off-bus

## NVIDIA driver falling off the bus

After purchasing some new hardware I was disappointed to find that my new machine would crash randomly every hour or so, seemingly more so while playing games. Something I was quite looking forward to doing.

Using Ubuntu 12.04 with an NVIDIA graphics card I suspected that the fault was graphics driver related. The machine was completely unresponsive when it crashed. I couldn't start an ssh session or ALT+F1 to a terminal to see what was happening.

I had a look through the logs and found this in /var/log/kern.log immediately before the logs finished

NVRM: GPU at 0000:01:00.0 has fallen off the bus.

After a quick google I found a few results that suggested putting the driver in to persistence mode.

	sudo nvidia-smi -pm 1

If that does the trick the change can be made permanent by adding the following line to /etc/rc.local before the exit 0

	/usr/bin/nvidia-smi -pm 1

<http://www.cyberciti.biz/faq/debian-ubuntu-rhel-fedora-linux-nvidia-nvrm-gpu-fallen-off-bus/>


## Stop the press

In a typical case of counting my chickens before they hatch my pc froze in the middle of writing this update. Other sites have suggested updating the NVIDIA driver or switching to the open source driver nouveau. Since I want to be able to play the odd game of Left 4 Dead 2 without having to boot in to windows I'll try updating the driver to the very latest before resorting to nouveau.

## Update - 29 Aug 2012

The more things I tried the more I was convinced the problem was hardware related. After changing some RAM settings I decided that it was at fault. Swapped the DIMMs around and have not had a crash since!
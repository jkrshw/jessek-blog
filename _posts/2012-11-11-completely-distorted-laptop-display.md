---
layout: post
title: Completely distorted laptop display
date: 2012-11-11 10:20
tags: edid laptop nvidia ubuntu xorg
slug: completely-distorted-laptop-display
---

I've installed Ubuntu so many times now and seen the process improve so much over the past few years that I thought replacing Windows 7 with Ubuntu 12.10 would be a piece of cake. Sadly I was wrong.

The issues I encountered were related to the discrete NVIDIA graphics card in the laptop. They were unrelated to similar issues around new laptops with 2 graphics cards for power saving, [NVIDIA Optiums](http://en.wikipedia.org/wiki/Nvidia_Optimus).

## Black screen on start up

Shortly in to the loading of the Ubuntu installation the screen goes black and doesn't come back. This is caused by a new kernel options trying to use the graphics card to improve the resolution and image quality during boot.

It is fairly easy to fix. During the start up of installation enable the nomodeset option under "F6 Other Options"

After installation it is likely that you will have to do this again to boot into your new system and install the proprietary nVidia driver. During boot up, press shift to bring up the grub options and navigate to the Ubuntu, with Linux ... option and hit e to edit. Find the line that starts with linux and change the options quite splash to nomodeset. Press ctrl+x to boot with the modified options.

See more detailed instructions with screenshots over at [AskUbuntu](http://askubuntu.com/questions/162075/my-computer-boots-to-a-black-screen-what-options-do-i-have-to-fix-it/162076#162076).

## Installing the proprietary nVidia driver

The installation process has got very good for adding restricted third party drivers but I found that they weren't installed correctly unless I had the linux-header-generic package installed first.

```
$ sudo apt-get install linux-header-generic
$ sudo apt-get install nvidia-current
$ sudo nvidia-xconfig
```

## Distorted display - EDID issues

This was the real time waster. After installing Ubuntu and the NVIDIA drivers I booted up hopefully only to have my good mood crushed by the completely garbled display. I heard the Ubuntu login noise but all I saw were black and white vertical lines.

I thought I was stuck. It seemed hopeless from here and I actually contemplated installing a copy of Win 8 I have from the University access to MSDN. Thankfully I held off on that and after some reading I realised I was actually very close. The driver HAD installed correctly, but the [EDID](http://en.wikipedia.org/wiki/Extended_display_identification_data) being reported by the laptop monitor was corrupted.

Checking /var/log/Xorg.0.log I found the line
The EDID read for display device DFP-0 is invalid: the  checksum for EDID version 1 is invalid.
Along with the raw EDID block in hex. Converting the hex back to binary and using parse-edid (installed with sudo apt-get install read-edid) I was able to get the correctly display mode for the monitor and then using the [modeline calculator](http://arachnoid.com/modelines/index.html) I generated the appropriate modeline for my display and added it to the Monitor section of /etc/X11/xorg.conf (always make a backup before modifying)

```
Section "Monitor"
  Identifier     "Monitor0"
  VendorName     "Unknown"
  ModelName      "Unknown"
  HorizSync       28.0 - 33.0
  VertRefresh     43.0 - 72.0
  Option         "DPMS"
  Modeline "1368x768_60.00" 85.86 1368 1440 1584 1800 768 769 772 795 -HSync +Vsync
EndSection
```

In the Display section I added a reference to the new mode

```
Section "Screen"
  Identifier     "Screen0"
  Device         "Device0"
  Monitor        "Monitor0"
  DefaultDepth    24
  SubSection     "Display"
    Depth       24
    Modes "1368x768_60.00"
  EndSubSection
EndSection
```

The last step was to add an option to ignore the bad checksum from the EDID to the Device section

```
Section "Device"
  Identifier     "Device0"
  Driver         "nvidia"
  VendorName     "NVIDIA Corporation"
  Option "IgnoreEDIDChecksum" "DFP"
EndSection
```

And with all of that my laptop is up and running with 3D accelerated graphics and it looks great.

![Fixed Display](/images/ubuntu-laptop-display.png)

## Resources

* Ignore checksum - <http://forums.freebsd.org/archive/index.php/t-23821.html>
* Modeline calculator - <http://arachnoid.com/modelines/index.html>
* Process EDID - <http://analogbit.com/fix_nvidia_edid>
* <http://forum.xbmc.org/showthread.php?tid=114518>
* <http://ubuntuforums.org/archive/index.php/t-1857772.html>
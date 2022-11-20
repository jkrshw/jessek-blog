---
layout: post
title: Everything is borke
date: 2011-12-20 10:20
tags: broken, linux, nvidia, ubuntu
slug: everything-is-borke
---

After upgrading to the 3.0 Linux kernel everything broke. This was somewhat anticipated and I had put it off until after my dissertation was due to avoid any extra stress.

The suspected cause was the nvidia dev driver I was using for Open CL GPU programming. I knew there would be a need to recompile of the kernel modules. What wasn't anticipated was that I wouldn't be able to boot in to a proper recover console and everything else would start breaking... soon after upgrading the PC wouldn't get much past the grub menu and wouldn't boot from a usb drive so I couldn't reinstall Ubuntu. At this point I gave up and left the PC for a month because I could use my laptop instead.

On trying once again to fix my PC I discovered the fairies had made things worse. Now no signal was coming from graphics card.

After a good 4 hours I was able to get signal from the graphics card, boot from a usb driver and re-install Ubuntu. Here are the things I did (in order) that may or may not have contributed to getting things back up and running:

1. Removed graphics card and vacuumed dust,
2. Vacuumed dust off CPU and case fans,
3. Removed CMOS battery for ~2 minutes,
4. Swapped RAM DIMMs to spare slots
5. After swapping the ram the PC returned to the (broken) state that it was when I first left it, except for some reason I could now boot from a USB drive and re-install Ubuntu.  

As a result of having separate partitions for home and root I didn't lose any personal data or settings and only had to re-install my favourite apps to get back up and running. 
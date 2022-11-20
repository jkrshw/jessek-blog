---
layout: post
title: Flashing BIOS with FreeDos Live USB
date: 2012-11-11 10:20
tags: bios, freedos, linux, ubuntu
slug: flashing-bios-with-freedos-live-usb
---

The bios flasher utility for my Acer Aspire laptop requires a windows or dos installation to run.

Having just recently installed Ubuntu 12.10 I wasn't keen to go back so I did some searching and found that the FreeDos USB disk can be used to run the flash utility.

Remember that flashing the bios can be risky. Make sure you have the correct bios for your computer and don't blame me if anything goes wrong.

## Create bootable USB

Download and extract the FreeDos img file and use unetbootin to create a bootable USB disk from the image. At first I tried to use the start up disk creator that comes with Ubuntu but it kept failing. Apparently it only supports creating Ubuntu live disks.

If unetbootin isn't installed you can install it from this ppa:

	$ sudo apt-add-repository ppa:gezakovacs/ppa
	$ sudo apt-get install unetbootin

Create the live disk:

	$ unetbootin

![unetbootin](/images/flash-unetbootin.png)

## Flash BIOS with Live USB

Copy the bios updater to the usb disk and then reboot. I placed it in a folder called bios. Make sure the current bios settings are set up to boot from USB.

During set up FreeDos will ask you to confirm the date and time, just hit enter twice and you'll be at the C prompt.

	C:\

Change to the directory with updater, which will probably be D drive:

	C:\ d:
	D:\ cd bios

Run the bios flasher bat file:

	D:\BIOS bios

Follow the instructions and wait while it does the update. Make sure you're connected to AC power, you do NOT want the battery to die in the middle of a flash.
---
layout: post
title: Unable to vnc to server because of gnome-keyring
date: 2011-03-26
tags: gnome, ubuntu, vnc, linux
slug: unable-to-vnc-to-server-because-of
---

Unable to vnc to server because of gnome-keyring

The vnc server vino uses the gnome keyring to store passwords in a secure way.  With automatic login the keyring is not unlocked and so the user is prompted to enter the password.  This makes it impossible to login remotely to a machine with no keyboard.

This bug report suggests a fix by reverting to the gnome-conf storage system for passwords <https://bugs.launchpad.net/ubuntu/+source/vino/+bug/562423>

Security was not a major issues for me so I removed the need for a password by navigating to System ->  Preferences -> Remote Desktop and unchecking 'Require the user to enter this password'
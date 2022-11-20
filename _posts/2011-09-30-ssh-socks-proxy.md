---
layout: post
title: SSH Socks Proxy
date: 2011-09-30 16:37
tags: ssh proxy linux
slug: ssh-socks-proxy
---

More SSH goodness.

To set up a SOCKS proxy over ssh simply run 
```bash
$ ssh -D 1080 user@example.com
``` 

and set your browser's SOCKS proxy settings to point to ```localhost:1080```

* [SSH Tunnel + SOCKS Proxy Forwarding = Secure Browsing](http://embraceubuntu.com/2006/12/08/ssh-tunnel-socks-proxy-forwarding-secure-browsing/)
* [SSH/OpenSSH/PortForwarding](https://help.ubuntu.com/community/SSH/OpenSSH/PortForwarding)

I found this really handy for downloading research journals using the university's subscriptions while not havin to head in to campus. 

Title: Using scp through a DMZ gateway to a machine behind a firewall using a tunnel
Date: 2011-10-01 10:20
Tags: proxy, ssh
Slug: ssh-socks-proxy

More SSH goodness.

To set up a SOCKS proxy over ssh simply run ```ssh -D 1080 user@example.com``` and set your browser's SOCKS proxy settings to point to localhost:1080


<http://embraceubuntu.com/2006/12/08/ssh-tunnel-socks-proxy-forwarding-secure-browsing/>

<https://help.ubuntu.com/community/SSH/OpenSSH/PortForwarding>

To download academic papers from home using the universities subscriptions

	ssh -D 1080 jker040@login.cs.auckland.ac.nz
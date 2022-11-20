Title: Using scp through a DMZ gateway to a machine behind a firewall using a tunnel
Date: 2011-09-18 10:20
Tags: firewall, linux, scp, ssh, ssh tunneling
Slug: using-scp-through-dmz-gateway-to

How to set up port forwarding from your local machine to a remote machine behind a firewall through a gateway machine.

Commands are run on your local machine.

IP addresses obviously need to be replaced with the actual addresses or host names of the target pc.

First you setup port forwarding through an intermediary. This forwards your localhost port 2222 to port 22 on 192.168.1.100. Remember, that 192.168.1.100 is not on your local network; 192.168.1.100 is on the LAN network shared with 208.77.188.166. 

	ssh -f -N -q -L 2222:6.7.8.9:22 user@1.2.3.4
	scp -P 2222 transformers.avi user@localhost:.

A diagram might help. Remember, port 22 is the SSH server port on the 192.168.1.100 machine.

	+-------------+        +--------------+        +--------------+
	|     your    |        |  remote DMZ  |        |   server on  |
	|local machine|        |    server    |        |  remote LAN  |
	|             |        |   1.2.3.4    |        |    6.7.8.9   |
	|         2222:  >-----|              |------->:22            |
	|             |        |\____________/|        |              |
	|             |        |              |        |              |
	+-------------+        +--------------+        +--------------+
 
<http://www.noah.org/wiki/SSH_tunnel>

To send files to to csgpu01 behind the UoA firewall:

	ssh -f -N -q -L 2222:csgpu01.cs.auckland.ac.nz:22 jker040@login.cs.auckland.ac.nz
	scp -P 2222 Dropbox/Development/hons/workspace/ac.nz.auckland.hons.gpu/src/vertex.cl jker040@localhost:/home/jker040/ac.nz.auckland.hons.gpu/src
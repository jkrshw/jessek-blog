Title: Mythweb Broken in Ubuntu 12.10 Quantal Quetzal
Date: 2013-02-17 10:20
Tags: apache, mythtv, mythweb, ubuntu
Slug: mythweb-broken-in-ubuntu-1210-quantal

Deciding to resurrect my Mythbox I can a quick sudo mythfilldatabase and then checked mythweb to see what was in the listings. Not surprisingly I was greeted with a rather plain error page indicating a server error occurred while trying to process my request. Oh well, at least something was running.

Not sure what logs to check I started with the mythtv logs

	tail -f /var/log/mythtv/*

No errors. Next apache:

	less /var/log/apache2/error.log:

	[Sun Feb 17 16:39:00 2013] [error] [client 192.168.1.5] PHP Warning:  Unknown: function '0' not found or invalid function name in Unknown on line 0
	[Sun Feb 17 16:39:00 2013] [error] [client 192.168.1.5] PHP Fatal error:  Call-time pass-by-reference has been removed in /usr/share/mythtv/bindings/php/MythBase.php on line 50

Googling the error pointed me at the [bug report](http://code.mythtv.org/trac/ticket/10504) and a helpfully titled forum post  [[SOLVED] 12.10 MythWEb PHP Fatal Error](http://ubuntuforums.org/showthread.php). The bug report included a patch and the forum post had simple instructions on downloading and applying the patch. It turns out Mythweb isn't compatible with PHP 5.4.0. This is easily patched and hopefully will be included in the next Mythweb. For now run the following to download and apply the patch.

	wget http://code.mythtv.org/trac/raw-attachment/ticket/10504/MythBase.php.patch
	wget http://code.mythtv.org/trac/raw-attachment/ticket/10504/sorting.php.patch
	wget http://code.mythtv.org/trac/raw-attachment/ticket/10504/schedules.php.patch
	wget http://code.mythtv.org/trac/raw-attachment/ticket/10504/tv-schedules.php.patch
	sudo patch --backup /usr/share/mythtv/bindings/php/MythBase.php MythBase.php.patch
	sudo patch --backup /usr/share/mythtv/mythweb/includes/sorting.php sorting.php.patch
	sudo patch --backup /usr/share/mythtv/mythweb/modules/tv/schedules.php tv-schedules.php.patch
	sudo patch --backup /usr/share/mythtv/mythweb/modules/tv/tmpl/default/schedules.php schedules.php.patch

Reloading the mythweb page <http://localhost/mythweb> displayed the mythweb home page and we're back in action. Now to do something about the horrible skin..

![MythTV Fixed](|filename|/images/mythweb.png)
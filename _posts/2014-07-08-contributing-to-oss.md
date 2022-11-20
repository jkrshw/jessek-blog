---
layout: post
title: Contributing to OSS
date: 2014-07-08 09:13
tags: oss community
slug: contributing-to-oss
published: false
---

I've been a fan of Open Source Software for a long time. Free stuff built by smart people sounds like an awesome idea. My friends, family and anyone foolish enough to ask for tech support from me invariably ends up with Ubuntu installed. They may complain about not being able to install x, y or z, but they're virus free and I've yet to see a real case where they couldn't be as productive with Ubuntu as they could with Windows.

Early in my software career I knew I wanted to contribute something back to the OSS community. A coworker I looked up to had contributed fixes to a web cam driver and that seemed awesome. I wanted in. But how?? I'm not a kernel hacker, I don't know anything about image processing or writing a text editor. The barrier to entry seemed way too high.

Then my career and other hobbies filled up my time and I forgot about it.

Community
---------

Fast forward a few years and github has become huge, I've discovered a world outside Java and all the communities that go with each language.

The communities are key. Look out for small libraries that might be useful and start using them. You'll find a use case or an annoying bug that others might benefit from and that you can fix. Maybe you found the documentation a bit lacking when you were trying to get set up. You can fix that and save the next person the pain you just went through. If you can't fix a bug, maybe you can document it and help test it when someone else fixes it. Learn to raise good issues so that someone else can fix the issue. Attaching tests and patches to your issues will go a long way in getting that issue addressed.

<blockquote class="twitter-tweet" lang="en"><p>OH: github issues is where bugs and feature requests go to die</p>&mdash; あさり (@hiro_asari) <a href="https://twitter.com/hiro_asari/statuses/458613847986040832">April 22, 2014</a></blockquote>

When I moved my blog from blogger I had a choice between the Ruby based Jekyll and the Python based Pelican. Going with Pelican has been really fun, partly because I feel the community is a little smaller. It is easier to find [small features](https://github.com/getpelican/pelican-plugins/pull/218) that are missing or even [improvements to documentation](https://github.com/getpelican/pelican-plugins/pull/212)!

Communication
-------------

Chances are you have a few different ideas about how something should be done. Submitting a Pull Request without providing context of why it's a good idea is a good way to get your PR closed.

Talking through your requirements and being prepared to make compromises will help make your contribution a success.

My first [Pull Request](https://github.com/togglz/togglz/pull/72) was related to a project at work. The library was well designed but assumed a fairly static runtime. With some investigation I found a way to meet my use case and not complicate the current design. We were able to talk it through and it was merged!

Sometimes there is going to be a use case that you really want but it takes the project in a direction the maintainer is unwilling to go. You may have to accept this and move on. If you really need the functionality, maintain a fork. Who knows, the maintainer may have a change of heart and merge the commits later.

Ethics
------

I never felt I had to contribute to OSS in order to get a job. [Ashe Dryden](https://twitter.com/ashedryden) has a post on the [Ethics of unpaid labor](http://www.ashedryden.com/blog/the-ethics-of-unpaid-labor-and-the-oss-community) that outlines why this requirement is a bad and unfair idea.

[Brendan Forster](https://twitter.com/shiftkey) did a great talk on the topic of this very post at [Codemania](https://www.youtube.com/watch?v=VE5lss9SEPw) this year. He talked a little about the barrier to entry. I too am White, Male in my late 20s and a native English speaker. While I felt the barrier to entry high when I was younger, I was able to age a little and suddenly fit in. I think Brendan was maybe a little too easy on the OSS community. He kindly suggested the OSS Community should be polite. Under his breath says "Don't be a dick". So let me emphasise that a bit more. *Don't be a dick.*

Work
----

My next challenge is how to apply the OSS model of contributions to a framework I help maintain at work. The original contributors have moved on to other projects and it's got to the point where our teams are only capable of maintaining the core feature set. Feature requests often get turned down or we reply with a generic "Please contribute this." response and hope for the best. That's probably a post for another time though...

<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

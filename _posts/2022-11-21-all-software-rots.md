---
layout: post
title: All software rots
date: 2022-11-21 10:20
tags: software legacy debt rot
slug: all-software-rots
---

Software starts to rot as soon as it's written. The sooner we realise that a line of code is no longer
needed, the cheaper its overall maintenance will be. Ideally during the planning phase of a feature
we rule out unnecessary code. Sometimes it's not until the code review that we realise what was just
written is not needed. It's easy to think, well the code is already written so we might as well deploy
it. This might be true if the most expensive part of development is writing a line of code, but when
we consider the overall cost of maintaining the code, the upfront development is probably closer to
a quarter of the cost or less!

The cheapest line of code to write is one that is immediately deleted. Once a feature is deployed the 
rot starts to set in. The longer it lives, the deeper the rot. Software requires constant maintenance 
to stay healthy, and eventually it's better off being deleted.

So when you write that line of code, always ask yourself if it needs to exist.

Of course we shouldn't just stop writing code, but it needs to have purpose and value. Most teams
working on a successful product have a difficult to maintain legacy solution that runs some critical
part of the product. Fortunately it doesn't require much maintenance but when it does the team
treads very carefully through the code base, trying not to disturb the delicate balance. For a while,
it may pay off to keep the service running, perhaps the product strategy is to move away from the
capability it provides, and the risk of it failing is acceptable. If the capability is critical to 
the business strategy at some stage a rewrite will probably be necessary. For small systems the
rewrite may be able to done as a 1-1 replacement. I've found that a 1-1 replacement for large complex
systems leads to massive delays and extra costs, and it's better to take a feature by feature approach.

This is all to say that, after 5 years of not writing a blog post here, my [Continuos Blog](/2014/05/continuous-blog.html) set up
had completely rotted through. Python had finally moved on to v3, the pelican static site generator 
seems to have lost all steam and [Travis CI](https://www.travis-ci.com/pricing/) eliminated the free tier.

Fortunately the set up is not too complex so it could be replaced all at once. I've migrated it over
to [Jekyll](https://jekyllrb.com/), built and deployed using Github actions thanks to <https://pagertree.com/2021/04/20/github-actions/>
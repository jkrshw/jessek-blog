---
layout: post
title: Thoughts from a Code Maniac
date: 2013-04-15 10:20
tags: codemania, javascript, js, test
slug: thoughts-from-code-maniac
---

While I'm still digesting the recent (and awesome) [codemania](http://codemania.co.nz/) conference I thought I'd share my notes taken during the talks.

## Glenn Block

Open source at Microsoft

* Microsoft is not necessarily 100% evil (imo it is probably still mostly evil)

## Paul Fenwick

All your brains suck: Off topic talk on how easy it is to fool your brain

* Reality delivers worse than "worst case"
* Team mates have more predictive power than you at estimating how long it will take you to complete a task
* Anonymous self estimation produces more accurate responses
* Q. Should you trust your past self? A. Probably not.
* [HabitRPG](https://habitrpg.com/static/front) might be a fun way to promote good habits
* Good tools can make testing fun
* - people like to do fun things
* - testing can suck because it is no fun
* Pair up, use your brain before starting a task

## Walter Rumsby - JS Test

Dispelling the Fear, Uncertainty & Doubt Around Unit Testing JavaScript.

* Q. How do I do it? A. **Just DO IT!**
actually pretty easy
* If you're afraid of the command line...don't be afraid of the command line
* Tools: quint, yui test, jasmine, mocha
* Use modules
* Assert library: chai
* Assert expected vs actual values instead of true/false
* [PhantomJS](http://phantomjs.org/) is OK. (headless webkit for JS testing)
* Faster feedback is better than x-browser testing
* Node.js tooling - shifter - grunt
* [Rebecca Murphy](http://rmurphey.com/)
* Abstract dom events to an API - dom events aren't interesting
* Istanbull - code coverage (warning: might hurt your feelings)
* [Katrina Owen](http://kytrinyx.com/)

## Amy Palamountain

Unsuck your backbone

* Don't build large JS Apps - Build modules
* UI Modules or Logic modules
* Ask for a resource, never take
* Group modules at right level
* Chatter & events vulnerable to bugs
* Air traffic control pattern - Single app that receives events and broadcasts as appropriate
* MV* not scalable without additional structure (i.e. [backbone](http://backbonejs.org/))

## Katie Miller

Monads to the Rescue

* This talk lost a few people along the way. Fair bit of technical details in the middle made seeing the value difficult for newbies. More on the awesome things you get once you have a Monad would have been great.
* Java 8 will make functional programming easier (in java)
* Monads are awesome
* Best way to introduce people to functional programming is to add it in small pieces to existing code

## Darren Wood

The Modern Webmonkey - Talk to the tools of the trade for designers

* I should have read the description for this one. Not what I was expecting but a good talk
* Photoshop plugins make web design easier. Sprite generator, colour pickers
* Compress/optimise pngs is easy and very worthwhile
* [Sublime](http://www.sublimetext.com/) rocks - column editing, emmet (zen coding)

## Paul Betts

On Programming

* I didn't agree with opening point that developing software is not engineering (who says engineering can't be art?) and the analogy between art and software wasn't quite nailed.
* Lots of interesting ideas to think about though. I particularly liked the idea of considering the approach to software development by looking at other disciplines (art and architecture)
* Considering what message you want to convey with your code, and that messages are clearer without so much detail transferred very nicely to software.

All the speakers were amazing. It was awesome being able to listen to a lot of inspiring people and share a drink or two with them after the conference. A+ conference, would attend again.
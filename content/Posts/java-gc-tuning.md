Title: Java GC Tuning
Date: 2015-04-03 14:02
Tags: java, gc, contracting
Slug: jvm-gc-tuning

JVM Garbage Collection wasn't something I'd ever had to worry about. Until recently. GC is a target of many jokes but in my experience it had always worked "good enough". That is, I'd never had the need for a large heap and high throughput.

That changed when I started contracting at a company working on a project to replace their aging CMS with a heavily customised CMS from Adobe. CQ, now called Adobe Experience Manager, is a java based CMS built on top of the felix OSGI container and the JCR Jackrabbit. I joined the project shortly before performance testing, after the project was considered dev complete (hah!).

My first task was to investigate the JVM memory settings, which quickly led to my first finding. The JVM max heap size was 40GB. Yikes. This was coupled with a dozen GC tuning settings. All foreign to me and noone in the project knew who set them or why.

Java Garbage Collection has change a lot over the years and there are plenty of atricles with tuning tips and suggestions. Some relevant, some terribly out of date.

I'll sumarise the main points I learned.

Logging
-------

Capturing metrics is incredibly important for performance tuning and general monitoring. There are a few different logging options that generate log messages whenever a GC occurs.

I had success for these options, although I found some produced output that was not compatible with HP JMeter.

    -Xloggc:gc-`date +"%m-%d-%y-%T"`.log # output to file gc-date-time.log
    -XX:+PrintGCDateStamps # Include pretty date-time in gc logs. Useful for analysis over time so anomalies can be compared to real world
events.
    -XX:+PrintGCDetails # Print additional GC details. Cannot be used with HP Jmeter.
    -XX:+PrintTenuringDistribution # Print details of young gen and old gen tenure. Cannot be used with HP Jmeter.

Heap Spaces
-----------

The JVM heap is split up into different heap spaces. In simple terms, there is the Young gen and the Old gen. Newly created objects are stored in the young gen and are eventually promoted through to the old gen as the survive minor GCs. The Young gen is further split up into the new space and survivor space.

While monitoring the GC data during performance testing we found that our app produced *A LOT* of garbage. This is not highly unexpected from an app that handles many short lived web requests but it would have been nice to try address some of the hot spots. 

Without obvious leaks there wasn't much evidence to suggest easy wins here so instead we ramped up the size of the young gen space so to reduce the frequency of minor GCs and promotion of objects into the old space. 

Monitoring also showed that the heap size after a full GC was quite low, indicating that we could safely reduce the size of the heap from the extremly large 40GB to the still very large 16GB without risking any Out of Memory exceptions.

One of the preexisting optimisations was to set the Max Tenuring Threshold to 2. That is, after 2 GCs surviving objects would be promoted to the old gen space. This option was far too aggressive and resulted in unnecessary overhead promoting objects and heap fragmentation making minor GCs very expensive.

Garbage Collection Algorithms
-----------------------------

Given the different nature of objects in the young gen vs the old gen space, it makes sense that there are different GC algorithms for each.

In Java 7 (yes we're still on 7) there are two main choices for the major GC algorithm. Concurrent Mark Sweep (CMS) and the Throughput Collector. CMS performs most of it's work in the background so it's often used for applications where pauses times are to be minimised, however it performs slower overal. The throughput collector will do it's work in a stop the world event which results in longer pauses but overall less than the CMS, so it's good for situations where overall throughput is desirable such as long running calculations.

As an application repsonding to web requests to serve content, the CMS collector with shorter pauses was chosen.
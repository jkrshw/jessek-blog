---
layout: post
title: MKV to Chromecast
date: 2017-07-19 20:17
tags: mkv, chromecast, ffmpeg, linux
slug: mkv-to-chromecast
---

I bought a Chromecast so I could wirelessly stream video from my PC to my TV. I don't have a 4k TV and don't intend to buying one anytime soon, so the standard Chromecast seemed reasonable.

I hadn't done much research into the Chromecast and had assumed it would be fairly straight forward to stream content from a video player such as VLC. Unfortunatly this isn't the case.

I had some success with the [Videostream](http://getvideostream.com/) app for Chrome, but was annoyed by the buffering caused by playing 1080p content.

If the video you wish to play is enocded with a codec [supported](https://developers.google.com/cast/docs/media) by Chrome, e.g H.264 or VP8 video with AAC or MP3 audio, you can use ffmpeg to change container formats without having to transcode the video. 

To check the codec information in Ubuntu, right click on the file and view the properties under the Audio/Video tab

![Audio/Video properties](|filename|/images/audio-video-properties.png)

Use ffmpeg to change the container format

    ffmpeg -i input.mkv -codec copy output.mp4

Source <https://askubuntu.com/a/195346>

Drag the resulting mp4 into a Chrome window and use the Chromecast extension to cast to your device. No more buffering and no long wait for a transcode! 

If the audio format is not supported, e.g. AC-3

![Audio AC-3](|filename|/images/audio-video-ac-3.png)

Use ffmpeg to re-encode the audio with the aac codec and leave the video as is

    ffmpeg -i input.mkv -c:v copy -c:a aac -b:a 160k -strict -2 output.mp4

The `-strict -2` is necessary in Ubuntu 16.04 as the aac encoder is experiemental in the version of ffmpeg in the standard repos. In the latest version it is no longer experiemental and the extra flag is not needed.

Source <https://trac.ffmpeg.org/wiki/Encode/AAC>
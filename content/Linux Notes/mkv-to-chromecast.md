Title: MKV to Chromecast
Date: 2017-07-19 20:17
Tags: mkv, chromecast, ffmpeg
Slug: mkv-to-chromecast

I bought a Chromecast so I could wirelessly stream video from my PC to my TV. I don't have a 4k TV and don't intend to buying one anytime soon, so the standard Chromecast seemed reasonable.

I hadn't done much research into the Chromecast and had assumed it would be fairly straight forward to stream content from a video player such as VLC. Unfortunatly this isn't the case.

I had some success with the [Videostream](http://getvideostream.com/) app for Chrome, but was annoyed by the buffering caused by playing 1080p content.

If the video you wish to play is enocded with a codec supported by Chrome, e.g as H.264 or VP8 with AAC or MP3 audio, you can use ffmpeg to change container formats without having to transcode the video. 

    ffmpeg -i input.mkv -codec copy output.mp4

Source <https://askubuntu.com/a/195346>

Drag the resulting mp4 into a Chrome window and use the Chromecast extension to cast to your device. No more buffering and no long wait for a transcode. You can check the codec information from Ubuntu by right clicking on the file and viewing the properties

![Audio/Video properties](|filename|/images/audio-video-properties.png)

If the source video format is [supported](https://developers.google.com/cast/docs/media), converting from mkv to mp4 without transcoding is a super quick and easy to way to reliably stream content to your Chromecast. 
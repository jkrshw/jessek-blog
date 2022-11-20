Title: Ubuntu nvidia TV out
Date: 2011-03-25
Tags: ubuntu, nvidia, linux
Slug: ubuntu-nvidia-tv-out
Summary: Enabling tv out on an nvidia graphics card by editing xorg.conf 

Enabling tv out on an nvidia graphics card by editing xorg.conf 

1. Backup xorg.conf

        sudo cp /etx/X11/xorg.conf /var/backups/xorg.conf.orig

2. Add to Device section of xorg.conf

        Option         "TVOutFormat" "SVIDEO"
        Option         "TVStandard" "PAL-BG"

3. Restart gdm

        sudo service gdm restart

Full xorg.conf ubuntu 10.10

```
Section "Screen"
        Identifier      "Default Screen"
        DefaultDepth    24
EndSection

Section "Module"
        Load    "glx"
EndSection

Section "Device"
        Identifier      "Default Device"
        Driver          "nvidia"
        Option          "NoLogo"        "True"
        Option          "TwinView"
        Option          "TwinViewOrientation" "Clone"
        Option          "TVOutFormat" "SVIDEO"
        Option          "TVStandard" "PAL-BG"
EndSection
```

Source <https://help.ubuntu.com/community/NvidiaTVOut>
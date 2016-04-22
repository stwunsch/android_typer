# android_typer
Small program to type on your Android device using your computer keyboard

Works most likely only under Linux!

How to setup the adb daemon and your Android device
----------------------------------------------------

Download adb (Android Debug Bridge) for your system and test the connection to
your device.

First, enable the debug mode by tapping multiple times on the entry in
Settings/About Phone/Build number. Then go to Settings/Developer options
and enable Android debugging. Now, you can connect your device via USB to the
computer.

Next, try to test the connection using following command:

$ adb devices -l

You should see something like this (dependent on your device):

$ List of devices attached  
$ 04d07b88064f4d7f       device usb:2-3 product:occam model:Nexus_4 device:mako

Apparently, everything worked! Otherwise you need probably an udev rule on your
machine. To employ this, read in the cyanogenmod wiki about it [0].

Run the program
---------------

That's simple:

$ python3 android_typer.py

Probably you want to to set a symbolic link to integrate it into your system:

$ ln -s /path_to_android_typer/android_typer.py /usr/bin/android_typer

Dependencies
------------

You need python 3, appropriate tkinter package for the GUI and adb.

Links
-----

[0] https://wiki.cyanogenmod.org/w/UDEV

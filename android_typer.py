#!/usr/bin/env python3

""" Connector class which talks to the android device """

import subprocess
import re
import sys

class connector:
    name = None # Device name

    """ Setup the connector (find device) """
    def __init__(self):
        # Look for devices
        s = subprocess.check_output(["adb", "devices", "-l"]).decode()
        # Find model name
        m = re.search(".* model:(.+) ", s, re.MULTILINE)
        # Name device if possible, otherwise print error
        if m!=None:
            self.name = m.group(1)
        else:
            print("[ERROR] Device name not found.", file=sys.stderr)
            sys.exit()

    """ Wake device up """
    def wakeup(self):
        s = subprocess.call(["adb", "shell", "input", "keyevent", "26"])

    """ Write text to device """
    def write(self, text):
        # Replace some characters to fit the adb input command
        text_send = text
        text_send = text_send.replace(" ", "\ ")
        text_send = text_send.replace(")", "\)")
        text_send = text_send.replace("(", "\(")
        text_send = text_send.replace("/", "\/")
        text_send = text_send.replace("!", "\!")
        text_send = text_send.replace("?", "\?")
        text_send = text_send.replace(":", "\:")

        # Send text to device if the text is not empty, otherwise send return
        if text!="":
            s = subprocess.call(["adb", "shell", "input", "text", text_send])
        else:
            s = subprocess.call(["adb", "shell", "input", "keyevent", "66"])

""" Inteface class for text input """

import tkinter as tk

class interface:
    root = tk.Tk() # Main window
    device = None # Android device

    """ Place elements on the main window """
    def __init__(self, device):
        # Set device
        self.device = device

        # Set entry element for text input
        self.entry = tk.Entry(self.root, width = 50)
        self.entry.grid(row=1, column=0, sticky="ew")

        # Make the entry sticky
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)

        # Set binding for pressing <Return> to send text to device
        self.entry.bind("<Return>", self.press_return)

        # Set button element to wakeup device
        self.button = tk.Button(self.root, text="Wake up!", command=device.wakeup)
        self.button.grid(row=1,column=1)

    """ Define callback for pressing <Return> in entry text field """
    def press_return(self, event):
        # Send text to device
        self.device.write(self.entry.get())

        # Delete text in entry
        self.entry.delete(0, 'end')

    """ Set device name in title """
    def set_device_name(self, device_name):
        self.root.title("Device: "+device_name)

    """ Run the mainloop """
    def run(self):
        self.root.mainloop()

""" Main program"""

# Setup device
dev = connector()

# Setup gui
gui = interface(dev)
gui.set_device_name(dev.name)

# Enter main loop
gui.run()

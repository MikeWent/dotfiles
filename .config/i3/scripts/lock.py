#!/usr/bin/env python3

import subprocess
from os import pipe, remove, mkdir
from time import strftime

wallpaper_path = "/home/mike/Wallpapers/satellite-1920.png"
photo_dir_path = "/home/mike/.lockphotos"

# check is block running now
block_pid = subprocess.run(["pidof", "block"], capture_output=True).stdout.decode()
if block_pid != "":
    exit(1)

# create directory for photos
try:
    mkdir(photo_dir_path)
except FileExistsError:
    pass

# create pipe for reading lockscreen output
read_p, write_p = pipe()

lock_process = subprocess.Popen(
    ["block", wallpaper_path, "-l", "ffffff88", "-a", "Roboto Condensed", "-r", "2", "-F", "%H:%M", "-s", "72", "-X", "30", "-Y", "990", "-x", "230", "-y", "1016"],
    stdout=write_p,
    stderr=write_p
)

with open(read_p, "r") as buf:
    while lock_process.poll() == None:
        message = buf.readline()
        if message == "Permission denied\n":
            # make a photo with webcam
            new_photo_filename = "{}/{}.jpg".format(photo_dir_path, strftime("%Y-%m-%d_%H:%M:%S"))
            subprocess.run(
                ["fswebcam", "-c", "/etc/fswebcam.conf", new_photo_filename]
            )
        if message == "Authentication success\n":
            break


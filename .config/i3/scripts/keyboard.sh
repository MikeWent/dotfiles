#!/bin/bash

# Set up keyboard layout (US, RU) and bind switch to CpasLock
# (ordinary CapsLock behavior is activated by Shift+CapsLock)
setxkbmap -layout $1,ru -option grp:caps_toggle

# Increase key repeat speed and decrease time after keypress before repeating the key
xset r rate 250 30

# Bind Insert key (118) to Compose key (Multi_key)
xmodmap -e 'keycode 118 = Multi_key'

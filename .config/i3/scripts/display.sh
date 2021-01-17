#!/bin/bash
xrdb -merge ~/.Xresources
xset s off -dpms
g="1.0.5"; b="0.85"; xcalib -c;# xcalib -a -red $g $b 100 -blue $g $b 100 -green $g $b 100

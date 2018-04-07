#!/bin/bash

# i3
mkdir -p ~/.config/i3
cp i3.config ~/.config/i3/config

# dunst
mkdir -p ~/.config/dunst
cp dunstrc ~/.config/dunst/dunstrc

# vscode
mkdir -p ~/.config/Code/User
cp vscode.json ~/.config/Code/User/vscode.json

# xfce4-terminal
mkdir -p ~/.config/xfce4/terminal
cp xfce4-terminalrc ~/.config/xfce4/terminal/terminalrc

# telegram white icons
cp -r ticons/* ~/.local/share/TelegramDesktop/tdata/ticons/

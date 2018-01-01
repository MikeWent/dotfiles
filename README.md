# dotfiles

What included:

- Visual Studio Code
- i3
- dunst
- xfce4-terminal
- Telegram white notification icons

## How to install

```bash
# i3
mkdir -p ~/.config/i3
ln i3.config ~/.config/i3/config

# dunst
mkdir -p ~/.config/dunst
ln dunstrc ~/.config/dunst/dunstrc

# vscode
mkdir -p ~/.config/Code/User
ln vscode.json ~/.config/Code/User/vscode.json

# xfce4-terminal
mkdir -p ~/.config/xfce4/terminal
ln xfce4-terminalrc ~/.config/xfce4/terminal/terminalrc

# telegram white icons
cp -r ticons/* ~/.local/share/TelegramDesktop/tdata/ticons/
```

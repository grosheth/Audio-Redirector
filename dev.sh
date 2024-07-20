#!/usr/bin/env bash

cd ~/work/Audio-Redirector || exit 1

kitty --detach nvim ~/work/Audio-redirector >/dev/null

# Ordering desktop
# bspc node -d 0
# bspc desktop -f DP-4

# Starting dev env
nix-shell shell.nix

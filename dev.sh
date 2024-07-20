#!/usr/bin/env bash

cd ~/work/Audio-Redirector || exit 1

kitty --detach nvim ~/work/Audio-redirector >/dev/null

nix-shell shell.nix

---
title: First Days on Arch: Switching Super + T to Ghostty (With Help from Reddit)
date: 2026-11-13
summary: Getting Docker running without sudo, figuring out what "Windows + T" is called in Hyprland, and tuning Ghostty based on r/Ghostty favorites.
tags: [arch-linux, hyprland, ghostty, docker]
---

Once I finished bringing up Arch Linux on my ThinkPad X13—wiring up `mesa`, `vulkan-intel`, `pipewire`, `uwsm`, and `end-4/dots-hyprland` (*illogical-impulse*)—the first real test was making it feel like *my* machine instead of someone else's dotfiles.

Right away I ran into two tiny day-one hurdles. First, Docker wasn't running out of the box—on Arch, installing a package doesn't auto-start its daemon, so I had to enable `docker.service` via `systemctl` and add my user to the `docker` group so I wouldn't need `sudo` on every container command.

Second, pressing **Windows + T** kept opening `kitty`, even though I wanted to move full-time to **Ghostty**. When I asked `agy` how to map `alpha + T` (and quickly corrected myself—*Windows + T*, not `Alt + T`), I learned two things about my setup:

1. Hyprland calls the Windows key **`SUPER`**.
2. My config wasn't using standard `.conf` files at all—it was running Lua (`keybinds.lua` and `variables.lua`), where `SUPER + T` launched a `terminal` variable defaulting to `kitty`.

Updating `SUPER + T` (and setting `terminal = "ghostty"` in `variables.lua`) got Ghostty opening immediately, which sparked the next question: *what do people on `r/Ghostty` actually put in their config?*

After checking community favorites through `agy`, I settled on a clean borderless setup in `~/.config/ghostty/config.ghostty`:

```ini
theme = Catppuccin Mocha
font-size = 13
background-opacity = 0.95
window-padding-x = 12
window-padding-y = 12
gtk-titlebar = false

mouse-hide-while-typing = true
copy-on-select = true
shell-integration = detect
confirm-close-surface = false
```

Plus one tip worth remembering for later: `send-env = COLORTERM` whenever SSHing into remote boxes that don't recognize Ghostty's `terminfo` yet. Validating it with `ghostty +validate-config` was my first small Arch win.

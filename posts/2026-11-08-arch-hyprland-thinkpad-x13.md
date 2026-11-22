---
title: Why I Run Arch Linux + Hyprland on My ThinkPad X13
date: 2026-11-08
summary: How I went from a bare Arch install to Hyprland + uwsm + illogical-impulse on a ThinkPad X13 Gen 1, and why this combo clicked for me.
tags: [arch-linux, hyprland, thinkpad, linux]
---

When I set up Arch Linux on my **Lenovo ThinkPad X13 Gen 1**, I didn't want a bloated desktop environment—I wanted something fast, keyboard-driven, and clean enough to stay out of my way while still looking great. That led me straight down the **Arch + Hyprland** rabbit hole.

## Starting Minimal on Arch

I started from a clean base, bringing up only the essentials first:

* **Graphics & Hardware Video:** `mesa`, `vulkan-intel`, and `intel-media-driver` for Comet Lake UHD Graphics.
* **Wayland Audio & Portals:** `pipewire`, `pipewire-pulse`, `pipewire-alsa`, `wireplumber`, and `xdg-desktop-portal-hyprland`.
* **AUR Helper:** Cloned and built `yay-bin` manually with `makepkg -si`.
* **Compositor & Session:** Started with `hyprland` directly, then moved to `uwsm start hyprland` with `sddm` so systemd user units and environment variables stay clean.

## Landing on `end-4/dots-hyprland` (*illogical-impulse*)

Rather than hand-writing every bar, lockscreen, notification daemon, and clipboard tool from scratch, I cloned [`end-4/dots-hyprland`](https://github.com/end-4/dots-hyprland) (*illogical-impulse*).

What makes this particular setup special is **Quickshell** (`illogical-impulse-quickshell-git`) combined with **`uwsm`**:

* You get crisp widgets, notifications, media controls, a built-in keybind cheatsheet, and smooth Wayland animations out of the box.
* Idle RAM stays around **~3.3 GiB** out of `15 GiB`, leaving plenty of room for Docker containers, IDEs, and browser tabs.

Once it was installed, I trimmed out a few default pieces I didn't need (like `kitty`, `dolphin`, and extra KDE integration packages) and settled on **`ghostty`** as my terminal and **`yazi`** in the terminal for browsing files.

## Why Arch + Hyprland Works So Well Together

People often ask why this specific pairing is everywhere right now. For me it comes down to three things:

| Setup | What Changes with Arch + Hyprland |
| --- | --- |
| **vs. Fixed-Release Distros** | Hyprland moves quickly. Arch's rolling release gives you the latest Hyprland, kernel, and Mesa updates right away—plus the AUR has every Wayland companion tool ready to install. |
| **vs. X11 WMs (`i3`, `bspwm`)** | Native Wayland means zero screen tearing, clean fractional scaling / multi-monitor support, and built-in blur/animations without maintaining a separate `picom` config. |
| **vs. GNOME / KDE Plasma** | Far lower idle overhead and full control via plain-text configs, without fighting a heavy desktop shell. |

The trade-off is simple: because both Arch and Hyprland evolve fast, I keep `~/dots-hyprland` handy before big `pacman`/`yay` upgrades so config changes don't catch me off guard. So far, it's been worth every minute.

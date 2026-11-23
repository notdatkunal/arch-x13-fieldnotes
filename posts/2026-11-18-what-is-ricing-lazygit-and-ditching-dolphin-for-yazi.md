---
title: Learning What "Ricing" Means—and Trading KDE Bloat for lazygit & yazi
date: 2026-11-18
summary: Searching for GitHub Desktop on Linux led me to lazygit, meta-package dependency puzzles, and replacing Dolphin with yazi in the terminal.
tags: [arch-linux, hyprland, ricing, lazygit, yazi]
---

Coming to Linux, one of the first apps I looked for was **GitHub Desktop**—specifically something keyboard-friendly where I could customize bindings. When I found out there's no official Linux build, `agy` pointed me toward **`lazygit`** paired with `gh`, both of which were *already* installed on my machine.

That made me pause and ask a basic question I hadn't actually settled in my head yet: *"What do we even call what I'm running here—is this a desktop environment or ricing?"*

Getting the ecosystem mapped out clicked everything into place: **Hyprland** isn't a bundled Desktop Environment like GNOME or KDE—it's just the Wayland compositor, **Quickshell** handles my bar and widgets, and assembling/tuning the pieces around dotfiles is what people call **ricing**. Better yet, I realized I didn't want anything GUI-heavy at all; a fast TUI-first setup fit me much better.

So I went looking for leftover bloat to remove—and immediately ran into Arch's dependency guardrails:

1. First I tried `sudo pacman -Rns kitty kactivitymanagerd plamsa-browser-integration`—and promptly misspelled `plasma` as `plamsa`.
2. Fixing the typo revealed the real catch: `kitty` was required by the `illogical-impulse-fonts-themes` meta-package, and `kactivitymanagerd` was required by `plasma-workspace`.
3. Before removing `plasma-browser-integration` on its own, I double-checked what it actually did (mostly KDE media controls, KRunner tab search, and KDE Connect browser tab sharing—nothing I needed inside Hyprland).

That left **`dolphin`**, the GUI file manager. When I asked if I could replace it with a terminal tool, **`yazi`** won immediately—Vim-style `h/j/k/l` navigation, spacebar selection, `y/x/p` copy-cut-paste, and native image previews right inside Ghostty.

Why was `dolphin` locked in by dependencies? Only because of an optional `illogical-impulse-kde` wrapper package. Pointing `fileManager` in `variables.lua` to `ghostty -e yazi` and running:

```bash
sudo pacman -S yazi
sudo pacman -Rns illogical-impulse-kde dolphin
```

cleaned out the last GUI file manager I wasn't using and made my workflow almost completely keyboard-driven.
